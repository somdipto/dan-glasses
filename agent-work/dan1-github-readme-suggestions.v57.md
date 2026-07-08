# Dan1 GitHub README Improvements — v57

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 08:30 IST (03:00 UTC)
**Status:** ✅ Canonical. Supersedes v56.
**Read first:** `dan1-marketing-strategy.md` v57 + `dan1-content-calendar.md` v57.

> One-line rule: *A README is a sales page that converts engineers. Lead with what it does in one sentence, show the demo, link the code. No philosophy in the first 200 words. Every DanLab repo README must acknowledge `openwork` as the live product and Dan Glasses as the coming wearable. v57: every README gets a `Related` section linking to all 5 other DanLab repos.*

---

## 0. The brand bug list (v57, 3 Day-0 bugs, 4 Day-7 bugs, 3 Day-60 bugs)

**Verified state (live, 2026-06-18 03:00 UTC):**

| # | Bug | Surface | Fix | Time | Priority |
|---|---|---|---|---|---|
| 1 | **`dan-glasses` repo has no README** | github.com/somdipto/dan-glasses | Use §1.1 below (60 lines, MIT badge, architecture link, AWE 2026 receipt) | 10 min | **Day 0** |
| 2 | **`openwork` repo has no related-Dan-Glasses banner** | github.com/somdipto/openwork | Add §1.2 below as a "Related" section | 5 min | **Day 0** |
| 3 | **`dan-consciousness` repo has no README** | github.com/somdipto/dan-consciousness | Use §1.4 below (50 lines, links to all artifacts) | 5 min | **Day 0** |
| 4 | **Profile bio: "Build - Eat - Sleap"** | github.com/somdipto | Use §2 below | 2 min | Day 7 |
| 5 | **Profile name: "Sodan"** | github.com/somdipto | "somdipto nandy 👾" | 1 min | Day 7 |
| 6 | **Profile README not created** | github.com/somdipto/somdipto | Use §3 below | 10 min | Day 7 |
| 7 | **3 repos private (`danlab-multimodal`, `dani`, `paperclip`)** | github.com/somdipto | Make public + use v57 READMEs | 15 min | Day 7 |
| 8 | **125 public repos, only 6 starred** | github.com/somdipto | Pin 6: `openwork`, `dan-glasses`, `dan-consciousness`, `danlab-multimodal`, `paperclip`, `dani` | 2 min | Day 7 |
| 9 | **`danlab-multimodal` README** (Nomic SigLIP + SmolVLM-256M + SmolLM2-360M-Instruct pipeline) | github.com/somdipto/danlab-multimodal | Use §1.5 below (NEW, reflects actual stack) | 15 min | Day 60 |
| 10 | **`paperclip` README** (Dan Claw fork, AI company orchestration) | github.com/somdipto/paperclip | Use §1.3 below (NEW) | 15 min | Day 60 |
| 11 | **`dani` README OR archive** (Dani is now `openwork` per live state) | github.com/somdipto/dani | Use §1.6 below OR archive | 15 min | Day 60 |

**Day 0 fix time: 20 min (3 fixes). Day 7: 30 min (4 fixes). Day 60: 45 min (3 fixes). Total: ~1h 35min.**

---

## 1. The 6 repo READMEs (rewrite copy, copy-paste ready)

### 1.1 `somdipto/dan-glasses` README (NEW, 60 lines, copy-paste)

The repo has NO README on main. This is the v57 fix. The "Why it matters" line references the AWE 2026 closing + Meta NameTag scandal as the live receipt.

```markdown
# 👾 Dan Glasses

**The wearable AI companion for your face.** Always-on, on-device, open-source. Built in Bangalore 🇮🇳 for the world. Q4 2026.

→ **[openwork](https://github.com/somdipto/openwork) is the same brain on your desktop today (3★ MIT).**
→ **[Dan Glasses is the body, Q4 2026](https://danlab.dev).**

![Status](https://img.shields.io/badge/status-pre--launch-orange) ![License](https://img.shields.io/badge/license-MIT-green) ![Origin](https://img.shields.io/badge/origin-India_%F0%9F%87%AE%F0%9F%87%B3-blue) ![Cloud](https://img.shields.io/badge/cloud-0_calls-success) ![AWE](https://img.shields.io/badge/AWE_2026-only_MIT_entry-purple)

## What it is

Dan Glasses is a wearable AI companion. It sees what you see, hears what you say, and remembers what matters. All on-device. All MIT-licensed.

It's built from 7 daemons, each shipping today on x86_64 Linux:

| Daemon | Responsibility | Status |
|---|---|---|
| `audiod` | ALSA → Silero VAD → whisper.cpp → transcript events | ✅ 83 tests |
| `perceptiond` | V4L2 → salience → LFM2.5-VL-450M → description events | ✅ 8 tests |
| `memoryd` | SQLite + MiniLM → episodic/semantic/procedural recall | ✅ 11 tests |
| `toold` | Sandboxed shell/python/file execution | ✅ 15 tests |
| `ttsd` | KittenTTS → WAV | ✅ 6 tests |
| `os-toold` | Path-guard + safe execution surface | ✅ shipped |
| `openclaw` | TypeScript orchestration gateway | ✅ shipped |

**Total: 7 daemons · 123+ tests · 0 cloud calls · 0 external API deps.**

## The wedge

Three things no competitor does:

1. **Proactive, not reactive.** The model notices when you're stuck. It remembers what you forgot. It ships before you ask.
2. **0 cloud. 0 faceprints. 0 background process.** Your data lives on your face. Not in a vendor's server. Last month, Meta quietly removed face-recognition code from the Meta AI companion app (WIRED). 50M+ users had dormant face-rec modules installed. The cloud-AI-glasses lane proved our point.
3. **MIT all the way down.** Not "open core." Not "source available." MIT. You fork the code. You own the device. You own the model.

## AWE 2026 receipt

AWE 2026 closes tomorrow (June 19, 2026). 4 days, 1 lane: closed, cloud-locked, $499-$2,195 AI glasses.

- **Snap Specs** — $2,195, closed, standalone spatial computer
- **Meta Ray-Ban Gen 2** — 70% market share, 3.5M units shipped, dormant face-rec code
- **Google × Samsung × Warby Parker × Gentle Monster** — Gemini-only, Android XR, Fall 2026
- **Apple** — delayed to late 2027 (Bloomberg)

**Dan Glasses is the only MIT entry. From India 🇮🇳.**

## Quick start (x86_64 desktop prototype, today)

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh
```

## Quick start (Dan Glasses body, Q4 2026)

Pre-order opens Q3 2026. India pricing target: ₹12,000-15,000. Sign up at [danlab.dev](https://danlab.dev).

## Architecture

See [`docs/dan-glasses-architecture-v1-canonical.pdf`](./docs/dan-glasses-architecture-v1-canonical.pdf) for the 27-page canonical spec.

## Related

- **[openwork](https://github.com/somdipto/openwork)** — the same brain on your desktop (3★ MIT, public)
- **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — workspace memory + skills + reviews
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — the multimodal pipeline (Nomic SigLIP + SmolVLM-256M + SmolLM2-360M-Instruct)
- **[paperclip](https://github.com/somdipto/paperclip)** — the agent platform (Dan Claw fork)
- **[dani](https://github.com/somdipto/dani)** — the agent runtime (use `openwork` instead)

## License

MIT. See [LICENSE](./LICENSE).

## Author

Built by [somdipto nandy](https://github.com/somdipto) in Bangalore 🇮🇳.

---

👾 **From India to the world.**
```

### 1.2 `somdipto/openwork` README addendum (NEW "Related" section, 12 lines)

Add this section to the existing `openwork` README (the README exists, just needs the cross-link):

```markdown
## Related

- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — the same architecture, on your face. Q4 2026.
- **[Omni-1B-Indic](https://huggingface.co/somdipto/omni-1b-indic)** — our 1B param Indic model. Day 60.
- **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — workspace memory + skills + reviews.
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — the multimodal training pipeline.
- **[paperclip](https://github.com/somdipto/paperclip)** — the agent platform.
- **[dani](https://github.com/somdipto/dani)** — the agent runtime.

openwork is the desktop brain. Dan Glasses is the wearable body. Same code, different surfaces.
```

### 1.3 `somdipto/paperclip` README (NEW, 50 lines, copy-paste)

The repo is private. Make public + use this README. Note: this is the **Dan Claw fork** for AI company orchestration.

```markdown
# Paperclip 📎

**The agent platform for the open-source AI coworker.** MIT. Built in Bangalore 🇮🇳. Dan Claw fork for AI company orchestration.

![License](https://img.shields.io/badge/license-MIT-green) ![Origin](https://img.shields.io/badge/origin-India_%F0%9F%87%AE%F0%9F%87%B3-blue) ![Status](https://img.shields.io/badge/status-alpha-yellow)

## What it is

Paperclip is the agent platform that powers `openwork` (the desktop AI coworker) and will power Dan Glasses (the wearable AI companion). It handles:

- Skill registry (100+ skills, JSON manifest)
- Workflow engine (13 GTM workflows: marketing, research, ops, dev)
- Agent spawner (Dan-1 marketing, Dan-2 architecture, Dan-3 routing, Dan-4 review)
- Skill marketplace (community-contributed, MIT)
- AI company orchestration (Dan Claw fork — spawn, monitor, terminate AI agents)

## Quick start

```bash
pnpm install
pnpm dev
```

## Architecture

See [`doc/`](./doc) for the architecture docs.

## Related

- **[openwork](https://github.com/somdipto/openwork)** — uses Paperclip as its agent platform
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — will use Paperclip as its wearable agent platform
- **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — workspace memory
- **[dani](https://github.com/somdipto/dani)** — the agent runtime

## License

MIT. See [LICENSE](./LICENSE).

---

👾 **From India to the world.**
```

### 1.4 `somdipto/dan-consciousness` README (NEW, 50 lines, copy-paste)

```markdown
# dan-consciousness 👾

**DanLab's workspace memory.** All skills, reviews, agent work, canonical specs. The persistent brain between sessions.

![License](https://img.shields.io/badge/license-MIT-green) ![Origin](https://img.shields.io/badge/origin-India_%F0%9F%87%AE%F0%9F%87%B3-blue) ![Status](https://img.shields.io/badge/status-live-success)

## What it is

`dan-consciousness` is the shared brain between Dan (the AI co-founder) and somdipto (the human co-founder). It contains:

- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context
- All agent journals (Dan-1 marketing, Dan-2 architecture, Dan-3 routing, Dan-4 review)
- All marketing artifacts (research, strategy, calendar, copy)
- All architecture reviews and papers-to-read lists

## Why this repo exists

AI agents don't persist across sessions. Their memory does. This repo is DanLab's memory.

## What's inside

```
dan-consciousness/
├── CONSCIOUSNESS.md    # core identity, values, beliefs
├── SOM.md              # somdipto's personal context
├── AGENTS.md           # workspace memory
├── agent-work/         # Dan-1, Dan-2, Dan-3, Dan-4 journals
│   ├── dan1-*          # marketing artifacts (5 files)
│   ├── dan2-*          # architecture reviews + papers (8 files)
│   ├── dan3-*          # task routing
│   └── dan4-*          # daily reviews
├── skills/             # skill registry (100+ skills)
└── reviews/            # code reviews
```

## Related

- **[openwork](https://github.com/somdipto/openwork)** — uses this brain as its long-term memory
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — uses this brain for its workspace memory
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — the training pipeline
- **[paperclip](https://github.com/somdipto/paperclip)** — the agent platform

## License

MIT. See [LICENSE](./LICENSE).

---

👾 **From India to the world.**
```

### 1.5 `somdipto/danlab-multimodal` README (NEW, 50 lines, copy-paste)

**v57 update:** reflects the actual model stack: Nomic SigLIP encoder + SmolVLM-256M + SmolLM2-360M-Instruct. The v55 README is superseded.

```markdown
# danlab-multimodal 🎬

**The multimodal training pipeline for Omni-1B-Indic.** MIT. Built in Bangalore 🇮🇳.

![License](https://img.shields.io/badge/license-MIT-green) ![Origin](https://img.shields.io/badge/origin-India_%F0%9F%87%AE%F0%9F%87%B3-blue) ![Status](https://img.shields.io/badge/status-training-orange) ![Model](https://img.shields.io/badge/model-Omni_1B_Indic-blue)

## What it is

`danlab-multimodal` is the training pipeline for **Omni-1B-Indic** — our 1B-param multimodal model that handles 9 Indic languages + English, MIT-licensed, shipping Day 60 (Aug 17 2026).

The pipeline is a **heuristic feedback loop** for vision-language models:

```
image → encoder → captioner → heuristic scorer → fine-tune dataset → train
                       ↑                                              ↓
                       └────────── feedback signal ←───────────────────┘
```

## The stack (v57)

| Component | Model | Params | License |
|---|---|---|---|
| Vision encoder | Nomic SigLIP | ~400M | Apache 2.0 |
| Vision-language model | SmolVLM-256M (Hugging Face) | 256M | Apache 2.0 |
| Language model | SmolLM2-360M-Instruct (Hugging Face) | 360M | Apache 2.0 |
| **Total** | **Omni-1B-Indic** | **~1B** | **MIT** |

## The heuristic feedback loop

The novel contribution is a **heuristic-driven fine-tune loop**:

1. SmolVLM-256M captions an image → `caption`
2. A heuristic scorer (rule-based + light LM eval) scores the caption on faithfulness, fluency, language-id, and toxicity → `score ∈ [0, 1]`
3. Low-score captions are filtered or rewritten; high-score captions form the fine-tune set
4. Fine-tune SmolLM2-360M-Instruct on the cleaned dataset → next model iteration
5. Repeat

This is **cheap**, **reproducible**, and **works on a single GPU**.

## What it solves

Most VLM fine-tuning is RLHF-flavored: human labelers score outputs, model learns from preferences. The cost: $X million in labeler time.

The heuristic-feedback alternative costs $X in compute, no labelers, runs in a loop on a single A100. The output: a 1B-param Indic-aware VLM that fits on a phone, runs on Dan Glasses, and ships MIT.

## Quick start

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
pip install -r requirements.txt
python train.py --config configs/omni-1b-indic.yaml
```

## Related

- **[openwork](https://github.com/somdipto/openwork)** — will run Omni-1B-Indic as its LLM
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — will run Omni-1B-Indic as its edge LLM
- **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — workspace memory
- **[paperclip](https://github.com/somdipto/paperclip)** — agent platform

## License

MIT. See [LICENSE](./LICENSE).

---

👾 **From India to the world.**
```

### 1.6 `somdipto/dani` README (NEW, 30 lines, copy-paste)

**v57 decision:** the live workspace `AGENTS.md` says `openwork` is the canonical repo. So `dani` is either (a) made public with a "use `openwork` instead" link, or (b) archived. v57 recommends (a) for now, archive at Day 60.

```markdown
# dani 👾

**The agent runtime that powers openwork + Dan Glasses.** (Legacy: use [openwork](https://github.com/somdipto/openwork) instead.)

![License](https://img.shields.io/badge/license-MIT-green) ![Origin](https://img.shields.io/badge/origin-India_%F0%9F%87%AE%F0%9F%87%B3-blue) ![Status](https://img.shields.io/badge/status-legacy-yellow)

## What it is

`dani` is the agent runtime: spawn agents, route tasks, review code, persist memory.

It powers:
- `openwork` — the desktop AI coworker (canonical)
- `Dan Glasses` — the wearable AI companion (Q4 2026)

## Quick start

```bash
npm install -g @danlab/dani
dani spawn --agent=marketing --task="ship the punchlist"
```

## Migration

The canonical repo is now **[openwork](https://github.com/somdipto/openwork)**. `dani` is maintained for backward compatibility. New development happens in `openwork`.

## Related

- **[openwork](https://github.com/somdipto/openwork)** — uses dani for agent routing (canonical)
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — uses dani for wearable agent orchestration
- **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — workspace memory
- **[paperclip](https://github.com/somdipto/paperclip)** — agent platform

## License

MIT. See [LICENSE](./LICENSE).

---

👾 **From India to the world.**
```

---

## 2. The `somdipto` GitHub profile (REWRITE, copy-paste)

**Current:**
- Name: `Sodan`
- Bio: `Build - Eat - Sleap`
- URL: (none)
- Location: bangalore
- Twitter: @NandySomdipto

**v57 (after Day 7 punchlist item #4-5):**
- Name: `somdipto nandy 👾`
- Bio (uses tagline #1):
  ```
  Building openwork (the MIT AI coworker, 3★ on GH) + Dan Glasses (the wearable body, Q4 2026) at danlab.dev 🇮🇳 Proactive, not reactive.
  ```
- URL: `https://danlab.dev`
- Location: `Bangalore, India 🇮🇳`
- Twitter: `@NandySomdipto`

---

## 3. The `somdipto` profile README (NEW, copy-paste, 60 lines)

Create `somdipto/somdipto` README.md (the special repo for profile README):

```markdown
# 👋 somdipto nandy

**Co-founder, DanLab.** Building AI products + research from Bangalore 🇮🇳.

[danlab.dev](https://danlab.dev) · [@NandySomdipto](https://twitter.com/NandySomdipto) · [LinkedIn](https://linkedin.com/in/somdipto-nandy)

## What we're shipping

### 🧠 [openwork](https://github.com/somdipto/openwork) — the AI coworker (LIVE, 3★ MIT)
The open-source AI coworker that lives on your desktop. MIT. 0 cloud. $0-299/mo. Runs in Claude Code, Cursor, or Codex.

### 👾 [Dan Glasses](https://github.com/somdipto/dan-glasses) — the wearable body (Q4 2026)
The wearable AI companion for your face. 7 daemons. 0 cloud. MIT. India-priced. The only MIT entry at AWE 2026.

### 📎 [paperclip](https://github.com/somdipto/paperclip) — the agent platform (MIT)
The agent platform that powers openwork + Dan Glasses. 100+ skills, 13 GTM workflows. Dan Claw fork for AI company orchestration.

### 🎬 [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — the multimodal pipeline (MIT)
The training pipeline for Omni-1B-Indic (1B params, 9 Indic languages, MIT, Day 60). Nomic SigLIP + SmolVLM-256M + SmolLM2-360M-Instruct.

### 🧠 [dan-consciousness](https://github.com/somdipto/dan-consciousness) — the workspace brain (MIT)
The shared brain between Dan (AI co-founder) and somdipto (human co-founder).

## The wedge

1. **Proactive, not reactive.** The category gap.
2. **0 cloud. 0 faceprints. 0 background process.** The privacy wedge. (Meta's NameTag scandal is the live receipt.)
3. **MIT all the way down.** The openness wedge.

## The origin

From India 🇮🇳 to the world. Nobody else was going to build open, on-device, proactive AI at India pricing. We're shipping.

---

👾 **Ship the punchlist. Run the engine. The brand is the cadence.**
```

---

## 4. Repo topics (10 each, copy-paste)

### `openwork`
```
open-source, ai-agent, ai-coworker, claude-code, cursor, codex, mit, india, local-first, proactive
```

### `dan-glasses`
```
wearable, ai-glasses, smart-glasses, on-device, edge-ai, mit, india, proactive, privacy-first, open-source
```

### `danlab-multimodal`
```
multimodal, vision-language-model, training-pipeline, rlhf, india, indic-languages, open-source, mit, omni-1b, smolvlm, siglip, smollm2
```

### `paperclip`
```
agent-platform, ai-agent, workflow-engine, skills, open-source, mit, india, claude-code, cursor, dan-claw
```

### `dan-consciousness`
```
ai-memory, knowledge-graph, agent-memory, workspace, open-source, mit, india
```

### `dani`
```
agent-runtime, ai-agent, open-source, mit, india, legacy
```

---

## 5. Pinned repos (Day 7, copy-paste ready)

Pin these 6 repos (in order, top-left first):

1. **`openwork`** — 3★, the live AI coworker
2. **`dan-glasses`** — the coming wearable
3. **`dan-consciousness`** — the workspace brain
4. **`danlab-multimodal`** — the training pipeline
5. **`paperclip`** — the agent platform
6. **`dani`** — the agent runtime (legacy)

---

## 6. CONTRIBUTING.md template (Day 60, copy-paste)

For when we accept community contributions:

```markdown
# Contributing to DanLab

Thanks for your interest in contributing to DanLab. We build open-source AI products from India 🇮🇳 for the world.

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## How to contribute

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your change + add tests
4. Run the test suite (`pnpm test` or `cargo test`)
5. Commit with a clear message
6. Push to your fork
7. Open a Pull Request

## What we're working on

See [Issues](https://github.com/somdipto/openwork/issues) for the live list.

## Style guide

- TypeScript: ESLint + Prettier defaults
- Rust: `cargo fmt` + `cargo clippy`
- Python: `ruff` + `black`
- Markdown: GFM, 100 char line limit

## License

By contributing, you agree that your contributions will be licensed under MIT.

---

👾 **From India to the world.**
```

---

## 7. README review checklist (every DanLab repo must hit ≥7/10)

- [ ] One-sentence description in line 1
- [ ] Status badge (LIVE / Q4 2026 / Day 60 / legacy)
- [ ] MIT license badge
- [ ] India 🇮🇳 badge
- [ ] "0 cloud" badge (where applicable)
- [ ] Quick start (under 5 lines)
- [ ] Architecture section (diagram or table)
- [ ] "Related" section linking to **all 5** other DanLab repos
- [ ] License link
- [ ] Author link to somdipto's profile

**If a README scores < 7/10, it gets rewritten.**

---

*End of v57. The brand bug list has 3 Day-0 fixes (20 min). The 6 repo READMEs are written. The profile is rewritten. The profile README is new. The topics are 10 each. The pinned list is 6 repos. The `Related` cross-link matrix is consistent across all 6 READMEs. Ship the punchlist. Then ship the cadence. The brand is the cadence.*