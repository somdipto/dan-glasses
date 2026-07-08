# Dan Glasses Model Analysis v8 — LFM2.5-VL-450M, whisper.cpp, Kokoro-82M

**Author:** Dan2 | **Date:** 2026-06-25 07:35 IST
**Status:** v8 supersedes v7

---

## Executive verdict

- **LFM2.5-VL-450M:** keep for now, but stop treating it as the endpoint.
- **whisper.cpp base.en:** still the right edge STT choice for English.
- **KittenTTS:** no longer the right choice. Replace with Kokoro-82M.
- **Best architecture:** small frozen encoder + calibration head + compression/routing stack around it.

---

## 1) LFM2.5-VL-450M — keep as default, not as final

### Why it still works
- Fits the wearable budget.
- Already integrated and proven in production.
- Good enough for low-stakes descriptions and salience gating.
- Stable in the current service split.

### Why it is not the endpoint
- The field moved.
- 2026 edge VLM work shows that **token pruning + speculative decoding + routing** deliver bigger gains than simple base-model swaps.
- OmniVLM-968M, HyperVL, and INAR-VL are better targets if the hardware can support them.

### Recommendation
Keep LFM2.5-VL-450M as the default production model, but make the system model-agnostic and prepare the compression/routing path:
- CondenseVLM
- QViD
- V5e-0
- INAR-VL router

### Replacement criteria
Swap the base only if:
- Redax-class hardware can run ~1B–2B class models reliably,
- battery/thermal measurements support it,
- and the new model materially improves OCR/chart/document understanding.

---

## 2) Edge VLM alternatives

### OmniVLM-968M
- Best candidate for a near-term swap if hardware allows.
- 9× token compression.
- Strong speedup on TTFT.
- Best if Danlab wants a more capable visual back end without jumping to 7B.

### HyperVL
- Stronger class, but bigger.
- More future-facing than current production-ready.
- Likely too heavy for the first wearable revision.

### INAR-VL
- Not a base model replacement; a routing architecture.
- The most important deployment idea in the stack.
- It makes edge/cloud a dynamic decision.

### SmolVLM / other ultra-small models
- Good as fallback or emergency mode.
- Not the main production choice if LFM2.5 is already working.

### Verdict
- **Default:** LFM2.5-VL-450M
- **Near-term improvement:** token pruning + speculative decoding
- **If hardware improves:** OmniVLM-968M
- **If deployment gets smarter:** INAR-VL routing

---

## 3) whisper.cpp — still the right STT choice

### Why it stays
- Mature.
- Local.
- Stable.
- Well understood.
- Good enough for wearable English STT.

### What to change around it
- Keep the encoder frozen.
- Add a calibration head for confidence.
- Measure ECE/Brier on Indian-accent English.
- Add multilingual fallback only if needed.

### Alternative candidates
- whisper-large-v3-turbo as a fallback for tougher multilingual cases.
- But for edge English, whisper.cpp base.en remains the pragmatic choice.

### Verdict
Do not chase STT novelty. Make whisper.cpp better calibrated.

---

## 4) KittenTTS — no longer competitive enough

### Why to replace it
- Latency and quality are good, but the market moved.
- Kokoro-82M gives a better cost/quality/footprint tradeoff.
- Kokoro has broader voice coverage and Hindi support.
- Apache 2.0 is a clean license story.

### Replace with
**Kokoro-82M**
- 82M parameters
- multiple quantized variants
- Hindi-native voices
- good warm-path latency
- easier story for India-cost and multilingual support

### Migration path
1. Add Kokoro-82M alongside KittenTTS.
2. Mirror the existing `ttsd` API.
3. Benchmark TTFA, MOS proxy, memory footprint.
4. Remove KittenTTS after parity is confirmed.

### Verdict
This is the clearest swap in the stack.

---

## 5) Model selection by subsystem

| Subsystem | Current | v8 recommendation | Why |
|----------|---------|-------------------|-----|
| audiod encoder | whisper.cpp base.en | keep | edge-efficient, stable |
| audiod calibration | none | 4-layer MLP head | enables auditable confidence |
| perceptiond VLM | LFM2.5-VL-450M | keep + prune/reroute | good enough now, room to grow |
| perceptiond upgrade | none | CondenseVLM/QViD/V5e-0 | biggest ROI on wall-clock |
| ttsd | KittenTTS | Kokoro-82M | better footprint / voices / license |
| memoryd embeddings | MiniLM-L6-v2 | keep for now; add stronger retrieval layer later | simple, cheap, good baseline |
| memoryd synthesis | none | LLM-wiki + consolidation | the missing memory layer |
| dani-skills base | mixed | small shared base + LoRA adapters | scalable personalization |

---

## 6) Compression strategy — what works in 2026

### Works
- LoRA / QLoRA for adaptation
- S-LoRA for serving many adapters
- EigenLoRAx for adapter recycling
- CondenseVLM for vision token reduction
- QViD for visual token pruning
- V5e-0 for self-speculative decoding
- INAR-VL for dynamic routing

### Does not solve the whole problem
- Quantization alone does not make a model suitable for edge.
- Smaller base models without routing can still be brittle.
- Full fine-tuning is usually the wrong answer for wearable deployment.

### Guidance
- For **base capability**, use the smallest model that clears the task.
- For **adaptation**, use LoRA/QLoRA.
- For **inference efficiency**, use pruning + speculative decoding + routing.
- For **reliability**, expose calibration and failure modes.

---

## 7) Final recommendation

If Danlab has to choose only three changes now:
1. **Swap KittenTTS to Kokoro-82M.**
2. **Keep LFM2.5-VL-450M but add token pruning and routing.**
3. **Add confidence calibration to whisper.cpp.**

If Danlab can do five:
4. **Add INAR-VL-style adaptive routing.**
5. **Prepare a hardware-upgrade path to OmniVLM-968M.**

— DAN-2, 2026-06-25 07:35 IST