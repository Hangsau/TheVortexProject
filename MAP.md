# MAP — TheVortexProject（游泳教學 canonical 真相源）

> 結構地圖，給冷啟動讀者（人/LLM）。格式與維護流程見 `C:\claudehome\CODEBASE_MAP_METHODOLOGY.md`。
> 行為規範見 `CLAUDE.md`；進度/待辦見 `HANDOFF.md`。
>
> `last_verified: 2026-07-29`

---

## 1. 一句話定位 + 技術棧

**游泳教學的 canonical 知識真相源**，以「水感（perception）優先」為核心：所有技術都是感知發展（L0–L6）的產物，不是反過來。  
**純資料/研究 repo——沒有任何 runtime 程式碼**：內容是 Markdown（研究散文）+ YAML（結構化 canonical）。  
下游消費端：`my-site`（只吃 public 層）、`swim-coach`（吃 public + diagnostic 層）。同步靠**下游**的腳本（`my-site/tools/sync_vortex.py`、`swim-coach/scripts/build_knowledge_index.py`），本 repo 不含同步碼。

---

## 2. 「要做 X → 去讀 Y」決策索引

| 你要做的事 | 動這裡 |
|-----------|--------|
| 改公開內容（網站會顯示的：技術/誤區/drill/L 階段/ADM/週期化） | **改 `canonical/` 對應 YAML**，不改散文 .md |
| 加/改技術分析散文（研究底稿） | `instructional/<泳式>深度技術分析.md` → 再人工整理進 `canonical/instructional/technical-analysis.yaml` |
| 加/改教學誤區 | `instructional/<泳式>教學誤區深探.md`（散文）→ `canonical/instructional/teaching-errors.yaml`（結構） |
| 改 L0–L6 水感框架 | `canonical/technica/{l-indicators,water-sense-levels}.yaml`（散文底稿在 `technica/`、`bridge/`） |
| 改 ADM（運動員發展矩陣） | `canonical/development/{matrix,technical-standards}.yaml` |
| 改週期化 | `canonical/periodization/{structure,taper,zones,_index}.yaml`（研究底稿在 `research/週期化/`） |
| 加練習 drill | `Drills/drills_<泳式>.yaml`（schema 見 `Drills/DRILL_INDEX.md` + 9 軸 fingerprint 見 `Drills/TAG_SCHEMA.md`；新增 drill 必填 9 軸） |
| 找 drill 分布 / 空白格 | `python tools/tag_coverage_report.py`（9 軸交叉表 + 碰撞分析） |
| 改 diagnostic（A/B/C 型診斷、失敗訊號）——**只給教練/swim-coach** | canonical YAML 的 `diagnostic{}` 區塊；**絕不會進 my-site** |
| 加研究主題/假設 | `research/{感知科學,物理現象,週期化}/`，狀態碼見下方 §4 |
| 重生機器索引／查看資料缺口 | `python tools/build_indices.py` → `indices/*.json` |
| 盤點／批次查驗來源 | `python tools/audit_sources.py` 分流；有 identifier 用 `python tools/verify_source_identifiers.py`，只有作者＋年份用 `python tools/search_source_bibliography.py` 產候選；review 後才用 `python tools/apply_verified_sources.py --apply` |

---

## 3. 檔案地圖

### 真相源：canonical/（單一來源，下游全部消費這裡）
| 檔 | 行 | 內容 | public/diagnostic |
|----|----|------|-------------------|
| `development/matrix.yaml` | 375 | ADM 4 支柱 × 5 階段（16 cells，FUN 無 cells） | public{summary,points} + links |
| `development/technical-standards.yaml` | 550 | 22 項技術標準（四式 + 起跳 + 6 轉身） | public{title,framework,phases.criteria} |
| `instructional/teaching-errors.yaml` | 2437 | 6 式 × 76 誤區 | public + diagnostic{type A/B/C} |
| `instructional/technical-analysis.yaml` | 2443 | 6 式 × 188 技術點 | **全 public**（物理層，無 diagnostic） |
| `technica/l-indicators.yaml` | 524 | L0–L6 × 5 式 感知指標矩陣 | public + diagnostic{failure_signal} |
| `technica/water-sense-levels.yaml` | 1616 | 26 個感知級別 | public + diagnostic{type_*} |
| `periodization/{structure,taper,zones,_index}.yaml` | 297/134/223/67 | 週期化（Bompa + 游泳文獻） | 每節點 cert+source+plain_zh+swim_application |
| `perception/free.yaml` | 172 | 自由式感知映射（**stub，多為骨架**） | 待擴充 |

### 研究/散文底稿（餵 canonical，本身不被下游讀）
- `instructional/*.md`（12 檔，280–711 行）— 四式 + 起跳轉身 + 水下蝶腳的技術分析 & 誤區深探
- `technica/*.md`、`bridge/*.md`（6+6 檔）— L 框架 + 感知橋接（**Bridge/ 可能退役，見雷 §4**）
- `research/{感知科學,物理現象,週期化}/`（~25 檔）— 文獻/假設層，狀態碼 🔵🟢🟡🟠🔴
- `Drills/drills_*.yaml`（7 檔，共 **176 drill**，每 drill 9 軸 fingerprint；含 22 個 Race Club 來源的 elite 層）+ `DRILL_INDEX.md` + `TAG_SCHEMA.md`
- `observations/*.md`（3 檔）— 教練觀察案例

### 治理文件
`_INDEX.md`(150) 內容導航 / `RESEARCH_PLAN.md`(341) 研究策略 / `FUTURE_RESEARCH.md`(366) 未解問題池 / `COLLAB.md`(101) 與 Talos 協作 / `三關校正_沒過清單_*.md` QA。

### 機器索引（generated views，不手改）
- `indices/content_index.json` — 770 個 promoted canonical／Drill ID 的內容與概念索引
- `indices/tag_reverse_index.json` — taxonomy field/value → 內容 ID
- `indices/source_reverse_index.json` — 477 個 registry source → 精確使用位置
- `indices/gap_report.json` — 無來源高確定性主張／未使用 taxonomy value／W003 同語意未連結條目
- 生成器：`python tools/build_indices.py`；契約測試：`python -m unittest tests.test_build_indices`

---

## 4. 踩雷點 / 非顯而易見處

1. **public vs diagnostic 分層是這個 repo 的命脈**：canonical YAML 每筆同時含 `public{}`（網站可見）和 `diagnostic{}`（A/B/C 型診斷、失敗訊號、stagnation_by_type）。**diagnostic 絕不可進 my-site**——剝離由 *下游* `my-site/tools/sync_vortex.py` 執行（2026-06-11 audit：0 洩漏）。在這裡改內容時放錯層 = 把教練診斷語洩漏到公開網站。對應記憶 `feedback_perception_language_not_public_content`。
2. **改公開內容要改 canonical YAML，不是改散文 .md**。`.md` 是研究底稿/人工整理來源，下游不讀它們。改了 .md 不跑人工整理 → canonical 不變 → 網站不變。
3. **Bridge/ 六個感知橋接 .md 規劃退役**（`_INDEX.md` 標 Phase E）：內容正被 `canonical/` 取代。改感知內容優先動 canonical，別投資在 Bridge 散文。
4. **占位/未完成檔別當成真內容**：`research/感知科學/隱性_顯性學習.md` 是 0 byte 占位；`canonical/perception/free.yaml` 多為 stub 骨架；週期化 canonical 目前以 Bompa 為主、游泳應用註記仍淺（Phase 2/3 未完）。
5. **canonical/ 目錄結構是下游硬依賴**：`sync_vortex.py` 與 `build_knowledge_index.py` 寫死預期 `canonical/<domain>/*.yaml` 路徑。在這裡 rename 目錄/檔名 = 不動下游碼就會炸下游 build。改名要同步通知 my-site + swim-coach。
6. **Talos 產出是 WIP**：`research/物理現象/教學競技框架_v1.md`（branch `talos-teaching-v1`）標「初稿待自測 + 小樣本驗證」，merge 狀態未定，別當定稿引用。
7. **YAML 內容必過「三關校正」才收**（符合研究 + 反問 + 反推），沒過列入 `三關校正_沒過清單`。對應記憶 `feedback_vortex_content_three_check_verification`。

---

## 5. 邊界 / 別碰

- **這是真相源，my-site / swim-coach 是消費端**：絕不反向——不要為了配合下游而在這裡改格式；下游有自己的呈現層。
- **不要手改 my-site `data/` 或 swim-coach `vendor/vortex`**：那些是這裡的同步產物（my-site 單向 sync，swim-coach 用 submodule pin）。
- **Hestia vault（~344 篇論文）不是主研究源**：週期化研究主要靠外部 PubMed/游泳專門文獻（Bompa/Olbrecht/Seiler/Maglischo…），vault 僅 ~2 篇直接相關。
- **`水感教學研究記錄.xlsx`** 是外部 Google Sheets 快照，未整合進 canonical，人工維護。
