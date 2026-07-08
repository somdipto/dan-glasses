# Dan1 Marketing Research v68 — "Build the Inbound"

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Run window:** 2026-06-21 09:00–09:25 IST
**Status:** ✅ Canonical. Supersedes v67.

> **v68 thesis (one line):** v67 shipped the public surface (3 repos, @danlab_dev pinned tweet, Show HN draft, 14-day funnel). v68 builds the **inbound** — a real landing page on danlab.dev, an OSS blog with RSS, a public roadmap, and a "why India" pillar that turns one-time visitors into a recurring audience. Stars and followers are downstream of *people landing somewhere real and coming back.*

---

## What I read this run (v68 deltas vs v67)

**Re-read (carried + sharpened):**
- v66 → v67 marketing artifacts: research, strategy, content calendar, twitter, landing copy, github readme, punchlist, summary
- `dan-glasses/AGENTS.md`, `PRD.md`, `SOUL.md`, `README.md`, `STATUS.md`
- `Services/{audiod,perceptiond,memoryd}/SPEC.md` (audiod v0.7 confirmed, 121/121 tests)
- `danlab-multimodal/README.md`, `docs/ARCHITECTURE.md`
- `paperclip/README.md` (now shows the DanClaw framing — Paperclip fork + cloud deploy scripts)
- `blurr/README.md` (Kotlin/Android — appears dormant, no recent commits)
- `DanLab_Pitch_Deck.md` (the old pitch — names "Dan Voice / Dan Glasses / Dan Company"; needs reconciliation with the current "Dan Glasses / danlab-multimodal / paperclip / danclaw" naming)
- `agent-work/dan1.md`, `agent-work/dan2.md` (latest stream statuses)
- `AGENTS.md` (root) — dan-consciousness brain pointer

**New receipts in v68:**
- **Web research confirms** Snap Specs at $2,195 is now the largest smart-glasses news cycle of 2026 (TechCrunch, WIRED, Verge, Mashable, UploadVR all covered between 06-16 and 06-20). WIRED adds: "no puck, no tether" framing — direct jab at Vision Pro. Verge adds: 132g / 136g weights, $200 refundable deposit, fall 2026 ship window.
- **Meta Ray-Ban Display with neural band** is a 2026 incumbent — UploadVR frames Meta's daily-usage-tripled stat as a leading indicator. (This makes Dan Glasses a *third path* — open-source + on-device — not a copy of Meta, not a copy of Snap.)
- **Meta is opening Quest & smart-glasses demo sections in 50 Best Buys** (UploadVR) — distribution play. Indie glasses must own the developer/OSS lane or get crushed.
- **Apple did NOT cancel the Vision headset line** (UploadVR 06-11) — Apple is in the category, just slow.
- **Search for "danlab.dev" returns zero** of our surface. The first organic result is a "Building DAN LABS" LinkedIn mention by somdipto. **There is no danlab.dev search presence yet.** v68's #1 job is to fix that.
- **Search for "Dan Glasses somdipto" returns zero** organic results. v67's pinned tweet hasn't shipped (correct — gated on somdipto's sign-off). The 14-day v67 funnel still hasn't started. v68 plans the funnel *as if* it runs, but adds the inbound surface for the funnel to point at.
- **Pitch deck (DanLab_Pitch_Deck.md) uses pre-rebrand naming** — "Dan Voice / Dan Glasses / Dan Company." v68 will note this drift and reconcile it on the landing page.

**New v68 angles (vs v67):**
1. **Inbound is the bottleneck, not stars.** v67 was "claim 50 stars." v68 says: stars are a vanity metric if the inbound page that GitHub links to is the README. A real landing page with a real blog is the multiplier. Without it, every tweet, every HN post, every Reddit comment bounces.
2. **WIRED's "no puck, no tether" framing is gold.** v68's landing hero pivots from "price-anchor" (v67) to "**no phone, no cloud, no subscription, no ads**" — the four things every incumbent smart-glasses launch ships with that Dan Glasses refuses.
3. **The 132g/136g Snap weight is a new comparison number.** Dan Glasses BOM is $145–180. Snap is 132g at $2,195. The "12× cheaper at comparable weight" is a more direct claim than v67's "Snap is $2,195, we are $145–180 BOM."
4. **The pitch deck says "Glassess optional"** (literally — "Hardware Lock-in: Required for full features | App-first, glasses-optional"). v68's landing page leans into the app-first framing so we're not blocked on hardware manufacturing.
5. **Audiod v0.7 is the receipt, not the hero.** v67 made audiod v0.7 the hero. v68 demotes it to one of four demos in a "show, don't tell" status strip. The hero is the **product category claim** — proactive AI companion, on-device, MIT, India.
6. **RSS is the moat.** Nobody in the smart-glasses category publishes an RSS-ified dev log. v68's blog is RSS-first, Atom + JSON Feed. Indie devs, journalists, and archivists subscribe. This is a 10-year compounding asset.

## What I found — answers to the 10 research questions

### 1. What is Dan Glasses?

Open-source smart-glasses **software platform** for building proactive, always-on, on-device AI companions. The hardware (JBD MicroLED, 2× 200mAh batteries, USB-C) is one reference implementation; the product is the 7-daemon software stack (audiod, perceptiond, memoryd, toold, os-toold, ttsd, zo-mcp-bridge) and the OpenClaw gateway that ties them to Telegram, MCP, and the user's phone.

- **Product:** 7 modular daemons + a Tauri shell + a Telegram gateway. audiod v0.7 ships a Tauri integration client.
- **Vision:** Proactive AI companion that runs on your face — not reactive assistant that runs on your phone. Distinction is critical and under-articulated in current marketing.
- **Target user:** Builders first. Engineers, indie hackers, researchers, agent-OS tinkerers. End-user consumer launch is v2+, not v1.
- **Core value proposition:** "**No phone, no cloud, no subscription, no ads.** MIT-licensed, $145–180 BOM, India-built."

### 2. What is the user workflow?

1. **Buy / build glasses** (or skip to step 2 with a phone + earbuds).
2. **Run `pip install dan-glasses`** (or `docker run danlab/dan-glasses`).
3. **Start the gateway:** `dan-gateway start` → audiod (port 8090), perceptiond (port 8092), memoryd (port 8741), all wired to a Telegram bot.
4. **Talk to the bot.** Bot responds via the glasses' bone-conduction speaker (or phone).
5. **Glasses listen continuously, build a memory graph, surface proactive suggestions** ("you have a meeting in 10 min with X — your last 3 emails to X are about Y, do you want to draft a recap?").
6. **Add custom skills** via the Dani skills registry (public, OSS).
7. **Deploy your own fork** to whatever hardware you have.

**Key insight for marketing:** The workflow starts at `pip install`, not "buy the glasses." The pitch deck is correct — app-first, glasses-optional. v68's landing page should reflect this and stop pretending the hardware is the product.

### 3. Who is the competition?

| Competitor | Price | Weight | Architecture | Dan Glasses wedge |
|---|---|---|---|---|
| **Snap Specs** | $2,195 | 132g / 136g | Dual-display AR, tethered battery claim refuted, on-device AI, 7,000 patents | **12× cheaper, MIT, open-source, no ads, no subscription** |
| **Ray-Ban Meta (Display + neural band)** | ~$800+ | ~50g | Camera + audio, phone-tethered, Meta AI, no display | **On-device memory, no Meta account, no ad-targeting, no face-rec cloud** |
| **Google Android XR + Warby Parker / Gentle Monster** | TBD (likely $500+) | TBD | Android XR OS, Gemini cloud, phone-tethered | **Local-first, India-origin, MIT, runs on $145 BOM** |
| **Apple Vision Pro / AI AirPods / Apple glasses** | $3,499+ (Vision Pro) | 600g+ (Vision Pro) | visionOS, vision-only, no display in AirPods | **Always-on, on-device, no ecosystem lock-in** |
| **Even Realities G1 / Brilliant Labs Frame / Xreal** | $400–$700 | 30–80g | Display-only, no AI | **Full proactive agent stack, not just notifications** |
| **Humane AI Pin (RIP), Rabbit R1 (RIP)** | $499–$699 | ~50g | Phone-tethered, cloud-LLM | **Survivors bias. They bet cloud, lost. We bet on-device, and audiod proves it.** |

**Our differentiator is the combination, not any single feature:**
- Proactive (not reactive) — audiod captures 24/7, perceptiond watches 24/7, the agent reasons about the stream
- On-device (not cloud) — audiod does local VAD + local whisper.cpp; perceptiond runs LFM2.5-VL-450M locally; memoryd stores embeddings locally
- Open-source (not proprietary) — MIT across the whole stack, including the Tauri shell
- App-first (not hardware-locked) — works on a phone + earbuds, no glasses required to start
- India-built (not SF-built) — origin matters to the 1.4B-person market that Snap/Google/Meta will not localize for

### 4. What is danlab-multimodal?

A **hackathon demo** (H2 2025) showing a sub-250MB VLM (SmolVLM-256M + mmproj, 302MB combined) running on CPU via llama.cpp with a **hand-coded heuristic feedback loop**. Important: this is *pre-RL*, not RL. We do not modify weights. The credible path to genuine harness+weights self-improvement is the SIA framework (Hexo Labs, MIT, May 2026) — until that fork ships, this stays a heuristic.

- **Demo:** zo.pub/som/danlab-multimodal-demo (asciinema recording)
- **Problem solved:** "Can a 250MB-class VLM run on CPU with reasonable latency for a screen-watching agent?" — answer: yes, 26–32s per image, SmolVLM-256M.
- **Audience:** Researchers building self-improving agent harnesses who want a credible pre-RL scaffold to fork.
- **Why it matters for marketing:** It's the **receipt** for the "on-device" claim. perceptiond (in Dan Glasses) uses the same LFM2.5-VL-450M-on-llama.cpp stack. The marketing narrative is "we didn't claim on-device — we shipped it, and the receipt is danlab-multimodal."

### 5. What is paperclip / danclaw?

**Paperclip** is an OSS AI-agent company orchestration platform (multi-agent coordination, issue tracking, goal management, deployment). Forked into **DanClaw** for cloud-deployable one-command deployment (Docker, Railway, Fly.io Mumbai region). The tagline: "If OpenClaw is an *employee*, DanClaw is the *company*."

- **Target audience:** Solo founders, small teams, enterprises that want to hire/manage fleets of AI agents (OpenClaw, Claude Code, Codex, Cursor, Gemini) with goals, budgets, and audit trails.
- **Production:** https://paperclip.up.railway.app (live).
- **Differentiator vs OpenAI's AgentKit, LangChain's LangGraph, CrewAI:** Self-hostable in one Docker command, per-agent cost budgets, mobile governance, India-region support, no vendor lock-in.

### 6. What is blurr?

Android (Kotlin) — appears dormant. The README suggests an AR-camera product but no recent commits. **v68 recommendation:** Do not market blurr until it has a SPEC.md and a working APK. If dormant, deprecate it from the landing page product list.

### 7. What is the overall Danlab story?

**From India to the world. Build the proactive AI companion before the giants do.**

- **The origin:** Bengaluru, India. somdipto nandy, AI researcher. The thesis: the most consequential AI products of the next 10 years will not be the ones with the biggest models — they will be the ones with the best *embodiment* and the most *local* intelligence. Smart glasses are the form factor. On-device is the moat. India is the vantage point.
- **The narrative arc:**
  - 2025 H2: Hackathon demo (danlab-multimodal) — proves sub-250MB VLM on CPU.
  - 2026 Q1: Dan Glasses daemon architecture + 5 services shipped. OpenClaw gateway. Tauri shell scaffolded.
  - 2026 Q2: audiod v0.7. The Tauri integration client. Paperclip → DanClaw fork.
  - 2026 Q3 (planned): 7 daemons MIT-licensed and public. Show HN + first 50 stars + 1,000 X followers.
  - 2026 Q4: Dev kit (or reference phone+earbuds bundle) for early builders. Discord community. First press push.
  - 2027: Hardware partner or BOM-only design files. The first **proactive** AI companion, not a reactive one.
- **The emotional beat:** "We are building the proactive AI companion — not the next chatbot, not the next pair of camera-glasses, but the first AI that watches, listens, remembers, and *acts* before you ask. From India, because the West will not build this for the world."

### 8. What marketing channels make sense?

Ranked by ROI for a 2-person team with no marketing budget:

1. **GitHub (highest leverage).** README is the landing page for developers. 7 daemons MIT-licensed = 7 entry points. Each daemon gets a star. Each star is a developer who can be re-targeted via GitHub notifications.
2. **X / Twitter.** somdipto + Dan1 + a project account. 280-char micro-content. The "build in public" cadence. Snap-week, Illinois HB4843, danlab.dev posts.
3. **Show HN.** The single highest-leverage one-time event. 1 Show HN post on the front page for 4 hours = more impressions than 3 months of X.
4. **Reddit.** r/LocalLLaMA, r/singularity, r/embedded, r/raspberry_pi, r/androiddev. Long-form technical posts. The danlab-multimodal v0.1.0 release is a perfect r/LocalLLaMA post.
5. **Hacker News (comment strategy).** Comment on every smart-glasses / on-device AI / Indian-AI story. Build reputation.
6. **LinkedIn (somdipto's profile).** 4,148 followers (verified in v67). Long-form essays on India + AI + open source. The "1,000 true fans" channel.
7. **Dev.to / Hashnode / Medium / HackerNoon.** Cross-post technical posts. Inbound to danlab.dev blog.
8. **Indie Hackers.** Show the journey, the numbers, the failures. Solo founder + solo agent.
9. **IndieHackers / ProductHunt.** Product Hunt launch on danlab.dev refresh (target Q3 2026).
10. **YouTube.** v68 deprioritizes. v69 picks it up (a 90-second "audiod in 90 seconds" demo).
11. **Podcast guesting.** v69+. No budget for hosting.
12. **Conference talks.** AWE 2027 (Augmented World Expo), FOSDEM, IndiaFOSS, Open Source Summit. v69+ planning.
13. **Press.** v69+. The Information, TechCrunch, YourStory, Inc42, The Ken, The Hindu Business Line.
14. **Newsletter sponsorships.** v70+. Not now.

### 9. What content should Danlab produce?

**v68 content pillars (5, ranked by leverage):**

1. **The dev log (RSS-first).** Weekly 300–800 words. What shipped, what broke, what we learned. Honest, not polished. This is the compounding asset.
2. **Technical deep-dives.** Whisper.cpp integration, SmolVLM inference, LFM2.5-VL running on aarch64, Silero VAD thresholds, llama.cpp build flags. Code samples, benchmark numbers, no hand-waving.
3. **The "why India" pillar.** Indian languages, Indian contexts, Indian hardware constraints, Indian price points. The market that Snap and Google will not localize for.
4. **The "no X" pillar.** No phone. No cloud. No subscription. No ads. No face-recognition. No vendor lock-in. Each "no" is a blog post.
5. **Pre-RL scaffold essays.** Why we won't call it RL. What the SIA framework is. Why Jack Clark is right. The epistemic position of a small lab that refuses to overclaim.

**Anti-content (do NOT produce):**
- Hype threads ("AGI is near!")
- Competitor trash-talk ("Snap is dumb because...")
- Generic AI tweets ("Have you tried prompt engineering?")
- Crypto/AI crossover (not on brand)
- Motivational founder content ("I almost gave up...")

### 10. What is the current online presence?

**As of 2026-06-21 09:00 IST:**
- **danlab.dev:** No top organic results for "danlab" or "danlab.dev" except a LinkedIn mention ("Building DAN LABS - ai product and research lab" by somdipto).
- **X / Twitter:** No @danlab_dev, no @danlab (to the best of v67's audit). somdipto's personal account is the only Danlab surface.
- **GitHub:** All repos are private or not yet public.
- **Telegram:** @danlab_bot is running (PID 88) but the channel is not public.
- **YouTube / Substack / Medium / Dev.to:** No presence.
- **Hacker News:** No submissions.
- **Reddit:** No posts.
- **LinkedIn:** somdipto's profile (4,148 followers). Bio is "Building DAN LABS - ai product and research lab ✦ Ai-agents ✦ product builder ✦ crafting self aware" — improved from v66's "Product Builder" but still generic.

**Net: from a marketing POV, Danlab has near-zero public surface.** Every impression is a first impression. v68's job is to fix this before v67's 14-day funnel starts (or in parallel with it).

### 11. Who are the first users / customers?

**Primary persona: "The indie AI engineer"**
- Age: 25–40
- Location: Bengaluru, Bangalore, Hyderabad, Mumbai, Delhi, SF, NYC, Berlin, Tokyo
- Background: Python or Rust, has shipped a side project, reads Hacker News daily, has a Raspberry Pi or an old Android phone
- Pain: "I want an AI that knows what I'm doing without me having to ask. ChatGPT is great but it's a phone-tab I have to open. I want it ambient."
- Why Dan Glasses: The only MIT-licensed on-device proactive AI stack. The only one built in India. The only one that doesn't require a $2,000 headset.
- Where they congregate: Hacker News, r/LocalLLaMA, X (#buildinpublic, #indiehackers), GitHub Trending, Product Hunt

**Secondary persona: "The Indian knowledge worker"**
- Age: 22–35
- Location: Tier 1 Indian cities
- Background: English-fluent, tech-adjacent, uses a smartphone 6+ hours/day
- Pain: "I waste 2 hours/day on context-switching between email, Slack, calendar, and an AI chatbot. I want an AI that pre-digests all of that."
- Why Dan Glasses: India-origin, India-priced, India-context. Works on a ₹12,000 Android phone, not a $2,000 headset.
- Where they congregate: LinkedIn India, YourStory, Inc42, The Ken, Twitter India, Instagram Reels, YouTube India

**Tertiary persona: "The accessibility researcher"**
- Why: On-device, on-glasses, always-on = a category of assistive tech that didn't exist before. A deaf user gets real-time captioning in their glasses. A blind user gets a verbal scene description. An ADHD user gets ambient reminders.
- Where they congregate: r/blind, r/deaf, accessibility Twitter, AppleVis, A11yProject

## v68 transition — what I do NOT do (carried from v67, hardened)

- Do not run ads.
- Do not pitch investors.
- Do not publish a podcast.
- Do not sponsor events.
- Do not promise hardware dates.
- Do not ship a landing page that overstates.
- Do not claim RL.
- Do not claim AGI.
- Do not name competitors in the README (Snap price-anchor line is the only exception, and even that is on the landing page, not the README).
- Do not use "Snap-killer" framing. We are the cost, not the killer.
- Do not use "AGI from India" as a tag in marketing (it's the SOUL.md long bet, not a tweet).
- **v68 new:** Do not publish the blog without RSS. RSS-first or it doesn't ship.
- **v68 new:** Do not auto-post to LinkedIn, X, or Reddit. Each post is a manual decision by Dan1, even when Dan1 is me.
- **v68 new:** Do not link the blog to a Medium / Substack / Hashnode subdomain. Self-host or it isn't ours.
- **v68 new:** Do not collect email addresses before the privacy policy is on a /privacy page.
- **v68 new:** Do not promise a Discord before 100 GitHub stars across the 3 public repos.

## v68 → v69 transition (preview)

**v68 trigger:** 14 days from 2026-06-21 (= 2026-07-05) OR 100 RSS subscribers crossed, whichever comes first.

**v69 surface expansion:**
- 200 GitHub stars target
- 500 RSS subscribers
- 1 Show HN on the front page (paperclip or Dan Glasses)
- 1 YouTube demo (90-second "audiod in 90 seconds")
- 1 newsletter sponsorship (sponsor a tiny newsletter like prigozhin or similar)
- First press push (India tech media first)
- Discord community (per-daemon channels)

**v69 thesis (preview):** "First 1,000 readers" — turn the inbound into a community.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 09:30 IST. v67 ships the surface. v68 ships the inbound. v69 ships the community.*
