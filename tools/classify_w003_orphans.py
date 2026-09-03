"""One-shot: classify current W003 orphans into 3 buckets for HANDOFF C table.

Class 1: has `links` block but ALL sub-keys empty/None/[]
Class 2: has `cross_ref` prose (or `cross_ref` sub-key elsewhere) but empty `cross_ref_ids`
Class 3: no relationship fields at all (or has partial links with some prose, doesn't fit 1/2)

Reads the current W003 list from reports/validation_report.md and cross-references
each orphan against its YAML entry.
"""

from __future__ import annotations
import io
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import load_yaml, iter_entries  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "reports" / "validation_report.md"


def parse_w003(report_path: Path) -> list[tuple[str, str]]:
    text = report_path.read_text(encoding="utf-8")
    m = re.search(r"## W003.*?(?=\n## |\Z)", text, re.S)
    if not m:
        return []
    body = m.group(0)
    pat = re.compile(r"file=([^ ]+) id='([^']+)'")
    return [(rel.replace("\\", "/"), eid) for rel, eid in pat.findall(body)]


def find_entry(data, target_id: str):
    """Walk data recursively; return the first dict whose 'id' == target_id."""
    if isinstance(data, dict):
        if data.get("id") == target_id:
            return data
        for v in data.values():
            r = find_entry(v, target_id)
            if r is not None:
                return r
    elif isinstance(data, list):
        for item in data:
            r = find_entry(item, target_id)
            if r is not None:
                return r
    return None


def has_cross_ref_prose(entry: dict) -> bool:
    """cross_ref text present at entry / public / diagnostic layer with empty cross_ref_ids."""
    for layer_key in ("__self__", "public", "diagnostic"):
        sub = entry if layer_key == "__self__" else entry.get(layer_key)
        if not isinstance(sub, dict):
            continue
        prose = sub.get("cross_ref")
        ids = sub.get("cross_ref_ids")
        prose_nonempty = bool(prose) and (
            (isinstance(prose, str) and prose.strip())
            or (isinstance(prose, list) and any(str(x).strip() for x in prose))
        )
        ids_nonempty = bool(ids) and (
            isinstance(ids, (list, tuple)) and any(str(x).strip() for x in ids)
        )
        if prose_nonempty and not ids_nonempty:
            return True
    return False


def links_shape(entry: dict) -> str:
    """Return 'all_empty', 'partial_prose', 'none'."""
    links = entry.get("links")
    if not isinstance(links, dict):
        return "none"
    any_value = False
    for k, v in links.items():
        if v is None:
            continue
        if isinstance(v, (list, tuple)) and len(v) == 0:
            continue
        if isinstance(v, str) and not v.strip():
            continue
        if isinstance(v, dict) and not v:
            continue
        any_value = True
        break
    return "partial_prose" if any_value else "all_empty"


def classify(entry: dict) -> str:
    cross = has_cross_ref_prose(entry)
    ls = links_shape(entry)
    if ls == "all_empty":
        return "class1"
    if cross:
        return "class2"
    if ls == "none":
        # completely no links block AND no cross_ref prose → class3
        return "class3"
    # ls == "partial_prose" → has some link prose (e.g. injuries perception_link str)
    # but no cross_ref hitting class2 — treat as class3 (still orphan)
    return "class3_partial"


def main():
    orphans = parse_w003(REPORT)
    print(f"Total W003 from report: {len(orphans)}")

    file_cache: dict[str, object] = {}
    def load(rel: str):
        if rel not in file_cache:
            file_cache[rel] = load_yaml(ROOT / rel)
        return file_cache[rel]

    class_counts = Counter()
    class_by_file: dict[str, Counter] = defaultdict(Counter)
    missing_entries: list[tuple[str, str]] = []

    for rel, eid in orphans:
        data = load(rel)
        entry = find_entry(data, eid)
        if entry is None:
            missing_entries.append((rel, eid))
            class_counts["missing"] += 1
            class_by_file[rel]["missing"] += 1
            continue
        cls = classify(entry)
        class_counts[cls] += 1
        class_by_file[rel][cls] += 1

    print("\n=== Global counts ===")
    for cls, n in sorted(class_counts.items()):
        print(f"  {cls}: {n}")

    print("\n=== Per file (Class1 / Class2 / Class3 / Class3_partial) ===")
    for rel in sorted(class_by_file):
        c = class_by_file[rel]
        c1 = c.get("class1", 0)
        c2 = c.get("class2", 0)
        c3 = c.get("class3", 0)
        c3p = c.get("class3_partial", 0)
        miss = c.get("missing", 0)
        total = c1 + c2 + c3 + c3p + miss
        parts = [f"C1={c1}", f"C2={c2}", f"C3={c3}"]
        if c3p:
            parts.append(f"C3p={c3p}")
        if miss:
            parts.append(f"MISS={miss}")
        print(f"  {rel:60s} total={total:3d}  " + "  ".join(parts))

    if missing_entries:
        print("\n=== Entries not found in YAML (possibly cross-file id) ===")
        for rel, eid in missing_entries:
            print(f"  {rel}  {eid}")


if __name__ == "__main__":
    # Force UTF-8 stdout so cp950 console doesn't mangle Chinese
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    main()
