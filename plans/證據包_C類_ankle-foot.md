# C 類 ankle-foot 證據包

- **生成日期**：2026-09-02（Asia/Taipei）
- **範圍**：FR-41、BR-35、ST-19，共 3 條 C 類踝足／推進時序主張。
- **方法**：依 `plans/證據包_蒐證派工規格.md` 走三層來源；依 `plans/關節主張驗證協議.md` 裁決。來源原文、作者解釋與本專案綜合分開記錄。
- **搜尋日期**：2026-09-02。線上來源只採可穩定定位的一手研究、PubMed／PMC／期刊正式頁；系統性回顧只用來找研究與確認相位定義，不取代一手研究。
- **重要邊界**：自由式 flutter kick、蛙式 kick、俯臥 UUS 是三種不同任務。跨任務證據只能縮限或提出候選機制，不能直接當成同一泳式的效果證明。

## 執行紀錄與覆蓋

### 第 1 層：兩本游泳書

- `rg -n -C 5 "plantar flex|plantarflex|ankle flexibil" C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming C:\claudehome\resources\books\Science_of_Swimming_Faster`
- `rg -n -C 10 "feet.*together|legs.*together|point.*toe|finish.*kick" C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\22_Chapter_19_Breaststroke_Kicking.md C:\claudehome\resources\books\Science_of_Swimming_Faster\42_Figure_4.1.md`
- `rg -n -C 6 "top of the kick|up kick|upkick|dorsiflex|plantar" C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\25_Chapter_22_Fundamentals_of_Dolphin_Kick.md`

### 第 2 層：本地 swimming-kinetic-chain

- `rg -n -C 6 "maximum plantar flexion|highest.*toe|dorsiflex|ankle.*ROM" C:\claudehome\resources\books\swimming-kinetic-chain\Underwater_Undulatory_Swimming_Kinematic_Systematic_Review\02_readable.md`
- 本地 43 篇原盤點的「踝」覆蓋為 0，故本層查無不能當反證；但 UUS 系統性回顧正文確有踝角與相位交界材料，依實際命中納入，並明標為二手綜合。
- 本層沒有直接回答自由式 FR-41 或蛙式 BR-35 的原始研究。

### 第 3 層：線上來源

- PubMed：`("flutter kick" AND ankle plantar flexion)` → McCullough et al. 2009，PMID 19855342。
- PMC／Frontiers：`("undulatory underwater swimming" AND ankle flexibility)` → Kuhn & Legerlotz 2022，PMCID PMC9402090。
- 期刊正式頁：`"Does ankle joint flexibility affect underwater kicking efficiency and three-dimensional kinematics"` → Shimojo et al. 2019，DOI 10.1080/02640414.2019.1633157。
- ISBS：`breaststroke kick ankle three dimensional kinematic analysis` → Matheson et al. 2011，正式論文 PDF。
- PMC：`breaststroke pullout feet come together end kick` → McCabe et al. 2022，PMCID PMC9445308。
- Frontiers／PMC：`underwater undulatory swimming ankle plantar flexion dorsiflexion phase` → Yamakawa et al. 2022，PMCID PMC9051435。

---

## FR-41｜踝蹠屈角度越大，打水效率越高

- **原文主張（逐字）**：`踝蹠屈角度越大，打水效率越高`
- **主張拆解**：
  1. 自由式 flutter kick 中，踝蹠屈是否與表現有關。
  2. 關係是否為「越大越高」的單調、近似無上限劑量反應。
  3. 終點是否真的是效率，而不是速度、衝量或單次足部推力。
  4. 蹠屈角度是否能獨立於足部浸水、內外旋、頻率與時序解釋結果。

### 第 1 層命中

1. `Fundamentals_of_Fast_Swimming/11_Chapter_8_Building_a_Faster_Freestyle_Kick.md:64,100`
   - 來源文字主張自由式快速打腿受益於「extraordinary plantar flexibility」與足部內轉；這是教練教材的機制模型，沒有樣本、對照組、效率定義或統計。
   - `:114,124` 的 45°／50° 是 Race Club 自訂陸上 squat 測法與經驗門檻，不是標準踝角，也不是水中效率閾值。
2. `Science_of_Swimming_Faster/70_Figure_6.17.md:17`
   - Keys & Lyttle 的單一菁英泳者 CFD 個案把蹠屈增加 10°，UUS 下踢足部峰值推力增加 16 N；任務是水下海豚踢、終點是 CFD 足部推力，不是自由式效率。
3. `Science_of_Swimming_Faster/79_Figure_7.5.md:5,7`
   - 同一泳者左踝總活動度 42°、右踝 35°，左右腿衝量為 35.0 與 31.2 Ns；但這是單一個案、左右側比較，且「活動度」混合蹠屈與背屈。
4. `Science_of_Swimming_Faster/80_Figure_7.6.md:5` 與 `81_Figure_7.7.md:5,7`
   - 同一泳者的六拍自由式中，起始蹠屈較大的踢次反而有較低淨推進；書中將差異歸因於足部出水。足部仍浸水的踢次即使踝柔軟度較不理想，力峰可達其他踢次約兩倍。
   - 這直接否定「只看角度即可推出效率」；浸水位置與時序是不可省略的共同決定因子。

### 第 2 層命中

- `Underwater_Undulatory_Swimming_Kinematic_Systematic_Review/02_readable.md:190,196` 報告 UUS 研究的踝 ROM 約 34°–64°，且不同研究把踝角、角速度與表現連在一起。
- 這是 UUS 二手綜合，不是自由式 flutter kick；只能提示關係可能涉及角速度、個人技術與其他關節，不能支持原句。

### 第 3 層命中

1. **McCullough et al. 2009** — [PubMed 19855342](https://pubmed.ncbi.nlm.nih.gov/19855342/)，DOI 10.1519/JSC.0b013e31819ab977。
   - 10 名 NCAA Division I 女性泳者 + 10 名休閒女性泳者；量測陸上踝蹠屈／內翻、22.86 m flutter kick 時間與 50 m 自由式時間。
   - 踝蹠屈與 flutter kick speed 為中度相關 `r = 0.509`。
   - **未回答**：效率、因果、個人內的角度增加效果、最佳值或「越大越好」。
2. **Kuhn & Legerlotz 2022** — [PMC9402090](https://pmc.ncbi.nlm.nih.gov/articles/PMC9402090/)，PMID 36032263，DOI 10.3389/fspor.2022.948034。
   - 10 名訓練良好成人泳者（5 男／5 女），隨機比較正常、貼紮限制與急性伸展增加蹠屈，節拍器控制頻率。
   - 限制蹠屈 10.42% 時，UUS 速度與 kick efficiency 低於正常；急性增加蹠屈 6.87% 後，**正常與增加條件的速度、效率無顯著差異**。
   - 作者明確把結果解讀為受限會不利，但正常範圍以上可能存在平台；仍未知門檻。這是 UUS，不是自由式。
3. **Shimojo et al. 2019** — [期刊正式摘要](https://www.tandfonline.com/doi/abs/10.1080/02640414.2019.1633157)，PMID 31216935。
   - 實驗 1 為 9 男／8 女大學生泳者，節拍固定，比較正常與踝貼紮；速度由 1.33 降至 1.26 m/s。
   - Froude efficiency 0.77 vs 0.76，未改變；水中 plantar angle 159.02° vs 160.38°，也未依預期降低。單一男性的 3D 分析顯示差異較像前足旋轉受限。
   - 這再次把「速度」「效率」「蹠屈角」拆開，不能互相代換。

### 綜合與裁決

- **來源文字可支持**：可用蹠屈受限可能限制打腿表現；自由式跨人資料中，蹠屈與短距離 flutter kick 速度有中度相關。
- **作者解釋可支持**：UUS 受限—正常之間有差，但正常—急性增加之間沒有顯著差；可能是門檻／平台而非無上限線性關係。
- **本專案綜合**：原句同時錯置了關係形狀與終點。它把「受限可能不利」改寫成「角度每增加都提高效率」，並忽略足部是否浸水、三維旋轉、頻率與時序。
- **裁決：修正（部分支持核心需求，否決單調因果與效率用語）**。
- **可寫入**：`蹠屈可用範圍不足可能限制自由式打腿；現有自由式資料只建立與短距離打腿速度的相關，未建立效率因果或通用角度目標。`
- **不得寫入**：`角度越大越有效率`、任何通用角度門檻、把 UUS 急性伸展直接當自由式訓練效果。
- **movement 落地**：W4 ankle-foot 可把自由式踝蹠屈需求由「全無泳式證據」更新為「跨人相關 + 教材／個案支持，仍無相位化踝角與肌電」；介入仍須 conditional，且不得把角度、效率或劑量寫成已證實。
- **根因**：**結構性根因 1（效益句自由代換）+ 根因 2（終點／比較條件缺欄位）**；本批另見根因 7 的「相位交界壓扁」。

---

## BR-35｜蹬夾期：雙腳於動作尾聲併攏，踝關節蹠屈收尾（推進時序宣稱）

- **原文主張（逐字）**：`蹬夾期：雙腳於動作尾聲併攏，踝關節蹠屈收尾（推進時序宣稱）`
- **主張拆解**：
  1. 雙腳是否在 kick 尾聲靠攏。
  2. 蹠屈是等到雙腳併攏後才發生，還是在靠攏途中已開始。
  3. 併攏／蹠屈是主要推進事件、低阻力流線收尾，或兩者跨界。

### 第 1 層命中

1. `Science_of_Swimming_Faster/42_Figure_4.1.md:93,95,103`
   - 腿向後伸展時雙腳逐漸靠近；腿伸直時雙腳仍稍分開，之後在上升至水平線的過程中完成靠攏。
   - 同章指出，推進主要來自小腿與足內側把水向後推；單靠外展後再內收「夾在一起」的推進很少。
2. `Fundamentals_of_Fast_Swimming/22_Chapter_19_Breaststroke_Kicking.md:68-82`
   - 教材要求在雙腿仍互相靠近時立即抬腿並把腳尖指向後方；若等到雙腳已併攏才做，已太晚。
   - `:82` 把「腿向後伸直、腳尖 pointed」描述為降低下一段正面阻力的 kick finish。

### 第 2 層命中

- 原盤點無蛙式研究覆蓋，查無不具推論力。本條不以本層下結論。

### 第 3 層命中

1. **Matheson et al. 2011** — [ISBS 正式頁](https://ojs.ub.uni-konstanz.de/cpa/article/view/4840)；[4 頁論文 PDF](https://ojs.ub.uni-konstanz.de/cpa/article/view/4840/4480)。
   - 12 名 NCAA Division I 女性泳者，三台水下攝影機建立 3D 下肢模型。
   - 推進相操作定義為「膝伸展開始」到「雙腿完成內收」；因此「併攏」可作研究相位終點，但不是單獨的推力證明。
   - 踝總角位移與髖前進速度無顯著關聯；最大踝動作與蹠屈角速度出現在推進相早期，尾端動作最少。結論偏向**時序與角速度**，不是末端角位移越大越好。
2. **McCabe et al. 2022** — [PMC9445308](https://pmc.ncbi.nlm.nih.gov/articles/PMC9445308/)，PMID 36081618，DOI 10.3389/fspor.2022.963578。
   - 60 名菁英泳者、150 筆世界大賽／奧運比賽影像；研究對象是水下 pullout。
   - 研究把 propulsive kick 定義為雙腳第一次後移，到「雙腳靠攏、結束向內側移動」；第三段 glide 從雙腳併攏開始。
   - 這支持「雙腳併攏是 kick→glide 的事件邊界」，但沒有量踝蹠屈角，也不能直接外推整個水面蛙式週期。
3. **Olstad et al. 2014** — [BMS 文獻紀錄](https://bms.sport-iat.de/bms/Record/4032654)。
   - 3D 自動追蹤顯示，傳統「雙腳主動併攏即 kick 結束」模型無法準確切分所有 modern wave-kick 泳者；不同波幅會改變 insweep 與收腿時序。
   - 此來源用於界定模型差異，不用來否定雙腳會靠攏。

### 綜合與裁決

- **來源文字可支持**：雙腳在 kick 尾聲完成靠攏；在某些研究模型中，它就是 propulsive kick 與 glide 的事件邊界。
- **來源同時要求修正**：踝蹠屈／腳尖後指應在雙腿仍靠近途中開始；不是「先併攏，再蹠屈」。主要推進來自腿伸展與小腿／足內側向後推水，單純末端夾腿推進很少。
- **本專案綜合**：原句若只表達「末端姿勢」大致成立；若讀成「最後一刻才蹠屈，靠併攏完成主要推進」則時序與機制都錯。蹠屈跨越推進末段與低阻力 glide 準備，不應只掛一個點事件。
- **裁決：部分支持 + 時序修正（型 3：相位內有變化）**。
- **可寫入**：`蹬腿後段，雙腳在完成靠攏的同時進入 kick→glide 邊界；踝蹠屈與腳尖後指在雙腿仍靠近時已開始，用於完成流線收尾。`
- **不得寫入**：`雙腳先併攏後才蹠屈`、`靠最後夾腿產生主要推進`、把 pullout 的事件定義當所有蛙式技術唯一分期。
- **movement 落地**：W4 應把「推進段的足部角速度／方向控制」與「kick finish 的蹠屈流線姿勢」拆成相鄰需求；不要用一筆 demand 同時承載主要推進與低阻力收尾。
- **根因**：**結構性根因 7（相位交界壓成單點）**；相位、事件邊界與動作起始未分欄。

---

## ST-19｜水下海豚打腿上踢期頂點：需要足夠的踝關節背屈活動度才能有效「咬住」水面

- **原文主張（逐字）**：`水下海豚打腿上踢期頂點：需要足夠的踝關節背屈活動度才能有效「咬住」水面`
- **原註記（逐字）**：`這是在描述上踢準備相的踝關節動作（從蹠屈轉向背屈的過渡）`
- **主張拆解**：
  1. 「上踢頂點」是腳趾最高垂直座標、足部接近水面，還是某個關節角事件。
  2. 此時踝是背屈位置／背屈方向，還是已開始轉向蹠屈。
  3. 需要的是背屈 ROM、背屈角速度、肌力／控制，或只是足部三維方向。
  4. 是否有研究把上述量連到推進或「咬水」終點。

### 第 1 層命中

- `Fundamentals_of_Fast_Swimming/25_Chapter_22_Fundamentals_of_Dolphin_Kick.md:30-39` 把 cycle top 當下踢開始的事件；上踢本身也可能推進。
- `:83` 描述強調上踢時仍把 toes pointed backward。這是教練教材與個案 VM 解釋，不是踝角量測，但方向上不支持「頂點要靠背屈咬水」。
- `:95-99` 同一個案即使強化上踢，平均總速反而較低；顯示單一視覺口令不能直接推出整體效率。

### 第 2 層命中

- `Underwater_Undulatory_Swimming_Kinematic_Systematic_Review/02_readable.md:178`：多數研究以腳趾最高、最低垂直座標切分 upkick／downkick；「頂點」是相位事件，不等於水面接觸。
- `:774`：Willems 等人的最大踝蹠屈事件出現在腳趾最高位置**稍後**，此時泳者已向下推水。這表示 apex 後已進入下踢，且關鍵踝角事件不是「頂點背屈」。
- `:806`：文獻多為俯臥 UUS，仰臥體位的表現決定因子仍缺；不得把俯臥相位直接當所有超流線體位的共同結論。

### 第 3 層命中

1. **Yamakawa et al. 2022** — [Frontiers 正式全文](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2022.829618/full)，PMCID PMC9051435，PMID 35498520。
   - 8 名男性國家級泳者，在水槽以個人最大 UUS 速度的 70／80／90% 進行 3D 運動學與水下 EMG。
   - 週期從腳趾垂直座標最高點開始；換言之，該點是 down-kick 起點，不是獨立的「上踢準備相」。
   - 高速條件同時有更快的踝蹠屈與背屈角速度；作者解讀為更快結束背屈並更早開始蹠屈，以改善上下踢腳趾速度對稱。
   - 脛前肌在 down-kick 出現活動峰值，顯示背屈肌／背屈方向控制確有角色；但研究沒有測「背屈 ROM 足夠→咬住水面」這條因果。
2. **Veiga et al. 2022** — [PMC9566274](https://pmc.ncbi.nlm.nih.gov/articles/PMC9566274/)，DOI 10.3390/ijerph191912196。
   - 系統性回顧再次確認最高腳趾座標是相位界線，且最大蹠屈稍後出現；不同研究若把兩者混成同一位置，會造成踝 ROM 的大幅差異。

### 綜合與裁決

- **來源文字可支持**：踝在 UUS 週期中有雙向角運動與控制；背屈角速度與脛前肌活動不能被刪成「無用」。
- **來源不支持**：需要更大背屈活動度、在最高點靠背屈「咬住水面」、或此機制提升推進。
- **本專案綜合**：原句混合四件不同的事——腳趾的池畔座標、踝關節角度、踝角速度／肌肉控制、推進效果。腳趾最高點是 down-kick 的事件起點；現有量測反而顯示此後很快轉入蹠屈，最大蹠屈稍後出現。「水面」也不是相位定義，UUS 研究可在水下 1 m 進行。
- **裁決：整條不採用；保留原文作錯誤版本，改用雙向控制命題**。
- **可寫入**：`俯臥 UUS 的腳趾最高點標記下踢開始；踝在週期中需要蹠屈與背屈雙向角速度／控制，最大蹠屈通常在最高點之後、下踢已開始時出現。`
- **不得寫入**：`頂點需要背屈活動度才能咬水`、把腳趾最高座標稱為水面、由脛前肌活動直接推出背屈活動度處方。
- **與 ST-18 的關係**：ST-18 的「持續蹠屈」只能縮限為**足部保持 pointed／整體仍處於蹠屈側的姿勢描述**，不能讀成整個上踢期只有單向蹠屈角運動。量測顯示踝有雙向角速度，且相位交界後才到最大蹠屈。
- **movement 落地**：不得新增「UDK 頂點背屈活動度」demand 或 stretching intervention；既有 `movement.demand.udk.down-kick.ankle-plantarflexion` 已用最高腳趾座標、最大蹠屈稍後與雙向控制描述，與本裁決一致，Step 15 不需改 canonical。
- **根因**：**結構性根因 7（相位交界壓成單點）+ 根因 1（效益句自由代換）**。

---

# 裁決總表（2026-09-02）

| ID | 類 | 衝突型 | 裁決 | 主要依據定位 | 根因 |
|---|---|---|---|---|---|
| FR-41 | C | — | 修正：保留「受限可能不利」，刪「越大越有效率」 | McCullough 2009；Kuhn 2022；SoSF Fig. 7.6–7.7 | **結構性 1 + 2** |
| BR-35 | C | 3 | 部分支持 + 時序修正：靠攏是邊界，蹠屈更早開始 | SoSF Fig. 4.1:93-103；Race Club Ch.19:78；Matheson 2011 | **結構性 7** |
| ST-19 | C | — | 整條不採用，改為相位交界的雙向控制命題 | Veiga 2022:4.3；Yamakawa 2022 Methods/Results | **結構性 1 + 7** |

計：修正 1、部分支持且修正 1、整條不採用 1；**零條原封不動通過**。

## 本批新增的結構性根因

7. **把相位交界壓成單點**（BR-35、ST-19，2/3）：原筆記用「尾聲／頂點」把至少三個事件折成同一瞬間——前一相位的末段動作、可見座標事件、下一相位的關節轉向。BR-35 因而把「雙腿仍靠近時開始蹠屈」寫成模糊的併攏收尾；ST-19 更把最高腳趾座標、水面、背屈 ROM 與推進效益接成一條。後續 movement demand 必須分列 `phase`、可見事件、關節位置／方向與效果終點，不能用一個時間詞代替。

## 對 W4 ankle-foot 的直接輸入

- FR-41：自由式踝蹠屈需求可引用 McCullough 2009 的 flutter-kick 相關，但 claim status 只能到部分支持；無效率因果、相位化踝角、通用角度或劑量。
- BR-35：將推進末段的足部方向／角速度與 glide 前的蹠屈流線收尾拆成相鄰需求；雙腳併攏是事件邊界，不是「夾腿產生主要推進」。
- ST-19：不建立頂點背屈活動度 demand 或介入；沿用既有 UDK 下踢需求的「最高腳趾座標→最大蹠屈稍後→雙向控制」。
- 本批沒有足以新增固定角度、伸展秒數、組數或週頻率的來源。

## 品質閘門

- **Source gate**：每條至少有游泳書命中；FR-41、BR-35、ST-19 均有可定位的一手或直接泳者研究。跨泳式材料已明標，不用來冒充同任務證明。
- **Claim gate**：速度、效率、推力、角度、ROM、角速度、相位事件分開記錄；未把一個終點換寫成另一個。
- **Tension gate**：保留正常—增加無差異、蛙式分期模型差異、ST-18／ST-19 的表面張力；沒有以多數決抹平。
- **Integration gate**：原錯誤句保留在主張清單；本檔記錄可寫／不得寫與 W4 落點。Step 15 不修改 canonical。
