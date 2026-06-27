# 週期化內容重做 — 設計文件（Phase 1）

> 狀態：Phase 1 設計（架構定稿）。本文件是整個重做的藍圖，Phase 2–6 依此執行。
> 對應 plan-check 任務：「週期化內容重做：保留游泳實證層、重做 Bompa 骨架、引入競爭框架、重組為多派對話 + 作者綜合」。
> 源頭：`TheVortexProject/canonical/periodization/`；my-site 為呈現端；swim-coach 為 FTS 消費端。

---

## 0. 問題診斷（為什麼要重做）

現有週期化模組的真正問題，不是「全部來自 Bompa」，而是三件具體的事：

1. **骨架是 Bompa 章節的逐節抄寫**。`structure.yaml` 的 `phases`（準備/競賽/過渡）、`annual_plan_types`、`macrocycle`（3:1）、`microcycle`，以及 `zones.yaml` 的 `table_7_1 / table_11_1 / table_11_2 / endurance_phases`，全部是 Bompa《Periodization》單一教科書的 🟡 轉述。讀起來像把一本書濃縮一次。
2. **把「有爭議的領域」呈現成「定論」**。週期化本身是學界active辯論的題目——Issurin 的板塊週期化、Seiler 的極化訓練都直接挑戰 Bompa 的線性/並行假設。現有內容沒有呈現這個張力，讀者會以為 Bompa = 真理。
3. **與 Vortex 核心命題脫節**。Vortex 的核心是「水感知為一切技術的基礎」。但週期化模組純粹是體能/代謝的週期化，完全沒有提到「感知發展（L0–L6）要不要、怎麼週期化」。這是整個 Vortex 專案裡最孤立的一塊。

**另外**：`zones.yaml` 的 `swim_application`（id `periodization.zones.swim`）整節是 🔵 推導——我自己把 Bompa 框架映射到游泳，不是文獻。這種「LLM 自己發明的映射偽裝成知識」要明確標示或重新接地。

---

## 1. 重做後的目標狀態

一句話：**週期化模組從「Bompa 教科書摘要」變成「以泳者/教練的真實問題為骨架、多派框架對話、作者綜合判斷、保留所有已查證游泳實證」的知識模組，且與 Vortex 水感知命題接上一條明確的橋。**

具體可驗收的狀態：
- canonical 不再以 Bompa 章節順序組織，而以**問題清單**（§3）為骨架。
- 每個有爭議的概念都呈現**至少兩派立場**（傳統 / 板塊 / 極化），標明各自證據與適用對象，而非單一定論。
- 所有 🟢 游泳實證節點（Mujika/Bosquet/Hellard/Maglischo/TID 等）**原樣保留、id 不變**（swim-coach 反查不破）。
- 新增「作者綜合」層：在多派之上給出「什麼水準/賽季/年齡選哪派」的判斷。
- 新增一個 Vortex 橋接節點：把感知發展週期化的缺口顯性化（標 🔵/🔴，誠實標示這是作者原創假設）。
- my-site 呈現三派對照；swim-coach FTS 重建後所有舊 id 仍可反查；兩端測試綠。

---

## 2. 來源策略（取代「單一來源」）

| 派別 / 來源 | 角色 | 驗證狀態 |
|---|---|---|
| **Bompa & Buzzichelli**《Periodization》6th ed | 傳統線性週期化代表（保留為「其中一派」，不再是唯一） | 既有，repo 內有書 |
| **Issurin, V.B.**《Block Periodization》(2008) + 《Block Periodization 2》 | 板塊週期化——直接挑戰 3:1 與多能力並行 | ✅ WebSearch 三軸驗證（作者 Wingate Institute、ISBN 9780981718002、概念 = 集中序列 mesocycle blocks）。Issurin 博論主題正是游泳 |
| **Seiler, S.**（極化訓練 / TID） | 強度分布層面的挑戰——80/20、避開中間閾值區 | ✅ 同行評審文獻：Seiler & Kjerland 2006、Seiler 2010 IJSPP「Best Practice for Training Intensity Distribution」 |
| **Olbrecht, J.**《The Science of Winning》 | 游泳專項——有氧無氧「練到最適非最大」、乳酸個體化、質疑閾值訓練 | ✅ 驗證（swim-native，40+ 年奧運經驗，乳酸測試方法論） |
| **Sweetenham & Atkinson**《Championship Swim Training》(2003) | 游泳專項——benchmark sets、青少年到 masters 長期發展、taper 實作 | ✅ 驗證（Human Kinetics, ISBN 9780736045438, 301pp） |
| **Maglischo**（既有 🟢）/ **Hellard 2019** / **Mujika & Bosquet**（既有 🟢） | 游泳實證層，全部保留 | 既有，PMID 可反查 |
| *(選用)* **Counsilman**《The Science of Swimming》 | 歷史錨點——游泳訓練科學化的起點 | 經典文獻，well-established；列為背景，非必讀 |

**反幻覺紀律（沿用 Vortex）**：每個數字必須反查 PMID / 書章 / 表格；人名歸因高風險，引用 Issurin/Seiler/Olbrecht 的具體主張時必須能對到原文；做不到的標 🔴。Phase 2 的 sub-agent 一律帶此紀律、禁 git 操作。

---

## 3. 新骨架：泳者/教練的問題清單（取代 Bompa 章節順序）

這是重做的核心——內容不再按「書的章節」排，而按「教練實際會問的問題」排。每個問題下接「各派怎麼說（張力）→ 游泳實證 → 作者綜合」。

| # | 問題 | 對話的派別 | 對應節點 |
|---|---|---|---|
| Q1 | 一年要怎麼切？衝幾個高峰？ | 傳統（mono/bi/tri/multipeak） vs 游泳實證（Hellard 2–4 macrocycle） | structure.annual.* + swim_annual |
| Q2 | 中週期怎麼堆負荷？「練三休一」是唯一解嗎？ | **傳統 3:1 vs Issurin 板塊集中負荷** ← 核心對話點 | macrocycle + 新 school_block |
| Q3 | 各能力同時練，還是一段時間專攻一項？ | **傳統並行 vs Issurin 序列集中（residual effects）** | phases + 新 school_block |
| Q4 | 強度怎麼分配？大部分時間練多輕/多重？ | **Bompa「週≥50% 賽配速」 vs Seiler 極化 80/20 vs 游泳 TID 實證（87–90% Z1）** | table_7_1 + swim_tid + 新 school_polarized |
| Q5 | 強度分區怎麼定義？百分比、心率、還是血乳酸？ | Bompa %max vs Maglischo 乳酸六區 vs Olbrecht 個體化乳酸 | table_7_1/11_2 + swim_maglischo + 新 olbrecht_model |
| Q6 | 不同距離，能量系統需求差在哪？ | 游泳實證（保留） | swim_energy_by_distance |
| Q7 | 有氧底練到什麼程度？閾值是捷徑嗎？ | **Olbrecht「最適非最大、閾值不是練有氧最佳法」 vs 傳統閾值堆量** | endurance_phases + 新 olbrecht_model |
| Q8 | 賽前怎麼減量達峰？ | 游泳實證（Mujika/Bosquet，保留） | taper.* 全模組 |
| Q9 | 休季/受傷停練，體能掉多快？ | 游泳實證（保留） | detraining |
| Q10 | 青少年分齡怎麼練？有「黃金窗口」嗎？ | 游泳實證 + 爭議標記（保留） | swim_youth_ltad |
| Q11 | **週期化裡，水感知擺在哪？** | Vortex 橋接（作者原創缺口） | 新 perception_periodization_bridge |

---

## 4. 三派骨架（每派的立場摘要）

重寫時，這三派 + 兩個游泳專項聲音 + 作者綜合，是貫穿所有問題的「對話成員」。

**A. 傳統線性週期化（Matveyev → Bompa）**
- 主張：長準備期、漸進負荷、多能力並行、3:1 微週期、單/雙巔峰。
- 證據基礎：數十年實作傳統（🟡）。
- 批評（要寫進去）：對高水準運動員「巔峰維持期」太短、多能力並行互相稀釋訓練刺激。
- 適用：新手、青少年、單一目標賽季——簡單、打底穩。

**B. 板塊週期化（Issurin）**
- 主張：短（2–4 週）高度**集中**的 mesocycle blocks、能力**序列**而非並行、利用「殘留訓練效應（residual training effects）」串接。
- 證據基礎：Issurin《Block Periodization》(2008)，高水準運動員資料。
- 批評（要寫進去）：對新手過度複雜；殘留效應的時長有個體差異。
- 適用：高水準、多賽季密集、需要反覆達峰者。

**C. 極化訓練 / TID（Seiler）**
- 主張：這是**強度分布**層面的主張（不是年度結構）。約 80% 低強度 + 20% 高強度，刻意避開中間閾值區。
- 證據基礎：Seiler & Kjerland 2006、Seiler 2010 IJSPP（菁英耐力選手自然採用）。
- 與游泳的關係（要寫進去）：游泳 TID 實證（swim_tid）顯示金字塔型在游泳也很常見，連衝刺者也 87–90% 在 Z1——極化是參考框架，不是教條。

**D. 游泳專項聲音一：Olbrecht**
- 有氧/無氧能力要練到「**最適而非最大**」；用乳酸測試**個體化**；質疑「在閾值速度練是提升有氧耐力的最佳方式」。
- 角色：把抽象的「強度分區」拉回游泳池實作 + 個體化視角。

**E. 游泳專項聲音二：Maglischo / Sweetenham**
- Maglischo：乳酸六區的實作語言（既有 🟢）。
- Sweetenham：benchmark sets、青少年→masters 長期發展、taper 實作細節。

**F. 作者綜合（Hangsau）— 整合層**
- 核心立場：**週期化不是單一正確模型，而是一組可選工具**；選哪個取決於泳者水準、賽季密度、年齡。
- 新手/青少年 → 傳統線性；高水準多賽季 → 板塊；強度分配 → 以游泳 TID 實證為準（項目別調金字塔/極化）。
- 強度語言：教練實作用 Maglischo 乳酸六區，比 Bompa %max 貼近池畔。
- **Vortex 缺口（誠實標 🔵/🔴）**：現有週期化全是體能/代謝週期化；Vortex 的 L0–L6 感知發展也應該有自己的「週期化」邏輯——什麼階段該鞏固哪一層感知、感知訓練如何隨年度結構安排。這是目前文獻空白，作者原創假設，不可偽裝成定論。

---

## 5. 28 節點 keep / rebuild / new 分類表

> 分類原則：
> - **KEEP** = 證據紮實（🟢，或權威為 Mujika/Bosquet/Hellard 等而非 Bompa 單一轉述）。內容與 id 都不動，最多做口吻潤飾。
> - **REBUILD** = Bompa 單一教科書轉述（🟡）或我自己的 🔵 映射。**id 保留不變**，但內容改寫成「多派對話 + 作者綜合」，數字保留並維持可反查。
> - **NEW** = 新增的競爭框架/橋接節點，新 id，加進**既有檔**的新 top-level key（不另開新檔，避免動 sync/index 的 file allowlist）。

### structure.yaml（9 個 curated 節點 + phases 區塊）

| 節點 id | 現 cert | 分類 | 處理 |
|---|---|---|---|
| `phases`（preparatory/competitive/transition，FTS id `…phases.*`） | 🟡 | **REBUILD** | 接 Q3；加 Issurin 序列 vs 並行對照 |
| `structure.annual.monocycle` | 🟡 | **REBUILD** | 接 Q1；標「適新手/青少年」定位 |
| `structure.annual.bicycle` | 🟡 | **REBUILD** | 接 Q1；保留 ADM T2W 連結 |
| `structure.annual.tricycle` | 🟡 | **REBUILD** | 接 Q1 |
| `structure.annual.multipeak` | 🟡 | **REBUILD** | 接 Q1；與板塊週期化對照 |
| `structure.macrocycle`（3:1） | 🟡 | **REBUILD** | 接 Q2 核心對話：3:1 vs 板塊集中負荷 |
| `structure.microcycle` | 🟡 | **REBUILD（輕）** | 週為單位屬通用，口吻潤飾為主 |
| `structure.detraining` | 🟢 | **KEEP** | Mujika & Padilla 權威，不動 |
| `structure.swim_annual` | 🟢 | **KEEP** | Hellard 2019，不動 |
| `structure.swim_youth_ltad` | 🟢 | **KEEP** | 含 contested 標記，不動 |

### taper.yaml（10 節點）— 整模組 KEEP

| 節點 id | 現 cert | 分類 |
|---|---|---|
| `taper.definition` / `.volume` / `.duration` / `.type.step` / `.type.fast_exponential` / `.swim` | 🟢 | **KEEP** |
| `taper.intensity` / `.frequency` / `.type.linear` / `.peak_window` | 🟡 | **KEEP（輕潤飾）** |

> 理由：taper 模組的權威是 Mujika & Padilla 2003、Bosquet 2007 元分析、Mujika 1996 游泳——不是 Bompa 單一轉述。整模組保留。**選用增補**：可加一個 NEW 小節點承載 Olbrecht 的「減量反應個體化」觀點（Q8 補充），非必須。

### zones.yaml（9 節點）

| 節點 id | 現 cert | 分類 | 處理 |
|---|---|---|---|
| `zones.table_7_1`（Bompa 六分區） | 🟡 | **REBUILD** | 接 Q5；重framing 為「分區法之一」 |
| `zones.table_11_2`（HR/VO2） | 🟡 | **REBUILD（輕）** | 生理對照表通用，潤飾 + 標來源 |
| `zones.table_11_1`（LIEE） | 🟡 | **REBUILD** | 接 Q7 |
| `zones.endurance_phases` | 🟡 | **REBUILD** | 接 Q7：vs Olbrecht 閾值質疑 |
| `zones.swim_maglischo` | 🟢 | **KEEP** | 不動 |
| `zones.swim_three_zone` | 🟢 | **KEEP** | 不動 |
| `zones.swim_energy_by_distance` | 🟢 | **KEEP** | 不動（含跨研究區間紀律） |
| `zones.swim_tid` | 🟢 | **KEEP** | 不動；Q4 與 Seiler 對話的實證基底 |
| `zones.swim`（🔵 映射） | 🔵 | **REBUILD** | 接 Q5；重新接地或明標「作者映射」 |

### 新增節點（NEW，加進既有檔的新 top-level key）

| 新 id | 放入檔 | 內容 |
|---|---|---|
| `periodization.structure.schools_overview` | structure.yaml | 三派框架總覽 + 「工具非教條」的作者立場（§4 F） |
| `periodization.structure.school_block` | structure.yaml | Issurin 板塊週期化：集中序列、殘留效應、適用對象、批評 |
| `periodization.zones.school_polarized` | zones.yaml | Seiler 極化/TID：80/20、避中間區、與游泳金字塔實證的關係 |
| `periodization.zones.olbrecht_model` | zones.yaml | Olbrecht：最適非最大、乳酸個體化、閾值質疑 |
| `periodization.structure.perception_periodization_bridge` | structure.yaml | **Vortex 橋**：L0–L6 感知發展的週期化缺口（🔵/🔴，作者原創假設） |

> 統計：KEEP 17（structure 3 + taper 10 + zones 4）；REBUILD 12（structure 7 含 phases + zones 5）；NEW 5。

---

## 6. id 遷移策略（swim-coach 反查不破）

已查證 swim-coach `scripts/build_knowledge_index.py` 的 `parse_periodization_file()`：
- 反查鍵 = canonical 節點的 `id`（→ FTS `source_id`）。
- list 項有 `id` 用 `id`，無則合成 `periodization.{sub}.{top_key}.{key}`；dict 頂層值同理。
- `_index.yaml`（`_` 開頭）被 skip；推測 indexer 以目錄 glob 收檔。

**策略：**
1. **KEEP / REBUILD 節點：id 一律不動**。REBUILD 只改 `plain_zh` 與 framing 文字、加 `school_*` 對照欄位，不改 `id` / `key` / 頂層 key。→ 反查完全不破。
2. **NEW 節點：加進既有檔的新 top-level key**（不另開 `schools.yaml`），新 id 不撞既有。→ 不需改 `sync_vortex.py` 的 `PERIODIZATION_FILES` allowlist；swim-coach 若為目錄 glob 則自動收，若為 file 列表則同檔自動含。
3. **`_index.yaml`：5 個 NEW 節點同步加 entry**（維護規則硬要求：每 entry id 必須與來源檔一致）。
4. **Phase 5 驗證**：跑 `build_knowledge_index` 後，比對重建前後的 `source_id` 集合，**確認所有舊 id 仍存在**（只增不減不改）；pytest 綠。
5. **數字紀律**：REBUILD 改寫時，所有訓練量/強度/週數/百分比保留原值與原 `source`，不因換 framing 而動數字（反幻覺）。

**風險與預案：**
- 風險：REBUILD 時不慎改到 `key`（合成 id 的一部分）→ 反查斷。預案：REBUILD 前後 diff 每個 `id:` 與 `key:` 行，確認零變動。
- 風險：NEW 節點若改成另開新檔，sync_vortex.py allowlist 漏加 → my-site 不顯示。預案：採「加進既有檔」策略，從源頭避免；若 Phase 4 證實必須新檔，則 allowlist 變更列入 checklist 並驗證。

---

## 7. 執行階段（Phase 2–6）

| Phase | 內容 | 派工 |
|---|---|---|
| **2 多源研究** | 並行 Sonnet sub-agents，每來源一個（Issurin / Seiler / Olbrecht / Sweetenham），反幻覺、禁 git，輸出 `Research/` 筆記，每主張帶可反查來源 | sub-agent（Sonnet） |
| **3 綜合重寫 canonical** | 按 §5 表改寫 REBUILD、新增 NEW、同步 `_index.yaml`、統一 plain_zh 口吻 | **手動 Claude，不派工**（口吻/綜合敏感） |
| **4 my-site 呈現** | `vortex-periodization.html` 加三派對照；跑 `sync_vortex.py`；hugo build；push；CI 綠。**動工前先讀 `resources/notes/DESIGN_SYSTEM.md` 選風格** | 手動 |
| **5 swim-coach 同步** | bump `vendor/vortex` submodule；重建 FTS；驗所有舊 id 可反查；pytest 綠 | 手動 |
| **6 收尾** | `/code-audit`（Opus）；更新兩個 HANDOFF + `_INDEX` + sync_state；commit + push | 手動 |

> 連續執行，階段間不停下來問；只有 context 滿了才換 session（用 HANDOFF 接力）。Phase 1 設計文件因屬基礎，於對話中完整呈現後即進 Phase 2。

---

## 8. 驗收標準

- canonical：5 個 NEW 節點存在且 `_index.yaml` 同步；Q1–Q11 問題骨架在內容中可辨識；每爭議概念至少兩派立場。
- 反幻覺：REBUILD 前後所有數字與 source 不變（diff 驗證）；NEW 節點每主張可反查或標 🔴。
- swim-coach：`build_knowledge_index` 重建後舊 `source_id` 集合無缺漏；pytest 綠。
- my-site：hugo build 成功、三派對照頁可見、CI 綠。
- Vortex 接合：`perception_periodization_bridge` 節點存在，明標 🔵/🔴，不偽裝定論。
