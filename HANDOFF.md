# The Vortex Project — 工作交接單

> 每次有實質推進後更新「當前狀態」與「下一步建議」。規則與背景見 `CLAUDE.md`。

---

## 當前狀態（2026-06-20）

### 文件校正——FUTURE_RESEARCH.md 過期狀態判斷修正（2026-06-20）

> 觸發：在 my-site Vortex「內容還缺什麼」的缺口盤點中，誤把 `FUTURE_RESEARCH.md`（2026-04-18）的舊狀態句當現況，得出「L4–L6 感知描述薄弱／四式不對稱」的錯誤結論。實際核對 `Technica/water-sense-levels.yaml` 後發現四式 L3→L6 早已補完（訓練重點 + 里程碑 + 三型 quick-card）。
> 已修 `FUTURE_RESEARCH.md` 三處過期判斷並加 2026-06-20 狀態註：①§3.1「L4 以上描述薄弱」→ 已補完，缺口收斂為與 L0–L6 正交的「感知深度」軸；②§4.2 三條 bullet 逐條標修正（L4–L6 已補完／渦流感知非「完全缺席」已有 Tornado Drill·蛙式蹬腿渦流整合·Tanaka 指標但未系統化／時序感知已擴展到蝶式 C 型與自由式里程碑）；③§五優先表理由句對齊。其餘 md 無同類過期句（grep 確認）。
> ⚠️ 教訓：規劃文件的狀態句有時效，引用前要對現行內容檔（yaml）核對，不可拿兩個月前的判斷當現況。

---

## 當前狀態（2026-06-19）

### 內容校正——A-1 自由式髖部驅動因果方向（2026-06-19）

> 觸發：my-site Vortex 內容邏輯稽核（minimax 初版 + Claude 抽查）發現 `technical-analysis.yaml` 同檔自打嘴巴。`free.tech.4` 原寫「髖旋轉先行帶動肩膀（髖帶肩）」，與同檔 `free.tech.15` ／ Pink et al.(1991) EMG「肩胛肌群是旋轉的主動發動者、髖部被動跟隨」離群衝突。
> 已改寫 `free.tech.4` mechanism：移除因果敘述，改述大幅髖旋轉(45–60°)為外顯特徵、肌肉啟動仍由肩胛肌群主導（對齊 free.tech.15）。已 resync 到 my-site。稽核全表見 my-site `research/vortex-content-logic-audit.md` §0。

---

## 當前狀態（2026-06-16）

### 已完成——Phase 2：心理層完整接入 Vortex 網站（八主題「心理地圖」全部上線，62 概念）（2026-06-16）

> 觸發：研究層完整化（B1–B4）達成後，用戶指示「繼續」，進入 Phase 2 網站接入。**用戶關鍵糾正 1：直達網址＝孤兒頁，不算接入 Vortex；必須有導覽入口。** **用戶關鍵糾正 2（「為什麼一直停下來，不直接做完」）：不要交付 pilot+stub 就停，一次把全部主題寫完。** Phase F 凍結的是「首頁重設計」，加入口卡＋本頁不在凍結範圍。
> 設計回應用戶「心理層有沒有分級」：分級＝水感 L0→L6／初學→競技這條脊椎本身。著陸頁＝「心理地圖」，8 主題沿脊椎排三帶（初學端 L0–L2／貫穿全程 L0–L6／進階競技端 L3–L6）。

**心理地圖（八主題三帶，全 complete）**：
- canonical `psychology.yaml`：8 主題、**62 概念**，每概念 public/diagnostic 兩層。fear theme（7，手寫 pilot）+ 其餘 7 主題由 7 個並行 Sonnet agent 各讀對應 dossier 寫出，每條過三關校正：
  - 初學端：①水中恐懼(7) ②心理-感知-生理交互(8)
  - 貫穿全程：③動機與動機氣候(9) ④意象與心理演練(6)
  - 進階競技端：⑤注意力焦點(6) ⑥自我對話與心理技能(8) ⑦喚醒焦慮與壓力崩潰(8) ⑧心流與去再投資(10)
  - theme 加定位欄位 band/l_band/level_tag/concept_count；merge 用 ruamel round-trip（保留 fear 手寫格式與檔頭註解）。
- **三關校正沒過清單（各 agent 自報，剔除不收）**：interaction 剔 Noakes CGT 獨立概念（反推：競技配速≠初學）、Pain/Effort 分離（🔴空白+🟠二手數字）；motivation 剔量表 α/factor%、need-thwarting 重複、Sarrazin 手球外推；imagery 剔意象量表信度、多巴胺 BCAA 機制（反推荒謬）、最佳劑量（證據初步）；self_talk 剔 beat-average 70%（🟠灰文獻）、感知導向自我對話（🔴空白）、PST 多模態打包（品質 critically low）；attention/arousal/flow 無剔除（全過）。
- `sync_vortex.py` pass-through theme 層 band 欄位；`vortex-psychology.html` 概覽＝三帶地圖（complete→is-ready 卡可點入、planned→is-planned＋建置中；現全 complete）；`vortex.css` 加 `.vx-band*`/`.vx-theme-*`；首頁入口卡（vortex-home.html）。
- 已驗：hugo build exit 0，8 ready 卡 0 planned、**62 concept panel**、9 rail group；sync 後 my-site data **0 diagnostic 洩漏**（reading_signals/abc_link/probe 全剝除）；清掉 2 處 §dossier 段號洩漏（§1.6/§6）；headless Edge 截圖視覺確認三帶全亮。


- **新 canonical domain `canonical/psychology/psychology.yaml`（commit 36d51f5，Vortex repo）**：theme→concept schema（跨泳式、跨族群，對應 perception `free.yaml` L16 預授權的 psychology domain）。pilot 主題「水中恐懼」7 概念，每概念 public/diagnostic 兩層。
  - 7 概念：失控不是怕水（control_loss）、恐懼關掉水感（perception_masking）、凍結是反射（freeze_reflex）、CO₂ 換氣過度恐慌（co2_breath_panic）、潛水反射冷靜（diving_reflex_calm）、安全前置（safety_precondition）、族群恐懼臉孔（population_faces）。
  - **public/diagnostic 分層**：public = 現象機制／生理硬體邊界／L0–L6 映射／誤區校正／可做介入／族群差異；diagnostic（泳者說 X→判斷、A/B/C 診斷、感知探針）**不公開**，sync 時剝離。
- **my-site 接入（commit 3df8b56，CI success，hugo-source）**：
  - `tools/sync_vortex.py` 加 `sync_psychology()`：iterate themes→concepts，只輸出 public 欄位（drop diagnostic），寫 `data/vortex/psychology.yaml`。已驗 0 diagnostic 洩漏。
  - `layouts/vortex/vortex-psychology.html` master-detail 頁（重用 vortex.css/vortex.js，左 rail 按 theme→concept、右 panel 渲染現象/邊界/誤區/介入/族群/來源/flow nav）。
  - `content/vortex/psychology/_index.md`（layout: vortex-psychology）。
  - **首頁入口卡**（`vortex-home.html`「更底層·感知的地基」section，現有 `.vx-toc-row` 樣式，主題數動態讀 data）——孤兒頁→真正接入導覽。
- **三關校正沒過清單（剔除 4 條，不收）**：US poll 百分比🟠（二手委託民調）、FWAQ 98.2%/α=0.831（反問不過：量表內部信度非教學可用結論）、Wolpe 90%🟡（舊文獻過度精確）、US 4.3%/40%🔴（待查）。三處 🔵 反推防護：perception_masking 標🔵附研究空白註、diving_reflex 附安全前置、呼吸介入限低強度（淺水昏迷風險）。

### 已完成——心理層 8 dossier 系統性引用查證 B1–B4：4 處誤歸因/誇大結果攔截 + 全數文獻 🔴 收斂（2026-06-16）

> 觸發：用戶指示「先做完整研究、把心理部分整理好，再看怎麼接入 vortex 網站」。先做研究層完整化（網站接入留待 Phase 2）。分 4 批逐檔查證每一條 🔴 待查引用，每個人名/DOI/PMID 都實際追到 Crossref / NCBI eutils 一手核對，不靠搜尋摘要。**過程攔到 4 處高風險幻覺/誤記，全部更正。**

- **B1（02+04，commit 9df3267）**：02 收斂 5 條（Scott & Gijsbers 1981 PMID 6789949、Hardy/Parfitt/Pates、Hanin 年鑑章節、Masters/Eves/Maxwell 2005 會議論文、O'Leary & Morris 2017 修作者序）；04 把 Teixeira et al. 2020 從 🔴 ResearchGate 升 🟢（PMID 31578934 / DOI 10.1080/17461391.2019.1675768），關閉 🔴02。
- **B2（03+05，commit fdde682）**：03 §2 盛行率溯源——WMH 22 國 2.3% 升 🟢（Wardenaar 2017, PMID 28222820 / 勘誤 28994357），美國 46/64/32–39% 追到 1998 Gallup × Miracle Swimming 委託民調維持 🟠；05 Hall et al. 1998 補 IJSP 29(1):73–89、Simonsmeier 2021 補 DOI 升 🟢，兩個「🔴PMID 待查」關閉。**關鍵辨識：IJSP / IRSEP 等刊物未被 PubMed 收錄，「無 PMID」是制度性而非「待查」——此前誤標待查。**
- **B3（06+07+08，commit cb7f038）— 攔到 3 處誤歸因**：
  - **06 ①** 「more/less successful 隊伍賽前準備」更正歸 **Gould, Guinan, Greenleaf, Medbery & Peterson 1999**（TSP 13(4):371–394, DOI:10.1123/tsp.13.4.371），v1 誤植為 Gould & Dieffenbach 2002（該 2002 篇實為奧運冠軍心理特質，不同主題）。
  - **06 ②** 游泳 PPR 研究作者更正 **Moraes → Richard, Mason, Alvarez-Alvarado, Perry, Lussier & Tenenbaum 2021**（TSP 35(2):97–107, DOI:10.1123/tsp.2020-0023）。**且 v1 誇大結果**——原寫「對表現/動作效能/自我效能/情緒均有正向效果」，實際速度/動作效能/自我效能皆「不顯著」，僅情緒顯著；正確結論是「PPR 對客觀指標效果有限、主要作用在情緒與主觀層面」。Zach 2024 補 DOI:10.32725/sk.2024.004。
  - **07 ③** Masters & Maxwell 2008 更正為 IRSEP 期刊論文「The theory of reinvestment」1(2):160–183, DOI:10.1080/17509840802287218，v1 誤植為「Hirsch 編書章」。Jackson 1995 補 DOI:10.1080/10413209508406962，並更正「PMID 8735997」誤植（該 PMID 屬 Jackson 1996 *RQES* 篇，非 1995 JASP 篇）。
  - **08**：補完 P07–P10 文獻層 🔴——Tucker 2004 40°C（PMID 15138825）、Tucker 2009（PMID 19224911）、Easterbrook 1959（**更正「1959 年無 PMID」誤記，實為 OLDMEDLINE PMID 13658305**）、Miu et al. 2009 HRV（PMID 19059813，補足三位作者）。
- **B4 收尾（本次）**：00 總覽的 Liao & Masters 桌球更正先前已傳播（§54/135/167），G2 已含「感知導向自我對話」第三類——無需再改。各 dossier footer 計數自核對齊（05 🔴6 = 5 編號空白 + 1 量表空白；08 文獻 🔴 歸零，剩 🔴-01~09 九項研究空白 + §4.3 未讀檔一處）。
- **總結**：心理層 8 dossier 的「待查引用」🔴 已全數收斂——剩餘 🔴 皆為**真研究空白**（已逐條標界「目前文獻無此數據」），可作未來實驗設計起點，非未完成查證債。**研究層完整化達成；下一步才是 Phase 2 網站接入評估。**

### 已完成——`隱性_顯性學習.md` 升 v2 + 攔截並更正一處跨檔誤歸因（2026-06-16）

> 承上方批次路線圖剩餘跨檔工程第①項。修 escape-bug + 用 dossier 02/07 素材擴成 v2。**升級過程中強制查證攔到一處重大誤歸因，連帶更正心理層多檔（含本人批次 B 的傳播）。**

- **`Research/感知科學/隱性_顯性學習.md` v1→v2**：原檔整檔一行字面 `\n`（escape-bug）渲染全壞。重寫為 7 節 clean v2：§1 隱性 vs 顯性對照、§2 再投資理論機制核心（Masters 1992 DOI 10.1111/j.2044-8295.1992.tb02446.x；動作 vs 決策再投資 Masters & Maxwell 2008 DOI 10.1080/17509840802287218；Beilock & Carr 2001 PMID 11757876）、§3 類比學習（**正確歸給桌球**）、§4 de-reinvestment=L5→L6、§5 L0–L6 教學映射、§6 研究空白、§7 dossier 連結。
- **⚠️ 攔截的誤歸因（高風險幻覺，自查時抓到）**：Liao & Masters 2001 的著名「analogy learning」研究**是桌球**（正手上旋、「直角三角形」拍路），**不是游泳**。心理層先前把它描述為「游泳第一手實證」，並附**無法核實、疑捏造**的 DOI（10.1080/026404101300149327）、頁碼（369–375）、標題（「…in swimming」）。正確版：DOI 10.1080/02640410152006081，pp 307–319，標題「Analogy learning: A means to implicit motor learning」。游泳應用是**外推**（🔵），非第一手實證。
- **連帶更正的檔**：`00_心理層總覽.md`（3 處，含**本人批次 B 寫的主軸 B 引用**——屬自我傳播的更正）、`07_心流與最佳表現.md`（內文 §250 + 研究空白 §287 + 資料來源 §306）、`_INDEX.md`（§126）、`RESEARCH_PLAN.md`（§123 Masters DOI tb02440→tb02446 修正 + §124 把無法核實的 Liao PMID 11354610 換成已核 DOI）。所有殘留的舊 DOI/頁碼字串都已被包進「⚠️ 更正」說明內，不再作為事實宣稱。
- **游泳專屬類比學習對照研究確認為研究空白**（v2 §6 + 07 §287 已標 🔴），不強行補。

---

### 已完成——新增 Research/心理/ 層：感知優先重讀運動心理學（2026-06-15）

> 目標：補上專案一直缺的「心理」環節。用戶指示「opus 負責規劃給其他做，再做最後整理，資料蒐集多一些」。Opus 規劃 8 個子主題 → 子代理（Claude + 預定 minimax）並行蒐集 dossier → Opus 整合。

**流程與產出：**
- Opus 把心理層拆成 8 個子主題，派 8 個子代理並行蒐集文獻 dossier（每份附 PMID/DOI + 確定性標記 + 游泳第一手 vs 跨運動外推分層 + 與水感框架的連結 + 🔴 研究空白）。
- 子代理在「生成回報訊息」時撞 Claude 限額（回報 token=0），但 **8 份 Write 都已落盤**；查證磁碟確認完整（每份 8–31 個 🔴/研究空白標記），無需重跑。
- Opus 收尾：① 查證並修正 dossier 02 兩個可疑引用（倒 U 曲線 TiCS 2024 DOI 格式錯誤→改用真實標題+PII S1364-6613(24)00078-0；ACTH 研究作者名「Frontaini」是捏造→移除，改用真實標題+PMID 34868421 並補正數據）② 8 份 dossier 從 `_raw/` 升到 `Research/心理/` 正式位置 ③ 寫 `00_心理層總覽.md`（Opus 整合骨架，非第九份 dossier）。

**`00_心理層總覽.md` 的整合價值（單一 dossier 看不到的）：**
- 五條貫穿全部 8 cluster 的主軸：A 感覺水=注意力焦點第三類（2024 Bayesian meta PMID 39480294 推翻 EF 全面優越）/ B Flow↔Reinvestment 軸線與 de-reinvestment（=L5→L6 機制）/ C EMG 悖論心理橋（焦慮過度控制證據最強，但意象 forward model 保留解釋 #2）/ D 動機氣候=感知探索土壤（感知目標語言=精熟氣候工具）/ E 恐懼=「失去動作控制」簽名（接 L0 閘門）
- 心理層 × L0–L6 對照表 + × A/B/C（C 型=全身張力，由 EMG 悖論機制鏈解釋）
- 5 項框架原創貢獻（感知耦合焦點/感知導向自我對話/「水在幫我」可操作指標/感知目標語言=動機工具/de-reinvestment 機制）—— 皆 🔴 文獻空白等級但具生成性
- 6 條跨 cluster 🔴 研究空白

**連帶更新：** `_INDEX.md`（新增 Research/心理/ 區）、`FUTURE_RESEARCH.md` §0.5 EMG 悖論（從「純推測」升級為「兩條有文獻支撐的競爭假說」，引心理層證據）。

**重要連結：** `Research/感知科學/隱性_顯性學習.md` 已存在（v1 stub，2026-04-25，僅 3KB）；dossier 02 + 07 提供大幅擴充素材（再投資動作 vs 決策分離、Liao & Masters 2001 完整方法、Beilock 明確監控假說），可把該 stub 升級為 v2。
> ⚠️ 順帶發現：該 stub 檔內容是**字面 `\n` 而非真正換行**（escape-bug，整檔一行），渲染全壞——需單獨修一次（非本次心理層任務範圍，先記錄）。

---

### 已完成——心理層查證債清理 + 教學對象框架釘入（2026-06-15，第二 session）

> 觸發：用戶檢視心理層問「還有沒有要補的」。先做缺口評估（4 個 haiku 平行讀完 8 dossier），再從最安全的查證債批次動手。

- **教學對象框架釘入 `CLAUDE.md`**：用戶澄清「客群涵蓋全光譜、無單一主客群」（兒童 / 兒童競技 / 青少年競技 / 鐵人三項 / 成人初學；未來加自由潛水成人+兒童）。寫入 CLAUDE.md 專案本質區，明令 AI / 子代理**不得自行推斷主客群**、文獻偏壓某族群只是素材缺口。**起因：缺口評估時一個 haiku 子代理把「成人休閒學習者=主客群」當事實塞進回報，被原樣轉述，用戶糾正——故釘入文件防複發。**
- **08 查證債全清（六條 🔴-P → 全數查證）**：逐條追 PubMed / 期刊原始頁。P01 Tucker, Lambert, Noakes 2006 → PMID 19116437；P02 Noakes 等 2005 → PMID 15665213；P03 → **更正**為 Noakes, Peltonen, Rusko 2001（DOI 10.1242/jeb.204.18.3225，原誤標第一作者 St Clair Gibson）；P04 Paulus & Stein 2010 → PMID 20490545（原誤記來源為 ScienceDirect Topics）；P05 Chambers 等 2009 → PMID 19237430；P06 PMC4152223 = Pappens 等 2014 → PMID 25181542。§七標題改「全數查證完成」。
- **修三處誤歸因**：① §六 🔴-07 漱糖水機制原歸 Tucker 2006 → 改 Chambers 2009 ② P03 第一作者 ③ P04 來源。
- **06 Bauman 兩條 🔴**：Gould, Dieffenbach & Moffett 2002 DOI 查得（10.1080/10413200290103482，運動心理期刊無 PMID），但其主題（奧運冠軍心理特質）與 dossier 描述（區分 more/less successful 隊伍）**不符** → 標為「篇目待原書核對」，不強行對齊以免製造新誤歸因；>X̄ Sydney 2000 訪談確認為**灰色文獻**（Bauman 書中自述，無發表原始資料）。

**心理層缺口路線圖（本 session 評估；批次 A 查證債已完成，B/C/D 待續）：**
- **B 整合缺口**（低風險，🔵 推導 + 可查文獻）：恐懼×動機氣候交互（00 總覽五主軸與 G1–G6 皆漏的整合缺口）、呼吸中斷的認知負荷（swimming-specific，補進 08，解釋水中 RPE 膨脹）、發展軌跡型 flow（07 只談「已達成」flow，缺 L2→L3 / L4→L5 過渡期）
- **C 族群覆蓋**（中風險；因「客群=全部」而從誤判升級為真缺口）：03/04 文獻偏壓兒童泳課+競技隊，缺成人初學 / 鐵人三項 / 青少年競技各自的恐懼·動機特異性，須分族群並列、查無則標 🔴
- **D 補厚單薄段**：07 IPS（僅 3 行就跳「已被取代」）、04 HMIEM（純理論占位無游泳實例）、08 中樞調節（自承二手）、02 Reinvestment 專節壓縮（與前文核心理論重疊約 40%）
- 另：`隱性_顯性學習.md` escape-bug（整檔字面 `\n`）+ 用 dossier 02/07 素材升 v2（見上方心理層主塊）

---

### 已完成——心理層批次 B：三條整合缺口補齊（2026-06-15，第二 session 續）

> 承上方缺口路線圖批次 B。全部建立在已驗證引用之上（🔵 推導明確標界，新數據缺口標 🔴），無憑空斷言。

- **B1 恐懼×動機氣候交互**（跨 cluster 03+04，總覽五主軸與 G1–G6 皆漏的二階整合）：
  - `00_總覽` §1 新增「主軸交互 D × E — 動機氣候調節恐懼的閘門效應」：表現氣候把私下「失去控制」恐懼放大成公開能力判決 → 抬高 L0 閘門；調節變項=知覺勝任感（低勝任+ego 最毒）；低勝任=所有初學族群共同起點，故同一交互在初學族群卡 L0、在競技族群壓縮 L4–L6 再探索（分族群並列，不一概而論）。支持文獻 🟢：Masters 泳者 Frontiers 2025（DOI 10.3389/fpsyg.2025.1574429）、統合分析 DOI 10.3390/ejihpe14040064。
  - `03` 新增「恐懼×動機氣候」小節（接 cluster 04，減敏/暴露須先卸評價威脅才生效）；`04` 新增命題六（互引 00 §1）+ **修正 §命題五原「成人=本框架主要使用對象」**改為「知覺勝任感調節、初學族群最脆弱」（消除與新教學對象框架的矛盾）。
  - 總覽 §5 加 🔴G7（氣候×恐懼交互的泳池實驗數據空白）。
- **B2 換氣的週期性認知負荷**（補進 08）：新增 §1.9「換氣作為週期性認知負荷注入」——換氣是必須與划臂對時的運動任務，未自動化者每次換氣抽走流場感知頻寬→水感節律性閃斷→換氣側水感系統性較差。定位為 C 型的**第二條獨立路徑**（與 §1.2 焦慮肌張力並列，介入方向不同：降喚醒 vs 換氣自動化）。🔵 推導，建立在已引用的雙重任務+Easterbrook 注意力窄化上；量值缺口標 🔴-09。總覽 §3 C 型條目同步改為「兩條獨立機制」。
- **B3 發展軌跡型 flow**（補進 07）：新增「心流的發展軌跡：flow 不是 L6 的專利」——挑戰-技能匹配是相對技能水平的，flow 在每個 L 級皆可發生、內容隨層遷移（L0–L2 控制感初獲 / L3–L4 局部融合 / L5–L6 場共振）。意義：早期 flow=動機燃料（連 04）、教學落點=主動工程化各層挑戰-技能匹配、兒童易進成人初學需更刻意去評價（連 03/04 交互）。🔵 建立在 Csikszentmihalyi 挑戰-技能模型；跨層 FSS-2 實測缺口已在 §6。

**批次 B 全程無新增未驗證 PMID；所有人名/DOI 均沿用已查證來源或標 🔵/🔴。** commit 90f2cbf。

---

### 已完成——心理層批次 C：族群覆蓋分列（2026-06-15，第二 session 續）

> 因「客群=全光譜、無單一主客群」，族群特異性從誤判升級為真缺口。03/04 文獻偏壓兒童泳課+競技隊，補上其餘族群並列。3 條 WebSearch 取得可用來源；查無者標 🔴（素材缺口非受眾界定）。

- **03 新增「族群特異性：恐懼的不同臉孔」**（分族群表）：兒童初學（代際傳遞，🟠 文獻默認）/ 成人初學（疊加社會性羞恥+自我意識+恐慌史，🟢 Educ Sci 2025 DOI 10.3390/educsci15060760）/ 鐵人三項（非怕水本身，怕開放水域情境=有能力泳者賽境 L0 退行，🟠 二手 ~22% Ironman 2004 Grand'Maison，原研究未核）/ 青少年競技（轉表現焦慮，跨指 cluster 02）。教學意涵：四群指向不同介入點，把鐵人/青少年用兒童 L0 水性課介入=族群混淆。加 🔴11/12。
- **04 新增「族群特異性：動機的不同引擎」**（分族群表）：兒童樂趣優先 / 青少年競技流失懸崖（參與 ~11 歲達峰→17 歲谷底女~64%男~45%下降，系統回顧 PMID 29910410 + 連既有 Difernand 2025 存活分析）/ 成人初學目標導向+勝任感脆弱 / 鐵人三項游泳=手段（🔴 動機結構幾無第一手）。加 🔴07/08，footer 條目數更新。
- **族群百分比數字標界**：Ironman 22%、流失 64%/45% 均標 🟠「原始未核」，不當硬數據用。

---

### 已完成——心理層批次 D：逐項覆核，只補真缺口（2026-06-15，第二 session 續）

> 對前 session haiku 評估的 4 個「單薄段」逐一覆核實際內容後判斷——**只有 1 項是真缺口，其餘 3 項評估過時或屬低值重構，不硬補**（避免製造填充內容）。

- **04 HMIEM 游泳實例（真缺口，已補）**：原 §7 純理論占位無游泳實例。新增三層模型（Global/Contextual/Situational）× 游泳情境 × L0–L6 對照表 + **bottom-up 動機修復槓桿**（單次成功 L0 感知體驗反覆累積 → 由下而上修復情境層動機、鬆動「我不是水裡的料」整體層自我認定，連 cluster 07 早期 flow，對成人初學尤關鍵）。🔵 推導，建立在 Vallerand 1997 既有框架，無新增未驗證引用。
- **07 IPS（覆核：非真缺口）**：§7 實含 Loehr + Hanin IZOF + Hardy/Jones/Gould 三源並誠實註明 IPS 已被取代，覆蓋足夠，不硬補。
- **08 中樞調節（覆核：評估過時）**：批次 A 已升級為 Noakes 一手（PMID 9140893 / 15665213 / 10.1242/jeb.204.18.3225 + Tucker 2009），非二手。僅殘 1 個 🔴（Tucker 40°C 閾值原始 PMID），低優先。
- **02 Reinvestment（覆核：不壓縮）**：§5 與「Reinvestment 專節 A–G」確有重疊，但分屬「核心理論條目」vs「深掘附錄」兩種角色；用戶意圖是補缺口非修剪冗長，且壓縮有損 nuance 風險，保留原狀。

**心理層 A/B/C/D 四批次全部收束。剩餘為跨檔大工程（非心理層收尾範圍）：① `隱性_顯性學習.md` escape-bug 修復 + 用 dossier 02/07 素材升 v2；② 各 dossier 殘餘 🔴 的逐條查證（多為研究空白等級，已標界）。**

---

### 已完成——週期化知識研究擴充 + 白話重寫 + 一源兩消費全鏈打通（2026-06-10）

> 目標：外部文獻研究擴充週期化 canonical，加 plain_zh 白話層（學員/家長/教練），並打通 canonical → my-site 呈現 + swim-coach FTS 兩個消費端。承接上方 Phase 1（canonical 建檔）。

- [x] **R1 外部文獻研究**（4 並行 Sonnet sub-agent，嚴守反幻覺）：可用 primary 來源——減量 Mujika 系列（PMID 12840640 / 8775162 / 12439774）+ Bosquet 2007（PMID 17762369）；能量系統 Toussaint & Hollander 1994 / Rodríguez & Mader 2011（跨研究區間不合併，如 400m 有氧 40–84%）；分區 Maglischo 2012《Training Zones Revisited》(J Swimming Research 19:2)；TID Papadimitriou 2025（DOI 10.1007/s00421-025-06064-x）；年度 Hellard 2019（PMC6470949）/ González-Ravé 2022（PMID 36247944, n=1）；LTAD Swimming Canada（windows of trainability **contested**——Ford 2011 PMID 21259156 + van Hooren 2020 批判）。
- [x] **canonical 三檔擴充 + plain_zh**：structure（+swim_annual_structure +swim_youth_ltad）、taper（修掉幻覺「1.62%」→ +2.18% PMID 12439774、補 +2.90/+3.20% PMID 8775162）、zones（+Maglischo 六分區 +三區乳酸 +各距離供能 +TID）。每節點加 plain_zh（白話），source/數字/cert 並排保留。
- [x] **_index.yaml 概念目錄**：28 節點（gist_zh 一句白話 + stages），index↔real id 零死連結。commit 7d03619（已 push remote）。
- [x] **my-site 呈現**：`sync_vortex.py` PERIODIZATION_FILES 加 `_index`；verbatim 搬 4 檔到 `data/periodization/`；`vortex-periodization.html` §1–§6 渲染 plain_zh + §5 加 4 游泳區塊 + 新增 §7 游泳年度結構 §8 青少年 LTAD（contested 警示）。hugo build 綠。my-site commit 31cea81（待 push 觸發 CI）。
- [x] **swim-coach FTS 被動繼承**：vendor/vortex submodule bump ce3a183→7d03619；`build_knowledge_index.py` 加 `_`-prefix skip（_index.yaml 非 FTS 內容）；FTS index 31 列（structure12/taper10/zones9），0 null source_id / 0 _index 列 / 0 重複；新增 swimming 區塊全 FTS 命中；加 2 behavioral test；pytest 73/73。swim-coach commit 6375496（未 push，Phase 3 政策）。

### 已完成——canonical/periodization/ 新 domain：Bompa 週期化收編為唯一真相源（Phase 1）

> 目標：把 Bompa《Periodization》(6th ed.) 週期化知識收進 canonical，成為唯一真相源，供兩個下游消費——my-site vortex 給 ADM 年度計畫補「週期化理論骨幹」、swim-coach 自動學課表能力的知識基礎。架構複製剛完成的 ADM 模式（一源兩消費）。**Phase 1（建 canonical）為本次範圍；Phase 2 vortex 呈現 / Phase 3 swim-coach 唯讀引用 / Phase 4 swim-coach rules schema 提案，後續進行。**

- [x] **Phase 0 來源核對**：5 章正文全讀自正確 body 檔（`XX_Summary_of_Major_Concepts.md`，非僅含參考文獻的 `Chapter_X.md`）。檔對照：11_=Ch5 / 13_=Ch7 / 14_=Ch8 / 15_=Ch9 / 18_=Ch11。每個數字溯源至章節/表格 + 標確定性。修正 Haiku 草稿兩處：taper 改為 41–60%（重負荷 60–90%）/ 8–14 天；macrocycle 3:1 確認正確（Bompa "probably the most common"）。
- [x] **structure.yaml**：年度計畫結構。3 階段（準備/競賽/過渡 + subphases）；4 計畫類型（mono/bi/tri/multipeak，Table 5.1 週數分配，dotted ID `periodization.structure.annual.*`）；macrocycle（2–6 週，3:1 預設負荷型態）；microcycle（4 分類）；detraining 安全表（🟢 Table 8.2 / Mujika & Padilla 2000，swim-coach 休賽/傷停課表關鍵安全參數）。
- [x] **taper.yaml**：賽前減量與達峰（Ch9 / Mujika & Padilla 2003 🟢 / Bosquet 2007）。四變數（量 41–60%主旋鈕 / 強度維持 / 頻率≥80% / 時長 8–14 天）；曲線型態（快速指數 ≈4–5% 為首選 vs 階梯 ≈1.2–1.5%）；達峰窗 7–14 天；游泳應用（文獻 50–90% 量遞減、三週減量 +2.2%、雪梨2000 名次差 1.62%）。
- [x] **zones.yaml**：能量系統強度分區。Table 7.1 六分區（賽配速=zone 2）；Table 11.2 HR/VO2/能量系統對照；Table 11.1 LIEE 六法；耐力週期化三階段；游泳配速分區（🔵 只映射 Bompa 框架不發明百分比）。
- [x] **三項驗證（Python，跑完即棄）**：① 三檔 YAML parse OK；② 跨 domain link 完整——所有 `links.development_stages` 引用（l2t/t2t/t2c/t2w）皆命中 development/matrix.yaml stages[].key，BAD=NONE；③ 22 個 ID 全唯一、全 `periodization.` 前綴，DUPLICATES=NONE。
- **整合點**：ADM matrix T2W 格已寫「48 週年度計畫；一年兩巔峰（春季選拔 + 夏季國際賽）」= bi-cycle，本 domain 提供其週期化理論背景，links 雙向可串。
- **下游待接**：Phase 2 my-site `sync_vortex.py` 加 periodization sync + vortex 呈現層；Phase 3 swim-coach `build_knowledge_index` 收進 L1 FTS；Phase 4 交付 `rules/periodization.yaml` schema 提案（Hang 自填教練參數，A-zone 不外包）。

### 已完成——canonical/development/ 新 domain：ADM 知識收編為唯一真相源

> 目標：把 ADM（Swimming Canada 運動員發展矩陣 / LTD）知識收進 TheVortexProject canonical，成為唯一真相源（一源兩消費：my-site 與 swim-coach 各自消費）。my-site `data/adm/` 為下游 sync 產物。**模組化為本次重點；橋接/呈現（Phase 4）不在此次範圍。**
> **更正（2026-06-10）**：原寫 swim-coach `rules/ltad_stages.yaml`「退役成下游 sync 副本」是錯誤 framing。用戶裁定：swim-coach（教練系統）與網站是兩個不同東西，沒有誰退役；兩邊各自消費同一份 canonical。swim-coach 自動繼承 canonical stages 為另案，rules 判斷值仍人工填。

- [x] **matrix.yaml**：`canonical/development/matrix.yaml`；4 支柱（physical/technical/mental/life）× 5 階段軸（fun/l2t/t2t/t2c/t2w；fun `has_cells:false`）+ 16 cells（`dev.{pillar}.{stage}`）。public.{summary,points} 逐字搬 my-site `data/adm/matrix.yaml`（週期化處方屬正當 prescriptive，全留 public）+ diagnostic null（ADM 無 A/B/C 感知判讀語）。technical 三格 links 串 22 std + 真實 drills/tech/l_indicators。修死連結 Fr28→Fr16。
- [x] **technical-standards.yaml**：`canonical/development/technical-standards.yaml`；附錄 A 技術基準 22 筆（`std.{stroke}.{aspect}`）= 4 式划水（free/back/fly/breast）+ 起跳×2（dive/back）+ 轉身×6（free/back/breast/fly/im-breast/im-free）。public{title/framework/applies_from:t2t/phases.criteria} + diagnostic null。左右鏡像小節（free/back pull+push）合併為單筆（側中性 criteria + note）。links 串「形式↔感知」l_indicators，全用已驗證 ID。
- [x] **驗證（throwaway script，跑完已刪）**：parse OK；cells=16 / stages=5（fun has_cells:false）/ standards=22；zero-drift（16 格 public.{summary,points} vs my-site 源檔逐格逐條零差異）；死連結=0（canonical ID universe 378，link refs 95，差集空）；appendix-a coverage 完整（22 未逐字命中者全為左右鏡像 bullet，已被 4 筆合併記錄語意涵蓋）。
- **下游待接**：my-site `sync_vortex.py` 尚未加 `sync_adm_matrix` / `sync_adm_standards`（Step 6）。~~swim-coach `rules/ltad_stages.yaml` 退役~~（取消——framing 錯誤，見 2026-06-10 更正；swim-coach 自動繼承 canonical 為另案）。

### 已完成——canonical/ 結構化資料層：散文→YAML 模組化（my-site 探索器來源）

> 目標：把 Vortex 主題層散文模組化成 my-site 可掃描 / 可篩選 / 可展開的探索器。canonical-first：結構先進 canonical/（public/diagnostic 兩層），再經 sync_vortex.py 只帶 public 傳到 my-site，diagnostic 留給 swim-coach。

- [x] **教學誤區**（commit 82f6fe0 + 9e68ffb）：6 式 76 條 → `canonical/instructional/teaching-errors.yaml`；public{misconception/physical_reason/evidence/correct_concept/perception_impact} + diagnostic{type}。my-site `vortex-errors.html` 探索器。
- [x] **技術分析**（commit 6ad36ea）：6 式 188 技術點 → `canonical/instructional/technical-analysis.yaml`；全 public（物理層）。my-site `vortex-tech.html` 探索器。
- [x] **L 指標矩陣**（commit 34090b6）：`Technica/技術指標_L級對應框架.md` → `canonical/technica/l-indicators.yaml`；43 indicators（6 levels × 5 strokes，30 格全填）；public{indicator/framework_state/quant_ref/evidence} + diagnostic{failure_signal（6 common 格）/ type（3 格 A/B/C：free.L3.evf=A / back.L4.roll-stability=C / fly.L4.outsweep=A）}。my-site `vortex-matrix.html`（ADM matrix 範式：rows=levels × cols=strokes，aspect chip → 共用 detail panel，泳式 focus 篩選 + deep-link / hash-jump）。
- 下游：my-site commit 3cf6069（Hangsau/cortex，CI green run 27053437843）；sync_vortex.py `sync_l_indicators()` 只帶 public，built HTML 診斷洩漏審查 = 0。swim-coach submodule 未 bump（l-indicators diagnostic 尚未被 vendor 消費，Phase G 再驗）。
- [x] **水感層級**（Phase D）：4 式 `Technica/*水感框架.md` → `canonical/technica/water-sense-levels.yaml`；26 levels（free/back L0–L6，breast/fly pre+L2–L6）。public{description/methods/indicators/quant/stagnation/milestone + 各式特有 four_problems/state_description/fatigue_collapse_four_layers/kaizen/stress_test} + diagnostic{type_diagnosis/type_states/type_training/type_milestones/stagnation_by_type} + 頂層 three_types/appendices。公開層三型/A/B/C 全數淨化：per-stroke 字面替換（如「重新做三型診斷」→「重新確認感知缺陷的主要方向」、移除「（A型）」標記）+ 把 stagnation 內的 A/B/C 型專屬尾段抽出搬到 `diagnostic.stagnation_by_type`；審查 regex（三型|A型|B型|C型|哪型|不論主型|typical_speech|main_problem|chain_breakpoint|failure_trigger）over public = 0 leaks。⚠ 訂正：本 Phase D 只完成 canonical + sync，my-site 呈現頁當時**並未實際建出**（曾誤記為「vxl- 縱向序列卡已建」，但 my-site layouts 從未有該檔，data 一直是孤兒）。my-site `vortex-levels.html` 於 **2026-06-11**（my-site commit 85546b6）才真正建出，設計是泳式 rail + 各級 `<details class="vx-level">` ladder（重用 vortex.js 面板切換，非 vxl- 卡片），並設為首頁第四塊主入口。
- 下游：my-site `sync_vortex.py` `sync_water_sense_levels()` 只帶 public（three_types/appendices/每 level diagnostic 整塊不取），built HTML 診斷洩漏審查 = 0。swim-coach submodule 未 bump（water-sense-levels diagnostic 尚未被 vendor 消費，Phase G 再驗）。

### 已完成——Drills/ 補入 how_to 操作步驟（commit a4ddee1）

- [x] 5 個 `Drills/drills_*.yaml` 全部 125 個動作補入 `how_to` 操作步驟（block list，插在 `purpose_zh` 之後）
- [x] 來源：*There's a Drill for That*（Laurie Sherret），每條過三關校正（符合研究 + 反問 + 反推）
- [x] commit `a4ddee1` 已 push 到 origin/master（524 insertions，純 how_to，0 deletions）

### 同步下游

- [x] **my-site 公開層**（commit ff69013，Hangsau/cortex）：`data/vortex/drills.yaml` 經 `sync_vortex.py` 的 `sync_drills` 合併重生；`vortex-drills.html` 渲染 how_to + 「要去感覺什麼」（`perception_goal` 改框）、移除 `failure_signal`（什麼是錯的）與成功/失敗對照、加 `#drill-<id>` 錨點；`vortex-explorer.js` drill chip 改為可點連結（對得上 `name_zh→id` 就連到 drill DB 卡片）。CI 綠、已部署
- [x] **swim-coach 診斷層**（commit 9a1fed3）：`vendor/vortex` submodule bump 到 `a4ddee1`
- 公開層原則重申：drill 內「要去感覺什麼」（perception_goal）屬可公開的感知目標；「感覺錯了是什麼樣」（failure_signal）只留在 canonical 診斷層，不上公開網站

---

## 當前狀態（2026-06-05）

### 內容修正
- [x] **物理數值/歸因三關校正回原始資料（2026-06-05，配合 my-site explorer 沒過清單）**：
  - 波阻定律 `F ∝ v⁴` → `F ∝ v³`，並改為「接近競速時約佔總阻力 25%（低速時較低）」（`Bridge/自由式感知橋接.md` + `Instructional/自由式深度技術分析.md`）
  - 小指轉朝下入水「阻力降低約 9.5%」→ 改為「有助降低入水阻力（教練觀測，主要見於 hip-driven 自由式，非通用物理量）🟠」，移除偽精確數字（`Bridge/自由式感知橋接.md`）
  - PMID 24290609 歸因修正：`Arellano, Pardillo & Gavilán 2013` → `Atkison et al. 2014`（WebFetch PubMed 確認真實作者；`Bridge/水下蝶腳感知橋接.md` + `Instructional/水下蝶腳技術分析.md` ×2 + `Instructional/水下蝶腳教學誤區深探.md`）。註：誤區深探 line 90 一處 `Arellano 2013`（無 PMID）依高風險歸因規則暫留不動
  - 蛙式「約 29% 體重出水」無可信來源 → 改為「上身過度出水（具體出水比例待查 🔴）」（`Instructional/蛙式深度技術分析.md` ×2）
- [x] `Bridge/自由式感知橋接.md`：刪除頭部位置的「頭頂放水瓶（Gary Hall Sr.）」教練觸發條件——頭頂水瓶是臉朝上的平衡訓練（仰式），自由式臉朝下且轉頭換氣放不住，屬仰式訓練誤掛到自由式。保留「蛙鏡鏡片不超過水面基準線」這個自由式有效視覺參考。此錯誤自 initial commit 起就存在，之前的口頭糾正未寫入檔案，導致重新生成 my-site explorer YAML 時再次出現；同步修正 my-site 兩層副本。

### 已完成——Drills/（新建）

- [x] `Drills/drills_freestyle.yaml` — Fr1–Fr24（24 個動作，含 Vortex 感知層標注）
- [x] `Drills/drills_backstroke.yaml` — Bk1–Bk26（26 個動作）
- [x] `Drills/drills_breaststroke.yaml` — Br1–Br34（34 個動作）
- [x] `Drills/drills_butterfly.yaml` — Fl1–Fl31（31 個動作，含水下蝶腳標注）
- [x] `Drills/drills_sculling.yaml` — Sc1–Sc10（10 個划水感知動作）
- [x] `Drills/DRILL_INDEX.md` — 完整索引（Schema / L級對應 / ABC型 / 快速查找）
- 來源：*There's a Drill for That*（Laurie Sherret），每個動作均有 `perception_goal`、`success_signal`、`failure_signal` 感知層標注

### 已完成——my-site 網頁（對應）

- [x] `data/vortex/drills.yaml` — 125 個動作合併檔（供 Hugo 讀取）
- [x] `layouts/vortex/vortex-drills.html` — 可篩選動作資料庫（泳式/L級/類別/ABC型四維篩選）
- [x] `static/css/vortex.css` — 新增 vxd-* 樣式（卡片 / 篩選鈕 / 感知行 / 分類/ABC型徽章）
- [x] `vortex-home.html` — 首頁加入動作練習資料庫入口
- [x] commit + push 到 Hangsau/cortex，CI 已觸發

---

## 當前狀態（2026-04-17）

### 已完成——Instructional/

- [x] 四式深度技術分析（自由式 / 仰式 / 蛙式 / 蝶式）
- [x] 出發與轉身技術分析（查證深化版）— Swimming Canada ADM + 實證文獻 + 背→蛙三種轉法比較（PMC7918682）+ 機制說明；剩餘 🔴×7 均確認為研究空白
- [x] **水下蝶腳技術分析.md**（獨立建立，深化版）— 壹～陸章；波動力學 / 渦流回收 / Strouhal / 踢腿力學 / 踝關節量化 / 代謝穩定性；剩餘 🔴×2
- [x] 自由式回臂入水教學誤區.md
- [x] 仰式水下動作教學爭議.md
- [x] 蛙式教學誤區深探.md
- [x] 蝶式教學誤區深探.md
- [x] **水下蝶腳教學誤區深探.md**（13條，外部來源全查証）
- [x] **出發與轉身教學誤區深探.md**（查證版，9條全查證，🔴×4 保留待深探）
- [x] **自由式教學誤區深探.md**（2026-04-17）— 23條全補完；7節；4條🔴查證完成；最終品質確認（USRPT 作者修正等）

### 已完成——Technica/

- [x] 水感指南.md（理論基礎 Part 1–6，原完整指南拆分而來）
- [x] 自由式水感框架.md（L0–L6 + 附錄，原完整指南 Part 7 提取）
- [x] 技術指標 L 級對應框架
- [x] 仰式水感框架 v4.2 / 蛙式 v5 / 蝶式 v2
- [x] **自由式水感框架.md**（2026-04-16）— 從完整指南第七部分提取；三型定義改為感知層面語言；A型確立為「分不出手跟水的互動」；四式框架齊全

### 已完成——Bridge/

- [x] 自由式感知橋接.md
- [x] 仰式感知橋接.md
- [x] 蛙式感知橋接.md
- [x] 蝶式感知橋接.md
- [x] 出發轉身感知橋接.md（完整版，2026-04-17）— 8 感知時刻 + IM 轉身（背→蛙三種轉法感知 + 蝶→背）+ Pullout 三技術感知差異 + 三型識別 + 指導語速查
- [x] **水下蝶腳感知橋接.md**（2026-04-16）— 7感知時刻 + 三型識別 + 疲勞崩潰 + 指導語速查 + SQ應用

### 已完成——Research/感知科學/

- [x] 因果倒置假設.md（主張A精確化 + L5 修訂）
- [x] 動態系統理論.md
- [x] 內臟感知與迷走神經.md
- [x] 神經學對照組三點座標.md
- [x] 感知量化SQ框架.md

### 已完成——Research/其他 + Observations/

- [x] RESEARCH_PLAN.md / FUTURE_RESEARCH.md / _INDEX.md
- [x] Observations/ 三份（L0漂浮三態診斷 / 小划手板實驗 / 指令層次設計）
- [x] **機械感受器.md**（2026-04-17）— 四類皮膚感受器特性 + 水環境影響 + 側線演化對比 + 訓練工具悖論（划手板/阻力手套）+ L級框架連結 + A型失敗神經說明；🔴×3

---

## 缺失/待建立（優先順序）

### 確認研究空白（不再追查）

- [x] **水下蝶腳技術分析 🔴×2**（2026-04-17 確認）
  - 膝蓋角度 30–40° vs 60–70°：假說合理（下踢前 vs 上踢峰值），無單一研究同步確認，**確認為研究空白**
  - Strouhal 縱向訓練後變化：現有文獻僅橫斷面描述，無縱向追蹤，**確認為研究空白**

### 中期（研究層擴充）

- [x] Research/感知科學/機械感受器.md（2026-04-17 完成）
- [x] Research/感知科學/感知學習.md（2026-04-17 完成）
- [x] Research/感知科學/feedforward機制.md（2026-04-18，整合自 Talos feedforward_mechanism.md）
- [x] Research/感知科學/隱性_顯性學習.md（v1 stub 已存在，2026-04-25，commit 33e49d8）— ⭐ 可用 Research/心理/02 + 07 的豐富素材升級為 v2；另需修 escape-bug（整檔字面 `\n`）
- [x] Research/心理/（2026-06-15 完成）— 8 份 dossier（注意力焦點/喚醒焦慮/水中恐懼/動機/意象/自我對話/心流/感知-生理）+ 00 Opus 整合總覽；感知優先重讀運動心理學，補上專案缺的心理環節
- [x] Research/物理現象/渦流回收.md（2026-04-18 完成，Talos 輔助研究）— 6 篇文獻全查證；🟢 Hochstein 2011（UUS 再捕獲）/ Takagi 2014（划水 wake capture）/ Garayev 2021（螳螂蝦跨物種）；🔴×3 待補
- [x] Research/物理現象/推進力理論演變.md（2026-04-18 完成，從 raw/notes 整合）— 阻力/升力/現代三階段；「找靜水」邏輯謬誤；🔵×2 🟡×4 🟢×1；連結 渦流回收.md / 機械感受器.md / 誤區深探
- [x] Research/物理現象/自然頻率.md（2026-04-25 完成，Talos + Claude 協作，v1 committed，c500f7b）
- [x] Research/物理現象/彈性蓄能.md（2026-04-25 完成，Talos + Claude 協作，v4 committed）

### 長期（需累積素材）

- [ ] Observations/ 更多教學案例（需實際教學素材）
- [ ] SQ框架最小可行觀察計畫執行（見感知量化SQ框架.md）

---

## 下一步建議

### 心理層：A/B/C/D 四批次已收束（2026-06-15）

心理層的缺口補強任務完成（查證債 / 整合缺口 / 族群覆蓋 / 補厚單薄段）。跨檔工程剩一件：
1. ~~**`隱性_顯性學習.md` 升 v2**~~ **已完成（2026-06-16，見當前狀態）**——並攔截更正一處 Liao & Masters 桌球/游泳誤歸因（連帶修 00/07/_INDEX/RESEARCH_PLAN）。
2. ~~**各 dossier 殘餘 🔴 逐條查證**~~ **已系統性收束（2026-06-16，B1–B4 全 8 dossier 引用查證，見當前狀態）**：所有「待查引用」🔴 已全數查證或釐清（含攔截 4 處誤歸因/誇大結果）；殘餘 🔴 皆為真研究空白（已明確標界「目前文獻無此數據」），保留為未來實驗設計起點，非未完成查證債。
3. ~~**Phase 2：心理層接入 Vortex 網站**~~ **全部完成（2026-06-16，見當前狀態）**——8 主題 62 概念全上線，三帶「心理地圖」著陸頁＋首頁入口＋public/diagnostic 分層 0 洩漏＋三關校正，my-site CI success。

### Phase 2 量產：心理層 8 主題全部完成 ✅（2026-06-16）

~~pilot+stub~~ → **全部 complete**。8 主題 62 概念，每條過三關校正、public/diagnostic 分層。其餘 7 主題由 7 個並行 Sonnet agent 各讀對應 dossier 寫出，ruamel round-trip merge 進 canonical（保留 fear 手寫格式）。沒過清單見當前狀態區。**族群全光譜紀律**：各 population_note 五族群分列、不窄化。
> **後續可選增強**（非必需）：① 加 concept 級 `populations`/level tag 做跨主題「依族群/分級篩選」（類似 database 的依需求找）；② 抽查各 agent 寫的 concept 內容品質（並行產出，未逐條人工複核 phenomenon 文字，建議 Hang 讀過一輪挑語氣/誇大）；③ database 跨泳式查資料頁是否納入心理層誤區。

### 週期化白話重寫 + 模組化（一源兩消費，plan-check 已備）

**plan-check 已完成（2026-06-08，Opus）**：`plans/periodization_integration_plancheck.md`。用戶需求：把週期化資訊整合、用 Claude 白話重寫（不照搬 Bompa 抽象敘述）、可整合的全整合、模組化讓 AI/人都好查。
- **核心架構決策**：在 `canonical/periodization/*.yaml` **各節點加 `plain_zh` 欄**（不另立白話模組）+ 新增 `canonical/periodization/_index.yaml` 概念目錄（source_id + 一行白話摘要 + cert）。本 repo 是「源」，主體工作在此。
- 靠 my-site `sync_vortex.py` 的 verbatim pass-through → 白話欄與 _index 自動流到 my-site `data/periodization/` 與 swim-coach submodule 兩端。
- **接手第一步**：讀該 plan-check 檔 → `/implement`（內含 8 步執行路徑、3 風險與預案、驗收、4 個待定案點、派工建議）。白話重寫不可外包（需 Claude 統一語感 + 反幻覺把關），列 manual。

### 當前最高優先——ADM 收編下游接通（Phase 2/3）

canonical/development/ 兩檔已落地（見當前狀態）。剩餘：

- [ ] **Step 6 my-site sync**：`my-site/tools/sync_vortex.py` 加 `sync_adm_matrix` + `sync_adm_standards`（仿 `sync_l_indicators`：讀 canonical development 兩層→剝 diagnostic→還原成 `adm-matrix.html` 現讀格式 `matrix.pillars[].stages[].{summary,points}`；納入 sync_state 追蹤）。
- [ ] **Step 7 my-site 驗證**：`--dry-run`→正式 sync→`hugo` build→ADM 頁面截圖比對渲染不變→commit+push（驗 CI 綠）。
- ~~**Step 8 swim-coach 退役**~~ **（取消——framing 錯誤，2026-06-10 用戶裁定）**：swim-coach 與網站是兩個不同東西，沒有「退役」這回事；原①②③作廢。canonical 是唯一真相源、swim-coach 與 my-site 各自消費；查得到的數據層可自動繼承，rules 的 # JUDGMENT 判斷值仍人工填。swim-coach 自動繼承 canonical stages 屬另案，不綁本 tracker。
- [ ] **Step 9 code-audit**：Phase 1+2+3 程式與資料改動的品質審查（push 前必跑）。

### Vortex 主題層模組化（散文→探索器）

進度（canonical-first：結構先進 canonical/，再經 my-site `sync_vortex.py` 只帶 public）：

- [x] **Phase A/A'/B/C**：教學誤區 / 技術分析 / L 指標矩陣 / Drills how_to → 已上線（見「當前狀態」）
- [x] **Phase D 水感層級**：4 式水感框架 → `canonical/technica/water-sense-levels.yaml`（26 levels，公開層三型 0 leaks）+ sync。⚠ my-site 呈現頁當時未實際建出（誤記，見上方訂正）；my-site `vortex-levels.html` 於 2026-06-11 才真正上線（rail+ladder 設計，首頁第四塊入口）。
- [ ] **Phase E 退役 Bridge/**：Bridge/ 散文已被 `canonical/perception/*.yaml`（public/diagnostic 兩層）+ stroke explorer 的 `data/vortex/{stroke}.yaml` 取代 → 冗餘。做法：① Bridge/*.md 加 deprecated 標頭（不刪）② my-site `sync_vortex.py` 移除 Bridge layer ③ 清空 `content/vortex/bridge/` ④ 首頁移除感知橋接卡。水感指南（基礎理論長文）保留為唯一散文（single.html）。
- [ ] **Phase F 首頁重設計**：把首頁做成真正的「感知地圖」= 泳式×層 矩陣／控制台，單一視覺語言。⚠️ 用戶已兩次不滿目前排列 → **此階段必須先取得用戶明確方向確認，不可自走**。
- [ ] **Phase G 收尾**：full sync + `--dry-run` 驗證、文件對齊（_INDEX / 兩邊 HANDOFF / vortex_sync_state.json）、swim-coach submodule 僅在 diagnostic 真被消費時才 bump。

待用戶決定：① 輪替先前暴露的 TheVortexProject token；② 是否把本 repo 既有未提交 WIP（CLAUDE.md / 蝶式深度技術分析.md / canonical/perception/ / 教學競技框架_v1.md / 沒過清單）併入或另行處理（本 session 未動）。

---

**前次 session（2026-04-25）完成：**
- `Research/物理現象/彈性蓄能.md` v4 — Talos + Claude 6 輪蘇格拉底教學協作完成
  - Richards 2012 整合（水阻衰減 SSC）
  - 🔵 推導格式重寫（物理演繹不需引用）
  - 所有假文獻描述清除（v1 subagent 幻覺根源識別）
  - committed to GitHub master；GitHub strikethrough bug 修正（`~` → `≈`）
- `Research/物理現象/自然頻率.md` v1 — Talos + Claude 5 輪蘇格拉底教學協作完成
  - 🔵 諧振子公式 + 水阻修正，0.8-1.5 Hz 物理推導
  - 🟢 Morris 2016（PMID 27052972 / DOI 10.1007/s00421-016-3372-4）
  - 🔴 4 項確認為研究空白（泳姿共振直接測量等）
  - committed to GitHub master（c500f7b）
  - ⚠️ 🟡 部分條目缺標題/DOI（PMID 36065966/34186517/31601852），v2 可補
- COLLAB.md Task #1、#2 標記完成
- `/check-talos-reply` skill 重大更新：新增草稿審閱 Step 4a（SCP+審閱清單），確保驗收後才宣告 goal_achieved

### 當前最高優先

**`Research/感知科學/隱性_顯性學習.md`（Task #3）**
- COLLAB.md 最後一份待建立文件
- 理論成熟但框架應用需討論，等下一輪教學 session 啟動
- Masters 1992 是起點文獻；Talos 已透過 claude-inbox 收到通知（2026-04-25）

### 已確認研究空白（彈性蓄能.md + 自然頻率.md）
- 自由式肩帶 in-vivo 彈性蓄能測量（無此文獻）
- 蝶式 dolphin kick SSC in-vivo 測量（無此文獻）
- 各泳式彈性貢獻量化 %（研究空白）
- 泳姿共振（stroke resonance）直接測量（PubMed 0 hits）
- 游泳 in-vivo 自然頻率測量（研究空白）

---

## 重要知識更新記錄

**2026-04-10** 確立：
- 感知優先的神經科學基礎（預測編碼、小腦模型、張力閘門）
- 前沿研究方向（渦流回收、感受器訓練、身體頻率、彈性蓄能）

**2026-04-11**：
- 內臟感知框架、神經學三點座標（嬰兒/魚/菁英）、L5 修訂、SQ框架、EMG悖論詳細版

**2026-04-14**：
- 出發起跳角度修正（精英 21–27°，非傳統 30–40°）
- UDK 深度修正（0.4–0.6m 實用範圍）、速度數據修正
- Kick Start 前後腳角色（後腳水平、前腳垂直，與傳統教學相反）
- 查出 3 篇文獻期刊名稱錯誤

**2026-04-16（本 session 上半段）**：
- 自由式回臂入水教學誤區.md 新建
- 仰式水下動作教學爭議.md 新建
- 蛙式教學誤區深探.md 新建
- 蝶式深度技術分析 + 蝶式教學誤區深探.md 新建（含多處文獻錯誤修正）
- 出發轉身感知橋接.md 新建
- 水下蝶腳技術分析.md 獨立建立、深化（含代謝穩定性節 Hvid 2024）
- 水下蝶腳教學誤區深探.md 新建
- **UDK 🔴×3 查證**：踝關節代償 → 🟢（PMC9402090 + PubMed 24984154）；其餘保留 🔴
- **水下蝶腳感知橋接.md 新建**（Bridge 層完整）
- **出發與轉身教學誤區深探.md 新建**（9 條全查證）

**2026-04-16（本 session 下半段）**：
- **出發與轉身技術分析第二輪查證**（🔴 8 → 7）：
  - 填入：膝蓋角度 100–120°（PMC6409673）+ 背→蛙規則（FINA SW 6.4）+ 蝶→背效率（PubMed 30694108）
  - 補充機制說明：過淺入水（PubMed 25455956）+ Pullout 三技術（PMC9445308）+ 翻滾啟動 + 仰式 OBL2（PubMed 28975846）
  - 剩餘 🔴×7 確認為研究空白或個體差異大，近期無需再查

**2026-04-17**：
- **出發轉身感知橋接補強**：IM 轉身感知（背→蛙 + 蝶→背）+ Pullout 三技術感知差異 → 感知時刻由 6 擴充至 8
- **背→蛙三種轉法補完**（技術分析 + 感知橋接兩層）：
  - Open / Bucket / Crossover 動作機制、PMC7918682 數據（推出速度差異）
  - 關鍵發現：Crossover 推出最快（2.17 m/s）但 7.5m 成績無差異——四個機制說明
  - 核心教學原則：執行穩定性 > 技術選擇
- **Technica 層重組**：
  - `游泳水感完整指南.md` 拆分為 `水感指南.md`（理論 Part 1–6）+ `自由式水感框架.md`（L0–L6，已於本 session 建立）
  - 原完整指南刪除；仰/蛙/蝶框架引用更新；重複內容消除
- **自由式教學誤區深探.md 完成**（2026-04-17 下半段）：
  - raw/notes 七份整合後刪除；七節 23 條全補完
  - 4 條 🔴 全查證：誤區 13（膝蓋角度）/ 14（踝關節訓練時程）/ 16（旋轉幅度）/ 23（CI → 特異性原則）
  - 最終品質確認：USRPT 作者 Bob Ernie 幻覺 → Dr. Brent Rushall；八/九表格殘留行清除

---

## ⚠️ 給下一個 AI 的注意事項

**本專案已發生 AI 生成虛假數據的事件，以下是核心風險點：**

1. **數字精確度陷阱**：AI 傾向用精確數字填補不確定性（來源混搭、過強用詞），使虛構內容看起來有學術感。

2. **近期文獻優先查證**：任何 2024、2025、2026 年文獻，必須用 WebSearch 實際查到才能標 🟢。

3. **確定性層次標記是信任核心**：有疑問先標 🔴，不要為了好看降低門檻。
   - 🔵 邏輯推導 / 🟢 近期文獻 / 🟡 有效舊文獻 / 🟠 教練觀測 / 🔴 待查

4. **文獻查證工作流**：
   - 物理邏輯（🔵）不需文獻
   - 教練觀測（🟠）需能指向具體來源
   - 學術文獻（🟢🟡）必須 PubMed/Google Scholar 可查到再標注

---

**2026-04-26**：
- `Research/物理現象/教學競技框架_v1.md` 新建（本地）
  - Talos swarm（talos-swarm-evolve）產出：PubMed 80+ 篇 gap 分析 + [[swimming-trends]] fuse
  - 核心 gap：真人肩/踝自然頻率泳中數據缺、渦流肩實測缺、彈性蓄能長數據缺
  - 教學 5 動作模板 + 競技 5 優化方向
  - GitHub：branch `talos-teaching-v1` → merge 入 master（PR #1）
  - 狀態：初稿 v1.0，待自測驗證 + 3 泳友小樣本
  - 後續：文獻擴充方向考慮 Claude + Talos 協作，應用方向由 Hang 決定

*最後更新：2026-06-16（Phase 2 完成：心理層 8 主題 62 概念全接入 Vortex 網站——三帶「心理地圖」著陸頁〔沿 L0→L6／初學→競技脊椎，8 主題全 complete〕+ 首頁入口。canonical/psychology/ 8 theme/62 concept〔fear 手寫 pilot + 7 主題 7 並行 Sonnet agent 寫、ruamel merge〕，每條過三關校正、public/diagnostic 0 洩漏，各 agent 沒過清單已記。my-site CI success）*
*下次更新時機：my-site 週期化知識整合（B）動工後*
