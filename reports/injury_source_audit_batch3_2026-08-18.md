# 傷害條目來源稽核 — 第 3 批（2026-08-18）

前兩批見 `injury_source_audit_2026-08-17.md`、`injury_source_audit_batch2_2026-08-17.md`。

本批處理第一批盤點出的最後 13 個 source_id，34 個目標全部走完。

**稽核問題不是「這個數字有沒有誇大」，而是「這個數字是不是來源真的報出來的那個數字」。**

---

## 一、結果總表

| source_id | 處置 | 認定 |
|---|---|---|
| `src.cdc-mmwr-2003-2007` | 升級 verified | CDC (2011) MMWR 60(19):605-9, PMID 21597452 |
| `src.ecg-scd-3-6-0-4-10-89-url` | 升級 verified | Corrado D et al. (2006) JAMA 296(13):1593-601, PMID 17018804 |
| `src.neurobehavioral-consequences-of-repetitive-h` | 升級 verified | Helmich I et al. (2024) J Sci Med Sport 27(1):16-19, PMID 37923648 |
| `src.quebec-44-year-diving-sci-study-sciencedirec` | 升級 verified | Barss P et al. (2008) Accid Anal Prev 40(2):787-97, PMID 18329434 |
| `src.mdi-management-review-annals-of-joint` | 升級 verified | Bishop ME et al. (2022) Ann Joint 7:10, PMID 38529164 |
| `src.red-s-clinical-assessment-tool-framework-ioc` | 升級 verified | Mountjoy M et al. (2015) BJSM 49(21):1354, PMID 26764434（CAT **v1**） |
| `src.ioc-red-s-2014-2018-2023-doi` | 升級 verified | Mountjoy M et al. (2023) BJSM 57(17):1073-1097, PMID 37752011 |
| `src.who-2024-12-13-drowning-deaths-decline-globa-2024` | 升級 verified | WHO 2024-12-13 新聞稿 |
| `src.female-athlete-triad-in-swimmers-systematic` | 升級 verified | Buchanan BK et al. (2025) JWSM 5(1):30-38, doi:10.53646/ahq2qs39 |
| `src.stress-fractures-in-swimmers-systematic-revi` | 升級 verified | Vasiliadis AV et al. (2018) IJKSS 6(3):25-31 |
| `src.pmc10372189` | 重寫（吸收重複 id） | Belilos E et al. (2023) Clin J Sport Med 33(4):428-434, PMID 36715985 |
| `src.mountjoy-ioc-consensus-webfetch` | **解除**（重複） | 與 `src.ioc-red-s-2014-2018-2023-doi` 同一份 |
| `src.aiac-ijkss-v-6n-1p-25` | **解除**（重複） | 與 `src.stress-fractures-in-swimmers-systematic-revi` 同一份 |
| `src.belilos-2023-hs-swimming-injury-epi` | **刪除**（我自己第 2 批誤建） | 與 `src.pmc10372189` 同一份 |
| `src.swimming-injury-imaging-review-1-radiologyke` | **解除**（不可引用） | radiologykey.com 為教科書章節未授權轉載 |
| `src.ioc-iron-in-sport-doi-webfetch` | **解除**（查無此文獻） | IOC 從未發表以鐵為主題的共識聲明 |
| `src.trikha-2022-collegiate-swimmer-health-events` | **新增** | Trikha R et al. (2022) OJSM 10(4), PMID 35400141 |

---

## 二、本批新增的四種錯誤型態

前兩批已記錄：灌水、反轉、低報、標準張冠李戴、來源—主張不匹配、型別錯誤（把「沒有來源」這件事登錄成 source_id）。本批新增四種：

### 1. 引用不存在的權威（`iron-deficiency-swimmer`）

原文掛「IOC 共識聲明 — Iron in sport」。**IOC 從未發表過以鐵為主題的共識聲明。**

處置是解除，不是換一篇近似的（該條目已另引 Sim 2019）。解除後條目一個字都沒少——**只是拿掉了「有 IOC 背書」的假象**。連帶效果是該條目的 11–41%、50%、20→40 mg 三個數字現在只剩一份敘事綜述可掛，全部降為待查。

### 2. 歸屬顛倒（`drowning`）

原文：「WHO 2024：2021 全球溺水死亡約 274,200 人（另估 ~30 萬，方法不同）」。

**方向反了。30 萬才是 WHO 自己報的數字，274,200 是 GBD／IHME 系列估計。** 原寫法把 WHO 的數字降級成「另估」，掛在 WHO 來源下的反而是別人的數字。這種錯誤不改變數量級，純機器檢查抓不到——source_id 存在、URL 可驗、數字也真的存在於文獻中，只是屬於另一個機構。

### 3. 重複登錄（本批抓到三組）

同一篇文獻登錄兩個 id：Mountjoy IOC 共識 ×2、Vasiliadis 應力性骨折回顧 ×2、Belilos 高中傷害監測 ×2（第三組是我自己在第 2 批誤建的，已刪除並在存活 id 的 notes 記下更正）。

危害在來源反向索引：**一份文獻會顯示成兩份獨立支撐。** 這在「有幾份研究支持這個說法」的判讀上直接誤導。

### 4. 族群張冠李戴（`starting-block-impact`）

Helmich 2024 的 Para 泳者個案被寫成「視障選手」，實際是**肢體缺損（limb deficiency）**組別，而且是 **n=1 個案報告**。原條目據此在 `population_notes.ability.para` 寫「視障 Para 選手腦震盪累積風險，需特別監測」——族群錯、樣本量被隱去、個案被寫成族群風險，三重放大。

---

## 三、被移出流行率欄的無來源數字

這些數字原本掛在真實來源之下，但**該來源的摘要並未報出它們**。已移出流行率欄，改列 `flags.pending_verification`：

| 數字 | 原掛來源 | 認定 |
|---|---|---|
| 「腦震盪為最常見游泳/跳水傷型（31.7%）」 | Belilos 2023 | 摘要未報腦震盪佔比 |
| 「女性佔 MDI 患者約 35.7%」 | Bishop 2022 | 該文為敘事型回顧、無統合統計，摘要無此數 |
| 「喙肱距每增 1 mm 風險上升約 20%」 | Bishop 2022 | 同上 |
| 「游泳族群約 41% 有三聯症風險」 | Buchanan 2025 | 摘要對不上；可對上的是低能量可及性 51%、低骨密度 12% |
| 「踝部佔游泳整體傷害約 1%」 | radiologykey | 來源已解除，數字成孤兒 |
| 「游泳者外耳道炎風險為非游泳者約 5 倍」 | CDC MMWR | 該來源分母是全美總人口，撐不起此倍數 |
| 「肘佔比低」 | Belilos 2023 / Wolf 2009 | 兩份監測研究都未單列肘部，屬推論非數據 |

---

## 四、期間與版本標錯

- **`swimmers-ear`**：「2003–2007 年年門診約 240 萬次」讀起來像五年平均，實際 240 萬／每千人 8.1 是 **2007 年單一年度**數值。
- **`red-s`**：IOC 共識 2014／2018／2023 三版結論不同，一個 id 綁三版等於數字無法追回版本。已註記須標版本。
- **`female-athlete-triad`**：RED-S CAT 有 v1（2015）與 CAT2（2023）兩代，引用須指明。

---

## 五、驗證器狀態

```
0 ERROR, 697 WARN
W008（孤兒來源）18 筆 — 含本批解除的 4 個 id
```

**W008 上升是正確結果，不是退步。** 孤兒來源代表「這份登錄不再有任何條目依賴它」——把查無實據的引用解除之後本來就會多出孤兒。反過來把它們硬升級成 verified 才會讓警告消失，那是造假。

---

## 六、34/34 完成後的殘留

- `flags.pending_verification` 全庫約 50 條未處理
- 48 份 drafts 中仍有 `references: verified: false` 條目
- 本批移出的 7 個數字需要各自回到原始文獻找出處，找不到就永久標為文獻空白
- 三份 🟠 條目（MDI、踝足、應力性骨折）的流行率欄現在誠實地寫著「無精確數字」——這是正確狀態，不是待補的洞
