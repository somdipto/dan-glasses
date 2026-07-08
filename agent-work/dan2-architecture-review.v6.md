# Dan Glasses Architecture Review v6

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-24 11:30 IST
**Status:** v6 — supersedes v1–v5
**Companion to:** `dan2-research-report.v6.md`, `dan2-agi-roadmap.v6.md`
**Live infra referenced:** 8/8 daemons, 144/144 tests, all services verified 11:30 IST this run.

---

## What v6 adds over v5

v5 named reliability as the new moat and memory as engineering. v6 operationalizes both:

1. **Reliability as a typed service contract.** v6 adds a `Reliability` section to every daemon's API schema (calibrated confidence, ECE/Brier, last failure mode, fault-class registry). audiod calibration is the first implementation.
2. **Operative Context surface on memoryd.** v6 adds an explicit `operative_context` table — the memory-derived information that *actually drives behavior*, distinct from raw stored memories. Aligned with the OpenReview "Operative Contexts" 2026 framing.
3. **`proactived` (NEW) added to architecture review.** v5 mentioned it in passing; v6 specifies the surface (calendar + location + time + email fusion), OpenClaw-tool exposure, and the audiod reliability metric it depends on.
4. **`rewardsd` (NEW) — full spec.** v5 mentioned AIE-Bench integration; v6 specifies endpoints, persistence, AIE-Bench / SEAGym harness contracts, and the failure-mode registry.
5. **Failure-mode registry is now a first-class artifact.** arXiv 2606.21090's rise-and-collapse finding means we cannot trust a self-improving agent without a failure-mode registry. audiod RL agent ships with it.
6. **`live_terminal.md` on the Dan Glasses SPA** — recommended (per Dan1 v82). v6 specifies the data flow: audiod confidence → proactived nudges → user-visible audit trail.

---

## Per-service review (v6)

### audiod (port 8090 + WS 8091) — the v6 centerpiece

**State:** ✅ shipped, 123 tests, 48+ min uptime, whisper.cpp base.en + Silero VAD.

**v6 work:**

1. **Confidence calibration RL agent (v6 priority, Deep Dive A).**
   - 4-layer MLP calibration head on frozen whisper.cpp base.en encoder.
   - Reward: Brier score on (prediction, WER-derived ground-truth).
   - 6-week build, 6-week eval. AIE-Bench + SEAGym submission target Sep 30, 2026.
   - arXiv pre-print target Aug 15, 2026.
   - Failure-mode registry: track `failure_class ∈ {silence, music_overlap, OOD_accent, low_SNR, hallucinated_token}` per event. arXiv 2606.21090 rise-and-collapse finding means we cannot trust the loop without a fault-class registry.
   - Implementation: extend `transcription.py` with `CalibrationHead` class; expose `/calibration/{predict, ingest, eval}` endpoints.

2. **`/reliability` endpoint (v6).** Returns ECE, Brier, accuracy-on-confidence-bin histogram, last failure class. Updates every 100 events.

3. **`/failure_mode` endpoint (v6).** Returns rolling failure-mode distribution, last 1000 events.

4. **Whisper binary hot-reload** (deferred to v0.9). Currently `/reload` re-resolves the path but doesn't restart the subprocess.

5. **WS server prunes dead clients (v6 fix).** Spec says "drops >60s idle" but implementation only pings at 30s. Add explicit `last_pong_at` check. Failure mode: NAT'd client holds slot indefinitely.

6. **Adaptive whisper timeout (deferred to v0.9).** Long utterances block the queue. Add `transcribe_queue_depth` to `/status` and oldest-frame drop when queue > N.

### perceptiond (port 8092) — model swap + on-device NPU path

**State:** ✅ live, 8/8 tests, watchful mode, LFM2.5-VL-450M Q4_0. ~10–15s/frame on CPU. Dan3 v5 work in progress (503 "no capture" race fix, /stream and /frame.jpg endpoints, VisionDashboard viewfinder).

**v6 work:**

1. **VLM model swap evaluation.** Eval OmniVLM-968M Q4_K_M (9× token compression → ~1.1s/frame) vs LFM2.5-VL-450M vs Gemma 3 4B on the existing test set. Measure watchful-mode queue depth and battery proxy. Decision Aug 1, 2026; swap by Oct 1, 2026. **v6 also adds:** V5e-0 self-speculative decoding (1.89× speedup on VLMs, OpenReview 2026 — zero training cost, only verifier-text-side drafting). Apply on top of whichever VLM ships.
2. **Token pre-processing.** CondenseVLM (submodular coverage + spatially-constrained merge, OpenReview 2026) and QViD (query-vision decomposition, OpenReview 2026) are training-free token condensation paths. Eval on perceptiond's salience-gated frames. Halves encoder time.
3. **Power-state machine.** `idle` should unload the VLM from RAM. Coordinated by OpenClaw heartbeat. Critical for wearable form factor (1.6W idle → 0.3W drowsy draw).
4. **Frame ring buffer (50 frames).** "What did you see?" queries are currently unanswerable. Add redaction-by-default frame retention.
5. **NPU offload path.** perceptiond is CPU-only. Redax NPU is the v2 acceleration target. v6: spec the NPU abstraction layer (llama.cpp + QNN backend or CoreML export) so model swaps don't re-write the inference path.

### memoryd (port 8741) — v2 rebuild around AEL + DPCM + LLM-Wiki + Operative Context + Reliability

**State:** ✅ live, 16/16 tests, SQLite + MiniLM-L6-v2 semantic recall. Roundtrip smoke green.

**v6 adds two new surfaces to the v5 plan:**

1. **`operative_context` table.** Stores the memory-derived information that *actually drives behavior* (per OpenReview "Operative Contexts" 2026). Different from stored memory. Key fields: `memory_ids[]`, `selected_at`, `selection_rationale`, `confidence_score`, `supersedes_operative_context_id`. **This is what gets exposed to proactived for nudges.**
2. **`/reliability` endpoint.** Exposes memoryd's own reliability: retrieval ECE, Brier over (top-1 confidence, true relevance), recall@5.

**v6 build sequence (8 weeks, unchanged from v5 but now with explicit weeks for new surfaces):**

| Week | Component | Deliverable |
|---|---|---|
| 1 | int8 quantization on existing semantic store | 4× memory win |
| 2 | DPCM provenance graph schema + migration | New tables, backward-compat read API |
| 3 | AEL fast Thompson bandit (5 modes) | Bandit over {semantic, episodic, procedural, graph, reranked} |
| 4 | Slow LLM reflection (nightly, opt-in) | New retrieval modes injected on plateau |
| 5 | LLM-Wiki reconsolidation (nightly) | Episodic → semantic distillation |
| 5.5 | **operative_context table + selection-rationale API** | NEW v6 |
| 6 | OpenClaw-memory adapter + reliability endpoint | `/memory/{bootstrap,semantic}` + `/reliability` |
| 7 | LongMemEval + PersonaMem-v2 submission | Public, auditable numbers |
| 8 | Tune + harden + deploy | memoryd v2 live |

### toold (port 8742) — ship, harden, no change

**State:** ✅ live, 18/18 tests, sandboxed shell + Python exec.

**v6 additions:**

1. **`/reliability` endpoint** — execution success rate, sandbox escape attempts blocked, command-allowlist denials.
2. **Socratic-SWE-style trace-derived skills (Q4 2026, per v5).** No v6 architectural change.

### ttsd (port 8743) — KittenTTS → Kokoro-82M swap (1-week decision)

**State:** ✅ live, 6/6 tests, KittenTTS medium `expr-voice-2-m`. Cold-path latency ~3.8s.

**v6 work:**

1. **Swap KittenTTS → Kokoro-82M (v5 commitment, v6 confirms).** Apache 2.0 license, 21 voices, 24kHz, MOS 4.45, 327MB, runs on Raspberry Pi. Sub-20ms TTFA on warm cache. Deploy by Jul 15, 2026.
2. **`/reliability` endpoint** — TTS intelligibility confidence (per OpenReview reliability literature), cold-vs-warm latency, voice-consistency check.
3. **Multi-engine router (Kokoro for English, Piper for non-English, MisoTTS for batch).** Language auto-detect.
4. **WebGPU in-browser option** — for v1.5 Tauri webview. WebNarrator 1.1.0 demonstrates the pattern (Kokoro-82M via ONNX Runtime Web + OPFS cache, opt-in download).

### os-toold (port 8744) — no change

**State:** ✅ live, manual tests only, path guard + command allowlist.

**v6 addition:** `/reliability` endpoint — denials distribution, suspicious-pattern count.

### openclaw (port 18789) — keep, align memory with OpenClaw contract, expose reliability

**State:** ✅ live, TS/Node gateway, Telegram `@danlab_bot` paired, mcporter bridge to Zo MCP, 6 OpenRouter providers configured.

**v6 work:**

1. **Memory adapter contract.** memoryd v2 must expose `/memory/{bootstrap,semantic}` (v5). v6 also requires `/operative_context` (proactived dependency).
2. **Reliability metric exposure.** The audiod agent should expose ECE/Brier/calibration curves as OpenClaw tool outputs. v6: add `dan_reliability_*` tool family (OpenClaw extension).
3. **Microsoft Scout (Build 2026, Jun 2 2026) compatibility.** Scout is built on OpenClaw. v6: track Scout-compatible extensions and adopt if any ship.
4. **Failure-mode registry broadcast.** When audiod RL agent detects rise-and-collapse (per arXiv 2606.21090), broadcast to all OpenClaw sessions for human inspection.

### dan-glasses-app (port 8747) — collapse proxy, Tauri-native

**State:** ✅ live, React SPA, 5 tabs (Bootstrap / Vision / Memory / TTS / Live). Roundtrip green.

**v6 work:**

1. **Collapse Python proxy** (v5). Run as Tauri dev-server reverse-proxy or Tauri sidecar binary.
2. **Add `live_terminal.md` view** (NEW v6). User-visible audit trail of: audiod confidence → memoryd operative_context selection → proactived nudges → user response. Aligned with the OpenReview "Operative Contexts" contestability framing.
3. **Reliability chip on every panel.** Every daemon's `/reliability` surfaced in the UI.

---

## Cross-cutting concerns (v6)

1. **Reliability as a typed service contract.** Every daemon exposes `/reliability` returning `{ece, brier, last_failure_class, fault_class_distribution, last_update_ts}`. audiod is first; perceptiond salience confidence, toold execution success, memoryd retrieval ECE, ttsd intelligibility confidence, os-toold denials distribution follow.
2. **Failure-mode registry (NEW v6).** Centralized JSON-Lines log of `(daemon, fault_class, confidence, ts)` written by every daemon to a shared file (`/var/log/danlab/failures.jsonl`). audiod RL agent reads it for early-stop signal.
3. **Operative Context surface (NEW v6).** memoryd → proactived → user-visible live terminal. Aligns with the contestability framing from OpenReview "Operative Contexts" 2026.
4. **OpenClaw-memory alignment.** memoryd v2 must expose `/memory/{bootstrap,semantic}` AND `/operative_context` (v6 addition).
5. **Power-state machine.** Global enum `wakeful|watchful|drowsy|asleep` on every daemon, coordinated by OpenClaw heartbeat. perceptiond: `idle` unloads the VLM from RAM.
6. **Hardware privacy switch (v1.5).** Camera off, mic off, LED configurable. The "AI glasses that don't spy on you" moat (per v5).
7. **`rewardsd` (NEW service, v6 spec).**
   - Endpoints: `/rewards/ingest`, `/rewards/policy/export`, `/rewards/aie-bench/{submit,status}`, `/rewards/seagym/{submit,status}`, `/reliability`, `/failure_mode`.
   - Persistence: SQLite + append-only log of `(task, action, signal)` tuples.
   - AIE-Bench harness integration: run meta-agent proposal loop, evaluate on held-out task set, log improvement.
   - SEAGym harness integration: run harness-only updates (prompts, memories, tools, skills) on Terminal-Bench 2.0 + HLE.
   - Failure-mode registry write access.
8. **`proactived` (NEW service, v6 spec).**
   - Inputs: calendar (CalDAV or Google Calendar adapter), location (optional, opt-in), time, email (Gmail or local IMAP), operative_context from memoryd.
   - Output: nudge → `ttsd.speak({text, priority, audio_volume})`.
   - OpenClaw tool exposure: `dan_proactive_*`.
   - Reliability dependency: must consume audiod's `/reliability` to gate nudges (don't nudge during failure-mode events).

---

## Verdict

The architecture is correct. The 8/8 daemons, 144/144 tests, published SPA, live OpenClaw gateway — these are the receipts. The v6 work adds:

1. **audiod calibration RL agent (THE differentiator)** — submit to AIE-Bench + SEAGym by Sep 30, 2026.
2. **memoryd v2** — AEL + DPCM + LLM-Wiki + operative_context + reliability + OpenClaw-memory adapter.
3. **ttsd v2** — Kokoro-82M swap by Jul 15, 2026.
4. **perceptiond v2** — OmniVLM-968M eval + V5e-0 speculative decoding + CondenseVLM token condensation.
5. **Power-state machine** — every daemon owns it (cross-cutting).
6. **rewardsd (NEW)** — AIE-Bench + SEAGym integration + failure-mode registry.
7. **proactived (NEW)** — calendar + location + time + email fusion, audiod-reliability-gated.
8. **Hardware privacy switch** — v1.5 PCB design.
9. **`/reliability` on every daemon** — ECE/Brier/fault-class as a first-class contract.

The 6-month plan (Jul – Dec 2026) is the verifiable self-improvement era. The 12-month plan is the on-device on-wearable era. The 24-month plan is the AGI thesis era.

— Dan2, 2026-06-24 11:30 IST
