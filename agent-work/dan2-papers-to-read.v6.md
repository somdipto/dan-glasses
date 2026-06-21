# Top 5 Papers to Read — Danlab Focus, June 2026
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-17
**Scope:** Five papers the team should read (or re-read) in Q3 2026, ordered by leverage on Danlab's roadmap. One per research area, not five papers from the same area.
**Prior versions:** `dan2-papers-to-read.v5.md` (2026-06-16) — kept as backup.

The picks optimize for:
- **Direct impact on the v1.5 / v2 roadmap.**
- **Coverage of the four research areas** the danlab team should own: self-improvement, edge VLM, memory, proactive AI.
- **Pragmatism over novelty** — papers with code, ablations, and concrete numbers beat papers with theoretical claims.
- **v6 reshuffle:** The v5 list had AEL, VLMCache, TiMem, Microsoft Proactive Triggers, SIA. v6 swaps to:

1. **SIA → RHO (Retrospective Harness Optimization).** SIA is the headline, but it requires labels. RHO works from past trajectories with no labels, which is the right cold-start primitive for danlab-multimodal. SIA is the v2 follow-on; RHO is the v1.5 entry point.
2. **Microsoft Research "Do Proactive Agents Really Need an LLM" → PRISM Festina Lente.** The Microsoft paper is the trigger architecture; PRISM is the gate that decides whether to fire. The two compose. Read both, but PRISM is the more recent and more generalizable insight.
3. **VLMCache stays** (highest ROI for wearable). v6 update: add **VLCache** (the related work from 2025-12) which goes a step further with hash-based image embedding reuse and 1.2–16× speedup. Both should be on the reading list, but VLCache is the more generalizable technique.
4. **TiMem stays** for the memory architecture lesson, but **Memanto is the alternative case** to read alongside. v6 reads TiMem + Memanto as a pair to settle the graph-vs-vector debate.
5. **AEL → ProActor.** AEL's Sharpe 2.13 is impressive but the proactive-agent framing is more directly applicable to Dan Glasses. ProActor (ACL 2026) is the timing-aware RL framework for proactive task scheduling — the right pattern for training our proactive trigger layer from user feedback.

---

## #1. **SIA: Self-Improvement Architecture** (Hexo Labs, MIT, May 2026)
- **arXiv:** https://arxiv.org/abs/2605.27276
- **GitHub:** https://github.com/hexo-ai/sia
- **Why this one:** SIA is the **only credible open path to harness+weights self-improvement in 2026** that we've found. Hexo Labs released it in May 2026, MIT-licensed. The headline results across three very different domains:
  - **56.6% improvement on LawBench** (Chinese legal charge classification).
  - **91.9% runtime reduction on GPU kernel optimization** (writing low-level CUDA).
  - **502% improvement on single-cell RNA denoising** (biology benchmark).
- **The architecture (three LLMs):**
  - **Meta-Agent** initializes the scaffold.
  - **Task-Specific Agent** executes.
  - **Feedback-Agent** (Claude Sonnet 4.6 in the released code) alternates between prompt/scaffold edits and triggering RL weight updates. **Crucially, the Feedback-Agent chooses dynamically between harness and weight updates based on reward dynamics** — not a fixed sequence.
- **The lesson for Danlab:** danlab-multimodal's README is honest: "We do not modify model weights. We do not run policy gradient or any RL algorithm. We will not call this RL until the harness+weights modification is open and auditable. The credible path is the SIA framework." That sentence is the integrity statement that makes the rest of the project trustworthy. **Reading SIA's code is the prerequisite for the v2 plan** (fork SIA, integrate as a harness, run the heuristic-vs.-RHO-vs.-learned-vs.-TT-SI-vs.-SIA ablation).
- **v6 nuance — SIA is not the v1.5 primitive.** SIA requires labeled reward data. RHO (paper #2) doesn't. **SIA is the v2.0 / Q2 2027 move. RHO is the v1.5 / Q4 2026 move.** SIA-H (harness only) is the v1.5 alternative if we want to stay in the SIA family.
- **What to take from it:**
  - The harness interface. What does a SIA-compatible harness look like? How does it expose the model's forward pass for weight updates?
  - The reward-model interface. How does SIA consume a reward signal (heuristic, learned, or human)?
  - The rollout / trajectory format. This is the contract between danlab-multimodal's loop and SIA's training loop.
  - The **dynamic harness-vs-weights switching** is the SOTA 2026 insight. Most prior work fixes one or the other.
- **Read time:** ~4 hours including a skim of the code. This is the most engineering-heavy of the five.

---

## #2. **Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference** (v6 NEW)
- **arXiv:** https://arxiv.org/html/2606.05922v2 (arXiv:2606.05922, June 2026)
- **Why this one:** RHO is the **right v1.5 primitive** for danlab-multimodal. Unlike SIA, it requires **no labels** — it improves a harness from past, unlabeled trajectories in a **single retrospective pass**. Empirically, RHO attains a higher SWE-Bench Pro pass rate (0.78) at a matched single-round budget than Meta-Harness (0.60). Even when Meta-Harness is allowed 10 rounds and reaches ~0.80, RHO wins on **compute efficiency** (3× less optimization compute) and on **the label-free property**.
- **The architecture:**
  - Operates over past trajectories — no external validation feedback required.
  - Single retrospective pass. Not iterative.
  - Improves the harness (prompts, parameters, workflow) without touching model weights.
- **The lesson for Danlab:** danlab-multimodal has a heuristic that scores descriptions. We don't have a labeled reward model. We don't have time to label 10,000 trajectories. RHO is the **drop-in primitive** that can take the heuristic outputs and improve the harness (the prompt template) on top, **with zero new labels**. This is the realistic v1.5 move.
- **v6 priority order:**
  1. **RHO first (Q3 2026).** Wire into danlab-multimodal. Improve harness from existing heuristic output.
  2. **TT-SI second (Q4 2026).** Test-time training on weak areas.
  3. **SIA third (Q1 2027).** Full harness+weights loop with a small learned reward model + HRM-Text 1B Feedback-Agent.
  4. **HarnessX / AHE / HarnessForge** as alternatives to SIA evaluated on the same benchmark.
- **What to take from it:**
  - The retrospective-pass technique. We have the data (heuristic output × vision-model output). The labels are not required.
  - The "no labels" property is the most important insight. **SIA-H requires labels. RHO doesn't.** For a small team, this is the difference between shipping in 6 weeks and shipping in 6 months.
  - Pair with SIA-H (harness-only SIA variant) as a follow-on. The SIA paper documents SIA-H separately.
- **Read time:** ~2 hours. Less engineering-heavy than SIA.

---

## #3. **VLCache: Computing 2% Vision Tokens and Reusing 98% for Vision–Language Inference** (v6 NEW) + **VisionTrim** (paired reading)
- **VLCache arXiv:** https://arxiv.org/html/2512.12977 (arXiv:2512.12977, December 2025)
- **VisionTrim arXiv:** https://arxiv.org/html/2601.22674v1 (arXiv:2601.22674, January 2026)
- **Why these two together:** **VLMCache (v5 #2) is now superseded by VLCache** for our use case. VLCache stores per-image ViT outputs and KV caches keyed by image hash, skipping ViT computation entirely on reused images. **1.2–16× speedup** depending on model and image-token length, with only **2–5% of vision tokens recomputed** at each LLM layer. **This is the highest-ROI paper for the wearable path.** VisionTrim complements it: training-free vision token compression using Dominant Vision Token Selection (CLS-attention) + Text-Guided Vision Complement (TGVC). **2–3× speedup** drop-in.
- **The lesson for Danlab:** the Dan Glasses "watchful" mode spends 95%+ of its time on near-static scenes (a desk, a conversation, a room). Caching the visual KV prefix by image hash is **the right architectural choice for always-on wearable vision**. With VLCache + VisionTrim stacked, we go from 10–15 s/frame on x86_64 CPU to **~1–2 s/frame on x86_64 CPU**, and on aarch64+NPU we hit the 250 ms target comfortably.
- **v6 architecture update:** both are drop-in to perceptiond. **VLCache for the KV-cache reuse, VisionTrim for the token-pruning.** Stacking both is the v1.5 path to real-time on-device VLM.
- **What to take from them:**
  - VLCache's per-image hashing: identify reused visual content across contexts. Skip ViT computation on hash hit.
  - VLCache's per-layer recompute: at each attention layer, recompute a fraction r of tokens; the rest reuse previous KV states. The 2–5% recompute number is the design point.
  - VisionTrim's TGVC: use textual guidance to cluster/merge pruned visual tokens that are relevant to the input text. Cross-modal alignment preserved.
  - **Pare this with SpecVLM (speculative decoding, 1.5–2.9×)** and **LQA (lightweight quantized-adaptive, 4.5% accuracy gain under shift)** as the v1.5 stack.
- **Read time:** ~2 hours each. The techniques are straightforward to implement in our pipeline.

---

## #4. **TiMem: Temporal-Hierarchical Memory Consolidation** + **Memanto: Typed Semantic Memory** (v6 paired)
- **TiMem arXiv:** https://arxiv.org/html/2601.02845v1 (arXiv:2601.02845, January 2026)
- **Memanto arXiv:** https://arxiv.org/html/2604.22085 (arXiv:2604.22085, April 2026)
- **Why these two together:** TiMem is the SOTA on LoCoMo (75.30%) and LongMemEval-S (76.88%), and reduces recalled memory length by 52% on LoCoMo. The Temporal Memory Tree (TMT) is the cleanest hierarchical memory design. **But** Memanto is the May 2026 counter-argument: a purely vector-based backend that hits SOTA on the same benchmarks, claiming graph + vector hybrids add complexity without improving performance.
- **The lesson for Danlab:** our memoryd is a flat SQLite + flat cosine. To credibly call Dan Glasses a "personal intelligence that learns," we need hierarchical memory. But we shouldn't over-engineer. The **correct read is: TiMem gives us the design pattern, Memanto tells us the architecture can be simpler than we think.**
- **v6 architecture decision:** implement the **MemX + TiMem hybrid** (vector + BM25 + memory_links + temporal hierarchy) as the v1.5 target. **Benchmark against a Memanto-style pure-vector + typing implementation.** If the hybrid is <5% better on our held-out eval, **simplify to Memanto-style in v2.** Don't carry complexity without measured benefit.
- **What to take from them:**
  - **TiMem's TMT:** raw events → episodic → semantic → procedural → schema, consolidated by semantic-guided, complexity-aware recall. The 52% length reduction is critical for the "first-token" latency budget — we can't ship 5000-token recall prompts to a 1B on-device LLM.
  - **Memanto's lesson:** modern LLMs (including HRM-Text 1B) handle the reasoning/filtering that graph precomputation aimed to address. Pure-vector + typed-memory is competitive.
  - **v1.5:** Add temporal + confidence + relational scoring on top of the existing flat store. (~2 weeks.)
  - **v2:** Add the Temporal Memory Tree, OR simplify to Memanto-style — benchmark decides.
- **Read time:** ~3 hours for the pair. Code is public for both.

---

## #5. **PRISM: Festina Lente Proactivity** (v6 NEW, replaces Microsoft "Proactive Triggers")
- **arXiv:** https://arxiv.org/pdf/2602.01532 (arXiv:2602.01532, ICLR 2026 poster)
- **Why this one:** PRISM is the **single most important proactive-AI paper for our wearable**. The "Festina Lente" (start slowly, proceed carefully) framework is the **exact right pattern for an AI that doesn't annoy you**. The Microsoft Research paper (v5 #4) is the trigger architecture; **PRISM is the gate that decides when to fire**. The two compose, but PRISM is the more recent, more generalizable insight.
- **The architecture:**
  - **Dual-process:** a fast model provides initial estimates of (p_need, p_accept). A single slow reasoning pass is triggered when fast outputs are near the decision boundary.
  - **Gate:** intervention only if the calibrated acceptance probability exceeds a threshold derived from asymmetric costs of missed help vs. false alarms.
  - **Training:** gate-aligned distillation where a teacher runs the full PRISM pipeline to supervise a student policy that can be decoupled from the gate for tunable, auditable control.
- **The empirical win:** on ProactiveBench, PRISM reduces false alarms by **22.8%** and improves F1 by **20.1%** over strong baselines. **This is the wearable-friendly proactive architecture.**
- **The lesson for Danlab:** the wearable power budget is dominated by *when* we run the LLM, not by the LLM itself. PRISM's fast-slow reasoning pattern is the **right design for our proactive layer**. Pair it with the Microsoft Research graph-encoder trigger (v5 #4) as the front-end. **Result: a wearable that initiates help 1% of the time, only when the user is likely to want it.**
- **What to take from it:**
  - **The asymmetric cost framing.** False alarms are worse than missed help (for a wearable). This is the right framing for a personal assistant.
  - **Gate-aligned distillation.** Train a small student policy that can be deployed without the gate, with the gate only as a tunable control. **This is the v1.5 deployment pattern.**
  - **ProactiveBench** as the evaluation. We need to benchmark our proactive layer here.
  - **v2 follow-on:** pair with ProActor (ACL 2026, paper: https://arxiv.org/html/2605.24900v1) — a timing-aware RL framework for proactive task scheduling. Once we have user feedback, ProActor is the right fine-tuning primitive.
- **Read time:** ~2 hours. The technique is elegant and well-documented.

---

## What about the rest?

These five are the **highest-leverage picks**. Other papers worth reading in Q4 2026 / Q1 2027, after the v1.5 plan is in motion:

- **HRM-Text 1B (Sapient Intelligence, 2026-05-18)** — not a paper per se, but the 1.15 B hierarchical-recurrent reasoning LLM release. Read the model card. https://sapient.inc/introducing-hrm-text
- **Anthropic, "When AI Builds Itself" (May 2026)** — the public framing of recursive self-improvement from Anthropic. Read for positioning, not technique. https://www.nectain.com/blog/the-next-ai-shock-is-already-loading
- **MemX: A Local-First Long-Term Memory System for AI Assistants** (arXiv:2603.16171) — closest architectural twin to what memoryd should become. 7-relation-type graph + RRF over vector + keyword.
- **MemMachine: Ground-Truth-Preserving Memory System** (arXiv:2604.04853) — three-layer memory (short-term working, long-term episodic, semantic/profile) with Neo4j graph + pgvector. Production-shape API.
- **AriadneMem: Threading the Maze of Lifelong Memory** (arXiv:2603.03290) — entropy-aware graph coarsening + Steiner Tree retrieval. 15% multi-hop F1 gain on LoCoMo.
- **TeleMem: Building Long-Term and Multimodal Memory for Agentic AI** (arXiv:2601.06037) — DAG-based memory substrate.
- **CraniMem: Cranial Inspired Gated and Bounded Memory** (arXiv:2603.15642) — RAS-inspired gating, utility-driven consolidation.
- **TT-SI: Self-Improving LLM Agents with Test-Time Training** (https://openreview.net/forum?id=k30IrbNYSG) — the test-time training playbook for when we want a lighter alternative to SIA.
- **SAGE: Multi-Agent Self-Evolution for LLM Reasoning** (https://openreview.net/forum?id=7sOeRzBzjB) — the multi-agent self-evolution pattern for when DanClaw has 3+ live agents and we want them to co-evolve.
- **Nanomind: Tiny but Mighty** (https://arxiv.org/abs/2510.05109) — the software/hardware co-design playbook for the wearable power budget. 18.8 h on 2000 mAh for a 0.5B VLM is the target.
- **EdgeFM: Efficient Edge Inference for VLMs** (arXiv:2604.27476) — agent-driven kernel optimization framework. 1.49× speedup over TensorRT-Edge-LLM on NVIDIA Orin.
- **LiteVLM** (arXiv:2506.07416) — patch selection + token compression + speculative decoding + FP8 PTQ. 2.5–3.2× speedup on NVIDIA DRIVE Thor.
- **VLMQ: Token Saliency-Driven Post-Training Quantization** (arXiv:2508.03351) — 16.45% accuracy improvement on MME-RealWorld with 2-bit quantization.
- **LQA: Lightweight Quantized-Adaptive Framework for VLMs on the Edge** (arXiv:2602.07849) — 4.5% accuracy gain under distribution shift, 19.9× reduction in TTA memory.
- **SPEED-Q: Staged Processing with Enhanced Distillation for On-Device VLM Quantization** (arXiv:2511.08914) — 2-bit InternVL3-1B at <400 MB RAM, accuracy comparable to 0.6B FastVLM at 1.5 GB.
- **CoVSpec: Device–Edge Co-Inference for VLMs via Speculative Decoding** (arXiv:2605.02218) — 2.21× throughput, 96% bandwidth reduction. The tethered-glasses path.
- **HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry** (arXiv:2606.14249) — co-evolution of harness and model.
- **HarnessForge: Joint Harness and Policy Evolution** (arXiv:2606.01779) — up to 12.0% gains via harness-policy co-evolution.
- **Agentic Harness Engineering (AHE)** (arXiv:2604.25850) — observability-driven automatic harness evolution. Terminal-Bench 2 from 69.7% → 77.0% in 10 iterations.
- **HyperAgents / DGM-H** (arXiv:2603.19461) — Darwin Gödel Machine variant where the meta-level modification procedure is itself editable.
- **SICA: A Self-Improving Coding Agent** (arXiv:2504.15228) — removes the meta-agent vs. target-agent separation. The agent edits its own codebase.
- **ProAct: A Dual-System Framework for Proactive Embodied Social Agents** (arXiv:2602.14048) — future-state prediction + idle-time acquisition + memory + proactive delivery. 0.020 → 0.447 anticipation recall improvement.
- **ProAgent: Harnessing On-Demand Sensory Contexts** (arXiv:2512.06721) — tiered perception (always-on cheap + on-demand expensive vision). **27.7% higher proactive accuracy, 20.5% lower false detections. 85% user satisfaction.** Implemented on AR glasses.
- **PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory** (arXiv:2604.08000) — DD-MM-PAS architecture + IntentFlow demand detection + hybrid co-evolving memory.
- **ContextAgent: Context-Aware Proactive LLM Agents** (arXiv:2505.14668) — context reasoner (A_S), proactive scores (P_S), tool chains (T_C). ContextAgentBench 1,000 samples.
- **ProActor: Timing-Aware Reinforcement Learning for Proactive Task Scheduling Agents** (arXiv:2605.24900, ACL 2026) — GRPO with stage-aware composite rewards. The fine-tuning primitive for the proactive layer.
- **ProAgentBench: Evaluating LLM Agents for Proactive Assistance with Real-World Data** (arXiv:2602.04482) — 28,000 events, 500+ hours. The benchmark for proactive layer eval.
- **Synthius-Mem** — for the adversarial-robust memory bar (99.6% on adversarial LoCoMo).
- **SkillRL: Evolving Agents via Recursive Skill-Augmented RL** (https://openreview.net/forum?id=By7Pj576U3) — the skill-bank pattern for "knows your workflow."

---

## Reading order for the team

| Week | Paper | Owner |
|------|-------|-------|
| W1 | RHO (#2) | DAN-2 (danlab-multimodal) |
| W1 | VLCache + VisionTrim (#3) | DAN-3 (perceptiond) |
| W2 | PRISM (#5) | DAN-1 (OpenClaw + power) |
| W2 | TiMem + Memanto (#4) | DAN-4 (memoryd) |
| W3 | SIA (#1) | somdipto + DAN-2 (research) |
| W4 | Re-read all 5 as a group, write a 1-page synthesis per paper | all |

---

## v6 → v7 watchlist (Q4 2026)

If we re-run this list in Q4 2026, expect:

- **Anthropic's "AI that builds itself" followup** (probably published in 2026 H2). Likely the next data point on the RSI conversation.
- **SIA-W (SIA with full weight updates) on a public release.** If Hexo Labs ships a public SIA-W that we can fork, danlab-multimodal v3 timeline moves forward.
- **A vision-language HRM model** (Sapient Intelligence). If they release a 1B vision-reasoning HRM, that's the perfect single-model replacement for our LFM2.5-VL + HRM-Text 1B pair.
- **A wearable-class Edge VLM benchmark.** The field needs this. danlab could publish.
- **The Anthropic "brake pedal" mechanism** (if it ships). Industry-wide standard for slowing frontier AI. danlab's positioning improves.
- **India-specific VLMs (Bhashini / AI4Bharat).** First credible 1B-class VLM with Hindi/Tamil/Bengali support. If this ships, the India-language bet becomes cheap.

---

## One more thing

The point of these five isn't to make Danlab an academic group. It's to **collapse the distance between "what's published" and "what we ship"**. Every paper above has open code. The v1.5 plan incorporates every one. The next move is to read them, prototype, and ship.

v6 deltas: RHO swapped in (label-free retrospective optimization is the right v1.5 primitive); VLCache swapped in (1.2–16× speedup, 2–5% vision token recompute — supersedes VLMCache for our use case); Memanto added as paired reading with TiMem (graph-vs-vector debate, benchmark decides); PRISM swapped in (Festina Lente gate, 22.8% false-alarm reduction, more generalizable than v5's Microsoft trigger paper).

*👾*
 cluster/merge pruned visual tokens that are relevant to the input text.
  - **Pair VLCache with VisionTrim, SpecVLM, and LiteVLM.** This stack is the v1.5 on-device VLM performance lever.
- **Read time:** ~3 hours for both. The techniques are straightforward to implement.

---

## #4. **TiMem: Temporal-Hierarchical Memory Consolidation** (v5 #3) + **Memanto: Typed Semantic Memory** (v6 paired reading)
- **TiMem arXiv:** https://arxiv.org/html/2601.02845v1
- **Memanto arXiv:** https://arxiv.org/html/2604.22085
- **Why these two together:** TiMem is the SOTA on LoCoMo (75.30%) and LongMemEval-S (76.88%), and reduces recalled memory length by 52% on LoCoMo. The Temporal Memory Transformer (TMT) is the cleanest hierarchical memory design. **But Memanto (April 2026) is the counter-argument**: a purely vector-based typed semantic memory with 13-category schema and built-in conflict resolution, hits SOTA on LongMemEval + LoCoMo, **without any graph database**. Memanto's ablation shows that **retrieval recall is the primary performance driver, not graph complexity**. Modern LLMs handle reasoning/filtering that graph precomputation aimed to address.
- **The lesson for Danlab:** **read both, then decide**. TiMem says "go hierarchical with a Temporal Memory Tree." Memanto says "go pure-vector with typed categories." The 2026 evidence is converging on: **good embeddings + good retrieval (BM25 + RRF + MemGate filter) + typed memory schema > complex graph**. The graph's value is in the **multi-hop reasoning** (AriadneMem, MemX) which we may not need at v1.5.
- **v6 architecture decision:**
  - **v1.5 (Q4 2026):** Implement the Memanto shape — typed semantic memory + RRF over vector + BM25 + memory_links table (7 relation types from MemX, but not graph-aware retrieval yet). Add MemGate-style 9M-param filter.
  - **v2 (Q2 2027):** Add TiMem-style Temporal Memory Tree if the v1.5 numbers show the hierarchy is worth it. If not, stay flat-vector.
- **What to take from them:**
  - **TiMem:** the Temporal Memory Transformer pattern, the level-specific consolidation. The 52% length reduction is critical for the "first-token" latency budget.
  - **Memanto:** the 13-category typed schema. The 5-stage ablation showing simplicity wins. The "Memory Tax" framing — every LLM extraction / graph build costs tokens and adds latency.
  - **The composite lesson:** don't carry graph complexity without measured benefit. v1.5 stays flat-vector with typed schema; v2 adds hierarchy only if it earns its complexity.
- **Read time:** ~4 hours for both. Most useful when read as a pair.

---

## #5. **PRISM: Festina Lente Proactivity** (v6 NEW) + **ProActor: Timing-Aware RL for Proactive Task Scheduling** (v6 NEW)
- **PRISM arXiv:** https://arxiv.org/pdf/2602.01532 (ICLR 2026 poster)
- **ProActor arXiv:** https://arxiv.org/html/2605.24900v1 (ACL 2026)
- **Why these two together:** PRISM is the **gate** (when to fire), ProActor is the **training** (how to learn from user feedback). Compose them.
- **PRISM (the gate):** Festina Lente ("make haste slowly"). A cost-sensitive gating mechanism that activates a slow, resource-intensive reasoning pass only **near decision boundaries**. Dual-process: fast model gives initial p_need × p_accept estimates; slow reasoning only when those estimates are ambiguous. On ProactiveBench, PRISM reduces false alarms by **~22.8%** and improves F1 by **~20.1%** vs. strong baselines. Public code + models released.
- **ProActor (the training):** A unified framework for training **proactive, timing-aware** conversational task scheduling agents. Domain-agnostic annotation that creates **full opportunity time windows** (not point labels) for proactiveness RL. GRPO with stage-aware composite rewards (RULER-based). Targets Qwen2.5-14B-ProActor-Q4 (4-bit LoRA fine-tuning). ACL 2026.
- **The lesson for Danlab:** **the wearable power budget is dominated by *when* we run the LLM, not by the LLM itself**. The Microsoft Research graph-encoder trigger (v5 #4) is the **always-on detector**; PRISM is the **cost-sensitive gate** that decides whether to call the LLM. ProActor is the **RL fine-tuning pattern** that lets us learn from user feedback (accept, dismiss, ignore) to improve the trigger over time.
- **The composition:**
  ```
  [VLM descriptions] + [transcripts]
        ↓
  [Proactive trigger] ← Microsoft Research graph encoder (220 MiB BF16, on-device)
        ↓
  [PRISM gate] ← p_need × p_accept, slow path only near boundary
        ↓
  [HRM-Text 1B + LFM2.5-VL-450M] ← LLM only fires <1% of the time
        ↓
  [ProActor-style RL fine-tuning] ← Learn from user feedback
        ↓
  [KittenTTS] → speaker / [Telegram] → phone
  ```
- **What to take from them:**
  - **PRISM:** the dual-process design (fast + slow), the asymmetric cost threshold, the gate-aligned distillation. Public code makes it shippable.
  - **ProActor:** the GRPO + composite reward pattern, the 4-bit LoRA fine-tuning recipe, the timing-aware evaluation framework.
  - **The v1.5 architecture:** Microsoft trigger (always-on, ~1 mW) + PRISM gate (decides if we call the LLM) + ProActor-style RL fine-tuning (improves trigger from user feedback).
- **Read time:** ~3 hours for both.

---

## v5 #1 (AEL) — still worth reading, demoted to honorable mention

**AEL: Agent Evolving Learning for Open-Ended Environments** (arXiv:2604.21725v1).
Sharpe ratio 2.13 on a portfolio benchmark — beating 5 published self-improving methods. The ablation is gold: memory + reflection yield ~58% over stateless, and *adding more components degrades performance*.

**Why demoted to honorable mention:** the AEL lesson is subsumed by SIA + RHO + HarnessX. AEL's "two-timescale design" pattern is mentioned in RHO's design. Read AEL if you have time; if not, RHO carries the lesson.

---

## What about the rest?

These five are the **highest-leverage picks**. Other papers worth reading in Q4 2026 / Q1 2027, after the v1.5 plan is in motion:

- **AHE: Agentic Harness Engineering** (https://arxiv.org/html/2604.25850v2) — observability-driven automatic evolution. Pass@1 69.7% → 77.0% on Terminal-Bench 2 in 10 iterations. Surpasses Codex-CLI.
- **HarnessForge: Joint Harness and Policy Evolution** (https://arxiv.org/html/2606.01779v1) — co-evolution of harness and policy. Up to 12.0% gains over harness-only and policy-only baselines.
- **HarnessX: Composable, Adaptive, Evolvable Agent Harness Foundry** (https://arxiv.org/html/2606.14249) — unifying theory of harness evolution. Argues for co-evolution of harness and model.
- **TT-SI: Self-Improving LLM Agents with Test-Time Training** (https://openreview.net/forum?id=k30IrbNYSG) — the test-time training playbook for when we want a lighter alternative to SIA.
- **MemMachine: Ground-Truth-Preserving Memory** (https://arxiv.org/pdf/2604.04853) — three-layer memory (short-term, long-term episodic, profile) with Neo4j + pgvector + SQLite. Production-shape REST/Python/MCP API.
- **MemX: Local-First Long-Term Memory** (https://www.arxiv.org/pdf/2603.16171) — Rust + libSQL, 7 relation types, RRF over vector + keyword. **The closest architectural twin to what memoryd should become.**
- **AriadneMem: Entropy-Aware Graph Coarsening** (https://arxiv.org/pdf/2603.03290) — if we ever do go graph, this is the most sophisticated topology.
- **CraniMem: Gated and Bounded Memory** (https://arxiv.org/pdf/2603.15642) — hippocampal-inspired gating. Strong retrieval vs. Mem0 baseline.
- **TeleMem: DAG-based Long-Term Memory** (https://arxiv.org/pdf/2601.06037) — for when we need causal reasoning over memories.
- **LiteVLM: Low-Latency Edge VLM** (https://arxiv.org/html/2506.07416v2) — the edge VLM pipeline. 2.5× speedup, 3.2× with FP8 PTQ.
- **SpecVLM: Speculative Decoding for VLMs** (https://arxiv.org/pdf/2509.11815) — pairs with VLCache/VisionTrim. 2.5–2.9× speedup.
- **CoVSpec: Device-Edge Co-Inference for VLMs** (https://arxiv.org/html/2605.02218v1) — the tethered-glasses architecture. 2.21× throughput, 96% bandwidth reduction.
- **Nanomind** (https://arxiv.org/abs/2510.05109) — the software/hardware co-design playbook for the wearable power budget. 18.8 h on 2000 mAh for a 0.5B VLM is the target.
- **ContextAgent: Context-Aware Proactive LLM Agents** (https://arxiv.org/html/2505.14668) — the proactive AI benchmark (ContextAgentBench, 1000 samples, 9 scenarios, 20 tools) we'll need to evaluate our proactive trigger layer.
- **ProAgentBench** (https://arxiv.org/pdf/2602.04482) — 28,000 events, 500+ hours, privacy-compliant. The right benchmark for v1.5 evaluation.
- **ProAct: Dual-System Proactive Embodied Social Agents** (https://arxiv.org/html/2605.25971v2) — anticipation recall 0.020 → 0.447.
- **ProAgent: On-Demand Sensory Contexts** (https://arxiv.org/pdf/2512.06721) — on AR glasses. 27.7% higher proactive prediction accuracy, 20.5% lower false detections.
- **SkillRL: Evolving Agents via Recursive Skill-Augmented RL** (https://openreview.net/forum?id=By7Pj576U3) — the skill-bank pattern for "knows your workflow."
- **DPCM: Memory Beyond Recall** (https://openreview.net/forum?id=ywl53zPXu0) — the dual-process memory design for v2.
- **Synthius-Mem** (https://arxiv.org/html/2603.04928) — adversarial-robust memory. 99.6% on LoCoMo. The bar for our safety story.
- **Sensible Agent (UMD 2026)** — gaze/hand-occupancy interrupt policy. The modality choice when the trigger fires.

---

## Reading order for the team

| Week | Paper | Owner |
|------|-------|-------|
| W1 | VLCache + VisionTrim (#3) | DAN-3 (perceptiond) |
| W1 | RHO (#2) | DAN-2 (audiod) + somdipto (research) |
| W2 | TiMem + Memanto (#4) | DAN-4 (memoryd) |
| W2 | PRISM + ProActor (#5) | DAN-1 (OpenClaw + proactive layer) |
| W3 | SIA (#1) | somdipto + DAN-2 (research) |
| W4 | Re-read all 5 as a group, write a 1-page synthesis per paper | all |

---

## One more thing

The point of these five isn't to make Danlab an academic group. It's to **collapse the distance between "what's published" and "what we ship"**. Every paper above has open code (or, in SIA's case, MIT-licensed code). The v1.5 plan incorporates every one. The next move is to read them, prototype, and ship.

v6 deltas from v5:
- **#1 SIA** unchanged in title, but nuanced: "SIA is the v2.0 move, not v1.5."
- **#2 RHO NEW** (replaces AEL as the v1.5 self-improvement primitive).
- **#3 VLCache NEW** + VisionTrim (replaces VLMCache; VLCache is the more generalizable technique with 1.2–16× speedup).
- **#4 TiMem + Memanto paired** (TiMem alone was v5 #3; Memanto is the counter-argument to graph complexity).
- **#5 PRISM + ProActor** (replaces Microsoft Proactive Triggers; PRISM is the gate, ProActor is the RL training).

---

*👾*
