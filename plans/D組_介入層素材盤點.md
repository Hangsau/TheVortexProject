# (D) 組：介入層素材盤點

盤點日期：2026-09-03
方法：沿用 (C) 組做法——**讀素材本身，不讀中繼資料**。不從「interventions 只有 5 筆、actions 有 31 個」推論「還有 29 個能寫」。

---

## 0. 現況

`canonical/movement/interventions.yaml` 共 **5 筆**，覆蓋 **31 個動作中的 2 個**：

| 動作 | 既有介入 |
|---|---|
| `shoulder-complex.elevation` | `.active-control`（主動控制不足）、`.conditional-soft-tissue`（被動軟組織限制） |
| `ankle-foot.plantarflexion` | `.conditional-mobility`（被動受限）、`.capacity-control`（主動控制不足） |
| （無動作連結） | `.breaststroke-breathing.arm-driven-torso-lift`（`action_ids: []`） |

每個被覆蓋的動作都是「被動受限 / 主動控制不足」一組兩筆的分流結構。

## 1. 素材在哪裡

全 canonical 掃 12 個限制類關鍵詞（活動度／伸展／緊縮／ROM／柔韌／受限／硬體邊界／代償／肌力訓練／容量訓練／過度活動／hypermobility）後：

- **主素材**：`instructional/technical-analysis.yaml` — 硬體邊界 9、柔韌 44、活動度 35、受限 20、代償 18。該檔有原生的 `category: hardware` 分類，共 **16 個點**，這就是介入層的原生素材集。
- 次素材：`health/injuries.yaml`、`instructional/teaching-errors.yaml`、`periodization/dryland.yaml`、`technica/water-sense-levels.yaml`
- **假陽性已排除**：`movement/stroke-demands.yaml` 262 次命中、`movement/actions.yaml` 99 次命中，幾乎全是「伸展」作為解剖動作名（extension），不是介入語意。

## 2. 逐點裁決

門檻取自既有 5 筆的實際寫法，不是取自 schema 註解。關鍵發現：**`dosage_source_ids: []` 是允許的**（`.conditional-soft-tissue`、兩筆 ankle 皆為空）。所以門檻不是「要有劑量來源」，而是：**能不能寫出可分流的 `limitation_type` + `works_when` / `fails_when` + `how_to_identify` + `action` 進退階 + `mobility_decision`**。

### 2.1 可寫成新介入（3 筆）

| # | 動作 | 素材 | 為什麼過得了門檻 |
|---|---|---|---|
| D1 | `shoulder-complex.scapular-upward-rotation` + `.scapular-protraction` | free.tech.10、fly.tech.27 | `limitation_type` 明確且**反直覺**：前鋸肌是耐力不足不是力量不足。Pink 1991／1993 兩份 EMG 直接證據——全划手週期只有前鋸肌與肩胛下肌持續高激活，其餘分段休息。`fails_when` 有現成分流：把它當力量項目練就是練錯方向。代償鏈完整（菱形肌代償→肩胛 winging→肩胛下肌代償→內部撞擊），可作 `how_to_identify`。 |
| D2 | `trunk.axial-rotation` | free.tech.33、back.tech.24、fly.tech.27 | 唯一**有真實劑量來源**的候選：Karpiński 2020 是 6 週、每週 2–3 次的 RCT（轉身後 5m −0.1 秒、50m −0.3 秒）。free.tech.33 已經寫好三分支決策樹（陸上左右不對稱／陸上對稱但高划頻才失同步／伴隨疼痛）。back.tech.24 提供水中疲勞觸發訊號（第一指標是髖旋轉增加，不是肩旋轉縮小，Psycharakis 2010）。 |
| ~~D3~~ | ~~`trunk.extension`~~ | ~~breast.tech.16、breast.tech.19、fly.tech.26~~ | **已撤回，見 §2.4。** |

### 2.4 撤回：D3 軀幹伸展風格分流

**錯誤 6：§2.1 初版把 D3 列為可寫，是只查了「哪些需求用 `trunk.extension`」而沒查「哪些是蛙式」。**

實查：8 筆蛙式需求（leg-insweep、glide、arm-recovery、arm-insweep、arm-outsweep、arm-catch、leg-recovery、foot-flip）**沒有任何一筆使用 `trunk.extension`**。使用 `trunk.extension` 的 7 筆分屬 udk、starts-turns、fly。而既有 5 筆介入**全部**靠 `demand_ids` 連回需求層（第 5 筆 `action_ids` 可以是空的，`demand_ids` 不曾是空的）——`demand_ids` 才是這一層的承重連結。

把蛙式風格分流的介入掛到 udk 或起跳轉身的軀幹伸展需求上，是假連結。

第二個獨立理由：D3 的 `action` 欄位會變成「改採較平的路徑」，那是**技術路徑選擇不是訓練步驟**。這個檔案的定位是「依限制型態整理訓練、活動度／伸展、進退階、劑量來源、水中重測與安全停止條件」，風格選擇不在其中。

breast.tech.16 的三分支決策樹留在 `technical-analysis.yaml` 原處即可，沒有損失。

### 2.2 補既有記錄（不新增，2 筆小改）

**`ankle-plantarflexion` 兩筆的 `how_to_identify` 缺一個水中觸發訊號。** udk.tech.15 有：踝蹠屈受限→加大膝彎曲代償→膝彎曲本身是主要正面阻力來源→速度反而下降；可觀察門檻 >40°（src.pmc9402090-a）。既有記錄的 `how_to_identify` 全是陸上量測加泛泛的水中重測，沒有點名這個代償型態。

寫法必須是**觸發訊號不是判定**：「水中觀察到上踢相膝過度彎曲，作為進入本分流的觸發，不作為蹠屈受限的判定」——否則違反 free.tech.38／breast.tech.36 的「不得由水中外觀反推關節歸屬」。

### 2.3 判定不寫（附理由）

| 素材 | 為什麼不寫 |
|---|---|
| free.tech.13、back.tech.16、breast.tech.14、fly.tech.24、udk.tech.14、udk.tech.16、udk.tech.28（踝蹠屈，7 點） | 素材集中度極高——16 個 hardware 點有 7 點在講同一個動作，而該動作**已有兩筆介入**，且既有記錄的保守度高於這些素材。 |
| udk.tech.28（單獨標記） | ⚠ **與既有記錄直接衝突**。udk.tech.28 宣稱「柔韌性訓練可改善蹠屈範圍，進而提升 UDK 表現」（src.pmid-24984154）；但 `.conditional-mobility` 的 `remaining_boundary` 明寫「沒有能支撐本處方的長期伸展介入試驗；既有急性伸展操作不是訓練試驗」。而 pmid-24984154 在 udk.tech.14 被引用時是**限制活動度 30%→速度降 19%** 的反向限制實驗——限制實驗支持「關聯」，不支持「拉鬆會變快」。**不把 udk.tech.28 的宣稱推進介入層；反而是 udk.tech.28 的措辭該修。**（列入待處理，本批不動） |
| breast.tech.15（髖內旋） | ❌ **詞彙表缺口**：31 個動作裡沒有 `hip.internal-rotation`（有 `hip.abduction`、`hip.external-rotation`，沒有內旋也沒有內收）。沒有動作就掛不上 `action_ids`。且證據只到 🟠 教練觀測，「每增加一度 +5% 推進力」原文自己註明非學術控制數字。taxonomy 改動，不夾在內容批次裡。 |
| starts-turns.tech.3、starts-turns.tech.40（膝角度） | 這兩點的結論是「無跨選手通用最優值」——這是**反處方，不是限制型態**。`limitation_type` 欄位填不出東西。留在 technical-analysis 是對的位置。 |
| free.tech.38、free.tech.39、free.tech.40、breast.tech.36、breast.tech.37、starts-turns.tech.48（joint 類 6 點） | 六點全部明文寫「本條不對介入方式下結論」。它們是**評估分層前提**（踝要分距小腿／距下／橫跗；頸要分上下段；肩要分盂肱／肩胛胸廓），不是介入。硬塞進 interventions.yaml 就是 (C) 組錯誤 5 的反向版——把不屬於這層的素材填進來充數。 |
| fly.tech.25（肩活動度） | 🔵 推導，**無 source_ids、無 evidence 區塊**。且 `shoulder-complex.elevation` 已有兩筆介入涵蓋被動／主動分流，這點加不了新分支。 |

## 3. 誠實的產出量

**2 筆新記錄 + 2 筆小改 + 1 個 taxonomy 決定，不是 29 筆。**

介入層 5 → 7 筆，覆蓋動作 2 → 5 個（`scapular-upward-rotation`、`scapular-protraction`、`trunk.axial-rotation` 加入）。剩下 26 個動作沒有介入，不是待辦缺口，是**庫內沒有符合門檻的素材**——大部分動作的既有素材停在「這個相位用到這個關節」的列舉層，沒有到「這個關節受限時怎麼分流、怎麼介入」。

這與專案 CLAUDE.md 的「硬體邊界 vs 感知缺陷」判斷一致：真正被研究到可介入程度的硬體邊界，就是踝蹠屈、肩上舉、前鋸肌、核心旋轉這幾個，其餘是空白而非遺漏。

## 4. 派工

| 批次 | 內容 | 方式 |
|---|---|---|
| W15 | D1 前鋸肌耐力介入（新記錄 1 筆） | codex 發包 |
| W16 | D2 跨側核心容量介入（新記錄 1 筆） | codex 發包 |
| — | 2.2 的 ankle 兩筆 `how_to_identify` 補句 | 手改（微 diff，不發包） |
| — | `hip.internal-rotation` 詞彙缺口、udk.tech.28 措辭衝突 | 寫入 HANDOFF 待處理，不在本批 |

W15 驗收通過並 commit 後才派 W16（串行，沿用 W13→W14 紀律）。
