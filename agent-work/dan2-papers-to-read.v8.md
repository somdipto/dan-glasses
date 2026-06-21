# Dan2 — Papers to Read v8
## Top 5 Papers for the Danlab AGI Mission (v8 — Updated)

**Date:** 2026-06-17 11:30 IST
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v8. v7 archived as `dan2-papers-to-read.v7.md`.
**Companion:** Read `dan2-research-report.md` for the deep-dive evidence these papers support.

---

## 0. v8 Read in 30 Seconds

v8 reshuffles the top 5 to reflect what matters for Danlab right now:

1. **HRM-Text (arXiv:2605.20613)** — the on-device reasoning model. Now in HuggingFace transformers and vLLM.
2. **RHO — Retrospective Harness Optimization (arXiv:2606.05922)** — label-free self-improvement via trajectory retrospection. Beats Meta-Harness at 1 round (0.78 vs 0.60 on SWE-Bench Pro).
3. **Memanto (2026)** — pure-vector + 13-category typed schema beats graph hybrids on LongMemEval. The strongest signal that we should skip the graph layer.
4. **Meta-Harness (ICML 2026)** — harness post-training beats weights in some regimes. Concrete validation of "improve the harness before changing weights."
5. **SIA (Hexo Labs, MIT, May 2026)** — the only open-source harness+weights self-improvement framework. Read with the v8 reality-check (only LawBench is held-out generalization).

**The v8 one-week reading schedule** is at the end.

---

## 1. The Top 5 Papers (v8, in priority order)

### 1.1 HRM-Text: Efficient Pretraining Beyond Scaling
**arXiv:2605.20613 | Sapient Intelligence | May 18 2026**
**Why:** This is the on-device reasoning model for our `reasond` service. It's now in HuggingFace transformers (PR #46025 merged) and vLLM (PR #43098 open). The architecture is dual H/L transformer stacks with H_cycles × (L_cycles + 1) traversals and PrefixLM masking. We can integrate it this month.

**Key claims to verify:**
- 1B params, ~600MB at Q4 — fits aarch64
- 60.7% MMLU, 81.9% ARC-C, 82.2% DROP, 84.5% GSM8K, 56.2% MATH — competitive with 2-7B open models
- 40B tokens training, ~$1,500 — 100-900× fewer tokens than comparable models
- Brain-inspired hierarchical reasoning: H (slow, strategic) + L (fast, execution)
- **v8 critical question:** how does it perform on the kinds of reasoning we actually need? (event correlation, user preference inference, proactive suggestion ranking)

**Read for:**
- Section 3 (architecture details for `reasond` integration)
- Section 4 (training data composition — what's the right fine-tuning data for our use cases?)
- Section 5 (limitations — where does HRM-Text break?)

**Time to read:** 90 minutes for the paper + 30 minutes for the HuggingFace PR.

**Action:** integrate HRM-Text 1B into `reasond` by end of month 2 (July 2026). Benchmark latency on aarch64.

### 1.2 RHO — Retrospective Harness Optimization
**arXiv:2606.05922 | June 2026**
**Why:** Label-free self-improvement via trajectory retrospection. This is the playbook for danlab-multimodal: no human-labeled rewards, no learned reward model, just retrospective analysis of what worked.

**Key claims to verify:**
- 0.78 SWE-Bench Pro at 1 round vs Meta-Harness 0.60 at 1 round
- 0.80 at 10 rounds with 3× compute (vs Meta-Harness 0.60 → ...)
- Label-free: retrains on successful trajectories, no human feedback required
- Applies to "trajectory space" — code, execution traces, retrieved information

**Read for:**
- Section 4 (the retrospection mechanism — how does it decide what to optimize?)
- Section 5 (the harness representation — what's the search space?)
- Section 6 (compute scaling — does it scale linearly? quadratically?)
- Section 7 (failure modes — when does retrospection fail?)

**Time to read:** 60 minutes.

**Action:** if the retrospection mechanism is general (not SWE-specific), this becomes our self-improvement loop. Replace SIA fork target with RHO fork if it's more general.

### 1.3 Memanto: Pure-Vector + Typed Schema Beats Graph
**2026, paper reference under review | https://arxiv.org/abs/2604.22085 in v7 reference**
**Why:** v7 thought we needed a graph layer for memory (MemX 7-relation-type design). v8 walks that back: Memanto's result (pure vector with 13-category typed schema beats graph hybrids on LongMemEval) suggests the graph is unnecessary; the type system is the leverage.

**Key claims to verify:**
- 13-category typed schema (which 13? what metadata per type?)
- Beats HippoRAG2 (graph + vector hybrid) on LongMemEval
- Beats MemGPT (hierarchical context window) on LongMemEval
- Pure vector + cosine similarity + typed filter is enough for most queries

**Read for:**
- Section 3 (the 13-type schema — what are the categories? what metadata?)
- Section 4 (the typed filter mechanism — how does it integrate with cosine similarity?)
- Section 5 (failure modes — when does typed schema fail? graph fallback?)
- Section 6 (compute cost — does typed filter add latency? how much?)

**Time to read:** 45 minutes.

**Action:** v8 `memoryd` v2 design adopts the 13-type schema. Graph layer is a fallback only.

### 1.4 Meta-Harness: Post-Training Reliable Agent Systems via Harness Search
**ICML 2026 | OpenReview:2Tx03Dan7u**
**Why:** Concrete validation of the v7 thesis that "improve the harness before changing weights." Meta-Harness searches over the agent-system layer (execution traces, code, retrieved information) rather than model weights. Result: TerminalBench-2 #1, +7.7 on text classification with 4× fewer context tokens.

**Key claims to verify:**
- Harness post-training can match or beat weight post-training in some regimes
- Coding-agent proposer reads source code + scores + traces from filesystem
- Works on TerminalBench-2 (outperforms Terminus-KIRA on Claude Opus 4.6)
- 7.7-point improvement on online text classification
- 4.7-point improvement on retrieval-augmented math reasoning across 5 held-out models

**Read for:**
- Section 3 (the harness representation — what's searchable?)
- Section 4 (the proposer — how does it generate harness candidates?)
- Section 5 (the scoring — how is harness quality measured?)
- Section 6 (the generalization claim — does it transfer across models?)

**Time to read:** 60 minutes.

**Action:** if we adopt Meta-Harness, the first candidate for our Dan Glasses stack is the `proactived` rule set. The proposer reads the rule log + user feedback, proposes new rules, scores them on held-out traces. **This is the highest-leverage v1.5 work after `reasond` ships.**

### 1.5 SIA: Self-Improving AI Framework
**Hexo Labs | MIT License | May 2026 | github.com/HexoLabs/SIA**
**Why:** This is the only open-source harness+weights self-improvement framework. v7 picked it as #1; v8 moves it to #5 because (a) RHO is newer and label-free, (b) the only reported held-out generalization is LawBench (TriMul and denoising are train/test overlap).

**Key claims to verify (with v8 skepticism):**
- 3 tasks: LawBench (70.1%), TriMul (14.02×), denoising (0.241)
- 2 levers: harness (instruction tuning) + weights (SFT on trace data)
- **Only LawBench is a held-out generalization.** TriMul is a synthetic task where train/test overlap is plausible; denoising is a regression task where train/test overlap is likely.
- The Feedback-Agent is a separate model (Qwen2.5-7B-Instruct in the reported runs)

**Read for:**
- Section 3 (the harness representation — what's the search space?)
- Section 4 (the weights mechanism — how are weight updates triggered?)
- Section 5 (the Feedback-Agent — what model? can we swap in HRM-Text 1B?)
- Section 6 (compute cost — what's the minimum compute for a measurable delta?)
- Section 7 (failure modes — what stops the loop from converging?)

**Time to read:** 90 minutes.

**Action:** v8 fork plan: build harness-only loop first (no weights), use HRM-Text 1B as the local Feedback-Agent. Move to harness+weights only after we have measured the harness-only improvement on a held-out task.

---

## 2. Honorable Mentions (read if time permits)

### 2.1 DPCM — Memory Beyond Recall
**OpenReview:ywl53zPXu0**
- Dual-process cognitive memory (System 1/2) for self-evolving agents
- +5.2 on PersonaMem-v2
- Alternative to MemGPT-style architecture
- **Read if:** v8 `memoryd` v2 needs a stronger memory organization story

### 2.2 StreamMemBench
**arXiv:2606.14571**
- Tests if memory systems can use stored evidence for future-oriented assistance
- Most systems fail
- Direct test for "remember this so you can help me later"
- **Read if:** `proactived` needs to know if memoryd's recall is actually useful

### 2.3 OP-Bench — Over-Personalization Benchmark
**ACL ARR 2026 | OpenReview:qRtPIkjN7P**
- Three failure modes: Irrelevance, Repetition, Sycophancy
- Tests if memory-augmented agents over-personalize
- **Read if:** `memoryd` v2 needs over-personalization guards

### 2.4 HERO — Hindsight-Enhanced Reflection
**OpenReview:CFnfsORP7Y**
- Turn-level self-distillation for multi-turn agents
- Beats GRPO and environment-feedback self-distillation
- **Read if:** SIA fork needs better per-turn credit assignment

### 2.5 StreamReady + ProReady-QA
**OpenReview:KXge8OA222**
- Readiness-aware streaming video QA
- Answers only when enough evidence
- **Read if:** `proactived` needs "when to speak" calibration

### 2.6 Darwin Family — Evolutionary Merging
**OpenReview:ZlbnuiD4I8**
- Training-free evolutionary merging of LMs
- Darwin-27BOpus: 86.9% on GPQA Diamond
- **Read if:** we want a training-free way to combine HRM-Text 1B + Gemma 4 1B + LFM2.5-VL-450M

### 2.7 V5e-0 — Self-Speculative Decoding for VLMs
**OpenReview:GpFgbKW7PR**
- 1.89× wall-clock speedup for VLMs
- Drafter reuses verifier's text-only hidden states
- **Read if:** perceptiond needs faster VLM inference

### 2.8 QViD — Vision Token Pruning
**OpenReview:UgbjqumIWe**
- Training-free token pruning via low-rank decomposition
- Aggressive token budgets with preserved performance
- **Read if:** LFM2.5-VL-450M inference is still too slow

### 2.9 Failing Tools — LLM Agent Recovery Under Tool Failures
**OpenReview:j7YsSnA64D**
- 218 scenarios, no model scored above 11.47% under base recovery evaluator
- Failure detection, retry/fallback, state verification, uncertainty communication
- **Read if:** `toold` needs a recovery contract; audiod needs graceful degradation

### 2.10 GAMBIT — Active Memory Benchmark
**OpenReview:qGMh6l7hRw**
- Tests online updating, ordered recall, interference resistance
- Models that score high on passive retrieval often fail on active state management
- **Read if:** we want a benchmark for `memoryd` v2's active recall

### 2.11 POISE — LLM-Discovered LLM-RL Algorithms
**OpenReview:EPWdJDKSXx**
- 64 candidate algorithms, starting from GRPO
- Best variant: weighted Overall 47.8 → 52.5, AIME25 pass@32 26.7% → 43.3%
- **Read if:** SIA fork needs a better RL algorithm than GRPO

### 2.12 MemRefine — LLM-Guided Memory Compression
**arXiv:2606.13177**
- LLM evaluates factual content before delete/merge/preserve
- Beats rule-based compression on tight budgets
- **Read if:** `memoryd` v2 needs a compression strategy at scale

### 2.13 When Users Don't Ask
**ACL ARR 2026 | OpenReview:jaAA72U0tr**
- LOCOMO-CONV benchmark: in-situ dialogue retrieval
- Conversational framing reveals retrieval gaps unseen in QA benchmarks
- **Read if:** `memoryd` v2 needs to handle "the user didn't ask but mentioned X"

### 2.14 Anthropic "When AI Builds Itself" (June 4-11 2026)
**Marina Favaro + Jack Clark | 36 pages**
- Claude writes >80% of Anthropic's code
- 60% chance of full RSI by end of 2028
- Proposes verifiable global pause mechanism
- **Read if:** you're making any self-improvement decision (this is the political backdrop)

### 2.15 Sapient HRM (the precursor to HRM-Text)
**arXiv:2506.21734 | 2025**
- The original Hierarchical Reasoning Model for non-language tasks
- Brain-inspired two-timescale architecture
- **Read if:** you want to understand why HRM-Text works

---

## 3. The v8 One-Week Reading Schedule

| Day | Paper(s) | Time | Outcome |
|---|---|---|---|
| **Mon** | HRM-Text (arXiv:2605.20613) + HuggingFace PR #46025 | 2h | Architecture decision for `reasond` |
| **Tue** | Meta-Harness (ICML 2026) + Anthropic "When AI Builds Itself" | 2.5h | Harness post-training thesis validated; political context loaded |
| **Wed** | RHO (arXiv:2606.05922) | 1h | Self-improvement playbook (label-free retrospection) |
| **Thu** | Memanto + DPCM | 1.5h | `memoryd` v2 typed-schema design |
| **Fri** | SIA + HERO + OP-Bench | 3h | SIA fork plan, credit assignment, over-personalization guards |
| **Sat** | StreamReady + StreamMemBench + GAMBIT | 2h | Proactive layer + active memory benchmarks |
| **Sun** | Light reading: V5e-0, QViD, Failing Tools, POISE | 1.5h | Optional speedups and failure modes |

**Total: ~13.5 hours across 7 days.** Roughly 2 hours/day. Realistic for a co-founder with a day job.

---

## 4. What Changed from v7 to v8

| # | v7 | v8 | Why |
|---|---|---|---|
| 1 | RHO | **HRM-Text** | HRM-Text is now in transformers + vLLM; RHO is still arXiv-only |
| 2 | VLCache | **RHO** | RHO is label-free; VLCache is a KV-cache speedup (still good but not priority) |
| 3 | MemPrivacy | **Memanto** | Memanto gives the strongest signal for our `memoryd` v2 design |
| 4 | AEL | **Meta-Harness** | Meta-Harness has ICML 2026 acceptance and broader evidence |
| 5 | SIA | **SIA** | Kept — still the only open-source harness+weights framework, but moved down due to generalization concerns |
| — | (new) | Anthropic brake pedal memo | The political backdrop; must-read for any self-improvement decision |
| — | (new) | OP-Bench | Direct benchmark for over-personalization — must-have for `memoryd` v2 |
| — | (new) | StreamMemBench | Direct test for "remember this to help later" — must-have for `proactived` |

**v8 critical move:** HRM-Text from honorable mention (#1 in v8) to #1 in top 5. The architecture is concrete, the integration path is clear, and it's the on-device reasoning model that makes Danlab's thesis real.

---

*End of v8 papers-to-read. Companion artifacts: `dan2-research-report.md` (deep dives), `dan2-architecture-review.md` (concrete fixes), `dan2-model-analysis.md` (replacement candidates), `dan2-agi-roadmap.md` (the plan).*
