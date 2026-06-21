# -*- coding: utf-8 -*-
"""
build_injuries.py — 把 canonical/health/drafts/*.yaml 提升整合成
單一 canonical/health/injuries.yaml（promoted artifact）。

職責：
  1. 載入所有草稿（_meta-reference 另存 meta_references，不列為傷害）
  2. 正規化 schema 漂移（scalar→list、stroke_phase→trigger_phase、補 who 鍵）
  3. 一致性稽核：必填欄位、未知 category、重複 id、潛在內容重疊
  4. 依 category 順序 + id 排序，輸出單檔 injuries.yaml
  5. 印稽核報告（drift 修正、異常、pending_verification 統計）

不發明任何內容；只搬運 + 正規化。drafts/ 仍是真相來源。
"""
import glob
import os
import sys
import yaml

HEALTH = os.path.join(os.path.dirname(__file__), "..", "canonical", "health")
DRAFTS = os.path.join(HEALTH, "drafts")
OUT = os.path.join(HEALTH, "injuries.yaml")

# category 顯示順序 + 中文標籤（渲染排序依此）
CATEGORY_ORDER = [
    ("A-shoulder-upper", "肩部與上肢"),
    ("B-lower-spine-strokespecific", "腰椎與泳式特異"),
    ("C-nonMSK-medical", "非肌骨醫療"),
    ("D-systemic-acute", "全身急性"),
    ("D-endocrine", "內分泌與骨骼"),
    ("E-acute-trauma", "急性外傷"),
    ("F-pediatric-growth", "兒童生長"),
]
CAT_RANK = {c: i for i, (c, _) in enumerate(CATEGORY_ORDER)}
KNOWN_CATS = set(CAT_RANK) | {"_meta-reference"}

REQUIRED_TOP = ["id", "zh", "en", "category", "environment",
                "sport_variant", "layer", "mechanism", "epidemiology"]


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def normalize(rec, drift):
    """就地正規化漂移欄位，記錄修正到 drift。回傳 rec。"""
    bn = rec.get("id")
    for key in ("environment", "sport_variant", "layer"):
        if key in rec and isinstance(rec[key], str):
            rec[key] = [rec[key]]
            drift.append(f"{bn}: {key} scalar→list")
    m = rec.get("mechanism") or {}
    if "stroke_phase" in m and "trigger_phase" not in m:
        m["trigger_phase"] = m.pop("stroke_phase")
        drift.append(f"{bn}: mechanism.stroke_phase→trigger_phase")
    if "who" not in m:
        m["who"] = None
        drift.append(f"{bn}: mechanism.who 補空鍵")
    rec["mechanism"] = m
    return rec


def main():
    files = sorted(glob.glob(os.path.join(DRAFTS, "*.yaml")))
    injuries, metas = [], []
    drift, anomalies = [], []
    ids = {}
    pending_total = 0

    for f in files:
        rec = yaml.safe_load(open(f, encoding="utf-8"))
        bn = os.path.basename(f)
        cat = rec.get("category", "?")
        rid = rec.get("id")

        if cat not in KNOWN_CATS:
            anomalies.append(f"{bn}: 未知 category '{cat}'")
        ids.setdefault(rid, []).append(bn)
        if cat != "_meta-reference":
            for k in REQUIRED_TOP:
                if k not in rec:
                    anomalies.append(f"{bn}: 缺必填欄位 '{k}'")

        rec = normalize(rec, drift)
        pending_total += len((rec.get("flags") or {}).get("pending_verification") or [])

        if cat == "_meta-reference":
            metas.append(rec)
        else:
            injuries.append(rec)

    for rid, locs in ids.items():
        if len(locs) > 1:
            anomalies.append(f"重複 id '{rid}': {locs}")

    injuries.sort(key=lambda r: (CAT_RANK.get(r.get("category"), 99),
                                 r.get("id") or ""))

    out_data = {
        "domain": "health",
        "sub": "injuries",
        "schema_version": 2,
        "note": "Promoted artifact，由 tools/build_injuries.py 從 drafts/ 整合產生；勿手改，改 drafts/ 後重跑。",
        "certainty_legend": "🔵推導 🟢近期文獻 🟡舊文獻 🟠教練觀測 🔴待查",
        "evidence_grade_legend": "A=RCT/SR B=cohort C=case-series Expert=共識（與 certainty 點獨立）",
        "categories": [{"id": c, "zh": z} for c, z in CATEGORY_ORDER],
        "meta_references": metas,
        "injuries": injuries,
    }

    # 稽核報告
    print("=" * 60)
    print(f"傷害草稿整合稽核  共 {len(files)} 檔")
    print("=" * 60)
    by_cat = {}
    for r in injuries:
        by_cat[r["category"]] = by_cat.get(r["category"], 0) + 1
    print(f"\n傷害條目 {len(injuries)} 條：")
    for c, _ in CATEGORY_ORDER:
        print(f"  {c:32s} {by_cat.get(c, 0)}")
    print(f"  meta_references                  {len(metas)}")

    print(f"\nSchema 漂移修正 {len(drift)} 處：")
    for d in drift:
        print(f"  - {d}")

    print(f"\npending_verification 旗標總數：{pending_total}")

    print(f"\n異常 {len(anomalies)} 處：")
    if anomalies:
        for a in anomalies:
            print(f"  ! {a}")
    else:
        print("  （無）")

    if "--dry-run" in sys.argv:
        print("\n[dry-run，未寫入 injuries.yaml]")
        return 1 if anomalies else 0

    out = yaml.safe_dump(out_data, allow_unicode=True,
                         default_flow_style=False, sort_keys=False, width=4096)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"\n寫入 {os.path.relpath(OUT)}")
    return 1 if anomalies else 0


if __name__ == "__main__":
    sys.exit(main())
