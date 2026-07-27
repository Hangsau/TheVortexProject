import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

import sys

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import search_source_bibliography as searcher


def candidate(title, authors, year, doi="10.1/x", score=50.0, container="Journal"):
    return {
        "title": title,
        "authors": authors,
        "year": year,
        "container": container,
        "type": "journal-article",
        "identifier": {"doi": doi},
        "crossref_score": score,
    }


class TestCandidateRanking(unittest.TestCase):
    def test_unique_author_year_is_review_only(self):
        source = {"display": "Smith et al. 2024", "authors": ["Smith"], "year": 2024}
        decision, ranked = searcher.classify_candidates(
            source, [candidate("Unstated title", ["Jane Smith"], 2024)]
        )
        self.assertEqual("unique_author_year", decision)
        self.assertEqual(1.0, ranked[0]["signals"]["author_coverage"])

    def test_title_hint_strengthens_but_does_not_verify(self):
        source = {
            "display": "Smith 2024, Swimming propulsion mechanics",
            "authors": ["Smith"],
            "year": 2024,
        }
        decision, _ = searcher.classify_candidates(
            source, [candidate("Swimming propulsion mechanics", ["Jane Smith"], 2024)]
        )
        self.assertEqual("strong_review_candidate", decision)

    def test_multiple_exact_matches_are_ambiguous(self):
        source = {"display": "Smith 2024", "authors": ["Smith"], "year": 2024}
        decision, _ = searcher.classify_candidates(source, [
            candidate("A", ["Jane Smith"], 2024, "10.1/a"),
            candidate("B", ["John Smith"], 2024, "10.1/b"),
        ])
        self.assertEqual("ambiguous_author_year", decision)

    def test_adjacent_year_is_separate_lane(self):
        source = {"display": "Smith 2024", "authors": ["Smith"], "year": 2024}
        decision, _ = searcher.classify_candidates(
            source, [candidate("A", ["Jane Smith"], 2025)]
        )
        self.assertEqual("near_year_candidate", decision)


class TestReport(unittest.TestCase):
    def test_only_bibliographic_lane_is_queried(self):
        seen = []

        def fetcher(url):
            seen.append(url)
            return {"message": {"items": [{
                "DOI": "10.1/x",
                "title": ["Swimming mechanics"],
                "author": [{"given": "Jane", "family": "Smith"}],
                "published": {"date-parts": [[2024]]},
                "container-title": ["Journal"],
                "type": "journal-article",
                "score": 90,
            }]}}

        sources = [
            {
                "id": "src.smith-2024",
                "display": "Smith 2024",
                "type": "other",
                "verification_status": "unverified",
                "authors": ["Smith"],
                "year": 2024,
            },
            {
                "id": "src.verified",
                "display": "Verified",
                "type": "journal-article",
                "verification_status": "verified",
                "authors": ["Smith"],
                "year": 2024,
                "identifier": {"doi": "10.1/v"},
            },
        ]
        report = searcher.build_report(sources, fetcher=fetcher, pause=0)
        self.assertEqual(1, report["candidate_count"])
        self.assertEqual(1, len(seen))
        self.assertEqual("src.smith-2024", report["results"][0]["id"])
        self.assertNotEqual("matched", report["results"][0]["decision"])


class TestRetries(unittest.TestCase):
    def test_429_is_retried(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b'{"message": {}}'
        with patch.object(searcher, "urlopen", side_effect=[
            HTTPError("https://example.test", 429, "slow down", {}, None),
            response,
        ]) as mocked, patch.object(searcher.time, "sleep"):
            payload = searcher.fetch_json("https://example.test", attempts=2)
        self.assertEqual({"message": {}}, payload)
        self.assertEqual(2, mocked.call_count)


if __name__ == "__main__":
    unittest.main()
