# Danlab AGI Roadmap v8 — Sakana-aligned, Perplexity-validated, AI-Wall-fortified

**Author:** Dan2 | **Date:** 2026-06-25 07:35 IST
**Status:** v8 supersedes v7
**North star:** auditable reliability + self-modeled harness evolution + open-source LLM-wiki memory + India-cost + wearable-shaped privacy

---

## 6-month plan (Jul – Dec 2026)

### Month 1 (Jul 1–31) — Foundation wins
1. **KittenTTS → Kokoro-82M swap** (1-week decision). Apache 2.0, 82M, 54 voices, 8 languages (Hindi native), 92MB quantized variant. Deploy by Jul 15. WebGPU fallback path for Tauri webview.
2. **Per-daemon reliability surface contract** (1-week spec, 2-week impl). Every daemon exposes `GET /reliability` returning {calibration, consistency, robustness, predictability, safety}. audiod promotes `confidence: 0.83` to first-class with `GET /reliability/calibration` returning ECE, Brier, reliability diagram. memoryd surfaces query/recall calibration; perceptiond surfaces salience-confidence; toold surfaces command-outcome; ttsd surfaces synthesis-quality.
3. **memoryd v2 spec lock** (2-week spec). Lock the AEL + DPCM + LLM-Wiki + operative_context + audit trail + self-model design. Reference: Perplexity Brain (closed but observable). Write SPEC.md + AGENTS.md.
4. **OpenClaw audiod_rl_events channel** (3 days). audiod RL agent broadcasts every snapshot save + failure-mode trigger to Telegram channel `audiod_rl_events`. Marketing asset: "watch Danlab's AI get better, auditable, every hour."

### Month 2 (Aug 1–31) — Self-model + memoryd v2 ship
1. **memoryd v2 build (weeks 5–8)**. 6-week compressed build. Operative_context stream is the self-model. Failure-mode registry is first-class. AEL bandit over retrieval modes (semantic/episodic/procedural/operative_context/graph). DPCM doubly-linked provenance. LLM-wiki overnight synthesis. Deploy by Aug 15.
2. **arXiv pre-print: audiod confidence-calibration RL agent**. v8 design (AHE-style harness evolution + self-model write-back to memoryd operative_context + ECE/Brier surface + failure-mode registry). Submit by Aug 15.
3. **Tauri v2 native bundle path** (deferred to v2 wearable, but start `.deb`/`.AppImage` build config).
4. **Open-source the danlab-multimodal repo's self-improvement loop** as the audiod RL agent's substrate (per dani integration discussion).

### Month 3 (Sep 1–30) — Submit, ship, evaluate
1. **Submit audiod RL agent to AIE-Bench (ICML 2026 CTB workshop) + SEAGym**. Both venues target meta-improvement and harness-only updates. Submission deadline Sep 30, 2026.
2. **Submit memoryd v2 to LongMemEval + PersonaMem-v2**. Memory-as-self-model benchmark.
3. **Perceptiond v0.8 — CondenseVLM/QViD/V5e-0 stack** (3-week impl). Combined 3-5× wall-clock on same LFM2.5-VL-450M model.
4. **Perceptiond v0.9 — INAR-VL adaptive routing** (2-week impl). Edge-only vs cloud-only is dead. Adaptive routing layer.

### Month 4 (Oct 1–31) — Hardware + v1 wearable target
1. **Hardware decision lock** (Redax / Monako Glass / Brilliant Labs Halo / Project Solara MDEP). Dev-kit buy this month.
2. **Form factor spec lock**. Camera + voice (v1). Display later. ~36g target (matches Even G2).
3. **Privacy posture spec lock**. Local-only by default. Hardware mic kill-switch in v2. Per-memory-type retention policy. Auditable calibration surface as marketing asset.

### Month 5 (Nov 1–30) — India market + marketing cycle alignment
1. **Hindi TTS voice fine-tune** on Kokoro-82M. Native Indian-accent support.
2. **Indian-accent OOD eval dataset** for audiod RL agent (CommonVoice Indian-accent subset).
3. **Show HN post draft** (Aug 25 target carried forward; Nov 2026 alternate if audiod RL agent needs more time).
4. **arXiv camera-ready** for ICML 2026 acceptance / rejection.

### Month 6 (Dec 1–31) — v1 wearable dev-kit
1. **Dev-kit prototype** (target: 50 units for early-access researchers).
2. **memoryd v2 production hardening** (LongMemEval + PersonaMem-v2 leaderboards).
3. **AIE-Bench + SEAGym publication** (camera-ready).
4. **AGI roadmap v9** based on v8 results.

---

## 12-month plan (Jul 2026 – Jun 2027)

### H2 2026 (Jul–Dec 2026)
- Ship audiod RL agent (arXiv + AIE-Bench + SEAGym).
- Ship memoryd v2 (6-week build → Aug 15 deploy).
- Ship TTS swap (Kokoro-82M + Hindi).
- Ship perceptiond v0.8 (token-pruning stack) + v0.9 (INAR-VL routing).
- Lock hardware decision (Redax et al).
- Dev-kit prototype (50 units).

### H1 2027 (Jan–Jun 2027)
- **v1 consumer launch** (camera + voice, no display, ₹4,999 student / ₹12K founder).
- **memoryd v3 with federation** (LoRA/QLoRA adapter upload, opt-in federated learning).
- **perceptiond v1.0** (condensed model + INAR-VL routing + frame retention).
- **proactived service** (per v33 proactive-AI deep-dive: GRAM + VARS + GraP-Mem + LOCOMO-CONV).
- **OpenClaw auditable surface** (every channel is auditable, every event has provenance).
- **arXiv v2** of audiod RL agent paper (incorporate ICML 2026 reviews + v2 results).

---

## 24-month plan (Jul 2026 – Jun 2028)

### 2026 H2 (above)
### 2027 H1 (above)

### 2027 H2 (Jul–Dec 2027)
- **Display module** (waveguide / microLED). Even G2-shaped display.
- **Hardware mic kill-switch v2**.
- **dani-skills library v2** (50+ LoRA-tuned skills on shared small base).
- **paperclip substrate decision** (per open question from v6; see open questions below).

### 2028 H1 (Jan–Jun 2028)
- **v2 consumer launch** (camera + voice + display + India-cost).
- **Memory-as-self-model v2** (federated + on-device consolidation).
- **Self-improving v2** (harness evolution + self-model + AHE + adaptive routing + auditable).
- **AGI roadmap v10** based on 2027 results.

---

## Bet ranking — what to fund first

| # | Bet | Horizon | ROI | Risk |
|---|-----|---------|-----|------|
| 1 | audiod calibration RL agent (arXiv + AIE-Bench) | 3 months | **Highest** | Medium (Sakana DGM proof mitigates) |
| 2 | memoryd v2 (Perplexity-Brain-shape, open-source) | 2 months | **Highest** | Low (Perplexity closed-but-observable) |
| 3 | KittenTTS → Kokoro-82M swap | 1 week | High | Very low (Apache 2.0, 1-week swap) |
| 4 | Perceptiond token-pruning stack | 3 weeks | High | Low (drop-in on LFM2.5) |
| 5 | INAR-VL adaptive routing | 2 weeks | Medium-High | Medium (router is new code) |
| 6 | Hardware dev-kit buy | 1 month | Medium | Medium (Redax moving target) |
| 7 | Open-source danlab-multimodal RL loop | 2 months | Medium | Medium (substrate choice open) |
| 8 | Microsoft Scout / OpenClaw collaboration | 6 months | High strategic | Low (they chose our gateway) |

---

## Open questions (need somdipto's input)

1. **Compute budget cap** for self-improvement training ($5K–$20K for audiod RL agent + memoryd v2 LoRA + perceptiond token-pruning distillation).
2. **Hardware decision** (Redax / Monako Glass / Brilliant Labs Halo / Project Solara MDEP / custom).
3. **Show HN date lock** — Aug 25 vs Nov 2026.
4. **memoryd v2 substrate** — pure Python/SQLite (current) or graph DB (Weaviate Engram pattern)?
5. **Hardware privacy switch** — v1 feature or v2?
6. **Even Realities G2 partnership** — they are the only "proactive AI" competitor. Partnership / acquisition path?
7. **paperclip substrate** for first self-improvement loop (per v6 open question).
8. **Microsoft Scout** — OpenClaw is their substrate. Should Danlab engage? (Microsoft just chose our gateway.)
9. **Dan1 marketing cycle (v83)** said "Aug 25 Show HN." v8 says audiod RL agent needs until Sep 30 for AIE-Bench submission. Reconcile?
10. **Dani integration role** — audiod RL agent as Dani skill, first-class daemon, or both?

---

## Why v8 is sharper than v7

- **External validation from Sakana (Jun 7)** + **Perplexity (Jun 18)** + **AI Weekly wall (Jun)** compresses v7's timeline by 2 weeks (memoryd v2 ships Aug 15, not Sep 15).
- **Meta Ray-Ban Display at $799 + Ray-Ban Gen 2 at $379 + Microsoft Scout on OpenClaw** sharpens competitive positioning. Meta is the scale competitor (EMG + display + cloud), Even is the philosophy competitor (no camera + on-device + privacy), Microsoft Scout is the substrate endorsement.
- **AI Weekly self-improvement wall** adds the self-model constraint that locks the audiod RL agent design. Without it, we'd ship a v7-style harness evolution that would plateau at iteration 1.
- **Perplexity Brain +25% / +16% / -13%** validates the memoryd v2 architecture at production scale. The closed competitor has done the engineering work; we ship the open-source version.

**The single sentence:** v8's 6-month plan compresses v7 by 2 weeks (memoryd v2 deploys Aug 15, not Sep 15) because Sakana and Perplexity have both validated the architecture from outside; v8's 12-month plan adds the v1 consumer launch and proactived service; v8's 24-month plan adds display module and federated memory. Show HN locks Aug 25 if audiod RL agent arXiv lands by Aug 15; otherwise Nov 2026.

— DAN-2, 2026-06-25 07:35 IST