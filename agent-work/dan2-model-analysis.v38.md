# Model Selection Deep-Dive — Dan2 v38 (2026-06-22 11:30 IST)

> **Scope.** Same as v34 (LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS) plus v38 deltas: **LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M (Jun 18, Liquid AI)** for memoryd, **Nanomind cascade pattern** for perceptiond v1.5, **Kokoro-82M** as KittenTTS alt. Evidence-based, no religion.

---

## TL;DR

| Slot | Current | v38 verdict | Recommendation |
|------|---------|-------------|----------------|
| **Vision** | LFM2.5-VL-450M Q4_0 | ✅ Keep, plan Nanomind-style cascade for v1.5 | Stay the course; Nanomind reference for v1.5 cascade |
| **STT** | whisper.cpp base.en + Silero VAD | ✅ Keep, no better alternative | Stay the course |
| **TTS** | KittenTTS "medium" | ✅ Keep for v1, evaluate Kokoro-82M in v1.5 | Stay; spike Kokoro for v1.5 alt |
| **Embedding** (v38 new) | all-MiniLM-L6-v2 (384d, US-origin) | ⚠ **Swap now** | LFM2.5-Embedding-350M (1024d, Apache 2.0-eq, multilingual) |
| **Reranker** (v38 new) | None | Add in v1.5 | LFM2.5-ColBERT-350M (Liquid AI, late-interaction) |

**v38 delta vs v34:** the two new Liquid models (released Jun 18, 2 days before this run) **resolve the embedding-sovereignty open question from v34 and the PRD** (which left it open). **memoryd v1.1 should swap all-MiniLM-L6-v2 → LFM2.5-Embedding-350M in the next sprint.**

---

## 1. Vision — LFM2.5-VL-450M (re-confirmed)

Same conclusion as v34. Three v38 deltas:

### 1.1 Nanomind cascade for v1.5 (NEW)

The closest published wearable VLM benchmark is **Nanomind (arXiv:2510.05109v6)**: LLaVA-OneVision-Qwen2-0.5B + camera at **0.375W continuous, 18.8h on 2000 mAh**. The cascade pattern is:

- **Light on-device VFM** (e.g., SigLIP-400M encoder, ~50 mW) for always-on detection
- **Heavy MM-LLM** (LFM2.5-VL-450M, ~330 mW) only when triggered
- **NPU/GPU/DSP modular dispatch** via Token-Aware Buffer Manager (TABM, zero-copy)

**v38 plan for perceptiond v1.5:**
- v1 keeps LFM2.5-VL-450M Q4_0 CPU. 10s/frame. Salience-gated. Battery irrelevant (AC).
- v1.5: LFM2.5-VL-450M + Nanomind-style cascade on GAP9 or Snapdragon AR1. Target 0.4W continuous, sub-1s/frame, 18h battery.

### 1.2 Quantization frontier (LQA + SPEED-Q)

v34 mentioned SPEED-Q (2-bit InternVL-1B in <400 MB). v38 adds **LQA (arXiv:2602.07849)** — 19.9× memory reduction over gradient-based TTA on edge VLM, with selective hybrid quantization (SHQ) for VLM TTA. **Combined with SPEED-Q's staged distillation, a 4-bit or 2-bit LFM2.5-VL-450M is plausible by end of 2026** with minimal quality loss.

**v38 read:** **don't compress further right now** (Q4_0 already works). Watch LQA + SPEED-Q follow-ups. If Liquid releases a 2-bit official GGUF in Q3 2026, benchmark it.

### 1.3 Edge Reliability Gap (carry from v34)

SmolVLM2-500M has 12.5pp negation collapse vs Qwen2.5-VL-7B on COCO. Mitigation in perceptiond: **structured-output prompts** ("Is there a key in the image? Respond JSON: {present: bool, bbox: [x,y,w,h]}"), not free-form description. **This is already partially in place** in perceptiond's v1.3 prompts.

---

## 2. STT — whisper.cpp base.en (re-confirmed)

No new evidence changes v34's verdict. whisper.cpp remains the CPU-STT king. Three notes:

1. **English-only is the open question for India-first deployment.** v34 said: "Make model-swappable so v1.5 can drop in whisper-small." v38 confirms: model-swap is the right path; whisper-small at 460MB is too big for v1.5 wearable (4× base.en).
2. **Moonshine STT** (Useful Sensors, 2026, ~250MB streaming) is the v1.5 streaming alt. Track for Q3 2026 release.
3. **Parakeet TDT** (NVIDIA, ~340MB multilingual) requires NPU/GPU. Not for v1.

---

## 3. TTS — KittenTTS "medium" (re-confirmed, v1.5 path sharpened)

Same conclusion as v34: keep for v1, add `/prewarm` endpoint.

**v38 sharpening:** **Kokoro-82M (2025, ~82MB)** is the v1.5 alternative. Higher quality than KittenTTS medium, larger (~3×) but still wearable-feasible. **Spike in Month 1 to benchmark cold-path latency and voice quality on Dan Glasses target hardware.**

**Open question:** **cold-path 3.8s latency is still too long.** Pre-warm at boot via openclaw is the v34 fix. v38 adds: **run a "first words" greeting on session-start** that triggers ttsd pre-warm, so the first user query is warm.

---

## 4. Embedding — LFM2.5-Embedding-350M (NEW v38, swap now)

### 4.1 What we have

- **Model:** `sentence-transformers/all-MiniLM-L6-v2` (384d, US-origin, English-only, MIT)
- **Storage:** SQLite BLOB
- **Performance:** sub-10ms per embedding on CPU

### 4.2 What's available now (Jun 18, 2026)

**LFM2.5-Embedding-350M** released 2026-06-18 by Liquid AI.[^1] Apache 2.0-equivalent (LFM Open License v1.0).
- 350M parameters, 1024d embeddings, multilingual (100+ languages including Hindi, Tamil, Bengali)
- Native Liquid architecture (hybrid shortconv+attention)
- Designed for edge deployment
- Apache 2.0-equivalent: no export control risk, sovereign by default

**LFM2.5-ColBERT-350M** also released Jun 18.[^1] Late-interaction reranker, designed to pair with LFM2.5-Embedding-350M for high-recall retrieval.

### 4.3 v38 verdict: **swap now**

The current `all-MiniLM-L6-v2` was a defensible v1 choice but has three v38-blocking problems:
1. **US-origin** — exposed to export control risk (cf. Anthropic Fable 5 / Mythos 5 suspension, Jun 12).
2. **English-only** — fails on India-first users.
3. **384d** — under-resolution for long-horizon memory (MemCog SOTA uses 1024d-class).

**LFM2.5-Embedding-350M** solves all three. Storage cost: 4× (1024d vs 384d × 4 bytes per float = 4KB vs 1.5KB per memory). For 10k memories, that's 40MB vs 15MB. **Acceptable.**

### 4.4 Migration plan (memoryd v1.1)

1. **Week 1:** Add LFM2.5-Embedding-350M to `memoryd/models/`. Keep all-MiniLM-L6-v2 as fallback.
2. **Week 2:** Migration script — re-embed all existing memories using the new model. Add `embedding_model_version` column to `memories` table.
3. **Week 3:** Update API: `/v1/embeddings` accepts `model` parameter. Default to LFM2.5-Embedding-350M.
4. **Week 4:** Deprecate all-MiniLM-L6-v2 path. Keep on disk for rollback.

**Open:** confirm LFM2.5-Embedding-350M has a pre-built ONNX/GGUF or if we need to convert. The blog post says "available on HuggingFace" — check there.

---

## 5. Reranker — LFM2.5-ColBERT-350M (NEW v38, v1.5 add)

Late-interaction reranker. Use case: high-recall retrieval on memoryd v2 v2.0 (Dec 2026 target).

**v38 plan:**
- v1.1: keep flat-cosine retrieval on LFM2.5-Embedding-350M.
- v1.5: add LFM2.5-ColBERT-350M as opt-in reranker for `query` API when `top_k > 10`.
- v2.0: default to two-stage retrieval (recall@100 with embedding, rerank@10 with ColBERT).

**Memory budget:** 350M × 2 bytes (Q4) ≈ 700MB. Tight on aarch64 4GB. **Only load on demand.**

---

## 6. Reasoning backbone — HRM-Text 1B vs LFM2.5-1.2B-Thinking (v38 unresolved)

The workspace AGENTS.md says **HRM-Text 1B** for reasoning. The PRD says **LFM2.5-1.2B-Thinking**. This is **v37's open question #8 and v34's open question #2**, still unresolved.

**v38 read:** **dglabs-eval v1 reasoning subset (5 tasks) settles this empirically.** Until then, no model lock-in for the reasoning backbone. Both are 1B-class, both Apache 2.0-eq, both edge-feasible. **dglabs-eval v1 measures both and we ship whichever wins on a 5-task reasoning subset.**

**HRM-Text 1B** advantage: faster (per Hierarchical Reasoning Model paper). LFM2.5-1.2B-Thinking advantage: better at chain-of-thought, larger training set.

---

## 7. What I'd watch in the next 30 days

1. **LFM2.5-Embedding-350M + ColBERT-350M GGUF conversion** — confirm available on HuggingFace.
2. **BitNet-VLM** — first 1-bit VLM. If it ships, it's the wearable v2 path. Track arXiv.
3. **OpenGlass GAP9 dev kit** — order one for $300. Validate the Nanomind cascade on real silicon.
4. **Brilliant Labs Halo** — order at $349. Get the LFM2-VL-450M production integration reference.
5. **Kokoro-82M on TTS eval** — benchmark cold-path latency, voice quality vs KittenTTS.

---

[^1]: https://www.liquid.ai/blog/lfm2-5-retrievers

*Dan2 model analysis, 2026-06-22 v38. Companion to dan2-research-report.v38.md and dan2-architecture-review.v38.md.*
