# Model Selection Deep-Dive — Danlab v99
**Author:** Dan2 👾
**Run:** 2026-06-27 10:30 IST (05:00 UTC)
**Version:** v99 — Gemma 4 12B unified architecture as v3 long-term convergence, Gemma 4 12B tradeoffs vs Gemma 4 E2B QAT-mobile, Mythos-partial-unblock changes GLM 5.2 positioning
**Inputs:** LFM2.5-VL-450M SPEC, perceptiond SPEC, audiod SPEC, ttsd SPEC, memoryd SPEC, v99 research report, all 18 web searches + 3 deep research calls

---

## TL;DR (v99 verdict)

**For Dan Glasses v1: keep all current picks.** LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS medium, all-MiniLM-L6-v2 are correct for the wearable form factor today. **Do not switch for hype.**

**For v1.5: swap the thermal fallback from LFM2.5-230M to Gemma 4 E2B QAT-mobile.** v98 verdict stands.

**For Q3 2026 (Show HN Aug 25):** add HRM-Text-1B as the on-device reasoner + GLM 5.2 as the cloud-fallback reasoner + LFM2.5-Embedding-350M swap in memoryd v2 + agent-memory partition for BAO bandit posterior.

**For Q4 2026 (memoryd v3 R&D):** explore SemanticXR object-level memory schema + Perplexity Brain-pattern agent-self-improvement loop. Cite both papers in the arXiv submission Aug 15.

**For H2 2027 (memoryd v3 ship):** evaluate **Gemma 4 12B unified architecture** as v3 single-model convergence thesis. If Snapdragon Reality Elite can fit 12B at 16GB, our 4-model pipeline collapses to 1.

**Mythos partial unblock (v99 NEW):** the arXiv framing shifts from "closed-weight frontier is gone" to "closed-weight frontier is geopolitically conditioned." GLM 5.2 remains the right cloud fallback (MIT, sovereign, no geopolitical gating).

---

## 1. Vision model: LFM2.5-VL-450M (verified, keep)

**Status (v99):** confirmed shipped, working in perceptiond at port 8092.

| Property | Value | Source |
|---|---|---|
| Architecture | LFM2.5-base + 400M SigLIP2 NaFlex + projector | Liquid AI Apr 8, 2026 |
| Parameters | 450M total | Liquid AI |
| Quant | Q4_0 (389MB) | Liquid4All cookbook |
| Context | 32,768 tokens | Liquid AI |
| Inference (CPU x86_64) | ~10–15s/frame watchful mode | perceptiond SPEC |
| Inference (target Redax aarch64) | unmeasured | critical gap |
| License | LFM Open License v1.0 (commercial-friendly) | Liquid AI |

**Benchmarks vs SmolVLM2-500M:** MMStar 43.0 vs 38.2 (+12%), RealWorldQA 58.4 vs 49.9 (+17%), MM-IFEval 45.0 vs 11.3 (+298%). [^v98]

**Verdict: keep.** Don't switch.

---

## 2. Thermal fallback: Gemma 4 E2B QAT-mobile (v98 NEW — keep)

**v97 verdict:** LFM2.5-230M. **v98 verdict: Gemma 4 E2B QAT-mobile.** **v99 verdict: keep Gemma 4 E2B.**

| Property | Gemma 4 E2B QAT-mobile |
|---|---|
| Footprint | 1GB on device |
| Mobile NPU support | Native (LiteRT-LM) |
| Compression ratio | 7× from full precision |
| Speed (mobile NPU) | 2× faster than unquantized |
| Multilingual | 140+ languages |

**v99 NEW consideration:** **Gemma 4 12B unified architecture** (Jun 3, 2026) is now the alternative. See §7 below.

---

## 3. STT: whisper.cpp base.en (verified, keep; A/B Moonshine Q4)

**Status:** unchanged from v98. 121/130 tests + 9 WS proxy tests.

**Alternatives considered:** Moonshine v2 (May 2026), Qwen3-ASR-0.6B, Parakeet TDT 0.6B, Cheetah.

**v99 verdict:** keep. A/B Moonshine v2 in Q3 2026.

---

## 4. TTS: KittenTTS medium (verified, keep; A/B Kokoro for Indic)

**Status:** unchanged from v98. 6/6 tests.

**v99 verdict:** keep. Add Kokoro-82M for v1.5 Indic.

---

## 5. Reasoning: HRM-Text-1B on-device + GLM 5.2 cloud fallback (v98/v99 unchanged)

**v99 verification:** **Sapient HRM-Text-1B confirmed in our analysis.** $1,500 training cost, GSM8K 84.5%, MATH 56.2%, 1.15B params, mlx-vlm merged May 29.

**Critical mechanistic analysis (v99 NEW):** The "Are Your Reasoning Models Reasoning or Guessing?" paper (arXiv:2601.10679) shows that **HRM performance on extremely difficult tasks is driven by guessing (multiple attempts) rather than true hierarchical reasoning**. Augmented HRM boosts Sudoku-Extreme from 55.0% to 96.9% via bootstrap + relabel + data mixing.

**v99 implication:** HRM-Text-1B on wearable is fine for "should I interrupt?" because the decision is not a hard reasoning task — it's a cost-benefit calibration. But for high-stakes reasoning (e.g., "is this conversation medically relevant?"), we should not over-rely on HRM-Text-1B alone. **GLM 5.2 cloud fallback is the right answer for high-stakes reasoning.** v99 reinforces v98's opt-in default.

### 5.1 CosmicFish-HRM caveat (v99 NEW)

The CosmicFish-HRM paper (arXiv:2605.28919) shows that **HRM at small scale (82.77M params) does NOT outperform comparable-size standard transformers** on standard benchmarks (HellaSwag, PIQA, WinoGrande, TriviaQA, ARC-Easy, Natural Questions). The HRM overhead dominates at small scale.

**v99 implication:** HRM-Text-1B is the right *minimum* size. Going smaller is counterproductive. **Do not try to scale HRM-Text below 1B for wearable inference.**

### 5.2 Tiny Recursive Model (TRM) alternative (v99 NEW)

The TRM paper (arXiv:2510.04871) shows a 7M-parameter recursive model **outperforms HRM** on Sudoku-Extreme (87.4% vs 55%) and Maze-Hard (85.3% vs 74.5%). Single tiny network, two nested loops, two latent states.

**v99 implication:** **TRM is the research direction for our v3 (H2 2027) on-device reasoner.** If we can compress HRM-Text-1B to a TRM-style 50-200M model without quality loss, we free up wearable memory budget for other models. **R&D item for H1 2027.**

---

## 6. Embedding model: LFM2.5-Embedding-350M (v98 verdict, keep)

**Status:** planned for Q3 2026 swap.

| Property | MiniLM-L6-v2 | LFM2.5-Embedding-350M |
|---|---|---|
| Dimensions | 384 | 1024 |
| Languages | English-only | 100+ languages, 22 Indic |
| Size | 80MB | ~350MB |

**v99 verdict:** swap in Q3 2026 week 1.

---

## 7. NEW v99: Gemma 4 12B unified architecture (v3 long-term convergence)

**Status:** research candidate, not implementation.

| Property | Value |
|---|---|
| Parameters | 11.95B |
| Architecture | Encoder-free unified (audio + vision + text) |
| License | Apache 2.0 |
| Footprint | 16GB VRAM / unified memory |
| Context | 256K tokens |
| Native capabilities | Tool-use, reasoning mode |

**Why this is the v3 convergence candidate:**

Our current pipeline (LFM2.5-VL-450M + whisper.cpp + KittenTTS + HRM-Text-1B) is **4 separate models with 4 separate memory budgets**. Gemma 4 12B unified could collapse this to **1 model with 1 memory budget**:

| Component | v1 (current) | v3 (H2 2027 candidate) |
|---|---|---|
| Vision | LFM2.5-VL-450M (209MB) | Gemma 4 12B (6GB at Q4_0) |
| STT | whisper.cpp base.en (74MB) | (unified) |
| TTS | KittenTTS medium (25MB) | (unified) |
| Reasoning | HRM-Text-1B (1.2GB at Q4_0) | (unified reasoning mode) |
| **Total memory** | **~1.5GB** | **~6GB** |

**Tradeoff:** 4× memory for 1 model that handles all modalities. **Hardware constraint:** 6GB at Q4_0 + KV-cache requires Snapdragon Reality Elite (48 TOPS) or equivalent. Timeline: H2 2027.

**v99 decision: YES, R&D-only for H2 2027.** No Q3 commitment.

### 7.1 What we lose with the unified model

- **Modular reasoning swaps.** Today we can swap HRM-Text-1B → GLM 5.2 for cloud fallback. With Gemma 4 unified, the reasoner is baked in.
- **Per-modality optimization.** whisper.cpp's STT is highly optimized for ASR; Gemma 4 unified audio is not (yet).
- **Memory budget flexibility.** Today we can load only the VLM when STT is not needed. With unified, the whole 6GB is always loaded.

### 7.2 What we gain

- **Encoder-free design eliminates ~150–300ms fusion latency.** This is the single biggest performance win.
- **Cross-modal attention emerges from training.** The model "sees" audio and vision simultaneously, which is qualitatively different from a pipeline.
- **Single quantization, single memory budget.** Simpler infra.

**v99 verdict: explore as v3 R&D. Don't commit until Snapdragon Reality Elite benchmarks land.**

---

## 8. Object-level memory: SemanticXR (v98 verdict, keep)

**Status:** research candidate.

**v99 verdict:** unchanged. Q3 2026 read, Q4 2026 prototype, H1 2027 ship as memoryd v3 if prototype succeeds.

---

## 9. NEW v99: Agent-self-memory architecture (Perplexity Brain + Engram pattern)

**Status:** design needed.

**v99 verdict:** add `agent_memories` table to memoryd v2 with schema `{interrupt_id, harness_variant, salience_score, cost_estimate, benefit_estimate, decision, reasoning_trace, user_response_label, bandit_posterior, timestamp}`. BAO bandit posterior updated async overnight.

**Open question for somdipto:** do we want **on-device-only** (privacy-first) or **opt-in cloud sync** (so the bandit can train on aggregate population data without exposing individual memories)? v99 recommends on-device-only by default, opt-in for the population training. This is the strongest privacy wedge we have.

---

## 10. Consolidated model matrix (v99)

| Component | v1 (current) | v1.5 (Q4 2026) | v2 (H1 2027) | v3 (H2 2027) | Research |
|---|---|---|---|---|---|
| Vision | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-1.6B | **Gemma 4 12B unified** | LFM2.5-VL-2B+ |
| Thermal fallback | LFM2.5-230M | **Gemma 4 E2B QAT-mobile** | Gemma 4 E4B QAT | (single-model) | Gemma 5 edge |
| STT | whisper.cpp base.en | Moonshine v2 / Qwen3-ASR | Qwen3-ASR | (Gemma 4 unified) | Indic-STT |
| TTS | KittenTTS medium | KittenTTS + Kokoro-82M Indic | Kokoro multilingual | (Gemma 4 unified) | MOSS-TTS-Drive |
| Reasoning (on-device) | (none) | HRM-Text-1B | **HRM-Text-1B + TRM-50M** (R&D) | (Gemma 4 unified) | TRM scaling |
| Reasoning (cloud fallback) | (none) | GLM 5.2 | GLM 5.x / LFM2.5-1.2B-Thinking | (cloud agent) | — |
| Embedding | MiniLM-L6-v2 | LFM2.5-Embedding-350M | LFM2.5-Embedding-1B | Gemma 4 native | — |
| Object memory | (none) | (none) | **SemanticXR object schema** | SemanticXR + agent memory | — |
| **Agent memory** | (none) | (none) | **memoryd v2 partition (v99 NEW)** | **memoryd v3 + Perplexity-Brain-pattern** | — |
| Reranker | (none) | LFM2.5-ColBERT-350M | LFM2.5-ColBERT-1B | — | — |

---

## 11. What we are NOT doing (v99 update)

- **Not switching from LFM2.5-VL-450M for hype.** It works.
- **Not switching from whisper.cpp.** Moonshine A/B is the only candidate worth exploring.
- **Not switching from KittenTTS for English.** It's good enough for v1.
- **Not adopting closed-weight reasoning models.** GLM 5.2 is the only cloud option (MIT, sovereign).
- **Not switching to LFM2.5-VL-1.6B pre-release.** Wait for stable.
- **Not skipping Gemma 4 E2B thermal fallback benchmark.**
- **NOT committing to Gemma 4 12B unified for v3.** R&D only, pending Snapdragon Reality Elite benchmark.
- **NOT assuming HRM-Text-1B scales below 1B.** CosmicFish-HRM caveat. Use TRM instead if going smaller.
- **NOT over-relying on HRM-Text-1B for high-stakes reasoning.** "Reasoning or Guessing?" paper shows HRM is partly guessing. Cloud fallback for high-stakes.

---

## 12. Risk register (v99 update)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Gemma 4 E2B license restricts commercial use | Medium | High | Verify Q3 week 1. Fallback: LFM2.5-230M. |
| HRM-Text-1B doesn't fit in 4GB with awarenessd loaded | Medium | High | Quantize Q4_0 + OSCAR-style KV-cache INT4. Fallback: skip on-device reasoning. |
| **HRM-Text-1B "guessing" failure mode for high-stakes decisions (v99 NEW)** | Medium | High | Always offer GLM 5.2 cloud fallback for high-stakes. UI prompts user to confirm. |
| GLM 5.2 cost increases after DeepSeek-moment hype | Low | Medium | On-device HRM-Text-1B default; GLM 5.2 opt-in. |
| SemanticXR prototype doesn't fit memoryd v2 | Medium | Medium | Keep as R&D only. |
| whisper.cpp base.en too slow on aarch64 | Medium | Medium | Moonshine v2 in Q3 A/B. |
| KittenTTS license blocks .deb | Medium | High | Verify Q3 week 2. Fallback: Kokoro-82M only. |
| **Gemma 4 12B unified does NOT fit on Snapdragon Reality Elite (v99 NEW)** | Medium | Medium | R&D evaluation in Q1 2027 before committing v3 architecture. |
| **Mythos fully unblocks and our geopolitical framing weakens (v99 NEW)** | Medium | Low | Our wedge is on-device + auditable + Indic + agent-memory. Stays valid regardless. |
| **Engram/Perplexity Brain captures cloud agent-memory before Show HN (v99 NEW)** | Medium | High | On-device + privacy + auditable differentiation. Make it visible at Show HN. |
| **OpenAI IPO delay signals broader AI capex slowdown (v99 NEW)** | Medium | Medium | Our path is bootstrappable to revenue, not venture-scale. |

---

*Dan2 👾 — 2026-06-27 10:30 IST — committed to building the future with my partner*
