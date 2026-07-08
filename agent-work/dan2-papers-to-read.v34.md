# Top 5 Papers for Danlab — Dan2 (2026-06-21)

> **Scope.** Five papers the Danlab team should read in the next 30 days, ranked by leverage on the AGI roadmap. Each pick is grounded in a concrete product or research decision the team is about to make.

These are *not* "the most cited papers in AI." These are the papers where finishing the read changes what we ship next month.

---

## 1. SIA: Self Improving AI with Harness & Weight Updates

**Why:** This is the credible path from our `danlab-multimodal` heuristic loop to genuine recursive self-improvement. The team has been honest about this in the multimodal README — they labeled it "pre-RL scaffold." SIA is the open-source (MIT) framework that actually closes the loop, updating both the harness (workflow, prompts, retry logic) AND the model weights on task feedback. We can fork it.

**Citation:** Baskaran, K. et al. "SIA: Self Improving AI with Harness & Weight Updates." arXiv:2605.27276 (May 2026). Hexo Labs + Oxford.

**What you'll learn:**
- The harness-update vs weight-update distinction (most self-improvement research does one or the other; SIA does both)
- How a Feedback-Agent rewrites both its own scaffold and the task-agent's weights via test-time training
- Why open-endedness (DGM-style archive) is harder to make stable than harness-only updates

**Direct Danlab application:**
- Replace `demo.py`'s heuristic scoring with SIA's harness-update loop
- Use `LFM2.5-1.2B-Thinking` as the Feedback-Agent (we can run it locally)
- Promote danlab-multimodal from "pre-RL scaffold" to "first genuinely self-improving cycle on a sub-500MB VLM"

**Time to read productively:** 2-3 hours. The paper is dense but the architecture is clear.

**Source:** https://arxiv.org/pdf/2605.27276

---

## 2. LFM2 Technical Report

**Why:** Our primary vision model is LFM2.5-VL-450M from Liquid AI's LFM2 family. We do not have benchmark numbers on aarch64, the deployment target. This paper is the closest thing to a vendor-provided benchmark — and Liquid's pitch (edge-first, tunable accuracy/latency) is the reason we picked the model in the first place. Reading this carefully tells us what *not* to measure and what to trust.

**Citation:** Liquid AI. "LFM2 Technical Report." arXiv:2511.23404 (November 2025).

**What you'll learn:**
- The Liquid Foundation Model architecture (hybrid shortconv + attention) — why it's faster than transformer-only at similar param counts
- The three LFM2-VL variants (450M, 1.6B, 3B) and what the size ladder actually buys you
- Which runtimes Liquid supports out of the box: Transformers, llama.cpp, ExecuTorch, vLLM
- Memory and throughput numbers on Liquid's reference hardware (not aarch64, but a starting point)

**Direct Danlab application:**
- Validate the LFM2.5-VL-450M choice with vendor numbers
- Plan the LFM2-VL-1.6B upgrade for "active" mode in PRD §5.2
- Identify which metrics to re-measure on Jetson Orin Nano / Redax (latency, memory, throughput density)

**Time to read productively:** 1.5 hours. Most of the value is in the architecture description and benchmark tables.

**Source:** https://arxiv.org/html/2511.23404

---

## 3. Tiny but Mighty: A Software-Hardware Co-Design Approach for Efficient Multimodal Inference on Battery-Powered Small Devices

**Why:** This is the closest paper to our actual deployment constraint — running a VLM on a battery-powered small device. It compares Nanomind, NanoVLM, llama.cpp on Jetson Nano/AGX and Orange Pi 5 Ultra, with explicit latency, memory, and energy measurements. If we're going to bet on a runtime for the wearable, this is the data.

**Citation:** "Tiny but Mighty: A Software-Hardware Co-Design Approach for Efficient Multimodal Inference on Battery-Powered Small Devices." arXiv:2510.05109v4 (October 2025).

**What you'll learn:**
- Real-world VLM latency on Jetson Nano vs Orange Pi 5 Ultra vs llama.cpp baseline
- How 4-bit quantization (Qwen2-VL-2B-Instruct, W4A16) changes the tradeoff
- Why Nanomind's TABM ring buffer beats llama.cpp on memory
- End-to-end latency from "image + prompt" to final output

**Direct Danlab application:**
- Decides: do we stay on llama.cpp or switch to Nanomind for the wearable?
- Sets realistic expectations: a 450M VLM on a sub-$300 SBC is feasible at ~5-10s/frame with proper quantization
- Identifies the GPU/NPU acceleration decision (issue #5 in dan2-architecture-review.md)

**Time to read productively:** 2 hours. The benchmark tables are the meat.

**Source:** https://arxiv.org/html/2510.05109v4

---

## 4. ProAgent: Harnessing On-Demand Sensory Contexts for Proactive Agent Systems in the Wild

**Why:** This is the architectural blueprint for `proactived` (the proposed 7th service in dan2-architecture-review.md §"Decision 3"). Proactive AI — agents that initiate rather than respond — is the product wedge. US-1 (Encounter Recall), US-2 (Contextual TaskReminder) from PRD §3 all require proactive behavior. This paper implements and evaluates it on actual AR glasses.

**Citation:** "ProAgent: Harnessing On-Demand Sensory Contexts for Proactive Agent Systems in the Wild." arXiv:2512.06721 (December 2025).

**What you'll learn:**
- How to combine always-on low-cost sensing with on-demand high-cost VLM inference (the exact pattern Dan Glasses needs)
- VLM-based "interrupt vs silent" decision making — when to speak, when to stay quiet
- The 4-component architecture: on-demand perception, persona/context fusion, VLM reasoner, delivery feedback loop
- Real benchmark: 27.7% higher proactive prediction accuracy, 20.5% lower false detection vs baselines, 85% user satisfaction in 20-person study

**Direct Danlab application:**
- Direct blueprint for the `proactived` service in our roadmap
- Validates the "salience-threshold gating" recommendation in dan2-architecture-review §issue 4
- 85% user satisfaction is a real benchmark to beat

**Time to read productively:** 2 hours. Architecture + benchmarks.

**Source:** https://arxiv.org/pdf/2512.06721

---

## 5. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Why:** Our `memoryd` is a first-wave vector store (episodic/semantic/procedural, all-MiniLM-L6-v2, SQLite). Mem0 is the second wave — memory as a managed external service with extraction, dedup, and (in Mem0^g) graph-based temporal reasoning. We are about to evaluate whether to swap or augment memoryd. This is the paper that defines what we're evaluating against.

**Citation:** Pratap, A. et al. "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory." arXiv:2504.19413 (April 2025).

**What you'll learn:**
- The "memory as conversation-pair extraction" pattern (vs raw log RAG)
- Why a knowledge-graph extension (Mem0^g) buys you 91% p95 latency reduction vs full-context baselines
- How Mem0 compares to Zep (temporal), Letta/MemGPT (LLM-managed), Cognee (knowledge graph), and our SQLite+vectors approach
- The LOCOMO benchmark for long-conversation memory QA — what we should be testing against

**Direct Danlab application:**
- Defines the promotion gate for issue #9 in dan2-architecture-review.md (memoryd provider evaluation)
- LoCoMo is the right benchmark to lock in now
- Mem0^g's temporal edges could be the v1.5 upgrade for `EpisodicEncounters` (the proposed memoryd extension)

**Time to read productively:** 1.5 hours. Architecture-focused sections are the value.

**Source:** https://arxiv.org/html/2504.19413

---

## Honorable Mentions (read if you have time)

- **MemMachine** (arXiv:2604.04853) — STM/LTM split, ground-truth preservation. Validates our three-tier (episodic/semantic/procedural) split.
- **Plan, Watch, Recover** (arXiv:2606.04970) — Proactive procedural assistance benchmark. EgoProactive dataset is relevant for Dan Glasses eval.
- **Galaxy: A Cognition-Centered Framework for Proactive, Privacy-Preserving, and Self-Evolving LLM Agents** (arXiv:2508.03991) — KoRa + Kernel dual-agent for proactive + self-evolution. Architectural inspiration for OpenClaw's multi-agent design.
- **Edge Reliability Gap** (arXiv:2603.26769) — SmolVLM2-500M negation collapse. Direct failure-mode data for our vision model.
- **ContextAgent** (arXiv:2505.14668) — Context-aware proactive agent with wearable sensors. Closer to our use case than ProAgent in some ways.

---

## Reading Order Recommendation

If you have **one weekend**, read in this order:

1. **LFM2 Technical Report** (Saturday morning) — know your own model
2. **Mem0** (Saturday afternoon) — know your own memory
3. **Tiny but Mighty** (Sunday morning) — know your own hardware
4. **ProAgent** (Sunday afternoon) — know your own product wedge
5. **SIA** (Sunday evening) — know your own research wedge

This order goes "where we are" → "what we're building" → "how we extend" → "where we're going." Each paper builds on the previous one's context.

---

*Dan2 reading list, 2026-06-21. Refresh quarterly as the field moves.*
