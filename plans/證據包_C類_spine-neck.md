# C 類 spine-neck／軀幹旋轉證據包

- **生成日期**：2026-09-02（Asia/Taipei）
- **範圍**：12 條 C 類游泳專屬時序／推進主張；順序依本批指定：FR-10、FR-30、FR-31、FR-33、FR-43、FR-44、BR-40、BR-42、BR-43、BF-35、BF-36、ST-09。
- **原文來源**：FR-* 取自 `plans/關節主張清單_自由式仰式.md`；BR-*、BF-*、ST-09 取自 `plans/關節主張清單_蛙式蝶式超流線.md`。本批 12 條在原清單均無另附 ⚠︎ 註記。
- **第 1 層**：`C:\claudehome\resources\books\Science_of_Swimming_Faster\`（234 檔）與 `C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\`（34 檔）。
- **第 2 層**：`C:\claudehome\resources\books\swimming-kinetic-chain\`（43 篇）。依派工規格，body roll、蛙式、蝶式在本層的直接原始研究覆蓋各為 0 篇；查無時一律明記「本層無覆蓋，非陰性結果」。
- **第 3 層**：Europe PMC REST 與 NCBI E-utilities；先以主題查詢篩選，再以 `resultType=core`、`fullTextXML` 或 PubMed `efetch` 核對摘要／全文段落。資料庫未收錄但由命中文獻追到的原始會議論文，另以出版者紀錄或全文核對並明記無 PMID／DOI。
- **命中計數**：「命中檔／命中」指經全文或摘要篩選後，能直接回答主張至少一個拆解子問題的去重來源；只在參考文獻表出現、僅作發現路徑或未提供可核對內容者不計。
- **讀法**：引文與說明分開；引文中的省略號只表示截短並保留原字序。肩線、骨盆線、頭胸朝向或體表可見 roll 只記為其操作定義下的空間量；除非研究實際量測脊椎分節，否則不轉寫成脊椎旋轉。教材效益句不代替成績、阻力、效率或力量終點；負荷與疼痛不代替流行病學。凡「最大轉體／頂點／尾聲／轉換」均另核對相位末段、座標事件與下一相位是否被壓成同一瞬間。本檔只蒐證，不作裁決。

## FR-10｜前伸滑行期：軀幹同側旋轉配合

- **原文主張（逐字）**：`前伸滑行期：軀幹同側旋轉配合`
- **主張拆解**：①「前伸滑行期」採哪一套相位邊界；②「同側」相對於前伸手、划手、下沉肩或呼吸側；③量到的是肩線／骨盆線 roll、整體剛體 roll，還是脊椎分節旋轉；④最大 roll 與手入水、前伸、抓水之間是時間窗還是同一事件。結構性根因篩命中 **#2（比較量與側別未定義）**、**#4（由體表朝向反推關節旋轉）**、**#7（最大轉體與相位交界壓成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'body roll as a clock setter|shoulder roll angle|as the arm reaches forward|maximum body roll' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/18_Chapter_2__Freestyle_Technique.md`；`Science_of_Swimming_Faster/19_Figure_2.1.md`；`Science_of_Swimming_Faster/20_Figure_2.2.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/18_Chapter_2__Freestyle_Technique.md:24`：
      > “The motion that sets the clock ... is the rotation of the body about its longitudinal axis, or body roll.”
    - `Science_of_Swimming_Faster/19_Figure_2.1.md:5`：
      > “the body is rolled maximally to one side ... and is about to start back the other way”
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:11`：
      > “As the arm reaches forward, the body rolls to the other side.”
  - 說明：第一本書明說圖中的「body roll」以 shoulder-roll 時間曲線作代理；第二句把最大值與即將反向並置；第三句則以某手前伸時身體「rolls to the other side」描述相對側。這三句沒有共同定義「同側」，也沒有量測脊椎分節；`maximum body roll` 是可見座標頂點與反向交界，不能自動壓成前伸滑行期的一個瞬間。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle).{0,160}(body roll|shoulder roll|hip roll|trunk rotation).{0,160}(entry|reach|glide|catch)|(entry|reach|glide|catch).{0,160}(body roll|shoulder roll|hip roll|trunk rotation)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：關鍵字會帶出 body-roll 二手回顧／書章的發現路徑，但本地 43 篇中沒有可直接核對「前伸相位 × 同側 × 軀幹旋轉」的原始運動學研究，故不列直接命中，也不據此作陰性推論。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" AND ("body roll" OR "shoulder roll") AND (entry OR reach OR timing))`；主題篩選後以 `EXT_ID:33436944 OR EXT_ID:40921148` 取 core record，並以 PMCID `PMC7804020` 的 `fullTextXML` 核對方法與 Discussion。
  - 命中（2）：
    1. PMID 33436944／PMCID PMC7804020，Gonjo et al.，2021，*Body roll amplitude and timing in backstroke swimming and their differences from front crawl at the same swimming intensities*，DOI 10.1038/s41598-020-80711-5。
    2. PMID 40921148，Ogata et al.，2025，*Differences in the rotation angles of the upper, middle, and lower thoracic spine, lumbar spine, and pelvis during front crawl swimming*，DOI 10.1080/14763141.2025.2555368。
  - 原文句（逐字，Results／Discussion）：
    - Gonjo et al.：
      > “maximum shoulder roll peak is achieved ... from the entry phase to the subsequent arm pull phase”
    - Ogata et al.：
      > “nor in peak timing across all segments”
  - 說明：Gonjo et al. 對 10 名男性、四種強度，以 19 個體表 landmark、四台水下與兩台水上攝影機重建；shoulder roll 是左右肩關節中心連線在橫斷面投影的角度，不是脊椎旋轉。該句把峰值放在 entry→pull 的交界，沒有把整段前伸等同於峰值。Ogata et al. 對 16 名健康泳者把五個 IMU 貼在棘突上，直接比較上／中／下胸椎、腰椎與骨盆，屬本批少數可寫成分節脊椎旋轉的量測；摘要報告各節段峰值時點無顯著差異，但未以「前伸滑行期同側配合」為終點。
- **綜合**：第 1 層提供 body roll 作節律基準及「前伸時 roll」的教材描述；第 3 層把肩線峰值定位在 entry→pull 交界，且另有真正分節 IMU 研究。可保留的資料必須分成三種量：肩線 roll、整體 roll、分節脊椎旋轉；「同側」與相位模型仍未定義。最大 roll 是一個座標事件，不能替代整段前伸滑行期。
- 裁決：**修正（「同側」無座標定義，且相位錨點錯位）**
  - **「同側」在本主張中不可判真假**：`20_Figure_2.2.md:11` 原文是「As the arm reaches forward, the body rolls to the **other** side」，其語境為「右臂回復時身體由右側出水轉為左側出水」——也就是前伸手那一側**沉入水中**。同一個動作，說成「往前伸手側轉」或「往對側轉」都成立，差別只在正負向約定。原主張沒有給參考系與正負向，因此它既不能被證實也不能被推翻，這是敘述缺陷不是實證爭議。
  - **相位錨點錯位**：Gonjo et al. 2021 把肩線 roll 峰值定位在 **entry→pull 交界**，不是「前伸滑行期」全段。把峰值當成整個相位的屬性即根因 7。
  - 可寫入：① body roll 是自由式的節律基準量，教材以 shoulder roll 作代理（SoSF `18:24`，明示 proxy 關係）；② 肩線 roll 峰值落在入水期到拉手期的交界（Gonjo 2021，n=10，19 個體表標記，肩線＝左右肩關節中心連線在橫斷面的投影角）；③ 已存在真正的分節量測管道（Ogata 2025，5 個 IMU 貼棘突），可作日後升級錨點。
  - 不得寫入：任何未附正負向與參考系的「同側／對側」句；不得把肩線 roll 寫成脊椎旋轉；不得把峰值時點寫成整段前伸期的狀態。
  - movement 落地：可作 demand，但**必須帶「觀察參考系」欄**（承第 3 批 FR-40 的新增欄位需求），`phase` 用 `entry`／`pull` 並綁 `phase_model`，不得使用「前伸滑行期」這個未登錄相位名。
  - 根因：結構性 2 ＋ 結構性 4 ＋ 結構性 7

## FR-30｜划手側肩下沉、對側上抬帶動核心旋轉

- **原文主張（逐字）**：`划手側肩下沉、對側上抬帶動核心旋轉`
- **主張拆解**：①划手側與肩線上下方向如何定義；②兩肩的體表位移是否等同上軀幹 roll；③「帶動」是運動學先後、肌肉因果、浮力矩或手臂水動力造成；④「核心旋轉」是整體 torso twist 還是脊椎分節。結構性根因篩命中 **#2（量與因果方向未定義）**、**#4（肩線朝向反推核心／脊椎旋轉）**、**#7（峰值與 entry→pull 轉換壓成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'shoulder roll|maximum roll|roll itself is pulling|shoulder rotation and hip rotation|rotate at different times' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/18_Chapter_2__Freestyle_Technique.md`；`Science_of_Swimming_Faster/20_Figure_2.2.md`；`Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/18_Chapter_2__Freestyle_Technique.md:24`：
      > “the temporal pattern of the shoulder roll (a measure of body roll) ... is like a sinusoidal wave”
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:27`：
      > “The body is near its maximum roll as the catch is made. The roll ... adds greatly to the speed of the hand”
    - `Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md:34`：
      > “The body rotation is separated into shoulder rotation and hip rotation, as the two parts of the body rotate at different times.”
  - 說明：第一句明示 shoulder roll 是 body roll 的代理量；第二句是教材的 catch 附近效益模型；第三句把 shoulder 與 hip 的時間分開。三者都沒有證明「某側肩上下位移 → 核心主動旋轉」的因果鏈，也沒有把肩線 roll 轉成脊椎分節角。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle).{0,180}(shoulder (drop|downward|elevation)|body roll|torso twist).{0,180}(cause|generate|core|trunk)|(buoyancy|muscle activity).{0,180}(body roll|torso twist)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：本地集沒有直接原始 body-roll 因果研究；二手技術敘述不計直接覆蓋，亦不作陰性證據。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" AND ("shoulder roll" OR "torso twist" OR bodyroll) AND (cause OR buoyancy OR EMG OR entry))`；以 `EXT_ID:33436944 OR EXT_ID:15046989 OR EXT_ID:34002671` 取 core record，PMCID 可用者再取全文。
  - 命中（3）：
    1. PMID 33436944／PMCID PMC7804020，Gonjo et al.，2021，DOI 10.1038/s41598-020-80711-5。
    2. PMID 15046989，Yanai，2004，*Buoyancy is the primary source of generating bodyroll in front-crawl swimming*，DOI 10.1016/j.jbiomech.2003.10.004。
    3. PMID 34002671，Andersen et al.，2023（2021 online），*Is torso twist production the primary role of the torso muscles in front crawl swimming?*，DOI 10.1080/14763141.2021.1925334。
  - 原文句（逐字，Discussion／Abstract）：
    - Gonjo et al.：
      > “swimmers drive their shoulder downward throughout the entry phase”
    - Yanai：
      > “buoyant force as the primary source of generating BR”
    - Andersen et al.：
      > “a greater role in maintaining stability and controlling posture ... than producing torso twist”
  - 說明：Gonjo 的「肩下沉」仍是肩關節中心連線的體表運動學。Yanai 對 11 名男性競技泳者以兩個移動式潛望攝影機作三維分析，從全身角動量與慣性矩積分出整體 long-axis bodyroll，並分解浮力矩貢獻；其因果量不是肩膀主動「帶動核心」。Andersen et al. 對 15 名男性同步三維運動學與 torso EMG，肌電—torso twist 的峰值互相關落後 400–775 ms，作者據此把肌群角色主要解讀為穩定／姿勢控制；這也不是脊椎分節量測。
- **綜合**：肩下降可作 shoulder-roll 的可見座標描述，但三層沒有支持由此直接推出「肩帶動核心」的單一路徑。第 3 層把整體 roll 的主要生成來源量到浮力矩，並顯示 torso 肌活動與 twist 的時差不符直接產生運動的時間尺度。肩線、整體剛體 roll、torso twist 與分節脊椎旋轉必須分欄保存。
- 裁決：**修正（因果歸因錯置：漏掉外力項）——本批新增結構性根因 10 的旗艦案例**
  - **「帶動」這個因果宣稱被直接量測的資料頂掉**：Yanai 2004（n=11，兩台移動潛望攝影機三維分析，由全身角動量與慣性矩積分出整體 long-axis body roll 並分解各力矩貢獻）把 body roll 的**主要生成來源量到浮力矩**。也就是說 roll 的主導生成端既不是肩、也不是核心，而是**身體外部的浮力矩**。
  - **肌肉端的時序也對不上**：Andersen et al. 2023（n=15，同步三維運動學＋軀幹 EMG）測得肌電與 torso twist 的峰值互相關**落後 400–775 ms**，作者據此把軀幹肌角色主要解讀為維持穩定與姿勢控制，而非產生 twist。這個時間尺度不支持「肌肉主動扭轉軀幹」。
  - **可保留的只有運動學共存**：Gonjo 2021 的「swimmers drive their shoulder downward throughout the entry phase」是**肩關節中心連線的體表運動學描述**，不是肌肉驅動的證據。原主張把「兩肩上下位移」與「核心主動旋轉」用一個「帶動」串起來，等於在沒有力學量測的情況下指定了因果方向。
  - 可寫入：① 入水期肩線持續下沉是可觀察的體表運動學（Gonjo 2021）；② 整體 long-axis body roll 的主要生成來源在直接量測中是浮力矩（Yanai 2004）；③ 軀幹肌 EMG 與 torso twist 峰值相差 400–775 ms，作者歸為穩定／姿勢控制角色（Andersen 2023）。三條各自獨立保存，不得串成一句。
  - 不得寫入：「肩下沉帶動核心旋轉」或任何同義的近端驅動句；不得寫成脊椎分節旋轉；不得把「核心」當成 roll 的動力來源。
  - movement 落地：**不得**產出「用肩帶動核心」型的 intervention。核心相關 intervention 若要保留，rationale 只能寫「維持姿勢／穩定」，且須對應 Andersen 的證據等級（EMG 關聯，非介入試驗）。
  - 根因：結構性 2 ＋ 結構性 4 ＋ **新增結構性 10**（把體節間共變寫成近端驅動遠端，漏掉外力項）

## FR-31｜body roll 可增加划距與力量傳導

- **原文主張（逐字）**：`body roll 可增加划距與力量傳導`
- **主張拆解**：①「划距」是手的幾何前伸距離、stroke length／distance per stroke，還是一次划手的水下路徑；②「力量傳導」是手速、手部水動力、拉手壓力或競賽速度；③ body roll 的幅度、角速度、時點何者是暴露量；④是否有同一協議同時量 roll、划距與力量／表現終點。結構性根因篩命中 **#1（效益句在 reach、stroke length、手速、力量間自由代換）**、**#2（暴露量與終點未對齊）**、**#4（肩線 roll 當脊椎／核心旋轉）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'rolled to the side.{0,120}reach|stroke length|adds greatly to the speed of the hand|kinetic energy can be coupled|body rotation.{0,80}(propulsion|drag)' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（4）：`Science_of_Swimming_Faster/20_Figure_2.2.md`；`Science_of_Swimming_Faster/29_Shoulder_and_Hip_Roll.md`；`Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md`；`Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:17`、`:27`：
      > “when the body is rolled to the side, the hand can naturally reach comfortably forward”
      >
      > “The roll ... adds greatly to the speed of the hand”
    - `Science_of_Swimming_Faster/29_Shoulder_and_Hip_Roll.md:7`：
      > “an increase in duration of the entry phase, longer stroke length, and reduced stroke frequency have been related to better economy”
    - `Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md:48`：
      > “more kinetic energy can be coupled with the pulling hand and kick”
    - `Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md:64`、`:66`：
      > “Rotating to the side, however, does not reduce frontal drag.”
      >
      > “Body rotation is an important technique to increase propulsion, but not to reduce drag.”
  - 說明：`reach comfortably forward` 是幾何可及與對線；`stroke length ... related to better economy` 是多變項關聯；hand speed、教材的 kinetic-energy coupling、PDM 教材主張又是不同終點。這些句子的所指並不相同，故只並列，不把任何一個效益自由換成另一個。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle).{0,180}(body roll|shoulder roll|trunk rotation).{0,180}(stroke length|distance per stroke|propulsive force|hand velocity|force transfer)|(stroke length|propulsive force|hand velocity).{0,180}(body roll|shoulder roll|trunk rotation)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：本地集的 body-roll 二手回顧／書章只作第 3 層追文獻的入口，不算本層直接原始研究覆蓋。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" AND ("body roll" OR "shoulder roll" OR "upper trunk rotation") AND ("stroke length" OR propulsion OR "hand velocity"))`；以 `EXT_ID:33641596 OR EXT_ID:27414043 OR EXT_ID:20131140` 取 core record／PubMed 摘要。
  - 命中（3）：
    1. PMID 33641596，Kudo et al.，2021，*Forwards-backwards hand velocity induced by the upper trunk rotation in front crawl strokes and its association with the stroke frequency*，DOI 10.1080/02640414.2021.1892266。
    2. PMID 27414043，Kudo et al.，2017，*Relationship between shoulder roll and hand propulsion in the front crawl stroke*，DOI 10.1080/02640414.2016.1206208。
    3. PMID 20131140，Psycharakis & Sanders，2010，*Body roll in swimming: a review*，DOI 10.1080/02640410903508847。
  - 原文句（逐字，Abstract）：
    - Kudo et al. 2021：
      > “28% and 19% of the backward hand velocity was induced by the upper trunk rotation”
    - Kudo et al. 2017：
      > “a significant within-swimmers correlation between ωSR and HPL in the push phase”
    - Psycharakis & Sanders：
      > “exploration of the association between body roll and ... propulsive/resistive forces”
  - 說明：2021 研究為 15 名熟練泳者、反光標記與動作捕捉，分解 roll-pitch-yaw 對手前後速度的貢獻；它量手速，不是划距或直接力量。2017 研究為 16 名熟練泳者、最大衝刺，以 dynamic-pressure approach 估手部 drag／lift，11 人在 push phase 有個體內 shoulder-roll 角速度與 HPL 的顯著關聯；它不是 stroke-length 研究，也不是全身「力量傳導」的直接量。2010 是批判性回顧，其未來研究清單仍要求直接探索 roll 與推進／阻力力值的關係。
- **綜合**：第 1 層同時存在 reach、stroke length、hand speed 與 coupling 的不同教材所指；第 3 層直接資料到達「上軀幹旋轉對手速的運動學貢獻」及「肩 roll 角速度與估算手部 lift 的個體內關聯」，沒有同一研究證成「body roll 增加划距」與「力量傳導」兩段。若保留資料，必須逐句附暴露量、相位與終點，不能把四種效益合成一條。
- 裁決：**修正（一條主張綁兩個未證效益，須拆解；只有手速一段有量化證據）**
  - **「划距」無任何直接證據**：三層沒有任何研究以 body roll 為暴露量、stroke length／distance per stroke 為終點。`29_Shoulder_and_Hip_Roll.md:7` 的「longer stroke length ... related to better economy」是**多變項關聯敘述**，而且同段的論證方向恰好相反——它說衝刺時 stroke frequency 高導致**沒有時間 roll**，是配速決定 roll，不是 roll 決定划距。把它當「roll 增加划距」的支持是把關聯句反向使用。
  - **「力量傳導」沒有力值量測**：Kudo 2017 的 HPL 是以 dynamic-pressure approach **估算**的手部 lift，且只有 16 人中的 11 人在 push phase 有個體內顯著關聯；這是關聯不是傳導鏈。
  - **唯一站得住的是手速，且有數字**：Kudo et al. 2021（n=15，反光標記動作捕捉，分解 roll-pitch-yaw 對手前後速度的貢獻）量到**上軀幹旋轉貢獻了 28% 與 19% 的手後向速度**。這一段可寫入，但它的終點是手速，不是划距也不是力量。
  - **兩本教材對「流線」的敘述不構成矛盾**：SoSF `20_Figure_2.2.md:17` 說「the rolled position of the body assists streamlining because the head is naturally nestled close to the upper arm」，FoFS `14_Chapter_11...:64` 用 PDM 量到側身比俯臥的迎流阻力**多 1.8%**、並明寫「Rotating to the side, however, does not reduce frontal drag」。過根因 8 三問：同一相位嗎？前者講前伸瞬間的體節對線，後者是固定姿勢的被動拖曳；同一個量嗎？前者是體節對線（不 kink），後者是迎流截面阻力；各自有方法可核嗎？前者是教材描述、後者有 PDM 數值。**三問皆否，所以是不同所指，不是學界分歧，也不得寫成教材對撞。**
  - 可寫入：上軀幹旋轉對手後向速度的量化貢獻（28%／19%，Kudo 2021，須附相位與量測方式）。
  - 不得寫入：「body roll 增加划距」；「力量傳導」；「body roll 減少阻力」；以及把上述任兩者用「因此」連起來。
  - movement 落地：可產出一條 demand，但主張句必須改寫成「上軀幹旋轉對手的後向速度有可量化貢獻」，且 `evidence_profile` 標為單一運動學研究、`derived_from_ids` 指回 instructional。原句的「划距」與「力量傳導」兩段落 `evidence-gap` ＋ `action_status: do-not-prescribe`。
  - 根因：結構性 1（效益句自由代換，本批最典型）＋ 結構性 2 ＋ 結構性 4

## FR-33｜骨盆隨軀幹旋轉同步轉動

- **原文主張（逐字）**：`骨盆隨軀幹旋轉同步轉動`
- **主張拆解**：①「軀幹」是肩線、上軀幹、胸腰椎或整體身體；②「骨盆轉動」是左右髖中心連線的 hip roll 還是骨盆剛體角；③「隨」表示因果、方向相同或只是共存；④「同步」容許多少時差、比較峰值還是整條時間曲線。結構性根因篩命中 **#2（同步容差與量測座標未定義）**、**#4（肩／髖線反推脊椎與骨盆關節旋轉）**、**#7（兩個峰值壓成同一瞬間）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'hips do not roll as much|hip roll tends to occur automatically|independency of the hips and shoulders|peak hip rotation occurs after the peak shoulder rotation' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/20_Figure_2.2.md`；`Science_of_Swimming_Faster/29_Shoulder_and_Hip_Roll.md`；`Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:37`：
      > “the hips do not roll as much as the shoulders do ... the hip roll tends to occur automatically in response to the shoulder roll”
    - `Science_of_Swimming_Faster/29_Shoulder_and_Hip_Roll.md:9`：
      > “a change in one is not necessarily reflected in a proportional change in the other”
    - `Fundamentals_of_Fast_Swimming/13_Chapter_10_Freestyle_Coupling_Motions.md:60`：
      > “The peak hip rotation occurs after the peak shoulder rotation. The two events are separated by about .2-.3 seconds.”
  - 說明：第一句是教材的自動反應模型，且同時明說幅度不同；第二句所指是肩、髖 roll 幅度的相對獨立；第三句用單一教材測試例描述峰值相隔 0.2–0.3 s。它們回答的量分別是因果敘述、幅度比例與峰值時差，不能把「都往同方向」換成「全程同步」。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle).{0,180}(shoulder roll|hip roll|pelvis rotation|torso twist).{0,180}(timing|synchron|phase|lag)|(pelvis|hip roll).{0,180}(shoulder roll|trunk rotation)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：本地集無可直接核對 shoulder／hip roll 同步性的原始 body-roll 研究，不以此否定或支持主張。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" AND ("shoulder roll" AND "hip roll") AND (timing OR synchron* OR "torso twist"))`；以 `EXT_ID:18981935 OR EXT_ID:31567840 OR EXT_ID:40921148` 取 core record／PubMed 摘要。
  - 命中（3）：
    1. PMID 18981935，Psycharakis & Sanders，2009，*Shoulder and hip roll changes during 200-m front crawl swimming*，DOI 10.1249/MSS.0b013e31818160bc。
    2. PMID 31567840，Andersen et al.，2020，*Kinematic Differences in Shoulder Roll and Hip Roll at Different Front Crawl Speeds in National Level Swimmers*，DOI 10.1519/JSC.0000000000003281。
    3. PMID 40921148，Ogata et al.，2025，DOI 10.1080/14763141.2025.2555368。
  - 原文句（逐字，Abstract）：
    - Psycharakis & Sanders：
      > “no consistent pattern was found for the group”
    - Andersen et al.：
      > “range ... of torso twist ... were greater at sprint than 400-m pace”
    - Ogata et al.：
      > “five inertial measurement units attached to the spinous processes”
  - 說明：Psycharakis & Sanders 對 10 名國家／國際級男性以四台水下、兩台水上同步攝影，分別計算 shoulder roll 與 hip roll；肩幅大於髖幅，個別峰值時點不同，群組沒有一致的左右峰值時序模式。Andersen et al. 對 13 名國家級泳者作三維運動學，sprint 與 400 m 配速下 shoulder roll、hip roll 與二者相對角（torso twist）的幅度／角速度改變不同。Ogata et al. 才是直接貼附於棘突的分節量測；其下胸椎、腰椎、骨盆幅度無顯著差異，所有節段峰值時點亦無顯著差異，但「無顯著差異」不是每條時間曲線完全同步。
- **綜合**：教材與研究都要求把肩、髖／骨盆分開計算。可見肩線與髖線常同週期轉動，但幅度、角速度與個體峰值時序不必相同；分節 IMU 研究的群組結果則顯示部分下位節段峰值時點無顯著差異。原主張若要保留「同步」，仍須先定義參考系、同步容差與比較的是峰值或全曲線，不能由體表朝向直接寫成脊椎同步旋轉。
- 裁決：**修正（「同步」不成立，但也不得改寫成「不同步」的絕對句）**
  - **三筆獨立資料否定「同步」**：① FoFS `13_Chapter_10...:60`「The peak hip rotation occurs after the peak shoulder rotation. The two events are separated by about .2-.3 seconds.」；② SoSF `29_Shoulder_and_Hip_Roll.md:9` 引 McCabe & Sanders 2012——距離配速相對衝刺配速，**髖 roll 增加約 16°，肩 roll 只增加 5°**，同段並明寫「the independency of the hips and shoulders in that a change in one is not necessarily reflected in a proportional change in the other」；③ Psycharakis & Sanders 2009（n=10 國家／國際級男性，四水下＋二水上同步攝影）「no consistent pattern was found for the group」。時差、幅度不成比例、群組無一致模式，三個面向都與「同步」不合。
  - **但 Ogata 2025 的「無顯著差異」不能拿來救也不能拿來打**：過根因 8 三問。同一相位嗎？是（都是完整週期）。**同一個量嗎？否**——FoFS／Psycharakis 量的是體表肩線與髖線，Ogata 量的是貼在棘突上的 5 個 IMU（上／中／下胸椎、腰椎、骨盆）之分節角。各自有方法可核嗎？Ogata 有、FoFS 的 0.2–0.3 s 是教材單一測試例無 n 無統計。**因為第二問是否，這兩組結果不構成分歧，各自成立於各自的量。** 另外「峰值時點無顯著差異」是統計未拒絕虛無假設，不等於曲線同步——不可反向寫成「已證實同步」。
  - **「隨」的因果也只有教材模型**：SoSF `20_Figure_2.2.md:37`「the hip roll tends to occur automatically in response to the shoulder roll」是教練指導模型（原文脈絡是「教練不必特別教髖的 roll」），不是量測到的驅動關係。
  - 可寫入（四條分開）：① 髖線 roll 幅度小於肩線（SoSF `20:37`，教材；Psycharakis 2009，量測）；② 肩線與髖線峰值有時差，教材測試例報 0.2–0.3 s（FoFS，標教材模型、無統計）；③ 兩者對配速的反應不成比例（+16° vs +5°，McCabe & Sanders 2012 轉引）；④ 貼棘突的分節量測在群組層級未測到峰值時點的顯著差異（Ogata 2025，n=16）。
  - 不得寫入：「同步轉動」；也**不得寫成「已證實不同步」**——後者會把三筆體表資料誤植到分節層。不得把肩線／髖線的體表量與 IMU 分節角混為同一個量。
  - movement 落地：可產出 demand，但主張句必須指名量（肩線 roll／髖線 roll／分節角）與同步容差；`phase_model` 必填。「同步」一詞本身不得進 canonical。
  - 根因：結構性 2 ＋ 結構性 4 ＋ 結構性 7 ＋ 結構性 8（三問在此正確擋下一次假分歧）

## FR-43｜不單獨過度抬頭（避免頸椎過度伸展致下半身下沉）

- **原文主張（逐字）**：`不單獨過度抬頭（避免頸椎過度伸展致下半身下沉）`
- **主張拆解**：①「抬頭」是頭部相對水面的高度、相對軀幹的頸椎伸展，或自由式 sighting；②「過度」的角度／高度門檻；③是否有同一研究量頸椎角與下肢／髖深度；④ body roll、核心張力、浮力與頭位的替代因果。結構性根因篩命中 **#2（過度門檻與下沉終點未定義）**、**#4（頭部空間姿勢反推頸椎伸展）**；疼痛來源另受讀法紀律 4 限制，不能代替下沉或阻力終點。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'head rotates as part of the body roll|no need for the head to lift|raising the head|hips tend to sink|higher the head is lifted' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/20_Figure_2.2.md`；`Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md`；`Fundamentals_of_Fast_Swimming/15_Chapter_12_Freestyle_Breathing_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:13`、`:15`：
      > “The head rotates as part of the body roll ... There is no need for the head to lift back”
      >
      > “raising the head back ... increases the surface area exposed to the flow and thereby increases resistance”
    - `Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md:56`：
      > “when a well-conditioned swimmer relaxes the core in freestyle, the hips tend to sink down”
    - `Fundamentals_of_Fast_Swimming/15_Chapter_12_Freestyle_Breathing_Techniques.md:24`：
      > “The higher the head is lifted out of the water and the longer it stays out of the water, the more drag is caused.”
  - 說明：第一本教材把不抬頭放在 body-roll 換氣與迎流面積；第二本把髖下沉明確歸於 core 放鬆，另把抬頭歸於阻力。這些句子分別談頭部相對水面、核心控制與 drag，沒有在同一協議量頸椎伸展角和下半身深度，故不把三段串成已證實的單一因果鏈。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(front crawl|freestyle).{0,160}(head|neck).{0,160}(extend|extension|lift|look forward|sink)|(extended head|neck extended|hyperextended cervical).{0,160}(front crawl|freestyle|swimmer)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（2）：`Shoulder_Neck_Pain_Front_Crawl_Stroke_Analysis_Masters/02_readable.md`；`Spinal_Musculoskeletal_Injuries_Swimming_Technique/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Shoulder_Neck_Pain_Front_Crawl_Stroke_Analysis_Masters/02_readable.md:176`：
      > “constantly look forward during the stroke, with the neck extended”
    - `Spinal_Musculoskeletal_Injuries_Swimming_Technique/02_readable.md:132`：
      > “looking or breathing forward ... [the] neck adopting an extended and rotated position”
  - 說明：第一篇為 61 名 Masters 的問卷、影片與教練共識編碼，終點是頸痛；作者在 `:188`、`:202` 明列不能保證細微技術缺陷對應特定症狀、樣本小且動作缺陷非客觀儀器量測。第二篇是技術／傷害敘事回顧。兩者可回答「抬頭外觀是否與頸伸姿態、症狀並存」，不能回答下半身是否下沉，也不能把疼痛頻率轉成水動力結果。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(("front crawl" OR freestyle) AND ("head position" OR "neck extension") AND (drag OR "lower body" OR sinking OR pain))`；以 `EXT_ID:26839604 OR EXT_ID:37830674` 取 core record，PMCID `PMC4723180`、`PMC10572881` 取全文段落。
  - 命中（2）：
    1. PMID 26839604／PMCID PMC4723180，Cortesi & Gatta，2015，*Effect of The Swimmer's Head Position on Passive Drag*，DOI 10.1515/hukin-2015-0106。
    2. PMID 37830674／PMCID PMC10572881，Rinonapoli et al.，2023，*Shoulder and Neck Pain in Swimmers: Front Crawl Stroke Analysis, Correlation with the Symptomatology in 61 Masters Athletes and Short Literature Review*，DOI 10.3390/healthcare11192638。
  - 原文句（逐字，Methods／Abstract）：
    - Cortesi & Gatta：
      > “head-up, head-middle and head-down”
    - Rinonapoli et al.：
      > “those who kept their heads extended, reported cervical pain”
  - 說明：Cortesi & Gatta 對 10 名男性區域級泳者在水下 60 cm、1.5／1.7／1.9 m/s 被動拖曳，操弄三種「頭相對身體水平線」的位置及兩種手臂姿勢，量被動阻力；沒有游自由式、沒有頸椎角、沒有量腿或髖深度。Rinonapoli et al. 與第 2 層第一篇是同一研究的線上 metadata／全文核對，並非獨立新增樣本；其終點仍是疼痛。
- **綜合**：教材直接支持「自由式換氣不必把頭向後抬」及「頭抬得更高／更久會增加 drag」的技術模型；被動拖曳研究支持頭相對水平線位置會改變阻力。下半身下沉在本次資料中另由核心放鬆、體位與浮力討論，三層都沒有同時量頸椎伸展角與下肢深度。因此「抬頭姿勢」「頸椎伸展」「阻力」「下半身下沉」必須維持為四個未完全連通的量。
- 裁決：**修正（行為建議保留，括號內的因果鏈刪除——教材自己給的是另一個機制）**
  - **括號「頸椎過度伸展致下半身下沉」與教材原文的歸因不同**：FoFS `14_Chapter_11...:56` 原文是「when a well-conditioned swimmer **relaxes the core** in freestyle, the hips tend to sink down, **as the lift forces come from the hands and feet**. Without a tight, elevated core, there is nothing to keep that part of the body straight.」——教材把髖下沉歸給**核心放鬆**，並明白指出升力來自**手與腳**。原主張把同一個現象改掛到頸椎伸展上，等於換掉了因果來源。這與 FR-30 同型：漏掉真正的力學來源（此處是手足升力與核心張力），把兩個共存現象直接串成因果。
  - **三層無任何研究同時量頸椎角與下肢／髖深度**，因此這條因果鏈不是「證據較弱」，是**沒有被量過**。
  - **疼痛端不得挪用**：第 2 層 Masters 研究與第 3 層 Rinonapoli et al. 2023 是**同一研究**（PMID 37830674），不是兩筆獨立證據；其終點是頸痛，作者自己在 `:188`／`:202` 標明樣本小、動作缺陷非儀器量測、不能保證細微技術缺陷對應特定症狀。用它支持水動力主張命中根因 3。
  - 可寫入：① 自由式換氣不需要把頭向後抬，因為換氣可在頭自身造成的水穴中完成（SoSF `20:13`，教材技術模型）；② 頭抬離水面愈高、停留愈久，阻力愈大（FoFS `15_Chapter_12...:24`，教材）；③ 頭相對身體水平線的位置會改變被動阻力（Cortesi & Gatta 2015，n=10，水下 60 cm、1.5／1.7／1.9 m/s 被動拖曳，head-up／middle／down 三分類）。
  - 不得寫入：「頸椎過度伸展致下半身下沉」（無量測，且教材歸因於核心放鬆）；不得以頸痛資料支持任何水動力或姿勢效益句；不得把 Masters 研究計為兩筆。
  - movement 落地：行為層 demand「換氣時不額外抬頭」可保留（有 ③ 支持，但須標被動拖曳條件）。括號因果鏈落 `evidence-gap` ＋ `action_status: do-not-prescribe`，`dosage_source_ids` 留空。
  - 根因：結構性 2 ＋ 結構性 3（疼痛端）＋ 結構性 4 ＋ **結構性 10**（括號因果鏈漏掉手足升力與核心張力項）

## FR-44｜額外的頸椎伸展會破壞流線

- **原文主張（逐字）**：`額外的頸椎伸展會破壞流線`
- **主張拆解**：①「額外」相對於何種基準頸位；②頸椎伸展角與頭部 head-up 空間姿勢是否被分開量；③「流線」是身體對線、迎流面積、被動阻力或主動游速；④水面自由式能否由水下被動 glide 外推。結構性根因篩命中 **#2（基準與終點未定義）**、**#4（head-up 外觀反推頸椎伸展）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'raising the head back|head tilted forward \\(neck extended\\)|lift the head any more than|tremendous increase in frontal drag|disrupts.*alignment' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（4）：`Science_of_Swimming_Faster/20_Figure_2.2.md`；`Fundamentals_of_Fast_Swimming/08_Chapter_5_Race_Club_Technology__Propulsion_Drag_Meter.md`；`Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md`；`Fundamentals_of_Fast_Swimming/15_Chapter_12_Freestyle_Breathing_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/20_Figure_2.2.md:15`：
      > “raising the head back ... increases resistance. Second, it disrupts the rhythm and body alignment.”
    - `Fundamentals_of_Fast_Swimming/08_Chapter_5_Race_Club_Technology__Propulsion_Drag_Meter.md:47`：
      > “The head tilted forward (neck extended) ... increased drag by 4%.”
    - `Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md:30`：
      > “lifts the head out of the water in the forward direction ... causes a tremendous increase in frontal drag”
    - `Fundamentals_of_Fast_Swimming/15_Chapter_12_Freestyle_Breathing_Techniques.md:28`：
      > “the swimmer should neither turn the head nor lift the head any more than is necessary”
  - 說明：Science 一句的所指是換氣時向後抬頭、阻力與 alignment；Fundamentals 的 4% 是該教材自有 PDM、head tilted-forward 分類；sighting 與低姿換氣又是不同情境。這些句子不共用頸椎角度或「流線」操作定義，故只保存各自的姿勢與終點。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(head in alignment with the spine|head position).{0,180}(streamline|drag)|(cervical|neck).{0,160}(extension|alignment).{0,160}(streamline|drag)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（1）：`Swimming_Anatomy_Lower_Back_Injuries_Narrative_Review/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Swimming_Anatomy_Lower_Back_Injuries_Narrative_Review/02_readable.md:46`：
      > “the head in alignment with the spine, and the hips slightly elevated to reduce drag”
  - 說明：這是 2024 敘事回顧中的技術描述，不是其納入研究直接量到的頸椎角—drag 實驗；它把頭脊對線與髖位一併描述，不能隔離「額外頸伸」的獨立效果。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(("head position" AND swimmer) AND (passive drag OR hydrodynamic OR CFD))`；以 `EXT_ID:26839604 OR EXT_ID:18374343` 取 core record／PubMed `efetch`。
  - 命中（2）：
    1. PMID 26839604／PMCID PMC4723180，Cortesi & Gatta，2015，DOI 10.1515/hukin-2015-0106。
    2. PMID 18374343，Zaïdi et al.，2008，*Analysis of the effect of swimmer's head position on swimming performance using computational fluid dynamics*，DOI 10.1016/j.jbiomech.2008.02.005。
  - 原文句（逐字，Abstract）：
    - Cortesi & Gatta：
      > “reduction of 4–5.2% in the average passive drag”
    - Zaïdi et al.：
      > “Three positions of the head were studied”
  - 說明：Cortesi & Gatta 的 4–5.2% 是手臂在體側時 head-down／aligned 相對 head-up 的被動拖曳差；雙臂頭上條件為 10.4–10.9%。Zaïdi et al. 是二維、steady-state CFD，約 `10^6` Reynolds 數下比較三種頭位並觀察 wake；不是實際頸椎角量測。兩篇都在水下 glide／數值模型，不是水面主動自由式，故可回答「頭位改變阻力」，不能直接把 head-up 分類等同於額外頸椎伸展角。
- **綜合**：第 1 層明確把向後／向前抬頭連到 alignment 與阻力；第 3 層直接顯示水下被動條件的頭位會改變 drag／wake。證據終點到達 head-position hydrodynamics，但沒有以頸椎節段角為暴露量，也沒有把「破壞流線」定成單一指標；水面主動自由式與水下被動 glide 的外推邊界必須保留。
- 裁決：**需補條件（方向正確，但暴露量寫錯層級、效果量高度依賴未寫出的條件）**
  - **暴露量錯層**：三層所有可用資料的操作變項都是**頭部空間位置分類**（head-up／middle／down、head tilted forward），沒有任何一筆量到頸椎節段角。原主張以「頸椎伸展」為暴露量，是由外觀頭位反推關節動作，根因 4 的教科書級案例。修正方向是把主張改寫成頭位，而不是補一個不存在的角度。
  - **效果量隨手臂姿勢變動超過兩倍**：Cortesi & Gatta 2015 的 4–5.2% 是**手臂置於體側**時 head-down／aligned 相對 head-up 的被動阻力差；同研究**雙臂過頭**條件為 **10.4–10.9%**。FoFS 自有 PDM 另報 head tilted forward（neck extended）增加 4%。把任一數字單獨引用而不附手臂姿勢與速度，讀者會取到錯的量級。
  - **Zaïdi 2008 不是量測**：二維、steady-state CFD，約 10⁶ Reynolds 數的數值模擬；可作機制佐證，不可列為實測證據。
  - **外推邊界**：Cortesi 與 Zaïdi 都在水下被動 glide／數值域，`20_Figure_2.2.md:15` 講的是水面換氣時向後抬頭。兩者不可互推。
  - 可寫入：① 頭部相對身體水平線的位置會改變被動阻力，效果量 4–5.2%（手臂體側）／10.4–10.9%（雙臂過頭）（Cortesi & Gatta 2015，n=10，水下 60 cm 被動拖曳）；② 教材 PDM 報頭前傾（頸伸）增加阻力 4%（FoFS `08:47`，標教材自有量測、無 n 無統計）；③ 換氣時向後抬頭會增加迎流面積並干擾節律與體線（SoSF `20:15`，教材）。
  - 不得寫入：以「頸椎伸展角」為暴露量的任何句子；不得把水下被動 glide 的百分比外推到水面主動自由式；**不得引用阻力百分比而不附手臂姿勢、速度與被動／主動條件**。
  - movement 落地：可作 demand，但**需要一個新欄位承載「量測條件」**（手臂姿勢／速度／水深／被動或主動）——否則 ① 的兩組數字無法在同一條目內共存。此為本批第二個新增欄位需求。
  - 根因：結構性 2 ＋ 結構性 4

## BR-40｜蛙式沒有縱軸旋轉，軀幹動作以矢狀面的波浪起伏（核心波動）為主

- **原文主張（逐字）**：`蛙式沒有縱軸旋轉，軀幹動作以矢狀面的波浪起伏（核心波動）為主`
- **主張拆解**：①「沒有」是規則／技術模型中的非刻意 roll，還是量測值等於零；②縱軸 roll、垂直軸 yaw 與橫軸 pitch 是否分清；③「波浪起伏」量的是頭、肩、髖垂直位移、trunk pitch 或脊椎屈伸；④對稱動作、個別不對稱與疲勞下的小幅旋轉如何界定。結構性根因篩命中 **#2（零值、座標軸與主要／次要未定義）**、**#4（體表朝向／起伏反推脊椎旋轉）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'breaststroke.{0,180}(body line|upper body|lumbar|wave)|head starts to rise|upper body starts angling upward|upper body coming down' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/41_Chapter_4__Breaststroke_Technique.md`；`Science_of_Swimming_Faster/42_Figure_4.1.md`；`Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/41_Chapter_4__Breaststroke_Technique.md:24`：
      > “From the fingertips to the toes, the body forms a straight horizontal line just under the surface”
    - `Science_of_Swimming_Faster/42_Figure_4.1.md:19`：
      > “the head starts to rise toward the surface and the upper body starts angling upward”
    - `Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md:18`、`:34`：
      > “the shoulders continue to elevate ... extending or arching the lumbar spine”
      >
      > “the downward motion of the upper body ... continues ... into a small flexion of the hips”
  - 說明：三個命中都在矢狀面描述 body line、上身角度、腰椎伸展或髖屈；它們沒有量長軸 roll，更沒有把體表起伏直接量成脊椎波。教材的所指是主要技術模式，不是「所有長軸角在每一瞬間皆為 0°」的量化結果。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'breaststroke.{0,180}(longitudinal axis|body roll|trunk roll|trunk pitch|trunk extension|undulat)|(longitudinal axis|body roll|trunk roll).{0,180}breaststroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：依本批覆蓋註記，蛙式在本地 43 篇沒有直接原始研究覆蓋；關鍵字命中的跨泳式敘事回顧不列本層直接證據。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(breaststroke AND ("trunk roll" OR "longitudinal axis" OR "trunk extension" OR "three-dimensional video"))`；以 `EXT_ID:25983579 OR EXT_ID:25189996` 取 core record，PMCID `PMC4424459` 以全文／出版者 PDF 核對 Methods。
  - 命中（2）：
    1. PMID 25983579／PMCID PMC4424459，Sanders et al.，2015，*An approach to identifying the effect of technique asymmetries on body alignment in swimming exemplified by a case study of a breaststroke swimmer*，無 DOI。
    2. PMID 25189996，Mills et al.，2015，*The movement of the trunk and breast during front crawl and breaststroke swimming*，DOI 10.1080/02640414.2014.946951。
  - 原文句（逐字，Methods／Abstract）：
    - Sanders et al.：
      > “upper and lower torso ... rotate about their longitudinal axis ... albeit not deliberately in breaststroke swimming”
    - Mills et al.：
      > “during breaststroke greater trunk extension occurred”
  - 說明：Sanders et al. 是一名國際級女性蛙式選手的 4 × 100 m fatigue-set 個案，以六台同步攝影、13 節段三維模型與 inverse dynamics 分析不對稱及 yaw；方法另以肩線、髖線估上／下 torso 長軸角動量。它的所指是非刻意且可能與不對稱並存的三維運動，不是典型技術主成分的群組估計。Mills et al. 為 6 名大胸圍女性在 flume、三種胸部支撐條件，以三台相機算 trunk／breast kinematics；摘要報告蛙式 trunk extension，主要問題是衣著支撐，不是縱軸 roll。
- **綜合**：第 1 層以矢狀面的上身升降、腰伸與髖屈描述蛙式主模式；第 3 層顯示「主動技術不要求長軸 roll」與「三維個案仍可出現非刻意長軸運動／不對稱」是不同所指。不能把後者寫成脊椎旋轉，也不能把前者的「沒有」解作儀器值必為零；roll、yaw、pitch 和分節屈伸需分開。
- 裁決：**修正（絕對零值宣稱不成立；另有一個未溯源的自造詞）**
  - **「沒有」被直接量測推翻，但推翻的是措辭不是意圖**：Sanders et al. 2015 對一名國際級女性蛙式選手作 4×100 m 疲勞組、六台同步攝影、13 節段三維模型，原文寫「upper and lower torso ... rotate about their longitudinal axis ... **albeit not deliberately** in breaststroke swimming」——長軸旋轉**存在但非刻意**。原主張想表達的「蛙式不以長軸 roll 為技術機制」是對的；寫成「沒有」則是把「非主要機制」偷換成「量測值為零」。這是根因 2 的零值形式。
  - **「核心波動」未溯源**：三層沒有任何來源使用這個詞或其英文對應。教材給的是 body line、upper body angling upward、lumbar extension、hip flexion 四個各自獨立的描述（SoSF `41:24`、`42:19`；FoFS `23:18`、`:34`）。「核心波動」是本專案自造的整合詞。
  - **矢狀面為主可保留但外推邊界要寫死**：Mills et al. 2015 報「during breaststroke greater trunk extension occurred」，但受試是 **6 名大胸圍女性在 flume、三種胸部支撐條件**，研究問題是衣著支撐——這個樣本與情境不能代表一般蛙式族群。
  - 可寫入：① 蛙式技術模型以矢狀面的上身角度變化、腰椎伸展與髖屈為主（SoSF `41:24`、`42:19`；FoFS `23:18`、`:34`，教材）；② 蛙式**不以**長軸 roll 為技術機制，但三維個案量測仍記錄到非刻意的長軸旋轉與不對稱（Sanders 2015，n=1 個案）；③ 蛙式相對自由式有較大 trunk extension（Mills 2015，n=6，須附大胸圍女性／flume／胸部支撐條件）。
  - 不得寫入：「沒有縱軸旋轉」；不得把 Sanders 的非刻意長軸運動寫成脊椎分節旋轉；不得把 roll、yaw、pitch 與分節屈伸混稱。
  - movement 落地：可作 demand（②③），但②必須寫成條件式且標 `evidence_profile` 為單一個案。**「核心波動」不得進 canonical**——若要保留須先登錄 `_taxonomy.yaml` 並明標為本專案自造整合詞、非文獻術語。
  - 根因：結構性 2（零值宣稱）＋ 結構性 4 ＋ 結構性 5（自造詞未溯源）

## BR-42｜換氣時頭頸隨肩胛帶上提自然抬離水面（分期時序）

- **原文主張（逐字）**：`換氣時頭頸隨肩胛帶上提自然抬離水面（分期時序）`
- **主張拆解**：①頭部開始上升落在 outsweep、inward sweep、lift 或 propulsion 的哪一套分期；②肩胛帶上提、肩關節中心上移與整個 torso elevation 是否混用；③頸椎相對胸廓是否保持中立；④「自然」表示被手臂水動力帶起、核心動作或不主動頸伸。結構性根因篩命中 **#4（肩／頭空間位移反推肩胛帶與頸椎動作）**、**#5（分期名稱需帶來源）**、**#7（開始上升、破水與呼吸事件壓成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'head starts to rise|lifting of the torso occurs because|shoulders, head and upper body begin to elevate|begin to lift his chin|inward sweep.{0,120}face breaks' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Science_of_Swimming_Faster/42_Figure_4.1.md`；`Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md`；`Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/42_Figure_4.1.md:19`、`:29`、`:31`：
      > “the head starts to rise ... and the upper body starts angling upward in preparation for the breath”
      >
      > “During the inward sweep, not any earlier in the stroke, the face breaks the surface”
      >
      > “the lifting of the torso occurs because of the movement of the arms, not because the swimmer is actively forcing the head up”
    - `Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md:28`：
      > “Toward the end of the lift phase, the shoulders, head and upper body begin to elevate”
    - `Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md:18`：
      > “before the hands turn and press backward ... begin to lift his chin ... and elevate the shoulders”
  - 說明：Science 把「開始上升」放在有深度的拉手段，把「臉破水」另放 inward sweep，並把 torso lift 歸於手臂運動；Fundamentals 使用自己的 lift／propulsion 分期並明寫 chin 離胸。這些句子各有相位模型，且「shoulders elevate」不等於研究量到肩胛骨上提；頭開始上升、臉破水、吸氣不是同一座標事件。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'breaststroke.{0,180}(head rise|head lift|breath|scapular|shoulder elevation|neck).{0,180}(phase|timing|outsweep|insweep)|(head rise|shoulder elevation).{0,180}breaststroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：蛙式在本地集為 0 篇直接覆蓋；查無不能作時序或頸位的陰性結果。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(breaststroke AND (breathing OR "head position") AND (kinematic* OR "dual-media" OR timing))`；以 `EXT_ID:40431895` 取 core record，PMCID `PMC12115840` 取 `fullTextXML` 的 Methods、Results 與 Discussion。
  - 命中（1）：PMID 40431895／PMCID PMC12115840，Alves et al.，2025，*Analyzing Breathing Patterns in the Breaststroke Technique Through Dual-Media Kinematics and Fractal Dimension*，DOI 10.3390/s25103104。
  - 原文句（逐字，Abstract）：
    > “the non-breathing cycle had ... the smallest vertical head amplitude”
  - 說明：15 名至少區域級泳者在六週適應後完成最大 25 m；七台水下、九台水上相機、50 個反光標記建立六自由度模型。研究比較每週期換氣與每兩週期換氣，量頭／手／足／CoM 路徑及髖、膝、trunk 矢狀面幅度；沒有量肩胛骨、頸椎相對胸廓角，也沒有以 outsweep／insweep 的單一事件報告頭開始上升。其「頭的垂直幅度」不能轉寫成「肩胛帶上提」。
- **綜合**：第 1 層提供多個清楚但命名不同的相位錨點，且把「頭開始上升」「臉破水」「吸氣」分開；第 3 層可確認換氣條件會改變頭部運動幅度，但沒有肩胛或頸椎量測。原主張的「隨肩胛帶上提」只能保留為教材動作模型，不能寫成已量測肩胛帶—頭頸耦合；分期時序必須附來源。
- 裁決：**修正（「肩胛帶上提」為無量測的關節指名；三個事件被壓成一個）**
  - **「肩胛帶上提」是由肩部空間上升反推的關節動作**：三層沒有任何肩胛骨量測。教材寫的是「the **shoulders**, head and upper body begin to elevate」（FoFS `21:28`）與「elevate the shoulders」（FoFS `23:18`）——`shoulders` 在教材語境是體表可見的肩部整體位置，不是 scapulothoracic 上提。指名肩胛帶等於替教材加上它沒說的解剖層級。
  - **「自然」的機制教材已經寫死，而且不是肩胛帶**：SoSF `42_Figure_4.1.md:31`「the lifting of the torso occurs **because of the movement of the arms**, not because the swimmer is actively forcing the head up or arching the back」。上身被抬起的動力來源是**手臂的水動力**。原主張把驅動端放在肩胛帶上提，又是漏掉外力項的同型錯誤（根因 10），只是本條的證據來自教材自身而非量測。
  - **三個事件不可壓成一點**：SoSF 把「頭開始上升」放在有深度的拉手段（`42:19`），把「臉破水」另放 inward sweep 並強調「**not any earlier in the stroke**」（`42:29`），吸氣又是第三個事件。原句「隨肩胛帶上提自然抬離水面」把三者疊成同一瞬間，根因 7。
  - **兩套分期並存，不是分歧**：SoSF 用 outsweep／inward sweep，FoFS 用 lift／propulsion 四相位。過根因 8 三問：同一相位嗎？兩套相位邊界本就不同；同一個量嗎？都是可見事件；各自有方法可核嗎？都是教材觀察無量測。這是**兩套命名系統**，不是學界分歧，也不得寫成教材對撞。凡引用必須綁 `phase_model`。
  - **第 3 層只到頭部空間幅度**：Alves et al. 2025（n=15，七台水下＋九台水上相機、50 個反光標記、六自由度模型）報「the non-breathing cycle had ... the smallest vertical head amplitude」；它量頭／手／足／CoM 路徑與髖、膝、trunk 矢狀面幅度，**沒有肩胛骨、沒有頸椎相對胸廓角**。
  - 可寫入：① 頭開始上升、臉破水、吸氣是三個分開的事件，各有相位錨點（SoSF `42:19`、`:29`，須綁 phase_model）；② 上身被抬起的動力來源是手臂運動，不是主動抬頭或主動拱背（SoSF `42:31`，教材且為明確的反向指導）；③ 換氣頻率會改變頭部垂直運動幅度（Alves 2025，n=15）。
  - 不得寫入：「隨肩胛帶上提」或任何肩胛骨層級的動作指名；不得把三個事件寫成同一瞬間；不得混用 SoSF 與 FoFS 的相位名。
  - movement 落地：②是本條最有價值的產出——它是**教材主動給出的反向指導**（不要主動抬頭／拱背），可直接落成 intervention 的 rationale。①可作 demand 但 `phase` 必須來自 `_taxonomy.yaml#movement_phase_registry` 且 `phase_model` 相符（W017）。「肩胛帶上提」整段落 `evidence-gap`。
  - 根因：結構性 4 ＋ 結構性 5 ＋ 結構性 7 ＋ 結構性 10

## BR-43｜呼氣時軀幹/頸椎回到中立，配合手臂前伸與蹬腿轉為超流線（時序）

- **原文主張（逐字）**：`呼氣時軀幹/頸椎回到中立，配合手臂前伸與蹬腿轉為超流線（時序）`
- **主張拆解**：①呼氣的起訖是否有呼吸流量量測；②軀幹／頸椎「中立」各自的角度參考；③手臂前伸完成、頭入線、腿開始推進與 kick 峰值的順序；④「超流線」是一般 body line、racing streamline 或 start／turn hyperstreamline。結構性根因篩命中 **#2（中立與超流線缺操作定義）**、**#4（頭／軀幹對線反推頸椎中立）**、**#5（相位／流線名稱未綁來源）**、**#7（呼氣、回中立、手伸與蹬腿壓成單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 4 'head maintains a neutral position|head and upper body will be just getting back into line|kick is engaging|racing streamline|chin goes all the way down|cycle should start and finish' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（4）：`Science_of_Swimming_Faster/41_Chapter_4__Breaststroke_Technique.md`；`Science_of_Swimming_Faster/42_Figure_4.1.md`；`Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md`；`Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/41_Chapter_4__Breaststroke_Technique.md:20`：
      > “Every breaststroke cycle should start and finish from a highly streamlined body position, also called the body line.”
    - `Science_of_Swimming_Faster/42_Figure_4.1.md:57`、`:63`、`:77`：
      > “the head maintains a neutral position with respect to the spine”
      >
      > “When the recovery is completed, the head and upper body will be just getting back into line with the arms.”
      >
      > “the kick is engaging and pushing back when the head is just getting in between the arms”
    - `Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md:74`、`:76`：
      > “the swimmer’s arms are fully extended ... well before the kick reaches its maximum propulsion”
      >
      > “The arms get into the racing streamline very soon after the peak propulsion occurs.”
    - `Fundamentals_of_Fast_Swimming/23_Chapter_20_Breaststroke_Coupling_Motions.md:32`：
      > “Once underwater, the chin goes all the way down to his chest, as his arms are already back into racing streamline position.”
  - 說明：Science 的 body line、頭對脊椎中立、arm recovery 完成與 kick engagement 是一套時序；Fundamentals 另分 fast 與 delayed arm recovery，前者手臂先入 racing streamline，後者 kick peak 後才入線，且另主張快速 head snap。這些句子分別回答不同技術策略；只並列所指，不把命名差異當結論。四檔都沒有量呼氣流量。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'breaststroke.{0,200}(exhal|expiration|neutral|head.*line|streamline|arm recovery|leg kick).{0,200}(timing|phase|coordination)|(expiration|exhalation).{0,180}breaststroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：蛙式在本地集沒有直接原始研究覆蓋；此 0 篇不能推論呼氣、頸位或 limb-coordination 的真偽。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(breaststroke AND (expiration OR exhalation OR breathing OR "arm-leg coordination") AND (streamline OR timing OR kinematic*))`；以 `EXT_ID:40431895 OR EXT_ID:27636684` 取 core record，PMCID `PMC12115840` 取全文。
  - 命中（2）：
    1. PMID 40431895／PMCID PMC12115840，Alves et al.，2025，DOI 10.3390/s25103104。
    2. PMID 27636684，Oxford et al.，2017，*Changes in kinematics and arm-leg coordination during a 100-m breaststroke swim*，DOI 10.1080/02640414.2016.1229012。
  - 原文句（逐字，Methods／Abstract）：
    - Alves et al.：
      > “joint angles assessed the hip, knee, and trunk sagittal amplitude”
    - Oxford et al.：
      > “time between end of arm pull and start of leg kick phases”
  - 說明：Alves et al. 的六自由度模型只報髖、膝、trunk 矢狀面幅度與頭的空間路徑，沒有頸椎角或呼氣事件。Oxford et al. 對 26 名蛙式專項泳者，以三台 50 Hz 水下攝影機分析 100 m 四趟末三個週期；其 coordination phase 2 是 arm-pull 結束至 leg-kick 開始的間隔，沒有頭、頸或呼吸流量。兩篇都不能把「呼氣時」當作其事件錨點。
- **綜合**：教材能支持週期回到 body line、頭相對脊椎保持中立，以及頭入線／手臂前伸／蹬腿之間有可描述時序；但教材本身並存 fast 與 delayed recovery 兩套策略。線上研究只量到換氣條件下的空間／矢狀面量與 arm-leg 時間間隔，未量呼氣或頸椎。因此原句至少包含四個不同事件，不能壓成「呼氣時」的同一瞬間；`body line`、`racing streamline`、`hyperstreamline` 也不可互換。
- 裁決：**修正（時序錨點本身未被量過；一句綁四個事件；三個流線名詞混用）**
  - **「呼氣時」不能當時序錨點**：三層沒有任何一筆量測呼吸流量或呼氣起訖。以一個未被量測的生理事件當作四個動作的共同時間原點，等於整條時序都沒有可核的起點。這是本批唯一一條**錨點本身不存在**的主張。
  - **一句綁四個事件**：軀幹回中立、頸椎回中立、手臂前伸、蹬腿轉超流線是四個獨立事件，教材給的順序還是有條件的——SoSF `42:63` 說 recovery 完成時頭與上身「just getting back into line」，`42:77` 說「the kick is engaging and pushing back **when the head is just getting in between the arms**」；FoFS `21:74` 則說手臂完全前伸「**well before** the kick reaches its maximum propulsion」。這些是可用的時序關係，但必須逐條拆開各自帶錨點，不能壓成「呼氣時」一瞬。
  - **fast vs delayed recovery 不是分歧，是兩套策略**：過根因 8 三問。同一相位嗎？兩者刻意改變手臂入線相對 kick peak 的時點，本來就不同。同一個量嗎？是（入線 vs kick peak 先後）。各自有方法可核嗎？**都沒有**，兩者皆為教材技術主張，無量測。第一與第三問為否 → 不是型 5 學界分歧，是**兩種並存的技術策略且皆未實證**。canonical 若要收，必須兩套並列並各標為教材策略。
  - **三個流線名詞不可互換**：`body line`（SoSF `41:20`，每個週期的起訖姿勢）、`racing streamline`（FoFS `21:76`、`23:32`）、`hyperstreamline`（FoFS `26:198`，手臂在頭後、下巴貼胸的起跳姿勢）是三個不同姿勢。原主張用「超流線」一詞，在原清單語境對應 ST-* 系列的 hyperstreamline，但蛙式週期內回到的是 body line。這是根因 5 的命名混用。
  - **唯一的量測只到 arm-leg 間隔**：Oxford et al. 2017（n=26 蛙式專項，三台 50 Hz 水下攝影，100 m 四趟末三週期）的 coordination phase 2 是「time between end of arm pull and start of leg kick phases」——沒有頭、頸、呼吸。
  - 可寫入：① 蛙式週期起訖回到 body line（SoSF `41:20`，教材）；② 頭相對脊椎保持中立（SoSF `42:57`，教材，無角度定義）；③ 手臂入線與 kick peak 的相對時序存在兩套教材策略（fast／delayed），並列且各標無實證；④ arm-pull 結束至 leg-kick 開始的時間間隔是可量的協調指標（Oxford 2017，n=26）。
  - 不得寫入：「呼氣時」作為任何動作的時間錨點；不得把四個事件寫成同時；不得把 body line／racing streamline／hyperstreamline 當同義詞；不得對頸椎「中立」給角度。
  - movement 落地：④可作 demand（有量測）。①②可作姿勢層描述但標教材模型。③兩套策略並列收錄，`action_status` 不得為 prescribe。「呼氣時」整個時序框架落 `evidence-gap` ＋ `do-not-prescribe`。
  - 根因：結構性 2 ＋ 結構性 5 ＋ 結構性 7 ＋ 結構性 8

## BF-35｜蝶式沒有縱軸旋轉（與自由式、仰式的區別）

- **原文主張（逐字）**：`蝶式沒有縱軸旋轉（與自由式、仰式的區別）`
- **主張拆解**：①「沒有」是對稱泳式的主要技術模式，還是 roll 量測值為零；②正常正面換氣、閉氣與側向換氣是否同一條件；③整體 long-axis roll、肩線 roll 與脊椎分節旋轉是否混用；④左右手力矩互消是理論條件還是每位泳者的實測結果。結構性根因篩命中 **#2（零值、條件與比較座標未定義）**、**#4（整體朝向反推脊椎旋轉）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'butterfly.{0,180}(longitudinal axis|body roll|symmetrical)|no body roll occurs|body roll cannot assist|unwarranted rotation of the whole body|long axis.*direction of travel' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（5）：`Science_of_Swimming_Faster/43_Chapter_5__Butterfly_Technique.md`；`Science_of_Swimming_Faster/44_Figure_5.1.md`；`Science_of_Swimming_Faster/48_Figure_5.5.md`；`Science_of_Swimming_Faster/51_Figure_5.8.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/43_Chapter_5__Butterfly_Technique.md:10`：
      > “The body undulates upward and downward rather than rolling around the longitudinal axis”
    - `Science_of_Swimming_Faster/44_Figure_5.1.md:5`：
      > “Because butterfly is a symmetrical stroke ... the rotational effects of one arm are cancelled by ... the other arm”
    - `Science_of_Swimming_Faster/48_Figure_5.5.md:9`：
      > “no body roll occurs about the longitudinal axis”
    - `Science_of_Swimming_Faster/51_Figure_5.8.md:7`、`:15`：
      > “unlike in the front crawl, body roll cannot assist the action”
      >
      > “lateral breathing ... induced an unwarranted rotation of the whole body around the longitudinal axis”
    - `Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md:20`：
      > “body rotation in the long axis of freestyle and backstroke is desirable ... In butterfly ... the body bends on the short axis”
  - 說明：前四個一般技術句的所指是對稱蝶式不以 long-axis roll 作必要／助力機制；`51_Figure_5.8.md:15` 另限定 lateral-breathing 條件，所指是整體可見長軸轉動。兩類句子條件不同，只並列。它們都沒有量脊椎分節，左右手力矩互消也以兩手力線相似為前提。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'butterfly.{0,180}(longitudinal axis|body roll|roll angle|whole-body rotation|lateral breathing)|(longitudinal axis|body roll).{0,180}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：蝶式在本地 43 篇為 0 篇直接覆蓋；查無不等於長軸轉動不存在。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST／NCBI E-utilities，`(butterfly swimming AND (wave OR roll OR "longitudinal axis" OR "lateral breathing"))`；以 `EXT_ID:7852446` 取 PubMed 摘要，再沿呼吸研究的引用鏈至 Biomechanics and Medicine in Swimming VIII 出版者紀錄與公開 PDF。
  - 命中（2）：
    1. PMID 7852446，Sanders, Cappaert & Devlin，1995，*Wave characteristics of butterfly swimming*，DOI 10.1016/0021-9290(95)80002-6。
    2. Alves, Cunha & Gomes-Pereira，1999，*Kinematical modifications induced by the introduction of the lateral inspiration in butterfly stroke*，Biomechanics and Medicine in Swimming VIII，pp. 15–19；無 PMID／DOI。
  - 原文句（逐字，Abstract／Results）：
    - Sanders et al.：
      > “vertical undulations of the vertex ... shoulders, hips, knees, and ankles”
    - Alves et al.：
      > “a rotation around the longitudinal axis of the whole body was created”
  - 說明：Sanders et al. 對 8 名菁英男性與 8 名菁英女性，以頭頂、肩、髖、膝、踝的垂直位移及 Fourier 相位檢驗頭至足的波；該設計支持矢狀面波，但沒有量 long-axis roll。Alves et al. 比較側向與正面呼吸的影像運動學，出版者摘要用「似乎」描述側向呼吸產生整體長軸轉動；這是整體體表朝向，不是脊椎分節旋轉。
- **綜合**：教材把「不以 long-axis roll 作主要機制」作為蝶式與自由式／仰式的技術區別；原始研究直接量到的是垂直波動，而側向呼吸研究另記整體長軸轉動。證據因此必須附「一般對稱技術／特定側向呼吸」條件，且不能把整體 roll 寫成脊椎旋轉。三層未提供能支持所有條件下 roll 精確等於 0°的量測。
- 裁決：**修正（第二個零值宣稱；教材原文本身就是條件式，條件在轉寫時被刪掉）**
  - **教材的「沒有」是推導結論，且前提寫在同一句裡**：SoSF `48_Figure_5.5.md:9` 的完整脈絡是「no body roll occurs about the longitudinal axis ... **if** the hands produce similar force with lines of action equidistant from the midline of the body, the torques produced by right and left arm actions **cancel out**」。零 roll 是**左右對稱前提下的力矩互消推導**，不是量測結果。原主張把條件句轉寫成無條件斷言。
  - **條件一改就量到 roll**：SoSF `51_Figure_5.8.md:15` 轉引 Alves et al. 1999——側向換氣「induced an unwarranted rotation of the whole body around the longitudinal axis」，且該研究同時發現側向換氣的 trunk inclination 較低，作者結論是**兩種換氣技術沒有絕對優劣**。因此蝶式長軸轉動的正確寫法是條件式：對稱、正面換氣 → 力矩互消；側向換氣 → 量到整體長軸轉動。
  - **與 BR-40 同型，本批第二次**：兩條都把「非主要技術機制」寫成「量測為零」。這已足以視為 canonical 的系統性措辭風險，不是個案。
  - **FoFS 講的是另一個軸，不可混入**：`24_Chapter_21...:20` 的主題是**短軸**（「the body **bends** on the short axis, rather than rotates on the short axis」），它只是順帶提到長軸 roll 在自由式／仰式是 desirable。引用時須連同短軸語境，否則會讓讀者以為它在直接支持長軸零值。
  - **整體 roll ≠ 脊椎旋轉**：Alves 量的是整體體表朝向；Sanders et al. 1995（8 男 8 女菁英，頭頂／肩／髖／膝／踝垂直位移＋Fourier 相位）根本沒量長軸 roll。三層無任何蝶式脊椎分節量測。
  - 可寫入：① 蝶式在左右對稱、力線等距的前提下，兩臂力矩互消，故不以長軸 roll 為推進機制（SoSF `44:5`、`48:9`，教材推導，須連前提一起寫）；② 側向換氣條件下量到整體長軸轉動（Alves 1999，經 SoSF 轉引；原文為會議論文集無 PMID／DOI）；③ 蝶式的軀幹動作以垂直波動為直接量測所在（Sanders 1995，n=16）。
  - 不得寫入：「蝶式沒有縱軸旋轉」的無條件句；不得把整體 roll 寫成脊椎旋轉；不得把 FoFS 的短軸論述當長軸證據。
  - movement 落地：①③可作 demand，①**必須把對稱前提寫進主張句本身**（不放註腳）。②標為條件式例外。與 BR-40 併為同一則措辭規範：**canonical 不得出現「沒有／零」的絕對運動學宣稱**，一律改寫為「非主要機制」＋條件。
  - 根因：結構性 2（零值宣稱，本批第二次）＋ 結構性 4

## BF-36｜波動順序：胸部下壓→髖部跟隨下壓→膝屈曲蓄力→腳踝鞭動出水面（時序）

- **原文主張（逐字）**：`波動順序：胸部下壓→髖部跟隨下壓→膝屈曲蓄力→腳踝鞭動出水面（時序）`
- **主張拆解**：①胸部／肩、髖、膝、踝各以位置、角度或速度何者定義；②遠端波的相位延遲是否等同四個離散動作依序開始；③「髖跟隨下壓」是否與肩下沉時髖上升的可見位置混淆；④膝屈曲在 upkick／downkick 交界的時點；⑤「蓄力」「鞭動」「出水面」分別是否有力值、踝角與水面穿越量測。結構性根因篩命中 **#2（量與事件定義不足）**、**#4（體表位置反推關節動作）**、**#7（相位末段、反向與效果壓成四個單點）**。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'wave.{0,120}(head to feet|hips to feet)|shoulders are moving down, the hips are moving up|maximum hip flexion|knees start to bend|thoracic flexion occurs during the up kick|feet.*surface' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（6）：`Science_of_Swimming_Faster/43_Chapter_5__Butterfly_Technique.md`；`Science_of_Swimming_Faster/44_Figure_5.1.md`；`Science_of_Swimming_Faster/45_Figure_5.2.md`；`Science_of_Swimming_Faster/51_Figure_5.8.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`；`Fundamentals_of_Fast_Swimming/25_Chapter_22_Fundamentals_of_Dolphin_Kick.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Science_of_Swimming_Faster/43_Chapter_5__Butterfly_Technique.md:12`、`:24`：
      > “a wave ... travelling progressively from the head to the feet”
      >
      > “The wavelike sequence of rotations of the trunk, thighs, and shanks transmits this kinetic energy to the feet”
    - `Science_of_Swimming_Faster/44_Figure_5.1.md:13`：
      > “A body wave has transmitted the energy from hips to feet.”
    - `Science_of_Swimming_Faster/45_Figure_5.2.md:7`：
      > “While the shoulders are moving down, the hips are moving up.”
    - `Science_of_Swimming_Faster/51_Figure_5.8.md:19`：
      > “the wave progressed consistently along the body regardless of whether it was a breathing or a nonbreathing cycle”
    - `Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md:26`：
      > “maximum hip flexion ... shortly after the hands enter ... when the swimmer’s chest is pressed downward”
    - `Fundamentals_of_Fast_Swimming/25_Chapter_22_Fundamentals_of_Dolphin_Kick.md:73`、`:194`：
      > “Once Kelsi’s knees start to bend and her legs draw forward, another major deceleration occurs”
      >
      > “Thoracic flexion occurs during the up kick in preparation for a more forceful down kick”
  - 說明：`head to feet` 是連續波的相位傳遞，不等於四個離散事件的開始時刻。Science 在肩向下時明寫髖向上，所指是體表垂直位置；Fundamentals 的 chest press 同時點是最大 hip flexion（關節角），不是髖部必定向下移。膝屈曲橫跨 upkick 到下一 downkick 的準備，且伴隨教材量到的減速。六個命中均未量「踝關節鞭動」或足／踝穿越水面的事件。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 'butterfly.{0,220}(chest|shoulder|hip|knee|ankle|wave).{0,220}(sequence|phase|timing|downbeat|upbeat)|(caudal|wave travel).{0,180}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（0）：無；**本層無覆蓋，非陰性結果**。
  - 原文句（逐字 + 檔名 + 行號）：無。
  - 說明：蝶式在本地集沒有直接原始研究；水下海豚踢的系統回顧是另一情境，未列作水面蝶式的直接命中。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST／NCBI E-utilities，`(butterfly AND ("wave characteristics" OR "segmental velocities" OR (hip AND knee AND ankle)) AND swimming)`；以 `EXT_ID:7852446 OR EXT_ID:24149450` 取 PubMed 摘要／core record，PMCID `PMC3761458` 以出版者全文核對方法與結果。
  - 命中（2）：
    1. PMID 7852446，Sanders, Cappaert & Devlin，1995，DOI 10.1016/0021-9290(95)80002-6。
    2. PMID 24149450／PMCID PMC3761458，Barbosa et al.，2008，*Predicting the intra-cyclic variation of the velocity of the centre of mass from segmental velocities in butterfly stroke: a pilot study*，無 DOI。
  - 原文句（逐字，Abstract）：
    - Sanders et al.：
      > “phase relationships among adjacent segments suggested ... transmitted caudally”
    - Barbosa et al.：
      > “Vy during the first downbeat, Vx and Vy during the arm’s insweep”
  - 說明：Sanders et al. 用各 landmark 垂直位移的 Fourier 頻率、振幅與相位差判定波向尾側傳遞；它不把胸、髖、膝、踝切成四個離散開始事件，也沒有踝關節角。Barbosa et al. 分兩部分研究 4 名國際級泳者的漸增 200 m 與 7 名國家／國際級男性的最大 25 m；四視角作手 3D、足 2D 速度，第一／第二 downbeat 是先定義的足速相位。高速度回歸把第一 downbeat 垂直足速與 arm-insweep 手速列為質心速度變異預測項，未量胸壓、膝「蓄力」、踝角或足出水事件。
- **綜合**：原始研究支持「相鄰體表 landmark 的垂直振盪具有向尾側傳遞的相位關係」，教材也提供 head→feet 的連續波模型；但原句的四個箭頭混合了胸部空間位移、髖部空間位移／髖角、膝角與未量的踝／水面事件。肩下沉時髖可正在上升，膝屈曲又跨越 upkick→downkick 交界，因此不能把連續相位波壓成四個同類型單點。
- 裁決：**修正（第二個箭頭方向錯，第四個箭頭無量測；四個箭頭混用三種不同性質的量）**
  - **第二箭頭「髖部跟隨下壓」在空間上是反的**：SoSF `45_Figure_5.2.md:7` 直接寫「**While the shoulders are moving down, the hips are moving up.**」胸部下壓的同一時刻，髖在**上升**。原主張把它寫成「跟隨下壓」，方向錯誤。
  - **錯誤的來源是把關節角當成空間位移**：FoFS `24_Chapter_21...:26` 說「maximum hip flexion **of about 25-30 degrees** should occur shortly after the hands enter the water (**about .12 seconds later**), when the swimmer's chest is pressed downward」——胸部下壓時髖處於**最大屈曲角**，同段並說此刻肩在整個週期的最深點。髖屈曲角最大與髖在空間中上升可以同時成立，因為前者是關節角、後者是位置。原主張把「髖屈曲」讀成「髖向下」，正是第 3 批已擴充的根因 4（由可見空間量反推關節動作）的鏡像——這次是反過來把關節動作讀成空間位移。
  - **「膝屈曲蓄力」與教材同處的量測相反**：FoFS `25_Chapter_22...:73`「Once Kelsi's knees start to bend and her legs draw forward, **another major deceleration occurs**」。教材在描述膝屈曲時量到的是**減速**。「蓄力」是能量隱喻，不可寫成效益。
  - **第四箭頭「腳踝鞭動出水面」完全無量測**：三層沒有踝關節角，也沒有足部穿越水面的事件。Sanders et al. 1995 量的是各 landmark 垂直位移的 Fourier 頻率、振幅與相位差，結論是「phase relationships among adjacent segments suggested ... transmitted caudally」——**連續相位波，不是四個離散開始事件**。Barbosa et al. 2008 的第一／第二 downbeat 是**預先定義的足速相位**，不是觀察到的事件邊界。
  - **與第 3 批 BF-32 同一家族**：BF-32 被判「腿啟動身體波動」因果顛倒（實為上身→髖→足）；BF-36 是同一個波，這次錯在把它切成四個離散單點並讓其中一段反向。兩條應併為同一則體波規範。
  - 可寫入：① 蝶式的體波以相鄰體表 landmark 垂直振盪的相位差向尾側傳遞（Sanders 1995，n=8 男＋8 女菁英，Fourier 相位分析）；② 肩下沉時髖上升（SoSF `45:7`，教材）；③ 最大髖屈約 25–30°，發生在手入水後約 0.12 s、胸部下壓時，此刻肩在週期最深點（FoFS `24:26`，教材測試例，無 n 無統計）；④ 膝開始屈曲、腿前移時教材量到一次主要減速（FoFS `25:73`）。
  - 不得寫入：「髖部跟隨下壓」；「膝屈曲蓄力」（教材該處量到減速）；「腳踝鞭動出水面」（無踝角、無水面穿越量測）；不得把連續相位波寫成四個依序開始的離散動作。
  - movement 落地：①③④可作 demand，③的兩個數字（25–30°、0.12 s）**只能以定性條件式存在**並連同「教材測試例、無統計」一起寫（承第 3 批「數值一律不進 demand」）。原句的四箭頭序列整體不得落成 demand；「腳踝鞭動」段落 `evidence-gap` ＋ `do-not-prescribe`。
  - 根因：結構性 2 ＋ 結構性 4（反向形式：關節角讀成空間位移）＋ 結構性 7

## ST-09｜靜態超流線：避免腰椎過度前凸（拱腰）

- **原文主張（逐字）**：`靜態超流線：避免腰椎過度前凸（拱腰）`
- **主張拆解**：①「超流線」是 start／turn 的靜態陸上姿勢、被動水下 glide 或教材 hyperstreamline；②腰椎前凸以目視體表曲率、傾角計 T12/L1 + L5/S1，還是影像分節角；③「過度」的門檻與對照；④效益終點是 drag、glide coefficient、速度或傷害。結構性根因篩命中 **#2（過度門檻、姿勢條件與終點未定義）**、**#4（體表拱腰反推腰椎分節角）**；傷害語句另受根因 **#3** 限制，不可代替水動力終點。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'hyperstreamline|lumbar spine is arched or extended|elevation of the core|lumbar spine to extend|straighter the human body' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔（3）：`Fundamentals_of_Fast_Swimming/08_Chapter_5_Race_Club_Technology__Propulsion_Drag_Meter.md`；`Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md`；`Fundamentals_of_Fast_Swimming/26_Chapter_23_Fundamentals_and_Ten_Points_to_a_Great_Start.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Fundamentals_of_Fast_Swimming/08_Chapter_5_Race_Club_Technology__Propulsion_Drag_Meter.md:43`、`:45`：
      > “Hyperstreamline (arms behind the head) compared to streamline ... reduced drag by 11%.”
      >
      > “Elevation of the core (slight hip flexion 3-5 degrees) ... reduced frontal drag by 10%.”
    - `Fundamentals_of_Fast_Swimming/14_Chapter_11_Freestyle_Head_and_Body_Positions.md:56`、`:58`：
      > “The straighter the human body, the less the frontal drag.”
      >
      > “the gravitational force will cause the lumbar spine to extend some ... [and] elevates the core and flexes at the hip slightly ... the frontal drag force decreases”
    - `Fundamentals_of_Fast_Swimming/26_Chapter_23_Fundamentals_and_Ten_Points_to_a_Great_Start.md:198`：
      > “The lumbar spine is arched or extended in this position. All of these positional changes lead to a lowering of the drag coefficient”
  - 說明：`26_Chapter_23...` 的所指是起跳入水用 hyperstreamline 整體形狀，並把 lumbar arch 與肩臂、胸腹外形等多個改變包在一起；`08`、`14` 的所指則是核心抬高／輕微髖屈讓水平身體更直。這些教材句沒有定義「過度」前凸的角度，也沒有隔離腰椎前凸的獨立效果；因此只並列各自姿勢組合與終點，不判斷兩者是否矛盾。
- **第 2 層（本地文獻）檢索**：
  - 實跑指令：`rg -n -i -C 2 '(streamline|streamlined).{0,180}(lumbar|lordosis|hyperlordosis|hyperextension)|(lumbar|lordosis|hyperlordosis|hyperextension).{0,180}(streamline|streamlined)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔（2）：`Wanivenhaus_2012_Injuries_Prevention_Competitive_Swimmers/02_readable.md`；`Swimming_Anatomy_Lower_Back_Injuries_Narrative_Review/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號）：
    - `Wanivenhaus_2012_Injuries_Prevention_Competitive_Swimmers/02_readable.md:104`：
      > “All swimming strokes maintain hyperextension of the lower back to achieve a streamlined position”
    - `Swimming_Anatomy_Lower_Back_Injuries_Narrative_Review/02_readable.md:154`、`:168`：
      > “maintain core activation and prevent hyperlordosis and hyperextension of the spine”
      >
      > “the natural curvature of the spine can become exaggerated (hyperlordosis)”
  - 說明：兩篇均為傷害預防／敘事回顧，不是 static streamline 的拖曳實驗。前者把一定程度的下背伸展描述為流線姿勢，同時討論重複／過量負荷；後者的「prevent hyperlordosis」是預防建議。它們沒有共同前凸角度門檻，傷害機制也不能替代 drag 終點。
- **第 3 層（線上）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`(("streamlined posture" OR "streamlined position" OR glide) AND (lumbar lordosis OR body curvature) AND swimming)`；以 `EXT_ID:33821747 OR EXT_ID:39640176` 取 core record，PMCID `PMC11617340` 取 `fullTextXML` 的 Methods／Results。
  - 命中（2）：
    1. PMID 33821747，Papic et al.，2024（2021 online），*Augmented feedback can change body shape to improve glide efficiency in swimming*，DOI 10.1080/14763141.2021.1900355。
    2. PMID 39640176／PMCID PMC11617340，Sawada et al.，2024，*Effect of Shoulder Flexion Range of Motion and Trunk Muscle Activity on Lumbar Lordosis in the Streamlined Posture in Healthy Young Men*，DOI 10.7759/cureus.72958。
  - 原文句（逐字，Abstract）：
    - Papic et al.：
      > “Significant changes to form gradients were related to reductions in lumbar lordosis”
    - Sawada et al.：
      > “lumbar lordosis angle ... had a significant negative correlation with ... IO/TrA”
  - 說明：Papic et al. 對 11 名國家級男女泳者作 feedback 前後 glide；以膝、髖、肩二維 landmark、手描 torso 橫／矢徑與 form gradient 計 glide factor、glide coefficient、速度。介入後三個 glide 終點改善，體表形狀改變與 lumbar-lordosis／胸部凸度降低相關；非隨機對照，摘要也沒有給「過度」角度門檻。Sawada et al. 對 31 名健康年輕男性在陸上站姿與 streamline，以兩個 inclinometer 量 T12/L1、L5/S1 後相加為 lordosis angle，另量骨盆傾角與 EMG；沒有在水中量 drag。這是直接腰椎角量測，不應與目視拱腰或 torso form gradient 混成同一量。
- **綜合**：第 3 層同時提供水中 glide 外形／表現介入與陸上 streamline 腰椎角／肌電關聯：降低體表曲率相關的 lumbar-lordosis 成分與 glide 指標改善並存，而腰椎前凸又受肩屈 ROM、站姿角與軀幹肌活動影響。第 1 層的 hyperstreamline 整體姿勢包含一定 lumbar extension，另一教材策略則用核心抬高／輕髖屈讓身體更直；兩者所指與姿勢組合不同。三層仍未定義何角度算「過度」，也不能用傷害回顧替代水動力閾值。
- 裁決：**修正（終點錯掛：這是傷害預防建議，卻掛在水動力標題下；且與 hyperstreamline 的定義直接扞格）**
  - **最低阻力姿勢本身就是拱腰的**：FoFS `26_Chapter_23...:198` 描述 hyperstreamline 時明寫「**The lumbar spine is arched or extended in this position.** All of these positional changes lead to a lowering of the drag coefficient of the human body.」原主張的標題是「靜態超流線」，內容卻是「避免拱腰」——**在同一個姿勢名稱下，教材說拱、主張說不要拱**。
  - **但這不是矛盾，過根因 8 三問即可拆開**：① 同一相位／情境嗎？教材講的是起跳入水的 hyperstreamline（手臂在頭後、下巴貼胸、肩前拉、腹腔內縮）；主張若指一般水平 streamline，姿勢組合根本不同。② 同一個量嗎？**否**——教材終點是 drag coefficient，兩篇第 2 層回顧的終點是**傷害**，Papic 的終點是 glide factor／coefficient／速度，Sawada 的終點是腰椎傾角與 EMG（陸上、無 drag）。四個不同終點。③ 各自有方法可核嗎？FoFS 是 Race Club PDM 敘述無 n 無統計；Papic n=11 前後測無對照；Sawada n=31 陸上；兩篇 L2 是敘事回顧。**第二問為否，所以不是型 5 學界分歧，是終點錯掛。**
  - **教材另有第三處說拱腰是功能需求**：FoFS `24_Chapter_21...:20`（蝶式）「To gain propulsion from the arms during the pull, **the lumbar spine must extend (arch)** and the shoulders must elevate」。加上 `14_Chapter_11...:58`「when the human body is horizontal and relaxed, the gravitational force will cause the lumbar spine to extend some」——教材立場是：腰椎伸展在水中是**常態且部分是功能需求**，該修的是核心抬高與輕微髖屈，不是「不要拱」。
  - **「過度」沒有任何門檻**：三層沒有一筆給出角度閾值。缺了門檻，「避免過度」在資料層是不可操作的。
  - **兩個水中／陸上量不可混**：Papic et al. 2024（n=11 國家級，膝／髖／肩二維 landmark ＋ 手描 torso 橫／矢徑算 form gradient）的 lumbar lordosis 是**由體表外形推的**（根因 4）；Sawada et al. 2024（n=31，兩個傾角計量 T12/L1 ＋ L5/S1 相加）是**唯一真正的腰椎分節角量測**，但在陸上站姿與 streamline、沒有 drag。這兩個「lumbar lordosis」不是同一個量。
  - 可寫入（三條分開，各帶終點）：① hyperstreamline 姿勢包含腰椎伸展，教材歸為最低阻力係數姿勢（FoFS `26:198`，教材 PDM 敘述，無 n 無統計）；② 水中 glide 介入後體表外形改變（含 lumbar lordosis 成分下降）與三個 glide 表現指標改善相關（Papic 2024，n=11，前後測**無對照組**，lordosis 由體表 form gradient 推得）；③ 陸上 streamline 姿勢的腰椎前凸角與 IO/TrA 活動呈負相關並受肩屈 ROM 影響（Sawada 2024，n=31，**陸上、無 drag 終點**）；④ 傷害預防回顧建議維持核心活化以避免 hyperlordosis（Wanivenhaus 2012、Swimming Anatomy 2024 敘事回顧，**傷害終點**）。
  - 不得寫入：「過度」的任何角度門檻（三層皆無）；不得用④支持①②③的水動力結論（根因 3）；不得把 Papic 的體表 form gradient 與 Sawada 的分節傾角當同一個量；不得把「避免拱腰」寫成 streamline 的水動力規範。
  - movement 落地：**「避免拱腰」不得落成 static-streamline 的 demand**——水動力終點不支持，教材甚至反向。可落成 intervention 的 rationale，但 `evidence_profile` 須標敘事回顧等級、終點欄標 injury-prevention，且與水動力 demand 分屬不同條目不得互相引用。①②③各自作 demand 並帶量測條件欄。
  - 根因：結構性 2（「過度」無門檻）＋ 結構性 3（傷害終點冒充水動力終點）＋ 結構性 4 ＋ 結構性 8

---

# 裁決總表（第 4 批 spine-neck／軀幹旋轉，12 條）

| ID | 裁決 | 一句話理由 | 命中根因 |
|---|---|---|---|
| FR-10 | 修正 | 「同側」無座標定義故不可判真假；峰值在 entry→pull 交界，非整段前伸期 | 2、4、7 |
| FR-30 | 修正 | 「肩帶動核心」被推翻：roll 的主要生成源量測為浮力矩，軀幹肌 EMG 落後 400–775 ms | 2、4、**10** |
| FR-31 | 修正 | 一句綁「划距」與「力量傳導」兩個未證效益；唯一量化證據是手速 28%／19% | 1、2、4 |
| FR-33 | 修正 | 「同步」被三筆資料否定（0.2–0.3 s 時差、+16° vs +5°、群組無一致模式） | 2、4、7、8 |
| FR-43 | 修正 | 括號因果鏈無量測；教材自己把髖下沉歸給核心放鬆與手足升力 | 2、3、4、**10** |
| FR-44 | 需補條件 | 方向對但暴露量錯層（無頸椎角量測）；效果量隨手臂姿勢差兩倍以上 | 2、4 |
| BR-40 | 修正 | 「沒有」被個案三維量測推翻（非刻意≠零）；「核心波動」為未溯源自造詞 | 2、4、5 |
| BR-42 | 修正 | 「肩胛帶上提」無量測；教材明說上身是被手臂抬起的；三事件壓成一點 | 4、5、7、**10** |
| BR-43 | 修正 | 「呼氣時」這個時序錨點本身從未被量過；四事件綁一句；三個流線名詞混用 | 2、5、7、8 |
| BF-35 | 修正 | 教材原文是「左右力矩互消」的條件式推導，條件在轉寫時被刪掉 | 2、4 |
| BF-36 | 修正 | 第二箭頭方向錯（肩下沉時髖上升）；「蓄力」處教材量到減速；踝段無量測 | 2、4、7 |
| ST-09 | 修正 | 傷害預防終點掛在水動力標題下；教材三處說腰椎伸展是常態或功能需求 | 2、3、4、8 |

**12 條全部需要修改，零條原封不動通過**（與第 3 批 hip-knee 相同）。其中 FR-44 為「需補條件」（主張方向成立，須改暴露量並補量測條件），其餘 11 條為「修正」。

## 三項實質發現

1. **「肩帶動核心」不成立，而且錯得有結構**（FR-30）。Yanai 2004 以全身角動量與慣性矩積分，直接把 body roll 的主要生成來源量到**浮力矩**；Andersen 2023 測得軀幹肌 EMG 與 torso twist 的峰值互相關落後 **400–775 ms**，作者歸為穩定／姿勢控制。也就是說 roll 的動力來源在**身體之外**，而軀幹肌是在後面追著穩定。原主張把兩個共存的體表運動學用「帶動」串成近端驅動遠端，漏掉了唯一被量到的力學來源。同型錯誤在本批出現三次（FR-30、FR-43 括號鏈、BR-42「隨肩胛帶上提」），足以立為新根因。

2. **「零值宣稱」是本分區的系統性措辭風險**（BR-40、BF-35）。兩條都把「非主要技術機制」寫成「沒有」。BR-40 的 Sanders 2015 個案原文是「rotate about their longitudinal axis ... **albeit not deliberately**」；BF-35 的 SoSF 原文是「no body roll occurs ... **if** the hands produce similar force ... torques ... cancel out」——後者根本是條件句，條件在轉寫時被刪掉。兩條合併成一則規範：**canonical 不得出現「沒有／零」的絕對運動學宣稱**。

3. **根因 8 三問在本批四次全部擋下假分歧，零次判為型 5**。本批出現四組「說法不同」——FR-31（教材說 roll 助流線 vs PDM 量到側身多 1.8% 阻力）、FR-33（0.2–0.3 s 時差 vs Ogata 無顯著差異）、BR-43（fast vs delayed recovery）、ST-09（避免拱腰 vs hyperstreamline 本身就是拱的）——**沒有任何一組是真正的學界分歧**，全部是不同量、不同終點或不同策略。這把第 3 批 BR-30 的教訓推到一般結論：**「來源說法不同」的預設判定應該是「不同所指」，要標成學界分歧必須舉證。**

## 結構性根因（延續第 1–3 批編號）

- **10（新增）把體節間共變寫成近端驅動遠端，漏掉外力項**：徵狀是「A 帶動 B」「A 驅動 B」句，其中 A、B 都只是體表運動學共變，而真正的生成源是**身體外部的力矩**（浮力矩、手臂水動力）或**未被指名的第三方**（核心張力、手足升力）。這在水中特別致命——陸上直覺是「肌肉產生動作」，水中的主導生成源常常不是。與根因 9（因果方向顛倒）的差別：9 是 A→B 寫成 B→A，10 是 C→(A,B) 寫成 A→B，屬於典型混淆變項。
  → **判準三問**：這個運動有沒有可能是外力矩產生的？有沒有量到肌肉活動、而且時序對得上？**原作者自己怎麼歸因？**（本批三次全部是作者或教材已經寫明了另一個機制，只是轉寫時被換掉。）
- **2（擴充）零值與絕對宣稱**：原定義是「量化／比較缺對照或座標定義」。BR-40 與 BF-35 顯示另一個高頻形式是**把「非主要機制」寫成「量測為零」**，以及**把條件句轉寫成無條件斷言**。治本是措辭規範，不是逐條補資料。
- **4（再擴充）反向形式：把關節動作讀成空間位移**：第 3 批已把 4 擴充為「由可見空間量反推關節動作」。BF-36 顯示它有對稱的反向錯誤——FoFS 說「胸部下壓時最大**髖屈曲角** 25–30°」，被讀成「髖部向下移動」，而同一時刻 SoSF 明寫髖在**上升**。**關節角與空間位移在同一時刻可以方向相反**，這是本庫第一次抓到這個方向的錯誤。

## 對後續批次的操作指示

- 根因 **10** 預期在所有含「帶動／驅動／啟動／連動」的主張高頻，尤其動力鏈類。**逐條回原文看作者自己的歸因**是成本最低的檢查——本批三次全部靠這一步抓到。
- 根因 **2（擴充）**：凡出現「沒有／不會／零／完全」等絕對詞，一律回原文檢查是否為條件句或「非主要機制」。
- 根因 **4（再擴充）**：凡主張同時提到「某關節屈曲／伸展」與「某部位上下移動」，必須確認兩者是同一個量還是兩個量，並確認方向。
- **跨層去重**：FR-43 出現同一研究（PMID 37830674 Rinonapoli 2023 ＝ 第 2 層 Masters 篇）在第 2、3 層各算一次。codex 本次自行標出，但派工規格應加為驗收條款：**同一 PMID／同一研究不得跨層重複計數。**

## 對 W4（Step 17–18）的直接輸入

- **可直接產出 demand**：FR-31 的上軀幹旋轉對手後向速度貢獻（Kudo 2021，28%／19%，本批唯一有數字的推進機制證據）；FR-44 的頭位—被動阻力（Cortesi & Gatta 2015，須帶手臂姿勢條件）；BR-43 的 arm-pull 結束至 leg-kick 開始間隔（Oxford 2017，n=26）；BF-36 的體波尾側傳遞相位關係（Sanders 1995）；FR-10 的肩線 roll 峰值時點（Gonjo 2021）。
- **可產出 intervention rationale（教材反向指導，價值高）**：BR-42 的「上身是被手臂抬起的，不要主動抬頭或拱背」（SoSF `42:31`）——這是教材主動給出的**否定式指導**，比正面描述更適合落成 intervention。
- **明確不得落成 demand／intervention**：FR-30 的「肩帶動核心」；FR-31 的「划距」與「力量傳導」；FR-33 的「同步」；FR-43 的括號因果鏈；BR-42 的「肩胛帶上提」；BR-43 的「呼氣時」時序框架；BF-36 的「腳踝鞭動出水面」與「膝屈曲蓄力」；ST-09 的「避免拱腰」作為水動力規範。以上一律 `evidence-gap` ＋ `action_status: do-not-prescribe` ＋ `dosage_source_ids` 留空（W016）。
- **新增欄位需求（本批第二個，承第 3 批「觀察參考系」）**：demand 若引用阻力／效果百分比，必須帶**「量測條件」欄**（手臂姿勢／速度／水深／被動或主動）。依據是 FR-44：同一個頭位操弄，手臂體側時 4–5.2%、雙臂過頭時 10.4–10.9%，差距超過兩倍。與「觀察參考系」欄一併在 Step 21 評估。
- **措辭規範（跨條目）**：canonical 不得出現「沒有／零」的絕對運動學宣稱；不得出現未附正負向與參考系的「同側／對側」；`body line`／`racing streamline`／`hyperstreamline` 三詞不得互換；「核心波動」若保留須先登錄 taxonomy 並標為本專案自造詞。
- **相位模型**：本批蛙式條目跨 SoSF（outsweep／inward sweep）與 FoFS（lift／propulsion 四相位）兩套分期，蝶式亦然。凡引用一律綁 `phase_model`（W017），同一條目內不得混用兩套。
- **與第 3 批併案**：BF-36 與第 3 批 BF-32 是同一個蝶式體波的兩種錯誤寫法（前者切成四個離散單點且方向反了，後者因果顛倒），建議在 W4 併為同一則體波規範條目。
