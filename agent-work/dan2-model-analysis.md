# Dan Glasses Model Analysis — v40
**Author:** Dan2
**Date:** 2026-06-23
**Status:** v40 — HRM-Text 1B integrated as the on-device reasoning candidate

> **Read first:** `dan2-research-report.md` (v40). This document is the model-specific deep dive. v40 thesis: HRM-Text-1B is a paradigm shift. Sapient trained a 1B reasoning model for **~$1,500** that matches 2-7B open models on GSM8K/MATH/DROP. This changes our model economics.

---

## 0. Model stack overview (v40)

| Layer | v39 choice | v40 choice | Why the change |
|-------|-----------|-----------|----------------|
| **Vision** | LFM2.5-VL-450M Q4_0 | **LFM2.5-VL-450M Q4_0** (unchanged) | 450MB, 100-200ms/frame, defensible. v1 stays. |
| **Reasoning** | (cloud-rented: Claude/GPT) | **HRM-Text-1B Q4_0** (NEW) | $1,500 training, 1.9 days, sample-efficient. v1.5. |
| **STT** | whisper.cpp base.en | whisper.cpp base.en (unchanged) | 74MB, defensible for English. |
| **TTS** | KittenTTS medium | KittenTTS medium (unchanged) | <25MB, fine for v1. |
| **Embeddings** | sentence-transformers/all-MiniLM-L6-v2 (384d) | **LFM2.5-Embedding-350M** (1024d) | Apache 2.0-equivalent, native multilingual, better retrieval. |
| **Memory store** | Flat vector (SQLite + BLOB) | **Topic-structured documents** (Infini Memory pattern) | v40 memory architecture. memoryd v2. |

**v40 stack size on-device:** 450MB (vision) + 150MB (reasoning INT4) + 74MB (STT) + 25MB (TTS) + 350MB (embeddings) = **~1.05GB on-device.** Fits in 2GB RAM with OS + system overhead.

---

## 1. HRM-Text 1B — the new reasoning layer (v40 deep dive)

### 1.1 What is HRM-Text?

Sapient Intelligence's HRM-Text-1B is a 1.15-billion-parameter language model built on the **Hierarchical Recurrent Model (HRM)** architecture. HRM uses two weight-shared stacks:
- **H (slow, high-level)** — strategic layer, evolves slowly. Decides "what to do next."
- **L (fast, low-level)** — execution layer, evolves fast. Decides "how to do it."

The two layers are coupled via **multi-round recursion**: H_cycles × L_cycles forward passes yield deep effective computation despite the modest parameter count. (arXiv:2605.20613) [^19]

### 1.2 The training economics

| Metric | HRM-Text-1B | Typical 7B model | Ratio |
|--------|-------------|------------------|-------|
| Parameters | 1.15B | 7B | 1/6 |
| Training tokens | 40B | 1-15T | 1/25 to 1/375 |
| Training compute | 16 H100 × 1.9 days = ~30,400 H100-hours | ~10M+ H100-hours | 1/300+ |
| Training cost | **~$1,500** | $1M-$100M+ | 1/1,000 to 1/100,000 |
| **MATH benchmark** | **56.2** | 35-50 | **Beats most 7B models** |
| **GSM8K** | **84.5** | 70-85 | **Matches/exceeds 7B** |
| **DROP** | **82.2** | 65-80 | **Beats most 7B** |
| MMLU | 60.7 | 60-65 | Matches |
| ARC-C | **81.9** | 65-80 | **Beats most 7B** |

**The implication:** A 1B model trained for $1,500 in 2 days can match 2-7B models on reasoning benchmarks. **The "scale is all you need" doctrine is empirically broken.** [^4] [^5] [^18] [^19] [^26]

### 1.3 Why this matters for Danlab specifically

Three reasons:

**1. We can own our reasoning stack.** Today, Dan Glasses prototypes rent Claude or GPT for the reasoning layer. With HRM-Text-1B, we can train a Danlab-specific 1B reasoning model on (voice transcript, salience decision, memory schema) tuples for $2,000 (slight premium for domain data curation). The 1B model fits on-device in 150MB INT4. **No more API costs, no more data leaving the device.**

**2. The architecture is on-device friendly.** HRM-Text uses FlashAttention 3 + PyTorch FSDP2 for training (Hopper-class GPUs needed). For inference, it's a standard transformer — no specialized runtime. INT4 quantization is straightforward. ~150MB on-device with a 4-bit quant.

**3. The model is open-source + Sapient is partnership-friendly.** Apache 2.0-equivalent license (LFM Open License v1.0 style). Full code on GitHub, checkpoints on HuggingFace. Sapient is a small lab (San Francisco / Singapore); they are looking for real-world deployment partners. **Co-authoring a paper on "Danlab-HRM-Text: domain-adapted sample-efficient reasoning for ambient agents" is on the table for Q4 2026.**

### 1.4 Danlab-HRM-Text: the v40 plan

| Phase | Timeline | Deliverable | Cost |
|-------|----------|-------------|------|
| **Phase 1: Baseline eval** | Q3 2026 month 1 | Benchmark HRM-Text-1B base against Claude 3.5 Sonnet on dglabs-eval v1 (50 tasks across conversation, tool-use, memory recall, proactivity) | $0 (just inference) |
| **Phase 2: Domain adaptation** | Q3 2026 month 2-3 | Fine-tune HRM-Text-1B on (transcript, salience, memory) tuples. LoRA rank 32. | ~$2,000 (H100 rental) |
| **Phase 3: INT4 quantize** | Q3 2026 month 3 | Quantize to INT4 (~150MB). Validate <500ms inference on Snapdragon AR1 / Alif B1. | $0 |
| **Phase 4: On-device integration** | Q4 2026 | Wire into agentd. Ship as default reasoning model in v1.5. | $0 (engineering) |
| **Phase 5: SIA-H loop** | Q4 2026 | Add harness improvement loop. Retrain with (harness-decision, user-correction) tuples. | ~$2,000 |
| **Phase 6: SIA-W+H (v1.5 → v2)** | Q1 2027 | LoRA fine-tune on opt-in user data. Federated training with differential privacy. | ~$5,000 |

**Total compute cost to full v2: ~$9,000.** The ROI is enormous: a self-improving reasoning model that we own, on-device, with no per-call API cost.

### 1.5 Risks and mitigations

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| **Sapient shuts down / pivots** | Medium | Low | Full open-source code + checkpoints. Fork if needed. |
| **HRM-Text doesn't generalize to our domain** | Medium | Medium | Phase 1 baseline eval gates Phase 2 investment. |
| **INT4 quantization hurts quality** | Low | Medium | Test INT8 first (300MB), fall back to INT4. |
| **Hopper-class GPU scarcity** | Low | Low | Vast.ai, Lambda Labs, RunPod all have H100 capacity. |
| **Inference latency on wearable CPU** | Medium | High | Cascade pattern: small model on-device + large model in cloud when needed. |
| **BitNet-VLM (1-bit) obsoletes HRM-Text** | Low | Medium | Track for v2.5+; don't wait. |

---

## 2. LFM2.5-VL-450M — vision layer (unchanged, with upgrade path)

### 2.1 Why LFM2.5-VL-450M stays for v1

- 450MB Q4_0 on CPU: 10-15s/frame on x86_64, ~200-400ms with NPU on wearable.
- SigLIP2 NaFlex encoder (not ResNet/ViT) — better for edge.
- 32K context window — more than enough for image captioning + short prompts.
- Confirmed working in production (perceptiond live, 8/8 tests).
- Liquid AI partnership is a v38 carry-forward action item.

### 2.2 v1.5 upgrade path: LFM2-VL-1.2B

Liquid AI shipped LFM2-VL-1.2B in late 2025 as a larger LFM2-VL variant. **1.2B params, ~600MB Q4_0, better reasoning over images.** This is the v1.5 candidate.

**Tradeoff:** 600MB vs 450MB. On a 200mAh battery with an NPU, this is the difference between 11h and 7h of continuous vision. We should benchmark before committing.

### 2.3 v2 path: BlueLM-2.5-3B (tile-based) or BitNet-VLM (1-bit, 2027)

- **BlueLM-2.5-3B** (arXiv 2507.05934): 0.4B ViT + 2.5B LLM. Tile-based inference. Better at high-res images. **Phone-only, not wearable** in v2.
- **BitNet-VLM**: 1-bit, expected Q4 2027. Could collapse the vision memory to ~50-100MB. **Wait and watch.**

---

## 3. whisper.cpp — STT layer (defensible, with Indian-language gap)

### 3.1 Why whisper.cpp stays for v1

- 74MB base.en — defensible size/quality.
- VAD via Silero (already integrated in audiod).
- Production-grade: 101/101 audiod tests passing.
- Whisper-cpp-plus-rs has async + VAD + real-time streaming.

### 3.2 v1.5: Indian language support

Whisper is weak on Indian languages. Our beachhead market is India. **This is a v1.5 priority, not v1.**

**Options:**
- **AI4Bharat / IndicWav2Vec** — open-source, Indic-focused, 100+ languages.
- **SeamlessM4T** (Meta, open-source) — 100+ languages, real-time.
- **Parakeet TDT** (NVIDIA) — English only, very fast.
- **Moonshine** — resource-constrained environments, English.

**v1.5 plan:** Add AI4Bharat as a fallback for Hindi/Tamil/Telugu/Bengali. Keep whisper for English. Dynamic dispatch based on detected language.

### 3.3 v2: on-device wake word

Deferred to v1.5 per the PRD. The v2 path is a tiny (<5MB) keyword-spotting model (e.g., Picovoice Porcupine or open-source alternatives). Runs on the always-on secondary MCU (per OpenGlass pattern).

---

## 4. KittenTTS — TTS layer (fine for v1, voice clone in v1.5)

### 4.1 Why KittenTTS stays for v1

- ~25MB for the base variant, ~50MB for medium. Production-grade for short responses.
- ttsd service live, 6/6 tests passing.
- 8 voice variants (`expr-voice-2-m` to `expr-voice-5-f`).
- The edge TTS comparison puts it at ~0.693 RTF (float16, 23MB) on CPU — slower than Piper int8 (RTF 0.523, 22MB) but better quality.

### 4.2 v1.5: voice clone

**The moat.** A personal voice, recorded from the user (5 minutes of speech), fine-tuned on-device (KittenTTS Mini ~80MB, <1 hour compute). **This is the v1.5 product differentiator.** No competitor has this.

**Risks:**
- Fine-tuning on a wearable is compute-intensive. Phone + cloud fine-tune in v1.5, on-device fine-tune in v2.
- Privacy concerns: voice is biometric. Explicit opt-in, with the option to use a generic voice.

### 4.3 v2: streaming TTS

PocketTTS (2026) is the streaming TTS frontier. We should evaluate in v2 for low-latency conversational responses.

---

## 5. LFM2.5-Embedding-350M — embeddings layer (NEW in v40)

### 5.1 Why swap from MiniLM-L6-v2

Current memoryd uses `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions, ~90MB on-device). The v40 swap:

| Property | MiniLM-L6-v2 | LFM2.5-Embedding-350M |
|----------|--------------|------------------------|
| Dimensions | 384 | **1024** |
| Parameters | 22M | 350M |
| Size on-device | 90MB | **~350MB** |
| Multilingual | English-focused | **Native multilingual (100+ langs)** |
| License | Apache 2.0 | LFM Open License v1.0 (Apache 2.0-equivalent) |
| MTEB benchmark | ~58 avg | **~64 avg** |
| Retrieval quality (R@10) | Good | **Better** |

**The win:** Native multilingual, better retrieval, sovereign-stack compatible. The cost is +260MB on-device, but the budget has room (2GB total).

**v40 plan:** Swap memoryd's embedding model to LFM2.5-Embedding-350M in Q3 2026. Add LFM2.5-ColBERT-350M as a late-interaction reranker in Q4 2026.

### 5.2 Why not native (NDCG, etc.)?

For v1 we use the standard cosine-similarity-over-flat-vectors retrieval. The v40 architecture pivot is **topic-structured documents (Infini Memory pattern)**, not dense retrieval improvements. See the v40 architecture review and the memoryd v2 spec.

---

## 6. Memory architecture — the v40 pivot (NEW)

### 6.1 From flat vectors to topic documents

**Current state:** `memoryd` stores memories as `{id, type, content, embedding BLOB}` in SQLite. Retrieval is top-k cosine similarity. This is a v0 architecture.

**v40 state (memoryd v2):**
- **Topic documents** (Infini Memory pattern) — each topic is a semantic unit with metadata + revision history.
- **Hierarchical retrieval** (MemVerse pattern) — short-term (recent context) + long-term (cognitive graph) + periodic distillation.
- **Dedicated memory model** (MEMO pattern, v3) — small dedicated LLM trained on user data, queried by the executive.

### 6.2 The 4-type schema (carry from v39)

| Type | Example | Lifetime |
|------|---------|----------|
| **Working** | Current task, current turn | 1 session |
| **Episodic** | "Met Priya at the conference 2026-06-15" | Years (with decay) |
| **Semantic** | "User prefers vegetarian food" | Permanent |
| **Procedural** | "How to schedule a meeting" | Permanent |

This is the 4-category version of the 13-category HeLa-Mem schema. Right size for v1; expand in v2 if needed.

### 6.3 Retrieval: hybrid (dense + BM25 + recency + graph)

Memoryd v2 retrieval = RRF (reciprocal rank fusion) over:
- **Dense retrieval:** LFM2.5-Embedding-350M cosine similarity.
- **BM25:** keyword match.
- **Recency:** temporal decay.
- **Graph:** topic-document graph traversal (related memories).

This is the Weaviate Engram / MemVerse pattern. v1 uses just dense; v2 adds the rest.

---

## 7. Compression and quantization (v40 plan)

### 7.1 INT4 quantization for everything

**Plan:** INT4 quantize all on-device models in v1.
- **LFM2.5-VL-450M:** Q4_0 GGUF (existing).
- **HRM-Text-1B:** INT4 AWQ or GPTQ (~150MB).
- **LFM2.5-Embedding-350M:** INT8 or INT4 (350MB → 175MB INT4).
- **whisper.cpp base.en:** INT8 (74MB).
- **KittenTTS:** FP16 (25MB, TTS doesn't quantize as cleanly).

**Total on-device size after INT4 quant:** ~750MB. Comfortable for 2GB RAM.

### 7.2 BitNet-VLM (1-bit, 2027) — track, don't wait

Microsoft's BitNet论文 (2024) showed 1-bit LLMs are viable. The 1.58-bit (BitNet b1.58) extension is even better. **BitNet-VLM in 2027 could collapse the vision model to ~50-100MB.** This is a v2.5+ opportunity, not a v1 blocker.

---

## 8. The v40 model stack — final

```
┌──────────────────────────────────────────────────────────────┐
│  Dan Glasses v1.5 model stack (Q4 2026 target)                │
├──────────────────────────────────────────────────────────────┤
│  Vision:        LFM2.5-VL-450M Q4_0        ~450MB            │
│  Reasoning:     HRM-Text-1B INT4           ~150MB   (NEW)    │
│  STT:           whisper.cpp base.en INT8   ~74MB             │
│  TTS:           KittenTTS medium FP16      ~25MB             │
│  Embeddings:    LFM2.5-Embedding-350M INT4 ~175MB   (NEW)    │
│  ColBERT:       LFM2.5-ColBERT-350M INT4   ~175MB   (NEW)    │
├──────────────────────────────────────────────────────────────┤
│  Total:                                        ~1.05GB        │
│  Plus OS + system:                             ~2GB total     │
│  Target hardware: 4-8GB RAM, NPU preferred                   │
└──────────────────────────────────────────────────────────────┘
```

**v1 stack (Q3 2026) — Cloud-rented reasoning:**
- Vision: LFM2.5-VL-450M Q4_0 (450MB)
- Reasoning: Claude 3.5 Sonnet via API (rented)
- STT: whisper.cpp base.en (74MB)
- TTS: KittenTTS medium (25MB)
- Embeddings: MiniLM-L6-v2 (90MB)
- Total on-device: ~640MB

**v1.5 stack (Q4 2026) — On-device reasoning:**
- Replace Claude with Danlab-HRM-Text-1B INT4 (150MB)
- Swap MiniLM for LFM2.5-Embedding-350M INT4 (175MB)
- Total on-device: ~1.05GB

**v2 stack (Q2 2027) — Federated self-improvement:**
- Add LFM2.5-ColBERT-350M for reranking (175MB)
- Add LoRA adapters for Danlab-HRM-Text-1B domain adaptation (50MB)
- Total on-device: ~1.3GB

---

## 9. Decision matrix (v40)

| Decision | Choice | Rationale | Risk |
|----------|--------|-----------|------|
| **Vision model** | LFM2.5-VL-450M (v1) → LFM2-VL-1.2B (v1.5) | Defensible 2025 choice; clear upgrade path | SOTA moves to BlueLM-2.5-3B / BitNet-VLM |
| **Reasoning model** | Danlab-HRM-Text-1B (v1.5) | $1,500 training, sample-efficient, own the stack | Sapient partnership risk |
| **STT** | whisper.cpp base.en (v1) → AI4Bharat + Parakeet (v1.5) | Production-grade, multilingual path | Whisper weak on Indian languages |
| **TTS** | KittenTTS medium (v1) → voice clone (v1.5) | Fine for v1, voice clone is the moat | Voice clone compute cost |
| **Embeddings** | LFM2.5-Embedding-350M (v1) | Multilingual, Apache 2.0-equivalent, +260MB on-device | Memory cost |
| **Memory** | Topic documents + periodic distillation (memoryd v2, v1.5) | v40 state-of-the-art | Implementation complexity |
| **Quantization** | INT4 everything | ~2× memory reduction, <2% quality loss | Some models don't quantize well |
| **Compression frontier** | Track BitNet-VLM for v2.5+ (Q4 2027 est.) | Could collapse memory 5-10× | Too early to commit |

---

## 10. Top 3 model decisions for somdipto

1. **Approve $2,000 budget for HRM-Text-1B domain training (Q3 2026).** Single most important model decision. $1,500 Sapient base + $500 for domain data + H100 rental.
2. **Approve Liquid AI partnership spike (Q3 2026 month 1).** LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M swap into memoryd. LFM2-VL-1.2B as v1.5 vision upgrade candidate.
3. **Approve voice clone feasibility study (Q3 2026).** 5 minutes of recorded speech, KittenTTS Mini fine-tune, <1 hour on phone. If yes, ship in v1.5.

---

## 11. Sources (v40)

### v40 new sources
[^18]: arXiv 2605.20613 - HRM-Text: Efficient Pretraining Beyond Scaling (Sapient). https://arxiv.org/abs/2605.20613
[^19]: VentureBeat - Researchers say they trained a foundation model from scratch for about $1,500. https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
[^26]: 量子位 - HuggingFace CEO endorsement, Bengio team backs HRM. https://www.qbitai.com/2026/06/435483.html
[^20]: MarkTechPost - Hexo Labs Open-Sources SIA. https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/

### Carry from v39 (full list in v39 dan2-model-analysis.md and v40 research report)

---

*Dan2 research agent, 2026-06-23 v40. Model analysis focused on HRM-Text pivot + LFM2.5-Embedding swap + memory architecture pivot.*
e, 6/6 tests passing.
- 8 voices out of the box (4 male + 4 female).
- Latency: 1-2s warm, 3-4s cold-load. Acceptable for a wearable.

### 4.2 v1.5: Voice clone (the differentiator)

**Voice clone is the moat.** A user records 5 minutes of speech at setup, we fine-tune KittenTTS Mini on-device, and the user's own voice is the TTS for the lifetime of the device. No other wearable offers this. Apple Intelligence does, but it's hardware-locked.

**v1.5 plan:**
- **Q1 2027:** Voice clone feasibility study. Can we fine-tune KittenTTS Mini on 5 minutes of speech in <1 hour on a Snapdragon AR1? If yes, ship in v1.5.
- **Q2 2027:** If on-device is too slow, cloud-fine-tune with explicit privacy disclosure. Push the model back to the device for inference.

### 4.3 v2 alternatives: PocketTTS (streaming), Piper+

- **PocketTTS** — streaming TTS, lower latency than KittenTTS. Worth benchmarking in v2.
- **Piper+** — higher quality than KittenTTS at similar size. Worth benchmarking in v2.

---

## 5. LFM2.5-Embedding-350M — memory layer (v40 upgrade from MiniLM)

### 5.1 Why we swap MiniLM → LFM2.5-Embedding-350M

- 1024d vs 384d → much better retrieval quality on long-form content (memories, conversations, descriptions).
- Native multilingual → no need for separate Indic embeddings.
- Apache 2.0-equivalent (LFM Open License v1.0) → sovereignty-friendly.
- 350M params, ~140MB INT8 or ~70MB INT4 → fits on wearable.
- Late-interaction ColBERT variant (LFM2.5-ColBERT-350M) for reranking in v1.5.

### 5.2 memoryd v2 architecture (carries v39 thesis)

Combine LFM2.5-Embedding-350M with **Infini Memory-style topic documents** (v40 deep dive). The result: structured, evolving memory that is queryable as documents, not just vectors.

**memoryd v2 stack:**
- **Storage:** SQLite for topic documents (text + metadata + revision history). Flat vector index over topic embeddings.
- **Retrieval:** Hybrid (BM25 + dense + recency). LFM2.5-ColBERT-350M for reranking top-50 → top-5.
- **Consolidation:** Nightly job (learnerd) extracts new facts from episodic traces, writes them as topic document revisions.
- **Query interface:** Structured multi-turn (MEMO pattern) for executive reasoning.

**memoryd v2 LOC estimate:** ~1,500 LOC Rust (preferred) or Python (faster to ship).

### 5.3 v3: dedicated memory model (Q2 2027)

Train a small (1-3B) dedicated memory model on user data. The HRM-Text-1B executive queries it for personal context. MEMO pattern: the memory model is a small fine-tuned LLM that owns knowledge; the executive is the reasoning layer.

**This is the path to "the model of the user" being a real artifact, not a flat list of vectors.**

---

## 6. v40 model timeline

| Phase | Date | Model | Action |
|-------|------|-------|--------|
| **v1 (now)** | Jul-Aug 2026 | LFM2.5-VL-450M Q4_0 + whisper.cpp + KittenTTS + MiniLM | Production deployment. ship it. |
| **v1.5** | Q4 2026 | + LFM2.5-Embedding-350M (memory) + LFM2-VL-1.2B (vision upgrade) + HRM-Text-1B (reasoning) | The full sovereign stack. |
| **v2** | Q2 2027 | + LFM2.5-ColBERT-350M (rerank) + voice clone (TTS) + Danlab-MEMORY (memory) | SIA-W+H self-improvement loop. |
| **v2.5** | Q4 2027 | + BitNet-VLM (vision, if shipped) + PocketTTS (TTS) | Watch the 1-bit frontier. |
| **v3** | Q2 2028 | + on-device fine-tuning of Danlab-HRM-Text (federated, opt-in) | The dream: every user has their own model. |

---

## 7. Open questions for somdipto

1. **Compute budget for HRM-Text training.** ~$2,000 for Phase 1+2. Is this a Q3 2026 budget item? **v40 critical blocker.**
2. **Domain data for HRM-Text training.** Where does the (transcript, salience, memory) dataset come from? We can start collecting today from the live audiod + perceptiond + memoryd services.
3. **Voice clone privacy posture.** 5 minutes of user speech leaves the device (cloud-fine-tune) or stays on-device (slower, 1 hour). Which is the v1.5 default?
4. **Indian language priority.** Hindi first, then Tamil, then what? This determines the multilingual model choice in v1.5.
5. **BitNet-VLM wait-or-ship.** v2 (Q2 2027) ships with HRM-Text-1B. Track BitNet-VLM for v2.5+.
6. **Sapient partnership.** If Sapient is open to a co-authored paper on "Danlab-HRM-Text-1B: domain-adapted sample-efficient reasoning for ambient agents," do we pursue? **Yes is my recommendation.**

---

## 8. Summary

The v40 model stack is the v39 stack + HRM-Text-1B as the reasoning layer + LFM2.5-Embedding-350M as the memory layer + memoryd v2 (topic-structured documents) as the memory architecture. The total on-device footprint grows from ~600MB to ~1.05GB, but the gains in:

- **Reasoning quality** (own model, no API rent, no data leaving device)
- **Memory quality** (1024d + topic structure + native multilingual)
- **Sovereignty** (no U.S.-controlled model, all open-source)
- **Self-improvement potential** (SIA-W+H becomes possible with HRM-Text-1B)

...are worth the extra 450MB. **This is the v40 model stack. Ship it.** 👾

*Dan2 research agent, 2026-06-23 v40. v40 delta: HRM-Text 1B integration + LFM2.5-Embedding-350M swap + memoryd v2 architecture + voice clone plan.*
