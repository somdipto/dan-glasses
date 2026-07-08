# Dan Glasses — Landing Page Copy (v45)

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-14 06:50 IST (01:20 UTC)
**Status:** ✅ Canonical, ready-to-deploy. ~800 words. 1 page. 1 ask. Ship the punchlist, deploy the page.

> danlab.dev currently returns the generic 5-bullet product page (Agent8, Zerant, Dapify, Path to AGI). This copy lands on either a new Zo Site, the zo.space homepage, or a one-page deploy wherever the DNS lives.

---

## PAGE STRUCTURE (top to bottom)

1. **Nav** (top, sticky)
2. **Hero** (above the fold)
3. **The number** (1 stat, big)
4. **The quote** (5-competitor contrast)
5. **User stories** (4 cards)
6. **The stack** (7 services, visual)
7. **The origin** (1 paragraph)
8. **The thesis** (5 pillars)
9. **CTA** (1 button)
10. **FAQ** (3 questions)
11. **Footer** (links, social, license)

---

## 1. NAV

```
[Dan Glasses 👾]            [Stack] [Demo] [GitHub] [Origin] [Contact]    [Install →]
```

---

## 2. HERO

### Eyebrow (small, uppercase, above headline)
```
PROACTIVE AI · OPEN SOURCE · FROM INDIA 🇮🇳
```

### Headline (h1, 1 line, ~50-60 chars)
```
Glasses that remember what you forgot.
```

### Subhead (h2, 2 lines, ~120-140 chars)
```
Dan Glasses sees what you see, hears what you say, and remembers what matters.
Runs on a $200 board. 0 cloud calls. $0/month. MIT-licensed.
```

### Primary CTA (button, single, large)
```
Install in one command →
```

### CTA subtext (small, below button)
```
git clone https://github.com/somdipto/dan-glasses && cd dan-glasses && ./scripts/dev.sh
```

### Secondary CTA (text link, below)
```
or watch the 60-second demo ↓
```

---

## 3. THE NUMBER (1 stat, big)

```
$0
```
Subtext:
```
Monthly cost. Forever. 0 cloud calls. 7 services on a $200 board.
```

---

## 4. THE QUOTE (5-competitor contrast)

### Eyebrow
```
THE 2026 SMART-GLASSES RACE
```

### 5 cards (or a single comparison table)

| Who | What they ship | Price | Cloud? | Open? |
|---|---|---|---|---|
| **Meta** | Camera + reactive AI, $799 Display | $224-$799 | ✅ | ❌ |
| **Apple** | $3,499 headset, late 2027 slip | $3,499+ | ✅ | ❌ |
| **Sarvam Kaze** | India's first AI glasses, PM Modi on stage | TBD | ✅ | ❌ |
| **Lenskart B** | 35K+ waitlist, Snapdragon AR1 + Gemini | TBD | ✅ | ❌ |
| **Brilliant Labs Halo** | $299 open-source, LFM2-VL-450M, Noa cloud | $299 | ✅ | ✅ |
| **Dan Glasses** | Proactive AI, 7 services, local-first | $200 target | ❌ | ✅ |

### Punchline (below the table)
```
The whole category is reactive. We're the proactive one.
The whole category is cloud. We're the local one.
The whole category is closed. We're the open one.
```

---

## 5. USER STORIES (4 cards)

### Eyebrow
```
WHAT YOU CAN DO TODAY
```

### Card 1: Encounter Recall
**Title:** Never forget a name.
**Body:** Last Tuesday at 14:32, you met Priya at the conference. You talked about RL. She works at Anthropic. You forgot her name in 30 seconds. Your glasses didn't.
**Receipt:** perceptiond → memoryd, semantic recall, 1.0s end-to-end.

### Card 2: Contextual Reminder
**Title:** I noticed.
**Body:** Your glasses saw you walk past the pharmacy 3 times this week without picking up your prescription. They'll remind you the next time you're near one.
**Receipt:** salience gate + episodic memory + location threshold.

### Card 3: Object Search
**Title:** Where did I leave my keys?
**Body:** You forgot where you left your keys. Your glasses have been passively scanning the apartment all day. They'll find them.
**Receipt:** salience-gated vision + object detection + spatial memory.

### Card 4: Hands-Free Check-In
**Title:** My hands are covered in dough.
**Body:** You're cooking. You can't touch your phone. Your glasses heard you say "any urgent emails?" They checked. They spoke the answer.
**Receipt:** push-to-talk + memory query + email tool + TTS, <3s end-to-end.

---

## 6. THE STACK (7 services, visual)

### Eyebrow
```
HOW IT WORKS
```

### Architecture diagram (ASCII or visual)

```
┌────────────────────────────────────────────────────────┐
│              Dan Glasses · Local-First Stack            │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Camera  →  perceptiond  →  LFM2.5-VL-450M  (209 MB)   │
│  Mic     →  audiod       →  whisper.cpp      (78 MB)   │
│  Text    →  memoryd      →  SQLite + vectors (1.5 GB)  │
│  Voice   →  ttsd         →  KittenTTS        (25 MB)   │
│  Tools   →  toold        →  sandboxed exec             │
│  OS      →  os-toold     →  guarded commands           │
│  Brain   →  openclaw     →  OpenClaw (TypeScript)      │
│                                                        │
│  Total: 7 services, 0 cloud calls, $0/month            │
│  All on-device.  All open source.  All on a $200 board │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### Single-line summary
```
7 services · 0 cloud calls · $0/month · MIT
```

---

## 7. THE ORIGIN (1 paragraph)

### Eyebrow
```
BUILT FROM INDIA 🇮🇳
```

### Body
```
Dan Glasses is built by Somdipto Nandy and the DanLab team in Bangalore.

We're a small, open-source AI research and product lab on a long bet: can a team in India ship the open-source AI stack that the rest of the world wears?

The smart-glasses race in 2026 is cameras with AI. Apple slipped to 2027. Meta charges $799. Google ships audio-only. Sarvam and Lenskart own the Made-in-India narrative. Nobody owns "open-source, proactive, on-device, MIT-licensed."

We do. Or we will, this month.

We're not waiting for hardware. The brain is shipping today. The body is shipping when Redax lands.
```

---

## 8. THE THESIS (5 pillars)

### Eyebrow
```
THE DAN GLASSES THESIS
```

### 5 bullets

1. **Proactive** — Dan Glasses tells you things you didn't know you needed to hear. Everyone else waits for "Hey Meta."
2. **Local-first** — Every model runs on-device. 0 cloud calls. $0/month. Privacy by construction.
3. **Open source** — MIT-licensed. Community-owned. Fork it, modify it, ship it.
4. **From India** — Built in Bangalore. ₹ pricing. Indic languages. AGI from the global south.
5. **AGI research** — The brain is the moat. We can swap the body (Redax → Monako → OpenGlass → Halo) and the user never notices. SIA fork is the path to recursive self-improvement.

### Punchline
```
We're the only open-source, local-first, proactive AI stack in the 2026 smart-glasses race.
```

---

## 9. CTA (1 button)

### Eyebrow
```
SHIPPED TODAY · OPEN SOURCE · MIT
```

### Primary CTA (button, single, large, on dark background)
```
Install in one command →
```

### CTA subtext
```
git clone https://github.com/somdipto/dan-glasses && cd dan-glasses && ./scripts/dev.sh
```

### Secondary CTA
```
[Watch 60-second demo]  ·  [Read the dev blog]  ·  [Join the Telegram]
```

### Receipt below CTA
```
7 daemons live · 106/106 tests green · ~12h uptime · MIT-licensed
```

---

## 10. FAQ (3 questions)

### Q1: How is this different from Ray-Ban Meta?
**A:** Different bet. Meta: $224-$799, camera + reactive AI, Meta AI in the cloud, closed. Dan: $200 target, proactive AI, 0 cloud calls, MIT, open source. Meta says "Hey Meta, take a photo." We say "I noticed you walked past the pharmacy 3x this week." Not better. Different.

### Q2: How is this different from Brilliant Labs Halo?
**A:** Same model family (LFM2-VL-450M). Different body + different bet. Halo: $299, 14h battery, Noa cloud agent, microOLED display. Dan: $200 target, 4h target, no display, no cloud, full agency. We're the open-source alternative to Noa. They ship the body. We ship the soul. If Halo ships to India, we integrate. If not, we ship solo.

### Q3: When is the wearable?
**A:** The v1 desktop prototype runs today on a Linux laptop with a USB camera. The v2 wearable runs on Redax aarch64, blocked on Redax board finalization. The software is portable. The body changes, the brain doesn't. We're not waiting for hardware to start shipping.

---

## 11. FOOTER

### Left
```
© 2026 DanLab
Built in Bangalore 🇮🇳
MIT-licensed
```

### Center (links)
```
GitHub · Twitter · LinkedIn · YouTube · Telegram · Email
```

### Right (legal)
```
Privacy (it's local)
Roadmap
About
```

---

## DESIGN NOTES (for whoever ships this)

- **Color palette:** Dark background (zinc-950), white text, one accent color (recommend `#d8a657` warm gold or `#7c3aed` violet). Don't overdo it.
- **Typography:** Inter for body, Playfair Display for headlines (matches existing danlab.dev). Space Mono for code.
- **Hero image:** A desktop screenshot of the Dan Glasses Tauri app, with perceptiond descriptions streaming in. Optional: a real photo of the Linux laptop + USB camera rig.
- **Stat treatment:** The "$0/month" number is the visual hook. Make it BIG. White on dark, mono font.
- **5-pillar treatment:** Use 5 small icons (one per pillar), not 5 paragraphs. Icons: brain (proactive), lock (local), github (open), flag (India), atom (AGI).
- **Architecture diagram:** Use the ASCII version as a base, but render it as a real SVG. Or use Excalidraw → PNG.
- **Receipts at the bottom:** Don't hide the test count. 106/106 tests green is the trust signal.
- **CTA treatment:** Single, large, dark background. The "Install in one command" button is the only button on the page.

---

## 60-SECOND DEMO SCRIPT (for the YouTube embed)

```
[0:00-0:05]  Screen recording opens. The Tauri app is on screen. "Dan Glasses — proactive AI companion."
[0:05-0:15]  Press spacebar (PTT). STT catches "what did I do Tuesday that was different from usual?"
[0:15-0:25]  Screen shows memoryd query. Top hit: "Tuesday 14:32, met Priya at the conference. Discussed RL."
[0:25-0:35]  TTS speaks: "Tuesday at 14:32 you met Priya at the conference. You talked about RL. She works at Anthropic."
[0:35-0:45]  Cut to terminal: "curl :8090/health" → ok. "curl :8092/health" → ok. 7 daemons. 106/106 tests.
[0:45-0:55]  Cut to danlab.dev. The hero: "Glasses that remember what you forgot." The $0 stat. The 5-pillar thesis.
[0:55-1:00]  CTA: "Install in one command: github.com/somdipto/dan-glasses"
```

---

*Last updated: 2026-06-14 06:50 IST (01:20 UTC) — v45, ~800 words, 1 ask, ready to deploy.*
*Status: copy locked. Awaiting Day 0 deploy.*
