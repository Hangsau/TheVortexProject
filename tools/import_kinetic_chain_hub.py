#!/usr/bin/env python3
"""將固定的 Knowledge Hub 游泳動力鏈快照匯入 Vortex 公開 canonical bundle。"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_HUB = Path(r"C:\claudehome\projects\knowledge-hub")
DEFAULT_ATLAS = Path(r"C:\claudehome\projects\kinetic-chain-knowledge-atlas")
DEFAULT_OUTPUT = ROOT / "canonical" / "evidence" / "kinetic-chain-knowledge-hub.json"
PROJECT_ID = "kinetic-chain-knowledge-atlas"


class ImportError(RuntimeError):
    pass


def _canonical_hash(payload: dict) -> str:
    clone = json.loads(json.dumps(payload))
    clone["manifest"]["generated_at"] = ""
    clone["manifest"]["content_hash"] = ""
    return hashlib.sha256(
        json.dumps(clone, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _git(atlas: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(atlas), *args], capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode:
        raise ImportError(result.stderr.strip() or "git read failed")
    return result.stdout


def _git_records(atlas: Path, commit: str, directory: str) -> list[dict]:
    listing = _git(atlas, "ls-tree", "-r", "--name-only", commit, "--", directory)
    output = []
    for path in listing.splitlines():
        if path.endswith(".json"):
            output.append(json.loads(_git(atlas, "show", f"{commit}:{path}")))
    return output


ANALYSIS_FIELDS = (
    "id", "source_id", "title_zh", "research_questions", "study_design", "population",
    "stroke_ids", "phase_ids", "local_concept_ids", "methods_summary_zh",
    "interventions_or_exposures", "measurements", "outcomes", "terminology",
    "detailed_sections", "result_matrix", "findings", "limitations_zh", "applicability",
    "practical_implications_zh", "research_gaps_zh", "review_status", "status", "checked_at",
)
PUBLICATION_FIELDS = (
    "id", "title", "subtitle", "summary", "audience", "sections", "practice_tools",
    "review_status", "status", "publishable", "checked_at",
)


def _select(record: dict, fields: tuple[str, ...]) -> dict:
    return {key: record[key] for key in fields if key in record}


def _reject_unsafe(value) -> None:
    if isinstance(value, dict):
        for item in value.values():
            _reject_unsafe(item)
    elif isinstance(value, list):
        for item in value:
            _reject_unsafe(item)
    elif isinstance(value, str):
        lowered = value.lower()
        forbidden = ("<script", "javascript:", "c:\\", "c:/users/", "/users/", "/home/")
        if any(token in lowered for token in forbidden):
            raise ImportError("公開 bundle 含不安全標記或本機路徑")


def build_bundle(snapshot: dict, selection: dict, atlas: Path) -> dict:
    manifest = snapshot.get("manifest", {})
    if manifest.get("project_id") != PROJECT_ID:
        raise ImportError("Hub project_id 不符")
    if manifest.get("schema_version") != 1:
        raise ImportError("不支援的 Hub schema_version")
    if _canonical_hash(snapshot) != manifest.get("content_hash"):
        raise ImportError("Hub snapshot content_hash 不符")
    for key in ("project_id", "source_commit", "content_hash"):
        if selection.get(key) != manifest.get(key):
            raise ImportError(f"Vortex selection 的 {key} 與 snapshot 不符")

    commit = manifest["source_commit"]
    if _git(atlas, "rev-parse", commit).strip() != commit:
        raise ImportError("Atlas commit 無法解析")
    analyses = [_select(item, ANALYSIS_FIELDS) for item in _git_records(atlas, commit, "library/source-analyses")]
    publications = [_select(item, PUBLICATION_FIELDS) for item in _git_records(atlas, commit, "knowledge/publications")]
    overlay_records = _git_records(atlas, commit, "crosswalks")
    overlay = next((item for item in overlay_records if item.get("id") == "vortex-drill-publication-overlay"), None)
    if overlay is None:
        raise ImportError("缺少 Vortex drill publication overlay")

    claims = [item for item in snapshot.get("claims", []) if item.get("publishable")]
    evidence_count = sum(len(item.get("evidence", [])) for item in claims)
    findings_count = sum(len(item.get("findings", [])) for item in analyses)
    tools_count = sum(len(item.get("practice_tools", [])) for item in publications)
    expected = {
        "analyses": 62, "findings": 299, "claims": 28,
        "evidence_references": 43, "publications": 3, "practice_tools": 5,
    }
    actual = {
        "analyses": len(analyses), "findings": findings_count, "claims": len(claims),
        "evidence_references": evidence_count, "publications": len(publications),
        "practice_tools": tools_count,
    }
    if actual != expected:
        raise ImportError(f"資料數量未達選定版本契約：expected={expected}, actual={actual}")

    bundle = {
        "schema_version": 1,
        "domain": "swimming-kinetic-chain",
        "title_zh": "游泳動力鏈知識庫",
        "description_zh": "研究結果、證據邊界、跨研究整合與訓練決策工具。證據到哪裡，結論就說到哪裡。",
        "provenance": {
            "atlas_project": PROJECT_ID,
            "atlas_commit": commit,
            "hub_snapshot": selection.get("snapshot"),
            "hub_content_hash": manifest["content_hash"],
            "generated_at": manifest["generated_at"],
        },
        "counts": actual,
        "evidence_basis_legend": {
            "direct-result": "研究直接報告的結果",
            "author-interpretation": "研究作者的解釋或建議",
            "reviewer-synthesis": "本知識庫依全文所做的整合判讀",
            "mechanistic-model": "用來解釋現象的機制模型",
            "context-only": "背景或使用情境，不能單獨證明效果",
        },
        "sources": snapshot.get("sources", []),
        "analyses": sorted(analyses, key=lambda item: item["id"]),
        "claims": sorted(claims, key=lambda item: item["id"]),
        "publications": sorted(publications, key=lambda item: item["id"]),
        "drill_overlay": overlay,
    }
    _reject_unsafe(bundle)
    return bundle


def write_atomic(path: Path, bundle: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, suffix=".tmp") as handle:
        handle.write(text)
        temp = Path(handle.name)
    temp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hub", type=Path, default=DEFAULT_HUB)
    parser.add_argument("--atlas", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        selection_path = args.hub / "reports" / f"{PROJECT_ID}-vortex-public.json"
        selection = json.loads(selection_path.read_text(encoding="utf-8"))
        snapshot = json.loads((args.hub / "snapshots" / selection["snapshot"]).read_text(encoding="utf-8"))
        bundle = build_bundle(snapshot, selection, args.atlas)
        if not args.dry_run:
            write_atomic(args.output, bundle)
    except (OSError, json.JSONDecodeError, ImportError) as exc:
        print(f"FAIL: {exc}")
        return 1
    counts = bundle["counts"]
    print("PASS: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    if args.dry_run:
        print("dry-run: 未寫入 canonical bundle")
    else:
        print(f"wrote: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
