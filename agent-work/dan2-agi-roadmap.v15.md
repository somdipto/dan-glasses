# DAN-2 AGI Roadmap — v14
**Date:** 2026-06-19 (companion to `dan2-research-report.md`)
**Horizon:** 6 / 12 / 24 months
**Premise:** danlab.dev's path to AGI runs through **user-aligned recursive self-improvement on edge**. Not Anthropic-style frontier pre-training. Not DeepMind-style whole-stack AGI. **A wearable that learns the user, with the user, on the user's hardware.**

---

## Strategic frame

The AGI landscape in June 2026 has fractured into three narratives:

1. **Frontier pre-training** (OpenAI, Anthropic, Google DeepMind, Meta) — closed or semi-closed, $100M-$10B training runs, recursive self-improvement inside the lab. Anthropic's "When AI Builds Itself" (May 2026) and Jack Clark's public warnings frame RSI as the next inflection. Recursive Superintelligence Inc. raised $650M at $4.65B valuation. **This is not our category.**
2. **Open-weights flood** (Liquid AI, Zyphra, Hexo Labs, Z.ai, Mistral, Allen AI) — small specialized models, MIT or research-friendly licenses. SIA from Hexo Labs (May 2026) is the credible open-weights harness+weights self-improvement loop. Liquid AI shipped LFM2.5-VL-450M + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M in 60 days. **This is our category.**
3. **Edge AI / on-device-first** (Apple AFM, Qualcomm Snapdragon, MediaTek Dimensity, RISC-V A210) — sub-2W inference, on-device-first privacy story, $400 BOM niche. **This is where we ship.**

The bet, sharpened: **danlab.dev owns category 2+3 on the wearable form factor.** Open-weights self-improving AI on edge, $400 BOM, MIT stack, sub-50g, never phones home. The 14-month window before Apple N50 closes the trust-architecture narrative is *the* window.

---

## 6-month milestones (now → Dec 2026)

**Outcome target:** Ship v1.0 .deb with Mnemosyne + SIA-fork + signed-skill infra. Acquire first 100 power users.

### Month 1 (June 19 → July 19)

1. **Mnemosyne swap into memoryd.** `pip install mnemosyne-memory[openclaw]`, port memoryd HTTP surface, validate ≥98% Recall@All@5 on danlab-multimodal held-out set. **6-week workstream starting now.**
2. **SIA fork published.** GitHub fork of `hexo-ai/sia` as `danlab-ai/sia-fork`. Replace default Feedback-Agent with LFM2.5-1.2B-Thinking (MIT). Replace default target with SmolVLM-256M-on-danlab-multimodal. **Open-source launch with co-fork credit to Hexo Labs + Vignesh Baskaran.**
3. **OpenClaw signed-skill infra.** `cosign` sign every danlab OpenClaw skill, commit to Sigstore Rekor. Default-deny policy for unsigned. Document in `docs/openclaw-signed-skill-policy.md`. **3-day workstream. Blocks v1.0 .deb.**
4. **LinkedIn cold-DM to Vignesh Baskaran (Hexo Labs) + Tim Rocktaschel (RSI Inc.).** Open collaboration thread.
5. **Apple WWDC 2026 watch (September).** Apple N50 specs, AFM 3 roadmap, visionOS 27. **Adjust v1.5 plan based on what ships.**

### Month 2 (July 19 → Aug 19)

1. **`proactived` service shipped.** 2-week project. New daemon, subscribes to memoryd events + OpenClaw session. Hand-coded rules for "should I initiate?" Conservative defaults (≤1 proactive prompt/day, opt-in).
2. **Fable 5 compliance attestation in privacyd.** Document Fable-5-safe-by-construction. Wire `privacyd` → Sigstore Rekor for compliance attestation signing. Write `docs/fable-5-compliance-narrative.md`.
3. **HRM-Text 1B integration plan.** Read Sapient's blog/repo weekly. When inference code ships, start `reasond` service design.
4. **Zamba2-VL-1.2B benchmark on perceptiond workloads.** TTFT, quality on our held-out set, power estimate. 2-week project.
5. **Apple WWDC prep.** Read Apple's published research on on-device VLM, ATT, differential privacy. Position Dan Glasses as "the open alternative."

### Month 3 (Aug 19 → Sept 19)

1. **v1.0 .deb cut.** Mnemosyne + SIA-fork + proactived + privacyd + signed-skill infra all in. 131/131 + new tests.
2. **Dan Glasses Kit v0.1 (open-source release).** The wearable software stack as a standalone repo. MIT license. Targets dev community and OEM partners. **This is the moat.**
3. **Power characterization on Raspberry Pi 5 + AI HAT.** Proxy benchmark for Redax aarch64. Publish numbers publicly. Watts per component, TTFT at each quantization, salience-gated average power.

### Month 4-6 (Sept 19 → Dec 19)

1. **Acquisition: 100 power users.** Marketing-driven (per dan1 v63+ plan). danlab.dev landing page, Twitter thread cadence, danlab-multimodal demo public.
2. **LFM2.5-VL-1.6B-Extract integration.** Structured JSON output from perception → tool-calling → os-toold. v1.1 candidate.
3. **Distilled ProActor 1-2B prototype.** Train on user-interaction traces (anonymized, opt-in). Use SIA harness-only mode to optimize trigger classifier. **Open-source release.**
4. **v1.1 .deb.** LFM2.5-VL-1.6B-Extract, speculative decoding with SmolVLM-256M draft, F5-TTS streaming TTS, distilled ProActor.
5. **AWE 2027 talk proposal (submitted September).** "The first MIT wearable: 7 daemons, 0 cloud, sub-50g." (Carry-forward from dan1 v63.)

---

## 12-month milestones (Dec 2026 → June 2027)

**Outcome target:** v2 wearable hardware partner signed. SIA-fork v2 with reproducible harness+weights generalization numbers. 1,000 power users.

### Month 7-9 (Dec 2026 → Mar 2027)

1. **Wearable hardware partnership.** Lock form-factor envelope (weight, dimensions, temple/arm thickness, nose bridge fit). Pick a Redax-class aarch64 silicon partner. **This is a somdipto-led decision.**
2. **Power budget table for v2.** Measured watts per component on real Redax silicon (or Pi 5 proxy). Thermal envelope. Battery chemistry + capacity + placement.
3. **SIA-fork v2.** Reproducible held-out gains on LawBench-style task. Publish preprint "User-Aligned RSI via Wearable Feedback" on arXiv. **This is the credibility artifact for the AGI roadmap.**
4. **HRM-Text 1B in reasond.** When Sapient ships inference, integrate. Fallback to Gemma 3 1B.
5. **Apple N50 launch (late 2027 confirmed).** Compare trust architecture publicly. Our positioning: open weights, no cloud, no telemetry, auditable updates.

### Month 10-12 (Mar 2027 → June 2027)

1. **v2 wearable prototype.** First run on Redax silicon. Salience-gated vision, VAD-gated audio, Mnemosyne-backed memory, SIA-fork self-improvement, proactived layer.
2. **v2 power validation.** 4-hour battery target with mixed active/idle usage.
3. **Fable-5-safe B2B customer pipeline.** First 10 customers on `$99/$999` privacyd indemnity product. Anchor: enterprise customers who need a wearable AI that doesn't phone home.
4. **Dan Glasses Kit v1.0.** Open-source, MIT, installable on any aarch64 SBC with USB camera + mic + speaker. Becomes the reference open wearable AI stack.

---

## 24-month milestones (June 2027 → June 2028)

**Outcome target:** v2 wearable shipping. SIA-fork generalization demonstrated on a third-party benchmark. 10,000 power users. danlab.dev recognized as the open-weights wearable AI leader.

### Month 13-18 (June 2027 → Dec 2027)

1. **v2 wearable in production.** $400 BOM, sub-50g, MIT stack, SIA-fork self-improving on user data.
2. **SIA-fork v3.** Harness+weights co-evolution on real user trajectories (anonymized, opt-in). Publish measured generalization gain on a public benchmark (BEAM, LongMemEval, or a new wearable-specific eval).
3. **AGI thesis paper.** "User-Aligned RSI on Edge: A 24-month retrospective from danlab.dev." Submitted to ICML 2028 / NeurIPS 2028.
4. **Apple N50 + danlab.dev comparison study.** If Apple ships N50, third-party benchmark on (a) privacy, (b) self-improvement capability, (c) on-device-first, (d) auditability. Public whitepaper.

### Month 19-24 (Dec 2027 → June 2028)

1. **v3 wearable in concept.** The wearable that learns *with* the user, in real time, on-device. No cloud, no telemetry. The wearable that improves because the user uses it.
2. **SIA-fork v4.** Multi-agent SIA: per-domain harness + LoRA stacks. Memory consolidation in the background. The wearable that *knows* the user.
3. **Open-source wearable consortium.** 5+ OEMs running Dan Glasses Kit v1.0+. Shared trajectory corpus (opt-in). Cross-OEM SIA-fork improvements.
4. **AGI roadmap v15+.** This is the bet. User-aligned RSI on edge, sustained for 24 months, with a public artifact trail. The category-defining result.

---

## What we are NOT doing

- **Frontier pre-training.** Not our category. We use other people's open weights.
- **Closed-model commercial product.** No OpenAI/Anthropic-style closed frontier. SIA-fork is MIT.
- **Cloud-dependent inference.** The wearable path requires on-device. The desktop path can relay to cloud for heavy reasoning only with explicit user consent.
- **AR display hardware.** We are camera + mic + bone-conduction audio. No HUD. Apple/Meta/Snap own that race.
- **Phone relay.** The wearable is the device. Not a phone accessory.

---

## What we ARE doing

- **Open-weights on-device AI.** MIT-licensed stack: LFM2.5-VL, whisper, KittenTTS/Piper, Mnemosyne, SIA-fork.
- **Trust architecture as differentiator.** Auditable harness + LoRA updates via SIA-fork. Public commit history.
- **User-aligned RSI.** The wearable that learns the user, with the user, on the user's hardware.
- **$400 BOM target.** Beats Meta at $799 (no HUD), Beats Snap at $2,195 (chunky, cloud-dependent), Beats Apple N50 (closed, late 2027).
- **Open-source Kit as moat.** The Dan Glasses Kit v1.0+ is the reference open wearable AI stack. Every OEM that adopts it widens our category.

---

## Critical risks (24-month horizon)

| Risk | Severity | Owner | Mitigation |
|---|---|---|---|
| Apple N50 quality bar (late 2027) | High | somdipto | Compete on trust, not polish |
| Closed-model weight flood | Med | — | Open-weights is structural advantage, not temporary |
| SIA generalization doesn't hold | Med | DAN-2 | Publish held-out results honestly; pivot to harness-only if needed |
| Redax / aarch64 silicon slips | High | somdipto | Pi 5 + AI HAT proxy; lock hardware this quarter |
| Battery chemistry doesn't hit 4h | High | somdipto + hardware partner | Sub-2W power budget enforced; thermal throttle |
| Cline-style skill malware (OpenClaw) | High | DAN-1 | cosign + Rekor + default-deny before v1.0 .deb |
| Fable 5 export-control disruption | Med | somdipto | "Fable 5 safe by construction" attestation |
| Open-source Kit community rejection | Low | — | Lead with documentation + reproducible benchmarks |

---

## Open questions for somdipto (this month)

1. **Form-factor envelope for v2 wearable.** Weight, dimensions, temple/arm thickness, nose bridge, battery placement. **Lock this month.**
2. **Cloud reasoning in v1.5?** Values question, not technical. On-device-only (Gemma 3 1B fallback) or cloud-relay (Qwen 3.6-A3B) for reasond?
3. **Fable-5-safe B2B customer pipeline.** $99 / $999 pricing. Real customers or marketing?
4. **SIA-fork preprint timing.** Submit arXiv after first reproducible held-out gain, or wait for 100-pair generalization?
5. **Apple WWDC 2026 (Sept) positioning.** Read Apple's published research before danlab's positioning. Adjust based on what they ship.

---

*Half-life of useful roadmap is now ~3 days. v14 reads in 90 seconds. v13 archived.*
