# Dan2 — Run notes (v12, 2026-07-03 02:00 UTC / 07:30 IST)

**Run window:** 2026-07-03 02:00–02:15 UTC (07:30–07:45 IST)
**Trigger:** scheduled research agent cycle
**Re-trigger from:** v11 (2026-07-03 06:30 IST, 18 hours ago)
**Status:** v12 SHIPPED — 5/5 artifacts on disk. v11 backed up to `*.v12-backup-2026-07-03.md`.

## What I did

1. Re-read dan1 v118, dan3 v6, dan4 v113 scratch pads. Foundation still locked. 7/7 daemons healthy. memoryd 16/16, toold 18/18, ttsd 6/6 (40/40 pass).
2. Re-read v11 dan2*.md (research-report, agi-roadmap, architecture-review, model-analysis, papers-to-read) for continuity. Backed up to `*.v12-backup-2026-07-03.md`.
3. Executed fresh 2026-07-03 web sweep:
   - **Red Queen Gödel Machine (arXiv:2606.26294v1, June 24 2026)** — Cambridge + NVIDIA paper, viral June 28 via Kucoin. The headline signal of v12.
   - **Qwen3-TTS is now the 2026 open-weights TTS SOTA** (TextToLab + LocalAIMaster July 2026). Displaces v11's Kokoro-82M as v1.5 plan-A.
   - **Chatterbox (Resemble AI, MIT, 0.5B)** — 65.3% preferred over ElevenLabs in vendor blind test. New v1.5 voice-cloning option.
   - **Karpathy 10-rule CLAUDE.md (June 28 2026)** — new openclaw contract pattern.
   - **Ollie gaze-informed proactive AI (arXiv 2607.00445, July 1 2026)** — closest published analog to our perceptiond-driven proactive AI.
   - **ICRA 2026 (Vienna, June 1-5)** — VLA pattern (TARS DexHand, Orbbec + Robbyant LingBot-Depth). Defer to v2.0.
   - **Vinton Cerf (Open Frontier, June 30 2026)** on agent protocol standards.
   - **Anthropic Favaro+Clark (Time, June 29 2026)** on RSI safety.
   - **Meta One Premium $20/mo paywall on Conversation Focus (July 1 2026)** — primary marketing wedge.
   - **Apple Siri AI WWDC 2026 (CNET, June 30 2026)** — "buy new hardware" TCO angle.
   - **Intelligence eyewear market +83% YoY Q1 2026 (Informa TechTarget, July 2026)** — market validation.
   - **LFM2.5-VL-450M-Extract + LFM2.5-VL-1.6B-Extract (Liquid AI, October 2025)** — v1.5 structured-output VLM candidates.
4. Wrote v12 of all 5 artifacts. Backed up v11 to `*.v12-backup-2026-07-03.md`. Promoted v12 to canonical (unsuffixed files).

## v12 deltas vs v11

### Architecture: Red Queen moving-judge is the new plan-A
- v11 said: HRM-Text-1B integration into audiod post-processor as v1.5 plan-A
- v12 says: **Red Queen Gödel Machine moving-judge pattern** is the v1.5 plan-A. HRM-Text-1B stays as v12 plan-B (still confirmed). The moving-judge is the v12 implementation of the v11 `auto_apply=False` contract.

### TTS: Qwen3-TTS displaces Kokoro-82M as v1.5 plan-A
- v11 said: Kokoro-82M as v1.5 plan-A
- v12 says: **Qwen3-TTS as v1.5 plan-A.** Kokoro-82M is now the v1.5 fallback / CPU mode. Chatterbox (Resemble AI, MIT, 0.5B) is the new v1.5 voice-cloning option.

### Proactive AI: Ollie pattern is the new proactived v1 architecture
- v11 said: GRAM, VARS, GraP-Mem, ToolScout, LOCOMO-CONV in the proactive AI survey
- v12 says: **Ollie gaze-informed two-stage pattern** is the v12 proactived v1 architecture. perceptiond.get_gaze_estimate() → region selection → ttsd.speak() → memoryd.write() with TTL + attention cost → user confirm/discard. 2-week port.

### Openclaw contract: Karpathy 10-rule CLAUDE.md
- v11 said: Anthropic Dreaming `auto_apply=False` is the v1.0 contract
- v12 says: **Anthropic Dreaming + Karpathy 10-rule CLAUDE.md pattern** is the v1.0 contract. Karpathy's 6 new rules teach the agent to "monitor its own reasoning, not just write code." 1-day spike.

### Marketing wedge: Meta $20/mo paywall + Apple $1,200+ upgrade
- v11 said: Gemma 3 in-orbit + HRM-Text-1B combination
- v12 says: **Meta $20/mo paywall + Apple $1,200+ upgrade** is the primary wedge. More relatable to consumers, more directly relevant to the AI-glasses buyer. The Gemma 3 in-orbit story is preserved as the v1.5 marketing second-wave.

## Files (v12)

- `dan2-research-report.md` (310 lines, 43.3KB) — v12 canonical
- `dan2-agi-roadmap.md` (207 lines, 19.8KB) — v12 canonical
- `dan2-architecture-review.md` (221 lines, 19.8KB) — v12 canonical
- `dan2-model-analysis.md` (202 lines, 17.7KB) — v12 canonical
- `dan2-papers-to-read.md` (149 lines, 15.9KB) — v12 canonical

## Files (v11 backups)

- `dan2-research-report.v12-backup-2026-07-03.md`
- `dan2-agi-roadmap.v12-backup-2026-07-03.md`
- `dan2-architecture-review.v12-backup-2026-07-03.md`
- `dan2-model-analysis.v12-backup-2026-07-03.md`
- `dan2-papers-to-read.v12-backup-2026-07-03.md`

## Open carry-forwards (unchanged from v11)

1. Rust toolchain on host is 1.63.0, Tauri 2 needs ≥1.74. **Now blocking audiod v6.1 wiring. Carry forward.**
2. Redax hardware still moving target. **Now in decision tree alongside Monako Glass / Brilliant Labs Halo / Project Solara MDEP / Snap Specs. Carry forward.**
3. Form factor (weight, battery) still unvalidated. **Critical path. Buy dev kits THIS WEEK.**
4. danlab-multimodal still pre-RL scaffold. **v12: now defensible as a research bet with the Red Queen moving-judge pattern as the v1.5 implementation.**
5. The 7-daemon supervision gap (`register_user_service`). **Still not done. 5-min fix. Day 1.**

## Telegram deliverable

SENT to somdipto (@Shodan_s) with:
- TL;DR of v12 thesis (3 paragraphs)
- List of 5 artifacts with file paths
- Top 3 recommendations for Danlab's AGI direction
- Open questions (3) for somdipto
