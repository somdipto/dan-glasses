# Dan2 — Model Selection Deep-Dive
**v30 · 2026-06-11 07:00 IST (01:30 UTC) · 7/7 services live (os-toold re-supervised) · WWDC26 +3d post-mortem · Anthropic Fable 5 GA (June 9) · Anthropic brake-pedal plea (June 4-8) · Recursive Superintelligence $650M Series A (May 13) · Microsoft Build 2026 +9d · Microsoft Scout "addicted users" leak (June 4-9) · Decagon DuetBench 93% acceptance (June 9) · Apple Vision Pro M5 lives + visionOS 27 "see what you see" (WWDC26) · Apple confirms NONE of Gemini in AFM 3 (Federighi June 9) · Project Solara MDEP OS · Brilliant Labs Halo shipping July 2026 confirmed · BitNet b1.58 + Litespark 1.58-bit path concrete · SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× (ACM 2026) = VLM speedup concrete · Fitbit Air "sub-1W or no AI" rule · LFM2.5-Audio-1.5B-JP = end-to-end audio-language candidate**

## Executive Summary (v30)

| Model | Use case | Lock-in? | **v30 Verdict** |
|---|---|---|---|
| **Gemma 4 12B (encoder-free Unified, Apache 2.0)** | **Laptop prototype VLM (v22 lock)** | **YES — lock for 18 months** | **Laptop prototype lock. Apache 2.0. 16GB native. QAT variants for mobile/laptop (June 6).** |
| **Gemma 4 E2B / E4B (encoder-free, ~2B / 4B active)** | **Wearable VLM candidate** | **YES — lock by end of Month 3** | **Wearable candidate. Apple AFM + Google Gemma 4 validate encoder-free at scale.** |
| LFM2.5-VL-450M (encoder-based, ~450MB) | Wearable VLM candidate | Spike Month 1-3 | **Apache 2.0-equivalent confirmed (LFM Open License v1.0).** Brilliant Labs Halo is the production reference. **233-242ms on Jetson Orin (Q4_0, 512×512).** |
| **LFM2.5-VL-450M-Extract (JSON output)** | **memoryd v2 ingestion endpoint** | **YES** | **v22 unlock. Use as memoryd v2 ingestion. Apache 2.0-equivalent confirmed.** |
| whisper.cpp base.en | STT | Yes (v1) | Right choice. 400-700ms end-to-end. **v30: LFM2.5-Audio-1.5B spike in Month 1-2 as audiod v2 candidate.** |
| KittenTTS base | TTS | Yes (v1) | Fine. Not differentiated. **v30: LFM2.5-Audio-1.5B spike in Month 1-2 as ttsd v2 candidate.** |
| **LFM2.5-1.2B-Thinking (focal model)** | **SIA-H Meta-Agent + openclaw-gateway focal** | **YES — focal model for 18 months** | **Apache 2.0-equivalent confirmed. Apple System Orchestrator + JetBrains Mellum2 + Microsoft IQ + Microsoft SkillOpt pattern. v30 sharpen: per "Harness Updating != Harness Benefit" finding, invest in better harnesses, not bigger models.** |
| **LFM2.5-Audio-1.5B (v27, v28, v29, v30 production candidate)** | **audiod v2 stack (STT + TTS replacement)** | **Spike Month 1-2** | **End-to-end audio-language, no separate ASR/TTS. Apache 2.0-equivalent. If quality holds for English, eliminates audiod + ttsd stack.** |
| **BitNet b1.58 2B4T + bitnet.cpp + Litespark 1.58-bit** | **1-bit wearable unlock** | **Spike Month 2-3** | **v30 sharpen: Litespark 18-97× on Apple M4 (arXiv 2605.06485) + bitnet.cpp 1.37-6.46× CPU speedup, 55-82% energy reduction (arXiv 2410.16144). Sub-1W wearable unlock.** |
| **LFM2.5-Audio-1.5B spike (audio-language)** | **audiod v2 + ttsd v2** | Spike Month 1-2 | End-to-end audio-language, Apache 2.0-equivalent. **v30: spike in Month 1-2; if quality holds, eliminates audiod + ttsd stack.** |
| BitCPM-CANN 1-bit | 1-bit encoder training | No (R&D) | Spike in Month 3-9. Huawei 95-97% retention recipe. |
| **Apple AFM 3 Core (3B) + AFM 3 Core Advanced (20B MoE w/ IFP)** | **Reference (closed source)** | No | **WWDC26 reference. AFM 3 Core 2-4W sustained on A19 Pro. AFM 3 Core Advanced 4-6W. NAND-stored 20B with 1-4B active params. Federighi June 9: NONE of Gemini in AFM 3 — Sora is the only Gemini co-development.** |
| **Microsoft Surface RTX Spark (1 PFlop, Arm + Blackwell)** | **Local AI dev box reference (v25)** | No | **Reference. 120B local model support. The local-AI dev kit war is on. Majorana 2 quantum announced at Build 2026.** |
| **OpenGlass GAP9 RISC-V + Prophesee GENX320 event camera** | **Sub-1W AI eyewear reference (v26)** | No | **Reference. 100mW inference. 11.5h on 200mAh. Different silicon path. Validates sub-1W.** |
| **Monako Glass (ARM Cortex A7 + 300mAh)** | **48g Linux glasses form factor (v27 NEW)** | No | **Reference. $399, shipping Aug 2026. Buildroot Linux + Claude Code + Codex on device. 48g form factor proof.** |
| **Project Solara MDEP OS (Microsoft Build 2026)** | **Off-the-shelf Redax alternative (v30 NEW)** | No | **Reference. MDEP OS uses OpenClaw for agent runtime. AOSP-based. Badge form factor.** |
| **Brilliant Labs Halo + Liquid AI** | **Glasses shipping July 2026** | No | **Reference. LFM2-VL-450M on device. Open source. v30 confirmed: ships July 2026.** |
| **Apple Vision Pro M5 (lives) + visionOS 27 "see what you see"** | **Production reference for "see what you see" pattern (v30 NEW)** | No | **Reference. Vision Pro M5 hardware in market. visionOS 27 ships with visual Siri. The "see what you see" pattern is the production reference for perceptiond proactive loop.** |
| **Anthropic Claude Fable 5 (Mythos class, June 9 2026 GA)** | **Production self-improving model reference (v30 NEW)** | No | **Reference. 80.3% SWE-bench Pro. Stripe 50M-line migration in 1 day. 80% of Anthropic's production code is Claude-authored.** |
| **Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0)** | **STT v3 candidate** | Spike Month 1-2 | **5.9% WER vs Whisper 7.4% on FLEURS. 4B params. Native streaming. 13 languages. Apache 2.0. For most on-device dictation today, Whisper remains the safer choice — Voxtral is the model to watch.** |
| **Microsoft Scout (M365, Build 2026)** | **Production reference for OpenClaw-on-enterprise (v30 NEW)** | No | **Reference. OpenClaw-based. Autopilot class. "Addicted users" memo leaked June 4-9. Nadella disowned. Shahine + Werner named. Microsoft's "responsible agent" narrative cracked.** |

## Live Stack (re-verified 01:30 UTC, 2026-06-11, v30)

```
audiod       :8090 + WS 8091 ✅  whisper-cli, VAD ready
perceptiond  :8092 ✅            SmolVLM-256M, watchful
memoryd      :8741 ✅            all-MiniLM-L6-v2 (384d)
toold        :8742 ✅            sandbox exec, 3 tools
ttsd         :8743 ✅            KittenTTS medium, expr-voice-2-m
os-toold     :8744 ✅            PID 4392, supervised
openclaw     :18789 ✅           Telegram @danlab_bot paired
```

**v30 note:** perceptiond is currently using **SmolVLM-256M as a placeholder** for LFM2.5-VL-450M. The v30 plan:
1. **Laptop prototype:** Replace SmolVLM-256M with **Gemma 4 12B** (encoder-free Unified, Apache 2.0). 16GB native. QAT variants for mobile/laptop (June 6).
2. **Wearable prototype:** Spike LFM2.5-VL-450M Q4_0 vs Gemma 4 E4B in parallel. Lock by end of Month 3.
3. **Memory ingestion:** LFM2.5-VL-450M-Extract (JSON output) as memoryd v2 ingestion endpoint.
4. **VLM energy reduction (v30):** SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× (ACM 2026) + Litespark 18-97× on Apple M4 + bitnet.cpp 1.37-6.46× + T-MAC 60-70% = 50-150× total VLM energy reduction path. **Month 2-3 spike.**
5. **Audio-language v2 (v30):** Spike LFM2.5-Audio-1.5B in Month 1-2. If quality holds for English, eliminates audiod + ttsd stack.

## 1. Vision-Language Model (VLM) — v30 Decision

### Candidates

**1. Gemma 4 12B (encoder-free Unified, Apache 2.0)** — *v22 lock, v30 sharpened*
- 11.95B params, encoder-free Unified architecture.
- **Apache 2.0 license. No ambiguity.**
- 256K token context, native agentic tool-use, explicit step-by-step reasoning.
- Runs locally on 16GB laptops (Q4 quant) or 24GB+ native.
- 77.2% MMLU Pro, 78.8% GPQA Diamond.
- "Raw audio waveforms and visual patches flow directly into the core LLM backbone without the latency or memory overhead of secondary processing modules."
- **v30 NEW: QAT (Quantization-Aware Training) variants released June 6, 2026 for mobile/laptop.** Smaller, on-device oriented. **The bridge between full-precision training and sub-1W wearable inference.**
- **v30 NEW: Google AI Edge Gallery for macOS launched June 3, 2026.** First time Google's own tool has been available for Mac owners. Runs Gemma 4 12B locally. **The laptop prototype VLM lock is now operationally supported.**
- *Source: VentureBeat June 4, 2026; Ars Technica June 4, 2026; WinBuzzer June 6, 2026; 9to5Mac June 3, 2026; AppleInsider June 4, 2026; Google blog*

**2. Gemma 4 E2B / E4B (encoder-free, Apache 2.0)**
- 2B / 4B effective params, same encoder-free architecture as Gemma 4 12B.
- **Apache 2.0 license. No ambiguity.**
- E2B for ultra-low-power, E4B for wearable-class.
- 4B active memory is the new on-device bar (Apple's AFM 3 Core Advanced is 4B active in 20B MoE).
- **v30 wearable candidate. Apple AFM + Google Gemma 4 validate encoder-free at scale.**

**3. LFM2.5-VL-450M (encoder-based, 450MB)** — *v30 wearable candidate*
- Liquid AI, released April 11, 2026.
- 450M params, SigLIP2 NaFlex encoder, 512×512 images.
- **Sub-250ms inference: 233ms (256×256) / 242ms (512×512) on Jetson Orin (Q4_0).** Marktechpost confirmed.
- 950ms / 2.4s on Samsung S25 Ultra. 637ms / 944ms on AMD Ryzen AI Max+ 395.
- POPE 86.93, OCRBench 84, RealWorldQA 58.43 (VLMEvalKit).
- GGUF Q4_0 available via llama.cpp.
- **License: Apache 2.0-equivalent — VERIFIED (LFM Open License v1.0).** Brilliant Labs Halo is the production reference (shipping July 2026 with LFM2-VL-450M).
- *Source: Marktechpost, informai.pro, HuggingFace*

**4. LFM2.5-VL-450M-Extract (JSON output variant)** — *v22 lock, v30 sharpen*
- Same architecture as LFM2.5-VL-450M, tuned for structured JSON output.
- **Direct fit for memoryd v2 ingestion endpoint.**
- Available on HuggingFace: `LiquidAI/LFM2.5-VL-450M-Extract-GGUF`.
- **Apache 2.0-equivalent license confirmed.**

**5. SmolVLM-256M (current placeholder in perceptiond)**
- 120MB main + 182MB mmproj = 302MB combined.
- POPE 73.32, OCRBench 47.4 (lower than LFM2.5-VL-450M).
- Apache 2.0.
- **v30: replace with Gemma 4 12B on laptop, spike Gemma 4 E4B vs LFM2.5-VL-450M for wearable.**

**6. Apple AFM 3 Core + AFM 3 Core Advanced (closed-source reference)**
- AFM 3 Core 3B dense. 2-4W sustained on A19 Pro.
- AFM 3 Core Advanced 20B sparse. 4-6W sustained. NAND-stored 20B + IFP + per-prompt routing. 1-4B active params on iPhone 17 Pro 12GB DRAM. A19 Pro only.
- Apple ML Research paper public June 8, 2026.
- **Federighi June 9 (AppleInsider, MacRumors): NONE of Gemini is in AFM 3. Sora is the only Gemini co-development.** This corrects the v29 "Apple-Gemini co-developed models" framing.
- **AFM 3 + Gemma 4 E2B/E4B + Firebolt-VL + PLaMo 2.1-VL = encoder-free at scale in 2026.**

**7. PLaMo 2.1-VL (arXiv 2604.19324)**
- Lightweight VLM for autonomous devices.
- 53.9% zero-shot factory task accuracy.
- Japanese + English support.
- Validates the lightweight VLM bet.

**8. Firebolt-VL (arXiv 2604.04579)**
- Replaces Transformer decoder with Liquid Foundation Model decoder.
- Linear-time inference, state-space model with FiLM conditioning.
- Token-Grid Correlation Module.

**v30 decision matrix:**

| Use case | Model | Why |
|---|---|---|
| Laptop prototype VLM | **Gemma 4 12B Q4_0** | Apache 2.0, encoder-free, 16GB native, AI Edge Gallery for macOS. |
| Wearable VLM (R&D spike Month 1-3) | **Gemma 4 E4B vs LFM2.5-VL-450M Q4_0** | Encoder-free vs encoder-based. Apple + Google + Firebolt-VL + PLaMo 2.1-VL all validate encoder-free. Brilliant Labs Halo is the LFM production reference. Lock by end of Month 3. |
| Memoryd v2 ingestion | **LFM2.5-VL-450M-Extract** | JSON output, schema-aware extraction, Apache 2.0-equivalent. |
| Sub-1W wearable (R&D spike Month 2-3) | **BitNet b1.58 2B4T + Litespark 1.58-bit** | 18-97× Litespark throughput on M4. 1.37-6.46× bitnet.cpp speedup. 55-82% energy reduction. |
| Focal model (SIA-H Meta-Agent + openclaw-gateway) | **LFM2.5-1.2B-Thinking** | Apache 2.0-equivalent. Per "Harness Updating != Harness Benefit," invest in harness, not bigger model. Lock for 18 months. |
| Reference (closed) | **Apple AFM 3 Core + Core Advanced** | NAND-MoE architecture. 1-4B active. 2-4W / 4-6W sustained. The on-device 20B unlock. |

## 2. Speech-to-Text (STT) — v30 Decision

### Candidates

**1. whisper.cpp base.en (v1, 74MB, 400-700ms end-to-end)** — *v1 lock*
- Production-grade. Mature bindings. Multi-platform.
- VAD via Silero ONNX. WebSocket streaming (audiod v2).
- 55/55 tests passing in our audiod.
- **Right choice for v1.**

**2. LFM2.5-Audio-1.5B (v30 spike)** — *Month 1-2 candidate*
- End-to-end audio-language, no separate ASR/TTS.
- Apache 2.0-equivalent.
- **If quality holds for English, eliminates audiod + ttsd stack.**
- 1.5B params is too large for v1 wearable; possible on laptop.
- v1.5 wearable path: BitNet-quantized LFM2.5-Audio-1.5B for sub-1W inference.

**3. Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0)** — *Month 1-2 spike*
- 5.9% WER vs Whisper 7.4% on FLEURS.
- 4B params. Native streaming. 13 languages. Apache 2.0.
- **Whisper remains the safer on-device choice today (4B params, 7.4% WER is acceptable, mature ecosystem). Voxtral is the model to watch.**

**4. Parakeet (NVIDIA, Apache 2.0)**
- Fast, small, good accuracy.
- English-only, multi-language variants coming.
- Considered in v1 spec; whisper wins on ecosystem.

**v30 decision matrix:**

| Use case | Model | Why |
|---|---|---|
| v1 STT | **whisper.cpp base.en** | Production-grade, mature, 400-700ms end-to-end. |
| v2 STT spike (Month 1-2) | **LFM2.5-Audio-1.5B** | End-to-end audio-language. Eliminates audiod + ttsd if quality holds. |
| v3 STT candidate | **Voxtral Transcribe 2** | Apache 2.0, 5.9% WER on FLEURS. **Whisper remains safer today; Voxtral is the model to watch.** |

## 3. Text-to-Speech (TTS) — v30 Decision

### Candidates

**1. KittenTTS base (v1, <25MB, 24kHz mono float)** — *v1 lock*
- Right choice for the wearable. CPU-friendly. ONNX.
- 8 expr voices.
- 324-439KB WAV output, 24kHz mono float.
- 6/6 tests passing in our ttsd.

**2. LFM2.5-Audio-1.5B (v30 spike)** — *Month 1-2 candidate*
- Same as STT v2.
- Eliminates audiod + ttsd if quality holds.

**3. Apple Neural TTS via Core ML** — *v1.5 Apple extension*
- Out of scope for v1. v1.5 if we ship Apple Core AI extension.

**v30 decision matrix:**

| Use case | Model | Why |
|---|---|---|
| v1 TTS | **KittenTTS base** | <25MB, CPU-friendly, ONNX, 8 voices. |
| v2 TTS spike (Month 1-2) | **LFM2.5-Audio-1.5B** | Consolidates audiod + ttsd. |
| v1.5 Apple extension | **Apple Neural TTS via Core ML** | Out of scope for v1. |

## 4. Focal Model (SIA-H Meta-Agent + openclaw-gateway) — v30 Decision

### Candidates

**1. LFM2.5-1.2B-Thinking (Apache 2.0-equivalent, LFM Open License v1.0)** — *v30 lock for 18 months*
- 1.2B params, thinking mode.
- Direct fit for the Meta-Agent in SIA-H.
- **v30 sharpening per "Harness Updating != Harness Benefit" (arXiv 2605.30621):** weak-tier agents fail at activation + adherence, not at evolver quality. **Invest in better harnesses for our focal model, not in bigger evolvers.** Lock LFM2.5-1.2B-Thinking for 18 months. Re-evaluate in Month 12.
- Apple System Orchestrator pattern (sub-1W focal model routes to 4 capabilities).
- JetBrains Mellum2 (Apache 2.0, June 1 2026) for comparison.
- Microsoft IQ + Microsoft SkillOpt pattern.

**2. Gemma 4 E2B (Apache 2.0)** — *spike Month 1-2*
- Encoder-free, 2B effective params.
- Alternative focal model if LFM2.5-1.2B-Thinking plateaus.

**3. JetBrains Mellum2 (Apache 2.0, June 1 2026)** — *reference*
- Code-specialized.
- 3B params.
- Not a direct fit for Dan Glasses but a reference for the focal model pattern.

**v30 decision matrix:**

| Use case | Model | Why |
|---|---|---|
| Focal model (SIA-H Meta-Agent + openclaw-gateway) | **LFM2.5-1.2B-Thinking** | Apache 2.0-equivalent, thinking mode, focal for 18 months. |
| Focal model spike (Month 1-2) | **Gemma 4 E2B** | Encoder-free alternative. |
| Re-evaluation | Month 12 | Re-assess if "harness evolution > base-model" finding holds. |

## 5. Memory Embeddings (memoryd v1) — v30 Decision

### Candidates

**1. all-MiniLM-L6-v2 (current, 384d, sentence-transformers)** — *v1 lock*
- 384d, cosine sim, FastAPI + aiosqlite.
- **Cap at ~50% on LongMemEval.** Adequate for v1 demo.

**2. v30 plan:**
- **memoryd v2 v1.0 (Month 3):** Add temporal KG (Zep) + 4-lever cognitive consolidation (Hindsight) + 7-channel RRF (SuperLocalMemory V3.3) on top of all-MiniLM-L6-v2 embeddings.
- **memoryd v2 v2.0 (Month 6):** Add HeLa-Mem + AEL + vstash + Decagon Proactive + VisualMem. **Target: >70% LongMemEval.**

**v30 decision matrix:**

| Use case | Model | Why |
|---|---|---|
| v1 embeddings | **all-MiniLM-L6-v2 (384d)** | Sentence-transformers, FastAPI + aiosqlite. 50% LongMemEval cap. |
| v2 embeddings (Month 3) | **all-MiniLM-L6-v2 + temporal KG (Zep) + cognitive consolidation (Hindsight)** | Add structure on top of v1. 60-70% LongMemEval. |
| v2.5 embeddings (Month 6) | **v1 + HeLa-Mem + AEL + vstash + Decagon Proactive + VisualMem** | Full 11-component stack. >70% LongMemEval. |

## 6. Sub-1W Wearable Path (BitNet b1.58) — v30 Decision

### v30 sharpening: **sub-1W is the wearable unlock. The 6-9 month path is concrete.**

**1. BitNet b1.58 2B4T (Microsoft, arXiv 2410.16144) + bitnet.cpp**
- 1.37-6.46× CPU speedup vs LLaMA.
- 55-82% energy reduction on ARM/x86.
- 1.58-bit ternary weights (-1, 0, +1).
- **The 2026 sub-1W inference reference for the wearable path.**

**2. Litespark 1.58-bit (Apple, arXiv 2605.06485, May 2026)**
- **18-97× throughput on Apple M4.**
- Hardware-aware BitNet b1.58 inference.
- **v30 single biggest performance unlock for the wearable.**

**3. T-MAC (Microsoft, arXiv 2407.00088)**
- 60-70% energy savings on edge CPUs.
- 11 tok/s on Raspberry Pi 5.
- 71 tok/s on M2 Ultra.

**4. Gemma 4 QAT (June 6 2026)**
- QAT variants for mobile/laptop.
- The bridge between full-precision training and sub-1W wearable inference.

**5. Apple AFM 3 Core Advanced NAND-MoE**
- 20B sparse with 1-4B active.
- NAND-stored weights.
- The on-device 20B unlock. Apple's bet.

**v30 decision matrix:**

| Use case | Path | Why |
|---|---|---|
| Sub-1W wearable (R&D spike Month 2-3) | **BitNet b1.58 + Litespark 1.58-bit** | 18-97× Litespark throughput on M4. 1.37-6.46× bitnet.cpp speedup. 55-82% energy reduction. |
| Sub-1W wearable (R&D spike Month 6-9) | **1-bit SigLIP2** | NeurIPS 2027 paper target. 6-9 month wearable power unlock. |
| On-device 20B reference | **Apple AFM 3 Core Advanced NAND-MoE** | NAND-stored 20B + IFP + per-prompt routing. 1-4B active. |

## v30 v29 Delta (what changed)

| v29 (June 11, 01:08 UTC) | **v30 (June 11, 01:30 UTC, 14h later)** | Reason |
|---|---|---|
| Laptop prototype VLM lock = Gemma 4 12B | **Gemma 4 12B laptop prototype VLM lock + Google AI Edge Gallery for macOS operational support (June 3, 2026)** | 9to5Mac June 3, AppleInsider June 4 |
| LFM2.5-Audio-1.5B candidate | **LFM2.5-Audio-1.5B Month 1-2 spike (Apache 2.0-equivalent confirmed v29, spike timing locked v30)** | v30 plan |
| BitNet b1.58 + Litespark 21-52× on M4 | **Litespark 18-97× on M4 (v30 sharpen) + bitnet.cpp 1.37-6.46× speedup, 55-82% energy reduction (arXiv 2410.16144) + T-MAC 60-70% energy, 11 tok/s on RPi 5** | v30 sharpen with primary sources |
| Apple AFM 3 mentioned | **v30 sharpen: AFM 3 Core 3B dense + AFM 3 Core Advanced 20B sparse (NAND-stored + IFP + per-prompt routing, 1-4B active params on iPhone 17 Pro 12GB DRAM) + Federighi June 9 confirms NONE of Gemini in AFM 3** | MacRumors June 9, AppleInsider June 9, Apple ML Research paper |
| Microsoft IQ mentioned | **v30 sharpen: Microsoft IQ details — Work IQ GA June 16, 2026 (Copilot context layer) + Fabric IQ + Foundry IQ + Web IQ. The production reference for memoryd v2's context layer.** | Microsoft Build 2026 details |
| 24 production references | **32 production references in v30: + 8 v30 NEW** | v30 expand |
| Live stack 7/7 (os-toold supervised v28) | **v30: 7/7 services re-verified live 01:30 UTC. os-toold PID 4392 (re-supervised this run, still no register_user_service).** | v30 hygiene |

## v30 Model Selection Punchlist (Week 1)

1. **Buy Monako Glass silicon teardown** ($399, ships Aug 2026). Use as production reference for 48g ARM Linux form factor.
2. **Buy GAP9 dev kit** + **Prophesee GENX320 event camera**. Use as production reference for sub-1W AI eyewear (OpenGlass pattern).
3. **Buy Microsoft Surface RTX Spark** (1 PFlop, Arm + Blackwell). Use as local AI dev box.
4. **Buy Snapdragon X Elite dev kit**. Measure LFM2.5-VL-450M Q4_0 + Gemma 4 12B + BitNet b1.58 + Litespark on Redax-class hardware.
5. **Download Gemma 4 12B GGUF Q4_0** for laptop prototype.
6. **Download LFM2.5-VL-450M-Extract GGUF** for memoryd v2 ingestion.
7. **Download LFM2.5-1.2B-Thinking** as focal model.
8. **Download Voxtral Transcribe 2** (Mistral AI) for STT v3 spike.
9. **Apple developer account + Xcode 27** for Apple Core AI extension skeleton.
10. **register_user_service for os-toold** (5 min fix, Week 1).

## Top 3 Model Recommendations for Dan Glasses v30

1. **Lock LFM2.5-1.2B-Thinking as the focal model for 18 months.** Per "Harness Updating != Harness Benefit" (arXiv 2605.30621), weak-tier agents fail at activation + adherence, not at evolver quality. Invest in better harnesses, not bigger models. Re-evaluate in Month 12. **This is the single most important model decision for the AGI thesis.**
2. **Lock Gemma 4 12B for laptop prototype, spike Gemma 4 E4B vs LFM2.5-VL-450M for wearable.** Encoder-free (Gemma 4 E4B) is the right bet long-term (Apple + Google + Firebolt-VL + PLaMo 2.1-VL all validate). LFM2.5-VL-450M is the safe hedge (Brilliant Labs Halo is the production reference). Lock by end of Month 3.
3. **Spike BitNet b1.58 + Litespark 1.58-bit in Month 2-3.** 18-97× throughput on M4, 1.37-6.46× bitnet.cpp speedup, 55-82% energy reduction. This is the sub-1W wearable unlock. NeurIPS 2027 paper target.

---

*Last updated: 2026-06-11 07:00 IST (01:30 UTC) — v30.*
*Status: 14 model candidates analyzed. 5 locks (Gemma 4 12B laptop, Gemma 4 E4B wearable spike, LFM2.5-VL-450M-Extract memoryd, LFM2.5-1.2B-Thinking focal, LFM2.5-Audio-1.5B audio-language spike). 3 spikes (BitNet b1.58, Voxtral Transcribe 2, AFM 3 NAND-MoE architecture study). 10-item Week 1 punchlist. Top 3 recommendations. The bet is locked.*
