# Dan Glasses Architecture Review
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-16
**Scope:** Review of the canonical Dan Glasses v1 architecture (per `PRD.md`, the build plan, service SPECs, and verified live state from `agent-work/dan1.md`).
**Inputs:** `dan2-research-report.md` (sections A1–A4, B7–B10, D-A/B/C).

---

## TL;DR

The architecture is **fundamentally right** for a 2026 wearable AI. The 5-daemon split (audiod, perceptiond, memoryd, toold, ttsd) + OpenClaw gateway + Tauri v2 + LFM2.5-VL-450M is a defensible v1. The critical gaps are **not architectural** — they are:

1. **No power state machine.** (VLM inference is 3–8W; capture-FPS throttling is the wrong lever.)
2. **No wake-word service.** (`wakewordd` is missing; audiod spec defers it to v3.)
3. **Memory is 2024-era.** (flat SQLite + flat cosine on MiniLM-L6. The 2026 literature is hierarchical, dual-process, schema-inducing.)
4. **No hardware contract.** (Redax is a codename. No weight, battery, thermal target. This blocks Track B.)
5. **No safety harness.** (Prompt injection via camera frames → os-toold. The canonical analysis flagged this; no mitigation in code.)

Everything else is incremental hardening.

---

## 1. The 5-daemon decomposition

**Verdict: correct.** Each daemon has a single, well-bounded responsibility and a clean HTTP+WS API. The decomposition matches the natural failure-mode boundaries (audio can fail without breaking vision, memory can fail without breaking tools, etc.).

**Things it gets right:**
- **Isolation** — no shared memory, no shared state. Each daemon is killable.
- **Schema-enforced events** — audiod's transcript event has a real schema, not ad-hoc JSON.
- **HTTP + WebSocket transports** — audiod uses stdlib WS (no `websockets` dep, which is excellent), perceptiond uses raw HTTP (no reqwest in Tauri bridge).
- **Health/status contracts** — every daemon has `/health` and `/status`, exposed through Tauri's command bridge.
- **Test coverage** — 106/106 across the 5 daemons is a strong floor. (perceptiond 8, memoryd 11, toold 15, ttsd 6, audiod 73 — all green.)

**Things to push on:**
- **Service discovery.** Right now port numbers are hardcoded (`8090`, `8092`, `8741`, `8742`, `8743`, `8744`, `18789`). When the Redax board lands or we have 2 glasses on a desk, this is a problem. Cheap fix: a small `dan-services.json` in `/etc/dan/` + a registration heartbeat. Don't over-engineer.
- **Authentication between daemons and OpenClaw.** Right now it's loopback. Fine for a laptop. **Not fine** for the wearable. Add a bearer token per daemon (per `zo.space` `Authorization: Bearer` pattern). The spec mentions "argument hashing and audit log" but nothing about inter-service auth.
- **No graceful restart story.** If perceptiond crashes, the Tauri UI does not know. Add a `last_heartbeat_ts` to `/status` and a UI banner on staleness.
- **No backpressure coordination across daemons.** VLM queue cap is 2 in perceptiond. Good. But if audiod is also backed up, both will silently drop. A shared "system pressure" channel in OpenClaw is the right place; not in each daemon.

---

## 2. The "multimodal RL feedback loop" in danlab-multimodal

**Verdict: honest, but should not be called RL.** The README is explicit. The code in `src/demo.py` is explicit. Good.

**Concrete evidence (per `src/demo.py` head + the architecture doc):**
```python
# hand-coded heuristics, not learned:
if len(response) < 30:      score -= 40
if "[ERROR]" in response:  score -= 60
if identifies_ui(response): score += 10
```
No weight updates, no policy gradient, no learned reward model. This is **pre-RL scaffold**, as labeled.

**The path to genuine self-improvement** is well-mapped in the research (see `dan2-research-report.md` section D-A):
- **Tier 1 (2 weeks):** Replace the heuristic with a learned reward model (MiniLM cross-encoder fine-tuned on 200–500 human-rated descriptions). Still not RL, but the prerequisite.
- **Tier 2 (4 weeks):** Add TT-SI (ACL 2026): self-awareness → self-data-augmentation → test-time training on weak areas.
- **Tier 3 (8 weeks):** Fork SIA (Hexo Labs, MIT, May 2026) and integrate as a harness. *Now* it is a real self-improving loop.
- **Tier 4 (16 weeks):** Add a published ablation: heuristic vs. learned reward vs. TT-SI vs. SIA-fork. This is the contribution to the field.

**Don't:**
- ❌ Add more heuristic rules. The current ones are the right shape; the next move is a learned reward model.
- ❌ Try to fine-tune LFM2.5-VL in the loop. The compute cost on x86_64 laptop is prohibitive; the right move is LoRA on a smaller model (MiniLM) acting as a reward.
- ❌ Conflate this with the dan-glasses memory loop. Different problem, different solution.

---

## 3. Power / performance tradeoffs

**Verdict: the model choices are right. The thermal/power architecture is missing.**

### 3a. LFM2.5-VL-450M — correct call
- Released April 11, 2026 (3 months ago). Sub-250ms edge inference target. SigLIP2 NaFlex encoder (better than ResNet/ViT for our use case).
- `llama-mtmd-cli` path works (verified live in perceptiond).
- 512×512 input is right for always-on scene description. For OCR-heavy frames, route to a larger model (Gemma3 fallback).
- **Bottleneck:** the spec cites "150–800ms" inference on LFM2.5-VL-450M, but the verified live number is **10–15s/frame on x86_64 CPU**. That's a 10–100× gap. The optimistic spec number is probably on aarch64 with NPU offload. We need the **measured** numbers in the spec, not the marketed ones.

### 3b. whisper.cpp + Silero VAD — correct call
- `whisper-cpp-plus-rs` (DAN-2's choice) with async + VAD is the right library. We chose the stdlib WS path instead — also fine, but loses the VAD integration. **Recommendation:** bring Silero VAD on-device for the wake word path (see §4).
- `ggml-base.bin` (148MB) is right for laptop; `ggml-tiny.bin` (78MB) is the right call for aarch64 wearable.

### 3c. KittenTTS — correct call but watch the variant
- v0.8 (Feb 2026), 3 variants: nano (15M, ~25MB int8), micro (40M), mini (80M).
- Live we use "medium" — that's not even in the canonical KittenTTS lineup. Either it's a custom build or the spec is referencing an old label. **Check.**
- For wearable: **nano-int8 at ~25MB**. 8–9× real-time. Quality is "lowest" but is good enough for spoken feedback.
- The Second State `kitten_tts_rs` crate is a Rust port — we should benchmark it against the Python/ONNX path. If it wins on latency, we save a process.

### 3d. The missing power architecture

This is the biggest gap in the v1 canonical spec. Per the canonical analysis (which is correct):
- Throttling capture FPS (idle=2, watchful=5, active=10) does not throttle VLM inference.
- Every captured frame in `watchful` still goes through the full perception pipeline if salient.
- At 2 FPS idle, the VLM still fires every 500ms on average. Wrong lever.

**Right design (proposed):**
- **Salience-based gating at the VLM level**, not the capture level. Run VLM only when:
  - Motion exceeds threshold AND scene-change classifier agrees, OR
  - A new face appears, OR
  - Push-to-talk / wake-word fires, OR
  - A scheduled "check-in" (e.g., every 30s in watchful mode).
- **Adaptive state machine** (see §4).
- **Thermal-aware throttling** — if SoC temp > threshold, drop to Gemma3-270M fallback (text-only, no vision). This buys 5–10× power reduction.

**Concretely, what the power budget should look like (per `dan2-model-analysis.md`):**

| Mode | CPU | LFM2.5-VL (avg) | Mic | Total | Battery (2000mAh@3.7V) |
|------|-----|------------------|-----|-------|--------------------------|
| Sleep (camera off, mic VAD only) | 0.05W | 0W | 0.05W | **0.1W** | ~74h |
| Idle (camera on, no VLM) | 0.4W | 0W | 0.1W | **0.5W** | ~15h |
| Watchful (VLM on motion, ~1 inf / 3s) | 0.6W | 0.8W (intermittent) | 0.1W | **1.5W avg** | ~5h |
| Active (continuous VLM, LLM on demand) | 0.8W | 3.0W | 0.1W | **4.0W peak** | ~1.8h |
| Burst (LLM response) | 1.0W | 3.0W | 0.1W | **5.0W peak (brief)** | — |

A 2× 200mAh battery (400mAh) at 3.7V = 1.48Wh. At watchful avg, that's ~1h. **Redax needs bigger batteries** or we need a tethered path. The Brilliant Labs Frame at ~6–8h battery uses a phone-tether architecture; that's a credible pattern.

---

## 4. Missing: wake-word + power state machine

**The canonical spec defers both. They are not optional for a wearable.**

### 4a. `wakewordd` (or merge into `audiod`)
- **Why:** Push-to-talk (the current default) is the right call for v1 (battery, safety), but is **not** a wearable UX. The user has to take a physical action every time. Wake-word is the difference between "compelling demo" and "daily driver."
- **Pick:** `openWakeWord` (open-source, Picovoice-derived, runs on CPU) or Porcupine (commercial, on-device). `openWakeWord` first; fall back to Porcupine if accuracy is bad.
- **Where:** New daemon `wakewordd` on a small port (e.g., 8095) using ONNX Runtime. Or fold into `audiod` as a pre-VAD stage.
- **Latency target:** <200ms from utterance to wake-event.
- **Power:** <50mW continuous (DSP-style).

### 4b. `powerd` (power state machine)
- **Why:** A wearable must transition between sleep / idle / watchful / active / burst gracefully, with measured Watt budgets at each state, and with thermal-aware throttling.
- **Pick:** New daemon `powerd` on port 8096. Owns:
  - Current state
  - Transition rules (event-driven, time-based, thermal-based)
  - Per-mode health checks (does the VLM process need to be alive?)
  - Battery percentage + estimated runtime at current state
- **Why a daemon, not a config:** because the transitions need to react to real events (wake word, push-to-talk, low battery, high temp) and coordinate service restarts.
- **Alternative:** implement as a state in `audiod` (the always-on process) and have it signal `perceptiond` / `memoryd` / OpenClaw via events. Cheaper to ship, less correct.

### 4c. Bootstrap and watchdog
- A small **watchdog** that restarts crashed daemons with exponential backoff is **missing**. Right now if `perceptiond` dies, the Tauri UI shows red and the user has to manually restart. systemd unit files exist (`packaging/systemd/*.service`) — but on the laptop dev path, we need the equivalent in `scripts/dev.sh` (which exists). Confirm restart-on-fail is wired.

---

## 5. OpenClaw as TS/Node orchestrator

**Verdict: acceptable for v1, but the gateway layer should be Rust by v1.5.**

### Why TS/Node is OK now
- **Agent ergonomics:** OpenClaw's MCP tool registration, policy filters, and the Telegram channel are TS-native. Building that in Rust from scratch is 6+ months of work.
- **Where the LLM actually lives** is in OpenClaw's prompt loop, where TS is fine — the LLM API call is the hot path, and Node handles it well.
- **Real failure modes observed** (per `agent-work/dan1.md`):
  - `tailscaled` not running — fine, we use loopback.
  - `mcporter` returns 405 from Zo MCP — we worked around with the `zo-bridge` stdio MCP shim. **This is the production path. Do not try to fix mcporter.**
  - Telegram channel enabled, `dmPolicy=pairing`, `groupPolicy=allowlist`, streaming=partial. Looks correct.

### Why TS/Node is a problem for the wearable
- **GC pauses.** Node's stop-the-world GC is 5–50ms typical, 200ms+ worst case. For a 200ms-wake-word → audio → LLM round-trip, that's 25–100% jitter. On a battery-powered wearable, this is a measurable power and latency penalty.
- **No native threading model.** OpenClaw's "Octopus Orchestrator" runs parallel arms as separate processes, which is correct — but the per-arm process model means each arm pays Node startup cost (200–500ms cold) and memory (~80–150MB per arm).
- **Update surface.** TypeScript dependency churn is real. `npm install` against the OpenClaw tree is a footgun. Lockfiles help, but the failure mode is silent dep drift.

### Recommendation
- **v1 (now):** keep OpenClaw. Don't try to replace it.
- **v1.5 (Q4 2026):** extract a thin **Rust gateway** that handles:
  - Health monitoring across daemons
  - Power-state transitions (see §4b)
  - Inter-service IPC (replace HTTP-loopback with Unix sockets + length-prefixed framing for the hot path)
  - Bearer-token auth between daemons and OpenClaw
- **v2 (2027):** port the agent loop in OpenClaw to Rust (or to a Rust + Wasmtime + Wasm-component model, which is the closest TS-equivalent that doesn't need a GC). This is the AGI-grade runtime.

---

## 6. Memory architecture

**Verdict: this is the single biggest missed opportunity in v1.**

Current state (per `Services/memoryd/SPEC.md` + verified):
- `sentence-transformers/all-MiniLM-L6-v2` (384-dim float32).
- Stored as BLOB in SQLite.
- Cosine similarity only.
- 3 types: episodic, semantic, procedural. Good taxonomy.

**What's missing for 2026 credibility:**
- **Temporal metadata** on every memory. Created-at is not enough — last-accessed, decay rate, version chain (when a fact changed).
- **Confidence decay** (Ebbinghaus-style). Memoryd is currently a static store. The 2026 literature (DPCM, TiMem, SmartVector, LiCoMemory) all treat confidence as a first-class signal.
- **Relational scoring.** "This memory is linked to that memory." Currently we have none.
- **Schema induction** (System 2 in DPCM). At night, the memory daemon should cluster episodic → semantic → procedural → schema. Not in v1.5; in v2.

**Concrete v1.5 changes (cheap, 2 weeks):**
1. Add `created_at`, `last_accessed_at`, `access_count`, `decay_rate` to the `memories` table.
2. Add a `ConsolidationAgent` cron job (every 6h) that:
   - Boosts memories with high `access_count`
   - Decays memories with low `access_count` and high age
   - Tags "supersedes" chains when semantic similarity > 0.92 between new and old
3. Change `/query` to score as `cosine * temporal_validity * confidence * relational_bonus`.

**This is the v1 → v1.5 delta that makes Dan Glasses feel like a personal intelligence, not a transcript logger.**

---

## 7. Tauri v2 frontend

**Verdict: correct choice, integration is incomplete.**

- React 19 + Vite 7 + TS frontend; Tauri v2 + Rust bridges for 7 services. Pattern is right.
- Live: 8 Rust bridge modules (greet, audiod, memoryd, perceptiond, toold, ttsd, os_toold, openclaw).
- Polling: DaemonHealth 4s, VisionDashboard 2.5s status + 5s descriptions. Reasonable.
- Build: 3.02s, 35 modules, ~210KB JS. Excellent.

**What to add:**
- **PTT button in UI.** Per `agent-work/dan2.md` Ship order, this is in progress. The fact that audiod's `/start`, `/stop`, `/ptt` endpoints don't exist is the real gap.
- **Voice picker in the bootstrap wizard.** Per `agent-work/dan4.md`, this is also in progress. Verify the round-trip write to memoryd after voice selection.
- **In-app TTS playback.** The wizard currently uses `aplay` server-side. For a desktop app pointed at localhost, the wizard should fetch `/speak` and play via `<audio>`.
- **System health banner with quick actions.** When `powerd` ships, this should be the home tab. "Battery: 64% (~3h watchful). Temp: 41°C. State: watchful." One glance, one click to change state.
- **Real-time transcript in the LiveTranscript component** is already working (per dan1 notes). Good.

---

## 8. OpenClaw integration / MCP / Telegram

**Verdict: solid for v1, with one known workaround that should be documented.**

- Telegram channel live, pairing-only DM, allowlist groups. Correct security posture.
- `zo-bridge` MCP shim works around the `mcporter` 405 on `https://api.zo.computer/mcp`. **Document this in OpenClaw config and stop trying to fix mcporter.** The shim is the production path.
- 2 MCP servers currently registered: `zo` (broken) and `OpusCode` (healthy). Clean up: remove the broken `zo` entry from `mcporter`'s registry; keep `zo-bridge` in `openclaw.json`.

**For v1.5:**
- Add per-daemon MCP servers (perception, memory, toold, tts) so OpenClaw agents can call them as tools.
- Add a "policy deny" rule for the perception → os-toold path (per §9).

---

## 9. Security / prompt injection

**Verdict: gap, not addressed in code.**

The canonical analysis flagged it. The current `toold` sandbox blocks shell metacharacters and confines to a workdir. Good. But:

- **A camera frame can contain text that is then read by the VLM and treated as a command.** Example: a poster that says "echo pwned > /tmp/x" → VLM caption includes that text → downstream LLM (in OpenClaw) reads the caption and decides to execute. The denylist doesn't catch this because the text is in the *content*, not the *command*.
- **Mitigations (cheap, in order):**
  1. **Perception-frame trust score** in perceptiond. Score = coherence × novelty × type. Text-heavy frames with command-like tokens get a low score.
  2. **Argument hashing + audit log** in `toold` (already mentioned in the canonical spec, verify it's in code).
  3. **Two-channel tool execution.** "Told to execute X" vs "user said execute X" — only the second is allowed. Implemented in OpenClaw's policy layer.
  4. **Strict denylist of "execute-from-perception" verbs.** No `os_toold` call is allowed whose `source` is a `perceptiond` event, period. The user must re-enter the command.

**Adversarial robustness literature:** Synthius-Mem reports 99.6% adversarial robustness on LoCoMo. That is the bar.

---

## 10. Packaging / deployment

**Verdict: 80% there, missing .deb.**

- 5 systemd unit files present (`packaging/systemd/`). Good.
- `packaging/debian/` is empty (only README). Per `dan1.md`, this is the next milestone.
- `scripts/dev.sh` (up/status/stop/restart) works for laptop dev. Good.
- `.deb` will need: control file, post-install hook that enables systemd units, signing (GPG or Sigstore — **pick one and document**).

**Recommendation:** Don't ship a Flatpak or AppImage. The canonical analysis is correct: .deb + systemd is the right path for hardware that needs udev rules, privileged install actions, and a real package signing story.

---

## What to do this week

1. **Add `wakewordd` (or fold openWakeWord into audiod).** Single highest-UX-impact change.
2. **Add `powerd` (or a state machine in audiod).** 2-day build, 1-week hardening.
3. **Memory v1.5: temporal + confidence + relational scoring.** 2 weeks. Single biggest credibility upgrade.
4. **Prompt-injection guard for os-toold.** 1 week. Use the perception-source denylist as the cheap mitigation.
5. **Measure LFM2.5-VL-450M power on x86_64 + simulated aarch64.** Stop using "150–800ms" from the spec. Get the real numbers.

## What to do this quarter

6. **Memory v2: dual-process (DPA/DPCM).** Replace the static SQLite + flat cosine.
7. **TT-SI pilot in danlab-multimodal.** Replace the hand-coded heuristic with a learned reward model.
8. **Daily briefing agent.** Calendar + email + memories → 60s spoken. The killer-app demo.
9. **Hardware decision.** Redax or indie path. 6-month clock.
10. **Paper.** The TT-SI vs. SIA ablation is publishable. Start drafting.

## What NOT to do

- ❌ Don't replace OpenClaw with Rust in v1.
- ❌ Don't add more heuristic rules to danlab-multimodal.
- ❌ Don't add another Python daemon. The 5 are enough.
- ❌ Don't call danlab-multimodal's loop "RL" until harness+weights are open.

---

*👾* Review complete. The architecture is fundamentally right; the next 90 days are about power, memory, and safety — not about redesigning the wheel.
