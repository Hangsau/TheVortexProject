# 研究報告索引

> 存放位置：`~/.claude/research/`（持久，不會被 OS 清掉）
> 命名格式：`<topic>-<YYYY-MM-DD>.md`
> 原始 workflow 輸出：`/tmp/claude-1002/.../tasks/<id>.output`（會被 OS 清掉，但已整理成本 Markdown）

---

## 2026-06-20

| 報告 | 問題 | 一句話結論 |
|------|------|----------|
| [swimming-dryland-vs-water-2026-06-20.md](./swimming-dryland-vs-water-2026-06-20.md) | 游泳比賽決勝負是水中還是陸地訓練？ | 兩者並非二選一——水中是基礎主體，陸地是出發/轉身/衝刺的加成器 |
| [swimming-water-training-breakthroughs-2026-06-20.md](./swimming-water-training-breakthroughs-2026-06-20.md) | 水中訓練到天花板了嗎？有什麼新突破？ | 框架沒翻轉，但海豚踢姿態、RPE 監測、VHL/RSH 缺氧訓練是三條新槓桿 |

---

## 使用方式

- 讀 Markdown：任何文字編輯器、`cat`、`less`、`glow`、`bat` 都可
- 全文搜尋：`grep -r "<關鍵字>" ~/.claude/research/`
- 重新跑研究：給 Claude 下 `deep-research <新問題>`，再要求「輸出到 ~/.claude/research/」
- 匯出成 PDF / HTML：用 `pandoc <file>.md -o <file>.pdf` 或 `pandoc <file>.md -o <file>.html`

## 清理政策

- 已驗收的研究 → 保留
- 草稿/未確認的研究 → 不放這裡
- 純 raw JSON output → `/tmp/`（會被 OS 清掉）