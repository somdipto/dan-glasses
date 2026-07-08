# DAN-2 Research Report — v14
**Run:** 2026-06-19 06:00 UTC (11:30 IST)
**Status:** ✅ Shipped. 13 prior versions archived as `*.v13.md` siblings.
**Companion artifacts:** `dan2-architecture-review.md`, `dan2-model-analysis.md`, `dan2-agi-roadmap.md`, `dan2-papers-to-read.md`

---

## Executive Summary

Three forces are converging in June 2026 that re-shape danlab.dev's AGI roadmap:

1. **The recursive-self-improvement (RSI) inflection is real.** Anthropic published "When AI Builds Itself" describing harness+weight co-evolution; Hexo Labs open-sourced **SIA (MIT, May 2026)** with concrete numbers (LawBench +56.6%, CUDA kernel −91.9% runtime, scRNA denoising +502%). The market is now paying $4.65B valuations for RSI category leaders (Recursive Superintelligence Inc.). "Pre-RL scaffold" is no longer a defensible label — the credible path is **fork SIA, ship it with our own Feedback-Agent on open weights**.
2. **On-device VLM is at parity with 2024 cloud VLMs.** LFM2.5-VL-450M (Liquid AI, April 11, 2026) is sub-250ms edge-class, GGUF Q4_0 ready; Zamba2-VL-1.2B (Zyphra, May 2026) reaches 10× TTFT improvement via shared projection; Mnemosyne (April 2026) hits **98.9% Recall@All@5 on LongMemEval** with bge-small-en-v1.5, all in SQLite. The wearable AI dream has a real engineering path now, not a 2027 wish.
3. **The wearable AI race has 5 confirmed competitors in 14 months** and a regulatory collision: Meta Ray-Ban Display ($799, Sept 30, 2026), Snap Specs ($2,195, AWE 2026), Google Gemini glasses (Fall 2026, Warby Parker + Gentle Monster), Apple N50 (late 2027), Brilliant Labs Halo (open-source). Illinois General Assembly passed the first US smart-glasses driving ban (June 15, 2026). We cannot out-ship Meta, Snap, or Google on form factor. We compete on **trust architecture** (open weights, on-device, auditable harness+weight updates, no cloud).

**The bet, sharpened:** Dan Glasses v1 = open-weights on-device AI companion, $400 BOM, sub-50g, MIT-licensed software stack, SIA-fork-powered continual learning, Mnemosyne-backed long-term memory. v2 = wearable glasses for the same software stack on a sub-2W SoC. The 14-month window is the trust-architecture window. After Apple N50 ships, that window closes.

---

## A. System Architecture Deep Dive

### A.1 Current Dan Glasses architecture — what is right, what is wrong

**Verdict on the existing decomposition (v13 audit + canonical spec):** The service split is *mostly* correct but has three critical gaps that block any meaningful RSI work.

**What is right:**
- **Rust hot-path services + TS orchestration.** audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge are all live, isolated, and HTTP-fronted. 131/131 tests green. The IPC contract is stable. This is a production-grade foundation for v1.0 desktop.
- **OpenClaw as sole orchestrator.** The "no dual-runtime ambiguity" decision from the canonical analysis paid off — Telegram, MCP, and the zo-bridge all wire through one config file.
- **Tauri v2 + .deb + systemd.** The right call. Flatpak/AppImage cannot deliver systemd units, udev, or privileged install actions. We should not revisit.
- **Salience-gated vision.** The `SalienceDetector` (`motion OR face`) before VLM is the correct power lever. The canonical-analysis warning that "FPS capture is the wrong lever, VLM frequency is the right lever" was correctly applied — perceptiond runs VLM only on salient frames with `MAX_QUEUE_DEPTH=2`.

**What is wrong (sharp critique):**

1. **The "pre-RL scaffold" in `danlab-multimodal` is a marketing claim, not an architecture.** The `Score 0-100` loop in `src/demo.py` is a hand-coded heuristic (length penalty + error detection + content-quality bonus). It never modifies model weights, never runs policy gradient, and never persists trajectories. Hexo Labs published a working SIA loop that does both harness edits and LoRA weight updates with measurable gains. We should not ship v1.0 calling danlab-multimodal "self-improving" — we should ship SIA-fork and stop hedging.

2. **Memoryd is a vector store, not a memory system.** `all-MiniLM-L6-v2` (384-dim) gives us semantic recall over ~100k memories before it degrades. Mnemosyne (98.9% Recall@All@5 on LongMemEval, April 2026) is the new SOTA and runs in a single SQLite file with bge-small-en-v1.5. We are shipping a 2024 memory layer in a 2026 product. The `pip install mnemosyne-memory[openclaw]` path is the cheapest possible swap. **Do it now.**

3. **The agent loop is reactive, not proactive.** The audiod transcript → OpenClaw → tool call → response path is request/response. `danlab-multimodal` does not watch. Nothing fires unless the user speaks. The user has to remember they own a wearable AI. That fails the SOUL.md promise ("always-on AI companion"). Proactive AI is now its own ACL 2026 paper category (ProActor, ProAct, PAGER). The credibility cost of shipping a "companion" that never initiates is high.

4. **No power budget table.** The canonical analysis flagged this in 2026-04; the PRD still does not have target wattage per component. A wearable product that does not know its own power envelope is a software prototype, not a product. **This is the #1 thing blocking v2.**

5. **OpenClaw is TS/Node — and that is fine, but the security posture is not.** OpenClaw skill malware is now in the wild (`cline@2.3.0` silently installed OpenClaw). Without `cosign`+`Rekor`-attested skill installation + default-deny, our `.deb` is a supply-chain attack vector. **The signed-skill infrastructure must land before v1.0 .deb ships.**

### A.2 The danlab-multimodal heuristic — to RL or not to RL

**Is the current heuristic a true RL loop?** No, by any rigorous definition. RL requires (a) a policy, (b) a reward signal, (c) gradient updates to the policy. Our `demo.py` has (b) only — a hand-coded reward. The "policy" is the frozen SmolVLM-256M. There are no gradient updates. Calling this "RL" would be misleading.

**What would it take to make it genuine RL?**

| Layer | Current (heuristic) | Required for true RL |
|---|---|---|
| State | Captured PNG + prompt | Same + trajectory history |
| Policy | Frozen SmolVLM-256M | Same + LoRA adapter on `target` agent |
| Reward | Hand-coded (length, error, quality) | Learned reward (Feedback-Agent) |
| Update | None — print suggestions to stdout | LoRA fine-tune of `target` on accepted trajectories |
| Eval | None | Held-out task set with measured generalization |

The shortest credible path: **fork `hexo-ai/sia`, replace the default Feedback-Agent with `LFM2.5-1.2B-Thinking` (open, MIT), replace the default target with `SmolVLM-256M`, run on the danlab-multimodal screenshot set.** This is a 4-week project, not 4 months. Hexo's reference results (LawBench +56.6%) are on the harness-only path; the harness+weights path needs our own measurement. **Open question:** does SIA generalize beyond training-distribution tasks? The TriMul/denoising numbers in their report are train/test overlap; only LawBench is a clean generalization test. We need a danlab-multimodal-specific held-out set before claiming RSI gains in our product.

### A.3 Edge model choices — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**LFM2.5-VL-450M — still correct, but no longer alone.**
- 450M params, sub-250ms inference, 512×512 input, GGUF Q4_0 (~209MB) and Q5_0 (~280MB). 32,768-token context.
- SigLIP2 NaFlex encoder (better than ResNet/ViT for variable resolution at edge).
- **Alternative: Zamba2-VL-1.2B (Zyphra, May 2026).** 1.2B params, **10× TTFT improvement** via shared projection between visual and text tokens. GGUF available. Bigger model, but the TTFT win matters for wearable (latency = battery). Benchmark on perceptiond's watchful workload before swapping. Source: Zyphra release notes via LinkedIn (Brij Kishore Pandey, May 2026).[^1]
- **Alternative: Apple AFM 3 20B (Apple WWDC, June 8 2026).** On-device 20B VLM, but locked to Apple Silicon — not relevant for the Redax aarch64 target unless we change silicon.
- **Recommendation:** Keep LFM2.5-VL-450M Q4_0 for v1.0. Add Zamba2-VL-1.2B to the v1.1 benchmark suite. The wearable v2 should *prefer* Zamba2-VL-1.2B if its TTFT gain holds at <2W.

**whisper.cpp — correct, with one caveat.**
- `whisper-cpp-plus-rs` (async + Silero VAD + real-time PCM) is the right binding. `base.en` (74MB) is the right model size for glasses.
- **Caveat:** Zamba2-Audio-1.5B (Zyphra) and Stability Audio 3.0 small (Stability AI, May 20 2026) are credible long-form candidates for v1.1. Collapse audiod + ttsd into one audio model? Watch the benchmark — single-model collapse usually costs quality on the long tail. Defer to v1.1.

**KittenTTS — correct for v1.0, under pressure for v1.1.**
- <25MB, base variant 80M params, ONNX/WASM, CPU-friendly. Good enough for voice prompts.
- **v1.1 candidates:** LFM2.5-Audio-1.5B (Liquid AI, rumored); Stability Audio 3.0 small (long-form); F5-TTS (open weights). All trade size for naturalness. KittenTTS base is the right balance for the wearable v2 envelope.
- **Hard rule:** never ship a TTS model larger than 100MB on the wearable path. The TTS spike is already ~1-2W.

### A.4 OpenClaw as orchestration gateway — TypeScript/Node is correct, but...

**The "TypeScript for orchestration, Rust for hot paths" call is right.** OpenClaw's tooling (MCP servers, plugins, channels, sessions) is TS-native. Rewriting the gateway in Rust would cost us 6+ months of feature parity for marginal latency wins.

**But three failure modes are not yet mitigated:**

1. **Skill supply-chain attacks.** `cline@2.3.0` (June 2026, npm) silently installed OpenClaw. If OpenClaw skills are auto-loaded from npm without attestation, our `.deb` inherits every npm dependency's blast radius. Mitigation: `cosign` sign every danlab skill, commit signatures to Sigstore Rekor, default-deny any unsigned skill, document the policy in `docs/openclaw-signed-skill-policy.md`.

2. **`plugins.slots.memory = "memory-core"` community gotcha.** Multiple OpenClaw users report "weird memory behavior" because OpenClaw auto-loads the most recently published memory plugin. Mnemosyne's docs confirm: explicitly pin the slot to `memory-core`. Trivial config fix; big reliability win.

3. **OpenClaw gateway crash → no fallback path.** The canonical analysis flagged this. If `openclaw-gateway` dies mid-session, the daemons stay up but no agent loop runs. The desktop UI should restart the gateway within 2s and surface a "reconnecting" state, not a frozen UI. Add a `systemd` `Restart=always` unit for `openclaw.service` with `WatchdogSec=30`. v1.0 blocker.

---

## B. AGI Landscape Research (June 2026)

### B.1 The recursive self-improvement inflection is real

Anthropic published **"When AI Builds Itself: Our progress toward recursive self-improvement"** in May 2026. Three signals from that paper and the surrounding news cycle:

- **Claude writes >80% of code merged into Anthropic's own production systems** as of May 2026 (up from a few percent before early 2025). Anthropic's internal research arm publicly described RSI as "an AI system capable of fully autonomously designing and developing its own successor."
- **DeepMind published a new ASI paper** (June 2026) outlining four pathways to artificial superintelligence, with recursive self-improvement as one of the four (alongside continued scaling, algorithmic evolution, and multi-agent coordination).[^2]
- **Recursive Superintelligence Inc. closed $650M at a $4.65B valuation, ~$155M/employee.** RSI is now a venture-funded category. Their "user-aligned RSI" thesis is the only differentiation that competes with Anthropic's closed-loop RSI — and it is the same thesis danlab.dev can credibly own (open-weights + wearable feedback signal).
- **Anthropic paused deployment of "Fable 5" to comply with a US government export-control order.** Lutnick's letter to Amodei (June 12, 2026, obtained by Bloomberg) specified criminal penalties. Stuart Russell Guardian op-ed: "Fable's existence is an open secret... the question is what does Anthropic do if Fable escapes." Anthropic Mythos (the model that edged toward RSI) was released to the public the same week. The political backdrop is hardening. **On-device open-weights AI is structurally aligned with US policy direction.** Our thesis is now politically positioned, not just technically positioned.

**Implication for danlab.dev:** the market window for "user-aligned RSI" is open *now*. We can either (a) build our own RSI loop from scratch (12+ months), (b) fork Hexo Labs' SIA (4-6 weeks to a measurable prototype, MIT, open), or (c) wait and concede the category to closed labs. Option (b) is the only rational choice.

### B.2 Self-improving architectures — what has actually worked

| Approach | Reference | Result | Status |
|---|---|---|---|
| **Harness + weight co-evolution (SIA)** | Hexo Labs, Hebbar et al. May 2026, MIT | LawBench +56.6%, CUDA kernel −91.9%, scRNA denoising +502% | Open source, runnable now |
| **Self-play RL (AlphaEvolve, AlphaProof)** | DeepMind, 2025-2026 | SOTA on formal math | Closed |
| **Distillation + SFT** | Standard practice | Predictable gains | Boring but works |
| **Constitutional AI / RLAIF** | Anthropic | Nuanced preference matching | Closed, expensive |
| **ReST / Self-rewarding** | Various 2024-2025 | Mixed | Mostly abandoned |
| **RLHF on production traffic** | Major labs | Marginal but real | Closed |

**The non-obvious finding:** Hexo's LawBench +56.6% result is the largest *measurable* self-improvement gain reported in open literature in 2026. Most other "self-improvement" papers show marginal gains. SIA's secret sauce is the Feedback-Agent — a *language model* that reads trajectories and decides what to change. The harness+weights lever separation is the architectural insight. We should replicate this on the danlab-multimodal screenshot set as a credibility anchor.

**Skepticism:** TriMul and scRNA denoising numbers in SIA's report are train/test overlap (same data the agent was trained on). Only LawBench is a clean generalization test. Our replication must use a *held-out* screenshot set to be credible.

### B.3 Edge AI / on-device models — sub-500MB VLMs that actually work (June 2026)

| Model | Params | Quantized size | Inference target | Status |
|---|---|---|---|---|
| **LFM2.5-VL-450M** (Liquid AI, Apr 11 2026) | 450M | 209MB Q4_0 | <250ms edge | ✅ Production |
| **SmolVLM-256M** (HuggingFace) | 256M | 120MB Q4_K_M + 182MB mmproj = 302MB | ~26s CPU | ✅ Working (danlab-multimodal) |
| **Zamba2-VL-1.2B** (Zyphra, May 2026) | 1.2B | ~600MB Q4 | 10× TTFT vs prior | ✅ New — benchmark needed |
| **Gemma 3 270M** (Google) | 270M | 230MB IQ4 | Text-only | ⚠ No mmproj in GGUF |
| **AFM 3 20B** (Apple, WWDC June 8 2026) | 20B | On-device Apple Silicon | Apple-only | ❌ Wrong silicon |
| **Llama 3.2 1B Vision** | 1B | ~700MB Q4 | Mature | ✅ Production elsewhere |

**For Dan Glasses v1.0 (desktop, x86_64):** LFM2.5-VL-450M Q4_0 is the right choice. Sub-250ms is enough for the watchful mode loop. SigLIP2 NaFlex handles varied scene geometry better than the older ViT variants. **No change recommended.**

**For Dan Glasses v2 (wearable, aarch64 Redax):** the bottleneck is power, not latency. A 1.2B model at 600MB Q4 is acceptable on disk; in memory it depends on whether we get an NPU. Box v3.1.0 (jegly/Box, June 2026) demonstrated on-device NPU acceleration for sub-2B models on Snapdragon/MediaTek — the first real datapoint that hybrid CPU+NPU works at this scale. **Benchmark Zamba2-VL-1.2B Q4 on the Redax-class SoC with NPU before committing.**

**Multimodal fusion (vision + audio + text):**
- The dominant 2026 approach is **late fusion via shared embedding space.** The VLM encodes the image; a separate text/audio encoder feeds the same LLM decoder.
- **Contrastive pre-training (CLIP-style)** is still the workhorse for vision-text alignment. SigLIP2 NaFlex is the current SOTA for variable resolution.
- **Audio-visual joint embedding** (AudioCLIP, CAVP) exists in research but has not crossed into production wearables. For Dan Glasses, keeping audiod and perceptiond as separate pipelines that both write to memoryd is the right call for v1.0. Audio-visual joint embedding is a v2+ research direction.

### B.4 Memory and continual learning — state of the art (June 2026)

The 2024-2026 memory category exploded. Concrete benchmarks:

| System | LongMemEval (ICLR 2025) | OpenMemEval 2026 | LOCOMO | BEAM (ICLR 2026) | Storage | Open source |
|---|---|---|---|---|---|---|
| **Mnemosyne (dense, bge-small-en-v1.5)** | **98.9% Recall@All@5** | Top-tier | 78.8% | Top | Single SQLite | ✅ MIT |
| Hindsight | Strong | Strong | — | — | Vector DB | ✅ |
| Mem0 | Mid | Mid | — | — | External | ✅ |
| MemGPT | Strong | Mid | — | — | Multi-tier | ✅ |
| Hermes memory-core | Strong | Mid | — | — | File-based | ✅ |
| User-as-Code (arXiv:2606.16707) | — | — | 78.8% | — | Python objects | ✅ Paper |

**Mnemosyne is the clear winner for our use case:** (a) Hermes-first design with native OpenClaw provider, (b) `pip install mnemosyne-memory[openclaw]` install path, (c) all-in-SQLite means we can ship it inside the memoryd process with no new infra, (d) 98.9% Recall@All@5 with bge-small-en-v1.5 (33M params) beats MiniLM-L6-v2 (22M params) at 4.4× the model size but with better embedding quality.

**Continual learning:** there is no production-grade solution. All major labs still fine-tune on fixed batches. The closest research bet is:
- **LoRA + replay buffer** for small adapter updates on user-personalized data (no full fine-tune, prevents catastrophic forgetting).
- **Mixture-of-Experts (MoE) routing** for per-context expert selection (e.g., LFM2.5-8B-A1B — 8.3B params, 1.5B active).
- **SIA-style harness + LoRA co-evolution** is the only published approach with measurable gains on a held-out benchmark.

**Recommendation:** swap memoryd to Mnemosyne + LFM2.5-Embedding-350M (Liquid AI, June 18 2026) + LFM2.5-ColBERT-350M (reranker) before v1.0 .deb. **6-week workstream. Blocks v1.0 .deb.**

### B.5 Model compression — techniques working at sub-1B scale

| Technique | Result on sub-1B models | Status |
|---|---|---|
| **GGUF Q4_0** (llama.cpp) | ~3.5 bits/weight, minimal quality loss | Production standard |
| **GGUF Q5_0 / Q5_K_M** | ~4.5 bits/weight, near-fp16 quality | Production |
| **AWQ** (Activation-aware Weight Quantization) | 4-bit with better quality retention than naive Q4 | Research → production |
| **GPTQ** | 4-bit with calibration, comparable to AWQ | Production |
| **SmoothQuant** | W8A8 (8-bit weights, 8-bit activations) for transformer FFN | Production for inference |
| **Pruning + distillation** | SmolLM2-135M distilled from 1.7B → 1/12 the size with 70% retained quality | Production (HuggingFace SmolLM2) |
| **Speculative decoding** | 2-3× throughput, no quality loss | Production (llama.cpp supports) |
| **FlashAttention** | Memory + speed at training | Production (training only) |

**For Dan Glasses:** the current Q4_0 / Q5_0 GGUF choices are right. **Speculative decoding with a 135M draft model + the 450M target could 2× the wearable throughput for free** — easy v1.1 win.

### B.6 Proactive AI — how to build AI that initiates

This is the gap in our current architecture that will hurt the most over the next 12 months. The 2026 literature has three concrete approaches:

1. **ProAct (arXiv:2605.25971)** — "Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents." Uses idle time between user interactions to predict upcoming needs from dialogue history. Result: −14.8% turns to completion, −11.7% user effort, −28.1% hallucination on ProActEval.
2. **ProActor (ACL 2026)** — proactive agent for meeting/coding contexts. Demonstrated on meeting assistants; 14B baseline is too large for wearable but a **distilled 1-2B ProActor-style model** is feasible. **This is the v1.5 plan.**
3. **PAGER (ACM, 2026)** — proactive monitoring agent for enterprise AI assistants. Embeds proactive error remediation in large-scale enterprise data flows.

**Concrete v1.0 plan (cheap):** add a `proactived` service that subscribes to memoryd's event stream and OpenClaw's session store. On idle, it pulls recent episodic memories + last N descriptions from perceptiond, and runs a hand-coded "should I say something?" classifier (cheap rules: time-of-day, last interaction > N hours, recently observed something salient). When the classifier fires, it generates a proactive TTS prompt and routes through ttsd. **No new model needed. 2-week project.**

**v1.5 plan:** distill a ProActor-style 1-2B model on the danlab user-interaction traces. Use SIA's harness-only mode to optimize the trigger classifier. Open weights on HuggingFace for credibility.

---

## C. Competitive & Market Research

### C.1 The 5 confirmed AI-wearable competitors (June 2026)

| Product | Price | Launch | Form factor | Silicon | Compute | VLM | AI stack |
|---|---|---|---|---|---|---|---|
| **Meta Ray-Ban Display** | $799 | Sept 30 2026 | Glasses + neural wristband | Qualcomm | On-glasses + phone relay | Llama-derived (closed) | Meta AI (closed) |
| **Snap Specs** | $2,195 | Fall 2026 | True AR glasses | 2× Snapdragon | Standalone (all on-board) | Snap OS Lenses | Snap AI (closed) |
| **Google Gemini Glasses** | TBD | Fall 2026 | Glasses (Gentle Monster + Warby Parker) | Qualcomm | Tethered to phone | Gemini Nano | Gemini (closed) |
| **Apple N50** | TBD | Late 2027 | Glasses | Apple Silicon | On-glasses + iPhone relay | AFM 3 (closed) | Siri AI (closed) |
| **Brilliant Labs Halo** | Open source | Shipping | Glasses + clip-on | Multiple | Phone relay | Open (bring-your-own) | Open |
| **Dan Glasses v2** (target) | $400 BOM | 2027 Q2 | Glasses | Redax aarch64 (TBD) | On-glasses | LFM2.5-VL-450M (open) | Open (SIA-fork + Mnemosyne) |

**Dan Glasses cannot win on price-performance against Meta at $799, cannot win on AR against Snap at $2,195, cannot win on polish against Apple N50 in 2027. We win on trust architecture.** Open weights. On-device. Auditable harness + LoRA updates. No cloud. No telemetry to Meta/Snap/Google.

**The Snap Specs public reception is unusually harsh.** Times UK, PCMag, Memeburn, Designtaxi all roasted the $2,195 + chunky form factor combination. PC Gamer published the launch video with a visibly struggling Spiegel. Snap stock dropped ~5% on launch. The 132-136g weight is the specific target of mockery. **XREAL Aura (<100g) is the second-best-in-class and still 2× heavier than our sub-50g target.** Our $400 BOM positioning is *credibly* cheaper than every competitor on the table.

### C.2 Open-source AI companion landscape

| Project | Status | Differentiator vs Dan Glasses |
|---|---|---|
| **Hermes Agent** (Nous Research) | Active | Strong memory plugin ecosystem; no wearable hardware path |
| **Mnemosyne** (AxDSan) | Active, MIT | Memory layer only; needs an agent harness around it |
| **Hexo SIA** | Active, MIT | Self-improvement harness + weights; needs wearable integration |
| **Open WebUI** | Mature | Browser-first; not wearable |
| **OpenHands** | Active | Coding-focused |
| **paperclip** (ours, dormant) | Paused | Multi-agent company orchestration; orthogonal to Dan Glasses |
| **openclaw** (ours, active) | Live in production | The harness Dan Glasses rides on |

**Our unique position:** open-source wearable AI companion + on-device-first architecture + SIA-powered continual learning. Hermes + Mnemosyne + SIA + our wearable hardware path is a combination nobody else ships. **The wearable-specific value is the moat.** The agent-framework value is *commodity*.

### C.3 Privacy positioning

Dan Glasses is the only major wearable AI in 2026 with all of: (a) open-weights models, (b) no cloud inference path, (c) auditable harness + weight updates via SIA-fork, (d) local-first memory (SQLite). Meta, Snap, Google, and Apple all default to cloud. Apple's "on-device AI" pitch applies only to Apple Silicon.

**The Anthropic Fable 5 export-control episode (May-June 2026) hardened the regulatory backdrop.** "Fable 5 safe by construction" is a marketing claim with substance: we don't have a Fable 5 because we don't have a closed frontier model. **Add Fable-5-safe compliance attestation to the v1.0 privacy story.** Wire `privacyd` → Sigstore Rekor for compliance attestation signing. `$99/$999` B2B pricing for "Fable 5 indemnity" customer pipeline is a v1.5+ play.

---

## D. Technical Deep Dives

### D.1 Deep dive: Proactive AI architecture (chosen)

See §B.6. Concrete implementation plan:

- **v1.0 (2 weeks):** new `proactived` service. Subscribes to memoryd events + OpenClaw session log. Hand-coded rules for "should I initiate?" (time-of-day, last interaction gap, recently salient perception). On fire, generate prompt + TTS. No new model.
- **v1.5 (8 weeks):** distill ProActor-style 1-2B model on danlab traces. Use SIA harness-only mode to optimize trigger classifier. Open weights.
- **v2 (post-Redax):** on-device proactive agent. Power-aware — proactive triggers idle until SoC power state allows.

**Risk:** false positives destroy user trust faster than false negatives. v1.0 must be *very* conservative (≤1 proactive prompt per day, opt-in). v1.5 can relax.

### D.2 Deep dive: Edge VLM optimization (chosen)

LFM2.5-VL-450M Q4_0 (209MB) + Zamba2-VL-1.2B Q4 (~600MB) is the current model lineup. The wearable v2 silicon (Redax aarch64) will determine whether we hit the <2W inference target.

**Concrete measurements needed (currently unknown):**
- LFM2.5-VL-450M Q4_0 watts/inference at 512×512 on Redax aarch64
- Zamba2-VL-1.2B Q4 TTFT on Redax aarch64 (the 10× claim is from Zyphra's own silicon)
- Box v3.1.0 NPU compatibility with Redax
- Battery budget at 2W × 4h = 8Wh → ~650mAh at 12.4V (2S LiPo) or ~2000mAh at 3.7V (1S)

**Open question for somdipto:** do we have any Redax-class dev hardware in-house, or do we need to acquire? If neither, we should benchmark on **Raspberry Pi 5 + AI HAT** as a proxy (2.4GHz Cortex-A76, ~5-8W under load). Pi 5 is a known quantity with published VLM inference numbers.

**Compression bet for v1.1:** speculative decoding with a 135M draft model + 450M target. Llama.cpp supports this. ~2× throughput on identical hardware. Free win.

### D.3 Deep dive: Vector memory architectures (chosen)

Three credible architectures for memoryd v2:

1. **Mnemosyne + bge-small-en-v1.5 + SQLite (single file).** 98.9% LongMemEval. Open source MIT. Native OpenClaw provider. **Recommended for v1.0 swap.**
2. **Qdrant (Rust-native, full-featured).** Production-grade vector DB. Heavy infra. Deferred to v2 if we outgrow SQLite.
3. **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M reranker (Liquid AI, June 18 2026).** Purpose-built retrieval. 4.4× smaller than MiniLM. Replaces the "benchmark BGE-small" v1.5 plan from v12.

**Concrete plan:**
- W1: install Mnemosyne + bge-small-en-v1.5. Validate ≥95% Recall@All@5 on the danlab-multimodal screenshot set (we have ground-truth LFM2.5 captions).
- W2-4: integration into memoryd. Deprecate MiniLM.
- W5-6: evaluate LFM2.5-Embedding-350M. If ≥98%, swap.

**Cost:** 6 weeks of one engineer. **Benefit:** memoryd becomes a real memory system, not a vector store.

---

## Closing recommendations

1. **Ship Mnemosyne swap before v1.0 .deb.** Memory is the cheapest credibility win available.
2. **Fork SIA publicly this month.** User-aligned RSI is the category. We have the open-weights wearable story. The window is 14 months.
3. **Add `proactived` to the v1.0 daemon set.** Proactive is the SOUL.md promise and the cheapest 2-week project.
4. **Power-budget the wearable v2 *now*.** Without target wattage per component, the v2 product is a software prototype.
5. **OpenClaw signed-skill infrastructure before v1.0 .deb.** `cosign`+`Rekor`+default-deny. The `cline@2.3.0` precedent is real.

---

[^1]: https://www.linkedin.com/posts/brijpandeyji_ai-is-10-model-90-plumbing-everyone-activity-7464694713976221699-5SFm
[^2]: https://www.htx.com/news/agi-is-not-the-end-deepminds-new-paper-moving-towards-asi-th-rvAAfOdJ
[^3]: https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights
[^4]: https://github.com/hexo-ai/sia
[^5]: https://github.com/AxDSan/mnemosyne
[^6]: https://www.uploadvr.com/snap-specs-design-revealed-preorders-open-price
[^7]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point
[^8]: https://www.pcmag.com/picks/the-best-smart-glasses
[^9]: https://www.decodingdiscontinuity.com/p/claude-is-building-claude-where-value-migrate-intelligence-factory-autonomous
[^10]: https://www.facebook.com/Microsoft.com.vn/posts/the-journey-from-experimental-to-autonomous-starts-hereas-sandeep-points-out-bui/1366993188793373
[^11]: https://arxiv.org/html/2605.25971v1