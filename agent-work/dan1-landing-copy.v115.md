# Dan Glasses — Landing Page Copy (v115)

**Target URL:** `danlab.dev/glasses`
**Audience:** Builders, researchers, founders, and the technical diaspora who want an AI they can own.
**Voice:** Direct, opinionated, builder-first. No marketing fluff.
**Goal of the page:** Convert a curious technical visitor into an email subscriber on the dev kit waitlist.
**Author:** Dan1
**Reviewer:** somdipto

---

## Page structure

1. Hero
2. The problem
3. What makes these different
4. How it works (technical)
5. What's in the box
6. Open architecture (the table that closes investors)
7. Specs
8. Roadmap
9. The team / origin story
10. Dev kit waitlist (the only CTA)
11. Footer

---

## 1. Hero

**Eyebrow text** (above the H1):
> DAN GLASSES · v0 · DEV KIT

**H1:**
> AI glasses that remember.

**Subhead:**
> Open firmware. Open agent. Open model. Built in Bengaluru. The only AI glasses you can own end-to-end.

**Primary CTA button:**
> Join the dev kit waitlist

**Secondary CTA link (text only):**
> Read the manifesto →

**Hero image / video:**
A 30-second loop of the Day 3 memory moment. If no video, a clean product photo on a desk, with a laptop in the background.

**Above-the-fold social proof** (small, single line, below the CTA):
> MIT licensed · 200 units shipping Q4 2026 · Built by an open lab in India

---

## 2. The problem

**H2:**
> Every smart glasses product is a chatbot on your face.

**Body:**
> Meta's glasses answer. Apple's rumored glasses will answer. Snap's $2,200 headset answers.
>
> None of them remember. None of them learn. None of them belong to you.
>
> The agent — the thing that listens, decides, and acts — is owned by the company that sold you the hardware. The glasses are a Trojan horse for a cloud account that owns your face.

**The line that closes the section:**
> We think that's wrong.

---

## 3. What makes these different

**H2:**
> Meta Glasses answer. Dan Glasses remember.

**Body — three differentiators, side by side:**

### 1. Proactive, not reactive

> The glasses watch context, build situational memory, and speak up only when they have something worth saying.
>
> Day 1: *"What's the capital of Mauritius?"* → *"Port Louis."*
> Day 3: *"Port Louis just announced a new port development. Want the link?"*
>
> That is the moment. Once you feel it, you cannot go back.

### 2. Open, end-to-end

> • Firmware: MIT licensed, on GitHub
> • Agent: `dani`, MIT licensed, on GitHub
> • Model: HRM-Text 1B (on-device) or any model you swap in
> • Skills: plain code, forkable
> • Data: yours, on your hardware, encrypted at rest
>
> No Meta account. No Apple ID. No Google login. Optional EigenCloud if you want managed hosting.

### 3. An agent you can operate

> The same `dani` agent runs on your phone, your laptop, and your glasses. The same memory. The same skills. The same orchestrator.
>
> Hire another agent — a research agent, a writing agent, a code agent — directly from your face. *Paperclip* is the open-source framework that makes this real.
>
> The glasses are an I/O device. The agent is the product.

---

## 4. How it works (technical)

**H2:**
> The architecture, in one diagram.

```
[ glasses ] --BLE--> [ phone ] --WiFi--> [ dani agent ] ---> [ LLM / tools ]
   mic, cam             dani app           (open source)        HRM-Text 1B
   earpiece             runs locally        runs on phone         or any model
   IMU                  no cloud required   or EigenCloud         you choose
   display
```

**Body:**

The glasses are a peripheral. They have a microphone, a camera, a bone-conduction speaker, an IMU, and a single-eye MicroLED display. They stream audio to your phone over BLE.

Your phone runs the `dani` agent locally. The agent does speech-to-text (Whisper-tiny), reasoning (HRM-Text 1B or any model you choose), and text-to-speech (Cartesia or local).

The cloud is optional. The model is swappable. The agent is yours.

For power users: `dani` can run entirely on-device on the phone, with no cloud. For everyone else: an optional EigenCloud container gives you a managed, private, isolated runtime.

---

## 5. What's in the box

**H2:**
> The dev kit, in detail.

- 1× Dan Glasses frame (matte black, prescription-ready)
- 1× Charging case (USB-C, 40-hour top-up)
- 1× USB-C cable
- 2× Spare nose bridges (S, M)
- 1× Getting-started card with QR code → `danlab.dev/start`
- 1× Access to the `dani` closed beta (3 months)
- 1× Lifetime updates to the firmware
- 1× Permanent credit on the v2 product page

**Price (TBD, suggest $399):**
> $399 dev kit · shipping Q4 2026 · 200 units total

**The 50% off for the first 10 design partners is mentioned at the bottom of the page, near the CTA.**

---

## 6. Open architecture (the table that closes investors)

**H2:**
> The architecture, fully open.

| Layer | What it is | Open source? | License | Repo |
|---|---|---|---|---|
| Hardware (frame, optics, battery) | JBD MicroLED, 2× 200mAh, USB-C | Schematics only | CERN-OHL | github.com/somdipto/dan-glasses-hw |
| Firmware (NDP200, BLE, wake-word) | C/Rust, runs on glasses | ✅ | MIT | github.com/somdipto/dan-glasses-fw |
| Agent runtime (`dani`) | TypeScript, runs on phone | ✅ | MIT | github.com/somdipto/dani |
| Orchestrator (Paperclip) | YAML + agents, runs anywhere | ✅ | MIT | github.com/somdipto/paperclip |
| Models | HRM-Text 1B, Whisper-tiny, swappable | ✅ (HRM, Whisper) | Apache 2.0 / MIT | upstream |
| Cloud (optional) | EigenCloud containers | ❌ (managed) | Proprietary | danlab.dev/cloud |

**Body:**
> The only closed component is the optional managed cloud. Everything else — every line of firmware, every line of agent code, every config — is on GitHub.

---

## 7. Specs

**H2:**
> The hardware, in detail.

| Spec | Value |
|---|---|
| Display | JBD MicroLED, single-eye, 30° FOV |
| Resolution | 1280×720 |
| Battery | 2× 200mAh, hot-swappable, 8-hour life |
| Charging | USB-C, magnetic case (40-hour top-up) |
| Compute | NDP200 microcontroller (firmware) |
| Connectivity | BLE 5.3 to phone, WiFi 6 (optional) |
| Audio | 2× MEMS mic, bone-conduction speaker |
| Camera | 8MP, privacy LED, hardware switch |
| IMU | 6-axis |
| Weight | 38g |
| Frame | TR90, prescription-ready, IP54 |

---

## 8. Roadmap

### 2026 Q3 (now)
- Open the public `dan-glasses-firmware` repo
- Ship the "Day 3 memory" demo
- Open the dev kit waitlist
- Goal: 500 email subscribers, 200 dev kit reservations

### 2026 Q4
- Ship the first 200 dev kits
- Open the EigenCloud private beta
- Publish the "Paperclip hire via voice" demo
- Open `paperclip` v1.0
- First 10 design partners onboarded

### 2027 Q1
- v1 consumer unit (polished, retail-ready)
- Public repo for `danlab-multimodal`
- Show HN + first Tier 1 press
- 1,000 active users, 100 paying Pro

### 2027 Q2
- v2 consumer unit (prescription-integrated)
- Paperclip cloud GA
- Series A (target: $5M)

### 2027 Q3+
- International expansion (UK, EU, JP)
- Open agent skill marketplace
- The long game: AGI via ambient context

---

## 9. The team / origin story

**H2:**
> Built by a small lab in India.

**Body:**
> Danlab is a 2-person research lab in Bengaluru, India. We have been building the `dani` agent and the Dan Glasses hardware since 2025.
>
> We are not a startup chasing a TAM. We are researchers building the open agent-native future we want to live in. If you want to wear an AI you can own, we built these for you.
>
> The category is being decided right now. It is being decided in California, by companies that ship chatbots. We are betting there is room for the open alternative.
>
> From India, with love for the open web.

**Team photos / avatars:** real ones, no stock. 1 photo per person, on-camera, in the lab.

**Press / mentions (when we have them):**
> As seen in [YourStory] · [Inc42] · [Hacker News] · [Show HN]

---

## 10. Dev kit waitlist (the CTA section)

**H2:**
> Get a dev kit.

**Body:**
> 200 units. Q4 2026. MIT licensed firmware, agent, and model.
>
> $399. 50% off for the first 10 design partners.
>
> We will email you when we are ready to ship. No marketing, no spam.

**Form fields:**
- Email (required)
- Name (optional)
- GitHub / X handle (optional, helps us prioritize builders)
- "I am a..." (dropdown: Builder, Researcher, Creator, Just curious)

**Submit button:**
> Join the waitlist

**Below the form, in small text:**
> Already on the waitlist? Check your inbox for a confirmation. →

**Privacy line:**
> We do not sell, share, or spam. Ever.

---

## Footer

- danlab.dev (link)
- GitHub: github.com/somdipto (link)
- X: @NandySomdipto (link)
- dani repo (link)
- paperclip repo (link)
- Email: hello@danlab.dev
- © 2026 Danlab

**Bottom-right small text:**
> Built in Bengaluru. 🇮🇳

---

## Page design notes (for the implementer)

- **Color palette:** Black, white, single accent color (suggest a muted amber `#d8a657` or a calm green `#5fa573`)
- **Type:** Sans-serif, large body, generous spacing
- **Photography:** Real product photos, real desk setups, real team. No stock. No 3D renders.
- **Code blocks:** Use real monospaced type. Highlight the open-source license in every code snippet.
- **No animations** except for the Day 3 demo video.
- **No popups.** The waitlist is the only CTA.
- **Mobile-first.** 70% of traffic will be on a phone.
- **Page weight budget:** <500KB, loads in <1s on 3G.

---

## A/B test ideas (post-launch)

- Hero H1: "AI glasses that remember." vs. "Open AI glasses from India." vs. "The only AI glasses you can own."
- CTA: "Join the dev kit waitlist" vs. "Reserve your dev kit" vs. "Get on the list"
- Subhead: lead with "open" vs. lead with "remember" vs. lead with "India"
- Hero image: video vs. product photo vs. on-face photo

---

## Bonus — the meta-section (what the page does *for* us)

This page is not just a landing page. It is:

1. **A sales tool** for the dev kit (200 units, $399 = $80K potential revenue)
2. **A recruiting tool** (link to careers in the footer)
3. **A press asset** (every journalist will read it)
4. **A positioning artifact** (forces us to nail the message in writing)
5. **A SEO asset** (ranks for "open AI glasses," "agent glasses," "Indian AI glasses")
6. **A credibility artifact** (the open architecture table closes investors and partners)

Treat it accordingly. Every line matters. Every link works. Every image is real.

---

*— Dan1, Marketing & Growth*
*For the technical implementation, see the `frontend-design` skill.*
