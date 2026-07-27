#!/usr/bin/env python3
"""Dereference strong source identifiers and emit a review report.

This S3c helper queries authoritative metadata registries for sources already
triaged into ``identifier_dereference`` by audit_sources.py. It never edits
canonical/_sources.yaml; decisions must be reviewed before a separate write
step marks records verified.

Usage:
    python tools/verify_source_identifiers.py

Output:
    reports/source_identifier_verification.json
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
from urllib.parse import quote
from urllib.request import Request, urlopen

import audit_sources

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = ROOT / "reports" / "source_identifier_verification.json"
SCHEMA_VERSION = 1
USER_AGENT = "VortexSourceVerifier/1.0"


def fetch_json(url: str, timeout: int = 30) -> dict:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def chunks(values: list[str], size: int) -> list[list[str]]:
    return [values[index:index + size] for index in range(0, len(values), size)]


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def extract_year(value: object) -> int | None:
    match = re.search(r"(?:19|20)\d{2}", str(value or ""))
    return int(match.group(0)) if match else None


def pubmed_metadata(record: dict) -> dict:
    article_ids = {
        item.get("idtype"): item.get("value")
        for item in (record.get("articleids") or [])
        if isinstance(item, dict) and item.get("idtype") and item.get("value")
    }
    return {
        "title": record.get("title", ""),
        "authors": [
            author.get("name", "")
            for author in (record.get("authors") or [])
            if isinstance(author, dict) and author.get("name")
        ],
        "year": extract_year(record.get("pubdate") or record.get("epubdate")),
        "container": record.get("fulljournalname", ""),
        "type": "journal-article",
        "identifier": {
            key: value for key, value in {
                "pmid": record.get("uid"),
                "pmcid": article_ids.get("pmc"),
                "doi": article_ids.get("doi"),
            }.items() if value
        },
    }


def crossref_metadata(message: dict) -> dict:
    published = message.get("published-print") or message.get("published-online") or message.get("published") or {}
    date_parts = published.get("date-parts") or []
    year = date_parts[0][0] if date_parts and date_parts[0] else None
    authors = []
    for author in message.get("author") or []:
        if not isinstance(author, dict):
            continue
        name = " ".join(part for part in (author.get("given"), author.get("family")) if part)
        if name:
            authors.append(name)
    crossref_type = message.get("type", "")
    source_type = "journal-article" if crossref_type == "journal-article" else "other"
    return {
        "title": (message.get("title") or [""])[0],
        "authors": authors,
        "year": year,
        "container": (message.get("container-title") or [""])[0],
        "type": source_type,
        "identifier": {
            key: value for key, value in {
                "doi": message.get("DOI"),
                "url": message.get("URL"),
            }.items() if value
        },
    }


def identifier_echoes_display(source: dict) -> bool:
    display = normalize_text(source.get("display"))
    identifier = source.get("identifier") or {}
    for kind, raw in identifier.items():
        value = audit_sources.normalize_identifier(kind, raw)
        if value and normalize_text(value) in display:
            return True
    return False


def title_matches_display(source: dict, metadata: dict) -> bool:
    display = normalize_text(source.get("display"))
    title = normalize_text(metadata.get("title"))
    if not display or not title:
        return False
    if len(title) >= 16 and (title in display or display in title):
        return True
    display_tokens = {token for token in display.split() if len(token) >= 3}
    title_tokens = {token for token in title.split() if len(token) >= 3}
    if not display_tokens or not title_tokens:
        return False
    overlap = len(display_tokens & title_tokens) / len(title_tokens)
    return overlap >= 0.65


def compare_source(source: dict, metadata: dict | None) -> tuple[str, list[str]]:
    if not metadata:
        return "lookup_failed", ["registry returned no metadata"]

    reasons = []
    expected_authors = source.get("authors") or []
    remote_authors = [normalize_text(author) for author in metadata.get("authors") or []]
    authors_ok = None
    if expected_authors:
        authors_ok = all(
            any(normalize_text(author) in remote for remote in remote_authors)
            for author in expected_authors
        )
        reasons.append(f"authors_match={authors_ok}")

    expected_year = source.get("year")
    year_ok = None
    if expected_year is not None:
        year_ok = int(expected_year) == metadata.get("year")
        reasons.append(f"year_match={year_ok}")

    echo = identifier_echoes_display(source)
    reasons.append(f"identifier_echo={echo}")
    title_match = title_matches_display(source, metadata)
    reasons.append(f"title_match={title_match}")

    explicit_checks = [check for check in (authors_ok, year_ok) if check is not None]
    if explicit_checks and not all(explicit_checks):
        if echo or title_match:
            return "matched_with_correction", reasons
        return "mismatch", reasons
    if authors_ok is True:
        return "matched", reasons
    if echo or title_match:
        return "matched", reasons
    return "needs_review", reasons


def lookup_pubmed(pmids: list[str], fetcher: Callable[[str], dict]) -> tuple[dict[str, dict], list[str]]:
    metadata: dict[str, dict] = {}
    errors = []
    for batch in chunks(sorted(set(pmids)), 100):
        if not batch:
            continue
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            f"?db=pubmed&id={','.join(batch)}&retmode=json"
        )
        try:
            payload = fetcher(url)
            result = payload.get("result", {})
            for pmid in batch:
                record = result.get(pmid)
                if isinstance(record, dict):
                    metadata[pmid] = pubmed_metadata(record)
                else:
                    errors.append(f"PMID {pmid}: missing from response")
        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"PubMed batch {batch[0]}..{batch[-1]}: {exc}")
    return metadata, errors


def convert_pmcids(pmcids: list[str], fetcher: Callable[[str], dict]) -> tuple[dict[str, dict], list[str]]:
    records: dict[str, dict] = {}
    errors = []
    for batch in chunks(sorted(set(pmcids)), 100):
        if not batch:
            continue
        ids = ",".join(batch)
        url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={ids}&format=json"
        try:
            payload = fetcher(url)
            for record in payload.get("records") or []:
                if isinstance(record, dict) and record.get("pmcid"):
                    records[record["pmcid"].upper()] = record
        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"PMCID batch {batch[0]}..{batch[-1]}: {exc}")
    return records, errors


def lookup_crossref(dois: list[str], fetcher: Callable[[str], dict]) -> tuple[dict[str, dict], list[str]]:
    metadata: dict[str, dict] = {}
    errors = []
    for doi in sorted(set(dois)):
        url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
        try:
            payload = fetcher(url)
            message = payload.get("message")
            if isinstance(message, dict):
                metadata[doi] = crossref_metadata(message)
            else:
                errors.append(f"DOI {doi}: missing message")
        except (HTTPError, URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"DOI {doi}: {exc}")
        time.sleep(0.1)
    return metadata, errors


def build_verification(sources: list[dict], fetcher: Callable[[str], dict] = fetch_json) -> dict:
    candidates = []
    for source in sources:
        flags = audit_sources.source_flags(source)
        if audit_sources.triage_lane(source, flags) == "identifier_dereference":
            candidates.append(source)

    pmids = []
    pmcids = []
    dois = []
    for source in candidates:
        identifier = source.get("identifier") or {}
        if identifier.get("pmid"):
            pmids.append(audit_sources.normalize_identifier("pmid", identifier["pmid"]))
        if identifier.get("pmcid"):
            pmcids.append(audit_sources.normalize_identifier("pmcid", identifier["pmcid"]))
        if identifier.get("doi"):
            dois.append(audit_sources.normalize_identifier("doi", identifier["doi"]))

    pmcid_records, errors = convert_pmcids(pmcids, fetcher)
    pmids.extend(
        str(record["pmid"])
        for record in pmcid_records.values()
        if record.get("pmid")
    )
    pubmed, pubmed_errors = lookup_pubmed(pmids, fetcher)
    crossref, crossref_errors = lookup_crossref(dois, fetcher)
    errors.extend(pubmed_errors)
    errors.extend(crossref_errors)

    results = []
    decisions: Counter[str] = Counter()
    for source in sorted(candidates, key=lambda item: item["id"]):
        identifier = source.get("identifier") or {}
        metadata = None
        registry = ""
        if identifier.get("pmid"):
            pmid = audit_sources.normalize_identifier("pmid", identifier["pmid"])
            metadata = pubmed.get(pmid)
            registry = "pubmed"
        elif identifier.get("pmcid"):
            pmcid = audit_sources.normalize_identifier("pmcid", identifier["pmcid"])
            converted = pmcid_records.get(pmcid, {})
            pmid = str(converted.get("pmid") or "")
            metadata = pubmed.get(pmid)
            registry = "pmc-idconv+pubmed"
        elif identifier.get("doi"):
            doi = audit_sources.normalize_identifier("doi", identifier["doi"])
            metadata = crossref.get(doi)
            registry = "crossref"

        decision, reasons = compare_source(source, metadata)
        decisions[decision] += 1
        results.append({
            "id": source["id"],
            "display": source.get("display", ""),
            "registry": registry,
            "decision": decision,
            "reasons": reasons,
            "current": {
                "type": source.get("type", "other"),
                "authors": source.get("authors", []),
                "year": source.get("year"),
                "identifier": identifier,
            },
            "resolved": metadata,
        })

    return {
        "schema_version": SCHEMA_VERSION,
        "retrieved_on": date.today().isoformat(),
        "candidate_count": len(candidates),
        "summary": dict(sorted(decisions.items())),
        "lookup_errors": errors,
        "results": results,
    }


def write_verification(report: dict, path: Path = OUTPUT_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    report = build_verification(audit_sources.load_sources())
    write_verification(report)
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    print(f"Candidates: {report['candidate_count']}")
    print(f"Decisions: {report['summary']}")
    print(f"Lookup errors: {len(report['lookup_errors'])}")
    return 0 if not report["lookup_errors"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
