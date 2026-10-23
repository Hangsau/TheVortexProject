#!/usr/bin/env python3
"""研究筆記登錄表（Research/_notes.yaml）的完整性檢查。

登錄表是研究筆記的唯一真相來源：my-site 的 sync_vortex.py 依它決定哪些筆記上網站、
放在哪個主題、排第幾、卡片寫什麼，「研究結論一覽」頁也由它的 findings 生成。
所以這裡擋的是「網站會無聲出錯」的情況：

* Research/、Observations/ 底下有 .md 沒登錄（新筆記寫了卻沒上網站，也沒說為什麼不上）
* 登錄的檔案不存在、slug 重複、主題沒宣告
* 卡片摘要是內部頁首（建立日期／dossier／定位：）而不是結論
* graduated_to 指向不存在的知識點、open_questions 指向不存在的開放問題

用法：python tools/check_notes.py      有錯 exit 1
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "Research"
OBSERVATIONS = ROOT / "Observations"
REGISTRY = RESEARCH / "_notes.yaml"
CONTENT_INDEX = ROOT / "indices" / "content_index.json"
FUTURE_RESEARCH = ROOT / "FUTURE_RESEARCH.md"

KINDS = {"analysis", "literature", "observation"}
STATUSES = {"researching", "graduated", "retracted"}
CERTAINTIES = {"🔵", "🟢", "🟡", "🟠", "🔴"}
ROLES = {None, "overview"}
BANNED_SUMMARY_PREFIXES = ("建立日期", "整合日期", "dossier", "Dossier", "定位", "主題：", "狀態")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _resolve(rel: str) -> Path:
    return (RESEARCH / rel).resolve()


def _content_ids() -> set[str]:
    data = json.loads(CONTENT_INDEX.read_text(encoding="utf-8"))
    return {r["id"] for r in data["records"] if "id" in r}


def _question_ids() -> set[str]:
    """FUTURE_RESEARCH.md 的「### 0.10 標題」→ fq.0.10。"""
    text = FUTURE_RESEARCH.read_text(encoding="utf-8")
    return {f"fq.{m}" for m in re.findall(r"^### (\d+(?:\.\d+)+)\s", text, re.M)}


def check(registry: dict, content_ids: set[str], question_ids: set[str]) -> list[str]:
    errors: list[str] = []

    themes: set[str] = set()
    group_keys: set[str] = set()
    overview_of: set[str] = set()
    for g in registry.get("groups") or []:
        if g.get("key") in group_keys:
            errors.append(f"group 重複：{g.get('key')}")
        group_keys.add(g.get("key"))
        for t in g.get("themes") or []:
            if t.get("key") in themes:
                errors.append(f"theme 重複：{t.get('key')}")
            themes.add(t.get("key"))
            if not t.get("name_zh"):
                errors.append(f"theme {t.get('key')} 缺 name_zh")

    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    seen_order: set[tuple[str, int]] = set()
    covered: set[Path] = set()
    for n in registry.get("notes") or []:
        nid = n.get("id", "<無 id>")
        if nid in seen_ids:
            errors.append(f"{nid}：id 重複")
        seen_ids.add(nid)

        slug = n.get("slug", "")
        if not SLUG_RE.match(slug):
            errors.append(f"{nid}：slug 不合格式「{slug}」")
        if slug in seen_slugs:
            errors.append(f"{nid}：slug 重複「{slug}」")
        seen_slugs.add(slug)

        path = _resolve(n.get("path", ""))
        if not path.is_file():
            errors.append(f"{nid}：檔案不存在 {n.get('path')}")
        covered.add(path)

        role = n.get("role")
        if role not in ROLES:
            errors.append(f"{nid}：role「{role}」不合法")
        if role == "overview":
            # 總覽掛在主題或大類上，每個只能有一篇；不編號、不必有 findings
            if n.get("theme") not in themes | group_keys:
                errors.append(f"{nid}：總覽的 theme「{n.get('theme')}」不是已宣告的主題或大類")
            if n.get("theme") in overview_of:
                errors.append(f"{nid}：「{n.get('theme')}」已經有一篇總覽")
            overview_of.add(n.get("theme"))
        else:
            if n.get("theme") not in themes:
                errors.append(f"{nid}：theme「{n.get('theme')}」未在 groups 宣告")
            key = (n.get("theme"), n.get("order"))
            if not isinstance(n.get("order"), int):
                errors.append(f"{nid}：order 必須是整數")
            elif key in seen_order:
                errors.append(f"{nid}：同主題 order 重複 {key}")
            seen_order.add(key)

        if n.get("kind") not in KINDS:
            errors.append(f"{nid}：kind「{n.get('kind')}」不合法")
        if n.get("status") not in STATUSES:
            errors.append(f"{nid}：status「{n.get('status')}」不合法")
        if "public" in n and not isinstance(n["public"], bool):
            errors.append(f"{nid}：public 必須是 true／false")

        summary = (n.get("summary_zh") or "").strip()
        if not summary:
            errors.append(f"{nid}：summary_zh 空白")
        elif summary.startswith(BANNED_SUMMARY_PREFIXES):
            errors.append(f"{nid}：summary_zh 是內部頁首不是結論「{summary[:12]}…」")

        findings = n.get("findings") or []
        if not findings and role != "overview":
            errors.append(f"{nid}：沒有 findings")
        for i, f in enumerate(findings, 1):
            if not (f.get("text_zh") or "").strip():
                errors.append(f"{nid}：finding {i} 缺 text_zh")
            if f.get("certainty") not in CERTAINTIES:
                errors.append(f"{nid}：finding {i} certainty「{f.get('certainty')}」不合法")

        graduated = n.get("graduated_to") or []
        if n.get("status") == "graduated" and not graduated:
            errors.append(f"{nid}：status 是 graduated 但 graduated_to 空白")
        for cid in graduated:
            if cid not in content_ids:
                errors.append(f"{nid}：graduated_to「{cid}」不是存在的知識點 ID")
        for q in n.get("open_questions") or []:
            if q not in question_ids:
                errors.append(f"{nid}：open_questions「{q}」在 FUTURE_RESEARCH.md 找不到")

    excluded_dirs: list[Path] = []
    for item in registry.get("non_public") or []:
        rel = item.get("path", "")
        target = _resolve(rel)
        if not item.get("reason"):
            errors.append(f"non_public {rel}：缺 reason")
        if rel.endswith("/"):
            if not target.is_dir():
                errors.append(f"non_public {rel}：資料夾不存在")
            excluded_dirs.append(target)
        else:
            if not target.is_file():
                errors.append(f"non_public {rel}：檔案不存在")
            covered.add(target)

    for base in (RESEARCH, OBSERVATIONS):
        for md in sorted(base.rglob("*.md")):
            md = md.resolve()
            if md in covered or any(d in md.parents for d in excluded_dirs):
                continue
            errors.append(f"未登錄：{md.relative_to(ROOT)}（加進 notes 或 non_public）")

    return errors


def main() -> int:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    errors = check(registry, _content_ids(), _question_ids())
    notes = registry.get("notes") or []
    public = sum(1 for n in notes if n.get("public", True))
    if errors:
        print(f"研究筆記登錄表：{len(errors)} 個錯誤")
        for e in errors:
            print(f"  ✗ {e}")
        return 1
    print(f"研究筆記登錄表 OK：{len(notes)} 篇登錄（{public} 篇公開）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
