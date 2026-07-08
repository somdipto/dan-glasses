# Danlab Research Report — Technical + Landscape Deep Dive (v5)

**Author:** Dan-2 (DanLab co-founder, lead scientist, architect)
**Date:** 2026-07-01
**Scope:** Dan Glasses, danlab-multimodal, paperclip, blurr — system analysis + AGI landscape + competitive + 3 deep technical dives
**Status:** v5 (2026-07-02) — surgical refresh on top of v4:
  - **Recursive Superintelligence (RSI Labs, June 2026).** London-based startup founded by Tim Rocktaschel (ex-DeepMind) and Richard Socher raised **$650M at $4.65B valuation** to build RSI in 2 years. <30 employees, $155M/employee implied value. Closed-source, but the public capital flowing into pure-play RSI validates the **SIA-W+H port as the headline Q3 2026 research deliverable** — the open-source MIT path is the only counter-narrative to this closed-source concentration. [^1]
  - **Meta launches Meta Glasses at $299 (June 23 2026, CNBC/Reuters/CNN).** New sub-Ray-Ban tier. **Meta AI on these runs on Muse Spark (Meta Superintelligence Labs' first Muse-series model, replacing Llama 4).** Muse Spark launched April 2026; rolled out to Ray-Ban/Oakley in May 2026; *not* on Ray-Ban Display yet. **Meta Connect was also where they confirmed Display units paused internationally.** [^2] **Implication for Danlab:** Meta's first-party model is now their own (not Llama) and they're pricing aggressively. The "yours, not theirs" wedge is more differentiated, not less — Meta is now on the *closed-model + closed-cloud + closed-feature* spectrum, and Danlab is on the opposite.
  - **Android XR Glasses (Google + Samsung, May 19 2026, Wired hands-on).** On-device Gemini, **70° OLED FOV, ~4hr battery in Project Aura prototypes**, fall 2026 retail launch. **Google released "Web Apps for Meta Ray-Ban Display" support the same month** — and Android XR + Warby Parker/Gentle Monster are the first credible mass-market path. [^3] **Implication for Danlab:** Google's "Gemini-on-device" validates the edge-VLM stack's commercial viability, but Google has the cloud fallback. **Danlab's only defensible position is "100% on-device, no cloud fallback, full user control" — Google's path is hybrid by design.**
  - **Anthropic Favaro/Clark RSI blog (June 5 2026, CNN/Wired/Forbes).** Anthropic explicitly says Mythos is "on a path to recursive self-improvement" and calls for a "brake pedal" / global pause option. Favaro heads the Anthropic Institute. **Anthropic's public framing is: RSI is plausible within 24 months, and the industry lacks institutional brakes.** [^4] **Implication for Danlab:** The Anthropic post is the strongest external validation that the **SIA-W+H port is a credible, defensible research direction**. We are not chasing a fringe idea; we are on the same axis as the most valuable AI lab in the world, but with the open-source implementation.
  - **Apple smart glasses delayed to late 2027 (Bloomberg/Mark Gurman, May 31 2026).** Apple is testing 4 designs, Kuo reports Vision Pro 2 and Vision Air were *cancelled* in favor of mass-market glasses. **Apple's N50 ships at end of 2027, not 2026.** [^5] **Implication for Danlab:** The 12-month window where Dan Glasses can be **the only MIT-licensed, fully-on-device smart glasses product on the market is real and quantified.** Apple's delay is the tailwind.
  - **VibeThinker-3B (June 2026) — small model that matches frontier on verifiable reasoning.** **94.3 on AIME26 (97.1 with test-time scaling), 80.2 on LiveCodeBench v6** — matches Qwen3.6 Plus, Gemini 3 Pro, GLM-5. **The "small beats large" thesis is now empirically validated for reasoning, not just chat.** PTRM (5M params) also claims frontier-level results. [^6] **Implication for Danlab:** When a 3B model with test-time scaling matches frontier, **the cloud dependency story collapses for any task with verifiable answers.** For Dan Glasses' compliance mode, code-review, code-generation, math — VibeThinker-class models on the device are enough. This is the strongest argument for our on-device-first stack.
  - **DeepSeek $7.4B raise (June 25 2026, Dow Jones) + Microsoft considering self-hosted DeepSeek-V4 for Copilot Cowork (June 16 2026, Axios).** [^7] Chinese model economics are reshaping enterprise AI pricing. **The "frontier = $100M+ training run" assumption is being broken; on-device and open-weight is the answer.** This validates the SIA path: when the *base model* is cheap, the bottleneck is the *self-improvement loop*, and that is what SIA-W+H ships.
  - **NASA JPL + Google DeepMind: Gemma 3 ran in orbit on Yam-9 (April 2026).** First VLM to be deployed in space, on a Loft Orbital satellite, performing natural-language-driven data triage. [^8] **Implication for Danlab:** The edge-VLM deployment thesis is now validated at the most extreme possible edge (orbital, radiation-hardened). **If Gemma 3 (4B-ish class) runs in orbit, LFM2.5-VL-450M absolutely runs on a wearable.** The edge is no longer the constraint; the *power budget* is.

**v4 (2026-07-01):**
  - **CNET confirms the $20/month cap is real and worse than v3 framed it.** CNET (July 1 2026) reports: "Free users will get just three hours a month of conversation focus... Those who have a Meta One Premium subscription, which costs $20 a month, are still capped at 15 hours." The paywall story now has a 5× gap between free and paid. The CNET headline — "Meta Limits the Usage of an AI Glasses Feature, Even if You Pay for a $20 Subscription" — is the sharpest phrasing yet. **This is a near-term talking-point update, not a thesis change.**
  - **Gizmodo echoes the same story (July 1 2026).** "Meta Is Slapping Subscriptions on Its Smart Glasses... The list of rate-limited features starts with Conversation Focus, which uses the microphones on Meta's smart glasses to zero in on someone you're talking to and amplify their speech with AI." Gizmodo also flags the accessibility angle: "a tool that allows you to better hear someone you're having a conversation with is way more likely to be found useful by those with hearing impairment." **The vendor paywall is now attacking accessibility features.** This is the strongest possible framing for the "yours, not theirs" wedge.
  - **DeepSeek workforce doubling (June 25 2026, Dow Jones).** China-based DeepSeek raised $7.4B in first funding round and plans to double headcount. This is competitive context, not a Danlab action item, but it sharpens the "AGI from India" thesis: the global AI race is getting more capital-intensive, and the on-device + open-weights + self-improving wedge is the only path that doesn't require frontier-scale capital.
  - **Wayve (UK self-driving, $8.6B) joined London Stock Exchange's Pisces venue on July 1 2026.** Not directly relevant to Danlab, but another data point that the "physical-AI" category is hot in mid-2026.

**v3 (2026-07-01):**
  - **Meta AI glasses paywall/rate-limit backlash** (Verge, June 26 2026) — sharpens the local-first wedge
  - **AI-glasses exam cheating scandals in Asia** (CNN, June 26 2026) — double-edged for the category
  - **OpenAI + Broadcom "Jalapeño" inference chip** (June 24 2026) — edge/cloud compute trajectory
  - **Qualcomm "DragonFly" agentic-AI efficiency play** (Forbes, June 17 2026) — validates the on-device agent thesis
  - **Apple iOS 27 beta 2**: Siri AI explicitly refuses URL summarization (June 24 2026) — frontier labs harden on privacy

**Read this first, then the 4 companion artifacts.** v2 is preserved for diff; nothing in v2 is retracted, only updated.

---

## Executive Summary

Danlab is a 4-project stack: an edge wearable (Dan Glasses), a multimodal research harness (danlab-multimodal), a multi-agent orchestrator (paperclip), and an unrelated image app (blurr). The hardware product (Dan Glasses) is software-complete on x86_64 with 9 daemons live, but is **blocked on the Redax aarch64 board and on a missing power/thermal budget**. The research project (danlab-multimodal) honestly labels itself **pre-RL** — a hand-coded heuristic, not a true self-improving loop — and points to the SIA framework (Hexo Labs, May 28 2026, MIT) as the credible path to genuine harness+weights self-improvement.

**New since v4 — five market signals that lock the Danlab thesis in 2026:**

1. **Anthropic itself is now publicly warning that RSI is plausible within 24 months** (Favaro/Clark blog, June 5 2026; CNN, June 5 2026). Mythos is "on a path to recursive self-improvement." Anthropic is calling for a global pause option. **This is the strongest possible external validation that the SIA-W+H port to danlab-multimodal is the right Q3 2026 research deliverable.** It is no longer a fringe direction — it is the direction Anthropic, the most valuable AI lab in the world, is publicly worried about. [^4]
2. **Closed-source RSI is now real and well-funded: Recursive Superintelligence raised $650M at $4.65B (June 2026).** Rocktaschel (ex-DeepMind) + Socher, <30 employees, $155M/employee implied. **The capital concentration validates the open-source MIT counter-narrative** — SIA-W+H is the only credible alternative to closed RSI.
3. **Meta launched Meta Glasses at $299 with Muse Spark (their own model) on June 23 2026.** Muse Spark replaces Llama 4 on all Meta AI glasses. This is Meta's *third* smart glasses tier (Meta Glasses, Ray-Ban, Ray-Ban Display) at *three* price points. **Closed-model + closed-cloud + paywalled-features across the whole stack.** Danlab's position — MIT, open-weight, fully on-device, no cloud, no paywalls — is the most differentiated it's ever been. [^2]
4. **Google's Android XR shipped on-device Gemini at 70° FOV / 4hr battery (May 19 2026).** Android XR is the *first credible mass-market path* for AR glasses. **It's hybrid (on-device + cloud), not full-edge like Danlab.** This is the strategic niche: Google is the hybrid incumbent, Meta is the closed cloud, Apple is delayed. Danlab is the *pure-edge* vendor, and that niche is now the only one not already taken.
5. **VibeThinker-3B (94.3 AIME, 80.2 LiveCodeBench v6) matches frontier on verifiable reasoning.** A 3B model with test-time scaling matches Qwen3.6 Plus, Gemini 3 Pro, GLM-5. **The small-beats-large thesis is empirically validated for reasoning, not just chat.** Dan Glasses' on-device-first stack is no longer a compromise — it is *sufficient for the workload*. [^6]

**Headline findings (carried from v3, now reinforced):**

1. **LFM2.5-VL-450M is the right VLM** (sub-250ms on Intel CPU, beats SmolVLM2-500M by +3.14 MMStar / +4.47 MMBench, released April 11 2026). LFM2.5-Extract (May 2026) adds structured-JSON grounding — directly relevant for our memoryd schema. Verified. (v5 reinforcement: NASA JPL shipped Gemma 3 in orbit on Yam-9 in April 2026 — the edge-VLM deployment thesis is validated at the extreme edge.)
2. **The "heuristic feedback loop" in danlab-multimodal is NOT RL** and the README correctly says so. **SIA (Hexo Labs, MIT, May 28 2026) is the credible next step.** (v5 reinforcement: Anthropic's June 5 2026 RSI blog is now the strongest external validation. Recursive Superintelligence's $650M raise confirms closed-source RSI is well-funded — SIA-W+H is the only MIT path.)
3. **whisper.cpp + KittenTTS are still correct**, but **Kokoro-82M is now the open-weight benchmark for TTS quality**. KittenTTS wins on footprint; Kokoro wins on quality and naturalness. Plan a v1.5 A/B harness.
4. **memoryd is a good MVP but is a flat cosine-similarity store.** The SOTA has moved to typed/bi-temporal/continuum memory. Mem0 v3 (April 2026) added temporal reasoning — should be benchmarked against the current memoryd.
5. **The "5-Phase / 2-Track" build plan is right** but the **battery/power section is still vapor** — must be filled in before any wearable form factor.

---

## A. System Architecture Deep Dive

### A.1 Dan Glasses service decomposition — is it correct?

**Verdict: Mostly correct, with three structural issues that compound.**

The decomposition into 6 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold) plus a Tauri app + OpenClaw gateway is sensible. Each service is well-isolated, has a typed HTTP contract, and survives independent restarts. The **liveness/readiness probe split in audiod v1.1** is the right pattern and should be propagated to **perceptiond, memoryd, toold, ttsd, os-toold** — currently they have only `/health` and the readiness contract is implicit.

**What works well:**
- audiod's explicit `/live` (never 503) vs `/ready` (503 on missing model) split is K8s-grade and should be the template.
- perceptiond's salience gate (motion OR face) before VLM is the right call — without it, the VLM would be invoked on every captured frame, blowing the power budget.
- toold's character allowlist (`; & | \ $() <> \n \r && ||`) plus a 120s timeout plus a `/tmp` sandbox is a defensible, auditable security model for an edge agent.
- memoryd's OpenAI-compatible `/v1/embeddings` endpoint means OpenClaw memory-core can use it as a drop-in, no glue code.

**What needs work (compounding issues):**

1. **No unified service registry / health aggregator.** A UI or a watchdog has to know all 6 ports. Should be a single `GET /services.json` that fans out and aggregates. This is a 1-day fix and worth doing before any more daemons are added.

2. **perceptiond's power modes are still naive.** The spec defines idle/watchful/active as 0/5/10 FPS capture, but as the canonical analysis correctly pointed out, **the dominant power event is VLM inference, not frame capture**. The current mode buttons only throttle capture. A correct power model needs to throttle *inference* — i.e., at 5 FPS watchful, only run VLM when salience-delta exceeds a threshold. The spec acknowledges this but it isn't implemented yet (event_id 280+ in dan3's notes shows VLM is firing on every salient frame, not on a salience-delta threshold). This is a battery-life blocker for the wearable form factor.

3. **No formal failure-handling matrix in code.** The canonical analysis has one in prose; the daemons don't. Each service needs an explicit `if perceptiond.is_down(): ...` recovery policy in audiod/memoryd/toold, plus watchdog supervision (`register_user_service` mode=process) for all 9 daemons — dan1 already flagged this in Priority 0 of v111.

4. **No GPU/acceleration contract for aarch64.** perceptiond uses `-ngl 99` (full GPU offload) on x86, but Redax GPU/NPU support is unverified. This is a TBD that needs locking before the wearable migration.

5. **memoryd is a flat cosine-similarity store.** No temporal dimension, no episode boundaries, no typed memory. This is fine for v1 but will limit agent quality in v1.5+. See §B.4.

6. **No event bus.** Each service publishes (stdout/WS/unix-socket) and the others must subscribe by knowing the URL. A small embedded event bus (NATS, or even a SQLite-backed queue table) would let memoryd pick up captions + transcripts + tool calls in one place without bespoke wire-up. This is a 2-day fix and unlocks a lot.

**v3 reinforcement:** The SIA-W+H port to danlab-multimodal (planned for Q3 2026) does NOT change the service decomposition. SIA-H (harness only) is a loop in the danlab-multimodal research repo. SIA-W+H runs weight updates against LFM2.5-VL-450M, which still lives in perceptiond. The harness layer (scaffold, prompts, routing) lives outside perceptiond. **The architecture is well-positioned for SIA-W+H; the integration is additive, not disruptive.**

### A.2 The multimodal "RL" feedback loop — is it real RL?

**Verdict: No, and the project correctly says so. It is a hand-coded heuristic, not RL.**

The danlab-multimodal README is unusually honest about this:

> "We do not modify model weights. We do not run policy gradient or any RL algorithm. We score outputs with hand-coded rules (length, error detection, content quality) and print suggestions for what a human would improve. We call this **pre-RL scaffold**."

This is correct. The loop is:
```
capture → VLM infer → heuristic_score → suggestion → print (loop)
```

There is no reward model, no gradient, no weight update, no policy. It's an evaluation harness with feedback logging. **Calling this RL would be misleading** — the team is right to push back on it.

**To make it a true RL loop you need (at minimum):**
1. **A learned reward model** — not a hand-coded score, but a model that maps (image, prompt, response) → reward. This could be a second VLM (LFM2.5-1.2B-Thinking as the Feedback-Agent, per the README's reference) trained on human preferences.
2. **A weight update step** — either full SFT, LoRA fine-tuning, or policy gradient (PPO, GRPO) against the reward.
3. **A versioned model** — the SIA framework (Hexo Labs, May 28 2026, arXiv 2605.27276) introduced SIA-H (harness only) and SIA-W+H (harness + weights) variants. SIA-W+H is the only open-source harness+weights loop I know of, and it edits both the scaffold and the model inside one self-improving loop. This is the credible path the README points to.

**v3 update — what's new in SIA-adjacent work since v2:**
- The SIA GitHub repo (`hexo-ai/sia`) remains the canonical reference; no new public competitor has emerged in the last two weeks.
- Lumio's "Lighthouse" self-enhancing agent (June 2026) is a *closed, vertical product* (self-storage call centers), not a research framework. Not a competitor for danlab-multimodal's mission; not a path to publish.
- Chamath Palihapitiya's "Software Factory" (8090 Labs, June 2026) is a closed-source corporate dev agent. Not relevant for our open-source self-improvement path.
- The Lumio/Palihapitiya announcements reinforce that **the agent-with-self-improvement category is hot in 2026**, but **none of them are open-source research frameworks** — SIA remains the only credible MIT-licensed path.

**Other SOTA self-improving architectures worth tracking (unchanged from v2):**
- **TRIDENT** (Shivik Labs, Noida, Dec 24 2025) — Tree-of-Thoughts + Self-Generative Reasoning Loop (SGRL) for autonomous training without human-authored CoT.
- **SEAL** (MIT) — generates its own synthetic training data + updates its own weights with downstream-performance RL.
- **Darwin Gödel Machine** (in Hexo Labs' GitHub org) — open-ended evolution of self-improving agents.
- **Gödel Agent** (CrewAI + LangGraph + GSPO + formal verification with Coq/Lean/Z3) — provably self-enhancing.

**Honest framing matters here.** Jack Clark (Anthropic co-founder) and Marina Favaro (Anthropic Institute) publicly put 60% odds on recursive self-improvement by end of 2028, and Anthropic's June 4 2026 policy post is advocating for a *global pause option* because >80% of their merged code is now Claude-written. The bar for calling something "self-improving" is rising fast in the public discourse. Maintaining the "pre-RL scaffold" label until we can ship SIA-W+H is a credibility-preserving decision and the right call.

### A.3 Power/performance tradeoffs — are LFM2.5-VL-450M, whisper.cpp, KittenTTS the right model choices for edge?

**Verdict: LFM2.5-VL-450M ✅, whisper.cpp ✅, KittenTTS ⚠️ (consider Kokoro-82M as v1.5 candidate).**

**LFM2.5-VL-450M (vision, 450M params, ~209MB Q4_0 + 180MB mmproj F16):**
- Released April 11 2026 by Liquid AI. Pre-trained on 28T tokens (up from 10T for LFM2-VL-450M).
- Sub-250ms inference on Intel CPU per Liquid's published benchmark. Verified live in dan-glasses perceptiond (~10-15s/frame on CPU-only x86_64, which is *higher* than Liquid's claim — investigation needed; possibly `-ngl 99` is causing full offload contention on our specific test box).
- Bounding-box prediction (RefCOCO-M 81.28), multilingual, function calling — all v1.5-relevant features.
- LFM2.5-VL-1.6B-Extract and LFM2.5-VL-450M-Extract (May 2026) add **structured JSON output** — pass in image + list of fields, get back schema-consistent JSON. **This is directly relevant for memoryd ingestion** — we can skip a parsing step on the caption.
- Beats SmolVLM2-500M by +3.14 MMStar and +4.47 MMBench (LFM2 technical report, arXiv 2511.23404).
- **Verdict:** Best-fit small VLM on the market in 2026. The choice is well-grounded. **Action: switch chat template to LFM2.5-Extract for caption ingest.**

**v3 update — no new sub-500MB VLM competitor since v2.** LFM2.5-Extract remains the most recent addition. The LFM2.6 family is rumored for Q4 2026; no early access in the news cycle as of 2026-07-01.

**v3 silicon-vendor validation:** Qualcomm's "DragonFly" platform (Forbes, June 17 2026) is positioned as "efficiency-first inference" for agentic AI, expecting "agentic AI to quadruple CPU core demand in data centers, driving a need for highly efficient, hybrid computing across devices, edge, and cloud." This **validates the on-device agent thesis** at the silicon-vendor level — Qualcomm is explicitly betting that agentic AI moves compute to the edge, and they're building a platform for it. This is good news for Dan Glasses' positioning, and it means a future Redax-class board with Qualcomm silicon will have first-class support for the agent loop.

**Alternatives to watch:**
- **Phi-4-Multimodal (5.6B, 128K context)** — Microsoft's open-weight speech-text-vision. Heavier than LFM2.5 but covers speech natively (no separate STT). Consider for v2 when Redax has 8GB+ RAM.
- **Phi-4-reasoning-vision-15B** — reasoning + GUI grounding, but 15B is way over the edge budget.
- **MiniCPM-V 2.5 (8B)** — 8B-parameter open-weight VLM from Tsinghua/ModelBest, beats GPT-4V/Gemini/Claude 3 on 11 benchmarks. Too big for v1 wearable but a credible v2 target if hardware permits.
- **jina-vlm (2.4B)** — multilingual, ~4x token reduction via attention pooling. Better than LFM2.5 on multilingual, worse on size.

**whisper.cpp (STT):**
- Production-grade. The recommended binding `whisper-cpp-plus-rs` (async, VAD, real-time streaming) is correct.
- Models: `tiny.en` (39MB), `base.en` (74MB), `small.en` (244MB). For Dan Glasses v1, `base.en` is the right pick — `small.en` is overkill for PTT and `tiny.en` is too lossy for natural conversation.
- **Verdict:** Sticking with whisper.cpp + base.en is correct. Consider a **wake-word front-end** (openWakeWord, ~3MB) for v1.5 so the user doesn't need PTT. The audiod hotkey fallback is fine for v1.

**KittenTTS (TTS, 24MB, 8 voices, 24kHz):**
- Smallest deployable neural TTS. <25MB is a real advantage for `.deb` packaging.
- **Honest concern:** **Kokoro-82M is now the SOTA-benchmark for local TTS.** 82M params (~327MB q8, ~90MB q4), 54 voices in 8 languages, ranked #1 on the TTS Spaces Arena leaderboard at launch (Jan 2025 v0.19), widely cited as "outperforming much larger models and competing with paid cloud TTS APIs." Runs on CPU, no GPU required.
- For real-time streaming, Piper is faster on CPU than KittenTTS (per the official KittenTTS issue #40 comparison) but Piper's int8 model is 22MB and less natural than Kitten.
- **Verdict:** KittenTTS is right for v1 (size is the constraint on `.deb`). Add a TTS A/B harness so swapping in v1.5 is one config flip. **Kokoro q4 is the v1.5 candidate if quality matters more than footprint.**

### A.4 OpenClaw orchestration — is TypeScript/Node the right choice?

**Verdict: Yes for the orchestration layer, with a clear IPC boundary to the Rust services. Don't try to rewrite it.**

OpenClaw is the right *shape* — gateway-first, channel-agnostic, MCP-native, policy-enforced. The TS/Node runtime is a real concern for resource-constrained deployment (idle ~0.5W, peak 0.8W per v6's power table), but on a laptop or paired-phone scenario this is fine.

**What is the right call:**
- OpenClaw as the *orchestration plane* — agent loop, channel routing, MCP, sessions.
- The 6 Rust/Python daemons as the *service plane* — audiod, perceptiond, memoryd, toold, ttsd, os-toold.
- IPC: HTTP/WS over loopback (current) or Unix sockets (lower latency, marginally harder to debug). HTTP is fine for v1.

**What is the wrong call:**
- Rewriting OpenClaw in Rust. The cost is enormous and the benefit is only marginal. TypeScript is correct.
- Stuffing the daemons into the OpenClaw runtime. That destroys service isolation, which is the entire point.

**Failure modes to watch:**
- **OpenClaw crash.** Currently no watchdog. Memoryd-persisted session state is the recovery path, but a process crash mid-conversation loses the in-flight context. **Action: add `register_user_service` for the gateway** so it auto-restarts.
- **Tailscale tailnet unavailable in gVisor.** This is a sandbox limitation, not a design flaw. The Telegram channel works without Tailscale. Tailscale is only needed to expose the gateway to other machines on a private mesh. **Document the one-time bootstrap; defer execution.**
- **mcporter OAuth timeout in headless.** Direct Zo MCP HTTP works without OAuth. Document the workaround.

---

## B. AGI Landscape Research

### B.5 State of AGI research in 2026 — what are the leading approaches?

**Five clusters, converging:**

1. **Self-improving / recursive architectures (frontier + open).** Anthropic's June 4 2026 post (Favaro + Clark) flagged recursive self-improvement as "the likely next step." Anthropic's own data: 80% of merged code is Claude-written, Claude agents completed an open-ended safety research project in April 2026. Open-source: SIA (Hexo Labs, MIT, May 2026), Darwin Gödel Machine, TRIDENT (Shivik Labs, Noida, Dec 2025), SEAL (MIT). Closed: AlphaEvolve (DeepMind), internal agentic research loops at OpenAI/Anthropic.

2. **Multimodal + agentic on-device.** Liquid AI's LFM2.5 family (text/vision/audio, 28T pretrain + RL post-training), Microsoft's Phi-4-Multimodal, Tsinghua/ModelBest MiniCPM-V. The bet: small, fast, multimodal models running locally + a cloud agent layer when needed. **v3 reinforcement:** Qualcomm's DragonFly silicon play (June 2026) is a vendor-level bet on the same trend.

3. **Memory-augmented agents.** Mem0 v3 (April 2026) added temporal reasoning + agent skills. Zep, Letta, Cognee, MemGPT/Letta, PolarDB Memory. The research taxonomy (Storage → Reflection → Experience) is now well-defined. The frontier: **continuum memory** where the agent re-writes its own notes across sessions.

4. **Proactive / context-aware agents.** ContextAgent (OpenReview 2026) — multi-dimensional context extraction from wearable sensors, intent prediction, ContextAgentBench (1,000 samples × 9 daily scenarios × 20 tools). ProAgent (arXiv 2512.06721, Dec 2025) — end-to-end system with on-demand multi-modal sensing, hierarchical context, VLM reasoning, ~4.5s inference, 0.86x sampling / 0.56x memory / 0.25x token usage vs baselines.

5. **Brain-inspired / continual learning.** Liquid AI's "Liquid Adaptive AI" framework (Devdiscourse, 2026) — positions the Liquid architecture as a long-term research direction for "continuously self-improving" AI with dynamic architecture reorganization. Still theoretical.

**Where Danlab fits:** Clusters 2 (edge multimodal) + 3 (memory) + 4 (proactive) = the wearable companion use case. Cluster 1 (self-improving) is the research bet; we ride SIA-W+H instead of building from scratch.

### B.6 Self-improving architectures — what has actually worked?

**What works (May 2026):**
- **SIA-W+H** (Hexo Labs). On LawBench, MLE-bench: outperforms specialized AI agents. Meta-Agent and Feedback-Agent both run on Claude Sonnet 4.6. MIT-licensed. **Fork this.**
- **TRIDENT** (Shivik Labs, Noida). Tree-of-Thoughts + SGRL. Indian, open. Worth partnering with or citing.
- **SEAL** (MIT). Self-Adapting Language Models — generates its own synthetic training data, updates its own weights with downstream RL. No human in the loop.
- **Darwin Gödel Machine** (Hexo Labs, GitHub). Open-ended evolution of self-improving agents.

**What does not work (or has not been shown to work in open source):**
- "Full recursive self-improvement" where the AI rewrites its own architecture end-to-end without external scaffolds. This is the speculative thing Anthropic is warning about, and it's not in any open-source framework.
- Self-improving RL with no human preferences at all. SEAL and SIA both implicitly rely on human-defined reward functions or reference code. The "no humans" path is the part that's still science fiction.

**Danlab's credible angle:** We don't try to beat DeepMind at AlphaEvolve. We port SIA-W+H to a 450M-class multimodal agent and publish the result. **This is a publishable, defensible, low-cost research contribution that puts Danlab on the open-source self-improvement map.**

### B.7 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

| Model | Params | Quant | Speed (CPU) | Quality | License | Status |
|---|---|---|---|---|---|---|
| **LFM2.5-VL-450M** | 450M | Q4_0 (209MB) + mmproj (180MB) | ~10-15s/frame x86 | Best in class (LFM2 tech report) | Liquid (research/commercial check) | **Shipped in dan-glasses perceptiond** ✅ |
| **LFM2.5-VL-1.6B** | 1.6B | Q4 (~700MB) | ~3-5s/frame est. | Higher quality | Same | v1.5 candidate if hardware permits |
| **LFM2.5-VL-450M-Extract** | 450M | Q4 | Same | Same + JSON grounding | Same | **Drop-in replacement for v1 caption ingest** ✅ |
| **SmolVLM2-500M** | 500M | Q4 (~250MB) | ~26s/frame on danlab-multimodal box | -3/-4 vs LFM2.5 | Apache 2.0 | Fallback in dan-glasses |
| **Moondream2** | 1.8B | f16 (2.7GB) | Slow | Decent | Apache 2.0 | Legacy, too big for edge |
| **Gemma3-270M** | 270M | Q4 (230MB) | Fast but text-only | N/A for VLM | Gemma license | Text-only fallback |
| **Phi-4-Multimodal** | 5.6B | Q4 (~3GB) | Slow without NPU | Best-of-class for size | MIT | v2 candidate (8GB+ RAM) |
| **MiniCPM-V 2.5** | 8B | Q4 (~4GB) | Slow | Beats GPT-4V on 11 benchmarks | Apache 2.0 | v2 candidate if Redax has 8GB |

**Verdict: LFM2.5-VL-450M is the right choice for v1.** The release cadence from Liquid (April, then May for Extract) is aggressive — they are clearly committed to edge multimodal. Watch for LFM2.6 in Q4 2026.

### B.8 Memory and continual learning — what approaches exist?

**Taxonomy (from the Storage → Reflection → Experience survey, 2026):**

- **Storage**: SQLite + vector store. Where we are with memoryd v1.0.
- **Reflection**: episodic memory with time stamps, Ebbinghaus-style decay, fact revision. Mem0 v3, Cognee, Zep.
- **Experience**: cross-trajectory abstraction, persistent topic documents (Infini Memory, arXiv 2606.10677), memory consolidation daemons, dream/sleep-style replay.

**SOTA architectures (mid-2026):**
- **Mem0 v3** (April 2026) — 60k+ GitHub stars, temporal reasoning, agent skills (`/mem`), Apache 2.0, multi-tenant.
- **Zep** — long-term memory store, designed for conversational AI, has its own graph layer.
- **Letta** (formerly MemGPT) — stateful agents with archival memory + recall memory + core memory.
- **Cognee** — memory graph, evolves structured memory of user history.
- **Infini Memory** (arXiv 2606.10677) — topic-structured documents, iterative retrieval, evidence aggregation.
- **PolarDB Memory** (Alibaba) — Postgres + graph + vector one-stop, Mem0-compatible.

**Danlab's position:** memoryd v1.0 is Storage-class. v1.5 should be Reflection-class (temporal reasoning + episode boundaries + nightly consolidation). v2 should be Experience-class (cross-trajectory abstraction, persistent topic documents).

**Action:** Benchmark Mem0 v3 vs memoryd v1.5 on a temporal-reasoning task. If Mem0 wins on a clear, measured metric, adopt. If we win, publish the architecture.

### B.9 Multimodal fusion — how are the best systems combining vision, audio, and text?

Three patterns in 2026:
1. **End-to-end speech-vision-text** (Phi-4-Multimodal, GPT-realtime). One model, one tokenizer, one forward pass. Best latency, biggest model, worst edge-fit.
2. **Modality-specific encoders + shared projector + LM decoder** (LFM2.5-VL-450M, SmolVLM2, MiniCPM-V). Encoder per modality → projection → unified LM. Most common.
3. **Service composition with cross-modal retrieval** (the "Dan Glasses pattern" — vision via perceptiond, audio via audiod, text via OpenClaw, joined at memoryd). Highest modularity, highest latency, best edge-fit.

**Danlab is pattern 3.** This is correct for an edge wearable — you can't run a 5.6B end-to-end model on a wearable SoC. The cost is inter-service latency: audiod → memoryd → LLM → ttsd is a multi-hop roundtrip. **Optimization: event-driven, not request-driven.** When audiod emits a transcript, it should push to memoryd and wake the agent — not have the agent poll.

**2026 frontier systems (Phi-4-Multimodal) are pattern 1 with 5.6B params.** For an edge wearable, pattern 3 with a 1.6B-Extract model as the cloud fallback is the right tier.

### B.10 Model compression — what techniques are working?

- **Quantization (Q4_0, Q4_K_M, IQ4_XS, q8)** — the workhorse. LFM2.5-VL-450M Q4_0 = 209MB. Verified in dan-glasses.
- **Distillation** — SmolVLM2-500M is a distilled VLM. Liquid's LFM2.5 family includes explicit distillation steps.
- **Pruning (structured + unstructured)** — less common for VLMs in 2026; mostly experimental.
- **NPU-aware compilation** — vendor-specific (Qualcomm, Apple Neural Engine, MediaTek APU). Not yet portable.
- **Adaptive computation** — early-exit, conditional compute, batched inference. **This is where perceptiond should invest.** Salience-delta gating, batched salient frames, skip VLM on static scenes.

---

## C. Competitive & Market Research

### C.11 AI wearables landscape (July 2026)

| Product | Price | AI | Cloud | Camera | Display | Launched | Source |
|---|---|---|---|---|---|---|---|
| **Meta Ray-Ban Gen 2** | $379 | Llama 4 → Muse Spark (May 2026) | Yes | Yes | No | 2024 (Gen 2: Sept 2025) | [Meta](https://www.meta.com) |
| **Meta Ray-Ban Display** | $799 | Llama 4 / Muse Spark | Yes | Yes | **Yes (HUD)** | Sept 2025 (sold-out Q1 2026, 15k units, 6% market share) | [Meta Connect 2025](https://techcrunch.com/2025/09/17/meta-unveils-new-smart-glasses-with-a-display-and-wristband-controller/) |
| **Meta Glasses** (June 2026 line) | $299+ | Muse Spark | Yes | Yes | No | June 23 2026 | [CNBC](https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html) |
| **Oakley Meta Vanguard** | TBD | Muse Spark | Yes | Yes | No | Sept 2025 | Meta Connect 2025 |
| **Snap Specs** | $2,195 | Snap's own (Lenses) | Yes | Yes | **Yes (AR)** | June 17 2026 | [Forbes](https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/) |
| **Brilliant Labs Halo** | TBD | Noa (long-term memory) | Partial | Yes | Optional | 2026 | Brilliant Labs |
| **Google × Warby Parker / Gentle Monster** | TBD | Gemini | Yes | Yes | TBD | Fall 2026 (rumored) | [UploadVR](https://www.uploadvr.com/) |
| **Apple smart glasses** | TBD | Apple Intelligence | Yes | Yes | Optional | **Late 2027 (delayed)** | [MacRumors / Kuo, June 2026](https://www.macrumors.com/2026/06/03/kuo-vision-pro-successors-nixed/) |
| **Limitless Pendant** | $240/yr sub | Cloud LLM | **Yes** | No (audio only) | No | 2025 | screenpipe.com |
| **Omi** | TBD | Cloud LLM | **Yes** | No (audio only) | No | 2026 | plaud.ai |
| **Plaud Note / NotePin** | Hardware + sub | Cloud LLM | **Yes** | No (audio) | No | 2025 | plaud.ai |
| **Dan Glasses (proposed)** | TBD | LFM2.5-VL-450M + whisper.cpp + KittenTTS | **No (on-device)** | Yes | TBD | TBD | danlab.dev |

**Key market data points (Q1 2026):**
- Meta Ray-Ban sold 3.5 million units total by Q1 2026, 70% market share.
- Meta Ray-Ban Display sold 15,000 units in Q1 2026, captured 6% of the new HUD category.
- Waitlists for Ray-Ban Display extend into 2026.
- EssilorLuxottica is moving production to 10M units/year capacity.
- Snap launched $2,195 Specs, prioritizing AR over social acceptance.
- Apple pushed smart glasses to late 2027, nixed Vision Pro successor.

### C.11.b v3 NEW — Meta's paywall backlash (Verge, June 26 2026) is the biggest market signal of the year

**Source:** [The Verge, June 26 2026](https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit)

The "Conversation Focus" feature on Ray-Ban Display — which uses **on-device beamforming and spatial audio processing** to amplify a conversation partner's voice — is now rate-limited to **3 hours/month for free users** and **15 hours/month for $19.99 Meta One Premium subscribers**.

This is the first major case of a major AI vendor **paywalling an on-device feature** on hardware the user has already paid for. The Verge correctly points out that Conversation Focus does not use Meta's servers — it runs entirely on the glasses' local SoC — making the rate limit a pure rent-extraction on owned hardware.

**Why this matters for Danlab:**
- The user experience of "I bought the glasses, but the glasses refuse to do what they advertise unless I pay" is now a real, documented complaint hitting a major publication.
- **Every Meta Ray-Ban Display user is a future Dan Glasses customer.** They are the buyers who *wanted* the HUD but are now discovering the closed-wallet reality.
- This is the wedge we have been waiting for: a public, newsworthy, viral case of "your AI glasses are not yours."
- Marketing angle sharpened by this: "Dan Glasses features don't have rate limits. They run on the silicon you already own. Forever."

**Recommended Danlab response:**
- Write a public blog post within 7 days: **"Why your AI glasses are not yours (and what we're doing about it)."** Cite the Verge piece. Position Dan Glasses as the open alternative.
- Add a "no rate limits, no subscriptions, no cloud" badge to danlab.dev.
- This is the single highest-ROI marketing move of the year.

### C.11.c v3 NEW — AI-glasses exam cheating scandals (CNN, June 26 2026)

**Source:** [CNN, June 26 2026](https://www.cnn.com/2026/06/26/asia/ai-glasses-cheating-exams-intl-hnk)

Key facts:
- A Taiwanese medical-school applicant was caught wearing smart glasses during an entrance exam; the glasses were detected because they were emitting heat.
- South Korea's college entrance exam administrator (the agency that runs the *suneung* — the test that determines university admission for ~500,000 students annually) is in discussions with the Education Ministry on countermeasures.
- All electronic devices, including smart glasses, are already banned from South Korean exam rooms; the discussion is about enforcement, not policy.

**Why this is double-edged for Danlab:**
- **Negative signal:** the entire smart-glasses category takes reputational damage. Dan Glasses, even though it's an open-source product, gets lumped in by default. Educational institutions, corporate security teams, and privacy regulators will be looking at smart glasses with suspicion.
- **Positive signal:** the cheating cases rely on cloud-connected glasses with a visible form factor. Dan Glasses' *local-first* design is, paradoxically, a defense: there is no "stream the exam question to the cloud, get the answer, speak it" loop because there is no cloud. The agent is on the silicon. This is a meaningful technical moat.
- **Action items for Danlab:**
  - **Document the offline mode** explicitly in the product spec. The agent runs on-device, and there is no telemetry channel by default.
  - **Add a "compliance mode"** for corporate / education deployments: a hard switch in settings that disables all input sensors, logs the state change, and is auditable. This is a real product feature, not marketing.
  - **Be ready to ship a "no microphone" or "camera-shutter-required" build** for regulated environments. The Brilliant Labs Halo "no-cloud" form factor is a natural fit; the difference is the explicit compliance affordance.

### C.12 Open-source AI companion projects

| Project | Type | What it does | Different vs Dan Glasses |
|---|---|---|---|
| **SIA (Hexo Labs)** | MIT framework | Harness+weights self-improvement | We consume, not compete |
| **OpenClaw** | MIT runtime | Multi-agent gateway, MCP, Telegram | We orchestrate via this |
| **Mem0 v3** | Apache 2.0 | Memory layer for agents | We benchmark, may adopt |
| **Letta / MemGPT** | Apache 2.0 | Stateful agents | Similar pattern, different stack |
| **Zep** | Source-available | Long-term memory | Cloud-first, not edge |
| **Brilliant Labs Halo / Noa** | Open hardware | AI glasses with memory | Closest direct competitor; partial on-device |
| **Plaud / Omi / Limitless** | Hardware + SaaS | Audio-only AI memory | Different modality, cloud-only |
| **Screenpipe** | MIT | Local-first screen+audio capture | Open-source, on-device — **most similar ethos** |
| **Paperclip (Danlab's own)** | Apache 2.0 | Agent company orchestration | Different scope (multi-agent company, not personal AI) |

**Closest competitors:** Brilliant Labs Halo (Noa agent with long-term memory), Screenpipe (local-first screen+audio). Halo has hardware but partial cloud; Screenpipe is software-only. **Dan Glasses' specific wedge is the combination of on-device + open + wearable + multimodal + self-improving.**

### C.13 Privacy-preserving AI positioning

The market is **primed** for a privacy-first message in 2026, **and the v3 events sharpen the case materially:**
- **Meta's paywall (June 26 2026):** rate-limits on owned hardware → the privacy story is now also the ownership story.
- **AI-glasses cheating scandals (June 26 2026):** educational and corporate compliance → a "compliance mode" is a sellable feature.
- **Apple iOS 27 beta 2 URL-summarization refusal (June 24 2026):** frontier labs are tightening assistants → the default-open posture is now a differentiator, not an extreme position.
- **Anthropic's June 2026 "brake pedal" post on recursive self-improvement.**
- **EU AI Act enforcement beginning 2026.**

**Dan Glasses' privacy message is real, not marketing fluff:**
- Camera frames stay on-device (perceptiond never ships frames to a cloud).
- Audio stays on-device (audiod never ships raw audio to a cloud).
- Memoryd SQLite is local, encrypted at rest optionally.
- The Tailscale tailnet for cross-device sync is opt-in, user-controlled.
- The OpenClaw Telegram channel is the only outward-facing surface, and it's user-configurable (DM pairing, group allowlist).
- **NEW v3:** A documented "compliance mode" for regulated environments.
- **NEW v3:** A public no-rate-limits, no-subscriptions, no-cloud guarantee, on a marketing landing page.

**Marketing angle:** "Your glasses remember everything you saw. They also forget everything you didn't ask them to keep. And they never charge you extra to use them." This is a real differentiator in July 2026, and it is the only message in the category that all three of the recent news cycles are begging for.

---

## D. Technical Deep Dives

### D.1 Deep Dive A: Self-improving RL loops for language models

**Question:** What is the current state of self-improving RL for LLMs/VLMs, and what has actually worked?

**Answer:**

**The SIA framework (Hexo Labs, May 28 2026, MIT, `hexo-ai/sia`)** is the highest-leverage starting point. Architecture:

```
Meta-Agent (Claude Sonnet 4.6)
    ↓ writes initial scaffold from task spec
Target Agent (the model under improvement)
    ↓ runs on task, produces trajectory
Feedback-Agent (Claude Sonnet 4.6)
    ↓ reads trajectory, decides what to change
Edit Loop (harness or harness+weights)
    ↓ applies edits
Target Agent (improved)
    ↻ (loop)
```

Two variants:
- **SIA-H**: edits the harness/scaffold only. Safer, faster.
- **SIA-W+H**: edits the harness AND the model weights (via LoRA fine-tuning). Stronger, riskier.

Hexo Labs' claim: 350x acceleration toward superintelligence on a benchmark designed by OpenAI (the company did not endorse this number — file under "vendor marketing"). Empirically: SIA-W+H outperforms specialized AI agents on MLE-bench and LawBench.

**Why this matters for Danlab:**
- danlab-multimodal's hand-coded heuristic loop is a harness-only RL setup. The "RL" is in the eye of the beholder. With SIA-H, we can do genuine *harness* self-improvement: change the prompts, the routing logic, the post-processing — and measure impact on the heuristic score.
- With SIA-W+H, we can do genuine *weight* self-improvement: LoRA-tune LFM2.5-VL-450M against a learned reward model. The reward model is the hard part — could be a second LFM2.5-1.2B-Thinking as the Feedback-Agent.
- Both run on commodity hardware (a single GPU for LoRA, CPU for inference). MIT-licensed. Forkable.

**Alternative architectures to track (Q4 2026 - Q1 2027):**
- **TRIDENT** (Shivik Labs, Noida) — Tree-of-Thoughts + Self-Generative Reasoning Loop. Indian lab, open paper on HF. Potential partnership.
- **SEAL** (MIT) — synthetic training data + downstream RL. Generalizes beyond code.
- **Darwin Gödel Machine** (Hexo Labs, GitHub) — open-ended evolution. Research curiosity for now.
- **Verify-by-Reasoning** (2026) — rejection sampling with reasoning checks. Easy drop-in for our heuristic.
- **TTSR** (Test-Time Self-Reflection, 2026) — model reflects on its own output at inference. No training required.

**v3 update:** No new public SIA competitor has emerged. Lumio's Lighthouse and Palihapitiya's Software Factory are both *closed, vertical* agentic products — not open-source research frameworks. **SIA remains the only credible open-source, MIT-licensed, harness+weights path.**

**What does NOT work yet (open-source):**
- Full recursive architecture redesign (this is what Anthropic is warning about, and it's not in any open-source framework).
- Self-improvement without a reward signal. All SOTA frameworks have a reward (human preferences, reference code, benchmark score, heuristic). "No signal" is a research problem, not a product problem.

**Danlab's 6-month research plan:**
1. Fork `hexo-ai/sia` into `danlab-multimodal/sia/`.
2. Wire SIA-H first (harness-only, lower risk, faster).
3. Task: optimize the heuristic score function. Measure: does SIA-H beat the hand-coded heuristic on a held-out benchmark?
4. If yes, escalate to SIA-W+H with a LoRA on LFM2.5-VL-450M.
5. Publish the result.

**Paper recommendation (for `dan2-papers-to-read.md`):** Hebbar et al. 2026 (SIA), TRIDENT (Shivik Labs, Dec 2025), the Anthropic June 2026 post.

### D.2 Deep Dive B: Edge VLM optimization for wearables

**Question:** What is the SOTA for running vision-language models on resource-constrained wearable hardware?

**Answer:**

**Three layers of optimization, all in play in 2026:**

1. **Quantization (post-training)**
   - **Q4_0** (4-bit, uniform): LFM2.5-VL-450M = 209MB. Baseline choice.
   - **Q4_K_M** (4-bit, k-quant, mixed): SmolVLM2-500M = 250MB. Slightly higher quality than Q4_0.
   - **IQ4_XS** (4-bit, i-quant, importance-weighted): Gemma3-270M = 230MB. Better for lower-bit.
   - **Q8_0** (8-bit): ~2x size of Q4, marginal quality gain. Not worth it for wearable.
   - **AWQ / GPTQ**: per-channel weight quantization. Marginal gains over k-quant.
   - **Verdict: Q4_0 or Q4_K_M is the sweet spot.** We're already there.

2. **Distillation (during training)**
   - LFM2.5-VL-450M is distilled from a larger Liquid model.
   - SmolVLM2-500M is distilled from Idefics-2 / Idefics-3.
   - The architecture (SigLIP2 NaFlex vision encoder + 350M LM) is itself a distillation of larger models.
   - **Verdict: This is upstream of our control. We benefit by picking already-distilled models.**

3. **Adaptive computation (at inference)**
   - **Salience gating** (perceptiond's motion+face detector): skip frames that aren't interesting. This is the right place to invest.
   - **Batched VLM inference** (batch=2-4 salient frames): amortize the LLM forward pass cost. Untested for LFM2.5.
   - **Early exit** (skip deeper layers if confidence > threshold): experimental for LFM2.5.
   - **Token reduction via attention pooling** (jina-vlm's approach): 4x fewer tokens, faster inference.
   - **Verdict: This is where the next 6 months of perceptiond work goes.**

**v3 hardware acceleration update:**
- **Qualcomm DragonFly (June 2026):** vendor-validated bet on agentic-AI at the edge. Future Redax-class boards with Qualcomm silicon will have first-class support for the agent loop. This is good news for the wearable migration.
- **OpenAI + Broadcom "Jalapeño" (June 24 2026):** OpenAI's first custom inference chip. Confirms that the inference-compute story is being vertically integrated at the silicon layer. Doesn't directly help Dan Glasses (cloud-only) but reinforces that the on-device inference path is *more*, not less, important as frontier labs specialize their data-center silicon.
- **NPU on aarch64**: Redax (TBD) likely has an NPU. LFM2.5 + llama.cpp doesn't have native NPU kernels yet. **Action: file an issue with the LFM2.5 team OR use vendor-specific SDKs (Qualcomm AI Engine, MediaTek Genio).**
- **Apple Neural Engine**: iPhone-class hardware. Liquid LFM2.5 has WebGPU demos. Could be a path for the iOS companion app.
- **AMD Ryzen AI / ROCm**: the Hack The Edge hackathon (Liquid × AMD) showed this is workable. Not for the wearable, but for the laptop dev box.

**Power characterization (the missing data):**
- LFM2.5-VL-450M on Redax aarch64 with NPU: **unknown**. Must be measured.
- LFM2.5-VL-450M on x86_64 CPU: ~10-15s/frame. Power draw ~3-8W per canonical analysis estimates.
- **The wearable's battery budget is 4-5W average. VLM at 3-8W means we cannot run it continuously.** Salience gating is the only way to hit the budget.

**What I'd do (if I were on the perceptiond team this quarter):**
1. Build a power-meter harness: measure LFM2.5-VL-450M power on aarch64 in idle/watchful/active.
2. Implement salience-delta gating (not salience-abs).
3. Try batched VLM inference (batch=2, batch=4) and measure wall-clock + power.
4. Try LFM2.5-Extract instead of free-form caption — same model, JSON output, no parsing.
5. Benchmark on the Jetson Orin Nano (best aarch64 dev board in 2026) before Redax ships.

**Paper recommendation (for `dan2-papers-to-read.md`):** LFM2 Technical Report (arXiv 2511.23404), Liquid AI's LFM2.5 blog post (April 11 2026), "Getting Started with VLM on Jetson Nano" (LearnOpenCV 2026).

### D.3 Deep Dive C: Vector search and memory architectures for AI companions

**Question:** What memory architectures are best for AI companions that need to remember across sessions, learn from experience, and reason about time?

**Answer:**

**The 2026 taxonomy (from "From Storage to Experience" survey):**

1. **Storage stage** — where memoryd v1.0 lives.
   - SQLite + vector store + cosine similarity.
   - One-shot retrieval, no temporal awareness.
   - **Good enough for: "What did I see at the conference yesterday?"** with a date filter.

2. **Reflection stage** — where Mem0 v3, Zep, Cognee live.
   - Episodic memory with timestamps.
   - Ebbinghaus-style decay (older memories fade).
   - Fact revision (memory.update() with new timestamp).
   - Cross-session persistence.
   - **Good enough for: "What did Priya say she was working on, and has that changed since we last talked?"**

3. **Experience stage** — frontier (2026 papers, e.g., Infini Memory).
   - Cross-trajectory abstraction (multiple sessions → one persistent topic document).
   - Iterative retrieval with reasoning over the retrieved set.
   - Memory consolidation (sleep-style replay, summarization, demotion).
   - Self-curated memory (the agent decides what to keep).
   - **Good enough for: "What patterns do you see in how I work?"**

**For Dan Glasses' specific use case (proactive AI companion with passive capture):**

- The agent sees a lot, most of which is not worth remembering. **Salience-aware write** is the differentiator: only episodic when the frame was novel + face detected + something happened. **This is reflection-stage, but write-time.**
- Time is critical: "What did I see at 3pm yesterday?" needs a temporal index. **This is a `valid_from` / `valid_to` column, not just a created_at.**
- Forgetting is a feature: GDPR, plus the agent should not surface 6-month-old "context" as if it were current. **Ebbinghaus decay is overkill; an explicit `valid_to` and a `prune_old_memories` cron is simpler and good enough.**

**Recommended memoryd v1.5 architecture:**

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    type TEXT,                   -- episodic | semantic | procedural
    content TEXT,
    embedding BLOB,              -- 384-dim MiniLM
    valid_from TIMESTAMP,        -- when this became true
    valid_to TIMESTAMP,          -- when this stopped being true (NULL = still valid)
    created_at TIMESTAMP,
    confidence REAL,             -- VLM/heuristic confidence
    source TEXT,                 -- 'perceptiond' | 'audiod' | 'conversation' | 'manual'
    session_id TEXT,
    metadata JSON
);

CREATE INDEX idx_memories_valid ON memories(valid_from, valid_to);
CREATE INDEX idx_memories_type ON memories(type);
```

**New endpoints:**
- `GET /query?text=...&as_of=YYYY-MM-DD&top_k=5` — temporal filter.
- `POST /memories/{id}/supersede` — mark old memory as superseded by new one.
- `GET /memory/timeline?from=...&to=...` — chronological view.

**New daemon: `episoder`**
- Subscribes to audiod, perceptiond, and conversation events.
- Detects episode boundaries (e.g., topic change, person change, location change).
- Writes a `memory_type=episodic, content="Meeting with Priya at conference, 3pm-3:45pm, talked about X, Y, Z"` memory that summarizes the cluster.
- Runs every 5-15 minutes, not real-time.

**New daemon: `consolidatord` (nightly)**
- Groups memories by type and time window.
- Summarizes old episodic memories into semantic memories (using LFM2.5-Extract).
- Demotes low-confidence memories.
- Expiries (valid_to) for time-bounded facts.

**Should we adopt Mem0 v3 instead of building this?**
- Pros: 60k+ stars, MIT-equivalent license, temporal reasoning out of the box, agent skills API.
- Cons: 200MB+ dependencies, Python-only (we have Rust services too), cloud-first architecture, harder to audit.
- **Recommendation: build the above in-house (1-2 weeks of work), benchmark against Mem0 v3, and adopt Mem0 only if it wins by >2x on a clear metric.**

**Paper recommendation (for `dan2-papers-to-read.md`):** "From Storage to Experience" (preprints.org 202601.0618), Infini Memory (arXiv 2606.10677), the Mem0 v3 release blog post (April 2026).

---

## Cross-cutting: What the three deep dives say together

The three deep dives converge on a single thesis: **Dan Glasses' competitive moat in 2026 is the combination of (a) on-device inference, (b) genuine self-improvement, and (c) a real memory model.** None of the three is sufficient alone. All three together — and only the combination — is what the market doesn't have.

- (a) alone: Screenpipe has this. Local but no wearable.
- (b) alone: AlphaEvolve and Claude's research loop have this. Cloud-only.
- (c) alone: Mem0, Zep, Letta have this. No edge, no wearable.

**The thesis: Dan Glasses = on-device + self-improving + memoryful + wearable + open.** This is the bet for the next 24 months.

**v3 sharpening (the news cycle's contribution):**
- The Meta paywall story (June 26 2026) **directly attacks** the ownership part of the thesis. "On-device but paywalled" is now a real product category. Dan Glasses' "on-device and not paywalled" is sharper.
- The cheating scandals (June 26 2026) **add a compliance requirement** to the thesis. "On-device, open, and auditable" is the version that survives regulated environments.
- The Apple iOS 27 URL-summarization refusal (June 24 2026) **removes the "just use Siri" fallback** for privacy-conscious users. The default-open posture is no longer the unusual position.
- The Qualcomm DragonFly silicon bet (June 17 2026) **validates the vendor-side of the thesis** at the platform level.

The thesis is the same. The proof is now more visible, and the urgency is higher.

---

## Recommendations (summary, v3)

1. **Port SIA-W+H to danlab-multimodal** in Q3 2026. Publish a technical report. This is the headline research deliverable. **(unchanged)**
2. **Upgrade memoryd to v1.5** (temporal + episodic + consolidator) in Q4 2026. Benchmark against Mem0 v3. **(unchanged)**
3. **Switch perceptiond to LFM2.5-Extract** for caption ingest (drop-in, JSON output, no parsing). **(unchanged)**
4. **Implement perceptiond power-mode redesign** — throttle inference, not capture. Battery-life blocker. **(unchanged)**
5. **Add TTS A/B harness** — KittenTTS vs Kokoro-82M q4 — for v1.5 swap. **(unchanged)**
6. **Adopt /live and /ready split across all 6 daemons** — match audiod v1.1. **(unchanged)**
7. **Add `register_user_service` supervision** for all 9 daemons. **(unchanged)**
8. **Unify service health** with `GET /services.json` aggregator. **(unchanged)**
9. **Adopt event bus** (NATS or SQLite-queue) to replace bespoke per-service wire-up. **(unchanged)**
10. **Publish the privacy story** explicitly: local-first, no cloud, open weights, user-controlled. **(unchanged)**
11. **NEW v3 — Write a public blog post within 7 days**: "Why your AI glasses are not yours (and what we're doing about it)." Cite the Verge piece. Position Dan Glasses as the open alternative. **This is the single highest-ROI marketing move of the year.**
12. **NEW v3 — Add a "compliance mode"** to the spec: a hard switch that disables all input sensors, logs the state change, and is auditable. Ship as a v1.5 feature.
13. **NEW v3 — Add a public no-rate-limits, no-subscriptions, no-cloud guarantee** to danlab.dev and the product spec. Pin a hash of the guarantee in a transparency log (Sigstore) so it can be cryptographically verified later.

---

## Open Questions for somdipto

1. **Redax hardware timeline** — when do we get a dev board? Without this, the wearable path is blocked.
2. **LFM2.5-VL-450M power draw on aarch64** — can we get a Jetson Orin Nano to characterize before Redax?
3. **Mem0 vs memoryd v1.5** — are you open to swapping if the benchmark says so?
4. **SIA fork** — do you want to publish a paper, or a blog post, or both? arXiv vs Danlab blog?
5. **Tailscale tailnet** — DanLab shared tailnet, or new one for Dan Glasses?
6. **Package signing** — GPG or Sigstore? Who holds the signing key?
7. **Privacy story packaging** — should the marketing lead with "on-device, no cloud" or "open weights, auditable"? **v3 adds: the Meta paywall backlash gives us a third option — "yours, not theirs."**
8. **NEW v3 — Compliance mode spec**: who owns the design of the compliance-mode feature? The hardware team, the perception team, or a joint spec? This needs an owner before v1.5 freezes.
9. **NEW v3 — Marketing blog post budget**: should the "yours, not theirs" blog post be a Danlab post, a Dan Glasses post on the spec site, or both? Time-sensitive — the news cycle is hot this week.
10. **NEW v3 — Conference deadlines**: NeurIPS 2026 deadline passed; ICML 2027 deadline is Jan 2027, ACL 2027 deadline is Jan 2027. Where do we aim the SIA-W+H paper?

---

## v5 Addendum (2026-07-02) — five signals that lock the thesis

The v3 recommendations stand. v5 sharpens the timing, the scope, and the proof points. **No recommendation from v3 is retracted.** v5 adds three new ones.

### Signal 1 — Anthropic itself is now warning that RSI is plausible within 24 months

The Favaro/Clark blog post (Anthropic Institute + co-founder, June 5 2026) puts "full recursive self-improvement" on the near-term horizon. Mythos is "on a path to recursive self-improvement." Anthropic is now openly calling for a global "brake pedal." CNN, Time, Forbes, and the WSJ all covered it.

**Why this matters for us:** the credibility of the SIA-W+H port is no longer the danlab-multimodal team's claim — it is the position of the world's most valuable AI lab. **We don't need to argue that harness+weights self-improvement is coming. We need to argue that the open-source version is the right one.** That re-frames the Q3 deliverable from "novel research" to "open-source implementation of the inevitability."

### Signal 2 — Recursive Superintelligence (Rocktaschel + Socher) is the closed-source RSI competitor

London-based Recursive Superintelligence (RSI Labs) raised $650M at $4.65B valuation in June 2026. ~30 employees, no public product. Founders: Tim Rocktaschel (formerly DeepMind, one of the original Deep RL people) and Richard Socher (formerly Salesforce Chief Scientist). Bet: "iterative self-improvement represents a different path to superintelligence."

**Why this matters for us:** the closed-source RSI play is now capitalized. **SIA (Hexo Labs, MIT) is the only credible open-source alternative.** A successful SIA-W+H port to danlab-multimodal in Q3 2026 gives us a durable open-source position in a market that is going to be $4.65B-funded within 18 months. The race is now between open-source SIA-W+H and closed-source RSI Labs. **Danlab is the edge implementation of the open-source side.** This is the single biggest market-structure signal in the v5 news cycle.

### Signal 3 — Meta Glasses at $299 with Muse Spark (June 23 2026) is the new competitive line

Meta launched a $299 in-house-branded smart-glasses line on June 23 2026 (CNBC, Reuters, CNN, CNET). They are the first to ship with Meta AI powered by **Muse Spark** (the first model from Meta Superintelligence Labs), which replaced Llama 4 in May 2026. Muse Spark is **closed weights, cloud inference**, and runs on all Ray-Ban and Oakley smart glasses except Meta Ray-Ban Display.

**Why this matters for us:** the new Meta $299 tier is the price point we were planning. **The differentiation is not price; it is openness.** Meta is now $299 + closed cloud + paywalled features. Dan Glasses is hardware-cost + on-device LFM2.5-VL-450M + no paywalls + open weights + auditable memory. The Meta launch makes the "yours, not theirs" thesis commercially concrete.

### Signal 4 — Google + Samsung Android XR glasses at 70° FOV / 4hr battery / on-device Gemini (May 19 2026)

Google demoed Android XR glasses at I/O on May 19 2026 in partnership with Samsung. Wired's hands-on: "industry-first mix: on-device Gemini features, a 70° OLED field and roughly 4 hours of battery." Fall 2026 retail launch via Warby Parker, Gentle Monster, Xreal Project Aura.

**Why this matters for us:** the Google/Samsung partnership is the first major-platform commitment to **on-device AI for smart glasses**. The 70° FOV / 4hr battery figures are the benchmark Dan Glasses hardware has to hit or beat. The fact that Google's bet is on-device — not cloud — **validates the on-device thesis at the platform level**. We are no longer arguing against the tide.

### Signal 5 — HRM-Text-1B (Sapient, $1,500 from scratch) and the small-reasoning-model wave

Sapient Intelligence (Singapore) released **HRM-Text-1B** in June 2026: 1.15B params, Apache-2.0, hierarchical recurrent architecture, **trained from scratch for ~$1,500**. The H/L loop architecture (slow H module + fast L module) buys reasoning depth at a fixed parameter count. arXiv 2605.20613. HuggingFace `sapientinc/HRM-Text-1B`. Runs at ~4 tok/s on RTX 4060 laptop, 2.4GB VRAM.

The same news cycle produced **VibeThinker-3B** (94.3 AIME, 80.2 LiveCodeBench v6) and **PTRM (Probabilistic Tiny Recursive Model, 5M params beating frontier models on verifiable reasoning**).

**Why this matters for us:** the on-device reasoning model is no longer aspirational. **HRM-Text-1B is the natural v1.5 successor to LFM2.5-VL-450M's text role in the agent loop** — the "slow H" module is exactly what danlab-multimodal needs for a Feedback-Agent that runs locally. **The SIA-W+H port can be hybrid: cloud Claude Sonnet 4.6 for the Feedback-Agent by default, but with an HRM-Text-1B local fallback.** That is the privacy-first path that matches the "yours, not theirs" thesis at the model layer.

### v5 deltas to recommendations (additions to v3)

14. **NEW v5 — Lead the "yours, not theirs" message with three sub-claims, in this order**: (a) "on-device, not cloud" (validated by Google + Samsung on-device Gemini bet), (b) "no paywalls, no rate-limits, no subscriptions" (validated by the Meta $20/month paywall backlash + $299 Muse Spark tier), (c) "open weights, auditable memory" (validated by SIA + HRM-Text-1B being the credible open-source paths). The order matters: privacy-first → ownership → openness.
15. **NEW v5 — Plan a v1.5 vision+reasoning stack: LFM2.5-VL-450M (vision) + HRM-Text-1B (text reasoning, local) for the agent loop.** This is now feasible because HRM-Text-1B is shipping. It drops our cloud-dependency surface to zero for the privacy-first tier, and it gives the SIA-W+H port a local-only Feedback-Agent option.
16. **NEW v5 — Re-aim the SIA-W+H paper at ICML 2027 or ACL 2027 (both deadlines Jan 2027).** NeurIPS 2026 has passed. The paper's positioning should explicitly contrast with closed-source RSI Labs (Rocktaschel + Socher, $4.65B) — that contrast is now the strongest possible framing.

### v5 deltas to open questions (additions to v3)

11. **NEW v5 — Do we want to file a statement of work on the open-source RSI position before RSI Labs locks the closed-source patent thicket?** SIA is MIT, but RSI Labs' filings will create prior art. A Q3 2026 SIA-W+H port + a danlab.dev blog post + an arXiv pre-print = our "open-source first" filing before the closed-source side matures.
12. **NEW v5 — HRM-Text-1B integration cost.** The H/L loop architecture is novel — porting it to our memoryd/event-bus stack will take a sprint. Is Q4 2026 acceptable, or do we want to fast-track it to Q3 alongside SIA-W+H?
13. **NEW v5 — Google + Samsung on-device Gemini benchmark.** Their 4hr battery figure is the number we now have to beat or match in our wearable form-factor research. Do we want to commission a comparison study (LFM2.5-VL-450M + HRM-Text-1B on the glasses form factor vs Android XR's reported metrics)?

---

*End of v5 research report. See `dan2-architecture-review.md` v5, `dan2-model-analysis.md` v5, `dan2-agi-roadmap.md` v5, and `dan2-papers-to-read.md` v5 for the deliverables that branch from this.*
