#!/usr/bin/env python3
"""MiniMax-M3 first-pass content review for 三層重構 Phase 2.

Splits each target file into chunks, sends every chunk to ``claude-m3-lite -p``
with the reviewer role and a fixed answer format, and writes one markdown file
per chunk under ``plans/內容審查_2026-10-14/初讀/``. Existing non-empty outputs
are skipped, so an interrupted run resumes where it stopped.

MiniMax only *finds suspicious points*; every finding is verified by Claude
before anything in canonical changes (plans/三層重構與全庫檢查_2026-10-14.md §4).

Usage:
    python tools/review_firstpass.py [--batch 2.1 ...] [--dry-run]
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MYSITE = ROOT.parent / "my-site"
OUT_DIR = ROOT / "plans" / "內容審查_2026-10-14" / "初讀"
ROLE_FILE = Path("C:/claudehome/tools/m3-reviewer-role.md")
M3 = "C:/Users/hangs/bin/claude-m3-lite"  # bash 腳本，Windows 要經 bash 執行
CHUNK_CHARS = 18000
CALL_TIMEOUT = 1200

BATCHES: dict[str, list[Path]] = {
    "2.1": sorted((ROOT / "canonical/health/drafts").glob("*.yaml"))
           + sorted((ROOT / "canonical/breathing").glob("*.yaml")),
    "2.2": [ROOT / "canonical/psychology/psychology.yaml"],
    "2.3": [MYSITE / "data/vortex" / f"{s}.yaml"
            for s in ("free", "back", "breast", "fly", "udk", "starts-turns")],
    "2.4": [ROOT / "canonical/instructional/problems.yaml"]
           + sorted((ROOT / "Drills").glob("drills_*.yaml")),
    "2.5": sorted((ROOT / "canonical/movement").glob("*.yaml")),
    "2.6": sorted((ROOT / "canonical/periodization").glob("*.yaml"))
           + sorted((ROOT / "canonical/development").glob("*.yaml")),
}

INSTRUCTIONS = """\
# 任務：游泳教學知識庫內容初讀（找可疑點，不下定論）

背景：The Vortex Project 是游泳教學知識庫，下面的 YAML 片段會公開上網站（`diagnostic` 子樹只給教練、不上網站）。
讀者涵蓋兒童、競技選手、鐵人三項、成人初學者、家長、教練，不得預設單一族群。
確定性標記：🔵 物理／解剖推導（不需文獻）、🟢 近期文獻、🟡 舊文獻、🟠 教練觀測、🔴 待查／假設。

請逐條找出下列問題，**只回報有問題的地方**：

1. 同一片段內互相矛盾（兩處說法衝突）。
2. 明顯的事實、物理、生理、解剖、算術、單位錯誤。
3. 安全主張失準：把正常訓練說成危險，或沒寫出真正危險的條件組合。判準是「哪一種行為」危險，不是地點粗分。
4. 確定性標記與內容不符：例如實證數字標 🔵、只有教練說法卻標 🟢、引用研究卻說不出研究顯示了什麼。
5. 文獻歸屬可疑：作者、年份、期刊、樣本數、效果量看起來不對或被過度解讀（例如單一小樣本寫成「確認」）。
6. 公開欄位（`diagnostic` 以外）出現教練診斷用語（A/B/C 型、分型判讀），或規定讀者「應該有什麼感覺」。
7. 把某一族群當成預設對象，或把只在某族群成立的結論寫成通則。

## 回答格式（每個問題一節，沒有問題的條目不要寫）

```
### <條目 id>｜<欄位路徑>
- 原文：「逐字摘錄有問題的那一句」
- 類型：1–7 擇一
- 問題：1–3 句
- 建議：可直接替換的句子；需要數字但不確定時寫〔待查證〕，不准自己填
- 查法：Claude 要怎麼驗證（查哪篇原文、grep 什麼、算什麼）
- 信心：高／中／低
```

最後一行寫：`本片段共 N 個問題`。整段都沒問題就只寫 `本片段共 0 個問題`。

## 鐵則

- 原文必須逐字摘錄自下面的片段；摘不出原文的問題不要寫。
- 不准捏造研究、作者、年份、數字。你不確定的事寫「待查證」。
- 不寫開場白、不寫總結、繁體中文。
"""


def role_block() -> str:
    text = ROLE_FILE.read_text(encoding="utf-8")
    start = text.index("## 【角色指令】")
    end = text.index("---", start)
    return text[start:end].strip()


def units_of(path: Path) -> list[tuple[str, object]]:
    """Split a YAML file into reviewable units (list items or top-level keys)."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return [(path.stem, data)]
    units: list[tuple[str, object]] = []
    for key, value in data.items():
        if isinstance(value, list) and value and isinstance(value[0], dict):
            for i, item in enumerate(value):
                units.append((f"{key}[{item.get('id', i)}]", item))
        elif isinstance(value, (dict, list)):
            units.append((key, value))
    return units or [(path.stem, data)]


def dump(obj: object) -> str:
    return yaml.safe_dump(obj, allow_unicode=True, sort_keys=False, width=200)


def chunks_of(path: Path) -> list[str]:
    chunks: list[str] = []
    current = ""
    for label, obj in units_of(path):
        block = f"## {label}\n```yaml\n{dump(obj)}```\n"
        if current and len(current) + len(block) > CHUNK_CHARS:
            chunks.append(current)
            current = ""
        current += block
    if current:
        chunks.append(current)
    return chunks


def out_name(batch: str, path: Path, n: int) -> Path:
    return OUT_DIR / f"{batch}_{path.parent.name}_{path.stem}_{n:02d}.md"


def call_m3(prompt: str) -> str:
    result = subprocess.run(
        ["bash", M3, "-p"],
        input=prompt.encode("utf-8"), capture_output=True, timeout=CALL_TIMEOUT,
    )
    text = result.stdout.decode("utf-8", errors="replace").strip()
    if result.returncode != 0 or not text:
        raise RuntimeError(f"exit {result.returncode}: "
                           f"{result.stderr.decode('utf-8', errors='replace')[-400:]}")
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--batch", nargs="*", default=list(BATCHES))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    role = role_block()
    for batch in args.batch:
        for path in BATCHES[batch]:
            for n, chunk in enumerate(chunks_of(path), 1):
                out = out_name(batch, path, n)
                if out.exists() and out.stat().st_size > 0:
                    continue
                if args.dry_run:
                    print(f"[dry] {out.name} {len(chunk)} chars")
                    continue
                prompt = f"{role}\n\n{INSTRUCTIONS}\n\n# 片段（{path.name} 第 {n} 段）\n\n{chunk}"
                for attempt in (1, 2):
                    try:
                        answer = call_m3(prompt)
                        break
                    except (RuntimeError, subprocess.TimeoutExpired) as exc:
                        print(f"[fail {attempt}] {out.name}: {exc}", flush=True)
                        if attempt == 2:
                            raise SystemExit(f"停在 {out.name}；重跑本指令會從這裡續")
                        time.sleep(60)
                header = f"<!-- 來源：{path.relative_to(ROOT.parent).as_posix()} 第 {n} 段 -->\n\n"
                out.write_text(header + answer + "\n", encoding="utf-8")
                print(f"[ok] {out.name}", flush=True)
    print("全部完成", flush=True)


if __name__ == "__main__":
    main()
