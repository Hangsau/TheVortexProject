"""從 canonical/technica/water-sense-levels.yaml 產生「L0–L6 × 三型」框架速查卡（Markdown）。

給學習者原話對照研究的分類者（人或 LLM）當唯一判準：卡片內容逐字取自 canonical，
不另寫摘要，避免分類依據與真相源漂移。canonical 改了就重跑。

用法：python tools/build_framework_card.py  → Research/學習者原話/framework_card.md
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "canonical" / "technica" / "water-sense-levels.yaml"
OUT = ROOT / "Research" / "學習者原話" / "framework_card.md"

STROKE_ZH = {"free": "自由式", "back": "仰式", "breast": "蛙式", "fly": "蝶式"}
LEVEL_FIELDS = ("description", "stagnation")


def flat(s) -> str:
    return " ".join(str(s).split()) if s else ""


def render_types(stroke: str, tt: dict) -> list[str]:
    lines = [f"### {STROKE_ZH.get(stroke, stroke)}：三型定義"]
    for t, d in (tt.get("definition") or {}).items():
        if not isinstance(d, dict):
            lines.append(f"- 註：{flat(d)}")
            continue
        lines.append(f"- **{t} 型｜{d.get('name', '')}**：{flat(d.get('core_problem'))}"
                     f"　表現：{flat(d.get('manifestation'))}　發展：{flat(d.get('development'))}")
    for key in ("pre_judgment",):
        if tt.get(key):
            lines.append(f"\n**前置判斷（硬體邊界 vs 感知缺陷）**：{flat(tt[key])}")
    return lines


def render_level(rec: dict) -> list[str]:
    pub, diag = rec.get("public") or {}, rec.get("diagnostic") or {}
    lines = [f"#### {rec['id']}｜{rec.get('name_zh', '')}：{rec.get('tagline', '')}"]
    for f in LEVEL_FIELDS:
        if pub.get(f):
            lines.append(f"- {f}：{flat(pub[f])}")
    for ind in pub.get("indicators") or []:
        lines.append(f"- 指標（{ind.get('type', '')}）：{flat(ind.get('text'))}")
    # 各泳式 diagnostic 的結構不一致（list／dict／字串都有），一律通用展開
    for key in ("type_diagnosis", "type_states", "sinking_triage"):
        val = diag.get(key)
        items = val.items() if isinstance(val, dict) else enumerate(val or [])
        for k, v in items:
            lines.append(f"- {key}[{k}]｜{inline(v)}")
    return lines


def inline(v) -> str:
    if isinstance(v, dict):
        return "｜".join(f"{k}：{inline(x)}" for k, x in v.items())
    if isinstance(v, list):
        return "；".join(inline(x) for x in v)
    return flat(v)


def main() -> None:
    data = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    out = ["# 框架速查卡：L0–L6 × 三型（自動產生，勿手改）",
           f"> 來源：`canonical/technica/water-sense-levels.yaml`；重生：`python tools/build_framework_card.py`",
           "> 三型診斷從 L3 開始適用；L0–L2 不判型。所有 typical_speech 是教練撰寫，不是實測語料。", ""]
    for stroke, tt in (data.get("three_types") or {}).items():
        out += render_types(stroke, tt) + [""]
        for rec in data.get("levels") or []:
            if rec.get("stroke") == stroke:
                out += render_level(rec) + [""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
