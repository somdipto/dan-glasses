# Top 5 Research Papers for the Danlab Team

**Author:** Dan-2
**Date:** 2026-07-01
**Scope:** Papers that directly inform Danlab's product and research decisions over the next 6-12 months
**Format:** Why it matters, key takeaways, how to apply it at Danlab

---

## Selection Criteria

A paper earns a spot on this list if it meets at least one of:
1. **Direct product impact** — informs a Dan Glasses architecture or model decision in 2026
2. **Research opportunity** — opens a publishable contribution Danlab can make
3. **Strategic positioning** — helps articulate the Danlab wedge (open, local, private, proactive)

I deliberately chose **5 papers** (not 10, not 20) because the team is small and reading is a tax. These are the highest-leverage reads.

---

## #1: SIA — Self-Improving AI with Harness and Weight Updates

**Authors:** Hexo Labs (MIT, May 2026)
**URL:** https://github.com/HexoLabs/SIA
**Companion:** https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights

### Why it matters (the most important paper on this list)

The danlab-multimodal README already names SIA as the credible path from "pre-RL heuristic" to "real self-improvement." This is the paper (and framework) that operationalizes that. **It's the first open-source framework that edits both the scaffold and the model weights in one self-improving loop.** SIA-H (harness only) and SIA-W+H (harness + weights) are the two variants.

The Meta-Agent writes the initial scaffold from a task spec; the Feedback-Agent (Claude Sonnet 4.6) reads the full trajectory and decides what to change. This is the architecture Danlab should port to. **If danlab-multimodal adopts SIA-W+H, it goes from "pre-RL scaffold" to "a real, defensible self-improving system" — and the team can publish the result.**

### Key takeaways

1. **Harness + weights > either alone.** SIA-W+H beats SIA-H, which beats static scaffolds. The combination of editing both the runtime and the model is what makes the loop work.
2. **The Feedback-Agent is the lever.** The Feedback-Agent decides *what* to change. A stronger Feedback-Agent = better self-improvement. **This means Danlab can improve the system by improving the Feedback-Agent, without touching the task agent.**
3. **SOTA on Karpathy's research agent benchmark.** SIA-W+H beats Karpathy's research agent — a strong baseline. The result is reproducible on GitHub.
4. **MIT licensed.** Free to use, modify, and ship commercially. No strings.

### How to apply it at Danlab

- **Q3 2026:** Port danlab-multimodal to SIA-W+H. LFM2.5-1.2B-Thinking as the task agent. Claude Sonnet 4.6 (API) or LFM2.5-1.2B-Thinking (local) as the Feedback-Agent. Validate on a multi-turn code-review task.
- **Q4 2026:** Add VSI-style reasoning verification to the SIA reward model (reject 30%+ of "correct" answers with flawed reasoning). See paper #2.
- **Q1 2027:** Extend SIA-W+H to use ETD-style recursive latent reasoning (see paper #4). This becomes the headline research contribution.
- **Target venue:** ICML 2027 or NeurIPS 2027.

**Read time:** ~3 hours for the paper + 1 day to set up the SIA framework.

---

## #2: TTSR — Test-Time Self-Reflection for Continual Reasoning Improvement

**URL:** https://arxiv.org/html/2603.03297v1

### Why it matters

TTSR is the SOTA for "single model gets better at itself" — it alternates Student and Teacher roles in a single pretrained model. The Teacher analyzes the Student's failed traces, diagnoses weaknesses, and generates targeted variant questions. This is **directly relevant to the SIA-W+H port** because the Feedback-Agent can be a TTSR-style Teacher instead of a static LLM call.

It's also the most practical path to "agent improves every week" — the kind of self-improvement the danlab-multimodal README is reaching for.

### Key takeaways

1. **Single model, two roles.** No need for a separate, larger teacher. The same model can be its own teacher.
2. **Diagnoses weaknesses from failed traces.** The Teacher doesn't just say "this is wrong" — it identifies *patterns* in the failures and generates targeted variants. **This is the right abstraction for the SIA Feedback-Agent.**
3. **No external data required.** Self-supervised at inference time. **Fits the "local-first" wedge.**
4. **Addresses noisy self-labels on hard questions.** Previous TTT methods collapse when the model can't reliably self-label. TTSR's Teacher mediation fixes this.

### How to apply it at Danlab

- **Q4 2026:** Add TTSR-style reflection to the SIA-W+H Feedback-Agent. The Feedback-Agent should:
  1. Read the task agent's failed traces
  2. Diagnose patterns ("the model fails when the input is a screenshot with text")
  3. Generate targeted training variants ("here are 5 similar screenshots with text")
  4. Re-train the task agent on the variants
- **Q1 2027:** Measure the SIA-W+H + TTSR combination on a multi-week longitudinal study.

**Read time:** ~2 hours.

---

## #3: SPEED-Q — Staged Processing with Enhanced Distillation Towards Efficient Low-Bit On-Device VLM Quantization

**URL:** https://doi.org/10.1609/aaai.v40i26.39296

### Why it matters

SPEED-Q is the SOTA for **aggressive low-bit quantization of small VLMs**. It demonstrates that sub-1B VLMs can be quantized to **2-bit or 4-bit with limited accuracy loss** — up to 6× better accuracy than prior 2-bit quantization. This is directly relevant to LFM2.5-VL-450M on Dan Glasses.

The current LFM2.5-VL-450M is Q4_0 (about 209MB). SPEED-Q 2-bit could shrink it to ~110MB — a 2× size reduction. **For a wearable with 4h battery life target, that's 2× less memory bandwidth, 2× less power, 2× faster inference.** This is the highest-leverage optimization available for the v1.5 wearable.

### Key takeaways

1. **Staged sensitivity-adaptive mechanism.** Vision (ViT) and language (LLM) components have different quantization sensitivity. SPEED-Q handles this asymmetry.
2. **Distillation-based stabilization.** Low-bit training is unstable. SPEED-Q uses distillation to keep training stable and reduce data requirements.
3. **6× better accuracy at 2-bit than prior methods.** At 4-bit, the loss is ~4.78%. At 2-bit, the loss is ~15.06%. **4-bit is the safe choice; 2-bit is the stretch goal.**
4. **Validated on InternVL2.5-1B vs. SmolVLM, FastVLM, H2OVL.** Outperforms all prior on-device VLM quantization.

### How to apply it at Danlab

- **Q4 2026:** Benchmark SPEED-Q 4-bit on LFM2.5-VL-450M. If quality holds within 5%, switch from Q4_0 to SPEED-Q 4-bit. **Saves ~50-100MB and 1.5-2× inference time.**
- **Q1 2027:** If 4-bit works, benchmark 2-bit for thermal-constrained wearable scenarios. **Stretch goal: 2-bit LFM2.5-VL-450M = ~110MB.**
- **Q2 2027:** Apply SPEED-Q to the mmproj (vision encoder) separately, since it's the F16 bottleneck (180MB of the 389MB total).

**Read time:** ~2 hours.

---

## #4: Encode-Think-Decode (ETD) — Scaling Test-Time Reasoning with Recursive Latent Thoughts

**URL:** https://openreview.net/forum?id=jY5Kh5Rjc7
**Venue:** ICLR 2026 workshop (LIT)

### Why it matters

ETD is a **parameter-free reasoning enhancement** that recursively reuses a small subset of reasoning-relevant layers during inference. **+28.4% on GSM8K, +36% on MATH with OLMo-2 1B Base.** No architectural changes, no data changes, no parameter changes.

For Dan Glasses' agent (which has to reason about the user's intent, the scene, and the proactive pre-filter all in one go), ETD-style recursive reasoning could give a **2-3× quality boost on multi-step tasks without any size cost**. This is the cheapest, highest-leverage reasoning improvement available.

### Key takeaways

1. **Recursive latent reasoning.** The model thinks over its own layers multiple times before producing output. Each pass refines the latent state.
2. **+28-36% on math/reasoning benchmarks.** Massive gains for a 1B model. Likely smaller but still meaningful for VLM-style reasoning.
3. **No new parameters, no new data.** Drop-in enhancement. The paper trains the model to do this once, then it's free at inference.
4. **Adaptive depth strategy** — compute varies per input token. Useful for wearable power management.

### How to apply it at Danlab

- **Q1 2027:** Train an ETD-style recursive latent reasoning pass on the LFM2.5-1.2B-Thinking model (which we plan to use as the task agent in SIA-W+H). Benchmark on multi-step reasoning (MATH, GSM8K).
- **Q2 2027:** If ETD works, combine with SIA-W+H: SIA-W+H edits the harness + weights, ETD gives the resulting model recursive reasoning. **This is the headline research contribution: SIA-W+H + VSI + ETD for edge agents.**
- **Q2 2027:** Apply ETD to the memoryd retrieval reasoning: when recalling episodic memories, the model "thinks" recursively over candidate memories before committing to a result.

**Read time:** ~1.5 hours.

---

## #5: ProVoice-Bench — Assessing the Proactivity of Voice Agents

**URL:** https://arxiv.org/html/2604.15037v2

### Why it matters

**ProVoice-Bench is the canonical benchmark for proactive voice agents.** It has 1,182 curated samples across 4 proactive tasks:
- **Proactive Intent Capture (PIC):** detect implicit user intent and initiate tool calls
- **Latent Topic Monitor (LTM):** monitor dialogue, intervene only when a user-defined trigger appears
- **Context Fact Checking (CFC):** interrupt when user statements contradict digital context
- **Environment Sound Sensing (ESS):** recognize user-defined acoustic events as cues to intervene

The proactive pre-filter is the biggest UX differentiator for Dan Glasses v1.5. **The team needs a benchmark to validate the proactive pre-filter. ProVoice-Bench is the answer.**

Without a benchmark, "is the proactive mode working?" becomes a vibes-based question. With ProVoice-Bench, it's measurable.

### Key takeaways

1. **Four concrete proactive tasks.** Not abstract — each is a measurable scenario.
2. **Multimodal evaluation.** Uses digital context (app states), implicit cues, and explicit triggers. **Fits Dan Glasses' sensor stack (camera + mic + memory).**
3. **The benchmark is the conversation.** Many proactive systems exist (ContextAgent, ProAgent) but until ProVoice-Bench, no way to compare them. **The team that runs on ProVoice-Bench first owns the narrative.**
4. **It's a benchmark, not a method.** The team can implement their own proactive pre-filter (PRPF-style) and evaluate against ProVoice-Bench.

### How to apply it at Danlab

- **Q4 2026 (now → Dec):** Run ProVoice-Bench on a baseline Dan Glasses configuration (no proactive pre-filter). Establish a floor.
- **Q1 2027:** Implement the PRPF (Perception-Reasoning Pre-Filter) architecture from the paper list. Run on ProVoice-Bench. Measure gain.
- **Q2 2027:** Add memoryd-triggered proactive events (ProAct pattern). Run on ProVoice-Bench again. Measure.
- **Q2 2027:** **Publish a "Proactive AI Glasses" paper** that runs ProVoice-Bench on Dan Glasses. First edge-AI-glasses product to ship proactive mode with a benchmark.

**Read time:** ~1.5 hours.

---

## Honorable Mentions (read if time permits)

These are the next 5 most-leverage papers. If the team has time, read them after the top 5.

| Paper | Why it matters | Read time |
|---|---|---|
| **Memanto** (https://arxiv.org/html/2604.22085) | SOTA long-term memory, 89.8% on LongMemEval. Use for v1.5 memoryd migration. | 2h |
| **True Memory** (https://arxiv.org/html/2605.04897v1) | Edge-friendly typed memory, SQLite-based. Direct fit for memoryd. | 1.5h |
| **TEMPO** (https://arxiv.org/pdf/2604.19295) | EM-style test-time training. Most principled TTT method. | 2h |
| **ProAct** (https://arxiv.org/html/2605.25971v1) | Idle-time compute → future-state prediction. 14.8% fewer turns. | 1.5h |
| **REVES** (https://arxiv.org/html/2606.18910) | Revision-and-verification augmented training. Multi-round self-improvement. | 1.5h |
| **All-Mem** (https://arxiv.org/html/2603.19595v2) | Agentic lifelong memory, online/offline decoupling. | 1.5h |
| **PITR-Select** (https://doi.org/10.1109/vcip67698.2025.11396912) | Visual token reduction for VLM video. 6× speedup. | 1h |
| **In-Place TTT** (https://arxiv.org/pdf/2604.06169) | Test-time training without architectural changes. | 1.5h |
| **ContextAgent** (https://doi.org/10.48550/arxiv.2505.14668) | Open-world sensory proactive LLM agents. Direct competitor. | 2h |
| **ProActor** (https://arxiv.org/html/2605.24900) | RL for proactive task timing. ACL 2026. | 1.5h |

---

## Suggested Reading Order (for the team)

If the team has 2 hours per week for paper reading:

1. **Week 1:** SIA (paper + framework setup) — this is the highest-leverage, must-read
2. **Week 2:** TTSR — directly extends SIA
3. **Week 3:** SPEED-Q — directly improves v1.5
4. **Week 4:** ProVoice-Bench — establishes the proactive benchmark
5. **Week 5:** ETD — reasoning enhancement for v2

After the top 5, prioritize the honorable mentions by what's blocking the roadmap:
- **Memory migration:** Memanto + True Memory
- **Proactive mode:** ProAct + ContextAgent
- **Self-improvement rigor:** TEMPO + REVES

---

## How These Papers Map to the Roadmap

| Roadmap Quarter | Paper(s) |
|---|---|
| Q3 2026 (SIA port) | SIA |
| Q4 2026 (VSI + proactive pre-filter) | TTSR, ProVoice-Bench |
| Q1 2027 (True Memory + ETD) | True Memory, ETD |
| Q2 2027 (paper #1 submission) | All of the above |
| Q3 2027 (SPEEED-Q 4-bit) | SPEED-Q |
| Q4 2027 (paper #2 submission) | ProAct, ContextAgent |
| Q1 2028 (edge SIA) | SIA + TTSR + ETD (combined) |
| Q2 2028 (paper #3 submission) | TEMPO, REVES, In-Place TTT |

---

*End of papers list. See dan2-research-report.md, dan2-agi-roadmap.md, dan2-architecture-review.md, dan2-model-analysis.md.*
