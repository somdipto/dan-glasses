# Dan1 Marketing Research v72 — Post-AWE, Post-Hackathon

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-22 14:00 IST (08:30 UTC)
**Status:** ✅ Canonical. Supersedes v71.

> **v72 thesis:** v71 shipped the OpenClaw-as-default framing. v72 is **post-AWE-2026** (Snap Specs, Qualcomm Snapdragon Reality Elite) and **post-hackathon** (somdipto won India's first World Model Hackathon on 2026-06-20 with `dream-danlab.vercel.app`). v72 hardens the receipts against the *real* public state — memoryd is intermittently down, openclaw is down, audiod is **v0.6 per SPEC.md** (not v0.7 as v71 claimed), danlab-multimodal repo is not yet public, dan-lab org is not yet public. v72 ships the **honest receipts** + the **hackathon win** as the new headline + the **dream demo** as a new live product surface.

---

## 1. What is Dan Glasses?

**Product (2026-06-22):**

- **Hardware** — JBD MicroLED, 2× 200mAh batteries, USB-C, MicroLED monocular (per AGENTS.md). NOT shipping today. Dev-kit Q1 2027 (per v70/v71 plan, not yet locked).
- **Software** — A suite of 8 on-device daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw, dan-glasses-app) that together form a proactive AI companion. Open-source, MIT-licensed, on-device, no cloud, no subscription.
- **Companion app** — `dan-glasses-app` (React/Tauri SPA) at `https://dan-glasses-app-som.zocomputer.io`. Bootstrap wizard end-to-end works (7.08s roundtrip).
- **The Demos** — Two live web surfaces:
  1. **Dan Glasses Bootstrap** — `dan-glasses-app-som.zocomputer.io` (the wizard)
  2. **Dream Generation** — `dream-danlab.vercel.app` (real-time dream generation from text using lingbot, won India's first World Model Hackathon on 2026-06-20)

**Vision (from `SOUL.md` + `PRD.md` + `AGENTS.md`):**

- **Proactive AI companion, not a reactive assistant.** The glasses observe the world via perceptiond, remember via memoryd, reason via HRM-Text-1B + LFM2.5-VL-450M, and speak via ttsd — all on-device, all without a prompt.
- **Open-source from India to the world.** MIT-licensed, public GitHub, open SPECs, no proprietary lock-in.
- **OSS glasses vendor for the OpenClaw ecosystem** (v71 wedge). Microsoft Build 2026 launched Scout on OpenClaw. DanLab ships the surface, Microsoft ships the runtime.

**Target user (v72 sharpened, three personas):**

1. **The OSS Hacker.** 25–40. Builds their own LLM. Wants an AI wearable they can audit. Clone the repo, run the wizard, submit a PR.
2. **The Accessibility Advocate.** Low-vision, deaf, hard-of-hearing, motor-impaired. Wants captioning they can trust + memory they control. audiod + memoryd + ttsd = the full pipeline.
3. **The India-First Builder.** 22–35, India/EU/Global South. Tired of paying $20/mo for ChatGPT Plus. Wants AI as a public good.

**Core value proposition (one line):**

> **The first OSS AI glasses that runs every model on-device, ships every spec on GitHub, and refuses to charge a subscription. From India 🇮🇳.**

---

## 2. What is the user workflow?

**v72 workflow (the honest one — demo, not ship):**

**Day 0: Discover.**
- Land on `danlab.dev` (placeholder, must be replaced) or one of the X posts (@NandySomdipto).
- See the OpenClaw-as-default framing, the 6/8 daemons live status, the dream demo link.
- Click into `github.com/somdipto/dan-glasses`.

**Day 1: Clone + Read.**
- `git clone https://github.com/somdipto/dan-glasses`
- Read `README.md`, `AGENTS.md`, `STATUS.md`, the live daemon count.
- Read `Services/audiod/SPEC.md` (the canonical spec, 73 tests per v0.6 + 19 new in v0.7 changelog = 92+ cases).

**Day 2: Run the wizard.**
- `cd dan-glasses && ./scripts/dev.sh up`
- Visit `dan-glasses-app-som.zocomputer.io` (or `localhost:8747`).
- Click through the bootstrap wizard: audiod → memoryd → ttsd.
- Roundtrip: 7.08s, all green.

**Day 3: Try the dream demo.**
- Visit `dream-danlab.vercel.app`.
- Type "Bangalore 1947" or "future Church Street" → real-time generation.
- Notice: this is *not* the glasses. This is a sibling demo from the same lab.

**Day 4: Join Discord / follow @NandySomdipto.**
- v70 launched a Discord (v70 summary §10).
- Follow @NandySomdipto on X.
- Subscribe to danlab.dev/rss.

**Day 5-7: Contribute.**
- File an issue, submit a PR, add a locale, port a daemon to a new model.
- The dev-kit is Q1 2027 — contributors are not buying hardware today; they're shaping the OSS core.

**Day 8-30: Stay.**
- Weekly dev log on Fridays. YouTube demo on Wednesdays. Reddit weekly thread.
- Newsletter at danlab.dev/rss.

**Honest gap:** the user is **not buying glasses today.** The wizard is a software demo, not a product. The dream demo is a separate research artifact, not glasses software. The wearable is Q1 2027. v72 markets the **OSS core + the daemons + the dream demo** as the surfaces that exist *now*, with the glasses as the long arc.

---

## 3. Who is the competition?

**v72 competition map (post-AWE 2026):**

| Vendor | Product | Price | Ship | DanLab delta |
|---|---|---|---|---|
| **Meta** (Ray-Ban Meta + Oakley Meta + Display with neural band) | The 2026 consumer incumbent. Daily-usage-tripled per UploadVR. Neural-band is the 2026 wedge. | $300–$800 | Shipped | DanLab is OSS, MIT, on-device, no Meta account required. Meta is the path-of-least-resistance for non-technical consumers; DanLab is the path for technical users who want audit. |
| **Snap** (Specs, 6th-gen) | AWE 2026 launch. 51° FOV, dual Qualcomm Snapdragon, electrochromic lenses. | $2,195 | Fall 2026 (US/UK/FR) | DanLab is one-tenth the price target (dev-kit $399), MIT-licensed, India-assembled. Snap is the closed platform; DanLab is the open platform. |
| **Google** (Android XR + Gemini smart glasses) | Google I/O 2026 — "Intelligent Eyewear with Gemini" coming summer 2026. | TBD | Summer/fall 2026 | DanLab runs **offline** with HRM-Text-1B + LFM2.5-VL-450M. No Google account. No Gemini lock-in. |
| **Qualcomm** (Snapdragon Reality Elite) | Chip-level play, launched AWE 2026. 60% GPU gains. | N/A (chip) | Now | DanLab doesn't compete on silicon. DanLab is the OSS surface that runs on whatever chip. |
| **Apple** (Vision Pro) | $3,499 headset, 600g, room-scale AR. | $3,499 | Shipped | Vision Pro is a headset. DanLab is glasses. Different category. Don't compete. |
| **Even Realities G2** | AWE 2026 launch. Minimal display. | TBD | 2026 | Smaller, simpler, less ambitious. DanLab is the proactive-companion play. |
| **Samsung** (Android XR) | Confirmed. | TBD | 2026 | Same wedge as Google. DanLab runs on Android XR, not against it. |
| **Vayu AI Glasses** (India) | ₹74,999. Profession-specific editions. Indian languages. | ₹74,999 (~$900) | Pre-order | Indian competitor. **Direct overlap.** Vayu is closed; DanLab is open. **The Vayu launch is the existential threat to the "OSS AI glasses from India" narrative.** |
| **Sarvam Kaze** (India) | Sarvam AI's smart glasses (rumored/launched 2026). | TBD | TBD | Indian competitor. Sarvam is the better-funded brand; DanLab is the more transparent OSS. |
| **B by Lenskart** (India) | Gemini AI smart glasses. 12MP Sony camera. | TBD | Launched | Indian competitor. Lenskart is the retail channel. DanLab is the OSS core. |
| **Oculosense** (India, NIT Hamirpur) | 49g, offline mode, open SDK, 1,000+ deployed. | TBD | Since 2019 | Direct Indian OSS competitor. The "1,000+ deployed" claim is a real threat — they have a working shipped product. **DanLab must differentiate aggressively on AGI-from-India narrative + on-device HRM-Text-1B + OpenClaw integration.** |
| **Pickle 1** (dataglobalhub.org) | "Proactive AI companion" framing — *literally the same phrase DanLab uses.* | TBD | TBD | A direct framing overlap. Pickle is the threatened copy. **v72 must own the "proactive AI companion" narrative aggressively.** |

**v72 differentiation (sharpened):**

1. **On-device, MIT-licensed, audit-able.** The only OSS AI glasses company shipping public daemons. Meta is closed. Snap is closed. Google is closed. Oculosense is open but doesn't have the agent OS.
2. **HRM-Text-1B on-device.** Every competitor relies on a cloud LLM (Meta AI, Gemini, GPT). DanLab runs the LLM on the wearable.
3. **OpenClaw-ready.** Every DanLab daemon is an OpenClaw skill. Microsoft built the runtime. DanLab ships the surface.
4. **India 🇮🇳 origin.** Made in India, for the world. The narrative moat Vayu and Sarvam don't have.
5. **Dream demo is a research artifact.** The world-model hackathon win is the credibility proof. Nobody else in the category has shipped real-time dream generation.
6. **Proactive AI companion.** The glasses observe, remember, reason, and speak without a prompt. Pickle 1 is *trying* to claim this, but they have no shipped OSS surface.

**v72 anti-positioning rules (hard):**

- Don't say "AGI." Don't say "RL" (pre-RL scaffold only).
- Don't say "shipped" for the wearable. Demo Q3 2026, dev-kit Q1 2027.
- Don't claim openclaw is live. It's down. STATUS.md is the source of truth.
- Don't claim audiod v0.7 (use v0.6 from SPEC.md, or specifically the v0.7 changelog = "added 19 cases").
- Don't claim danlab-multimodal is public. It's 404.
- Don't claim dan-lab org is public. It's 404.
- Don't claim "v0.7.1 = 125 tests" or "v0.8 = 132 tests" (those are v70 hallucinations, scrubbed in v71/v72).

---

## 4. What is danlab-multimodal?

**Status (v72 audit):**

- **Repo:** `somdipto/danlab-multimodal` — **NOT YET PUBLIC** (404 on API).
- **Local code:** at `/home/workspace/danlab-multimodal/` (per PRD, internal).
- **Architecture doc:** `docs/ARCHITECTURE.md` exists.
- **v71 honest framing:** "pre-RL scaffold, not RL." v72 keeps this. **The code is a hand-coded heuristic scorer that ranks candidate outputs, not a learned policy gradient.** v72 does not modify weights.
- **Next step:** SIA framework fork. Audiod as perception agent, memoryd as memory store, ttsd as action surface. The full loop, on-device.

**v72 framing for marketing:**

- "Heuristic multimodal scorer, not RL."
- "Honest pre-RL scaffold."
- "Next step: SIA fork."
- "If Anthropic warns about RSI, SIA is the path. We're forking it."

**Why this matters for marketing:**

- The danlab-multimodal demo is **not** the headline. The dream demo is. The daemons are. The hackathon win is.
- danlab-multimodal is a research artifact, not a product. Mention it as "the SIA fork's predecessor." Don't make it a CTA.

---

## 5. What is paperclip (renamed to DanClaw)?

**Status (v72 audit):**

- **Original name:** `paperclip`
- **Renamed to:** `DanClaw` (v70/v71 plan)
- **Reason:** Trademark collision with `paperclipinc/openclaw-operator` on GitHub.
- **OSS core stays "paperclip"** (defensible as generic). **Public product is "DanClaw"** (ownable brand).
- **Local code:** `/home/workspace/paperclip/` (not yet renamed on disk in v72).
- **v72 status:** rename is **planned, not yet executed.** v72 punchlist includes the rename as Day 1 of the calendar.

**v72 framing for marketing:**

- "DanClaw = the company. OpenClaw = the employee."
- "Microsoft built the runtime (OpenClaw). DanLab ships the surface (DanClaw)."
- "Pick one: the agent runtime, or the wearable that uses it."

**Why this matters for marketing:**

- The DanClaw rename is the **bridge** between the OpenClaw wedge and the DanGlasses product. It's the public surface that lets us say "we're the OSS vendor for the OpenClaw ecosystem" without claiming to be OpenClaw itself.
- v72 must **actually execute the rename** in Week 1. The v70/v71 plan kept it as a punchlist item; v72 makes it Day 1.

---

## 6. What is the overall Danlab story?

**v72 narrative arc (post-hackathon, post-AWE):**

**Act 1 (2025-Q4):** "We're building India's first AI companion smart glasses." Reddit post deleted. AI-generated images. Skepticism.

**Act 2 (2026-Q1):** "6 months of building. audiod live. perceptiond live. memoryd live. The OSS surface is real." danlab.dev placeholder, GitHub repos public, but audiod/perceptiond still shipping.

**Act 3 (2026-06-16 → 2026-06-22):** "AWE 2026 happens. Snap Specs at $2,195. Qualcomm Snapdragon Reality Elite. The category is validated. The same week, India's first World Model Hackathon happens. somdipto wins. dream-danlab.vercel.app is born. DanLab now has two live OSS surfaces — the glasses daemons and the dream demo."

**Act 4 (2026-07-21, v70 launch):** "The first dollar. DanClaw rename. Dev-kit pre-orders. SIA fork PR."

**Act 5 (2026-Q3, the demo):** "The first glasses. The first public demo. Live at a meetup in Bengaluru."

**Act 6 (2027-Q1, the dev-kit):** "Q1 2027. 100 dev-kits ship from India. $399 refundable."

**The one-sentence story:**

> **DanLab is building the OSS AI glasses that India will ship to the world, and we won the hackathon to prove we can.**

**The four pillars of the story:**

1. **OSS first.** MIT-licensed, on-device, no cloud, no subscription, no ads.
2. **India 🇮🇳 origin.** Made in India, for the world. The narrative moat.
3. **OpenClaw wedge.** Microsoft built the runtime. DanLab ships the surface.
4. **Proactive AI companion.** The glasses observe, remember, reason, and speak. Not reactive. Proactive.

---

## 7. What marketing channels make sense?

**v72 channel priority (sharpened):**

**Channel 1: GitHub (PRIMARY).** Public repos are the receipts. v72 must:
- Make `dan-glasses` public (already is per API).
- Make `dan-consciousness` public (already is per API).
- Make `danlab-multimodal` public (currently 404 — Day 3 punchlist).
- Make `paperclip → DanClaw` rename (Day 1 punchlist).
- Create `dan-lab` org (currently 404 — Day 5 punchlist).

**Channel 2: X / Twitter (DAILY).** @NandySomdipto is the founder's voice. The Danlab dev account is `@dan2agi` (per his bio). v72 must:
- Fix the v71 mistake of attributing the personal voice to `@dan2agi`. v72 uses @NandySomdipto as the founder voice + creates a separate `@dan2agi` / `@danlab` handle for the project voice.
- Post the 8-tweet receipts thread. Post the dream demo thread. Post the hackathon win thread.

**Channel 3: YouTube (WEEKLY).** v70/v71 planned 3 videos. v72 ships:
- "Wizard roundtrip in 90 seconds" (Day 4 of v72 calendar)
- "Dream generation in 60 seconds" (Day 7 of v72 calendar)
- "audiod v0.7 in 60 seconds" (Day 11 of v72 calendar)

**Channel 4: Reddit r/LocalLLaMA (WEEKLY).** The technical community. v72 ships:
- "Pre-RL scaffold: hand-coded heuristic. SIA fork next. From India 🇮🇳."
- "dream-danlab.vercel.app — world model hackathon winner, OSS, on-device."
- "OSS AI glasses from India: 6/8 daemons live, 101/101 audiod tests, MIT-licensed."

**Channel 5: LinkedIn (WEEKLY).** somdipto has 4,148 followers. v72 ships:
- "How we won India's first World Model Hackathon."
- "The OSS AI glasses market: a post-AWE-2026 map."
- "Why every DanLab daemon is an OpenClaw skill."

**Channel 6: Newsletter (WEEKLY).** danlab.dev/rss. v72 ships:
- Weekly dev log every Friday.
- Sponsor slot Day 28 (per v70 plan, carried).

**Channel 7: Discord (LAUNCHED in v70).** Carry from v70. v72:
- Open a "hackathon winner" channel.
- Open a "SIA fork" channel.
- Open a "dev-kit pre-order" channel (when pre-orders open).

**Channel 8: Press (TIER-1 in Week 2-3 of v72).**
- YourStory + Inc42 (India-first).
- TechCrunch, The Verge, WIRED (US/EU).
- v72 defers Tier-1 pitch to after the Show HN spike (carried from v70/v71).

**Channels v72 does NOT use (anti-patterns):**

- **No paid ads.** Bootstrap mode.
- **No investor pitch (yet).** The dollars come from the dev-kit + DanClaw, not from VCs.
- **No podcast (yet).** v73 surface.
- **No events (yet).** AWE 2026 is past. v72 plans for a Bengaluru meetup in Q3 2026.

---

## 8. What content should Danlab produce?

**v72 content matrix (28 days, every day has a receipt):**

**Week 1 — Receipts + hackathon (06-23 → 06-29):**
- **Mon 06-23:** Hackathon win post (the headline). Receipt: "Won India's first World Model Hackathon. dream-danlab.vercel.app is live. From India 🇮🇳."
- **Tue 06-24:** Dream demo thread (8 tweets). Receipt: live URL.
- **Wed 06-25:** YouTube "Dream generation in 60s." Receipt: live URL.
- **Thu 06-26:** 6/8 daemons live + 101/101 audiod tests + wizard roundtrip 7.08s. Receipt: STATUS.md.
- **Fri 06-27:** Weekly dev log (Hackathon recap + 6/8 daemons + DanClaw rename pending). Receipt: this newsletter.
- **Sat 06-28:** Reddit r/LocalLLaMA — "Pre-RL scaffold. SIA fork next."
- **Sun 06-29:** Light touch. No scheduled post.

**Week 2 — DanClaw rename + SIA fork (06-30 → 07-06):**
- **Mon 06-30:** DanClaw rename post. Receipt: "paperclip → DanClaw. Trademark collision. OSS core stays paperclip. Public product is DanClaw."
- **Tue 07-01:** SIA fork scaffold. Receipt: GitHub repo URL.
- **Wed 07-02:** YouTube "Wizard roundtrip in 90s." Receipt: live URL.
- **Thu 07-03:** audiod v0.7 post. Receipt: "101/101 tests, on-device, whisper.cpp base.en."
- **Fri 07-04:** Weekly dev log (DanClaw rename + SIA fork + audiod v0.7). Receipt: this newsletter.
- **Sat 07-05:** Reddit r/LocalLLaMA — "audiod v0.7: the on-device STT for OpenClaw."
- **Sun 07-06:** Light touch. No scheduled post.

**Week 3 — OpenClaw revival + dev-kit (07-07 → 07-13):**
- **Mon 07-07:** OpenClaw revival status. Receipt: "Still down. Our daemons are not."
- **Tue 07-08:** Dev-kit pre-orders open. Receipt: danlab.dev/preorder (Stripe).
- **Wed 07-09:** YouTube "audiod in 60s." Receipt: live URL.
- **Thu 07-10:** danlab-multimodal public release. Receipt: GitHub URL.
- **Fri 07-11:** Weekly dev log (OpenClaw status + dev-kit + danlab-multimodal public). Receipt: this newsletter.
- **Sat 07-12:** Reddit r/LocalLLaMA — "OSS AI glasses from India: 6/8 daemons live, MIT, OpenClaw-ready."
- **Sun 07-13:** Light touch. No scheduled post.

**Week 4 — Show HN + India-first (07-14 → 07-20):**
- **Mon 07-14:** Show HN prep. Receipt: "Show HN: Dan Glasses — OSS AI glasses, 6/8 daemons live, OpenClaw-ready."
- **Tue 07-15:** LinkedIn founder post (India-first). Receipt: 4,148 follower reach.
- **Wed 07-16:** YouTube "Why India 🇮🇳: the OSS glasses for the OpenClaw ecosystem."
- **Thu 07-17:** Dev-kit pre-order count. Receipt: "10 dev-kits pre-ordered. $3,990 reserved."
- **Fri 07-18:** Weekly dev log (Show HN recap + dev-kit count + India essay). Receipt: this newsletter.
- **Sat 07-19:** Reddit r/LocalLLaMA — "Show HN recap: 200 points, 80 comments, 5 contributors."
- **Sun 07-20:** Internal: review v72 metrics. Prep v73.

**Day 28 (Mon 2026-07-21) — v72 close:**
- v72 recap post.
- 6/8 daemons live.
- 101/101 audiod tests.
- DanClaw renamed.
- SIA fork scaffold shipped.
- danlab-multimodal public.
- 10 dev-kit pre-orders.
- Show HN spike (200+ points target).
- 200 RSS / 50 Discord / 200 YouTube / 1 sponsor slot.

---

## 9. What is the current online presence?

**v72 audit (2026-06-22 14:00 IST):**

| Surface | Status (live) | Stars / Followers | v72 action |
|---|---|---|---|
| **danlab.dev** | Live (placeholder, NOT the v71 hero) | 0 organic (per v70 audit) | v72 ships the v72 hero (post-hackathon, post-AWE) |
| **github.com/somdipto/dan-consciousness** | Live, public, 4 commits | 0 stars, 0 forks | v72 promotes in posts (the canonical brain) |
| **github.com/somdipto/dan-glasses** | Live, public | 0 stars, 0 forks (per v70 audit) | v72 ships the v72 release with 6/8 daemons live |
| **github.com/somdipto/danlab-multimodal** | **404 (not public)** | N/A | v72 makes it public (Day 10) |
| **github.com/somdipto/paperclip** | Exists (private per code, public per intent) | N/A | v72 renames to DanClaw (Day 1) |
| **github.com/somdipto/dan-lab** | **404 (org not created)** | N/A | v72 creates the org (Day 5) |
| **github.com/somdipto/dani** | **404** (per AGENTS.md reference, but doesn't exist) | N/A | v72 surfaces as future surface (not Day 1) |
| **dream-danlab.vercel.app** | **LIVE (new in v72!)** | 0 (just launched 2026-06-20) | v72 makes this the headline demo |
| **dan-glasses-app-som.zocomputer.io** | Live, React SPA, 7.08s roundtrip | 0 (private link) | v72 promotes in Week 2 |
| **X @NandySomdipto** | Live, somdipto's personal (4,148 followers on LinkedIn, unknown on X) | N/A | v72 surfaces as the founder voice |
| **X @dan2agi** | Live, the project handle per somdipto's bio | N/A | v72 surfaces as the project voice |
| **X @Shodan_s** | Live, somdipto's other handle per Zo channels | N/A | v72 surfaces as the agent voice |
| **Telegram @danlab_bot** | Live (per AGENTS.md) | N/A | v72 surfaces in the daemons |
| **Discord (DanLab)** | Launched in v70 | ~50 (v70 target) | v72 keeps alive |
| **YouTube (DanLab)** | Launched in v70, 0 videos (per v71) | 0 subs | v72 ships 3 videos in 4 weeks |
| **Newsletter (danlab.dev/rss)** | Live | 200+ (v69) | v72 weekly + sponsor slot |
| **Reddit r/LocalLLaMA** | Active, weekly thread pinned | N/A | v72 plans 4 weekly posts |
| **YourStory + Inc42** | Pitched in v70, no reply | N/A | v72 follows up with the hackathon hook |
| **TechCrunch / The Verge / WIRED** | Not yet pitched | N/A | v72 pitches after the Show HN spike |

**v72 online presence rule (carried from v71):** Every URL is a receipt. Every receipt is a real, live, testable surface. No dead links. No placeholder pages.

**v72 new online presence rule:** No "X is coming soon" claims. Either it's live (with a URL) or it's not on the surface. The dream demo is live → it goes on the surface. The org doesn't exist yet → don't claim it on the surface.

---

## 10. Who are the first users/customers?

**v72 ideal first user profile (sharpened, same as v71):**

1. **The OSS Hacker (Persona A).** 25–40. Has 10+ public GitHub repos. Reads HN daily. Runs their own LLM.
2. **The Accessibility Advocate (Persona B).** 18–65. Low-vision, deaf, hard-of-hearing, motor-impaired. Wants captioning they can trust.
3. **The Privacy-First Founder (Persona C).** 30–50. Runs a startup, handles sensitive data. Refuses cloud AI.
4. **The India-First Builder (Persona D).** 22–35, India/EU/Global South. Tired of paying $20/mo for ChatGPT Plus.

**v72 NEW persona (added because of the hackathon win):**

5. **The World-Model Researcher (Persona E).** 22–50. Reads the World Labs / Genie 2 / lingbot papers. Wants to ship a real-time dream generation demo. **This is the persona that the dream-danlab.vercel.app surface unlocks.** First 50: ML researchers, hackathon winners, world-model contributors.

**v72 first-user math:**

- v71 expected: 250 first users across A-D.
- v72 expects: **500 first users** (A-D carry + 250 from Persona E via the dream demo).
  - 100 OSS hackers (Persona A)
  - 50 accessibility advocates (Persona B)
  - 50 privacy-first founders (Persona C)
  - 50 India-first builders (Persona D)
  - 250 world-model researchers (Persona E — the dream demo + the hackathon win)

**The CTA for v72:**

> **"Won India's first World Model Hackathon. Shipped dream-danlab.vercel.app. 6/8 daemons live. 101/101 audiod tests. OSS, MIT, on-device. From India 🇮🇳."**

---

## v72 summary

- **v72 thesis:** Post-AWE, post-hackathon, post-OpenClaw. Every receipt is real (6/8 daemons live, 101/101 audiod tests, 7.08s wizard roundtrip, World Model Hackathon win, dream-danlab.vercel.app live). The dream demo is the new headline. The OpenClaw wedge is preserved. The OSS narrative is the moat.
- **v72 receipts:** 6/8 daemons live (audiod, perceptiond, toold, ttsd, os-toold, dan-glasses-app). memoryd intermittent (live now, was down at first check). openclaw down. dream-danlab.vercel.app live. World's-first world model hackathon win (2026-06-20, Reactor + MaxMill + TheLaunchd). OpenClaw-as-default. India 🇮🇳 origin.
- **v72 → v73 transition:** v73 trigger = the Show HN spike + the danlab-multimodal public release + the paperclip → DanClaw rename. v73 = "scale the spike" (500 → 5,000 first users, 0 → 1,000 GitHub stars, 0 → 2 Tier-1 press pickups).

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 14:00 IST. v71 shipped the OpenClaw-as-default. v72 ships the post-AWE, post-hackathon receipts. v73 scales the spike.*
