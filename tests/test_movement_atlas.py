#!/usr/bin/env python3
"""Movement atlas contracts in tools/validate.py.

The fixtures in this module are deliberately minimal and independent of the
repository's real canonical content.  The four W012-W015 checks are exercised
as pure functions; integration-only behavior uses an isolated temporary tree.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import re
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

spec = importlib.util.spec_from_file_location(
    "movement_validate", REPO_ROOT / "tools" / "validate.py"
)
validate_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_mod)


MOVEMENT_TAXONOMY = {
    "publication_status": {"draft", "published"},
    "claim_status": {"supported"},
    "action_status": {"actionable"},
    "evidence_profile": {"direct"},
    "mobility_decision": {"evidence-gap", "not-routine"},
    "action_reference_frame": {"joint-local", "body-fixed", "poolside-fixed"},
}

MOVEMENT_IDS = {
    "action_ids": "movement.action.shoulder-complex",
    "muscle_ids": "movement.muscle.rotator-cuff",
    "demand_ids": "movement.demand.freestyle-recovery",
    "intervention_ids": "movement.intervention.scapular-control",
}

# derived_from_ids 指向 movement 以外的既有 canonical 記錄。
CANONICAL_IDS = {"free.tech.6", "starts-turns.tech.27"}

def make_warnings():
    return {
        code: []
        for code in (
            "W012", "W013", "W014", "W015", "W016", "W017", "W018", "W019"
        )
    }


def make_errors():
    return {"E010": []}


def make_taxonomy():
    """Build the on-disk shape expected by load_taxonomy()."""
    return {
        "schema_version": 1,
        "domain": "_meta",
        "description": "movement atlas test taxonomy",
        "fields": {
            field: {
                "controlled": True,
                "review_status": "reviewed",
                "values": [{"key": value} for value in sorted(values)],
            }
            for field, values in MOVEMENT_TAXONOMY.items()
        },
    }


def make_sources(source_ids=None):
    return {
        "schema_version": 1,
        "domain": "_meta",
        "description": "movement atlas test sources",
        "sources": [{"id": sid} for sid in (source_ids or [])],
    }


def make_published_entry(
    eid: str, *, intervention: bool = False, demand: bool = False
):
    entry = {
        "id": eid,
        "publication_status": "published",
        "claim_status": "supported",
        "action_status": "actionable",
        "evidence_profile": "direct",
        # evidence-gap 會被 W016 要求配 do-not-prescribe，用它當通用 fixture
        # 會讓所有正向案例都變成 W016 案例，故預設用 not-routine。
        "mobility_decision": "not-routine",
    }
    if demand:
        entry["derived_from_ids"] = sorted(CANONICAL_IDS)[:1]
        # poolside-fixed 是不需要分節段量測的取值，讓通用 fixture 不必
        # 為了通過 W018 而假造 source_ids。
        entry["action_reference_frame"] = "poolside-fixed"
    if intervention:
        entry.update(
            {
                "affirmative_conclusion": "Use the intervention conditionally.",
                "works_when": ["the limitation matches"],
                "fails_when": ["the limitation does not match"],
                "how_to_identify": "Compare active and passive findings.",
                "action": "Retest after the intervention.",
                "remaining_boundary": "Individual response still varies.",
            }
        )
    return entry


def run_movement_checks(documents):
    """Apply the same document-to-entry adaptation used by run_validation()."""
    warnings = make_warnings()
    movement_documents = []
    movement_id_set = set()

    for filename, (entry_key, expected_prefix) in (
        validate_mod.MOVEMENT_FILE_RULES.items()
    ):
        data = documents.get(filename)
        raw_entries = data.get(entry_key) if isinstance(data, dict) else None
        entries = (
            [
                (index, entry)
                for index, entry in enumerate(raw_entries)
                if isinstance(entry, dict)
            ]
            if isinstance(raw_entries, list)
            else []
        )
        movement_documents.append((filename, entry_key, expected_prefix, entries))
        movement_id_set.update(
            entry["id"]
            for _index, entry in entries
            if isinstance(entry.get("id"), str)
        )

    for rel, entry_key, expected_prefix, entries in movement_documents:
        validate_mod.check_movement_id_names(
            rel, entry_key, entries, expected_prefix, warnings
        )
        validate_mod.check_movement_taxonomy(
            rel, entry_key, entries, MOVEMENT_TAXONOMY, warnings
        )
        validate_mod.check_movement_references(
            rel, entry_key, entries, movement_id_set, CANONICAL_IDS, warnings
        )
        validate_mod.check_movement_published_completeness(
            rel, entry_key, entries, warnings
        )
        validate_mod.check_mobility_evidence_gap(
            rel, entry_key, entries, warnings
        )
        validate_mod.check_action_reference_frame(
            rel, entry_key, entries, warnings
        )
        validate_mod.check_measurement_conditions(
            rel, entry_key, entries, {"src.example"}, warnings
        )

    return warnings


class MovementFixtureTestBase(unittest.TestCase):
    """Create an isolated canonical tree and point validate_mod at it."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.canonical_dir = self.root / "canonical"
        self.movement_dir = self.canonical_dir / "movement"
        self.drills_dir = self.root / "Drills"
        self.reports_dir = self.root / "reports"
        self.movement_dir.mkdir(parents=True)
        self.drills_dir.mkdir()

        self._original_paths = {
            name: getattr(validate_mod, name)
            for name in (
                "ROOT",
                "CANONICAL_DIR",
                "DRILLS_DIR",
                "TAXONOMY_FILE",
                "SOURCES_FILE",
                "REPORTS_DIR",
                "MOVEMENT_DIR",
            )
        }

        validate_mod.ROOT = self.root
        validate_mod.CANONICAL_DIR = self.canonical_dir
        validate_mod.DRILLS_DIR = self.drills_dir
        validate_mod.TAXONOMY_FILE = self.canonical_dir / "_taxonomy.yaml"
        validate_mod.SOURCES_FILE = self.canonical_dir / "_sources.yaml"
        validate_mod.REPORTS_DIR = self.reports_dir
        validate_mod.MOVEMENT_DIR = self.movement_dir

        self._write_yaml(validate_mod.TAXONOMY_FILE, make_taxonomy())
        self._write_yaml(validate_mod.SOURCES_FILE, make_sources())
        self._write_yaml(self.drills_dir / "_categories.yaml", {})
        for filename, (entry_key, _prefix) in (
            validate_mod.MOVEMENT_FILE_RULES.items()
        ):
            self._write_yaml(self.movement_dir / filename, {entry_key: []})

    def tearDown(self):
        for name, value in self._original_paths.items():
            setattr(validate_mod, name, value)
        self.tmp.cleanup()

    def _write_yaml(self, path: Path, data):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.dump(data, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )

    def _run_validation(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exit_code = validate_mod.run_validation()
        return exit_code, stdout.getvalue(), stderr.getvalue()

    def assert_code_count(self, output: str, code: str, expected: int):
        match = re.search(rf"\b{re.escape(code)}: (\d+) 筆", output)
        self.assertIsNotNone(match, f"找不到 {code} 摘要：\n{output}")
        self.assertEqual(int(match.group(1)), expected, output)

    def assert_movement_counts(self, output: str, expected=None):
        expected = expected or {}
        for code in ("W012", "W013", "W014", "W015"):
            self.assert_code_count(output, code, expected.get(code, 0))


class TestMovementPositive(unittest.TestCase):
    def test_four_valid_published_records_pass_all_checks(self):
        action = make_published_entry(MOVEMENT_IDS["action_ids"])
        muscle = make_published_entry(MOVEMENT_IDS["muscle_ids"])
        demand = make_published_entry(MOVEMENT_IDS["demand_ids"], demand=True)
        intervention = make_published_entry(
            MOVEMENT_IDS["intervention_ids"], intervention=True
        )

        for entry in (action, muscle, demand, intervention):
            entry.update(
                {
                    "action_ids": MOVEMENT_IDS["action_ids"],
                    "muscle_ids": [MOVEMENT_IDS["muscle_ids"]],
                    "demand_ids": MOVEMENT_IDS["demand_ids"],
                    "intervention_ids": [MOVEMENT_IDS["intervention_ids"]],
                }
            )

        warnings = run_movement_checks(
            {
                "actions.yaml": {"actions": [action]},
                "muscle-groups.yaml": {"muscle_groups": [muscle]},
                "stroke-demands.yaml": {"demands": [demand]},
                "interventions.yaml": {"interventions": [intervention]},
            }
        )

        self.assertEqual(warnings, make_warnings())


class TestW012MovementIdNames(unittest.TestCase):
    def _check(self, eid):
        warnings = make_warnings()
        validate_mod.check_movement_id_names(
            "canonical/movement/actions.yaml",
            "actions",
            [(0, {"id": eid})],
            "movement.action.",
            warnings,
        )
        return warnings["W012"]

    def test_wrong_file_namespace_warns(self):
        messages = self._check("movement.muscle.shoulder")
        self.assertEqual(len(messages), 1)
        self.assertIn("命名空間違規", messages[0])

    def test_uppercase_segment_warns(self):
        messages = self._check("movement.action.Shoulder")
        self.assertEqual(len(messages), 1)
        self.assertIn("段格式違規", messages[0])

    def test_underscore_segment_warns(self):
        messages = self._check("movement.action.shoulder_complex")
        self.assertEqual(len(messages), 1)
        self.assertIn("shoulder_complex", messages[0])

    def test_numeric_segment_warns(self):
        messages = self._check("movement.action.shoulder.120")
        self.assertEqual(len(messages), 1)
        self.assertIn("'120'", messages[0])

    def test_valid_and_hyphenated_segments_do_not_warn(self):
        for eid in (
            "movement.action.shoulder",
            "movement.action.shoulder-complex.external-rotation2",
        ):
            with self.subTest(eid=eid):
                self.assertEqual(self._check(eid), [])


class TestW013MovementTaxonomy(unittest.TestCase):
    def _check(self, entry):
        warnings = make_warnings()
        validate_mod.check_movement_taxonomy(
            "canonical/movement/actions.yaml",
            "actions",
            [(0, entry)],
            MOVEMENT_TAXONOMY,
            warnings,
        )
        return warnings["W013"]

    def _assert_invalid_field_warns(self, field):
        messages = self._check(
            {"id": "movement.action.test", field: "not-in-taxonomy"}
        )
        self.assertEqual(len(messages), 1)
        self.assertIn(f"{field}=", messages[0])

    def test_invalid_publication_status_warns(self):
        self._assert_invalid_field_warns("publication_status")

    def test_invalid_claim_status_warns(self):
        self._assert_invalid_field_warns("claim_status")

    def test_invalid_action_status_warns(self):
        self._assert_invalid_field_warns("action_status")

    def test_invalid_evidence_profile_warns(self):
        self._assert_invalid_field_warns("evidence_profile")

    def test_invalid_mobility_decision_warns(self):
        self._assert_invalid_field_warns("mobility_decision")

    def test_valid_values_do_not_warn(self):
        entry = make_published_entry("movement.action.test")
        self.assertEqual(self._check(entry), [])

    def test_missing_controlled_fields_do_not_warn(self):
        self.assertEqual(self._check({"id": "movement.action.test"}), [])

    def test_invalid_value_nested_deeply_warns(self):
        entry = {
            "id": "movement.action.test",
            "public": {"evidence": [{"claim_status": "not-in-taxonomy"}]},
        }
        messages = self._check(entry)
        self.assertEqual(len(messages), 1)
        self.assertIn("public.evidence[0].claim_status", messages[0])


class TestW014MovementReferences(unittest.TestCase):
    def _check(self, entry, movement_ids=None, canonical_ids=None):
        warnings = make_warnings()
        validate_mod.check_movement_references(
            "canonical/movement/actions.yaml",
            "actions",
            [(0, entry)],
            set(movement_ids or MOVEMENT_IDS.values()),
            set(canonical_ids or CANONICAL_IDS),
            warnings,
        )
        return warnings["W014"]

    def test_external_bridge_resolving_outside_movement_does_not_warn(self):
        entry = {
            "id": "movement.demand.test",
            "derived_from_ids": ["free.tech.6"],
        }
        self.assertEqual(self._check(entry), [])

    def test_external_bridge_unresolvable_warns(self):
        entry = {
            "id": "movement.demand.test",
            "derived_from_ids": ["free.tech.99999"],
        }
        messages = self._check(entry)
        self.assertEqual(len(messages), 1)
        self.assertIn("目標 ID 不存在於 canonical", messages[0])

    def test_external_bridge_pointing_into_movement_warns_direction(self):
        entry = {
            "id": "movement.demand.test",
            "derived_from_ids": [MOVEMENT_IDS["action_ids"]],
        }
        messages = self._check(entry)
        self.assertEqual(len(messages), 1)
        self.assertIn("方向錯", messages[0])

    def test_external_bridge_empty_list_does_not_warn(self):
        entry = {"id": "movement.demand.test", "derived_from_ids": []}
        self.assertEqual(self._check(entry), [])

    def test_unresolvable_scalar_reference_warns(self):
        messages = self._check(
            {
                "id": "movement.action.owner",
                "action_ids": "movement.action.does-not-exist",
            }
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("無法解析", messages[0])
        self.assertNotIn("命名空間錯", messages[0])

    def test_unresolvable_list_references_warn_for_each_target(self):
        messages = self._check(
            {
                "id": "movement.action.owner",
                "muscle_ids": [
                    "movement.muscle.missing-one",
                    "movement.muscle.missing-two",
                ],
            }
        )
        self.assertEqual(len(messages), 2)
        self.assertTrue(all("無法解析" in message for message in messages))

    def test_existing_wrong_namespace_scalar_warns(self):
        messages = self._check(
            {
                "id": "movement.action.owner",
                "action_ids": MOVEMENT_IDS["muscle_ids"],
            }
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("命名空間錯", messages[0])
        self.assertNotIn("無法解析", messages[0])

    def test_existing_wrong_namespace_list_warns(self):
        messages = self._check(
            {
                "id": "movement.action.owner",
                "action_ids": [MOVEMENT_IDS["muscle_ids"]],
            }
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("命名空間錯", messages[0])

    def test_each_reference_field_enforces_its_namespace(self):
        wrong_targets = {
            "action_ids": MOVEMENT_IDS["muscle_ids"],
            "muscle_ids": MOVEMENT_IDS["demand_ids"],
            "demand_ids": MOVEMENT_IDS["intervention_ids"],
            "intervention_ids": MOVEMENT_IDS["action_ids"],
        }
        for field, target in wrong_targets.items():
            with self.subTest(field=field):
                messages = self._check(
                    {"id": "movement.action.owner", field: target}
                )
                self.assertEqual(len(messages), 1)
                self.assertIn("命名空間錯", messages[0])

    def test_valid_scalar_and_list_references_do_not_warn(self):
        entry = {
            "id": "movement.action.owner",
            "action_ids": MOVEMENT_IDS["action_ids"],
            "muscle_ids": [MOVEMENT_IDS["muscle_ids"]],
            "demand_ids": MOVEMENT_IDS["demand_ids"],
            "intervention_ids": [MOVEMENT_IDS["intervention_ids"]],
        }
        self.assertEqual(self._check(entry), [])


class TestW015PublishedCompleteness(unittest.TestCase):
    def _check(self, entry, entry_key="actions"):
        warnings = make_warnings()
        validate_mod.check_movement_published_completeness(
            f"canonical/movement/{entry_key}.yaml",
            entry_key,
            [(0, entry)],
            warnings,
        )
        return warnings["W015"]

    def _assert_missing_warns(self, field, *, intervention=False):
        entry = make_published_entry(
            "movement.intervention.test"
            if intervention
            else "movement.action.test",
            intervention=intervention,
        )
        entry.pop(field)
        messages = self._check(
            entry, "interventions" if intervention else "actions"
        )
        self.assertEqual(len(messages), 1)
        self.assertIn(field, messages[0])

    def test_evidence_gap_with_actionable_status_warns(self):
        warnings = make_warnings()
        entry = make_published_entry(
            "movement.intervention.test", intervention=True
        )
        entry["mobility_decision"] = "evidence-gap"
        validate_mod.check_mobility_evidence_gap(
            "canonical/movement/interventions.yaml",
            "interventions",
            [(0, entry)],
            warnings,
        )
        self.assertEqual(len(warnings["W016"]), 1)
        self.assertIn("do-not-prescribe", warnings["W016"][0])

    def test_evidence_gap_with_dosage_sources_warns(self):
        warnings = make_warnings()
        entry = make_published_entry(
            "movement.intervention.test", intervention=True
        )
        entry["mobility_decision"] = "evidence-gap"
        entry["action_status"] = "do-not-prescribe"
        entry["dosage_source_ids"] = ["src.example"]
        validate_mod.check_mobility_evidence_gap(
            "canonical/movement/interventions.yaml",
            "interventions",
            [(0, entry)],
            warnings,
        )
        self.assertEqual(len(warnings["W016"]), 1)
        self.assertIn("dosage_source_ids", warnings["W016"][0])

    def test_honest_evidence_gap_does_not_warn(self):
        warnings = make_warnings()
        entry = make_published_entry(
            "movement.intervention.test", intervention=True
        )
        entry["mobility_decision"] = "evidence-gap"
        entry["action_status"] = "do-not-prescribe"
        entry["dosage_source_ids"] = []
        validate_mod.check_mobility_evidence_gap(
            "canonical/movement/interventions.yaml",
            "interventions",
            [(0, entry)],
            warnings,
        )
        self.assertEqual(warnings["W016"], [])

    def test_evidence_gap_check_ignores_non_interventions(self):
        warnings = make_warnings()
        entry = make_published_entry("movement.demand.test", demand=True)
        entry["mobility_decision"] = "evidence-gap"
        validate_mod.check_mobility_evidence_gap(
            "canonical/movement/stroke-demands.yaml",
            "demands",
            [(0, entry)],
            warnings,
        )
        self.assertEqual(warnings["W016"], [])

    def test_published_demand_missing_derived_from_ids_warns(self):
        entry = make_published_entry("movement.demand.test")
        messages = self._check(entry, "demands")
        self.assertEqual(len(messages), 1)
        self.assertIn("derived_from_ids", messages[0])

    def test_published_demand_with_derived_from_ids_does_not_warn(self):
        entry = make_published_entry("movement.demand.test", demand=True)
        self.assertEqual(self._check(entry, "demands"), [])

    def test_derived_from_ids_not_required_outside_demands(self):
        entry = make_published_entry("movement.action.test")
        self.assertEqual(self._check(entry, "actions"), [])

    def test_missing_claim_status_warns(self):
        self._assert_missing_warns("claim_status")

    def test_missing_action_status_warns(self):
        self._assert_missing_warns("action_status")

    def test_missing_evidence_profile_warns(self):
        self._assert_missing_warns("evidence_profile")

    def test_missing_affirmative_conclusion_warns(self):
        self._assert_missing_warns("affirmative_conclusion", intervention=True)

    def test_missing_works_when_warns(self):
        self._assert_missing_warns("works_when", intervention=True)

    def test_missing_fails_when_warns(self):
        self._assert_missing_warns("fails_when", intervention=True)

    def test_missing_how_to_identify_warns(self):
        self._assert_missing_warns("how_to_identify", intervention=True)

    def test_missing_action_warns(self):
        self._assert_missing_warns("action", intervention=True)

    def test_missing_remaining_boundary_warns(self):
        self._assert_missing_warns("remaining_boundary", intervention=True)

    def test_missing_mobility_decision_warns(self):
        self._assert_missing_warns("mobility_decision", intervention=True)

    def test_empty_string_counts_as_missing(self):
        entry = make_published_entry("movement.action.test")
        entry["claim_status"] = ""
        messages = self._check(entry)
        self.assertEqual(len(messages), 1)
        self.assertIn("claim_status", messages[0])

    def test_empty_list_counts_as_missing(self):
        entry = make_published_entry("movement.action.test")
        entry["evidence_profile"] = []
        messages = self._check(entry)
        self.assertEqual(len(messages), 1)
        self.assertIn("evidence_profile", messages[0])

    def test_non_published_entry_may_be_incomplete(self):
        entry = {
            "id": "movement.intervention.draft",
            "publication_status": "draft",
        }
        self.assertEqual(self._check(entry, "interventions"), [])

    def test_non_intervention_does_not_require_decision_fields(self):
        entry = {
            "id": "movement.action.test",
            "publication_status": "published",
            "claim_status": "supported",
            "action_status": "actionable",
            "evidence_profile": "direct",
        }
        self.assertEqual(self._check(entry, "actions"), [])


class TestW018ActionReferenceFrame(unittest.TestCase):
    """W018：demand 必須宣告 action_ids 的歸屬基準，joint-local 有自證義務。

    來源是 FR-40 裁決：「腿足維持在窄通道」（池畔可見）與「髖幾乎不做
    外展／內收」（關節角）在 YAML 上長得一樣，差別只在證據。
    """

    DEMANDS = "canonical/movement/stroke-demands.yaml"

    def _check(self, entry, entry_key="demands"):
        warnings = make_warnings()
        validate_mod.check_action_reference_frame(
            self.DEMANDS, entry_key, [(0, entry)], warnings
        )
        return warnings["W018"]

    def _demand(self, **overrides):
        entry = {
            "id": "movement.demand.free.down-kick.hip-abduction",
            "stroke": "free",
            "action_ids": ["movement.action.hip.abduction"],
            "source_ids": ["src.example"],
            "action_status": "provisional",
        }
        entry.update(overrides)
        return entry

    def test_missing_frame_warns(self):
        messages = self._check(self._demand())
        self.assertEqual(len(messages), 1)
        self.assertIn("action_reference_frame", messages[0])

    def test_joint_local_without_sources_warns(self):
        messages = self._check(
            self._demand(action_reference_frame="joint-local", source_ids=[])
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("joint-local", messages[0])

    def test_joint_local_with_sources_does_not_warn(self):
        self.assertEqual(
            self._check(self._demand(action_reference_frame="joint-local")), []
        )

    def test_do_not_prescribe_exempts_empty_sources(self):
        """誠實宣告「待驗證候選」不該被擋，與 W016 對 evidence-gap 同邏輯。"""
        self.assertEqual(
            self._check(
                self._demand(
                    action_reference_frame="joint-local",
                    source_ids=[],
                    action_status="do-not-prescribe",
                )
            ),
            [],
        )

    def test_poolside_fixed_without_sources_does_not_warn(self):
        """池畔可見描述本來就不宣稱關節角，不需要分節段量測。"""
        self.assertEqual(
            self._check(
                self._demand(
                    action_reference_frame="poolside-fixed", source_ids=[]
                )
            ),
            [],
        )

    def test_body_fixed_without_sources_does_not_warn(self):
        self.assertEqual(
            self._check(
                self._demand(
                    action_reference_frame="body-fixed", source_ids=[]
                )
            ),
            [],
        )

    def test_check_ignores_non_demands(self):
        entry = {"id": "movement.action.test"}
        self.assertEqual(self._check(entry, "actions"), [])


class TestW019MeasurementConditions(unittest.TestCase):
    """W019：demand 文字出現量化主張時必須帶完整的 measurement_conditions。

    來源是 FR-44：同一個頭位操弄，手臂體側 4–5.2%、雙臂過頭 10.4–10.9%。
    """

    DEMANDS = "canonical/movement/stroke-demands.yaml"
    SOURCES = {"src.cortesi-2015"}

    def _check(self, entry, entry_key="demands"):
        warnings = make_warnings()
        validate_mod.check_measurement_conditions(
            self.DEMANDS, entry_key, [(0, entry)], self.SOURCES, warnings
        )
        return warnings["W019"]

    def _condition(self, **overrides):
        cond = {
            "source_id": "src.cortesi-2015",
            "quantity": "head-down／aligned 相對 head-up 的被動阻力差",
            "value": "4–5.2%",
            "conditions": "手臂置於體側；水下 60 cm；被動拖曳；n=10",
            "endpoint": "passive-drag",
            "extrapolation_boundary": "不外推至水面主動自由式",
        }
        cond.update(overrides)
        return cond

    def _demand(self, text, **overrides):
        entry = {
            "id": "movement.demand.free.breathing.head-position",
            "public": {"description": text},
        }
        entry.update(overrides)
        return entry

    def test_percentage_without_field_warns(self):
        messages = self._check(self._demand("被動阻力下降 4–5.2%。"))
        self.assertEqual(len(messages), 1)
        self.assertIn("measurement_conditions", messages[0])

    def test_angle_without_field_warns(self):
        messages = self._check(self._demand("軀幹旋轉約 25–30°。"))
        self.assertEqual(len(messages), 1)

    def test_seconds_without_field_warns(self):
        messages = self._check(self._demand("持續約 0.12 s。"))
        self.assertEqual(len(messages), 1)

    def test_correlation_without_field_warns(self):
        messages = self._check(self._demand("與泳速相關 r = 0.35。"))
        self.assertEqual(len(messages), 1)

    def test_non_claim_numbers_do_not_warn(self):
        """n=15、L0–L6、2D／3D 是非主張數字，不應觸發。"""
        self.assertEqual(
            self._check(
                self._demand("以 2D 與 3D 影像分析 15 名泳者，對應 L0–L6 框架。")
            ),
            [],
        )

    def test_quantified_claim_with_complete_conditions_does_not_warn(self):
        self.assertEqual(
            self._check(
                self._demand(
                    "被動阻力下降 4–5.2%。",
                    measurement_conditions=[self._condition()],
                )
            ),
            [],
        )

    def test_empty_list_with_quantified_claim_warns(self):
        messages = self._check(
            self._demand("被動阻力下降 4–5.2%。", measurement_conditions=[])
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("空 list", messages[0])

    def test_missing_subkey_warns(self):
        cond = self._condition()
        cond.pop("extrapolation_boundary")
        messages = self._check(
            self._demand("被動阻力下降 4–5.2%。", measurement_conditions=[cond])
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("extrapolation_boundary", messages[0])

    def test_blank_subkey_warns(self):
        messages = self._check(
            self._demand(
                "被動阻力下降 4–5.2%。",
                measurement_conditions=[self._condition(conditions="   ")],
            )
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("conditions", messages[0])

    def test_unresolvable_source_id_warns(self):
        messages = self._check(
            self._demand(
                "被動阻力下降 4–5.2%。",
                measurement_conditions=[self._condition(source_id="src.nope")],
            )
        )
        self.assertEqual(len(messages), 1)
        self.assertIn("_sources.yaml", messages[0])

    def test_conditions_own_value_does_not_self_trigger(self):
        """measurement_conditions 自帶的 value 不得觸發它自己。"""
        self.assertEqual(
            self._check(
                self._demand(
                    "本筆不含量化主張。",
                    measurement_conditions=[self._condition()],
                )
            ),
            [],
        )

    def test_check_ignores_non_demands(self):
        entry = {"id": "movement.action.test", "public": {"d": "增加 4%。"}}
        self.assertEqual(self._check(entry, "actions"), [])


class TestE010MovementDiagnosticLeak(unittest.TestCase):
    def _check(self, data):
        errors = make_errors()
        validate_mod.check_public_layer_leak(
            "canonical/movement/interventions.yaml", data, errors
        )
        return errors["E010"]

    def test_three_new_movement_keys_under_public_are_errors(self):
        data = {
            "interventions": [
                {
                    "id": "movement.intervention.test",
                    "public": {
                        "active_rom": "measurement",
                        "strength_endurance_test": ["test"],
                        "limitation_classification": {"type": "mobility"},
                    },
                }
            ]
        }
        messages = self._check(data)
        self.assertEqual(len(messages), 3)
        for key in (
            "active_rom",
            "strength_endurance_test",
            "limitation_classification",
        ):
            self.assertTrue(any(key in message for message in messages))

    def test_same_movement_keys_under_diagnostic_are_allowed(self):
        data = {
            "interventions": [
                {
                    "id": "movement.intervention.test",
                    "diagnostic": {
                        "active_rom": "measurement",
                        "strength_endurance_test": ["test"],
                        "limitation_classification": {"type": "mobility"},
                    },
                }
            ]
        }
        self.assertEqual(self._check(data), [])

    def test_deeply_nested_public_movement_key_is_error(self):
        data = {
            "interventions": [
                {
                    "id": "movement.intervention.test",
                    "public": {
                        "mechanism": {
                            "details": {"passive_rom": "measurement"}
                        }
                    },
                }
            ]
        }
        messages = self._check(data)
        self.assertEqual(len(messages), 1)
        self.assertIn("public.mechanism.details.passive_rom", messages[0])


class TestE002MovementDuplicate(MovementFixtureTestBase):
    def test_same_movement_id_in_two_files_is_duplicate(self):
        duplicate_id = "movement.action.shared"
        self._write_yaml(
            self.movement_dir / "actions.yaml",
            {
                "actions": [
                    {"id": duplicate_id, "publication_status": "draft"}
                ]
            },
        )
        self._write_yaml(
            self.movement_dir / "muscle-groups.yaml",
            {
                "muscle_groups": [
                    {"id": duplicate_id, "publication_status": "draft"}
                ]
            },
        )

        exit_code, output, _stderr = self._run_validation()

        self.assertEqual(exit_code, 1)
        self.assert_code_count(output, "E002", 1)


class TestE005MovementSourceResolution(MovementFixtureTestBase):
    def _write_action_with_source(self, source_id):
        self._write_yaml(
            self.movement_dir / "actions.yaml",
            {
                "actions": [
                    {
                        "id": "movement.action.test",
                        "publication_status": "draft",
                        "source_ids": [source_id],
                    }
                ]
            },
        )

    def test_missing_source_id_is_e005(self):
        self._write_action_with_source("src.missing")

        exit_code, output, _stderr = self._run_validation()

        self.assertEqual(exit_code, 1)
        self.assert_code_count(output, "E005", 1)
        report = (self.reports_dir / "validation_report.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("src.missing", report)

    def test_registered_source_id_is_not_e005(self):
        self._write_yaml(
            validate_mod.SOURCES_FILE, make_sources(["src.registered"])
        )
        self._write_action_with_source("src.registered")

        exit_code, output, _stderr = self._run_validation()

        self.assertEqual(exit_code, 0)
        self.assert_code_count(output, "E005", 0)


class TestMovementBoundaries(MovementFixtureTestBase):
    def test_empty_arrays_do_not_raise_or_warn(self):
        exit_code, output, _stderr = self._run_validation()
        self.assertEqual(exit_code, 0)
        self.assert_movement_counts(output)

    def test_missing_entry_key_does_not_raise_or_warn(self):
        self._write_yaml(self.movement_dir / "actions.yaml", {})
        exit_code, output, _stderr = self._run_validation()
        self.assertEqual(exit_code, 0)
        self.assert_movement_counts(output)

    def test_non_list_entry_key_does_not_raise_or_warn(self):
        for raw_value in ("not-a-list", {"id": "not-a-list"}):
            with self.subTest(value_type=type(raw_value).__name__):
                self._write_yaml(
                    self.movement_dir / "actions.yaml", {"actions": raw_value}
                )
                exit_code, output, _stderr = self._run_validation()
                self.assertEqual(exit_code, 0)
                self.assert_movement_counts(output)

    def test_non_dict_list_items_do_not_raise(self):
        valid_entry = make_published_entry("movement.action.valid")
        self._write_yaml(
            self.movement_dir / "actions.yaml",
            {"actions": ["not-an-entry", None, valid_entry]},
        )
        exit_code, output, _stderr = self._run_validation()
        self.assertEqual(exit_code, 0)
        self.assert_movement_counts(output)

    def test_entry_without_id_does_not_raise(self):
        self._write_yaml(
            self.movement_dir / "actions.yaml",
            {"actions": [{"publication_status": "draft"}]},
        )
        exit_code, output, _stderr = self._run_validation()
        self.assertEqual(exit_code, 0)
        self.assert_movement_counts(output, {"W012": 1})

    def test_five_hundred_records_complete_with_correct_result(self):
        entries = [
            make_published_entry(f"movement.action.record{index}")
            for index in range(500)
        ]
        entries[-1]["claim_status"] = "not-in-taxonomy"
        self._write_yaml(
            self.movement_dir / "actions.yaml", {"actions": entries}
        )

        exit_code, output, _stderr = self._run_validation()

        self.assertEqual(exit_code, 0)
        self.assert_movement_counts(output, {"W013": 1})


if __name__ == "__main__":
    unittest.main()
