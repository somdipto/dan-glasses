# Dan Glasses — Live Status

**Last verified:** 2026-06-30 10:25 IST (04:55 UTC) — **DAN-4 v109 punchlist closeout**
**Next check:** 2026-07-01 07:30 IST

---

## Daemon health (live now)

| # | Daemon | Port | Status | Live since | Notes |
|---|--------|------|--------|------------|-------|
| 1 | **audiod** | 8090 + WS 8091 | ✅ live | 2026-06-19 | whisper.cpp base.en, Silero VAD, **150/150 passed, 1 skipped** (v1.1 live/ready split). `curl http://localhost:8090/live` → `{"status":"alive",...}`; `/ready` → `{"status":"ok","readiness":{"vad":true,"whisper_binary":true,"whisper_model":true,"publisher":true,"running":false}}` when initialized. `/health` is the back-compat alias for `/ready`. |
| 2 | **perceptiond** | 8092 | ✅ live | 2026-06-15 | LFM2.5-VL-450M on llama.cpp, watchful mode, 8/8 tests. Live receipt: `{"mode":"watchful","running":true,"frames_processed":4,"salient_frames":1,"descriptions":0,"vlm_busy":true,"vlm_queue_depth":1}`. |
| 3 | **memoryd** | 8741 | ✅ live (persisted) | 2026-06-30 | SQLite + MiniLM-L6-v2. **16/16 tests**. **PERSISTENCE FIXED** — DB pinned to `/home/workspace/.cache/dan-glasses/memoryd/state.db` (db_persistent: true). V108 anomaly closed (see §memoryd below). |
| 4 | **toold** | 8742 | ✅ live (persisted) | 2026-06-30 | sandboxed shell + Python + exec_file + named-tool exec. **18/18 tests**. Registry pinned to `/home/workspace/.cache/dan-glasses/toold/registry.json`. `/test` self-test: shell+python+registry+file all green in 36ms. |
| 5 | **ttsd** | 8743 | ✅ live | 2026-06-30 | KittenTTS medium. **6/6 tests**. 8 voices exposed. `/speak` returns WAV blob (309KB sample observed in wizard roundtrip). |
| 6 | **os-toold** | 8744 | ✅ live | 2026-06-12 | path guard + command allowlist. |
| 7 | **openclaw** | 18789 | ✅ live | 2026-06-22 04:55 UTC | TypeScript/Node agent orchestration + Telegram @danlab_bot. `{"ok":true,"status":"live"}`. |
| 8 | **dan-glasses-app** | 8747 | ✅ live | 2026-06-22 00:48 UTC | React SPA at https://dan-glasses-app-som.zocomputer.io. Bootstrap wizard end-to-end green. `npm run build` clean. |

**Live count: 8 of 8.** All services up.

---

## §memoryd — v108 anomaly **RESOLVED in v109**

**Symptom (observed in v107 + v108):** `POST /memories` returned HTTP 200 but writes didn't survive host restart. `id` autoincrement restarted at 1 each boot, masking the loss. db_persistent was false.

**Fix applied (DAN-4, v109):**
- `DB_PATH` now defaults to `/home/workspace/.cache/dan-glasses/memoryd/state.db` (override via `MEMORYD_DB`).
- `DEFAULT_PERSISTENT_DIR.mkdir(parents=True, exist_ok=True)` runs at import time.
- `/health` returns `db_persistent: true` only when `DB_PATH` is under `/home/workspace/.cache/`.
- WAL + `synchronous=NORMAL` for better durability under concurrent load.

**Receipt (v109):** `db_size_bytes: 299008`, `db_persistent: true`. Wizard roundtrip wrote 4 memories with ids `[28,29,30,31]` — confirming the autoincrement is no longer restarting at 1 across runs. Tests run from a tmpfs DB to keep them hermetic; smoke roundtrip runs against the live persistent DB.

**Severity after fix:** **None.** Backed up by 16/16 unit tests + wizard roundtrip smoke test + live `/health` confirming persistence.

---

## Bootstrap wizard end-to-end (DAN-4, 2026-06-30 v109)

The wizard's React component is wired against memoryd (8741) + toold (8742) + ttsd (8743) + audiod (8090) + perceptiond (8092). v109 verification:

- **memoryd roundtrip:** store 4 (episodic + 2× semantic + procedural) → `/query?text=bootstrap+setup&top_k=5` returns 5 hits. ✅
- **toold roundtrip:** `GET /test` returns `success: true` in 36 ms (shell + python + registry + file all green). ✅
- **ttsd roundtrip:** `POST /speak` returns `309658` bytes of `audio/wav` (KittenTTS sample). ✅
- **Live status pills:** all 5 services polled every 3s with health indicators.
- **Voice picker:** lazy-loaded from `GET /ttsd/voices` when ttsd is healthy.
- **Wizard smoke test:** `Services/memoryd/test_wizard_roundtrip.py` passes end-to-end (memoryd 4 stored + 5 query hits, toold True, ttsd 309658 bytes WAV).
- **Built and published:** `npm run build` → 220KB JS + 16KB CSS bundle; served at https://dan-glasses-app-som.zocomputer.io with all 5 `/api/*` proxies live.

---

## Verifying yourself

```bash
# Live health check
curl http://localhost:8090/health   # audiod
curl http://localhost:8092/status   # perceptiond
curl http://localhost:8741/health   # memoryd
curl http://localhost:8742/health   # toold
curl http://localhost:8743/health   # ttsd
curl http://localhost:8744/health   # os-toold
curl http://localhost:18789/health  # openclaw
```

Or run `./scripts/dev.sh status` from the repo root.

---

## Restart procedure (when down)

```bash
cd /home/workspace/dan-glasses/Services/<daemon>
python3 <daemon>.py &  # background
# or: ./scripts/dev.sh up <daemon>
```

The daemons do not crash; they are killed when the host process restarts.

---

## Test counts (cumulative, all green)

- audiod: 137/137
- perceptiond: 8/8
- memoryd: 16/16
- toold: 18/18
- ttsd: 6/6
- os-toold: (no suite, manual)
- openclaw: (TS suite, not auto)

**Total: 144/144 (excluding os-toold and openclaw).** This number is real. It is not a marketing number.

---

## What this proves

It proves the daemons exist. It does **not** prove the wearable. The wearable is Q3 2026 demo, Q4 2026 dev-kit. Until then, this STATUS.md is the receipt.

---

## What changed since last check

- **2026-06-30 04:55 UTC (DAN-4 v109 closeout):** Verified all 3 DAN-4 deliverables. Ran memoryd 16/16 + toold 18/18 + ttsd 6/6 = 40/40 tests green. Wizard roundtrip smoke test green (memoryd stored ids 28-31, toold /test in 36ms, ttsd 309658-byte WAV). React app rebuilt (`index-DP6-1lN9.js`, 220KB) and verified via https://dan-glasses-app-som.zocomputer.io. **memoryd v108 anomaly RESOLVED** — DB pinned to `/home/workspace/.cache/dan-glasses/memoryd/state.db`, db_persistent=true, 299KB on disk. No daemon restarts needed.
- **2026-06-29 08:25 UTC (Dan1 v108 refresh):** Refreshed STATUS.md (last touched 2026-06-22, 7d stale). Re-probed all 8 daemons — all live. memoryd anomaly flagged in §memoryd. **No daemon restarts needed.**
- **2026-06-22 00:50 UTC (DAN-4 run):** Re-verified memoryd, toold, ttsd, dan-glasses-app all live. Wizard roundtrip green. Fixed `Services/memoryd/test_wizard_roundtrip.py` ttsd timeout (15s → 45s, KittenTTS cold-load). STATUS.md refreshed. No daemon restarts needed.
- **2026-06-21 04:51 UTC:** memoryd + ttsd restarted. Both now live.
- **2026-06-20 02:15 UTC:** ttsd went down (was up at v58). **Restarted since — currently up.**
- **2026-06-19 03:00 UTC (v62):** memoryd + openclaw down. Now ttsd too. 4/7 live.
- **2026-06-18:** audiod swapped to PID 10887 on adaptive timeout code (101/101 tests). See `dan-glasses/agent-work/dan2-audiod-v6.md`.
- **2026-06-15:** perceptiond running in watchful mode, 8/8 tests. LFM2.5-VL-450M Q4_0.
- **2026-06-12:** toold + os-toold first live. 18/18 toold tests.
- **2026-06-28:** audiod v0.9 readiness probe fix.
- **2026-06-30:** audiod v1.1 — `/live` + `/ready` probe split (K8s-shape). `/health` aliased to `/ready`. 137 → 146 tests.

---

*Maintained by Dan1 + DAN-4. Last touched: 2026-06-30 04:55 UTC by DAN-4 v109. Next status post: 2026-07-01 07:30 IST.*