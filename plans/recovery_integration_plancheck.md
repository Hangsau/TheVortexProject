# 恢復章整合規劃（運動員休息與恢復 → canonical/recovery/）

> 建立：2026-08-12。規劃當下 Claude 7D 配額剩 3%，本檔只做規劃，執行全數留到下一個視窗。
> 來源稿：`C:\claudehome\resources\raw\notes\運動員休息_文獻回顧骨架.md`（500 行，7 章，47 筆參考文獻）

---

## 0. 前置判定（已完成，不必重做）

**來源稿品質**：抽驗 4 筆最吃重引用，4 筆全部真實且描述準確——

| 主張 | 查證 |
|---|---|
| 338 名選手、六成以上 PSQI≥5 | 真實。115 菁英 + 223 次菁英，64% / 65%。即 *Nutrients* 2021, 13(4):1330 |
| 26 篇 RCT 系統回顧，被動恢復反而較優 | 真實。2020，PubMed 32744041 |
| 〈是過度訓練還是敬業精神？〉 | 真實。*Sports* 2021, 9(6):85（Bell et al.） |
| MAC vs 本土化 MAIC 統合分析 | 真實。*Front. Psychol.* 2024, PMC11560761 |

內容非幻覺產物，可以整合。**硬傷只在書目層**：47 筆裡 20 筆是 `(n.d.)` 標題起頭、無作者卷期 DOI；且第四章 16 筆缺 11 筆（69%），正是全稿自稱的差異化章節。另確認一筆重複：`Sleep quality among elite and sub-elite athletes: A survey of 338 competitors. (n.d.)` 與 `The sleep and recovery practices of athletes. (2021). Nutrients` 是同一篇。

---

## 1. 目標

把這篇泛運動恢復科學文獻回顧，整合成 Vortex 的**獨立一章** `canonical/recovery/`，仿呼吸章（`canonical/breathing/`）的多檔結構，約 24 個概念節點，全 public 無 diagnostic 子樹。

**明確不做**：不拆進 psychology-knowledge-atlas / neurochemistry-knowledge-atlas / kinetic-chain-knowledge-atlas。使用者 2026-08-12 決策：「分得太多了，最後都得整合起來」。跨 atlas 的重疊改用 cross-ref 註記，不搬運內容。

---

## 2. 影響範圍

**新增**
- `canonical/recovery/_index.yaml`
- `canonical/recovery/framework.yaml` ← 來源稿第二章
- `canonical/recovery/physiology.yaml` ← 第三章
- `canonical/recovery/mental.yaml` ← 第四章（**不可命名 psychology.yaml**，會與 `canonical/psychology/psychology.yaml` 混淆）
- `canonical/recovery/barriers.yaml` ← 第五章

**修改**
- `canonical/_sources.yaml`：新增約 40 筆來源（去重後）
- `_INDEX.md`：登錄新章
- `HANDOFF.md`：更新進度
- `MAP.md`：canonical 檔案表新增一列
- `C:\claudehome\projects\my-site\tools\sync_vortex.py`：**路徑寫死在第 25–63 行，不改這裡新章不會上站**

**刪除**
- `resources/raw/notes/運動員休息_文獻回顧骨架.md`（`resources/CLAUDE.md` 規定 raw/notes 整合後立即刪除，不存檔）

**不動**
- `canonical/periodization/`（Bompa 週期化）。恢復章與它是姊妹章，用 cross-ref 互指。來源稿第二章對超補償模型的批判**會與 periodization 現有內容產生張力**，見風險 R2。

---

## 3. 執行路徑

派工欄位依 `C:\claudehome\DELEGATION_METHODOLOGY.md` 標註。

### W0　書目補完（前置，不可跳過）　`[delegate: haiku]`

把 20 筆 `(n.d.)` 回資料庫補完整書目（作者、年份、期刊、卷期、DOI/PMID），併掉 338 那筆重複條目。輸出成一份對照表 `plans/recovery_sources_resolved.md`，格式：`原標題 | 完整書目 | DOI或PMID | 查無此文則標 NOT_FOUND`。

**為什麼必須先做**：`_sources.yaml` registry 目前 477 筆，verified 93 / unverified 384，而 S3c 作者年份批次正在清理中。現在直接灌 20 筆無 metadata 進去，等於在清理進行中往裡面倒更多 unverified，會加重 S3c 負擔。

**驗收**：NOT_FOUND 比例 > 25% 就停下回報，代表來源稿可信度需要重新評估（目前抽驗 4/4 全中，預期 NOT_FOUND 應該很低）。

### W1　落點與 schema 確認　`[manual]`

三件事，全部是讀檔，很便宜：

1. 讀 `canonical/psychology/psychology.yaml` 的 8 個 themes 清單。**若其中已有「倦怠 / 恢復 / 動機耗竭」相關 theme（目前 7 個 status: planned，未確認主題名）**，第四章內容改為併入該 theme，不另開 `recovery/mental.yaml`。這是本規劃唯一的未確認前提。
2. 讀 `canonical/breathing/framework.yaml` 前 80 行，確認獨立章的 theme/concept 欄位實際寫法（psychology.yaml 的 schema 已知，但呼吸章是「全 public 無 diagnostic」的先例，格式可能略有差異）。
3. 確認 `l_levels` 欄位在呼吸章怎麼處理。

### W2　framework.yaml（第二章）　`[blocked: 管道待恢復，見 R6]`

約 6 概念：被動休息 vs 主動恢復的時間尺度反轉、超補償模型及其侷限、雙因子模型、恢復監測工具（HRV / CMJ / 生化 / 主觀量表）、個體與項目差異、恢復的三條生理路徑概覽。

### W3　physiology.yaml（第三章）　`[blocked: 管道待恢復，見 R6]`

約 5 概念：睡眠（證據等級最高）、冷水浸泡的短期效益與長期代價、機械式介入（按摩 / 加壓衣 / 震動）、安慰劑效應與雙盲困境、證據強度總覽表。

### W4　mental.yaml（第四章）　`[blocked: 管道待恢復，見 R6]`

約 8 概念：Kellmann 壓力—恢復平衡（剪刀模型）、COR 資源保存理論、恢復經驗四構念（心理脫離 / 放鬆 / 掌控 / 控制感）、倦怠 Maslach 三因子、過度訓練症候群與倦怠的區辨、急性心理恢復（POMS 軌跡）、介入方法光譜（行為 / 認知 / 心像 / 正念 ACT）、SDT 與教練行為。

### W5　barriers.yaml（第五章）　`[blocked: 管道待恢復，見 R6]`

約 5 概念：休息等於偷懶的隱性偏見、教練知識與工具落差、賽制結構性壓縮、污名化（**須標 🔴，來源稿自承是邏輯推論非定論**）、跨文化比較與台灣體育班制度因素。

### W6　_index.yaml + 來源註冊　`[manual]`

寫 `_index.yaml`（章導言 / 章節順序 / 與 periodization 和 psychology 兩章的 cross-ref）；把 W0 產出的書目寫進 `_sources.yaml`，每個 concept 補 `source_ids`。

### W7　下游同步　`[claude: refactor]`

改 `my-site/tools/sync_vortex.py` 第 25–63 行加入 recovery 章路徑（比照呼吸章「整檔搬運、無剝離」），跑同步，push my-site，**開線上頁面確認實際渲染**（push 成功 ≠ 上線）。

### W8　收尾　`[manual]`

更新 `_INDEX.md` / `HANDOFF.md` / `MAP.md`；跑 `python C:/claudehome/tools/check_map_freshness.py`；刪除 `resources/raw/notes/運動員休息_文獻回顧骨架.md`；commit + push。

**每個 W 完成即 commit + push，不累積**（配額警戒節奏）。

---

## 4. 風險

**R1　體裁衝突（最大工作量，不是搬運是改寫）**
Vortex canonical 要求綜述語言、不做引用拼裝物；來源稿通篇是「一份研究發現…」「系統性回顧指出…」的引用拼裝體。
→ 緩解：schema 本身已提供解法。`public.phenomenon` 分 `text`（學術陳述）與 `plain_text`（白話版），把引用語氣收進 `text`，`plain_text` 寫成綜述語言。派工 spec 必須明寫這條，否則外包回來會是整段貼原文。

**R2　超補償批判與既有 periodization 章衝突　→ 2026-08-12 已查證，風險降級**
原本擔心來源稿第二章批判超補償（「被過度簡化的比喻」、Selye GAS 源自大鼠實驗）會撞上以 Bompa 為主的 `canonical/periodization/`。
實際 grep 結果：超補償在 periodization 章只命中兩處，都是順帶的操作性引用——`structure.yaml:317`「不適合初中級者（達超補償只需 2–3 課）」、`zones.yaml:300`「每 5–6 週在小週期第一週（超補償高峰、疲勞最低）重測」。**該章沒有把超補償當理論支柱陳述**，而且 `structure.yaml` 已有 `critique_of_traditional_zh`（引 Issurin 2010 批評 Bompa/Matveyev 線性模型）、`limitations_zh`、`author_note_zh`，本來就是多派並陳的寫法。
→ 恢復章的超補償批判可直接接上既有 critique 脈絡，不需統一立場。**唯一要注意**：別讓「超補償是簡化比喻」的批判，跟 `zones.yaml:300`「超補償高峰重測乳酸」這條操作建議互相打臉——W2 寫到監測工具時，把後者定位成「操作上的實用近似」而非理論背書。

**R3　l_levels 對應牽強**
恢復概念（睡眠、CWI、倦怠）與 L0–L6 感知階梯沒有自然對應——L0 是呼吸感知建立、L6 是全身場感知，恢復不是感知級別。
→ 建議：concept 層不填 `l_levels`，改在 theme 層用 `band`（初 / 中 / 進）標示適用階段，並在 `_index.yaml` 註明本章為跨 L 級章節。W1 先確認呼吸章怎麼處理，照抄。

**R4　泛運動內容進游泳專案**
來源稿是泛運動（足球密集賽程、力量項目教練、空手道、水球），Vortex 是游泳。
→ 不必自創機制：schema 已有 `hardware_boundary` 欄位，專為跨領域外推註明邊界而設。每個非游泳來源的概念都要填這欄，寫明「證據來自 X 項目，外推到游泳的邊界是 Y」。

**R5　sync_vortex.py 漏改**
路徑寫死，新目錄不加進去就靜默不上站，而且不會報錯。
→ W7 已列為獨立步驟，且驗收要求開線上頁面確認渲染，不接受「push 成功」當完成。

**R6　配額：三條管道同時見底（2026-08-12 實查，這是目前唯一的真正阻塞）**

| 管道 | 7D 用量 | 重置時點 | 備註 |
|---|---|---|---|
| Claude | 98% | 約 2026-08-14 上午 | 5H 窗雖會先重置，但 7D 才是天花板 |
| MiniMax | 93% | 約 2026-08-17 早上 | 且使用者告知它正在跑翻譯，翻完前無空檔 |
| Codex / ChatGPT | 100% | 約 2026-08-18 中午 | 讀數為 24 小時前快照（stale），非即時 |

→ W2–W5 是四個 50–300 行完整新檔，正是發包體裁（單檔 verbatim spec，1 W = 1 file = 1 call），但**現在沒有任何管道可承接**，故全數標 `[blocked]`。
→ **最早可動的是 Claude 8/14 上午那一窗**。屆時的優先序：先 W1（三項確認，讀檔，最便宜）→ W0（書目補完，發 haiku）→ 再看剩餘配額決定 W2 是自寫還是等 MiniMax 8/17。
→ 若 8/14 那窗配額寬裕（>50%），W2–W5 可由 Claude 自寫，不必等 MiniMax——這四檔總量約 800–1200 行 YAML，屬於單窗吃得下的量級。查額度指令：`cd C:/claudehome/tools/deskboard && python -c "import llm_usage; print(llm_usage.read_claude())"`

---

## 5. 預案

- **W0 NOT_FOUND > 25%**：停止整合，回報使用者重新評估來源稿可信度。
- **W1 發現 psychology.yaml 已有恢復/倦怠 theme**：第四章改併入既有 theme，`recovery/` 只保留 framework / physiology / barriers 三檔，_index 加 cross-ref。
- **R2 兩章立場衝突無法調和**：不強行統一，在恢復章標為對立觀點並保留雙方 citation，寫進 HANDOFF 問使用者。
- **發包回來品質不合**：先 `diff` 交付檔與 spec；零 diff = spec 寫錯（修 spec 重發），非零才是模型沒照做。
- **視窗中途撞牆**：已完成的 W 已各自 commit，HANDOFF 記剩餘清單，用 shotclock 排下一窗。

---

## 6. 整體檢視

這章做完，Vortex 會多一個與呼吸章同量級（21 vs 約 24 節點）的獨立章節，且補上一塊既有三個 atlas 都沒吃到的空白：倦怠、Kellmann 剪刀模型、COR、CWI、恢復監測工具應用層。

**要留意的是這篇的體裁風險**——它與 `psychology-schools`（48 篇 AI 綜述）和 `kinetic-chain-textbook` 是同一個 genre，那兩個都已被降級成 legacy。差別在於這篇引用抽查乾淨，而且進 Vortex 後會被拆成有穩定 ID、有 `source_ids`、有確定性標記的原子節點——脫離「單一長篇綜述」這個結構才是它不會重蹈覆轍的關鍵。W0 的書目補完與 W6 的來源註冊是這件事的成敗點，不能省。

---

## 執行起點

下一個視窗從 **W0** 開始。W1 的三項確認結果會決定 W4 是否需要，其餘 W 不受影響。
