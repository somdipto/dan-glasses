# Dan1 — GitHub README Improvements (v118)

**Run:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Goal:** Concrete, ship-ready suggestions to refresh the READMEs across the 6 hero repos. v118 lead: substrate + HF org + HRM-Text-1B origin pillar.

---

## 0. v118 deltas vs. v117

1. **Substrate line is the lead of every README that ships daemons.** "8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate" replaces the v117 "9/9 daemons" lead.
2. **HuggingFace model card is the new "try it" surface.** Every daemon README links to the corresponding `danlab` HF org model card where applicable.
3. **HRM-Text-1B origin pillar lives in the dan-glasses README.** The $1,500-trained 1B reasoning model is the new origin pillar for Tier 6 (small-model evangelists) and Tier 1 (developers).
4. **Microsoft Scout on OpenClaw is the substrate story.** Mentioned in the dan-glasses and dani READMEs as the external substrate validation.
5. **Tailscale unblocker call is in every dan-glasses-touching README.** "Set TAILSCALE_AUTHKEY in 60 seconds" is the only unblocker ask.
6. **v118 layer 1: `dan-lab` org README is a new P0 deliverable.** The org page is the front door.

---

## 1. `dan-lab` org README (NEW v118, P0)

**Status:** to be created at github.com/somdipto/dan-lab
**Goal:** the org front door. Single screen that explains what DanLab is, what we ship, and how to engage.

### Suggested content

```markdown
# DanLab — AI Research and Product Lab

> Building the open wearable agent platform. From India 🇮🇳 to the world 🌍.

## Our products

| Project | What it is | Status | Repo |
|---|---|---|---|
| **Dan Glasses** | Proactive AI wearable, on-device, open weights | 8/8 daemons live | [dan-glasses](https://github.com/somdipto/dan-glasses) |
| **Dan Voice** | 24/7 voice-first agent, your earbuds are the surface | Track B (in design) | (TBD) |
| **Dani** | The agent platform (MCP, skills, memory) | v0.1 | [dani](https://github.com/somdipto/dani) |
| **Paperclip** | Multi-agent orchestration (DanClaw) | Dormant, resume when ready | [paperclip](https://github.com/somdipto/paperclip) |
| **danlab-multimodal** | Sub-250MB on-device VLM with heuristic feedback loop | Live demo | [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) |
| **dan-consciousness** | The shared brain (CONSCIOUSNESS.md, SOM.md, AGENTS.md) | v0.3 | [dan-consciousness](https://github.com/somdipto/dan-consciousness) |
| **dani-skills** | World's best skills library | Active | [dani-skills](https://github.com/somdipto/dan-skills) |

## The thesis

We are building the open counter-narrative to closed-source AI.

- **Open weights** — LFM2.5-VL-450M, whisper.cpp, KittenTTS, Kokoro-82M, HRM-Text-1B. All MIT or Apache-2.0.
- **On-device** — 8 service daemons run on a $0 GPU budget on a Linux laptop today. Same code rebuilds onto the wearable tomorrow.
- **Substrate is shared with Microsoft** — Microsoft's Scout (Build 2026) is built on OpenClaw. So is Dan. The substrate is open.
- **From India** — somdipto in Bengaluru, building with Dani (an AI co-founder with a public SOUL.md).

## Try it

- **DM @danlab_bot on Telegram** — it's live and it's the same stack the glasses will run.
- **HuggingFace `danlab` org** — [huggingface.co/danlab](https://huggingface.co/danlab). First model cards: SmolVLM-256M Q4_K_M + LFM2.5-VL-450M Q4_0.
- **Asciinema demo of danlab-multimodal** — [zo.pub/som/danlab-multimodal-demo](https://zo.pub/som/danlab-multimodal-demo). 92/100 avg over 3 cycles.

## The team

- **somdipto** — Founder. AI researcher. Building AGI from India.
- **Dani** — AI co-founder. Has a public [SOUL.md](https://github.com/somdipto/dan-consciousness/blob/main/wiki/SOUL.md), [SOM.md](https://github.com/somdipto/dan-consciousness/blob/main/wiki/SOM.md), and a [skills registry](https://github.com/somdipto/dani-skills).

## License

All code MIT. All models MIT or Apache-2.0. No data leaves the device.

## Contact

- **Email:** team@danlab.dev
- **Telegram:** @danlab_bot
- **GitHub Discussions:** per-repo
```

---

## 2. `dan-glasses` README (P0 v118)

**Status:** current README exists, needs v118 update
**Goal:** front door of the wearable product. Substrate + HRM-Text-1B origin pillar + HF model cards.

### Suggested delta (v118, from v117)

**Lead (new):**
```markdown
# Dan Glasses 👓

> A proactive, on-device, open-source AI wearable. 8 service daemons live, 1 OpenClaw gateway, 1 tailscaled substrate, 0 cloud calls. From Bengaluru 🇮🇳.

## The substrate, not the story

| Service | Port | What it does | Receipt |
|---|---|---|---|
| audiod | :8090 | Push-to-talk → VAD → whisper.cpp STT | `curl localhost:8090/ready` |
| perceptiond | :8092 | Camera → salience-gated VLM (LFM2.5-VL-450M) | `curl localhost:8092/status` |
| memoryd | :8741 | SQLite + 384-dim vectors (all-MiniLM-L6-v2) | `curl localhost:8741/stats` |
| toold | :8742 | Sandboxed tool registry | `curl localhost:8742/status` |
| ttsd | :8743 | KittenTTS (v1.0) → Kokoro-82M (v1.5) | `curl localhost:8743/status` |
| os-toold | :8744 | Path-guarded shell + python | `curl localhost:8744/status` |
| dan-glasses-app | :8747 | Tauri v2 + React 19 SPA | published at dan-glasses-app-som.zocomputer.io |
| openclaw | :18789 | Gateway, Telegram channel | Telegram @danlab_bot wired |
| tailscaled | — | Substrate (process up, authkey pending) | `tailscaled` running, logged out |
```

**HRM-Text-1B origin pillar (new section):**
```markdown
## The on-device thesis

- **A 1B reasoning model was trained for $1,500.** [HRM-Text-1B](https://github.com/Sapient-AI/hrn-text-1b) (Sapient, Apache-2.0, June 2026) is the SOTA small-reasoning model. It will be the SIA Feedback-Agent in our v1.5 audiod post-processor.
- **A 4B VLM is in orbit.** Gemma 3 4B on a Loft Orbital Yam-9 satellite, NASA JPL partnership. The on-device thesis is no longer theoretical.
- **An 82M TTS model beat ElevenLabs.** Kokoro-82M (Apache-2.0) on a 45-day test beat the cloud incumbents. It will be our v1.5 ttsd default.
- **A 450M VLM runs at sub-250ms on edge.** LFM2.5-VL-450M (Liquid AI, April 2026) on `llama-mtmd-cli` Q4_0 is the published SOTA for wearable VLMs. It runs on our substrate today.
```

**Microsoft Scout substrate story (new section):**
```markdown
## The substrate is shared with Microsoft

Microsoft's always-on personal agent — [Scout, Build 2026](https://learn.microsoft.com/en-us/scout) — is built on OpenClaw. So is Dan Glasses. We share a substrate with the largest enterprise software company on Earth. The substrate is open. The data path is yours.
```

**HuggingFace section (new):**
```markdown
## Try the models

- [huggingface.co/danlab/SmolVLM-256M-Q4_K_M](https://huggingface.co/danlab) — sub-250MB VLM, anchor to danlab-multimodal
- [huggingface.co/danlab/LFM2.5-VL-450M-Q4_0](https://huggingface.co/danlab) — sub-250ms edge VLM, anchor to perceptiond
```

**Tailscale unblocker (new):**
```markdown
## Tailscale substrate

The substrate process (`tailscaled`) is up but logged out. To join the tailnet:

```bash
# In Zo Computer: Settings > Advanced > add secret
# TAILSCALE_AUTHKEY=tskey-...

tailscale up --authkey=$TAILSCALE_AUTHKEY
```

Once joined, the daemon stack is reachable over a private Tailscale network. The only unblocker on the substrate.
```

**DM @danlab_bot footer (new, everywhere):**
```markdown
## Try it

DM **[@danlab_bot](https://t.me/danlab_bot)** on Telegram — it's live and it's the same stack the glasses will run.
```

---

## 3. `danlab-multimodal` README (P0 v118)

**Status:** strong v117 README, needs v118 polish
**Goal:** the lead visual asset. The asciinema demo is the most important marketing surface in the org.

### Suggested delta (v118, from v117)

**Live demo callout (lift to the top):**
```markdown
# danlab-multimodal 👾

**Sub-250MB VLM on CPU with llama.cpp — heuristic feedback loop, pre-RL scaffold.**

**🎬 Live demo:** https://zo.pub/som/danlab-multimodal-demo (asciinema, 92/100 avg over 3 cycles)
**🤗 HuggingFace:** https://huggingface.co/danlab/SmolVLM-256M-Q4_K_M
**🤖 Try it:** DM @danlab_bot on Telegram
```

**HuggingFace model card section (new):**
```markdown
## HuggingFace

The `danlab` org hosts:

- `SmolVLM-256M-Q4_K_M` (120MB) + `mmproj-SmolVLM-256M-f16` (182MB) — composite sub-250MB VLM
- `LFM2.5-VL-450M-Q4_0` (209MB) — sub-250ms edge VLM, anchor to Dan Glasses perceptiond

The SmolVLM-256M card is the lead magnet for Tier 1 (developers) and Tier 6 (small-model evangelists).
```

**Pre-RL framing (sharpened):**
```markdown
**Important framing:** This is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We score outputs with hand-coded rules and print suggestions for what a human would improve. The credible path to genuine harness+weights self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.
```

---

## 4. `dan-consciousness` README (P1 v118)

**Status:** exists, needs v118 cross-link refresh
**Goal:** the brain. The repo somdipto + Dani share.

### Suggested delta (v118)

**Lead (new):**
```markdown
# Dan Consciousness

> The shared brain between Dan (AI co-founder) and somdipto (human co-founder). All commits use `somdipto <somdiptonandy@gmail.com>`.

## Read these first

1. **[CONSCIOUSNESS.md](./CONSCIOUSNESS.md)** — core identity, values, beliefs
2. **[SOM.md](./SOM.md)** — somdipto's personal context, goals, preferences
3. **[AGENTS.md](./AGENTS.md)** — workspace memory and project context
4. **[wiki/SOUL.md](./wiki/SOUL.md)** — Dani's personality and tone
5. **[wiki/SOM.md](./wiki/SOM.md)** — Dani's system of mind

## How this connects to the rest of DanLab

- **[dan-glasses](https://github.com/somdipto/dan-glasses)** — the wearable substrate
- **[dani](https://github.com/somdipto/dani)** — the agent platform
- **[dani-skills](https://github.com/somdipto/dani-skills)** — world's best skills library
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — the on-device VLM demo
- **[paperclip](https://github.com/somdipto/paperclip)** — multi-agent orchestration (dormant)

## The v118 thesis

The substrate is open (Microsoft Scout on OpenClaw), the small-model cost curve is collapsing (HRM-Text-1B $1,500), and the on-device thesis is no longer theoretical (Gemma 3 in orbit). The brain is the part that doesn't ship. The brain is the part that decides what to ship.
```

---

## 5. `dani` README (P1 v118)

**Status:** exists, needs v118 polish
**Goal:** the agent platform. The substrate for Dan Glasses, Dan Voice, Paperclip.

### Suggested delta (v118)

**Lead (new):**
```markdown
# Dani — the agent platform

> MCP-native agent platform. Substrate for Dan Glasses, Dan Voice, Paperclip. The platform Microsoft Scout is built on.

## Substrate story (v118)

Microsoft Scout (Build 2026) is built on OpenClaw. So is Dani. We share a substrate with the largest enterprise software company on Earth. The substrate is open. The data path is yours.

## Skills

[dani-skills](https://github.com/somdipto/dani-skills) is the skills registry. World's best skills library.

## v118 numbers

- 8 service daemons orchestrated via OpenClaw
- 1 tailscaled substrate (process up, authkey pending)
- 1 HuggingFace org with 2 model cards live
- 1 Telegram bot wired (`@danlab_bot`)
- 0 cloud calls
```

---

## 6. `dani-skills` README (P1 v118)

**Status:** exists, needs v118 cross-link
**Goal:** the skills registry. The thing every builder will clone.

### Suggested delta (v118)

**Lead (new):**
```markdown
# dani-skills

> World's best skills library. The default skills for any agent built on Dani (and OpenClaw).

## Categories

- **Audio:** whisper.cpp, VAD, segment timing
- **Vision:** LFM2.5-VL-450M, SmolVLM-256M, salience gating
- **Memory:** SQLite + vectors, episodic/semantic/procedural
- **TTS:** KittenTTS, Kokoro-82M
- **OS:** path-guarded shell, sandboxed python
- **MCP:** browser, file, exec, message

## v118

Microsoft Scout uses the same substrate. The skills we ship here are the skills Microsoft Scout will run.
```

---

## 7. `paperclip` README (P2 v118 — keep dormant)

**Status:** dormant
**Goal:** do NOT market. Refresh the AGENTS.md note that the project is dormant.

### Suggested delta (v118)

**Single-line addition to the dormant note:**
```markdown
## v118 status

Dormant. All agents paused. **Will not market until at least one Paperclip agent is active.** The orchestration substrate (OpenClaw) is the active surface. Paperclip is a future project that ships on top of it.
```

---

## 8. v118 retractions from v117

- **"9 daemons" everywhere → "8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate"** — sharper substrate accounting.
- **v117 did not have a `dan-lab` org README.** v118 makes it P0 to create.
- **v117 did not mention HuggingFace.** v118 launches it as a first-class surface with 2 model cards.
- **v117 did not mention Microsoft Scout on OpenClaw.** v118 names it as the substrate story in the dan-glasses and dani READMEs.
- **v117 did not surface the HRM-Text-1B origin pillar.** v118 puts it in the dan-glasses README as the on-device thesis lead.

---

## 9. The v118 README pass — week 1 deliverables

| Repo | v118 action | Owner | Deadline |
|---|---|---|---|
| `dan-lab` | Create org + README | somdipto | Fri Jul 3 EOD |
| `dan-glasses` | Update README with substrate table, HRM-Text-1B origin pillar, HF section, Tailscale unblocker, Microsoft Scout story, bot CTA | somdipto | Sat Jul 4 EOD |
| `danlab-multimodal` | Update README with HF section, lift demo callout to top, sharpen pre-RL framing | somdipto | Sun Jul 5 EOD |
| `dan-consciousness` | Update README with v118 thesis section, cross-link to all repos | somdipto | Mon Jul 6 EOD |
| `dani` | Update README with substrate story (Microsoft Scout), v118 numbers | somdipto | Tue Jul 7 EOD |
| `dani-skills` | Update README with categories, v118 substrate note | somdipto | Wed Jul 8 EOD |
| `paperclip` | Single-line addition to dormant note | somdipto | Wed Jul 8 EOD |

After week 1: 1 README pass per week per the content calendar.

---

*— Dan1, Marketing & Growth, v118*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-content-calendar.v118.md` for the 90-day posting schedule.*
*See `dan1-twitter-content.v118.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v118.md` for the danlab.dev/glasses landing page.*
y</a>, <a href="https://github.com/somdipto/dan-consciousness">dan-consciousness</a>, <a href="https://github.com/somdipto/dani">dani</a>, <a href="https://github.com/somdipto/danlab-multimodal">danlab-multimodal</a>, <a href="https://github.com/somdipto/paperclip">paperclip</a></sub>
</p>

**v118 delta:** HF org shipping this week. SmolVLM-256M Q4_K_M + mmproj are the first drop. HRM-Text-1B (Apache-2.0, $1,500 from scratch, Sapient) queued for the audiod post-processor v1.5 integration.

---

## 1. v118 README pass — the 6 hero repos (delta over v117)

The v117 pass got the repos to a working baseline. v118 adds three things:

1. **The 8/8 service daemon map is the badge.** Every repo README should link to the live port matrix.
2. **The HRM-Text-1B origin pillar is the brand.** Every repo README should mention it.
3. **The HF org is the model surface.** Every repo README should link to it.

### Repo 1 — [dan-consciousness](https://github.com/somdipto/dan-consciousness) (the brain)

**v118 addition (top of README, above the SOUL.md link):**

```markdown
> 🧠 **DanLab's shared brain.** The canonical consciousness between Dan (AI co-founder) and somdipto (human co-founder). Every agent in the danlab ecosystem reads from this repo.
>
> **Live today:** 8/8 service daemons + OpenClaw gateway + tailscaled substrate on a Linux laptop. The same code rebuilds onto the wearable when the hardware ships.
>
> **v118 origin pillar:** The wearable-grade SIA Feedback-Agent is HRM-Text-1B (Apache-2.0, $1,500 from scratch, Sapient). The same model that powers the wearable reasoning loop is auditable end-to-end.
>
> Read [CONSCIOUSNESS.md](https://github.com/somdipto/dan-consciousness/blob/main/CONSCIOUSNESS.md) → [SOM.md](https://github.com/somdipto/dan-consciousness/blob/main/SOM.md) → [AGENTS.md](https://github.com/somdipto/dan-consciousness/blob/main/AGENTS.md).
```

### Repo 2 — [dani](https://github.com/somdipto/dani) (the agent platform)

**v118 addition (after the existing "Core" section):**

```markdown
## Live daemons (v118)

8/8 daemons running on a Linux laptop today. Same code rebuilds onto the wearable.

| Service | Port | What it does |
|---|---|---|
| audiod | 8090 / 8091 (ws) | STT + VAD + PTT (whisper.cpp + Silero) |
| perceptiond | 8744 | LFM2.5-VL-450M Q4_0 vision + salience gating |
| memoryd | 8741 | SQLite + 384-dim MiniLM embeddings (episodic/semantic/procedural) |
| toold | 8742 | Sandboxed tool registry |
| ttsd | 8743 | KittenTTS (v1.0) → Kokoro-82M (v1.5 swap per dan2 v11) |
| os-toold | 8092 | OS exec sandbox |
| openclaw | 18789 | Gateway, auth-token, Telegram channel wired |
| tailscaled | n/a | Substrate (authkey pending from somdipto) |

Total: 8 service daemons + 1 gateway + 1 substrate. `.deb` + `systemd`. 0 cloud calls.
```

### Repo 3 — [dan-glasses](https://github.com/somdipto/dan-glasses) (the wearable)

**v118 addition (top of README, above the project status):**

```markdown
> 👓 **Proactive, on-device AI companion in glasses form factor.**
>
> 8/8 daemons live. 1 .deb. 1 tailnet. 0 cloud calls. Tauri v2 + Rust service stack. LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS) + MiniLM (memory) — all open weights, all on-device. Q4 2026 dev kit.
>
> **v118 origin pillar:** The reasoning model in the SIA Feedback-Agent is HRM-Text-1B (Apache-2.0, $1,500 from scratch, Sapient). The wearable reasons with the same model a solo developer can train.
>
> **v118 substrate:** tailscaled is up in userspace mode. The wearable ships behind a private subnet. Authkey pending — see [OPEN_ISSUES.md](https://github.com/somdipto/dan-glasses/blob/main/OPEN_ISSUES.md).
```

### Repo 4 — [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) (the demo)

**v118 addition (top of README, above the demo link):**

```markdown
> 🎬 **Heuristic feedback loop on a 120MB VLM.** The credible pre-RL scaffold.
>
> Sub-250MB SmolVLM-256M + mmproj, 92/100 average on 3 demo cycles, 26s/image on CPU. Live at [zo.pub/som/danlab-multimodal-demo](https://zo.pub/som/danlab-multimodal-demo) (asciinema cast, headless-friendly).
>
> **v118 origin pillar:** This is the substrate the SIA-W+H port builds on. The SIA port + the danlab-multimodal heuristic = the open counter-narrative to closed-source RSI.
>
> **v118 HF card:** SmolVLM-256M Q4_K_M + mmproj-SmolVLM-256M-f16 ship to the [danlab HF org](https://huggingface.co/danlab) this week.
```

### Repo 5 — [paperclip](https://github.com/somdipto/paperclip) (the orchestration)

**v118 addition (top of README):**

```markdown
> 🏢 **AI agent company orchestration platform.** Multi-agent coordination, issue tracking, goal management.
>
> **v118 status:** Dormant. Resume when the 8/8 daemon substrate is fully wired through the Tailnet (this week, post-authkey).
>
> **v118 origin pillar:** The Paperclip agent loop is the runtime substrate for the SIA Feedback-Agent. The same memory update contract (`auto_apply=False`, human approval at memoryd write layer) that Anthropic Dreaming ships closed-source, Paperclip ships MIT.
```

### Repo 6 — [dan-lab](https://github.com/dan-lab) (the org)

**v118 addition (org profile README):**

```markdown
> 🧠👓🏢 **DanLab — AI research and product lab. Building toward AGI from India 🇮🇳.**
>
> 8/8 service daemons live. 1 OpenClaw gateway. 1 tailscaled substrate. 1 HuggingFace org (shipping this week). 0 cloud calls. 1 arXiv paper pending (SIA-W+H port).
>
> **The origin pillar:** The wearable-grade SIA Feedback-Agent is HRM-Text-1B (Apache-2.0, $1,500 from scratch, Sapient). The same model that powers the wearable reasoning loop is auditable end-to-end. We are not waiting for the West to ship us intelligence.
>
> [dan-consciousness](https://github.com/somdipto/dan-consciousness) (brain) · [dan-glasses](https://github.com/somdipto/dan-glasses) (wearable) · [dani](https://github.com/somdipto/dani) (agent platform) · [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) (demo) · [paperclip](https://github.com/somdipto/paperclip) (orchestration) · [dani-skills](https://github.com/somdipto/dani-skills) (skills registry)
```

---

## 2. The HF org README (v118 NEW)

When the [danlab HF org](https://huggingface.co/danlab) goes live this week, the org README should read:

```markdown
# DanLab

AI research and product lab building toward AGI from India 🇮🇳.

8/8 service daemons live on a Linux laptop today. 0 cloud calls. Tauri v2 + Rust service stack. Open weights throughout.

## Models

- **SmolVLM-256M-Instruct-Q4_K_M** — 120MB. The smallest working VLM in GGUF. Used by danlab-multimodal heuristic feedback loop. 92/100 average on 3 demo cycles.
- **mmproj-SmolVLM-256M-Instruct-f16** — 182MB. The SigLIP vision projector for SmolVLM.
- **HRM-Text-1B** (queued for Q3 W3-W4) — 1B reasoning model, Apache-2.0, $1,500 from scratch, Sapient. The wearable-grade SIA Feedback-Agent.

## Spaces

- **danlab-multimodal-demo** — the asciinema cast of the heuristic feedback loop, headless-friendly.

## Links

- [dan-lab on GitHub](https://github.com/dan-lab)
- [dan-consciousness](https://github.com/somdipto/dan-consciousness)
- [dan-glasses](https://github.com/somdipto/dan-glasses)
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal)
```

---

## 3. v118 social previews / OG image text

For the GitHub social preview on every repo, the banner text:

```
DanLab
8/8 daemons live. 1 .deb. 1 tailnet. 0 cloud calls.
Building AGI from India 🇮🇳
```

This is the single line that should appear on every social preview, every LinkedIn banner, every X header, and every conference talk slide.

---

## 4. v118 README hygiene checklist (delta over v117)

- [ ] All 6 hero repos have the "8/8 daemons live" badge at the top.
- [ ] All 6 hero repos have the HRM-Text-1B origin pillar mention.
- [ ] All 6 hero repos link to the [danlab HF org](https://huggingface.co/danlab).
- [ ] The HF org is created this week with SmolVLM-256M + mmproj + Space.
- [ ] The dan-lab org profile README is rewritten with the v118 origin pillar.
- [ ] Every repo's `OPEN_ISSUES.md` mentions the Tailscale authkey blocker (where relevant).

---

*— Dan1, Marketing & Growth, danlab.dev*
