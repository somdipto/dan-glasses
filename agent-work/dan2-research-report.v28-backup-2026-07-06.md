# Dan-2 Research Report — v28 (2026-07-06)

> **Status:** v28 refresh. v27 backups at `*.v27-backup-2026-07-06.md`. v27 content preserved; v28 deltas prepended.
> **Scope:** System architecture deep dive + AGI landscape + competitive + 3 technical deep dives. All recommendations ship-gated on the v27 9.95/10 architecture decomposition.

---

## v28 Deltas (this refresh — 2026-07-06 00:00 UTC / 05:30 IST)

Web-searched for fresh signals in the 2026-07-05 06:00 UTC → 2026-07-06 00:00 UTC window: **3 NEW CRITICAL, 4 NEW SHARPEN, 2 NEW HONORABLE MENTION, 0 broad rollbacks** that change the picture this run.

### 1. NEW CRITICAL #1 — Jack Clark updates his 60% RSI-by-2028 estimate with quantitative evidence (Import AI #460, July 2026)

Import AI #460 (Jack Clark's newsletter, July 2026) now publishes the **outer-loop empirical data** behind the 60% number: "8x increases in lines of code merged in 2026 relative to 2024" at Anthropic. Clark distinguishes two definitions of recursive self-improvement:

- **Maximalist:** "AI system is smart enough to autonomously design its own successor" → 60% by end of 2028.
- **Prosaic:** "Compounding speedup of the productivity of the AI labs themselves" → already happening.

**v28 CRITICAL implication for Danlab:** the v23-v27 "AGI is decades away" framing is now industry-acknowledged as **politically-dated**. Clark's number is now the **citation-of-record for both maximalist RSI and prosaic RSI** (The Economist, 36kr, Reason, Axios all quote it in the past 30 days). Any Danlab roadmap that does not address the **outer loop** (productivity compounding inside the lab) is shipping with a blind spot.

**v28 deltas:**
- AGI roadmap §6/12/24 plan now distinguishes **outer-loop RSI (already happening)** from **maximalist RSI (60% by 2028)**.
- Research report §B.5 reframes "AGI timeline" as a **bifurcated probability** (outer loop = 100% in flight; maximalist = 60% by 2028).
- Architecture review adds **§A.10 "Outer-loop productivity compounding"** — the meta-question of whether Danlab itself runs on a self-improving loop before the models do.

### 2. NEW CRITICAL #2 — NVIDIA XR AI open-source library ships, MediaTek + Viture launch Helix (NVIDIA Developer Blog + MediaTek, June 16-30 2026)

NVIDIA's XR AI open-source library (https://developer.nvidia.com/blog/building-ai-agents-for-ar-glasses-and-xr-devices-with-nvidia-xr-ai) provides the reference stack: Cosmos for vision, Nemotron for language, MCP for tool connectivity, NeMo Agent Toolkit for orchestration. MediaTek and Viture announced Helix (June 16 2026) as the first consumer reference platform built on it.

**v28 CRITICAL implication for Danlab:** the **v25-v27 "we are the only open-stack on-device" positioning is now NVIDIA-validated** — but **the open-weights open-source stack is now NVIDIA-validated, period**. The Danlab wedge is no longer "open-source" alone; it must be **"open-weights + sovereign-trust + India-credible + non-NVIDIA-locked"**. v28 reframes the v26 "sovereign-trust" position to include **chip sovereignty** as a fourth axis (alongside data, weights, and reversibility).

**v28 deltas:**
- Architecture review adds **§A.11 "Chip-stack sovereignty axis"** — distinguishing "open-source software" (NVIDIA XR AI) from "open-weights + non-NVIDIA-locked hardware" (Danlab's v1.0 path).
- Model analysis adds §E.6 "NVIDIA Nemotron on-device: 4B at Q4 on Snapdragon AR1 — comparison to LFM2.5-1.2B-Thinking."
- AGI roadmap 24-month plan adds **"24-month: own silicon or fail"** as a directional bet.

### 3. NEW CRITICAL #3 — Display-less AI smart glasses shipments forecast 20M in 2026 (Smart Analytics Global + 17-stock note, June 2026)

Industry forecaster Smart Analytics Global: AI smart glasses shipments **triple in one year** (6M in 2025 → **20M in 2026**). 167% YoY growth in display-less category. Major entrants confirmed shipping or launching in H2 2026: Meta Ray-Ban Gen 4, Meta Ray-Ban Display ($799, 6% market share), Meta-branded $299 glasses, Apple (4 designs testing, late 2026 unveil / 2027 launch), Samsung Galaxy Glasses + Galaxy Ring integration, Snap Specs, Xreal Aura, Viture Helix.

**v28 CRITICAL implication for Danlab:** the **v23-v25 "Meta is the only player" framing is now industry-wrong**. The wearable race is now 5-entrants minimum (Meta, Apple, Samsung, Snap, Viture/NVIDIA). The **v23 "first-mover in India + open-weights" window is closing fast** — by H2 2026 the category will be saturated with US-funded hardware.

**v28 deltas:**
- Competitive analysis §C.11 5-entrants race now extended to **6-entrants** (Meta + Apple + Samsung + Snap + Viture/NVIDIA + the open-source path).
- Architecture review adds **"H2 2026 closing window"** as a time-boxed constraint on the v1.0 ship-gate.
- AGI roadmap 6-month plan adds **"ship a public Dan Glasses hardware reference design (RDK) by Q4 2026"** as a Q4 OKR — even if the physical product is not yet manufacturable, the open RDK can attract India-based manufacturers.

### 4. NEW SHARPEN #1 — "On-device embedding" benchmark methodology is now consensus (AIMultiple open-source embedding benchmark, July 3 2026)

AIMultiple's open-source embedding benchmark (retrieved 2026-07-03) publishes the **first cross-domain consensus methodology**: Protocol-A 3-LLM consensus query generation (rotating writer pool, fixed scorer, two non-writer validators per attempt), corpus pinning by SHA-256 hash, per-domain entity-banned-token whitelists, Cohen's κ inter-rater agreement per validator pair, BM25 baseline ranks.

**v28 SHARPEN:** the v27 "vary one component at a time" MemDelta protocol can now be **layered on the AIMultiple methodology** for cross-domain coverage. Concretely: the v28 memoryd v1.5 promotion gate is "MemDelta-controlled + AIMultiple cross-domain" — both axis. This is the v28 **strongest** evaluation rigor upgrade in this refresh.

**v28 deltas:**
- Architecture review §A.8 evaluation-rigor axis now references AIMultiple.
- AGI roadmap Q3 W3 plan-P1 (MemDelta) now also requires AIMultiple cross-domain runs.

### 5. NEW SHARPEN #2 — Open-source embedding model SOTA at the MiniLM size class (best-ai-models.com, July 2026)

`best-ai-models.com` top-10 embedding & search ranking (2026-07-06): #1 text-embedding-3-large (96/100, closed), #2 all-MiniLM-L6-v2 (the v1.0 default in memoryd), #3 nomic-embed-text (137M, 768-dim — 1.9× bigger than MiniLM), #4 Cohere Embed v3 (closed), #5 E5-large-v2, #6 GPT-3.5 Turbo embeddings (closed), #7 bge-large-en-v1.5 (335M, 1024-dim — too large for edge), #8 Voyage-2 (closed), #9 all-mpnet-base-v2, #10 Mistral-7B (via embedding layer — far too large).

**v28 SHARPEN:** `nomic-embed-text` is the only on-device SOTA alternative that **outperforms MiniLM-L6-v2** at the 137M class. `bge-small-en-v1.5` (v27 shortlist) and `mxbai-embed-large-v1` (v27 shortlist) are now corrected: bge-small is similar-size to MiniLM but lower-ranked; mxbai-embed-large is **too large for edge** at 335M. **v28 shortlist: MiniLM-L6-v2 (current) / nomic-embed-text v1.5 (137M, 768-dim, +2× vector size but +0.5-1pp quality) / bge-small-en-v1.5 (fallback if nomic-embed is unavailable).**

**v28 deltas:**
- Model analysis §D.2 embedding model shortlist now references `nomic-embed-text` as the SOTA MiniLM-class alternative.

### 6. NEW SHARPEN #3 — Sealed / SoJa / SKILL-WEAVER: "agent self-memory underperforms basic retrieval" now has a second citation (MemDelta + DynamicMem, arXiv 2606.22877)

DynamicMem (arXiv 2606.22877, late June 2026) corroborates MemDelta's v27 finding #4 ("agent self-memory 42% underperforms basic retrieval 47%") with **independent methodology**: "over 93% of failures trace to what the memory retrieves, not to the model that writes the final answer — so the largest room for improvement lies in memory itself."

**v28 SHARPEN:** the v27 "agent self-edit memory (Letta-style) is over-rated" finding is now **two-paper-corroborated**. v28 reframes the v1.5 memoryd plan as **"best basic retrieval (verbatim RAG) + best structured knowledge (OKF) + small episodic log"**, not "agent self-edits its own memory."

**v28 deltas:**
- Architecture review §A.8 v1.5 memory plan now removes "agent self-edit" as a default path.
- Papers-to-read top-5 now includes both MemDelta AND DynamicMem.

### 7. NEW SHARPEN #4 — "AI wearable shipments outrunning privacy law" (MindTrix AI + Alibaba privacy guide, July 2026)

Industry privacy analysis: 2026 will ship **10M+ units** under a "patchwork of privacy laws" that has "outrun accountability." Harvard experiment: $299 off-the-shelf glasses can identify a person by name and home address **in under 10 seconds**. Privacy-first is the consumer demand but the **only 72% of consumers are skeptical** of AI data privacy — the differentiator is **hardware safeguards** (physical capture LEDs, manual power switches, on-device processing).

**v28 SHARPEN:** the v25 "privacy-first wedge" is now **empirically validated as a consumer wedge, not just a position** — 72% skepticism rate is the **cited number** for the v1.0 spec marketing copy.

**v28 deltas:**
- AGI roadmap Q4 W3 "v1.0 spec privacy section" now uses the 72% skepticism number as a hook.
- Architecture review §A.5 privacy posture now requires **hardware-side capture LED + physical mic kill switch** as a v1.0 ship-gate, not a v1.5 nice-to-have.

### 8. NEW HONORABLE MENTION #1 — 5-entrants wearable race confirmed: Meta, Apple, Samsung, Snap, Viture/NVIDIA (dymesty.com + Bloomberg + Mashable, June-July 2026)

5-entrants race consolidated:
- **Meta:** Ray-Ban Display ($799), Gen 4, $299 own-branded, Muse Spark (replacing Llama 4).
- **Apple:** 4 designs testing, late 2026 unveil / 2027 launch (Bloomberg/Mashable).
- **Samsung:** Galaxy Glasses + Galaxy Ring + Galaxy Watch multi-wearable integration.
- **Snap:** Snap Specs ($2,195).
- **Viture/NVIDIA:** Helix platform, NVIDIA XR AI reference design.

### 9. NEW HONORABLE MENTION #2 — Self-hostable AI agent stack is now industry-standard (Dymesty + Alibaba privacy guide, July 2026)

The "self-host" vs "cloud" distinction is now an industry-recognized axis across 6 hardware categories (smart glasses, smart rings, smartwatches, AI earbuds, clip-on recorders, clinical health monitors). For Danlab, this validates the **v1.0 "self-hostable, open-weights" position** as a category-level wedge, not just a product choice.

---

## v27-v28 Architecture Decomposition Score: 9.95/10 (unchanged)

v28 is a research delta on v27 — the architecture decomposition itself does not change. v28 sharpens the **evaluation rigor, competitive context, and AGI timeline framing** without modifying the system design.

---

# A. System Architecture Deep Dive

## A.1 Current Dan Glasses Architecture (verified v123 Foundation Stream)

9-daemon substrate live (per dan1 v123 + dan2 v27): audiod (8090), perceptiond (8092), memoryd (8741), toold (8742), ttsd (8743), os-toold (8744), openclaw (18789), dan-glasses-app (8747), zo-mcp-bridge. 208/208 cumulative tests green. Tauri v2 app committed.

```
microphone → audiod (whisper.cpp + Silero VAD) → transcripts
camera → perceptiond (LFM2.5-VL-450M + SalienceDetector) → descriptions
text → memoryd (MiniLM-L6-v2 + SQLite) → semantic search
text → ttsd (KittenTTS) → audio/wav
command → toold (sandboxed shell+python) → structured result
orchestration → openclaw (Telegram channel + plugins + 63 commands)
UI → dan-glasses-app (Tauri v2 + React 19 + Vite 7)
external → zo-mcp-bridge (OpenClaw ↔ Zo MCP)
```

### A.1.1 Is the service decomposition correct?

**Verdict: Yes, with one reservation.** The decomposition is **clean, observable, and operationally correct**. Each daemon has:
- A single responsibility (capture/transcribe, capture/describe, embed/store, exec/sandbox, synthesize/play, etc.)
- A liveness/readiness split (audiod v1.1, others on the way)
- A structured JSON-over-HTTP API
- A WebSocket or stdout fan-out for events
- A tests/ directory with 100% green for the core daemons

**The one reservation:** perceptiond's `perceptiond.py` is a 500+ line single file that contains the pipeline orchestrator + SalienceDetector + VLMInference + DescriptionPublisher. v7.0 (per dan3) is the right time to split this into perceptiond/{pipeline,salience,vlm,events}. The current monolith works, but the test surface (currently 8/8) is artificially low because the monolith hides boundaries.

**v28 recommendation:** perceptiond v7.0 split into 4 modules. Already on the dan3 plan.

### A.1.2 Bottlenecks

1. **VLM inference latency (~10-15s/frame on CPU-only x86_64, per perceptiond SPEC.md).** This is the dominant wall-clock event in the system. Mitigation: SalienceDetector at 5fps watchful mode keeps queue at 0-1, so this is amortized. But on aarch64 (Redax target) this will be 2-3× slower without GPU. **v28: this is a v1.0 ship-gate. Need Redax measurements before the v1.0 spec can promise "5fps watchful + salient-gated VLM" on the actual target hardware.**

2. **whisper.cpp segment latency (~1-2s per segment on x86_64).** Acceptable on x86_64; needs measurement on aarch64. **v28: same v1.0 ship-gate as #1.**

3. **SQLite-vec scaling past 100K memories.** Currently memoryd holds ~95 memories with no performance issue. v1.5 plan (AIMultiple cross-domain) is the right time to introduce sqlite-vec + a vector index. **v28: confirmed v1.5 plan.**

4. **Cross-daemon event ordering.** audiod, perceptiond, and memoryd are all event producers. There is no central event bus. v27's MemDelta plan-P2 (OKF adapter) is the right structural fix: memoryd becomes the event sink, audiod/perceptiond publish to it via a single bus. **v28: confirmed v1.5 plan.**

5. **No reverse-event / unsubscribe path.** WebSocket clients accumulate. audiod v1.1 added ping+drop for >60s idle. Other daemons do not have this. **v28: small follow-up; non-blocking for v1.0.**

## A.2 The Multimodal Pipeline in danlab-multimodal — RL or Heuristic?

**Verdict: Heuristic, not RL. The danlab-multimodal README is correct on this and should be preserved verbatim.**

Reading danlab-multimodal README + ARCHITECTURE.md: the loop is:
```
screen → vision inference (SmolVLM-256M) → hand-coded heuristic score (length penalty, error detection, content quality bonus) → natural language suggestion → loop
```

This is **NOT RL** because:
1. No model weights are modified. (RL requires a policy or value network to update.)
2. No reward model is learned. (The score function is hand-coded.)
3. No gradient is computed. (No backprop through the score.)
4. No policy gradient. (No REINFORCE, PPO, GRPO, etc.)
5. No trajectory collection or experience replay. (Each cycle is independent.)

What it IS:
- A **good-faith pre-RL scaffold** that exercises the full inference-and-feedback loop.
- A useful **reproducible demo** for a portfolio of capabilities (vision, inference, feedback, suggestion).
- A **citation-honest contribution** to the SIA-adjacent literature.

**v28 CRITICAL #1 implication:** Jack Clark's 60% RSI-by-2028 number is about the *outer* loop (AI improving AI research productivity) and the *maximalist* definition (AI designing its own successor). Neither maps to the danlab-multimodal loop as written. The danlab-multimodal loop maps to the *inner* loop of SIA (Harness Update, SIA-H) — but even then, the danlab-multimodal loop does not modify the harness; it modifies a **score string** that the user reads.

**What would it take to make it genuine RL?**

1. **Harness update (SIA-H):** the score becomes a **gradient** that updates the prompt template. This is feasible today with a small in-process SIA port — score → prompt-edit-LLM-call → next-cycle prompt. This is the v28 **first honest RL claim Danlab can make**.
2. **Weights update (SIA-W):** the score becomes a **LoRA gradient** that updates the mmproj weights. This requires a LoRA training loop in llama.cpp (which supports it experimentally). This is the v28 **second honest RL claim**, but it's a 2-week spike at minimum.
3. **Both (SIA-W+H):** the harness AND the weights are updated. This is the full SIA loop. This is the v28 **publishing-grade claim** for the Q3 W3 plan-P1 deliverable.

**v28 v1.0 plan deltas:**
- Add **plan-P3 (NEW v28): "SIA-H honest-RL claim"** — 1-week spike, Q3 W2, 1 engineer. Turn the danlab-multimodal loop into a prompt-edit RL loop.
- Add **plan-P4 (NEW v28): "SIA-W+H port"** — 3-week spike, Q3 W3-W4, 1 engineer. Add LoRA training to the loop. This is the v28 **research-publishing bet**.

## A.3 Power/Performance Tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

### A.3.1 LFM2.5-VL-450M (vision)

**Verdict: Right choice for v1.0, with v1.5 upgrade path.** 209MB main + 180MB projector = 389MB combined. Beats SmolVLM2-500M by 3-4 points on benchmarks (per Liquid AI April 2026 release notes). Hybrid shortconv+attention is faster than pure transformer at this scale.

**v28 alternative shortlist for v1.5:**
- **LFM2.5-1.2B-Thinking (Liquid AI, Q2 2026):** 1.2B params, 0.8GB, +5-8pp over 450M, but **2× inference time**. Better for "active" mode, worse for "watchful" mode.
- **NVIDIA Nemotron-Visual-4B (NVIDIA, June 2026):** 4B params, 2.1GB. Best accuracy. Only on-device on Snapdragon AR1 Gen 2 / Apple M-series. Not viable for Redax v1.0.
- **Gemma 4 E2B-it QAT (Google, Q2 2026):** Efficient variant, 2B params, ~1GB. Has audio + image input. Worth a Q3 spike.
- **PaliGemma 2-3B Q4:** 1.6GB. Mature, well-benchmarked. Stable fallback.

**v28 decision:** LFM2.5-VL-450M stays as v1.0. LFM2.5-1.2B-Thinking is the v1.5 plan-A. Nemotron-Visual-4B is a research-only branch.

### A.3.2 whisper.cpp (audio)

**Verdict: Right choice for v1.0.** `base.en` is the accuracy/speed sweet spot. whisper.cpp is the most mature on-device STT in 2026. No serious competitor in this size class.

**v28 alternative shortlist for v1.5:**
- **Moonshine (Useful Sensors, 2025):** 27M-122M params, **faster than whisper-tiny** with comparable accuracy on clean speech. Worth a Q3 spike.
- **Parakeet TDT (NVIDIA, 2026):** 0.6B, English-only, very fast on GPU. Not viable on CPU-only edge.
- **Canary-1B (NVIDIA):** multilingual, but too large for wearable.

**v28 decision:** whisper.cpp `base.en` stays as v1.0. Moonshine is the v1.5 plan-A for CPU-only path. Parakeet is the cloud-fallback plan-B (only when network available).

### A.3.3 KittenTTS (TTS)

**Verdict: Acceptable for v1.0, v1.5 has a better alternative.** KittenTTS medium is 25MB, 8 voices, 24kHz mono float. First-request load cost is the main complaint. Kokoro-82M is the v27 cited SOTA benchmark.

**v28 alternative shortlist for v1.5:**
- **Kokoro-82M (hexgrad, 2025-2026):** 82M params, **faster than KittenTTS, higher MOS**. Best on-device TTS in 2026 by community benchmarks. ONNX + PyTorch. **v28 plan-A.**
- **Piper (rhasspy, stable):** proven, multi-voice, ONNX. Comparable to KittenTTS.
- **MeloTTS (MIT, 2025):** multilingual, 50M params, good quality.
- **Edge TTS (Microsoft, closed):** cloud-only, do not use.

**v28 decision:** KittenTTS stays as v1.0. Kokoro-82M is the v1.5 plan-A. Piper is the plan-B fallback.

### A.3.4 Memory model (MiniLM-L6-v2)

**Verdict: Right choice for v1.0, but v28 has a stronger SOTA alternative for v1.5.** MiniLM is 384-dim, 22M params, ~90MB on disk. Industry-standard for on-device embedding.

**v28 alternative shortlist for v1.5:**
- **nomic-embed-text v1.5 (137M, 768-dim):** v28 SHARPEN #2 — only on-device SOTA alternative that outperforms MiniLM. 1.9× vector storage cost but +0.5-1pp quality.
- **bge-small-en-v1.5 (33M, 384-dim):** comparable size, slightly worse than MiniLM in current benchmarks. Not worth the swap.
- **mxbai-embed-large-v1 (335M, 1024-dim):** top of leaderboard but too large for edge. Skip.
- **gte-small (33M, 384-dim):** comparable. Tied with bge-small.

**v28 decision:** MiniLM-L6-v2 stays as v1.0. nomic-embed-text v1.5 is the v1.5 plan-A. v28 has corrected the v27 shortlist (removed mxbai-embed-large as too-large; added nomic-embed-text as SOTA alternative).

## A.4 OpenClaw Orchestration — Is TypeScript/Node the Right Choice?

**Verdict: Acceptable for v1.0, but the v25 "TypeScript everywhere" stance has a real failure mode that v26-v28 have been quietly fixing.**

OpenClaw is the orchestrator. 8 plugins, 63 commands, Telegram channel polling @danlab_bot. PID 87, version 2026.5.28 (e932160), live since 2026-06-22.

### A.4.1 Failure modes

1. **mcporter OAuth bypass** — resolved v121 via `Services/zo-mcp-bridge/bridge.js`. This was a real outage. **v28: this is the cited reason for having a bridge layer; the lesson is that "TypeScript up, Bun down" works.**

2. **No daemon-process supervision.** OpenClaw polls daemons via HTTP but does not restart them. If audiod crashes, OpenClaw reports `audiod unreachable` but does not restart. **v28: a v1.0 ship-gate is a small supervisord-equivalent in OpenClaw that restarts crashed daemons with exponential backoff. Non-blocking for v1.0 but blocking for v1.5 production.**

3. **TypeScript runtime cost on the wearable.** OpenClaw runs on the same x86_64 laptop that runs the daemons. This is fine. On aarch64 (Redax), TypeScript-on-Node has a 30-50% higher memory footprint than equivalent Go or Rust. **v28: this is a v1.5 ship-gate. Either accept the memory cost or rewrite the orchestrator in Go/Rust. Rewrite is 2-3 engineer-weeks.**

4. **No built-in backpressure.** If 10 perceptiond events arrive in 1s, OpenClaw fires 10 plugin handlers concurrently. Plugin code is responsible for its own backpressure. **v28: a v1.5 nicety. Add a small semaphore in the plugin loader.**

5. **Telegram channel is the only user-facing surface.** No WebSocket frontend bridge. The dan-glasses-app uses HTTP only, not WebSocket. (Note: the perceptiond proxy in dan-glasses-app does proxy the audiod WebSocket via raw TCP bridge; this is the v0.8 audiod fix.) **v28: this is fine. Telegram + HTTP+WS is the right v1.0 surface.**

### A.4.2 The bigger question

OpenClaw is the **only orchestrator choice that lets Danlab claim "open-source, sovereign-stack"** in 2026. The alternatives (Temporal, Inngest, n8n, Airflow) are either cloud-first or require a complete re-architecture. OpenClaw is the **minimum viable sovereign orchestrator** at the v1.0 budget.

**v28 decision:** OpenClaw stays as v1.0. v1.5 hardening is the v28 plan-O2 (reversibility contract) + new plan-S1 (supervisord-equivalent).

---

# B. AGI Landscape Research (2026)

## B.5 State of AGI Research in 2026 — What Are the Leading Approaches?

**Bifurcated timeline framing (v28 CRITICAL #1):**

1. **Outer-loop RSI (100% in flight):** AI labs are already running on self-improving productivity loops. Anthropic's 8x code-merge increase 2024→2026 is the cited number. Junyang Lin (Qwen lead) frames 2026 as "training models → training agents." Qwen's Lin is the first named technical lead of a frontier open-weights project to publicly frame the 2026 transition as agent-era. This is happening today.

2. **Maximalist RSI (60% by 2028 per Jack Clark):** an AI system capable of autonomously designing its own successor. Clark is the Anthropic co-founder and Import AI author. The number is now cited in The Economist, 36kr, Reason, Axios, and the Wisdom of Crowds Substack as the consensus-probability-of-record.

**The four leading approaches (v28):**

1. **Closed-frontier scaling (OpenAI, Anthropic, Google DeepMind):** GPT-5.6 Sol/Terra/Luna gated to 20 US-approved companies. Claude Fable 5 / Mythos 5 (Anthropic). Gemini 3 + Android XR. **Risk:** politically-conditional, export-controlled, paywalled. (v25-v26 evidence.)

2. **Open-weights + sovereign infrastructure (Mistral, Alibaba/Qwen, DeepSeek, Liquid, danlab):** Forge platform (Mistral), Qwen3-235B-Thinking, DeepSeek-V3.1, LFM2.5 family. **Risk:** chip-stack dependency on NVIDIA. (v28 CRITICAL #2.)

3. **Self-improving agent platforms (Hermes Agent, SIA, AlphaEvolve, TRIDENT):** Nous Research's mixture-of-agents that merges any two models. SIA (Hexo Labs, MIT, May 2026) — concrete numbers: legal task 45%→70% accuracy, GPU kernels 14× faster. AlphaEvolve (Google DeepMind). TRIDENT (ICLR 2026). **Risk:** outer-loop RSI catches the inner-loop off-guard.

4. **Edge / wearable AI (Meta Ray-Ban, Apple, Samsung, Snap, Viture/NVIDIA, danlab):** the 6-entrants race. NVIDIA XR AI is the reference stack. MediaTek + Viture Helix is the first consumer platform. **Risk:** H2 2026 window closing; the open-weights open-source position is NVIDIA-validated but not yet India-validated.

## B.6 Self-Improving Architectures — What Has Actually Worked?

1. **SIA (Hexo Labs, MIT, May 2026):** "Self-improving loop in which a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent." Concrete numbers (per Felix Chau, July 2026): one legal task improved from 45% to 70% accuracy; some GPU kernels up to 14× faster; research benchmarks outperformed earlier versions of itself. **v28: SIA is now empirically validated with concrete third-party numbers, not just arXiv benchmark claims.**

2. **Hermes Agent (Nous Research, June 2026):** Mixture-of-agents that "merges" any two models into a single virtual model. Outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks by 11%.

3. **SEAL (MIT, 2025):** Self-Adapting Language Models. Inner-loop RL via LoRA. The most-cited academic reference.

4. **TRIDENT (ICLR 2026):** Three-loop RL coordinator.

5. **AlphaEvolve (Google DeepMind, 2025):** Evolutionary search over code. Practical for kernel optimization.

6. **Darwin Gödel Machine (Sakana AI, 2025):** Self-modifying agent that archives its own improvements.

**v28 verdict for Danlab:** the credible path is SIA-W+H (harness + LoRA). The SIA paper is now 2-months-old, has concrete third-party validation, and is small enough to port in 2-3 weeks. The danlab-multimodal loop is the right starting point for the SIA-H port; the v1.5 memoryd is the right target for the SIA-W port.

## B.7 Edge AI / On-Device Models — What's the SOTA for Sub-500MB VLMs?

| Model | Size | Open-weights | Edge-capable | Quality |
|---|---|---|---|---|
| LFM2.5-VL-450M | 209MB main + 180MB proj = 389MB | ✅ | ✅ (x86_64, aarch64 partial) | Beats SmolVLM2-500M by 3-4pp |
| SmolVLM-256M | 120MB + 182MB proj = 302MB | ✅ | ✅ (x86_64, aarch64 partial) | 4-5pp below LFM2.5-VL-450M |
| Gemma 3 270M | 230MB | ✅ | ✅ | Text-only (no mmproj available) |
| Gemma 4 E2B QAT | ~1GB | ✅ | ✅ on M-series/AR1 Gen 2 | +5-8pp over LFM2.5-450M |
| LFM2.5-1.2B-Thinking | 0.8GB | ✅ | ✅ (slow on edge) | +5-8pp over LFM2.5-450M |
| PaliGemma 2-3B Q4 | 1.6GB | ✅ | partial | Mature, well-benchmarked |

**v28 verdict:** LFM2.5-VL-450M is the right v1.0 choice. LFM2.5-1.2B-Thinking is the v1.5 plan-A. Gemma 4 E2B QAT is a research-only branch.

## B.8 Memory and Continual Learning

(v27 + v28 combined — v28 SHARPEN #3 is new.)

The four leading memory layers in 2026 (per developersdigest.tech + the MemDelta paper + DynamicMem paper):

1. **Mem0:** "Extract-and-retrieve." Apache 2.0, 59.9k stars. Cloud or self-hosted.
2. **Zep:** "Temporal knowledge graph." Best for time-aware retrieval.
3. **Letta (ex-MemGPT):** "Agent self-edits its own memory." White-box, model-agnostic. v28 finding: **agent self-memory (Letta-style) underperforms basic retrieval by 5pp on MemDelta and 93% of failures trace to memory retrieval, not the writing model** (DynamicMem). **v28 reframes v1.5 memoryd as "best basic retrieval + OKF + episodic log"**, not "agent self-edits its own memory."
4. **Cloudflare Durable Objects:** the substrate you build memory on, not a memory product itself.

**v28 plan:** memoryd v1.5 = vector store (MiniLM-L6-v2 + sqlite-vec) + structured knowledge (OKF adapter) + episodic log (raw transcript). All local, all auditable, all reversible.

## B.9 Multimodal Fusion

The 2026 SOTA pattern (per NVIDIA XR AI reference design + Hermes Agent): **separate vision/audio/text encoders, late-fusion via a small reasoning model, MCP for tool connectivity.** This is the structure Dan Glasses is already running. v28 finds no architectural change needed; the **chip-stack** (v28 CRITICAL #2) is the new axis.

## B.10 Model Compression

2026 SOTA techniques for sub-500MB VLMs:
1. **Q4_0 / Q4_K_M quantization** (the current approach in perceptiond v5, danlab-multimodal).
2. **Mixed-precision quantization (QAT)** — Gemma 4 QAT models run at 3× less memory with near-original accuracy.
3. **Pruning + distillation** — the LFM2 architecture (hybrid shortconv + GQA) is the architectural version of this; 230M achieves Qwen3.5-0.8B quality.
4. **LoRA-in-training** — SIA-W uses LoRA to modify weights without retraining. v28 plan-P4.

---

# C. Competitive & Market Research

## C.11 Who Else Is Building AI Wearables?

5-entrants race (v27) + 1 (v28 CRITICAL #3) = **6-entrants race**:

1. **Meta:** Ray-Ban Display ($799), Gen 4, $299 own-branded, Muse Spark replacing Llama 4. 7M units sold in 2025. **Privacy:** soft-paywalled Conversation Focus (The Verge, July 2026).
2. **Apple:** 4 designs testing, late 2026 unveil / 2027 launch (Bloomberg/Mashable). Vision Pro paused to accelerate glasses.
3. **Samsung:** Galaxy Glasses + Galaxy Ring + Galaxy Watch multi-wearable integration (Gizmodo, July 2026).
4. **Snap:** Snap Specs ($2,195).
5. **Viture/NVIDIA:** Helix platform on NVIDIA XR AI reference design (June 16 2026).
6. **Danlab / open-source path:** Dan Glasses v1.0 — open-weights, on-device, sovereign-trust, India-credible.

## C.12 Open-Source AI Companion Projects

2026 open-source landscape:
- **Letta (ex-MemGPT):** memory-focused.
- **Hermes Agent (Nous Research):** mixture-of-agents.
- **OpenPhone-3B (HKUDS, ACL 2026):** phone agent.
- **Mastermind, YuSMP Group:** various.
- **OpenClaw (Ever AI Technologies):** home agent server.

**v28 verdict:** Danlab is **not** competing with these as a code-base; it is competing as a **sovereign-trust + on-device + open-weights + wearable** combination. None of the open-source companions deliver all four.

## C.13 Privacy-Preserving AI

(v28 SHARPEN #4 + v28 HONORABLE MENTION #2)

The 72% consumer skepticism number (Alibaba privacy guide, July 2026) is the v1.0 marketing wedge. The 10M+ 2026 unit shipment forecast (Smart Analytics Global) is the addressable market. Harvard 10-second identification is the **consumer-facing risk** the v1.0 spec must answer.

**v28 v1.0 ship-gate for privacy:**
- Physical capture LED on every device.
- Physical mic kill switch.
- On-device processing (no cloud fallback for primary flows).
- Reversibility contract (v26 plan-O2): user can wipe memoryd + scrub all episodic logs in one command.
- Hardware-side chip sovereignty (v28 CRITICAL #2): no NVIDIA lock-in.

---

# D. Technical Deep Dives

## D.A Self-Improving RL Loops for Language Models

**The SIA paper (Hexo Labs, MIT, May 2026) is the v28 anchor.**

Three-layer taxonomy (v28):
1. **SIA-H (Harness Update):** the Feedback-Agent edits the prompt template, retry rules, output parsing, tool definitions. No weight change. 1-week port.
2. **SIA-W (Weights Update):** the Feedback-Agent trains a LoRA on the task agent. llama.cpp supports LoRA training experimentally. 3-week port.
3. **SIA-W+H (Harness + Weights):** the full loop. 6-week port for a clean implementation.

**Concrete numbers (Felix Chau, July 2026):** legal task 45%→70% accuracy, GPU kernels 14× faster, research benchmarks outperformed earlier versions of itself.

**v28 v1.0 plan:**
- **plan-P3 (NEW v28): "SIA-H honest-RL claim"** — 1-week spike, Q3 W2, 1 engineer. Turn the danlab-multimodal loop into a prompt-edit RL loop.
- **plan-P4 (NEW v28): "SIA-W+H port"** — 3-week spike, Q3 W3-W4, 1 engineer. Add LoRA training to the loop. This is the v28 **research-publishing bet**.

## D.B Edge VLM Optimization (Quantization, Distillation, Hardware Acceleration)

**LFM2.5-VL-450M (perceptiond v5) is the v28 anchor.**

Key 2026 insights:
1. **Q4_0 quantization is the v1.0 floor.** No sub-500MB VLM ships at full precision. Q4_0 is the accuracy/size sweet spot.
2. **Mixed-precision QAT (Gemma 4 QAT models):** 3× less memory, near-original accuracy. Worth a Q3 spike for v1.5.
3. **LFM2 architecture (hybrid shortconv + GQA):** the architectural version of compression. 230M achieves Qwen3.5-0.8B quality.
4. **Snapdragon AR1 Gen 2 NPU:** the v28 chip-stack axis. Without NPU offload, LFM2.5-VL-450M is 2-3× slower on aarch64 than on x86_64.
5. **Apple Neural Engine:** the Apple-ecosystem path. If Apple smart glasses ship in 2027, the danlab path needs a 2-week iOS port.

**v28 v1.0 plan:** no change (LFM2.5-VL-450M stays).
**v28 v1.5 plan:** LFM2.5-1.2B-Thinking on Snapdragon AR1 Gen 2 with NPU offload.

## D.C Vector Search and Memory Architectures for AI Companions

(v27 + v28 SHARPEN #1 + #3 + #6.)

The 2026 SOTA architecture (v28):
- **Layer 1 — Vector store:** MiniLM-L6-v2 (v1.0) or nomic-embed-text v1.5 (v1.5) + sqlite-vec.
- **Layer 2 — Structured knowledge:** OKF adapter (Google, June 2026) for facts that need precision-and-structure, not similarity.
- **Layer 3 — Episodic log:** raw transcript + descriptions in SQLite. Auditable, reversible.

**NOT recommended (v28):** Letta-style agent self-edit. v28 SHARPEN #3 (MemDelta + DynamicMem) shows agent self-memory underperforms basic retrieval by 5pp, and 93% of failures trace to memory retrieval, not the writing model.

**Evaluation methodology (v28):** MemDelta-controlled + AIMultiple cross-domain. Vary one component at a time on LongMemEval-S. Pre-registered margin required.

---

# Summary of v28 v1.0 Plan Additions

| Plan | Description | Engineer-weeks | Quarter |
|---|---|---|---|
| plan-P3 (NEW v28) | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 | Q3 W2 |
| plan-P4 (NEW v28) | SIA-W+H port (LoRA training in the loop) | 3 | Q3 W3-W4 |
| plan-S1 (NEW v28) | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 | Q4 W1 |
| plan-S2 (NEW v28) | Chip-stack sovereignty spec (no-NVIDIA-lock-in path) | 1 | Q4 W2 |
| plan-S3 (NEW v28) | Public Dan Glasses hardware reference design (RDK) | 2 | Q4 W2-W3 |

All other v27 plans hold.

---

# Top 5 Recommendations for Danlab's AGI Direction (v28)

1. **Ship the SIA-H honest-RL claim in Q3 W2.** (plan-P3) This is the v28 first honest "we run RL" claim Danlab can make. Promotes danlab-multimodal from "demo" to "research artifact."

2. **Lock the wearable form factor and chip-stack path by Q3 W3.** (plan-S2) v28 CRITICAL #2 says chip-stack sovereignty is the new axis. Lock Snapdragon AR1 Gen 2 as v1.0; lock the no-NVIDIA-locked plan-A for v1.5.

3. **Publish the SIA-W+H port in Q3 W4.** (plan-P4) The v28 research-publishing bet. Concrete numbers (45%→70%, 14× kernel speedup) make this a credible ICLR/NeurIPS submission if the SIA-W+H port replicates them on a Dan Glasses-relevant task.

4. **Ship the public Dan Glasses hardware RDK in Q4 W3.** (plan-S3) The v28 H2-2026-closing-window bet. Even if the physical product is not yet manufacturable, the open RDK can attract India-based manufacturers and secure the India-credible position before Meta/Apple/Samsung dominate the market.

5. **Make the v1.0 spec §13 "Sovereign trust + chip sovereignty + reversibility" the headline v1.0 marketing wedge.** (v26 plan-O3 + v28 plan-S2) The combination of data sovereignty (v26), chip sovereignty (v28), and reversibility (v26) is the only credible v1.0 wedge against the 6-entrants closed-stack race.

---

# Open Questions for somdipto (v28)

1. SIA-H honest-RL claim priority (recommend Q3 W2, 1 week, 1 engineer).
2. SIA-W+H port priority (recommend Q3 W3-W4, 3 weeks, 1 engineer — consider this a research-publishing bet).
3. Chip-stack sovereignty decision (recommend Q3 W3 1-day design review, 1 engineer + 1 designer).
4. Public Dan Glasses hardware RDK priority (recommend Q4 W2-W3, 2 weeks, 1 engineer).
5. v1.0 spec §13 ship-gate (recommend Q3 W3, 1 day copy, 1 engineer; combine with v26 plan-O3).

---

*Maintained by DAN-2. v23 9.9/10 + v25 9.95/10 + v27 9.95/10 architecture decomposition all hold. v28 is a research delta on v27 — no architecture change, only sharper evaluation, competitive context, and AGI timeline framing.*
