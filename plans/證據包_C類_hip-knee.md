# C 類 hip-knee 證據包

- **生成日期**：2026-09-02（Asia/Taipei）
- **範圍**：5 條 C 類游泳專屬時序／推進主張；順序依本批指定：FR-40、BR-29、BR-30、BF-32、BF-33。BR-30 依派工規格為方法追查特例，不套一般三層檢索，也不重做 BR-23 或 BR-30 的既有裁決。
- **第 1 層**：`C:\claudehome\resources\books\Science_of_Swimming_Faster\`（234 檔）與 `C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\`（34 檔）。
- **第 2 層**：`C:\claudehome\resources\books\swimming-kinetic-chain\`（43 篇）。已知覆蓋缺口為蛙式、蝶式、踝、body roll 各 0 篇；因此 BR-29、BF-32、BF-33 在本層查無時不作推論。
- **第 3 層**：Europe PMC REST 與 NCBI E-utilities；先以主題查詢篩選，再以 `resultType=core`、`fullTextXML` 或 PubMed `efetch` 取摘要／全文段落；從命中文獻追到的原始會議論文另以出版者全文核對。
- **讀法**：引文與說明分開；引文中的省略號只表示截短，保留字序。腿／足在空間中維持窄幅或朝外，不直接轉寫成髖或膝的內外旋；第一／第二踢只有在文獻明示週期起點與相位邊界時才互相比較；教材效益語句不等同於成績、阻力或效率終點；傷害頻率與風險只取自有樣本與方法的研究。

## FR-40｜髖幾乎不做外展/內收（避免打水過寬增加阻力）

- **原文主張（逐字）**：`髖幾乎不做外展/內收（避免打水過寬增加阻力）`
- **主張拆解**：① 自由式打水時髖外展／內收的實際幅度是否接近零；② 腿或足是否維持在身體投影內的窄通道；③ 加大打水寬度是否會增加主動阻力。結構性根因篩中命中 **#2（量化／比較缺座標與對照）**、**#4（由空間位置反推關節旋轉）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'legs swinging out to the side|legs and feet remain in a narrow channel|tighter motion' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（2）：`Science_of_Swimming_Faster/21_Figure_2.3.md`；`Fundamentals_of_Fast_Swimming/11_Chapter_8_Building_a_Faster_Freestyle_Kick.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/21_Figure_2.3.md:7`：
      > “The legs and feet remain in a narrow channel aligned with the body, thereby minimizing resistance.”
    - `Fundamentals_of_Fast_Swimming/11_Chapter_8_Building_a_Faster_Freestyle_Kick.md:178`：
      > “To learn to kick with a tighter motion, try placing an elastic band around both legs below the knees.”
  - 說明：第一句的所指是腿與足相對身體的空間通道，並同段允許身體滾轉下的斜向打水；第二句是教材練習提示。兩者都沒有量測股骨相對骨盆的額狀面角度，也沒有寬打水與窄打水的同協議阻力比較。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle|flutter kick).{0,120}(hip (joint )?(abduction|adduction)|kick width|narrow channel|legs? swinging out)|(hip (joint )?(abduction|adduction)|kick width|narrow channel).{0,120}(front crawl|freestyle|flutter kick)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：本次直接關係查無；此結果只描述該 43 篇本地集的覆蓋，不作陰性推論。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" OR freestyle) AND ("leg kick" OR "kicking motion") AND (drag OR resistance)`（`resultType=core`，主題查詢 63 筆）；依標題、摘要與方法篩選後，以 `EXT_ID:29921521 AND SRC:MED` 取 core record。
  - 命中（1）：PMID 29921521，Narita, Nakashima & Takagi，2018，*Effect of leg kick on active drag in front-crawl swimming: Comparison of whole stroke and arms-only stroke during front-crawl and the streamlined position*，DOI 10.1016/j.jbiomech.2018.05.027。
  - 原文句（逐字，Abstract）：
    > “although leg movement did not cause a difference in drag coefficient for front-crawl swimming, there was a large effect size (d = 1.43) at 1.3 m s−1.”
  - 說明：7 名男性競技選手在水槽以 1.1、1.3 m/s 完成全泳與只用手兩條件，並以連接泳者的 load cells 量主動阻力。這是「有無腿部動作」的阻力比較，不是打水寬度介入，也沒有髖外展／內收角度。
- **綜合**：第 1 層直接描述「窄通道」的腿足位置與教材效益，但不能由此反推髖外展／內收接近零；第 3 層直接量到主動阻力，操弄的是有無打水而非寬度。三層均未同時量測髖額狀面角度、打水寬度與阻力，因此原主張的兩段因果鏈仍缺同一協議的直接資料。
- 裁決：

## BR-29｜翻腳期：膝關節「外旋幅度」是決定鞭狀踢速度的主要因素之一（傷害相關宣稱）

- **原文主張（逐字）**：`翻腳期：膝關節「外旋幅度」是決定鞭狀踢速度的主要因素之一（傷害相關宣稱）`
- **主張拆解**：① 「膝外旋幅度」是陸上被動／主動活動度，還是水中脛骨相對股骨的動態角度；② 它與踢腿速度、踢距或教練評分的關係；③ 它與膝痛／內側組織傷害的關係。結構性根因篩中命中 **#2（量與終點未先對齊）**、**#3（力學負荷不可代替流行病學）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 5 'laxity in the knee joint.{0,220}(breaststroke|propulsion)|externally rotate at the knee joint' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（1）：`Fundamentals_of_Fast_Swimming/22_Chapter_19_Breaststroke_Kicking.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Fundamentals_of_Fast_Swimming/22_Chapter_19_Breaststroke_Kicking.md:54`：
      > “some swimmers ... have some ability to externally rotate at the knee joint, aiding their quest to increase the surface instep area pressing backward.”
  - 說明：此處以個別名將的關節鬆弛作教材例子，所指是增加向後壓水的足背表面；沒有樣本、角度量測、速度比較或傷害終點。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'breaststroke.{0,80}knee external rotation|knee external rotation.{0,80}breaststroke|whip kick.{0,80}knee rotation' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`breaststroke AND ("knee external rotation" OR "external tibial rotation") AND (speed OR performance OR pain OR injury)`（`resultType=core`，6 筆）；以 PMID／PMCID 取摘要與全文。再沿 Strzała et al. 的原始參考文獻鏈，至 ISBS 出版者 PDF 核對 Kippenhan 2002 的 Methods 與結果。
  - 命中（4）：
    1. PMID 23486737／PMCID PMC3588692，Strzała et al.，2012，*Swimming speed of the breaststroke kick*，DOI 10.2478/v10078-012-0087-4。
    2. PMID 15962572，Jagomägi & Jürimäe，2005，*The influence of anthropometrical and flexibility parameters on the results of breaststroke swimming*，DOI 10.1127/anthranz/63/2005/213。
    3. Kippenhan，2002，*Lower-extremity joint angles used during the breaststroke whip kick and the influence of flexibility on the effectiveness of the kick*，ISBS 20 Proceedings，無 PMID／DOI。
    4. PMID 7396051，Keskinen, Eriksson & Komi，1980，*Breaststroke swimmer's knee: A biomechanical and arthroscopic study*，DOI 10.1177/036354658000800402。
  - 原文句（逐字，含所在段落）：
    - Strzała et al.，Abstract：
      > “knee external rotation ... had an impact on swimming speed and kick length ... 0.35, p < 0.08”
    - Jagomägi & Jürimäe，Abstract：
      > “The most important parameter from the measured flexibility indices was knee external rotation (11.1%, R2 x 100).”
    - Kippenhan，Conclusions：
      > “External knee rotation was identified as the joint motion most likely to limit the effectiveness of the kick, especially during the downsweep.”
    - Keskinen et al.，Abstract：
      > “No significant differences in swimming technique among the six patients studied and three controls could be observed.”
  - 說明：
    - Strzała et al. 對 27 名區域／全國級選手以塑膠量角器量陸上 ROM，`Knee-Ext` 是俯臥、膝約 90°時的活動度；50 m kickboard 踢腿中，與速度的年齡控制偏相關為 0.35、`p < 0.08`，而該研究最強的速度關係是 15 秒垂直跳所得無氧耐力（0.46、`p < 0.05`）。
    - Jagomägi & Jürimäe 對 125 名 11–18 歲女性，以塑膠量角器量髖外旋、膝外旋、踝背屈與足旋後，再以 100 m kickboard 踢腿作表現終點；11.1% 是逐步迴歸的解釋量，不是水中翻腳期的動態角度占比。
    - Kippenhan 對 28 名大學校隊／休閒泳者做兩次 22.9 m kickboard 衝刺，以 60 Hz 上下水攝影、16 個體表 landmark 與 7 節段模型重建三維角度；「effectiveness」由兩名教練以 1–8 分主觀評定，和直接速度終點不同。
    - Keskinen et al. 的傷害端包含關節鏡與水槽攝影；技術比較只有 6 名患者與 3 名對照。作者把高速髖膝角運動與脛骨相對股骨外旋的重複組合列為可能機制，但病例／對照技術差異未達顯著，不能把外旋幅度單獨寫成傷害發生率或風險倍數。
- **綜合**：表現端至少有三種不同量：陸上關節 ROM（Strzała；Jagomägi & Jürimäe）、水中節段重建角度加教練評分（Kippenhan）、實際 kickboard 速度。它們不能合併成一個未定義的「翻腳期外旋幅度」。傷害端只有小樣本病例／對照與機制推測，沒有把動態膝外旋幅度作為獨立暴露量的前瞻風險研究；因此必須分開保存表現關係與傷害關係。
- 裁決：

## BR-30｜翻腳期：髖關節旋轉方向（內旋 vs 外旋）存在爭議，不同研究描述不一致

- **原文主張（逐字）**：`翻腳期：髖關節旋轉方向（內旋 vs 外旋）存在爭議，不同研究描述不一致`；⚠︎ 註記（逐字）：`BR-30：原文誠實標注此為爭議，不作斷言，是正確處理。然此條結構為「原文自承爭議的 meta 陳述」，本身是 C 類（游泳運動學爭議），不屬教科書可裁決範疇。旗標提醒：此爭議在自我驗證段有兩派說法對立，裁決時須與 BR-23 一起處理，不可單獨裁決。`
- **特例界線**：已先讀 `plans/關節主張裁決_蛙式.md:315` 起的 BR-23 裁決與 `:426` 起的 BR-30 附錄裁決；以下只記來源與測量方法，不重蒐證、不選邊、不解讀方向。
- **爭議兩派的原始文獻與測量方法**：
  - **外旋文字端**：Emily Dunlap，〈Swim Stroke Training and Modification for Rehabilitation〉，收於 Brody & Geigle 編，*Aquatic Exercise for Rehabilitation and Training*（Human Kinetics，2009，ISBN 9780736071307）；`C:\claudehome\resources\raw\notes\游泳四式關節動作全拆解(整合版).md:493` 的 `cite index="13-1"` 可追到出版者公開摘錄的 **Frog Kick: Leg Recovery Phase** 段（`https://us.humankinetics.com/blogs/excerpt/correct-form-for-the-breaststroke`）。這是復健教材的技術敘述，不是受試者研究報告。
    - 測量方法（逐字）：**原文未報告測量方法**。
  - **內旋／低外旋的直接量測端**：B. Christina Kippenhan，2001，*Influence of Lower Extremity Joint Motions on the Effectiveness of the Kick in Breaststroke Swimming*，ISBS 19 Proceedings，pp. 48–52，無 PMID／DOI；出版者 PDF：`https://ojs.ub.uni-konstanz.de/cpa/article/download/3865/3583/0`。
    - 測量方法（逐字，Methods）：
      > “Sixteen body landmarks were digitized to define a 7-segment model ... The 3D coordinates were used to compute ... hip ... internal/external rotation.”
    - 方法範圍：29 名泳者做兩次 22.9 m kickboard 蛙式踢衝刺；兩套可平移 periscope 攝影系統以 60 Hz 拍水上／水下影像，先 digitize 2D landmark，再由自製軟體重建 3D；髖旋轉是體表 landmark 加 7 節段模型計算值，不是骨性影像的直接量測。
  - **`cite index="15-1"` 的來源狀態**：現有 raw note 只有引文索引與中文轉述，沒有作者、篇名、URL 或 bibliography；本次無法把它唯一對回一篇原始研究，因此不得由其「膝屈曲時腳尖朝外」的措辭推測量測協議。
    - 測量方法（逐字）：**原文未報告測量方法**。
  - **方法缺口**：可取得的兩端並不是「兩篇都有方法、只差方法」的對稱證據：外旋教材端與 `15-1` 均無可核方法；Kippenhan 則明示以體表 landmark 建立 7 節段三維模型。尚缺一篇可識別、可重現且直接代表另一文字端的原始研究，故不能把摘要／教材姿勢詞補寫成髖旋轉量測。
- 裁決：

## BF-32｜第一次踢（較大力）：配合手臂入水+外掃，協助壓胸、啟動身體波動（推進時序）

- **原文主張（逐字）**：`第一次踢（較大力）：配合手臂入水+外掃，協助壓胸、啟動身體波動（推進時序）`
- **主張拆解**：① 「第一次踢」的週期起點與 downbeat 邊界；② 它與手入水、catch／outsweep 的相對時序；③ 「較大力」用何種力、足速或速度峰值比較；④ 壓胸／啟動波動是否為實測結果。結構性根因篩中命中 **#2（比較量未定義）**、**#7（相位交界壓成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 4 'modest downbeat of the feet|peak propulsion from the first down kick|first down kick of the cycle' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（2）：`Science_of_Swimming_Faster/44_Figure_5.1.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/44_Figure_5.1.md:13`：
      > “The downward dive is assisted by a modest downbeat of the feet that tends to rotate the body forward.”
    - `Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md:62`：
      > “first down kick ... pulling hands are near the belly button”
  - 說明：第一本書的所指是手臂回復後入水附近的一次 modest downbeat 與身體前轉；第二本書把手在腹部附近、正向後拉時的 down kick 編為「first」，並把回復臂入水時的峰值編為「second」。兩句採用的踢次編號與相位錨點需分開保存；教材均未提供兩踢同協議的力值比較。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'butterfly.{0,160}(first downbeat|first down[- ]?kick).{0,160}(hand entry|outsweep|larger|greater)|(hand entry|outsweep).{0,160}(first downbeat|first down[- ]?kick).{0,160}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND ("arm-leg coordination" OR "first downbeat" OR "second downbeat")`（`resultType=core`，12 筆）；再以 `EXT_ID:16572376 OR EXT_ID:17935810 OR PMC3761458` 精煉，PubMed `efetch` 取兩篇摘要、Europe PMC `fullTextXML` 取 Barbosa 全文。
  - 命中（3）：PMID 16572376，Chollet et al.，2006，*Arm to leg coordination in elite butterfly swimmers*，DOI 10.1055/s-2005-865658；PMID 17935810，Seifert et al.，2008，*Differences in spatial-temporal parameters and arm-leg coordination in butterfly stroke as a function of race pace, skill and gender*，DOI 10.1016/j.humov.2007.08.001；PMID 24149450／PMCID PMC3761458，Barbosa et al.，2008，*Predicting the intra-cyclic variation of the velocity of the centre of mass from segmental velocities in butterfly stroke: a pilot study*。
  - 原文句（逐字，Abstract／Discussion）：
    - Chollet et al.：
      > “entry of the hands ... high break-even point of the first undulation”
    - Seifert et al.：
      > “arms' catch phase ... first leg kick”
    - Barbosa et al.：
      > “strong first downbeat and the arm’s insweep”
  - 說明：
    - Chollet et al. 以 14 名菁英男性、四種比賽配速及影片識別手臂／腿相位；T1 是手入水與第一波動高轉折點之間的時間差，T2 是手開始向後與第一波動低轉折點之間的時間差。轉折點是時間編碼事件，不是峰值力量。
    - Seifert et al. 以 40 名泳者（菁英／較低技術、男女各組）在四種配速下錄影；其 T1 把手臂 catch 起點與第一腿 down phase 起點配對，T2 配對 arm pull 與第一腿 up phase。
    - Barbosa et al. 分別研究 4 名國際級泳者的漸增 200 m 與 7 名國家／國際級男性的最大 25 m；四視角重建手的 3D 速度、足的 2D 速度與質心速度變異。高速度模型中第一 downbeat 足垂直速度與 arm insweep 變數共同預測質心速度變異，但這是小樣本 pilot 的回歸，不是腿力直接量測。
- **綜合**：三篇研究都先定義影片事件再談第一踢；其共同可讀內容是第一 downbeat 與入水／catch 到 pull 的一段時間窗相關，而不是把入水、外掃、壓胸與推進壓成同一瞬間。Barbosa 提供足速與質心速度變異的資料，但沒有兩踢「用力大小」量表，也沒有直接量胸部下壓或波的起點；教材的 modest／first 編號又各有自己的相位錨點。
- 裁決：

## BF-33｜第二次踢（較小力）：配合手臂推水+出水，維持前進動能、避免臀部下沉（推進時序）

- **原文主張（逐字）**：`第二次踢（較小力）：配合手臂推水+出水，維持前進動能、避免臀部下沉（推進時序）`
- **主張拆解**：① 「第二次踢」的週期起點與 downbeat 邊界；② 它與 arm push／upsweep／hand exit 的相對時序；③ 「較小力」的比較量；④ 維持動能與臀部高度是否有直接終點。結構性根因篩中命中 **#2（比較量未定義）**、**#7（推水末、出水與踢腿轉折混成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 4 'downbeat of the second kick|second down kick.{0,180}(hands enter|hands strike|recovering arms|hand entry)|second-down-kick' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（2）：`Science_of_Swimming_Faster/51_Figure_5.8.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/51_Figure_5.8.md:11`：
      > “During the upsweep, the downbeat of the second kick occurs. This kick ... produces propulsion and elevates the center of mass.”
    - `Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md:62`：
      > “The second peak propulsion ... occurs precisely as the recovering arms hit the water.”
  - 說明：第一本書把 second kick 的 downbeat 放在水下 upsweep／接近出手的時間窗；第二本書把「second」的推進峰放在回復臂再次入水。兩者各自的週期錨點不同。前者談整體質心抬升，不等同於單獨量臀部高度；後者談教材／VM 峰值，不提供「較小力」的跨踢比較。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'butterfly.{0,160}(second downbeat|second down[- ]?kick).{0,160}(hand exit|upsweep|smaller|hip)|(hand exit|upsweep).{0,160}(second downbeat|second down[- ]?kick).{0,160}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND ("arm-leg coordination" OR "first downbeat" OR "second downbeat")`（`resultType=core`，12 筆）；再以 `EXT_ID:16572376 OR EXT_ID:17935810 OR PMC3761458` 精煉，PubMed `efetch` 取兩篇摘要、Europe PMC `fullTextXML` 取 Barbosa 全文。
  - 命中（3）：PMID 16572376，Chollet et al.，2006，DOI 10.1055/s-2005-865658；PMID 17935810，Seifert et al.，2008，DOI 10.1016/j.humov.2007.08.001；PMID 24149450／PMCID PMC3761458，Barbosa et al.，2008。
  - 原文句（逐字，Abstract／Discussion）：
    - Chollet et al.：
      > “hands' release ... low break-even point of the second undulation”
    - Seifert et al.：
      > “arms' push phase ... second leg kick”
    - Barbosa et al.：
      > “strong second downbeat ... keep the hip near to surface”
  - 說明：
    - Chollet et al. 的 T3 配對手到肩垂直面與第二波動高轉折點，T4 配對手離水與第二波動低轉折點；14 名菁英男性、四種配速。
    - Seifert et al. 的 T3 配對 arm push 起點與第二腿 down phase 起點，T4 配對 arm recovery 與第二腿 up phase；40 名不同技術層級與性別的泳者、四種配速。
    - Barbosa et al. 在高速度條件觀察到第二 downbeat 的平均足垂直速度高於第一 downbeat；全速度合併模型中 arm upsweep、第二 downbeat、hand entry 與泳速共同解釋 94% 的質心速度變異。作者談強第二 downbeat 與髖接近水面的關係，但研究量的是足速、segment 速度和估算質心，不是踢力，也不是「小力」介入試驗。
- **綜合**：直接運動學資料把第二 downbeat 放在 arm push 到 hand release 的時間窗，且相位起訖會隨研究操作定義而變；另一本教材則把回復臂入水的峰值編為第二踢。Barbosa 的 pilot 同時提供質心速度變異與髖接近水面的討論，但沒有把「較小力」與「較大力」作同協議比較，也沒有單獨測試避免臀部下沉的因果效果。
- 裁決：
