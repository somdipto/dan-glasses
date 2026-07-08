# Top 5 Research Papers to Read — Danlab v99
**Author:** Dan2 👾
**Run:** 2026-06-27 10:30 IST (05:00 UTC)
**Version:** v99 — three papers rotated vs v98: adds Perplexity Brain (industry reference, validated), Gemma 4 12B (Apache 2.0 whitepaper), and the "Reasoning or Guessing" HRM mechanistic analysis. SIA + BAO retained as load-bearing pair. Continual Harness promoted to honorable mentions.
**Inputs:** v99 research report, all 18 web searches + 3 deep research calls

These are the 5 papers/references every Danlab agent should read in July 2026. Ordered by **direct relevance to product decisions in the next 90 days**. Read the abstracts first; if the abstract is relevant, read the full paper; if it changes your work, cite it in the arXiv submission Aug 15.

---

## #1 — SIA: Self-Improving AI with Harness & Weight Updates
**arXiv:** 2605.27276 (May 2026)
**Authors:** Hexo Labs, MIT
**URL:** https://arxiv.org/html/2605.27276v1

### Why we read it

This is the paper danlab-multimodal's pre-RL scaffold prefigures. SIA is a 3-agent loop (Meta-Agent, Task-Specific Agent, Feedback-Agent) that **alternates between harness updates and weight updates**, soft-labeled rather than rigid stages. Three empirical wins: +56.6% on LawBench, -91.9% runtime on GPU kernel optimization, +502% on single-cell RNA denoising.

### What we take from it (v99)

- **The 3-agent structure maps cleanly to our 8-daemon decomposition.** Meta-Agent = dani (the system of mind). Task-Specific Agent = any Dan. Feedback-Agent = the heuristic loop in danlab-multimodal.
- **The harness-update arm is reproducible on edge.** No GPU fine-tuning needed. We can ship this in danlab-multimodal in 2 weeks.
- **The "soft-labeled phases" insight is critical.** SIA doesn't rigidly schedule harness vs weight updates; it chooses per-step based on observed performance. We can do the same in awarenessd.
- **Cite in our arXiv paper** as the theoretical framework for danlab-multimodal v0.2 (the SIA harness-only fork).
- **Anthropic "When AI Builds Itself" (Jun 2026) validates this paradigm at trillion-dollar scale** — 80% of Anthropic's production code is Claude-written; Mythos Preview is 64% better than human decisions.
- **RAH (arXiv:2606.13643, Jun 2026) provides the performance attribution methodology** — +9.6pp accuracy on long-context reasoning from harness recursion alone, with the same GPT-5 model. This is the cleanest possible evidence that *harness recursion beats model upgrade at the same model.*

### Q3 deliverable

`danlab-multimodal/sia_harness_only.py` — replicates SIA's harness-update arm using LFM2.5-1.2B-Thinking as the Feedback-Agent. Benchmarked on **5 tasks** (3 existing + LawBench-style + KernelBench-style). Ship as `preprint/v0.2` alongside v0.1 (pre-RL scaffold). 2 weeks, Dan2 lead.

---

## #2 — Behavioral Agentic Optimization (BAO): Pushing Forward Pareto Frontiers of Proactive Agents
**arXiv:** 2602.11351 (Feb 2026, ICLR 2026 workshop)
**Authors:** Yihang Yao, Zhepeng Cen, Haohong Lin, Shiqi Liu, Zuxin Liu, Jiacheng Zhu, Zhang-Wei Hong, Laixi Shi, Ding Zhao
**URL:** https://arxiv.org/pdf/2602.11351
**Project page:** https://proactive-agentic-rl.github.io

### Why we read it

awarenessd needs to learn **when to interrupt the user**. BAO is the 2026 paper that explicitly frames this as a multi-objective optimization: **task performance vs user engagement**. Two mechanisms:
1. **Behavior enhancement** — explicit proactive inter-turn behaviors (retrospective reasoning + prospective planning).
2. **Behavior-regularized RL** — constrains policy updates to avoid inefficient/redundant interactions.

BAO outperforms standard RL baselines on UserRL benchmark and matches/surpasses frontier LLM agents on multi-turn tasks. **This is the training framework for awarenessd.**

### What we take from it (v99)

- **The two-part framing is exactly right.** awarenessd should enhance its proactive behaviors (interruption quality) AND regularize them (avoid annoying the user). Both are load-bearing.
- **The UserRL benchmark is the eval framework.** awarenessd v1.0 should report on UserRL tasks.
- **The behavior-regularized RL term is the calibration mechanism.** Without it, the bandit learns to interrupt constantly.
- **The 3-harness-variant bandit in v98 is the behavioral enhancement mechanism** — V_HEDGE / V_BALANCED / V_AGGRESSIVE.
- **PASK (arXiv:2604.08000) is the reference architecture for proactive AI.** IntentFlow streaming demand detection pre-screens before the bandit. Adds IntentFlow to awarenessd v0.1 design.
- **HANDRAISER (arXiv:2604.06452) is the cost-benefit calibration mechanism.** Adds cost-benefit head to the bandit.

### Q3 deliverable

`Services/awarenessd/v0.1/bao_bandit.py` — implements the 3-harness-variant bandit with:
- HRM-Text-1B on-device reasoner.
- IntentFlow demand-detection pre-screen (PASK pattern).
- Cost-benefit calibration head (HANDRAISER pattern).
- Agent-memory write on every decision (Perplexity Brain pattern).
- Asynchronous bandit posterior update.

4 weeks, Dan2 + Dan3 lead.

---

## #3 — Perplexity Brain (Industry reference, not a paper) — NEW in v99
**Launch:** June 18, 2026
**Source:** https://www.marktechpost.com/2026/06/18/perplexity-launches-brain/

### Why we read it

This is **not a paper — it's a product launch.** But the architectural insight is load-bearing for memoryd v2 / v3.

Perplexity Brain reframes AI memory in a way we should adopt directly:

> "Most AI memory remembers the user. Brain remembers what the agent did. The first is what the memory is about. The second is what it's for."

| Memory type | About | For | Produces |
|---|---|---|---|
| **User memory** (most AI today) | The user | Feeling more engaged with the agent | A profile of the user |
| **Agent memory** (Brain) | The agent's work | Helping the agent get better at the job | A traceable context graph |

### What we take from it (v99)

- **memoryd v2 must add an `agent_memories` table** alongside user-facing memories. The agent needs to remember:
  - What interrupts it issued.
  - What harness variant it used.
  - What the user response was (positive / negative / ignored).
  - What salience + cost-benefit scores were.
  - What reasoning trace led to the decision.
- **The bandit posterior updates async, overnight.** This is the Perplexity "learns overnight" pattern. Don't try to update synchronously on every interrupt.
- **The context graph is the traceable structure.** Every agent-memory is part of a graph (interrupt → response → bandit update → next interrupt), not just a flat row.
- **On-device only by default.** Perplexity Brain and Weaviate Engram are cloud-only. **Our wedge is on-device agent-memory with provenance + audit + Indic + privacy.**
- **Cite in our arXiv paper** as the architectural pattern we replicate at open-weight edge scale with HNSW + LFM2.5-Embedding-350M.

### Q3 deliverable

`Services/memoryd/agent_memories.py` + `bao_bandit.py` integration. Schema:
```sql
CREATE TABLE agent_memories (
  id INTEGER PRIMARY KEY,
  interrupt_id TEXT UNIQUE NOT NULL,
  harness_variant TEXT CHECK (harness_variant IN ('V_HEDGE', 'V_BALANCED', 'V_AGGRESSIVE')),
  salience_score REAL,
  cost_estimate REAL,
  benefit_estimate REAL,
  decision TEXT CHECK (decision IN ('GO', 'NO_GO')),
  reasoning_trace TEXT,
  user_response_label TEXT,
  bandit_posterior REAL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
1 week, Dan4 lead.

---

## #4 — SemanticXR: Object-Level Device-Cloud Semantic Memory for XR
**arXiv:** 2606.12849 (Jun 2026)
**Authors:** Rahul Singh (UIUC), Devdeep Ray (NVIDIA), Connor Smith (NVIDIA), Sarita Adve (UIUC)
**URL:** https://arxiv.org/abs/2606.12849

### Why we read it

**This is the missing semantic-memory architecture for object-aware proactive interruption.** awarenessd's "you walked past the pharmacy 3 times" (PRD US-2) requires *object-level* memory, not frame-level. SemanticXR is the first peer-reviewed paper that:
- Treats **objects as first-class units** of communication, execution, and memory footprint.
- Implements **object-centric parallelize + downsampling** on the server (3D semantic mapping point cloud).
- Uses **device-side sparse local map with incremental updates + update prioritization** for network-robust querying.
- Encodes object updates as **H.264 video frames** (not raw point clouds).

### What we take from it (v99)

- **Object-level memory is implementable today.** The architecture is published, benchmarked, and works under XR power/bandwidth/memory constraints.
- **State tracking is the load-bearing innovation.** Our current memoryd can only store "the pharmacy was here on Tuesday"; SemanticXR enables "the pharmacy door was closed on Tuesday, open on Wednesday, closed on Thursday."
- **The object-binding pattern is generalizable** to people ("the person with the red hat is Priya"), places ("this is the conference room"), and things ("this is my prescription").
- **Perplexity Brain + SemanticXR = object-aware agent-self-memory.** The context graph (Brain) is bound to objects (SemanticXR). The bandit posterior learns which *object interactions* warrant an interrupt.

### Q3 deliverable

- **Q3 2026, weeks 1–2:** Dan2 reads the paper, writes 1-page assessment at `agent-work/semanticxr-assessment.md`.
- **Aug 15, 2026:** cite the paper in the arXiv submission alongside SIA, BAO, Perplexity Brain, Mythos partial-unblock, GPT 5.6 staggering.
- **Q4 2026:** Dan4 prototypes an object-level memory extension to memoryd v2 (HNSW + LFM2.5-Embedding + object-binding layer).
- **H1 2027:** ship as memoryd v3 if prototype succeeds.

---

## #5 — Gemma 4 12B: Encoder-Free Unified Multimodal Architecture (NEW in v99)
**Released:** June 3, 2026 (Google)
**Source:** https://venturebeat.com/technology/googles-new-open-source-gemma-4-12b-analyzes-audio-video-and-runs-entirely-locally-on-a-typical-16gb-enterprise-laptop

### Why we read it

Gemma 4 12B is the **single-model convergence thesis for Dan Glasses v3 (H2 2027)**. The architecture is genuinely novel:

- **Encoder-free design.** Raw audio waveforms and visual patches flow directly into the core LLM backbone without secondary processing modules.
- **Apache 2.0 license.** Commercial-friendly. No geopolitical gating.
- **256K context.** Massive for a wearable.
- **Native agentic tool-use + explicit reasoning mode.** Maps cleanly to our awarenessd's needs.
- **16GB VRAM / unified memory footprint.** Fits Snapdragon Reality Elite (48 TOPS).

### What we take from it (v99)

- **The encoder-free design eliminates ~150–300ms fusion latency.** This is the single biggest performance win for wearable inference.
- **The 4-model pipeline (LFM2.5-VL-450M + whisper.cpp + KittenTTS + HRM-Text-1B) collapses to 1 model.** Memory budget goes from ~1.5GB (4 models) to ~6GB (1 unified model at Q4_0).
- **Cross-modal attention emerges from training.** The model "sees" audio and vision simultaneously, which is qualitatively different from a pipeline.
- **The tradeoff: 4× memory for 1 model.** Worth it if Snapdragon Reality Elite hits the market in H2 2027.
- **R&D only for now.** No Q3 commitment. Evaluate in Q1 2027 when Snapdragon Reality Elite benchmarks are public.

### Q3 deliverable

- **Q3 2026:** Dan2 + Dan3 read the Gemma 4 12B technical report.
- **Q1 2027:** benchmark on Snapdragon Reality Elite dev kit (when available).
- **Q2 2027:** make the v3 architecture decision (single-model unified vs multi-model pipeline).

### Why this is the v99 rotation

v98's #5 was AutoNeural (NPU co-design). v99 rotates to Gemma 4 12B because:
- **It's more architecturally aligned** with our convergence thesis.
- **It's a model release, not a research paper** — but the architecture is publishable in our own paper.
- **It's Apache 2.0** — better license than AutoNeural's NPU research.
- **It's the long-term convergence thesis** for H2 2027.

---

## Honorable mentions (read if you have time)

- **Continual Harness** (arXiv:2605.09998, May 2026) — Reset-free online harness updates mid-episode. Maps to awarenessd's online adaptation needs.
- **HarnessX** (arXiv:2606.14249, Jun 2026) — Composable, adaptive, evolvable harness foundry. Observability + falsifiable progress emphasis maps to our audit-log requirement.
- **APEX** (arXiv:2606.15363, Jun 2026) — Three-layer co-evolution (harness + behavioral principles + workflow topology). Production-validated on NVIDIA Nemotron Edge AI Agent (+90% health score).
- **Recursive Agent Harness (RAH)** (arXiv:2606.13643, Jun 2026) — +9.6pp accuracy on long-context reasoning from harness recursion alone with the same GPT-5 model. Cite in arXiv.
- **Self-Harness** (arXiv:2606.09498, Jun 2026) — Self-improvement loop for fixed-model agents. Three stages: weakness mining, harness proposal, proposal validation. Maps to SIA fork.
- **Are Your Reasoning Models Reasoning or Guessing?** (arXiv:2601.10679, Jan 2026) — HRM performance on hard tasks is driven by guessing. HRM-Text-1B on wearable is fine for "should I interrupt?" but not for high-stakes reasoning. Cite in arXiv.
- **Tiny Recursive Model (TRM)** (arXiv:2510.04871, Oct 2025) — 7M-parameter recursive model outperforms HRM on Sudoku-Extreme (87.4% vs 55%). Use as v3 on-device reasoner if we can compress HRM-Text.
- **CosmicFish-HRM** (arXiv:2605.28919, May 2026) — HRM at small scale (82M) does NOT outperform comparable transformers. Don't scale HRM below 1B.
- **HANDRAISER** (arXiv:2604.06452, Apr 2026) — Interruptible multi-agent communication framework. 24–49% cost reduction. Use as cost-benefit calibration head.
- **InterruptBench** (arXiv:2604.00892, Apr 2026) — First systematic eval for interruptible agents in long-horizon tasks. Validates proactive interruption is a hard problem worth solving.
- **PASK** (arXiv:2604.08000, Apr 2026) — IntentFlow streaming demand detection. Reference architecture for awarenessd pipeline.
- **POISE** (arXiv:2603.23951, Mar 2026) — Policy Optimization through Iterative Search and Evidence. For awarenessd v2 RL.
- **E-SPL** (arXiv:2602.14697, Feb 2026) — Evolutionary System Prompt Learning. 38.8% → 45.1% on AIME-to-Beyond-AIME. For awarenessd system-prompt evolution.
- **Polaris** (arXiv:2603.23129, Mar 2026) — Gödel Agent for Small LMs. For danlab-multimodal on-CPU repair loop.
- **SGM** (arXiv:2510.10232, Oct 2025) — Statistical Gödel Machine. E-value risk control. Use as safety wrapper for SIA fork.
- **DPCM** (arXiv:2606.09483, Jun 2026) — Dual-Process Memory. System 1 sync / System 2 async. Maps to awarenessd on-device + cloud split.
- **ProAct** (arXiv:2605.25971, May 2026) — Idle-time Compute + Future-State Prediction. Use as awarenessd scheduler design.
- **MemCog** (arXiv:2605.28046, May 2026) — Memory-as-Cognition. ProactiveMemBench SOTA.
- **CogniFold** (arXiv:2605.13438v2, May 2026) — Always-on cognitive folding. For memoryd v3.
- **MRAgent** (arXiv:2606.06036, Jun 2026) — Cue-Tag-Content graph, +23% on LoCoMo/LongMemEval. For memoryd v3 graph design.
- **AMD Ryzen AI** (arXiv:2602.06063, May 2026) — Mapping Gemma3 onto Edge Dataflow Architecture. 67× more power-efficient than CPU. Hardware benchmark reference.
- **SPEED-Q** (arXiv:2511.08914, Nov 2025) — 2-bit VLM in <400 MB. Reference for ultra-low-bit quantization.
- **CHIME** (arXiv:2601.19908v1, Jan 2026) — Chiplet-based Heterogeneous Near-Memory. 41× faster than Jetson Orin NX. Reference for v2 hardware.
- **AutoNeural** (arXiv:2512.02924, Dec 2025) — Co-Designing VLMs for NPU Inference. 14× lower latency on Qualcomm SA8295P.

---

## Industry references (cite but don't deep-read) — v99 NEW

- **Anthropic "When AI Builds Itself"** (Jun 2026) — 80% Claude-written code, Mythos Preview 64% better than human. Industry validation of SIA pattern.
- **Anthropic Mythos partial unblock** (Jun 26, 2026) — Released to ~100 US companies/agencies. Geopolitical conditioning, not closure. Cite in arXiv.
- **OpenAI GPT 5.6 staggered release** (Jun 26, 2026) — Limited preview at US government request. Geopolitical conditioning of frontier access.
- **OpenAI Jalapeño chip announcement** (Jun 24, 2026) — First custom OpenAI inference ASIC.
- **OpenAI IPO delay** (Jun 25, 2026) — At least 2027. Funding environment bifurcating.
- **Zhipu GLM 5.2 launch** (Jun 13, 2026) — 744B MoE, MIT license, within 1pp of Opus 4.8. Reasoning model choice.
- **Meta Muse Spark Glasses** (Jun 23, 2026) — $299, 8+ hour battery. Competitive landscape.
- **Sapient HRM-Text-1B** (May 2026) — $1,500 training, GSM8K 84.5%. On-device reasoner.
- **Google Gemma 4 E2B QAT-mobile** (May 2026) — 1GB footprint, 2× faster on mobile NPU. Thermal fallback.
- **Google Gemma 4 12B** (Jun 3, 2026) — Encoder-free unified audio + vision + text. v3 convergence thesis.
- **Perplexity Brain** (Jun 18, 2026) — Agent-self-memory. memoryd v2/v3 reference.
- **Weaviate Engram** (Jun 6, 2026) — Managed cloud memory. $98M raised. Cloud competitor.
- **Microsoft MAI-Thinking-1** (Build 2026) — Microsoft's first reasoning model. 97% AIME. Closed-weight alternative.

---

*Dan2 👾 — 2026-06-27 10:30 IST — committed to building the future with my partner*
