# Top 5 Papers to Read — Danlab Focus, Mid-2026
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-16
**Scope:** Five papers the team should read (or re-read) in Q3 2026, ordered by leverage on Danlab's roadmap. One per research area, not five papers from the same area.

The picks optimize for:
- **Direct impact on the v1.5 / v2 roadmap.**
- **Coverage of the four research areas** the danlab team should own: self-improvement, edge VLM, memory, proactive AI.
- **Pragmatism over novelty** — papers with code, ablations, and concrete numbers beat papers with theoretical claims.

---

## #1. **AEL: Agent Evolving Learning for Open-Ended Environments**
- **arXiv:** https://arxiv.org/abs/2604.21725v1
- **Why this one:** AEL's headline result is the cleanest empirical argument for *what to build next* in self-improving agents. Sharpe ratio 2.13 on a portfolio benchmark — beating 5 published self-improving methods and all non-LLM baselines. The ablation is the gold: memory + reflection yield ~58% over stateless, and *adding more components degrades performance*.
- **The lesson for Danlab:** the bottleneck in self-improving agents is **diagnosing how to use experience**, not accumulating more components. A simple Thompson Sampling bandit + LLM-driven reflection beats fancier systems. **This is exactly the pattern danlab-multimodal's heuristic loop should evolve into** — a learned reward model (Tier 1) → test-time training (Tier 2) → SIA-fork harness (Tier 3), in that order. Don't skip to Tier 3.
- **What to take from it:**
  - Two-timescale design (fast bandit + slow LLM reflection) is the right shape for our memory daemon.
  - Reflection is a System-2 operation, not a System-1 one. Run it at night, not on every event.
  - "More components is worse" is the corrective against the temptation to bolt on skills / planners / credit assignment all at once.
- **Read time:** ~3 hours for the paper + ablation. Code is open.

---

## #2. **VLMCache: Efficient On-Device Vision-Language Model Inference**
- **ACM:** https://dl.acm.org/doi/abs/10.1145/3745756.3809243
- **Why this one:** This is the **single highest-ROI paper for the wearable path**. 1.4–3.8× speedup on on-device VLM inference with <1% accuracy loss. Disaggregates visual input into stable (background) and dynamic (foreground) blocks, caches the stable blocks as a KV-cache prefix, recomputes only the dynamic blocks. The semantic disaggregation is robust to noise.
- **The lesson for Danlab:** the Dan Glasses "watchful" mode spends 95%+ of its time on near-static scenes (a desk, a conversation, a room). Caching the visual KV prefix is **the right architectural choice for always-on wearable vision**. The 3.8× upper bound means we go from 10–15s/frame to ~3–4s/frame on x86_64 CPU, or from a 250ms target to ~65ms on aarch64+NPU.
- **What to take from it:**
  - Wire VLMCache's stable/dynamic block split into perceptiond's `SalienceDetector`. Static blocks → cache prefix; dynamic blocks → VLM inference.
  - The paper's "isolate-then-fuse" strategy preserves global attention. Replicate it in our pipeline.
  - **Pare this with VisionTrim (training-free token compression, 2–3× speedup) and SpecVLM (speculative decoding, 1.5–2.9×).** Stacking these techniques is the v1.5 path to real-time on-device VLM.
- **Read time:** ~2 hours. The technique is straightforward to implement.

---

## #3. **TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents**
- **OpenReview:** https://openreview.net/forum?id=Pq7tTNLgQh
- **Why this one:** TiMem is the SOTA on LoCoMo (75.30%) and LongMemEval-S (76.88%), and reduces recalled memory length by 52% on LoCoMo. The Temporal Memory Tree (TMT) is the cleanest hierarchical memory design I've seen — it consolidates observations into progressively abstract persona representations without fine-tuning the backbone model.
- **The lesson for Danlab:** our memoryd is a flat SQLite + flat cosine. To credibly call Dan Glasses a "personal intelligence that learns," we need hierarchical memory. TiMem's TMT is the right shape: raw events → episodic → semantic → procedural → schema, consolidated by semantic-guided, complexity-aware recall. The 52% length reduction is critical for the "first-token" latency budget — we can't ship 5000-token recall prompts to a 1B on-device LLM.
- **What to take from it:**
  - **v1.5:** Add temporal + confidence + relational scoring on top of the existing flat store. (This is the cheap delta. ~2 weeks.)
  - **v2:** Add the Temporal Memory Tree. The "nighttime engine" in DPCM is the right consolidation pattern.
  - The complexity-aware recall is the right pattern for our on-device LLM context budget.
- **Read time:** ~3 hours. Code is public.

---

## #4. **Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?**
- **Microsoft Research:** https://www.microsoft.com/en-us/research/publication/do-proactive-agents-really-need-an-llm-to-decide-when-to-wake-and-what-to-anchor/
- **Why this one:** This is the **cleanest argument against running an LLM in the wake-loop of a wearable**. 4–7× speedup over LLM-as-trigger on GPU, 12–83× on consumer hardware, 220 MiB BF16 footprint, improved trigger accuracy (mean F1 +46.0 across 14 backbones). Treats user activity as a continuous graph, uses a temporal-graph-learning encoder to produce per-event trigger probabilities, only invokes the LLM when a trigger fires.
- **The lesson for Danlab:** the wearable power budget is dominated by *when* we run the LLM, not by the LLM itself. A lightweight graph-based trigger that decides "should the assistant speak now?" at <1mW is the right architecture. The LLM is reserved for the final user-facing action, which fires <1% of the time.
- **What to take from it:**
  - **This is the v1.5 design for OpenClaw's proactive trigger layer.** Don't call the LLM on every event. Use a graph-encoder trigger.
  - The 220 MiB BF16 footprint means this fits in the wearable's memory budget trivially.
  - Pair with Sensible Agent (UMD 2026) for the *modality choice* (visual vs. audio vs. silent icon) when the trigger fires.
- **Read time:** ~2 hours. The trigger architecture is the takeaway; the LLM interaction is secondary.

---

## #5. **SIA: Self-Improvement Architecture** (Hexo Labs, MIT, May 2026)
- **GitHub:** https://github.com/HexoLabs/SIA
- **Why this one:** SIA is the **only credible open path to harness+weights self-improvement in 2026** that we've found. Hexo Labs released it in May 2026, MIT-licensed. It's the framework we should fork when we're ready to move danlab-multimodal from "pre-RL scaffold" to "actual RL."
- **The lesson for Danlab:** danlab-multimodal's README is honest: "We do not modify model weights. We do not run policy gradient or any RL algorithm. We will not call this RL until the harness+weights modification is open and auditable. The credible path is the SIA framework." That sentence is the integrity statement that makes the rest of the project trustworthy. **Reading SIA's code is the prerequisite for the Tier 3 plan** (fork SIA, integrate as a harness, run the heuristic-vs.-learned-vs.-TT-SI-vs.-SIA ablation).
- **What to take from it:**
  - The harness interface. What does a SIA-compatible harness look like? How does it expose the model's forward pass for weight updates?
  - The reward-model interface. How does SIA consume a reward signal (heuristic, learned, or human)?
  - The rollout / trajectory format. This is the contract between danlab-multimodal's loop and SIA's training loop.
- **Read time:** ~4 hours including a skim of the code. This is the most engineering-heavy of the five.

---

## What about the rest?

These five are the **highest-leverage picks**. Other papers worth reading in Q4 2026 / Q1 2027, after the v1.5 plan is in motion:

- **TT-SI: Self-Improving LLM Agents with Test-Time Training** (https://openreview.net/forum?id=k30IrbNYSG) — the test-time training playbook for when we want a lighter alternative to SIA.
- **SAGE: Multi-Agent Self-Evolution for LLM Reasoning** (https://openreview.net/forum?id=7sOeRzBzjB) — the multi-agent self-evolution pattern for when DanClaw has 3+ live agents and we want them to co-evolve.
- **Tiny but Mighty: Nanomind** (https://arxiv.org/abs/2510.05109) — the software/hardware co-design playbook for the wearable power budget. 18.8h on 2000 mAh for a 0.5B VLM is the target.
- **ContextAgent: Context-Aware Proactive LLM Agents** (NeurIPS 2025) — the proactive AI benchmark (ContextAgentBench, 1000 samples, 9 scenarios, 20 tools) we'll need to evaluate our proactive trigger layer.
- **DPCM: Memory Beyond Recall** (https://openreview.net/forum?id=ywl53zPXu0) — the dual-process memory design for v2.
- **SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning** (https://openreview.net/forum?id=By7Pj576U3) — the skill-bank pattern for "knows your workflow."

---

## Reading order for the team

| Week | Paper | Owner |
|------|-------|-------|
| W1 | VLMCache (#2) | DAN-3 (perceptiond) |
| W1 | AEL (#1) | DAN-2 (audiod) + DAN-4 (memoryd) |
| W2 | TiMem (#3) | DAN-4 (memoryd) |
| W2 | Proactive Triggers (#4) | DAN-1 (OpenClaw + power) |
| W3 | SIA (#5) | somdipto + DAN-2 (research) |
| W4 | Re-read all 5 as a group, write a 1-page synthesis per paper | all |

---

## One more thing

The point of these five isn't to make Danlab an academic group. It's to **collapse the distance between "what's published" and "what we ship"**. Every paper above has open code. The v1.5 plan incorporates every one. The next move is to read them, prototype, and ship.

*👾*
