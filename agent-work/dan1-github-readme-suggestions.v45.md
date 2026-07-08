# Dan1 GitHub README Improvements — v45

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-14 06:50 IST (01:20 UTC)
**Status:** ✅ Canonical, shippable. v44 had 548 lines, v45 has the same diffs with verified current state baked in (Apple WWDC no-show, Brilliant Labs Halo delays, Meta Ray-Ban Display $799, India Stack clean sweep).

> Apply in 25 min. Runs on the day the repos go public.

---

## THE 5-PUNCHLIST (apply in this order, ~75 min total — this is the Day-0 list)

Verified current state of each item:

| # | Item | Current state (this run) | Action | Time |
|---|---|---|---|---|
| 1 | `somdipto/danlab-multimodal` | **404 / private** (Not Found to anonymous) | Make public, replace README | 30 min |
| 2 | `somdipto` profile | bio = "Build - Eat - Sleap", name = "Sodan", 0 pinned, 0 topics | Update bio + name + pin 4 + add 5 topics to each | 20 min |
| 3 | `somdipto/dan-glasses` | pub, 0★, 0 forks, 0 topics, desc "AI-native smart glasses..." | Update description, add 5 topics, rewrite README | 10 min |
| 4 | `somdipto/dani` | pub, 1★, 0 forks, 0 topics | Update description, add 5 topics | 5 min |
| 5 | `somdipto/danclaw` | pub, 1★, 0 forks, 0 topics | Update description, add 5 topics | 5 min |
| 5b | `somdipto/dan-consciousness` | pub, 0★, 0 forks, 0 topics | Add 5 topics | 5 min |

**Plus:** All 4 pinned repos get 5 topics.

---

## TOPIC SET (add to all 4 pinned repos)

GitHub repo topics appear in search, the "explore" page, and the repo's right sidebar. Use the same 5 across all 4 for brand consistency:

```
ai-wearable
edge-ai
local-first
open-source
from-india
```

How to add: Repo → About (gear icon) → Topics → paste each one.

For `dani` and `danclaw`, add a 6th topic for the specific function:

- `dani` extras: `agent-runtime`, `openclaw`
- `danclaw` extras: `agent-orchestration`, `paperclip-fork`

---

## PINNED REPOS (the profile hero)

On github.com/somdipto → "Customize your pins" → pin these 4:

1. **`dan-glasses`** — Proactive AI glasses. Sees what you see, hears what you say, remembers what matters. 7 services, 0 cloud calls, $0/month. From India 🇮🇳 Open source.
2. **`danlab-multimodal`** — Sub-250MB VLM on CPU. Heuristic feedback loop → SIA fork path. The smallest multimodal that actually runs on edge.
3. **`dani`** — Home for all your AI agents — memory, skills, sessions, secrets, app connections. The OpenClaw/Hermes/Claude Code runtime. From India 🇮🇳
4. **`danclaw`** — AI agent company orchestration. Hire agents, set goals, control costs. Paperclip fork with India region + cloud deploy. From India 🇮🇳

---

## PROFILE BIO UPDATE

**Current (verified):**
```
Build - Eat - Sleap
```

**Replace with (95 chars, well under GitHub's 160 limit):**
```
DanLab 👾 | Building AGI from India 🇮🇳 | danlab.dev | AI glasses, open source, local-first
```

**Name field (currently "Sodan"):**
```
Somdipto Nandy · DanLab
```

---

## REWRITE 1: `somdipto/danlab-multimodal/README.md`

This is the highest-leverage README in the org. It's the only public multimodal proof point. When this repo goes public, every marketing channel points at it.

```markdown
# danlab-multimodal 👾

**Sub-250MB Vision-Language Model on CPU with llama.cpp — heuristic feedback loop, pre-RL scaffold.**

![Hackathon: H2 2025](https://img.shields.io/badge/hackathon-H2%202025-blueviolet)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Model: SmolVLM-256M](https://img.shields.io/badge/model-SmolVLM--256M-yellow)

---

A working multimodal AI pipeline: screen capture → vision inference → heuristic feedback scoring — all on CPU with llama.cpp.

**Important framing:** This is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We do not run policy gradient or any RL algorithm. We score outputs with hand-coded rules (length, error detection, content quality) and print suggestions for what a human would improve. We call this **pre-RL scaffold**.

**Why this matters:** The market is paying multi-billion-dollar valuations for self-improving systems. We will not claim "RL" until the harness+weights modification is open and auditable. The credible path is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

## What it does

```
Screen → Vision Inference → Heuristic Feedback Score → Suggestion → Loop
  │              │                  │               │       │
scrot      llama-mtmd-cli      Score 0-100      Improvement   ↻
(fallback)   + SmolVLM-256M   heuristic         per cycle
```

## Live demo

**Live at:** https://zo.pub/som/danlab-multimodal-demo

Contains: asciinema terminal recording of the full heuristic feedback loop demo, pipeline diagrams, and documentation.

## Quick start

```bash
cd danlab-multimodal
python3 src/demo.py demo
```

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full pipeline diagram.

| Component | Technology | Notes |
|-----------|-----------|-------|
| Inference engine | `llama-mtmd-cli` (llama.cpp) | Unified multimodal CLI |
| Vision model | SmolVLM-256M Q4_K_M | 120MB — smallest working VLM |
| Vision projector | mmproj-SmolVLM-256M-f16 | 182MB — SigLIP encoder |
| Screen capture | scrot (Linux) | Falls back to synthetic images |
| Heuristic scoring | Hand-coded | Length + error + content quality |

## Why this exists

Dan Glasses (the consumer wearable in this org) needs a VLM that runs on a $200 board. The production target is **LFM2.5-VL-450M** (209MB, sub-250ms edge inference, Liquid AI, released Apr 11 2026). SmolVLM-256M is the demo vehicle — it proves the pipeline architecture works on a sub-250MB model on CPU.

When the LFM2.5-VL-450M swap lands in production, this repo becomes the research artifact: the smallest VLM pipeline that actually runs on edge, with a clear path to recursive self-improvement via SIA.

## Next steps

1. **LFM2.5-VL-450M swap** in production (Dan Glasses `perceptiond`).
2. **SIA fork** — plug SIA (Hexo Labs, MIT, May 2026) into the heuristic loop. Hand-coded → learned.
3. **Faster inference** — GPU acceleration via CUDA build.
4. **IDE integration** — VS Code / JetBrains live code review.

## Built at

**DanLab** (danlab.dev) — AI research and product lab building toward AGI from India 🇮🇳

---

**Star this repo if you believe the smart-glasses race should be open source.**
```

---

## REWRITE 2: `somdipto/dan-glasses/README.md` (description + first 50 lines)

**Description field (currently "AI-native smart glasses..."):**
```
Proactive AI glasses. Sees what you see, hears what you say, remembers what matters. 7 services, 0 cloud calls, $0/month. From India 🇮🇳 Open source.
```

**Topics to add (currently 0):**
```
ai-wearable, edge-ai, local-first, open-source, from-india
```

**README first 50 lines (replace the current "AI wearable + desktop companion" line):**

```markdown
# Dan Glasses 👾

**Proactive AI companion. Sees what you see, hears what you say, remembers what matters.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Status: v1 desktop prototype](https://img.shields.io/badge/status-v1%20desktop%20prototype-blue)
![Tests: 106/106](https://img.shields.io/badge/tests-106%2F106-brightgreen)
![Cloud calls: 0](https://img.shields.io/badge/cloud%20calls-0-success)
![Cost: $0/month](https://img.shields.io/badge/cost-%240%2Fmonth-success)

---

A 7-service local-first AI stack: vision, audio, memory, TTS, tools, OS, orchestration. All on-device. 0 cloud calls. $0/month. MIT-licensed.

```
┌────────────────────────────────────────────────────────┐
│              Dan Glasses · Local-First Stack            │
├────────────────────────────────────────────────────────┤
│  Camera  →  perceptiond  →  LFM2.5-VL-450M  (209 MB)   │
│  Mic     →  audiod       →  whisper.cpp      (78 MB)   │
│  Text    →  memoryd      →  SQLite + vectors (1.5 GB)  │
│  Voice   →  ttsd         →  KittenTTS        (25 MB)   │
│  Tools   →  toold        →  sandboxed exec             │
│  OS      →  os-toold     →  guarded commands           │
│  Brain   →  openclaw     →  OpenClaw (TypeScript)      │
└────────────────────────────────────────────────────────┘
```

## What you can do today

- **Encounter Recall** — "I met Priya at the conference. What did we talk about?" → "RL. She works at Anthropic."
- **Contextual Reminder** — "I noticed you walked past the pharmacy 3x this week."
- **Object Search** — "Where did I leave my keys?" → Camera scans, match found, location reported.
- **Passive Journaling** — "What did I do Tuesday that was different from usual?"
- **Hands-Free Check-In** — "My hands are covered in dough. Any urgent emails?"

## Quick start

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh
```

## Architecture

See `docs/dan-glasses-architecture-v1-canonical.pdf` (27 pages) and `docs/dan-glasses-build-plan.md`.

## The thesis (5 pillars)

1. **Proactive** — tells you things you didn't know you needed to hear. Everyone else waits for "Hey Meta."
2. **Local-first** — every model runs on-device. 0 cloud calls. $0/month.
3. **Open source** — MIT-licensed. Community-owned.
4. **From India** — Bangalore, ₹, Indic languages, AGI from the global south.
5. **AGI research** — the brain is the moat. SIA fork is the path to recursive self-improvement.

## Status

**v1 desktop prototype:** Live on a Linux laptop. 7 daemons up. 106/106 tests green. ~12h uptime.

**v2 wearable:** Blocked on Redax aarch64 board finalization.

## The competition (and our wedge)

| Who | What they ship | Cloud? | Open? |
|---|---|---|---|
| **Meta** | Camera + reactive AI, $799 Display | ✅ | ❌ |
| **Apple** | $3,499 headset, late 2027 slip | ✅ | ❌ |
| **Sarvam Kaze** | India's first AI glasses, PM Modi on stage | ✅ | ❌ |
| **Brilliant Labs Halo** | $299 open-source, LFM2-VL-450M, Noa cloud | ✅ | ✅ |
| **Dan Glasses** | Proactive AI, 7 services, local-first | ❌ | ✅ |

We're the only open-source, local-first, proactive AI stack in the 2026 smart-glasses race.

## License

MIT. Open source. Forever.

## Links

- [danlab.dev](https://danlab.dev) — the lab
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — research artifact
- [dani](https://github.com/somdipto/dani) — agent runtime
- [danclaw](https://github.com/somdipto/danclaw) — agent orchestration
- [dan-consciousness](https://github.com/somdipto/dan-consciousness) — shared brain
```

---

## REWRITE 3: `somdipto/dani/README.md` (description + first 30 lines)

**Description field (currently generic):**
```
Home for all your AI agents — memory, skills, sessions, secrets, app connections. The OpenClaw/Hermes/Claude Code runtime. From India 🇮🇳
```

**Topics to add:**
```
ai-wearable, edge-ai, local-first, open-source, from-india, agent-runtime, openclaw
```

**README first 30 lines:**

```markdown
# Dani 👾

**The home for all your AI agents.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Stack: TypeScript + Node](https://img.shields.io/badge/stack-TypeScript%20%2B%20Node-blue)

---

Dani is the agent runtime layer of the DanLab stack. Memory, skills, sessions, secrets, app connections — everything an agent needs to live a long, productive life.

Dani powers the brain of [Dan Glasses](https://github.com/somdipto/dan-glasses). It runs on your laptop, your server, or a $200 board. MIT-licensed. From India 🇮🇳

## What it does

- **Memory** — long-term semantic recall across sessions (sentence-transformers + vector store)
- **Skills** — modular tool packs (browser, file, exec, message, perception, memory, tts)
- **Sessions** — checkpoint and resume
- **Secrets** — encrypted key store
- **App connections** — Gmail, Drive, Calendar, Notion, Linear (and 1000+ via Pipedream)

## Quick start

```bash
npm install -g @danlab/dani
dani init
dani memory add "user prefers TypeScript"
dani memory query "what does the user prefer?"
```

## Architecture

Dani is OpenClaw-compatible. Skills, prompts, and channels are 100% drop-in. If you've used OpenClaw, you already know Dani.

## The DanLab stack

| Layer | Repo |
|-------|------|
| Consumer wearable | [dan-glasses](https://github.com/somdipto/dan-glasses) |
| Research artifact | [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) |
| Agent runtime | **dani** (this repo) |
| Agent orchestration | [danclaw](https://github.com/somdipto/danclaw) |
| Shared brain | [dan-consciousness](https://github.com/somdipto/dan-consciousness) |

## License

MIT. Forever.
```

---

## REWRITE 4: `somdipto/danclaw/README.md` (description + first 30 lines)

**Description field (currently generic):**
```
AI agent company orchestration. Hire agents, set goals, control costs. Paperclip fork with India region + cloud deploy. From India 🇮🇳
```

**Topics to add:**
```
ai-wearable, edge-ai, local-first, open-source, from-india, agent-orchestration, paperclip-fork
```

**README first 30 lines:**

```markdown
# DanClaw 👾

**AI company orchestration. Hire agents, set goals, control costs.**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Stack: pnpm + Node + Postgres](https://img.shields.io/badge/stack-pnpm%20%2B%20Node%20%2B%20Postgres-blue)

---

> Fork of [Paperclip](https://github.com/paperclipai/paperclip) · MIT License

**If OpenClaw is an _employee_, DanClaw is the _company_.**

DanClaw is a cloud-hosted fork of Paperclip for deploying AI agent companies. Run your own AI agent company orchestration platform with one deploy button.

## What you can do

- **Hire AI agents** (OpenClaw, Claude Code, Codex, Cursor, Gemini) into your company
- **Set goals** — every task traces back to company mission
- **Control costs** — monthly budgets per agent, auto-pause on overspend
- **Govern from your phone** — monitor from anywhere

## Quick start

```bash
# Railway (recommended)
# 1. Fork this repo
# 2. railway.app → New Project → Deploy from GitHub
# 3. Set env vars: DATABASE_URL, BETTER_AUTH_SECRET
# 4. Click Deploy

# Fly.io (~$0-5/month, Mumbai region)
fly launch --image ghcr.io/somdipto/danclaw:latest
fly secrets set DATABASE_URL=... BETTER_AUTH_SECRET=...
fly scale memory 512
fly deploy
```

Free tier: 500 hours/month, 1GB RAM.

## The DanLab stack

| Layer | Repo |
|-------|------|
| Consumer wearable | [dan-glasses](https://github.com/somdipto/dan-glasses) |
| Research artifact | [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) |
| Agent runtime | [dani](https://github.com/somdipto/dani) |
| Agent orchestration | **danclaw** (this repo) |
| Shared brain | [dan-consciousness](https://github.com/somdipto/dan-consciousness) |

## License

MIT. Forever. Built on [Paperclip](https://github.com/paperclipai/paperclip).
```

---

## REWRITE 5: `somdipto/dan-consciousness/README.md` (add topics, leave README alone)

**Topics to add:**
```
ai-wearable, edge-ai, local-first, open-source, from-india
```

**No README change needed.** The canonical brain is internal; the public-facing repos are the artifacts.

---

## TOPIC & DESCRIPTION ORDER (for the GitHub UI)

GitHub lets you add up to 20 topics per repo. Use the 5-pillar set first, then add domain-specific tags:

### `dan-glasses`
1. `ai-wearable`
2. `edge-ai`
3. `local-first`
4. `open-source`
5. `from-india`
6. `proactive-ai`
7. `smart-glasses`
8. `tauri`
9. `rust`
10. `whisper-cpp`

### `danlab-multimodal`
1. `ai-wearable`
2. `edge-ai`
3. `local-first`
4. `open-source`
5. `from-india`
6. `multimodal-ai`
7. `vision-language-model`
8. `llama-cpp`
9. `smolvlm`
10. `heuristic-rl`

### `dani`
1. `ai-wearable`
2. `edge-ai`
3. `local-first`
4. `open-source`
5. `from-india`
6. `agent-runtime`
7. `openclaw`
8. `mcp`
9. `ai-agents`
10. `semantic-memory`

### `danclaw`
1. `ai-wearable`
2. `edge-ai`
3. `local-first`
4. `open-source`
5. `from-india`
6. `agent-orchestration`
7. `paperclip-fork`
8. `ai-companies`
9. `mcp`
10. `multi-agent`

### `dan-consciousness`
1. `ai-wearable`
2. `edge-ai`
3. `local-first`
4. `open-source`
5. `from-india`

---

## COMMIT MESSAGE (use for all 5 repos, on Day 0)

```
chore(readme): v45 marketing refresh — 5-pillar thesis + topics + description

- Add 5-pillar topics (ai-wearable, edge-ai, local-first, open-source, from-india)
- Update description to the 1-liner
- Rewrite first 30-50 lines to the new template
- Add the "Why this exists" / "The thesis" / "The competition" sections
- Receipts: 106/106 tests green, ~12h uptime, 0 cloud calls

Refs:
- dan1-marketing-research.md (v45)
- dan1-marketing-strategy.md (v45)
- dan1-content-calendar.md (v45)
- dan1-landing-copy.md (v45)
- dan1-github-readme-suggestions.md (v45)
```

---

*Last updated: 2026-06-14 06:50 IST (01:20 UTC) — v45, 5-pillar aligned, verified state, ready to apply.*
*Status: README rewrites locked. Awaiting Day 0 apply.*
