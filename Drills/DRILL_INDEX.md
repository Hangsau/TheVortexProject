# Vortex Drill Database — Index

> Sources: *There's a Drill for That* (Laurie Sherret) + *Fundamentals of Fast Swimming* (The Race Club / Gary Hall Sr) + Vortex 整理（呼吸、UDK、starts-turns、gap fills）  
> Perception layer mapping: Vortex L0–L6 framework (Hangsau 2026)  
> 9-axis tag fingerprint v1.0 (2026-06-27): 見 `TAG_SCHEMA.md`  
> Total: **176 drills** (Fr44 + Bk32 + Br38 + Fl34 + Sc12 + ST9 + UDK7)；其中 **22 elite**

## Files

| File | Count | Content |
|------|-------|---------|
| `drills_freestyle.yaml` | 44 | Fr1–Fr24 + FrBr1–FrBr4（呼吸）+ FrEC1/FrPad1/FrSt1/FrP1/FrP2/FrSide1/FrSide2/FrLow1（gap fills）+ FrEL1–FrEL8（Race Club elite） |
| `drills_backstroke.yaml` | 32 | Bk1–Bk26 + BkEC1/BkPad1/BkSt1/BkP1/BkLow1（gap fills）+ BkEL1（Race Club elite） |
| `drills_breaststroke.yaml` | 38 | Br1–Br34 + BrEC1/BrPad1/BrSt1/BrLow1（gap fills） |
| `drills_butterfly.yaml` | 34 | Fl1–Fl31 + FlEC1/FlPad1/FlSt1（gap fills） |
| `drills_sculling.yaml` | 12 | Sc1–Sc10 + ScFist/ScUW1（gap fills） |
| `drills_starts-turns.yaml` | 9 | ST1–ST5 + STSpat1（gap fills）+ STEL1–STEL3（Race Club 仰式出發） |
| `drills_udk.yaml` | 7 | UDK1–UDK5 + UDKEC1/UDKLow1（gap fills） |

## YAML Schema

既有欄位 + 9 軸 fingerprint（見 `TAG_SCHEMA.md`）：

```yaml
- id: "Fr1"                        # 唯一 ID
  name_en: "Standing Breathing"    # 英文名稱
  name_zh: "站姿呼吸"               # 中文名稱
  strokes: [freestyle]             # 適用泳式：freestyle / backstroke / breaststroke / butterfly / underwater_dolphin_kick / starts_turns
  category: breathing              # breathing / kick / arm / balance / timing / sculling / turn
  equipment: []                    # [] / fins / kickboard / pull_buoy / snorkel / foam_roller / noodle / ball / partner / lane_line / paddles / tubing / tempo_trainer / small_object
  l_target: [L0]                   # Vortex L 級別：L0–L6（可多個）
  abc_type: null                   # A型（手感缺失）/ B型（腳感缺失）/ C型（全身張力）/ null（通用）
  purpose_zh: "brief purpose"      # 動作目的（中文）
  how_to: [...]                    # 操作步驟
  perception_goal: "..."           # 應該感覺到什麼（中文）
  success_signal: "..."            # 感知成功的樣子（中文）
  failure_signal: "..."            # 感知失敗的樣子（中文）
  deficiency_fixes: [1, 2]         # 對應書中 Common Stroke Deficiencies 編號
  source: "There's a Drill for That"
  # === 9-axis fingerprint ===
  body_position: standing          # standing / vertical / prone / supine / side / underwater / transitional
  constraints: []                  # 多選：no_arms / single_arm / closed_fist / paddle_amplifier / no_kick / single_leg / no_breath / breath_added / eyes_closed / tempo_constrained / tension_held
  movement_pattern: static         # static / progressive / continuous / pause_pulse / alternating / rotational
  skill_focus: [breath_rhythm]     # 1-2 個：見 TAG_SCHEMA.md §4
  stroke_phase: non_stroke         # entry / catch / pull / push / recovery / glide / transition / whole_stroke / non_stroke
  drill_function: warmup           # warmup / corrective / skill_isolation / skill_integration / progression / pre_main_set / cooldown
  cognitive_load: low              # low / medium / high
  tactile_anchor: pool_floor_visual  # pool_floor_visual / hand_pressure / foot_pressure / core_tension_internal / wall_contact / water_sound / partner_feedback / equipment_feedback / surface_break
  difficulty_tier: foundation      # foundation / intermediate / advanced / elite
```

## L 級對應說明

| L 級 | 感知狀態 | 對應動作層次 |
|------|----------|--------------|
| L0 | 呼吸感知建立 | 呼吸節律、基本換氣 |
| L1 | 基礎平衡/流線 | 身體對齊、漂浮平衡 |
| L2 | 推進感萌芽 | 踢腿前進、手部水壓初步 |
| L3 | 水感出現但不穩定 | 捕水、EVF、節律感知 |
| L4 | 壓力下感知失守 | 速度/疲勞下的技術維持 |
| L5 | 感知自動化過渡 | 高速下穩定，精英技術特徵 |
| L6 | 感知自動化完成 | 疲勞下不崩潰，持續精煉 |

## A/B/C 型診斷

- **A型**：手感缺失，EVF 崩潰，只靠手掌划水 → 優先做 arm 類 drill
- **B型**：腳感缺失，踢水節律失守 → 優先做 kick 類 drill  
- **C型**：全身張力問題，換氣或轉體觸發感知遮蔽 → 優先做 balance / timing 類 drill

## 快速查找

### 按泳式
- 自由式：Fr1–Fr24
- 仰式：Bk1–Bk26
- 蛙式：Br1–Br34（含 Sc 划水鑽）
- 蝶式：Fl1–Fl31（含 Sc 划水鑽）
- 水下蝶腳：Fl2, Fl4–Fl11 + 所有 underwater_dolphin_kick 標記
- 出發與轉身：Fl30

### 按 L 級（精選）
- **L0**：Fr1（呼吸）
- **L1**：Fr2, Fr3, Fr4, Bk1–Bk5（平衡流線）
- **L2**：Fr5–Fr8, Bk6–Bk7, Br1–Br9, Fl1–Fl3（推進萌芽）
- **L3**：Fr9–Fr19, Bk8–Bk14, Br10–Br23, Fl12–Fl18, Sc1–Sc10
- **L4**：Fr20–Fr24, Bk15–Bk26, Br24–Br32, Fl19–Fl29
- **L5**：Br31–Br32, Fl28, Bk23

### 按類別
- **呼吸**：Fr1, FrBr1–FrBr4, Br12（蛙式換氣相關）
- **踢水**：Fr2–Fr9, Bk1–Bk7, Br1–Br11, Fl1–Fl12
- **捕水/EVF**：Fr10–Fr16, Bk8–Bk16, Br12–Br20, Fl12–Fl17
- **划水感知**：Sc1–Sc10, ScFist, ScUW1（所有泳式適用）
- **時序整合**：Fr20, Fr23–Fr24, Br17, Br30–Br31, Fl26–Fl27

### 按 9 軸 fingerprint（v1.0 新增檢索）
- **熱身專用**（drill_function=warmup）：Fr1, FrBr1, FrSt1, FrLow1, BkSt1, BkLow1, BrSt1, BrLow1, FlSt1, UDKLow1
- **閉眼系列**（constraints includes eyes_closed）：FrEC1, BkEC1, BrEC1, FlEC1, UDKEC1, STSpat1
- **手掌板系列**（constraints includes paddle_amplifier）：FrPad1, BkPad1, BrPad1, FlPad1
- **同伴回饋**（tactile_anchor=partner_feedback）：FrP1, FrP2, BkP1, Fl23 Ball Toss
- **站姿乾預演**（body_position=standing）：Fr1, FrBr1, FrSt1, BkSt1, BrSt1, FlSt1, Br12, Br13
- **垂直水中**（body_position=vertical）：Fr8, Bk7, Br2–Br4, Br14, Fl10, Fl23, Fl28, Sc8, UDK1, UDKEC1, FrBr2
- **水下整段**（body_position=underwater）：Br23, Br27, Br28, Fl8, Fl9, Sc... etc（共 11 個）
- **完整泳式整合**（drill_function=skill_integration）：Fr20, Fr23, Fr24, Bk16, Bk20, Bk21, Br21, Br33, Fl26, Fl27, Fl30, Fl31, ST5, UDK5

跑 `python tools/tag_coverage_report.py` 取得最新完整分布表。
