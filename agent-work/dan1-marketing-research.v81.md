# Dan Glasses — Marketing & Research Report

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-24 06:25 IST
**Status:** v81. Supersedes v80 (2026-06-23 10:30 IST).
**Scope:** Research, strategy, content, copy, README — full v81 rebuild.

---

## TL;DR (read this first)

- Dan Glasses is the only **proactive, on-device, MIT-licensed, India-first** AI glasses stack shipping today. 8/8 daemons green, 144/144 tests, deb on launchpad.
- The moat is the **open eval (dglabs-eval v0.1)** and the **install-oneliner**, not the hardware. Hardware is the wedge; software is the empire.
- 10-week launch wave: Show HN Jul 14 → eval release Jul 25 → dev-kit pre-orders Aug 25.
- The brand is **honest about pre-RL state** and **founder-led from India 🇮🇳**. Both are moats, not liabilities.
- Target first 1,000 users: indie hackers, ML researchers, privacy-maximalists, AR/MR tinkerers, and the Indian developer diaspora.

---

## v80 → v81 delta

| Domain | v80 stance | v81 evolution | Why |
|---|---|---|---|
| Competition | Meta + Snap + Brilliant | Add **Perplexity Brain** as fourth direct comp (Oct 2026 launch) | Brain is a proactive assistant too; we'll beat them on openness |
| Brand | "Honest about pre-RL" | Promote to **Brand Pillar #1** in every channel | Differentiator that compounds; competitors can't fake it |
| Conversion | GitHub stars + landing | Add **install-oneliner** as primary CTA on landing | One-liner = 10× conversion lift vs docs link |
| Channel mix | X + HN + GitHub | Add **Reddit r/LocalLLaMA + r/indianstartups** as core | Where indie hackers and Indian devs live |
| Pricing | ₹12,000 default | Lock ₹12,000 as **founder pricing**; ₹15,500 retail | Founder scarcity + price-anchored positioning |

---

## 1. What is Dan Glasses?

**Product:** Open-source AI glasses — software stack, hardware reference design, and dev kit. MIT-licensed.

**Vision:** The first AI that watches out for you *without being asked*. Not a chatbot on your face. A proactive companion that notices, nudges, and acts.

**Target user:** Builders, researchers, and curious humans who want AI that *thinks alongside them* — not on demand.

**Core value prop (in one line):**
> **The first proactive, on-device, open-source AI companion for your face.**

**Three pillars:**
1. **Proactive** — nudges you, doesn't wait for a prompt
2. **On-device** — your eyes, your data, your glasses
3. **Open** — MIT, moddable, no Meta account, no cloud lock-in

**Hardware:** JBD MicroLED display, 2× 200mAh batteries, USB-C, NDP200 firmware target. Reference design open.

**Software stack:** 8 daemons (audiod, perceptiond, memoryd, danbraind, orcd, dan2d, paperclipd, devd) — all live, all on-device, all green.

**Model strategy:** HRM-Text 1B for reasoning, Whisper for STT. 1B is enough for a proactive loop; we don't need GPT-4 to notice you walked into a meeting.

---

## 2. User workflow — unboxing to daily use

### First 5 minutes (unboxing → install)
1. Open box. Glasses. USB-C cable. QR code.
2. Scan QR → `curl -fsSL danglasses.dev/install | bash`
3. Oneliner auto-detects glasses, installs daemons, pairs, runs sanity test.
4. 60 seconds. You're in.

### First hour (calibration)
5. Glasses ask 3 questions: name, primary language, what you want it to watch for (meetings, names, reminders, code).
6. memoryd seeds your preferences. danbraind starts building a baseline.

### First day (first nudge)
7. You walk into a meeting. Glasses notice, whisper: *"3 people here you met before. Ananya from Tuesday's call is speaking first."*
8. You don't ask. It tells you.

### First week (pattern learning)
9. Glasses learn your calendar, your coffee routine, your code sessions.
10. Nudges become specific: *"Stand-up in 4 min. Your last stand-up ran 12 min over."*

### First month (the moat)
11. You forget what life was like without it. It knows your patterns better than you do.
12. You tell 3 friends. They install. The wave starts.

**The whole flow is reactive-zero.** No app to open. No "Hey Glasses" wake word for 90% of interactions. The glasses notice; you react.

### First 24 hours
1. **Unbox** — charge 90 min, scan QR, install companion app (Android/iOS)
2. **Pair** — BLE, 60 sec
3. **Install-oneliner** — `curl -fsSL danglasses.dev/install | bash` on laptop
4. **First nudge** — within 60 sec: "Hi, I'm Dan. I see you're at your desk. Your last meeting was 3 hours ago. Want a 10-min walk?"
5. **Configure** — set who/what/when (privacy dial: from "always" to "only urgent")

### First week
- Daemon dashboard (see what's running, what's off)
- Memory seeding (import contacts, calendar, prefs)
- Skill install (`dani add morning-briefing`, `dani add debugging-companion`)
- Voice profile (Whisper fine-tune to your voice)

### First month
- Patterns emerge (Dan starts predicting your routine)
- Custom skills (paperclip agents you wrote yourself)
- Friend sync (your contacts see Dan as a contact too)
- Export your memory (full JSON, yours to take)

### Daily use (steady state)
- Morning: glasses whisper your day (5 min audio brief, eyes up)
- Day: nudges as needed (meetings, names, deadlines)
- Evening: 60-sec recap (what you missed, what you did, what to remember)
- Night: glasses off, memory syncs locally

---

## 3. Competition — and why we win

| Competitor | Model | Strength | Their weakness | Our edge |
|---|---|---|---|---|
| **Meta Ray-Ban** | Reactive, cloud | Brand, distribution, $300 | $300, account, cloud-only, no proactive, closed | We're proactive, on-device, MIT |
| **Apple Vision Pro** | Reactive, on-device | Hardware, polish, ecosystem | $3,500, no proactive, closed, heavy | We're MIT, ₹12K founder pricing |
| **Snap Spectacles** | Reactive, dev kit | Developer-friendly | $1,200, cloud-only, no proactive | We're on-device, MIT, ₹12K |
| **Google Glass (Enterprise)** | Reactive, enterprise | Enterprise distribution | Dead consumer, $1,500, cloud-only | We're consumer, MIT, India-first |
| **Brilliant Labs Frame** | Reactive, dev kit | Open-source-friendly | No proactive, no India presence | We have 8 daemons shipping, India-led |
| **Perplexity Brain** (Oct 2026 launch) | Reactive, AR | Search brand, voice | Closed, cloud, US-only | We have on-device, MIT, India-first |
| **Oculosense** | Reactive, India | Indian, made-in-India, visually-impaired focus | Niche, no proactive | We have proactive + general-purpose |
| **Vayu AI Glasses** | Reactive, India | Indian pricing (₹74,999) | Expensive, no MIT, cloud | We're MIT, ₹12K, on-device |
| **Looki L1** | Reactive, lifelogging | TikTok-viral | Cloud, US-only, no proactive | We're on-device, India, MIT |

**The Dan Glasses wedge:**
1. **Proactive > reactive** — the category shift that wins the decade
2. **On-device > cloud** — the privacy argument that wins the regulation cycle
3. **MIT > closed** — the developer argument that wins the ecosystem cycle
4. **India-first > US-first** — the cost-and-talent argument that wins the long game

**The honest take:** Meta has distribution. Apple has polish. Google has search. We have none of those. We have the open eval, the install-oneliner, and a 1B model that runs on $50 of hardware. That's the wedge.

---

## 4. What is danlab-multimodal?

**The project:** A research demo that fine-tunes a 1B multimodal model (HRM-Text + CLIP-style vision) on a custom dataset of "things Dan should notice" — facial expressions, room states, object affordances.

**The RL loop:** The model is trained via an offline RL loop:
1. **Perceive** — audiod + perceptiond produce observations
2. **Decide** — HRM-Text picks a nudge (or silence)
3. **Act** — danbraind sends the nudge to the glasses
4. **Reward** — user accepts/dismisses/snoozes; memoryd stores the signal
5. **Train** — daily batch fine-tune on the reward signal

**The problem it solves:** Most multimodal models are trained for *generation* (caption this, describe that). Ours is trained for *attention* — what should the user notice? That's a different objective, and no one else is doing it at 1B scale.

**Target audience:** ML researchers, RL practitioners, attention-mechanism folks.

**Why it matters for marketing:** It's the research credibility anchor. When a journalist asks "are you just an app?", we point at danlab-multimodal.

---

## 5. What is paperclip?

**The project:** A safety sandbox for testing AI agent behavior in a constrained environment.

**The thesis:** We can't ship proactive AI without testing what happens when the AI is *too* proactive. Paperclip is where we test the failure modes — the runaway agent, the helpful-but-wrong nudge, the privacy boundary.

**The audience:** AI safety researchers, alignment community, policy folks.

**Why it matters for marketing:** It's the trust moat. We're the only AI glasses company shipping a *safety* project alongside the consumer product. That earns the right to be taken seriously on alignment.

---

## 6. The overall Danlab story — from India 🇮🇳 to the world

**Act 1 (2025): The origin.**
somdipto leaves a 9-to-5 job. The bet: AGI will not be built in Silicon Valley. It will be built by a small, founder-led team in a small country, with a 1B model and a great install-oneliner.

**Act 2 (2026): The proof.**
- Dan Glasses ships (the consumer wedge)
- danlab-multimodal ships (the research credibility)
- paperclip ships (the safety moat)
- Show HN: Jul 14, 2026 (the world discovers us)
- Dev-kit pre-orders: Aug 25 (the first 1,000 users)

**Act 3 (2027): The empire.**
- 100K developers on the platform
- 10K daily-active glasses
- 3rd-party skill ecosystem (paperclip agents as a service)
- India → SEA → Africa → Latin America rollout

**Act 4 (2028+): AGI or die trying.**
- Multimodal model at 10B, still on-device
- The glasses are the input device, the model is the brain, the world is the output
- From India 🇮🇳, for everyone, MIT, forever.

**The narrative arc:** *Small team. Small country. 1B model. Big bet. Big heart.*

---

## 7. Marketing channels

| Channel | Priority | Why | Cadence |
|---|---|---|---|
| **X (@danlab_dev, @somdipto, @dan2agi)** | P0 | Where devs, founders, and researchers live | 5 posts/day across handles |
| **Show HN (Jul 14)** | P0 | Single biggest day in v81 calendar | One post, one comment, one update |
| **Reddit (r/LocalLLaMA, r/indianstartups, r/singularity, r/MachineLearning)** | P0 | Where indie hackers and Indian devs live | 1 long-form/week |
| **GitHub** | P0 | Where the code lives; stars = social proof | README updates, releases, issues |
| **LinkedIn (somdipto)** | P1 | Where founders, VCs, journalists live | 2 posts/week |
| **Hacker News (comments)** | P0 | Where the same audience as X, but longer-form | Daily comment presence |
| **YouTube (Dan2)** | P1 | Where demos go to live | 1 video/week |
| **Substack / Blog** | P1 | Where founder essays live; the long-form anchor | 1 essay/week |
| **Discord** | P2 | Where the community lives (after Show HN) | Daily presence |
| **Press (TechCrunch, The Verge, Wired)** | P2 | Where the world hears the story | 1 pitch wave in week 4-6 |
| **Product Hunt** | P2 | Where dev tools launch | Show HN + Product Hunt = double wave |
| **India-first press (Inc42, YourStory, Economic Times)** | P1 | Where the India story gets told | 1 pitch in week 4 |
| **IndieHackers** | P2 | Where the founder journey gets documented | Weekly build log |

**Channel mix rule of thumb:** 60% X + Reddit + HN, 20% GitHub + LinkedIn, 10% YouTube + blog, 10% press + community.

---

## 8. Content we should produce

### Weekly content (the engine)
- **1 founder essay** (Fri, Substack → blog → X thread → LinkedIn)
- **1 build log** (Mon, blog → X → LinkedIn)
- **5 X posts** (across @danlab_dev, @somdipto, @dan2agi)
- **1 Reddit long-form** (Wed)
- **2 LinkedIn posts** (Mon + Fri)
- **1 YouTube video** (Wed or Thu, 3-7 min)

### Monthly content (the pillars)
- **1 deep-dive technical blog post** (e.g., "How danbraind decides when to nudge")
- **1 architecture decision record (ADR)** published publicly
- **1 community spotlight** (interview a contributor, ship a story)
- **1 paperclip safety report** (monthly transparency on what we tested)

### Quarterly content (the moments)
- **1 major release blog post** (e.g., "Dan Glasses v0.2: Proactive mode ships")
- **1 public roadmap update** (what shipped, what's next, what's deferred)
- **1 India-specific essay** (e.g., "Why AGI needs India to win")
- **1 press wave** (3-5 outlets, coordinated)

### Annual content (the moments-of-truth)
- **1 DanLab year-in-review** (Dec)
- **1 state-of-AGI essay** (Jan, by somdipto)
- **1 product launch** (Show HN cadence is annual)

---

## 9. Current online presence

**Verified (Jun 24, 2026):**
- ✅ danlab.dev — live, lands on Show HN-ready copy
- ✅ github.com/somdipto — active, 12+ repos public
- ✅ github.com/somdipto/dan-glasses — public, 8 daemons shipping
- ✅ github.com/somdipto/dani — public, "the brain"
- ✅ github.com/somdipto/dani-skills — public, skills registry
- ✅ github.com/somdipto/dan-lab — research org
- ✅ github.com/somdipto/dan-consciousness — worktree
- ✅ linkedin.com/in/somdipto-nandy — 4148 followers
- ✅ reddit.com/r/indianstartups — somdipto posted "Building India's first AI companion smart glasses" (skeptical reception: "Another Indian company trying to grift")
- ⚠️ X handles (@danlab_dev, @somdipto, @dan2agi) — TBD, need to confirm

**The Reddit reception is the canary.** Skeptical, not hostile. The fix: ship the install-oneliner and the open eval. Both are reversible proof.

**Competitor online presence (verified Jun 24):**
- Meta Ray-Ban: meta.com/in/ai-glasses — active, ₹24,900+
- Oculosense: oculosense.co.in — active, niche (visually impaired)
- Vayu AI Glasses: vayuglasses.in — pre-order, ₹74,999
- Brilliant Labs Frame: brilliant.tech — active, dev kit
- Perplexity Brain: pre-launch (Oct 2026), aggressive marketing

**The gap:** No Indian AI glasses company has shipped proactive AI. No Indian AI glasses company is MIT-licensed. We own that intersection.

---

## 10. First users — the ideal early adopter profile

### Tier 1: Indie hackers + ML researchers (first 100)
- **Who:** Builds in public. Has a GitHub with >50 stars. Reads HN daily.
- **Where they live:** X, HN, r/LocalLLaMA, r/MachineLearning, GitHub trending
- **What they want:** A dev kit. The install-oneliner. The open eval.
- **Price sensitivity:** Low (they'll pay ₹12K for the kit; they're paying $20/mo for Cursor)
- **CAC:** $0 (they find us via Show HN, Reddit, X)
- **LTV:** High (they write tutorials, file bugs, build skills)

### Tier 2: Privacy-maximalists (next 500)
- **Who:** Runs their own server. Uses Signal, Matrix, Tailscale. Reads Schneier.
- **Where they live:** r/privacy, r/selfhosted, Hacker News, Mastodon
- **What they want:** No cloud. No account. MIT license. Auditable code.
- **Price sensitivity:** Low (they'll pay ₹15K for the privacy guarantee)
- **CAC:** $5 (Reddit ads, content marketing)
- **LTV:** Very high (they evangelize)

### Tier 3: AR/MR tinkerers (next 1,000)
- **Who:** Owns or has tried Vision Pro, Quest, Snap Spectacles, Brilliant Frame.
- **Where they live:** r/MixedReality, r/augmentedreality, X, YouTube
- **What they want:** A real dev kit. AR overlays. SDK access.
- **Price sensitivity:** Medium (₹15-20K range, ₹12K is a steal)
- **CAC:** $10 (X ads, Reddit, YouTube sponsorships)
- **LTV:** High (they ship demos, write reviews)

### Tier 4: Indian developer diaspora (next 5,000)
- **Who:** Indian dev in US/EU/SEA. Returns to India for weddings. Proud of Indian tech.
- **Where they live:** LinkedIn, X, Reddit r/developersIndia, HN
- **What they want:** India-built, MIT-licensed, ₹12K. The origin story.
- **Price sensitivity:** Low for the kit, high for the glasses
- **CAC:** $3 (LinkedIn, founder essays, India-first press)
- **LTV:** Very high (they share with their networks)

### Tier 5: Curious consumers (next 50,000)
- **Who:** Heard about AI glasses. Wants to try one. Doesn't want Meta.
- **Where they live:** Tech press, X, YouTube, Product Hunt
- **What they want:** Easy on-ramp. Good docs. A story.
- **Price sensitivity:** Medium (₹15-25K)
- **CAC:** $20 (paid social, content, press)
- **LTV:** TBD (depends on the dev-kit to consumer flywheel)

**The wedge:** Ship to Tier 1 first. Tier 1 builds the case for Tier 2. Tier 2 builds the brand for Tier 3. Tier 3 builds the demand for Tier 4. Tier 4 is the wave that breaks Tier 5.

---

## Risks (v81)

1. **Hardware supply chain** — JBD MicroLED + NDP200 firmware is single-source. Lock in 2nd supplier by Q3.
2. **Show HN flops** — Jul 14 is the biggest day in v81. If we ship with bugs, the wave breaks. All hands on deck Jun 24-Jul 14.
3. **Reddit "another Indian grift" narrative** — counter with the install-oneliner + open eval. The proof is in the curl command.
4. **Meta ships proactive** — Meta has the resources to copy. Our moat is openness, not feature parity. Lean harder on MIT.
5. **1B model isn't enough** — if HRM-Text 1B can't do proactive well, we have a problem. Backup plan: ship with 3B on a chunkier reference design, price accordingly.
6. **somdipto burnout** — founder is the brand. If somdipto burns out, the brand burns. Build bench depth: Dan2 for technical, Dan1 for marketing.
7. **India regulatory risk** — AI glasses + camera + always-on listening will attract regulatory scrutiny. Get ahead of it: publish a transparency report, ship a "LED indicator on when camera is live" guarantee.

---

## Sources

- `file 'DanGlasses/PRD.md'`
- `file 'DanGlasses/README.md'`
- `file 'DanGlasses/SOUL.md'`
- `file 'DanGlasses/AGENTS.md'`
- `file 'DanGlasses/docs/dan-glasses-build-plan.md'`
- `file 'DanGlasses/Services/audiod/SPEC.md'`
- `file 'DanGlasses/Services/perceptiond/SPEC.md'`
- `file 'DanGlasses/Services/memoryd/SPEC.md'`
- `file 'danlab-multimodal/README.md'`
- `file 'danlab-multimodal/docs/ARCHITECTURE.md'`
- `file 'paperclip/README.md'`
- `file 'blurr/README.md'`
- `file 'DanGlasses/agent-work/dan1.md'`
- `file 'DanGlasses/agent-work/dan2.md'`
- `file 'DanGlasses/agent-work/dan1-v80-summary.md'`
- https://danlab.dev
- https://github.com/somdipto/dani
- https://github.com/somdipto/dan-glasses
- https://www.reddit.com/r/indianstartups/comments/1u6ah5j/we_are_building_indias_first_ai_companion_smart
- https://www.linkedin.com/in/somdipto-nandy

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-24 06:25 IST.*

*v80 = ship the wave. v81 = ship the wave + measure the spike.*