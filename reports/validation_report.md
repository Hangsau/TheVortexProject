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

## W001 — `cross_ref` 為自由文字、無法解析成穩定 ID（S4 待辦）

**WARN，共 61 筆**

  file=canonical\instructional\teaching-errors.yaml id='free.err1' public.cross_ref (120 chars): '技術分析 §2.1、§3.1（三種風格對應三種回臂策略）'
  file=canonical\instructional\teaching-errors.yaml id='free.err5' public.cross_ref (120 chars): '技術分析 §3.1（晚期回臂）'
  file=canonical\instructional\teaching-errors.yaml id='free.err10' public.cross_ref (120 chars): '技術分析 §3.1（後象限推進）'
  file=canonical\instructional\teaching-errors.yaml id='free.err12' public.cross_ref (120 chars): '技術分析 §肆（踢水機制）'
  file=canonical\instructional\teaching-errors.yaml id='free.err15' public.cross_ref (120 chars): '技術分析 §伍（身體旋轉）'
  file=canonical\instructional\teaching-errors.yaml id='free.err17' public.cross_ref (120 chars): '技術分析 §伍（Coupling 能量）'
  file=canonical\instructional\teaching-errors.yaml id='free.err18' public.cross_ref (120 chars): '技術分析 §陸（頭部位置與弓形波）'
  file=canonical\instructional\teaching-errors.yaml id='free.err20' public.cross_ref (120 chars): '技術分析 §柒（划頻 vs 划距）'
  file=canonical\instructional\teaching-errors.yaml id='free.err21' public.cross_ref (120 chars): '技術分析 §參（六階段划手週期 ①升力相）'
  file=canonical\instructional\teaching-errors.yaml id='free.err24' public.cross_ref (120 chars): 'free.tech.7（S 形划水歷史錯誤）、back.err2（仰式同樣誤區）'
  file=canonical\instructional\teaching-errors.yaml id='free.err25' public.cross_ref (120 chars): 'free.tech.9（EVF 核心物理）、back.err3（仰式對應誤區）'
  file=canonical\instructional\teaching-errors.yaml id='back.err1' public.cross_ref (120 chars): '技術分析 §旋轉機制'
  file=canonical\instructional\teaching-errors.yaml id='back.err6' public.cross_ref (120 chars): '教學誤區 §back.err3（深度與肘位）'
  file=canonical\instructional\teaching-errors.yaml id='back.err8' public.cross_ref (120 chars): '教學誤區 §back.err5（踢水方向）'
  file=canonical\instructional\teaching-errors.yaml id='back.err9' public.cross_ref (120 chars): '教學誤區 §back.err1（旋轉壓制造成的張力）'
  file=canonical\instructional\teaching-errors.yaml id='back.err13' public.cross_ref (120 chars): 'free.tech.33（螺旋筋膜線是 coupling 解剖基礎）'
  file=canonical\instructional\teaching-errors.yaml id='back.err15' public.cross_ref (120 chars): 'free.tech.32（octane 三層光譜）、free.tech.29（手砸水 = 肩旋轉同源）'
  file=canonical\instructional\teaching-errors.yaml id='back.err17' public.cross_ref (120 chars): 'starts-turns.err10（起跳抬頭二元口令的對應討論）'
  file=canonical\instructional\teaching-errors.yaml id='breast.err4' public.cross_ref (120 chars): '技術分析 §3.2'
  file=canonical\instructional\teaching-errors.yaml id='breast.err5' public.cross_ref (120 chars): '技術分析 §2.1'
  file=canonical\instructional\teaching-errors.yaml id='breast.err11' public.cross_ref (120 chars): '技術分析 §2.3'
  file=canonical\instructional\teaching-errors.yaml id='breast.err15' public.cross_ref (120 chars): 'free.tech.9（EVF 通用原理）、fly.tech.11（Insweep 是最大推進）'
  file=canonical\instructional\teaching-errors.yaml id='breast.err17' public.cross_ref (120 chars): '自由式 FrBr3（連續涓流吐氣 drill）通用呼吸原則'
  file=canonical\instructional\teaching-errors.yaml id='fly.err1' public.cross_ref (120 chars): '技術分析 伍5.1（外划功能重建）；伍5.1 五階段划水'
  file=canonical\instructional\teaching-errors.yaml id='fly.err4' public.cross_ref (120 chars): '技術分析 柒7.2 Recovery物理目標表；捌8 疲勞崩潰第二環'
  file=canonical\instructional\teaching-errors.yaml id='fly.err6' public.cross_ref (120 chars): '技術分析 貳2.1 波動vs擺動；貳2.2 完整動力傳遞鏈'
  file=canonical\instructional\teaching-errors.yaml id='fly.err7' public.cross_ref (120 chars): '技術分析 拾壹11.1（踝關節蹠屈柔韌性）'
  file=canonical\instructional\teaching-errors.yaml id='fly.err8' public.cross_ref (120 chars): '技術分析 參3.1-3.3 兩踢功能不對稱矩陣'
  file=canonical\instructional\teaching-errors.yaml id='fly.err9' public.cross_ref (120 chars): '技術分析 參3.2 第二踢；肆4 連動鏈閉環'
  file=canonical\instructional\teaching-errors.yaml id='fly.err10' public.cross_ref (120 chars): '技術分析 貳2.3 幅度vs頻率策略表；拾壹11.3 不同距離技術差異化'
  file=canonical\instructional\teaching-errors.yaml id='fly.err11' public.cross_ref (120 chars): '技術分析 貳2.2 動力傳遞鏈；陸6.1 低頭：波動觸發器'
  file=canonical\instructional\teaching-errors.yaml id='fly.err12' public.cross_ref (120 chars): '技術分析 陸6.2 抬頭呼吸；陸6.3 完整呼吸時序；捌8 疲勞崩潰第三環'
  file=canonical\instructional\teaching-errors.yaml id='fly.err14' public.cross_ref (120 chars): '技術分析 拾壹11.3 不同距離技術差異化'
  file=canonical\instructional\teaching-errors.yaml id='udk.err6' public.cross_ref (120 chars): '技術分析 §陸（UDK vs 蝶式踢腿對照表）'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err1' public.cross_ref (120 chars): '技術分析 §壹 1.2 推蹬階段：起跳角度數據（精英 21–27°）'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err2' public.cross_ref (120 chars): '技術分析 §壹 1.3 Kick Start 變體：前後腳角色重新分配'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err3' public.cross_ref (120 chars): '技術分析 §壹 1.2 入水點：水平速度是主要預測變數'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err4' public.cross_ref (120 chars): '技術分析 §壹 1.4 仰式起跳'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err5' public.cross_ref (120 chars): '技術分析 §貳 2.3/2.4 接近與旋轉：完整最後一划'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err6' public.cross_ref (120 chars): '技術分析 §貳 2.1 接觸與推蹬：流線型應在觸牆前就位'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err7' public.cross_ref (120 chars): '技術分析 §貳 2.2 接近與旋轉：🔴 旗幟計步系統'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err8' public.cross_ref (120 chars): '技術分析 §貳 2.3/2.4 接觸與推蹬：觸牆深度'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err9' public.cross_ref (120 chars): '技術分析 §貳 通用：流線型品質與推蹬方向同等重要'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err10' public.cross_ref (120 chars): 'starts-turns.tech.4（兩派並陳分析）'
  file=canonical\instructional\teaching-errors.yaml id='starts-turns.err14' public.cross_ref (120 chars): 'starts-turns.tech.44（自由式 Breakout 七要點，含「第一划不換氣」）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.3' public.cross_ref (120 chars): 'free.tech.13（划頻 vs 划距的生理條件分析）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.9' public.cross_ref (120 chars): 'free.tech.10（前鋸肌硬體邊界）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.26' public.cross_ref (120 chars): 'free.tech.1（無唯一最優技術的框架前提）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.32' public.cross_ref (120 chars): 'free.tech.4/5/6（hip/shoulder/hybrid 風格的對應位置）、free.tech.16（晚期回臂作為 coupling 動作）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.33' public.cross_ref (120 chars): 'free.tech.10（前鋸肌）、free.tech.15（菱形肌啟動旋轉）、free.tech.16（coupling）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.34' public.cross_ref (120 chars): 'free.tech.32（octane recovery 是 streamline 偏離程度的選擇）'
  file=canonical\instructional\technical-analysis.yaml id='free.tech.35' public.cross_ref (120 chars): 'free.tech.4/5/6（hip/shoulder/hybrid 風格決定起點位置）'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.28' public.cross_ref (120 chars): 'free.tech.32（octane 三層光譜物理基礎）、back.err15（誤套導致的傷害風險）'
  file=canonical\instructional\technical-analysis.yaml id='back.tech.29' public.cross_ref (120 chars): 'back.err11（小指先入水執著常引發入水偏外）、Bk22（泳鏡平衡）'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.1' public.cross_ref (120 chars): '四式推進機制對比見 fly.tech.2'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.12' public.cross_ref (120 chars): '2024–2025 外划幅度縮小趨勢已成為精英教學主流演進方向'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.17' public.cross_ref (120 chars): '呼吸策略的決定因子是換氣方式，不是換氣次數（見 fly.tech.30）'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.24' public.cross_ref (120 chars): '四式踝關節柔韌性結論一致，見 fly.tech.34'
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.36' public.cross_ref (120 chars): 'free.tech.34（自由式 streamline 基準姿態對照）、fly.tech.10（IVV 與波動效率）'
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.35' public.cross_ref (120 chars): 'breast.err16（wave style 誤套到 flat style 適合者）'
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.2' public.cross_ref (120 chars): 'starts-turns.tech.41（Track Start 重心策略）'

---

## W002 — `certainty` 為 green 或 yellow 但沒有 `source_ids`（S3 待辦）

**WARN，共 88 筆**

  file=canonical\instructional\technical-analysis.yaml id='free.tech.3' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.27' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.28' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.10' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.11' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.12' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.13' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.15' public.mechanism.certainty=yellow 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.19' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.20' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.21' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.23' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.24' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.25' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='free.tech.35' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.1' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.2' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.5' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.11' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.15' public.mechanism.certainty=yellow 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.16' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.17' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.18' public.mechanism.certainty=yellow 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.22' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.24' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.25' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='back.tech.27' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.3' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.5' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.6' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.7' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.8' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.9' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.11' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.12' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.14' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.17' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.18' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.19' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.22' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.23' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.24' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.25' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.27' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.28' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.30' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='breast.tech.31' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.3' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.7' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.11' public.mechanism.certainty=yellow 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.13' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.17' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.24' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.31' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.32' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='fly.tech.35' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.3' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.5' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.6' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.7' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.10' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.12' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.13' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.15' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.17' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.25' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.26' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.27' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='udk.tech.28' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.3' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.42' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.7' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.9' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.12' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.14' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.15' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.17' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.21' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.22' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.25' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.26' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.27' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.28' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.29' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.33' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.40' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.45' public.mechanism.certainty=green 無 source_ids
  file=canonical\instructional\technical-analysis.yaml id='starts-turns.tech.46' public.mechanism.certainty=green 無 source_ids

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

## W004 — 欄位名為 `*_link` 但值為散文（schema 債）

**WARN，共 20 筆**

> **schema 債說明**：以下欄位名稱宣稱是 link，但值為散文。修法是將每筆拆成 `*_link`（ID 陣列）+ `*_note`（散文說明），並修改 `canonical/health/drafts/*.yaml` 再重跑 `tools/build_injuries.py`。**不可直接改 `canonical/health/injuries.yaml`**（promoted artifact，檔頭寫明勿手改）。

  file=canonical\health\injuries.yaml id='swimmers-shoulder' links.mechanism_link 散文前120字: '前鋸肌耐力是 EVF（早期垂直前臂）的硬體前提，疲勞後肩胛失穩→捕水崩潰'
  file=canonical\health\injuries.yaml id='swimmers-shoulder' links.technical_link 散文前120字: 'free.tech.10 前鋸肌硬體邊界 / free 疲勞崩潰順序第③步'
    （候選 ID: free.tech.10）
  file=canonical\health\injuries.yaml id='swimmers-shoulder' links.perception_link 散文前120字: 'L4–L6 手感與全身張力'
  file=canonical\health\injuries.yaml id='breaststrokers-knee' links.mechanism_link 散文前120字: '踢腿外翻負荷與髖外旋代償可接『硬體邊界 vs 感知缺陷』判斷(髖活動度=硬體)'
  file=canonical\health\injuries.yaml id='breaststrokers-knee' links.technical_link 散文前120字: '蛙式踢腿技術分析(外翻角/髖帶動)——待對應 canonical technical 條目'
  file=canonical\health\injuries.yaml id='breaststrokers-knee' links.perception_link 散文前120字: 'L2–L4 腳感層(踢腿節律與蹬夾感知)'
  file=canonical\health\injuries.yaml id='cold-water-shock' links.perception_link 散文前120字: '可接 L0 呼吸感知(冷水喘氣反射的生理意義)'
  file=canonical\health\injuries.yaml id='drowning' links.perception_link 散文前120字: '可接 L0 呼吸感知層作為水安全教育素材(非技術介入)'
  file=canonical\health\injuries.yaml id='shallow-water-blackout' links.perception_link 散文前120字: '可接 L0 呼吸感知層：閉氣與換氣衝動的生理意義屬呼吸感知教育素材'
  file=canonical\health\injuries.yaml id='sipe' links.perception_link 散文前120字: '可接 L0 呼吸感知/配速感知教育(辨識異常呼吸窘迫 vs 正常喘)'
  file=canonical\health\injuries.yaml id='exercise-amenorrhea' links.mechanism_link 散文前120字: 'female-athlete-triad'
  file=canonical\health\injuries.yaml id='female-athlete-triad' links.mechanism_link 散文前120字: 'red-s'
  file=canonical\health\injuries.yaml id='stress-fracture-swimmer' links.mechanism_link 散文前120字: 'swimmer-low-bone-density'
  file=canonical\health\injuries.yaml id='swimmer-low-bone-density' links.mechanism_link 散文前120字: 'female-athlete-triad'
  file=canonical\health\injuries.yaml id='diving-cervical-injury' links.technical_link 散文前120字: '競賽出發台入水角度技術(racing start)——與出發台撞擊傷共享預防'
  file=canonical\health\injuries.yaml id='flip-turn-wall-push' links.technical_link 散文前120字: '翻滾轉身技術——時序與足位精準度直接影響受傷風險'
  file=canonical\health\injuries.yaml id='starting-block-impact' links.technical_link 散文前120字: '出發台 racing start 技術——與跳水頸椎傷共享水深/角度預防'
  file=canonical\health\injuries.yaml id='salter-harris-physeal-fracture' links.mechanism_link 散文前120字: 'diving-cervical-injury'
  file=canonical\health\injuries.yaml id='scheuermann-kyphosis' links.mechanism_link 散文前120字: 'extension-low-back-pain'
  file=canonical\health\injuries.yaml id='youth-swimmer-apophysitis' links.mechanism_link 散文前120字: 'rotator-cuff-tendinopathy'

---

## W005 — `links` 下未知子鍵（未歸類為 ID 參照類、詞彙參照類或已知自由文字類）

**WARN，共 0 筆**

（無）

---
