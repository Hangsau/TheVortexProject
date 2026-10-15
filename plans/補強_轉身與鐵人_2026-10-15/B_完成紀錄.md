# 規格 B 完成紀錄：新技能「開放水域與鐵人」open-water（2026-10-15）

## 驗收數字

- validate：前 0 ERROR / 145 WARN，後 0 ERROR / 147 WARN。新增 5 個 W002（drill 有 source 顯示字串、無 source_ids：OW2、OW7、OW10、OW13、OW14，照既有無出處 drill 的寫法）。W009、W011、W028、W029 皆為 0。147 比 145+5 少 3，我沒有逐項追查是哪一類 WARN 減少（現況：W002 之外只剩 W003 124 筆、W008 3 筆，皆為既有類別）；沒有新增的 W003／W008 以報告中搜不到 open-water／OW 條目為準。
- build_knowledge_map.py、build_indices.py、tag_coverage_report.py 已重跑。
- unittest：255 全過。唯一修改：`tests/test_build_indices.py` 的 problems 總數常數 78 改為 84（新增 6 個問題）。

## 規則全文抓取結果：失敗，沒有寫任何規則數字

- World Triathlon 競賽規則：triathlon.org/documents 與 about/downloads/category/competition_rules 兩頁的文件清單是動態載入，WebFetch 取不到任何 PDF 連結。
- World Aquatics 開放水域規則：worldaquatics.com/rules、/rules/competition-regulations、/open-water、/open-water/rules 四頁都沒有 OWS 技術規則 PDF 連結（只有世界排名 PDF、泳裝核准與 Constitution）。
- 因此防寒衣的水溫門檻、是否強制／禁止、跟游的距離與碰觸限制、出發方式的規定，全部只寫一般性說法（「許多賽事允許」「依水溫與賽事規則」「以報名賽事的規則為準」），沒有任何數字，`_sources.yaml` 沒有新增條目。
- 後續若取得規則 PDF（需手動下載後給本機路徑），可用 pymupdf 抽文字補 tech.4、tech.5、tech.7、tech.8 的規則細節。

## 實際來源

規格預期書中沒有太多開放水域內容，實際上本機有一章：Riewald & Rodeo (2015) Science of Swimming Faster 第 24 章 Open Water Swimmers（Steve Munatones 撰寫），來源早已登錄為 `src.riewald-rodeo-2015`，本次全章讀過（含 POW 泳池開放水域、列隊游、上岸組、定向、閉眼偏向測試、恐慌處置、冷水適應）。凡是有引用的數字都是書中原文有的（1.3 倍距離緩衝、十公里每二十五公尺抬頭約四百次）；書中沒有的（防寒衣浮力與肩部阻力、仰臥滾轉、海豚跳細節、跟游機制）都標 🔵 推導。

## 結構登錄

- `canonical/_taxonomy.yaml`：stroke 加 `open-water`；category 加 `open_water_skill`（drills 範圍）與 `open_water`（instructional 範圍，給 problems）。
- `Drills/_categories.yaml`：加 `open_water_skill`（開放水域技能）。
- `canonical/instructional/problems.yaml`：categories 加 `open_water`（開放水域）。
- `tools/validate.py`：ID 正則兩處加 `open-water`；問題索引的 drills 連結正則加 `OW` 前綴；註解補 `open-water.tech.1`。
- `tools/build_knowledge_map.py`（泳式標籤「開放水域與鐵人」、四處清單、Drills 清單與列數文字）、`tools/audit_layers.py`、`tools/review_firstpass.py`、`tools/tag_coverage_report.py`（加 `drills_open-water.yaml`）。
- `Drills/DRILL_INDEX.md`：檔案表加一行。
- 沒有在 `Drills/TAG_SCHEMA.md` 登錄（它不列舉 strokes／category 值，`strokes: [open_water]` 沒有被驗證器限制）。

## 新增 ID

技術點（stroke: open-water，technical-analysis.yaml）：open-water.tech.1 至 tech.19（共 19；tech.14 在追加要求後改寫，tech.16 至 19 為追加）

| ID | 主題 | 確定性與依據 |
|---|---|---|
| tech.1 | 沒有牆、沒有池底線，泳池成績不能直接換算 | 🔵；evidence 🟢 書第 24 章 |
| tech.2 | 定向抬頭（鱷魚眼） | 🔵；evidence 🟢 書第 24 章 |
| tech.3 | 游直的能力與閉眼偏向測試 | 🔵；evidence 🟢 書第 24 章 |
| tech.4 | 跟游 | 🔵；evidence 🟢 書列隊游；規則細節未取得 |
| tech.5 | 集體出發 | 🔵；evidence 🟢 書進進出出與上岸組 |
| tech.6 | 繞浮標與仰臥滾轉 | 🔵；evidence 🟢 書不蹬牆轉身與左右肩繞標；仰臥滾轉部分純推導並註明無比較資料 |
| tech.7 | 防寒衣（一）身體位置 | 🔵；evidence 🟢 僅限鹽水淡水浮力差，書未討論防寒衣浮力（文中已寫明） |
| tech.8 | 防寒衣（二）動作代價 | 🔵（無外部來源） |
| tech.9 | 波浪與水流 | 🔵；evidence 🟢 書第 24 章 |
| tech.10 | 踢腿分配 | 🔵；evidence 🟢 書第 24 章 |
| tech.11 | 出水上岸 | 🔵；evidence 🟢 僅限書的上岸組與心率變化，頭暈機制為推導 |
| tech.12 | 恐慌與過度換氣 | 🔵；evidence 🟢 書的處置清單；cross_ref 健康、心理、呼吸條目 |
| tech.13 | 泳池裡怎麼練開放水域 | 🔵；evidence 🟢 書第 24 章 |
| tech.14 | 鐵人泳段和池游比賽的需求差異（改寫） | 🔵 推導，無 evidence |
| tech.16 | 泳訓轉移與比例調整（含菁英允許跟游短距離賽的族群差異；cross_ref CSS 條目並寫明無開放水域 CSS 效度研究） | 🔵 推導 |
| tech.17 | 長距離連續游的定位（含總量不等於連續游距離、非恢復課） | 🔵 推導 |
| tech.18 | 時間預算：每堂一個主目的 | 🔵 推導 |
| tech.19 | 週期結構（基礎、建構、賽前、減量，只寫結構） | 🔵 推導 |
| tech.15 | 和騎跑一起排 | 🔵（無外部來源） |

動作（moves.yaml）：open-water.move.1 至 move.8（定向抬頭、游直線、跟游、集體出發、繞浮標、防寒衣游、海豚跳、出水上岸）。全部省略 cue_bad／cue_why／cue_good。

Drill（Drills/drills_open-water.yaml）：OW1 至 OW15（共 15）。有書中出處（source_ids: src.riewald-rodeo-2015）：OW1、OW3、OW4、OW5、OW6、OW8、OW9、OW11、OW12、OW15。通行形式、source_ids 為空：OW2、OW7、OW10、OW13、OW14。OW3、OW11、OW14、OW15 的安全條件（看守、水深底質、水溫、不勉強）寫在步驟內。

問題（problems.yaml）：prob.open-water.panic-breathless、veer-off-course、legs-sink-after-sighting、wetsuit-shoulder-fatigue、start-blowup、exit-dizzy（共 6）。照規格 A 的做法 cross_ref 留空、cross_ref_ids 為空，連結放 links.technical_analysis 與 links.drills；coverage_gap 皆 no_intervention。

週期化：`canonical/periodization/decisions.yaml` 的 planner 區塊 `links.related` 加入 open-water.tech.14、open-water.tech.15，未改任何既有數值。

## 刻意省略

- 教學誤區（teaching-errors.yaml）：0 條。三個候選（鐵人游泳不用踢腿的過度執行版、鐵人只要長距離慢游、穿防寒衣就不用練身體位置）我無法在本機書或不做文獻搜尋的前提下確認「哪種教練或教材主動這樣教」，依收錄標準不收；tech.10 與 tech.7 已把對應的正確觀念寫在技術點。若 Hang 能確認哪個鐵人教練圈真的這樣講，再補 open-water.err 條目。
- 沒有寫任何防寒衣水溫門檻、跟游規則數字、省力百分比。
- 沒有取得 World Triathlon 與 World Aquatics 規則全文，見上。
- 補給與賽中補水（書中有，但屬營養領域，且超出規格主題）未寫；健康條目的脫水低血鈉已由 tech.12 cross_ref。
- 沒有改既有條目內容（僅 decisions.yaml 一行 related 與 taxonomy／工具登錄）。
- 沒有做文獻搜尋；沒有任何 git 操作；沒有動 `tools/map_learner_speech.py`（工作樹中它的修改是別的 session 的）。

## 下游 my-site 需要改的清單（在 my-site repo 看到的寫死泳式清單）

- `tools/sync_vortex.py:32` DRILL_STROKES 加 `open-water`（drills 檔名 `drills_open-water.yaml`，drill 的 strokes 值是 `open_water`）。
- `tools/build_vortex_links.py:20` MOVE_FILES、`:32` 的 `starts_turns` → `starts-turns` 對映（需加 `open_water` → `open-water`）、`:36` NO_LEVEL_STROKES（open-water 無 L 級對應，應加入）、`:220` 泳式中文名（加「開放水域與鐵人」）。
- `next/layouts/_partials/vortex/home.html:4-5`、`list.html:17,24-25,34`、`rail.html:7`、`stroke.html:235`、`movement.html:217`：泳式順序、中文標籤、strokes 對映都要加 `open-water`。
- `next/specs/check.py:26` STROKES 加 `open-water`。
- `tools/test_vortex_links.py` 與 `research/content-presentation-2026-09-05/inventory.py` 若寫死泳式清單也要同步（未細查）。
- moves 的 `drills` 連結用 drill ID（OW1…）；problems 的 drills 連結正則在 canonical 側已加 `OW`。
- 跑 `sync_vortex.py` 後確認新技能頁、技術分析、練習清單、問題索引都出現，並推 my-site。本次沒有動 my-site。

## 追加要求處理（無依據數字、鐵人訓練架構）

- 數字稽核：移除自訂處方。OW4 改名「雙邊換氣」（原 3／5 划），步驟改為固定間隔、從容易的開始；OW11 水深改為條件式（水深足夠入水不碰底、由有經驗的人確認）；OW12 的「站穩一兩秒」改為站穩確認不暈再走；OW15 等無數字處方。剩餘數字只有書中原文的：1.3 倍距離緩衝、十公里每二十五公尺抬頭約四百次、約四百公尺配速出發。tech.14 的「50 到 1500 公尺」是池游比賽項目距離的事實描述。
- 鐵人訓練架構：tech.14（改寫）、tech.16 至 tech.19，共 5 點，category 皆 tempo（划頻划距與訓練哲學），全部 🔵 且不引數字；tech.15（跟騎跑一起排）保留。decisions.yaml planner 的 related 擴為 tech.14 至 tech.19。
- 使用者的問題回答位置：鐵人泳訓與一般泳訓差異見 tech.14；專練還是轉移見 tech.16；偶爾排 1500／2000／3400 長距離課見 tech.17（價值、非恢復課、總量不等於連續游）。
- 重跑結果：validate 0 ERROR / 147 WARN（W002 共 20，其中新增 5），unittest 255 全過，地圖與索引已重生。
