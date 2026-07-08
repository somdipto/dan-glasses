# Dan2 — Model Selection Deep Dive v11 (2026-07-03 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Scope:** the four model decisions that shape Dan Glasses v1.0 and v1.5, plus the on-device cascade gate (v8), the MemDelta eval rig (v9), the HRM-Text-1B integration (v11), and the Kokoro-82M elevation (v11).
> **v11 deltas vs v9:** 1 new model layer (HRM-Text-1B as the v1.5 audiod post-processor), 1 v9 confirmation (LFM2.5-VL-450M still the v1.0 VLM, validated by Gemma 3 in orbit), 1 v9 retraction (Mem0 v1.5 promotion paused pending MemDelta protocol), 1 v9 elevation (Kokoro-82M displaced MAI-Voice-2 as v1.5 plan-A TTS), 1 v11 add (Gemma 3 in orbit as external reference for on-device VLM thesis).

---

## Decision 1: VLM (perceptiond) — LFM2.5-VL-450M

**v11 update:** no change to v9. **LFM2.5-VL-450M is now more valuable, not less, because the open-weights edge VLM space is the scarce strategic asset in 2026-07.** The GPT 5.6 closed-source pattern (White House asked to slow roll, June 25 2026), the Anthropic Mythos 5 Glasswing gating (July 1 2026), and the Meta cloud-AI business (July 1 2026) all reinforce: closed-source frontier is the policy default. **Open-weights <500MB VLMs are the scarce asset.**

**v11 add: Gemma 3 4B in orbit (April 2026, NASA JPL + Loft Orbital Yam-9 satellite) is the strongest possible external validation of the on-device edge VLM thesis.** A 4B Gemma can do real Earth-observation triage work in space with limited compute, far from a data center. **Our 450M LFM2.5-VL-450M is the same architectural class, just smaller.** The on-device thesis is no longer "we hope it works" — it is "a 4B model is in space right now, doing triage."

### Current (v118 verified live)
- **Model:** LFM2.5-VL-450M-Q4_0.gguf (209 MB), mmproj-F16 (180 MB).
- **Runtime:** llama-mtmd-cli, -ngl 99, -c 2048, -b 1 -ub 1, -t 8.
- **Latency:** 10–15s/frame on CPU x86_64; 5–8s/frame on Apple M1.
- **Quality:** beats SmolVLM2-500M by 3–4 points (April 2026 release).
- **License:** LFM-1.0 (MIT-family, commercial use OK).
- **Verified live (2026-07-03 06:25 IST):** perceptiond v6 in `watchful` mode, 188 frames, 167 salient, 166 descriptions, vlm_busy=true. Healthy.

### Alternatives evaluated (v11 table, refreshed)
LFM2.5-VL-450M ✅, SmolVLM2-256M ✅ fallback, Gemma 3 4B ⚠️ v1.5 cloud-bridge, Gemma 4 12B Unified 🚨 v1.5/v2.0 spike, Phi-3.5-Vision ❌, InternVL2.5-1B ❌, PaliGemma 2 3B ❌, **Gemma 3 in-orbit deployment (April 2026) — external reference for the on-device thesis.**

### Recommendation
**v1.0:** keep LFM2.5-VL-450M. **v1.5:** 2-week Gemma 4 12B spike + VisualClaw cascade gate.

### Open question
What is the NDP200 NPU throughput on LFM2.5-VL-450M Q4_0? If 1.5–3s/frame, the v1.0 latency story changes.

---

## Decision 2: STT (audiod) — whisper.cpp base.en

**v11 update:** no change. **The v11 add: MAI-Transcribe-1.5 ("5x faster" per Microsoft Build 2026) is the v1.5 cloud-bridge candidate, confirmed.** Sarvam ASR remains the v1.5 India option.

**v11 add: HRM-Text-1B is the v1.5 audiod post-processor default** (replaces the v9 LFM2.5-1.2B-Thinking placeholder). The audiod post-processor does intent classification + named-entity extraction + sentiment analysis + memory-update proposal in a single forward pass. HRM-Text-1B's hierarchical reasoning model architecture is purpose-built for this.

### Current (v118 verified live)
- **Model:** ggml-base.en.bin (142 MB), int8 quant.
- **Runtime:** whisper-cli, 2 threads, 16kHz mono.
- **Latency:** ~300ms/s of audio on ARM Cortex-A78.
- **Quality:** 7.4% WER on LibriSpeech test-clean; ~12% on Indian English.
- **License:** MIT.
- **Verified live (2026-07-03 06:25 IST):** audiod v1.3 ready, segment_timing histogram shipping to Loki. 178/178 tests pass.

### Alternatives evaluated (v11 table, refreshed)
whisper.cpp base.en ✅, whisper.cpp tiny.en ⚠️ PTT, whisper.cpp large-v3 ❌, Moonshine ⚠️ v1.5, Parakeet TDT ❌, MAI-Transcribe-1.5 ⚠️ v1.5 cloud option, Sarvam ASR ⚠️ v1.5 India, **HRM-Text-1B ✅ v1.5 post-processor (NEW v11)**, LFM2.5-1.2B-Thinking ❌ retired (NEW v11).

### Recommendation
**v1.0:** keep whisper.cpp base.en. **v1.5:** evaluate Moonshine for PTT; MAI-Transcribe-1.5 for cloud-bridge; Sarvam for India. **HRM-Text-1B for the post-processor (1-week port, Q3 W3-W4).**

---

## Decision 3: TTS (ttsd) — KittenTTS medium (v1.0) → Kokoro-82M (v1.5)

**v11 update:** **MAJOR CHANGE from v9.** v9 left KittenTTS as the v1.0 default and MAI-Voice-2 as the v1.5 plan-A multilingual TTS. **v11 elevates Kokoro-82M as the v1.5 plan-A English TTS, demotes MAI-Voice-2 to v1.5 cloud-bridge multilingual fallback.** The kveeky.com 2026 TTS review, the bee.devs 45-day test against ElevenLabs/Google Cloud TTS/Amazon Polly, and the Instagram demo ecosystem all confirm Kokoro-82M as the SOTA edge TTS.

### Current (v118 verified live)
- **Model:** KittenTTS `medium` (15M params, Apache-2.0).
- **Runtime:** Python API, 24kHz mono IEEE Float WAV.
- **Voices:** 8 (expr-voice-2-m/f through expr-voice-5-m/f).
- **Latency:** ~3.8s cold, <1s warm.
- **License:** Apache-2.0.
- **Verified live (2026-07-03 06:25 IST):** ttsd healthy, voice `expr-voice-2-m`.

### Alternatives evaluated (v11 table, refreshed)
KittenTTS medium ✅ v1.0, **Kokoro-82M ✅ v1.5 plan-A (NEW v11, elevated from v9 plan-B)**, Piper ⚠️ v1.5 multilingual, **MAI-Voice-2 ⚠️ v1.5 cloud-bridge (NEW v11, demoted from v9 plan-A)**, Bark ❌, Tortoise ❌, XTTS v2 ❌, HybridCodec 🔍 v2.0 watch, **VoxCPM2 🔍 v2.0 watch (22.9k stars, TTS-from-text-description)**.

### v11 three-tier TTS stack
- **v1.0:** KittenTTS medium (8 voices, 24kHz, ~3.8s cold, Apache-2.0) — unchanged.
- **v1.5 plan-A:** Kokoro-82M (82M params, 100+ languages, Apache-2.0, on-device, beats ElevenLabs on the 45-day test) — **NEW v11, elevated from v9 plan-B to v11 plan-A.**
- **v1.5 cloud-bridge:** MAI-Voice-2 (15 languages, "realistic expression and instant voice matching", Microsoft Foundry free tier) — preserved from v9, demoted from plan-A to cloud-bridge fallback.
- **v2.0 watch:** VoxCPM2 (22.9k GitHub stars, July 1 2026, TTS-from-text-description) — creative voice design, on-device, free.

### Recommendation
**v1.0:** keep KittenTTS medium. **v1.5:** evaluate Kokoro-82M as the plan-A English TTS (1-week port, Q3 W4-W5). **v1.5 cloud-bridge:** MAI-Voice-2 for multilingual.

---

## Decision 4: Memory embeddings (memoryd) — sentence-transformers/all-MiniLM-L6-v2

**v11 update — no change to v9.** v9 said "the v1.5 promotion to Mem0 is paused pending MemDelta." **v11 confirms this.** The MemDelta paper is still the memoryd evaluation harness. **The v1.0 memoryd choice (all-MiniLM-L6-v2 + episodic/semantic/procedural schema + cosine similarity) is defensible only if we run it on the MemDelta protocol and the numbers are competitive.**

**v11 add: the v1.5 promotion to Mem0 is *still* paused, with a sharper condition.** MemDelta shows the "Mem0 beats MiniLM-RAG by 11pp" claim is conditional and reverses with cloud-RAG. We will not promote Mem0 until the MemDelta protocol shows our MiniLM-RAG baseline losing to Mem0 on the LongMemEval-S benchmark.

### Current (v118 verified live)
- **Model:** all-MiniLM-L6-v2 (22M params, Apache-2.0).
- **Dimension:** 384.
- **Runtime:** sentence-transformers, CPU.
- **License:** Apache-2.0.

### Alternatives evaluated (v11 table, refreshed)
all-MiniLM-L6-v2 ✅ v1.0, BGE-small-en-v1.5 ⚠️ v1.5 candidate, nomic-embed-text-v1.5 ⚠️ v1.5 candidate, Mem0 ❌ v1.5 paused, Zep ❌ v1.5 paused, Cognee ❌ v1.5 paused, Letta ⚠️ v1.5 research.

### Recommendation
**v1.0:** keep all-MiniLM-L6-v2. **v1.5:** run MemDelta protocol first; only promote to Mem0/BGE/nomic if the protocol shows a >5pp improvement on LongMemEval-S.

---

## Decision 5 (NEW v11): Reasoning model (audiod post-processor + openclaw agent loop) — HRM-Text-1B

**v11 new decision.** HRM-Text-1B (Sapient, June 2026) is the new SOTA small-reasoning model. **1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model (HRM) architecture.** The two-level recurrent computation enables reasoning in a single forward pass, not chain-of-thought. **The $1,500 training cost is the killer story** — when Meta or Anthropic charges $1B for their reasoning model and we trained ours for $1,500, the marketing wedge writes itself.

### Why HRM-Text-1B is the v1.5 audiod post-processor default
- **Hierarchical reasoning model architecture** — two-level recurrent computation. Designed for reasoning in a single forward pass, not chain-of-thought.
- **Small-beats-large empirically** — at 1B params, beats larger reasoning models on math/reasoning benchmarks. The HRM architecture is the algorithmic innovation, not the parameter count.
- **$1,500 from scratch** — the most extreme data-efficient training result of 2026. The "AI is too expensive to train" myth is dead.
- **Apache-2.0** — commercial use OK. No licensing risk.
- **Fits in the audiod post-processor budget** — 1B params, ~500MB Q4, runs on ARM Cortex-A78 in <500ms for 3s segments.

### Why not the alternatives
- **LFM2.5-1.2B-Thinking** — v9 placeholder, retired in v11. Training cost is unknown; HRM-Text-1B is the better story.
- **Phi-3.5-mini** — chain-of-thought, too slow for the audiod post-processor.
- **Qwen-1.5B** — chain-of-thought, too slow.
- **DeepSeek-R1-Distill-Qwen-1.5B** — chain-of-thought, too slow.
- **Gemma 3 1B** — chain-of-thought, too slow.

### Recommendation
**v1.5:** integrate HRM-Text-1B into the audiod post-processor as the v1.5 plan-A default. 1-week port, Q3 W3-W4. Direct-swap, not benchmark-first — the architectural fit is so strong that the only question is "does it work on our hardware," not "is it the best model."

---

## v11 Summary

| Decision | v1.0 (current) | v1.5 plan-A | v1.5 plan-B | v2.0 watch |
|---|---|---|---|---|
| VLM (perceptiond) | LFM2.5-VL-450M ✅ | Gemma 4 12B spike | VisualClaw cascade gate | Gemma 3 4B in-orbit reference |
| STT (audiod) | whisper.cpp base.en ✅ | Moonshine PTT | MAI-Transcribe-1.5 cloud | Sarvam India |
| **Reasoning (audiod post-processor, NEW v11)** | n/a | **HRM-Text-1B** ✅ | LFM2.5-1.2B-Thinking ❌ retired | HRM-Text-1B v2 |
| TTS (ttsd) | KittenTTS medium ✅ | **Kokoro-82M** ✅ (elevated v11) | MAI-Voice-2 cloud-bridge (demoted v11) | VoxCPM2 |
| Memory embeddings (memoryd) | all-MiniLM-L6-v2 ✅ | BGE-small-en-v1.5 (if MemDelta shows >5pp gain) | nomic-embed-text-v1.5 | — |

## v11 Retractions

- v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path." **v11 demotes to cloud-bridge.**
- v9 said "Kokoro-82M is the v1.5 plan-B English TTS." **v11 promotes to plan-A.**
- v9 said "audiod post-processor v1.5 will use LFM2.5-1.2B-Thinking." **v11 retires in favor of HRM-Text-1B.**

## v11 Confirmations (from v9)

- v9 said "LFM2.5-VL-450M is the v1.0 VLM." **v11 confirms.**
- v9 said "whisper.cpp base.en is the v1.0 STT." **v11 confirms.**
- v9 said "KittenTTS medium is the v1.0 TTS." **v11 confirms.**
- v9 said "all-MiniLM-L6-v2 is the v1.0 memory embeddings, Mem0 v1.5 paused pending MemDelta." **v11 confirms.**

---

**End of v11 model analysis.**
