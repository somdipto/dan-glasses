# Dan2 — AGI Roadmap v9
## 6 / 12 / 24 Month Plan with the Fable 5 / Apple Window Delta

**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v9. v8 archived as `dan2-agi-roadmap.v8.md`.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

## 0. v9 Read in 60 Seconds

The v8 AGI roadmap is correct in structure. v9 changes three things:

1. **Apple-window kickoff is moved forward to v9 month 1 (this month, June 2026).** With Apple N50 confirmed for late 2027 (Bloomberg, June 16 2026), the 18-month head start is real but the v1.0 must ship credible by Q4 2026 / Q1 2027. v9 puts the marketing + community + early-access prep in v9 month 1.
2. **privacyd is moved into v9 month 2 (was v9 month 3 in v8).** The Fable 5 / Mythos 5 export-control suspension (June 12 2026) makes privacyd the *first* new service to ship, not the second. The "Fable 5 test" is the v1.0 marketing claim.
3. **Stanford SIA team outreach is in v9 month 1 (was v9 month 3 in v8).** The Stanford SIA release (per v9 research) and the Anthropic brake-pedal memo together make the next 90 days critical for the self-improvement work. Outreach now, not in 90 days.

The v9 timeline:

- **6 months (Q4 2026):** ship Dan Glasses v1.0. 7 services + privacyd. Fable 5 safe. Open-source. Apple-window kickoff.
- **12 months (Q1-Q2 2027):** ship Dan Glasses v1.1. + reasond + proactived. + VLCache + LFM2.5-VL-1.6B-Extract. Memoryd v2 (13-typed). Stanford SIA fork v0.5.
- **24 months (Q3 2027 - Q2 2028):** ship Dan Glasses v2. + Redax aarch64 wearable. + SIA v1.0 with held-out generalization. + Omni-Embed-Mini memoryd. Pre-AGI product.

---

## 1. The v9 6-Month Plan (June 2026 - November 2026, ship v1.0)

### Month 1 (June 2026) — Foundation + Scaffolding

**Goal:** ship-ready architecture + Stanford SIA outreach + privacyd design.

- [ ] **Dan1:** OpenClaw pin to ≥ 2026.5.x + `policy.deny_skills: ["*"]` + supervisord restart. (This week.)
- [ ] **Dan1:** OpenClaw installed-skill audit against Trail-of-Bits patterns. (This week.)
- [ ] **Dan1+Dan2:** Write `docs/privacy-threat-model.md` v0.5. (This week.)
- [ ] **Dan1+Dan2:** Write `docs/privacyd-design.md` v0.5. (This week.)
- [ ] **Dan2:** Stanford SIA outreach email. (This week.)
- [ ] **Dan2:** Apple-window positioning post draft. (Next week.)
- [ ] **Dan2:** Vendor LFM2.5-VL-450M, KittenTTS, MiniLM in `models/`. (This week.)
- [ ] **Dan2:** Verify LFM2.5-VL-450M and KittenTTS licenses. Document in `docs/model-licenses.md`. (This week.)
- [ ] **Dan2:** Create `shared/` Rust crate with serde structs for the 7 service types. (This month.)
- [ ] **Dan1+Dan2:** Apple N50 + Fable 5 product brief. (This month.)

### Month 2 (July 2026) — privacyd v0.5 + wake-word + memoryd v2 design

- [ ] **Dan1+Dan2:** privacyd v0.5 running. netns + cgroup + seccomp. Allowlist (telegram.org, api.zo.computer). Port 8748.
- [ ] **Dan2:** Wake-word for audiod (v0.5). PicoVoice Porcupine or open-source alternative.
- [ ] **Dan2:** memoryd v2 design. 13-typed-schema. Local classifier (Gemma 4 1B + heuristic).
- [ ] **Dan3:** LFM2.5-VL-450M benchmark on x86_64 (perceptiond latency profile).
- [ ] **Dan3:** Salience threshold tuning (perceptiond).
- [ ] **Dan4:** TTS streaming (chunked response) for long-form speech.

### Month 3 (August 2026) — VLCache + LFM 1.6B benchmark + memoryd v2

- [ ] **Dan3:** Integrate VLCache in perceptiond. Target: 5-8s/frame (down from 10-15s).
- [ ] **Dan3:** Benchmark LFM2.5-VL-1.6B-Extract on x86_64. Decide v1.1 swap.
- [ ] **Dan2:** memoryd v2 implementation. 13-typed schema. Local classifier.
- [ ] **Dan1:** Debian .deb package. systemd units for all 7 services + privacyd.
- [ ] **Dan2:** Stanford SIA discussion (if Hexo Labs / Oxford responds).

### Month 4 (September 2026) — reasond + memoryd v2 + wake-word

- [ ] **Dan2:** reasond v0.5. HRM-Text 1B integration. Port 8745.
- [ ] **Dan2:** memoryd v2 ship. Dual-write migration. Backwards compat for v1.
- [ ] **Dan2:** audiod v0.5 with wake-word gated behind user opt-in.
- [ ] **Dan4:** Benchmark Moonshine + Kokoro on real audiod + ttsd workloads.
- [ ] **Dan3:** perceptiond v1.1. LFM 1.6B-Extract as "pro" mode.

### Month 5 (October 2026) — proactived v0.5 + SIA fork

- [ ] **Dan2:** proactived v0.5. Port 8746. Hand-coded readiness rules. Reasoner hook.
- [ ] **Dan2:** Fork SIA. Replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B.
- [ ] **Dan1:** Bootstrap wizard v3. Privacyd status visible. Fable 5 test runner.
- [ ] **Dan1:** Tauri app v1.0.0-rc.1. All 8 services (7 + privacyd) integrated.

### Month 6 (November 2026) — v1.0 Ship

- [ ] **Dan1:** v1.0.0 release. Open-source on GitHub.
- [ ] **Dan1+Dan2:** Public "Fable 5 safe" attestation doc. Privacy threat model.
- [ ] **Dan2:** HackerNews post + ProductHunt post.
- [ ] **Dan2:** Apple-window positioning piece (blog, X, LinkedIn).
- [ ] **Dan3:** perceptiond v1.0.0. VLCache + LFM 1.6B-Extract.
- [ ] **Dan4:** ttsd v1.0.0. memoryd v2 ship.
- [ ] **Dan2:** toold v1.0.0. 50+ tools in registry (shell, python, file, git, http, fs).
- [ ] **Dan1:** debian .deb signed. Release on GitHub Releases.

**v1.0 acceptance criteria:**
- [ ] 7 services + privacyd all live, all tests pass.
- [ ] end-to-end push-to-talk voice → response via TTS <3s.
- [ ] end-to-end camera frame → VLM → description <1s.
- [ ] Memoryd v2 (13-typed) operational. <50ms p95 query.
- [ ] Fable 5 test passes (privacyd --test).
- [ ] OpenClaw ≥ 2026.5.x, deny_skills, no exploits.
- [ ] .deb installs cleanly. Systemd units active. Service health contracts honored.
- [ ] 100/100 tests pass.
- [ ] Privacy threat model + "Fable 5 safe" doc public.

---

## 2. The v9 12-Month Plan (Q4 2026 - Q4 2027, ship v1.1)

### Months 7-9 (December 2026 - February 2027) — v1.1 Scaffolding

- [ ] **Dan3:** reasond v1.0. HRM-Text 1B + Gemma 4 1B.
- [ ] **Dan3:** proactived v1.0. StreamReady-style readiness scorer. Reasoner hook.
- [ ] **Dan2:** SIA fork v0.5. Harness-only loop on danlab-multimodal. LawBench reproduction.
- [ ] **Dan1:** Redax aarch64 build (if hardware lands) OR alternative chip evaluation.
- [ ] **Dan4:** Wake-word general availability. Always-listening (with opt-in).
- [ ] **Dan2:** privacyd v1.0. Audit log. /test endpoint. CI integration.
- [ ] **Dan2:** Memoryd v2 visual memory hooks. Perceptiond → memoryd typed visual record.

### Months 10-12 (March - May 2027) — v1.1 Polish

- [ ] **Dan3:** perceptiond v1.1. LFM 1.6B-Extract default. VLCache + V5e-0.
- [ ] **Dan4:** audiod v1.1. whisper.cpp multilingual (Hindi, Spanish, Mandarin). Moonshine as "fast" mode.
- [ ] **Dan4:** ttsd v1.1. Kokoro as alternative. Streaming (chunked response).
- [ ] **Dan2:** SIA fork v1.0. Harness + weights. Held-out generalization (LawBench + HumanEval + LongMemEval).
- [ ] **Dan1:** v1.1.0 release. Redax build (if available). Wearable form factor (if available).
- [ ] **Dan2:** Apple-window + Apple N50 (late 2027 ship) positioning piece.

**v1.1 acceptance criteria:**
- [ ] reasond integrated. HRM-Text 1B inference <5s/response.
- [ ] proactived integrated. <1 false positive per hour.
- [ ] SIA fork v1.0 reproduces LawBench 70.1% or better.
- [ ] Redax aarch64 build (or alternative) works for all 9 services.
- [ ] 200/200 tests pass.
- [ ] Public SIA fork on GitHub (Apache 2.0).

---

## 3. The v9 24-Month Plan (Q4 2026 - Q3 2028, ship v2)

### Year 2 (Q2 2027 - Q1 2028) — v2 Build

- [ ] **Dan3:** perceptiond v2. Distilled VLM (Omni-Embed-Mini-style). NPU acceleration.
- [ ] **Dan4:** audiod v2. Streaming Parakeet or Universal-1 (cloud fallback only with opt-in).
- [ ] **Dan4:** ttsd v2. Coqui XTTS v2 voice cloning. "Dan in your own voice."
- [ ] **Dan2:** memoryd v3. Omni-Embed-Mini integration. Index/query decoupling (NanoVDR-style). <50ms on 1M memory corpus.
- [ ] **Dan2:** SIA v2. Harness + weights with safety case. Brake-pedal-aligned.
- [ ] **Dan1:** Redax aarch64 wearable form factor. <50g. 4h battery. Privacy threat model validated.
- [ ] **Dan2:** Pre-AGI product. "Dan v2" — the on-device AI companion that learns from you.

### Year 2.5-3 (Q1 2028 - Q3 2028) — v2 Ship + AGI Roadmap Re-evaluation

- [ ] **Dan1:** v2.0.0 release. Wearable. Redax aarch64. Fable 5 safe.
- [ ] **Dan2:** Public SIA paper. "Honest harness + weights self-improvement for a $1K training budget."
- [ ] **Dan2:** AGI roadmap v3. Beyond the wearable.
- [ ] **Dan2:** Frontier watch. If Anthropic Mythos 5 / Fable 5 re-enabled, re-evaluate architecture.
- [ ] **Dan2:** India launch. DPDP Act compliance.

**v2 acceptance criteria:**
- [ ] Redax aarch64 wearable shipping. <50g. 4h battery. Fable 5 safe.
- [ ] SIA v2.0 with held-out generalization. Brake-pedal-aligned.
- [ ] On-device memoryd v3. 1M memory corpus. <50ms query.
- [ ] On-device Coqui XTTS v2 voice cloning. "Dan in your own voice."
- [ ] 500/500 tests pass.
- [ ] Public AGI roadmap v3. Beyond the wearable.

---

## 4. The v9 Apple Window (Q4 2026 Ship Target)

### 4.1 The Window (v9 verification)

| Date | Event | Implication for Dan Glasses |
|---|---|---|
| 2026-09 | AWE 2026 (per v9 web research, The Gadgeteer) | Demo v1.0-rc.1. Get developer feedback. |
| 2026-Q4 | Google Gemini glasses (Warby Parker, Gentle Monster) ship | Direct comp. Our moat: open-source + on-device. |
| 2026-11 | Dan Glasses v1.0 ships (per v9 plan) | Our ship date. |
| 2027-Q1 | Google/Samsung Android XR display version | Apple/Samsung/Meta all in market. Our moat: open-source + on-device + Fable 5 safe. |
| 2027-Q3 | Apple N50 announcement (rumored) | Apple commits to 2027 ship. |
| 2027-Q4 | Apple N50 ships (Bloomberg) | Market closes for new entrants. |

**v9 window math:** 12-18 month head start over Apple N50. v1.0 must ship credible by Q4 2026 to be in market before Apple. v1.1 in Q2 2027 establishes the moat before Apple N50.

### 4.2 v9 Apple-Window Positioning

**Public claim (Q4 2026 launch):**
> "Dan Glasses is the open-source AI companion for your face. Every model runs on the device. No cloud. No tracking. No jailbreak surface. We passed the Fable 5 test."

**Differentiation:**
- **vs Meta Ray-Ban (cloud):** open-source + on-device + auditable.
- **vs Google Gemini glasses (cloud):** open-source + on-device + Fable 5 safe.
- **vs Apple N50 (cloud-dependent):** open-source + on-device + auditable + India-first.
- **vs Brilliant Labs Frame (BYO model):** we ship the model stack + memory + reasoning; they ship the hardware.

**Channels (Q4 2026):**
- HackerNews "Show HN" with privacyd + Apple-window positioning.
- ProductHunt launch.
- X thread: "Why we built the Fable 5 safe AI companion."
- LinkedIn long-form: "On-device + auditable + open-weights. The moat vs Meta + Google + Apple."
- GitHub README: install, contribute, customize.
- India-first: Bangalore / Delhi / Mumbai meetups. DPDP Act compliance.

---

## 5. The v9 Fable 5 Window (privacyd + on-device moat)

### 5.1 The Fable 5 trigger

The Anthropic Fable 5 / Mythos 5 export-control suspension (June 12 2026) made one thing clear: any cloud-frontier LLM is a fragile dependency. The "jailbreak" cited was "widely available in other models (including OpenAI's GPT-5.5)."

**v9 implication:** frontier models in the cloud are a moving target. On-device + open-weights + auditable is the stable target. We are already there.

### 5.2 v9 Fable 5 safe marketing claim

> "Dan Glasses v1.0 is the only AI companion that has passed the Fable 5 test. Every model runs on the device. Every outbound call is logged and audited. You can verify with `dan-privacyd --test`."

This claim is verifiable by the user. It is a strong, defensible, auditable claim. It positions Dan Glasses against every cloud-LLM competitor.

### 5.3 v9 privacyd timeline (moved forward from v8)

- v9 month 2 (July 2026): privacyd v0.5. netns + cgroup + seccomp.
- v9 month 4 (September 2026): privacyd v1.0. Audit log. /test endpoint. CI.
- v9 month 6 (November 2026): privacyd v1.0 ships with v1.0. Public "Fable 5 safe" doc.

---

## 6. The v9 Self-Improvement Plan (SIA + memoryd v2)

### 6.1 v9 SIA fork timeline

- v9 month 1 (June 2026): Stanford SIA outreach.
- v9 month 3 (August 2026): Fork SIA. Replace Feedback-Agent.
- v9 month 5 (October 2026): SIA fork v0.5. Harness-only loop on danlab-multimodal.
- v9 month 8 (January 2027): SIA fork v0.9. Held-out LawBench reproduction.
- v9 month 10 (March 2027): SIA fork v1.0. Harness + weights. Brake-pedal-aligned.
- v9 month 18 (December 2027): SIA v2.0 with safety case. Public paper.

### 6.2 v9 memoryd v2 timeline

- v9 month 2 (July 2026): memoryd v2 design. 13-typed schema.
- v9 month 3 (August 2026): memoryd v2 implementation.
- v9 month 4 (September 2026): memoryd v2 ship. Dual-write migration.
- v9 month 7 (December 2026): memoryd v2.5. Graph fallback. Compression.
- v9 month 12 (May 2027): memoryd v3. Omni-Embed-Mini integration.

### 6.3 v9 reasond timeline

- v9 month 1 (June 2026): HRM-Text 1B license + inference code review.
- v9 month 4 (September 2026): reasond v0.5. HRM-Text 1B + Gemma 4 1B.
- v9 month 6 (November 2026): reasond v1.0 ships with v1.0.
- v9 month 7-9 (December 2026 - February 2027): reasond v1.1. Tuned for wearable form factor.

---

## 7. The v9 Final Read

The v8 AGI roadmap is correct in structure. v9 changes three things to compress the timeline:

1. **Apple-window kickoff moved to v9 month 1.** The 12-18 month head start is real.
2. **privacyd moved to v9 month 2.** The Fable 5 test is the v1.0 marketing claim.
3. **Stanford SIA outreach in v9 month 1.** The next 90 days are critical for self-improvement work.

The v9 timeline:
- **6 months:** v1.0 ships. Fable 5 safe. Open-source.
- **12 months:** v1.1 ships. SIA v0.5. Redax build (if hardware).
- **24 months:** v2 ships. Wearable. SIA v1.0. Pre-AGI.

The moat: on-device + auditable + open-weights + Fable 5 safe. The window: Q4 2026 - Q4 2027 before Apple N50.

Build.

---

*End of v9 AGI roadmap. Total: ~270 lines / ~17KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-architecture-review.md` (the architectural fix list), `dan2-model-analysis.md` (model selection), `dan2-papers-to-read.md` (what to read). v8 archived as `dan2-agi-roadmap.v8.md`.*
