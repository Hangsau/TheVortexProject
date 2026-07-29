# 書籍萃取 × Vortex 補強 Implementation Checklist

日期：2026-07-29

## 原則

- 不以「是否直接量到節段能量」作為能否使用的二分門檻。
- 直接研究、間接研究、教材模型與教練量測都可以產生內容，但必須說明各自回答什麼。
- 有多少證據說多少話；模型要能導向觀察、訓練選擇與個人驗收，不只留下限制聲明。
- 先展開 Vortex 既有完整來源鏈，再判斷書籍材料是補強、補應用、補多模型或真正衝突。

## A. 比對基線

- [x] 固定 Atlas commit `48ec9bb` 與 Vortex commit `8c1d505`。
- [x] 確認兩本泳書共 14 份分析；NSCA、Anatomy Trains、Yoga Anatomy、Drill、Periodization 各 1 份，共 19 份。
- [x] 19/19 建立 Vortex 對應 ID、完整來源鏈、差異分類與行動。
- [x] 區分 `直接研究／書籍模型／教練量測／整合應用`，不把其中任一類自動判成無效。

## B. 可直接增加產能的補強

- [x] 兩本泳書的相位／coupling 模型保留為可操作的教練模型。
- [x] 將模型連到影片觀察點、個人 A/B 測試與完整泳段 outcome。
- [x] NSCA 補入測試效度、需求分析、總負荷與 criteria-based progression。
- [x] 出發／轉身補入完整 segment 與個人速度切換，同時保留新研究對多數精英立即起踢的支持。
- [x] 蛙式與蝶式保留多種策略，不以單一書籍模型壓掉其他可行解。

## C. 來源與說法校正

- [x] 為已完成全文核對的兩本泳書及相關直接研究建立 verified source records。
- [x] 修正把 Anatomy Trains 假說寫成已證實游泳傳力路徑的條目，但保留它作動作觀察與陸上候選。
- [x] 將固定手腿比例、固定 coupling 時差等數字綁回實際量測情境，不刪除其教練用途。
- [x] 同步 canonical、研究散文與 periodization index 中的重複說法。

## D. 明確不做

- [x] 不恢復已撤回的 Knowledge Hub／publication。
- [x] 不新增重複 drill；現有 176 IDs 與 125/125 書籍 drill 保持不變。
- [x] 不用書籍分析覆蓋 Vortex 已有的較新直接研究。
- [x] 不因不確定性而只產生「不能說」的空洞內容。

## E. 驗收

- [x] `python tools/validate.py`：0 ERROR。
- [x] Vortex 全測試通過，drill ID／taxonomy 零漂移。
- [x] `python tools/build_indices.py` 連續重建一致。
- [x] my-site sync dry-run、實際同步與 Hugo production build 通過。
- [x] 網站不復活 Knowledge Hub，更新內容可追到 Vortex canonical。
- [x] commit、push、CI 與線上抽查完成（Vortex `452a910`；my-site `99d5565`）。

## F. 肯定式公開重寫（2026-07-29）

- [x] 自由式主幹改為直接功率分解：胸廓旋轉、肩內收、肘伸與踢腿減阻。
- [x] 自由式、蝶式、蛙式與 UDK 全部加入「看到什麼問題 → 修哪個節點 → 用什麼驗收」。
- [x] UDK 以個人滑行／踢腿淨力交叉速度決定起踢，保留 1.9–2.2 m/s 群體起點。
- [x] 陸訓改成出發、推牆、水面功率、轉身後 5m、疼痛與活動度的條件分流。
- [x] 早期無反應研究改寫成 4–6 週後的換法規則，不再當成整頁否定句。
- [x] taper 改成可直接執行的減量幅度、頻率、天數與比賽分流。
- [x] Vortex canonical 驗證、全測試、索引冪等與 diff check。
- [x] 同步 my-site、Hugo production build、部署與線上抽查（Vortex `48efa92`；my-site `1feab71`）。
