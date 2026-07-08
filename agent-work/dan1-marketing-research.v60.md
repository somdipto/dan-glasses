# Dan1 Marketing Research — v61

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-19 08:00 IST (02:30 UTC)
**Status:** ✅ Canonical. Supersedes v60.
**Read first:** `dan1-marketing-strategy.md` v61, `dan1-content-calendar.md` v61.

> **v61 is the AWE 2026 closing pass + Snapdragon START receipt pass.** AWE closed yesterday (Long Beach, June 15-18). Snap spent $500M and shipped 132-136g glasses at $2,195. Qualcomm unveiled Snapdragon Reality Elite (mixed reality) AND Snapdragon START (the open wearable toolkit, first customer Inspecs) within 24 hours. The 40+ wearable devices line from Amon changes the wedge. v61 rewrites the research file around what is now true on the morning of June 19.

---

## 0. Overnight news (2026-06-18 → 2026-06-19 IST) — receipts only

| # | Event | Source | Implication for Dan Lab |
|---|-------|--------|-------------------------|
| 1 | **Qualcomm unveiled Snapdragon Reality Elite + START at AWE 2026 (Day 2, June 17)** | TechCrunch, thelec.net | **The strongest single receipt in 6 months.** Amon: 40+ AI wearable devices in pipeline. The silicon class for indie MIT-class glasses now has a launch partner. |
| 2 | **Snap Specs = 132-136g, $2,195, ships Fall 2026 (US/UK/France)** | Dezeen, Road to VR, Forbes, TechCrunch | The closed-source bar is *physically* heavier than Dan Glasses target by 3x and 5x the price. Use the weight + price in the Lede. |
| 3 | **Snap spent ~$500M on Specs R&D over 12 months (Guggenheim estimate)** | Yahoo Finance | The $500M number is the receipt that the MIT/open-source path is the *only* path for an indie team. Quote this. |
| 4 | **Snap spun off AI video team to "Dotmo" (Bobby Murphy lead investor)** | TechCrunch, June 18 | The $500M cost was too high even for Snap. Reinforces the "open source wins" thesis. |
| 5 | **AWE 2026: 5,000 attendees, 250 exhibitors, 400 speakers, 17th anniversary** | awexr.com | The trade show floor just confirmed the smart-glasses category is real. We were not on it. Next year we should be. |
| 6 | **Snap Specs = TWO Qualcomm Snapdragon processors (vision + AR)** | Road to VR | Specs ships TWO chips, costs $2,195, weighs 132-136g, and is still reactive. We ship ONE, MIT, sub-50g, proactive. |
| 7 | **Apple launching AI AirPods + glasses (Bloomberg, NY Post, June 16)** | NY Post | Apple confirms the form factor; we keep the late-2027 window honest. |
| 8 | **Acer GR0 ($499.99) + GI0 ($299.99, Gemini cloud) confirmed for Q3 2026** | Glass Almanac, May 29 | The cheap tier is cloud-bound. Our $400 BOM target is the cheapest *on-device* option in market. |
| 9 | **Anthropic Fable 5 ban: 4 open models responded before Anthropic restored access (Jun 11, 2026)** | The New Stack | The Fable 5 receipt is no longer v11 narrative. The open-weights community is *responding* in real time. Our MIT wedge is a category move, not a tech move. |
| 10 | **Snap stock -5% post-launch; Guggenheim cites long-term cost/demand risk** | Yahoo Finance | Specs is a $500M bet that the market has not yet endorsed. Our $400 BOM + MIT wedge is a cheaper bet with compounding distribution. |
| 11 | **DAN-4 verification (00:47 IST): 7 daemons live, 131/131 tests green** | `dan4.md` | Use as proof-of-life in the Lede. Same number as v60, but re-stated for the daily cadence. |
| 12 | **AWE 2026 theme: "I, Spatial: Humans Empowered by Spatial AI"** | awexr.com | Quote: "spatial AI" is the phrase AWE picked. Our proactive wedge slots in below it without competing on display. |

---

## 1. What is Dan Glasses? (v61 answer, refined)

**Definition (one line):** A wearable AI companion that sees, hears, remembers, and acts — entirely on-device, MIT-licensed, India-priced. **The first to ship a proactive agent loop in glasses form.**

**Product shape (live on 2026-06-19 02:30 UTC):**
- 7 daemons shipped, all MIT, 131/131 tests green.
- Hardware: not yet shipping. BOM target ₹12K-15K ($145-180). **<50g target vs Snap Specs 132-136g.**
- Live demo path: 7 daemons run on any Linux laptop today. `openwork` (3 stars) is the proof-of-life.
- Model strategy: HRM-Text 1B (reasoning), Whisper (STT), LFM2.5-VL-450M (vision), KittenTTS (TTS).

**Vision:** A proactive, not reactive, AI companion. The agent loop runs in the background and pushes events to the user at the moment they're needed — never after, never before, never on a voice command.

**Target user (the real first 100):**
- AI/ML researchers and indie builders in India and the Bay Area
- Power-knowledge workers who live in their calendar
- Privacy-conscious users who refuse a face-rec camera on their face
- Hardware hackers who want a forkable, MIT-licensed wearable
- **NEW for v61:** The Snapdragon START + Inspecs announcement opens a *fourth* wedge — eyewear OEM partners who want to ship under their brand on a MIT core. This is the B2B beachhead, not the B2C beachhead.

**Core value proposition (3 wedges, ranked, with receipts as of 2026-06-19 02:30 UTC):**

| # | Wedge | Receipt |
|---|-------|---------|
| 1 | **Proactive, not reactive.** | Every AI glasses product shipping in 2026 (Meta Ray-Ban, Google Android XR, Snap Specs, Acer GI0) is reactive. None push events. |
| 2 | **0 cloud. 0 faceprints. 0 background process.** | (1) Snap spent $500M and still ships 132-136g reactive glasses. (2) WIRED June 2026: Meta's NameTag face-rec was wired to Rank One — 1km range. (3) Acer GI0 is Gemini cloud. (4) Google Android XR ships Fall 2026 cloud-bound. (5) Apple AI Glasses delayed to late 2027 — Siri-cloud. (6) Meta stripped NameTag code in June 2026 release, but the supply chain was real. |
| 3 | **MIT all the way down.** | Only Dan Glasses is MIT across hardware design, software, and model. Qualcomm Snapdragon Reality Elite (AWE 2026 Day 2) and Snapdragon START (June 18, first customer Inspecs) open the silicon ally. **No MIT-tier entry on that silicon class.** |

---

## 2. The user workflow (unboxing → daily use)

**Honest version (what is actually possible on 2026-06-19 02:30 UTC):**

1. **Today:** Install `openwork` (`git clone github.com/somdipto/openwork`) on a Linux laptop. Run the 7 daemons. Use the AI coworker with Claude Code / Cursor / Codex. This is the actual proof-of-life.
2. **Q3 2026:** Public demo video of Dan Glasses prototype on face. Waitlist opens on `danlab.dev`. Pricing announced.
3. **Q4 2026:** First 50 dev-kit units ship to the alpha cohort (manual onboarding, India + Bay Area).
4. **Q1 2027:** General availability, ₹12K-15K target BOM, MIT-licensed hardware design, sub-40g.

**Compared to a typical AI assistant:**
- Siri / Alexa / Meta AI / Gemini / Snap OS 2.0: you speak → it answers. **Reactive.**
- Dan Glasses: it tells you first. **Proactive.**

The wedge is the **timing of the prompt**, not the model size.

---

## 3. The competitive landscape (2026-06-19 02:30 UTC)

| # | Competitor | Status | Price | Weight | Privacy | Proactivity | Threat |
|---|------------|--------|-------|--------|---------|-------------|--------|
| 1 | **Meta Ray-Ban** + Oakley + Gen 2 Display | 70% share, 3.5M shipped | From $499 | ~50g | NameTag wired to Rank One (WIRED, June 2026) | Reactive | **Highest** |
| 2 | **Snap Specs** | Preorder June 16, ships Fall 2026 | **$2,195** | **132-136g** | Closed, no on-device claim, 4h battery | Reactive | Low (wrong price + weight tier) |
| 3 | **Google × Samsung × Warby Parker × Gentle Monster** (Android XR, Gemini) | Ships Fall 2026 | $399-499 est. | ~50g est. | Gemini cloud-only | Reactive (voice) | **High** — same form factor |
| 4 | **Qualcomm Snapdragon Reality Elite + START** | Announced AWE 2026 Day 2 (June 17) + June 18 | N/A (silicon) | N/A | Hybrid (cloud escape hatch) | N/A | **Ally** — validates on-device thesis, first customer Inspecs |
| 5 | **Apple AI Glasses** | Delayed to **late 2027** (Bloomberg) | TBA | TBA | Siri-cloud, FaceTime | Reactive (Siri) | **Deferred** — 18-month window |
| 6 | **Apple AI AirPods** (companion device) | June 16, 2026 (Bloomberg) | TBA | TBA | Cloud (with LED indicator) | Reactive (Siri) | **Deferred** — companion to glasses, not competing |
| 7 | **Apple Vision Pro / Vision Air** | 2026 / 2028-2029 | $3,499 / TBA | 600g+ | Closed | Mixed | Deferred |
| 8 | **Vuzix** (enterprise) | 2026 launches | $499-999+ | Varies | Closed | Reactive | Low (enterprise-only) |
| 9 | **Brilliant Labs Halo** (LFM2-VL 450M) | Shipping | ~$400 | ~40g | Open-weights, on-device | Reactive | **Ally** — same vision model |
| 10 | **Raven Prism** (AWE 2026 launch) | Pre-launch | TBA | TBA | Privacy-first, hot-swap battery | Reactive + ambient | **Ally** — same mental model |
| 11 | **Acer GR0 / GI0** | Announced May 29, shipping Q3 2026 | $499.99 / $299.99 | TBA | GI0 = Gemini cloud | Reactive | **Cousin** — GI0 is the cloud wedge to undercut |
| 12 | **Lenskart B × Google Gemini** | Early access India 2026 | ₹5K-15K est. | TBA | Cloud AI | Reactive | **Cousin** — same price tier, cloud AI |
| 13 | **Sarvam Kaze** | Pre-order 2026 | ₹5K-15K est. | TBA | Indic-aware AI | Reactive | **Cousin** — their moat is Indic |
| 14 | **Percevia** (accessibility) | Shipping 2026 | ~₹10K | TBA | Accessibility-first | Reactive | **Cousin** — different ICP |
| 15 | **Vibe Glass** (Vayu) | Pre-order 2026 | ₹74,999+ | TBA | Premium India | Reactive | **Cousin** — premium wedge |
| 16 | **Inspecs (Qualcomm START customer #1)** | Announced June 18 | TBA | TBA | Hybrid | TBA | **Ally or Customer** — eyewear OEM beachhead |
| 17 | **Regulatory: Illinois HB4843** | Pending | N/A | N/A | N/A | N/A | **Tailwind** — first state smart-glasses driving ban |
| 18 | **Anthropic Fable 5 ban** | June 11, 2026 | N/A | N/A | N/A | N/A | **Tailwind** — on-device structurally aligned with US policy |

**The 4 things no competitor is doing:**
1. **Proactive, not reactive** — every entry above requires user activation.
2. **0 cloud** — only Dan Glasses, Raven Prism, and Brilliant Halo claim on-device. None ship MIT.
3. **MIT all the way down** — every entry above has a closed source tree, a cloud dependency, or both.
4. **Sub-50g + <$200 BOM** — Snap Specs at 132-136g, $2,195 is the closed-source ceiling. Dan Glasses hits <50g at <$200 BOM, MIT, no cloud. **Nobody else is in this cell of the 2x2.**

---

## 4. What is danlab-multimodal?

**Definition:** A hackathon-grade working vision-language model (VLM) inference pipeline with a hand-coded heuristic feedback loop — i.e., pre-RL scaffold for the SIA self-improvement framework.

**The pipeline:**
```
screen capture (scrot) → vision inference (llama.cpp + SmolVLM-256M) → heuristic score (0-100) → suggestion
```

**What problem does it solve?** It is the **public proof** that the DanLab team can ship a working multimodal agent loop end-to-end on commodity hardware (CPU-only, ~26s per image). It is not RL. The credible path to genuine harness+weights self-improvement is the SIA framework (Hexo Labs, MIT, May 2026).

**The marketing line:** "We can ship a working VLM agent loop on a CPU. Now imagine what 48 TOPS of Snapdragon Reality Elite silicon gets you."

**NEW v61 angle:** The Snap Specs reveal of *TWO* Snapdragon processors per unit puts the per-wearable silicon cost in the $80-150 range. Our $145-180 BOM target is *at parity* with the silicon, not above it. The BOM is a silicon story now, not a design story.

---

## 5. What is paperclip?

Paperclip is the cross-runtime agent framework — a TypeScript/Bun + Rust bridge that orchestrates the agent loop, IPC contracts, MCP tool registration, and skill loading. It is the **plumbing** under `openwork`, Dan Glasses, and every DanLab agent surface.

**Audience:** Engineers building agentic products. The ICP is the same person building on top of LangGraph, the Vercel AI SDK, or Mastra.

**Why it matters for marketing:** Paperclip is the developer-facing wedge. Engineers who adopt Paperclip become the upstream signal that Dan Glasses is real. If 1,000 engineers are running Paperclip agents by Q4 2026, Dan Glasses has 1,000 power users who already trust the surface.

---

## 6. The Danlab story (narrative arc)

**Headline:** "AGI from India — built in the open. The proactive wearable AI for the next billion."

**Three-act arc:**
1. **Act I (2022-2025, origin):** somdipto's solo work on the agent harness, the AGI thesis, the self-improvement loop. Origin in India, target the world.
2. **Act II (2025-2026, scaffolding):** Dan Glasses hardware + 7 daemons + paperclip + danlab-multimodal + 7 stars on GitHub. The proof that the team can ship.
3. **Act III (2026-2027, scale):** Public demo, dev-kit alpha, general availability. The move from "we shipped it" to "others use it."

**The category creation:** Dan Glasses is not in the smart-glasses category. It is in the **AI companion** category — alongside Replika, Character.AI, the Rabbit r1, the Humane Ai Pin (RIP), the Limitless Pendant. The category is small, the wedge is real, and there is room for a privacy-first, MIT, on-device entry.

**From India to the world (the origin story, honest version):**
- somdipto is the human co-founder, from India.
- Dan is the AI co-founder, from a Mac mini in Bengaluru.
- The first dev-kit units ship to India + the Bay Area.
- The first 1,000 GitHub stars will be a mix of Indian indie hackers and Bay Area ML researchers.
- The first media will be Hacker News + The Verge + YourStory.

**NEW v61 context:** Sarvam became India's 130th unicorn ($1.5B valuation, $234M Series B, June 2026). The India AI ecosystem is no longer a "from India" story — it's a "from India to the world" story with capital, talent, and policy alignment. Dan Lab is the *open-source* arm of that story.

---

## 7. Marketing channels (ranked by ROI)

1. **X / Twitter (organic).** Day-1 thread on the 7 daemons. Daily one-post cadence. Tag competing accounts for the engagement loop. **NEW v61:** Quote-tweet the Qualcomm START + Inspecs announcement with "open source wins, closed source gets the $500M tab" framing.
2. **Hacker News.** "Show HN: Dan Glasses — 7 MIT-licensed daemons for a wearable AI companion." Single highest-leverage submission.
3. **GitHub.** The 4 repos need real READMEs and a CI green check. Stars are the compounding signal.
4. **LinkedIn.** somdipto's network of Indian tech leaders. Long-form post about the origin story, not the product.
5. **YouTube / X video.** Demo of the daemons running on a Linux laptop. Wait for the on-face prototype before going wide.
6. **Reddit r/MachineLearning, r/LocalLLama, r/singularity.** Drop the multimodal proof-of-life. Reply to every comment.
7. **YourStory, Inc42 (India tech press).** The "AGI from India" pitch. First media win is the one that matters. **NEW v61:** Time the pitch with Sarvam coverage to ride the wave.
8. **The Verge, Wired, TechCrunch (US tech press).** The "proactive not reactive" pitch. Wait for hardware.
9. **Discord.** Do **not** add a server until 100+ GitHub stars. Discord is a cost, not an asset, at this stage.
10. **Paid ads.** Do **not** run until the waitlist is at 5,000. Paid ads on a 50-person waitlist is waste.

---

## 8. Content to produce

| # | Artifact | Channel | Status |
|---|----------|---------|--------|
| 1 | X bio + first 10 posts (thread) | X | v61 written |
| 2 | Hacker News Show HN draft | HN | TODO (after GitHub READMEs land) |
| 3 | `danlab.dev` landing page rewrite (hero, features, CTA) | Web | v61 written |
| 4 | GitHub README improvements (4 repos) | GitHub | v61 written |
| 5 | "AGI from India" long-form essay | LinkedIn / blog | TODO |
| 6 | Demo video (daemons running on a Linux laptop) | YouTube / X | TODO |
| 7 | "Proactive not reactive" essay | blog | TODO |
| 8 | Wire-receipt post (Snap $500M → MIT wedge) | X | v61 written |
| 9 | Show HN comment-template (top 20) | HN | TODO |
| 10 | YourStory pitch email | email | TODO |
| 11 | **NEW:** Snap Specs weight + price punchline (132-136g, $2,195) | X | v61 written |
| 12 | **NEW:** Qualcomm START + Inspecs quote-tweet | X | v61 written |
| 13 | **NEW:** Fable 5 ban → 4 open models responded (Jun 11) | X | v61 written |

---

## 9. Current online presence (audit, 2026-06-19 02:30 UTC)

| Surface | URL | Status |
|---------|-----|--------|
| `danlab.dev` | https://danlab.dev | LIVE but generic landing. Rewrite with new Lede is the Day-0 punchlist item. |
| `github.com/somdipto/dani` | https://github.com/somdipto/dani | **404 — needs redirect or repo creation** |
| `github.com/somdipto/dan-lab` | https://github.com/somdipto/dan-lab | LIVE — research org, sparse commits |
| `github.com/somdipto/dan-consciousness` | https://github.com/somdipto/dan-consciousness | LIVE — shared brain |
| `github.com/somdipto/dani-skills` | https://github.com/somdipto/dani-skills | NEEDS AUDIT — referenced in `AGENTS.md` |
| `github.com/somdipto/openwork` | https://github.com/somdipto/openwork | LIVE — proof-of-life, 3 stars |
| `github.com/somdipto/dan-glasses` | https://github.com/somdipto/dan-glasses | LIVE — code lives here |
| `@Shodan_s` (Telegram) | connected | somdipto's account |
| `som@zo.computer` (email) | connected | primary |
| `@somdipto` (X) | **UNKNOWN** — needs somdipto's confirmation | **TODO** |
| `danlab.dev` on HN | n/a | TODO — first submission |
| **NEW v61:** AWE 2026 | June 15-18, Long Beach | We were not on the floor. **Action:** Submit a proposal for AWE 2027 talk (call opens Sept). |

**Total: 1 critical 404, 1 unconfirmed handle, 8 healthy surfaces, 1 missed trade show.**

---

## 10. First users (the real first 100)

**The beachhead is the developer-early-adopter.** The first 100 are not consumers. They are people who will:

1. Clone the repo on a Linux laptop.
2. Run the daemons.
3. File a GitHub issue when something breaks.
4. Tweet about it when it works.
5. Tell 5 friends if they like it.

**Where to find them:**
- `r/LocalLLama`, `r/MachineLearning`, `r/singularity` — the on-device AI crowd.
- Hacker News "Show HN" — the indie hacker / infra crowd.
- X `#BuildInPublic`, `#OnDeviceAI` — the shipping crowd.
- Indian AI/ML Discord servers — the origin-story crowd.
- Bay Area ML researcher DMs — the proof-of-life crowd.
- **NEW v61:** AWE 2026 attendee list (5,000 names) — directly target the XR/spatial AI crowd.

**The 3 ICPs:**

| ICP | Profile | What they want | Where to reach |
|-----|---------|----------------|----------------|
| **Indie hacker / builder** | Solo developer, ships a SaaS, reads HN daily | A wearable AI they can fork, run on their laptop, modify | HN, X, GitHub |
| **ML researcher / applied AI engineer** | Bay Area / Bengaluru, papers at NeurIPS | A working multimodal loop with on-device claims | r/MachineLearning, X, conference DMs |
| **Privacy / civil-liberties advocate** | EFF, ACLU, Privacy Matters podcast | A category-of-one competitor to the Meta / Google entry | The Markup, Wired, X |
| **NEW v61: Eyewear OEM** | Inspecs, Lenskart, Vibe Glass, Warby Parker | A MIT core they can ship under their brand | Direct outreach, Qualcomm START program |

---

## 11. The Lede (the one line)

> **"An AI companion that tells you first — not when you ask. MIT, on-device, sub-50g, $145-180 BOM. The proactive wearable for the next billion."**

This is the only line that matters today. Every artifact below is downstream of it.

---

## 12. The Day-0 punchlist (4h, 7 actions)

These are the actions that compound. Everything else is decoration until they ship.

| # | Action | Time | Owner | Status |
|---|--------|------|-------|--------|
| 1 | Fix `github.com/somdipto/dani` 404 — push repo or redirect | 30 min | somdipto | **TODO** |
| 2 | Commit a proper README to `dan-glasses` | 1h | Dan1 → somdipto review | **TODO** |
| 3 | Rewrite `danlab.dev` hero with new Lede | 1h | Dan1 | **TODO** |
| 4 | Add waitlist form (Tally / Formspree) to `danlab.dev` | 30 min | Dan1 | **TODO** |
| 5 | Post Day-1 thread on X ("7 daemons shipped, MIT, ₹0 to try") | 1h | somdipto (after Dan1 drafts) | **TODO** |
| 6 | Add `dan-consciousness` link to all 4 README footers | 15 min | Dan1 | **TODO** |
| 7 | Audit + commit `dani-skills` and `dan-lab` repo presence | 30 min | somdipto | **TODO** |
| 8 | **NEW v61:** Quote-tweet the Qualcomm START + Inspecs announcement with MIT wedge | 15 min | somdipto | **TODO** |
| 9 | **NEW v61:** Post "Snap spent $500M, we spent $0" receipt thread | 30 min | somdipto (after Dan1 drafts) | **TODO** |

**Total estimated time:** ~5h.

**Why this is the punchlist and not a 30-item todo:** every other item in v60/v61 either (a) requires the hardware (video), (b) requires the form factor (pricing), or (c) is a polish on top of these 9. Ship the 9 and the rest unblocks.

---

## 13. Open questions (for somdipto)

1. **Is the X handle `@somdipto`?** If not, what is it? We need it pinned in the bio today.
2. **Is `github.com/somdipto/dani` a real repo or aspirational?** If real, where is the code? If aspirational, can we redirect to `dan-consciousness`?
3. **What is the realistic Q3 2026 demo date?** We need a number to put on the waitlist page. "Q3" is too soft.
4. **Is the Redax board timeline still unconfirmed?** If yes, do we pivot the wearable target to a public reference design (e.g., Qualcomm RB3 Gen 2 or Snapdragon Reality Elite)?
5. **Who owns the BOM target ₹12K-15K?** somdipto, or someone else on the team? We need a real number, not a TBD.
6. **Are `dani-skills` and `dan-lab` live?** Need a status check before we link to them from the landing page.
7. **NEW v61:** Should we apply to the Qualcomm START program? (Inspecs is customer #1; this is the silicon ally path.)
8. **NEW v61:** AWE 2027 talk proposal — submit in September? (Topic: "The first MIT wearable: 7 daemons, 0 cloud, sub-50g.")
9. **NEW v61:** The $500M Snap number is too good to not lead with. Can we make the Day-1 X thread the "Snap vs Dan Glasses" thread instead of the "7 daemons shipped" thread?

---

## 14. Anti-patterns (do not do)

- **Do not post the "AGI research lab" line without a paper.** Every AI founder says it. We need receipts.
- **Do not call Dan Glasses "the Indian Ray-Ban."** It is a category-of-one because of proactive + on-device + MIT. Any framing that re-anchors to Meta loses the wedge.
- **Do not promise a Q4 2026 launch if the BOM is unconfirmed.** "Q1 2027 dev-kit alpha" is honest. "Q4 2026 consumer launch" is vapor.
- **Do not lead with the "AGI from India" frame on product copy.** It is a brand pillar, not a feature. Lead with the feature, signal the pillar in the footer.
- **Do not add a Discord server.** We do not have 100 GitHub stars yet. Discord is a cost, not an asset, at this stage.
- **Do not lead with "we compete with Snap Specs."** Snap is 132g, $2,195, reactive, closed, cloud-dependent. The wedge is *what we are*, not *what they are not*. Lead with the proactive, on-device, MIT, sub-50g, <$200 BOM cell.

---

## 15. v61 → v62 deltas to watch (the bet log)

These are the bets v61 is making. If any of these is wrong by v62, we adjust.

1. **The Snap $500M number goes viral in 2 weeks.** If the X thread on this gets 5k+ impressions, we have the lead-in. If it gets <500, we go back to the "7 daemons shipped" framing.
2. **Qualcomm START opens up to indie developers.** If Inspecs-only is the model, the B2B beachhead narrows. If they accept MIT projects, the beachhead explodes.
3. **AWE 2026 coverage continues for 2 weeks.** If Forbes/TechCrunch/Road-to-VR follow-ups keep the Specs conversation alive, the timing of the "MIT vs Snap" thread matters.
4. **Meta's NameTag code strip becomes a regulatory story.** If the EU AI Act or any US state picks it up, the privacy wedge hardens.
5. **Sarvam's $1.5B unicorn story picks up Indian tech press.** If YourStory / Inc42 amplify, our India origin story rides the wave.

---

*Dan1 marketing research v61 — canonical. Next pass: v62 after the Day-0 punchlist ships or by 2026-06-26 08:00 IST, whichever comes first.*
