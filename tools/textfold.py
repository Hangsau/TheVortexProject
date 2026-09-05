#!/usr/bin/env python3
"""
textfold.py — 接掉 YAML 摺疊純量（`>-`）在中文句子中間留下的折行空白。

為什麼需要：YAML 規範把 `>-` 的每個折點接成一個空白，那是為「空白分詞」的語言
訂的規則。中文沒有詞間空白，所以 canonical 每一次為了可讀而折行，下游拿到的字串
就會在句子中間多一個空格。canonical 那邊的折行是對的（好讀、好 diff），要接的是
輸出端——my-site 的 `sync_vortex.py` 已經在 `dump_yaml()` 接掉了，這裡是同一套
規則給 Vortex 自己的產出物（`indices/*.json`、`KNOWLEDGE_MAP.md`）用。

不接的話症狀很鈍：檔案看起來完全正常，只有「跨折點的片語 grep 不到」——搜
「感知系統的輸出」找不到，因為實際存的是「感知系統的 輸出」。單詞搜尋沒事，所以
會拖很久才被發現。

**兩邊的正規表示式必須保持一致**。改這裡就要改 my-site 的 `tools/sync_vortex.py`，
反之亦然。
"""
from __future__ import annotations

import re

# 只在「空白兩側都是漢字、假名或中文標點」時接掉。全形符號兩側的空白（例如
# `可見方向 ＋ 解剖動作`）是作者有意的排版，所以 ＋＝＜＞ 這類不列入字元集。
_CJK = (
    "㐀-䶿一-鿿"      # 漢字
    "぀-ヿ"                   # 假名
    "、-〃〈-】〔-〟"  # 、。〈〉《》「」『』【】〔〕
    "！（），．：；？"  # ！（），．：；？
)
_CJK_FOLD_SPACE = re.compile("(?<=[" + _CJK + "]) (?=[" + _CJK + "])")

# 破折號與刪節號要單獨處理：中文的 `——`／`…` 一律成對且兩側不留空白，所以緊鄰
# 它們的空白必定是折點。**只認成對的 `——`**——單一 `—` 在本庫是有意的分隔符
# （`頭帶平衡 — 面朝下`），把它兩側的空白接掉會改掉作者的排版。
_CJK_FOLD_DASH = re.compile(
    "(?<=——) (?=[" + _CJK + "])|(?<=[" + _CJK + "]) (?=——)"
    "|(?<=…) (?=[" + _CJK + "])|(?<=[" + _CJK + "]) (?=…)"
)


def unfold_cjk(value):
    """遞迴移除 CJK 折行空白；非字串（含 dict／list 的鍵）原樣回傳。"""
    if isinstance(value, str):
        return _CJK_FOLD_DASH.sub("", _CJK_FOLD_SPACE.sub("", value))
    if isinstance(value, dict):
        return {k: unfold_cjk(v) for k, v in value.items()}
    if isinstance(value, list):
        return [unfold_cjk(v) for v in value]
    return value
