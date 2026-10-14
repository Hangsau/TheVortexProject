#!/usr/bin/env python3
"""Audit which layer every published Vortex page belongs to (三層重構 Phase 1).

Reads a local my-site build (``hugo -d <dir>/cortex``) plus this repo's prose
and canonical history, and writes ``reports/layer_audit.md`` with four checks:

1. W1.1 page → source kind → target layer; pages matching no rule are listed.
2. W1.2 prose drift: clauses removed from canonical since ``--since`` that are
   no longer anywhere in canonical but still appear in published prose.
3. W1.3 diagnostic language (A/B/C 型 etc.) in published page text.
4. W1.4 machine keys, external links, and 🟢/🟡 prose lines without a year.

Counts in the report are the denominators for the Phase 3 gate
(plans/三層重構與全庫檢查_2026-10-14.md). Zero LLM involvement.

Usage:
    python tools/audit_layers.py --site <build>/cortex [--since 27ffd10^]
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MYSITE = ROOT.parent / "my-site"
REPORT = ROOT / "reports" / "layer_audit.md"
DEFAULT_SINCE = "27ffd10^"  # parent of the 2026-10-01 content review

# Prose directories that my-site mounts as article pages (sync_vortex.py).
PROSE_DIRS = ("Instructional", "Technica", "Bridge")
# 仍在呈現／應用層的散文（其餘 Instructional／Technica 是研究庫的凍結底稿，Bridge 已退役）
PRESENTATION_PROSE = {"游泳器材使用指南", "水感是什麼"}
STROKE_DATA = ("free", "back", "breast", "fly", "udk", "starts-turns")

# first URL segment under /vortex/ → (source kind, source, target layer, issue)
SEGMENT_RULES = {
    "": ("my-site 版型", "next/layouts/_partials/vortex/home.html", "呈現", ""),
    "tech": ("canonical", "instructional/technical-analysis.yaml", "呈現", ""),
    "errors": ("canonical", "instructional/teaching-errors.yaml", "呈現", ""),
    "levels": ("canonical", "technica/water-sense-levels.yaml", "呈現", ""),
    "injuries": ("canonical", "health/injuries.yaml", "呈現", ""),
    "mind": ("canonical", "psychology/psychology.yaml", "呈現", ""),
    "psychology": ("canonical", "psychology/psychology.yaml", "呈現", ""),
    "drills": ("canonical", "Drills/drills_*.yaml", "呈現", ""),
    "adm": ("canonical", "development/*.yaml", "呈現", ""),
    "breathing": ("canonical", "breathing/*.yaml", "呈現", ""),
    "periodization": ("canonical", "periodization/*.yaml", "呈現", ""),
    "joints": ("canonical", "instructional/technical-analysis.yaml (joint)", "呈現", ""),
    "movement": ("canonical", "movement/*.yaml", "呈現", ""),
    "problems": ("canonical", "instructional/problems.yaml", "應用", ""),
    "workout-studio": ("工具", "next/layouts/_partials/vortex/workout-redirect.html", "應用", "P4"),
    "workout": ("工具", "next/assets/js/workout*.js", "應用", "P4"),
    "moves": ("canonical", "instructional/moves.yaml", "呈現", ""),
    "water-sense": ("散文（公開文章）", "Technica/水感是什麼.md", "呈現", ""),
    "research": ("散文（研究底稿）", "Instructional／Technica/*.md → research/drafts", "資料庫", ""),
    "instructional": ("散文", "Instructional/*.md", "資料庫", "P1"),
    "technica": ("散文", "Technica/*.md", "資料庫", "P1"),
    "bridge": ("散文", "Bridge/*.md", "資料庫", "P1"),
}
for _s in STROKE_DATA:
    SEGMENT_RULES[_s] = ("canonical", "instructional/moves.yaml（泳式樞紐）", "呈現", "")
# Article pages whose target layer differs from their directory's default.
PAGE_OVERRIDES = {
    "instructional/equipment-guide": ("散文", "Instructional/游泳器材使用指南.md", "應用", ""),
    "instructional": ("my-site 版型", "content/vortex/instructional/_index.md", "應用", ""),
}

DIAG_PATTERNS = {
    "A/B/C 型": re.compile(r"[ABC]\s?型"),
    # 「疼痛三型」「讓泳者說得出」是一般用語，只算診斷框架的寫法
    "三型": re.compile(r"三型(?:診斷|分類|的|訊號|區分)|感知三型"),
    "泳者說": re.compile(r"泳者說[「『：:]"),
    "typical_speech": re.compile(r"typical_speech"),
    "診斷問題": re.compile(r"診斷問題"),
}
MACHINE_KEY = re.compile(r"\bsrc\.[a-z0-9][a-z0-9-]+|\b(?:fatal_acute|source_ids|observation_basis|cross_ref)\b")
CLAUSE_SPLIT = re.compile(r"[，。；：！？、（）()「」『』\n|*#>]+|——")
YEAR = re.compile(r"(?:19|20)\d\d")
MIN_CLAUSE = 10

TAG = re.compile(r"<[^>]+>")
SCRIPT_STYLE = re.compile(r"<(script|style)\b.*?</\1>", re.S)
HREF = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"')
REDIRECT = re.compile(r'http-equiv="refresh"')


def page_text(raw: str) -> str:
    return html.unescape(TAG.sub(" ", SCRIPT_STYLE.sub(" ", raw)))


def classify(rel: str):
    if rel in PAGE_OVERRIDES:
        return PAGE_OVERRIDES[rel]
    return SEGMENT_RULES.get(rel.split("/")[0] if rel else "")


def collect_pages(site: Path):
    """Yield (relative url path, raw html) for every non-redirect Vortex page."""
    for f in sorted((site / "vortex").rglob("index.html")):
        raw = f.read_text(encoding="utf-8")
        if REDIRECT.search(raw):
            continue
        rel = f.parent.relative_to(site / "vortex").as_posix()
        yield ("" if rel == "." else rel), raw


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout


def clauses(text: str):
    for c in CLAUSE_SPLIT.split(text):
        c = c.strip(" -+'\"`")
        if len(c) >= MIN_CLAUSE:
            yield c


def removed_canonical_clauses(since: str) -> dict[str, str]:
    """Clauses deleted from canonical YAML since ``since`` and absent from HEAD."""
    diff = git("diff", "--unified=0", since, "HEAD", "--", "canonical",
               ":(exclude)canonical/_sources.yaml")
    removed: dict[str, str] = {}
    current_file = ""
    for line in diff.splitlines():
        if line.startswith("+++ "):
            current_file = line[6:]
        elif line.startswith("-") and not line.startswith("---"):
            for c in clauses(line[1:]):
                removed.setdefault(c, current_file)
    canonical_now = "\n".join(p.read_text(encoding="utf-8")
                              for p in (ROOT / "canonical").rglob("*.yaml"))
    return {c: f for c, f in removed.items() if c not in canonical_now}


def prose_files():
    """(path, is_presentation)：研究底稿已在研究庫標凍結，漂移分開計。"""
    for d in PROSE_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            yield p, p.stem in PRESENTATION_PROSE
    yield ROOT / "canonical" / "instructional" / "moves.yaml", True


def label(p: Path) -> str:
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return "my-site/" + p.relative_to(MYSITE).as_posix()


def audit(site: Path, since: str) -> str:
    pages = list(collect_pages(site))
    by_kind: Counter = Counter()
    by_layer: Counter = Counter()
    issues: dict[str, list[str]] = defaultdict(list)
    unmatched: list[str] = []
    diag_hits: list[tuple[str, Counter]] = []
    machine_hits: list[tuple[str, list[str]]] = []
    external: list[tuple[str, str]] = []

    for rel, raw in pages:
        rule = classify(rel)
        if rule is None:
            unmatched.append(rel)
        else:
            kind, _src, layer, issue = rule
            by_kind[kind] += 1
            by_layer[layer] += 1
            if issue:
                issues[issue].append(rel)
        text = page_text(raw)
        hits = Counter({k: len(p.findall(text)) for k, p in DIAG_PATTERNS.items()})
        hits = +hits
        if hits:
            diag_hits.append((rel, hits))
        # 審查與裁決紀錄是工作紀錄：來源鍵與欄位名就是被審查的對象，照原樣保留
        keys = [] if rel.startswith("research/rulings") else sorted(set(MACHINE_KEY.findall(text)))
        if keys:
            machine_hits.append((rel, keys))
        for url in HREF.findall(raw):
            if "hangsau.github.io" not in url and "127.0.0.1" not in url:
                external.append((rel, url))

    removed = removed_canonical_clauses(since)
    drift: list[tuple[str, str, str]] = []
    frozen_drift = 0
    cert_no_year: list[tuple[str, int, str]] = []
    for p, presentation in prose_files():
        if not p.exists():
            continue
        body = p.read_text(encoding="utf-8")
        for c, src in removed.items():
            if c in body:
                if presentation:
                    drift.append((label(p), c, src))
                else:
                    frozen_drift += 1
        for n, line in enumerate(body.splitlines(), 1):
            if presentation and ("🟢" in line or "🟡" in line) and not YEAR.search(line):
                cert_no_year.append((label(p), n, line.strip()[:80]))

    out: list[str] = []
    w = out.append
    w("# 三層歸屬稽核報告（Phase 1）\n")
    w(f"> 由 `tools/audit_layers.py` 產生；drift 基準 `{since}`。數字是 Phase 3 閘門分母。\n")
    w("## 摘要\n")
    w("| 檢查 | 筆數 |\n|---|---|")
    w(f"| 已發布 Vortex 頁（不含轉址） | {len(pages)} |")
    w(f"| 無歸屬頁 | {len(unmatched)} |")
    w(f"| P1 散文頁 | {len(issues['P1'])} |")
    w(f"| P3 my-site 手管／手寫頁 | {len(issues['P3'])} |")
    w(f"| P1 漂移候選：呈現／應用層（閘門，須為 0） | {len(drift)} |")
    w(f"| 漂移：研究庫凍結底稿（已加凍結說明，僅供參考） | {frozen_drift} |")
    w(f"| P2 公開頁含診斷語的頁 | {len(diag_hits)}（共 {sum(sum(c.values()) for _, c in diag_hits)} 處） |")
    w(f"| 機器鍵外洩頁 | {len(machine_hits)} |")
    w(f"| 外站連結 | {len(external)} |")
    w(f"| 🟢／🟡 但同行無年份（呈現層散文／手管） | {len(cert_no_year)} |\n")

    w("## W1.1 頁面 → 層\n")
    w("| 目標層 | 頁數 |\n|---|---|")
    for k, v in sorted(by_layer.items()):
        w(f"| {k} | {v} |")
    w("\n| 來源種類 | 頁數 |\n|---|---|")
    for k, v in sorted(by_kind.items()):
        w(f"| {k} | {v} |")
    w("\n**無歸屬頁**：" + ("、".join(f"`{u}`" for u in unmatched) if unmatched else "無") + "\n")
    for code in ("P1", "P3", "P4"):
        if issues[code]:
            w(f"**{code} 頁**：" + "、".join(f"`{u}`" for u in issues[code]) + "\n")

    w("## W1.2 散文漂移候選\n")
    w("句段在 canonical 的修訂中被刪除、現行 canonical 已無，但仍出現在散文或手管資料。"
      "屬「候選」：改寫同義、或散文本就另有語境者需人工判定。\n")
    w("| 檔案 | 句段 | 原 canonical 檔 |\n|---|---|---|")
    for f, c, src in sorted(drift):
        w(f"| `{f}` | {c.replace('|', '／')} | `{src}` |")

    w("\n## W1.3 公開頁診斷語\n")
    w("| 頁 | 命中 |\n|---|---|")
    for rel, hits in sorted(diag_hits, key=lambda x: -sum(x[1].values())):
        w(f"| `{rel or '(首頁)'}` | " + "、".join(f"{k}×{v}" for k, v in hits.items()) + " |")

    w("\n## W1.4 機器鍵／外站連結／確定性無年份\n")
    w("**機器鍵外洩**\n")
    for rel, keys in machine_hits:
        w(f"- `{rel}`：{', '.join(keys)}")
    if not machine_hits:
        w("- 無")
    w("\n**外站連結**\n")
    for rel, url in external:
        w(f"- `{rel}` → {url}")
    if not external:
        w("- 無")
    w("\n**🟢／🟡 同行無年份**\n")
    w("| 檔案 | 行 | 內容 |\n|---|---|---|")
    for f, n, line in cert_no_year:
        w(f"| `{f}` | {n} | {line.replace('|', '／')} |")
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--site", required=True, type=Path,
                    help="hugo 建置輸出的 cortex 目錄（內含 vortex/）")
    ap.add_argument("--since", default=DEFAULT_SINCE,
                    help="漂移比對的 canonical 基準 commit")
    args = ap.parse_args()
    if not (args.site / "vortex").is_dir():
        raise SystemExit(f"找不到 {args.site / 'vortex'}：請先用 hugo -d 建置 my-site")
    REPORT.write_text(audit(args.site, args.since), encoding="utf-8")
    print(f"寫入 {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
