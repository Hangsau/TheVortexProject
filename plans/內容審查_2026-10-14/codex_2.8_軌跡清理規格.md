# codex 規格：2.8 公開正文審查軌跡清理

## ⚠️ 執行指令（最重要）

**立即執行，不要輸出計畫，不要等確認。沒有修改檔案、沒有寫紀錄，就算失敗。**

**禁止任何 git 操作**：commit、reset、checkout、stash、pull、rebase、clean、restore 一律不准。

## 背景

`C:\claudehome\projects\TheVortexProject` 的 canonical YAML 會公開上網站。有約 60 處讀者看得到的文字夾著審查軌跡，例如「（2026-09-04 更正：原寫 X，經查…）」「見錯誤 32」。修訂史已經另外收在研究庫的審查紀錄裡，公開正文只應寫最終說法。

找出所有位置：先跑 `python tools/validate.py`，再看 `reports/validation_report.md` 的 **W029** 段，每一筆都列出檔案和欄位路徑。

## 每一處怎麼改

1. 讀懂那句更正在說什麼，把它分成兩部分：
   - **最終說法**：現在正確的陳述。如果帶有讀者需要知道的限定，例如「只涵蓋男子項目」「樣本只有 14 人」「是敘事綜述、不是系統性回顧」，一定要保留。
   - **修訂史**：「原寫 X」「2026-09-04 更正」「經查」「見錯誤 N」這類話。
2. 把公開欄位改成只寫最終說法：不帶日期，不帶「原寫」，不帶錯誤編號。限定要改寫成自然的陳述句。
3. 修訂史不可以直接丟掉，要搬到不公開的欄位：
   - `canonical/health/drafts/*.yaml`：在同一個區塊加 `maintenance_note: "<修訂史原文>"`。sync 在任何層級都會剝掉這個欄位。
   - 其他檔（technical-analysis、teaching-errors、l-indicators、periodization、psychology、movement）：**只能**把 `maintenance_note` 放在條目的最外層，也就是和 `id` 同一層、`public` 之外。**絕不可以**放進 `public:` 底下，否則會上網站。
   - `references[].citation` 或 `sources` 裡的更正，例如「（2026-09-04 更正：只涵蓋男子項目）」：citation 改成乾淨的書目，加上必要的限定（例如「只涵蓋男子項目」）；修訂史一樣搬到條目最外層的 `maintenance_note`。
4. 不要改其他文字；不要動數字，除非更正本身就是在改那個數字，這時候保留更正後的值。
5. YAML 縮排和折行風格照原檔。

## 驗收（每改完一個檔就跑）

- `python tools/build_injuries.py`（只有改了 health drafts 才要跑）
- `python tools/validate.py`：最後一行必須是 `[RESULT] PASS`，**W029 筆數只能往下降**。
- 全部改完時，W029 應為 0。如果有判斷不了的，W029 可以留著，但要寫進紀錄說明原因。

## 紀錄

每個檔處理完，立刻追加到 `plans/內容審查_2026-10-14/codex紀錄/2.8_軌跡清理.md`：

```
### <檔案>｜<條目 id>｜<欄位>
- 原句：…
- 新句：…
- 修訂史搬到：<條目 id>.maintenance_note
```

最後一行寫：`清理 N 處／保留 N 處（原因）`。
