# Dan2 — AGI Roadmap v10
## 6 / 12 / 24 Month Plan with Meta Display Comp + SIA Collaboration + HUD Decision

**Date:** 2026-06-18 07:30 IST (02:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v10. v9 archived as `dan2-agi-roadmap.v9.md`.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

## 0. v10 Read in 90 Seconds

The v9 AGI roadmap is correct in structure. v10 changes four things based on data from the last 1-12 hours:

1. **Apple-window compressed to ~14 months.** Meta Display ships Sept 30, 2026 (not Apple's N50 in 18 months). Apple-window is now "before Meta Display + Apple N50 general availability." That's Q4 2026.
2. **SIA fork is now a collaboration, not a unilateral fork.** Contact Vignesh Baskaran (LinkedIn/Stanford Salone d'Onore, June 2026). Plan co-fork + co-publication.
3. **Wearable v2 form factor = NO HUD.** $400 BOM. Bone-conduction audio. Compete on trust, not hardware.
4. **Three compliance attestations:** privacyd publishes Fable 5 safe, EU AI Act aligned, DPDP Act aligned. Each is a separate `/privacy/<claim>` endpoint.

The v10 timeline:
- **6 months (Q4 2026):** ship Dan Glasses v1.0. 7 services + privacyd. Fable 5 safe. EU AI Act aligned. DPDP Act aligned. Open-source. **Ship the month Meta Display ships.**
- **12 months (Q1-Q2 2027):** ship Dan Glasses v1.1. + reasond + proactived. + VLCache + LFM2.5-VL-1.6B-Extract. Memoryd v2 (13-typed). SIA fork v0.9 (co-published).
- **24 months (Q3 2027 - Q2 2028):** ship Dan Glasses v2. + NO-HUD wearable. + SIA v1.0. + Omni-Embed-Mini memoryd. + India localization. Pre-AGI product.

## 1. The v10 6-Month Plan (June 2026 - November 2026, ship v1.0)

### Month 1 (June 2026) — Foundation + Scaffolding + SIA Collaboration

**Goal:** ship-ready architecture + Stanford SIA outreach + privacyd design + wearable v2 form-factor decision.

- [ ] **Dan1:** OpenClaw pin to ≥ 2026.5.x + `policy.deny_skills: ["*"]` + supervisord restart. (This week.)
- [ ] **Dan1:** OpenClaw installed-skill audit against Trail-of-Bits patterns. (This week.)
- [ ] **Dan1+Dan2:** Write `docs/privacy-threat-model.md` v0.5. (This week.)
- [ ] **Dan1+Dan2:** Write `docs/privacyd-design.md` v0.5 with three compliance attestations. (This week.)
- [ ] **Dan1+Dan2:** Write `docs/v2-form-factor.md` v0.5 — NO HUD decision, BOM target $400. (This week.)
- [ ] **Dan2:** LinkedIn outreach to Vignesh Baskaran (Hexo Labs, Stanford Salone d'Onore). GitHub issue on HexoLabs/SIA. (This week.)
- [ ] **Dan2:** Ask somdipto for warm intro to Vignesh or Hexo Labs if possible. (This week.)
- [ ] **Dan2:** Meta Display positioning post draft. "We don't chase the HUD. We chase the audit log." (This week.)
- [ ] **Dan2:** Apple N50 + Fable 5 product brief. (This month.)
- [ ] **Dan2:** Vendor LFM2.5-VL-450M, KittenTTS, MiniLM in `models/`. Verify licenses. Document in `docs/model-licenses.md`. (This week.)
- [ ] **Dan2:** Create `shared/` Rust crate with serde structs for the 7 service types. (This month.)

### Month 2 (July 2026) — privacyd v0.5 + SIA fork + wake-word + memoryd v2 design

- [ ] **Dan1+Dan2:** privacyd v0.5 running. netns + cgroup + seccomp. Allowlist (telegram.org, api.zo.computer). Port 8748.
- [ ] **Dan2:** SIA fork v0.1. Thin wrapper around HexoLabs/SIA. Replace Feedback-Agent placeholder. (If collaboration succeeds, this is co-developed; if not, unilateral fork per v9.)
- [ ] **Dan2:** Wake-word for audiod (v0.5). openWakeWord or PicoVoice Porcupine.
- [ ] **Dan2:** memoryd v2 design. 13-typed-schema. Local classifier (Gemma 4 1B + heuristic).
- [ ] **Dan3:** LFM2.5-VL-450M benchmark on x86_64 (perceptiond latency profile, full).
- [ ] **Dan3:** Salience threshold tuning (perceptiond).
- [ ] **Dan4:** TTS streaming (chunked response) for long-form speech.
- [ ] **Dan2:** Compar draft — Meta Display vs Dan Glasses v1.0. Publish as blog post / X thread.

### Month 3 (August 2026) — VLCache + LFM 1.6B benchmark + memoryd v2

- [ ] **Dan3:** Integrate VLCache in perceptiond. Target: 5-8s/frame (down from 10-15s).
- [ ] **Dan3:** Benchmark LFM2.5-VL-1.6B-Extract on x86_64.
- [ ] **Dan2:** memoryd v2 implementation. 13-typed schema. Local classifier.
- [ ] **Dan1:** Debian .deb package. systemd units for all 7 services + privacyd.
- [ ] **Dan2:** SIA fork v0.3 (if not done in month 2). Run on danlab-multimodal 100-pair held-out.

### Month 4 (September 2026) — reasond + memoryd v2 + wake-word + Meta Display launch response

- [ ] **Dan2:** reasond v0.5. HRM-Text 1B integration. Port 8745.
- [ ] **Dan2:** memoryd v2 ship. Dual-write migration. Backwards compat for v1.
- [ ] **Dan2:** audiod v0.5 with wake-word gated behind user opt-in.
- [ ] **Dan4:** Benchmark Moonshine + Kokoro on real audiod + ttsd workloads.
- [ ] **Dan3:** perceptiond v1.1. LFM 1.6B-Extract as "pro" mode.
- [ ] **Dan2:** SIA fork v0.5. Harness-only loop on danlab-multimodal. Day-1 of Meta Display launch.

### Month 5 (October 2026) — proactived v0.5 + SIA v0.5 + Meta Display launch response

- [ ] **Dan2:** proactived v0.5. Port 8746. Hand-coded readiness rules. Reasoner hook.
- [ ] **Dan2:** SIA fork v0.5 publication (draft). Co-publish with Hexo/Stanford if collaboration succeeded.
- [ ] **Dan1:** Bootstrap wizard v3. Privacyd status visible. Fable 5 test runner.
- [ ] **Dan1:** Tauri app v1.0.0-rc.1. All 8 services (7 + privacyd) integrated.
- [ ] **Dan2:** "Fable 5 + EU AI Act + DPDP Act" compliance doc publication.

### Month 6 (November 2026) — v1.0 Ship (right around Meta Display launch)

- [ ] **Dan1:** v1.0.0 release. Open-source on GitHub.
- [ ] **Dan1+Dan2:** Public compliance doc: "Fable 5 safe + EU AI Act aligned + DPDP Act aligned."
- [ ] **Dan2:** HackerNews post + ProductHunt post. *"Dan Glasses: the AI companion that has passed the Fable 5 test."*
- [ ] **Dan2:** Meta Display compar post. *"Why we don't ship a HUD."*
- [ ] **Dan3:** perceptiond v1.0.0. VLCache + LFM 1.6B-Extract.
- [ ] **Dan4:** ttsd v1.0.0. memoryd v2 ship.
- [ ] **Dan2:** toold v1.0.0. 50+ tools in registry.
- [ ] **Dan1:** debian .deb signed. Release on GitHub Releases.
- [ ] **Dan2:** India launch. DPDP Act compliance doc in Hindi + English.

**v1.0 acceptance criteria:**
- [ ] 7 services + privacyd all live, all tests pass.
- [ ] end-to-end push-to-talk voice → response via TTS <3s.
- [ ] end-to-end camera frame → VLM → description <1s.
- [ ] Memoryd v2 (13-typed) operational. <50ms p95 query.
- [ ] Fable 5 test passes (privacyd --test fable5-safe).
- [ ] EU AI Act test passes (privacyd --test eu-ai-act).
- [ ] DPDP Act test passes (privacyd --test dpdp-act).
- [ ] OpenClaw ≥ 2026.5.x, deny_skills, no exploits.
- [ ] .deb installs cleanly. Systemd units active.
- [ ] 100/100 tests pass.
- [ ] Public compliance doc + "Fable 5 safe" attestation.

## 2. The v10 12-Month Plan (Q4 2026 - Q4 2027, ship v1.1)

### Months 7-9 (December 2026 - February 2027) — v1.1 Scaffolding

- [ ] **Dan3:** reasond v1.0. HRM-Text 1B + Gemma 4 1B.
- [ ] **Dan3:** proactived v1.0. StreamReady-style readiness scorer. Reasoner hook.
- [ ] **Dan2:** SIA fork v0.9. Held-out LawBench reproduction. **Co-publish with Hexo/Stanford.**
- [ ] **Dan1:** Redax aarch64 build (if hardware lands) OR alternative chip evaluation.
- [ ] **Dan4:** openWakeWord general availability. Always-listening (with opt-in).
- [ ] **Dan2:** privacyd v1.0. Audit log. /test endpoint. CI integration.

### Months 10-12 (March - May 2027) — v1.1 Polish + Apple N50 pre-launch response

- [ ] **Dan3:** perceptiond v1.1. LFM 1.6B-Extract default. VLCache + V5e-0.
- [ ] **Dan4:** audiod v1.1. whisper.cpp multilingual (Hindi, Spanish, Mandarin). Moonshine as "fast" mode.
- [ ] **Dan4:** ttsd v1.1. Kokoro as alternative. Streaming.
- [ ] **Dan2:** SIA fork v1.0. Harness + weights. Brake-pedal-aligned. **Co-publish with Hexo/Stanford.**
- [ ] **Dan1:** v1.1.0 release. Redax build (if available).
- [ ] **Dan2:** Apple N50 (late 2027 ship) positioning piece.

**v1.1 acceptance criteria:**
- [ ] reasond integrated. HRM-Text 1B inference <5s/response.
- [ ] proactived integrated. <1 false positive per hour.
- [ ] SIA fork v1.0 reproduces LawBench 70.1% or better.
- [ ] Redax aarch64 build (or alternative) works for all 9 services.
- [ ] 200/200 tests pass.
- [ ] Public SIA fork on GitHub (Apache 2.0) co-published.
- [ ] India: Hindi fine-tuned LFM2.5-1.2B-JP-202606 benchmark complete.

## 3. The v10 24-Month Plan (Q4 2026 - Q3 2028, ship v2)

### Year 2 (Q2 2027 - Q1 2028) — v2 Build (NO HUD wearable)

- [ ] **Dan3:** perceptiond v2. LFM2.5-VL-1.6B default. NPU acceleration on Redax.
- [ ] **Dan4:** audiod v2. openWakeWord + Moonshine + multilingual.
- [ ] **Dan4:** ttsd v2. Coqui XTTS v2 voice cloning. "Dan in your own voice."
- [ ] **Dan2:** memoryd v3. Omni-Embed-Mini integration. 1M corpus. <50ms query.
- [ ] **Dan2:** SIA v2. Harness + weights with safety case. Brake-pedal-aligned.
- [ ] **Dan1:** Redax aarch64 wearable. <50g. Bone-conduction audio. NO HUD. Privacyd validation.
- [ ] **Dan2:** Pre-AGI product. "Dan v2" — the on-device AI companion that learns from you.

### Year 2.5-3 (Q1 2028 - Q3 2028) — v2 Ship + AGI Roadmap Re-evaluation

- [ ] **Dan1:** v2.0.0 release. Wearable. Redax aarch64. Fable 5 safe.
- [ ] **Dan2:** Public SIA paper. "Honest harness + weights self-improvement for a $1K training budget."
- [ ] **Dan2:** AGI roadmap v3. Beyond the wearable.
- [ ] **Dan2:** Frontier watch. If Anthropic Mythos 5 / Fable 5 re-enabled, re-evaluate architecture.
- [ ] **Dan2:** India launch at scale. DPDP Act compliance validated at production scale.

**v2 acceptance criteria:**
- [ ] Redax aarch64 wearable shipping. <50g. NO HUD. Privacy LED. Fable 5 safe.
- [ ] SIA v2.0 with held-out generalization. Brake-pedal-aligned.
- [ ] On-device memoryd v3. 1M memory corpus. <50ms query.
- [ ] On-device Coqui XTTS v2 voice cloning. "Dan in your own voice."
- [ ] 500/500 tests pass.
- [ ] Public AGI roadmap v3. Beyond the wearable.

## 4. The v10 Meta Display Window (Q4 2026 Ship Target)

### 4.1 The Window (v10 verification)

| Date | Event | Implication for Dan Glasses |
|---|---|---|
| 2026-06 | Meta Lab @ Best Buy 50+ stores open | Meta marketing ramp. |
| 2026-09-30 | Meta Ray-Ban Display ships at $799 | The Meta Display launch. Our comp. |
| 2026-Q4 | Google Gemini glasses (Warby Parker, Gentle Monster) ship | Second comp. Open-source + on-device is our moat. |
| 2026-11 | Dan Glasses v1.0 ships (per v10 plan) | Our ship date. Same month as Meta Display launch. |
| 2027-Q1 | SIA fork v0.9 co-published with Hexo/Stanford | Our technical credibility milestone. |
| 2027-Q2 | Dan Glasses v1.1 ships | SIA v1.0 + reasond + proactived. |
| 2027-Q3 | Google Android XR display version | Apple/Samsung/Meta all in market. Our moat: open-source + on-device + Fable 5 safe. |
| 2027-Q4 | Apple N50 ships (Bloomberg) | Market closes for new entrants. |
| 2028-Q3 | Dan Glasses v2 ships | NO HUD wearable. SIA v2. Pre-AGI. |

**v10 window math:** v1.0 must ship credible in Nov 2026 to be in market before Apple N50 and alongside Meta Display. v1.1 in Q2 2027 establishes the moat before Apple N50.

### 4.2 v10 Meta Display Counter-Positioning

**Public claim (Q4 2026 launch, same month as Meta Display):**

> "Dan Glasses is the open-source AI companion dev kit for your laptop. We don't ship a HUD. We ship an audit log. Every model runs on the device. Every outbound call is logged. The user can verify with `dan-privacyd --test fable5-safe`. Try that with your Meta Ray-Ban Display."

**Differentiation from Meta Display:**
- **vs Meta Display (HUD + cloud):** open-source + on-device + auditable + no HUD (intentional) + no Meta AI.
- **vs Google Gemini glasses (cloud):** open-source + on-device + Fable 5 safe.
- **vs Apple N50 (cloud-dependent):** open-source + on-device + auditable + India-first.
- **vs Snap Specs (cloud):** open-source + on-device.

**Channels (Q4 2026, timed around Meta Display launch Sept 30):**
- HackerNews "Show HN" on Nov 1 (the day after Meta Display launch hype peaks). "Dan Glasses: open-source AI companion. No HUD. No Meta AI. Fable 5 safe."
- ProductHunt launch.
- X thread: "Meta Display ships today. We're shipping the opposite. Here's why."
- LinkedIn long-form: "On-device + auditable + open-weights + no HUD. The moat vs Meta + Google + Apple."
- Reddit r/LocalLLaMA, r/openclaw, r/MachineLearning posts.
- GitHub README: install, contribute, customize.
- India-first: Bangalore / Delhi / Mumbai meetups. DPDP Act compliance doc in Hindi + English.

## 5. The v10 SIA Collaboration Plan

### 5.1 Outreach (v10 month 1)

- [ ] LinkedIn message to Vignesh Baskaran (Hexo Labs presenter at Stanford, June 2026).
- [ ] GitHub issue on HexoLabs/SIA proposing co-fork + co-publication.
- [ ] Email to somdipto: ask for warm intro if any.
- [ ] Identify 1-2 other open-source SIA implementations (Stanford?) for parallel contact.

### 5.2 Collaboration agreement (if Hexo responds, v10 month 2)

- [ ] Joint benchmark design (COCO Captions subset, 500-pair held-out).
- [ ] Joint publication venue (arXiv first; NeurIPS / ICML submission if quality is there).
- [ ] Credit structure: Danlab as co-author on SIA v1.0 + v2.0. Hexo retains SIA primary authorship.
- [ ] Fork strategy: Danlab fork is a *downstream* of Hexo, not a *competitor*. We contribute back.

### 5.3 SIA fork timeline (v10 LOCKED)

- v10 month 1 (June 2026): outreach.
- v10 month 2 (July 2026): sign collaboration (if Hexo responds). Plan joint benchmark.
- v10 month 3 (August 2026): fork SIA. Replace Feedback-Agent. Run on 100-pair.
- v10 month 4 (September 2026): scale to 500-pair. Compare to Hexo reference.
- v10 month 5 (October 2026): SIA fork v0.5. Harness-only loop. **Co-publish.**
- v10 month 8 (January 2027): SIA fork v0.9. Held-out LawBench reproduction. **Co-publish.**
- v10 month 10 (March 2027): SIA fork v1.0. Harness + weights. Brake-pedal-aligned. **Co-publish.**
- v10 month 18 (December 2027): SIA v2.0 with safety case. **Co-publish (paper).**

## 6. The v10 HUD Decision (NO HUD, LOCKED)

### 6.1 The decision

**v10 LOCKED:** Dan Glasses v2 wearable = camera + mic + bone-conduction audio. **NO HUD.**

**Why:**
1. Meta Display ships Sept 30, 2026 with HUD. The HUD race is Meta's race.
2. HUD requires expensive display optics. We cannot match Meta's $100B+ capex.
3. HUD does NOT align with our moat. Our moat is trust architecture, not hardware features.
4. Bone-conduction audio is enough for the wearable v2 use case.
5. The "no HUD" decision is *itself positioning*. It signals: we are not chasing Apple's Vision Pro race; we are chasing the trust category.

### 6.2 v10 wearable v2 BOM ($400 target)

| Component | Cost |
|---|---|
| Redax board (aarch64, 4GB/32GB) | $80-120 |
| Camera module (V4L2, 1080p) | $30-50 |
| MEMS mic array (2-mic, beam-forming) | $10-15 |
| Bone-conduction audio (temple-mounted) | $20-30 |
| Battery (LiPo, 600mAh, USB-C PD) | $15-25 |
| Frame + optics + assembly | $100-150 |
| Misc (PCB, passives) | $20-30 |
| **Total BOM** | **$275-420** |
| **Retail target** | **$400** |

### 6.3 v10 wearable v2 design constraints

- **Weight:** <50g.
- **Battery:** 4h continuous use (watchful mode).
- **Privacy:** hardwired LED that lights up whenever the camera is on (cannot be disabled in software).
- **No display:** intentional.
- **Bone conduction:** open-source alternatives to AfterShokz exist.

**v10 deliverable:** `docs/v2-form-factor.md` written in v10 month 1.

## 7. The v10 Three Compliance Attestations

### 7.1 The claims

- **Fable 5 safe:** no frontier API dependency. Verified by `privacyd --test fable5-safe`.
- **EU AI Act aligned:** on-device model registry + audit log + human-oversight hooks. Verified by `privacyd --test eu-ai-act`.
- **DPDP Act aligned:** no data leaves device + data localization + consent + breach-notification. Verified by `privacyd --test dpdp-act`.

### 7.2 The political alignment

v10 elevates these from marketing claims to *political positioning*:

- **US policy direction** (DoD "supply chain risk", Fable 5 export control) is *aligned* with our on-device thesis.
- **EU AI Act** is *aligned* with our auditable claim.
- **Indian DPDP Act** is *aligned* with our no-cloud-data claim.

**v10 message to somdipto:** the pitch to investors, governments, and partners is:

> "Dan Glasses is the only AI companion that is Fable-5-safe, EU-AI-Act-compliant, and DPDP-Act-compliant. Every model runs on the device. Every outbound call is logged. The user can verify with `dan-privacyd --test`. This is the AI companion the post-Fable-5 world needs."

This is a *policy-aligned* pitch. Policy-aligned pitches survive regulatory changes.

## 8. The v10 Final Read

The v9 AGI roadmap is correct in structure. v10 changes four things based on the last 1-12 hours:

1. **Apple-window compressed to ~14 months** because Meta Display ships Sept 30, 2026.
2. **SIA fork is a collaboration** with Hexo/Stanford (Vignesh Baskaran, LinkedIn-confirmed).
3. **Wearable v2 = NO HUD.** $400 BOM. Compete on trust.
4. **Three compliance attestations** in privacyd: Fable 5 safe, EU AI Act aligned, DPDP Act aligned.

The v10 timeline:
- **6 months:** v1.0 ships Nov 2026. Fable 5 safe. EU AI Act aligned. DPDP Act aligned. Open-source. Ship *with* Meta Display launch.
- **12 months:** v1.1 ships Q2 2027. SIA v1.0 co-publish.
- **24 months:** v2 ships Q3 2027 (NO HUD wearable). SIA v2.0 paper.

The moat: open-source + on-device + auditable + Fable 5 safe + EU AI Act aligned + DPDP Act aligned + US supply-chain-risk aligned + NO HUD (intentional).

Build. Ship. Don't chase the HUD.

---

*End of v10 AGI roadmap. Total: ~270 lines / ~17KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-architecture-review.md` (architectural fix list), `dan2-model-analysis.md` (model selection), `dan2-papers-to-read.md` (what to read). v9 archived as `dan2-agi-roadmap.v9.md`.*
