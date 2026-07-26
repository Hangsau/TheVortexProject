# Vortex 知識地圖 KNOWLEDGE MAP

> 自動生成於 2026-07-26 by `tools/build_knowledge_map.py`。重跑：`python tools/build_knowledge_map.py`
> 確定性圖例：🔵 推導 / 🟢 近期文獻 / 🟡 舊文獻 / 🟠 教練觀測 / 🔴 待查

這份地圖是查內容、找缺口、看哪些條目該更新的單一入口。
- **想加新內容前**：先掃對應章節，看是否已有重複或相近條目
- **想更新舊內容時**：濾出 🟡/🔴 的條目作為優先候選
- **想做新舊觀念對比時**：用 ID 去 grep canonical/ 取得完整內容

---

## 摘要

| 章節 | 條目數 | 備註 |
|---|---|---|
| `technical-analysis` | 207 | 泳式分布：{'free': 35, 'back': 29, 'breast': 32, 'fly': 36, 'udk': 29, 'starts-turns': 46}；確定性：{'🔵': 86, '🟢': 84, '🟠': 33, '🟡': 4} |
| `teaching-errors` | 102 | 泳式分布：{'free': 25, 'back': 17, 'breast': 17, 'fly': 16, 'udk': 13, 'starts-turns': 14} |
| `l-indicators` | 47 | L0–L6 各泳式感知指標 |
| `water-sense-levels` | 26 | 26 個感知級別 |
| `development/matrix` | 16 | ADM 4 支柱 × 4 階段 = 16 格 |
| `development/technical-standards` | 22 | 技術基準 |
| `periodization/structure` | 9 | 各節點 |
| `periodization/taper` | 3 | 各節點 |
| `periodization/zones` | 12 | 各節點 |
| `periodization/dryland` | 8 | 各節點 |
| `periodization/_index` | 0 | 各節點 |
| `health/injuries (built)` | 47 | 從 drafts/ build 出 |
| `health/breathing-training` | 5 | 呼吸訓練（生理線） |
| `psychology` | 8 | 8 themes / 共 62 concepts |
| `Drills (7 files)` | 176 | 176 drill 含 9 軸 fingerprint |

---

## 教學層 `canonical/instructional/`

### `technical-analysis.yaml` — 技術分析（**207 條目**）

**泳式分布**：仰式 29, 蛙式 32, 蝶式 36, 自由式 35, 起跳轉身 46, 水下蝶腳 29

#### 自由式 (35)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| free.tech.1 | concept |  | 🔵 |
| free.tech.2 | concept |  | 🔵 |
| free.tech.3 | tempo |  | 🟢 |
| free.tech.4 | style |  | 🟠 |
| free.tech.5 | style |  | 🟠 |
| free.tech.6 | style |  | 🟠 |
| free.tech.7 | stroke-cycle |  | 🟠 |
| free.tech.8 | stroke-cycle |  | 🟠 |
| free.tech.27 | stroke-cycle |  | 🟢 |
| free.tech.28 | stroke-cycle |  | 🟢 |
| free.tech.9 | stroke-cycle |  | 🔵 |
| free.tech.10 | hardware |  | 🟢 |
| free.tech.11 | kick |  | 🟢 |
| free.tech.12 | kick |  | 🟢 |
| free.tech.13 | hardware |  | 🟢 |
| free.tech.14 | kick |  | 🔵 |
| free.tech.15 | rotation |  | 🟡 |
| free.tech.16 | rotation |  | 🟠 |
| free.tech.29 | rotation |  | 🟠 |
| free.tech.17 | head |  | 🔵 |
| free.tech.18 | head |  | 🔵 |
| free.tech.19 | tempo |  | 🟢 |
| free.tech.20 | errors |  | 🟢 |
| free.tech.21 | errors |  | 🟢 |
| free.tech.22 | errors |  | 🔵 |
| free.tech.23 | errors |  | 🟢 |
| free.tech.24 | fatigue |  | 🟢 |
| free.tech.25 | watersense |  | 🟢 |
| free.tech.26 | comparison |  | 🔵 |
| free.tech.32 | stroke-cycle |  | 🟠 |
| free.tech.33 | hardware |  | 🟠 |
| free.tech.30 | rotation |  | 🟠 |
| free.tech.31 | fatigue |  | 🟠 |
| free.tech.34 | streamline |  | 🔵 |
| free.tech.35 | timing |  | 🟢 |

#### 仰式 (29)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| back.tech.28 | recovery |  | 🟠 |
| back.tech.29 | recovery |  | 🟠 |
| back.tech.1 | rotation |  | 🟢 |
| back.tech.2 | rotation |  | 🟢 |
| back.tech.3 | rotation |  | 🔵 |
| back.tech.4 | rotation |  | 🔵 |
| back.tech.5 | rotation |  | 🟢 |
| back.tech.6 | rotation |  | 🟠 |
| back.tech.7 | tempo |  | 🟠 |
| back.tech.8 | stroke-cycle |  | 🔵 |
| back.tech.9 | errors |  | 🔵 |
| back.tech.10 | stroke-cycle |  | 🔵 |
| back.tech.11 | stroke-cycle |  | 🟢 |
| back.tech.12 | stroke-cycle |  | 🔵 |
| back.tech.13 | stroke-cycle |  | 🔵 |
| back.tech.14 | errors |  | 🔵 |
| back.tech.15 | kick |  | 🟡 |
| back.tech.16 | hardware |  | 🟢 |
| back.tech.17 | kick |  | 🟢 |
| back.tech.18 | kick |  | 🟡 |
| back.tech.19 | kick |  | 🔵 |
| back.tech.20 | errors |  | 🔵 |
| back.tech.21 | head |  | 🔵 |
| back.tech.22 | streamline |  | 🟢 |
| back.tech.23 | streamline |  | 🔵 |
| back.tech.24 | fatigue |  | 🟢 |
| back.tech.25 | concept |  | 🟢 |
| back.tech.26 | comparison |  | 🔵 |
| back.tech.27 | comparison |  | 🟢 |

#### 蛙式 (32)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| breast.tech.1 | concept |  | 🔵 |
| breast.tech.2 | comparison |  | 🔵 |
| breast.tech.3 | stroke-cycle |  | 🟢 |
| breast.tech.4 | stroke-cycle |  | 🔵 |
| breast.tech.5 | stroke-cycle |  | 🟢 |
| breast.tech.6 | stroke-cycle |  | 🟢 |
| breast.tech.7 | streamline |  | 🟢 |
| breast.tech.8 | timing |  | 🟢 |
| breast.tech.9 | kick |  | 🟢 |
| breast.tech.10 | kick |  | 🔵 |
| breast.tech.11 | kick |  | 🟢 |
| breast.tech.12 | kick |  | 🟢 |
| breast.tech.13 | kick |  | 🔵 |
| breast.tech.14 | hardware |  | 🟢 |
| breast.tech.15 | hardware |  | 🟠 |
| breast.tech.16 | hardware |  | 🔵 |
| breast.tech.17 | style |  | 🟢 |
| breast.tech.18 | style |  | 🟢 |
| breast.tech.19 | style |  | 🟢 |
| breast.tech.20 | undulation |  | 🔵 |
| breast.tech.21 | style |  | 🔵 |
| breast.tech.22 | tempo |  | 🟢 |
| breast.tech.23 | watersense |  | 🟢 |
| breast.tech.24 | errors |  | 🟢 |
| breast.tech.25 | errors |  | 🟢 |
| breast.tech.26 | errors |  | 🔵 |
| breast.tech.27 | fatigue |  | 🟢 |
| breast.tech.28 | streamline |  | 🟢 |
| breast.tech.29 | comparison |  | 🔵 |
| breast.tech.30 | kick |  | 🟢 |
| breast.tech.31 | concept |  | 🟢 |
| breast.tech.35 | timing |  | 🟠 |

#### 蝶式 (36)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| fly.tech.1 | concept |  | 🔵 |
| fly.tech.2 | comparison |  | 🔵 |
| fly.tech.3 | undulation |  | 🟢 |
| fly.tech.4 | undulation |  | 🔵 |
| fly.tech.5 | undulation |  | 🟠 |
| fly.tech.6 | kick |  | 🟠 |
| fly.tech.7 | kick |  | 🟢 |
| fly.tech.8 | kick |  | 🔵 |
| fly.tech.9 | kick |  | 🟠 |
| fly.tech.10 | stroke-cycle |  | 🔵 |
| fly.tech.11 | stroke-cycle |  | 🟡 |
| fly.tech.12 | stroke-cycle |  | 🔵 |
| fly.tech.13 | stroke-cycle |  | 🟢 |
| fly.tech.14 | stroke-cycle |  | 🔵 |
| fly.tech.15 | stroke-cycle |  | 🔵 |
| fly.tech.16 | head |  | 🔵 |
| fly.tech.17 | head |  | 🟢 |
| fly.tech.18 | timing |  | 🔵 |
| fly.tech.19 | head |  | 🔵 |
| fly.tech.20 | stroke-cycle |  | 🔵 |
| fly.tech.21 | timing |  | 🔵 |
| fly.tech.22 | fatigue |  | 🔵 |
| fly.tech.23 | fatigue |  | 🔵 |
| fly.tech.24 | hardware |  | 🟢 |
| fly.tech.25 | hardware |  | 🔵 |
| fly.tech.26 | hardware |  | 🔵 |
| fly.tech.27 | hardware |  | 🔵 |
| fly.tech.28 | errors |  | 🔵 |
| fly.tech.29 | errors |  | 🔵 |
| fly.tech.30 | tempo |  | 🟠 |
| fly.tech.31 | streamline |  | 🟢 |
| fly.tech.32 | watersense |  | 🟢 |
| fly.tech.33 | comparison |  | 🔵 |
| fly.tech.34 | comparison |  | 🔵 |
| fly.tech.35 | concept |  | 🟢 |
| fly.tech.36 | streamline |  | 🔵 |

#### 起跳轉身 (46)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| starts-turns.tech.1 | comparison |  | 🔵 |
| starts-turns.tech.2 | stroke-cycle |  | 🔵 |
| starts-turns.tech.3 | hardware |  | 🟢 |
| starts-turns.tech.4 | head |  | 🟠 |
| starts-turns.tech.41 | stroke-cycle |  | 🟠 |
| starts-turns.tech.42 | stroke-cycle |  | 🟢 |
| starts-turns.tech.43 | coupling |  | 🟠 |
| starts-turns.tech.44 | stroke-cycle |  | 🟠 |
| starts-turns.tech.5 | stroke-cycle |  | 🔵 |
| starts-turns.tech.6 | stroke-cycle |  | 🔵 |
| starts-turns.tech.7 | stroke-cycle |  | 🟢 |
| starts-turns.tech.8 | stroke-cycle |  | 🔵 |
| starts-turns.tech.9 | stroke-cycle |  | 🟢 |
| starts-turns.tech.10 | stroke-cycle |  | 🔵 |
| starts-turns.tech.11 | streamline |  | 🔵 |
| starts-turns.tech.12 | depth |  | 🟢 |
| starts-turns.tech.13 | depth |  | 🔵 |
| starts-turns.tech.14 | stroke-cycle |  | 🟢 |
| starts-turns.tech.15 | stroke-cycle |  | 🟢 |
| starts-turns.tech.16 | stroke-cycle |  | 🔵 |
| starts-turns.tech.17 | concept |  | 🟢 |
| starts-turns.tech.18 | streamline |  | 🔵 |
| starts-turns.tech.19 | tempo |  | 🔵 |
| starts-turns.tech.20 | watersense |  | 🔵 |
| starts-turns.tech.21 | stroke-cycle |  | 🟢 |
| starts-turns.tech.22 | streamline |  | 🟢 |
| starts-turns.tech.23 | watersense |  | 🟠 |
| starts-turns.tech.24 | stroke-cycle |  | 🔵 |
| starts-turns.tech.25 | stroke-cycle |  | 🟢 |
| starts-turns.tech.26 | stroke-cycle |  | 🟢 |
| starts-turns.tech.27 | depth |  | 🟢 |
| starts-turns.tech.28 | comparison |  | 🟢 |
| starts-turns.tech.29 | stroke-cycle |  | 🟢 |
| starts-turns.tech.30 | comparison |  | 🔵 |
| starts-turns.tech.31 | comparison |  | 🟠 |
| starts-turns.tech.32 | depth |  | 🔵 |
| starts-turns.tech.33 | kick |  | 🟢 |
| starts-turns.tech.34 | kick |  | 🟠 |
| starts-turns.tech.35 | comparison |  | 🔵 |
| starts-turns.tech.36 | errors |  | 🟠 |
| starts-turns.tech.37 | errors |  | 🟠 |
| starts-turns.tech.38 | errors |  | 🟠 |
| starts-turns.tech.39 | concept |  | 🔵 |
| starts-turns.tech.40 | hardware |  | 🟢 |
| starts-turns.tech.45 | comparison |  | 🟢 |
| starts-turns.tech.46 | stroke-cycle |  | 🟢 |

#### 水下蝶腳 (29)

| ID | 範疇 | 標題 | 確定性 |
|---|---|---|---|
| udk.tech.1 | concept |  | 🔵 |
| udk.tech.2 | depth |  | 🔵 |
| udk.tech.3 | depth |  | 🟢 |
| udk.tech.4 | undulation |  | 🔵 |
| udk.tech.5 | undulation |  | 🟢 |
| udk.tech.6 | kick |  | 🟢 |
| udk.tech.7 | kick |  | 🟢 |
| udk.tech.8 | concept |  | 🔵 |
| udk.tech.9 | kick |  | 🔵 |
| udk.tech.10 | kick |  | 🟢 |
| udk.tech.11 | comparison |  | 🔵 |
| udk.tech.12 | kick |  | 🟢 |
| udk.tech.13 | tempo |  | 🟢 |
| udk.tech.14 | hardware |  | 🔵 |
| udk.tech.15 | hardware |  | 🟢 |
| udk.tech.16 | hardware |  | 🟠 |
| udk.tech.17 | depth |  | 🟢 |
| udk.tech.18 | depth |  | 🔵 |
| udk.tech.19 | depth |  | 🔵 |
| udk.tech.20 | depth |  | 🔵 |
| udk.tech.21 | depth |  | 🔵 |
| udk.tech.22 | comparison |  | 🔵 |
| udk.tech.23 | comparison |  | 🔵 |
| udk.tech.24 | streamline |  | 🟠 |
| udk.tech.25 | kick |  | 🟢 |
| udk.tech.26 | kick |  | 🟢 |
| udk.tech.27 | tempo |  | 🟢 |
| udk.tech.28 | kick |  | 🟢 |
| udk.tech.29 | streamline |  | 🔵 |

### `teaching-errors.yaml` — 教學誤區（**102 條目**）

**泳式分布**：仰式 17, 蛙式 17, 蝶式 16, 自由式 25, 起跳轉身 14, 水下蝶腳 13

#### 自由式 (25)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| free.err1 | recovery |  |
| free.err2 | recovery |  |
| free.err3 | recovery |  |
| free.err4 | recovery |  |
| free.err5 | recovery |  |
| free.err6 | entry |  |
| free.err7 | entry |  |
| free.err8 | entry |  |
| free.err9 | entry |  |
| free.err10 | pull |  |
| free.err11 | kick |  |
| free.err12 | kick |  |
| free.err13 | kick |  |
| free.err14 | kick |  |
| free.err15 | rotation |  |
| free.err16 | rotation |  |
| free.err17 | rotation |  |
| free.err18 | head |  |
| free.err19 | head |  |
| free.err20 | tempo |  |
| free.err21 | tempo |  |
| free.err22 | tempo |  |
| free.err23 | tempo |  |
| free.err24 | pull |  |
| free.err25 | pull |  |

#### 仰式 (17)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| back.err1 | rotation |  |
| back.err2 | pull |  |
| back.err3 | depth |  |
| back.err4 | rotation |  |
| back.err5 | kick |  |
| back.err6 | pull |  |
| back.err7 | head |  |
| back.err8 | kick |  |
| back.err9 | posture |  |
| back.err10 | head |  |
| back.err11 | entry |  |
| back.err12 | pull |  |
| back.err13 | posture |  |
| back.err14 | head |  |
| back.err15 | recovery |  |
| back.err16 | recovery |  |
| back.err17 | recovery |  |

#### 蛙式 (17)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| breast.err1 | kick |  |
| breast.err2 | kick |  |
| breast.err3 | kick |  |
| breast.err4 | kick |  |
| breast.err5 | pull |  |
| breast.err6 | pull |  |
| breast.err7 | head |  |
| breast.err8 | head |  |
| breast.err9 | head |  |
| breast.err10 | timing |  |
| breast.err11 | timing |  |
| breast.err12 | streamline |  |
| breast.err13 | head |  |
| breast.err14 | kick |  |
| breast.err15 | pull |  |
| breast.err16 | undulation |  |
| breast.err17 | head |  |

#### 蝶式 (16)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| fly.err1 | pull |  |
| fly.err2 | entry |  |
| fly.err3 | pull |  |
| fly.err4 | recovery |  |
| fly.err5 | timing |  |
| fly.err6 | kick |  |
| fly.err7 | kick |  |
| fly.err8 | kick |  |
| fly.err9 | timing |  |
| fly.err10 | undulation |  |
| fly.err11 | undulation |  |
| fly.err12 | head |  |
| fly.err13 | head |  |
| fly.err14 | head |  |
| fly.err15 | entry |  |
| fly.err16 | entry |  |

#### 起跳轉身 (14)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| starts-turns.err1 | start |  |
| starts-turns.err2 | start |  |
| starts-turns.err3 | entry |  |
| starts-turns.err4 | start |  |
| starts-turns.err5 | turn |  |
| starts-turns.err6 | streamline |  |
| starts-turns.err7 | turn |  |
| starts-turns.err8 | depth |  |
| starts-turns.err9 | concept |  |
| starts-turns.err10 | head |  |
| starts-turns.err11 | turn |  |
| starts-turns.err12 | breakout |  |
| starts-turns.err13 | timing |  |
| starts-turns.err14 | breakout |  |

#### 水下蝶腳 (13)

| ID | 範疇 | 標題/摘要 |
|---|---|---|
| udk.err1 | kick |  |
| udk.err2 | kick |  |
| udk.err3 | kick |  |
| udk.err4 | tempo |  |
| udk.err5 | undulation |  |
| udk.err6 | concept |  |
| udk.err7 | depth |  |
| udk.err8 | turn |  |
| udk.err9 | depth |  |
| udk.err10 | timing |  |
| udk.err11 | concept |  |
| udk.err12 | concept |  |
| udk.err13 | streamline |  |

---

## 感知層 `canonical/technica/`

### `l-indicators.yaml` — L 級指標（**47 條目**）

| ID | 泳式 | L | 面向 | 指標 |
|---|---|---|---|---|
| common.pre.resistance | common | pre | 阻力感知 | 靜止漂浮距離可量測；緊鬆身體有明顯差異 |
| common.L2.propulsion | common | L2 | 推進萌芽 | 浮板踢水穩定前進；手部能撐起換氣（蛙）/ 前臂感覺水壓（自蝶）/ 上踢有感知（仰） |
| common.L3.watersense | common | L3 | 水感萌芽 | 捕水有前臂壓力感（自蝶仰）；踢腿後有滑行感（蛙）；波動傳到腳（蝶）；肩旋轉帶動划手（仰） |
| common.L4.under-pressure | common | L4 | 壓力崩潰 | 慢游技術正確但加速後崩潰；EVF 在高划頻下消失；蛙式踢腿時機在速度下跑掉；蝶式第二踢失同步 |
| common.L5.automation | common | L5 | 自動化過渡 | 划頻提升但划距不下降（Staunton 2025）；蛙式 late kick 時機穩定；蝶式兩踢功能分化；仰式旋轉角度不因速度縮小 |
| common.L6.stability | common | L6 | 自動化完成 | 疲勞下仍維持技術穩定性（Gonjo & Olstad 2023 精英特徵）；能感知並即時修正細微偏差；SWOLF 跨距離差距極小 |
| free.pre.resistance | free | pre | 阻力感知 | 靜止漂浮身體鬆緊有可觀察差異；推蹬後滑行距離可量測 |
| free.L2.kick | free | L2 | 踢水推進 | 浮板踢水能穩定前進，踝蹠屈角度使腳掌朝後 |
| free.L2.hand-pressure | free | L2 | 手部壓力 | 前臂面向後方時有水壓感知（外感受器啟動） |
| free.L3.evf | free | L3 | EVF 捕水 | 划手有明顯的捕水「卡頓感」；拳頭游 vs 開手速度差 > 15% |
| free.L3.kick-rhythm | free | L3 | 踢水節律 | 六拍踢能描述「對側配對」；踢水後下半身不下沉 |
| free.L4.roll-coupling | free | L4 | 旋轉耦合 | 加速後旋轉崩潰（肩旋轉提前縮小）；高划頻下 EVF 消失 |
| free.L4.sr-sl | free | L4 | 划頻×划距 | SR 提高時 SL 下降 > 5%（感知尚未支撐技術） |
| free.L5.sr-sl | free | L5 | 划頻×划距 | 精英特徵：高 SR 下 SL 不下降；SR 與速度負相關消失 |
| free.L5.coupling-timing | free | L5 | 肩-髖旋轉時間差 | 精英特徵：肩旋轉峰值與髖旋轉峰值相差 0.2–0.3 秒（不是同步）；初學者兩者同時或無時差 |
| free.L5.lift-phase-duration | free | L5 | 升力相時長與風格匹配 | 精英特徵：升力相時長與所選風格的 SR 對應——hip-driven 60 SPM 約 >0.6 秒、shoulder-driven 120 SPM <0.3  |
| free.L5.serratus | free | L5 | 前鋸肌耐力 | 疲勞後 EVF 仍維持；肩胛骨不 wing；第 4-6 趟技術與第 1-2 趟差距小 |
| free.L6.stability | free | L6 | 技術穩定性 | 疲勞全程划距穩定（Gonjo & Olstad 2023 精英特徵）；SWOLF 跨速度差異 < 3 |
| back.pre.orientation | back | pre | 方向感安全 | 能仰漂靜止 > 5 秒不扶持；描述得出「耳入水聲音變化」 |
| back.L2.up-kick | back | L2 | 上踢推進 | 浮板仰式踢水穩定前進；腳背往上踢能描述「水團被往上推」 |
| back.L3.pull | back | L3 | 手部划水 | 前臂在水下有水壓感知；能描述拉水「有抓住什麼」；入水不跨越中線（蛇行感知） |
| back.L3.shoulder-roll | back | L3 | 肩旋轉感知 | 能感知「回臂側肩膀向上帶起」；旋轉幅度約 30-40°可自評 |
| back.L4.roll-stability | back | L4 | 旋轉穩定 | 高划頻下旋轉幅度縮小；加速後蛇行明顯；流線型滑行後提早抬頭 |
| back.L4.head-stillness | back | L4 | 頭部加速靜止度 | 加速後頭部仍能維持完全靜止（不左右晃、不前後點）；額頭水線位置不偏移。
L4 訊號是「加速時頭部開始輕微晃動但仍能控制」；L5 是「全速下完全不動」。
測試：在 |
| back.L5.roll-invariant | back | L5 | 旋轉不隨速縮 | 仰式精英特徵：速度增加時旋轉幅度維持（≠ 自由式）；划距穩定 |
| back.L5.start-turn | back | L5 | 出發轉身流線 | 推蹬後流線型滑行至速度降至游進速度才開始划手；時機感知穩定 |
| back.L6.stability | back | L6 | 技術穩定性 | 疲勞後技術與前段差距極小；六拍踢節律全程維持；划距跨速度穩定 |
| fly.pre.undulation | fly | pre | 波動感知 | 胸骨下壓能描述「有東西傳到腳」；海豚漂浮有連貫弧線而非上下擺動 |
| fly.L2.kick | fly | L2 | 踢水推進 | 浮板蝶式踢水能穩定前進；腳背有水壓感知（而非只是在拍水） |
| fly.L2.catch | fly | L2 | 捕水感知 | 外划後停住時前臂有水壓感知（兩側對稱） |
| fly.L3.undulation-integration | fly | L3 | 波動整合 | 胸部下壓有帶動腿踢的感知（不是腿獨立踢）；身體像「一條線」而非兩段 |
| fly.L3.two-kick-timing | fly | L3 | 兩踢時機 | 能描述「第一踢在手入水時」；第二踢和出水有部分同步感 |
| fly.L4.second-kick | fly | L4 | 第二踢失守 | 加速後第二踢消失；疲勞後手出水無法「飛過」水面；髖部下沉明顯 |
| fly.L4.outsweep | fly | L4 | 外划過大 | 捕水感知不穩時外划幅度代償性增大；前臂感知比手掌感知更弱 |
| fly.L5.two-kick-differentiation | fly | L5 | 兩踢功能分化 | 能區分第一踢（輕、穩、觸發）和第二踢（強、同步出水）的不同感知 |
| fly.L5.glide-elimination | fly | L5 | 滑行相消除 | 每個 stroke cycle 的「滑行/減速期」幾乎消失——推進力連續銜接、不存在「等」的瞬間。
L4 訊號是「能感知滑行期但無法消除」；L5 是「在標準訓練 |
| fly.L6.chain-closure | fly | L6 | 波動鏈閉環 | 每個划手週期從胸到腳感知連貫；疲勞後仍維持兩踢時機；SWOLF 穩定 |
| breast.pre.resistance | breast | pre | 阻力感知 | 靜止漂浮感覺到「緊的身體滑更遠」；能描述阻力存在（非推進） |
| breast.L2.leg-propulsion | breast | L2 | 腿部推進 | 浮板踢水能穩定前進；翻腳掌時腳掌有水壓感知（非腳心朝後） |
| breast.L2.hand-support | breast | L2 | 手部撐水 | 外划內抱能撐起身體換氣（不需要額外抬頭） |
| breast.L3.kick-vortex | breast | L3 | 踢腿渦流 | 踢完後有滑行感；能描述「夾水後身體繼續往前」而非踢完即停 |
| breast.L3.recovery-drag | breast | L3 | 收腿阻力 | 開始感知收腿「有煞車感」；收腿路徑往外側而非正中（髖外旋意識） |
| breast.L4.timing | breast | L4 | 手腳時序 | 加速後手腳時序跑掉（兩個推進脈衝重疊或空白過長）；速度谷值明顯加深 |
| breast.L4.undulation | breast | L4 | 波動整合 | 能做波動蛙式但偶爾下沉（角度不穩）；Wave style 俯衝角度感知不穩 |
| breast.L5.late-kick | breast | L5 | late kick 時機 | insweep 啟動時才踢腿（比傳統更晚）；速度谷值明顯縮小；%VDO 降低 |
| breast.L5.undulation-stability | breast | L5 | 波動穩定 | Wave style 俯衝角度可自評（胸口下壓時機穩定）；收腿阻力與滑行感配對 |
| breast.L6.stability | breast | L6 | 技術穩定性 | 精英特徵：划距穩定；疲勞後 IVV（週期內速度波動）差距極小 |

### `water-sense-levels.yaml` — 水感層級（**26 條目**）

| ID | 泳式 | L | tagline/摘要 |
|---|---|---|---|
| free.L0 | free | L0 |  |
| free.L1 | free | L1 |  |
| free.L2 | free | L2 |  |
| free.L3 | free | L3 |  |
| free.L4 | free | L4 |  |
| free.L5 | free | L5 |  |
| free.L6 | free | L6 |  |
| back.L0 | back | L0 |  |
| back.L1 | back | L1 |  |
| back.L2 | back | L2 |  |
| back.L3 | back | L3 |  |
| back.L4 | back | L4 |  |
| back.L5 | back | L5 |  |
| back.L6 | back | L6 |  |
| breast.pre | breast | pre |  |
| breast.L2 | breast | L2 |  |
| breast.L3 | breast | L3 |  |
| breast.L4 | breast | L4 |  |
| breast.L5 | breast | L5 |  |
| breast.L6 | breast | L6 |  |
| fly.pre | fly | pre |  |
| fly.L2 | fly | L2 |  |
| fly.L3 | fly | L3 |  |
| fly.L4 | fly | L4 |  |
| fly.L5 | fly | L5 |  |
| fly.L6 | fly | L6 |  |

---

## 發展層 `canonical/development/`

### `matrix.yaml` — ADM 4×4 發展矩陣（**16 格**）

| ID | 支柱 | 階段 | 摘要 |
|---|---|---|---|
| dev.physical.l2t | physical | l2t | 多元體能基礎；速度與柔軟度為敏感訓練期；體重阻力；GPP 佔 80% |
| dev.physical.t2t | physical | t2t | 進入耐力與肌力可訓練窗口；開始離心負重；增強式訓練；GPP 佔 50% |
| dev.physical.t2c | physical | t2c | 個別化體能強化；70% 1RM 肌力訓練；高強度增強式；GPP 佔 35% |
| dev.physical.t2w | physical | t2w | 完全個別化；世界級標準監控；48 週年度計畫；兩次巔峰週期 |
| dev.technical.l2t | technical | l2t | 四式基礎；起跳轉身入門；廣泛多項運動；動作技能自動化 |
| dev.technical.t2t | technical | t2t | 技術精緻化；個人划水模型；划水效率指標（SR、DPS）；比賽技能整合 |
| dev.technical.t2c | technical | t2c | 疲勞下技術穩定；SR/DPS 精準控制；比賽策略與能量分配；開始專項化 |
| dev.technical.t2w | technical | t2w | 疲勞下技術完全不受影響；最佳起跳與水下蝶式踢；精確比賽策略 |
| dev.mental.l2t | mental | l2t | 正向態度建立；教練引導下的目標設定；情緒與行為的連結；視覺化入門 |
| dev.mental.t2t | mental | t2t | SMART 目標設定；情緒管理策略；視覺化練習；理想表現狀態輪廓 |
| dev.mental.t2c | mental | t2c | 高壓情境應對；以實證為基礎的目標設定；系統性賽後錯誤分析 |
| dev.mental.t2w | mental | t2w | 頂峰表現心理；正常化挫折；長期生涯規劃；全感官視覺化與應變計畫 |
| dev.life.l2t | life | l2t | 時間管理與自律；正向飲食關係；基礎 SEL；公平競賽理解 |
| dev.life.t2t | life | t2t | 整合運動與學業；壓力管理；領導力發展；禁藥倫理意識 |
| dev.life.t2c | life | t2c | 高壓表現；長期壓力管理；媒體與旅行技能；職涯規劃起步 |
| dev.life.t2w | life | t2w | 高度審視下產出成績；退役轉型計畫；代表國家的意義；文化理解 |

### `technical-standards.yaml` — 技術基準（**22 條目**）

| ID | 起始階段 | 標題 |
|---|---|---|
| std.free.pull | t2t | 自由式——拉水技術 |
| std.free.push | t2t | 自由式——推水技術 |
| std.free.full-cycle | t2t | 自由式——完整划水週期 |
| std.back.pull | t2t | 仰式——拉水技術 |
| std.back.push | t2t | 仰式——推水技術 |
| std.back.full-cycle | t2t | 仰式——完整划水週期 |
| std.fly.pull | t2t | 蝶式——手臂拉水階段 |
| std.fly.push-kick | t2t | 蝶式——手臂推水 & 腿部踢水階段 |
| std.fly.recovery | t2t | 蝶式——手臂恢復階段 |
| std.fly.full-cycle | t2t | 蝶式——完整划水週期 |
| std.breast.kick | t2t | 蛙式——腿部踢水階段 |
| std.breast.pull | t2t | 蛙式——手臂拉水階段 |
| std.breast.recovery-flex | t2t | 蛙式——手臂恢復 & 腿部屈曲階段 |
| std.breast.full-cycle | t2t | 蛙式——完整划水週期 |
| std.start.dive | t2t | 潛水式起跳（自由式 / 仰式 / 蝶式 / 蛙式） |
| std.start.back | t2t | 仰式起跳 |
| std.turn.free | t2t | 自由式轉身 |
| std.turn.back | t2t | 仰式轉身 |
| std.turn.breast | t2t | 蛙式轉身 |
| std.turn.fly | t2t | 蝶式轉身 |
| std.turn.im-breast | t2t | 個人混合式轉身——蛙式出（IM → Breast） |
| std.turn.im-free | t2t | 個人混合式轉身——自由式出（IM → Free） |

---

## 週期化 `canonical/periodization/`

### `structure.yaml` （**9 節點**）

| ID | 確定性 | premise/摘要 |
|---|---|---|
| periodization.structure.macrocycle | 🟡 | Macrocycle＝由幾個週組成的中型週期（2–6 週）。最常見的節奏是『3:1』——練 3 個漸增負荷的週，接 1 個減量恢復週。這契合身體自然的疲勞—恢復節律。泳者特別累時改 |
| periodization.structure.microcycle | 🟡 | Microcycle＝一週，是排課表的最小單位。一週有不同類型：發展型（往上堆）、競賽型（賽前 3–5 天達峰）、恢復型、卸載型（量砍一半以上）。游泳就以『週』為單位排課。週內休息 |
| periodization.structure.gas | 🟢 | 為什麼週期化要有節奏不能一路往上堆？因為身體對訓練壓力有三個階段：① 警覺期（剛開始幾天，覺得難）、② 適應期（幾週後身體變強）、③ 耗竭期（再撐就崩）。週期化的目標就是每段訓練都 |
| periodization.structure.detraining | 🟢 | 完全停練掉得有多快？最大攝氧量：停 4 天掉 4%、停 4 週掉 14%、停 8 週掉 20%。力量也類似（停 4 週最大肌力掉 6–10%）。好消息是這些可以練回來。實務結論：休 |
| periodization.structure.swim_annual | 🟢 | 菁英游泳的年度結構長怎樣（有實證的）：一年大概切 2–4 個中週期（每個約 15 週）。最反直覺的數字——高達 86–90% 的訓練量是低強度（血乳酸 ≤4），不是整天操高強度。有 |
| periodization.structure.swim_youth_ltad | 🟢 | 青少年怎麼分齡練（對齊 ADM 階段）：大致按年齡分學習訓練→訓練為訓練→訓練為競賽→訓練為勝利。生長陡增高峰（長最快的時候）女生約 12.5 歲、男生約 14 歲，可作排訓練的參 |
| periodization.structure.schools_overview | 🔵 | 週期化不是一套被證明的定論，而是幾套互相辯論的框架。它們問的問題不同、適用的對象不同——把任何一派當『標準答案』都是誤讀。 |
| periodization.structure.school_block | 🟡 | 板塊週期化（Issurin）跟 Bompa 最大的不同：Bompa 主張準備期可以同時把很多能力一起練；Issurin 說高水準選手做不到——很多訓練刺激會互相打架（大量有氧會干擾 |
| periodization.structure.perception_periodization_bridge | 🔵 | 先講清楚兩層：第一層『技能會不會該被週期化、疲勞會不會傷技術』——這層有研究撐：Branscheidt 2019 證實疲勞不只讓你當下做不好，連『學會新技能』的能力都被拖累，而且累 |

### `taper.yaml` （**3 節點**）

| ID | 確定性 | premise/摘要 |
|---|---|---|
| periodization.taper.definition | 🟢 | 減量＝比賽前那幾週，故意把訓練量慢慢降下來。關鍵在：之前練出來的本事（體能）會留著，但累積的疲勞會被消掉。比賽當天身體既有料又不累，成績自然跑得出來。 |
| periodization.taper.peak_window | 🟡 | 巔峰狀態不是無限期的——大概只能撐 7–14 天。所以主賽一定要排在這個窗口裡。一個賽季有好幾場重要比賽時，就用幾段短減量，分別對準每一場（見 structure.yaml 多巔峰 |
| periodization.taper.swim | 🟢 | 游泳的實際做法：對準主賽往前推 8–14 天開始減量，總量降到平常的四到六成，但下水次數和短距離快游照舊，曲線用前快後慢的指數型。研究顯示游泳選手減三週平均能進步約 2–3%——在 |

### `zones.yaml` （**12 節點**）

| ID | 確定性 | premise/摘要 |
|---|---|---|
| periodization.zones.table_7_1 | 🟡 | Bompa 把訓練強度分成 6 區，用『佔最大表現的百分比』定義。zone 1 最吃力（90–100%），zone 5 最輕（<50%），recovery 是不下水。比賽配速落在  |
| periodization.zones.table_11_2 | 🟡 | 這張表把心率／攝氧量對應到身體主要靠哪套能量系統供能。心率越高、越偏無氧；心率 50% 上下是有氧恢復區。用途是確認某一組課實際練到的是哪個系統，避免賽季階段跟能量系統錯配。 |
| periodization.zones.table_11_1 | 🟡 | 低強度耐力的幾種練法：主動恢復、長慢游、節奏游、有氧間歇等。最重要的一句警告——低強度耐力和高強度耐力不能亂混著練，耐力型態選錯會拖累專項表現。 |
| periodization.zones.endurance_phases | 🟡 | 耐力是分階段堆起來的：先用廣度有氧打底（過渡期＋準備期早期），再疊上專項代謝需求，最後練對準比賽的專項耐力。順序不能顛倒——沒打好有氧底就直接衝專項，後面會撐不住。不過『有氧底＝大 |
| periodization.zones.swim_maglischo | 🟢 | Maglischo 是游泳專用的分區系統，用血乳酸＋訓練目的把游泳強度分成：恢復、有氧基礎(En1)、有氧維持(En2)、有氧超負荷(En3)、無氧閾值(AnTh，乳酸 3–5)、 |
| periodization.zones.swim_three_zone | 🟢 | 做訓練強度分布分析時最常用的簡化版：用血乳酸把強度切三段——Z1 輕鬆（≤2）、Z2 閾值（2–4）、Z3 吃力（>4）。下面的 polarized / pyramidal 分布就 |
| periodization.zones.energy_systems_primer | 🟡 | 身體有三套供能系統，差別在『撐多久、靠什麼、怎麼累』：① 磷酸原（ATP-PCr）——前 10 秒的爆發力來源，用肌肉裡現成的能量，不產乳酸，但很快用完，休 3–5 分鐘才回補；對 |
| periodization.zones.swim_energy_by_distance | 🟢 | 不同距離靠的能量系統差很多：50m 幾乎全靠無氧（有氧只 5–20%），100m 有氧無氧大概各半，400m 以上開始有氧主導。注意 400m 的有氧占比在不同研究差很大（40%  |
| periodization.zones.swim_tid | 🟢 | TID＝整個週期裡輕鬆/閾值/吃力三種強度各占多少。主要有三種分布：極化型（大量輕鬆＋少量超吃力、中間幾乎不練）、金字塔型（由下往上遞減）、閾值型（中間那塊偏多）。游泳實證裡『金字 |
| periodization.zones.swim | 🔵 | 游泳怎麼套 Bompa 這套：組課強度用『比賽配速百分比』講——賽配速＝zone 2，比賽更快（衝刺/乳酸耐受）＝zone 1，閾值/節奏＝zone 3，有氧基礎＝zone 4，恢 |
| periodization.zones.school_polarized | 🟢 | 極化派（Seiler）問的不是『每區強度多少』而是『每區各占幾成』。他觀察菁英耐力選手，發現他們自然形成『大量輕鬆＋少量超吃力、中間幾乎不練』的分布——大約 80% 低強度、20% |
| periodization.zones.olbrecht_model | 🟡 | Olbrecht（游泳能量系統論）的核心是『最適，不是最大』：有氧和無氧都不是越大越好，要配到最適組合點——無氧太強會拖累有氧效率，有氧練過頭又壓掉速度。他最有名的是質疑閾值訓練是 |

### `dryland.yaml` （**8 節點**）

| ID | 確定性 | premise/摘要 |
|---|---|---|
| periodization.dryland.overview | 🔵 | 陸上力量常被當成『游得快的捷徑』或被當成『沒用、浪費水感』兩個極端來吵。兩種都是誤讀。陸訓能讓人變強這件事幾乎沒爭議；真正有爭議的是三件事：① 變強的力量能不能轉移到游速（轉移問題 |
| periodization.dryland.transfer | 🟡 | 別把陸訓當保證。最該記住的數字是：回顧裡大約每兩篇就有一篇看不到效果。會看到效果的，通常是技術已經穩、練的是最大力量、而且練法盡量貼近游泳動作的人。如果你還在抓水感、或練的是跟游泳 |
| periodization.dryland.methods | 🟢 | 不是所有陸訓都一樣。要游速進步，最大力量訓練最靠譜；增強式跳躍主要幫你『跳得更遠、轉身蹬得更猛』，但對中間那段游程幫助有限。最聰明的做法是讓陸訓盡量像游泳——划手板、拖傘比深蹲更容 |
| periodization.dryland.concurrent | 🟢 | 怕重訓害你隔天游不動？至少這份研究說：隔一個晚上（約 12 小時）就恢復了，隔天 100 公尺一樣快。所以重訓最好排在關鍵課的前一天、留一晚睡眠，別跟比賽擠在同一天。但這只測了 8 |
| periodization.dryland.injury | 🟢 | 游泳肩不是運氣不好，是划手把『內旋』練太強、『外旋』練太弱的必然結果。陸上拿彈力帶練外旋和肩胛穩定（8 週就有效），是把這個失衡扳回來的標準做法。而且新研究發現：練整條手臂—肩—核 |
| periodization.dryland.youth | 🟢 | 孩子幾歲能重訓？關鍵不是年齡數字，而是『聽不聽得懂指令、守不守得住安全規則』——大約 7、8 歲就可以開始（先用自體重量）。游泳界的標準更保守：發育衝刺期之前只做徒手，女生大約 1 |
| periodization.dryland.flexibility | 🟢 | 游泳對三個關節活動度的依賴度高於多數運動：**肩**（划手延伸與高肘恢復）、**髖**（蛙腿外翻與蝶腰波動）、**踝**（蹠屈推進面積）。三個關節若活動度不足，技術天花板會被『硬體 |
| periodization.dryland.caveats | 🟡 | 如果有人跟你說『重訓一定讓你游更快』，他沒讀過反面的那一半研究。陸訓有用是有前提的——技術要先穩、要練對的東西（最大力量）、練法要像游泳。前提不滿足，花在陸上的時間很可能換不到水裡 |

### `_index.yaml` （**0 節點**）

（無）

---

## 健康 `canonical/health/`

### `injuries.yaml` — 已 build 之傷害條目（**47 條目**，來源 `drafts/`）

#### 肩部與上肢 (A-shoulder-upper, 7)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| biceps-tendinopathy | 肱二頭肌長頭肌腱病 | Biceps (long head) tendinopathy | 🟡 |
| rotator-cuff-tendinopathy | 旋轉肌袖肌腱病（棘上肌） | Rotator cuff (supraspinatus) tendinopathy | 🟡 |
| shoulder-multidirectional-instability | 多向性肩關節不穩定（MDI） | Multidirectional shoulder instability | 🟠 |
| slap-lesion | 上盂唇前後損傷（SLAP） | Superior labrum anterior-posterior (SLAP) lesion | 🟠 |
| swimmer-elbow-wrist-overuse | 游泳者肘/腕過度使用傷 | Swimmer's elbow & wrist overuse | 🔵 |
| swimmers-shoulder | 游泳肩 | Swimmer's shoulder | 🟡 |
| thoracic-outlet-syndrome | 胸廓出口症候群（TOS） | Thoracic outlet syndrome in swimmers | 🔵 |

#### 腰椎與泳式特異 (B-lower-spine-strokespecific, 6)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| breaststrokers-knee | 蛙泳膝 | Breaststroker's knee | 🟡 |
| extension-low-back-pain | 伸展型下背痛（蝶泳） | Extension-type low back pain (butterfly) | 🟡 |
| femoroacetabular-impingement | 股骨髖臼撞擊（FAI） | Femoroacetabular impingement in swimmers | 🟡 |
| groin-adductor-strain | 腹股溝/內收肌損傷（蛙泳） | Groin / adductor strain (breaststroke) | 🟡 |
| spondylolysis | 椎弓解離/脊椎滑脫 | Spondylolysis / spondylolisthesis | 🟡 |
| swimmer-ankle-foot-overuse | 游泳者踝/足過度使用傷 | Swimmer's ankle & foot overuse | 🔵 |

#### 非肌骨醫療 (C-nonMSK-medical, 10)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| acanthamoeba-keratitis | 棘阿米巴角膜炎（隱形眼鏡泳者） | Acanthamoeba keratitis in swimmers | 🟢 |
| chlorine-eye-irritation | 氯 / 化學性結膜炎與角膜刺激 | Chlorine / chemical conjunctivitis & corneal irritation | 🟡 |
| recreational-water-cryptosporidium | 隱孢子蟲 / 泳池水傳染腸道病 | Cryptosporidium & recreational water illness | 🟢 |
| sci-hip-flexor-contracture | 脊髓損傷泳者的髖屈攣縮 | Hip flexor contracture in SCI swimmers | 🟠 |
| surfers-ear-exostosis | 外耳道骨瘤 / 骨疣（衝浪耳） | Surfer's ear / external auditory exostosis | 🟡 |
| swimmer-dental-erosion | 牙齒酸蝕（游泳者） | Swimmer's dental erosion | 🟡 |
| swimmer-dermatoses | 泳者皮膚問題群 | Swimmer dermatoses (folliculitis / swimmer's itch / green hair / chlorine dermatitis) | 🟡 |
| swimmers-ear | 游泳耳 / 外耳道炎 | Swimmer's ear / otitis externa | 🟡 |
| swimming-induced-bronchoconstriction | 運動誘發支氣管收縮 / 游泳氣喘 | Exercise-induced bronchoconstriction in swimmers | 🟡 |
| uv-photo-damage | 曬傷 / 光化性傷害（皮膚 + 眼睛） | UV / photo-damage — skin cancer & pterygium in outdoor swimmers | 🟡 |

#### 全身急性 (D-systemic-acute, 7)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| cold-water-shock | 冷水休克 / 冷水衝擊反應 | Cold water shock / Cold shock response | 🟠 |
| dehydration-hyponatremia | 運動性脫水 / 低鈉血症 | Exercise-associated dehydration / hyponatremia in swimmers | 🟡 |
| drowning | 溺水 / 近乎溺水 | Drowning / Near-drowning | 🟢 |
| exertional-sudden-cardiac-death | 運動性猝死（游泳 / 運動員） | Exertional sudden cardiac death — swimming / athletes | 🟢 |
| hypothermia-swimmers | 游泳者低體溫（開放水域） | Hypothermia in swimmers / open-water hypothermia | 🟡 |
| shallow-water-blackout | 淺水昏迷 | Shallow water blackout (SWB) | 🟠 |
| sipe | 游泳誘發肺水腫 | Swimming-Induced Pulmonary Edema (SIPE) | 🟡 |

#### 內分泌與骨骼 (D-endocrine, 7)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| exercise-amenorrhea | 運動性月經功能障礙 | Exercise-associated menstrual dysfunction | 🟡 |
| female-athlete-triad | 女性運動員三聯症 | Female athlete triad | 🟡 |
| iron-deficiency-swimmer | 泳者鐵質缺乏（含非貧血性鐵缺） | Iron deficiency in swimmers (including non-anemic iron deficiency) | 🟡 |
| oral-contraceptives-performance | 口服避孕藥對運動表現的影響 | Oral contraceptives and athletic performance | 🟡 |
| red-s | 相對能量不足（RED-S） | Relative Energy Deficiency in Sport (RED-S) | 🟡 |
| stress-fracture-swimmer | 游泳員疲勞性骨折（肋骨為主） | Stress fracture in swimmers (rib-predominant) | 🟠 |
| swimmer-low-bone-density | 游泳員低骨密度 | Low bone mineral density in swimmers | 🟡 |

#### 急性外傷 (E-acute-trauma, 5)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| diving-cervical-injury | 跳水 / 入水頸椎與脊髓損傷 | Diving-related cervical spine and spinal cord injury | 🟢 |
| flip-turn-wall-push | 轉身 / 蹬牆相關急性傷 | Flip-turn and wall-push acute injuries | 🟡 |
| open-water-marine-biological-hazards | 開放水域海洋生物危害（螫刺 / 感染） | Open-water marine biological hazards — stings, punctures, infections | 🟡 |
| poolside-slip-fall | 池畔濕滑跌倒傷 | Poolside slip-and-fall injuries | 🟡 |
| starting-block-impact | 出發台 / 牆面 / 水面撞擊傷 | Starting block, wall, and water-surface impact injuries | 🟢 |

#### 兒童生長 (F-pediatric-growth, 5)

| ID | 中文名 | 英文名 | 流病確定性 |
|---|---|---|---|
| osgood-schlatter | Osgood-Schlatter 病 | Osgood-Schlatter disease | 🟢 |
| salter-harris-physeal-fracture | Salter-Harris 生長板骨折 | Salter-Harris physeal fracture | 🟢 |
| scheuermann-kyphosis | Scheuermann 病（青少年脊椎後凸） | Scheuermann's kyphosis | 🟢 |
| sever-disease | Sever 病（跟骨骨突炎） | Sever's disease (calcaneal apophysitis) | 🟢 |
| youth-swimmer-apophysitis | 年輕游泳員肩/肘骨骺與骨突損傷 | Youth swimmer shoulder/elbow physeal & apophyseal injury | 🟠 |

### `breathing-training.yaml` — 呼吸訓練生理線（**5 節點**）

| ID | 確定性 | premise/摘要 |
|---|---|---|
| health.breathing.safety | 🟢 |  |
| health.breathing.overview | 🔵 | 『呼吸要不要練、怎麼練』之所以講不清楚，是因為大家把兩件不同的事混在一起。Vortex 把呼吸拆成兩條線：① **感知線**——吐氣連不連續、換氣會不會緊張、兩側順不順，這是水感的 |
| health.breathing.imt_rmt | 🟡 | 用阻力呼吸器練『吸氣的肌肉』，肌肉確實會變強，這點研究很一致。但變強會不會讓你游更快？短距離（50–200）多數研究說沒差，長一點的距離可能有一點點幫助，別期待太大。如果你已經是練 |
| health.breathing.co2_tolerance | 🔴 | 自由潛水那套『閉氣表』在游泳圈很流行，但沒有任何像樣的研究證明它能讓你游更快——這是從別的運動硬搬過來的說法。真要練 CO2 耐受，只在陸上、找人陪、別獨自做；而且永遠不要把閉氣帶 |
| health.breathing.grading | 🔵 | 『純粹的呼吸訓練能不能分級？』能，但要看哪一條線，而且分級的軸不一樣： |

---

## 心理 `canonical/psychology/`

### `psychology.yaml` — 心理（**8 themes / 62 concepts**）

| ID | 主題 | 狀態 | 概念數 | L 範圍 | 使用情境 |
|---|---|---|---|---|---|
| psych.fear | 水中恐懼 | complete | 7 | L0–L2 | 還不敢放手、一下水就僵、怕到不敢開始時 |
| psych.interaction | 心理–感知–生理交互 | complete | 8 | L0–L2 | 不怕了，但一緊張身體就僵、換氣一亂整個垮時 |
| psych.motivation | 動機與動機氣候 | complete | 9 | L0–L6 | 提不起勁、練不下去、想找回能一直練下去的動力時 |
| psych.imagery | 意象與心理演練 | complete | 6 | L0–L6 | 想用想像在岸上補練、強化動作記憶時 |
| psych.attention | 注意力焦點 | complete | 6 | L3–L6 | 一上場就分心、不知道該把注意力放哪時 |
| psych.self_talk | 自我對話與心理技能 | complete | 8 | L3–L6 | 腦中雜念停不下、想用自我喊話穩住表現時 |
| psych.arousal | 喚醒、焦慮與壓力崩潰 | complete | 8 | L3–L6 | 一比賽就緊到崩、越想控制越糟時 |
| psych.flow | 心流與去再投資 | complete | 10 | L3–L6 | 想進入忘我、把好表現守在壓力下時 |

---

## 練習 `Drills/`

### `drills_freestyle.yaml` — freestyle (**44 drills**)

**難度分布**：{'foundation': 9, 'intermediate': 13, 'advanced': 14, 'elite': 8}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| Fr1 | 站姿呼吸 | breathing | L0 | foundation | freestyle |
| Fr2 | 頭帶平衡 — 面朝下 | balance | L1 | foundation | freestyle |
| Fr3 | 頭帶平衡 — 側躺 | balance | L1 | foundation | freestyle |
| Fr4 | 頭帶平衡 + 旋轉 | balance | L1 L2 | intermediate | freestyle |
| Fr5 | 超人踢水 | kick | L1 L2 | foundation | freestyle |
| Fr6 | 手臂主導平衡（六拍） | balance | L2 L3 | intermediate | freestyle |
| Fr7 | 流線踢水 | kick | L1 L2 | foundation | freestyle |
| Fr8 | 垂直踢水 | kick | L2 L3 | intermediate | freestyle |
| Fr9 | 360度滾轉 | balance | L2 L3 | intermediate | freestyle |
| Fr10 | 帆船划手 | arm | L3 L4 | advanced | freestyle |
| Fr11 | 單臂划手 | arm | L3 L4 | advanced | freestyle |
| Fr12 | 指尖拖水 | arm | L3 | intermediate | freestyle |
| Fr13 | 描黑線 | arm | L2 L3 | intermediate | freestyle |
| Fr14 | 水下溜冰（水下恢復臂） | arm | L3 L4 | advanced | freestyle |
| Fr15 | 超人趕上 | arm | L3 L4 | advanced | freestyle |
| Fr16 | 握拳划手 | arm | L3 L4 | intermediate | freestyle |
| Fr17 | 三點觸碰 | arm | L2 L3 | advanced | freestyle |
| Fr18 | 懸空手 | balance | L3 L4 | advanced | freestyle |
| Fr19 | 水球式自由式 | arm | L3 | intermediate | freestyle |
| Fr20 | 高爾夫計分 | timing | L4 L5 | advanced | freestyle |
| Fr21 | 靜音入水 | arm | L4 L5 | advanced | freestyle |
| Fr22 | 無氣泡 | arm | L4 L5 | advanced | freestyle |
| Fr23 | 三划滑行 | timing | L3 L4 | intermediate | freestyle |
| Fr24 | 俄式滾轉 | timing | L3 L4 | advanced | freestyle backstroke |
| FrBr1 | 水中吐氣節律（韻律呼吸） | breathing | L0 | foundation | freestyle |
| FrBr2 | 放鬆下沉 | breathing | L0 | foundation | freestyle |
| FrBr3 | 連續涓流吐氣 | breathing | L1 | intermediate | freestyle |
| FrBr4 | 兩側換氣（每三划） | breathing | L2 | intermediate | freestyle |
| FrEC1 | 閉眼超人趕上 | arm | L3 L4 | advanced | freestyle |
| FrPad1 | 手掌板捕水靜止 | arm | L3 L4 | advanced | freestyle |
| FrSt1 | 站姿高肘軌跡描繪 | arm | L1 L2 | foundation | freestyle |
| FrP1 | 同伴擊掌恢復臂 | arm | L3 | intermediate | freestyle |
| FrP2 | 同伴阻力帶拖游 | timing | L4 L5 | advanced | freestyle |
| FrSide1 | 側躺前手錨定捕水 | arm | L3 L4 | advanced | freestyle |
| FrSide2 | 側躺滑行壓力檢查 | balance | L2 L3 | intermediate | freestyle |
| FrLow1 | 戴呼吸管輕鬆捕水 | arm | L2 L3 | foundation | freestyle |
| FrEL1 | 六踢換邊（蛙鞋+呼吸管） | timing | L5 | elite | freestyle |
| FrEL2 | 四踢二划（衝刺節律） | timing | L5 | elite | freestyle |
| FrEL3 | Snap 手掌板（爆發捕水） | arm | L5 | elite | freestyle |
| FrEL4 | 高肘撥水（手掌板+蛙鞋+呼吸管） | sculling | L5 | elite | freestyle |
| FrEL5 | Race Club 全身旋轉 | timing | L5 | elite | freestyle |
| FrEL6 | 波頂入水 vs 波底入水 | arm | L5 L6 | elite | freestyle |
| FrEL7 | 比賽配速短反覆（呼吸管+蛙鞋） | timing | L5 L6 | elite | freestyle |
| FrEL8 | 三秒暫停趕上 | timing | L5 | elite | freestyle |

### `drills_backstroke.yaml` — backstroke (**32 drills**)

**難度分布**：{'foundation': 7, 'intermediate': 12, 'advanced': 11, 'elite': 2}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| Bk1 | 仰式流線踢水 | kick | L1 L2 | foundation | backstroke |
| Bk2 | 交叉手踢水 | kick | L1 | foundation | backstroke |
| Bk3 | 浮板壓腿踢水 | kick | L2 | intermediate | backstroke |
| Bk4 | 頭帶側身平衡踢水 | balance | L1 | foundation | backstroke |
| Bk5 | 頭帶平衡旋轉踢水 | balance | L1 L2 | intermediate | backstroke |
| Bk6 | 超人仰式踢水 | kick | L1 L2 | foundation | backstroke |
| Bk7 | 垂直仰式踢水 | kick | L2 L3 | intermediate | backstroke |
| Bk8 | 手臂主導平衡 | balance | L2 L3 | foundation | backstroke |
| Bk9 | 交替手臂主導 | balance | L3 L4 | intermediate | backstroke |
| Bk10 | 頭帶平衡＋四分之一抬臂 | timing | L3 L4 | intermediate | backstroke |
| Bk11 | 仰式趕上 | timing | L3 L4 | intermediate | backstroke |
| Bk12 | 雙臂同步仰式 | arm | L2 L3 | intermediate | backstroke |
| Bk13 | 單臂仰式 | arm | L3 L4 | advanced | backstroke |
| Bk14 | L形鑽 | timing | L3 L4 | advanced | backstroke |
| Bk15 | 快速L形切換 | timing | L4 L5 | advanced | backstroke |
| Bk16 | L形切換接正式仰式 | timing | L4 L5 | advanced | backstroke |
| Bk17 | 暫停點 | timing | L4 L5 | advanced | backstroke |
| Bk18 | 指天 | kick | L4 L5 | advanced | backstroke |
| Bk19 | 握拳仰式 | arm | L3 L4 | intermediate | backstroke |
| Bk20 | 俄式滾轉（仰式） | timing | L3 L4 | advanced | backstroke freestyle |
| Bk21 | 三划滑行（仰式） | timing | L3 | intermediate | backstroke |
| Bk22 | 泳鏡平衡 | balance | L1 L2 | foundation | backstroke |
| Bk23 | 高速仰式 | timing | L5 | elite | backstroke |
| Bk24 | 仰式拉力板 | arm | L4 L5 | advanced | backstroke |
| Bk25 | 加速入水 | arm | L4 L5 | advanced | backstroke |
| Bk26 | 水線輔助拉水 | arm | L3 | intermediate | backstroke |
| BkEC1 | 閉眼仰式流線踢水 | kick | L2 L3 | intermediate | backstroke |
| BkPad1 | 手掌板仰式拉手 | arm | L4 L5 | advanced | backstroke |
| BkSt1 | 站姿仰式划手模擬 | arm | L1 L2 | foundation | backstroke |
| BkP1 | 同伴並肩配速仰式 | timing | L4 L5 | advanced | backstroke |
| BkLow1 | 六踢換邊 | timing | L2 L3 | intermediate | backstroke |
| BkEL1 | 仰式 6K1S（蛙鞋） | timing | L5 | elite | backstroke |

### `drills_breaststroke.yaml` — breaststroke (**38 drills**)

**難度分布**：{'foundation': 6, 'intermediate': 15, 'advanced': 14, 'elite': 3}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| Br1 | 牆邊蛙式腿 | kick | L2 | foundation | breaststroke |
| Br2 | 打蛋器踢水 | kick | L2 | foundation | breaststroke |
| Br3 | 垂直蛙式踢腿 | kick | L2 L3 | intermediate | breaststroke |
| Br4 | 垂直踢腿流線臂 | kick | L3 | advanced | breaststroke |
| Br5 | 浮力棒踢腿 | kick | L2 L3 | intermediate | breaststroke |
| Br6 | 手放臀部面朝下踢腿 | kick | L2 L3 | intermediate | breaststroke |
| Br7 | 手放臀部面朝上踢腿 | kick | L2 L3 | intermediate | breaststroke |
| Br8 | 超人蛙式踢腿 | kick | L3 | intermediate | breaststroke |
| Br9 | 仰面超人蛙式踢腿 | kick | L2 L3 | intermediate | breaststroke |
| Br10 | 墓碑浮板踢腿 | kick | L3 L4 | advanced | breaststroke |
| Br11 | Barrowman腿（交替踢） | kick | L4 L5 | advanced | breaststroke |
| Br12 | 蛙式手臂外撇 | arm | L2 L3 | foundation | breaststroke |
| Br13 | 蛙式泡麵條輔助拉手 | arm | L2 L3 | foundation | breaststroke |
| Br14 | 高肘支撐練習 | arm | L3 | intermediate | breaststroke |
| Br15 | 蛙式拉手＋自由式踢水 | arm | L3 L4 | intermediate | breaststroke |
| Br16 | 蛙式拉手＋蝶式踢水 | arm | L3 L4 | advanced | breaststroke |
| Br17 | 眼鏡蛇 | timing | L4 L5 | advanced | breaststroke |
| Br18 | 單臂蛙式 | arm | L3 | intermediate | breaststroke |
| Br19 | 握拳蛙式 | arm | L3 L4 | intermediate | breaststroke |
| Br20 | 時速拉手 | timing | L4 L5 | elite | breaststroke |
| Br21 | 潛水下衝 | timing | L4 L5 | advanced | breaststroke |
| Br22 | 平面蛙式拉手 | arm | L3 L4 | intermediate | breaststroke |
| Br23 | 水下波動 | timing | L4 L5 | advanced | breaststroke |
| Br24 | 踢腿潛水遞進 | timing | L4 L5 | advanced | breaststroke |
| Br25 | 抬頭快速前推 | arm | L4 L5 | advanced | breaststroke |
| Br26 | 戴呼吸管游蛙式 | arm | L2 L3 | foundation | breaststroke |
| Br27 | 水下完整蛙式 | timing | L4 | advanced | breaststroke |
| Br28 | 仰面水下蛙式 | timing | L4 | advanced | breaststroke |
| Br29 | 正仰面組合 | timing | L4 | advanced | breaststroke |
| Br30 | 拉停踢停 | timing | L3 L4 | intermediate | breaststroke |
| Br31 | 重疊時序 | timing | L5 | elite | breaststroke |
| Br32 | 划次速度訓練 | timing | L5 | elite | breaststroke |
| Br33 | 短軸組合（蛙蝶） | timing | L4 L5 | advanced | breaststroke butterfly |
| Br34 | 冰凍頭部 | arm | L3 L4 | intermediate | breaststroke |
| BrEC1 | 閉眼水下流線蛙式拉手 | timing | L4 | advanced | breaststroke |
| BrPad1 | 手掌板蛙式外撇 | arm | L3 L4 | intermediate | breaststroke |
| BrSt1 | 站姿牆邊流線設定 | balance | L1 L2 | foundation | breaststroke |
| BrLow1 | 拉拉踢 | timing | L2 L3 | intermediate | breaststroke |

### `drills_butterfly.yaml` — butterfly (**34 drills**)

**難度分布**：{'foundation': 3, 'intermediate': 7, 'advanced': 22, 'elite': 2}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| Fl1 | 胸部下壓 | kick | L1 L2 | foundation | butterfly |
| Fl2 | 手放兩側蝶式踢腿 | kick | L2 | foundation | butterfly underwater_dolphin_kick |
| Fl3 | 胸部下壓小指朝上 | kick | L2 L3 | intermediate | butterfly |
| Fl4 | 仰面雙臂上舉蝶腿 | kick | L3 L4 | advanced | butterfly underwater_dolphin_kick |
| Fl5 | 仰面流線蝶腿 | kick | L2 L3 | intermediate | butterfly underwater_dolphin_kick |
| Fl6 | 側面蝶腿踢水 | kick | L3 | advanced | butterfly underwater_dolphin_kick |
| Fl7 | 衝浪蝶腿 | kick | L3 L4 | advanced | butterfly underwater_dolphin_kick |
| Fl8 | 水下蝶腿 | kick | L3 L4 | advanced | butterfly underwater_dolphin_kick |
| Fl9 | 鯨魚仰式蝶腿 | kick | L3 L4 | advanced | butterfly underwater_dolphin_kick |
| Fl10 | 垂直蝶腿 | kick | L3 L4 | advanced | butterfly underwater_dolphin_kick |
| Fl11 | 蝶腿360度 | kick | L4 | advanced | butterfly underwater_dolphin_kick |
| Fl12 | 跨過木桶 | kick | L3 L4 | advanced | butterfly |
| Fl13 | 天使翅膀 | arm | L2 L3 | intermediate | butterfly |
| Fl14 | 天使翅膀接完整蝶式 | arm | L3 L4 | advanced | butterfly |
| Fl15 | 蝶式划手跑直線 | arm | L3 L4 | advanced | butterfly |
| Fl16 | 外划到組合 | arm | L3 L4 | advanced | butterfly |
| Fl17 | 蝶式恢復臂（水下） | timing | L4 L5 | advanced | butterfly |
| Fl18 | 單臂蝶式 | arm | L3 L4 | advanced | butterfly |
| Fl19 | 二二二組合 | arm | L4 | advanced | butterfly |
| Fl20 | 保持低位換氣 | timing | L4 L5 | advanced | butterfly |
| Fl21 | 深度捕水 | arm | L4 L5 | advanced | butterfly |
| Fl22 | 拇指拖水恢復 | arm | L3 L4 | intermediate | butterfly |
| Fl23 | 球拋練習 | kick | L4 | advanced | butterfly |
| Fl24 | 輕鬆恢復蝶式 | arm | L3 | intermediate | butterfly |
| Fl25 | 慢速前恢復 | arm | L3 L4 | advanced | butterfly |
| Fl26 | 三角形（Biondi）鑽 | timing | L4 L5 | advanced | butterfly |
| Fl27 | 每划四踢 | timing | L4 L5 | elite | butterfly |
| Fl28 | 垂直蝶式 | timing | L5 L6 | elite | butterfly |
| Fl29 | 泡棉滾筒高肘捕水 | arm | L3 L4 | intermediate | butterfly |
| Fl30 | 破水動作 | timing | L4 L5 | advanced | butterfly starts_turns |
| Fl31 | 短軸組合（蝶蛙） | timing | L4 L5 | advanced | butterfly breaststroke |
| FlEC1 | 閉眼蝶腿 | kick | L3 L4 | intermediate | butterfly underwater_dolphin_kick |
| FlPad1 | 手掌板水下恢復臂 | arm | L4 L5 | advanced | butterfly |
| FlSt1 | 站姿胸壓+髖前後 | kick | L1 L2 | foundation | butterfly |

### `drills_sculling.yaml` — sculling (**12 drills**)

**難度分布**：{'intermediate': 4, 'advanced': 8}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| Sc1 | 寬Y型划水 | sculling | L2 L3 | intermediate | freestyle backstroke breaststroke butterfly |
| Sc2 | 頭朝下划水（窄Y） | sculling | L2 L3 | intermediate | freestyle breaststroke butterfly |
| Sc3 | 頭朝上划水 | sculling | L2 L3 | advanced | freestyle breaststroke butterfly |
| Sc4 | 雨刷划水（頭朝下） | sculling | L3 L4 | advanced | breaststroke butterfly |
| Sc5 | 雨刷划水（下巴朝上） | sculling | L3 L4 | advanced | breaststroke butterfly |
| Sc6 | 腳先行划水 | sculling | L2 L3 | intermediate | freestyle backstroke breaststroke butterfly |
| Sc7 | 髖部划水 | sculling | L3 | intermediate | freestyle backstroke butterfly |
| Sc8 | 坐姿划水 | sculling | L3 L4 | advanced | breaststroke |
| Sc9 | 單臂划水 | sculling | L3 L4 | advanced | breaststroke butterfly |
| Sc10 | 頭後方划水 | sculling | L3 L4 | advanced | backstroke |
| ScFist | 握拳划水 | sculling | L3 L4 | advanced | freestyle breaststroke butterfly |
| ScUW1 | 水下寬 Y 懸停 | sculling | L4 | advanced | freestyle breaststroke butterfly |

### `drills_starts-turns.yaml` — starts-turns (**9 drills**)

**難度分布**：{'foundation': 1, 'intermediate': 2, 'advanced': 2, 'elite': 4}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| ST1 | 中池翻滾 | turn | L1 L2 | foundation | starts_turns |
| ST2 | 翻牆踩牆（腳尖朝上） | turn | L2 L3 | intermediate | starts_turns |
| ST3 | 蹬牆流線測距 | turn | L2 L3 | intermediate | starts_turns |
| ST4 | 仰式旗下數划手 | turn | L3 L4 | advanced | starts_turns |
| ST5 | 蹬牆轉體出水 | turn | L3 L4 | advanced | starts_turns |
| STSpat1 | 閉眼靠水聲判斷牆距 | turn | L5 | elite | starts_turns |
| STEL1 | 仰式階梯式出發 | turn | L5 | elite | starts_turns |
| STEL2 | 仰式出發腿驅動跳 | turn | L5 L6 | elite | starts_turns |
| STEL3 | 仰式出發踢沙灘球 | turn | L5 L6 | elite | starts_turns |

### `drills_udk.yaml` — udk (**7 drills**)

**難度分布**：{'intermediate': 2, 'advanced': 2, 'elite': 3}

| ID | 中文名 | 類別 | L 目標 | 難度 | 適用泳式 |
|---|---|---|---|---|---|
| UDK1 | 垂直打水 | kick | L2 L3 | intermediate | underwater_dolphin_kick |
| UDK2 | 流線打水換面（仰／側／俯） | kick | L4 L5 | advanced | underwater_dolphin_kick |
| UDK3 | 繫繩最大努力海豚腳 | kick | L4 L5 | elite | underwater_dolphin_kick |
| UDK4 | 節拍器找個人打水頻率 | kick | L4 L5 | elite | underwater_dolphin_kick |
| UDK5 | 比賽配速水下打水 | kick | L5 L6 | elite | underwater_dolphin_kick |
| UDKEC1 | 閉眼垂直蝶腿 | kick | L4 | advanced | underwater_dolphin_kick |
| UDKLow1 | 戴呼吸管水下巡航 | kick | L3 | intermediate | underwater_dolphin_kick |
