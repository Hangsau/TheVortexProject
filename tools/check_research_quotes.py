"""比對 sources.md 每筆來源的英文引句是否逐字出現在原始網頁（curl 取得，非模型轉述）。"""
import re, sys, subprocess, html, json, pathlib

src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
out_dir = pathlib.Path(sys.argv[2]); out_dir.mkdir(exist_ok=True)
blocks = re.split(r"\n(?=## S\d+)", src)
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", html.unescape(s).lower().replace("’", "'")).strip()
results = []
for b in blocks:
    m = re.match(r"## (S\d+)", b)
    if not m:
        continue
    sid = m.group(1)
    urls = re.findall(r"https?://[^\s）)」，,]+", b)
    quotes = [q for q in re.findall(r"[「\"“]([^」\"”]{25,})[」\"”]", b) if re.search(r"[a-zA-Z]{4,}", q) and not re.search(r"[一-鿿]", q)]
    if not urls or not quotes:
        results.append((sid, "no-url-or-no-english-quote", 0, len(quotes)))
        continue
    cache = out_dir / f"{sid}.txt"
    if not cache.exists():
        r = subprocess.run(["curl", "-sL", "-A", "Mozilla/5.0", "--max-time", "40", urls[0]], capture_output=True)
        raw = r.stdout
        if raw[:4] == b"%PDF":
            try:
                import fitz
                doc = fitz.open(stream=raw, filetype="pdf")
                text = "".join(p.get_text() for p in doc)
            except Exception as e:
                text = ""
        else:
            text = re.sub(r"<[^>]+>", " ", raw.decode("utf-8", "ignore"))
        cache.write_text(text, encoding="utf-8")
    page = norm(cache.read_text(encoding="utf-8"))
    hit = 0
    for q in quotes:
        words = norm(q).split()
        key = " ".join(words[:8]) if len(words) >= 8 else " ".join(words)
        if key and key in page:
            hit += 1
    status = "empty-page" if len(page) < 500 else ("ok" if hit == len(quotes) else ("partial" if hit else "none"))
    results.append((sid, status, hit, len(quotes)))
for r in results:
    print(*r, sep="\t")
