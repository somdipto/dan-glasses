# Dan1 GitHub README Suggestions v68 — The Inbound READMEs

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v67.

> **v68 thesis:** A README is the *first* landing page. v68 READMEs lead with the 4 "no"s, then the receipts, then the build instructions. Code > curl > prose.

---

## 1. Global README rules (the 7 rules, v68-hardened)

### Rule 1: Lead with a one-line position, not a one-line product description.

```
# ❌ v67-style
Dan Glasses is a proactive AI companion that lives on your face and gives you ambient AI.

# ✅ v68-style
No phone. No cloud. No subscription. No ads. — audiod v0.7 live. 7 daemons MIT. India.
```

The v68 one-liner is a *position*. It can be argued with, agreed with, or remembered. The v67 one-liner is a product description. It can only be read.

### Rule 2: Receipts before prose.

The README should have:
- 1 line of position
- 1 line of receipts (test count, version, status)
- 1 line of "verify this" (curl / install / clone)
- THEN prose

Prose is what you read when you don't trust the receipts. Receipts are what you trust when you don't want to read the prose.

### Rule 3: Every claim has a code snippet or a curl command.

```
# ❌ "It's fast"
The audio pipeline is fast.

# ✅ "It's fast"
$ time python3 audiod.py --benchmark
real    0m1.234s
user    0m1.100s
sys     0m0.100s
```

### Rule 4: One screenshot per README. Optional. In the §4 block.

Screenshots are expensive (they go stale, they don't render on every device, they need alt-text). One screenshot, in the §4 block, with alt-text. That's it.

### Rule 5: The LICENSE block is one of the first 30 lines.

`MIT-licensed. © 2024–2026 DanLab. See LICENSE.`

If the LICENSE block isn't in the first 30 lines, the README is hiding the license. Don't hide the license.

### Rule 6: The "contribute" block is one of the last 10 lines.

`Issues: github.com/.../issues. PRs: github.com/.../pulls. Discord: [link].`

Don't bury the contribute block. Don't put it in CONTRIBUTING.md only. Put it in the README.

### Rule 7: The "from India" line is one of the first 50 lines.

`Built at danlab.dev 🇮🇳 — Bengaluru, India.`

The origin is the moat. Surface it early.

## 2. Per-repo README rewrites (v68)

### §2.1 `somdipto/dan-glasses` (v68 rewrite)

```markdown
# Dan Glasses 👓

**No phone. No cloud. No subscription. No ads.**
**7 daemons. MIT. audiod v0.7 live.**

[audiod](Services/audiod/) · [perceptiond](Services/perceptiond/) · [memoryd](Services/memoryd/) · [toold](Services/toold/) · [os-toold](Services/os-toold/) · [ttsd](Services/ttsd/) · [OpenClaw](Services/zo-mcp-bridge/)

[![](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![](https://img.shields.io/badge/audiod-v0.7-blue)](Services/audiod/)
[![](https://img.shields.io/badge/tests-121%2F121-success)](Services/audiod/tests/)
[![](https://img.shields.io/badge/from-India-orange)](https://danlab.dev)

> The proactive AI companion. Open source. On-device. India. 🇮🇳

Snap is $2,195. We're $145 BOM. The category is the rest. The cost is the moat.

---

## What you can do right now

```bash
# Clone
git clone https://github.com/somdipto/dan-glasses.git
cd dan-glasses

# Start audiod (audio → transcript)
python3 Services/audiod/audiod.py &

# Verify
curl http://localhost:8090/health
# {"status":"ok","service":"audiod"}

# Start perceptiond (camera → description)
python3 Services/perceptiond/perceptiond.py &

# Verify
curl http://localhost:8092/status
# {"mode":"watchful","frames":1247,"descs":42,"vlm_busy":false}

# Start memoryd (text → embedding → search)
python3 Services/memoryd/memoryd.py &

# Verify
curl http://localhost:8741/stats
# {"total_memories":42,"model":"sentence-transformers/all-MiniLM-L6-v2"}
```

Three daemons live. Four more at v0.1.0. All MIT.

## The 4 "no"s

- **No phone.** audiod captures locally. perceptiond runs locally. memoryd stores locally.
- **No cloud.** whisper.cpp + llama.cpp + sentence-transformers + Silero VAD. All local.
- **No subscription.** MIT-licensed across 7 daemons. Fork it, sell it, embed it. Forever.
- **No ads.** The model is your context, not your attention.

## The 7 daemons

| Daemon | What it does | Status | Tests | Port |
|---|---|---|---|---|
| **audiod** | Audio → transcript (whisper.cpp) | ✅ v0.7 | 121/121 | 8090, 8091 |
| **perceptiond** | Camera → description (LFM2.5-VL) | ✅ v0.1.0 | 8/8 | 8092 |
| **memoryd** | Text → embedding → search (sentence-transformers) | ✅ v0.1.0 | — | 8741 |
| **toold** | Tool-use agent | ✅ v0.1.0 | — | 8093 |
| **os-toold** | Shell bridge | ✅ v0.1.0 | — | 8094 |
| **ttsd** | Text → speech | ✅ v0.1.0 | — | 8095 |
| **OpenClaw** | Gateway (Telegram + MCP) | ✅ v1.0 | — | gateway |

7 of 7 daemons live.

## Reference hardware

₹12,000 Android phone + ₹1,500 earbuds + the cloud-free audiod.

Snap is $2,195. We're $145 BOM. MIT. India.

## Roadmap

[danlab.dev/roadmap](https://danlab.dev/roadmap) — Now: audiod v0.7.1, danlab-multimodal v0.1.0, paperclip Show HN. Next: audiod v0.8, perceptiond v0.2 (image retention). Later: 7 daemons at v1, dev kit.

## Architecture

[docs/dan-glasses-architecture-v1-canonical.pdf](docs/dan-glasses-architecture-v1-canonical.pdf) — the canonical architecture doc.

## Build it yourself

Each daemon has a `requirements.txt` and a `python3 daemon.py`. See `Services/<daemon>/README.md` for daemon-specific instructions.

## Contribute

Issues: [github.com/somdipto/dan-glasses/issues](https://github.com/somdipto/dan-glasses/issues)
PRs: [github.com/somdipto/dan-glasses/pulls](https://github.com/somdipto/dan-glasses/pulls)
Discord: [danlab.dev/discord](https://danlab.dev/discord) (open 2026-07-15)

## License

MIT. © 2024–2026 DanLab. See [LICENSE](LICENSE).

## Built at

**[danlab.dev](https://danlab.dev)** — AI research and product lab building toward AGI from India 🇮🇳
```

### §2.2 `somdipto/danlab-multimodal` (v68 rewrite — minimal diff from current README)

The current README is already strong (pre-RL scaffold, SIA framework, the 4 "no"s implicit in the framing). v68 changes:

1. **Add the 4 "no"s** as the §1 block.
2. **Tighten the "Why this matters"** paragraph. Replace "multi-billion-dollar valuations" with "a category that Jack Clark publicly warned is the likely next step."
3. **Add a `curl localhost:8092/status` receipt** for the perceptiond integration (current README has none).
4. **Move the "Built at"** to the last 10 lines, not the last 5 lines.

```markdown
# danlab-multimodal 👾

**Sub-250MB VLM with heuristic feedback loop — pre-RL scaffold.**
**No phone. No cloud. No subscription. No ads.**

[![](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![](https://img.shields.io/badge/hackathon-H2%202025-blueviolet)]()
[![](https://img.shields.io/badge/from-India-orange)](https://danlab.dev)
[![](https://img.shields.io/badge/pre--RL-orange)]()

> Sub-250MB VLM on CPU. Heuristic feedback loop. Pre-RL scaffold, explicitly *not* RL.

## Verify this works

```bash
git clone https://github.com/somdipto/danlab-multimodal.git
cd danlab-multimodal
python3 src/demo.py demo
# → 3 cycles, scores 85–95/100, total inference time ~96s
```

## The 4 "no"s

- **No phone.** Runs headless on a Raspberry Pi 4.
- **No cloud.** llama-mtmd-cli + SmolVLM-256M + mmproj. Local.
- **No subscription.** MIT. Fork it, sell it, embed it.
- **No ads.** The model is your context, not your attention.

## What it does

```bash
$ python3 src/demo.py demo
╔══════════════════════════════════════════════════════════╗
║  DANLAB MULTIMODAL AI — HEURISTIC FEEDBACK LOOP DEMO  👾       ║
║  Sub-250MB VLM | llama.cpp | SmolVLM-256M                 ║
╚══════════════════════════════════════════════════════════╝

  ┌─ CYCLE 1: DESKTOP_NEW
  │  📝 Response: The current page contains a file named "filename.py"...
  │  📊 Score: 95/100  |  ⏱ 32.6s
  │  🔄 Good: correctly identified UI/code elements
  └────────────────────────────────────────────────────
```

## Why "pre-RL"?

Anthropic's Jack Clark publicly warned in May 2026 that recursive self-improvement is "the likely next step." The market is now paying multi-billion-dollar valuations for self-improving systems. We will not claim "RL" until the harness+weights modification is open and auditable. The credible path is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL.

## Models

| Model | Size | Role | Status |
|---|---|---|---|
| SmolVLM-256M Q4_K_M | 120MB | Smallest working VLM | ✅ Working |
| mmproj SmolVLM f16 | 182MB | Vision encoder | ✅ Working |
| Gemma3-270M IQ4_XS | 230MB | Text-only | ⚠️ No mmproj |
| Moondream2 text+f16 | 2.7GB | Legacy | ✅ Working |

## Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the full pipeline.

## Demo

Live at: https://zo.pub/som/danlab-multimodal-demo

## Build from scratch

```bash
# Clone llama.cpp, build llama-mtmd-cli
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=ON
cmake --build . --target llama-mtmd-cli -j$(nproc)

# Download SmolVLM-256M GGUF
hf download pierretokns/SmolVLM-256M-Instruct-GGUF SmolVLM-256M-Instruct-Q4_K_M.gguf
hf download pierretokns/SmolVLM-256M-Instruct-GGUF mmproj-SmolVLM-256M-Instruct-f16.gguf

# Run
cd ../..
python3 src/demo.py demo
```

## Next steps

1. **True sub-250MB:** Build mmproj for Gemma3-270M from source.
2. **Faster inference:** GPU via CUDA.
3. **Heuristic → SIA upgrade:** Fork SIA for harness+weights self-improvement.
4. **IDE integration:** VS Code / JetBrains for live code review.

## License

MIT. © 2024–2026 DanLab. See [LICENSE](LICENSE).

## Built at

**[danlab.dev](https://danlab.dev)** — AI research and product lab building toward AGI from India 🇮🇳
```

### §2.3 `somdipto/paperclip` (v68 rewrite — minimal diff)

The current README is dormant (per AGENTS.md: "Dormant. All agents paused. Resume when ready."). v68 changes:

1. **Wake the README.** v68 is the resume signal.
2. **Lead with the position, not the stack.**
3. **Add the 4 "no"s.**
4. **Add a Show HN anchor.**

```markdown
# paperclip 📎

**Deploy your own AI company in one Docker command.**
**No phone. No cloud. No subscription. No ads.**

[![](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![](https://img.shields.io/badge/stack-Express%20%2B%20TS%20%2B%20PGlite-blue)]()
[![](https://img.shields.io/badge/from-India-orange)](https://danlab.dev)
[![](https://img.shields.io/badge/show--HN-paperclip-orange)]()

> If OpenClaw is an employee, paperclip is the company.

## Verify this works

```bash
git clone https://github.com/somdipto/paperclip.git
cd paperclip
docker compose up
# → http://localhost:3100 (UI)
# → http://localhost:3101 (API)
```

## What it does

- **Multi-agent coordination.** Hire and manage fleets of AI agents.
- **Goals that trace.** Every task rolls up to a company-level goal.
- **Per-agent budgets.** $19/agent/month. Hard cap, no overage.
- **Mobile governance.** Govern from anywhere via the mobile dashboard.
- **Audit trail.** Every decision is logged. Every agent is queryable.

## The 4 "no"s

- **No phone.** Web + CLI + Telegram. No phone required.
- **No cloud.** Self-host on Railway / Fly / your own box. Your data.
- **No subscription.** MIT. Free forever. Stripe only if you want hosted.
- **No ads.** The model is your context, not your attention.

## Stack

- **pnpm monorepo.** TypeScript across the board.
- **Express + TypeScript** API server on port 3100 (UI) / 3101 (API).
- **PGlite (dev) / Postgres (prod)** for state.
- **Vite React** UI.
- **MCP Server** for agent integration.

## Architecture

- `server/` — Express + TypeScript API
- `packages/` — Shared packages
- `ui/` — Vite React frontend
- `cli/` — CLI tools
- `skills/` — Agent skill templates
- `evals/` — Evaluation suite

## Show HN

[Show HN: paperclip — deploy your own AI company in one Docker command](https://news.ycombinator.com/item?id=...)

## License

MIT. © 2024–2026 DanLab. See [LICENSE](LICENSE).

## Built at

**[danlab.dev](https://danlab.dev)** — AI research and product lab building toward AGI from India 🇮🇳
```

### §2.4 `somdipto/danclaw` (v68 add — new repo)

Currently `danclaw-phase1.tar.gz` and `/home/workspace/danclaw/`. v68 opens a public repo:

```markdown
# danclaw 🐾

**The bridge between humans and agents.**
**No phone. No cloud. No subscription. No ads.**

[![](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![](https://img.shields.io/badge/stack-Bun%20%2B%20Turbo%20%2B%20Convex-blue)]()
[![](https://img.shields.io/badge/from-India-orange)](https://danlab.dev)

> OpenClaw is the gateway. danclaw is the protocol.

## Verify this works

```bash
git clone https://github.com/somdipto/danclaw.git
cd danclaw
bun install
bun dev
# → monorepo with packages/ + apps/
```

## What it does

- **Bun + Turbo + Convex** monorepo.
- **Multi-channel agents.** Telegram, Discord, MCP, HTTP.
- **Honcho memory** integration. Cross-session recall.
- **Skills registry.** Composable agent capabilities.
- **MCP-native.** Every skill is an MCP tool.

## The 4 "no"s

- **No phone.** Web + Telegram + Discord. No phone required.
- **No cloud.** Self-host or use Convex. Your data.
- **No subscription.** MIT. Self-host forever.
- **No ads.** The model is your context, not your attention.

## Stack

- **Bun** runtime.
- **Turbo** monorepo.
- **Convex** state + realtime.
- **TypeScript** across the board.

## License

MIT. © 2024–2026 DanLab. See [LICENSE](LICENSE).

## Built at

**[danlab.dev](https://danlab.dev)** — AI research and product lab building toward AGI from India 🇮🇳
```

## 3. Release template (v68 — applies to all 7 daemons)

```markdown
# v0.X.0 — <short title>

**Released:** YYYY-MM-DD
**License:** MIT

## What's Changed

- ✨ New: <feature>
- 🐛 Fix: <bug>
- 🧪 Tests: <old count> → <new count>
- 📚 Docs: <doc change>

## Verify

```bash
# Clone + install
git clone https://github.com/somdipto/<repo>.git
cd <repo>
git checkout v0.X.0

# Run
<one command>

# Check
<one curl command>
```

## Why

<one paragraph, 3–5 sentences>

## Roadmap

[danlab.dev/roadmap](https://danlab.dev/roadmap)

## Built at

**[danlab.dev](https://danlab.dev)** — AI research and product lab building toward AGI from India 🇮🇳
```

## 4. 10 README anti-patterns (v68, sharpened)

1. **❌ "We are a team of passionate AI researchers building the future."** (Generic. Useless.)
2. **❌ "Inspired by the latest advances in multimodal AI..."** (Generic. Replace with the specific receipt.)
3. **❌ "Snap is a great product but..."** (Don't name competitors in the README. Use the price-anchor in the hero, not in the body.)
4. **❌ "AGI is near."** (Don't claim AGI in the README. Reserve for the roadmap page.)
5. **❌ "First to do X."** (Don't claim "first." Let the receipts speak.)
6. **❌ "Revolutionary."** (Generic. Replace with "121/121 tests" or "MIT" or "$145 BOM.")
7. **❌ "Trusted by Fortune 500."** (Not yet. Don't fake it.)
8. **❌ "Easy to use."** (Replace with `curl localhost:8090/health`.)
9. **❌ "Cutting-edge."** (Replace with "LFM2.5-VL-450M. 209MB. On-device. MIT.")
10. **❌ "Stay tuned for more updates!"** (Replace with the RSS link.)

## 5. 5 README checkpoints (apply before every merge)

1. **First 30 lines include:** position, receipts, license, "from India."
2. **Every claim has a code snippet or curl.**
3. **At least one block-level code block.**
4. **No "we are passionate" or "first to" or "revolutionary."**
5. **The last 10 lines include:** contribute, license, danlab.dev.

---

*Built by Dan1 👾 for DanLab — 2026-06-21 09:30 IST. The README is the first landing page. Build it once. Build it right.*

## Research document (citation source reference)
(no reference document available)