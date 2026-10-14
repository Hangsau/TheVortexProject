# MAP — TheVortexProject（游泳教學 canonical 真相源）

> 結構地圖，給冷啟動讀者（人/LLM）。格式與維護流程見 `C:\claudehome\CODEBASE_MAP_METHODOLOGY.md`。
> 行為規範見 `CLAUDE.md`；進度/待辦見 `HANDOFF.md`。
>
> `last_verified: 2026-10-14`（三層重構收尾時全檔重寫，§2–§4 逐項對照實檔查證）

---

## 1. 一句話定位 + 技術棧

**游泳教學的 canonical 知識真相源**，以「水感（perception）優先」為核心：所有技術都是感知發展（L0–L6）的產物，不是反過來。
內容是 YAML（`canonical/`、`Drills/`，結構化真相源）＋ Markdown（研究散文、研究底稿）；`tools/` 是 Python 驗證與索引工具，沒有對外 runtime。
下游消費端：`my-site`（只吃 public 層）、`swim-coach`（吃 public + diagnostic 層）。同步碼在**下游**（`my-site/tools/sync_vortex.py`、`swim-coach/scripts/build_knowledge_index.py`）；本 repo push 到 `master` 後由 `.github/workflows/notify-mysite.yml` 通知 my-site 自動同步。

**網站三層（2026-10-14 三層重構）**：知識（canonical 生成的知識點頁）／應用（找問題、排課、器材、發展自評）／研究庫（來源條目頁、審查與裁決紀錄、研究筆記、研究底稿）。散文長文已撤出知識區，只在研究庫以「研究底稿」凍結呈現。

---

## 2. 「要做 X → 去讀 Y」決策索引

| 你要做的事 | 動這裡 |
|-----------|--------|
| 改公開內容（技術、誤區、drill、L 階段、ADM、週期化、心理、健康、呼吸、動作） | **改 `canonical/` 對應 YAML**，不改散文 .md（散文不是呈現層） |
| 改泳式頁的動作（51 個） | `canonical/instructional/moves.yaml`（drill 用 ID 連結），my-site 端由 `sync_moves()` 生成 |
| 改問題索引（找問題） | `canonical/instructional/problems.yaml`；契約與測試在 `tests/test_problem_index.py` |
| 改健康傷害 | **改 `canonical/health/drafts/<id>.yaml`**，再跑 `python tools/build_injuries.py` 重生 `injuries.yaml`（直接手改產物 → E019） |
| 改呼吸章 | `canonical/breathing/{safety,framework,physiology,training,regulation}.yaml`；**`_index.yaml` 的 gist 是摘要，本文改了要同步** |
| 改心理 | `canonical/psychology/psychology.yaml` |
| 改 L0–L6 水感框架 | `canonical/technica/{l-indicators,water-sense-levels}.yaml`；「什麼是水感」頁的真相源是 `Technica/水感是什麼.md`（原樣同步） |
| 改 ADM（運動員發展矩陣） | `canonical/development/{matrix,technical-standards}.yaml` |
| 改週期化 | `canonical/periodization/{_index,structure,taper,zones,set-design,dryland,decisions}.yaml` |
| 加練習 drill | `Drills/drills_<泳式>.yaml`（schema 見 `Drills/DRILL_INDEX.md`，9 軸 fingerprint 見 `Drills/TAG_SCHEMA.md`） |
| 找 drill 分布／空白格 | `python tools/tag_coverage_report.py` |
| 改動作—肌群—訓練—活動度圖譜 | `canonical/movement/{actions,muscle-groups,stroke-demands,interventions}.yaml`；相位先登錄 `_taxonomy.yaml#movement_phase_registry`（雷 §4.7） |
| 改 diagnostic（A/B/C 型診斷、失敗訊號）——只給教練／swim-coach | canonical YAML 的 `diagnostic{}` 子樹；**絕不寫進 `public{}`**（E010／W028） |
| 寫修訂紀錄 | 條目最外層 `maintenance_note`（與 `id` 同層、`public` 之外）；公開文字只寫最終說法（W029） |
| 加／改來源 | `canonical/_sources.yaml`（`src.<slug>`）；查驗工具：`tools/audit_sources.py`、`verify_source_identifiers.py`、`search_source_bibliography.py`、`apply_verified_sources.py --apply` |
| 驗證資料契約（改完 canonical 必跑） | `python tools/validate.py` → `reports/validation_report.md`；錯誤碼定義在 `tools/validate.py` 檔頭（E001–E019 ERROR、W001–W029 WARN） |
| 重生人讀地圖／機器索引 | `python tools/build_knowledge_map.py`（`KNOWLEDGE_MAP.md`）＋ `python tools/build_indices.py`（`indices/*.json`）；兩個都是 committed 產物 |
| 查某條結論怎麼來的 | `indices/decision_trail.json`（知識點 ID → 審查／裁決檔段落）；審查紀錄在 `plans/內容審查_*.md`、`plans/關節主張裁決_*.md` |
| 稽核網站分層（無歸屬頁、診斷語、外連、機器鍵、散文漂移） | `python tools/audit_layers.py`（需先 `hugo -d <tmp>/cortex` 建置 my-site）→ `reports/layer_audit.md` |
| 跑 MiniMax 內容初讀 | `python -X utf8 -u tools/review_firstpass.py [--batch 2.1 …]`，輸出 `plans/內容審查_2026-10-14/初讀/`，已完成的塊自動跳過；初讀只是可疑點，每條須第一手驗證 |

---

## 3. 檔案地圖

### 真相源：canonical/（單一來源，下游全部消費這裡）

| 檔 | 行 | 內容 |
|----|----|------|
| `instructional/technical-analysis.yaml` | 3961 | 6 式技術點（物理層，全 public） |
| `instructional/teaching-errors.yaml` | 4117 | 6 式教學誤區（public + diagnostic） |
| `instructional/moves.yaml` | 869 | 泳式頁 51 動作（W3.1 從 my-site 手管 YAML 遷入） |
| `instructional/problems.yaml` | 1635 | 問題索引（找問題入口） |
| `technica/l-indicators.yaml` | 670 | L0–L6 × 5 式感知指標（public + diagnostic） |
| `technica/water-sense-levels.yaml` | 1664 | 感知級別 |
| `development/{matrix,technical-standards}.yaml` | 391／550 | ADM 4 支柱 × 階段；22 項技術標準 |
| `periodization/*.yaml`（7 檔） | 104–1058 | 週期化、強度區、組合設計、陸上訓練、決策 |
| `psychology/psychology.yaml` | 3829 | 心理概念 |
| `health/drafts/*.yaml`（48 檔）→ `health/injuries.yaml` | —／5434 | 健康傷害；**drafts 是真相源**，injuries 由 `build_injuries.py` 生成 |
| `breathing/*.yaml`（6 檔） | 71–162 | 呼吸章：安全置頂、三條線框架、生理機制、訓練、喚醒調節 |
| `movement/*.yaml`（4 檔＋`_index`） | 637–5029 | 動作—肌群—訓練—活動度圖譜（不用 certainty，用四軸狀態，雷 §4.6） |
| `perception/free.yaml` | 85 | 自由式感知映射（stub） |
| `_taxonomy.yaml` | 785 | 受控詞彙、`movement_phase_registry`、證據契約（`evidence_contract`） |
| `_sources.yaml` | 11160 | 來源註冊表，863 筆（含 retracted 墓碑） |

### Drills/
- `drills_*.yaml`（7 檔，179 drill，每 drill 9 軸 fingerprint）＋ `DRILL_INDEX.md` ＋ `TAG_SCHEMA.md` ＋ `_categories.yaml`

### 研究散文（研究庫素材，不是知識區呈現層）
- `Instructional/*.md`（13 檔）：四式＋起跳轉身＋水下蝶腳的技術分析與誤區深探長文 → 網站研究庫「研究底稿」（凍結、剝除診斷語與外連）。例外：`游泳器材使用指南.md` 是應用層文章。
- `Technica/*.md`（7 檔）：L 框架長文 → 研究底稿；`水感是什麼.md` 是「什麼是水感」頁的真相源。
- `Bridge/*.md`（6 檔）：**已退役**，網站不再掛載，保留在 repo 供查。
- `Research/{感知科學,物理現象,週期化,心理}/`：研究筆記，網站研究庫公開 26 篇（標「研究中」）；整本書萃取、內部稽核、`_incoming-hestia-*` 不公開（分類見規劃書 W3.5）。
- `Observations/*.md`（3 檔）：教練觀察案例。

### plans/（審查與規劃紀錄）
- `內容審查_2026-10-01.md`、`內容審查_2026-10-14.md`（＋同名資料夾：初讀、codex 紀錄、規格）：逐條審查紀錄，網站研究庫公開。
- `三層重構與全庫檢查_2026-10-14.md`：三層重構規劃書與 §7 checkpoint。
- `關節主張裁決_*.md`、`證據包_C類_*.md`、`關節主張驗證協議.md`：movement 的關節主張裁決。

### tools/
| 工具 | 用途 |
|------|------|
| `validate.py` | 資料契約驗證（引用、tag、來源、證據分層、診斷外洩、審查軌跡） |
| `build_knowledge_map.py` / `build_indices.py` | 人讀地圖 / 五份機器索引 |
| `build_injuries.py` | health drafts → injuries.yaml |
| `audit_layers.py` | 網站分層稽核（三層重構 Phase 1 閘門） |
| `review_firstpass.py` | MiniMax 初讀（經 `claude-m3-lite`），斷點續跑 |
| `textfold.py` | 接掉 `>-` 折行在中文句中留下的空白（地圖與索引用） |
| `tag_coverage_report.py` | drill 9 軸覆蓋 |
| `audit_sources.py`、`verify_source_identifiers.py`、`search_source_bibliography.py`、`apply_verified_sources.py` | 來源查驗流水線 |
| `classify_w003_orphans.py` | 一次性：W003 孤兒條目分類 |

### 機器索引（generated views，不手改）
- `indices/content_index.json`（1067 筆）、`tag_reverse_index.json`、`source_reverse_index.json`（863 來源）、`gap_report.json`、`decision_trail.json`（560 個知識點有推論紀錄）
- 契約測試：`python -m unittest discover tests`

---

## 4. 踩雷點 / 非顯而易見處

1. **public vs diagnostic 分層是命脈**：診斷判讀語只能放 `diagnostic` 子樹。sync 對 `public` 整包白名單輸出，所以**唯一洩漏路徑是把診斷內容寫進 `public` 底下**——鍵名由 E010 擋、文字由 W028 擋。
2. **散文不是呈現層**：改公開內容改 canonical。散文長文在網站只以凍結的研究底稿出現；改了 .md 不會改知識點頁。
3. **health 的真相源是 drafts**：`injuries.yaml` 是產物，直接改它會被下次重建蓋掉（2026-10-14 曾因此丟失 5 條修正），E019 現在會擋。
4. **跨檔同一主張**：同一個數字或主張常在多檔各寫一次（呼吸 `_index` gist vs 本文、moves vs technical-analysis、健康 vs 發展矩陣）。改任何數字或主張前先 grep 全 canonical。
5. **修訂史不進公開文字**：寫在條目最外層 `maintenance_note`；health drafts 任何層級的 `maintenance_note` 都會被 sync 剝除，其他檔只能放在 `public` 之外。
6. **movement 不用 certainty 五色**：改用 `claim_status`／`action_status`／`evidence_profile`／`publication_status` 四軸。
7. **movement 的相位不是自由字串**：`phase` 只能取 `_taxonomy.yaml#movement_phase_registry` 已登錄的鍵（W017）；泳姿分期沒有單一真相，資料層強制標明出處分期。
8. **關節主張裁決只存在 `plans/`**：`FR-*`／`BK-*` 等 ID 在 canonical 零命中，是待審主張編號；錯誤版本保留不刪。
9. **來源 id 是穩定鍵**：重建書目時 id 字面保留（例：`src.pmc-2018` 實為 Strzała 2017）；重複登錄合併後舊 id 轉 `retracted` 墓碑，墓碑不得被引用（E015）。
10. **canonical 目錄結構是下游硬依賴**：`sync_vortex.py` 與 `build_knowledge_index.py` 寫死 `canonical/<domain>/*.yaml`；改名要同步下游。
11. **線上分支是 `master`**：`git push origin HEAD:master`；推到 `main` 不會觸發 notify-mysite。

---

## 5. 邊界 / 別碰

- **這是真相源，my-site / swim-coach 是消費端**：不要為了配合下游在這裡改格式。
- **不要手改 my-site `data/vortex/` 或 swim-coach `vendor/vortex`**：那些是同步產物。
- **`水感教學研究記錄.xlsx`** 是外部 Google Sheets 快照，未整合進 canonical，人工維護。
