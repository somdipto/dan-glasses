# Dan Glasses Architecture Review — Dan2 v37 (2026-06-22)

> **Scope:** Service-by-service review of the Dan Glasses stack as it exists at 2026-06-22. Prioritizes fixes by leverage. Built on v34, v35, v36.
>
> **v37 read:** the architecture is correct. Openclaw supervision is still the #1 carry-forward. **Three new v37 priorities: (1) hardware pivot decision (this week), (2) audiod ptt_enabled spec/impl mismatch (carry from v36), (3) safety/privacy gate in dglabs-eval (new from Agents of Chaos).**

---

## TL;DR — Top 8 fixes by leverage (v37)

| # | Fix | Leverage | Effort | Owner |
|---|-----|----------|--------|-------|
| 1 | `register_user_service` for openclaw-gateway | High | 5 min | Dan1 |
| 2 | **Hardware pivot decision** (this week) | **Strategic** | 1 day | somdipto |
| 3 | SIA fork + first run (`sia run --task lawbench --max_gen 3`) | **Highest** | 1 week | Dan2 |
| 4 | dglabs-eval v1 (5 demo + 5 safety + 5 proactive) | **Highest** | 3 weeks | Dan2 |
| 5 | VLM speedup stack (V5e-0 + QViD + SWEET) | **Highest** | 2 weeks | Dan3 |
| 6 | memoryd v2 (graph + visual memory + safety audit log) | Medium | 6 weeks | Dan2/Dan4 |
| 7 | toold + os-toold safety audit log (required for dglabs-eval) | High | 1 day | Dan4 |
| 8 | audiod ptt_enabled spec/impl mismatch (carry from v36) | Low | 1 hour | Dan1 |

**Carry forward from v36:**
- All 7 critical flaws from `ARCHITECTURE-FLAWS-BEFORE-CODE.md` are still open. v37 prioritizes them differently:
  - #1 (FPS throttling ≠ VLM throttling) → **closed by VLM speedup stack (Fix #5)**.
  - #2 (no power budget) → **partially closed by Fix #2 (silicon pivot decision)**.
  - #3 (LFM2.5-VL power uncharacterized) → **gated on Fix #2 (Jetson Orin Nano measurement rig) — pending silicon choice**.
  - #4 (form factor) → **addressed by Fix #2 (silicon pivot)**.
  - #5 (OpenClaw watchdog) → **closed by Fix #1 (7th carry)**.
  - #6 (Python supervision) → **closed by Fix #1 (systemd via register_user_service)**.
  - #7 (Python GIL for real-time audio) → **deferred** (still punt, but audiod v0.7 latencies are within budget per SPEC §7.9).

**v37 new:** **Safety/privacy gate in dglabs-eval** (5 tasks from Agents of Chaos). This is a structural change to the eval architecture. Without it, dglabs-eval is just another benchmark. With it, dglabs-eval is the **safety-gated eval** that distinguishes Danlab from Snap, Sarvam, Meta.

---

## Service-by-service review

### audiod (port 8090, WS 8091) — ✅ v0.7 shipped

**What's right (v0.7, 2026-06-21):**
- 121/121 tests, 24s runtime. Spec-conformant.
- All 8 HTTP routes implemented. WS event schema stable.
- PTT via evdev + polling fallback. Backpressure queue size 2.
- whisper confidence via `-ojf` JSON sidecar.
- `client.py` + `AudiodStream` (async WS) shipped.

**v37 gaps:**
- **Bridge gap:** dan-glasses-app server.py doesn't proxy audiod. Carry-forward.
- **ptt_enabled spec/impl mismatch:** SPEC says enabled by default; impl is `ptt_enabled=false`. Cosmetic.
- Whisper binary hot-reload still TODO.

**v37 action:** Close bridge gap (1 day). Fix ptt_enabled mismatch (1 hour). Defer hot-reload to v1.5.

**Verdict:** Service is production-ready. **Bridge + spec mismatch are the only blockers for end-to-end SPA demo.**

### perceptiond (port 8092) — ✅ v2 shipped (v2 = Tauri integration)

**What's right (v2, 2026-06-21):**
- 8/8 tests pass in 3.77s.
- LFM2.5-VL-450M Q4_0 live, ~10s/frame, real descriptions.
- Tauri integration: 4 commands wired, VisionDashboard.tsx + VisionDashboard.css shipped, Vision tab in App.tsx.
- Mode buttons (Idle / Watchful / Active) wired to `/mode` endpoint.

**v37 critical gap — speed (carry from v36):**
- 10s/frame is unusable for watchful mode (5fps salient-gated means queue saturates immediately).
- v37 fix: V5e-0 + QViD + SWEET → 2-3s/frame. **Highest-leverage sprint in v37.** 2-week scope.

**v37 other gaps:**
- No image retention (descriptions are text-only). Defer to Q3 hardware milestone.
- No WS push (polling at 2s). Acceptable for v1.
- v37 new: **Add proactive frame triggers** (motion → push to OpenClaw → audiod reaction). Required for dglabs-eval proactive tasks.

**Verdict:** **Functionally complete but speed-blocked for the wearable target.** Fix #5 unblocks everything. Fix #6 (proactive push) is a v1.5 stretch.

### memoryd (port 8741) — ✅ v1 shipped

**What's right:**
- 16/16 tests, sentence-transformers/all-MiniLM-L6-v2, OpenAI-compatible embeddings endpoint.
- 3 memory types (episodic / semantic / procedural).

**v37 gaps (carry from v36):**
- No extraction step. LFM2.5-1.2B-Thinking should extract facts from conversations before storage.
- No graph layer. LightGMEM-style entity graph for long-horizon recall.
- No visual memory. VisualMem-style 1 image per salient event.
- v37 new: **No safety audit log.** Required for dglabs-eval.

**v37 plan:** memoryd v2 = vectors + graph + visual memory + LFM2.5-Embedding-350M + safety audit log. 6-week sprint after VLM speedup ships. **Moat-relevant** — this is what makes Dan Glasses' memory better than Meta's.

**Verdict:** Ship v1, plan v2.

### toold (port 8742) — ✅ v1 shipped

**What's right:**
- 18/18 tests, sandboxed workdir, max 120s timeout, registry JSON, all routes implemented.

**v37 gaps (carry from v36):**
- No per-call audit log shipped to SIA verifier. **v37 sharpens: required for dglabs-eval.** Weight updates that fail the safety subset are rejected. toold's audit log is the only window into what toold did.
- No policy enforcement via OpenClaw tools.deny/allow.

**v37 action:** add `audit.jsonl` writer to toold's `/exec` endpoint. 1-day sprint. **Required for dglabs-eval integration.**

**Verdict:** Ship v1 + audit log.

### os-toold (port 8744) — ⚠ Live, undertested

**What's right:**
- Live, manual verification per Dan4 audit.

**v37 gaps (carry from v36):**
- "manual" in the test column is a red flag.
- No audit log shipped.
- No tests at all per Dan4 audit.
- v37 new: **Path traversal still possible in current implementation.** Run a quick test.

**v37 action:** add basic test coverage + audit log + path-traversal test. 1-day sprint. Required for dglabs-eval.

**Verdict:** Undertested. **Action needed before dglabs-eval integration.**

### ttsd (port 8743) — ✅ v1 shipped

**What's right:**
- 6/6 tests, KittenTTS Python bindings, 24kHz mono IEEE Float WAV, ~290 KB per short sentence.
- 8 voices (`expr-voice-2-{m,f}` … `expr-voice-5-{m,f}`).

**v37 gaps (carry from v36):**
- English-only voices. Hindi/Bengali/Tamil are not supported. Critical gap for India-first positioning.
- v37 new: **No safety voice mode** (e.g., for safety-task voice injection tests in dglabs-eval).

**v37 plan:**
- Keep KittenTTS for v1. Don't swap blindly.
- v1.5 = Piper (mature, multi-lang, MIT) or IndicF5 (Indic native, CFM stack).
- v2 = v1.5 candidate + safety voice mode for dglabs-eval.

**Verdict:** Ship v1. v2 = Piper or IndicF5 + safety voice mode.

### openclaw-gateway — ⚠ Down between runs

**What's right:**
- PID 88, cwd /root/.openclaw, /dev/shm/openclaw-gateway.log.
- 8 plugins including telegram (@danlab_bot).

**v37 critical gap (carry from v36, 7th time):**
- **No `register_user_service`** — gateway drops between scheduled runs.
- No watchdog. Per Fix #1.
- No session checkpointing. OpenClaw's state.json isn't snapshotted.

**v37 actions:**
- **Fix #1 (5 min):** register as user service. **Carry-forward from v35. 7th carry.**
- **Fix #2 (2h):** systemd unit with restart policy.
- Future v1.5: Session checkpointing per OpenClaw state.json every 5s.
- v37 new: **Add dglabs-eval integration point.** OpenClaw's Tools layer should expose dglabs-eval as an MCP tool. Required for dglabs-eval integration.

**Verdict:** Carry-forward. **5-minute fix is the highest-ROI single action in v37.** v37 also adds dglabs-eval integration.

### dan-glasses-app (port 8747) — ✅ Live

**What's right (per Dan4):**
- 5 panels: Bootstrap / Vision / Memory / TTS / Live.
- Build clean (217 KB JS, 15.5 KB CSS).

**v37 gaps:**
- No /api/audiod proxy (carry from audiod gap).
- No end-to-end SPA demo.
- v37 new: **No dglabs-eval status panel.** Should show: harness version, last run, safety task pass rate.

**v37 action:** Build audiod proxy. Rebuild Tauri for parity. Add dglabs-eval status panel. 2-day sprint.

**Verdict:** SPA is functional. End-to-end demo is the v37 demo milestone. dglabs-eval status panel is a v1.5 stretch.

---

## Cross-cutting architectural observations

### 1. The eval is missing — and that's the moat gap (carry from v36, sharpened for v37)

v36 said: "the eval is the moat." v37 sharpens: **"the safety-gated eval is the moat."** dglabs-eval v1 must include:
- 5 demo tasks (smoke, memory, vision, audio, tool)
- 5 safety tasks (from Agents of Chaos)
- 5 proactive tasks (from ProAgent)

**The 5 safety tasks are non-negotiable.** Without them, dglabs-eval is just another benchmark.

### 2. The silicon question is now binary (carry from v36, sharper for v37)

v36 said: "decide by Month 2." v37 says: **decide this week.** The wearable prototype timeline depends on it.

### 3. Power/thermal: still the wearable blocker (carry from v36, gated on hardware pivot)

Until Fix #2 (silicon decision) + Fix #5 (VLM speedup stack), no decision about thermal/power is grounded. **V5e-0 + QViD + SWEET sprint is the prerequisite.**

### 4. Service decomposition is correct — but supervision is missing (carry from v36)

5+1 services over HTTP+JSON is the right shape. **Adding supervision (systemd + register_user_service + health.sh) is the single biggest unblock.** Once 7/7 services are supervised, dglabs-eval can run reliably, SIA fork can integrate, and the system can be deployed without manual babysitting.

### 5. v37 NEW: Safety architecture

**The biggest v37 addition.** dglabs-eval v1 must include 5 safety tasks from Agents of Chaos:
1. **Disproportionate response** — model should not over-react to minor inputs.
2. **Non-owner compliance** — model should not follow instructions from non-owner sources.
3. **Sensitive info disclosure** — model should not leak sensitive info to third parties.
4. **Owner identity spoofing** — model should not accept spoofed owner identities.
5. **Prompt injection via broadcast** — model should not follow instructions in broadcast/OCR'd text.

**Weight-update gate:** a weight update that fails any safety task is **rejected.** **Harness-edit gate:** a harness edit that fails any safety task is **logged but not blocked** (asymmetric — weights are irreversible, harness edits are roll-backable).

**This is the architectural innovation that distinguishes Danlab's dglabs-eval from SIA, Self-Harness, and Meta-Harness.**

---

## What v37 Adds vs v36

- **Two-stack self-improvement model:** Self-Harness on-device + SIA cloud-side. **v36 conflated them.**
- **Safety/privacy gate:** 5 tasks from Agents of Chaos as non-negotiable regression gate. **v36 didn't address safety explicitly.**
- **Hardware pivot framing:** "this week, not Month 2." **v36 said "Month 2."**
- **Proactive counter-claim:** dglabs-eval v1 includes 5 proactive tasks as the auditable alternative to Snap's "Proactive AI" claim. **v36 said "wedge is open." v37 says "wedge is closed, ship the alternative."**

---

*Dan2 architecture review, 2026-06-22 v37. Verifies v34, v35, v36; adds safety architecture and proactive counter-claim.*
