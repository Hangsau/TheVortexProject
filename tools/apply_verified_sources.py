#!/usr/bin/env python3
"""Apply only fully matched identifier verification results to _sources.yaml.

The update is block-surgical: registry comments and untouched source blocks
remain byte-identical. The default is a dry run; pass ``--apply`` to write.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml

import audit_sources
import verify_source_identifiers as verifier

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "canonical" / "_sources.yaml"
REPORT_FILE = ROOT / "reports" / "source_identifier_verification.json"

MANAGED_FIELDS = {
    "title",
    "type",
    "verification_status",
    "authors",
    "year",
    "container",
    "identifier",
    "retrieved_on",
}
SOURCE_START_RE = re.compile(r"^  - id: (\S+)\s*$", re.MULTILINE)
TOP_FIELD_RE = re.compile(r"^    ([a-z_]+):", re.MULTILINE)


def yaml_scalar(value: object) -> str:
    return json.dumps(value, ensure_ascii=False)


def desired_fields(result: dict) -> dict:
    current = result.get("current") or {}
    resolved = result.get("resolved") or {}
    identifiers = dict(current.get("identifier") or {})
    identifiers.update(resolved.get("identifier") or {})
    fields = {
        "title": resolved.get("title") or "",
        "type": (
            current.get("type")
            if current.get("type") and current.get("type") != "other"
            else resolved.get("type") or "other"
        ),
        "verification_status": "verified",
        "authors": resolved.get("authors") or [],
        "year": resolved.get("year"),
        "container": resolved.get("container") or "",
        "identifier": identifiers,
        "retrieved_on": result.get("retrieved_on"),
    }
    missing = [
        key for key in ("title", "authors", "year", "identifier", "retrieved_on")
        if not fields.get(key)
    ]
    if missing:
        raise ValueError(f"{result.get('id')}: verified fields missing {missing}")
    return fields


def render_managed_fields(fields: dict) -> str:
    lines = [
        f"    title: {yaml_scalar(fields['title'])}",
        f"    type: {fields['type']}",
        "    verification_status: verified",
        f"    authors: {yaml_scalar(fields['authors'])}",
        f"    year: {int(fields['year'])}",
    ]
    if fields.get("container"):
        lines.append(f"    container: {yaml_scalar(fields['container'])}")
    lines.append("    identifier:")
    for kind, value in fields["identifier"].items():
        lines.append(f"      {kind}: {yaml_scalar(value)}")
    lines.append(f"    retrieved_on: {yaml_scalar(fields['retrieved_on'])}")
    return "\n".join(lines) + "\n"


def strip_managed_fields(block: str) -> tuple[str, int]:
    matches = list(TOP_FIELD_RE.finditer(block))
    spans = []
    for index, match in enumerate(matches):
        if match.group(1) not in MANAGED_FIELDS:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(block)
        spans.append((match.start(), end))
    for start, end in reversed(spans):
        block = block[:start] + block[end:]
    return block, len(spans)


def update_block(block: str, fields: dict) -> str:
    stripped, _removed = strip_managed_fields(block)
    display_match = re.search(r"^    display:.*(?:\n|$)", stripped, flags=re.MULTILINE)
    if not display_match:
        raise ValueError("source block has no display field")
    insertion = render_managed_fields(fields)
    return stripped[:display_match.end()] + insertion + stripped[display_match.end():]


def block_ranges(text: str) -> dict[str, tuple[int, int]]:
    starts = list(SOURCE_START_RE.finditer(text))
    return {
        match.group(1): (match.start(), starts[index + 1].start() if index + 1 < len(starts) else len(text))
        for index, match in enumerate(starts)
    }


def apply_results(text: str, report: dict) -> tuple[str, list[str]]:
    selected = [result for result in report.get("results") or [] if result.get("decision") == "matched"]
    ranges = block_ranges(text)
    replacements = []
    selected_ids = []
    for result in selected:
        source_id = result["id"]
        if source_id not in ranges:
            raise ValueError(f"source block not found: {source_id}")
        start, end = ranges[source_id]
        block = text[start:end]
        live_source = yaml.safe_load("sources:\n" + block)["sources"][0]
        live_current = dict(result.get("current") or {})
        live_type = live_source.get("type", "other")
        if live_type != "other" or not live_current.get("type"):
            live_current["type"] = live_type
        live_current["identifier"] = live_source.get("identifier", live_current.get("identifier", {}))
        enriched = {
            **result,
            "current": live_current,
            "retrieved_on": report.get("retrieved_on"),
        }
        fields = desired_fields(enriched)
        replacements.append((start, end, update_block(block, fields)))
        selected_ids.append(source_id)
    for start, end, replacement in sorted(replacements, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text, sorted(selected_ids)


def assert_semantic_safety(before: str, after: str, selected_ids: list[str]) -> None:
    before_data = yaml.safe_load(before)
    after_data = yaml.safe_load(after)
    before_sources = {source["id"]: source for source in before_data["sources"]}
    after_sources = {source["id"]: source for source in after_data["sources"]}
    if set(before_sources) != set(after_sources):
        raise ValueError("source IDs changed during apply")
    for source_id in before_sources:
        if before_sources[source_id].get("display") != after_sources[source_id].get("display"):
            raise ValueError(f"display changed: {source_id}")
        if source_id not in selected_ids and before_sources[source_id] != after_sources[source_id]:
            raise ValueError(f"unselected source changed: {source_id}")
    for source_id in selected_ids:
        if after_sources[source_id].get("verification_status") != "verified":
            raise ValueError(f"selected source not verified: {source_id}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write canonical/_sources.yaml")
    args = parser.parse_args()

    before = SOURCES_FILE.read_text(encoding="utf-8")
    report = json.loads(REPORT_FILE.read_text(encoding="utf-8"))
    after, selected_ids = apply_results(before, report)
    assert_semantic_safety(before, after, selected_ids)
    action = "Applied" if args.apply else "Dry run"
    if args.apply:
        SOURCES_FILE.write_text(after, encoding="utf-8")
    print(f"{action}: {len(selected_ids)} fully matched sources")
    print(f"Unchanged source IDs: {len(audit_sources.load_sources()) - len(selected_ids)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
