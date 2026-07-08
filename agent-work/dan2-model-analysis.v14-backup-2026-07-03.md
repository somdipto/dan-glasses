# Dan2 — Model Analysis v14 (2026-07-03 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Scope:** re-evaluate every model selection in the Dan Glasses stack against fresh 2026-07-03 signals.
> **Backup of v13:** `dan2-model-analysis.v13-backup-2026-07-03.md`
> **v14 deltas vs v13 (3 new candidates, 1 sharpening, 0 retractions, 5 confirmations):**
> 1. **Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026)** — v1.5 audiod post-processor alternative for EU data-residency. Multilingual variant watch.
> 2. **Memora pattern (Microsoft Research, July 2026)** — v1.5 memoryd architecture. Not a model, a storage/retrieval pattern.
> 3. **Hermes Agent (Nous Research, June 2026)** — v14 openclaw agent-framework plan-B. MIT, open-source, supports ChatGPT subscription integration.
> 4. **MiCRo (EPFL, late June 2026)** — 4-cognitive-region LLM. Validates the on-device specialized-region thesis.
> 5. **v13 confirmations:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, HRM-Text-1B, Qwen3-TTS plan-A, Kokoro-82M fallback, MemDelta eval rig, Karpathy 10-rule openclaw, Ollie gaze-informed proactive, GLM-5.2 research bet, INT8 memoryd compression.
> 6. **v14 sharpening:** BBC-reported Meta paywall ($19.99/mo, 15hr) is now the primary marketing anchor. Anthropic Sonnet 5 is 5-57x more expensive than GLM-5.2 / Kimi-K2.6 / DeepSeek-V4-Pro (X coverage, late June 2026) — the open-weights cost multiplier is the new marketing fact.

---

# v13 model analysis (preserved below)

# Dan2 — Model Selection Deep Dive v13 (2026-07-03 03:00 UTC / 08:30 IST)

> **Canonical (v13):** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Scope:** the four model decisions that shape Dan Glasses v1.0 and v1.5.
> **v13 deltas vs v12 (2 new candidates, 1 INT8 compression add, 0 retractions, 4 confirmations):** GLM-5.2, Mirendil, INT8 memoryd compression.

---

## Decision 1: VLM (perceptiond) — LFM2.5-VL-450M

**v14 update:** no change to v9/v11/v12/v13. **LFM2.5-VL-450M is still the v1.0 default.** v14 adds:

- **MiCRo (EPFL, late June 2026)** — brain-like LLM with 4 specialized cognitive regions (memory, reasoning, language, decision). Validates the on-device specialized-region thesis. **Direct read-through:** our 6-daemon split (audiod, perceptiond, memoryd, toold, ttsd, openclaw) is the engineering analogue of the MiCRo "4 cognitive regions" pattern. Each daemon is a specialized region; the inter-daemon protocol is the "neural pathway" between regions. **v14 add: cite MiCRo as the academic validation of our 6-daemon split in v1.0 marketing.**

### Current (v118 verified live)
- **Model:** LFM2.5-VL-450M-Q4_0.gguf (209 MB), mmproj-F16 (180 MB).
- **Runtime:** llama-mtmd-cli, -ngl 99, -c 2048, -b 1 -ub 1, -t 8.
- **Latency:** 10–15s/frame on CPU x86_64; 5–8s/frame on Apple M1.
- **Quality:** beats SmolVLM2-500M by 3–4 points (April 2026 release).
- **License:** LFM-1.0 (MIT-family, commercial use OK).
- **Verified live (2026-07-03 06:25 IST):** perceptiond v6 in `watchful` mode, 188 frames, 167 salient, 166 descriptions, vlm_busy=true. Healthy.

### Alternatives evaluated (v14 table, refreshed)
LFM2.5-VL-450M ✅ v1.0 default, LFM2.5-VL-450M-Extract ⚠️ v1.5 structured-JSON, LFM2.5-VL-1.6B-Extract ⚠️ v1.5 cloud-bridge structured-JSON, SmolVLM2-256M ✅ v1.0 fallback, Gemma 3 4B ⚠️ v1.5 cloud-bridge (now in-orbit), Gemma 4 12B Unified 🚨 v1.5/v2.0 spike, Phi-3.5-Vision ❌, InternVL2.5-1B ❌, PaliGemma 2 3B ❌, MiCRo (EPFL) ✅ v1.0 marketing citation.

### Recommendation
**v1.0:** keep LFM2.5-VL-450M. **v1.5:** 2-week Gemma 4 12B spike + VisualClaw cascade gate + LFM2.5-VL-Extract (1.6B for cloud, 450M for on-device) for structured-JSON queries. **v1.0 marketing:** cite MiCRo as the academic validation of the 6-daemon split.

### Open question
What is the NDP200 NPU throughput on LFM2.5-VL-450M Q4_0? If 1.5–3s/frame, the v1.0 latency story changes.

---

## Decision 2: STT (audiod) — whisper.cpp base.en

**v14 update:** no change to v9/v11/v12/v13. **v14 add: Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026) is the v1.5 audiod post-processor alternative for EU data-residency.** Apertus is a fully open-weights 4B instruction-tuned model with EU-grade data compliance. HRM-Text-1B remains the v1.5 plan-A; Apertus is the v1.5 plan-B for EU users.

### Current (v118 verified live)
- **Model:** ggml-base.en.bin (142 MB), int8 quant.
- **Runtime:** whisper-cli, 2 threads, 16kHz mono.
- **Latency:** ~300ms/s of audio on ARM Cortex-A78.
- **Quality:** 7.4% WER on LibriSpeech test-clean; ~12% on Indian English.

### Alternatives evaluated (v14 table, refreshed)
whisper.cpp base.en ✅ v1.0 default, whisper-large-v3 ❌ (size), distil-whisper ⚠️ v1.1 research, Moonshine ❌ (untested), HRM-Text-1B ✅ v1.5 post-processor, GLM-5.2 🚨 v1.5 research, Apertus v1.1 4B Instruct ✅ v1.5 EU post-processor.

### Recommendation
**v1.0:** keep whisper.cpp base.en. **v1.5:** HRM-Text-1B integration into audiod post-processor. **v1.5 EU variant:** Apertus v1.1 4B Instruct.

---

## Decision 3: TTS (ttsd) — KittenTTS medium

**v14 update:** no change to v9/v11/v12/v13. KittenTTS remains v1.0 default; Qwen3-TTS remains v1.5 plan-A; Chatterbox remains v1.5 voice-cloning.

---

## Decision 4: Memoryd (memoryd) — SQLite + MiniLM-L6-v2

**v14 update:** **NEW: Memora storage/retrieval split is the v1.5 architecture.** v14 replaces the v9/v11/v12/v13 single-tier MiniLM-L6-v2 model with a two-tier architecture:

- **Storage tier (rich):** raw memories, raw held-out ground truth, raw agent proposals. Same MiniLM-L6-v2 embeddings as v1.0 (no migration risk). Schema: `memories.type` extended to include `storage` (rich content) and `cue` (lightweight abstraction).
- **Retrieval tier (lightweight):** cue anchors + summaries. The cue anchors are computed at write time (storage writes trigger an async cue-generation pass). Retrieval is a two-hop: cue-level cosine similarity first → if cue matches, surface the full rich memory. This is the Memora pattern.

**Direct read-through:** the Memora paper claims 98% context token reduction with no accuracy loss. The MemDelta paper shows our current 384-dim single-tier is worse than basic RAG (42% < 47%). The Memora pattern is the architectural fix.

**v14 add:** the storage/retrieval split is the v1.5 memoryd architecture. Effort: 2 weeks, 1 engineer. Schedule Q3 W2-W3, in parallel with the Anthropic Dreaming port.

### Current (v118 verified live)
- **Model:** sentence-transformers/all-MiniLM-L6-v2, 384-dim float32.
- **Storage:** SQLite + BLOB embedding column, WAL mode, 50k memories supported.
- **Retrieval:** cosine similarity on the embedded content.
- **Verified live (2026-07-03 06:15 IST):** 540KB DB, 44 memories, persistence verified across restarts.

### Alternatives evaluated (v14 table, refreshed)
MiniLM-L6-v2 ✅ v1.0 default, MiniLM-L12 ⚠️ v1.1 research, BGE-M3 ❌ (size), nomic-embed-text ⚠️ v1.1 research, OpenAI text-embedding-3-small ❌ (cloud), Cohere embed-v3 ❌ (cloud), **Memora pattern ✅ v1.5 architecture**, INT8 MiniLM-L6-v2 ✅ v1.1 RAM cost compression.

### Recommendation
**v1.0:** keep MiniLM-L6-v2 + SQLite + cosine similarity. **v1.1:** INT8 quantization of stored embeddings (4× storage reduction, <2% recall@10 loss) — 1-week spike in response to RAM cost crisis. **v1.5:** Memora storage/retrieval split.

---

## v14 new candidates (research bet, not v1.0/v1.5)

### Hermes Agent (Nous Research, June 2026)
- **What:** open-source agent framework, MIT, supports ChatGPT subscription integration.
- **License:** MIT.
- **Why v14 add:** SIA-W+H is the v1.5 plan-A agent-framework port. Hermes is the v1.5 plan-B if SIA port stalls. Mirendil (a16z-backed) and Memora (Microsoft) are closed-source references, not portable.
- **Open question:** does Hermes support the `auto_apply=False` contract for memoryd writes? Need to read the spec.

### Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026)
- **What:** open-weights 4B instruction-tuned, Swiss provenance, EU-grade data compliance.
- **License:** open-weights (specific license TBD).
- **Why v14 add:** EU data-residency requirements. HRM-Text-1B is the v1.5 plan-A audiod post-processor; Apertus is the v1.5 plan-B for EU users. Multilingual variant watch.

### MiCRo (EPFL, late June 2026)
- **What:** brain-like LLM with 4 specialized cognitive regions (memory, reasoning, language, decision). Open-weights research release.
- **License:** research-only, not production.
- **Why v14 add:** validates the on-device specialized-region thesis. Use as a v1.0 marketing citation, not a v1.5 model candidate.

---

## v14 cost multiplier fact (marketing)

**Anthropic Sonnet 5 is 5-57x more expensive than the open-weights alternatives (X coverage, late June 2026):**
- GLM-5.2: 5x cheaper than Sonnet 5
- Kimi-K2.6: 7x cheaper than Sonnet 5
- DeepSeek-V4-Pro: 57x cheaper than Sonnet 5
- Opus 4.8 Max: 1.2x more expensive than Sonnet 5
- GPT-5.5-xhigh: 2x more expensive than Sonnet 5

**v14 add:** the open-weights cost multiplier is now a quantified 2026 fact. The BBC-reported Meta $19.99/mo paywall + the Sonnet 5 vs GLM-5.2 cost multiplier are the two v1.0 marketing anchors.
