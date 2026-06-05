# Vortex Drill Database — Index

> Source: *There's a Drill for That* (Laurie Sherret)  
> Perception layer mapping: Vortex L0–L6 framework (Hangsau 2026)  
> Total: 125 drills (Fr24 + Bk26 + Br34 + Fl31 + Sc10)

## Files

| File | Count | Content |
|------|-------|---------|
| `drills_freestyle.yaml` | 24 | Fr1–Fr24 |
| `drills_backstroke.yaml` | 26 | Bk1–Bk26 |
| `drills_breaststroke.yaml` | 34 | Br1–Br34 |
| `drills_butterfly.yaml` | 31 | Fl1–Fl31 |
| `drills_sculling.yaml` | 10 | Sc1–Sc10 |

## YAML Schema

```yaml
- id: "Fr1"                        # 唯一 ID
  name_en: "Standing Breathing"    # 英文名稱
  name_zh: "站姿呼吸"               # 中文名稱
  strokes: [freestyle]             # 適用泳式：freestyle / backstroke / breaststroke / butterfly / underwater_dolphin_kick / starts_turns / all
  category: breathing              # breathing / kick / arm / balance / timing / sculling / awareness
  equipment: []                    # [] / fins / kickboard / pull_buoy / snorkel / foam_roller / noodle / ball / partner / lane_line
  l_target: [L0]                   # Vortex L 級別：L0–L6（可多個）
  abc_type: null                   # A型（手感缺失）/ B型（腳感缺失）/ C型（全身張力）/ null（通用）
  purpose_zh: "brief purpose"      # 動作目的（中文）
  perception_goal: "..."           # 應該感覺到什麼（中文）
  success_signal: "..."            # 感知成功的樣子（中文）
  failure_signal: "..."            # 感知失敗的樣子（中文）
  deficiency_fixes: [1, 2]         # 對應書中 Common Stroke Deficiencies 編號
  source: "There's a Drill for That"
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
- **呼吸**：Fr1, Br12（蛙式換氣相關）
- **踢水**：Fr2–Fr9, Bk1–Bk7, Br1–Br11, Fl1–Fl12
- **捕水/EVF**：Fr10–Fr16, Bk8–Bk16, Br12–Br20, Fl12–Fl17
- **划水感知**：Sc1–Sc10（所有泳式適用）
- **時序整合**：Fr20, Fr23–Fr24, Br17, Br30–Br31, Fl26–Fl27
