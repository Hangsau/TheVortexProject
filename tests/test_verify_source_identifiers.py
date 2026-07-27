import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import verify_source_identifiers as verifier


class TestMetadataParsing(unittest.TestCase):
    def test_pubmed_metadata(self):
        record = {
            "uid": "123",
            "title": "Swimming study",
            "pubdate": "2024 Jan",
            "fulljournalname": "Journal",
            "authors": [{"name": "Smith J"}],
            "articleids": [{"idtype": "doi", "value": "10.1/x"}],
        }
        metadata = verifier.pubmed_metadata(record)
        self.assertEqual(2024, metadata["year"])
        self.assertEqual(["Smith J"], metadata["authors"])
        self.assertEqual("10.1/x", metadata["identifier"]["doi"])

    def test_crossref_metadata(self):
        message = {
            "DOI": "10.1/x",
            "title": ["Title"],
            "author": [{"given": "Jane", "family": "Smith"}],
            "published": {"date-parts": [[2023, 1, 1]]},
            "container-title": ["Journal"],
            "type": "journal-article",
        }
        metadata = verifier.crossref_metadata(message)
        self.assertEqual("Title", metadata["title"])
        self.assertEqual(2023, metadata["year"])
        self.assertEqual("journal-article", metadata["type"])


class TestComparison(unittest.TestCase):
    def test_author_and_year_match(self):
        source = {"authors": ["Smith"], "year": 2024, "identifier": {"pmid": "123"}}
        metadata = {"authors": ["Jane Smith"], "year": 2024}
        decision, _reasons = verifier.compare_source(source, metadata)
        self.assertEqual("matched", decision)

    def test_mismatch_is_not_auto_verified(self):
        source = {"authors": ["Smith"], "year": 2024, "identifier": {"pmid": "123"}}
        metadata = {"authors": ["Jones A"], "year": 2022}
        decision, _reasons = verifier.compare_source(source, metadata)
        self.assertEqual("mismatch", decision)

    def test_identifier_echo_with_wrong_bibliography_requires_correction(self):
        source = {
            "display": "Smith 2024 PMID 123",
            "authors": ["Smith"],
            "year": 2024,
            "identifier": {"pmid": "123"},
        }
        metadata = {"title": "Different", "authors": ["Jones A"], "year": 2022}
        decision, _reasons = verifier.compare_source(source, metadata)
        self.assertEqual("matched_with_correction", decision)

    def test_identifier_only_needs_echo(self):
        metadata = {"authors": ["Jones A"], "year": 2022}
        matched, _ = verifier.compare_source(
            {"display": "PMID 123", "identifier": {"pmid": "123"}}, metadata
        )
        review, _ = verifier.compare_source(
            {"display": "some paper", "identifier": {"pmid": "123"}}, metadata
        )
        self.assertEqual("matched", matched)
        self.assertEqual("needs_review", review)

    def test_title_can_confirm_identifier_without_author_fields(self):
        source = {
            "display": "The Backstroke Swimming Start: State of the Art",
            "identifier": {"pmcid": "PMC1"},
        }
        metadata = {
            "title": "The backstroke swimming start: state of the art.",
            "authors": ["de Jesus K"],
            "year": 2014,
        }
        decision, _reasons = verifier.compare_source(source, metadata)
        self.assertEqual("matched", decision)


class TestBatchLookup(unittest.TestCase):
    def test_pubmed_lookup_uses_returned_records(self):
        def fetcher(_url):
            return {
                "result": {
                    "uids": ["123"],
                    "123": {"uid": "123", "title": "T", "pubdate": "2020"},
                }
            }

        metadata, errors = verifier.lookup_pubmed(["123"], fetcher)
        self.assertEqual([], errors)
        self.assertEqual("T", metadata["123"]["title"])


if __name__ == "__main__":
    unittest.main()
