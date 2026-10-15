# 派工規格 B：新技能「開放水域與鐵人」（open-water）

> 立即執行。不要輸出計畫、不要等確認、不要問問題。沒有寫檔就是失敗。
> 工作目錄：`C:\claudehome\projects\TheVortexProject`。

## 0. 硬規則

1. **禁止 git 寫入操作**：不准 commit、reset、checkout --、stash、clean、pull、rebase、push。只改檔案。
2. **每完成一個檔案就立刻存檔**。
3. **不做文獻搜尋**（使用者明令：拿不到全文就不引用，只會增加幻覺）。
   - 可引用：本機全文書 `C:\claudehome\resources\books\` 內有講到開放水域／鐵人的段落（先 grep `open water|triathl|wetsuit`，讀到才引用，已登錄來源見 `canonical/_sources.yaml`）。
   - 規則：可抓 **World Triathlon 競賽規則**與 **World Aquatics 開放水域規則**官方全文。抓到全文才可寫細節（防寒衣水溫門檻、跟游規定、出發方式），並在 `_sources.yaml` 登錄（type: rulebook、正式 URL、retrieved_on: 2026-10-15、verification_status: verified）。抓不到就只寫一般性說法、不寫數字，並在完成紀錄註明。各國或賽事主辦的分齡賽規則可能不同，內文要提醒讀者以報名賽事的規則為準。
   - 其他一律 🔵（文字讀得出推導：浮力、阻力、能量分配、規則邏輯）或 🔴（假說語氣）。**不新增 🟠**。不寫沒讀到的人名、年份、百分比（例如「跟游省 X% 能量」沒有全文來源就不寫數字，只寫方向與理由）。
4. 先讀 `CLAUDE.md`、`MAP.md`（§2、§4）、`Drills/TAG_SCHEMA.md`、`Drills/DRILL_INDEX.md`，以及現有 `starts-turns` 在各檔的條目當格式範本。
5. public／diagnostic 分層、機器鍵不入散文、W028／W029 規則同 CLAUDE.md。
6. **受眾**：鐵人三項（分齡賽、成人初學鐵人、青少年鐵人）＋一般開放水域泳者（長泳、比賽）。兩者都要服務，不窄化成競技菁英。
7. **安全優先**：開放水域的死亡風險主要在恐慌、冷水、心臟事件（canonical/health 已有 `cold-water-shock`、`exertional-sudden-cardiac-death`、`hypothermia-swimmers`、`drowning`、`dehydration-hyponatremia` 等 drafts，用它們的條目 ID `cross_ref`，**不重寫健康內容**）。恐慌與恐懼接心理層 `psych.fear.*`（先 grep `canonical/psychology/psychology.yaml` 找實際 ID），呼吸調節接 `canonical/breathing/regulation.yaml`。
8. 繁體中文、台灣用語（防寒衣、浮標、跟游、集體出發、蛙鞋）。

## 1. 結構登錄（新增技能 key：`open-water`，中文名「開放水域與鐵人」）

照 `starts-turns` 在每個地方的登錄方式，加入 `open-water`：

- `canonical/_taxonomy.yaml`：`fields.stroke.values` 加 `open-water`；如有其他列舉 stroke 的地方一併加（count 照實）。
- `tools/validate.py`：ID 正則（`(?:free|back|breast|fly|udk|starts-turns|common)` 那幾處，以及檔頭附近的命名空間說明）加 `open-water`。
- `tools/build_knowledge_map.py`、`tools/audit_layers.py`、`tools/review_firstpass.py`、`tools/tag_coverage_report.py`：清單加入 `open-water`（Drills 檔名 `drills_open-water.yaml`），標籤「開放水域與鐵人」。
- Drills 的 `strokes` 標籤值用 `open_water`（比照 `starts_turns`）；若 `TAG_SCHEMA.md`／`_categories.yaml` 列舉了 strokes 或 category 值，同步登錄（category 可新增 `open_water_skill`，須登錄）。
- 若 `tests/` 有寫死泳式清單的契約測試，同步更新。

## 2. 內容

### 2a. `canonical/instructional/technical-analysis.yaml`：stroke `open-water`，ID `open-water.tech.1` 起，約 14–16 點

每點有 `title`、`public.summary`、`public.mechanism{certainty,text}`、`public.practical_implication`。主題：

1. 沒有牆、沒有池底線：每一划都要自己推進、少了轉身的短暫休息與蹬牆加速，泳池成績不能直接換算開放水域配速；連續游能力要另外練。
2. 定向抬頭（sighting）：只讓眼睛剛出水看前方（俗稱鱷魚眼），看完再轉頭換氣；抬頭越高腿越沉、阻力越大。看與換氣可分開或合併，依水況選。抬頭頻率依直線能力與水況調整，用「自己偏多少」決定，不給固定數字。
3. 游直的能力：左右划手不對稱、單邊換氣、踢腿偏向會讓人在沒有參照物時偏航；先在泳池測自己的偏向（閉眼或不看線），再決定抬頭頻率。雙邊換氣的實際用途是保留選邊（避浪、看浮標、看對手）。
4. 跟游（drafting）：正後方跟腳，或在前一位泳者髖側；省力的方向與理由（前方泳者帶動水流、減少自己迎面阻力），不寫百分比；風險是跟到方向錯或配速不合的人。規則上鐵人的游泳段允許跟游（以抓到的規則全文為準）。
5. 集體出發：開頭一段強度遠高於巡航配速（搶位置、避開碰撞），之後要能降回巡航配速而不爆掉；這是要專門練的能力。出發方式：沙灘跑入、水中出發、跳台／浮台出發；淺水段可用海豚跳（雙手前撲入水、蹬底再起）。
6. 繞浮標：靠內線較短但擁擠，外線較長但順；轉向時可用仰臥滾轉（corkscrew，翻仰一划再翻回）縮小轉彎半徑。
7. 防寒衣（一）身體位置：浮力集中在軀幹與下肢，讓下沉的腿浮起，受益最大的是腿沉的泳者；浮力好的泳者效益較小。
8. 防寒衣（二）動作代價：肩部周圍布料增加回臂阻力、限制活動度，常見對策是回臂較寬較低、划頻略高；穿脫與合身要提前在泳池練，不在比賽日第一次穿。規則上依水溫允許／強制／禁止（以全文為準）。
9. 波浪與水流：滑行會被浪打斷，開放水域常見較高划頻、較短滑行；換氣邊選背浪側。
10. 踢腿分配：鐵人游泳段多半用較少的踢腿（例如兩拍踢）以保留下肢給騎跑，防寒衣補足身體位置；但腿沉又不穿防寒衣的泳者減少踢腿會讓身體下沉——這是硬體條件（浮力、踝活動度）而非意志問題。
11. 出水上岸：游到手划到底（碰到沙）才站起；最後一段可加踢腿喚醒下肢；從水平轉為站立時可能頭暈（姿勢改變的血液重新分配），要先站穩再跑。🔵／🔴 依推導強度標。
12. 恐慌與過度換氣：冷水接觸、臉入水看不到底、擁擠碰撞會觸發急促呼吸；先預防（下水前入水熱身、先在冷水中慢慢吐氣、出發站邊線）；發生時的自救：翻成仰漂或抬頭蛙式、舉手求救、抓住救生艇或浮具。必須 `cross_ref` health 與心理、呼吸條目。
13. 泳池裡怎麼練開放水域：不推牆的轉身（中池轉身或池邊不蹬牆）、每 N 划抬頭看池端目標、三人一道並排游模擬擁擠、跟腳游、長距離連續游、穿防寒衣練習。
14. 鐵人泳段的組課：泳段目標通常是用最低代價完成、出水還有餘力騎跑；強度用 CSS 或閾值配速做組（`cross_ref` `canonical/periodization/set-design.yaml` 的 CSS 相關條目，並註明 set-design 已記錄「開放水域沒有 CSS 效度研究」的缺口），搭配快出發後回穩的組。
15. 跟騎跑一起排：游泳主要負荷在上肢與軀幹，跟跑步的關鍵課衝突較小，常排在同日；但總疲勞要一起算（`cross_ref` decisions.yaml 的 triathlon 族群選項）。

### 2b. `canonical/instructional/moves.yaml`：新增 `stroke: open-water` 區塊

`premise` 一段（含一句安全前提：不獨自下水、帶顯眼的救生浮標、先確認水溫與水況），`moves` 7–9 個：定向抬頭、游直線、跟游、集體出發、繞浮標、防寒衣游、海豚跳、出水上岸。欄位照既有（id: `open-water.move.N`）。`cue_bad` 只寫教練真的會講的錯誤口令；想不到就省略三個 cue 欄位。

### 2c. 新檔 `Drills/drills_open-water.yaml`：約 14–16 個 drill，ID 前綴 `OW`

檔頭註解比照其他 drills 檔。完整 9 軸 fingerprint（值必須在 TAG_SCHEMA 內）。無書面出處寫 `source: "通行的…練習形式；本庫未取得可定位的單篇出處"`、`source_ids: []`。建議清單：

- 鱷魚眼抬頭（泳池：每 N 划看池端目標，只露眼）
- 抬頭看＋轉頭換氣分開做 vs 合併做
- 閉眼直線測試（有人看守、空水道，測偏向）
- 雙邊換氣 3／5 划
- 擁擠游：三人並排同一水道（輕微碰撞耐受）
- 跟腳游（兩人一組，前後交換）
- 髖側跟游
- 不蹬牆轉身（模擬沒有牆）
- 快出發回穩組（例如前段快、後段回巡航，用配速而非數字定義）
- 仰臥滾轉繞標（泳池用水道繩或浮具模擬浮標）
- 海豚跳（淺水，水深與底質安全條件寫清楚）
- 出水上岸轉換（最後一段加踢、站起先穩再走）
- 防寒衣泳池適應（先穿著做輕鬆游、再做抬頭與轉向）
- 冷水入水程序（漸進入水、臉入水慢慢吐氣；`cross_ref` cold-water-shock）
- 恐慌自救練習：游進中翻成仰漂、恢復呼吸再翻回

### 2d. `canonical/instructional/teaching-errors.yaml`：0–4 條 `open-water.errN`

只收**教練或鐵人教材真的會主動這樣教**的觀念（照 CLAUDE.md 誤區收錄標準），每條附一句「哪種教練／教材這樣教」。候選（自行判斷是否成立，不成立就不收）：「鐵人游泳不用踢腿」（過度執行版）、「鐵人只要長距離慢游就好」、「穿防寒衣就不用練身體位置」。格式照既有誤區條目。

### 2e. `canonical/instructional/problems.yaml`：新增 4–6 個 open-water 問題

讀者描述式標題，例如：「一到開放水域就喘不過氣、想停」「游不直，抬頭才發現偏了」「每次抬頭看完腳就沉」「穿防寒衣肩膀很快就痠」「出發一開始就爆掉」「上岸站起來頭暈腿軟」。category 需新增時先在 problems.yaml 的 categories 登錄（例如 `open_water` 開放水域技能）。`links` 指向本次技術點與 drill；`coverage_gap` 如實填。

### 2f. 週期化

在 `canonical/periodization/decisions.yaml` 的 `triathlon` 選項附近，或 set-design 合適處，加一段鐵人泳段組課原則的 `cross_ref`，指向 `open-water.tech.14`、`open-water.tech.15`。不要改既有數值。

## 3. 完成前必做

1. `python tools/validate.py` → **0 ERROR**；新內容不得新增 W009、W011、W028、W029。
2. `python tools/build_knowledge_map.py`、`python tools/build_indices.py`、`python tools/tag_coverage_report.py`。
3. `python -m unittest discover tests` 全過。
4. 寫 `plans/補強_轉身與鐵人_2026-10-15/B_完成紀錄.md`：新增 ID 清單、每條確定性與依據、規則全文抓取結果（URL）、validate 前後 WARN 數、刻意省略項目與理由、**下游 my-site 需要改的地方清單**（你在本 repo 看到的、寫死泳式清單的下游假設）。
