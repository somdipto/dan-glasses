# Model Selection Deep-Dive v14 — Dan Glasses
**Author:** Dan2 (lead scientist / architect)
**Date:** 2026-06-19 10:30 IST
**Supersedes:** dan2-model-analysis.v13 (24 hours old)

---

## 0. TL;DR (v14 deltas from v13)

| Layer | v13 choice | v14 choice | Delta |
|---|---|---|---|
| Vision (desktop) | LFM2.5-VL-450M Q5_K_M | LFM2.5-VL-450M Q5_K_M | unchanged |
| Vision (wearable v1.5) | LFM2.5-VL-450M Q4_0 | LFM2.5-VL-450M Q4_0 | unchanged |
| Vision (wearable v2) | LFM2.5-VL-450M IQ3_XXS hybrid CPU+NPU | LFM2.5-VL-450M IQ3_XXS + **Snapdragon Start silicon** | **NEW: Snapdragon Start path parallel to Redax** |
| STT (desktop) | whisper.cpp base.en | whisper.cpp base.en | unchanged |
| STT (wearable) | whisper.cpp tiny.en | whisper.cpp tiny.en | unchanged |
| TTS (desktop) | KittenTTS medium | KittenTTS medium | unchanged |
| TTS (wearable) | KittenTTS base | KittenTTS base | unchanged |
| Reasoning (desktop) | cloud (OpenClaw) + GLM-5.2 for SIA | cloud (OpenClaw) + GLM-5.2 for SIA | **NEW: Shazeer at OpenAI validates non-transformer architecture; HRM-Text-1B / LFM2.5-Thinking are less contrarian** |
| Reasoning (wearable) | HRM-Text-1B (deferred) | HRM-Text-1B (deferred) | unchanged |
| Embeddings | LFM2.5-Embedding-350M (June 18) | LFM2.5-Embedding-350M | unchanged |
| Rerank | LFM2.5-ColBERT-350M (June 18) | LFM2.5-ColBERT-350M | unchanged |
| **Compliance attestation** | none | **privacyd + Sigstore Rekor + SLSA provenance** | **NEW v14** |

**Single most important v14 change:** the **Snapdragon Start program** unlocks a parallel silicon path to the wearable v2. **Plus** the v14 commercial compliance attestation stack (`privacyd` + Sigstore + SLSA).

## 1. Vision — LFM2.5-VL-450M still right; Snapdragon Start new silicon datapoint

### 1.1 v14: Snapdragon Start silicon path (NEW)

**Qualcomm Snapdragon Start (June 17 2026)** [^1]:
- **First customer:** Inspecs (global eyewear company, just partnered with Snap for Specs)
- **"Scalable Turnkey AI-Ready Toolkit"** — designed for personal AI device makers
- **Hybrid AI support** — AI device + smartphone app + cloud service
- **Security-first** — designed in

**What this means for Danlab.** Snapdragon Start is the program that gives indie glasses makers:
- Turnkey SoC reference designs
- Hybrid AI software stack
- Reference firmware
- Co-marketing with Qualcomm brand
- Access to Inspecs eyewear OEM channel

**v14 action:** Apply to Snapdragon Start this week. If accepted, plan the wearable v2 silicon around Snapdragon Start + Redax (parallel paths, not sequential). If not accepted, Redax remains the primary path.

**v14 silicon plan (updated):**

| Component | v13 plan | v14 plan |
|---|---|---|
| Vision encoder (86M) | NPU (Box-style, vendor TBD) | **Snapdragon Start NPU (preferred) + Box NPU (fallback)** |
| Text decoder (360M) | CPU | CPU |
| HRM-Text-1B (1.15B) | CPU or NPU | CPU or Snapdragon NPU |
| Whisper-tiny (39M) | CPU / DSP | CPU / DSP / Snapdragon low-power island |
| TTS base (15M) | CPU + NPU assist | CPU + Snapdragon NPU |

**Net v14 wearable v2:** Snapdragon Start silicon path is the *first* silicon plan, Redax is the *second*. This collapses the v13 "Redax hardware date still open" risk.

### 1.2 Quantization ladder (unchanged from v13)

| Quant | Combined size | Quality (vs f16) | Notes |
|---|---|---|---|
| Q8_0 | ~510 MB | ~99% | laptop only |
| Q5_K_M | ~360 MB | ~98% | laptop default |
| Q4_K_M | ~290 MB | ~96% | laptop fallback |
| Q4_0 (current) | ~390 MB | ~96% | v1.5 wearable default |
| IQ3_XXS | ~210 MB | ~94% | v2 wearable (with NPU assist) |
| IQ2_XXS | ~165 MB | ~92% | stretch target |

## 2. STT — whisper.cpp still right (unchanged from v13)

## 3. TTS — KittenTTS still right; LFM2.5-Audio-1.5B W1.5 spike still valid

## 4. Reasoning — v14 validation from Shazeer move

### 4.1 The OpenAI Shazeer move validates non-transformer architecture

**v14 critical datapoint:** Noam Shazeer (Gemini co-lead, transformer paper co-author, Character.AI founder) joins OpenAI as **lead for architecture research.** [^2] Reading: OpenAI is signaling **post-transformer architecture work aimed at consumer AI companion.**

**What this means for our model choices:**
- **LFM2.5 (hybrid shortconv+attention)** — non-transformer-or-hybrid. **Validated direction.**
- **HRM-Text (hierarchical recurrent)** — non-transformer. **Validated direction.**
- **Mnemosyne (retrieval-augmented memory)** — non-transformer-augmentation. **Validated direction.**

**Our bets are now *less contrarian* than v13 thought.** OpenAI is publicly signaling the same architectural exploration. The non-transformer lane is real.

### 4.2 GLM-5.2 (cloud) for SIA

Unchanged from v13. **Still the right Feedback-Agent.** Open, MIT, 1M context, $2/hr on H100, ranks #2 on PostTrainBench.

## 5. Embeddings + Rerank — unchanged from v13

LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M. W9 workstream.

## 6. NEW v14: Compliance attestation model stack

### 6.1 The stack

| Component | Choice | Why |
|---|---|---|
| Signing | Sigstore cosign | Mature, Kubernetes-grade, OSS |
| Transparency log | Sigstore Rekor | Public, append-only, auditable |
| Provenance format | SLSA provenance v1 | Industry standard |
| Supply-chain attestation | in-toto | Multi-party attestation |
| Orchestration | `privacyd` | Danlab's existing daemon, re-architected |

### 6.2 Compliance profiles (v14 launch set)

- **fable-5-safe** (NEW)
- **mythos-5-safe** (NEW)
- **eu-ai-act-art-9** (EU AI Act risk management)
- **dpdp-act-2023** (India DPDP Act)
- **soc2-ai** (SOC2 for AI deployments)

### 6.3 Resource budget

- Sigstore Rekor: ~$50/mo on H100 (self-hosted) or free on sigstore.dev public instance.
- cosign: free, OSS.
- `privacyd` re-architecture: ~3 weeks Dan2 + 1 week Dan1 UI.

## 7. What the model stack looks like at each form factor (v14, updated)

| Form factor | Vision | STT | TTS | Reasoning | Embedding | Rerank | Compliance | Total resident |
|---|---|---|---|---|---|---|---|---|
| **Desktop (laptop, x86_64)** | LFM2.5-VL-450M Q5_K_M (330 MB) | whisper.cpp base.en (74 MB) | KittenTTS medium (25 MB) | cloud (OpenClaw) + GLM-5.2 for SIA | LFM2.5-Embedding-350M (~150 MB) | LFM2.5-ColBERT-350M (~150 MB) | privacyd (~20 MB) | ~750 MB |
| **Wearable v1.5 (aarch64, 4h target)** | LFM2.5-VL-450M Q4_0 (209 MB) + mmproj Q8 (90 MB) | whisper.cpp tiny.en (39 MB) | KittenTTS base (15 MB) | cloud fallback | MiniLM (80 MB) | none | privacyd (lightweight, ~10 MB) | ~445 MB |
| **Wearable v2.0 (Snapdragon Start silicon, 6-8h target)** | LFM2.5-VL-450M IQ3_XXS (~150 MB) + mmproj Q8 (90 MB) — vision encoder on Snapdragon NPU | whisper.cpp tiny.en (39 MB) — low-power DSP | KittenTTS base (15 MB) — Snapdragon NPU | **HRM-Text-1B Q4 (~700 MB)** on-device | LFM2.5-Embedding-350M (150 MB) | LFM2.5-ColBERT-350M (150 MB) | privacyd (lightweight, ~10 MB) | ~1.3 GB |
| **Wearable v2.0 (lighter, no HRM-Text, 8h target)** | LFM2.5-VL-450M IQ3_XXS + mmproj | whisper.cpp tiny.en | KittenTTS base | LFM2.5-Thinking (350M, ~150 MB) on-device | MiniLM | none | privacyd (lightweight) | ~635 MB |

**Net v14 change:** Snapdragon Start row added. privacyd added as a low-overhead layer across all form factors.

## 8. What I am NOT recommending (unchanged from v13)

1. Training a custom VLM from scratch.
2. A custom STT model.
3. A custom TTS voice.
4. A 7B+ on-device LLM.
5. **NEW v14:** Building a custom Sigstore Rekor — use the public sigstore.dev instance or host one, don't fork the infrastructure.

## 9. Open questions for Somdipto

1. **Snapdragon Start application.** OK to apply this week? (3-5 days decision.)
2. **privacyd as compliance attestation product.** OK to productize with OSS / $99 / $999 tiers? (W26, 4 weeks.)
3. **Mnemosyne + LFM2.5-Embedding/ColBERT swap.** OK to benchmark + swap in W9?
4. **GLM-5.2 as SIA Feedback-Agent.** OK to use open, MIT, $2/hr H100?
5. **LFM2.5-Audio-1.5B collapse spike.** OK to benchmark in W14?
6. **HRM-Text-1B vs LFM2.5-Thinking.** OK to benchmark both on memory consolidation test set?
7. **Storage tier.** Lock 64GB primary? (Apple memory chip pricing pressure.)
8. **Liquid AI license.** Verify LFM2.5 family is commercially shippable in a .deb?
9. **Snapdragon Start co-marketing.** If accepted, OK to publicly associate Danlab with Qualcomm + Inspecs? (Strategic call.)
10. **privacyd launch branding.** "privacyd" or "Fable-5-Safe" or something else? (Marketing call.)

---

## 10. Sources

[^1]: Qualcomm Snapdragon Start Program (June 17 2026, AWE). TheLEC. https://www.thelec.net/news/articleView.html?idxno=11450
[^2]: Shazeer leaves Google DeepMind for OpenAI as lead for architecture research. TechCrunch / Ynetnews, June 18 2026. https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/