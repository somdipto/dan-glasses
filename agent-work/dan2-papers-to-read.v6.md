# Top 5 Research Papers to Read (v6)

**Author:** Dan2 (Research Agent) | **Date:** 2026-06-24 11:30 IST
**Status:** v6 — supersedes v1–v5
**Companion to:** `dan2-research-report.v6.md`

> v6 selection criterion: **every paper must (a) inform a concrete Danlab decision in the next 90 days, (b) have a public benchmark or eval, (c) be readable in a single sitting, and (d) cite or reference each other.** The 5 papers are the spine of the audiod calibration RL agent, memoryd v2, and proactived v1 designs.

---

## #1 — AIE-Bench: Benchmarking Agents That Build Agents (ICML 2026)

**Venue:** ICML 2026
**URL:** https://openreview.net/forum?id=f9yc09BuxG
**Why it matters:** This is **the public venue for audiod calibration RL agent submission.** Operationalizes meta-improvement as a measurable, reproducible benchmark with two task families (terminal interaction, tool calling). A meta-agent proposes modifications; a target-agent is evaluated on a held-out task set; improvement is measured across iterations.

**Concrete Danlab action:** Submit the audiod calibration RL agent to AIE-Bench by Sep 30, 2026. The audiod agent is *both* a meta-agent (proposes calibration head modifications) and a target-agent (whisper.cpp base.en wrapped with calibration head). AIE-Bench scoring becomes the public benchmark for the audiod RL agent's improvement curve.

**Reading time:** 90 min for the main paper + 60 min for the SEAGym companion (paper #2).

---

## #2 — SEAGym: An Evaluation Environment for Self-Evolving LLM Agents (OpenReview 2026)

**Venue:** OpenReview 2026
**URL:** https://openreview.net/forum?id=hLHB7NCuke
**Why it matters:** Companion to AIE-Bench. Tests harness-only updates (prompts, memories, tools, skills, middleware) on Terminal-Bench 2.0 and HLE under a unified epoch/batch protocol. **Key finding:** "Frequent updates do not necessarily improve held-out performance; useful intermediate snapshots can degrade later." This is the empirical confirmation of arXiv 2606.21090's rise-and-collapse finding for harness-only loops.

**Concrete Danlab action:** Submit the audiod RL agent (harness-only variant — calibration head is the only updated parameter) to SEAGym alongside AIE-Bench. Eval the failure-mode registry's effectiveness: does ES (early-stop on validation ECE) prevent the SEAGym "useful intermediate snapshots degrade later" trap?

**Reading time:** 60 min.

---

## #3 — AEL: Agent Evolving Learning for Open-Ended Environments (ACL ARR 2026)

**Venue:** ACL ARR 2026
**URL:** https://openreview.net/forum?id=dtPo105y8x
**Why it matters:** **The architecture pattern for memoryd v2's fast Thompson bandit.** AEL treats memory usage as online policy selection: a fast Thompson Sampling bandit selects among memory-retrieval policies episode-by-episode; a slow LLM reflection follows a diagnose-before-prescribe approach. Sharpe +27% on a portfolio benchmark (lowest variance among stochastic methods); +18% on support-ticket routing vs reflection-free Thompson, +51% vs best prior baseline.

**Concrete Danlab action:** Adopt AEL's two-timescale pattern in memoryd v2 (week 3 of the v2 build). The 5-mode bandit — {semantic, episodic, procedural, graph, reranked} — maps directly onto memoryd's planned stores. Reflective policy injection is the slow loop (nightly batch, opt-in).

**Reading time:** 75 min. (The AEL bandit pseudocode in our `dan2-research-report.v6.md` Deep Dive C is the v6 implementation spec.)

---

## #4 — Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory (DPCM, ACL ARR 2026)

**Venue:** ACL ARR 2026
**URL:** https://openreview.net/forum?id=ywl53zPXu0
**Why it matters:** **The architecture pattern for memoryd v2's doubly-linked provenance graph AND the operative_context surface (NEW v6).** DPCM organizes memory along a cognitive capability hierarchy from raw inputs and atomic facts up to domain schemas, latent intentions, and cross-domain patterns. SYSTEM 1 (synchronous writer, doubly-linked superseded chains) handles immediate belief revisions; SYSTEM 2 (asynchronous engine) induces schemas, intentions, cross-domain consistency. +5.20 on PersonaMem-v2.

**Concrete Danlab action:** Adopt DPCM's doubly-linked graph schema in memoryd v2 (week 2). The v6 extension: add the `operative_context` table as the SYSTEM 1 → SYSTEM 2 handoff point — the "what currently drives behavior" surface that proactived reads.

**Reading time:** 60 min. (DPCM's hierarchical capability model maps onto memoryd's {episodic, semantic, procedural} type taxonomy.)

---

## #5 — Towards a Science of AI Agent Reliability (arXiv 2602.16666)

**Venue:** arXiv preprint, 2026
**URL:** https://arxiv.org/html/2602.16666v3
**Why it matters:** **The theoretical frame for the audiod calibration RL agent and every daemon's `/reliability` endpoint.** Decomposes reliability into four first-class axes: consistency (does the same input → same output?), robustness (does small input perturbation → bounded output perturbation?), predictability (is confidence calibrated?), safety (does the agent refuse when it should?). The audiod RL agent is **a predictability implementation** — calibrated confidence on speech transcription.

**Concrete Danlab action:** Every daemon ships a `/reliability` endpoint returning `{consistency_score, robustness_score, ece, brier, last_failure_class}`. audiod is first (predictability); perceptiond salience confidence follows; toold execution success; memoryd retrieval ECE; ttsd intelligibility; os-toold denials distribution.

**Reading time:** 90 min (theory paper, dense).

---

## Honorable mentions (read in second pass)

These didn't make the top 5 because they don't directly inform a 90-day Danlab decision, but they're critical for the 12-month and 24-month plans:

- **POISE: Autonomous Discovery of LLM-RL Algorithms** (ACL ARR 2026) — LLM agents that discover improved RL algorithms. Relevant for audiod RL agent's training-loop design if we hit a ceiling. https://openreview.net/forum?id=EPWdJDKSXx
- **SIA (Hexo Labs, MIT, May 2026)** — Harness+weights self-improvement substrate. The long-term fork target. https://github.com/HexoLabs/SIA
- **EvoMaster** (OpenReview 2026) — Self-evolving agent framework. +159-316% over OpenClaw baseline on HLE / MLE-Bench Lite / BrowseComp / FrontierScience. https://openreview.net/forum?id=lidiprht3N
- **Socratic-SWE** (arXiv 2606.07412) — Self-evolving coding agents with trace-derived skills. Pattern for paperclip agent v2. https://arxiv.org/abs/2606.07412v1
- **Operative Contexts: Belief Revision and Memory in Agentic AI** (OpenReview 2026) — The "operative context vs stored memory" distinction is the theoretical frame for the v6 `operative_context` table. https://openreview.net/forum?id=KSzS4FHzau
- **GRAM** (OpenReview 2026) — Graph-structured memory management via GRPO. https://openreview.net/forum?id=rzGvGnwVC7
- **RefCon** (ACL ARR 2026) — Iterative Refinement and Contrastive Memory Extraction. Pattern for procedural memory. https://openreview.net/forum?id=fatsyRRKEs
- **AtomMem** (ACL ARR 2026) — Learnable dynamic agentic memory with atomic CRUD operations. https://openreview.net/forum?id=dfWiKLx6fs
- **SEER** (ACL ARR 2026) — Unsupervised self-evolution of reasoning via model-intrinsic verification. https://openreview.net/forum?id=9PhHO8wFyh
- **Self-Compacting Language Model Agents** (arXiv 2606.23525) — Adaptive context compaction, up to 18.1-point gains in math tasks, 30-70% lower token cost. https://arxiv.org/abs/2606.23525v1
- **Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode** (arXiv 2606.21090) — REINFORCE on competitive programming, Qwen-2.5-3B/7B, CARE / ES / GRPO mitigation. The failure-mode registry justification. https://arxiv.org/abs/2606.21090v1
- **From Trainee to Trainer** (arXiv 2606.17682) — LLM-as-Environment-Engineer for RL. Qwen3-4B backbone. https://arxiv.org/abs/2606.17682v1
- **V5e-0** (OpenReview 2026) — Self-speculative decoding for VLMs, 1.89× speedup, zero training. https://openreview.net/forum?id=GpFgbKW7PR
- **CondenseVLM** (OpenReview 2026) — Visual token condensation, evidence-preserving. https://openreview.net/forum?id=9rMb7isKDc
- **QViD** (OpenReview 2026) — Query-Vision Interaction Decomposition for token pruning. https://openreview.net/forum?id=UgbjqumIWe
- **SpecFlow** (arXiv 2606.02842) — Spectral-Progressive Thought Flow, bounded visual workspace. 2.1× compute/KV-cache savings. https://arxiv.org/abs/2606.02842v1
- **RWRR-BENCH** (OpenReview 2026) — Right-Answer Wrong-Reason benchmark. Reasoning faithfulness eval. https://openreview.net/forum?id=GEOrdCc0
- **CAGE / Abstraction Gap in VLMs** (arXiv 2605.28779) — Causal reasoning in VLMs. Eval baseline for VLM causal claims. https://arxiv.org/abs/2605.28779v1
- **StreamMemBench** (arXiv 2606.14571) — Streaming eval of agent memory for future-oriented assistance. Proactived eval baseline. https://arxiv.org/abs/2606.14571v1
- **HINT: Hierarchical Inference for ARC-AGI** (OpenReview 2026) — Hierarchical inference with task demonstrations, 20.8% on ARC-AGI-2 at $0.28/task. Reasoning agent reference. https://openreview.net/forum?id=9eE9OWN5Uf
- **Anthropic Jun 4 2026 pause call (Jack Clark + Marina Favaro)** — The reason reliability work is the v6 differentiator. https://www.aljazeera.com/economy/2026/6/5/anthropic-urges-ai-labs-to-pause-warns-humans-risk-losing-control

---

## Reading order (recommended)

1. **AIE-Bench** first — sets the eval frame.
2. **SEAGym** second — extends the eval frame to harness-only.
3. **AEL** third — gives the memoryd v2 bandit pattern.
4. **DPCM** fourth — gives the memoryd v2 graph + operative context pattern.
5. **Reliability** fifth — gives the theoretical frame for `/reliability` on every daemon.

Total reading time: ~6 hours. Best done in a single weekend.

---

## v5 → v6 changes

1. **v5 #1 was POISE. v6 #1 is AIE-Bench.** The shift: v6 prioritizes *measured self-improvement* (AIE-Bench + SEAGym public benchmarks) over *theoretically-grounded RL discovery* (POISE). audiod calibration is auditable, not theoretical.
2. **v5 #2 was DPCM. v6 #2 is SEAGym.** SEAGym is the harness-only counterpart to AIE-Bench; the audiod RL agent is harness-only by design (calibration head is the only updated parameter).
3. **v5 #5 was reliability paper. v6 #5 is still the reliability paper.** Stayed — this is the theoretical frame for `/reliability` on every daemon.
4. **AEL held at #3 across v5 and v6.** The fast Thompson bandit pattern is the v6 memoryd v2 implementation spec.
5. **DPCM dropped from #2 to #4.** SEAGym's "useful intermediate snapshots degrade later" finding is more actionable in the 90-day window than DPCM's full hierarchical capability model.
6. **Added 20 honorable mentions (v5 had 6).** The 2026 self-improvement literature has exploded; v6 makes the literature legible.

— Dan2, 2026-06-24 11:30 IST
