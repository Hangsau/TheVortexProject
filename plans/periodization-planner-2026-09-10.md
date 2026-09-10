# 訓練週期決策工具第一版 — 執行與證據紀錄

使用者已同意試做：共用決策表、情境範例及 my-site 互動選擇器。phase：decision → integration → publication。採 quantitative empirical（研究摘要／實验結果）及 project model（操作流程）兩種證據型態；不把可執行規則當已驗證的訓練療效。

- [manual] 既有內容比對：periodization 44 個穩定 ID；目錄 42 筆，缺 GAS 與 flexibility。修正已有節點，不另建同義概念。
- [manual] 修正 RPE／計時／速度方向、固定排程預設及技能學習研究外推。
- [manual] 新增 canonical 決策契約，明列輸入值域、規則優先序、適用條件、改變條件及觀察方法；同步至 my-site。
- [manual] 實作公開表單、靜態流程與範例、可複製的安排；不使用學員診斷或私人資料。
- [manual] 驗收 canonical、目錄覆蓋、同步一致性、規則衝突、手機、鍵盤、無 JavaScript、正式部署。

## 來源與採用範圍

| 來源／尋獲方式 | 已取得 | 採用 | 不採用 |
|---|---|---|---|
| Nikitakis & Toubekis；PubMed 41410759，題名與 DOI 搜尋 | metadata + 摘要；直接開啟回空，搜尋索引回完整摘要；2026-09-10 核對 | 單次組課不同生理反應，不用單一乳酸／內負荷代替整堂課；先記組課結構 | 長期適應優劣、所有族群通用區間；未稱全文精讀 |
| Carvalho 等；PubMed 41348148 | metadata + 原始摘要；2026-09-10 核對 | 小樣本加量期間 HRV 改變而表現維持；HRV 單獨下降不自動判失敗 | AI 個人診斷、固定 HRV 停課門檻；未称全文精讀 |
| Branscheidt 等；eLife 40578 | 原文方法／結果（含實驗 4），未稱全篇逐頁精讀 | 疲勞影響手部力量控制任務學習；低力量序列任務未見同樣損害 | 所有技能都受損、水感 L0–L6 已驗證、低強度高量等於低疲勞 |
| 2025 西班牙教練問卷，DOI 10.3389/fspor.2025.1642020 | 方法／結果／限制段 | 背景篩選紀錄保留，本版不新登錄 | 用 18 人橫斷問卷證明哪種週期最好 |
| 2024 青少年減量、急性 PAPE、非游泳 HRV 與數學預印本 | 篩選 | 排除於本版規則 | 未做完整系統回顧，不宣稱窮盡最新研究 |

新增研究以 2026 紙本年份登錄，保留 2025 首次上線日期。輸入與分支皆為專案模型；每一高影響規則具 affirmative_conclusion / works_when / fails_when / how_to_identify / action / remaining_boundary。暫採「賽前兩週」為介面辨認近期事件的窗口，不代表文獻證實人人應減量 14 天。

## 驗收目標與邊界

有症狀優先於比賽與進步；疲勞优先調整今日，反覆退步才回看週安排。未知資料不自動加量；陸上進步不等於游泳轉移成功；比賽臨近不安排補課或新重訓。任何分支都列出當次取捨與下次重看條件，週課次與時間只分配使用者可用資源。規則可供其他公開消費端重用，本版只接 my-site，不更動 swim-coach 私人診斷流程。

基線：canonical validator 0 ERROR / 142 WARN。

## 2026-09-10 中斷恢復與接續檢查

使用者上一階段要求優化週期內容、補新研究並做可套用邏輯，於臺灣 07:44 回覆「好 試試著做看看吧」；本次要求接續。沿用既有實作及專案發布授權，不重新要求確認。中斷對話最後一筆工具結果在臺灣 08:05:37：Hugo 已成功，但新驗收腳本在 `zones.yaml` 的原始字串比對失敗。原始變更仍留在兩個工作目錄，未提交。

### 1. 目標

保留中斷前成果，完成原定週期決策第一版驗收、版本保存與既有網站發布流程，讓下一次可從實際狀態接續。

### 2. 範圍与消費端

- canonical：`canonical/periodization/{structure,taper,zones,dryland,decisions,_index}.yaml`（taper 僅驗證）、`canonical/_sources.yaml`、地圖工具及衍生 `KNOWLEDGE_MAP.md`、`indices/*.json`、驗證報告、此紀錄與 HANDOFF。
- my-site：periodization 同步資料、公開來源表、同步 allowlist、週期頁與資料庫模板、新 partial/CSS/JS/驗收工具、驗收證據與 HANDOFF。
- 不擴充其他章節；swim-coach 私人規則、首頁、兩冊教材與既存未追蹤 `WinError` 不在本批。
- 公開靜態網站供泳者及教練使用；互動在瀏覽器執行，輸入不持久化。電腦重啟不影響已部署內容；本機預覽需重啟。無新增排程，GitHub push 觸發同步／建置，恢復後以實際 SHA 核對 CI。
- 規則唯一來源為 decisions.yaml；JS 解譯器、靜態表、範例共用資料。目錄驅動導航／資料庫。同步後按既有 `unfold_cjk` 清理規則核對所有資料。

### 3. 執行路徑

1. 已將兩個 repo 的 29 個變更檔打包到 `C:/claudehome/tmp/periodization-recovery-2026-09-10/saved-before-resume.zip`，逐檔 SHA-256 見同目錄 manifest.json；備份不發布。
2. 確認六份 YAML 經既有中文折行清理後完全一致，再修正驗收的誤報；若出現其他差異，逐欄查明，不放寬內容比對。
3. 執行 canonical validator、地圖／索引重建、Hugo、實際瀏覽器與 8,820 組規則驗收；失敗先修該項。
4. 保存兩端 HANDOFF 與提交；my-site 先發布含新同步 allowlist 與完整頁面的版本，再推 canonical，避免 notify-mysite 用舊同步腳本漏掉 decisions。推送失敗不強推，先比較远端變更。
5. 按提交 SHA 檢查 CI，對正式站重跑互動驗收並核對 CSS/JS；記錄發布結果。

### 4–5. 風險與處理

| 風險／機制 | 事前檢查 | 恢復方式 |
|---|---|---|
| 中斷後誤覆寫已存內容 | Git 狀態與逐檔備份清單 | 只從備份取回確認需要的檔案，不重跑舊一次性整合腳本 |
| canonical 中文折行清理造成假差異 | 六檔以既有 `unfold_cjk` 比對；實際只 zones 一欄有清理差異 | 修驗收，不回改中文排版、不忽略其他欄位差異 |
| 規則衝突、空白／異常輸入或舊結果殘留 | 8,820 組、非法 enum／數字、清空與輸入變更、症狀分支 | 修分支／輸入處理後重跑；保留無 JS 靜態表 |
| 兩 repo 發布與自動同步相互覆蓋 | 先查遠端狀態，先發 my-site，再發 canonical；按 SHA 追蹤兩端 workflow | 非快轉停止並比較；必要時以新 revert commit 回復，不強推 |
| 前端複製非同步、使用者文字注入、舊快取 | 複製失敗 fallback、輸入作文字、正式 CSS/JS 比對 | 清除失效結果；修程式並重驗正式資產 |

資料格式是新建 schema v1，無舊持久化資料需遷移；不寫私人輸入或資料庫。程式不把使用者文字組成 shell／SQL／正則。共享狀態只在單一頁面，剪貼簿 Promise 完成時檢查結果快照；兩端發布需序列執行。超長目標有長度上限，數字值域明訂。

### 6. 驗收與下一步

沿現有檔案修復是最少變動路徑，無新增研究範圍或重新建立功能。本次覆核仍將文獻摘要與專案模型分開，未把規則測試視為訓練成效驗證。

- canonical：0 ERROR / 140 WARN（基線 142，未新增警告）；48 個穩定 ID 全部在正確目錄中，各一次。
- Hugo：170 頁成功，保留既有 languageCode 淘汰警告。
- 本機瀏覽器：21 項驗收、8,820 組規則全部通過；390/320px、200% 字級、鍵盤、無 JS、三範例、複製 fallback、來源定位與資料庫入口均已驗。
- 已目視手機表單與桌面結果。來源重核：PubMed 41410759 直接開啟回空，改從同站索引取得完整摘要；41348148 摘要及 eLife 40578 實驗 4 已核，未提高閱讀狀態。
- 發布完成：my-site 實作 `a37790963e2922b9f2cbd80d2017287ee67a2c90`、canonical `748756ffc4867767ba0399ce6f0a2ba7a655f670` 均已推送；[網站部署 CI](https://github.com/Hangsau/cortex/actions/runs/34452544465) 與 [canonical 同步 CI](https://github.com/Hangsau/TheVortexProject/actions/runs/34452546812) 已按完整 SHA 核對成功。
- [正式工具](https://hangsau.github.io/cortex/vortex/periodization/#planner) 驗收 21/21、8,820 條件組合通過，內嵌資料與本機相同，CSS／JS 逐位元相同；證據為 my-site `research/periodization-planner-2026-09-10/{public-validation,public-assets,ci-verification}.json`。截圖已排除擷取長元件時的固定導覽遮擋。
- 本階段已完成。後續以實際使用回饋修訂模型，無未完成的背景任務；不需重跑暫存整合腳本。
