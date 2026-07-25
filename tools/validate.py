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
        （任意深度的區塊，不限條目頂層）
  E006  cross_ref_ids 內含無法解析的 ID（canonical 全集 + Drills）
  E007  links.*_link_ids 內含無法解析的 ID（canonical 全集 + Drills）
  W001  cross_ref 字串中偵測到疑似穩定 ID 的 token，但該 token 沒有列入
        同一層的 cross_ref_ids（ids 與顯示字串脫節）
  W002  certainty 為 green/yellow 且**有**來源顯示資訊（source 字串或
        sources 清單），但同一區塊沒有 source_ids（機器鍵沒跟上顯示層）
  W003  孤兒條目：沒有任何 links 指入、自己也沒指出
  W004  links.*_link 字串中偵測到疑似穩定 ID 的 token，但該 token 沒有列入
        對應的 links.*_link_ids（ids 與顯示字串脫節）
  W005  links 下未知子鍵（不在 ID 參照類、詞彙參照類或已知自由文字類中）
  W006  cross_ref 有值但完全沒有 cross_ref_ids 欄位（連空陣列都沒有）
  W007  links.*_link 有非空字串但完全沒有對應的 *_link_ids 欄位
        （連空陣列都沒有）
  W008  孤兒來源：_sources.yaml 有登錄但沒有任何條目以 source_ids 引用
  W009  certainty 為 green/yellow 且**完全沒有**任何來源資訊
        （既無 source/sources 顯示字串，也無 source_ids）→ S3b 範圍

備註：
  canonical/health/drafts/ 是 build source，canonical/health/injuries.yaml
  是 build artifact（正式 canonical）。本驗證器只掃 injuries.yaml，
  排除 drafts/ 以避免 ID 重複誤報。

  cross_ref / cross_ref_ids 分工（S4c）：
    cross_ref      顯示層自由文字，下游 my-site 的 vortex-database.html 直接
                   當純字串渲染，**不可改成陣列**（會印出 Go slice 字面值）。
    cross_ref_ids  機器鍵（list of string），放從 cross_ref 抽出且確實能在
                   全域 ID 集合解析的穩定 ID。
                   `[]` = 已檢查過、確認無 ID 可連（多為指向 Instructional/
                   散文的節號）；欄位缺席 = 尚未處理（W006）。

  *_link / *_link_ids 分工（S4b，與 cross_ref 同一模式）：
    mechanism_link / technical_link / perception_link
                   顯示層自由文字，下游 my-site 的 vortex-injuries.html 直接
                   當純字串渲染，**不可改名或改成陣列**（會印出 Go slice 字面值）。
    *_link_ids     機器鍵（list of string），放從對應 *_link 抽出且確實能在
                   全域 ID 集合解析的穩定 ID。
                   `[]` = 已檢查過、確認無 ID 可連（多為指向尚未建立的
                   technical 條目、或無 stroke 前綴因而無法解析的水感層級
                   L0/L4–L6 這類敘述）；欄位缺席 = 尚未處理（W007）。
    真相來源是 canonical/health/drafts/*.yaml，改完要重跑
    tools/build_injuries.py；**不可直接改 canonical/health/injuries.yaml**。

  source / source_ids 分工（S3a，與 cross_ref 同一模式）：
    source         顯示層自由文字，下游 my-site 的 vortex-*.html 直接當純字串
                   渲染，**不可改寫或改成陣列**。
    source_ids     機器鍵（list of string），指向 canonical/_sources.yaml 的
                   src.<slug>。**與 certainty / source 放在同一個區塊**
                   （證據 block 上，不是掛在條目頂層），機器鍵才不會跨層對錯。
    certainty 掃描範圍（S3a 修正）：舊版只看 entry.certainty 與
    entry.public.mechanism.certainty（覆蓋 88 個區塊），實際上 934 個帶
    certainty 的區塊散落在 evidence / references / phenomenon / epidemiology
    等任意深度。現改為遞迴掃描任何含 certainty 的 dict，W002/W009 數字因此
    大幅上升——那是原本就存在、只是沒被看見的債。
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

# 自由文字顯示類：mechanism_link、technical_link、perception_link 值是散文，
# 下游 my-site 當純字串渲染，不可改名或改成陣列（S4b 定案）。
# 機器可解析的部分改放同名 + _ids 的機器鍵（見 LINKS_IDS_KEYS）。
# 真相來源是 canonical/health/drafts/*.yaml，改完重跑 tools/build_injuries.py；
# 不可直接改 canonical/health/injuries.yaml（promoted artifact，檔頭寫明勿手改）。
LINKS_FREE_TEXT_KEYS = {"mechanism_link", "technical_link", "perception_link"}

# 機器鍵類（E007 / W004 / W007 檢查對象）：每個自由文字顯示鍵對應一個 _ids 鍵，
# 值為 list of string，元素必須能在全域 ID 集合解析。
LINKS_IDS_KEYS = {k + "_ids" for k in LINKS_FREE_TEXT_KEYS}

# 用於從散文值中保守抽取候選 ID 的 regex
# 匹配命名空間格式（如 free.tech.10、back.err2、starts-turns.err10）
# 或 Drill 編號（如 FrBr3、Fr1、Bk22）
# 注意：命名空間段允許 - 與 _（真實 ID 有 starts-turns.tech.44、
# psych.self_talk.trainable_skill 這類形態），最後一段不限定為純數字，
# 否則 back.err2 / starts-turns.err10 這類會漏抽。
import re as _re
_CANDIDATE_ID_RE = _re.compile(
    r"(?<![0-9A-Za-z_.-])(?:"
    r"[a-z][a-z0-9_-]*(?:\.[a-z0-9_-]+)+"   # 命名空間格式：free.tech.10 / back.err2
    r"|[A-Z][a-z][A-Z]?[a-z]*\d+"            # Drill 編號格式：FrBr3 / Fr1 / Bk22
    r")"
)


def extract_candidate_ids(text: str) -> list[str]:
    """從自由文字中保守抽取疑似穩定 ID 的 token（保序去重）。

    只做形態辨識，不保證能解析——是否存在由呼叫端比對全域 ID 集合決定。
    """
    found: list[str] = []
    for token in _CANDIDATE_ID_RE.findall(text or ""):
        if token not in found:
            found.append(token)
    return found


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


def iter_blocks(data: object, path: str = "", nearest_id: str = "(no id)"):
    """遞迴走訪 YAML 樹，yield (dot_path, nearest_entry_id, dict)。

    與 iter_entries() 的差別：iter_entries 只給「有 id 的 dict」（條目層），
    本函式給**每一個 dict**，並附帶它在檔案內的路徑與最近一層祖先條目的 id。
    certainty / source / source_ids 這類欄位可以出現在任意深度（evidence[]、
    references[]、public.mechanism、public.phenomenon…），只掃條目層會漏掉
    絕大多數區塊，所以 E005 / W002 / W009 都走這一份走訪。
    """
    if isinstance(data, dict):
        if isinstance(data.get("id"), str):
            nearest_id = data["id"]
        yield (path or "(root)", nearest_id, data)
        for k, v in data.items():
            child = f"{path}.{k}" if path else str(k)
            yield from iter_blocks(v, child, nearest_id)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            yield from iter_blocks(item, f"{path}[{i}]", nearest_id)


def has_display_source(block: dict) -> bool:
    """區塊上是否有「來源顯示資訊」。

    兩種既有寫法都算：
      source   單數字串（instructional / technica）
      sources  複數字串清單（health/injuries、psychology）
    有顯示資訊但缺機器鍵 → W002；兩者皆無 → W009（需要補來源，不是補鍵）。
    """
    src = block.get("source")
    if isinstance(src, str) and src.strip():
        return True
    srcs = block.get("sources")
    if isinstance(srcs, list) and any(
        isinstance(s, str) and s.strip() for s in srcs
    ):
        return True
    return False


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


# ── 全域 ID 集合 ──────────────────────────────────────────────────────────────

def build_global_id_set() -> tuple[set[str], set[str], set[str]]:
    """建立全域 ID 集合，回傳 (all_id_set, canonical_id_set, drills_id_set)。

    canonical 端含 drafts/（drafts 條目仍是合法參照目標），只排除 _ 前綴
    meta 檔。E003（links 斷鏈）與 E006（cross_ref_ids 斷鏈）都以此為準。
    需要抽 ID 的外部腳本請直接呼叫本函式，不要另寫一份收集邏輯。
    """
    all_canonical_files = sorted(CANONICAL_DIR.rglob("*.yaml"))
    id_source_files = [
        p for p in all_canonical_files if not p.name.startswith("_")
    ]
    drills_files = sorted(DRILLS_DIR.glob("*.yaml"))
    canonical_id_set = set(collect_all_ids_from_files(id_source_files).keys())
    drills_id_set = set(collect_all_ids_from_files(drills_files).keys())
    return canonical_id_set | drills_id_set, canonical_id_set, drills_id_set


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


# ── 機器鍵（*_ids）共用檢查 ───────────────────────────────────────────────────

def collect_declared_ids(
    rel: str,
    eid: str,
    ids_key: str,
    raw_ids: object,
    has_ids_key: bool,
    all_id_set: set,
    sink: list,
) -> list[str]:
    """驗證一個 *_ids 機器鍵並回傳其中宣告的 ID 清單。

    型別錯誤、非字串元素、無法解析的 ID 都寫進 sink（呼叫端給對應的
    ERROR 清單：cross_ref_ids → E006、links.*_link_ids → E007）。
    cross_ref_ids 與 *_link_ids 共用本函式，不各寫一份。
    """
    declared_ids: list[str] = []
    if isinstance(raw_ids, list):
        for item in raw_ids:
            if isinstance(item, str) and item.strip():
                declared_ids.append(item)
                if item not in all_id_set:
                    sink.append(
                        f"  file={rel} id={eid!r} "
                        f"{ids_key} 含無法解析的 {item!r}"
                    )
            else:
                sink.append(
                    f"  file={rel} id={eid!r} "
                    f"{ids_key} 含非字串元素 {item!r}"
                )
    elif has_ids_key and raw_ids is not None:
        sink.append(
            f"  file={rel} id={eid!r} {ids_key} "
            f"型別應為 list，實際為 {type(raw_ids).__name__}"
        )
    return declared_ids


def missing_declared_ids(
    text: str, declared_ids: list[str], all_id_set: set
) -> list[str]:
    """列出 text 內疑似穩定 ID、但沒被宣告進 *_ids 的 token。

    候選一律由 extract_candidate_ids() 產生（唯一一份抽取邏輯），另補一種
    形態辨識抓不到的情況：整個字串本身就是一個可解析的 ID。health 傷害條目
    的 ID 是裸 slug（red-s、female-athlete-triad），沒有命名空間點號，regex
    認不出來——而「整個 *_link 就填一個條目 ID」正是 links.*_link 最常見的
    寫法，不補這一項 W004 對它零覆蓋。W001（cross_ref）共用同一規則。
    """
    candidates = extract_candidate_ids(text)
    whole = (text or "").strip()
    if whole and whole in all_id_set and whole not in candidates:
        candidates.append(whole)
    return [t for t in candidates if t not in declared_ids]


# ── cross_ref 契約檢查（E006 / W001 / W006）───────────────────────────────────

def check_cross_ref(
    rel: str,
    eid: str,
    container: dict,
    location: str,
    all_id_set: set,
    errors: dict,
    warnings: dict,
):
    """檢查單一層（entry 或 public）的 cross_ref / cross_ref_ids 契約。

    E006  cross_ref_ids 內有無法解析的值（或型別不是 list）→ ERROR
    W001  cross_ref 字串裡有疑似穩定 ID 的 token，但沒列進 cross_ref_ids
    W006  cross_ref 有值但沒有 cross_ref_ids 欄位（連 [] 都沒寫）

    注意：不做任何 ASCII encode 轉換，直接保留原始 Unicode 字串，
    才能在報告中正確顯示中文。顯示截斷為 120 字元。
    """
    has_ids_key = "cross_ref_ids" in container
    declared_ids = collect_declared_ids(
        rel, eid, f"{location}.cross_ref_ids",
        container.get("cross_ref_ids"), has_ids_key,
        all_id_set, errors["E006"],
    )

    cr = container.get("cross_ref")
    if not (isinstance(cr, str) and cr.strip()):
        return

    if not has_ids_key:
        # 尚未處理：與「明確宣告 []（已檢查、無 ID 可連）」區分開
        warnings["W006"].append(
            f"  file={rel} id={eid!r} {location}.cross_ref 有值但缺 "
            f"cross_ref_ids 欄位 (120 chars): {cr[:120]!r}"
        )
        return

    missing = missing_declared_ids(cr, declared_ids, all_id_set)
    if missing:
        warnings["W001"].append(
            f"  file={rel} id={eid!r} {location}.cross_ref 內疑似穩定 ID "
            f"{missing} 未列入 cross_ref_ids (120 chars): {cr[:120]!r}"
        )


# ── links.*_link 契約檢查（E007 / W004 / W007）────────────────────────────────

def check_link_ids(
    rel: str,
    eid: str,
    links: dict,
    all_id_set: set,
    errors: dict,
    warnings: dict,
):
    """檢查 links 下三個自由文字顯示鍵與其 *_link_ids 機器鍵的契約。

    E007  *_link_ids 內有無法解析的值（或型別不是 list）→ ERROR
    W004  *_link 字串裡有疑似穩定 ID 的 token，但沒列進對應的 *_link_ids
    W007  *_link 有非空字串但沒有 *_link_ids 欄位（連 [] 都沒寫）

    注意：不做任何 ASCII encode 轉換，直接保留原始 Unicode 字串，
    才能在報告中正確顯示中文。顯示截斷為 120 字元。
    """
    for link_key in sorted(LINKS_FREE_TEXT_KEYS):
        ids_key = link_key + "_ids"
        has_ids_key = ids_key in links
        declared_ids = collect_declared_ids(
            rel, eid, f"links.{ids_key}",
            links.get(ids_key), has_ids_key,
            all_id_set, errors["E007"],
        )

        val = links.get(link_key)
        if not (isinstance(val, str) and val.strip()):
            continue

        if not has_ids_key:
            # 尚未處理：與「明確宣告 []（已檢查、無 ID 可連）」區分開
            warnings["W007"].append(
                f"  file={rel} id={eid!r} links.{link_key} 有值但缺 "
                f"{ids_key} 欄位 (120 chars): {val[:120]!r}"
            )
            continue

        missing = missing_declared_ids(val, declared_ids, all_id_set)
        if missing:
            warnings["W004"].append(
                f"  file={rel} id={eid!r} links.{link_key} 內疑似穩定 ID "
                f"{missing} 未列入 {ids_key} (120 chars): {val[:120]!r}"
            )


# ── source 契約檢查（E005 / W002 / W009）──────────────────────────────────────

def check_source_blocks(
    rel: str,
    data: object,
    allowed_source_ids: set,
    errors: dict,
    warnings: dict,
) -> set[str]:
    """遞迴檢查單一檔案內所有區塊的 source 契約，回傳被引用到的 source_id。

    E005  source_ids 型別錯、含非字串元素、或指向 _sources.yaml 沒有的 ID
    W002  certainty green/yellow + 有 source/sources 顯示字串 + 缺 source_ids
    W009  certainty green/yellow + 完全沒有來源資訊

    走 iter_blocks()（任意深度），不是只看條目頂層——certainty 與 source 大多
    掛在 evidence[] / references[] / public.mechanism 這類巢狀區塊上。
    回傳值供呼叫端做 W008（孤兒來源）比對。
    """
    referenced: set[str] = set()
    for loc, eid, block in iter_blocks(data):
        raw_ids = block.get("source_ids")
        if "source_ids" in block:
            if isinstance(raw_ids, list):
                for sid in raw_ids:
                    if isinstance(sid, str) and sid.strip():
                        referenced.add(sid)
                        if sid not in allowed_source_ids:
                            errors["E005"].append(
                                f"  file={rel} id={eid!r} at={loc} "
                                f"source_ids 包含不存在的 {sid!r}"
                            )
                    else:
                        errors["E005"].append(
                            f"  file={rel} id={eid!r} at={loc} "
                            f"source_ids 含非字串元素 {sid!r}"
                        )
            elif raw_ids is not None:
                errors["E005"].append(
                    f"  file={rel} id={eid!r} at={loc} source_ids "
                    f"型別應為 list，實際為 {type(raw_ids).__name__}"
                )

        cert = block.get("certainty")
        if cert not in CERTAINTY_NEEDS_SOURCE:
            continue
        if raw_ids:
            continue
        cert_label = "green" if cert == "\U0001F7E2" else "yellow"
        if has_display_source(block):
            field = "source" if block.get("source") else "sources"
            warnings["W002"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"certainty={cert_label} 有 {field} 顯示字串但無 source_ids"
            )
        else:
            warnings["W009"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"certainty={cert_label} 完全無來源資訊"
                f"（無 source/sources，也無 source_ids）"
            )
    return referenced


def check_orphan_sources(
    allowed_source_ids: set,
    referenced_source_ids: set,
    warnings: dict,
):
    """W008：_sources.yaml 有登錄但沒有任何條目以 source_ids 引用。"""
    for sid in sorted(allowed_source_ids - referenced_source_ids):
        warnings["W008"].append(
            f"  source_id={sid!r} 已登錄於 _sources.yaml 但無任何條目引用"
        )


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

    # ── 建立全域 ID 集合（含 Drills，用於 E003 / E006 參照）──
    all_id_set, _canonical_id_set, drills_id_set = build_global_id_set()

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
        "E001": [], "E002": [], "E003": [], "E004": [], "E005": [],
        "E006": [], "E007": []
    }
    warnings: dict[str, list[str]] = {
        "W001": [], "W002": [], "W003": [], "W004": [], "W005": [],
        "W006": [], "W007": [], "W008": [], "W009": []
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
        # 自由文字顯示類（*_link）與其機器鍵（*_link_ids）另由
        # check_link_ids() 檢查（E007 / W004 / W007）。
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
                elif link_type in LINKS_FREE_TEXT_KEYS:
                    # 自由文字顯示鍵：契約由 check_link_ids() 統一檢查
                    pass
                elif link_type in LINKS_IDS_KEYS:
                    # 機器鍵：契約由 check_link_ids() 統一檢查
                    pass
                else:
                    # 未知子鍵（W005 fail-closed）：
                    # 不在 ID 參照類、詞彙參照類或已知自由文字類中
                    val_preview = ""
                    if isinstance(targets, str):
                        val_preview = targets[:120]
                    elif isinstance(targets, list):
                        val_preview = str(targets)[:120]
                    warnings["W005"].append(
                        f"  file={rel} id={eid!r} "
                        f"links.{link_type} 未歸類，值前120字: {val_preview!r}"
                    )

            # ── E007 / W004 / W007: *_link 與 *_link_ids 契約 ──
            check_link_ids(rel, eid, links, all_id_set, errors, warnings)

        # ── E004: taxonomy 不存在的值 ──
        for field in ("category", "stroke", "certainty", "status"):
            val = entry.get(field)
            if val is not None and isinstance(val, str):
                allowed = taxonomy.get(field, set())
                if val not in allowed:
                    errors["E004"].append(
                        f"  file={rel} id={eid!r} {field}={val!r}"
                    )

        # ── E005: source_ids 斷鏈 ──
        # 已移到下方「逐區塊檢查」的遞迴走訪（source_ids 可出現在任意深度，
        # 只掃條目頂層會漏掉 evidence[] 上的 201 筆機器鍵）。

        # ── E006 / W001 / W006: cross_ref 契約（entry 頂層與 public 層）──
        check_cross_ref(rel, eid, entry, "entry", all_id_set, errors, warnings)
        pub = entry.get("public", {})
        if isinstance(pub, dict):
            check_cross_ref(
                rel, eid, pub, "public", all_id_set, errors, warnings
            )

    # ── 逐區塊檢查（E005 / W002 / W009）：遞迴走訪任意深度 ──
    # certainty 與 source/source_ids 多數不在條目頂層，而在 evidence[]、
    # references[]、public.mechanism 這類巢狀區塊上；per-entry 迴圈看不到。
    referenced_source_ids: set[str] = set()
    for path in validate_files:
        try:
            data = load_yaml(path)
        except Exception:
            continue
        rel = str(path.relative_to(ROOT))
        referenced_source_ids |= check_source_blocks(
            rel, data, allowed_source_ids, errors, warnings
        )

    # ── W008: 孤兒來源（_sources.yaml 有登錄但沒人引用）──
    check_orphan_sources(allowed_source_ids, referenced_source_ids, warnings)

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
        "E006": (
            "ERROR",
            "`cross_ref_ids` 內含無法解析的 ID",
        ),
        "E007": (
            "ERROR",
            "`links.*_link_ids` 內含無法解析的 ID",
        ),
        "W001": (
            "WARN",
            "`cross_ref` 內的疑似穩定 ID 未列入同層 `cross_ref_ids`",
        ),
        "W002": (
            "WARN",
            "`certainty` green/yellow 且**有**來源顯示字串（`source`/`sources`）"
            "但同區塊缺 `source_ids`（機器鍵沒跟上顯示層）",
        ),
        "W003": (
            "WARN",
            "孤兒條目：無 links 指入、自身也無指出",
        ),
        "W004": (
            "WARN",
            "`links.*_link` 內的疑似穩定 ID 未列入對應的 `links.*_link_ids`",
        ),
        "W005": (
            "WARN",
            "`links` 下未知子鍵（未歸類為 ID 參照類、詞彙參照類或已知自由文字類）",
        ),
        "W006": (
            "WARN",
            "`cross_ref` 有值但缺 `cross_ref_ids` 欄位（未處理；`[]` 才是「已檢查、無 ID 可連」）",
        ),
        "W007": (
            "WARN",
            "`links.*_link` 有值但缺 `*_link_ids` 欄位（未處理；`[]` 才是「已檢查、無 ID 可連」）",
        ),
        "W008": (
            "WARN",
            "孤兒來源：`_sources.yaml` 有登錄但沒有任何條目以 `source_ids` 引用",
        ),
        "W009": (
            "WARN",
            "`certainty` green/yellow 且**完全沒有**來源資訊"
            "（無 `source`/`sources`，也無 `source_ids`）→ 需補來源，S3b 範圍",
        ),
    }

    w004_header_written = False
    w002_header_written = False

    for code, (tag, desc) in code_meta.items():
        items = errors.get(code, warnings.get(code, []))
        lines.append(f"## {code} — {desc}")
        lines.append("")
        lines.append(f"**{tag}，共 {len(items)} 筆**")
        lines.append("")

        # W002 區塊開頭附說明
        if code == "W002" and not w002_header_written:
            w002_header_written = True
            lines.append(
                "> **契約說明（S3a）**：`source` 是顯示層自由文字（下游 my-site 當純"
                "字串渲染，不可改寫或改成陣列）；可解析的來源鍵放同區塊的 "
                "`source_ids`，指向 `canonical/_sources.yaml` 的 `src.<slug>`。"
                "W002 與 W009 都是「🟢/🟡 但沒有 `source_ids`」，差別在**有沒有來源"
                "顯示資訊**：W002 已經有 `source`/`sources` 字串，只差把它登錄成"
                "來源條目再補機器鍵（純遷移）；W009 連顯示字串都沒有，得回頭找出"
                "主張的依據（S3b，不能靠遷移解決）。兩者不可互相代替，也不可用"
                "佔位來源填掉 W009。"
            )
            lines.append("")

        # W004 區塊開頭附說明
        if code == "W004" and not w004_header_written:
            w004_header_written = True
            lines.append(
                "> **契約說明（S4b）**：`mechanism_link` / `technical_link` / "
                "`perception_link` 是顯示層自由文字（下游 my-site 當純字串渲染，"
                "不可改名或改成陣列）；可解析的穩定 ID 放同名 + `_ids` 的機器鍵。"
                "本節列出「顯示字串裡看得到 ID、但機器鍵沒同步」的脫節案例。"
                "修法是改 `canonical/health/drafts/*.yaml` 補進 `*_link_ids` 再重跑 "
                "`tools/build_injuries.py`。"
                "**不可直接改 `canonical/health/injuries.yaml`**（promoted artifact，檔頭寫明勿手改）。"
            )
            lines.append("")

        if items:
            # WARN 類總數是後續工作量依據，列到 400 筆（W009 是 S3b 全量清單）
            max_show = (
                400 if code in (
                    "W001", "W002", "W004", "W005", "W006", "W007",
                    "W008", "W009",
                )
                else len(items)
            )
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
