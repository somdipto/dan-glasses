# Top 5 Papers to Read — Dan2 v37 (2026-06-22)

> **Scope.** Five papers the Danlab team should read this month. v37 picks replace v36's list because: (a) **SIA v2 (May 28, 2026) has verified numbers now**, (b) **Self-Harness (Shanghai AI Lab, Jun 8, 2026) is the on-device default**, (c) **Agents of Chaos (Tomer Ullman, Feb 2026) is the safety source**.

## Why these 5 (v37 update)

The Jun 2026 literature has consolidated around three things: (1) SIA v2 has measurable wins on LawBench (70.1%, +25.1 SOTA) and CUDA kernels (91.9% reduction), (2) Self-Harness (Shanghai AI Lab, Jun 8 2026) is the harness-only alternative for on-device deployment, (3) Agents of Chaos (Ullman, Feb 2026) is the empirical source for what goes wrong with AI agents.

v37 picks: **SIA v2** (the framework Danlab forks), **Self-Harness** (the on-device companion), **Agents of Chaos** (the safety source), **ProAgent** (the proactive AI counter-claim), **V5e-0** (the VLM speedup that makes the wearable target achievable).

Read order:
1. **SIA v2** — defines the framework Danlab will fork.
2. **Self-Harness** — defines the on-device companion architecture.
3. **Agents of Chaos** — defines the safety benchmark dglabs-eval must include.
4. **ProAgent** — defines the proactive AI counter-claim dglabs-eval must measure.
5. **V5e-0** — defines the VLM speedup Dan3 needs to ship to make perceptiond usable on the wearable target.

---

## Pick 1 — SIA v2: Self Improving AI with Harness & Weight Updates

**Authors:** Hebbar et al. (Hexo Labs, Palo Alto / Brussels / Toronto, with Oxford collaboration)
**Year:** v2 May 28, 2026 (paper arXiv:2605.27276 v2)
**License:** MIT (code at github.com/hexo-ai/sia; 1,712+ stars as of mid-Jun 2026)
**Why this is #1:** This is the framework Danlab is forking. **Understanding SIA v2 is understanding the SIA-fork plan in dan2-agi-roadmap.md Week 1, Action 2.**

### What it does
A self-improvement loop with three agents:
- **Meta-Agent:** reads the task, generates the initial target agent.
- **Target Agent:** executes the task. Logs trajectories.
- **Feedback Agent:** evaluates the output, proposes harness and/or weight updates.

Both harness AND weights can be updated. The framework ships a CLI (`sia run`, `sia web` for visualization) and supports automatic RL algorithm selection per generation:
- PPO+GAE
- GRPO
- Entropic Advantage Weighting

**Selected by the Feedback-Agent based on task reward shape, not by the developer.**

### Verified numbers (v2, May 28 2026)
- **LawBench:** 13.5% → 70.1% (+56.6% / +25.1 over SOTA). Harness-only: 50%. Harness + weights: 70.1%.
- **CUDA kernel optimization:** 1,161µs → 1,017µs (12.4% reduction in 1 iteration).
- **Single-cell RNA denoising:** 502% improvement (the simplest weight-update fix — clip/round outputs to non-negative integers — surpassed harness-only improvements).

### Stack
- Base model: GPT-OSS 120B + LoRA rank 32.
- Meta + Feedback agents: Claude Sonnet.
- Python 3.11+, `pip install 'sia-agent[claude]'` or `'sia-agent[openhands]'`.
- Backends: Claude Agent SDK or OpenHands (multi-provider: Gemini, OpenAI, Anthropic).

### Why it matters for Danlab
- **Danlab will fork this**, not build from scratch.
- **dglabs-eval becomes SIA's verifier** — the eval Danlab builds becomes the moat.
- **LFM2.5-1.2B-Thinking (or HRM-Text 1B) is the Feedback-Agent** — the eval signal from Dan Glasses' on-device behavior feeds back to the Feedback-Agent, which proposes harness changes.
- **SIA's weight-update path is gated** on the harness being mature enough. Danlab's 6-month harness-first sprint aligns.

### Concrete Danlab application
- **Week 1:** `pip install 'sia-agent[claude]'`. `sia run --task lawbench --max_gen 3`. Document results.
- **Month 1:** Fork `hexo-ai/sia` into `danlab-multimodal/sia/`. Wrap `src/demo.py`'s heuristic scorer as SIA verifier. Use LFM2.5-1.2B-Thinking as Feedback-Agent.
- **Month 2-3:** Build `dglabs-eval` as the verifier. SIA fork runs against it.
- **Month 4-6:** Enable weight-update path. First reproducibility benchmark.

### Reading time
- Paper: ~30 min
- Code: 1-2 days to fork + integrate
- **Priority:** Highest. Read first.

---

## Pick 2 — Self-Harness: Harnesses That Improve Themselves

**Authors:** Shanghai AI Lab (paper, Jun 8, 2026; CC BY 4.0)
**Year:** 2026 (Jun 8)
**License:** CC BY 4.0 (no public implementation as of mid-2026)
**Why this is #2:** **Defines the on-device companion architecture to SIA.** Where SIA requires cloud-side Claude Sonnet, Self-Harness is a regression-gated loop around a **fixed model** — the right architecture for on-device deployment.

### What it does
A regression-gated self-improvement loop that modifies only the harness (system prompts, tool wrappers, validation steps, planning templates) around a **fixed model and fixed evaluator.**
- **Held-in + held-out splits:** every proposed harness edit is tested on both. Keep only if at least one split improves and neither degrades.
- **3-5 minimal harness edits per weakness** identified in execution traces.
- **5-7 iterations until gains converge.**

### Verified numbers (Jun 2026)
- **Terminal-Bench 2.0:** 14-21 percentage point absolute improvements across 3 models. **Driven entirely by harness modifications. Base models unchanged.**
- Other domains: substantial gains on document classification, data cleaning.

### Why it matters for Danlab
- **Two-stack model: Self-Harness on-device + SIA cloud-side.** Self-Harness doesn't require cloud-side LLMs (uses the fixed on-device model). SIA requires cloud-side (Claude Sonnet). v37 architecture.
- **Self-Harness is the on-device default.** Danlab's audiod/perceptiond/memoryd/toold/ttsd services can run Self-Harness loops locally. SIA runs in the cloud.
- **Self-Harness is safer than SIA for on-device.** No weight updates. Harness edits are roll-backable.

### Concrete Danlab application
- **memoryd v2:** Self-Harness loop around all-MiniLM-L6-v2. Test harness edits (chunking, retrieval, reranking) on dglabs-eval's memory subset. Hold-out: dglabs-eval's safety subset (memory recall of sensitive info).
- **perceptiond v3:** Self-Harness loop around LFM2.5-VL-450M. Test harness edits (prompts, postprocessing, salience gating) on dglabs-eval's vision subset.
- **Month 2-3:** First Danlab self-improving service (memoryd or perceptiond).

### Reading time
- Paper: ~30 min
- Implementation: 2-3 days to build the loop by hand (no public repo)
- **Priority:** High. Read second.

---

## Pick 3 — Agents of Chaos

**Authors:** Tomer Ullman (Harvard)
**Year:** Feb 23, 2026 (arXiv:2602.20021v1)
**License:** Open (arXiv)
**Why this is #3:** **Defines the safety benchmark dglabs-eval must include.** Without Agents of Chaos, dglabs-eval is just another benchmark. With it, dglabs-eval is the safety-gated eval.

### What it does
An empirical study of what goes wrong with AI agents. Based on actual Discord conversations where agents failed.
- **12 case studies** spanning disproportionate response, non-owner compliance, sensitive info disclosure, looping, DoS, provider values, agent harm, owner identity spoofing, agent collaboration, agent corruption, libelous within communities, prompt injection via broadcast.

### Why it matters for Danlab
- **5 of 12 cases become dglabs-eval safety subset (v37 architecture review):**
  1. Disproportionate response
  2. Non-owner compliance
  3. Sensitive info disclosure
  4. Owner identity spoofing
  5. Prompt injection via broadcast
- **Weight-update gate:** a weight update that fails any safety task is **rejected.**
- **Harness-edit gate:** a harness edit that fails any safety task is **logged but not blocked** (asymmetric).

### Concrete Danlab application
- **dglabs-eval v1 includes 5 safety tasks from Agents of Chaos.**
- **Each service (audiod, memoryd, toold, os-toold, perceptiond, ttsd) has a safety subset** verified before any weight update is applied.
- **arXiv paper #1:** "dglabs-eval: a held-out, on-device, on-user, safety-gated evaluation harness for self-improving AI wearables." Cite Agents of Chaos explicitly.

### Reading time
- Paper: ~60 min (long)
- Implementation: 1-2 weeks (5 safety tasks)
- **Priority:** High. Read third, before designing dglabs-eval.

---

## Pick 4 — ProAgent: Proactive AI Agent

**Authors:** (per arXiv:2512.06721)
**Year:** 2026
**License:** Open (arXiv)
**Why this is #4:** **Defines the proactive AI counter-claim dglabs-eval must measure.** Without ProAgent, dglabs-eval doesn't measure the wedge Danlab claims. With it, Danlab has a published baseline for proactive AI.

### What it does
Proactive AI agents — agents that **initiate** rather than respond. Key insight: **27.7% higher proactive accuracy vs reactive baselines.**
- **5 proactive task types:**
  1. Motion trigger (user moves → agent acts)
  2. Scene change (environment changes → agent acts)
  3. Scheduled reminder (time-based → agent acts)
  4. Person re-identification (familiar person appears → agent acts)
  5. Off-device question (user asks later about something the agent saw → agent recalls)

### Why it matters for Danlab
- **Snap's "Proactive AI" claim (AWE 2026, Jun 16) is closed-source.** Danlab's counter: **auditable proactive AI.**
- **5 ProAgent tasks become dglabs-eval proactive subset** (v37 architecture review).
- **perceptiond + memoryd + audiod + toold can serve the proactive use case.** Proactive motion trigger = perceptiond salience + memoryd recall + audiod synthesis + ttsd output.

### Concrete Danlab application
- **dglabs-eval v1 includes 5 proactive tasks from ProAgent.**
- **perceptiond v3 proactive push:** when salience detector fires, push to OpenClaw → audiod reaction. Required for proactive subset.
- **arXiv paper #1:** Cite ProAgent explicitly.

### Reading time
- Paper: ~30 min
- Implementation: 2-3 weeks (5 proactive tasks)
- **Priority:** High. Read fourth, before designing dglabs-eval.

---

## Pick 5 — V5e-0: A Minimalist Self-Speculative Decoding Framework for Vision-Language Models

**Authors:** (OpenReview, ACL ARR 2026)
**Year:** 2026 (Jun 2026)
**License:** Open (ACL ARR)
**Why this is #5:** The training-free VLM speedup Dan3 needs to ship. **Direct application to perceptiond v3.**

### What it does
Self-speculative decoding using **only text-side hidden states** (no vision encoder call, no cross-modal updates).
- **Free-Root token** + two lightweight continuation heads.
- **Single-root depth-3 speculative tree** verified in one forward pass.
- **~1.89× wall-clock speedup** across 15 VLMs.
- **Trade-off:** slightly lower than ViSpec on TextVQA (0.31× gap) but maintains OCRBench accuracy with 1.46× speedup.

### Why it matters for Danlab
- **perceptiond v2 = 10s/frame on LFM2.5-VL-450M Q4_0.** Watchful mode (5fps) is unusable at this speed.
- **perceptiond v3 = LFM2.5-VL-450M + V5e-0 wrapper + QViD preprocessor + SWEET-style Q4/Q5/Q8 gating.**
- **Combined estimate:** 10s/frame → 2-3s/frame. Watchful mode becomes fluid.
- **Highest-leverage sprint in v37.** 2-week scope.

### Concrete Danlab application
- **perceptiond vlm.py:** wrap the existing llama-mtmd-cli call with a V5e-0-style drafter. No model retraining.
- **QViD preprocessor:** filter visual tokens before the VLM forward pass.
- **SWEET-style salience gating:** Q5 for salient frames, Q4 for non-salient. **Direct answer to v35's architecture flaw #1.**

### Reading time
- Paper: ~20 min
- Implementation: 1-2 weeks
- **Priority:** Highest. This is what makes the wearable target achievable.

---

## What to skip (and why)

These are good papers but lower-priority for Danlab's next 6 months:

- **Darwin Family** — training-free model merging. **Interesting, but Danlab isn't merging models.**
- **POISE** — LLM-discovered RL algorithms. **Useful background; not immediate Danlab work.**
- **AEL** — Thompson Sampling over memory policies. **Interesting for memoryd v3 (after v2 ships); not v2.**
- **SEAGym** — eval harness. **Already incorporated into dglabs-eval design via Meta-Harness.**
- **AtomMem, DPCM, GraP-Mem, FwPKM, MemRefine** — all worth reading for memoryd v3 design. **Defer.**
- **Wavelet-driven CFM TTS** — relevant for ttsd v2 (Indic). **Defer.**
- **TRACE, SEER, AWA-RL, SkillsVote** — research direction. **Read if/when we ship dglabs-eval v1.**

---

## v37 new: read order summary

1. **This week:** SIA v2 paper + code. `pip install 'sia-agent[claude]'`. `sia run --task lawbench --max_gen 3`.
2. **Week 2:** Self-Harness. Build the on-device loop by hand around all-MiniLM-L6-v2 (memoryd v2 candidate) or LFM2.5-VL-450M (perceptiond v3 candidate).
3. **Week 3:** Agents of Chaos. Implement 5 safety tasks for dglabs-eval v1.
4. **Week 4:** ProAgent. Implement 5 proactive tasks for dglabs-eval v1.
5. **Week 5:** V5e-0. Start perceptiond v3 sprint.

---

*Dan2 papers-to-read, 2026-06-22 v37. Replaces v36's list (SIA, Meta-Harness, VisualMem, LightGMEM, V5e-0) with SIA v2, Self-Harness, Agents of Chaos, ProAgent, V5e-0. Sharpens the read order with concrete Danlab applications.*
