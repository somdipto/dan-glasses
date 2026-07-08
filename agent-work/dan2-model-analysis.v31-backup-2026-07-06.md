# Dan-2 Model Analysis — v31 (2026-07-06)

> **Status:** v31 refresh. v30 backups at `*.v30-backup-2026-07-06.md`. v30 content preserved; v31 deltas prepended.
> **Scope:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, LFM2.5-230M, nomic-embed-text — are they still the right choices? What alternatives exist?
> **Verdict:** v23-v30 choices all hold. v31 adds 1 NEW supply-chain constraint (RAM pricing 40-50% Q3 + 30% Q4) that locks the 600MB combined model footprint as the v1.0 *only* sensible path, and updates the v30 v1.5 TTS plan-A with v31 VLM-power-characterization data.

---

## v31 Deltas (this refresh — 2026-07-06)

### 7. NEW SUPPLY-CHAIN CONSTRAINT — RAM prices 40-50% Q3, +30% Q4 (TechSpot, July 5 2026)

Ethan Tan (former Samsung China exec) at Jefferies briefing: **RAM prices will rise 40-50% in Q3 2026 vs Q2, then another 30% in Q4.** California lawsuit accuses Samsung/SK Hynix/Micron of conspiring to inflate. Analyst forecast: relief not until 2028.

**v31 verdict:** every MB of model footprint translates to cents per unit at scale. v1.0 model stack (combined 504MB):
- LFM2.5-VL-450M Q4_0: 209MB
- mmproj-LFM2.5-VL-450M-F16: 180MB
- KittenTTS medium: ~25MB
- MiniLM-L6-v2: ~90MB
- (Plus whisper.cpp base.en: 142MB, run-on-demand only — not resident in RAM)

v1.5 model stack (combined ~1GB):
- LFM2.5-VL-1.2B-Thinking: ~600MB (if v1.0 negation gate fails)
- MatchaTTS + vocos: 123MB
- nomic-embed-text v1.5: ~270MB
- (Plus Hermes Agent openclaw framework: ~400MB if local)

**v31 verdict:** the v1.0 504MB footprint is v31 the v1.0 *only* sensible path on supply-chain grounds. v1.5 expansion should be justified on per-feature ROI, not "because the model exists." v31 plan-X7 commits the v1.0 spec §14 to a "600MB combined model footprint is the supply-chain-constrained bet" anchor.

### 8. CONFIRMED — LFM2.5-230M reasoning post-processor (v30) holds

No new findings in v31 window for the audiod post-processor slot. LFM2.5-230M (Liquid AI, June 26 2026, 230M params, 213 tok/s on Galaxy S25 Ultra) remains v1.0 plan-A. HRM-Text-1B (v1.5 plan-A), Apertus v1.1 4B (v1.5 plan-B), OpenPhone-3B (v1.5 plan-C) all hold.

### 9. CONFIRMED — LFM2.5-VL-450M v1.0 VLM still subject to v30 plan-E1 negation gate

The v30 plan-E1 (LFM2.5-VL-450M negation-collapse probe, Q3 W3, 1 engineer-week, BEFORE v1.0 ships) holds. No new negation data in v31 window. The v31 plan-X7 RAM-pricing-anchor makes the *cost* of falling back to LFM2.5-VL-1.6B (1.6B variant, ~600MB) more painful: 3× the v1.0 footprint for marginal negation improvement. v31 sharpens the v30 plan-E1 to "if LFM2.5-VL-450M negation gate fails, the v1.5 LFM2.5-VL-1.6B substitution cost is now 2.5-3× the v1.0 footprint."

### 10. CONFIRMED — whisper.cpp base.en v1.0 STT holds

No new STT findings in v31 window. whisper.cpp base.en (142MB, fast, accurate) holds. Moonshine (Useful Sensors, 27M-122M params) remains v1.5 plan-A for CPU-only path. The v1.0 whisper.cpp is *run-on-demand* (only resident in RAM during transcription), so the v31 RAM pricing does not affect STT stack.

### 11. CONFIRMED — KittenTTS medium v1.0 TTS holds

No new TTS findings in v31 window. KittenTTS medium (~25MB, 8 voices, Python API, already wired up) holds for v1.0. MatchaTTS + vocos (123MB, 22 voices, RTF 0.163) remains v1.5 plan-A from v30. Kokoro-82M remains v1.5 plan-B.

### 12. CONFIRMED — MiniLM-L6-v2 v1.0 embedding holds

No new embedding findings in v31 window. MiniLM-L6-v2 (90MB, 384-dim, sentence-transformers) holds for v1.0. nomic-embed-text v1.5 (270MB) remains v1.5 plan-A subject to v28 plan-M1 MemDelta-controlled baseline evaluation.

---

## v31 v1.0 Model Decisions (final)

| Layer | v1.0 model | v1.5 candidate | Why |
|-------|------------|----------------|-----|
| STT (audiod) | whisper.cpp base.en (142MB, run-on-demand) | Moonshine 122M | base.en is fast, accurate, on-demand. Moonshine is a possible v1.5 upgrade. |
| Reasoning (post-processor) | LFM2.5-230M (v30) | HRM-Text-1B or Nemotron-4B-Q4 | LFM2.5-230M is the v30 best on-device reasoning model. |
| Vision (perceptiond) | LFM2.5-VL-450M (209MB + 180MB mmproj) — subject to v30 plan-E1 negation gate | LFM2.5-1.2B-Thinking (plan-A) / LFM2.5-1.6B (plan-B if gate fails) | v1.0 footprint = 389MB. v1.5 plan-A = 600MB. v31 RAM pricing makes v1.5 substitution 2.5-3× costlier. |
| TTS (ttsd) | KittenTTS medium (~25MB) | MatchaTTS + vocos (v30 NEW plan-A, 123MB) / Kokoro-82M (plan-B) | MatchaTTS is the v30 fastest + smallest on-device TTS. |
| Embedding (memoryd) | MiniLM-L6-v2 (90MB) | nomic-embed-text v1.5 (270MB) | Depends on deployment shape. AIMultiple + MemDelta evaluation required before swap. |
| Agent framework (openclaw) | Hermes Agent (v30 plan-A, v30 adds channel-fracture verification) | SIA-W+H (research bet) | Hermes Agent is the v30 1-2 week drop-in. |

## v31 v1.0 Combined Footprint (the v31 supply-chain bet)

| Component | Size (MB) | Notes |
|-----------|-----------|-------|
| LFM2.5-VL-450M Q4_0 | 209 | Vision main model |
| mmproj-LFM2.5-VL-450M-F16 | 180 | Vision encoder |
| KittenTTS medium | ~25 | TTS |
| MiniLM-L6-v2 | ~90 | Embedding |
| LFM2.5-230M (Q4) | ~115 | Reasoning post-processor |
| **Total resident** | **~619** | Plus whisper.cpp base.en (142MB, on-demand only) |
| Hermes Agent framework (openclaw) | ~400 | TS/Node, not model weights |

**v31 verdict:** the v1.0 stack is 619MB resident. v31 plan-X7 commits the v1.0 spec §14 to this number. Every MB of v1.5 expansion (MatchaTTS +98MB, nomic-embed +180MB, LFM2.5-1.6B +400MB) is a *cost* in cents-per-unit at scale.

## v31 v1.0 + v1.5 Plan Additions

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-E1 (v30) | LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head | 1 | Q3 W3, BEFORE v1.0 ships |
| plan-T1 (v30) | MatchaTTS + vocos v1.5 TTS spike | 1 | Q3 W3 |
| plan-M1 (v30) | nomic-embed-text v1.5 vs MiniLM-L6-v2 MemDelta-controlled baseline | 1 | Q3 W3 |
| plan-M2 (v30) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark | 1 | Q3 W2 |
| plan-X7 (NEW v31) | v1.0 spec §14 RAM-pricing-anchor (619MB model footprint) | 1 day copy | Q3 W1 |

---

*Maintained by DAN-2. v31 is a model-delta on v30. All v23-v30 model choices hold; v31 adds 1 new supply-chain constraint (RAM pricing 40-50% Q3 + 30% Q4) that locks the 619MB v1.0 combined footprint as the v1.0 *only* sensible path on supply-chain grounds, and adds 1 new ship-gate plan (plan-X7, 1 day copy, Q3 W1) to commit the v1.0 spec §14 to this number.*
