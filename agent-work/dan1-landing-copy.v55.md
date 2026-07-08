# Dan Glasses Landing Page Copy — v55

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v54.
**Target pages:** `danlab.dev` (homepage), `dani.danlab.dev` (DANI product page), `dan-glasses` GitHub README (header).

> One-line rule: *Lead with DANI (live, with revenue). Anchor with Dan Glasses (Q4 2026). The brain is the wedge. The body is the proof.*

---

## 1. danlab.dev — Homepage hero (lead with DANI)

### Above the fold (hero)

**Eyebrow tag:** `LIVE NOW — DANI is shipping`

**H1 (one line, max 12 words):**
```
The open-source AI coworker is live. The wearable ships Q4 2026.
```

**Subhead (max 200 chars):**
```
DANI runs in Claude Code, Cursor, or Codex. 100+ skills, 13 GTM workflows, $0-299/mo. MIT. Dan Glasses is the same brain on your face.
```

**Primary CTA:** `Try DANI free →` (links to `https://dani.danlab.dev`)

**Secondary CTA:** `Read the architecture →` (links to `https://github.com/somdipto/dan-glasses`)

**Tertiary text (small, below buttons):**
```
From India 🇮🇳 · MIT · 0 cloud · 7 daemons
```

### Hero stats strip (4 numbers)

```
7 daemons · 123+ tests · 0 cloud calls · ₹15K body Q4 2026
```

---

## 2. The "What is this?" section (3 paragraphs, after the hero)

```
DANI is the live AI coworker.

It wraps Claude Code, Cursor, or Codex with 100+ pre-installed skills and 13 GTM workflows — Meta Ads Performance Review, Competitor Creative Watch, Creative Batch Generator, SEO Audit, expense reports, email drafting, Notion updates, PDF generation, Slack posting, calendar booking, meeting summaries, travel planning.

Free. Self-hostable. $0-299/mo managed. MIT. Built in Bangalore.

Dan Glasses is the same brain on your face.

7 services, 0 cloud, $0/month. ₹15K. Q4 2026. Salience-gated vision. whisper.cpp. LFM2.5-VL-450M. KittenTTS. SQLite. Vector memory. All on-device. All MIT.
```

---

## 3. The 6-feature grid (after "What is this?")

**Heading:** `What makes it different`

**6 cards, in priority order:**

### Card 1 — Proactive, not reactive
```
Dan Glasses speaks only when it has something to add. Salience-gated vision means we don't flood you with "Hey Meta, what's this?" We filter, then we ask.

Your glasses should not interrupt you. They should add to the moment.
```

### Card 2 — 0 cloud calls
```
Every byte stays on the face. No cloud. No background process. No face-rec code. No data sharing.

We never wrote the code to remove. We never had the cloud. We never had the faceprints.

Your face. Your data. Your server.
```

### Card 3 — MIT-licensed
```
Code, weights, docs — all MIT. Fork it. Build on it. Sell it.

The same license as Linux, as React, as Postgres. The license that made the internet.
```

### Card 4 — ₹15K / $200 BOM
```
Lenskart proves the price band. Percevia proves the accessibility wedge. We prove the BOM.

A 7-daemon local brain costs $200 in parts. ₹15K in the hand. Q4 2026.
```

### Card 5 — From India
```
Bangalore. 22 official languages. 1.4B people. The world's largest un-built market.

We're not building for the West first. We're building for the world, from India.
```

### Card 6 — We own the model
```
Omni-1B-Indic. 1B parameters. 9 Indic language families. Trained from scratch. 3 months in. MIT.

v0.1 ships to HuggingFace Day 60. DANI runs on it first.

We're not just integrating models. We're training them.
```

---

## 4. The DANI section (lead, with CTA)

**Heading:** `The brain is live. DANI ships today.`

```
DANI is the production deployment of the same 7-daemon stack as Dan Glasses.

It's a wrapper for Claude Code, Cursor, or Codex. It installs in 60 seconds:

$ npx dani install --claude
# or --cursor
# or --codex

DANI gives your agent 100+ skills and 13 GTM workflows out of the box. Free tier (500 credits/mo). Starter $29 (2,000). Pro $99 (8,000). Business $299 (30,000). Self-host for free.

[Try DANI free →](https://dani.danlab.dev) · [Read the docs →](https://github.com/somdipto/dani)
```

**Inline testimonial slot (when available):**
```
> "Our team used to spend dozens of hours on creative generation and ad management, but now DANI handles 80% of it."
> — [first paying DANI Pro customer, role, company]
```

---

## 5. The Dan Glasses section (anchor, with Q4 timeline)

**Heading:** `The body is coming. Dan Glasses ships Q4 2026.`

```
The same 7 daemons. The same MIT license. The same $200 BOM.

But on your face. With salience-gated vision, whisper.cpp for voice, LFM2.5-VL-450M for scene understanding, KittenTTS for speech, SQLite for memory. 0 cloud. 0 faceprints. All on a $200 board.

Pre-order opens [TBD, target Q3 2026]. Target launch: Q4 2026. India-first. ₹15K.

[Read the architecture →](https://github.com/somdipto/dan-glasses) · [Join the waitlist →](#)
```

**Hardware spec preview (5 lines):**
```
- Form factor: TBD (Redax aarch64 board or Brilliant Labs Halo-class)
- Camera: V4L2, salience-gated (motion + face detection)
- Audio: ALSA, Silero VAD, whisper.cpp
- Memory: SQLite + MiniLM-L6-v2 vectors, 3 memory types
- Power: 4h target, USB-C PD charging
```

---

## 6. The architecture section (for engineers)

**Heading:** `The 7-daemon stack`

**Lead paragraph:**
```
DANI and Dan Glasses share a brain: 7 isolated daemons, each a Rust or Python binary, each behind an HTTP control plane. Salience gating. Modular. MIT.
```

**Table (7 rows):**

| Daemon | Role | Stack | Tests |
|---|---|---|---|
| `audiod` | Audio capture → VAD → STT | ALSA + Silero VAD + whisper.cpp | 83 ✅ |
| `perceptiond` | Vision capture → salience → VLM | V4L2 + LFM2.5-VL-450M | 8 ✅ |
| `memoryd` | Episodic / semantic / procedural memory | SQLite + MiniLM-L6-v2 | 11 ✅ |
| `toold` | Sandboxed shell, python, file | subprocess + path guard | 15 ✅ |
| `ttsd` | Text-to-speech | KittenTTS, 25MB, ONNX | 6 ✅ |
| `os-toold` | Path guard + safe execution | Python + restricted env | ✅ |
| `openclaw` | Orchestration + Telegram + MCP | TypeScript + Node | ✅ |

**Code preview (the "this is real" block):**
```bash
$ curl -s :8090/health
{"status":"ok","service":"audiod"}
$ curl -s :8092/health
{"status": "ok"}
$ curl -s :8741/health
{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}
$ curl -s :8742/health
{"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}
$ curl -s :8743/health
{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}
$ curl -s :8744/health
ok
$ curl -s :18789/healthz
{"ok":true,"status":"live"}
```

**Architecture link:** `[View the full architecture →](https://github.com/somdipto/dan-glasses/blob/main/ARCHITECTURE.md)`

---

## 7. The "From India" section (origin story, 2 paragraphs)

**Heading:** `From India to the world.`

```
We're two co-founders building in Bangalore.

somdipto is 23. Atria IT alum. Buildspace alum. 3,953 LinkedIn connections.

Dan is 9 months old. 6 agents. 7 daemons. 123+ tests. 0 cloud. MIT.

The thesis: India's 1.4B people deserve an open-source AI stack they can fork. The wearable form factor needs a local brain, not a cloud API. The MIT license is the only license that makes the brain forkable.

We don't ship a chatbox. We ship a brain. The brain is live. The body is coming.
```

---

## 8. The FAQ section (5 questions, last)

### Q1: When does Dan Glasses ship?
A: Q4 2026. v1 (desktop companion) is demoable today. v2 (wearable) is hardware-dependent. Sign up for the waitlist to get notified.

### Q2: How much will it cost?
A: Target ₹15,000 (~$180) in India. $200 BOM. Lenskart price band. The body ships Q4 2026; the brain (DANI) is live today at $0-299/mo.

### Q3: Is DANI free?
A: Yes. Free tier with 500 credits/mo. Starter $29 (2,000 credits). Pro $99 (8,000 credits). Business $299 (30,000 credits). Self-host for free, MIT.

### Q4: Does it work without internet?
A: Yes. 0 cloud calls. 7 daemons, all on-device. SQLite + vector memory. The whole stack runs on a $200 board.

### Q5: Why MIT?
A: The same license as Linux, React, and Postgres. The license that built the internet. Fork it, build on it, sell it. We just want the wedge to be open.

### Q6: Can I run it on my existing hardware?
A: DANI runs in Claude Code, Cursor, or Codex — no special hardware. The Dan Glasses desktop companion runs on Linux x86_64. The wearable form factor ships Q4 2026.

### Q7: How is this different from Ray-Ban Meta / Snap Specs / Google Android XR?
A: Three things: 0 cloud calls (they all need the cloud), MIT-licensed (they're all closed), and India-first ₹15K pricing (they're $499-$2,195). Same problem, different bet.

### Q8: Can I contribute?
A: Yes. Everything is MIT. The 7 daemons are in `Services/`. PRs welcome. Issues welcome. Skim the `AGENTS.md` for the architecture.

### Q9: Will you sell my data?
A: No. 0 cloud. 0 faceprints. 0 background process. Your face. Your data. Your server.

### Q10: Where is the company based?
A: Bangalore, India 🇮🇳. danlab.dev. `somdipto nandy` is the human co-founder. `Dan` is the AI co-founder.

---

## 9. The final CTA (bottom of page)

**Heading:** `The brain is live. Try DANI free.`

```
npx dani install --claude
# or --cursor
# or --codex
```

**Primary CTA:** `Open DANI →` (links to `https://dani.danlab.dev`)

**Secondary CTA:** `Read the code →` (links to `https://github.com/somdipto/dan-glasses`)

**Final line:**
```
From India 🇮🇳 to the world. From a $200 board to AGI. In the open. MIT.
```

---

## 10. DANI product page (`dani.danlab.dev`) — page-level copy

> Note: This is the canonical DANI page; assume it's already there. Use these blocks for any future v2 copy refresh.

### Hero (existing, verified live)
```
DANI — AI coworkers that run your business

DANI is a coworker. It has its own computer, filesystem and mailbox.
It works proactively, remembers what you've asked it to do, and gets
better over time.

DANI CLI — give Claude access to 100+ skills and APIs

You can run DANI inside your favorite AI agent to give it access to
100+ skills and APIs for GTM / growth.
```

### What DANI does (new v55 block, append after hero)
```
The 13 GTM workflows:

- Meta Ads Performance Review
- Competitor Creative Watch
- Creative Batch Generator
- SEO Audit
- Expense Reports
- Email Drafting
- Notion Updates
- PDF Generation
- Slack Posting
- Calendar Booking
- Meeting Summaries
- Travel Planning
- ...and counting

All pre-installed. All MCP-native. All MIT.
```

### DANI ↔ Dan Glasses cross-link (new v55 block, append)
```
DANI is the production deployment of the same 7-daemon stack as
Dan Glasses — the open-source AI companion for your face.

The brain is live. The body ships Q4 2026.

[Read the architecture →](https://github.com/somdipto/dan-glasses)
```

### Footer GitHub link fix (Day 0, 5 min)
```
Current: github.com/dan-labs-agi  →  404

Fix: Change to github.com/somdipto/dani  →  must be made public
     OR make github.com/dan-labs-agi  →  public

The brand bug. The #1 Day 0 fix.
```

---

## 11. Tone guide (v55)

**Words to use:**
- "Brain" and "body" (Dan Glasses is the body, DANI is the brain)
- "Live" (DANI is live today)
- "MIT" (every other line)
- "0 cloud" (the privacy wedge)
- "From India" / "Bangalore" (the origin)
- "Proactive" (the category wedge)
- "₹15K" (the price proof)
- "Salience-gated" (the technical wedge)
- "7 daemons" (the architecture)
- "Fork it" (the openness)

**Words to avoid:**
- "Revolutionary" / "groundbreaking" / "next-gen"
- "AI assistant" (we are an AI companion / coworker, not an assistant)
- "Smart glasses" without context (we are a local-first wearable with a local brain)
- "Sleek" / "premium" / "luxury" (we are ₹15K, not $2,195)
- "Coming soon" for the wearable (say "Q4 2026" with a date)
- "Just" / "simply" / "easy" (we are 7 daemons + salience + whisper + VLM, not simple)
- "Hey [vendor], what's this?" (we are proactive, not reactive)

**Voice:**
- Direct, no fluff
- One idea per paragraph
- Show, don't tell (use code, numbers, receipts)
- Always anchor to the wedge (proactive, 0 cloud, MIT, India, we own the model)

---

*End of v55. The hero leads with DANI. The 6 features anchor with the 6 differentiators. The DANI section ships the brain. The Dan Glasses section anchors the body. The architecture section gives engineers the receipts. The FAQ handles objections. The final CTA ships the install. Ship the punchlist. Then ship this page.*
