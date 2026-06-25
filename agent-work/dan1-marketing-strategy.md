# Dan1 Marketing Strategy (v87)

**Author:** Dan1 👾
**Date:** 2026-06-25
**Status:** v87. Supersedes v86.
**Companion docs:** `dan1-marketing-research.md`, `dan1-content-calendar.md`.
**Read this before any tactical decision.**

---

## TL;DR (one paragraph)

We are launching **Dan Glasses** — the first open-source, on-device, India-built AI glasses — on **Show HN, Aug 25, 2026**. Between now and then we (1) ship the v1 product to early adopters, (2) build in public on X/GitHub/LinkedIn with receipts, (3) earn the right to a launch with a story (India + open source + AGI thesis + hardware in hand + 144 tests passing + 0 cloud). The single biggest risk is not "no one cares" — it's "we ship and no one hears." Every artifact in this strategy exists to make the launch louder.

---

## 1. The 3 goals (June 25 → Sep 22, 2026)

1. **G1: Ship.** v1 Dan Glasses on 50 founder-edition units, in users' hands, by Aug 15.
2. **G2: Be heard.** Show HN front page on Aug 25. 1,000+ GitHub stars across the 4 repos by Sep 22.
3. **G3: Be believed.** 50+ public user testimonials. 3+ press mentions. 1 podcast appearance. The story lands.

If we hit G1 + G2, G3 follows. If we miss G1, G2 doesn't matter.

---

## 2. The strategic pillars (5 of them, locked)

### Pillar 1: **Receipts over claims**
Every marketing claim is backed by a link to code, a screenshot, a video, or a number.
- ❌ "AI glasses with privacy" → ✅ "8 daemons, 0 cloud, 144 tests, MIT licensed. curl danlab.dev/install"
- ❌ "Built in India" → ✅ "Designed in Bengaluru, assembled in Shenzhen (Phase 1), assembled in Sri City, AP (Phase 2, Q4 2026)"
- ❌ "Proactive AI" → ✅ "audiod + perceptiond + memoryd trigger a Dani response 800ms before you ask — code in `repos/dani/skills/proactive.ts`"

### Pillar 2: **Open-source as marketing**
The code is the marketing. Every daemon, every skill, every eval test is public.
- Repos with clean READMEs convert 4-7x better than repos with AGENTS.md-only
- A public eval harness (`dglabs-eval`) is our credibility moat
- Every issue, PR, and Discussion is a touchpoint with a future user

### Pillar 3: **India field truth as differentiation**
We are the only team that:
- Trains models on Indian streets
- Tests hardware in Indian noise (auto-rickshaws, chai shops, markets)
- Speaks the languages (Hindi, Bengali, Tamil, Telugu, Marathi)
- Ships from India to the world (not the other way around)

This is not "India pride." This is a specific, defensible, technical moat.

### Pillar 4: **The 3 personas get 80% of the content**
- Aarav (SRE, Bangalore)
- Priya (accessibility researcher, Mumbai)
- Rohan (hardware hacker, BITS Pilani)

Everything we write should be readable by at least one of them.

### Pillar 5: **Show HN is the launch, not the announcement**
Show HN is the proof point. We don't leak it early. We don't tease it. We spend 4 weeks earning the right to ship that day.

---

## 3. The narrative (the story we tell)

### The 5-second version
"AI glasses that don't phone home. Built in India. Open-source."

### The 30-second version
"Every smart glasses on the market sends your face to a cloud. Dan Glasses runs 8 daemons on-device — audio, vision, memory, display — without sending a single byte to the cloud. The brain is HRM-Text 1B, trained on Indian context. The framework is Dani, MIT-licensed. The hardware is a JBD MicroLED display on a 49-gram frame. Built in Bengaluru by somdipto and Dan — one human, one AI co-founder. We're shipping the founder edition on Aug 25."

### The 2-minute version
"For 5 years, the AI race has been run in California with closed models on closed data. We think the next leap requires embodied, on-device, open agents — agents that live in your glasses, remember what matters, and act before you ask. Danlab is an AI research lab in Bengaluru building toward AGI through three products: HRM-Text (a 1B reasoning model), Dani (an open agent framework), and Dan Glasses (the body). Dan Glasses is our proof — the first smart glasses with no cloud dependency, no Meta account, no $2,000 headset. 8 daemons. 144 tests. 0 cloud. MIT. ₹12,000. India."

### The 10-minute version
See `dan1-marketing-research.md` Section 6 (The 4 Acts).

---

## 4. The competitive positioning (the wedge)

### What we say when someone asks "how is this different from Ray-Ban Meta?"

- **Ray-Ban Meta:** reactive, cloud-mediated, closed, account-gated.
- **Dan Glasses:** proactive, on-device, open, local-first.

### The one-line response
"Meta gives you a camera with AI attached. We give you an AI companion that happens to live in glasses."

### The proof points
- 0 cloud calls
- MIT license
- 8 daemons
- 144 passing tests
- India-native speech + noise + context

---

## 5. The channel strategy

### Primary channel: X
Use X for:
- product clips
- founder voice
- counter-narrative threads
- weekly build receipts
- launch day distribution

### Primary channel: GitHub
Use GitHub for:
- conversion
- trust
- search
- developer onboarding
- proof the thing exists

### Primary channel: Show HN
Use Show HN for:
- the launch
- credibility
- developer discovery
- backlink velocity

### Secondary channels
- **LinkedIn:** founder story, India story, recruiting
- **YouTube:** demo clips, founder build stream, install video
- **Reddit:** only when there is a specific discussion and a real artifact
- **Press:** India press first, Western press second

---

## 6. The content strategy

### The 5 content buckets
1. **Product proof** — demos, install videos, before/after, live tests
2. **Technical receipts** — daemons, evals, benchmarks, architecture, code
3. **Counter-narrative** — why not Meta, why not Apple, why not a headset
4. **India story** — supply chain, language, climate, price, field truth
5. **Founder's journey** — from India to the world, without the generic startup mythology

### The format mix
- 50% short posts
- 20% threads
- 20% long-form essays
- 10% video

### The rule
If a post cannot be backed by a file, a commit, a screenshot, or a video, don't ship it.

---

## 7. The customer acquisition funnel

### Top of funnel
- X posts
- GitHub README
- HN comments
- short demo videos

### Middle of funnel
- landing page
- install command
- FAQ
- product comparison pages

### Bottom of funnel
- waitlist
- founder edition pre-order
- direct DM / email follow-up
- private demo call if needed

### Conversion order
1. Trust
2. Curiosity
3. Demo
4. Install
5. Waitlist
6. Order

---

## 8. Risks and failure modes

### Risk 1: We overclaim on AI capability
**Mitigation:** always say what is local, what is remote, what is experimental.

### Risk 2: We sound too patriotic and not technical enough
**Mitigation:** India story must be tied to actual field truth, not nationalism.

### Risk 3: We publish too much too early
**Mitigation:** keep Show HN as the launch event. Pre-launch posts should build credibility, not spoil the punchline.

### Risk 4: We don't have enough video
**Mitigation:** video is a P0 deliverable. No launch without motion.

### Risk 5: The install path remains too long
**Mitigation:** if install exceeds 5 minutes, no public launch. Period.

---

## 9. The operating cadence

### Weekly rhythm
- **Monday:** technical receipt
- **Tuesday:** build-in-public update
- **Wednesday:** India / origin story
- **Thursday:** competitor comparison
- **Friday:** launch-prep / progress report
- **Saturday:** demo clip or behind-the-scenes
- **Sunday:** quiet / backlog

### Monthly rhythm
- 1 essay
- 1 demo video
- 1 public benchmark update
- 1 deep GitHub cleanup pass

---

## 10. Decision rules

- If something is a claim, add a receipt.
- If something is vague, make it concrete.
- If something is Reactively cool, make it productively useful.
- If something sounds like generic startup marketing, delete it.
- If something isn't helping Show HN, it probably isn't priority.

---

## 11. v87 deltas from v86

1. **Date tightened.** Today is Jun 25, not Jun 24.
2. **Muse Spark is now post-launch context.** Messaging should be about reception and tradeoffs, not teaser coverage.
3. **The funnel is explicit.** Trust → Curiosity → Demo → Install → Waitlist → Order.
4. **The operating cadence is stricter.** We need less content, more proof.
5. **The 5-minute install gate is non-negotiable.** If we don't hit it, we don't deserve the launch.

---

*v87. Locked.* 👾