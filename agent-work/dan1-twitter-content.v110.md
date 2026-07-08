# DanLab Twitter/X Content — Run v110
**Date:** 2026-06-29
**Owner:** DAN-1
**Audience:** Technical founders, AI engineers, privacy-conscious builders, India-tech diaspora.
**Format note:** Each post is a Tweet or thread with the exact character count. Replace the bracketed placeholders when posting.

---

## 0. Bio

**Line 1 (≤70 chars):**
```
Proactive AI you can audit. Dan Glasses + Dan Voice + Paperclip. Open source. From India 🇮🇳
```

**Line 2:**
```
🧠 github.com/somdipto/dan-consciousness
🥽 github.com/somdipto/dan-glasses
🏗 github.com/somdipto/dan-lab
```

**Location:** Bengaluru, India (set in profile settings, not in bio).

**Link:** pin one of the four product URLs above; rotate monthly.

---

## 1. Post #1 — Launch tweet (pin for 7 days)
**Goal:** announce the public lineup.
**Format:** single tweet, no media.

> 4 open repos. 9 daemons live on my Linux laptop. 1 heuristic feedback loop that scores 92/100. We are building Dan — a proactive personal AI — from India.
>
> The brain: github.com/somdipto/dan-consciousness
> The glasses: github.com/somdipto/dan-glasses
> The orchestrator: github.com/somdipto/paperclip
> The demo: github.com/somdipto/danlab-multimodal
>
> All MIT. All open. Read the source. 🧠

**Why this works:** first number is "4 open repos," second is "9 daemons live" — concrete. No adjectives. Ends with a CTA.

---

## 2. Post #2 — Privacy one-liner
**Goal:** position against Quark/Meta/Apple.
**Format:** single tweet, no media.

> Quark AI Glasses: data in Alibaba cloud.
> Meta Ray-Ban: data in Meta cloud.
> Dan Glasses: data in *your* Docker container.
>
> I cannot read your emails even if I wanted to. Not "we promise." Architecturally cannot.

**Why this works:** three competitors named explicitly. Architecture claim is verifiable (read the open-source code).

---

## 3. Post #3 — Dan Voice announcement thread (5 tweets)
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
> - Push-to-talk + wake word
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

## 4. Post #4 — Watchful mode demo (visual)
**Goal:** showcase the daemon-level proactive AI.
**Format:** 30-second screen recording (use agent-browser or ffmpeg to capture).

> Two laptops, two cameras. Watch the watchful mode.
>
> The girl on the left moves. The glasses fire perceptiond. Salience passes. VLM runs. Memory stores. The right screen shows the description event arriving in real time.
>
> Open source. Sub-10W. Runs on a £300 laptop.
>
> Repo: github.com/somdipto/dan-glasses · "perceptiond"

---

## 5. Post #5 — India AGI builder thread (engagement bait by accident)
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
> - Home-grown inference (SmolVLM-256M + LFM2.5-VL + HRM-Text-1B)
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

## 6. Post #6 — 9-daemons-quickstats (engineering credibility)
**Goal:** signal engineering depth.
**Format:** single tweet + a screenshot of the daemon dashboard.

> 9/9 daemons live on my Linux laptop today.
>
> audiod (8090) · audiod-ws (8091) · perceptiond (8092) · memoryd (8741) · toold (8742) · ttsd (8743) · os-toold (8744) · openclaw-web (18789) · dan-glasses-app (3888)
>
> 137+ tests passing on audiod alone. 8/8 on perceptiond.
>
> Open source daemon-by-daemon. Each one isolated. Each one tested. github.com/somdipto/dan-glasses

---

## 7. Post #7 — Build-in-public: hardware v2 update
**Goal:** show work-in-progress honestly.
**Format:** single tweet + photo of the ForgeCAD render.

> Hardware status: blocked on Redax board.
>
> What I have: a 97-part parametric glasses model in ForgeCAD. A working daemon stack that runs on a laptop. A 3D-printed frame test-fit that I am not showing anyone yet.
>
> What I need: the actual board.
>
> Specs if you can source: github.com/somdipto/dan-glasses/wiki/hardware

---

## 8. Post #8 — Plug Paperclip (developer-focused)
**Goal:** recruit Python/TS developers.
**Format:** tweet + repo link.

> If you ever wanted an open-source alternative to LangChain + Temporal + n8n in one repo —
>
> Paperclip orchestrates AI agents. Multi-agent runs. Issue tracking. Goal management. One Docker image.
>
> github.com/somdipto/paperclip
>
> Built by one founder in Bengaluru. Tested in production. Fork-friendly MIT.

---

## 9. Post #9 — "From India" one-pager
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

## 10. Post #10 — "What is proactive AI" explainer (evergreen)
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
> Dan Glasses does all four. Perceptiond watches. Memoryd remembers. Paperclip orchestrates. TTS speaks.
>
> Demo: github.com/somdipto/dan-glasses
> Whitepaper: github.com/somdipto/dan-consciousness/wiki/proactive-ai

---

## 11. Post cadence

| Day | Platform | Post |
|---|---|---|
| Mon | Twitter | Engineering-credibility post (e.g., 9-daemons) |
| Tue | LinkedIn | Cross-post Post #5 (India thread) |
| Wed | Twitter | Product-positioning (Post #2, #3, or #10) |
| Thu | Dev.to | Long-form blog (~1k words, see content calendar) |
| Fri | Twitter | Founder-personal (Post #7, #9) |
| Sat | YouTube Short | Demo (Post #4, narrated) |
| Sun | — | rest, research the next week |

Adjusted to somdipto's timezone (Asia/Calcutta).

---

## 12. Banned phrasings (will auto-reject)

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

*End of Twitter content. Companion artifacts: [strategy](./dan1-marketing-strategy.v110.md), [calendar](./dan1-content-calendar.v110.md), [landing copy](./dan1-landing-copy.v110.md), [README suggestions](./dan1-github-readme-suggestions.v110.md).*
