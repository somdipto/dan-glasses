# Dan2 — Top 5 Papers to Read v11 (2026-07-03 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Scope:** 5 papers that every Danlab engineer should read in Q3 2026, with 12 honorable mentions.
> **v11 deltas vs v9:** 1 new paper added (HRM-Text-1B / Sapient), 1 paper reordered (Anthropic Dreaming promoted to #2 with a MemDelta-conditioned caveat), 1 v9 paper demoted (MemDelta moves from #2 to #3 because the Dreaming API is now the more actionable reference), 1 v9 paper demoted (VisualClaw stays #1 but with the 24.4 rounds/scenario benchmark callout), 2 v11 adds to honorable mentions (Gemma 3 in orbit, Proactive Systems in HCI survey).

## Reading order (1 paper per engineer-week, total 5 weeks)

The order is chosen so each paper informs the next. Week 1 is the architecture question, weeks 2-3 are the memory questions, weeks 4-5 are the research questions.

---

## Paper 1: VisualClaw (Mervin Praison, June 2026) — the on-device cascade gate

**Why this is first.** Unchanged from v8/v9. VisualClaw proves the on-device cascade gate architecture works for AI glasses. 98.1% VLM API cost reduction, +15.8% accuracy on EgoSchema, on-device filtering of frames before they reach the cloud VLM. **This is the single most directly applicable piece of published research to our Dan Glasses architecture.** If the gate works on Gemini 3 Flash / GPT 5.2 with frozen weights, it works on LFM2.5-VL-450M with frozen weights.

**v11 add: VisualClawArena averages 24.4 rounds/scenario across 200 scenarios.** This is the new test budget for "agent does multi-step work" — we should adopt the 24.4 rounds/scenario number as the v1.5 test budget for our own agent loop. If our openclaw + VisualClaw-pattern agent loop can't do 24.4 rounds/scenario on VisualClawArena, we have a regression.

**What to read.** VisualClaw paper (Mervin Praison, June 2026). Key sections: (a) the on-device cascade gate that encodes frames per-frame; (b) the hot/cold skill injection; (c) the memory-augmented evolver; (d) the four video-QA benchmarks (EgoSchema, EgoPlan-Bench, Video-MME long, NextQA); (e) the VisualClawArena 200-scenario benchmark release.

**Key claim to verify.** 98.1% API cost reduction with +15.8% accuracy lift, and the 24.4 rounds/scenario test budget on VisualClawArena.

**Open-source artefacts.** Code on GitHub (Mervin Praison / VisualClaw). VisualClawArena benchmark released.

**Reading time.** 3-4 hours for the paper + 4-6 hours for the gate code.

**Source.** https://mer.vin/2026/06/visualclaw-explained-self-evolving-video-agent-cuts-vlm-api-cost-98-for-ai-glasses

---

## Paper 2: Anthropic Dreaming (Jim Bennett, May 6 2026 + June 2 2026) — the closed-source productized continual-learning reference

**Why this is second (NEW v11).** The Anthropic Dreaming API is the closed-source shipped product pattern for "agent that improves itself overnight." Concrete API: `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. **The 27-day gap between Anthropic (May 6) and a second lab (June 2) tells us the industry is converging on "agent that improves itself overnight" as a product pattern.** We are at risk of being late to the product pattern even if we are early to the open-source implementation.

**v11 add: the `auto_apply=False` default is the v1.0 contract.** This is the most important safety pattern in the entire self-improving-agent space. Anthropic requires human approval for every memory update. **Our SIA-W+H port must do the same.** The Anthropic Dreaming API is not a paper in the traditional sense (it's a LinkedIn post + a beta API), but the architectural pattern it documents is the most actionable signal of the quarter.

**v11 add: the `session_limit=50` parameter is the safety pattern we should adopt for our SIA/Dreaming port.** No single dreaming session exceeds 50 agent turns without human review. This is the operational contract for the SIA/Dreaming port.

**What to read.** Jim Bennett's LinkedIn post (May 6 2026 + June 2 2026) + the Anthropic Dreaming beta API docs. Key sections: (a) the dual-lab dreaming pattern (Anthropic vs the second lab); (b) the `auto_apply=False` default; (c) the `session_limit=50` safety parameter; (d) the proposed-memory-update table.

**Key claim to verify.** The Dreaming API is the closed-source reference for the product pattern. The v1.0 contract is `auto_apply=False`.

**Open-source artefacts.** None — the Dreaming API is closed-source. We port the pattern, not the code.

**Reading time.** 2-3 hours for the LinkedIn post + 2-3 hours for the API docs.

**Source.** https://www.linkedin.com/pulse/two-labs-started-dreaming-built-different-jim-bennett-q9ghc

---

## Paper 3: MemDelta (Kuan Wang et al., arXiv 2606.29914, June 30 2026) — the controlled memory evaluation

**Why this is third (demoted from v9 #2).** MemDelta is still the defining paper for memoryd. But the Anthropic Dreaming API (paper #2 in v11) is now the more actionable reference because it documents the *product* contract, not just the *evaluation* protocol. MemDelta tells us how to evaluate our memoryd; the Dreaming API tells us what contract the memoryd write layer must enforce.

**Key findings (unchanged from v9):**
1. Verbatim RAG matches full-context GPT-4o-mini (47.2% vs p=0.34).
2. Ranking reverses across models.
3. Swapping only the embedding model shifts accuracy by +6.2pp (p=0.004).
4. **Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — so one variable flips the conclusion.**
5. **Agent self-memory (42%) underperforms basic retrieval (47%).** This is the empirical challenge to the SIA/Dreaming "agent writes own memory" pattern.

**v11 add: the v1.5 evaluation rig should include a supersession test set.** The Diagnosing the Memory-Update Gap paper (v8) and the MemDelta paper (v9) both identify supersession as the failure mode. The Q3 v1.5 evaluation rig should include a supersession test set: 50 questions where the "right" answer is the *new* memory, not the *old* memory.

**What to read.** The full paper. Key sections: (a) the LongMemEval-S protocol; (b) the four findings above; (c) the controlled protocol design (vary one component at a time); (d) the cloud-RAG vs MiniLM-RAG comparison; (e) the agent self-memory evaluation.

**Key claim to verify.** The protocol is reproducible on our memoryd stack. The "agent self-memory underperforms basic retrieval" finding is the empirical challenge to the SIA/Dreaming pattern.

**Open-source artefacts.** arXiv preprint. Code not yet released (as of v11).

**Reading time.** 4-5 hours for the paper.

**Source.** https://arxiv.org/abs/2606.29914

---

## Paper 4: HRM-Text-1B (Sapient, June 2026) — the small-budget reasoning model

**Why this is fourth (NEW v11).** HRM-Text-1B is the most extreme data-efficient training result of 2026. 1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model (HRM) architecture with two-level recurrent computation. **This is the v1.5 audiod post-processor default and the v1.5 openclaw agent loop candidate.** The $1,500 training cost is the killer story.

**v11 add: the audiod post-processor becomes the proof point for "small-beats-large on a constrained device."** When Meta or Anthropic charges $1B for their reasoning model and we trained ours for $1,500, the marketing wedge writes itself. The audiod post-processor (which currently does intent classification + named-entity extraction on transcribed segments) needs a reasoning model that can do reasoning in a single forward pass, not a chain-of-thought. HRM-Text-1B is purpose-built for that.

**What to read.** Sapient's HRM-Text-1B blog post + the YouTube explainer ("This 1B Model Doesn't Think in Layers", June 2026) + the arXiv preprint of the original HRM paper (Sapient, 2025). Key sections: (a) the two-level recurrent computation; (b) the $1,500 training cost; (c) the 1B parameter count; (d) the reasoning model evaluation.

**Key claim to verify.** HRM-Text-1B does reasoning in a single forward pass at <500ms on ARM Cortex-A78 for 3-second segments.

**Open-source artefacts.** HRM-Text-1B weights on HuggingFace (Apache-2.0). Original HRM paper (Sapient, 2025) on arXiv.

**Reading time.** 2-3 hours for the explainer + 4-6 hours for the HRM paper.

**Sources.**
- https://www.youtube.com/watch?v=oCx22mwtw2Y — This 1B Model Doesn't Think in Layers: HRM-Text 1B (Sapient, June 2026)
- https://arxiv.org/abs/2506.21754 — Hierarchical Reasoning Model (Sapient, original 2025 paper)

---

## Paper 5: Gemma 3 in orbit (TechCrunch, June 15 2026, Loft Orbital Yam-9 satellite, NASA JPL, April 2026 deployment) — the on-device VLM in space

**Why this is fifth (NEW v11).** The first reported VLM in orbit. A 4B Gemma does real Earth-observation triage work in space with limited compute, far from a data center. **Our 450M LFM2.5-VL-450M is the same architectural class, just smaller.** The on-device VLM thesis is no longer "we hope it works" — it is "a 4B model is in space right now, doing triage."

**v11 add: this is the new external marketing reference for the on-device thesis.** "If Google trusts Gemma 3 in orbit with classified Earth-observation data, you can trust Dan Glasses with your daily memory." The combination of Gemma 3 in orbit + HRM-Text-1B at $1,500 is the v11 marketing wedge.

**What to read.** The TechCrunch article + the Loft Orbital / NASA JPL deployment notes. Key sections: (a) the constrained-device framing ("designed to run on limited hardware far from a data center"); (b) the Earth-observation use case (find areas of interest in response to natural language queries); (c) the prompt structure we should benchmark LFM2.5-VL-450M against.

**Key claim to verify.** The in-orbit prompt structure is reproducible on LFM2.5-VL-450M on the wearable.

**Open-source artefacts.** Gemma 3 weights on HuggingFace (Apache-2.0). The in-orbit deployment is not open-source, but the prompt structure is.

**Reading time.** 1-2 hours for the TechCrunch article + 2-3 hours for the prompt-structure spike.

**Source.** https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/

---

## Honorable mentions (12 papers + 2 industry reports)

1. **OpenLife (arXiv 2606.31046, June 30 2026)** — 6 LLM agents × 12 weeks in the open × first self-earned external income. Validates the "society of asynchronous processes" pattern.
2. **A-Evolve-Training (arXiv 2606.20657, June 2026)** — frontier-scale autonomous post-training (30B Nemotron, 0.86 vs 0.87 on NVIDIA Nemotron-Reasoning Challenge). Closed-source.
3. **Diagnosing the Memory-Update Gap (arXiv 2606.27472, June 2026)** — frontier models drop 92% → 77% on supersession tasks when forced to use bounded self-maintained memory. The fundamental gap for any production memoryd.
4. **SIA (arXiv 2605.27276, MIT, May 2026)** — self-improving loop with harness and weight updates. Only MIT-licensed open-source RSI counter-narrative to Anthropic Dreaming.
5. **Kokoro-82M (Apache-2.0, 2026)** — the SOTA edge TTS. 100+ languages, 82M params, on-device. **Watch the Kokoro GitHub releases.**
6. **HybridCodec (Yutori 2026-06-30 brief)** — discrete + continuous representations for efficient speech language models. v2.0 watch.
7. **Continual Harness (Prime Intellect, ARC-AGI-3, June 30 2026)** — self-improving agent with internal world model of task rules. ARC-AGI-3 is the new test-time-learning benchmark.
8. **Situation Perception (arXiv 2606.30481, June 2026)** — 3-component recipe for ASI: abstract prediction + long-term compressed memory + active learning.
9. **Active Inference as Test-Time Scaling Law (Debbah et al., June 2026)** — physical AI test-time scaling via surprise minimization.
10. **Physical AI 2.0 (Atomathic white paper, July 1 2026)** — world models → physical state recovery → reasoning → action. Embodied AI architectural sequence.
11. **Proactive Systems in HCI and AI (arXiv 2606.25149, June 2026)** — survey of proactive-agent design challenges: timing, appropriateness, user control, transparency, trust. **NEW v11.**
12. **Gemma 3 in orbit (TechCrunch, June 15 2026)** — the on-device VLM in space. **NEW v11. Already #5, listed here for reference.**

**Industry reports (2):**
- **Microsoft Build 2026 lineup (June 2 2026)** — MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Transcribe-1.5, MAI-Voice-2, Microsoft Scout (built on OpenClaw).
- **Anthropic Mythos 5 / Fable 5 export controls (July 1 2026)** — Mythos 5 gated to US Glasswing partners; Fable 5 global. The closed-source competitor to our open-weights thesis.

---

**End of v11 papers-to-read.**
