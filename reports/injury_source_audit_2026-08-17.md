# 傷害條目來源健檢 — 第 1 批（2026-08-17）

## 為什麼做這件事

C 類傷害宣稱裁決（`plans/關節主張裁決_C類傷害宣稱.md`）只碰了 `breaststrokers-knee` 與
`swimmers-shoulder` 兩個條目，就抓出三處與一手文獻方向相反的錯誤。那批的教訓是：
**錯誤型態是「反轉」而不是「誇大」**——句子讀起來精確、帶著引用、又符合常識，所以只有逐字比對一手摘要才抓得到。

既然兩個條目就有三處，`canonical/health/drafts/` 剩下的 45 個沒理由乾淨。本批把範圍從「內容」換成「來源」：

- 全庫 48 個 draft 共 **50 筆 `pending_verification`**、**15 筆 `references` 標 `verified: false`**
- 但更有槓桿的訊號是：**傷害條目引用的 95 個 `source_ids` 當中，34 個的 `verification_status` 不是 verified**
  ——這些是正在被當機器鍵使用、卻沒人確認過存在的引用

本批處理其中最容易判定的 12 個（6 個 StatPearls 章節 + 6 個具名作者期刊文獻）。

## 檢索方法

- **期刊文獻**：NCBI E-utilities `esearch.fcgi` → `esummary.fcgi` → 必要時 `efetch.fcgi`（`rettype=abstract`）
  取完整書目與摘要原文。（PubMed 網頁版被 cookie 通知擋住，WebFetch 不可用。）
- **StatPearls / NCBI Bookshelf**：直接取 `ncbi.nlm.nih.gov/books/<NBK>/` 頁面，
  讀 `<title>` 與 `citation_date` / `citation_authors` meta 標籤。
- **判定原則**：期刊、年份、主題、文獻類型四項須同時相符才認定為同一篇。
  只要有一項不符，一律記為「無法定位」，**不以近似文獻頂替**。

## 結果總表

| # | source_id | 判定 | 說明 |
|---|-----------|------|------|
| 1 | `src.multidirectional-instability-of-the-shoulder` | ✅ 升 verified | NBK557726，標題應為 Multidirectional Shoulder Instability（原記語序有誤） |
| 2 | `src.osgood-schlatter-disease-statpearls-nbk44199` | ✅ 升 verified | NBK441995（id slug 尾碼被截，以 identifier 為準） |
| 3 | `src.salter-harris-fractures-statpearls-nbk430688` | ✅ 升 verified | NBK430688，官方章名為**單數** Salter-Harris Fracture |
| 4 | `src.scheuermann-disease-statpearls-nbk499966` | ✅ 升 verified | NBK499966，標題相符 |
| 5 | `src.sever-s-disease-calcaneal-apophysitis-statpe` | ✅ 升 verified | NBK441928，官方章名不帶所有格 's |
| 6 | `src.statpearls-swimmer-s-shoulder-ncbi-bookshelf` | ✅ 升 verified | NBK470589；**全篇只處理自由式**的使用邊界已寫入 notes |
| 7 | `src.brannigan-et-al-hypothermia-mass-participati-2009` | ✅ 升 verified | PMID 19364182，作者年份期刊標題全符，僅缺識別碼 |
| 8 | `src.tipton-mj-et-al-cold-water-immersion-sudden-2003` | ⚠️ 更正後 verified | PMID 14698111。**單一作者 Tipton M，原記的「et al.」共同作者不存在**；且為 Lancet supplement 兩頁短文，非原始研究 |
| 9 | `src.sim-2019` | ⚠️ 更正後 verified | PMID 31055680。是 **narrative review**，且標題主題為運動員鐵營養全面綜述，hepcidin 僅其中一節 |
| 10 | `src.elliott-sale-2020` | ⚠️ 更正後 verified | PMID 32666247。**期刊記錯**：實為 Sports Med，非 Br J Sports Med |
| 11 | `src.akkurt-2017` | ❌ 查無此文獻 | 見下 |
| 12 | `src.bushman-2006` | ❌ 查無此文獻 | 見下 |

## 兩筆無法定位的引用

### `src.akkurt-2017`
原記「Akkurt et al. 2017, J Phys Ther Sci（SCI 髖屈攣縮綜述）」。
`Akkurt[au] AND 2017[dp] AND "J Phys Ther Sci"[ta]` → **0 筆**。
放寬後 2017 年唯一相符者是 **Akkurt H 等，Eur J Phys Rehabil Med，「上肢有氧運動 RCT」（PMID 27824234）**
——期刊、主題、文獻類型三項皆不符。

**連帶處置**：`sci-hip-flexor-contracture` 的「嚴重攣縮（≥ 60°）報告比例 30–50%」是掛在這個引用下的唯一數字，
一併撤除；`certainty` 由 🟠 改 🔵（撤掉數字後剩下的是解剖推導，本專案並無 SCI 泳者觀察案例，
標 🟠 會暗示一個不存在的觀察基礎）。

### `src.bushman-2006`
原記「Bushman et al. 2006, Phys Sportsmed（早期 OC × VO₂max 量化）」。
`Bushman[au] AND "Phys Sportsmed"[ta]` → **0 筆**；`Bushman[au] AND (VO2 OR "aerobic capacity")` 亦無相符。
唯一真實的 Bushman × 口服避孕藥文獻是 J Sports Med Phys Fitness 2006 的**無氧功率**研究（PMID 16596112）
——期刊與測量指標皆不符。

## 本批最嚴重的發現：`oral-contraceptives-performance` 整條與其證據衝突

追查 `src.bushman-2006` 時發現 VO₂max 數字的真正出處應是
**Lebrun CM 等（2003），Br J Sports Med 37(4):315–320，PMID 12893716**
（已新增為 `src.lebrun-2003-triphasic-oc-vo2max`）。取得摘要原文後，對照出四處錯誤：

| 舊稿寫法 | 一手文獻實際內容 | 判定 |
|---|---|---|
| VO₂max 降 **10–11%**（範圍 6–15%） | OC 組降 **4.7%**，安慰劑組 +1.5%，**n = 14** | **數字灌水約 2.3 倍** |
| 「400m 以上耐力項目**受影響顯著**」 | 同研究直接測有氧耐力（90% VO₂max 力竭時間）**無顯著變化**；無氧速度、等速肌力、最大通氣量、心率、血比容亦全無差異 | **與自己的證據相反** |
| 「三相型 > 單相型 > 低劑量」劑量-反應排序，標 grade B | Lebrun 只測了三相型**一種**配方，無跨配方對照；Elliott-Sale 2020 指納入研究配方混雜、異質性高 | **未建立的排序** |
| prevention：「對耐力選手優先選擇低劑量單相型或非荷爾蒙避孕」 | Elliott-Sale 2020（42 篇 / 590 人）結論：群體效果**極可能 trivial**，**現有證據不足以支持通則性建議**，應個別化 | **建議與其來源直接牴觸，且超出教練角色** |

另撤除兩處無來源數字：使用率「30–50%」（兩個掛名來源都不產出使用率資料）、
prognosis「停用後 2–3 個月 VO₂max 回升」（Lebrun 是單向設計，無停藥後追蹤）。

**「6–15%」這個範圍的可能來源**：Lebrun 文中提到兩名受試者下降「4 與 9 **ml/kg/min**」
——那是絕對值不是百分比。舊稿疑似把絕對值誤讀成百分比再擴成區間。

## 數字使用紀律（已寫入 `_sources.yaml` notes，改寫者必讀）

- 引用 **4.7%** 時必須同句寫出 **n = 14**
- 引用 4.7% 時必須併陳同研究的**陰性結果**（耐力、無氧、肌力皆無差異），
  否則會複製出「OC 傷耐力」這個原本就是錯的結論
- Elliott-Sale 2020 只能用來談**表現影響**，不能用來談**使用率**
- Sim 2019 是敘事綜述，引用時寫「綜述指出」不寫「研究發現」
- Tipton 2003 是單一作者兩頁短文，不寫「Tipton 等人的研究發現」

## 驗證狀態

`python tools/validate.py` → **0 ERROR**（W008 4 → 6、W011 維持 64）。

W008 增加 2 是**正確的結果**：`src.akkurt-2017` 與 `src.bushman-2006` 解除引用後成為孤兒來源。
「查無此文獻」的引用本來就該是孤兒；不會為了消掉這兩個 WARN 去補假引用，
也不會為了避免孤兒而把假引用留在條目上。

## 剩餘範圍（第 2 批以後）

34 個未驗證來源中，本批處理 12 個，剩 22 個分三類：

- **可查但非 PubMed**：`src.astm-f2508`（工程標準）、`src.cdc-mmwr-2003-2007`、
  `src.who-2024-12-13-drowning-deaths-decline-globa-2024`、`src.ioc-red-s-2014-2018-2023-doi`、
  `src.ioc-iron-in-sport-doi-webfetch`、`src.mountjoy-ioc-consensus-webfetch`、
  `src.red-s-clinical-assessment-tool-framework-ioc`、`src.ecg-scd-3-6-0-4-10-89-url`
- **標題可查、需回推書目**：`src.female-athlete-triad-in-swimmers-systematic`、
  `src.mdi-management-review-annals-of-joint`、`src.multidirectional-instability-of-the-shoulder` 之外的
  `src.neurobehavioral-consequences-of-repetitive-h`、`src.quebec-44-year-diving-sci-study-sciencedirec`、
  `src.stress-fractures-in-swimmers-systematic-revi`、`src.swimming-injury-imaging-review-1-radiologyke`
- **佔位字串，預期無法定位**：`src.breath-hold-training`、`src.sipe`、
  `src.military-swim-training-sipe`、`src.jellyfish-envenomation-first-aid`、
  `src.falls-and-hip-fracture-mortality-pmid`、`src.shallow-water-blackout-prevention-webfetch`、
  `src.clinical-coach-report-no-epidemiology`、`src.adductor-loading-return-to-sport-practice-co`

第三類的處置預期與 akkurt / bushman 相同：保持 unverified、解除引用、
檢查依附其上的數字是否也要撤除。**重點不是把它們變 verified，而是找出還有多少數字是掛在空引用下的。**
