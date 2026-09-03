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
  E008  category 跨網域誤用：值合法（在 _taxonomy.yaml）但該值的 scope
        不含本檔所屬網域（instructional / health / drills）
  E009  條目的 category 未宣告於**該檔自己的 categories 區塊**
        → my-site 查表落空會渲染成空字串（無錯誤訊息的靜默失敗）
  E010  診斷層洩漏：診斷型鍵名（perception_probe / signal_structure /
        discriminators / type_diagnosis…）出現在 `public` 子樹內。
        sync_vortex.py 是白名單（`rec.update(pub)` 整包搬 public），
        所以 public 底下的任何東西都會上公開站——診斷判讀語寫在
        public 裡是唯一的實際洩漏路徑（S6）
  E011  evidence_from 內含無法解析的 ID。evidence_from 是 W009 的豁免路徑
        （「本句證據由所列子條目承擔」），不驗證它指得到東西的話，寫一個
        不存在的 ID 也能消警告——這條檢查是那個豁免的代價（S3b）
  E012  movement 受控值不在 _taxonomy.yaml 對應欄位（原 W013，2026-09-02
        升級）。這組欄位打錯字會 **fail-open**：sync_vortex.py 只擋
        `draft`/`withheld` 兩個字面值，`publication_status` 拼錯即上站；
        `action_status` 拼錯會讓 do-not-prescribe 與 W016 閘一起穿透
  W001  cross_ref 字串中偵測到疑似穩定 ID 的 token，但該 token 沒有列入
        同一層的 cross_ref_ids（ids 與顯示字串脫節）
  W002  區塊有來源顯示資訊（source 字串或 sources 清單）但沒有 source_ids
        （機器鍵沒跟上顯示層）。**不看 certainty**——見下方 S3a-2 說明
  W003  孤兒條目：沒有任何 links 指入、自己也沒指出
  W004  links.*_link 字串中偵測到疑似穩定 ID 的 token，但該 token 沒有列入
        對應的 links.*_link_ids（ids 與顯示字串脫節）
  W005  links 下未知子鍵（不在 ID 參照類、詞彙參照類或已知自由文字類中）
  W006  cross_ref 有值但完全沒有 cross_ref_ids 欄位（連空陣列都沒有）
  W007  links.*_link 有非空字串但完全沒有對應的 *_link_ids 欄位
        （連空陣列都沒有）
  W008  孤兒來源：_sources.yaml 有登錄但沒有任何條目以 source_ids 引用
  W009  certainty 為 green/yellow 且**完全沒有**任何來源資訊
        （既無 source/sources/citation 顯示字串，也無 source_ids，
        祖先區塊也沒有，且未以 evidence_from 宣告證據由子條目承擔）
        → S3b 範圍
  W010  死標籤：categories 區塊宣告了某 key，但該檔沒有任何條目使用
  W011  certainty 為 orange（教練觀測）但缺 observation_basis：
        教練觀測是第一手實務證據，不需要 source_ids，但必須說出
        觀察基礎與外推邊界，否則與「沒有依據」無法區分（S6）
  W012  movement ID 的檔案命名空間或分段格式違規
  W014  movement 跨檔引用無法解析，或連到存在但命名空間錯誤的 ID
  W015  published movement 條目缺少狀態、證據或介入決策必填欄位
  W016  mobility_decision 為 evidence-gap，但該介入仍寫成可執行處方
        （action_status 不是 do-not-prescribe，或帶了劑量來源）
  W017  demand 的 (stroke, phase) 未登錄於 movement_phase_registry，
        或 phase_model 與登錄表不符（相位跨分期系統搬運）
  W018  demand 缺 action_reference_frame，或標 joint-local 卻無分節段量測
        支撐（source_ids 空且未標 do-not-prescribe）：由池畔可見的空間量
        反推關節動作，是 C 類蒐證命中最多次的結構性根因
  W019  demand 文字出現量化主張但缺 measurement_conditions，或該欄的必填
        子鍵缺漏／source_id 無法解析：數值不得裸奔進 demand

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

  source / sources / source_ids 分工（S3a，與 cross_ref 同一模式）：
    source         顯示層自由文字（單數，字串）。下游 my-site 的 vortex-*.html
                   直接當純字串渲染，**不可改寫或改成陣列**。
    sources        顯示層自由文字（複數，list of string）。psychology.yaml 與
                   health/injuries.yaml 用這一種，my-site 的
                   vortex-injuries.html 直接 range 它，**不可改名成 source**。
                   兩種顯示形式並存是既有事實；驗證器對兩者一視同仁，
                   不為了統一而改欄位名（那會炸掉線上頁面）。
    source_ids     機器鍵（list of string），指向 canonical/_sources.yaml 的
                   src.<slug>。**與 source / sources 放在同一個區塊**
                   （證據 block 上，不是掛在條目頂層），機器鍵才不會跨層對錯。

    掃描範圍（S3a 修正）：舊版只看 entry.certainty 與
    entry.public.mechanism.certainty（覆蓋 88 個區塊），實際上 934 個帶
    certainty 的區塊散落在 evidence / references / phenomenon / epidemiology
    等任意深度。現改為遞迴掃描任何含 certainty 的 dict。

    W002 與 certainty 解耦（S3a-2）：「這個區塊有沒有標確定性」跟「這個來源
    該不該進註冊表」是兩件事，把 W002 綁在 certainty 上是舊 W002 框架的殘留。
    現在只要區塊有 source/sources 顯示字串就要求 source_ids。W009 不動——
    它問的是「標了 🟢/🟡 卻拿不出任何來源」，本來就以 certainty 為前提。

    來源檢查（E005/W002/W009）另外掃 Drills/*.yaml：Drills 也有大量帶 source
    的區塊，過去完全不在任何檢查範圍內。只擴這一組代碼，不把 Drills 併進
    validate_files——否則 E001/W003/W005 這些 canonical 專屬規則會一次
    套到全部 drills 上，那是另一個決策。S2 另把 E004/E008/E009/W010 加進
    這個 Drills 專段（category 是 Drills 與 canonical 共用的欄位，不擴就是死碼）。

  category 的兩層真相來源（S2）：
    canonical/_taxonomy.yaml   擁有**合法 key 集合 + 每個值的 scope**。
                               category 是三個互不相交的值空間共用一個欄位名
                               （instructional 技術面向 / health 傷害類別 /
                               drills 練習環節），scope 是唯一把它們分開的機制。
                               不改欄位名——改名會炸掉四份 my-site layout
                               與 `where $injuries "category" "D-..."`。
    各資料檔的 categories 區塊  擁有**標籤（name_zh / zh）**。同一個 key 在不同
                               檔可有不同措辭（kick 在 technical-analysis 是
                               「踢水與腿部機制」，在 teaching-errors / drills 是
                               「踢腿」），所以標籤不上收到 taxonomy。
                               Drills 的標籤真相源是 Drills/_categories.yaml。
                               my-site 一律從資料 merge，不得硬編副本。
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
MOVEMENT_DIR = CANONICAL_DIR / "movement"

# movement 驗證只掃這四個內容檔；_index.yaml 是 _ 前綴 meta 檔，不在範圍內。
MOVEMENT_FILE_RULES = {
    "actions.yaml": ("actions", "movement.action."),
    "muscle-groups.yaml": ("muscle_groups", "movement.muscle."),
    "stroke-demands.yaml": ("demands", "movement.demand."),
    "interventions.yaml": ("interventions", "movement.intervention."),
}

MOVEMENT_TAXONOMY_FIELDS = (
    "publication_status",
    "claim_status",
    "action_status",
    "evidence_profile",
    "mobility_decision",
    "phase_model",
    "action_reference_frame",
)

MEASUREMENT_CONDITION_SUBKEYS = (
    "source_id",
    "quantity",
    "value",
    "conditions",
    "endpoint",
    "extrapolation_boundary",
)

MOVEMENT_REFERENCE_FIELDS = {
    "action_ids": "movement.action.",
    "muscle_ids": "movement.muscle.",
    "demand_ids": "movement.demand.",
    "intervention_ids": "movement.intervention.",
}

# movement → 既有網域的反向橋。這些欄位指向 movement 以外的 canonical ID，
# 所以不能套 MOVEMENT_REFERENCE_FIELDS 的「必須是 movement.*」規則，改為
# 「必須存在於 canonical，且必須不是 movement.*」——後者用來擋把 demand_ids
# 該做的事寫進 derived_from_ids。
MOVEMENT_EXTERNAL_REFERENCE_FIELDS = ("derived_from_ids",)

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
_MOVEMENT_ID_SEGMENT_RE = _re.compile(r"^[a-z][a-z0-9-]*$")
_CANDIDATE_ID_RE = _re.compile(
    r"(?<![0-9A-Za-z_.-])(?:"
    r"[a-z][a-z0-9_-]*(?:\.[a-z0-9_-]+)+"   # 命名空間格式：free.tech.10 / back.err2
    r"|[A-Z][a-z][A-Z]?[a-z]*\d+"            # Drill 編號格式：FrBr3 / Fr1 / Bk22
    r")"
)

# W019：判定「本筆文字出現量化主張」的形狀。四批 C 類蒐證裡真正出事的數值
# 就是這四類——百分比（Cortesi 的 4–5.2% vs 10.4–10.9%）、角度（FoFS 的
# 25–30°）、秒數（0.12 s）、統計量（Strzała 的 r=0.35）。刻意不含裸數字，
# 否則 n=15、L0–L6、2D／3D 這類非主張數字會淹掉訊號。
MEASUREMENT_CLAIM_PATTERNS = (
    _re.compile(r"\d+(?:[.,]\d+)?\s*(?:[–~-]|至)?\s*\d*(?:[.,]\d+)?\s*%"),
    _re.compile(r"\d+(?:[.,]\d+)?\s*(?:[–~-]|至)?\s*\d*(?:[.,]\d+)?\s*°"),
    _re.compile(r"\d+(?:[.,]\d+)?\s*(?:ms|s)\b"),
    _re.compile(r"\b[rdp]\s*=\s*[-.\d]"),
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


def iter_blocks_with_source_inheritance(
    data: object,
    path: str = "",
    nearest_id: str = "(no id)",
    inherited: bool = False,
):
    """與 iter_blocks() 同樣走訪每個 dict，額外回傳「祖先是否已帶來源資訊」。

    yield (dot_path, nearest_entry_id, dict, inherited_source)

    為什麼 W009 需要這個：來源常登錄在條目層（例如 psychology 的
    `concepts[].public` 同時放 `sources` + `source_ids`），而 certainty 標在
    更細的子區塊（`public.phenomenon`）。只看同層的話，子區塊會被判成
    「完全沒有來源資訊」，但它的來源就在正上方一層——那不是缺口，是粒度差。
    實測 57 筆 W009 屬於這一類。

    inherited 只在「同一顆樹上的祖先」成立，不跨條目繼承。
    """
    if isinstance(data, dict):
        if isinstance(data.get("id"), str):
            nearest_id = data["id"]
        yield (path or "(root)", nearest_id, data, inherited)
        child_inherited = inherited or has_source_info(data)
        for k, v in data.items():
            child = f"{path}.{k}" if path else str(k)
            yield from iter_blocks_with_source_inheritance(
                v, child, nearest_id, child_inherited
            )
    elif isinstance(data, list):
        for i, item in enumerate(data):
            yield from iter_blocks_with_source_inheritance(
                item, f"{path}[{i}]", nearest_id, inherited
            )


def has_source_info(block: dict) -> bool:
    """區塊自身是否帶任何來源資訊（顯示字串或機器鍵）。"""
    if has_display_source(block):
        return True
    sids = block.get("source_ids")
    return isinstance(sids, list) and any(
        isinstance(s, str) and s.strip() for s in sids
    )


def display_source_field(block: dict) -> str:
    """回傳該區塊承載來源顯示字串的欄位名（供警告訊息用）。"""
    for field in ("source", "citation", "sources"):
        if block.get(field):
            return field
    return "source"


def has_evidence_from(block: dict) -> bool:
    """區塊是否以 evidence_from 宣告「本句的證據由所列子條目承擔」。

    用於綜述句：psychology 的 `themes[].premise` 是把整個主題底下 concepts 的
    研究結論濃縮成一句，它自己不對應單一文獻，證據是子條目的集合。這種句子
    要嘛拆成可裁決的單一主張，要嘛明講證據在哪些條目上——後者就是本欄位。
    空 list 不算宣告（等於沒指），與 cross_ref_ids 的 `[]` 語意不同。
    """
    ef = block.get("evidence_from")
    return isinstance(ef, list) and any(
        isinstance(x, str) and x.strip() for x in ef
    )


def has_display_source(block: dict) -> bool:
    """區塊上是否有「來源顯示資訊」。

    三種既有寫法都算：
      source    單數字串（instructional / technica）
      sources   複數字串清單（health/injuries、psychology）
      citation  references[] 元素的來源顯示字串（health/injuries）

    citation 是 S3b triage 才認出的第三種承載欄位：`references[]` 的每個元素
    形如 {citation, certainty, verified}，元素本身就是一筆來源（多數還內嵌
    PMC/PMID），只是欄位名不叫 source。S3a 沒認它，於是 101 筆「來源條目」
    被 W009 判成「有 🟢 但拿不出來源」——是要求一筆引用去引用另一筆引用。
    正確歸屬是 W002（有顯示字串、缺機器鍵，純遷移）。

    有顯示資訊但缺機器鍵 → W002；兩者皆無 → W009（需要補來源，不是補鍵）。
    """
    src = block.get("source")
    if isinstance(src, str) and src.strip():
        return True
    cit = block.get("citation")
    if isinstance(cit, str) and cit.strip():
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


def load_phase_registry() -> dict[str, dict[str, str]]:
    """回傳 {stroke: {phase_key: phase_model}}，供 W017 比對。

    相位鍵的合法範圍隨泳式而異（free 有 lift，breast 沒有），所以它不能像
    其他受控欄位那樣放進扁平的 fields，登錄在 movement_phase_registry。
    登錄表缺漏視為空集合——fail-closed，不預設放行。
    """
    data = load_yaml(TAXONOMY_FILE)
    strokes = (data.get("movement_phase_registry") or {}).get("strokes") or {}
    return {
        stroke: {
            phase["key"]: phase.get("phase_model")
            for phase in (phases or [])
            if isinstance(phase, dict) and isinstance(phase.get("key"), str)
        }
        for stroke, phases in strokes.items()
    }


def load_category_scope() -> dict[str, set[str]]:
    """回傳 {category_key: set_of_allowed_domains}。

    category 是三個互不相交的值空間（instructional / health / drills）共用
    同一個欄位名，光靠 E004 只能擋「不存在的值」，擋不住「把 health 的傷害
    類別寫進 drills 條目」這種跨域誤用。scope 缺漏視為未宣告（空集合），
    由 E008 報出——fail-closed，不預設放行。
    """
    data = load_yaml(TAXONOMY_FILE)
    field = data.get("fields", {}).get("category", {})
    return {
        item["key"]: set(item.get("scope") or [])
        for item in field.get("values", [])
    }


def domain_of(rel: str) -> str:
    """由檔案相對路徑推導條目所屬網域，供 E008 比對 scope。

    rel 由 str(path.relative_to(ROOT)) 產生，Windows 上是反斜線，
    這裡兩種分隔符都吃。
    """
    parts = rel.replace("\\", "/").split("/")
    if parts[0] == "Drills":
        return "drills"
    if parts[0] == "canonical" and len(parts) > 2:
        return parts[1]
    return "_root"


def check_category_scope(
    rel: str,
    eid: str,
    entry: dict,
    domain: str,
    category_scope: dict[str, set[str]],
    taxonomy: dict[str, set[str]],
    errors: dict[str, list[str]],
) -> None:
    """E008：條目的 category 必須容許出現在該條目所屬的網域。

    值本身不存在於 taxonomy 的情況由 E004 負責，這裡不重複報。
    """
    cat = entry.get("category")
    if not isinstance(cat, str):
        return
    if cat not in taxonomy.get("category", set()):
        return
    allowed = category_scope.get(cat, set())
    if domain not in allowed:
        errors["E008"].append(
            f"  file={rel} id={eid!r} category={cat!r} "
            f"用在 domain={domain!r}，但 scope 只容許 {sorted(allowed) or '（未宣告）'}"
        )


def check_file_categories(
    rel: str,
    data: dict,
    entry_lists: list[list],
    errors: dict[str, list[str]],
    warnings: dict[str, list[str]],
) -> None:
    """E009 / W010：條目 category 與該檔 categories 區塊必須互相涵蓋。

    my-site 的標籤字典是由各檔的 categories 區塊 merge 出來的
    （vortex-database.html 的 errCatName / techCatName / injCatName）。
    條目用了沒宣告的值，Hugo 的 index 查不到 key 會回空字串——分類標籤
    直接消失在頁面上，而且不會有任何錯誤。2026-07-26 實測有 10 張卡片
    正處於這個狀態，全靠 build 輸出比對才發現。E009 就是為了讓這件事
    在 canonical 端就爆掉。

    反向的 W010（宣告了但沒條目用）是死標籤：篩選 chip 點下去零結果。
    """
    declared = data.get("categories")
    if not isinstance(declared, list) or not declared:
        return
    keys = {
        c.get("key") or c.get("id")
        for c in declared if isinstance(c, dict)
    }
    keys.discard(None)

    used: set[str] = set()
    for entries in entry_lists:
        for e in entries:
            if isinstance(e, dict) and isinstance(e.get("category"), str):
                used.add(e["category"])

    for cat in sorted(used - keys):
        errors["E009"].append(
            f"  file={rel} category={cat!r} 未宣告於本檔 categories 區塊"
            f"（my-site 標籤會渲染成空字串）"
        )
    for cat in sorted(keys - used):
        warnings["W010"].append(
            f"  file={rel} category={cat!r} 已宣告但無任何條目使用（死標籤）"
        )


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
    """收集條目所有指出的 ID（供 W003 孤兒偵測用）。

    兩個來源：既有網域的 `links.*`，以及 movement 網域的關聯欄位。

    movement 那組是 2026-09-02 補的。原本 W003 只認 `links.*`，而
    movement 四個檔一個 `links` 都沒有——它用 `action_ids`／`demand_ids`／
    `derived_from_ids`／`muscle_roles[].muscle_id` 表達關聯。結果是 37 筆
    彼此密集互連的記錄被整層報成孤兒（528 筆裡的 34 筆），而「movement 是
    孤兒層、要補 cross_ref」這個結論其實是檢查器的視野缺口，不是內容缺口。
    """
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
    out |= collect_movement_relation_ids(entry)
    out |= collect_cross_ref_ids(entry)
    return out


def collect_cross_ref_ids(entry: dict) -> set[str]:
    """收集條目三層 `cross_ref_ids` 的目標（供 W003 孤兒偵測用）。

    2026-09-03 補。`cross_ref_ids` 是 S4c 定義的機器鍵，語意就是「這條指向
    那條」，但 W003 原本只認 `links.*` 與 movement 關聯欄位，於是被
    cross_ref 串起來的條目照樣被報成孤兒。這與 2026-09-02 補 movement 欄位
    是同一個視野缺口：孤兒名單長，不代表內容真的沒連起來，可能只是檢查器
    沒看那個欄位。

    層別清單與 validate() 主迴圈的 cross_ref 契約檢查一致，改一邊要改兩邊。
    """
    out: set[str] = set()
    containers = [entry]
    for layer in ("public", "diagnostic"):
        sub = entry.get(layer)
        if isinstance(sub, dict):
            containers.append(sub)
    for container in containers:
        value = container.get("cross_ref_ids")
        if isinstance(value, list):
            out.update(item for item in value if isinstance(item, str))
    return out


def collect_movement_relation_ids(entry: dict) -> set[str]:
    """收集 movement 條目的關聯目標 ID。

    `muscle_roles` 是 list[dict]，關聯鍵在 `muscle_id`；其餘三個是 list[str]。
    這些欄位的可解析性由 W014 負責，這裡只管「有沒有指出去」。
    """
    out: set[str] = set()
    for field in ("action_ids", "demand_ids", "derived_from_ids"):
        value = entry.get(field)
        if isinstance(value, list):
            out.update(item for item in value if isinstance(item, str))
    roles = entry.get("muscle_roles")
    if isinstance(roles, list):
        for role in roles:
            if isinstance(role, dict) and isinstance(role.get("muscle_id"), str):
                out.add(role["muscle_id"])
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
    W002  有 source/sources 顯示字串 + 缺 source_ids（**與 certainty 無關**）
    W009  certainty green/yellow + 完全沒有來源資訊

    走 iter_blocks()（任意深度），不是只看條目頂層——certainty 與 source 大多
    掛在 evidence[] / references[] / public.mechanism 這類巢狀區塊上。

    W002 自 S3a-2 起與 certainty 解耦：「這個區塊有沒有標確定性」跟「這個來源
    該不該被註冊」是兩件事，把檢查條件綁在 certainty 上是舊 W002 框架的殘留。
    W009 則仍綁 certainty——它問的是「宣稱有文獻依據卻拿不出任何來源」，
    語意本來就以確定性標記為前提。
    回傳值供呼叫端做 W008（孤兒來源）比對。
    """
    referenced: set[str] = set()
    for loc, eid, block, inherited in iter_blocks_with_source_inheritance(data):
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

        if raw_ids:
            continue

        cert = block.get("certainty")
        cert_label = {"\U0001F7E2": "green", "\U0001F7E1": "yellow"}.get(cert)

        # W002：有顯示字串就該有機器鍵，不看 certainty
        if has_display_source(block):
            field = display_source_field(block)
            suffix = f" certainty={cert_label}" if cert_label else " 無 certainty"
            warnings["W002"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"有 {field} 顯示字串但無 source_ids（{suffix.strip()}）"
            )
        # W009：宣稱 🟢/🟡 卻連顯示字串都沒有（仍以 certainty 為前提）。
        # 兩個豁免（S3b）：祖先區塊已帶來源＝粒度差不是缺口；
        # evidence_from 已宣告證據由子條目承擔＝綜述句的合法歸屬。
        elif cert in CERTAINTY_NEEDS_SOURCE:
            if inherited or has_evidence_from(block):
                continue
            warnings["W009"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"certainty={cert_label} 完全無來源資訊"
                f"（無 source/sources/citation，也無 source_ids，"
                f"祖先亦無，且未宣告 evidence_from）"
            )
    return referenced


# ── 教練觀測層契約（W011）與診斷層洩漏（E010）─────────────────────────────────

CERTAINTY_PRACTITIONER = "\U0001F7E0"  # LARGE ORANGE CIRCLE — 教練觀測

DIAGNOSTIC_KEYS = frozenset({
    "perception_probe",
    "signal_structure",
    "discriminators",
    "type_diagnosis",
    "type_diagnosis_note",
    "diagnosis_note",
    "diagnostic_protocols",
    "manipulation",
    "contrast_question",
    # movement 網域的被動／主動 ROM 測量、力量耐力測試、限制分類、教練決策樹與個別水中重測判讀必須擋在 public 外，避免診斷推理被公開站整包搬走。
    "passive_rom",
    "active_rom",
    "rom_measurement",
    "strength_endurance_test",
    "limitation_classification",
    "coach_decision_tree",
    "in_water_retest",
    "retest_reading",
})


def check_practitioner_blocks(rel: str, data: object, warnings: dict):
    """W011：certainty 🟠（教練觀測）但沒說出觀察基礎。

    🟠 是第一手實務證據，本來就不該被要求 source_ids（那會逼人去替教練觀察
    硬找文獻，也就是把自己的觀察包裝成別人的研究）。但「第一手」不等於
    「不用交代」——沒有 observation_basis 的 🟠 與「沒有依據」在資料上無法
    區分。observation_basis 要能回答：誰觀察的、在什麼族群/樣本上、
    這個判讀外推到哪裡為止。
    """
    for loc, eid, block in iter_blocks(data):
        if block.get("certainty") != CERTAINTY_PRACTITIONER:
            continue
        basis = block.get("observation_basis")
        if isinstance(basis, str) and basis.strip():
            continue
        if has_source_info(block):
            # 已經指了外部來源（例如引 Race Club 的影像觀察）→ 依據可追
            continue
        warnings["W011"].append(
            f"  file={rel} id={eid!r} at={loc} "
            f"certainty=orange 但缺 observation_basis（未交代觀察基礎與外推邊界）"
        )


def check_public_layer_leak(rel: str, data: object, errors: dict):
    """E010：診斷型鍵名出現在 public 子樹內。

    sync_vortex.py 對每個檔案都做 `rec.update(pub)`——白名單，整包搬 public。
    所以新增一個 diagnostic 同層鍵不會洩漏（不在白名單內就是不搬），
    真正會洩漏的只有一種寫法：把診斷判讀語寫進 public 裡面。
    黑名單也涵蓋 movement 的 ROM／力量耐力量測、限制分類、教練決策樹與
    個別水中重測判讀鍵名；這個檢查把所有這類洩漏路徑關掉。
    """
    def walk(node, path, in_public):
        if isinstance(node, dict):
            for k, v in node.items():
                child = f"{path}.{k}" if path else str(k)
                if in_public and k in DIAGNOSTIC_KEYS:
                    errors["E010"].append(
                        f"  file={rel} at={child} "
                        f"診斷型鍵 {k!r} 出現在 public 子樹內"
                        f"（sync 白名單會整包搬上公開站）"
                    )
                walk(v, child, in_public or k == "public")
        elif isinstance(node, list):
            for i, item in enumerate(node):
                walk(item, f"{path}[{i}]", in_public)

    walk(data, "", False)


# ── Movement 網域契約（W012–W015）────────────────────────────────────────────

def check_movement_id_names(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    expected_prefix: str,
    warnings: dict,
):
    """W012：movement 條目 ID 須符合檔案命名空間與穩定分段格式。

    每段只允許小寫字母起頭及小寫字母、數字、連字號；純數字段也禁止，
    避免把角度數字、證據等級或可變文案編進 ID，造成內容修正時被迫換 ID。
    """
    for index, entry in entries:
        eid = entry.get("id")
        loc = f"{entry_key}[{index}]"

        if not isinstance(eid, str) or not eid:
            warnings["W012"].append(
                f"  file={rel} id={eid!r} at={loc} movement ID 段格式違規："
                "ID 必須是非空字串"
            )
            continue

        if not eid.startswith(expected_prefix):
            warnings["W012"].append(
                f"  file={rel} id={eid!r} at={loc} movement ID 命名空間違規："
                f"預期前綴 {expected_prefix!r}"
            )

        invalid_segments = [
            segment for segment in eid.split(".")
            if segment.isdigit() or not _MOVEMENT_ID_SEGMENT_RE.fullmatch(segment)
        ]
        if invalid_segments:
            warnings["W012"].append(
                f"  file={rel} id={eid!r} at={loc} movement ID 段格式違規："
                f"不合法段={invalid_segments!r}（每段須符合 "
                "^[a-z][a-z0-9-]*$，且不得為純數字）"
            )


def check_movement_taxonomy(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    taxonomy: dict[str, set[str]],
    errors: dict,
):
    """E012：movement 任意層的七個受控欄位都必須存在於 taxonomy。

    原為 W013（WARN），2026-09-02 依 Step 21 決策升級成 ERROR。理由是
    這一組欄位**打錯字會 fail-open**，不是單純標籤漂移：
    `sync_vortex.py` 的 `MOVEMENT_HIDDEN_STATUS` 只擋 `draft`/`withheld`
    這兩個字面值，所以 `publication_status: publised` 不在擋單上，草稿
    直接上公開站。同理 `action_status` 打錯會讓 `do-not-prescribe` 失效、
    W016 的 evidence-gap 閘一起穿透。這與 E010（診斷層洩漏）同一個風險
    類別，維持 WARN 等於留一條靜默的發布漏洞。
    """
    for index, entry in entries:
        eid = entry.get("id", "(no id)")
        entry_loc = f"{entry_key}[{index}]"
        for loc, _nearest_id, block in iter_blocks(entry, entry_loc, str(eid)):
            for field in MOVEMENT_TAXONOMY_FIELDS:
                if field not in block:
                    continue
                value = block.get(field)
                allowed = taxonomy.get(field, set())
                if not isinstance(value, str) or value not in allowed:
                    errors["E012"].append(
                        f"  file={rel} id={eid!r} at={loc}.{field} "
                        f"{field}={value!r} 不在 taxonomy.{field}"
                    )


def check_movement_references(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    movement_id_set: set[str],
    canonical_id_set: set[str],
    warnings: dict,
):
    """W014：movement 跨檔引用須存在，且落在欄位指定的命名空間。

    先判斷目標是否存在；存在但前綴不符時另報「命名空間錯」，以區分
    一般斷鏈與「確實連到東西、但連錯 movement 層」的較隱蔽錯誤。
    derived_from_ids 是反向橋，判定條件相反：必須解析到 movement 以外的
    canonical ID。
    """
    for index, entry in entries:
        eid = entry.get("id", "(no id)")
        entry_loc = f"{entry_key}[{index}]"
        for loc, _nearest_id, block in iter_blocks(entry, entry_loc, str(eid)):
            for field, expected_prefix in MOVEMENT_REFERENCE_FIELDS.items():
                if field not in block:
                    continue
                raw_targets = block.get(field)
                if isinstance(raw_targets, str):
                    targets = [raw_targets]
                elif isinstance(raw_targets, list):
                    targets = [v for v in raw_targets if isinstance(v, str)]
                else:
                    continue

                for target in targets:
                    if target not in movement_id_set:
                        warnings["W014"].append(
                            f"  file={rel} id={eid!r} at={loc}.{field} "
                            f"{field}={target!r} 無法解析："
                            "目標 ID 不存在於 movement 檔案"
                        )
                    elif not target.startswith(expected_prefix):
                        warnings["W014"].append(
                            f"  file={rel} id={eid!r} at={loc}.{field} "
                            f"{field}={target!r} 命名空間錯：目標存在，但本欄位"
                            f"必須指向 {expected_prefix + '*'!r}"
                        )

            for field in MOVEMENT_EXTERNAL_REFERENCE_FIELDS:
                if field not in block:
                    continue
                raw_targets = block.get(field)
                if isinstance(raw_targets, str):
                    targets = [raw_targets]
                elif isinstance(raw_targets, list):
                    targets = [v for v in raw_targets if isinstance(v, str)]
                else:
                    continue

                for target in targets:
                    if target.startswith("movement."):
                        warnings["W014"].append(
                            f"  file={rel} id={eid!r} at={loc}.{field} "
                            f"{field}={target!r} 方向錯：本欄位是 movement 對"
                            "既有網域的來源橋，movement 內部連結請用 "
                            "action_ids／muscle_ids／demand_ids／intervention_ids"
                        )
                    elif target not in canonical_id_set:
                        warnings["W014"].append(
                            f"  file={rel} id={eid!r} at={loc}.{field} "
                            f"{field}={target!r} 無法解析："
                            "目標 ID 不存在於 canonical"
                        )


def check_movement_published_completeness(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    warnings: dict,
):
    """W015：published movement 條目須具備可發布的狀態與決策欄位。"""
    common_required = (
        "claim_status",
        "action_status",
        "evidence_profile",
    )
    # demand 是 movement 與既有 instructional 記錄唯一的接點：published 的
    # demand 若不指出它是從哪一筆技術記錄推出來的，這個網域就沒有回溯路徑。
    demand_required = ("derived_from_ids",)
    intervention_required = (
        "affirmative_conclusion",
        "works_when",
        "fails_when",
        "how_to_identify",
        "action",
        "remaining_boundary",
        "mobility_decision",
    )

    for index, entry in entries:
        if entry.get("publication_status") != "published":
            continue

        required = common_required
        if entry_key == "demands":
            required += demand_required
        if entry_key == "interventions":
            required += intervention_required

        missing = []
        for field in required:
            value = entry.get(field)
            filled = (
                isinstance(value, str) and bool(value.strip())
            ) or (
                isinstance(value, list) and bool(value)
            )
            if not filled:
                missing.append(field)

        # plan 尚未提供可機器判定「活動度記錄」的欄位，所以目前把
        # interventions.yaml 中所有 published 條目都視為必填 mobility_decision；
        # evidence-gap 永遠是誠實可用的值，不會逼作者編造。Step 13 pilot
        # 審查後重新檢討。
        if missing:
            eid = entry.get("id", "(no id)")
            warnings["W015"].append(
                f"  file={rel} id={eid!r} at={entry_key}[{index}] "
                "publication_status='published' 完整性不足："
                f"缺必填欄位 {', '.join(missing)}"
            )


def check_mobility_evidence_gap(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    warnings: dict,
):
    """W016：evidence-gap 必須真的沒有處方，不能只是換個標籤。

    evidence-gap 存在的理由是「不知道」與「不該做」是兩件事：not-routine 是
    一個主張（正常活動度或缺轉移證據，所以不常規拉伸），evidence-gap 是
    承認資料不足。但這個承認很容易被當成免責標籤——標了 evidence-gap，
    底下照樣寫出可照做的劑量。本檢查把兩個矛盾組合擋掉。
    """
    if entry_key != "interventions":
        return

    for index, entry in entries:
        if entry.get("mobility_decision") != "evidence-gap":
            continue

        eid = entry.get("id", "(no id)")
        loc = f"{entry_key}[{index}]"

        action_status = entry.get("action_status")
        if action_status != "do-not-prescribe":
            warnings["W016"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"mobility_decision='evidence-gap' 但 action_status="
                f"{action_status!r}：資料不足就不能標成可據以行動，"
                "應為 'do-not-prescribe'"
            )

        dosage = entry.get("dosage_source_ids")
        if isinstance(dosage, list) and dosage:
            warnings["W016"].append(
                f"  file={rel} id={eid!r} at={loc} "
                "mobility_decision='evidence-gap' 但 dosage_source_ids 非空："
                "有劑量來源就不是證據空白，請改標 conditional 或 not-routine"
            )


def check_movement_phase(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    phase_registry: dict[str, dict[str, str]],
    warnings: dict,
):
    """W017：demand 的 (stroke, phase) 須已登錄，且 phase_model 須與登錄一致。

    分期不是單一真相（BK-26 裁決：型 1 座標系衝突），數套分期各有來源並存。
    因此這裡擋的不是「用錯分期」，而是兩件會讓並存變成混亂的事：
    就地發明相位名，以及把同一個相位掛到另一套分期底下——後者會讓
    race-club-6phase 的 front-quadrant-propulsion 與 kudo-power-phase 的 pull
    看起來可以互換，而它們既不是同一段也不是同一個量。
    要新增相位一律先改 movement_phase_registry。
    """
    if entry_key != "demands":
        return

    for index, entry in entries:
        if "phase" not in entry:
            continue

        eid = entry.get("id", "(no id)")
        loc = f"{entry_key}[{index}]"
        stroke = entry.get("stroke")
        phase = entry.get("phase")

        known_phases = phase_registry.get(stroke) if isinstance(stroke, str) else None
        if known_phases is None:
            warnings["W017"].append(
                f"  file={rel} id={eid!r} at={loc} stroke={stroke!r} "
                "未登錄於 movement_phase_registry.strokes，無法判定相位合法性"
            )
            continue

        if phase not in known_phases:
            warnings["W017"].append(
                f"  file={rel} id={eid!r} at={loc} phase={phase!r} "
                f"不在 movement_phase_registry.strokes.{stroke}："
                "請先在登錄表新增相位，不要在 demand 端就地發明"
            )
            continue

        registered_model = known_phases[phase]
        declared_model = entry.get("phase_model")
        if declared_model != registered_model:
            warnings["W017"].append(
                f"  file={rel} id={eid!r} at={loc} "
                f"phase={phase!r} 登錄於 {registered_model!r}，"
                f"但本筆寫 phase_model={declared_model!r}："
                "相位不可跨分期系統搬運"
            )


def check_action_reference_frame(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    warnings: dict,
):
    """W018：demand 必須宣告 action_ids 的歸屬基準，且 joint-local 有自證義務。

    C 類 39 條蒐證裡命中最多次的結構性根因是「由可見空間量反推關節動作」
    （FR-40 的髖外展／內收、FR-44 的頸椎伸展、BF-36 的反向形式）。
    這些主張在 YAML 上與有量測的關節需求長得一模一樣，差別只在證據，
    所以必須讓基準顯性化才擋得住。

    joint-local 的代價是 source_ids 非空；唯一豁免是已標
    action_status: do-not-prescribe——那等於誠實宣告「這是待驗證候選」，
    與 W016 對 evidence-gap 的處理是同一個邏輯：不禁止承認不知道，
    只禁止不知道卻寫成可照做的需求。

    取值合法性由 E012 負責（本欄位已列入 MOVEMENT_TAXONOMY_FIELDS），
    這裡只管缺漏與自證義務。
    """
    if entry_key != "demands":
        return

    for index, entry in entries:
        eid = entry.get("id", "(no id)")
        loc = f"{entry_key}[{index}]"
        frame = entry.get("action_reference_frame")

        if frame is None:
            warnings["W018"].append(
                f"  file={rel} id={eid!r} at={loc} 缺 action_reference_frame："
                "demand 必須宣告 action_ids 是以關節、身體軸線還是池畔座標成立"
            )
            continue

        if frame != "joint-local":
            continue

        source_ids = entry.get("source_ids")
        has_source = isinstance(source_ids, list) and len(source_ids) > 0
        if has_source:
            continue

        if entry.get("action_status") == "do-not-prescribe":
            continue

        warnings["W018"].append(
            f"  file={rel} id={eid!r} at={loc} "
            "action_reference_frame='joint-local' 但 source_ids 為空："
            "關節動作需求要有分節段量測支撐，否則改標 body-fixed／"
            "poolside-fixed，或標 action_status: do-not-prescribe"
        )


def _iter_prose_strings(block: object):
    """遞迴取出區塊內所有字串值，供 W019 掃量化主張。"""
    if isinstance(block, str):
        yield block
    elif isinstance(block, dict):
        for value in block.values():
            yield from _iter_prose_strings(value)
    elif isinstance(block, list):
        for value in block:
            yield from _iter_prose_strings(value)


def check_measurement_conditions(
    rel: str,
    entry_key: str,
    entries: list[tuple[int, dict]],
    source_id_set: set,
    warnings: dict,
):
    """W019：demand 文字出現量化主張時，必須帶完整的 measurement_conditions。

    直接依據是 FR-44：同一個頭位操弄，手臂體側時 4–5.2%、雙臂過頭時
    10.4–10.9%，差距超過兩倍。決定量級的條件不在數字裡，在數字旁邊——
    靠行文自律留不住，所以改成結構欄位。

    掃描範圍刻意排除 measurement_conditions 本身（否則它自帶的 value 會
    觸發它自己）與 source_ids／id 這類機器鍵。
    """
    if entry_key != "demands":
        return

    for index, entry in entries:
        eid = entry.get("id", "(no id)")
        loc = f"{entry_key}[{index}]"

        scanned = {
            key: value for key, value in entry.items()
            if key not in ("measurement_conditions", "source_ids", "id")
        }
        matched = None
        for text in _iter_prose_strings(scanned):
            for pattern in MEASUREMENT_CLAIM_PATTERNS:
                found = pattern.search(text)
                if found:
                    matched = found.group(0).strip()
                    break
            if matched:
                break

        raw = entry.get("measurement_conditions")

        if matched and not isinstance(raw, list):
            warnings["W019"].append(
                f"  file={rel} id={eid!r} at={loc} 文字含量化主張 {matched!r} "
                "但缺 measurement_conditions：數值必須連同量測條件、終點與"
                "外推邊界一起寫，否則讀者會取到錯的量級"
            )
            continue

        if not isinstance(raw, list):
            continue

        if matched and not raw:
            warnings["W019"].append(
                f"  file={rel} id={eid!r} at={loc} 文字含量化主張 {matched!r} "
                "但 measurement_conditions 為空 list"
            )

        for cond_index, cond in enumerate(raw):
            cond_loc = f"{loc}.measurement_conditions[{cond_index}]"
            if not isinstance(cond, dict):
                warnings["W019"].append(
                    f"  file={rel} id={eid!r} at={cond_loc} "
                    "元素必須是 dict"
                )
                continue

            missing = [
                key for key in MEASUREMENT_CONDITION_SUBKEYS
                if not isinstance(cond.get(key), str) or not cond.get(key).strip()
            ]
            if missing:
                warnings["W019"].append(
                    f"  file={rel} id={eid!r} at={cond_loc} "
                    f"必填子鍵缺漏或為空：{missing!r}"
                )

            sid = cond.get("source_id")
            if isinstance(sid, str) and sid and sid not in source_id_set:
                warnings["W019"].append(
                    f"  file={rel} id={eid!r} at={cond_loc} "
                    f"source_id={sid!r} 不存在於 _sources.yaml"
                )


def check_evidence_from(
    rel: str, data: object, all_id_set: set, errors: dict
):
    """E011：evidence_from 內的 ID 必須可解析到全域 ID 集合。

    evidence_from 是 W009 的豁免路徑（「本句的證據由所列子條目承擔」）。
    若不驗證它指得到東西，它就變成零成本的免罪符——寫一個不存在的 ID
    也能讓警告消失。這條檢查是那個豁免的代價。
    """
    for loc, eid, block, _inherited in iter_blocks_with_source_inheritance(data):
        if "evidence_from" not in block:
            continue
        raw = block.get("evidence_from")
        if not isinstance(raw, list):
            errors["E011"].append(
                f"  file={rel} id={eid!r} at={loc} evidence_from "
                f"型別應為 list，實際為 {type(raw).__name__}"
            )
            continue
        for item in raw:
            if not (isinstance(item, str) and item.strip()):
                errors["E011"].append(
                    f"  file={rel} id={eid!r} at={loc} "
                    f"evidence_from 含非字串元素 {item!r}"
                )
            elif item not in all_id_set:
                errors["E011"].append(
                    f"  file={rel} id={eid!r} at={loc} "
                    f"evidence_from 含無法解析的 {item!r}"
                )


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
        phase_registry = load_phase_registry()
        category_scope = load_category_scope()
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
    all_id_set, canonical_id_set, drills_id_set = build_global_id_set()

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
        "E006": [], "E007": [], "E008": [], "E009": [], "E010": [],
        "E011": [], "E012": []
    }
    warnings: dict[str, list[str]] = {
        "W001": [], "W002": [], "W003": [], "W004": [], "W005": [],
        "W006": [], "W007": [], "W008": [], "W009": [], "W010": [],
        "W011": [], "W012": [], "W014": [], "W015": [],
        "W016": [], "W017": [], "W018": [], "W019": []
    }

    # ── W012–W019: movement 網域契約（只掃四個明列內容檔）──
    movement_documents: list[
        tuple[str, str, str, list[tuple[int, dict]]]
    ] = []
    movement_id_set: set[str] = set()
    for filename, (entry_key, expected_prefix) in MOVEMENT_FILE_RULES.items():
        path = MOVEMENT_DIR / filename
        try:
            data = load_yaml(path)
        except Exception as e:
            sys.stderr.write(f"[WARN] load error {path}: {e}\n")
            continue

        rel = str(path.relative_to(ROOT))
        raw_entries = data.get(entry_key) if isinstance(data, dict) else None
        entries = [
            (index, entry)
            for index, entry in enumerate(raw_entries)
            if isinstance(entry, dict)
        ] if isinstance(raw_entries, list) else []
        movement_documents.append((rel, entry_key, expected_prefix, entries))
        movement_id_set.update(
            entry["id"]
            for _index, entry in entries
            if isinstance(entry.get("id"), str)
        )

    for rel, entry_key, expected_prefix, entries in movement_documents:
        check_movement_id_names(
            rel, entry_key, entries, expected_prefix, warnings
        )
        check_movement_taxonomy(rel, entry_key, entries, taxonomy, errors)
        check_movement_references(
            rel, entry_key, entries, movement_id_set, canonical_id_set, warnings
        )
        check_movement_published_completeness(
            rel, entry_key, entries, warnings
        )
        check_mobility_evidence_gap(rel, entry_key, entries, warnings)
        check_movement_phase(
            rel, entry_key, entries, phase_registry, warnings
        )
        check_action_reference_frame(rel, entry_key, entries, warnings)
        check_measurement_conditions(
            rel, entry_key, entries, allowed_source_ids, warnings
        )

    # ── E001: 在已知條目陣列鍵中發現缺 id 的元素 ──
    for path in validate_files:
        try:
            data = load_yaml(path)
            rel = str(path.relative_to(ROOT))
            find_missing_id_in_lists(data, rel, errors["E001"])
        except Exception:
            pass

    # ── E009 / W010: 各檔 categories 區塊與條目 category 互相涵蓋 ──
    # Drills 一併納入：Drills/_categories.yaml 是 drills 標籤的真相源，
    # 但 drills_*.yaml 不在 validate_files（會誤觸 E001/W003），所以這裡
    # 用「宣告檔 + 條目檔」的組合單獨檢查。
    for path in validate_files:
        try:
            data = load_yaml(path)
            rel = str(path.relative_to(ROOT))
            if not isinstance(data, dict):
                continue
            entry_lists = [
                v for k, v in data.items()
                if k in KNOWN_ENTRY_LIST_KEYS and isinstance(v, list)
            ]
            check_file_categories(rel, data, entry_lists, errors, warnings)
        except Exception:
            pass

    try:
        drill_cats = load_yaml(DRILLS_DIR / "_categories.yaml")
        drill_entry_lists = []
        for path in sorted(DRILLS_DIR.glob("*.yaml")):
            if path.name.startswith("_"):
                continue
            d = load_yaml(path)
            if not isinstance(d, dict) or not isinstance(d.get("drills"), list):
                continue
            drill_entry_lists.append(d["drills"])
            # E004 / E008：drills 條目不在 validate_files 的逐條目迴圈裡，
            # 詞彙合法性與 scope 得在這裡自己跑一次，否則兩個檢查對 Drills
            # 完全是死碼（實測：把 health 的 A-shoulder-upper 塞進 drill
            # 條目，E008 靜默放行）。
            drel = str(path.relative_to(ROOT))
            for e in d["drills"]:
                if not isinstance(e, dict):
                    continue
                cat = e.get("category")
                if not isinstance(cat, str):
                    continue
                eid = e.get("id", "(no id)")
                if cat not in taxonomy.get("category", set()):
                    errors["E004"].append(
                        f"  file={drel} id={eid!r} category={cat!r}"
                    )
                    continue
                check_category_scope(
                    drel, eid, e, "drills", category_scope, taxonomy, errors
                )
        check_file_categories(
            "Drills/_categories.yaml", drill_cats, drill_entry_lists,
            errors, warnings,
        )
    except Exception as e:
        errors["E009"].append(f"  Drills/_categories.yaml 無法載入或比對: {e}")

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

        # ── movement 關聯欄位的入邊（W003 用）──
        # 與 links.* 分開累計：movement 不使用 links，斷鏈由 W014 管，
        # 這裡只要目標存在就算一次指入。
        for target in collect_movement_relation_ids(entry):
            if target in all_id_set:
                inbound_ids[target] += 1

        # ── cross_ref_ids 的入邊（W003 用）──
        # 斷鏈由 E006 管，這裡只要目標存在就算一次指入。
        for target in collect_cross_ref_ids(entry):
            if target in all_id_set:
                inbound_ids[target] += 1

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
        for field in ("category", "stroke", "certainty", "status", "joint_region"):
            val = entry.get(field)
            if val is not None and isinstance(val, str):
                allowed = taxonomy.get(field, set())
                if val not in allowed:
                    errors["E004"].append(
                        f"  file={rel} id={eid!r} {field}={val!r}"
                    )

        # ── E004: also_strokes（跨式適用宣告）逐值檢查 ──
        # 一張卡只有一份內容、一個歸屬泳式（stroke）；also_strokes 宣告它在哪些
        # 別式同樣成立，各式頁據此顯示同一張卡。自列本式會讓該頁畫出兩張。
        also = entry.get("also_strokes")
        if also is not None:
            allowed = taxonomy.get("stroke", set())
            if not isinstance(also, list):
                errors["E004"].append(
                    f"  file={rel} id={eid!r} also_strokes 須為 list，實際 {type(also).__name__}"
                )
            else:
                for v in also:
                    if v not in allowed:
                        errors["E004"].append(
                            f"  file={rel} id={eid!r} also_strokes 含未登錄泳式 {v!r}"
                        )
                    elif v == entry.get("stroke"):
                        errors["E004"].append(
                            f"  file={rel} id={eid!r} also_strokes 重複列出自身泳式 {v!r}"
                        )

        # ── E008: category 跨網域誤用 ──
        check_category_scope(
            rel, eid, entry, domain_of(rel), category_scope, taxonomy, errors
        )

        # ── E005: source_ids 斷鏈 ──
        # 已移到下方「逐區塊檢查」的遞迴走訪（source_ids 可出現在任意深度，
        # 只掃條目頂層會漏掉 evidence[] 上的 201 筆機器鍵）。

        # ── E006 / W001 / W006: cross_ref 契約（entry 頂層、public、diagnostic）──
        # diagnostic 層原本沒跑：2026-09-03 發現 stroke-demands 有一筆把 ID 陣列寫進
        # diagnostic.cross_ref（顯示用自由文字）而非 cross_ref_ids，驗證器完全看不到。
        # 診斷層的斷鏈不會外洩到公開站，但它同樣是給人跳轉用的鍵，一樣要能解析。
        check_cross_ref(rel, eid, entry, "entry", all_id_set, errors, warnings)
        for layer in ("public", "diagnostic"):
            sub = entry.get(layer)
            if isinstance(sub, dict):
                check_cross_ref(
                    rel, eid, sub, layer, all_id_set, errors, warnings
                )

    # ── 逐區塊檢查（E005 / W002 / W009）：遞迴走訪任意深度 ──
    # certainty 與 source/source_ids 多數不在條目頂層，而在 evidence[]、
    # references[]、public.mechanism 這類巢狀區塊上；per-entry 迴圈看不到。
    #
    # 掃描範圍另外加上 Drills/*.yaml：Drills 也有大量帶 source 的區塊，
    # 只把它們納入**來源契約**這一組檢查（E005/W002/W009），不併進
    # validate_files——後者會連帶把 E001/E004/W003/W005 等 canonical 專屬
    # 規則套到 Drills 上，那是另一個決策，不在 S3a-2 範圍。
    source_scan_files = validate_files + sorted(DRILLS_DIR.glob("*.yaml"))
    referenced_source_ids: set[str] = set()
    for path in source_scan_files:
        try:
            data = load_yaml(path)
        except Exception:
            continue
        rel = str(path.relative_to(ROOT))
        referenced_source_ids |= check_source_blocks(
            rel, data, allowed_source_ids, errors, warnings
        )
        # W011 / E010 與來源契約同一輪走訪範圍（含 Drills）：教練觀測與
        # 診斷層鍵名在 Drills 也可能出現。
        check_practitioner_blocks(rel, data, warnings)
        check_public_layer_leak(rel, data, errors)
        check_evidence_from(rel, data, all_id_set, errors)

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
    lines.append(f"> 生成日期：{date.today()}")
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
        # E008 / E009 / W010 自 S2 起就有檢查，但當時漏了登錄進 code_meta，
        # 於是即使有筆數也不會出現在報告裡（靜默的報告缺口）。S3b 補上。
        "E008": (
            "ERROR",
            "`category` 跨網域誤用：值合法但該值的 scope 不含本檔所屬網域",
        ),
        "E009": (
            "ERROR",
            "條目的 `category` 未宣告於該檔自己的 `categories` 區塊"
            "（my-site 查表落空 → 靜默渲染成空字串）",
        ),
        "E010": (
            "ERROR",
            "診斷層洩漏：既有與 movement 診斷型鍵名出現在 `public` 子樹內"
            "（`sync_vortex.py` 白名單會整包搬 public 上公開站）",
        ),
        "E011": (
            "ERROR",
            "`evidence_from` 含無法解析的 ID"
            "（它是 W009 的豁免路徑，不驗證就變成零成本免罪符）",
        ),
        "E012": (
            "ERROR",
            "movement 受控欄位值不在 `_taxonomy.yaml` 對應詞彙集合"
            "（原 W013，2026-09-02 升級：`publication_status` 等欄位拼錯會"
            "fail-open，`sync_vortex.py` 只擋 `draft`/`withheld` 字面值）",
        ),
        "W001": (
            "WARN",
            "`cross_ref` 內的疑似穩定 ID 未列入同層 `cross_ref_ids`",
        ),
        "W002": (
            "WARN",
            "區塊**有**來源顯示字串（`source`/`sources`）但缺 `source_ids`"
            "（機器鍵沒跟上顯示層）；S3a-2 起不看 `certainty`",
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
            "（無 `source`/`sources`/`citation`，也無 `source_ids`，祖先亦無，"
            "且未宣告 `evidence_from`）→ 需補來源或改確定性，S3b 範圍",
        ),
        "W010": (
            "WARN",
            "死標籤：`categories` 區塊宣告了某 key，但該檔沒有任何條目使用",
        ),
        "W011": (
            "WARN",
            "`certainty` orange（教練觀測）但缺 `observation_basis`"
            "（未交代觀察基礎與外推邊界）→ S6 範圍",
        ),
        "W012": (
            "WARN",
            "movement 條目 ID 的檔案命名空間或分段格式違規",
        ),
        "W014": (
            "WARN",
            "movement 跨檔引用無法解析，或目標存在但命名空間錯誤",
        ),
        "W015": (
            "WARN",
            "`published` movement 條目缺少狀態、證據或介入決策必填欄位",
        ),
        "W016": (
            "WARN",
            "`mobility_decision: evidence-gap` 的介入仍寫成可執行處方",
        ),
        "W017": (
            "WARN",
            "demand 的相位未登錄，或 phase_model 與 movement_phase_registry 不符",
        ),
        "W018": (
            "WARN",
            "demand 缺 `action_reference_frame`，或 `joint-local` 無分節段量測支撐",
        ),
        "W019": (
            "WARN",
            "demand 文字含量化主張但 `measurement_conditions` 缺漏或不完整",
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
                "> **契約說明（S3a／S3a-2）**：`source`（單數字串）與 `sources`"
                "（複數清單）都是顯示層自由文字，下游 my-site 直接渲染，"
                "**不可改寫、改名或改成陣列**；可解析的來源鍵放同區塊的 "
                "`source_ids`，指向 `canonical/_sources.yaml` 的 `src.<slug>`。"
                "W002 自 S3a-2 起**與 `certainty` 解耦**：一個區塊只要帶了來源"
                "顯示字串，不論有沒有標確定性，那個來源都該進註冊表、都該有"
                "`source_ids` 指過去。掃描範圍也含 `Drills/*.yaml`。"
                "W009 仍綁 `certainty`——它問的是「標了 🟢/🟡 卻拿不出任何來源」，"
                "語意本來就以確定性標記為前提。"
                "兩者差別在**有沒有來源顯示資訊**：W002 已經有字串，只差把它"
                "登錄成來源條目再補機器鍵（純遷移）；W009 連顯示字串都沒有，"
                "得回頭找出主張的依據（S3b，不能靠遷移解決）。"
                "兩者不可互相代替，也不可用佔位來源填掉 W009。"
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
