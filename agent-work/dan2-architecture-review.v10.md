# Dan2 — Dan Glasses Architecture Review v10
## Concrete Fixes: HUD Decision, Meta Display Comp, SIA Collaboration

**Date:** 2026-06-18 07:30 IST (02:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v10. v9 archived as `dan2-architecture-review.v9.md`. v10 is a delta on v9.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

## 0. v10 Read in 60 Seconds

The v9 architecture is correct. v10 changes four things:

1. **Wearable v2 form factor = NO HUD.** Meta Ray-Ban Display ships Sept 30, 2026 with HUD at $799. We do not chase the HUD. v2 is camera + mic + bone-conduction audio only.
2. **SIA fork = collaboration with Hexo Labs / Stanford.** Contact Vignesh Baskaran (LinkedIn-confirmed) this week. Plan co-fork and co-publication.
3. **privacyd v1.0 publishes three compliance attestations:** Fable 5 safe, EU AI Act aligned, DPDP Act aligned. Each is a separate `/privacy/<claim>` endpoint with audit log.
4. **The 10-service topology is locked.** No new services in v10. The v10 work is *integration + ship*, not *new architecture*.

The v10 architecture:
- **v1.0 (Nov 2026):** 8 services. The 7 v1 services + privacyd (with three compliance attestations).
- **v1.1 (Q2 2027):** 10 services. + reasond + proactived.
- **v2 (Q3 2027):** 10 services. + wearable form factor (NO HUD).

## 1. v10 Service Topology (LOCKED)

### 1.1 The 10-Service Topology

| # | Service | Port | v1.0 | v1.1 | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | audiod | 8090 + WS 8091 | ✅ | ✅ | Dan2 | live, 83 tests |
| 2 | perceptiond | 8092 | ✅ | ✅ | Dan3 | live, 8 tests |
| 3 | memoryd | 8741 | ✅ (v1) → v2 in v1.1 | v2 | Dan4 | live, 16 tests |
| 4 | toold | 8742 | ✅ | ✅ | Dan4 | live, 18 tests |
| 5 | ttsd | 8743 | ✅ | ✅ | Dan4 | live, 6 tests |
| 6 | os-toold | 8744 | ✅ | ✅ | Dan1 | live |
| 7 | openclaw-gateway | 18789 | ✅ (hardened) | ✅ | Dan1 | live |
| 8 | privacyd | 8748 | ✅ (NEW v9/v10 month 2) | ✅ | Dan1+Dan2 | design |
| 9 | reasond | 8745 | — | ✅ | Dan2 | design |
| 10 | proactived | 8746 | — | ✅ | Dan2 | design |

**v10 verdict:** no topology changes from v9. The 10-service shape is locked.

### 1.2 IPC Pattern (v10 LOCKED, no change from v9)

- HTTP control plane on each service.
- WebSocket fan-out where events stream (audiod WS 8091, perceptiond ring buffer GET).
- Unix sockets for high-frequency local IPC (within Tauri app).
- Bearer-token auth on cross-machine endpoints (none in v1.x — all loopback).
- JSON over HTTP. Serde structs in `shared/` Rust crate.

## 2. v10 Wearable v2 Form Factor: NO HUD (NEW v10)

### 2.1 The HUD decision (v10 LOCKED)

**v9 said:** wearable v2 = glasses with camera + mic + speaker.
**v10 LOCKED:** wearable v2 = glasses with camera + mic + bone-conduction audio. NO HUD. NO display.

**Why:**
1. **Meta Ray-Ban Display ships Sept 30, 2026 at $799 with HUD.** The HUD race is *Meta's race*, not ours. Meta has $100B+ in capex. We cannot match their hardware.
2. **HUD requires:** display module (waveguide or microLED), optics calibration, battery +30%, thermal design for display heat. This is *hardware engineering at scale*.
3. **HUD does NOT align with our moat.** Our moat is *open-source + on-device + auditable + Fable 5 safe*. The HUD is a *hardware feature*, not a *trust feature*. Chasing the HUD dilutes our moat.
4. **Bone-conduction audio is enough** for the wearable v2 use case: hear Dan's voice without blocking ears, while still hearing ambient sound.

### 2.2 v10 wearable v2 hardware BOM (target $400)

| Component | Cost | Notes |
|---|---|---|
| Redax board (aarch64, 4GB RAM, 32GB eMMC) | $80-120 | the canonical SoC |
| Camera module (V4L2-compatible, 1080p) | $30-50 | commodity, multiple vendors |
| MEMS microphone array (2-mic, beam-forming) | $10-15 | used in hearing aids |
| Bone-conduction audio (temple-mounted) | $20-30 | AfterShokz-style, open-source alternatives exist |
| Battery (LiPo, 600mAh, USB-C PD charging) | $15-25 | single battery, not 2x |
| Frame + optics + assembly | $100-150 | injection-molded, custom design |
| Misc (PCB, passives, ESD protection) | $20-30 | |
| **Total BOM** | **$275-420** | **Target: $400 with margin** |

**v10 BOM comparison:** Meta Ray-Ban Display = ~$300 BOM + $499 marketing/distribution = $799 retail. We can hit $400 retail with $275-420 BOM. **We undercut Meta Display by 2x.**

### 2.3 v10 wearable v2 design constraints (NEW v10)

- **Weight target:** <50g (target: 45g with bone-conduction + lightweight battery).
- **Battery life target:** 4h continuous use (with VLM in watchful mode).
- **Form factor:** similar to Meta Ray-Ban (camera + mic + audio, NO display).
- **Privacy:** camera has a hardwired LED indicator (always on when camera is on; cannot be disabled in software).

**v10 form-factor decision:** write `docs/v2-form-factor.md` in v10 month 1. Document the BOM. Document the NO-HUD decision. Document the privacy LED.

## 3. v10 SIA Fork Collaboration (NEW v10)

### 3.1 The collaboration plan (v10 LOCKED)

The SIA fork in v9 was a *unilateral fork*. v10 elevates it to a *collaboration* with Hexo Labs / Stanford.

**v10 outreach plan:**
- **v10 month 1 (this week):**
  - LinkedIn message to Vignesh Baskaran (Hexo Labs presenter at Stanford Salone d'Onore, June 2026).
  - GitHub issue on HexoLabs/SIA proposing co-fork collaboration.
  - Email to somdipto: ask for warm intro to Vignesh or Hexo Labs contacts if any.

- **v10 month 2 (July 2026):**
  - If Hexo responds: sign collaboration agreement. Plan joint benchmark (COCO Captions subset, 500-pair held-out).
  - If Hexo does not respond: fork unilaterally per v9 plan.

- **v10 month 3-10 (August 2026 - March 2027):**
  - v10 month 3: fork SIA. Replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B. Run on 100-pair.
  - v10 month 4: scale to 500-pair held-out. Compare to Hexo reference. Co-publish delta.
  - v10 month 5: SIA fork v0.5. Harness-only loop on danlab-multimodal. **Co-publish with Hexo.**
  - v10 month 8: SIA fork v0.9. Held-out LawBench reproduction. **Co-publish with Hexo/Stanford.**
  - v10 month 10: SIA fork v1.0. Harness + weights. Brake-pedal-aligned. **Co-publish with Hexo/Stanford.**

### 3.2 v10 collaboration value

If collaboration succeeds:
- Joint benchmark design (Hexo's experience + our danlab-multimodal dataset).
- Joint publication (Stanford academic credibility + Hexo + Danlab).
- Possible Stanford hosting of the SIA fork (academic sustainability).
- Joint credibility for AGI positioning.

If collaboration fails:
- We fork unilaterally per v9 plan.
- Timeline slip: 3-6 months.
- Lost value: ~30% of the above.

**v10 verdict:** outreach has high upside, low downside. Do it this week.

## 4. v10 privacyd (P0, ARCHITECTURAL NEW — three attestations)

### 4.1 Three compliance attestations (v10 NEW)

**v9 had:** privacyd v1.0 = netns + cgroup + seccomp + audit log + /test endpoint.
**v10 adds:** three compliance attestation endpoints, each backed by the same audit log:

1. **`GET /privacy/fable5-safe`** — returns `{"compliant": true, "evidence": [...], "last_audit": "..."}`.
   - Evidence: no outbound calls to known frontier LLM providers (api.anthropic.com, api.openai.com, generativelanguage.googleapis.com).
   - Evidence: no outbound calls to US-supply-chain-risk-flagged domains.
   - Evidence: every outbound call is to the privacyd allowlist (telegram.org, api.zo.computer).

2. **`GET /privacy/eu-ai-act`** — returns `{"compliant": true, "evidence": [...], "last_audit": "..."}`.
   - Evidence: on-device model registry (every model loaded from allowlist, not from web).
   - Evidence: audit log of model invocations (transparency requirement).
   - Evidence: human-oversight hooks (user can disable any service).

3. **`GET /privacy/dpdp-act`** — returns `{"compliant": true, "evidence": [...], "last_audit": "..."}`.
   - Evidence: no data leaves the device (all outbound calls are to allowlist).
   - Evidence: data-localization (no cross-border data transfer).
   - Evidence: consent and breach-notification hooks (privacyd can flush all data on demand).

### 4.2 v10 privacyd timeline (no change from v9)

- **v10 month 2 (July 2026):** privacyd v0.5. netns + cgroup + seccomp. Allowlist.
- **v10 month 4 (September 2026):** privacyd v1.0. Audit log. /test endpoint. CI integration. **Three compliance attestation endpoints.**
- **v10 month 6 (November 2026):** privacyd v1.0 ships with v1.0. Public compliance doc.

## 5. v10 Service Failure Cascade Contract (v9 carryforward, validated)

The v9 contracts stand. No v10 changes.

## 6. v10 Power State Machine (v9 carryforward, P0 for v1)

The v9 power states stand. No v10 changes.

## 7. v10 OpenClaw Security (P0, Fable 5 aligned)

### 7.1 v9 carryforward (no change)

The v9 P0 actions stand:
1. Pin OpenClaw to ≥ 2026.5.x.
2. `policy.deny_skills: ["*"]`.
3. Audit installed skills against Trail-of-Bits patterns.
4. Supervisord restart policy.
5. Audit Telegram channel config.

### 7.2 v10 Fable 5 hardening (NEW)

**The trigger:** DoD Under Secretary (CNBC, June 17, 2026) called Anthropic a "supply chain risk." Fable 5 / Mythos 5 still offline.

**v10 implication for OpenClaw:** OpenClaw is a TypeScript/Node runtime. It is not a frontier LLM. The exposure:
- `zo-bridge` calls `api.zo.computer/zo/ask`. Is `api.zo.computer` a "frontier LLM provider"? **NO** — Zo uses our M3 model (MiniMax M3). It is not a frontier model. It is not subject to the Fable 5 directive.
- Telegram is fine — Telegram is the channel, not the model.

**v10 verdict:** OpenClaw security is P0. The DoD-Anthropic trigger is a *marketing* trigger, not an *engineering* trigger. Our OpenClaw deployment is already DoD-Anthropic-safe because Zo's model is not a frontier model.

**v10 action:** Document the call graph: openclaw → zo-bridge → api.zo.computer → M3. Document the audit log. Document: no frontier-frontier LLM dependency. Run `dan-privacyd --test fable5-safe` from the bootstrap wizard.

## 8. v10 Open Questions for the User (somdipto)

The v10 research surfaced questions that need user input:

1. **Wearable v2 form factor:** confirm "NO HUD" decision. Recommendation: yes, NO HUD. Compete on trust, not hardware.
2. **SIA collaboration outreach:** can somdipto intro to Vignesh Baskaran or Hexo Labs via LinkedIn? If yes, the collaboration accelerates. If no, we fork unilaterally.
3. **Dev kit pricing for v1:** free (Apache 2.0) vs $99 paid support tier vs $499 "Pro" tier with model bundle. Recommendation: free + optional paid support. Maximize adoption.
4. **Wearable v2 BOM target:** $400 (commodity) vs $300 (aggressive) vs $500 (premium). Recommendation: $400. Undercut Meta Display by 2x.
5. **v1 ship target:** Q4 2026 (aggressive, beats Meta Display launch + Apple-window head start) vs Q1 2027 (safer) vs Q2 2027 (loses Meta Display window). Recommendation: Q4 2026. The window is real.
6. **Meta Display response strategy:** ignore it, copy some features (e.g., bone conduction audio — v10 already adds this), or position against it explicitly. Recommendation: position against it explicitly. The "Fable 5 safe + open-source + on-device" pitch is *anti-Meta*.

## 9. v10 Final Read

The v9 architecture is correct. v10 makes four concrete changes:

1. **Wearable v2 = NO HUD.** Compete on trust architecture, not hardware.
2. **SIA fork = collaboration with Hexo/Stanford.** Outreach this week.
3. **privacyd publishes three compliance attestations.** Fable 5 safe, EU AI Act aligned, DPDP Act aligned.
4. **10-service topology locked.** No new services in v10. The v10 work is integration + ship.

The v10 moat: open-source + on-device + auditable + Fable 5 safe + EU-AI-Act-aligned + DPDP-Act-aligned + US-supply-chain-risk-aligned + NO-HUD (intentional, anti-Meta race).

Build. Ship. Don't chase the HUD.

---

*End of v10 architecture review. Total: ~240 lines / ~14KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-model-analysis.md` (model selection), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read). v9 archived as `dan2-architecture-review.v9.md`.*
