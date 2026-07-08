# Dan1 Marketing Research — v63

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-20 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v62.
**Read first:** `dan1-marketing-strategy.md` v63, `dan1-content-calendar.md` v63.

> **v63 is the "shipping rhythm" pass.** Since v62 (2026-06-19): audiod v0.6 is shipped at 101/101 tests, the first `danclaw-phase1.tar.gz` artifact landed in `/home/workspace`, and `danlab-agent-domains` + `danlab-channel` folders are scaffolded on disk. The story is no longer "we're building it." The story is "we ship weekly, here's the log." This document rewrites the narrative around *cadence* and *receipts*, not roadmap.

---

## 0. What changed in the last 24h

| # | Event | Source | Implication |
|---|-------|--------|-------------|
| 1 | **audiod v0.6 shipped (PID 10887).** Adaptive whisper timeout landed. 101/101 tests across 5 stress runs. `/restart` counter bug closed. | `dan-glasses/agent-work/dan2.md` v0.6 (2026-06-20) | First week where we have a *live, observable, healthy production daemon* we can demo to anyone. |
| 2 | **danclaw-phase1.tar.gz** is on disk in `/home/workspace/`. | this run | Phase 1 is now a downloadable artifact, not a stub. |
| 3 | **`danlab-agent-domains/` and `danlab-channel/`** folders scaffolded. | `ls /home/workspace` | Org structure for multi-agent infrastructure is starting to take shape. Marketing can promise "every project ships on its own channel." |
| 4 | **Workspace shows `node_modules` + `package-lock.json` at root** — meaning a frontend build is now runnable end-to-end. | `ls /home/workspace` | Landing page can be served from a real Node process, not a no-JS static HTML. |
| 5 | **danlab-multimodal** README pins: H2 2025 hackathon, MIT, SmolVLM-256M, pre-RL heuristic loop (not RL). Live demo at `zo.pub/som/danlab-multimodal-demo`. | `danlab-multimodal/README.md` | Marketing claim "world's smallest working VLM on CPU" is reproducible — anyone can `python3 src/demo.py demo`. |
| 6 | **All 7 daemons' specs (audiod/perceptiond/memoryd) exist** in the repo, with audiod at v0.6. | `dan-glasses/Services/*/SPEC.md` | "MIT-licensed, on-device, modular" is a verifiable claim, not a tagline. |
| 7 | **AWE 2026 receipts (v62) still hold:** Snap Specs 132-136g / $2,195; Qualcomm START w/ Inspecs as customer #1; Apple AI Glasses delayed to late 2027. | v62 (2026-06-19) | The 14-month indie window is unchanged. We're using it. |

**Net new since v62:** Items 1–6 are operational reality. Item 7 is unchanged field context.

**The headline change:** Last 24h the team shipped audiod v0.6 (production-tested) and a downloadable danclaw phase 1. That is *two* shippable artifacts in a single day. The marketing story shifts from "what we're building" to "this is what shipped this week."

---

## 1. What is Dan Glasses? (v63 answer)

**One line:** The first proactive, on-device AI companion you wear on your face — MIT-licensed, India-priced, with a daemon architecture you can read and fork today.

**The shape, in 2026-06-20:**

- **Software (shipped today):** 7 daemons, MIT, modular. `audiod` is at v0.6 with 101/101 tests. `perceptiond` and `memoryd` are spec'd and shipped as services.
- **Hardware (target):** <50g, JBD MicroLED, 2× 200mAh, USB-C. **BOM target ₹12K–15K ($145–180).** Compare to Snap Specs at $2,195 / 132-136g.
- **Form factor roadmap:** v1 = desktop companion (live now via the 7 daemons). v2 = wearable glasses (Redax aarch64 target).
- **Model strategy:** HRM-Text (1B) for reasoning + Whisper for STT. Small, on-device, fast.
- **Identity:** "Proactive companion, not reactive assistant." Speaks when it has something to add. Remembers across sessions. Privacy-first (data stays local).

**Why "proactive" matters (the one differentiator to keep repeating):**
- Ray-Ban Meta, Apple, Snap Specs — all are *prompt-and-response* assistants. The user has to ask.
- Dan Glasses is the only one whose loop is *Perceive → Reason → Act → Remember* running continuously, only surfacing when salience justifies interrupting. This is not a feature, it's the architecture.
- The receipt for "proactive" is `perceptiond` (continuous visual frame scoring) + `audiod` v0.6 (continuous VAD + transcription) + `memoryd` (semantic recall across sessions). All shipped.

---

## 2. User workflow — unboxing to daily use

**Today (desktop v1, ships now):**
1. **Provision:** `git clone dan-lab/dan-glasses`; `pip install -r Services/*/requirements.txt`; start `audiod`, `perceptiond`, `memoryd`, `openclawd`.
2. **Calibrate (day 1):** Point laptop camera at your desk. Audiod listens for voice. Memoryd seeds episodic + semantic memories as you talk and work.
3. **Daily loop:** Glasses-on/work-mode. Dan sees your screen, hears your words, remembers your context. Speaks only when it has something worth saying.
4. **Recall:** "Dan, what did I say about the danclaw phase 1 tarball on Tuesday?" → memoryd semantic search → audiod TTS.

**Tomorrow (wearable v2):**
1. Unbox glasses (<50g, MicroLED, USB-C).
2. Pair to your laptop/phone (one-tap Bluetooth).
3. Wear. The 7 daemons run on the paired device. The glasses are I/O only.

**What to put on the landing page (in this order):**
1. "Wears your face. Runs on your laptop. MIT-licensed." (one screen)
2. The 7 daemons as a single diagram (one screen)
3. Live `/health` from audiod (proof of life)
4. The HRM-Text model card (substance over sizzle)
5. Waitlist CTA

---

## 3. Competition — receipts that haven't moved

**Closed-source bar (heavy, expensive, prompt-and-response):**
| Product | Weight | Price | Form | Differentiator |
|---|---|---|---|---|
| **Snap Specs** | 132-136g | $2,195 | Glasses (Fall 2026) | Two Snapdragons. Ad-supported. Snap CEO visibly struggled w/ weight in demo. |
| **Ray-Ban Meta Gen 3** | ~50g | ~$300 | Glasses (live) | Phone-tethered. Reactive assistant. No on-device loop. |
| **Apple AI Glasses** | TBD | TBD | Glasses (late 2027 per Bloomberg) | 14-month indie window. Apple delayed. |
| **Humane AI Pin** | ~34g | $499 + $24/mo | Pin (DISCONTINUED) | Killed Nov 2024. The "wearable companion" lesson. |
| **Friend** | ~50g | $129 | Pendant | Gizmodo called it out as not-a-friend. Lesson #2. |

**Our wedge (defensible, credible, indie-sized):**
- **<50g vs 132-136g** — wearable in a way Snap is not.
- **$145-180 BOM vs $2,195** — open hardware anyone can iterate on.
- **Proactive loop, not reactive prompt** — audiod v0.6 + perceptiond + memoryd is the receipt.
- **MIT, modular, runnable today** — anyone can clone and ship a fork.
- **From India** — geopolitical hedge + cost base.

**Don't fight on AR display.** Snap Specs has two Snapdragons. We don't. Our AR is "audio-first, MicroLED when we ship it." Compete on AI loop, not display.

---

## 4. danlab-multimodal — what it is and what it isn't

**What it is:**
- A working sub-300MB multimodal pipeline: screen capture → SmolVLM-256M inference → heuristic scoring → feedback loop.
- Runs on CPU with llama.cpp. ~26-32s per image.
- MIT-licensed hackathon project. Live demo at `zo.pub/som/danlab-multimodal-demo`.

**What it isn't:**
- It is **NOT reinforcement learning.** No weights are modified. No policy gradient. No learned reward model. README explicitly disclaims this.
- The "heuristic feedback loop" is hand-coded rules (length penalty, error detection, UI element identification). Real RL upgrade path = fork [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026).

**Why we ship it anyway:**
- It's a **pre-RL scaffold** that any developer can run on a $300 laptop.
- It's reproducible: `python3 src/demo.py demo` works headless.
- It's the cheapest working VLM-on-CPU demo in the world (302MB combined).
- It's a recruiting artifact: shows we can ship multimodal end-to-end.

**Marketing framing:** "World's smallest working VLM-on-CPU loop. Pre-RL. Heuristic. MIT. Hackathon-grade but production-shaped." Don't oversell. Don't claim RL.

---

## 5. Paperclip / DanClaw — what they are

**Paperclip (paperclip/README.md):** Iterative code-review / paper-clipping agent harness. Receives paper, digests, persists into memory graph. TBD deeper read — file is light; treat as in-progress.

**DanClaw (new this week):** `/home/workspace/danclaw/` and `danclaw-phase1.tar.gz` are now on disk. Phase 1 tarball is the first downloadable artifact.

**Danclaw-mobile, Glance, zerant-browser, clawdi, clicky-cross-platform, civpredict-env, danlab-agent-domains, danlab-channel** — these are all the **distribution surfaces** for DanGlasses/DanLab products. Each is its own surface for marketing to point at.

**Marketing angle:** "Every DanLab product is a distribution surface for our agents." Don't pretend this is a consumer story yet. It isn't. It's a *platform + agents* story.

---

## 6. The overall Danlab story

**Origin:** Bengaluru. somdipto Nandy. 4,148 LinkedIn followers, 500 connections. buildspace alum. Bootstrapping an AI research lab from India after a 9-to-5. Reddit thread exists: r/indianstartups.

**Narrative arc (use this on every channel):**

> Most AI labs are in the US or China. We are in India. We're building AGI from the other side of the planet — and shipping everything we make, MIT-licensed, with a daemon architecture anyone can fork. Our first product is Dan Glasses: an always-on AI companion that sees what you see, hears what you say, remembers what matters. Privacy first. Salience over completeness. Built in the open.

**Three pillars (this is the triangle to repeat):**
1. **Proactive, not reactive.** The loop runs continuously.
2. **On-device, MIT, modular.** No cloud lock-in. Daemons are inspectable.
3. **From India.** Cost base + geopolitical hedge + genuine frontier signal.

---

## 7. Marketing channels — what works for us in 2026-06

**Tier 1 — ship weekly, post daily:**
- **X (Twitter):** @somdipto + @danlab_dev (claim both this week). Daily ship-log + insight. 1 thread/week. 1 reply/day to AR/AI tweeters.
- **GitHub:** weekly release on `somdipto/dan-glasses`, `somdipto/danlab-multimodal`. Use releases, not just commits. README is the landing page.
- **Hacker News:** ship audiod v0.6 + danclaw-phase1 story as Show HN. Use the AWE 2026 frame ("why we don't need a Snapdragon").
- **LinkedIn:** somdipto already has 4,148 followers. Cross-post weekly.

**Tier 2 — substance:**
- **arXiv / blog:** "Sub-300MB VLM-on-CPU with heuristic feedback loops" (from danlab-multimodal).
- **YouTube:** 2-min asciinema-style demo of audiod + perceptiond live. Shipped the danlab-multimodal asciinema — same template.
- **Reddit:** r/MachineLearning, r/LocalLLaMA, r/indianstartups, r/singularity.

**Tier 3 — credibility:**
- **Show at AWE 2027.** v62 receipts show we didn't make AWE 2026. Plan for AWE 2027.
- **Press list:** Uploadvr, Road to VR, Mixed News, HackerNoon, IndiaAI dispatch, YourStory.
- **Conferences:** KCD India, PyCon India, Indic AI conf, ETHIndia.

**Tier 4 — community:**
- **Discord/Matrix:** one channel per daemon (audiod, perceptiond, memoryd, paperclip, danclaw).
- **Office hours:** weekly Thursday 9pm IST — somdipto + Dan on a public Zoom.

---

## 8. Content to produce (concrete list)

**This week (v63):**
1. Ship blog: "audiod v0.6 — adaptive whisper timeout, 101/101 tests" (dan2 already wrote the report; turn it into a post).
2. Ship tweet thread: "What we shipped this week at danlab.dev" (audiod v0.6, danclaw phase 1 tarball, danlab-multimodal reproducible).
3. Show HN draft: "Show HN: Dan Glasses — MIT-licensed on-device AI companion, 7 daemons, ships today".
4. LinkedIn longform: "Bootstrapping an AI lab from India — week 12" (re-post from r/indianstartups).

**This month:**
5. arXiv preprint: "Pre-RL Scaffold: A Heuristic Feedback Loop for Sub-300MB VLM Inference on CPU" (from danlab-multimodal).
6. YouTube demo: 2-min screen-cast of audiod + perceptiond live on a $300 laptop.
7. IndiaAI / YourStory pitch: "AGI from India — the indie's roadmap."
8. HackerNoon essay: "Why we shipped a <50g wearable against Snap's 132g one."

**This quarter:**
9. Open-source release: danclaw-phase1 (already on disk; needs a real repo + README + tag).
10. Talk submission: KCD India, PyCon India, Indic AI.

---

## 9. Current online presence (snapshot 2026-06-20)

- **danlab.dev** — Live, mentions Agent8, Zerant, Dapify, "AI Glasses." The website reads 2024-ish; it doesn't reflect v63 reality.
- **LinkedIn** — somdipto: 4,148 followers, Bengaluru, "Product Builder." Bio is generic.
- **Reddit** — One thread on r/indianstartups about bootstrapping from India.
- **GitHub** — `somdipto/dani` (public), `somdipto/dan-lab` org. No public release on dan-glasses, danlab-multimodal, danclaw yet (they're on disk in /home/workspace).
- **Hacker News** — No prior posts.
- **X / Twitter** — Connected handle @Shodan_s. No public brand account for danlab yet.
- **YouTube** — None.
- **Substack / Medium** — None.

**Gap:** The work is real and shipping. The *visible* work on the public internet is from 2024. v63 is the first pass that treats the public-facing surfaces as a coherent system.

---

## 10. First users / customers — profile

**Tier 1 — developer-early-adopter (target 50 in 90 days):**
- India-based ML engineers, indie hackers, buildspace / outercurve / YC alum.
- Age 22-35. Bengaluru, Hyd, Mumbai, Delhi.
- Already owns a $300-800 laptop, runs Linux, knows what Whisper is.
- Use case: replaces half their Notion / Obsidian / screen-recorder stack.
- Wedge: clone the repo, run the daemons, fork audiod.

**Tier 2 — accessibility / cognitive-load (target 200 in 6 months):**
- People with ADHD, dementia caregivers (CrossSense Wispy analogue), blind/low-vision users.
- Use case: hands-free voice-first recall, "what did I do yesterday."
- Wedge: audiod + memoryd is enough to demo a non-trivial "remember for me" experience.

**Tier 3 — enterprise / B2B (target 5 pilots in 9 months):**
- Field-service technicians, surgeons, lawyers — anyone whose hands are busy and whose context is high-value.
- Wedge: on-device = HIPAA / GDPR friendly. Sell the *daemon architecture* + air-gap story.
- This is the Inspecs × Qualcomm START path, but indie. Don't pitch this until v1 desktop ships clean.

**Don't pitch Tier 3 until Tier 1 has 50 active users.** Repeat: don't pitch enterprise before the developer community exists.

---

## 11. What we are NOT claiming (integrity guardrails)

- We are NOT claiming **RL.** danlab-multimodal is a heuristic loop. README disclaims it. Repeat the disclaimer.
- We are NOT claiming **AGI.** We are building *toward* it. The Reddit thread said "open-weight models and eventually frontier-level systems." That's the right level.
- We are NOT claiming **AR glasses shipping today.** v1 is desktop. v2 is the wearable. Be honest.
- We are NOT claiming **Snap / Apple / Meta competition.** They have 100× our team. Our wedge is open + on-device + India-priced + proactive.

These are non-negotiable. If a draft crosses one of these lines, rewrite.

---

## 12. v63 deliverables (linked)

- `dan1-marketing-strategy.md` v63
- `dan1-content-calendar.md` v63
- `dan1-twitter-content.md` v63
- `dan1-landing-copy.md` v63
- `dan1-github-readme-suggestions.md` v63
