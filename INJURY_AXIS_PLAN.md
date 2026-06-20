# 游泳運動傷害知識軸 — 建置計畫 v2

> 從 canonical（渦流計畫）出發，每個傷害「一條線做完整」（機制→文獻→如何避免→發生後如何處理→何時就醫），最終渲染進 my-site 的 vortex section。
> 規劃/整合：Opus｜審稿：minimax-m3｜研究+核實：Sonnet（WebSearch/WebFetch）｜結構化欄位比對：haiku
> **v2 變更**：已整合 minimax-m3 第一輪審稿（20 點建議，見 §8 triage）。

---

## 0. 定位（前提校正）

- **傷害是 Vortex 的獨立軸**，與「水感知技術軸」並列、不從屬。核心命題「所有游泳技術都建立在水感知上」規範的是技術教學，不涵蓋傷害安全。
- **兩軸交會點**做 cross_ref（游泳肩→前鋸肌/EVF、蛙泳膝→踢腿力學），其餘不強綁。
- **受眾**：全光譜（CLAUDE.md 鐵律）。族群差異分多維度欄位（年齡/性別/能力/生命週期），不窄化單一族群。
- **範圍邊界**：主軸是**游泳（四式 + 出發轉身 + 未來自由潛水）**。鄰近水上項目（水球、藝術游泳、競技跳水）只在與游泳訓練實際重疊處收錄（如跳水入水頸椎傷 = 出發台/淺水風險），不展開成多項目傷害百科——避免 scope creep。

---

## 1. 分類體系（Taxonomy v2）

**六大類**（v2 新增 E 急性創傷、拆出 D-內分泌、補溺水/心臟/海洋生物）：

| 類 | 中文 | 代表項 | 與感知軸 |
|----|------|--------|---------|
| A | 肩與上肢（肌骨過度使用） | 游泳肩、棘上肌腱病、MDI、SLAP、二頭肌腱病、TOS、肘腕 | 有交會 |
| B | 下肢與脊椎（肌骨，泳式特異） | 蛙泳膝(拆 MCL/髕股/鵝足滑囊)、腹股溝、FAI、椎弓解離、伸展型腰痛、踝足 | 部分交會 |
| C | 非肌骨醫學（環境/化學/感染） | 游泳耳、外耳道骨瘤、氯結膜炎、皮膚(肉芽腫/毛囊炎/泳者癢/綠髮)、EIB/菁英泳者氣喘、牙齒酸蝕、隱孢子蟲、棘阿米巴角膜炎 | 無 |
| D | 系統性 / 環境急性 | **溺水/近乎溺水(置頂)**、SWB 淺水昏迷、SIPE 肺水腫、冷水休克、低體溫、UV/曬傷、脫水、**運動性猝死(HCM/心肌炎/commotio cordis)** | 無 |
| D-內分泌 | 能量與內分泌 | RED-S、女性運動員三聯症、運動性無月經、低骨密度、疲勞性骨折(鐵人/陸訓帶入) | 無 |
| E | 急性創傷 | 跳水頸椎/脊髓傷、出發台/水面撞擊、池邊滑倒、轉身蹬牆急性傷、開放水域生物危害(水母/海膽/弧菌/鉤端螺旋體) | 無 |
| F | 族群骨突/骨骺(兒少特有) | Osgood-Schlatter、Sever、游泳版 apophysitis、Salter-Harris 骨骺傷、Scheuermann's | 無 |

**injury-level 必填維度欄**（不靠 population_notes 帶過）：
- `environment`: pool / open_water / surf（傷害圖譜差異大，影響鐵人+公開水域受眾）
- `sport_variant`: swim / open_water_swim / diving_entry / freediving（**限游泳相關**，不擴 water_polo/artistic）

---

## 2. 分層（public vs clinical）

| 層 | 受眾 | 內容 | 防幻覺 |
|----|------|------|--------|
| **public 安全衛教** | 全受眾 | 機制白話 + 如何避免 + **紅旗(何時就醫)** + 水中替代處方 | 未核實數字**不得進** |
| **clinical 細節** | 深讀者 | 流病數字、文獻、復健 protocol、鑑別診斷 | 待查標🔴；爭議標來源 |

注意 sync_injuries() 將比照現有 sync 函式：canonical 兩層 → 剝出 public 寫進 my-site；clinical 是否上站於 Phase 4 決定（injuries 的 clinical ≠ 教學 diagnostic，原則可公開，但 pending_verification 數字在 layout 層隱藏）。

---

## 3. 資料 schema v2

**設計原則**：核心欄位必填（研究可靠填得出）；臨床欄位 optional（避免 schema 膨脹 + 降低幻覺面——逼填 imaging 閾值會誘發捏造）。

```yaml
meta: { domain: injury-prevention, axis: independent, last_updated: 2026-06-20 }

categories: [ {id, zh, nav_zh}, ... ]   # A/B/C/D/D-endo/E/F

injuries:
  - id: swimmers-shoulder
    zh: 游泳肩
    en: Swimmer's shoulder
    category: A-shoulder-upper
    environment: pool            # 必填維度
    sport_variant: swim          # 必填維度
    layer: [public, clinical]

    # ── 機制 ──
    structures: [棘上肌腱, 肱二頭肌長頭腱, 肩峰下滑囊]
    mechanism:
      summary: 前鋸肌疲勞→肩胛去穩定→旋轉肌過載繼發夾擊/肌腱病
      stroke_phase: 自由式抓水—早期推水（肱骨外展+內旋）

    # ── 流病（來源性質 vs 證據強度分開）──
    epidemiology:
      prevalence: "菁英泳者 40–91%"
      certainty: 🟡               # 來源性質：🔵推導🟢近期🟡舊🟠教練🔴假設
      evidence_grade: B           # 證據強度：A(RCT/系統綜述)/B(世代)/C(個案)/Expert
      caveat: 盛行率不可橫向比較（現症vs生涯、自陳vs影像）
      sources: ["McKenzie 2023 系統綜述（DOI 待 WebFetch 驗證）"]

    risk_factors: [訓練量>35km/週, 肩鬆弛/不穩, 既往疼痛史, 高肘崩潰]

    # ── 如何避免（每條附證據等級）──
    prevention:
      - { text: 旋轉肌+肩胛穩定耐力訓練, grade: B }
      - { text: 技術矯正（避免越中線入水、雙側換氣）, grade: C }
      - { text: 訓練量漸進管理, grade: B }

    # ── 發生後如何處理（v2 擴充）──
    management:
      red_flags:                  # public 層必填：何時必須停練+就醫
        - 夜間靜止痛/手臂無力 → 排除旋轉肌全層撕裂
        - 頸部放射痛+手麻 → 排除頸神經根
      acute: 相對休息+物理治療；避免誘發動作
      pain_rules: 復健期疼痛≤3/10、不改動作型態、24h 不惡化
      rehab: 旋轉肌/肩胛穩定漸進阻力；離心
      functional_progression_criteria:   # 以功能指標為錨，非時間
        - 肩胛穩定測試對稱
        - 無痛全活動度
      swim_modifications_in_rehab:        # 水中替代處方（核心非選配）
        - 初期 pull buoy 減踢、避免過頭爆發
        - 單臂划水分離患側負荷
      return_to_train: 無痛活動度+穩定測試過 → 漸進回水，技術重建優先於量
      return_to_compete: 全量無痛訓練 2 週 + 技術穩定 → 復賽
      prognosis: 保守治療多數 6–12 週改善（依嚴重度）

    # ── 族群差異（多維度，不塞一欄）──
    population_notes:
      age: { youth: 早發肌腱病, adult_beginner: 既有退化下技術未熟易夾擠, masters: 二頭肌腱病/鈣化偏多 }
      sex: ~
      ability: { para: 上肢推進依賴者肩負擔最高 }
      lifecycle: ~                # pregnancy / freediving 視傷害填

    # ── 接回感知/技術軸（三層拆分）──
    links:
      mechanism_link: 前鋸肌耐力是 EVF 硬體前提
      technical_link: free.tech.10 前鋸肌硬體邊界
      perception_link: L4–L6 手感/張力

    # ── 文獻 + 防幻覺 ──
    references:
      - { citation: "Sein ML et al. 2010, Br J Sports Med 44(2):105-113", certainty: 🟢, verified: false }
    flags:
      pending_verification: ["Olympic 96% supraspinatus tendinosis 為轉述，待原文核實"]
      contested:
        - claim: 機制為真夾擊 vs 不穩定繼發肌腱病
          consensus_source: 學界偏向不穩定繼發
          dissent_source: 早期 Neer 夾擊模型
      vintage_warning: false      # evidence 主要 2015 前時 true

    audit: { last_reviewed: 2026-06-20, reviewer: opus, supersedes: ~ }

  # ── optional 臨床欄（有資料才填，不逼填）──
  # severity_grade / diagnostic_criteria / imaging_trigger /
  # differential_diagnosis / contraindications
```

### 3.1 Smoke pilot 校準（W1 完成後回填，schema 凍結版）

5 傷（游泳肩 A / 蛙泳膝 B / SWB + SIPE D / RED-S D-內分泌）跨四類驗證後，schema 微調如下：

- **`sport_variant` 改為可純量可列表**：肌骨單一泳式用純量（`swim`），系統性/環境急性常跨情境用列表（`[swim, freediving]`、`[swim, open_water_swim]`）。
- **新增 `fatal_acute: true`（optional 旗標）**：致命急性風險（SWB/SIPE/溺水/冷水休克/心臟猝死）標記，供 layout 置頂用。非致命傷不寫此欄。
- **新增 `subtypes`（optional 列表）**：傘狀總稱傷害（蛙泳膝拆 MCL/PFPS/鵝足/皺襞）在頂層列子型；子型機制差異寫進 mechanism/management 文字。
- **`mechanism` 子鍵彈性化**：`summary` 必填；其餘按傷害性質選填 `stroke_phase`(肌骨泳式特異) / `trigger_phase`(環境急性) / `driver`(能量/負荷驅動) / `who`(高危族群速記)。不逼非肌骨傷填 `stroke_phase`。
- **`population_notes.sex` 可純量(~)可子map**：性別有明確差異者展開 `{female, male}`（RED-S/SIPE），無差異填 `~`。`age`/`ability`/`lifecycle` 同理。
- **`grade` 欄嚴格 A/B/C/Expert**：證據等級欄不得放確定性圓點（🟠 等）；專家共識/機制推導級用 `Expert`。確定性圓點只出現在 `certainty`/`references.certainty`。
- 校準結論：**核心欄位在四類傷害皆填得滿**，大量 `~` 出現在系統性傷的肌骨欄（pain_rules/rehab/mechanism_link）屬合理 null，非 schema 缺陷。schema 凍結，W2 展開。

---

## 4. Pipeline v2（含 smoke pilot）

### Phase 0 — 規劃審稿 ✅
Opus 出計畫 → minimax-m3 審稿 → v2 定稿（本文件）

### Phase 1 — 研究蒐集（先 smoke 後展開）★唯一耗 Claude 配額
- **W0 鎖 schema**：本文件 §3 即 schema 凍結版
- **W1 smoke pilot（5 傷）**：游泳肩 / SIPE / SWB / 蛙泳膝 / RED-S
  - 這 5 項已有 4 份報告的豐富素材 → **由 Opus 直接整合進 v2 schema**驗證欄位完整性，**不需新派研究**（省配額）
  - smoke 完成 → 回頭校準 schema → 確認可填得滿 → 才展開
- **W2 展開研究**（Sonnet+WebSearch，分批每批一子系統）：
  - 補全缺漏（E 急性創傷、溺水、心臟猝死、海洋生物、棘阿米巴、外耳道骨瘤等）
  - 深化每項 management（acute/rehab/RTT/RTC/red_flags/prognosis）
  - **W2.4 亞洲/華文流病**：補中國國家隊/台灣競技泳者數據，避免單一英語偏壓
- **W3 防幻覺核實**（**Sonnet** WebFetch 原文，非 Haiku）：核實待查作者名、轉述數字、DOI 字串；**Haiku 只做結構化欄位比對**（PMID→DOI、標題→作者拼字）
- **每完成一條 injury → Opus 寫進 `canonical/health/drafts/<id>.yaml` 並 commit**（防覆蓋，符合全域「並行任務逐條 commit」）
- **中段 minimax-m3 抽審**：每 10 條一次（不只 Phase 3 終審）
- sub-agent prompt **強制禁 git 操作**，**只回文字不寫檔**

### Phase 2 — 整合（Opus）
- drafts/*.yaml 合併成 `canonical/health/injuries.yaml`
- Opus 親自做跨傷害一致性審（術語、相位命名、cross_ref）——不另開協調員 agent
- 更新 `_INDEX.md` 加 health 層

### Phase 3 — 最終審查（minimax-m3）
- 防幻覺逐項對 §6 checkpoint、分類一致、族群覆蓋、框架定位、schema 正確

### Phase 4 — 網站渲染（my-site）
- 加 `sync_injuries()`（比照現有 sync 函式：兩層→剝 public→data/vortex/injuries.yaml）
- vortex 傷害頁 layout（沿用 vortex 設計語言；按 environment/類別/泳式/族群篩選 + 搜尋，**致命急性風險置頂**）
- sync → build → push 兩 repo（token 繞道）

---

## 5. 派工分工表 v2

| Phase | 任務 | 執行者 | 理由 |
|-------|------|--------|------|
| 0 | 規劃/整合 | **Opus（本 session）** | 框架判斷 |
| 0/1/3 | 審稿（計畫/中段/終審） | **minimax-m3** | 月費不吃配額；客觀性審查 |
| 1 smoke | 5 傷整合驗 schema | **Opus** | 用既有報告，省配額 |
| 1 W2 | 展開研究（含亞洲流病） | Sonnet ×N（WebSearch） | 引用級研究須 Claude |
| 1 W3 | 原文核實作者/數字/DOI | **Sonnet**（WebFetch） | 人名+數字是幻覺區，不可 Haiku |
| 1 W3 | 結構化欄位比對 | haiku | PMID→DOI 機械比對 |
| 2 | 整合+一致性審 | **Opus** | 確定性判斷、框架一致 |
| 4 | sync_injuries() + layout | Opus | 程式+設計 |

---

## 6. 防幻覺把關 checkpoint（強制）

1. 人名只在搜尋明確查得才填，否則「待查」，**不編造**；核實一律 Sonnet 不用 Haiku
2. 數字必追原始論文；「轉述」數字不進 public 層
3. `certainty`（來源性質）與 `evidence_grade`（證據強度）**分開兩欄**
4. 共識 vs 爭議：`flags.contested` 須附 consensus_source + dissent_source
5. 版本控制：`last_reviewed` + `supersedes` + `vintage_warning`（RED-S 2014 正名、EIB 命名更新、過度訓練 2022 分類）
6. **審稿者的事實「更正」本身也要驗證**（見 §8：m3 把 Sein 2010 BJSM 誤改 JOSPT，駁回）

---

## 7. 驗收標準

- [ ] injuries.yaml 涵蓋 A–F 六類「所有常見」傷害，每項核心欄完整（含 management.red_flags）
- [ ] 所有盛行率附來源；public 層無「待查」殘留；爭議項附正反來源
- [ ] 族群差異多維度填寫，無單一族群偏壓；含亞洲流病
- [ ] sync_injuries() 跑通，data 正確生成
- [ ] vortex 傷害頁可篩選/搜尋，致命急性風險（溺水/SWB/SIPE/冷水休克）置頂
- [ ] minimax-m3 終審通過
- [ ] HANDOFF/_INDEX/RESEARCH_PLAN 對齊，commit+push 兩 repo

---

## 8. minimax-m3 審稿 triage（20 點）

**全採納**（12 條）：①分類加 E/D-內分泌/溺水/心臟/海洋生物/兒少骨突 ②environment+sport_variant 必填 ③蛙泳膝拆子條目 ④RED-S 與過度訓練分列 ⑥return_to_swim 拆 train/compete、cross_ref 拆三層 ⑦management 加 red_flags/pain_rules/functional_progression/swim_mods ⑧加 evidence_grade 欄 ⑨加 last_reviewed/supersedes ⑩smoke pilot 先 5 傷 ⑪核實改 Sonnet、Haiku 降為結構化比對 ⑬中段 m3 抽審 ⑭sub-agent 禁 git+逐條 draft commit ⑰補亞洲華文流病 ⑱補「教練主動教的傷害性口令」誤區（接 teaching-errors 框架）

**採納但修改**（5 條）：
- ⑤schema 9 欄 → 核心必填 + 臨床 optional（guard 膨脹/幻覺面：imaging_trigger/diagnostic_criteria/differential 設 optional）
- ②sport_variant → 限游泳相關變體，不擴 water_polo/artistic（守 Vortex 游泳教學定位）
- ⑫協調員 → Opus 整合時親自做一致性審，不另開 agent（省配額）
- ⑮raw 存檔 → 用 references 內 verified 旗標 + 保留研究報告原文，不做 per-injury query log（省 bookkeeping）
- ⑲injury→observation 回流 → 設計 `Observations/injury_cases/` 但延後到建置完成後（非阻塞）

**駁回**（1 條，重要）：
- ⑯m3「修正」Sein 2010 為「JOSPT 40(4):236-243」→ **駁回**。此文確為 *Br J Sports Med* 2010;44(2):105-113，Sonnet 研究員原本就對，**m3 的更正本身是 MiniMax 幻覺**。改列入 W3 待 WebFetch 原文最終核實（連同 m3 質疑的 McKenzie DOI 一起驗）。教訓：m3 的結構性批評可信、具體事實更正不可信，必須各自驗證。

**部分採納**：⑳已先讀 sync_vortex.py 確認 injuries 走新 sync_injuries() 比照現有 public-strip 模式，無架構意外。
