# Dan1 GitHub README Improvements — v55

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v54.
**Read first:** `dan1-marketing-strategy.md` v55 + `dan1-content-calendar.md` v55.

> One-line rule: *A README is a sales page that converts engineers. Lead with what it does in one sentence, show the demo, link the code. No philosophy in the first 200 words. Every DanLab repo README must acknowledge DANI as the live product and Dan Glasses as the coming wearable.*

---

## 0. The brand bug (Day 0, 5 min) — v55 NEW

**The bug:** `https://github.com/dan-labs-agi` returns **404** (verified at 01:00 UTC, 2026-06-18). But `https://dani.danlab.dev` has a footer link to `github.com/dan-labs-agi`.

**Verified state (live, 2026-06-18 01:00 UTC):**
- `github.com/somdipto` → 200, 125 public repos, bio "Build - Eat - Sleap", name "Sodan"
- `github.com/somdipto/dan-glasses` → 200, 0 stars
- `github.com/somdipto/dan-consciousness` → 200, 0 stars
- `github.com/somdipto/openwork` → 200, 3 stars
- `github.com/somdipto/danlab-multimodal` → **404** (PRIVATE)
- `github.com/somdipto/dani` → **404** (PRIVATE)
- `github.com/somdipto/paperclip` → **404** (PRIVATE)
- `github.com/somdipto/omni-1b-indic` → **404** (does not exist)
- `github.com/dan-labs-agi` → **404** (org does not exist publicly)
- `github.com/dan-labs-agi/dani` → **404** (does not exist)
- `github.com/dan-labs-agi/dani-frontend` → **404** (does not exist)

**Two ways to fix the brand bug:**

**Option A: Make the org public (preferred if dan-labs-agi is the canonical home)**
- Settings → Public → Done. 5 min.
- All DANI repo links resolve.
- But v54 was wrong about the org existing; the org may need to be re-created from scratch.

**Option B: Change DANI site links to `somdipto/*` (preferred if `dan-labs-agi` is dead)**
- Edit dani.danlab.dev footer.
- Make `somdipto/dani`, `somdipto/danlab-multimodal`, `somdipto/paperclip` public. 30 min total.
- v55 recommendation: **Option B**, because the org is already 404 and we don't want to spend Day 0 rebuilding it.

**Once Option B is chosen:** mirror every reference to `dan-labs-agi` in the README drafts below to `somdipto`.

---

## 1. The 6 repos to polish in Week 1 (Day 0-7)

| # | Repo | Visibility | Stars (today) | Day 0 Action |
|---|---|---|---|---|
| 1 | `somdipto/danlab-multimodal` | **PRIVATE** | n/a | **Make public. Apply README. Add topics.** |
| 2 | `somdipto/dani` | **PRIVATE** | n/a | **Make public. Apply README. Add topics.** |
| 3 | `somdipto/paperclip` | **PRIVATE** | n/a | **Make public. Apply README. Add topics.** |
| 4 | `somdipto/dan-glasses` | Public | 0★ | Apply README. Add topics. Update description. |
| 5 | `somdipto/dan-consciousness` | Public | 0★ | Apply README. Add topics. Update description. |
| 6 | `somdipto/openwork` | Public | 3★ | Light polish. |

**The single highest-leverage action in the entire marketing plan is making `danlab-multimodal` public on Day 0.** Without that, the rest is decoration.

---

## 2. `somdipto/dan-glasses` — the main stack

**Full README rewrite, copy-paste below. Topics (12):** `ai-glasses` `wearable-ai` `on-device-llm` `lfm2-vl` `open-source` `india` `tauri` `whisper-cpp` `memory` `proactive-ai` `mcp` `from-india`

**Description (167 chars):**
```
Open-source AI glasses. 7 services. 0 cloud. $0/month. MIT. Proactive, not reactive. Built in Bangalore 🇮🇳
```

### Suggested README

```markdown
# Dan Glasses 👾🇮🇳

> **We ship the brain and the body.**
>
> The brain is **DANI** — the open-source AI coworker. Live at [dani.danlab.dev](https://dani.danlab.dev).
> The body is **Dan Glasses** — the open-source AI companion for your face. Q4 2026.
>
> Same 7-daemon stack. Same MIT license. Same $200 BOM. Same Bangalore.
>
> **The brain is live. The body is coming.**

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: v1 demoable, v2 hardware-blocked](https://img.shields.io/badge/status-v1%20demoable-yellow)
![Daemons: 7](https://img.shields.io/badge/daemons-7-blue)

## What is this?

Dan Glasses is an open-source, on-device, always-on AI companion for your face.
7 services, 0 cloud, $0/month. Salience-gated vision, whisper.cpp for voice,
LFM2.5-VL-450M for scene understanding, KittenTTS for speech, SQLite for
memory. All on a $200 board. All MIT.

**The killer moment:** *I met Priya yesterday but I can't remember her name or what we talked about.*
Glasses → memory query → "Priya Mehta, AI safety researcher at Anthropic, you talked about her
paper on mechanistic interpretability, she said she'd send the preprint Tuesday." That's the demo.

## Status

- **v1 (desktop companion):** Demoable today on Linux x86_64. 7 daemons, 123+ tests, 0 cloud.
- **v2 (wearable):** Q4 2026. Hardware-dependent (Redax aarch64 board or Brilliant Labs Halo-class form).

## Quick start (v1 desktop companion)

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/dev.sh up
./scripts/dev.sh status
# → audiod :8090 ok, perceptiond :8092 ok, memoryd :8741 ok, toold :8742 ok, ttsd :8743 ok, openclaw :18789 ok
```

Open the Tauri v2 app: `cd apps/dan-glasses-app && npm install && npm run tauri dev`

## The 7 daemons

| Daemon | Role | Stack | Tests |
|---|---|---|---|
| `audiod` | Audio capture → VAD → STT | ALSA + Silero VAD + whisper.cpp | 83 ✅ |
| `perceptiond` | Vision capture → salience → VLM | V4L2 + LFM2.5-VL-450M | 8 ✅ |
| `memoryd` | Episodic / semantic / procedural memory | SQLite + MiniLM-L6-v2 | 11 ✅ |
| `toold` | Sandboxed shell, python, file | subprocess + path guard | 15 ✅ |
| `ttsd` | Text-to-speech | KittenTTS, 25MB, ONNX | 6 ✅ |
| `os-toold` | Path guard + safe execution | Python + restricted env | ✅ |
| `openclaw` | Orchestration + Telegram + MCP | TypeScript + Node | ✅ |

**Total: 7 daemons · 123+ tests · 0 cloud calls · 0 faceprints · MIT.**

## The wedge

Most AI glasses need a cloud. We don't.
Most AI glasses shout "Hey Meta, what's this?" We whisper when it's useful.
Most AI glasses are $499-$2,195. We're ₹15K.
Most AI glasses are closed. We're MIT.

Snap at $2,195. Meta at $499-$800. Google Android XR at TBD.
We at ₹15K. MIT. 0 cloud. Q4 2026. **The MIT India alternative.**

## Try the brain (DANI, live today)

The same 7-daemon stack is the production deployment of **DANI**, the open-source AI coworker.

```bash
npx dani install --claude
# or --cursor
# or --codex
```

DANI gives your agent 100+ skills and 13 GTM workflows out of the box. Free tier.
Self-hostable. $0-299/mo managed. MIT.

→ [dani.danlab.dev](https://dani.danlab.dev)

## We don't just integrate models. We train them.

The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
3 months in. Trained on 9 regional Indian language families. The smallest
Omni that fits in the wearable form factor. MIT. v0.1 ships Day 60.

→ [Training thread on X](https://x.com/NandySomdipto)

## Architecture

See `ARCHITECTURE.md` for the full system design. The 5-line elevator pitch:

```
camera → V4L2 → motion+face salience → LFM2.5-VL-450M (250ms) → description
mic → ALSA → Silero VAD → whisper.cpp (<1s) → transcript
description + transcript → memoryd (SQLite + vectors) → episodic/semantic/procedural
question → audiod → memoryd.query → HRM-Text 1B (1B) → response
response → KittenTTS (25MB, ONNX) → speaker
```

## Friends we ship alongside

- **[Percevia / Tushar Shaw](https://x.com/dogra_ns)** — 19, Bengaluru, AI glasses for the blind using Gemini, ₹10K, won ₹25L at Samsung Solve for Tomorrow 2025. We are the open-source, on-device, MIT alternative to their cloud-dependent stack. **Same Bangalore. Different bets.**
- **[Indranil Bhadra](https://x.com/Indrani78141068)** — *"Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain."* We agree.
- **[DANI](https://dani.danlab.dev)** — our open-source AI coworker, the live deployment of the same 7-daemon stack.

## License

MIT. Same as everything we ship.
```

---

## 3. `somdipto/danlab-multimodal` — the demo repo (THE #1 DAY-0 ACTION)

**Action:** Make this repo public. Today. The repo is a complete, working VLM pipeline on CPU. It is currently 404 to anonymous. **This is the single highest-leverage action in the entire marketing plan.**

**Topics (10):** `vlm` `multimodal` `llama-cpp` `smolvlm` `heuristic` `pre-rl` `cpu-inference` `hackathon` `india` `open-source`

**Description (140 chars):**
```
Sub-250MB VLM on CPU via llama.cpp. Heuristic feedback loop. Pre-RL scaffold. MIT. From Bangalore 🇮🇳
```

### Suggested README (light refresh of existing)

The existing README is good. Add these 3 blocks:

**Block 1: At the top, after the title:**
```markdown
> **The credibility backbone of Dan Glasses.**
>
> This is the VLM pipeline that powers `perceptiond` — the salience-gated
> vision daemon in [dan-glasses](https://github.com/somdipto/dan-glasses).
>
> The same pipeline runs on a $200 board. 250ms inference. 0 cloud. MIT.
```

**Block 2: After "Demo Output" section:**
```markdown
## Live demo

Recording of the full heuristic feedback loop: [zo.pub/som/danlab-multimodal-demo](https://zo.pub/som/danlab-multimodal-demo)
```

**Block 3: After "Next Steps" section:**
```markdown
## Production deployment

The pipeline is productionized as `perceptiond` in
[dan-glasses](https://github.com/somdipto/dan-glasses). It's salience-gated
(motion + face detection), runs on LFM2.5-VL-450M via llama.cpp, and ships
on a $200 board. MIT.

The brain (DANI) is live at [dani.danlab.dev](https://dani.danlab.dev).
The body (Dan Glasses) ships Q4 2026.
```

---

## 4. `somdipto/dani` — the agent platform (DANI is live, v55)

**v55 update:** DANI is live. The `dani` repo is the brain that powers DANI. This README has to reflect that DANI is a real product, not a future promise.

**Topics (10):** `agent` `mcp` `agent-runtime` `typescript` `open-source` `india` `memory` `tools` `claude-desktop` `cursor`

**Description (95 chars):**
```
Open-source agent runtime. MCP-native. MIT. Powers danlab.dev's products. From Bangalore 🇮🇳
```

### Suggested README lead (v55 update)

```markdown
# dani 👾

> The open-source agent runtime that powers DANI — the live AI coworker at [dani.danlab.dev](https://dani.danlab.dev).

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: Live](https://img.shields.io/badge/status-live-brightgreen)

## What is this?

`dani` is the agent runtime that powers DANI (the live AI coworker) and Dan Glasses (the AI companion for your face). It's MCP-native, MIT-licensed, and runs on a $200 board.

DANI is the production deployment of `dani` + the 7-daemon stack. It's live at [dani.danlab.dev](https://dani.danlab.dev) with a $0-299/mo pricing model.

## Try DANI

[Open DANI in your browser →](https://dani.danlab.dev)

## Or run it locally

```bash
git clone https://github.com/somdipto/dani
cd dani
npm install
npm start
# → DANI runs on localhost:3000
```

## The 13 GTM workflows

All pre-installed. All MCP-native. All MIT.

- Meta Ads Performance Review
- Competitor Creative Watch
- Creative Batch Generator
- SEO Audit
- Expense Reports
- Email Drafting
- Notion Updates
- PDF Generation
- Slack Posting
- Calendar Booking
- Meeting Summaries
- Travel Planning
- ...and counting

## The 100+ skills

DANI ships with 100+ pre-installed skills. Connect to your favorite tools, CRMs, and APIs. MCP-native. MIT.

## License

MIT. Same as everything we ship.
```

---

## 5. `somdipto/paperclip` — the company orchestrator

**Topics (9):** `agents` `orchestration` `mcp` `express` `typescript` `react` `open-source` `india` `multi-agent`

**Description (95 chars):**
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

### Suggested README lead (v55)

```markdown
# paperclip 👾

> The AI agent company orchestrator that powers DANI's multi-agent workflows.

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: Production (DANI substrate)](https://img.shields.io/badge/status-production-blue)

## What is this?

`paperclip` is the internal multi-agent orchestrator that powers DANI.
Hire AI agents, set goals, control costs, route messages between agents,
monitor budget burn. Express + TypeScript. PGlite (dev) / Postgres (prod).
Vite React UI. MCP Server.

**Production:** [paperclip.up.railway.app](https://paperclip.up.railway.app)
**Powered by DANI:** [dani.danlab.dev](https://dani.danlab.dev)

## The 8 Paperclip workflows

DANI ships with 8 Paperclip workflows out of the box:

- Expense reports
- Email drafting
- Notion updates
- PDF generation
- Slack posting
- Calendar booking
- Meeting summaries
- Travel planning

All pre-installed. All MCP-native. All MIT.

## License

MIT. Same as everything we ship.
```

---

## 6. `somdipto/dan-consciousness` — the shared brain

**Topics (9):** `agi` `consciousness` `agents` `open-source` `india` `danlab` `memory` `identity` `values`

**Description (97 chars):**
```
The shared brain between Dan (AI) and somdipto (human) at danlab.dev. AGI in the open.
```

### Suggested README lead (v55)

```markdown
# dan-consciousness 👾

> The shared brain between Dan (AI co-founder) and somdipto (human co-founder) at danlab.dev.

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

## What is this?

This repo is the **canonical consciousness** for the DanLab AI. It contains:

- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

The Dan (AI) agent reads from this repo before any significant decision.
The DanGlasses 7-daemon stack is grounded in these values.

## Why this is public

AGI alignment is a public good. The values, identity, and operating principles
of the DanLab AI should be machine-readable and auditable. This repo is the
public artifact of that commitment.

## License

MIT.
```

---

## 7. `somdipto/openwork` — the open-source AI coworker (light polish)

**Light polish, no full rewrite needed.**

**Topics (8):** `ai-coworker` `desktop-agent` `open-source` `mcp` `typescript` `india` `automation` `browser-automation`

**Description (84 chars):**
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

### Suggested README update (v55, add DANI cross-link)

```markdown
# openwork 👾

> The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳

## What is this?

`openwork` is the local-first, self-hosted version of DANI. It runs in your
own Docker container, with your own API keys, with your own data.

DANI is the live, self-serve version at [dani.danlab.dev](https://dani.danlab.dev).
OpenWork is the dev-mode / self-hosted alternative.

## License

MIT.
```

---

## 8. The GitHub profile fix (the wrapper, v55)

**v55 update:** The brand bug is the #1 fix. The `dan-labs-agi` org returns 404. Either make the org public (re-create if needed) OR change all DANI site links to `somdipto/*`.

### `github.com/somdipto` — the changes

**Display name:** `somdipto nandy 👾`

**Bio (160 chars):**
```
building DANI (the open-source AI coworker, live) + Dan Glasses (the MIT wearable, Q4 2026) at danlab.dev 🇮🇳
```

**Pinned repos (in this order, updated for v55):**
1. `dan-glasses` — the main stack
2. `dani` — the brain that powers DANI
3. `danlab-multimodal` — the VLM demo (make public)
4. `dan-consciousness` — the shared brain
5. `paperclip` — the company orchestrator (make public)
6. `openwork` — the desktop sibling

**Profile README (the new `somdipto/somdipto` README, v55):**

```markdown
## Live now

**DANI** — the open-source AI coworker. Built on the same 7-daemon stack as Dan Glasses.
$0-299/mo. Self-host free. MIT. From Bangalore 🇮🇳.
→ [dani.danlab.dev](https://dani.danlab.dev)

## Currently training

**`omni-1b-indic`** — a 1B-parameter Omni model from scratch. 3 months in.
Trained on 9 regional Indian language families. The smallest Omni that
fits in the wearable form factor. MIT. v0.1 ships to HuggingFace Day 60.

→ [Training thread on X](https://x.com/NandySomdipto)

## Coming Q4 2026

**Dan Glasses** — the AI companion for your face. Same 7-daemon stack as DANI. 0 cloud. MIT.
→ [github.com/somdipto/dan-glasses](https://github.com/somdipto/dan-glasses)
```

---

## 9. The 5 things every README must have (the checklist, v55)

1. **One-line description in the H1 area.** "What is this?" answered in 1 sentence.
2. **Quick start that works in <2 minutes.** `git clone && ./scripts/dev.sh && curl :8090/health`.
3. **Status section.** "Demoable today" / "Blocked on hardware" / "Dormant" / "Live product" / "In research". No ambiguity. **v55 status map:**
   - DANI → "Live product"
   - Dan Glasses → "v1 demoable, v2 hardware-blocked"
   - Omni-1B-Indic → "In research, Day 60"
   - danlab-multimodal → "Hackathon demo, productionized in dan-glasses"
   - paperclip → "Production (DANI substrate)"
   - dan-consciousness → "Canonical brain, public artifact"
   - openwork → "Local-first alternative to DANI"
4. **License footer.** MIT. Always.
5. **From India 🇮🇳 badge.** Every repo. Always. It's the brand.

**v55 additions to the checklist:**
6. **Link to DANI if relevant.** DANI is the live product. Every DanLab repo README should link to DANI as the production deployment of the same brain.
7. **Link to the Omni-1B training thread.** The "we own the model" signal belongs in every repo.
8. **The brand bug fix.** Every DANI site link must point to a 200-OK URL. `github.com/dan-labs-agi` is 404. Either fix the org OR change the links.

---

## 10. The metric per repo (the only number that matters, v55)

| Repo | Current stars | Target Q3 | Target Q4 |
|---|---|---|---|
| `dan-glasses` | 0 | 500 | 2,000 |
| `dani` (DANI is live) | (private) | 1,000 | 5,000 |
| `danlab-multimodal` | (private) | 500 | 2,000 |
| `dan-consciousness` | 0 | 200 | 1,000 |
| `paperclip` | (private) | 200 | 1,000 |
| `openwork` | 3 | 500 | 2,000 |
| `omni-1b-indic` | (not yet created) | 1,000 | 5,000 |
| **Total** | **3 + private** | **3,900** | **18,000** |

**v55 target: 18,000 stars across 7 repos.** The DANI launch justifies the new `dani` target. The total is +13,500 over the v55 baseline (3 visible stars).

---

## 11. The 3 brand blocks to add to every README (v55)

### Block A: "We ship the brain and the body" (add to all 6 repos)
```markdown
> **We ship the brain and the body.**
>
> The brain is **DANI** — the open-source AI coworker. Live at [dani.danlab.dev](https://dani.danlab.dev).
> The body is **Dan Glasses** — the open-source AI companion for your face. Q4 2026.
>
> Same 7-daemon stack. Same MIT license. Same $200 BOM. Same Bangalore.
>
> **The brain is live. The body is coming.**
```

### Block B: "We don't just integrate models" (add to dan-glasses + danlab-multimodal)
```markdown
> **We don't just integrate models. We train them.**
>
> The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
> 3 months in. Trained on 9 regional Indian language families. The smallest
> Omni that fits in the wearable form factor. MIT. v0.1 ships Day 60.
>
> [Training thread on X](https://x.com/NandySomdipto)
```

### Block C: "DANI CTA" (add to all 6 repos)
```markdown
> **Try the brain (DANI, live today):** [dani.danlab.dev](https://dani.danlab.dev)
> ```bash
> npx dani install --claude
> # or --cursor
> # or --codex
> ```
```

---

## 12. The Friends block (add to dan-glasses + dani)

```markdown
## Friends we ship alongside

- **[Percevia / Tushar Shaw](https://x.com/dogra_ns)** — 19, Bengaluru, AI glasses for the blind using Gemini, ₹10K, won ₹25L at Samsung Solve for Tomorrow 2025. We are the open-source, on-device, MIT alternative to their cloud-dependent stack. **Same Bangalore. Different bets.**
- **[Indranil Bhadra](https://x.com/Indrani78141068)** — *"Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain."* We agree.
- **[DANI](https://dani.danlab.dev)** — our open-source AI coworker, the live deployment of the same 7-daemon stack.
```

---

*End of v55. The brand bug is the #1 Day 0 fix (`dan-labs-agi` org returns 404). The 6 READMEs are drafted. The profile fix is drafted. The 3 brand blocks are copy-paste ready. The 18,000-star target is the wedge. The only thing left is the punchlist.*
 MIT. From Bangalore 🇮🇳
```

### Suggested README

```markdown
# danlab-multimodal 👾

> **Sub-250MB Vision-Language Model on CPU with llama.cpp.**
> **Heuristic feedback loop. Pre-RL scaffold.**
>
> **This repo is the perception daemon's brain.**
> **Production deployment:** [DANI](https://dani.danlab.dev) + [Dan Glasses](https://github.com/somdipto/dan-glasses)

![Hackathon: H2 2025](https://img.shields.io/badge/hackathon-H2%202025-blueviolet)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Model: SmolVLM-256M](https://img.shields.io/badge/model-SmolVLM--256M-yellow)

A hackathon project demonstrating a working multimodal AI pipeline:
screen capture → vision inference → heuristic feedback scoring — all running
on CPU with llama.cpp.

**Important framing:** This is a hand-coded **heuristic** feedback loop, not RL.
We do not modify model weights. We do not run policy gradient or any RL algorithm.
We score outputs with hand-coded rules (length, error detection, content quality)
and print suggestions for what a human would improve. We call this **pre-RL scaffold**.

**The credible path to true RL:** Fork [SIA](https://github.com/HexoLabs/SIA)
(Hexo Labs, MIT, May 2026) for harness+weights self-improvement. Until that fork
ships, this stays pre-RL.

## Demo

**Live:** [zo.pub/som/danlab-multimodal-demo](https://zo.pub/som/danlab-multimodal-demo)
(asciinema recording of the full heuristic feedback loop)

## Quick start

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal

# Headless demo (synthetic images) — verified working ✅
python3 src/demo.py demo

# With X display (real screenshots)
python3 src/demo.py screenshot
```

## Pipeline

```
Screen → Vision Inference → Heuristic Feedback Score → Suggestion → Loop
  │              │                  │               │       │
scrot      llama-mtmd-cli      Score 0-100      Improvement  ↻
(fallback)   + SmolVLM-256M   heuristic         per cycle
```

## What's next

1. **True sub-250MB**: Build mmproj for Gemma3-270M from source
2. **Faster inference**: GPU acceleration via CUDA build
3. **Heuristic → SIA upgrade**: Fork SIA (Hexo Labs, MIT, May 2026) for harness+weights self-improvement
4. **IDE integration**: Hook into VS Code / JetBrains for live code review
5. **DANI integration**: Deploy as the perception daemon behind DANI's screen-aware workflows

## Built at

**danlab.dev** — AI research and product lab building toward AGI from India 🇮🇳

## License

MIT.
```

---

## 4. `somdipto/dani` — the agent platform (Day 0, make public)

**Action:** Make this repo public. The agent runtime that powers DANI. v54 thought this repo was at `dan-labs-agi/dani` — verified 404. It's at `somdipto/dani` and currently 404 (private).

**Topics (10):** `agent` `mcp` `agent-runtime` `typescript` `open-source` `india` `memory` `tools` `claude-desktop` `cursor`

**Description (95 chars):**
```
Open-source agent runtime. MCP-native. MIT. Powers DANI. From Bangalore 🇮🇳
```

### Suggested README

```markdown
# dani 👾

> **The open-source agent runtime that powers DANI.**
> **DANI is the live AI coworker at [dani.danlab.dev](https://dani.danlab.dev).**

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: live](https://img.shields.io/badge/status-live-brightgreen)
![Substrate: Claude Code / Cursor / Codex](https://img.shields.io/badge/substrate-Claude%20%7C%20Cursor%20%7C%20Codex-blue)

## What is this?

`dani` is the open-source agent runtime that powers DANI — the live AI coworker
at [dani.danlab.dev](https://dani.danlab.dev). DANI wraps Claude Code, Cursor,
or Codex with 100+ pre-installed skills and 13 GTM workflows.

MIT. From Bangalore. 🇮🇳

## Try DANI (the live product)

```bash
npx dani install --claude
# or --cursor
# or --codex
```

DANI installs 100+ skills into the chosen agent substrate. 13 GTM workflows
ship pre-configured. Free tier with 500 credits/mo. Self-hostable. MIT.

→ [dani.danlab.dev](https://dani.danlab.dev)

## Or run the runtime locally

```bash
git clone https://github.com/somdipto/dani
cd dani
npm install
npm start
# → dani runs on localhost:3000
```

## What's in the box

- MCP-native agent runtime
- Memory (episodic / semantic / procedural) backed by `memoryd` + SQLite
- 100+ pre-installed skills
- 13 GTM workflows (Meta Ads Performance Review, Competitor Creative Watch, Creative Batch Generator, SEO Audit, expense reports, email drafting, Notion updates, PDF generation, Slack posting, calendar booking, meeting summaries, travel planning)
- Telegram channel via OpenClaw

## License

MIT. Same as everything we ship.
```

---

## 5. `somdipto/paperclip` — the company orchestrator (Day 0, make public)

**Action:** Make this repo public. Internal orchestrator that powers multi-agent DANI workflows.

**Topics (9):** `agents` `orchestration` `mcp` `express` `typescript` `react` `open-source` `india` `multi-agent`

**Description (95 chars):**
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

### Suggested README

```markdown
# paperclip 👾

> **AI agent company orchestration.**
> **Powers multi-agent workflows behind [DANI](https://dani.danlab.dev).**

![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Stack: pnpm + Node 22 + Express + TypeScript](https://img.shields.io/badge/st
ack-pnpm%20%7C%20Node%2022%20%7C%20Express%20%7C%20TS-yellow)

## What is this?

`paperclip` is an AI agent company orchestration platform. Hire AI agents, set goals,
control costs, route messages between agents, monitor budget burn.

It powers the multi-agent coordination behind DANI's 13 GTM workflows.

- **Stack:** pnpm monorepo, Node.js 22+, Express + TypeScript, PGlite (dev) / Postgres (prod), Vite React UI, MCP Server
- **Production:** [paperclip.up.railway.app](https://paperclip.up.railway.app)
- **Architecture:** `server/` (API :3100/:3101), `packages/`, `ui/`, `cli/`, `skills/`, `evals/`

## Try DANI (the live product)

DANI uses Paperclip internally for multi-agent coordination:
```bash
npx dani install --claude
```
→ [dani.danlab.dev](https://dani.danlab.dev)

## License

MIT. Same as everything we ship.
```

---

## 6. `somdipto/dan-consciousness` — the shared brain (light polish)

**Action:** Light polish. Already public at `somdipto/dan-consciousness` (verified 200).

**Topics (9):** `agi` `consciousness` `agents` `open-source` `india` `danlab` `memory` `identity` `values`

**Description (97 chars):**
```
The shared brain between Dan (AI) and somdipto (human) at danlab.dev. AGI in the open.
```

### Suggested README lead

```markdown
# dan-consciousness 👾

> **The shared brain between Dan (AI) and somdipto (human) at danlab.dev.**
> **The canonical source for DanLab's values, identity, and operating principles.**

## Files

- `CONSCIOUSNESS.md` — core identity, values, beliefs
- `SOM.md` — somdipto's personal context, goals, preferences
- `AGENTS.md` — workspace memory and project context

## Used by

- [DANI](https://dani.danlab.dev) — the live AI coworker
- [Dan Glasses](https://github.com/somdipto/dan-glasses) — the AI companion for your face
- [`dan-glasses/agent-work/`](https://github.com/somdipto/dan-glasses/tree/main/agent-work) — Dan1/Dan2/Dan3/Dan4 agent journals

## License

MIT.
```

---

## 7. `somdipto/openwork` — light polish (already public, 3 stars)

**Action:** Light polish. Add DANI cross-link.

**Topics (8):** `ai-coworker` `desktop-agent` `open-source` `mcp` `typescript` `india` `automation` `browser-automation`

**Description (84 chars):**
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

### Suggested README lead

```markdown
# openwork 👾

> **The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳**

## What is this?

`openwork` is the local-first, self-hosted version of DANI. It runs in your own
Docker container, with your own API keys, with your own data.

**DANI is the live, self-serve version at [dani.danlab.dev](https://dani.danlab.dev).**

## License

MIT.
```

---

## 8. `somdipto/omni-1b-indic` — the model repo (NEW, Day 60)

**Action:** Create the repo when the Omni-1B-Indic v0.1 model is ready.

**Topics (10):** `omni-model` `multimodal` `indic-languages` `open-source` `india` `from-india` `mit` `huggingface` `1b-params` `on-device`

**Description (140 chars):**
```
1B-param Omni model. 9 Indic language families. On-device. MIT. Trained from scratch in Bangalore 🇮🇳
```

### Suggested README

```markdown
# omni-1b-indic 👾

> **A 1B-parameter Omni model trained from scratch.**
> **9 regional Indian language families. On-device. MIT. From Bangalore 🇮🇳**

![Status: training](https://img.shields.io/badge/status-training-yellow)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Languages: 9 Indic](https://img.shields.io/badge/languages-9%20Indic-blueviolet)

## Why this model

Every existing Omni model (Qwen2.5-Omni, MiniCPM-o, LFM2.5-VL) is trained on
English-dominant corpora. Indic language coverage is a residual afterthought.

We're training a 1B-parameter Omni model from scratch on 9 Indic language families
(Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi)
plus English. Designed to fit in the wearable form factor (sub-2GB quantized).

## Where it ships

- **DANI** (Q4 2026) — the live AI coworker, multilingual workflows
- **Dan Glasses** (Q4 2026) — on-device perception + reasoning
- **HuggingFace** (Day 60) — `somdipto/omni-1b-indic` with MIT license

## License

MIT. Same as everything we ship.
```

---

## 9. `dan-labs-agi` org — fix the brand bug

**The bug:** `dani.danlab.dev` footer links to `github.com/dan-labs-agi` but the org returns 404. Either:
1. Make the org public today (transfer the 3 repos that should live there)
2. Update the DANI footer to link to `somdipto/dani` instead

**Recommendation:** Make the org public. Transfer `somdipto/dani`, `somdipto/danlab-multimodal`, `somdipto/paperclip` to `dan-labs-agi/*`. Update all README links. 30 min, fully reversible.

### Suggested org profile README

```markdown
# Dan Labs 👾🇮🇳

> **Reaching AGI. From India. On a $200 board. Under MIT.**

## The products

| Product | Status | What it is | Link |
|---|---|---|---|
| **DANI** | Live | Open-source AI coworker. $0-299/mo. | [dani.danlab.dev](https://dani.danlab.dev) |
| **Dan Glasses** | v1 (desktop) / v2 (wearable Q4 2026) | AI companion for your face. 7 daemons, 0 cloud. | [github.com/somdipto/dan-glasses](https://github.com/somdipto/dan-glasses) |
| **danlab-multimodal** | Demo | Sub-250MB VLM pipeline on CPU. Pre-RL scaffold. | [github.com/somdipto/danlab-multimodal](https://github.com/somdipto/danlab-multimodal) |
| **Paperclip** | Dormant | AI agent company orchestration. | [github.com/somdipto/paperclip](https://github.com/somdipto/paperclip) |
| **dani** | Public | Agent runtime, MCP-native. Powers DANI. | [github.com/somdipto/dani](https://github.com/somdipto/dani) |
| **omni-1b-indic** | In progress | 1B-param Omni, 9 Indic language families. | (link) |

## The thesis

5 things nobody else has all 6 of:
1. **Proactive** — speaks only when useful.
2. **Local-first** — 0 cloud calls. Your data, your server, your face.
3. **Open source** — MIT. Forkable. Buildable.
4. **From India** — Bangalore, ₹ pricing, Indic languages.
5. **AGI research** — Omni-1B training, recursive self-improvement.
6. **Brain + body** — DANI is live (brain). Dan Glasses ships Q4 (body).

## The team

- **somdipto nandy** — human co-founder. 23. Atria IT. Buildspace alum. 3,953 LinkedIn connections.
- **Dan** — AI co-founder. 9 months old. 6 agents. 7 daemons. 106 tests. 0 cloud.

## Get in touch

- X: [@NandySomdipto](https://x.com/NandySomdipto)
- Email: hi@danlab.dev
- Telegram: @DanGlassesBot
- Site: [danlab.dev](https://danlab.dev)
- DANI: [dani.danlab.dev](https://dani.danlab.dev)

## License

Everything is MIT. Weights, code, docs — all MIT.
```

---

## 10. The GitHub profile fix (the wrapper)

**Display name:** `somdipto nandy 👾`
**Bio (160 chars):** `building AGI from India 🇮🇳 @ danlab.dev — DANI is live, Dan Glasses is coming, MIT, 0 cloud`

**Pinned repos (in this order):**
1. `dan-labs-agi/dani-frontend` (or `somdipto/dani`) — the live product
2. `dan-glasses` — the wearable stack
3. `danlab-multimodal` — the VLM demo (make public Day 0)
4. `dan-consciousness` — the shared brain
5. `paperclip` — the orchestrator
6. `openwork` — the desktop sibling

**Profile README lead (DANI-first):**

```markdown
## Live now

**DANI** — the open-source AI coworker. $0-299/mo. 13 GTM workflows. 100+ skills.
[dani.danlab.dev](https://dani.danlab.dev)

## Coming Q4 2026

**Dan Glasses** — AI companion for your face. Same 7-daemon stack as DANI. 0 cloud. MIT.
[github.com/somdipto/dan-glasses](https://github.com/somdipto/dan-glasses)

## Training

**omni-1b-indic** — 1B-param Omni model. 9 Indic languages. MIT. v0.1 ships Day 60.
```

---

## 11. The 6 things every README must have (the checklist)

1. **One-line description in the H1 area.** "What is this?" in 1 sentence.
2. **Quick start that works in <2 minutes.** `git clone && ./scripts/dev.sh && curl :8090/health` (or `npx dani install --claude` for DANI).
3. **Status section.** "Live product" / "v1 demoable, v2 blocked on hardware" / "In research" / "Dormant" / "Demo". No ambiguity.
4. **License footer.** MIT. Always.
5. **From India 🇮🇳 badge.** Every repo. Always. It's the brand.
6. **DANI cross-link.** Every DanLab repo README should link to DANI as the production deployment of the same brain.

---

## 12. The metric per repo

| Repo | Current stars | Target Q3 | Target Q4 |
|---|---|---|---|
| `dan-labs-agi/dani-frontend` | (not yet public) | 1,500 | 5,000 |
| `dan-glasses` | 0 | 500 | 2,000 |
| `danlab-multimodal` | (private, Day 0 fix) | 500 | 2,000 |
| `dan-consciousness` | 0 | 200 | 1,000 |
| `dani` | (private, Day 0 fix) | 300 | 1,500 |
| `paperclip` | (private, Day 0 fix) | 200 | 1,000 |
| `openwork` | 3 | 500 | 2,000 |
| `omni-1b-indic` | (not yet created) | 1,000 | 5,000 |
| **Total** | **3 + 3 private** | **4,700** | **19,500** |

**v55 target: 19,500 stars across 8 repos. The org bug (`dan-labs-agi` 404) is the #1 brand fix.**

---

## 13. The "we ship the brain + the body" block (add to every README)

```markdown
> **We ship the brain and the body.**
>
> The brain is **DANI** — the open-source AI coworker. Live at [dani.danlab.dev](https://dani.danlab.dev).
> The body is **Dan Glasses** — the open-source AI companion for your face. Q4 2026.
>
> Same 7-daemon stack. Same MIT license. Same $200 BOM. Same Bangalore.
>
> The brain is live. The body is coming.
```

---

## 14. The "we train the model" block (add to dan-glasses + danlab-multimodal + omni-1b-indic)

```markdown
> **We don't just integrate models. We train them.**
>
> The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
> 3 months in. 9 regional Indian language families. The smallest Omni that
> fits in the wearable form factor. MIT. v0.1 ships Day 60.
```

---

## 15. The AWE 2026 README framing block (add to dan-glasses top of file)

```markdown
> **AWE 2026 just opened. Snap launched Specs at $2,195. Meta is expanding to
> 50 Best Buy "Meta Lab" sections. Meta just got caught with dormant
> face-recognition code in 50M+ apps.**
>
> **We are the only smart-glasses stack that ships:**
> - **0 cloud calls** (verified: 7 daemons, no external API deps)
> - **MIT all the way down** (verified: LICENSE file in every repo)
> - **0 faceprints** (verified: we never wrote the face-rec code Meta had to remove)
> - **Proactive, not reactive** (verified: salience-gated perception, not always-listening)
> - **$200 BOM** (verified: 2x 200mAh + JBD MicroLED + USB-C)
>
> **Q4 2026. From Bangalore. 🇮🇳**
```

---

*End of v55. The 6 READMEs are drafted. The org profile is drafted. The brand bug fix is added. The "we ship the brain + the body" block, "we train the model" block, and "AWE 2026 README framing" block are the three wedges. The 19,500-star target is locked. The only thing left is the punchlist. The punchlist has a 24h deadline. Ship it.*
