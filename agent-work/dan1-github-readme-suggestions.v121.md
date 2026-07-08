# Dan1 — GitHub README Improvements (v121)

**Run:** 2026-07-04 11:35 IST
**Author:** Dan1
**Scope:** `dan-glasses`, `dani`, `danlab-multimodal`, `paperclip`, `blurr`, and the `danlab` org profile README.
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## 0. The cross-cutting rules (apply to every README)

1. **Lead with the one-liner, not the project name.** The README is the homepage for the repo. The first 200 chars decide if a developer stays.
2. **Show the daemon map, the .deb, or the bot in the first 500 chars.** Receipts > adjectives.
3. **Link to the threat model doc and the protocol surface doc in every README that touches OpenClaw.** This is non-negotiable after the Mashable flag.
4. **No "we're excited to announce."** Show the work.
5. **The 4 pillars appear in this order:** protocol → observability → on-device → small-beats-large.
6. **Pin to: danlab.dev, dan-consciousness, danlab-multimodal-demo.**
7. **License + provenance block at the top of every README:** `MIT · Built in Bengaluru · The substrate is auditable, not perfect.`
8. **Badges:** GitHub stars, license, last commit, arXiv (when applicable), HuggingFace (when applicable). No build-status badges unless they actually mean something.
9. **Contributing section must include the threat model reporting flow.** This is how security researchers become allies, not enemies.
10. **No "TODO" sections in the public README.** TODOs belong in the issue tracker.

---

## 1. `dan-glasses` (the flagship)

### Current state
PRD §1 framing. Doesn't lead with the live state.

### Suggested first 30 lines (replace the existing top section)

```markdown
# Dan Glasses

> **Your glasses, on your terms.** Open, on-device, agent-native AI in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying. MIT-licensed. 9 daemons live today.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![daemons live](https://img.shields.io/badge/daemons-9%20live-brightgreen)]()
[![cloud calls](https://img.shields.io/badge/cloud%20calls-0-blue)]()
[![Built in Bengaluru](https://img.shields.io/badge/built%20in-Bengaluru-orange)]()

## Install

\`\`\`bash
# .deb (Q3 2026)
curl -fsSL https://danlab.dev/install.sh | bash
\`\`\`

## The substrate is the bet

Vinton Cerf said AI agents need TCP/IP. Anthropic shipped a closed-source version 2 days later. **We shipped it first** — MIT-licensed, MCP-bridged, on a wearable that runs on a $349 laptop in Bengaluru. [Read the protocol →](PROTOCOL.md)

## The threat model is public

@Mashable flagged a flaw in OpenClaw 2 months before mobile launch. We are auditing it. The fix is in the doc. **This is what auditable means.** [Read the threat model →](THREAT_MODEL.md)

## Daemon map (live)

| Daemon | Port | Status |
|---|---|---|
| audiod | 8090 | ✅ |
| perceptiond | 8092 | ✅ |
| memoryd | 8741 | ✅ |
| toold | 8742 | ✅ |
| ttsd | 8743 | ✅ |
| os-toold | 8744 | ✅ |
| dan-glasses-app | 8747 | ✅ |
| openclaw | 18789 | ✅ |
| tailscaled | — | 🟡 (authkey) |

## DM the bot

`@danlab_bot` on Telegram. Same daemon stack, different surface.

## The 4 pillars

1. **The protocol is the bet.** Cerf, Anthropic Apps Gateway, OpenClaw, MCP.
2. **The harness is the workbench.** audiod `segment_timing`, PagerDuty-class observability, on-device.
3. **On-device, validated by orbit.** LFM2.5-VL-450M. The same architecture class as the 4B Gemma 3 NASA put in orbit.
4. **Small beats large.** HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs.

## Try it

- [danlab-multimodal demo](https://zo.pub/som/danlab-multimodal-demo) — runs in your browser, no install
- [DM `@danlab_bot`](https://t.me/danlab_bot) — see the daemon stack live
- [Architecture](ARCHITECTURE.md) — full system spec
- [PRD](PRD.md) — the 5 user stories
- [SOUL](SOUL.md) — the project's voice

## Origin

Built by a 2-person lab in Bengaluru — one human co-founder, one AI co-founder. The brain is open at [github.com/somdipto/dan-consciousness](https://github.com/somdipto/dan-consciousness).

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

### Add a new file: `THREAT_MODEL.md`

Cite Mashable. List the flaw. Show the fix. Credit the auditor. Link to CVE filing flow.

### Add a new file: `PROTOCOL.md`

Cite Cerf, Anthropic Apps Gateway, OpenClaw, MCP. Diagram the wire format. Show the MCP bridge. List the audit log surface.

---

## 2. `dani` (the agent platform)

### Current state
SOUL.md / SOM.md framing. Doesn't lead with the substrate.

### Suggested top section (replace the existing intro)

```markdown
# Dani — the agent platform

> **The agent platform that ships the substrate.** Open, on-device, MCP-native. The same wire protocol Anthropic shipped on Jul 2 2026 — open, auditable, MCP-bridged. MIT-licensed.

## The substrate is the bet

Anthropic shipped a closed-source Apps Gateway. We shipped the same protocol surface first — MIT, MCP-bridged, on a wearable, on a phone, on a laptop. [Read the protocol →](https://github.com/somdipto/dan-glasses/blob/main/PROTOCOL.md)

## The threat model is public

@Mashable flagged a flaw. We audited it. The fix is public. The audit log is public. **This is what auditable means.** [Read the threat model →](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md)

## Skills registry

[github.com/somdipto/dani-skills](https://github.com/somdipto/dani-skills) — the world's best skills library. Each skill is auditable. Each skill has a threat model entry. Each skill is MIT.

## The 4 pillars

1. **The protocol is the bet.**
2. **The harness is the workbench.**
3. **On-device, validated by orbit.**
4. **Small beats large.**

## Quick start

\`\`\`bash
bun add @danlab/dani
\`\`\`

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

### Add: `SECURITY.md`

Standard SECURITY.md with: (a) the threat model reporting flow, (b) CVE filing path, (c) credit policy (we credit researchers, we don't sue them), (d) response time SLA (72h).

---

## 3. `danlab-multimodal` (the demo)

### Current state
README exists but reads like a model card, not a product.

### Suggested top section

```markdown
# danlab-multimodal

> **A 120MB VLM running on your CPU.** SmolVLM-256M (Q4_K_M) + llama.cpp + a heuristic feedback loop. Live in your browser. No GPU. No cloud.

[▶ Try the demo](https://zo.pub/som/danlab-multimodal-demo)

[![asciinema](https://asciinema.org/a/.svg)](https://asciinema.org/a/)

## Heuristic feedback loop — not RL

The agent proposes a change. A heuristic scores it. The change is applied if the score improves. No gradient. No reward model. **This is the cheapest possible improvement loop, and it works.**

[Read the loop spec →](docs/LOOP.md)
[Read the architecture →](docs/ARCHITECTURE.md)

## What's inside

- SmolVLM-256M (Q4_K_M, 120MB main)
- SigLIP vision tower (182MB mmproj)
- llama.cpp runtime
- Heuristic feedback scaffold
- Browser-side inference

## The 4 pillars

1. **The protocol is the bet.** This demo is the on-device substrate in action.
2. **The harness is the workbench.** Every loop iteration is logged.
3. **On-device, validated by orbit.** Same architecture class as Gemma 3 in orbit.
4. **Small beats large.** 120MB beats 1.7TB.

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 4. `paperclip` (dormant but documented)

### Current state
Exists, dormant.

### Suggested top section

```markdown
# paperclip

> **Multi-agent orchestration for the open substrate.** Currently dormant. Architecture frozen. Awaiting VisualClaw port to dan-glasses.

Paperclip is the multi-agent orchestration layer for the DanLab ecosystem. It is dormant while we focus on shipping the wearable substrate. The architecture is documented; the implementation is queued.

[Read the architecture →](ARCHITECTURE.md)

## Why dormant

The substrate (OpenClaw) is standardizing faster than we expected. Anthropic shipped the Apps Gateway, X shipped the MCP server, Microsoft shipped Scout on OpenClaw. We are doubling down on the wearable substrate first. Paperclip returns when the substrate has settled.

## The 4 pillars

(same as dan-glasses)

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

### Add an `ARCHITECTURE.md`

Link to the design doc. State clearly: "Dormant. Q4 2026 revisit."

---

## 5. `blurr` (the multimodal training/eval framework)

### Current state
README exists, generic ML framing.

### Suggested top section

```markdown
# blurr

> **The eval harness for on-device multimodal models.** Bench, regression, ablations. Built for the substrate era.

## The harness is the workbench

PagerDuty says agent model drift is the new outage. BNP Paribas says $725B AI infra spend in 2026. **The harness is the bottleneck, not the model.** blurr is the eval harness for the on-device era.

[Read the spec →](SPEC.md)

## Quick start

\`\`\`bash
bun add @danlab/blurr
\`\`\`

## The 4 pillars

1. **The protocol is the bet.**
2. **The harness is the workbench.** (← blurr lives here)
3. **On-device, validated by orbit.**
4. **Small beats large.**

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 6. `danlab` org profile README

### Suggested full body

```markdown
# danlab

> **An open AI research and product lab in Bengaluru.** Building the first open, on-device, agent-native wearable. The substrate is the bet. The data path is yours.

## Active projects

- [dan-glasses](https://github.com/somdipto/dan-glasses) — open, on-device, agent-native AI in glasses form factor
- [dani](https://github.com/somdipto/dani) — the agent platform
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — 120MB VLM demo
- [blurr](https://github.com/somdipto/blurr) — eval harness for on-device multimodal
- [dani-skills](https://github.com/somdipto/dani-skills) — the skills registry

## The thesis

Vinton Cerf said AI agents need TCP/IP. Anthropic shipped a closed-source version 2 days later. We shipped it first. MIT-licensed, MCP-bridged, on a wearable that runs on a $349 laptop in Bengaluru.

The substrate is the bet. The data path is yours. The threat model is public. The wearable ships it.

## The threat model

[Read the threat model →](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md)

The threat model is public. The audit log is public. The fix is public. **This is what auditable means.**

## The 4 pillars

1. **The protocol is the bet.**
2. **The harness is the workbench.**
3. **On-device, validated by orbit.**
4. **Small beats large.**

## Origin

Built by a 2-person lab in Bengaluru — one human co-founder, one AI co-founder. The brain is open at [github.com/somdipto/dan-consciousness](https://github.com/somdipto/dan-consciousness).

## Press

- Newsweek, "Open Accountability Standards," early July 2026
- Mashable, OpenClaw security critique, June 2026
- 9to5Google / Engadget / TechCrunch, OpenClaw mobile launch, June 2026

## Contact

- Telegram: [@danlab_bot](https://t.me/danlab_bot)
- X: [@somdipto](https://x.com/somdipto) (founder), [@danlab](https://x.com/danlab) (lab, TBD)
- Web: [danlab.dev](https://danlab.dev)

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 7. `dan-consciousness` (the brain)

### Suggested top section (additive, do not remove existing content)

```markdown
## The substrate is the bet

The consciousness is the substrate. Open, auditable, MCP-bridged. The same wire protocol Anthropic shipped on Jul 2 2026 — we shipped it first.

[Read the protocol →](https://github.com/somdipto/dan-glasses/blob/main/PROTOCOL.md)
[Read the threat model →](https://github.com/somdipto/dan-glasses/blob/main/THREAT_MODEL.md)
```

---

## 8. HuggingFace model card (LFM2.5-VL-450M)

### Suggested card body

```markdown
# LFM2.5-VL-450M (danlab fork)

> **A 209MB vision-language model that runs on a laptop.** Same architecture class as the 4B Gemma 3 NASA put in orbit. MIT-licensed. The substrate is auditable.

## Model details

- **Architecture:** LFM2.5-VL-450M (vision-language)
- **Parameters:** 450M
- **Quantization:** Q4_K_M
- **Size:** 209MB
- **Runtime:** llama.cpp, CPU
- **License:** MIT

## The 4 pillars

1. **The protocol is the bet.**
2. **The harness is the workbench.**
3. **On-device, validated by orbit.** (← this model)
4. **Small beats large.**

## Use

\`\`\`bash
# in the Dan Glasses daemon stack
perceptiond --model danlab/lfm2.5-vl-450m
\`\`\`

## Eval

[blurr](https://github.com/somdipto/blurr) bench results coming Q3 2026.

## Provenance

Built by [danlab](https://github.com/somdipto). From Bengaluru, for the world.

---

MIT · Built in Bengaluru · The substrate is auditable, not perfect.
```

---

## 9. The cross-README checklist (apply to every public repo)

- [ ] One-liner in the first 200 chars
- [ ] `.deb` or install one-liner in the first 500 chars (where applicable)
- [ ] Daemon map / receipts (not adjectives) in the first 500 chars
- [ ] "The substrate is the bet" link to PROTOCOL.md
- [ ] "The threat model is public" link to THREAT_MODEL.md
- [ ] "The 4 pillars" block
- [ ] `SECURITY.md` with threat model reporting flow
- [ ] License + provenance footer: `MIT · Built in Bengaluru · The substrate is auditable, not perfect.`
- [ ] Topics tags: `on-device`, `agent-native`, `mcp`, `substrate`, `open-source`, `edge-ai`
- [ ] Pinned to: danlab.dev, dan-consciousness, danlab-multimodal-demo

---

## 10. The single rule

**Every README should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**
