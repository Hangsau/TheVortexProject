# Vortex Canonical 驗證報告

> 生成日期：2026-09-04
> 驗證條目數：754，Drills ID 數：176

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

## W001 — `cross_ref` 內的疑似穩定 ID 未列入同層 `cross_ref_ids`

**WARN，共 1 筆**

  file=canonical\instructional\technical-analysis.yaml id='free.tech.39' public.cross_ref 內疑似穩定 ID ['back.tech.28'] 未列入 cross_ref_ids (120 chars): 'free.tech.36（同屬技術描述的欄位粒度問題）、back.tech.28（仰式轉體幅度）'

---

## W002 — 區塊**有**來源顯示字串（`source`/`sources`）但缺 `source_ids`（機器鍵沒跟上顯示層）；S3a-2 起不看 `certainty`

**WARN，共 0 筆**

> **契約說明（S3a／S3a-2）**：`source`（單數字串）與 `sources`（複數清單）都是顯示層自由文字，下游 my-site 直接渲染，**不可改寫、改名或改成陣列**；可解析的來源鍵放同區塊的 `source_ids`，指向 `canonical/_sources.yaml` 的 `src.<slug>`。W002 自 S3a-2 起**與 `certainty` 解耦**：一個區塊只要帶了來源顯示字串，不論有沒有標確定性，那個來源都該進註冊表、都該有`source_ids` 指過去。掃描範圍也含 `Drills/*.yaml`。W009 仍綁 `certainty`——它問的是「標了 🟢/🟡 卻拿不出任何來源」，語意本來就以確定性標記為前提。兩者差別在**有沒有來源顯示資訊**：W002 已經有字串，只差把它登錄成來源條目再補機器鍵（純遷移）；W009 連顯示字串都沒有，得回頭找出主張的依據（S3b，不能靠遷移解決）。兩者不可互相代替，也不可用佔位來源填掉 W009。

（無）

---

## W003 — 孤兒條目：無 links 指入、自身也無指出

**WARN，共 349 筆**

  file=canonical\breathing\framework.yaml id='breathing.framework.overview'
  file=canonical\breathing\framework.yaml id='breathing.framework.grading'
  file=canonical\breathing\framework.yaml id='breathing.framework.boundaries'
  file=canonical\breathing\physiology.yaml id='breathing.physiology.muscles'
  file=canonical\breathing\physiology.yaml id='breathing.physiology.neural_control'
  file=canonical\breathing\physiology.yaml id='breathing.physiology.chemoreceptors'
  file=canonical\breathing\physiology.yaml id='breathing.physiology.autonomic_coupling'
  file=canonical\breathing\physiology.yaml id='breathing.physiology.baroreflex_resonance'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.principle'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.physiological_sigh'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.resonance_breathing'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.box_breathing'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.wim_hof'
  file=canonical\breathing\regulation.yaml id='breathing.regulation.claims_gap'
  file=canonical\breathing\safety.yaml id='breathing.safety.hypoxic_blackout'
  file=canonical\breathing\safety.yaml id='breathing.safety.hypocapnia_mechanism'
  file=canonical\breathing\training.yaml id='breathing.training.imt'
  file=canonical\breathing\training.yaml id='breathing.training.co2_tolerance'
  file=canonical\breathing\training.yaml id='breathing.training.buteyko'
  file=canonical\breathing\training.yaml id='breathing.training.bolt_test'
  file=canonical\breathing\training.yaml id='breathing.training.self_tracking'
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
  file=canonical\health\injuries.yaml id='shoulder-multidirectional-instability'
  file=canonical\health\injuries.yaml id='slap-lesion'
  file=canonical\health\injuries.yaml id='swimmer-elbow-wrist-overuse'
  file=canonical\health\injuries.yaml id='thoracic-outlet-syndrome'
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
  file=canonical\health\injuries.yaml id='cold-water-shock'
  file=canonical\health\injuries.yaml id='dehydration-hyponatremia'
  file=canonical\health\injuries.yaml id='drowning'
  file=canonical\health\injuries.yaml id='exertional-sudden-cardiac-death'
  file=canonical\health\injuries.yaml id='hypothermia-swimmers'
  file=canonical\health\injuries.yaml id='shallow-water-blackout'
  file=canonical\health\injuries.yaml id='sipe'
  file=canonical\health\injuries.yaml id='iron-deficiency-swimmer'
  file=canonical\health\injuries.yaml id='oral-contraceptives-performance'
  file=canonical\health\injuries.yaml id='open-water-marine-biological-hazards'
  file=canonical\health\injuries.yaml id='poolside-slip-fall'
  file=canonical\health\injuries.yaml id='osgood-schlatter'
  file=canonical\health\injuries.yaml id='sever-disease'
  file=canonical\instructional\teaching-errors.yaml id='free.err2'
  file=canonical\instructional\teaching-errors.yaml id='free.err3'
  file=canonical\instructional\teaching-errors.yaml id='free.err4'
  file=canonical\instructional\teaching-errors.yaml id='free.err6'
  file=canonical\instructional\teaching-errors.yaml id='free.err7'
  file=canonical\instructional\teaching-errors.yaml id='free.err8'
  file=canonical\instructional\teaching-errors.yaml id='free.err9'
  file=canonical\instructional\teaching-errors.yaml id='free.err11'
  file=canonical\instructional\teaching-errors.yaml id='free.err13'
  file=canonical\instructional\teaching-errors.yaml id='free.err14'
  file=canonical\instructional\teaching-errors.yaml id='free.err16'
  file=canonical\instructional\teaching-errors.yaml id='free.err19'
  file=canonical\instructional\teaching-errors.yaml id='free.err22'
  file=canonical\instructional\teaching-errors.yaml id='free.err23'
  file=canonical\instructional\teaching-errors.yaml id='back.err4'
  file=canonical\instructional\teaching-errors.yaml id='back.err7'
  file=canonical\instructional\teaching-errors.yaml id='back.err10'
  file=canonical\instructional\teaching-errors.yaml id='back.err12'
  file=canonical\instructional\teaching-errors.yaml id='back.err14'
  file=canonical\instructional\teaching-errors.yaml id='back.err16'
  file=canonical\instructional\teaching-errors.yaml id='breast.err1'
  file=canonical\instructional\teaching-errors.yaml id='breast.err2'
  file=canonical\instructional\teaching-errors.yaml id='breast.err3'
  file=canonical\instructional\teaching-errors.yaml id='breast.err6'
  file=canonical\instructional\teaching-errors.yaml id='breast.err7'
  file=canonical\instructional\teaching-errors.yaml id='breast.err8'
  file=canonical\instructional\teaching-errors.yaml id='breast.err9'
  file=canonical\instructional\teaching-errors.yaml id='breast.err10'
  file=canonical\instructional\teaching-errors.yaml id='breast.err12'
  file=canonical\instructional\teaching-errors.yaml id='breast.err13'
  file=canonical\instructional\teaching-errors.yaml id='breast.err14'
  file=canonical\instructional\teaching-errors.yaml id='fly.err2'
  file=canonical\instructional\teaching-errors.yaml id='fly.err3'
  file=canonical\instructional\teaching-errors.yaml id='fly.err5'
  file=canonical\instructional\teaching-errors.yaml id='fly.err13'
  file=canonical\instructional\teaching-errors.yaml id='fly.err15'
  file=canonical\instructional\teaching-errors.yaml id='fly.err16'
  file=canonical\instructional\teaching-errors.yaml id='udk.err1'
  file=canonical\instructional\teaching-errors.yaml id='udk.err2'
  file=canonical\instructional\teaching-errors.yaml id='udk.err3'
  file=canonical\instructional\teaching-errors.yaml id='udk.err4'
  file=canonical\instructional\teaching-errors.yaml id='udk.err5'
  file=canonical\instructional\teaching-errors.yaml id='udk.err7'
  file=canonical\instructional\teaching-errors.yaml id='udk.err8'
  file=canonical\instructional\teaching-errors.yaml id='udk.err9'
  file=canonical\instructional\teaching-errors.yaml id='udk.err10'
  file=canonical\instructional\teaching-errors.yaml id='udk.err11'
  file=canonical\instructional\teaching-errors.yaml id='udk.err12'
  file=canonical\instructional\teaching-errors.yaml id='udk.err13'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err11'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err12'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err13'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.14'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.41'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.7'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.9'
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
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.17'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.18'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.22'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.30'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.9'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.31'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.33'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.35'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.3'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.4'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.8'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.12'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.13'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.16'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.19'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.20'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.21'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.23'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.25'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.26'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.27'
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.29'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.15'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.28'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.32'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.33'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.36'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.45'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.46'
  file=canonical\movement\actions.yaml id='movement.action.hip.adduction'
  file=canonical\perception\free.yaml id='protocol.free.evf'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.overview'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.transfer'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.methods'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.concurrent'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.needs_analysis'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.injury'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.youth'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.flexibility'
  file=canonical\periodization\dryland.yaml id='periodization.dryland.caveats'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.monocycle'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.bicycle'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.tricycle'
  file=canonical\periodization\structure.yaml id='periodization.structure.annual.multipeak'
  file=canonical\periodization\structure.yaml id='periodization.structure.detraining'
  file=canonical\periodization\structure.yaml id='periodization.structure.swim_annual'
  file=canonical\periodization\structure.yaml id='periodization.structure.swim_youth_ltad'
  file=canonical\periodization\structure.yaml id='periodization.structure.schools_overview'
  file=canonical\periodization\structure.yaml id='periodization.structure.school_block'
  file=canonical\periodization\structure.yaml id='periodization.structure.perception_periodization_bridge'
  file=canonical\periodization\taper.yaml id='periodization.taper.definition'
  file=canonical\periodization\taper.yaml id='periodization.taper.volume'
  file=canonical\periodization\taper.yaml id='periodization.taper.intensity'
  file=canonical\periodization\taper.yaml id='periodization.taper.frequency'
  file=canonical\periodization\taper.yaml id='periodization.taper.duration'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.linear'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.step'
  file=canonical\periodization\taper.yaml id='periodization.taper.type.fast_exponential'
  file=canonical\periodization\taper.yaml id='periodization.taper.peak_window'
  file=canonical\periodization\taper.yaml id='periodization.taper.swim'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_7_1'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_11_2'
  file=canonical\periodization\zones.yaml id='periodization.zones.table_11_1'
  file=canonical\periodization\zones.yaml id='periodization.zones.endurance_phases'
  file=canonical\periodization\zones.yaml id='periodization.zones.swim_maglischo'
  file=canonical\periodization\zones.yaml id='periodization.zones.swim_three_zone'
  file=canonical\periodization\zones.yaml id='periodization.zones.energy_systems_primer'
  file=canonical\periodization\zones.yaml id='periodization.zones.swim_energy_by_distance'
  file=canonical\periodization\zones.yaml id='periodization.zones.swim_tid'
  file=canonical\periodization\zones.yaml id='periodization.zones.swim'
  file=canonical\periodization\zones.yaml id='periodization.zones.school_polarized'
  file=canonical\periodization\zones.yaml id='periodization.zones.olbrecht_model'
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
