"""問題索引必須通過實際掃檔與關係收集，不能只有 YAML 可讀。"""
from tests.test_validate import FixtureTestBase, validate_mod
from collections import defaultdict
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
import io
import unittest
from unittest.mock import patch


class TestProblemRegistration(FixtureTestBase):
    def test_missing_id_is_detected_in_new_file(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "problems": [{"title": "抬頭後沉髖"}],
        })
        errors, _, _ = self._run()
        self.assertTrue(errors["E001"])

    def test_both_intervention_paths_check_real_ids(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "problems": [{"id": "prob.breast.head-lift", "links": {
                "interventions": ["movement.intervention.missing"],
                "water_interventions": ["movement.intervention.water-missing"],
            }}],
        })
        errors, warnings, _ = self._run()
        self.assertEqual(2, len(errors["E003"]))
        self.assertFalse(warnings["W005"])

    def test_empty_problem_file_does_not_create_entries(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "categories": [], "problems": [],
        })
        errors, _, count = self._run()
        self.assertEqual(0, count)
        self.assertFalse(errors["E001"])

    def test_truncated_file_fails_real_validator(self):
        path = self.canonical_dir / "instructional/problems.yaml"
        path.parent.mkdir()
        path.write_text("problems: [\n", encoding="utf-8")
        with patch.object(validate_mod, "MOVEMENT_DIR", self.canonical_dir / "movement"), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            code = validate_mod.run_validation()
        self.assertEqual(1, code)
        report = (self.reports_dir / "validation_report.md").read_text(encoding="utf-8")
        self.assertIn("unreadable problem YAML", report)


class TestProblemContract(unittest.TestCase):
    def setUp(self):
        self.doc = {"domain": "instructional", "sub": "problems", "schema_version": 1,
            "categories": [{"key": "head", "name_zh": "頭部與換氣"}], "problems": [{
                "id": "prob.breast.head-lift", "stroke": "breast", "category": "head", "title": "抬頭後沉髖",
                "public": {"observable": "換氣抬頭後髖部下沉", "mechanism_summary": ""},
                "links": {"technical_analysis": [], "drills": [], "interventions": [],
                    "water_interventions": ["movement.intervention.breast.water"]},
                "cross_ref": "", "cross_ref_ids": [],
                "coverage_gap": ["no_mechanism", "no_drill", "no_intervention"],
            }]}

    def check(self, doc):
        errors = defaultdict(list)
        validate_mod.check_problem_contract("fixture", doc, {}, errors)
        return errors["E018"]

    def test_water_intervention_preserves_dryland_gap(self):
        self.assertEqual([], self.check(self.doc))
        self.doc["problems"][0]["coverage_gap"].remove("no_intervention")
        self.assertTrue(self.check(self.doc))

    def test_malformed_fields_are_rejected(self):
        for field, value in [("links", []), ("public", {"id": "override"}),
                             ("coverage_gap", "no_drill"), ("stroke", "free"),
                             ("cross_ref_ids", ["Br1"]), ("title", "")]:
            with self.subTest(field=field):
                doc = deepcopy(self.doc)
                doc["problems"][0][field] = value
                self.assertTrue(self.check(doc))

    def test_wrong_reference_type_and_duplicate_gap_rejected(self):
        doc = deepcopy(self.doc)
        doc["problems"][0]["links"]["interventions"] = ["Br1"]
        self.assertTrue(self.check(doc))
        self.doc["problems"][0]["coverage_gap"].append("no_drill")
        self.assertTrue(self.check(self.doc))

    def test_empty_and_large_partial_documents(self):
        empty = dict(self.doc, problems=[], categories=[])
        self.assertEqual([], self.check(empty))
        entries = []
        for i in range(333):
            entry = deepcopy(self.doc["problems"][0])
            entry["id"] = f"prob.breast.case-{i}"
            entries.append(entry)
        self.assertEqual([], self.check(dict(self.doc, problems=entries)))

    def test_public_unknown_key_and_wrong_summary_fail(self):
        self.doc["problems"][0]["public"]["diagnostic"] = "SHOULD-NOT-LEAK"
        self.assertTrue(self.check(self.doc))
        del self.doc["problems"][0]["public"]["diagnostic"]
        self.doc["problems"][0]["public"]["mechanism_summary"] = "unsupported"
        self.assertTrue(self.check(self.doc))
