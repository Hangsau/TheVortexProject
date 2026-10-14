# 三層歸屬稽核報告（Phase 1）

> 由 `tools/audit_layers.py` 產生；drift 基準 `27ffd10^`。數字是 Phase 3 閘門分母。

## 摘要

| 檢查 | 筆數 |
|---|---|
| 已發布 Vortex 頁（不含轉址） | 820 |
| 無歸屬頁 | 0 |
| P1 散文頁 | 0 |
| P3 my-site 手管／手寫頁 | 1 |
| P1 漂移候選：呈現／應用層（閘門，須為 0） | 0 |
| 漂移：研究庫凍結底稿（已加凍結說明，僅供參考） | 49 |
| P2 公開頁含診斷語的頁 | 0（共 0 處） |
| 機器鍵外洩頁 | 2 |
| 外站連結 | 0 |
| 🟢／🟡 但同行無年份（呈現層散文／手管） | 7 |

## W1.1 頁面 → 層

| 目標層 | 頁數 |
|---|---|
| 呈現 | 723 |
| 應用 | 78 |
| 資料庫 | 19 |

| 來源種類 | 頁數 |
|---|---|
| canonical | 795 |
| my-site 手寫 | 1 |
| my-site 版型 | 2 |
| 工具 | 2 |
| 散文 | 1 |
| 散文（研究底稿） | 19 |

**無歸屬頁**：無

**P3 頁**：`water-sense`

**P4 頁**：`workout`、`workout-studio`

## W1.2 散文漂移候選

句段在 canonical 的修訂中被刪除、現行 canonical 已無，但仍出現在散文或手管資料。屬「候選」：改寫同義、或散文本就另有語境者需人工判定。

| 檔案 | 句段 | 原 canonical 檔 |
|---|---|---|

## W1.3 公開頁診斷語

| 頁 | 命中 |
|---|---|

## W1.4 機器鍵／外站連結／確定性無年份

**機器鍵外洩**

- `movement`：cross_ref
- `tech/udk-tech-14`：cross_ref

**外站連結**

- 無

**🟢／🟡 同行無年份**

| 檔案 | 行 | 內容 |
|---|---|---|
| `my-site/next/content/vortex/water-sense.md` | 37 | ### 神經科學層次 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 78 | ### 學習水感的四個能力階段 🟡 |
| `my-site/next/content/vortex/water-sense.md` | 177 | ### SWOLF：最實用的無儀器效率指標 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 192 | ### SPL（每趟划手數） 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 227 | ### 1. 製造大誤差，而非漸進微調 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 237 | ### 2. 交替練習，而非連續練習 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 249 | ### 4. 暫時回到認知學習階段 🟡 |
