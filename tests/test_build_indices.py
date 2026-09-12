import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_indices


class TestOwnedBlocks(unittest.TestCase):
    def test_nested_entry_does_not_leak_into_parent(self):
        parent = {
            "id": "parent",
            "category": "parent-tag",
            "children": [{"id": "child", "category": "child-tag"}],
        }
        blocks = [block for _path, block in build_indices.iter_owned_blocks(parent)]
        self.assertEqual(["parent"], [b["id"] for b in blocks if "id" in b])

    def test_nested_entry_source_does_not_leak_into_parent(self):
        parent = {
            "id": "parent",
            "children": [{"id": "child", "source_ids": ["src.child"]}],
        }
        self.assertEqual([], list(build_indices.owned_source_usages(parent)))


class TestGapDetection(unittest.TestCase):
    def test_problem_coverage_all_link_combinations(self):
        # Exercise all eight combinations and keep water-only intervention apart.
        entries = []
        for mechanism in (False, True):
            for drill in (False, True):
                for land in (False, True):
                    entries.append({"id": f"prob.free.case-{len(entries)}", "stroke": "free", "links": {
                        "technical_analysis": ["tech"] if mechanism else [],
                        "drills": ["drill"] if drill else [],
                        "interventions": ["land"] if land else [],
                        "water_interventions": ["water"],
                    }})
        result = build_indices.problem_coverage(entries)
        self.assertEqual(result["counts"], {"mechanism_drill_land": 1, "mechanism_drill_no_land": 1, "mechanism_no_drill": 2, "no_mechanism": 4})
        self.assertEqual(result["by_stroke"]["free"]["with_land"], 4)
        self.assertEqual(len(result["with_water_interventions"]), 8)
        self.assertEqual([len(v) for v in result["missing"].values()], [4, 4, 4])
        flattened = [i for ids in result["buckets"].values() for i in ids]
        self.assertEqual(len(set(flattened)), 8)
        self.assertEqual(build_indices.problem_coverage([])["total"], 0)

    def test_high_certainty_scanner_is_live(self):
        data = {
            "points": [
                {"id": "missing", "certainty": "🟢"},
                {"id": "covered", "certainty": "🟡", "source_ids": ["src.ok"]},
            ]
        }
        gaps = build_indices.find_high_certainty_without_source("fixture.yaml", data)
        self.assertEqual(["missing"], [gap["id"] for gap in gaps])

    def test_unlinked_records_uses_the_validator_edge_definition(self):
        # 錯誤 19（2026-09-03）：這裡曾自己重寫入邊、只認 links.*，漏掉 movement
        # 關聯欄位與 cross_ref_ids，孤兒虛報成 557（驗證器同時是 403）——而
        # docstring 當時就寫著 "Mirror validate.py W003"。這個測試釘住「入邊也
        # 走 validate.collect_outbound_ids()」：兩筆只靠 cross_ref_ids 相連的
        # 條目，在舊寫法下會雙雙被報成孤兒。
        records = [
            {"id": "a", "domain": "canonical", "file": "f.yaml", "path": "$"},
            {"id": "b", "domain": "canonical", "file": "f.yaml", "path": "$"},
            {"id": "lonely", "domain": "canonical", "file": "f.yaml", "path": "$"},
        ]
        entry_by_id = {
            "a": {"id": "a", "cross_ref_ids": ["b"]},
            "b": {"id": "b"},
            "lonely": {"id": "lonely"},
        }
        gaps = build_indices.unlinked_records(records, entry_by_id)
        self.assertEqual(["lonely"], [gap["id"] for gap in gaps])


class TestGeneratedViews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.views = build_indices.build_views(ROOT)

    def test_four_views_and_unique_records(self):
        self.assertEqual(
            {
                "content_index.json",
                "tag_reverse_index.json",
                "source_reverse_index.json",
                "gap_report.json",
            },
            set(self.views),
        )
        content = self.views["content_index.json"]
        ids = [record["id"] for record in content["records"]]
        self.assertEqual(content["record_count"], len(ids))
        self.assertEqual(len(ids), len(set(ids)))

    def test_reverse_indices_only_reference_content_records(self):
        content_ids = {
            record["id"] for record in self.views["content_index.json"]["records"]
        }
        tag_index = self.views["tag_reverse_index.json"]["fields"]
        for values in tag_index.values():
            for record_ids in values.values():
                self.assertTrue(set(record_ids) <= content_ids)

        for source in self.views["source_reverse_index.json"]["sources"]:
            self.assertEqual(source["usage_count"], len(source["usages"]))
            self.assertTrue({u["id"] for u in source["usages"]} <= content_ids)

    def test_gap_summary_matches_payloads(self):
        report = self.views["gap_report.json"]
        self.assertEqual(
            report["summary"]["high_certainty_without_source"],
            len(report["high_certainty_without_source"]),
        )
        self.assertEqual(
            report["summary"]["unused_taxonomy_values"],
            len(report["unused_taxonomy_values"]),
        )
        self.assertEqual(
            report["summary"]["unlinked_records"],
            len(report["unlinked_records"]),
        )

    def test_real_problem_partition_and_gap_contract(self):
        import yaml
        entries = yaml.safe_load((ROOT / "canonical/instructional/problems.yaml").read_text(encoding="utf-8"))["problems"]
        coverage = self.views["gap_report.json"]["problem_coverage"]
        self.assertEqual(coverage["total"], 73)
        self.assertEqual(sum(coverage["counts"].values()), 73)
        covered = [i for ids in coverage["buckets"].values() for i in ids]
        self.assertEqual(len(set(covered)), 73)
        self.assertEqual(set(covered), {entry["id"] for entry in entries})
        for gap, ids in coverage["missing"].items():
            self.assertEqual(set(ids), {entry["id"] for entry in entries if gap in entry["coverage_gap"]})
        content_ids = {r["id"] for r in self.views["content_index.json"]["records"]}
        self.assertLessEqual(set(covered), content_ids)
        self.assertEqual(sum(s["with_land"] for s in coverage["by_stroke"].values()), 6)

    def test_serialization_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            build_indices.write_views(self.views, output)
            first = {path.name: path.read_bytes() for path in output.iterdir()}
            build_indices.write_views(build_indices.build_views(ROOT), output)
            second = {path.name: path.read_bytes() for path in output.iterdir()}
        self.assertEqual(first, second)
        for payload in second.values():
            json.loads(payload.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
