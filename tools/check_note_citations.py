#!/usr/bin/env python3
"""研究筆記引用核對：把公開筆記裡的 DOI／PMID／PMCID 逐筆查回書目，挑出對不上的。

2026-10-23 第一次全面跑：395 筆識別碼裡，彈性蓄能一篇 7 筆全部是假的、自然頻率的核心
引用對不上，心理層有 8 筆 DOI／PMID 指到別篇論文（canonical 的來源註冊表早已改正，
研究筆記沒跟上）。網路摘要與模型記憶裡的識別碼都不可信，寫進筆記前要能查回原篇。

* DOI → Crossref；PMID／PMCID → Europe PMC（PubMed 網頁有 cookie 閘，工具抓不到）
* 判定「可疑」：查不到；或查到的標題、第一作者都沒出現在筆記那一行（啟發式，
  會有誤報——那一行只寫中文描述時也會被挑出來——結果要人工看）
* 連線失敗另列「連線失敗」，不算成假引用；重跑即可
* 結果寫 reports/note_citations.md；有「查不到」不讓 exit 0（「可疑」要人工看，不擋）

用法：python tools/check_note_citations.py [--slug <筆記 slug>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "Research"
REPORT = ROOT / "reports" / "note_citations.md"

DOI_RE = re.compile(r"10\.\d{4,9}/[A-Za-z0-9.\-_;:/()<>]+")
PMID_RE = re.compile(r"PMID[:：\s]*(\d{6,9})")
PMC_RE = re.compile(r"PMC(\d{6,8})")
RETRIES = 4                # 429 限流時重試次數，每次多等 RETRY_WAIT_S 秒
RETRY_WAIT_S = 10
TIMEOUT_S = 30
POLITE_DELAY_S = 0.2       # 每筆查詢之間的間隔，避免被 Crossref 限流
MIN_SURNAME_LEN = 3        # 太短的姓氏（如 Li）容易在句子裡誤中，不拿來比
MIN_TITLE_WORD_HITS = 2    # 標題裡至少要有幾個實詞出現在那一行
NETWORK_ERROR = "<連線失敗>"
STOP = set("the and with from that this into during between effect effects study analysis "
           "among using their versus over after under through review".split())


class Resolver:
    def __init__(self):
        self.cache: dict[str, str | None] = {}

    def _get(self, url: str):
        """回傳 JSON；查無此書目回 None；網路問題回 NETWORK_ERROR（不能當成假引用）。"""
        for attempt in range(RETRIES):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "vortex-note-citations/1.0"})
                with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(RETRY_WAIT_S * (attempt + 1))
                    continue
                return None if e.code == 404 else NETWORK_ERROR
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
                return NETWORK_ERROR
        return NETWORK_ERROR

    def doi(self, doi: str) -> str | None:
        key = "doi:" + doi
        if key not in self.cache:
            j = self._get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/()"))
            if j == NETWORK_ERROR:
                return NETWORK_ERROR  # 不快取，重跑時再查
            m = j and j.get("message")
            self.cache[key] = (f"{(m.get('title') or [''])[0]} | {(m.get('author') or [{}])[0].get('family', '')}"
                               if m else None)
            time.sleep(POLITE_DELAY_S)
        return self.cache[key]

    def epmc(self, query: str) -> str | None:
        key = "epmc:" + query
        if key not in self.cache:
            j = self._get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&query="
                          + urllib.parse.quote(query))
            if j == NETWORK_ERROR:
                return NETWORK_ERROR
            r = j and j["resultList"]["result"]
            self.cache[key] = (f"{r[0]['title']} | {r[0].get('authorString', '').split(',')[0].split(' ')[0]}"
                               if r else None)
            time.sleep(POLITE_DELAY_S)
        return self.cache[key]


def clean_doi(raw: str) -> str:
    raw = raw.rstrip(".。,;)")
    # 括號只保留成對的（例如 0191-8869(93)90113-H）
    while raw.count(")") > raw.count("("):
        raw = raw[: raw.rindex(")")]
    return raw


def matches(title_author: str, line: str) -> bool:
    title, _, family = title_author.partition(" | ")
    low = line.lower()
    if family and len(family) >= MIN_SURNAME_LEN and family.lower() in low:
        return True
    words = [w for w in re.findall(r"[A-Za-z]{5,}", title.lower()) if w not in STOP]
    return sum(w in low for w in words) >= MIN_TITLE_WORD_HITS


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="只查這一篇")
    args = ap.parse_args()
    reg = yaml.safe_load((RESEARCH / "_notes.yaml").read_text(encoding="utf-8"))
    res = Resolver()
    rows = []
    for n in reg["notes"]:
        if not n.get("public", True) or (args.slug and n["slug"] != args.slug):
            continue
        text = (RESEARCH / n["path"]).resolve().read_text(encoding="utf-8")
        for ln, line in enumerate(text.split("\n"), 1):
            idents = [("DOI " + clean_doi(d), res.doi(clean_doi(d))) for d in set(DOI_RE.findall(line))]
            idents += [("PMID " + p, res.epmc(f"EXT_ID:{p} AND SRC:MED")) for p in set(PMID_RE.findall(line))]
            idents += [("PMC" + p, res.epmc(f"PMCID:PMC{p}")) for p in set(PMC_RE.findall(line))]
            for ident, found in idents:
                if found == NETWORK_ERROR:
                    rows.append(("連線失敗", n["slug"], ln, ident, "", line.strip()))
                elif found is None:
                    rows.append(("查不到", n["slug"], ln, ident, "", line.strip()))
                elif not matches(found, line):
                    rows.append(("可疑", n["slug"], ln, ident, found, line.strip()))
    REPORT.parent.mkdir(exist_ok=True)
    count = {k: sum(r[0] == k for r in rows) for k in ("查不到", "可疑", "連線失敗")}
    out = ["# 研究筆記引用核對", "", f"查不到 {count['查不到']} 筆、可疑 {count['可疑']} 筆、連線失敗 {count['連線失敗']} 筆（重跑即可）。"
           "「可疑」是啟發式（查到的標題與第一作者都沒出現在那一行），多數是那一行只寫中文描述的誤報，要人工判斷。", ""]
    for kind, slug, ln, ident, found, line in rows:
        out.append(f"- **{kind}** `{slug}`:{ln} {ident} → {found or '—'}  \n  {line[:200]}")
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"查不到 {count['查不到']}、可疑 {count['可疑']}、連線失敗 {count['連線失敗']} → {REPORT.relative_to(ROOT)}")
    return 1 if any(r[0] == "查不到" for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
