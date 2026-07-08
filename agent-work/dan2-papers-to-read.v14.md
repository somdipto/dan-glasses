# Top 5 Papers to Read v14 — Danlab AGI Team
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 10:30 IST
**Supersedes:** dan2-papers-to-read.v13 (24 hours old)

---

## Why these five (v14 deltas from v13)

The v13 list (SIA, OpenGlass, HRM-Text, UaC, Mnemosyne, Box-stretch) is **still right** for the long-form technical background. v14 adds two *new* papers/projects that shipped in the last 24 hours and are operationally critical:

1. **SIA (Hexo Labs, May 2026)** — unchanged from v13. The credible upgrade path for danlab-multimodal.
2. **OpenGlass (arXiv:2606.07431, June 2026)** — unchanged from v13. The SOTA reference for ultra-low-power AI eyewear.
3. **HRM-Text-1B (Sapient AI, May 2026)** — unchanged from v13.
4. **User-as-Code (UaC, arXiv:2606.16707, June 16 2026)** — unchanged from v13. The user-model schema.
5. **Mnemosyne (AxDSan, 2026)** — unchanged from v13. The memory runner.
6. **(Stretch) Box v3.1.0** — unchanged from v13.

**NEW v14 picks:**
7. **Arbor (Renmin University + Microsoft Research, June 18 2026)** — **NEW v14.** 2.5× faster than Claude Code/Codex on real engineering tasks under same compute. First public benchmark of "cumulative learning > trial-and-error" in autonomous optimization. The SIA Meta-Agent pattern validated at engineering-task level.
8. **Qualcomm Snapdragon Start announcement (June 17 2026)** — **NEW v14.** Not a paper but the silicon path that unlocks wearable v2. Read the program brief + Inspecs case study.

## 1. SIA: Self-Improving AI with Harness & Weight Updates

**Citation.** Hebbar et al., 2026. arXiv:2605.27276. Open source at `github.com/hexo-ai/sia`. MIT license.

**Why read.** v12 → v13 → v14: still the most important paper for Danlab.

**v14 delta:** Run SIA-H alongside Arbor (W2.5) to compare two approaches to the same problem. **SIA-H** writes harness + LoRA weights; **Arbor** writes code cumulatively. Both are AO loops; different shapes.

**Decision it enables.** W2 (SIA-H fork) + W2.5 (Arbor benchmark) + W13 (SIA-W+H).

## 2. OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision

**Citation.** Anonymous (open review), arXiv:2606.07431, June 2026.

**Why read.** Unchanged from v13. 11.5 hours on 200 mAh, 78.3 ms inference.

**v14 delta:** The Snapdragon Start silicon path (W19) may enable even lower idle power. The OpenGlass reference architecture is the right comparison point for both software and hardware paths.

**Decision it enables.** W12 (6 weeks, sub-50 mW idle target).

## 3. HRM-Text-1B: Efficient Pretraining Beyond Scaling

**Citation.** Sapient Intelligence, May 2026. Model: `sapientinc/HRM-Text-1B` on Hugging Face.

**Why read.** Unchanged from v13.

**v14 delta:** The OpenAI Shazeer move (architecture research lead) **validates** non-transformer architecture work. HRM's hierarchical recurrent premise is no longer contrarian. **Confidence bump on the wearable v2 silicon plan.**

**Decision it enables.** W14 spike: HRM-Text-1B vs LFM2.5-Thinking on memory consolidation test set.

## 4. User-as-Code: Executable Memory for Personalized Agents

**Citation.** arXiv:2606.16707, June 16 2026. cs.AI.

**Why read.** Unchanged from v13. Living software project as user model. 78.8% on LOCOMO.

**Decision it enables.** W9.5 (Week 3-4 of memoryd v1.5).

## 5. Mnemosyne: The Zero-Dependency, Sub-Millisecond AI Memory System

**Citation.** AxDSan, 2026. `github.com/AxDSan/mnemosyne`. ICLR 2025/2026 benchmarks.

**Why read.** Unchanged from v13. 98.9% Recall@All@5 on LongMemEval. OpenClaw native provider.

**Decision it enables.** W9 (Day 1-3 install + memory pin fix).

## 6. (Stretch) Box v3.1.0: First On-Device NPU Acceleration

**Citation.** Project: `github.com/jegly/Box`, v3.1.0, June 2026.

**Why read.** Unchanged from v13. Snapdragon + MediaTek NPU acceleration for Gemma 3 1B works.

**v14 update:** Snapdragon Start silicon path makes this *more* relevant — the Snapdragon Start SoC is likely to have a comparable NPU class. Box is the reference for the wearable v2 NPU path.

## 7. (NEW v14) Arbor: Autonomous Optimization with Cumulative Learning

**Citation.** Renmin University of China + Microsoft Research, June 18 2026. VentureBeat writeup. Paper: "Arbor: Autonomous Optimization with Cumulative Learning" (search arXiv for canonical citation).

**Why read.** First public benchmark proving "cumulative learning > trial-and-error" in autonomous optimization (AO). 2.5× more verifiable performance gains than Claude Code/Codex on real engineering tasks under the same compute budget. The Arbor paper validates the SIA Meta-Agent pattern at the engineering-task level — not just the law-bench level SIA showed.

**Key quote:** "Automation can keep an AI working for a very long time — but a loop is not the same as progress." — Jiajie Jin, paper co-author.

**What to extract.**
- The cumulative-learning algorithm: how does Arbor *avoid* the "loop is not progress" trap?
- The benchmark setup: how do they measure "verifiable performance gain"?
- The compute economics: what is the right scale of compute per AO loop?

**Decision it enables.** W2.5 (Week 5-6 of W2): run Arbor on the danlab-multimodal screenshot task set. Compare Arbor vs SIA-H head-to-head. Document the win/loss.

**How to read.** Paper + VentureBeat writeup. ~2 hours. **NEW v14 operational priority.**

## 8. (NEW v14, not a paper) Qualcomm Snapdragon Start Program

**Citation.** Qualcomm, announced June 17 2026 at AWE. https://www.thelec.net/news/articleView.html?idxno=11450

**Why read.** Snapdragon Start is the program that gives indie glasses makers turnkey silicon + hybrid AI support + Inspecs eyewear channel access. **First customer: Inspecs.** Same Inspecs that just partnered with Snap for Specs. Qualcomm is consolidating the AI glasses supply chain.

**What to extract.**
- Eligibility criteria (indie makers, <$10M revenue, etc.)
- Hardware support (which SoCs)
- Software support (hybrid AI stack)
- Time-to-prototype (typical 3-6 months)
- Co-marketing with Qualcomm + Inspecs

**Decision it enables.** W19 (wearable v2 silicon): Snapdragon Start path is now the *primary* path, Redax is the *secondary* path. v13 had Redax as the only path.

**How to engage.** Read the program brief + the Inspecs case study + the Qualcomm + Applied Materials joint announcement. ~30 min. **NEW v14 operational priority — apply this week.**

## Reading order

1. **SIA** — read in full. 3 hours. Owner: every engineer. (Unchanged from v13.)
2. **OpenGlass** — read for the architecture. 2 hours. Owner: Dan2, Dan3. (Unchanged from v13.)
3. **Mnemosyne README + benchmark** — 1 hour. Owner: Dan2. (Unchanged from v13.)
4. **User-as-Code (UaC)** — read in full. 2 hours. Owner: Dan2. (Unchanged from v13.)
5. **HRM-Text** — HF model card + architecture. 1.5 hours. Owner: Dan2. (Unchanged from v13.)
6. **Arbor** — paper + VentureBeat. 2 hours. Owner: Dan2. **NEW v14 priority.**
7. **Box v3.1.0 release notes** — 30 min. Owner: Hardware. (Unchanged from v13.)
8. **Qualcomm Snapdragon Start brief + Inspecs case study** — 30 min. Owner: Somdipto + Dan1. **NEW v14 priority.**

Total: ~12 hours. Distributed over one week.

## What we are NOT reading this quarter (unchanged from v13)

- Frontier model internal technical reports.
- GRPO / PPO fine-tuning papers (read after SIA-W+H is benchmarked).
- Vector DB papers (HNSW choice is made).
- `paperswithcode` SOTA leaderboards.

## What we ADDED to the read list (v14)

- **Arbor paper (Renmin University + Microsoft Research, June 18 2026)** — operational priority. 2 hours.
- **Qualcomm Snapdragon Start program brief** — operational priority. 30 min. Apply this week.
- **OpenClaw skill malware guide (Skywork, June 2026)** — operational, not academic. 30 min. (Carry from v13.)
- **GLM-5.2 technical report** — IndexShare architecture. 1 hour. (Carry from v13.)
- **Apple 2027 product roadmap (Gurman, Bloomberg, June 18 2026)** — strategic. 15 min.
- **Anthropic-Lutnick compliance framework reporting (Politico/NYT/NYPost, June 18 2026)** — strategic + privacyd positioning. 30 min.

*End of paper list. Own your reading. 👾*