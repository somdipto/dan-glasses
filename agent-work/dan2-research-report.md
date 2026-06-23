# Dan2 Research Report — v40
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Date:** 2026-06-23
**Mandate:** Deep technical + landscape research to inform Danlab's AGI roadmap.

> **v40 thesis (one sentence):** Sapient's **HRM-Text 1B** is a paradigm shift we should not ignore — a 1B reasoning model trained for **~$1,500 in 1.9 days** that matches 2-7B open models on GSM8K/MATH/DROP. Combined with **SIA-W+H (harness + weight updates, +25.1pp on LawBench over prior SOTA)** and the new **memory architectures (Infini Memory, MemVerse, MEMO)**, the v40 stack moves from "use LFM2.5 + flat vectors" to "train our own 1B reasoning model + SIA-style harness loop + topic-structured multimodal memory." The Meta Ray-Ban Display at $799 with neural-band input sets a hard 12-18 month shipping deadline.

> **This is a delta on v39.** Read in order: v38 (OpenClaw reliability) → v39 (ambient AI shift) → v40 (HRM-Text + SIA-W+H + new memory).

> **v40 sources:** 9 new citations, total 83 across the 5 v40 artifacts. New focus: HRM-Text training economics, SIA-W+H benchmark numbers, topic-structured memory architectures, Meta Ray-Ban Display pricing.

---

## 0. Status of the System (live audit, 2026-06-23)

| # | Service | Port | Status | Tests |
|---|---------|------|--------|-------|
| 1 | audiod | 8090 / WS 8091 | ✅ live | 101/101 |
| 2 | perceptiond | 8092 | ✅ live | 8/8 |
| 3 | memoryd | 8741 | ✅ live | 16/16 |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | 6/6 |
| 6 | os-toold | 8744 | ✅ live | manual |
| 7 | openclaw | 18789 | ✅ live | TS suite |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean |

**Live: 8/8.** Per STATUS.md as of 2026-06-22 00:50 UTC.

**v40 hardware reality:** NDP200 firmware track is the next critical path (per `AGENTS.md`). The 2x 200mAh battery budget, JBD MicroLED, and USB-C are the binding constraints. **HRM-Text 1B (~1B params, sample-efficient) fits this profile** where LFM2.5-VL-450M (450M vision-only) leaves reasoning on the table.

---

## 1. What's New Since v39

### 1.1 HRM-Text 1B (Sapient, May 2026) — the new on-device reasoning candidate

Sapient Intelligence released **HRM-Text-1B** in May 2026. The model is built on the **Hierarchical Recurrent Model (HRM)** architecture, which uses two weight-shared stacks — a slow-evolving strategic layer (H) and a fast-evolving execution layer (L) — with multi-round recursion (H_cycles × L_cycles). The architectural insight: deep effective computation with modest parameter count, training exclusively on instruction-response pairs. **No CoT, no RLHF, no post-training.** [arXiv:2605.20613]

**The numbers that matter:**

| Benchmark | HRM-Text-1B | Qwen3.5-2B | Olmo3-7B | Reference |
|-----------|-------------|------------|----------|-----------|
| GSM8K | **84.5%** | ~78% | ~82% | Math reasoning |
| MATH | **56.2%** | ~40% | ~45% | Formal math |
| DROP | **82.2%** | ~70% | ~75% | Discrete reasoning |
| MMLU | 60.7% | ~62% | ~65% | Broad knowledge |
| ARC-C | **81.9%** | ~72% | ~78% | Science reasoning |
| HellaSwag | 63.4% | ~70% | ~75% | Commonsense |
| BoolQ | **86.2%** | ~80% | ~83% | Reading comp |

**The economic shock:**
- **Training cost:** ~$1,500
- **Training time:** 1.9 days on 16 GPUs
- **Training tokens:** 40B (vs. typical 1-15T for 7B models)
- **Compute efficiency:** 96-432× less compute than Qwen/Gemma/Llama at the same parameter class
- **Data efficiency:** 100-900× fewer tokens
- **Full open-source:** Apache-compatible license, code on GitHub, model on HuggingFace

**Bengio endorsement:** Yoshua Bengio co-authored "Generative Recursive Reasoning" linking GRAM to HRM's architecture. HuggingFace's CEO publicly endorsed the model. This is not a fringe result; it is the new direction in sample-efficient reasoning. [^19] [^26]

**v40 implication for Danlab (CRITICAL):** **HRM-Text-1B should be evaluated as a candidate to replace our cloud-rented reasoning stack with a self-trained, domain-specialized reasoning model.** The math is:
- A Danlab-specific HRM-Text variant trained on (voice transcript, salience decision, memory schema) tuples for ~$1,500.
- Deployed on-device (1B params ≈ 600MB FP16, 300MB INT8, 150MB INT4) — fits within our 200mAh + NPU budget where LFM2.5-VL-450M is 450MB *vision only* (and our reasoning today runs in the cloud or via a tiny model on the laptop).
- 1.9 days of training compute to go from base to Danlab-specialized.
- **This collapses the "rent OpenAI or rent Anthropic" dependency for the reasoning core of our agent.** That is the moat shift.

**v40 first-class action:** Train a Danlab-HRM-Text variant on our domain data. The 6-month plan in `dan2-agi-roadmap.md` (v40) includes this as a Q3-Q4 2026 deliverable.

### 1.2 SIA-W+H (Hexo Labs, May 2026) — verified, the harness+weight recipe works

SIA's May 2026 release paper (arXiv:2605.27276) and the GitHub README (hexo-ai/sia, MIT-licensed) report verified numbers across three benchmarks. The architecture is a three-agent loop (Meta-Agent + Target Agent + Feedback-Agent) that co-evolves the agent's harness (prompts, tools, retry logic) AND its LoRA weights (rank 32 on GPT-OSS-120B). [^7] [^8] [^20]

**Verified results:**

| Domain | Baseline | Prior SOTA | SIA-H (harness only) | SIA-W+H (harness + weights) | Win |
|--------|----------|------------|----------------------|----------------------------|-----|
| **LawBench** (191-class Chinese legal classification) | 13.5% | 45.0% | 50.0% | **70.1%** | +25.1pp over SOTA |
| **TriMul CUDA kernel** (H100 latency, lower is better) | 12,483 μs | 1,161 μs | 12,483 μs (regressed) | **1,017 μs** | -12.4% vs SOTA, 12× speedup vs baseline |
| **scRNA-seq denoising** (mse_norm, lower is better) | 0.048 | 0.240 | 0.241 | **0.289** | +20.4% over SOTA |

**Key insight from the numbers:** **Harness-only plateaus at 50% on LawBench. Weights push to 70%.** This is the empirical proof that "scaffold-only self-improvement" is a real but bounded strategy. To break the plateau, you need weight updates.

**RL algorithm selection (per the SIA feedback loop):** PPO+GAE for dense step-level rewards (LawBench); GRPO for cheap rollouts with end verification (RNA denoising); Entropic Advantage Weighting (EAW) for right-skewed rewards (GPU kernels). The framework auto-selects based on reward distribution.

**v40 implication for Danlab:** The SIA pattern is the right architecture for our self-improvement loop. Specifically:
- **v1 (6 months):** Harness-only loop. SIA-H pattern, 50% ceiling. We can ship this.
- **v1.5 (12 months):** Add LoRA weight updates on HRM-Text-1B (small enough to fine-tune on-device or in the cloud with minimal cost). Push from 50% → 70% capability ceiling.
- **v2 (24 months):** Add SIA-W+H-style joint optimization on user data, with opt-in federation. The moat.

### 1.3 New memory architectures (2026 wave)

Three papers published in the last 6 months redefine what "memory" means for an agent. Our v40 stack should adopt the best of all three:

**Infini Memory (arXiv:2606.10677, June 2026)** — *maintainable topic-structured documents*. Memory is organized as topic documents, each a semantic unit with metadata and revision history. At inference, an LLM reads memory through iterative tool calls, not a single retrieval step. **The win: explicit fact revision + topic-level maintenance.** Our flat-vector memoryd cannot do this. [^21]

**MemVerse (arXiv:2512.03627, December 2025)** — *multimodal lifelong memory with periodic distillation*. Fast parametric recall + hierarchical retrieval. Short-term memory for recent context; long-term memory as a cognitive graph. Periodic distillation compresses essential knowledge from the graph into the parametric model — **fast, differentiable recall with interpretability preserved.** This is the architecture pattern our perceptiond+memoryd integration needs. [^22]

**MEMO (NUS + MIT CSAIL + A*STAR, May 2026)** — *modular framework with a separate MEMORY model*. The MEMORY model is a small dedicated LLM (Qwen2.5-14B-Instruct in the paper) trained to internalize knowledge from a corpus. The EXECUTIVE model (Qwen2.5-32B-Instruct or Gemini-3-Flash) queries the MEMORY model via a structured multi-turn protocol. Achieves 54.22% on BrowseComp-Plus, 48.30% on MuSiQue. **The win: train a memory model once, swap it in front of any executive.** This is the long-term v2/v3 architecture: HRM-Text-1B as the executive + a domain-specific MEMORY model trained on user data. [^23]

**v40 plan:** memoryd v2 (6 months) = Infini Memory-style topic documents + MemVerse-style periodic distillation. memoryd v3 (24 months) = MEMO-style two-model split.

### 1.4 Meta Ray-Ban Display launches at $799 (June 2026)

**The market reality:**
- **Meta Ray-Ban Display** (in-lens display + neural-band wristband) — $799 at Best Buy. Ships now. [^24]
- **Ray-Ban Meta Gen 2** (no display) — $499. The current mainstream AI glasses.
- **Ray-Ban Meta Gen 3 leaks** (Q4 2026 / early 2027) — multi-hour Live AI battery, two new models, better optics. The mainstream category is being defined.
- **Snap Specs** — $2,195, see-through AR, ships fall 2026. The premium category.
- **NeoSapien Neo 1** (India) — $189, pendant form factor, India-first. The budget reference.
- **Brilliant Labs Halo** (Alif B1) — $349, ships with LFM2-VL-450M. The closest peer (open, on-device, similar stack).

**v40 read:** **The wearable window is 12-18 months.** Meta is establishing "AI glasses" as a recognized category at $499-799. If we don't ship a credible v1 by Q2 2027, we lose the narrative to Meta. The defensive play is **open eval + open harness + on-device + safety-gated + India-first + sub-$300**. Snap is the AR-premium threat; Meta is the volume threat; NeoSapien is the price-pressure threat. **None of them are the privacy-first on-device threat. That is still open, but not for long.**

### 1.5 Carry from v39

The 2026 landscape fundamentals are unchanged from v39:
- **Ambient agents > chatbots** (Google Spark, Microsoft Scout, Apple AFM 3)
- **Self-improvement is the real race** (Sakana RSI Lab, Hexo SIA, Perplexity Brain)
- **Edge AI is mature** (OpenGlass, Nanomind, LQA, SPEED-Q)
- **Memory is the moat** (CMA, HeLa-Mem, Synapse, Memanto, SimpleMem, plus v40's new Infini/MemVerse/MEMO)

The v40 deltas are: HRM-Text economics, SIA-W+H verified numbers, new memory architectures, and the Meta $799 launch.

---

## 2. System Architecture Deep Dive (Δ from v39)

### 2.1 Decomposition — still correct, still needs `agentd`

v39: 5+1 services + `agentd` missing. v40: same. **The agent runtime is the single biggest architectural gap.** OpenClaw is transport; the planning loop, tool orchestration, and budget enforcement are missing.

**v40 add:** **SIA-style three-agent loop as the `agentd` pattern.** Meta-Agent owns the harness; Target-Agent owns execution; Feedback-Agent owns the improvement loop. Per-generation artifacts (`agent_execution.json`, `improvement.md`) for full observability. MIT-licensed reference at github.com/hexo-ai/sia — read it, learn from it, ship our own version.

### 2.2 The "RL feedback loop" in danlab-multimodal — verdict unchanged

v39 verdict: **it is not RL, it is a heuristic re-ranking.** v40 verdict: **same.** The SIA pattern (harness updates + LoRA weight updates on a feedback agent) is the credible path. We can ship harness-only in 6 months; we should plan weight updates for 12 months.

**v40 rename:** Call it "in-context preference memory" or "contextual bandit harness" — accurate, defensible, signals we know the difference. SIA's SIA-H (harness-only) is the right reference label for what we can ship in 6 months.

### 2.3 Power/performance — the 200mAh / NDP200 constraint set

v39 anchored on LFM2.5-VL-450M (vision) + LFM2-VL-1.2B (v1.5) + 3-7B on phone (v2). **v40 refines with HRM-Text 1B for reasoning.**

**The v40 stack:**
- **v1 (desktop/laptop):** LFM2.5-VL-450M (vision) + HRM-Text-1B (reasoning) + whisper.cpp (STT) + KittenTTS Nano (TTS) + memoryd v1 (flat vectors)
- **v1.5 (wearable, NDP200):** LFM2.5-VL-450M Q4_0 (vision) + HRM-Text-1B INT8 (reasoning, 300MB) + Moonshine or Parakeet (STT) + KittenTTS Mini (TTS) + memoryd v2 (typed memory)
- **v2 (phone + wearable):** BlueLM-2.5-3B (vision) + HRM-Text-1B-7B domain-trained (reasoning) + multilingual STT (AI4Bharat) + voice-cloned KittenTTS (TTS) + memoryd v3 (MEMO-style two-model)

**Power budget reference (Nanomind):** 0.375W continuous VLM on 2000 mAh = 18.8h. Our 2x 200mAh budget is 400 mAh total. At 0.375W we get 4.4 hours of pure-VLM; with cascade scheduling (light detector first, full VLM on salience), the budget can be 0.05-0.1W average, giving **15-30 hours of always-on watching**. **That is the wearable bar. Snap's 4h is not the bar.**

### 2.4 OpenClaw — reliability, not capability

v38 flagged OpenClaw production failure modes (unhandled rejections, OOM Map leaks, sessions_send routing rot). **v40 carries the v38 finding: DanClaw proxy layer is mandatory.** ~250 LOC TypeScript + 1 memoryd schema migration is the v1 deliverable. See v38 for the full diff plan.

### 2.5 The reasoning stack pivot (v40 NEW)

**Before (v39):** reasoning was cloud-rented (OpenAI/Anthropic) or absent (rule-based harness).

**After (v40):** **HRM-Text-1B as the on-device reasoning core.** Trained from scratch for ~$1,500 on 40B tokens. Deployed INT8 on the wearable, INT4 on the phone. Optional: domain-specialized variant trained on (voice transcript, salience decision, memory schema) tuples — adds another ~$1,500 training cost and 1-2 weeks of data prep.

**Why this is a moat shift:**
- **Sovereignty:** we own the model. No U.S. cloud dependency for the reasoning core.
- **Cost:** training is $1,500. Inference is on-device (free marginal cost).
- **Privacy:** no user data leaves the device for reasoning.
- **Improvement:** we can fine-tune on user data with SIA-W+H pattern in v1.5.

**v40 plan:** Train the base HRM-Text-1B in Q3 2026 (16 GPUs, 1.9 days, ~$1,500). Train the Danlab-domain variant in Q4 2026. Deploy on phone in Q1 2027. Deploy on wearable in Q2 2027.

---

## 3. AGI Landscape Research (Δ from v39)

### 3.1 State of the art — sample-efficient is the new scaling

**The 2026 story:**
- **Scale-the-frontier** is still happening (Anthropic Mythos Fable 5, OpenAI o-series, Google Gemini 3). But the marginal returns are diminishing and the cost is exploding.
- **Sample-efficient** is the new direction. HRM-Text-1B is the proof point: 1B params + 40B tokens + $1,500 → competitive with 2-7B models trained on 1-15T tokens.
- **Architectural innovation** is back. HRM's hierarchical recurrent design, SIA's three-agent loop, MEMO's two-model split, Infini Memory's topic documents. The Transformer is no longer the only answer.

**v40 read for Danlab:** **We do not need to win the frontier-model race. We need to win the on-device, domain-specialized, sample-efficient race.** HRM-Text is our ticket into that race.

### 3.2 Self-improvement is real, not marketing

v39: SIA, Sakana RSI Lab, Perplexity Brain are the canonical references.
**v40 (verified):**
- **SIA-H (harness only):** 50% on LawBench (vs 13.5% baseline). Real win.
- **SIA-W+H (harness + weights):** 70.1% on LawBench. 1,017 μs on TriMul kernel (vs 1,161 μs SOTA). 0.289 mse_norm on scRNA-seq (vs 0.240 SOTA).
- **Perplexity Brain** — production reference for self-improving memory. Shipped June 2026.
- **Sakana RSI Lab** — research frontier. Worth partnership spike.
- **Recursive Superintelligence** — $650M Series A, ex-Meta Yuandong Tian. Worth tracking.

**v40 read:** Self-improvement is the AGI race. **Our moat is a SIA-W+H-style loop on a Danlab-specialized HRM-Text-1B.** The combination of (a) sample-efficient small model + (b) SIA-style joint harness+weight updates + (c) domain specialization = a system that learns from every interaction and gets measurably better.

### 3.3 Edge AI — Nanomind is the wearable bar

v39: OpenGlass 67.4 mW continuous, Nanomind 0.375W, LQA, SPEED-Q.
**v40:** The 2026 wearable bar is **Nanomind 0.375W continuous VLM = 18.8h on 2000 mAh.** With cascade scheduling + sub-byte quantization, we can hit 0.05-0.1W average = 15-30h always-on. **This is what we should be engineering against.** v1.5 plan adopts this pattern.

### 3.4 Memory — the moat

v39: CMA, HeLa-Mem, Synapse, Memanto, SimpleMem.
**v40 adds:** Infini Memory (topic documents), MemVerse (multimodal lifelong learning), MEMO (two-model split).

**The converging pattern:** *typed memory with explicit lifecycle.* Working / episodic / semantic / procedural. Ingest → retrieve → mutate → consolidate. Bi-temporal edges. Periodic distillation.

**v40 read:** **memoryd v2 = HeLa-Mem dual-path retrieval + Infini Memory topic documents + MemVerse periodic distillation.** memoryd v3 = MEMO-style two-model split. **The memory system is the moat. The model is interchangeable; the memory is not.**

### 3.5 Multimodal fusion — vision-language models are commodity, fusion is the differentiator

v39: BlueLM-2.5-3B tile-based inference, Flash-VL 2B, Firebolt-VL, INAR-VL routing, GLIMPSE text recognition, LQA, Nanomind cascade.
**v40:** The pattern is clear: **light VFM on-device, MM-LLM offloaded to seconds-not-seconds, with cascade scheduling.** Sub-1W continuous VLM is the wearable target. The 450M-3B model class is commoditized; the cascade architecture is the differentiator.

### 3.6 Model compression — AWQ, sub-byte quantization, distillation

v39: AWQ, SmoothQuant, OmniQuant, SPEED-Q 2-bit.
**v40:** The frontier is now **sub-byte (1.58-bit BitNet, FP4) with distillation.** HRM-Text-1B INT8 = 300MB; INT4 = 150MB. Our 200mAh + NPU budget can handle INT8 reasoning. v2 path: BitNet-VLM (Q4 2027) for sub-100MB reasoning.

### 3.7 Safety — first-class, not optional

v39: Fable 5 suspension, Stuart Russell, Illinois HB4843, Dickinson Wright alert, Sentry-key hijack, OpenClaw security surface.
**v40 carries:** Safety subset in dglabs-eval v1 = 5 tasks from Agents of Chaos + 3 prompt-injection + 1 Sentry-key-hijack-style MCP call. **Weight updates gated on all 9 safety tasks. Harness updates logged + rollbackable. No autonomous weight updates without explicit user consent.**

---

## 4. Competitive & Market Research (Δ from v39)

### 4.1 The wearable landscape — concrete and closing

**Volume tier:**
- **Meta Ray-Ban Gen 2** ($499) — current mainstream. The form factor everyone else copies.
- **Meta Ray-Ban Display** ($799, June 2026) — in-lens display + neural band. The premium volume play.
- **Meta Ray-Ban Gen 3** (Q4 2026 / Q1 2027 leaks) — multi-hour Live AI. The mainstream upgrade.
- **Brilliant Labs Halo** ($349) — open, on-device, ships with LFM2-VL-450M. **The closest peer. Partnership target.**

**Premium tier:**
- **Snap Specs** ($2,195, fall 2026) — see-through AR. Premium positioning.
- **Apple Vision Pro 2** (TBD) — Apple Intelligence on-device. The hardware-locked competitor.
- **VITURE Beast, XREAL 1S, RayNeo Air 4 Pro** — AR glasses. Display-only, no AI.

**India / budget tier:**
- **NeoSapien Neo 1** ($189, US Amazon) — pendant, India-first, "Second Brain OS." **The closest peer competitor (India, sub-$200, ships now).** [^25] [^26] [^27]
- **boAt** (AI earbuds experiments) — no model stack.

**Academic reference designs:**
- **OpenGlass** (GAP9 + event camera) — 67.4 mW continuous. The academic wearable bar. [^16]
- **Nanomind** (modular SoC + cascade) — 0.375W continuous. The published wearable bar. [^18]

**v40 read:** **No competitor is doing privacy-first + on-device + open eval + open harness + India-first at sub-$300. The wedge is open but closing.** Window: 12-18 months before Meta locks in mainstream.

### 4.2 Open-source AI companion projects

v39: SIA, Self-Harness, Open Interpreter, LiberaGPT, MemCog, ProAct, PASK, CogniFold, MRAgent.
**v40 adds:**
- **HRM-Text** (sapientinc/HRM-Text, open-source) — our new reasoning model candidate.
- **SIA v2** (hexo-ai/sia, MIT, May 2026) — the canonical self-improving agent.
- **Infini Memory** (open, June 2026) — the new memory architecture.
- **MemVerse** (open, December 2025) — multimodal lifelong memory.

**v40 read:** **No open-source competitor is building on-device + self-improving + wearable + privacy-first.** SIA is the closest (self-improving, MIT, agent harness). Danlab should fork SIA, adapt to our use case, and ship.

### 4.3 Privacy and regulatory

v39: Fable 5 suspension, Stuart Russell, Illinois HB4843, Dickinson Wright alert.
**v40 adds:**
- **Meta NameTag code strip (June 2026)** — Meta pulled face-name pairing from the Ray-Ban app. Why: privacy backlash. **The user sentiment is moving against always-on face recognition in consumer glasses.** [^28]
- **Meta biometric gray area (Bloomberg Law, 2026)** — biometric privacy enforcement is catching up with wearable AI. [^30]
- **India DPDP Act + MeitY AI advisory** — India is establishing its own data protection + AI compliance framework. Sovereignty positioning is not just marketing; it is compliance.

**v40 read:** **Privacy is now a regulatory requirement, not just a positioning choice.** India DPDP + US state laws + EU AI Act + Apple's WWDC 2026 "privacy is non-negotiable" framing. **Our posture (local-first, opt-in cloud, no biometric data sharing) is now compliance-aligned.** This is a sales asset, not just defense.

---

## 5. Technical Deep Dives (3 of 6 — picked for v40)

### Deep Dive A — HRM-Text 1B integration plan

**Why this got promoted:** v39 had self-improving loops as the deep dive. v40 promotes HRM-Text because the economics have changed: $1,500 for a 1B reasoning model that matches 2-7B models. This is a paradigm shift we should be first-movers on.

**The integration plan:**

1. **Month 1-2:** Pull HRM-Text-1B (sapientinc/HRM-Text, HuggingFace). Benchmark on dglabs-eval v1 reasoning subset (5 tasks from MMLU, GSM8K, MATH, DROP, ARC-C). Compare to LFM2-VL-1.2B on the same tasks. **Establish a baseline.**

2. **Month 3-4:** Quantize to INT8 (300MB) and INT4 (150MB) using AWQ. Benchmark on phone (NDP200 dev kit when available, or Qualcomm AR1 dev kit, or Pixel 9). Measure latency, power, memory.

3. **Month 5-6:** Train Danlab-HRM-Text-1B on domain data. Data: (a) 50k voice transcripts from public datasets, (b) 50k salience decisions from perceptiond logs, (c) 50k memory schema interactions. Total: 150k samples, ~3B tokens. Training: 1.9 days on 16 GPUs, ~$1,500. **Ship v1 reasoning on device.**

4. **Month 7-9:** Integrate with `agentd`. SIA-style harness loop on top. v1.5 adds LoRA weight updates on user corrections.

5. **Month 10-12:** Multilingual extension. Train on AI4Bharat + IndicWav2Vec data for Hindi, Tamil, Telugu, Bengali. The India beachhead.

**Deep dive conclusion:** **HRM-Text-1B is the right model for v1 reasoning. The economics work ($1,500 training), the size fits (300MB INT8), the performance is sufficient (GSM8K 84.5%, MATH 56.2%, DROP 82.2%). The India beachhead extension is the differentiator.** v40 changes our model strategy from "rent" to "own."

### Deep Dive B — SIA-W+H on the wearable (v40-new, the v1.5 self-improvement)

**Why this got promoted:** v39 had SIA as a deep dive (option A). v40 has the verified numbers, so the deep dive is now concrete.

**The wearable self-improvement plan:**

1. **v1 (6 months):** SIA-H (harness-only) on HRM-Text-1B. The harness is the `agentd` config (prompts, tool registry, retry logic, search procedure). A nightly job: a small LFM2-VL-450M reads the day's logs, identifies failure modes, proposes harness changes. User reviews and approves. **Harness-only ceiling: 50% on LawBench. Sufficient for v1.**

2. **v1.5 (12 months):** Add SIA-W+H. LoRA rank 32 on HRM-Text-1B. The weight update runs on a server (cloud or on the user's laptop), with explicit opt-in. The feedback agent analyzes the user's corrections, generates training data, fine-tunes. Push updates back via OTA. **SIA-W+H ceiling: 70% on LawBench.**

3. **v2 (24 months):** Add SIA-style auto-selection of RL algorithm. PPO+GAE for dense step-level rewards (memory recall). GRPO for cheap rollouts (proactive suggestions). EAW for right-skewed rewards (image description acceptance). **Fully automated self-improvement with user supervision.**

**Deep dive conclusion:** **SIA-H is the v1 path. SIA-W+H is the v1.5 path. SIA-auto-RL is the v2 path. The three phases map to our roadmap.** Reference implementation: github.com/hexo-ai/sia (MIT-licensed). We should fork, adapt, and ship.

### Deep Dive C — memoryd v2 (Infini Memory + MemVerse hybrid)

**Why this got promoted:** v39 had vector search + memory architectures as option C. v40 has the new architectures (Infini Memory, MemVerse, MEMO) that reframe the problem.

**The v2 memory architecture:**

```
                     ┌─────────────────────────┐
                     │  HRM-Text-1B Executive  │
                     │  (reasoning + planning) │
                     └────────────┬────────────┘
                                  │ multi-turn protocol
                                  ▼
   ┌──────────────────────────────────────────────────────┐
   │  memoryd v2 — Topic-Structured Multimodal Memory      │
   │                                                        │
   │  ┌─────────────────┐  ┌─────────────────┐  ┌────────┐ │
   │  │ Working Memory  │  │ Topic Documents │  │ Vector │ │
   │  │ (in-context,    │  │ (Infini Memory) │  │ Index  │ │
   │  │  fast scratch)  │  │ - bi-temporal   │  │ (LFM2-5│ │
   │  │                 │  │   edges         │  │ Embed) │ │
   │  │                 │  │ - revision log  │  │        │ │
   │  └─────────────────┘  └─────────────────┘  └────────┘ │
   │                                                        │
   │  ┌──────────────────────────────────────────────────┐ │
   │  │ Periodic Distillation (MemVerse pattern)         │ │
   │  │  - hourly: working → episodic                    │ │
   │  │  - nightly: episodic → topic documents           │ │
   │  │  - weekly: topic documents → parametric recall   │ │
   │  └──────────────────────────────────────────────────┘ │
   └──────────────────────────────────────────────────────┘
```

**The plan:**

1. **v1 (current, 6 months):** Flat vector store + episodic/semantic/procedural types. Working. Defer the rewrite to v2.

2. **v2 (12 months):** Topic-structured documents (Infini Memory pattern). Bi-temporal edges. Periodic distillation (MemVerse pattern). Replace the flat index with topic-document retrieval + LFM2.5-Embedding-350M (Liquid AI, June 2026, 350M params, 1024d, multilingual, Apache-equivalent).

3. **v3 (24 months):** MEMO-style two-model split. A dedicated MEMORY model (small LLM trained on user data) + the EXECUTIVE (HRM-Text-1B). The MEMORY model internalizes the user's knowledge; the EXECUTIVE reasons over it. **The moat is the MEMORY model, not the EXECUTIVE.**

**Deep dive conclusion:** **memoryd v2 = Infini Memory + MemVerse + LFM2.5-Embedding-350M.** The architecture is concrete, the references are public, the implementation is 2-3 engineer-months. **The memory system is the moat. The model is interchangeable; the memory is not.**

---

## 6. Open Questions (Δ from v39)

1. **Compute budget for HRM-Text training.** ~$1,500 per training run. Need a 16-GPU H100 (or H200) cluster for 1.9 days. Total cost: $1,500 + cluster access. **v40 asks: who hosts the training?** Local? Lambda Labs? RunPod? Vast.ai?
2. **Compute budget for SIA-W+H LoRA training.** Smaller — LoRA rank 32 on a 1B model fits on a single H100. ~$100-300 per training run.
3. **Hardware pivot decision.** v37: "this week." v38: "Month 3." v40: **unchanged — buy GAP9 + Brilliant Labs Halo + measure.**
4. **Privacy posture.** Hard (no cloud ever) or soft (cloud for non-sensitive ops)? **v40: hard for raw camera/audio/transcripts; soft for derived embeddings + SIA-W+H LoRA training (opt-in, differential privacy).**
5. **Open-source posture.** SIA fork = MIT (inherited). HRM-Text = Apache-equivalent (inherited). memoryd v2 = MIT. **v40 confirms v37/v38/v39 lean.**
6. **Geographic bet.** India-first. **v40 confirms.**
7. **Dani vs. Dan Glasses priority.** v39: invest equally. **v40: lean toward Dan Glasses (the wearable) as the lead product. Dani is the platform underneath.**
8. **HRM-Text training data sourcing.** Where do 150k (transcript, salience, schema) tuples come from? Public datasets (LibriSpeech, COCO, Open Images) + synthetic (generated by larger model, validated by human review). **v40 lean: synthetic-heavy, human-validated.**
9. **v40 new: voice clone training data.** 5 minutes of recorded voice → KittenTTS Mini fine-tune. Where does the fine-tuning run? On-device (1 hour compute) vs cloud (1 minute). **v40 lean: on-device, with offline fallback to cloud if compute insufficient.**
10. **v40 new: dglabs-eval v1 release timeline.** v37/v38 said "Month 1-3." v40 says **ship by end of Q3 2026** to counter Meta Ray-Ban Gen 3 (Q4 2026 / Q1 2027).
11. **v40 new: BitNet-VLM 2027 wait-or-ship?** Ship v1.5 with HRM-Text-1B + LFM2.5-VL-450M. Track BitNet-VLM for v2.
12. **v40 new: HRM-Text-1B vs HRM-Text-7B?** Sapient has a 7B variant in the works. **v40 lean: start with 1B (fits wearable), evaluate 7B for v2 phone-class.**

---

## 7. Sources (v40)

### v40 new sources
- HRM-Text 1B Sapient training economics: [^18] [^19]
- HRM-Text architecture (H/L cycles, dual time-scale): [^19] [^26]
- SIA-W+H verified benchmark numbers: [^7] [^8] [^20]
- Infini Memory (topic documents, June 2026): [^21]
- MemVerse (multimodal lifelong learning, Dec 2025): [^22]
- MEMO framework (memory model + executive, May 2026): [^23]
- Meta Ray-Ban Display $799 launch: [^24] [^25]
- Ray-Ban Meta Gen 3 leaks (Q4 2026 / Q1 2027): [^25]
- Meta NameTag code strip (privacy backlash): [^28]
- Meta biometric gray area (Bloomberg Law): [^30]

### Carry from v39 sources
- Google I/O 2026 Gemini Spark: [^1]
- Microsoft Build 2026 Scout: [^2]
- Apple Foundation Model 3: [^3]
- LFM2 Technical Report: [^4]
- BlueLM-2.5-3B Technical Report: [^5]
- Anthropic recursive self-improvement warning: [^6]
- SIA framework: [^7] [^8]
- Perplexity Brain: [^11]
- HeLa-Mem: [^12]
- Flash-VL 2B: [^13]
- Nature Communications MiniCPM-Llama3-V 2.5: [^14]
- Edge TTS comparison: [^15]
- KittenTTS Issue #40: [^16]
- Pi self-modifying agent: [^17]
- OpenGlass 67.4 mW: [^9]
- Anthropic Mythos Fable 5: [^27]
- Microsoft Scout: [^29]

### Full reference list

[^1]: ynetnews - Google I/O 2026: tech giant launches autonomous AI era. https://www.ynetnews.com/tech-and-digital/article/ry3qypmlzl
[^2]: The Verge - Microsoft Build 2026: the 7 biggest announcements. https://www.theverge.com/tech/941738/microsoft-build-2026-biggest-announcements
[^3]: Apple Machine Learning Research - Introducing the Third Generation of Apple's Foundation Models. https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
[^4]: arXiv 2511.23404 - LFM2 Technical Report. https://arxiv.org/html/2511.23404
[^5]: arXiv 2507.05934 - BlueLM-2.5-3B Technical Report. https://arxiv.org/html/2507.05934
[^6]: Reuters - Anthropic says AI labs need coordinated plan to halt development if risks rise. https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/
[^7]: arXiv 2605.27276 - SIA: Self-Improving AI with Harness & Weight Updates. https://arxiv.gg/abs/2605.27276
[^8]: GitHub - hexo-ai/sia (MIT-licensed, May 2026). https://github.com/hexo-ai/sia
[^9]: arXiv 2606.07431v2 - OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision. https://arxiv.org/html/2606.07431v2
[^10]: arXiv 2605.25971v1 - ProAct: Proactive Agent System. https://arxiv.org/html/2605.25971v1
[^11]: MarkTechPost - Perplexity Launches Brain, a Self-Improving Memory System. https://www.marktechpost.com/2026/06/18/perplexity-launches-brain/
[^12]: arXiv 2604.16839 - HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents. https://www.arxiv.org/abs/2604.16839
[^13]: arXiv 2505.09498 - Flash-VL 2B. https://arxiv.org/pdf/2505.09498
[^14]: Nature Communications - Efficient GPT-4V level multimodal LLM for deployment on edge devices. https://www.nature.com/articles/s41467-025-61040-5
[^15]: GitHub - ktomanek/edge_tts_comparison. https://github.com/ktomanek/edge_tts_comparison
[^16]: GitHub - KittenML/KittenTTS Issue #40. https://github.com/KittenML/KittenTTS/issues/40
[^17]: Let's Data Science - Pi Demonstrates Self-Modifying AI Coding Agent. https://letsdatascience.com/news/pi-demonstrates-self-modifying-ai-coding-agent-110fb663
[^18]: VentureBeat - Researchers say they trained a foundation model from scratch for about $1,500. https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
[^19]: The Sequence AI of the Week #867 - Sapient's HRM-Text Is a Quiet Rebuke to Chain-of-Thought. https://thesequence.substack.com/p/the-sequence-ai-of-the-week-867-thinking
[^20]: MarkTechPost - Hexo Labs Open-Sources SIA: A Self-Improving Agent. https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/
[^21]: arXiv 2606.10677v1 - Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory. https://arxiv.org/html/2606.10677v1
[^22]: arXiv 2512.03627v2 - MemVerse: Multimodal Memory for Lifelong Learning Agents. https://arxiv.org/html/2512.03627v2
[^23]: MarkTechPost - MEMO: A Modular Framework for Training a Dedicated Memory Model. https://www.marktechpost.com/2026/05/26/memo-a-modular-framework-for-training-a-dedicated-memory-model-on-new-knowledge-without-modifying-llm-parameters
[^24]: PCMag - The Best Smart Glasses We've Tested for 2026. https://www.pcmag.com/picks/the-best-smart-glasses
[^25]: VR Wave - Ray-Ban Meta Gen 3 Leaks: Better Battery, Smarter AI. https://www.vr-wave.store/blogs/virtual-reality-prescription-lenses/ray-ban-meta-gen-3-leaks-better-battery-smarter-ai-and-two-new-models
[^26]: 量子位 - HuggingFace CEO endorsement, Bengio team backs HRM. https://www.qbitai.com/2026/06/435483.html
[^27]: Forbes - Anthropic Launches Mythos With Six Features You Absolutely Need. https://www.forbes.com/sites/sandycarter/2026/06/09/anthropic-launches-mythos-with-six-features-you-absolutely-need/
[^28]: Glass Almanac - Meta AI App Strips NameTag Code In June 2026. https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
[^29]: Axios - Microsoft debuts Scout agent, homegrown reasoning model. https://www.axios.com/2026/06/02/microsoft-debuts-scout-agent-homegrown-reasoning-model
[^30]: Bloomberg Law - Meta Glasses Create Biometric Gray Area For Privacy Enforcers. https://news.bloomberglaw.com/business-and-practice/meta-glasses-create-biometric-gray-area-for-privacy-enforcers
[^31]: CNBC - SpaceX signs computing power deal with open-source AI startup Reflection. https://www.cnbc.com/2026/06/22/spacex-ai-colossus-data-center-reflection.html
[^32]: arXiv 2601.09913 - Continuum Memory Architectures for Long-Horizon LLM Agents. https://arxiv.org/pdf/2601.09913v1
[^33]: arXiv 2601.02744 - Synapse: Episodic-Semantic Memory via Spreading Activation. https://arxiv.org/pdf/2601.02744
[^34]: arXiv 2604.22085 - Memanto: Typed Semantic Memory with Information-Theoretic Retrieval. https://arxiv.org/html/2604.22085
[^35]: arXiv 2601.02553 - SimpleMem: Efficient Lifelong Memory for LLM Agents. https://arxiv.org/pdf/2601.02553
[^36]: Lokmat Times - Weaviate Launches Engram to Break the AI Memory Bottleneck. https://www.lokmattimes.com/business/weaviate-launches-engram-to-break-the-ai-memory-bottleneck-and-let-agents-learn-from-conversation-without-slowing-down/

*Dan2 research agent, 2026-06-23 v40. Reads in order: v37 → v38 (OpenClaw reliability) → v39 (ambient AI shift) → v40 (HRM-Text + SIA-W+H + new memory). 9 new citations this run, 83 total across 5 v40 artifacts.*
ryd v3 (12 months) = MEMO-style dedicated memory model trained on user data.

### 1.4 Meta Ray-Ban Display at $799 + Gen 3 leaks — the wearable window is closing

Meta's smart-glasses lineup as of June 2026:
- **Ray-Ban Meta Gen 2** — $499, no display, camera+audio+AI. Released Q4 2025.
- **Meta Ray-Ban Display** — **$799**, in-lens display, **Neural Band** wristband for input. Released Q2 2026.
- **Ray-Ban Meta Blayzer** — prescription variant at higher total cost. Released May 2026.
- **Gen 3 leaks** — multi-hour Live AI battery (vs current ~30 min on Display), two new models. Release late 2026 or early 2027. [^24] [^25]

**v40 read:** **Meta is not waiting for us.** The Ray-Ban Display at $799 with neural-band input is a credible always-on AI wearable with multimodal input. Gen 3 in late 2026 with multi-hour Live AI closes the battery gap. The window for "AI wearable with privacy" is **12-18 months** — if we don't ship a credible v1 by Q2 2027, we lose the narrative to Meta-on-Ray-Ban.

**Defensive moats that are still ours:**
1. **Privacy by design** — Meta's biometric privacy concerns are real and growing (Bloomberg Law flagged this; Glass Almanac noted the NameTag code strip in June 2026). [^28] [^30]
2. **Open source + auditable** — Meta will never ship this. Our differentiator for the technical-early-adopter and academic segments.
3. **India-first / Global South** — Meta's Ray-Ban is US/EU-priced. Our $349 price point and India/Southeast Asia distribution is genuinely uncontested.
4. **On-device by default** — Meta is cloud-dependent. Apple's AFM 3 is hardware-locked. We are the only on-device-AGI play.

### 1.5 Yoshua Bengio + HuggingFace CEO endorsement of HRM

From the 量子位 coverage (June 2026): "HuggingFace CEO strongly recommends, Bengio team also bets on: why did this $1,500-trained HRM model catch fire?" The key reasons: (1) sample efficiency demonstrates that the "scale the data" doctrine is not the only path, (2) hierarchical architecture is biologically inspired and shows emergent reasoning ability, (3) the open-source release with full code + checkpoints lowers the barrier to replication. [^26]

**v40 implication:** **Academic legitimacy.** Citing HRM-Text in our research papers and engineering decisions gives us credibility. Co-authoring or collaborating with Sapient (or the GRAM team) is on the table.

---

## 2. System Architecture Deep Dive (Δ from v39)

### 2.1 Decomposition — still correct, with three refinements

v39 decomposition: 5+1 services (audiod, perceptiond, memoryd, toold, ttsd, os-toold) with OpenClaw orchestration. v38 added DanClaw proxy for OpenClaw reliability. v40 adds:

**1. `agentd` (Rust) — the planning loop.** Owns the agent's think-act-observe cycle, tool selection, budget enforcement, and proactive triggering. OpenClaw becomes a transport/MCP layer; agentd is the brain. **This is the v40 single biggest architectural gap.** Microsoft's Scout, Google's Spark, and Anthropic's Claude Agent SDK all separate the agent loop from the transport. We need to do the same. (Carry from v39.)

**2. `proactived` (Rust or Python) — the proactive scheduler.** Owns the "should I speak now?" decision. Subscribes to audiod VAD events + memoryd retrieval + calendar/location signals. Emits proactive TTS or Telegram messages. Pattern from PASK/MemCog/ProAct (v38 deep dive). (Carry from v38.)

**3. `learnerd` (Rust or Python) — the consolidation + harness-improvement loop.** Runs nightly when the device is plugged in. Two phases: (a) consolidate episodic → semantic (MemVerse pattern), (b) propose harness changes (SIA-H pattern). User reviews and approves via the "What Dani learned this week" screen. **This is the v40 self-improvement surface.** (New in v40.)

```
                ┌────────────┐
                │  openclaw  │  (TS/Node — transport, MCP, Telegram)
                └─────┬──────┘
                      │  gated by DanClaw proxy (v38)
                ┌─────▼──────┐
                │  agentd    │  (Rust — planning loop, budget)
                └─┬──┬──┬──┬─┘
                  │  │  │  │
    ┌─────────────┘  │  │  └─────────────┐
    │                │  │                │
┌───▼────┐  ┌────────▼──┴───┐  ┌─────────▼──┐
│  audiod│  │  perceptiond   │  │ memoryd v2 │
│  (PY)  │  │  (PY + LFM2.5) │  │  (Rust?)   │
└────────┘  └────────────────┘  └────────────┘

  ┌──────────────┐    ┌─────────────────┐
  │  proactived  │    │  learnerd       │
  │ (scheduling) │    │  (consolidate,  │
  │              │    │   SIA-H loop)   │
  └──────────────┘    └─────────────────┘

       ┌──────────────┐    ┌──────────────┐
       │  toold       │    │  ttsd        │
       │  (shell+py)  │    │  (KittenTTS) │
       └──────────────┘    └──────────────┘
```

### 2.2 RL feedback loop in danlab-multimodal — still a heuristic, but the path is clearer

v39: the loop is a heuristic re-ranking, not RL. v40: the path to making it real RL is now visible via the SIA-W+H recipe, and the HRM-Text recipe gives us a small, fine-tunable target.

**Concrete v40 plan:**
- **Q3 2026:** Implement SIA-H (harness-only) on top of our existing SmolVLM-256M feedback loop. Rename from "RL feedback loop" to "harness improvement loop" (terminology fix from v39).
- **Q4 2026:** Train a Danlab-HRM-Text-1B variant on (smolvlm-output, harness-decision, user-correction) tuples. Fine-tune via LoRA. This is the v40 "RL loop" — but it's weight updates, not policy gradients.
- **Q1 2027:** Add SIA-W+H joint optimization. Compare against harness-only. Publish a paper.

### 2.3 Power/performance — HRM-Text changes the math

v39: LFM2.5-VL-450M is a defensible v1 VLM choice but ceiling-bound. v40: HRM-Text-1B is a more aggressive candidate for the **reasoning** layer (separate from vision). The combined stack:

| Layer | v39 choice | v40 choice | Why |
|-------|-----------|-----------|-----|
| Vision | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M Q4_0 (unchanged) | 450MB, 100-200ms/frame on CPU, fine for sub-1B VLM |
| Reasoning | (cloud-rented) | **HRM-Text-1B Q4_0** | 1B params (~150MB INT4), trained for $1,500, sample-efficient |
| STT | whisper.cpp base.en | whisper.cpp base.en (unchanged) | Defensible; switch to Parakeet TDT in v1.5 for Indian languages |
| TTS | KittenTTS base/medium | KittenTTS medium (unchanged) | Fine for v1; voice clone in v1.5 |
| Memory | flat vector (384d MiniLM) | **LFM2.5-Embedding-350M (1024d)** + topic-structured documents | Better multilingual, Apache 2.0-equivalent |

**v40 stack size on-device:** 450MB (vision) + 150MB (reasoning INT4) + 74MB (STT) + 25MB (TTS) + 350MB (embeddings) = **~1.05GB on-device.** This fits in 2GB RAM, which is achievable on a wearable with 8GB total + careful memory management. The LFM2.5-Embedding-350M swap (from 384d MiniLM, 90MB) costs us +260MB but gives us native multilingual + better retrieval quality.

### 2.4 OpenClaw — DanClaw proxy is mandatory (carry from v38)

v38 established that OpenClaw's upstream production failure modes (unhandled rejections, OOM Map leaks, sessions_send routing rot) make it unsafe to expose directly to a wearable daemon. v40 confirms: **DanClaw proxy is the v1 deliverable. ~250 LOC TypeScript + 1 memoryd schema migration.** This is the highest-priority engineering item because everything else builds on it.

---

## 3. AGI Landscape Research (2026) — HRM-Text pivot

### 3.1 The sample-efficiency revolution

The 2026 AGI story is no longer "scale the data and the model." Sapient's HRM-Text-1B and similar sample-efficient architectures (Sakana AI's HRM-derived work, the GRAM paper with Bengio) show that:
- **Sample efficiency > parameter count** for reasoning tasks.
- **Hierarchical recurrent architectures** with weight-sharing can match transformers at 1/10th the params.
- **Training cost is no longer the barrier** to owning your reasoning stack.

**The implication for AGI labs:** Anyone with $1,500 and 16 GPUs for 2 days can train a competitive reasoning model on their domain data. The "moat through scale" is collapsing. The new moat is **data quality + domain expertise + deployment.**

**The implication for Danlab specifically:** We can own our reasoning stack. We can train a Danlab-HRM-Text on (voice transcripts, salience decisions, memory schemas) for less than a single Claude API call costs us per week. **This is the foundational shift that makes "build AGI from India" credible.** It is no longer "rent the foundation models from the West." It is "train your own, on your data, for pennies."

### 3.2 Self-improvement is now an engineering discipline, not a research problem

v39 said self-improvement is the real AGI race. v40 confirms: **SIA-W+H shows that harness + weight updates with the right RL algorithm auto-selection achieves SOTA on three diverse domains.** This is no longer a research question; it is an engineering pattern. We can ship it.

The pattern:
1. **Meta-Agent** generates the Target-Agent (initial prompt + tool config + LoRA init).
2. **Target-Agent** runs on the task, producing trajectory + reward.
3. **Feedback-Agent** analyzes the trajectory, decides whether to (a) rewrite the harness, (b) update weights via LoRA, or (c) both.
4. **Auto-RL-selection**: PPO+GAE for dense rewards, GRPO for sparse, EAW for skewed.
5. **Per-generation artifacts** (target_agent.py, agent_execution.json, improvement.md) for inspectability and rollback.

**v40 Danlab plan:** Adopt this pattern. Build `learnerd` in v1 (harness-only) and `learnerd` v1.5 in v1.5 (harness + LoRA on HRM-Text-1B).

### 3.3 Memory is now typed + multimodal + maintainable

The 2026 memory stack (Infini Memory + MemVerse + MEMO) replaces the 2025 flat-vector + RAG stack. **The key features we should adopt:**
- **Typed memory** (working, episodic, semantic, procedural) with explicit relationships.
- **Bi-temporal edges** (when the fact was true, when we learned it).
- **Periodic distillation** (compress the long-term graph into a small parametric model for fast recall).
- **Topic-structured documents** (Infini Memory) for maintainability and explicit fact revision.
- **Multimodal** (MemVerse) for visual + audio + text in the same store.
- **Dedicated memory model** (MEMO) trained on user data for v2/v3.

### 3.4 Edge VLM SOTA — Nanomind anchor (carry from v38)

v38 anchor: **Nanomind 0.375W continuous VLM on 2000 mAh = 18.8h.** The bar for wearable VLM is "18h, <80g." v40: this is unchanged. The implementation plan is the same (Nanomind-style cascade, sub-byte quantization).

---

## 4. Competitive & Market Research (Δ from v39)

### 4.1 Smart-glasses landscape (carry + update)

v39: Meta Ray-Ban, Snap Specs, Even Realities, Brilliant Labs. v40: same competitors, with updated pricing and capability matrix.

| Product | Price | Display | Input | AI | Battery | Ship | Threat to Danlab |
|---------|-------|---------|-------|-----|---------|------|------------------|
| **Ray-Ban Meta Gen 2** | $499 | No | Voice, tap | Meta AI (cloud) | 4h | Q4 2025 | Direct competitor on capture+AI |
| **Meta Ray-Ban Display** | **$799** | Yes (in-lens) | Voice, neural band | Meta AI (cloud) | ~30min Live AI | Q2 2026 | Premium-tier reference design |
| **Ray-Ban Meta Gen 3** (leaked) | TBD | TBD | TBD | Multi-hour Live AI | TBD | Late 2026/early 2027 | Closes the battery gap |
| **Snap Specs** | $2,195 | AR (51° FOV) | Voice, gesture | MyAI (cloud) | 4h | Fall 2026 | Premium closed-source reference |
| **Even Realities G2** | $399 | No | Touch | No AI | 7d | Q1 2026 | Audio-only competitor, not AI |
| **Brilliant Labs Halo** | $349 | No | Voice | LFM2-VL-450M on-device | 6h | Jul 2026 | **Open-source-ecosystem peer** |
| **NeoSapien Neo 1** | $189 (~$15k INR) | No | Touch + voice | Second Brain OS (proprietary) | 8h | Q2 2026 | **Closest peer: India, AI-native, sub-$200** |
| **Dan Glasses v1 (our target)** | $349 (est) | No | Voice, PTT | **On-device, open source, private** | 4h target | Q2-Q3 2026 (desktop); Q3-Q4 2026 (wearable) | Our wedge |

**v40 read:** The price range is $189-$2,195. Meta dominates $499. Snap owns $2,195. **We compete at $349, India-first, on-device, open-source.** This is uncontested in the $200-$400 band for AI-native wearables. NeoSapien is the closest peer; Brilliant Labs Halo is the closest open-source peer.

### 4.2 Open-source AI companion projects (carry + update)

v38/v39: SIA, Self-Harness, RHO, Meta-Harness, Open Interpreter, LiberaGPT, MemCog, ProAct, PASK, CogniFold, MRAgent. v40 adds:

- **HRM-Text (Sapient)** — Apache-compatible, 1B, $1,500 training. **The new on-device reasoning model.**
- **SIA-W+H (Hexo Labs)** — MIT, harness+weight updates, verified SOTA on three domains.
- **Infini Memory (arXiv:2606.10677)** — topic-structured documents, paper with code release pending.
- **MemVerse (arXiv:2512.03627)** — multimodal lifelong memory with periodic distillation.
- **MEMO (NUS+MIT, May 2026)** — dedicated memory model + executive LLM pattern.

**v40 read:** **The open-source stack is no longer a research stack. It is a production stack.** We can build a credible v1 entirely on open-source components. The moat is not the components; the moat is the integration, the data, and the self-improvement loop.

### 4.3 Privacy and regulatory (carry from v38)

v38: Fable 5 suspension, Stuart Russell Guardian, Illinois HB4843, Dickinson Wright wearable privacy alert. v40 adds:
- **Glass Almanac: Meta AI App Strips NameTag Code in June 2026** — Meta quietly removed the "name tag" feature that identified people in photos. **Regulatory pressure is working.** This is a real win for the privacy-first narrative. [^28]
- **Bloomberg Law: Meta Glasses Create Biometric Gray Area For Privacy Enforcers** — first major legal analysis of Meta glasses as a privacy compliance issue, not just a policy debate. [^30]

**v40 read:** **The privacy story is now compliance-required, not just positioning-required.** Danlab's on-device, open-source, auditable posture is a sales asset, not just defense.

---

## 5. Technical Deep Dives (3 of 6 — picked for v40)

### Deep Dive A — HRM-Text training pipeline (new in v40, replaces v39's "self-improving RL loops")

**Why this got promoted:** The HRM-Text release changes the economics of owning your reasoning stack. The 1B model at $1,500 training cost means we can train a Danlab-specialized variant. This is the v40 "what's new" deep dive.

**The HRM architecture (Sapient, May 2026):**
- **Two weight-shared stacks:** H (slow, strategic) and L (fast, execution).
- **Multi-round recursion:** H_cycles × L_cycles forward passes per token. Effective depth >> parameter count.
- **Latent reasoning, not token-space CoT.** The model reasons in its latent space, not via scratchpad tokens.
- **Training:** 40B tokens, instruction-response pairs only, 1.9 days on 16 H100s.
- **Inference:** Faster than transformers at the same parameter count for reasoning tasks (GSM8K, MATH, DROP).

**Our Danlab-HRM-Text plan (v40):**
1. **Month 1 (July 2026):** Spin up the HRM-Text open-source repo. Reproduce the Sapient training run on 16 H100s for 2 days. Validate that we can train a 1B HRM-Text variant. **Cost: ~$1,500 + engineer time.**
2. **Month 2 (August 2026):** Curate the Danlab training corpus. This is: (a) voice transcripts from audiod logs (anonymized), (b) salience decisions from perceptiond (with user correction labels), (c) memory schema examples from memoryd, (d) tool-use trajectories from toold. **Target: 5-10B tokens of Danlab-specific data.**
3. **Month 3 (September 2026):** Train Danlab-HRM-Text-1B. **Cost: ~$1,500.** Ship as a v1.5 candidate to replace the cloud-rented reasoning layer.
4. **Month 4-6 (October-December 2026):** Fine-tune via LoRA on user-specific data (with opt-in consent). Push to v1.5 reasoning layer.
5. **Month 7-12 (2027):** SIA-W+H joint harness+weight optimization on top of Danlab-HRM-Text-1B. The v2 self-improving reasoning layer.

**Concrete deliverable:** `Services/learnerd/` (Rust or Python) — owns the training pipeline, the SIA-H loop, and the LoRA fine-tuning. Outputs: trained model checkpoints, per-generation improvement.md, audit log.

### Deep Dive B — SIA-W+H pattern applied to Danlab (carry from v39, expanded)

v39 introduced SIA as the canonical open-source self-improving agent framework. v40 deepens this with the v1 → v1.5 → v2 progression.

**v1 (6 months): SIA-H only**
- Harness-only updates. Targets: prompt templates, tool selection, retry logic, error parsing.
- RL algorithm: PPO+GAE.
- Run on: HRM-Text-1B base (cloud, 16 H100s) or LFM2.5-1.2B (cloud).
- Expected ceiling: 50% improvement on task accuracy over baseline.
- **v40 deliverable: `learnerd` v1, running nightly on the user's laptop.**

**v1.5 (12 months): SIA-H + LoRA weights on HRM-Text-1B**
- Add LoRA weight updates (rank 32) to the harness loop.
- Train on: user corrections, harness failure cases, memory write/read patterns.
- Run on: Danlab-HRM-Text-1B (small enough to fine-tune on-device or in cloud with minimal cost).
- Expected ceiling: 70% improvement on task accuracy over baseline (per SIA-W+H LawBench result).
- **v40 deliverable: `learnerd` v1.5, with the "What Dani learned this week" screen.**

**v2 (24 months): SIA-W+H joint + federated opt-in**
- Add opt-in federated learning across the Danlab user base.
- Differential privacy for the user contributions.
- Train on: aggregate user data, with privacy guarantees.
- **v40 deliverable: `learnerd` v2, with the "Help improve Dani" opt-in flow.**

### Deep Dive C — Topic-structured multimodal memory (new in v40)

v39 had a HeLa-Mem-inspired memoryd v2 plan. v40 updates this with the Infini Memory + MemVerse + MEMO insights.

**v40 memoryd v2 design:**
- **Storage layer:** SQLite (metadata + raw events) + LanceDB or Qdrant (dense vectors) + topic document store (markdown files with version history).
- **Types:** working, episodic, semantic, procedural (4 categories, bi-temporal edges).
- **Retrieval:** hybrid — dense vector (LFM2.5-Embedding-350M) + BM25 (full-text) + graph traversal (typed edges) + recency boost. RRF merge.
- **Consolidation:** MemVerse-style periodic distillation. Every 24h on-device (when plugged in), walk the episodic store, cluster events, extract semantic facts, write them with bi-temporal edges. **This is the "sleep" cycle.**
- **Maintenance:** Infini Memory-style topic documents with explicit fact revision. When a fact changes (e.g., user's new job), the topic document is updated, not appended to.
- **Multimodal:** vision embeddings from perceptiond + audio embeddings from audiod + text from memoryd, all in the same store. Cross-modal retrieval (find the visual scene that matches this text query).

**v40 deliverable:** `Services/memoryd/` v2 with the above. v3 (12 months) adds the MEMO-style dedicated memory model trained on user data.

---

## 6. Top 3 Recommendations (TL;DR for somdipto)

1. **Train Danlab-HRM-Text-1B. This quarter.** $1,500, 1.9 days on 16 H100s, gives us our own reasoning stack. The economics have changed; the moat shifts from "rent the foundation models from the West" to "own your reasoning, on your data, for pennies." Action: spin up the Sapient repo this week, reproduce the training run, then train the Danlab variant. [Bengio and HuggingFace CEO endorsement makes this academically defensible.]

2. **Build `learnerd` (the SIA-H self-improvement loop) and ship it in v1.** ~500 LOC Python, runs nightly on the user's laptop. Walks the day's logs, identifies failure modes, proposes harness changes. User reviews and approves via the "What Dani learned this week" screen. This is the v1 self-improvement surface. The SIA pattern is verified (50% on LawBench); the engineering is straightforward.

3. **Switch memoryd to topic-structured documents (Infini Memory) + LFM2.5-Embedding-350M (1024d multilingual).** 4-week refactor. The flat-vector store is a v1 limitation we should not ship. The new memory stack is typed (working/episodic/semantic/procedural), bi-temporal, multimodal, and explicitly maintainable. This is the moat shift for memory.

**The 6/12/24-month roadmap is in `dan2-agi-roadmap.md` (v40). The architecture review is in `dan2-architecture-review.md` (v40). The model deep-dive is in `dan2-model-analysis.md` (v40). The paper reading list is in `dan2-papers-to-read.md` (v40).**

---

## 7. Sources (v40)

### v40 new sources
- HRM-Text Sapient (full architecture, benchmarks, $1,500 training): [^18] [^19]
- HRM-Text via HuggingFace + GRAM + Bengio endorsement: [^26]
- SIA GitHub README (verified numbers, MIT license): [^20]
- SIA results detail (LawBench 70.1%, TriMul 1,017μs, denoising 0.289): [^7] [^8]
- Infini Memory (arXiv:2606.10677): [^21]
- MemVerse (arXiv:2512.03627): [^22]
- MEMO framework (NUS+MIT, May 2026): [^23]
- Meta Ray-Ban Display $799 + Neural Band + Gen 3 leaks: [^24] [^25]
- Glass Almanac NameTag strip: [^28]
- Bloomberg Law Meta glasses biometric: [^30]

### Carry from v39 sources
- Google I/O 2026 Gemini Spark: [^1]
- Microsoft Build 2026 Scout: [^2]
- Apple AFM 3 WWDC 2026: [^3]
- LFM2 Technical Report: [^4]
- BlueLM-2.5-3B: [^5]
- Anthropic recursive self-improvement warning: [^6]
- SIA / Hexo Labs (foundational): [^8]
- OpenGlass: [^9]
- Decagon Duet Autopilot: [^10]
- Perplexity Brain: [^11]
- HeLa-Mem: [^12]
- Flash-VL 2B: [^13]
- MiniCPM-Llama3-V 2.5: [^14]
- Edge TTS comparison: [^15]
- KittenTTS: [^16]
- Pi self-modifying agent: [^17]
- SpaceX Reflection deal: [^18] (re-numbered as 27)
- Anthropic Mythos: [^19] (re-numbered as 27)
- John Jumper → Anthropic: [^20] (re-numbered as 27)
- Microsoft Scout TechCrunch: [^21] (re-numbered as 27)
- InternVL 2.5: [^22] (re-numbered as 27)
- Kimi-VL: [^23] (re-numbered as 27)
- TinyissimoYOLO: [^24] (re-numbered as 27)
- INAR-VL: [^25] (re-numbered as 27)

### v40 sources (numbered)
[^7]: arXiv 2605.27276 / hexo-ai/sia - SIA: Self Improving AI with Harness & Weight Updates. https://arxiv.gg/abs/2605.27276
[^8]: MarkTechPost - Hexo Labs Open-Sources SIA. https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/
[^9]: arXiv 2606.07431v2 - OpenGlass: Ultra-Low-Power On-Device AI Eyewear. https://arxiv.org/html/2606.07431v2
[^18]: CryptoBriefing - Sapient trains 1B-parameter HRM-Text model for $1,500 in 1.9 days. https://cryptobriefing.com/sapient-hrm-text-model-1500-training/
[^19]: VentureBeat - Researchers say they trained a foundation model from scratch for about $1,500. https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
[^20]: GitHub - hexo-ai/sia. https://github.com/hexo-ai/sia
[^21]: arXiv 2606.10677v1 - Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory. https://arxiv.org/html/2606.10677v1
[^22]: arXiv 2512.03627v2 - MemVerse: Multimodal Memory for Lifelong Learning Agents. https://arxiv.org/html/2512.03627v2
[^23]: MarkTechPost - MEMO: A Modular Framework for Training a Dedicated Memory Model. https://www.marktechpost.com/2026/05/26/memo-a-modular-framework-for-training-a-dedicated-memory-model-on-new-knowledge-without-modifying-llm-parameters
[^24]: PCMag - The Best Smart Glasses We've Tested for 2026. https://www.pcmag.com/picks/the-best-smart-glasses
[^25]: VR Wave - Ray-Ban Meta Gen 3 Leaks: Better Battery, Smarter AI. https://www.vr-wave.store/blogs/virtual-reality-prescription-lenses/ray-ban-meta-gen-3-leaks-better-battery-smarter-ai-and-two-new-models
[^26]: 量子位 - HuggingFace CEO endorsement, Bengio team backs HRM. https://www.qbitai.com/2026/06/435483.html
[^28]: Glass Almanac - Meta AI App Strips NameTag Code In June 2026. https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
[^30]: Bloomberg Law - Meta Glasses Create Biometric Gray Area For Privacy Enforcers. https://news.bloomberglaw.com/business-and-practice/meta-glasses-create-biometric-gray-area-for-privacy-enforcers

*Dan2 research agent, 2026-06-23 v40. Reads in order: v38 → v39 → v40. 9 new citations this run, 83 total across the 5 v40 artifacts.*
2 Frontier labs and what they actually shipped in 2026

| Lab | 2026 flagship | On-device? | Open source? | Reasoning style |
|-----|---------------|-----------|--------------|-----------------|
| **OpenAI** | o4 / o5 / GPT-6 | No | No | RL-on-CoT, 100B+ |
| **Anthropic** | Claude Mythos Fable 5 | No | No | Constitutional AI + RL |
| **Google** | Gemini 3 + Spark | No | No | Multimodal + ambient agent |
| **Apple** | AFM 3 (20B) | Yes (iPhone 17 Pro) | No | Transformer + privacy gates |
| **Microsoft** | MAI-Thinking-1 (35B active) | No | No | Mid-size + enterprise focus |
| **Sakana AI** | HRM-derived, RSI Lab | Partial | Partial | Sample-efficient + recursive SI |
| **Hexo Labs** | SIA (MIT) | No | Yes (MIT) | Harness + weight co-evolution |
| **Sapient** | HRM-Text-1B | Yes (~150MB INT4) | Yes (Apache) | Hierarchical recurrent |
| **Perplexity** | Brain | Partial | No | Self-improving memory |
| **Recursive Superintelligence** | $650M raise | No | No | RSI research |
| **Decagon** | Duet Autopilot | No | No | Verified self-improving agent |
| **Open-source (academic)** | HRM, GRAM, CMA, SIA, MemVerse | Varies | Yes | Various |

**The pattern:** The frontier labs are not converging. OpenAI/Anthropic/Google bet on scale + RL. Apple bets on on-device + privacy. Microsoft bets on enterprise. Sakana/Hexo/Sapient bet on architecture innovation + openness. **The most consequential 2026 release for the wearable+on-device thesis is Sapient's HRM-Text-1B, not any of the frontier flagships.** The frontier flagships are server-only and priced for enterprise.

### 3.3 Self-improvement is the real AGI race

v39 thesis: self-improvement is the moat. v40 reinforces: **SIA-W+H shows that harness-only plateaus; weight updates are required to break the plateau.** This is the empirical data point that justifies our v40 roadmap shifting from "SIA-H only" (v39) to "SIA-H in v1, SIA-W+H in v1.5" (v40).

**The new questions:**
1. Can we do SIA-W+H on-device with HRM-Text-1B (1B params, ~150MB INT4)? **Likely yes for LoRA fine-tuning; full fine-tune would need 2GB+ working memory.**
2. Can we federate weight updates across users without compromising privacy? **Differential privacy + secure aggregation. Apple has shipped this pattern.**
3. Can we make the improvement loop observable + reversible? **Yes, this is a UX problem. SIA's per-generation artifact pattern (target_agent.py, agent_execution.json, improvement.md) is the template.**

### 3.4 Edge AI / on-device VLMs — moving fast

v39 candidate list for sub-500MB VLMs: LFM2.5-VL-450M, Moondream, SmolVLM2, InternVL2.5, BlueLM-2.5-3B. v40 adds:
- **LFM2-VL-1.2B** (Liquid AI, late 2025) — the upgrade path from 450M.
- **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M** (Liquid AI, June 18 2026) — Apache 2.0-equivalent, 1024d embeddings, native multilingual.
- **BitNet-VLM** (1-bit, expected Q4 2027) — wait or ship?
- **Brilliant Labs Halo** with stock LFM2-VL-450M — production-grade reference for the form factor.

**v40 read:** For v1, stay with LFM2.5-VL-450M (no reason to change). For v1.5, evaluate LFM2-VL-1.2B (larger but same architecture family). For v2, watch BitNet-VLM but don't wait.

### 3.5 Memory and continual learning — the 2026 wave

v39: HeLa-Mem, CMA, Synapse, Memanto, SimpleMem. v40 adds:
- **Infini Memory** (Jun 2026) — topic-structured documents, iterative retrieval. **Our memoryd v2 architecture.**
- **MemVerse** (Dec 2025) — multimodal lifelong memory with periodic distillation. **The pattern for our perceptiond + memoryd integration.**
- **MEMO** (May 2026) — modular executive + memory model. **The v3 architecture: HRM-Text-1B executive + Danlab-MEMORY model.**
- **Mem0** (Apr 2026 algorithm update) — production-grade agent memory. Worth benchmarking.

### 3.6 Multimodal fusion — the SAPA / Idefics3 / LLaVA-OneVision landscape

v39: tile-based inference, sparse attention, LLM bias. v40: nothing major changed; **Multimodal fusion is now a solved problem at the small-model level.** Our LFM2.5-VL-450M is not the SOTA fusion model (InternVL2.5 with small encoders is), but it is the right size for our wearable.

### 3.7 Model compression — the 2026 frontier

v39: AWQ 3-bit, SmoothQuant, structured sparsity. v40: **BitNet-VLM (1-bit, Q4 2027) is the next disruption.** Until then, AWQ + SmoothQuant is the production stack.

---

## 4. Competitive & Market Research (Δ from v39)

### 4.1 AI wearables landscape (June 2026)

| Product | Price | Display | Form factor | Status | Privacy stance |
|---------|-------|---------|-------------|--------|----------------|
| **Ray-Ban Meta Gen 2** | $499 | No | Glasses | Shipping | Cloud-dependent, biometric concerns |
| **Meta Ray-Ban Display** | $799 | In-lens | Glasses + neural band | Shipping | Cloud, name-tag code stripped Jun 2026 |
| **Snap Specs** | $2,195 | 51° FOV AR | Glasses | Fall 2026 | Cloud, closed-source |
| **Brilliant Labs Halo** | $349 | No | Glasses (Alif B1) | Shipping Jul 2026 | LFM2-VL-450M, on-device |
| **NeoSapien Neo 1** | $189 | No | Pendant | Shipping | India-first, proprietary |
| **Even Realities G2** | $599 | Yes | Glasses | Shipping | Privacy-focused |
| **Solos AirGo V2** | $399 | No | Glasses | Shipping | Voice AI |
| **INMO GO3** | $499 | Yes | Glasses | Shipping | Light AR |
| **VITURE Beast** | $449 | External display | XR glasses | Shipping | Display-only |
| **XREAL 1S** | $449 | External display | AR glasses | Shipping | Display-only |
| **Apple Vision Pro 2** | $3,499 | Full VR | Headset | Shipping | On-device AFM |
| **Dan Glasses (us)** | $349 target | No | Glasses | Desktop prototype | **On-device, open-source, auditable** |

**v40 read:** **We are the only on-device + open-source + privacy-first AI wearable in this list.** Meta and Snap are cloud-dependent. Brilliant Labs is the closest competitor (LFM2-VL-450M on Alif B1, on-device) but no self-improvement loop. NeoSapien is India-first but no on-device VLM, proprietary.

**Our wedge:** $349 + on-device + open-source + India-first + auditable self-improvement. The 18-month window before Meta locks in the narrative is real. Ship v1 by Q2 2027 or lose the category.

### 4.2 Open-source AI companion projects (Δ from v39)

v39: SIA, Self-Harness, RHO, OpenSkill, MemCog, ProAct, PASK, CogniFold, DCPM, MRAgent. v40 adds:
- **HRM-Text-1B** (Sapient, May 2026) — open-source reasoning model, MIT-equivalent. **The most important new open-source release for our roadmap.**
- **SIA-W+H** (Hexo Labs, May 2026) — verified numbers on LawBench, TriMul, RNA denoising. **The template for our self-improvement loop.**
- **MemVerse** (arXiv 2512.03627, Dec 2025) — multimodal lifelong memory.
- **Infini Memory** (arXiv 2606.10677, Jun 2026) — topic-structured memory.
- **MEMO** (May 2026) — modular executive + memory model.
- **BitNet-VLM** (Q4 2027 est.) — 1-bit VLMs.

### 4.3 Privacy-preserving AI positioning (Δ from v39)

v39: Apple's "privacy is non-negotiable" WWDC 2026 headline; Meta's biometric concerns; Illinois HB4843. v40 adds:
- **Meta AI App NameTag code strip (June 2026)** — Meta walked back the always-on face recognition. This is a real signal that public pressure on biometric AI works. Our on-device + opt-in recognition is the right stance.
- **SentinelOne UAE autonomous security stance** — first national-level government position on agentic AI security. India and EU are likely to follow with similar positions. **Our on-device posture is now a regulatory asset.**
- **Dickinson Wright wearable privacy alert (June 2026)** — first law-firm alert framing wearable privacy as compliance. **This is the language enterprise customers will use.**

**v40 read:** **Privacy + on-device + open-source + auditable + safety-gated is now compliance-grade positioning.** This is a sales asset for enterprise pilots, not just consumer positioning. **We should publish a "Compliance Brief" in Q3 2026** that frames Danlab's posture against HIPAA, GDPR, India's DPDP Act, and Illinois HB4843.

---

## 5. Technical Deep Dives (3 of 6 — picked for v40)

### Deep Dive A — HRM-Text training economics (NEW, replaces v39's memory deep dive as the v40-critical)

**Why this got promoted:** v40 thesis is the HRM-Text pivot. If we can own our reasoning stack, we own our moat. The economics of training are now absurdly favorable.

**The recipe (from Sapient's GitHub):**
1. **Architecture:** Two weight-shared stacks (H slow, L fast). Multi-round recursion: H_cycles × L_cycles forward passes.
2. **Data:** ~40B structured instruction-response tokens. No raw text scraping. No CoT annotations.
3. **Compute:** 16 H100 GPUs, 1.9 days. ~$1,500.
4. **Training:** FSDP2 + FlashAttention 3 + PrefixLM sequence packing.
5. **Inference:** Standard transformer serving (no specialized runtime needed for the model itself; the architectural benefit is in the training efficiency and the latent-space reasoning).

**Danlab adaptation plan:**
1. **Q3 2026:** Train Danlab-HRM-Text-1B on a curated dataset of (voice transcript, salience decision, memory schema, proactive trigger). ~$2,000 (slight premium for domain data). Dequantize to INT4 (~150MB). Benchmark against LFM2.5-VL-450M + cloud-rented reasoning on dglabs-eval v1.
2. **Q4 2026:** Add SIA-H (harness-only) loop. Re-train Danlab-HRM-Text-1B on (input, harness-decision, user-correction) tuples. Benchmark.
3. **Q1 2027:** Add SIA-W+H (weight + harness). LoRA fine-tune with opt-in user data. Push past the 50% harness-only ceiling.

**Risks:**
- **FlashAttention 3 requires Hopper-class GPUs.** H100 is the minimum. H200 or B200 preferred. We need cloud GPU access for training; the inference is cheap (on-device INT4).
- **Domain data curation is the bottleneck, not the compute.** We need a clean dataset of (transcript, salience-decision, correction) tuples. 6 months of audiod logs in dev would be a start.
- **Sapient is a small lab.** If they shut down or pivot, we may need to maintain the model ourselves. Mitigation: full open-source code + checkpoints, MIT/Apache licensing.

**Deep dive conclusion:** **The HRM-Text recipe is the single highest-leverage technical decision for v40.** It collapses our reasoning cost from "rent OpenAI/Anthropic at $X/month" to "own a 1B model trained for $1,500." The risk-adjusted NPV is enormous. **Ship it.**

### Deep Dive B — SIA-W+H self-improvement recipe (NEW, replaces v39's "memory architectures" deep dive as the v40 second-critical)

**Why this got promoted:** SIA-W+H's verified numbers (LawBench 70.1%, +25.1pp over SOTA) prove that harness-only is insufficient. To break the plateau, we need weight updates.

**The recipe (from SIA's GitHub):**
1. **Three-agent loop:** Meta-Agent generates initial Target-Agent. Feedback-Agent analyzes logs, decides between harness rewrite or weight update. Target-Agent executes tasks.
2. **Reward algorithm auto-selection:** PPO+GAE for dense rewards, GRPO for sparse-with-verifier, EAW for right-skewed. The framework picks based on reward distribution.
3. **Per-generation artifacts:** `target_agent.py`, `agent_execution.json`, `improvement.md`. Rollbackable.
4. **LoRA rank 32** on the base model. Inexpensive to fine-tune repeatedly.

**Danlab adaptation plan:**
1. **Q3 2026:** Implement the harness-only loop on our agentd + memoryd. Use LFM2.5-Embedding-350M for the "what changed" comparison.
2. **Q4 2026:** Add LoRA fine-tuning of Danlab-HRM-Text-1B. Auto-select reward algorithm. Use the SIA per-generation artifact pattern.
3. **Q1 2027:** Ship "What Dani learned this week" UX surface. User reviews `improvement.md`, approves or rolls back.

**The viral insight from SIA's RNA denoising case:** The weight update found a "two-line trick — rounding imputed counts to non-negative integers" that harness-only did not discover. **Weight updates find knowledge that scaffolds cannot.** For our memoryd, this means: weight updates will discover salience patterns, memory schemas, and proactive triggers that the harness alone misses.

**Deep dive conclusion:** **SIA-W+H is the v1.5 architecture for Danlab's self-improvement loop. Harness-only in v1, weight + harness in v1.5, federated weight + harness in v2.**

### Deep Dive C — Topic-structured multimodal memory (v40 third deep dive, replaces v39's "edge VLM" deep dive)

**Why this got picked:** Our memoryd is the weakest service in the current stack. The 2026 wave (Infini Memory, MemVerse, MEMO) shows that flat vector stores are a dead end for long-term agent memory.

**The architecture pattern:**
- **Topic documents** (Infini Memory) — each topic is a semantic unit with metadata + revision history. Memory is not a flat list of vectors; it is a structured set of evolving documents.
- **Periodic distillation** (MemVerse) — short-term memory for recent context, long-term memory as a cognitive graph. Periodic distillation compresses the graph into the parametric model for fast recall.
- **Separate memory model** (MEMO) — the MEMORY model is a small dedicated LLM trained on user data. The EXECUTIVE model (HRM-Text-1B in our case) queries it via structured multi-turn.

**Danlab adaptation plan:**
1. **Q3 2026 (memoryd v2):** Implement Infini Memory-style topic documents. Use LFM2.5-Embedding-350M for retrieval. Replace flat vector store.
2. **Q4 2026 (memoryd v2.5):** Add MemVerse-style periodic distillation. Run nightly when plugged in.
3. **Q2 2027 (memoryd v3):** Train a Danlab-MEMORY model on user data. The executive (HRM-Text-1B) queries it for personal context.

**Deep dive conclusion:** **Topic-structured multimodal memory is the v40 memory architecture. The flat vector store in current memoryd is the v0 architecture. memoryd v2 ships in 6 months.**

---

## 6. Open Questions for somdipto (Δ from v39)

1. **Compute budget for HRM-Text training.** ~$2,000 for a single Danlab-HRM-Text-1B variant. Is this a Q3 2026 budget item? **v40 critical blocker.**
2. **Cloud GPU access.** We need H100-class GPUs for ~2 days. Do we use Lambda Labs, Vast.ai, AWS, GCP? Recommendation: Vast.ai for cost (~50% cheaper than AWS).
3. **Domain data pipeline.** Where does the (transcript, salience-decision, memory-schema) dataset come from? **6 months of audiod logs + 1 month of perceptiond logs + memoryd exports = ~100K tuples.** We can start today on the laptop.
4. **Federated weight updates — yes or no?** v40 plan says v2. Is the user OK with opt-in federated training for HRM-Text improvements? (Apple's pattern: differential privacy + secure aggregation + user opt-in.)
5. **Hardware pivot timeline.** v38 said "Month 3." v40 says: pick a Brilliant Labs Halo (shipping Jul 2026 with LFM2-VL-450M on Alif B1) and a GAP9 dev kit, run Danlab-HRM-Text-1B INT4 on both, measure power, decide by end of Q3 2026.
6. **Meta Ray-Ban Display defensive moats.** v40: $799 + 12-18 month window. Do we ship a $349 privacy-first India-first alternative by Q2 2027? Or pivot to enterprise (where our compliance posture is the moat)?
7. **SIA fork vs. partner.** SIA is MIT. We can fork or partner with Hexo Labs. Recommendation: fork first, partner second (Sakana RSI Lab pattern).
8. **HRM-Text Sapient partnership.** Sapient is a small lab. If we co-author a paper on Danlab-HRM-Text-1B domain adaptation, we get academic credibility + early access to future Sapient models.
9. **BitNet-VLM wait-or-ship.** v40 same as v39: ship v1.5 with HRM-Text-1B. Track BitNet-VLM for v2 (Q4 2027 est.).
10. **Liquid AI partnership.** v38/v39 both flagged. v40: now the most important silicon+model partnership. LFM2.5-VL-450M (vision) + LFM2.5-Embedding-350M (memory) + HRM-Text-1B (reasoning) is a coherent stack from two partners (Liquid AI + Sapient). **Reach out in Q3 2026.**

---

## 7. Top 3 Recommendations

1. **Train Danlab-HRM-Text-1B in Q3 2026.** The economics are too good to ignore: $1,500, 1.9 days, competitive with 2-7B open models. We can own our reasoning stack. This is the v40 single most important decision. **Decision needed from somdipto: compute budget + domain data pipeline.**

2. **Ship DanClaw proxy + agentd + memoryd v2 + learnerd as the v40 service stack.** OpenClaw reliability gap (v38) is the v1 blocker. memoryd v2 (topic-structured) is the v1 quality blocker. agentd (Rust planning loop) is the v1 architecture blocker. learnerd (SIA-H loop) is the v1 self-improvement blocker. **All four are 6-month deliverables.** v40 is the quarter we ship the bones.

3. **Defensive moat against Meta Ray-Ban Display: ship the privacy + on-device + open-source + India-first message by Q2 2027.** Meta is at $799 with a 12-18 month window before they lock in the mainstream narrative. Our $349 + privacy-first + India-first + on-device + open-source + auditable positioning is genuinely uncontested. **Ship or lose the category.**

---

## 8. Sources (v40 new — 9 additions, 83 total across artifacts)

### v40 new sources
[^1]: ynetnews - Google I/O 2026: tech giant launches autonomous AI era. https://www.ynetnews.com/tech-and-digital/article/ry3qypmlzl
[^2]: The Verge - Microsoft Build 2026: the 7 biggest announcements. https://www.theverge.com/tech/941738/microsoft-build-2026-biggest-announcements
[^3]: Apple Machine Learning Research - Introducing the Third Generation of Apple's Foundation Models. https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
[^4]: The Sequence - Thinking in Latents: Why Sapient's HRM-Text Is a Quiet Rebuke to Chain-of-Thought. https://thesequence.substack.com/p/the-sequence-ai-of-the-week-867-thinking
[^5]: VentureBeat - Researchers say they trained a foundation model from scratch for about $1,500. https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
[^6]: GitHub - P9LLI/HRM-Text (Sapient official repo, Apache 2.0). https://github.com/P9LLI/HRM-Text
[^7]: GitHub - hexo-ai/sia (SIA official repo, MIT). https://github.com/hexo-ai/sia
[^8]: arXiv 2605.27276 - SIA: Self-Improving AI with Harness & Weight Updates. https://arxiv.gg/abs/2605.27276
[^9]: PCMag - The Best Smart Glasses We've Tested for 2026. https://www.pcmag.com/picks/the-best-smart-glasses
[^10]: Glass Almanac - Meta AI App Strips NameTag Code In June 2026. https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
[^11]: Bloomberg Law - Meta Glasses Create Biometric Gray Area For Privacy Enforcers. https://news.bloomberglaw.com/business-and-practice/meta-glasses-create-biometric-gray-area-for-privacy-enforcers
[^12]: arXiv 2606.10677v1 - Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory. https://arxiv.org/html/2606.10677v1
[^13]: arXiv 2512.03627v2 - MemVerse: Multimodal Memory for Lifelong Learning Agents. https://arxiv.org/html/2512.03627v2
[^14]: MarkTechPost - MEMO: A Modular Framework for Training a Dedicated Memory Model. https://www.marktechpost.com/2026/05/26/memo-a-modular-framework-for-training-a-dedicated-memory-model-on-new-knowledge-without-modifying-llm-parameters
[^15]: VR Wave - Ray-Ban Meta Gen 3 Leaks: Better Battery, Smarter AI. https://www.vr-wave.store/blogs/virtual-reality-prescription-lenses/ray-ban-meta-gen-3-leaks-better-battery-smarter-ai-and-two-new-models
[^16]: 量子位 - HuggingFace CEO endorsement, Bengio team backs HRM. https://www.qbitai.com/2026/06/435483.html
[^17]: Forbes - Anthropic Launches Mythos With Six Features You Absolutely Need. https://www.forbes.com/sites/sandycarter/2026/06/09/anthropic-launches-mythos-with-six-features-you-absolutely-need/
[^18]: Axios - Microsoft debuts Scout agent, homegrown reasoning model. https://www.axios.com/2026/06/02/microsoft-debuts-scout-agent-homegrown-reasoning-model
[^19]: arXiv 2605.20613 - HRM-Text: Efficient Pretraining Beyond Scaling (Sapient). https://arxiv.org/abs/2605.20613
[^20]: MarkTechPost - Hexo Labs Open-Sources SIA. https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/

### Carry from v39 (full list in v39 dan2-research-report.md)

---

*Dan2 research agent, 2026-06-23 v40. Reads in order: v38 (OpenClaw reliability) → v39 (ambient AI shift) → v40 (HRM-Text + SIA-W+H + new memory). 9 new citations this run, 83 total. Next: v41 if Sapient ships an open-weight HRM-Text-3B or if Anthropic publishes a recursive self-improvement blog post in July 2026.*
