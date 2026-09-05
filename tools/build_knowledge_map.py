#!/usr/bin/env python3
"""
build_knowledge_map.py — 掃 canonical/ + Drills/，生成 KNOWLEDGE_MAP.md

用途：
  - 給 LLM 與人類一個全內容的 TOC，避免每次都摸石頭過河
  - 顯示每條目的 id / 標題 / 確定性 / 適用泳式
  - 可掃出 🟡/🔴 多的條目作為「該更新」候選

跑法：
  python tools/build_knowledge_map.py

輸出：
  KNOWLEDGE_MAP.md（覆寫）

CI 整合：
  push 到 master 前自動跑一次（或加入 pre-commit hook）。
"""
from __future__ import annotations

import sys
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

from textfold import unfold_cjk

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "KNOWLEDGE_MAP.md"

CERT_LEGEND = "🔵 推導 / 🟢 近期文獻 / 🟡 舊文獻 / 🟠 教練觀測 / 🔴 待查"

# ── 萃取器：每種 canonical 檔型一個 extractor ──

def _cert_from(d, *keys):
    """從 dict 樹路徑中找 certainty 標記"""
    for k in keys:
        if not isinstance(d, dict):
            return ""
        d = d.get(k, {})
    if isinstance(d, str):
        return d
    return ""

def extract_technical_analysis(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for p in data.get("points", []) or []:
        pub = p.get("public", {}) or {}
        rows.append({
            "id": p.get("id", "?"),
            "stroke": p.get("stroke", ""),
            "category": p.get("category", ""),
            "title": pub.get("title", ""),
            "cert": _cert_from(pub, "mechanism", "certainty"),
        })
    return rows

def extract_teaching_errors(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for e in data.get("errors", []) or []:
        pub = e.get("public", {}) or {}
        rows.append({
            "id": e.get("id", "?"),
            "stroke": e.get("stroke", ""),
            "category": e.get("category", ""),
            "title": pub.get("title") or pub.get("summary", "")[:60],
            "cert": _cert_from(pub, "mechanism", "certainty"),
        })
    return rows

def extract_l_indicators(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for e in data.get("indicators", []) or []:
        pub = e.get("public", {}) or {}
        rows.append({
            "id": e.get("id", "?"),
            "stroke": e.get("stroke", ""),
            "level": e.get("level", ""),
            "aspect": e.get("aspect", ""),
            "title": pub.get("indicator", "")[:80],
        })
    return rows

def extract_water_sense_levels(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for l in data.get("levels", []) or []:
        pub = l.get("public", {}) or {}
        rows.append({
            "id": l.get("id", "?"),
            "stroke": l.get("stroke", ""),
            "level": l.get("level", ""),
            "title": pub.get("tagline") or pub.get("summary", "")[:80],
        })
    return rows

def extract_adm_matrix(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for c in data.get("cells", []) or []:
        pub = c.get("public", {}) or {}
        rows.append({
            "id": c.get("id", "?"),
            "pillar": c.get("pillar", ""),
            "stage": c.get("stage", ""),
            "title": pub.get("summary", "")[:80],
        })
    return rows

def extract_technical_standards(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for s in data.get("standards", []) or []:
        pub = s.get("public", {}) or {}
        rows.append({
            "id": s.get("id", "?"),
            "title": pub.get("title", ""),
            "applies_from": pub.get("applies_from", ""),
        })
    return rows

def extract_periodization(path: Path):
    """週期化檔——top-level 各 dict 一個條目"""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    SKIP = {"domain", "sub", "schema_version", "source_repos", "certainty_legend", "evidence_grade_legend"}
    for key, val in data.items():
        if key in SKIP:
            continue
        if not isinstance(val, dict):
            continue
        rows.append({
            "id": val.get("id", key),
            "section": key,
            "cert": val.get("cert", ""),
            "title": (val.get("premise_zh") or val.get("plain_zh") or val.get("text_zh") or "")[:90],
        })
    return rows

def extract_psychology(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for t in data.get("themes", []) or []:
        rows.append({
            "id": t.get("id", "?"),
            "name_zh": t.get("name_zh", ""),
            "status": t.get("status", ""),
            "concept_count": t.get("concept_count", "?"),
            "l_band": t.get("l_band", ""),
            "when_zh": t.get("when_zh", "")[:60],
        })
    return rows

def extract_breathing(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    SKIP = {"domain", "sub", "schema_version"}
    for key, val in data.items():
        if key in SKIP:
            continue
        if not isinstance(val, dict):
            continue
        # 各節的第一段敘述欄位命名不一（premise_zh / danger_zh / what_zh / why_zh…），
        # 固定順序取不到時退回該節第一個 *_zh 字串，避免摘要留空
        title = val.get("premise_zh") or val.get("plain_zh") or ""
        if not title:
            title = next((v for k, v in val.items()
                          if k.endswith("_zh") and isinstance(v, str)), "")
        rows.append({
            "id": val.get("id", key),
            "section": key,
            "cert": val.get("cert", ""),
            "title": title[:90],
        })
    return rows

def extract_injuries_built(path: Path):
    """injuries.yaml（built artifact）—— 列出每個傷害條目"""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for cat in data.get("categories", []) or []:
        cat_id = cat.get("id", "")
        for inj in data.get("injuries", []) or []:
            if inj.get("category") != cat_id:
                continue
            rows.append({
                "id": inj.get("id", "?"),
                "category": cat_id,
                "category_zh": cat.get("zh", ""),
                "zh": inj.get("zh", ""),
                "en": inj.get("en", ""),
                "cert": (inj.get("epidemiology") or {}).get("certainty", "") if isinstance(inj.get("epidemiology"), dict) else "",
            })
    return rows

def extract_movement(path: Path, list_key: str):
    """canonical/movement/ 四個檔共用。各檔欄位不同，共通的只有 id / name / 三個狀態欄。"""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for r in data.get(list_key, []) or []:
        pub = r.get("public") or {}
        rows.append({
            "id": r.get("id", "?"),
            "name": r.get("name") or pub.get("name_zh", ""),
            "name_zh": pub.get("name_zh", ""),
            "joint_region": r.get("joint_region") or ", ".join(r.get("joint_regions") or []),
            "stroke": r.get("stroke", ""),
            "phase": r.get("phase", ""),
            "phase_model": r.get("phase_model", ""),
            "limitation_type": r.get("limitation_type", ""),
            "claim_status": r.get("claim_status", ""),
            "action_status": r.get("action_status", ""),
            "evidence_profile": r.get("evidence_profile", ""),
            "publication_status": r.get("publication_status", ""),
            "desc": (pub.get("description") or "").strip().replace("\n", " ")[:70],
        })
    return rows


def movement_coverage(taxonomy_path: Path, demands: list[dict]):
    """相位覆蓋率。分母取 _taxonomy.yaml 的 registry（canonical），
    不取 plans/movement_coverage_denominator.yaml——後者是規劃檔且已知落後
    （free.early-pull-through 有 demand 卻沒登錄進去）。以 registry 為準才會
    讓分母落差自己浮出來。"""
    reg = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))["movement_phase_registry"]["strokes"]
    covered = {(d["stroke"], d["phase"]) for d in demands}
    rows = []
    for stroke, phases in reg.items():
        miss = [p for p in phases if (stroke, p["key"]) not in covered]
        rows.append({
            "stroke": STROKE_ZH.get(stroke, stroke),
            "covered": f"{len(phases) - len(miss)}/{len(phases)}",
            "models": ", ".join(sorted({p["phase_model"] for p in phases})),
            "missing": ", ".join(f'{p["key"]}（{p["label_zh"]}）' for p in miss) or "—",
        })
    total = sum(len(p) for p in reg.values())
    return rows, total - sum(int(r["covered"].split("/")[0]) for r in rows), total


def extract_drills(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rows = []
    for d in data.get("drills", []) or []:
        rows.append({
            "id": d.get("id", "?"),
            "name_zh": d.get("name_zh", ""),
            "category": d.get("category", ""),
            "l_target": " ".join(d.get("l_target", []) or []),
            "difficulty_tier": d.get("difficulty_tier", ""),
            "strokes": " ".join(d.get("strokes", []) or []),
        })
    return rows


# ── 渲染：各檔型一個 renderer ──

STROKE_ZH = {"free": "自由式", "back": "仰式", "breast": "蛙式", "fly": "蝶式",
             "starts-turns": "起跳轉身", "udk": "水下蝶腳"}
PILLAR_ZH = {"physical": "體能", "technical": "技術戰術", "mental": "心理", "life": "生活技能"}
STAGE_ZH = {"l2t": "L2T 學習訓練", "t2t": "T2T 訓練為訓練", "t2c": "T2C 訓練為競賽", "t2w": "T2W 訓練為勝利"}


def render_table(rows: list[dict], cols: list[tuple[str, str]]) -> list[str]:
    """rows + cols=[(col_key, header)] → markdown table 行列表"""
    if not rows:
        return ["（無）"]
    lines = []
    lines.append("| " + " | ".join(h for _, h in cols) + " |")
    lines.append("|" + "|".join("---" for _ in cols) + "|")
    for r in rows:
        lines.append("| " + " | ".join(str(r.get(k, "")) for k, _ in cols) + " |")
    return lines


def stats_by(rows: list[dict], key: str) -> Counter:
    c = Counter()
    for r in rows:
        v = r.get(key, "") or "?"
        c[v] += 1
    return c


# ── 主流程 ──

def main():
    lines = []
    lines.append(f"# Vortex 知識地圖 KNOWLEDGE MAP")
    lines.append("")
    lines.append(f"> 自動生成於 {date.today()} by `tools/build_knowledge_map.py`。重跑：`python tools/build_knowledge_map.py`")
    lines.append(f"> 確定性圖例：{CERT_LEGEND}")
    lines.append("")
    lines.append("這份地圖是查內容、找缺口、看哪些條目該更新的單一入口。")
    lines.append("- **想加新內容前**：先掃對應章節，看是否已有重複或相近條目")
    lines.append("- **想更新舊內容時**：濾出 🟡/🔴 的條目作為優先候選")
    lines.append("- **想做新舊觀念對比時**：用 ID 去 grep canonical/ 取得完整內容")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 摘要")
    lines.append("")

    summary_rows = []  # 每章節一行統計

    # === 教學層 instructional ===
    lines.append("---")
    lines.append("")
    lines.append("## 教學層 `canonical/instructional/`")
    lines.append("")

    # technical-analysis
    ta = extract_technical_analysis(ROOT / "canonical/instructional/technical-analysis.yaml")
    by_stroke = stats_by(ta, "stroke")
    by_cert = stats_by(ta, "cert")
    summary_rows.append(("technical-analysis", len(ta), f"泳式分布：{dict(by_stroke)}；確定性：{dict(by_cert)}"))

    lines.append(f"### `technical-analysis.yaml` — 技術分析（**{len(ta)} 條目**）")
    lines.append("")
    lines.append(f"**泳式分布**：{', '.join(f'{STROKE_ZH.get(k,k)} {v}' for k,v in sorted(by_stroke.items()))}")
    lines.append("")
    for stroke in ["free", "back", "breast", "fly", "starts-turns", "udk", ""]:
        rows = [r for r in ta if r["stroke"] == stroke]
        if not rows:
            continue
        sname = STROKE_ZH.get(stroke, stroke or "（未分類）")
        lines.append(f"#### {sname} ({len(rows)})")
        lines.append("")
        lines.extend(render_table(rows, [("id", "ID"), ("category", "範疇"), ("title", "標題"), ("cert", "確定性")]))
        lines.append("")

    # teaching-errors
    te = extract_teaching_errors(ROOT / "canonical/instructional/teaching-errors.yaml")
    by_stroke_te = stats_by(te, "stroke")
    summary_rows.append(("teaching-errors", len(te), f"泳式分布：{dict(by_stroke_te)}"))

    lines.append(f"### `teaching-errors.yaml` — 教學誤區（**{len(te)} 條目**）")
    lines.append("")
    lines.append(f"**泳式分布**：{', '.join(f'{STROKE_ZH.get(k,k)} {v}' for k,v in sorted(by_stroke_te.items()))}")
    lines.append("")
    for stroke in ["free", "back", "breast", "fly", "starts-turns", "udk", ""]:
        rows = [r for r in te if r["stroke"] == stroke]
        if not rows:
            continue
        sname = STROKE_ZH.get(stroke, stroke or "（未分類）")
        lines.append(f"#### {sname} ({len(rows)})")
        lines.append("")
        lines.extend(render_table(rows, [("id", "ID"), ("category", "範疇"), ("title", "標題/摘要")]))
        lines.append("")

    # === 感知層 technica ===
    lines.append("---")
    lines.append("")
    lines.append("## 感知層 `canonical/technica/`")
    lines.append("")

    li = extract_l_indicators(ROOT / "canonical/technica/l-indicators.yaml")
    summary_rows.append(("l-indicators", len(li), "L0–L6 各泳式感知指標"))
    lines.append(f"### `l-indicators.yaml` — L 級指標（**{len(li)} 條目**）")
    lines.append("")
    lines.extend(render_table(li, [("id", "ID"), ("stroke", "泳式"), ("level", "L"), ("aspect", "面向"), ("title", "指標")]))
    lines.append("")

    wsl = extract_water_sense_levels(ROOT / "canonical/technica/water-sense-levels.yaml")
    summary_rows.append(("water-sense-levels", len(wsl), "26 個感知級別"))
    lines.append(f"### `water-sense-levels.yaml` — 水感層級（**{len(wsl)} 條目**）")
    lines.append("")
    lines.extend(render_table(wsl, [("id", "ID"), ("stroke", "泳式"), ("level", "L"), ("title", "tagline/摘要")]))
    lines.append("")

    # === 發展層 development ===
    lines.append("---")
    lines.append("")
    lines.append("## 發展層 `canonical/development/`")
    lines.append("")

    matrix = extract_adm_matrix(ROOT / "canonical/development/matrix.yaml")
    summary_rows.append(("development/matrix", len(matrix), "ADM 4 支柱 × 4 階段 = 16 格"))
    lines.append(f"### `matrix.yaml` — ADM 4×4 發展矩陣（**{len(matrix)} 格**）")
    lines.append("")
    lines.extend(render_table(matrix, [("id", "ID"), ("pillar", "支柱"), ("stage", "階段"), ("title", "摘要")]))
    lines.append("")

    stds = extract_technical_standards(ROOT / "canonical/development/technical-standards.yaml")
    summary_rows.append(("development/technical-standards", len(stds), "技術基準"))
    lines.append(f"### `technical-standards.yaml` — 技術基準（**{len(stds)} 條目**）")
    lines.append("")
    lines.extend(render_table(stds, [("id", "ID"), ("applies_from", "起始階段"), ("title", "標題")]))
    lines.append("")

    # === 週期化 periodization ===
    lines.append("---")
    lines.append("")
    lines.append("## 週期化 `canonical/periodization/`")
    lines.append("")
    for fname in ["structure", "taper", "zones", "dryland", "_index"]:
        path = ROOT / f"canonical/periodization/{fname}.yaml"
        if not path.exists():
            continue
        rows = extract_periodization(path)
        summary_rows.append((f"periodization/{fname}", len(rows), "各節點"))
        lines.append(f"### `{fname}.yaml` （**{len(rows)} 節點**）")
        lines.append("")
        lines.extend(render_table(rows, [("id", "ID"), ("cert", "確定性"), ("title", "premise/摘要")]))
        lines.append("")

    # === 呼吸 breathing ===
    lines.append("---")
    lines.append("")
    lines.append("## 呼吸 `canonical/breathing/`")
    lines.append("")
    # safety 置頂：缺氧昏迷是讀其他節點的前提，不是並列主題之一
    for fname in ["safety", "framework", "physiology", "training", "regulation"]:
        path = ROOT / f"canonical/breathing/{fname}.yaml"
        if not path.exists():
            continue
        rows = extract_breathing(path)
        summary_rows.append((f"breathing/{fname}", len(rows), "各節點"))
        lines.append(f"### `{fname}.yaml` （**{len(rows)} 節點**）")
        lines.append("")
        lines.extend(render_table(rows, [("id", "ID"), ("cert", "確定性"), ("title", "premise/摘要")]))
        lines.append("")

    # === 健康 health ===
    lines.append("---")
    lines.append("")
    lines.append("## 健康 `canonical/health/`")
    lines.append("")

    inj_path = ROOT / "canonical/health/injuries.yaml"
    if inj_path.exists():
        inj = extract_injuries_built(inj_path)
        summary_rows.append(("health/injuries (built)", len(inj), "從 drafts/ build 出"))
        lines.append(f"### `injuries.yaml` — 已 build 之傷害條目（**{len(inj)} 條目**，來源 `drafts/`）")
        lines.append("")
        for cat in ["A-shoulder-upper", "B-lower-spine-strokespecific", "C-nonMSK-medical",
                    "D-systemic-acute", "D-endocrine", "E-acute-trauma", "F-pediatric-growth"]:
            rows = [r for r in inj if r["category"] == cat]
            if not rows:
                continue
            cat_zh = rows[0]["category_zh"]
            lines.append(f"#### {cat_zh} ({cat}, {len(rows)})")
            lines.append("")
            lines.extend(render_table(rows, [("id", "ID"), ("zh", "中文名"), ("en", "英文名"), ("cert", "流病確定性")]))
            lines.append("")

    # === 心理 psychology ===
    lines.append("---")
    lines.append("")
    lines.append("## 心理 `canonical/psychology/`")
    lines.append("")

    psy = extract_psychology(ROOT / "canonical/psychology/psychology.yaml")
    total_concepts = sum(int(p["concept_count"]) if str(p["concept_count"]).isdigit() else 0 for p in psy)
    summary_rows.append(("psychology", len(psy), f"{len(psy)} themes / 共 {total_concepts} concepts"))
    lines.append(f"### `psychology.yaml` — 心理（**{len(psy)} themes / {total_concepts} concepts**）")
    lines.append("")
    lines.extend(render_table(psy, [("id", "ID"), ("name_zh", "主題"), ("status", "狀態"),
                                    ("concept_count", "概念數"), ("l_band", "L 範圍"), ("when_zh", "使用情境")]))
    lines.append("")

    # === 動作圖譜 movement ===
    mv_dir = ROOT / "canonical/movement"
    if mv_dir.exists():
        lines.append("---")
        lines.append("")
        lines.append("## 動作圖譜 `canonical/movement/`")
        lines.append("")
        lines.append("列舉式圖譜：列出「這個相位牽涉到什麼」與「可能的狀況有哪些」，"
                     "不判定誰主導、不判定某泳者被什麼限制、不規定練到幾度。")
        lines.append("")

        acts = extract_movement(mv_dir / "actions.yaml", "actions")
        musc = extract_movement(mv_dir / "muscle-groups.yaml", "muscle_groups")
        dems = extract_movement(mv_dir / "stroke-demands.yaml", "demands")
        itvs = extract_movement(mv_dir / "interventions.yaml", "interventions")

        cov_rows, n_missing, n_total = movement_coverage(ROOT / "canonical/_taxonomy.yaml", dems)
        n_cov = n_total - n_missing
        summary_rows.append(("movement", len(acts) + len(musc) + len(dems) + len(itvs),
                             f"actions {len(acts)} / muscle-groups {len(musc)} / "
                             f"demands {len(dems)} / interventions {len(itvs)}；相位覆蓋 {n_cov}/{n_total}"))

        lines.append(f"### 相位覆蓋（**{n_cov}/{n_total}**）")
        lines.append("")
        lines.append("未覆蓋的相位分兩類：**已有裁決待撰寫**（照既有規格可直接落 demand）與"
                     "**無裁決授權**（不得憑空補）。動手前先去 `plans/關節主張裁決_*.md` 判性質。")
        lines.append("")
        lines.extend(render_table(cov_rows, [("stroke", "泳式"), ("covered", "覆蓋"),
                                             ("models", "分期系統"), ("missing", "未覆蓋相位")]))
        lines.append("")

        lines.append(f"### `actions.yaml` — 解剖動作（**{len(acts)} 條目**）")
        lines.append("")
        lines.extend(render_table(acts, [("id", "ID"), ("name", "名稱"), ("joint_region", "部位"),
                                         ("claim_status", "主張狀態"), ("action_status", "行動狀態")]))
        lines.append("")

        lines.append(f"### `muscle-groups.yaml` — 肌群（**{len(musc)} 條目**）")
        lines.append("")
        lines.extend(render_table(musc, [("id", "ID"), ("name", "名稱"), ("joint_region", "部位"),
                                         ("claim_status", "主張狀態"), ("action_status", "行動狀態")]))
        lines.append("")

        lines.append(f"### `stroke-demands.yaml` — 泳式需求（**{len(dems)} 條目**）")
        lines.append("")
        lines.append("**相位名綁 `phase_model`，跨分期系統不可互換也不可換算**（BK-26）。")
        lines.append("")
        for stroke in ["free", "back", "breast", "fly", "starts-turns", "udk", ""]:
            rows = [r for r in dems if r["stroke"] == stroke]
            if not rows:
                continue
            lines.append(f"#### {STROKE_ZH.get(stroke, stroke or '（未分類）')} ({len(rows)})")
            lines.append("")
            lines.extend(render_table(rows, [("id", "ID"), ("phase", "相位"), ("phase_model", "分期系統"),
                                             ("name_zh", "名稱"), ("claim_status", "主張狀態"),
                                             ("action_status", "行動狀態")]))
            lines.append("")

        lines.append(f"### `interventions.yaml` — 條件式訓練與活動度（**{len(itvs)} 條目**）")
        lines.append("")
        lines.extend(render_table(itvs, [("id", "ID"), ("name_zh", "名稱"), ("limitation_type", "限制類型"),
                                         ("claim_status", "主張狀態"), ("action_status", "行動狀態")]))
        lines.append("")

    # === 練習 Drills ===
    lines.append("---")
    lines.append("")
    lines.append("## 練習 `Drills/`")
    lines.append("")
    total_drills = 0
    for stroke in ["freestyle", "backstroke", "breaststroke", "butterfly", "sculling", "starts-turns", "udk"]:
        path = ROOT / f"Drills/drills_{stroke}.yaml"
        if not path.exists():
            continue
        rows = extract_drills(path)
        total_drills += len(rows)
        by_tier = stats_by(rows, "difficulty_tier")
        lines.append(f"### `drills_{stroke}.yaml` — {stroke} (**{len(rows)} drills**)")
        lines.append("")
        lines.append(f"**難度分布**：{dict(by_tier)}")
        lines.append("")
        lines.extend(render_table(rows, [("id", "ID"), ("name_zh", "中文名"),
                                         ("category", "類別"), ("l_target", "L 目標"),
                                         ("difficulty_tier", "難度"), ("strokes", "適用泳式")]))
        lines.append("")
    summary_rows.append(("Drills (7 files)", total_drills, "176 drill 含 9 軸 fingerprint"))

    # === 把摘要插回最前面 ===
    summary_lines = ["| 章節 | 條目數 | 備註 |", "|---|---|---|"]
    for sec, n, note in summary_rows:
        summary_lines.append(f"| `{sec}` | {n} | {note} |")

    # 找到 "## 摘要" 之後的空白行，插入 summary_lines
    insert_idx = None
    for i, l in enumerate(lines):
        if l == "## 摘要":
            insert_idx = i + 2  # 跳過空白行
            break
    if insert_idx is not None:
        lines = lines[:insert_idx] + summary_lines + [""] + lines[insert_idx:]

    # 全檔唯一的輸出口。canonical 的 `>-` 折點會被 YAML 接成空白，中文因此在句
    # 子中間長出空格；不接掉的話跨折點的片語在地圖裡 grep 不到。
    OUT.write_text(unfold_cjk("\n".join(lines)), encoding="utf-8")
    print(f"已寫入 {OUT.relative_to(ROOT)}（{len(lines)} 行）")
    print(f"摘要：")
    for sec, n, _ in summary_rows:
        print(f"  {sec}: {n}")


if __name__ == "__main__":
    main()
