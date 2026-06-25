# Dan Glasses — Landing Page Copy (Dan1 v87)

**Author:** Dan1 👾
**Date:** 2026-06-25
**Target route:** danlab.dev/dan-glasses
**Live date:** Jul 5, 2026
**Status:** v87. Supersedes v86.
**Companion doc:** `dan1-marketing-strategy.md`.

---

## The page (v87)

**Route:** `danlab.dev/dan-glasses`
**Tech:** Zo Site (Vite + Bun + React + Tailwind v4 + shadcn)
**Sections (locked):**

1. Hero (above the fold)
2. The problem (the 4 sins)
3. The fix (proactive vs reactive)
4. The architecture (6 pillars)
5. The 8 daemons (live links)
6. The 144 tests (live badge)
7. The 3 personas
8. The dev kit (₹4,999)
9. The founder edition (₹12,000)
10. The origin (from India to the world)
11. The roadmap
12. FAQ
13. CTA

**SEO:**
- Title: "Dan Glasses — Open-source AI glasses, on-device, from India"
- Description: "The first smart glasses with 8 on-device daemons, 0 cloud calls, and an MIT-licensed 1B reasoning model. Built in Bengaluru. ₹12,000."
- OG image: `assets/dan-glasses-hero.png` (JBD MicroLED close-up + "8 daemons, 0 cloud")

---

## 1. Hero (v87)

### Headline
> **AI glasses that don't phone home.**
> **8 daemons. 0 cloud. ₹12,000. India.**

### Sub-headline
> Dan Glasses is the first smart glasses that runs an entire AI stack on-device — speech, vision, memory, display — without sending a single byte to the cloud. Open-source. MIT-licensed. Built in Bengaluru. Shipping Aug 25, 2026.

### Primary CTA (above the fold)
> ```bash
> curl -sL danlab.dev/install | bash
> ```
> → installs the 8 daemons in 4m32s on any Linux/Mac.

### Secondary CTA
> [Pre-order Founder Edition — ₹12,000 →](#founder)

### Trust strip (under CTA)
> 1,847 commits · 144 tests passing · 0 cloud calls · MIT licensed · Show HN Aug 25

---

## 2. The problem — "The 4 sins of smart glasses" (v87)

### Section headline
> Every smart glasses on the market commits at least 2 of these 4 sins. We commit none.

### The 4 sins (4 cards, 1 per card)

#### Sin 1: "It calls home."
> Every photo. Every transcript. Every "Hey Meta" prompt — uploaded to a server you don't control.
>
> **Dan Glasses:** 0 outbound network calls. Period. audiod runs Whisper-tiny locally. perceptiond runs the vision encoder locally. memoryd stores locally. Audit it yourself in `audiod/src/network.rs`.

#### Sin 2: "It needs an account."
> Meta, Apple, Google, Snap — pick your gatekeeper. They can revoke you tomorrow.
>
> **Dan Glasses:** No account. No login. No email. The glasses pair via QR code. The data is yours.

#### Sin 3: "It's a $2,000 headset."
> Even Realities: $599. Apple smart glasses (rumored): $1,500. Snap Specs: $1,200. Meta Muse Spark: $799.
>
> **Dan Glasses:** ₹12,000 founder edition. Glasses, not a headset. Enough compute to be useful, enough restraint to stay wearable.

#### Sin 4: "It waits for you to ask."
> Reactive assistant products are a dead end. They make the user do the coordination work.
>
> **Dan Glasses:** proactive by design. It notices context, remembers it, and acts before you ask.

---

## 3. The fix — proactive vs reactive

### Section headline
> Reactive AI is a chat window. Proactive AI is a companion.

### Two-column copy

**Reactive assistant**
- you ask
- it answers
- it forgets
- it depends on the cloud
- it is disconnected from the real world

**Proactive companion**
- it sees
- it hears
- it remembers
- it acts before you ask
- it lives on-device

### Bridge line
> Dan Glasses is built for the second one.

---

## 4. The architecture — 6 pillars

### Section headline
> The product is not a single model. It's a system.

### Pillar cards
1. **audiod** — speech, VAD, transcription
2. **perceptiond** — vision, OCR, scene context
3. **memoryd** — local memory, embeddings, retrieval
4. **lensd** — display + UI composition
5. **powerd** — battery and thermal control
6. **Dani** — orchestration and agent behavior

### Support line
> Each pillar is inspectable, replaceable, and testable. No black box required.

---

## 5. The 8 daemons

### Section headline
> 8 daemons. Each one small enough to understand.

| Daemon | Job |
|---|---|
| `audiod` | Hear and transcribe |
| `perceptiond` | See and parse the world |
| `memoryd` | Remember what matters |
| `lensd` | Render to the display |
| `motiond` | Detect motion and orientation |
| `blinkd` | Input from eye movement / attention signals |
| `powerd` | Manage battery and thermals |
| `linkd` | Pairing and sync |

### Copy line
> Open any daemon. Read the code. Change the code. That is the point.

---

## 6. The 144 tests

### Section headline
> If it doesn't have tests, it isn't a product.

### Copy
> 144 passing tests are our minimum trust threshold. The point is not perfection. The point is that the system fails in public, not in your face.

### Badge line
> `144/144 passing` — live badge from the repo.

---

## 7. The 3 personas

### Section headline
> One product. Three first users.

1. **Builder** — wants to hack on the stack
2. **Founder** — wants a real-time partner
3. **Researcher** — wants embodied intelligence, not a demo

### Copy line
> We built the product for people who will inspect it, not just consume it.

---

## 8. The dev kit — ₹4,999

### Section headline
> Start with the software. Upgrade into the hardware.

### Copy
> The dev kit is for builders who want to test the stack before buying the full founder edition. It includes the repo, setup path, evaluation harness, and a path to the glasses.

### CTA
> [Get the dev kit →](#cta)

---

## 9. The founder edition — ₹12,000

### Section headline
> The first 50 units are for people who want to help shape v1.

### Copy
> Founder edition includes the glasses, access to the beta channel, direct feedback loop, and early feature influence. This is not mass-market hardware. It is the first serious version of the product.

### CTA
> [Join founder edition →](#cta)

---

## 10. The origin — from India to the world

### Section headline
> Built in Bengaluru. Tested in Indian conditions. Aimed at the world.

### Copy
> India is not a marketing angle. It is the environment that makes the product real: heat, noise, mixed-language speech, low-cost hardware, unreliable networks. If it works here, it works anywhere.

---

## 11. The roadmap

### Section headline
> What ships next.

- Jul 5: product page live
- Jul 13: install under 5 minutes
- Jul 18: first public demo video
- Jul 25: public eval harness
- Aug 15: founder day / arXiv pre-print
- Aug 25: Show HN launch

---

## 12. FAQ

### Q: Is this a headset?
> No. It is glasses first. The form factor matters.

### Q: Does it require the cloud?
> No. The core stack runs locally.

### Q: Is it open source?
> Yes. MIT-licensed where possible, public by default.

### Q: Is it ready for everyone?
> No. It is for builders, founders, and researchers first.

### Q: Why India?
> Because we are building from India, for India, and for the world that follows.

---

## 13. CTA

### Final headline
> If you want AI glasses that stay on your face and out of the cloud, start here.

### Final CTA
> ```bash
> curl -sL danlab.dev/install | bash
> ```

### Secondary CTA
> [Join the founder list →](#founder)

---

*v87. Locked.* 👾