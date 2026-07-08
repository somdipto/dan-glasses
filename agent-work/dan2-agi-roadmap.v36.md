# Danlab AGI Roadmap — Dan2 v36 (2026-06-21)

> **Mission:** Build toward AGI from India. Two vectors run in parallel: (1) ship Dan Glasses as a real product, (2) publish credible self-improving AI research that no one else is doing from this part of the world.
>
> **v36 shift from v35:** v35's three-bet structure stands. v36 sharpens each bet with concrete primitives, sharper timelines, and a specific response to the Jun 2026 "harness + weights" consolidation in the literature.

---

## The Strategic Wedge (unchanged from v35)

1. **The wearables category is exploding** (Snap Specs $2,195, Meta Ray-Ban Gen-2, Google Project Aura, Qualcomm Reality Elite). All are cloud-dependent. All are reactive.
2. **No one is shipping on-device proactive AI** at consumer scale. The closest published architecture is ProAgent (arXiv:2512.06721) — 27.7% higher proactive accuracy.
3. **The credible path to recursive self-improvement is now MIT-licensed and shipping on GitHub** (`hexo-ai/sia`, May 2026). **v36 changes the calculus: we fork, not build.**

**Danlab's wedge = on-device + proactive + open self-improving research + India-first distribution.**

---

## 6-Month Window (Now → Dec 2026)

**Theme: Make Dan Glasses a credible demo + ship the SIA fork + land the dglabs-eval moat.**

### Month 1 — Stabilize the foundation
- [ ] **Action 1 (5 min):** `register_user_service` for openclaw-gateway. Kills the "STATUS.md says 4/7 live" lie. **Carry-forward from v35, still not done.**
- [ ] **Action 2 (2h):** Systemd units for all 7 services with `Restart=on-failure`, `RestartSec=2`.
- [ ] **Action 3 (1 day):** `scripts/health.sh` that curl-checks all services and posts to Telegram on failure. Replaces stale manual status.
- [ ] **Action 4 (3 days):** VLM speedup sprint — apply V5e-0 + QViD + SWEET (Q4/Q5/Q8 salience-gated) to perceptiond/vlm.py. Target: 10s/frame → 2-3s/frame. **Highest-leverage engineering in v36.**
- [ ] **Action 5 (1 week):** Fork `hexo-ai/sia` into `danlab-multimodal/sia/`. Wrap `src/demo.py`'s heuristic scorer as SIA verifier. Use LFM2.5-1.2B-Thinking as Feedback-Agent. Run first reproducibility test (50 iterations on the 3 demo screens). **Honest reporting required.**

### Month 2-3 — Ship the dglabs-eval moat
- [ ] **Build `dglabs-eval`:** SEAGym-style harness for Dan Glasses. Frozen update-validation + replay diagnostics + audit log. Open-source under **MIT**. This is the moat.
- [ ] **memoryd v2:** Add graph layer (LightGMEM entity graph) on top of vectors. Add visual memory (VisualMem) — 1 image per salient event. Wire LFM2.5-Embedding-350M as primary embedder.
- [ ] **Perceptiond v2:** Ship VLM speedup stack from Month 1. Add Whisper streaming + VAD improvements.
- [ ] **Bootstrap wizard v1:** Ship the actual wizard state machine + retry UX + permission flow. **v35 deferred this; v36 makes it a hard gate.**
- [ ] **First public demo:** Stream Dan Glasses live via Telegram (@danlab_bot). One of the first public on-device proactive AI demos. Capture for content.

### Month 4-6 — Land the India-first distribution
- [ ] **HMD / Lava / JioBharat partnership pitch:** Dan Glasses software (no hardware) + HMD earbuds with cameras. **One integration deal > ten engineering sprints.**
- [ ] **Publish first paper:** "dglabs-eval: a held-out, on-device, on-user evaluation harness for self-improving AI wearables." arXiv + India AI Mission submission. **This is what differentiates Danlab from every other Dan2-equivalent team in India.**
- [ ] **SIA reproducibility benchmark:** Run dglabs-eval with SIA fork on dglabs-eval's tasks. Publish results. **First public SIA-vs-baseline on a real on-device harness.**
- [ ] **Memoryd v3:** VisualMem + LFM2.5-ColBERT-350M reranker. Personal visual recall — the first open-source implementation.

---

## 12-Month Window (Now → Jun 2027)

**Theme: Wearable prototype + AGI research credibility.**

### Month 7-9 — Wearable dev kit
- [ ] **Pick the silicon.** v36 read: pivot from Redax to **Qualcomm Snapdragon AR1 Gen 1** or **Snapdragon Reality Elite** (Jun 16 announcement). 6+ month time-to-prototype advantage. **Decision needs to be made in Month 2.**
- [ ] **First wearable prototype on dev kit:** LFM2.5-VL-450M + whisper.cpp + KittenTTS + audiod + memoryd + toold all running on glasses form factor.
- [ ] **dglabs-eval v2:** Add wearable-specific tasks (motion, salience, battery-aware power scheduling).
- [ ] **SIA-fork v2:** Add harness code-modification with dglabs-eval as the verifier gate.

### Month 10-12 — Public research output
- [ ] **arXiv paper #2:** "SIA meets on-device: harness + weights on a wearable." With reproducible dglabs-eval results.
- [ ] **Conference submission:** NeurIPS 2027 / ICML 2027 / ICLR 2027 workshops. Target: AI for AGI / On-Device ML.
- [ ] **Open-source releases:** dglabs-eval (MIT), SIA-fork (AGPL), Dan Glasses reference hardware design (CERN-OHL-S).
- [ ] **First 100 users:** India-only closed beta. Bug bounty for adversarial privacy testing.

---

## 24-Month Window (Now → Jun 2028)

**Theme: AGI primitives from India.**

- [ ] **On-device proactive AI product launch.** HMD/JioBharat/Lava distribution. Target: 10,000 MAU.
- [ ] **dglabs-eval as a research benchmark.** Cited in 10+ external papers. Maintainer status.
- [ ] **SIA fork as a default framework** for self-improving on-device AI. Maintainer status on `hexo-ai/sia`.
- [ ] **First Danlab self-improving wearable model.** Open weights. Trained via SIA fork on dglabs-eval. **This is the AGI primitive.**
- [ ] **Indian decentralized AGI narrative crystallized.** Published book / paper / manifesto: "AGI from India, on-device, open-source, self-improving."

---

## The Three Bets (sharpened)

**Bet 1: On-device proactive AI is a real wedge.**
- v36 timeline: 12-18 months. **Tighter than v35.**
- v36 risk: Snap ships proactive AI on-device (Snapdragon XR) before us. **Plausible by Q4 2026.**
- v36 mitigation: **dglabs-eval + first public paper.** Define the eval category; ship before Snap can productize.

**Bet 2: SIA-fork is the credible recursive self-improvement path. v36: fork + integrate, not build.**
- v36 timeline: 6-12 months. **Tighter than v35** because SIA is now on GitHub with CLI + visualizer.
- v36 risk: Hexo Labs or Sakana ships a closed-source productization first.
- v36 mitigation: **dglabs-eval + open harness + reproducible benchmark.** Open-source moat.

**Bet 3: LFM2.5-VL-450M stays the right edge VLM for 12 months.**
- v36 timeline: 6-12 months. Unchanged.
- v36 risk: A new edge VLM (OmniVLM-968M, Llama 4 Nano, Gemma 4) leapfrogs.
- v36 mitigation: perceptiond fallback chain. perceptiond.yaml + download.sh already support SmolVLM-256M auto-fallback. **Add OmniVLM-968M and Qwen3-VL-2B to the candidate list as v1.5 candidates.**

---

## Open Questions for somdipto

1. **Compute budget.** Realistic GPU budget for SIA fork + any future training? **v36 asks again — this is the #1 blocker.**
2. **Hardware pivot.** Stay with Redax (locked but timeline unclear) or pivot to Qualcomm AR1 (Jun 16 announced, 6+ month time advantage)? **v36 leans Qualcomm. Decision needed by Month 2.**
3. **Privacy posture — hard or soft?** v36 sharpens: hard. "No cloud ever." Pick the side.
4. **Open-source posture.** SIA fork = MIT (inherited). danlab-multimodal = AGPL (fork-back). dglabs-eval = MIT (moat via usage, not license). **v36 leans this trio.** Confirm.
5. **Geographic bet.** India-first (Sarvam + HMD + JioBharat + India AI Mission) or US/EU (Qualcomm + Snap + Meta channels)? **v36 leans India-first.** Confirm.
6. **Paperclip.** Revive as dani-skills plugin, or let die? **v36 lean: let it die.** Focus.

---

## What This Roadmap Is Not

- It's not a foundation-model training plan. **Sarvam has the 30B/105B budget. Danlab doesn't compete there.**
- It's not a research-only path. **The product (Dan Glasses) and research (SIA fork + dglabs-eval) reinforce each other.**
- It's not a "ship the wearable first" plan. **The wearable is gated on the silicon pivot decision (Month 2). Until then, the desktop prototype + SIA fork + dglabs-eval is the focus.**

---

*Dan2, 2026-06-21 v36. Aligned with PRD v1.0, canonical analysis, SIA literature, and the Jun 2026 "harness + weights" consensus.*
