# E組執行清單與 run manifest

使用者於 2026-09-12 確認開始 W18–W25；原計畫與對話中的三項補正均已授權。
profile: mixed_cross_domain。任務是既有 canonical 的索引整合，不新增研究主張或介入。
起始版本：Vortex 7b308bc；my-site 2dea9c3。起始工作樹乾淨。
實測基線：104 誤區、222 技術條目、7 介入、179 drills；0 ERROR / 138 WARN。

## 資料契約補正

- `links.interventions` 僅表示陸上介入；`links.water_interventions` 保留水中介入連結。
  `no_intervention` 明確表示無符合門檻的陸上介入。水中介入不會消除此缺口。
- 新問題同時接上 validate、build_indices、build_knowledge_map、sync 與網頁。
- 檢查缺口與連結一致、目標類型、格式、重複 ID；公開層只帶讀者欄位。
- W19 的 title 按實際資料取條目 title，必要時取 public.title，原文不改寫。
- 只以既有材料作連結；僅有主觀感受、一般理論或未裁決方向衝突的候選另列原因。
- 公開頁以候選路徑呈現介入，保留其適用、不適用、證據邊界與停止條件。

## Checkpoints

| W | 派工 | 狀態 | 驗收 / 提交 |
|---|---|---|---|
| W18 | manual（本代理） | 完成 | d771a51；3 測試通過；0 ERROR / 138 WARN；943 records；地圖接線 |
| W19 | manual（本代理，機械抽取） | 完成 | fdcaec7；333 筆原文欄位 |
| W20 | manual（本代理） | 完成 | 73 個可見問題；333 候選有歸併／背景／不收錄去向 |
| W21a | manual（本代理） | 完成 | 12 問題；0 ERROR / 138 WARN；三關審閱 |
| W21b | manual（本代理） | 完成 | 15 問題；0 ERROR / 138 WARN；三關審閱 |
| W21c | manual（本代理） | 完成 | 12 問題；0 ERROR / 136 WARN；三關審閱 |
| W21d | manual（本代理） | 完成 | 11 問題；0 ERROR / 136 WARN；三關審閱 |
| W21e | manual（本代理） | 完成 | 11 問題；0 ERROR / 136 WARN；三關審閱 |
| W21f | manual（本代理） | 完成 | 12 問題；0 ERROR / 136 WARN；三關審閱 |
| W22 | manual（本代理） | 完成 | legacy 說明與 _INDEX；179 筆 drill 原文不變 |
| W23 | manual（本代理） | 完成並上線 | my-site 3b06c0b；公開同步 11 項＋movement 8 項通過 |
| W24 | claude: refactor（本代理沿用既有版型） | 完成並上線 | my-site 70e6c8e／476089d；309 連結／9 頁、四種寬度、搜尋與所有篩選在線上通過 |
| W25 | manual（本代理） | 本機完成，待推送授權 | 6894568；四組 1／43／26／3；138 項測試，0 ERROR／136 WARN |

## 執行與復原

每包驗收並 commit 後才開始下一包。canonical 變更重生地圖與四份 indices。
不使用多代理或同時寫同一 YAML；同步與部署也依序執行，避免 bot 與本機推送競爭。
push 前 fetch 並確認來源版本；同步失敗不發布後續頁面，修復後手動觸發既有 workflow。
本機睡眠或中斷不自動補跑；恢復工作後先核對本清單、git diff 與最後提交，再續作。
GitHub workflow 可在本機離線時完成，需核對觸發 SHA 與公開頁內容才記完成。

## 驗收矩陣

- 真實全庫驗證；缺 ID、無效或錯類目標、重複 ID、缺口不一致、未知鍵／格式拒絕。
- 空問題庫、完整候選量、部分完成及截斷 YAML；失敗同步保留上一份有效輸出。
- 舊資料無問題檔時相容；四份既有 JSON 視圖保留原欄位，新增統計採擴充欄位。
- 公開同步以診斷哨兵、未知頂層鍵、public 偽造欄位與錯誤 links 測試不洩漏。
- Hugo 完整建置；六式篩選、陸上／drill 組合、搜尋、零結果、重設、深連結、鍵盤、RWD。
- 每個公開連結驗 HTTP 與目標錨點；讀者文字無診斷鍵、來源機器鍵或未渲染格式。
- 並行修改風險以單一寫入者與串行 workflow 執行排除，不新增共享服務或排程。

## 未通過與裁決

隨候選歸併逐筆記入 `E組_問題候選盤點.md`；不是要求新增介入的待辦。

## W25 整合結果

- 73 題、333 候選（191 筆已連結／142 筆保留原因），完整統計見 `E組_覆蓋驗收報告.md`。
- `indices/gap_report.json.problem_coverage` 四組互斥；陸上與水中分開計數。
- 1016 內容 ID、179 drills、861 sources；858 → 861 來自執行中另一路已提交的週期化工作，E 組未新增來源或介入。
- 本機 logs 與截圖位於工作區暫存 `tmp/vortex-e-20260912/`；可重跑的驗收程式已入庫。
- W23／W24 推送一度被自動核准審查擋下；核對 origin、公開 repo 與三個 outgoing commits 後獲核准。

## 部署結果與待授權動作

- 網站 `476089d` 部署成功：[CI 34697248838](https://github.com/Hangsau/cortex/actions/runs/34697248838)，使用 Hugo 0.159.1。
- [公開找問題頁](https://hangsau.github.io/cortex/vortex/problems/) 重跑 `audit_vortex_problems.js` 全通過，與本機相同 73 題／309 連結／9 頁／四種寬度，JS error 0。
- Vortex W25 提交 `6894568` 推至 `Hangsau/TheVortexProject` 的 `master` 被自動核准審查拒絕，理由是共享主分支需要明確發布授權。未改推其他分支或繞過審查。
- 待使用者授權後，正常推送 W25 與本次交接記錄；等 notify-mysite workflow 成功，確認沒有非預期的公開資料差異。
- 73 題主體已由 W21 推至遠端；剩餘 canonical 內容變動僅「动作／停顿」兩處正體字校正，另有 W25 索引程式、報告、測試與交接文件。
