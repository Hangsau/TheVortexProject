# Step 20 派工規格：my-site 動作圖譜版型

> 自足規格。執行者不需要讀 plan-check、不需要讀 implementation list、不需要問任何問題。
> 目標倉庫：`C:/claudehome/projects/my-site`（Hugo，branch `hugo-source`）。
> 上游資料源：`C:/claudehome/projects/TheVortexProject/canonical/movement/`（唯讀，不要改）。

---

## 0. 執行指令（給派工者複製用）

```
codex exec --sandbox danger-full-access --cd C:/claudehome/projects/my-site "<本檔第 1 節起的全文>"
```

prompt 開頭必須附這段：

> 立即執行，不要輸出計畫，不要等我確認，沒有實際寫出檔案就是失敗。
> 禁止任何 git 操作（commit、reset、pull、rebase、stash、checkout --、clean 一律不准）。
> 完成後只回報：改了哪些檔、`hugo --quiet` 的結果。

---

## 1. 交付物（四個檔，缺一即未完成）

| 檔案 | 動作 |
|---|---|
| `layouts/vortex/vortex-movement.html` | **新建** |
| `static/css/vortex-movement.css` | **新建** |
| `content/vortex/movement/_index.md` | **新建** |
| `layouts/partials/vortex/sidebar.html` | **修改**（加一條目，見 §6） |

**不得動的檔**：`tools/sync_vortex.py`、`data/` 底下任何檔、`static/css/vortex.css`、
`static/css/vortex-joints.css`、`static/css/vortex-injuries.css`、`static/css/vortex-nav.css`、
以及 TheVortexProject 的任何檔。

---

## 2. 這章的定位（決定所有文案怎麼寫，先讀懂再動手）

**這是一份列舉式的圖譜，不是裁定書。** 它回答的是「這個動作涉及哪些關節、哪些肌群」
「做不到時可能是哪幾種情況」。它**不回答**、也不得寫成回答：

- ❌ 游這一式這個相位時，哪塊肌肉主導、各出多少力
- ❌ 某個泳者做不到，是哪一塊肌肉的問題
- ❌ 該練什麼、拉什麼、練到什麼角度

記錄本身已經是照這個定位寫的，逐筆結尾都在明講自己不做什麼（例：「本條不給目標角度，
也不作為伸展或肌力處方的依據」「兩套都是教材技術主張，目前都沒有實證比較，因此本筆
並列保存，不指定其中一套」）。**版型的文案必須延續這個語氣，不要在 overview 或區段
說明裡加上記錄本身刻意避開的斷言**，例如不要寫「找出限制你的那塊肌肉」。

overview 的自介建議照這個意思寫：列出涉及什麼、以及可能有哪些情況；哪一種成立要個別
評估，本章不替任何人判定。

## 2b. 資料狀態與 build 安全

canonical 的 37 筆已於 2026-09-02 全數改為 `publication_status: published`，
`sync_movement()` 實測輸出 **37/37**（actions 7、muscle_groups 9、demands 16、
interventions 5）。**但 my-site 的 `data/movement/` 目前仍不存在**——真正的資料要等
Step 21 的 rollout 順序才由同步腳本生成。

因此兩種情況都要處理：

- `index hugo.Data "movement" "actions"` 在資料未同步時會回 nil。**頁面必須照樣建得起來**，
  `hugo --quiet` 不得有任何 error。
- 資料不存在時，overview 面板顯示一個「**資料尚未同步**」區塊，說明內容在上游 canonical
  已發布、等同步後顯示。**不要**寫成「內容準備中」「敬請期待」這類空話。
- 四個區段各自為空時，該區段整段不渲染（連標題都不出現）。
- **禁止只寫有資料時的分支**，也禁止只寫空資料的分支。每一層都要 `with` / `if` 護，
  兩種情況都要用 §9 的兩段驗證實際跑過。

## 2c. 覆蓋範圍必須寫在 overview（否則空白會被誤讀）

demand 目前覆蓋 **13/58 個相位**：自由式 6 筆、蛙式 4 筆、蝶式 3 筆、起跳轉身 2 筆、
水下海豚腿 1 筆、**仰式 0 筆**。

overview 必須明寫這件事，並講清楚**空白代表「這批還沒蒐證到」，不是「判定不存在」**。
沒有這句話，讀者翻到仰式一片空白會讀成內容判斷。

---

## 3. 資料形狀（verbatim，這是 `sync_movement()` 的實際輸出）

同步後會有四份檔：`data/movement/{actions,muscle-groups,stroke-demands,interventions}.yaml`。
每份的頂層是 `domain` / `sub` / `description` 加**一個清單鍵**，清單鍵各不相同：

| 檔名 | 清單鍵 | 筆數（發布後上限） |
|---|---|---|
| `actions.yaml` | `actions` | 7 |
| `muscle-groups.yaml` | `muscle_groups` | 9 |
| `stroke-demands.yaml` | **`demands`** | 16 |
| `interventions.yaml` | `interventions` | 5 |

`stroke-demands.yaml` 的鍵是 `demands` 不是 `stroke_demands`，抄錯會整段空白且不報錯。

記錄是「白名單記錄層欄位 + `public` 子樹攤平」的結果。以下是真實記錄跑過同步後的樣子：

### 3.1 `actions` 一筆

```yaml
id: movement.action.shoulder-complex.elevation
claim_status: supported
action_status: ready
evidence_profile: anatomy
source_ids: [src.neumann-2017, src.ludewig-2009, src.fernandez-matias-2025, src.aliaj-2021]
name: 肩複合體上舉
aliases: [肩上舉, 手臂上舉, shoulder elevation, arm elevation]
joint_region: shoulder-arm
definition: "肩複合體上舉是上肢在矢狀面、冠狀面或肩胛面向上抬起的複合動作……"
plane: [sagittal, coronal, scapular]
axis: ["矢狀面：冠狀軸", "冠狀面：矢狀軸", "肩胛面：肩胛面垂直軸"]
observable_boundaries: "起點為解剖零位……終點為最大主動或被動上舉角度……"
general_anatomical_capacity: "肩複合體在解剖正常條件下可在多個平面完成完整或接近完整的上舉……"
name_zh: 肩複合體上舉
description: "手臂向上抬起時，肩膀不是只有一個關節在動……"
safety_note: "若上舉時出現疼痛、夾擠感、明顯不穩或麻木感，應立即停止……"
```

### 3.2 `muscle_groups` 一筆

```yaml
id: movement.muscle.scapular-upward-rotators
claim_status: supported
action_status: ready
evidence_profile: anatomy
source_ids: [src.neumann-2017]
name: 肩胛上旋肌群
aliases: [肩胛骨上旋肌群, scapular upward rotators, 上旋肌群]
joint_regions: [shoulder-arm]          # 注意是複數清單，一筆可跨多個部位
cross_joint_characteristics: "本肌群由前鋸肌（下束）與斜方肌……共同組成力偶……"
general_capabilities: "肩胛上旋：……穩定肩胛於胸廓：……協調盂肱空間：……"
roles:
  - name: 肩上舉中的肩胛上旋
    boundary: "此角色在解剖條件正常時成立；具體在何種游泳動作中被多少程度地招募，需泳者 EMG 資料支持……"
name_zh: 肩胛上旋肌群
description: "當手臂向上抬起時，肩胛骨需要同步上旋……"
safety_note: "若感到肩膀夾擠、不穩或疼痛，不要嘗試強制抬高手臂。"
```

### 3.3 `demands` 一筆

```yaml
id: movement.demand.starts-turns.underwater-glide.shoulder-elevation
claim_status: partially-supported
action_status: provisional
evidence_profile: synthesis-inference
source_ids: [src.martens-2015]
stroke: starts-turns
phase_model: descriptive
phase: underwater-glide
body_position: prone
action_reference_frame: joint-local
derived_from_ids: [starts-turns.tech.27, starts-turns.tech.34]
action_ids: [movement.action.shoulder-complex.elevation]
muscle_roles:
  - muscle_id: movement.muscle.scapular-upward-rotators
    role: "在超流線位維持肩胛骨上旋……"
  - muscle_id: movement.muscle.rotator-cuff
    role: "在上舉末端動態穩定盂肱關節……"
measurement_conditions: "……（量測條件與外推邊界，可能缺）"
poolside_direction: "由池畔觀察，雙腿在身體後方伸直併攏，腳尖指向後方"   # 可能缺
name_zh: 水下滑行超流線位的肩上舉需求
description: "出發入水或轉身推蹬後的水下滑行，要求雙臂完全前舉過頭……"
limitation_context: "做不到完整超流線位的原因不只一種，而且不同原因的處理方向完全相反……"
safety_note: "若在超流線姿勢中出現肩部疼痛、夾擠感或麻木，不應強撐維持姿勢……"
```

### 3.4 `interventions` 一筆

```yaml
id: movement.intervention.shoulder-elevation.active-control
claim_status: partially-supported
action_status: provisional
evidence_profile: intervention
source_ids: [src.fone-2022, src.muniz-pardos-2019]
limitation_type: "主動控制不足（肩胛上旋肌群力量或耐力不足，超流線末端無法主動保持）"
action_ids: [movement.action.shoulder-complex.elevation]
demand_ids: [movement.demand.starts-turns.underwater-glide.shoulder-elevation]
mobility_decision: not-routine
dosage_source_ids: [src.fone-2022, src.muniz-pardos-2019]
safety_stop_conditions:
  - 訓練中出現新發或加劇的肩部疼痛立即停止
  - 出現麻木、刺痛或無力感
  - 關節出現明顯不穩定感
remaining_boundary: "目前訓練轉移研究以競技泳者為主，不同族群……的最佳劑量與進退階時程尚無充分資料……"
name_zh: 主動末端控制與容量取向訓練
description: "若肩膀活動度足夠但超流線位維持不住（塌陷或不對稱）……"
works_when_summary: "被動活動度已足夠，但主動維持時姿勢崩潰，且無急性傷或夾擠禁忌。"
fails_when_summary: "被動角度本身不夠，或有急性疼痛、結構性問題，應先處理根本原因。"
training_options: "從岸上肩胛骨主動控制練習開始（wall slides、Y-T-W 系列），進階到阻力帶上舉與水中流線型靜態維持。"
safety_note: "若訓練中出現疼痛加劇、麻木、刺痛或不穩定感，立即停止，不要強撐。"
```

**每個欄位都可能缺**（不同記錄的完整度不同），一律 `with` 護，不要假設存在。

---

## 4. 值域與中文標籤（verbatim；查不到一律 fallback 印原 key）

在 template 頂端定義這幾個 dict。**規則：`{{ $x := index $dict .key }}{{ if not $x }}{{ $x = .key }}{{ end }}`
——Hugo 的 `index` 查不到 key 回空字串且不報錯，沒有 fallback 的話 canonical 一加新值，
頁面標籤就無聲消失。這是本站鐵則，違反即退件。**

```
joint_region / joint_regions:
  shoulder-arm 肩・臂 / spine-neck 脊柱・頸 / hip-knee 髖・膝 / ankle-foot 踝・足

stroke:
  free 自由式 / back 仰式 / breast 蛙式 / fly 蝶式 /
  udk 水下海豚腿 / starts-turns 起跳轉身 / common 共通

phase_model:
  descriptive 描述式分期 / heinlein-2010-phases Heinlein 2010 分期 /
  kudo-power-phase Kudo 動力相 / race-club-6phase Race Club 六相

claim_status:
  supported 有來源支持 / partially-supported 部分支持 /
  contested 有爭議 / unsupported 無來源

action_status:
  ready 可用 / provisional 暫定 / do-not-prescribe 不得處方

evidence_profile:
  anatomy 解剖推導 / swimming-emg 游泳 EMG / swimming-kinematics 游泳運動學 /
  intervention 介入研究 / practice-observation 教學觀察 / synthesis-inference 綜合推論

mobility_decision:
  routine 常規 / conditional 有條件 / not-routine 非常規

action_reference_frame:
  joint-local 關節局部座標 / body-fixed 體固定座標 / poolside-fixed 池畔固定座標
```

**`phase` 不給中文對照表，這是刻意的。** 分期名稱綁定 `phase_model`，跨模型的相位名
**不可互換也不可換算**（例如 descriptive 的 `glide` 與 race-club-6phase 的相位不是同一件事）。
`phase` 一律以**原 key + 所屬 phase_model 中文名**成對顯示，禁止單獨印 `phase`，
也禁止自己造一個跨模型通用的中文相位名。人類可讀的敘述用該筆的 `name_zh`。

**分組清單一律 range 資料產生**，不要在 template 打一份 `joint_region` 或 `stroke` 名單。
資料多出一個新部位／新泳式時要自動出現（標籤 fallback 成原 key），不能靜默漏掉。

---

## 5. 版型結構

骨架照抄 `layouts/vortex/vortex-joints.html` 的兩欄文件頁模式（左常駐目次 + 右全展開面板）。
先讀那個檔，它是本站文件型頁面的參考實作。

```
{{ define "head-extra" }}  → 載入 Google Fonts（同 joints 那行，一字不改）
                            + vortex.css + vortex-nav.css + vortex-movement.css
{{ define "main" }}
  <div class="vx-shell">
    {{ partial "vortex/sidebar.html" (dict "ctx" . "current" "movement") }}
    <div class="vx-stroke-wrap vx-doc">
      <aside class="vx-rail vx-rail--collapsible">   ← 左欄目次
      <main class="vx-panels">                        ← 右欄面板
    </div>
  </div>
  <script src="{{ .Site.BaseURL }}js/vortex.js" defer></script>
```

### 5.1 左欄目次

- 第一項固定：`#overview` →「這章在做什麼」
- 之後四個 `vx-rail-theme` 可收合分組，順序固定：
  **動作 → 肌群 → 泳式需求 → 介入**
- 每組的 `vx-rail-theme-count` 印該組筆數；**該組筆數為 0 時整組不渲染**
- 組內連結文字用 `name_zh`，缺則 `name`，再缺則 `id`

### 5.2 右欄面板（順序固定）

**`#overview`** — 必渲染，即使資料全空。內容要交代四層的關係，用自己的話寫，不要抄本規格：

> 動作（關節能做什麼）→ 肌群（誰驅動）→ 泳式需求（某一式某一相位要求哪些動作）
> → 介入（做不到時分哪幾種原因、各自怎麼處理）。

加一段「怎麼讀誠實標記」：說明 `claim_status` / `action_status` / `evidence_profile`
三個標記各自代表什麼、為什麼要標。**`action_status: do-not-prescribe` 的意思是
「這條不得當成處方使用」，必須在圖例裡講明白。**

資料尚未同步時，這裡再加一塊「資料尚未同步」告示（見 §2b）。覆蓋範圍那段（§2c）
則是**兩種情況都要出現**，不隨資料有無而消失。

**`#actions`** — 按 `joint_region` 分組，每筆一個 `vx-panel`：
標題 `name_zh`（缺則 `name`）→ 誠實標記列 → `description` → `definition` →
`plane` / `axis`（並列小標）→ `observable_boundaries` → `general_anatomical_capacity` →
`aliases`（小字）→ `safety_note`（若有，樣式要跳出來）→ 來源行。

**`#muscles`** — 按 `joint_regions` 分組（一筆可出現在多組，這是正確的，不要去重成單組）：
標題 → 誠實標記 → `description` → `cross_joint_characteristics` →
`general_capabilities` → `roles`（逐條列 `name` + `boundary`，`boundary` 是適用邊界，
必須跟 `name` 同區可見，不可收合）→ `aliases` → `safety_note` → 來源行。

**`#demands`** — 按 `stroke` 分組：
標題 → **相位行：`phase`（原 key）+ phase_model 中文名**（見 §4 的禁令）→ 誠實標記 →
`description` → `body_position` / `action_reference_frame` → `poolside_direction`
（標成「池畔可觀察到什麼」）→ `limitation_context` → `action_ids` / `muscle_roles`
（連到 `#<id>` 錨點，因為那些條目就在同一頁）→ **`measurement_conditions`（若有，
必須與敘述同區顯示，不得收合到看不見——這是量測條件與外推邊界，抽掉它等於把
有條件的結論講成無條件）** → `safety_note` → 來源行。

`derived_from_ids` 指向 canonical 的技術卡 id，本站的 movement 資料裡沒有對應物件，
**印成純文字小字即可，不要造連結**。

**`#interventions`** — 不分組，平鋪 5 筆（`limitation_type` 是整句敘述不是分類鍵，
拿來當分組標題會變成 5 組各 1 筆的文字牆）。每筆：
標題 → **`safety_stop_conditions` 置頂且不可收合**（同呼吸章 `#safety` 鐵則：
停止條件是讀其他每一段的前提，收起來或往下移就會被誤用）→ `mobility_decision`
（醒目標示，例：「活動度處置：非常規」）→ 誠實標記 → `description` →
`limitation_type`（標成「這條在處理哪一種限制」）→ `works_when_summary` /
`fails_when_summary` 並列 → `training_options` → `remaining_boundary`
（標成「還沒解決的邊界」）→ `action_ids` / `demand_ids` 錨點連結 →
`safety_note` → 來源行（`source_ids` 與 `dosage_source_ids` 分兩行，
後者標「劑量來源」）。

### 5.3 來源行（四個區段共用，照抄 joints 的作法）

```
{{ $srcReg := dict }}
{{ with index hugo.Data "vortex" "source-registry" }}{{ with .sources }}{{ $srcReg = . }}{{ end }}{{ end }}
```

渲染規則（三條都是鐵則）：

1. 查得到 → 印 `$s.display`，有 `$s.link` 就掛 `↗` 外連（`target="_blank" rel="noopener"`）
2. **查不到 → 印 `$sid` 本身**。沒有 fallback 的話來源行會無聲消失，讀者會以為這條本來就沒來源
3. `$s.verification_status == "unverified"` → 加 `<span class="vx-src-unverified">未查證</span>`
   （全站 532 筆來源有 359 筆屬此類，專案規範明訂無法查證者不得以肯定句包裝）

只有 ISBN 的書沒有 `link`，這是正確狀態，不要為了每筆都可點去拼書店網址。

---

## 6. sidebar 修改（`layouts/partials/vortex/sidebar.html`）

在第 45–46 行那一項（`vortex/joints/`「骨關節動作 · 命名校正」）**之後**插入一項，格式照抄：

```html
      <li class="vxnav-item{{ if eq $cur "movement" }} is-current{{ end }}">
        <a href="{{ $base }}vortex/movement/"><span class="vxnav-n">動</span>動作圖譜 · 動作與肌群</a></li>
```

joints 那條**保留不動**——那章講的是「池畔講法在解剖上錯在哪」的命名校正，
本章講的是「關節能做什麼 → 誰驅動 → 泳式要求什麼 → 做不到怎麼辦」，兩件事。
這就是規格標題說的「拆兩入口」。

---

## 7. `content/vortex/movement/_index.md`

```markdown
---
title: "動作圖譜"
layout: "vortex-movement"
slug: "movement"
---
```

---

## 8. CSS（`static/css/vortex-movement.css`）

- **所有新 class 一律 `vx-mv-` 前綴**
- **不得 `@import` 或借用** `vortex-joints.css` / `vortex-injuries.css` 的 class
  （那兩份檔名綁特定章節，跨頁引用會讓「這條規則歸誰維護」變模糊）
- 可直接沿用 `vortex.css` / `vortex-nav.css` 既有的共用 class：
  `vx-shell` `vx-stroke-wrap` `vx-doc` `vx-rail` `vx-rail--collapsible` `vx-rail-head`
  `vx-rail-scroll` `vx-rail-list` `vx-rail-theme` `vx-rail-theme-head` `vx-rail-theme-top`
  `vx-rail-theme-caret` `vx-rail-theme-name` `vx-rail-theme-count` `vx-navlink`
  `vx-panels` `vx-panel` `vx-sec-no` `vx-overview` `vx-premise` `vx-read-howto`
  `vx-block-label` `vx-howto` `vx-boundary` `vx-cite` `vx-src-unverified` `vx-flow` `vx-empty`
- 只為本章特有的東西寫新樣式：誠實標記列、相位行、安全停止條件區塊、量測條件區塊、
  資料尚未同步告示、覆蓋範圍說明、錨點交互參照。
- 沿用站上既有設計語言：**無陰影、無圓角、無 hover 位移**，方角規則線。
- **不寫 inline style，不用 `!important`。**

---

## 9. 本機驗證步驟（必做，做完才算交付）

### 9.1 空資料（現況）

```bash
cd C:/claudehome/projects/my-site
hugo --quiet
```

必須零 error。`public/vortex/movement/index.html` 要存在，且內含「資料尚未同步」告示
與 §2c 的覆蓋範圍說明。

### 9.2 有資料（預覽用，驗完必須刪掉）

跑這段產生**臨時**預覽資料（只跑 movement，不要跑整支 `sync_vortex.py`——那會動到
其他章節的 `data/`）：

```bash
cd C:/claudehome/projects/my-site && python -c "
import sys, yaml, pathlib
sys.path.insert(0, 'tools')
from sync_vortex import MOVEMENT_FILES, MOVEMENT_SRC_DIR, MOVEMENT_DST_DIR, movement_public_records
MOVEMENT_DST_DIR.mkdir(parents=True, exist_ok=True)
for name, key, fields in MOVEMENT_FILES:
    d = yaml.safe_load((MOVEMENT_SRC_DIR / (name + '.yaml')).read_text(encoding='utf-8')) or {}
    recs = movement_public_records(d.get(key) or [], fields)
    (MOVEMENT_DST_DIR / (name + '.yaml')).write_text(
        yaml.safe_dump({'domain': d.get('domain'), 'sub': d.get('sub'),
                        'description': d.get('description'), key: recs},
                       allow_unicode=True, sort_keys=False, default_flow_style=False, width=4096),
        encoding='utf-8')
    print(name, len(recs))
"
```

再跑一次 `hugo --quiet`，確認：四個區段都有內容、37 筆全部渲染、左欄四組計數分別是
7 / 9 / 16 / 5、沒有空白標籤、來源行有文字。

**驗完立刻刪除預覽資料：**

```bash
rm -rf C:/claudehome/projects/my-site/data/movement
```

`data/movement/` **絕對不可以留下、不可以進 commit**。真正的資料要等 Step 21
的 rollout 順序（先推 my-site 相容 sync、再合併 canonical）才由 `sync_vortex.py` 生成；
現在先寫進去會把順序顛倒。最後回報前用 `ls data/` 確認它不在。

### 9.3 交付回報

只回報三件事：改了／建了哪些檔、`hugo --quiet` 兩次的結果、`ls data/` 的輸出。
不要 commit、不要 push、不要碰 git。

---

## 10. 退件條件（任一成立即需重做）

1. `data/movement/` 留在 repo 裡
2. 空資料時 `hugo --quiet` 報 error，或頁面沒有「資料尚未同步」告示；或有資料時反而爆掉
2b. overview 沒寫覆蓋範圍 13/58（仰式 0 筆）與「空白＝尚未蒐證、非判定不存在」
2c. 文案出現 §2 明列的三種禁止斷言（誰主導／是哪塊肌肉的問題／該練什麼）
3. template 裡硬編了 `joint_region` / `stroke` 名單，沒有 range 資料
4. 標籤 dict 查不到時印空白（沒有 fallback 印原 key）
5. 單獨印 `phase` 而沒有綁 `phase_model`
6. `source_ids` 查不到時來源行消失，或 `unverified` 沒標「未查證」
7. `safety_stop_conditions` 被收合或不在 intervention 面板最上方
8. `measurement_conditions` 被收合或省略
9. 新 class 沒有 `vx-mv-` 前綴，或 import 了 joints／injuries 的 CSS
10. 動了 `sync_vortex.py`、`data/`、canonical，或執行了任何 git 指令
