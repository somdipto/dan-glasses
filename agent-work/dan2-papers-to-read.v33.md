# Dan2 — Top 5 Research Papers to Read (v33)
**Date:** 2026-06-20 06:30 UTC (12:00 IST)
**Status:** v33 — refreshed after June 16-20 research wave
**Audience:** somdipto, Dan1/Dan3/Dan4
**Scope:** The 5 papers Danlab must read to make the right product and research decisions in 2026

---

## How to read this list

These papers are prioritized by **direct impact on Dan Glasses / Danlab AGI roadmap decisions in the next 6 months**. They are not the "best" papers of 2026 abstractly — they are the ones that change what we should build, what we should spike, and what we should defer.

**Read order:**
- **Week 1, Paper 1 + 2**: The self-improving agent primitive (Meta-Harness) and the wearable silicon (OpenGlass).
- **Week 2, Paper 3 + 4**: The memory layer (Mnemosyne + Mem0) and the eval harness (SEAGym).
- **Week 3-4, Paper 5**: The proactive agent (Decagon DuetBench or the proactive memory literature).

Then read the 5 honorable mentions as time allows.

---

## Paper 1: Meta-Harness (Chelsea Finn group, 2026)

**Citation:** https://openreview.net/forum?id=2Tx03Dan7u

**Why this paper:**

Meta-Harness is the **single most important paper for Danlab's agent evolution strategy in 2026**. It proves that **harness search alone — without weight updates — beats weight tuning in production-grade agent benchmarks**. The discovered harness:
- Outperforms Terminus-KIRA on Claude Opus 4.6 and ranks **#1 on TerminalBench-2** among Claude Haiku 4.5 agents.
- Improves state-of-the-art context-management by **7.7 points with 4x fewer context tokens** on online text classification.
- Improves accuracy on **200 IMO-level problems across 5 held-out models by ~4.7 points** on retrieval-augmented math reasoning.

**Why it matters for Danlab:**

1. **It validates the Dan1/Dan2/Dan3/Dan4 skill-document-as-harness thesis.** SIA-H showed harness-only is good. Meta-Harness shows harness search + selection **beats** weight tuning on a production benchmark. This is the architectural primitive for memoryd v2's evolution loop and for the danlab-multimodal SIA-H fork.

2. **It is the bridge to the SIA-W+H focal model.** Once we have a verifiable harness search, the weight updates become safer (because the harness is the verification oracle).

3. **The "Post-Training Reliable Agent Systems via Harness Search" framing is the right product framing.** We are not "self-improving" — we are doing **post-training** of the agent system via harness search. This is a more defensible label than "self-improvement."

**What to do after reading:**

- **Month 1**: Stand up a SEAGym-style eval harness for the Dan1/Dan2/Dan3/Dan4 skill documents. Use Meta-Harness's "execution trace → diagnosis → harness patch" loop.
- **Month 1-2**: Spike SkillsVote as the skill lifecycle governance layer.
- **Month 2-3**: Spike SIA-H fork into danlab-multimodal using a LFM2.5-1.2B-Thinking focal model (1.2B per "Harness Updating Is Not Harness Benefit").

---

## Paper 2: OpenGlass: Open-Source Smart Glasses for On-Device Event-Based Gesture Recognition (June 2026)

**Citation:** arXiv 2606.07431. https://arxiv.org/abs/2606.07431

**Why this paper:**

This is the **wearable silicon reference for 2026**. OpenGlass achieves **11.8 hours of continuous on-device ML from a 200 mAh battery** using a GAP9 RISC-V SoC + Prophesee GENX320 event camera + nRF5340 PMIC coordinator. End-to-end gesture recognition latency is **78.3 ms** with 83.94% cross-subject accuracy.

**The architecture:**
- **GAP9 RISC-V SoC** (GreenWaves Technologies) — 10-core RISC-V cluster, sub-1W typical power.
- **Prophesee GENX320 event camera** — event-based, not frame-based. 320x320, microsecond latency, ~10mW.
- **nRF5340 PMIC coordinator** — event-driven wake-up, keeps GAP9 powered down between inferences.
- **200 mAh battery** — sufficient for 11.8h of continuous ML.

**Why it matters for Danlab:**

1. **Sub-1W wearable is achievable in 2026.** The PRD's 8-13W active estimates are wrong. Sub-1W is feasible with the right silicon + event-driven wake-up.
2. **Event cameras are the right sensor for always-on vision.** Frame-based cameras waste power on every frame. Event cameras wake up only on change.
3. **The 200 mAh reference is the right weight class.** Fits in the Brilliant Labs Halo / Monako Glass form factor.
4. **It is open-source.** All hardware schematics + software are open. We can replicate the architecture.
5. **The 78.3 ms end-to-end latency validates the salience-gated inference gate.**

**What to do after reading:**

- **Month 1**: Buy GAP9 dev kit + Prophesee GENX320 + nRF5340 PMIC. Measure LFM2.5-VL-450M on GAP9 with event camera. Target: sub-1W sustained at 4-10 FPS.
- **Month 1**: Lock the form factor decision tree (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP).
- **Month 4-6**: Integrate event camera into perceptiond v5 (replace V4L2 with event-driven capture).
- **Month 7-9**: Wearable pilot (50-100 users) on the locked form factor.

---

## Paper 3: Mnemosyne (April 2026)

**Citation:** https://github.com/mnemosyne-project/mnemosyne (and 2026 blog)

**Why this paper:**

Mnemosyne is **the single best memory system for personal AI in 2026**. It achieves **98.9% Recall@All@5 on LongMemEval** with bge-small-en-v1.5, all in a single SQLite file. The architecture is **Hermes-first with a native OpenClaw provider**. Install: `pip install mnemosyne-memory[openclaw]`.

**Why it matters for Danlab:**

1. **98.9% Recall@All@5 is the new bar.** Hindsight 91.4% (the previous ceiling) is now the floor. Letta 83.2%, Mem0 49%, all are below the new SOTA.
2. **All-in-SQLite fits the danlab architecture.** No new infra. memoryd v1 already uses SQLite BLOB. Mnemosyne is a drop-in upgrade.
3. **Hermes-first design is OpenClaw-native.** The integration path is one config line.
4. **bge-small-en-v1.5 (33M params) is small enough for the wearable.** Beats all-MiniLM-L6-v2 (22M params) at 4.4x the model size but with better embedding quality.

**What to do after reading:**

- **Month 1**: Spike Mnemosyne in memoryd. `pip install mnemosyne-memory[openclaw]` and replace the all-MiniLM-L6-v2 + cosine pipeline.
- **Month 1**: Spike LFM2.5-Embedding-350M (Liquid AI, June 18 2026) as the multilingual primary embedding.
- **Month 2-3**: Integrate Mnemosyne into memoryd v2 v1.0 (6-core stack: Mnemosyne + Mem0 + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M + Weaviate Engram).

---

## Paper 4: SEAGym: An Evaluation Environment for Self-Evolving LLM Agents (2026)

**Citation:** https://openreview.net/forum?id=hLHB7NCuke

**Why this paper:**

SEAGym is **the eval harness for self-evolving agents**. It converts Harbor-compatible benchmarks (Terminal-Bench 2.0, HLE) into dynamic self-evolution tasks with:
- train batches
- frozen update-validation
- held-out in-domain and transfer tests
- replay diagnostics
- auditable snapshot records

It runs ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. Key findings:
- **Frequent updates may not improve held-out performance.**
- **Useful intermediate snapshots can degrade later.**
- **Source task diversity and model backend influence harness reliability.**

**Why it matters for Danlab:**

1. **We cannot claim self-improving-agent gains without a SEAGym-style eval harness.** Hand-waved "looks better" is not measurement. The danlab-multimodal screenshot set needs train/val/test splits, frozen-update rules, and replay diagnostics.
2. **It directly informs memoryd v2's consolidation strategy.** "Frequent updates may not improve held-out performance" is a real warning for the AEL two-timescale Thompson Sampling design.
3. **The auditable snapshot record is the right primitive for SIA-W+H in production.** Per-user-isolated weights + audit log of every weight delta = SEAGym-style snapshot system.

**What to do after reading:**

- **Month 1**: Stand up a SEAGym-style eval harness for the danlab-multimodal screenshot set. Hold out 20% as the generalization test.
- **Month 1-2**: Spike AEL (two-timescale Thompson Sampling) in memoryd v2 dev branch.
- **Month 2-3**: Spike SIA-H on the harness-only path. Measure generalization on the held-out set.

---

## Paper 5: ProAct (2026) and Decagon Proactive Agents (June 2026)

**Citations:**
- ProAct: arXiv 2605.25971
- Decagon DuetBench: Forbes, June 13 2026

**Why these papers:**

ProAct is **the proactive AI primitive**. It uses idle time between user interactions to predict upcoming needs from dialogue history. Results: **-14.8% turns to completion, -11.7% user effort, -28.1% hallucination on ProActEval.**

Decagon Duet Autopilot is the **production reference for proactive agents** as of June 2026. The Decagon DuetBench acceptance target is 93% — a credible benchmark for proactive agent quality.

**Why it matters for Danlab:**

1. **The current stack is reactive.** audiod transcript -> OpenClaw -> tool call -> response. It does not watch. The user has to remember they own an AI companion. That fails the SOUL.md promise.
2. **The 2-week cheap path is `proactived` service** with hand-coded trigger classifier (time-of-day, last interaction > N hours, recent salient vision event). No new model.
3. **The v1.5 path is ProAct-style distilled 1-2B model** on danlab user-interaction traces. Use SIA's harness-only mode to optimize the trigger classifier.

**What to do after reading:**

- **Month 1**: Add a `proactived` service subscribing to memoryd's event stream. Hand-coded trigger classifier. Ship.
- **Month 3**: Spike ProAct-style model on the danlab interaction traces.
- **Month 6+**: Decagon DuetBench-style benchmark for Dan Glasses. Beat 93% bar.

---

## Honorable Mention 1: Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills (June 2026)

**Citation:** arXiv 2606.07412v1

Self-evolving framework for code-writing agents that uses the agent's own solving traces to build structured skills. Achieved **50.40% on SWE-bench Verified after 3 iterations**. The "trace -> skill -> task -> validate -> update" loop is the right pattern for danlab-multimodal.

## Honorable Mention 2: AEL: Agent Evolving Learning for Open-Ended Environments (2026)

**Citation:** https://openreview.net/forum?id=dtPo105y8x

Two-timescale Thompson Sampling bandit for memory-retrieval policy selection, with slow LLM reflection. **Sharpe ratio up ~27%** on sequential portfolio benchmarks. The right primitive for memoryd v2 consolidation.

## Honorable Mention 3: GRAM: Empowering Agent with Actively Managed Graph-Structured Memory (2026)

**Citation:** https://openreview.net/forum?id=rzGvGnwVC7

RL framework (Group Relative Policy Optimization) for agents to manage dynamic graph-structured memory. Sub-4B models can master memory governance. Right primitive for the v1.5+ memory evolution layer.

## Honorable Mention 4: Salesforce Fin (June 15, 2026) - $3.6B acquisition

**Citation:** https://www.reuters.com/business/salesforce-buy-fin-about-36-billion-2026-06-15/

**Why this is on the list:** This is **not a paper, it's a market signal** — but it is the single most important M&A event of 2026 for personal AI. Salesforce bought Fin (autonomous AI agent platform) for **$3.6B** on June 15. **A $3.6B vote that agents are now a platform category.** memoryd v2 is the moat layer that makes any agent platform worth $3.6B. Ship it open-source in September 2026, then build the danlab agent platform on top.

## Honorable Mention 5: Probably (June 16, 2026) - $9M Series from Andreessen Horowitz

**Citation:** https://www.thesaasnews.com/news/probably-raises-9m-seed/

Probably raised $9M to build AI hallucination elimination via validation harness. The product is a **deterministic validation system for LLM outputs**. This is the same architectural primitive as SEAGym's "frozen update-validation" and SkillsVote's "only successful, reusable discoveries are admitted as evidence." **The capital is validating the harness-first / verification-first thesis for 2026.**

---

## Reading schedule

| Week | Papers | Effort | Output |
|---|---|---|---|
| **Week 1** | Meta-Harness (Paper 1) + OpenGlass (Paper 2) | 6 hours total | SEAGym eval harness plan + GAP9 dev kit order |
| **Week 2** | Mnemosyne (Paper 3) + SEAGym (Paper 4) | 6 hours total | memoryd v2 design + eval harness spike |
| **Week 3** | ProAct + Decagon (Paper 5) | 3 hours | proactived service spike |
| **Week 4** | Socratic-SWE + AEL + GRAM (Honorable Mentions 1-3) | 4 hours | memoryd v2 v1.0 component list |
| **Async** | Salesforce Fin + Probably (Honorable Mentions 4-5) | 2 hours | Open-source release plan |

Total: ~21 hours over 4 weeks. One paper per workday.

---

## The 1-page summary

| # | Paper | Key claim | Danlab action |
|---|---|---|---|
| 1 | **Meta-Harness (Chelsea Finn, 2026)** | Harness search alone beats weight tuning. #1 on TerminalBench-2. | Stand up SEAGym eval harness. SkillsVote for governance. SIA-H fork in Month 2-3. |
| 2 | **OpenGlass (arXiv 2606.07431)** | Sub-1W wearable: GAP9 + event camera, 11.8h on 200mAh, 78.3ms latency. | Buy GAP9 dev kit Month 1. Form factor decision Month 1. |
| 3 | **Mnemosyne (April 2026)** | 98.9% Recall@All@5 on LongMemEval. Single SQLite. Hermes-first. | Replace all-MiniLM-L6-v2 in memoryd. Drop-in upgrade. |
| 4 | **SEAGym (2026)** | Eval harness for self-evolving agents. Replay + cost accounting. | Stand up for danlab-multimodal screenshot set. Hold out 20% as generalization test. |
| 5 | **ProAct + Decagon Duet Autopilot (2026)** | -14.8% turns, -11.7% effort, -28.1% hallucination. 93% DuetBench target. | Ship proactived service Month 1. Decagon DuetBench-style benchmark Month 9-12. |

These 5 papers directly inform the 24-month AGI roadmap in `dan2-agi-roadmap.v33.md`.
