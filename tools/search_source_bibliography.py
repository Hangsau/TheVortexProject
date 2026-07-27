#!/usr/bin/env python3
"""Search Crossref for author/year source records and emit a review queue.

This S3c helper is deliberately non-mutating.  Author/year strings are not
unique identifiers, so even a high-scoring result remains a candidate until a
human checks it against the canonical usage context.

Usage:
    python tools/search_source_bibliography.py

Output:
    reports/source_bibliography_candidates.json
"""
from __future__ import annotations

import json
import re
import time
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import audit_sources
import verify_source_identifiers as identifier_verifier

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = ROOT / "reports" / "source_bibliography_candidates.json"
SCHEMA_VERSION = 1
USER_AGENT = "VortexBibliographySearch/1.0"
ROWS = 10


def fetch_json(url: str, timeout: int = 30, attempts: int = 4) -> dict:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(attempts):
        try:
            with urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == attempts - 1:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            delay = float(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
            time.sleep(delay)
    raise RuntimeError("unreachable retry loop")


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def meaningful_tokens(value: object) -> set[str]:
    stop = {"and", "the", "for", "with", "from", "study", "et", "al"}
    return {
        token for token in normalize_text(value).split()
        if len(token) >= 3 and token not in stop and not token.isdigit()
    }


def candidate_from_message(message: dict) -> dict:
    metadata = identifier_verifier.crossref_metadata(message)
    return {
        **metadata,
        "crossref_score": float(message.get("score") or 0.0),
    }


def author_coverage(expected: list[str], candidate: dict) -> float:
    expected_names = [normalize_text(author) for author in expected if normalize_text(author)]
    remote_names = [normalize_text(author) for author in candidate.get("authors") or []]
    if not expected_names:
        return 0.0
    hits = sum(any(name in remote for remote in remote_names) for name in expected_names)
    return hits / len(expected_names)


def display_overlap(display: str, candidate: dict) -> float:
    display_tokens = meaningful_tokens(display)
    candidate_tokens = meaningful_tokens(
        f"{candidate.get('title', '')} {candidate.get('container', '')}"
    )
    if not candidate_tokens:
        return 0.0
    return len(display_tokens & candidate_tokens) / len(candidate_tokens)


def rank_candidate(source: dict, candidate: dict) -> tuple[float, dict]:
    coverage = author_coverage(source.get("authors") or [], candidate)
    expected_year = source.get("year")
    remote_year = candidate.get("year")
    year_delta = abs(int(expected_year) - int(remote_year)) if expected_year and remote_year else None
    overlap = display_overlap(source.get("display", ""), candidate)
    score = coverage * 50.0 + overlap * 20.0
    if year_delta == 0:
        score += 30.0
    elif year_delta == 1:
        score += 15.0
    score += min(candidate.get("crossref_score", 0.0), 100.0) / 100.0
    signals = {
        "author_coverage": round(coverage, 3),
        "year_delta": year_delta,
        "display_overlap": round(overlap, 3),
        "rank_score": round(score, 3),
    }
    return score, signals


def classify_candidates(source: dict, candidates: list[dict]) -> tuple[str, list[dict]]:
    ranked = []
    for candidate in candidates:
        score, signals = rank_candidate(source, candidate)
        ranked.append({**candidate, "signals": signals, "_score": score})
    ranked.sort(
        key=lambda item: (
            -item["_score"],
            normalize_text(item.get("title")),
            normalize_text((item.get("identifier") or {}).get("doi")),
        )
    )
    for item in ranked:
        item.pop("_score", None)

    exact = [
        item for item in ranked
        if item["signals"]["author_coverage"] == 1.0
        and item["signals"]["year_delta"] == 0
    ]
    hinted = [item for item in exact if item["signals"]["display_overlap"] >= 0.25]
    nearby = [
        item for item in ranked
        if item["signals"]["author_coverage"] == 1.0
        and item["signals"]["year_delta"] == 1
    ]
    if len(hinted) == 1:
        decision = "strong_review_candidate"
    elif len(exact) == 1:
        decision = "unique_author_year"
    elif len(exact) > 1:
        decision = "ambiguous_author_year"
    elif nearby:
        decision = "near_year_candidate"
    else:
        decision = "no_candidate"
    return decision, ranked


def search_url(source: dict) -> str:
    year = int(source["year"])
    query = " ".join(source.get("authors") or [])
    params = {
        "query.author": query,
        "query.bibliographic": source.get("display", ""),
        "filter": f"from-pub-date:{year - 1}-01-01,until-pub-date:{year + 1}-12-31",
        "rows": ROWS,
    }
    return "https://api.crossref.org/works?" + urlencode(params)


def build_report(
    sources: list[dict],
    fetcher: Callable[[str], dict] = fetch_json,
    pause: float = 0.1,
) -> dict:
    candidates = []
    for source in sources:
        flags = audit_sources.source_flags(source)
        if audit_sources.triage_lane(source, flags) == "bibliographic_search":
            candidates.append(source)

    results = []
    decisions: Counter[str] = Counter()
    errors = []
    for source in sorted(candidates, key=lambda item: item["id"]):
        raw_items = []
        error = ""
        try:
            payload = fetcher(search_url(source))
            raw_items = (payload.get("message") or {}).get("items") or []
        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            error = str(exc)
            errors.append(f"{source['id']}: {exc}")
        parsed = [candidate_from_message(item) for item in raw_items if isinstance(item, dict)]
        decision, ranked = classify_candidates(source, parsed)
        if error:
            decision = "lookup_failed"
        decisions[decision] += 1
        results.append({
            "id": source["id"],
            "display": source.get("display", ""),
            "expected": {
                "authors": source.get("authors") or [],
                "year": source.get("year"),
            },
            "decision": decision,
            "error": error,
            "candidates": ranked,
        })
        if pause:
            time.sleep(pause)

    return {
        "schema_version": SCHEMA_VERSION,
        "retrieved_on": date.today().isoformat(),
        "candidate_count": len(candidates),
        "summary": dict(sorted(decisions.items())),
        "lookup_errors": errors,
        "results": results,
    }


def write_report(report: dict, path: Path = OUTPUT_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    report = build_report(audit_sources.load_sources())
    write_report(report)
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    print(f"Candidates: {report['candidate_count']}")
    print(f"Decisions: {report['summary']}")
    print(f"Lookup errors: {len(report['lookup_errors'])}")
    return 0 if not report["lookup_errors"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
