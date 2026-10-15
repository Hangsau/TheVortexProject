# E 完成紀錄：鐵人訓練架構依查證改寫（open-water.tech.14–19）

驗證：`validate.py` 0 ERROR（WARN 147，與動工前相同；W009／W011／W028／W029 皆 0）；`build_knowledge_map.py`、`build_indices.py` 已重生；`unittest` 255 項全過。

## 來源登錄（canonical/_sources.yaml，新增 17 筆，皆 verified，retrieved_on 2026-10-15）
- 研究（2）：landers-2008-swim-positioning-triathlon、selles-perez-2019-polarized-pyramidal-half-ironman
- 實務文件（11）：heggy-2021、newsome-2025（Swim Smooth）、mackinnon-2024、bernhardt-12-week-sprint-swim-plan、hayes-2018（220 Triathlon）、slaughter-2019、laughlin-2016、petrie-2025、filliol-2015、bernhardt-workout-placement-recovery（二手轉述 9 人研究）、triathlon-magazine-canada-2012-open-water-tips
- 論壇討論串（4）：slowtwitch 減量、泳訓量、賽前最長游、最長連續組。分類法沒有 forum-thread，選 web_article，notes 與 evidence text 開頭都註明是論壇討論串。
- 未登錄：S04、S05、S08、S11、S13、S14、S17、S19（只讀摘要）、S26。

## 逐條改了什麼
- **tech.14**：摘要改成「推導，不是量測」，新增 3 筆 evidence（Landers 2008 首群出水，🟢；Heggy 技術優先、Slaughter 短距離仍速度耐力並重，皆 🔵 實務文件）。practical 明說能量需求無全文研究、短距離說法分歧。
- **tech.15**：新增 1 筆 evidence（Bernhardt 轉述 9 人研究，🔵 實務文件，註明樣本小、原研究未讀）。practical 降為「可選排法」；「衝擊小」「全週疲勞」標無出處。
- **tech.16**：標題與摘要改寫，不再斷言「乳酸耐受降到少量」；新增 5 筆 evidence（Slaughter 依賽距、Heggy 與 Hayes 的衝刺插入、Swim Smooth CSS 每 4–6 週重測且無鐵人換算、Selles-Perez 2019 全項目分布非泳段，🟢、Landers 首群出水且訓練組成無資料，🟢）。
- **tech.17**：標題改為意見分歧；摘要列支持與反對雙方；新增 5 筆 evidence（Hayes 計畫最長 OW 2.5 km 對 1.5 km 賽距；Laughlin／Mackinnon 反對；三則論壇討論串）。「不是恢復課」標明無直接出處，屬負荷推導。
- **tech.18**：摘要與 practical 改為各教練範圍並附人名（Mackinnon 2／3／4+ 堂與 45–60 分、Slaughter ≥3 堂、Hayes 2–4 堂與 sprint −30%／70.3 +30%、Bernhardt 初學 2 堂一強一輕、Filliol 單一菁英約 5 堂各 4–5 km）；新增 4 筆 evidence。「一堂一目的」標無直接出處。
- **tech.19**：新增 4 筆 evidence（Petrie 週期與減量最後兩週且非泳段專屬、Hayes 計畫後半每週兩次 OW、Slowtwitch 減量討論串、開放水域提示文章）。practical 加上有出處的單一參考並列缺口。

## 剩餘缺口（條目內已明寫）
- 泳段專屬強度分布、乳酸耐受與速耐比例、純速劑量：無全文資料（Cejuela 2023、Casado 2021 全文未取得）。
- 菁英跟游短距離賽的訓練組成：無資料（Landers 2008 只有位置結果）。
- 鐵人專屬 CSS 到開放水域配速換算：無（Swim Smooth 明言）。
- 泳段專屬減量降幅與天數：只有論壇個人說法與整體鐵人「最後兩週」。
- 防寒衣練習次數與起始時間；初學者技術時間占比；各賽距每週總量：無出處。
- 長連續游：實務與論壇互相矛盾，未寫成通則。
- 游泳作為跑步後恢復：僅單一 9 人研究的二手轉述，原研究未讀。
