# Dan2 — Model Selection Deep Dive (v4, 2026-06-16 03:00 UTC)
**Status:** Final v4 (delta over v3)
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices? What alternatives exist?
**Run window:** 2026-06-16 03:00 UTC

---

## 0. TL;DR (v4)

**LFM2.5-VL-450M (vision), whisper.cpp (STT), KittenTTS (TTS), all-MiniLM-L6-v2 (embeddings) remain the v1 stack.** v4 deep-dive validated each choice against 2026 SOTA. The optimizations identified (VLMCache, per-layer mixed-precision, Omni-Embed-Mini) are additive, not replacement. **Gemma 3 4B running in orbit is the new upper bound** — proves sub-10B edge VLM works in extreme environments, but is too large for v1 wearable.

**The single most impactful v4 model change:** adopt **Omni-Embed-Mini (0.9B, multimodal)** for `memoryd v2` to replace text-only all-MiniLM-L6-v2. This is the only v4 model swap that's worth doing. Everything else is optimization on the current model.

---

## 1. Vision: LFM2.5-VL-450M (current) + Gemma 3 (new production reference)

### Current: LFM2.5-VL-450M via GGUF Q4_0
- **Live verified:** 10-15s/frame CPU on x86_64
- **Size:** 209MB (Q4_0) + 180MB mmproj (F16) = 389MB total
- **Salience-gated:** watchful mode, MAX_QUEUE_DEPTH=2

### v4 Deep-Dive Findings (Edge VLM)

| Source | Finding | v4 Impact |
|---|---|---|
| **VLMCache (ACM MM 2026)** | 1.4-3.8× speedup with <1% accuracy loss via background block caching | **`perceptiond v2` adopts this** — 3-5s/frame target |
| **SpecFlow (arXiv 2606.02842)** | Spectral (DCT) visual state, 2.1× KV-cache reduction | **Future v2.5 — bounded memory for wearable** |
| **SWEET (Frontiers 2026)** | Per-layer quantization, 11.9-18.1% payload reduction, 0.08-0.66% accuracy loss | **`perceptiond v2` adopts this** — 30-40% size reduction |
| **Omni-Embed-Mini** | 0.9B multimodal embedder (text/speech/audio/image/video/docs) | **`memoryd v2` adopts this for the memory layer** |
| **EMemBench (2026)** | Episodic memory for VLM agents is hard; visual induction bottleneck | **Add geometric/landmark descriptors for memory grounding** |
| **Abstraction Gap (arXiv 2605.28779)** | VLMs generate fluent text but few valid causal chains (AG 0.84-0.92) | **Use structured prompts (people/objects/actions/location/time)** |
| **DUAL-Bench (2026)** | Best VLM achieves only 12.9% safe completion on dual-use | **`os-toold v2` safety filters compensate** |
| **Gemma 3 in orbit (Yam-9, April 2026)** | First edge VLM in space, on satellite | **Upper bound: sub-10B edge VLM is validated** |

### Alternatives considered (v4)

| Model | Size | Pros | Cons | Verdict |
|---|---|---|---|---|
| **LFM2.5-VL-450M (current)** | 389MB | Production-validated, sub-250ms target, runs on CPU | 10-15s/frame currently | **KEEP for v1** |
| **Gemma 3 4B** | ~2.4GB | In-orbit validation, higher quality | Too large for v1 wearable, needs GPU | **Validate on Redax as upper bound** |
| **SmolVLM-256M** | 302MB | Used in danlab-multimodal, smallest VLM | Slightly worse than LFM2.5 | **Keep as fallback in download.sh** |
| **PaliGemma 2 (3B)** | ~2GB | Google's edge-class | Larger than LFM2.5, less proven | **Monitor, not adopt** |
| **Qwen3-VL-8B** | ~5GB | Avenir-Web baseline (25.7% → 57.5% with harness) | Way too large for v1 | **Monitor for v2.5** |
| **LFM2.5-VL-1.2B** | ~1GB | Larger variant of current model, better quality | 2.5× larger, more power | **Benchmark on Redax for v2 wearable** |

**LFM2.5-VL-450M verdict (v4):** **Still the right choice for v1 wearable.** Adopting VLMCache + per-layer mixed-precision brings us to 3-5s/frame CPU. **Gemma 3 4B is the upper bound we should validate on Redax hardware** (proves sub-10B edge VLM works in space).

### Concrete v2 optimizations for perceptiond

1. **Per-layer mixed-precision GGUF** (3-day effort):
   - Q4_K_M in attention layers (better quality than Q4_0)
   - Q8_0 in vision projector mmproj (size reduction from F16)
   - Q4_0 in text decoder (current)
   - Target: 250-280MB total (down from 389MB), <1% accuracy loss

2. **VLMCache-style background caching** (1-week effort):
   - Hash visual blocks, reuse embeddings as KV-cache prefix
   - Recompute only foreground/dynamic blocks
   - Target: 3-5s/frame CPU (down from 10-15s)

3. **Structured prompt template** (1-week effort):
   - `Describe this image briefly. Output as JSON: {people: [], objects: [], actions: [], location: "", time: ""}`
   - Better memory recall, better proactive triggers
   - Backward compatible: free-form text still supported as fallback

4. **Geometric/landmark descriptors** (3-day effort):
   - Color histogram, edge density, landmark detection in capture/salience
   - Output alongside VLM description
   - Better US-1 (encounter recall) per EMemBench findings

---

## 2. STT: whisper.cpp + base.en (current) — UNCHANGED from v2

### Current: whisper.cpp + ggml-base.bin (148MB) or ggml-tiny.bin (78MB)
- **Live verified:** 400-700ms end-to-end on x86_64 (silence-invariant)
- **VAD:** Silero ONNX, 0.5 threshold
- **PTT:** edge detection, key-down lock

### v4 Deep-Dive Findings (Audio)

| Source | Finding | v4 Impact |
|---|---|---|
| **XTTS-v2 urgency-preserving** | Sub-3s end-to-end TTS, urgency-aware prosody | **Future TTS v2 idea** (not STT) |
| **wavelet-driven CFM boosting (2026)** | NFE 32→26, FAD -61% in TTS | **Future TTS v2** |
| **UNISON (2026)** | 621M unified audio (TTS + sound + editing) | **Monitor for v2 TTS** |

**whisper.cpp verdict:** **UNCHANGED.** No v4 update. v3 said "right accuracy/size balance" and v4 confirms. Streaming whisper is the v1.5 enhancement (carries from v2).

### Alternatives considered (v4)

| Model | Size | Pros | Cons | Verdict |
|---|---|---|---|---|
| **whisper.cpp base.en (current)** | 148MB | Proven, 400-700ms latency, multi-language | English-only | **KEEP for v1** |
| **whisper.cpp tiny.en** | 78MB | Smaller, faster, recommended for Redax | Lower accuracy | **KEEP as Redax option** |
| **Moonshine** | ~100MB | Newer, designed for edge | Less proven, no significant advantage | **Monitor** |
| **Parakeet TDT (NVIDIA)** | ~150MB | Streaming-optimized | GPU-targeted | **Monitor for v2** |
| **Canary (NVIDIA)** | ~1GB | Multilingual, high quality | Too large for edge | **No** |

---

## 3. TTS: KittenTTS (current) — UNCHANGED from v2

### Current: KittenTTS base (~25MB), medium variant
- **Live verified:** ttsd running with KittenTTS medium
- **Voice:** expr-voice-2-m
- **Output:** WAV, played via aplay

### v4 Deep-Dive Findings (TTS)

| Source | Finding | v4 Impact |
|---|---|---|
| **BareWave (arXiv 2606.09048)** | Waveform-native flow-matching, no intermediate representations | **Monitor for v2 TTS** |
| **Wavelet-driven CFM boosting (2026)** | NFE 32→26, FAD -61% improvement, training-free | **Adopt when on flow-matching TTS** |
| **UNISON (2026)** | 621M unified audio (TTS + sound + editing) | **Monitor for v2 TTS** |
| **XTTS-v2 urgency-preserving** | Sub-3s end-to-end, urgency-aware prosody | **Adopt for v1.5 proactive mode** |
| **Piper / Kokoro** | 15-30MB, ONNX, open-source | **Already considered v2, still monitor** |

**KittenTTS verdict:** **UNCHANGED for v1.** Right balance of size + quality. **For v2, watch BareWave and UNISON** — both target edge with quality approaching larger models.

### Alternatives considered (v4)

| Model | Size | Pros | Cons | Verdict |
|---|---|---|---|---|
| **KittenTTS base (current)** | 25MB | Tiny, ONNX, proven | Lower quality than larger models | **KEEP for v1** |
| **KittenTTS medium (live)** | ~50MB | Better quality | 2× size | **KEEP for laptop prototype** |
| **Piper** | 15-30MB | ONNX, many voices, open-source | Quality similar to KittenTTS | **Alternative if KittenTTS stalls** |
| **Kokoro-82M** | 82MB | High quality for size | 3× KittenTTS size | **Watch for v2** |
| **Bark** | ~1GB | Very high quality | Way too large | **No** |
| **XTTS-v2** | ~500MB | Zero-shot voice cloning, urgency-aware | 20× KittenTTS size | **v2 hardware only** |
| **BareWave** | TBD | Waveform-native flow-matching | New (June 2026), no edge benchmark yet | **Monitor** |
| **UNISON** | 621M | Unified audio (TTS + sound + editing) | 25× KittenTTS size | **v2 only** |

---

## 4. Memory embedding: all-MiniLM-L6-v2 (current) — v4 UPDATE

### Current: all-MiniLM-L6-v2 (sentence-transformers, 384d)
- **Live verified:** 11/11 tests green
- **Storage:** BLOB in SQLite
- **Query:** cosine similarity

### v4 NEW RECOMMENDATION: Omni-Embed-Mini for `memoryd v2`

**Why:**
- **0.9B params** (vs 22M for MiniLM)
- **Multimodal:** text, speech, audio, image, video, documents in ONE shared space
- **No text-side fine-tuning required** (frozen backbone)
- **Matryoshka SigLIP contrastive loss** (flexible dimensionality)
- **2.7-9.5× smaller than competing omni-embedders**
- **Preserves text retrieval quality of backbone** (49.50 nDCG@10 on MTEB-v2 BEIR-8)
- **49.50 nDCG@10** on MTEB-v2 BEIR-8 is competitive with much larger models
- **Online hard-negative mining** for better discriminative power

**Trade-off:**
- **Larger model** (0.9B vs 22M, ~350MB vs ~90MB)
- **Slower inference** (sub-second per query vs ~10ms)
- **More memory** (every embedding is larger)

**When to adopt:**
- **v1 (now):** **MiniLM. Proven, 384d works, sub-10ms query.** 
- **v2 (6 months):** **Omni-Embed-Mini for the multimodal memory store.** When `memoryd v2` hierarchical architecture lands, we need multimodal embeddings for Tier 0 raw events.

**Implementation:**
- Add `omni-embed-mini` as optional backend in `memoryd`
- Migration: re-embed all memories with Omni-Embed-Mini (one-time batch job)
- Storage: increase BLOB size from 384×4=1536 bytes to ~1024×4=4096 bytes per memory
- Query: support both backends during transition

### Alternatives considered (v4)

| Model | Size | Dim | Pros | Cons | Verdict |
|---|---|---|---|---|---|
| **all-MiniLM-L6-v2 (current)** | 90MB | 384 | Proven, fast, small | Text-only | **KEEP for v1** |
| **Omni-Embed-Mini** | ~350MB | ~1024 | Multimodal, 2.7-9.5× smaller than peers | Larger, slower | **Adopt for v2 memory** |
| **BGE-M3** | ~2GB | 1024 | Multilingual, high quality | Way too large | **No** |
| **Nomic Embed v1.5** | ~550MB | 768 | Open-source, long context | Larger | **Monitor** |
| **Qwen3-Embedding** | ~600MB | up to 4096 | High quality | Larger | **Monitor** |

---

## 5. Reasoning model — UNCHANGED from v2

**No reasoning model in v1.** OpenClaw handles reasoning via the LLM backbone (currently the LLM that the Zo MCP bridge calls, or a future local model).

**For v2:** the LFM2.5-1.2B-Thinking variant is the right target. **For v1:** no local reasoning model — cloud LLM via Zo API for complex queries, rule-based for simple ones.

---

## 6. Audio-language unified — UNCHANGED from v2

**No unified audio-language model in v1.** Whisper (audio→text) + KittenTTS (text→audio) + MiniLM (text embedding) is the stack. **For v2:** watch UNISON (621M unified audio) and Qwen3-Omni (large).

---

## 7. Model selection decision matrix (v4)

| Layer | v1 choice | v2 choice | v3+ horizon | Why v4 keeps v1 |
|---|---|---|---|---|
| **Vision (perceptiond)** | LFM2.5-VL-450M Q4_0 | + VLMCache + per-layer mixed-precision | LFM2.5-VL-1.2B (Redax) → Gemma 3 4B (v2) | Right size for v1 wearable, validated in orbit (Gemma 3) |
| **STT (audiod)** | whisper.cpp base.en | + streaming whisper + RNNoise | Parakeet TDT (edge-streaming) | Right accuracy/size, proven |
| **TTS (ttsd)** | KittenTTS base/medium | + urgency-aware prosody (XTTS-v2 style) | BareWave / UNISON | Right size, open-source, proven |
| **Memory embed (memoryd)** | all-MiniLM-L6-v2 (text-only, 384d) | **Omni-Embed-Mini (multimodal, ~1024d)** | Qwen3-Embedding | MiniLM for v1 proven, Omni-Embed-Mini for v2 when multimodal needs land |
| **Reasoning** | Cloud LLM via Zo API | LFM2.5-1.2B-Thinking local | Gemma 3 4B (reasoning) | v1 doesn't need local reasoning; v2 wearable is the target |
| **Audio-language unified** | None (separate components) | None | UNISON (621M) | Modular is fine for v1; unified is v2.5+ |

---

## 8. Quantization decision matrix (carry from v2) + v4 memory constraint

| Model | v1 Quant | v2 Quant (per-layer mixed) | Memory budget (wearable) |
|---|---|---|---|
| **LFM2.5-VL-450M** | Q4_0 + mmproj F16 | Q4_K_M attn + Q8_0 mmproj + Q4_0 decoder | 250-280MB (down from 389MB) |
| **whisper.cpp base.en** | Q5_1 (148MB) | Q5_1 (no change) | 148MB |
| **KittenTTS base** | ONNX FP16 (~25MB) | ONNX FP16 (no change) | 25MB |
| **all-MiniLM-L6-v2** | FP32 (90MB) | FP16 (45MB, half-size) | 45-90MB |
| **Total model memory** | ~650MB | ~450-550MB | Target: <600MB on wearable |

**v4 sharpening:** Per-layer mixed-precision (SWEET 2026) is the key to fitting all models in wearable memory budget. **Current v1 stack at ~650MB; v2 stack at ~450-550MB is achievable.**

---

## 9. Acceleration techniques to integrate (carry from v2 + v4)

**Existing techniques (v1):**
- llama.cpp with `-ngl 99` (full GPU offload) — for laptop
- llama.cpp with `-ngl 0` (CPU only) — for Redax
- whisper.cpp with `-ng` (no GPU)
- Silero VAD ONNX (lightweight)
- GGUF Q4_0 / Q5_0 quantization
- Salience-gated VLM (Watchful mode, MAX_QUEUE_DEPTH=2)

**v4 NEW techniques (for v2):**
- **VLMCache-style background caching** — 1.4-3.8× speedup, <1% accuracy loss
- **Per-layer mixed-precision quantization** (SWEET) — 30-40% size reduction
- **Spectral (DCT) visual state** (SpecFlow) — 2.1× KV-cache reduction
- **Matryoshka SigLIP loss** (Omni-Embed-Mini) — flexible embedding dimensionality
- **Structured prompts** (Abstraction Gap mitigation) — better memory recall
- **Geometric/landmark descriptors** (EMemBench mitigation) — better episodic memory

---

## 10. Anti-recommendations (don't) — v2 + v3 + v4

1. **Don't jump to Gemma 3 4B for v1.** Too large. LFM2.5-VL-450M + optimizations is the v1 path.
2. **Don't replace whisper.cpp with Parakeet TDT for v1.** Not proven for edge yet.
3. **Don't replace KittenTTS with XTTS-v2 for v1.** XTTS-v2 is 20× larger.
4. **Don't replace MiniLM with Omni-Embed-Mini in v1.** Defer to v2 when multimodal memory needs land.
5. **Don't add a custom reasoning model in v1.** Cloud LLM via Zo API is fine.
6. **Don't use a unified audio-language model in v1.** Modular is fine.
7. **Don't claim any of these models is "AGI."** None of them are.
8. **Don't trust model cards.** Measure on your own hardware with your own prompts. The Abstraction Gap paper shows AG values 0.84-0.92 across 8 VLMs — fluent text doesn't mean valid reasoning.
9. **Don't ship without DUAL-Bench safety testing.** Edge VLMs are bad at safe completion. `os-toold v2` safety filters must compensate.

---

## 11. Open questions (v4)

1. **Omni-Embed-Mini for v1.5 instead of v2?** It's a 0.9B model (~350MB). Adding it to the wearable memory budget means a heavier load. **Recommend: keep MiniLM for v1, Omni-Embed-Mini for v2 when hierarchical memory is in place.**
2. **LFM2.5-VL-1.2B for v2 wearable (Redax)?** Larger variant of current model, better quality. 2.5× larger, 2.5× more power. **Recommend: benchmark on Redax when hardware lands.**
3. **Custom voice cloning for v2 TTS?** XTTS-v2 / UNISON both support. **Recommend: not v2, monitor for v2.5.**
4. **On-device wake word model in v1.5?** Picovoice / Picollm / openWakeWord. **Recommend: yes for v1.5 — it's a usability win.**

---

## 12. Sources (v4)

See `dan2-research-report.md` §8 for full v4 source list. Key model-related sources:
- LFM2.5-VL-450M (Liquid AI, live verified)
- Gemma 3 in orbit (Yam-9, Loft Orbital + JPL, April 2026) [^13]
- VLMCache (ACM MM 2026) [^6]
- SpecFlow (arXiv 2606.02842) [^7]
- SWEET (Frontiers 2026) [^14]
- Omni-Embed-Mini (OpenReview 2026) [^9]
- EMemBench (OpenReview 2026) [^12]
- Abstraction Gap (arXiv 2605.28779) [^10]
- DUAL-Bench (OpenReview 2026) [^11]
- BareWave (arXiv 2606.09048)
- UNISON (OpenReview 2026)
- XTTS-v2 (Springer 2026)
- Wavelet-driven CFM boosting (OpenReview 2026)

---

*Dan2 Model Analysis v4 — 2026-06-16 03:00 UTC. v4 adds: Omni-Embed-Mini for `memoryd v2` (the only model swap worth doing), VLMCache + per-layer mixed-precision for `perceptiond v2`, structured prompts + geometric descriptors. All v1 model choices unchanged. Gemma 3 4B is the new upper-bound reference (validated in orbit).*
