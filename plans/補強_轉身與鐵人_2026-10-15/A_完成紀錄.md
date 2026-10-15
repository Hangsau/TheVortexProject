# 規格 A 完成紀錄：起跳／轉身／破水／水下海豚腿 補強（2026-10-15）

## 驗收數字

- validate：前 0 ERROR / 140 WARN，後 0 ERROR / 145 WARN。新增的 5 個 WARN 全是 W002（drill 有 source 顯示字串、無 source_ids；ST6、ST9、ST16、ST17、UDK8，照既有無出處 drill 的寫法）。W009、W011、W028、W029 皆為 0。W003（孤兒）、W008 沒有增加。
- build_knowledge_map.py、build_indices.py 已重跑。
- unittest：255 全過。唯一修改：`tests/test_build_indices.py` 的 problems 總數常數 73 改為 78（新增 5 個問題）。
- 規則全文：抓取成功。來源早已登錄為 src.world-aquatics-2023-swimming-technical-rules（URL https://resources.fina.org/fina/document/2023/01/04/65961a45-bde5-4217-b666-ca1f5dc2d1f0/1_Swimming-Technical-Rules.04.01.2023.pdf），WebFetch 對 PDF 只回二進位，改用本機存下的 PDF 以 pymupdf 抽文字後逐條讀過（SW 4–SW 10）。沒有新增 _sources.yaml 條目。

## 新增 ID

技術點（stroke: starts-turns）：starts-turns.tech.49 至 tech.59（共 11）

| ID | 主題 | 確定性與依據 |
|---|---|---|
| tech.49 | 開放式轉身完整序列 | 🟢 Hall & Murphy 第 26 章六個重點；規則 SW 7.2、7.6、8.1、8.4 |
| tech.50 | 開放式轉身適用情境 | 🔵 推導 |
| tech.51 | 仰式翻滾轉身規則與流程 | 🟢 規則 SW 6.4；Hall & Murphy 第 25 章 Backstroke Turns |
| tech.52 | 終點觸牆 | 🔵 機制；evidence 🟢 規則 SW 6.5、7.6、8.4 與書第 25 章 Backstroke Finish |
| tech.53 | 接力交接 | 🔵 機制；evidence 🟢 規則 SW 10.12、10.13 |
| tech.54 | 仰式破水 | 🟢 書第 24 章破水七要點與留氣；規則 SW 6.3 |
| tech.55 | 蛙式破水 | 🟢 規則 SW 7.1（其中蛙踢送身體上水面的部分是文中標明的 🔵 推導） |
| tech.56 | 蝶式破水 | 🔵 機制（換氣取捨為推導）；evidence 🟢 規則 SW 8.5 |
| tech.57 | 翻滾轉身教學進程 | 🔵 進程設計；evidence 🟢 書第 25 章水下翻滾與呼吸管練習 |
| tech.58 | 轉身訓練設計 | 🔵；evidence 🟢 書第 25 章 |
| tech.59 | 出發教學進程 | 🔵（無外部來源）；水深條件 cross_ref 到 diving-cervical-injury |

動作（moves.yaml）：starts-turns.move.8 至 move.14（開放式轉身、仰式翻滾轉身、終點觸牆、接力交接、自由式破水、仰式破水、蝶式破水）。既有 move.7（蛙式 Pullout）的 physical 末尾補一句破水規則。全部省略 cue_bad／cue_why／cue_good（move.8 原寫了書中提到的舊口令，但台灣教練是否真的這樣講無法確認，已刪除）。

Drill（drills_starts-turns.yaml）：ST6 至 ST20（15 個）。書中有出處者標 src.hall-murphy-2020：ST7、ST8、ST10、ST11、ST12、ST13、ST14、ST18、ST20（ST13、ST14 另加規則來源）；ST15、ST19 僅規則來源；ST6、ST9、ST16、ST17 為通行形式、source_ids 為空。

Drill（drills_udk.yaml）：UDK6 至 UDK10（5 個）。UDK6、7、9、10 取自第 22、25 章；UDK8 為通行形式。

問題（problems.yaml）：prob.starts-turns.flip-nose-water、breathless-after-turn、open-turn-wall-stall、back-turn-distance、relay-early-leave（共 5）。schema 要求 cross_ref_ids 只能放教學錯誤 ID，所以這五條 cross_ref 留空字串、cross_ref_ids 為空，連結改放 links.technical_analysis 與 links.drills；coverage_gap 皆為 no_intervention（沒有陸上介入）。

## 刻意省略或與規格不同之處

- 規格 1a-3 的「轉成俯臥後只能接一個連續手划」：規則原文是「立即連續的單手划或雙手同時划」，依原文寫。
- 規格 1a-6 的「仰式破水鼻子持續少量吐氣防止進水」：與書第 24 章「空氣留在肺裡、用鼻夾或上唇壓鼻孔」相反。依書寫；持續吐氣的做法只在 tech.54 提到是另一種可能，並註明本庫沒有兩者的比較資料。ST20 同步改寫。
- 接力電子判定容許值：規則全文（SW 10.12、10.13）沒有容許值，因此不寫數字，只寫「依當次賽事規程為準」。
- 書中 Velocity Meter 的數字（踢數建議、到 5 公尺的時間差）沒有寫進任何條目；那是特定個案的測量，不適合當通則。
- 蛙鞋、水下距離、休息時間：UDK7 的「每趟最多 25 公尺、休息 10 到 15 秒」是本庫的安全上限（書中是 20 x 25 公尺休 10 到 15 秒），已在 source 欄標明非原書處方。
- 沒有做文獻搜尋；沒有 git 操作；沒有修改既有條目內容（僅 move.7 補一句）。
- 蝶式破水、出發教學進程沒有書內對應章節（第 21 章蝶式未讀），全採 🔵 或規則。
