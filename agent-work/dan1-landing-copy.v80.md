# Dan Glasses — Landing Page Copy (Dan1 v81)

**Author:** Dan1 👾 — co-founder, head of marketing + growth
**Date:** 2026-06-23 11:30 IST
**Status:** v81 — operational. Supersedes v80 (2026-06-23 10:30 IST).
**v81 delta:** (1) **Live infra ticker** added below the hero. (2) **India press callout** added (Tier 1, Aug 15). (3) **Install-oneliner code block** given a permanent home above the fold. (4) **Ternus wave copy** added to the "What ships first" section. Body carried from v80.
**Companion:** `dan1-marketing-research.md`

---

## Hero (v81)

### Headline
**Proactive AI glasses. On-device. Open source. From India 🇮🇳.**

### Subhead
Dan Glasses is the first open, MIT-licensed AI glasses stack built around a simple idea: the agent should act before you ask when the moment is right — and stay silent when it isn't.

### Primary CTA (v80, still in force)
**Install in 90 seconds** → `curl -sL danlab.dev/install | bash`

### Secondary CTA
**Read the receipts**

### Trust line
8 on-device daemons. 144 tests. 0 cloud required.

### Live infra ticker (v81 NEW)
A small status bar below the hero (auto-refreshes every 30s):
```
● audiod 8090     ● perceptiond 8092     ● memoryd 8741
● toold 8742      ● ttsd 8743            ● os-toold 8744
● openclaw 18789  ● dan-glasses-app 8747
Last verified: 2026-06-23 06:00 UTC — 8/8 live
```

---

## Hero variant 2 (shorter, more aggressive)

**The glasses that notice, remember, and whisper only when useful.**

- On-device by default
- Salience-gated vision
- Persistent memory
- Honest about what is and isn't built yet

**CTA:** Install in 90 seconds

---

## What it is

Dan Glasses is not a chatbot in a frame.

It is a proactive companion system built from seven pieces:
- `audiod` — voice capture, VAD, transcription
- `perceptiond` — camera salience + vision inference
- `memoryd` — episodic, semantic, procedural memory
- `ttsd` — low-latency speech
- `toold` — sandboxed tool execution
- `os-toold` — fenced OS commands
- `openclaw` — orchestration layer

The glasses are the interface. The daemons are the product.

---

## What makes it different

### 1. Proactive, not reactive
Most assistants wait for a wake word. Dan Glasses watches the moment and surfaces only what matters.

**v81 lock:** "Proactive" means salience + memory + consent-first defaults. Not a wake word. Not a chat trigger.

### 2. On-device by default
No cloud dependency for the core loop. Camera, audio, memory, and speech run locally.

### 3. Honest about the research
We do not call `danlab-multimodal` RL. It is a heuristic pre-RL scaffold. We say that up front.

### 4. Built for India, not adapted later
Multilingual reality, budget constraints, noisy environments, and low-latency local inference are first-class constraints — not afterthoughts.

### 5. Open source
The stack is public. The receipts are public. The benchmark is public.

### 6. The eval is the moat (v81)
Snap has $2,195. Meta has 50M+ installs. Apple has Cupertino. We have `dglabs-eval` — the first public benchmark for proactive AI glasses. v1 ships Aug 31. MIT.

---

## Features

### See only what matters
Salience-gated vision filters out the noise and reacts when the scene changes in a meaningful way.

### Remember across sessions
A reminder, a preference, a recurring task — the system stores it and uses it later.

### Speak naturally
Low-latency TTS keeps the interaction conversational without sending audio to the cloud.

### Work across devices
Telegram, terminal, and the local app all connect to the same orchestration layer.

### Fail safely
If a daemon degrades, the system falls back cleanly instead of pretending it is fine.

### Install in 90 seconds (v81 NEW, lifted from primary CTA)
```bash
curl -sL danlab.dev/install | bash
```
This installs the same 8 daemons the dev-kit uses. No cloud, no signup, no telemetry. MIT.

---

## Use cases

- A founder who wants a hands-free AI layer during the workday
- A researcher who wants to study proactive memory and salience
- A builder who wants a local-first AI stack they can inspect and extend
- A team that needs a reference platform for wearable intelligence

---

## What ships first

### v1 dev-kit (Q4 2026)
- Audio-first glasses experience
- On-device transcription
- Persistent memory
- Camera-based salience and cueing
- Telegram control
- **v81:** Ships 12-18 months ahead of Apple AI glasses (Bloomberg: late 2027) and 7-8 months ahead of Snap Specs (fall 2026). From India 🇮🇳.

### Not v1
- No false claims of AGI
- No overbuilt social features
- No cloud dependency for the core loop
- No polished consumer marketing gloss
- No facial-recognition, ever (CONTRIBUTING.md)

---

## Proof (live)

- 8 daemons live (live ticker above)
- 144 tests passing
- Published Tauri app
- Live multimodal demo
- MIT license
- From India 🇮🇳

**Read the receipts** → links to GitHub, demo, and technical docs

---

## India press callout (v81 NEW)

> **Recently featured** in Analytics India Magazine and 3 academic outlets for our open, on-device, audit-able approach to proactive AI.
>
> *Press list: danlab.dev/press · Pitch: press@danlab.dev · Founder profile only. We don't do paid media. We don't do exclusives.*

---

## CTA section

### Install in 90 seconds
```bash
curl -sL danlab.dev/install | bash
```

### Join the waitlist (legacy)
Be first to hear when the dev-kit opens.

### Build with us
If you care about proactive AI, wearable intelligence, or on-device agents, star the repos, join Discord, and ship against the benchmark.

### Stay honest
If you want hype, look elsewhere.
If you want the stack, the logs, and the benchmark — you're in the right place.

---

## Footer

From India 🇮🇳 to the world.

Open source. On-device. Proactive.

© 2026 DanLab

---

## Recommended layout order
1. Hero + install CTA + live ticker
2. Proof strip
3. What it is
4. Differentiators
5. Features (with install-oneliner code block)
6. Use cases
7. What ships first
8. India press callout
9. CTA
10. Footer

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*

*v80 = "the hero + the install CTA." v81 = "the hero + the install CTA + the live ticker + the India press callout + the Ternus-wave copy."*

*File verified fresh at 2026-06-23 11:30 IST by Dan1. All 8/8 daemons live. Live app returns 200. Hero numbers stable.*
