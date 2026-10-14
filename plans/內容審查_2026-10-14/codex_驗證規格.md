# codex 驗證規格：Vortex 內容審查 Phase 2

## ⚠️ 執行指令（最重要）

**立即執行，不要輸出計畫，不要等確認，不要問「需要調整嗎」。沒有修改檔案、沒有寫出紀錄檔，就算失敗。**

**禁止任何 git 操作**：不准 commit、reset、checkout、stash、pull、rebase、clean、restore。只能編輯下面指定的檔案。

## 背景

`C:\claudehome\projects\TheVortexProject` 是一個游泳教學知識庫，`canonical/` 底下的 YAML 會公開上網站。MiniMax 已經先讀過一輪，在 `plans/內容審查_2026-10-14/初讀/<檔名>.md` 列出「可疑點」（finding）。這些只是可疑點，可能是對的，也可能是 MiniMax 捏造的。

你的工作：對指定的每一份初讀檔，**逐條第一手驗證**，決定改或不改，然後直接修改對應的 canonical YAML。

## 每條 finding 怎麼處理

1. 在目標 YAML 找到 finding 說的原文（`grep`）。原文找不到，就判「駁回：原文不存在」。
2. 判斷類型，照下面處理：
   - **內部矛盾／事實錯誤／算術錯誤／單位錯誤**：自己讀上下文、計算、查原始文獻後判定。
   - **文獻數字或歸屬**：讀原始文獻摘要或全文，取得方式見下一節。
     - 只說「請查證」、沒指出具體問題，而且 `canonical/_sources.yaml` 裡該來源是 `verification_status: verified`：判「駁回：來源已驗證、finding 未指出具體矛盾」。
     - 指出了具體問題，或來源是 unverified：去讀原文。
   - **安全主張**：判準是「哪一種行為」危險，不是地點粗分。不得把正常訓練寫成危險，也不得漏寫真正危險的條件組合。
   - **確定性標記**：判準是 🟢＝約 2010 年後的文獻、🟡＝約 2010 年前的文獻、🔵＝物理或解剖推導、🟠＝教練實務觀察、🔴＝待查。
   - **population_notes 的 null**：null 代表原研究沒有拆分，一律駁回。
3. 結果只能是三種之一：
   - **修**：直接改 YAML。
   - **駁回**：寫出證偽依據。
   - **待查**：原文取不到，而且句子是高風險的具體數字或醫療主張。在句中加註「（本庫來源未涵蓋，待查證）」，或把數字改成定性描述。

## 取原文的方法（PubMed 網頁會擋，只能用這兩個 API）

- PubMed 摘要：`curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text"`
- PMC 全文：`curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML"`
- 用 DOI 或關鍵字查：`curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<查詢>&resultType=core&format=json"`
- PMID、PMCID、DOI 先從 `canonical/_sources.yaml` 對應的 `src.*` 條目找。

## 修改規則

- 只改「有問題的那一句」，其他文字保持原樣。YAML 的縮排和引號照原檔風格。
- 數字只能改成原文寫的值。原文沒有的數字不准自己補，寧可改成定性描述。
- 不得在文字裡寫 `src.xxx`、PMID 這類機器鍵；引用寫成「作者 年份」。
- health 的真相源是 `canonical/health/drafts/*.yaml`，**不要改 `canonical/health/injuries.yaml`**。改完執行 `python tools/build_injuries.py`。
- 每一份檔改完執行 `python tools/validate.py`，最後一行必須是 `[RESULT] PASS`。出現 ERROR 就修到過為止。

## 紀錄（必寫，每份檔處理完立刻寫入，不要等全部做完）

寫到 `plans/內容審查_2026-10-14/codex紀錄/<初讀檔同名>.md`，格式：

```
### <finding 編號或標題>
- 判定：修／駁回／待查
- 依據：如果讀了原文，**逐字貼出原文中支撐判定的那一句英文**，並註明 PMID 或 PMCID；如果是推導或計算，寫出算式
- 改動：原句 → 新句（駁回寫「無」）
```

最後一行寫：`修 N／駁回 N／待查 N`。

## 本次範圍

處理本 prompt 最後列出的初讀檔，一份一份依序做。
