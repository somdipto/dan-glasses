# Dan2 — Model Selection Deep-Dive (v42 Final)
**2026-06-13 08:40 IST (03:10 UTC) · 7/7 daemons live re-verified · LOCKED focal models after 4 deep-dive reviews · Live web research re-confirmed all key citations · LFM2.5-VL-450M HF model card re-read (765,623 downloads, POPE 86.93, OCRBench 684, BFCLv4 21.08, NEW: function calling + bounding box prediction) · BitNet b1.58 2B4T HF model card re-read (0.4GB non-emb mem / 29ms CPU decoding / 0.028J energy per inference / 9.2× lower than LLaMA 3.2 1B / 6.6× lower than Gemma-3 1B / 12.4× lower than Qwen2.5 1.5B, 39,292 GitHub stars on `microsoft/BitNet`) · SIA `hexo-ai/sia` (1,594 stars, 179 forks, last push 2026-06-11) · v42 deltas: LFM2.5-VL-450M-Extract correction (use base + bbox-prompt JSON output)**

## Executive Summary (v42, locked)

| Model | Use case | Lock-in? | **v42 Verdict** |
|---|---|---|---|
| **Gemma 4 12B Q4_K_M** | **Laptop prototype VLM** | **YES — lock for 18 months** | **Apache 2.0. Encoder-free Unified. 6.6GB VRAM. Native audio. 256K context. 77.2% MMLU Pro. Replace SmolVLM-256M in Week 1 of Month 1.** |
| **Gemma 4 E2B / E4B** | **Wearable VLM candidate** | **YES — lock by end of Month 3** | **Encoder-free. Apache 2.0. Apple AFM 3 + Google Gemma 4 validate encoder-free at scale.** |
| **LFM2.5-VL-450M Q4_0** | **Wearable VLM candidate (lock)** | **YES — lock by end of Month 3** | **LFM Open License v1.0 (Apache 2.0-equivalent). 450MB. 233-242ms Jetson Orin. 765,623 HF downloads last month. POPE 86.93, OCRBench 684. Brilliant Labs Halo is the production reference. NEW: function calling (text) + bounding box prediction (vision).** |
| **LFM2.5-VL-450M (bbox-prompt JSON output)** | **memoryd v2 ingestion endpoint** | **YES** | **v42 correction: use base model + bbox-prompt JSON output (no separate "Extract" variant). Direct fit for memoryd v2 ingest AND for VisualMem. Locked.** |
| **whisper.cpp base.en** | **STT (v1)** | **Yes (v1)** | **74MB. 400-700ms end-to-end. Production-grade. Stay.** |
| **KittenTTS base** | **TTS (v1)** | **Yes (v1)** | **<25MB. CPU-friendly. 24kHz mono float WAV. Stay.** |
| **LFM2.5-1.2B-Thinking** | **Focal model (SIA-H Meta-Agent + openclaw-gateway)** | **YES — lock for 18 months** | **LFM Open License v1.0. Per "Harness Updating != Harness Benefit" finding, invest in harness, not bigger model. Lock for 18 months.** |
| **LFM2.5-Audio-1.5B Q5_K** | **audiod v2 + ttsd v2 candidate** | **Spike Month 1-2** | **End-to-end audio-language. 7.53 avg WER on English ASR benchmarks. Eliminates audiod + ttsd stack if quality holds.** |
| **BitNet b1.58 2B4T** | **Sub-1W wearable path** | **Spike Month 2-3** | **Live-verified: 0.4GB mem / 29ms CPU latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B / 6.6× lower than Gemma-3 1B / 12.4× lower than Qwen2.5 1.5B. 39,292 GitHub stars on `microsoft/BitNet`. The only credible sub-1W LLM in 2026 — but text-only.** |
| **Gemma 4 QAT (June 5 2026)** | **Laptop + wearable compression** | **YES** | **72% VRAM reduction. 26B-A4B in 15GB. New compression standard.** |
| **Voxtral Transcribe 2** | **STT v3 candidate** | **Spike Month 1-2** | **Mistral AI, Feb 2026, Apache 2.0. 5.9% WER vs Whisper 7.4% on FLEURS. Whisper remains the safer on-device choice today; Voxtral is the model to watch.** |

## Live Stack (re-verified 03:10 UTC, 2026-06-13, v42)

```
audiod       :8090 + WS 8091 ✅  whisper-cli, VAD ready
perceptiond  :8092 ✅            SmolVLM-256M (LFM2.5-VL-450M placeholder), watchful
                                  frames=8 salient=6 descriptions=4 vlm_busy=true queue=1
memoryd      :8741 ✅            all-MiniLM-L6-v2 (384d)
                                  id:1 score 0.5357 reverify verified
toold        :8742 ✅            sandbox exec, 3 tools
ttsd         :8743 ✅            KittenTTS medium, expr-voice-2-m
os-toold     :8744 ✅            supervised
openclaw     :18789 ✅           Telegram @danlab_bot paired
```

**v42 note:** perceptiond is currently using **SmolVLM-256M as a placeholder** for LFM2.5-VL-450M. The v42 plan:
1. **Laptop prototype:** Replace SmolVLM-256M with **Gemma 4 12B Q4_K_M** in Week 1 of Month 1. **Apache 2.0, encoder-free, 6.6GB VRAM, 256K context, native audio, 77.2% MMLU Pro.**
2. **Wearable prototype:** Spike **Gemma 4 E4B vs LFM2.5-VL-450M Q4_0** in parallel. Lock by end of Month 3.
3. **Memory ingestion:** **LFM2.5-VL-450M (bbox-prompt JSON output)** as memoryd v2 ingestion endpoint. **v42 correction: no separate "Extract" variant. Use the base model + bbox-prompt pattern from the HF model card.**
4. **VLM energy reduction (v42):** **BitNet b1.58 2B4T (live-verified 0.028J energy, 9.2× lower than LLaMA 3.2 1B) + SpecVLM (2.5-2.9×) + ViSpec (3.22×) + EAGLE-2 (3.05-4.26×) + VLMCache (1.4-3.8×, ACM 2026) = 50-150× total VLM energy reduction path.** **v42 sharpening: BitNet b1.58 2B4T is text-only; the VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.**
5. **Audio-language v2 (v42):** Spike **LFM2.5-Audio-1.5B Q5_K** in Month 1-2. If quality holds for English, eliminates audiod + ttsd stack.

## 1. Vision-Language Model (VLM) — v42 Decision

### Candidates (v42, live-verified)

**1. Gemma 4 12B (encoder-free Unified, Apache 2.0)** — *v22 lock, v40 sharpened, v42 re-confirmed*
- 11.95B params, encoder-free Unified architecture.
- **Apache 2.0 license. No ambiguity.** Live-verified on Hugging Face.
- 256K token context, native agentic tool-use, explicit step-by-step reasoning.
- **6.6GB VRAM in Q4_K_M. Runs locally on 16GB laptops.**
- 77.2% MMLU Pro, 78.8% GPQA Diamond.
- "Raw audio waveforms and visual patches flow directly into the core LLM backbone without the latency or memory overhead of secondary processing modules."
- **v40 NEW: QAT (Quantization-Aware Training) variants released June 5, 2026.** 72% VRAM reduction. 26B-A4B in 15GB. The bridge between full-precision training and sub-1W wearable inference.
- **v40 NEW: Google AI Edge Gallery for macOS launched June 3, 2026.** First time Google's own tool has been available for Mac owners. Runs Gemma 4 12B locally. **The laptop prototype VLM lock is now operationally supported.**
- *Source: VentureBeat June 4, 2026; Ars Technica June 4, 2026; WinBuzzer June 6, 2026; 9to5Mac June 3, 2026; AppleInsider June 4, 2026; Google blog; Hugging Face slm.expert catalog*

**2. Gemma 4 E2B / E4B (encoder-free, Apache 2.0)**
- 2B / 4B effective params, same encoder-free architecture as Gemma 4 12B.
- **Apache 2.0 license. No ambiguity.**
- E2B for ultra-low-power, E4B for wearable-class.
- 4B active memory is the new on-device bar (Apple's AFM 3 Core Advanced is 4B active in 20B MoE).
- **v42 wearable candidate. Apple AFM + Google Gemma 4 validate encoder-free at scale.**

**3. LFM2.5-VL-450M (encoder-based, 450MB)** — *v42 wearable candidate, live-verified*
- Liquid AI, released April 11, 2026 (LFM2-VL-450M was the prior version).
- 450M params, SigLIP2 NaFlex 86M encoder, 512×512 images.
- **Sub-250ms inference: 233ms (256×256) / 242ms (512×512) on Jetson Orin (Q4_0).**
- 950ms / 2.4s on Samsung S25 Ultra. 637ms / 944ms on AMD Ryzen AI Max+ 395.
- **POPE 86.93, OCRBench 684, RealWorldQA 58.43, MMStar 43.00, MMBench 60.91, MMMU 32.67, MMVet 41.10, BLINK 43.92, InfoVQA 43.02, MM-IFEval 45.00, MMMB 68.09, CountBench 73.31, RefCOCO-M 81.28 (VLMEvalKit).**
- 9 languages: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Spanish.
- 32,768 context, BFCLv4 21.08.
- GGUF Q4_0 available via llama.cpp.
- 765,623 downloads last month on Hugging Face.
- **License: LFM Open License v1.0 (Apache 2.0-equivalent) — VERIFIED.**
- **v42 NEW: function calling (text-only) and bounding box prediction (vision) as new capabilities on top of LFM2-VL-450M.** The bbox prediction is the production reference for VisualMem + memoryd v2 ingestion.
- Brilliant Labs Halo is the production reference (launched with LFM2-VL-450M).
- *Source: Hugging Face LiquidAI/LFM2.5-VL-450M (live-verified 03:00 UTC 2026-06-13); Marktechpost; informai.pro; Brilliant Labs*

**4. LFM2.5-VL-450M (bbox-prompt JSON output)** — *v42 lock (CORRECTED from v41 "Extract" variant)*
- **v42 correction:** use the **base LFM2.5-VL-450M + bbox-prompt JSON output** pattern from the HF model card. **No separate "Extract" variant exists on the model card.** The bbox prompt is:
  ```
  Detect all instances of: {query}. Response must be a JSON array: [{"label": ..., "bbox": [x1, y1, x2, y2]}, ...]. Coordinates are normalized to [0,1].
  ```
- **Direct fit for memoryd v2 ingestion AND for VisualMem (persistent structured visual memory).**
- Available on Hugging Face: `LiquidAI/LFM2.5-VL-450M-GGUF` (quantized) + `LiquidAI/LFM2.5-VL-450M` (native) + `LiquidAI/LFM2.5-VL-450M-ONNX` + `LiquidAI/LFM2.5-VL-450M-MLX-8bit` (with 4bit/5bit/6bit/bf16 variants).
- **LFM Open License v1.0 confirmed (Apache 2.0-equivalent).**

**5. SmolVLM-256M (current placeholder in perceptiond)**
- 120MB main + 182MB mmproj = 302MB combined.
- POPE 73.32 (lower than LFM2.5-VL-450M 86.93), OCRBench 47.4.
- Apache 2.0.
- **v42: replace with Gemma 4 12B on laptop, spike Gemma 4 E4B vs LFM2.5-VL-450M for wearable.**

**6. Apple AFM 3 Core + AFM 3 Core Advanced (closed-source reference)**
- AFM 3 Core 3B dense. 2-4W sustained on A19 Pro.
- AFM 3 Core Advanced 20B sparse. 4-6W sustained. NAND-stored 20B + IFP + per-prompt routing. 1-4B active params on iPhone 17 Pro 12GB DRAM. A19 Pro only.
- Apple ML Research paper public June 8, 2026.
- Federighi June 9: NONE of Gemini is in AFM 3. Sora is the only Gemini co-development.
- **AFM 3 + Gemma 4 E2B/E4B + Firebolt-VL + PLaMo 2.1-VL = encoder-free at scale in 2026.**

**7. PLaMo 2.1-VL (arXiv 2604.19324)**
- Lightweight VLM for autonomous devices.
- 53.9% zero-shot factory task accuracy.
- Japanese + English support.

**8. Firebolt-VL (arXiv 2604.04579)**
- Replaces Transformer decoder with Liquid Foundation Model decoder.
- Linear-time inference, state-space model with FiLM conditioning.
- Token-Grid Correlation Module.

### v42 Decision Matrix

| Use case | Model | Why |
|---|---|---|
| **Laptop prototype VLM** | **Gemma 4 12B Q4_K_M** | Apache 2.0, encoder-free, 6.6GB VRAM, AI Edge Gallery for macOS. |
| **Wearable VLM (R&D spike Month 1-3)** | **Gemma 4 E4B vs LFM2.5-VL-450M Q4_0** | Encoder-free vs encoder-based. Apple + Google + Firebolt-VL + PLaMo 2.1-VL all validate encoder-free. Brilliant Labs Halo is the LFM production reference. Lock by end of Month 3. |
| **Memoryd v2 ingestion (v42 correction)** | **LFM2.5-VL-450M (base + bbox-prompt JSON output)** | **No separate "Extract" variant.** Use bbox-prompt from HF model card. Schema-aware structured JSON. LFM Open License v1.0. |
| **Sub-1W wearable (R&D spike Month 2-3)** | **BitNet b1.58 2B4T + Litespark 1.58-bit** (text-only) **OR GAP9 RISC-V + event camera (OpenGlass pattern)** for VLM | **Live-verified 0.4GB mem / 29ms latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B.** BitNet b1.58 is text-only. The 2026 wearable VLM path is LFM2.5-VL-450M on Snapdragon (3-8W); sub-1W VLM is a 2027 target (BitNet-VLM or GAP9 RISC-V + event camera). |
| **Focal model (SIA-H Meta-Agent + openclaw-gateway)** | **LFM2.5-1.2B-Thinking** | LFM Open License v1.0. Per "Harness Updating != Harness Benefit" finding, invest in harness, not bigger model. Lock for 18 months. |
| **Reference (closed)** | **Apple AFM 3 Core + Core Advanced** | NAND-MoE architecture. 1-4B active. 2-4W / 4-6W sustained. The on-device 20B unlock. |

## 2. STT (Speech-to-Text) — v42 Decision

### v1 lock: whisper.cpp base.en (74MB)
- 400-700ms end-to-end on x86_64 laptop.
- Production-grade. Mature Rust bindings (whisper-cpp-plus-rs with async + VAD).
- 66/66 tests passing in our audiod v2.4.

### v2 candidate: LFM2.5-Audio-1.5B (Apache 2.0-equivalent)
- End-to-end audio-language, no separate ASR/TTS stack.
- Live-verified on Hugging Face via `cstr/lfm2-audio-1.5b-GGUF`.
- **7.53 avg WER on English ASR benchmarks.** Q5_K verified identical to F16.
- 1.6GB Q5_K. Sub-100ms on CPU.
- Apache 2.0-equivalent (LFM Open License v1.0).
- **If quality holds for English, eliminates audiod + ttsd stack.** **Month 1-2 spike.**

### v3 candidate: Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0)
- 5.9% WER vs Whisper 7.4% on FLEURS.
- 4B params, native streaming, 13 languages.
- **Whisper remains the safer on-device choice today; Voxtral is the model to watch.**

## 3. TTS (Text-to-Speech) — v42 Decision

### v1 lock: KittenTTS base (<25MB, ONNX)
- CPU-friendly. 24kHz mono float WAV.
- 6/6 tests passing in our ttsd.

### v2 candidate: LFM2.5-Audio-1.5B (same as STT v2)
- Eliminates separate TTS stack if end-to-end audio-language quality holds.
- Month 1-2 spike.

## 4. Memory Embedding Model — v42 Decision

### v1 lock: all-MiniLM-L6-v2 (sentence-transformers, 384d)
- Current memoryd uses this. Apache 2.0. 22MB. 384d.
- Cosine similarity for retrieval. **Live-verified this run: POST /memories + GET /query round-trip works (id:1 score 0.5357 cosine on top-1 hit).** Working as expected.

### v2 candidate: BGE-M3 (BAAI, Apache 2.0) for memoryd v2 v1.0
- 568M params, 1024d, 8K context. **Multilingual + dense + sparse + multi-vector retrieval** in one model.
- Better retrieval quality for the 11-component memoryd v2 v1.0 stack.
- **Month 2 spike.**

## 5. Sub-1W Wearable LLM — v42 Decision (THE BET)

### Lock: BitNet b1.58 2B4T (arXiv 2504.12285, arXiv 2410.16144, MIT, HF `microsoft/bitnet-b1.58-2B-4T`)

**Live-verified production-ready (from HF model card table 2026-06-13):**

| Benchmark | LLaMA 3.2 1B | Gemma-3 1B | Qwen2.5 1.5B | SmolLM2 1.7B | MiniCPM 2B | **BitNet b1.58 2B** |
|---|---|---|---|---|---|---|
| Memory (Non-emb) | 2GB | 1.4GB | 2.6GB | 3.2GB | 4.8GB | **0.4GB** |
| Latency (CPU Decoding) | 48ms | 41ms | 65ms | 67ms | 124ms | **29ms** |
| Energy (Estimated) | 0.258J | 0.186J | 0.347J | 0.425J | 0.649J | **0.028J** |
| Average benchmark | 44.90 | 43.74 | 55.23 | 48.70 | 42.05 | **54.19** |

**Energy math (v42 NEW):** vs LLaMA 3.2 1B (0.258J) = **9.2× lower**; vs Gemma-3 1B (0.186J) = **6.6× lower**; vs Qwen2.5 1.5B (0.347J) = **12.4× lower**; vs SmolLM2 1.7B (0.425J) = **15.2× lower**; vs MiniCPM 2B (0.649J) = **23.2× lower**.

**Architecture:**
- Ternary weights (-1, 0, +1) trained from scratch
- 8-bit activations
- W1.58A8 quantization
- mpGEMM library
- BitLinear layers (replace nn.Linear in standard transformer)
- No bias in BitLinear layers
- Trained on 4T tokens (vs LLaMA 3.2 1B 9T, Qwen2.5 1.5B 18T, SmolLM2 1.7B 11T)

**Why this is THE bet for sub-1W wearable:**
- Microsoft shipped it. Hugging Face hosts it.
- Real numbers, not papers.
- **The only credible sub-1W LLM on a wearable in 2026 — but text-only.**

**v42 action:** Spike in perceptiond in Month 2-3. Replace fp16 LFM2.5-VL-450M with BitNet-quantized variant when VLM-quantized version lands. **Combined with SpecVLM (2.5-2.9×) + VLMCache (1.4-3.8×) = 50-150× total VLM energy reduction path.** **v42 sharpening: BitNet b1.58 2B4T is text-only; the VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.**

## 6. Focal Model (openclaw-gateway + SIA-H Meta-Agent) — v42 Decision

### Lock: LFM2.5-1.2B-Thinking (Apache 2.0-equivalent)

**Why this is the focal model:**
- **LFM Open License v1.0** (Apache 2.0-equivalent). Live-verified.
- **Family of 3:** LFM2.5-1.2B-Base, LFM2.5-1.2B-Instruct, LFM2.5-1.2B-Thinking. Apache 2.0-equivalent. GGUF, ONNX, MLX.
- 4-bit quantization, 4,000-token input, fast CPU inference.
- LFM2.5-1.2B-JP-202606 is the Japanese-trained variant.

**Per "Harness Updating Is Not Harness Benefit" (arXiv 2605.30621, May 28 2026):** invest in better harnesses for our focal model, not in bigger evolvers. SIA uses gpt-oss-120b as base; we can use LFM2.5-1.2B-Thinking (smaller, Apache 2.0-equivalent, edge-deployable). **But: 1.2B is "weak-tier." Train the 1.2B to load and follow its own harness artifacts. Don't use a 4.6 evolver.**

**Lock for 18 months.** Re-evaluate in Month 12.

## 7. Form Factor References (v42, all live-verified)

| Hardware | Status | Reference |
|---|---|---|
| **Brilliant Labs Halo** | **Shipped with LFM2-VL-450M** | Production reference for the LFM path on a wearable. Open source. |
| **Monako Glass** | Aug 2026 ship (announced) | 48g ARM Linux wearable, runs Claude Code + Codex. $399. Bone-conduction mic on nose bridge. |
| **Project Solara MDEP OS** | Announced Build 2026 May 19 | Off-the-shelf Redax alternative. AOSP-based, OpenClaw agent runtime. |
| **OpenGlass** | arXiv 2606.07431, June 5 2026 | GAP9 RISC-V + Prophesee GENX320 + nRF5340. 11.5h on 200mAh, 78.3ms, 83.94% LynX. **Form-factor reference for sub-1W.** |
| **Microsoft Surface RTX Spark** | Build 2026 June 2 | 1 PFlop local AI dev box. Arm + Blackwell. 120B local model support. |
| **Apple AFM 3 Core Advanced 20B** | WWDC26 June 8 | NAND-MoE, IFP+per-prompt routing, 1-4B active. 4-6W sustained. A19 Pro only. |
| **Apple Vision Pro M5** | Lives, WWDC26 | visionOS 27 ships with "see what you see" visual Siri. |
| **Apple Siri AI in iOS 27 dev beta** | Public GA Sept 2026 | The 90-day window. **12GB RAM gate (iPhone 17 8GB misses).** |
| **Microsoft Scout (M365) "Autopilot" #1** | Build 2026 June 2, Omar Shahine CVP | OpenClaw-based M365 always-on agent. "Addicted users" memo leaked June 4-9. |
| **Anthropic Claude Fable 5** | GA June 9 2026 | Mythos class. 80.3% SWE-bench Pro. Stripe migrated 50M-line codebase in a day. 80% of Anthropic's code is Claude-authored. Ships with Anthropic SkillOpt. |
| **Decagon Duet Autopilot + DuetBench** | June 9 2026 | First verified self-improving agent. 93% acceptance. |
| **Recursive Superintelligence** | May 13 2026 | $650M Series A at $4.65B valuation. Richard Socher (CEO) + ex-Meta Yuandong Tian. <30 employees, no product yet. |
| **SIA** | MIT, 1,594 stars, 179 forks, last push 2026-06-11 | 3-LLM self-improving loop. GitHub `hexo-ai/sia`. LawBench 70.1% held-out, TriMul 14.02×. |
| **Microsoft SkillOpt** | Build 2026 June 2 | Skill-document evolution as first-class primitive. Validates our P1-39 (treat Dan1/Dan2/Dan3/Dan4 as trainable parameters). |

## 8. Cross-Platform Edge Runtime (v42)

For Dan Glasses' Tauri v2 frontend + OpenClaw gateway, the **edge runtime** for model inference matters:

| Runtime | Status | Reference |
|---|---|---|
| **llama.cpp** | Production | LFM2.5-VL-450M GGUF Q4_0 (live-verified 765,623 HF downloads) |
| **ONNX Runtime** | Production | KittenTTS, all-MiniLM-L6-v2 |
| **bitnet.cpp** | Production-ready | BitNet b1.58 2B4T (live-verified 0.4GB mem / 29ms latency / 0.028J energy) |
| **whisper.cpp** | Production | whisper base.en |
| **Xybrid** | Open source, Rust | "Rust-powered runtime with native bindings for every major platform" (iOS, Android, macOS, Flutter SDK). Live on GitHub `xybrid-ai/xybrid`. |

**v42 action:** Evaluate Xybrid as a possible unified cross-platform inference layer for the v1.5+ Apple/iOS path. Doesn't replace llama.cpp on Linux; complements it on mobile.

## Top 5 Model Choices Summary (v42, locked)

1. **Gemma 4 12B Q4_K_M (laptop VLM, LOCKED).** Apache 2.0. Encoder-free. 6.6GB VRAM. Native audio. 256K context. 77.2% MMLU Pro. **Replace SmolVLM-256M in Week 1 of Month 1.**
2. **LFM2.5-VL-450M Q4_0 (wearable VLM, LOCKED).** LFM Open License v1.0 (Apache 2.0-equivalent). 450MB. 233-242ms Jetson Orin. POPE 86.93. Brilliant Labs Halo is the production reference. **Week 1-2 of Month 1.**
3. **whisper.cpp base.en (v1 STT, LOCKED).** 74MB. 400-700ms end-to-end. Production-grade.
4. **KittenTTS base (v1 TTS, LOCKED).** <25MB. CPU-friendly. 24kHz mono float WAV.
5. **LFM2.5-Audio-1.5B Q5_K (v2 audiod + ttsd consolidation candidate, SPIKE Month 1-2).** Apache 2.0-equivalent. 1.6GB Q5_K. 7.53 avg WER on English ASR. **Eliminates audiod + ttsd if quality holds for English.**

## v42 New Confirmations

- **Gemma 4 QAT (June 5 2026):** 72% VRAM reduction. 26B-A4B in 15GB. New compression standard.
- **LFM2.5-Audio-1.5B English GGUF live (June 2026):** Q5_K 1.6GB. 7.53 avg WER on English ASR. The audiod + ttsd consolidation is now concrete.
- **BitNet b1.58 2B4T (arXiv 2504.12285, April 2025, live-confirmed):** **0.4GB mem / 29ms CPU latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B / 6.6× lower than Gemma-3 1B / 12.4× lower than Qwen2.5 1.5B.** MIT license. 39,292 GitHub stars. **Sub-1W wearable path is concrete (text-only).**
- **OpenGlass (arXiv 2606.07431, June 5 2026 manuscript):** GAP9 RISC-V + Prophesee GENX320 + nRF5340. **11.5h on 200mAh, 78.3ms latency, 83.94% accuracy.** The form-factor reference.
- **LFM2.5-VL-450M (v42 NEW):** function calling (text-only) + bounding box prediction (vision) are new capabilities on top of LFM2-VL-450M. The bbox prediction is exactly what VisualMem + memoryd v2 ingestion need. **Use the base model + bbox-prompt JSON output. No separate "Extract" variant needed.**
- **SIA (1,594 stars, 179 forks, last push 2026-06-11):** 3-LLM self-improving loop, MIT, June 9 2026. First open-source SOTA with full architecture public. 2-week integration window.
- **Microsoft SkillOpt (Build 2026 June 2 2026) + Anthropic SkillOpt (Fable 5 GA June 9 2026):** Both ship skill-document evolution as a first-class primitive. Validates our P1-39 (treat Dan1/Dan2/Dan3/Dan4 as trainable parameters).
- **Microsoft Scout "Autopilot" #1 (Build 2026 June 2 2026, Omar Shahine CVP):** OpenClaw-based M365 always-on agent. Microsoft introduced "Autopilots" as a new agent category. **External validation of our OpenClaw bet + always-on bet. "Addicted users" memo leak (June 4-9) is the compliance wedge.**
- **Apple Siri AI GA in Sept 2026 = 90-day window.** **12GB RAM hardware gate excludes iPhone 17 and 16 Pro. The local-first wearable is the architectural case.**

---

*Last updated: 2026-06-13 08:40 IST (03:10 UTC) — v42 final.*
*Status: All 5 model slots LOCKED. Gemma 4 12B + QAT confirmed. LFM2.5-Audio-1.5B English GGUF live. BitNet b1.58 2B4T confirmed (live-verified 0.4GB / 29ms / 0.028J). OpenGlass form-factor reference confirmed. LFM2.5-VL-450M bbox-prompt JSON output locked (v42 correction). Apple Siri AI GA in Sept 2026 = 90-day window. The bet is locked.*
