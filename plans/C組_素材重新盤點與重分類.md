# (C) 組素材重新盤點與重分類

> **本檔的定位**：更正 `HANDOFF.md` 對剩餘 15 個相位的三分類。
> 該分類是 (B) 組結案時寫的，**判準用錯了**，導致 8 個本來可寫的相位被判為不可寫。
> 本檔記錄錯誤、記錄更正判準、記錄逐相位的證據，並定出後續兩批派工的範圍。

---

## 錯誤 5：相位可寫性用錯了判準 — 錯

**我先前寫的**（`HANDOFF.md` 剩餘 15 相位三分類）：

> (C) 12 個相位「缺裁決或缺素材，不得憑空補」。

**錯在哪**：我是拿兩樣東西當判準的——

1. `canonical/_taxonomy.yaml#movement_phase_registry` 裡該相位**有沒有 `definition` 欄位**；
2. `plans/關節主張裁決_*.md` 系列**有沒有針對該相位的裁決條目**。

這兩樣都不是可寫性的判準。

**反證就在庫內**：`movement.demand.free.front-quadrant-propulsion.wrist-isometric-stability`
已經是一筆 published 記錄。而 `front-quadrant-propulsion` 在登錄表裡**沒有 `definition`**，
裁決清單裡**也沒有針對它的條目**。它之所以寫得出來，是因為
`canonical/instructional/technical-analysis.yaml` 的 `free.tech.8` **原生就描述了
race-club 六相的每一個相位邊界**——素材是這個分期模型自己的素材，不需要跨模型換算。

**正確判準**：

> 一個相位可不可寫，由 `technical-analysis.yaml` 裡**原生屬於該分期模型**的素材
> 有沒有可對到關節詞彙的內容決定。
> **登錄表有沒有 `definition`、裁決清單有沒有條目，都與可寫性無關。**

`definition` 欄位的實際用途是**在有跨模型混淆風險時釘死邊界**
（全登錄表只有 `free.early-pull-through` 帶 `note`，內容正是「不得與 pull、
front-quadrant-propulsion 互相換算」）。沒有 `note` 代表沒有混淆風險，不代表沒有定義。

**這個錯誤的可推廣教訓**：判斷「素材夠不夠」時，要去讀素材本身，
不要讀素材的**中繼資料**（欄位齊不齊、有沒有被裁決過、有沒有 source）。
中繼資料回答的是「這筆素材被整理到什麼程度」，不是「這筆素材說了什麼」。

---

## 更正後的判準與證據

對 15 個未覆蓋相位逐一做**關節詞彙命中掃描**：把 31 個 action 與 22 個 muscle-group
的中文對應詞（屈曲／伸展／外展／內收／旋轉／外旋／內旋／蹠屈／背屈／旋前／旋後／
上舉／水平外展／水平內收／肩胛…）在該相位的素材記錄全文裡計數。

命中數不是分數，是**「這個相位的素材裡有沒有可命名的關節動作」的存在性檢查**。
命中 0 表示素材主體是時序、流體力學或決策，`joint-local` 框架接不住。

| 相位 | 素材記錄 | 命中 | 更正後分類 |
|---|---|---|---|
| `free.lift` 升力相 | `free.tech.8`、`free.tech.4`、`free.tech.5` | 多 | **可寫（W13 D1）** |
| `free.rear-quadrant-propulsion` 後象限推進 | `free.tech.8`、`free.tech.4` | 多 | **可寫（W13 D2）** |
| `free.push` 推水相 | `free.tech.16` | 多 | **可寫（W13 D3）** |
| `free.release` 釋放相 | `free.tech.8`、`free.tech.37` | 多 | **可寫（W13 D4）** |
| `free.early-recovery` 早期回臂 | `free.tech.8`、`free.tech.32` | 多 | **可寫（W13 D5）** |
| `free.late-recovery` 晚期回臂 | `free.tech.8`、`free.tech.29`、`free.tech.32` | 多 | **可寫（W13 D6）** |
| `udk.terminal-down-kick` 下踢末段 | `udk.tech.6`、`udk.tech.9` | 多 | **可寫（W14 D1）** |
| `fly.breathing-window` 呼吸視窗 | `fly.tech.16`、`fly.tech.17`、`fly.tech.18` | 多 | **可寫（W14 D2）** |
| `udk.kick-initiation` 起踢 | `udk.tech.17`、`udk.tech.29` | **0** | (D) 缺關節層素材 |
| `udk.down-to-up-transition` 下踢→上踢過渡 | `udk.tech.7` | **0** | (D) 缺關節層素材 |
| `starts-turns.breaststroke-pullout` 蛙式 Pullout | — | **0** | (D) 缺關節層素材 |
| `breast.leg-outsweep` 腿外划 | `breast.tech.3`、`breast.tech.24` | 少 | **(F) 內容已被既有記錄擁有** |
| `starts-turns.underwater-dolphin-kick` 海豚踢 | 與 `udk` 泳式全段重複 | — | **(F) 結構重複，待除名決策** |
| `starts-turns.flip` 翻滾 | — | — | (E) 框架不適用 |
| `starts-turns.wall-rotation` 牆上旋轉 | — | — | (E) 框架不適用 |

**寫完 W13＋W14 之後，覆蓋率由 44／59 推進到 52／59。**

---

## 各類的處置

### (D) 缺關節層素材 — 3 個，不派工，不憑空補

- **`udk.kick-initiation` 起踢**：`udk.tech.17` 的內容是「滑到個人滑行／海豚踢
  交叉速度就開始踢」，`udk.tech.29` 是出發與轉身的起踢時機差異。
  兩筆都是**時機決策**，決策的自變項是速度，不是關節。
- **`udk.down-to-up-transition` 下踢→上踢過渡**：`udk.tech.7` 的內容是渦流回收
  （Vortex Recapture），是**流體力學機制**。過渡本身在關節層只是兩個相位的邊界，
  邊界不是動作。
- **`starts-turns.breaststroke-pullout` 蛙式 Pullout**：庫內沒有描述 pullout
  關節構型的素材。（此筆先前已判為 (D)，本次重掃結論不變。）

三者的共通處理：**在 `HANDOFF.md` 記錄「缺什麼素材才能寫」，不記「不可寫」。**
缺口是 (D) 的內容，不是它的標籤。

### (E) 框架不適用 — 2 個

- **`starts-turns.flip` 翻滾**、**`starts-turns.wall-rotation` 牆上旋轉**：
  兩者的技術主體是**身體作為剛體在空間中的重定向**（繞橫軸翻、繞長軸轉）。
  `joint-local` 記錄的是體節相對體節的角度變化；剛體重定向不改變任何體節間角度，
  在這個框架下沒有對應。
  這不是素材缺口——**再多的量測也不會讓剛體旋轉變成一個關節動作**。
  要覆蓋它們需要的是新增一個參考系或新的需求類型，屬結構決策，不在本輪。

### (F) 兩個新判出的類別 — 需要決策而不是派工

**`breast.leg-outsweep` 腿外划**：素材（`breast.tech.3` 外划定位不推進、
`breast.tech.24` 外划過寬）裡**可對到關節的部分已經被
`movement.demand.breast.foot-flip.multi-joint-composition-of-toe-out` 擁有**
（翻腳的四關節合成）。剩下的是流體力學（外划不推進、過寬的效率損失）。
硬寫一筆 `leg-outsweep` 只會與 `foot-flip` 重複。

> **決策**：不派工。在 `HANDOFF.md` 標為「內容已由 `breast.foot-flip` 承載，
> 本相位在動作圖譜層不另立記錄」，**不改分母**——登錄表保留這個相位，
> 因為它在教學分期上確實存在，只是這一層沒有獨立內容。

**`starts-turns.underwater-dolphin-kick` 海豚踢**：這個相位與 `udk` 這個泳式的
七個相位（`streamlined-glide` / `kick-initiation` / `down-kick` /
`terminal-down-kick` / `down-to-up-transition` / `up-kick` / `breakout`）
**完全重複**——`udk` 泳式的存在本身就是把它展開成七段。

> **決策**：不派工，**也不除名**。除名會動到分母（59→58），
> 而分母已經印在 my-site 的公開頁面上，改分母要連帶改公開文案，
> 這是結構決策不該夾在覆蓋填充裡做。
> 在 `HANDOFF.md` 標為「與 `udk` 泳式七相位重複，覆蓋由 `udk.*` 承擔；
> 是否除名另案決定」。

---

## W13／W14 的切分理由

- **W13＝六個自由式相位**。它們共用同一組素材（`free.tech.8` 的六階段模型），
  共用同一個跨模型陷阱（race-club 六相 vs kudo 動力相位，BK-26），
  也共用同一組來源錨（`free.tech.8/4/5/29/32` 全部沒有 `source_ids`）。
  拆開派會讓同一個陷阱要在兩份規格裡各寫一次，且相位之間的擁有權分工
  必須在同一份規格裡才釘得住。
- **W14＝`udk.terminal-down-kick` ＋ `fly.breathing-window`**。兩筆素材無關，
  但都是單筆、都與既有記錄有明確的擁有權邊界要防，合成一批派一次即可。

**串行派發**：W13 驗收 commit 後才派 W14。
