# The Vortex Project — 工作交接單

> 每次有實質推進後更新「當前狀態」與「下一步建議」。規則與背景見 `CLAUDE.md`。

---

## 當前狀態（2026-07-27）

### 進行中——canonical 資料契約升級：S0–S5 完成（S3c／S6 待續）

**基線**：`python tools/validate.py` **0 ERROR／650 WARN**（E001–E011 全 0、**W009 已歸零**；剩 W002 111、W003 476、W011 63）；`python -m unittest discover -s tests` **112 tests OK**。

**S5 四視圖機器索引完成（2026-07-27）**

- 新增 `tools/build_indices.py`，由 promoted canonical + 176 Drills 生成 deterministic JSON；drafts 與 `_` meta 檔不進內容索引，來源／taxonomy 則各讀自己的 canonical registry。
- `indices/content_index.json`：770 個穩定 ID（canonical 594 + Drills 176），含檔案、YAML path、標題、受控 tags、來源與機器關係。
- `indices/tag_reverse_index.json`：7 個 taxonomy field 的反向索引；目前唯一未使用的 taxonomy value 是 `development_stage: fun`（ADM 刻意沒有 FUN cells，屬已知結構空位）。
- `indices/source_reverse_index.json`：476 個已註冊來源及精確使用位置；與內容索引採 nested-entry ownership 邊界，心理 theme 不會誤吃 concept 的 tags／sources。
- `indices/gap_report.json`：高確定性無來源 0、未使用 taxonomy value 1、未連結條目 476；未連結語意刻意與驗證器 W003 完全一致，不把 `cross_ref_ids`／`source_ids` 偷算成內容關係。
- 新增 `tests/test_build_indices.py` 7 tests：巢狀 ownership／來源隔離、四視圖／ID 唯一性、反向索引可解析、gap scanner 活性與 summary、重生 byte-for-byte deterministic。
- **數字釐清**：`_sources.yaml` 的 476 個來源與 W003 的 476 個未連結條目只是同數，並非同一批資料；S3c 查來源識別碼不會自然解掉 W003。

**S3b 批次收尾：102 筆一次寫回（2026-07-27）**

分流實測結果與先前預估的「88 推導 vs 19 複述」**不同**：102 筆裡只有 **11 筆**是真的沒有任何可用來源的獨立主張，其餘 91 筆同 entry 早就有註冊來源，只是 `mechanism`／`physical_reason` 是 `evidence[]` 的**兄弟節點**，繼承規則（只在最近的 `id` 子樹內）拿不到。

| 動作 | 筆數 | 內容 |
|---|---|---|
| 補 `source_ids`（複述同 entry 已註冊的文獻） | 88 | 72 `mechanism` + 16 `physical_reason` |
| 改標 🔵（純物理／解剖推導，無兄弟證據） | 7 | free.tech.11／12／25／28／35、breast.tech.25、starts-turns.tech.45 |
| 改標 🔴（無來源的實證主張，誠實標待查） | 1 | udk.tech.5（核心肌群輪替激活是 EMG 型主張，全庫查無註冊來源） |
| `evidence_from`（綜述句，證據由子條目承擔） | 6 | breast.tech.31、udk.tech.27、starts-turns.tech.40 + psychology 三個 `premise` |
| 順帶降級 certainty | 4 | back.err16 🟢→🟡、breast.err15／starts-turns.err14 🟢→🟠、fly.tech.24 🟢→🟡（唯一來源是 2009 舊文獻或教練實測，原本標綠過頭） |

執行方式：逐行手術腳本（定位 `- id:` → block key → `certainty:`，於其後插入來源鍵），**不做 `yaml.safe_dump` round-trip**——那會摧毀全部註解與折行。套用前先程式驗過「88 筆的來源鍵全在 `_sources.yaml`」與「6 筆 `evidence_from` 的 ID 全解析得到」，零漏。3 個轉 🟠 的條目因帶 `source_ids`（`has_source_info()` 豁免）不會新增 W011。

**S3b 前段（契約 + 驗證器 + 試點）**

1. **證據分層契約落地**（`canonical/_taxonomy.yaml#evidence_contract` + `CLAUDE.md`「證據分層契約」節）。不套單一文獻門檻——那會讓感知層永遠不合格。改成文獻證據（🟢/🟡，需 `source_ids`）與實務證據（🟠，需 `observation_basis` 交代誰觀察／什麼族群／外推邊界，不冒充文獻）兩級並存；`certainty` 逐值寫了 `criterion`，擋「預設標綠」。
2. **W009 誤判 158 筆清除**（270 → 112）。HANDOFF 原本猜「多半是 certainty 標錯」是**錯的**：實測 101 筆是 `references[].citation` 這個 S3a 漏收的來源承載欄位、57 筆是祖先已帶來源的粒度差。驗證器改動：`has_display_source()` 認 `citation`、新增 `iter_blocks_with_source_inheritance()` 做來源沿樹繼承（不跨兄弟條目）。
3. **新增三項檢查**：`W011`（🟠 缺 `observation_basis`，63 筆）、`E010`（診斷型鍵名寫進 `public` 子樹 = 唯一實際洩漏路徑，0 筆）、`E011`（`evidence_from` 的 ID 必須解析得到——它是 W009 的豁免路徑，不驗證就是零成本免罪符，0 筆）。另修一個既存的靜默回報缺口：E008/E009/W010 早有檢查但沒進 `code_meta`，所以從來沒出現在 `reports/validation_report.md`。
4. **10 筆試點分流完成**（W009 112 → 102），驗證分流規則可批次化——批次結果見上表。

**下一步**：S3c（476 筆已註冊來源查 DOI／PMID／ISBN／正式 URL 與查驗日）→ S6（public/private 匯出隔離 + W011 63 筆）。W002 111 筆可另以 S3a-3 純遷移批次處理。

**同期浮出的新項目（尚未動）**
- **W002 111 筆**：絕大多數是 `canonical/health/injuries.yaml` 的 `references[].citation`——有來源顯示字串但缺 `source_ids`，屬純遷移（S3a-3 候選，可派工）。⚠ `injuries.yaml` 是 build 產物，改動要進 `canonical/health/drafts/*.yaml` 再跑 `python tools/build_injuries.py`。
- **W011 63 筆**：🟠 條目缺 `observation_basis`，屬 S6 範圍。

### 進行中——canonical 資料契約升級（S0 + S1 完成）（2026-07-25）

**S1 已完成（commit a04df0a）**：`canonical/_taxonomy.yaml`（受控詞彙表，照現況反向抽取未歸一）、`canonical/_sources.yaml`（來源註冊表空殼 + 欄位契約）、`tools/validate.py`（8 項檢查，ERROR/WARN 兩級）、`tests/test_validate.py`（13 tests 全通過）、`reports/validation_report.md`。`build_knowledge_map.py` 未修改（它硬寫檔名清單，自然跳過 `_` 前綴檔）。

**驗證器首跑實測（規模：canonical 594 條目 + Drills 176 ID = 全域 770 ID）**

| 代碼 | 筆數 | 意義 |
|---|---|---|
| E001 | 6 | `l-indicators.yaml` 的 `levels[]` 用 `key` 不用 `id` — 需領域判斷是否該有 ID |
| E002 | 0 | ID 無重複 |
| E003 | **108** | 斷鏈。① `links.development_stages` 用短鍵 `l2t`/`t2t`，但 matrix.yaml 是 `dev.*.l2t` 全 ID（約 70）② `health/injuries.yaml` 的 `mechanism_link`/`technical_link`/`perception_link` 是中文自由文字（約 38） |
| E004 | 0 | tag 全合法（反向抽取的自洽性檢查通過，抽取邏輯無 bug） |
| E005 | 0 | 尚無條目引用 sources（空殼） |
| W001 | **61** | `cross_ref` 自由文字 → S4 工作量 |
| W002 | **88** | 🟢/🟡 但無 `source_ids` → S3 工作量 |
| W003 | 473 | 孤兒條目；修完 E003 後應大幅下降，不必單獨處理 |

**⚠ 修正先前盤點的錯誤數字**（S1 實測為準）：
- `category`：先前記 291 筆 / 44 相異值 — **錯**，實測 405 筆 / 36 相異值
- `certainty`：先前記 651 筆 — **錯**，實測 1,095 筆（health drafts 的 sub-dict 內也有 certainty，先前只算了頂層）
- `status`：先前記 complete + draft 兩值 — **錯**，實測只有 `complete` 單一值
- **S3 工作量：先前估「🟢🟡 約 164 筆」— 錯**，實際需補來源的是 W002 = **88 筆**

**S2 新發現**：`category` 欄位混用兩套語意 — 教學類別（kick / stroke-cycle…）與健康傷害類別（`A-`/`B-`/`C-`/`D-`/`E-`/`F-` 前綴）共用同一欄位。S2 需先決定是否拆欄位，再談歸一。

### 進行中——canonical 資料契約升級（S0 完成）（2026-07-25）

> 觸發：`CLAUDE.md` 新增「知識索引與證據規範（canonical）」一節（先前未提交，本次隨 S0 提交）。該規範宣告的四項設施 **目前 Vortex 一項都沒有**，本段記錄實作缺口，避免冷啟動誤以為已具備。

**規範 vs 現況落差（2026-07-25 盤點）**

| 規範要求 | 現況 |
|---|---|
| 受控 taxonomy 詞彙表 | ❌ 無檔案。`category` 291 筆 / 44 個相異值 / 7 個單次出現值，無中央登錄 |
| 來源註冊表（`source_id` → DOI/PMID/ISBN/URL） | ❌ 無。`source` 335 + `sources` 160 筆為自由文字，PMID/DOI 塞在括號內 |
| 引用完整性 / tag 合法性驗證器 | ❌ 無。`tools/` 只有 `build_knowledge_map.py`、`build_injuries.py`、`tag_coverage_report.py`，皆只做生成與統計 |
| 四個機器索引 + 缺口報告 | ❌ 無。只有人讀的 `KNOWLEDGE_MAP.md` |

**已具備的基礎（不必重建）**
- 穩定 ID：`domain.sub.entity` 格式，63 個 canonical 檔一致
- `links`（162 筆）已是結構化 ID 陣列 `{standards, drills, l_indicators}` — 本來就可驗證
- `certainty`（651 筆）已是受控 enum 🔵🟢🟡🟠🔴；`status`（70 筆）只有 complete / draft
- `canonical/periodization/_index.yaml` 已建立「`_` 前綴 meta 檔」慣例

**關鍵縮減點**：規範只要求 🟢／🟡 的外部主張需要來源註冊。以 certainty 分布（🔵 205 / 🟢 134 / 🟠 60 / 🟡 30 / 🔴 1）計，真正要遷移的約 164 筆，非 335 筆。

**與 knowledge-hub 的關係**：hub `registry/projects.yaml` 中 vortex 為 `status: planned` / `export_contract: pending` / `P4；必須先完成 public/private 匯出隔離`。hub 閘門要求「所有 tag、source ID、cross-reference 必須可解析」，Vortex 現況直接接 adapter 會全數 hard fail。本升級是 hub P4 的前置條件，**不是**把資料匯入 hub。

### 已完成——Race Club + Science of Swimming Faster 兩本書 4 批整合（2026-06-27 晚）

> 觸發：用戶看完菁英 drill 擴充後問「這兩本書有沒有可以提取到計畫的內容做交叉比對」。盤點 4 批高 ROI 主題，整批執行。中途用戶定下「未來所有書包含我們用的內容都要整理吸收後才寫出來；不要到處引用結果整個內容都是引用拼裝物」——存成 feedback memory `feedback_synthesize_not_citation_patchwork.md`，全程套用。

**Batch 1 — Race Club 結構性擴充（4 子任務）**
- B1.1 Three Styles of Freestyle：既有 free.tech.4/5/6 重寫成深綜述，加入 SPM 範圍、front-end/back-end 力學細節、菁英代表選手、Anthony Ervin 案例
- B1.2 6-phase 拉手週期：free.tech.8 升級加入升力相時長分風格（hip 0.6s+/shoulder 0.3s-）、前象限推進 0.15–0.21s、推進峰值位置依風格變動；新增 free.tech.27（入水手部位置與小指朝下、+13% 到 -9.5% 阻力對照）+ free.tech.28（手指微張製造紊流）
- B1.3 Coupling Motions：free.tech.16 升級加入走路類比、coupling 三必要條件、雙 coupling（旋轉 + 晚期回臂）；新增 free.tech.29（手砸水強度 = 肩旋轉速度同源驅動）
- B1.4 10 Points to Great Start：tech.4 加入頭部位置兩派並陳；新增 tech.41 重心前傾 vs 後仰、tech.42 hyperstreamline+hip lift+ toes pointed、tech.43 起跳三個 coupling 動作、tech.44 自由式 Breakout 七要點

**Batch 2 — Science of Swimming Faster 週期化交叉驗證（3 子任務）**
- B2.1 Ch 9 Periodization：structure.yaml 加入 GAS 三階段框架（Selye 1974/76）作為週期化生物學底層；microcycle 加入 6:1 vs 4:1 vs 7:0 休日模式
- B2.2 Ch 10 Tapering：taper.yaml swim_application 加入 level-stratified gains（高中 5–8% / 大學 2.6–3.2% / 國際級 1.5–2.5%）、no event specificity（跨距離跨泳式一致）、心理面與生理面同等重要
- B2.3 Ch 17 Growth/Development：matrix.yaml dev.physical.l2t/t2t 加入 pre-PHV 速度柔軟度窗口、年幼不是迷你成人生理、PHV-PWV-PSV 順序與肌力跟不上骨架的傷病風險；dev.mental.l2t 加入生理年齡 vs 實際年齡公平性、晚熟者留下機制

**Batch 3 — L4-L6 biomarker 補實測**
- l-indicators.yaml 新增 free.L5.coupling-timing（肩-髖旋轉 0.2–0.3 秒時間差）+ free.L5.lift-phase-duration（升力相時長與風格匹配）

**Batch 4 — 族群差異化（1 子任務 + 1 跳過）**
- B4.1 跳過：Science Ch 18 sports medicine 概論性內容對既有 45 個 health drafts 已無新增價值（rotator-cuff 等深度遠超 Ch 18 提供）
- B4.2 新建 `canonical/development/populations.yaml`：5 大族群（青少年/Masters/女性/開放水/Adaptive）每族群 4–5 個高 ROI 結構洞察 + 3 個跨族群共通原則；整本書 5 章內容綜述進 Vortex 自己的結構，非引用拼裝

**已補完（同日晚）**：populations 端到端 + 跨 repo 自動化
- `sync_vortex.py` 加 `sync_adm_populations`；VORTEX_SRC/HUGO_ROOT 改 env var 可覆寫
- my-site 新建 `layouts/vortex/vortex-populations.html` + content stub + sidebar 入口 + CSS
- `.github/workflows/sync-from-vortex.yml`（my-site）：on `repository_dispatch:vortex-content-updated` 或 manual；checkout 兩 repo → 跑 sync → commit + push hugo-source（觸發 deploy）
- `.github/workflows/notify-mysite.yml`（vortex）：push 到 master 且改 `canonical/**` 或 `Drills/**` 時自動 dispatch
- ⚠ **待用戶完成 PAT 設定才會真正動起來**：見 vortex repo Settings → Secrets → Actions 加 `MYSITE_DISPATCH_TOKEN`

---

### 已完成——drills 菁英層擴充：Race Club 12 新 drill + 4 retag（2026-06-27 下午）

> 觸發：用戶看完 9 軸 UI 後問「菁英 drill 哪裡來、為什麼少」。盤點現況 6 個 elite 全來自《There's a Drill for That》最難的幾個 + 我的 STSpat1，素材池本身就薄。

**動作**：
- 從 `resources/books/Fundamentals_of_Fast_Swimming/`（The Race Club / Gary Hall Sr 2020）派 Haiku agent 平行掃 24 章，extract 36 個 drill；過濾掉跟既有重複的（One arm / Catch-up / Breast Pull with Flutter Kick 等已收），確認 12 個全新 elite-tier 可加。
- 同時審 advanced tier 找出 4 個實質屬於 elite 的 retag：Fl27 每划四踢、UDK3 繫繩最大努力、UDK4 節拍器找頻率、Br20 時速拉手（mph 比賽配速隱喻）。

**12 新 elite drill**：
- 自由式 +8：FrEL1 六踢換邊、FrEL2 四踢二划（衝刺）、FrEL3 Snap 手掌板、FrEL4 高肘撥水（手掌板）、FrEL5 Race Club 全身旋轉、FrEL6 波頂/波底入水、FrEL7 比賽配速短反覆、FrEL8 三秒暫停趕上
- 仰式 +1：BkEL1 仰式 6K1S
- 仰式出發 +3：STEL1 階梯式出發、STEL2 腿驅動跳、STEL3 踢沙灘球（partner）

來源全部 cite Race Club 章節（Ch 6/7/10/13/16/24）。

**結果**：drill 總數 164 → **176**；elite 從 6 → **22**（自由式 8 / 仰式 2 / 蛙式 3 / 蝶式 2 / UDK 3 / 仰式出發 4）。

### 已完成——drills 9 軸特色指紋系統 + 25 個新 drill 填空白格（2026-06-27）

> 觸發：用戶反映「drill 全擠在 category=arm 或 L3 那 38 個泥裡，每個 drill 沒有特色出場機會」。要求重新分類 + 找空白格 + 補新 drill。

**① 設計 9 軸正交標籤系統（`Drills/TAG_SCHEMA.md`）**：
`body_position / constraints / movement_pattern / skill_focus / stroke_phase / drill_function / cognitive_load / tactile_anchor / difficulty_tier`。每軸有明確 enum 與判別準則，每個 drill 在 9D 空間有獨特指紋，可從 9 個角度被檢索（取代原本只能靠 category/L/abc_type 三軸的稀薄分類）。所有既有欄位保留，9 軸為附加，下游 `sync_vortex.py` pass-through 無影響。

**② 139 個既有 drill 全部補完 9 軸（5 commits，每泳式一檔）**：
自由式 28 → 仰式 26 → 蛙式 34 → 蝶式 31 → sculling/UDK/starts-turns 20。`python tools/tag_coverage_report.py` 驗證無重大碰撞（4 組碰撞均為跨泳式同概念 drill，設計上允許）。

**③ 寫 `tools/tag_coverage_report.py` 做 gap 分析**：發現重大空白格——`eyes_closed: 0`、`paddle_amplifier: 0`、`warmup: 2`、`partner_feedback: 1`、`standing: 4`。

**④ 補 25 個新 drill 填空白格（commit fc370b8）**：
- 自由式 +8（FrEC1 閉眼超人趕上、FrPad1 手掌板捕水靜止、FrSt1 站姿高肘軌跡、FrP1 同伴擊掌恢復、FrP2 同伴阻力帶拖游、FrSide1 側躺前手錨定、FrSide2 側躺滑行壓力、FrLow1 戴呼吸管輕鬆捕水）
- 仰式 +5（BkEC1 閉眼流線踢水、BkPad1 手掌板拉手、BkSt1 站姿划手模擬、BkP1 同伴並肩配速、BkLow1 六踢換邊）
- 蛙式 +4（BrEC1 閉眼水下拉手、BrPad1 手掌板外撇、BrSt1 站姿牆邊流線、BrLow1 拉拉踢）
- 蝶式 +3（FlEC1 閉眼蝶腿、FlPad1 手掌板水下恢復、FlSt1 站姿胸壓+髖前後）
- sculling +2（ScFist 握拳划水、ScUW1 水下寬 Y 懸停）
- starts-turns +1（STSpat1 閉眼靠水聲判斷牆距）
- UDK +2（UDKEC1 閉眼垂直蝶腿、UDKLow1 戴呼吸管水下巡航）

來源涵蓋 Counsilman 捕水傳統、Maglischo Swimming Fastest、USA Swimming Foundations、Salo & Riewald、Total Immersion 感知訓練、FINIS 教練資源。

**結果**：drill 總數 139 → **164**；`warmup 2→10` / `eyes_closed 0→6` / `paddle_amplifier 0→4` / `partner_feedback 1→4` / `standing 4→8`。

**⚠ 未做**：
- `DRILL_INDEX.md` 與 `MAP.md` 還沒更新 drill 計數（145/125 已過時，應 → 164）
- 下游 `sync_vortex.py` 還沒跑，my-site `data/vortex/drills.yaml` 仍是舊 139；下次 sync 自動會帶 25 個新 drill + 9 軸欄位過去
- swim-coach 未檢查（pin 在某 commit）

---

### 已完成——感知×週期化「缺口」：從 🔴 純假設升級為 🔵 作者綜合（2026-06-23）

> 觸發：用戶質疑「把感知×週期化叫缺口」的正當性——若兩者本是不同東西，硬找連結永遠不成；若有連結還叫缺口，就該去補而不是只貼標籤。要求掃描他處有無同類誤標。

**① 分類掃描結論**：全 canonical 的「缺口/空白/待補」標記分四類——A 概念橋接缺口（該不該連）、B 素材缺口（某族群無文獻）、C 研究空白（游泳專屬量測不存在）、D 引用待補（DOI/PMID）。B/C/D 都是誠實的資料缺位標記（正確做法，非誤標）；**A 類「硬湊連結」型全專案只有一個——感知×週期化**，且它本就不是「只貼標籤」（已含 hypothesis_zh 三點推論）。沒有需要撤標的假連結。

**② 跑 🔴查證工作流補實證**（CLAUDE.md 規定「不接受搜不到作為結束」）：原節點寫「目前無直接文獻支持此接點」**講過頭**。查證後分兩層——
- 通用層**有據**：Branscheidt et al. 2019（eLife 8:e40578，四來源交叉確認）證實疲勞損害技能「學習」本身非僅執行、延續隔天；Otte/Millar/Klatt 2019 PoST 框架（Front. Sports Act. Living 1:61）證實「技能週期化」是已發表框架；減量研究證實降頻掉 motor sensation。
- 真正仍 🔴 的只剩**水感知（L0–L6）專屬層**：無人直接量測過「水感知品質的週期化」。

**③ 改動**：`canonical/periodization/structure.yaml` perception_periodization_bridge 節點 cert 🔴→🔵、source/hypothesis_zh/status_zh/plain_zh 全改為分兩層誠實標記＋內嵌兩條查實引用；`canonical/periodization/_index.yaml` gist 同步；`FUTURE_RESEARCH.md` 新增 §0.6（水感知的週期化，⭐⭐）。三關校正通過。
- 同步 my-site `data/periodization/`，Hugo build EXIT=0，`public/vortex/periodization/index.html` 含新內容（Branscheidt/PoST/分兩層）。週期化頁 layout 第 166–173 行渲染此節點。

---

### 已完成——背式誤區 5→9 + udk/starts-turns drills 0→5 + Ward 引用全式統一（2026-06-23）

> 觸發：my-site 全站健康檢查（4 路 inventory agent → Claude grep → M3 三輪審查）抓出三個真缺口。用戶授權「該做的就去做、改整理得全部整理好」。全程 canonical-first，補完 sync 進 my-site + Hugo build 驗證。

**① 背式 teaching-errors 5 → 9（`canonical/instructional/teaching-errors.yaml`）**
- 新增 back.err6（直臂划手 / pull / A型）、err7（呼吸無節律 / breathing / C型）、err8（僵直腿過度矯正 / kick / B型，與 err5 踢向錯不同軸）、err9（拱背 / body-position / C型）。
- **刻意停在 9 不灌水到 14**：嚴格套「教練主動這樣教」收錄標準後，多數背式「常見錯誤」文獻實為選手習慣（crossover、高頭位）非教練錯口令。M3 列的 4 條補充候選（划手到大腿/頭不要動/膝蓋出水/永遠六拍）經查證**無一通過收錄標準**——反向驗證 9 是把關非偷懶。
- **邊界透明**：err6/err9 是收錄標準邊界案例（M3 A3/A4 合理質疑），內容已自帶 🟠＋明文揭露爭議（不偽裝鐵案）。

**② udk + starts-turns drills 各 0 → 5（新建 `Drills/drills_udk.yaml`、`Drills/drills_starts-turns.yaml`）**
- UDK1–5（垂直打水 / 流線換面 / 繫繩最大努力 / 節拍器找頻率 / 比賽配速），ST1–5（中池翻滾 / 翻牆踩牆 / 流線測距 / 旗下數划手 / 轉體出水）。
- 管線原本**無此兩 slot**：另在 my-site `tools/sync_vortex.py` 的 `DRILL_STROKES` 加 `udk`/`starts-turns`、layout 補分類名「出發轉身」。
- UDK3「4×5 繫繩」經 WebSearch 確認 yourswimlog 原文逐字相符（M3 B1-1 疑為自創，證偽）。

**③ Ward 引用全式補 2018（資料層＋散文層）**
- `canonical/instructional/technical-analysis.yaml`（蛙式 late-kick）、`canonical/technica/l-indicators.yaml`（breast.L4/L5 兩處）→ Ward 2018（碩士論文 U Hawaii Manoa；亦見 JSR Vol.26）。
- 散文層 `Instructional/蛙式深度技術分析.md`（3 處，含書目行補 (2018)+JSR）、`Technica/技術指標_L級對應框架.md`（2 處）→ Ward 2018，全式統一。
- scope 驗證：三處引用全為 stroke:breast，無跨式 scope creep。

> ⚠ 本輪只動我的 7 檔（teaching-errors / technical-analysis / l-indicators / 2 散文 md / 2 drills）。其餘 untracked（periodization plans、canonical/perception/、蝶式 md 等）為他輪未提交工作，**未 stage**。

---

## 當前狀態（2026-06-22 · 夜）

### 已完成——呼吸訓練輔助軸畢業進 canonical + 呼吸感知 drills 上脊椎（2026-06-22）

> 觸發：MiniMax-M3 v2 審查（Hestia VM `/home/hangsau/vortex-review-2026-06-22.md`）指出呼吸內容單薄。我先驗證 M3 聲稱（filter「bug」其實是內容缺口=只有 1 個呼吸 drill；誤區「沒正確版」半錯=correct_concept 有渲染、真缺的是 cross_ref 連結）。用戶授權「整理要做哪些→規劃→一次執行完」。**未照 M3 處方（身份/topic 入口、L 自評測都違反既有設計原則），只做有價值且原則相容的部分。**

**框架決策：呼吸拆「兩條線」**
- ① 感知線（水中呼吸節律/吐氣/換氣）= 水感一部分，按 L0–L6 分級，住 drills。
- ② 生理線（呼吸肌 IMT/RMT + CO2 耐受）= 硬體側輔助軸，定位**平行於 dryland**，**按負荷分級不按 L 分級**。

**① 感知線：新增 4 個呼吸 drill 進 `Drills/drills_freestyle.yaml`**
- FrBr1 韻律呼吸(L0) / FrBr2 放鬆下沉(L0) / FrBr3 連續涓流吐氣(L1) / FrBr4 兩側換氣(L2)。皆描述「物理/呼吸力學」(吐氣連續、浮力)非規定內在感覺，可分級。誠實標 source「通用游泳教學法（Vortex 整理）」（非 Sherret 書，避免假歸因）。FrBr2 failure_signal 明標偏瘦/低體脂者沉=硬體浮力低非緊張（硬體 vs 感知反推）。sync 後 drills 125→129。

**② 生理線：新建 canonical `health/breathing-training.yaml`（5 節點，安全置頂）**
- **safety（🟢，渲染必置頂）**：缺氧昏迷(SWB)機轉 + CDC MMWR 2015（紐約 1988–2011，16 DUBB / 4 死，17–22 歲男）+ 美國紅十字會/YMCA/USA Swimming 三方聯合聲明（缺氧訓練只能水面做、不能水下）。本軸所有方法零水下憋氣。
- **overview（🔵）**：兩條線框架 + 作者立場（先問瓶頸是感知還是呼吸肌）。
- **imt_rmt（🟡）**：IMT/RMT 證據**分距離看**——MIP 必進步(robust)、但短中距(≤200m)游泳成績無顯著、長距/有氧 modest；協議 **50% MIP**(非 30%，30% 是臨床病人劑量)→80%、30 breaths×2/day、6–12 週、POWERbreathe。誠實反例 Cunha 2019 (PMID 33501396) 菁英 null。
- **co2_tolerance（🔴）**：CO2 表對游泳表現**無實證=游泳脈絡的 bro-science**；陸上做無溺水風險但有迷走暈厥、勿獨自；自由潛水脈絡不外推游泳。
- **grading（🔵）**：回答用戶「呼吸能不能分級」——能，但兩套軸：感知線按 L、呼吸肌按負荷(%MIP)、CO2 表不列入游泳分級。
- **查證**：bounded 證據蒐集派 general-purpose（Sonnet）跑 WebSearch 驗 PMID/DOI，三關校正+框架整合由我做（同 dryland 不派 m3 之理）。
- ⚠ 此檔**未進 _INDEX.md/RESEARCH_PLAN**（health 域非 periodization _index 管轄；injuries 也是獨立 health artifact）。

### 已完成——陸上力量訓練軸畢業進 canonical + 上站（2026-06-22）

> 觸發：能量系統內容上站後，用戶問「接下來要做什麼」→ 我建議把陸訓建成獨立輔助軸（如同 injuries），用 WebSearch 查證非派 m3 → 授權「去做吧」（含最終 commit/push）。

**① 全光譜證據蒐集（WebSearch + 三關校正，非派 m3）**
- 6 輪 WebSearch 涵蓋四軸：B1 整體轉移效果、B2 游泳肩傷害預防、B3 青少年負重安全/PHV/年齡門檻、B4 null/反例。**理由同上批**：m3 走 MiniMax 後端無 WebSearch，撈引用＝吐捏造 PMID，故自做。
- **關鍵反例（三關抓出）**：增強式「有效」多指出發/轉身，對 50/100m 整體游速證據不足（618 人 SR 對水中垂直跳/敏捷無效）；16 篇約 7 篇對游泳表現無顯著效果；臥推未必預測衝刺速度——誠實並列，不只報正向。

**② 新建 canonical `periodization/dryland.yaml`（7 節點）**
- overview（🔵 真正爭論=轉移/排程/成熟度非「能不能變強」）/ transfer_evidence（🟡 有條件成立）/ methods（🟢 最大力量 vs 增強式 vs 專項阻力）/ concurrent_scheduling（🟢 傍晚陸訓+12h 睡眠隔天 100m 無殘留疲勞，JFMK 2023 PMID 37489300 n=8）/ injury_prevention（🟢 內旋>外旋失衡=游泳肩；Kabat D2 彈力帶 RCT PMC10679734；動力鏈優於孤立肩肌）/ youth_safety（🟢 成熟度>實齡；PHV 前只徒手；AAP 2020 e20201011；**成人初學/masters/para 明標 🔴 素材缺口不外推**）/ null_caveats（🟡 誠實反例彙整）。
- 註冊進 `_index.yaml`（新增 dryland 區塊 7 entry）。兩 YAML 經 yaml.safe_load 驗證 OK。

**③ my-site 上站（完整鏈：canonical→sync→layout→build→push）**
- `sync_vortex.py` 的 `PERIODIZATION_FILES` 加入 "dryland"；sync 已跑，`data/periodization/dryland.yaml` 到位。
- **關鍵（rendering-gap 教訓）**：`vortex-periodization.html` hardcode 各節點渲染、不 iterate _index——故新增「主題 5 · 陸上力量訓練」section（7 個 `<details>`）+ 概覽 path-item + 左欄 rail link + zones flow nav 前進連結，全部手動接線；各 section 計數 /4→/5。`hugo` build 通過，grep `public/vortex/periodization/index.html` 確認 7 節點全渲染、3 條 dryland 導航連結到位。

---

## 當前狀態（2026-06-22 · 下午）

### 已完成——週期化內容畢業進 canonical + 建三大能量系統入門 + sync my-site（2026-06-22）

> 觸發：用戶質疑「既然有內容為什麼沒上 vortex；不夠就去捕足夠；m3 流量回來了有缺就補；這些章節有歸類成類型嗎；做陸上訓練 or 更詳細三大能量系統運作+可訓練方式？」→ 授權「好 去做吧」（含最終 commit/push）。修正：先前把已查證內容停在散文層而自滿於「分層紀律」是過度保守，有價值的查證內容該讓它上站。

**① 修 canonical Crowley→González-Ravé 歸因（散文層上批已修、canonical 漏修導致線上版仍錯）**
- `canonical/periodization/zones.yaml`（line 20 註解 / school_polarized source / swim_caveat_zh / plain_zh）、`structure.yaml`（schools_overview polarized weakness_zh）、`_index.yaml`（zones gist）四處全部 Crowley→González-Ravé et al. 2021（PMID 33952709, IJSPP 16(7):913–926）。grep 確認 canonical 已零 Crowley。

**② TID 依距離分流正式補進 swim_tid 節點**
- 新增 `pyramidal_majority_zh`（162 筆 TID：金字塔 89/極化 65/閾值 8）、`distance_split_zh`（短=極化+閾值/中=閾值+金字塔/長=金字塔）、`distance_split_caveat_zh`（觀察歸納非 RCT，9 篇僅 3 篇 1b）；source 加 González-Ravé 2021；plain_zh 與 _index gist 同步更新。

**③ 新建三大能量系統入門節點 `energy_systems_primer`（用戶明點的最高價值缺口）**
- 補上 swim_energy_by_distance（供能比）與 table_11_2（HR 對照）之間缺的「系統本身怎麼運作」入門框架：磷酸原(ATP-PCr,0–10s 爆發,無乳酸)/糖酵解(10s–2min,乳酸限制)/有氧(2min+,持續+負責恢復)三系統 × 主導時長 × 燃料 × 限制因子 × 恢復 × 主導距離 × 訓練方向。系統運作標 🟡（教科書級公認生理），訓練方向標 🔵。caveat 明標三系統連續重疊非開關。已註冊進 _index.yaml。
- **訓練協議已補入**（原規劃派 m3，技術判斷後改自做）：m3 走 MiniMax 後端無 WebSearch（Anthropic 伺服端工具），派它撈引用＝吐捏造 PMID 的最高幻覺風險，故撤回派工、改由 Claude 自己 WebSearch 查證。`training_protocols` 區塊（5 條）：磷酸原 6–15s/休90–120s/5–10reps 🟠；糖酵解-乳酸生成 25–50m 最大努力/長休/300–500m 🟠（British Swimming 指南）；乳酸耐受 35–100m/50m 常用/48h 恢復 🟠；SIT 實測 4×50–8×50 誘發 12–18mmol 🟢（PMC8607769）；有氧交叉引用 liee_methods+Maglischo 🔵。保留 1 🔴 `protocol_caveat_zh`：多為教練指南/共識層非 RCT 最適化，RCT 級協議比較仍是研究空白。

**④ my-site 同步（已執行，與上批不同）**
- `python tools/sync_vortex.py` 已跑：periodization 三檔 + 上批已提交的 instructional（水下蝶腳/出發轉身）+ drills/technical-analysis 全部propagate 到 my-site `data/`。canonical 三 YAML 經 `yaml.safe_load` 驗證 OK。

---

## 當前狀態（2026-06-22）

### 已完成——整合 Hestia VM 兩份游泳研究報告進 research/instructional 散文層（2026-06-22）

> 觸發：用戶指示「VM 內 /home/hangsau/.claude/research 有游泳報告，拉回看 TheVortexProject 有沒有用 → 研究怎麼擴充銜接進去 → 規劃好直接動手不用再問」。兩份報告經 SCP 拉回 `research/_incoming-hestia-2026-06-20/`：① water-training-breakthroughs（有用）② dryland-vs-water（邊際價值）。

**整合原則**：全部進 research/ 與 instructional/ 的**散文底稿層**（下游 my-site 不讀此層），**未動 canonical**。每筆引用動筆前逐一 WebSearch 查證，校正報告多處歸因錯誤。

**週期化 research 層（補 4 + 新建 2）**
- `極化訓練_Seiler.md`：新增「TID 依主項距離分流」（González-Ravé 2021；短=極化+閾值/中=閾值+金字塔/長=金字塔，標證據等級限制）；**修正既有檔的 PMID 33952709 歸因錯誤**（原誤標 Crowley→實為 González-Ravé，WebSearch 確認）。
- `板塊週期化_Issurin.md`：新增 6.5 游泳板塊/反向週期化仍缺 RCT 驗證（9 篇 SR 僅 3 篇 1b）。
- `Sweetenham_游泳訓練實作.md`：新增反向週期化缺 RCT 註記；報告的「2022 reverse periodization review」聲稱**無法獨立查證 → 標 🔴 未寫成事實**。
- `頂尖教練訓練哲學_Sandbakk.md`（新）：Sandbakk 2025（PMID 40278987，12 挪威世界級教練/380+ 獎牌/8 奧運耐力項目）。**校正報告蒸餾**：報告把「傳統週期化+taper」「高量低強度+2–3 關鍵日」投票駁回(0-3)，但 WebSearch 追原文(PMC12031707)確認這正是原文結論 → 以原文為準。
- `低通氣訓練_VHL_RSH.md`（新）：Woorons 2016（PMID 26741118）+ Trincat 2017（PMID 27294771）+ Précart 2025 統合分析（Sports Med Open 11:55）；機制=無氧糖酵解；限制 n=16 小樣本；明標不涉感知層、對兒童/初學無外推。保留 2 🔴（Woorons 秒數待追原文、Précart PMID 待核）。

**Instructional 層（補 2 檔）**
- `水下蝶腳技術分析.md`：新增 3.6 末段速度衰退與垂直波幅控制（Veiga 2023 PMID 36756980；η²=0.65 速度受損，軀幹傾角為因，垂直波幅為控制槓桿）+ 4.4 新增即時生理指標盲區（Marinho 2022 PMID 35177993；HR/即時乳酸無差異、RPE 顯著升高）。**釐清 Marinho 與既有 Hvid 2024 為互補非矛盾**（即時小差距 vs 賽後累積，協議不同不可直接比）。
- `出發與轉身技術分析.md`：新增 1.5 陸地肌力訓練對出發的加成（Thng/Pearson/Keogh 2019 SR + Yang 2025 RCT PMC11877300），框定「**增益器非分水嶺**」、效益集中出發/轉身/衝刺、介入效果仍未定論。**校正報告歸因錯誤**：報告把此 SR 誤標 Beattie 2020、且兩篇不同論文重複給同一 PMID 32149877 → 改用正確歸因 Thng et al.。新增 1 🔴（轉身陸地訓練證據稀薄），全檔 🔴×8。

**三關校正結論**：所有新內容過「符合研究 / 反問 / 反推」三關；報告的二手再詮釋與原文落差均已標注並以查證後原文為準；無法獨立查證的聲稱一律標 🔴 不寫成事實。

**my-site 同步**：本批**未觸發**——全部落在 research/instructional 散文層，canonical 未動，故 my-site sync 不需執行（待這些內容日後升格進 canonical 才觸發同步）。

**待清理**：`research/_incoming-hestia-2026-06-20/`（兩份 raw json + md + INDEX）為暫存區，內容已整合，可保留作來源存證或清除。

---

## 當前狀態（2026-06-21）

### 已完成——運動傷害層完整建立 + 接入 Vortex 網站（44 條傷害，獨立軸）（2026-06-21）

> 觸發：用戶指示「從渦流計畫出發、最後寫進 vortex 網站，盡量找出所有常見游泳運動傷害，一條線做完整（文獻＋如何避免＋發生後如何解決），盡量派工，Opus 規劃 / minimax-m3 審稿」。**關鍵定位：傷害是與水感技術軸正交的獨立軸，不掛 L0–L6 水感脊椎**（核心命題「所有技術建立在水感知上」只管技術、不管傷害）。**全光譜紀律：族群差異一律並列，文獻偏壓某族群是素材缺口不是受眾界定。**

**內容（canonical/health/injuries.yaml，44 條 + 1 meta）**
- 七大分類：A 肩部與上肢(7) / B 腰椎與泳式特異(6) / C 非肌骨醫療(9) / D 全身急性(7) / D 內分泌與骨骼(5) / E 急性外傷(5) / F 兒童生長(5)。
- v2 schema（每條）：mechanism{summary/trigger_phase/who} · epidemiology{prevalence/certainty/evidence_grade(A=RCT/SR,B=cohort,C=case,Expert=consensus)/caveat/sources} · risk_factors · prevention · management{red_flags/acute/pain_rules/rehab/RTC/prognosis} · population_notes（youth/adult/masters/sex/para 全光譜並列）· contested · references{citation/certainty/verified}。
- 整合走 `tools/build_injuries.py`：載入 drafts/*.yaml → 正規化 schema drift（scalar→list、stroke_phase→trigger_phase、補 who）→ 一致性稽核 → 輸出單一 canonical 檔。重建結果：44 條、0 異常、14 處 drift 修正、49 處 pending_verification。

**獨立審查（Phase 3）**
- minimax-m3 撞月費上限（429 Token Plan limit），改派獨立 Sonnet subagent（fresh context = 真獨立、非 Opus 自審）。
- 結論：**無 P0、無安全風險、無全光譜違規**；4 處 certainty 矛盾（references 標 🟢 高信度但 verified:false）→ 全降 🔴；exercise-amenorrhea 82% 數字加樣本警語。已修並重建。

**網站接入（my-site，commit e8736fa，CI 建置中）**
- `sync_vortex.py` 加 `sync_injuries`（剝 audit + flags.pending_verification，meta_references 不公開）→ `data/vortex/injuries.yaml`（44 條、0 洩漏）。
- `layouts/vortex/vortex-injuries.html` + `vortex-injuries.css`：左欄按七分類折疊、緊急傷害置頂橫幅、「你怎麼了」四處境入口（受傷當下/慢慢開始痛/非外傷不舒服/長期系統）、每條 panel 渲染機制/流病/grade 徽章/危險因子/預防/處置(red_flags 優先)/族群並列/爭議/連結/引用。sidebar 加「運動傷害」導航。

⚠️ 剩 49 處 pending_verification（含 6 個降 🔴 的引用：IOC RED-S / ACSM / ILCOR-AHA / SIPE pathophys / Sein 2010 / McKenzie 2023 DOI）待 W3 派工查證（見下一步建議）。

---

## 當前狀態（2026-06-20）

### 文件校正——FUTURE_RESEARCH.md 過期狀態判斷修正（2026-06-20）

> 觸發：在 my-site Vortex「內容還缺什麼」的缺口盤點中，誤把 `FUTURE_RESEARCH.md`（2026-04-18）的舊狀態句當現況，得出「L4–L6 感知描述薄弱／四式不對稱」的錯誤結論。實際核對 `Technica/water-sense-levels.yaml` 後發現四式 L3→L6 早已補完（訓練重點 + 里程碑 + 三型 quick-card）。
> 已修 `FUTURE_RESEARCH.md` 三處過期判斷並加 2026-06-20 狀態註：①§3.1「L4 以上描述薄弱」→ 已補完，缺口收斂為與 L0–L6 正交的「感知深度」軸；②§4.2 三條 bullet 逐條標修正（L4–L6 已補完／渦流感知非「完全缺席」已有 Tornado Drill·蛙式蹬腿渦流整合·Tanaka 指標但未系統化／時序感知已擴展到蝶式 C 型與自由式里程碑）；③§五優先表理由句對齊。其餘 md 無同類過期句（grep 確認）。
> ⚠️ 教訓：規劃文件的狀態句有時效，引用前要對現行內容檔（yaml）核對，不可拿兩個月前的判斷當現況。

---

## 當前狀態（2026-06-19）

### 內容校正——A-1 自由式髖部驅動因果方向（2026-06-19）

> 觸發：my-site Vortex 內容邏輯稽核（minimax 初版 + Claude 抽查）發現 `technical-analysis.yaml` 同檔自打嘴巴。`free.tech.4` 原寫「髖旋轉先行帶動肩膀（髖帶肩）」，與同檔 `free.tech.15` ／ Pink et al.(1991) EMG「肩胛肌群是旋轉的主動發動者、髖部被動跟隨」離群衝突。
> 已改寫 `free.tech.4` mechanism：移除因果敘述，改述大幅髖旋轉(45–60°)為外顯特徵、肌肉啟動仍由肩胛肌群主導（對齊 free.tech.15）。已 resync 到 my-site。稽核全表見 my-site `research/vortex-content-logic-audit.md` §0。

---

## 當前狀態（2026-06-16）

### 已完成——Phase 2：心理層完整接入 Vortex 網站（八主題「心理地圖」全部上線，62 概念）（2026-06-16）

> 觸發：研究層完整化（B1–B4）達成後，用戶指示「繼續」，進入 Phase 2 網站接入。**用戶關鍵糾正 1：直達網址＝孤兒頁，不算接入 Vortex；必須有導覽入口。** **用戶關鍵糾正 2（「為什麼一直停下來，不直接做完」）：不要交付 pilot+stub 就停，一次把全部主題寫完。** Phase F 凍結的是「首頁重設計」，加入口卡＋本頁不在凍結範圍。
> 設計回應用戶「心理層有沒有分級」：分級＝水感 L0→L6／初學→競技這條脊椎本身。著陸頁＝「心理地圖」，8 主題沿脊椎排三帶（初學端 L0–L2／貫穿全程 L0–L6／進階競技端 L3–L6）。

**心理地圖（八主題三帶，全 complete）**：
- canonical `psychology.yaml`：8 主題、**62 概念**，每概念 public/diagnostic 兩層。fear theme（7，手寫 pilot）+ 其餘 7 主題由 7 個並行 Sonnet agent 各讀對應 dossier 寫出，每條過三關校正：
  - 初學端：①水中恐懼(7) ②心理-感知-生理交互(8)
  - 貫穿全程：③動機與動機氣候(9) ④意象與心理演練(6)
  - 進階競技端：⑤注意力焦點(6) ⑥自我對話與心理技能(8) ⑦喚醒焦慮與壓力崩潰(8) ⑧心流與去再投資(10)
  - theme 加定位欄位 band/l_band/level_tag/concept_count；merge 用 ruamel round-trip（保留 fear 手寫格式與檔頭註解）。
- **三關校正沒過清單（各 agent 自報，剔除不收）**：interaction 剔 Noakes CGT 獨立概念（反推：競技配速≠初學）、Pain/Effort 分離（🔴空白+🟠二手數字）；motivation 剔量表 α/factor%、need-thwarting 重複、Sarrazin 手球外推；imagery 剔意象量表信度、多巴胺 BCAA 機制（反推荒謬）、最佳劑量（證據初步）；self_talk 剔 beat-average 70%（🟠灰文獻）、感知導向自我對話（🔴空白）、PST 多模態打包（品質 critically low）；attention/arousal/flow 無剔除（全過）。
- `sync_vortex.py` pass-through theme 層 band 欄位；`vortex-psychology.html` 概覽＝三帶地圖（complete→is-ready 卡可點入、planned→is-planned＋建置中；現全 complete）；`vortex.css` 加 `.vx-band*`/`.vx-theme-*`；首頁入口卡（vortex-home.html）。
- 已驗：hugo build exit 0，8 ready 卡 0 planned、**62 concept panel**、9 rail group；sync 後 my-site data **0 diagnostic 洩漏**（reading_signals/abc_link/probe 全剝除）；清掉 2 處 §dossier 段號洩漏（§1.6/§6）；headless Edge 截圖視覺確認三帶全亮。


- **新 canonical domain `canonical/psychology/psychology.yaml`（commit 36d51f5，Vortex repo）**：theme→concept schema（跨泳式、跨族群，對應 perception `free.yaml` L16 預授權的 psychology domain）。pilot 主題「水中恐懼」7 概念，每概念 public/diagnostic 兩層。
  - 7 概念：失控不是怕水（control_loss）、恐懼關掉水感（perception_masking）、凍結是反射（freeze_reflex）、CO₂ 換氣過度恐慌（co2_breath_panic）、潛水反射冷靜（diving_reflex_calm）、安全前置（safety_precondition）、族群恐懼臉孔（population_faces）。
  - **public/diagnostic 分層**：public = 現象機制／生理硬體邊界／L0–L6 映射／誤區校正／可做介入／族群差異；diagnostic（泳者說 X→判斷、A/B/C 診斷、感知探針）**不公開**，sync 時剝離。
- **my-site 接入（commit 3df8b56，CI success，hugo-source）**：
  - `tools/sync_vortex.py` 加 `sync_psychology()`：iterate themes→concepts，只輸出 public 欄位（drop diagnostic），寫 `data/vortex/psychology.yaml`。已驗 0 diagnostic 洩漏。
  - `layouts/vortex/vortex-psychology.html` master-detail 頁（重用 vortex.css/vortex.js，左 rail 按 theme→concept、右 panel 渲染現象/邊界/誤區/介入/族群/來源/flow nav）。
  - `content/vortex/psychology/_index.md`（layout: vortex-psychology）。
  - **首頁入口卡**（`vortex-home.html`「更底層·感知的地基」section，現有 `.vx-toc-row` 樣式，主題數動態讀 data）——孤兒頁→真正接入導覽。
- **三關校正沒過清單（剔除 4 條，不收）**：US poll 百分比🟠（二手委託民調）、FWAQ 98.2%/α=0.831（反問不過：量表內部信度非教學可用結論）、Wolpe 90%🟡（舊文獻過度精確）、US 4.3%/40%🔴（待查）。三處 🔵 反推防護：perception_masking 標🔵附研究空白註、diving_reflex 附安全前置、呼吸介入限低強度（淺水昏迷風險）。

### 已完成——心理層 8 dossier 系統性引用查證 B1–B4：4 處誤歸因/誇大結果攔截 + 全數文獻 🔴 收斂（2026-06-16）

> 觸發：用戶指示「先做完整研究、把心理部分整理好，再看怎麼接入 vortex 網站」。先做研究層完整化（網站接入留待 Phase 2）。分 4 批逐檔查證每一條 🔴 待查引用，每個人名/DOI/PMID 都實際追到 Crossref / NCBI eutils 一手核對，不靠搜尋摘要。**過程攔到 4 處高風險幻覺/誤記，全部更正。**

- **B1（02+04，commit 9df3267）**：02 收斂 5 條（Scott & Gijsbers 1981 PMID 6789949、Hardy/Parfitt/Pates、Hanin 年鑑章節、Masters/Eves/Maxwell 2005 會議論文、O'Leary & Morris 2017 修作者序）；04 把 Teixeira et al. 2020 從 🔴 ResearchGate 升 🟢（PMID 31578934 / DOI 10.1080/17461391.2019.1675768），關閉 🔴02。
- **B2（03+05，commit fdde682）**：03 §2 盛行率溯源——WMH 22 國 2.3% 升 🟢（Wardenaar 2017, PMID 28222820 / 勘誤 28994357），美國 46/64/32–39% 追到 1998 Gallup × Miracle Swimming 委託民調維持 🟠；05 Hall et al. 1998 補 IJSP 29(1):73–89、Simonsmeier 2021 補 DOI 升 🟢，兩個「🔴PMID 待查」關閉。**關鍵辨識：IJSP / IRSEP 等刊物未被 PubMed 收錄，「無 PMID」是制度性而非「待查」——此前誤標待查。**
- **B3（06+07+08，commit cb7f038）— 攔到 3 處誤歸因**：
  - **06 ①** 「more/less successful 隊伍賽前準備」更正歸 **Gould, Guinan, Greenleaf, Medbery & Peterson 1999**（TSP 13(4):371–394, DOI:10.1123/tsp.13.4.371），v1 誤植為 Gould & Dieffenbach 2002（該 2002 篇實為奧運冠軍心理特質，不同主題）。
  - **06 ②** 游泳 PPR 研究作者更正 **Moraes → Richard, Mason, Alvarez-Alvarado, Perry, Lussier & Tenenbaum 2021**（TSP 35(2):97–107, DOI:10.1123/tsp.2020-0023）。**且 v1 誇大結果**——原寫「對表現/動作效能/自我效能/情緒均有正向效果」，實際速度/動作效能/自我效能皆「不顯著」，僅情緒顯著；正確結論是「PPR 對客觀指標效果有限、主要作用在情緒與主觀層面」。Zach 2024 補 DOI:10.32725/sk.2024.004。
  - **07 ③** Masters & Maxwell 2008 更正為 IRSEP 期刊論文「The theory of reinvestment」1(2):160–183, DOI:10.1080/17509840802287218，v1 誤植為「Hirsch 編書章」。Jackson 1995 補 DOI:10.1080/10413209508406962，並更正「PMID 8735997」誤植（該 PMID 屬 Jackson 1996 *RQES* 篇，非 1995 JASP 篇）。
  - **08**：補完 P07–P10 文獻層 🔴——Tucker 2004 40°C（PMID 15138825）、Tucker 2009（PMID 19224911）、Easterbrook 1959（**更正「1959 年無 PMID」誤記，實為 OLDMEDLINE PMID 13658305**）、Miu et al. 2009 HRV（PMID 19059813，補足三位作者）。
- **B4 收尾（本次）**：00 總覽的 Liao & Masters 桌球更正先前已傳播（§54/135/167），G2 已含「感知導向自我對話」第三類——無需再改。各 dossier footer 計數自核對齊（05 🔴6 = 5 編號空白 + 1 量表空白；08 文獻 🔴 歸零，剩 🔴-01~09 九項研究空白 + §4.3 未讀檔一處）。
- **總結**：心理層 8 dossier 的「待查引用」🔴 已全數收斂——剩餘 🔴 皆為**真研究空白**（已逐條標界「目前文獻無此數據」），可作未來實驗設計起點，非未完成查證債。**研究層完整化達成；下一步才是 Phase 2 網站接入評估。**

### 已完成——`隱性_顯性學習.md` 升 v2 + 攔截並更正一處跨檔誤歸因（2026-06-16）

> 承上方批次路線圖剩餘跨檔工程第①項。修 escape-bug + 用 dossier 02/07 素材擴成 v2。**升級過程中強制查證攔到一處重大誤歸因，連帶更正心理層多檔（含本人批次 B 的傳播）。**

- **`Research/感知科學/隱性_顯性學習.md` v1→v2**：原檔整檔一行字面 `\n`（escape-bug）渲染全壞。重寫為 7 節 clean v2：§1 隱性 vs 顯性對照、§2 再投資理論機制核心（Masters 1992 DOI 10.1111/j.2044-8295.1992.tb02446.x；動作 vs 決策再投資 Masters & Maxwell 2008 DOI 10.1080/17509840802287218；Beilock & Carr 2001 PMID 11757876）、§3 類比學習（**正確歸給桌球**）、§4 de-reinvestment=L5→L6、§5 L0–L6 教學映射、§6 研究空白、§7 dossier 連結。
- **⚠️ 攔截的誤歸因（高風險幻覺，自查時抓到）**：Liao & Masters 2001 的著名「analogy learning」研究**是桌球**（正手上旋、「直角三角形」拍路），**不是游泳**。心理層先前把它描述為「游泳第一手實證」，並附**無法核實、疑捏造**的 DOI（10.1080/026404101300149327）、頁碼（369–375）、標題（「…in swimming」）。正確版：DOI 10.1080/02640410152006081，pp 307–319，標題「Analogy learning: A means to implicit motor learning」。游泳應用是**外推**（🔵），非第一手實證。
- **連帶更正的檔**：`00_心理層總覽.md`（3 處，含**本人批次 B 寫的主軸 B 引用**——屬自我傳播的更正）、`07_心流與最佳表現.md`（內文 §250 + 研究空白 §287 + 資料來源 §306）、`_INDEX.md`（§126）、`RESEARCH_PLAN.md`（§123 Masters DOI tb02440→tb02446 修正 + §124 把無法核實的 Liao PMID 11354610 換成已核 DOI）。所有殘留的舊 DOI/頁碼字串都已被包進「⚠️ 更正」說明內，不再作為事實宣稱。
- **游泳專屬類比學習對照研究確認為研究空白**（v2 §6 + 07 §287 已標 🔴），不強行補。

---

### 已完成——新增 Research/心理/ 層：感知優先重讀運動心理學（2026-06-15）

> 目標：補上專案一直缺的「心理」環節。用戶指示「opus 負責規劃給其他做，再做最後整理，資料蒐集多一些」。Opus 規劃 8 個子主題 → 子代理（Claude + 預定 minimax）並行蒐集 dossier → Opus 整合。

**流程與產出：**
- Opus 把心理層拆成 8 個子主題，派 8 個子代理並行蒐集文獻 dossier（每份附 PMID/DOI + 確定性標記 + 游泳第一手 vs 跨運動外推分層 + 與水感框架的連結 + 🔴 研究空白）。
- 子代理在「生成回報訊息」時撞 Claude 限額（回報 token=0），但 **8 份 Write 都已落盤**；查證磁碟確認完整（每份 8–31 個 🔴/研究空白標記），無需重跑。
- Opus 收尾：① 查證並修正 dossier 02 兩個可疑引用（倒 U 曲線 TiCS 2024 DOI 格式錯誤→改用真實標題+PII S1364-6613(24)00078-0；ACTH 研究作者名「Frontaini」是捏造→移除，改用真實標題+PMID 34868421 並補正數據）② 8 份 dossier 從 `_raw/` 升到 `Research/心理/` 正式位置 ③ 寫 `00_心理層總覽.md`（Opus 整合骨架，非第九份 dossier）。

**`00_心理層總覽.md` 的整合價值（單一 dossier 看不到的）：**
- 五條貫穿全部 8 cluster 的主軸：A 感覺水=注意力焦點第三類（2024 Bayesian meta PMID 39480294 推翻 EF 全面優越）/ B Flow↔Reinvestment 軸線與 de-reinvestment（=L5→L6 機制）/ C EMG 悖論心理橋（焦慮過度控制證據最強，但意象 forward model 保留解釋 #2）/ D 動機氣候=感知探索土壤（感知目標語言=精熟氣候工具）/ E 恐懼=「失去動作控制」簽名（接 L0 閘門）
- 心理層 × L0–L6 對照表 + × A/B/C（C 型=全身張力，由 EMG 悖論機制鏈解釋）
- 5 項框架原創貢獻（感知耦合焦點/感知導向自我對話/「水在幫我」可操作指標/感知目標語言=動機工具/de-reinvestment 機制）—— 皆 🔴 文獻空白等級但具生成性
- 6 條跨 cluster 🔴 研究空白

**連帶更新：** `_INDEX.md`（新增 Research/心理/ 區）、`FUTURE_RESEARCH.md` §0.5 EMG 悖論（從「純推測」升級為「兩條有文獻支撐的競爭假說」，引心理層證據）。

**重要連結：** `Research/感知科學/隱性_顯性學習.md` 已存在（v1 stub，2026-04-25，僅 3KB）；dossier 02 + 07 提供大幅擴充素材（再投資動作 vs 決策分離、Liao & Masters 2001 完整方法、Beilock 明確監控假說），可把該 stub 升級為 v2。
> ⚠️ 順帶發現：該 stub 檔內容是**字面 `\n` 而非真正換行**（escape-bug，整檔一行），渲染全壞——需單獨修一次（非本次心理層任務範圍，先記錄）。

---

### 已完成——心理層查證債清理 + 教學對象框架釘入（2026-06-15，第二 session）

> 觸發：用戶檢視心理層問「還有沒有要補的」。先做缺口評估（4 個 haiku 平行讀完 8 dossier），再從最安全的查證債批次動手。

- **教學對象框架釘入 `CLAUDE.md`**：用戶澄清「客群涵蓋全光譜、無單一主客群」（兒童 / 兒童競技 / 青少年競技 / 鐵人三項 / 成人初學；未來加自由潛水成人+兒童）。寫入 CLAUDE.md 專案本質區，明令 AI / 子代理**不得自行推斷主客群**、文獻偏壓某族群只是素材缺口。**起因：缺口評估時一個 haiku 子代理把「成人休閒學習者=主客群」當事實塞進回報，被原樣轉述，用戶糾正——故釘入文件防複發。**
- **08 查證債全清（六條 🔴-P → 全數查證）**：逐條追 PubMed / 期刊原始頁。P01 Tucker, Lambert, Noakes 2006 → PMID 19116437；P02 Noakes 等 2005 → PMID 15665213；P03 → **更正**為 Noakes, Peltonen, Rusko 2001（DOI 10.1242/jeb.204.18.3225，原誤標第一作者 St Clair Gibson）；P04 Paulus & Stein 2010 → PMID 20490545（原誤記來源為 ScienceDirect Topics）；P05 Chambers 等 2009 → PMID 19237430；P06 PMC4152223 = Pappens 等 2014 → PMID 25181542。§七標題改「全數查證完成」。
- **修三處誤歸因**：① §六 🔴-07 漱糖水機制原歸 Tucker 2006 → 改 Chambers 2009 ② P03 第一作者 ③ P04 來源。
- **06 Bauman 兩條 🔴**：Gould, Dieffenbach & Moffett 2002 DOI 查得（10.1080/10413200290103482，運動心理期刊無 PMID），但其主題（奧運冠軍心理特質）與 dossier 描述（區分 more/less successful 隊伍）**不符** → 標為「篇目待原書核對」，不強行對齊以免製造新誤歸因；>X̄ Sydney 2000 訪談確認為**灰色文獻**（Bauman 書中自述，無發表原始資料）。

**心理層缺口路線圖（本 session 評估；批次 A 查證債已完成，B/C/D 待續）：**
- **B 整合缺口**（低風險，🔵 推導 + 可查文獻）：恐懼×動機氣候交互（00 總覽五主軸與 G1–G6 皆漏的整合缺口）、呼吸中斷的認知負荷（swimming-specific，補進 08，解釋水中 RPE 膨脹）、發展軌跡型 flow（07 只談「已達成」flow，缺 L2→L3 / L4→L5 過渡期）
- **C 族群覆蓋**（中風險；因「客群=全部」而從誤判升級為真缺口）：03/04 文獻偏壓兒童泳課+競技隊，缺成人初學 / 鐵人三項 / 青少年競技各自的恐懼·動機特異性，須分族群並列、查無則標 🔴
- **D 補厚單薄段**：07 IPS（僅 3 行就跳「已被取代」）、04 HMIEM（純理論占位無游泳實例）、08 中樞調節（自承二手）、02 Reinvestment 專節壓縮（與前文核心理論重疊約 40%）
- 另：`隱性_顯性學習.md` escape-bug（整檔字面 `\n`）+ 用 dossier 02/07 素材升 v2（見上方心理層主塊）

---

### 已完成——心理層批次 B：三條整合缺口補齊（2026-06-15，第二 session 續）

> 承上方缺口路線圖批次 B。全部建立在已驗證引用之上（🔵 推導明確標界，新數據缺口標 🔴），無憑空斷言。

- **B1 恐懼×動機氣候交互**（跨 cluster 03+04，總覽五主軸與 G1–G6 皆漏的二階整合）：
  - `00_總覽` §1 新增「主軸交互 D × E — 動機氣候調節恐懼的閘門效應」：表現氣候把私下「失去控制」恐懼放大成公開能力判決 → 抬高 L0 閘門；調節變項=知覺勝任感（低勝任+ego 最毒）；低勝任=所有初學族群共同起點，故同一交互在初學族群卡 L0、在競技族群壓縮 L4–L6 再探索（分族群並列，不一概而論）。支持文獻 🟢：Masters 泳者 Frontiers 2025（DOI 10.3389/fpsyg.2025.1574429）、統合分析 DOI 10.3390/ejihpe14040064。
  - `03` 新增「恐懼×動機氣候」小節（接 cluster 04，減敏/暴露須先卸評價威脅才生效）；`04` 新增命題六（互引 00 §1）+ **修正 §命題五原「成人=本框架主要使用對象」**改為「知覺勝任感調節、初學族群最脆弱」（消除與新教學對象框架的矛盾）。
  - 總覽 §5 加 🔴G7（氣候×恐懼交互的泳池實驗數據空白）。
- **B2 換氣的週期性認知負荷**（補進 08）：新增 §1.9「換氣作為週期性認知負荷注入」——換氣是必須與划臂對時的運動任務，未自動化者每次換氣抽走流場感知頻寬→水感節律性閃斷→換氣側水感系統性較差。定位為 C 型的**第二條獨立路徑**（與 §1.2 焦慮肌張力並列，介入方向不同：降喚醒 vs 換氣自動化）。🔵 推導，建立在已引用的雙重任務+Easterbrook 注意力窄化上；量值缺口標 🔴-09。總覽 §3 C 型條目同步改為「兩條獨立機制」。
- **B3 發展軌跡型 flow**（補進 07）：新增「心流的發展軌跡：flow 不是 L6 的專利」——挑戰-技能匹配是相對技能水平的，flow 在每個 L 級皆可發生、內容隨層遷移（L0–L2 控制感初獲 / L3–L4 局部融合 / L5–L6 場共振）。意義：早期 flow=動機燃料（連 04）、教學落點=主動工程化各層挑戰-技能匹配、兒童易進成人初學需更刻意去評價（連 03/04 交互）。🔵 建立在 Csikszentmihalyi 挑戰-技能模型；跨層 FSS-2 實測缺口已在 §6。

**批次 B 全程無新增未驗證 PMID；所有人名/DOI 均沿用已查證來源或標 🔵/🔴。** commit 90f2cbf。

---

### 已完成——心理層批次 C：族群覆蓋分列（2026-06-15，第二 session 續）

> 因「客群=全光譜、無單一主客群」，族群特異性從誤判升級為真缺口。03/04 文獻偏壓兒童泳課+競技隊，補上其餘族群並列。3 條 WebSearch 取得可用來源；查無者標 🔴（素材缺口非受眾界定）。

- **03 新增「族群特異性：恐懼的不同臉孔」**（分族群表）：兒童初學（代際傳遞，🟠 文獻默認）/ 成人初學（疊加社會性羞恥+自我意識+恐慌史，🟢 Educ Sci 2025 DOI 10.3390/educsci15060760）/ 鐵人三項（非怕水本身，怕開放水域情境=有能力泳者賽境 L0 退行，🟠 二手 ~22% Ironman 2004 Grand'Maison，原研究未核）/ 青少年競技（轉表現焦慮，跨指 cluster 02）。教學意涵：四群指向不同介入點，把鐵人/青少年用兒童 L0 水性課介入=族群混淆。加 🔴11/12。
- **04 新增「族群特異性：動機的不同引擎」**（分族群表）：兒童樂趣優先 / 青少年競技流失懸崖（參與 ~11 歲達峰→17 歲谷底女~64%男~45%下降，系統回顧 PMID 29910410 + 連既有 Difernand 2025 存活分析）/ 成人初學目標導向+勝任感脆弱 / 鐵人三項游泳=手段（🔴 動機結構幾無第一手）。加 🔴07/08，footer 條目數更新。
- **族群百分比數字標界**：Ironman 22%、流失 64%/45% 均標 🟠「原始未核」，不當硬數據用。

---

### 已完成——心理層批次 D：逐項覆核，只補真缺口（2026-06-15，第二 session 續）

> 對前 session haiku 評估的 4 個「單薄段」逐一覆核實際內容後判斷——**只有 1 項是真缺口，其餘 3 項評估過時或屬低值重構，不硬補**（避免製造填充內容）。

- **04 HMIEM 游泳實例（真缺口，已補）**：原 §7 純理論占位無游泳實例。新增三層模型（Global/Contextual/Situational）× 游泳情境 × L0–L6 對照表 + **bottom-up 動機修復槓桿**（單次成功 L0 感知體驗反覆累積 → 由下而上修復情境層動機、鬆動「我不是水裡的料」整體層自我認定，連 cluster 07 早期 flow，對成人初學尤關鍵）。🔵 推導，建立在 Vallerand 1997 既有框架，無新增未驗證引用。
- **07 IPS（覆核：非真缺口）**：§7 實含 Loehr + Hanin IZOF + Hardy/Jones/Gould 三源並誠實註明 IPS 已被取代，覆蓋足夠，不硬補。
- **08 中樞調節（覆核：評估過時）**：批次 A 已升級為 Noakes 一手（PMID 9140893 / 15665213 / 10.1242/jeb.204.18.3225 + Tucker 2009），非二手。僅殘 1 個 🔴（Tucker 40°C 閾值原始 PMID），低優先。
- **02 Reinvestment（覆核：不壓縮）**：§5 與「Reinvestment 專節 A–G」確有重疊，但分屬「核心理論條目」vs「深掘附錄」兩種角色；用戶意圖是補缺口非修剪冗長，且壓縮有損 nuance 風險，保留原狀。

**心理層 A/B/C/D 四批次全部收束。剩餘為跨檔大工程（非心理層收尾範圍）：① `隱性_顯性學習.md` escape-bug 修復 + 用 dossier 02/07 素材升 v2；② 各 dossier 殘餘 🔴 的逐條查證（多為研究空白等級，已標界）。**

---

### 已完成——週期化知識研究擴充 + 白話重寫 + 一源兩消費全鏈打通（2026-06-10）

> 目標：外部文獻研究擴充週期化 canonical，加 plain_zh 白話層（學員/家長/教練），並打通 canonical → my-site 呈現 + swim-coach FTS 兩個消費端。承接上方 Phase 1（canonical 建檔）。

- [x] **R1 外部文獻研究**（4 並行 Sonnet sub-agent，嚴守反幻覺）：可用 primary 來源——減量 Mujika 系列（PMID 12840640 / 8775162 / 12439774）+ Bosquet 2007（PMID 17762369）；能量系統 Toussaint & Hollander 1994 / Rodríguez & Mader 2011（跨研究區間不合併，如 400m 有氧 40–84%）；分區 Maglischo 2012《Training Zones Revisited》(J Swimming Research 19:2)；TID Papadimitriou 2025（DOI 10.1007/s00421-025-06064-x）；年度 Hellard 2019（PMC6470949）/ González-Ravé 2022（PMID 36247944, n=1）；LTAD Swimming Canada（windows of trainability **contested**——Ford 2011 PMID 21259156 + van Hooren 2020 批判）。
- [x] **canonical 三檔擴充 + plain_zh**：structure（+swim_annual_structure +swim_youth_ltad）、taper（修掉幻覺「1.62%」→ +2.18% PMID 12439774、補 +2.90/+3.20% PMID 8775162）、zones（+Maglischo 六分區 +三區乳酸 +各距離供能 +TID）。每節點加 plain_zh（白話），source/數字/cert 並排保留。
- [x] **_index.yaml 概念目錄**：28 節點（gist_zh 一句白話 + stages），index↔real id 零死連結。commit 7d03619（已 push remote）。
- [x] **my-site 呈現**：`sync_vortex.py` PERIODIZATION_FILES 加 `_index`；verbatim 搬 4 檔到 `data/periodization/`；`vortex-periodization.html` §1–§6 渲染 plain_zh + §5 加 4 游泳區塊 + 新增 §7 游泳年度結構 §8 青少年 LTAD（contested 警示）。hugo build 綠。my-site commit 31cea81（待 push 觸發 CI）。
- [x] **swim-coach FTS 被動繼承**：vendor/vortex submodule bump ce3a183→7d03619；`build_knowledge_index.py` 加 `_`-prefix skip（_index.yaml 非 FTS 內容）；FTS index 31 列（structure12/taper10/zones9），0 null source_id / 0 _index 列 / 0 重複；新增 swimming 區塊全 FTS 命中；加 2 behavioral test；pytest 73/73。swim-coach commit 6375496（未 push，Phase 3 政策）。

### 已完成——canonical/periodization/ 新 domain：Bompa 週期化收編為唯一真相源（Phase 1）

> 目標：把 Bompa《Periodization》(6th ed.) 週期化知識收進 canonical，成為唯一真相源，供兩個下游消費——my-site vortex 給 ADM 年度計畫補「週期化理論骨幹」、swim-coach 自動學課表能力的知識基礎。架構複製剛完成的 ADM 模式（一源兩消費）。**Phase 1（建 canonical）為本次範圍；Phase 2 vortex 呈現 / Phase 3 swim-coach 唯讀引用 / Phase 4 swim-coach rules schema 提案，後續進行。**

- [x] **Phase 0 來源核對**：5 章正文全讀自正確 body 檔（`XX_Summary_of_Major_Concepts.md`，非僅含參考文獻的 `Chapter_X.md`）。檔對照：11_=Ch5 / 13_=Ch7 / 14_=Ch8 / 15_=Ch9 / 18_=Ch11。每個數字溯源至章節/表格 + 標確定性。修正 Haiku 草稿兩處：taper 改為 41–60%（重負荷 60–90%）/ 8–14 天；macrocycle 3:1 確認正確（Bompa "probably the most common"）。
- [x] **structure.yaml**：年度計畫結構。3 階段（準備/競賽/過渡 + subphases）；4 計畫類型（mono/bi/tri/multipeak，Table 5.1 週數分配，dotted ID `periodization.structure.annual.*`）；macrocycle（2–6 週，3:1 預設負荷型態）；microcycle（4 分類）；detraining 安全表（🟢 Table 8.2 / Mujika & Padilla 2000，swim-coach 休賽/傷停課表關鍵安全參數）。
- [x] **taper.yaml**：賽前減量與達峰（Ch9 / Mujika & Padilla 2003 🟢 / Bosquet 2007）。四變數（量 41–60%主旋鈕 / 強度維持 / 頻率≥80% / 時長 8–14 天）；曲線型態（快速指數 ≈4–5% 為首選 vs 階梯 ≈1.2–1.5%）；達峰窗 7–14 天；游泳應用（文獻 50–90% 量遞減、三週減量 +2.2%、雪梨2000 名次差 1.62%）。
- [x] **zones.yaml**：能量系統強度分區。Table 7.1 六分區（賽配速=zone 2）；Table 11.2 HR/VO2/能量系統對照；Table 11.1 LIEE 六法；耐力週期化三階段；游泳配速分區（🔵 只映射 Bompa 框架不發明百分比）。
- [x] **三項驗證（Python，跑完即棄）**：① 三檔 YAML parse OK；② 跨 domain link 完整——所有 `links.development_stages` 引用（l2t/t2t/t2c/t2w）皆命中 development/matrix.yaml stages[].key，BAD=NONE；③ 22 個 ID 全唯一、全 `periodization.` 前綴，DUPLICATES=NONE。
- **整合點**：ADM matrix T2W 格已寫「48 週年度計畫；一年兩巔峰（春季選拔 + 夏季國際賽）」= bi-cycle，本 domain 提供其週期化理論背景，links 雙向可串。
- **下游待接**：Phase 2 my-site `sync_vortex.py` 加 periodization sync + vortex 呈現層；Phase 3 swim-coach `build_knowledge_index` 收進 L1 FTS；Phase 4 交付 `rules/periodization.yaml` schema 提案（Hang 自填教練參數，A-zone 不外包）。

### 已完成——canonical/development/ 新 domain：ADM 知識收編為唯一真相源

> 目標：把 ADM（Swimming Canada 運動員發展矩陣 / LTD）知識收進 TheVortexProject canonical，成為唯一真相源（一源兩消費：my-site 與 swim-coach 各自消費）。my-site `data/adm/` 為下游 sync 產物。**模組化為本次重點；橋接/呈現（Phase 4）不在此次範圍。**
> **更正（2026-06-10）**：原寫 swim-coach `rules/ltad_stages.yaml`「退役成下游 sync 副本」是錯誤 framing。用戶裁定：swim-coach（教練系統）與網站是兩個不同東西，沒有誰退役；兩邊各自消費同一份 canonical。swim-coach 自動繼承 canonical stages 為另案，rules 判斷值仍人工填。

- [x] **matrix.yaml**：`canonical/development/matrix.yaml`；4 支柱（physical/technical/mental/life）× 5 階段軸（fun/l2t/t2t/t2c/t2w；fun `has_cells:false`）+ 16 cells（`dev.{pillar}.{stage}`）。public.{summary,points} 逐字搬 my-site `data/adm/matrix.yaml`（週期化處方屬正當 prescriptive，全留 public）+ diagnostic null（ADM 無 A/B/C 感知判讀語）。technical 三格 links 串 22 std + 真實 drills/tech/l_indicators。修死連結 Fr28→Fr16。
- [x] **technical-standards.yaml**：`canonical/development/technical-standards.yaml`；附錄 A 技術基準 22 筆（`std.{stroke}.{aspect}`）= 4 式划水（free/back/fly/breast）+ 起跳×2（dive/back）+ 轉身×6（free/back/breast/fly/im-breast/im-free）。public{title/framework/applies_from:t2t/phases.criteria} + diagnostic null。左右鏡像小節（free/back pull+push）合併為單筆（側中性 criteria + note）。links 串「形式↔感知」l_indicators，全用已驗證 ID。
- [x] **驗證（throwaway script，跑完已刪）**：parse OK；cells=16 / stages=5（fun has_cells:false）/ standards=22；zero-drift（16 格 public.{summary,points} vs my-site 源檔逐格逐條零差異）；死連結=0（canonical ID universe 378，link refs 95，差集空）；appendix-a coverage 完整（22 未逐字命中者全為左右鏡像 bullet，已被 4 筆合併記錄語意涵蓋）。
- **下游待接**：my-site `sync_vortex.py` 尚未加 `sync_adm_matrix` / `sync_adm_standards`（Step 6）。~~swim-coach `rules/ltad_stages.yaml` 退役~~（取消——framing 錯誤，見 2026-06-10 更正；swim-coach 自動繼承 canonical 為另案）。

### 已完成——canonical/ 結構化資料層：散文→YAML 模組化（my-site 探索器來源）

> 目標：把 Vortex 主題層散文模組化成 my-site 可掃描 / 可篩選 / 可展開的探索器。canonical-first：結構先進 canonical/（public/diagnostic 兩層），再經 sync_vortex.py 只帶 public 傳到 my-site，diagnostic 留給 swim-coach。

- [x] **教學誤區**（commit 82f6fe0 + 9e68ffb）：6 式 76 條 → `canonical/instructional/teaching-errors.yaml`；public{misconception/physical_reason/evidence/correct_concept/perception_impact} + diagnostic{type}。my-site `vortex-errors.html` 探索器。
- [x] **技術分析**（commit 6ad36ea）：6 式 188 技術點 → `canonical/instructional/technical-analysis.yaml`；全 public（物理層）。my-site `vortex-tech.html` 探索器。
- [x] **L 指標矩陣**（commit 34090b6）：`Technica/技術指標_L級對應框架.md` → `canonical/technica/l-indicators.yaml`；43 indicators（6 levels × 5 strokes，30 格全填）；public{indicator/framework_state/quant_ref/evidence} + diagnostic{failure_signal（6 common 格）/ type（3 格 A/B/C：free.L3.evf=A / back.L4.roll-stability=C / fly.L4.outsweep=A）}。my-site `vortex-matrix.html`（ADM matrix 範式：rows=levels × cols=strokes，aspect chip → 共用 detail panel，泳式 focus 篩選 + deep-link / hash-jump）。
- 下游：my-site commit 3cf6069（Hangsau/cortex，CI green run 27053437843）；sync_vortex.py `sync_l_indicators()` 只帶 public，built HTML 診斷洩漏審查 = 0。swim-coach submodule 未 bump（l-indicators diagnostic 尚未被 vendor 消費，Phase G 再驗）。
- [x] **水感層級**（Phase D）：4 式 `Technica/*水感框架.md` → `canonical/technica/water-sense-levels.yaml`；26 levels（free/back L0–L6，breast/fly pre+L2–L6）。public{description/methods/indicators/quant/stagnation/milestone + 各式特有 four_problems/state_description/fatigue_collapse_four_layers/kaizen/stress_test} + diagnostic{type_diagnosis/type_states/type_training/type_milestones/stagnation_by_type} + 頂層 three_types/appendices。公開層三型/A/B/C 全數淨化：per-stroke 字面替換（如「重新做三型診斷」→「重新確認感知缺陷的主要方向」、移除「（A型）」標記）+ 把 stagnation 內的 A/B/C 型專屬尾段抽出搬到 `diagnostic.stagnation_by_type`；審查 regex（三型|A型|B型|C型|哪型|不論主型|typical_speech|main_problem|chain_breakpoint|failure_trigger）over public = 0 leaks。⚠ 訂正：本 Phase D 只完成 canonical + sync，my-site 呈現頁當時**並未實際建出**（曾誤記為「vxl- 縱向序列卡已建」，但 my-site layouts 從未有該檔，data 一直是孤兒）。my-site `vortex-levels.html` 於 **2026-06-11**（my-site commit 85546b6）才真正建出，設計是泳式 rail + 各級 `<details class="vx-level">` ladder（重用 vortex.js 面板切換，非 vxl- 卡片），並設為首頁第四塊主入口。
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
- [x] Research/感知科學/隱性_顯性學習.md（v1 stub 已存在，2026-04-25，commit 33e49d8）— ⭐ 可用 Research/心理/02 + 07 的豐富素材升級為 v2；另需修 escape-bug（整檔字面 `\n`）
- [x] Research/心理/（2026-06-15 完成）— 8 份 dossier（注意力焦點/喚醒焦慮/水中恐懼/動機/意象/自我對話/心流/感知-生理）+ 00 Opus 整合總覽；感知優先重讀運動心理學，補上專案缺的心理環節
- [x] Research/物理現象/渦流回收.md（2026-04-18 完成，Talos 輔助研究）— 6 篇文獻全查證；🟢 Hochstein 2011（UUS 再捕獲）/ Takagi 2014（划水 wake capture）/ Garayev 2021（螳螂蝦跨物種）；🔴×3 待補
- [x] Research/物理現象/推進力理論演變.md（2026-04-18 完成，從 raw/notes 整合）— 阻力/升力/現代三階段；「找靜水」邏輯謬誤；🔵×2 🟡×4 🟢×1；連結 渦流回收.md / 機械感受器.md / 誤區深探
- [x] Research/物理現象/自然頻率.md（2026-04-25 完成，Talos + Claude 協作，v1 committed，c500f7b）
- [x] Research/物理現象/彈性蓄能.md（2026-04-25 完成，Talos + Claude 協作，v4 committed）

### 長期（需累積素材）

- [ ] Observations/ 更多教學案例（需實際教學素材）
- [ ] SQ框架最小可行觀察計畫執行（見感知量化SQ框架.md）

---

## 下一步建議

### 最高優先——canonical 資料契約升級 S1–S5（2026-07-25）

分段規劃如下。**S1 先行**：其驗證器跑完會產出真實錯誤清單，那份清單才是 S2/S3 的正確定量依據；現在直接承諾整套遷移是矇眼估工。

| 段 | 內容 | 性質 | 派工 |
|---|---|---|---|
| S0 | 提交 CLAUDE.md 規範 + 本缺口條目 | 文件 | ✅ 已完成 2026-07-25 |
| S1 | `_taxonomy.yaml` + `_sources.yaml` 空殼 + `tools/validate.py` + `tests/` | 純機械，零內容風險 | ✅ 已完成 2026-07-25（commit a04df0a） |
| S2 | `category` 36 個值：先決定教學類別 vs 健康傷害類別（`A-`~`F-` 前綴）是否拆欄位，再談歸一與 alias | 需領域判斷 | ✅ 已完成 2026-07-26（不拆欄位，改 per-value `scope`；新增 E008/E009/W010；my-site 硬編標籤字典全清） |
| S3a／S3a-2／S3b | 來源註冊表建置 + 證據分層契約 + W009 歸零 | 最大宗 | ✅ 已完成 2026-07-26／27（476 筆 `src.*` 註冊；W009 270→0；新增 W011／E010／E011） |
| S3c | 476 筆已註冊來源補 DOI／PMID／ISBN + 查驗日（W003 的解） | 機械查詢 | 可派工 |
| S3a-3 | W002 剩 111 筆（多為 `injuries.yaml` `references[].citation`）→ `source_ids` | 純遷移 | 可派工 ⚠ 改 `canonical/health/drafts/` 再 build |
| S4a | 校正驗證器誤判 + 補 fail-closed | 機械 | ✅ 已完成 2026-07-25（6ae575e、634b298） |
| S4b | injuries 的 **20 筆** `*_link` 散文欄位加 `*_link_ids` 機器鍵（**不**拆成 ID 陣列，同 S4c 的「加欄位不換內容」） | 需讀內容判斷 | ✅ 已完成 2026-07-26（W004 20→0，新增 E007/W007） |
| S4c | **W001 = 61 筆** `cross_ref` → 穩定 ID（新增 `cross_ref_ids` 機器鍵；節號類列為遺留債） | 機械為主 | ✅ 已完成 2026-07-26（W001 61→0，新增 E006/W006） |
| S5 | `tools/build_indices.py`：四視圖（內容／tag 反向／來源反向／缺口報告） | 機械 | ✅ 已完成 2026-07-27（770 records／476 sources／7 tests） |
| S6 | public/private 匯出隔離（hub P4 前置）+ W011 63 筆補 `observation_basis` | 需分層判斷 | 未規劃 |

**風險與預案**：S3 是唯一有資料損毀風險的一段（動 164 筆條目內容欄位）。對策＝`source_display` 保留原文字不刪，遷移只做「加欄位」不做「換內容」，任何時候可回退。S2 的歸一會改變既有 tag 值，須先跑「哪些條目會受影響」的預覽再動。

**驗收**：`python tools/validate.py` 綠燈 + 缺口報告產出 + `build_knowledge_map.py` 仍能跑通且 `KNOWLEDGE_MAP.md` 無非預期 diff。

#### S4a 驗收與當前基線（2026-07-25，commit 634b298）

`python tools/validate.py`：**2 ERROR / 645 WARN**；`python -m unittest discover -s tests`：**28 tests OK**。

| 代碼 | S1 初測 | 現在 | 說明 |
|---|---|---|---|
| E001 缺 id | 6 | **0** | 全是驗證器誤判——`l-indicators.levels[]` 用 `key` 是 Vortex 既定慣例（詞彙定義表用 `key`、內容條目用 `id`） |
| E003 斷鏈 | 108 | **2** | ~70 筆是同一誤判（`links.development_stages: l2t` 是 `matrix.yaml stages[].key` 的合法詞彙值，不是條目 ID）。剩 2 筆是真斷鏈 |
| W001 cross_ref 自由文字 | 61 | 61 | 未動，S4c |
| W002 🟢/🟡 缺 source_ids | 88 | 88 | 未動，S3 |
| W003 孤兒條目 | 473 | 476 | ⚠ 差 3 未解釋（撞配額前沒查完） |
| W004 `*_link` 散文無 ID | — | **20** | 新增檢查揭出的真債（見下） |
| W005 未知 links 子鍵 | — | 0 | 新增，堵住 fail-open |

**S4a 過程中攔截的一次品質事故**：第一版 S4a 把 `mechanism_link` / `technical_link` / `perception_link` 歸為「自由文字類，跳過驗證」，等於讓真實的連結債從報告中消失；且未知 `links` 子鍵走 `else` 靜默放行（fail-open）。已要求補 W004/W005 修正。**教訓：驗證器的「誤判修正」與「把問題改成低風險類型」只有一線之隔，每次縮小檢查範圍都要問「這是誤判，還是把債藏起來」。**

**剩餘 2 筆 E003**（真斷鏈，可直接修）：`canonical/periodization/structure.yaml` 條目 `periodization.structure.gas` 的 `links.related` 用短名 `macrocycle` / `microcycle`，應為 `periodization.structure.macrocycle` / `periodization.structure.microcycle`。

**S4b 的 20 筆定位**：全在 `canonical/health/injuries.yaml`（三個欄位各 44 次出現、共 132 處，其中 112 為 null，20 有散文值）。⚠ **`injuries.yaml` 是 `tools/build_injuries.py` 產生的 promoted artifact，不可直接改**；一律改 `canonical/health/drafts/*.yaml` 後重跑生成器。

~~**S2 待用戶裁定（阻塞中）**：`category` 的 36 個值混了兩種語意……要拆成兩個欄位，還是保留單欄位用命名空間前綴？~~ → 已於 2026-07-26 解決，見下方「S2 驗收」：**不拆欄位**，改用 per-value `scope` + `domain_of()`。

#### S4c 驗收（2026-07-26）

`python tools/validate.py`：**0 ERROR / 584 WARN**；`python -m unittest discover -s tests`：**42 tests OK**（原 28 + 新增 14）。

**資料契約決定（不可回退成陣列）**：`cross_ref` 維持自由文字顯示層，**逐字不動**；新增 `cross_ref_ids`（list of string）當機器鍵。理由：下游 `my-site/layouts/vortex/vortex-database.html` 第 103 行把 `cross_ref` 當純字串渲染（`{{ with .cross_ref }}{{ . }}{{ end }}`），改成陣列會在線上印出 Go slice 字面值 `[a b c]`。語意約定：`cross_ref_ids: []` = **已檢查、確認無 ID 可連**；欄位缺席 = **尚未處理**（觸發 W006）。

**61 筆的實際分類（重新統計，與用戶估計不符處已標出）**：

| 項目 | 用戶估計 | 實測 | 差異說明 |
|---|---|---|---|
| 分佈檔案 | 全在 `teaching-errors.yaml` | **45 在 `teaching-errors.yaml` + 16 在 `technical-analysis.yaml`** | ⚠ 估錯。S4c 範圍依「W001 = 61 筆」這個錨點，兩檔都做了；只做 45 筆會留 16 筆警告 |
| 內嵌可解析 ID | 26 | **27**（teaching-errors 12 + technical-analysis 15） | 多 1 筆 |
| 節號／散文指向 | 35 | **34**（teaching-errors 33 + technical-analysis 1） | 少 1 筆 |

**「看起來像 ID 但解析不到」的 token：0 筆**。但這一項查出更值得記的東西——**S4c 之前 W001 的抽取邏輯本身是漏的**：舊 `_CANDIDATE_ID_RE` 要求命名空間最後一段必須是純數字、且不允許連字號，所以 `back.err2`、`starts-turns.err10`、`starts-turns.tech.44` 這類真實 ID **從來沒被抽出來過**。第一輪分析因此誤報 22/39，修正 regex 後才得到 27/34。也就是說：舊 W001 不只是「沒解析」，是**連候選都少認**。修正後重跑，W004 區塊逐字無差異（確認 regex 改動沒有外溢影響）。

**臨機規則（僅存在於一次性補欄腳本，此處存證）**：`free.tech.4/5/6` 這種斜線簡寫（出現在 `free.tech.32`、`free.tech.35`）展開成三個 ID 寫入。已先確認 `free.tech.5` / `free.tech.6` 確實存在才展開。驗證器**不**內建此規則——未來若有人再寫斜線簡寫，會正常觸發 W001 要求手動處理，這是刻意的。

**遺留債（S4c 範圍外，未動手）——34 筆節號類 `cross_ref`**：這些指向 `Instructional/` 散文的節號，例如 `技術分析 §2.1`、`技術分析 §伍（身體旋轉）`、`技術分析 貳2.2 動力傳遞鏈`、`技術分析 拾壹11.3 不同距離技術差異化`。**canonical 目前沒有散文章節的穩定 ID**，`Instructional/自由式深度技術分析.md` 的標題是 `## 壹、分析框架：自由式的物理本質` 這種形式，無 ID 可指。

- 建議：**在 `Instructional/` 散文層建立章節級穩定 ID**（如 `doc.free-tech-analysis.§2.1`），登錄進全域 ID 集合後回填這 34 筆。
- 理由：這 34 筆不是壞資料，是**指向了一個還沒被納入 ID 體系的層**。若不做，`cross_ref_ids: []` 會永遠停在「已檢查、無 ID 可連」，等於承認散文層永遠只是顯示層、不可機器追蹤——那 knowledge-hub 的關係圖會缺掉「教學誤區 ↔ 技術分析」這條最密的連結（34/61，超過一半）。
- 成本：要先決定散文章節 ID 的粒度（章 vs 節 vs 小節）與命名法，並確保散文標題改寫時 ID 不漂移。這是 schema 決策，不是機械工作，**不適合順手做**。

**順帶查出、未修的資料品質問題 1 筆**：`technical-analysis.yaml` 的 `fly.tech.12`，其 `cross_ref` 值是「2024–2025 外划幅度縮小趨勢已成為精英教學主流演進方向」——這根本不是交叉參照，是一句趨勢陳述被誤填進 `cross_ref` 欄位。已給 `cross_ref_ids: []`（依約定正確），但**欄位誤用本身沒改**，因為改它等於動 `cross_ref` 顯示層內容，超出 S4c「只加欄位不改內容」的界線。這是 technical-analysis 唯一那筆非節號類的散文。

**刻意不做的變更**：W003 孤兒偵測仍只讀 `links.*`，`cross_ref_ids` **不**計入出向連結。若計入，W003 會從 476 掉下來——但那是把「顯示層參照」偷渡成「結構化關係」，屬於用計算方式讓數字變好看，不是真的補了連結。要改應是明確決策，不是 S4c 的副作用。

**新增檢查碼**：E006（ERROR，`cross_ref_ids` 內含無法解析的 ID，fail-closed 已實測：塞入 `free.tech.999` → exit=1）／W001 重新定義（`cross_ref` 內的疑似穩定 ID 未列入同層 `cross_ref_ids`）／W006（`cross_ref` 有值但 `cross_ref_ids` 欄位整個缺席）。測試 harness 原本自行複製一份驗證邏輯（**導致語意改動後 28 tests 仍全綠的假陽性**），已改為直接呼叫 `validate.build_global_id_set()` 與 `validate.check_cross_ref()`。

**當前基線**：E001–E006 全 0；W001 **0**（原 61）、W002 88、W003 476、W004 20、W005 0、W006 **0**。`python tools/build_knowledge_map.py` 跑通且 `KNOWLEDGE_MAP.md` 無 diff。

#### S4b 驗收（2026-07-26）

`python tools/validate.py`：**0 ERROR / 564 WARN**（原 584）；`python -m unittest discover -s tests`：**53 tests OK**（原 42 + 新增 11）。

**資料契約決定（與 S4c 同型，不可回退成陣列）**：`mechanism_link` / `technical_link` / `perception_link` 維持自由文字顯示層，**逐字不動**；新增同名 + `_ids` 的機器鍵（list of string）。理由同 S4c：下游 `my-site/layouts/vortex/vortex-injuries.html` 第 262–264 行把三個欄位當純字串渲染（`{{ with .mechanism_link }}{{ . }}{{ end }}`），改陣列會在線上印出 Go slice 字面值。語意約定：`*_link_ids: []` = **已檢查、確認無 ID 可連**；欄位缺席 = **尚未處理**（觸發 W007）。112 筆 null 的 `*_link` 不補欄位（無值可檢查）。

**20 筆的實際分類（重新統計）**：

| 項目 | 用戶估計 | 實測 | 差異說明 |
|---|---|---|---|
| A 類：值本身就是合法傷害 ID（裸 slug） | 7 | **7** | 一致 |
| B 類：散文內嵌可解析 ID（`free.tech.10`） | 1 | **1** | 一致 |
| C 類：純散文、canonical 無對應目標 | 12 | **12** | 一致 |
| 分佈檔案數 | 12 | **16 個 drafts 檔** | ⚠ 唯一估錯處。`swimmers-shoulder` 與 `breaststrokers-knee` 各自三個欄位都有值，所以 20 筆散在 16 檔而非 12 檔 |

**C 類 12 筆為什麼連不上（逐類）**：

- **水感層級（6 筆）**：`perception_link` 寫 `L4–L6 手感與全身張力`、`L2–L4 腳感層`、`可接 L0 呼吸感知` 這類裸層級。canonical 的水感 ID **全是泳式限定**（`free.L0` … `fly.L6`，另有 `breast.pre` / `fly.pre`），沒有跨泳式的 `L0`／`L4`，所以裸層級與區間寫法（`L4–L6`）都解析不到。
- **不存在的技術條目（4 筆）**：`蛙式踢腿技術分析(外翻角/髖帶動)`（散文自己就寫「待對應 canonical technical 條目」）、`racing start` 出發台技術（`diving-cervical-injury` 與 `starting-block-impact` 各一筆，兩者以中文互指「與出發台撞擊傷共享預防」／「與跳水頸椎傷共享水深/角度預防」）、`翻滾轉身技術`。canonical technical 層目前沒有出發／轉身的獨立技術條目可指。
- **機制敘述而非參照（2 筆）**：`swimmers-shoulder` 的 `mechanism_link`（前鋸肌耐力→EVF 硬體前提）與 `breaststrokers-knee` 的 `mechanism_link`（踢腿外翻負荷可接「硬體邊界 vs 感知缺陷」判斷）。這兩筆是把欄位當說明文字用，指向的是**概念**不是條目。

**刻意不推論**：`diving-cervical-injury` ↔ `starting-block-impact` 用中文名互指，兩邊 ID 其實都存在，但該欄位的實際指向是「racing start 技術條目」而非對方傷害條目；把對方 ID 填進去等於改寫語意。兩筆都給 `[]`，列為發現不動手。

**遺留債建議 1 —— 水感層級該不該建可被 health 層引用的穩定 ID**：**建議建**，但要當 schema 決策做，不是順手。現況是水感 ID 綁泳式（`free.L4`），而傷害條目講的是**跨泳式的感知層級本身**（「手感與全身張力」不分自由式蛙式）。若不建，這 6 筆會永遠停在 `[]`，knowledge-hub 的關係圖會缺掉「傷害 ↔ 感知層級」這條軸。可行做法是在 taxonomy 登錄 `L0`–`L6` 為跨泳式層級 ID（與泳式限定 ID 並存、互為 parent/child），但要先決定區間寫法（`L4–L6`）是展開成三個 ID 還是禁用。

**遺留債建議 2 —— 出發／轉身技術條目缺席**：4 筆 C 類裡有 3 筆指向出發台入水角度、racing start、翻滾轉身。canonical 已有 `starts-turns.*` 命名空間（`starts-turns.tech.44` 等），但沒有可被傷害層引用的「技術動作」層條目。這是內容缺口不是資料缺陷，補內容時順手回填即可。

**顯示層債（記錄，S4b 範圍外，未動手）**：A 類 7 筆的 `*_link` 值本身就是裸 slug，網站上現在會渲染成「機制關聯 red-s」「機制關聯 female-athlete-triad」這種**未翻譯的英文 slug**，對讀者不友善。涉及的 7 筆：`exercise-amenorrhea`→`female-athlete-triad`、`female-athlete-triad`→`red-s`、`stress-fracture-swimmer`→`swimmer-low-bone-density`、`swimmer-low-bone-density`→`female-athlete-triad`、`salter-harris-physeal-fracture`→`diving-cervical-injury`、`scheuermann-kyphosis`→`extension-low-back-pain`、`youth-swimmer-apophysitis`→`rotator-cuff-tendinopathy`。修法有兩條（顯示層改中文名／`*_link_ids` 存在時改渲染成連結），**兩條都是改顯示內容或改 my-site 模板，超出 S4b「只加欄位不改內容」的界線**，未動。

**新增檢查碼**：E007（ERROR，`links.*_link_ids` 內含無法解析的 ID 或型別非 list）／W004 重新定義（`*_link` 內的疑似穩定 ID 未列入對應 `*_link_ids`）／W007（`*_link` 有值但 `*_link_ids` 欄位整個缺席）。

#### ⚠ S3 範圍重估：W002 = 88 是**嚴重低報**，實際約 510（2026-07-26）

動手 S3 前先量了一次，發現 W002 的檢查範圍有覆蓋缺口。`tools/validate.py` 的 W002 只查兩個位置——`entry.certainty` 與 `entry.public.mechanism.certainty`。但 canonical（不含 drafts）裡帶 🟢／🟡 的區塊實際分佈是：

| 位置 | 數量 | 有 `source` 顯示字串 |
|---|---|---|
| `evidence[]` | 201 | 多數有 |
| `references` | 101 | — |
| `mechanism` | 88 | **全無** |
| `phenomenon` | 44 | 部分 |
| `epidemiology` | 37 | 部分 |
| `physical_reason` | 19 | 部分 |
| `intervention_refs` / `hardware_boundary` / `premise` / 其他 | 19 | 部分 |
| **合計** | **510** | 201 有 / 309 無 |

**所以 S3 的真實工作量是 ~510 個區塊、138 個不重複來源字串，不是 88。** 先前 HANDOFF 寫的「S3 = 88 筆」要作廢。

**兩種債性質完全不同，必須分開處理**：

1. **有 `source` 顯示字串的 201 筆**：格式是 `Staunton, Ruiz-Navarro & Born 2025`、`Maglischo 2003`、`Nicol et al. 2022`（出現 11 次，最高頻）這種作者＋年份，**沒有 DOI／PMID／ISBN**。這批可機械處理：去重成 138 個 `src.*` 條目寫進 `_sources.yaml`、`display` 逐字保留、`locator: null` + `verification_status: unverified`，條目加 `source_ids`。**零內容改動、零捏造風險**。
2. **完全沒有 source 字串的 309 筆（含 mechanism 全部 88 筆）**：這批不是「忘記填來源」，而是**確定性標記本身可能標錯**。實例 `free.tech.3` 的 `mechanism.certainty: 🟢` 但文字是「SR 提高而 SL 下降是『技術沒有同步支撐划頻』的結果，不是物理必然」——這是**從 evidence 推導出的詮釋**，按專案的確定性階梯應該是 🔵推導，不是 🟢近期文獻。**逐筆判斷是內容工作，不可機械批次，也不可外包給不懂框架的 agent 亂降級。**

**因此 S3 拆成三段**：

| 段 | 內容 | 性質 | 風險 |
|---|---|---|---|
| S3a | 138 個來源字串 → `_sources.yaml` 註冊 + 201 筆加 `source_ids`；同時修 W002 覆蓋缺口（改成掃所有帶 `certainty` 的區塊） | 純機械 | 低。加欄位不換內容 |
| S3b | 309 筆無來源的 🟢／🟡 逐筆判定：該降 🔵推導，還是漏填引用 | 內容判斷 | **高**。動確定性標記＝動對外可信度宣告 |
| S3c | 138 個來源補 DOI／PMID／ISBN（WebSearch + 追一手） | 查證 | 中。**嚴禁捏造識別碼**，查不到就留 `unverified` |

S3a 可立刻派工；S3b 建議先做一個 10 筆的 pilot 看判定準則穩不穩，再決定要不要批次；S3c 是既有查證債（HANDOFF 別處已記錄 49 處 `pending_verification`）的同類工作，可合併規劃。

**順帶補的抽取漏洞**：舊 `extract_candidate_ids()` 只認命名空間 ID 與 Drill ID，**認不出裸 slug**（無點號）——而 A 類 7 筆正好全是裸 slug，等於新 W004 對主流形態零覆蓋。修法是在共用的 `missing_declared_ids()` 裡加一種候選：整個字串本身就是可解析 ID 時列為候選（**不是**加第二套 regex）。此改動同時作用於 W001，實測 `cross_ref` 目前 0 筆屬此形態，故 W001 維持 0，無外溢。

**測試誠實性**：harness 原本自帶一份 W004 邏輯副本（S4a 事故同型），已刪除並改為直接呼叫 `validate.check_link_ids()`。用突變測試驗證過覆蓋率——把產品端迴圈掏空 → 7 個測試失敗；還原 → 53 OK。

**`tools/build_injuries.py` 未改**：確認它是整筆 `yaml.safe_load` / `safe_dump`，新鍵自動帶過。`injuries.yaml` 由重跑生成器產生（+28 行：20 個新欄位，其中 8 個非空清單以 block style 各佔 2 行），**未手改**。

**刻意不做的變更**：同 S4c，W003 孤兒偵測**不**把 `*_link_ids` 計入出向連結，所以 W003 維持 476 無位移。要改應是明確決策。

**當前基線**：E001–E007 全 0；W001 0、W002 88、W003 476、W004 **0**（原 20）、W005 0、W006 0、W007 **0**。`python tools/build_knowledge_map.py` 跑通且 `KNOWLEDGE_MAP.md` 無 diff（地圖不呈現 `*_link_ids`，符合預期）。

**另記**：4 個 drafts 檔完全沒有 `links` 區塊——`_asian-epidemiology-supplement`、`iron-deficiency-swimmer`、`oral-contraceptives-performance`、`sci-hip-flexor-contracture`。未觸發任何警告（無 `*_link` 值可檢查），但值得日後確認是刻意還是漏填。

#### S3a 驗收（2026-07-26）

**已完成**：138 個來源登錄進 `canonical/_sources.yaml`，201 個 🟢／🟡 區塊加上 `source_ids`（`technical-analysis` 121、`teaching-errors` 46、`l-indicators` 34），孤兒來源 0、斷鏈 0。`source` 顯示字串**一字未動**（前兩檔是純插入 0 刪行，`l-indicators` 是 flow style 只在 `}` 前追加 `, source_ids: [...]`）。

**`_sources.yaml` 契約改到 v2，改了什麼、為什麼**：

v1 把 `title` / `authors` / `year` / `identifier` / `retrieved_on` 全列必填，且 `identifier` 至少要有一個可重取識別。但實際 138 筆裡，多數只有「作者＋年份」，有些連作者都沒有（`PMC6409673`、`PLOS ONE 2020`），5 筆根本不是文獻（「通用游泳醫學共識」「歷史背景」）。照 v1 走，唯一能填滿的辦法就是去猜 DOI／期刊／標題——正是明文禁止的捏造。**所以是契約錯，不是資料錯。**

| 欄位 | v1 | v2 | 理由 |
|---|---|---|---|
| `verification_status` | 無 | **無條件必填**，封閉值域 `verified`／`unverified` | 把「查沒查過」變成資料本身的欄位，而不是靠註解 |
| `display` | 無 | **無條件必填** | 逐字保留原顯示字串當溯源錨點，S3c 靠它對回原文位置 |
| `id` / `type` | 必填 | 維持無條件必填 | 不查證也能確定為真 |
| `title` / `identifier` / `retrieved_on` | 必填 | **僅 `verified` 時必填** | 沒查過就沒有標題／識別碼／查驗日可填 |
| `authors` / `year` | 必填 | **僅 `verified` 時必填**（超出原指示） | 原指示只點名 title/identifier/retrieved_on，但實測有無作者、無單一年份的字串（複合字串、純 PMC 編號），不放寬同樣會逼出捏造 |
| `container` / `et_al` / `notes` | 無 | 選填 | `et_al` 用布林標記「作者蓄意不完整」，而不是把字面 `et al.` 塞進 `authors` 讓它看起來像人名 |

**138 筆全部 `unverified`——包含那 40 筆有識別碼的。** 原指示允許把帶 DOI／PMID 的標成 `verified`，但我的契約要求 `verified` 必填查驗日，而我一筆都沒有 dereference 過，標 `verified` 就得編一個查驗日，違反最重要那條。折衷是：識別碼照樣**逐字轉錄**（23 筆來自顯示字串內的 PMID／PMCID／DOI，17 筆來自同層 `url:` 欄位，合計 40 筆），但狀態留 `unverified`。S3c 只要把這 40 筆查一遍就能直接翻成 `verified`，零資訊損失。

**順帶更正原任務書的一個前提**：任務書寫「這批**沒有 DOI／PMID／ISBN**」，實際上 138 筆裡 23 筆字串內就帶識別碼，另有 30 個區塊帶同層 `url:`（各顯示字串對應的 url 無衝突）。

**刻意不合併的疑似重複（25 組、共 64 筆）**：碰撞者各給獨立 ID（依 display 排序加 `-a/-b/-c`），notes 互指「疑似同一文獻，待 S3c 查證後合併」。**寧可留可合併的重複，不可誤併成一筆**——誤併會把兩篇不同文獻的主張混在同一個 `source_id` 底下，事後從資料上看不出來；重複只是暫時多幾筆，S3c 查到 DOI 後合併是安全的單向操作。典型無法判定的例子就是 `Staunton et al. 2025` vs `Staunton, Ruiz-Navarro & Born 2025`。

- 4 筆組（4 組）：`staunton-2025`、`sanders-1995`、`maglischo-2003`、`pmc8960438`
- 3 筆組（6 組）：`atkison-2014`、`gonjo-2020`、`gonjo-2021`、`nicol-2022`、`strzala-2013`、`tanaka-2024`
- 2 筆組（15 組）：`benjanuvatra-2007`、`colman-1998`、`gonzalez-rave-2025`、`journal-pone-0241345`、`mason-1992`、`mccullough`、`mccullough-2009`、`novais-2012`、`pink-1991`、`pmc4234766`、`pmc6409673`、`pmc8442910`、`pmc9402090`、`pmid-40252339`、`welcher-2008`
- 另有 **13 組跨消歧組共用識別碼**（如 pmid 24290609 橫跨 `atkison-2014-a/b/c`、pmid 27149652 橫跨 `takai`／`takai-2016`、pmid 24984154 橫跨 `pmid-24984154`／`pmc9402090-a`），同樣在 notes 互相標注、同樣不合併。

**其他 S3a 沒動、留給 S3c 的**：20 筆是複合字串（一個字串含多筆文獻，以 `;`／`；` 分隔）→ 待拆；5 筆非文獻引用（通則／共識敘述）→ 須判定改標確定性或補實際來源；34 筆無識別碼且缺作者或年份，不足以唯一定位。全部已寫進各筆 `notes`。

**`tools/validate.py` 改動**：

- **W002 覆蓋缺口已修**：改成遞迴掃描任何含 `certainty` 的 dict（新增 `iter_blocks()`），不再只看 `entry.certainty` 與 `entry.public.mechanism.certainty`。覆蓋從 88 跳到 510。
- **W002 拆成兩碼**（原指示允許同碼不同訊息或拆碼，選了拆碼，因為兩者修法完全不同、且 W002 應該歸零而 W009 是長期債）：
  - **W002 = 39**：🟢／🟡 且**有**來源顯示字串但缺 `source_ids`。這 39 筆全是 `sources`（**複數清單**）格式，來自 `health/injuries.yaml` 與 `psychology.yaml`，不在 S3a（`source` 單數字串）範圍。S3a 該歸零的部分**已歸零**。
  - **W009 = 270**：🟢／🟡 且**完全沒有**任何來源資訊 → S3b 範圍。（39 + 270 = 309，與 S3 範圍重估的 309 對得上。）
- **E008 沒有新增，改為擴充 E005**：查過既有 E005，語意已經就是「`source_ids` 指向 `_sources.yaml` 不存在的 ID → ERROR」，只是**只跑條目頂層**，對全部落在巢狀 `evidence[]` 的 201 筆機器鍵零覆蓋。新增第二個碼會是重複定義，所以改成遞迴，並補了型別錯誤與非字串元素兩種情況。
- **W008（新增）**：`_sources.yaml` 有登錄但無任何條目引用的孤兒來源。目前 0。

**測試誠實性**：harness 原本自帶一份 E005／W002 邏輯副本（與 S4a、S4c 同型事故）。已刪除，改為呼叫產品端新抽出的 `check_source_blocks()` 與 `check_orphan_sources()`。53 → **67 tests OK**（原 2 個 W002 測試改寫成 7 個涵蓋 W002／W009 分流與巢狀掃描，另加 6 個 E005、3 個 W008）。

**當前基線**：E001–E007 全 0；W001 0、**W002 39**（原 88，語意已變）、W003 476、W004 0、W005 0、W006 0、W007 0、**W008 0**、**W009 270**。總計 0 ERROR / 785 WARN（原 564；增加的 221 是原本就存在、只是掃不到的債）。`python tools/build_knowledge_map.py` 跑通且 `KNOWLEDGE_MAP.md` 無 diff。

**發現但沒處理的問題**：

1. **176 個帶 `source` 顯示字串的區塊不在任何檢查裡**（canonical 共 377 個 `source` 區塊，S3a 只覆蓋 201）——它們的 certainty 是 🟠 118／無 57／🔵 1，不觸發 W002/W009。分佈：`teaching-errors` 93、`technical-analysis` 20、`periodization/structure` 20、`periodization/zones` 17、`periodization/taper` 10、`periodization/dryland` 7、`l-indicators` 6、`health/breathing-training` 3。其中 `periodization/*.yaml` 那 54 筆的 `source` 字串**帶真 DOI／PMID**（如 `Mujika & Padilla 2003 (PMID 12840640)`、`DOI 10.3389/fphys.2025.1638739`），品質比 S3a 這批高，卻因為所在區塊**沒有 `certainty` 欄位**而完全落在網外。這是**檢查條件綁 certainty 造成的盲區**，值得單獨決策：要不要改成「有 `source` 就該有 `source_ids`」（那樣 W002 會從 39 跳到 215）。
2. **`sources`（複數清單）與 `source`（單數字串）是兩套並行格式**，前者用在 `injuries.yaml`／`psychology.yaml`（49 + 62 個清單），且已含已驗證的 PMCID。S3a 沒碰。要不要統一、以及複數清單怎麼對到 `source_ids`，需要先決策再動。
3. **`title` 全部留空**（138/138）。這是刻意的——寧可空白也不編。但代表 `_sources.yaml` 目前對人類讀者的可讀性只靠 `display`。
4. **W003 = 476 未動**：同 S4b/S4c，孤兒偵測不把 `source_ids` 計入出向連結。要改應是明確決策，不順手改。

#### S3a-2 驗收（2026-07-26）

處理 S3a 發現 ① ②。**決策：來源檢查與 `certainty` 解耦**——「這個區塊有沒有標確定性」跟「這個來源該不該被註冊」是兩件事，綁在 `certainty` 上是原始 W002 框架的殘留。

**`tools/validate.py` 檢查語意改動**：

| 碼 | 舊條件 | 新條件 |
|---|---|---|
| W002 | 🟢／🟡 **且**有 `source`／`sources` 但缺 `source_ids` | **有 `source`／`sources` 就必須有 `source_ids`**，不看 `certainty`（訊息尾綴標 `certainty=green/yellow` 或 `無 certainty`，兩態可分辨） |
| W009 | 🟢／🟡 且完全無來源資訊 | **維持不變**——「宣稱高確定性卻連顯示字串都沒有」的語意本來就以 `certainty` 為前提，綁對了 |

**掃描範圍另外加上 `Drills/*.yaml`**（176 個帶 `source` 的區塊原本完全在網外）。只把 Drills 納入**來源契約這一組**檢查（E005／W002／W009），**不**併進 `validate_files`——後者會連帶把 E001/E004/W003/W005 等 canonical 專屬規則套到 Drills 上，那是另一個決策，不在本批範圍。

**`sources`（複數）不改名。** `my-site/layouts/vortex/vortex-injuries.html:180` 是 `{{ with .sources }}{{ range ... }}`，改名直接打壞線上頁面。改法是驗證器**同時接受兩種形態**、兩種都要求 `source_ids`。格式統一列為 legacy debt（見文末）。

**遷移成果**：`_sources.yaml` 138 → **476 筆**（+338），全部 `verification_status: unverified`，130 筆帶逐字轉錄的 `identifier`。**既有 138 筆的 `id` 一律釘住不動**——新來源若與既有 base 碰撞，只能往後續排字母（既有無字母的 `src.<base>` 視同佔用 `-a` 位，新成員從 `-b` 起）。舊筆只有 6 筆被改動，且**只改 `notes`**（`src.mccullough-a/-b`、`src.pmc6409673-a/-b`、`src.race-club`、`src.ward-2018`，各追加一句「疑似與 … 為同一來源，待 S3c 查證後合併」）。

`source_ids` 補齊 **463 處**，分佈：`Drills/*.yaml` 176、`teaching-errors` 93、`psychology` 62、`injuries`（經 drafts 重生成）49、`technical-analysis` 20、`periodization/structure` 20、`zones` 17、`taper` 10、`dryland` 7、`l-indicators` 6、`health/breathing-training` 3。**`source` 顯示字串逐字未動**——65 個改動檔全數比對 HEAD，0 字串變更。`injuries.yaml` 未手改，由 `tools/build_injuries.py` 重生（149 插入／0 刪除）。

**`periodization/*` 的識別碼照原則處理**：字串內的 PMID／DOI（`Mujika & Padilla 2003 (PMID 12840640)`、`DOI 10.3389/fphys.2025.1638739` 等）**逐字轉錄進 `identifier`，但狀態留 `unverified`**——沒 dereference 過就不能標 `verified`（會逼出捏造的查驗日）。

**測試**：67 → **75 tests OK**。新增 `TestW002DecoupledFromCertainty`（4：無 certainty 的 `source` 仍觸發、`sources` 複數同樣觸發、無 certainty 也無來源時靜默、補 `source_ids` 後解除且不製造 W008）與 `TestSourceCheckCoversDrills`（4：Drills 的 W002／E005／W008 計數／W009）。harness 一樣直接呼叫產品端 `check_source_blocks()`，無邏輯副本。**突變測試驗過覆蓋率**：把 W002 重新綁回 `certainty` → 5 個測試失敗；把 Drills 移出掃描範圍 → 4 個失敗。

**當前基線**：E001–E007 全 0；W001 0、**W002 39 → 0**、W003 476（未動，同前批決策）、W004 0、W005 0、W006 0、W007 0、W008 0、**W009 270（不變，解耦不影響其語意）**。總計 0 ERROR / 746 WARN。`build_knowledge_map.py` 跑通且 `KNOWLEDGE_MAP.md` **無 diff**（地圖不呈現 `source_ids`，符合預期）。

**仍未被任何檢查覆蓋的帶 `source` 區塊：49 個，不是 0。** 全部在 `canonical/health/drafts/`（48 檔各 1 個 `epidemiology.sources`，`_asian-epidemiology-supplement.yaml` 2 個）。原因是 `is_excluded()` **刻意**把整個 `drafts/` 排除在所有檢查外——drafts 是 `injuries.yaml` 的建構來源，納入掃描會讓每個傷害條目都觸發 E002 重複 ID 誤報。**資料本身已被覆蓋**：這 49 個區塊的內容經 `build_injuries.py` 升格進被掃描的 `injuries.yaml`，且該 49 個 draft 區塊本身也都已補上 `source_ids`。所以這是**檢查器覆蓋的缺口，不是資料的缺口**。要真正歸零需先讓驗證器分辨「來源建構層 vs 升格產物」，屬獨立決策。

**legacy debt（本批刻意不動）**：

1. **`source`／`sources` 兩套格式並存**。統一需同時改 canonical 資料、`build_injuries.py` 與 `my-site` 模板，跨 repo 且會動到線上頁面，須獨立決策。
2. **90 筆識別碼已轉錄但未 dereference**，S3c 查一遍即可翻 `verified`，零資訊損失。
3. **55 筆複合字串**（一個字串含多筆文獻，以 `;`／`；` 分隔）待拆。
4. **73 筆是內部交叉參照**（`Research/心理/NN_*.md#anchor`），已給 `research-psych-NN` 系列 ID，但它們是專案內部檔案錨點而非外部文獻，日後可能該改用另一種指涉機制。
5. **Drills 的書籍章節來源缺頁碼**（如 `There's a Drill for That`），只能定位到書不能定位到段落。

#### S2 驗收（2026-07-26）——canonical 側完成，my-site 側待做

**核心決策：`category` 不拆欄位，改用 per-value `scope`。**

拆欄位（`category` → `technique_category` + `injury_category`）要同時改四份 my-site layout 與 `vortex-database.html` 的 `where $injuries "category" "D-systemic-acute"`，跨 repo 且會動線上頁面。實際上 `category` 是**三個互不相交的值空間共用一個欄位名**：instructional（技術面向）、health（傷害類別，`A-`–`F-` 前綴排序即嚴重度分層）、drills（練習環節）。只要在 `_taxonomy.yaml` 每個值上宣告 `scope`，再由 `domain_of(rel)` 從檔案路徑推網域，驗證器就能擋跨域誤用——**欄位名一個字都不用動**。三個重疊值（`kick`／`timing`／`turn`）語意相容故共用 scope。

**標籤不上收 taxonomy。** 同一個 key 在不同檔可有不同措辭（`kick` 在 technical-analysis 是「踢水與腿部機制」，在 teaching-errors／drills 是「踢腿」）。所以 `_taxonomy.yaml` 只擁有**合法 key 集合 + scope**，各資料檔自己的 `categories:` 區塊擁有**標籤**。新建 `Drills/_categories.yaml` 補上 Drills 缺的那一份（7 個 key）。

**內容歸一（逐筆有證據，非猜測）**：

| 動作 | 值 | 依據 |
|---|---|---|
| 合併 | `body-position`（back.err9）、`core`（back.err13）→ `posture` | `posture` 原本**宣告了但零條目**（孤兒），這兩個是未宣告條目卻正屬於它——一次解掉一個孤兒 + 兩個未宣告 |
| 合併 | `approach`（starts-turns.err11）→ `turn` | 內容是「轉身 approach 速度」，本就是 turn 環節 |
| 合併 | `tactic`（free.tech.31）→ `fatigue` | 內容是「30 秒後系統性下降」，是疲勞不是戰術 |
| 合併 | teaching-errors 的 `breathing` 12 筆 → `head` | 兩者標籤**同為「頭部與換氣」**、內容全是換氣時的頭位；統一到 `head` 後 `breathing` 收斂為 drills 專用（標籤「呼吸」），三網域 scope 乾淨切開 |
| 保留宣告 | `coupling` | 橫跨 **8 個檔案**的框架級概念，不是雜訊 |
| 補宣告 | `breakout`（2）、`recovery` | 真實且相異的類別，補進所屬檔的 `categories` 區塊 |

**驗證器新增三碼**（`load_category_scope()` / `domain_of()` / `check_category_scope()` / `check_file_categories()`）：

- **E008** 值合法但 scope 不含本檔網域（跨域誤用）。**未宣告 scope＝空集合＝報錯**，不是靜默放行。
- **E009** 條目的 `category` 未宣告於**該檔自己的 `categories` 區塊**。這正是本批在 my-site 抓到的兩個線上 bug 的機制：Hugo 的 `{{ index $dict .key }}` 查不到 key 會回**空字串且不報錯**，標籤就這樣人間蒸發。
- **W010** 死標籤（宣告了沒條目用）。

**E008 一度是死碼——突變測試抓到的。** 前兩個突變（health 值塞進 drill 條目、把 `arm` 的 scope 清空）都回報 **E008: 0 筆**，因為 per-entry 迴圈跑的是 `validate_files`，而它**刻意排除 `Drills/`**（S3a-2 的決策）。先用「把 `arm` 塞進 canonical teaching-errors 條目」證明 E008 本身會動（1 筆），再把 E004／E008 補進 Drills 專段。重跑四個突變全部攔下：突變 2 → E008 1 + E009 1；突變 3 → **E008 51**；突變 4（Drills 塞不存在的值）→ E004 1 + E009 1；還原 → exit 0。**教訓同 S4a：新檢查上線前必須突變測試，否則「0 筆」分不清是乾淨還是沒跑到。**

**測試**：75 → **90 tests OK**。新增 `TestE008CategoryScope`（6）、`TestE009FileCategories`（5）、`TestDomainOf`（4），全部直呼產品端函式。

**當前基線**：`python tools/validate.py` **0 ERROR／746 WARN**（E001–E009 全 0；W003 476、W009 270 未動，同前批決策；W010 0）。`KNOWLEDGE_MAP.md` diff **恰為 16 行 category 改名**，無非預期變動。兩份 instructional 檔 0 未宣告／0 孤兒 category。

**同批修掉的兩個 my-site 線上 bug**（已 push，CI 綠）：

- `vortex-stroke.html:40` 的 `$drillCatName` 漏了 `turn` → starts-turns 頁 9 張 drill 卡的分類標籤全空（commit `0597861`）。
- `vortex-database.html:15` 硬編了一份漂移的 `$injCatName`，而 `injuries.yaml` 早已自帶 `categories` 區塊 → 改成從資料 merge，同時修好三個標籤漂移（肩與上肢→肩部與上肢、內分泌→內分泌與骨骼、急性創傷→急性外傷）（commit `6bdd91f`）。

**S2 的 my-site 側——已完成**（commit `ba03da8`／`19da9d2`，CI 綠）：

1. `sync_vortex.py` 的 `sync_drills()` 現在把 `Drills/_categories.yaml` 帶進 `data/vortex/drills.yaml` 的 `categories` 區塊（與 teaching-errors／technical-analysis 同一模式）。
2. `vortex-drills.html:16` 與 `vortex-stroke.html:40` 兩處 `$drillCatName` 改成從資料 merge。**站上已無任何硬編分類標籤字典**（`grep "CatName := dict \""` 零命中）。
3. 同批把 canonical 累積未同步的內容一併帶下去（`source_ids`、S2 的 category 歸一、`periodization.structure.related` 短名修正、兩筆 🟠→🟢）。**24 行刪除逐條稽核過**，全數為預期改名／修正，無內容遺失。
4. **驗證**：176 張 drill 卡的分類標籤逐筆比對 `drills.yaml`，7 類數量全中（呼吸 5／平衡 13／踢腿 43／划手 51／銜接 42／搖櫓 13／出發轉身 9），**0 空標籤**。
5. 規則寫進 `my-site/CLAUDE.md`（「Vortex 分類標籤：一律從資料讀，禁止在 layout 硬編」），含 Hugo 靜默失敗的成因說明。

**legacy debt（本批刻意不動）**：

1. **`A-`–`F-` 前綴留著**。前綴同時承載排序（嚴重度分層），去前綴要協同改 my-site，屬獨立決策。
2. **`build_injuries.py` 的 `CATEGORY_ORDER` 仍是第二套排序真相源**。考慮過在 taxonomy 加 `sort_order` 收攏，未做。

### Hestia 報告整合後續（2026-06-22）

研究/instructional 散文層整合已完成、查證已逐筆把關。剩餘為可選後續：

- [ ] **殘餘 🔴 收束**：`低通氣訓練_VHL_RSH.md` 2 處（Woorons 2016 進步秒數 −3.7/−6.9/−13.6 待追原文摘要核對；Précart 2025 PMID 待從 PubMed eutils 核）；`出發與轉身技術分析.md` 1 處（轉身環節陸地訓練證據）；`Sweetenham` 1 處（報告「2022 reverse review」聲稱待獨立查證）。皆屬查證債，不阻塞。
- [ ] **（評估）升格 canonical**：本批新內容若要上 Vortex 網站，需先進 `canonical/periodization/*.yaml`（TID 分流、缺 RCT 證據缺口）或對應 instructional canonical（Veiga/Marinho/陸地訓練），再經 `my-site/tools/sync_vortex.py` 同步 + push。**目前停在 research/ 散文層，未觸發同步**（符合分層紀律）。觸發條件＝用戶要這些上線。
- [ ] **清理暫存區**：`research/_incoming-hestia-2026-06-20/`（raw json + md + INDEX）內容已整合，可清除或保留作來源存證。

### 運動傷害層：Phase 1 W3 引用查證（待派工）（2026-06-21）

骨架 + 整合 + 獨立審查 + 網站接入已完成、已上線。剩餘為查證債，**不阻塞發布**（pending_verification 欄位已使未核數字不進公開層）：

- [ ] **49 處 pending_verification 逐條查證**（人名/DOI/PMID/數字皆高幻覺區，須追到 PMC/PMID 一手核對，WebSearch 摘要數字不算）。優先含 6 個降 🔴 的引用：IOC RED-S consensus、ACSM position stand、ILCOR/AHA 溺水演算法、SIPE pathophysiology review、Sein 2010 (BMJ/BJSM)、McKenzie 2023 (DOI:10.1111/sms.14454)；另含台灣溺水數據、Scheuermann OR 值等。**派工 Sonnet**（並行 WebSearch + eutils），查完更新 drafts → 重跑 `build_injuries.py` → resync。
- [ ] **（可選）minimax-m3 最終複審**：MiniMax 月費明早 reset 後，可把 injuries.yaml 給 m3 做第二輪獨立審（用戶提過此選項，省 Claude 配額）。
- [ ] **（可選 Phase 2 精煉）**：把 `_asian-epidemiology-supplement`（現為獨立 meta_references）折進相關傷害的 population_notes/epidemiology。
- [ ] **（可選）** 釐清 swimmers-shoulder（傘狀）vs rotator-cuff-tendinopathy（具體）重疊——現兩條並存、傘狀條已註明 subtypes。

### 心理層：A/B/C/D 四批次已收束（2026-06-15）

心理層的缺口補強任務完成（查證債 / 整合缺口 / 族群覆蓋 / 補厚單薄段）。跨檔工程剩一件：
1. ~~**`隱性_顯性學習.md` 升 v2**~~ **已完成（2026-06-16，見當前狀態）**——並攔截更正一處 Liao & Masters 桌球/游泳誤歸因（連帶修 00/07/_INDEX/RESEARCH_PLAN）。
2. ~~**各 dossier 殘餘 🔴 逐條查證**~~ **已系統性收束（2026-06-16，B1–B4 全 8 dossier 引用查證，見當前狀態）**：所有「待查引用」🔴 已全數查證或釐清（含攔截 4 處誤歸因/誇大結果）；殘餘 🔴 皆為真研究空白（已明確標界「目前文獻無此數據」），保留為未來實驗設計起點，非未完成查證債。
3. ~~**Phase 2：心理層接入 Vortex 網站**~~ **全部完成（2026-06-16，見當前狀態）**——8 主題 62 概念全上線，三帶「心理地圖」著陸頁＋首頁入口＋public/diagnostic 分層 0 洩漏＋三關校正，my-site CI success。

### Phase 2 量產：心理層 8 主題全部完成 ✅（2026-06-16）

~~pilot+stub~~ → **全部 complete**。8 主題 62 概念，每條過三關校正、public/diagnostic 分層。其餘 7 主題由 7 個並行 Sonnet agent 各讀對應 dossier 寫出，ruamel round-trip merge 進 canonical（保留 fear 手寫格式）。沒過清單見當前狀態區。**族群全光譜紀律**：各 population_note 五族群分列、不窄化。
> **後續可選增強**（非必需）：① 加 concept 級 `populations`/level tag 做跨主題「依族群/分級篩選」（類似 database 的依需求找）；② 抽查各 agent 寫的 concept 內容品質（並行產出，未逐條人工複核 phenomenon 文字，建議 Hang 讀過一輪挑語氣/誇大）；③ database 跨泳式查資料頁是否納入心理層誤區。

### 週期化白話重寫 + 模組化（一源兩消費，plan-check 已備）

**plan-check 已完成（2026-06-08，Opus）**：`plans/periodization_integration_plancheck.md`。用戶需求：把週期化資訊整合、用 Claude 白話重寫（不照搬 Bompa 抽象敘述）、可整合的全整合、模組化讓 AI/人都好查。
- **核心架構決策**：在 `canonical/periodization/*.yaml` **各節點加 `plain_zh` 欄**（不另立白話模組）+ 新增 `canonical/periodization/_index.yaml` 概念目錄（source_id + 一行白話摘要 + cert）。本 repo 是「源」，主體工作在此。
- 靠 my-site `sync_vortex.py` 的 verbatim pass-through → 白話欄與 _index 自動流到 my-site `data/periodization/` 與 swim-coach submodule 兩端。
- **接手第一步**：讀該 plan-check 檔 → `/implement`（內含 8 步執行路徑、3 風險與預案、驗收、4 個待定案點、派工建議）。白話重寫不可外包（需 Claude 統一語感 + 反幻覺把關），列 manual。

### 當前最高優先——ADM 收編下游接通（Phase 2/3）

canonical/development/ 兩檔已落地（見當前狀態）。剩餘：

- [ ] **Step 6 my-site sync**：`my-site/tools/sync_vortex.py` 加 `sync_adm_matrix` + `sync_adm_standards`（仿 `sync_l_indicators`：讀 canonical development 兩層→剝 diagnostic→還原成 `adm-matrix.html` 現讀格式 `matrix.pillars[].stages[].{summary,points}`；納入 sync_state 追蹤）。
- [ ] **Step 7 my-site 驗證**：`--dry-run`→正式 sync→`hugo` build→ADM 頁面截圖比對渲染不變→commit+push（驗 CI 綠）。
- ~~**Step 8 swim-coach 退役**~~ **（取消——framing 錯誤，2026-06-10 用戶裁定）**：swim-coach 與網站是兩個不同東西，沒有「退役」這回事；原①②③作廢。canonical 是唯一真相源、swim-coach 與 my-site 各自消費；查得到的數據層可自動繼承，rules 的 # JUDGMENT 判斷值仍人工填。swim-coach 自動繼承 canonical stages 屬另案，不綁本 tracker。
- [ ] **Step 9 code-audit**：Phase 1+2+3 程式與資料改動的品質審查（push 前必跑）。

### Vortex 主題層模組化（散文→探索器）

進度（canonical-first：結構先進 canonical/，再經 my-site `sync_vortex.py` 只帶 public）：

- [x] **Phase A/A'/B/C**：教學誤區 / 技術分析 / L 指標矩陣 / Drills how_to → 已上線（見「當前狀態」）
- [x] **Phase D 水感層級**：4 式水感框架 → `canonical/technica/water-sense-levels.yaml`（26 levels，公開層三型 0 leaks）+ sync。⚠ my-site 呈現頁當時未實際建出（誤記，見上方訂正）；my-site `vortex-levels.html` 於 2026-06-11 才真正上線（rail+ladder 設計，首頁第四塊入口）。
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

*最後更新：2026-06-16（Phase 2 完成：心理層 8 主題 62 概念全接入 Vortex 網站——三帶「心理地圖」著陸頁〔沿 L0→L6／初學→競技脊椎，8 主題全 complete〕+ 首頁入口。canonical/psychology/ 8 theme/62 concept〔fear 手寫 pilot + 7 主題 7 並行 Sonnet agent 寫、ruamel merge〕，每條過三關校正、public/diagnostic 0 洩漏，各 agent 沒過清單已記。my-site CI success）*
*下次更新時機：my-site 週期化知識整合（B）動工後*
