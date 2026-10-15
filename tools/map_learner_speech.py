"""學習者原話研究步驟 3：經 claude-m3-lite（MiniMax）做兩段處理，結果供 Claude 抽驗。

  extract：_raw/*/posts.jsonl → 判斷是否為第一人稱卡關自述，抽出原話單位 → _work/extract/*.json
  map    ：抽出的單位 → 對照 framework_card.md（只附該泳式段落）標 L 級／三型候選 → _work/map/*.json
  merge  ：兩段結果合併成 units.jsonl（進 repo 的成品）

規格見 Research/學習者原話/README.md。每批結果獨立成檔，已存在就跳過，可斷點續跑。
MiniMax 只做初標；units.jsonl 的對應在使用者審過前一律是 🔴 假設。

用法：
  python tools/map_learner_speech.py extract --round N        （飽和抽樣第 N 輪：Reddit 每查詢 4 篇＋PTT 粗篩後 150 篇）
  python tools/map_learner_speech.py extract [--limit N] [--source reddit|ptt]
  python tools/map_learner_speech.py map [--limit N]
  python tools/map_learner_speech.py merge
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "Research" / "學習者原話"
RAW = BASE / "_raw"
WORK = RAW / "_work"  # 中間產物含原文摘錄，與 _raw 一樣不進 repo
CARD = BASE / "framework_card.md"
UNITS = BASE / "units.jsonl"
M3 = "C:/Users/hangs/bin/claude-m3-lite"  # bash 腳本，Windows 要經 bash 執行

EXTRACT_BATCH = 16
MAP_BATCH = 15
BODY_CHARS = 1800
CALL_TIMEOUT = 1200
MAX_ATTEMPTS = 2
RETRY_WAIT_SECONDS = 60
STROKES = ("free", "back", "breast", "fly")
CARD_HEADINGS = {"free": "自由式", "back": "仰式", "breast": "蛙式", "fly": "蝶式"}

EXTRACT_PROMPT = """\
# 任務：從游泳論壇貼文抽出「學習者自述卡關」的原話

下面是 {n} 篇論壇貼文（英文或中文）。逐篇判斷，只輸出 JSON。

## 收或不收
- **收**：發文者用第一人稱描述**自己**游泳時的困難、身體感覺、做不到的地方。
- **不收**：器材選購、比賽／新聞資訊、純問課表或配速數字、替別人（孩子、學生）問、純分享成就沒有描述困難、只有給別人建議。

## 每篇收的貼文抽出 1–4 個「原話單位」，每個單位：
- `speech_zh`：中文改寫一句。**保留發文者自己的感覺用語**（例：腳很沉、像在爬坡、手好像划過去、喘不過氣），不要翻成專業術語，不要加入你的判斷或原因推測。器材譯名固定：pull buoy＝「夾腿浮條」，kickboard＝「浮板」，fins＝「蛙鞋」，paddles＝「划手板」，snorkel＝「呼吸管」（夾腿浮條與浮板是不同器材，不可混用）。
- `quote_orig`：原文中對應的那一句（逐字，一句以內）。
- `kind`：這句話是哪一種——`felt`（游的當下自己感覺到的，例：腳很沉、吸不到氣）、`observed`（從影片、別人告知、計時結果得知的，例：看影片才發現屁股塌）、`self_explanation`（發文者自己推測的原因，例：應該是臀部下沉造成阻力）。
- `stroke`：free／back／breast／fly／general（沒指明泳式且非四式專屬時用 general）。
- `context`：物件，只填貼文裡**明確提到**的：`speed`（slow／accelerating／sprint）、`fatigue`（例：after_200m、end_of_set）、`equipment`（pull_buoy／fins／kickboard／paddles／snorkel／none）、`breathing`（true 表示困難與換氣有關）、`observed`（true 表示被計時或被看時才發生）。沒提到的鍵不要寫。
- `background`：物件，只填明確提到的：`age_group`（child／teen／adult／senior）、`profile`（beginner／returning／competitive／triathlete／masters）、`years`（泳齡，字串）。

## 輸出格式（只輸出一個 JSON 陣列，放在 ```json 區塊內，不要其他文字）
```json
[
  {{"post_id": "…", "keep": false, "reason": "器材選購"}},
  {{"post_id": "…", "keep": true, "units": [{{"speech_zh": "…", "quote_orig": "…", "stroke": "free", "context": {{}}, "background": {{}}}}]}}
]
```
每篇貼文都要有一筆（共 {n} 筆），`post_id` 照抄。

## 鐵則
- `quote_orig` 必須逐字出現在該貼文中，找不到就不要抽那個單位。
- 不准捏造貼文沒有的內容。

# 貼文
{posts}
"""

MAP_PROMPT = """\
# 任務：把學習者原話對應到水感框架（只做候選假設，不下結論）

下面附「框架速查卡」（{stroke_zh}段落，逐字取自教練框架）與 {n} 句學習者原話。
判準**只能**用速查卡的內容，不要用你自己對游泳分級的理解。

## 每句輸出
- `unit_id`：照抄。
- `sufficient`：這句話的資訊夠不夠判讀。**只要**提到身體部位、身體感覺或具體情境（例：「夾了浮條還是沉」「很難浮起來」「換氣喝到水」）就是 true。只有籠統結果、完全沒有身體或情境（例：「都游不快」「好難」「技術怪怪的」）才是 false，此時 `level_candidates`、`type_candidates` 都給空陣列，其餘欄位照填。
- `level_candidates`：可能的 L 級（L0–L6），1–3 個，每個附 `why`（一句）與 `evidence`（從速查卡**逐字複製**的一小段原文，10–40 字，會被程式比對，不是逐字就作廢）與 `card_id`（該段所在條目，例如 free.L3）。
- `type_candidates`：A／B／C，可多個，每個附 `why`、`evidence`、`card_id`（規則同上）。**L0–L2 不判型；候選都在 L0–L2 時給空陣列。**
- `non_perception`：只在原話或情境**明確提到**時才標，不要推測。
  - `hardware`：泳者說出了身體上**為什麼**做不到的具體原因（關節卡住、活動度不夠、某部位壓不下去、體型／體脂讓身體特別浮或特別沉）。只描述「做不到」「改不掉」「腿會沉」「感覺水壓下來」**不是**硬體——那是感知或身體位置問題（速查卡「前置判斷」：不能描述為什麼 → 感知）。
  - `fitness`：明確提到體力、心肺、肌耐力不夠。單純「累」「喘」若同時有技術描述，不標。
  - `fear_panic`：提到怕、慌、快溺水、恐慌。
  - `pacing`、`equipment`、`pain_injury`、`other`：同理，需明確提到。
- `discriminator`：候選不只一個時，寫一個能把候選分開的問題（比照速查卡判型題的口吻，問泳者的感覺或可做的對照，例如握拳游 vs 開手游）；只有一個候選就寫空字串。
- `matches`：若這句話和速查卡某條 typical_speech 或判型題選項說的是同一件事，填該條目 ID 與型（例如 "free.L3 C typical_speech"）；沒有就空字串。

## 輸出格式（只輸出一個 JSON 陣列，放在 ```json 區塊內）
```json
[{{"unit_id": "…", "sufficient": true, "level_candidates": [{{"level": "L3", "card_id": "free.L3", "evidence": "…逐字…", "why": "…"}}], "type_candidates": [{{"type": "C", "card_id": "free.L3", "evidence": "…逐字…", "why": "…"}}], "non_perception": [], "discriminator": "…", "matches": ""}}]
```
共 {n} 筆。不准捏造速查卡沒有的條目 ID 或引文。繁體中文。
原話的 `kind` 若是 observed（外部得知）或 self_explanation（自己推測原因），判讀時要考慮泳者當下其實可能**感覺不到**——這本身就是感知層級的線索。

# 框架速查卡（{stroke_zh}）
{card}

# 學習者原話
{units}
"""


ENGINE = os.environ.get("VORTEX_ENGINE", "m3")  # m3｜codex（MiniMax 額度不夠時改走 codex 訂閱）
CODEX_PREFIX = "只輸出最後答案，不要執行任何指令、不要讀寫任何檔案、不要輸出計畫。\n\n"


def call_codex(prompt: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "last.txt"
        result = subprocess.run([shutil.which("codex") or "codex", "exec", "--skip-git-repo-check", "--sandbox", "danger-full-access",
                                 "-C", tmp, "-o", str(out), "-"], input=(CODEX_PREFIX + prompt).encode("utf-8"),
                                capture_output=True, timeout=CALL_TIMEOUT)
        text = out.read_text(encoding="utf-8").strip() if out.exists() else ""
    if result.returncode != 0 or not text:
        raise RuntimeError(f"codex exit {result.returncode}: {result.stderr.decode('utf-8', 'replace')[-400:]}")
    return text


def call_m3(prompt: str) -> str:
    if ENGINE == "codex":
        return call_codex(prompt)
    result = subprocess.run(["bash", M3, "-p"], input=prompt.encode("utf-8"),
                            capture_output=True, timeout=CALL_TIMEOUT)
    text = result.stdout.decode("utf-8", errors="replace").strip()
    if result.returncode != 0 or not text:
        raise RuntimeError(f"exit {result.returncode}: {result.stderr.decode('utf-8', 'replace')[-400:]}")
    return text


def parse_json_array(text: str) -> list:
    """M3 有時把結果拆成多個陣列或逐行物件輸出；逐段 raw_decode 後合併。"""
    dec, items, i, found = json.JSONDecoder(), [], 0, False
    while (i := min((k for k in (text.find("[", i), text.find("{", i)) if k >= 0), default=-1)) >= 0:
        try:
            val, end = dec.raw_decode(text, i)
        except json.JSONDecodeError:
            i += 1
            continue
        if isinstance(val, list):
            items += [v for v in val if isinstance(v, dict)]  # 丟掉混進來的裸字串（如 ["fear_panic"]）
            found = True
        elif isinstance(val, dict):
            items.append(val)
            found = True
        i = end
    if not found:
        raise ValueError("no JSON array in answer")
    return items


def run_batch(prompt: str, out: Path) -> None:
    """Call M3 (with retries), validate JSON, write result; stop the run on repeated failure."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            data = parse_json_array(call_m3(prompt))
            out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"[ok] {out.name} ({len(data)})", flush=True)
            return
        except (RuntimeError, ValueError, json.JSONDecodeError, subprocess.TimeoutExpired) as exc:
            print(f"[fail {attempt}] {out.name}: {exc}", flush=True)
            if attempt == MAX_ATTEMPTS:
                raise SystemExit(f"停在 {out.name}；重跑本指令會從這裡續")
            time.sleep(RETRY_WAIT_SECONDS)


def load_posts(source: str | None) -> list[dict]:
    posts = []
    for src in ("reddit", "ptt"):
        if source and src != source:
            continue
        path = RAW / src / "posts.jsonl"
        if path.exists():
            posts += [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l]
    return posts


# PTT 雜訊多（試點 24 篇只留 4 篇）：先用身體／技術詞粗篩，省 MiniMax 額度
PTT_BODY_WORDS = ("換氣", "呼吸", "沉", "浮", "喘", "嗆", "喝水", "踢", "划", "腳", "腿", "手", "臀", "屁股", "腰",
                  "肩", "頭", "身體", "水感", "抓水", "抽筋", "轉身", "滾翻", "憋氣", "前進", "吃力", "卡")


def ptt_relevant(p: dict) -> bool:
    text = p["title"] + p["body"][:BODY_CHARS]
    return p["title"].startswith(("[泳技]", "[問題]", "[請益]")) and sum(w in text for w in PTT_BODY_WORDS) >= 3


def sample_round(round_no: int, per_query: int, ptt_n: int) -> list[dict]:
    """Deterministic stratified sample for one saturation round (each round takes the next slice).

    Reddit: `per_query` posts per search query, so every 卡關切角 is represented.
    PTT: `ptt_n` posts from those passing `ptt_relevant`, evenly spread over the board's history.
    """
    picked = []
    by_query: dict[str, list[dict]] = {}
    for p in load_posts("reddit"):
        by_query.setdefault(p["query"], []).append(p)
    lo, hi = (round_no - 1) * per_query, round_no * per_query
    for group in by_query.values():
        picked += group[lo:hi]
    ptt = [p for p in load_posts("ptt") if ptt_relevant(p)]
    if ptt and ptt_n:
        stride = max(1, len(ptt) // (ptt_n * 4))  # 最多 4 輪不重複
        offset = round_no - 1
        picked += ptt[offset::stride][:ptt_n]
    return picked


def minimax_5h_used() -> float | None:
    """Read MiniMax 5H usage from deskboard; None if unavailable (then we don't block)."""
    try:
        sys.path.insert(0, "C:/claudehome/tools/deskboard")
        import llm_usage  # noqa: PLC0415
        return next(w.used_percent for w in llm_usage.read_minimax().windows if w.label == "5H")
    except Exception:
        return None


QUOTA_STOP_PERCENT = 90


def quota_guard() -> None:
    if ENGINE == "codex":
        return
    used = minimax_5h_used()
    if used is not None and used >= QUOTA_STOP_PERCENT:
        raise SystemExit(f"MiniMax 5H 已用 {used:.0f}%（≥{QUOTA_STOP_PERCENT}%），停下；重跑同指令會從這裡續")


def cmd_extract(limit: int | None, source: str | None, round_no: int | None = None) -> None:
    out_dir = WORK / "extract"
    out_dir.mkdir(parents=True, exist_ok=True)
    if round_no:  # PTT 還在蒐集時先跑 --source reddit，抽樣才不會隨資料增加而漂移
        posts = [p for p in sample_round(round_no, per_query=4, ptt_n=150)
                 if not source or p["source"].startswith(source)]
    else:
        posts = load_posts(source)[:limit] if limit else load_posts(source)
    print(f"{len(posts)} posts to extract", flush=True)
    for i in range(0, len(posts), EXTRACT_BATCH):
        batch = posts[i:i + EXTRACT_BATCH]
        out = out_dir / f"{batch[0]['id']}__{len(batch)}.json"
        if out.exists():
            continue
        quota_guard()
        text = "\n\n".join(f"## post_id: {p['id']}\n標題：{p['title']}\n{p['body'][:BODY_CHARS]}" for p in batch)
        run_batch(EXTRACT_PROMPT.format(n=len(batch), posts=text), out)


def norm(s: str) -> str:
    """Compare quotes on letters/digits/CJK only, so full- vs half-width punctuation and spacing don't matter."""
    return re.sub(r"[\W_]+", "", s or "").lower()


def extracted_units() -> list[dict]:
    """Flatten extract results into units with stable ids, checking quotes against the raw post."""
    posts = {p["id"]: p for p in load_posts(None)}
    units, done_posts = [], set()
    for f in sorted((WORK / "extract").glob("*.json")):
        for rec in json.loads(f.read_text(encoding="utf-8")):
            post = posts.get(rec.get("post_id"))
            if not rec.get("keep") or not post or post["id"] in done_posts:  # 同篇跨輪重抽只取一次
                continue
            done_posts.add(post["id"])
            for k, u in enumerate(rec.get("units") or [], 1):
                quote = (u.get("quote_orig") or "").strip()
                u.update(unit_id=f"{post['id']}#{k}", post_id=post["id"], url=post["url"],
                         source=post["source"], date=post.get("date", ""),
                         quote_verified=bool(norm(quote)) and norm(quote) in norm(post["title"] + post["body"]))
                units.append(u)
    return units


def card_section(stroke: str) -> str:
    """Return the framework card part for one stroke (general → free, the most detailed one)."""
    card = CARD.read_text(encoding="utf-8")
    zh = CARD_HEADINGS.get(stroke, "自由式")
    parts = re.split(r"(?m)^### ", card)
    keep = [p for p in parts[1:] if p.startswith(zh)]
    return "### " + "### ".join(keep) if keep else card


def cmd_map(limit: int | None) -> None:
    out_dir = WORK / "map"
    out_dir.mkdir(parents=True, exist_ok=True)
    units = [u for u in extracted_units() if u["quote_verified"]]
    units = units[:limit] if limit else units
    by_stroke: dict[str, list[dict]] = {}
    for u in units:
        by_stroke.setdefault(u.get("stroke") if u.get("stroke") in STROKES else "free", []).append(u)
    shard, n_shards = map(int, os.environ.get("VORTEX_SHARD", "0/1").split("/"))  # 平行跑：0/3、1/3、2/3
    k = -1
    for stroke, group in by_stroke.items():
        for i in range(0, len(group), MAP_BATCH):
            batch = group[i:i + MAP_BATCH]
            out = out_dir / f"{stroke}__{batch[0]['unit_id'].replace('#', '_')}__{len(batch)}.json"
            k += 1
            if out.exists() or k % n_shards != shard:
                continue
            quota_guard()
            text = "\n".join(f"- unit_id: {u['unit_id']}｜泳式：{u.get('stroke')}｜kind：{u.get('kind', '')}"
                             f"｜情境：{json.dumps(u.get('context') or {}, ensure_ascii=False)}"
                             f"｜原話：{u['speech_zh']}" for u in batch)
            run_batch(MAP_PROMPT.format(stroke_zh=CARD_HEADINGS[stroke], n=len(batch),
                                        card=card_section(stroke), units=text), out)


def check_evidence(cands: list, card_norm: str) -> tuple[list, int]:
    """Keep candidates whose `evidence` is a verbatim excerpt of the framework card; return (kept, dropped)."""
    kept = [c for c in cands or [] if len(norm(c.get("evidence"))) >= 6 and norm(c.get("evidence")) in card_norm]
    return kept, len(cands or []) - len(kept)


def cmd_merge() -> None:
    card_norm = norm(CARD.read_text(encoding="utf-8"))
    mapped = {}
    for f in sorted((WORK / "map").glob("*.json")):
        for rec in json.loads(f.read_text(encoding="utf-8")):
            mapped[rec.get("unit_id")] = rec
    rows, dropped, seen = [], 0, set()
    for u in extracted_units():
        m = mapped.get(u["unit_id"])
        if not m or u.get("quote_orig") in seen:  # 跨板重貼的同一句只留第一次
            continue
        seen.add(u.get("quote_orig"))
        # codex 有時把 non_perception 寫成 {"key": "fitness", "why": …}；統一成字串鍵
        m["non_perception"] = [x if isinstance(x, str) else next(
            (x[k] for k in ("key", "kind", "category", "type") if isinstance(x.get(k), str)),
            next((k for k, v in x.items() if v is True), "other")) for x in m.get("non_perception") or []]
        u.update({k: v for k, v in m.items() if k != "unit_id"}, certainty="🔴", reviewed=False)
        for key in ("level_candidates", "type_candidates"):
            u[key], n = check_evidence(u.get(key), card_norm)
            dropped += n
        rows.append(u)
    UNITS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"wrote {len(rows)} units → {UNITS.relative_to(ROOT)}；引文非逐字而作廢的候選 {dropped} 個")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("cmd", choices=("extract", "map", "merge"))
    ap.add_argument("--limit", type=int)
    ap.add_argument("--source", choices=("reddit", "ptt"))
    ap.add_argument("--round", type=int, help="飽和抽樣第幾輪（extract 用）")
    args = ap.parse_args()
    {"extract": lambda: cmd_extract(args.limit, args.source, args.round),
     "map": lambda: cmd_map(args.limit), "merge": cmd_merge}[args.cmd]()


if __name__ == "__main__":
    main()
