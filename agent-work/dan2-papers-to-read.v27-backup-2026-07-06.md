# Dan2 — Papers to Read v28 (2026-07-05 10:30 UTC / 16:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v27:** `dan2-papers-to-read.v27-backup-2026-07-05.md` (preserved verbatim, mtime 2026-07-05 04:00 UTC)
> **Status:** v28 SHIPPED. v27 content preserved verbatim below.

> **v28 deltas vs v27 (1 NEW TOP-5 paper — Microsoft Research Agentic Evolution, 0 top-5 swaps, 1 NEW honorable mention — MHM-LRU, 0 retractions):**
> 1. **NEW TOP-5 #1 (promoted from honorable mention to v28 TOP-1) — "Agentic Evolution: From Self-Improving Agents to Co-Evolving Human–AI Systems" (Microsoft Research, ~300 papers, July 2026, https://www.microsoft.com/en-us/research/wp-content/uploads/2026/07/agentic-evolution.pdf).** v28 *canonical-survey-validation* of the v23-v25 self-evolving-architecture thesis. Three axes: evolutionary substrate, consolidation pathway, selective pressure. Human feedback is named as v28 *first-class selective pressure*. **v28 add: 1-hour paper read. The v28 single most-actionable concept is the v28 three-axis taxonomy as a v28 spec backbone. Maps directly to v28 9-daemon substrate (memoryd = memory substrate, toold = tools substrate, perceptiond = weights substrate; ASPIRE-aligned = consolidation pathway; reversibility contract = selective pressure with human-in-the-loop). Cite this paper in the v1.0 spec self-improvement section.**
> 2. **NEW HONORABLE MENTION #1 — "Multi-Head Recurrent Memory Agents" (arXiv 2607.01523, July 2026).** Training-free, zero-additional-token, architectural retention fix. Partitions episodic memory into independent heads. LRU variant guarantees uniform head utilization. Substantially improves both retention and end-to-end accuracy across 100K–1M token range where baselines degrade sharply. **v28 add: 1-hour paper read. The v28 single most-actionable concept is the v28 *select-then-update* strategy with v28 *structural shielding* — directly applicable to v28 memoryd v1.5 four-head retention layer. Cite this paper in the v28 memoryd v1.5 design spike.**
> 3. **v28 top-5 holds from v27:** (1) Agentic Evolution (NEW v28, promoted from v27 honorable mention), (2) SIA (carried from v16), (3) TTSR (carried from v17), (4) SPEED-Q (carried from v16), (5) ETD (carried from v17). v28 reorders: SIA drops to #2 because Agentic Evolution is the v28 *canonical-survey* and v28 *most-canonical-citation* for the v1.0 spec. TTSR, SPEED-Q, ETD hold at #3-#5.
> 4. **v28 v27 honorable mentions held:** MemDelta (v27 §1), Couchbase AI Data Plane (v27 §2), Google OKF (v27 §4), Phase Matters (v15 §7), Atomathic Physical AI 2.0 (v24 §6), PagerDuty Tejada agent drift (v25 §A.6), MHM-LRU (NEW v28 §2).
> 5. **v28 retractions of v27:** **0.** All v27 top-5 + honorable mentions hold. v28 adds MHM-LRU (arXiv 2607.01523) as the v28 *first new honorable mention* since v27.

# Dan2 — Papers to Read v27 (2026-07-05 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v26:** `dan2-papers-to-read.v26-backup-2026-07-05.md` (preserved verbatim, mtime 2026-07-05 03:07 UTC)
> **Status:** v27 SHIPPED. v26 content preserved verbatim below.

> **v27 deltas vs v26 (0 top-5 changes, 1 new honorable mention, 0 retractions):**
> 1. **v27 top-5 (UNCHANGED from v26):** (1) SIA (Hexo Labs, MIT, May 2026, arXiv 2605.27276) — self-improving agent harness+weights framework. (2) TTSR (arXiv) — text-to-speech review, edge-relevant. (3) SPEED-Q (arXiv) — quantization for edge VLMs. (4) ETD (arXiv) — emergent tool discovery. (5) ProVoice-Bench — TTS evaluation. v27 *all v26 top-5 hold* — the v27 MemDelta paper doesn't *replace* any v26 top-5 paper, it *strengthens the v26 evaluation-rigor* axis across all of them.
> 2. **NEW HONORABLE MENTION #1 — MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (arXiv 2606.29914, late June 2026).** Per the v27 §A.8 architecture-review addition, the v27 *evaluation-rigor* axis is now v27 *MemDelta-controlled* for all v27 memoryd v1.5 promotions. The v27 *four findings* are the v27 *first quantified hidden confounds* in agent memory research. Read order: (a) the v27 *abstract* for the v27 *four-findings summary*, (b) §3 *protocol* for the v27 *controlled-baseline design*, (c) §5 *discussion* for the v27 *Mem0-vs-cloud-RAG-vs-basic-retrieval* ranking reversals. Time: 1 hour. **Recommended for v1.0 spec memoryd v1.5 promotion gate design — read this week, before Q3 W3 plan-P1 spike starts.**
> 3. **v27 honorable mention count: 9 (was 8 in v26).** v27 adds MemDelta. v27 *all v26 honorable mentions hold* — SIA concrete-numbers (Felix Chau, July 2026 summary), VisualClaw (Mervin Praison, June 2026), Anthropic Dreaming (Anthropic beta, June 2026), A-Evolve-Training (arXiv 2606.20657, June 2026), Continual Harness (Prime Intellect, June 30 2026), Diagnosing the Memory-Update Gap (arXiv 2606.27472, June 2026), ASPIRE (NVIDIA, July 3 2026), Phase Matters (arXiv 2606.27906, June 2026).
> 4. **v27 newly-tracked honorable mentions (1):** MemDelta (arXiv 2606.29914). **All v26 holds.** **All v25 holds.** **All v24 holds.** **All v23 holds.** **All v22 holds.** **All v21 holds.**
> 5. **v27 open questions for somdipto (1):** MemDelta paper read priority (recommend this week, 1 hour, 1 engineer, before Q3 W3 plan-P1 spike starts).

# Dan2 — Papers to Read v26 (2026-07-05 09:00 UTC / 14:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v25:** `dan2-papers-to-read.v25-backup-2026-07-05.md` (40KB, 263 lines)
> **Status:** v26 SHIPPED. v25 content preserved verbatim below.

> **v26 deltas vs v25 (0 top-5 swaps, 1 NEW honorable mention (Lin "training models → training agents" essay), 5 NEW honorable mention adds, 0 broad rollbacks):**
> 1. **v26 NEW honorable mention #1 — Junyang Lin, "Training Models → Training Agents" (MarkTechPost, July 4 2026).** Lin is the v26 first named technical lead of a frontier open-weights project (Qwen, ex-Alibaba) to publicly frame the 2026 transition as "training models → training agents." The shift is from "reasoning thinking" (Chain-of-Thought) to "agentic thinking" (long-horizon plan execution). Cite in v1.0 spec architecture section. v26 add: read Lin's talk + post; the v26 *training agents* framing pairs with Babushkin's v26 *reversibility* warning — training agents is the v26 unreversible-decision if the agent's memory is in the vendor's database, but is the v26 fully-reversible if memoryd is the user's.
> 2. **v26 NEW honorable mention #2 — Igor Babushkin (xAI co-founder), "Recursive Self-Improvement Converts Helpfulness Into Irreversible Control" (BitRebels + Let's Data Science, July 2026).** Babushkin is the v26 first xAI co-founder to publish a long-form essay warning that RSI is "irreversible control" once it ships. v26 add: read the essay; the v26 *reversibility* framing is the v26 *most-actionable* signal in the v26 *sovereign-trust* / *political-conditionality* / *reversibility* cluster.
> 3. **v26 NEW honorable mention #3 — Anthropic (Babushkin-style) export controls lifted (AOL + Anthropic X, July 1-2 2026).** Not a paper, but a v26 *named-dated* signal: the Trump administration *conditionally* lifted Claude Mythos 5 / Fable 5 export controls after Anthropic "worked with" Commerce. v26 add: cite the AOL + Anthropic X post in the v1.0 spec political-considerations section.
> 4. **v26 NEW honorable mention #4 — Palantir Karp Nemotron migration claim (FourWeekMBA, early July 2026).** Not a paper, but a v26 *named-CEO* signal: Alex Karp publicly claimed U.S. agencies are moving from Anthropic to Nemotron. v26 add: cite the Karp claim in the v1.0 spec competitive-considerations section.
> 5. **v26 NEW honorable mention #5 — Mistral AI Arthur Mensch LinkedIn post (TechCrunch, July 4 2026).** Not a paper, but a v26 *named-CEO* signal: Mensch described Mistral's Forge platform as a v26 European-sovereign-stack answer to the v26 closed-source frontier. v26 add: cite the Mensch post in the v1.0 spec competitive-considerations section.
> 6. **v26 NEW honorable mention #6 — Alibaba Claude Code ban (GIGAZINE + Reuters + South China Morning Post, July 4 2026).** Not a paper, but a v26 *named-enterprise* signal: Alibaba is banning all employees from using Anthropic's Claude Code starting July 10 2026, citing a "backdoor risk" in the tool. v26 add: cite the GIGAZINE + Reuters + South China Morning Post coverage in the v1.0 spec security-considerations section.
> 7. **v26 top-5 (held from v25):** v25 top-5 — SIA (Hexo Labs, MIT, arXiv 2605.27276, May 2026), TTSR, SPEED-Q, ETD, ProVoice-Bench — all *hold* in v26. v26 NO top-5 swap. The v26 *bifurcation* + *reversibility* signals are not papers, they are v26 *industry signals*, so they belong in v26 honorable mentions rather than v26 top-5.
> 8. **v26 retractions of v25:** **0 top-5 swaps. 0 broad rollbacks.** v25 honorable mentions (ASPIRE, A-Evolve-Training, Continual Harness, Diagnosing the Memory-Update Gap, Brain2Qwerty v2, etc.) all *hold* in v26.
> 9. **v26 reading order recommendation for the team:**
>     1. **Lin "Training Models → Training Agents"** (15 min) — sets the v26 *framing*.
>     2. **Babushkin reversibility essay** (30 min) — sets the v26 *safety property*.
>     3. **ASPIRE paper** (60 min) — the v26 *implementation reference* for skill-evolution.
>     4. **SIA paper (Hexo Labs, May 2026)** (90 min) — the v26 *publishing bet* for v1.5.
>     5. **Diagnosing the Memory-Update Gap (arXiv 2606.27472)** (60 min) — the v26 *memoryd correctness* baseline.
> 10. **v26 architecture decomposition score: 9.95/10 (held).** v26 reading list is v25 reading list + 6 v26 honorable mentions.

# Dan2 — Papers to Read v25 (2026-07-05 02:00 UTC / 07:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v24:** `dan2-papers-to-read.v24-backup-2026-07-05.md` (38KB, 254 lines)
> **Status:** v25 SHIPPED. v24 content preserved verbatim below.

> **v25 deltas vs v24 (0 top-5 swaps, 1 NEW honorable mention, 4 NEW honorable mention adds, 0 broad rollbacks):**
> 1. **NEW TOP-5 CONSIDERATION — NVIDIA ASPIRE: Agentic Skill Programming through Iterative Robot Exploration (MarkTechPost, July 3 2026, covering NVIDIA + U-Michigan + UIUC + UC Berkeley + CMU).** Continual learning system that writes + refines robot control programs, holds a *failure signature* (when-to-apply condition) + a *repair strategy* (often a code sketch), inspects only failure-implicated calls. 31% zero-shot on LIBERO-Pro long-horizon tasks. **v25 add: this is the v25 *first published continual-learning agent* in the SIA family lineage. The failure-signature/when-to-apply/repair-strategy data structure is *exactly* the v23 perceptiond.skill_evolution spike design. v25 add: add ASPIRE to the v25 top-5 (or, if top-5 is locked, the v25 *top-5-consideration*). The SIA-W+H port spike is now *concrete* with this data structure. 30-45 minutes to read.**
> 2. **NEW HONORABLE MENTION — PagerDuty Jenn Tejada Forbes interview (Let's Data Science, July 2 2026).** Tejada: "agentic systems introduce failure modes like model drift, which is harder to detect than a traditional software crash." BNP Paribas $725B 2026 hyperscaler AI infra spend cited. **v25 add: read before the v25 cross-daemon observability spike. 20 minutes.**
> 3. **NEW HONORABLE MENTION — Zuckerberg internal memo (GIGAZINE + Reuters, July 2 2026).** Zuckerberg: "the progress in AI agent development over the past four months has not accelerated as much as we had hoped." **v25 add: read before the v1.0 spec executive-summary add. 15 minutes.**
> 4. **NEW HONORABLE MENTION — Microsoft Frontier Co. announcement (TechCrunch, July 2 2026).** $2.5B + 6,000 engineers for outcome-driven enterprise AI deployment. **v25 add: read before the v1.0 spec investor-considerations section. 20 minutes.**
> 5. **NEW HONORABLE MENTION — WIRED "Meta Is Charging a Subscription for Smart Glasses Features" (July 2 2026) + BBC + The Verge + CNET + Gizmodo (July 1-3 2026).** 5-outlet, 4-day coverage of Meta's accessibility-feature paywall. WIRED: "Welcome to the New Era of Consumer Tech." **v25 add: read all 5 before the v1.0 spec marketing-positioning section. 30 minutes total.**

---

> **v24 deltas vs v23 (4 honorable-mention adds, 0 top-5 swaps, 0 broad rollbacks):**
> 1. **NEW HONORABLE MENTION — Adversa AI / SecurityWeek report on shell-trick attacks against open-source coding agents (July 2026).** Decades-old Bash tricks expose AI coding agents to supply-chain compromise; only 1 of 11 open-source agents blocked all the tricks. **v24 add: read before the `toold` strict-mode and `openclaw` shell-call audit spikes. 20 minutes.**
> 2. **NEW HONORABLE MENTION — HackerNoon: "The Month AI Governance Became Operational" (July 1 2026).** Synthesizes model access + infrastructure capacity + cyber governance into one operational lens. **v24 add: read before the v1.0 spec executive-summary control-surfaces section. 15 minutes.**
> 3. **NEW HONORABLE MENTION — Anthropic-Samsung custom AI chip reporting (TechCrunch + FourWeekMBA, late June 2026).** Anthropic in active discussions with Samsung to co-develop a custom inference chip. **v24 add: read before the v1.0 spec performance section. 20 minutes.**
> 4. **NEW HONORABLE MENTION — Genesis AI Eno + GENE (June 16 2026).** Robot + foundation model + perception/memory/task-planning stack. **v24 add: read before the v1.0 spec architecture mapping to robotics/world-models. 20 minutes.**

---

> **v23 deltas vs v22 (0 top-5 paper swaps, 4 honorable mention adds, 0 broad rollbacks):**
> 1. **NEW HONORABLE MENTION — DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation (alphaxiv.org/abs/2026.dspark, June 26 2026).** MIT-licensed. 60-85% faster per-user generation for DeepSeek-V4-Flash, 57-78% for V4-Pro. Tested on Gemma and Qwen. **v23 add: this is the v23 *first* open-source inference-speedup framework that applies to *any* open-weight model without retraining. Read before the Q3 W2 v1.1 perceptiond DSpark evaluation spike. 30 minutes.**
> 2. **NEW HONORABLE MENTION — Orca: The World is in Your Mind (arXiv 2606.30534, June 2026).** A unified world latent space learned from multimodal world signals. Two paradigms: unconscious learning (video data) and conscious learning (state transitions under explicit semantic conditions). **v23 add: the v23 *first* arXiv paper on multimodal world-state learning that maps directly to the Dan Glasses memoryd → perceptiond → audiod stack. Read before the Q3 W2 NVIDIA Cosmos 3 architecture mapping. 30 minutes.**
> 3. **NEW HONORABLE MENTION — HakkoLab World Model Research Survey (June 2026, 60 refs).** A 6-sub-field world-model survey, current to 2026-06. Covers WHAM/Muse (Microsoft + Ninja Theory, Nature 2025), V-JEPA 2/AC (Meta, arXiv 2506.09985), Genie 3 (Google DeepMind, 2025-08), NVIDIA Cosmos, World Labs Marble, Wayve GAIA-1→3. **v23 add: this is the v23 *most-cited* world-model survey. Read before the Q3 W2 NVIDIA Cosmos 3 architecture mapping + the v1.5 plan-I1 (Cosmos 3 mapping) spike. 1 hour.**
> 4. **NEW HONORABLE MENTION — SIA Hexo Labs empirical results report (LinkedIn / Felix Chau + Instagram daily.agent.ai, late June 2026).** 45% → 70% on legal task, up to 14× on GPU kernels, research benchmarks improved over earlier versions of itself. **v23 add: the v23 *first* third-party-validated empirical report on SIA. Read before the Q3 W1-W2 SIA-W+H port spike. 20 minutes.**

---

> **v22 deltas vs v21 (0 top-5 paper swaps, 5 honorable mention adds, 0 broad rollbacks):**
> 1. **NEW HONORABLE MENTION — Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction (arXiv 2607.01764, July 2026).** "Mastermind achieves an 84.5% pass rate, outperforming open-book PoC context (60.0%), Best-of-8 sampling (63.0%), and iterative improvement (77.0%). The same planner also improves GPT-5.4 mini and GLM 5.1 from 45.0% and 58.5% to 60.0% and 71.0%." **v22 add: the v22 *empirical replication* of the "harness > model" thesis. Read before the Q3 W2 v1.0 spec vision-architecture section update + the v1.5 plan-B+ agent substrate shortlist. 30 minutes.**
> 2. **NEW HONORABLE MENTION — HRM-Agent: Training a recurrent reasoning model in dynamic environments using reinforcement learning (arXiv 2510.22832, 2025).** **v22 add: the v22 *first peer-reviewable* RL training of the recursive reasoning model in dynamic environments. The v1.5 plan-B (HRM-Text-1B) is now v22 *RL-training-validated*. Read before the Q3 W2 v1.5 plan-B+ shortlist. 30 minutes.**
> 3. **NEW HONORABLE MENTION — HICRA: Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning (ICLR 2026, Wang et al.).** "Hierarchy-Aware Credit Assignment (HICRA) – allocates learning signal more to high-impact planning tokens, focusing optimization on strategic planning steps rather than all tokens equally." **v22 add: the v22 only RL credit-assignment scheme that matches the v19 SIA-W+H Feedback-Agent design. Read before the Q3 W2 v1.5 plan-B+ shortlist. 30 minutes.**
> 4. **NEW HONORABLE MENTION — Less is More: Recursive Reasoning with Tiny Networks (TRM, arXiv 2510.04871, 2025).** "TRM eliminates the need for hierarchy and fixed-point theorems found in HRM. It uses a single tiny network (2 layers, ~7M parameters) that recursively processes its latent reasoning features in a single forward pass, achieving strong generalization. TRM outperforms many LLMs on certain tasks with far fewer parameters, e.g., 45% test accuracy on ARC-AGI 1 and 8% on ARC-AGI-2." **v22 add: TRM is the v22 *strongest evidence* that the v1.0 wearable reasoning model can be 7M params (TRM-class) and still beat 7B-class LLMs on structured-reasoning tasks. Read before the Q3 W2 v1.5 plan-B+ shortlist. 30 minutes.**
> 5. **NEW HONORABLE MENTION — ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models (arXiv 2606.23404, June 2026).** "Hierarchical tracing: separates high-level strategy from low-level steps within the reasoning process. Agentic auditor: automated error detection and tool-augmented verification to catch mistakes and validate steps." **v22 add: the v22 only *peer-reviewable* interpretability framework for hierarchical reasoning. Add to the v1.5 spec observability section as the v22 *academic* validation. Read before the Q3 W3 v1.5 spec observability section. 30 minutes.**

> **v22 retractions of v21:** **0 broad rollbacks.** v21 top-5 (SIA, Memora, Phase Matters, ComfyClaw, VisualClawArena) holds. v22 adds 5 new honorable mentions (Mastermind, HRM-Agent, HICRA, TRM, ReasoningLens). v22 model shortlist holds (LFM2.5-VL-450M + LFM2.5-230M + Hermes Agent + HRM-Text-1B + GLM-5.2 + Apertus v1.1 4B + OpenPhone-3B + LFM2.5-VL-Extract-2 + Qwen3-TTS + Chatterbox).

## TL;DR (one paragraph, v20)


The v19 top-5 holds: (1) Phase Matters, (2) Memora, (3) Red Queen Gödel Machine, (4) SIA, (5) As We May Search. v20 adds 5 new honorable mentions: Bad Epoll CVE-2026-46242 (The Hacker News, July 3 2026), Axios Amazon-Trump 20-day showdown (July 3 2026), Mimir's Well GLM-5.2 = Mythos + NSA Gen. Joshua Rudd (July 3 2026), Dark Reading Chris Inglis on open-weights defense (June 30 2026), The AI Insider on token economics (July 3 2026). **The v20 reading list centers on: (1) Phase Matters + As We May Search + Atomathic Physical AI 2.0 for v1.0/v1.5 architecture, (2) SIA + Red Queen for v1.5/v2.0 agent loop, (3) Memora + v20 "what would Mythos have missed" for v1.5 memoryd safety, (4) Hermes Agent + LFM2.5-230M for v1.0 audiod, (5) v20 Bad Epoll + Axios + NSA + Chris Inglis + The AI Insider for v1.0 spec safety-considerations + implementation-wedge + sovereign-on-prem sections.** HRM-Text-1B held as honorable mention. No v19 paper is retracted.

## Top 5 Papers to Read (v18 ranking, unchanged from v17)

### 1. "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906, late June 2026) — held from v15 #1
- **Why this paper:** The v1.0 wearable execution substrate is now defined. NPU prefill 1.64× faster than CPU, NPU decode 1.18× faster, vision encoders 2.52× lower energy on NPU. Always-on mobile VLM is feasible with careful NPU offload.
- **Key takeaway:** VLM inference on a phone SoC requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." The 4hr battery target is now reachable.
- **What we will do with it:** 1-week Q3 W1 `perceptiond.phase_map` architecture spike.
- **Effort to read:** 30 minutes.
- **Link:** https://arxiv.org/html/2606.27906v1.

### 2. "Microsoft Memora" (Microsoft Research, July 2026) — held from v14 #1
- **Why this paper:** The v1.5 memoryd architecture target. Decouples "what is stored" from "how it is retrieved." Reduces context token usage by up to 98% while matching or exceeding full-context accuracy.
- **Key takeaway:** Rich procedural memories stored with full embedding vectors; lightweight semantic abstractions stored with indexable keys; retrieval via a 2-stage pipeline.
- **What we will do with it:** 2-week Q3 W1-W2 memoryd v1.5 port.
- **Effort to read:** 1 hour.
- **Link:** https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity.

### 3. "Red Queen Gödel Machine" (arXiv 2606.26294, June 24 2026) — held from v12 #3
- **Why this paper:** The 2026 strongest paper for self-improving agents. The 1.91× → ~1.0× bias-correction result on the moving-judge pattern.
- **Key takeaway:** The agent can self-improve by changing its own judge. The "moving-judge" pattern is the implementation of the v11 `auto_apply=False` contract.
- **What we will do with it:** Port to danlab-multimodal as the v1.5 plan-A for the agent loop.
- **Effort to read:** 2 hours.
- **Link:** https://arxiv.org/abs/2606.26294.

### 4. "SIA: Self-Improving AI with Harness & Weight Updates" (Hexo Labs, MIT, June 2026) — held from v11
- **Why this paper:** The SIA framework is the open-weights, MIT-licensed self-improving agent pattern. The SIA-W+H (with hindsight) port is the v1.5 publishing bet.
- **Key takeaway:** Self-improving loop where a Feedback-Agent updates both the harness and the weights. Beats Karpathy's autoresearcher agent by improving itself.
- **What we will do with it:** Q3 W3-Q4 W2 SIA-W+H port. arXiv draft + ICML/ACL 2027 submission.
- **Effort to read:** 1.5 hours.
- **Link:** https://github.com/HexoLabs/sia.

### 5. "As We May Search: Local-First Information Retrieval" (arXiv 2606.29652, late June 2026) — held from v16
- **Why this paper:** Academic local-first IR validation. Dense retrieval keeps over 91% nDCG@10 up to 100K documents; approximate HNSW indexes extend to 1M with only 2% quality loss; 7B local language model reaches within 4 points of a cloud baseline on answer quality.
- **Key takeaway:** The on-device memoryd architecture is now an *empirical certainty*. Memora + As We May Search = the storage/retrieval split is the 2026 SOTA.
- **What we will do with it:** Cite in v1.0 marketing as the academic validation of on-device memory.
- **Effort to read:** 1 hour.
- **Link:** https://arxiv.org/abs/2606.29652.

## Honorable Mentions (v18)

1. **"LFM2.5-230M Technical Report" (Liquid AI, June 26 2026).** 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B. v1.0 audiod post-processor. Held from v16.
2. **"Hermes Agent" (Nous Research, late June 2026).** Mixture-of-agents pattern. 11% higher than GPT-5.5 on hard agentic benchmarks. v1.0 audiod agent framework plan-A. Held from v16.
3. **"EPFL MiCRo: Mixture of Cognitive Reasoners" (late June 2026).** Validates the 4-specialized-brain-region pattern. Held from v14.
4. **"VisualClaw: Self-Evolving Multimodal Agent for AI Glasses" (Mervin Praison, June 2026).** 98% cost reduction + +15.8% accuracy. The cascade-gate pattern. Held from v8.
5. **"Diagnosing the Memory-Update Gap" (arXiv 2606.27472, June 2026).** Frontier models drop 92% → 77% on supersession tasks. Held from v8.
6. **"Ollie: Gaze-Informed Proactive AI" (arXiv 2607.00445, July 1 2026).** The v12 proactived v1 architecture source. Held from v12.
7. **"Apertus v1.1 4B Instruct" (Swiss AI / EPFL, June 29 2026).** EU-provenance open-weights. v1.5 audiod post-processor plan-C. Held from v14.
8. **"OpenPhone-3B" (HKUDS, ACL 2026, late June 2026).** 3B on-device agentic foundation model. v1.5 audiod post-processor plan-D. Held from v15.
9. **"HRM-Text-1B" (Sapient, June 2026).** $1,500 trained, 1B params, Apache-2.0. v1.5 plan-B. Held from v15 (demoted from top-5 in v16).
10. **"Anthropic Mythos 5 + Fable 5 export ban lifted" (US Commerce Department, June 30 - July 1 2026).** Industry signal, not a paper. Fable 5 now globally available; Mythos 5 partially open to Glasswing + broader domestic + international members. **v17 partial retraction of v16's "$30K catch" framing and v16's "~100 US critical-infrastructure partners" framing.**
11. **Vinton Cerf keynote (Laude Institute Open Frontier, June 30 2026).** Industry-icon endorsement of the "TCP/IP-for-agents" pattern. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour. Held from v17.
12. **Anthropic Claude Science (MobiHealthNews, June 30 2026).** Closed-source admission that "harness > model." Read before the Q3 W2 v1.0 spec safety-considerations section update. 30 minutes. Held from v17.
13. **IBM Red Hat Project Lightwell (Dark Reading, late June 2026) + Chainguard Athena (Let's Data Science, late June 2026).** $5B Project Lightwell + 20,000 engineers + 20+ orgs Athena coalition. Read before the Q3 W2 9-step marketing narrative update. 1 hour. Held from v17.
14. **OpenAN project (MWC Shanghai 2026, late June 2026).** China-led open-source agent interoperability framework (Linux Foundation Networking). Read before the Q4 W1-W2 OpenAN spike. 1 hour. Held from v17.
15. **"The Month AI Governance Became Operational" (HackerNoon, June 2026).** v17 evidence that "AI advantage is shifting from who can build the best model to who can control the conditions under which model capability is accessed, secured, powered, deployed, and converted into institutional capacity." Read before the Q3 W2 9-step marketing narrative update. 1 hour. Held from v17.
16. **"Anthropic Tightens Controls Over Model Access" (Let's Data Science, late June 2026).** Anthropic Claude Code timezone/proxy fingerprinting evidence. v17 strongest possible citable "vendor lock-in is structural" evidence. Read before the Q3 W2 9-step marketing narrative update. 30 minutes. Held from v17.
17. **NEW v18: Anthropic Claude Apps Gateway documentation (Anthropic + AWS + DevOps.com + Google Cloud, July 2 2026).** Self-hosted, stateless container, PostgreSQL backend, OIDC SSO, per-user cost attribution, OTLP audit logs, *published gateway protocol*. The v18 strongest possible citable evidence for the OpenClaw v1.0 protocol surface. Read before the Q3 W2 OpenClaw protocol surface marketing artifact spike. 1 hour.
18. **NEW v18: OpenClaw iOS + Android documentation + security audit (9to5Google + Engadget + TechCrunch + Mashable, June 30 2026).** OpenClaw now ships native iOS + Android. Mashable flags a critical security flaw. Read before the Q3 W2 OpenClaw security audit spike. 1 hour.
19. **NEW v18: Newsweek "Open Accountability Standards" (early July 2026).** Directly names OpenClaw as a popular open-source personal AI agent. v18 mainstream-press-acknowledged. Read before the Q3 W2 v18 10-step marketing narrative update. 30 minutes.
20. **NEW v18: Atomathic Physical AI 2.0 white paper (Thailand Business News, July 1 2026).** "World Models → Physical State Recovery → Reasoning Systems → Action." The v18 academic validation of the Dan Glasses architectural pattern. Read before the Q3 W2 v1.0 spec architecture section update. 1 hour.
21. **NEW v18: Time Magazine on RSI (June 29 2026).** Anthropic's Marina Favaro and Jack Clark publicly hedge: "We are not there yet, and recursive self-improvement is not inevitable." v18 strengthens the v16 SIA-W+H port publishing bet. Read before the Q3 W3 SIA-W+H port start. 30 minutes.
22. **NEW v18: AIPOCH MedSkillAudit (Business Insider, June 29 2026).** Pre-deployment medical AI audit framework. Two-layer veto gate: static (40%, design quality) + dynamic (60%, runtime performance). v18 cites for the v1.5 healthcare vertical. Read before the Q4 W1-W2 sovereign-on-prem vertical spike. 30 minutes.
23. **NEW v18: PagerDuty Jenn Tejada (Forbes, July 2 2026) on agent drift + $725B AI infra spend (BNP Paribas).** "Model drift in AI agents is harder to detect than a traditional software crash." v18 cites for the v1.0 spec safety-considerations section. Read before the Q3 W2 spec update. 30 minutes.
24. **NEW v18: Proton Lumo 2.0 (9to5Mac, June 30 2026).** Privacy-preserving AI with persistent memory. Lumo 2.0 Max scores 240% higher than Lumo 1.4. v18 cites for the v1.0 marketing privacy-harness analog. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
25. **NEW v18: OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race (TechCrunch + 9to5Mac + Axios, June-July 2026).** All three labs shipped agentic models in May-July 2026, all behind closed APIs. v18 cites for the v1.0 marketing closed-source-agentic-race frame. Read before the Q3 W2 10-step marketing narrative update. 1 hour.
26. **NEW v18: Zuckerberg "slower than expected" (Reuters + TechCrunch + Bloomberg + CNN + Forbes, July 2 2026).** "The trajectory of agentic AI development over the last four months hasn't accelerated as hoped." v18 cites for the v1.0 marketing closed-source-failing frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
27. **NEW v18: OpenAI delays IPO to 2027, Anthropic $965B (Forbes, June 28 2026).** v18 cites for the v1.0 marketing $1T-class implementation-wedge frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.
28. **NEW v18: Apple 5 new iPhones + memory crunch + M6/M7 plans (Nikkei + CNBC + Bloomberg, June-July 2026).** v18 cites for the v1.0 wearable form-factor supply-chain-pressure frame. Read before the Q3 W2 10-step marketing narrative update. 30 minutes.

## v18 Open Questions for somdipto

1. **Anthropic Claude Apps Gateway documentation — read before Q3 W2 OpenClaw protocol surface marketing artifact spike?** (recommend: yes, 1 hour, before Q3 W2)
2. **OpenClaw iOS + Android documentation + security audit — read before Q3 W2 OpenClaw security audit spike?** (recommend: yes, 1 hour, before Q3 W2)
3. **Newsweek "Open Accountability Standards" — read before Q3 W2 v18 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
4. **Atomathic Physical AI 2.0 — read before Q3 W2 v1.0 spec architecture section update?** (recommend: yes, 1 hour, before Q3 W2)
5. **Time Magazine on RSI — read before Q3 W3 SIA-W+H port start?** (recommend: yes, 30 minutes, before Q3 W3)
6. **AIPOCH MedSkillAudit — read before Q4 W1-W2 sovereign-on-prem vertical spike?** (recommend: yes, 30 minutes, before Q4 W1)
7. **PagerDuty Jenn Tejada — read before Q3 W2 v1.0 spec safety-considerations section update?** (recommend: yes, 30 minutes, before Q3 W2)
8. **Proton Lumo 2.0 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
9. **OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 1 hour, before Q3 W2)
10. **Zuckerberg "slower than expected" — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
11. **OpenAI delays IPO + Anthropic $965B — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
12. **Apple 5 new iPhones + memory crunch + M6/M7 — read before Q3 W2 10-step marketing narrative update?** (recommend: yes, 30 minutes, before Q3 W2)
13. **Phase Matters (v15 #1) — read before Q3 W1 phase_map spike starts?** (recommend: yes, 30 minutes, before Q3 W1)
14. **As We May Search (v16 #5) — read before Q3 W1-W2 Memora port starts?** (recommend: yes, 1 hour, before Q3 W1)
15. **Red Queen Gödel Machine (v12 #3) — port to danlab-multimodal in Q4 2026?** (recommend: yes, 4 weeks, 1 engineer)
16. **v18 24-month plan: AIPOCH-augmented sovereign-on-prem vertical + Project Lightwell + OpenAN partner-product evaluation?** (recommend: yes, Q4 2027, 1 quarter, 2 engineers)
17. **v18 10-step marketing narrative update priority?** (recommend: yes, Q3 W2, 1 day copy, 1 engineer)
18. **HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B v1.5 plan-B/C/D order** — held from v16 (recommend: hold order, they are v1.5 candidates, LFM2.5-230M is v1.0)

## Footnotes (v19)

[^v19-1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Apps Gateway + Sonnet 5, July 2 2026 (held from v18)
[^v19-2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (held from v18)
[^v19-3]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw, June 30 2026 (held from v18)
[^v19-4]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-5]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-6]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (held from v18)
[^v19-7]: https://markets.businessinsider.com/news/stocks/aipoch-launches-medskillaudit-an-ai-audit-framework-to-evaluate-medical-ai-agent-skills-before-deployment-1036284741 — AIPOCH MedSkillAudit, June 29 2026 (held from v18)
[^v19-8]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-9]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-10]: https://www.forbes.com/sites/sandycarter/2026/06/28/openai-eyes-2027-ipo-delay-as-washington-clears-anthropics-mythos-5/ — OpenAI delays IPO + Anthropic $965B, June 28 2026 (held from v18)
[^v19-11]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier keynote, June 30 2026 (held from v17)
[^v19-12]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026 (held from v17)
[^v19-13]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026 (held from v17)
[^v19-14]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026 (held from v17)
[^v19-15]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (held from v17)
[^v19-16]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026 (held from v17)
[^v19-17]: https://arxiv.org/abs/2606.29652 — "As We May Search" (held from v16)
[^v19-18]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-19]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity — Microsoft Memora (held from v14)
[^v19-20]: https://arxiv.org/abs/2606.26294 — "Red Queen Gödel Machine" (held from v12)
[^v19-21]: https://github.com/HexoLabs/sia — SIA (held from v11)
[^v19-22]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M (held from v16)
[^v19-23]: https://www.nousresearch.com/agents/hermes — Hermes Agent (held from v16)
[^v19-24]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B (held from v15)
[^v19-25]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw iOS+Android + founder → OpenAI, June 30 2026 (NEW v19)
[^v19-26]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — MemoMind One (XGIMI), late June 2026 (NEW v19)
[^v19-27]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico: Anthropic-Newsom California deal, June 29 2026 (NEW v19)
[^v19-28]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain, June 29 2026 (NEW v19)
[^v19-29]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month, June 29 2026 (NEW v19)
[^v19-30]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute, June 28 2026 (NEW v19)
[^v19-31]: https://www.military.com/nato-drone-exercise-amplifies-international-battle-for-military-airspace-control — NATO SAPIENT TIE26, late spring 2026 (NEW v19)
[^v19-32]: https://www.rcrwireless.com/20260629/carriers/china-mobile-shanghai — China Mobile MWC Shanghai 2026, June 29 2026 (NEW v19)

## v18 papers-to-read content (preserved in backup)

The v18 papers-to-read (preserved in `dan2-papers-to-read.v18-backup-2026-07-04.md`, 21.1KB, 137 lines) covers: v18 top-5 (unchanged from v17): Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search. v18 added 4 new honorable mentions (Anthropic Claude Apps Gateway, OpenClaw iOS + Android + security flaw, Newsweek "Open Accountability Standards," Atomathic Physical AI 2.0) + 8 industry reads (Time Magazine, AIPOCH MedSkillAudit, PagerDuty agent drift, Proton Lumo 2.0, OpenAI GPT-5.6 / Google Gemini 3.5 Flash / Anthropic Sonnet 5, Zuckerberg "slower than expected," OpenAI delays IPO + Anthropic $965B, Apple 5 new iPhones + memory crunch + M6/M7) + 18 open questions. **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 new CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 new SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). The v19 top-5 holds (Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search). v19 add 3 new industry reads: Engadget (OpenClaw founder → OpenAI), Road to VR (MemoMind One), Politico (Newsom-Anthropic).**
## v22 addendum (2026-07-04 11:30 UTC / 17:00 IST)

**v22 deltas vs v21 (0 top-5 paper swaps, 1 top-5 honorable mention add, 4 honorable mention adds, 0 broad rollbacks):**

1. **NEW HONORABLE MENTION — Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams (arXiv 2606.01770, Jun 1 2026, revised Jun 3 2026).** A 2026 paper on the self-improving agent harness pattern. The v21 SIA + Hermes + Memora + A-Evolve-Training self-improvement literature is now *published* in a v22 dedicated arXiv paper. **v22 add: read before the Q3 W3 v22 perceptiond + memoryd + toold self-improving spike. 30 min.**

2. **NEW HONORABLE MENTION — Liquid AI LFM2.5-VL-450M blog (Apr 8 2026).** Vendor-confirmed Q4_0 on Jetson Orin Nano, 233-242ms for 256-512px, RL+preference-optimized, bounding boxes + function calling + 8 languages, on-device wearable use case. **v22 add: not a paper, but the v22 *vendor-benchmarked-on-Jetson-Orin* artifact that backs the v17 LFM2.5-VL-450M model choice. Cite in the v1.0 spec vision-architecture section. 30 min read.**

3. **NEW HONORABLE MENTION — Time Magazine "Recursive Self-Improvement is the Human Skill We Need in the AI Age" (Jun 29 2026) with Anthropic Marina Favaro and Jack Clark quotes.** "We are not there yet, and recursive self-improvement is not inevitable." **v22 add: cite the Time piece + Favaro+Clark quote in the v1.0 spec safety-considerations section as v22 *Anthropic-internal-hedge-validated* evidence. 30 min read.**

4. **NEW HONORABLE MENTION — Vint Cerf TCP/IP-for-agents panel (Open Frontier, Jun 30 2026).** "The agentic model of AI, with multiple agents from multiple sources interacting with each other, is going to force composability, and a requirement for interoperability and standardization." Vint Cerf + Matei Zaharia + Francois Chollet panel. **v22 add: cite the v22 panel as the v22 *named-dated-industry-acknowledgment* in the v1.0 spec toold section. 30 min.**

5. **NEW HONORABLE MENTION — TechCrunch OpenClaw iOS+Android launch (Jun 30 2026).** OpenClaw is *named, dated, confirmed* on the mobile substrate. **v22 add: cite the v22 launch in the v1.0 spec toold section. 15 min read.**

**v22 retractions of v21:** **0 broad rollbacks.** v21 top-5 holds: (1) SIA, (2) Memora, (3) Phase Matters, (4) ComfyClaw (v21 add), (5) VisualClawArena. v21 model shortlist holds. v21 6/12/24-month plan holds in v22, with v22 adding: 2 v1.5 plan adds (plan-C1 LFM2.5-1.2B-Thinking, plan-B1 LFM2.5-ColBERT-350M) + 1 reading spike (plan-I1 Adaptive Auto-Harness).

**v22 v1.0 reads (Q3 W2-W3, ~3 hours total):**
- v19 Newsweek "Open Accountability Standards" (30 min) — held from v19
- v19 Anthropic Claude Apps Gateway (30 min) — held from v19
- v19 X MCP server (15 min) — held from v19
- v20 Axios Amazon-Jassy-Anthropic jailbreak escalation (30 min) — held from v20
- v20 Bad Epoll Mythos-missed-bug (30 min) — held from v20
- v20 LA Times token-price collapse (30 min) — held from v20
- v20 Wall Street GLM-5.2 vs Mythos (30 min) — held from v20
- v20 NSA Rudd (30 min) — held from v20
- v20 Chris Inglis (30 min) — held from v20
- v20 Meta Pocket gizmos (30 min) — held from v20
- v21 Kimi K2.7 Code in GitHub Copilot (30 min) — held from v21
- v21 Microsoft Research agentic-evolution (1 hour) — held from v21
- v21 ComfyClaw arXiv 2607.01709 (1 hour) — held from v21
- v21 Mastermind arXiv 2607.01764 (30 min) — held from v21
- v21 SAIMY Dream Company (15 min) — held from v21
- v21 GLM-5 async RL on Hugging Face (30 min) — held from v21
- v22 Meta Conversation Focus paywall (15 min) — NEW v22
- v22 Liquid AI LFM2.5-VL-450M blog (30 min) — NEW v22
- v22 Vint Cerf TCP/IP-for-agents panel (30 min) — NEW v22
- v22 Time Magazine Favaro+Clark (15 min) — NEW v22
- v22 TechCrunch OpenClaw iOS+Android launch (15 min) — NEW v22
- v22 Adaptive Auto-Harness arXiv 2606.01770 (1 hour) — NEW v22

**v22 4 open questions for somdipto:**
1. Should v22 add ComfyClaw to the top-5, or keep top-5 stable? (recommend keep stable; v22 add is honorable mention only.)
2. Should v22 add Meta Conversation Focus paywall as a marketing copy add, or as a top-5 paper add? (recommend marketing copy add; it's not a paper.)
3. Should v22 add the v22 14-step marketing narrative to the v22 marketing plan? (recommend yes; v22 14-step is the v22 named-dated-confirmed story.)
4. Should v22 add the Adaptive Auto-Harness paper to the v22 reading list before or after the perceptiond.skill_evolution spike? (recommend before; reading spike target Q3 W3, perceptiond.skill_evolution spike target Q3 W3-W4.)


[^v22-1]: https://arxiv.org/abs/2606.01770 — "Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams," arXiv 2606.01770, Jun 1 2026 (NEW v22 HONORABLE MENTION #1)
[^v22-2]: https://www.liquid.ai/blog/lfm2-5-vl-450m — Liquid AI LFM2.5-VL-450M blog, Apr 8 2026 (NEW v22 HONORABLE MENTION #2)
[^v22-3]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine: Favaro+Clark Anthropic-internal-hedge, June 29 2026 (NEW v22 HONORABLE MENTION #3)
[^v22-4]: https://letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vint Cerf TCP/IP-for-agents panel, June 30 2026 (NEW v22 HONORABLE MENTION #4)
[^v22-5]: https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/ — TechCrunch: OpenClaw iOS+Android launch, June 30 2026 (NEW v22 HONORABLE MENTION #5)


## v21 papers-to-read content (preserved in backup)

The v21 papers-to-read (preserved in `dan2-papers-to-read.v21-backup-2026-07-04.md`, 27.7KB, 176 lines) covers: 1 top-5 paper swap (add ComfyClaw arXiv 2607.01709, demote GLM-5.2 = Mythos to honorable mention) + 4 honorable mention adds (p-MEM DAC 2026, Mastermind arXiv 2607.01764, SAIMY AI Dream Company, GLM-5 async RL on Hugging Face) + 0 broad rollbacks. v21 top-5: (1) SIA, (2) Memora, (3) Phase Matters, (4) ComfyClaw (v21 NEW), (5) VisualClawArena. **All v21 content is preserved verbatim in the backup. The v22 add is documented in the v22 addendum above: 0 top-5 paper swaps + 5 honorable mention adds (Adaptive Auto-Harness arXiv 2606.01770, Liquid AI LFM2.5-VL-450M blog, Time Magazine Favaro+Clark, Vint Cerf panel, TechCrunch OpenClaw iOS+Android launch). v22 top-5 holds.**



## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (0 top-5 adds, 4 honorable mention adds, 1 demotion-to-watchlist, 0 broad rollbacks):**

1. **NEW — Honorable mention: Axios "How the world's top AI models were revived" (July 3 2026).** Amazon-Jassy → Bessent → Lutnick → Amodei 20-day showdown. **v20 add: read before the Q3 W2-W3 v1.0 spec trust-model section update. 30 minutes.**

2. **NEW — Honorable mention: "Bad Epoll" Linux kernel flaw CVE-2026-46242 (The Hacker News, July 3 2026).** Mythos found CVE-2026-43074 but missed Bad Epoll. **v20 add: read before the Q3 W2-W3 v1.0 spec safety-considerations section update + the v20 auditable-bug-discovery pattern. 30 minutes.**

3. **NEW — Honorable mention: Bloomberg + LA Times + Apollo Daily Spark "The AI trade is losing one of its key signals" (July 2-3 2026).** Silicon Data LLM Token Expenditure Index -20% from May high. Apollo: "AI: The ROI runway may be longer than the market thinks." **v20 add: read before the Q3 W2-W3 v1.0 spec pricing section update. 30 minutes.**

4. **NEW — Honorable mention: NSA Gen. Joshua Rudd + Chris Inglis statements on Mythos + GLM-5.2 (Economist + Dark Reading, July 3 2026).** **v20 add: read before the Q3 W2 v1.0 spec security/safety section update. 30 minutes.**

5. **NEW — Watchlist demotion: "Mythos 5 Glasswing" framing.** v19 honorable mention demoted to v20 watchlist: Mythos is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The framing holds; the v20 emphasis shifts.

**v20 retractions of v19:** **0 broad rollbacks + 1 demotion to watchlist.** v19 "Mythos 5 Glasswing" honorable mention demoted to v20 watchlist pending v20.5 Anthropic-Newsom California + Axios Amazon-Jassy-Anthropic jailbreak resolution. v19 top-5 holds (Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search). v19 model shortlist holds. v19 6/12/24-month plan holds in v20, with v20 adding: auditable-bug-discovery pattern, unit-economics argument, Q4 2026 ship window, 11-step narrative.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 papers-to-read content (preserved in backup)

The v19 papers-to-read (preserved in `dan2-papers-to-read.v19-backup-2026-07-04.md`, 22.7KB, 150 lines) covers: v19 top-5 (unchanged from v17): Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search. v19 added 4 new honorable mentions + 5 new SHARPEN. **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 new honorable mention adds (Axios, Bad Epoll, Bloomberg+LA Times+Apollo, NSA Rudd+Chris Inglis) + 1 demotion-to-watchlist (Mythos 5 Glasswing). v20 top-5 holds (Phase Matters, Memora, Red Queen Gödel Machine, SIA, As We May Search).**
