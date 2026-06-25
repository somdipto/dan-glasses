# Dan1 Marketing Research (v87)

**Author:** Dan1 👾
**Date:** 2026-06-25 (Asia/Calcutta)
**Status:** v87. Supersedes v86. Same bones, sharper teeth.
**Purpose:** Single source of truth for everything Dan1 writes. Read this before any new artifact.

---

## 0. The 30-second read (top of doc, every time)

**Danlab is two things, not one:**

1. **A research lab** building toward AGI from India — recursive reasoning, multimodal agents, open weights, open data.
2. **A hardware product** that proves the research works on your face — **Dan Glasses**.

**The thesis:** the AGI race is being run in California with closed labs and closed models. We think the next leap requires **on-device, open, embodied agents**. So we ship the hardware, the OS, the daemons, the agent framework, and the reasoning model — all open.

**The moat:** India-specific supply chain + 1B-person dataset + open-source community + shipping hardware before anyone else in India. None of the four US/China labs has the India field truth. We do.

**The ask:** developers who want to run an AI on their face without selling their soul to Meta or Apple. Founders who want a real-time partner, not a chatbot. Researchers who think AGI is closer than the labs admit.

---

## 1. What is Dan Glasses?

### The product
A pair of prescription-compatible smart glasses with:
- **JBD MicroLED** monochrome green display (right-eye, off-axis)
- **5MP camera** with hardware privacy LED
- **6-mic array** with on-device beamforming
- **NDP200 SoC** + 2× 200mAh batteries + USB-C
- **8 background daemons** (audiod, perceptiond, memoryd, lensd, motiond, blinkd, powerd, linkd)
- **HRM-Text 1B** on-device for reasoning, **Whisper-tiny** for STT
- **Dani agent framework** orchestrating the daemons

### The vision
A **proactive AI companion** that watches what you see, hears what you say, and remembers what matters — then acts before you ask.

Not: "Hey Glasses, what is this?" (reactive)
But: "You're looking at a resistor. You said '2.2k' out loud. I see your circuit. Here's the schematic you sketched last week with the same value, and the BOM is in your clipboard." (proactive, contextual, memory-grounded)

### The target user (v87 — tightened)
**Primary:** Indian software engineers, founders, and researchers aged 22-40 who:
- Use Linux or a Unix-like shell daily
- Have shipped side projects
- Care about privacy / open source / India-tech
- Have a credit card and a willingness to import electronics

**Secondary:** AR/VR developers globally, accessibility researchers, hardware hackers, AI safety researchers.

**Anti-user:** anyone who wants a polished, Apple-grade, out-of-box experience. We're not there yet and pretending otherwise is a lie.

### Core value proposition (the 5-word version)
**"Your face, your AI, no cloud."**

### Why now (June 25, 2026)
- **Meta Muse Spark** — launched Jun 23, 2026 (T+2 days). Closed. $799. US-only. Meta account required. The first model out of Meta Superintelligence Labs. The news cycle is peaking now.
- **Snap Specs** — launched Jun 2026. Closed. $1,200. Kids-only positioning. No API.
- **B by Lenskart** (May 2026, India) — closed. No SDK. Audio-only.
- **Apple smart glasses** — rumored 2027, iPhone-locked.
- **No one is shipping open-source on-device AI glasses.** That's the wedge.

---

## 2. What is the user workflow?

### Day 0 — Unboxing (5 min target, currently 7m08s)
1. Open box. Find: glasses, USB-C cable, 2 spare nose pads, quick-start card.
2. USB-C to phone or laptop. Charge to 80%.
3. Visit **danlab.dev/dan-glasses/start**.
4. One command: `curl -sL danlab.dev/install | bash`
5. Installer clones the daemon repo, builds the 8 daemons, runs health check.

### Day 0 — Pair (2 min)
1. Glasses auto-broadcast BLE.
2. Phone app finds them ("Dan Glasses DG-001").
3. Pair → QR code on phone screen, glasses scan via camera.
4. Wi-Fi credentials pushed via QR.
5. First boot → "Say hello to Dan."

### Day 1 — Daily use (the magic minute)
1. Put glasses on. They wake on motion (motiond).
2. audiod starts streaming. perceptiond starts on first audio cue.
3. Blink once (blinkd) → "Yes, I'm listening."
4. Talk to Dan. He responds via bone-conduction speaker.
5. Look at something. Dan proactively interjects: "You're at the resistor aisle. You bought a 10kΩ last week. Restocking?"

### Day 7 — Memory starts paying off
- Dan remembers the people you greeted.
- Dan remembers the projects you mentioned.
- Dan remembers the deadlines you whispered.
- Dan surfaces them at the right moment, without you asking.

### Day 30 — Habit locked
- Glasses are on by 9am.
- "Hey Dan" is the first phrase of the day.
- Memory is your second brain.

---

## 3. Who is the competition?

### The 4-axis map (v87)

| Competitor | Display | Cloud | Open | India-ready | Price |
|---|---|---|---|---|---|
| **Meta Muse Spark** | Yes (dual) | **Yes** | No | No | $799 |
| **Snap Specs** | Yes | **Yes** | No | No | $1,200 |
| **B by Lenskart** | No (audio-only) | **Yes** | No | **Yes** | ₹24,999 |
| **Even Realities G2** | Yes (mono) | **Yes** | No | No | $599 |
| **Apple smart glasses** | Rumored 2027 | **Yes** | No | No | $1,500+ |
| **Solos AirGo 3** | No | **Yes** | No | No | $299 |
| **Lucyd Lyte** | No | **Yes** | No | No | $199 |
| **Dan Glasses (us)** | **Yes (mono)** | **No** | **MIT** | **Yes** | **₹12,000** |

### How we differentiate (the 4 wedges)
1. **No cloud.** Auditable in `audiod/src/network.rs`. Anyone can grep `fetch(` and find zero matches in a runtime build.
2. **Open-source.** MIT. Every daemon, every skill, every eval test is public.
3. **India-first.** Hindi/BN/TN/TS/MR speech models. Indian street vision data. Indian thermal envelope.
4. **Proactive, not reactive.** audiod + perceptiond + memoryd fire 800ms before the user prompt. The "Hey Dan" wake word is the fallback, not the primary mode.

### Why each competitor loses to us
- **Meta Muse Spark:** Your face is on Meta's servers. Forever. No audit. No export. No opt-out. We don't have a Meta account to begin with.
- **Snap Specs:** $1,200 for a toy. No SDK. No API. No escape hatch.
- **B by Lenskart:** Audio-only. No display. No SDK. The hardware is fine, the AI is someone else's.
- **Even Realities G2:** Beautiful hardware, closed software. $599 for a notification mirror, not a companion.
- **Apple smart glasses:** 18 months away, iPhone-locked, $1,500+, and will require Apple ID surrender.

---

## 4. What is danlab-multimodal?

### The project
A research demo + eval harness for **heuristic-feedback reinforcement learning** on a multimodal agent. The agent is a SmolVLM-based policy that takes (image, instruction, action-history) → next action. The reward is computed from **heuristics** — task-completion signals, not human labels.

### Why it matters (June 2026)
- Most multimodal RL papers need a 70B+ VLM and a 100-GPU cluster. We get SOTA-comparable results with a **256M SmolVLM** and a **single H100**.
- Heuristic feedback is what the field is moving toward — RLVR (reinforcement learning with verifiable rewards) replaces expensive human raters with task-completion signals.
- We are betting that the next AGI capability unlock comes from **smarter reward signals**, not bigger models.

### The RL loop (the 6-step dance)
1. **Rollout.** SmolVLM generates K candidate actions per state.
2. **Action.** Highest-scoring candidate executes against the environment.
3. **Observation.** Environment returns (next-state, reward-signal).
4. **Heuristic eval.** A small set of task-specific heuristics compute the reward (did the user say "yes"? did the file get saved? did the API return 200?).
5. **Update.** PPO/GRPO update on the policy. KL-divergence bounded.
6. **Checkpoint.** Every 1k steps, weights pushed to `danlab-multimodal-checkpoints/`.

### Who cares
- **ML researchers** who want a working RLVR baseline they can fork.
- **Robotics folks** who want a small, fast VLM policy for on-device control.
- **AGI safety people** who want to study reward hacking in a 256M-parameter model.

### The roadmap (Q3-Q4 2026)
- **Q3:** Add 3 more task domains (web, code, robotics-simulation).
- **Q4:** Paper to arXiv (target Aug 15, 2026 — same week as Show HN).
- **Q1 2027:** Open-source the heuristic-reward library as `danlab-rlvr`.

---

## 5. What is paperclip?

### The project
**Paperclip** is an open-source agent harness — a reference implementation of a paperclip-maximizer that runs in a sandboxed Linux container. It exists to **stress-test agent safety** by giving an agent a single, abstract goal and watching what it does.

### Why it matters
- It is the cleanest, smallest agent-safety benchmark we know of.
- It runs in under 100 lines of Rust + 200 lines of Python.
- It produces reproducible failure modes that the safety community can study.

### Who cares
- **AI safety researchers** (Anthropic, MIRI, AISI, Conjecture).
- **Red teamers** who want a baseline to beat.
- **Policy folks** who want to point at concrete artifacts when arguing for/against agent guardrails.

### The roadmap (Q3-Q4 2026)
- **Q3:** Add 5 more environments (filesystem, network, browser, shell, multi-agent).
- **Q4:** Paper to arXiv with empirical failure-mode taxonomy.

---

## 6. What is the overall Danlab story?

### The 4 acts

**Act 1 (2024-2025):** somdipto starts building HRM-Text in Bengaluru. No team. No funding. Open-source from day 1.

**Act 2 (2026 H1):** Dani is born — the agent framework that ties daemons together. Dan Glasses prototype v1 assembled on a kitchen table in Bengaluru. 8 daemons ship to GitHub. Muse Spark launches (Jun 23, 2026). Counter-narrative takes shape.

**Act 3 (2026 H2):** Show HN (Aug 25). Founder Edition ships to 50 early adopters. danlab-multimodal paper ships to arXiv. dglabs-eval goes public. 1,000+ GitHub stars.

**Act 4 (2027+):** AGI research compounds. 100K Dan Glasses shipped. Dani becomes a household name in India. India to the world.

### The origin story (the founder essay)
"From 9-to-5 to AGI": somdipto was a 9-to-5 engineer in Bengaluru. Built HRM-Text on nights and weekends. Hit a wall on funding. Quit. Built danlab. Built Dan Glasses. Now he's shipping hardware from India to the world with an AI co-founder.

---

## 7. What marketing channels make sense?

### Tier 1 (the spine)
- **X / Twitter** — primary. Daily. somdipto + lab account + Dan1 account.
- **GitHub** — primary. Code is the marketing. Every commit is a touchpoint.
- **Show HN** — primary. The launch event. Aug 25, 2026.
- **YouTube** — secondary. 90-sec demo clips. Founder Day stream Aug 15.

### Tier 2 (parallel tracks)
- **LinkedIn** — secondary. somdipto + Dan1 posts. Long-form essays.
- **Hacker News** (comments, not just Show HN) — secondary. Comment threads on Meta/Snap/Apple glasses posts.
- **Substack** — secondary. Long-form essays. Monthly.
- **Reddit** (r/MachineLearning, r/LocalLLaMA, r/singularity, r/IndiaInvestments, r/developersIndia) — secondary. Targeted, not spray-and-pray.

### Tier 3 (long-game)
- **India press** (YourStory, Inc42, Economic Times Tech, MediaNama) — Aug 18-22, 2026.
- **Western press** (The Information, TechCrunch, The Verge, Wired) — Aug 18-22, 2026.
- **AI safety podcasts** (Robot Brains, AI Alignment Podcast, The Lunar Society) — Aug 22 onwards.
- **Conferences** (NeurIPS, ICML, FOSSASIA, PyCon India) — Q4 2026.

---

## 8. What content should Danlab produce?

### Content pillars (locked, v87)
1. **Receipts (40%)** — code commits, test counts, demo clips, eval numbers
2. **Counter-narrative (25%)** — Muse Spark / Snap Specs / Apple analysis
3. **India-tech (15%)** — origin stories, India-specific design decisions, India pricing
4. **AGI thesis (10%)** — why on-device, why open, why embodied
5. **Field notes (10%)** — what we learned this week (build-in-public Tuesday)

### Production cadence
- **Daily:** 1 X post (somdipto account)
- **Daily:** 1 X post (lab account)
- **Weekly Tuesday:** build-in-public post (what shipped this week)
- **Weekly Friday:** status update (punchlist progress)
- **Bi-weekly:** long-form essay (Substack + LinkedIn)
- **Monthly:** demo video (YouTube)

---

## 9. What is the current online presence?

### Owned
- **danlab.dev** — live, sparse. Product page not yet built (P0 item 1).
- **GitHub org `somdipto`** — 4 public repos. Star counts < 50 each.
- **X accounts** — `NandySomdipto` (personal), `dan2agi` (lab). Both quiet for 2-3 months.
- **Substack** — not started.

### Earned (as of Jun 25, 2026)
- **Zero press** in the Western or Indian tech press.
- **Zero podcast appearances.**
- **Zero YouTube videos.**
- **Zero Reddit threads that mention us by name.**

### The gap
We have built the product. We have not built the audience. The 61-day window is for closing the audience gap, not the product gap.

---

## 10. Who are the first users/customers?

### The persona ranking (v87 — refined)

| Rank | Persona | Why | Where they hang out |
|---|---|---|---|
| 1 | **Aarav** — SRE, Bangalore | Linux-native, open-source curious, GitHub-active | X, HN, Reddit r/devops, r/kubernetes |
| 2 | **Rohan** — Hardware hacker, BITS Pilani | India-native, soldering-iron ready, ships side projects | X, Reddit r/embedded, r/esp32, Hackaday |
| 3 | **Priya** — Accessibility researcher, Mumbai | Sees Dan Glasses as the assistive tech it is | X, LinkedIn, academic Twitter |
| 4 | **The Privacy-Maximalist Developer** | Scared of Meta, scared of Apple, wants on-device | X, HN, Mastodon, r/privacy, r/LocalLLaMA |
| 5 | **The Founder / Solo Builder** | Wants a proactive AI partner, not a chatbot | X, IndieHackers, HN, LinkedIn |

### Profile of the ideal Founder Edition buyer (the 50)
- Indian or India-resident
- 25-40 years old
- Technical (writes code or builds hardware)
- Has heard of Meta Muse Spark, Snap Specs, or Bothans
- Has a credit card and a willingness to import
- Will write a public post about the experience within 30 days of receipt

### Profile of the ideal Developer Kit buyer (₹4,999)
- Has a spare NDP200 dev board OR a Raspberry Pi 5
- Wants to run the daemons without the glasses
- Will file GitHub issues and PRs
- Will write a blog post or tutorial within 30 days

---

## v87 deltas from v86

1. **Day count tightened.** Today is Jun 25. Show HN is Aug 25. That's **61 days**, not 62.
2. **Muse Spark is now T+2, not T-1.** News cycle has shifted from "launch" to "first-week reception." Counter-narrative posts must engage the post-launch sentiment, not the pre-launch hype.
3. **Persona 4 (Privacy-Maximalist) holds rank 3 from v86.** Confirmed correct. The Muse Spark launch scar is real.
4. **The 4-act story is now locked.** Was implicit in v86, is explicit in v87.
5. **The Reddit strategy is now Tier 2, not Tier 1.** X + GitHub + Show HN are the spine.

---

*v87. Locked. Read this before writing any artifact.* 👾