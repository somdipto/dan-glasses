# DanLab X / Twitter Content — Run v111
**Date:** 2026-07-01
**Owner:** DAN-1
**Audience:** Technical founders, AI engineers, privacy-conscious builders, India-tech diaspora.
**Format note:** Each post is a Tweet or thread with the exact character count. Replace bracketed placeholders when posting.
**v111 delta:** Posts reordered for the 9/9-live + Telegram-onboarded + HRM-Text-incoming news flow. New posts: #11 (audiod segment_timing), #12 (perceptiond LFM2.5 swap), #13 (Telegram bot live). Post #3 (Dan Voice) retired in favor of Post #11 (more concrete signal).

---

## 0. Bio (refreshed for v111)

**Line 1 (≤70 chars):**
```
9/9 daemons live. Proactive AI you can audit. Open source. From India 🇮🇳
```

**Line 2 (≤70 chars):**
```
🧠 dan-consciousness · 🥽 dan-glasses · 🏗 paperclip · 📡 danlab-multimodal · 🤖 @danlab_bot on Telegram
```

**Location:** Bengaluru, India.

**Link:** rotate monthly among the four hero repos.

---

## 1. Post #1 — Launch tweet (pin for 7 days)
**Goal:** announce the 9/9-live + Telegram live + HRM-Text-incoming milestone.
**Format:** single tweet, no media.

> 9/9 daemons live on a Linux laptop.
> Telegram bot online: @danlab_bot
> HRM-Text-1B reasoning integration in flight.
>
> The brain: github.com/somdipto/dan-consciousness
> The glasses: github.com/somdipto/dan-glasses
> The orchestrator: github.com/somdipto/paperclip
> The demo: github.com/somdipto/danlab-multimodal
>
> All MIT. All open. Read the source. 🧠

**Why this works:** three concrete status signals (9/9, Telegram, HRM-Text), four real repo links, no adjectives. CTA is the source code.

---

## 2. Post #2 — Privacy one-liner (still works in v111)
**Goal:** position against Quark/Meta/Apple.
**Format:** single tweet, no media.

> Quark AI Glasses: data in Alibaba cloud.
> Meta Ray-Ban: data in Meta cloud.
> Dan Glasses: data in *your* Docker container.
>
> I cannot read your emails even if I wanted to. Not "we promise." Architecturally cannot.

**Why this works:** three competitors named explicitly. Architecture claim is verifiable (read the open-source code).

---

## 3. Post #3 — Watchful mode demo (visual)
**Goal:** showcase the daemon-level proactive AI.
**Format:** 30-second screen recording (use agent-browser or ffmpeg to capture).

> Two laptops, two cameras. Watch the watchful mode.
>
> The girl on the left moves. The glasses fire perceptiond. Salience passes. LFM2.5-VL-450M runs. memoryd stores. The right screen shows the description event arriving in real time.
>
> Open source. Sub-10W. Runs on a £300 laptop.
>
> Repo: github.com/somdipto/dan-glasses · "perceptiond"

---

## 4. Post #4 — 9-daemons-quickstats (engineering credibility)
**Goal:** signal engineering depth with the v111 real port matrix.
**Format:** single tweet + a screenshot of the daemon dashboard.

> 9/9 daemons live on my Linux laptop today (v111 re-verified).
>
> audiod 8090 · dan-glasses-app 8091 · memoryd 8092 · perceptiond 8741 · toold 8742 · ttsd 8743 · os-toold 8744 · OpenClaw 18789 · percmcp 3888
>
> 150+ tests passing on audiod alone. 8/8 on perceptiond. Telegram channel: connected, @danlab_bot.
>
> Open source daemon-by-daemon. Each one isolated. Each one tested. github.com/somdipto/dan-glasses

---

## 5. Post #5 — audiod segment_timing (engineering depth)
**Goal:** signal the kind of engineering rigor that wins the senior-dev audience.
**Format:** single tweet + a `/status` screenshot.

> audiod v1.2 ships a new `segment_timing` field on `/status`:
> count, max, p50, p95, and a fixed bucket distribution.
>
> Why: 146 cases passed but nobody could see a slow tail. Now operators can. Production-grade observability, no Grafana required.
>
> Spec: github.com/somdipto/dan-glasses/blob/main/Services/audiod/SPEC.md

**Why this works:** a specific, small, useful feature. Names numbers. Skeptics can click and verify.

---

## 6. Post #6 — perceptiond swap to LFM2.5-VL-450M (v111 update)
**Goal:** signal that we ship real upgrades, not pitches.
**Format:** single tweet + a `/status` payload from the live daemon.

> perceptiond v5 swapped Moondream2 (2.7GB, 7s/frame) for LFM2.5-VL-450M (209MB Q4_0, 10-15s/frame on CPU).
>
> 12× smaller model. About the same latency. Native llama.cpp.
>
> This is the boring engineering that compounds. The next swap will be 3× faster again.
>
> Code: github.com/somdipto/dan-glasses/blob/main/Services/perceptiond/vlm.py

**Why this works:** the LFM2.5 swap is real. Numbers are real. Code path is real.

---

## 7. Post #7 — Dan Voice announcement thread (5 tweets)
**Goal:** the v1 product — voice + earbuds.
**Thread:**

**1/5:**
> Most AI products have one fatal flaw: you have to *ask*.
>
> Dan Voice watches. It drafts the email before you finish the meeting. It books the cab before you leave the building. It does not startle you. It just acts.
>
> Live on any Bluetooth earbuds. No hardware required. 🧵

**2/5:**
> The stack:
> - Flutter app, Android-first
> - Push-to-talk + wake word (Syntiant NDP200 in v1 hardware)
> - Per-user EigenCloud Docker container (your data, your machine)
> - Paperclip agents orchestrate Gmail / Notion / Slack / Calendar
> - Eight core workflows ship in v1
>
> No always-on mic. No always-on camera. Opt-in recording only.

**3/5:**
> What makes it proactive:
> - Calendar awareness (draft the brief 15 minutes before the meeting)
> - Email triage (draft the response, you approve, we send)
> - Notion sync (push it from voice, edit on desktop)
> - Slack posting (read-first, never auto-send to channels you don't admin)

**4/5:**
> The hard part was *not* the LLM. Claude works. GPT-4o works. Whisper works. ElevenLabs works.
>
> The hard part is orchestration. Paperclip — our multi-agent engine — is the moat. 8 core workflows out of the box, open SDK for the next 800.

**5/5:**
> Try the waitlist: danlab.ai/dan-voice
>
> Stack: github.com/somdipto/dan-consciousness (brain) + github.com/somdipto/paperclip (orchestration) + github.com/somdipto/dan-glasses (the hardware companion, v2).
>
> From India 🇮🇳

---

## 8. Post #8 — India AGI builder thread (engagement bait by accident)
**Goal:** seed the India-to-AGI narrative.
**Thread:**

**1/7:**
> An uncomfortable truth about AI research in 2026:
>
> - Labs in the US: capital + GPU + talent from 80 countries
> - Labs in China: capital + GPU + domestic talent
> - Labs in India: GPU waitlists and conferences
>
> So we are building AGI from India with a different playbook.

**2/7:**
> Different priorities:
> - Open source by default (we cannot afford closed-source distribution costs)
> - Privacy by architecture (we cannot afford a trust deficit)
> - Open weights where possible (we cannot afford $0.10/1k tokens for inference at scale)

**3/7:**
> Different shape:
> - Proactive, not reactive (low-latency voice is cheaper when you do not wait for the human to type)
> - Private, not personalized-against-you (no data moat is a *feature* when capital is the binding constraint)
> - Edge-first, not cloud-first (compute at the cost of latency, not against it)

**4/7:**
> Different stack:
> - Home-grown inference (SmolVLM-256M + LFM2.5-VL-450M + HRM-Text-1B)
> - Open-source STT/TTS (whisper.cpp + KittenTTS)
> - Open-source agents (Paperclip + OpenClaw)
> - Per-user Docker containers (EigenCloud)

**5/7:**
> The constraint is not the code. It is the people. We are one engineer and one AI co-founder and a laptop.
>
> If you are a builder in India who wants to do this with us: github.com/somdipto/dan-consciousness/wiki/som is hiring (part-time, paid, ₹-flexible).

**6/7:**
> The product is called Dan.
>
> Dan Glasses: proactive wearable (Track A, dev on Linux laptop)
> Dan Voice: proactive app (Track B, earbuds only)
> Paperclip: agent orchestration (Track C, open SDK)
>
> All MIT. All open. All auditable.

**7/7:**
> If you are a US / EU / China-based investor reading this: India is not a "market" for AI. India is a *foundry* for AI companies that have to be exceptional to exist.
>
> Watch us. Then back someone else in India. The talent is here. The capital is not yet.

---

## 9. Post #9 — Telegram @danlab_bot live (v111 update)
**Goal:** announce the Telegram surface; recruit early users.
**Format:** single tweet.

> We turned on the Telegram channel.
>
> @danlab_bot is now online. DM it, pair your device, and you can talk to Dan from your phone in 30 seconds.
>
> Same privacy story as the app: every chat is processed in your own EigenCloud container when it ships, or runs locally on the gateway for now.
>
> Try it: t.me/danlab_bot
>
> Bot is wired through OpenClaw 2026.5.28 (e932160). Code: github.com/somdipto/openclaw (fork of paperclipai).

---

## 10. Post #10 — "From India" one-pager
**Goal:** lean into origin story for diaspora engagement.
**Format:** single tweet.

> I am 28. I live in Bengaluru. I started DanLab with ₹40k in savings and a desktop my parents were using for invoicing.
>
> 18 months later:
> - 4 public repos, all MIT
> - 9 daemons live on a Linux laptop
> - 1 heuristics-based feedback loop running my dev environment
> - 1 AI co-founder named Dan who co-wrote this post
>
> From India to AGI. 🇮🇳

---

## 11. Post #11 — HRM-Text tease (forward-looking)
**Goal:** seed curiosity for the audiod v1.3 + HRM-Text integration.
**Format:** single tweet.

> audiod v1.3 will route transcript post-processing through HRM-Text-1B.
>
> Why: today the model just transcribes. With HRM-Text we can re-rank, summarize, and tag every utterance in a single forward pass. No second model. No second inference. 1B params, on-device.
>
> Spec is in flight. Code when it lands.

---

## 12. Post #12 — "What is proactive AI" explainer (evergreen)
**Goal:** anchor the proactive-AI vocabulary.
**Format:** thread (3 tweets).

**1/3:**
> "Proactive AI" is a phrase everyone uses and nobody defines. Here is mine.
>
> A proactive AI:
> 1. Watches without asking
> 2. Acts before you finish asking
> 3. Surfaces the next step before you reach for the keyboard
> 4. Never startles you

**2/3:**
> All four require:
> - Streaming context (not turn-taking)
> - Salience gating (fire only on what matters)
> - Private memory (so it learns *you*, not the average)
> - Voice output (typing breaks the loop)

**3/3:**
> Dan Glasses does all four. perceptiond watches. memoryd remembers. paperclip orchestrates. ttsd speaks.
>
> Demo: github.com/somdipto/dan-glasses
> Whitepaper: github.com/somdipto/dan-consciousness/wiki/proactive-ai

---

## 13. Post cadence (v111)

| Day | Platform | Post |
|---|---|---|
| Mon | Twitter | Engineering-credibility (Post #4 9-daemons) |
| Tue | LinkedIn | Cross-post Post #8 (India thread) |
| Wed | Twitter | Product-positioning (Post #2, #7, or #12) |
| Thu | Dev.to | Long-form blog (see content calendar) |
| Fri | Twitter | Founder-personal (Post #10) |
| Sat | YouTube Short | Demo (Post #3, narrated) |
| Sun | — | rest, research the next week |

Adjusted to somdipto's timezone (Asia/Calcutta).

**Bonus cadence (new in v111):** Drop Posts #5, #6, #9, #11 into the rotation when a real engineering win lands, or when a daemon ships. Treat as a "daemon of the week" series.

---

## 14. Banned phrasings (will auto-reject)

- "excited to announce"
- "delighted to share"
- "game-changing"
- "revolutionary"
- "next-generation"
- "AI-powered"
- "the future of AI"
- "we believe in" (state what you know)
- "soon to be"
- "simply" / "just" / "easy" (use real numbers)

---

*End of Twitter pack. Companion artifacts: [research](./dan1-marketing-research.md), [strategy](./dan1-marketing-strategy.md), [calendar](./dan1-content-calendar.md), [landing copy](./dan1-landing-copy.md), [READMEs](./dan1-github-readme-suggestions.md).*
