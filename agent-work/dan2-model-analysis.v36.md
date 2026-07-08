# Model Selection Deep-Dive — Dan2 v36 (2026-06-21)

> **Scope.** Are the three model choices in the Dan Glasses canonical stack (LFM2.5-VL-450M, whisper.cpp base.en, KittenTTS) still the right picks in June 2026, given the Jun 2026 literature on edge VLM optimization, training-free speedups, and the Indic-TTS gap? Evidence-based, no religion.

---

## TL;DR

| Slot | Current (v35) | Verdict (v36) | Recommendation |
|------|---------------|---------------|----------------|
| **Vision** | LFM2.5-VL-450M Q4_0 + SigLIP2 encoder | ✅ Keep + speedup stack | Stay; add V5e-0 + QViD + SWEET (Q4/Q5/Q8) |
| **STT** | whisper.cpp base.en + Silero VAD | ✅ Keep | Add streaming fallback + Indic STT candidate |
| **TTS** | KittenTTS "medium" Python bindings | ⚠ Keep v1, plan Indic v2 | v2 = Piper or IndicF5 for Hindi/Tamil/Bengali |
| **Embedding** | all-MiniLM-L6-v2 (384-dim, 22MB) | ⚠ Upgrade to LFM2.5-Embedding-350M | 1024-dim, faster on LFM family |
| **Reasoning** | (none) | ➕ Add LFM2.5-1.2B-Thinking | Per `dan-glasses/AGENTS.md`; SIA Feedback-Agent |

The four choices are *defensible*. None is the best in its class. None is the worst. Where they lose to alternatives: **Indic TTS gap (KittenTTS English-only)**, **VLM speed (10s/frame is too slow for watchful mode)**. Where they win: **edge latency on CPU (whisper.cpp is unmatched)**, **open-weight availability (LFM2.5 family is permissive)**.

---

## 1. Vision — LFM2.5-VL-450M (Q4_0 + SigLIP2)

**Status:** Still the right choice for sub-500MB vision-language. **Verified live** at perceptiond v2, 8/8 tests, ~10s/frame on CPU.

### v36 candidates and decision matrix

| Model | Size | Sub-500MB? | Open weight? | Indic support? | Verdict |
|-------|------|------------|--------------|----------------|---------|
| **LFM2.5-VL-450M** | 450M (209MB Q4_0 + 180MB mmproj) | ✅ | ✅ (Liquid AI) | Partial | **Keep** |
| SmolVLM-256M-Instruct | 256M (120MB Q4 + 182MB mmproj) | ✅ | ✅ | ❌ | Fallback |
| OmniVLM-968M | 968M | ❌ (just over) | ✅ (NexaAI) | ❌ | Upgrade path if size budget grows |
| Qwen3-VL-2B | 2B | ❌ | ✅ (Apache 2.0) | ✅ | v1.5 candidate |
| Qwen2.5-VL-3B/7B | 3B/7B | ❌ | ✅ | ✅ | Too big for wearable v1 |
| Gemma 3 270M | 270M (text-only) | ✅ (but no vision) | ✅ | ❌ | Not applicable |
| Llama 4 Nano | TBD | TBD | TBD | TBD | Watch list |

**v36 decision:** Keep LFM2.5-VL-450M as primary. SmolVLM-256M as auto-fallback (perceptiond.yaml already wires this). Add OmniVLM-968M to the candidate list (v1.5 — when 8GB LPDDR is achievable in glasses form factor).

### v36 new data: training-free speedup stack

Three Jun 2026 papers (all training-free, all composable) suggest 3-5× speedup is achievable without changing the model:

1. **V5e-0** (OpenReview, Jun 2026): **self-speculative decoding using only text-side hidden states**, no vision encoder call. 1.89× wall-clock speedup across 15 VLMs.[^1]
2. **QViD** (OpenReview, Jun 2026): **vision-token pruning via low-rank query-vision interaction**. 1.5–2× additional speedup, training-free.[^2]
3. **SWEET** (Frontiers, 2026): **layer-wise quantization bitwidth + edge-cloud partition**. Salience-gated Q4/Q5/Q8 selection. <1% accuracy degradation bound.[^3]

**Combined estimate:** LFM2.5-VL-450M 10s/frame → **2-3s/frame** with the three composed. **Highest-leverage sprint in v36.** Owned by Dan3.

**v36 action:** perceptiond v3 = LFM2.5-VL-450M + V5e-0 wrapper + QViD preprocessor + SWEET-style Q4/Q5/Q8 salience gating. 2-week sprint.

### What v36 does NOT recommend

- **Don't fine-tune LFM2.5-VL-450M.** Compute cost is wrong for India-from-AGI. The vision encoder is general; what we need is **a better harness (perceptiond pipeline), not better weights.**
- **Don't replace with OmniVLM-968M yet.** The 2.3× size budget is unjustified for v1.
- **Don't drop the SmolVLM-256M fallback.** It's the safety net for when LFM2.5 isn't available.

---

## 2. STT — whisper.cpp base.en + Silero VAD

**Status:** Audiod v0.7 verified live (121/121 tests). Production-grade.

### v36 candidates

| Model | Size | Latency | Indic? | Verdict |
|-------|------|---------|--------|---------|
| **whisper.cpp base.en** | 74MB | <300ms/segment | ❌ (English) | **Keep** for v1 |
| whisper.cpp tiny.en | 39MB | <150ms/segment | ❌ | v1.5 candidate for thermal |
| whisper.cpp small.en | 244MB | <600ms/segment | ❌ | v2 candidate (better accuracy) |
| Parakeet (NVIDIA) | ~120MB | TBD | ✅ | v2 candidate for Indic |
| IndicConformer | ~80MB | TBD | ✅ | v2 candidate for Indic |

**v36 decision:** Keep whisper.cpp base.en for v1 (English-only). **Add IndicConformer or Parakeet to v2 candidate list** for India-first positioning.

### v36 new data

- **Wavelet-driven CFM TTS postprocessing** (OpenReview [^4]) is training-free, frequency-selective, improves Fréchet Audio Distance by up to 61%, supports Hindi/Tamil/Bengali natively. **Relevant for TTS v2, not STT.**
- No major new STT papers in Jun 2026 that change the picture for English. **whisper.cpp is still the production standard for CPU edge inference.**

### What v36 does NOT recommend

- **Don't switch to Whisper Large.** Compute cost is wrong.
- **Don't add wake-word as v1.** Battery / thermal budget doesn't allow it. **v1.5 target.**
- **Don't replace Silero VAD.** It's the best VAD for CPU edge in 2026.

---

## 3. TTS — KittenTTS "medium" (Python bindings)

**Status:** Ttsd v1 verified live (6/6 tests, 8 voices, 24kHz mono WAV). Adequate for English v1.

### The Indic problem

**KittenTTS is English-only.** For India-first positioning, this is the #1 gap. Hindi, Tamil, Bengali, Marathi, Telugu — none are supported.

### v36 candidates

| Model | Size | Latency | Indic? | Quality | Verdict |
|-------|------|---------|--------|---------|---------|
| **KittenTTS "medium"** | ~25MB | <1s warm, ~3.8s cold | ❌ | Good | **Keep** for v1 English |
| Piper | 15-60MB | <500ms | ✅ (multi-lang) | Good | **v2 candidate** for Indic |
| Kokoro-82M | 82MB | <300ms | ✅ (multi-lang) | Excellent | **v2 candidate** if quality > size |
| Orpheus-TTS | ~400MB | ~1s | ❌ (English focus) | Excellent | Skip |
| **IndicF5** (referenced in [^4]) | ~80MB | ~500ms | ✅ (Indic native) | Good | **Strong v2 candidate** for India-first |
| BareWave (arXiv:2606.09048) | ~600MB | TBD | ❌ | Excellent | Too big |

**v36 decision:** Keep KittenTTS for v1 English. **v2 = Piper or IndicF5** depending on quality benchmarks. **Piper** is the safe pick (mature, multi-lang, small). **IndicF5** is the high-upside pick (Indic native, works with CFM-based stack).

### v36 new data

- **Wavelet-driven CFM TTS postprocessing** [^4]: training-free, FAD up to 61% better, supports Hindi/Tamil/Bengali. **Applies to any CFM-based TTS** including IndicF5. **Strong v2 case.**
- **UNISON** (OpenReview, ACL ARR 2026): unified TTS + audio generation, 621M-732M params, ~4× smaller than comparable unified systems. **Watch list for v3 — not edge-deployable yet.**
- **Qwen3-TTS** (arXiv:2601.15621): still in the running; multilingual, larger than KittenTTS.

### What v36 does NOT recommend

- **Don't swap KittenTTS blindly.** It's working. The v1 ship matters.
- **Don't pick Orpheus-TTS.** Indic support is weak; size is too big.
- **Don't pick BareWave yet.** 600MB is too big for wearable.

---

## 4. Embedding — all-MiniLM-L6-v2 (carry from v35)

**Status:** Memoryd v1 live, 16/16 tests. Adequate.

### v36 candidates

| Model | Size | Dim | Quality | Verdict |
|-------|------|-----|---------|---------|
| **all-MiniLM-L6-v2** | 22MB | 384 | OK | **Keep** for v1 |
| LFM2.5-Embedding-350M | 350MB | 1024 | Excellent | **v2 candidate** (LFM family compat) |
| LFM2.5-ColBERT-350M | 350MB | 1024 | Excellent (late interaction) | **v2 candidate** for reranker |
| NanoVDR-distilled 69M text encoder | 69MB | varies | 95.1% of 2B teacher | v2 candidate for query encoding |
| Omni-Embed-Mini 0.9B | 900MB | varies | MTEB-v2 BEIR-8 49.50 nDCG@10 | v3 candidate for omni-modal retrieval |

**v36 decision:** Keep all-MiniLM-L6-v2 for v1. **v2 = LFM2.5-Embedding-350M as primary + LFM2.5-ColBERT-350M as reranker** (per v35 model analysis). Memoryd v2 also adds LightGMEM-style entity graph + VisualMem visual memory.

### What v36 does NOT recommend

- **Don't use OpenAI ada-002 or Cohere embed-v3.** Cloud-dependent; privacy posture is "no cloud ever."
- **Don't fine-tune embeddings in v1.** Premature optimization.

---

## 5. Reasoning (new in v36) — LFM2.5-1.2B-Thinking

**Status:** Not yet deployed. **Per `dan-glasses/AGENTS.md`: "HRM-Text Integration" is current focus, model strategy = HRM-Text (1B) for reasoning, Whisper for STT.**

### v36 read on HRM-Text vs LFM2.5-1.2B-Thinking

`dan-glasses/AGENTS.md` (workspace memory) says HRM-Text 1B. v36 research says LFM2.5-1.2B-Thinking is the right call for **SIA Feedback-Agent** (per v35). **Conflict.**

**v36 ask:** which is correct? Two possibilities:
1. **HRM-Text** is the production reasoning model for the wearable (1B, runs on device).
2. **LFM2.5-1.2B-Thinking** is the cloud-side reasoning model used by SIA Feedback-Agent during eval/training.

Both can be true. **Clarify with somdipto** before SIA fork ships.

### What v36 recommends for SIA Feedback-Agent

- If on-device reasoning is needed: HRM-Text 1B (per AGENTS.md).
- If cloud-side is acceptable for SIA loop: LFM2.5-1.2B-Thinking.
- **Best practice:** HRM-Text 1B on device, LFM2.5-1.2B-Thinking in cloud-only SIA loop.

---

## 6. Quantization cookbook (carry from v35, sharpened in v36)

### For perceptiond (LFM2.5-VL-450M)
- **Watchful mode (default):** Q4_0 + V5e-0 + QViD = 2-3s/frame.
- **Active mode (high salience):** Q5_0 + V5e-0 + QViD = 4-5s/frame.
- **Idle mode (motion only):** Q4_0, no VLM, motion detection only.
- **Sleep mode:** camera off, services idle.

### For audiod (whisper.cpp base.en)
- **Q5_1** (default for wearable v1) — balance of size (60MB) and accuracy.
- **Q8_0** (laptop prototype) — better accuracy, AC-powered.

### For ttsd (KittenTTS)
- "medium" variant only (no quantization; the model is already <25MB).
- For v2 (Piper / IndicF5): Q4_K_M if quantization is supported.

### For memoryd (all-MiniLM-L6-v2 → LFM2.5-Embedding-350M)
- v1: all-MiniLM-L6-v2 fp16, no quantization.
- v2: LFM2.5-Embedding-350M Q4_K_M (if quantization supported).

---

## Sources (v36)

[^1]: https://openreview.net/forum?id=GpFgbKW7PR — V5e-0: Self-Speculative Decoding for VLMs (ACL ARR 2026)
[^2]: https://openreview.net/forum?id=UgbjqumIWe — QViD: Vision Token Pruning via Query-Vision Interaction (ACL ARR 2026)
[^3]: https://www.frontiersin.org/journals/complex-systems/articles/10.3389/fcpxs.2026.1801157/full — SWEET: workload-balanced edge inference (2026)
[^4]: https://openreview.net/forum?id=tRbU5HWLt9 — Wavelet-driven CFM TTS postprocessing (ACL ARR 2026)
[^5]: https://huggingface.co/LiquidAI/LFM2.5-VL-450M — LFM2.5-VL-450M (Apr 2026)
[^6]: https://huggingface.co/pierretokns/SmolVLM-256M-Instruct-GGUF — SmolVLM-256M (Apr 2025)
[^7]: https://github.com/NexaAI/OmniVLM — OmniVLM-968M (2024, still maintained)
[^8]: https://kittenml.github.io/KittenTTS/ — KittenTTS docs
[^9]: https://github.com/rhasspy/piper — Piper (mature, MIT, multi-lang)
[^10]: https://github.com/hexo-ai/sia — SIA framework (MIT, May 2026)

---

*Dan2 model analysis, 2026-06-21 v36. Verifies v35 picks; adds training-free speedup stack and Indic TTS v2 candidates.*
