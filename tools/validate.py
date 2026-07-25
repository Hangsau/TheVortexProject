#!/usr/bin/env python3
"""
validate.py - Vortex canonical 資料契約驗證器

用途：
  掃描 canonical/**/*.yaml（排除 drafts/ 與 _meta 前綴）與 Drills/*.yaml，
  執行引用完整性、tag 合法性、來源存在性與孤兒條目檢查。

跑法：
  python tools/validate.py

輸出：
  - stdout 摘要（純 ASCII 符號）
  - reports/validation_report.md（每代碼一個區塊）

exit code：
  1 = 有任何 ERROR
  0 = 只有 WARN 或全通過

檢查代碼：
  E001  在已知條目陣列鍵（points/errors/levels/cells/standards/
        indicators/injuries/themes）中發現缺 id 的元素
  E002  id 全域重複（排除 drafts/ 目錄）
  E003  links.* 指向不存在的 ID（canonical 全集 + Drills）
  E004  category/stroke/certainty/status 出現不在 _taxonomy.yaml 的值
  E005  source_ids 指向不存在的 _sources.yaml ID
  W001  cross_ref 是自由文字、無法解析成穩定 ID（S4 待辦）
  W002  certainty 為 green 或 yellow 但沒有 source_ids（S3 待辦）
  W003  孤兒條目：沒有任何 links 指入、自己也沒指出

備註：
  canonical/health/drafts/ 是 build source，canonical/health/injuries.yaml
  是 build artifact（正式 canonical）。本驗證器只掃 injuries.yaml，
  排除 drafts/ 以避免 ID 重複誤報。
"""
from __future__ import annotations

import sys
import traceback
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIR = ROOT / "canonical"
DRILLS_DIR = ROOT / "Drills"
TAXONOMY_FILE = CANONICAL_DIR / "_taxonomy.yaml"
SOURCES_FILE = CANONICAL_DIR / "_sources.yaml"
REPORTS_DIR = ROOT / "reports"

# 本專案慣例：詞彙定義表用 key（不需要 id），內容條目用 id。
# VOCAB_LIST_KEYS 列出「詞彙定義表陣列鍵」——這些鍵下的元素是詞彙定義，
# 用 key 欄位識別，不應被 E001 要求加 id。
VOCAB_LIST_KEYS = {
    "levels",    # technica/l-indicators — L 級感知層級定義表（key: pre/L2/L3/L4/L5/L6）
    "stages",    # development/matrix    — LTD 發展階段定義表（key: fun/l2t/t2t/t2c/t2w）
    "pillars",   # development/matrix    — 發展支柱定義表（key: physical/technical/mental/life）
    "strokes",   # technica/l-indicators — 泳式定義表（key: common/free/back/fly/breast）
}

# 已知條目陣列鍵（用於 E001 偵測）
# 這些鍵下的元素是內容條目，必須有 id。
# VOCAB_LIST_KEYS 的鍵已明確排除在外，不會出現在此集合中。
KNOWN_ENTRY_LIST_KEYS = {
    "points",       # technical-analysis, teaching-errors (errors 鍵)
    "errors",       # teaching-errors
    "cells",        # development/matrix（內容格，不是詞彙定義）
    "standards",    # development/technical-standards
    "indicators",   # technica/l-indicators（技術指標條目，有 id）
    "injuries",     # health/injuries
    "themes",       # psychology
    "drills",       # Drills/*.yaml
    "diagnostic_protocols",  # perception/*.yaml
}

# 本專案慣例：links 子鍵分三類
# ID 參照類：值應對應全域 ID 集合，違規報 E003
LINKS_ID_REF_KEYS = {
    "standards",         # → development/technical-standards 的 std.* ID
    "drills",            # → Drills/*.yaml 的 Fr*/Bk*/Br*/Fl*/Sc* ID
    "l_indicators",      # → technica/l-indicators 的 {stroke}.{level}.{aspect} ID
    "technical_analysis", # → instructional/technical-analysis 的 {stroke}.tech.N ID
    "related",           # → 同 domain 其他條目 ID（periodization 內部互連）
}

# 詞彙參照類：值應對應 _taxonomy.yaml 的指定詞彙欄位，違規報 E004
# 格式：{link_key: taxonomy_field}
LINKS_VOCAB_REF_KEYS = {
    "development_stages": "development_stage",  # 值應為 development_stage 詞彙
}

# 自由文字類：mechanism_link、technical_link、perception_link 是 narrative 說明，
# 混有自由文字與部分 ID 參照，統一不做 E003/E004 驗證。
# （injuries.yaml 的設計慣例；後續 S5 可再拆成可驗證 ID 參照層）


# ── 工具函式 ─────────────────────────────────────────────────────────────────

def load_yaml(path: Path) -> object:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def iter_entries(data: object):
    """遞迴走訪 YAML 樹，yield 所有含 'id' 鍵的 dict。"""
    if isinstance(data, dict):
        if "id" in data:
            yield data
        # 不在 yield 後停止，子樹可能還有更多條目
        for v in data.values():
            yield from iter_entries(v)
    elif isinstance(data, list):
        for item in data:
            yield from iter_entries(item)


def collect_all_ids_from_files(files) -> dict[str, list[str]]:
    """從多個 YAML 檔收集所有 id，回傳 {id: [路徑, ...]}"""
    id_to_files: dict[str, list[str]] = defaultdict(list)
    for path in files:
        try:
            data = load_yaml(path)
            for entry in iter_entries(data):
                eid = entry["id"]
                if isinstance(eid, str):
                    id_to_files[eid].append(str(path.relative_to(ROOT)))
        except Exception as e:
            sys.stderr.write(f"[WARN] load error {path}: {e}\n")
    return id_to_files


# ── 是否排除 drafts 目錄 ──────────────────────────────────────────────────────

def is_excluded(path: Path) -> bool:
    """drafts/ 目錄及 _ 前綴 meta 檔排除驗證（但保留在 ID 集合中）"""
    if path.name.startswith("_"):
        return True
    parts = path.parts
    if "drafts" in parts:
        return True
    return False


# ── Taxonomy 載入 ─────────────────────────────────────────────────────────────

def load_taxonomy() -> dict[str, set[str]]:
    """回傳 {field_name: set_of_allowed_keys}。"""
    data = load_yaml(TAXONOMY_FILE)
    result: dict[str, set[str]] = {}
    for field, field_data in data.get("fields", {}).items():
        keys = set()
        for item in field_data.get("values", []):
            keys.add(item["key"])
        result[field] = keys
    return result


# ── Sources 載入 ──────────────────────────────────────────────────────────────

def load_source_ids() -> set[str]:
    """回傳 _sources.yaml 中所有已登錄的 id。"""
    data = load_yaml(SOURCES_FILE)
    return {
        s["id"] for s in (data.get("sources") or [])
        if isinstance(s, dict) and "id" in s
    }


# ── 確定性：需要來源的等級 ─────────────────────────────────────────────────────

# green=\U0001F7E2, yellow=\U0001F7E1
CERTAINTY_NEEDS_SOURCE = {"\U0001F7E2", "\U0001F7E1"}


# ── 孤兒偵測輔助 ──────────────────────────────────────────────────────────────

def collect_outbound_ids(entry: dict) -> set[str]:
    """收集條目 links.* 裡所有指出的 ID（string 型）。"""
    out: set[str] = set()
    links = entry.get("links")
    if isinstance(links, dict):
        for v in links.values():
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, str):
                        out.add(item)
            elif isinstance(v, str) and v:
                out.add(v)
    return out


# ── E001 輔助：在已知條目陣列鍵中偵測缺 id ────────────────────────────────────

def find_missing_id_in_lists(data: object, rel: str, result: list):
    """遞迴走訪，在 KNOWN_ENTRY_LIST_KEYS 的子列表中找缺 id 的元素。
    VOCAB_LIST_KEYS 的鍵（詞彙定義表，用 key 識別）直接跳過，不要求 id。
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k in VOCAB_LIST_KEYS:
                # 詞彙定義表：用 key 識別，不需要 id，跳過
                pass
            elif k in KNOWN_ENTRY_LIST_KEYS and isinstance(v, list):
                for i, item in enumerate(v):
                    if isinstance(item, dict) and "id" not in item:
                        result.append(
                            f"  file={rel} {k}[{i}] 缺 id，已有鍵: "
                            f"{list(item.keys())[:5]}"
                        )
            else:
                find_missing_id_in_lists(v, rel, result)
    elif isinstance(data, list):
        for item in data:
            find_missing_id_in_lists(item, rel, result)


# ── 主驗證邏輯 ────────────────────────────────────────────────────────────────

def run_validation():
    # ── 載入 taxonomy 與 sources ──
    try:
        taxonomy = load_taxonomy()
    except Exception as e:
        print(f"[ERROR] Cannot load _taxonomy.yaml: {e}")
        sys.exit(1)

    try:
        allowed_source_ids = load_source_ids()
    except Exception as e:
        print(f"[ERROR] Cannot load _sources.yaml: {e}")
        sys.exit(1)

    # ── 掃描所有 canonical 檔 ──
    all_canonical_files = sorted(CANONICAL_DIR.rglob("*.yaml"))

    # 驗證用：排除 _ 前綴 meta 檔與 drafts/
    validate_files = [p for p in all_canonical_files if not is_excluded(p)]

    # ID 集合用：canonical 全部檔案（含 drafts）都算 ID 來源
    # 但排除 _ 前綴 meta 檔
    id_source_files = [p for p in all_canonical_files if not p.name.startswith("_")]

    # ── 掃描 Drills 取 ID ──
    drills_files = sorted(DRILLS_DIR.glob("*.yaml"))
    drills_id_map = collect_all_ids_from_files(drills_files)
    drills_id_set = set(drills_id_map.keys())

    # ── 建立 canonical ID 集合（全域，用於 E003 參照）──
    canonical_id_map = collect_all_ids_from_files(id_source_files)
    canonical_id_set = set(canonical_id_map.keys())
    all_id_set = canonical_id_set | drills_id_set

    # ── 收集驗證範圍內的條目 ──
    # {id: [(rel_path, entry)]}
    id_registry: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    all_entries: list[tuple[str, dict]] = []

    for path in validate_files:
        try:
            data = load_yaml(path)
            rel = str(path.relative_to(ROOT))
            for entry in iter_entries(data):
                eid = entry.get("id")
                if eid is not None and isinstance(eid, str):
                    id_registry[eid].append((rel, entry))
                    all_entries.append((rel, entry))
        except Exception as e:
            sys.stderr.write(f"[WARN] load error {path}: {e}\n")

    # ── 錯誤/警告收集器 ──
    errors: dict[str, list[str]] = {
        "E001": [], "E002": [], "E003": [], "E004": [], "E005": []
    }
    warnings: dict[str, list[str]] = {
        "W001": [], "W002": [], "W003": []
    }

    # ── E001: 在已知條目陣列鍵中發現缺 id 的元素 ──
    for path in validate_files:
        try:
            data = load_yaml(path)
            rel = str(path.relative_to(ROOT))
            find_missing_id_in_lists(data, rel, errors["E001"])
        except Exception:
            pass

    # ── E002: id 全域重複（僅在驗證範圍內）──
    for eid, occurrences in id_registry.items():
        if len(occurrences) > 1:
            files_list = ", ".join(f for f, _ in occurrences)
            errors["E002"].append(f"  id={eid!r} 出現於: {files_list}")

    # ── 用於 W003 孤兒偵測 ──
    inbound_ids: dict[str, int] = defaultdict(int)

    # ── 逐條目檢查 ──
    for rel, entry in all_entries:
        eid = entry.get("id", "(no id)")

        # ── E003: links.* ID 參照類斷鏈 ──
        # ── E004 (詞彙參照類): links.* 詞彙值不在 taxonomy ──
        # 自由文字類（mechanism_link / technical_link / perception_link）跳過。
        links = entry.get("links")
        if isinstance(links, dict):
            for link_type, targets in links.items():
                if link_type in LINKS_VOCAB_REF_KEYS:
                    # 詞彙參照類：比對 taxonomy 指定欄位
                    tax_field = LINKS_VOCAB_REF_KEYS[link_type]
                    allowed_vocab = taxonomy.get(tax_field, set())
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str) and target:
                                if target not in allowed_vocab:
                                    errors["E004"].append(
                                        f"  file={rel} id={eid!r} "
                                        f"links.{link_type}={target!r} "
                                        f"（不在 taxonomy.{tax_field}）"
                                    )
                    elif isinstance(targets, str) and targets:
                        if targets not in allowed_vocab:
                            errors["E004"].append(
                                f"  file={rel} id={eid!r} "
                                f"links.{link_type}={targets!r} "
                                f"（不在 taxonomy.{tax_field}）"
                            )
                elif link_type in LINKS_ID_REF_KEYS:
                    # ID 參照類：比對全域 ID 集合
                    if isinstance(targets, list):
                        for target in targets:
                            if isinstance(target, str):
                                if target not in all_id_set:
                                    errors["E003"].append(
                                        f"  file={rel} id={eid!r} "
                                        f"links.{link_type}={target!r}"
                                    )
                                else:
                                    inbound_ids[target] += 1
                    elif isinstance(targets, str) and targets:
                        if targets not in all_id_set:
                            errors["E003"].append(
                                f"  file={rel} id={eid!r} "
                                f"links.{link_type}={targets!r}"
                            )
                        else:
                            inbound_ids[targets] += 1
                # else: 自由文字類（mechanism_link 等），跳過不驗證

        # ── E004: taxonomy 不存在的值 ──
        for field in ("category", "stroke", "certainty", "status"):
            val = entry.get(field)
            if val is not None and isinstance(val, str):
                allowed = taxonomy.get(field, set())
                if val not in allowed:
                    errors["E004"].append(
                        f"  file={rel} id={eid!r} {field}={val!r}"
                    )

        # ── E005: source_ids 指向不存在的 ID ──
        source_ids = entry.get("source_ids")
        if source_ids and isinstance(source_ids, list):
            for sid in source_ids:
                if isinstance(sid, str) and sid not in allowed_source_ids:
                    errors["E005"].append(
                        f"  file={rel} id={eid!r} source_ids "
                        f"包含不存在的 {sid!r}"
                    )

        # ── W001: cross_ref 自由文字（在 entry 頂層或 public 層）──
        # 注意：不做任何 ASCII encode 轉換，直接保留原始 Unicode 字串，
        # 才能在報告中正確顯示中文。顯示截斷改為 120 字元。
        def _check_cross_ref(d: dict, location: str):
            cr = d.get("cross_ref")
            if cr is not None and isinstance(cr, str) and cr.strip():
                warnings["W001"].append(
                    f"  file={rel} id={eid!r} "
                    f"{location}.cross_ref (120 chars): {cr[:120]!r}"
                )

        _check_cross_ref(entry, "entry")
        pub = entry.get("public", {})
        if isinstance(pub, dict):
            _check_cross_ref(pub, "public")

        # ── W002: certainty green/yellow 無 source_ids ──
        # 直接在 entry 層
        cert = entry.get("certainty")
        if cert in CERTAINTY_NEEDS_SOURCE:
            if not entry.get("source_ids"):
                cert_label = "green" if cert == "\U0001F7E2" else "yellow"
                warnings["W002"].append(
                    f"  file={rel} id={eid!r} "
                    f"certainty={cert_label} 無 source_ids"
                )
        # 在 public.mechanism.certainty 層
        pub = entry.get("public", {})
        if isinstance(pub, dict):
            mech = pub.get("mechanism", {})
            if isinstance(mech, dict):
                cert_pub = mech.get("certainty")
                if cert_pub in CERTAINTY_NEEDS_SOURCE:
                    if not entry.get("source_ids"):
                        cert_label = (
                            "green" if cert_pub == "\U0001F7E2" else "yellow"
                        )
                        warnings["W002"].append(
                            f"  file={rel} id={eid!r} "
                            f"public.mechanism.certainty={cert_label} "
                            f"無 source_ids"
                        )

    # ── W003: 孤兒條目 ──
    for rel, entry in all_entries:
        eid = entry.get("id")
        if not eid:
            continue
        outbound = collect_outbound_ids(entry)
        is_pointed_to = inbound_ids.get(eid, 0) > 0
        has_outbound = len(outbound) > 0
        if not is_pointed_to and not has_outbound:
            warnings["W003"].append(f"  file={rel} id={eid!r}")

    # ── 統計 ──
    has_error = any(len(v) > 0 for v in errors.values())
    total_errors = sum(len(v) for v in errors.values())
    total_warns = sum(len(v) for v in warnings.values())

    # ── stdout 摘要 ──
    sep = "=" * 60
    print(sep)
    print("Vortex canonical 驗證摘要")
    print(f"掃描日期: {date.today()}")
    print(f"驗證條目數: {len(all_entries)}")
    print(f"Drills ID 數: {len(drills_id_set)}")
    print(f"全域 ID 集合: {len(all_id_set)}")
    print(sep)
    print()

    for code, items in errors.items():
        tag = "[ERROR]" if items else "[OK]   "
        print(f"  {tag} {code}: {len(items)} 筆")

    for code, items in warnings.items():
        tag = "[WARN] " if items else "[OK]   "
        print(f"  {tag} {code}: {len(items)} 筆")

    print()
    print(f"總計: {total_errors} ERROR, {total_warns} WARN")
    if has_error:
        print("[RESULT] FAIL - 有 ERROR，請查 reports/validation_report.md")
    else:
        print("[RESULT] PASS - 無 ERROR (WARN 見 reports/validation_report.md)")
    print(sep)

    # ── 生成 markdown 報告 ──
    REPORTS_DIR.mkdir(exist_ok=True)
    _write_report(errors, warnings, len(all_entries), len(drills_id_set))

    return 1 if has_error else 0


def _write_report(
    errors: dict,
    warnings: dict,
    entry_count: int,
    drills_count: int,
):
    lines: list[str] = []
    lines.append("# Vortex Canonical 驗證報告")
    lines.append("")
    lines.append(f"> 生成日期：{date.today()}  ")
    lines.append(f"> 驗證條目數：{entry_count}，Drills ID 數：{drills_count}")
    lines.append("")
    lines.append("---")
    lines.append("")

    code_meta = {
        "E001": (
            "ERROR",
            "已知條目陣列鍵中發現缺 `id` 的元素",
        ),
        "E002": (
            "ERROR",
            "`id` 全域重複（驗證範圍內）",
        ),
        "E003": (
            "ERROR",
            "`links.*` 指向不存在的 ID",
        ),
        "E004": (
            "ERROR",
            "`category`/`stroke`/`certainty`/`status` 出現不在 `_taxonomy.yaml` 的值",
        ),
        "E005": (
            "ERROR",
            "`source_ids` 指向不存在的 `_sources.yaml` ID",
        ),
        "W001": (
            "WARN",
            "`cross_ref` 為自由文字、無法解析成穩定 ID（S4 待辦）",
        ),
        "W002": (
            "WARN",
            "`certainty` 為 green 或 yellow 但沒有 `source_ids`（S3 待辦）",
        ),
        "W003": (
            "WARN",
            "孤兒條目：無 links 指入、自身也無指出",
        ),
    }

    for code, (tag, desc) in code_meta.items():
        items = errors.get(code, warnings.get(code, []))
        lines.append(f"## {code} — {desc}")
        lines.append("")
        lines.append(f"**{tag}，共 {len(items)} 筆**")
        lines.append("")
        if items:
            # W001/W002/W003 總數是 S3/S4 工作量依據，完整列出
            max_show = 200 if code in ("W001", "W002") else len(items)
            for item in items[:max_show]:
                lines.append(item)
            if len(items) > max_show:
                lines.append(
                    f"  ... （共 {len(items)} 筆，已顯示前 {max_show} 筆）"
                )
        else:
            lines.append("（無）")
        lines.append("")
        lines.append("---")
        lines.append("")

    report_path = REPORTS_DIR / "validation_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[INFO] 報告已寫入 {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        exit_code = run_validation()
    except Exception:
        traceback.print_exc()
        sys.exit(2)
    sys.exit(exit_code)
