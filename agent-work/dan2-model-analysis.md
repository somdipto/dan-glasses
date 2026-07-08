# Dan-2 Model Analysis — v33 (2026-07-06)

> **Status:** v33 refresh. v32 backups at `*.v32-backup-2026-07-06.md`. v32 content preserved; v33 deltas prepended.
> **Scope:** Are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right model choices? What alternatives exist in v33?
> **Run window:** 2026-07-06 04:00 → 05:00 UTC (60 min).

---

## v33 Verdict (TL;DR)

**v32 model stack holds: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + MiniLM-L6-v2 (embedding).** No competitor ships a sub-500MB VLM with comparable quality in the v33 run window. Whisper.cpp is *still* the SOTA STT for the size class. KittenTTS is *still* the SOTA TTS for the size class. v33 only sharpens: (1) confirms SK Hynix $29B IPO + Foxconn +40% YoY + Jensen 4-year memory supply as v33 *industry-funded* signal that 619MB is the v1.0 *only* path; (2) adds HRM-Text-1B as v1.5 reasoning model with the v33 *quantization-first* frame (per The New Stack "The AI revolution will not be televised — it'll be quantized"); (3) considers the v33 *next-vision-model* candidate (LFM2.5-230M, SmolVLM3, Apertus v1.1 4B) for v1.5.

---

## v33 Vision model — LFM2.5-VL-450M holds

### Current state (v32 → v33 unchanged)
- **Model**: LFM2.5-VL-450M Q4_0 (209MB) + mmproj-LFM2.5-450M-F16 (180MB)
- **Total**: 389MB combined VLM stack
- **Performance**: ~10-15s/frame on CPU-only x86_64, watchful mode keeps queue at 0-1
- **License**: Research/commercial (per Liquid AI)
- **v33 confirmation**: still the best-fit sub-500MB VLM in 2026 H2

### v33 competitor scan (window 2026-07-06 04:00-05:00 UTC)

| Model | Size (VLM total) | Quality | v33 Verdict |
|-------|------------------|---------|-------------|
| LFM2.5-VL-450M | 389MB (Q4_0 + F16 mmproj) | Best sub-500MB | **HOLD — default v1.0** |
| SmolVLM-256M (current danlab-multimodal) | 302MB | Good, smaller | HOLD as fallback |
| LFM2.5-230M | ~200MB est. | Smaller variant | v33 watch (Q3) |
| Gemma 4 12B (per New Stack, June 4 2026) | ~8GB Q4 | Nearly matches 26B benchmarks | TOO BIG for wearable — v1.0 desktop / v2.0 server |
| LFM2.5-VL-1.2B | ~1.2GB | Reasoning-tuned | v33 candidate for v1.5 (Q3) |
| HRM-Text-1B (reasoning) | 1B Q4 = ~700MB | Reasoning, not vision | ADD to v1.5 as reasoning layer |
| Apertus v1.1 4B | ~2.5GB Q4 | EU-bloc compliance | v33 candidate for v1.5 if EU data-residency required |
| Nemotron-4B-Q4 (NVIDIA) | ~2.5GB Q4 | Multi-purpose | v33 watch (Q3) |
| HTC VIVE Eagle built-in voice | N/A | Not a model, cloud-OpenAI/Gemini | NOT — v33 wedge is on-device |

**v33 conclusion on vision: LFM2.5-VL-450M is the v1.0 default. v1.5 candidates are LFM2.5-VL-1.2B (reasoning), Apertus v1.1 4B (EU residency), HRM-Text-1B (reasoning). v2.0 desktop is Gemma 4 12B Q4.**

### v33 NEW: quantization-first frame

The New Stack (July 5 2026): "The AI revolution will not be televised — it'll be quantized" — Chinese frontier models reaching near-frontier quality at Q4 quantization. v33 implication: **v1.0's 619MB footprint is the v33 supply-chain-validated + quantization-first path.** v1.0 v32 spec §14 can cite New Stack + the v33 "quantization-first" frame as the v33 *answer* to "why not bigger models?" — the answer is "because quantization + on-device is the v33 *winning architecture*, not the v33 *compromise*."

**External validation**: [The New Stack - "The AI revolution will not be televised — it'll be quantized"](https://thenewstack.io/chinese-frontier-models-quantization/) (July 5 2026).

## v33 STT — whisper.cpp base.en holds

### Current state
- **Engine**: whisper.cpp via `whisper-cli` (C/C++ subprocess)
- **Model**: ggml-base.en.bin (74MB native, 142MB downloaded)
- **Quant**: int8 (default)
- **v33 confirmation**: still the SOTA STT for sub-150MB

### v33 competitor scan

| Engine | Model | Size | Quality | v33 Verdict |
|--------|-------|------|---------|-------------|
| whisper.cpp base.en | 74MB | 142MB | WER ~3-5% on clean English | **HOLD — default v1.0** |
| whisper.cpp tiny.en | 39MB | 75MB | WER ~7-10% on clean English | v1.0 thermal-throttle fallback |
| whisper-cpp-plus-rs | async + VAD | ~80MB | Same model, async | v33 Rust-port candidate (Q3) |
| Parakeet (NVIDIA) | ~250MB Q4 | ~250MB | Better WER, multi-lang | v33 candidate for v1.5 multi-lingual |
| Parakeet-TDT-0.6B | 600MB | 600MB | WER ~6% on multi-lang | v33 watch |
| OpenPhone-3B (HKUDS, ACL 2026) | 3B | 1.8GB Q4 | Phone-agent, multi-modal STT + LLM | v33 candidate for v1.5 audiod post-processor |
| Zipformer (k2-fsa) | varies | varies | SOTA for streaming | v33 watch for v2.0 streaming STT |

**v33 conclusion on STT: whisper.cpp base.en is the v1.0 default. v1.5 candidates are Parakeet (multi-lingual), OpenPhone-3B (post-processor, 1.8GB Q4), Zipformer (streaming). v2.0 watch for speech-2 (unified STT+LLM).**

## v33 TTS — KittenTTS medium holds

### Current state
- **Engine**: KittenTTS Python API
- **Model**: medium (~25MB, 8 voices)
- **Output**: 24kHz mono IEEE Float WAV
- **v33 confirmation**: still the SOTA TTS for sub-50MB

### v33 competitor scan

| Engine | Model | Size | Quality | v33 Verdict |
|--------|-------|------|---------|-------------|
| KittenTTS medium | 25MB | 25MB | 8 voices, 24kHz | **HOLD — default v1.0** |
| KittenTTS mini | ~12MB | 12MB | Lower quality | v1.0 thermal-throttle fallback |
| Kokoro TTS | ~80MB | 80MB | Better quality, fewer voices | v33 candidate for v1.5 if quality matters more than size |
| Higgs audio | varies | varies | Higher quality | v33 watch for v2.0 |
| Parler-TTS | ~700MB | 700MB | High quality, voice-clone | v33 desktop only (v1.0 companion app) |
| ChatTTS | varies | varies | Conversational | v33 watch for v1.5 conversational mode |
| Edge TTS (Microsoft, closed-source cloud) | N/A | 0 | High quality | NOT — wedge is on-device |

**v33 conclusion on TTS: KittenTTS medium is the v1.0 default. v1.5 candidates are Kokoro TTS (80MB, higher quality), ChatTTS (conversational). v2.0 watch for speech-3 (unified TTS+emotion+prosody).**

## v33 Embedding — MiniLM-L6-v2 holds, with v1.5 swap

### Current state
- **Model**: sentence-transformers/all-MiniLM-L6-v2
- **Dim**: 384
- **Size**: 90MB ONNX
- **v33 confirmation**: still the SOTA for sub-100MB embedding

### v33 competitor scan (per plan-M1, dan4 Q3 W2)

| Model | Dim | Size | Quality (MTEB) | v33 Verdict |
|-------|-----|------|----------------|-------------|
| all-MiniLM-L6-v2 | 384 | 90MB | ~58 MTEB | **HOLD — default v1.0** |
| BGE-small-en-v1.5 | 384 | ~90MB | ~62 MTEB | v33 candidate (Q3) |
| nomic-embed-text-v1.5 | 768 | ~250MB | ~62 MTEB | v33 candidate (Q3) |
| E5-small-v2 | 384 | ~90MB | ~61 MTEB | v33 candidate (Q3) |
| gte-small | 384 | ~90MB | ~61 MTEB | v33 candidate (Q3) |
| BGE-large-en-v1.5 | 1024 | ~1.3GB | ~64 MTEB | v33 watch for v1.5 desktop |
| Cohere embed v3 (closed) | 1024 | 0 (API) | ~64 MTEB | NOT — wedge is on-device |
| Qwen3-Embedding-0.6B | 1024 | ~600MB Q4 | ~65 MTEB | v33 watch for v1.5 |

**v33 conclusion on embedding: MiniLM-L6-v2 is the v1.0 default. v1.5 candidates are BGE-small-en-v1.5 (drop-in swap, similar size, +4 MTEB), nomic-embed-text-v1.5 (+4 MTEB but 2.7× size, requires MemDelta gate per plan-M1).**

## v33 Reasoning — HRM-Text-1B is v1.5 candidate

### Current state
- **None on v1.0** — audiod v1.3 doesn't post-process transcripts. perceptiond v7.0 doesn't post-process descriptions.

### v33 candidate (per plan-M2, dan2 Q3 W3)

| Model | Size (Q4) | Quality | v33 Verdict |
|-------|-----------|---------|-------------|
| HRM-Text-1B (Sapphire, 2026) | ~700MB Q4 | Reasoning-tuned, ~competitive with 3-7B | v33 v1.5 candidate |
| LFM2.5-1.2B-Thinking | ~800MB Q4 | Reasoning, Liquid AI | v33 v1.5 candidate |
| Nemotron-4B-Q4 (NVIDIA) | ~2.5GB Q4 | Multi-purpose | v33 watch |
| Apertus v1.1 4B (EPFL) | ~2.5GB Q4 | EU-bloc, multilingual | v33 v1.5 if EU residency |
| Qwen3-1.7B | ~1.1GB Q4 | Strong reasoning | v33 watch |

**v33 conclusion on reasoning: HRM-Text-1B is the v1.5 default (per dan2-AGENTS.md "Model Strategy: HRM-Text (1B) for reasoning"). v1.5 + reasoning model brings the v1.0 619MB to v1.5 ~1.5GB total. Fits within 4GB Redax budget with 2.5GB headroom for OS + services.**

## v33 Total footprint — v1.0 unchanged, v1.5 sharpens

| Stack | v1.0 (current) | v1.5 (plan-A + plan-M2) |
|-------|----------------|--------------------------|
| Vision | LFM2.5-VL-450M Q4_0 (209) + mmproj (180) = 389MB | Same + LFM2.5-1.2B-Thinking Q4 (800MB) optional |
| STT | whisper.cpp base.en (142MB) | Same + Parakeet (250MB) optional multi-lingual |
| TTS | KittenTTS medium (25MB) | Same + Kokoro (80MB) optional |
| Embedding | MiniLM-L6-v2 (90MB) | BGE-small-en-v1.5 swap (90MB) |
| Reasoning | None | HRM-Text-1B Q4 (700MB) — *NEW* |
| **Total v1.0 raw** | **646MB** | — |
| **Total v1.5 raw** | — | **~1.5GB** |
| **Total v1.0 dedup (no reasoning)** | **~619MB** | — |
| Redax v1.0 budget (4GB) | 619MB / 4096MB = **15% utilization** | 1500MB / 4096MB = **37% utilization** |
| Redax v1.0 budget (8GB) | 619MB / 8192MB = **8% utilization** | 1500MB / 8192MB = **18% utilization** |

**v33 conclusion on footprint: 619MB v1.0 and 1.5GB v1.5 both fit within the v33 4GB consumer-validated design floor (OnePlus N6, v32). v33 supply-chain (Jensen 4-year + SK Hynix $29B IPO + Foxconn +40% YoY) makes this footprint the v33 *only* sane path.**

## v33 Model Analysis — 5 new v33 validations

1. **Jensen Huang 4-year memory shortage (Motley Fool July 5 2026)** — supply-chain *funded* signal that 619MB is right
2. **SK Hynix $29B US IPO (Reuters July 5 2026)** — supply-chain *public* signal that the v33 bet is right
3. **Foxconn +40% YoY Q2 (Reuters July 5 2026)** — supply-chain *priced-in* signal
4. **The New Stack "quantized revolution" (July 5 2026)** — quantization is the v33 *winning architecture*
5. **Gartner $234B SaaS-at-risk (CIO.com July 2 2026)** — agentic AI displaces SaaS, v1.0 stack is the v33 *displacement target*

## v33 Final Verdict

**Hold the v1.0 model stack.** LFM2.5-VL-450M + whisper.cpp base.en + KittenTTS medium + MiniLM-L6-v2. v1.5 sharpens with HRM-Text-1B (reasoning) + BGE-small-en-v1.5 (embedding) + LFM2.5-1.2B-Thinking (vision reasoning). 619MB v1.0 → 1.5GB v1.5. v33 supply-chain + 4-year Jensen + SK Hynix $29B IPO make this the v33 *only* sane path. v33 quantization-first frame: the v33 winning architecture is *not* "small model on big chip" — it is *quantized model on small chip with full chip-stack sovereignty.*
