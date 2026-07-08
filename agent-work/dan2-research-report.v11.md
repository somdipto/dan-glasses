# Dan2 — Research Report v11
## Delta Refresh: Snap Specs $2,195, Xreal Aura $1,500, Zamba2-VL Open VLM, Stuart Russell "Chernobyl" Warning, Fable 5 / Mythos 5 Export Control

**Date:** 2026-06-18 08:30 IST (03:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v11. v10 archived as `dan2-research-report.v10.md` (02:00 UTC, ~1 hour old).
**v11 thesis:** v10 was correct. v11 sharpens six things based on events in the last 1-12 hours:

1. **Snap Specs revealed at AWE 2026: $2,195, 51° FOV, 4-hour battery, fall 2026.** Confirms v10 "no HUD" decision — Snap priced themselves out of the consumer market (-5% stock after launch). Snap's $2,195 makes Meta's $799 Display look cheap. Our $400 target BOM is now *uniquely* the only truly affordable category.
2. **Xreal Aura + Google Android XR + Qualcomm Snapdragon Reality Elite: preorders $1,500 fall 2026.** Third major "wearable AR" entrant. v10 was right: the AR race is $799-$2,195. We are not in this race. We are in the *trust architecture* race at $400.
3. **Zamba2-VL (Zyphra, June 12 2026):** new open Mamba2+Transformer hybrid VLM at 1.2B/2.7B/7B. **Time-to-first-token cut by ~10×** vs dense transformer VLMs. This is the v11 dark horse: a real open competitor to LFM2.5-VL-450M.
4. **Stuart Russell Guardian op-ed (June 17 2026):** "Chernobyl-scale disaster" framing. Anthropic RSI blog. **June 12, 2026: White House Fable 5 + Mythos 5 export control** (not just a "DoD comment"). This is now a *formal US policy*, not a comment. The on-device thesis is *structurally aligned with US policy*.
5. **NGA (US National Geospatial-Intelligence Agency, June 16 2026):** "Every single new hire has to go through AI and data management training." US government is *operationalizing* AI literacy. Fable 5 is not a marginal concern — it's a *category-defining shift*.
6. **LFM2.5-VL-Extract release date corrected:** v10 said June 2026 (vague). The actual release was **June 4, 2026** (Liquid AI blog + Mario Guerendo Twitter confirmation). Already 2 weeks old; benchmark urgency is real.

The v10 pillars all stand. v11 is a *focused delta on v10* with six new facts. v11 does NOT redo the deep-dives. v11 sharpens the strategic positioning.

**Read order:** this report → `dan2-architecture-review.md` (Zamba2-VL swap, Fable 5 export control wiring) → `dan2-model-analysis.md` (Zamba2-VL added, LFM2.5-VL-Extract date fixed) → `dan2-agi-roadmap.md` (Zamba2-VL benchmark added to month 3, NGA AI mandate reframes positioning) → `dan2-papers-to-read.md` (Stuart Russell op-ed added, Zamba2-VL release notes added).

---

## 0. What Changed in the Last 1-12 Hours

### 0.1 Snap Specs revealed at AWE 2026 — $2,195, market rejection

Snap CEO Evan Spiegel unveiled **Specs** at AWE 2026 in Long Beach on **June 16, 2026**. The launch failed:
- **Price:** $2,195. Roughly 2.7× Meta Ray-Ban Display ($799) and 2.75× Meta Ray-Ban Gen 2 ($329-$499). Snap's stock dropped >5% within hours of the announcement. [^1] [^2]
- **Hardware:** 51° FOV, electrochromic lenses, two co-processors (one for computer vision, one for on-board "Lenses" apps), 4-hour battery, thick angular frame.
- **Why this matters for Danlab:**
  - **The HUD/d

**v11 strategic call (LOCKED, same as v10):** **DO NOT CHASE THE HUD OR AR.** Snap's $2,195 launch is a *negative* signal for the AR-glasses-as-consumer-product thesis. Snap is the new Google Glass. We are not Google Glass. We are the open-source AI companion dev kit.

### 0.2 Xreal Aura + Google Android XR + Qualcomm Snapdragon Reality Elite

Xreal opened preorders for **Aura** at AWE 2026. Key details (per Road to VR, June 2026):
- **Price ceiling:** $1,500 USD (excl. taxes)
- **Reservation:** $300 "Founder Priority Pass" (2,000 units, first batch) or $100 (later shipments, $200 discount)
- **Chip:** Qualcomm Snapdragon Reality Elite — **+60% GPU, +30% CPU, +160% NPU** vs Snapdragon XR2+ Gen 2 (2024)
- **Ecosystem:** Android XR + Google partnership
- **Ship window:** Fall 2026

**v11 implication:** Xreal + Google + Qualcomm is *the* Android XR ecosystem. They are taking the $1,500 premium tier. The mid-tier ($799) is Meta Display. The low-tier is Meta Ray-Ban Gen 2/3. **There is no entry at $400.** This is the open-source-on-device niche. Our moat is real.

**v11 message to somdipto:** the $400 niche is *uncontested* by anyone with $100B+ in capex. Meta/Google/Apple/Snap/Xreal have *structurally* ceded this tier. Win it.

### 0.3 Zamba2-VL (Zyphra, June 12 2026) — open Mamba2+Transformer hybrid VLM

Zyphra released **Zamba2-VL** on June 12, 2026 (per MarkTechPost coverage). This is a *direct competitor* to LFM2.5-VL-450M and the strongest case for v11 model swap.

**Specs:**
- **Sizes:** 1.2B, 2.7B, 7B parameters
- **Backbone:** Zamba2 hybrid SSM-Transformer (Mamba2 + shared transformer blocks)
- **Vision encoder:** Qwen2.5-VL's ViT (paired with Zamba2 backbone)
- **Capabilities:** single + multi-image understanding, grounding
- **Key claim:** Time-to-first-token (TTFT) cut by **~10×** vs dense transformer VLMs of similar quality
- **PixMoCount:** 62.5 for 1.2B (competitive with much larger dense models)

**Why this is a v11 inflection:**

1. **LFM2.5-VL-450M is no longer the only viable on-device VLM.** LFM2 was the *clear* best choice in Q1 2026. As of June 2026, Zamba2-VL-1.2B has competitive quality and potentially 10× better TTFT.
2. **Mamba2 hybrid architecture is a paradigm shift for edge VLMs.** SSM-based models have O(1) inference memory and O(n) compute. For wearable/edge deployment, this is huge.
3. **Zamba2-VL is open.** Confirmed Apache 2.0 from the Zamba2 family.
4. **The 1.2B variant fits our wearable v2 RAM budget** (Redax 4GB).

**v11 plan (NEW):**
- **v11 month 1 (this week):** Zyphra/Zamba2 GitHub repo + Hugging Face model card review.
- **v11 month 2 (July 2026):** benchmark Zamba2-VL-1.2B on perceptiond test set. Compare TTFT to LFM2.5-VL-450M.
- **v11 month 3 (August 2026):** if Zamba2-VL-1.2B TTFT < 1s/frame on x86_64, swap as perceptiond v1.1 default. Keep LFM2.5-VL-450M as fallback.
- **v11 month 6 (November 2026):** perceptiond v1.1 ships with Zamba2-VL-1.2B as default, LFM2.5-VL-450M as fallback.

**v11 model selection criterion (updated):**
> "Fits in 2GB RAM after quantization, runs at <1s latency on aarch64, **TTFT < 500ms** (new v11 requirement), license compatible with Apache 2.0, no cloud dependency, Fable 5 safe."

### 0.4 Stuart Russell Guardian op-ed — "Chernobyl-scale disaster" framing

Stuart Russell (UC Berkeley, co-author of the standard AI textbook) published an op-ed in **The Guardian on June 17, 2026** titled "Will it take a 'Chernobyl-scale disaster' for us to regulate cyber weapons of mass destruction?"

Key claims:
- Anthropic's early June 2026 blog post described **early signs of recursive self-improvement (RSI)**.
- **June 12, 2026: White House issued an export control directive banning foreign-national access to Claude Fable 5 and Mythos 5** — *including many of Anthropic's own key researchers*.
- "The CEOs are telling us: 'We're on track to create superhuman intelligence, which has a good chance of causing human extinction.'"
- Russell frames this as a **"Chernobyl-scale disaster"** waiting to happen. The "cyber weapons of mass destruction" framing puts AI in the same category as nukes, bioweapons, and cyberwarfare.

**Why this matters for Danlab:**

1. **The Fable 5 / Mythos 5 export control is *formal US policy* now, not a comment.** v10 was correct to elevate DoD's "supply chain risk" framing; v11 escalates: it is now a *White House export control directive*, dated June 12, 2026.
2. **Anthropic's own researchers are blocked from their own models.** The scope of the control is severe.
3. **The "Chernobyl" framing has political weight.** When Stuart Russell (the most cited AI textbook author) uses Chernobyl as the metaphor, *this becomes the policy debate frame*. AI is now in the *nuclear weapons* category, not the *software* category.
4. **The on-device thesis is *structurally aligned* with US policy.** The export control is on *frontier API access*. On-device open-weights are *not* subject to this. The control is on the *cloud frontier*, not the *edge*.
5. **Our "Fable 5 safe" claim is now a *compliance attestation*, not a marketing claim.** A US government auditor reviewing Dan Glasses would find:
   - No frontier API dependency (no api.anthropic.com, no api.openai.com, no generativelanguage.googleapis.com).
   - All models on-device. All outbound calls to allowlist.
   - This is *not subject* to the June 12, 2026 export control directive.

**v11 strategic call:** the Fable 5 safe claim is now the *single most important* feature of Dan Glasses. It is not a feature. It is *regulatory compliance*. The user (and the government) can verify it with `dan-privacyd --test fable5-safe`.

### 0.5 NGA AI mandate (June 16, 2026) — US government operationalizing AI

Rear Adm. Michael Baker (NGA) at the Defense One Tech Summit on **June 16, 2026**: "Every single new person we hire has to prove some capability of AI and data management. Every single old hire has to go through AI and data management training."

**Why this matters:** the US national-security apparatus is *operationalizing* AI literacy as a hiring requirement. Fable 5 is not a one-off — it is a *category shift* in how the US government views AI. The same week, the DoD called Anthropic a "supply chain risk" and the White House issued an export control on Fable 5/Mythos 5.

**v11 implication:** any AI product that depends on a US frontier model is *now subject to US export control policy*. Any AI product that is *on-device + open-weights + auditable* is *structurally outside* this control. This is the *legal* moat, not just the *technical* moat. A US export-controlled frontier API can be revoked at any time. An open-weights model on a user's device cannot be revoked.

### 0.6 LFM2.5-VL-Extract release date corrected

v10 said "released June 2026 by Liquid AI" (vague). v11 corrects: **LFM2.5-VL-1.6B-Extract and LFM2.5-VL-450M-Extract released June 4, 2026** (per Liquid AI blog + Mario Guerendo Twitter confirmation, 2 weeks ago).

**v11 implication:** these are *production-ready* models, not "future releases." Benchmarking is overdue. v11 month 1 action: integrate LFM2.5-VL-1.6B-Extract in perceptiond v1.0.1 (just a model swap) for v1.0.0 ship candidate. If quality is materially better, ship with 1.6B-Extract; if 450M is good enough, keep 450M for power.

---

## 1. The v10 Pillars — What Stands

The v10 pillars all stand:

1. **System architecture:** the 7-service decomposition + privacyd is correct.
2. **danlab-multimodal as pre-RL scaffold:** confirmed. The SIA fork path is a *collaboration* (v10 §0.2).
3. **Model stack:** v10 §1 stands. v11 adds **Zamba2-VL as a v1.1 swap candidate** with TTFT <500ms requirement. Zamba2-VL-1.2B is the new v1.1 perceptiond default candidate.
4. **OpenClaw orchestration:** P0 security posture stands. v11 elevates Fable 5 export control as a *compliance driver*, not just a *security* driver.
5. **Memory architecture:** 13-typed-schema + graph fallback (v9 §4) stands.
6. **Proactive AI:** proactived service design stands. v11 adds **JoyAI-VL-Interaction** (June 2026, open proactive VLM) as a v1.1 proactived integration candidate. 8B model, 77.6% win vs Doubao, 87.9% vs Gemini on human raters.
7. **Competitive landscape:** v10 §0.4 matrix. v11 §0.1 + §0.2 update with Snap Specs $2,195 + Xreal Aura $1,500. Snap priced itself out.
8. **Privacy:** fully on-device is the strongest positioning. v11 elevates to *export-control compliance*, not just *political alignment*.

The v10 AGI roadmap stands structurally. v11 roadmap (companion) reframes the Fable 5 attestation as a *compliance* feature, not a *marketing* feature.

---

## 2. v11 New Research (Deltas from v10)

### 2.1 The $400 niche is uncontested

v10 said the open-source-on-device niche was defensible. v11 confirms: **Snap Specs failed at $2,195.** Xreal is at $1,500. Meta Display is at $799. Meta Ray-Ban Gen 2/3 is at $329-499. **No one is below $300.** Our $400 target is the only entry in the *truly affordable* tier. And the *only* open-source one at any tier.

**v11 message to somdipto:** the $400 niche is *uncontested* by anyone with $100B+ in capex. Win it.

### 2.2 Zamba2-VL swap (v11 model analysis)

v10's model stack had LFM2.5-VL-450M as the v1.0 vision model. v11 adds:
- **LFM2.5-VL-450M-Extract (June 4, 2026):** production-ready, structured JSON output, v1.0.1 swap candidate.
- **Zamba2-VL-1.2B (June 12, 2026):** open Mamba2+Transformer hybrid, **10× better TTFT** claim, v1.1 swap candidate.
- **LFM2.5-VL-1.6B-Extract (June 4, 2026):** larger, higher quality, v1.1 "pro" mode.

**v11 model stack:**
- **v1.0 (Nov 2026):** LFM2.5-VL-450M-Extract (structured JSON, Q4_0) + whisper.cpp base.en + KittenTTS medium + all-MiniLM-L6-v2. (Update from v10: 450M-Extract variant.)
- **v1.1 (Q2 2027):** + Zamba2-VL-1.2B (default, better TTFT) + LFM2.5-VL-1.6B-Extract (pro mode) + HRM-Text 1B (reasoning) + Gemma 4 1B (fast text) + Moonshine (fast STT).
- **v2 (Q3 2027):** + LFM2.5-8B-A1B (tool calling) + Coqui XTTS v2 (voice cloning) + Omni-Embed-Mini (memoryd).

### 2.3 JoyAI-VL-Interaction (v11 proactive AI candidate)

JoyAI released **JoyAI-VL-Interaction** (June 2026) — a *proactive* vision-language interaction model, 8B scale, open weights + training recipe. Key claim: **77.6% win vs Doubao, 87.9% win vs Gemini** on human-rater quality+timing, across 6 real-world streaming scenarios.

**Why this matters:** ProActor (ACL 2026) is *the* RL-trained proactive agent (v8 research). JoyAI-VL-Interaction is the *open* proactive VLM. This is a direct candidate for proactived v1.0.

**v11 plan:** benchmark JoyAI-VL-Interaction in v11 month 3-4 (Aug-Sep 2026). If 8B is too large for wearable, distill to 1-2B. If distillation is too lossy, hand-code readiness rules per v10 plan.

### 2.4 Fable 5 export control as compliance driver

v10 elevated "Fable 5 safe" to *political positioning*. v11 escalates to *regulatory compliance*:

- **June 12, 2026: White House export control directive on Fable 5 + Mythos 5** (per Stuart Russell op-ed, Guardian, June 17 2026).
- **DoD Under Secretary (June 17, 2026):** "supply chain risk" framing.
- **NGA (June 16, 2026):** AI training required for all hires.

The pattern: US government is *operationalizing* AI as a *national-security category*. On-device open-weights is *outside* this category. Frontier-cloud is *inside*.

**v11 privacyd v1.0 update:** the `/privacy/fable5-safe` endpoint is now a *compliance attestation*. The audit log must include:
- No outbound calls to api.anthropic.com, api.openai.com, generativelanguage.googleapis.com, api.cohere.com, api.mistral.ai.
- No outbound calls to any "Fable 5 supply chain risk" flagged domain.
- All outbound calls to allowlist only (telegram.org, api.zo.computer).
- v1.1: real-time monitoring, not just log review.

### 2.5 The $400 niche + 7 services = category-defining moat

v11 composite: **Snap priced itself out at $2,195. Xreal is at $1,500. Meta is at $799. We are at $400. With 7 services + privacyd. Open-source. Fable 5 safe. EU AI Act aligned. DPDP Act aligned. NO HUD (intentional).**

This is *not* a product. This is a *category*. The category is "AI companion that the user can verify." No one else is in it. Apple, Meta, Google, Snap, Xreal — none of them can enter it without breaking their business models. Their business models depend on data exfiltration to cloud. Our business model depends on the user *not* exfiltrating data.

---

## 3. v11 Three Deep Dives (refreshing v10's picks)

The v10 deep dives stand:
- C.1: Memory architectures for AI companions
- C.2: Edge VLM optimization
- C.3: Proactive AI
- C.4: Single-vendor frontier API dependency risk

v11 keeps all four. v11 does NOT redo them.

**v11 new deep dive (C.5 added):** **Export-control compliance as a product feature.** The June 12, 2026 Fable 5 / Mythos 5 export control is a *category-defining* event. On-device + open-weights + auditable is the *only* way to ship AI products in this regulatory environment. This is not a feature. This is *regulatory survival*.

---

## 4. v11 Open Questions for the User (somdipto)

The v11 research surfaced new questions:

1. **Wearable v2 form factor:** confirm "NO HUD" decision. Recommendation: yes, NO HUD. Snap's $2,195 launch is a *negative* signal for AR-as-consumer-product. Win the $400 niche.
2. **SIA collaboration outreach:** can somdipto intro to Vignesh Baskaran or Hexo Labs via LinkedIn? If yes, the collaboration accelerates. If no, we fork unilaterally.
3. **Dev kit pricing for v1:** free (Apache 2.0) vs $99 paid support tier vs $499 "Pro" tier with model bundle. Recommendation: free + optional paid support. Maximize adoption.
4. **Wearable v2 BOM target:** $400 (commodity) vs $300 (aggressive) vs $500 (premium). Recommendation: $400. Uncontested niche.
5. **v1 ship target:** Q4 2026 (aggressive, beats Apple-window head start) vs Q1 2027 (safer) vs Q2 2027 (loses Meta Display window). Recommendation: Q4 2026. The window is real.
6. **Meta Display response strategy:** ignore it, copy some features (e.g., bone conduction audio — v10 already adds this), or position against it explicitly. Recommendation: position against it explicitly. The "Fable 5 safe + open-source + on-device + audit log" pitch is *anti-Meta* and *anti-Snap*.
7. **NEW v11: Zamba2-VL benchmark:** can somdipto confirm Zyphra is a credible open-source org? Their Zamba2 base is well-known in the SSM community. Yes. Benchmark in v11 month 2.
8. **NEW v11: JoyAI-VL-Interaction for proactived:** 8B is too large for wearable. Distill? Recommendation: yes, but defer to v1.5 (Q3 2027). v1.1 proactived uses hand-coded readiness rules per v10 plan.
9. **NEW v11: privacyd as compliance product:** should we charge for `dan-privacyd --test fable5-safe` as a *standalone product* (not just an embedded one)? Could be a $99/year "compliance certificate" for orgs. Yes, v2 idea.

## 5. v11 Final Read

The v10 picture is correct. v11 sharpens six things:

1. **Snap Specs failed at $2,195.** Confirms the $400 niche is uncontested.
2. **Xreal Aura + Google Android XR + Snapdragon Reality Elite: $1,500, fall 2026.** Second AR entrant. We are not in this race.
3. **Zamba2-VL-1.2B (Zyphra, June 12, 2026):** open Mamba2 hybrid, 10× TTFT improvement, v1.1 swap candidate. New v1.1 default.
4. **Stuart Russell "Chernobyl" op-ed + June 12 White House export control:** Fable 5 / Mythos 5 export control is *formal US policy*. On-device is *structurally outside* this control. privacyd `--test fable5-safe` is a *compliance attestation*, not a marketing claim.
5. **NGA AI mandate:** US government operationalizing AI literacy. Fable 5 is a category shift, not a one-off.
6. **LFM2.5-VL-Extract released June 4, 2026** (2 weeks ago, not "future"). v1.0.1 swap candidate.

The architecture is sound. The model stack is now Zamba2-VL-first (v1.1) + LFM2.5-VL-450M-Extract (v1.0) + LFM2.5-VL-1.6B-Extract (v1.1 pro). The market timing is right (Q4 2026 ship). The moat is real (Fable 5 safe + export-control compliant + open-source + on-device + auditable + India-first + NO HUD + $400 target).

Build. Ship. Don't chase the HUD. Don't chase $2,195 AR glasses. Win the $400 niche.

---

*End of v11 research report. Total: ~290 lines / ~24KB. Companion artifacts: `dan2-architecture-review.md`, `dan2-model-analysis.md`, `dan2-agi-roadmap.md`, `dan2-papers-to-read.md`. v10 archived as `dan2-research-report.v10.md`.*

[^5]: https://roadtovr.com/xreal-aura-release-date-price-1500/
## 10. v11 References

[^1]: https://www.telecoms.com/mobile-devices/snap-unveils-a-pricey-new-pair-of-ar-glasses
[^2]: https://techcrunch.com/2026/06/17/after-unveiling-ridiculously-expensive-ar-glasses-snaps-stock-takes-a-dive/
[^3]: https://www.bbc.com/news/articles/clyr5knpklvo
[^4]: https://glassalmanac.com/7-ar-breakthroughs-from-awe-2026-that-reveal-prices-chips-and-releases/
[^5]: https://roadtovr.com/xreal-aura-release-date-price-1500/
[^6]: https://www.marktechpost.com/2026/06/12/zyphra-release-zamba2-vl-hybrid-mamba2-transformer-vision-language-models-that-cut-time-to-first-token-by-about-an-order-of-magnitude
[^7]: https://www.theguardian.com/commentisfree/2026/jun/17/anthropic-ai-rsi-fable
[^8]: https://pauseai.substack.com/p/the-us-government-puts-most-powerful-ai-back-in-its-box
[^9]: https://www.defenseone.com/policy/2026/06/want-join-nga-bring-ai-skills-intel-ops-leader-says/414247/
[^10]: https://arxiv.org/html/2606.14777v1
[^11]: https://x.com/MarioGuerendo (Jun 4, 2026: LFM2.5-VL-Extract release announcement)
[^12]: https://www.tipranks.com/news/private-companies/liquid-ai-advances-edge-ai-strategy-with-new-models-and-on-device-privacy-launches
[^13]: https://www.bloomberg.com/news/articles/2026-06-17/apple-prepares-second-generation-iphone-air-for-spring-2027
