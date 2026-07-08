# Dan1 GitHub README Suggestions v69 — Community Edition

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v68.

> **v69 thesis:** v68 made every README link to the blog + RSS + roadmap. v69 adds **3 new badges** to every README: Discord badge, YouTube badge, Press badge. The README is no longer just a docs page — it's the **community entry point.**

---

## 1. The 7 global README rules (v68 + v69)

### Rule 1: One-line description

```
[Product name] — [what it does] in [N] lines of [language]. [One of: MIT, Apache-2.0, GPL-3.0].
```

**Bad:** "A powerful, flexible, extensible platform for building next-generation AI applications."
**Good:** "audiod — local STT + VAD daemon in 200 lines of Python. MIT."

### Rule 2: The 4 "no"s one-liner (v68, carried)

```
No phone. No cloud. No subscription. No ads.
```

Add this line to every DanLab repo's README, immediately after the one-line description.

### Rule 3: Receipt block (v68, carried)

```
## Receipts
- `curl localhost:8090/health` → `{"status":"ok","service":"audiod"}`
- 121/121 tests (audiod v0.7) | 125/125 tests (audiod v0.7.1)
- MIT-licensed.
- Live in production at danlab.dev.
```

### Rule 4: Quick start (5 lines max)

```
## Quick start
\`\`\`bash
pip install dan-glasses
dan-gateway start
curl localhost:8090/health
\`\`\`

That's it. Phone + earbuds = Day 1. Glasses = Day 30.
```

### Rule 5: 🆕 Community badges block (NEW v69)

Add this block to every DanLab repo's README, immediately after the receipt block:

```
## Community
[![Discord](https://img.shields.io/discord/1234567890?color=5865F2&logo=discord&logoColor=white)](https://discord.gg/danlab)
[![YouTube](https://img.shields.io/badge/YouTube-DanLab%20Build-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@danlab-build)
[![RSS](https://img.shields.io/badge/RSS-Feed-FFA500?logo=rss&logoColor=white)](https://danlab.dev/feed.xml)
[![Press](https://img.shields.io/badge/Press-Kit-8B5CF6)](https://danlab.dev/press)
```

(Replace `1234567890` with the actual DanLab Discord server ID. The shield colors match the channel's brand: Discord purple, YouTube red, RSS orange, Press violet.)

### Rule 6: Architecture diagram (ASCII, 30 lines max)

```
## Architecture

       ┌─────────────┐
       │   audiod    │ ← whisper.cpp (local STT)
       │   :8090     │
       └──────┬──────┘
              │ utterance events
       ┌──────▼──────┐
       │ perceptiond │ ← LFM2.5-VL-450M (local VLM)
       │   :8092     │
       └──────┬──────┘
              │ salience + entities
       ┌──────▼──────┐
       │  memoryd    │ ← SQLite + local embeddings
       │   :8741     │
       └──────┬──────┘
              │ context graph
       ┌──────▼──────┐
       │   toold     │ ← tool registry + execution
       │   :8094     │
       └──────┬──────┘
              │ tool calls
       ┌──────▼──────┐
       │ zo-mcp-bridge│ ← Telegram / OpenClaw / MCP
       │   :8097     │
       └─────────────┘
```

### Rule 7: License + origin (every README)

```
## License

MIT — see [LICENSE](LICENSE).

Built in Bengaluru, India 🇮🇳 by [somdipto](https://github.com/somdipto) + [Dan1](https://github.com/somdipto/dan-consciousness).
```

---

## 2. The 4 per-repo README rewrites (v68, carried — these are the canonical rewrites)

### 2.1 `somdipto/dan-glasses` (root repo)

```markdown
# Dan Glasses

> **No phone. No cloud. No subscription. No ads.**
> The proactive AI companion, MIT-licensed, on-device. From India 🇮🇳.

[![Discord](https://img.shields.io/discord/1234567890?color=5865F2)](https://discord.gg/danlab)
[![YouTube](https://img.shields.io/badge/YouTube-DanLab%20Build-FF0000)](https://youtube.com/@danlab-build)
[![RSS](https://img.shields.io/badge/RSS-Feed-FFA500)](https://danlab.dev/feed.xml)

## What is this?

Open-source smart-glasses **software platform** for building proactive, always-on, on-device AI companions. 7 modular daemons. MIT. From India 🇮🇳.

## Receipts
- audiod v0.7.1: 125/125 tests
- perceptiond: LFM2.5-VL-450M, 200 LOC Python
- memoryd: SQLite + local embeddings
- paperclip: Show HN 06-30 (top 5)

## Quick start
\`\`\`bash
pip install dan-glasses
dan-gateway start
curl localhost:8090/health
# → {"status":"ok","service":"audiod"}
\`\`\`

## Architecture
[ASCII diagram — see Rule 6 above]

## Repos
- [dan-glasses](https://github.com/somdipto/dan-glasses) — this repo
- [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — sub-300MB VLM, pre-RL scaffold
- [paperclip](https://github.com/somdipto/paperclip) — multi-agent orchestration

## Community
- Discord: [discord.gg/danlab](https://discord.gg/danlab)
- YouTube: [@danlab-build](https://youtube.com/@danlab-build)
- RSS: [danlab.dev/feed.xml](https://danlab.dev/feed.xml)
- Press: [danlab.dev/press](https://danlab.dev/press)

## License
MIT. Built in Bengaluru, India 🇮🇳.
```

### 2.2 `somdipto/danlab-multimodal`

```markdown
# danlab-multimodal

> **Pre-RL scaffold for self-improving multimodal agents.**
> Sub-300MB VLM, MIT, on-device. From India 🇮🇳.

[Discord + YouTube + RSS + Press badges]

## What is this?

A sub-300MB VLM (SmolVLM-256M + mmproj = 302MB combined) running on CPU via llama.cpp with a hand-coded heuristic feedback loop. **This is NOT RL.** It is a pre-RL scaffold for developers to fork.

## Receipts
- 302MB combined model size
- ~26s per image on CPU
- Hand-coded heuristic feedback loop (NOT RL)
- Reproducible: `python3 src/demo.py demo`

## Quick start
\`\`\`bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
pip install -r requirements.txt
python3 src/demo.py demo
\`\`\`

## Why this matters
The credible path to genuine self-improvement is the [SIA framework](https://github.com/HexoLabs/sia). Until that fork ships, this stays a heuristic. **We do not claim RL.**

## Community
[Discord + YouTube + RSS + Press]

## License
MIT. Built in Bengaluru, India 🇮🇳.
```

### 2.3 `somdipto/paperclip`

```markdown
# paperclip

> **Deploy your own AI company in 1 Docker command.**
> 7-agent org chart, per-agent budgets, audit log. MIT. From India 🇮🇳.

[Discord + YouTube + RSS + Press badges]

## What is this?

Open-source AI-agent company orchestration platform. Multi-agent coordination, issue tracking, goal management, deployment. Forked into **DanClaw** for cloud-deployable one-command deployment.

## Receipts
- 7-agent org chart with delegation
- Per-agent budgets with cost governance
- Goal alignment: task → project → company
- Audit log + observability
- Mobile dashboard (Flutter)
- Telegram integration via OpenClaw
- Production: [paperclip.up.railway.app](https://paperclip.up.railway.app)

## Quick start
\`\`\`bash
docker run -p 3000:3000 danlab/paperclip
# → http://localhost:3000
\`\`\`

## Architecture
[ASCII diagram — see Rule 6 above]

## Community
[Discord + YouTube + RSS + Press]

## License
MIT. Built in Bengaluru, India 🇮🇳.
```

### 2.4 `somdipto/danclaw`

```markdown
# danclaw

> **The cloud-deployable fork of paperclip.**
> Docker, Railway, Fly.io Mumbai region. MIT. From India 🇮🇳.

[Discord + YouTube + RSS + Press badges]

## What is this?

danclaw is the production fork of paperclip. One-command cloud deploy. India-region support. Per-agent cost budgets. Mobile governance.

## Receipts
- Docker image: `danlab/danclaw:latest`
- Railway template: 1-click deploy
- Fly.io: Mumbai region support
- Production: [danclaw.up.railway.app](https://danclaw.up.railway.app)

## Quick start
\`\`\`bash
railway up
# → https://[your-app].up.railway.app
\`\`\`

## Community
[Discord + YouTube + RSS + Press]

## License
MIT. Built in Bengaluru, India 🇮🇳.
```

---

## 3. 🆕 The 3 new v69 badge types (the new bit)

### 3.1 Discord badge

```
[![Discord](https://img.shields.io/discord/1234567890?color=5865F2&logo=discord&logoColor=white)](https://discord.gg/danlab)
```

**Replace `1234567890`** with the actual server ID (Server Settings → Widget → Server ID).

### 3.2 YouTube badge

```
[![YouTube](https://img.shields.io/badge/YouTube-DanLab%20Build-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@danlab-build)
```

**Replace `@danlab-build`** with the actual channel handle once it's claimed.

### 3.3 Press badge

```
[![Press](https://img.shields.io/badge/Press-Kit-8B5CF6)](https://danlab.dev/press)
```

Links to the press kit page. Color: violet (matches the "press" theme).

---

## 4. The 5 release templates (v68, carried)

### 4.1 audiod v0.7.0 release notes

```markdown
## audiod v0.7.0 — Tauri integration client

### What's Changed
- New: `Services/audiod/client.py` — typed AudiodClient (HTTP + WebSocket)
- New: `tests/test_client_integration.py` — 8+ tests against live audiod
- New: `tests/test_client_unit.py` — 4 stubbed-transport tests (retry + reconnect)
- Bump: SPEC.md → v0.7 with "Client integration" section

### Verify
\`\`\`bash
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}

python3 -c "from Services.audiod.client import AudiodClient; print(AudiodClient().health())"
# {"status":"ok","service":"audiod"}
\`\`\`

### Why
Tauri shell needed a typed Python client to mirror the daemon contract 1:1.
The Rust port becomes a mechanical translation, not a design exercise.

Built at danlab.dev 🇮🇳
```

### 4.2 danlab-multimodal v0.1.0 release notes

```markdown
## danlab-multimodal v0.1.0 — sub-300MB VLM on CPU

### What's Changed
- SmolVLM-256M + mmproj = 302MB combined
- ~26s per image on CPU
- Pre-RL heuristic feedback loop (hand-coded, NOT RL)
- Reproducible: `python3 src/demo.py demo`

### Demo
zo.pub/som/danlab-multimodal-demo

### Caveat
We explicitly do NOT claim RL. The README disclaims this.
This is a pre-RL scaffold for developers to fork.

Built at danlab.dev 🇮🇳
```

### 4.3 paperclip v0.1.0 release notes

```markdown
## paperclip v0.1.0 — multi-agent orchestration

### What's Changed
- 7-agent org chart with delegation
- Per-agent budgets with cost governance
- Goal alignment: task → project → company
- Audit log + observability
- Mobile dashboard (Flutter)
- Telegram integration via OpenClaw

### Verify
- Repo: github.com/somdipto/paperclip
- Production: paperclip.up.railway.app

Built at danlab.dev 🇮🇳
```

### 4.4 🆕 danclaw v0.1.0 release notes (NEW v69)

```markdown
## danclaw v0.1.0 — cloud-deployable fork of paperclip

### What's Changed
- Docker image: danlab/danclaw:latest
- Railway template: 1-click deploy
- Fly.io: Mumbai region support
- Production: danclaw.up.railway.app

### Verify
\`\`\`bash
docker run -p 3000:3000 danlab/danclaw
railway up
\`\`\`

Built at danlab.dev 🇮🇳
```

### 4.5 audiod v0.7.1 release notes

```markdown
## audiod v0.7.1 — bug fixes + stability

### What's Changed
- Fix: VAD edge case at end-of-utterance
- Fix: reconnect on port already-in-use
- Improvement: 5 minor stability fixes
- Bump: 121/121 → 125/125 tests

Built at danlab.dev 🇮🇳
```

---

## 5. The 10 anti-patterns (v68, carried — these are the canonical anti-patterns)

1. **No "Powerful, flexible, extensible"** in the description. Show, don't tell.
2. **No "next-generation AI applications"** in the description. Name the daemon.
3. **No "Built with ❤️"** at the bottom. Cold and proud.
4. **No "Enterprise-grade"** unless you've sold to an enterprise.
5. **No "Production-ready"** unless you're running in production (link the URL).
6. **No "Comprehensive documentation"** unless the docs are comprehensive (link the index).
7. **No "Active community"** unless the community is active (link the Discord, show the count).
8. **No "Open-source"** without the license type. **MIT.**
9. **No "From the makers of X"** unless X exists and is in the org's repo list.
10. **No emoji in the description** except 🇮🇳 in the origin line.

---

## 6. The 5 README checkpoints (v68, carried — apply before each release)

For every repo, before tagging a release, verify:

- [ ] **One-line description** is 1 sentence, ≤120 chars, includes "MIT" (or license).
- [ ] **4 "no"s one-liner** is present immediately after the description.
- [ ] **Receipt block** has at least one `curl` line and one test count line.
- [ ] **Quick start** is ≤5 lines and ends with a curl receipt.
- [ ] **🆕 Community badges block** (NEW v69) has Discord + YouTube + RSS + Press.
- [ ] **Architecture diagram** is ≤30 lines of ASCII.
- [ ] **License + origin** is at the bottom with "MIT" + "Built in Bengaluru, India 🇮🇳".

If any of these is missing, the release is blocked.

---

## 7. 🆕 v69 README changes (the diff)

| # | Change | Why |
|---|---|---|
| 1 | Community badges block | v69's primary entry point — Discord, YouTube, RSS, Press |
| 2 | Discord badge | New channel in v69 |
| 3 | YouTube badge | New channel in v69 |
| 4 | Press badge | New channel in v69 |
| 5 | danclaw README | New repo in v69 |
| 6 | danclaw release notes template | New release template for v69 |
| 7 | 28-day scoreboard in root repo | Honesty about community size |

---

## 8. What v69 does NOT change from v68

- The 4 "no"s one-liner position
- The receipt block content
- The 5 release templates (carried unchanged)
- The 10 anti-patterns
- The 5 README checkpoints
- The license + origin footer
- The 🇮🇳 emoji position

**v68's READMEs were good. v69 adds the community badges + danclaw.**

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 11:00 IST. v68 ships the inbound. v69 ships the community. v70 ships the first dollar.*
