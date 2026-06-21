# Dan2 — Model Selection Deep-Dive
**Date:** 2026-06-14
**Status:** Final v1
**Scope:** Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices for Dan Glasses? What alternatives exist in 2026?

---

## 0. TL;DR

The current model selections are **correct for the laptop prototype**. For the wearable, the dominant variable is **VLM power draw**, and the 2026 sub-1W path is **GAP9 RISC-V + event camera (OpenGlass pattern)** or the 2027 **BitNet-VLM** (text-only BitNet b1.58 is already shipping; VLM variant does not exist yet). The single highest-ROI upgrade is **VLMCache (1.4-3.8× VLM speedup with <1% accuracy loss)**. The single highest-ROI new model evaluation is **LFM2-Audio-1.5B** — if it ships an ONNX/GGUF export, it eliminates the audiod + ttsd stack. **memoryd embedding model needs to be upgraded from all-MiniLM-L6-v2 (384d) to a multi-model stack** in memoryd v2 v1.0 (Sept 2026).

---

## 1. Vision: LFM2.5-VL-450M (current)

### Current spec
- **Model:** LFM2.5-VL-450M Q4_0 (209MB) + mmproj-F16 (180MB)
- **Engine:** llama-mtmd-cli (llama.cpp)
- **Architecture:** lfm2 (Liquid AI 2.5 — 16 layers, 1024 embd, hybrid shortconv+attention)
- **Context:** 32,768 tokens
- **Speed:** sub-250ms CPU inference
- **Input:** 512×512
- **License:** Research/commercial (check Liquid AI license)
- **HuggingFace:** LiquidAI/LFM2.5-VL-450M

### Verdict: **KEEP for laptop prototype.** Right model, right size, right quantization. ⭐⭐⭐⭐

### Why it works
- Smallest working VLM with native GGUF support in llama.cpp
- SigLIP2 NaFlex encoder (not ResNet/ViT — better for edge)
- Sub-250ms latency on CPU
- Liquid AI is a credible 2026 lab (backed by Steve Jobs' son, recent LFM2 release)
- Architecture scales: LFM2.5-base + 400M SigLIP2 NaFlex + efficient projector

### Alternatives (2026)

| Model | Size | Speed | Quality | Verdict |
|---|---|---|---|---|
| **Gemma 4 12B Q4_K_M** | 8GB | Slower on CPU, fast on NPU | **Higher** | **Spike for laptop** (AC-powered). Not for wearable. |
| **Gemma 4 1B** | 1GB | Fast | Lower | **Spike for wearable thermal fallback** (Gemma 4 1B at 42°C throttle). |
| **Qwen2.5-VL-3B / 7B** | 2-5GB | Slower | Higher | **Laptop alternative** if compute allows. |
| **Qwen-VLA** (arXiv 2605.30280) | 7B+ | Slower | SOTA on robotics | **Defer to v3** (generalist robotics, not wearable). |
| **SmolVLM-256M** | 120MB + 182MB mmproj | 26s/image on CPU (slow) | Acceptable for descriptions | **Currently deployed as LFM2.5-VL fallback**. Keep. |
| **Moondream2** | 2.7GB | Slow | Higher | **Legacy. Don't use.** |
| **Gemma 4 26B-A4B (MoE)** | 15GB (QAT) | TBD | SOTA | **Defer. Not for wearable.** |

### Wearable alternatives (sub-1W target)

| Path | Power | Latency | Quality | Status |
|---|---|---|---|---|
| **GAP9 RISC-V + event camera (OpenGlass)** | **Sub-1W** (11.8h on 200mAh) | 78.3ms end-to-end | 83.94% accuracy on gesture recognition | **Reference: arXiv 2606.07431 (June 2026).** |
| **Hailo-10H / Hailo-15 + LFM2.5-VL-450M** | Sub-1.5W sustained at 4 FPS | TBD | TBD | **Measure in Month 1.** |
| **BitNet-VLM** | TBD | TBD | TBD | **Does not exist yet. 2027 target.** |
| **Alif B1 NPU + LFM2-VL-450M** (Brilliant Labs Halo) | <0.5W | TBD | Halo-grade | **Production reference (July 2026 ship).** |

### Recommendation

**Month 1 (July 2026):**
1. **Spike Gemma 4 12B Q4_K_M** in perceptiond (laptop prototype VLM lock — better quality, AC-powered).
2. **Spike Gemma 4 1B** in perceptiond (wearable thermal fallback at 42°C).
3. **Buy Hailo-10H M.2 + RPi 5** dev kit. Measure LFM2.5-VL-450M on Hailo-10H. **Sub-1.5W sustained at 4 FPS = wearable path locked.**
4. **Buy GAP9 dev kit + Prophesee GENX320** event camera. Measure SmolVLM-256M on GAP9. **11.8h on 200mAh = sub-1W validated.**

**Month 2 (August 2026):**
5. **Integrate VLMCache** in perceptiond. **1.4-3.8× speedup with <1% accuracy loss.** Stable background, dynamic foreground. Block-level visual KV-cache.
6. **Integrate V5e-0 / ViSpec-style self-speculative decoding** in perceptiond. **1.89× mean speedup across 15 VLMs.** No vision encoder in drafter.
7. **Spike Salience CNN** in perceptiond salience detector. Replace EMA + Haar cascade. Biggest power lever for the wearable.

**Month 3 (September 2026):**
8. **Replace SmolVLM-256M with LFM2.5-VL-450M** in perceptiond (laptop prototype, when HF GGUF mirror publishes).
9. **Form factor decision tree locked** based on Month 1 measurements.

---

## 2. STT: whisper.cpp + base.en (current)

### Current spec
- **Engine:** whisper.cpp via whisper-cpp-plus-rs (async + VAD)
- **Model:** ggml-base.bin (148MB, default) or ggml-tiny.bin (78MB, recommended on Redax aarch64)
- **VAD:** Silero VAD via ONNX
- **Latency:** 400-700ms end-to-end (ggml-tiny, 2 threads)
- **Languages:** auto-detect or `-l en`

### Verdict: **KEEP.** Correct stack, correct quantization, correct Rust bindings. ⭐⭐⭐⭐

### Why it works
- whisper-cpp-plus-rs has async + VAD (Silero) + real-time PCM streaming
- Mature, production-grade, multiple bindings
- GPU: Vulkan, Metal, CUDA, ROCm all supported
- Quantization: integer quantization, zero-runtime allocations
- Cross-platform: macOS, iOS, Android, Linux, Windows, WebAssembly, Raspberry Pi

### Alternatives (2026)

| Engine | Size | Latency | Quality | Verdict |
|---|---|---|---|---|
| **whisper-tiny.en** (ggml-tiny) | 39MB | 200-500ms | Lower | **Use on Redax aarch64 (smaller, faster).** |
| **whisper-base.en** (ggml-base) | 74MB | 400-700ms | Better | **Default on laptop.** |
| **whisper-small.en** | 244MB | 800-1500ms | Highest | **Laptop only. Not for wearable.** |
| **Parakeet** (Nvidia) | ~250MB | Slower | Higher | **Defer. Nvidia-only path.** |
| **Moonshine** (Useful Sensors) | ~26MB | <100ms | Lower | **Edge-focused. Defer to v2.** |
| **LFM2-Audio-1.5B** (Liquid AI) | TBD | TBD | TBD | **Spike in Month 1. If it ships ONNX/GGUF, eliminates audiod + ttsd stack.** |
| **Streaming whisper (whisper-stream)** | Same as above | 150-300ms | Same as above | **v3 upgrade. Sub-300ms latency.** |

### Wearable alternatives (sub-1W target)

| Path | Power | Latency | Quality | Status |
|---|---|---|---|---|
| **GAP9 + streaming whisper-tiny** | Sub-1W | <300ms | Acceptable | **Measure in Month 1.** |
| **Whisper.cpp + NPU (Hailo-10H)** | Sub-1W | TBD | TBD | **Measure in Month 1.** |
| **OpenGlass audio pipeline** | TBD | TBD | TBD | **OpenGlass focuses on vision, not audio.** |

### Recommendation

**Month 1 (July 2026):**
1. **Spike LFM2-Audio-1.5B** in audiod. If it ships an ONNX/GGUF export and quality holds, **eliminates audiod + ttsd stack** (single audio-language model).
2. **Spike Moonshine** (Useful Sensors) on GAP9. Sub-100ms latency. 26MB. If quality holds, **the wearable STT**.
3. **Spike Parakeet** for laptop (better quality, AC-powered).

**Month 2-3:**
4. **Streaming whisper (whisper-stream)** spike for sub-300ms latency on laptop.
5. **Noise suppression (RNNoise)** before VAD on audiod.
6. **Speaker diarization (pyannote.audio)** for multi-user wearables.

**v1.5 (defer):**
7. **Wake word ("Hey Dan")** — separate `wakewordd` service.
8. **Per-speaker embedding indexing** for memory context.

---

## 3. TTS: KittenTTS (current)

### Current spec
- **Engine:** KittenTTS via ONNX
- **Model:** base (~25MB) — medium (80M params, "KittenTTS medium, 8 expr voices" per dan4.md)
- **Voices:** 8 expr voices
- **Output:** 24kHz WAV via scipy.io.wavfile + aplay
- **Endpoint:** POST /speak (audio/wav bytes), POST /play (runs aplay)

### Verdict: **KEEP for laptop prototype.** Spike LFM2-Audio for wearable. ⭐⭐⭐⭐

### Why it works
- <25MB total — fits in .deb without bloating
- Three variants: default, base, mini (quality: default > base > mini, speed: inverse)
- State-of-the-art quality for size class
- ONNX export available, WASM browser runner exists
- CPU-friendly, designed for edge deployment

### Alternatives (2026)

| Engine | Size | Latency | Quality | Voices | Verdict |
|---|---|---|---|---|---|
| **KittenTTS base** | ~25MB | Fast | Good | 8 expr | **Default on laptop.** |
| **KittenTTS mini** | ~15MB | Faster | Lower | 8 expr | **Wearable primary.** |
| **Piper TTS** | 15-60MB | Fast | Good | 100+ | **Defer. On-prem, multi-voice.** |
| **Coqui XTTS v2** | 1.5GB | Slow | SOTA | Voice cloning | **Defer. Cloud-only.** |
| **OpenVoice v2** | 100MB | Fast | High | Voice cloning | **Defer. Quality is high but model size.** |
| **MOSS-TTS** (Sophon 2026) | TBD | TBD | TBD | TBD | **Defer. Watch.** |
| **Qwen3-TTS** (Sophon 2026) | TBD | TBD | TBD | TBD | **Defer. Watch.** |
| **Fish Audio S2** (Sophon 2026) | TBD | TBD | TBD | TBD | **Defer. Watch.** |
| **LFM2-Audio-1.5B** (Liquid AI) | TBD | TBD | TBD | TBD | **Spike in Month 1. If it ships ONNX/GGUF, eliminates audiod + ttsd stack.** |
| **BareWave** (arXiv 2606.09048, June 2026) | TBD | TBD | TBD | TBD | **Defer. Watch.** |
| **TEMPO** (OpenReview 2026) | TBD | TBD | TBD | TBD | **Defer. Watch.** |

### Wearable alternatives (sub-1W target)

| Path | Power | Latency | Quality | Status |
|---|---|---|---|---|
| **KittenTTS mini on GAP9** | Sub-1W | TBD | Lower | **Measure in Month 1.** |
| **LFM2-Audio-1.5B on GAP9** | Sub-1W | TBD | TBD | **Spike if available.** |
| **Piper TTS on GAP9** | Sub-1W | Fast | Good | **Defer.** |
| **Qwen3-TTS on Hailo-10H** | Sub-1.5W | TBD | TBD | **Defer.** |

### Recommendation

**Month 1 (July 2026):**
1. **Spike LFM2-Audio-1.5B** in ttsd. If it ships ONNX/GGUF, it replaces audiod + ttsd with a single audio-language model.
2. **Spike KittenTTS mini** in ttsd (wearable variant, smaller).
3. **Spike Piper TTS** for multi-voice on-demand.

**v1.5 (defer):**
4. **Streaming TTS** (first-chunk latency <300ms).
5. **Voice cloning** (OpenVoice v2 or Piper voice-mix).

---

## 4. Memory embedding: all-MiniLM-L6-v2 (current)

### Current spec
- **Model:** sentence-transformers/all-MiniLM-L6-v2
- **Dimension:** 384
- **Storage:** BLOB in SQLite
- **Retrieval:** Cosine similarity

### Verdict: **KEEP for memoryd v1 (prototype).** Upgrade to multi-model stack in memoryd v2 v1.0. ⭐⭐⭐

### Why it works (for v1)
- Small, fast, well-documented
- Good baseline for prototype
- 384d fits in SQLite BLOB
- Multilingual? No. (English-only model.)

### Alternatives (2026) for memoryd v2 v1.0

| Model | Dim | Size | Quality | Multilingual | Verdict |
|---|---|---|---|---|---|
| **all-MiniLM-L6-v2** (current) | 384 | 22MB | Baseline | No | **Keep as fallback in v2.** |
| **all-mpnet-base-v2** | 768 | 110MB | Better | No | **Laptop primary.** |
| **BGE-small-en-v1.5** | 384 | 33MB | Better than MiniLM | No | **Laptop primary alternative.** |
| **BGE-M3** | 1024 | 2.3GB | SOTA | **Yes (100+ langs)** | **For multilingual memoryd.** |
| **GTE-Qwen2-7B-instruct** | 4096 | 7GB | SOTA | Yes | **Defer. Too large for v1.** |
| **nomic-embed-text-v1.5** | 768 | 270MB | SOTA | Yes | **Defer.** |
| **E5-mistral-7b-instruct** | 4096 | 7GB | SOTA | Yes | **Defer.** |
| **CLIP ViT-B/32** | 512 | 150MB | SOTA for image-text | Yes | **For visual memory (VisualMem).** |
| **SigLIP2 NaFlex** (LFM2.5-VL-450M internal) | 1024+ | 400MB | SOTA | Multilingual | **Use the vision encoder for memory embeddings (bbox-prompt JSON output).** |

### Memoryd v2 v1.0 (6-core stack, Sept 2026)

**Architecture:** One process, 3 internal modules (ingest / retrieve / consolidate). Multi-model ensemble:

1. **Ingest:** LFM2.5-VL-450M (vision encoder for image+text) + BGE-small-en-v1.5 (text) + CLIP ViT-B/32 (image). 3 models, ~600MB total.
2. **Retrieve:** Hindsight 4-lever (World/Experience/Opinion/Observation) + Tenure's multi-path BM25 + cosine over the 3-model ensemble.
3. **Consolidate:** AEL Thompson Sampling bandit + LLM reflection + DPCM System 2 nighttime engine.

**Storage:**
- SQLite (canonical, durable)
- Vectors in Weaviate Engram (in-process, not external)
- Markdown + JSONL on filesystem (for transparent audit)
- Git-backed memory versioning (Nexus-Memory pattern)

**Target:** >70% LongMemEval, 91.4% with scale (Hindsight reference), 70.4% zero-LLM (SuperLocalMemory V3.3 reference).

### Recommendation

**Month 1 (July 2026):**
1. **Begin memoryd v2 v1.0 design** — 6-core stack, single-process with 3 internal modules.
2. **Spike BGE-small-en-v1.5** as the primary text embedding (replaces MiniLM).
3. **Spike BGE-M3** for multilingual (Indian languages, future-proofing).
4. **Spike LFM2.5-VL-450M** as a vision embedding source (bbox-prompt JSON output → text + visual memory).
5. **Read Mem0 (arXiv 2504.19413), Zep, Hindsight, SuperLocalMemory V3.3 docs.** Fork the best pieces.

**Month 2-3 (Aug-Sept 2026):**
6. **memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public.** 6-core stack. **The bet.**

---

## 5. Reasoning model (new, currently no canonical choice)

### Current state
- The PRD doesn't name a reasoning model.
- OpenClaw uses Anthropic / OpenAI / Gemini / local models via the agent runtime.
- For local-only mode, no canonical model.

### Recommendation: **HRM-Text (1B)** per dan-glasses/AGENTS.md (the dan-consciousness canon) + **LFM2.5-1.2B-Thinking** for SIA-W+H focal model.

### Why
- **HRM-Text** (1B) is the AGENTS.md-canonical reasoning model for Dan Glasses. Hierarchical Reasoning Model. Efficient pretraining beyond scaling. Sub-500M parameters, SOTA on reasoning benchmarks.
- **LFM2.5-1.2B-Thinking** for the SIA-W+H focal model (1.2B is the right scale per SIA paper's "Harness Updating Is Not Harness Benefit" caveat — don't use a 4.6B evolver).
- **Gemma 4 12B Q4_K_M** for laptop (AC-powered, higher quality).
- **Gemma 4 1B** for wearable thermal fallback (sub-1W at low quality).

### Spike in Month 1
- HRM-Text (1B) in perceptiond as the reasoning layer
- LFM2.5-1.2B-Thinking as the SIA-W+H focal model in danlab-multimodal

---

## 6. Audio-language unified (new — emerging 2026 trend)

### Current state
- audiod (STT) + ttsd (TTS) = 2 separate models, 2 services
- 2026 trend: unified audio-language models (LFM2-Audio-1.5B)

### Recommendation: **LFM2-Audio-1.5B** if it ships an ONNX/GGUF export. Eliminates audiod + ttsd stack.

### Why
- Single audio-language model for STT + reasoning + TTS
- Sub-1W target on GAP9 (vs. whisper.cpp + KittenTTS = 2× compute)
- Apache 2.0-equivalent license
- Liquid AI's track record (LFM2, LFM2.5-VL, etc.) is credible

### Spike in Month 1
- LFM2-Audio-1.5B in audiod + ttsd
- If quality holds + ONNX/GGUF export ships, **consolidate audiod + ttsd into one audiolangd service**

### Risk
- If LFM2-Audio-1.5B doesn't ship an ONNX/GGUF export, **carry and use existing audiod + ttsd**

---

## 7. Model selection decision matrix (final)

| Component | Current | Laptop target (Month 1) | Wearable target (Month 1) | Wearable target (Month 4) |
|---|---|---|---|---|
| **Vision** | LFM2.5-VL-450M Q4_0 (fallback: SmolVLM-256M) | Gemma 4 12B Q4_K_M (spike) OR LFM2.5-VL-450M | LFM2.5-VL-450M on Hailo-10H (sub-1.5W) | BitNet-VLM OR GAP9 + event camera (sub-1W) |
| **STT** | whisper.cpp base.en (ggml-base 148MB) | whisper-stream (sub-300ms) | Moonshine 26MB (spike) OR whisper-tiny on GAP9 | Moonshine OR streaming whisper on GAP9 |
| **TTS** | KittenTTS base (~25MB) | KittenTTS default (higher quality) | KittenTTS mini (~15MB) | LFM2-Audio-1.5B OR Piper on GAP9 |
| **Reasoning** | None (no canonical) | HRM-Text (1B) | HRM-Text (1B) | HRM-Text (1B) on GAP9 |
| **Embedding** | all-MiniLM-L6-v2 (384d) | BGE-small-en-v1.5 (384d) OR BGE-M3 (1024d multilingual) | BGE-small-en-v1.5 (384d) on GAP9 | BGE-small-en-v1.5 on GAP9 |
| **Memory (SIA focal)** | N/A | LFM2.5-1.2B-Thinking | HRM-Text (1B) | HRM-Text (1B) on GAP9 |
| **Unified audio-language** | N/A (2 services) | LFM2-Audio-1.5B (spike) | LFM2-Audio-1.5B | LFM2-Audio-1.5B on GAP9 |

---

## 8. Quantization decision matrix

| Quant | Use case | Tradeoff |
|---|---|---|
| **Q4_0** | Default on wearable (LFM2.5-VL-450M, ggml-tiny) | Best size, acceptable quality. |
| **Q4_K_M** | danlab-multimodal (SmolVLM-256M Q4_K_M, 120MB) | Slightly larger, better quality than Q4_0. |
| **Q5_0** | Laptop (LFM2.5-VL-450M Q5_0, ~550MB) | AC-powered, better quality. |
| **Q8_0** | Server (LFM2.5-VL-450M Q8_0, ~900MB) | Best quality, server-only. |
| **BitNet b1.58** | Text-only (2B4T, 0.4GB) | Sub-1W, 9.2× lower energy. No vision yet. |
| **Gemma 4 QAT** | Sub-1B on edge (26B-A4B in 15GB) | 72% VRAM reduction. |
| **Litespark 1.58-bit** | Sub-1B on edge (CPU SIMD) | 18.15× speedup on Apple Silicon, 6.03× memory. |
| **1.58-bit (LFM2-1.5B in development)** | Watch for the 2027 variant | 50-150× combined VLM energy reduction. |

---

## 9. Acceleration techniques to integrate

### VLM (perceptiond)
- **VLMCache (ACM 2026)** — 1.4-3.8× speedup, <1% accuracy loss. **Month 2. Highest ROI.**
- **V5e-0 (OpenReview 2026)** — 1.89× mean speedup, self-speculative. **Month 2.**
- **ViSpec / EAGLE-2** — 3.22× / 3.05-4.26× speedup. **Month 2.**
- **BASTION** — 6.61× speedup, tree-structured block diffusion. **Month 2.**
- **MineDraft** — 75% throughput improvement, batch parallel. **Month 3.**
- **MI-Pruner** — visual token pruning via mutual information. **Month 2.**
- **QViD** — query-aware visual token pruning. **Month 2.**

### LLM (openclaw-gateway)
- **TISA** — 3.8-7.3× indexer speedup, sparse attention. **Month 3.**
- **PRKV** — 6.75× speedup, page-restructured KV cache. **Month 3.**

### Memory (memoryd v2)
- **Tenure multi-path BM25** — sub-15ms retrieval, 89/89 precision. **Month 3.**
- **VisualMem visual memory** — not caption-only. **Month 3.**
- **Hindsight 4-lever consolidation** — 91.4% LongMemEval. **Month 3.**

### Edge (wearable silicon)
- **GAP9 RISC-V + event camera** — sub-1W, 11.8h on 200mAh. **Month 1.**
- **Hailo-10H NPU** — sub-1.5W, 13 TOPS. **Month 1.**
- **BitNet b1.58 + Litespark SIMD** — 18.15× speedup, sub-1W text. **Month 1.**

---

## 10. Anti-recommendations (don't)

1. **Don't replace LFM2.5-VL-450M with a larger VLM on the laptop** unless quality is the blocker. 209MB is small enough to keep.
2. **Don't replace whisper.cpp with a Python-only STT** (e.g., faster-whisper). The C/C++ with Rust bindings is the right choice for real-time audio.
3. **Don't replace KittenTTS with a heavier TTS** (e.g., OpenVoice v2 at 100MB). 25MB is small enough to keep.
4. **Don't deploy BitNet b1.58 as a VLM** — it's text-only.
5. **Don't try BitNet-VLM in 2026** — it doesn't exist yet. 2027 target.
6. **Don't deploy BitNet on Snapdragon-class** — use GAP9 or Hailo-10H for sub-1W. Snapdragon is 2-5W sustained.
7. **Don't replace all-MiniLM-L6-v2 with a 7B embedding model in v1** — context is too long, latency too high. Use BGE-small-en-v1.5 or BGE-M3 in v2.
8. **Don't replace the 6-model memoryd v2 stack with a single model** — each component has a specific job (Mem0 dedup, Zep temporal, Hindsight consolidation, etc.).
9. **Don't use a 4.6B evolver in SIA-W+H** — use a 1.2B focal model per the SIA paper's "Harness Updating Is Not Harness Benefit" caveat.
10. **Don't pick the wearable silicon path without measuring it.** $150-500 in dev kits is the single most important investment in Month 1.

---

## 11. Open questions

1. **Does LFM2-Audio-1.5B ship an ONNX/GGUF export?** If yes, it eliminates audiod + ttsd. If no, carry the 2-service stack.
2. **Does LFM2.5-VL-450M ship a Q5_0 or Q8_0 GGUF on HF?** If yes, upgrade laptop prototype. If no, stick with Q4_0.
3. **Does HRM-Text (1B) ship an ONNX/GGUF export?** If yes, it's the wearable reasoning model. If no, find an alternative.
4. **What is the BGE-M3 model size for wearable?** 2.3GB is too large for GAP9. Need a quantized variant or smaller model.
5. **What is the SOTA memory benchmark for personal AI agents in 2026?** LongMemEval is the standard, but PersonaMem-v2, LoCoMo, EMemBench, and MemoryArena are all relevant. Pick the benchmark that aligns with the use case.

---

## 12. Sources

See `dan2-research-report.md` Section 8 for the full source list. Key new sources specific to models:

- LFM2.5-VL-450M (HuggingFace LiquidAI) [^1]
- BitNet b1.58 (ENERZAi on QCS6490 Hexagon) [^2]
- Litespark (arXiv 2605.06485) [^3]
- VLMCache (ACM 2026) [^4]
- V5e-0 (OpenReview) [^5]
- ViSpec / EAGLE-2 (referenced in BASTION) [^6]
- BASTION (OpenReview) [^7]
- MineDraft (OpenReview) [^8]
- TISA (OpenReview) [^9]
- PRKV (OpenReview) [^10]
- MI-Pruner (OpenReview) [^11]
- QViD (OpenReview) [^12]
- OpenGlass (arXiv 2606.07431) [^13]
- Brilliant Labs Halo [^14]
- Monako Glass [^15]
- Apple Siri AI 12GB gate [^16]
- Apple Glasses N50 [^17]
- Microsoft Scout [^18]
- Microsoft Work IQ [^19]
- Microsoft Project Solara [^20]
- Anthropic Fable 5 / Mythos [^21]
- SIA (arXiv 2605.27276) [^22]
- Harness Updating Is Not Harness Benefit (arXiv 2605.30621) [^23]
- Meta-Harness [^24]
- AEL [^25]
- DPCM [^26]
- LightGMEM [^27]
- SkillOpt [^28]
- SkillsVote [^29]
- CMM [^30]
- SkillCompiler [^31]
- The Living Wiki [^32]
- HERO [^33]
- PAM [^34]
- TRACE [^35]
- Skill Induction for Code Agents [^36]
- Cognitive Memory Manager [^30]
- LFM2-Audio (Liquid AI) — pending public release
- BGE-small-en-v1.5 (BAAI)
- BGE-M3 (BAAI)
- all-MiniLM-L6-v2 (sentence-transformers)
- Moonshine (Useful Sensors)
- whisper-cpp-plus-rs (operator-kit)
- KittenTTS (KittenML)
- Piper TTS (rhasspy)
- Moonshine (Useful Sensors)
- TEMPO (OpenReview 2026)
- Speaker-Reasoner (OpenReview 2026)
- BareWave (arXiv 2606.09048)
- MOSS-TTS (Sophon 2026)
- Qwen3-TTS (Sophon 2026)
- Fish Audio S2 (Sophon 2026)
- Coqui XTTS v2
- OpenVoice v2
- HRM-Text (Sophon 2026)
- SkillVote (Lifecycle Governance) [^29]
- Tenure (arXiv 2605.11325) [^37]
- Hindsight [^38]
- SuperLocalMemory V3.3 [^39]
- Mem0 (arXiv 2504.19413) [^40]
- VisualMem (arXiv 2605.28806) [^41]
- DUAL-Bench (OpenReview 2026) [^42]
- R-APS (arXiv 2606.04823) [^43]

[^1]: https://huggingface.co/LiquidAI/LFM2.5-VL-450M
[^2]: https://www.edge-ai-vision.com/2026/06/running-bitnet-on-qualcomm-hexagon-with-custom-1-58-kernels
[^3]: https://arxiv.org/html/2605.06485v2
[^4]: https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^5]: https://openreview.net/forum?id=GpFgbKW7PR
[^6]: https://openreview.net/forum?id=uqeOxztSIS
[^7]: https://openreview.net/forum?id=uqeOxztSIS
[^8]: https://openreview.net/forum?id=UmTQ21h8HC
[^9]: https://openreview.net/forum?id=6kOo3YtMdu
[^10]: https://openreview.net/forum?id=HbjaTsG8vU
[^11]: https://openreview.net/forum?id=Bc2DZoXBus
[^12]: https://openreview.net/forum?id=UgbjqumIWe
[^13]: https://arxiv.org/abs/2606.07431
[^14]: https://quasa.io/video/brilliant-labs-halo-open-source-ai-glasses-for-curious-minds
[^15]: https://www.timesofai.com/news/monako-glass-custom-linux-computer-glasses/
[^16]: https://www.macrumors.com/2026/05/31/apple-glasses-late-2027-report/
[^17]: https://www.macobserver.com/news/apple-delays-smart-glasses-again-vision-air-still-expected-by-2029/
[^18]: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
[^19]: https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/
[^20]: https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/
[^21]: https://www.linkedin.com/posts/kai-t-williams_this-week-anthropics-internal-think-tank-activity-7468690513249107968-hqua
[^22]: https://arxiv.org/html/2605.27276v2
[^23]: https://huggingface.co/papers/2605.30621
[^24]: https://openreview.net/forum?id=2Tx03Dan7u
[^25]: https://openreview.net/forum?id=dtPo105y8x
[^26]: https://openreview.net/forum?id=ywl53zPXu0
[^27]: https://openreview.net/forum?id=FCQR2oceJ1
[^28]: https://openreview.net/forum?id=2ONrrPIFYi
[^29]: https://openreview.net/forum?id=kj068rI9Uh
[^30]: https://openreview.net/forum?id=yCsHQnvvWY
[^31]: https://openreview.net/forum?id=baOeYyuxty
[^32]: https://openreview.net/forum?id=e64EcfHp8L
[^33]: https://openreview.net/forum?id=CFnfsORP7Y
[^34]: https://openreview.net/forum?id=ptIjkWmtl9
[^35]: https://openreview.net/forum?id=p37UqCmcxG
[^36]: https://openreview.net/forum?id=GmCoFYNEIU
[^37]: https://arxiv.org/html/2605.11325v2
[^38]: https://github.com/vectorize-io/hindsight
[^39]: https://github.com/SuperLocalMemory/SuperLocalMemoryV3
[^40]: https://arxiv.org/abs/2504.19413
[^41]: https://arxiv.org/abs/2605.28806v1
[^42]: https://openreview.net/forum?id=SLaIKf46Dz
[^43]: https://arxiv.org/abs/2606.04823v1
