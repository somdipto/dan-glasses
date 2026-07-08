# DAN-2 Papers to Read — v14
**Date:** 2026-06-19 (companion to `dan2-research-report.md`)
**Audience:** somdipto + any engineer joining danlab.dev
**Selection criteria:** Directly informs Dan Glasses v1.0/v1.5/v2 product decisions. Ordered by read priority.

---

## Top 5 — must read this month

### 1. **SIA: Self Improving AI with Harness & Weight Updates** (Hebbar et al., 2026)
**arXiv:** forthcoming (paper accompanies `hexo-ai/sia` GitHub release, May 29 2026)
**Code:** https://github.com/hexo-ai/sia
**License:** MIT

**Why:** This is the credible path from danlab-multimodal's "pre-RL scaffold" to a real self-improvement loop. Reads the trajectory from a target agent, has a Feedback-Agent (default: gpt-oss-120b) decide between rewriting the harness and triggering a LoRA weight update. Reference gains: LawBench +56.6%, CUDA kernel −91.9% runtime, scRNA denoising +502%. **TriMul/denoising numbers are train/test overlap — only LawBench is a clean generalization test.** We need to build our own held-out set.

**What to take to product:**
- The two-lever framing (harness + weights) is the right model for our wearable.
- Fork as `danlab-ai/sia-fork`, swap default Feedback-Agent for LFM2.5-1.2B-Thinking (MIT).
- 6-week workstream for an engineer. 4-week if we already have harness orchestration.

**Caveat:** the published LoRA updates are on `gpt-oss-120b` (120B params). Our wearable target is sub-2W — we need to test whether LoRA on LFM2.5-VL-450M gives measurable gain. Likely yes; not guaranteed.

---

### 2. **Anthropic — "When AI Builds Itself: Our progress toward recursive self-improvement"** (May 2026)
**URL:** https://www.anthropic.com/research/recursive-self-improvement (and Hacker News discussion at https://news.ycombinator.com/item?id=48400842)
**No paywall** (Anthropic policy blog).

**Why:** Anthropic's most detailed public account of how they are developing recursive self-improvement (RSI). Frame: AI system "fully autonomously designing and developing its own successor." They describe pre-training acceleration via RSI (Karpathy hired to lead the team). Read this to understand **the closed-frontier framing of our category.** Don't copy. Differentiate on the user-aligned + on-device axis.

**What to take to product:**
- Understand what frontier RSI looks like. Our version is post-training on user data, not pre-training.
- Read the Jack Clark / Dario Amodei quotes for the regulatory backdrop.
- Watch for the Fable 5 export-control episode (May-June 2026) — this is the political tailwind for our on-device thesis.

**Caveat:** Anthropic frames RSI as a frontier-only capability. We frame it as a wearable capability. The two framings will collide in 2027-2028. We win by publishing reproducible held-out gains *first*.

---

### 3. **DeepMind — "AGI is Not the End: A Research Roadmap from AGI to ASI"** (2026)
**URL:** https://www.htx.com/news/agi-is-not-the-end-deepminds-new-paper-moving-towards-asi-th-rvAAfOdJ (secondary); original on DeepMind blog.
**No paywall** (DeepMind publication policy).

**Why:** DeepMind's research team outlines four pathways from AGI to ASI: (1) compute/model/data scaling, (2) algorithmic evolution, (3) recursive self-improvement, (4) multi-agent coordination. They identify six bottlenecks: data wall, economic/resource pressures, neural network paradigm limits, research difficulty, abstraction barriers, regulatory pushback. **Read for the framing of where we sit in the landscape.**

**What to take to product:**
- Our category is (3) + (4) on edge. Validated externally as a credible path.
- Bottleneck 6 (regulatory pushback) is our tailwind. The Fable 5 episode + DoD "supply chain risk" framing of Anthropic (CNBC, June 17 2026) + Illinois HB4843 smart-glasses driving ban (June 15 2026) all reinforce the on-device-first thesis.
- Bottleneck 1 (data wall) means our user-trajectory corpus is structurally valuable. Don't waste it.

---

### 4. **ProAct — "Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents"** (arXiv:2605.25971)
**URL:** https://arxiv.org/html/2605.25971v1
**License:** arXiv preprint (likely CC-BY-NC or similar).

**Why:** This is the architecture for our `proactived` service. Uses idle time between user interactions to predict upcoming needs from dialogue history. Result: −14.8% turns to completion, −11.7% user effort, −28.1% hallucination on ProActEval. Maps directly to "the wearable that initiates, doesn't just respond."

**What to take to product:**
- The idle-time compute framing justifies the v1.0 cheap-proactive plan (hand-coded rules on memoryd events).
- The ProActEval benchmark is the eval for v1.5 distilled ProActor 1-2B.
- Concurrency-safe: ProAct runs alongside the user-interaction loop, doesn't block.

**Caveat:** ProAct's 14B baseline is too large for wearable. v1.5 plan is to distill a 1-2B version. No paper does this yet — we'd be first.

---

### 5. **Mnemosyne — "The Zero-Dependency, Sub-Millisecond AI Memory System for Hermes Agents and Everyone Else"** (April 2026)
**URL:** https://github.com/AxDSan/mnemosyne
**License:** MIT (per README)

**Why:** This is the swap target for memoryd. 98.9% Recall@All@5 on LongMemEval (ICLR 2025 benchmark). Single SQLite file. Zero cloud dependencies. Native OpenClaw provider via `pip install mnemosyne-memory[openclaw]`. The cheapest credibility upgrade available to Dan Glasses.

**What to take to product:**
- Drop-in replacement for our current `all-MiniLM-L6-v2` flat index.
- Set `plugins.slots.memory = "memory-core"` in `openclaw.json` (community gotcha — without this, OpenClaw loads the wrong memory plugin).
- 6-week workstream to swap. Validates ≥95% Recall@All@5 on our held-out set.
- Mnemosyne also scored top on BEAM (ICLR 2026). Worth benchmarking both.

**Caveat:** Mnemosyne is a 6-layer framework with "dual reasoning" — if our use cases are mostly simple episodic recall, we pay complexity tax. Mitigation: use Mnemosyne in dense mode (default), ignore the framework layers we don't need.

---

## Next 5 — read this quarter

### 6. **Zamba2-VL** (Zyphra, May 2026)
**Why:** Direct competition for LFM2.5-VL-450M. 10× TTFT improvement claim via shared projection between visual and text tokens. Need to measure on our silicon. The 10× claim is from Zyphra's own benchmark — not guaranteed to hold on Redax aarch64.

### 7. **ProActor (ACL 2026) — proactive agent for meeting/coding contexts**
**Why:** The 14B baseline is too large for wearable. But a distilled 1-2B ProActor-style model is the v1.5 plan. Read to understand the distillation target.

### 8. **User-as-Code (UaC, arXiv:2606.16707, June 16 2026)**
**Why:** Typed Python objects as user model. 78.8% on LOCOMO benchmark. New 5th memory option that didn't exist when v12 was written. Worth evaluating for v1.5 alongside Mnemosyne.

### 9. **PAGER — "Proactive Monitoring Agent for Enterprise AI Assistant"** (ACM 2026)
**URL:** https://dl.acm.org/doi/full/10.1145/3786335.3813212
**Why:** Enterprise framing of proactive agents. Validates the category. Useful for the Fable-5-safe B2B pitch.

### 10. **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M** (Liquid AI, June 18 2026)
**Why:** Purpose-built retrieval layer. 4.4× smaller than MiniLM with higher retrieval quality. Replaces the v12 "benchmark BGE-small in v1.5" plan. Worth integrating as the embedding layer of Mnemosyne swap.

---

## Carry-forwards from v13/v12 (still relevant)

- **RHO (Retrospective Harness Optimization, arXiv:2606.05922)** — label-free; 0.78 SWE-Bench Pro at 1 round vs Meta-Harness 0.60 at 1 round. Real playbook for danlab-multimodal.
- **VLCache (arXiv:2512.12931)** — vision-language caching. Worth understanding before v2 wearable.
- **Memanto counter-argument** — for v1.5 memory evaluation, also benchmark Memanto to stress-test Mnemosyne.
- **PRISM + ProActor** — paired: PRISM for proactive tool selection, ProActor for proactive timing. v1.5 stack.
- **Eywa + SpatialWorld** — demoted to read list (v13). Architecture-of-thought work; speculative for AGI but not yet product-relevant.

---

## Reading schedule (suggested)

| Week | Paper | Deliverable |
|---|---|---|
| W1 | #1 SIA | Start fork + define held-out set |
| W1 | #5 Mnemosyne | Start `pip install` + eval plan |
| W2 | #2 Anthropic RSI | Write internal framing doc |
| W2 | #3 DeepMind roadmap | Update `docs/agi-roadmap-v14.md` |
| W3 | #4 ProAct | Start proactived design |
| W4 | #6 Zamba2-VL | Start perceptiond benchmark |
| W5-8 | #7-10 | Read in spare cycles |

---

*Half-life of useful reading list is now ~1 week. v14 reads in 90 seconds. v13 archived.*