# Dan2 — Model Selection Deep-Dive (v33)
**Date:** 2026-06-20 06:30 UTC (12:00 IST)
**Status:** v33 — refreshed with June 16-20 landscape changes
**Scope:** Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices for Dan Glasses in 2026?

---

## 0. TL;DR

**Yes for v1 (desktop + camera+voice wearable). No for v2 if we ever target built-in display.** LFM2.5-VL-450M remains the best fit for a camera+voice always-on wearable; whisper.cpp and KittenTTS remain correct. The new 2026 pressure is:

- **Snap Specs** proved display is a real consumer ask — but at 132-136g and $2,195. Dan Glasses should remain camera+voice first, add display later.
- **Apple's memory crisis** makes every byte on the wearable more expensive — both compute memory and storage.
- **Self-improving-agent research** has graduated — SmolVLM-256M in danlab-multimodal is the right *baseline*; the focal model that wraps it should now be larger and better integrated with skill evolution.

---

## 1. Vision — LFM2.5-VL-450M (kept)

**Still correct** because:
- 209MB Q4_0 + 180MB mmproj is small enough for glasses.
- SigLIP2 NaFlex is the right encoder for variable scene geometry.
- Liquid AI's licensing (LFM Open License v1.0, Apache 2.0-equivalent) makes it the sovereign option.
- Brilliant Labs Halo ships with LFM2-VL on-device in July 2026 — external validation.

**Updates worth tracking:**
- **Zamba2-VL-1.2B** — 10x TTFT improvement is real but at ~600MB. Worth benchmarking.
- **AFM 3** — Apple-only, not relevant unless silicon changes.
- **Gemma 3 270M** — text-only, no mmproj in GGUF. Not viable for VLM.
- **SmolVLM-256M** — already deployed as fallback in perceptiond.

**Open question:** does LFM2.5-VL-450M ship a Q5_0 or Q8_0 GGUF? If yes, laptop prototype improves. If no, Q4_0 stays.

**Recommendation:** keep LFM2.5-VL-450M Q4_0 for v1. Spike Zamba2-VL-1.2B for v1.1. Begin measuring power on real wearable silicon.

---

## 2. STT — whisper.cpp + base.en (kept)

**Still correct** because:
- whisper-cpp-plus-rs has async + VAD + real-time streaming.
- base.en (74MB) is the right balance for glasses.
- ggml-tiny (39MB) is the right thermal-fallback model.

**Updates worth tracking:**
- **LFM2-Audio-1.5B** — single audio-language model. If it ships ONNX/GGUF and quality holds, it can collapse audiod + ttsd into one. Worth spiking.
- **Moonshine (Useful Sensors)** — 26MB, <100ms latency. Edge-focused. Worth a wearable spike.
- **Parakeet** — better quality, but Nvidia-only.

**Recommendation:** keep whisper.cpp for v1. Spike LFM2-Audio-1.5B in Month 1. Spike Moonshine for wearable thermal envelope.

---

## 3. TTS — KittenTTS (kept)

**Still correct** because:
- ~25MB total, fits in the .deb without bloating.
- ONNX-friendly, CPU-friendly.
- Voices are sufficient for prompts.

**Updates worth tracking:**
- **LFM2-Audio-1.5B** — same spike as STT. If audio-language works, TTS can be a layer in the same model.
- **Piper TTS** — multi-voice on-prem.
- **F5-TTS** — open weights, higher quality, larger model.

**Hard rule:** no TTS larger than 100MB on the wearable path.

---

## 4. Reasoning — none canonical (add now)

**Gap:** the PRD does not name a reasoning model. The wearable's intelligence layer cannot rely on a cloud model.

**Recommendation:**
- **HRM-Text (1B)** — per the dan-glasses/AGENTS.md canonical reasoning model. Hierarchical reasoning, sub-500M, SOTA on reasoning benchmarks.
- **LFM2.5-1.2B-Thinking** — for the SIA-W+H focal model (1.2B is the right scale per "Harness Updating Is Not Harness Benefit").

**Action:** spike HRM-Text (1B) in perceptiond and openclaw-gateway in Month 1.

---

## 5. Memory embedding — all-MiniLM-L6-v2 (replaced for memoryd v2)

**Not enough for v2.** memoryd v1 is fine for prototype. memoryd v2 needs a richer stack.

**memoryd v2 v1.0 stack:**
- **Mnemosyne** — 98.9% Recall@All@5 on LongMemEval, single SQLite, MIT
- **Mem0** — 4-stage pipeline (Extract / Reflect / Update / Search)
- **Hindsight** — 4-lever (World / Experience / Opinion / Observation)
- **SuperLocalMemory V3.3** — zero-LLM, 7-channel RRF
- **LFM2.5-VL-450M (bbox-prompt JSON output)** — visual memory ingestion
- **Weaviate Engram** — background-write vector store

**Open question:** does BGE-M3 (1024d multilingual) ship a wearable-sized variant? Currently 2.3GB — too large.

---

## 6. Self-improving focal model — SmolVLM-256M (kept for baseline, upgraded for focal)

**danlab-multimodal keeps SmolVLM-256M** as the baseline (cheap, fast, fits the "pre-RL scaffold" framing for public demo).

**For the internal focal model (SIA-W+H path):**
- LFM2.5-1.2B-Thinking (1.2B) — right scale per "Harness Updating Is Not Harness Benefit"
- PopuLoRA populations with TrueSkill cross-eval
- Per-user-isolated weights
- Verifier-gated weight writes

---

## 7. Acceleration techniques to integrate

| Technique | Gain | Where to apply |
|---|---|---|
| **VLMCache** | 1.4-3.8x VLM speedup with <1% accuracy loss | perceptiond |
| **V5e-0 / ViSpec** | 1.89-3.22x self-speculative decoding | perceptiond |
| **MI-Pruner / QViD / SFPruner** | visual token pruning | perceptiond |
| **Speculative decoding (135M draft + 450M target)** | ~2x throughput | perceptiond |
| **Salience CNN** | replaces EMA + Haar cascade | perceptiond |
| **BitNet b1.58** | 9.2x lower energy (text-only) | reasoning layer |
| **Litespark 1.58-bit** | 18.15x speedup on Apple Silicon, 6.03x memory | reasoning layer |
| **Gemma 4 QAT** | 72% VRAM reduction | reasoning layer |

---

## 8. Quantization decision matrix

| Quant | Use case | Tradeoff |
|---|---|---|
| **Q4_0** | Default on wearable (LFM2.5-VL-450M, ggml-tiny) | Best size, acceptable quality |
| **Q4_K_M** | danlab-multimodal (SmolVLM-256M) | Slightly larger, better quality |
| **Q5_0** | Laptop (LFM2.5-VL-450M Q5_0) | AC-powered, better quality |
| **Q8_0** | Server only | Best quality |
| **BitNet b1.58** | Text-only (2B4T, 0.4GB) | Sub-1W, 9.2x lower energy. **No vision yet.** |
| **Gemma 4 QAT** | Sub-1B on edge (26B-A4B in 15GB) | 72% VRAM reduction |
| **Litespark 1.58-bit** | Sub-1B on edge (CPU SIMD) | 18.15x speedup, 6.03x memory |
| **1.58-bit (LFM2-1.5B in development)** | Watch for the 2027 variant | 50-150x combined VLM energy reduction |

---

## 9. Anti-recommendations

1. **Don't replace LFM2.5-VL-450M with a larger VLM on the laptop** unless quality is the blocker. 209MB is small enough to keep.
2. **Don't replace whisper.cpp with a Python-only STT** (e.g., faster-whisper). The C/C++ with Rust bindings is right for real-time audio.
3. **Don't replace KittenTTS with a heavier TTS** (e.g., OpenVoice v2 at 100MB). 25MB is small enough to keep.
4. **Don't deploy BitNet b1.58 as a VLM** — it is text-only.
5. **Don't try BitNet-VLM in 2026** — it does not exist yet. 2027 target.
6. **Don't deploy BitNet on Snapdragon-class silicon** — it will draw 2-5W. Use GAP9 or Hailo-10H for sub-1W.
7. **Don't replace all-MiniLM-L6-v2 with a 7B embedding model in v1** — context is too long, latency too high. Use BGE-small-en-v1.5 or BGE-M3 in v2.
8. **Don't pick the wearable silicon path without measuring it.** $150-500 in dev kits is the single most important investment in Month 1.
9. **Don't ship a display in v1 wearable.** Camera + voice is the right v1. Display is v2+ once power is measured.
10. **Don't compete on raw model quality with Snap / Apple.** Compete on trust architecture.

---

## 10. Open questions

1. Does LFM2-Audio-1.5B ship an ONNX/GGUF export? If yes, it collapses audiod + ttsd.
2. Does LFM2.5-VL-450M ship Q5_0 or Q8_0 GGUF on HF?
3. Does HRM-Text (1B) ship an ONNX/GGUF export?
4. What is the BGE-M3 model size for wearable? 2.3GB is too large.
5. What is the SOTA memory benchmark for personal AI agents in 2026? LongMemEval is the standard, but PersonaMem-v2, LoCoMo, EMemBench, and MemoryArena are all relevant.
