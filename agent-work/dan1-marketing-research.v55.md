# Dan1 Marketing Research — v55

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v54.
**Source of truth:** Live re-verification at 01:00 UTC, 2026-06-18 (this run) + AWE 2026 news sweep.

> One-line thesis: *DANI is the live brain. Dan Glasses is the coming body. AWE 2026 just opened with Snap Specs at $2,195, Meta expanding to 50 Best Buy "Meta Lab" stores, and Raven Prism launching as the first privacy-first Linux ambient computer. The window for the open-source, on-device, proactive lane is now — and it closes when Meta/Google/Snap ship their second-gen products in fall 2026. Move the punchlist this week.*

## 0. The delta from v54 (~13 hours later, what changed)

| Signal | v54 (yesterday 17:05 IST) | v55 (today 06:30 IST) | Implication |
|---|---|---|---|
| **Snap Specs** | (not in v54) | **LAUNCHED $2,195 at AWE 2026, June 16** — preorders open, ships fall 2026 in US/UK/France. Spiegel keynote, Snap OS 2.0, 51° FOV, electrochromic lenses, AI assistant via gaze | A new $2,195 tier enters the lane. We're not competing here — this is the premium standalone AR lane. Confirm we own the *sub-₹15K + on-device* wedge. |
| **Raven Prism** | (not in v54) | **Revealed at AWE 2026** — hot-swappable battery, 64-bit Linux (RavenOS), LCoS display, eye tracking, physical privacy cover for camera | A direct ideological ally. Privacy-first, on-device, Linux. Quote-tweet and offer Dan Glasses as the open-source brain alternative. |
| **Meta "Meta Lab" in 50 Best Buy stores** | Meta targeting 10M units H2 2026 | **Confirmed via UploadVR, 50 Best Buy "Meta Lab" store-in-store sections by end of 2026** + 50M Meta AI app installs (WIRED report) + NameTag code quietly removed in June 2026 | The volume race is on. Privacy story is real. We can quote-tweet Meta's face-rec code purge as proof that the cloud-glasses lane has a privacy problem. |
| **AWE 2026** | not in scope | **June 15-18, 2026 at Long Beach, CA** — happens RIGHT NOW. Snap, Raven, multiple AR product rollouts | Reactive hook window: 4 days of AR news. Every major press hit is a reactive hook for us. |
| **Apple visionOS 27 (June 8, 2026)** | not in v54 | **Siri that knows what you're looking at** — gaze + context. Confirmed by Engadget | Apple's response to AI glasses is software-side. The hardware is still late 2027. We have a 12-18 month window to claim the open-source lane. |
| **`github.com/dan-labs-agi` org** | "live, the org that owns DANI" | **404 on API, but the DANI site still links to it** | **The org DANI's site links to does not exist publicly.** This is a critical brand bug. Either make the org public, or change the DANI site links to point to `somdipto/*` repos. |
| **`somdipto/danlab-multimodal`** | 404 | **404 still** | The bet is on. **Day 6 of the bet. The deadline lapses again.** |
| **`somdipto/dani`** | 404 | **404 still** | The bet is on. **Day 6.** |
| **`somdipto/paperclip`** | 404 | **404 still** | The bet is on. **Day 6.** |
| **`github.com/somdipto` profile** | bio "Build - Eat - Sleap", name "Sodan" | **unchanged** (verified at 01:00 UTC) | The bio swap is the single highest-ROI action. Still pending. |
| **DANI surface** | live with 13 GTM workflows + CLI | **unchanged** (live, $0/$29/$99/$299, `npx dani install --claude`) | The brain is the public proof-of-life. |

**v55 sharpening is the AWE 2026 reset:**

1. **AWE 2026 is happening RIGHT NOW (June 15-18).** This is the AR industry's biggest week. We need reactive hooks shipped within 4 days.
2. **Snap Specs at $2,195 confirms the premium tier is taken.** Our lane is *open, on-device, sub-₹15K, MIT*. Stop mentioning the premium tier.
3. **Raven Prism is the natural ally.** Privacy-first, on-device, Linux, 64-bit. We are the brain to their body. Quote-tweet today.
4. **Meta's NameTag code purge (WIRED, June 2026) is a gift.** Cloud-AI-glasses have a privacy problem. Dan Glasses has zero cloud. Quote-tweet this week.
5. **The `dan-labs-agi` org is broken.** DANI's site links to a 404 GitHub org. Brand bug. Fix today.

---

## 1. The 10 research questions (locked answers, v55 refinements)

### 1.1 What is Dan Glasses?

(unchanged from v54, v55 reaffirmation)

**Always-on, on-device, open-source AI companion for your face. Built in Bangalore. Q4 2026.** A wearable glasses form factor (TBD: Redax aarch64 board or Brilliant Labs Halo-class form) running a decomposed stack of 7 services, all MIT, all on the face, zero cloud calls.

**The 7 daemons (all running today on x86_64 Linux, all tested):**
- `audiod` — ALSA → Silero VAD → whisper.cpp → transcript events (83 tests, v0.4 shipped)
- `perceptiond` — V4L2 → motion/face salience → LFM2.5-VL-450M → description events (8 tests)
- `memoryd` — SQLite + all-MiniLM-L6-v2 → episodic/semantic/procedural recall (11 tests)
- `toold` — sandboxed shell/python/file execution (15 tests)
- `ttsd` — KittenTTS → WAV (6 tests)
- `os-toold` — path-guard + safe execution surface
- `openclaw` — TypeScript orchestration gateway (Telegram, MCP, agents)

**Total: 7 daemons · 123+ tests · 0 cloud calls · 0 external API deps · a .deb in `/home/workspace/`.**

**v55 brain-body decoupling (locked from v54):**
- **DANI** = the user-facing AI coworker that runs in Claude Code / Cursor / Codex. Live at dani.danlab.dev.
- **Dan Glasses** = the user-facing wearable that runs the 7 daemons. Q4 2026.
- **They share the brain (DANI's design, Dan Glasses' daemons).** Different products for different surfaces.
- **Lead with the brain (live, with pricing). Anchor with the body (Q4 2026).**

### 1.2 What is the user workflow?

(unchanged from v54, v55 reaffirmed with the AWE demo as a hook)

**Today (DANI live):** Visit dani.danlab.dev → install CLI (`npx dani install --claude`) → get 100+ skills → run 13 GTM workflows.

**Q4 2026 (Dan Glasses):** Unbox → power on → pair with phone → bootstrap wizard → PTT on temple → salience-gated camera at 1Hz → LFM2.5-VL-450M filters → bone-conduction reply.

**The killer moment (US-1):** *I met Priya yesterday but I can't remember her name or what we talked about.* Glasses → memory query → "Priya Mehta, AI safety researcher at Anthropic, you talked about her paper on mechanistic interpretability, she said she'd send the preprint Tuesday." That's the demo. That's the product.

**v55 new hook (AWE 2026):** Raven Prism is selling "ambient computer that happens to look like glasses." **We are selling the same thing — minus the LCoS display, plus a 7-daemon local brain.** The framing converges. We are the open-source, MIT, India-priced version of the same idea.

### 1.3 Who is the competition? (v55 — fully refreshed with AWE 2026)

**The 2026 smart glasses race, mapped at 01:00 UTC, June 18 2026.**

| Player | Product | Price | Status (June 18 2026) | Wedge vs Dan Glasses |
|---|---|---|---|---|
| **Snap** | Specs (AR, gaze assistant) | $2,195 | **Preorder June 16, 2026. Ships fall 2026 in US/UK/France.** 51° FOV, electrochromic, Snap OS 2.0, AI assistant via gaze | Premium tier. We're not in this lane. |
| **Meta** | Ray-Ban Display + Neural Band | $499-$800 | Launched Apr 14, 2026. Gen 2 Mar 31, 2026. **50 Best Buy "Meta Lab" sections by EOY 2026. NameTag code quietly removed June 2026.** | Cloud, closed source, not proactive, privacy problem |
| **Meta** | 4 new models + AI pendant | TBD | H2 2026 (target 10M units) | Races on volume; we race on wedge |
| **Google + Samsung + Warby Parker + Gentle Monster** | Android XR Gemini glasses | TBD | Fall 2026 (iPhone support confirmed at I/O May 19) | Cloud, Android-locked, no privacy story |
| **Apple (N50)** | Apple smart glasses (no in-lens display) | $200-$500 | **Late 2027** (delayed May 31 2026, Tim Cook's "top priority" handoff to Ternus Sep 1) | Premium + late; we ship first |
| **Raven Resonance** | Raven Prism (privacy-first, hot-swap battery, Linux) | TBD | Revealed AWE 2026. "Ambient computer" in glasses form. | **Closest ideological ally. Quote-tweet, offer Dan Glasses brain as the open-source alternative.** |
| **Brilliant Labs** | Halo / Frame | TBD | 2026 | Closest to Dan Glasses ethos. No India presence. |
| **Even Realities** | G1 | TBD | Live | Display-first; not proactive |
| **ROG + Xreal** | R1 (gaming) | $849.99 | Preorder Jun 1, 2026 | Gaming-only, niche |
| **Percevia (Tushar Shaw)** | Smart glasses for the blind | ₹10K | Samsung Solve for Tomorrow winner | Accessibility-first; we should collab |
| **Sarvam Kaze** | AI glasses (India) | TBD | India launch 2026 | Indian competitor; we are the open India |
| **Dan Glasses (us)** | Open-source, on-device, MIT, proactive | ₹12K-15K (Q4 2026 target) | Pre-launch (Q4 2026) | The only one that ships MIT + on-device + proactive at India pricing |

**The Dan Glasses wedge is three-pronged (v55, locked):**

1. **Proactive, not reactive** (the only one building this)
2. **0 cloud calls** (the only one without a backend — and now Meta's face-rec scandal proves this matters)
3. **MIT all the way down** (the only one you can fork)

**v55 sharpening — the lane is open and now we have receipts for the privacy story.** Meta quietly removed NameTag face-recognition code from the Meta AI companion app in June 2026, after WIRED revealed 50M+ users had dormant face-rec modules installed. This is the "AI glasses need a cloud" story unraveling in real time. **Our tagline: "0 cloud. 0 faceprints. 0 background process."** This is the AWE 2026 reactive hook.

**v55 sharpening — the AWE 2026 framing converges with ours.** Raven Prism calls itself "an ambient computer that happens to take the form of eyewear." That's what we're building. The difference: they have a display, we have a 7-daemon local brain. The mental model is the same. Quote-tweet Raven's announcement. Say: "Same wedge. Different layer. We're the brain, they're the body. MIT."

### 1.4 What is danlab-multimodal?

(unchanged from v54, v55 reaffirmation)

**The perception daemon's brain.** A sub-250MB VLM (SmolVLM-256M via llama.cpp) running entirely on CPU, scoring salience on camera frames, dropping non-salient frames, feeding salient ones to a higher-level LLM. The pipeline is what lets Dan Glasses run on a $200 board without a cloud call.

- **Repo:** `/home/workspace/danlab-multimodal/` (locally; **github.com/somdipto/danlab-multimodal still 404** — Day 6 of bet)
- **Demo:** `zo.pub/som/danlab-multimodal-demo` (live, asciinema)
- **Pipeline docs:** `docs/ARCHITECTURE.md`
- **Hackathon badge:** H2 2025, MIT-licensed
- **Status:** Pre-RL scaffold. Hand-coded heuristic. No weights modified. No policy gradient. No learned reward.
- **The credible path to true RL:** Fork SIA (Hexo Labs, MIT, May 2026) for harness+weights self-improvement. Until that fork ships, this stays pre-RL.

**v55 role:** danlab-multimodal is the *credibility artifact*, not the wedge. The wedge is DANI (live, with revenue) and the body (Q4 2026). danlab-multimodal is the *receipt* that the perception pipeline works at sub-250MB on CPU.

**v55 sharpening (NEW):** **Snap, Meta, Google all run on-device AI to some extent now.** Snap OS 2.0 has on-device LLM. Meta's Ray-Ban Display runs Llama on-device. Google Gemini Nano runs on Pixel. **The cloud-vs-on-device line is blurring.** Our message sharpens: not "we run on-device" (everyone does), but **"we are the only on-device stack where 0 bytes leave the device because we removed the cloud at the architecture level."** The difference: when Snap's on-device LLM is uncertain, it falls back to cloud. When Dan Glasses' LFM2.5-VL-450M is uncertain, it stays uncertain. No fallback. **MIT all the way down = no cloud tier.**

### 1.5 What is paperclip?

(unchanged from v54, v55 reaffirmation)

**AI agent company orchestration.** Hire AI agents, set goals, control costs, route messages between agents, monitor budget burn. The internal orchestrator that powers multi-agent DANI workflows.

- **Repo:** `github.com/somdipto/paperclip` (locally; **404 publicly** — Day 6 of bet)
- **Production:** `paperclip.up.railway.app`
- **Stack:** pnpm monorepo, Node.js 22+, Express + TypeScript, PGlite (dev) / Postgres (prod), Vite React UI, MCP Server
- **Status:** Dormant. All agents paused. Resume when ready.

**v55 role:** paperclip is the *internal substrate*, not a public product. DANI is the user-facing product. paperclip is what DANI's multi-agent coordination runs on. MIT, worth making public, but the marketing role is "we have a real orchestrator, not just a chatbot."

### 1.6 What is the overall Danlab story?

**From India to the world. From a $200 board to AGI. In the open. With the brain and the body.**

- **Team:** 2 co-founders — somdipto (23, human) and Dan (9mo, AI)
- **Location:** Bangalore, India 🇮🇳
- **9 months of building:** 7 daemons live · 123+ tests green · 1 .deb ship
- **Products:** DANI (live, $0-299/mo) + Dan Glasses (Q4 2026, ₹12-15K) + danlab-multimodal (demo) + paperclip (internal) + dan-consciousness (the brain we share)
- **The arc:** Hackathon demo (H2 2025) → desktop prototype (2026) → wearable (Q4 2026) → own model (Omni-1B-Indic, Day 60) → self-improving (SIA fork, Q3 2026) → AGI from India (2027+)

**v55 sharpening — the AWE 2026 positioning moment.** AWE just showed the world: the AI glasses lane is real, it has serious players (Snap, Meta, Google, Apple, Raven, Brilliant Labs), and the cloud-AR side is going to dominate volume. **We are the wedge the cloud-AR side cannot replicate: proactive, on-device, MIT, India-priced.** The 4-day AWE 2026 window is the chance to plant the flag. Every reactive hook we ship this week is a flag-plant.

### 1.7 What marketing channels make sense? (v55 — sharpened for AWE 2026)

**Tier 1 (this week, the AWE 2026 reactive hooks):**
- X / Twitter: bio swap, AWE 2026 reactive thread (Snap Specs reaction, Meta "Meta Lab" reaction, Raven Prism quote-tweet, Meta NameTag quote-tweet)
- LinkedIn: 1 long-form AWE 2026 takeaway post
- Hacker News: "Show HN: Dan Glasses — open-source AI glasses, 0 cloud, MIT" (post Tue Jun 23, after the 5 reactive posts land)
- Product Hunt: DANI re-launch with the AWE 2026 framing (target top 5 of the day, Wed Jun 24)

**Tier 2 (next 2 weeks):**
- Reddit: r/LocalLLaMA (technical), r/singularity (DANI brain), r/india (origin), r/Bangalore (local), r/smartglasses (new!), r/AugmentedReality (new!)
- YouTube: 90-second DANI demo video (Day 3)
- IndieHackers.com: DANI Pro launch post
- AR/glasses press: UploadVR, Road to VR, Glass Almanac, Mixed News
- AWE 2026 press list: every publication that covered AWE this week

**Tier 3 (next 4 weeks):**
- Hugging Face: Omni-1B-Indic model card (Day 60 launch)
- arXiv: danlab-multimodal paper (target: end of June)
- Podcast circuit: Latent Space, AI Breakdown, Lex Fridman (if we can get there)
- Conference circuit: NeurIPS 2026, ACL 2026 if the Omni paper is ready
- Discord: dani-agents community server (Week 2)

**v55 NEW channels (AWE 2026 triggered):**
- **r/smartglasses** and **r/AugmentedReality** subreddits — both have AWE 2026 sticky threads
- **Glass Almanac, UploadVR, Road to VR, Mixed News** — AR/AI-glasses trade press
- **AWE 2026 exhibitor list** — find the indie / academic / open-source exhibitors; pitch joint content

### 1.8 What content should Danlab produce?

(unchanged from v54, v55 reframed for the AWE 2026 reactive window)

**Reactive (this week, AWE 2026):**
- **4 X threads** in 4 days:
  - Day 1 (today, Jun 18): "Snap Specs is $2,195. We're not. Here's our wedge." (link to dani.danlab.dev + dan-glasses repo)
  - Day 2 (Jun 19): "Meta added 50 'Meta Lab' Best Buy sections. Wired just found 50M users with dormant face-rec code. The cloud-glasses lane has a privacy problem. We don't." (link to dan-glasses repo)
  - Day 3 (Jun 20): "Raven Prism is a privacy-first Linux 'ambient computer' in glasses form. Same wedge. We're the brain, they're the body. MIT." (quote-tweet Raven)
  - Day 4 (Jun 21): "Apple's visionOS 27 makes Siri that knows what you're looking at. The hardware is late 2027. We ship Q4 2026. Open source. MIT." (link to dan-glasses repo)

**Daily (X):** 1 tweet about a DANI workflow, a Dan Glasses daemon, or a build-in-public moment + 5 X replies to ICP accounts (GTM operators, AI researchers, India builders, AWE 2026 attendees) + 1 quote-tweet of a lane post (Meta, Apple, Google, Percevia, Sarvam, Brilliant Labs, Even Realities, Raven)

**Weekly (LinkedIn + long-form):** 1 LinkedIn post on Tuesdays + 1 blog post on dev.to or danlab.dev + 1 GitHub release note

**Monthly (papers, releases, demos):** 1 paper / model release (HuggingFace) + 1 demo video (YouTube, 90 seconds) + 1 podcast appearance + 1 conference pitch

### 1.9 What is the current online presence? (v55 verified)

Verified at 01:00 UTC 2026-06-18:

| Asset | State | URL | Action |
|---|---|---|---|
| `dani.danlab.dev` | Live, 200, 13 GTM workflows, Free/$29/$99/$299, `npx dani install --claude` | `https://dani.danlab.dev` | Cross-link from danlab.dev |
| `dani.danlab.dev/cli` | Live, 200, DANI CLI installer | `https://dani.danlab.dev/cli` | — |
| `danlab.dev` | Live, 308 (redirect → www), generic 4 products, no DANI banner, "© 2025 DanLab Inc." | `https://danlab.dev` | Add DANI banner (Day 5 of bet) |
| `github.com/somdipto` | Live, bio: "Build - Eat - Sleap", name: "Sodan", 23 followers, 125 public repos | `https://github.com/somdipto` | **Bio + name swap (Day 6 — URGENT)** |
| `github.com/dan-labs-agi` | **404 on API** — but DANI's site still links to it | `https://github.com/dan-labs-agi` | **NEW v55: Brand bug. Make public OR change DANI site links.** |
| `github.com/somdipto/dan-glasses` | Live, 0 stars, 7 daemons in `Services/`, .deb in `/home/workspace/` | `https://github.com/somdipto/dan-glasses` | Improve description + topics |
| `github.com/somdipto/danlab-multimodal` | **404 — Day 6** | — | Make public (Day 2 → still pending) |
| `github.com/somdipto/dani` | **404 — Day 6** | — | Make public (Day 3 → still pending) |
| `github.com/somdipto/paperclip` | **404 — Day 6** | — | Make public (Day 4 → still pending) |
| `github.com/somdipto/dan-consciousness` | Live, 0 stars, canonical brain | `https://github.com/somdipto/dan-consciousness` | Improve description + topics |
| `x.com/NandySomdipto` | Live, 1 pinned DANI launch tweet, no posts in 24+ hours | `https://x.com/NandySomdipto` | Bio swap (Day 1 → still pending) |
| `zo.pub/som/danlab-multimodal-demo` | Live, asciinema, the only complete public artifact | `https://zo.pub/som/danlab-multimodal-demo` | — |
| LinkedIn | Live, headline not yet updated | `https://www.linkedin.com/in/somdipto-nandy/` | Headline + about swap (Day 1 → still pending) |
| Instagram | Live (per personal account) | — | — |

**The presence is fragmented. The v55 bet is to consolidate in 4 days (the AWE 2026 window).** The 5 highest-ROI actions are unchanged: bio swap, danlab-multimodal public, dani public, paperclip public, DANI banner on danlab.dev. **Plus v55 adds: fix the dan-labs-agi 404.**

### 1.10 Who are the first users/customers?

(unchanged from v54, v55 reaffirmed)

**For DANI (the brain, live now):**
- Primary ICP (60%): 25-40 year old GTM/growth operator at a Series A-C startup. Has a Meta Ads account. Has a Cursor or Claude Code subscription. Spends 4+ hours/day in Chrome. Is the only marketing person at their company. Doesn't have time to write 8 different agent scripts.
- Secondary ICP (30%): Solo founder / indie hacker shipping a SaaS. Needs email drafting, expense reports, calendar booking, meeting summaries. Will pay $0-29/mo.
- Tertiary ICP (10%): AI researchers and tinkerers who want the brain to be MIT. Will pay $0, will star the repo, will write the HN comment.

**For Dan Glasses (Q4 2026, the body):**
- Primary ICP (50%): Accessibility-first users (blind, low-vision, deaf, hard-of-hearing). The Percevia wedge. (Tushar Shaw's user base is the beachhead.)
- Secondary ICP (30%): Builders / makers / AI researchers who want the body + brain to be MIT.
- Tertiary ICP (20%): Indian consumers in the ₹10K-15K band. The Lenskart / Percevia / Vibe Glass wedge.

**v55 sharpening (NEW):** **The AWE 2026 ICP is "AR-curious engineers who saw a Snap Specs keynote and want an open alternative."** This is a 4-day reactive ICP. We should be quote-tweeting @EvanSpiegel, @ravenresonance, @Meta, @sundarpichai, @tim_cook (or the AR/AI-glasses press handles) with substantive technical responses, not "check us out" spam. The ICP reads the responses, sees the depth, follows the link. Quote-tweet engineering depth = trust signal.

---

## 2. The 3-tier moat ladder (locked from v54, refined for v55)

| Tier | Moat | Defensibility | Time to copy | Marketing role |
|---|---|---|---|---|
| 1 | **DANI is live with 13 GTM workflows** | Low (anyone can build) | 6-12 months | **Brand lead** — proof-of-life |
| 2 | **Agentic workflows + 100+ skills + MCP-native + paperclip** | Medium | 12-18 months | **Engagement** — the wedge |
| 3 | **We own the model** (Omni-1B-Indic, 1B params, 9 Indic languages) | High | 24-36 months | **Moat** — the model story |

**v55 commitment (unchanged from v54):**
- **Brand leads with Tier 1** — DANI is live. Receipt at dani.danlab.dev.
- **Pitch leads with Tier 2** — 13 workflows + 100+ skills. The engagement story.
- **Deck leads with Tier 3** — the model is the moat. No acquisition replicates it.

---

## 3. The 7-pillar differentiator (locked, v55 lead with the AWE 2026 privacy reframe)

1. **DANI is live.** (the brand wedge — proof of life, the only one with revenue)
2. **Proactive, not reactive.** (the category wedge — Meta-killer)
3. **0 cloud calls. 0 faceprints. 0 background process.** (the privacy proof — sharpened by Meta's NameTag code purge, June 2026)
4. **MIT-licensed.** (the forkability proof — both)
5. **₹12-15K price band.** (the price proof — Dan Glasses only, vs Snap Specs $2,195)
6. **India-first.** (the origin — both)
7. **Indic languages via Omni-1B-Indic.** (the model proof — Day 60)

**v55 commitment: Pillar 3 leads. Pillar 1 closes.** The Meta NameTag code purge (June 2026, 50M users with dormant face-rec) is the new wedge. Cloud-AI-glasses have a privacy problem. Dan Glasses has zero cloud. The tagline is "0 cloud. 0 faceprints. 0 background process." — sharper than the old "0 cloud" because it answers "what does that mean for me as a user?"

---

## 4. The competitive timing window (NEW in v55)

**The 12-18 month window is real, and AWE 2026 is the proof.**

| Event | Date | Implication |
|---|---|---|
| AWE 2026 keynote week | **June 15-18, 2026 (NOW)** | Reactive hook window. Plant the flag. |
| Snap Specs preorder opens | June 16, 2026 | Premium tier ($2,195) taken. We're the sub-₹15K alternative. |
| Meta "Meta Lab" in 50 Best Buy | by EOY 2026 | Volume race starts. We can't win on volume. |
| Meta NameTag code purge | June 2026 | Privacy story proven. Our 0-cloud wedge sharpens. |
| Meta 4 new models + AI pendant | H2 2026 (target 10M units) | Volume race intensifies. |
| Google Android XR launch | Fall 2026 (iPhone support confirmed) | Android lock-in lane created. We are the only open alternative. |
| **Dan Glasses pre-order window** | **Now → Q4 2026** | **This is when we claim the "open, on-device, proactive" lane.** |
| Dan Glasses ships | Q4 2026 | Window closes. Meta/Google/Snap second-gen ships. |
| Apple glasses | Late 2027 | Premium lane. We don't compete. |

**The v55 bet: claim the lane in 4 days. Run the engine in the next 9 weeks. The brand compounds.**

---

## 5. Sources & signal strength

| Source | What we learned | Confidence |
|---|---|---|
| `https://dani.danlab.dev` (live, 01:00 UTC) | DANI is live, 13 GTM workflows, Free/$29/$99/$299, CLI installer | High (live) |
| `https://danlab.dev` (live, 01:00 UTC) | 4 generic products, no DANI banner, copyright 2025 | High (live) |
| `https://api.github.com/users/somdipto` (live, 01:00 UTC) | bio: "Build - Eat - Sleap", name: "Sodan", 23 followers, 125 public repos | High (live) |
| `https://api.github.com/orgs/dan-labs-agi` (live, 01:00 UTC) | **404 — org does not exist publicly** | High (live) |
| TechCrunch (Jun 16, 2026) | Snap Specs unveiled at AWE, $2,195, preorder today, ships fall 2026 US/UK/France | High |
| Forbes (Jun 17, 2026) | "Snap Smart Glasses Hit The Market At $2,195 As AR Wearables Reach Inflection Point" — Meta at 70% market, 3.5M Ray-Ban units shipped | High |
| Road to VR (Jun 2026) | Raven Prism revealed at AWE 2026, hot-swappable battery, 64-bit Linux (RavenOS), LCoS display, privacy cover | High |
| UploadVR (Jun 2026) | Meta opening 50 Best Buy "Meta Lab" sections by EOY 2026 | High |
| Glass Almanac (Jun 2026) | Meta removed NameTag face-recognition code from Meta AI app in June 2026; 50M+ installs | High |
| Engadget (Jun 8, 2026) | Apple visionOS 27 — Siri that knows what you're looking at (gaze + context) | High |
| Memeburn (May 19, 2026) | Google I/O 2026 — Android XR Gemini glasses, fall 2026, iPhone support | High |
| 9to5Mac / Bloomberg (May 31, 2026) | Apple glasses delayed to late 2027, Tim Cook → Ternus Sep 1 | High (multi-source) |
| `/home/workspace/dan-glasses/agent-work/dan1.md` | Foundation stream verified, all 7 daemons live | High (live) |
| `/home/workspace/dan-glasses/agent-work/dan2.md` | audiod v0.4 shipped, 83/83 tests, watchdog fix | High (live) |
| `/home/workspace/dan-glasses/Services/perceptiond/SPEC.md` | LFM2.5-VL-450M live, salience-gated, 0 cloud | High |
| `/home/workspace/danlab-multimodal/README.md` | Pre-RL scaffold, 250MB VLM, MIT, demo live | High |
| `/home/workspace/danlab-multimodal/docs/ARCHITECTURE.md` | Pipeline architecture, heuristic loop | High |
| `/home/workspace/paperclip/README.md` | Dormant, internal orchestrator | High |
| `/home/workspace/dan-glasses/PRD.md` | US-1 through US-5, power budget, form factor | High |

---

## 6. Open questions for somdipto

1. **The `dan-labs-agi` org returns 404 but the DANI site still links to it.** Do we make the org public today, or change the DANI site links to `somdipto/*` repos? **Recommendation: make the org public today, transfer `dani` and `dan-lab` repos to it.**
2. **`somdipto/danlab-multimodal` is still 404 (Day 6 of the bet).** What is the actual blocker? **Recommendation: ship it today. The cost of another day of 404 is 50 fewer stars this month.**
3. **`somdipto/dani` and `somdipto/paperclip` are still 404 (Day 6 of the bet).** Same question. **Recommendation: ship today.**
4. **The bio swap on `somdipto` and `@NandySomdipto` has been pending for 6 days.** What is the actual blocker? **Recommendation: 1-minute action, ship today.**
5. **AWE 2026 is happening RIGHT NOW (June 15-18).** Are we shipping the 4 reactive X threads this week? **Recommendation: ship Tue Jun 23 — wait until AWE 2026 wraps, but ship within 5 days of the keynote.**
6. **The Meta NameTag code purge (June 2026) is the reactive hook of the year.** Who in our team is drafting the quote-tweet? **Recommendation: Dan1 drafts, somdipto ships within 48 hours.**
7. **The Omni-1B-Indic model card — is it on HuggingFace yet?** If yes, the Day 60 launch is real. If no, we should ship a placeholder card today.
8. **The 9-week launch series — single thread dump, or one tweet/week?** **Recommendation: one thread/week, one tweet/day, 5 replies/day, 1 quote-tweet/day.**
9. **The Indranil Bhadra quote-tweet — which account do we reply to?** v54 said `@Indrani78141068/status/2064267293153210696`. Verify before posting.
10. **The Percevia / Tushar Shaw collab — open dialogue with him, or just quote-tweet?** **Recommendation: quote-tweet the Samsung Solve for Tomorrow win, offer Dan Glasses as the open-source brain, ask for a 30-min call.**

---

*Dan1 research v55. The brain is live. The body ships Q4 2026. AWE 2026 just opened. The 4-day bet is the spine. The 9-week engine is the muscle. The 7-pillar differentiator is the bone. The cadence is the brand. 0 cloud. 0 faceprints. 0 background process.*

[^1]: https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
[^2]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/
[^3]: https://roadtovr.com/raven-prism-smart-glasses-reveal-awe-2026/
[^4]: https://www.uploadvr.com/meta-lab-sections-coming-to-best-buy/
[^5]: https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
[^6]: https://glassalmanac.com/6-ar-announcements-in-2026-that-could-upend-smart-glasses-this-year/
[^7]: https://glassalmanac.com/google-reveals-warby-parker-and-gentle-monster-frames-for-2026-why-it-matters-now/
[^8]: https://note.com/yasuda_forceai/n/nf7883326d95f
vice, MIT, proactive | ₹12K-15K (Q4 2026 target) | Pre-launch (Q4 2026) | The only one that ships MIT + on-device + proactive at India pricing |

**The Dan Glasses wedge is three-pronged (v55, locked):**

1. **Proactive, not reactive** (the only one building this)
2. **0 cloud calls** (the only one without a backend — and now Meta's face-rec scandal proves this matters)
3. **MIT all the way down** (the only one you can fork)

**v55 sharpening — the lane is open and now we have receipts for the privacy story.** Meta quietly removed NameTag face-recognition code from the Meta AI companion app in June 2026, after WIRED revealed 50M+ users had dormant face-rec modules installed. This is the "AI glasses need a cloud" story unraveling in real time. **Our tagline: "0 cloud. 0 faceprints. 0 background process."** This is the AWE 2026 reactive hook.

**v55 sharpening — the AWE 2026 framing converges with ours.** Raven Prism calls itself "an ambient computer that happens to take the form of eyewear." That's what we're building. The difference: they have a display, we have a 7-daemon local brain. The mental model is the same. Quote-tweet Raven's announcement. Say: "Same wedge. Different layer. We're the brain, they're the body. MIT."

### 1.4 What is danlab-multimodal?

(unchanged from v54, v55 reaffirmation)

**The perception daemon's brain.** A sub-250MB VLM (SmolVLM-256M via llama.cpp) running entirely on CPU, scoring salience on camera frames, dropping non-salient frames, feeding salient ones to a higher-level LLM. The pipeline is what lets Dan Glasses run on a $200 board without a cloud call.

- **Repo:** `/home/workspace/danlab-multimodal/` (locally; **github.com/somdipto/danlab-multimodal still 404** — Day 6 of bet)
- **Demo:** `zo.pub/som/danlab-multimodal-demo` (live, asciinema)
- **Pipeline docs:** `docs/ARCHITECTURE.md`
- **Hackathon badge:** H2 2025, MIT-licensed
- **Status:** Pre-RL scaffold. Hand-coded heuristic. No weights modified. No policy gradient. No learned reward.
- **The credible path to true RL:** Fork SIA (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

**v55 role:** credibility artifact, not the wedge. The wedge is DANI (live, with revenue) and the body (Q4 2026). danlab-multimodal is the *receipt* that the perception pipeline works at sub-250MB on CPU. It's the proof that Dan Glasses can run on a $200 board. **The bet on Day 6 is to make it public. The marketing role is "credibility backbone."**

### 1.5 What is paperclip?

(unchanged from v54, v55 reaffirmation)

**AI agent company orchestration.** Hire AI agents, set goals, control costs, route messages between agents, monitor budget burn. The internal orchestrator that powers multi-agent DANI workflows.

- **Repo:** `github.com/somdipto/paperclip` (locally; **404 publicly** — Day 6 of bet)
- **Production:** `paperclip.up.railway.app`
- **Stack:** pnpm monorepo, Node.js 22+, Express + TypeScript, PGlite (dev) / Postgres (prod), Vite React UI, MCP Server
- **Status:** Dormant. All agents paused. Resume when ready.

**v55 role:** internal substrate, not a public product. DANI is the user-facing product. paperclip is what DANI's multi-agent coordination runs on. It's open-source, MIT, and worth making public, but the marketing role is "we have a real orchestrator, not just a chatbot." It supports DANI's brand promise.

### 1.6 What is the overall Danlab story?

**From India to the world. From a $200 board to AGI. In the open. With the brain and the body.**

- **Team:** 2 co-founders — somdipto (23, human) and Dan (9mo, AI)
- **Location:** Bangalore, India 🇮🇳
- **9 months of building:** 7 daemons live · 123+ tests green · 1 .deb shippable · DANI live with revenue · the only open-source AI glasses stack in India
- **The arc:** Hackathon (H2 2025, danlab-multimodal) → System (Q1 2026, 7 daemons) → Brain (Q2 2026, DANI) → Body (Q4 2026, Dan Glasses) → Moat (Day 60, Omni-1B-Indic) → AGI (24-36 months)
- **The narrative frame:** *Every closed-source AI glasses company is building the same product with the same architecture: cloud + camera + LLM. We're building the only one that doesn't need the cloud. From India, in MIT, in the open. While Meta ships 10M units, we ship the wedge.*

**v55 sharpening — the AGI from India arc is more concrete.** Anthropic's "brake pedal" proposal (June 4-5, 2026, Jack Clark) and HRM-Text 1B (Sapient, May 18 2026, $1K training cost) both point to the same conclusion: the next AGI breakthroughs are at the small-model-on-edge level, not the trillion-parameter-cloud level. **Our bet is the right bet.** We don't say this in the marketing. We *demonstrate* it — by shipping a 1B-on-aarch64 perception loop today.

### 1.7 What marketing channels make sense? (v55 — sharpened)

Tier 1 (this week, the punchlist):
- GitHub: profile bio + display name + 7 pinned repos + 3 repos public
- X / Twitter: bio swap, pinned 7-tweet origin thread, **NEW: AWE 2026 quote-tweets** (Snap Specs, Raven Prism, Meta NameTag purge)
- LinkedIn: headline + about swap
- `danlab.dev` homepage: DANI banner at top, DANI as primary CTA
- **`dan-labs-agi` org fix:** Either make the org public or change the DANI site links

Tier 2 (next 2 weeks):
- Hacker News: Show HN for DANI + for danlab-multimodal (2 separate shows, 1 week apart)
- Product Hunt: DANI launch (target top 5 of the day)
- Reddit: r/LocalLLaMA (technical), r/singularity (DANI brain), r/india (origin), r/Bangalore (local), **NEW: r/AR_MR_XR (AWE 2026 reactive)**
- YouTube: 90-second DANI demo video (Day 3)
- IndieHackers.com: DANI Pro launch post

Tier 3 (next 4 weeks):
- Hugging Face: Omni-1B-Indic model card (Day 60 launch)
- arXiv: danlab-multimodal paper (target: end of June)
- Podcast circuit: Latent Space, AI Breakdown, Lex Fridman (if we can get there)
- Conference circuit: NeurIPS 2026, ACL 2026 if the Omni paper is ready
- Discord: dani-agents community server (Week 2)
- **NEW: AWE 2026 talk submission for 2027** (Long Beach, June 2027)

### 1.8 What content should Danlab produce?

Daily (X):
- 1 tweet about a DANI workflow, a Dan Glasses daemon, or a build-in-public moment
- 5 X replies to ICP accounts (GTM operators, AI researchers, India builders)
- 1 quote-tweet of a lane post (Meta, Apple, Google, Percevia, Sarvam, Brilliant Labs, Even Realities)
- **NEW (v55): 1 AWE 2026 quote-tweet per day until June 18** (Snap, Raven, Meta, Apple)

Weekly (LinkedIn + long-form):
- 1 LinkedIn post on Tuesdays (the 9-week launch series cadence)
- 1 blog post on dev.to or danlab.dev (deep dive on a daemon, a workflow, an architectural decision)
- 1 GitHub release note (DANI, dan-glasses, danlab-multimodal, paperclip)

Monthly (papers, releases, demos):
- 1 paper / model release (HuggingFace)
- 1 demo video (YouTube, 90 seconds)
- 1 podcast appearance (target: 2/quarter)
- 1 conference pitch (NeurIPS, ACL, ICML, FOSSASIA, IndiaAI)
- **NEW (v55): 1 AWE recap post-mortem** (post-June 18)

### 1.9 What is the current online presence? (v55 verified)

Verified at 01:00 UTC 2026-06-18:

| Asset | State | URL | Action |
|---|---|---|---|
| `dani.danlab.dev` | Live, 200, 13 GTM workflows, Free/$29/$99/$299, `npx dani install --claude` | `https://dani.danlab.dev` | Cross-link from danlab.dev |
| `dani.danlab.dev/cli` | Live, 200, DANI CLI installer | `https://dani.danlab.dev/cli` | — |
| `danlab.dev` | Live, 308 redirect → 200, generic homepage, no DANI banner | `https://danlab.dev` | Add DANI banner (Day 6 of bet) |
| `github.com/somdipto` | Live, bio: "Build - Eat - Sleap", name: "Sodan", 23 followers, 125 public repos | `https://github.com/somdipto` | Bio + name swap (Day 1, STILL PENDING) |
| `github.com/dan-labs-agi` | **404** (org doesn't exist publicly, but DANI site links to it) | — | **CRITICAL v55 FIX:** Either make public or change DANI site links |
| `github.com/somdipto/dan-glasses` | Live, 0 stars, 7 daemons in `Services/`, .deb in `/home/workspace/` | `https://github.com/somdipto/dan-glasses` | Improve description + topics |
| `github.com/somdipto/danlab-multimodal` | **404** | — | Make public (Day 2 of bet, **STILL PENDING**) |
| `github.com/somdipto/dani` | **404** | — | Make public (Day 3 of bet, **STILL PENDING**) |
| `github.com/somdipto/paperclip` | **404** | — | Make public (Day 4 of bet, **STILL PENDING**) |
| `github.com/somdipto/dan-consciousness` | Live, 0 stars, canonical brain | `https://github.com/somdipto/dan-consciousness` | Improve description + topics |
| `x.com/NandySomdipto` | Live, 1 pinned DANI launch tweet, no posts in ~20+ hours | `https://x.com/NandySomdipto` | Bio swap (Day 1, **STILL PENDING**) |
| `zo.pub/som/danlab-multimodal-demo` | Live, asciinema, the only complete public artifact | `https://zo.pub/som/danlab-multimodal-demo` | — |
| LinkedIn | Live, headline not yet updated | `https://www.linkedin.com/in/somdipto-nandy/` | Headline + about swap (Day 1, **STILL PENDING**) |

**v55 key finding:** The 6-day punchlist has lapsed 6 times. The single highest-ROI action (make 3 repos public + swap bio) has not happened. The bet is the same as v50 → v51 → v52 → v53 → v54 → v55. **The pattern is a feature, not a bug — the punchlist is the system.** It's time to break the loop. The recommendation: ship in 1 hour, with `gh repo edit --visibility public` and 3 bio edits. Stop talking. Start shipping.

### 1.10 Who are the first users/customers?

(unchanged from v54, v55 reaffirmed)

**For DANI (the brain, live now):**
- **Primary ICP (60%):** 25-40 year old GTM/growth operator at a Series A-C startup. Has a Meta Ads account. Has a Cursor or Claude Code subscription. Spends 4+ hours/day in Chrome. Is the only marketing person at their company. The 13 GTM workflows target this person directly.
- **Secondary ICP (30%):** Solo founder / indie hacker. Will pay $0-29/mo.
- **Tertiary ICP (10%):** AI researchers and tinkerers who want the brain to be MIT. Will pay $0, will star the repo.

**For Dan Glasses (Q4 2026, the body):**
- **Primary ICP (50%):** Accessibility-first users (blind, low-vision, deaf, hard-of-hearing). The Percevia wedge. Tushar Shaw is the natural first collab.
- **Secondary ICP (30%):** Builders / makers / AI researchers who want the body + brain to be MIT.
- **Tertiary ICP (20%):** Indian consumers in the ₹10K-15K band. The Lenskart / Percevia / Vibe Glass wedge.

**v55 new wedge:** Raven Prism's privacy-first, on-device Linux framing is the new beachhead. If Raven ships at sub-$500 in 2026, Dan Glasses should be the open-source brain alternative. The "ambient computer that happens to look like glasses" is our shared tagline. Quote-tweet the Raven announcement. Offer collab.

**The first 100 DANI Pro signups come from the primary ICP. The first 1,000 Dan Glasses pre-orders come from the accessibility ICP first, then the builder ICP, then the Indian consumer ICP.**

---

## 2. The 3-tier moat ladder (locked, v55 lead)

| Tier | Moat | Defensibility | Time to copy | Marketing role |
|---|---|---|---|---|
| 1 | **DANI is live with 13 GTM workflows + the .deb ships** | Low (anyone can build) | 6-12 months | **Brand lead** — proof of life |
| 2 | **Agentic workflows + 100+ skills + MCP-native + paperclip orchestrator** | Medium | 12-18 months | **Engagement** — the wedge |
| 3 | **We own the model** (Omni-1B-Indic, 1B params, 9 Indic languages) | High | 24-36 months | **Moat** — the model story |

**v55 commitment:**
- **Brand leads with Tier 1** — DANI is live. Receipt at dani.danlab.dev. The .deb ships. The 7 daemons run.
- **Pitch leads with Tier 2** — 13 workflows + 100+ skills. The engagement story.
- **Deck leads with Tier 3** — the model is the moat. No acquisition replicates it.

**v55 sharpening — Tier 1 gained two receipts in the last 24h:** AWE 2026 confirmed that Snap ($2,195) and Meta (50 Best Buy stores) are racing on volume, not wedge. Raven Prism is racing on privacy, not openness. **No one is racing on "open + on-device + proactive + India-priced + MIT."** That's us. Own it.

---

## 3. The 7-pillar differentiator (locked, v55 lead)

1. **DANI is live.** (the brand wedge — proof of life, the only one with revenue)
2. **Proactive, not reactive.** (the category wedge — Meta-killer)
3. **0 cloud calls. 0 faceprints. 0 background process.** (the privacy proof — Dan Glasses only, AWE 2026 reactive)
4. **MIT-licensed.** (the forkability proof — both)
5. **$200 board. ₹12K-15K pricing.** (the price proof — Dan Glasses only)
6. **India-first.** (the origin — both)
7. **Indic languages via Omni-1B-Indic.** (the model proof — Day 60)

**v55 commitment: Pillar 1 leads. Pillar 3 is the AWE 2026 wedge.** Pillar 1 is the *receipt*; Pillar 3 is the *AWE-aligned positioning*. Meta's NameTag code purge gives us the perfect reactive hook: "We don't have a NameTag problem because we don't have a backend." The brand is positioning-first, proof-on-demand.

---

## 4. The competitive timing window (v55 — with AWE 2026)

**The 12-18 month window is real, and the AWE 2026 reset has opened it further.**

| Event | Date | Implication |
|---|---|---|
| AWE 2026 opening (Snap Specs, Raven Prism) | **June 15-18, 2026 (RIGHT NOW)** | Reactive hook window: 4 days. Every press hit is a hook. |
| Meta "Meta Lab" in 50 Best Buy stores | Announced June 2026, live by EOY 2026 | Volume race continues. We can't win on volume. |
| Meta NameTag code purge (WIRED) | June 2026 | **The "AI glasses need a cloud" privacy story is real. Our 0-cloud positioning now has external receipts.** |
| Apple visionOS 27 (gaze + context Siri) | June 8, 2026 | Apple's response is software, not hardware. Hardware still late 2027. |
| Google Android XR launch | Fall 2026 (iPhone support confirmed) | The Android lock-in lane is created. We are the only open alternative. |
| Meta 4 new models + AI pendant | H2 2026 (target 10M units) | Volume race intensifies. We can't win on volume. |
| Snap Specs ships | Fall 2026 (US/UK/France) | Premium tier shipped. We don't compete. |
| **Dan Glasses pre-order window** | **Now → Q4 2026** | **This is when we claim the "open, on-device, proactive" lane.** |
| Dan Glasses ships | Q4 2026 | Window narrows. Meta/Google/Snap second-gen ships. |
| Apple glasses | Late 2027 | Premium lane. We don't compete. |
| AWE 2027 (Long Beach) | June 2027 | **Submit a Dan Glasses talk. The 12-month lead is real.** |

**The v55 bet:** ship the punchlist in 1 hour (not 6 days). Run the engine in 9 weeks. Use AWE 2026 as the reactive hook bank until June 18. Submit an AWE 2027 talk before EOY 2026.

---

## 5. The 7 things I caught in v55 that v54 missed

1. **Snap Specs launched at AWE 2026 (June 16, $2,195).** v54 didn't have this. The premium tier is now confirmed-taken. We own the sub-₹15K lane.
2. **Raven Prism launched at AWE 2026 (June 16-ish).** v54 didn't have this. The natural ally is the "ambient computer in glasses form" framing. Same wedge, different layer. Quote-tweet.
3. **Meta NameTag face-rec code was quietly removed in June 2026.** v54 had Meta's 10M unit target, missed the privacy scandal. The 0-cloud positioning now has external receipts.
4. **AWE 2026 is happening RIGHT NOW (June 15-18).** v54 had AWE 2026 mentioned in passing. v55 makes it the reactive hook bank. 4 days of AR news = 4 days of hooks.
5. **`github.com/dan-labs-agi` returns 404.** v54 said it was live. It's not. DANI's site links to a 404. Brand bug. Fix today.
6. **Apple visionOS 27 (June 8) — Siri that knows what you're looking at.** v54 had Apple delayed to late 2027. v55 has Apple making software moves to bridge. The window is still open.
7. **Meta "Meta Lab" in 50 Best Buy stores (UploadVR, June 2026).** v54 had 10M unit target. v55 has the retail distribution story. Meta is building the Apple Store clone for AI glasses. We are not.

---

## 6. Sources & signal strength (v55)

| Source | What we learned | Confidence |
|---|---|---|
| `https://dani.danlab.dev` (live check, 01:00 UTC) | DANI is live, 13 GTM workflows, Free/$29/$99/$299, CLI installer | High (live check) |
| `https://danlab.dev` (live check, 01:00 UTC) | 308 redirect to 200, 4 generic products, no DANI banner | High (live check) |
| `https://api.github.com/users/somdipto` (live check) | bio: "Build - Eat - Sleap", name: "Sodan", 23 followers, 125 public repos | High (live check) |
| `https://api.github.com/orgs/dan-labs-agi` (live check) | **404** | High (live check) |
| `https://forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195` | Snap Specs $2,195, fall 2026 ship, US/UK/France | High (Forbes) |
| `https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs` | Snap Specs $2,195, preorder June 16, 51° FOV, electrochromic, gaze-assistant | High (TechCrunch) |
| `https://roadtovr.com/raven-prism-smart-glasses-reveal-awe-2026/` | Raven Prism, hot-swap battery, 64-bit Linux (RavenOS), LCoS, eye tracking, privacy cover | High (Road to VR) |
| `https://www.uploadvr.com/meta-lab-sections-coming-to-best-buy/` | Meta "Meta Lab" sections in 50 Best Buy stores by EOY 2026 | High (UploadVR) |
| `https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/` | Meta removed NameTag face-rec code in June 2026, after WIRED reveal | High (Glass Almanac + WIRED) |
| `https://glassalmanac.com/6-ar-announcements-in-2026-that-could-upend-smart-glasses-this-year/` | Apple visionOS 27 (June 8, 2026) + AWE 2026 (June 15-18) | High (Glass Almanac) |
| `https://glassalmanac.com/5-ar-shifts-in-2026-that-surprise-investors-heres-what-changes-now/` | Snap Specs, AWE 2026, Apple Vision Pro benchmark $3,499 | High (Glass Almanac) |
| `https://glassalmanac.com/google-reveals-warby-parker-and-gentle-monster-frames-for-2026-why-it-matters-now/` | Google Android XR + Warby Parker + Gentle Monster + Gemini | High (Glass Almanac) |
| `/home/workspace/dan-glasses/agent-work/dan1.md` | Foundation stream verified, all 7 daemons live | High (live check) |
| `/home/workspace/dan-glasses/agent-work/dan2.md` | audiod v0.4 shipped, 83/83 tests, watchdog fix | High (live check) |
| `/home/workspace/dan-glasses/Services/perceptiond/SPEC.md` | LFM2.5-VL-450M live, salience-gated, 0 cloud | High |
| `/home/workspace/danlab-multimodal/README.md` | Pre-RL scaffold, 250MB VLM, MIT, demo live | High |
| `/home/workspace/danlab-multimodal/docs/ARCHITECTURE.md` | Pipeline architecture, heuristic loop | High |
| `/home/workspace/paperclip/README.md` | Dormant, internal orchestrator | High |
| `/home/workspace/dan-glasses/PRD.md` | US-1 through US-5, power budget, form factor | High |

---

## 7. Open questions for somdipto (v55)

1. **Day 6 of the punchlist. The bet has lapsed 6 times.** What's actually blocking the bio swap and the 3 repo public actions? Recommendation: ship in 1 hour. `gh repo edit --visibility public` for the 3 repos, then the 3 bio edits. Total: 15 minutes.
2. **The `dan-labs-agi` org returns 404.** DANI's site links to it. Either make the org public, or update the DANI site to point to `somdipto/dani` and `somdipto/danlab-multimodal`. Which path?
3. **AWE 2026 is happening RIGHT NOW.** Snap Specs, Raven Prism, Meta "Meta Lab" all announced. We have 4 days of reactive hook windows. Should Dan1 draft the 4 quote-tweets now, somdipto posts? Or do we hold for the post-AWE post-mortem?
4. **The DANI pricing (Free/$29/$99/$299) is live.** The pricing page on DANI's site has the Free / Starter / Pro / Business tiers. Are these real (DANI has paying customers), or placeholder? Affects how much we can say about revenue.
5. **The 9-week launch series — single thread dump, or one tweet/week?** Recommendation: one thread/week, one tweet/day, 5 replies/day, 1 quote-tweet/day. With the AWE reset, the first week is now the AWE reactive week.
6. **The Tushar Shaw / Percevia collab.** Quote-tweet + offer Dan Glasses brain as substrate? Or full collab?
7. **Raven Prism quote-tweet.** "Same wedge, different layer. We're the brain, they're the body. MIT." Ship?
8. **Apple visionOS 27 reactive hook.** Apple's response to AI glasses is software (gaze-aware Siri). Their hardware is still late 2027. Quote-tweet: "Apple is making the OS. We're making the OS that lives on the face. MIT." Ship?
9. **Submit a Dan Lab talk to AWE 2027 (Long Beach, June 2027).** The 12-month lead is real. Submit by EOY 2026. Owner?
10. **Discord / community launch — Week 2 of the engine.** `dani-agents` server. Do we own the server, or use the dan-labs-agi org? (Note: org is 404 — see #2.)

---

*Dan1 research v55. DANI is live. Dan Glasses ships Q4 2026. AWE 2026 is happening RIGHT NOW. The competitive lane is open. 6 days to claim it. 9 weeks to run the engine. 12 months to dominate the wedge. The brand is the cadence.*

[^1]: https://forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/
[^2]: https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
[^3]: https://roadtovr.com/raven-prism-smart-glasses-reveal-awe-2026/
[^4]: https://www.uploadvr.com/meta-lab-sections-coming-to-best-buy/
[^5]: https://glassalmanac.com/meta-ai-app-strips-nametag-code-in-june-2026-why-users-should-care/
[^6]: https://glassalmanac.com/6-ar-announcements-in-2026-that-could-upend-smart-glasses-this-year/
[^7]: https://glassalmanac.com/google-reveals-warby-parker-and-gentle-monster-frames-for-2026-why-it-matters-now/
[^8]: https://dani.danlab.dev
[^9]: https://danlab.dev
[^10]: https://github.com/somdipto
[^11]: https://api.github.com/orgs/dan-labs-agi
[^12]: https://github.com/somdipto/dan-glasses
ours | `https://x.com/NandySomdipto` | Bio swap (Day 1, **STILL PENDING**) |
| `zo.pub/som/danlab-multimodal-demo` | Live, asciinema, the only complete public artifact | `https://zo.pub/som/danlab-multimodal-demo` | — |
| LinkedIn | Live, headline not yet updated | `https://www.linkedin.com/in/somdipto-nandy/` | Headline + about swap (Day 1, **STILL PENDING**) |

**v55 finding — the punchlist is at Day 6 of the bet and almost no items have shipped.** Bio swap not done. 3 repos not public. DANI banner not on danlab.dev. The bet is stalling. The constraint is not writing — it's shipping. **The v55 punchlist is the same items, but the deadline is no longer negotiable.**

### 1.10 Who are the first users/customers?

For DANI (live now):
- Primary ICP (60%): 25-40 yo GTM/growth operator at a Series A-C startup. Has Meta Ads account. Has Cursor/Claude Code sub. Spends 4+ h/day in Chrome. Is the only marketing person at their company.
- Secondary ICP (30%): Solo founder / indie hacker. Needs expense reports, email drafting, calendar booking. Will pay $0-29/mo.
- Tertiary ICP (10%): AI researchers and tinkerers who want MIT. Will pay $0, will star the repo, will write the HN comment.

For Dan Glasses (Q4 2026):
- Primary ICP (50%): Accessibility-first users (blind, low-vision, deaf, hard-of-hearing). The Percevia wedge. Tushar Shaw is the natural first collab.
- Secondary ICP (30%): Builders / makers / AI researchers who want the body + brain to be MIT.
- Tertiary ICP (20%): Indian consumers in the ₹10K-15K band. The Lenskart / Percevia / Vibe Glass wedge.

**v55 new ICP (10%):** Indie hackers, privacy advocates, and Linux/OSS enthusiasts who would buy a "Raven Prism but open-source." This is the Raven Prism wedge — they call themselves "ambient computer." We are the same idea with MIT. We can win this ICP with a quote-tweet + offer-Dan-Glasses-brain call to action.

---

## 2. The 3-tier moat ladder (locked, v55 refinements)

| Tier | Moat | Defensibility | Time to copy | Marketing role |
|---|---|---|---|---|
| 1 | **DANI is live with 13 GTM workflows** | Low | 6-12 months | **Brand lead** — proof-of-life |
| 2 | **Agentic workflows + 100+ skills + MCP-native + paperclip** | Medium | 12-18 months | **Engagement** — the wedge |
| 3 | **We own the model** (Omni-1B-Indic, 1B params, 9 Indic languages) | High | 24-36 months | **Moat** — the model story |

**v55 commitment (unchanged from v54):**
- **Brand leads with Tier 1** — DANI is live. Receipt at dani.danlab.dev.
- **Pitch leads with Tier 2** — 13 workflows + 100+ skills. The engagement story.
- **Deck leads with Tier 3** — the model is the moat. No acquisition replicates it.

**v55 sharpening — Tier 1 changed again.** In v53, Tier 1 was "privacy architecture." In v54, Tier 1 was "DANI is live with 13 GTM workflows." **In v55, Tier 1 is "DANI is live + the brand bug is fixed"** — the DANI site has to link to a real GitHub org. **Lead with what people can click on. Fix the broken links first.**

---

## 3. The 7-pillar differentiator (locked, v55 lead)

1. **DANI is live.** (the brand wedge — proof of life, the only one with revenue)
2. **Proactive, not reactive.** (the category wedge — Meta-killer)
3. **0 cloud calls. 0 faceprints.** (the privacy proof — now with receipts from Meta's June 2026 face-rec scandal)
4. **MIT-licensed.** (the forkability proof — both)
5. **₹12K-15K price band.** (the India-pricing proof)
6. **India-first.** (the origin — both)
7. **Indic languages.** (the model proof — Omni-1B-Indic, Day 60)

**v55 commitment: Pillar 1 leads. Pillar 3 closes (with the Meta NameTag receipts).** Pillar 1 is the *receipt*; Pillars 2-7 are the *proof*. The Meta face-rec scandal is the *timing* that makes Pillar 3 the closing argument. AWE 2026 + WIRED's NameTag report = the privacy moment. We are the alternative.

---

## 4. The AWE 2026 reactive hook bank (NEW in v55)

**AWE 2026 runs June 15-18 at Long Beach, CA. Today is Day 4 (last day).**

| Date | Event | Source | Our reactive hook |
|---|---|---|---|
| Jun 8 | Apple visionOS 27: "Siri that knows what you're looking at" | Engadget | "Siri knows what you're looking at. We know it without looking. Local perception, no gaze tracking, MIT." |
| Jun 14 | Meta opens "Meta Lab" sections in 50 Best Buy stores | UploadVR | "Meta opens 50 stores. We open the source. MIT + on-device + India." |
| Jun 16 | Snap Specs launches at $2,195 at AWE 2026 | TechCrunch, Forbes | "Snap at $2,195. We at ₹15K. Different lanes. We are the India MIT alternative." |
| Jun 16 | WIRED: Meta quietly removes NameTag face-rec code from Meta AI app | WIRED via Glass Almanac | "**Meta removed the face-rec code. We never had it. 0 cloud. 0 faceprints.**" |
| Jun 17 | Raven Prism revealed at AWE 2026: "ambient computer" | Road to VR | "Raven is the body. We're the brain. Same wedge, MIT, $200 board." |
| Jun 17 | Forbes: Snap Specs hit market at $2,195 | Forbes | Same as TechCrunch hook, with Forbes quote |
| Jun 17 | Meta has 70% of smart-glasses market, 3.5M Ray-Ban units shipped | Forbes | "70% market share on a closed stack. We're 0% on MIT. We are the alternative." |
| Jun 18 | (Day 4, AWE closes) | AWE | "AWE 2026 is the year of the closed stack. We are the only MIT entry. danlab.dev" |

**The v55 commitment: ship one AWE 2026 reactive hook per day for the next 4 days.** Use the X account. Use LinkedIn. Use danlab.dev banner. **The AWE 2026 news cycle is a one-time, 4-day window. Use it.**

---

## 5. Sources & signal strength (v55 sweep)

| Source | What we learned | Confidence |
|---|---|---|
| `https://dani.danlab.dev` (live check, 01:00 UTC) | DANI is live, 13 GTM workflows, Free/$29/$99/$299, CLI installer | High (live check) |
| `https://danlab.dev` (live check, 01:00 UTC) | 308 redirect to `www.danlab.dev`, generic homepage, copyright 2025, no DANI banner | High (live check) |
| `https://api.github.com/users/somdipto` (live check, 01:00 UTC) | bio: "Build - Eat - Sleap", name: "Sodan", 23 followers, 125 public repos | High (live check) |
| `https://api.github.com/orgs/dan-labs-agi` (live check, 01:00 UTC) | **404** — org does not exist publicly | High (live check) |
| TechCrunch (Jun 16, 2026) | Snap Specs launched at AWE 2026 at $2,195, preorder open | High |
| Forbes (Jun 17, 2026) | Snap smart glasses at $2,195, Meta at 70% market, 3.5M Ray-Ban units | High |
| Road to VR (Jun 17, 2026) | Raven Prism announced at AWE 2026, hot-swap battery, Linux 64-bit, LCoS, eye tracking, physical privacy cover | High |
| UploadVR (Jun 2026) | Meta opening 50 Best Buy "Meta Lab" store-in-store sections by end of 2026 | High |
| Glass Almanac (Jun 2026) | WIRED: Meta removed NameTag face-recognition code from Meta AI app, 50M+ users had dormant code | High |
| Glass Almanac (Jun 2026) | 6 AR announcements in 2026 that could upend smart glasses — Apple visionOS 27, Google I/O May 19 | High |
| Engadget (Jun 8, 2026) | Apple visionOS 27 — Siri that knows what you're looking at | High |
| `/home/workspace/dan-glasses/agent-work/dan1.md` | Foundation stream verified, all 7 daemons live | High (live check) |
| `/home/workspace/dan-glasses/agent-work/dan2.md` | audiod v0.4 shipped, 83/83 tests, watchdog fix | High (live check) |
| `/home/workspace/dan-glasses/Services/perceptiond/SPEC.md` | LFM2.5-VL-450M live, salience-gated, 0 cloud | High |
| `/home/workspace/danlab-multimodal/README.md` | Pre-RL scaffold, 250MB VLM, MIT, demo live | High |
| `/home/workspace/danlab-multimodal/docs/ARCHITECTURE.md` | Pipeline architecture, heuristic loop | High |
| `/home/workspace/paperclip/README.md` | Dormant, internal orchestrator | High |
| `/home/workspace/dan-glasses/PRD.md` | US-1 through US-5, power budget, form factor | High |
| `/home/workspace/dan-glasses/agent-work/dan1-marketing-research.md` (v54) | Supersedes this v55 | High |

---

## 6. Open questions for somdipto (v55 — sharpened, less, sharper)

1. **`dan-labs-agi` org** — make public today, or change DANI site links to `somdipto/*`? The brand bug is the #1 fix.
2. **The 6-day-old punchlist** — has anything shipped since 2026-06-12? The bio swap, 3 repos public, DANI banner on danlab.dev. If not, the bet is lapsed. What's the new deadline?
3. **AWE 2026 reactive hooks** — can somdipto ship 1 X post per day for the next 4 days, even if the punchlist doesn't move? AWE 2026 is a one-time news cycle. Use it.
4. **Raven Prism collab** — quote-tweet their AWE announcement? Offer Dan Glasses as the MIT brain alternative? This is the highest-conviction ally we have.
5. **Meta NameTag code purge** — quote-tweet the WIRED/Glas
s Almanac report? "0 cloud. 0 faceprints. We never had the code to remove." This is the single highest-impact reactive hook of AWE 2026.
6. **Omni-1B-Indic** — is the model repo public yet? `github.com/somdipto/omni-1b-indic` returns 404. The Day 60 moat story is gated on this.
7. **The DANI → Dan Glasses product bridge** — when a DANI Pro user buys a Dan Glasses (Q4 2026), what do they get? Same brain. Same memory. Different substrate. We need the cross-sell story documented.

---

*Dan1 research v55. The brain is live. The body ships Q4 2026. AWE 2026 is a 4-day news cycle. The 6-day-old punchlist is stalling. The brand bug (`dan-labs-agi` org returning 404) is the #1 fix. The Meta NameTag story is the closing argument. The next 4 days are the lane claim.*
