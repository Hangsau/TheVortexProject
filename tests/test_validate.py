#!/usr/bin/env python3
"""
test_validate.py - tools/validate.py 的單元測試

用途：
  用最小 fixture 驗證各代碼的偵測邏輯，
  不依賴真實 canonical 資料（避免測試隨內容改動而損壞）。

跑法：
  python -m unittest tests/test_validate.py
  # 或在 repo 根執行：
  python -m unittest discover tests/
"""
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

# 加入 repo 根到 sys.path 以 import tools/validate.py
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# 載入驗證器的核心函式（不執行 main）
import importlib.util
spec = importlib.util.spec_from_file_location(
    "validate", REPO_ROOT / "tools" / "validate.py"
)
validate_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_mod)


# ── Fixture 工廠 ─────────────────────────────────────────────────────────────

def make_taxonomy(values: dict | None = None):
    """建立最小 _taxonomy.yaml 內容。"""
    default_vals = {
        "category": [{"key": "kick"}, {"key": "pull"}, {"key": "concept"}],
        "stroke": [{"key": "free"}, {"key": "back"}, {"key": "common"}],
        # 五個確定性 emoji
        "certainty": [
            {"key": "\U0001F7E2"},  # green
            {"key": "\U0001F535"},  # blue
            {"key": "\U0001F7E0"},  # orange
            {"key": "\U0001F7E1"},  # yellow
            {"key": "\U0001F534"},  # red
        ],
        "status": [{"key": "complete"}, {"key": "draft"}],
    }
    if values:
        default_vals.update(values)
    return {
        "schema_version": 1,
        "domain": "_meta",
        "description": "test taxonomy",
        "fields": {
            field: {"controlled": True, "review_status": "reviewed", "values": vals}
            for field, vals in default_vals.items()
        },
    }


def make_sources(sources=None):
    return {
        "schema_version": 1,
        "domain": "_meta",
        "description": "test sources",
        "sources": sources or [],
    }


class FixtureTestBase(unittest.TestCase):
    """在 tmp 目錄建立 canonical/_taxonomy.yaml 與 _sources.yaml。"""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.canonical_dir = self.root / "canonical"
        self.drills_dir = self.root / "Drills"
        self.canonical_dir.mkdir()
        self.drills_dir.mkdir()
        self.reports_dir = self.root / "reports"

        # 預設 taxonomy & sources
        self._write_yaml(self.canonical_dir / "_taxonomy.yaml", make_taxonomy())
        self._write_yaml(self.canonical_dir / "_sources.yaml", make_sources())

        # 猴子補丁：讓 validate_mod 的路徑常數指向 tmp
        validate_mod.ROOT = self.root
        validate_mod.CANONICAL_DIR = self.canonical_dir
        validate_mod.DRILLS_DIR = self.drills_dir
        validate_mod.TAXONOMY_FILE = self.canonical_dir / "_taxonomy.yaml"
        validate_mod.SOURCES_FILE = self.canonical_dir / "_sources.yaml"
        validate_mod.REPORTS_DIR = self.reports_dir

    def tearDown(self):
        self.tmp.cleanup()

    def _write_yaml(self, path: Path, data: dict):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.dump(data, allow_unicode=True), encoding="utf-8")

    def _run(self):
        """執行驗證，回傳 (errors_dict, warnings_dict, entry_count)。"""
        taxonomy = validate_mod.load_taxonomy()
        allowed_source_ids = validate_mod.load_source_ids()

        all_canonical_files = sorted(self.canonical_dir.rglob("*.yaml"))
        validate_files = [
            p for p in all_canonical_files
            if not validate_mod.is_excluded(p)
        ]
        id_source_files = [
            p for p in all_canonical_files
            if not p.name.startswith("_")
        ]

        drills_files = sorted(self.drills_dir.glob("*.yaml"))
        drills_id_map = validate_mod.collect_all_ids_from_files(drills_files)
        drills_id_set = set(drills_id_map.keys())

        canonical_id_map = validate_mod.collect_all_ids_from_files(id_source_files)
        canonical_id_set = set(canonical_id_map.keys())
        all_id_set = canonical_id_set | drills_id_set

        from collections import defaultdict
        id_registry = defaultdict(list)
        all_entries = []

        for path in validate_files:
            try:
                data = validate_mod.load_yaml(path)
                rel = str(path.relative_to(self.root))
                for entry in validate_mod.iter_entries(data):
                    eid = entry.get("id")
                    if eid and isinstance(eid, str):
                        id_registry[eid].append((rel, entry))
                        all_entries.append((rel, entry))
            except Exception:
                pass

        errors = {"E001": [], "E002": [], "E003": [], "E004": [], "E005": []}
        warnings = {"W001": [], "W002": [], "W003": []}

        # E001
        for path in validate_files:
            data = validate_mod.load_yaml(path)
            rel = str(path.relative_to(self.root))
            validate_mod.find_missing_id_in_lists(data, rel, errors["E001"])

        # E002
        for eid, occs in id_registry.items():
            if len(occs) > 1:
                files_list = ", ".join(f for f, _ in occs)
                errors["E002"].append(f"  id={eid!r} at: {files_list}")

        inbound_ids = defaultdict(int)

        for rel, entry in all_entries:
            eid = entry.get("id", "(no id)")

            # E003
            links = entry.get("links")
            if isinstance(links, dict):
                for link_type, targets in links.items():
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str):
                                if target not in all_id_set:
                                    errors["E003"].append(
                                        f"  {rel} {eid!r} links.{link_type}={target!r}"
                                    )
                                else:
                                    inbound_ids[target] += 1

            # E004
            for field in ("category", "stroke", "certainty", "status"):
                val = entry.get(field)
                if val is not None and isinstance(val, str):
                    allowed = taxonomy.get(field, set())
                    if val not in allowed:
                        errors["E004"].append(
                            f"  {rel} {eid!r} {field}={val!r}"
                        )

            # E005
            source_ids = entry.get("source_ids")
            if source_ids and isinstance(source_ids, list):
                for sid in source_ids:
                    if isinstance(sid, str) and sid not in allowed_source_ids:
                        errors["E005"].append(
                            f"  {rel} {eid!r} source_ids={sid!r}"
                        )

            # W001
            def _check_cross_ref(d, location):
                cr = d.get("cross_ref")
                if cr is not None and isinstance(cr, str) and cr.strip():
                    warnings["W001"].append(
                        f"  {rel} {eid!r} {location}.cross_ref"
                    )
            _check_cross_ref(entry, "entry")
            pub = entry.get("public", {})
            if isinstance(pub, dict):
                _check_cross_ref(pub, "public")

            # W002
            cert = entry.get("certainty")
            if cert in validate_mod.CERTAINTY_NEEDS_SOURCE:
                if not entry.get("source_ids"):
                    warnings["W002"].append(f"  {rel} {eid!r} cert no-source")
            pub2 = entry.get("public", {})
            if isinstance(pub2, dict):
                mech = pub2.get("mechanism", {})
                if isinstance(mech, dict):
                    cert_pub = mech.get("certainty")
                    if cert_pub in validate_mod.CERTAINTY_NEEDS_SOURCE:
                        if not entry.get("source_ids"):
                            warnings["W002"].append(
                                f"  {rel} {eid!r} pub.mech.cert no-source"
                            )

        # W003
        for rel, entry in all_entries:
            eid = entry.get("id")
            if not eid:
                continue
            outbound = validate_mod.collect_outbound_ids(entry)
            is_pointed_to = inbound_ids.get(eid, 0) > 0
            has_outbound = len(outbound) > 0
            if not is_pointed_to and not has_outbound:
                warnings["W003"].append(f"  {rel} {eid!r}")

        return errors, warnings, len(all_entries)


# ── 各代碼測試 ────────────────────────────────────────────────────────────────

class TestE002IdDuplicate(FixtureTestBase):
    """E002：id 重複偵測。"""

    def test_duplicate_detected(self):
        # 兩個檔案用同一 id
        self._write_yaml(
            self.canonical_dir / "file_a.yaml",
            {"points": [{"id": "dup-id", "category": "kick", "stroke": "free"}]},
        )
        self._write_yaml(
            self.canonical_dir / "file_b.yaml",
            {"points": [{"id": "dup-id", "category": "pull", "stroke": "back"}]},
        )
        errors, _, _ = self._run()
        self.assertGreater(len(errors["E002"]), 0, "重複 id 應觸發 E002")

    def test_unique_ids_no_error(self):
        self._write_yaml(
            self.canonical_dir / "file_a.yaml",
            {"points": [{"id": "id-a", "category": "kick", "stroke": "free"}]},
        )
        self._write_yaml(
            self.canonical_dir / "file_b.yaml",
            {"points": [{"id": "id-b", "category": "pull", "stroke": "back"}]},
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E002"]), 0, "唯一 id 不應觸發 E002")


class TestE003BrokenLinks(FixtureTestBase):
    """E003：links.* 斷鏈偵測。"""

    def test_broken_link_detected(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-a",
                        "links": {"technical_analysis": ["nonexistent-id"]},
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertGreater(len(errors["E003"]), 0, "斷鏈應觸發 E003")

    def test_valid_link_no_error(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "target-id", "category": "kick", "stroke": "free"},
                    {
                        "id": "entry-a",
                        "links": {"technical_analysis": ["target-id"]},
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E003"]), 0, "指向存在 id 不應觸發 E003")

    def test_drills_id_not_broken(self):
        # Drills ID 存在時不應報 E003
        self._write_yaml(
            self.drills_dir / "drills_free.yaml",
            {"drills": [{"id": "Fr1", "name_zh": "test drill"}]},
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "standards": [
                    {
                        "id": "std-1",
                        "links": {"drills": ["Fr1"]},
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E003"]), 0, "Drills ID 應被識別為有效，不觸發 E003")


class TestE004TaxonomyViolation(FixtureTestBase):
    """E004：taxonomy 外的值偵測。"""

    def test_invalid_tag_detected(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-1",
                        "category": "NONEXISTENT_CATEGORY",
                        "stroke": "free",
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertGreater(len(errors["E004"]), 0, "不在 taxonomy 的值應觸發 E004")

    def test_valid_tags_no_error(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-1",
                        "category": "kick",
                        "stroke": "free",
                        "certainty": "\U0001F7E2",
                        "status": "complete",
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E004"]), 0, "合法 taxonomy 值不應觸發 E004")


class TestW002CertaintyNoSource(FixtureTestBase):
    """W002：certainty green/yellow 但無 source_ids。"""

    def test_green_no_source_triggers_w002(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-green",
                        "certainty": "\U0001F7E2",  # green
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(len(warnings["W002"]), 0, "green certainty 無 source_ids 應觸發 W002")

    def test_yellow_no_source_triggers_w002(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-yellow",
                        "certainty": "\U0001F7E1",  # yellow
                        "category": "pull",
                        "stroke": "back",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(len(warnings["W002"]), 0, "yellow certainty 無 source_ids 應觸發 W002")

    def test_orange_no_source_no_w002(self):
        # orange（教練觀測）不需要 source_ids
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-orange",
                        "certainty": "\U0001F7E0",  # orange
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0, "orange certainty 不應觸發 W002")

    def test_green_with_source_no_w002(self):
        # green + source_ids → 正常，不觸發 W002
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.test-2000", "type": "journal-article",
                           "title": "Test", "authors": ["A"],
                           "year": 2000, "identifier": {"doi": "10.1/test"},
                           "retrieved_on": "2026-01-01"}]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-ok",
                        "certainty": "\U0001F7E2",
                        "source_ids": ["src.test-2000"],
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0, "green + source_ids 不應觸發 W002")


class TestCleanDataNoFalsePositive(FixtureTestBase):
    """正常資料不觸發任何錯誤或警告。"""

    def test_clean_entry_no_errors(self):
        # 完整乾淨的條目：有 id、合法 tag、連結到存在 id、有 source_ids
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.clean-2020", "type": "review",
                           "title": "Clean Source", "authors": ["B"],
                           "year": 2020, "identifier": {"pmid": "12345"},
                           "retrieved_on": "2026-01-01"}]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-target",
                        "category": "concept",
                        "stroke": "common",
                    },
                    {
                        "id": "entry-clean",
                        "category": "kick",
                        "stroke": "free",
                        "certainty": "\U0001F7E2",
                        "status": "complete",
                        "source_ids": ["src.clean-2020"],
                        "links": {"technical_analysis": ["entry-target"]},
                    },
                ]
            },
        )
        errors, warnings, count = self._run()
        for code, items in errors.items():
            self.assertEqual(len(items), 0, f"乾淨資料不應觸發 {code}: {items}")
        for code in ("W001", "W002"):
            self.assertEqual(
                len(warnings[code]), 0,
                f"乾淨資料不應觸發 {code}: {warnings[code]}"
            )
        self.assertEqual(count, 2, "應掃到 2 個條目")

    def test_drafts_excluded_from_e002(self):
        # drafts/ 目錄的同 id 不應觸發 E002
        drafts_dir = self.canonical_dir / "health" / "drafts"
        drafts_dir.mkdir(parents=True)
        self._write_yaml(
            drafts_dir / "test-injury.yaml",
            {"id": "test-injury", "category": "A-shoulder-upper"},
        )
        # 同 id 的 build artifact
        self._write_yaml(
            self.canonical_dir / "health" / "injuries.yaml",
            {"injuries": [{"id": "test-injury", "category": "A-shoulder-upper"}]},
        )
        # 在 taxonomy 加上 A-shoulder-upper
        self._write_yaml(
            self.canonical_dir / "_taxonomy.yaml",
            make_taxonomy({"category": [
                {"key": "kick"}, {"key": "pull"}, {"key": "concept"},
                {"key": "A-shoulder-upper"},
            ]}),
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E002"]), 0,
            "drafts/ 與 build artifact 的同 id 不應觸發 E002"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
