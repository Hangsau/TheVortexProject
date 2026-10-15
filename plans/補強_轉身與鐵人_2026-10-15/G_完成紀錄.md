# G 完成紀錄：鐵人迷思判定寫進 canonical（2026-10-15）

## 新增條目與引用來源（來源編號對照 Research/鐵人泳訓/sources.md）

| ID | 內容 | 引用 |
|---|---|---|
| open-water.err1（teaching-errors） | M1 鐵人不用學踢腿（只收「完全不踢／不用學」版本） | S30、S46、S27、S48（論壇）、S53 |
| open-water.err2（teaching-errors） | M7 一定要雙邊換氣、固定每三划 | S35、S27、S46、S36（論壇） |
| open-water.tech.20 | M3 游泳占比小、練游泳不划算：部分正確（依族群） | S01（🟡）、S29（論壇）、S04（論壇） |
| open-water.tech.21 | M4＋M5：證據不足 | S03、S15 對應的既有登錄（Heggy、Slaughter）、S04（論壇）、Hayes、S16、S02（既有登錄） |
| open-water.tech.22 | M12 保留體力慢慢游：部分正確（依族群） | S03、S01（🟡） |
| open-water.tech.23 | M13 成人學太晚：迷思，證據只有自述 | S41（論壇）、S42 |
| open-water.tech.24 | M15 賽前一天不下水：證據不足 | S10（論壇）、S43（論壇）、S45（廠商部落格） |

## 修改既有條目
- open-water.tech.4（跟游）：加 evidence S52（🟡）、S53（🟡）；summary 加 M14「跟游沒差別」判定一句，並把「沒有可套用百分比」改為「泳池結果不能直接套到鐵人賽事」。
- open-water.tech.7（防寒衣）：加 evidence S54（🟢）；summary 加 M16「20% 沒有出處」與 M2「證據不足」各一句。

## 新登錄來源（_sources.yaml，共 15 筆，verified）
S52 chatard-wilson-2003、S53 brisswalter-hausswirth-2008、S54 gay-2019、S27 mclarty-2013、S30 burgan-2008、S35 casey-2016、S46 sutton-2015、S48、S36、S29、S04、S41、S43（論壇，notes 註明論壇）、S42、S45。沿用既有：Landers 2008（S01）、Heggy（S03）、Slaughter、Laughlin、Hayes、Selles-Perez（S02）、Slowtwitch taper（S10）。

## 規格落差與取捨
- 規格 M12 輸入列了 S55、S19，M4 列了 S50、S47 等：它們在 quote_check 為 none／partial／empty-page 或不在白名單，一律未引用。S44、S32、S50、S07、S09、S17、S21、S23、S26、S47 同理。
- M12「保留體力」的反方沒有研究，S19（Peeling 2005）未採用；M1 的 EJAP 2016 研究（S32 轉述）未採用。
- Landers 2008 在新條目標 🟡（2010 年前研究，依規格 tech.4 規則）；既有 tech.14／16 仍標 🟢，本次未動。
- Brisswalter & Hausswirth 2008 登錄為 journal-article（簡短綜述，非系統性回顧）。
- 論壇與廠商部落格的 type 沿用既有慣例 web_article，notes 註明論壇或廠商。

## 驗證
- validate.py：0 ERROR，147 WARN（與施作前相同），W009／W011／W028／W029 沒有新增。
- build_knowledge_map.py、build_indices.py：已重生。
- unittest discover tests：255 tests OK。
