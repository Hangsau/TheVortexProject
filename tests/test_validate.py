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
        warnings = {"W001": [], "W002": [], "W003": [], "W004": [], "W005": []}

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

            # E003 / E004（links 子鍵分三類，與 validate_mod 邏輯一致）
            links = entry.get("links")
            if isinstance(links, dict):
                for link_type, targets in links.items():
                    if link_type in validate_mod.LINKS_VOCAB_REF_KEYS:
                        # 詞彙參照類 → 比對 taxonomy，違規報 E004
                        tax_field = validate_mod.LINKS_VOCAB_REF_KEYS[link_type]
                        allowed_vocab = taxonomy.get(tax_field, set())
                        if isinstance(targets, list):
                            for target in targets:
                                if isinstance(target, str) and target:
                                    if target not in allowed_vocab:
                                        errors["E004"].append(
                                            f"  {rel} {eid!r} "
                                            f"links.{link_type}={target!r}"
                                        )
                        elif isinstance(targets, str) and targets:
                            if targets not in allowed_vocab:
                                errors["E004"].append(
                                    f"  {rel} {eid!r} "
                                    f"links.{link_type}={targets!r}"
                                )
                    elif link_type in validate_mod.LINKS_ID_REF_KEYS:
                        # ID 參照類 → 比對全域 ID 集合，違規報 E003
                        if isinstance(targets, list):
                            for target in targets:
                                if isinstance(target, str):
                                    if target not in all_id_set:
                                        errors["E003"].append(
                                            f"  {rel} {eid!r} links.{link_type}={target!r}"
                                        )
                                    else:
                                        inbound_ids[target] += 1
                        elif isinstance(targets, str) and targets:
                            if targets not in all_id_set:
                                errors["E003"].append(
                                    f"  {rel} {eid!r} links.{link_type}={targets!r}"
                                )
                            else:
                                inbound_ids[targets] += 1
                    elif link_type in validate_mod.LINKS_FREE_TEXT_KEYS:
                        # 已知自由文字類 → W004
                        if isinstance(targets, str) and targets:
                            snippet = targets[:120]
                            candidates = validate_mod._CANDIDATE_ID_RE.findall(targets)
                            candidate_note = (
                                f"（候選 ID: {', '.join(candidates)}）"
                                if candidates else ""
                            )
                            warnings["W004"].append(
                                f"  {rel} {eid!r} "
                                f"links.{link_type} 散文前120字: {snippet!r}"
                                + (f"\n    {candidate_note}" if candidate_note else "")
                            )
                    else:
                        # 未知子鍵 → W005
                        val_preview = ""
                        if isinstance(targets, str):
                            val_preview = targets[:120]
                        elif isinstance(targets, list):
                            val_preview = str(targets)[:120]
                        warnings["W005"].append(
                            f"  {rel} {eid!r} "
                            f"links.{link_type} 未歸類，值前120字: {val_preview!r}"
                        )

            # E004（欄位值 taxonomy 驗證，與 links 無關）
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

            # W001（保留完整 Unicode，不做 ASCII encode）
            def _check_cross_ref(d, location):
                cr = d.get("cross_ref")
                if cr is not None and isinstance(cr, str) and cr.strip():
                    warnings["W001"].append(
                        f"  {rel} {eid!r} {location}.cross_ref (120 chars): {cr[:120]!r}"
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


class TestE001VocabListSkipped(FixtureTestBase):
    """E001：詞彙定義表（key 型清單）不觸發 E001；真正缺 id 的條目仍觸發。"""

    def test_vocab_list_key_no_e001(self):
        # levels / stages / pillars 是詞彙定義表，元素用 key 不用 id，不應觸發 E001
        self._write_yaml(
            self.canonical_dir / "vocab_def.yaml",
            {
                "domain": "technica",
                "levels": [
                    {"key": "pre", "name_zh": "前置"},
                    {"key": "L2", "name_zh": "L2"},
                ],
                "stages": [
                    {"key": "l2t", "name_en": "Learn to Train"},
                    {"key": "t2t", "name_en": "Train to Train"},
                ],
                "pillars": [
                    {"key": "physical", "name_zh": "體能"},
                ],
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E001"]), 0,
            "詞彙定義表（levels/stages/pillars）不應觸發 E001"
        )

    def test_content_entry_without_id_still_triggers_e001(self):
        # 真正的內容條目（cells 裡的元素）缺 id 應觸發 E001
        self._write_yaml(
            self.canonical_dir / "content.yaml",
            {
                "domain": "development",
                "cells": [
                    {"pillar": "physical", "stage": "l2t"},  # 缺 id
                    {"id": "dev.physical.l2t", "pillar": "physical", "stage": "l2t"},  # 有 id
                ],
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E001"]), 1, "缺 id 的 cells 元素應觸發 E001")


class TestE003LinksVocabSeparation(FixtureTestBase):
    """E003 / E004：links 詞彙參照類與 ID 參照類分離。"""

    def setUp(self):
        super().setUp()
        # taxonomy 加入 development_stage 詞彙
        self._write_yaml(
            self.canonical_dir / "_taxonomy.yaml",
            make_taxonomy({
                "category": [{"key": "kick"}, {"key": "pull"}, {"key": "concept"}],
                "stroke": [{"key": "free"}, {"key": "back"}, {"key": "common"}],
                "certainty": [
                    {"key": "\U0001F7E2"}, {"key": "\U0001F535"},
                    {"key": "\U0001F7E0"}, {"key": "\U0001F7E1"},
                    {"key": "\U0001F534"},
                ],
                "status": [{"key": "complete"}, {"key": "draft"}],
                "development_stage": [
                    {"key": "fun"}, {"key": "l2t"}, {"key": "t2t"},
                    {"key": "t2c"}, {"key": "t2w"},
                ],
            })
        )

    def test_valid_development_stages_no_e003_no_e004(self):
        # links.development_stages 用合法詞彙值，不應觸發 E003 也不觸發 E004
        self._write_yaml(
            self.canonical_dir / "periodization.yaml",
            {
                "entries": [
                    {
                        "id": "period.overview",
                        "links": {
                            "development_stages": ["l2t", "t2t", "t2c"],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E003"]), 0,
            "合法 development_stage 詞彙不應觸發 E003"
        )
        # E004 可能有其他 taxonomy 觸發，只確認 development_stages 這條沒問題
        e004_devstage = [
            m for m in errors["E004"] if "development_stages" in m
        ]
        self.assertEqual(
            len(e004_devstage), 0,
            "合法 development_stage 詞彙不應觸發 E004"
        )

    def test_invalid_development_stages_triggers_e004_not_e003(self):
        # links.development_stages 用未登錄值應觸發 E004，不觸發 E003
        self._write_yaml(
            self.canonical_dir / "periodization.yaml",
            {
                "entries": [
                    {
                        "id": "period.overview",
                        "links": {
                            "development_stages": ["l2t", "INVALID_STAGE"],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E003"]), 0,
            "development_stages 值不應觸發 E003（應改報 E004）"
        )
        e004_devstage = [
            m for m in errors["E004"] if "development_stages" in m
        ]
        self.assertGreater(
            len(e004_devstage), 0,
            "未登錄的 development_stage 值應觸發 E004"
        )

    def test_links_standards_broken_id_still_triggers_e003(self):
        # links.standards 指向不存在 ID 仍觸發 E003（ID 參照類行為不變）
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-a",
                        "links": {
                            "standards": ["std.free.pull.nonexistent"],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertGreater(
            len(errors["E003"]), 0,
            "links.standards 指向不存在 ID 應觸發 E003"
        )


class TestW001ChineseEncoding(FixtureTestBase):
    """W001：cross_ref 中文字串寫入報告後可正確讀回（防 ASCII encode 回歸）。"""

    def test_chinese_cross_ref_preserved_in_warning(self):
        # cross_ref 含中文，W001 警告字串必須保留原始 Unicode，不能變問號
        chinese_ref = "感知層 L2.1→L3.1 手感建立與水感萌芽連結"
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-chinese",
                        "public": {
                            "cross_ref": chinese_ref,
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W001"]), 0, "含中文 cross_ref 應觸發 W001"
        )
        # 驗證警告字串中的中文被完整保留（不是問號）
        w001_msg = warnings["W001"][0]
        self.assertIn(
            "感知層",
            w001_msg,
            "W001 警告訊息必須保留中文，不能轉換成問號"
        )

    def test_chinese_cross_ref_in_report_file(self):
        # 同樣的中文 cross_ref 必須能正確寫入 reports/validation_report.md 並讀回
        chinese_ref = "感知層 L2.1→L3.1 手感建立與水感萌芽連結"
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-chinese-report",
                        "public": {
                            "cross_ref": chinese_ref,
                        },
                    }
                ]
            },
        )
        # 先跑一次以收集 warnings
        from collections import defaultdict
        errors_dict = {
            "E001": [], "E002": [], "E003": [], "E004": [], "E005": []
        }
        _, warnings_dict, _ = self._run()

        # 模擬寫入報告
        self.reports_dir.mkdir(exist_ok=True)
        validate_mod._write_report(errors_dict, warnings_dict, 1, 0)

        # 讀回報告，確認中文完整
        report_path = self.reports_dir / "validation_report.md"
        content = report_path.read_text(encoding="utf-8")
        self.assertIn(
            "感知層",
            content,
            "報告中的 W001 中文必須完整，不能變問號"
        )


class TestW004FreeTextLink(FixtureTestBase):
    """W004：*_link 欄位含散文應觸發 W004，null 值不觸發。"""

    def test_mechanism_link_prose_triggers_w004(self):
        # mechanism_link 含散文應觸發 W004
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-001",
                        "links": {
                            "mechanism_link": "前鋸肌耐力是 EVF 的硬體前提，疲勞後肩胛失穩",
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W004"]), 0,
            "mechanism_link 含散文應觸發 W004"
        )

    def test_technical_link_with_candidate_id(self):
        # technical_link 含 free.tech.10 這類 ID → W004 應附候選 ID 備註
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-002",
                        "links": {
                            "technical_link": "free.tech.10 前鋸肌硬體邊界說明",
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W004"]), 0,
            "technical_link 含散文應觸發 W004"
        )
        # 確認候選 ID 被抽出並附在警告中
        w004_msg = warnings["W004"][0]
        self.assertIn(
            "free.tech.10",
            w004_msg,
            "W004 應附候選 ID free.tech.10"
        )

    def test_perception_link_with_drill_id(self):
        # perception_link 含 Drill 編號格式（如 FrBr3）→ W004 應附候選 ID
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-003",
                        "links": {
                            "perception_link": "可接 FrBr3 drill 的感知層作業",
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W004"]), 0,
            "perception_link 含散文應觸發 W004"
        )
        w004_msg = warnings["W004"][0]
        self.assertIn(
            "FrBr3",
            w004_msg,
            "W004 應附候選 Drill ID FrBr3"
        )

    def test_null_link_no_w004(self):
        # *_link 值為 null（Python None）不觸發 W004
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-null",
                        "links": {
                            "mechanism_link": None,
                            "technical_link": None,
                            "perception_link": None,
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W004"]), 0,
            "null 值不應觸發 W004"
        )


class TestW005UnknownLinksKey(FixtureTestBase):
    """W005：links 下未知子鍵應觸發 W005；已知子鍵不觸發。"""

    def test_unknown_link_key_triggers_w005(self):
        # links.foobar 不在任何已知集合中，應觸發 W005
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-unknown-link",
                        "links": {
                            "foobar": "some value",
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W005"]), 0,
            "links.foobar 應觸發 W005"
        )

    def test_known_id_ref_key_no_w005(self):
        # links.technical_analysis 是 ID 參照類，不觸發 W005（即使 ID 斷鏈也只觸發 E003）
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "target-id",
                        "category": "kick",
                        "stroke": "free",
                    },
                    {
                        "id": "entry-known",
                        "links": {
                            "technical_analysis": ["target-id"],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W005"]), 0,
            "links.technical_analysis（ID 參照類）不應觸發 W005"
        )

    def test_known_vocab_ref_key_no_w005(self):
        # links.development_stages 是詞彙參照類，不觸發 W005
        self._write_yaml(
            self.canonical_dir / "_taxonomy.yaml",
            make_taxonomy({
                "category": [{"key": "kick"}],
                "stroke": [{"key": "free"}],
                "certainty": [{"key": "\U0001F7E2"}],
                "status": [{"key": "complete"}],
                "development_stage": [{"key": "fun"}, {"key": "l2t"}],
            })
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-vocab",
                        "links": {
                            "development_stages": ["fun", "l2t"],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W005"]), 0,
            "links.development_stages（詞彙參照類）不應觸發 W005"
        )

    def test_known_free_text_key_no_w005(self):
        # links.mechanism_link 是已知自由文字類，不觸發 W005（可能觸發 W004）
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-free",
                        "links": {
                            "mechanism_link": "一些散文說明",
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W005"]), 0,
            "links.mechanism_link（已知自由文字類）不應觸發 W005"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
