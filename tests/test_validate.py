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
        # 全域 ID 集合直接用產品程式碼的函式（路徑常數已在 setUp 猴子補丁），
        # 測試不自己維護第二份收集邏輯
        all_id_set, _, _ = validate_mod.build_global_id_set()

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

        errors = {
            "E001": [], "E002": [], "E003": [], "E004": [], "E005": [],
            "E006": [], "E007": [], "E010": [], "E011": [],
        }
        warnings = {
            "W001": [], "W002": [], "W003": [], "W004": [], "W005": [],
            "W006": [], "W007": [], "W008": [], "W009": [], "W011": [],
        }

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

            # W003 入邊：非 links 的關聯欄位一律走產品端 helper，不在這裡重寫。
            # 2026-09-03：harness 原本只累計 links.* 的入邊，movement 關聯欄位
            # 與 cross_ref_ids 都沒算，等於 W003 的一半邏輯在測試裡沒被覆蓋。
            for target in validate_mod.collect_movement_relation_ids(entry):
                if target in all_id_set:
                    inbound_ids[target] += 1
            for target in validate_mod.collect_cross_ref_ids(entry):
                if target in all_id_set:
                    inbound_ids[target] += 1

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
                        # 自由文字顯示鍵 → 交給 check_link_ids()
                        pass
                    elif link_type in validate_mod.LINKS_IDS_KEYS:
                        # 機器鍵 → 交給 check_link_ids()
                        pass
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

                # E007 / W004 / W007：直接呼叫產品程式碼的 *_link 契約檢查
                validate_mod.check_link_ids(
                    rel, eid, links, all_id_set, errors, warnings
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

            # E005 / W002 / W009：由 check_source_blocks() 逐檔遞迴處理
            # （見下方），這裡不重複一份條目層邏輯

            # E006 / W001 / W006：直接呼叫產品程式碼的 cross_ref 契約檢查
            # 這幾行是產品端 validate.py 主迴圈的鏡像，層別清單必須跟它一致；
            # 產品端加層而這裡沒跟上，新增的層就會在測試裡永遠沒被覆蓋到。
            validate_mod.check_cross_ref(
                rel, eid, entry, "entry", all_id_set, errors, warnings
            )
            for layer in ("public", "diagnostic"):
                sub = entry.get(layer)
                if isinstance(sub, dict):
                    validate_mod.check_cross_ref(
                        rel, eid, sub, layer, all_id_set, errors, warnings
                    )

        # E005 / W002 / W009：直接呼叫產品程式碼的 source 契約檢查
        # （遞迴走訪整棵樹，不只條目層；掃描範圍與產品端一致，含 Drills）
        source_scan_files = validate_files + sorted(
            self.drills_dir.glob("*.yaml"))
        referenced_source_ids = set()
        for path in source_scan_files:
            try:
                data = validate_mod.load_yaml(path)
            except Exception:
                continue
            rel = str(path.relative_to(self.root))
            referenced_source_ids |= validate_mod.check_source_blocks(
                rel, data, allowed_source_ids, errors, warnings
            )
            # W011 / E010 / E011：與產品端同一輪走訪
            validate_mod.check_practitioner_blocks(rel, data, warnings)
            validate_mod.check_public_layer_leak(rel, data, errors)
            validate_mod.check_evidence_from(rel, data, all_id_set, errors)

        # W008：直接呼叫產品程式碼的孤兒來源檢查
        validate_mod.check_orphan_sources(
            allowed_source_ids, referenced_source_ids, warnings
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
    """W002 / W009：缺 source_ids 的兩種型態。

    S3a 把舊 W002 拆成兩碼，因為兩者的修法完全不同：
      W002  已經有 source/sources 顯示字串 → 只差登錄成來源條目再補機器鍵
      W009  連顯示字串都沒有             → 得回頭找主張依據（S3b），
                                            不能靠遷移或佔位來源解決

    S3a-2 再把 W002 與 certainty 解耦（見 TestW002DecoupledFromCertainty）：
    有顯示字串就要有機器鍵，不論該區塊有沒有標確定性。W009 維持綁 certainty。
    """

    def test_green_no_source_info_triggers_w009_not_w002(self):
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
        self.assertGreater(
            len(warnings["W009"]), 0,
            "green 且完全無來源資訊應觸發 W009",
        )
        self.assertEqual(
            len(warnings["W002"]), 0,
            "沒有 source 顯示字串就不是 W002（不可用 W002 混稱）",
        )

    def test_yellow_no_source_info_triggers_w009_not_w002(self):
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
        self.assertGreater(len(warnings["W009"]), 0, "yellow 無來源資訊應觸發 W009")
        self.assertEqual(len(warnings["W002"]), 0)

    def test_green_with_source_string_triggers_w002_not_w009(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-src",
                        "certainty": "\U0001F7E2",
                        "source": "Nicol et al. 2022",
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W002"]), 0,
            "有 source 顯示字串但缺 source_ids 應觸發 W002",
        )
        self.assertEqual(
            len(warnings["W009"]), 0,
            "有 source 顯示字串就不算「完全無來源資訊」",
        )
        self.assertIn("source 顯示字串", warnings["W002"][0])

    def test_sources_plural_list_triggers_w002_not_w009(self):
        # health/injuries、psychology 用的是 sources（複數清單）
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-srcs",
                        "certainty": "\U0001F7E1",
                        "sources": ["Masters shoulder ultrasound, PMC7824457"],
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(len(warnings["W002"]), 0)
        self.assertEqual(len(warnings["W009"]), 0)

    def test_empty_source_string_counts_as_no_source_info(self):
        # source: '' 是「有欄位但沒內容」，不算來源資訊 → W009 不是 W002
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-empty-src",
                        "certainty": "\U0001F7E2",
                        "source": "   ",
                        "category": "kick",
                        "stroke": "free",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0)
        self.assertGreater(len(warnings["W009"]), 0)

    def test_nested_evidence_block_is_scanned(self):
        # S3a 修正重點：certainty 掛在巢狀 evidence[] 上也要被掃到
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-nested",
                        "category": "kick",
                        "stroke": "free",
                        "public": {
                            "evidence": [
                                {
                                    "certainty": "\U0001F7E2",
                                    "text": "巢狀證據",
                                    "source": "Gonjo & Olstad 2023",
                                },
                                {
                                    "certainty": "\U0001F7E2",
                                    "text": "沒有來源的巢狀證據",
                                },
                            ]
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W002"]), 1,
            "巢狀 evidence[] 的 certainty 必須被遞迴掃到（舊版只看條目頂層）",
        )
        self.assertEqual(len(warnings["W009"]), 1)
        self.assertIn("public.evidence[0]", warnings["W002"][0])
        self.assertIn("entry-nested", warnings["W009"][0])

    def test_nested_block_with_source_ids_no_warning(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.test-2000", "type": "other",
                           "verification_status": "unverified",
                           "display": "Test 2000"}]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-nested-ok",
                        "category": "kick",
                        "stroke": "free",
                        "public": {
                            "evidence": [
                                {
                                    "certainty": "\U0001F7E2",
                                    "text": "有機器鍵",
                                    "source": "Test 2000",
                                    "source_ids": ["src.test-2000"],
                                }
                            ]
                        },
                    }
                ]
            },
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0)
        self.assertEqual(len(warnings["W009"]), 0)
        self.assertEqual(len(errors["E005"]), 0)

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
        self.assertEqual(len(warnings["W009"]), 0, "orange certainty 不應觸發 W009")

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
        self.assertEqual(len(warnings["W009"]), 0, "green + source_ids 不應觸發 W009")


class TestW002DecoupledFromCertainty(FixtureTestBase):
    """S3a-2：W002 不再以 certainty 為前提。

    「這個區塊有沒有標確定性」跟「這個來源該不該被註冊」是兩件事。
    綁在 certainty 上是舊 W002 框架的殘留，會讓 periodization/*、Drills/* 這類
    沒標確定性但確實帶 source 的區塊完全逃過檢查。
    W009 相反——它問的是「標了 🟢/🟡 卻拿不出來源」，本來就該綁 certainty。
    """

    def test_source_without_certainty_still_triggers_w002(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-no-cert",
                        "category": "kick",
                        "stroke": "free",
                        # 刻意不給 certainty
                        "source": "Ch5 Periodization Terminology; Ch8 Phases",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W002"]), 1,
            "有 source 字串就該要求 source_ids，不論有沒有 certainty",
        )
        self.assertIn("無 certainty", warnings["W002"][0])
        self.assertEqual(
            len(warnings["W009"]), 0,
            "沒有 certainty 就不該進 W009（W009 仍以 certainty 為前提）",
        )

    def test_sources_plural_without_certainty_triggers_w002(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-no-cert-plural",
                        "category": "kick",
                        "stroke": "free",
                        "epidemiology": {
                            "sources": ["IOC RED-S 共識聲明", "Mountjoy 等 IOC consensus"],
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 1)
        self.assertIn("有 sources 顯示字串", warnings["W002"][0])
        self.assertIn("epidemiology", warnings["W002"][0])
        self.assertEqual(len(warnings["W009"]), 0)

    def test_no_certainty_no_source_is_silent(self):
        # 沒 certainty 又沒 source → 兩碼都不該叫（解耦不等於全面收網）
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-plain",
                        "category": "kick",
                        "stroke": "free",
                        "text": "純敘述，沒有來源主張",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0)
        self.assertEqual(len(warnings["W009"]), 0)

    def test_source_without_certainty_resolved_by_source_ids(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.ch5-ch8", "type": "other",
                           "verification_status": "unverified",
                           "display": "Ch5; Ch8"}]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-no-cert-ok",
                        "category": "kick",
                        "stroke": "free",
                        "source": "Ch5; Ch8",
                        "source_ids": ["src.ch5-ch8"],
                    }
                ]
            },
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W002"]), 0)
        self.assertEqual(len(errors["E005"]), 0)
        self.assertEqual(
            len(warnings["W008"]), 0,
            "無 certainty 的區塊引用也應算數，來源不該被判成孤兒",
        )


class TestSourceCheckCoversDrills(FixtureTestBase):
    """S3a-2：來源契約檢查（E005/W002/W009）擴到 Drills/*.yaml。

    Drills 過去只被 build_global_id_set() 用來湊 ID 集合，
    它裡面 176 個帶 source 的區塊不在任何檢查範圍內。
    這裡只擴這一組代碼——Drills 沒有 canonical 的 links/category 契約，
    把它併進 validate_files 會一次噴出大量無關的 E001/E004/W003/W005。
    """

    def test_drills_source_without_ids_triggers_w002(self):
        self._write_yaml(
            self.drills_dir / "drills_freestyle.yaml",
            {
                "drills": [
                    {
                        "id": "Fr01",
                        "name_zh": "測試 drill",
                        "source": "There's a Drill for That",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W002"]), 1,
            "Drills 的 source 區塊也要被來源契約檢查覆蓋",
        )
        self.assertIn("drills_freestyle.yaml", warnings["W002"][0])

    def test_drills_dangling_source_ids_triggers_e005(self):
        self._write_yaml(
            self.drills_dir / "drills_butterfly.yaml",
            {
                "drills": [
                    {
                        "id": "Fl01",
                        "source": "Maglischo Swimming Fastest",
                        "source_ids": ["src.does-not-exist"],
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 1)
        self.assertIn("src.does-not-exist", errors["E005"][0])

    def test_drills_reference_counts_against_w008(self):
        # Drills 的引用要算進「有人引用」，否則來源會被誤判成孤兒
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.theres-a-drill-for-that", "type": "book",
                           "verification_status": "unverified",
                           "display": "There's a Drill for That"}]),
        )
        self._write_yaml(
            self.drills_dir / "drills_sculling.yaml",
            {
                "drills": [
                    {
                        "id": "Sc01",
                        "source": "There's a Drill for That",
                        "source_ids": ["src.theres-a-drill-for-that"],
                    }
                ]
            },
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(errors["E005"]), 0)
        self.assertEqual(len(warnings["W002"]), 0)
        self.assertEqual(
            len(warnings["W008"]), 0,
            "只被 Drills 引用的來源不是孤兒",
        )

    def test_drills_certainty_without_source_triggers_w009(self):
        self._write_yaml(
            self.drills_dir / "drills_backstroke.yaml",
            {
                "drills": [
                    {
                        "id": "Bk01",
                        "certainty": "\U0001F7E2",
                        "text": "宣稱有文獻但沒給來源",
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W009"]), 1)
        self.assertEqual(len(warnings["W002"]), 0)


class TestE005SourceIdsResolution(FixtureTestBase):
    """E005：source_ids 指向 _sources.yaml 不存在的 ID（任意深度）。

    S3a 前 E005 只掃條目頂層；201 筆機器鍵全在巢狀 evidence[] 上，
    等於對實際資料零覆蓋。這裡兩層都測。
    """

    def _sources_fixture(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.nicol-2022", "type": "other",
                           "verification_status": "unverified",
                           "display": "Nicol et al. 2022"}]),
        )

    def test_dangling_source_id_at_entry_level_triggers_e005(self):
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-a",
                        "category": "kick",
                        "stroke": "free",
                        "source": "Nicol et al. 2022",
                        "source_ids": ["src.does-not-exist"],
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 1)
        self.assertIn("src.does-not-exist", errors["E005"][0])

    def test_dangling_source_id_in_nested_block_triggers_e005(self):
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-b",
                        "category": "kick",
                        "stroke": "free",
                        "public": {
                            "evidence": [
                                {
                                    "certainty": "\U0001F7E2",
                                    "source": "Nicol et al. 2022",
                                    "source_ids": ["src.ghost-1999"],
                                }
                            ]
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E005"]), 1,
            "巢狀區塊的 source_ids 斷鏈必須被抓到",
        )
        self.assertIn("src.ghost-1999", errors["E005"][0])
        self.assertIn("public.evidence[0]", errors["E005"][0])

    def test_resolvable_source_id_no_e005(self):
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-c",
                        "category": "kick",
                        "stroke": "free",
                        "public": {
                            "evidence": [
                                {
                                    "certainty": "\U0001F7E2",
                                    "source": "Nicol et al. 2022",
                                    "source_ids": ["src.nicol-2022"],
                                }
                            ]
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 0)

    def test_non_list_source_ids_triggers_e005(self):
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-d",
                        "category": "kick",
                        "stroke": "free",
                        "source_ids": "src.nicol-2022",  # 應為 list
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 1)
        self.assertIn("型別應為 list", errors["E005"][0])

    def test_non_string_element_triggers_e005(self):
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-e",
                        "category": "kick",
                        "stroke": "free",
                        "source_ids": ["src.nicol-2022", 123],
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 1)
        self.assertIn("非字串元素", errors["E005"][0])

    def test_empty_source_ids_list_no_e005(self):
        # [] = 已檢查、確認無來源可連（與欄位缺席不同義）
        self._sources_fixture()
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-f",
                        "category": "kick",
                        "stroke": "free",
                        "source_ids": [],
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(len(errors["E005"]), 0)


class TestW008OrphanSources(FixtureTestBase):
    """W008：_sources.yaml 有登錄但沒有任何條目引用。"""

    def test_unreferenced_source_triggers_w008(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([
                {"id": "src.used-2020", "type": "other",
                 "verification_status": "unverified", "display": "Used 2020"},
                {"id": "src.orphan-1999", "type": "other",
                 "verification_status": "unverified", "display": "Orphan 1999"},
            ]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-w008",
                        "category": "kick",
                        "stroke": "free",
                        "source": "Used 2020",
                        "source_ids": ["src.used-2020"],
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W008"]), 1)
        self.assertIn("src.orphan-1999", warnings["W008"][0])

    def test_all_sources_referenced_no_w008(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([
                {"id": "src.used-2020", "type": "other",
                 "verification_status": "unverified", "display": "Used 2020"},
            ]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-w008-ok",
                        "category": "kick",
                        "stroke": "free",
                        "public": {
                            "evidence": [
                                {
                                    "certainty": "\U0001F7E1",
                                    "source": "Used 2020",
                                    "source_ids": ["src.used-2020"],
                                }
                            ]
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W008"]), 0)

    def test_dangling_reference_does_not_suppress_w008(self):
        # 引用了不存在的 ID（E005），已登錄的來源仍是孤兒（W008），兩碼各報各的
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([
                {"id": "src.real-2020", "type": "other",
                 "verification_status": "unverified", "display": "Real 2020"},
            ]),
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "entry-w008-dangling",
                        "category": "kick",
                        "stroke": "free",
                        "source_ids": ["src.typo-2020"],
                    }
                ]
            },
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(errors["E005"]), 1)
        self.assertEqual(len(warnings["W008"]), 1)
        self.assertIn("src.real-2020", warnings["W008"][0])


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
    """cross_ref 中文字串寫入警告與報告後可正確讀回（防 ASCII encode 回歸）。

    S4c 後：純散文（無疑似 ID）的 cross_ref 未處理時走 W006，
    含疑似 ID 但未同步 cross_ref_ids 時走 W001；兩者都必須保留中文。
    """

    def test_chinese_cross_ref_preserved_in_warning(self):
        # cross_ref 含中文且未處理（無 cross_ref_ids）→ W006，中文須完整保留
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
            len(warnings["W006"]), 0, "未處理的中文 cross_ref 應觸發 W006"
        )
        # 驗證警告字串中的中文被完整保留（不是問號）
        w006_msg = warnings["W006"][0]
        self.assertIn(
            "感知層",
            w006_msg,
            "W006 警告訊息必須保留中文，不能轉換成問號"
        )

    def test_chinese_cross_ref_with_id_preserved_in_w001(self):
        # cross_ref 含中文 + 疑似 ID，但 cross_ref_ids 沒同步 → W001，中文須完整
        chinese_ref = "感知層與 free.tech.7 的手感建立連結"
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {
                        "id": "entry-chinese-w001",
                        "public": {
                            "cross_ref": chinese_ref,
                            "cross_ref_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W001"]), 0, "疑似 ID 未同步應觸發 W001"
        )
        self.assertIn(
            "感知層",
            warnings["W001"][0],
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
        errors_dict = {
            "E001": [], "E002": [], "E003": [], "E004": [], "E005": [],
            "E006": [],
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
            "報告中的 cross_ref 中文必須完整，不能變問號"
        )


class TestW004LinkIdsDesync(FixtureTestBase):
    """W004：*_link 裡看得到的穩定 ID 沒同步進 *_link_ids → WARN。

    S4b 起 W004 不再是「有散文就警告」，而是 fail-closed 的脫節偵測：
    顯示字串抽得出可解析 ID、但機器鍵沒列 → 警告。
    """

    def test_namespaced_id_not_in_ids_triggers_w004(self):
        # technical_link 內有 free.tech.10，ids 卻是空的 → W004
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "free.tech.10"},
                    {
                        "id": "inj-002",
                        "links": {
                            "technical_link": "free.tech.10 前鋸肌硬體邊界說明",
                            "technical_link_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W004"]), 1,
            "technical_link 含未同步的 free.tech.10 應觸發 W004"
        )
        self.assertIn("free.tech.10", warnings["W004"][0])

    def test_bare_slug_link_not_in_ids_triggers_w004(self):
        # 整個 mechanism_link 就是一個裸 slug 條目 ID（health 最常見寫法）
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "female-athlete-triad"},
                    {
                        "id": "exercise-amenorrhea",
                        "links": {
                            "mechanism_link": "female-athlete-triad",
                            "mechanism_link_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W004"]), 1,
            "裸 slug 的 mechanism_link 未同步進 ids 應觸發 W004"
        )
        self.assertIn("female-athlete-triad", warnings["W004"][0])

    def test_drill_id_not_in_ids_triggers_w004(self):
        # perception_link 含 Drill 編號格式（FrBr3）且未同步 → W004
        self._write_yaml(
            self.drills_dir / "free.yaml",
            {"drills": [{"id": "FrBr3"}]},
        )
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-003",
                        "links": {
                            "perception_link": "可接 FrBr3 drill 的感知層作業",
                            "perception_link_ids": [],
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W004"]), 1,
            "perception_link 含未同步的 FrBr3 應觸發 W004"
        )
        self.assertIn("FrBr3", warnings["W004"][0])

    def test_ids_in_sync_no_w004(self):
        # 顯示字串裡的 ID 已列入 ids → 不警告
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "free.tech.10"},
                    {"id": "female-athlete-triad"},
                    {
                        "id": "inj-sync",
                        "links": {
                            "technical_link": "free.tech.10 前鋸肌硬體邊界說明",
                            "technical_link_ids": ["free.tech.10"],
                            "mechanism_link": "female-athlete-triad",
                            "mechanism_link_ids": ["female-athlete-triad"],
                        },
                    },
                ]
            },
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W004"]), 0, "ids 已同步不應觸發 W004")
        self.assertEqual(len(errors["E007"]), 0, "可解析 ID 不應觸發 E007")

    def test_pure_prose_with_empty_ids_no_w004(self):
        # 純散文、無任何可解析 ID，ids 明確寫 [] → 不警告（已檢查、無 ID 可連）
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-001",
                        "links": {
                            "mechanism_link": "前鋸肌耐力是 EVF 的硬體前提，疲勞後肩胛失穩",
                            "mechanism_link_ids": [],
                            "perception_link": "L4–L6 手感與全身張力",
                            "perception_link_ids": [],
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W004"]), 0,
            "純散文 + 明確 [] 不應觸發 W004"
        )

    def test_null_link_no_w004_no_w007(self):
        # *_link 值為 null（Python None）不觸發 W004，也不要求補 ids 欄位
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
        self.assertEqual(len(warnings["W004"]), 0, "null 值不應觸發 W004")
        self.assertEqual(len(warnings["W007"]), 0, "null 值不應觸發 W007")


class TestE007LinkIds(FixtureTestBase):
    """E007：links.*_link_ids 內含無法解析的 ID → ERROR。"""

    def test_unresolvable_link_id_triggers_e007(self):
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-bad",
                        "links": {
                            "mechanism_link": "接某個機制條目",
                            "mechanism_link_ids": ["no-such-injury"],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E007"]), 1,
            "無法解析的 mechanism_link_ids 應觸發 E007"
        )
        self.assertIn("no-such-injury", errors["E007"][0])

    def test_resolvable_link_ids_no_e007(self):
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "red-s"},
                    {
                        "id": "female-athlete-triad",
                        "links": {
                            "mechanism_link": "red-s",
                            "mechanism_link_ids": ["red-s"],
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E007"]), 0,
            "可解析的 mechanism_link_ids 不應觸發 E007"
        )

    def test_drill_id_in_link_ids_no_e007(self):
        self._write_yaml(
            self.drills_dir / "free.yaml",
            {"drills": [{"id": "Fr12"}]},
        )
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-drill",
                        "links": {
                            "perception_link": "可接 Fr12",
                            "perception_link_ids": ["Fr12"],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E007"]), 0,
            "Drills 的 ID 也算全域 ID 集合，不應觸發 E007"
        )

    def test_non_list_link_ids_triggers_e007(self):
        # 型別錯誤（寫成字串而非 list）也是 hard fail
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "red-s"},
                    {
                        "id": "inj-typed",
                        "links": {
                            "mechanism_link": "red-s",
                            "mechanism_link_ids": "red-s",
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E007"]), 1,
            "mechanism_link_ids 型別非 list 應觸發 E007"
        )
        self.assertIn("型別應為 list", errors["E007"][0])

    def test_empty_ids_list_no_e007(self):
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-empty",
                        "links": {
                            "mechanism_link": "純散文，無 ID 可連",
                            "mechanism_link_ids": [],
                        },
                    }
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E007"]), 0,
            "空陣列是合法宣告，不應觸發 E007"
        )


class TestW007MissingLinkIdsKey(FixtureTestBase):
    """W007：*_link 有值但連 *_link_ids 欄位都沒有 → WARN。"""

    def test_missing_ids_key_triggers_w007(self):
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-nokey",
                        "links": {
                            "technical_link": "某個技術說明散文",
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W007"]), 1,
            "technical_link 有值但缺 technical_link_ids 應觸發 W007"
        )
        self.assertIn("technical_link_ids", warnings["W007"][0])

    def test_empty_ids_key_no_w007(self):
        # 明確寫 [] = 已檢查、無 ID 可連 → 不算未處理
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-declared",
                        "links": {
                            "technical_link": "某個技術說明散文",
                            "technical_link_ids": [],
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W007"]), 0,
            "明確宣告 [] 不應觸發 W007"
        )

    def test_missing_ids_key_takes_precedence_over_w004(self):
        # 缺欄位時只報 W007（未處理），不重複報 W004（脫節）
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {"id": "red-s"},
                    {
                        "id": "inj-both",
                        "links": {"mechanism_link": "red-s"},
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(len(warnings["W007"]), 1, "缺欄位應報 W007")
        self.assertEqual(len(warnings["W004"]), 0, "缺欄位時不應重複報 W004")

    def test_link_ids_keys_never_trigger_w005(self):
        # *_link_ids 是已登錄的機器鍵，不可被當成未知子鍵
        self._write_yaml(
            self.canonical_dir / "injuries.yaml",
            {
                "injuries": [
                    {
                        "id": "inj-w005",
                        "links": {
                            "mechanism_link": "散文",
                            "mechanism_link_ids": [],
                            "technical_link_ids": [],
                            "perception_link_ids": [],
                        },
                    }
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W005"]), 0,
            "*_link_ids 不應觸發 W005"
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


class TestE006CrossRefIds(FixtureTestBase):
    """E006：cross_ref_ids 內含無法解析的 ID → ERROR。"""

    def test_unresolvable_cross_ref_id_triggers_e006(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {
                        "id": "free.err24",
                        "public": {
                            "cross_ref": "free.tech.7（S 形划水）、free.tech.999（不存在）",
                            "cross_ref_ids": ["free.tech.7", "free.tech.999"],
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E006"]), 1,
            "cross_ref_ids 內不存在的 ID 應觸發 E006"
        )
        self.assertIn("free.tech.999", errors["E006"][0])

    def test_resolvable_cross_ref_ids_no_e006(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {"id": "back.err2"},
                    {
                        "id": "free.err24",
                        "public": {
                            "cross_ref": "free.tech.7（S 形划水）、back.err2（仰式同樣誤區）",
                            "cross_ref_ids": ["free.tech.7", "back.err2"],
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E006"]), 0,
            "全部可解析的 cross_ref_ids 不應觸發 E006"
        )

    def test_cross_ref_ids_counts_as_edge_for_w003(self):
        # 2026-09-03：W003 原本只認 links.* 與 movement 關聯欄位，不認
        # cross_ref_ids，於是被 cross_ref 串起來的條目照樣被報成孤兒（實測
        # 修完少 45 筆）。這個測試同時釘住出邊與入邊，且指向的層是 diagnostic
        # ——三層都要算，只認 entry 頂層會漏掉最常用的那一層。
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {
                        "id": "free.err24",
                        "diagnostic": {"cross_ref_ids": ["free.tech.7"]},
                    },
                    {"id": "free.tech.99"},
                ]
            },
        )
        _, warnings, _ = self._run()
        orphans = "\n".join(warnings["W003"])
        self.assertNotIn(
            "free.err24", orphans,
            "有 diagnostic.cross_ref_ids 出邊的條目不該被報成孤兒",
        )
        self.assertNotIn(
            "free.tech.7", orphans,
            "被 diagnostic.cross_ref_ids 指到的條目不該被報成孤兒",
        )
        self.assertIn(
            "free.tech.99", orphans,
            "完全沒有進出邊的條目仍應被報成孤兒（否則這個測試無法證偽）",
        )

    def test_unresolvable_cross_ref_id_in_diagnostic_triggers_e006(self):
        # 2026-09-03：契約檢查原本只跑 entry 頂層與 public，diagnostic 層完全沒看。
        # stroke-demands 有一筆把 ID 陣列寫進 diagnostic.cross_ref 而驗證器沉默通過，
        # 才發現這個盲區。這個測試釘住「diagnostic 層也在契約範圍內」。
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {
                        "id": "free.err24",
                        "diagnostic": {
                            "cross_ref_ids": ["free.tech.7", "free.tech.999"],
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E006"]), 1,
            "diagnostic.cross_ref_ids 內不存在的 ID 應觸發 E006"
        )
        self.assertIn("free.tech.999", errors["E006"][0])
        self.assertIn("diagnostic", errors["E006"][0])

    def test_drill_id_in_cross_ref_ids_no_e006(self):
        # Drill ID（Drills/*.yaml，不含點號）也是合法解析目標
        self._write_yaml(
            self.drills_dir / "free.yaml",
            {"drills": [{"id": "FrBr3", "name": "連續涓流吐氣"}]},
        )
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "breast.err17",
                        "public": {
                            "cross_ref": "自由式 FrBr3（連續涓流吐氣 drill）通用呼吸原則",
                            "cross_ref_ids": ["FrBr3"],
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertEqual(
            len(errors["E006"]), 0, "Drill ID 應可解析，不觸發 E006"
        )

    def test_non_list_cross_ref_ids_triggers_e006(self):
        # 型別錯誤（字串而非 list）同樣無法解析成穩定 ID → E006
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {
                        "id": "free.err24",
                        "public": {
                            "cross_ref": "free.tech.7（S 形划水）",
                            "cross_ref_ids": "free.tech.7",
                        },
                    },
                ]
            },
        )
        errors, _, _ = self._run()
        self.assertGreater(
            len(errors["E006"]), 0,
            "cross_ref_ids 型別不是 list 應觸發 E006"
        )


class TestW001CrossRefIdsOutOfSync(FixtureTestBase):
    """W001：cross_ref 內疑似穩定 ID 未同步到 cross_ref_ids → WARN。"""

    def test_id_in_cross_ref_missing_from_ids_triggers_w001(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {"id": "back.err2"},
                    {
                        "id": "free.err24",
                        "public": {
                            # 只登錄了一個，back.err2 漏掉
                            "cross_ref": "free.tech.7（S 形划水）、back.err2（仰式同樣誤區）",
                            "cross_ref_ids": ["free.tech.7"],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W001"]), 1,
            "cross_ref 有 ID 未列入 cross_ref_ids 應觸發 W001"
        )
        self.assertIn("back.err2", warnings["W001"][0])

    def test_all_ids_synced_no_w001(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {"id": "free.tech.7"},
                    {"id": "back.err2"},
                    {
                        "id": "free.err24",
                        "public": {
                            "cross_ref": "free.tech.7（S 形划水）、back.err2（仰式同樣誤區）",
                            "cross_ref_ids": ["free.tech.7", "back.err2"],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W001"]), 0,
            "cross_ref_ids 已同步不應觸發 W001"
        )

    def test_prose_section_ref_with_empty_ids_no_w001(self):
        # 指向散文節號（無疑似 ID token）+ 明確空陣列 → 不觸發 W001 也不觸發 W006
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "free.err1",
                        "public": {
                            "cross_ref": "技術分析 §2.1、§3.1（三種風格對應三種回臂策略）",
                            "cross_ref_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W001"]), 0, "散文節號不含疑似 ID，不應觸發 W001"
        )
        self.assertEqual(
            len(warnings["W006"]), 0, "已宣告空陣列不應觸發 W006"
        )

    def test_unresolvable_lookalike_token_still_triggers_w001(self):
        # 疑似 ID 但全域解析不到（打錯字 / 指向已刪條目）仍要警告，不可靜默放過
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "free.err24",
                        "public": {
                            "cross_ref": "free.tech.999（已刪除的條目）",
                            "cross_ref_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W001"]), 1,
            "解析不到的疑似 ID token 仍應觸發 W001（可能是斷鏈或打錯字）"
        )

    def test_hyphen_and_err_style_ids_extracted(self):
        # extract_candidate_ids 必須抽得到 starts-turns.err10 / back.err2 這類形態
        tokens = validate_mod.extract_candidate_ids(
            "starts-turns.err10（起跳）、back.err2、free.tech.7、FrBr3"
        )
        self.assertEqual(
            tokens,
            ["starts-turns.err10", "back.err2", "free.tech.7", "FrBr3"],
        )


class TestW006CrossRefIdsMissing(FixtureTestBase):
    """W006：cross_ref 有值但完全沒有 cross_ref_ids 欄位 → WARN。"""

    def test_missing_cross_ref_ids_triggers_w006(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "free.err1",
                        "public": {
                            "cross_ref": "技術分析 §2.1（三種風格對應三種回臂策略）",
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W006"]), 1,
            "cross_ref 缺 cross_ref_ids 欄位應觸發 W006"
        )

    def test_empty_list_no_w006(self):
        # 空陣列 = 已檢查過、確認無 ID 可連，與「根本沒處理」必須分開
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "free.err1",
                        "public": {
                            "cross_ref": "技術分析 §2.1（三種風格對應三種回臂策略）",
                            "cross_ref_ids": [],
                        },
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W006"]), 0,
            "明確宣告空陣列不應觸發 W006"
        )

    def test_no_cross_ref_at_all_no_w006(self):
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {"points": [{"id": "free.err1", "public": {"misconception": "x"}}]},
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W006"]), 0, "沒有 cross_ref 就不該觸發 W006"
        )

    def test_entry_level_cross_ref_also_checked(self):
        # cross_ref 在條目頂層（非 public 層）同樣要被檢查
        self._write_yaml(
            self.canonical_dir / "entries.yaml",
            {
                "points": [
                    {
                        "id": "free.err1",
                        "cross_ref": "技術分析 §2.1",
                    },
                ]
            },
        )
        _, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W006"]), 1,
            "entry 頂層的 cross_ref 也應觸發 W006"
        )


class TestE008CategoryScope(unittest.TestCase):
    """E008：category 跨網域誤用。

    category 是三個互不相交的值空間（instructional / health / drills）
    共用同一個欄位名。E004 只能擋「不存在的值」，擋不住「health 的傷害
    類別出現在 drills 條目上」。
    """

    def _check(self, cat, domain, scope):
        errors = {"E008": []}
        validate_mod.check_category_scope(
            "f.yaml", "e1", {"category": cat}, domain,
            {cat: set(scope)}, {"category": {cat}}, errors,
        )
        return errors["E008"]

    def test_in_scope_passes(self):
        self.assertEqual(self._check("arm", "drills", ["drills"]), [])

    def test_out_of_scope_flagged(self):
        hits = self._check("A-shoulder-upper", "drills", ["health"])
        self.assertEqual(len(hits), 1)
        self.assertIn("drills", hits[0])

    def test_shared_value_allowed_in_both(self):
        self.assertEqual(self._check("kick", "drills", ["drills", "instructional"]), [])
        self.assertEqual(
            self._check("kick", "instructional", ["drills", "instructional"]), []
        )

    def test_missing_scope_is_fail_closed(self):
        # scope 未宣告視為空集合，不預設放行
        hits = self._check("arm", "drills", [])
        self.assertEqual(len(hits), 1)
        self.assertIn("未宣告", hits[0])

    def test_unknown_value_left_to_e004(self):
        # 值不在 taxonomy 時 E008 不重複報（E004 的職責）
        errors = {"E008": []}
        validate_mod.check_category_scope(
            "f.yaml", "e1", {"category": "bogus"}, "drills",
            {}, {"category": {"arm"}}, errors,
        )
        self.assertEqual(errors["E008"], [])

    def test_non_string_category_ignored(self):
        errors = {"E008": []}
        validate_mod.check_category_scope(
            "f.yaml", "e1", {"category": ["a"]}, "drills",
            {}, {"category": set()}, errors,
        )
        self.assertEqual(errors["E008"], [])


class TestE009FileCategories(unittest.TestCase):
    """E009 / W010：條目 category 與該檔 categories 區塊互相涵蓋。

    這組檢查對應一個實際線上 bug：2026-07-26 有 10 張卡片的分類標籤是
    空字串，因為條目的 category 沒宣告在該檔的 categories 區塊裡，
    而 Hugo 的 index 查不到 key 只會靜默回空字串。
    """

    def _run(self, declared, used):
        errors, warnings = {"E009": []}, {"W010": []}
        validate_mod.check_file_categories(
            "f.yaml",
            {"categories": declared},
            [[{"id": f"e{i}", "category": c} for i, c in enumerate(used)]],
            errors, warnings,
        )
        return errors["E009"], warnings["W010"]

    def test_undeclared_category_flagged(self):
        e, _ = self._run([{"key": "kick"}], ["kick", "body-position"])
        self.assertEqual(len(e), 1)
        self.assertIn("body-position", e[0])

    def test_declared_but_unused_is_dead_label(self):
        _, w = self._run([{"key": "kick"}, {"key": "posture"}], ["kick"])
        self.assertEqual(len(w), 1)
        self.assertIn("posture", w[0])

    def test_exact_match_clean(self):
        e, w = self._run([{"key": "kick"}, {"key": "pull"}], ["kick", "pull"])
        self.assertEqual((e, w), ([], []))

    def test_id_key_shape_accepted(self):
        # injuries.yaml 的 categories 用 id/zh，不是 key/name_zh
        e, w = self._run([{"id": "A-shoulder-upper"}], ["A-shoulder-upper"])
        self.assertEqual((e, w), ([], []))

    def test_no_categories_block_skipped(self):
        errors, warnings = {"E009": []}, {"W010": []}
        validate_mod.check_file_categories(
            "f.yaml", {}, [[{"id": "e1", "category": "kick"}]],
            errors, warnings,
        )
        self.assertEqual((errors["E009"], warnings["W010"]), ([], []))


class TestS3bSourceGranularity(FixtureTestBase):
    """S3b：W009 的三個豁免——citation 承載、祖先繼承、evidence_from。

    S3b triage 實測 270 筆 W009 只有 112 筆是真缺口，其餘 158 筆分兩類誤判：
      101 筆  references[] 元素自帶 citation（元素本身就是一筆來源）
       57 筆  來源登錄在父層，certainty 標在子區塊（粒度差，不是缺口）
    這個類別把三個豁免各鎖一條負向測試，避免日後重構把誤判放回來。
    """

    def _point(self, public: dict) -> dict:
        return {
            "categories": [{"key": "concept", "name_zh": "概念"}],
            "points": [{
                "id": "free.tech.900",
                "stroke": "free",
                "category": "concept",
                "public": public,
            }],
        }

    def test_citation_counts_as_display_source(self):
        """references[].citation 是來源顯示字串 → W002（缺機器鍵），不是 W009。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._point({
                "references": [
                    {"citation": "Gonjo et al. 2020, PMC7824457",
                     "certainty": "\U0001F7E2"},
                ],
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W009"]), 0,
            "自帶 citation 的區塊不該被判成「拿不出任何來源」",
        )
        self.assertGreater(
            len(warnings["W002"]), 0,
            "citation 有字串但缺 source_ids → 應歸 W002（純遷移）",
        )
        self.assertIn("citation 顯示字串", warnings["W002"][0])

    def test_ancestor_source_exempts_child_block(self):
        """父層已有 source_ids，子區塊標 🟢 不算缺來源（粒度差）。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._point({
                "source_ids": ["src.test-one"],
                "sources": ["Test Source 2020"],
                "mechanism": {"certainty": "\U0001F7E2", "text": "子區塊主張"},
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W009"]), 0,
            "來源在正上方一層時，子區塊不是缺口",
        )

    def test_ancestor_exemption_does_not_leak_across_entries(self):
        """繼承只沿同一顆樹；隔壁條目有來源不能豁免本條目。"""
        data = {
            "categories": [{"key": "concept", "name_zh": "概念"}],
            "points": [
                {
                    "id": "free.tech.901",
                    "stroke": "free",
                    "category": "concept",
                    "public": {
                        "source_ids": ["src.test-one"],
                        "sources": ["Test Source 2020"],
                    },
                },
                {
                    "id": "free.tech.902",
                    "stroke": "free",
                    "category": "concept",
                    "public": {
                        "mechanism": {
                            "certainty": "\U0001F7E2", "text": "無來源主張",
                        },
                    },
                },
            ],
        }
        self._write_yaml(self.canonical_dir / "instructional" / "ta.yaml", data)
        errors, warnings, _ = self._run()
        self.assertGreater(
            len(warnings["W009"]), 0,
            "同檔隔壁條目的來源不得豁免本條目",
        )
        self.assertIn("free.tech.902", warnings["W009"][0])

    def test_evidence_from_exempts_synthesis_line(self):
        """綜述句以 evidence_from 指出證據所在的子條目 → 合法歸屬。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._point({
                "mechanism": {
                    "certainty": "\U0001F7E2",
                    "text": "把底下條目濃縮成一句",
                    "evidence_from": ["free.tech.1", "free.tech.2"],
                },
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W009"]), 0)

    def test_empty_evidence_from_is_not_a_declaration(self):
        """`evidence_from: []` 不算宣告（沒指到任何條目）。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._point({
                "mechanism": {
                    "certainty": "\U0001F7E2",
                    "text": "空宣告",
                    "evidence_from": [],
                },
            }),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(warnings["W009"]), 0)


class TestW011PractitionerEvidence(FixtureTestBase):
    """W011：🟠 教練觀測必須交代 observation_basis。"""

    def _entry(self, block: dict) -> dict:
        return {
            "categories": [{"key": "concept", "name_zh": "概念"}],
            "points": [{
                "id": "free.tech.910",
                "stroke": "free",
                "category": "concept",
                "public": {"mechanism": block},
            }],
        }

    def test_orange_without_basis_warns(self):
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({"certainty": "\U0001F7E0", "text": "教練觀察到的現象"}),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(warnings["W011"]), 0)
        self.assertIn("observation_basis", warnings["W011"][0])

    def test_orange_with_basis_passes(self):
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({
                "certainty": "\U0001F7E0",
                "text": "教練觀察到的現象",
                "observation_basis": "作者教學實務，成人初學 30+ 人；未在競技族群驗證",
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W011"]), 0)

    def test_orange_with_external_source_passes(self):
        """引外部教練體系的觀測（如 Race Club 影像分析）→ 依據可追，不報。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({
                "certainty": "\U0001F7E0",
                "text": "Race Club 影像觀察數據",
                "sources": ["The Race Club, Fundamentals of Fast Swimming Ch 6"],
                "source_ids": ["src.test-one"],
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(warnings["W011"]), 0)

    def test_orange_never_requires_source_ids(self):
        """🟠 不進 W009——教練觀測不該被要求文獻來源。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({
                "certainty": "\U0001F7E0",
                "text": "教練觀察",
                "observation_basis": "作者教學實務",
            }),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(
            len(warnings["W009"]), 0,
            "W009 只問 🟢/🟡；🟠 被拉進來就是逼人替自己的觀察硬找文獻",
        )


class TestE010DiagnosticLeak(FixtureTestBase):
    """E010：診斷型鍵名不得出現在 public 子樹內。

    sync_vortex.py 是白名單（`rec.update(pub)`），所以 diagnostic 同層鍵本來
    就不會外流；唯一的洩漏路徑是把判讀語寫進 public 裡面。
    """

    def _entry(self, public: dict, diagnostic: dict | None = None) -> dict:
        point = {
            "id": "free.tech.920",
            "stroke": "free",
            "category": "concept",
            "public": public,
        }
        if diagnostic is not None:
            point["diagnostic"] = diagnostic
        return {
            "categories": [{"key": "concept", "name_zh": "概念"}],
            "points": [point],
        }

    def test_probe_under_public_is_error(self):
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({
                "summary": "公開說明",
                "perception_probe": {"principle": "泳者說 X 才算到位"},
            }),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(errors["E010"]), 0)
        self.assertIn("perception_probe", errors["E010"][0])

    def test_probe_under_diagnostic_is_fine(self):
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry(
                {"summary": "公開說明"},
                {"perception_probe": {"principle": "泳者說 X 才算到位"}},
            ),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(errors["E010"]), 0)

    def test_nested_under_public_still_caught(self):
        """埋在 public 更深處一樣要抓到（in_public 沿子樹傳遞）。"""
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._entry({
                "summary": "公開說明",
                "detail": {"items": [{"discriminators": ["講對詞不算"]}]},
            }),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(errors["E010"]), 0)
        self.assertIn("discriminators", errors["E010"][0])


class TestE011EvidenceFromResolvable(FixtureTestBase):
    """E011：evidence_from 是 W009 的豁免路徑，其 ID 必須解析得到。

    不驗證的話，隨便寫一個不存在的 ID 就能讓 W009 消失——豁免必須有代價。
    """

    def _file(self, evidence_from) -> dict:
        return {
            "categories": [{"key": "concept", "name_zh": "概念"}],
            "points": [
                {
                    "id": "free.tech.930",
                    "stroke": "free",
                    "category": "concept",
                    "public": {
                        "summary": "綜述句",
                        "premise": {
                            "certainty": "\U0001F7E2",
                            "text": "本句結論由子條目承擔",
                            "evidence_from": evidence_from,
                        },
                    },
                },
                {
                    "id": "free.tech.931",
                    "stroke": "free",
                    "category": "concept",
                    "public": {
                        "summary": "承載證據的子條目",
                        "evidence": [
                            {
                                "certainty": "\U0001F7E2",
                                "text": "實測數據",
                                "source_ids": ["src.real-one"],
                            }
                        ],
                    },
                },
            ],
        }

    def test_resolvable_id_passes_and_exempts_w009(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.real-one", "type": "other",
                           "verification_status": "unverified",
                           "display": "來源 A"}]),
        )
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._file(["free.tech.931"]),
        )
        errors, warnings, _ = self._run()
        self.assertEqual(len(errors["E011"]), 0)
        self.assertEqual(
            [w for w in warnings["W009"] if "free.tech.930" in w], []
        )

    def test_unresolvable_id_is_error(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.real-one", "type": "other",
                           "verification_status": "unverified",
                           "display": "來源 A"}]),
        )
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._file(["free.tech.does-not-exist"]),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(errors["E011"]), 0)
        self.assertIn("free.tech.does-not-exist", errors["E011"][0])

    def test_wrong_type_is_error(self):
        self._write_yaml(
            self.canonical_dir / "_sources.yaml",
            make_sources([{"id": "src.real-one", "type": "other",
                           "verification_status": "unverified",
                           "display": "來源 A"}]),
        )
        self._write_yaml(
            self.canonical_dir / "instructional" / "ta.yaml",
            self._file("free.tech.931"),
        )
        errors, warnings, _ = self._run()
        self.assertGreater(len(errors["E011"]), 0)
        self.assertIn("型別應為 list", errors["E011"][0])


class TestDomainOf(unittest.TestCase):
    """domain_of：由相對路徑推導網域，Windows 反斜線也要吃。"""

    def test_canonical_domain(self):
        self.assertEqual(
            validate_mod.domain_of("canonical/instructional/teaching-errors.yaml"),
            "instructional",
        )

    def test_windows_separator(self):
        self.assertEqual(
            validate_mod.domain_of(r"canonical\health\injuries.yaml"), "health"
        )

    def test_drills(self):
        self.assertEqual(
            validate_mod.domain_of("Drills/drills_freestyle.yaml"), "drills"
        )

    def test_canonical_root_file(self):
        self.assertEqual(validate_mod.domain_of("canonical/_sources.yaml"), "_root")


if __name__ == "__main__":
    unittest.main(verbosity=2)
