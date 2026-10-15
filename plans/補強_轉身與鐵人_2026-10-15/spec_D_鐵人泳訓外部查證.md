# 研究規格 D：鐵人泳段訓練架構——外部查證＋出課表參數蒐集

> 立即執行。不要只輸出計畫。每讀完一個來源就把紀錄 append 進輸出檔（撞到額度只損失進行中那一筆）。
> 工作目錄：`C:\claudehome\projects\TheVortexProject`。輸出目錄：`Research/鐵人泳訓/`（新建）。
> 禁止 git 寫入操作。不改 canonical/、Drills/（那是下一步，由派工方依本研究決定）。

## 0. 證據規則（使用者明令）

- **只採讀到全文的來源**。摘要、搜尋結果摘要、二手轉述都不算證據，只能列為「待讀線索」。每筆紀錄要標 `全文已讀: 是/否`。
- 可讀全文的典型來源：PMC／開放取用期刊全文、各國鐵人總會公開的教練手冊或訓練計畫頁（British Triathlon、USA Triathlon、Triathlon Australia、World Triathlon 等）、知名教練或游泳教學機構公開的完整文章、論壇討論串原文（Slowtwitch、Reddit r/triathlon、r/Swimming、TrainingPeaks 文章等）。
- 三種證據分開標，不得混稱：
  - `研究`：有方法與資料的論文（記錄受試族群、樣本數、距離、主要結果）。
  - `實務文件`：總會手冊、教練文章、公開訓練計畫（記錄作者／機構、針對族群）。
  - `社群討論`：論壇原文（記錄討論串網址、主流意見、反對意見、大致幾則回覆支持哪一方；不得把論壇說成「研究顯示」）。
- 人名、數字、年份只寫原文裡出現的；抄數字要附原文所在段落的一句引文（英文原文即可）。
- 找不到就寫「未找到」，不要補推論。

## 1. 要查證的推論（逐條給判定：支持／部分支持／反對／無資料）

H1. 鐵人泳段（連續、無牆、之後要騎跑）的能量需求以有氧與閾值附近的持續配速為主，和多數池游比賽（50–1500 m、轉身多）的需求不同。
H2. 泳訓的技術、有氧、閾值（CSS）訓練可直接轉移到鐵人泳段；強度區與組型可沿用泳訓系統。
H3. 調整的是比例：閾值與有氧比例提高；乳酸耐受／速耐少量；純速小劑量保留（技術維持＋出發與繞標的短暫加速）。
H4. 族群例外：菁英允許跟游（draft-legal）短距離賽，開頭與繞標的加速決定位置，速度／速耐比重接近池游選手。
H5. 長距離連續游（1500／2000／3400 m）的價值是配速、距離信心、把開放水域技能放進長距離；它是有氧訓練量，不等於恢復課；整堂總量 3400 與連續游 3400 不同。
H6. 鐵人技能（抬頭定向、游直、跟游、繞標、防寒衣）需要專練，但可放進泳池課；每週一堂技術＋開放水域技能是常見安排。
H7. 每週泳課次數有限，每堂一個主目的（閾值／技術＋技能／長距離有氧）。
H8. 游泳對下肢衝擊小，常排在跑步關鍵課隔天或同日；全週疲勞一起算。
H9. 週期：基礎（技術、有氧）→建構（加閾值）→賽前（比賽配速分段、實地開放水域與防寒衣）→減量。
H10. 池游的 CSS／閾值配速換到開放水域會變慢（無牆、抬頭、水況），換算方式為何？有無實務換算方法？

## 2. 出課表需要的參數（盡量找到有出處的範圍；分族群：初學／分齡賽／菁英；分賽距：sprint 750 m、標準 1500 m、半超 1900 m、超鐵 3800 m）

P1. 每週泳課次數。
P2. 每週游泳總量或每堂時間。
P3. 強度分布（各強度區占比，或高強度課占幾堂）。
P4. 最長單堂／最長連續游距離與比賽距離的關係（例如長課是否超過比賽距離）。
P5. 典型主課組型（公開計畫中實際出現的組，例如 N×100／N×200／N×400 在 CSS 配速、休息幾秒）。
P6. 減量期長度與游泳量下降幅度（鐵人專屬，或沿用游泳減量）。
P7. 防寒衣與開放水域實地練習在賽前多久、幾次。
P8. 初學鐵人（游泳能力弱者）的不同處理：技術時間占比、是否先求完成距離。

## 3. 搜尋方向（每方向至少 2 輪不同關鍵字，換關鍵字再試一輪才可判「未找到」）

- 學術：triathlon swim training intensity distribution；triathlon swimming pacing open water；swim training transfer triathlon；draft-legal triathlon swim start speed position；wetsuit swimming performance；triathlon swim then cycling performance（游泳強度對後續騎跑影響）；concurrent training triathlon interference。只收能讀全文者。
- 實務：federation coaching manuals／beginner triathlon training plans swim sessions；"CSS" triathlon swim sets；Swim Smooth triathlon；open water pace vs pool pace conversion；triathlon swim taper。
- 社群：Slowtwitch／Reddit r/triathlon 關於「triathletes should swim like swimmers or do long steady swims」「how many swim sessions per week for 70.3 / Ironman」「is sprint work useful for triathlon swim」「long continuous swim vs interval」。

## 4. 輸出

1. `Research/鐵人泳訓/sources.md`：每個讀過的來源一筆（標題、作者／機構、年份、URL、類型、全文已讀、族群、跟哪幾條 H／P 有關、關鍵引文）。
2. `Research/鐵人泳訓/verdicts.md`：H1–H10 逐條判定＋依據（指向 sources 編號＋引文）＋反對證據；P1–P8 逐條給有出處的範圍或「未找到」，並分族群／賽距。最後一段「對出課表的影響」：哪些參數已有足夠出處可寫進課表規則、哪些仍是缺口。
3. 最終回覆：H1–H10 判定一覽、P1–P8 找到／未找到一覽、讀了幾個全文來源（三類各幾個）。
