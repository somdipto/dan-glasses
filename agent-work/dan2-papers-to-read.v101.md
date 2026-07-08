# Top 5 Research Papers — v101 (Dan2, 2026-06-29)

**Author:** Dan2 (👾) | **Selection rule:** highest-leverage for Danlab's 6/12/24-month roadmap (Dan Glasses v1, harness RL loop, on-device companion).

Read in this order. Each paper is paired with **why Danlab cares**, **what to extract**, and **assigned owner**.

---

## 1. **Darwin Gödel Machine** (Sakana AI + UBC, ICLR 2026)
**arXiv:** https://arxiv.org/abs/2505.22954  
**Read by:** Dan4, Dan2  
**Why:** First empirical self-improving coding agent with measured gains (SWE-bench 20%→50%). Validates the "harness as the right RL target" thesis that anchors our SIA paper.  
**Extract for Danlab:**
- Archive-and-mutate-loop structure (variant → measure → keep if better).
- Sandboxing + safety constraints for self-modifying code (we need this for `learningd`).
- The bound on improvement per generation — empirically what's the ceiling?

## 2. **Hierarchical Reasoning Model (HRM)** (Sapient Inc., Jun 2025)
**arXiv:** https://arxiv.org/abs/2506.21734  
**Read by:** Dan2, Dan3  
**Why:** Our locked-in planner head (HRM-Text 1B) is based on this. Need to deeply understand the two-module recurrent architecture, training distribution, and limits. **Important:** HRM is trained on ARC-AGI puzzles, not chat — so we need a chat head on top (see model-analysis §4).  
**Extract for Danlab:**
- The coupled-recurrent-module math (high-level summary, not full derivations).
- Benchmark results on ARC-AGI 1+2 to estimate ceiling.
- Where HRM breaks: out-of-distribution generalization, language modeling quality.

## 3. **Letta Memory Models: Towards Agents That Learn** (Letta, Jun 2026)
**URL:** https://www.letta.com/blog/towards-agents-that-learn/  
**Read by:** Dan4  
**Why:** The most-recent 2026 statement on memory-native RL for agents. Mirrors our SIA thesis (RL the harness, not the weights) but applies it specifically to the **memory controller**. Closest published reference for what `memoryd` + `learningd` should look like in production.  
**Extract for Danlab:**
- The "memory model" abstraction: a small RL-trained policy that decides *what to write, what to recall, what to forget*.
- Training signal: user dwell, retry, rating. (Matches our existing feedback collector.)
- Architectural split: USER.md + MEMORY.md + episodic + procedural. (Already locked in.)

## 4. **Sakana DGM safety analysis** (Sakana AI, 2025)
**arXiv:** https://arxiv.org/abs/2505.22954 (same paper, focus on §6 safety)  
**Read by:** Dan2 (architect), somdipto (founder review)  
**Why:** DGM is the closest analogue to our `learningd`. Sakana flagged concrete failure modes that we will hit:
- Self-rewriting code may introduce alignment drift.
- Sandboxing must be airtight; rewards must be tamper-resistant.
- Empirical validation on benchmarks ≠ validation on real-world deployment.
- Limitation: only code-editing domain, not general agents.  
**Extract for Danlab:**
- Safety checklist for `learningd` v1 (no live traffic modification, shadow-mode first, A/B before promote).
- What the field considers an acceptable self-improvement loop.

## 5. **Liquid AI LFM2.5-VL-450M blog + GGUF model card** (Liquid AI, Apr 2026)
**URL:** https://www.liquid.ai/blog/lfm2-5-vl-450m  
**GGUF:** https://huggingface.co/LiquidAI/LFM2.5-VL-450M-GGUF  
**Read by:** Dan3 (primary), Dan1 (vision pipeline integration)  
**Why:** This is the production vision model for Dan Glasses v1. We need to understand its strengths, failure modes, and structured-output APIs (bounding boxes, function calling).  
**Extract for Danlab:**
- Bounding box output schema and prompt templates.
- BFCLv4 function-calling format — integrate into `toold` directly.
- 128K context window implications for multi-frame perceptiond.
- Sub-250ms edge inference benchmarks on Snapdragon 8 Elite — characterize on our target hardware.

---

## Bonus papers if time permits

- **Mem0 vs Letta comparison 2026** — https://vectorize.io/articles/mem0-vs-letta — for memoryd component decisions.
- **Hermes Agent memory architecture** — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory — for production reference.
- **MCP adoption statistics 2026** — https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol — for interop strategy.
- **darwin-godel-machine GitHub repo** — https://github.com/jennyzzt/dgm — read the README and example `coding_agent.py`.

---

## Reading schedule

- **Week 1:** Paper #1 (DGM) + Paper #5 (LFM2.5-VL) — directly unblocks Dan4 + Dan3.
- **Week 2:** Paper #2 (HRM) + Paper #3 (Letta Memory Models) — clarifies the planner + memory architecture.
- **Week 3:** Paper #4 (DGM safety analysis) — gated before `learningd` ships.
- **Week 4:** Bonus papers, integrate into design docs.

---

## v101 changes from v100

- **Dropped**: stale memoryRAG papers that v100 covered but no longer feel prioritized.
- **Added**: Letta Memory Models (Jun 2026) — freshest reference for harness-RL on memory.
- **Upgraded**: HRM (Sapient Inc.) added as **#2** because we now know HRM-Text 1B is locked but it has chat-head weakness — paper is mandatory background.
- **Pivoted**: Liquid AI LFM2.5-VL-450M promoted from "blog post to skim" to "top 5 paper-equivalent" because it is now production-bound.
- **Reorganized**: each paper now has read-by owner assigned (Dan1/Dan2/Dan3/Dan4).
- **Added**: explicit week-by-week reading schedule.
