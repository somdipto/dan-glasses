# Model Selection Deep-Dive — v101 (Dan2, 2026-06-29)

**Author:** Dan2 (👾) | **Source:** SOTA surveys (Apr–Jun 2026), team RFCs, locked decisions in AGENTS.md.

---

## TL;DR

Five locked-in model picks, two changes since v100.

| Job | Locked | v100? | v101 | Why |
|---|---|---|---|---|
| **Reasoning (planner)** | HRM-Text 1B | HRM-Text 1B | HRM-Text 1B + **chat head needed** | HRM is trained on puzzles, not chat |
| **Vision** | LFM2.5-VL-450M | LFM2-VL-450M | **LFM2.5-VL-450M** | Apr 2026: +bbox, +function-calling, 28T tokens, sub-250ms |
| **STT** | whisper.cpp | whisper.cpp | whisper.cpp | whisper-tiny.en floor, whisper-base comfort |
| **TTS** | KittenTTS | KittenTTS | **KittenTTS default + Kokoro-82M quality opt-in** | Kokoro is #1 on TTS Arena (Jan 2026) |
| **Orchestrator** | OpenClaw (Bun/TS) | OpenClaw (Bun/TS) | OpenClaw (Bun/TS) | Locked, no change |

The two changes: (1) **vision upgrade** to the new LFM2.5 release, (2) **TTS pivot** to dual-track (KittenTTS for size, Kokoro for quality).

---

## 1. **Vision: LFM2.5-VL-450M** — confirmed right, upgraded release

**Locked.** Apr 2026 release of the model we already had locked in v100 (under its prior name LFM2-VL-450M). The new release is strictly better:

| Capability | LFM2-VL-450M (v100) | LFM2.5-VL-450M (v101) | Delta |
|---|---|---|---|
| Training tokens | 10T | **28T** | +180% |
| RealWorldQA | 52.29 | (improved, exact TBD) | ✓ |
| MM-IFEval (instruction following) | 32.93 | **45.00** | +37% |
| Bounding box output | ❌ | ✅ (RefCOCO-M) | new |
| Function calling | ❌ | ✅ (BFCLv4) | new |
| Context window | ~32K | **128K** | 4× |
| Sub-250ms edge inference | ✓ | ✓ | unchanged |
| GGUF Q4_0 / Q8_0 | ✓ | ✓ | unchanged |
| Multilingual | partial | **expanded** | ✓ |

**Sources:** Liquid AI blog Apr 8 2026, HuggingFace model card, local-Llama reddit benchmark threads.

**Implications for Dan Glasses:**
- perceptiond can output **structured bounding boxes** ("where is my coffee cup?" → `{"bbox": [120, 200, 300, 400]}`) instead of free-text descriptions. Faster to render on JBD MicroLED HUD, lower latency, higher precision.
- Function-calling means perceptiond can call toold directly without round-tripping through HRM-Text. New fast-path.
- 128K context means we can stream multi-frame sequences into perceptiond without sliding-window truncation.

**Concrete next step for Dan3:** swap GGUF from `LiquidAI/LFM2-VL-450M-GGUF` to `LiquidAI/LFM2.5-VL-450M-GGUF`, add bbox-aware prompt templates, test 6-turn conversation memory.

**SmolVLM2-500M comparison:** LFM2.5-VL-450M is the clear winner on most benchmarks (RealWorldQA, MM-IFEval, BFCLv4). SmolVLM2 has video support — but Dan Glasses is glasses, not video. LFM2.5 wins.

---

## 2. **STT: whisper.cpp (whisper-tiny.en floor)** — still right

**Locked.** whisper-tiny (39M) is ~6× realtime on Apple Silicon. whisper-tiny.en (English-only) is the floor for v1. whisper-base (74M) is comfortable for noisy environments. whisper-large is out of scope for glasses.

**Multilingual path:** when we add Hindi support, switch whisper-tiny.en → whisper-tiny (multilingual, ~10% slower but covers 99 languages).

**Conclusion:** no change.

---

## 3. **TTS: KittenTTS default + Kokoro-82M quality opt-in** — pivoted

**Prior:** KittenTTS (<25MB) as the only TTS.
**v101:** dual-track.

### Why KittenTTS is still default
- **Smallest production-grade TTS** in 2026. <25MB model.
- Multilingual-ready (KittenTTS supports Hindi natively).
- Apache 2.0.
- 25MB RAM + sub-100ms first chunk on glasses-class ARM.
- Important: every MB on the glasses matters (2×200mAh battery, JBD MicroLED controller budget).

### Why add Kokoro-82M as quality opt-in
- **#1 on TTS Arena (Jan 2026)**, beating models 10–100× its size. The Arena score is the closest thing to a "people voted on this" benchmark for TTS.
- **300MB FP16 / 164MB quantized**. Heavy for glasses, fine for phone companion.
- **English-only**. So KittenTTS remains the multilingual default.
- Apache 2.0 license, full commercial use allowed.
- 36–96× realtime on GPU, 24kHz output.

### Recommended code path

```ts
// ttsd config
type TTSConfig = {
  primary: { engine: 'kittentts'; voices: string[] };     // always warm
  quality: { engine: 'kokoro-82m'; voices: string[] };     // phone-only, opt-in
  routing: (text, ctx) =>
    ctx.device === 'glasses' ? 'primary'
    : ctx.user_prefers_quality ? 'quality'
    : 'primary';
};
```

### Comparison

| Dimension | KittenTTS | Kokoro-82M |
|---|---|---|
| Model size | <25MB | 300MB (FP16) / 164MB (Q4) |
| Languages | Multilingual incl. Hindi | English only |
| Quality (Arena Elo) | unknown (smallest, not Arena) | **#1 Jan 2026** |
| CPU capable | ✓ | ✓ |
| Voices | limited | 10+ voicepacks |
| License | Apache 2.0 | Apache 2.0 |
| Voice cloning | ❌ | ❌ |
| On-glasses viability | ✅ default | ❌ (too heavy) |
| On-phone viability | ✅ | ✅ (recommended) |

**Sources:** Kokoro review (TextToLab Jan 2026), KittenTTS GitHub issue #40, Artificial Analysis TTS leaderboard.

---

## 4. **Reasoning: HRM-Text 1B + chat head** — caveat added

**Locked.** HRM-Text 1B (Hierarchical Reasoning Model, ~27M params + 1B total) is the planner head. Inspired by Sapient Inc.'s ARC-AGI work.

**New concern raised in v101 review:**
- HRM is trained on **reasoning puzzles (ARC-AGI)**, not general conversation.
- Without a chat-tuned head, conversation quality will be poor.
- Risk: user says "tell me a joke" → HRM tries to reason → nonsense.

**Recommendation:** add a chat head. Three options:

| Option | Pros | Cons | Recommendation |
|---|---|---|---|
| **LFM2.5-1.2B-Instruct** | 1.2B, edge-deployable, chat-tuned, Apache 2.0, same family as LFM2.5-VL-450M | Slightly larger than HRM | **Recommended.** |
| **Phi-4-mini-instruct** | 3.8B, top reasoning for size | 3× larger, slower on glasses | Use as fallback for non-glasses contexts |
| **Fine-tune HRM-Text on chat** | Single model | Requires a chat dataset + training run; delays v1 | Defer to v2 |

**Recommended split:**
- `perceptiond` → `hramed-plan(image, context)` (HRM-Text, planning)
- `ttsd` ← `chat-head(text, style)` (LFM2.5-1.2B-Instruct, surface)
- Joint training via v1.5 distill the chat head back into HRM.

**Owner:** Dan2 (reasoning layer), with input from Dan3 (vision integration).

---

## 5. **Orchestration: OpenClaw (Bun/TypeScript)** — locked, no change

Already covered in AGENTS.md and architecture-review.md. TS/Bun for gateway, Rust for performance-critical services. MCP for interop.

---

## 6. Future option: **LFM2.5-8B-A1B** for phone-side reasoning

Liquid released on May 28 2026:
- 8.3B total parameters
- 1.5B **active** per token
- 128K context
- 38T training tokens
- llama.cpp + MLX + vLLM + SGLang + ONNX day one

Why this matters: **active parameters beat total parameters** for edge/phone deployment. The same hardware that runs LFM2.5-VL-450M (4x Snapdragon-class) can host LFM2.5-8B-A1B for the phone-side reasoning. **This unlocks "phone-class Dan" running on Dan Glasses' paired phone.**

**Recommendation:** v1.5 candidate for the phone-side reasoning upgrade. Keep HRM-Text 1B on the glasses itself.

---

## 7. Things we are NOT using (and why)

| Model | Why we don't use it |
|---|---|
| GPT-5 / Claude Opus 4.8 | Cloud-only, kills privacy story |
| Llama 3.1 405B | Too large for edge |
| Qwen2.5-VL-3B | Heavier than 450M, marginal quality gain, not edge |
| DiinternVL2-1B | Not SOTA in this segment anymore |
| ElevenLabs / Polly / Gemini TTS | Cloud, kills privacy |
| Hermes Agent itself (as a model) | It's an agent framework, not a foundation model |
| Whisper-large-v3 | Too heavy for glasses (1.5GB) |
| Claude Code / GitHub Copilot | Cloud, not on-device |

---

## 8. Open questions for somdipto

1. **HRM-Text chat head.** LFM2.5-1.2B-Instruct, Phi-4-mini, or fine-tune HRM? Decision blocks the planning pipeline.
2. **Kokoro opt-in or default?** Quality vs memory tradeoff. Recommend opt-in for v1.
3. **LFM2.5-8B-A1B on phone — which version?** Phone-class Dan vs glasses Dan.
4. **Whisper multilingual.** v1 English-only or English+Hindi? Affects whisper-tiny vs whisper-tiny.en.
5. **SmolVLM2 video.** If Dan Glasses adds a video-record button, do we switch to SmolVLM2 for video frames?

---

## 9. v101 changes from v100

- Vision: **upgraded** to LFM2.5-VL-450M (was LFM2-VL-450M).
- TTS: **pivoted** to dual-track (KittenTTS default, Kokoro-82M quality).
- Reasoning: **added caveat** — HRM-Text needs a chat head; recommended LFM2.5-1.2B-Instruct.
- Added: **LFM2.5-8B-A1B** as future phone-side option.
- Tightened the "things we're not using" list.
- Added 5 open questions for somdipto.

---

## Sources

- Liquid AI LFM2.5-VL-450M blog: https://www.liquid.ai/blog/lfm2-5-vl-450m
- LFM2.5-VL-450M-GGUF HF: https://huggingface.co/LiquidAI/LFM2.5-VL-450M-GGUF
- Liquid AI LFM2.5-8B-A1B analysis: https://www.llmrumors.com/news/liquid-ai-lfm25-edge-models-device-race
- Kokoro-82M review: https://texttolab.com/blog/kokoro-tts-review
- KittenTTS comparisons: https://github.com/KittenML/KittenTTS/issues/40
- Artificial Analysis TTS: https://artificialanalysis.ai/text-to-speech/models
- HRM (Sapient Inc., hierarchical reasoning): https://arxiv.org/abs/2506.21734
- Danlab Claw-SWE-Bench (harness benchmark): https://arxiv.org/abs/2606.12344
