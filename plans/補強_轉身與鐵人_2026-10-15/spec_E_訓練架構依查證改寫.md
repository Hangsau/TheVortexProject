# 派工規格 E：依外部查證改寫鐵人訓練架構（open-water.tech.14–19）

> 立即執行，不要只輸出計畫。工作目錄 `C:\claudehome\projects\TheVortexProject`。禁止任何 git 操作；不碰 `tools/map_learner_speech.py`。

## 輸入
- `Research/鐵人泳訓/verdicts.md`（H1–H10 判定、P1–P8、「對出課表的影響」）與 `sources.md`（S01–S26，含引文）。只用這兩份裡已標「全文已讀: 是」的來源，**不再上網搜尋**。
- 現有條目：`canonical/instructional/technical-analysis.yaml` 的 `open-water.tech.14`～`tech.19`（目前全是 🔵 推導）。

## 要做
1. **來源登錄**：把要引用的全文已讀來源登錄進 `canonical/_sources.yaml`（`src.<slug>`；type 用 journal-article／web-article／forum-thread 之一，若 taxonomy 不允許 forum-thread，先查 `_sources.yaml` 既有 type 值選最接近的並在 notes 註明是論壇討論串；含 title、作者或機構、year、identifier.url 或 doi、retrieved_on: 2026-10-15、verification_status: verified、notes 寫證據類型與族群）。
2. **逐條改寫 tech.14–19**，依判定：
   - 推論被支持或部分支持：保留 `mechanism`（🔵），新增 `evidence:` 清單，每筆含 `certainty`、`text`、`source_ids`。**🟢 只給研究類**；實務文件與社群討論用 🔵 並在 text 開頭明寫「實務文件：」或「論壇討論：」，不得寫「研究顯示」。
   - 被反對、意見分歧或無資料的部分：改寫內文，明說分歧或缺口（例：長連續游，實務與論壇意見分歧，列兩方理由；鐵人專屬強度分布、乳酸耐受比例、開放水域配速換算、鐵人專屬減量：目前沒有可讀全文的資料）。
   - 有出處的課表參數寫進 `practical_implication`（附來源人名或機構，例如「Triathlon Magazine Canada 教練文章建議…」），範圍照 verdicts 原文，**不自補數字**；單一來源要寫明是單一計畫或單一教練。
   - 菁英跟游賽（H4）：引 Landers 2008（S01）的首群出水結果，訓練組成仍標無資料。
3. 使用者規則：沒有依據不准自訂數字上限或處方。
4. 散文欄位不得出現 `src.*` 機器鍵；修訂史不寫進 public（W029）。

## 完成前
- `python -X utf8 tools/validate.py` 0 ERROR，不新增 W009／W011／W028／W029。
- `python tools/build_knowledge_map.py`、`python tools/build_indices.py`、`python -m unittest discover tests` 全過。
- 寫 `plans/補強_轉身與鐵人_2026-10-15/E_完成紀錄.md`：每條改了什麼、引了哪些來源、還剩哪些缺口。最終回覆附同樣摘要。
