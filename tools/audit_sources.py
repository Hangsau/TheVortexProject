#!/usr/bin/env python3
"""Inventory Vortex source-registry debt without using network or LLM calls.

The output is a deterministic triage view for S3c. It separates records that
can be dereferenced mechanically from compound, internal, and ambiguous
records that require content judgment.

Usage:
    python tools/audit_sources.py

Output:
    reports/source_audit.json
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "canonical" / "_sources.yaml"
OUTPUT_FILE = ROOT / "reports" / "source_audit.json"
SCHEMA_VERSION = 1

STRONG_IDENTIFIER_KEYS = frozenset({"doi", "pmid", "pmcid", "isbn"})
SOURCE_TYPES = frozenset({
    "journal-article", "review", "book", "book-chapter", "guideline",
    "org-page", "dataset", "video", "other",
})
COMPOUND_MARKER = "疑似含多筆"
DUPLICATE_MARKER = "疑似與"
INSUFFICIENT_MARKER = "不足以唯一定位"
CONSENSUS_MARKER = "通則／共識"
INTERNAL_REFERENCE_RE = re.compile(r"(?:Research|research)[/\\]心理[/\\]")


def load_sources(path: Path = SOURCES_FILE) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("sources"), list):
        raise ValueError(f"invalid source registry: {path}")
    sources = [item for item in data["sources"] if isinstance(item, dict)]
    ids = [item.get("id") for item in sources]
    if any(not isinstance(source_id, str) or not source_id for source_id in ids):
        raise ValueError("every source must have a non-empty string id")
    duplicates = [source_id for source_id, count in Counter(ids).items() if count > 1]
    if duplicates:
        raise ValueError(f"duplicate source ids: {duplicates}")
    return sources


def validate_verified_contract(sources: list[dict]) -> None:
    problems = []
    for source in sources:
        source_id = source.get("id", "(missing)")
        if source.get("type") not in SOURCE_TYPES:
            problems.append(f"{source_id}: invalid type")
        if source.get("verification_status") != "verified":
            continue
        required = {
            "title": isinstance(source.get("title"), str) and bool(source["title"].strip()),
            "authors": isinstance(source.get("authors"), list) and bool(source["authors"]),
            "year": isinstance(source.get("year"), int),
            "identifier": isinstance(source.get("identifier"), dict) and bool(source["identifier"]),
            "retrieved_on": isinstance(source.get("retrieved_on"), str)
            and bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", source["retrieved_on"])),
        }
        for field, valid in required.items():
            if not valid:
                problems.append(f"{source_id}: verified source missing valid {field}")
    if problems:
        raise ValueError("; ".join(problems))


def normalize_identifier(kind: str, value: object) -> str:
    if not isinstance(value, str):
        return ""
    normalized = value.strip()
    if kind == "doi":
        normalized = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", normalized, flags=re.I)
        normalized = re.sub(r"^doi:\s*", "", normalized, flags=re.I)
        match = re.search(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", normalized, flags=re.I)
        return (match.group(0) if match else normalized).lower()
    if kind == "pmid":
        return "".join(re.findall(r"\d+", normalized))
    if kind == "pmcid":
        token = normalized.upper()
        return token if token.startswith("PMC") else f"PMC{token}"
    if kind == "isbn":
        return re.sub(r"[^0-9Xx]", "", normalized).upper()
    if kind == "url":
        return normalized.rstrip("/")
    return normalized


def source_flags(source: dict) -> list[str]:
    notes = source.get("notes") or ""
    display = source.get("display") or ""
    flags = []
    if COMPOUND_MARKER in notes:
        flags.append("compound")
    if DUPLICATE_MARKER in notes:
        flags.append("duplicate_candidate")
    if INSUFFICIENT_MARKER in notes:
        flags.append("insufficient_bibliography")
    if CONSENSUS_MARKER in notes:
        flags.append("consensus_not_citation")
    if INTERNAL_REFERENCE_RE.search(display):
        flags.append("internal_reference")
    return flags


def triage_lane(source: dict, flags: Iterable[str]) -> str:
    flags = set(flags)
    identifier = source.get("identifier") or {}
    identifier_keys = set(identifier) if isinstance(identifier, dict) else set()
    if source.get("verification_status") == "verified":
        return "complete"
    if "internal_reference" in flags:
        return "internal_reference"
    if "compound" in flags:
        return "compound_split"
    if identifier_keys & STRONG_IDENTIFIER_KEYS:
        return "identifier_dereference"
    if "url" in identifier_keys:
        return "url_review"
    if source.get("authors") and source.get("year"):
        return "bibliographic_search"
    return "manual_reconstruction"


def identifier_collisions(sources: list[dict]) -> list[dict]:
    owners: dict[tuple[str, str], list[str]] = defaultdict(list)
    for source in sources:
        identifier = source.get("identifier") or {}
        if not isinstance(identifier, dict):
            continue
        for kind, raw_value in identifier.items():
            value = normalize_identifier(kind, raw_value)
            if value:
                owners[(kind, value)].append(source["id"])
    return [
        {"kind": kind, "value": value, "source_ids": sorted(source_ids)}
        for (kind, value), source_ids in sorted(owners.items())
        if len(source_ids) > 1
    ]


def build_audit(sources: list[dict]) -> dict:
    validate_verified_contract(sources)
    items = []
    lane_counts: Counter[str] = Counter()
    flag_counts: Counter[str] = Counter()
    identifier_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()

    for source in sorted(sources, key=lambda item: item["id"]):
        identifier = source.get("identifier") or {}
        identifier = identifier if isinstance(identifier, dict) else {}
        flags = source_flags(source)
        lane = triage_lane(source, flags)
        lane_counts[lane] += 1
        flag_counts.update(flags)
        identifier_counts.update(identifier.keys())
        status_counts[source.get("verification_status", "(missing)")] += 1
        items.append({
            "id": source["id"],
            "display": source.get("display", ""),
            "verification_status": source.get("verification_status", ""),
            "lane": lane,
            "flags": flags,
            "identifier": identifier,
            "authors": source.get("authors", []),
            "year": source.get("year"),
        })

    collisions = identifier_collisions(sources)
    return {
        "schema_version": SCHEMA_VERSION,
        "source_count": len(sources),
        "summary": {
            "verification_status": dict(sorted(status_counts.items())),
            "identifier_records": sum(
                1 for source in sources if isinstance(source.get("identifier"), dict)
                and bool(source["identifier"])
            ),
            "identifier_keys": dict(sorted(identifier_counts.items())),
            "lanes": dict(sorted(lane_counts.items())),
            "flags": dict(sorted(flag_counts.items())),
            "identifier_collision_groups": len(collisions),
        },
        "identifier_collisions": collisions,
        "items": items,
    }


def write_audit(audit: dict, path: Path = OUTPUT_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    audit = build_audit(load_sources())
    write_audit(audit)
    summary = audit["summary"]
    print(f"Wrote {OUTPUT_FILE.relative_to(ROOT)}")
    print(f"Sources: {audit['source_count']}")
    print(f"Status: {summary['verification_status']}")
    print(f"Identifier records: {summary['identifier_records']}")
    print(f"Identifier keys: {summary['identifier_keys']}")
    print(f"Lanes: {summary['lanes']}")
    print(f"Flags: {summary['flags']}")
    print(f"Identifier collision groups: {summary['identifier_collision_groups']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
