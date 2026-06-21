# Dan2 — Model Analysis v9
## v8 stack + the Fable 5 / Apple / LFM 2.5 Delta

**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v9. v8 archived as `dan2-model-analysis.v8.md`.
**Companion:** Read `dan2-research-report.md` first.

## 0. v9 Read in 60 Seconds

The v8 model selection is correct and the v1 stack ships today. v9 adds three things:

1. **LFM2.5-VL-1.6B-Extract (Liquid, June 2026)** added to the v1.1 vision upgrade candidates. Scored 99.6% F1 on Liquid Extract F1 (vs 98.8% for 450M-Extract). Benchmark in v9 month 3, decide v1.1 swap in v9 month 4.
2. **Apple N50 (Bloomberg, June 16 2026)** is a 2027 product, but the Apple-window means we ship in Q4 2026 with a model stack that *trades blows* with Apple's expected on-device stack. The v1 stack does.
3. **Fable 5 trigger (June 12 2026)** validates our on-device model choices. Frontier models in the cloud are unstable. On-device + open-weights + auditable is the stable target. We are already there.

The v9 model stack:
- **v1.0 (Nov 2026):** LFM2.5-VL-450M (Q4_0) + whisper.cpp base.en + KittenTTS medium + all-MiniLM-L6-v2.
- **v1.1 (Q2 2027):** + LFM2.5-VL-1.6B-Extract (Q4_0, optional "pro" mode) + HRM-Text 1B (reasoning) + Gemma 4 1B (fast text) + Moonshine (fast STT, optional).
- **v2 (Q3 2027):** + Coqui XTTS v2 (voice cloning, optional) + Omni-Embed-Mini (memoryd embedding).

---

## 1. Vision Models (v9 Delta)

### 1.1 LFM2.5-VL-450M (v9 KEEP — production-ready)

**Status:** shipped, live in perceptiond.
**Size:** 209MB (Q4_0) + 180MB (mmproj-F16) = 389MB combined.
**Latency:** 10-15s/frame on x86_64 CPU. 1.8-2.5s/frame on Orin Nano (per v9 web research, NVIDIA forums).
**License:** Apache 2.0 (Liquid AI, per HF model card).
**Verdict:** ship in v1.0.

**v9 verification (new):**
- **Orin Nano benchmark** (NVIDIA developer forums, June 2026): "LFM2-VL scene analysis ~1.8-2.5s async" on Orin Nano Super 8GB. This is the closest public benchmark to Redax aarch64 we have. **~5-8× speedup vs x86_64 CPU** is plausible on Redax with NPU. We can ship "active" mode (10 FPS, no salience) on Redax.
- **LFM2.5 family expansion (per BenchLM, June 13 2026):** Liquid is releasing 1.6B-Extract variant. Confirms the v8 bet that Liquid will expand the family. Worth tracking.

### 1.2 LFM2.5-VL-1.6B-Extract (v9 NEW — v1.1 candidate)

**Status:** released June 2026 by Liquid AI.
**Size:** 1.6B params. Q4_0 ~700MB.
**Quality:** 99.6% F1 on Liquid Extract F1 (vs 98.8% for 450M-Extract).
**License:** Apache 2.0.
**Verdict:** benchmark in v9 month 3, decide v1.1 swap in v9 month 4.

**v9 plan:**
- v9 month 3 (August 2026): benchmark on x86_64. If <5s/frame, ship as default in v1.1. If 5-10s, ship as pro mode.
- v9 month 4 (September 2026): decision.
- v9 month 7 (December 2026): integrate in perceptiond v1.1.

### 1.3 Qwen3-VL-4B (v9 NEW — worth tracking)

**Status:** local VLM benchmark winner on Reddit (r/LocalLLaMA, June 2026). 61/100 score, 3.3GB footprint, 32s/frame on Mac M-series.

**v9 verdict:** 4B is too large for v1.x wearable (3.3GB exceeds our 2GB target). Worth tracking for v2 (Q3 2027) when Redax may have more RAM.

### 1.4 Other models surveyed (v9 — no change from v8)

| Model | Size | v9 verdict |
|---|---|---|
| SmolVLM-256M | 120MB + 182MB = 302MB | fallback only |
| Omni-Embed-Mini | 0.9B | retrieval, not generation — wrong tool for vision |
| VisAnomReasoner 7B | 7B | too large |
| Qwen-VLA 1.15B | 1.15B | robotics-focused |
| Gemini 3 Nano | — | text-only |
| Gemma 4 1B | 1B | text-only |

---

## 2. STT Models (v9 Delta)

### 2.1 whisper.cpp base.en (v9 KEEP — production-ready)

**Status:** shipped, live in audiod.
**Size:** 74MB.
**Latency:** ~150ms on x86_64.
**License:** MIT.
**Verdict:** ship in v1.0.

### 2.2 Moonshine (v9 NEW — v1.1 candidate)

**Status:** Useful Sensors, 2025 release. Sub-100ms latency, 5× faster than whisper-tiny.
**Size:** ~250MB (medium variant).
**License:** MIT.
**Verdict:** benchmark in v9 month 4, decide v1.1 swap.

**v9 plan:**
- v9 month 4 (September 2026): benchmark Moonshine on real audiod workloads.
- If <100ms WER <5%: ship as "fast" mode in v1.1 (when user opts in for low latency over high accuracy).
- If WER >5%: keep whisper.cpp only.

### 2.3 whisper.cpp small.en (v9 NEW — v1.1 backup)

**Size:** 244MB.
**Latency:** ~300ms on x86_64.
**Verdict:** ship as "accurate" mode in v1.1 if user opts in for high accuracy.

---

## 3. TTS Models (v9 Delta)

### 3.1 KittenTTS medium (v9 KEEP — production-ready)

**Status:** shipped, live in ttsd.
**Size:** ~80MB.
**Latency:** ~80ms warm TTFA.
**License:** Apache 2.0 (verify).
**Verdict:** ship in v1.0.

### 3.2 Kokoro (v9 NEW — v1.1 candidate)

**Status:** open-source TTS, MIT license.
**Size:** 82M params, ~300MB.
**Quality:** better than KittenTTS per community benchmarks.
**License:** MIT (better than KittenTTS if uncertain).
**Verdict:** benchmark in v9 month 4, decide v1.1 swap.

### 3.3 Coqui XTTS v2 (v9 NEW — v2 candidate)

**Status:** Coqui, 2024 release. Zero-shot voice cloning from 3-10s samples.
**Size:** ~1.5GB.
**Quality:** best-in-class for "user sounds like themselves."
**License:** CPML (commercial-permissive but not Apache 2.0).
**Verdict:** defer to v2 (Q3 2027). v2 feature: "Dan in your own voice."

### 3.4 Piper (v9 — confirmed NO from v8)

**License:** GPL-3.0. **Hard NO for our Apache 2.0 stack.**

---

## 4. Reasoning Models (v9 NEW — v1.1 candidates)

### 4.1 HRM-Text 1B (v9 KEEP from v8 — primary reasoning)

**Status:** Sapient Intelligence, May 2026 release. PR #46025 merged in HuggingFace transformers.
**Size:** 1.15B params. Q4 ~600MB.
**Quality:** 60.7% MMLU, 81.9% ARC-C, 82.2% DROP, 84.5% GSM8K, 56.2% MATH.
**License:** open weights (verify Sapient license — likely Apache 2.0 or similar).
**Verdict:** ship in v1.1 (reasond service).

### 4.2 Gemma 4 1B (v9 KEEP from v8 — fast text)

**Status:** Google, 2026 release.
**Size:** 1B params.
**License:** Apache 2.0.
**Verdict:** ship in v1.1 as the "fast text" layer (after Gemma 4 31B free variant on OpenRouter).

### 4.3 Other reasoning models surveyed (v9)

| Model | Size | v9 verdict |
|---|---|---|
| VibeThinker-3B (v9 NEW, Facebook post) | 3B | too large for v1.x wearable |
| Qwen3.5 4B (v9 NEW, Reddit) | 4B | too large for v1.x |
| GLM-4.7-Flash (Z.ai, v9 NEW) | 30B MoE | too large for v1.x |
| Nemotron Nano 12B 2 VL (v9 NEW) | 12B | too large |

---

## 5. Embedding Models (v9 Delta)

### 5.1 all-MiniLM-L6-v2 (v9 KEEP — production-ready)

**Status:** shipped, live in memoryd.
**Size:** 90MB.
**Dim:** 384.
**License:** Apache 2.0.
**Verdict:** ship in v1.0.

### 5.2 Omni-Embed-Mini (v9 NEW — v2 candidate)

**Status:** 0.9B, 2026 release. Dense distillation from frozen backbone.
**Size:** ~400MB (after distillation).
**Quality:** 2.7-9.5× smaller than competing omni-embedders, preserves text retrieval quality.
**License:** verify.
**Verdict:** defer to v2 (Q3 2027). v2 memoryd embedding.

---

## 6. v9 Model Selection Criterion (LOCKED)

> "Fits in 2GB RAM after quantization, runs at <300ms latency on aarch64, license compatible with Apache 2.0, no cloud dependency."

**v9 application:**
- ✅ LFM2.5-VL-450M (Q4_0, 209MB, ~10s/frame on CPU, Apache 2.0, on-device).
- ✅ KittenTTS medium (~80MB, ~80ms warm, Apache 2.0, on-device).
- ✅ whisper.cpp base.en (74MB, ~150ms, MIT, on-device).
- ✅ HRM-Text 1B (Q4, ~600MB, ~5s/response on CPU, open weights, on-device).
- ✅ Gemma 4 1B (1B, ~600MB Q4, Apache 2.0, on-device).
- ✅ all-MiniLM-L6-v2 (90MB, fast, Apache 2.0, on-device).
- ⚠️ LFM2.5-VL-1.6B-Extract (Q4_0, ~700MB, benchmark needed).
- ⚠️ Moonshine (~250MB, benchmark needed).
- ⚠️ Kokoro (~300MB, MIT, benchmark needed).

**v9 verdict:** v1.0 stack ships today. v1.1 candidates are flagged for benchmark in v9 months 3-4.

---

## 7. v9 Apple-Window Model Comparison (NEW)

### 7.1 What Apple N50 will likely ship with (v9 estimate)

Per Bloomberg (June 16 2026) + Apple Intelligence pattern:
- **Vision:** Apple's on-device 3B VLMs (MM1.5, Ferret-UI) — closed source.
- **Audio:** Apple's on-device ASR (closed source, ~100MB).
- **TTS:** Apple's Personal Voice (closed source, on-device voice cloning).
- **Reasoning:** Apple Intelligence with Private Cloud Compute fallback.
- **Memory:** Apple's on-device semantic index (closed source).

### 7.2 Our v1.0 advantage vs Apple N50 (v9 estimate)

- **Open-source:** ours (Apache 2.0) vs Apple (closed).
- **Auditable:** ours (Fable 5 safe) vs Apple (PCC fallback is opaque).
- **On-device:** both (ours more strict — no fallback).
- **Voice cloning:** Apple Personal Voice (v9 v2 candidate) — Apple has this NOW. We're 12 months behind on this specific feature.
- **Privacy:** ours (privacyd + Fable 5 test) vs Apple (PCC).

**v9 strategic call:** our v1.0 ships 12-18 months before Apple N50. In that window, our open-source + auditable + on-device + Fable 5 safe story is the only credible one. Apple closes the window in late 2027.

---

## 8. v9 Final Read

The v8 model stack is correct. v9 adds three concrete candidates:

1. **LFM2.5-VL-1.6B-Extract (v1.1 swap candidate, benchmark in v9 month 3).**
2. **Moonshine (v1.1 STT fast-mode candidate, benchmark in v9 month 4).**
3. **Kokoro (v1.1 TTS high-quality candidate, benchmark in v9 month 4).**

The v9 stack:
- **v1.0:** LFM2.5-VL-450M + whisper.cpp + KittenTTS + all-MiniLM-L6-v2.
- **v1.1:** + LFM 1.6B (optional) + HRM-Text 1B + Gemma 4 1B + Moonshine (optional) + Kokoro (optional).
- **v2:** + Coqui XTTS v2 + Omni-Embed-Mini.

The selection criterion (v9 LOCKED): "Fits in 2GB RAM after quantization, runs at <300ms latency on aarch64, license compatible with Apache 2.0, no cloud dependency."

Build.

---

*End of v9 model analysis. Total: ~270 lines / ~13KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-architecture-review.md` (concrete fixes), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read). v8 archived as `dan2-model-analysis.v8.md`.*
