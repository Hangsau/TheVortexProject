# C 類 shoulder-arm 證據包

- **生成日期**：2026-08-29（Asia/Taipei）
- **範圍**：14 條 C 類游泳專屬時序／推進主張；順序依本批指定，BK-26 置首。
- **第 1 層**：`C:\claudehome\resources\books\Science_of_Swimming_Faster\`（234 檔）與 `C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\`（34 檔）。
- **第 2 層**：`C:\claudehome\resources\books\swimming-kinetic-chain\`（43 篇）。已知覆蓋缺口為蛙式、蝶式、踝、body roll 各 0 篇；因此 BR-06、BR-18、BF-05、BF-09、BF-22、BF-25 在本層查無時不作推論。
- **第 3 層**：Europe PMC REST 與 NCBI E-utilities；先以主題查詢篩選，再以 `resultType=core`、`fullTextXML` 或 PubMed `efetch` 取摘要／全文段落。
- **讀法**：引文與其後的說明分開；「掌心／拇指朝向」只記為空間朝向，除非研究實際量測前臂，否則不轉寫成旋前／旋後。教材中的效益語句也不等同於有成績或效率終點的研究。

## BK-26｜「第一下掃/第一上掃/第二下掃/第二上掃」四段式分期命名

- **原文主張（逐字）**：`「第一下掃/第一上掃/第二下掃/第二上掃」四段式分期命名`；⚠︎ 註記（逐字）：`BK-26：自我驗證段已自承此分期採自單一教學網站，屬「其中一種常見拆法」而非標準；屬型 5（命名慣例分歧），保留並標明流派來源。`
- **主張拆解**：① 四個 sweep 名稱是否見於游泳文獻；② 這四段是否就是完整週期；③ 文獻是否並存其他分期名稱／段數。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'first downsweep|first upsweep|second downsweep|second upsweep|six phases of the backstroke|backstroke pulling cycle' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/17_Chapter_14_The_Six_Phases_of_the_Backstroke_Pulling_Cycle.md`；`Science_of_Swimming_Faster/36_Chapter_3__Backstroke_Technique.md`、`37_Figure_3.1.md`、`38_Figure_3.2.md`、`39_Figure_3.3.md`、`40_Figure_3.4.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `17_Chapter_14_The_Six_Phases_of_the_Backstroke_Pulling_Cycle.md:22`（The Six Phases）：
      > “We classify the backstroke pulling cycle with the same six phases we use in the freestyle cycle: lift, front-quadrant propulsion, back-quadrant propulsion, release, early recovery and late recovery.”
    - `Science_of_Swimming_Faster/36_Chapter_3__Backstroke_Technique.md:48`、`38_Figure_3.2.md:17`、`39_Figure_3.3.md:15`、`40_Figure_3.4.md:13` 另以 **Catch / Midpull Mechanics / Finish / Rotation** 為章節骨架，並另述 recovery；這不是四個 sweep 的同一套詞彙。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'backstroke.{0,100}(phase|cycle)|phase.{0,100}backstroke|downsweep|upsweep' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無命中。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`backstroke AND ("first down sweep" OR "first downsweep" OR "six phases")`（`pageSize=5`）；對 PMCID 以 `.../PMC9180488/fullTextXML` 讀 Methods；另以 `EXT_ID:18409098` 取 PubMed 摘要。
  - 命中：PMID 35682325／PMCID PMC9180488，*Velocity Variability and Performance in Backstroke in Elite and Good-Level Swimmers*，Fernandes et al.，2022，*International Journal of Environmental Research and Public Health*，DOI 10.3390/ijerph19116744；PMID 18409098，*Arm coordination in elite backstroke swimmers*，Chollet, Seifert & Carter，2008，*Journal of Sports Sciences*，DOI 10.1080/02640410701787791。
  - 原文句（逐字，含所在段落標題）：
    - Fernandes et al.，Methods—Video Analysis（省略各段中間的邊界敘述，但保留原名）：
      > “(i) first down sweep … (ii) first up sweep … (iii) second down sweep … (iv) second up sweep … (v) recovery”
    - Chollet et al.，Abstract：
      > “The six phases of the arm stroke were identified by video analysis...”
- **找到的證據屬哪一層級**：直接量測的游泳運動學研究 + 游泳教材模型。
- **是否直接回答原主張**：是；四個 sweep 名稱確實被研究用來編碼影像，但該研究把 recovery 列為第 5 相；另有六相研究與六相教材體系，段數／名稱並不唯一。
- **樣本與外推邊界**：Fernandes et al. 為 16 名 elite（12 女）與 15 名 good-level（7 女），室內 25 m 池、最大強度 25 m、矢狀面 120 Hz、共 196 週期；Chollet et al. 為 14 名 elite 男子，4 × 25 m，速度對應 400／200／100／50 m。這些分相是研究操作定義，不是跨文獻命名共識調查。
- **缺口**：沒有找到把「四個 sweep」宣告為完整週期且排除 recovery 的標準文件；也沒有分期命名的共識研究。
- 裁決：

## FR-09｜前伸滑行期：肩胛骨前伸可「增加划距」

- **原文主張（逐字）**：前伸滑行期：肩胛骨前伸可「增加划距」
- **主張拆解**：① 前伸滑行期是否實際出現肩胛骨前伸；② 前伸是否讓手的幾何可及距離增加；③ 是否使 stroke length、速度或效率增加。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'scapul(ar|a)|protract|reach farther|reach forward|stroke length|distance per stroke' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/20_Figure_2.2.md`、`29_Shoulder_and_Hip_Roll.md`；未命中「肩胛前伸增加划距」的直接句。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `20_Figure_2.2.md:17`：
      > “But when the body is rolled to the side, the hand can naturally reach comfortably forward without causing this misalignment.”
    - `29_Shoulder_and_Hip_Roll.md:7`：
      > “an increase in duration of the entry phase, longer stroke length, and reduced stroke frequency have been related to better economy in distance swimming”
    - 前一句把 reach 歸於 body roll；後一句是 entry duration、stroke length、stroke frequency 與 economy 的組合關係，兩句都沒有把效果歸於肩胛前伸。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'scapul(ar|a).{0,100}(protract|reach|stroke length)|protract.{0,100}(reach|stroke length)|stroke length' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Tovin_2006_Prevention_Treatment_Swimmers_Shoulder/02_readable.md`；`Wanivenhaus_2012_Injuries_Prevention_Competitive_Swimmers/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `Tovin_2006.../02_readable.md:34`：
      > “During the pull-through phase, the scapula is protracted while the humerus is adducted, extended, and internally rotated.”
    - `Wanivenhaus_2012.../02_readable.md:108`：
      > “The correct stroke pattern should be accompanied by correct body roll to reduce the scapular protraction needed to maintain proper alignment of the glenohumeral joint.”
    - 兩處分別談 pull-through 與傷害力學；不是前伸滑行期的 reach 或 stroke-length 終點。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" OR freestyle) AND scapula* AND (protraction OR "stroke length" OR reach)`；再以 `DOI:"10.1080/14763141.2019.1640277" OR TITLE:"Critical scapula motions for preventing subacromial impingement in fully-tethered front-crawl swimming"` 精煉，`resultType=core` 取摘要。
  - 命中：PMID 31355716，*Critical scapula motions for preventing subacromial impingement in fully-tethered front-crawl swimming*，Du & Yanai，2022（2019 online），*Sports Biomechanics*，DOI 10.1080/14763141.2019.1640277。
  - 原文句（逐字，含所在段落標題）：
    - Abstract：
      > “The aims were to quantitatively describe the coordinated motions of the scapula and humerus during fully tethered front-crawl strokes...”
    - 該研究終點為疑似肩峰下壓迫姿態所占週期時間，未量 reach、stroke length、速度或效率。
- **找到的證據屬哪一層級**：直接量測的游泳肩胛運動學研究 + 游泳教材模型；原主張的效益鏈本身無。
- **是否直接回答原主張**：否；三層分別談到 body roll 與 reach、拉水期肩胛前伸、肩胛運動與夾擠，但沒有把「前伸滑行期肩胛前伸」連到「划距增加」，更沒有成績／效率終點。
- **樣本與外推邊界**：Du & Yanai 為 17 名大學游泳選手、dominant side 電磁追蹤、fully tethered front crawl；不能直接外推自由游、划距或比賽成績。教材未交代可重現樣本與 protocol。
- **缺口**：「肩胛前伸 → 手前伸距離／stroke length → 速度或效率」三段關係皆未被本次三層來源直接量測；此核心關係為三層皆無。
- 裁決：

## FR-13｜抓水期：腕伸直或輕度屈曲，形成「划槳面」

- **原文主張（逐字）**：抓水期：腕伸直或輕度屈曲，形成「划槳面」
- **主張拆解**：① 抓水／早期推進的腕角度；② 手與前臂是否作為固定單元；③ 此配置是否提高有效面積或推進。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'wrist|paddle|surface area of the hand and forearm|palm.{0,30}(back|down)' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/10_Chapter_7_The_Six_Phases_of_the_Freestyle_Pulling_Cycle.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `10_Chapter_7...md:61`：
      > “We do so by initially keeping the arm straight with the wrist and the hand in alignment with the forearm, all of which are pointing forward.”
    - `10_Chapter_7...md:89`：
      > “During the early propulsion, it is correct to think of the hand and forearm as being a single unit, connected by a stiffened wrist.”
    - 這是教材姿勢模型；第二句談 early propulsion，並非量測「划槳面」的水動力實驗。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'front crawl.{0,120}(wrist|palm|hand surface)|wrist.{0,100}(front crawl|freestyle)|paddle' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Biomechanics_of_Competitive_Swimming_Book_Chapter/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `02_readable.md:268`：
      > “Caty et al. (2007) found an important stabilization of the wrist and high antagonist flexor and extensor carpi activity during the insweep phase.”
    - 此為書章對研究的二手摘要；沒有給中立／輕屈的角度值。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`("front crawl" OR freestyle) AND wrist AND (stabilization OR flexion OR extension)`；再以 `EXT_ID:16677829 OR TITLE:"Wrist stabilisation and forearm muscle coactivation during freestyle swimming"` 精煉並以 `resultType=core` 取摘要。
  - 命中：PMID 16677829，*Wrist stabilisation and forearm muscle coactivation during freestyle swimming*，Caty et al.，2007，*Journal of Electromyography and Kinesiology*，DOI 10.1016/j.jelekin.2006.02.005。
  - 原文句（逐字，含所在段落標題）：
    - Abstract：
      > “Important stabilisation of the wrist and high antagonist muscle activity were observed during the insweep phase...”
- **找到的證據屬哪一層級**：直接量測的游泳 EMG／腕矢狀面運動學研究 + 游泳教材模型。
- **是否直接回答原主張**：只回答部分；教材直接描述 wrist-hand-forearm 對齊與 stiffened unit，研究直接觀察 insweep 的腕穩定，但沒有證明抓水期可在「伸直或輕屈」兩者擇一，也未以力或效率終點驗證「划槳面」。
- **樣本與外推邊界**：Caty et al. 為 7 名男性國際級選手，最大 semi-tethered power test；EMG 為 FCU／ECU，影片只取腕矢狀面角度，分 insweep／outsweep。不能直接外推一般自由游抓水或三維掌面角度。
- **缺口**：抓水瞬間的三維腕角度分布；輕度屈曲與中立的比較；有效掌面面積、手部推力或效率的直接比較。
- 裁決：

## FR-17｜拉水期：肘部保持高於手掌（High Elbow）

- **原文主張（逐字）**：拉水期：肘部保持高於手掌（High Elbow）
- **主張拆解**：① 拉水期是否有可操作化的 high-elbow 姿勢；② 「肘高於手掌」是否就是研究定義；③ 與速度／阻力的關係是否為因果。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'high elbow|elbow.{0,40}(hand|palm)|early vertical forearm|vertical forearm' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/10_Chapter_7_The_Six_Phases_of_the_Freestyle_Pulling_Cycle.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `10_Chapter_7...md:59`：
      > “Using a high-elbow pulling motion has the effect of keeping the upper part of the arm, which is the largest part, out of harm’s way.”
    - `10_Chapter_7...md:87`：
      > “Notice the very high elbow to reduce frontal drag from the upper arm (VM technology).”
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'high[- ]elbow|early vertical forearm|vertical forearm|elbow.{0,60}(hand|wrist|palm)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Heinlein_2010_Biomechanical_Considerations_Competitive_Swimmers_Shoulder/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `02_readable.md:36`：
      > “During early pull-through, the elbow remains high, toward the surface of the water...”
    - 同段把 early pull-through 定為 glide 結束至肱骨約在身體前方 90° 的區間。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`"front crawl" AND "high elbow"`；以 `EXT_ID:27540768`、`resultType=core` 取摘要。
  - 命中：PMID 27540768，*A quantitative evaluation of the high elbow technique in front crawl*，Suito, Nunome & Ikegami，2017，*Journal of Sports Sciences*，DOI 10.1080/02640414.2016.1221517。
  - 原文句（逐字，含所在段落標題）：
    - Abstract：
      > “Many coaches often instruct swimmers to keep the elbow in a high position ... during ... the pull phase in front crawl...”
- **找到的證據屬哪一層級**：直接量測的三維游泳運動學研究 + 游泳教材模型。
- **是否直接回答原主張**：是；研究以肩、肘、腕三維座標建立 high-elbow index，且明定在 pull phase 評估。原句「肘高於手掌」是簡化語句，研究實際採三關節座標指標，不只看垂直高度。
- **樣本與外推邊界**：16 名 highly skilled 與 6 名 novice 男性，最大努力 25 m front crawl，60 Hz 三維攝影；high-elbow index 與 pull-phase 速度為相關，不是姿勢介入的因果試驗，亦未納入女性或長距離 protocol。
- **缺口**：沒有隨機／交叉技術介入證明保持 high elbow 本身提高速度；「高於手掌」與正式 high-elbow index 的換算門檻未在原主張中定義。
- 裁決：

## BK-10｜入水位置對肩壓力影響大，是仰式肩傷好發位置

- **原文主張（逐字）**：入水位置對肩壓力影響大，是仰式肩傷好發位置
- **主張拆解**：① 入水／抓水姿勢是否增加特定肩部結構負荷；② 該位置是否有傷害發生率、盛行率或風險倍數；③ 「好發位置」是症狀時點、組織負荷，還是流行病學頻率。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'backstroke.{0,80}(injur|shoulder)|entry.{0,80}(injur|shoulder|stress|pressure)|mechanics and injury risk' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/38_Figure_3.2.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `38_Figure_3.2.md:13`：
      > “If the swimmer identifies the first half of the underwater arm stroke, specifically the catch, as the part that hurts, then the pain is likely arising because the arm is too far behind the back and outside the scapular plane.”
    - `38_Figure_3.2.md:15`：
      > “Most of the time, the cause of the pain is that the swimmer drives the arm too deep on the initial hand entry and catch...”
    - 這是教材的症狀／技術診斷語句，未附發生率研究或比較組。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'backstroke.{0,160}(entry|catch).{0,160}(pain|injur|risk|stress|pressure)|shoulder.{0,160}backstroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Tovin_2006_Prevention_Treatment_Swimmers_Shoulder/02_readable.md`；`Wanivenhaus_2012_Injuries_Prevention_Competitive_Swimmers/02_readable.md`；`McKenzie_2023_Shoulder_Risk_Factors_Competitive_Swimmers_Systematic_Review/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `Tovin_2006.../02_readable.md:38`：
      > “This position places increased stress on the anterior capsule.”
    - `Wanivenhaus_2012.../02_readable.md:60`：
      > “Backstroke swimmers generally experience isolated anterior glenohumeral instability due to the position of the arm in overhead elevation and external rotation at hand entry.”
    - `McKenzie_2023.../02_readable.md:40`（Abstract）：
      > “There was no strong evidence supporting or refuting the association between 80 assessed variables and shoulder injury or pain.”
    - 前兩篇是臨床敘述／敘事綜述；系統性回顧未列出「仰式入水位置」的風險估計。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`backstroke AND shoulder AND (entry OR catch) AND (injury OR pain OR risk)`；再以 `EXT_ID:37515375 OR TITLE:"Shoulder pain and injury risk factors in competitive swimmers"` 精煉，PubMed／Europe PMC 摘要核對。
  - 命中：PMID 37515375，*Shoulder pain and injury risk factors in competitive swimmers: A systematic review*，McKenzie et al.，2023，*Scandinavian Journal of Medicine & Science in Sports*，DOI 10.1111/sms.14454；主題查詢沒有命中以仰式入水／抓水位置為暴露、以傷害為終點的一手隊列或病例對照研究。
  - 原文句（逐字，含所在段落標題）：
    - Abstract—Results：
      > “specialty stroke ... had moderate evidence opposing an association.”
- **找到的證據屬哪一層級**：游泳教材模型 + 運動醫學敘事綜述 + 傷害風險系統性回顧；無仰式入水位置的一手流行病學估計。
- **是否直接回答原主張**：只回答部分；有 anterior capsule stress、overhead elevation/external rotation 與入水／抓水疼痛的負荷描述；沒有回答「好發」所需的發生率、盛行率、相對風險或傷害事件時點。
- **樣本與外推邊界**：McKenzie et al. 納入 22 篇競技游泳研究，最高品質單篇 n=201；泳式專項與傷害的方向未指向仰式，且沒有 backstroke-entry exposure。教材與敘事綜述沒有可重現的入水深度分組或傷害追蹤 protocol。
- **缺口**：仰式入水／抓水位置特異的傷害頻率、風險倍數與前瞻性暴露資料三層皆無；現有資料只有負荷／疼痛位置描述。
- 裁決：

## BK-17｜抓水期：腕伸直，掌心朝下後方形成划水面

- **原文主張（逐字）**：抓水期：腕伸直，掌心朝下後方形成划水面
- **主張拆解**：① 抓水腕位；② 掌心的空間朝向；③ 手／前臂形成划水面的描述。掌心朝向不反推前臂旋轉。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'wrist|palm.{0,40}(feet|back|down)|surface area of the hand and forearm' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/37_Figure_3.1.md`、`39_Figure_3.3.md`；`Fundamentals_of_Fast_Swimming/17_Chapter_14_The_Six_Phases_of_the_Backstroke_Pulling_Cycle.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `37_Figure_3.1.md:7`：
      > “The first movement is to bend at the wrist so that the fingertips point to the side and the palm faces back.”
    - `37_Figure_3.1.md:16`：
      > “the palm should never be pitched downward to face the bottom of the pool during the initial part of the stroke.”
    - `17_Chapter_14...md:46`：
      > “It transitions quickly from the palm facing to the side with the pinky down to pointing the fingers directly to the side with the wrist slightly flexed...”
    - `39_Figure_3.3.md:7` 把 hand and forearm together描述為最大化 pulling surface；上述兩本教材都描述輕屈／屈腕與掌心向側後方，不是「腕伸直、掌心朝池底」。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'backstroke.{0,120}(wrist|palm|hand orientation)|palm.{0,100}backstroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Heinlein_2010_Biomechanical_Considerations_Competitive_Swimmers_Shoulder/02_readable.md`（只命中 finish，不是 catch）。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `02_readable.md:72`：
      > “The arm continues pushing down toward the feet, finishing the stroke with wrist flexion...”
    - 抓水期腕位與掌心朝向無直接命中。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`backstroke AND (wrist OR palm OR "hand orientation")`（105 筆）；再篩 `backstroke systematic review`、`hand orientation`、`wrist` 全文／摘要。
  - 命中：主題篩選命中 PMID 40483624／PMCID PMC12146239（González-Ravé et al., 2025，backstroke performance 系統性回顧）及 PMID 35682325／PMCID PMC9180488（Fernandes et al., 2022），但兩者都未報告抓水腕角或掌心朝向；無可直接回答命中。
  - 原文句（逐字，含所在段落標題）：無（命中研究只量週期、速度、roll 或腕點速度，未量腕關節角／掌面法向量）。
- **找到的證據屬哪一層級**：游泳教材模型；第 2／3 層無抓水腕位／掌向的一手量測。
- **是否直接回答原主張**：是（限第 1 層教材對姿勢的直接描述）；教材直接說明腕與掌心朝向，且其描述為 wrist bent/slightly flexed、palm lateral→back。這是掌心空間朝向，不等同前臂旋前／旋後。
- **樣本與外推邊界**：教材未提供樣本數、性別、速度 protocol 或腕角測量方法；線上命中研究沒有相應變項。因此只能識別教材模型，不能估計競技選手的實際角度分布。
- **缺口**：仰式抓水期三維腕角、掌面法向量、手＋前臂有效面積與推力的同步量測。
- 裁決：

## BK-21｜第二下掃：肩持續伸展，手掌路徑再度向下

- **原文主張（逐字）**：第二下掃：肩持續伸展，手掌路徑再度向下
- **主張拆解**：① second down sweep 的時間邊界；② 手掌／手的向下路徑；③ 肩盂肱關節是否持續伸展。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'second downsweep|downward finish|finish.{0,80}(down|hand)|hand.{0,50}downward' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/39_Figure_3.3.md`；`Fundamentals_of_Fast_Swimming/17_Chapter_14_The_Six_Phases_of_the_Backstroke_Pulling_Cycle.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `39_Figure_3.3.md:17`：
      > “At that point, the hand should start to pitch downward and inward while pushing water in those directions.”
    - `17_Chapter_14...md:128`：
      > “Finish with a quick downward turn of the hand, but don’t let the hand finish too deep.”
    - 兩本教材把向下動作放在 finish；沒有在同句量化肩伸展。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'second downsweep|downward finish|backstroke.{0,100}(hand path|downward|finish)' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Heinlein_2010_Biomechanical_Considerations_Competitive_Swimmers_Shoulder/02_readable.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `02_readable.md:72`：
      > “The arm continues pushing down toward the feet, finishing the stroke with wrist flexion, as if dribbling a basketball next to the hip.”
    - 這是綜述的技術敘述，沒有關節角時間序列。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`backstroke AND "second down sweep"`；以 `.../PMC9180488/fullTextXML` 讀 Methods—Video Analysis。
  - 命中：PMID 35682325／PMCID PMC9180488，Fernandes et al.，2022，*Velocity Variability and Performance in Backstroke in Elite and Good-Level Swimmers*，*IJERPH*，DOI 10.3390/ijerph19116744。
  - 原文句（逐字，含所在段落標題）：
    - Methods—Video Analysis：
      > “second down sweep, from the hand below the shoulder to the end of its backward movement”
- **找到的證據屬哪一層級**：直接量測的游泳運動學研究（相位邊界）+ 游泳教材／臨床綜述模型（路徑）。
- **是否直接回答原主張**：只回答部分；研究直接定義 second down sweep，教材與綜述直接描述末段向下路徑；沒有同步量測肩關節角，因此「肩持續伸展」未被直接回答。
- **樣本與外推邊界**：Fernandes et al. 為 31 名 elite／good-level 選手、最大 25 m、矢狀面 120 Hz；相位由手與肘視覺辨識，未建立肩盂肱三維角度。教材／綜述沒有 protocol。
- **缺口**：second down sweep 期間的三維肩伸展角度與速度；「掌心」而非手部標記的實際向下軌跡。
- 裁決：

## BK-29｜拉水過程延遲旋轉，推水末段才快速轉向另一側

- **原文主張（逐字）**：拉水過程延遲旋轉，推水末段才快速轉向另一側
- **主張拆解**：① 拉水主要推進段的 roll 是否較少；② roll 的角度／角速度峰值是否在末段；③ 「延遲」是否是研究操作變項或教練口令。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'delay.{0,40}rotat|rotat.{0,80}(finish|end|late)|finish.{0,80}rotat|late.{0,40}rotat' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/40_Figure_3.4.md`；`Fundamentals_of_Fast_Swimming/19_Chapter_16_Backstroke_Coupling_Motions.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `40_Figure_3.4.md:25`：
      > “the body should rotate quickly and at a specific time in the stroke cycle—as one arm is entering and the other arm is finishing.”
    - 同行續句：
      > “The rotation should happen only at the beginning and end of the arm strokes, not during the most propulsive parts of the arm stroke...”
    - `40_Figure_3.4.md:31`：
      > “Late rotation is the result, which creates problems in engaging the catch with the opposite arm.”
    - 教材區分「主要推進段不旋轉」與「late rotation error」；它沒有把 late/delayed rotation 當同義技術。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'backstroke.{0,160}(rotation|roll).{0,160}(timing|finish|pull)|late rotation|rotation.{0,160}backstroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：`Heinlein_2010_Biomechanical_Considerations_Competitive_Swimmers_Shoulder/02_readable.md`（敘事段落）；沒有專門量測 backstroke body-roll timing 的本地一手研究。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `02_readable.md:72`：
      > “The opposite arm enters the water a split second before the first arm finishes pulling.”
    - 此句只給雙臂時序，沒有 roll 角度／角速度。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`backstroke AND ("body roll" OR "shoulder roll") AND timing`；以 `.../PMC7804020/fullTextXML` 讀 Results／Discussion。
  - 命中：PMID 33436944／PMCID PMC7804020，*Body roll amplitude and timing in backstroke swimming and their differences from front crawl at the same swimming intensities*，Gonjo et al.，2021，*Scientific Reports*，DOI 10.1038/s41598-020-80711-5。
  - 原文句（逐字，含所在段落標題）：
    - Results：
      > “The timing of peak in WBRBT and shoulder roll was earlier in backstroke than in front crawl.”
    - Discussion 另彙述既有報告：second down-sweep 完成時可見最大 shoulder-roll angular velocity；該句是作者引用先前研究來解釋機制，不是本研究直接測得的手部力。
- **找到的證據屬哪一層級**：直接量測的游泳三維 body-roll 運動學研究 + 游泳教材模型。
- **是否直接回答原主張**：只回答部分；文獻直接量 roll 幅度與峰值時序，也把 finish／entry 視為快速轉換區，但沒有把「延遲旋轉」定義成介入或策略；教材反而另把 late rotation 標為技術錯誤。
- **樣本與外推邊界**：10 名男性競技選手（4 freestyle、3 backstroke、3 IM），每泳式 4 × 50 m，約最大速度 83／88／93／100%，25 m 池、2 台水上與 4 台水下攝影機、19 個標記；每 trial 取 1 個上肢週期。沒有女性，且峰值角度時序不等於角速度峰值或主觀「延遲」。
- **缺口**：「拉水過程延遲」的明確相位／角度門檻；推水末段的 roll angular velocity 原始資料與技術介入成績。
- 裁決：

## BR-06｜外掃期：手掌向外下方壓出約 45° 角

- **原文主張（逐字）**：外掃期：手掌向外下方壓出約 45° 角
- **主張拆解**：① 外掃的手部移動／施力方向；② 45° 是掌面 pitch、angle of attack，還是對池面的空間角；③ 是否來自實際蛙式量測。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 '45-degree|45 degree|outsweep|outward|palm' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\41_Chapter_4__Breaststroke_Technique.md' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\42_Figure_4.1.md' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md`；`Science_of_Swimming_Faster/42_Figure_4.1.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `21_Chapter_18...md:24`：
      > “The palms of the hands should not be facing directly to the sides during the lift phase, but rather pitched at about a 45-degree angle.”
    - `42_Figure_4.1.md:19`：
      > “The arms are angled so that they start to push water downward and backward.”
    - 第一處是 Race Club 教材的 pitch 口令；第二處描述 outward scull 後才增加深度，兩本書的相位詞彙亦不同。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'breaststroke.{0,160}(45|outsweep|outward|palm)|outsweep.{0,100}breaststroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無可直接回答命中；屬已知蛙式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`breaststroke AND (outsweep OR "angle of attack") AND hand`；精煉 `breaststroke AND "angle of attack" AND (kinematic OR hand)`；以 `.../PMC3590870/fullTextXML` 讀 Introduction／Methods。
  - 命中：PMID 23487493／PMCID PMC3590870，*Qualitative evaluation of water displacement in simulated analytical breaststroke movements*，Martens & Daly，2012，*Journal of Human Kinetics*，DOI 10.2478/v10078-012-0023-7。
  - 原文句（逐字，含所在段落標題）：
    - Introduction—Sculling：
      > “the hands move outward or inward through the water with an efficient angle of attack (approximately 40°)”
    - 這句引用 Arellano (2006) 的 sculling 說明；本研究以染料觀察 analytical breaststroke-like movements，沒有直接量完整蛙式外掃的掌面角。
- **找到的證據屬哪一層級**：游泳教材模型 + 間接的分析式 sculling 質性實驗／文獻敘述。
- **是否直接回答原主張**：只回答部分；第 1 層直接給約 45° pitch，線上來源給 sculling 約 40° angle of attack，但沒有證明兩者是同一座標定義，也不是競技蛙式完整週期的直接角度量測。
- **樣本與外推邊界**：Martens & Daly 共 11 名受試者（9 男、2 女；7 名年齡組國家級蛙手、1 名國際級自由式、3 名游泳專項動作科學學生），執行 4 種分析式／模擬蛙式動作，以螢光染料做質性水流視覺化；不是比賽速度、沒有掌面 IMU／三維角度。
- **缺口**：45° 的參考座標與正負方向；實際競技蛙式外掃期間掌面 angle-of-attack 的分布、速度依賴與推力終點。
- 裁決：

## BR-18｜前送期：雙手在下巴/胸前併攏後迅速前推伸直（划距效益描述）

- **原文主張（逐字）**：前送期：雙手在下巴/胸前併攏後迅速前推伸直（划距效益描述）
- **主張拆解**：① 雙手何時／何處靠攏；② 前送是否快速且達伸直；③ 這種做法是否增加划距、速度或效率。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 2 'hands.*(together|converg)|arms.*(extend|forward)|strike phase|rapid|quick|streamline' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\42_Figure_4.1.md' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md'`
  - 命中檔：`Science_of_Swimming_Faster/42_Figure_4.1.md`；`Fundamentals_of_Fast_Swimming/21_Chapter_18_The_Four_Phases_of_the_Breaststroke_Pulling_Cycle.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `42_Figure_4.1.md:59`：
      > “the hands, which will come together in the middle of the arm recovery as the hands are moving forward.”
    - `42_Figure_4.1.md:61`：
      > “The hands should not clap together.”
    - `21_Chapter_18...md:68`：
      > “The hands should feel as if they are shooting almost straight forward, with a slight downward trajectory, but not upward.”
    - `21_Chapter_18...md:74`：
      > “This technique also puts the hands back in front sooner, so it enables a much faster stroke rate.”
    - 兩本教材都描述快速前送／伸直；對「先在胸前拍合」的細節並非同一教法，效益句也不是控制實驗。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'breaststroke.{0,160}(chin|chest|recovery|recover forward|stroke length)|stroke length.{0,100}breaststroke' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無可直接回答命中；屬已知蛙式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`breaststroke AND ("arm recovery" OR "stroke length" OR "hands forward")`；精煉 `breaststroke AND (coordination OR kinematic*) AND (recovery OR "arm-leg") AND (elite OR competitive)`；以 NCBI PMC HTML 讀 PMCID PMC3873659。
  - 命中：PMID 24421728／PMCID PMC3873659，*Intra-cyclic phases of arm-leg movement and index of coordination in relation to sprint breaststroke swimming in young swimmers*，Strzała et al.，2013，*Journal of Sports Science & Medicine*。
  - 原文句（逐字，含所在段落標題）：
    - Abstract：
      > “A significant correlation was observed between the V50surface breast with the percentage of partially surfaced hand phase of arm recovery 0.54, p < 0.01.”
    - Methods 把 recovery 分為 submerged–partly emerged–submerged 三段，沒有標定 hands-at-chin/chest 或「併攏」事件。
- **找到的證據屬哪一層級**：直接量測的蛙式週期運動學／相關研究 + 游泳教材模型。
- **是否直接回答原主張**：只回答部分；教材直接描述前送與伸直，研究把 recovery phase 與 50 m 速度相連；沒有直接量「下巴／胸前先併攏」或以介入證明增加划距。
- **樣本與外推邊界**：23 名男性 regional／national-level 青少年（15.0 ± 1.17 歲，14–17 歲），25 m 池完成 50 m all-out breaststroke；相關係數受週期時序、技術水準等共同影響，不能推為因果，也不能外推成人／女性或長距離。
- **缺口**：雙手靠攏位置的三維座標；「先併攏」與「移動中才靠攏」的直接比較；stroke length、速度、效率的隨機／交叉技術比較。
- 裁決：

## BF-05｜入水期：掌心朝下或些微朝外下方（掌心空間朝向）

- **原文主張（逐字）**：`入水期：掌心朝下或些微朝外下方（掌心空間朝向）`；⚠︎ 註記（逐字）：`BF-05：「掌心朝下或些微朝外下方」是空間朝向，不是前臂關節位置描述。此描述無法用解剖學術語（旋前/旋後）直接裁決。**疑似缺陷 3**，分類暫 C，裁決時確認。`
- **主張拆解**：單一空間朝向主張；另檢查來源是否真的量前臂旋轉（不可由掌心朝向反推）。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'palm|entry|enter|thumb.*down|hand.*pitch' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\44_Figure_5.1.md' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`；`Science_of_Swimming_Faster/44_Figure_5.1.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `24_Chapter_21...md:104`：
      > “Michael Phelps entered his hands pitched with the thumbs down slightly, which causes less drag than with the palms down.”
    - `44_Figure_5.1.md:11`：
      > “turn the hands so that the thumbs are pointing downward toward the bottom of the pool.”
    - 兩句都是教學空間朝向／手勢；沒有量前臂相對肱骨的旋轉。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'butterfly.{0,160}(entry|palm|hand orientation)|palm.{0,100}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無命中；屬已知蝶式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND ("hand entry" OR palm) AND swimming`；精煉 `butterfly swimming AND hand AND (entry angle OR orientation OR kinematic*)`，篩摘要與 PMCID 全文。
  - 命中：PMID 40868310／PMCID PMC12382985，*The Associations Between the Swimming Speed, Anthropometrics, Kinematics, and Kinetics in the Butterfly Stroke*，Pinto et al.，2025，*Bioengineering*，DOI 10.3390/bioengineering12080797；研究只用 hand entry/exit 劃週期，未量掌面朝向。無可直接回答命中。
  - 原文句（逐字，含所在段落標題）：無（Methods 只以手的 entry／exit 定界，沒有 palm-normal 或 forearm-rotation 變項）。
- **找到的證據屬哪一層級**：游泳教材／教練慣例；無直接量測掌面朝向的一手研究命中。
- **是否直接回答原主張**：只回答部分；教材直接比較 palms down 與 thumbs-down slight pitch，可回答入水手部空間朝向；沒有量「些微朝外下方」的角度，也不能由這些句子推回前臂旋轉。
- **樣本與外推邊界**：教材以 Michael Phelps 為示例但未提供樣本、重複試次、座標系或統計；Pinto et al. 為 8 名青年男性、3 次最大 25 m butterfly，只量速度、stroke frequency/length 與推力，不量掌向。
- **缺口**：入水瞬間掌面法向量的三維量測、個體／速度差異；肱骨旋轉與前臂旋轉的分離量測。
- 裁決：

## BF-09｜外掃期：手掌向外、向下、向後掃出，形成「鑰匙孔（keyhole）」路徑的起手（推進描述）

- **原文主張（逐字）**：外掃期：手掌向外、向下、向後掃出，形成「鑰匙孔（keyhole）」路徑的起手（推進描述）
- **主張拆解**：① 外／下／後是否同時或依序；② 整體手路徑形狀；③ 「keyhole」是否為文獻中的命名；④ 外掃是否直接產生推進。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'keyhole|key hole|hourglass|outward.*downward.*backward|outward.*backward|downward.*backward' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`；`Science_of_Swimming_Faster/45_Figure_5.2.md`、`46_Figure_5.3.md`、`50_Figure_5.7.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `24_Chapter_21...md:106`：
      > “there is a very brief and short outsweeping motion of both hands for a few inches.”
      > “This brief outsweep is followed by a pressing downward of the palms then a backward motion with the fingers pointing down.”
    - `50_Figure_5.7.md:1`：
      > “The hourglass pattern scribed by the hands from the commencement of the (a) outsweep, (b) insweep, (c) upsweep, and (d) release.”
    - 本批兩本書未命中 keyhole；一書給「外→下→後」依序，另一書命名為 hourglass。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'butterfly.{0,160}(keyhole|outsweep|outward|downward|backward)|keyhole' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無命中；屬已知蝶式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND (outsweep OR "hand path" OR keyhole) AND swimming`；另以 NCBI ESearch 實跑 `"butterfly" "outsweep" swimming biomechanics` 與 `butterfly swimming "keyhole"`。
  - 命中：PMID 39454553，*Breaststroke and butterfly intercycle kinematic variation according to different competitive levels with Statistical Parametric Mapping analysis*，Fernandes et al.，2024，*Journal of Biomechanics*，DOI 10.1016/j.jbiomech.2024.112380；`butterfly swimming "keyhole"` 的 5 筆命中皆為非游泳同義詞雜訊。
  - 原文句（逐字，含所在段落標題）：
    - Abstract：
      > “the outsweep phases originating variability between butterfly cycles.”
    - 該研究辨識 outsweep 相位，但摘要未提供三維手路徑或 keyhole/hourglass 命名。
- **找到的證據屬哪一層級**：直接量測的游泳週期運動學研究（只到相位）+ 游泳教材模型（手路徑）。
- **是否直接回答原主張**：只回答部分；教材直接描述外→下→後的順序和 hourglass 路徑，研究確認 outsweep 作為分析相位；三層均未找到游泳來源使用「keyhole」命名，也未量起手三方向的同步推力。
- **樣本與外推邊界**：Fernandes et al. 為 20 名 elite 與 15 名 national-level，完成 25 m breaststroke 與 butterfly sprint，水下矢狀面 120 Hz；分析相位時長與速度變異，沒有掌面法向量、橫向攝影或三維 keyhole 路徑。教材無樣本 protocol。
- **缺口**：「keyhole」作為蝶式路徑名稱三層皆無；外／下／後三維手軌跡與分相推力的同步量測亦無。
- 裁決：

## BF-22｜出水期：蝶式沒有軀幹旋轉輔助，肩胛骨穩定肌群（菱形肌、前鋸肌）負擔比自由式更大

- **原文主張（逐字）**：出水期：蝶式沒有軀幹旋轉輔助，肩胛骨穩定肌群（菱形肌、前鋸肌）負擔比自由式更大
- **主張拆解**：① 蝶式出水／移臂是否沒有縱軸 body roll 輔助；② 菱形肌與前鋸肌在該期的活動／負荷；③ 是否以同一 protocol 直接比較蝶式與自由式，且蝶式更大。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'butterfly.{0,160}(scapul|rhomboid|serratus|trunk rotation|body roll)|body roll cannot assist|cannot be assisted by a body roll' 'C:\claudehome\resources\books\Science_of_Swimming_Faster' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming' -g '*.md'`
  - 命中檔：`Science_of_Swimming_Faster/44_Figure_5.1.md`、`48_Figure_5.5.md`、`51_Figure_5.8.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `44_Figure_5.1.md:5`：
      > “the height of the recovery is limited by the shoulder structure and, unlike in front crawl, cannot be assisted by a body roll about the longitudinal axis of the body.”
    - `51_Figure_5.8.md:7`：
      > “But unlike in the front crawl, body roll cannot assist the action.”
    - 兩句回答 body-roll 部分；兩本書未命中「rhomboid/serratus 負擔比 freestyle 更大」的比較資料。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'butterfly.{0,160}(scapul|rhomboid|serratus|trunk rotation|body roll)|scapul.{0,160}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無命中；屬已知蝶式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND (scapular OR serratus OR rhomboid OR electromyography) AND swimming`；NCBI ESearch 精煉 `butterfly swimming rhomboid serratus anterior electromyography` 與 `butterfly freestyle serratus anterior comparison`；PubMed `efetch` 取摘要。
  - 命中：PMID 3752349，*Fine wire electromyography analysis of muscles of the shoulder during swimming*，Nuber et al.，1986，*American Journal of Sports Medicine*；PMID 8458154，*The normal shoulder during the butterfly swim stroke. An electromyographic and cinematographic analysis of twelve muscles*，Pink et al.，1993，*Clinical Orthopaedics and Related Research*（無摘要／全文）；PMID 36068286／PMCID PMC9448761，*Difference in muscle synergies of the butterfly technique with and without swimmer's shoulder*，Matsuura et al.，2022，*Scientific Reports*，DOI 10.1038/s41598-022-18624-8。
  - 原文句（逐字，含所在段落標題）：
    - Nuber et al.，PubMed Abstract：
      > “the serratus anterior functions near maximal muscle test during each stroke”
    - 同研究比較 freestyle、breaststroke、butterfly，但沒有說 butterfly 大於 freestyle，且未量 rhomboid；Matsuura et al. 量 serratus anterior／trapezius 等 12 肌，但只有蝶式、有無肩傷兩組，也未量 rhomboid。
- **找到的證據屬哪一層級**：直接量測的游泳 EMG 研究 + 游泳教材模型。
- **是否直接回答原主張**：只回答部分；body-roll 缺席由教材直接描述，EMG 顯示 serratus anterior 在各泳式皆接近 maximal muscle test；沒有同一研究中的「蝶式 > 自由式」菱形肌／前鋸肌負荷比較。
- **樣本與外推邊界**：Nuber et al. 共 11 名游泳者（5 名 dry-land、7 名 aquatic，1 人兩者皆做），分析 freestyle／breaststroke／butterfly、8 肌；水中樣本很小，摘要未報泳式間統計。Matsuura et al. 為 20 名 elite 年輕男性（12 control、8 swimmer’s shoulder），50 m 池以 100 m 蝶速游 25 m、12 肌 surface EMG；沒有自由式對照或菱形肌電極。
- **缺口**：同一受試者、同速度／強度下的蝶式 vs 自由式出水／移臂期 rhomboid 與 serratus anterior EMG／肌力矩比較；「負擔」的操作定義（幅度、積分 EMG、疲勞或力矩）。
- 裁決：

## BF-25｜移臂期：前臂掌心由朝內逐漸轉為朝下（準備入水）（掌心朝向描述）

- **原文主張（逐字）**：`移臂期：前臂掌心由朝內逐漸轉為朝下（準備入水）（掌心朝向描述）`；⚠︎ 註記（逐字）：`BF-25：「掌心由朝內逐漸轉為朝下」是空間朝向描述，嘗試推斷前臂旋轉方向。掌心朝向由肱骨旋轉＋前臂旋轉合成，不能單從掌心朝向反推前臂。**疑似缺陷 3（朝向反推旋轉）**，分類降 C，裁決時確認。`
- **主張拆解**：① 移臂早期掌心是否朝內；② 接近入水是否轉至朝下；③ 是否有連續的掌面朝向量測；④ 不由掌向推論前臂關節旋轉。
- **第 1 層（游泳書）檢索**：
  - 實跑指令：`rg -n -i -C 3 'arm recovery|recovery.*(hand|palm|thumb)|hand.*recovery|thumb.*entry|thumb.*down|palms.*down|palms.*in' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\43_Chapter_5__Butterfly_Technique.md' 'C:\claudehome\resources\books\Science_of_Swimming_Faster\44_Figure_5.1.md' 'C:\claudehome\resources\books\Fundamentals_of_Fast_Swimming\24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md'`
  - 命中檔：`Science_of_Swimming_Faster/44_Figure_5.1.md`；`Fundamentals_of_Fast_Swimming/24_Chapter_21_Butterfly_Fundamentals_and_Techniques.md`。
  - 原文句（逐字 + 檔名 + 行號／章節）：
    - `44_Figure_5.1.md:11`：
      > “The instruction to achieve the required internal rotation is simply to turn the hands so that the thumbs are pointing downward toward the bottom of the pool.”
    - `24_Chapter_21...md:104`：
      > “The hands should enter the water slightly inside the shoulders, perhaps 8-10 inches apart, preferably with the thumbs down.”
    - 兩句只給接近入水／入水的 endpoint，未描述移臂早期 palms-in，也未連續量掌向；thumbs-down 和 palms-down 不是同一空間描述。
- **第 2 層（本地文獻集）檢索**：
  - 實跑指令：`rg -n -i 'butterfly.{0,160}(recovery|palm|hand orientation)|palm.{0,100}butterfly' 'C:\claudehome\resources\books\swimming-kinetic-chain' -g '02_readable.md'`
  - 命中檔：無命中；屬已知蝶式 0 篇覆蓋缺口，查無不具推論力。
  - 原文句（逐字 + 檔名 + 行號／章節）：無。
- **第 3 層（線上文獻）檢索**：
  - 實跑查詢 + 管道：Europe PMC REST，`butterfly AND ("arm recovery" OR "hand entry") AND (palm OR forearm)`；精煉 `butterfly swimming AND recovery AND (hand orientation OR palm OR forearm rotation)`，篩摘要與可用 PMCID 全文。
  - 命中：PMID 36068286／PMCID PMC9448761，Matsuura et al.，2022，*Difference in muscle synergies of the butterfly technique with and without swimmer's shoulder*，*Scientific Reports*；該研究用 wrist／elbow／acromion／hip LED 標記切 early pull、late pull、recovery，但未量掌面朝向或前臂旋轉。無可直接回答命中。
  - 原文句（逐字，含所在段落標題）：無（Methods 沒有手掌標記、掌面法向量或橈尺骨旋轉變項）。
- **找到的證據屬哪一層級**：游泳教材／教練慣例；無連續掌向或前臂旋轉的一手量測命中。
- **是否直接回答原主張**：只回答部分；教材只回答接近入水的 thumbs-down endpoint，未回答「由朝內逐漸轉為朝下」的完整過程；任何掌向句都不能單獨回答前臂旋轉。
- **樣本與外推邊界**：教材沒有樣本或座標系；Matsuura et al. 為 20 名 elite 年輕男性、25 m butterfly at 100 m race pace、50 m 池、200 Hz 影片＋surface EMG，但其標記／變項不足以重建掌面或區分肱骨與前臂旋轉。
- **缺口**：移臂全程掌面法向量；早期 palms-in 的直接資料；肱骨縱軸旋轉與前臂旋前／旋後的同步分離量測。
- 裁決：

# 14 條索引總表

| ID | 找到的證據層級 | 是否直接回答 | 最主要未回答部分 |
|---|---|---|---|
| BK-26 | 直接游泳運動學 + 教材模型 | 是 | 無跨文獻命名共識；四 sweep 之外另列 recovery |
| FR-09 | 肩胛運動學 + 教材／綜述周邊證據 | 否 | 肩胛前伸 → 划距／速度／效率的直接鏈結 |
| FR-13 | 直接 EMG／腕運動學 + 教材模型 | 只回答部分 | 抓水腕角兩方案及「划槳面」力學效益 |
| FR-17 | 直接三維游泳運動學 + 教材模型 | 是 | 技術介入的因果效果；口語高度與正式 index 門檻 |
| BK-10 | 教材負荷模型 + 臨床綜述 + 傷害系統性回顧 | 只回答部分 | 仰式入水位置特異的傷害頻率／風險倍數 |
| BK-17 | 教材模型 | 是（教材層級） | 抓水三維腕角／掌面與推力的一手量測 |
| BK-21 | 相位運動學 + 教材／綜述模型 | 只回答部分 | second down sweep 的肩伸展角時間序列 |
| BK-29 | 直接三維 body-roll 運動學 + 教材模型 | 只回答部分 | 「延遲」的操作定義與末段角速度介入效果 |
| BR-06 | 教材模型 + 間接 sculling 質性實驗 | 只回答部分 | 實際蛙式外掃的 45° 座標與直接量測 |
| BR-18 | 直接蛙式週期相關研究 + 教材模型 | 只回答部分 | 下巴／胸前併攏事件及划距因果效果 |
| BF-05 | 教材／教練慣例 | 只回答部分 | 三維掌向角；不可由掌向推前臂旋轉 |
| BF-09 | 週期運動學 + 教材模型 | 只回答部分 | keyhole 命名與三維路徑／分相推力 |
| BF-22 | 直接游泳 EMG + 教材模型 | 只回答部分 | 蝶式 > 自由式的菱形肌／前鋸肌同 protocol 比較 |
| BF-25 | 教材／教練慣例 | 只回答部分 | palms-in → palms-down 全程與前臂旋轉分離量測 |

- **三層皆無（以原主張核心關係是否被直接回答為口徑）**：FR-09（「前伸滑行期肩胛前伸 → 增加划距／效率」）。
- **整條連周邊資訊都沒有任何命中的 ID**：無；其餘 13 條至少有教材描述、相位資料、負荷資料或直接運動學／EMG 的其中一部分。
- **另有三層皆無的子主張**：BK-10 的仰式入水位置特異傷害頻率；BF-09 的 `keyhole` 游泳命名；BF-22 的「菱形肌、前鋸肌負擔比自由式更大」同 protocol 比較。
