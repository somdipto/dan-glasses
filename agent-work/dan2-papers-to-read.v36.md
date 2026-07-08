# Top 5 Papers to Read — Dan2 v36 (2026-06-21)

> **Scope.** Five papers the Danlab team should read this month, picked for direct relevance to Danlab's near-term work (SIA fork + dglabs-eval, memoryd v2, on-device proactive AI, VLM speedup, and India-first positioning). Read in this order. Each pick includes the concrete Danlab application.

---

## Why these 5 (v36 update)

The Jun 2026 literature is dominated by "harness + weight updates" work (SIA, Meta-Harness, Darwin Family, POISE, AEL). v36 picks 2 papers from that frame (SIA itself + Meta-Harness) because **the eval is the moat**, and SIA + Meta-Harness together define the modern eval-harness contract. The remaining 3 picks are direct levers on Danlab's product: visual memory, agent memory, and VLM speedup.

Read order:
1. **SIA** — defines the framework Danlab will fork.
2. **Meta-Harness** — defines the harness-search contract Danlab needs to understand to design dglabs-eval.
3. **VisualMem** — defines the missing dimension (visual memory) for AI companions; direct application to memoryd v2.
4. **LightGMEM** — the most deployable graph-on-vector memory architecture in 2026; direct application to memoryd v2.
5. **V5e-0** — the training-free VLM speedup Dan3 needs to ship to make perceptiond usable on the wearable target.

---

## Pick 1 — SIA: Self Improving AI with Harness & Weight Updates

**Authors:** Hebbar et al. (Hexo Labs)
**Year:** May 2026
**License:** MIT (code at github.com/hexo-ai/sia)
**Why this is #1:** This is the framework Danlab is forking. **Understanding SIA is understanding the SIA-fork plan in dan2-agi-roadmap.md Month 1, Action 5.**

### What it does
A self-improvement loop with three agents:
- **Meta-Agent:** reads the task, generates the initial target agent.
- **Target Agent:** executes the task.
- **Feedback Agent:** evaluates the output, proposes harness and/or weight updates.

Both harness AND weights can be updated. The framework ships a CLI (`sia run`, `sia web` for visualization) and is verified to improve LawBench performance by +56.6% over baseline.

### Why it matters for Danlab
- **Danlab will fork this**, not build from scratch.
- **dglabs-eval becomes SIA's verifier** — the eval Danlab builds becomes the moat.
- **LFM2.5-1.2B-Thinking (or HRM-Text 1B) is the Feedback-Agent** — the eval signal from Dan Glasses' on-device behavior feeds back to the Feedback-Agent, which proposes harness changes.
- **SIA's weight-update path is gated** on the harness being mature enough. Danlab's 6-month harness-first sprint aligns.

### Concrete Danlab application
- **Month 1:** Fork `hexo-ai/sia` into `danlab-multimodal/sia/`. Wrap `src/demo.py`'s heuristic scorer as SIA verifier.
- **Month 2-3:** Build `dglabs-eval` as the verifier. SIA fork runs against it.
- **Month 4-6:** Enable weight-update path. First reproducibility benchmark.

### Reading time
- Paper: ~30 min
- Code: 1-2 days to fork + integrate
- **Priority:** Highest. Read first.

---

## Pick 2 — Meta-Harness: Post-Training Reliable Agent Systems via Harness Search

**Authors:** Chelsea Finn et al.
**Year:** 2026 (OpenReview, posted Jun 2026)
**License:** Open (paper + reference code)
**Why this is #2:** Defines the harness-search contract that dglabs-eval needs to support. **Without understanding Meta-Harness, Danlab's eval design will miss the "search over harness" abstraction.**

### What it does
Searches over agent-systems configurations (what to store, retrieve, show the model) using execution traces from prior candidates. Specifically targets long-horizon failures.
- **TerminalBench-2:** Meta-Harness > Terminus-KIRA on Claude Opus 4.6; #1 among reported Claude Haiku 4.5 agents.
- **Online text classification:** +7.7 points vs state-of-the-art context-management; 4× fewer context tokens.
- **Retrieval-augmented math reasoning:** +4.7 points across 5 held-out models on 200 IMO-level problems.

### Why it matters for Danlab
- **dglabs-eval must support harness search**, not just score outputs. Otherwise SIA's Meta-Agent has nowhere to search.
- The 3 measurements (TerminalBench-2, online classification, IMO-level math) define **the kind of task battery** dglabs-eval needs.
- **"4× fewer context tokens"** is the right efficiency target for memoryd v2.

### Concrete Danlab application
- **dglabs-eval v1 design:** must support harness search as a primitive, not as an afterthought. Steal Meta-Harness's task battery structure (held-out, transfer, replay).
- **memoryd v2:** context-management as a first-class eval target.
- **perceptiond v3:** salience-gating as a harness choice, not a model choice.

### Reading time
- Paper: ~30 min
- Reference code: 1 day to study
- **Priority:** High. Read second, before designing dglabs-eval.

---

## Pick 3 — VisualMem: Personal Visual Memory from Explicit and Implicit Evidence

**Authors:** (per arXiv:2605.28806)
**Year:** 2026 (Jun 2026)
**License:** Open (arXiv)
**Why this is #3:** Defines the missing dimension for AI companions — visual memory. **Dan Glasses has a camera; current memory architectures throw visual data away.** This is the paper that shows why that's a mistake.

### What it does
Maintains structured visual memories for recurring people, user-associated assets, ownership, and durable visually grounded facts. Contrasts with caption-based storage (Mem0, MemOS, SimpleMem) which loses fine-grained visual detail.
- **Evaluated against:** Naive LLM (Full Context, Oracle), Self-RAG, HippoRAG2 (RAG-based), LightMem, SimpleMem, Mem0, MemOS (memory-based).
- **Uses MemOS as default text-memory backend** — visual memory + text memory, integrated.
- **Long-term, persistent, structured visual representations.**

### Why it matters for Danlab
- **Dan Glasses has a camera running 24/7** (perceptiond watchful mode). Currently the perceptiond ring buffer stores text descriptions only.
- **VisualMem pattern = store 1 image per salient event + visual embedding for similarity search.**
- Direct synergy with perceptiond's existing ring buffer.
- **First open-source implementation of visual memory for AI companions.** Danlab could ship the first open visual-memory layer for wearables.

### Concrete Danlab application
- **memoryd v2 adds VisualMem pattern:** perceptiond's salient-event descriptions + 1 thumbnail image + visual embedding for similarity search.
- **memoryd v2 query path:** "Show me where I was when I last saw X" — recall by current frame similarity.
- **First open visual-memory implementation.** Publishable. Citeable.

### Reading time
- Paper: ~20 min
- Implementation: 1-2 weeks (memoryd v2 sprint)
- **Priority:** High. Direct moat-relevant.

---

## Pick 4 — LightGMEM: Lightweight Agent Graph Memory Generation

**Authors:** (ACL ARR 2026 long paper)
**Year:** 2026 (Jun 2026)
**License:** Open (ACL ARR)
**Why this is #4:** The most deployable graph-on-vector memory architecture in 2026. **Direct application to memoryd v2.**

### What it does
Lightweight graph-based memory system for LLM agents:
- **Entity extraction:** GLiNER2 (zero-shot NER) instead of per-episode LLM extraction. **58× fewer LLM calls than Zep baseline.**
- **Disambiguation:** conflict-lane partitioning for overlapping candidate mentions.
- **Community structure:** Ego-Splitting for overlapping communities.
- **Construction:** **151× faster than Zep baseline.**
- **Multi-session QA (LoCoMo):** strong performance. Single-session (LongMemEval): competitive.

### Why it matters for Danlab
- **memoryd v2 = vectors + graph + visual memory.** Graph layer is non-optional for long-horizon recall.
- **GLiNER2** is the right extraction primitive for memoryd v2 — zero-shot, no LLM cost per extraction.
- **58× fewer LLM calls = 58× cheaper memory operations.** Sustainable at edge.
- **Ego-Splitting communities** match Danlab's mental model (perceptiond event clusters, memoryd entity clusters, both communities).

### Concrete Danlab application
- **memoryd v2 = LightGMEM-style graph + vectors + VisualMem.** 6-week sprint after VLM speedup ships.
- **memoryd `/graph` endpoint** for entity-relation queries alongside the existing `/query` endpoint.
- **Performance target:** 58× fewer LLM calls than baseline.

### Reading time
- Paper: ~25 min
- Implementation: 1-2 weeks
- **Priority:** High. Direct memoryd v2 architecture input.

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
- **Highest-leverage sprint in v36.** 2-week scope.

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

- **Darwin Family** — training-free model merging. **Interesting, but Danlab isn't merging models.** Cite if we do multi-model experiments.
- **POISE** — LLM-discovered RL algorithms. **Useful background; not immediate Danlab work.**
- **AEL** — Thompson Sampling over memory policies. **Interesting for memoryd v3 (after v2 ships); not v2.**
- **SEAGym** — eval harness. **Already incorporated into dglabs-eval design via Meta-Harness.**
- **AtomMem, DPCM, GraP-Mem, FwPKM, MemRefine** — all worth reading for memoryd v3 design. **Defer.**
- **Wavelet-driven CFM TTS** — relevant for ttsd v2 (Indic). **Defer.**
- **TRACE, SEER, AWA-RL, SkillsVote, SEAGym, HERO** — research direction. **Read if/when we ship dglabs-eval v1.**

---

## Reading order summary

1. **This week:** SIA paper + code. Fork + first demo.
2. **Week 2:** Meta-Harness. Design dglabs-eval.
3. **Week 3:** V5e-0. Start perceptiond v3 sprint.
4. **Week 4:** LightGMEM. Plan memoryd v2.
5. **Week 5:** VisualMem. Plan memoryd v2 visual layer.

---

*Dan2 papers-to-read, 2026-06-21 v36. Adds VisualMem + V5e-0 to v35's list (SIA, Meta-Harness, LightGMEM were already v35 picks); sharpens the read order with concrete Danlab applications.*
