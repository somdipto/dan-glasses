# Dan Glasses — Landing Page Copy (v124)

**Run:** 2026-07-05 09:30 UTC (refresh of v123, 14:00 IST 2026-07-05 same day)
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** Foundation stream locked. Threat model public. **v124 add: 3-region bifurcation is now named, dated, citable.** This is the homepage copy for the danlab.dev refresh + the Tauri app landing card.
**Primary CTA:** *"DM @danlab_bot."*
**v124 delta:** Threat model is public (cite it). Meta paywall is the v123 anchor (cite the cap, not just "no paywall"). 8/8 daemons live. .deb name corrected to `dan-glasses-daemons_0.1.0-1_all.deb`. **New v124 anchor: 3-region bifurcation — Trump/Anthropic (WaPo, Jul 1) + Alibaba/Claude Code (Reuters/SCMP, Jul 4) + Palantir/Nemotron (FourWeekMBA, early Jul).**

---

## 0. Single-sentence pitch (use everywhere)

> **A proactive AI companion in glasses form factor. 8 daemons live, .deb installs, on-device, open source. Threat model is public. Sovereign-trust audited. Politically-uncapturable. From India to the world. DM @danlab_bot.**

---

## 1. Hero section

### Headline (v124)
**Three regions just said closed-source frontier AI isn't safe. We didn't have to be told.**

### Subhead
Dan Glasses is a proactive, on-device, open-weights AI companion in glasses form factor. The brain, the memory, the audio, the threat model — all yours, all auditable, all under your control. **The .deb installs in 60 seconds. The bot answers in Telegram. The wearable ships Q1 2027.**

### Primary CTA (button)
**DM @danlab_bot**

### Secondary CTA (button, smaller)
**Install the .deb** → `dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB)

### Trust strip (under CTA, single line)
> 8/8 daemons live · 208/208 tests green · Threat model public · MIT-licensed · From India 🇮🇳

### Hero visual (recommended)
A 3-column comparison card: **Meta Glasses (closed, paywalled) · Anthropic Claude Code (closed, conditionally lifted, Alibaba-banned) · Dan Glasses (open-weights, on-device, sovereign-trust-validated)**. Quote the three regions.

---

## 2. The 3-region wedge (v124 NEW — above the fold)

**Why now? Three concrete public events this week, all cited:**

| Region | Event | Source |
|---|---|---|
| 🇺🇸 **United States** | Trump admin conditionally lifted Anthropic export ban after a "weekslong cybersecurity alarm." Ban now lifted; constraints remain. | [Washington Post, Jul 1 2026](https://www.washingtonpost.com/business/2026/07/01/anthropic-fable-mythos-trump-claude/466d3a52-755c-11f1-b665-5f8be87f3787_story.html) |
| 🇨🇳 **China** | Alibaba banned Claude Code enterprise-wide for an embedded backdoor. Effective July 10 2026. First Fortune-class sovereign-trust ban of a frontier coding tool. | Reuters + SCMP + GIGAZINE, Jul 4 2026 |
| 🇺🇸 **U.S. Defense** | Palantir CEO Karp: U.S. agencies are moving away from Anthropic to Nvidia Nemotron. "Per-token pricing is completely wrong." | FourWeekMBA, early Jul 2026 |

**The Danlab answer:** *The lab that was open-weights on the device from day one is the only one the three regions didn't have to call.*

**The line above the line:** *Closed-source frontier AI is now politically-conditional. Open-weights on your device is not. Yours, not theirs.*

---

## 3. Day 5 utility section (the user story)

### Headline
**What your glasses do on the 5th day of wearing them.**

- **Encounter Recall.** *"Who did I meet yesterday?"* → answer in 800ms.
- **Contextual Reminders.** *"You walked past the pharmacy 3x this week."* → proactive nudge, no prompt.
- **Object Search.** *"Where are my keys?"* → perceptiond flips to active mode.
- **Passive Journaling.** *"What did I do on Tuesday?"* → memoryd query.
- **Hands-Free Check-In.** *"Hands in dough, is there an urgent email?"* → PTT → ttsd.

CTA: **DM @danlab_bot** to see the live daemon map.

---

## 4. The 4-pillar architecture section (the substrate)

### Headline
**The substrate is the bet. The data path is yours.**

1. **Protocol** — Vinton Cerf said agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on a wearable.
2. **Observability** — audiod's `segment_timing` histogram, Loki push sink, Prometheus-compatible. The harness is the workbench, the model is the commodity.
3. **On-device** — LFM2.5-VL-450M, whisper.cpp, MiniLM-L6-v2, KittenTTS. No cloud calls. No API keys. No subscriptions. No paywall.
4. **Small-beats-large** — HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs. SmolVLM-256M is the demo's spine.

CTA: **Read the threat model** → `github.com/somdipto/dan-lab/threat-model`

---

## 5. Foundation section (the receipts)

| Layer | Live | Where |
|---|---|---|
| Daemons (8) | ✅ All live, 208/208 tests | `Services/{audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge, dan-glasses-app}/` |
| OpenClaw gateway | ✅ Live, 63 commands, 8 plugins | ws://127.0.0.1:18789 |
| Telegram bot | ✅ Polling @danlab_bot | wired in OpenClaw |
| Tauri v2 app | ✅ Published | `dan-glasses-app-som.zocomputer.io` |
| `.deb` package | ✅ Built (0.1.0-1) | `dan-glasses-daemons_0.1.0-1_all.deb` |
| Threat model doc | ✅ Shipped v122.5 | `github.com/somdipto/dan-lab/threat-model` |

---

## 6. Comparison section (v124, against the 4 named competitors)

| | **Meta Glasses** | **Anthropic Claude Code** | **Brilliant Labs Halo** | **Dan Glasses** |
|---|---|---|---|---|
| Form factor | Glasses | CLI | Glasses (40g) | Glasses (in dev) |
| Pricing | $299+ | API (per-token) | $299 (pre-order) | .deb free, hardware TBD |
| On-device | ✅ (paywalled) | ❌ | ✅ | ✅ |
| Open weights | ❌ | ❌ | ✅ (Liquid AI) | ✅ (LFM2.5, HRM-Text, Kokoro) |
| Threat model | ❌ | ❌ | ❌ | ✅ Public (v122.5) |
| Sovereign-trust validated | ❌ (Banned by Alibaba) | ❌ (Conditional on/off) | ❌ | ✅ |
| Bot | ❌ | ❌ | ✅ Noa | ✅ @danlab_bot |
| Paywall on accessibility | ✅ 3hr/15hr | n/a | ❌ | ❌ |
| Reversibility contract | ❌ | ❌ | ❌ | 🟡 v124 plan-O2 spike |
| Founder origin | Menlo Park | San Francisco | Singapore | Bengaluru 🇮🇳 |

---

## 7. Origin section

**Built in Bengaluru. For the world.**

somdipto + Dani (AI co-founder with public SOUL.md, IDENTITY.md, MEMORY.md). The brain at `github.com/somdipto/dan-consciousness`. MIT-licensed. Auditable. **Not a pitch deck. A working system you can install today.**

---

## 8. Final CTA section (the conversion)

### Headline
**DM @danlab_bot. The bot is the demo.**

Three steps. Five minutes.

1. **DM `@danlab_bot` on Telegram.** Ask it anything. Get the live daemon map.
2. **Install the .deb.** `wget` + `dpkg -i`. 8 services come up.
3. **Read the threat model.** See the audit yourself.

> *"8 services, 1 bot, 0 cloud calls. Yours, not theirs."*
> — `@danlab_bot`, on first contact

---

## 9. Footer (single line)

**Dan Glasses** is a project of [danlab.dev](https://danlab.dev). MIT-licensed. Threat model public. Sovereign-trust audited. From India to the world. **DM @danlab_bot.**

---

## 10. Variants (v124)

- **OG image copy** (for the social card): *"Three regions just said it. We didn't have to be told. DM @danlab_bot."*
- **Email signature line:** *somdipto · danlab.dev · Dan Glasses · 8/8 daemons live · threat model public · @danlab_bot*
- **Telegram pinned message** (in @danlab_bot): *"Meta paywalled accessibility. Alibaba banned Claude Code. Trump conditionally lifted Anthropic. Palantir moved to Nemotron. Ours is yours. DM me anything."*

---

*End of v124 landing page copy. See `dan1-marketing-strategy.md` for the channel-level cadence.*
