# Plan-check 交接 — 週期化知識整合 + 白話重寫 + 模組化

> 產出：Opus plan-check（2026-06-08）。**這是交接單，下個 session 從這裡接手。**
> 接手第一步：讀本檔 → 跑 `/implement` 轉成步驟清單 → 依序執行。
> **接手前置動作**：把本檔路徑各補一行指標到 `my-site/HANDOFF.md`、`TheVortexProject/HANDOFF.md`（本 session 配額將盡，未同步全部 HANDOFF；swim-coach 已指）。
> 模型要求：plan-check / code-audit 須 Opus；本檔已由 Opus 完成 plan-check。

---

## 背景（用戶原話）

1. 整合所有週期化訓練相關資訊
2. 用字整理後用「Claude 自己的白話說法」輸出，不照搬書/文獻敘述（用戶反映 Bompa 跨運動寫太抽象、看不懂）
3. 可整合的全部整合，不散落各地
4. 資料模組化：查詢/檢索/索引一目了然，AI 與人都能快速搜到

範圍是「一源兩消費」全鏈，**不只 swim-coach**：canonical 源 + my-site vortex 呈現 + swim-coach 唯讀反查。

---

## 現況footprint（Haiku 探勘 2026-06-08）

- **源**：`TheVortexProject/canonical/periodization/{structure,taper,zones}.yaml`（5 domain 之一；其餘 development/instructional/perception/technica）。週期化內容也散見 `canonical/development/matrix.yaml`（年度計畫 links）、`canonical/perception/free.yaml`（taper ref）。
- **sync**：`my-site/tools/sync_vortex.py` 的 `sync_periodization()`（L622–664）**逐字 pass-through，無 transform**，寫到 `my-site/data/periodization/{structure,taper,zones}.yaml`；SHA-256 狀態存 `vortex_sync_state.json`。
- **my-site 呈現**：`layouts/vortex/vortex-periodization.html`（Hugo template，讀 `hugo.Data.periodization.*`）。另有 `content/library/essentials-of-strength-training/ch20-21/*.md`（NSCA 力量訓練書，**不同來源，本任務不碰**）。
- **swim-coach**：`scripts/build_knowledge_index.py` 的 `parse_periodization_file()` 把每個帶 `id` 節點出一列進 `periodization` + `periodization_fts`；`_pz_collect_text()` 會收集**所有非 skip 欄位**進 summary。`rules/periodization.yaml`（教練決策層，已填 canonical 轉錄欄）。
- **Hestia vault 週期化相關**：344 檔中僅 ~2 篇直接相關（`RAW/PMID-35500602`（taper/神經肌肉疲勞）、`PMID-38162699`（load-velocity））+ 對應 digests。**不值得整批匯入**。

---

## 關鍵架構決策（plan-check 的核心結論）

**白話層加在 canonical YAML 節點內（新增 `plain_zh` 欄位），不另開獨立白話模組。**

理由（直接對映 sync 機制）：sync 是逐字 pass-through，所以在 canonical 節點加 `plain_zh` →
- my-site 自動拿到（只需改 template 呈現該欄）；
- swim-coach 自動拿到（`_pz_collect_text` 已收所有非 skip 欄 → 白話文字自動進 FTS）。

→ 一次寫在源頭、兩消費端繼承，完全滿足「不散落 + 單一真相 + 模組化檢索」。獨立白話模組會製造第二份真相、破壞 source_id 反查，反而散落。

**模組化/檢索**：source_id 反查鍵已存在（如 `periodization.structure.annual.bicycle`）。再加一個**概念目錄檔** `canonical/periodization/_index.yaml`：列出全部 source_id + 一行白話摘要 + cert，當人/AI 的「一目了然」入口。

---

## 步驟 1｜目標狀態

完成後：`canonical/periodization/` 內每個週期化概念節點都有一段 **Claude 白話 `plain_zh`**（保留原 `source`/數字/`cert` 標記，白話為**加法不取代**）；新增 `_index.yaml` 概念目錄當檢索入口；sync 後 my-site vortex-periodization 頁面顯示白話、swim-coach FTS 可用白話詞命中；散在 development/perception 的週期化片段以 links 指回 canonical 單一真相，不重複定義。**一句話：週期化知識集中在 canonical 一處、有白話有索引，人讀得懂、AI 查得到、數字仍可反查 Bompa 原文。**

## 步驟 2｜影響範圍

### 2a. 會動到
- `TheVortexProject/canonical/periodization/{structure,taper,zones}.yaml`（每節點加 `plain_zh`）
- `TheVortexProject/canonical/periodization/_index.yaml`（**新檔**，概念目錄）
- `my-site/tools/sync_vortex.py`（若 `_index.yaml` 也要同步，`sync_periodization()` 加一檔；plain_zh 因 verbatim 不需改 sync）
- `my-site/data/periodization/*`（sync 產物，自動）
- `my-site/layouts/vortex/vortex-periodization.html`（呈現 `plain_zh`）
- `swim-coach/scripts/build_knowledge_index.py`（**可能微調**：讓 `plain_zh` 優先進 title/summary；若不調，白話仍會進 summary，僅排序差異）
- `swim-coach` 的 `vendor/vortex` submodule pointer（bump 到含白話的 canonical commit）
- 三方 HANDOFF（收尾）

### 2b. 明確不在範圍內
- 其餘 4 個 canonical domain（perception/development/instructional/technica）**不做白話化**（只做週期化）
- my-site `content/library/essentials-of-strength-training/*`（NSCA 書，不同來源）
- Hestia vault 88 篇整批匯入（最多引用 PMID-35500602 taper 一篇強化既有 taper 節點，標 🟢）
- `rules/periodization.yaml` 的 `# JUDGMENT` 欄（教練默會判斷，仍等 Hang）

### 2c. 服務範圍
- **誰會用**：my-site 公開面向學員/家長/教練（白話對這端最關鍵）；swim-coach 課表引擎（AI 反查）；Hang 自己。
- **跑在什麼機器**：my-site 為 Hugo 靜態站（build 後部署，無 runtime trigger）；swim-coach 本機。無排程/trigger 議題。
- **驗證標準**：my-site `hugo` build 綠 + 頁面實際顯示白話；swim-coach `uv run pytest` 71/71 + 白話詞 FTS 命中。

### 2d. 分散點掃描
- **週期化定義散落 3 處**：canonical/periodization（主）、development/matrix.yaml（年度計畫 links）、perception/free.yaml（taper ref）。本次**只在 canonical/periodization 加白話**；另 2 處確認是 links 引用非重複定義 → 不複製白話，維持單一真相。
- **同一份 periodization YAML 被 3 處讀**：sync_vortex.py、build_knowledge_index.py、my-site template。加 `plain_zh`（純加欄）對三者皆向後相容（YAML 多一欄不破壞既有 parser）。
- **`_index.yaml` 新檔**若要進 swim-coach FTS：build_knowledge_index 的 glob `*.yaml` 會自動掃到 → 需確認 parser 對「純目錄檔」不會出垃圾列（可能要在 parser skip `_index.yaml` 或讓它出摘要列）。**這是要在 implement 時決定的點。**

## 步驟 3｜執行路徑
1. **白話重寫 canonical 3 檔**：逐節點加 `plain_zh`，過 Vortex 三關校正（符合研究 + 反問 + 反推），保留 source/數字/cert。工具：Edit。前置：已讀完 3 檔現況。
2. **建 `_index.yaml`**：掃 3 檔所有 source_id，每筆一行 `{source_id, plain_summary, cert, file}`。工具：Write（可先用 script 抽 source_id 再人工補白話摘要）。
3. **（選）引用 Hestia taper 文獻**：在 taper.yaml 既有節點補 PMID-35500602 佐證，標 🟢。
4. **canonical 端驗證**：`yaml.safe_load` 全 3 檔 + `_index.yaml`；commit TheVortexProject。前置失敗：YAML 壞 → 修再 commit。
5. **sync 到 my-site**：跑 `python my-site/tools/sync_vortex.py`；若同步 `_index.yaml` 先改 `sync_periodization()`。驗 my-site/data 更新 + SHA 變。
6. **my-site 呈現**：改 `vortex-periodization.html` 顯示 `plain_zh`（缺欄要 fallback 原文）；`hugo` build 驗綠。
7. **swim-coach 接線**：`git submodule update --remote vendor/vortex` bump pointer；`uv sync`；（選）微調 build_knowledge_index 讓 plain_zh 優先 + 處理 `_index.yaml`；重建索引；`uv run pytest` 71/71 + 加白話 FTS 測試。
8. **收尾**：三方 HANDOFF 更新 + commit（各 repo，不 push，依 DELEGATION Phase 3）。

## 步驟 4｜預期風險
**4a 執行時**
- **R1 白話化扭曲原意/掉數字**（步驟 1）：重寫時把「降 41–60%」寫成「大幅降低」之類，或漏掉 cert 標記 → 反幻覺承接破功。根據：用戶要「白話」與專案要「數字可反查」天然張力。
- **R2 sync verbatim 把半成品推上公開站**（步驟 5）：白話只寫一半就 sync + hugo build → my-site 公開面出現空/亂白話欄。根據：sync 無 transform、my-site 是公開窗口。
- **R3 `_index.yaml` 進 swim-coach 出垃圾 FTS 列**（步驟 7）：build_knowledge_index glob `*.yaml` 會掃到目錄檔，parser 對非標準結構可能出 source_id=None 或重複列 → 污染索引/測試。根據：2d 分散點掃描第 3 點。

**4b 結構性**
- 並發：不適用（知識撰寫，無並發寫）。
- 邊界：節點缺 `plain_zh` → my-site template 與 swim-coach parser 都須優雅 fallback（不可 crash/空白）。
- 持久化：canonical YAML 加欄=純加法，無 migration；swim-coach 索引每次重建；my-site data 由 sync 重生。**無破壞性 schema 變更。**
- 外部輸入驗證：白話是撰寫內容非 runtime 輸入；但 swim-coach `engine/validators.py` 做 source_id 反查 → 加欄不影響（source_id 不變）。
- 命令注入：不適用。
- 跨狀態一致性：無 status 欄變更。

## 步驟 5｜風險預案
- **R1**：提前偵測 = 每條 `plain_zh` 旁保留原 `source`/數字欄，diff 時並排比對；過 Vortex 三關（符合研究 + 反問 + 反推）。發生後 = 抓出扭曲條目，以原文重寫，不靠記憶。
- **R2**：提前偵測 = canonical 全部白話寫完 + commit **才** sync；sync 前 grep 確認無空 `plain_zh:`。發生後 = 回退 my-site/data（sync 可重跑覆蓋）+ 暫不 hugo deploy。
- **R3**：提前偵測 = 建 `_index.yaml` 後先 `python build_knowledge_index.py` 看 periodization 列數有無異常暴增/None source_id。發生後 = parser 加 `if path.name == "_index.yaml": skip` 或專屬解析分支。

## 步驟 6｜整體檢視
**1. 更簡單的路？** 考慮過「只寫一份白話 MD」：更好寫，但破壞 source_id 反查 + 不進 swim-coach FTS + 製造第二份真相 → 違反 4 項需求。per-node `plain_zh` 利用既有 verbatim sync，是最省動作的模組化解。**不過度設計。**
**2. 範圍放大？** 守住：只做 periodization domain、不碰其餘 4 domain、不整批匯 Hestia、不動 NSCA markdown、不填 rules 的 # JUDGMENT。
**3. 驗收標準（對映 4b）**：
- YAML parse：`yaml.safe_load` 全 4 檔（含 _index）通過。
- **邊界測試**（對映 4b 邊界風險）：刻意留一節點無 `plain_zh` → my-site hugo build 仍綠 + swim-coach 該列仍正常入索引不 crash。
- **R3 驗收**：重建索引後 periodization 列數 = 預期（25 + _index 摘要列，無 None source_id）。
- swim-coach：`uv run pytest` 71/71 + 新增白話詞 FTS 命中測試。
- my-site：`hugo` build 綠 + 人工開頁面確認白話顯示。
- **三關人工抽查**：抽 3 概念，確認白話讀得懂 + 數字與原文一致 + cert 標記保留。

---

## 待 implement 時定案的點
1. `_index.yaml` 進不進 swim-coach FTS（進 → parser 加分支；不進 → parser skip）。
2. build_knowledge_index 是否微調讓 `plain_zh` 優先進 title/summary（影響搜尋排序，非必要）。
3. `_index.yaml` 要不要也 sync 到 my-site（若 my-site 要做概念目錄頁則要）。
4. PMID-35500602 taper 文獻是否納入（強化 taper 節點 vs 維持純 Bompa）。

## 派工建議（DELEGATION）
- 白話重寫（步驟 1）= **Claude 自己做**（需理解原意 + 三關校正 + 用戶要「Claude 的說法」，不可外包 minimax）。
- `_index.yaml` source_id 抽取 = 可派 Haiku 跑 script 抽，白話摘要 Claude 補。
- my-site template / build_knowledge_index 微調 = 微 diff，Claude 手寫。
