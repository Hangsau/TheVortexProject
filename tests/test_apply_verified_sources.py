import unittest
from pathlib import Path

import sys
import yaml

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import apply_verified_sources as apply_verified


class TestApplyVerifiedSources(unittest.TestCase):
    def setUp(self):
        self.before = """schema_version: 2
# registry comment stays
sources:

  - id: src.a
    display: "Smith 2024 PMID 1"
    type: other
    verification_status: unverified
    authors: ["Smith"]
    year: 2024
    identifier:
      pmid: "1"
    notes: "keep me"

  - id: src.b
    display: "untouched"
    type: other
    verification_status: unverified
"""
        self.report = {
            "retrieved_on": "2026-07-27",
            "results": [
                {
                    "id": "src.a",
                    "decision": "matched",
                    "current": {"type": "review", "identifier": {"pmid": "1"}},
                    "resolved": {
                        "title": "Study",
                        "authors": ["Jane Smith"],
                        "year": 2024,
                        "container": "Journal",
                        "type": "journal-article",
                        "identifier": {"pmid": "1", "doi": "10.1/x"},
                    },
                },
                {"id": "src.b", "decision": "needs_review"},
            ],
        }

    def test_apply_is_surgical_and_preserves_display(self):
        after, selected = apply_verified.apply_results(self.before, self.report)
        apply_verified.assert_semantic_safety(self.before, after, selected)
        self.assertEqual(["src.a"], selected)
        self.assertIn("# registry comment stays", after)
        self.assertIn('notes: "keep me"', after)
        data = yaml.safe_load(after)
        sources = {source["id"]: source for source in data["sources"]}
        self.assertEqual("verified", sources["src.a"]["verification_status"])
        self.assertEqual("Study", sources["src.a"]["title"])
        self.assertEqual("review", sources["src.a"]["type"])
        self.assertEqual("10.1/x", sources["src.a"]["identifier"]["doi"])
        self.assertEqual("Smith 2024 PMID 1", sources["src.a"]["display"])
        second, second_ids = apply_verified.apply_results(after, self.report)
        self.assertEqual(after, second)
        self.assertEqual(selected, second_ids)

    def test_missing_required_metadata_fails_closed(self):
        report = {
            "retrieved_on": "2026-07-27",
            "results": [{"id": "src.a", "decision": "matched", "current": {}, "resolved": {}}],
        }
        with self.assertRaises(ValueError):
            apply_verified.apply_results(self.before, report)


if __name__ == "__main__":
    unittest.main()
