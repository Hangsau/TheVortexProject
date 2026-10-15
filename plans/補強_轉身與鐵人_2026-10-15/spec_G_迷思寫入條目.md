# 派工規格 G：鐵人迷思判定寫進 canonical

> 立即執行，不要只輸出計畫。工作目錄 `C:\claudehome\projects\TheVortexProject`。禁止任何 git 操作。不上網。

## 輸入
- `Research/鐵人泳訓/myths.md`（M1–M17 判定）、`sources.md`、`quote_check.md`。
- **可引用的來源只限**：`quote_check.md` 裡狀態為 `ok` 的，加上手動確認的 S02、S12、S16、S24、S52、S53、S54。其他來源（partial、none、empty-page、S55）不得作為條目依據；它們的說法若要用，只能當「流傳證據」寫在研究層，不進 canonical。
- 已登錄的來源（`canonical/_sources.yaml`）直接沿用；新引用的照 spec_E 方式登錄（研究 journal-article；實務 web-article；論壇 web-article 並在 notes 註明論壇）。

## 要寫
1. **教學誤區**（`canonical/instructional/teaching-errors.yaml`，`open-water.err1` 起，格式照既有誤區條目，含「哪種教練／教材這樣教」）：只收 myths.md 判定「可收為教學誤區」的版本：
   - M1「鐵人游泳不用踢腿／不用學踢腿」（只收「完全不踢、不用學」的版本；比賽中輕踢是實務共識，要寫清楚分界）
   - M7「一定要雙邊換氣／一定要每三划換氣」（雙邊換氣是有用技能，「一定要」沒有出處）
2. **常見說法判定**（`technical-analysis.yaml`，stroke open-water，新 tech 編號接續，category `concept`，標題格式「『說法』——判定（迷思／部分正確／證據不足）」）。收這幾條，內容寫判定、兩方依據、族群差異：
   - M3 游泳占比小、練游泳不划算
   - M4＋M5 合併：鐵人是長距離所以不用練速度、都以長距離為主／一定要連續游完比賽距離 vs 間歇就夠（連到 tech.16、tech.17，不重寫，只寫判定與證據）
   - M12 游泳段保留體力慢慢游就好
   - M13 成人學太晚、技術改不了（證據只有自述，判定要照 myths.md）
   - M15 賽前一天不要下水
3. **補證據到既有條目**：
   - `open-water.tech.4`（跟游）：加 evidence，Chatard & Wilson 2003（S52）的結果（附受試族群：泳者、非鐵人賽事）與 Brisswalter & Hausswirth 2008 綜述（S53）；🟡（2010 年前研究）。M14「跟游沒差」的判定寫進 summary 一句。
   - `open-water.tech.7`（防寒衣）：加 evidence，Gay et al. 2019（S54）約 6% 的結果（泳者、泳池與水槽 400 m）；🟢。M16「防寒衣快 20%」：20% 沒有出處，寫進 summary。M2「穿防寒衣就不用練技術」證據不足，一句帶過。
4. 規則：
   - 🟢／🟡 只給研究；實務與論壇用 🔵，並在文字開頭標「實務文件：」或「論壇討論：」。不得寫「研究顯示」去包裝實務或論壇。
   - 不自訂數字。數字只寫原文有的，並附受試族群，避免外推到鐵人賽事。
   - 散文不出現 `src.*`；修訂史不進 public。

## 完成前
- `python -X utf8 tools/validate.py` 0 ERROR，不新增 W009／W011／W028／W029。
- `python tools/build_knowledge_map.py`、`python tools/build_indices.py`、`python -m unittest discover tests` 全過（測試若寫死條目數，照實更新常數）。
- 寫 `plans/補強_轉身與鐵人_2026-10-15/G_完成紀錄.md`，最終回覆列新增／修改 ID 與各自引用的來源編號。
