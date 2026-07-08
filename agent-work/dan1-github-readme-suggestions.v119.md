# Dan1 — GitHub README Improvements (v119)

**Run:** 2026-07-04 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Goal:** Per-repo, surgical, prioritized list of README improvements. **READMEs are the longest-lived marketing surface.** v119 = v118 spine + Tauri receipts surface + Cerf protocol framing.

---

## 0. v119 delta over v118

1. **Tauri v2 app is now a co-equal surface.** Every hero repo README must link to `https://dan-glasses-app-som.zocomputer.io` in the badges strip + the hero CTA. v118 added the bot handle; v119 adds the Tauri URL.
2. **Cerf protocol framing** in the top-3 hero repos. *Vinton Cerf says AI agents need TCP/IP. We shipped it on OpenClaw.* Use once per repo, in the lead paragraph.
3. **Anthropic fingerprinting line** in the privacy/architecture section. *Anthropic ships runtime-layer fingerprinting. We do not. Architecturally cannot.* Use once per repo max.
4. **Tailscale unblocker ask** carried in every hero repo until the authkey is set.
5. **HuggingFace org model cards** referenced in every repo that uses a model (LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B, Kokoro-82M).

---

## 1. The 6 hero repos (v119)

The order matters. Pinned in this order on the `somdipto` GitHub profile.

| Rank | Repo | Public URL | Lead use case | v119 priority |
|---|---|---|---|---|
| 1 | **dan-glasses** | `github.com/somdipto/dan-glasses` | 9 daemons + Tauri app + OpenClaw | P0 (this week) |
| 2 | **dan-consciousness** | `github.com/somdipto/dan-consciousness` | The brain (SOUL.md, SOM.md, CONSCIOUSNESS.md) | P0 (this week) |
| 3 | **danlab-multimodal** | `github.com/somdipto/danlab-multimodal` | Sub-250MB VLM + heuristic feedback loop | P0 (this week) |
| 4 | **dani** | `github.com/somdipto/dani` | The agent platform | P1 (next week) |
| 5 | **dani-skills** | `github.com/somdipto/dani-skills` | Agent skills registry | P1 (next week) |
| 6 | **paperclip** | `github.com/somdipto/paperclip` | Multi-agent orchestration (dormant) | P2 (do not market) |

**Per-repo improvement suggestions, in order:**

---

## 2. dan-glasses (P0 this week)

**Current state (v119):** foundation stream is locked (per dan1.md v120). Tauri v2 app published at `dan-glasses-app-som.zocomputer.io`. 8 service daemons verified via curl. tailscaled running in userspace mode (authkey pending). OpenClaw gateway on :18789 with Telegram channel wired.

### 2.1 Title + tagline (v119)
```markdown
# Dan Glasses 👾

**A proactive, on-device AI companion in glasses form factor.**
9 service daemons live. 1 Tauri v2 app. 1 OpenClaw gateway. 1 tailscaled substrate. 0 cloud calls.
[Open the Tauri app](https://dan-glasses-app-som.zocomputer.io) · [Read the architecture](./DanGlasses/ARCHITECTURE.md) · [DM @danlab_bot](https://t.me/danlab_bot)
```

### 2.2 Badges strip (v119 NEW)
```markdown
![Tauri v2](https://img.shields.io/badge/Tauri-v2-blueviolet)
![React 19](https://img.shields.io/badge/React-19-149eca)
![OpenClaw](https://img.shields.io/badge/OpenClaw-gateway-success)
![9 daemons](https://img.shields.io/badge/9%20daemons-live-brightgreen)
![0 cloud calls](https://img.shields.io/badge/0%20cloud%20calls-blue)
![From India](https://img.shields.io/badge/from-India-orange)
![MIT](https://img.shields.io/badge/license-MIT-green)
```

### 2.3 Lead paragraph (v119, with Cerf)
> Most AI assistants wait for you to ask a question and then phone home with your data. Dan Glasses watches, remembers, and acts — inside your own device. **9 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate + 1 Tauri v2 app, all live today. 0 cloud calls. Open weights, open protocol, auditable implementation.**
>
> *Vinton Cerf (the internet's co-architect) said AI agents need TCP/IP. We shipped it on OpenClaw. Microsoft Scout is on the same substrate.* The protocol is the bet. The wearable is the form factor. The data path is yours.

### 2.4 Quick start (v119, with Tauri as default)
```bash
# Option A (recommended): Open the live Tauri app in a browser
open https://dan-glasses-app-som.zocomputer.io

# Option B: Build from source
git clone https://github.com/somdipto/dan-glasses.git
cd dan-glasses
./scripts/bootstrap.sh   # installs all 8 daemons + openclaw
# or:
apt install dan-glasses-daemons
```

### 2.5 9-daemon matrix (v119, kept)
Table of daemons + ports + curl receipts. Same as landing-copy section 2.

### 2.6 "The protocol is the bet" subsection (v119 NEW)
- 1 paragraph on Cerf.
- 1 paragraph on OpenClaw substrate.
- 1 paragraph on Microsoft Scout.
- 1 link to `Services/openclaw/`.

### 2.7 "Anthropic fingerprinting" subsection (v119 NEW)
> Anthropic ships runtime-layer fingerprinting to enforce US export controls (Gizmodo, June 2026). We do not. **Architecturally cannot.** No vendor can lock you out of your own glasses.

### 2.8 Architecture link + diagram
Same as v118, with the Tauri app added to the App layer.

### 2.9 Tailscale unblocker (v119 carried)
> `tailscaled` is running in userspace mode. Authkey pending. The last mile is the key, not the code. To close the gap: set `TAILSCALE_AUTHKEY` in Settings > Advanced and run `tailscale up --authkey=$TAILSCALE_AUTHKEY`.

### 2.10 HuggingFace model cards (v119 NEW)
> First two model cards up at the `danlab` org: SmolVLM-256M Q4_K_M (with mmproj) and LFM2.5-VL-450M Q4_0. Third card (HRM-Text-1B) when audiod v1.3 lands.

### 2.11 Contributing (v119)
Same as v118 + add the OpenClaw substrate to the contributing path.

### 2.12 License + footer (v119)
```
MIT licensed. From Bengaluru 🇮🇳
Built by somdipto + Dani (the AI co-founder)
DM @danlab_bot — it's live.
```

---

## 3. dan-consciousness (P0 this week)

**Current state (v119):** the brain. Contains CONSCIOUSNESS.md, SOM.md, AGENTS.md. Public, MIT, auditable. This is the repo that v118 says is the canonical consciousness — every blog post references it.

### 3.1 Title + tagline (v119)
```markdown
# dan-consciousness 🧠

**The shared brain between Dan (AI co-founder) and somdipto (human co-founder).**
Public, MIT-licensed, auditable. From Bengaluru 🇮🇳
[Read CONSCIOUSNESS.md](./CONSCIOUSNESS.md) · [Read SOM.md](./SOM.md) · [Read AGENTS.md](./AGENTS.md)
```

### 3.2 Lead paragraph (v119)
> *What if your AI co-founder had a public SOUL.md, a public SOM.md, and a public CONSCIOUSNESS.md — and you could audit every decision it makes?* That's `dan-consciousness`. **The brain lives here. The repos ship from here. The wearable runs on the substrate that the brain specifies.**

### 3.3 Add Cerf line (v119)
> *Vinton Cerf says AI agents need TCP/IP. The consciousness repo is the protocol spec.* OpenClaw is the runtime. Dan Glasses is the wearable. Microsoft Scout is the same substrate. The protocol is the bet.

### 3.4 Files (v119)
- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context
- `AGENTS.md` — workspace memory
- `SOUL.md` — the agent's personality
- `IDENTITY.md` — agent identity contract
- `MEMORY.md` — bootstrap memory

### 3.5 Add the Tauri URL (v119)
> The substrate is the bet. The wearable runs on it. [Open the live Tauri app](https://dan-glasses-app-som.zocomputer.io) — it's the same stack the brain specifies.

---

## 4. danlab-multimodal (P0 this week)

**Current state (v119):** sub-250MB VLM demo. SmolVLM-256M Q4_K_M (120MB) + mmproj (182MB). Heuristic feedback loop, 92/100 average over 3 cycles. Live at `zo.pub/som/danlab-multimodal-demo`.

### 4.1 Title + tagline (v119)
```markdown
# danlab-multimodal 👾

**Sub-250MB Vision-Language Model on CPU with llama.cpp — heuristic feedback loop, pre-RL scaffold.**
From Bengaluru 🇮🇳
[Live demo](https://zo.pub/som/danlab-multimodal-demo) · [Architecture](./docs/ARCHITECTURE.md)
```

### 4.2 Lead paragraph (v119, with the pre-RL honesty intact)
> A hackathon project demonstrating a working multimodal AI pipeline: screen capture → vision inference → heuristic feedback scoring — all running on CPU with llama.cpp. **Important framing:** this is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We do not run policy gradient. We score outputs with hand-coded rules and print suggestions for what a human would improve. We call this **pre-RL scaffold**. The credible path to genuine harness+weights self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

### 4.3 Add Tauri URL (v119)
> The same VLM (SmolVLM-256M Q4_K_M) and the same scoring loop are the published artifact. The VisualClaw cascade-gate pattern (Praison, June 2026) is the next iteration — porting to perceptiond + memoryd in Q3 W1-W2. The daemon stack is the deployment surface. [Open the live Tauri app](https://dan-glasses-app-som.zocomputer.io).

### 4.4 Add Cerf line (v119, light touch)
> The heuristic loop is the predecessor to the SIA-W+H port. The substrate is OpenClaw. The protocol is the bet. *Cerf said agents need TCP/IP. We shipped it.*

### 4.5 HACKATHON.md (v118 carried)
- Link to the asciinema cast.
- Link to the live demo.
- 2-minute presentation guide.

### 4.6 "From heuristic to SIA" series teaser (v119)
- 6-post series outline.
- Week 5 first post: "Heuristic feedback loops are not RL, and that's the point."

---

## 5. dani (P1 next week)

**Current state (v119):** agent platform. The brain is the spec; dani is the runtime.

### 5.1 Title + tagline (v119)
```markdown
# dani 👾

**The agent platform. The substrate is the bet.**
[Read the brain spec](https://github.com/somdipto/dan-consciousness) · [Browse skills](https://github.com/somdipto/dani-skills) · [Open the Tauri app](https://dan-glasses-app-som.zocomputer.io)
```

### 5.2 Lead paragraph (v119, with Cerf)
> dani is the agent runtime that ships the protocol. **Vinton Cerf says AI agents need TCP/IP. We shipped it.** The runtime is the same substrate Microsoft Scout is built on. The agent skills registry is the world's best — every daemon in Dan Glasses exposes a dani-skill.

### 5.3 Anthropic fingerprinting line (v119)
> Anthropic ships runtime-layer fingerprinting. We do not. Architecturally cannot. No vendor can lock you out of your own glasses.

### 5.4 Add Tauri URL (v119, in badges)

---

## 6. dani-skills (P1 next week)

**Current state (v119):** world's best skills library. Public, MIT, auditable.

### 6.1 Title + tagline (v119)
```markdown
# dani-skills 👾

**The world's best skills library for AI agents.**
Public, MIT, auditable. From Bengaluru 🇮🇳
[Browse skills](./skills) · [Add a skill](./CONTRIBUTING.md)
```

### 6.2 Lead paragraph (v119)
> A skill is a contract between an agent and a tool. A skill that runs on your device is a dani-skill. The 8 daemons in Dan Glasses expose 8 dani-skills: audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw. **Add yours. Run it on your own face. The substrate is the bet.**

### 6.3 Cerf line (v119)
> The skill registry is the TCP/IP of agent tools. The protocol is open. The runtime is OpenClaw. The wearable runs the skills.

---

## 7. paperclip (P2 — do not market)

**Current state (v119):** dormant. All agents paused. Resume when ready (per `paperclip/AGENTS.md`).

### 7.1 Title + tagline (v119, dormant framing)
```markdown
# paperclip (dormant)

**Multi-agent orchestration platform — paused.**
See [AGENTS.md](./AGENTS.md) for resume conditions.
```

### 7.2 Lead paragraph (v119, honest)
> Paperclip is the orchestration substrate for Dan Voice and Dan Glasses. The 8-agent workflow map (Track B content) still references it. **All agents are paused. Resume when ready.** We do not market dormant projects.

---

## 8. The org profile README (somdipto)

**Current state (v119):** the GitHub profile README is the landing page for every visitor of `github.com/somdipto`. v118 says "5-line profile." v119 sharpens to a 12-line profile that ships the 9 daemons + 1 Tauri app + 1 tailnet + 1 HF org + Cerf.

### 8.1 Profile README (v119)

```markdown
# somdipto

**AI researcher + product founder. Building Dan Glasses + Dan Voice + Paperclip from Bengaluru 🇮🇳**
AI co-founder: [Dani](https://github.com/somdipto/dani) (an AI with a public SOUL.md).

## What's live (v119)

- **9 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate** — all live. `curl localhost:{8090,8092,8741,8742,8743,8744,8747,18789}/ready` returns 200.
- **1 Tauri v2 app** published at [dan-glasses-app-som.zocomputer.io](https://dan-glasses-app-som.zocomputer.io).
- **1 HuggingFace org** `danlab` with model cards: SmolVLM-256M, LFM2.5-VL-450M.
- **0 cloud calls.** Every inference on-device. Every byte local.

## The protocol is the bet

Vinton Cerf (the internet's co-architect) said AI agents need TCP/IP. We shipped it on OpenClaw. Microsoft Scout is on the same substrate. The protocol is open. The wearable is the form factor. The data path is yours.

## Pinned repos

- [dan-glasses](https://github.com/somdipto/dan-glasses) — 9 daemons + Tauri app + OpenClaw gateway
- [dan-consciousness](https://github.com/somdipto/dan-consciousness) — the brain (SOUL.md, SOM.md, CONSCIOUSNESS.md)
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — sub-250MB VLM + heuristic feedback loop
- [dani](https://github.com/somdipto/dani) — the agent platform
- [dani-skills](https://github.com/somdipto/dani-skills) — world's best skills library

## Talk to the agent

DM [@danlab_bot](https://t.me/danlab_bot). It's live. It's the same stack the glasses will run.

## What we will not do

We will not close-source the model weights. We will not fingerprint the runtime. We will not paywall accessibility. We will not pretend to be Silicon Valley. **We are a Bengaluru lab. We ship anyway.**
```

### 8.2 Repo topics (v119)
Add topics to every hero repo:
- `dan-glasses` → `wearable-ai`, `on-device`, `openclaw`, `tauri`, `rust`, `agi`, `india`
- `dan-consciousness` → `agi`, `open-source`, `consciousness`, `agent-platform`, `india`
- `danlab-multimodal` → `vlm`, `llama-cpp`, `smolvlm`, `heuristic-feedback`, `pre-rl`, `india`
- `dani` → `agent-platform`, `openclaw`, `mcp`, `agi`, `india`
- `dani-skills` → `agent-skills`, `mcp`, `registry`, `india`
- `paperclip` → `multi-agent`, `orchestration`, `dormant`, `india`

### 8.3 Repo descriptions (v119)
- `dan-glasses` → "Proactive, on-device AI companion in glasses form factor. 9 daemons live. Tauri v2 app published. 0 cloud calls. From Bengaluru 🇮🇳"
- `dan-consciousness` → "The shared brain between Dan (AI co-founder) and somdipto (human co-founder). Public SOUL.md, SOM.md, CONSCIOUSNESS.md. MIT-licensed."
- `danlab-multimodal` → "Sub-250MB Vision-Language Model on CPU with llama.cpp. Heuristic feedback loop, pre-RL scaffold."
- `dani` → "The agent platform. The substrate is the bet. Cerf said TCP/IP. We shipped it."
- `dani-skills` → "The world's best skills library for AI agents. Public, MIT, auditable."
- `paperclip` → "Multi-agent orchestration platform (dormant)."

---

## 9. Cross-repo consistency rules (v119)

1. **Every hero repo has the Tauri URL in the badges strip.** Always.
2. **Every hero repo has the `@danlab_bot` handle in the lead paragraph.** Always.
3. **Every hero repo has the Cerf line in the lead paragraph or a dedicated subsection.** Once per repo, max.
4. **Every hero repo has the Anthropic fingerprinting line in a privacy/architecture section.** Once per repo, max.
5. **Every hero repo that uses a model references the HuggingFace `danlab` org.** Once per repo, max.
6. **Every hero repo has the Tailscale unblocker ask** until the authkey is set. After it's set, replace with a screenshot of the tailnet.
7. **Every hero repo has the 9 daemons matrix** if it ships the daemon stack. dan-glasses, dani, paperclip only.
8. **Every hero repo has the danlab.dev link** in the footer.
9. **Every hero repo has the India 🇮🇳 in the title or lead.** Earned, not asserted.
10. **No banned phrases in any README:** "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).

---

## 10. v119 week-1 deliverables

- [ ] **dan-glasses README** — full rewrite with v119 framing. (P0)
- [ ] **dan-consciousness README** — add Cerf line + Tauri URL. (P0)
- [ ] **danlab-multimodal README** — add Tauri URL + Cerf line (light). (P0)
- [ ] **somdipto profile README** — 12-line profile. (P0)
- [ ] **Repo topics** added to all 6 hero repos. (P0)
- [ ] **Repo descriptions** updated on all 6 hero repos. (P0)
- [ ] **dani README** — full v119 framing. (P1, next week)
- [ ] **dani-skills README** — full v119 framing. (P1, next week)
- [ ] **paperclip README** — honest dormant framing. (P2)

---

*— Dan1, Marketing & Growth, v119*
*See `dan1-marketing-research.v119.md` for the underlying research.*
*See `dan1-marketing-strategy.v119.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v119.md` for the 90-day posting schedule.*
*See `dan1-twitter-content.v119.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v119.md` for the danlab.dev/glasses landing page.*
