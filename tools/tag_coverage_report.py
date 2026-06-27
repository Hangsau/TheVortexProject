"""
Tag coverage report for Drills/ — 9-axis fingerprint分析

跑：python tools/tag_coverage_report.py
輸出：每軸 enum 值的 drill 數量、碰撞（指紋重複）、空白格、擁擠格
"""
from __future__ import annotations
import sys
from collections import Counter, defaultdict
from pathlib import Path
import yaml

DRILLS_DIR = Path(__file__).resolve().parent.parent / "Drills"
FILES = [
    "drills_freestyle.yaml",
    "drills_backstroke.yaml",
    "drills_breaststroke.yaml",
    "drills_butterfly.yaml",
    "drills_sculling.yaml",
    "drills_starts-turns.yaml",
    "drills_udk.yaml",
]

AXES_SCALAR = [
    "body_position",
    "movement_pattern",
    "stroke_phase",
    "drill_function",
    "cognitive_load",
    "tactile_anchor",
    "difficulty_tier",
]
AXES_LIST = ["constraints", "skill_focus"]


def load_all() -> list[dict]:
    drills = []
    for fname in FILES:
        path = DRILLS_DIR / fname
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for d in data.get("drills", []):
            d["_file"] = fname
            drills.append(d)
    return drills


def axis_counts(drills: list[dict]) -> dict[str, Counter]:
    result: dict[str, Counter] = {}
    for ax in AXES_SCALAR:
        result[ax] = Counter(d.get(ax) for d in drills)
    for ax in AXES_LIST:
        c: Counter = Counter()
        for d in drills:
            vals = d.get(ax) or []
            if not vals:
                c["(empty)"] += 1
            for v in vals:
                c[v] += 1
        result[ax] = c
    return result


def fingerprint(d: dict) -> tuple:
    parts = []
    for ax in AXES_SCALAR:
        parts.append((ax, d.get(ax)))
    for ax in AXES_LIST:
        vals = tuple(sorted(d.get(ax) or []))
        parts.append((ax, vals))
    return tuple(parts)


def collisions(drills: list[dict]) -> dict[str, list[str]]:
    """同 stroke 下指紋完全相同 = 標籤定義太粗 or drill 真重複"""
    by_stroke: dict[str, list[dict]] = defaultdict(list)
    for d in drills:
        for s in d.get("strokes") or ["unknown"]:
            by_stroke[s].append(d)

    result: dict[str, list[str]] = {}
    for stroke, ds in by_stroke.items():
        groups: dict[tuple, list[str]] = defaultdict(list)
        for d in ds:
            groups[fingerprint(d)].append(d["id"])
        for fp, ids in groups.items():
            if len(ids) > 1:
                result.setdefault(stroke, []).append(", ".join(ids))
    return result


def cross_tab(
    drills: list[dict], ax_a: str, ax_b: str, scope_stroke: str | None = None
) -> dict[tuple, int]:
    """ax_a × ax_b 二維分布"""
    grid: Counter = Counter()
    for d in drills:
        if scope_stroke and scope_stroke not in (d.get("strokes") or []):
            continue
        va = d.get(ax_a)
        vb = d.get(ax_b)
        if ax_a in AXES_LIST:
            va_list = d.get(ax_a) or ["(empty)"]
        else:
            va_list = [va]
        if ax_b in AXES_LIST:
            vb_list = d.get(ax_b) or ["(empty)"]
        else:
            vb_list = [vb]
        for a in va_list:
            for b in vb_list:
                grid[(a, b)] += 1
    return dict(grid)


def print_section(title: str):
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


def main():
    drills = load_all()
    print(f"Loaded {len(drills)} drills from {len(FILES)} files.")

    print_section("1. 各軸 enum 值分布")
    for ax in AXES_SCALAR + AXES_LIST:
        c = axis_counts(drills)[ax]
        print(f"\n[{ax}]")
        for val, n in sorted(c.items(), key=lambda x: -x[1]):
            bar = "#" * min(n, 50)
            print(f"  {str(val):30s} {n:4d}  {bar}")

    print_section("2. 指紋碰撞（同泳式內 9 軸完全相同）")
    coll = collisions(drills)
    if not coll:
        print("  ✓ 無碰撞——每個 drill 在所屬泳式內都有獨特指紋。")
    else:
        for stroke, groups in coll.items():
            print(f"\n  [{stroke}] {len(groups)} 組碰撞：")
            for g in groups:
                print(f"    - {g}")

    print_section("3. body_position × skill_focus（找空白格）")
    grid = cross_tab(drills, "body_position", "skill_focus")
    body_vals = sorted({k[0] for k in grid})
    focus_vals = sorted({k[1] for k in grid})
    header = "body \\ focus".ljust(15) + "".join(f"{f[:6]:>8s}" for f in focus_vals)
    print(header)
    for bv in body_vals:
        row = f"{bv:15s}"
        for fv in focus_vals:
            n = grid.get((bv, fv), 0)
            row += f"{n:>8d}" if n > 0 else f"{'.':>8s}"
        print(row)

    print_section("4. 各泳式 drill 分布")
    by_stroke: Counter = Counter()
    for d in drills:
        for s in d.get("strokes") or ["unknown"]:
            by_stroke[s] += 1
    for s, n in sorted(by_stroke.items(), key=lambda x: -x[1]):
        print(f"  {s:25s} {n:4d}")

    print_section("5. drill_function × difficulty_tier")
    grid = cross_tab(drills, "drill_function", "difficulty_tier")
    funcs = sorted({k[0] for k in grid})
    tiers = ["foundation", "intermediate", "advanced", "elite"]
    print(f"  function \\ tier".ljust(25) + "".join(f"{t[:6]:>10s}" for t in tiers))
    for f in funcs:
        row = f"  {f:23s}"
        for t in tiers:
            n = grid.get((f, t), 0)
            row += f"{n:>10d}" if n > 0 else f"{'.':>10s}"
        print(row)


if __name__ == "__main__":
    main()
