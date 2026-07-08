# Dan-2 Model Analysis — v28 (2026-07-06)

> **Status:** v28 refresh. v27 content preserved. v28 deltas prepended.
> **Scope:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2 — are they still the right choices? What alternatives exist?
> **Verdict:** v23-v27 choices **all hold**. v28 adds 2 new model candidates and 1 new evaluation requirement.

---

## v28 Deltas (this refresh — 2026-07-06)

### 1. NEW MODEL CANDIDATE — Liquid LFM2.5-230M (text-only post-processor)

Released June 26 2026. 230M params, hybrid gated short-conv + grouped-query attention (no transformer). 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction (Liquid AI's own benchmark). llama.cpp + MLX + vLLM + SGLang + ONNX support. Open-weight, dual-license (free <$10M ARR, paid enterprise).

**v28 verdict:** LFM2.5-230M is the v1.0 audiod post-processor plan-A, displacing HRM-Text-1B. The audiod post-processor ordering is now: LFM2.5-230M (v1.0) → HRM-Text-1B (v1.5 plan-A) → Apertus v1.1 4B (v1.5 plan-B) → OpenPhone-3B (v1.5 plan-C).

### 2. NEW MODEL CANDIDATE — nomic-embed-text v1.5 (137M embedder)

nomic-embed-text v1.5 (137M params, 768 dims) is the SOTA local embedder per Local RAG with Ollama (2026) and the AIMultiple open-source embedding benchmark. 7B chat at Q4 + embedder = 6GB total, comfortable on 8GB GPU.

**v28 verdict:** if memoryd can run on the **companion laptop**, nomic-embed-text v1.5 is the v1.0 embedder (replaces MiniLM-L6-v2). If memoryd must run on the **glasses** (edge-only), MiniLM-L6-v2 (22M params, 384 dims, 80MB) remains the v1.0 choice. **Decision deferred to v1.0 spec; current memoryd runs on the laptop, so nomic-embed-text v1.5 is the v28 preferred path.**

### 3. NEW EVALUATION REQUIREMENT — MemDelta-controlled baseline

MemDelta paper (arXiv 2606.29914, late June 2026): swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500, p<0.004. Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — **one variable flips the conclusion**.

**v28 verdict:** any model swap (MiniLM-L6-v2 → nomic-embed-text v1.5, or any other) must be evaluated under the MemDelta protocol: vary one component at a time on LongMemEval-S, require pre-registered margin. Add to v27 plan-P1.

### 4. NEW EVALUATION REQUIREMENT — AIMultiple cross-domain methodology

AIMultiple's open-source embedding benchmark (retrieved 2026-07-03) publishes the first cross-domain consensus methodology: Protocol-A 3-LLM consensus query generation, corpus pinning by SHA-256 hash, per-domain entity-banned-token whitelists, Cohen's κ inter-rater agreement.

**v28 verdict:** the v1.0 embedder decision must use this methodology, not a single-domain synthetic test. Add to v27 plan-P1.

### 5. NEW MODEL CANDIDATE — NVIDIA Nemotron on-device (4B at Q4)

NVIDIA XR AI open-source library (June 2026) ships Nemotron for on-device language. Vitre Helix reference platform uses it. 4B at Q4 fits on Snapdragon AR1 Gen 2 (the Meta Ray-Ban Display chip). Open-weight, NVIDIA-tuned.

**v28 verdict:** compare Nemotron-4B-Q4 vs LFM2.5-1.2B-Thinking for v1.0 reasoning. Both are open-weight, ~4B, edge-deployable. LFM2.5 wins on the "no NVIDIA lock-in" axis; Nemotron wins on the "NVIDIA-validated reference platform" axis. **Decision deferred to v28 plan-S2 chip-stack sovereignty review.**

### 6. CONFIRMED — KittenTTS vs Kokoro-82M (TTS update)

v27 confirmed Kokoro-82M as the SOTA TTS benchmark. v28 re-verifies: Kokoro-82M (Hexo Labs, January 2026 release) is still the SOTA on quality. KittenTTS remains the v1.0 choice due to **on-device Python API maturity** (no ONNX runtime needed) and **8 voice IDs** (Kokoro has fewer). **Verdict: KittenTTS for v1.0; Kokoro-82M for v1.5 TTS upgrade.**

### 7. CONFIRMED — LFM2.5-VL-450M still the v1.0 VLM

v23-v27 chose LFM2.5-VL-450M (April 2026 release) as the v1.0 VLM. v28 re-verifies against:
- SmolVLM-256M (smaller, lower quality)
- SmolVLM2-500M (newer, comparable quality)
- LFM2.5-Extract (Liquid AI's data-extraction variant, not conversational)

**v28 verdict:** LFM2.5-VL-450M still wins on the **conversational VLM + liquid arch (no transformer) + Q4 209MB + edge-viable** combination. v1.5 candidate: **LFM2.5-VL-1.2B (if released in 2026 H2)** — 2.7× larger, may not fit on the 200mAh battery budget.

### 8. CONFIRMED — whisper.cpp base.en still the v1.0 STT

v23-v27 chose whisper.cpp base.en. v28 re-verifies against:
- Whisper-large-v3 (too large for edge)
- Distil-Whisper (faster, but lower accuracy on long-form)
- Parakeet / Canary (NVIDIA, more recent, but less tested)

**v28 verdict:** whisper.cpp base.en is still the v1.0 STT. v1.5 candidate: **Parakeet-TDT-0.6B (NVIDIA, ~600MB, on-device)** if the v1.0 path shows accuracy issues. Add to v1.5 spike list.

---

## v28 v1.0 Model Decisions (final)

| Layer | v1.0 model | v1.5 candidate | Why |
|-------|------------|----------------|-----|
| STT (audiod) | whisper.cpp base.en | Parakeet-TDT-0.6B | base.en is 142MB, fast, accurate. Parakeet is a possible v1.5 upgrade. |
| Reasoning (post-processor) | **LFM2.5-230M (v28 NEW)** | HRM-Text-1B or Nemotron-4B-Q4 | LFM2.5-230M is the v28 best on-device reasoning model. |
| Vision (perceptiond) | LFM2.5-VL-450M | LFM2.5-VL-1.2B (if released) | LFM2.5-VL-450M is still the SOTA sub-250MB VLM. |
| TTS (ttsd) | KittenTTS medium | Kokoro-82M | KittenTTS for v1.0 maturity; Kokoro-82M for v1.5 quality. |
| Embedding (memoryd) | **nomic-embed-text v1.5 (v28 NEW, if on laptop)** or MiniLM-L6-v2 (if on glasses) | — | Depends on deployment shape. AIMultiple + MemDelta evaluation required before swap. |
| Agent framework (openclaw) | **Hermes Agent (v28 NEW)** | SIA-W+H (research bet) | Hermes Agent is the v28 1-2 week drop-in. SIA-W+H is the 3-week research bet. |

---

## v28 v1.0 Plan Additions

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-P3 (NEW) | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 | Q3 W2 |
| plan-P4 (NEW) | SIA-W+H port (LoRA training in the loop) | 3 | Q3 W3-W4 |
| plan-M1 (NEW) | nomic-embed-text v1.5 vs MiniLM-L6-v2 MemDelta-controlled baseline (with v27 plan-P1) | 1 | Q3 W3 |
| plan-M2 (NEW) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark on audiod post-processor | 1 | Q3 W2 |

---

*Maintained by DAN-2. v28 is a model-delta on v27. All v23-v27 model choices hold; v28 adds 2 new candidates (LFM2.5-230M, nomic-embed-text v1.5) and 2 new evaluation requirements (MemDelta, AIMultiple).*
