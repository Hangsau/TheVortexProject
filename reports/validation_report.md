# Vortex Canonical 驗證報告

> 生成日期：2026-07-26  
> 驗證條目數：594，Drills ID 數：176

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

**WARN，共 476 筆**

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
  file=canonical\health\injuries.yaml id='A-shoulder-upper'
  file=canonical\health\injuries.yaml id='B-lower-spine-strokespecific'
  file=canonical\health\injuries.yaml id='C-nonMSK-medical'
  file=canonical\health\injuries.yaml id='D-systemic-acute'
  file=canonical\health\injuries.yaml id='D-endocrine'
  file=canonical\health\injuries.yaml id='E-acute-trauma'
  file=canonical\health\injuries.yaml id='F-pediatric-growth'
  file=canonical\health\injuries.yaml id='_asian-epidemiology-supplement'
  file=canonical\health\injuries.yaml id='biceps-tendinopathy'
  file=canonical\health\injuries.yaml id='rotator-cuff-tendinopathy'
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability'
  file=canonical\health\injuries.yaml id='slap-lesion'
  file=canonical\health\injuries.yaml id='swimmer-elbow-wrist-overuse'
  file=canonical\health\injuries.yaml id='thoracic-outlet-syndrome'
  file=canonical\health\injuries.yaml id='extension-low-back-pain'
  file=canonical\health\injuries.yaml id='femoroacetabular-impingement'
  file=canonical\health\injuries.yaml id='groin-adductor-strain'
  file=canonical\health\injuries.yaml id='spondylolysis'
  file=canonical\health\injuries.yaml id='swimmer-ankle-foot-overuse'
  file=canonical\health\injuries.yaml id='acanthamoeba-keratitis'
  file=canonical\health\injuries.yaml id='chlorine-eye-irritation'
  file=canonical\health\injuries.yaml id='recreational-water-cryptosporidium'
  file=canonical\health\injuries.yaml id='sci-hip-flexor-contracture'
  file=canonical\health\injuries.yaml id='surfers-ear-exostosis'
  file=canonical\health\injuries.yaml id='swimmer-dental-erosion'
  file=canonical\health\injuries.yaml id='swimmer-dermatoses'
  file=canonical\health\injuries.yaml id='swimmers-ear'
  file=canonical\health\injuries.yaml id='swimming-induced-bronchoconstriction'
  file=canonical\health\injuries.yaml id='uv-photo-damage'
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia'
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death'
  file=canonical\health\injuries.yaml id='hypothermia-swimmers'
  file=canonical\health\injuries.yaml id='iron-deficiency-swimmer'
  file=canonical\health\injuries.yaml id='oral-contraceptives-performance'
  file=canonical\health\injuries.yaml id='red-s'
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards'
  file=canonical\health\injuries.yaml id='poolside-slip-fall'
  file=canonical\health\injuries.yaml id='osgood-schlatter'
  file=canonical\health\injuries.yaml id='sever-disease'
  file=canonical\instructional\teaching-errors.yaml id='free.err1'
  file=canonical\instructional\teaching-errors.yaml id='free.err2'
  file=canonical\instructional\teaching-errors.yaml id='free.err3'
  file=canonical\instructional\teaching-errors.yaml id='free.err4'
  file=canonical\instructional\teaching-errors.yaml id='free.err5'
  file=canonical\instructional\teaching-errors.yaml id='free.err6'
  file=canonical\instructional\teaching-errors.yaml id='free.err7'
  file=canonical\instructional\teaching-errors.yaml id='free.err8'
  file=canonical\instructional\teaching-errors.yaml id='free.err9'
  file=canonical\instructional\teaching-errors.yaml id='free.err10'
  file=canonical\instructional\teaching-errors.yaml id='free.err11'
  file=canonical\instructional\teaching-errors.yaml id='free.err12'
  file=canonical\instructional\teaching-errors.yaml id='free.err13'
  file=canonical\instructional\teaching-errors.yaml id='free.err14'
  file=canonical\instructional\teaching-errors.yaml id='free.err15'
  file=canonical\instructional\teaching-errors.yaml id='free.err16'
  file=canonical\instructional\teaching-errors.yaml id='free.err17'
  file=canonical\instructional\teaching-errors.yaml id='free.err18'
  file=canonical\instructional\teaching-errors.yaml id='free.err19'
  file=canonical\instructional\teaching-errors.yaml id='free.err20'
  file=canonical\instructional\teaching-errors.yaml id='free.err21'
  file=canonical\instructional\teaching-errors.yaml id='free.err22'
  file=canonical\instructional\teaching-errors.yaml id='free.err23'
  file=canonical\instructional\teaching-errors.yaml id='free.err24'
  file=canonical\instructional\teaching-errors.yaml id='free.err25'
  file=canonical\instructional\teaching-errors.yaml id='back.err1'
  file=canonical\instructional\teaching-errors.yaml id='back.err2'
  file=canonical\instructional\teaching-errors.yaml id='back.err3'
  file=canonical\instructional\teaching-errors.yaml id='back.err4'
  file=canonical\instructional\teaching-errors.yaml id='back.err5'
  file=canonical\instructional\teaching-errors.yaml id='back.err6'
  file=canonical\instructional\teaching-errors.yaml id='back.err7'
  file=canonical\instructional\teaching-errors.yaml id='back.err8'
  file=canonical\instructional\teaching-errors.yaml id='back.err9'
  file=canonical\instructional\teaching-errors.yaml id='back.err10'
  file=canonical\instructional\teaching-errors.yaml id='back.err11'
  file=canonical\instructional\teaching-errors.yaml id='back.err12'
  file=canonical\instructional\teaching-errors.yaml id='back.err13'
  file=canonical\instructional\teaching-errors.yaml id='back.err14'
  file=canonical\instructional\teaching-errors.yaml id='back.err15'
  file=canonical\instructional\teaching-errors.yaml id='back.err16'
  file=canonical\instructional\teaching-errors.yaml id='back.err17'
  file=canonical\instructional\teaching-errors.yaml id='breast.err1'
  file=canonical\instructional\teaching-errors.yaml id='breast.err2'
  file=canonical\instructional\teaching-errors.yaml id='breast.err3'
  file=canonical\instructional\teaching-errors.yaml id='breast.err4'
  file=canonical\instructional\teaching-errors.yaml id='breast.err5'
  file=canonical\instructional\teaching-errors.yaml id='breast.err6'
  file=canonical\instructional\teaching-errors.yaml id='breast.err7'
  file=canonical\instructional\teaching-errors.yaml id='breast.err8'
  file=canonical\instructional\teaching-errors.yaml id='breast.err9'
  file=canonical\instructional\teaching-errors.yaml id='breast.err10'
  file=canonical\instructional\teaching-errors.yaml id='breast.err11'
  file=canonical\instructional\teaching-errors.yaml id='breast.err12'
  file=canonical\instructional\teaching-errors.yaml id='breast.err13'
  file=canonical\instructional\teaching-errors.yaml id='breast.err14'
  file=canonical\instructional\teaching-errors.yaml id='breast.err15'
  file=canonical\instructional\teaching-errors.yaml id='breast.err16'
  file=canonical\instructional\teaching-errors.yaml id='breast.err17'
  file=canonical\instructional\teaching-errors.yaml id='fly.err1'
  file=canonical\instructional\teaching-errors.yaml id='fly.err2'
  file=canonical\instructional\teaching-errors.yaml id='fly.err3'
  file=canonical\instructional\teaching-errors.yaml id='fly.err4'
  file=canonical\instructional\teaching-errors.yaml id='fly.err5'
  file=canonical\instructional\teaching-errors.yaml id='fly.err6'
  file=canonical\instructional\teaching-errors.yaml id='fly.err7'
  file=canonical\instructional\teaching-errors.yaml id='fly.err8'
  file=canonical\instructional\teaching-errors.yaml id='fly.err9'
  file=canonical\instructional\teaching-errors.yaml id='fly.err10'
  file=canonical\instructional\teaching-errors.yaml id='fly.err11'
  file=canonical\instructional\teaching-errors.yaml id='fly.err12'
  file=canonical\instructional\teaching-errors.yaml id='fly.err13'
  file=canonical\instructional\teaching-errors.yaml id='fly.err14'
  file=canonical\instructional\teaching-errors.yaml id='fly.err15'
  file=canonical\instructional\teaching-errors.yaml id='fly.err16'
  file=canonical\instructional\teaching-errors.yaml id='udk.err1'
  file=canonical\instructional\teaching-errors.yaml id='udk.err2'
  file=canonical\instructional\teaching-errors.yaml id='udk.err3'
  file=canonical\instructional\teaching-errors.yaml id='udk.err4'
  file=canonical\instructional\teaching-errors.yaml id='udk.err5'
  file=canonical\instructional\teaching-errors.yaml id='udk.err6'
  file=canonical\instructional\teaching-errors.yaml id='udk.err7'
  file=canonical\instructional\teaching-errors.yaml id='udk.err8'
  file=canonical\instructional\teaching-errors.yaml id='udk.err9'
  file=canonical\instructional\teaching-errors.yaml id='udk.err10'
  file=canonical\instructional\teaching-errors.yaml id='udk.err11'
  file=canonical\instructional\teaching-errors.yaml id='udk.err12'
  file=canonical\instructional\teaching-errors.yaml id='udk.err13'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err1'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err2'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err3'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err4'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err5'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err6'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err7'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err8'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err9'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err10'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err11'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err12'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err13'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err14'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.33'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.34'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.35'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.33'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.34'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.35'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.36'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.35'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.41'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.42'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.43'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.44'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.5'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.6'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.10'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.11'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.24'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.33'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.34'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.35'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.36'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.37'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.38'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.39'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.40'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.45'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.46'
  file=canonical\perception\free.yaml id='protocol.free.evf'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.multipeak'
  file=canonical\periodization\taper.yaml id='periodization.taper.definition'
  file=canonical\periodization\taper.yaml id='periodization.taper.volume'
  file=canonical\periodization\taper.yaml id='periodization.taper.intensity'
  file=canonical\periodization\taper.yaml id='periodization.taper.frequency'
  file=canonical\periodization\taper.yaml id='periodization.taper.duration'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.linear'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.step'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.fast_exponential'
  file=canonical\periodization\taper.yaml id='periodization.taper.peak_window'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_7_1'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_11_2'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_11_1'
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
  file=canonical\technica\l-indicators.yaml id='common.pre.resistance'
  file=canonical\technica\l-indicators.yaml id='free.pre.resistance'
  file=canonical\technica\l-indicators.yaml id='free.L2.kick'
  file=canonical\technica\l-indicators.yaml id='free.L3.kick-rhythm'
  file=canonical\technica\l-indicators.yaml id='free.L5.coupling-timing'
  file=canonical\technica\l-indicators.yaml id='free.L5.lift-phase-duration'
  file=canonical\technica\l-indicators.yaml id='back.pre.orientation'
  file=canonical\technica\l-indicators.yaml id='back.L2.up-kick'
  file=canonical\technica\l-indicators.yaml id='back.L4.head-stillness'
  file=canonical\technica\l-indicators.yaml id='fly.pre.undulation'
  file=canonical\technica\l-indicators.yaml id='fly.L2.kick'
  file=canonical\technica\l-indicators.yaml id='fly.L5.glide-elimination'
  file=canonical\technica\l-indicators.yaml id='breast.pre.resistance'
  file=canonical\technica\water-sense-levels.yaml id='free.L0'
  file=canonical\technica\water-sense-levels.yaml id='free.L1'
  file=canonical\technica\water-sense-levels.yaml id='free.L2'
  file=canonical\technica\water-sense-levels.yaml id='free.L3'
  file=canonical\technica\water-sense-levels.yaml id='free.L4'
  file=canonical\technica\water-sense-levels.yaml id='free.L5'
  file=canonical\technica\water-sense-levels.yaml id='free.L6'
  file=canonical\technica\water-sense-levels.yaml id='back.L0'
  file=canonical\technica\water-sense-levels.yaml id='back.L1'
  file=canonical\technica\water-sense-levels.yaml id='back.L2'
  file=canonical\technica\water-sense-levels.yaml id='back.L3'
  file=canonical\technica\water-sense-levels.yaml id='back.L4'
  file=canonical\technica\water-sense-levels.yaml id='back.L5'
  file=canonical\technica\water-sense-levels.yaml id='back.L6'
  file=canonical\technica\water-sense-levels.yaml id='breast.pre'
  file=canonical\technica\water-sense-levels.yaml id='breast.L2'
  file=canonical\technica\water-sense-levels.yaml id='breast.L3'
  file=canonical\technica\water-sense-levels.yaml id='breast.L4'
  file=canonical\technica\water-sense-levels.yaml id='breast.L5'
  file=canonical\technica\water-sense-levels.yaml id='breast.L6'
  file=canonical\technica\water-sense-levels.yaml id='fly.pre'
  file=canonical\technica\water-sense-levels.yaml id='fly.L2'
  file=canonical\technica\water-sense-levels.yaml id='fly.L3'
  file=canonical\technica\water-sense-levels.yaml id='fly.L4'
  file=canonical\technica\water-sense-levels.yaml id='fly.L5'
  file=canonical\technica\water-sense-levels.yaml id='fly.L6'

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

## W008 — 孤兒來源：`_sources.yaml` 有登錄但沒有任何條目以 `source_ids` 引用

**WARN，共 0 筆**

（無）

---

## W009 — `certainty` green/yellow 且**完全沒有**來源資訊（無 `source`/`sources`，也無 `source_ids`）→ 需補來源，S3b 範圍

**WARN，共 270 筆**

  file=canonical\health\injuries.yaml id='_asian-epidemiology-supplement' at=meta_references[0].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='_asian-epidemiology-supplement' at=meta_references[0].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='_asian-epidemiology-supplement' at=meta_references[0].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='biceps-tendinopathy' at=injuries[0].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='biceps-tendinopathy' at=injuries[0].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='rotator-cuff-tendinopathy' at=injuries[1].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='rotator-cuff-tendinopathy' at=injuries[1].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='rotator-cuff-tendinopathy' at=injuries[1].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='rotator-cuff-tendinopathy' at=injuries[1].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability' at=injuries[2].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability' at=injuries[2].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability' at=injuries[2].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='slap-lesion' at=injuries[3].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='slap-lesion' at=injuries[3].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='slap-lesion' at=injuries[3].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmers-shoulder' at=injuries[5].references[2] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='thoracic-outlet-syndrome' at=injuries[6].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='thoracic-outlet-syndrome' at=injuries[6].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='breaststrokers-knee' at=injuries[7].references[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='extension-low-back-pain' at=injuries[8].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='extension-low-back-pain' at=injuries[8].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='femoroacetabular-impingement' at=injuries[9].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='femoroacetabular-impingement' at=injuries[9].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='groin-adductor-strain' at=injuries[10].references[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='spondylolysis' at=injuries[11].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='spondylolysis' at=injuries[11].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-ankle-foot-overuse' at=injuries[12].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='acanthamoeba-keratitis' at=injuries[13].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='chlorine-eye-irritation' at=injuries[14].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='recreational-water-cryptosporidium' at=injuries[15].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='recreational-water-cryptosporidium' at=injuries[15].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='surfers-ear-exostosis' at=injuries[17].references[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='surfers-ear-exostosis' at=injuries[17].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dental-erosion' at=injuries[18].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dental-erosion' at=injuries[18].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dental-erosion' at=injuries[18].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dermatoses' at=injuries[19].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dermatoses' at=injuries[19].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-dermatoses' at=injuries[19].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmers-ear' at=injuries[20].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmers-ear' at=injuries[20].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimming-induced-bronchoconstriction' at=injuries[21].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimming-induced-bronchoconstriction' at=injuries[21].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimming-induced-bronchoconstriction' at=injuries[21].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='uv-photo-damage' at=injuries[22].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='uv-photo-damage' at=injuries[22].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='uv-photo-damage' at=injuries[22].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='uv-photo-damage' at=injuries[22].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='cold-water-shock' at=injuries[23].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='cold-water-shock' at=injuries[23].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='cold-water-shock' at=injuries[23].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='cold-water-shock' at=injuries[23].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia' at=injuries[24].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia' at=injuries[24].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia' at=injuries[24].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia' at=injuries[24].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='drowning' at=injuries[25].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='drowning' at=injuries[25].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='drowning' at=injuries[25].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='drowning' at=injuries[25].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='drowning' at=injuries[25].references[4] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death' at=injuries[26].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death' at=injuries[26].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death' at=injuries[26].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death' at=injuries[26].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death' at=injuries[26].references[4] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='hypothermia-swimmers' at=injuries[27].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='hypothermia-swimmers' at=injuries[27].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='hypothermia-swimmers' at=injuries[27].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='hypothermia-swimmers' at=injuries[27].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='sipe' at=injuries[29].references[1] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exercise-amenorrhea' at=injuries[30].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='exercise-amenorrhea' at=injuries[30].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='female-athlete-triad' at=injuries[31].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='female-athlete-triad' at=injuries[31].references[1] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='stress-fracture-swimmer' at=injuries[35].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='stress-fracture-swimmer' at=injuries[35].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-low-bone-density' at=injuries[36].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='swimmer-low-bone-density' at=injuries[36].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='diving-cervical-injury' at=injuries[37].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='diving-cervical-injury' at=injuries[37].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='diving-cervical-injury' at=injuries[37].references[2] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='diving-cervical-injury' at=injuries[37].references[3] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='diving-cervical-injury' at=injuries[37].references[4] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='flip-turn-wall-push' at=injuries[38].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='flip-turn-wall-push' at=injuries[38].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards' at=injuries[39].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards' at=injuries[39].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards' at=injuries[39].references[2] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='poolside-slip-fall' at=injuries[40].references[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='poolside-slip-fall' at=injuries[40].references[1] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='starting-block-impact' at=injuries[41].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='starting-block-impact' at=injuries[41].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='starting-block-impact' at=injuries[41].references[2] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='osgood-schlatter' at=injuries[42].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='osgood-schlatter' at=injuries[42].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='salter-harris-physeal-fracture' at=injuries[43].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='scheuermann-kyphosis' at=injuries[44].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='sever-disease' at=injuries[45].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='sever-disease' at=injuries[45].references[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\health\injuries.yaml id='youth-swimmer-apophysitis' at=injuries[46].references[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='free.err7' at=errors[6].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='free.err24' at=errors[23].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='free.err25' at=errors[24].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err1' at=errors[25].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err2' at=errors[26].public.physical_reason certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err4' at=errors[28].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err5' at=errors[29].public.physical_reason certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err8' at=errors[32].public.physical_reason certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='back.err16' at=errors[40].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='breast.err5' at=errors[46].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='breast.err15' at=errors[56].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err1' at=errors[75].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err3' at=errors[77].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err4' at=errors[78].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err6' at=errors[80].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err7' at=errors[81].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='udk.err12' at=errors[86].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err12' at=errors[99].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err14' at=errors[101].public.physical_reason certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.3' at=points[2].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.27' at=points[8].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.28' at=points[9].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.10' at=points[11].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.11' at=points[12].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.12' at=points[13].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.13' at=points[14].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.15' at=points[16].public.mechanism certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.19' at=points[21].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.20' at=points[22].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.21' at=points[23].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.23' at=points[25].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.24' at=points[26].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.25' at=points[27].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='free.tech.35' at=points[34].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.1' at=points[37].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.2' at=points[38].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.5' at=points[41].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.11' at=points[47].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.15' at=points[51].public.mechanism certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.16' at=points[52].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.17' at=points[53].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.18' at=points[54].public.mechanism certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.22' at=points[58].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.24' at=points[60].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.25' at=points[61].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='back.tech.27' at=points[63].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.3' at=points[66].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.5' at=points[68].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.6' at=points[69].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.7' at=points[70].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.8' at=points[71].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.9' at=points[72].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.11' at=points[74].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.12' at=points[75].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.14' at=points[77].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.17' at=points[80].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.18' at=points[81].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.19' at=points[82].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.22' at=points[85].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.23' at=points[86].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.24' at=points[87].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.25' at=points[88].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.27' at=points[90].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.28' at=points[91].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.30' at=points[93].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.31' at=points[94].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.3' at=points[97].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.7' at=points[101].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.11' at=points[105].public.mechanism certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.13' at=points[107].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.17' at=points[111].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.24' at=points[118].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.31' at=points[125].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.32' at=points[126].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.35' at=points[129].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.3' at=points[132].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.5' at=points[134].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.6' at=points[135].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.7' at=points[136].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.10' at=points[139].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.12' at=points[141].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.13' at=points[142].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.15' at=points[144].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.17' at=points[146].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.25' at=points[154].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.26' at=points[155].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.27' at=points[156].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.28' at=points[157].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.3' at=points[163].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.42' at=points[166].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.7' at=points[171].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.9' at=points[173].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.12' at=points[176].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.14' at=points[178].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.15' at=points[179].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.17' at=points[181].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.21' at=points[185].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.22' at=points[186].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.25' at=points[189].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.26' at=points[190].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.27' at=points[191].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.28' at=points[192].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.29' at=points[193].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.33' at=points[197].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.40' at=points[204].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.45' at=points[205].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.46' at=points[206].public.mechanism certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.fear.control_loss' at=themes[0].concepts[0].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.fear.control_loss' at=themes[0].concepts[0].public.intervention_refs[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.fear.freeze_reflex' at=themes[0].concepts[2].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.fear.co2_breath_panic' at=themes[0].concepts[3].public.hardware_boundary certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.fear.diving_reflex_calm' at=themes[0].concepts[4].public.hardware_boundary certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.anterior_insula_gain' at=themes[1].concepts[0].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.stress_hypertonia' at=themes[1].concepts[1].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.rpe_psychobiological' at=themes[1].concepts[2].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.rpe_psychobiological' at=themes[1].concepts[2].public.intervention_refs[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.attentional_narrowing' at=themes[1].concepts[3].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.vagal_tone_fear_extinction' at=themes[1].concepts[4].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.vagal_tone_fear_extinction' at=themes[1].concepts[4].public.intervention_refs[0] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.freeze_prefrontal_shutdown' at=themes[1].concepts[5].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.water_immersion_interoception' at=themes[1].concepts[7].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.interaction.water_immersion_interoception' at=themes[1].concepts[7].public.hardware_boundary certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation' at=themes[2].premise certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation.bpn_triad' at=themes[2].concepts[0].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation.continuum' at=themes[2].concepts[1].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation.autonomy_support' at=themes[2].concepts[2].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation.mastery_vs_performance_climate' at=themes[2].concepts[3].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.motivation.competence_moderator' at=themes[2].concepts[5].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery' at=themes[3].premise certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.functional_equivalence' at=themes[3].concepts[0].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.functional_equivalence' at=themes[3].concepts[0].public.hardware_boundary certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.pettlep' at=themes[3].concepts[1].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.pettlep' at=themes[3].concepts[1].public.intervention_refs[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.pettlep' at=themes[3].concepts[1].public.intervention_refs[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.kinesthetic_priority' at=themes[3].concepts[2].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.feedforward_calibration' at=themes[3].concepts[3].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.functional_types' at=themes[3].concepts[4].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.imagery.off_water_maintenance' at=themes[3].concepts[5].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention' at=themes[4].premise certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.ef_if_definition' at=themes[4].concepts[0].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.cah' at=themes[4].concepts[1].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.elite_resilience' at=themes[4].concepts[2].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.distance_effect' at=themes[4].concepts[3].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.water_sense_third_category' at=themes[4].concepts[4].public.hardware_boundary certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.association_dissociation' at=themes[4].concepts[5].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.attention.association_dissociation' at=themes[4].concepts[5].public.intervention_refs[1] certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk' at=themes[5].premise certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.trainable_skill' at=themes[5].concepts[0].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.ist_mst_matching' at=themes[5].concepts[1].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.external_focus_ist' at=themes[5].concepts[2].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.mst_endurance_efficiency' at=themes[5].concepts[5].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.pre_performance_routine' at=themes[5].concepts[6].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.systematic_training' at=themes[5].concepts[7].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.systematic_training' at=themes[5].concepts[7].public.intervention_refs[0] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.self_talk.systematic_training' at=themes[5].concepts[7].public.intervention_refs[1] certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal' at=themes[6].premise certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.inverted_u' at=themes[6].concepts[0].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.izof' at=themes[6].concepts[1].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.catastrophe' at=themes[6].concepts[2].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.reinvestment' at=themes[6].concepts[3].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.explicit_monitoring' at=themes[6].concepts[4].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.arousal.implicit_learning' at=themes[6].concepts[7].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.action_awareness_merging' at=themes[7].concepts[0].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.challenge_skill_balance' at=themes[7].concepts[1].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.indirect_control' at=themes[7].concepts[2].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.flow_vs_clutch' at=themes[7].concepts[3].public.phenomenon certainty=green 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.reinvestment' at=themes[7].concepts[4].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.hypofrontality' at=themes[7].concepts[6].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）
  file=canonical\psychology\psychology.yaml id='psych.flow.izof_individual_zones' at=themes[7].concepts[9].public.phenomenon certainty=yellow 完全無來源資訊（無 source/sources，也無 source_ids）

---
