# Dan2 — Model Analysis v8
## Are LFM2.5-VL-450M, whisper.cpp, KittenTTS Still the Right Choices?

**Date:** 2026-06-17 11:30 IST
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v8. v7 archived as `dan2-model-analysis.v7.md`.
**Companion:** Read `dan2-research-report.md` §B for the AGI landscape context.

---

## 0. v8 Read in 60 Seconds

The v7 model stack is **correct** for v1:

| Layer | Model | v8 verdict | Replacement candidates |
|---|---|---|---|
| Vision (VLM) | LFM2.5-VL-450M (Q4_0) | ✅ correct for v1 | Qwen2.5-VL-3B (better quality, 2× size); HRM-Text 1B (text-only, not a replacement); PaliGemma 2 3B (older) |
| STT | whisper.cpp (base.en) | ✅ correct for v1 | Moonshine (3B? edge-friendly); Parakeet (NVIDIA TDT-0.6B); streaming distilled Whisper |
| TTS | KittenTTS (medium) | ⚠️ keep for v1, **revisit v1.5** | Piper (15MB, more languages, lower quality); Kokoro 82M (Apache 2.0, 8 voices, MIT); Coqui XTTS v2 (cloning, larger) |
| Memory embed | all-MiniLM-L6-v2 (384-dim) | ✅ correct for v1 | BGE-small-en-v1.5 (better quality, 384-dim); gte-small (similar); Stella (1.5B) |
| Reasoning (NEW v8) | HRM-Text 1B | ✅ correct for v1.5+ (when on-device stack) | Gemma 4 1B; Qwen3 1.7B; Phi-4-mini |
| Fast text (NEW v8) | Gemma 4 1B | ✅ correct for v1 | Phi-4-mini; Qwen3 1.7B; Llama 3.2 1B |

**The big change from v7:** HRM-Text 1B is now in HuggingFace transformers (PR #46025) and vLLM (PR #43098). It's no longer "potential future model" — it's deployable today. v8 makes it the **on-device reasoning** model.

**The new question v8 raises:** is KittenTTS the right **long-term** TTS, or is Piper the better choice? v8 verdict: **Piper is the better long-term choice** (smaller, more languages, GPL-3.0 vs unknown KittenTTS license, broader community). v1 ships with KittenTTS because it's already integrated; v1.5 evaluates Piper head-to-head.

**The second new question:** should we use Qwen2.5-VL-3B instead of LFM2.5-VL-450M for v1? v8 verdict: **no, keep LFM2.5-VL-450M** for v1. The 2× size of Qwen2.5-VL-3B and the higher power cost are disqualifying for wearable v1. v2 (when NPU is available) can revisit.

**The third new question:** is `all-MiniLM-L6-v2` the right embedding model? v8 verdict: **yes for v1, BGE-small-en-v1.5 for v2**. BGE is genuinely better on MTEB; MiniLM is faster. v1 doesn't have the compute to host a better model.

---

## 1. Vision (VLM) — LFM2.5-VL-450M (v8 verdict: keep)

### 1.1 Current state (v7 → v8)

LFM2.5-VL-450M:
- Released April 11, 2026 by Liquid AI
- 450M params, 16 layers, 1024 embd, hybrid shortconv+attention
- SigLIP2 NaFlex vision encoder (400M)
- Context: 32,768 tokens
- Quant: Q4_0, ~209MB; mmproj-F16 ~180MB
- Sub-250ms target inference on dedicated hardware
- License: research/commercial (need to verify specifics)

**v7 status:** live in `perceptiond`, inference ~10-15s/frame on x86_64 CPU. Works.

### 1.2 Alternative candidates (v8 evaluation)

| Model | Size | Quality (vs LFM2.5-VL-450M) | Edge viability | License | v8 verdict |
|---|---|---|---|---|---|
| **LFM2.5-VL-450M** | 209MB + 180MB | baseline | ✅ best in class | research/commercial | **keep for v1** |
| **SmolVLM-256M** | 120MB + 182MB | lower (worse on document VQA) | ✅ even smaller | Apache 2.0 | fallback if LFM2.5 disappears |
| **Qwen2.5-VL-3B** | ~1.8GB (Q4) | higher (better reasoning, OCR) | ⚠️ 2× size, 2× power | Apache 2.0 | **v2 candidate** (when NPU available) |
| **PaliGemma 2 3B** | ~1.8GB | similar to Qwen2.5-VL-3B | ⚠️ same | Apache 2.0 | v2 candidate, behind Qwen2.5-VL |
| **Gemma 3 4B** | ~2.4GB (Q4) | higher | ⚠️ 2.5× size | Gemma license | v2 candidate, larger |
| **InternVL3 2B** | ~1.2GB | higher | ⚠️ 1.4× size | MIT | v2 candidate, MIT-licensed |
| **DeepSeek-VL2-Tiny** | ~1.0GB | higher | ⚠️ similar | DeepSeek license | v2 candidate |
| **PaliGemma 2 3B + ScreenAgent** | 1.8GB | higher for screen understanding | ⚠️ same | Apache 2.0 | v2 if we focus on screen tasks |

**v8 verdict: keep LFM2.5-VL-450M for v1.** It is the right size for wearable v1 (no NPU). The 2× size jump to Qwen2.5-VL-3B is disqualifying on battery and thermals. When v2 brings NPU support, Qwen2.5-VL-3B becomes the leading candidate for the reasoning-and-vision merge.

### 1.3 What we lose by staying with LFM2.5-VL-450M

- Document OCR quality is weaker than Qwen2.5-VL-3B. **Mitigation:** offload OCR to a separate lightweight pipeline (Tesseract for fast path, or v2 with Qwen2.5-VL-3B).
- Complex scene understanding is weaker. **Mitigation:** keep the salience-based gating; only run VLM on frames where motion/face detection fires. The "low quality on irrelevant frames" is masked.
- The "what is this person doing" reasoning is weaker. **Mitigation:** the `reasond` service (HRM-Text 1B) post-processes the VLM description and adds reasoning. The system is stronger than any single model.

### 1.4 What if LFM2.5-VL-450M disappears?

The `models/download.sh` script already has the SmolVLM-256M fallback. v8 adds Qwen2.5-VL-3B as a second fallback (it's the most likely "next thing"). v8 also adds a `models/MANIFEST.md` documenting the priority order:

1. LFM2.5-VL-450M (current)
2. SmolVLM-256M (smaller fallback)
3. Qwen2.5-VL-3B (better quality, requires NPU)

---

## 2. STT — whisper.cpp (v8 verdict: keep, with streaming option)

### 2.1 Current state (v7 → v8)

whisper.cpp:
- `base.en` model, 74MB
- Production-grade via `whisper-cpp-plus-rs` (async, VAD, real-time)
- Vendor: vendored at `/home/workspace/dan-glasses/whisper.cpp/`
- Live in `audiod`, 83 tests pass

### 2.2 Alternative candidates (v8 evaluation)

| Model | Size | Quality | Latency (vs base.en) | Streaming | License | v8 verdict |
|---|---|---|---|---|---|---|
| **whisper base.en** | 74MB | baseline | baseline | ✅ via VAD | MIT | **keep for v1** |
| **whisper tiny.en** | 39MB | -10% WER | ~2× faster | ✅ | MIT | fallback for thermal |
| **Moonshine (3B edge)** | ~200MB | +15% WER | ~3× faster | ✅ native streaming | MIT | **v1.5 candidate** |
| **Parakeet TDT-0.6B** | ~400MB | +20% WER | ~4× faster | ✅ native streaming | CC-BY-4.0 | v1.5 candidate |
| **Distil-Whisper** | ~150MB | -3% WER | same | ❌ | MIT | meh |
| **NVIDIA Canary-1B** | ~1GB | +25% WER | ~5× faster | ✅ | CC-BY-4.0 | v2 candidate |

**v8 verdict: keep whisper.cpp base.en for v1.** v1.5 evaluates **Moonshine** (the strongest streaming option, MIT-licensed, purpose-built for edge).

### 2.3 What we gain from Moonshine in v1.5

- **Native streaming** (vs. whisper's "wait for VAD end" model). Lower latency, more natural conversation.
- **Better WER** than whisper base.en (15% relative improvement per the tts-bench community benchmarks).
- **3× faster inference** means the audiod thread can spend the saved power on the wake-word VAD.

**v8 action:** in month 4-5, benchmark Moonshine head-to-head with whisper.cpp base.en on a held-out 10-hour audio set. If it wins by >10% WER, switch. If it ties, keep whisper (less risk).

---

## 3. TTS — KittenTTS (v8 verdict: keep for v1, plan Piper for v1.5)

### 3.1 Current state (v7 → v8)

KittenTTS:
- Medium model, 8 voices (`expr-voice-2-m` default)
- ONNX export, CPU-friendly
- License: **unknown** (this is a problem; see §3.3)
- Live in `ttsd`, 6 tests pass
- ~25MB total

### 3.2 Alternative candidates (v8 evaluation)

| Model | Size | Quality | Latency | Voices | Languages | License | v8 verdict |
|---|---|---|---|---|---|---|---|
| **KittenTTS medium** | 25MB | baseline | ~80ms TTFA on x86_64 | 8 | EN | **unknown** | **keep for v1** |
| **Piper** | 15MB | slightly lower | ~107ms TTFA | 900+ | 47 | GPL-3.0 | **v1.5 candidate** |
| **Kokoro 82M** | ~300MB | higher than Kitten/Piper | 50-200x RT on CPU | 8 | EN/UK/ES/FR | MIT | v1.5 candidate, better quality |
| **Coqui XTTS v2** | ~1.5GB | very high (cloning) | sub-200ms first-chunk | many | 17 | CPML (license fragmentation) | v2, cloning use case |
| **ElevenLabs (cloud)** | n/a | highest | cloud latency | many | many | proprietary | not v1, cloud defeats privacy |
| **Chatterbox-Turbo** | ~1GB | high | GPU | many | many | various | not edge |

**v8 verdict: keep KittenTTS for v1 (already integrated), plan Piper or Kokoro for v1.5.**

### 3.3 The license problem (v8 P1)

KittenTTS license is unclear from the public repo. **v8 action:** DAN-1 to file an issue / contact KittenML asking for license clarity. If the license is Apache 2.0 / MIT / BSD → keep. If GPL-3.0+ → still fine for our open-source stack. If "research only" or "no commercial" → **P1 switch to Piper or Kokoro immediately**, before v1 ships.

This is a **release blocker**. v8 makes it explicit.

### 3.4 Why Piper is the v1.5 lead

- **15MB** (vs KittenTTS 25MB) — meaningful for wearable storage
- **900+ voices** (vs KittenTTS 8) — 100× the language/voice coverage
- **47 languages** (vs KittenTTS English-only)
- **GPL-3.0** is acceptable for our open-source runtime
- **Production-grade** — used in Mycroft, Home Assistant, Rhasspy

**v8 caveat:** Piper quality is slightly lower than KittenTTS-medium per the tts-bench community benchmarks. The trade-off is size/voices/languages vs quality. For an open-source AI companion, the breadth wins.

### 3.5 v8 TTS roadmap

- **v1 (ship Q4 2026):** KittenTTS medium, 8 English voices
- **v1.5 (Q1 2027):** evaluate Piper + Kokoro head-to-head; pick one (likely Piper for size)
- **v2 (Q2 2027):** add voice cloning (Coqui XTTS v2 or Piper fine-tune) for the "I want my AI to sound like me" use case
- **v3 (2028+):** explore sub-100ms streaming for natural conversation

---

## 4. Memory Embedding — all-MiniLM-L6-v2 (v8 verdict: keep, plan BGE for v2)

### 4.1 Current state (v7 → v8)

all-MiniLM-L6-v2:
- 384-dim, 22M params, ~80MB
- CPU-fast, Apache 2.0
- Live in `memoryd`, 16 tests pass
- Quality: 58.8 on MTEB (average)

### 4.2 Alternative candidates (v8 evaluation)

| Model | Size | MTEB score | License | v8 verdict |
|---|---|---|---|---|
| **all-MiniLM-L6-v2** | 80MB | 58.8 | Apache 2.0 | **keep for v1** |
| **BGE-small-en-v1.5** | 130MB | 62.0 | MIT | **v2 candidate** |
| **gte-small** | 70MB | 61.0 | MIT | v2 candidate, slightly smaller |
| **Stella 1.5B** | 1.5GB | 65.0+ | MIT | v3 candidate, too large for v1/v2 |
| **all-mpnet-base-v2** | 420MB | 63.0 | Apache 2.0 | v2 if BGE is unavailable |
| **nomic-embed-text-v1.5** | 540MB | 62.0 | Apache 2.0 | v2 candidate, longer context |

**v8 verdict: keep all-MiniLM-L6-v2 for v1.** It's small, fast, and good enough. v2 swaps in BGE-small-en-v1.5 for a 3-point MTEB improvement; the size jump (80→130MB) is fine for aarch64.

---

## 5. Reasoning (NEW in v8) — HRM-Text 1B

### 5.1 Why this is new in v8

In v7, HRM-Text 1B was flagged as a *potential* reasoning model. v8 elevates it because:
- **HuggingFace transformers PR #46025 merged** (HRM-Text is now a first-class architecture)
- **vLLM PR #43098 merged** (production inference support)
- **1.2B base checkpoint downloadable** as `sapientinc/HRM-Text-1B`
- **Architecture verified:** 16 layers, hidden 1536, 12 heads, head_dim 128, H_cycles=2, L_cycles=6, max_seq=4096
- **Pretrain is real:** $1,000-$1,500, 1 day, 16 GPUs, 40B tokens
- **Inference code released** at `github.com/sapientinc/hrm-text`

### 5.2 What HRM-Text 1B is good for

Per the paper + HF model card:
- **Hierarchical reasoning:** the dual H/L cycle means the model "thinks" in latent space before emitting tokens
- **Instruction-following:** trained on instruction-response pairs only (no raw text); 60.7% MMLU, 81.9% ARC-C, 82.2% DROP, 84.5% GSM8K, 56.2% MATH
- **Small footprint:** ~0.6 GiB at int4 → fits on aarch64 with room to spare
- **Brain-inspired architecture:** slower (H) + faster (L) timescales match the kind of "plan, then execute" reasoning that an AI companion needs

### 5.3 What HRM-Text 1B is NOT good for

- **Open-ended chat.** It's a reasoning model, not a chat model. Pair it with Gemma 4 1B for chat.
- **Long context.** Max 4096 tokens. For long-context tasks, use a model with longer context.
- **Multilingual.** Trained mostly on English instruction data.
- **General world knowledge.** It's small. For world knowledge, use a retrieval system + HRM-Text for reasoning over the retrieved context.

### 5.4 v8 reasond design (architecture)

The `reasond` service uses HRM-Text 1B for the *planning* step:

```python
# reasond.py (sketch)

class ReasoningService:
    def __init__(self):
        self.hrm = HRMTextEngine("sapientinc/HRM-Text-1B", quantization="int4")
        self.gemma = GemmaEngine("gemma-4-1b", quantization="int4")
        self.memory = MemorydClient()
        self.proactive = ProactivedClient()

    async def process_observation(self, obs):
        # Retrieve relevant memories
        mems = await self.memory.query(obs.summary, top_k=5)

        # HRM-Text plans: should we say something, what, when?
        plan = await self.hrm.plan(
            observation=obs,
            memories=mems,
            proactive_state=await self.proactive.state(),
        )

        # Gemma 4 turns the plan into natural language
        if plan.should_speak:
            text = await self.gemma.generate(
                plan=plan,
                style="concise, conversational, <30 words"
            )
            return Suggestion(text=text, target="speak", provenance=[plan, mems])
        return None
```

### 5.5 v8 reasoning model stack

| Component | Model | Size (Q4) | Purpose |
|---|---|---|---|
| Planning | HRM-Text 1B | ~600MB | "Should I speak? What? When?" |
| Generation | Gemma 4 1B | ~600MB | Natural language for the speak step |
| Vision (separate) | LFM2.5-VL-450M | ~390MB | Scene understanding |
| Memory (separate) | all-MiniLM-L6-v2 | ~80MB | Semantic recall |

**Total on-device stack:** ~1.7GB. Fits on a 4GB-RAM aarch64 board. Doesn't fit on 2GB. **v8 hardware implication: 4GB RAM is the minimum for the full stack.**

---

## 6. Fast Text (NEW in v8) — Gemma 4 1B

Gemma 4 1B is the v8 pick for fast natural-language generation. It's a clean Transformer, trained on diverse data, with strong instruction-following. It's not as "smart" as HRM-Text 1B for planning, but it's much faster at emitting tokens.

**Alternatives:** Phi-4-mini (~3.8B, too large for v1), Qwen3 1.7B (1.7B is too large for v1), Llama 3.2 1B (1B, comparable quality, Meta's license is more permissive but the model is older).

**v8 verdict: Gemma 4 1B** for v1. Phi-4-mini is the v1.5 candidate when compute is tighter.

---

## 7. Power Budget (v1, refined from canonical analysis)

v8 commits to a v1 power budget:

| Component | Watchful | Active | Notes |
|---|---|---|---|
| openclaw-gateway | 0.5W | 0.8W | Node.js idle baseline |
| memoryd (SQLite + MiniLM) | 0.2W | 0.3W | Embedding compute on recall only |
| os-toold | 0.1W | 0.2W | Idle + occasional exec |
| audiod (mic + VAD) | 0.3W | 0.5W | VAD on ALSA loop |
| audiod (whisper base.en) | 0W | 1.5W | Burst during transcription |
| perceptiond (camera + salience) | 0.5W | 0.8W | V4L2 capture + Haar |
| LFM2.5-VL-450M | 0W | 3-5W | **CPU inference, dominant spike** |
| KittenTTS (spike) | 0W | 1-2W | Synthesis burst |
| **HRM-Text 1B + Gemma 4 1B** (NEW v8) | 0W | 1-2W | Planning + generation burst |
| **Total** | ~1.6W | **~8-12W** | active peak |

**v8 battery implication:** 8-12W peak, 1.6W idle. At 4Wh battery (1080mAh @ 3.7V), that's 30 minutes of active use, 2.5 hours of watchful. **The v1 battery must be larger — minimum 6-8Wh** for 1.5-3 hours of active use. The form-factor decision (see AGI roadmap §1) must account for this.

**v8 NPU delta:** if we can move LFM2.5-VL-450M inference to NPU at 0.5-1W, total active drops to ~5-7W → 1.5-2× battery life. **This is the v2 NPU track's main value proposition.**

---

## 8. The Model Stack Summary (v8)

```
┌─────────────────────────────────────────────────────────────┐
│                    ON-DEVICE STACK (v1)                      │
├─────────────────────────────────────────────────────────────┤
│ Vision       LFM2.5-VL-450M Q4_0      390MB    ✅ live     │
│ STT          whisper.cpp base.en     74MB     ✅ live     │
│ TTS          KittenTTS medium         25MB     ✅ live     │
│ Memory       all-MiniLM-L6-v2        80MB     ✅ live     │
│ Reasoning    HRM-Text 1B int4         600MB    ⚠️ v8 add   │
│ Fast text    Gemma 4 1B int4          600MB    ⚠️ v8 add   │
│                                                             │
│ Total                                  ~1.77GB              │
│ RAM peak (estimated)                   ~3-4GB               │
│ Storage                                 ~2GB                 │
│ v1 hardware minimum                    4GB RAM / 16GB       │
└─────────────────────────────────────────────────────────────┘
```

**v8 verdict:** the stack is **right**. The model choices are **right**. The size is **right** for a 4GB-RAM aarch64 board. v2 swaps in higher-quality models (Qwen2.5-VL-3B for vision, BGE for memory, Piper/Kokoro for TTS) when NPU is available. v8 closes the reasoning gap with HRM-Text 1B + Gemma 4 1B.

---

*End of v8 model analysis. Companion artifacts: `dan2-research-report.md` (deep dives), `dan2-architecture-review.md` (concrete fixes), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read).*
