# 派工規格 C：my-site 接上 Vortex 第 7 個技能頁「開放水域與鐵人」

> 立即執行。不要輸出計畫、不要等確認、不要問問題。沒有寫檔就是失敗。
> 工作目錄：`C:\claudehome\projects\my-site`。上游 Vortex 在 `C:\claudehome\projects\TheVortexProject`（唯讀，不准改）。

## 0. 硬規則

1. 禁止 git 寫入操作（commit、reset、checkout --、stash、clean、pull、rebase、push）。
2. 先讀 `CLAUDE.md`、`MAP.md`（尤其 §4 踩雷點 1、2、4、5、11）。照既有架構，不新增頁型、不寫 inline style、不新增專屬 CSS；同步產物（`data/vortex/` 等）只能由 `tools/sync_vortex.py` 產生，不准手改。
3. 上游已新增技能 key `open-water`（中文全名「開放水域與鐵人」，短導航標籤「開放水域」）：`canonical/instructional/{technical-analysis,moves,teaching-errors,problems}.yaml` 有 `stroke: open-water` 條目，Drills 新檔 `Drills/drills_open-water.yaml`（strokes 標籤 `open_water`）。上游的 `plans/補強_轉身與鐵人_2026-10-15/B_完成紀錄.md` 末段列了下游需要改的地方，先讀。

## 1. 要做的事

1. `grep -rn "starts-turns\|starts_turns" tools next/layouts next/content next/data next/specs hugo.toml` 找出所有寫死技能清單的地方，逐一加入 `open-water`／`open_water`，排在 `starts-turns` 之後。已知至少：
   - `tools/sync_vortex.py`：`DRILL_STROKES`，以及 `sync_moves()` 產出的 `data/vortex/<stroke>.yaml`（要多產 `open-water.yaml`）。
   - `tools/build_vortex_links.py`：`MOVE_FILES`、strokes 標籤對照、`NO_LEVEL_STROKES`（open-water 沒有 L 級，比照 starts-turns）、中文標籤。
   - `next/layouts/_partials/vortex/{home,list,rail,stroke,movement}.html` 的順序、標籤、長名對照 dict。
   - `next/content/vortex/_content.gotmpl` 產生技能頁的地方。
   - `next/specs/check.py` 若有寫死 6 個技能頁的斷言，改成 7 個。
2. 跑 `python -X utf8 tools/sync_vortex.py`（上游路徑依它既有設定）→ `python tools/build_vortex_links.py` → `python tools/build_library.py` → `python tools/build_starters.py`。
3. 建置：照 MAP §4.1，`hugo -d <暫存目錄>/cortex --baseURL http://127.0.0.1:1319/cortex/`（不要用 hugo server、不要寫進 public/）。確認：
   - 開放水域頁存在，看得到 premise、動作卡、drill 清單；左欄與 Vortex 首頁都點得到它（不能是孤兒頁）。
   - 起跳轉身頁的新動作與新 drill 也有出現（上游規格 A 新增的）。
4. `python -X utf8 next/specs/check.py` 全部 W 跑一次，全 PASS；原本就 FAIL 的要在紀錄註明，不是你造成的不必修。
5. 寫 `C:\claudehome\projects\my-site\research\vortex-open-water-page-2026-10-15.md`：改了哪些檔、為什麼、check 結果、建置後新頁的網址路徑。
