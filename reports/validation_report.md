# Vortex Canonical 驗證報告

> 生成日期：2026-09-05
> 驗證條目數：747，Drills ID 數：176

---

## E001 — 已知條目陣列鍵中發現缺 `id` 的元素

**ERROR，共 0 筆**

（無）

---

## E002 — `id` 全域重複（驗證範圍內）

**ERROR，共 0 筆**

（無）

---

## E003 — `links.*` 指向不存在的 ID

**ERROR，共 0 筆**

（無）

---

## E004 — `category`/`stroke`/`certainty`/`status` 出現不在 `_taxonomy.yaml` 的值

**ERROR，共 0 筆**

（無）

---

## E005 — `source_ids` 指向不存在的 `_sources.yaml` ID

**ERROR，共 0 筆**

（無）

---

## E006 — `cross_ref_ids` 內含無法解析的 ID

**ERROR，共 0 筆**

（無）

---

## E007 — `links.*_link_ids` 內含無法解析的 ID

**ERROR，共 0 筆**

（無）

---

## E008 — `category` 跨網域誤用：值合法但該值的 scope 不含本檔所屬網域

**ERROR，共 0 筆**

（無）

---

## E009 — 條目的 `category` 未宣告於該檔自己的 `categories` 區塊（my-site 查表落空 → 靜默渲染成空字串）

**ERROR，共 0 筆**

（無）

---

## E010 — 診斷層洩漏：既有與 movement 診斷型鍵名出現在 `public` 子樹內（`sync_vortex.py` 白名單會整包搬 public 上公開站）

**ERROR，共 0 筆**

（無）

---

## E011 — `evidence_from` 含無法解析的 ID（它是 W009 的豁免路徑，不驗證就變成零成本免罪符）

**ERROR，共 0 筆**

（無）

---

## E012 — movement 受控欄位值不在 `_taxonomy.yaml` 對應詞彙集合（原 W013，2026-09-02 升級：`publication_status` 等欄位拼錯會fail-open，`sync_vortex.py` 只擋 `draft`/`withheld` 字面值）

**ERROR，共 0 筆**

（無）

---

## E013 — `_sources.yaml` 的 `verification_status` 不是 `verified`／`unverified`／`retracted` 三值之一（拼錯會讓 retracted 墓碑靜默回到 W008 名單）

**ERROR，共 0 筆**

（無）

---

## E014 — `_sources.yaml` 把「教練觀測」這類觀察行為登錄成來源（fail-open：它會滿足 W011 的來源逃生口，讓「🟠 要交代觀察基礎」被一個內容就是「教練觀測」的登錄擋掉）

**ERROR，共 0 筆**

（無）

---

## E015 — `source_ids` 指向 `retracted` 墓碑（墓碑仍在 allowed 集合裡，E005 會放行，等於靜默引用一筆已判定不可引用的來源）

**ERROR，共 0 筆**

（無）

---

## W022 — `text` 的內容就是它自己的來源名稱（「Mason 1992」）——只宣告有這篇文獻，沒說它顯示了什麼；W021 抓不到（text 非空）

**WARN，共 15 筆**

  file=canonical\technica\l-indicators.yaml id='free.L2.kick' at=indicators[7].public.evidence[0] text 就是來源名稱 'McCullough 2009'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='free.L4.roll-coupling' at=indicators[11].public.evidence[0] text 就是來源名稱 'Gonjo 2020'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='free.L5.serratus' at=indicators[16].public.evidence[1] text 就是來源名稱 'StatPearls 2023'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='back.L2.up-kick' at=indicators[19].public.evidence[0] text 就是來源名稱 'Maglischo 2003'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='back.L3.pull' at=indicators[20].public.evidence[0] text 就是來源名稱 'Gonjo 2020'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='back.L4.roll-stability' at=indicators[22].public.evidence[0] text 就是來源名稱 'González-Ravé 2025'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='back.L5.roll-invariant' at=indicators[24].public.evidence[0] text 就是來源名稱 'Gonjo 2021'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='fly.L2.kick' at=indicators[28].public.evidence[0] text 就是來源名稱 'PMC 2018'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='fly.L3.undulation-integration' at=indicators[30].public.evidence[0] text 就是來源名稱 'Sanders 1995'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='fly.L4.outsweep' at=indicators[33].public.evidence[0] text 就是來源名稱 'Peyrebrune & Turner 2007'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='fly.L5.two-kick-differentiation' at=indicators[34].public.evidence[0] text 就是來源名稱 'Mason 1992'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='fly.L5.two-kick-differentiation' at=indicators[34].public.evidence[1] text 就是來源名稱 'Swim Like A Fish 2025'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='breast.L4.undulation' at=indicators[43].public.evidence[0] text 就是來源名稱 'Colman 1998'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='breast.L5.undulation-stability' at=indicators[45].public.evidence[0] text 就是來源名稱 'Nicol 2022'（只說了有這篇，沒說它顯示什麼）
  file=canonical\technica\l-indicators.yaml id='breast.L5.undulation-stability' at=indicators[45].public.evidence[1] text 就是來源名稱 'Tanaka 2024'（只說了有這篇，沒說它顯示什麼）

---

## W024 — 機器鍵（PMID／PMC／DOI／`src.*`）寫進讀者散文欄位（`text`／`caveat`／`population_note`…）——這些欄位原樣上線，讀者看到的是識別碼不是「作者 年份」

**WARN，共 51 筆**

  file=canonical\health\injuries.yaml field='caveat' PMID/PMC='PMID 31141446' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\health\injuries.yaml field='prevalence' PMID/PMC='PMC11424229' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\health\injuries.yaml field='caveat' PMID/PMC='PMID 27824234' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\health\injuries.yaml field='caveat' PMID/PMC='PMID 16596112' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\health\injuries.yaml field='caveat' source_id='src.pmc8147101' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\health\injuries.yaml field='caveat' source_id='src.pmc2858141' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 20490545' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1038/s41398-024-02933-9' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='population_note' PMID/PMC='PMC3261851' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC11723612' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 26878097' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1016/j.neulet.2017.02.033' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC11723612' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='population_note' PMID/PMC='PMC11723612' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 19131473' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC4263011' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 9140893' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 19224911' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 13658305' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 25181542' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 19059813' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC4495877' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3390/ijerph181910259' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3389/fpsyg.2020.01659' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 18769531' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 31578934' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1023/A:1014805132406,' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 18769531' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3389/fspor.2023.1236256,' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1177/17479541251400621' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 31578934' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1177/17479541231174806,' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3389/fpsyg.2026.1771962' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3389/fpsyg.2025.1574429,' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 38242101' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.3389/fpsyg.2025.1667429,' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 40110418' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 29910410' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID 29910410' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC7063062' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID: 17566428' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1007/s00426-025-02225-x' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID: 29691389' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC12433939' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID: 40426460' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID: 16368636' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMID: 7932942' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1080/17509840802287218' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1111/j.1469-8986.1994.tb01039.x' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' PMID/PMC='PMC10497761' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml
  file=canonical\psychology\psychology.yaml field='text' DOI='10.1260/174795407780367177' 寫進讀者散文——改成人可讀的「作者 年份」，識別碼留在 _sources.yaml

---

## W023 — `_sources.yaml` 的 `display` 是本專案自己的草稿路徑（`Research/心理/03_….md#凍結反應`）——引用自己的草稿當來源是自證，且這串會原樣印在讀者頁面的「來源」欄

**WARN，共 63 筆**

  source_id='src.research-psych-02-a' display='Research/心理/02_喚醒焦慮與壓力崩潰.md#Reinvestment專節' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-02-b' display='Research/心理/02_喚醒焦慮與壓力崩潰.md#核心理論' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-02-c' display='Research/心理/02_喚醒焦慮與壓力崩潰.md#游泳特異性' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-02-d' display='Research/心理/02_喚醒焦慮與壓力崩潰.md#與水感框架的連結' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-a' display='Research/心理/03_水中恐懼與學習者心理.md#FWAQ' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-b' display='Research/心理/03_水中恐懼與學習者心理.md#凍結反應' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-c' display='Research/心理/03_水中恐懼與學習者心理.md#呼吸介入' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-d' display='Research/心理/03_水中恐懼與學習者心理.md#感知遮蔽機制' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-e' display='Research/心理/03_水中恐懼與學習者心理.md#族群特異性' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-f' display='Research/心理/03_水中恐懼與學習者心理.md#潛水反射' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-03-g' display='Research/心理/03_水中恐懼與學習者心理.md#社會安全感' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-a' display='Research/心理/04_動機與自我決定.md#HMIEM' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-b' display='Research/心理/04_動機與自我決定.md#SDT應用' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-c' display='Research/心理/04_動機與自我決定.md#動機氣候' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-d' display='Research/心理/04_動機與自我決定.md#族群特異性' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-e' display='Research/心理/04_動機與自我決定.md#核心理論' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-f' display='Research/心理/04_動機與自我決定.md#游泳特異研究' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-g' display='Research/心理/04_動機與自我決定.md#精熟氣候實驗研究' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-h' display='Research/心理/04_動機與自我決定.md#連結' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-04-i' display='Research/心理/04_動機與自我決定.md#需求受阻' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-a' display='Research/心理/05_意象與心理演練.md#1-功能等價functional-equivalence' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-b' display='Research/心理/05_意象與心理演練.md#2-pettlep-意象模型' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-c' display='Research/心理/05_意象與心理演練.md#3-意象的功能分類paivio-1985--hall-et-al-1998' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-d' display='Research/心理/05_意象與心理演練.md#4-內部視角-vs-外部視角internal--external-imagery-perspective' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-e' display='Research/心理/05_意象與心理演練.md#5-運動意象與-feedforward-預測模型的關係' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-f' display='Research/心理/05_意象與心理演練.md#a-動覺意象能否預先建立或強化水感' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-g' display='Research/心理/05_意象與心理演練.md#c-動覺意象-vs-視覺意象的分離效應' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-05-h' display='Research/心理/05_意象與心理演練.md#視角與測量' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-a' display='Research/心理/06_自我對話與心理技能訓練.md#心理技能訓練套裝計畫' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-b' display='Research/心理/06_自我對話與心理技能訓練.md#指導型-vs-激勵型自我對話' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-c' display='Research/心理/06_自我對話與心理技能訓練.md#核心概念' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-d' display='Research/心理/06_自我對話與心理技能訓練.md#游泳特異研究-vs-跨運動外推' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-e' display='Research/心理/06_自我對話與心理技能訓練.md#自我對話的作用機制' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-f' display='Research/心理/06_自我對話與心理技能訓練.md#自我對話的時態框架過去現在未來' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-g' display='Research/心理/06_自我對話與心理技能訓練.md#與水感框架指令層次注意力焦點的連結' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-h' display='Research/心理/06_自我對話與心理技能訓練.md#賽前例行程序' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-06-i' display='Research/心理/06_自我對話與心理技能訓練.md#關鍵文獻清單' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-a' display='Research/心理/07_心流與最佳表現.md#1-csikszentmihalyi-心流九大維度' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-b' display='Research/心理/07_心流與最佳表現.md#2-挑戰-技能平衡challenge-skill-balance模型演化' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-c' display='Research/心理/07_心流與最佳表現.md#4-精英運動員心流研究jackson1995-1996' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-d' display='Research/心理/07_心流與最佳表現.md#5-swann-等人心流系統回顧2012' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-e' display='Research/心理/07_心流與最佳表現.md#6-flow-vs-clutch-statesswann-等人2017-2023' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-f' display='Research/心理/07_心流與最佳表現.md#7-理想表現狀態ips--the-zone' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-g' display='Research/心理/07_心流與最佳表現.md#8-心流-表現關係-meta-analysis' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-h' display='Research/心理/07_心流與最佳表現.md#9-心流的神經認知機制' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-i' display='Research/心理/07_心流與最佳表現.md#flow-reinvestment-軸線的水感應用' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-j' display='Research/心理/07_心流與最佳表現.md#flow-vs-reinvestment-對照' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-k' display='Research/心理/07_心流與最佳表現.md#reinvestment-理論masters-1992masters-maxwell-2008' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-l' display='Research/心理/07_心流與最佳表現.md#心流的發展軌跡flow-不是-l6-的專利推導' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-m' display='Research/心理/07_心流與最佳表現.md#游泳特異研究-vs-跨運動外推' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-07-n' display='Research/心理/07_心流與最佳表現.md#與水感框架-l5-l6-水我合一的連結' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-a' display='Research/心理/08_心理感知生理交互.md#1.1' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-b' display='Research/心理/08_心理感知生理交互.md#1.2' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-c' display='Research/心理/08_心理感知生理交互.md#1.3' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-d' display='Research/心理/08_心理感知生理交互.md#1.4' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-e' display='Research/心理/08_心理感知生理交互.md#1.6' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-f' display='Research/心理/08_心理感知生理交互.md#1.7' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-g' display='Research/心理/08_心理感知生理交互.md#1.8' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-h' display='Research/心理/08_心理感知生理交互.md#1.9' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-i' display='Research/心理/08_心理感知生理交互.md#4.1' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-j' display='Research/心理/08_心理感知生理交互.md#4.2' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-k' display='Research/心理/08_心理感知生理交互.md#5.1' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄
  source_id='src.research-psych-08-l' display='Research/心理/08_心理感知生理交互.md#5.2' 是本專案自己的草稿路徑——回草稿找它引的原始文獻再登錄

---

## W001 — `cross_ref` 內的疑似穩定 ID 未列入同層 `cross_ref_ids`

**WARN，共 0 筆**

（無）

---

## W002 — 區塊**有**來源顯示字串（`source`/`sources`）但缺 `source_ids`（機器鍵沒跟上顯示層）；S3a-2 起不看 `certainty`

**WARN，共 0 筆**

> **契約說明（S3a／S3a-2）**：`source`（單數字串）與 `sources`（複數清單）都是顯示層自由文字，下游 my-site 直接渲染，**不可改寫、改名或改成陣列**；可解析的來源鍵放同區塊的 `source_ids`，指向 `canonical/_sources.yaml` 的 `src.<slug>`。W002 自 S3a-2 起**與 `certainty` 解耦**：一個區塊只要帶了來源顯示字串，不論有沒有標確定性，那個來源都該進註冊表、都該有`source_ids` 指過去。掃描範圍也含 `Drills/*.yaml`。W009 仍綁 `certainty`——它問的是「標了 🟢/🟡 卻拿不出任何來源」，語意本來就以確定性標記為前提。兩者差別在**有沒有來源顯示資訊**：W002 已經有字串，只差把它登錄成來源條目再補機器鍵（純遷移）；W009 連顯示字串都沒有，得回頭找出主張的依據（S3b，不能靠遷移解決）。兩者不可互相代替，也不可用佔位來源填掉 W009。

（無）

---

## W003 — 孤兒條目：無 links 指入、自身也無指出

**WARN，共 126 筆**

  file=canonical\development\matrix.yaml id='dev.physical.l2t'
  file=canonical\development\matrix.yaml id='dev.physical.t2t'
  file=canonical\development\matrix.yaml id='dev.physical.t2c'
  file=canonical\development\matrix.yaml id='dev.physical.t2w'
  file=canonical\development\matrix.yaml id='dev.mental.l2t'
  file=canonical\development\matrix.yaml id='dev.mental.t2t'
  file=canonical\development\matrix.yaml id='dev.mental.t2c'
  file=canonical\development\matrix.yaml id='dev.mental.t2w'
  file=canonical\development\matrix.yaml id='dev.life.l2t'
  file=canonical\development\matrix.yaml id='dev.life.t2t'
  file=canonical\development\matrix.yaml id='dev.life.t2c'
  file=canonical\development\matrix.yaml id='dev.life.t2w'
  file=canonical\health\injuries.yaml id='_asian-epidemiology-supplement'
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability'
  file=canonical\health\injuries.yaml id='slap-lesion'
  file=canonical\health\injuries.yaml id='recreational-water-cryptosporidium'
  file=canonical\health\injuries.yaml id='swimmer-dental-erosion'
  file=canonical\health\injuries.yaml id='swimmer-dermatoses'
  file=canonical\health\injuries.yaml id='swimming-induced-bronchoconstriction'
  file=canonical\health\injuries.yaml id='uv-photo-damage'
  file=canonical\health\injuries.yaml id='iron-deficiency-swimmer'
  file=canonical\health\injuries.yaml id='oral-contraceptives-performance'
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards'
  file=canonical\health\injuries.yaml id='poolside-slip-fall'
  file=canonical\health\injuries.yaml id='osgood-schlatter'
  file=canonical\health\injuries.yaml id='sever-disease'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.26'
  file=canonical\movement\actions.yaml id='movement.action.hip.adduction'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.overview'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.transfer'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.methods'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.concurrent'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.needs_analysis'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.youth'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.caveats'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.tricycle'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.multipeak'
  file=canonical\periodization\structure.yaml id='periodization.structure.swim_annual'
  file=canonical\periodization\structure.yaml id='periodization.structure.swim_youth_ltad'
  file=canonical\periodization\taper.yaml id='periodization.taper.definition'
  file=canonical\periodization\taper.yaml id='periodization.taper.volume'
  file=canonical\periodization\taper.yaml id='periodization.taper.duration'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.linear'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.step'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.fast_exponential'
  file=canonical\periodization\taper.yaml id='periodization.taper.peak_window'
  file=canonical\periodization\taper.yaml id='periodization.taper.swim'
  file=canonical\psychology\psychology.yaml id='psych.fear'
  file=canonical\psychology\psychology.yaml id='psych.fear.control_loss'
  file=canonical\psychology\psychology.yaml id='psych.fear.perception_masking'
  file=canonical\psychology\psychology.yaml id='psych.fear.freeze_reflex'
  file=canonical\psychology\psychology.yaml id='psych.fear.co2_breath_panic'
  file=canonical\psychology\psychology.yaml id='psych.fear.diving_reflex_calm'
  file=canonical\psychology\psychology.yaml id='psych.fear.safety_precondition'
  file=canonical\psychology\psychology.yaml id='psych.fear.population_faces'
  file=canonical\psychology\psychology.yaml id='psych.interaction'
  file=canonical\psychology\psychology.yaml id='psych.interaction.anterior_insula_gain'
  file=canonical\psychology\psychology.yaml id='psych.interaction.stress_hypertonia'
  file=canonical\psychology\psychology.yaml id='psych.interaction.rpe_psychobiological'
  file=canonical\psychology\psychology.yaml id='psych.interaction.attentional_narrowing'
  file=canonical\psychology\psychology.yaml id='psych.interaction.vagal_tone_fear_extinction'
  file=canonical\psychology\psychology.yaml id='psych.interaction.freeze_prefrontal_shutdown'
  file=canonical\psychology\psychology.yaml id='psych.interaction.breathing_cognitive_load'
  file=canonical\psychology\psychology.yaml id='psych.interaction.water_immersion_interoception'
  file=canonical\psychology\psychology.yaml id='psych.motivation'
  file=canonical\psychology\psychology.yaml id='psych.motivation.bpn_triad'
  file=canonical\psychology\psychology.yaml id='psych.motivation.continuum'
  file=canonical\psychology\psychology.yaml id='psych.motivation.autonomy_support'
  file=canonical\psychology\psychology.yaml id='psych.motivation.mastery_vs_performance_climate'
  file=canonical\psychology\psychology.yaml id='psych.motivation.amotivation_trap'
  file=canonical\psychology\psychology.yaml id='psych.motivation.competence_moderator'
  file=canonical\psychology\psychology.yaml id='psych.motivation.climate_biology'
  file=canonical\psychology\psychology.yaml id='psych.motivation.hmiem_bottomup'
  file=canonical\psychology\psychology.yaml id='psych.motivation.population_engines'
  file=canonical\psychology\psychology.yaml id='psych.imagery'
  file=canonical\psychology\psychology.yaml id='psych.imagery.functional_equivalence'
  file=canonical\psychology\psychology.yaml id='psych.imagery.pettlep'
  file=canonical\psychology\psychology.yaml id='psych.imagery.kinesthetic_priority'
  file=canonical\psychology\psychology.yaml id='psych.imagery.feedforward_calibration'
  file=canonical\psychology\psychology.yaml id='psych.imagery.functional_types'
  file=canonical\psychology\psychology.yaml id='psych.imagery.off_water_maintenance'
  file=canonical\psychology\psychology.yaml id='psych.attention'
  file=canonical\psychology\psychology.yaml id='psych.attention.ef_if_definition'
  file=canonical\psychology\psychology.yaml id='psych.attention.cah'
  file=canonical\psychology\psychology.yaml id='psych.attention.elite_resilience'
  file=canonical\psychology\psychology.yaml id='psych.attention.distance_effect'
  file=canonical\psychology\psychology.yaml id='psych.attention.water_sense_third_category'
  file=canonical\psychology\psychology.yaml id='psych.attention.association_dissociation'
  file=canonical\psychology\psychology.yaml id='psych.self_talk'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.trainable_skill'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.ist_mst_matching'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.external_focus_ist'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.interfering_thoughts_bandwidth'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.tense_drift'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.mst_endurance_efficiency'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.pre_performance_routine'
  file=canonical\psychology\psychology.yaml id='psych.self_talk.systematic_training'
  file=canonical\psychology\psychology.yaml id='psych.arousal'
  file=canonical\psychology\psychology.yaml id='psych.arousal.inverted_u'
  file=canonical\psychology\psychology.yaml id='psych.arousal.izof'
  file=canonical\psychology\psychology.yaml id='psych.arousal.catastrophe'
  file=canonical\psychology\psychology.yaml id='psych.arousal.reinvestment'
  file=canonical\psychology\psychology.yaml id='psych.arousal.explicit_monitoring'
  file=canonical\psychology\psychology.yaml id='psych.arousal.muscle_tension_loop'
  file=canonical\psychology\psychology.yaml id='psych.arousal.breath_reinvestment'
  file=canonical\psychology\psychology.yaml id='psych.arousal.implicit_learning'
  file=canonical\psychology\psychology.yaml id='psych.flow'
  file=canonical\psychology\psychology.yaml id='psych.flow.action_awareness_merging'
  file=canonical\psychology\psychology.yaml id='psych.flow.challenge_skill_balance'
  file=canonical\psychology\psychology.yaml id='psych.flow.indirect_control'
  file=canonical\psychology\psychology.yaml id='psych.flow.flow_vs_clutch'
  file=canonical\psychology\psychology.yaml id='psych.flow.reinvestment'
  file=canonical\psychology\psychology.yaml id='psych.flow.de_reinvestment'
  file=canonical\psychology\psychology.yaml id='psych.flow.hypofrontality'
  file=canonical\psychology\psychology.yaml id='psych.flow.flow_across_levels'
  file=canonical\psychology\psychology.yaml id='psych.flow.water_as_feedback'
  file=canonical\psychology\psychology.yaml id='psych.flow.izof_individual_zones'
  file=canonical\technica\water-sense-levels.yaml id='free.L0'
  file=canonical\technica\water-sense-levels.yaml id='back.L0'

---

## W004 — `links.*_link` 內的疑似穩定 ID 未列入對應的 `links.*_link_ids`

**WARN，共 0 筆**

> **契約說明（S4b）**：`mechanism_link` / `technical_link` / `perception_link` 是顯示層自由文字（下游 my-site 當純字串渲染，不可改名或改成陣列）；可解析的穩定 ID 放同名 + `_ids` 的機器鍵。本節列出「顯示字串裡看得到 ID、但機器鍵沒同步」的脫節案例。修法是改 `canonical/health/drafts/*.yaml` 補進 `*_link_ids` 再重跑 `tools/build_injuries.py`。**不可直接改 `canonical/health/injuries.yaml`**（promoted artifact，檔頭寫明勿手改）。

（無）

---

## W005 — `links` 下未知子鍵（未歸類為 ID 參照類、詞彙參照類或已知自由文字類）

**WARN，共 0 筆**

（無）

---

## W006 — `cross_ref` 有值但缺 `cross_ref_ids` 欄位（未處理；`[]` 才是「已檢查、無 ID 可連」）

**WARN，共 0 筆**

（無）

---

## W007 — `links.*_link` 有值但缺 `*_link_ids` 欄位（未處理；`[]` 才是「已檢查、無 ID 可連」）

**WARN，共 0 筆**

（無）

---

## W008 — 孤兒來源：`_sources.yaml` 有登錄但沒有任何條目以 `source_ids` 引用（`verification_status: retracted` 的墓碑除外）

**WARN，共 3 筆**

  source_id='src.gonjo-2018' 已登錄於 _sources.yaml 但無任何條目引用
  source_id='src.lee-2008' 已登錄於 _sources.yaml 但無任何條目引用
  source_id='src.liu-2025-core-meta' 已登錄於 _sources.yaml 但無任何條目引用

---

## W009 — `certainty` green/yellow 且**完全沒有**來源資訊（無 `source`/`sources`/`citation`，也無 `source_ids`，祖先亦無，且未宣告 `evidence_from`）→ 需補來源或改確定性，S3b 範圍

**WARN，共 0 筆**

（無）

---

## W010 — 死標籤：`categories` 區塊宣告了某 key，但該檔沒有任何條目使用

**WARN，共 0 筆**

（無）

---

## W011 — `certainty` orange（教練觀測）但缺 `observation_basis`（未交代觀察基礎與外推邊界）→ S6 範圍

**WARN，共 0 筆**

（無）

---

## W012 — movement 條目 ID 的檔案命名空間或分段格式違規

**WARN，共 0 筆**

（無）

---

## W014 — movement 跨檔引用無法解析，或目標存在但命名空間錯誤

**WARN，共 0 筆**

（無）

---

## W015 — `published` movement 條目缺少狀態、證據或介入決策必填欄位

**WARN，共 0 筆**

（無）

---

## W016 — `mobility_decision: evidence-gap` 的介入仍寫成可執行處方

**WARN，共 0 筆**

（無）

---

## W017 — demand 的相位未登錄，或 phase_model 與 movement_phase_registry 不符

**WARN，共 0 筆**

（無）

---

## W018 — demand 缺 `action_reference_frame`，或 `joint-local` 無分節段量測支撐

**WARN，共 0 筆**

（無）

---

## W019 — demand 文字含量化主張但 `measurement_conditions` 缺漏或不完整

**WARN，共 0 筆**

（無）

---

## W020 — `action_status: ready` 的必要條件未滿足（`claim_status` 不是 `supported`，或 demand 缺 `measurement_conditions`）

**WARN，共 0 筆**

（無）

---

## W021 — 區塊標了 `certainty` 但沒有任何內容欄位（證據標記還在、內容不見了）

**WARN，共 0 筆**

（無）

---
