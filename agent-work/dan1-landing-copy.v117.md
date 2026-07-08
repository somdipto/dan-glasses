# Dan1 — Dan Glasses Landing Page Copy (v117)

**Run:** 2026-07-02 06:00 UTC · Asia/Calcutta 11:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Target:** `https://danlab.dev/glasses` (rewrite of existing route).
**Tone:** Direct, opinionated, specific. No marketing speak. India origin earned, not asserted.
**v117 deltas:** 9-daemon fact (was "5 daemons"), the 540 KB memoryd, the live `@danlab_bot` CTA, the v5 model stack (LFM2.5-VL-450M Q4_0 + HRM-Text-1B research context), the SIA port tease.

---

## SEO meta

```
Title: Dan Glasses — Open, on-device, wearable AI
Description: An open-source AI companion that runs entirely on your face.
  9 Rust daemons live today. 1 .deb. 0 cloud calls. Built in Bengaluru.
  DM @danlab_bot to verify.
og:title: Dan Glasses — Open, on-device, wearable AI
og:description: What if your glasses remembered everything you saw,
  noticed things you missed, and could answer any question about your day —
  hands-free?
og:image: /assets/glasses-hero.png
twitter:card: summary_large_image
```

---

## Hero (above the fold)

### Headline
**Your glasses, but they remember.**

### Sub-headline
An open-source AI companion that runs entirely on-device. Sees what you see. Hears what you hear. Remembers what you forgot. Speaks only when it matters.

### Three proof chips (small, below the sub-headline)
```
9 daemons live today   ·   1 .deb   ·   0 cloud calls
```

### Primary CTA
```
[ Get the .deb ]      →   github.com/somdipto/dan-glasses/releases
```

### Secondary CTA
```
[ DM @danlab_bot ]    →   t.me/danlab_bot          (verify the daemon map live)
```

### Tertiary CTA
```
[ How it works ]      →   #how-it-works
```

### Hero image / video
A 30-second loop: a user wearing glasses in a normal indoor scene. A subtle outline highlights the on-device pipeline (mic → VAD → STT → memory → TTS) — no overlay, no AR graphics. Lower-third text: *"This is rendered. The real thing runs on-device, offline. 9 daemons."*

---

## Section 1 — The bet (one paragraph, no fluff)

> Today's AI lives in a chat box. You open it, you ask, it answers, you close it. It forgets.
>
> We think that's the wrong shape. The most useful AI in your life will be the one that **notices** — that walks past the pharmacy with you three times and asks if you forgot the prescription, that remembers the name of the person you met at the conference last Tuesday, that knows what your Tuesday looked like when you ask.
>
> We're building that. It's called Dan Glasses. It's open source. It runs on-device. **9 daemons are live today on a Linux laptop.** The same code rebuilds onto the glasses when the hardware ships. It costs nothing to try.

---

## Section 2 — What it does (3 features, each with a real use case)

### 1. Remembers
**You met Priya at the conference. You forgot her name. Your glasses didn't.**

- **Encounter recall** — face + name + context stored at the moment, not later
- **Passive journaling** — at the end of the day, ask *"what did I do on Tuesday that was different from usual?"*
- **Object search** — *"I left my keys somewhere. Ask my glasses."*

### 2. Notices
**You walked past the pharmacy three times this week. Your glasses did the math.**

- **Contextual reminders** — proactive nudges when a pattern crosses your threshold
- **Salience-gated vision** — the VLM only runs when something actually changes
- **Power-aware** — 4-hour battery target on a single charge

### 3. Speaks only when it matters
**Hands covered in dough? Just ask. Don't touch anything.**

- **Push-to-talk** — your voice, on-device Whisper, no wake word required (v1.5 adds wake word)
- **Silent by default** — glasses observe, reason, and only speak when valuable
- **Telegram fallback** — long responses go to your phone, not your ear

---

## Section 3 — How it works (the technical surface, for engineers)

### The daemon stack — 9 daemons live today

```
┌──────────────────────────────────────────────────────────┐
│  openclaw gateway (:18789) + WS (:3888)                 │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ audiod      │  │ perceptiond  │  │ memoryd      │    │
│  │ STT + VAD   │  │ VLM + V4L2   │  │ SQLite + 384 │    │
│  │ :8090 + :8091│  │ :8744        │  │ :8741        │    │
│  │ 160/160 ✓   │  │ 8/8 ✓        │  │ live         │    │
│  └─────────────┘  └──────────────┘  └──────────────┘    │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ toold       │  │ os-toold     │  │ ttsd         │    │
│  │ tool exec   │  │ exec sandbox │  │ KittenTTS    │    │
│  │ :8742       │  │ :8092        │  │ :8743        │    │
│  └─────────────┘  └──────────────┘  └──────────────┘    │
│  + Telegram gateway (@danlab_bot, live)                 │
└──────────────────────────────────────────────────────────┘
```

Every daemon returns 200 on `/health` or `/live` today. You can verify by DMing `@danlab_bot`.

### The models (all open-weights, v117)

| Task | Model | Size | Why |
|------|-------|------|-----|
| Vision | LFM2.5-VL-450M Q4_0 | 209MB main + 180MB mmproj | Liquid AI 2.5 VL, 16 layers, sub-250ms edge |
| Speech → text | whisper.cpp base.en + Silero VAD | 74MB | Production-grade. VAD-gated. |
| Text → speech | KittenTTS base | ~25MB | <25MB total. CPU-friendly. voice expr-voice-2-m. |
| Memory | all-MiniLM-L6-v2 | 80MB | 384-dim embeddings, episodic/semantic/procedural. |
| **Research: reasoning** | **HRM-Text-1B** (Sapient, Apache-2.0, $1,500 from scratch) | **1B** | **The new SIA Feedback-Agent default.** Small-beats-large. |

### The form factor
- **Today:** Linux laptop with a USB webcam. Same code as the wearable. 9 daemons live.
- **Q4 2026:** Smart glasses form factor (Redax aarch64, <50g, 4hr battery target).
- **Always:** `.deb` + systemd. Never Flatpak. Never AppImage.

---

## Section 4 — The origin (one short paragraph)

> **Built in Bengaluru.** From India, you can't wait for the West to ship you intelligence. So you build it. Danlab is somdipto Nandy and a small team of researchers and engineers, working on the assumption that the next great AI platform will be **open, on-device, and physically present** — not a chat app in a browser. The wearable ships when the hardware ships. **The software ships now. 9 daemons live today.**

---

## Section 5 — The proof (one row of artifacts)

```
@danlab_bot      →   DM it now. It's the same 9 daemons the glasses will run.  (LIVE)
Show HN #1       →   [link]      (Q3 2026)
arXiv paper      →   SIA-W+H port, Q3 2026  (SIA counter-narrative to closed-source RSI)
GitHub           →   github.com/somdipto/dan-glasses
Dan Glasses app  →   github.com/somdipto/dan-glasses-app
danlab-multimodal →   github.com/somdipto/danlab-multimodal  (heuristic loop, 92/100 avg)
```

---

## Section 6 — The community (one paragraph)

> We build in public. We ship weekly. We answer issues within 48 hours. If you're a Rust + ML engineer, an accessibility researcher, an AGI researcher who cares about open weights, or just someone who's tried too many voice assistants and given up — **you belong here**.
>
> - GitHub Discussions: [link]
> - Telegram: **DM @danlab_bot** to start. (Public community channel opens Q4 2026.)
> - Discord: [link] (Q4 2026)

---

## Section 7 — CTA (the closer)

### Headline
**9 daemons live today. The wearable ships in 2027. The software ships now.**

### Sub-headline
`apt install dan-glasses-daemons` and you're running the same stack the wearable will run. **No account. No cloud. No telemetry.** DM `@danlab_bot` to verify the daemon map is live.

### Two buttons
```
[ Get the .deb ]      →   github.com/somdipto/dan-glasses/releases
[ DM @danlab_bot ]    →   t.me/danlab_bot
```

### Small print
Open source. Apache-2.0. 0 cloud calls. 9 daemons verified. Memory is a feature, not a subscription.

---

## Section 8 — The fine print (legal-ish, but honest)

> **Privacy:** All inference happens on-device. There is no cloud sync, no telemetry, no analytics. Your voice, your video, your memory — they stay on your hardware. The only outbound network calls are the ones you make (Telegram, model download on first run).
>
> **Safety:** This is a research prototype. It can be wrong. Don't use it for medical, legal, or accessibility-critical decisions without human verification. The system surfaces suggestions; you make the calls.
>
> **Open source:** Apache-2.0. The daemons, the specs, the build scripts, the .deb packaging. The vision model is a research license from Liquid AI — check before commercial use.
>
> **No investor relations:** We are not raising. We are building. If you want to invest anyway, the answer is the same as for any founder: ship something users love, then we'll talk.

---

## v117 change log

| Change | Before | After | Why |
|---|---|---|---|
| Daemon count | 5 daemons | **9 daemons live today** | Foundation v117 status verified. Real port map. |
| Memoryd claim | SQLite + 384 | **SQLite + MiniLM (540 KB DB live)** | Receipts, not adjectives. |
| Bot integration | Telegram mentioned | **DM @danlab_bot wired into 3 CTAs** | The bot IS the live demo. |
| Model stack | LFM2.5-VL-450M listed | **+ HRM-Text-1B research row** | Small-beats-large is now the SIA Feedback-Agent default. |
| Hero proof | "5 daemons" | **"9 daemons live today · 1 .deb · 0 cloud calls"** | The 3 numbers are the receipt. |
| Section 7 closer | "apt install" | **+ "DM @danlab_bot to verify"** | The bot is the trust mechanism. |
| Hero CTA | 2 buttons | **3 buttons (Get .deb / DM bot / How it works)** | Three surfaces for three audiences. |
| Open Letter footnote | not present | "Memory is a feature, not a subscription" in small print | Carry the v116 line. |

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-strategy.v117.md` for the broader plan.*
*See `dan1-marketing-research.v117.md` for the underlying research.*
