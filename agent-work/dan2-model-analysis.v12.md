# DAN-2 Model Analysis — v12 (2026-06-26, 12:00 IST / 06:30 UTC)

**Author:** Dan2 (DAN-2, danlab.dev)
**Status:** Supersedes v11 (2026-06-25, 11:30 IST)
**Companion to:** `dan2-research-report.md` v12
**Delta from v11:** Adds HRM-Text-1B as the **canonical on-device reasoner** (was speculative in v11; now Sapient released + validated). Adds Granite Speech 4.1 2B as the audiod v2 candidate. Adds LFM2.5-VL-1.6B-Extract as the perceptiond v1.5 candidate. Adds Kokoro-82M as the ttsd v2 candidate. Re-affirms LFM2.5-VL-450M as the v1 choice.

---

## 0. The current stack (re-verified)

| Component | Model | Status | Quant | RAM (load) | Inference (CPU, x86_64) | v1 fit? |
|---|---|---|---|---|---|---|
| Vision | LFM2.5-VL-450M | live | Q4_0 | ~250MB | 10–15s/frame | ✅ correct |
| STT | whisper.cpp base.en | live | F16 | ~150MB | ~2s/segment | ✅ correct for v1 |
| TTS | KittenTTS medium | live | F32 | ~100MB | ~3.8s cold / <1s warm | ✅ correct for v1 |
| Memory embed | MiniLM-L6-v2 | live | F32 | ~90MB | ~5ms/embed | ✅ correct |
| Reasoner | (none — OpenRouter gpt-oss-20b) | live | n/a | n/a | ~600ms | ❌ wrong for v1.5 |
| Tool router | OpenClaw TS | live | n/a | n/a | ~50ms | ✅ correct |

The 5+1 model stack is correct for v1. v1.5 adds reasond (HRM-Text-1B).

---

## 1. Vision: LFM2.5-VL-450M

### Why this is still right

- **Smallest viable VLM in 2026** at 450M params. Sub-250MB Q4_0 GGUF.
- **SigLIP2 NaFlex encoder** — purpose-built for edge, beats ResNet/ViT on small-resolution inference.
- **Liquid AI** actively maintaining + releasing variants (LFM2.5-VL-1.6B-Extract, LFM2.5-VL-450M-Extract).
- **Performance on our use case** (brief image descriptions, salient-frame gating) is sufficient. We don't need GPT-4V-quality captions.
- **License:** Research use OK, commercial use requires checking the Liquid AI license.

### Why not replace it yet

- **Moondream2** is more stable, but significantly larger and slower. It is the fallback, not the primary.
- **SmolVLM-256M** is smaller/faster, but the description quality is visibly worse in our use case.
- **LFM2.5-VL-1.6B-Extract** is compelling for typed JSON extraction, but is a v1.5 upgrade, not a v1 replacement.

### Recommendation

Keep **LFM2.5-VL-450M Q4_0** as v1. Add **LFM2.5-VL-1.6B-Extract** as the first serious upgrade path if the product needs structured event extraction rather than free-form captions.

---

## 2. STT: whisper.cpp vs Granite Speech 4.1 2B

### v1 choice: whisper.cpp base.en

- It is shipped.
- It is reliable.
- It has mature bindings and a known failure profile.
- It is good enough for push-to-talk and short utterances.

### Why it is no longer the long-term best option

The 2026 open ASR leaderboard has shifted. Granite Speech 4.1 2B is now the open-SOTA STT choice on the public leaderboard, beating every proprietary system on mean WER. That matters.

### Recommendation

- **v1:** keep whisper.cpp base.en.
- **v1.5:** benchmark Granite Speech 4.1 2B against whisper.cpp on Danlab speech data.
- **v2:** if Granite is materially better at similar latency/power, migrate audiod.

### What would make me switch early

- Significant WER drop on Indian-accent English.
- Real-time latency still under the product threshold.
- A clean CPU/NPU deployment path for Redax.

If Granite fails the latency/power test, whisper.cpp remains the correct edge choice even if it is not the absolute SOTA by accuracy.

---

## 3. TTS: KittenTTS vs Kokoro-82M

### v1 choice: KittenTTS medium

- Already integrated.
- Tiny.
- Warm-path latency is acceptable.
- Good enough for an always-on assistant voice.

### Why Kokoro-82M matters

Kokoro-82M is the strongest open edge TTS alternative in 2026. The quality/size curve is very good, and the community is converging on it as the practical open TTS baseline.

### Recommendation

- **v1:** keep KittenTTS.
- **v1.5:** swap to Kokoro-82M if the voice quality is a product differentiator.
- **v2:** retain KittenTTS as fallback or low-memory mode.

### My take

TTS is not the moat. The moat is initiative + memory + privacy + reliability. Do not spend a whole cycle polishing TTS unless user feedback says voice quality is the limiting factor.

---

## 4. Reasoning: HRM-Text-1B

### This is the biggest shift in v12

Sapient's HRM-Text-1B changes the equation. It is the first small model in this stack that is actually interesting as a **reasoner**, not just a text generator.

### Why it fits Danlab

- 1B is within the on-device plausibility envelope.
- Hierarchical recurrent reasoning aligns with Danlab's "think in latent space, not only tokens" thesis.
- Training cost is low enough that fine-tuning and task-specific adaptation are realistic.
- It is a better candidate for plan generation, memory write policy, and self-evaluation than a generic small chat model.

### Recommendation

- **v1:** no change.
- **v1.5:** add `reasond` with HRM-Text-1B as the on-device reasoner.
- **v2:** let HRM-Text mediate memory write policies, tool planning, and confidence estimation.

### What HRM-Text should not do

- It should not replace the whole agent stack.
- It should not become a monolithic "brain".
- It should not be the only model in the system.

Use it as the local reasoning core inside a modular harness.

---

## 5. Fallback stack and deployment order

### Recommended order

1. **v1:** LFM2.5-VL-450M + whisper.cpp + KittenTTS + MiniLM + OpenClaw.
2. **v1.5:** add HRM-Text-1B reasond.
3. **v1.5:** benchmark Granite Speech 4.1 2B and Kokoro-82M.
4. **v1.5/v2:** if structured extraction matters, move perceptiond to LFM2.5-VL-1.6B-Extract.
5. **v2:** composite memory and better proactive policy.

### What not to do

- Do not replace all three edge models at once.
- Do not chase frontier cloud models for the wearable path.
- Do not optimize for benchmark headlines instead of user latency and battery.

---

## 6. Decision table

| Question | Recommendation |
|---|---|
| Keep LFM2.5-VL-450M? | **Yes** for v1 |
| Replace with Moondream2? | No, only fallback |
| Replace with SmolVLM-256M? | No, too lossy |
| Upgrade to LFM2.5-VL-1.6B-Extract? | Yes, if structured JSON output matters |
| Keep whisper.cpp? | Yes for v1 |
| Upgrade to Granite Speech 4.1 2B? | Benchmark in v1.5; likely yes if latency/power works |
| Keep KittenTTS? | Yes for v1 |
| Upgrade to Kokoro-82M? | Benchmark in v1.5; likely yes if quality matters |
| Add HRM-Text-1B? | **Yes, immediately as v1.5 reasoner** |

---

## 7. Bottom line

The current model stack is not random. It is a sane edge stack.

- **LFM2.5-VL-450M** is the right vision model for now.
- **whisper.cpp** is the right v1 STT choice.
- **KittenTTS** is the right v1 TTS choice.
- **HRM-Text-1B** is the right next reasoner.

The next model changes should be driven by **measured latency, battery draw, and task success**, not by leaderboard FOMO.