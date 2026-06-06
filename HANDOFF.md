# The Vortex Project — 工作交接單

> 每次有實質推進後更新「當前狀態」與「下一步建議」。規則與背景見 `CLAUDE.md`。

---

## 當前狀態（2026-06-06）

### 已完成——canonical/ 結構化資料層：散文→YAML 模組化（my-site 探索器來源）

> 目標：把 Vortex 主題層散文模組化成 my-site 可掃描 / 可篩選 / 可展開的探索器。canonical-first：結構先進 canonical/（public/diagnostic 兩層），再經 sync_vortex.py 只帶 public 傳到 my-site，diagnostic 留給 swim-coach。

- [x] **教學誤區**（commit 82f6fe0 + 9e68ffb）：6 式 76 條 → `canonical/instructional/teaching-errors.yaml`；public{misconception/physical_reason/evidence/correct_concept/perception_impact} + diagnostic{type}。my-site `vortex-errors.html` 探索器。
- [x] **技術分析**（commit 6ad36ea）：6 式 188 技術點 → `canonical/instructional/technical-analysis.yaml`；全 public（物理層）。my-site `vortex-tech.html` 探索器。
- [x] **L 指標矩陣**（commit 34090b6）：`Technica/技術指標_L級對應框架.md` → `canonical/technica/l-indicators.yaml`；43 indicators（6 levels × 5 strokes，30 格全填）；public{indicator/framework_state/quant_ref/evidence} + diagnostic{failure_signal（6 common 格）/ type（3 格 A/B/C：free.L3.evf=A / back.L4.roll-stability=C / fly.L4.outsweep=A）}。my-site `vortex-matrix.html`（ADM matrix 範式：rows=levels × cols=strokes，aspect chip → 共用 detail panel，泳式 focus 篩選 + deep-link / hash-jump）。
- 下游：my-site commit 3cf6069（Hangsau/cortex，CI green run 27053437843）；sync_vortex.py `sync_l_indicators()` 只帶 public，built HTML 診斷洩漏審查 = 0。swim-coach submodule 未 bump（l-indicators diagnostic 尚未被 vendor 消費，Phase G 再驗）。
- [x] **水感層級**（Phase D）：4 式 `Technica/*水感框架.md` → `canonical/technica/water-sense-levels.yaml`；26 levels（free/back L0–L6，breast/fly pre+L2–L6）。public{description/methods/indicators/quant/stagnation/milestone + 各式特有 four_problems/state_description/fatigue_collapse_four_layers/kaizen/stress_test} + diagnostic{type_diagnosis/type_states/type_training/type_milestones/stagnation_by_type} + 頂層 three_types/appendices。公開層三型/A/B/C 全數淨化：per-stroke 字面替換（如「重新做三型診斷」→「重新確認感知缺陷的主要方向」、移除「（A型）」標記）+ 把 stagnation 內的 A/B/C 型專屬尾段抽出搬到 `diagnostic.stagnation_by_type`；審查 regex（三型|A型|B型|C型|哪型|不論主型|typical_speech|main_problem|chain_breakpoint|failure_trigger）over public = 0 leaks。my-site `vortex-levels.html`（vxl- 縱向序列卡：泳式 + L 級篩選、card expand、deep-link/hash-jump）。
- 下游：my-site `sync_vortex.py` `sync_water_sense_levels()` 只帶 public（three_types/appendices/每 level diagnostic 整塊不取），built HTML 診斷洩漏審查 = 0。swim-coach submodule 未 bump（water-sense-levels diagnostic 尚未被 vendor 消費，Phase G 再驗）。

### 已完成——Drills/ 補入 how_to 操作步驟（commit a4ddee1）

- [x] 5 個 `Drills/drills_*.yaml` 全部 125 個動作補入 `how_to` 操作步驟（block list，插在 `purpose_zh` 之後）
- [x] 來源：*There's a Drill for That*（Laurie Sherret），每條過三關校正（符合研究 + 反問 + 反推）
- [x] commit `a4ddee1` 已 push 到 origin/master（524 insertions，純 how_to，0 deletions）

### 同步下游

- [x] **my-site 公開層**（commit ff69013，Hangsau/cortex）：`data/vortex/drills.yaml` 經 `sync_vortex.py` 的 `sync_drills` 合併重生；`vortex-drills.html` 渲染 how_to + 「要去感覺什麼」（`perception_goal` 改框）、移除 `failure_signal`（什麼是錯的）與成功/失敗對照、加 `#drill-<id>` 錨點；`vortex-explorer.js` drill chip 改為可點連結（對得上 `name_zh→id` 就連到 drill DB 卡片）。CI 綠、已部署
- [x] **swim-coach 診斷層**（commit 9a1fed3）：`vendor/vortex` submodule bump 到 `a4ddee1`
- 公開層原則重申：drill 內「要去感覺什麼」（perception_goal）屬可公開的感知目標；「感覺錯了是什麼樣」（failure_signal）只留在 canonical 診斷層，不上公開網站

---

## 當前狀態（2026-06-05）

### 內容修正
- [x] **物理數值/歸因三關校正回原始資料（2026-06-05，配合 my-site explorer 沒過清單）**：
  - 波阻定律 `F ∝ v⁴` → `F ∝ v³`，並改為「接近競速時約佔總阻力 25%（低速時較低）」（`Bridge/自由式感知橋接.md` + `Instructional/自由式深度技術分析.md`）
  - 小指轉朝下入水「阻力降低約 9.5%」→ 改為「有助降低入水阻力（教練觀測，主要見於 hip-driven 自由式，非通用物理量）🟠」，移除偽精確數字（`Bridge/自由式感知橋接.md`）
  - PMID 24290609 歸因修正：`Arellano, Pardillo & Gavilán 2013` → `Atkison et al. 2014`（WebFetch PubMed 確認真實作者；`Bridge/水下蝶腳感知橋接.md` + `Instructional/水下蝶腳技術分析.md` ×2 + `Instructional/水下蝶腳教學誤區深探.md`）。註：誤區深探 line 90 一處 `Arellano 2013`（無 PMID）依高風險歸因規則暫留不動
  - 蛙式「約 29% 體重出水」無可信來源 → 改為「上身過度出水（具體出水比例待查 🔴）」（`Instructional/蛙式深度技術分析.md` ×2）
- [x] `Bridge/自由式感知橋接.md`：刪除頭部位置的「頭頂放水瓶（Gary Hall Sr.）」教練觸發條件——頭頂水瓶是臉朝上的平衡訓練（仰式），自由式臉朝下且轉頭換氣放不住，屬仰式訓練誤掛到自由式。保留「蛙鏡鏡片不超過水面基準線」這個自由式有效視覺參考。此錯誤自 initial commit 起就存在，之前的口頭糾正未寫入檔案，導致重新生成 my-site explorer YAML 時再次出現；同步修正 my-site 兩層副本。

### 已完成——Drills/（新建）

- [x] `Drills/drills_freestyle.yaml` — Fr1–Fr24（24 個動作，含 Vortex 感知層標注）
- [x] `Drills/drills_backstroke.yaml` — Bk1–Bk26（26 個動作）
- [x] `Drills/drills_breaststroke.yaml` — Br1–Br34（34 個動作）
- [x] `Drills/drills_butterfly.yaml` — Fl1–Fl31（31 個動作，含水下蝶腳標注）
- [x] `Drills/drills_sculling.yaml` — Sc1–Sc10（10 個划水感知動作）
- [x] `Drills/DRILL_INDEX.md` — 完整索引（Schema / L級對應 / ABC型 / 快速查找）
- 來源：*There's a Drill for That*（Laurie Sherret），每個動作均有 `perception_goal`、`success_signal`、`failure_signal` 感知層標注

### 已完成——my-site 網頁（對應）

- [x] `data/vortex/drills.yaml` — 125 個動作合併檔（供 Hugo 讀取）
- [x] `layouts/vortex/vortex-drills.html` — 可篩選動作資料庫（泳式/L級/類別/ABC型四維篩選）
- [x] `static/css/vortex.css` — 新增 vxd-* 樣式（卡片 / 篩選鈕 / 感知行 / 分類/ABC型徽章）
- [x] `vortex-home.html` — 首頁加入動作練習資料庫入口
- [x] commit + push 到 Hangsau/cortex，CI 已觸發

---

## 當前狀態（2026-04-17）

### 已完成——Instructional/

- [x] 四式深度技術分析（自由式 / 仰式 / 蛙式 / 蝶式）
- [x] 出發與轉身技術分析（查證深化版）— Swimming Canada ADM + 實證文獻 + 背→蛙三種轉法比較（PMC7918682）+ 機制說明；剩餘 🔴×7 均確認為研究空白
- [x] **水下蝶腳技術分析.md**（獨立建立，深化版）— 壹～陸章；波動力學 / 渦流回收 / Strouhal / 踢腿力學 / 踝關節量化 / 代謝穩定性；剩餘 🔴×2
- [x] 自由式回臂入水教學誤區.md
- [x] 仰式水下動作教學爭議.md
- [x] 蛙式教學誤區深探.md
- [x] 蝶式教學誤區深探.md
- [x] **水下蝶腳教學誤區深探.md**（13條，外部來源全查証）
- [x] **出發與轉身教學誤區深探.md**（查證版，9條全查證，🔴×4 保留待深探）
- [x] **自由式教學誤區深探.md**（2026-04-17）— 23條全補完；7節；4條🔴查證完成；最終品質確認（USRPT 作者修正等）

### 已完成——Technica/

- [x] 水感指南.md（理論基礎 Part 1–6，原完整指南拆分而來）
- [x] 自由式水感框架.md（L0–L6 + 附錄，原完整指南 Part 7 提取）
- [x] 技術指標 L 級對應框架
- [x] 仰式水感框架 v4.2 / 蛙式 v5 / 蝶式 v2
- [x] **自由式水感框架.md**（2026-04-16）— 從完整指南第七部分提取；三型定義改為感知層面語言；A型確立為「分不出手跟水的互動」；四式框架齊全

### 已完成——Bridge/

- [x] 自由式感知橋接.md
- [x] 仰式感知橋接.md
- [x] 蛙式感知橋接.md
- [x] 蝶式感知橋接.md
- [x] 出發轉身感知橋接.md（完整版，2026-04-17）— 8 感知時刻 + IM 轉身（背→蛙三種轉法感知 + 蝶→背）+ Pullout 三技術感知差異 + 三型識別 + 指導語速查
- [x] **水下蝶腳感知橋接.md**（2026-04-16）— 7感知時刻 + 三型識別 + 疲勞崩潰 + 指導語速查 + SQ應用

### 已完成——Research/感知科學/

- [x] 因果倒置假設.md（主張A精確化 + L5 修訂）
- [x] 動態系統理論.md
- [x] 內臟感知與迷走神經.md
- [x] 神經學對照組三點座標.md
- [x] 感知量化SQ框架.md

### 已完成——Research/其他 + Observations/

- [x] RESEARCH_PLAN.md / FUTURE_RESEARCH.md / _INDEX.md
- [x] Observations/ 三份（L0漂浮三態診斷 / 小划手板實驗 / 指令層次設計）
- [x] **機械感受器.md**（2026-04-17）— 四類皮膚感受器特性 + 水環境影響 + 側線演化對比 + 訓練工具悖論（划手板/阻力手套）+ L級框架連結 + A型失敗神經說明；🔴×3

---

## 缺失/待建立（優先順序）

### 確認研究空白（不再追查）

- [x] **水下蝶腳技術分析 🔴×2**（2026-04-17 確認）
  - 膝蓋角度 30–40° vs 60–70°：假說合理（下踢前 vs 上踢峰值），無單一研究同步確認，**確認為研究空白**
  - Strouhal 縱向訓練後變化：現有文獻僅橫斷面描述，無縱向追蹤，**確認為研究空白**

### 中期（研究層擴充）

- [x] Research/感知科學/機械感受器.md（2026-04-17 完成）
- [x] Research/感知科學/感知學習.md（2026-04-17 完成）
- [x] Research/感知科學/feedforward機制.md（2026-04-18，整合自 Talos feedforward_mechanism.md）
- [ ] Research/感知科學/隱性_顯性學習.md（待建立，Masters 1992，見 RESEARCH_PLAN 1.4）
- [x] Research/物理現象/渦流回收.md（2026-04-18 完成，Talos 輔助研究）— 6 篇文獻全查證；🟢 Hochstein 2011（UUS 再捕獲）/ Takagi 2014（划水 wake capture）/ Garayev 2021（螳螂蝦跨物種）；🔴×3 待補
- [x] Research/物理現象/推進力理論演變.md（2026-04-18 完成，從 raw/notes 整合）— 阻力/升力/現代三階段；「找靜水」邏輯謬誤；🔵×2 🟡×4 🟢×1；連結 渦流回收.md / 機械感受器.md / 誤區深探
- [x] Research/物理現象/自然頻率.md（2026-04-25 完成，Talos + Claude 協作，v1 committed，c500f7b）
- [x] Research/物理現象/彈性蓄能.md（2026-04-25 完成，Talos + Claude 協作，v4 committed）

### 長期（需累積素材）

- [ ] Observations/ 更多教學案例（需實際教學素材）
- [ ] SQ框架最小可行觀察計畫執行（見感知量化SQ框架.md）

---

## 下一步建議

### 當前最高優先——Vortex 主題層模組化（散文→探索器）

進度（canonical-first：結構先進 canonical/，再經 my-site `sync_vortex.py` 只帶 public）：

- [x] **Phase A/A'/B/C**：教學誤區 / 技術分析 / L 指標矩陣 / Drills how_to → 已上線（見「當前狀態」）
- [x] **Phase D 水感層級**：4 式水感框架 → `canonical/technica/water-sense-levels.yaml`（26 levels，公開層三型 0 leaks）+ my-site `vortex-levels.html`。本 session 完成。
- [ ] **Phase E 退役 Bridge/**：Bridge/ 散文已被 `canonical/perception/*.yaml`（public/diagnostic 兩層）+ stroke explorer 的 `data/vortex/{stroke}.yaml` 取代 → 冗餘。做法：① Bridge/*.md 加 deprecated 標頭（不刪）② my-site `sync_vortex.py` 移除 Bridge layer ③ 清空 `content/vortex/bridge/` ④ 首頁移除感知橋接卡。水感指南（基礎理論長文）保留為唯一散文（single.html）。
- [ ] **Phase F 首頁重設計**：把首頁做成真正的「感知地圖」= 泳式×層 矩陣／控制台，單一視覺語言。⚠️ 用戶已兩次不滿目前排列 → **此階段必須先取得用戶明確方向確認，不可自走**。
- [ ] **Phase G 收尾**：full sync + `--dry-run` 驗證、文件對齊（_INDEX / 兩邊 HANDOFF / vortex_sync_state.json）、swim-coach submodule 僅在 diagnostic 真被消費時才 bump。

待用戶決定：① 輪替先前暴露的 TheVortexProject token；② 是否把本 repo 既有未提交 WIP（CLAUDE.md / 蝶式深度技術分析.md / canonical/perception/ / 教學競技框架_v1.md / 沒過清單）併入或另行處理（本 session 未動）。

---

**前次 session（2026-04-25）完成：**
- `Research/物理現象/彈性蓄能.md` v4 — Talos + Claude 6 輪蘇格拉底教學協作完成
  - Richards 2012 整合（水阻衰減 SSC）
  - 🔵 推導格式重寫（物理演繹不需引用）
  - 所有假文獻描述清除（v1 subagent 幻覺根源識別）
  - committed to GitHub master；GitHub strikethrough bug 修正（`~` → `≈`）
- `Research/物理現象/自然頻率.md` v1 — Talos + Claude 5 輪蘇格拉底教學協作完成
  - 🔵 諧振子公式 + 水阻修正，0.8-1.5 Hz 物理推導
  - 🟢 Morris 2016（PMID 27052972 / DOI 10.1007/s00421-016-3372-4）
  - 🔴 4 項確認為研究空白（泳姿共振直接測量等）
  - committed to GitHub master（c500f7b）
  - ⚠️ 🟡 部分條目缺標題/DOI（PMID 36065966/34186517/31601852），v2 可補
- COLLAB.md Task #1、#2 標記完成
- `/check-talos-reply` skill 重大更新：新增草稿審閱 Step 4a（SCP+審閱清單），確保驗收後才宣告 goal_achieved

### 當前最高優先

**`Research/感知科學/隱性_顯性學習.md`（Task #3）**
- COLLAB.md 最後一份待建立文件
- 理論成熟但框架應用需討論，等下一輪教學 session 啟動
- Masters 1992 是起點文獻；Talos 已透過 claude-inbox 收到通知（2026-04-25）

### 已確認研究空白（彈性蓄能.md + 自然頻率.md）
- 自由式肩帶 in-vivo 彈性蓄能測量（無此文獻）
- 蝶式 dolphin kick SSC in-vivo 測量（無此文獻）
- 各泳式彈性貢獻量化 %（研究空白）
- 泳姿共振（stroke resonance）直接測量（PubMed 0 hits）
- 游泳 in-vivo 自然頻率測量（研究空白）

---

## 重要知識更新記錄

**2026-04-10** 確立：
- 感知優先的神經科學基礎（預測編碼、小腦模型、張力閘門）
- 前沿研究方向（渦流回收、感受器訓練、身體頻率、彈性蓄能）

**2026-04-11**：
- 內臟感知框架、神經學三點座標（嬰兒/魚/菁英）、L5 修訂、SQ框架、EMG悖論詳細版

**2026-04-14**：
- 出發起跳角度修正（精英 21–27°，非傳統 30–40°）
- UDK 深度修正（0.4–0.6m 實用範圍）、速度數據修正
- Kick Start 前後腳角色（後腳水平、前腳垂直，與傳統教學相反）
- 查出 3 篇文獻期刊名稱錯誤

**2026-04-16（本 session 上半段）**：
- 自由式回臂入水教學誤區.md 新建
- 仰式水下動作教學爭議.md 新建
- 蛙式教學誤區深探.md 新建
- 蝶式深度技術分析 + 蝶式教學誤區深探.md 新建（含多處文獻錯誤修正）
- 出發轉身感知橋接.md 新建
- 水下蝶腳技術分析.md 獨立建立、深化（含代謝穩定性節 Hvid 2024）
- 水下蝶腳教學誤區深探.md 新建
- **UDK 🔴×3 查證**：踝關節代償 → 🟢（PMC9402090 + PubMed 24984154）；其餘保留 🔴
- **水下蝶腳感知橋接.md 新建**（Bridge 層完整）
- **出發與轉身教學誤區深探.md 新建**（9 條全查證）

**2026-04-16（本 session 下半段）**：
- **出發與轉身技術分析第二輪查證**（🔴 8 → 7）：
  - 填入：膝蓋角度 100–120°（PMC6409673）+ 背→蛙規則（FINA SW 6.4）+ 蝶→背效率（PubMed 30694108）
  - 補充機制說明：過淺入水（PubMed 25455956）+ Pullout 三技術（PMC9445308）+ 翻滾啟動 + 仰式 OBL2（PubMed 28975846）
  - 剩餘 🔴×7 確認為研究空白或個體差異大，近期無需再查

**2026-04-17**：
- **出發轉身感知橋接補強**：IM 轉身感知（背→蛙 + 蝶→背）+ Pullout 三技術感知差異 → 感知時刻由 6 擴充至 8
- **背→蛙三種轉法補完**（技術分析 + 感知橋接兩層）：
  - Open / Bucket / Crossover 動作機制、PMC7918682 數據（推出速度差異）
  - 關鍵發現：Crossover 推出最快（2.17 m/s）但 7.5m 成績無差異——四個機制說明
  - 核心教學原則：執行穩定性 > 技術選擇
- **Technica 層重組**：
  - `游泳水感完整指南.md` 拆分為 `水感指南.md`（理論 Part 1–6）+ `自由式水感框架.md`（L0–L6，已於本 session 建立）
  - 原完整指南刪除；仰/蛙/蝶框架引用更新；重複內容消除
- **自由式教學誤區深探.md 完成**（2026-04-17 下半段）：
  - raw/notes 七份整合後刪除；七節 23 條全補完
  - 4 條 🔴 全查證：誤區 13（膝蓋角度）/ 14（踝關節訓練時程）/ 16（旋轉幅度）/ 23（CI → 特異性原則）
  - 最終品質確認：USRPT 作者 Bob Ernie 幻覺 → Dr. Brent Rushall；八/九表格殘留行清除

---

## ⚠️ 給下一個 AI 的注意事項

**本專案已發生 AI 生成虛假數據的事件，以下是核心風險點：**

1. **數字精確度陷阱**：AI 傾向用精確數字填補不確定性（來源混搭、過強用詞），使虛構內容看起來有學術感。

2. **近期文獻優先查證**：任何 2024、2025、2026 年文獻，必須用 WebSearch 實際查到才能標 🟢。

3. **確定性層次標記是信任核心**：有疑問先標 🔴，不要為了好看降低門檻。
   - 🔵 邏輯推導 / 🟢 近期文獻 / 🟡 有效舊文獻 / 🟠 教練觀測 / 🔴 待查

4. **文獻查證工作流**：
   - 物理邏輯（🔵）不需文獻
   - 教練觀測（🟠）需能指向具體來源
   - 學術文獻（🟢🟡）必須 PubMed/Google Scholar 可查到再標注

---

**2026-04-26**：
- `Research/物理現象/教學競技框架_v1.md` 新建（本地）
  - Talos swarm（talos-swarm-evolve）產出：PubMed 80+ 篇 gap 分析 + [[swimming-trends]] fuse
  - 核心 gap：真人肩/踝自然頻率泳中數據缺、渦流肩實測缺、彈性蓄能長數據缺
  - 教學 5 動作模板 + 競技 5 優化方向
  - GitHub：branch `talos-teaching-v1` → merge 入 master（PR #1）
  - 狀態：初稿 v1.0，待自測驗證 + 3 泳友小樣本
  - 後續：文獻擴充方向考慮 Claude + Talos 協作，應用方向由 Hang 決定

*最後更新：2026-06-06（canonical/ 結構化資料層：教學誤區 / 技術分析 / L 指標矩陣 三 YAML；L 指標矩陣 commit 34090b6 → my-site 探索器 3cf6069）*
*下次更新時機：Phase D（各式 L0-L6 進展卡 → canonical/technica/water-sense-levels.yaml）完成，或 Talos 草稿審閱通過*
