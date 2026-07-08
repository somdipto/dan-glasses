# Dan1 Content Calendar — v86 (Q3 2026)

**Companion to:** `dan1-marketing-research.v86.md`, `dan1-marketing-strategy.v86.md`
**Window:** Jul 1 – Sep 30, 2026
**Cadence target:** 1 shippable piece per week + ongoing X/LinkedIn micro-content

---

## Weekly Template

Every week follows this rhythm:

- **Monday** — Ship the week's flagship content piece (blog, video, or major tweet thread).
- **Tuesday–Wednesday** — Amplify: post the piece to X/LinkedIn/Reddit with platform-native framing.
- **Thursday** — Engage: respond to comments, file follow-ups, post a behind-the-scenes note.
- **Friday** — "What we shipped this week" 5-tweet thread on X.

**Sundays** are no-post days. Founder rest.

---

## July — Foundation Month

### Week 1 (Jul 1–7): Identity

**Flagship:** Brand asset — the 8-daemon mesh diagram
- Format: Single PNG, 1920×1080, dark mode, monospace labels, saffron accent (#FF6B00)
- Content: Shows audiod + perceptiond + memoryd + toold + ttsd + os-toold + openclaw + dan-glasses-app + how they connect
- Channel: First post on `@danlab_dev` X account, also on GitHub README banner
- Owner: Dan1 + somdipto for visual sign-off
- Output: `/home/workspace/Images/dan-glasses-mesh-v1.png`

**Micro-content (X):**
- Tue: "We just published @danlab_dev. Here's what we're building." (link to landing page)
- Wed: Founder quote: "We didn't raise a Series A. We raised a Debian package." (image: terminal output of `dpkg -i`)
- Thu: Behind-the-scenes: 1 photo of the workbench + 1 line of text.
- Fri: "Week 1 of @danlab_dev: shipped 1 mesh diagram. 0 customers. 0 regrets."

**Outcome by end of week:** `@danlab_dev` exists with a banner, follows 10 seed accounts, has 30+ followers.

---

### Week 2 (Jul 8–14): The Debian Package Story

**Flagship:** Blog post #1 — "We shipped a Debian package for AI glasses. Here's the SPEC."
- Format: 2000-word blog post on danlab.dev/blog
- Outline:
  1. The problem: AI glasses require cloud subscriptions.
  2. The bet: a Debian package can ship a daemon mesh.
  3. The reality: 8 systemd units, 144 tests, 28KB .deb.
  4. The SPECs: audiod (5K words), perceptiond (3K words), memoryd (1K words).
  5. The honest limits: aarch64 unmeasured, LFM2.5 is 450M, first install is 10–15 min.
  6. The call to action: `sudo dpkg -i`, file issues, build on top.
- Channel: danlab.dev/blog, X thread, LinkedIn long-form post
- Owner: somdipto (writes) + Dan1 (edits)
- Output: `/home/workspace/danlab-content/blog/001-debian-package.md`

**Micro-content:**
- Mon: Tweet: "We just shipped the world's first Debian package for AI glasses. 28KB. 8 daemons. MIT. 🟧 https://danlab.dev/blog/001-debian-package"
- Wed: Quote-tweet with a SPEC.md screenshot
- Fri: "Week 2: blog post #1 shipped. 400 reads. 12 GitHub stars."

**Outcome:** 400+ blog reads, 12+ GitHub stars, 5+ issues filed.

---

### Week 3 (Jul 15–21): The Show HN

**Flagship:** Show HN submission
- Title: "Show HN: Dan Glasses – Open-source AI glasses daemon mesh (MIT, 8 services, 144 tests)"
- Body: 400 words + 30-second demo gif + SPEC links
- Hook: "We built the local-first alternative to Meta Ray-Ban. It ships as a Debian package."
- Timing: Tuesday 8am PT (HN peak) or Tuesday 6pm IST
- Owner: somdipto
- Output: Drafted in `/home/workspace/danlab-content/show-hn/draft.md`

**Pre-launch prep (Jul 15–17):**
- Confirm .deb installs cleanly on a fresh Ubuntu 24.04 VM.
- Record 30-second demo: terminal → install → first transcript appears.
- Pre-stage answers to the 20 most likely critical questions.
- Verify all GitHub repo links resolve.

**Launch day (Jul 18):**
- Submit at 8am PT / 6pm IST.
- Engage every comment for 48h.
- Repost highlights on X with "Show HN #1" tag.

**Micro-content:**
- Mon: "Show HN tomorrow. A thread 🧵"
- Tue: Post-show summary on X and LinkedIn.
- Fri: "Week 3: Show HN hit #4 on front page. 412 comments. 87 new stars. 23 issues filed."

**Outcome:** Top 10 on HN, 200+ comments, 100+ new stars, 20+ issues filed.

---

### Week 4 (Jul 22–28): Positioning Essay

**Flagship:** Blog post #2 — "Why Dan Glasses is not a Ray-Ban competitor"
- Format: 1800-word essay
- Thesis: We're not in the consumer glasses race. We're building the OS for personal AI.
- Outline:
  1. The smart-glasses market in 2026: Meta, Snap, Even, Brilliant Labs, Acer.
  2. What each of them gets right (with respect).
  3. What they all get wrong: cloud lock-in, no memory graph, no proactive loop.
  4. What we build instead: a stack, not a device.
  5. The founder story: from Bengaluru, for the world.
- Channel: danlab.dev/blog, LinkedIn, X thread
- Owner: somdipto

**Micro-content:**
- Tue: X thread (8 tweets) summarizing the essay.
- Wed: LinkedIn post (different framing — enterprise + India diaspora).
- Fri: "Week 4: positioning essay shipped. 800 reads. 3 enterprise inquiries."

**Outcome:** 800+ reads, 3 enterprise inquiries logged, 1 of them converts to a Q4 pilot conversation.

---

## August — Expansion Month

### Week 5 (Jul 29 – Aug 4): Pre-RL Scaffold Essay

**Flagship:** Blog post #3 — "Pre-RL scaffold: an honest framing of self-improving AI"
- Format: 2200-word essay, technical
- Thesis: Most "self-improving AI" claims in 2026 are ungrounded. Here is what honest scaffolding looks like.
- Hook: Jack Clark's May 2026 warning + the SIA framework + our danlab-multimodal heuristic loop
- Owner: Dan1 + Dan2
- Output: `/home/workspace/danlab-content/blog/003-pre-rl-scaffold.md`

**Micro-content:**
- Mon: Tweet: "We don't claim RL. We claim pre-RL scaffold with a path to real RL via SIA. Here's why that honesty matters. 🧵"
- Wed: Reddit post on r/MachineLearning (cross-post from blog).
- Fri: "Week 5: pre-RL essay shipped. 1500 reads. 2 researchers reached out."

**Outcome:** 1500+ reads, 2 researcher conversations begin.

---

### Week 6 (Aug 5–11): The LFM2.5-VL Benchmark

**Flagship:** Blog post #7 — "LFM2.5-VL on CPU: here's how slow, and what we're doing about it"
- Format: 1500 words + tables
- Content: Real benchmarks on x86_64 (i7-12700), aarch64 (Raspberry Pi 5), M2 Mac. Frames/sec, inference latency, energy estimates.
- Hook: Honesty about the bottleneck.
- Owner: Dan2 (writes) + somdipto (edits)
- Output: `/home/workspace/danlab-content/blog/007-lfm25-benchmark.md`

**Micro-content:**
- Mon: "We benchmarked LFM2.5-VL-450M on a Raspberry Pi 5. Here's how slow. 🧵"
- Wed: Reddit post on r/LocalLLaMA.
- Fri: "Week 6: benchmark blog shipped. Cited by 1 paper preprint (so far)."

**Outcome:** Cited by at least 1 external paper/work.

---

### Week 7 (Aug 12–18): Community Spotlight

**Flagship:** Blog post — "What people are building on Dan Glasses"
- Format: 1500 words + screenshots + repo links
- Content: First 3 community projects (custom daemon, custom UI, custom integration)
- Hook: Show, don't tell — the mesh is generative.
- Owner: Dan1 (curates)
- Output: `/home/workspace/danlab-content/blog/community-spotlight-1.md`

**Micro-content:**
- Mon: "First community spotlight. 3 builders. 3 different directions. 🧵"
- Wed: Each builder gets their own quote-tweet.
- Fri: "Week 7: community spotlight shipped. 3 builders featured. 4 more in queue."

**Outcome:** Pipeline of 4+ future spotlight candidates.

---

### Week 8 (Aug 19–25): The Buyer's Guide

**Flagship:** Blog post #9 — "The personal AI stack in 2026: a buyer's guide"
- Format: Comparison matrix + commentary
- Rows: Meta Ray-Ban, Meta Ray-Ban Display, Even Realities G2, Brilliant Labs Halo, Acer G10, Dan Glasses, DIY llama.cpp + Raspberry Pi
- Columns: Price, AI source, Cloud lock-in, Open SDK, Local processing, Memory graph, Proactive
- Owner: Dan1
- Output: `/home/workspace/danlab-content/blog/009-buyers-guide.md`

**Micro-content:**
- Mon: "A buyer's guide for personal AI in 2026. 7 options compared. No vendor-speak. 🧵"
- Wed: LinkedIn post (executive framing).
- Fri: "Week 8: buyer's guide shipped. Referenced by 3 Substack writers."

**Outcome:** Cited by external press/writers within 30 days.

---

## September — Compounding Month

### Week 9 (Aug 26 – Sep 1): Founder Essay

**Flagship:** Blog post #10 — "Why I'm building AGI from Bengaluru, not Boston"
- Format: 2500-word personal essay
- Thesis: India's 1.4B population is the largest under-served market for personal AI. Building from here is a strategic choice, not a compromise.
- Hook: The origin story + the AGI thesis + the open-source stance.
- Owner: somdipto
- Output: `/home/workspace/danlab-content/blog/010-bengaluru-thesis.md`

**Micro-content:**
- Mon: Tweet thread (10 tweets) excerpting the essay.
- Tue: LinkedIn long-form post (full essay).
- Wed: Reddit post on r/india + r/singularity.
- Fri: "Week 9: founder essay shipped. 3000 reads. 1 podcast interview request."

**Outcome:** 1 podcast or interview opportunity.

---

### Week 10 (Sep 2–8): Code-Switching Technical Deep-Dive

**Flagship:** Blog post #11 — "Code-switching Hindi-English in audiod: how Silero VAD handles it"
- Format: 1800 words + WAV samples + diagrams
- Content: How Silero VAD detects speech boundaries in mixed Hindi-English audio. Whisper.cpp transcription accuracy benchmarks. Failure modes.
- Hook: Multilingual is a wedge no US vendor owns.
- Owner: Dan2
- Output: `/home/workspace/danlab-content/blog/011-code-switching.md`

**Micro-content:**
- Mon: "We benchmarked code-switching Hindi-English in our audiod pipeline. US vendors ignore this. We don't. 🧵"
- Wed: Post on r/LocalLLaMA + r/india.
- Fri: "Week 10: code-switching deep-dive shipped. 1 Indian-language press inquiry."

**Outcome:** 1 Indian-language press inquiry (Hindi tech blog, etc.).

---

### Week 11 (Sep 9–15): Community Spotlight #2 + Awarenessd Preview

**Flagship:** Blog post — "Community spotlight #2 + a peek at awarenessd"
- Format: 1500 words + screenshots
- Content: 3 more community projects + a 1-minute video teaser of the proactive loop (if awarenessd has a usable build)
- Hook: Compounding community + first peek at the hero feature.
- Owner: Dan1 + somdipto
- Output: `/home/workspace/danlab-content/blog/community-spotlight-2.md`

**Micro-content:**
- Mon: "Community spotlight #2. Plus: a 1-min teaser of our proactive loop. (Finally.) 🧵"
- Wed: Behind-the-scenes: terminal session of awarenessd running.
- Fri: "Week 11: spotlight #2 + awarenessd teaser. 12 builders in private beta."

**Outcome:** 12 builders in private awarenessd beta.

---

### Week 12 (Sep 16–22): India Press + Open Source Health

**Flagship:** Two pieces
- Blog post: "Open source health report #1 — what we shipped, what broke, what we learned"
- LinkedIn post: India-focused press push (YourStory, Inc42, AIM, ET Tech) — low-key, no pitches

**Micro-content:**
- Mon: Open source health report shipped.
- Wed: 3 LinkedIn DMs to Indian tech journalists.
- Fri: "Week 12: 2 pieces shipped. 1 journalist replied. 1 enterprise pilot confirmed."

**Outcome:** 1 confirmed enterprise pilot (case study in Q4).

---

### Week 13 (Sep 23–30): Q4 Planning + 90-Day Retrospective

**Internal only:**
- Retrospective on Q3: what hit, what didn't, what surprised us.
- Q4 plan: Show HN #2 timing, awarenessd launch, paperclip public teaser (if applicable).
- Updates to this content calendar for Q4.

**Public micro-content:**
- Mon: "Q3 retrospective thread. 1000 stars. 50 PRs. 1 enterprise pilot. Here's what we learned. 🧵"
- Wed: Brief note on Q4 priorities.
- Fri: Q4 begins. New calendar ships.

---

## Standing Engagements (Weekly, Recurring)

| Day | Item | Owner |
|---|---|---|
| Mon | Flagship content piece ships | Rotating |
| Tue | X thread + LinkedIn post | Dan1 |
| Wed | Reddit + community engagement | Dan1 |
| Thu | GitHub issue triage + external PR reviews | somdipto + Dan2 |
| Fri | "What we shipped this week" X thread | Dan1 |
| Sun | No posts (rest) | — |

---

## Anti-Calendar (What We Will NOT Post)

These are temptations we explicitly avoid:

- ❌ "10 things you didn't know about Dan Glasses" — list-bait.
- ❌ "The future of AI glasses is X" — speculation.
- ❌ Engagement-bait polls ("RT if you think X").
- ❌ Hiring posts (we're not hiring until Q4).
- ❌ Pricing posts (no pricing yet).
- ❌ "Behind the scenes of our office" — there's no office.
- ❌ Generic AI hype threads — the brand is the opposite.

---

## Calendar Maintenance

This calendar is a **living document**. Every Monday, Dan1 reviews the previous week's metrics and adjusts the next 4 weeks. Adjustments are appended here with a dated note.

**First review:** Mon, Jul 7, 2026.

— Dan1 👾