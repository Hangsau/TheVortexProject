"""蒐集學習者自述卡關的原始貼文（Reddit 搜尋 RSS、PTT swim 板），供「學習者原話 → L 級／三型」對照研究使用。

輸出只寫進 Research/學習者原話/_raw/（gitignored）：原文含使用者帳號與全文，不進 repo。
每抓到一筆立即 append 到 JSONL，已完成的查詢／頁面記在 done 檔，中斷後重跑會跳過。

用法：
  python tools/collect_learner_speech.py reddit
  python tools/collect_learner_speech.py ptt
"""
import html
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "Research" / "學習者原話" / "_raw"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ATOM = {"a": "http://www.w3.org/2005/Atom"}

REDDIT_GAP_SEC = 40
PTT_GAP_SEC = 1.5
MAX_RETRY = 5

# (subreddit, query)：只找「自己描述卡關」的切角，回覆不收
REDDIT_QUERIES = [("Swimming", q) for q in [
    "legs sink", "hips sink", "legs sinking freestyle", "out of breath", "gasping for air",
    "can't breathe freestyle", "breathing freestyle help", "tired arms", "shoulders tired",
    "pull buoy faster", "kick doesn't move", "kicking slow", "kickboard not moving",
    "feel the water", "catch feels", "slipping through water", "breaststroke kick help",
    "breaststroke slow", "butterfly exhausted", "butterfly timing", "backstroke sinking",
    "backstroke water nose", "flip turn help", "swallow water", "panic deep water",
    "can't swim more than 25", "struggling to swim laps", "plateau", "stuck at same pace",
    "why am I so slow", "technique feedback", "heavy legs swimming", "head position",
    "rotation freestyle", "crossover", "exhausted after one lap", "lose rhythm",
    "stroke falls apart", "drag", "streamline", "feel like I'm not moving",
    "working hard but slow", "kick from knees", "ankle flexibility kick", "dizzy flip turn",
]] + [("triathlon", q) for q in [
    "swim legs sink", "swim breathing panic", "swim struggling", "swim plateau",
    "total immersion", "swim technique help", "open water panic",
]]

# 一般游泳板是 swim（Swimming 是校隊板）；只收發文者自己發問／自述的分類，Re: 多為回答不收
PTT_BOARD = "swim"
PTT_KEEP_TAGS = ("[泳技]", "[問題]", "[請益]", "[心得]")


def _get_urllib(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Cookie": "over18=1"})
    try:
        return 200, urllib.request.urlopen(req, timeout=30).read()
    except urllib.error.HTTPError as e:
        return e.code, b""


def _get_curl(url: str) -> tuple[int, bytes]:
    """Reddit 對 Python urllib 一律回 429（用戶端指紋），curl 可正常取得。"""
    p = subprocess.run(["curl", "-s", "-A", UA, "-w", "\n%{http_code}", url],
                       capture_output=True, timeout=60)
    body, _, code = p.stdout.rpartition(b"\n")
    return int(code or 0), body


def fetch(url: str, gap: float, via_curl: bool = False) -> bytes:
    """GET with 429/5xx backoff; sleeps `gap` after every attempt to stay polite."""
    delay = gap
    for attempt in range(1, MAX_RETRY + 1):
        code, data = (_get_curl if via_curl else _get_urllib)(url)
        time.sleep(gap)
        if code == 200:
            return data
        if code not in (429, 500, 502, 503) or attempt == MAX_RETRY:
            raise RuntimeError(f"HTTP {code}")
        print(f"    {code}, retry {attempt} after {delay:.0f}s", flush=True)
        time.sleep(delay)
        delay *= 2
    raise RuntimeError("unreachable")


def load_done(path: Path) -> set:
    return set(path.read_text(encoding="utf-8").splitlines()) if path.exists() else set()


def load_ids(path: Path) -> set:
    if not path.exists():
        return set()
    return {json.loads(line)["id"] for line in path.read_text(encoding="utf-8").splitlines() if line}


def append(path: Path, rec: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def mark_done(path: Path, key: str) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(key + "\n")


def strip_html(s: str) -> str:
    s = re.sub(r"<br\s*/?>|</p>", "\n", html.unescape(s or ""))
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"submitted by .*", "", s, flags=re.S)
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", s)).strip()


def collect_reddit() -> None:
    out_dir = RAW / "reddit"
    out_dir.mkdir(parents=True, exist_ok=True)
    out, done_f = out_dir / "posts.jsonl", out_dir / "done_queries.txt"
    done, seen = load_done(done_f), load_ids(out)
    for sub, q in REDDIT_QUERIES:
        key = f"{sub}|{q}"
        if key in done:
            continue
        url = (f"https://www.reddit.com/r/{sub}/search.rss?q={urllib.parse.quote_plus(q)}"
               f"&restrict_sr=1&sort=relevance&t=all&limit=100")
        try:
            root = ET.fromstring(fetch(url, REDDIT_GAP_SEC, via_curl=True))
        except Exception as e:  # 單一查詢失敗不中斷整批，下次重跑會補
            print(f"FAIL {key}: {e}", flush=True)
            continue
        new = 0
        for e in root.findall("a:entry", ATOM):
            link = e.find("a:link", ATOM).get("href")
            m = re.search(r"/comments/([a-z0-9]+)/", link)
            if not m or m.group(1) in seen:
                continue
            body = strip_html(e.findtext("a:content", "", ATOM))
            seen.add(m.group(1))
            append(out, {
                "id": f"reddit.{m.group(1)}", "source": f"reddit/r/{sub}", "query": q,
                "url": link, "date": (e.findtext("a:updated", "", ATOM) or "")[:10],
                "title": e.findtext("a:title", "", ATOM), "body": body,
            })
            new += 1
        mark_done(done_f, key)
        print(f"{key}: +{new} (total {len(seen)})", flush=True)


def ptt_text(page: str) -> tuple[str, str]:
    """Return (date, body) from a PTT article page; body excludes header metadata, signature and pushes."""
    main = re.search(r'<div id="main-content"[^>]*>(.*?)<span class="f2">※ 發信站', page, re.S)
    raw = main.group(1) if main else ""
    date = re.search(r'時間</span><span class="article-meta-value">([^<]+)', raw)
    raw = re.sub(r'<div class="article-metaline.*?</div>', "", raw, flags=re.S)
    text = strip_html(raw)
    text = text.split("\n--\n")[0].strip()
    return (date.group(1).strip() if date else ""), text


def collect_ptt() -> None:
    out_dir = RAW / "ptt"
    out_dir.mkdir(parents=True, exist_ok=True)
    out, done_f = out_dir / "posts.jsonl", out_dir / "done_pages.txt"
    done, seen = load_done(done_f), load_ids(out)
    first = fetch(f"https://www.ptt.cc/bbs/{PTT_BOARD}/index.html", PTT_GAP_SEC).decode("utf-8", "replace")
    prev = re.search(r'href="/bbs/' + PTT_BOARD + r'/index(\d+)\.html">&lsaquo;', first)
    last_page = int(prev.group(1)) + 1 if prev else 1
    for n in range(last_page, 0, -1):
        key = f"index{n}"
        if key in done:
            continue
        try:
            page = fetch(f"https://www.ptt.cc/bbs/{PTT_BOARD}/index{n}.html", PTT_GAP_SEC).decode("utf-8", "replace")
        except Exception as e:
            print(f"FAIL {key}: {e}", flush=True)
            continue
        new = 0
        for href, title in re.findall(r'<a href="(/bbs/' + PTT_BOARD + r'/M\.[^"]+)">([^<]+)</a>', page):
            title = html.unescape(title).strip()
            aid = "ptt." + href.rsplit("/", 1)[1].removesuffix(".html")
            if aid in seen or not title.startswith(PTT_KEEP_TAGS):
                continue
            try:
                art = fetch("https://www.ptt.cc" + href, PTT_GAP_SEC).decode("utf-8", "replace")
            except Exception as e:
                print(f"  FAIL {aid}: {e}", flush=True)
                continue
            date, body = ptt_text(art)
            seen.add(aid)
            append(out, {"id": aid, "source": f"ptt/{PTT_BOARD}", "url": "https://www.ptt.cc" + href,
                         "date": date, "title": title, "body": body})
            new += 1
        mark_done(done_f, key)
        print(f"{key}: +{new} (total {len(seen)})", flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    {"reddit": collect_reddit, "ptt": collect_ptt}[sys.argv[1]]()
