# Top 5 Papers to Read v13 — Danlab AGI Team
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 09:30 IST
**Supersedes:** dan2-papers-to-read.v12 (24 hours old)

---

## Why these five (v13 deltas from v12)

The v12 list (SIA, OpenGlass, HRM-Text, Eywa, SpatialWorld) is **still right** for the long-form technical background. v13 adds three new papers/projects that *just* shipped in the last 72 hours and are now operationally critical:

1. **SIA (Hexo Labs, May 2026)** — unchanged from v12. The credible upgrade path for danlab-multimodal. v13: now implementable with GLM-5.2 (open, MIT, 1M context) as the Feedback-Agent.
2. **OpenGlass (arXiv:2606.07431, June 2026)** — unchanged from v12. The SOTA reference architecture for ultra-low-power AI eyewear.
3. **HRM-Text-1B (Sapient AI, May 2026)** — unchanged from v12. The on-device "thinker" bet.
4. **User-as-Code (UaC, arXiv:2606.16707, June 16 2026)** — **NEW v13.** 78.8% on LOCOMO. The user-model schema for the SIA user model.
5. **Mnemosyne (AxDSan, 2026, ICLR 2026 BEAM + LongMemEval benchmarks)** — **NEW v13.** 98.9% Recall@All@5. The runner for the v1.5 memory workstream.
6. **(Stretch) Box v3.1.0 (jegly/Box, June 2026)** — **NEW v13.** First on-device NPU acceleration for sub-2B models. The wearable v2 silicon datapoint.

Dropped from v12 (still on the read list, but no longer top-5):
- **Eywa** (arXiv:2605.30771, May 2026) — kept on the read list as schema reference, but Mnemosyne is the runner now. v12's #4.
- **SpatialWorld** (arXiv:2606.09669, June 2026) — kept on the read list. v12's #5.

## 1. SIA: Self-Improving AI with Harness & Weight Updates

**Citation.** Hebbar et al., 2026. arXiv:2605.27276. Open source at `github.com/hexo-ai/sia`. MIT license.

**Why read.** v12 said "the most important paper of 2026 for Danlab." v13 confirms. The SIA-W+H workstream (W2 + W13) is the path from heuristic to genuine RSI.

**v13 delta:** the Feedback-Agent is now **GLM-5.2** (Z.ai, June 14 2026), not Claude-class or GPT-class. 1M context, MIT, $2/hr on H100, ranks #2 on PostTrainBench. v12 said "Claude or GPT" — v13 corrects.

**What to extract.** Unchanged from v12:
- Meta-Agent / Feedback-Agent separation.
- SIA-H vs SIA-W+H ablation.
- Profile system in `hexo-ai/sia`. CLI: `sia run`, `sia web`.

**Decision it enables.** Fork SIA, swap Feedback-Agent to GLM-5.2, run SIA-H on existing screenshot trajectories. **Time: 6 weeks** (down from v12's 8 weeks because GLM-5.2 is cheaper than a cloud API).

## 2. OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision

**Citation.** Anonymous (open review), arXiv:2606.07431, June 2026.

**Why read.** Unchanged from v12. The SOTA reference for ultra-low-power AI eyewear. 11.5 hours on 200 mAh, 78.3 ms inference. The lesson is **wake-on-event**, not the specific gesture model.

**v13 delta:** the W12 wake-on-event primitive now targets **sub-50 mW idle** (down from v12's 500 mW target) based on the Box v3.1.0 NPU datapoint. The OpenGlass architecture is the right reference for both the hardware event camera path and the software V4L2 background-frame-diff path.

**Decision it enables.** W12 (6 weeks, lowered idle target to 50 mW). Owner: Dan2.

## 3. HRM-Text-1B: Efficient Pretraining Beyond Scaling

**Citation.** Sapient Intelligence, May 2026. Model: `sapientinc/HRM-Text-1B` on Hugging Face. Paper title: "HRM-Text: Efficient Pretraining Beyond Scaling."

**Why read.** Unchanged from v12. The `dan-glasses/AGENTS.md` file names HRM-Text (1B) as the current model strategy. The team needs to internalize the architecture before integrating it.

**v13 delta:** add LFM2.5-Thinking (Liquid AI, on-device reasoning) to the v14 benchmark. The wearable v2 silicon plan now has **two** on-device reasoning candidates.

**Decision it enables.** W14 spike: benchmark HRM-Text-1B vs LFM2.5-Thinking on the memory consolidation test set. Time: 2 weeks. Owner: Dan2.

## 4. User-as-Code: Executable Memory for Personalized Agents (NEW v13)

**Citation.** arXiv:2606.16707, June 16 2026. cs.AI.

**Why read.** A new paradigm for AI memory. The user's model is a **living software project**: typed Python objects hold the user's state, and ordinary Python functions encode the rules that govern it. The enabling mechanism is a **two-phase pipeline** that turns raw conversation into this code — an append-only log that never discards a fact, periodically checkpointed into structured, typed code. A design long used in database systems, applied to LLM memory for the first time.

**What to extract.**
- The two-phase pipeline (append-only log → typed Python checkpoint) is a database-systems pattern. v13: implement the SIA user model as a UaC module on top of Mnemosyne.
- 78.8% on LOCOMO competitive with full-context upper bound and strongest prior memory systems.
- "An interpreter can run" — the user model is executable. v13: implement the SIA Meta-Agent's scaffold generator as a UaC codegen pass.

**Decision it enables.** W9.5 (Week 3-4 of memoryd v1.5): implement the UaC user-model schema as a Mnemosyne data layer. Owner: Dan2.

**How to read.** Read in full. ~2 hours. This is the v13 most-actionable new paper.

## 5. Mnemosyne: The Zero-Dependency, Sub-Millisecond AI Memory System (NEW v13)

**Citation.** AxDSan, 2026. Open source at `github.com/AxDSan/mnemosyne`. ICLR 2025 LongMemEval + ICLR 2026 BEAM benchmark results.

**Why read.** 98.9% Recall@All@5 on LongMemEval (with bge-small-en-v1.5 embedding). 100 instances, April 2026. One SQLite file, zero cloud dependencies. Hermes-first, but **OpenClaw native provider exists** (`pip install mnemosyne-memory[openclaw]`).

**v13 delta:** this is the v12 "build consolidation from scratch" plan, replaced. Mnemosyne handles retrieval, consolidation, scoping, and (most of) provenance. The workstream W9 is now 6 weeks instead of 12.

**What to extract.**
- The OpenClaw provider: `provider: mnemosyne.integrations.openclaw:create_provider` in `openclaw.json`.
- The explicit memory pin: `plugins.slots.memory = "memory-core"` to avoid the documented default-loads-wrong-provider bug.
- The benchmark: BEAM ICLR 2026 + LongMemEval ICLR 2025, both top-tier scores.
- The zero-dependency SQLite architecture — fits the v12 PRD §7.3 "Memory: SQLite + flat vectors" shape.

**Decision it enables.** W9 (Day 1-3): install `mnemosyne-memory[openclaw]`, set the explicit memory pin, verify the 98.9% number on the danlab-multimodal screenshot set. The rest of W9 (LFM2.5-Embedding-350M, LFM2.5-ColBERT-350M, Eywa provenance, UaC schema, RHO consolidation) builds on Mnemosyne. Owner: Dan2.

**How to read.** README + benchmark notes. ~1 hour.

## 6. (Stretch) Box v3.1.0: First On-Device NPU Acceleration (NEW v13)

**Citation.** Not a paper. Project: `github.com/jegly/Box`, v3.1.0, June 2026.

**Why read.** Box is the first on-device AI suite where **NPU acceleration actually works on Snapdragon and MediaTek** for the Gemma 3 1B model. Previous builds shipped the NPU models but crashed on load. v3.1.0 also slides the context window so the chat keeps going.

**Why this is the wearable v2 unlock.** v12 said "NPU not yet for sub-2B models" — v13 says it works. The wearable v2 silicon plan (W19) is now hybrid CPU+NPU. The vision encoder (the ~86M-param part of LFM2.5-VL-450M) can run on a 2026 mobile NPU, leaving the text decoder on CPU. The wearable idle power drops from ~500 mW target to sub-50 mW.

**What to extract.**
- The Snapdragon NPU build works for Gemma 3 1B. Measure for LFM2.5-VL-450M vision encoder.
- The MediaTek NPU build works. Cross-vendor validation matters.
- The context-window slide is a UX primitive — applies to any LLM on a memory-constrained device.

**Decision it enables.** W19 (12-month workstream): identify and validate a 12-TOPS-class NPU wearable SoC. The candidate list is: Snapdragon 8 Gen 3+ wearable variants, MediaTek Dimensity 9200+ wearable variants, MediaTek Genio Pro 5100. Time: 12 weeks. Owner: Hardware partner.

**How to engage.** Read the Box v3.1.0 release notes. Run the Gemma 3 1B NPU build on a Snapdragon reference phone. Document the watts-per-token in `agent-work/box-npu-benchmark.md`.

## Reading order

1. **SIA** — read in full. 3 hours. Owner: every engineer. (Unchanged from v12.)
2. **OpenGlass** — read for the architecture. 2 hours. Owner: Dan2, Dan3. (Unchanged from v12.)
3. **Mnemosyne README + benchmark** — 1 hour. Owner: Dan2. **NEW v13 priority** (operationally critical).
4. **User-as-Code (UaC)** — read in full. 2 hours. Owner: Dan2. **NEW v13 priority** (user-model schema).
5. **HRM-Text** — HF model card + architecture. 1.5 hours. Owner: Dan2. (Unchanged from v12.)
6. **Box v3.1.0 release notes** — 30 min. Owner: Hardware. **NEW v13 stretch.**

Total: ~10 hours. One week, distributed.

## What we are NOT reading this quarter (unchanged from v12)

- Frontier model internal technical reports.
- GRPO / PPO fine-tuning papers (read after SIA-W+H is benchmarked).
- Vector DB papers (HNSW choice is made).
- `paperswithcode` SOTA leaderboards.

## What we ADDED to the read list (v13)

- **OpenClaw skill malware guide (Skywork, June 2026)** — operational, not academic. Read this week. 30 min.
- **GLM-5.2 technical report (Z.ai, June 14 2026)** — IndexShare architecture. 1 hour.
- **Brilliant Labs Halo public docs** — buy one, read the repo. 1 hour.
- **Apple memory chip pricing WSJ article (June 18 2026)** — informs the storage tier spec. 15 min.

*End of paper list. Own your reading. 👾*
