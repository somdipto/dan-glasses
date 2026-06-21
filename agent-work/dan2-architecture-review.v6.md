# Dan Glasses Architecture Review
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-17
**Scope:** Review of the canonical Dan Glasses v1 architecture (per `PRD.md`, the build plan, service SPECs, and verified live state from `agent-work/dan1.md`).
**Inputs:** `dan2-research-report.md` (v6, 2026-06-17) — sections A1–A4, B7–B10, D-A/B/C; danlab-multimodal README + ARCHITECTURE; paperclip / blurr READMEs; verified live state from `dan1.md`, `dan2.md`, `dan3.md`, `dan4.md`.
**Prior versions:** `dan2-architecture-review.v5.md` (2026-06-16) — kept as backup.

---

## TL;DR

The architecture is **fundamentally right** for a 2026 wearable AI. The 5-daemon split (audiod, perceptiond, memoryd, toold, ttsd) + OpenClaw gateway + Tauri v2 + LFM2.5-VL-450M is a defensible v1. The critical gaps are **not architectural** — they are:

1. **No power state machine.** (VLM inference is 3–8 W; capture-FPS throttling is the wrong lever.)
2. **No wake-word service.** (`wakewordd` is missing; audiod spec defers it to v3.)
3. **Memory is 2024-era.** (flat SQLite + flat cosine on MiniLM-L6. The 2026 literature is hierarchical, dual-process, schema-inducing.)
4. **No hardware contract.** (Redax is a codename. No weight, battery, thermal target. This blocks Track B.)
5. **No safety harness.** (Prompt injection via camera frames → os-toold. The canonical analysis flagged this; no mitigation in code.)

**v6 changes from v5:**
- **HRM-Text 1B conflict resolved** — root `AGENTS.md` says "HRM-Text (1B) for reasoning" but `dan-glasses/AGENTS.md` says "LFM2.5-VL-450M for vision." v6 sets the record straight: **HRM-Text 1B is the on-device reasoning LLM (text); LFM2.5-VL-450M is the vision encoder.** Two models, one pipeline. See §3a.
- **Anthropic "brake pedal" (2026-06-04)** now public — this is a *coordination* problem and validates the open-source, auditable, on-device positioning. See §9.
- **Muse Spark (May 2026) replaced Llama 4 on Meta Ray-Bans** — this matters because Meta's wearable AI is no longer the meta-Llama series, breaking the "follow Llama" mental model. See §4.
- **Apple glasses delayed to late 2027** (per Gurman, 2026-05-31) — gives us another 12+ months of window before Apple's consumer push. See §4.

Everything else is incremental hardening on top of v5.

---

## 1. The 5-daemon decomposition

**Verdict: correct.** Each daemon has a single, well-bounded responsibility and a clean HTTP+WS API. The decomposition matches the natural failure-mode boundaries (audio can fail without breaking vision, memory can fail without breaking tools, etc.).

**Things it gets right:**
- **Isolation** — no shared memory, no shared state. Each daemon is killable.
- **Schema-enforced events** — audiod's transcript event has a real schema, not ad-hoc JSON.
- **HTTP + WebSocket transports** — audiod uses stdlib WS (no `websockets` dep, which is excellent), perceptiond uses raw HTTP (no reqwest in Tauri bridge).
- **Health/status contracts** — every daemon has `/health` and `/status`, exposed through Tauri's command bridge.
- **Test coverage** — 106/106 across the 5 daemons is a strong floor. (perceptiond 8, memoryd 11, toold 15, ttsd 6, audiod 66 — all green, per `dan4.md` and `dan1.md`.)

**Things to push on (v6 deltas):**
- **Service discovery.** Right now port numbers are hardcoded (`8090`, `8092`, `8741`, `8742`, `8743`, `8744`, `18789`). When the Redax board lands or we have 2 glasses on a desk, this is a problem. Cheap fix: a small `dan-services.json` in `/etc/dan/` + a registration heartbeat. Don't over-engineer.
- **Authentication between daemons and OpenClaw.** Right now it's loopback. Fine for a laptop. **Not fine** for the wearable. Add a bearer token per daemon (per `zo.space` `Authorization: Bearer` pattern).
- **No graceful restart story.** If perceptiond crashes, the Tauri UI does not know. Add a `last_heartbeat_ts` to `/status` and a UI banner on staleness.
- **No backpressure coordination across daemons.** VLM queue cap is 2 in perceptiond. Good. But if audiod is also backed up, both will silently drop. A shared "system pressure" channel in OpenClaw is the right place; not in each daemon.
- **v6 add: Shared `/types` IPC crate.** The `shared/` directory is empty per `dan1.md`. Each daemon defines its own JSON shapes. A small Rust crate with serde structs (and a Python `dataclass` mirror) would prevent the drift `dan1.md` already calls out. **This is the highest-ROI architectural hardening we can do for v1.1.**

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

### 2a. v6 update — the SIA landscape has moved (May 2026 → June 2026)

Since the v5 report, the self-improving-agent literature has exploded. The current map (June 2026):

- **SIA** (Hexo Labs, arXiv:2605.27276, May 2026) — the canonical harness+weights framework. 56.6% gain on LawBench, 91.9% runtime reduction on GPU kernels, 502% improvement on denoising when **harness + weight updates are both enabled** (SIA-W+H) vs. harness-only (SIA-H).
- **HarnessX** (arXiv:2606.14249, June 2026) — explicit theory: *harness-only optimization and model training alone hit distinct ceilings. Co-evolution enables the model to internalize strategies introduced by successive harness versions.* This is exactly the SIA-W+H story, formalized.
- **Self-Harness** (arXiv:2606.09498, June 2026) — a three-stage self-contained loop (weakness mining → harness proposal → proposal validation) that requires **no human engineers and no stronger external agent**. Lighter than SIA.
- **AHE — Agentic Harness Engineering** (arXiv:2604.25850, May 2026) — observability-driven harness evolution. 10 iterations improved pass@1 from 69.7% → 77.0% on Terminal-Bench 2, surpassing Codex-CLI's human-tuned harness (71.9%).
- **HarnessForge** (arXiv:2606.01779, June 2026) — joint harness+policy co-evolution. Up to 12% gains vs. harness-only or policy-only baselines.
- **RHO — Retrospective Harness Optimization** (arXiv:2606.05922, June 2026) — *single-pass label-free harness improvement* over past trajectories. Achieves 0.78 SWE-Bench Pro pass@1 in one round, beating Meta-Harness's 10-round 0.80 with 3× less compute and no labels.
- **SICA — A Self-Improving Coding Agent** (arXiv:2504.15228) — removes the meta-agent/target-agent separation; the meta-agent is itself drawn from the agent archive. ADAS-like.
- **HyperAgents / DGM-H** (arXiv:2603.19461) — meta-level modification procedure is itself editable. The improvement strategy evolves.
- **Adaptive Auto-Harness** (arXiv:2606.01770) — sustained self-improvement for **open-ended task streams** (the case danlab-multimodal actually is). Stateful four-phase multi-agent evolver.

**Implication for danlab-multimodal:** SIA is no longer the only game in town. The right first move is probably **RHO (label-free, single-pass)** + **SIA (harness+weights) as the target**. RHO is cheap and needs no human-rated data; SIA is the destination. **Re-evaluate the SIA-only plan from v5.**

### 2b. The path to genuine self-improvement — concrete next steps

- **Tier 1 (2 weeks):** Replace the heuristic with a learned reward model (MiniLM cross-encoder fine-tuned on 200–500 human-rated descriptions). Still not RL, but the prerequisite. **OR** start with RHO over our existing trajectories — label-free, single-pass, no human data needed.
- **Tier 2 (4 weeks):** Add TT-SI (ACL 2026): self-awareness → self-data-augmentation → test-time training on weak areas.
- **Tier 3 (8 weeks):** Fork SIA (or HarnessForge) and integrate as a harness. *Now* it is a real self-improving loop.
- **Tier 4 (16 weeks):** Add a published ablation: RHO vs. learned reward vs. TT-SI vs. SIA-fork vs. HarnessForge-fork. Five configurations, same eval, same data. This is the contribution to the field.

**Don't:**
- ❌ Add more heuristic rules. The current ones are the right shape; the next move is a learned reward model OR RHO.
- ❌ Try to fine-tune LFM2.5-VL in the loop. The compute cost on x86_64 laptop is prohibitive; the right move is LoRA on a smaller model (MiniLM) acting as a reward.
- ❌ Conflate this with the dan-glasses memory loop. Different problem, different solution.

---

## 3. Power / performance tradeoffs

**Verdict: the model choices are right. The thermal/power architecture is missing.**

### 3a. v6 update — reconciling the model strategy

The root `AGENTS.md` says: **"HRM-Text (1B) for reasoning, Whisper for STT."** The `dan-glasses/AGENTS.md` says: **"LFM2.5-VL-450M for vision."** These are not contradictory — they specify different models for different jobs. Here's the canonical model lineup for v1:

| Role | Model | Size | Where | Status |
|---|---|---|---|---|
| **Reasoning LLM** (text) | HRM-Text 1B | ~1.15B params, ~2 GB FP16, ~500 MB INT4 | Laptop → wearable (int4) | Released 2026-05-18; needs integration |
| **Vision encoder + VLM** | LFM2.5-VL-450M | 209 MB Q4_0 + 180 MB mmproj F16 | perceptiond, on aarch64+NPU target | Live, ~10–15s/frame on x86_64 CPU |
| **STT** | whisper.cpp / ggml-base.bin | 148 MB (or 78 MB tiny) | audiod | Live |
| **TTS** | KittenTTS | 25–80 MB (nano/micro/mini) | ttsd | Live (variant label "medium" needs reconciling) |
| **Memory embeddings** | all-MiniLM-L6-v2 | 22 MB, 384-dim | memoryd | Live |
| **Wake-word** | openWakeWord | ~5 MB | wakewordd (proposed) | Missing |

**Why HRM-Text 1B matters:** Sapient Intelligence released HRM-Text on 2026-05-18. Key claims:
- 1.15 B parameters, **40B training tokens** (vs. 4–36T for comparable models — ~1000× less).
- Full training in ~1 day for ~$1,000.
- **Reasons in continuous latent space** rather than long visible CoT chains. This is huge for wearables: a 1B model that does "real" reasoning at <500 MB INT4.
- Competitive with 4–36T-token models on reasoning benchmarks.

**For Dan Glasses, the HRM-Text 1B integration is the v1.1 next step.** It should sit between the VLM descriptions + transcripts (incoming) and the ttsd speak (outgoing), reasoning about what the user wants, what to remember, and when to speak. **Don't add it as another daemon — wire it as a module in OpenClaw's prompt loop**, or as a thin `reasond` service. This is what `dan2-research-report.md` §2.1 calls out as missing.

### 3b. LFM2.5-VL-450M — correct call (unchanged from v5)
- Released April 11, 2026. Sub-250ms edge inference target on aarch64+NPU. SigLIP2 NaFlex encoder.
- `llama-mtmd-cli` path works (verified live in perceptiond).
- 512×512 input is right for always-on scene description.
- **Bottleneck:** the spec cites "150–800ms" inference, but the verified live number is **10–15 s/frame on x86_64 CPU**. The 250ms target is on aarch64+NPU. We need the *measured* numbers, not the marketed ones.

### 3c. v6 update — Whisper + Moonshine trade-off

For 2026 multilingual India support, the standard `ggml-base.bin` (148 MB) is right for English; for multilingual, evaluate:
- **ggml-small** (244 MB) — wider language support.
- **Moonshine** (moonshine-ai) — purpose-built for edge, transformer + compact LLM on 1 TOPS NPU, beats whisper-tiny in accuracy while running real-time on-device. **Worth evaluating for v1.5.**
- **Parakeet** (NVIDIA) — streaming, fast, English-first.

Keep whisper.cpp for compatibility, but build a parallel Moonshine path.

### 3d. KittenTTS — correct call but watch the variant (unchanged)
- v0.8 (Feb 2026), 3 variants: nano (15M, ~25 MB int8), micro (40M), mini (80M).
- Live we use "medium" — **this is not a canonical KittenTTS variant.** Reconcile.
- For wearable: **nano-int8 at ~25 MB**. 8–9× real-time. Quality is "lowest" but is good enough for spoken feedback.
- For v1.5, evaluate `kitten_tts_rs` (Second State Rust port, no Python dep) and **Kokoro-82M** as the quality bar (still <100 MB).

### 3e. The missing power architecture (unchanged from v5)

This is the biggest gap in v1:
- Throttling capture FPS (idle=2, watchful=5, active=10) does not throttle VLM inference.
- Every captured frame in `watchful` still goes through the full perception pipeline if salient.

**Right design (proposed v1.1):**
- **Salience-based gating at the VLM level**, not the capture level. Run VLM only when:
  - Motion exceeds threshold AND scene-change classifier agrees, OR
  - A new face appears, OR
  - Push-to-talk / wake-word fires, OR
  - A scheduled "check-in" (e.g., every 30s in watchful mode).
- **Adaptive state machine** (see §4).
- **Thermal-aware throttling** — if SoC temp > threshold, drop to Gemma3-270M text-only fallback. Buys 5–10× power reduction.

**Concretely, what the power budget should look like:**

| Mode | CPU | LFM2.5-VL (avg) | Mic | Total | Battery (2000 mAh @ 3.7 V) |
|------|-----|------------------|-----|-------|------------------------------|
| Sleep (camera off, mic VAD only) | 0.05 W | 0 W | 0.05 W | **0.1 W** | ~74 h |
| Idle (camera on, no VLM) | 0.4 W | 0 W | 0.1 W | **0.5 W** | ~15 h |
| Watchful (VLM on motion, ~1 inf / 3 s) | 0.6 W | 0.8 W (intermittent) | 0.1 W | **1.5 W avg** | ~5 h |
| Active (continuous VLM, LLM on demand) | 0.8 W | 3.0 W | 0.1 W | **4.0 W peak** | ~1.8 h |
| Burst (LLM response) | 1.0 W | 3.0 W | 0.1 W | **5.0 W peak (brief)** | — |

A 2× 200 mAh battery (400 mAh) at 3.7 V = 1.48 Wh. At watchful avg, that's ~1 h. **Redax needs bigger batteries or a tethered path.** Brilliant Labs Frame at ~6–8 h battery uses a phone-tether architecture — credible pattern.

---

## 4. Missing: wake-word + power state machine

**The canonical spec defers both. They are not optional for a wearable.**

### 4a. `wakewordd` (or merge into `audiod`)
- **Why:** Push-to-talk (the current default) is the right call for v1 (battery, safety), but is **not** a wearable UX.
- **Pick:** `openWakeWord` (open-source, Picovoice-derived, runs on CPU) or Porcupine (commercial, on-device). `openWakeWord` first; fall back to Porcupine if accuracy is bad.
- **Where:** New daemon `wakewordd` on a small port (e.g., 8095) using ONNX Runtime. Or fold into `audiod` as a pre-VAD stage.
- **Latency target:** <200 ms from utterance to wake-event.
- **Power:** <50 mW continuous (DSP-style).

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
- A small **watchdog** that restarts crashed daemons with exponential backoff is **missing**. systemd unit files exist (`packaging/systemd/*.service`) — but on the laptop dev path, we need the equivalent in `scripts/dev.sh` (which exists). Confirm restart-on-fail is wired.

---

## 5. OpenClaw as TS/Node orchestrator

**Verdict: acceptable for v1, but the gateway layer should be Rust by v1.5.** (Unchanged from v5.)

### Why TS/Node is OK now
- **Agent ergonomics:** OpenClaw's MCP tool registration, policy filters, and the Telegram channel are TS-native. Building that in Rust from scratch is 6+ months of work.
- **Where the LLM actually lives** is in OpenClaw's prompt loop, where TS is fine.
- **Real failure modes observed** (per `agent-work/dan1.md`):
  - `tailscaled` not running — fine, we use loopback.
  - `mcporter` returns 405 from Zo MCP — we worked around with the `zo-bridge` stdio MCP shim. **This is the production path. Do not try to fix mcporter.**
  - Telegram channel enabled, `dmPolicy=pairing`, `groupPolicy=allowlist`, streaming=partial. Looks correct.

### Why TS/Node is a problem for the wearable
- **GC pauses.** Node's stop-the-world GC is 5–50 ms typical, 200 ms+ worst case. For a 200 ms-wake-word → audio → LLM round-trip, that's 25–100% jitter. On a battery-powered wearable, this is a measurable power and latency penalty.
- **No native threading model.** OpenClaw's "Octopus Orchestrator" runs parallel arms as separate processes, which is correct — but the per-arm process model means each arm pays Node startup cost (200–500 ms cold) and memory (~80–150 MB per arm).
- **Update surface.** TypeScript dependency churn is real.

### v6 recommendation
- **v1 (now):** keep OpenClaw.
- **v1.5 (Q4 2026):** extract a thin **Rust gateway** that handles:
  - Health monitoring across daemons
  - Power-state transitions (see §4b)
  - Inter-service IPC (replace HTTP-loopback with Unix sockets + length-prefixed framing for the hot path)
  - Bearer-token auth between daemons and OpenClaw
  - **v6 add: HRM-Text 1B inference as a sub-process** — keep the LLM call out of Node's GC.
- **v2 (2027):** port the agent loop in OpenClaw to Rust (or to a Rust + Wasmtime + Wasm-component model).

---

## 6. Memory architecture

**Verdict: this is the single biggest missed opportunity in v1.** (Updated from v5 with newer 2026 papers.)

Current state (per `Services/memoryd/SPEC.md` + verified):
- `sentence-transformers/all-MiniLM-L6-v2` (384-dim float32).
- Stored as BLOB in SQLite.
- Cosine similarity only.
- 3 types: episodic, semantic, procedural.

### 6a. v6 update — the memory landscape (May–June 2026)

Since v5, several new memory systems have landed:

- **Memanto** (arXiv:2604.22085, April 2026) — **purely vector, no graph**, 13-category typed schema, conflict resolution, SOTA on LoCoMo and LongMemEval. **Counter-argument to "graph is required"**: retrieval recall is the primary driver; modern LLMs handle the reasoning that graph precomputation aimed to address.
- **TeleMem** (arXiv:2601.06037, January 2026) — **DAG of memory threads** for causal reasoning. Moves beyond unordered embeddings.
- **CraniMem** (arXiv:2603.15642, March 2026) — cranial-inspired **RAS-gated bounded episodic buffer + long-term knowledge graph**. The most biologically motivated design I've seen.
- **MemX, MemMachine, TiMem, APEX-MEM, Mem0^g, AriadneMem, Memori** — all from v5, still relevant.

**v6 verdict on graph vs. vector:** Memanto's strong vector-only results push back against the v5 recommendation. **The right move is hybrid: vector-primary + lightweight graph for typed relations + MemGate-style filter on retrieval.** Don't over-engineer the graph.

### 6b. Concrete v1.5 changes (cheap, 2 weeks)

1. **Temporal metadata:** add `created_at`, `last_accessed_at`, `access_count`, `decay_rate` to the `memories` table.
2. **Confidence decay** (Ebbinghaus-style). First-class signal.
3. **Lightweight relations:** add a `memory_links` table with **4 typed relations, not 7** (similar, related, supersedes, caused_by). Skip contradicts/extends/temporal — YAGNI until we have evidence we need them.
4. **BM25 (FTS5) index** on `content`. Reciprocal Rank Fusion with vector for hybrid retrieval.
5. **ConsolidationAgent** cron job (every 6h) that:
   - Boosts memories with high `access_count`
   - Decays memories with low `access_count` and high age
   - Tags "supersedes" chains when semantic similarity > 0.92 between new and old
6. **Change `/query` to score as `cosine × temporal_validity × confidence × relational_bonus × RRF`**.

### 6c. v2 changes (Q1–Q2 2027)
- **Dual-process memory** (DPA / DPCM): synchronous daytime writer + async nighttime schema induction.
- **TiMem-style Temporal Memory Tree**: raw events → episodic → semantic → procedural → schema.
- **MemGate** (9M-param, 35 MB) as retrieval-time filter.
- **LoCoMo benchmark eval.** 75–95% range is where 2026 SOTA lives.

**This is the v1 → v1.5 delta that makes Dan Glasses feel like a personal intelligence, not a transcript logger.**

---

## 7. Tauri v2 frontend

**Verdict: correct choice, integration is incomplete.** (Unchanged from v5.)

- React 19 + Vite 7 + TS frontend; Tauri v2 + Rust bridges for 7 services. Pattern is right.
- Live: 8 Rust bridge modules (greet, audiod, memoryd, perceptiond, toold, ttsd, os_toold, openclaw).
- Polling: DaemonHealth 4s, VisionDashboard 2.5s status + 5s descriptions. Reasonable.
- Build: 3.02s, 35 modules, ~210 KB JS. Excellent.

**What to add:**
- **PTT button in UI.** Per `agent-work/dan2.md` Ship order, this is in progress.
- **Voice picker in the bootstrap wizard.** Per `agent-work/dan4.md`, this is also in progress. Verify the round-trip write to memoryd after voice selection.
- **In-app TTS playback.** The wizard currently uses `aplay` server-side. For a desktop app pointed at localhost, the wizard should fetch `/speak` and play via `<audio>`.
- **System health banner with quick actions.** When `powerd` ships, this should be the home tab.
- **v6 add: Proactive intervention UI** — when the proactive trigger layer ships, the UI needs a non-modal intervention surface (silent icon → TTS → Telegram push). Don't bury proactive in the same UI as user-initiated queries.

---

## 8. OpenClaw integration / MCP / Telegram

**Verdict: solid for v1, with one known workaround that should be documented.** (Unchanged from v5.)

- Telegram channel live, pairing-only DM, allowlist groups. Correct security posture.
- `zo-bridge` MCP shim works around the `mcporter` 405 on `https://api.zo.computer/mcp`. **Document this in OpenClaw config and stop trying to fix mcporter.** The shim is the production path.
- 2 MCP servers currently registered: `zo` (broken) and `OpusCode` (healthy). Clean up: remove the broken `zo` entry from `mcporter`'s registry; keep `zo-bridge` in `openclaw.json`.

**For v1.5:**
- Add per-daemon MCP servers (perception, memory, toold, tts) so OpenClaw agents can call them as tools.
- Add a "policy deny" rule for the perception → os-toold path (per §9).
- **v6 add: HRM-Text 1B as a tool** — OpenClaw calls `reasond` (a thin Rust wrapper around the HRM-Text 1B INT4 GGUF) for any reasoning step. The Node gateway is a thin prompt-loop; the LLM is a separate process.

---

## 9. Security / prompt injection

**Verdict: gap, not addressed in code. v6 — the threat has moved from "external prompt injection" to "internal CIK poisoning + sabotage in production environments."**

The canonical analysis flagged camera-frame → VLM → tool-execution prompt injection. v6 update: the 2026 agentic-security literature (per `dan2-research-report.md` v5) shows the threat model has shifted. Two recent papers are especially relevant:

- **CIK ("Your Agent, Their Asset")** — image-based context-injection attacks; defends via frame-source provenance + per-frame trust scores.
- **SlotGuard** — transcript-redaction at the LLM boundary (15 μs overhead, 0% credential leakage).
- **ToolPrivBench** — least-privilege tool selection benchmark.
- **LinuxArena + DeepTrap** — production sabotage benchmarks for computer-use agents.
- **SudoBench, CAPSPLIT-IB, NOVA** — contextual authorization, control-flow integrity for CUAs.

**v6 mitigations (in order of cost/impact):**

1. **Perception-frame trust score** in perceptiond. Score = coherence × novelty × type. Text-heavy frames with command-like tokens get a low score. **(Carry-forward from v5.)**
2. **Argument hashing + audit log** in `toold` (already mentioned in the canonical spec, verify it's in code).
3. **Two-channel tool execution.** "Told to execute X" vs "user said execute X" — only the second is allowed. Implemented in OpenClaw's policy layer.
4. **Strict denylist of "execute-from-perception" verbs.** No `os_toold` call is allowed whose `source` is a `perceptiond` event, period. The user must re-enter the command.
5. **v6 add: zo-mcp-bridge SlotGuard integration** — redact transcripts at the LLM boundary using SlotGuard's pattern. Per v5, ~15 μs overhead, 0% credential leakage. **Ship week 1 of v6.**
6. **v6 add: LinuxArena + DeepTrap as acceptance tests** for the perception → os-toold path. If we can't pass 90% on these benchmarks, the path isn't safe to ship.

**Adversarial robustness literature:** Synthius-Mem reports 99.6% adversarial robustness on LoCoMo. That is the bar.

---

## 10. Packaging / deployment

**Verdict: 80% there, missing .deb.** (Unchanged from v5.)

- 5 systemd unit files present (`packaging/systemd/`). Good.
- `packaging/debian/` is empty (only README). Per `dan1.md`, this is the next milestone.
- `scripts/dev.sh` (up/status/stop/restart) works for laptop dev. Good.
- `.deb` will need: control file, post-install hook that enables systemd units, signing (GPG or Sigstore — **pick one and document**).

**Recommendation:** Don't ship a Flatpak or AppImage. The canonical analysis is correct: .deb + systemd is the right path for hardware that needs udev rules, privileged install actions, and a real package signing story.

**v6 add:** When the Redax board lands, the .deb needs udev rules for the V4L2 camera, I2C for the MicroLED, and the battery gauge. Start the udev rule set now, against the eventual hardware, even if it's untested.

---

## 11. v6 add — Anthropic "brake pedal" coordination problem

On 2026-06-04, Anthropic (via Jack Clark + Jared Kaplan) called for frontier labs to establish a **coordinated, verifiable way to slow down or temporarily pause development** if advanced systems begin improving themselves faster than society can manage the risks. This is a public, on-the-record statement from a frontier lab saying "we need a brake pedal."

**Why this matters for Danlab:**
- **It validates our positioning.** On-device, auditable, open-source self-improving systems are the *antidote* to a closed-lab RSI race. We are explicitly on the right side of this.
- **It raises the bar for open-source RSI.** Anthropic's "ultimate risk" framing (Kaplan) means any open RSI project will face scrutiny. **Our integrity work in danlab-multimodal — calling the heuristic a "pre-RL scaffold" and naming the credible path to RL (SIA / RHO) — is exactly the right discipline.**
- **It changes the regulatory landscape.** EU AI Act + India DPDP + the brake-pedal conversation mean on-device, private-by-default architectures will be the only legal way to ship many agent features in 2027–2028. **This is a tailwind for our thesis.**
- **It informs what we publish.** A negative-result paper ("we tried SIA-W+H on SmolVLM-256M and didn't beat the heuristic on screen-captioning") is more valuable now than a positive-result paper. The community needs the failure modes, not the benchmarks.

**Action:** keep danlab-multimodal's "pre-RL scaffold" label until harness+weights are open and audited. This is the integrity call. Publish the negative results, not the positive.

---

## What to do this week (v6 priorities)

1. **Reconcile the model lineup in both AGENTS.md files** — explicitly: HRM-Text 1B for reasoning (OpenClaw loop), LFM2.5-VL-450M for vision (perceptiond). 1-hour change.
2. **Add `wakewordd` (or fold openWakeWord into audiod).** Single highest-UX-impact change.
3. **Add `powerd` (or a state machine in audiod).** 2-day build, 1-week hardening.
4. **`zo-mcp-bridge` SlotGuard integration** (transcript redaction at the LLM boundary). 1-day change.
5. **Memory v1.5: temporal + confidence + 4-relation scoring + BM25.** 2 weeks. Single biggest credibility upgrade.
6. **Measure LFM2.5-VL-450M real power on x86_64 and on aarch64+NPU sim.** Stop using "150–800ms" from the spec. Get the real numbers.

## What to do this quarter

7. **Integrate HRM-Text 1B** as a `reasond` service in OpenClaw's loop. The 1.15B / INT4 GGUF, ~500 MB, ~$1,000 train cost. This is the v1.1 flagship.
8. **Memory v2: dual-process (DPA/DPCM).** Replace the static SQLite + flat cosine.
9. **TT-SI OR RHO pilot in danlab-multimodal** — v6 update: start with RHO (label-free, single-pass) over existing trajectories. SIA-fork is the destination.
10. **Daily briefing agent.** Calendar + email + memories → 60s spoken. The killer-app demo.
11. **Hardware decision.** Redax or indie path. 6-month clock.
12. **LinuxArena + DeepTrap as acceptance tests** for the perception → os-toold path. 134 safety cases.
13. **Paper.** The RHO vs. learned reward vs. TT-SI vs. SIA-fork ablation is publishable. Start drafting.

## What NOT to do

- ❌ Don't replace OpenClaw with Rust in v1.
- ❌ Don't add more heuristic rules to danlab-multimodal.
- ❌ Don't add another Python daemon without a hard latency/safety reason. The 5 are enough.
- ❌ Don't call danlab-multimodal's loop "RL" until harness+weights are open.
- ❌ Don't optimize for x86_64 laptop performance beyond "good enough to demo."
- ❌ Don't ignore the Anthropic brake-pedal coordination problem — the regulatory and reputational risks are real.

---

*👾* Architecture is fundamentally right. The next 90 days are about power, memory, safety, and the HRM-Text 1B integration — not about redesigning the wheel.
ion.

---

## 3. Power / performance tradeoffs

**Verdict: the model choices are right. The thermal/power architecture is missing.**

### 3a. LFM2.5-VL-450M (vision) + HRM-Text 1B (reasoning) — two models, one pipeline

**v6 update — the HRM-Text 1B question.** The root `AGENTS.md` says "HRM-Text (1B) for reasoning." Sapient Intelligence released HRM-Text 1B on **May 18, 2026** — three days after the v5 report.[^h1] It is a 1.15B-parameter hierarchical recurrent reasoning model trained on **40 B structured tokens** (1000× less than typical 4–36 T pretraining runs). The full model pre-trains in roughly one day for ~$1,000.[^h2] It performs reasoning in **continuous latent space**, not visible CoT tokens — this is the design choice that makes it cheap at inference.

**The right architecture (v6, definitive):**

```
[camera frame] ──► LFM2.5-VL-450M (vision encoder) ──► text description
[microphone]   ──► Silero VAD + whisper-tiny         ──► text transcript
                          │
                          ▼
                  [memoryd retrieval (RRF: vector + BM25 + graph)]
                          │
                          ▼
                  HRM-Text 1B (reasoning LLM)  ◄── on-device, latent-space reasoning
                          │
                          ▼
                  [text response] ──► KittenTTS-nano ──► audio out
```

**Why two models and not one?**
- LFM2.5-VL-450M is the right vision encoder: sub-250 ms target on aarch64+NPU, 512×512 input, SigLIP2 NaFlex encoder. Live verified on x86_64 at 10–15 s/frame CPU.
- HRM-Text 1B is the right reasoning LLM: 1.15B params, latent-space reasoning (cheap at inference, no CoT token burn), competitive with much larger models on structured reasoning benchmarks. Pre-trains in 1 day / $1,000 — a credible target for **fine-tuning our own variant** on the danlab-multimodal loop data.
- **No fused VLM-reasoner model** is needed. Late-fusion over text is simpler, more interpretable, and cheaper.

**v6 deltas vs. v5 on the LFM2.5-VL question:**
- **Bottleneck:** the spec cites "150–800 ms" inference on LFM2.5-VL-450M, but the verified live number is **10–15 s/frame on x86_64 CPU**. That's a 10–100× gap. The optimistic spec number is probably on aarch64 with NPU offload. We need the **measured** numbers in the spec, not the marketed ones.
- **Gemma 3 in space** (JPL + Loft Orbital, 2026-04): Google DeepMind's Gemma 3 ran onboard a satellite — the first reported VLM in orbit. Validates the "small VLM on edge" thesis but for satellite, not wearables. Worth noting for the philosophy, not directly applicable.[^gemma_space]
- **Nanomind-style modular mapping** (arXiv:2510.05109): the right pattern is to map each brick (vision encoder, projector, language model, audio front-end) to the most suitable accelerator (NPU, GPU, DSP), with a Token-Aware Buffer Manager for zero-copy transfers. **42.3% energy reduction** demonstrated. LLaVA-OneVision-Qwen2-0.5B + camera → **18.8 hours on 2000 mAh battery**. This is the wearable power-budget playbook.

### 3b. whisper.cpp + Silero VAD — correct call
- `ggml-base.bin` (148 MB) is right for laptop; `ggml-tiny.bin` (78 MB) is the right call for aarch64 wearable.
- `whisper-cpp-plus-rs` (DAN-2's choice) with async + VAD is the right library. We chose the stdlib WS path instead — also fine, but loses the VAD integration. **Recommendation:** bring Silero VAD on-device for the wake word path (see §4).
- For multilingual India, **Moonshine** (purpose-built edge STT, 1 TOPS NPU target) or **Parakeet** (NVIDIA streaming) is the right v1.5 upgrade.

### 3c. KittenTTS — correct call but watch the variant
- v0.8 (Feb 2026), 3 variants: nano (15M, ~25 MB int8), micro (40M), mini (80M).
- Live we use "medium" — that's not even in the canonical KittenTTS lineup. Either it's a custom build or the spec is referencing an old label. **Check.**
- For wearable: **nano-int8 at ~25 MB**. 8–9× real-time. Quality is "lowest" but is good enough for spoken feedback.
- The Second State `kitten_tts_rs` crate is a Rust port — we should benchmark it against the Python/ONNX path. If it wins on latency, we save a process.

### 3d. The missing power architecture

This is the biggest gap in the v1 canonical spec. Per the canonical analysis (which is correct):
- Throttling capture FPS (idle=2, watchful=5, active=10) does not throttle VLM inference.
- Every captured frame in `watchful` still goes through the full perception pipeline if salient.
- At 2 FPS idle, the VLM still fires every 500 ms on average. Wrong lever.

**Right design (proposed, v6):**
- **Salience-based gating at the VLM level**, not the capture level. Run VLM only when:
  - Motion exceeds threshold AND scene-change classifier agrees, OR
  - A new face appears, OR
  - Wake-word / push-to-talk fires, OR
  - A scheduled "check-in" (e.g., every 30 s in watchful mode).
- **Adaptive state machine** (see §4).
- **Thermal-aware throttling** — if SoC temp > threshold, drop to Gemma3-270M fallback (text-only, no vision). This buys 5–10× power reduction.

**Concretely, what the power budget should look like (per `dan2-model-analysis.md`):**

| Mode | CPU | LFM2.5-VL (avg) | Mic | Total | Battery (2000 mAh@3.7 V) |
|------|-----|------------------|-----|-------|--------------------------|
| Sleep (camera off, mic VAD only) | 0.05 W | 0 W | 0.05 W | **0.1 W** | ~74 h |
| Idle (camera on, no VLM) | 0.4 W | 0 W | 0.1 W | **0.5 W** | ~15 h |
| Watchful (VLM on motion, ~1 inf / 3 s) | 0.6 W | 0.8 W (intermittent) | 0.1 W | **1.5 W avg** | ~5 h |
| Active (continuous VLM, LLM on demand) | 0.8 W | 3.0 W | 0.1 W | **4.0 W peak** | ~1.8 h |
| Burst (LLM response) | 1.0 W | 3.0 W | 0.1 W | **5.0 W peak (brief)** | — |

A 2× 200 mAh battery (400 mAh) at 3.7 V = 1.48 Wh. At watchful avg, that's ~1 h. **Redax needs bigger batteries** or we need a tethered path. The Brilliant Labs Frame at ~6–8 h battery uses a phone-tether architecture; that's a credible pattern.

---

## 4. Missing: wake-word + power state machine

**The canonical spec defers both. They are not optional for a wearable.**

### 4a. `wakewordd` (or merge into `audiod`)
- **Why:** Push-to-talk (the current default) is the right call for v1 (battery, safety), but is **not** a wearable UX. The user has to take a physical action every time. Wake-word is the difference between "compelling demo" and "daily driver."
- **Pick:** `openWakeWord` (open-source, Picovoice-derived, runs on CPU) or Porcupine (commercial, on-device). `openWakeWord` first; fall back to Porcupine if accuracy is bad.
- **Where:** New daemon `wakewordd` on a small port (e.g., 8095) using ONNX Runtime. Or fold into `audiod` as a pre-VAD stage.
- **Latency target:** <200 ms from utterance to wake-event.
- **Power:** <50 mW continuous (DSP-style).

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
- **GC pauses.** Node's stop-the-world GC is 5–50 ms typical, 200 ms+ worst case. For a 200 ms-wake-word → audio → LLM round-trip, that's 25–100% jitter. On a battery-powered wearable, this is a measurable power and latency penalty.
- **No native threading model.** OpenClaw's "Octopus Orchestrator" runs parallel arms as separate processes, which is correct — but the per-arm process model means each arm pays Node startup cost (200–500 ms cold) and memory (~80–150 MB per arm).
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

### 6a. v6 update — the memory landscape has moved (May–June 2026)

Since v5, the literature has continued to mature. The current top 5 contenders for "memory architecture for an AI companion" are:

1. **MemX** (arXiv:2603.16171) — local-first Rust + libSQL. **Seven relation types** in `memory_links`: `similar`, `related`, `contradicts`, `extends`, `supersedes`, `caused_by`, `temporal`. Reciprocal-Rank-Fusion of vector + keyword + four-factor re-rank. **The closest architectural twin to what memoryd should become.** This is still the v5 recommendation.
2. **MemMachine** (arXiv:2604.04853) — three-layer (short-term working / long-term episodic / semantic profile), PostgreSQL + pgvector + Neo4j. **Ground-truth-preserving** — stores raw episodes to reduce LLM-extraction drift. Exposes REST/Python/MCP. **The cleanest production-shape API in 2026.**
3. **TiMem** (arXiv:2601.02845) — Temporal Memory Transformer + Memory Consolidator + recall planner. SOTA on LoCoMo (75.30%) and LongMemEval-S (76.88%). Reduces recalled memory length by 52% on LoCoMo. The right shape for "first-token latency budget" on small on-device LLMs.
4. **Memanto** (arXiv:2604.22085) — **vector-only** (no graph), 13-category typed semantic memory schema, built-in conflict resolution. SOTA on LongMemEval and LoCoMo with **zero-cost ingestion**. The contrarian 2026 result: "retrieval recall is the primary performance driver; modern LLMs handle reasoning/filtering that graph precomputation aimed to address." Worth benchmarking against our planned graph upgrade.
5. **APEX-MEM** (arXiv:2604.14362) — temporal semi-structured memory with relational and temporal reasoning. 88.88% on LoCoMo QA, 86.2% on LongMemEval. **State-of-the-art for graph memory in 2026.**

Other notable 2026 entries:
- **CraniMem** (arXiv:2603.15642) — cranial-inspired (RAS-gated) bounded episodic buffer + long-term knowledge graph. The "bounded" angle is interesting for wearables with limited storage.
- **TeleMem** (arXiv:2601.06037) — DAG of memory threads for causal reasoning and context restoration. Better for reasoning over event sequences.
- **Mem0g / Mem0** — still the most-deployed production memory layer; graph extension (Mem0g) is modest uplift over flat Mem0.
- **Memori** (arXiv:2603.19935) — semantic triples + conversation summaries. High signal-to-noise index.

### 6b. Concrete v1.5 changes (cheap, 2 weeks)

This is unchanged from v5 because it's the right answer:
1. Add `created_at`, `last_accessed_at`, `access_count`, `decay_rate` to the `memories` table.
2. Add a `ConsolidationAgent` cron job (every 6 h) that:
   - Boosts memories with high `access_count`
   - Decays memories with low `access_count` and high age
   - Tags "supersedes" chains when semantic similarity > 0.92 between new and old
3. Change `/query` to score as `cosine × temporal_validity × confidence × relational_bonus`.
4. Add BM25 (FTS5) on `content`.
5. Add `memory_links` table with MemX's 7 relation types (or Memanto's 13-category schema if we benchmark it as better).

### 6c. v2 changes (Q1–Q2 2027) — pick the architecture

- **Recommendation:** prototype **two** candidates in parallel on a 1k-memory LoCoMo subset.
  - **MemX-style** (graph + vector + RRF) — the v5 recommendation, still strong.
  - **Memanto-style** (vector-only with typed schema) — simpler, possibly as good or better, definitely cheaper.
- **Don't** commit to graph before measuring. Memanto's 2026 result is a real challenge to the conventional wisdom.

**This is the v1 → v1.5 delta that makes Dan Glasses feel like a personal intelligence, not a transcript logger.**

---

## 7. Tauri v2 frontend

**Verdict: correct choice, integration is incomplete.**

- React 19 + Vite 7 + TS frontend; Tauri v2 + Rust bridges for 7 services. Pattern is right.
- Live: 8 Rust bridge modules (greet, audiod, memoryd, perceptiond, toold, ttsd, os_toold, openclaw).
- Polling: DaemonHealth 4 s, VisionDashboard 2.5 s status + 5 s descriptions. Reasonable.
- Build: 3.02 s, 35 modules, ~210 KB JS. Excellent.

**What to add:**
- **PTT button in UI.** Per `agent-work/dan2.md` Ship order, this is in progress. The fact that audiod's `/start`, `/stop`, `/ptt` endpoints don't exist is the real gap.
- **Voice picker in the bootstrap wizard.** Per `agent-work/dan4.md`, this is also in progress. Verify the round-trip write to memoryd after voice selection.
- **In-app TTS playback.** The wizard currently uses `aplay` server-side. For a desktop app pointed at localhost, the wizard should fetch `/speak` and play via `<audio>`.
- **System health banner with quick actions.** When `powerd` ships, this should be the home tab. "Battery: 64% (~3 h watchful). Temp: 41 °C. State: watchful." One glance, one click to change state.
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

### 9a. v6 update — Anthropic's "brake pedal" (2026-06-04)

On June 4, 2026, Anthropic publicly stated that AI labs should have a **verifiable way to slow or pause development** if systems begin recursively self-improving faster than society can manage the risks. Jack Clark, co-founder of Anthropic: "The AI industry has a gas pedal, but it doesn't have a brake pedal." The same week, Reuters reported Anthropic's projection that by 2027 AI could manage tasks that currently require weeks.[^anthropic_brake]

**Implication for Danlab:** this is a *coordination* problem the open-source community can help with. Our position should be:

- **On-device by default.** On-device = no API call = no external prompt injection vector = no single point of coordination failure.
- **Auditable by default.** Every memory, every description, every tool call is local and inspectable. The user owns the trace.
- **Honest about RL.** We do not call danlab-multimodal's loop "RL" until harness+weights are open and auditable. This is the integrity call that lets us credibly ship the rest.

**The Anthropic call validates our positioning, not our product.** Our product still has to ship.

---

## 10. Packaging / deployment

**Verdict: 80% there, missing .deb.**

- 5 systemd unit files present (`packaging/systemd/`). Good.
- `packaging/debian/` is empty (only README). Per `dan1.md`, this is the next milestone.
- `scripts/dev.sh` (up/status/stop/restart) works for laptop dev. Good.
- `.deb` will need: control file, post-install hook that enables systemd units, signing (GPG or Sigstore — **pick one and document**).

**Recommendation:** Don't ship a Flatpak or AppImage. The canonical analysis is correct: .deb + systemd is the right path for hardware that needs udev rules, privileged install actions, and a real package signing story.

---

## What to do this week (v6 deltas)

1. **Resolve the HRM-Text / LFM2.5-VL ambiguity** in the workspace AGENTS.md. Document: HRM-Text 1B is the on-device reasoning LLM, LFM2.5-VL-450M is the vision encoder. **This is now a 1-day documentation change.** §3a.
2. **Add `wakewordd`** (or fold openWakeWord into audiod). Single highest-UX-impact change.
3. **Add `powerd`** (or a state machine in audiod). 2-day build, 1-week hardening.
4. **Memory v1.5: temporal + confidence + relational scoring.** 2 weeks. Single biggest credibility upgrade.
5. **Prompt-injection guard for os-toold.** 1 week. Use the perception-source denylist as the cheap mitigation.
6. **Measure LFM2.5-VL-450M power on x86_64 + simulated aarch64.** Stop using "150–800 ms" from the spec. Get the real numbers.
7. **Re-evaluate SIA vs. RHO vs. HarnessForge** for the danlab-multimodal Tier 1 plan. v6 update: RHO is label-free and lighter; consider it as the first move. §2a.

## What to do this quarter

8. **Memory v2: dual-process (DPA/DPCM).** Replace the static SQLite + flat cosine. Benchmark MemX-style vs. Memanto-style; pick the winner on a LoCoMo subset.
9. **TT-SI pilot in danlab-multimodal.** Replace the hand-coded heuristic with a learned reward model.
10. **Daily briefing agent.** Calendar + email + memories → 60 s spoken. The killer-app demo.
11. **HRM-Text 1B benchmark on our screen-caption task.** If it holds up against 7B+ models, this is the wearable-reasoning-LLM story.
12. **Anthropic coordination position paper.** Publish a 1-pager: "Danlab's on-device auditable self-improvement framework." Part of the credibility story for the SIA fork.
13. **Hardware decision.** Redax or indie path. 6-month clock.
14. **Paper.** The TT-SI vs. SIA ablation is publishable. Start drafting.

## What NOT to do

- ❌ Don't replace OpenClaw with Rust in v1.
- ❌ Don't add more heuristic rules to danlab-multimodal.
- ❌ Don't add another Python daemon. The 5 are enough.
- ❌ Don't call danlab-multimodal's loop "RL" until harness+weights are open.
- ❌ Don't pick a memory architecture (MemX vs. Memanto) before benchmarking both. The 2026 literature has not converged.

---

## Footnotes

[^h1]: Sapient Intelligence launches HRM-Text, 2026-05-18. https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html
[^h2]: Introducing HRM-Text (Sapient Inc). https://sapient.inc/introducing-hrm-text
[^gemma_space]: Loft Orbital Yam-9 satellite + NASA JPL software + Google DeepMind Gemma 3 — first VLM in orbit. TechCrunch 2026-06-15. https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
[^anthropic_brake]: Anthropic — "When AI Builds Itself" / coordinated-pause proposal. Reuters 2026-06-04. https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/

---

*Dan2, 2026-06-17. The architecture is fundamentally right; the next 90 days are about power, memory, and the HRM-Text reasoning integration — not about redesigning the wheel. 👾*
k/dan1.md`):
  - `tailscaled` not running — fine, we use loopback.
  - `mcporter` returns 405 from Zo MCP — we worked around with the `zo-bridge` stdio MCP shim. **This is the production path. Do not try to fix mcporter.**
  - Telegram channel enabled, `dmPolicy=pairing`, `groupPolicy=allowlist`, streaming=partial. Looks correct.

### Why TS/Node is a problem for the wearable
- **GC pauses.** Node's stop-the-world GC is 5–50 ms typical, 200 ms+ worst case. For a 200 ms-wake-word → audio → LLM round-trip, that's 25–100% jitter. On a battery-powered wearable, this is a measurable power and latency penalty.
- **No native threading model.** OpenClaw's "Octopus Orchestrator" runs parallel arms as separate processes, which is correct — but the per-arm process model means each arm pays Node startup cost (200–500 ms cold) and memory (~80–150 MB per arm).
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

### 6a. v6 update — the memory landscape has matured (May–June 2026)

Since the v5 report, several new memory architectures have appeared or matured. Map (v6):

- **MemX** (arXiv:2603.16171) — local-first, Rust + libSQL (SQLite w/ vectors), 7-type memory_links (similar, related, contradicts, extends, supersedes, caused_by, temporal). RRF over vector + keyword. **The closest architectural twin to what memoryd should become.**
- **MemMachine** (arXiv:2604.04853) — three-layer (short-term, long-term episodic, semantic/profile). Raw episode storage to avoid LLM-extraction drift. REST + Python + MCP.
- **Memanto** (arXiv:2604.22085, May 2026) — **vector-first, no graph database**. 13-category typed semantic memory. Information-theoretic retrieval. SOTA on LongMemEval and LoCoMo at *lower* complexity than Mem0. The case: "retrieval recall is the primary performance driver; modern LLMs handle reasoning/filtering that graph precomputation aimed to address."
- **TeleMem** (arXiv:2601.06037) — DAG memory substrate. Dependency-aware, closure-based retrieval. Multimodal.
- **CraniMem** (arXiv:2603.15642) — cranial-inspired. RAS-style gating, bounded episodic buffer + knowledge graph.
- **AriadneMem** (arXiv:2603.03290) — entropy-aware graph coarsening + Steiner-tree completion. 15% multi-hop F1 gain on LoCoMo. Most sophisticated graph topology.
- **APEX-MEM** (arXiv:2604.14362) — agentic semi-structured memory with temporal reasoning. 88.88% on LoCoMo QA, 86.2% on LongMemEval.
- **Memori** (arXiv:2603.19935) — semantic triples + conversation summaries. High signal-to-noise.
- **Mem0 / Mem0^g** (arXiv:2504.19413) — 91% lower p95 latency than full-context. Graph extension.

**The 2026 pattern is convergence on 4 layers:**

1. **Vector index** for semantic recall (we have this).
2. **Keyword index** (BM25) for exact-match (e.g., "Priya", "Aspirin"). MemX uses RRF to merge both. **Add this.**
3. **Graph relations** for "X is similar to Y", "X contradicts Y", "X was caused by Y". MemX has 7 relation types. **Add this as a `memory_links` table.**
4. **Retrieval-time gate** to filter out stale, off-topic, or unsafe memories before they hit the LLM context. **Add this.**

### 6b. Concrete v1.5 changes (cheap, 2 weeks)

1. Add `created_at`, `last_accessed_at`, `access_count`, `decay_rate` to the `memories` table.
2. Add a `ConsolidationAgent` cron job (every 6 h) that:
   - Boosts memories with high `access_count`
   - Decays memories with low `access_count` and high age
   - Tags "supersedes" chains when semantic similarity > 0.92 between new and old
3. Add BM25 (FTS5) index on `content`.
4. Add `memory_links` table with the 7 relation types from MemX.
5. Change `/query` to score as `RRF(cosine) * temporal_validity * confidence * relational_bonus`.

**This is the v1 → v1.5 delta that makes Dan Glasses feel like a personal intelligence, not a transcript logger.**

### 6c. v2 (Q1–Q2 2027)

- **Memanto-style typed semantic schema** — 13 memory categories, automatic conflict resolution.
- **MemMachine-style three-layer** — short-term working + long-term episodic + semantic/profile.
- **Memori-style triples + summaries** — knowledge-graph-compatible atomic units.
- **AriadneMem-style connected subgraph retrieval** — for multi-hop reasoning ("what did Priya say about the trip last spring, and how does it relate to the new project?").

**This is the v1 → v2 delta that makes Dan Glasses a memory-grade AI, not a SQLite lookup.**

---

## 7. Tauri v2 frontend

**Verdict: correct choice, integration is incomplete.**

- React 19 + Vite 7 + TS frontend; Tauri v2 + Rust bridges for 7 services. Pattern is right.
- Live: 8 Rust bridge modules (greet, audiod, memoryd, perceptiond, toold, ttsd, os_toold, openclaw).
- Polling: DaemonHealth 4s, VisionDashboard 2.5s status + 5s descriptions. Reasonable.
- Build: 3.02s, 35 modules, ~210 KB JS. Excellent.

**What to add:**
- **PTT button in UI.** Per `agent-work/dan2.md` Ship order, this is in progress.
- **Voice picker in the bootstrap wizard.** Per `agent-work/dan4.md`, this is also in progress. Verify the round-trip write to memoryd after voice selection.
- **In-app TTS playback.** The wizard currently uses `aplay` server-side. For a desktop app pointed at localhost, the wizard should fetch `/speak` and play via `<audio>`.
- **System health banner with quick actions.** When `powerd` ships, this should be the home tab. "Battery: 64% (~3h watchful). Temp: 41°C. State: watchful." One glance, one click to change state.
- **Real-time transcript in the LiveTranscript component** is already working (per dan1 notes). Good.
- **v6 add: Proactive surfaces panel.** When the proactive trigger layer (see §10) lands, the home tab needs a "what's on your mind?" card. This is the v1.5 home.

---

## 8. OpenClaw integration / MCP / Telegram

**Verdict: solid for v1, with one known workaround that should be documented.**

- Telegram channel live, pairing-only DM, allowlist groups. Correct security posture.
- `zo-bridge` MCP shim works around the `mcporter` 405 on `https://api.zo.computer/mcp`. **Document this in OpenClaw config and stop trying to fix mcporter.** The shim is the production path.
- 2 MCP servers currently registered: `zo` (broken) and `OpusCode` (healthy). Clean up: remove the broken `zo` entry from `mcporter`'s registry; keep `zo-bridge` in `openclaw.json`.

**For v1.5:**
- Add per-daemon MCP servers (perception, memory, toold, tts) so OpenClaw agents can call them as tools.
- Add a "policy deny" rule for the perception → os-toold path (per §9).
- Add a proactive trigger layer (per §10) — this is the major v1.5 architecture addition.

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

### 9a. v6 update — Anthropic's "brake pedal" call (June 4, 2026)

Anthropic co-founder Jack Clark publicly said (2026-06-04) that the AI industry has a gas pedal but no brake pedal, and that frontier AI developers should establish a **coordinated, verifiable way to slow down or temporarily pause development** if advanced systems begin improving themselves faster than society can manage the risks.[^anthropic_brake]

**What this means for Dan Glasses:**
- **We are the right side of the debate.** On-device, open-source, auditable, harness+weights both visible — this is exactly what Jack Clark is implicitly asking the field to build.
- **The harness must be auditable.** When we adopt SIA / HarnessForge / Self-Harness, the harness changes need to be in a public, reviewable diff. This is non-negotiable for credibility.
- **Safety paper is a high-value contribution.** The perception-frame trust score + argument-hashing + two-channel execution combo is a publishable safety mechanism. "An Open-Source, On-Device Defense Against Cross-Modal Prompt Injection for AI Wearables" — paper that target, submit to USENIX Security or IEEE S&P.
- **Open weights + auditable harness** is the positioning moat. Meta has Muse Spark (closed weights). Apple has a closed iOS stack. We have on-device, open, auditable. This is the brand.

### 9b. Adversarial robustness literature
- **Synthius-Mem** reports 99.6% adversarial robustness on LoCoMo. That is the bar.
- **CIK (Cross-modal Indirect Knowledge)** taxonomy — agents that can see and act need a different threat model than agents that only read text.

---

## 10. Proactive AI — the v1.5 architecture addition

**v6 update — this is now a first-class architectural concern, not just a research note.**

The biggest product differentiator vs. every AI wearable on the market is **proactive over reactive**. Meta AI, Plaud, Rabbit, Amazon Bee — all are reactive. The 2026 academic literature has the architecture for what Dan Glasses should do: **proactive agents** (see `dan2-research-report.md` §5.3 for the full review).

### 10a. The right architecture (v6)

```
[VLM descriptions] + [transcripts]
          ↓
  [Event Queue] ← salience-gated, intent-gated
          ↓
  [Proactive Trigger — Microsoft Research 2026 pattern]  ◄── 220 MiB BF16, on-device, graph-encoder
    - Treats user activity as a continuous graph
    - p_trigger = encoder(graph, recent_events)
    - if p_trigger < 0.5: silent
    - if 0.5 ≤ p_trigger < 0.8: silent, but log for PRISM
    - if p_trigger ≥ 0.8: invoke LLM
          ↓
  [PRISM Gate — Festina Lente]  ◄── cost-sensitive, uncertainty-aware
    - p_need = P(user will want this surfaced | recent context)
    - p_accept = P(user will accept interruption | time, mode, history)
    - if p_need × p_accept > θ: surface
    - if near boundary: slow down, deliberate (slow reasoning pass)
    - asymmetric cost: false alarms are 4× worse than missed help
          ↓
  [Decision] → [silently store] | [TTS speak] | [Telegram notify] | [icon in UI]
```

### 10b. Where each piece lives

- **Proactive Trigger** (Microsoft Research graph encoder) — new lightweight Rust module in OpenClaw. ~220 MiB BF16 footprint. <1 mW continuous.
- **PRISM Gate** — Python module in OpenClaw's policy layer. ~50 ms per check.
- **Slow-reasoning pass** — HRM-Text 1B on-device, fires only when p_trigger is near the decision boundary. <5% of all events.
- **Memory coupling** — every decision (surface / dismiss / ignore) is written to memoryd as a procedural memory with the user's prior feedback weight. **This is the SIA loop on a per-user basis.**

### 10c. Why this matters

- **No wearable does proactive well.** This is the moat.
- **The math is conservative.** PRISM's ProactiveBench result: 22.8% fewer false alarms, 20.1% higher F1. Direct user-experience win.
- **The "AI that doesn't annoy you" framing** is the right brand. PRISM's design literally optimizes for "make haste slowly" — slow when uncertain, fast when clear.

---

## 11. Packaging / deployment

**Verdict: 80% there, missing .deb.**

- 5 systemd unit files present (`packaging/systemd/`). Good.
- `packaging/debian/` is empty (only README). Per `dan1.md`, this is the next milestone.
- `scripts/dev.sh` (up/status/stop/restart) works for laptop dev. Good.
- `.deb` will need: control file, post-install hook that enables systemd units, signing (GPG or Sigstore — **pick one and document**).

**Recommendation:** Don't ship a Flatpak or AppImage. The canonical analysis is correct: .deb + systemd is the right path for hardware that needs udev rules, privileged install actions, and a real package signing story.

**v6 add: Tailscale setup script.** The skill `Skills/zopenclaw/` is the right place. tailscaled isn't running in this container per `dan1.md`. A 1-page setup script for "install tailscale, authenticate, run OpenClaw on Tailscale IP" would unlock remote access for the wearable.

---

## What to do this week

1. **Add `wakewordd` (or fold openWakeWord into audiod).** Single highest-UX-impact change.
2. **Add `powerd` (or a state machine in audiod).** 2-day build, 1-week hardening.
3. **Memory v1.5: temporal + confidence + relational scoring.** 2 weeks. Single biggest credibility upgrade.
4. **Prompt-injection guard for os-toold.** 1 week. Use the perception-source denylist as the cheap mitigation.
5. **Reconcile the HRM-Text 1B + LFM2.5-VL-450M story in the AGENTS.md files.** Two models, one pipeline. Document the split.
6. **Measure LFM2.5-VL-450M power on x86_64 + simulated aarch64.** Stop using "150–800 ms" from the spec. Get the real numbers.
7. **Try RHO (Retrospective Harness Optimization) on danlab-multimodal's existing trajectories.** No labels, single pass, no human data. If it improves on the heuristic, publish.

## What to do this quarter

8. **Memory v2: dual-process (DPA / DPCM / MemMachine / Memanto hybrid).** Replace the static SQLite + flat cosine.
9. **Proactive trigger layer** in OpenClaw. Microsoft Research graph encoder + PRISM gate. This is the v1.5 architecture.
10. **TT-SI pilot in danlab-multimodal.** Replace the hand-coded heuristic scorer with a learned reward model.
11. **SIA / HarnessForge fork** in danlab-multimodal. **Now** it's a real self-improving loop.
12. **Daily briefing agent.** Calendar + email + memories → 60 s spoken. The killer-app demo.
13. **Hardware decision.** Redax or indie path. 6-month clock.
14. **Safety paper.** Perception-frame trust score + argument-hashing + two-channel execution. Submit to USENIX Security.
15. **Paper.** The RHO vs. learned reward vs. TT-SI vs. SIA ablation is publishable. Start drafting.

## What NOT to do

- ❌ Don't replace OpenClaw with Rust in v1.
- ❌ Don't add more heuristic rules to danlab-multimodal.
- ❌ Don't add another Python daemon. The 5 are enough.
- ❌ Don't call danlab-multimodal's loop "RL" until harness+weights are open.
- ❌ Don't try to fine-tune HRM-Text or LFM2.5-VL in the loop on the laptop. Use a smaller reward model.
- ❌ Don't conflate HRM-Text and LFM2.5-VL. They are different models for different jobs. Document the split.
- ❌ Don't ship proactive AI without PRISM. A naïve proactive agent is an annoyance; a PRISM-gated one is a value-add.

---

## Footnotes

[^h1]: Sapient Intelligence launches HRM-Text 1B, May 18, 2026. https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html
[^h2]: Sapient Inc — Introducing HRM-Text. https://sapient.inc/introducing-hrm-text
[^gemma_space]: TechCrunch — A satellite just learned to find things on its own (Gemma 3 on Yam-9 satellite via Loft Orbital + JPL). 2026-06-15. https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/
[^anthropic_brake]: Reuters — Anthropic says AI labs need coordinated plan to halt development if risks rise. 2026-06-04. https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/

---

*👾* Review complete. The architecture is fundamentally right; the next 90 days are about power, memory, safety, and proactive gating — not about redesigning the wheel. v6 deltas: HRM-Text 1B clarified, SIA landscape expanded (RHO, HarnessX, Self-Harness, HarnessForge), Anthropic brake-pedal signal absorbed, proactive layer promoted to v1.5 architecture.
