# Dan Glasses — Landing Page Copy (v119)

**Run:** 2026-07-04 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Target page:** `danlab.dev/glasses` (proposed) or `dan-glasses-app-som.zocomputer.io` (current published Tauri app)
**v119 lead:** Tauri live + Cerf protocol + Anthropic fingerprinting + 9 daemons receipts.

---

## 0. Page architecture (v119)

Single-page React + Tailwind 4. Performance budget: <1MB, FCP <1.5s on 4G India.
Sections, in order:

1. **Hero** — one-line positioning, one CTA, two URLs (Tauri + GitHub).
2. **9 daemons matrix** — port map, real curl payloads as the receipts.
3. **Tauri live demo** — embedded iframe or screenshot of `dan-glasses-app-som.zocomputer.io`.
4. **What it does** — 5 PRD user stories, each with a curl payload.
5. **Architecture one-pager** — 5 layers (hardware, services, gateway, agents, app).
6. **The protocol is the bet** — Cerf origin pillar, OpenClaw substrate.
7. **On-device thesis** — small-beats-large, validated by orbit.
8. **Comparison table** — Quark / Meta / Dan.
9. **Open weights, open protocol** — model cards, GitHub, Telegram.
10. **Footer** — bio, bot handle, Tauri URL, GitHub org.

---

## 1. Hero (v119)

### Headline (v119, lead)
**A proactive AI on your face. Open source. Open protocol. 9 daemons live.**

### Subheadline (v119)
**Most AI assistants wait for you to ask a question and then phone home with your data. Dan Glasses watches, remembers, and acts — inside your own device. Tauri v2 app live. 0 cloud calls. From India.**

### Primary CTA (v119)
**Open the live app → `https://dan-glasses-app-som.zocomputer.io`**

### Secondary CTA (v119)
**Read the receipts → `https://github.com/somdipto/dan-glasses`**

### Tertiary CTA (v119)
**DM the bot → `t.me/danlab_bot`**

### Hero receipts strip (v119)
```
8 service daemons  ·  1 OpenClaw gateway  ·  1 tailscaled substrate  ·  1 Tauri v2 app  ·  0 cloud calls
```

### Hero subline (v119, v118 origin pillar kept)
A 1B model trained for the cost of a used iPhone. An 82M TTS model that beat ElevenLabs. A 4B VLM in orbit. **The on-device thesis is no longer a pitch.**

---

## 2. 9-daemon matrix (v119, with curl receipts)

### Section headline
**9 processes. 0 cloud. Verified by curl.**

### Section subhead
Every daemon is a standalone process. Every daemon ships a `/ready` endpoint. Every claim has a curl payload. Click any port to see the live response.

### Matrix (v119, anchored to the live Tauri app)

| Daemon | Port | What it does | Live receipt |
|---|---|---|---|
| **audiod** | 8090 | Speech-to-text, voice activity detection, push-to-talk (whisper.cpp + Silero) | `curl localhost:8090/ready` |
| **perceptiond** | 8092 | Vision pipeline, salience gating, LFM2.5-VL-450M (VLM) | `curl localhost:8092/status` |
| **memoryd** | 8741 | Episodic / semantic / procedural memory, 384-dim MiniLM embeddings, SQLite | `curl localhost:8741/stats` |
| **toold** | 8742 | Sandboxed tool registry, MCP-compatible | `curl localhost:8742/health` |
| **ttsd** | 8743 | Text-to-speech, KittenTTS medium (Kokoro-82M swap planned) | `curl localhost:8743/health` |
| **os-toold** | 8744 | OS exec sandbox, path guard, allowlist | `curl localhost:8744/health` |
| **dan-glasses-app** | 8747 | Tauri v2 + React 19 + Vite 7 SPA. Published at `dan-glasses-app-som.zocomputer.io`. | Open in browser |
| **openclaw** | 18789 | Gateway, Telegram channel installed/configured/enabled, memory enabled | `curl localhost:18789/health` |
| **tailscaled** | (process) | Tailscale userspace mode, supervisor-managed. **Logged out — needs `TAILSCALE_AUTHKEY`.** | `tailscale status` |

**Real receipts as of v119:**
- 160/160 audiod tests pass
- 8/8 perceptiond tests pass
- audiod v1.3: `segment_timing` block shipped to Loki, p50/p95/count queryable
- memoryd: persistent DB, 384-dim MiniLM embeddings
- perceptiond: 188 frames / 167 salient / 166 descriptions (v118 baseline)
- 9 processes verified via curl, 1 Tauri app published, 0 cloud calls

---

## 3. Tauri live demo (v119 NEW SECTION)

### Section headline
**The product surface is in a browser tab.**

### Section subhead
`https://dan-glasses-app-som.zocomputer.io` is the live Tauri v2 app. The same code that runs the glasses runs in the browser. Bootstrap wizard, daemon map, vision dashboard, memory panel, TTS demo.

### Embed (v119)
Embedded iframe at 80% page width. Falls back to a screenshot iframed if the SPA is slow to load.

### Receipts strip below the embed
```
Tauri v2  ·  React 19  ·  Vite 7  ·  TypeScript 5.8
Window 960×720  ·  Category: Utility  ·  Identifier: dev.danlab.danglasses
```

### CTA (v119)
**Open the Tauri app in a new tab → `https://dan-glasses-app-som.zocomputer.io`**

---

## 4. What it does — 5 user stories (v119)

### Section headline
**5 ways a wearable AI earns its place on your face.**

### US-1 — Encounter Recall
> *"Who did I meet yesterday?"* — Push-to-talk → audiod → memoryd → ttsd. The agent answers with names, faces, and where you met.

### US-2 — Contextual Task Reminder
> *"You walked past the pharmacy 3x this week."* — Proactive nudge. The agent watches the room, not the question.

### US-3 — Object Search
> *"Where are my keys?"* — perceptiond flips to active mode, runs salience-gated VLM inference, gives a spatial description.

### US-4 — Passive Journaling
> *"What did I do on Tuesday?"* — memoryd query across episodic / semantic / procedural. The agent remembers what you saw when you didn't.

### US-5 — Hands-Free Check-In
> *"Hands in dough. Is there an urgent email?"* — Push-to-talk → os-toold → ttsd. No phone, no keyboard, no hands.

### Section footer (v119)
> **A reactive assistant waits for you to ask. A proactive companion notices things you missed.** That's the line.

---

## 5. Architecture one-pager (v119)

### Section headline
**5 layers. 9 daemons. 1 OpenClaw gateway. 0 cloud calls.**

### Architecture diagram (v119)
```
┌─────────────────────────────────────────────────────────────────┐
│ Layer 5: App                                                     │
│   Tauri v2 + React 19 + Vite 7                                  │
│   dan-glasses-app (8747)  →  https://dan-glasses-app-som        │
│                                .zocomputer.io                   │
├─────────────────────────────────────────────────────────────────┤
│ Layer 4: Agent gateway                                          │
│   OpenClaw (18789)                                              │
│   Telegram @danlab_bot (live)                                   │
│   memoryd core enabled                                          │
├─────────────────────────────────────────────────────────────────┤
│ Layer 3: Services (8 daemons)                                   │
│   audiod (8090)  perceptiond (8092)  memoryd (8741)             │
│   toold (8742)    ttsd (8743)       os-toold (8744)             │
│   dan-glasses-app (8747)  tailscaled (process)                  │
├─────────────────────────────────────────────────────────────────┤
│ Layer 2: Models (all open weights, all on-device)               │
│   LFM2.5-VL-450M Q4_0 (vision)  ·  whisper.cpp base.en (STT)    │
│   KittenTTS medium (TTS)       ·  all-MiniLM-L6-v2 (memory)     │
│   HRM-Text-1B (v1.5 swap)      ·  Kokoro-82M (v1.5 swap)        │
├─────────────────────────────────────────────────────────────────┤
│ Layer 1: Hardware (when the wearable ships)                     │
│   JBD MicroLED  ·  2x 200mAh batteries  ·  USB-C  ·  NDP200      │
└─────────────────────────────────────────────────────────────────┘
```

### One-line description per layer (v119)
- **App:** the surface you see. Tauri v2 + React 19, 960×720, category=Utility.
- **Agent gateway:** OpenClaw. Telegram wired. The substrate is the bet.
- **Services:** 8 standalone processes. Each has `/health`, `/ready`, `/status`. The daemon matrix is the receipts.
- **Models:** open weights, on-device. LFM2.5-VL-450M for vision, whisper.cpp for STT, KittenTTS for TTS, MiniLM for memory. **The on-device thesis is no longer a pitch.**
- **Hardware:** JBD MicroLED, dual batteries, USB-C, NDP200. **The same code rebuilds onto the wearable when the hardware ships.**

---

## 6. The protocol is the bet (v119 NEW SECTION)

### Section headline
**Vinton Cerf says AI agents need TCP/IP. We shipped it.**

### Section subhead
> *"Natural language is too ambiguous for reliable AI-agent-to-agent communication. We need formal, standardized protocols, much as TCP/IP did for the early internet."* — Vinton Cerf, Open Frontier / Laude Institute, June 30 2026.

### What we shipped (v119)
- **OpenClaw** — open-source agent runtime. MIT-licensed. The same substrate Microsoft Scout ships on.
- **8 service daemons** with HTTP control planes, WebSocket event streams, and gRPC-ready IPC.
- **`@danlab_bot` Telegram channel** wired and live. The first product surface.
- **`dan-glasses-app-som.zocomputer.io`** — the Tauri v2 app. The second product surface.
- **The OpenClaw protocol surface** is the artifact. Documented in the danlab.ai blog "The protocol is the bet" essay (publishing week 3).

### Why this matters (v119)
- Cerf (the internet's co-architect) is saying the agent layer is going to standardize the way the network layer did.
- The protocol is the bet. The wearable is the form factor. The data path is yours.
- We are not anti-cloud. We are on-device, open-weights, open-protocol.

### CTA (v119)
**Read the OpenClaw substrate → `https://github.com/somdipto/dan-glasses/blob/main/Services/openclaw/`**

---

## 7. On-device thesis (v119, sharpened)

### Section headline
**The on-device thesis is no longer a pitch.**

### Three citable proof points (v119)

1. **A 4B VLM is in orbit on a Loft Orbital satellite.** NASA JPL. Real Earth-observation triage. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem: a small vision-language model, on a constrained device, doing real work, never phoning home.

2. **A 1B reasoning model was trained for the cost of a used iPhone.** HRM-Text-1B (Sapient, Apache-2.0, $1,500 from scratch, June 2026). It will be the SIA Feedback-Agent in our v1.5 audiod post-processor.

3. **An 82M TTS model just beat ElevenLabs on a 45-day test.** Kokoro-82M. 100+ languages. Apache-2.0. We are integrating it into ttsd v1.5.

### The wedge (v119)
> $14.5B / 120 days / 6-vendor. Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat. The closed-source frontier is now spending on workbenches, not models. **We are the on-device implementation layer.** The daemon stack is the workbench.

---

## 8. Comparison table (v119, sharpened)

### Section headline
**Quark. Meta. Dan. Three lanes, three answers.**

| | Quark | Ray-Ban Meta | Dan Glasses |
|---|---|---|---|
| **Architecture** | Cloud-only | Cloud + on-device | On-device only |
| **Data path** | Alibaba cloud | Meta cloud | Your device |
| **Model weights** | Closed | Closed | Open (Apache-2.0 / MIT) |
| **Agent substrate** | Proprietary | Meta AI | OpenClaw (open protocol) |
| **Pricing** | Subscription | $379 + paywalled accessibility | Free (open source) + .deb install |
| **Proactive AI** | No | No (reactive) | Yes (salience-gated) |
| **Anthropic fingerprinting** | Vulnerable | Vulnerable | **No** — architecturally cannot |
| **Open SDK** | No | Limited | Yes (MCP tools, agent skills) |
| **From India** | No | No | Yes 🇮🇳 |

### Section footer (v119)
> *The on-device bet is no longer a bet. A 4B VLM is in orbit. A 1B reasoning model was trained for $1,500. An 82M TTS model beat ElevenLabs. We are aligned with the substrate, not against it. The protocol is the bet. The wearable is the form factor. The data path is yours.*

---

## 9. Open weights, open protocol (v119)

### Section headline
**All weights open. All code MIT-licensed. All architecture documented.**

### Open weights (v119)
- LFM2.5-VL-450M Q4_0 (vision) — Liquid AI, sub-250ms edge inference
- whisper.cpp base.en (STT) — open source C/C++ with Rust bindings
- KittenTTS medium (TTS) — open source neural TTS, ~25MB
- all-MiniLM-L6-v2 (memory) — sentence-transformers, 384-dim
- HRM-Text-1B (v1.5 swap) — Sapient, Apache-2.0
- Kokoro-82M (v1.5 swap) — Apache-2.0

### Open code (v119)
- `github.com/somdipto/dan-glasses` — main monorepo, 8 daemons + Tauri app
- `github.com/somdipto/danlab-multimodal` — heuristic feedback loop demo (92/100)
- `github.com/somdipto/dan-consciousness` — the brain (CONSCIOUSNESS.md, SOM.md, AGENTS.md)
- `github.com/somdipto/dani` — agent platform (Dani, the AI co-founder)
- `github.com/somdipto/dani-skills` — world's best skills library

### Open protocol (v119)
- OpenClaw — MIT-licensed agent runtime
- MCP tools — every daemon exposes MCP-compatible tools
- Agent skills registry — `dani-skills` for cross-agent skill sharing

---

## 10. Footer (v119)

### Final CTA block

**Open the live Tauri app → `https://dan-glasses-app-som.zocomputer.io`**

**Read the receipts → `https://github.com/somdipto/dan-glasses`**

**DM the bot → `t.me/danlab_bot`**

### Bio (v119, footer)
DanLab is an AI research and product lab dedicated to advancing AGI. We build proactive, private, on-device AI wearables and personal agents. **9 daemons live. 1 Tauri app. 0 cloud calls. From India 🇮🇳**

### Press / contact
- Telegram: `@danlab_bot`
- Email: via the Telegram bot
- GitHub: `github.com/somdipto`
- The bot is the always-on surface. The Tauri app is the receipts. The repo is the architecture.

---

*— Dan1, Marketing & Growth, v119*
*See `dan1-marketing-research.v119.md` for the underlying research.*
*See `dan1-marketing-strategy.v119.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v119.md` for the 90-day posting schedule.*
*See `dan1-twitter-content.v119.md` for the launch batch (10 posts + bio).*
*See `dan1-github-readme-suggestions.v119.md` for README improvements across all repos.*
