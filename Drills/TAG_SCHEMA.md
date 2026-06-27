# Drill Tag Schema — 9 軸特色指紋

> 補充 `DRILL_INDEX.md`：擴充原本稀薄的 `category/l_target/abc_type` 三軸到 9 軸正交標籤。
> 目的：每個 drill 有獨特指紋，可從 9 個角度被檢索，避免「39 個 arm drill 全擠一起」。
>
> 版本：v1.0 (2026-06-27)

---

## 設計原則

1. **正交**：9 軸彼此獨立，每軸都對 drill 提供新資訊
2. **互斥 enum**：除特別標示「可多選」外，每軸只挑一個值
3. **保留既有欄位**：`category / l_target / abc_type / equipment / strokes / deficiency_fixes` 全部不動，9 軸是附加
4. **避免「unknown / null」**：每個 drill 必須完整 9 軸，沒有適用情境也要做出最近的判斷
5. **指紋唯一性**：同泳式內若兩個 drill 9 軸完全相同 → 標籤定義太粗 / 該 drill 真的重複

---

## 9 軸定義

### 1. `body_position`（互斥）

身體在水中的擺法。

| 值 | 判別 |
|---|---|
| `standing` | 雙腳踩池底（含彎腰把臉放水裡） |
| `vertical` | 身體垂直、雙腳離地（垂直踢水、treading water） |
| `prone` | 俯臥水平（臉朝下） |
| `supine` | 仰躺水平（臉朝上） |
| `side` | 側躺（含 45° 半側） |
| `underwater` | 整段在水面下（含 UDK、潛行） |
| `transitional` | 持續在多姿勢間切換（360° 滾轉、旋轉 drill） |

### 2. `constraints`（可多選 0–3 個；空陣列代表無限制）

把什麼元素拿掉 / 限制，讓某種感知浮出來。

| 值 | 判別 |
|---|---|
| `no_arms` | 雙手不划（手放大腿 / 手抱浮板 / streamline） |
| `single_arm` | 只用一手划（另一手前伸或貼身） |
| `closed_fist` | 握拳 / 戴拳套 |
| `paddle_amplifier` | 戴手掌板放大感知（非減去） |
| `no_kick` | 不踢腳（pull buoy / 腳交叉） |
| `single_leg` | 只用一腳踢 |
| `no_breath` | 不換氣（屏氣 / 短池無呼吸） |
| `breath_added` | 在原本不換氣 drill 加入換氣 |
| `eyes_closed` | 閉眼 / 戴遮蔽鏡 |
| `tempo_constrained` | 用 tempo trainer 限定節奏 |
| `tension_held` | 必須維持特定肌張力（如腳交叉、夾浮板） |

### 3. `movement_pattern`（互斥）

動作的時間型態。

| 值 | 判別 |
|---|---|
| `static` | 在原地不前進 |
| `progressive` | 慢速前進，重點不是速度 |
| `continuous` | 連續穩定游 |
| `pause_pulse` | 動一下停一下（catch-up、單臂等劃完才換邊） |
| `alternating` | 規律左右 / 兩種姿勢交替（如 3-3-3 切換） |
| `rotational` | 主軸是旋轉本身（360° 滾轉、screw kick） |

### 4. `skill_focus`（可多選 1–2 個）

drill 主要建立的感知標的。**最多 2 個**，超過代表 drill 散焦。

| 值 | 判別 |
|---|---|
| `breath_rhythm` | 吐氣節律、換氣時機 |
| `streamline_line` | 流線體線、頭頸對齊 |
| `buoyancy_balance` | 浮力配置、漂浮平衡 |
| `core_tension` | 核心收緊、肋骨穩定 |
| `hip_drive` | 髖部啟動旋轉 / 推進 |
| `catch_evf` | 早期垂直前臂、捕水高肘 |
| `forearm_pressure` | 前臂全長壓水感 |
| `hand_acceleration` | 手部加速 / 推水末段 |
| `entry_extension` | 入水點 + 前伸延展 |
| `recovery_path` | 移臂路徑（高肘 / 鬆肩 / 圓滑） |
| `kick_origin` | 踢水從髖啟動非膝蓋 |
| `kick_amplitude` | 踢水振幅大小控制 |
| `wave_undulation` | 蝶蛙波動傳遞 |
| `rotation_connection` | 上下身旋轉同步 |
| `rhythm_tempo` | 整體節奏 / 划頻控制 |
| `spatial_awareness` | 水道 / 牆 / 池底空間定位 |
| `pressure_mapping` | 全身水壓分布感知 |
| `glide_efficiency` | 滑行段距離效率 |

### 5. `stroke_phase`（互斥）

對應划水週期哪一段。

| 值 | 判別 |
|---|---|
| `entry` | 入水點 |
| `catch` | 抓水（手剛沉入待出力前） |
| `pull` | 前抓 → 中段（手到肩下） |
| `push` | 中段 → 出水（手到大腿） |
| `recovery` | 移臂出水到再入水 |
| `glide` | 滑行 / 延伸期 |
| `transition` | 相位轉換（如蛙腿到划手） |
| `whole_stroke` | 整個動作週期 |
| `non_stroke` | 不直接對應划水（純呼吸 / 平衡 / 踢水） |

### 6. `drill_function`（互斥）

在訓練流程中的角色。

| 值 | 判別 |
|---|---|
| `warmup` | 熱身就能做、低強度 |
| `corrective` | 矯正特定錯誤動作 |
| `skill_isolation` | 把單一技巧孤立出來練 |
| `skill_integration` | 把已建立技巧整合進完整泳姿 |
| `progression` | 連續加難度的階梯式 drill |
| `pre_main_set` | 主項目前活化感知 |
| `cooldown` | 緩和、技術性放鬆 |

### 7. `cognitive_load`（互斥）

需要的專注程度，決定能否在疲勞下做。

| 值 | 判別 |
|---|---|
| `low` | 簡單 cue、疲勞下仍可維持 |
| `medium` | 需要一個關鍵 cue |
| `high` | 多個 cue 同時、無法分心 |

### 8. `tactile_anchor`（互斥）

「做對了」的回饋訊號從哪來。

| 值 | 判別 |
|---|---|
| `pool_floor_visual` | 視覺：看池底線 |
| `hand_pressure` | 手掌 / 前臂感受到水壓 |
| `foot_pressure` | 腳掌 / 腳背感受到水壓 |
| `core_tension_internal` | 內部肌張力（沒有外部信號，靠本體感覺） |
| `wall_contact` | 牆面 / 池邊接觸 |
| `water_sound` | 聲音（水煮沸 vs 大濺水） |
| `partner_feedback` | 同伴或教練的外部回饋 |
| `equipment_feedback` | 浮板、tempo trainer、snorkel 等器材給的訊號 |
| `surface_break` | 換氣破水 / 不破水時機 |

### 9. `difficulty_tier`（互斥）

執行門檻，**獨立於 L 級**（L 是感知深度，這是動作難度）。

| 值 | 判別 |
|---|---|
| `foundation` | 完全新手能做 |
| `intermediate` | 有基本游姿後能做 |
| `advanced` | 需要可靠的某項感知才能做 |
| `elite` | 比賽級技術門檻 |

---

## YAML 格式

附加在每個 drill 既有欄位之後，順序固定：

```yaml
  - id: Fr1
    name_en: "Standing Breathing"
    name_zh: "站姿呼吸"
    strokes: [freestyle]
    category: breathing
    equipment: []
    l_target: [L0]
    abc_type: null
    purpose_zh: "..."
    how_to: [...]
    perception_goal: "..."
    success_signal: "..."
    failure_signal: "..."
    deficiency_fixes: [1, 2]
    source: "There's a Drill for That"
    # === 9 軸特色指紋 (v1.0) ===
    body_position: standing
    constraints: []
    movement_pattern: static
    skill_focus: [breath_rhythm]
    stroke_phase: non_stroke
    drill_function: warmup
    cognitive_load: low
    tactile_anchor: pool_floor_visual
    difficulty_tier: foundation
```

---

## 自我檢查清單

完成一個泳式檔後跑：

1. **完整性**：每個 drill 9 軸都有值，沒有空字串 / null（`constraints: []` 是合法值）
2. **指紋唯一性**：同泳式內無兩個 drill 9 軸完全相同；發現重複 → 拆細其一的標籤
3. **反推測試**：隨機抽 3 個 drill，只看 9 軸能否反推回 `purpose_zh` 大意；不能 → 標籤判斷錯
4. **focus 散焦**：`skill_focus` 超過 2 個 → 必須拆細或重判
5. **L 與 difficulty 對齊不強制**：L0 drill 可以是 elite（蝶式呼吸給菁英）；不要把 L 自動映射成 difficulty
