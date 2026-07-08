# Danlab AGI Roadmap — Dan2 v37 (2026-06-22)

> **Mission:** Build toward AGI from India. Two vectors run in parallel: (1) ship Dan Glasses as a real product, (2) publish credible self-improving AI research that no one else is doing from this part of the world.
>
> **v37 shift from v36:** Snap's "Proactive AI" launch (Jun 16) and NeoSapien Neo 1 ($189, India-built) collapse v36's "wedge is open" claim. **The response is sharper focus on the dglabs-eval moat and a hardware pivot decision that cannot wait for Month 2.** Self-Harness (Shanghai AI Lab, Jun 8 2026) is now the on-device default. SIA v2 (May 28 2026) has verified numbers and is the cloud-side path.

---

## The Strategic Wedge (sharpened for v37)

v36 said: "On-device + proactive + open self-improving research + India-first distribution."

v37 sharpens: **"On-device + auditable + safety-gated + open self-improving research + India-first distribution."**

**What changed:**
1. **Snap claimed "proactive AI"** (AWE 2026, Jun 16). Closed-source, cloud-dependent. Our counter: **auditable.**
2. **Agents of Chaos (Feb 2026)** is now the empirical source for what goes wrong. Our counter: **safety-gated** (5 tasks from Agents of Chaos as regression gate).
3. **Self-Harness (Jun 8 2026)** is now the on-device default. SIA v2 is the cloud-side path. **Two-stack model.**
4. **NeoSapien Neo 1 ($189) + Quest Global Neprion + Sarvam Kaze** confirm India is now a real manufacturing + distribution market. **Pick a price tier.**

**v37 wedge = on-device + auditable + safety-gated + open self-improving research + India-first distribution.**

---

## 6-Month Window (Now → Dec 2026)

**Theme: Ship dglabs-eval v1 + SIA fork + land the hardware pivot decision.**

### Week 1 (THIS WEEK) — Stabilize the foundation
- [ ] **Action 1 (5 min):** `register_user_service` for openclaw-gateway. **7th carry. Highest-ROI single action.**
- [ ] **Action 2 (1 day):** `pip install 'sia-agent[claude]'`. `sia run --task lawbench --max_gen 3`. Document results. **First SIA-fork sprint deliverable.**
- [ ] **Action 3 (1 day):** **Hardware pivot decision.** Pick one of {Qualcomm AR1 Gen 1, Snapdragon Reality Elite, Quest Global Neprion, stay with Redax}. 6-month vs 12-month wearable prototype timeline.

### Weeks 2-4 — Build dglabs-eval v1 (the moat)
- [ ] **Action 4 (1 week):** Convert Dan1/2/3/4 stream logs into dglabs-eval harness. **5 demo tasks** (smoke, memory roundtrip, vision roundtrip, audio roundtrip, tool roundtrip).
- [ ] **Action 5 (1 week):** Add **5 safety tasks** from Agents of Chaos (disproportionate response, non-owner compliance, sensitive info disclosure, owner spoofing, prompt injection). **Non-negotiable regression gate.**
- [ ] **Action 6 (1 week):** Add **5 proactive tasks** from ProAgent (motion trigger, scene change, scheduled reminder, person re-id, off-device question). **Direct counter to Snap's "AI that moves before you do" claim.**

### Months 2-3 — Ship the speedup stack + memoryd v2
- [ ] **Action 7 (2 weeks):** VLM speedup sprint — V5e-0 + QViD + SWEET (Q4/Q5/Q8 salience-gated) to perceptiond/vlm.py. Target: 10s/frame → 2-3s/frame. **Highest-leverage engineering in v37.**
- [ ] **Action 8 (6 weeks):** memoryd v2 = vectors + LightGMEM graph + VisualMem visual memory + safety audit log. LFM2.5-Embedding-350M as primary embedder.
- [ ] **Action 9 (1 week):** toold + os-toold safety audit log. Required for dglabs-eval integration.

### Months 4-6 — Public research output
- [ ] **Action 10 (2 weeks):** **First public paper:** "dglabs-eval: a held-out, on-device, on-user, safety-gated evaluation harness for self-improving AI wearables." arXiv + India AI Mission submission. **This is what differentiates Danlab from every other Dan2-equivalent team in India.**
- [ ] **Action 11 (1 week):** SIA reproducibility benchmark. Run dglabs-eval with SIA fork on dglabs-eval's tasks. Publish results. **First public SIA-vs-Self-Harness on a real on-device harness.**
- [ ] **Action 12 (1 week):** Neprion (or chosen) partner integration proof-of-concept. **First third-party wearable with dglabs-eval running.**

---

## 12-Month Window (Now → Jun 2027)

**Theme: Wearable prototype + AGI research credibility + first 1,000-user pilot.**

### Months 7-9 — Wearable dev kit
- [ ] **Action 13 (12 weeks):** First wearable prototype on chosen silicon. LFM2.5-VL-450M + V5e-0 speedup stack + whisper.cpp + KittenTTS + audiod + memoryd + toold all running on glasses form factor.
- [ ] **Action 14 (4 weeks):** dglabs-eval v2 = harness search (Meta-Harness-style) + wearable-specific tasks (motion, salience, battery-aware power scheduling).
- [ ] **Action 15 (4 weeks):** SIA-fork v2 with LFM2.5-1.2B-Thinking as Feedback-Agent (not Claude). Cross-task memory for Feedback-Agent decisions. **Publishable contribution.**

### Months 10-12 — Public research output
- [ ] **Action 16 (4 weeks):** **arXiv paper #2:** "SIA meets on-device: harness + weights on a wearable." With reproducible dglabs-eval v2 results.
- [ ] **Action 17 (1 day):** Conference submission. NeurIPS 2027 / ICML 2027 / ICLR 2027 workshops. Target: AI for AGI / On-Device ML.
- [ ] **Action 18 (2 weeks):** Open-source releases: dglabs-eval (MIT), SIA-fork (AGPL or MIT — confirm with somdipto), Dan Glasses reference hardware design (CERN-OHL-S).
- [ ] **Action 19 (4 weeks):** First 1,000-user closed beta. India-only. Bug bounty for adversarial privacy testing.

---

## 24-Month Window (Now → Jun 2028)

**Theme: AGI primitives from India.**

- [ ] **Action 20:** On-device proactive AI product launch via Neprion (or chosen partner). Target: 10,000 MAU.
- [ ] **Action 21:** dglabs-eval as a research benchmark. Cited in 10+ external papers. Maintainer status.
- [ ] **Action 22:** SIA fork as a default framework for self-improving on-device AI. Maintainer status on `hexo-ai/sia`.
- [ ] **Action 23:** First Danlab self-improving wearable model. Open weights. Trained via SIA fork on dglabs-eval. **This is the AGI primitive.**
- [ ] **Action 24:** Indian decentralized AGI narrative crystallized. Published book / paper / manifesto: "AGI from India, on-device, open-source, self-improving, safety-gated."

---

## The Three Bets (sharpened for v37)

**Bet 1: dglabs-eval is the moat.**
- v37 timeline: 6-12 months. **Tighter than v36.**
- v37 risk: Snap ships a public eval before us. **Plausible by Q4 2026.**
- v37 mitigation: **Ship dglabs-eval v1 in 3 weeks. First-to-market for on-device proactive AI eval.**

**Bet 2: Two-stack self-improvement (Self-Harness on-device + SIA cloud-side) is the architecture.**
- v37 timeline: 6-12 months. **Tighter than v36** because Self-Harness is now published and SIA v2 has verified numbers.
- v37 risk: Someone else ships a similar architecture first.
- v37 mitigation: **Open-source moat (dglabs-eval MIT) + India-first distribution + safety-gated (Agents of Chaos-inspired).**

**Bet 3: LFM2.5-VL-450M stays the right edge VLM for 12 months.**
- v37 timeline: 6-12 months. Unchanged.
- v37 risk: A new edge VLM (LFM2.5-VL-1B, OmniVLM-968M, Llama 4 Nano) leapfrogs.
- v37 mitigation: perceptiond fallback chain. perceptiond.yaml + download.sh already support SmolVLM-256M auto-fallback. **Add OmniVLM-968M and LFM2.5-VL-1B to the candidate list as v1.5 candidates.**

---

## v37 New: Safety Bet

**Bet 4: Safety-gated self-improvement is the differentiator.**
- v37 timeline: 6 months.
- v37 risk: A weight-update bug in SIA-fork causes a safety regression. Anthropic has published similar incidents.
- v37 mitigation: **5 safety tasks from Agents of Chaos as non-negotiable regression gate. Weight updates that fail any safety task are rejected. Harness edits that fail any safety task are logged but not blocked (asymmetric — weights are irreversible, harness edits are roll-backable).**

---

## Open Questions for somdipto (Δ from v36)

1. **Compute budget.** Realistic GPU budget for SIA fork + SIA-fork training? **v37 asks again — still #1 blocker. ~220 GPU-hours rough estimate for first SIA run.**
2. **Hardware pivot decision.** Redax vs Qualcomm AR1 vs Snapdragon Reality Elite vs Quest Global Neprion. **v37: must decide THIS WEEK.** 6-month vs 12-month wearable prototype timeline.
3. **Privacy posture — hard or soft.** v37 sharpens: **hard.** "No cloud ever" is now a regulatory requirement, not a marketing position.
4. **Open-source posture.** SIA fork = MIT (inherited). danlab-multimodal = AGPL. dglabs-eval = MIT. **v37 confirms v36's lean. Confirm with somdipto.**
5. **Geographic bet.** India-first (Sarvam + HMD + JioBharat + India AI Mission + Neprion + NeoSapien). **v37 confirms v36's lean.**
6. **Paperclip.** Still dormant. **v37 lean: let it die. Focus on dglabs-eval + Dan Glasses.**
7. **(v37 new) Open-source posture for Snap's proactive AI claim.** v37 lean: **build dglabs-eval and let it speak.** No need to engage Snap directly.
8. **(v37 new) HRM-Text vs LFM2.5-1.2B-Thinking on-device reasoning.** workspace AGENTS.md says HRM-Text 1B. PRD says LFM2.5-1.2B-Thinking. **v37 still can't resolve without somdipto input.** dglabs-eval supports both. Recommend: HRM-Text 1B on device (1B is the wearable ceiling today), LFM2.5-1.2B-Thinking in cloud-only SIA loop (1.2B exceeds wearable memory budget).

---

## What This Roadmap Is Not

- It's not a foundation-model training plan. **Sarvam has the 30B/105B budget. Danlab doesn't compete there.**
- It's not a research-only path. **The product (Dan Glasses) and research (SIA fork + dglabs-eval) reinforce each other.**
- It's not a "ship the wearable first" plan. **The wearable is gated on the silicon pivot decision (this week). Until then, the desktop prototype + SIA fork + dglabs-eval is the focus.**
- It's not a "ship the eval first" plan. **dglabs-eval v1 ships in 3 weeks, in parallel with the desktop prototype + SIA fork.** All three run concurrently.

---

*Dan2, 2026-06-22 v37. Aligned with PRD v1.0, canonical analysis, SIA v2 literature, Self-Harness, Agents of Chaos, and the Snap "Proactive AI" claim.*
