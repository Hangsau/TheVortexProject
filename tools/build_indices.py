#!/usr/bin/env python3
"""Build deterministic machine-readable indices for Vortex canonical data.

Outputs four JSON views under ``indices/``:

* content_index.json: one searchable record per stable content ID
* tag_reverse_index.json: controlled vocabulary value -> content IDs
* source_reverse_index.json: registered source -> exact usage locations
* gap_report.json: high-certainty claims without sources, unused tags, and
  entries without links

The scanner follows the same scope and relationship semantics as
``tools/validate.py``. Generated files are views; canonical YAML remains the
only source of truth.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Iterator

import yaml

import validate

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "indices"
SCHEMA_VERSION = 1

# Canonical field -> possible field names used by existing records.
TAG_FIELD_ALIASES = {
    "category": ("category",),
    "stroke": ("stroke", "strokes"),
    "joint_region": ("joint_region",),
    "certainty": ("certainty", "cert"),
    "status": ("status",),
    "development_stage": ("stage", "applies_from"),
    "pillar": ("pillar",),
    "l_level": ("level", "l_target"),
    "publication_status": ("publication_status",),
    "claim_status": ("claim_status",),
    "action_status": ("action_status",),
    "evidence_profile": ("evidence_profile",),
    "mobility_decision": ("mobility_decision",),
    # 這兩個 movement 受控欄位的 taxonomy 註記都寫「使用數以
    # indices/tag_reverse_index.json 為準」，漏收在這裡會讓那句話變成假的：
    # 欄位有值，反向索引卻永遠是空 list。phase_model 在 Step 16.5 登錄時漏收。
    "phase_model": ("phase_model",),
    "action_reference_frame": ("action_reference_frame",),
}

TITLE_FIELDS = (
    "title",
    "title_zh",
    "name_zh",
    "zh",
    "tagline",
    "summary",
    "indicator",
    "premise_zh",
    "plain_zh",
    "text_zh",
    "en",
)


def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def formal_source_files(root: Path) -> list[Path]:
    """Return promoted canonical files plus Drill content files.

    Drafts and underscore-prefixed metadata are deliberately excluded from
    the content index, matching validate.py's promoted-content scope.
    """
    canonical = [
        path
        for path in sorted((root / "canonical").rglob("*.yaml"))
        if not validate.is_excluded(path)
    ]
    drills = sorted((root / "Drills").glob("drills_*.yaml"))
    return canonical + drills


def iter_entries_with_path(
    data: object, path: str = ""
) -> Iterator[tuple[str, dict]]:
    """Yield every ID-bearing mapping and its stable YAML tree path."""
    if isinstance(data, dict):
        if isinstance(data.get("id"), str):
            yield path or "(root)", data
        for key, value in data.items():
            child = f"{path}.{key}" if path else str(key)
            yield from iter_entries_with_path(value, child)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            yield from iter_entries_with_path(item, f"{path}[{index}]")


def iter_owned_blocks(
    entry: dict, path: str = "", root_id: str | None = None
) -> Iterator[tuple[str, dict]]:
    """Walk blocks owned by one entry without absorbing nested entries.

    Psychology themes contain concept entries, for example. A theme must not
    inherit its concepts' sources or tags merely because they are nested in
    YAML, so recursion stops at a different stable ID.
    """
    if root_id is None:
        root_id = entry.get("id")
    if isinstance(entry.get("id"), str) and entry["id"] != root_id:
        return
    yield path or "(entry)", entry
    for key, value in entry.items():
        child = f"{path}.{key}" if path else str(key)
        if isinstance(value, dict):
            yield from iter_owned_blocks(value, child, root_id)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    yield from iter_owned_blocks(item, f"{child}[{index}]", root_id)


def first_text(mapping: dict) -> str:
    """Find a compact human label without copying full content into indices."""
    candidates: list[dict] = [mapping]
    public = mapping.get("public")
    if isinstance(public, dict):
        candidates.append(public)
        mechanism = public.get("mechanism")
        phenomenon = public.get("phenomenon")
        if isinstance(mechanism, dict):
            candidates.append(mechanism)
        if isinstance(phenomenon, dict):
            candidates.append(phenomenon)
    for candidate in candidates:
        for field in TITLE_FIELDS:
            value = candidate.get(field)
            if isinstance(value, str) and value.strip():
                return " ".join(value.split())[:160]
    return ""


def scalar_values(value: object) -> Iterator[str]:
    if isinstance(value, str) and value:
        yield value
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, str) and item:
                yield item


def owned_tags(entry: dict, taxonomy: dict[str, set[str]]) -> dict[str, list[str]]:
    tags: dict[str, set[str]] = defaultdict(set)
    for _path, block in iter_owned_blocks(entry):
        for canonical_field, aliases in TAG_FIELD_ALIASES.items():
            allowed = taxonomy.get(canonical_field, set())
            for alias in aliases:
                for value in scalar_values(block.get(alias)):
                    if value in allowed:
                        tags[canonical_field].add(value)
    return {field: sorted(values) for field, values in sorted(tags.items())}


def owned_source_usages(entry: dict) -> Iterator[tuple[str, str]]:
    for path, block in iter_owned_blocks(entry):
        source_ids = block.get("source_ids")
        if isinstance(source_ids, list):
            for source_id in source_ids:
                if isinstance(source_id, str) and source_id:
                    yield source_id, path


def owned_relations(entry: dict, all_ids: set[str]) -> list[str]:
    targets: set[str] = set()
    for _path, block in iter_owned_blocks(entry):
        for key, value in block.items():
            if key == "source_ids":
                continue
            if key in {"cross_ref_ids", "evidence_from"} or key.endswith("_link_ids"):
                targets.update(v for v in scalar_values(value) if v in all_ids)
        links = block.get("links")
        if isinstance(links, dict):
            for key in validate.LINKS_ID_REF_KEYS | validate.LINKS_IDS_KEYS:
                targets.update(v for v in scalar_values(links.get(key)) if v in all_ids)
    return sorted(targets)


def source_registry(root: Path) -> list[dict]:
    data = load_yaml(root / "canonical" / "_sources.yaml")
    if not isinstance(data, dict):
        return []
    return [item for item in (data.get("sources") or []) if isinstance(item, dict)]


def taxonomy_values(root: Path) -> dict[str, set[str]]:
    data = load_yaml(root / "canonical" / "_taxonomy.yaml")
    fields = data.get("fields", {}) if isinstance(data, dict) else {}
    result: dict[str, set[str]] = {}
    for field, spec in fields.items():
        if not isinstance(spec, dict):
            continue
        result[field] = {
            item["key"]
            for item in (spec.get("values") or [])
            if isinstance(item, dict) and isinstance(item.get("key"), str)
        }
    return result


def collect_records(root: Path) -> tuple[list[dict], dict[str, dict]]:
    taxonomy = taxonomy_values(root)
    raw_records: list[tuple[str, str, dict]] = []
    for file in formal_source_files(root):
        rel = file.relative_to(root).as_posix()
        data = load_yaml(file)
        for yaml_path, entry in iter_entries_with_path(data):
            raw_records.append((rel, yaml_path, entry))

    all_ids = {entry["id"] for _rel, _path, entry in raw_records}
    records: list[dict] = []
    entry_by_id: dict[str, dict] = {}
    for rel, yaml_path, entry in raw_records:
        entry_id = entry["id"]
        if entry_id in entry_by_id:
            raise ValueError(f"duplicate promoted content id: {entry_id}")
        source_ids = sorted({sid for sid, _path in owned_source_usages(entry)})
        record = {
            "id": entry_id,
            "domain": "drills" if rel.startswith("Drills/") else rel.split("/")[1],
            "file": rel,
            "path": yaml_path,
            "title": first_text(entry),
            "tags": owned_tags(entry, taxonomy),
            "source_ids": source_ids,
            "outgoing_ids": owned_relations(entry, all_ids),
        }
        records.append(record)
        entry_by_id[entry_id] = entry
    records.sort(key=lambda item: item["id"])
    return records, entry_by_id


def build_content_index(records: list[dict]) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "record_count": len(records),
        "records": records,
    }


# _taxonomy.yaml 裡不是「條目標籤」的受控欄位。它們登錄在同一份 taxonomy
# 是為了保有單一詞彙真相源，但值出現在別的檔（source metadata），不會被任何
# 條目 tag 引用——列進 tag 反向索引會讓 gap_report 永遠多報幾筆假死標籤。
NON_ENTRY_TAXONOMY_FIELDS = frozenset({"source_verification_status"})


def build_tag_reverse_index(records: list[dict], taxonomy: dict[str, set[str]]) -> dict:
    reverse: dict[str, dict[str, list[str]]] = {
        field: {value: [] for value in sorted(values)}
        for field, values in sorted(taxonomy.items())
        if field not in NON_ENTRY_TAXONOMY_FIELDS
    }
    for record in records:
        for field, values in record["tags"].items():
            for value in values:
                reverse.setdefault(field, {}).setdefault(value, []).append(record["id"])
    return {
        "schema_version": SCHEMA_VERSION,
        "fields": reverse,
    }


def build_source_reverse_index(root: Path, records: list[dict], entry_by_id: dict[str, dict]) -> dict:
    record_meta = {record["id"]: record for record in records}
    usage: dict[str, list[dict]] = defaultdict(list)
    for entry_id, entry in entry_by_id.items():
        meta = record_meta[entry_id]
        for source_id, path in owned_source_usages(entry):
            usage[source_id].append({
                "id": entry_id,
                "file": meta["file"],
                "path": f'{meta["path"]}.{path}' if path != "(entry)" else meta["path"],
            })

    sources = []
    for source in sorted(source_registry(root), key=lambda item: item.get("id", "")):
        source_id = source.get("id", "")
        sources.append({
            "id": source_id,
            "display": source.get("display", ""),
            "verification_status": source.get("verification_status", ""),
            "identifier": source.get("identifier", {}),
            "usage_count": len(usage.get(source_id, [])),
            "usages": sorted(
                usage.get(source_id, []),
                key=lambda item: (item["id"], item["file"], item["path"]),
            ),
        })
    return {
        "schema_version": SCHEMA_VERSION,
        "source_count": len(sources),
        "sources": sources,
    }


def find_high_certainty_without_source(rel: str, data: object) -> list[dict]:
    """Return W009-equivalent gaps from one already-loaded document."""
    gaps: list[dict] = []
    for path, entry_id, block, inherited in validate.iter_blocks_with_source_inheritance(data):
        if block.get("certainty") not in validate.CERTAINTY_NEEDS_SOURCE:
            continue
        if validate.has_source_info(block) or inherited or validate.has_evidence_from(block):
            continue
        gaps.append({
            "id": entry_id,
            "file": rel,
            "path": path,
            "certainty": block["certainty"],
        })
    return gaps


def high_certainty_without_source(root: Path) -> list[dict]:
    gaps: list[dict] = []
    for file in formal_source_files(root):
        rel = file.relative_to(root).as_posix()
        gaps.extend(find_high_certainty_without_source(rel, load_yaml(file)))
    return sorted(gaps, key=lambda item: (item["file"], item["path"], item["id"]))


def unlinked_records(records: list[dict], entry_by_id: dict[str, dict]) -> list[dict]:
    """Mirror validate.py W003.

    出邊入邊都走 `validate.collect_outbound_ids()`。這裡曾經自己重寫入邊
    （只認 `links.*`，漏掉 movement 關聯欄位與 `cross_ref_ids`），孤兒因此
    虛報成 557 而非 403——**而 docstring 當時就寫著 Mirror**。不要再在這裡
    重寫任何一個方向。
    """
    canonical_records = [r for r in records if r["domain"] != "drills"]
    all_ids = {record["id"] for record in records}
    inbound: dict[str, int] = defaultdict(int)
    for record in canonical_records:
        for target in validate.collect_outbound_ids(entry_by_id[record["id"]]):
            if target in all_ids:
                inbound[target] += 1

    gaps = []
    for record in canonical_records:
        entry = entry_by_id[record["id"]]
        if inbound.get(record["id"], 0) == 0 and not validate.collect_outbound_ids(entry):
            gaps.append({
                "id": record["id"],
                "file": record["file"],
                "path": record["path"],
            })
    return sorted(gaps, key=lambda item: item["id"])


def build_gap_report(
    root: Path,
    records: list[dict],
    entry_by_id: dict[str, dict],
    tag_index: dict,
) -> dict:
    unused_tags = []
    for field, values in tag_index["fields"].items():
        for value, ids in values.items():
            if not ids:
                unused_tags.append({"field": field, "value": value})

    high_risk = high_certainty_without_source(root)
    unlinked = unlinked_records(records, entry_by_id)
    return {
        "schema_version": SCHEMA_VERSION,
        "summary": {
            "high_certainty_without_source": len(high_risk),
            "unused_taxonomy_values": len(unused_tags),
            "unlinked_records": len(unlinked),
        },
        "high_certainty_without_source": high_risk,
        "unused_taxonomy_values": unused_tags,
        "unlinked_records": unlinked,
    }


def build_views(root: Path = ROOT) -> dict[str, dict]:
    records, entry_by_id = collect_records(root)
    taxonomy = taxonomy_values(root)
    content = build_content_index(records)
    tags = build_tag_reverse_index(records, taxonomy)
    sources = build_source_reverse_index(root, records, entry_by_id)
    gaps = build_gap_report(root, records, entry_by_id, tags)
    return {
        "content_index.json": content,
        "tag_reverse_index.json": tags,
        "source_reverse_index.json": sources,
        "gap_report.json": gaps,
    }


def write_views(views: dict[str, dict], output_dir: Path = OUT_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in views.items():
        text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
        (output_dir / name).write_text(text, encoding="utf-8")


def main() -> int:
    views = build_views(ROOT)
    write_views(views, OUT_DIR)
    gaps = views["gap_report.json"]["summary"]
    print(f"Wrote {len(views)} views to {OUT_DIR.relative_to(ROOT)}/")
    print(f"Content records: {views['content_index.json']['record_count']}")
    print(f"Registered sources: {views['source_reverse_index.json']['source_count']}")
    print(
        "Gaps: "
        f"high-certainty-without-source={gaps['high_certainty_without_source']}, "
        f"unused-taxonomy-values={gaps['unused_taxonomy_values']}, "
        f"unlinked-records={gaps['unlinked_records']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
