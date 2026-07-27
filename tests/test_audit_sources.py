import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import audit_sources


class TestSourceAudit(unittest.TestCase):
    def test_normalize_identifier(self):
        self.assertEqual("10.1000/xyz", audit_sources.normalize_identifier("doi", "https://doi.org/10.1000/XYZ"))
        self.assertEqual("10.1111/sms.14454", audit_sources.normalize_identifier("doi", "10.1111/sms.14454（DOI 待驗證）"))
        self.assertEqual("12345", audit_sources.normalize_identifier("pmid", "PMID 12345"))
        self.assertEqual("PMC42", audit_sources.normalize_identifier("pmcid", "42"))
        self.assertEqual("9781234567890", audit_sources.normalize_identifier("isbn", "978-1-234-56789-0"))

    def test_lane_precedence_keeps_compound_out_of_auto_dereference(self):
        source = {
            "identifier": {"doi": "10.1000/x"},
            "notes": "顯示字串疑似含多筆文獻（以 ; 分隔）",
        }
        flags = audit_sources.source_flags(source)
        self.assertEqual("compound_split", audit_sources.triage_lane(source, flags))

    def test_internal_reference_is_not_treated_as_external_source(self):
        source = {"display": "Research/心理/03_動機.md#section"}
        flags = audit_sources.source_flags(source)
        self.assertIn("internal_reference", flags)
        self.assertEqual("internal_reference", audit_sources.triage_lane(source, flags))

    def test_verified_source_is_complete(self):
        source = {
            "verification_status": "verified",
            "identifier": {"pmid": "123"},
        }
        self.assertEqual("complete", audit_sources.triage_lane(source, []))

    def test_incomplete_verified_source_fails_closed(self):
        with self.assertRaises(ValueError):
            audit_sources.build_audit([
                {
                    "id": "src.bad",
                    "display": "bad",
                    "type": "other",
                    "verification_status": "verified",
                }
            ])

    def test_identifier_collisions_are_normalized(self):
        sources = [
            {"id": "src.a", "identifier": {"doi": "10.1000/ABC"}},
            {"id": "src.b", "identifier": {"doi": "https://doi.org/10.1000/abc"}},
        ]
        self.assertEqual(
            [{"kind": "doi", "value": "10.1000/abc", "source_ids": ["src.a", "src.b"]}],
            audit_sources.identifier_collisions(sources),
        )

    def test_audit_is_deterministic_and_serializable(self):
        sources = [
            {"id": "src.b", "display": "B", "type": "other", "verification_status": "unverified"},
            {
                "id": "src.a",
                "display": "A",
                "type": "other",
                "verification_status": "unverified",
                "identifier": {"pmid": "123"},
            },
        ]
        first = audit_sources.build_audit(sources)
        second = audit_sources.build_audit(list(reversed(sources)))
        self.assertEqual(first, second)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "audit.json"
            audit_sources.write_audit(first, output)
            self.assertEqual(first, json.loads(output.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
