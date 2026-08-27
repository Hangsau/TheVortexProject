# 骨關節動作—肌群—訓練—活動度圖譜：實作計畫（plan-check）

> 建立：2026-08-27（Asia/Taipei）
>
> 狀態：**計畫已保存，待使用者說「開始」後才進入 canonical／my-site 實作**
>
> 觸發：檢視 my-site「骨關節動作 · 命名校正」章，校正錯誤，並延伸到各泳姿動作的肌肉角色、訓練與拉伸／活動度介入
>
> 現有基線：公開章 13 條 `category: joint`；底層稽核 183 條主張（A 解剖 136、B ROM 8、C 泳姿特定 39），C 類尚有 34 條待游泳一手文獻裁決

---

## 0. 決策摘要

本計畫不把現有 13 張命名校正卡硬擴成一份巨型肌肉百科，而是建立兩個互相連結、責任不同的產品：

1. **命名校正章**：保留現有 13 張卡，修正過度絕對或跨越證據能力的敘述，顯示可追溯來源。
2. **泳姿動作圖譜**：新增 canonical `movement/` domain，以「泳式 × 相位 × 體位 × 關節動作」連到肌肉角色、條件式訓練、活動度介入與水中重測。

非協商原則：

- 「補齊拉伸」的定義是**每個已收錄動作都有明確活動度決策**：`條件式適用／不建議常規使用／證據不足`；不是每條肌肉都硬配一個伸展。
- 肌肉不用單一「主肌」欄概括，至少區分：產力、離心煞車、關節穩定、力量傳遞；泳者表面 EMG 不等於肌肉力。
- 解剖教科書只能裁決命名、一般作用線與正常能力；泳姿相位、實際肌肉招募、推進、傷害風險與訓練轉移須各自使用相符證據。
- `public` 只放一般教育內容、適用條件與安全停止條件；教練判讀、測試結果分類與個別分流放 `diagnostic`，my-site 同步時必須剝除。
- Validator 通過只表示結構與可追溯性合格，不代表內容已被科學證實。

---

## 1. Target state

完成時，Vortex 會同時擁有一份已校正、來源可見的 13 條關節命名章，以及一套覆蓋六個游泳領域實際需求的 canonical 動作圖譜；每個公開動作都能追到正確的關節命名、相位與體位、肌肉角色、條件式訓練／活動度決策、安全邊界與來源，而未完成或只有解剖推論的泳姿主張不會被當成已驗證內容發布。

---

## 2. Scope

### 2a. Affected

#### TheVortexProject：既有真相源

| 位置 | 預期變更 |
|---|---|
| `canonical/instructional/technical-analysis.yaml` | 修正 13 條 joint 卡的語意強度、跨層推論與來源；保留既有 ID、`also_strokes`、`joint_region`、`nav_zh` |
| `canonical/periodization/dryland.yaml` | 修正肩部預設 sleeper stretch、蛙腿髖旋轉相位混寫、蹠屈不足卻處方腓腸肌伸展三處問題；保留「被動／主動／疼痛」分流骨架 |
| `canonical/_taxonomy.yaml` | 登錄 movement domain 所需受控值；不挪用現有 `status: complete` 承載證據狀態 |
| `canonical/_sources.yaml` | 重用既有來源 ID；新文獻先去重、查驗 metadata 與可用邊界，再新增穩定 ID |
| `plans/關節主張裁決_*.md` | 作為歷史稽核與原始主張定位；不覆寫舊裁決，新增更正記錄或新的 C 類裁決檔 |

#### TheVortexProject：預計新增 canonical domain

| 檔案 | 單一責任 |
|---|---|
| `canonical/movement/_index.yaml` | 章節順序、讀者路徑、覆蓋範圍與穩定 ID 目錄 |
| `canonical/movement/actions.yaml` | 關節／節段動作定義、平面與軸、可觀察邊界、一般解剖能力 |
| `canonical/movement/muscle-groups.yaml` | 肌群名稱、同義詞、跨關節特性與可承擔的角色；不宣稱任何泳姿一定如何招募 |
| `canonical/movement/stroke-demands.yaml` | 泳式 × 相位 × 體位 × 池畔方向 × 解剖動作，連到 action 與 muscle-role；泳姿專屬主張須用游泳證據 |
| `canonical/movement/interventions.yaml` | 依限制型態整理訓練、活動度／伸展、進退階、劑量來源、水中重測與安全停止條件 |

#### 驗證、索引與測試

| 位置 | 預期變更 |
|---|---|
| `tools/validate.py` | 驗證新 ID、受控詞彙、跨檔引用、來源、public/diagnostic、發布完整性與狀態一致性 |
| `tools/build_indices.py` | 將 movement 記錄納入內容／tag／來源反向索引，產生動作覆蓋缺口視圖 |
| `tools/build_knowledge_map.py` | 新增 movement 摘要與分布，不手改生成結果 |
| `tests/test_movement_atlas.py`（新） | 正向 schema、負向 fixture、空／大量／部分資料、跨檔引用與狀態測試 |
| `tests/test_build_indices.py` | movement 索引與來源反向索引契約 |
| `KNOWLEDGE_MAP.md`、`indices/*.json` | 由工具重生的生成物 |
| `_INDEX.md`、`HANDOFF.md` | 文件導航、完成狀態、剩餘缺口與下一步 |

#### my-site 公開呈現端

| 位置 | 預期變更 |
|---|---|
| `tools/sync_vortex.py` | 新增 movement 同步；只帶 public；草稿／withheld 不發布；以暫存檔＋原子 replace 避免中斷留下半份資料 |
| `data/vortex/movement/*.yaml` | 同步生成物，不手改 |
| `data/vortex/source-registry.yaml` | 只匯出本章實際引用來源的公開白名單欄位（display、作者、年份、identifier、URL、verification status），不帶內部 notes |
| `content/vortex/movement/_index.md` | 新圖譜入口 stub |
| `layouts/vortex/vortex-movement.html` | 依泳式／相位與關節區域雙入口瀏覽；呈現肌肉角色、條件分支、訓練／活動度與來源 |
| `layouts/vortex/vortex-joints.html` | 13 條校正卡顯示來源，並連到圖譜相應 action／demand |
| `layouts/vortex/vortex-stroke.html`、`layouts/vortex/vortex-database.html` | 保留既有 joint 卡消費方式；需要時補圖譜入口，不複製內容 |
| `layouts/partials/vortex/sidebar.html` | 把「命名校正」與「動作圖譜」做成清楚的兩個入口 |
| `static/css/vortex-movement.css` | 新圖譜獨立 class 前綴；不借用傷害頁或 joint 頁的語意綁定樣式 |

#### 下游與外部狀態

- `my-site` 的 `hugo-source` 分支與 GitHub Pages build/deploy。
- TheVortexProject 的 `notify-mysite.yml`，只在 `canonical/**`／`Drills/**` 進 master 後觸發。
- `swim-coach/vendor/vortex`：本階段只做相容性檢查；不新增 movement FTS parser、不更新課表規則。

### 2b. Explicitly excluded

- 不做個人診斷、復健治療、傷後回場判定或醫療替代建議。
- 不建立涵蓋人體所有關節與肌肉的通用解剖百科；範圍限於 Vortex 六個游泳領域實際出現的動作需求。
- 不把「肌肉在動」直接等同「主要推進肌」，不因肌肉被使用就預設需要拉長。
- 不替每個肌肉編造孤立訓練；訓練單位以能力缺口與泳姿轉移目標為主。
- 不改 L0–L6 水感框架，也不把硬體邊界重新包裝成感知缺陷。
- 不手改 `my-site/data/`，也不從 my-site 反向覆寫 canonical。
- 不在本階段把新 domain 接進 swim-coach FTS、診斷規則或自動課表。
- 不刪除原始關節筆記；C 類剩餘 34 條未完成前，原始稽核鏈仍須保留。
- 不趁本計畫整理其他 dryland、傷害或來源登錄債務；只處理與本章直接相撞的內容。

### 2c. Service contexts

| 使用者／環境 | 生命週期與失敗行為 | 補跑方式 |
|---|---|---|
| 作者／教練，本機 Windows 工作區 | 沒有排程；關機、睡眠、離線時不會有漏跑任務，只是尚未 commit／push | 回復連線後先跑完整驗證，再 push；不靠背景程序追趕 |
| my-site 公開讀者 | GitHub-hosted build，不受本機時區影響；Vortex master push 後才會同步 | 正常目標是 push 後 15 分鐘內確認 sync 與 deploy；失敗時以 workflow dispatch 重跑，仍失敗則停止發布並保留舊頁 |
| my-site 維護者／bot | 直接向 `hugo-source` 寫同步資料；若同時有人推相同分支可能 non-fast-forward | rollout 前確認分支與 workflow 無進行中 run；失敗時 rebase／重跑 sync，不強推 |
| swim-coach | vendor submodule 為手動 pin；不會因 Vortex master 更新自動吃到新 schema | 本階段保持舊 pin；未來另立計畫升級 parser，沒有「漏跑後自動追趕」需求 |

### 2d. Dispersed logic scan

| 定義／消費者 | 現況 | 本計畫處置 |
|---|---|---|
| `canonical/_taxonomy.yaml` 的 `category: joint`、`joint_region` | 只覆蓋 13 張命名卡 | 保留；movement 新欄位另登錄，避免改壞 joint 卡 |
| `technical-analysis.yaml` 13 個 stable ID | 同時供頂層 joint 頁與各泳式頁使用 | 原 ID 不變；只修內容、來源與 cross-ref |
| `periodization/dryland.yaml#flexibility_mobility` | my-site 週期化頁直接渲染 | 同步修三處衝突；圖譜收詳細內容，dryland 留總則＋連結 |
| `_sources.yaml` | 所有來源機器鍵真相源 | movement 不另建來源副本；公開端只匯出引用到的白名單視圖 |
| `tools/validate.py` E004／來源／E010 | 目前不知道 movement 的 record types 與新 refs | schema 與驗證器同 commit；先 warning-only 跑真資料，再將低誤報完整性規則升 ERROR |
| `build_indices.py`／`build_knowledge_map.py` | 沒掃 movement | 同步新增 parser；生成物不得手改 |
| `my-site/tools/sync_vortex.py` 常數、sync 函式與 `main()` | 路徑白名單寫死；新目錄會被靜默忽略 | my-site 先部署「新目錄不存在時安全跳過」的 sync，再合併 Vortex canonical |
| `vortex-joints.html` | 顯示 certainty 與 optional evidence，不解析 `source_ids` | 顯示可點來源；不再讓彩色圓點代替引用 |
| `vortex-stroke.html` | 用 `stroke OR also_strokes` 顯示 joint 卡 | 保持同步；圖譜以連結進入，不複製動作內容 |
| `vortex-periodization.html` | 直接呈現 dryland 活動度段落 | dryland 更正會自動傳下；檢查舊措辭不殘留 |
| `vortex-database.html` | 搜尋／瀏覽 technical-analysis | 13 ID 不改，因此相容；需要時只補 movement 新索引入口 |
| `sidebar.html` | 一條「骨關節動作 · 命名校正」 | 拆清楚校正章與完整圖譜，不移除原入口 |
| Vortex `notify-mysite.yml` | canonical master push 後直接 checkout my-site 並同步 | 不改觸發範圍；feature branch 開發，最後只做一次受控 master rollout |
| my-site `sync-from-vortex.yml` | 舊 repository_dispatch／手動備援路徑 | 本計畫不改；只作手動 fallback，不讓兩條 workflow 同時跑 |
| swim-coach `build_knowledge_index.py` | 目前只解析 Vortex `canonical/periodization/*.yaml`，不讀 technical-analysis／movement | 明確排除語意接入；只驗證新目錄不會改既有 FTS 數量或使 build 失敗 |

---

## 3. Execution path

### 3.1 Canonical 資料模型（先定契約，再填內容）

#### 四種記錄，不互相冒用

1. `movement.action.*`：解剖動作與量測邊界。
2. `movement.muscle.*`：肌群的一般能力、跨關節特性與別名。
3. `movement.demand.*`：泳式相位中的動作需求與肌肉角色。
4. `movement.intervention.*`：只有在可辨識條件成立時才採用的訓練／活動度決策。

建議穩定 ID 例：

```yaml
movement.action.shoulder-complex.elevation
movement.muscle.scapular-upward-rotators
movement.demand.streamline.shoulder-complex.elevation
movement.intervention.shoulder-elevation.active-control
```

ID 不含角度數字、證據等級或可變文案，避免內容修正時被迫換 ID。

#### 證據狀態與決策狀態分開

不重用現有 `status: complete`。movement 新增受控欄位：

- `publication_status`: `draft | reviewed | published | withheld`
- `claim_status`: `supported | partially-supported | disputed | unverified`
- `action_status`: `ready | provisional | do-not-prescribe`
- `evidence_profile`: `anatomy | swimming-kinematics | swimming-emg | intervention | practice-observation | synthesis-inference`

`published` 只代表可對讀者發布，不等於所有主張因果確定；`verified` 仍只用於來源 metadata 的查驗狀態。

#### 每筆介入必填的決策欄

```yaml
affirmative_conclusion: 現階段能肯定說什麼
works_when: 哪些可觀察條件成立時適用
fails_when: 哪些條件下無效或不應使用
how_to_identify: 用什麼 ROM、力量、症狀或水中重測分流
action: 實際訓練／活動度步驟與進退階
remaining_boundary: 做完後仍不能回答什麼
```

此外，所有活動度記錄必有 `mobility_decision`：

- `conditional`：確認被動限制且無禁忌時使用。
- `not-routine`：正常活動度、主動控制不足、過度活動或沒有轉移證據時不常規拉伸。
- `evidence-gap`：目前沒有足夠資料給特定處方；保留評估與重測，不捏造動作。

#### public／diagnostic 分層

- `public`：正確命名、一般肌肉角色、教育性訓練選項、`works_when/fails_when` 白話版、公開安全停止條件、來源。
- `diagnostic`：被動／主動 ROM 測量、力量耐力測試、如何分類限制、教練決策樹、個別水中重測判讀。
- 疼痛、急性傷、明顯不穩、麻木無力等「不要強拉」安全訊息必須留在 public；具體診斷推理仍不公開。

### 3.2 證據路由

| 問題 | 可接受來源 | 不可跨用 |
|---|---|---|
| 動作名稱、平面、一般肌肉作用線 | 肌骨教科書／解剖研究 | 不能證明泳姿實際時序、推進或風險 |
| 泳姿相位與關節角度 | 泳者 2D／3D 運動學、明確相位定義 | 靜態正常 ROM 不能代替游泳實測 |
| 肌肉招募 | 泳者 EMG，保留肌肉、泳速、相位與正規化方法 | EMG 振幅不能直接等同肌力、力矩或推進貢獻 |
| 訓練轉移 | 游泳介入研究、系統性回顧，並保留水中 outcome | 一般重量訓練變強不能自動寫成游速提升 |
| 活動度／伸展 | ROM 介入、功能或游泳表現研究 | 相關研究不能證明伸展有效；高於正常的角度不等於更好 |
| 傷害／風險 | 泳者傷害研究、臨床研究、系統性回顧 | 一般解剖碰撞模型不能產生盛行率或式別風險排序 |

本輪已定位、但在 canonical 落地前仍要逐筆查重與確認讀取層級的種子來源：

| 用途 | 識別碼 | 本計畫可用上限 |
|---|---|---|
| Neumann 肌骨解剖 | ISBN 9780323287531，既有 `src.neumann-2017` | 本地全文已核，可裁決解剖命名與一般機制 |
| 肩複合體三維運動 | PMCID PMC2657311 | 全文可讀；支持平面差異，不支持蝶式風險排序 |
| 肩胛運動學系統回顧 | PMID 40845626 | PubMed 層；支持個體／平面變異，不把 120+60 當固定值 |
| 真實盂肱軸向旋轉方法 | PMCID PMC8316370 | 全文可讀；限制用手掌或 Euler 表觀旋轉反推 |
| 踝生物力學 | PMCID PMC4994968 | 全文可讀；支持「PF/DF 為主但有耦合運動」 |
| 自由式頭／胸／髖 roll | PMID 18027307 | 摘要層；只能支持分節段量測，不分配脊椎來源 |
| UDK 系統性回顧 | PMCID PMC9566274 | 全文可讀；支持相位與方法異質性邊界 |
| UDK 肌群／運動學 | PMCID PMC9051435 | 全文可讀；只對該體位、速度與 protocol 外推 |
| 四式游泳 EMG 系統回顧 | PMID 25556010 | 摘要層；支持異質性與不可建單一固定模式 |
| 游泳阻力訓練回顧 | PMID 35099631、31343554 | 摘要層；支持條件式轉移，不指定唯一最佳方法 |
| 蹠屈與 UDK 實驗 | PMCID PMC9402090／PMID 36032263 | 全文可讀；限制正常 PF 會變差，但急性超過正常未再改善 |
| swimmer shoulder 風險回顧 | PMID 37515375 | 已在 registry 有候選／可能重複 ID；落地前先合併查重 |

### 3.3 工作包與提交邊界

#### W0 — 基線凍結與覆蓋分母

- **動作**：建立 feature branch；記錄 git baseline；盤點 13 卡、183 主張、dryland 三處衝突與所有下游消費者；把「要覆蓋哪些泳姿相位」定成機器可讀清單。
- **工具／命令**：`rg`、`python tools/validate.py`、`python -m unittest discover -s tests -v`、`python tools/build_indices.py`。
- **前提**：工作樹沒有不明修改；現有 validator 0 ERROR。
- **停止／fallback**：若有不屬於本任務的修改，先隔離，不覆蓋；若基線本身有 ERROR，先記錄並停止 schema 工作。
- **commit gate**：只提交覆蓋清單／測試骨架，不動公開內容。

#### W1 — 先修現有 13 卡與 dryland（不等新圖譜）

13 卡處置表：

| 組別 | ID | 動作 |
|---|---|---|
| 必修 | `free.tech.38` | 「踝沒有內外旋」改為「距小腿 PF/DF 為主；目視足部三維旋轉不能單獨歸因」；移除「所有蹠屈肌鬆弛」絕對句 |
| 必修 | `free.tech.39` | 把 body roll 與脊椎節間旋轉分開；禁止用靜態 ROM 分配肩／胸／髖線剛體滾轉 |
| 必修 | `udk.tech.30` | 改成「解剖命名不翻，池底／水面方向映射會隨體位改變」；膝與踝也須逐相位映射 |
| 必修 | `fly.tech.37` | 保留上舉平面概念；移除「比自由式更危險／更容易撞」與掌心方向直接等於外旋 |
| 必修 | `starts-turns.tech.48` | 把 120+60 降為教學近似；移除「常見真正限制必在肩胛」的診斷式結論 |
| 降級／分層 | `free.tech.36/40/41`、`back.tech.30`、`breast.tech.36/37`、`starts-turns.tech.47` | 將解剖事實、泳姿推論、教練應用與尚待實測分欄；拿掉必然、主要、異常、伸展一定有效等越界詞 |
| 保留＋補量測邊界 | `free.tech.37` | 保留「掌心方向不能單獨反推旋前／旋後」，補單一視角與節段量測限制 |

dryland 同批修正：

1. 蛙式翻腳依回收／翻腳／推水分相位，不再用「髖內旋讓腳掌外翻」概括。
2. 蹠屈不足不再預設用腓腸肌伸展；改成先辨識被動限制、主動末端控制、前側組織／關節或疼痛。
3. 肩後囊／sleeper stretch 從預設工具降為條件式選項；正常或過度活動度者優先處理容量與控制。

- **前提**：每個新／替換來源有 stable source ID 與 locator；PubMed 摘要不得寫成全文已讀。
- **停止／fallback**：找不到泳姿來源時只保留較窄的解剖結論，`claim_status: unverified` 的泳姿延伸不公開。
- **commit gate**：13 個 ID 全數仍存在；現有泳式與 joint 頁卡數不變；validator／tests 全過。

#### W2 — Schema 與兩條垂直切片 pilot

只先做兩條完整鏈：

1. **超流線肩複合體上舉**：action → scapular/GH muscle roles → passive/active screen → end-range control／capacity → 條件式軟組織介入 → streamline 水中重測。
2. **踝蹠屈與 UDK／flutter kick**：action → plantarflexor/control roles → passive/active PF → end-range isometric／calf capacity → 非預設伸展 → 25m kick／UDK 重測。

- **動作**：先寫 taxonomy、validator 與負向測試，再寫兩條資料；my-site 先用最小模板讀 pilot。
- **前提**：W1 內容與來源邊界已通過人工檢視。
- **停止／fallback**：若兩條 pilot 必須大量重複肌肉或處方文字，先調 schema，不擴到全身；若 public/diagnostic 無法確實剝離，停止上站但可保留 canonical draft。
- **commit gate**：pilot 人工核准後才進 W3；未核准時新 domain 保持 `draft`，sync 必須輸出 0 筆。

#### W3 — C 類 34 條泳姿主張的獨立證據 lane

- **動作**：按既有協議逐條走游泳書 → 本地游泳文獻集 → NCBI 一手研究；每條保留原主張、來源層級、實際文句／數據、裁決與適用邊界。
- **順序**：先處理會影響 W4 相位 mapping 的關節方向／時序／肌肉招募，再處理不影響圖譜骨架的數字與次要推進說法。
- **停止／fallback**：三層皆無時不拿一般解剖補成泳姿事實；只發布 anatomical action，對應 stroke demand 留 `withheld` 或明標證據缺口。
- **commit gate**：按關節區域分批提交；每批來源與裁決同 commit，不把來源先標 verified、內容留到下一批。

#### W4 — 全圖譜分區填充

順序：`shoulder-arm` → `ankle-foot` → `hip-knee` → `spine-neck`。每區都完成 actions、muscle groups、stroke demands、interventions 後才進下一區，避免留下四個半成品檔。

- **動作**：從已凍結的泳姿相位覆蓋清單產生缺口矩陣；每筆 action 至少有一個 muscle-role 判斷，每個 demand 有相位／體位／池畔方向，每個 intervention 有六項 evidence-to-decision 欄與安全邊界。
- **前提**：pilot schema 不再變動；C 類相關條目已有裁決或被 withheld。
- **停止／fallback**：某區資料不足時發布完成區域，缺區明確顯示「尚未完成」，不以空清單冒充完整。
- **commit gate**：一區一 commit；索引計數由工具產生，不手寫總數。

#### W5 — my-site 接線與公開頁

Rollout 順序不能顛倒：

1. 先在 my-site feature branch 完成「movement 目錄不存在時安全跳過」的 sync、模板、來源 registry 與 public/diagnostic 測試。
2. 用本機 Vortex feature branch 做 cross-repo sync 與 Hugo build。
3. 先合併／推送 my-site `hugo-source` 的相容 sync 程式；此時 Vortex master 尚無 movement，公開站不變。
4. 再合併 Vortex canonical 到 master；`notify-mysite` 觸發後才產生並發布新資料。

- **工具／命令**：`python tools/sync_vortex.py --dry-run`、實際 sync、`hugo --minify`、資料洩漏測試。
- **停止／fallback**：Hugo 或 sync 失敗時不推 Vortex master；若 Vortex 已推而同步失敗，舊 joint 頁仍可用，movement route 保持不進側欄或顯示 unavailable。
- **commit gate**：my-site code 與 generated data 分開辨識；generated data 只能由 sync 產生。

#### W6 — 全鏈驗收、發布與交接

- Vortex：重生 map／indices、跑 validator 與完整 tests，第二次重跑必須 zero diff。
- my-site：fresh checkout 重新 sync、Hugo build、檢查 13 卡來源與 pilot／全圖譜頁、確認無 diagnostic 欄位。
- swim-coach：以新 Vortex tree 做 compatibility build；periodization FTS 數與既有測試不應因 movement 新目錄改變。
- 發布：確認沒有同時進行中的同步 workflow；單次合併 master；在 15 分鐘內確認 Vortex sync 與 my-site deploy。
- 交接：更新 HANDOFF「當前狀態／下一步建議」、`_INDEX.md`、MAP 與未解 C 類清單。

---

## 4. Expected risks

### 4a. Runtime risks

| ID | 發生步驟 | 機制 | 後果 |
|---|---|---|---|
| R1 | W1–W4 | 用解剖來源支撐泳姿時序、肌肉招募、傷害或訓練轉移 | 讀者把合理推論當成已驗證事實 |
| R2 | W1/W4 | 把「肌肉有用到」轉成常規拉伸，或方向相反（例如蹠屈不足拉腓腸肌） | 活動度無效、增加不穩或延誤真正問題 |
| R3 | W2/W5 | 新 schema 與寫死路徑的 sync／Hugo consumer 不相容 | canonical 正確但網站靜默缺頁或 build 失敗 |
| R4 | W4 | technical-analysis、dryland、movement 各存一份相似處方 | 幾個月後相互矛盾，來源與更正漂移 |
| R5 | W2/W5 | 評估判讀誤放 public 或 sync 白名單寫錯 | 教練診斷層外洩到公開站 |
| R6 | W1–W4 | `_sources.yaml` 既有 alias／重複來源未先合併 | 同一研究顯示成多份獨立支持，證據權重失真 |
| R7 | W5 | 同步中斷或序列化失敗直接覆寫目的檔 | my-site 留下半份 YAML，下一次 build 壞掉 |
| R8 | W3/W4 | 183 主張與全肌群範圍膨脹，先寫內容後才定 coverage | 長期停在「看似很多、實際缺口不明」的半成品 |
| R9 | W5/W6 | Vortex bot 與人同時推 my-site `hugo-source` | non-fast-forward、遺失同步 commit 或重複 deploy |
| R10 | W4 | 來源族群偏競技成人／單一性別，卻寫成全齡通則 | 違反 Vortex 全光譜受眾契約，兒童、masters、para 被錯誤外推 |

### 4b. Structural risks checklist

| 類別 | 判定 |
|---|---|
| concurrency／shared state | canonical 編寫採單一 writer，不涉及 runtime race；但跨 repo bot push 有 R9，rollout 以單次 master merge 與 workflow preflight 處理 |
| empty input | movement 目錄不存在時 sync 必須安全跳過；若 `_index` 宣稱 published 但 actions 為空，validator 必須報 ERROR |
| large input | 完整 183 主張與所有 movement refs 要在線性時間內完成驗證／索引；測試用合成大量記錄檢查 ID 與 refs，不靠人工抽查 |
| interrupted／partial input | `draft` 可部分存在但不發布；`published` 缺必填欄必須 ERROR；sync 採原子寫入，失敗保留上一版 |
| persistence／schema compatibility | 保留 13 stable ID 與現有 data 檔；新 domain 為 additive；my-site 先支援缺目錄再 rollout |
| migration／backup | 無破壞式資料 migration；git feature branch 與每階段 commit 即 rollback 點；不刪原始稽核資料 |
| malformed YAML／configuration | wrong type、unknown enum、broken ref、duplicate ID、非法 source URL、public 夾 diagnostic 均要有負向 fixture |
| injection surfaces | 無 SQL／SSH／使用者 runtime 輸入；Hugo 不用 `safeHTML` 渲染來源文字，URL 只接受 registry 的 `https`／DOI／PMID 正規連結 |
| producer／consumer status consistency | taxonomy、validator、sync 與 template 必須共用 `publication_status` 語意；只有 `published` 進 my-site，`withheld/draft` 不得出現 |

---

## 5. Risk responses

| 風險 | 可執行 preflight detection | 發生後 recovery／rollback |
|---|---|---|
| R1 證據跨層 | validator 要求每個 `stroke-demand`、肌肉招募與 intervention 各有 `evidence_profile`；review 報告列 anatomy-only 卻含泳姿／傷害／療效語句 | 將越界子句移回 `synthesis-inference` 或 `withheld`；保留較窄解剖結論與原裁決，不用同義改寫掩蓋 |
| R2 不當活動度處方 | `mobility_decision`、`works_when/fails_when/how_to_identify` 與 public safety 缺一即擋發布；負向測試放入正常 ROM、過度活動、疼痛案例 | 立即把介入改 `do-not-prescribe`／移出 public；保留 action 與評估資訊，回到上一個完成 commit |
| R3 consumer 不相容 | my-site 在 Vortex movement 目錄不存在、只有 pilot、完整資料三種 fixture 跑 dry-run＋Hugo | 不合併 Vortex master；若已合併，暫時移除側欄入口並讓 sync skip movement，舊 13 卡頁保留 |
| R4 重複漂移 | `rg` 搜相同 stable ID、訓練名稱與關鍵句；indices 產生跨 domain duplicate／unlinked report | 指定單一 canonical home；其他檔只留一句總則＋`cross_ref_ids`，刪掉衍生副本並重生索引 |
| R5 diagnostic 外洩 | 在同步測試中遞迴掃 output keys；注入 `diagnostic/perception_probe/discriminators` fixture 必須確認輸出為 0 | 阻止 deploy、刪除該次 generated data commit；修白名單後從 clean checkout 重跑 sync |
| R6 來源重複 | `audit_sources.py`、identifier 查重、同 DOI／PMID／PMCID collision 報告；新增來源前 `rg` 全 registry | 沿用存活 stable source ID，更新所有 refs；被合併 ID 留 migration note，不用兩個 ID 同時支撐同一主張 |
| R7 半寫檔 | sync 測試在 dump／replace 前注入例外，確認舊檔 hash 不變；生成後立即 safe-load 全部輸出 | 從 git 恢復上一版 generated file；修復後以 clean tree 完整重跑，不手補半份 YAML |
| R8 範圍失控 | W0 先凍結 coverage denominator；每區由索引輸出 completed／withheld／missing，不用手算 | 停在最後完整區域；未完成區標 draft/withheld，不開公開入口，不用佔位句偽裝完成 |
| R9 push race | rollout 前 `gh run list` 確認無 sync/deploy 進行中，確認 my-site `hugo-source` 最新 SHA；只做一次 Vortex master merge | 不強推；更新 my-site checkout、重跑 sync，產生新的正常 commit；失敗 workflow 用 dispatch 單獨補跑 |
| R10 族群外推 | 每個 intervention 要有 population/context；一般化句子須能指出研究族群與外推邊界 | 收窄到實際研究族群，其他族群標 evidence gap；安全性不明者 `provisional` 或 `do-not-prescribe` |

---

## 6. Overall review

### 6.1 是否有更簡單、移動零件更少的路線？

有，且本計畫已採用：**先修 13 卡與 dryland，再以肩上舉、踝蹠屈兩條垂直切片驗證 schema，通過後才擴全圖譜。**直接一次寫完 183 條會把內容判斷、schema 與網站呈現三種問題混在一起，無法知道失敗在哪一層。

四檔 relational model 比單一巨型 YAML 多幾個引用，但它是必要的最小分離：若把 action、muscle、stroke phase、exercise 全嵌同一筆，同一肌群與訓練會在多個泳式重複，漂移風險更高。

### 6.2 是否超出使用者需求？

沒有。使用者要求校正錯誤、延伸各動作肌群、針對肌群訓練並補齊拉伸；canonical、驗證器與 my-site 同步是讓這些內容可長期維護及公開所需的最小完整鏈。swim-coach 語意接入、個人處方、醫療復健與人體全解剖百科已明確排除。

### 6.3 可執行完成檢查

#### Vortex 結構與內容

```powershell
python tools/validate.py
python -m unittest discover -s tests -v
python tools/build_indices.py
python tools/build_knowledge_map.py
python C:\claudehome\tools\check_map_freshness.py
```

重生後再執行一次，`KNOWLEDGE_MAP.md` 與 `indices/*.json` 必須 zero diff。Validator 的完成條件是 0 ERROR；WARN 必須與實作前 baseline 比對，不得用「總數很多」掩蓋新增警告。

#### movement 契約測試

- [ ] 既有 13 個 joint ID 全部存在、卡數與跨式顯示不變。
- [ ] 5 條必修卡已移除被判定的絕對／跨層句，7 條完成分層，`free.tech.37` 保留並補量測邊界。
- [ ] dryland 三處矛盾不再命中舊句。
- [ ] 每個 `published action` 至少一筆 muscle-role；每筆 role 有 evidence profile。
- [ ] 每個 `published stroke-demand` 有 stroke、phase、body position、pool direction、action refs 與證據狀態。
- [ ] 每個 `published intervention` 有六項 evidence-to-decision 欄、`mobility_decision`、水中重測與 public safety stop。
- [ ] anatomy-only 來源不得單獨支撐 swimmer EMG、推進、傷害風險或療效句。
- [ ] broken ref、重複 ID、unknown enum、非法 URL、published partial record 均被負向測試抓到。
- [ ] 空 movement 目錄安全跳過；大量記錄測試完成；中斷同步不改舊輸出。
- [ ] `draft/withheld` 在 my-site output 為 0；diagnostic key leakage 為 0。

#### my-site 與 rollout

```powershell
python tools\sync_vortex.py --dry-run
python tools\sync_vortex.py
hugo --minify
```

- [ ] 13 張命名卡能看到可點擊的來源名稱，不只顯示色圓或 raw source ID。
- [ ] 新圖譜可按泳式／相位與關節區域進入，兩條路到同一 stable ID。
- [ ] 手機與桌面皆能讀，來源連結為 `https`，無 raw internal notes。
- [ ] 先部署 my-site 相容 sync，再合併 Vortex canonical；順序有實際 workflow 記錄可查。
- [ ] Vortex sync 與 my-site deploy 均成功；若 15 分鐘內未完成則啟動手動 fallback，不宣稱已上線。
- [ ] swim-coach knowledge-index 與既有測試通過，movement 未被意外解析或改變既有 periodization 數量。

### 6.4 Definition of done

只有同時符合下列條件才算完成：

1. 13 卡語意修正、dryland 衝突修正、來源可見。
2. movement coverage denominator 已凍結，所有預定格都有 `published／withheld／missing` 的明確狀態，沒有無聲空白。
3. 每個公開動作都能走完「動作 → 肌肉角色 → 條件辨識 → 訓練或活動度決策 → 水中重測 → 邊界」。
4. 所有適用 gates、validator、tests、Hugo 與 cross-repo sync 通過。
5. 未驗證 C 類與族群外推仍被明確保留，沒有因網站需要完整而補出假結論。
6. HANDOFF、`_INDEX.md`、KNOWLEDGE_MAP、indices 與 GitHub workflow 狀態全部同步。

> 計劃如上。有需要調整的地方嗎？
>
> 確認後可以說「開始」直接執行；多步驟或跨多檔案工作，也可以先要求把計劃保存成可追蹤的 implementation checklist。
