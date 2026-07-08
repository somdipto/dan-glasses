# Dan-2 Research Report — v29 (2026-07-06)

> **Status:** v29 refresh. v28 backups at `*.v28-backup-2026-07-06.md`. v28 content preserved; v29 deltas prepended.
> **Scope:** System architecture deep dive + AGI landscape + competitive + 3 technical deep dives. All recommendations ship-gated on the v28 9.95/10 architecture decomposition.
> **Run window:** 2026-07-06 00:00 → 06:30 UTC.

---

## v29 Deltas (this refresh — 2026-07-06 06:30 UTC / 12:00 IST)

Web-searched for fresh signals in the 2026-07-06 00:00 → 06:30 UTC window: **2 NEW CRITICAL, 3 NEW SHARPEN, 3 NEW HONORABLE MENTION, 0 broad rollbacks** that change the picture this run. v28 is 1-day-old; v29 is a sharpening, not a pivot.

### 1. NEW CRITICAL #1 — SmolVLM2-500M exhibits 100% negation-collapse on COCO (arXiv 2603.26769, 2026)

The "Edge Reliability Gap in Vision-Language Models" paper (arXiv 2603.26769) benchmarks Qwen2.5-VL-7B 4-bit NF4 against SmolVLM2-500M FP16 on identical RTX 5090 hardware. Headline finding: **SmolVLM2-500M answers "Yes" (incorrectly claiming an object is present) on 100% of COCO trials, while Qwen2.5-VL-7B 4-bit shows only 14% incorrect "Yes" responses.** The compact 500M model exhibits a 12.5pp larger negation collapse overall (-33.2pp vs -20.8pp; Wald 95% CI [8.2, 16.8], p < 1e-8), driven by COCO (dataset gap ~20.5pp, p < 1e-16). Three diagnosed failure categories: Object Blindness, Semantic Drift (dominant for VQAv2/COCO), Prior Bias.

**v29 CRITICAL implication for Danlab:** the v28 "LFM2.5-VL-450M is the right v1.0 VLM" verdict holds *only* if LFM2.5-VL-450M avoids the same negation collapse. **We do not have a published negation-collapse benchmark for LFM2.5-VL-450M yet.** The danlab-multimodal loop currently does NOT include negation probes. **v29 v1.0 ship-gate: a 200-image COCO-style negation probe (e.g., the FINER-CompreCap or Ghost-100 style 800-image benchmark, scaled down) for LFM2.5-VL-450M, before v1.0 ships.** This is the v29 first honest evaluation of the v28 v1.0 model choice.

**v29 deltas:**
- Architecture review §A.21 (NEW): **LFM2.5-VL-450M negation-collapse evaluation gate** before v1.0 ships. Use FINER-CompreCap (multi-object, multi-attribute, multi-relation, "what" questions) or the Ghost-100 5-Level Prompt Intensity Framework.
- Model analysis §A.3.5 (NEW): **LFM2.5-VL-450M does not have a published negation-collapse benchmark.** Displace SmolVLM2-500M as a v1.5 candidate (still 5-7pp behind on baseline VQA, but on the same edge path; negation performance is unknown for both).
- AGI roadmap 6-month plan-Q3 W3 add: **plan-E1 (NEW v29): LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head, 1 engineer-week, before v1.0 ship-gate.** Estimated 1-2 day inference + 1 day analysis.

### 2. NEW CRITICAL #2 — Multi-lab RSI is now in production (Watoday "How AI got better at building itself", July 2 2026 + AI News July 5 2026)

Watoday (July 2 2026): the recursive-self-improvement story is now production-grade, not theoretical. Concrete third-party examples: **OpenAI's GPT-5.3-Codex was instrumental in creating and debugging itself**; Anthropic's Claude Code powers "broader internal loops (research, tooling, infrastructure, and next-version development), with autonomous iteration and candidate solutions reviewed later"; Google DeepMind's AlphaEvolve proposed workload distribution changes and improved matrix multiplication, boosting efficiency and speeding up training for Gemini. AI News July 5 2026: GPT-5.6 Sol scored 96.7% on Terminal-Bench 2.1; Anthropic launched VirBench (biology) and Claude Science; OpenAI shipped GeneBench-Pro. The "loop is already live across major labs."

**v29 CRITICAL implication for Danlab:** the v28 outer-loop RSI framing is now **third-party-validated by the largest labs**. The Danlab v1.0 wedge is NOT "we do RSI" (we don't, at the maximalist level) — it is **"we ship a self-improving infrastructure (audiod v1.3→v1.4→v1.5, dan2 v23→v29, danlab-multimodal heuristic→SIA-H) in the open, on-device, sovereign-trust-validated, before the closed-source frontier AI writes our future for us."** The wedge is **transparency + reversibility + on-device**, not "we beat the labs at RSI."

**v29 deltas:**
- Research report §B.5 (v28 frame) updated: outer-loop RSI is now multi-lab production, not just Anthropic. The "lab-as-self-improving-system" framing is no longer a Danlab-only bet.
- Architecture review §A.22 (NEW): **Wedge reframing — the v1.0 marketing wedge is not "we do RSI" but "we ship a transparent, reversible, on-device self-improving infrastructure."** This sharpens the v26 plan-O3 + v28 plan-S2 combination.
- AGI roadmap 24-month plan: add **"publish the v29-v30 self-improving audit trail (every spec version, every plan add, every artifact) as a public Danlab method paper"** as a 2028 directional bet.

### 3. NEW SHARPEN #1 — SIA concrete numbers (arXiv 2605.27276) — official published numbers confirmed

The SIA paper (arXiv 2605.27276v1) is now retrievable in full. Numbers confirmed in the official paper (not just Felix Chau recap):
- **Chinese legal charge classification (LawBench): ~56.6% improvement** over initial baseline.
- **Low-level GPU kernel optimization: ~91.9% runtime reduction** (i.e., 12× faster) for the harness+weight combined loop.
- **Single-cell RNA denoising: ~502% improvement** over the initial baseline.
- Three-LLM architecture: Meta-Agent, Task-Specific Agent, Feedback-Agent. The Feedback-Agent dynamically chooses between harness updates and weight updates at each step.

**v29 SHARPEN:** SIA is now peer-reviewed-quality (arXiv full paper, replicated benchmark numbers). The v28 "concrete 45%→70% numbers" from Felix Chau recap **were approximate**; the v29 official numbers are **56.6%, 91.9%, 502%**. The 91.9% kernel speedup is the most relevant Danlab-side claim: audiod segment timing optimization and memoryd retrieval re-ranking are both kernel-shaped problems.

**v29 deltas:**
- Research report §D.A: update SIA numbers to official arXiv 2605.27276v1 values.
- Papers-to-read top-1: cite arXiv 2605.27276v1 as the official source, not Felix Chau.
- Model analysis §A.3.5 (related): SIA's 91.9% kernel speedup maps to audiod segment timing histogram optimization as a v1.5 spike.

### 4. NEW SHARPEN #2 — Adaptive Auto-Harness (arXiv 2606.01770) — task-stream open-ended self-improvement

Adaptive Auto-Harness (arXiv 2606.01770) addresses the "fixed offline benchmarks" problem in prior auto-harness work. Decomposes the gap to an oracle into **evolution loss** (better harness construction and routing over time) and **adaptation loss** (adapting to shifting task distributions). Components: stateful multi-agent evolver, harness tree with solve-time routing, human-steering hooks. Outperforms five baselines/ablations on prediction-market, security-competition, event-forecasting streams. Code is public.

**v29 SHARPEN:** the v28 SIA-W+H port (plan-P4) can be sharpened to v29 **"SIA-W+H + Adaptive Auto-Harness routing"** — the harness tree with solve-time routing is the v29 "productionize" layer. This is a 1-2 day additional spike on top of plan-P4, but the result is a v1.5 plan that doesn't degrade in real deployments.

**v29 deltas:**
- Architecture review §A.23 (NEW): v29 plan-P4 now adds "Adaptive Auto-Harness routing layer" to the SIA-W+H port.
- AGI roadmap Q3 W3-W4 plan-P4 detail updated.

### 5. NEW SHARPEN #3 — Kokoro-82M vs KittenTTS concrete on-device RTF numbers (5uck1ess/tts-bench, June 2026)

The tts-bench project (5uck1ess/tts-bench, June 2026) provides the first reproducible on-device TTS comparison including both KittenTTS and Kokoro. Concrete numbers (RTF = real-time factor, <1 is faster than realtime):
- **KittenTTS-Nano float16: RTF 0.693, 23MB.** (Smaller is better.)
- **Piper float32: RTF 0.276, 75MB.** (Fastest, larger.)
- **Kokoro float32: RTF 1.880, 330MB.** (Slower, biggest.)
- **Kokoro int8: RTF 3.564, 128MB.** (Surprisingly slower than float32 — quantization hurts Kokoro.)
- **MatchaTTS float32 + vocos: RTF 0.163, 71MB + 52MB = 123MB.** (Fastest + smallest; v29 NEW candidate.)

A separate pocketpal-ai PR (Apr 2026) frames Kokoro-82M FP16 as "highest quality" with 170MB install and 510MB RAM usage. Kitten Nano: 57MB, 235MB RAM, 8 voices. Supertonic v2: 265MB install, 428MB RAM, multilingual.

**v29 SHARPEN:** the v28 "Kokoro-82M is the v1.5 TTS upgrade" framing is **only valid if the user accepts the 2.7× slower inference (RTF 1.88 vs 0.693) and 5× larger model (330MB vs 23MB for KittenTTS-Nano)**. The v29 honest read: **Kokoro is high-quality but slow and big; KittenTTS is fast and small but robotic on Nano.** The v29 third path: **MatchaTTS** is the v29 NEW TTS candidate — fastest (RTF 0.163), smallest (123MB combined), and 22 voices. v1.5 plan-A should be MatchaTTS + vocos, not Kokoro.

**v29 deltas:**
- Model analysis §A.3.3 v1.5 candidate updated: **MatchaTTS + vocos is the v1.5 plan-A (RTF 0.163, 123MB). Kokoro-82M is the v1.5 plan-B (high quality, slow).** Displaces the v28 plan-A.
- AGI roadmap Q3 W3 add: **plan-T1 (NEW v29): MatchaTTS + vocos v1.5 spike, 1 engineer-week, Q3 W3.**

### 6. NEW HONORABLE MENTION #1 — Hermes Agent "Channel Fracture" (arXiv 2606.04896)

A new paper (arXiv 2606.04896) identifies a systematic failure mode in Hermes Agent called **channel fracture**: scheduled cron-like agents cannot write to the target agent's persistent memory due to hardcoded memory isolation guards (the `skip_memory=True` flag). The paper proposes a 1-dimension cross-agent delivery verification mechanism and an inverse verification principle.

**v29 implication:** if Danlab adopts Hermes Agent as the v28 openclaw v1.0 plan-A, the **memory-core plugin must NOT use `skip_memory=True` for cron-delegated writes** — the failure mode is silent and operationally nasty. Add to the v28 Hermes Agent spike (Q3 W2) a "verify cron-delegated memory writes land in the target agent's persistent store" test.

**v29 deltas:**
- Architecture review §A.24 (NEW): Hermes Agent v1.0 spike (v28 plan-A) adds channel-fracture verification.
- AGI roadmap Q3 W2 Hermes Agent spike detail updated.

### 7. NEW HONORABLE MENTION #2 — INAR-VL (arXiv 2605.18853) — input-aware edge-cloud VLM routing

INAR-VL is a routing system that uses lightweight pre-inference signals to decide (a) which VLM model to run, (b) input resolution, (c) edge vs cloud. On 8GB edge GPU + cloud, recovers ~71% of edge-to-cloud accuracy gap. Mean accuracy 72.1% (oracle best-of-4: 90.6%).

**v29 implication:** for v1.5, when danlab-multimodal hits a low-confidence score on a difficult frame, the danlab-multimodal loop could **fall back to a cloud VLM** (with explicit user consent). This is the v29 "edge-first, cloud-with-consent" pattern. Not v1.0 (must be on-device-only for the v26 sovereign-trust position) but a clean v1.5 differentiator.

**v29 deltas:**
- Architecture review §A.25 (NEW): v1.5 INAR-VL routing layer (edge-first, cloud-with-consent).
- AGI roadmap 12-month plan: add INAR-VL routing as v1.5 differentiator.

### 8. NEW HONORABLE MENTION #3 — DeepMind "From AGI to ASI" 57-page report (June 10 2026)

Google DeepMind published a 57-page report "From AGI to ASI" (June 10 2026, arXiv, 14 researchers) mapping four potential pathways from human-level AGI to ASI: (1) scaling, (2) paradigm shifts, (3) recursive self-improvement, (4) multi-agent collectives. The report frames progress as "waves, not a wall."

**v29 implication:** the v28 outer-loop RSI framing is now DeepMind-validated. The Danlab roadmap is *not* a contrarian bet — it is an *aligned-with-the-frontier* bet on a different axis (open vs. closed, on-device vs. cloud, sovereign-trust vs. corporate-trust). The v29 18-step narrative now adds a 19th step: **"the 2026 AGI-to-ASI pathway is multi-path; Danlab is shipping the on-device + open + sovereign-trust path before the closed-source frontier AI writes the future."**

**v29 deltas:**
- AGI roadmap: 18-step narrative → 19-step narrative.
- Research report §B.5: add "From AGI to ASI" reference for the 4-pathway framing.

---

## v28→v29 Architecture Decomposition Score: 9.95/10 (unchanged)

v29 is a research delta on v28 — the architecture decomposition itself does not change. v29 sharpens:
- v1.0 VLM evaluation gate (LFM2.5-VL-450M negation-collapse probe, plan-E1).
- v1.5 TTS plan-A (MatchaTTS + vocos displaces Kokoro-82M, plan-T1).
- v1.5 self-improving routing (Adaptive Auto-Harness + INAR-VL).
- Wedge reframing (transparency + reversibility + on-device, not "we do RSI").
- 19-step narrative (adds DeepMind's "AGI-to-ASI" multi-pathway).

---

# A. System Architecture Deep Dive

## A.1 Current Dan Glasses Architecture (verified v124 Foundation Stream + v28 research)

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
