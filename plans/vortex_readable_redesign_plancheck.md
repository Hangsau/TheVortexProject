# Vortex 可讀化重做 — 規劃（plan-check）

> 規劃者：Opus 4.8（Fable 5 已於 2026-06-13 停用、訂閱呼叫不到，其 fallback 即 Opus 4.8）
> 日期：2026-06-17
> 範圍：先做 psychology 層為樣板，跑通後套到其他層（泳式 / 感知 / 週期化）
> 實作派工：閱讀外殼 → minimax（`claude-m3 -p`）；敘事黏合層 → Opus 撰寫過三關校正

---

## 0. 要解的真問題（先對齊）

使用者原話：「你整個閱讀方式 就很難有個延續　第一個找到　或是　要延續怎麼讀　都沒有辦法　就沒有辦法整理成好讀　好理解　適合全齡　大眾　可以閱讀的東西嗎」

現況診斷：整個 Vortex 站是 **reference（索引 + 跳轉面板）**——左欄目次、右邊點哪看哪。三個病：

1. 進站不知道**第一個該讀什麼**（首頁是一排並列入口，不是一條起跑線）
2. 讀完一段不知道**往哪續**（面板之間沒有「下一段」的線）
3. 內容**查得到但讀不下去**（psychology 文字是參考書登錄體，學術、無白話主線）

目標：沿 **L0→L6 脊椎的連續敘事**——全齡、大眾、明確起點、有「下一段」把人往前拉，學術深度當安靜支撐（就地可展開，不另開頁、不藏到看不到）。

### 0.1 關鍵發現：這是「兩個問題」不是一個

| 問題 | 層 | 誰做 |
|------|----|------|
| 沒有一條讀下去的線（結構） | layout / CSS / JS | **minimax** |
| 內容是登錄體、缺白話主線與章節橋接（內容） | canonical YAML | **Opus 撰寫，過三關校正** |

→ 單派 minimax 重做殼，只是把讀不下去的學術文字換殼裝。**內容黏合層不補，怎麼排都讀不下去。**
→ 對照：週期化層有 `plain_zh`，psychology 層**完全沒有**白話層——這是內容缺口，不是排版缺口。

---

## 1. 設計：一站兩模式（READ 為主，LOOK-UP 退為旁路）

不丟掉現有的 rail+panel explorer——把它**降級成「跳著查」模式**，另起一個**「一條讀下來」READ 模式**當預設主入口。

```
心理層著陸頁
├─ 【主】一條讀下來　READ  ← 預設、最大、最上面
│    序章 → L0 → L0–L2 → 貫穿 → L3+ → L6，連續滾動 + prev/next
└─ 【旁】跳著查　LOOK-UP   ← 現有 rail+panels，收成一個次要入口
     已經知道要找哪個主題/概念時用
```

兩模式**共用同一份 canonical 資料**，只是兩個 layout 渲染。READ 模式新增、LOOK-UP 模式 = 現有 `vortex-psychology.html` 原封不動保留（改個入口定位）。

---

## 2. READ 模式結構（psychology 樣板）

一頁長文，沿脊椎走一趟。**章 = 主題**，依 L0→L6 順序排：

```
序章　為什麼心理是水感的地基（L0 的閘門）
  ↓ 接下來：先過第一道閘——恐懼
第1章　恐懼 · 還沒碰到動作之前，門先被關上　[L0]
  ↓ 接下來：怕的關卡過了，但身體和心理還在水裡互相點火
第2章　身心交互 · 一緊張就僵　[L0–L2]
  ↓ 接下來：能下水了，但練不練得下去是另一回事
第3章　動機 · 能一直練下去的力氣從哪來　[貫穿 L0–L6]
  ↓ 接下來：在岸上也能練的，是腦中的演練
第4章　意象 · 用想像補練動作　[貫穿 L0–L6]
  ↓ 接下來：感知建立後，高層的心理才上場——先是注意力
第5章　注意力 · 該把注意力放哪　[L3–L6]
  ↓ 接下來：注意力之外，腦中那個一直說話的聲音
第6章　自我對話 · 腦中的聲音　[L3–L6]
  ↓ 接下來：壓力一上來，前面建立的全部會被測試
第7章　喚醒與崩潰 · 為什麼一比賽就崩　[L3–L6]
  ↓ 接下來：守得住的最高狀態
第8章　心流 · 把好表現守在壓力下　[L6]
  尾聲　回到水感：心理→感知→技術這條線
```

### 2.1 每章的三層結構（解決「白話 vs 學術深度」）

```
┌─ 章首白話導引（lead_zh，2–4 句，全齡口吻）          ← 主敘事，誰都讀得懂
│   「怕水的人，多半不是怕水這個東西，是怕一下水
│    就管不住自己的身體。這種怕會在你還沒學動作之前，
│    就先把你學東西的能力關掉。」
│
├─ 概念群（既有 concepts，編織成段而非條列）           ← 讀得下去的散文
│   每個 concept 的 phenomenon 用白話改寫當正文，
│   原學術原文 + 確定性標記 + 來源 收進就地 <details>
│   「想深一點」——不藏到別頁，點開就在原地。
│
└─ 章尾橋接（bridge_zh，1–2 句）                       ← 連續性引擎
    「恐懼的門過了，可是真到水裡，身體一緊張還是會
     僵——心理和身體會互相點火。下一章講這個。」
    [接著讀：身心交互 →]
```

### 2.2 連續性引擎（三件套）

1. **常駐進度脊椎**：左側一條 L0→L6 垂直標尺，滾到哪一章哪一節高亮——隨時知道「我在這趟旅程的哪裡」。取代現有 rail 的「目次」職能，但語意從「目錄」變「旅程位置」。
2. **章尾 prev/next + 為什麼**：每章結尾一句 `bridge_zh` 解釋**為什麼下一章接這個**（沿脊椎的因果），不是乾巴巴的「下一頁」。
3. **頂部閱讀進度條**：細條，顯示整頁讀到百分之幾——大眾讀長文的標準回饋。

---

## 3. 內容缺口：要新增的 canonical 欄位（Opus 寫）

psychology.yaml 現缺三類「敘事黏合」欄位。全部加在 canonical，走 sync passthrough，**不在 my-site 手改 data/**。

| 欄位 | 層級 | 內容 | 字數 | 範例 |
|------|------|------|------|------|
| `lead_zh` | theme | 章首白話導引 | 2–4 句 | 見 §2.1 |
| `bridge_zh` | theme | 章尾橋接到下一章 + 為什麼 | 1–2 句 | 見 §2.1 |
| `plain_text` | concept.public.phenomenon | 白話改寫版正文（與原 `text` 並存，原 text 退為 details 內「研究原文」） | 原文的 1/2 長度、口語 | 把 FWAQ 那段改成「有人專門量過怕水的人到底在怕什麼…」 |
| `intro_zh` | domain 頂層 | 序章全文 | 1 段 | 「技術建立在感知上，感知又建立在心理上…」 |
| `outro_zh` | domain 頂層 | 尾聲全文 | 1 段 | 回扣水感主線 |

**三關校正（每條 plain_text / lead_zh 都要過，memory feedback_vortex_content_three_check_verification）：**
1. 符合研究：白話改寫不得扭曲原 phenomenon 的事實與確定性等級
2. 反問：這句話會不會讓讀者以為「該有某種標準感覺」？（prescriptive 感知＝退回，memory feedback_vortex_perception_cannot_be_prescribed）
3. 反推：有沒有反例會打破這句話的普適性？（如把恐懼說成「人人都怕失控」要排除真有環境創傷者）

**公開層邊界不變**：plain_text 一樣**不放診斷判讀語**（「泳者說 X = 到位」屬 diagnostic 層）。改寫只動 public.phenomenon，不碰 diagnostic 區塊。

---

## 4. 派工切分

### W1 — canonical 敘事層撰寫【Opus，不派】
- 8 主題 × (`lead_zh` + `bridge_zh`)
- 序章 `intro_zh` + 尾聲 `outro_zh`
- 各 concept.public.phenomenon 加 `plain_text`（psychology 共 62 概念，先做 status:complete 的）
- 每條過三關，沒過的列「沒過清單」交使用者
- 理由：寫作 + 非 prescriptive 判斷 + 幻覺歸因風險，minimax 會踩雷

### W2 — sync_vortex.py passthrough 擴充【minimax 或手動微 diff】
- `sync_vortex.py` theme dict 加 `lead_zh` / `bridge_zh` passthrough
- concept rec 的 phenomenon 加 `plain_text` passthrough
- domain 頂層 `intro_zh` / `outro_zh` 帶進 data
- 規格：≤10 行 diff，**手動寫**（微 diff 不派，CLAUDE.md 規則）

### W3 — READ 模式 layout【minimax，verbatim 全檔規格】
- 新檔 `layouts/vortex/vortex-psychology-read.html`（~200 行）
- content stub `content/vortex/psychology-read/_index.md`
- 序章 → 8 章（lead_zh / concepts 散文 / details 學術原文 / bridge_zh）→ 尾聲
- 1 call = 1 file；規格含每個 Hugo range/with、class 名、欄位路徑 inline

### W4 — 連續性引擎 CSS + JS【minimax，verbatim 規格】
- `vortex.css` 加 `.vx-read-*`（進度脊椎 / 章節 / 橋接卡 / 頂部進度條）
- `vortex.js` 加滾動監聽（IntersectionObserver 高亮當前章 + 進度條）
- 規格含完整 CSS 區塊 + JS 函式 verbatim

### W5 — 著陸頁雙模式入口【手動或 minimax 微 diff】
- 現 `vortex-psychology.html` 改成 LOOK-UP 入口，頂部加「想一條讀下來？→ READ」
- `vortex-home.html` 心理層入口指向 READ 模式
- READ 頁頂加「想跳著查？→ LOOK-UP」

### W6 — 驗收 + 套用其他層【Opus + minimax】
- psychology READ 跑通、使用者拍板後
- 同樣板套：泳式（已有 plain 素材較多）、感知層、週期化（已有 plain_zh，最好套）

---

## 5. 派工順序與依賴

```
W1 (Opus 寫內容) ──┐
                   ├──→ W2 (sync) ──→ W3+W4 (minimax 殼) ──→ W5 (入口) ──→ 驗收 ──→ W6 (推廣)
canonical 有內容後 ─┘
```

W1 必須先行——**沒有 lead_zh/plain_text/bridge_zh，W3 的殼是空的**。
W3 + W4 可並行派 minimax（兩個獨立 file）。

---

## 6. 為什麼這樣切（給使用者的決策依據）

- **不是重寫整站**：LOOK-UP 模式（現有 rail+panel）完整保留，只新增 READ 模式 + 降級入口。風險低、可回退。
- **psychology 先做樣板**：它是最讀不下去的層（純學術、無 plain 層），打通它＝最難的先過；週期化已有 plain_zh，反而最後套最省力。
- **minimax 只碰殼不碰內容**：殼是機械式 verbatim（它強項、額度高、不吃 Claude 配額）；內容黏合需要寫作判斷與三關校正（Opus）。切錯會得到「換殼的學術文」。
- **canonical-first 不破壞**：所有內容進 canonical → sync → my-site，雙消費（swim-coach 也讀）不受影響。

---

## 7. 待使用者拍板

1. 這個「READ 為主 / LOOK-UP 為旁」的雙模式方向，對不對？
2. W1 的敘事內容由 **Opus（我）寫好給你三關審**，可以嗎？（vs 你自己寫白話、我只做殼）
3. psychology 先做樣板、跑通再推其他層，這個順序 OK？
