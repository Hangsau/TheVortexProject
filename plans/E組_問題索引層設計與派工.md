# E組 — 問題索引層：設計與派工

> 建立日期：2026-09-11
> 觸發：使用者問「渦流計畫有沒有單一問題解決庫（力學解釋 → 陸上動作 → 水中 drill）」
> 定位：**接線層，不是內容層**。本規劃不新寫技術內容、不增厚介入層。
> 前置依據：`plans/D組_介入層素材盤點.md`（介入層 7 筆是證據上限，不是待辦缺口）

---

## 1. 為什麼是接線而不是寫內容

庫裡四種素材都已存在，但彼此沒有接起來。實測數字（2026-09-11 掃描）：

| 層 | 檔 | 條數 | 是否問題導向 | 指向 drill 的引用數 |
|---|---|---|---|---|
| 誤區 | `canonical/instructional/teaching-errors.yaml` | 104 | 半（以「教練怎麼教錯」為軸） | **2**（Bk22、Bk5） |
| 機制 | `canonical/instructional/technical-analysis.yaml` | 222 | 否（以技術點為軸） | **6** |
| 陸上介入 | `canonical/movement/interventions.yaml` | 7 | 是（`limitation_type` 就是問題） | **0** |
| 水中 drill | `Drills/drills_*.yaml` | 179 | 否（以練習環節為軸） | — |

反向也是空的：**179 個 drill 沒有任何一個指回 canonical ID（實測 0 筆）**。

Drill 唯一帶問題語意的欄位是 `deficiency_fixes`，179 個全有，值域 1–16。但：

- 它是外部書本（*There's a Drill for That!*）的 Common Stroke Deficiencies 編號，專案內只有 `Drills/DRILL_INDEX.md` 第 38 行一句「對應書中編號」，**沒有任何地方寫得出 1 是什麼、16 是什麼**。
- 它與 drill 自己的 `category` 不對齊——值 `1` 的 26 個 drill 橫跨 kick／balance／timing／arm／breathing 五類，值 `11` 的 22 個橫跨 arm 12／kick 8／timing 2。所以**無法從 drill 內容反推編號語意**。

結論：這個編號不能修，只能被取代。專案必須擁有自己的問題 ID 空間。

### 今天現場抓到的一個例子

本次把「蛙式換氣抬頭壓髖」寫進 `breast.err18` + `Br35` + `Br36` 之後，才發現
`movement.intervention.breaststroke-breathing.arm-driven-torso-lift` 講的是同一個機制，
兩邊零連結、我也沒被導向它。這正是「先寫內容再做索引」的後果——所以本規劃先接線。

---

## 2. 設計

### 2.1 新檔位置與理由

`canonical/instructional/problems.yaml`

放在 `instructional/` 而非新開 `canonical/problems/`，是驗證器決定的：`tools/validate.py`
的 `_domain_of_path()` 取 `canonical/` 下第一層目錄當 domain，E008 再拿 domain 去比對
`_taxonomy.yaml` 每個 category 值的 `scope`。新開目錄等於 domain=`problems`，現有
category 值（head／pull／kick／timing…）的 scope 都不含它，會整批報 E008，
被迫改動 taxonomy 30+ 行。放進 `instructional/` 則 domain=`instructional`，**現有值一個都不用改**。

### 2.2 條目 schema

```yaml
- id: prob.breast.head-lift-hip-drop
  stroke: breast                 # 既有 taxonomy 值；跨式問題用 common
  category: head                 # 沿用 instructional scope 的既有 category
  title: "換氣時一抬頭，髖就沉下去"
  public:
    observable: |-               # 池畔看得到的、或泳者自己說得出的現象
      - 換氣那一下臀部明顯下沉、腳跟離開水面
      - 換氣周期比不換氣周期慢
    mechanism_summary: >-        # 一兩句，細節不在這裡，在 links 指到的條目
      重心被往後移、離浮心變遠，身體變成繞著支點翻轉的槓桿。
  links:
    technical_analysis: [breast.tech.5]        # E003 檢查
    drills: [Br35, Br36]                       # E003 檢查
    interventions: [movement.intervention.breaststroke-breathing.arm-driven-torso-lift]
  cross_ref: "游慢一點就不會抬頭壓髖、內划（Insweep）"
  cross_ref_ids: [breast.err18, breast.err13]  # E006 檢查
  coverage_gap: []               # 明列本條哪一欄是空的，見 §2.4
```

**沒有的欄位**，以及為什麼沒有：

- 沒有 `physical_reason` / `evidence` / `source_ids`：問題條目不承擔證據，證據在它指到的
  誤區／機制／介入條目上。索引層自己帶來源會變成第二套真相（違反 canonical 單一真相源）。
- 沒有 `diagnostic` 子樹：判讀語留在原條目。這層是「找得到」，不是「判斷」。
- 沒有 `perception_goal` 之類：**感知不能被規定**，`observable` 只寫看得到的／泳者說得出的。

### 2.3 為什麼不改 Drills/

所有對應關係寫在問題條目的 `links.drills`（一對多）。Drills 檔**零改動**。
反過來在 179 個 drill 各加一個 `problem_ids` 是 179 處編輯、且會產生雙向同步負擔，
收益是零——查詢方向永遠是「我有問題 → 給我 drill」，不是反向。

### 2.4 空格是產出，不是待辦

介入層只有 7 筆，且 D組 已裁定那是**證據上限**：
「真正被研究到可介入程度的硬體邊界，就是踝蹠屈、肩上舉、前鋸肌、核心旋轉這幾個，
其餘是空白而非遺漏」。

所以問題索引上線那天，**多數問題的「陸上動作」欄會是空的**。這是設計結果，要在頁面上
明寫「本項目前沒有符合門檻的陸上介入」，不是留白讓人以為忘了填。

`coverage_gap` 欄位就是給這件事用的，值域三個：`no_intervention` / `no_drill` / `no_mechanism`。
`tools/build_indices.py` 的缺口報告據此產出覆蓋表。

---

## 3. 工作單元

每個 W 完成即 commit；`canonical/` 或 `Drills/` 動到就跑
`build_knowledge_map.py` + `build_indices.py`，並推 `master`（不是 `main`）。

| W | 內容 | 派工 |
|---|---|---|
| **W18** | 骨架 + 驗證器註冊 | `[manual]` |
| **W19** | 問題候選抽取表 | `[delegate: haiku]` |
| **W20** | 候選歸併、定案問題清單 | `[manual]` |
| **W21a** | 蛙式問題條目填寫（試點 / 對照組） | `[manual]` |
| **W21b–f** | 自由式／仰式／蝶式／水下蝶腳／出發轉身 | `[delegate: codex]` 串行 |
| **W22** | `deficiency_fixes` 退役標記 | `[manual]` |
| **W23** | `sync_vortex.py` 出站 | `[delegate: codex]` |
| **W24** | my-site 問題頁 | `[claude: refactor]` |
| **W25** | 覆蓋缺口報告 | `[manual]` |

---

### W18 — 骨架 + 驗證器註冊　`[manual]`

微 diff，不派。

1. 建 `canonical/instructional/problems.yaml`：檔頭註解 + `domain: instructional` /
   `sub: problems` / `schema_version: 1` / `categories:`（照 teaching-errors 的清單抄，
   只留實際會用到的）/ `problems: []`。
2. `tools/validate.py` 三處：
   - `KNOWN_ENTRY_LIST_KEYS` 加 `"problems"`（否則 E001 不檢查條目缺 id）
   - `LINKS_ID_REF_KEYS` 加 `"interventions"`（否則 `links.interventions` 完全不被檢查）
   - 檔頭 docstring 的規則說明同步一行
3. 跑 `python tools/validate.py`，確認仍是 **0 ERROR / 140 WARN**（空 `problems` 不應增減任何一條）。

驗收：validate 數字不變 + 新檔被 `CANONICAL_DIR.rglob("*.yaml")` 掃到（故意寫一個壞 ID 確認 E003 會叫，再刪掉）。

---

### W19 — 問題候選抽取表　`[delegate: haiku]`

純機械讀檔＋列表，不做判斷。

輸出 `plans/E組_問題候選盤點.md`，三張表：

- 表 A：teaching-errors 104 條 → `id | stroke | category | title`
- 表 B：technical-analysis 222 條 → `id | stroke | category | title`
- 表 C：interventions 7 條 → `id | limitation_type | demand_ids | action_ids`

派工 prompt 必含：禁止任何 git 操作；只抄欄位不改寫措辭；不要歸併、不要下判斷、不要建議。

---

### W20 — 候選歸併、定案問題清單　`[manual]`

把 W19 的 333 行歸併成「池畔看得到的現象」。判斷標準：

- 同一個**可見現象**的多條誤區／機制 → 一個問題（例：「抬頭」與「壓髖」是同一條）
- 只是教練口令不同、現象相同 → 一個問題
- 現象看不到、只能靠泳者自述感覺 → **不收**（那是感知層，走 L0–L6 脊椎）
- 現象看得到但庫裡沒有任何機制條目解釋 → 收，`coverage_gap: [no_mechanism]`

**條數不預設**，由歸併結果決定。輸出寫回 `plans/E組_問題候選盤點.md` 的「定案」段。

---

### W21a — 蛙式試點　`[manual]`

蛙式先做的理由：本次剛寫完 `breast.err18` / `Br35` / `Br36` / `breast.tech.13`，
還有那條沒接上的 `movement.intervention.breaststroke-breathing.arm-driven-torso-lift`，
素材最新、最容易驗出接線對不對。

同時這一批要當 W21b–f 的**對照組**——codex 派工前先有一份已驗收的成品可比對。

每條要過：
1. `links.*` 每個 ID 都 grep 得到（validate 會擋，但先自己看一遍）
2. `observable` 是看得到的，不是規定的感覺
3. 三關校正（符合研究 / 反問 / 反推），沒過的列「沒過清單」
4. `coverage_gap` 誠實標，寧可標空不要硬塞近似 drill

驗收後 commit，不等其他泳式。

---

### W21b–f — 其餘五式　`[delegate: codex]`　串行

一式一包，**上一包驗收 + commit 後才發下一包**（D組 W15/W16/W17 就是這個節奏）。

派工 prompt 必含：
- 開頭指令區塊：「立即執行、不要輸出計畫、不要等確認、沒寫檔就是失敗」
- 禁 git 操作（reset / pull --rebase / stash / checkout -- / clean）
- `--sandbox danger-full-access` / `--cd` 鎖在專案目錄
- 每寫完一條立即寫盤
- 附 W21a 成品當 verbatim 範例
- 明寫「找不到對應 drill 就標 `coverage_gap: [no_drill]`，不准塞近似的」

驗收一律看 `git diff` 與 `python tools/validate.py`，不看 exit code。

codex 撞配額 → commit + 寫 HANDOFF + 收工，不排自動續跑。

---

### W22 — `deficiency_fixes` 退役標記　`[manual]`

不刪欄位（179 檔改動零收益），只在 `Drills/DRILL_INDEX.md` 的 schema 註解區加：

```
deficiency_fixes: [1, 2]   # legacy：外部書本 Common Stroke Deficiencies 編號，
                           # 專案內無法解析（值域 1–16，與 category 不對齊）。
                           # 已由 canonical/instructional/problems.yaml 的 prob.* 取代，
                           # 保留僅為回溯原書，不得作為查詢軸。
```

同步 `_INDEX.md` 一行。

---

### W23 — `sync_vortex.py` 出站　`[delegate: codex]`

在 `my-site/tools/sync_vortex.py` 加：

- `PROBLEMS_SRC = VORTEX_SRC / "canonical" / "instructional" / "problems.yaml"`
- `PROBLEMS_DST = HUGO_ROOT / "data" / "vortex" / "problems.yaml"`
- `sync_problems(dry_run)`，照 `sync_teaching_errors()` 的形狀寫

**白名單**（不是黑名單，理由同 `MOVEMENT_COMMON_FIELDS` 的註解）：
`id / stroke / category / title / links / cross_ref / cross_ref_ids / coverage_gap`
＋ `public` 子樹整包 `rec.update(pub)`。

`diagnostic` 不存在於本檔，但白名單照樣寫死，防的是以後有人加。

驗收：`python tools/test_sync_movement.py` 不受影響 +
`grep -c diagnostic my-site/data/vortex/problems.yaml` 為 0。

---

### W24 — my-site 問題頁　`[claude: refactor]`

**不新造視覺方向**：複用 `layouts/vortex/vortex-drills.html` 已驗證的
filterbar + chip + 展開卡版型（同一站、同一 `vortex.css`／`vortex-nav.css`）。
這是 refactor 不是設計任務，所以不觸發「先讀 DESIGN_SYSTEM.md 現生方向」那條——
若實作中發現版型撐不住四欄，停手，那時才走設計流程。

- 新增 `layouts/vortex/vortex-problems.html`
- 新增 `content/vortex/problems/_index.md`（`layout: "vortex-problems"`）
- 篩選軸：① 泳式 ② 環節（category）③ 只看有陸上動作的 / 只看有 drill 的
- 卡片展開＝四欄：**現象 → 力學解釋 → 陸上動作 → 水中 drill**
- 空欄一律顯示「目前庫內沒有符合門檻的項目」，不留空白
- 在 `layouts/vortex/vortex-database.html` 的 `$types` 加一個 `問題` chip 指過來（單行）

上線前 grep 反引號與 `src\.` 確認無機器鍵外洩。

---

### W25 — 覆蓋缺口報告　`[manual]`

`tools/build_indices.py` 加一段 problems 覆蓋統計：

- 有機制、有 drill、有介入（三欄全滿）
- 有機制、有 drill、無介入（預期最大宗）
- 有機制、無 drill
- 無機制

寫進既有的缺口報告輸出。這張表就是之後「要不要增厚介入層」的唯一依據——
D組 說證據到頂了，這張表會顯示到底頂在哪裡。

---

## 4. 不做的事

- **不增厚 `interventions.yaml`**。D組 已裁定 7 筆是證據上限。要加必須先有新素材，不是先有需求。
- **不解碼 `deficiency_fixes`**。已證實不可反推。
- **不碰 `hip.internal-rotation` 方向衝突**（`breast.tech.15` 的 🟠 內旋 vs 兩條已發布 demand 的外旋，引 `src.neumann-2017` / `src.nordin-frankel-2012`）。D組 錯誤 7 記在案、未裁決；問題索引遇到它就標 `coverage_gap`，不在這裡裁。
- **不碰 `udk.tech.28` 措辭衝突**。同上。
- **不改 Drills/ 任何一個檔**（W22 只動 `DRILL_INDEX.md` 說明）。

---

## 5. 狀態

| W | 狀態 |
|---|---|
| W18 | 完成（2026-09-12；0 ERROR / 138 WARN；補地圖接線，詳執行清單） |
| W19 | 完成（2026-09-12；104 + 222 + 7 筆原文） |
| W20 | 完成（73 個可見問題；排除與使用邊界見盤點） |
| W21a | 完成（12 個蛙式問題；詳執行清單） |
| W21b–f | 完成（五包依序驗收與提交；詳執行清單） |
| W22 | 完成（legacy 回溯標記與 _INDEX 已同步） |
| W23 | 完成並上線（公開白名單同步及失敗保留；詳執行清單） |
| W24 | 完成並上線（73 題問題頁、四欄與篩選；線上 309 連結驗收通過） |
| W25 | 完成並推送（四組覆蓋 1／43／26／3；同步 CI 成功，公開資料一致） |

---

W18–W25 實作、驗收、推送與同步均完成；CI／公開頁證據見 `E組_執行清單.md`。
