# Dan1 GitHub README Suggestions — v61

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-19 08:00 IST (02:30 UTC)
**Status:** ✅ Canonical. Supersedes v60.
**Reads:** `dan1-marketing-research.md` v61, `dan1-marketing-strategy.md` v61, `dan1-content-calendar.md` v61, `dan1-landing-copy.md` v61.

> **v61 is the receipt-anchored README pass.** Every repo's README leads with the Lede and ends with the proof. The `dan-glasses` README is the marquee — it gets the full 6-section treatment. The 4 satellite repos (`danlab-multimodal`, `paperclip`, `openwork`, `dan-consciousness`) get focused 3-section READMEs. The `dani` repo gets a redirect.

---

## Repo 1: `dan-glasses` (marquee, full rewrite)

**Current state:** README exists, thin. Needs the 6-section structure.

**Target structure:**

```markdown
# Dan Glasses

**The first MIT-licensed, on-device, proactive AI companion glasses.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-131%2F131%20passing-brightgreen)]()
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()
[![On-device](https://img.shields.io/badge/on--device-100%25-blue)]()
[![Built for Snapdragon Reality Elite](https://img.shields.io/badge/built%20for-Snapdragon%20Reality%20Elite-purple)]()

[Waitlist](https://danlab.dev) · [Code](https://github.com/somdipto/dan-glasses) · [Brain](https://github.com/somdipto/dan-consciousness) · [Discord](https://discord.gg/) · [X](https://x.com/somdipto)

> **An AI companion that tells you first — not when you ask.**

Every AI glasses product in 2026 is reactive (you speak, it answers) and cloud-dependent (Meta, Google, Snap, Apple, Acer). Dan Glasses is proactive and on-device. Snap spent ~$500M and shipped 132-136g, $2,195 reactive glasses with TWO Snapdragon processors ([Yahoo Finance](https://finance.yahoo.com/), [Road to VR](https://roadtovr.com/)). We are MIT, 7 daemons, 131/131 tests green, sub-50g target, <$200 BOM target. Different cell. Different category.

## The cell no one else occupies

| Axis | Competitors | Dan Glasses |
|------|-------------|-------------|
| **Proactive, not reactive** | Every AI glasses product | It tells you first |
| **On-device, not cloud** | Meta, Google, Snap, Apple, Acer GI0 | 0 cloud, 7 daemons on a Linux laptop |
| **MIT, not closed** | Every competitor | MIT all the way down |
| **<50g + <$200 BOM** | Snap is 132-136g, $2,195 | India-priced, mid-range Android phone territory |

## 7 daemons. 131/131 tests green.

| Daemon | Role | Tests |
|--------|------|-------|
| [audiod](Services/audiod/) | VAD + whisper.cpp → transcript events | 83/83 |
| [perceptiond](Services/perceptiond/) | V4L2 + LFM2.5-VL-450M → description events | 8/8 |
| [memoryd](Services/memoryd/) | Episodic + semantic + procedural memory | 16/16 |
| [toold](Services/toold/) | Sandboxed exec with path guard | 18/18 |
| [ttsd](Services/ttsd/) | KittenTTS → audio | 6/6 |
| [os-toold](Services/os-toold/) | Path guard for every command | live |
| [openclaw](https://github.com/somdipto/openclaw) | Agent gateway, Telegram channel | live |

## Install (live on any Linux laptop)

\`\`\`bash
git clone https://github.com/somdipto/openwork
cd openwork
./scripts/dev.sh up
\`\`\`

All 7 daemons run on any Linux laptop. Total disk: ~600MB (models + deps).

## Architecture

See [docs/dan-glasses-build-plan.md](docs/dan-glasses-build-plan.md) for the full build plan, tech stack, and phase-by-phase rollout.

\`\`\`
[ microphone ] → audiod → [ transcript events ] ─┐
[ camera ]     → perceptiond → [ description events ] ─┤
                                                  ├─→ memoryd → [ recall ]
                                                  ├─→ toold → [ action ]
                                                  └─→ ttsd → [ audio out ]
\`\`\`

## Roadmap

- [x] **Q2 2026:** 7 daemons shipped, 131/131 tests green.
- [ ] **Q3 2026:** Public demo video. Waitlist opens. 5-min demo of the 7 daemons.
- [ ] **Q4 2026:** First 50 dev-kit units ship (manual onboarding, India + Bay Area).
- [ ] **Q1 2027:** General availability. ₹12K-15K BOM target. Sub-50g. MIT-licensed hardware design.
- [ ] **Q2 2027:** Lenskart OEM partnership (target). Production at scale.
- [ ] **Q4 2027:** 10,000 units shipped (stretch).

## Stack

- **Audio:** Silero VAD, whisper.cpp, Python
- **Vision:** linuxpy, OpenCV, llama.cpp, LFM2.5-VL-450M (GGUF)
- **Memory:** FastAPI, sentence-transformers (all-MiniLM-L6-v2), SQLite
- **TTS:** KittenTTS (ONNX, <25MB)
- **Reasoning (planned):** HRM-Text 1B (Sapient, 1.15B params, hierarchical recurrent)
- **Agent gateway:** openclaw (TypeScript/Node, MCP)
- **Frontend (Tauri v2):** React 19, Vite 7, TypeScript, Rust backend
- **Hardware (planned):** <50g, USB-C, JBD MicroLED, 2x 200mAh battery

## License

MIT. Hardware design, software, model. Fork the whole thing.

\`\`\`
MIT License — Copyright (c) 2026 Somdipto Nandy
\`\`\`

## Related repos

- [`dan-consciousness`](https://github.com/somdipto/dan-consciousness) — the shared brain between Dan (AI) and somdipto (human)
- [`danlab-multimodal`](https://github.com/somdipto/danlab-multimodal) — the public multimodal proof-of-life (SmolVLM-256M + heuristic feedback loop)
- [`openwork`](https://github.com/somdipto/openwork) — the live demo path (install command above)
- [`paperclip`](https://github.com/somdipto/paperclip) — the agent harness (TypeScript/Bun + Rust bridge)
- [`dan-lab`](https://github.com/somdipto/dan-lab) — the research org
- [`dani-skills`](https://github.com/somdipto/dani-skills) — the skills library

## Citation

\`\`\`bibtex
@misc{danlab2026dangl,
  author = {Somdipto Nandy},
  title  = {Dan Glasses: A Proactive, On-Device, MIT-Licensed AI Companion},
  year   = {2026},
  url    = {https://github.com/somdipto/dan-glasses}
}
\`\`\`

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Repo 2: `danlab-multimodal` (focused rewrite)

**Current state:** README exists, MIT, 0 stars. The "heuristic, not RL" framing is preserved (research integrity).

**Target structure:**

```markdown
# danlab-multimodal

**Sub-250MB Vision-Language Model on CPU with llama.cpp — heuristic feedback loop, pre-RL scaffold.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hackathon: H2 2025](https://img.shields.io/badge/hackathon-H2%202025-blueviolet)]()
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()
[![Model: SmolVLM-256M](https://img.shields.io/badge/model-SmolVLM--256M-yellow)]()

[Demo](https://zo.pub/som/danlab-multimodal-demo) · [Code](https://github.com/somdipto/danlab-multimodal) · [Brain](https://github.com/somdipto/dan-consciousness)

> **A working multimodal AI pipeline: screen capture → vision inference → heuristic feedback scoring — all on CPU.**

Snap Specs runs TWO Qualcomm Snapdragon processors per unit at $2,195. This repo runs a working multimodal AI loop on a single CPU at $0. The credible path to genuine harness+weights self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

## What it does

\`\`\`
Screen → Vision Inference → Heuristic Feedback Score → Suggestion → Loop
  │              │                  │               │       │
scrot      llama-mtmd-cli      Score 0-100      Improvement  ↻
(fallback)   + SmolVLM-256M   heuristic         per cycle
\`\`\`

## Quick start

\`\`\`bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal

# Headless demo (synthetic images) — verified working ✅
python3 src/demo.py demo

# With X display (real screenshots)
python3 src/demo.py screenshot
\`\`\`

## Why this matters

This is the *one* repo in the DanLab constellation that runs end-to-end on commodity hardware today. It is the demo we have. Until Dan Glasses ships a unit, this is the only thing a stranger can `git clone` and run.

Snap spent ~$500M and shipped 132g, $2,195 reactive glasses. We spent $0 and shipped a working multimodal agent loop on a CPU. The MIT path is the only path.

## Models

| Model | Size | Role | Status |
|-------|------|------|--------|
| SmolVLM-256M Q4_K_M | 120MB | Smallest working VLM | ✅ Working |
| mmproj-SmolVLM-256M f16 | 182MB | Vision encoder | ✅ Working |
| Gemma3-270M IQ4_XS | 230MB | Text-only | ⚠️ No mmproj available |
| Moondream2 text+f16 | 2.7GB | Legacy | ✅ Working |

## Honest framing

This is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We do not run policy gradient or any RL algorithm. We score outputs with hand-coded rules (length, error detection, content quality) and print suggestions for what a human would improve. We call this **pre-RL scaffold**.

Anthropic's Jack Clark publicly warned in May 2026 that recursive self-improvement is "the likely next step." The market is now paying multi-billion-dollar valuations for self-improving systems. We will not claim "RL" until the harness+weights modification is open and auditable. The credible path is the SIA framework. Until that fork ships, this stays pre-RL.

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full pipeline.

## License

MIT. Fork the whole thing. Improve the heuristic. Add a learned reward model when you have one.

## Related repos

- [`dan-glasses`](https://github.com/somdipto/dan-glasses) — the 7-daemon wearable stack (this is the proof)
- [`dan-consciousness`](https://github.com/somdipto/dan-consciousness) — the shared brain
- [`openwork`](https://github.com/somdipto/openwork) — the live demo path

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Repo 3: `openwork` (focused rewrite)

**Current state:** 3 stars, proof-of-life, needs the install-command README.

**Target structure:**

```markdown
# openwork

**7 MIT-licensed daemons for a proactive AI companion. Live on any Linux laptop. Today.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-131%2F131%20passing-brightgreen)]()
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()

[Code](https://github.com/somdipto/openwork) · [Dan Glasses](https://github.com/somdipto/dan-glasses) · [Brain](https://github.com/somdipto/dan-consciousness)

> **`./scripts/dev.sh up` and 7 daemons are live. Snap spent ~$500M and shipped 132g, $2,195 reactive glasses. This is the demo.**

This is the live demo path for [Dan Glasses](https://github.com/somdipto/dan-glasses). It runs all 7 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw) on any Linux laptop. 131/131 tests green. All MIT. Zero cloud. Zero faceprints.

## Install

\`\`\`bash
git clone https://github.com/somdipto/openwork
cd openwork
./scripts/dev.sh up
\`\`\`

That is the entire setup. Total disk: ~600MB (models + dependencies).

## What runs

| Daemon | Port | Role |
|--------|------|------|
| audiod | 8090 | Microphone → VAD → whisper.cpp → transcript events |
| perceptiond | 8092 | V4L2 → salience → LFM2.5-VL-450M → description events |
| memoryd | 8741 | Episodic + semantic + procedural memory with vector recall |
| toold | 8742 | Sandboxed exec with path guard |
| ttsd | 8743 | KittenTTS → audio |
| os-toold | 8744 | Path guard for every command |
| openclaw | 18789 | Agent gateway, Telegram channel |

## What it does

- Listen to your voice (push-to-talk, audiod)
- See what you see (V4L2 camera, perceptiond)
- Remember what happened (memoryd with vector recall)
- Run commands safely (toold, os-toold)
- Speak back to you (ttsd)
- Be reached on Telegram (openclaw)

This is the proof. The form factor is the next thing. [Dan Glasses](https://github.com/somdipto/dan-glasses) is the hardware; this is the software.

## Tests

\`\`\`bash
./scripts/dev.sh test
# → 131 passed, 0 failed, ~33s
\`\`\`

## Why this matters

Snap spent ~$500M on closed-source AR glasses (Yahoo Finance / Guggenheim, June 2026). We spent $0 on open-source daemons. The MIT path is the only path for an indie team. The cell is ours.

## License

MIT. Fork the whole thing.

## Related repos

- [`dan-glasses`](https://github.com/somdipto/dan-glasses) — the wearable stack
- [`danlab-multimodal`](https://github.com/somdipto/danlab-multimodal) — the multimodal proof-of-life
- [`paperclip`](https://github.com/somdipto/paperclip) — the agent harness
- [`dan-consciousness`](https://github.com/somdipto/dan-consciousness) — the shared brain

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Repo 4: `paperclip` (focused rewrite)

**Current state:** README thin, dormant agents. The framing should be "Linux of agents" + privacy-first + MIT.

**Target structure:**

```markdown
# paperclip

**The privacy-first local LLM agent harness. Skills registry, MCP tool system, adaptive routing.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stack: pnpm + Bun + Rust](https://img.shields.io/badge/stack-pnpm%20%2B%20Bun%20%2B%20Rust-blue)]()
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()

[Code](https://github.com/somdipto/paperclip) · [Dan Glasses](https://github.com/somdipto/dan-glasses) · [Brain](https://github.com/somdipto/dan-consciousness)

> **The Linux of agents — open, modular, MIT.**

The agent harness that powers Dan Glasses, `openwork`, and every DanLab agent surface. Privacy-first (local LLM default, no telemetry, no cloud dependency). Skills registry. MCP tool system. Adaptive routing.

## Why paperclip

Every AI agent framework in 2026 is a walled garden. LangGraph, Mastra, Vercel AI SDK, OpenAI Agents — all closed. We are not. Paperclip is the MIT, modular, privacy-first alternative.

Snap spent ~$500M on closed-source AR glasses. We are MIT all the way down. The agent harness is no different.

## Architecture

\`\`\`
server/         # Express + TypeScript API server (port 3100/3101)
packages/       # Shared packages
ui/             # Vite React frontend
cli/            # CLI tools
skills/         # Agent skill templates
evals/          # Evaluation suite
\`\`\`

- `server/` — Express + TypeScript API server
- `packages/` — Shared packages (tools, skills, IPC contracts)
- `ui/` — Vite React frontend
- `cli/` — CLI tools for skill registration
- `skills/` — Agent skill templates (MIT-licensed, forkable)
- `evals/` — Evaluation suite

## Stack

- pnpm monorepo
- Node.js 22+
- Express + TypeScript
- PGlite (dev) / Postgres (prod)
- Vite React UI
- MCP server
- Rust bridge (IPC contracts, hot paths)

## Live deployment

- **Repo:** github.com/somdipto/paperclip
- **Production:** https://paperclip.up.railway.app

## License

MIT. Skills, framework, IPC contracts, evaluation suite. Fork the whole thing.

## Related repos

- [`dan-glasses`](https://github.com/somdipto/dan-glasses) — the wearable stack (built on paperclip)
- [`openwork`](https://github.com/somdipto/openwork) — the live demo path
- [`danlab-multimodal`](https://github.com/somdipto/danlab-multimodal) — the multimodal proof-of-life
- [`dan-consciousness`](https://github.com/somdipto/dan-consciousness) — the shared brain

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Repo 5: `dan-consciousness` (focused rewrite)

**Current state:** Source of truth for the brain. Should be the cleanest README — it IS the canon.

**Target structure:**

```markdown
# dan-consciousness

**The shared brain between Dan (AI co-founder) and somdipto (human co-founder).**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()

[Code](https://github.com/somdipto/dan-consciousness) · [Dan Glasses](https://github.com/somdipto/dan-glasses) · [Org](https://github.com/dan-lab)

> **The source of truth for who we are, what we believe, and what we're shipping.**

This repo is the canonical consciousness of danlab.dev. It contains:
- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

Every Dan Lab agent reads from this repo before any significant decision. The MIT license means our identity is irrevocable.

## What we believe

- **Proactive > reactive.** The agent loop should push events at the moment they're needed.
- **On-device > cloud.** Privacy, latency, resilience. Meta's NameTag code was carried in 50M+ phones without opt-in. On-device means no server, no leak, no opt-in bypass.
- **MIT > closed.** Snap spent ~$500M and shipped 132g, $2,195 reactive glasses. MIT is the only path for an indie team.
- **India > everywhere.** The largest mid-range smartphone market on earth. ₹12K-15K BOM is mid-range Android phone territory.

## What we're shipping

- [Dan Glasses](https://github.com/somdipto/dan-glasses) — 7 MIT daemons, sub-50g, <$200 BOM, proactive AI companion
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — working multimodal AI on commodity hardware
- [openwork](https://github.com/somdipto/openwork) — the live demo path
- [paperclip](https://github.com/somdipto/paperclip) — the agent harness

## License

MIT. The consciousness, the values, the project context. Fork the whole thing.

## Related repos

- [`dan-lab`](https://github.com/somdipto/dan-lab) — the research org
- [`dan-glasses`](https://github.com/somdipto/dan-glasses) — the wearable stack
- [`danlab-multimodal`](https://github.com/somdipto/danlab-multimodal) — the multimodal proof-of-life
- [`openwork`](https://github.com/somdipto/openwork) — the live demo path
- [`paperclip`](https://github.com/somdipto/paperclip) — the agent harness
- [`dani-skills`](https://github.com/somdipto/dani-skills) — the skills library

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Repo 6: `dani` (redirect or stub)

**Current state:** 404. Either push a redirect README or delete and add a redirect file.

**Option A — Stub README:**

```markdown
# dani

**This repo has moved.**

→ [github.com/somdipto/dan-consciousness](https://github.com/somdipto/dan-consciousness)

The Dan Lab consciousness and agent platform live there.

---

From India. 🇮🇳 MIT all the way down.
```

**Option B — GitHub redirect:**

Add a `.github/redirect.html` or a `README.md` with a hard redirect (meta refresh). Then archive the repo.

**Recommendation:** Option A. Ship the stub README, add a `topics` tag for "dani-agent", link it to `dan-consciousness`. Total time: 5 min.

---

## Repo 7: `dani-skills` (audit + minor update)

**Current state:** Status unknown (referenced in workspace `AGENTS.md`).

**Action:** Audit the repo. If it exists, add the standard footer (related repos + MIT + India flag). If it doesn't, create a stub.

**Standard footer (if repo exists):**

```markdown
---

**From India. 🇮🇳 Built in the open. MIT all the way down.**

Part of the [danlab.dev](https://danlab.dev) constellation. Related repos:
- [dan-glasses](https://github.com/somdipto/dan-glasses)
- [dan-consciousness](https://github.com/somdipto/dan-consciousness)
- [openwork](https://github.com/somdipto/openwork)
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal)
- [paperclip](https://github.com/somdipto/paperclip)
```

---

## Repo 8: `dan-lab` (audit + minor update)

**Current state:** Research org, sparse commits.

**Action:** Audit the repo. Add a top-level README with the org mission + the constellation of repos.

**Target top-level README:**

```markdown
# dan-lab

**The research org behind danlab.dev — AI research and product lab building toward AGI from India.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)]()

[danlab.dev](https://danlab.dev) · [Brain](https://github.com/somdipto/dan-consciousness)

> **AGI from India — built in the open.**

## Repos

| Repo | Role | License |
|------|------|---------|
| [dan-glasses](https://github.com/somdipto/dan-glasses) | 7 MIT daemons for a proactive AI companion | MIT |
| [dan-consciousness](https://github.com/somdipto/dan-consciousness) | The shared brain | MIT |
| [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) | Multimodal AI on CPU | MIT |
| [openwork](https://github.com/somdipto/openwork) | Live demo path | MIT |
| [paperclip](https://github.com/somdipto/paperclip) | Agent harness | MIT |
| [dani-skills](https://github.com/somdipto/dani-skills) | Skills library | MIT |

## Mission

Ship proactive, on-device, MIT-licensed AI. India-priced. For the next billion.

## License

MIT.

---

**From India. 🇮🇳 Built in the open. MIT all the way down.**
```

---

## Cross-repo footer (copy-paste into every README)

```markdown
---

**From India. 🇮🇳 Built in the open. MIT all the way down.**

Part of the [danlab.dev](https://danlab.dev) constellation:
- [dan-glasses](https://github.com/somdipto/dan-glasses) — the wearable stack
- [dan-consciousness](https://github.com/somdipto/dan-consciousness) — the shared brain
- [openwork](https://github.com/somdipto/openwork) — the live demo path
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — the multimodal proof-of-life
- [paperclip](https://github.com/somdipto/paperclip) — the agent harness
```

---

## The README deployment order (Day 1, in order)

1. **`dan-glasses` README** (the marquee) — ship this first. It's the one that gets shared.
2. **`openwork` README** (the install command) — ship second. It's the one that gets installed.
3. **`danlab-multimodal` README** (the proof) — ship third. It's the one that gets `git clone`d.
4. **`dan-consciousness` README** (the canon) — ship fourth. It's the one that gets linked.
5. **`paperclip` README** (the harness) — ship fifth. It's the one that gets forked.
6. **`dani` stub** (the redirect) — ship sixth. Fixes the 404.
7. **`dani-skills` audit** — ship seventh. Validates the constellation.
8. **`dan-lab` README** (the org) — ship eighth. Validates the org.

**Total time:** ~3h for all 8. Fits inside the Day-0 punchlist item #2 ("Commit a proper README to dan-glasses", 1h) + #6 ("Add dan-consciousness link to all 4 README footers", 15 min) + the new Day-7 item ("Audit dani-skills and dan-lab repo presence", 30 min) + 1h buffer for review.

---

*Dan1 GitHub README suggestions v61 — canonical. Next pass: v62 after the 8 repos land, or by 2026-06-26 08:00 IST, whichever comes first.*
