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
- 裁決：**修正（拆三段：姿勢層支持、關節歸屬刪除、效益句降為教材主張）**｜衝突型 1（參考系未對齊）
  - 判定：三段必須拆開。①「腿足維持在與身體對齊的窄通道」有教材直述（`21_Figure_2.3.md:7`），**姿勢層成立**。②「髖幾乎不做外展／內收」**無任何量測支持**，且是由池畔可見的腿部路徑寬度反推額狀面關節動作——同一段原文恰恰說明了為什麼不能這樣反推：身體滾轉使打水成為**斜向（oblique）**，「窄通道」是相對**身體軸線**而非相對池畔垂直面。③「避免打水過寬增加阻力」只到教材主張層；Narita 2018 操弄的是**有無打水**而非打水寬度，三層無同協議的寬度—阻力比較。
  - **反向警示**：同段教材明寫刻意把腳維持在垂直面內是反效果——
    > “it is not necessary—in fact, it is counterproductive—to try to keep the feet kicking perfectly in the vertical plane.”

    原主張若被讀成「別讓腿往兩側動」，會直接產生與教材相反的教學指令。
  - 可寫入：腿足相對**身體軸線**維持窄通道（教材層）；身體滾轉下打水呈斜向是常態而非缺陷。
  - 不得寫入：髖外展／內收幅度接近零（無量測）；打水寬度與主動阻力的量化因果。
  - movement 落地：可產出**姿勢層** demand，但必須標為池畔可見的空間描述，不得寫成關節角度需求。
  - 根因：結構性 4，且揭示其一般形式是「**可見空間量→關節動作**」而不只是「朝向→旋轉」；加重條件是**參考系本身在轉**（body roll），同一條腿路徑在池畔系與隨體系有完全不同的關節解釋。見文末結構性根因 4 的擴充。

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
- 裁決：**表現端修正（降級並強制標量測方式）＋傷害端整條不採用**｜表現端衝突型 1（同名不同量）；傷害端非衝突，是證據層級冒用
  - 判定（表現端）：三個來源量的是**三種不同的東西**，不能合併成一個「翻腳期外旋幅度」——Strzała 2012 與 Jagomägi 2005 量的是**陸上 ROM**（塑膠量角器、俯臥膝約 90°），Kippenhan 2002 量的是**水中體表標記重建的節段角**且終點是兩名教練 1–8 分的**主觀 effectiveness**。三者都不是「翻腳期的動態外旋幅度」。強度用語「主要因素之一」不成立：Strzała 的年齡控制偏相關 r=0.35、`p < 0.08`（**未達 0.05**），且同研究最強的速度關係是 15 秒垂直跳的無氧耐力（0.46、`p < 0.05`）；Jagomägi 的 11.1% 是逐步迴歸解釋量，樣本限 11–18 歲女性、終點是 100 m 踢板。
  - 判定（傷害端）：Keskinen 1980 是 **6 名患者對 3 名對照**的關節鏡／攝影研究，且**技術差異未達顯著**；作者只把重複的高速髖膝角運動與脛股外旋列為**可能機制**。沒有任何以動態膝外旋幅度為獨立暴露量的前瞻風險研究。據此寫出頻率、風險或「好發」語言即命中根因 3。
  - 可寫入：陸上膝外旋 aROM 與蛙式踢板速度／踢距有弱至中度關聯但未達顯著（Strzała 2012, n=27）；在 11–18 歲女性中為表現變異的解釋項之一（11.1%，Jagomägi 2005, n=125）；膝外旋是最可能限制踢腿 effectiveness 的關節動作（Kippenhan 2002，**教練評分終點**）。**每一句都必須連同量測方式與終點一起寫，拆開即失真。**
  - 不得寫入：「決定鞭狀踢速度的主要因素之一」；任何傷害頻率、風險倍數或「好發」語言；把 effectiveness 當速度終點。
  - **待查（本次無法核）**：同作者 2001（ISBS 19）與 2002（ISBS 20）對下掃期膝旋轉方向的表述疑似不一致（一處作 internal、一處作 external knee rotation）。本次 `ojs.ub.uni-konstanz.de` 連線遭拒（ECONNREFUSED），未能核對 2001 全文；**在核實前不得引用此方向差異下的任何結論**。
  - movement 落地：表現端只能落成**條件式**描述，不得成為訓練指令；傷害端 `evidence-gap` + `action_status: do-not-prescribe`，`dosage_source_ids` 留空（W016）。
  - 根因：結構性 2（同名不同量、缺座標與終點定義）＋ 結構性 3（機制推測冒充流行病學）。

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
- 裁決：**修正（改判：型 5「真實學界分歧」不成立，改為研究空白 ＋ 型 1 相位／方法未對齊）**
  - **依附錄自訂的判準**：`plans/關節主張裁決_蛙式.md:451` 已預先定死「方法層對不上就不構成真正的矛盾」。本次查證結果比預期更不對稱——**不是兩派方法不同，而是有一派根本不是量測研究**。因此這不是推翻附錄，是依它自己寫下的條件把它走完。
  - 判定：①「外旋端」是復健教材的技術敘述（Dunlap，收於 Brody & Geigle 2009），**原文未報告測量方法**，屬來源優先序第 3 層。②`cite index="15-1"` 端連文獻身分都無法解析，且其推論形式正是根因 4——由「腳尖朝外」這個**空間朝向**反推髖旋轉方向；而 BR-28 附錄（同檔 `:418`）已裁定非負重下「腳尖朝外」目視**無法**分辨是髖、膝或距下在轉。③唯一有方法可核的是 Kippenhan 2001（ISBS 19；29 名泳者、22.9 m 踢板衝刺、60 Hz 雙攝影、16 體表標記／7 節段三維重建），但其髖旋轉是**體表標記推算值**，且結論所屬相位是**下掃期**，不是本主張的**翻腳期**。
  - **兩派其實不在同一相位**：raw note `:493` 的甲說明寫「收腿期」，`:494` 的乙說講「蛙式蹬腿動作」，而唯一可核的量測資料落在**下掃期**。收腿／翻腳／蹬夾／下掃被壓成同一個問題（根因 7），這正是「爭議」看起來無法收斂的主因之一。
  - 可寫入：此問題**目前沒有任何針對翻腳期、以分節段三維量測直接回答髖旋轉方向的研究**；既有各方分別是教材敘述、解剖推理與下掃期的標記推算值，彼此未回答同一問題。
  - 不得寫入：任一單一方向答案；**也不得再寫成「學界有爭議」**——那會讓讀者以為兩邊各有實證，實際上是研究空白。BR-23 的既有「修正」裁決**維持不動**（依規格不重做）。
  - movement 落地：`evidence-gap` + `action_status: do-not-prescribe`，不得落成 demand 或活動度 intervention。
  - 根因：結構性 4（空間朝向反推關節旋轉）＋ 結構性 7（相位交界壓成單點）＋ **新增結構性 8**（把「來源說法不同」直接標成學界分歧），見文末。

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
- 裁決：**修正（三段全改：時序並列、「較大力」與證據反向須刪、因果方向顛倒須改寫）**｜衝突型 1 ＋ 根因 7
  - 判定①（時序）：部分支持，但四個來源各有自己的相位錨點——SoSF `44_Figure_5.1.md:13` 錨在移臂後入水的俯衝；FoFS `24_Chapter_21...md:62` 把推進峰錨在**手到腹部、正向後拉**時；Chollet 2006 的 T1／T2 錨在手入水與第一波動的高／低轉折點；Seifert 2008 的 T1 錨在 arm catch 起點。依型 1 並列不選邊，但寫入時必須標明採用哪一套操作定義。
  - 判定②（「較大力」）：**與現有證據方向相反，必須刪除**。SoSF `44:13` 明寫第一踢是 “a modest downbeat of the feet”，且 “does not need great effort”；Barbosa 2008 在高速條件下實測**第二** downbeat 的平均足垂直速度**高於**第一。三層沒有任何同協議的兩踢力值比較，而所有可比資料都指向與原文相反的方向。
  - 判定③（「協助壓胸、啟動身體波動」）：**因果方向顛倒**。SoSF `44:13` 原文為第一踢 “takes advantage of the energy transmitted to the lower body by the pendulum-like rotation of the upper body. A body wave has transmitted the energy from hips to feet.”——體波是**上身→髖→足**傳下來的，第一踢是**承接端**，不是波動的啟動端。
  - 可寫入：第一次下踢落在手入水／catch 到拉水前段的時間窗（標明分期出處）；它承接上身鐘擺傳下的體波並協助身體前轉；其耗能低。
  - 不得寫入：「第一次踢較大力」；「腿啟動身體波動」；把入水、外掃、壓胸與推進寫成同一瞬間。
  - movement 落地：時序可落成 demand（須帶 `phase_model`）；**力量大小與「啟動波動」不得落成 demand 或 intervention**。
  - 根因：結構性 2（比較級無量表）＋ 結構性 7（相位壓成單點）＋ **新增結構性 9**（因果方向顛倒），與 2026-06-19 已修正的 A-1 自由式髖部驅動同型。

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
- 裁決：**修正（時序支持並列、「較小力」與證據反向須刪、臀部下沉降為未證）**｜衝突型 1 ＋ 根因 7
  - 判定①（時序）：**支持**。SoSF `51_Figure_5.8.md:11` 明寫 “During the upsweep, the downbeat of the second kick occurs”；Chollet 2006 的 T3／T4 配對手到肩垂直面與手離水、Seifert 2008 的 T3 配對 arm push 起點與第二腿 down phase 起點。三者一致把第二踢放在推水到出水的時間窗。
  - 判定②（與 FoFS 的表面不一致**不是矛盾**）：FoFS `24_Chapter_21...md:62` 把第二個推進峰錨在 “precisely as the recovering arms hit the water”。這與 SoSF 並不衝突——一個講 downbeat 的**起始**（upsweep 期），一個講**推進峰值**（接近入水）。把兩者當對撞就是根因 7；正確處置是拆成 `phase`／`event`／`outcome` 三欄並列。
  - 判定③（「較小力」）：**與證據反向，必須刪除**。SoSF `51:11` 明寫此踢 “produces propulsion and elevates the center of mass”，而**第一**踢才是 “modest”；Barbosa 2008 高速條件下第二 downbeat 足垂直速度高於第一。原文的大／小力分配**整組顛倒**。
  - 判定④（「避免臀部下沉」）：降為未證。Barbosa 只在討論段談 strong second downbeat 與 “keep the hip near to surface” 的關係，量的是足速、節段速度與**估算質心**；SoSF 說的是 “elevates the center of mass”（質心）而非臀高。無任何以臀部高度為終點的介入研究。
  - 可寫入：第二次下踢的 downbeat 起始落在推水／upsweep 期，其推進峰值接近手出水至回復臂入水（**兩者分欄**）；此踢與質心抬升相關（Barbosa 2008，pilot，樣本小）。
  - 不得寫入：「第二次踢較小力」；「避免臀部下沉」的因果句；把 downbeat 起始與推進峰值寫成同一瞬間。
  - movement 落地：時序是本批**證據最強、可直接產出 demand** 的一條（兩份直接運動學研究 ＋ 教材一致），須帶 `phase_model` 與 `event` 欄；力量大小與臀高效果不得落成 demand。
  - 根因：結構性 2 ＋ 結構性 7；與 BF-32 合觀屬同一組**大／小力分配整體顛倒**。

---

# 裁決總表（2026-09-02）

| ID | 類 | 衝突型 | 裁決 | 主要依據定位 | 根因 |
|---|---|---|---|---|---|
| FR-40 | C | 1 | 修正（姿勢層留、關節歸屬刪、效益句降教材層） | `21_Figure_2.3.md:7`；Narita 2018 (PMID 29921521) | **結構性 4（擴充）** |
| BR-29 | C | 1（表現端） | 表現端修正並降級；**傷害端整條不採用** | Strzała 2012；Jagomägi 2005；Kippenhan 2002；Keskinen 1980 | **結構性 2 + 3** |
| BR-30 | C | 改判 5→1 | 修正（**型 5 不成立，改為研究空白**） | 蛙式附錄 `:418`／`:451`；Kippenhan 2001 (ISBS 19)；raw note `:493`–`:494` | **結構性 4 + 7 + 8** |
| BF-32 | C | 1 | 修正三段（時序並列、刪「較大力」、改因果方向） | `44_Figure_5.1.md:13`；Chollet 2006；Seifert 2008；Barbosa 2008 | **結構性 2 + 7 + 9** |
| BF-33 | C | 1 | 修正（時序支持、刪「較小力」、臀高降未證） | `51_Figure_5.8.md:11`；`24_Chapter_21...md:62`；Barbosa 2008 | **結構性 2 + 7** |

計：**5 條全部修正，零條原封不動通過**；其中 BR-30 改判分類、BR-29 傷害端與 BF-32／BF-33 的力量分配為整段不採用。

## 本批的三個實質發現

1. **蝶式兩次踢的大／小力分配整組寫反**（BF-32＋BF-33）。原文寫「第一次踢較大力、第二次較小力」，但 SoSF 明寫第一踢是 “modest”、“does not need great effort”，第二踢 “produces propulsion and elevates the center of mass”；Barbosa 2008 在高速條件實測第二 downbeat 足垂直速度高於第一。**所有可比證據都指向相反方向**，且這組敘述若落成 demand 會直接產出錯誤的教學重點。
2. **BR-30 的「學界爭議」其實是研究空白**。附錄原判型 5（真實學界分歧）並預留了推翻條件；查證後發現「外旋端」是復健教材敘述（無測量方法）、另一端連文獻身分都無法解析且屬空間朝向反推，唯一有方法的 Kippenhan 2001 講的是**下掃期**而非翻腳期。兩派根本不在同一相位、不是同一種證據。
3. **FR-40 暴露 movement demand 缺「參考系」欄位**。「窄通道」是相對**身體軸線**的空間描述，而身體在滾轉；同一條腿路徑在池畔固定系與隨體系有完全不同的關節解釋。這是協議 §5 已知結構缺陷（池畔可見方向 vs 解剖動作）在**額狀面 + body roll** 的延伸。

## 結構性根因（延續第 1–2 批編號）

- **4（擴充）由可見空間量反推關節動作**：原定義是「由空間朝向反推關節旋轉」（掌心朝下→旋前）。FR-40 與 BR-30 顯示其一般形式是「**可見空間量 → 關節動作**」，含路徑寬度、腳尖朝向等；加重條件是**參考系本身在轉**（body roll、非負重下的足相對小腿）。治本是資料層強制標明**觀察參考系**，不是逐條修。
- **8（新增）「來源說法不同」未經同相位／同量／同方法檢查就標成學界分歧**：型 5 誤用。徵狀是條目寫「不同研究描述不一致／存在爭議」，但各方其實沒有回答同一個問題。這是 BK-29 教訓（蒐證期誤判教材對撞）在**裁決層**的鏡像：前者把不矛盾的當矛盾，後者把不對等的當對等。**代價比誤判更高**——標成「爭議」會讓讀者以為兩邊各有實證，實際上是沒有人量過。
  → **裁決任何「爭議」標記前必須先答三問**：各方是同一相位嗎？量的是同一個量嗎？各自有方法可核嗎？三問有一個否，就不是型 5。
- **9（新增）因果方向顛倒**：把被動承接的環節寫成驅動端（BF-32 的「腿啟動身體波動」，原文實為上身鐘擺→髖→足傳下的體波）。與 2026-06-19 已修正的 A-1 自由式髖部驅動同型，是本庫第二次出現。凡出現「啟動／驅動／帶動」等詞，一律回原文確認能量或動作的傳遞方向。

## 對第 4 批（spine-neck／軀幹旋轉，12 條）的操作指示

- 根因 **8** 預期在本分區高頻：body roll 與軀幹旋轉最容易出現「不同研究描述不一致」的措辭，且第 2 層對 body roll **0 篇覆蓋**。凡遇「爭議／不一致」一律先過上述三問，不得直接標型 5。
- 根因 **4（擴充）** 同樣預期高頻：肩線、骨盆、軀幹的「轉多少度」極易由體表可見朝向反推；且自由式與仰式全程在滾轉，**參考系問題是本分區的預設狀態而非例外**。
- 根因 **9**：軀幹旋轉與手臂／腿的因果敘述（「轉體帶動手臂」vs「手臂拉動轉體」）必須逐條回原文確認方向。

## 對 W4（Step 17–18）的直接輸入

- **可直接產出 demand**：BF-33 的第二踢時序（Chollet 2006 ＋ Seifert 2008 兩份直接運動學研究 ＋ SoSF 一致，本批證據最強，須帶 `phase_model` 與 `event` 欄）；BF-32 的第一踢時序（同樣須標分期出處）；FR-40 的窄通道**姿勢層**描述（須標為池畔可見空間描述）。
- **明確不得落成 demand／intervention**：BR-30（`evidence-gap` + `do-not-prescribe`）；BR-29 傷害端（同上）；BF-32 的「較大力」與「啟動波動」；BF-33 的「較小力」與「避免臀部下沉」。
- **數值一律不進 demand**：Strzała 的 r=0.35／Jagomägi 的 11.1% 只能以定性條件式存在，且必須連同量測方式與終點一起寫。
- **新增欄位需求**：demand 需要能標「觀察參考系」（池畔固定 vs 隨體）。此為 FR-40 的直接產出，建議與 Step 21（W013 是否升級）一併評估。
