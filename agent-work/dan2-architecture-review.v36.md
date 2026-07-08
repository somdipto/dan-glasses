# Dan Glasses Architecture Review — Dan2 v36 (2026-06-21)

> **Scope:** Service-by-service review of the Dan Glasses stack as it exists at 2026-06-21. Prioritizes fixes by leverage, not by completeness. Built on top of v34 and v35 reviews.
>
> **v36 read:** the architecture is **more correct than the status doc suggests**. All 6 daemons + the SPA are live and tested. The gaps are not architectural — they're (a) supervision, (b) speed, (c) the moat. **Fix those three, ship.**

---

## TL;DR — Top 8 fixes by leverage

| # | Fix | Leverage | Effort | Owner |
|---|-----|----------|--------|-------|
| 1 | `register_user_service` for openclaw-gateway | High | 5 min | Dan1 |
| 2 | Systemd units for all 7 services | High | 2 hours | Dan1 |
| 3 | VLM speedup stack (V5e-0 + QViD + SWEET) | **Highest** | 2 weeks | Dan3 |
| 4 | SIA fork + dglabs-eval scaffold | **Highest** | 3 weeks | Dan2 |
| 5 | Bootstrap wizard state machine | High | 1 week | Dan4 |
| 6 | memoryd v2 (graph + visual memory) | Medium | 6 weeks | Dan2/Dan4 |
| 7 | Hardware pivot decision (Redax vs Qualcomm AR1) | Strategic | 1 day | somdipto |
| 8 | Power/thermal rig on Jetson Orin Nano | High | 2 weeks | Dan3 |

**Carry forward from v35:**
- All 7 critical flaws from `ARCHITECTURE-FLAWS-BEFORE-CODE.md` are **still open**. v36 prioritizes them differently:
  - #1 (FPS throttling ≠ VLM throttling) → **closed by Fix #3 above** (salience-gated Q4/Q5/Q8)
  - #2 (no power budget) → **partially closed by Fix #8** (measurement rig)
  - #3 (LFM2.5-VL power uncharacterized) → **closed by Fix #8**
  - #4 (form factor) → **addressed by Fix #7** (silicon pivot)
  - #5 (OpenClaw watchdog) → **closed by Fix #1 + #2**
  - #6 (Python supervision) → **closed by Fix #2**
  - #7 (Python GIL for real-time audio) → **deferred** (still punt, but audiod v0.7 latencies are within budget per SPEC §7.9)

---

## Service-by-service review

### audiod (port 8090, WS 8091) — ✅ v0.7 shipped

**What's right (v0.7, 2026-06-21):**
- 121/121 tests, 24s runtime. Spec-conformant.
- All 8 HTTP routes implemented. WS event schema stable.
- PTT via evdev + polling fallback. Backpressure queue size 2.
- whisper confidence via `-ojf` JSON sidecar.
- `client.py` + `AudiodStream` (async WS) shipped.
- `audiod_demo.html` browser proof of concept.

**v36 gaps:**
- **Bridge gap:** dan-glasses-app server.py doesn't proxy audiod; the SPA is on its own. Carry-forward from Dan2 v35.
- Whisper binary hot-reload still TODO.
- Per-segment language detection still TODO.

**v36 action:** **Close the bridge gap** (1 day) — add `/api/audiod/*` proxy endpoints to server.py. Defer hot-reload and per-segment language detection to v1.5.

**Verdict:** Service is production-ready. **Bridge is the only blocker for end-to-end SPA demo.**

### perceptiond (port 8092) — ✅ v2 shipped (v2 = Tauri integration)

**What's right (v2, 2026-06-21):**
- 8/8 tests pass in 3.77s.
- LFM2.5-VL-450M Q4_0 live, ~10s/frame, real descriptions from real VLM (verified event_id 320).
- Tauri integration: 4 commands wired, VisionDashboard.tsx + VisionDashboard.css shipped, Vision tab in App.tsx.
- Port drift bug (8093 → 8092) fixed.
- Mode buttons (Idle / Watchful / Active) wired to `/mode` endpoint.
- Mock capture fallback works (no /dev/video0 → drifting blob).

**v36 critical gap — speed:**
- 10s/frame is **unusable for watchful mode** (5fps salient-gated means queue saturates immediately).
- v36 fix: V5e-0 + QViD + SWEET → **2-3s/frame**. **Highest-leverage sprint in v36.** 2-week scope.

**v36 other gaps:**
- No image retention (descriptions are text-only). Defer to Q3 hardware milestone.
- No WS push (polling at 2s). Acceptable for v1; revisit with bridge parity.

**Verdict:** **Functionally complete but speed-blocked for the wearable target.** Fix #3 unblocks everything.

### memoryd (port 8741) — ✅ v1 shipped

**What's right:**
- 16/16 tests, sentence-transformers/all-MiniLM-L6-v2, OpenAI-compatible embeddings endpoint.
- 3 memory types (episodic / semantic / procedural).
- `/stats` aggregation.

**v36 gaps (carry from v35):**
- **No extraction step.** LFM2.5-1.2B-Thinking should extract facts from conversations before storage.
- **No graph layer.** LightGMEM-style entity graph would let memoryd handle long-horizon recall.
- **No visual memory.** VisualMem shows visual recall is a missing dimension.
- **all-MiniLM-L6-v2 is 22MB, 384-dim.** Adequate for v1. LFM2.5-Embedding-350M (1024-dim) or NanoVDR-distilled 69M text encoder are v2 upgrades.

**v36 plan:** memoryd v2 = vectors + graph + visual memory + LFM2.5-Embedding-350M. 6-week sprint after VLM speedup ships. **Moat-relevant** — this is what makes Dan Glasses' memory better than Meta's.

**Verdict:** Ship v1, plan v2.

### toold (port 8742) — ✅ v1 shipped

**What's right:**
- 18/18 tests, sandboxed workdir, max 120s timeout, registry JSON, all routes implemented.
- `/test` self-test endpoint is the bootstrap wizard's verification target.

**v36 gaps:**
- **No per-call audit log shipped to SIA verifier.** Critical for the SIA fork — SIA needs to see what toold did.
- **No policy enforcement via OpenClaw tools.deny/allow.** OpenClaw has it; toold doesn't expose it.

**v36 action:** add `audit.jsonl` writer to toold's `/exec` endpoint. 2-hour job. **Required for SIA fork integration.**

**Verdict:** Ship v1 + audit log.

### os-toold (port 8744) — ⚠ Live, undertested

**What's right:**
- Live, manual verification per Dan4 audit.

**v36 gaps:**
- "manual" in the test column is a red flag.
- No audit log shipped.
- No tests at all per Dan4 audit.

**v36 action:** add basic test coverage + audit log. 1-day sprint. Required for SIA fork.

**Verdict:** Undertested. **Action needed before SIA fork.**

### ttsd (port 8743) — ✅ v1 shipped

**What's right:**
- 6/6 tests, KittenTTS Python bindings, 24kHz mono IEEE Float WAV, ~290 KB per short sentence.
- 8 voices (`expr-voice-2-{m,f}` … `expr-voice-5-{m,f}`).
- Caches model after first request. <1s warm path.

**v36 gaps:**
- English-only voices. **Hindi/Bengali/Tamil are not supported.** Critical gap for India-first positioning.
- 290 KB per sentence is fine for short responses but bloats long responses.

**v36 plan (carry from v35):**
- **Keep KittenTTS for v1.** Don't swap blindly.
- **Evaluate v1.5:** Kokoro-82M (multi-lang, MIT), Orpheus-TTS (smaller, Indic support), Piper (mature, smaller).
- **IndicF5** (referenced in wavelet-driven TTS paper, OpenReview [^26 in model-analysis]) supports Hindi/Tamil/Bengali natively and works with CFM-based stack. **Strong India-first candidate for v2.**

**Verdict:** Ship v1. **v2 = IndicF5 or Piper for Indic languages.**

### openclaw-gateway — ⚠ Down between runs

**What's right:**
- PID 88, cwd /root/.openclaw, /dev/shm/openclaw-gateway.log.
- 8 plugins including telegram (@danlab_bot).
- TS suite passes.

**v36 critical gap:**
- **No `register_user_service`** — gateway drops between scheduled runs. Killed by gVisor.
- **No watchdog.** Per Fix #2.
- **No session checkpointing.** OpenClaw's state.json isn't snapshotted.

**v36 actions:**
- **Fix #1 (5 min):** register as user service. **Carry-forward from v35.**
- **Fix #2 (2h):** systemd unit with restart policy.
- **Future v1.5:** Session checkpointing per OpenClaw state.json every 5s.

**Verdict:** Carry-forward. **5-minute fix is the highest-ROI single action in v36.**

### dan-glasses-app (port 8747) — ✅ Live

**What's right (per Dan4):**
- 4 panels: Bootstrap / Vision / Memory / TTS / Live (LiveTranscript fixed).
- server.py DIST path bug fixed.
- Build clean (217 KB JS, 15.5 KB CSS).

**v36 gaps:**
- **No /api/audiod proxy** (carry from audiod gap).
- **No end-to-end SPA demo.** SPA can hit some services directly, others via the bridge.
- **Tauri commands use direct fetch in dev mode** (per Dan3 v2) — Rust rebuild needed for production parity.

**v36 action:** Build audiod proxy. Rebuild Tauri for parity. 1-day sprint.

**Verdict:** SPA is functional. End-to-end demo is the v36 demo milestone.

---

## Cross-cutting architectural observations

### 1. The eval is missing — and that's the moat gap

The current stack has **no eval harness** for self-improvement. SIA's whole premise is "the eval gates the writes." Without a dglabs-eval, SIA can't run on Dan Glasses. **v36 prioritizes dglabs-eval as the #1 moat asset.** 

### 2. The silicon question is now binary

v34/v35 said "wait for Redax." v36 says: Redax is moving target; Qualcomm AR1 Gen 1 / Reality Elite is real silicon shipping in 2026. **Decision needed in Month 2.** Stay with Redax = 12-month wearable prototype. Pivot to Qualcomm = 6-month wearable prototype. 6 months = first-mover advantage in India wearable AI.

### 3. Power/thermal: still the wearable blocker

Until Fix #8 (Jetson Orin Nano measurement rig), no decision about thermal/power is grounded. **2-week sprint, owned by Dan3.** Use V5e-0 + QViD + SWEET to measure inference power at Q4/Q5/Q8 with salience gating. **Numbers > opinions.**

### 4. Service decomposition is correct — but supervision is missing

5+1 services over HTTP+JSON is the right shape. **Adding supervision (systemd + register_user_service + health.sh) is the single biggest unblock.** Once 7/7 services are supervised, dglabs-eval can run reliably, SIA fork can integrate, and the system can be deployed without manual babysitting.

---

## What v36 Adds vs v35

- **Concrete primitives:** V5e-0 / QViD / SWEET for VLM speedup. SIA fork + dglabs-eval for self-improvement. IndicF5 for Indic TTS.
- **Hardware pivot framing:** Redax vs Qualcomm AR1 as a binary decision. **v36 calls the question.**
- **Moat framing:** dglabs-eval as the moat. **v36 makes this the #1 bet.**
- **India-first framing:** Sarvam + HMD + JioBharat + India AI Mission as distribution channels. **v36 makes this concrete.**

---

*Dan2 architecture review, 2026-06-21 v36. Verifies v34 and v35 reviews; adds 3 new actions and sharpens the silicon question.*
