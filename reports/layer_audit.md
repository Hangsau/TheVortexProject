# 三層歸屬稽核報告（Phase 1）

> 由 `tools/audit_layers.py` 產生；drift 基準 `27ffd10^`。數字是 Phase 3 閘門分母。

## 摘要

| 檢查 | 筆數 |
|---|---|
| 已發布 Vortex 頁（不含轉址） | 826 |
| 無歸屬頁 | 0 |
| P1 散文頁 | 26 |
| P3 my-site 手管／手寫頁 | 59 |
| P1 散文漂移候選（已從 canonical 移除的句段仍在散文／手管資料） | 53 |
| P2 公開頁含診斷語的頁 | 39（共 450 處） |
| 機器鍵外洩頁 | 2 |
| 外站連結 | 12 |
| 🟢／🟡 但同行無年份（散文／手管） | 89 |

## W1.1 頁面 → 層

| 目標層 | 頁數 |
|---|---|
| 呈現 | 723 |
| 應用 | 77 |
| 資料庫 | 26 |

| 來源種類 | 頁數 |
|---|---|
| canonical | 737 |
| my-site 手寫 | 1 |
| my-site 手管 | 58 |
| my-site 版型 | 1 |
| 工具 | 2 |
| 散文 | 27 |

**無歸屬頁**：無

**P1 頁**：`bridge/backstroke-perception-bridge`、`bridge/breaststroke-perception-bridge`、`bridge/butterfly-perception-bridge`、`bridge/freestyle-perception-bridge`、`bridge`、`bridge/starts-turns-bridge`、`bridge/underwater-dolphin-kick-bridge`、`instructional/backstroke-teaching-errors`、`instructional/backstroke-technical-analysis`、`instructional/breaststroke-teaching-errors`、`instructional/breaststroke-technical-analysis`、`instructional/butterfly-teaching-errors`、`instructional/butterfly-technical-analysis`、`instructional/freestyle-teaching-errors`、`instructional/freestyle-technical-analysis`、`instructional`、`instructional/starts-turns-teaching-errors`、`instructional/starts-turns-technical-analysis`、`instructional/underwater-dolphin-kick-analysis`、`instructional/underwater-dolphin-kick-errors`、`technica/backstroke-water-sense`、`technica/breaststroke-water-sense`、`technica/butterfly-water-sense`、`technica/freestyle-water-sense`、`technica`、`technica/technical-indicators-l-level`

**P3 頁**：`back`、`breast`、`fly`、`free`、`moves/back-1`、`moves/back-2`、`moves/back-3`、`moves/back-4`、`moves/back-5`、`moves/back-6`、`moves/back-7`、`moves/back-8`、`moves/back-9`、`moves/breast-1`、`moves/breast-10`、`moves/breast-11`、`moves/breast-2`、`moves/breast-3`、`moves/breast-4`、`moves/breast-5`、`moves/breast-6`、`moves/breast-7`、`moves/breast-8`、`moves/breast-9`、`moves/fly-1`、`moves/fly-2`、`moves/fly-3`、`moves/fly-4`、`moves/fly-5`、`moves/fly-6`、`moves/fly-7`、`moves/fly-8`、`moves/fly-9`、`moves/free-1`、`moves/free-2`、`moves/free-3`、`moves/free-4`、`moves/free-5`、`moves/free-6`、`moves/free-7`、`moves/free-8`、`moves`、`moves/starts-turns-1`、`moves/starts-turns-2`、`moves/starts-turns-3`、`moves/starts-turns-4`、`moves/starts-turns-5`、`moves/starts-turns-6`、`moves/starts-turns-7`、`moves/udk-1`、`moves/udk-2`、`moves/udk-3`、`moves/udk-4`、`moves/udk-5`、`moves/udk-6`、`moves/udk-7`、`starts-turns`、`udk`、`water-sense`

**P4 頁**：`workout`、`workout-studio`

## W1.2 散文漂移候選

句段在 canonical 的修訂中被刪除、現行 canonical 已無，但仍出現在散文或手管資料。屬「候選」：改寫同義、或散文本就另有語境者需人工判定。

| 檔案 | 句段 | 原 canonical 檔 |
|---|---|---|
| `Bridge/蝶式感知橋接.md` | Exit Kick / Power Kick | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式教學誤區深探.md` | 70–90% 推進力來自上踢 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/仰式教學誤區深探.md` | Hollander 等 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/仰式深度技術分析.md` | 但因不存在像自由式 hip-driven 那樣以低頻率換高 SL 的泳型策略 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 划水側被動深沉的單側主動模式 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 單次划手最大推力輸出點 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 大幅向上 forward roll | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 把回臂側肩膀盡量抬高 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 疲勞時泳者維持肩旋轉幅度 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 這個向上動作把對側肩膀壓得更深入水下 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/仰式深度技術分析.md` | 進入更有力的生物力學位置 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/出發與轉身技術分析.md` | 超出最佳力–長度曲線 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/出發與轉身技術分析.md` | 超過 0.75 m 無額外效益 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/出發與轉身教學誤區深探.md` | 出去速度 = 推蹬力量 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/水下蝶腳教學誤區深探.md` | 有效推進力來自踝關節柔韌性與上踢速度 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/水下蝶腳教學誤區深探.md` | 與魚類的最優推進比例相符 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | CFD 分析真實手部模型 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | → 啟動對側身體滾轉 → 髖部被動跟隨 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | 指尖間距約 3.2 mm | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | 推水末段 → 肩胛肌群收縮 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | 每次減速都是推進力損失 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式教學誤區深探.md` | 阻力係數提升 2–5% | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/自由式深度技術分析.md` | 旋轉的感知目標是肩胛骨的動作 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式教學誤區深探.md` | outsweep展開時 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式教學誤區深探.md` | 但這是腳掌翻轉到位的功能性指標 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式教學誤區深探.md` | 手腳的推進階段必須交替發生 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式教學誤區深探.md` | 有支撐力的時候就開始吸氣 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式教學誤區深探.md` | 而不是等到結束才呼吸 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蛙式深度技術分析.md` | 且與多數業餘訓練習慣相反 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蛙式深度技術分析.md` | 水面上方回臂可進一步降低阻力 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蛙式深度技術分析.md` | 踝關節柔韌性主要靠軟組織訓練可以改善 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蛙式深度技術分析.md` | 雙臂保持伸直向外展至肩寬外 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蝶式教學誤區深探.md` | EVF入水後直線加速後推 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | S形是觀察角度造成的錯覺 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | insweep → upsweep 階段自然產生的 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | 其實是手臂在三維空間移動 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | 刻意的鑰匙孔路徑增加橫向阻力並拉長外划時間 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | 現代生物力學分析與高速影像顯示 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | 而非刻意設計的手部路徑 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式教學誤區深探.md` | 踝關節蹠屈柔韌性是蝶腿推進的 | `canonical/instructional/teaching-errors.yaml` |
| `Instructional/蝶式深度技術分析.md` | Exit Kick / Power Kick | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蝶式深度技術分析.md` | 且與多數業餘訓練習慣相反 | `canonical/instructional/technical-analysis.yaml` |
| `Instructional/蝶式深度技術分析.md` | 雙臂保持伸直向外展至肩寬外 | `canonical/instructional/technical-analysis.yaml` |
| `Technica/仰式水感框架.md` | 拳頭游 vs 張開手速度差縮小至 5 秒以內 | `canonical/technica/water-sense-levels.yaml` |
| `Technica/仰式水感框架.md` | 柔韌性訓練優先於力量訓練 | `canonical/technica/water-sense-levels.yaml` |
| `Technica/技術指標_L級對應框架.md` | SR 與速度負相關消失 | `canonical/technica/l-indicators.yaml` |
| `Technica/技術指標_L級對應框架.md` | 拳頭游 vs 開手速度差 | `canonical/technica/l-indicators.yaml` |
| `Technica/技術指標_L級對應框架.md` | 高 SR 下 SL 不下降 | `canonical/technica/l-indicators.yaml` |
| `Technica/自由式水感框架.md` | 入水後手速是否逐漸加快　拳頭游 vs 張開手速度差縮小至 5 秒以內 | `canonical/technica/water-sense-levels.yaml` |
| `Technica/自由式水感框架.md` | 拳頭游 vs 張開手速度差縮小至 5 秒以內 | `canonical/technica/water-sense-levels.yaml` |
| `Technica/蝶式水感框架.md` | 拳頭游速度達開手游 80% | `canonical/technica/water-sense-levels.yaml` |
| `my-site/data/vortex/back.yaml` | 柔韌性訓練優先於力量訓練 | `canonical/technica/water-sense-levels.yaml` |
| `my-site/data/vortex/free.yaml` | 每次減速都是推進力損失 | `canonical/instructional/teaching-errors.yaml` |

## W1.3 公開頁診斷語

| 頁 | 命中 |
|---|---|
| `technica/freestyle-water-sense` | A/B/C 型×54、三型×10、診斷問題×3 |
| `technica/backstroke-water-sense` | A/B/C 型×56、三型×6、診斷問題×3 |
| `technica/breaststroke-water-sense` | A/B/C 型×48、三型×10、診斷問題×4 |
| `technica/butterfly-water-sense` | A/B/C 型×48、三型×10、診斷問題×4 |
| `instructional/freestyle-teaching-errors` | A/B/C 型×32 |
| `instructional/butterfly-teaching-errors` | A/B/C 型×24 |
| `bridge/butterfly-perception-bridge` | A/B/C 型×19 |
| `instructional/breaststroke-teaching-errors` | A/B/C 型×17 |
| `bridge/backstroke-perception-bridge` | A/B/C 型×16 |
| `bridge/breaststroke-perception-bridge` | A/B/C 型×14 |
| `bridge/underwater-dolphin-kick-bridge` | A/B/C 型×13 |
| `bridge/freestyle-perception-bridge` | A/B/C 型×9 |
| `technica/technical-indicators-l-level` | A/B/C 型×8、三型×1 |
| `instructional/backstroke-teaching-errors` | A/B/C 型×8 |
| `bridge/starts-turns-bridge` | A/B/C 型×6 |
| `instructional/underwater-dolphin-kick-errors` | A/B/C 型×4 |
| `errors/back-err5` | A/B/C 型×1 |
| `errors/back-err6` | A/B/C 型×1 |
| `errors/back-err7` | A/B/C 型×1 |
| `errors/back-err8` | A/B/C 型×1 |
| `errors/back-err9` | A/B/C 型×1 |
| `levels/free-l3` | A/B/C 型×1 |
| `moves/back-2` | A/B/C 型×1 |
| `moves/back-4` | A/B/C 型×1 |
| `moves/back-5` | A/B/C 型×1 |
| `moves/breast-11` | A/B/C 型×1 |
| `moves/breast-5` | A/B/C 型×1 |
| `moves/fly-4` | A/B/C 型×1 |
| `moves/fly-5` | A/B/C 型×1 |
| `moves/fly-7` | A/B/C 型×1 |
| `moves/fly-8` | A/B/C 型×1 |
| `moves/free-3` | A/B/C 型×1 |
| `moves/free-5` | A/B/C 型×1 |
| `moves/free-6` | A/B/C 型×1 |
| `moves/free-8` | A/B/C 型×1 |
| `moves/starts-turns-1` | A/B/C 型×1 |
| `moves/udk-1` | A/B/C 型×1 |
| `moves/udk-2` | A/B/C 型×1 |
| `moves/udk-4` | A/B/C 型×1 |

## W1.4 機器鍵／外站連結／確定性無年份

**機器鍵外洩**

- `movement`：cross_ref
- `tech/udk-tech-14`：cross_ref

**外站連結**

- `instructional/freestyle-teaching-errors` → https://www.usms.org/fitness-and-training/articles-and-videos/articles/freestyle-demystified
- `instructional/freestyle-teaching-errors` → https://blog.tritonwear.com/how-to-have-a-flawless-freestyle-swimming-recovery
- `instructional/freestyle-teaching-errors` → https://chicagobluedolphins.com/article-freestyle-straight-arm-recovery/
- `instructional/freestyle-teaching-errors` → https://tritrainingharder.com/blog/2021/6/blog-is-straight-arm-better-than-high-elbow
- `instructional/freestyle-teaching-errors` → https://www.usms.org/fitness-and-training/articles-and-videos/articles/the-right-and-wrong-time-to-have-high-elbows-on-freestyle
- `instructional/freestyle-teaching-errors` → https://chilitri.com/blog/karenparnell01@hotmail.com/bent-elbow-vs-straight-arm-recovery-which-is-best-for-you
- `instructional/freestyle-teaching-errors` → https://tri-coaching.co.uk/2015/04/21/freestyle-recovery/
- `instructional/freestyle-teaching-errors` → https://theraceclub.com/aqua_note/common-mistakes-from-the-freestyle-hand-entry/
- `instructional/freestyle-teaching-errors` → https://theraceclub.com/aqua_note/common-mistakes-from-the-freestyle-hand-entry/
- `instructional/freestyle-teaching-errors` → https://www.swimmingworldmagazine.com/news/science-of-performance-hand-entry/
- `instructional/freestyle-teaching-errors` → https://www.yourswimlog.com/how-to-improve-freestyle-hand-entry/
- `instructional/freestyle-teaching-errors` → https://rocketswim.com/four-phases-of-freestyle-arm-stroke/

**🟢／🟡 同行無年份**

| 檔案 | 行 | 內容 |
|---|---|---|
| `Instructional/仰式教學誤區深探.md` | 5 | > 確定性標記：推導🔵 / 近期文獻🟢 / 舊文獻🟡 / 教練觀測🟠 / 未查證假設🔴 |
| `Instructional/出發與轉身技術分析.md` | 48 | **Grab start vs Track start 數據** 🟢： |
| `Instructional/出發與轉身技術分析.md` | 131 | **起跳角度數據** 🟢： |
| `Instructional/出發與轉身技術分析.md` | 139 | 以上數據收錄於系統性綜述：Biomechanical Analysis of the Swim-Start: A Review（PMC3990873）🟢。 |
| `Instructional/出發與轉身技術分析.md` | 180 | **入水角度與入水點** 🟢： |
| `Instructional/出發與轉身技術分析.md` | 186 | - 三變數合計解釋成績變異的 **86.1%** 🟢 |
| `Instructional/出發與轉身技術分析.md` | 240 | **髖部高度是關鍵變數** 🟢（The Backstroke Swimming Start: State of the Art，PMC4234766）： |
| `Instructional/出發與轉身技術分析.md` | 245 | **仰式出發台（Backstroke Ledge）的效益** 🟢（PubMed 28975846，OBL2 研究）： |
| `Instructional/出發與轉身技術分析.md` | 326 | 推蹬出水速度由三個因素共同決定 🟢： |
| `Instructional/出發與轉身技術分析.md` | 330 | ／ 推蹬力道 ／ 解釋轉身成績約 **42%** 的變異 ／ PMC6409673 🟢 ／ |
| `Instructional/出發與轉身技術分析.md` | 331 | ／ 推蹬方向（力向量對齊重心）／ 與出水速度相關 **r = 0.76**（p < 0.001）／ PubMed 40252339 🟢 ／ |
| `Instructional/出發與轉身技術分析.md` | 386 | **推蹬方向與出水速度** 🟢（PubMed 40252339）： |
| `Instructional/出發與轉身技術分析.md` | 389 | **最優觸牆膝蓋屈曲角度** 🟢（PMC6409673；Kinetic Analysis of Swimming Flip-Turn Push-Off Tech |
| `Instructional/出發與轉身技術分析.md` | 477 | **最優觸牆深度** 🟢（PMC8960438，Biomechanical Features of Backstroke to Breaststroke Tra |
| `Instructional/出發與轉身技術分析.md` | 506 | **水下滑行深度** 🟢（PMC8960438）：最優滑行深度 0.4–0.6 m（來自背→蛙轉身研究，蛙式 pullout 適用性可參考）。 |
| `Instructional/出發與轉身技術分析.md` | 565 | **FINA/World Aquatics 規則精確解讀** 🟢（FINA Swimming Technical Rules SW 6.4；USA Swimmi |
| `Instructional/出發與轉身技術分析.md` | 596 | **動作力學差異** 🟢（PMC7918682）： |
| `Instructional/出發與轉身技術分析.md` | 604 | **關鍵研究發現** 🟢（PMC7918682）： |
| `Instructional/出發與轉身技術分析.md` | 658 | - 速度關鍵：**上踢的腳尖峰值速度** 🟢 |
| `Instructional/出發與轉身教學誤區深探.md` | 38 | 以上數據收錄於系統性綜述：Biomechanical Analysis of the Swim-Start: A Review（PMC3990873）🟢。 |
| `Instructional/出發與轉身教學誤區深探.md` | 51 | 起跳目標是最大化水平速度，而非最大化飛行高度或距離。精英選手的低角度起跳看起來「沒有跳很高」，但入水後速度更快 🟢。 |
| `Instructional/出發與轉身教學誤區深探.md` | 73 | > — Contribution of hand and foot force to take-off velocity for the kick-start（ |
| `Instructional/出發與轉身教學誤區深探.md` | 84 | 現代 Kick Start 的核心是後腳水平蹬出，前腳控制起跳角度。慣用腳放前，是讓它負責**精準控制起跳方向**，而非「主力水平發力」🟢（PubMed 271 |
| `Instructional/出發與轉身教學誤區深探.md` | 128 | 仰式起跳研究直接確認：**起跳角度越大，成績越差** 🟢（The Backstroke Swimming Start: State of the Art，PMC |
| `Instructional/出發與轉身教學誤區深探.md` | 135 | **真正的關鍵變數是髖部高度**（hip height），而非背部弧線的幅度 🟢（PMC4234766）： |
| `Instructional/出發與轉身教學誤區深探.md` | 144 | 仰式起跳的目標同樣是水平速度最大化，關鍵是**髖部高度**而非弧線幅度。弧線是起跳的結果，不是目標。判斷標準應是「入水後速度保留」，而非「背部弧線視覺感」🔵 + |
| `Instructional/出發與轉身教學誤區深探.md` | 251 | 研究直接確認：蛙式最優觸牆深度為 **30–40 cm** 🟢（Biomechanical Features of Backstroke to Breastst |
| `Instructional/出發與轉身教學誤區深探.md` | 267 | 正確的腳找牆邏輯，是透過縮腿路徑（腿從身體下方收回），讓腳自然落在 30–40 cm 的最優深度，而非靠身體主動下沉來補位 🔵 + 🟢。 |
| `Instructional/出發與轉身教學誤區深探.md` | 291 | > — Kinetic Analysis of Swimming Flip-Turn Push-Off Techniques（PMC6409673）🟢 |
| `Instructional/出發與轉身教學誤區深探.md` | 296 | > — Can the tumble turn performance be improved by aligning the push-off force v |
| `Instructional/出發與轉身教學誤區深探.md` | 307 | 三個因素並重，但實際教學中，**推蹬方向**和**流線型時機**往往比單純腿力更容易改善且效益更高 🔵 + 🟢。 |
| `Instructional/出發與轉身教學誤區深探.md` | 310 | 轉身訓練的優先順序：流線型時機 → 推蹬方向 → 推蹬力道。在流線型和方向不到位的前提下強化腿力，是邊際效益最低的投資 🔵 + 🟢（PMC6409673；Pub |
| `Instructional/水下蝶腳技術分析.md` | 50 | ／ ≥ 0.7 m ／ 波浪阻力 < 5% 總阻力，效益趨於穩定 ／ ScienceDirect 波浪阻力研究 🟢 ／ |
| `Instructional/水下蝶腳技術分析.md` | 79 | ／ 核心（腹肌/下背）／ 啟動並穩定整個波動 ／ 能量的發動機；核心力量提升使踝關節力量增加 25% 🟢 ／ |
| `Instructional/水下蝶腳技術分析.md` | 85 | 🟢（phantomlattice.com 生物力學分析；yourswimlog 核心力量研究） |
| `Instructional/水下蝶腳技術分析.md` | 87 | **核心在不同踢腿相的時序激活** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 100 | **下踢末段的渦流噴射** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 103 | **下踢→上踢過渡的渦流回收（Vortex Recapture）** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 134 | **動作序列** 🔵 + 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 141 | > — Kinematic differences research（ResearchGate）🟢 |
| `Instructional/水下蝶腳技術分析.md` | 146 | **膝蓋彎曲的核心矛盾** 🟢（The Race Club）： |
| `Instructional/水下蝶腳技術分析.md` | 160 | **為什麼上踢是 UDK 速度的關鍵預測變數** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 165 | **上踢的三重貢獻** 🟢（yourswimlog）： |
| `Instructional/水下蝶腳技術分析.md` | 178 | **現實情況** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 208 | **量化數據** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 246 | **衰退主因**：接近水面時**軀幹傾斜增加 + 矢狀面身體波幅變大**（姿態崩解），而非海豚踢動作本身的關節活動度改變——除髖關節外，各關節 ROM 無顯著變 |
| `Instructional/水下蝶腳技術分析.md` | 261 | **規則：滑到個人「流線滑行—海豚踢」淨力交叉速度，立刻開始踢。** 🟢 |
| `Instructional/水下蝶腳技術分析.md` | 394 | ／ 長水道中距離，個人化優化 ／ 主動 UDK，速度仍高 ／ 混合 ／ 🟡 個體差異大 ／ |
| `Instructional/水下蝶腳技術分析.md` | 407 | 🟢（SwimSwam "Why dolphin kick is faster on your back"；WKU Digital Commons Kinemat |
| `Instructional/水下蝶腳技術分析.md` | 422 | > — SwimSwam 🟢 |
| `Instructional/水下蝶腳技術分析.md` | 456 | **Monofin（單蛙鞋）訓練** 🟢（yourswimlog monofin 研究）： |
| `Instructional/水下蝶腳技術分析.md` | 465 | **計時反饋** 🟢： |
| `Instructional/水下蝶腳技術分析.md` | 470 | **柔韌性訓練**（去除硬體限制）🟢（PubMed 24984154）： |
| `Instructional/水下蝶腳技術分析.md` | 482 | 🟢（Elite Japanese swimmer study, 4-month intervention；yourswimlog）： |
| `Instructional/水下蝶腳教學誤區深探.md` | 96 | UDK 的目標是「踢腿對稱性（sagittal kick symmetry）」——上踢與下踢各自高效，而非只強化下踢。上踢速度是 UDK 效率的關鍵預測變數 🟢 |
| `Instructional/水下蝶腳教學誤區深探.md` | 113 | > — Gonjo et al.（PubMed 28605694）🟢 |
| `Instructional/水下蝶腳教學誤區深探.md` | 117 | 最優踢頻是**個體特異的**——受身體形態、踝關節柔韌性、核心力量影響，沒有跨選手通用數字 🔵 + 🟢。 |
| `Instructional/水下蝶腳教學誤區深探.md` | 202 | ／ ≥ 0.7 m ／ 阻力趨於穩定，**波浪阻力已 < 5% 總阻力** ／ ScienceDirect 波浪阻力研究 🟢 ／ |
| `Instructional/水下蝶腳教學誤區深探.md` | 208 | 實用深度約 **0.4–0.6 m**，超過 0.75 m 沒有追加效益。推牆後的流線型深度以 0.4–0.6 m 為目標，不需要特別往深處去 🟢。 |
| `Instructional/水下蝶腳教學誤區深探.md` | 237 | 轉身後，第一下上踢應在離牆後**盡快啟動**，而非等待滑行。目標是最小化從推牆到第一踢之間的速度損失窗口 🟠 + 🟢。 |
| `Instructional/水下蝶腳教學誤區深探.md` | 266 | 水下踢腿的終止點應是速度交叉點，而非固定距離。提升水下踢腿速度（讓交叉點更遠）才是正確訓練方向，而非強迫延長距離 🔵 + 🟢。 |
| `Instructional/水下蝶腳教學誤區深探.md` | 313 | > — SwimSwam / Kinematic Comparison（WKU Digital Commons）🟢 |
| `Instructional/水下蝶腳教學誤區深探.md` | 325 | 仰式 UDK 的技術指導應強調「對抗浮力的下踢感」和「速度穩定感」，而非套用俯式的「向下爆發感」口令 🔵 + 🟢。 |
| `Instructional/水下蝶腳教學誤區深探.md` | 407 | ／ **髖屈曲角度** ／ 蝶式第二踢峰值**小於** UDK 🟢 ／ 較大（三維分析研究確認）／ |
| `Instructional/水下蝶腳教學誤區深探.md` | 411 | 🟢 三維分析研究：ResearchGate, Maffulli et al. / 三維分析髖膝關節 |
| `Instructional/自由式教學誤區深探.md` | 7 | > 確定性標記：🔵推導 · 🟢近期文獻 · 🟡有效舊文獻 · 🟠教練觀測 · 🔴未查證假設 |
| `Instructional/自由式教學誤區深探.md` | 109 | **肩部安全補充** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 168 | **文獻支持** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 178 | **額外文獻** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 240 | **歷史背景** 🟡 |
| `Instructional/自由式教學誤區深探.md` | 243 | **為什麼是誤區** 🟢🔵 |
| `Instructional/自由式教學誤區深探.md` | 251 | **文獻** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 280 | **文獻 / 教練觀測支持** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 379 | **文獻 / 教練觀測支持** 🟡 |
| `Instructional/自由式教學誤區深探.md` | 510 | **文獻 / 教練觀測支持** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 557 | **文獻 / 教練觀測支持** 🟢 |
| `Instructional/自由式教學誤區深探.md` | 670 | ／ Biomechanical Considerations in the Competitive Swimmer's Shoulder ／ PMC343887 |
| `Instructional/蛙式教學誤區深探.md` | 113 | **為什麼是誤區？** 🟢🟠 |
| `Instructional/蛙式教學誤區深探.md` | 254 | **為什麼是誤區？** 🔵🟢 |
| `Instructional/蝶式深度技術分析.md` | 18 | > **【🟡 有效舊文獻】** 舊研究但物理原理至今仍被引用 |
| `Instructional/蝶式深度技術分析.md` | 187 | ／ ① 外划 Outsweep ／ 🟢 文獻 ／ 肩膀內旋，手掌轉45°，雙臂保持伸直向外展至肩寬外，形成Y字形。速度平穩，不加速 ／ 定位：將手移至最佳捕水起 |
| `Instructional/蝶式深度技術分析.md` | 191 | ／ ⑤ 回臂 Recovery ／ 🟢 文獻 ／ 手掌合攏後快速出水，低位弧線前移，掌心朝外。應在最短時間內完成 ／ 波動重置------能量從水下移交空中，初 |
| `my-site/next/content/vortex/water-sense.md` | 37 | ### 神經科學層次 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 78 | ### 學習水感的四個能力階段 🟡 |
| `my-site/next/content/vortex/water-sense.md` | 177 | ### SWOLF：最實用的無儀器效率指標 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 192 | ### SPL（每趟划手數） 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 227 | ### 1. 製造大誤差，而非漸進微調 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 237 | ### 2. 交替練習，而非連續練習 🟢 |
| `my-site/next/content/vortex/water-sense.md` | 249 | ### 4. 暫時回到認知學習階段 🟡 |
