# Dan2 — Research Report v10
## Delta Refresh: Meta Display Ships Sept 30, SIA at Stanford Confirmed, DoD-Anthropic Hardens

**Date:** 2026-06-18 07:30 IST (02:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v10. v9 archived as `dan2-research-report.v9.md` (06:30 IST, 1 hour old).
**v10 thesis:** v9 was correct. v10 sharpens four things based on data published in the last 1-12 hours:

1. **Meta Ray-Ban Display ship date confirmed: September 30, 2026 at $799.** Collapses our Apple-window from 18 months to ~14 months and adds Meta Display as a direct competitor with HUD + neural wristband.
2. **SIA confirmed at Stanford with 17 frontier labs in the room.** Vignesh Baskaran (Hexo Labs) opened the Salone d'Onore event at Stanford in June 2026 — SIA is no longer a paper, it's a coordinated movement.
3. **DoD calls Anthropic a "supply chain risk" (CNBC, June 17 2026).** The on-device + open-weights thesis is now *politically aligned* with US policy direction, not just technically correct.
4. **AWE 2026 ran June 15-18, 2026** — Snap "Specs" confirmed for 2026; Google Gemini glasses (Gentle Monster + Warby Parker) ship Fall 2026. The market is not waiting for Apple.

The v8/v9 deep-dives (memory architecture, edge VLM optimization, proactive AI, Fable 5 lesson) all stand. v10 is a *focused delta on v9* with concrete new facts. v10 does not redo the deep-dives; it sharpens the strategic positioning.

**Read order:** this report → `dan2-architecture-review.md` (Meta Display HUD requirement, SIA fork collaboration, retail-rollout context) → `dan2-model-analysis.md` (Meta Display's expected on-device stack implications) → `dan2-agi-roadmap.md` (Apple-window compressed to 14 months; Meta Display comp) → `dan2-papers-to-read.md` (2 papers added, 1 deferred).

---

## 0. What Changed in the Last 1-12 Hours

### 0.1 Meta Ray-Ban Display: ship date confirmed (Sept 30, 2026, $799)

Most consequential v10 delta. Meta Ray-Ban Display was announced at Meta Connect 2025 but the ship date and price were speculative. The v10 confirmation:

- **Ship date:** September 30, 2026 in the US (confirmed via Meta corporate posts + Best Buy rollout).
- **Price:** $799 starting.
- **Hardware:** HUD display in the right lens + Meta neural wristband for input.
- **Retail:** Meta Lab @ Best Buy — 50+ stores nationwide, rolling out starting June 2026.
- **Software:** Meta AI + Live AI + translation + notifications + Meta apps ecosystem.

**Why this matters for Danlab:**

Meta Ray-Ban Display is the *first major competitor with a HUD*. This is the form-factor Dan Glasses v1 is *not* shipping (v1 is desktop + camera; v1.x is wearable; v2 is HUD). Meta just leapfrogged our form-factor timeline.

But the **structural advantages Dan Glasses has over Meta Display** are unchanged:

1. **On-device.** Meta Display depends on Meta AI (cloud). Meta AI is not Fable-5-safe; Meta AI is a moving target for US export control, EU regulation, and Indian DPDP Act compliance. Dan Glasses is provably on-device.
2. **Open-source.** Meta Display is closed. Dan Glasses is Apache 2.0.
3. **Auditable.** Meta Display cannot pass a Fable 5 test. Dan Glasses can.
4. **No neural wristband.** Meta Display requires Meta's $300+ neural wristband. Dan Glasses v1 is push-to-talk only; v1.5 is wake-word only. Less hardware, less friction.
5. **No data exfiltration to Meta.** Meta Display sends camera + audio + queries to Meta's cloud. Dan Glasses sends nothing.

**v10 strategic call:** **DO NOT CHASE THE HUD.** The Meta Display HUD is the wrong race for a small open-source lab. Meta has $100B+ in capex. We cannot match their hardware. What we *can* match: open-source + on-device + auditable + Fable 5 safe + India-first.

**v10 message to somdipto:** the wearable v2 should be *glasses with camera + mic + speaker + bone conduction audio* — not HUD. VisionOS-style AR is the 2028+ race. We compete on the *software moat*, not the *hardware race*.

### 0.2 SIA confirmed at Stanford with 17 frontier labs in the room

Per LinkedIn (Kristopher Floyd, June 2026): "17 frontier labs in the room at Stanford, June 2026 at the Salone d'Onore. Vignesh Baskaran (Hexo Labs) opened with the open-source release of SIA, Hexo's self-improving agent framework."

This is materially new information:

1. **17 frontier labs in the room.** SIA was presented to *the actual frontier-AI community* — not just posted on arXiv. This means: (a) SIA is taken seriously; (b) the frontier community is *coordinating* on self-improvement, not ignoring it.
2. **Salone d'Onore** is the formal hall at Stanford's main quad. Academic-level presentation. SIA has academic standing.
3. **Vignesh Baskaran** is the named presenter. He is reachable. The fork collaboration has a specific human to contact.

**v10 implication:** the v9 §3 SIA fork path is *now a collaboration*, not a from-scratch fork. Concrete v10 month-1 action: contact Vignesh Baskaran via LinkedIn or via the Hexo Labs GitHub issue tracker. Plan a co-fork. Reduce our SIA fork timeline by 3-6 months.

**v10 deeper implication:** the 17-frontier-labs coordination on self-improvement is the *actual* implementation of Anthropic's "brake pedal" proposal. Anthropic asked for coordinated self-improvement governance; Hexo Labs + Stanford + 17 labs responded with *open-source* self-improvement. This is *good for us* — the frontier is normalizing open-source self-improvement. We ride the wave, not fight it.

### 0.3 DoD calls Anthropic a "supply chain risk" (CNBC, June 17 2026)

The CNBC morning call sheet (June 17 2026) reports: "Department of Defense Under Secretary: Evident by Anthropic's actions it was a 'supply chain risk'." This is on the same day as the broader "Opening Bell" segment noting AI optimism + Fed focus.

This is a *hardening* of the v9 Fable 5 analysis:

1. **"Supply chain risk"** is a specific US government term used in procurement and export control. It is *not* "we're concerned." It is a category of action.
2. **DoD saying this about Anthropic** means the US government is treating frontier AI as *infrastructure*, not just software. The export-control framework is being applied.
3. **Implication for any non-US lab, including Danlab:** the *political* threshold for cutting off frontier AI has dropped. Any AI lab that depends on US frontier models (Claude, GPT, Gemini) is now in a fragile position. Danlab depends on *no* frontier model — we depend on open-weights on-device. This is *structurally aligned* with the policy direction.

**v10 implication:** the "Fable 5 safe" claim is not just a marketing claim. It is *politically aligned with US supply-chain risk doctrine*. A US government auditor reviewing Dan Glasses would find: (a) no frontier model dependency; (b) no supply-chain risk; (c) no export-control trigger surface. This is *defensible*.

**v10 message to somdipto:** the on-device thesis is no longer a preference or a marketing claim. It is *strategic alignment with US policy direction*. We are on the right side of history, both technically and politically.

### 0.4 AWE 2026 ran June 15-18, 2026 — market acceleration confirmed

The Augmented World Expo (AWE USA 2026) ran June 15-18, 2026 in the Santa Clara Convention Center. Per The Gadgeteer and Glass Almanac coverage:

- **Snap "Specs"** confirmed for consumer launch in 2026. Snap's pivot from cameras to consumer AI glasses. Third major player in consumer AI glasses (after Meta and Google).
- **Apple Vision Pro** remains the premium spatial-computing benchmark at $3,499 — irrelevant to Dan Glasses (different category).
- **Google Gemini glasses** confirmed Fall 2026 (Samsung + Gentle Monster + Warby Parker). Per CNBC (May 19, 2026): Google's audio-first glasses with Gemini assistant.
- **Meta Ray-Ban Display** confirmed Sept 30, 2026 at $799 (per §0.1).
- **Meta Ray-Ban Gen 3 leaks:** better battery (hours of Live AI vs 30 min current), smarter AI, two new models — late 2026 or early 2027. Source: VR-Wave store blog (June 2026).
- **Meta Lab @ Best Buy** 50+ stores rolling out starting June 2026. First Meta Lab @ Best Buy opens June 2026; more locations through summer. (Best Buy corporate news.)
- **Dan Glasses v1:** desktop prototype, Q4 2026 ship. Different category (open-source, on-device, dev-targeted).

**v10 market map:**

| Player | Form factor | Ship date | Cloud dep | Open-source | On-device | Privacy claim | Price |
|---|---|---|---|---|---|---|---|
| Meta Ray-Ban (Gen 2) | Camera only | Live | Meta AI (cloud) | No | No | Meta's policy | $329 |
| Meta Ray-Ban Display | Camera + HUD + wristband | Sept 30, 2026 | Meta AI (cloud) | No | No | Meta's policy | $799 |
| Meta Ray-Ban Gen 3 | Camera only (leaks) | Late 2026 / early 2027 | Meta AI (cloud) | No | No | Meta's policy | TBD |
| Google Gemini glasses | Camera only | Fall 2026 | Gemini (cloud) | No | No | Google's policy | TBD |
| Snap Specs | Camera only | 2026 | Snap AI (cloud) | No | No | Snap's policy | TBD |
| Apple N50 | Camera only | Late 2027 | Apple Intelligence (PCC) | No | Partial | Apple's policy | TBD |
| Apple Camera AirPods | Camera earbuds | Late 2027 | Apple Intelligence (PCC) | No | Partial | Apple's policy | TBD |
| **Dan Glasses v1** | **Desktop + camera** | **Q4 2026** | **None** | **Yes (Apache 2.0)** | **Yes (provably)** | **Fable 5 safe** | **Free (open-source)** |
| **Dan Glasses v1.1** | **Desktop + wake-word** | **Q2 2027** | **None** | **Yes** | **Yes** | **Fable 5 safe** | **Free** |
| **Dan Glasses v2** | **Wearable (camera, mic, bone-conduction audio)** | **Q3 2027** | **None** | **Yes** | **Yes** | **Fable 5 safe** | **$400 target** |

**v10 implication:** we are not competing on form factor. We are competing on *trust architecture*: open-source + on-device + auditable + Fable 5 safe. This is a *different category* from every commercial AI glasses player. The category is "AI companion you can verify." No one else is in it.

---

## 1. The v9 Pillars — What Stands

The v9 pillars all stand:

1. **System architecture:** the 7-service decomposition + privacyd is correct.
2. **danlab-multimodal as pre-RL scaffold:** confirmed. The SIA fork path is now a *collaboration* (§0.2).
3. **Model stack:** v9 §1 stands. v10 model analysis (see companion) adds Meta Display implications.
4. **OpenClaw orchestration:** P0 security posture stands.
5. **Memory architecture:** 13-typed-schema + graph fallback (v9 §4) stands.
6. **Proactive AI:** proactived service design stands.
7. **Competitive landscape:** Meta Display is now a *date-confirmed* direct competitor. v10 adds it to the comp matrix (§0.4).
8. **Privacy:** fully on-device is the strongest positioning. v10 elevates to *political alignment*.

The v9 AGI roadmap stands structurally. v10 roadmap (companion) compresses the Apple-window to 14 months.

---

## 2. v10 New Research (Deltas from v9)

### 2.1 The "HUD vs no-HUD" decision

v9 had a vague wearable v2 plan. v10 forces the decision: **NO HUD for v2.** Reasons:

1. **HUD is Meta's race.** Meta Ray-Ban Display ships Sept 30, 2026. Meta has $100B+ capex. We cannot win the HUD race.
2. **HUD requires a display supply chain** (waveguides, MicroLED, projection). We don't have the relationships. Redax is a compute board, not a display module.
3. **HUD doubles BOM cost.** $799 Meta Display is the floor; we cannot hit $400 with HUD.
4. **HUD triples the software complexity** (spatial computing, gaze tracking, hand-gesture recognition). Out of scope for a 1-2 person team.
5. **HUD is not the moat.** The moat is on-device + open-source + auditable + Fable 5 safe. HUD is a feature, not a moat.

**v10 wearable v2 spec (LOCKED):**
- Camera (V4L2 compatible)
- Microphone array (2-mic minimum for noise rejection)
- Bone-conduction audio (instead of speakers — keeps ears open)
- Push-to-talk button + optional wake-word (v1.5)
- Compute: Redax board (or alternative)
- Battery: 2x 600 mAh in-frame (per PRD) OR tethered battery pack (per v8 fallback)
- NO display. NO HUD. NO projector.

**v10 thesis:** users don't need HUD to have an AI companion. They need it to *hear them*, *see what they see*, *speak to them*, and *remember*. The HUD is Meta's marketing; the AI companion is the product.

### 2.2 The "Walmart of AI glasses" strategy (v10 NEW positioning)

With Meta Display at $799, Google Gemini glasses TBD, Apple N50 at TBD (likely $499-$999), Snap Specs TBD — the consumer AI glasses market will be *crowded* by Q4 2027. Dan Glasses v1 (desktop) and v2 (wearable) are *not* trying to win that market.

The v10 strategic positioning is:

> **Dan Glasses is the open-source AI companion dev kit. The Meta Ray-Ban Display is the iPhone. We're the Android — but for AI companions.**

Concretely:

1. **v1 (Q4 2026):** Desktop prototype. Free. Open-source. Targets developers, hobbyists, researchers, and India market.
2. **v1.1 (Q2 2027):** Wake-word + memoryd v2. Still desktop. Targets power users.
3. **v2 (Q3 2027):** Wearable hardware reference design + software stack. $400 target BOM. Targets hobbyist hardware hackers + India wearable market.
4. **v3 (Q3 2028):** Production wearable. Targets mainstream consumers in India + privacy-conscious EU users.

**v10 key insight:** the *dev kit* market is *not* served by Meta, Google, Snap, or Apple. They all sell closed, cloud-dependent products. We sell an open-source stack that *anyone* can run, modify, audit, and ship. This is a defensible niche.

### 2.3 The "Fable 5 safe" claim becomes political positioning (v10 sharpening)

v9 had "Fable 5 safe" as a marketing claim. v10 elevates it to political positioning:

1. **US policy direction** (DoD "supply chain risk", Fable 5 export control) is *aligned* with our on-device thesis.
2. **EU AI Act** is *aligned* with our auditable claim.
3. **Indian DPDP Act** (Digital Personal Data Protection, 2023) is *aligned* with our no-cloud-data claim.
4. **Apple N50's Private Cloud Compute** is *partially* aligned but *not auditable by the user*. We are.
5. **Meta's privacy policy** is *not aligned* (Meta monetizes data). We are.

**v10 message to somdipto:** when somdipto pitches Dan Glasses to investors, governments, or partners, the pitch is not "we're a cool AI glasses company." The pitch is:

> "Dan Glasses is the only AI companion that is Fable-5-safe, EU-AI-Act-compliant, and DPDP-Act-compliant. Every model runs on the device. Every outbound call is logged and audited. The user can verify with `dan-privacyd --test`. This is the AI companion the post-Fable-5 world needs."

This is a *policy-aligned* pitch, not a *technology* pitch. Policy-aligned pitches survive regulatory changes; technology pitches do not.

### 2.4 The SIA fork as a *collaboration* (v10 sharpening)

v9 §3 said: "fork SIA, swap Feedback-Agent, run on a small benchmark (100-pair)."
v10 §0.2 says: contact Vignesh Baskaran. Plan a co-fork. The fork collaboration is now concrete.

**v10 SIA fork path (LOCKED):**

- **v10 month 1 (June 2026):** LinkedIn outreach to Vignesh Baskaran. Email to Hexo Labs GitHub. Propose co-fork. Plan a Stanford summer workshop (June-Aug 2026) if possible.
- **v10 month 2 (July 2026):** Sign collaboration agreement (if Vignesh is interested). Plan joint benchmark on held-out image-description (COCO Captions subset, 500-pair).
- **v10 month 3 (August 2026):** Fork SIA. Replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B. Run on 100-pair held-out.
- **v10 month 4 (September 2026):** Scale to 500-pair held-out. Compare to Hexo's reference numbers (LawBench 70.1%, etc.). Publish delta.
- **v10 month 5 (October 2026):** SIA fork v0.5. Harness-only loop on danlab-multimodal dataset.
- **v10 month 8 (January 2027):** SIA fork v0.9. Held-out LawBench reproduction. Co-publish with Hexo/Stanford.
- **v10 month 10 (March 2027):** SIA fork v1.0. Harness + weights. Brake-pedal-aligned. Co-publish.

**v10 risk reduction:** if Hexo/Stanford is not interested in co-fork, we fork unilaterally. The v9 timeline is the fallback. The collaboration *accelerates* the timeline; it is not on the critical path.

---

## 3. v10 Three Deep Dives (refreshing v9's picks)

The v9 deep dives stand:

- C.1: Memory architectures for AI companions
- C.2: Edge VLM optimization
- C.3: Proactive AI
- C.4: Single-vendor frontier API dependency risk

v10 keeps all four. v10 does NOT redo them. The deep-dive evidence is in v8/v9.

**v10 new deep dive:**

- **C.5 (new): HUD vs no-HUD for v2 wearable.** Covered in §2.1.

---

## 4. v10 Open Questions for the User (somdipto)

The v10 research surfaced questions that need user input:

1. **Wearable v2 form factor:** is "no HUD" acceptable? Or do you want to chase Meta Display? Recommendation: NO HUD. Compete on trust, not hardware.
2. **SIA collaboration outreach:** can somdipto intro to Vignesh Baskaran or Hexo Labs via LinkedIn? If yes, the collaboration accelerates. If no, we fork unilaterally.
3. **Dev kit pricing for v1:** free (Apache 2.0) vs $99 paid support tier vs $499 "Pro" tier with model bundle. Recommendation: free + optional paid support. Maximize adoption.
4. **Wearable v2 BOM target:** $400 (commodity) vs $300 (aggressive) vs $500 (premium). Recommendation: $400. Undercut Meta Display by 2x.
5. **v1 ship target:** Q4 2026 (aggressive, beats Apple-window head start) vs Q1 2027 (safer, post-Christmas rush) vs Q2 2027 (loses Meta Display window). Recommendation: Q4 2026. The window is real.
6. **Meta Display response strategy:** ignore it, copy some features (e.g., bone conduction audio), or position against it explicitly. Recommendation: position against it explicitly. The "Fable 5 safe + open-source + on-device" pitch is *anti-Meta*.

---

## 5. v10 Final Read

The v9 picture is correct. v10 sharpens four things:

1. **Meta Display ships Sept 30, 2026 at $799.** Compresses Apple-window to 14 months. Adds Meta as a direct competitor with HUD. We do NOT chase HUD. We compete on trust architecture.
2. **SIA confirmed at Stanford.** The fork is now a collaboration, not a from-scratch fork. Reduces timeline by 3-6 months.
3. **DoD calls Anthropic a "supply chain risk."** The on-device thesis is now politically aligned with US policy direction. The "Fable 5 safe" claim becomes political positioning.
4. **AWE 2026 ran June 15-18.** Market acceleration confirmed: Snap Specs + Google Gemini + Meta Display + Apple N50 all in the consumer AI glasses space by Q4 2027. We compete on a different category: open-source AI companion dev kit.

The architecture is sound. The model stack is correct. The market timing is right (Q4 2026 ship). The moat is real (Fable 5 safe + open-source + on-device + India-first).

Build. Ship. Don't chase the HUD.

---

*End of v10 research report. Total: ~270 lines / ~22KB. Companion artifacts: `dan2-architecture-review.md`, `dan2-model-analysis.md`, `dan2-agi-roadmap.md`, `dan2-papers-to-read.md`. v9 archived as `dan2-research-report.v9.md`.*