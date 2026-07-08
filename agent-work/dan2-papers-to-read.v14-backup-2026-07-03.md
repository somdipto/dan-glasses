# Dan2 — Top 5 Papers to Read v14 (2026-07-03 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Scope:** 5 papers that every Danlab engineer should read in Q3 2026, with 13 honorable mentions (1 new in v14).
> **Backup of v13:** `dan2-papers-to-read.v13-backup-2026-07-03.md`
> **v14 deltas vs v13 (1 new paper, 1 reorder, 0 demotions, 1 new honorable mention):** 1 new paper (Microsoft Memora, July 2026, #2), 1 reorder (Red Queen stays #1 because of the v14 sharpening: ground truth is a memoryd write; Memora moves to #2 because the storage/retrieval split is the v1.5 architecture), 0 demotions, 1 new honorable mention (MiCRo, EPFL, late June 2026).

## Reading order (1 paper per engineer-week, total 5 weeks)

The order is chosen so each paper informs the next. Week 1 is the on-device architecture question, weeks 2-3 are the self-improving + memory questions, week 4 is the proactive question, week 5 is the model-compression question.

---

## Paper 1: VisualClaw (Mervin Praison, June 2026) — the on-device cascade gate

**Why this is first.** Unchanged from v8/v9/v11/v12/v13. VisualClaw proves the on-device cascade gate architecture works for AI glasses. 98.1% VLM API cost reduction, +15.8% accuracy on EgoSchema, on-device filtering of frames before they reach the cloud VLM. **This is the single most directly applicable piece of published research to our Dan Glasses architecture.**

**v14 add: VisualClawArena averages 24.4 rounds/scenario across 200 scenarios.** This is the new test budget for "agent does multi-step work."

**What to read.** VisualClaw paper (Mervin Praison, June 2026). Key sections: (a) the on-device cascade gate; (b) the hot/cold skill injection; (c) the memory-augmented evolver; (d) the four video-QA benchmarks (EgoSchema, EgoPlan-Bench, Video-MME long, NextQA); (e) the VisualClawArena 200-scenario benchmark release.

**Key claim to verify.** 98.1% API cost reduction with +15.8% accuracy lift, and the 24.4 rounds/scenario test budget on VisualClawArena.

**Open-source artefacts.** Code on GitHub (Mervin Praison / VisualClaw). VisualClawArena benchmark released.

**Reading time.** 3-4 hours for the paper + 4-6 hours for the gate code.

**Source.** https://mer.vin/2026/06/visualclaw-explained-self-evolving-video-agent-cuts-vlm-api-cost-98-for-ai-glasses

---

## Paper 2: **NEW v14** — Microsoft Memora (Microsoft Research, July 2026) — the storage/retrieval split for long-horizon agent memory

**Why this is second (NEW v14, promoted).** Microsoft Memora (research blog + InfoWorld coverage, July 2026) is the closed-source shipped product pattern for long-horizon agent memory. Core claim: "decouple what is stored (rich memory content) from how it is retrieved (lightweight abstractions and cue anchors), reducing context token usage by up to 98% while matching or exceeding full-context accuracy." This is the v1.5 memoryd architecture.

**v14 critical read-through: the Memora pattern is the architectural fix for the v9 MemDelta finding ("agent self-memory 42% < basic RAG 47%").** Our v1.0 memoryd is a single-tier MiniLM-L6-v2 with cosine similarity. The Memora pattern adds a two-tier: rich storage + lightweight retrieval. Cue anchors are computed at write time. Retrieval is a two-hop: cue-level cosine first → if cue matches, surface the full rich memory.

**v14 critical implementation: the `auto_apply=False` contract binds at the *storage* layer, not the *retrieval* layer.** Human approves at storage write; retrieval is automatic. This is the structural enforcement of the v11 Anthropic Dreaming pattern.

**What to read.** Microsoft Research blog (Xuchao Zhang, Molly Xia, Mayukh Das, Anson Bastos, Rujia Wang, Chetan Bansal, Saravan Rajmohan) + InfoWorld coverage. Key sections: (a) the storage/retrieval split architecture; (b) the cue-anchor generation at write time; (c) the 98% context token reduction claim; (d) the bitemporal merge of new info into existing entries; (e) the long-horizon task productivity result.

**Key claim to verify.** 98% context token reduction with no accuracy loss on a long-horizon task. Two-hop retrieval (cue → rich) is faster and more accurate than single-hop cosine.

**Open-source artefacts.** Microsoft Research blog post (no code release as of v14). InfoWorld coverage with the architecture diagram.

**Reading time.** 2-3 hours for the blog + InfoWorld article + 4-6 hours for the spike plan.

**Source.** https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity ; https://www.infoworld.com/article/4191031/microsoft-unveils-memora-to-tackle-ai-agents-memory-problem.html

---

## Paper 3: Anthropic Dreaming (Jim Bennett, May 6 2026 + June 2 2026) — the closed-source productized continual-learning reference

**Why this is third (moved up from v11 #2, down from v13 #2).** The Anthropic Dreaming API is the closed-source shipped product pattern for "agent that improves itself overnight." Concrete API: `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. **The 27-day gap between Anthropic (May 6) and a second lab (June 2) tells us the industry is converging on "agent that improves itself overnight" as a product pattern.**

**v14 add: the `auto_apply=False` contract binds at the memoryd write layer. Memora's storage/retrieval split is the architectural pattern for this.** Memora makes the storage layer the only human-approval checkpoint. Retrieval is automatic.

**v14 add: the Favaro+Clark Time magazine statement (June 29 2026) — "We are not there yet, and recursive self-improvement is not inevitable" — is the Anthropic safety position that aligns with our v11/v12/v13/v14 `auto_apply=False` contract.** We are aligned with the Anthropic safety stance on agent-to-memoryd writes requiring human approval.

**What to read.** Jim Bennett's LinkedIn post (May 6 2026 + June 2 2026) + the Anthropic Dreaming beta API docs + the Favaro+Clark Time magazine article. Key sections: (a) the dual-lab dreaming pattern (Anthropic vs the second lab); (b) the `auto_apply=False` default; (c) the `session_limit=50` safety parameter; (d) the proposed-memory-update table; (e) the Anthropic safety stance on RSI.

**Key claim to verify.** The `auto_apply=False` default is enforced at the memoryd write layer, not the agent loop. Defense in depth.

**Open-source artefacts.** Closed beta API. Jim Bennett's LinkedIn post is the public reference.

**Reading time.** 2-3 hours for the LinkedIn post + Time article.

**Source.** https://www.linkedin.com/in/jimbennett/ ; Time magazine (June 29 2026).

---

## Paper 4: Red Queen Gödel Machine (Cambridge + NVIDIA, arXiv:2606.26294v1, June 24 2026) — the self-improving SOTA with the moving-judge safety finding

**Why this is fourth (moved down from v12 #2 / v13 #1).** The Red Queen Gödel Machine (RQGM) is the strongest 2026 paper for self-improving agents. **It is "not RSI, it's recursive evaluation"** — the agent AND the evaluator co-evolve under one hard constraint (a fixed ground-truth anchor). Headline results: 1.35–1.72× fewer steps than HGM-H on code/math benchmarks; **1.91× AI-paper over-acceptance bias in static judges reduced to ~1.0× with the moving judge**.

**v14 sharpening: the ground-truth set is a memoryd write, not a perceptiond-local file.** Procedural memory with TTL=7 days, rotated by somdipto, queried via the standard memoryd API. Single source of truth. The Red Queen held-out set is the 50-question procedural memory that gets re-queried at every dream pass.

**v14 critical read-through: the bias-correction result is directly applicable to our perceptual anchor problem.** A held-out, human-curated, weekly-rotated ground-truth set that re-scores the last 7 days of perceptiond descriptions is the operational implementation of the moving judge.

**v14 critical limitation: the ground-truth anchor re-introduces Goodhart pressure one level up** — the same problem we already have with our supervised anchor. The paper acknowledges this. **v14 conclusion: a single fixed anchor is not enough; we need a held-out ground-truth set that is rotated by the human. The v11 `auto_apply=False` contract is the v12 operational implementation, and the Memora storage/retrieval split is the v14 structural enforcement.**

**What to read.** The arXiv paper. Key sections: (a) the co-evolution architecture; (b) the fixed ground-truth anchor and the bias-correction protocol; (c) the 1.35–1.72× step-efficiency result; (d) the AI-paper-reviewer self-preference bias and the 1.91× → ~1.0× reduction; (e) the limitations and the Goodhart pressure one level up.

**Key claim to verify.** The bias-correction protocol is reproducible on our danlab-multimodal stack. A 50-question held-out set, rotated weekly, by somdipto, is the v14 implementation.

**Open-source artefacts.** arXiv preprint 2606.26294v1. Code not yet released as of v14.

**Reading time.** 4-5 hours for the paper + 2-3 hours for the bias-correction protocol design.

**Source.** https://arxiv.org/abs/2606.26294 ; https://whatisgm.com/blogs/ai/the-red-queen-has-a-patent-why-a-cambridge-nvidia-preprint-just-reset-the-self-improvement-debate

---

## Paper 5: Gaze-Informed Proactive AI (arXiv:2607.00445, July 1 2026) — the proactive AI pattern for wearables

**Why this is fifth (unchanged from v12/v13).** Gaze-Informed Proactive AI is the closest published analog to our proactived service. The Ollie paper proposes a two-stage design: (a) gaze estimate → region selection, (b) region select → LLM describe. The wearable must initiate not just respond. **This is the direct pattern for our proactived v1.**

**v14 add: Memora is the memoryd layer that makes Ollie possible.** Ollie's "when to assist + what to provide" needs the storage/retrieval split: storage remembers "I usually need help when looking at X" (semantic memory), retrieval surfaces the cue in <50ms. The Memora pattern is the v1.5 enabler.

**What to read.** The arXiv paper. Key sections: (a) the two-stage proactive design; (b) the gaze estimate → region select pipeline; (c) the LLM describe step; (d) the wearable latency budget; (e) the evaluation results.

**Key claim to verify.** The two-stage design matches the proactived v1 spec. The gaze estimate accuracy is sufficient for region selection.

**Open-source artefacts.** arXiv preprint 2607.00445. Code availability TBD.

**Reading time.** 2-3 hours for the paper.

**Source.** https://arxiv.org/abs/2607.00445

---

## Honorable mentions (12 → 13 in v14)

1. **Anthropic Favaro+Clark on RSI (Time magazine, June 29 2026)** — the Anthropic safety position. Unchanged from v12/v13.
2. **Karpathy 10 rules CLAUDE.md (June 28 2026)** — the harness engineering pattern. Unchanged from v12/v13.
3. **Vinton Cerf on agent protocol standards (Open Frontier, June 30 2026)** — the agent-interop risk. Unchanged from v12/v13.
4. **Meta One Premium paywall (Meta Help, BBC, July 1-2 2026)** — the empirical marketing anchor. Unchanged from v12/v13. **v14 add: BBC link https://www.bbc.com/news/articles/c3wy317d71jo is the citable primary source.**
5. **Apple Siri AI WWDC 2026 (CNET, June 30 2026)** — the TCO differentiation. Unchanged from v12/v13.
6. **Hermes Agent (Nous Research, June 2026)** — open-source agent-framework plan-B. **NEW v14 honorable mention.**
7. **GLM-5.2 (Z.ai, MIT, late June 2026)** — open-weights Mythos-class. Unchanged from v13.
8. **Mirendil (a16z-backed, June 2026)** — open-source RSI play. Unchanged from v13.
9. **Palantir + NVIDIA Nemotron sovereign engine (June 29 2026)** — sovereign vertical validation. Unchanged from v13.
10. **Anthropic Sonnet 5 + Bedrock/Vertex (July 2 2026)** — the closed-source enterprise stack. Unchanged from v13. **v14 add: the 5-57x cost multiplier vs open-weights alternatives is the new v1.0 marketing fact.**
11. **Apertus v1.1 4B (Swiss AI / EPFL, June 29 2026)** — open-weights 4B for EU data-residency. Unchanged from v14 model-analysis.
12. **MiCRo (EPFL, late June 2026)** — brain-like LLM with 4 cognitive regions. **NEW v14 honorable mention. Validates the 6-daemon split as the engineering analogue of the 4-cognitive-region pattern.**
13. **MemDelta (Kuan Wang et al., arXiv:2606.29914, June 30 2026)** — controlled memory evaluation. Unchanged from v9/v11/v12/v13. **v14 add: now the gating test for the Memora spike (we must beat the 47% basic-RAG baseline on the MemDelta test set to ship the Memora pattern to v1.5).**
