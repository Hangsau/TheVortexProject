# 傷害條目來源健檢 — 第 2 批：佔位字串（2026-08-17）

## 這批在查什麼

第 1 批查的是「引用寫得像文獻、但文獻不存在」（akkurt / bushman）。
第 2 批的目標更直白：**8 個 source_id 的顯示字串本身就寫著「待查」「待補 PMID」「待 WebFetch 核實」**
——它們從一開始就不是引用，是佔位符。問題不在於它們沒被驗證，而在於**有多少數字正掛在這些空引用下**。

第 1 批報告寫下的預期處置是「保持 unverified、解除引用、檢查依附其上的數字是否也要撤除」。
實際做下來，處置比預期好一級：**其中幾個佔位符背後是有真文獻的，只是從來沒人去找**。
所以本批的動作不是「撤數字」，而是「查到真文獻 → 對照 → 發現數字錯了 → 改成對的」。

## 已完成（3 個佔位符解除，7 個真來源新增）

### 1. `poolside-slip-fall` — 兩處錯誤，一處是數字灌水，一處是張冠李戴

**錯誤 A：髖骨折一年死亡率 20–30%**

原引用 `src.falls-and-hip-fracture-mortality-pmid`，顯示字串是
「Falls and hip fracture mortality, 一般骨科文獻（待補具體 PMID）」——括號裡就寫著沒有 PMID。

查真實文獻後，這個數字**對本專案的讀者族群偏高約 1.5–2 倍**：

| 來源 | 族群 | 一年死亡率 |
|---|---|---|
| Wang 2013, Bone（PMID 23727435） | 台灣健保資料庫，≥60 歲，n=143,595 | 年死亡率 1999 年 **18.10%** → 2009 年 **13.98%** |
| Lee 2017, Aging Dis（PMID 28840055） | 台灣髖骨折**術後**，n=5,442，平均 78.8 歲 | 整體 **16.8%** |
| Harvey 2024, Arch Gerontol Geriatr（PMID 38941947） | 亞太區系統回顧，142 研究 / 1,139,752 人 | 新加坡 **10.8%** ～ 紐西蘭 **23.8%** |

Harvey 2024 的核心結論就是「亞太區內差異極大，亞洲短期死亡率低至澳紐的四分之一，一年期仍約為一半」。
20–30% 大致落在澳紐等西方族群的上緣。對一個服務台灣讀者的專案，直接套用會誇大風險。

已改寫為分地區、附樣本數的敘述；`prognosis` 由「一年死亡率 20–30%」改為
「台灣資料約 14–17%……西方族群報告可達 23% 上下，地區差異大，引用時須連地區一起說」。

**錯誤 B：「乾混凝土靜摩擦約 0.6（ASTM 建議濕地最低標）」**

這句話把兩件事同時弄錯：

- **ASTM F2508 不是門檻標準**。它的全名是 *Standard Practice for Validation of Walkway Tribometry
  Using Research-based Reference Materials*（前版為 Validation, Calibration, and Certification of
  Walkway Tribometers Using Reference Surfaces）——規範的是**摩擦計本身如何校驗**。
  ASTM 從未發布走道最低摩擦係數。
- **0.60 / 0.40 這組數字出自 ANSI/NFSI B101.1**，而且全部是**濕態**靜摩擦係數（wet SCOF）分級：
  ≥ 0.60 高抓地力 / 0.40–0.60 中等 / < 0.40 低抓地力。拿來描述「乾混凝土」是語意錯置。

有意思的是，原句的**結構**是對的（泳池濕區落在低抓地力區間），錯的只有歸屬與乾濕語意。
這正是第 1 批總結的錯誤型態：讀起來精確、帶著引用、符合常識。

`src.astm-f2508` 已升 verified 但注記「本來源不含任何門檻值」，
另新增 `src.ansi-nfsi-b101-1` 承接分級門檻。
NFSI 自述的「wet SCOF ≥ 0.60 可使滑倒索賠減少達 90%」屬機構宣稱非同儕審查，本專案不引用。

另撤除 mechanism 中「部分量測濕磁磚低至 0.3」——查不到具體量測來源。

### 2. `sipe` — 兩個 source_id 都是佔位符，但真文獻其實很充分

原 `source_ids: [src.sipe, src.military-swim-training-sipe]`，顯示字串分別是
「SIPE 病理生理與鐵人三項案例系列（作者/年份待查）」與「軍事泳訓 SIPE 研究（具體文獻待 WebFetch 核實）」。
`prevalence` 欄位當時只寫「報導發生率範圍待 WebFetch 核實」。

這條寫得誠實（它自己承認沒查），所以本批不是修錯，是把空欄位填上：

| 新來源 | 關鍵數據 |
|---|---|
| Spencer 2018, Sports Med Open（PMID 30238206）系統回顧 | **僅 9 篇納入、異質性過高無法量化統合**；各研究 0.01%（英國鐵人賽）～ 26.7%（以色列海上軍訓）；約 30% 復發 |
| Hårdstedt 2021, Chest（PMID 34186036） | 瑞典 47,573 人次，**0.44%**；**女 0.75% vs 男 0.09%（OR 8.59）**；18–30 歲 0.08% → ≥61 歲 1.1%（OR 12.74） |
| Volk 2021, Chest（PMID 33245874） | 美國海軍 SEAL 儲訓生 2,117 人，**5.0%** |

三個發現值得單獨記下：

1. **不存在「SIPE 發生率是 X%」這種說法。** 0.44%（一般賽事）與 5.0%（軍事儲訓）相差逾十倍，
   系統回顧納入的研究彼此差距近三個數量級。條目已改為並列族群，不給單一數字。
2. **女性風險是主效應不是附註。** 原稿把它寫成「部分研究指出（待核實）」grade C；
   實測 OR 8.59、患者中 90% 為女性（參賽性別比接近 1:1），已升為 grade B 並拆成獨立風險因子。
3. **Spencer 2018 明確寫出「找不到任何報告 SIPE 死亡的研究」。**
   本條標 `fatal_acute: true` 仍然保留——但 caveat 現在寫明那是基於機制上的致命潛勢與急症處置需求，
   **不是基於已發表的死亡率數據**。這兩者混用會讓標記看起來有它沒有的證據基礎。

另撤除 prevention 的西地那非建議：Spencer 2018 指該用法只有兩篇極小型無對照研究、結論不確定，
且用藥決定超出教練角色（與第 1 批 OC 條目的撤除理由同一類）。

### 3. `groin-adductor-strain` — 本批唯一完全乾淨的條目

`src.grote-2004`（PMID 14754731）已是 verified，取回摘要逐字比對，
條目中六個統計數字**全部相符**：296 名泳者；當前腹股溝痛蛙泳 6.92% vs 個人混合式 0%（P=0.015）；
過去一年因傷無法完成蛙泳訓練 42.7% vs 個人混合式 21.5%（P=0.000622）vs 非蛙泳非混合 5.8%（P=0.00000311）。
**無需更正**——這是本輪健檢第一個。同條的另一個 source_id
`src.adductor-loading-return-to-sport-practice-co` 仍是佔位符，但它沒有支撐任何數字（數字全在 Grote 名下）。

## 驗證狀態

`python tools/validate.py` → **0 ERROR**（W008 4 → 7、W011 維持 64）。

W008 由 6 增至 7 是正確結果：`src.falls-and-hip-fracture-mortality-pmid`、`src.sipe`、
`src.military-swim-training-sipe` 解除引用後成為孤兒。與第 1 批同一原則——
不會為了消掉 WARN 去補假引用，也不會為了避免孤兒而把佔位符留在條目上。

## 本批尚未處理

- `src.jellyfish-envenomation-first-aid`（`open-water-marine-biological-hazards`，🟡，
  含壞死性筋膜炎死亡率 >20%、台灣為創傷弧菌／鉤端螺旋體流行區等宣稱）
- `src.breath-hold-training` + `src.shallow-water-blackout-prevention-webfetch`
  （`shallow-water-blackout`，🟠，無硬數字，暴險低）
- `src.clinical-coach-report-no-epidemiology`（`swimmer-elbow-wrist-overuse`，🔵，無硬數字，暴險低）
- `src.adductor-loading-return-to-sport-practice-co`（數字已由 Grote 2004 承擔，只需解除引用）

以及第 1 批列出的另兩類共 14 個：可查但非 PubMed（8）、標題可查需回推書目（6）。
