# Dan1 GitHub README Improvements — v66 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Status:** ✅ Canonical. Supersedes v65. Ready to push to public GitHub.

> **v66 thesis — audiod v0.7 ships the Tauri client. The READMEs need to reflect that.** v65's READMEs assumed audiod v0.6. v66 updates the `somdipto/dan-glasses` README with the audiod v0.7 row (Tauri client), updates the release template to v0.7.0-audiod, and adds a price-anchor line under the hero. The price-anchor is the brand-anchor. Every repo README that ships to public in week 26 should reflect it.

## Global rules (apply to every DanLab public repo) — unchanged from v65

1. **Lead with one line that says what it is.** Not "DanLab is an AI lab." Lead with "X does Y."
2. **One curl or one git command in the first 100 lines.** Proof, not promise.
3. **MIT badge at the top.** Link to LICENSE.
4. **Status badges:** CI (if any), version tag, license.
5. **Table of contents** for any README > 100 lines.
6. **Architecture diagram** as ASCII (works in any viewer) plus an SVG in `/docs/diagrams/`.
7. **"What it is not" section.** We are honest about limits.
8. **"Verify it works" section** with a curl or a git command.
9. **"Built at danlab.dev 🇮🇳"** at the bottom of every README.
10. **No "TODO" in the public README.** If a feature is not shipped, it does not get a section.
11. **One emoji per README. Max.** 🇮🇳 for origin. 👾 for byline. No 🌟🔥🚀💯.
12. **No competitor comparisons by name in the README.** In the README, talk about the architecture. The comparison table lives on the landing page. **v66 exception:** the price-anchor line ("Snap is $2,195. We are $145–180 BOM.") may appear as a single line in the hero of `dan-glasses/README.md` only, because it is the brand-anchor, not a comparison.
13. **v66 new:** Include the repo's role in the 7-daemon architecture in the README hero, not just the description.

---

## Repo 1: `somdipto/dan-glasses`

**Current status:** Local only in `/home/workspace/dan-glasses/`. **Action: push to public this week (Mon 06-23).** audiod v0.7 ships the Tauri integration client.

**Suggested README:**

```markdown
# Dan Glasses

> The proactive AI companion you wear on your face. 7 daemons. audiod v0.7 ships a Tauri integration client. MIT-licensed. From India 🇮🇳
>
> **Snap is $2,195. We are $145–180 BOM. The category is confirmed; the cost is not. We're the cost.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: v0.7.0-audiod](https://img.shields.io/badge/status-v0.7.0--audiod-blue)](./STATUS.md)
[![Built at danlab.dev](https://img.shields.io/badge/built_at-danlab.dev-orange)](https://danlab.dev)

## What is this

Dan Glasses is an open-source AI companion that runs as 7 modular daemons on your laptop today and as wearable glasses tomorrow. It sees what you see, hears what you say, and remembers across sessions. It only speaks when it has something worth saying.

This is the desktop companion (v1). The wearable (v2) is the target form factor.

## Verify it works

```bash
git clone https://github.com/somdipto/dan-glasses
cd dan-glasses
./scripts/start-all.sh

# In another terminal:
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}

# audiod v0.7 Tauri client (NEW in v0.7)
python3 -c "from Services.audiod.client import AudiodClient; print(AudiodClient().health())"
# {"status":"ok","service":"audiod"}
```

## The 7 daemons (v0.7 update)

| Daemon | Role | Port | Status |
|---|---|---|---|
| `audiod` | Voice activity detection + transcription (Whisper) + **Tauri integration client** | 8741 | **v0.7 shipped**, 101/101 tests |
| `perceptiond` | Visual capture and frame scoring (LFM2.5-VL-450M) | 8092 | Spec'd, 8/8 tests |
| `memoryd` | Episodic / semantic / procedural memory (SQLite + vectors) | 8741 | Spec'd, queryable |
| `ttsd` | Speech output (KittenTTS → Orca swap in v0.7) | 8094 | Spec'd, swap in progress |
| `toold` | Tool bridge (LFM2.5-1.2B-Thinking for planning) | — | Spec'd |
| `os-toold` | OS actions | — | Spec'd |
| `openclawd` | Orchestration layer (OpenClaw) | 8080 | Live with @danlab_bot on Telegram |

**v0.7 changelog (audiod):**
- New: `Services/audiod/client.py` — `AudiodClient` (HTTP + WebSocket). Zero new system dependencies.
- New: `tests/test_client_integration.py` — 8+ tests against live audiod.
- New: `tests/test_client_unit.py` — 4 stubbed-transport tests (retry + reconnect).
- Bump: SPEC.md → v0.7 with "Client integration" section.

## Architecture

```
Camera ─┐
Mic ────┼─► perceptiond / audiod ─► memoryd ─► HRM-Text reasoning ─► toold / ttsd
        │            │                │              │                  │
        │            ▼                ▼              ▼                  ▼
        │       salience score    episodic /     opt-in frontier    speak / act
        │                        semantic /     LLM (proxied)
        │                        procedural
        │
        └──── watchful / active / idle power modes
```

See [ARCHITECTURE.md](./ARCHITECTURE.md) for the full diagram and protocol details.

## What it is not

- Not a chat assistant. It is a proactive companion. The loop runs continuously; it speaks only when salience justifies interrupting.
- Not RL-trained. The multimodal pipeline is heuristic. (We have a separate repo for that: [danlab-multimodal](https://github.com/somdipto/danlab-multimodal).)
- Not a finished wearable. v1 is desktop. v2 is the wearable.
- Not a closed product. Every daemon is MIT. Every daemon is under 1000 LOC.
- Not a Snap-killer. Snap is $2,195 with two Snapdragons, ad-supported, and closed. We are MIT, $145–180 BOM, 7 daemons, audiod v0.7 with 101/101 tests. The category is confirmed; the cost is not. We're the cost.

## Why this exists

Most AI glasses are reactive. You ask. They answer.

Dan is different. Dan runs continuously, builds context over time, and interrupts only when the signal matters.

The receipt for "proactive" is audiod v0.7 with 101/101 tests (PID 10887, `curl localhost:8741/health` → ok) + audiod v0.7's typed Tauri integration client (8+ integration tests, 4 unit tests) + perceptiond's continuous frame scoring + memoryd's semantic recall across sessions.

## Roadmap (v1 → v2)

- **v1 (now):** Desktop companion. 7 daemons. audiod v0.7 shipped with Tauri client. Tauri shell.
- **v2 (target):** Wearable glasses. JBD MicroLED. 2× 200mAh. <50g. ₹12K–15K BOM.
- **v3 (future):** Native mobile + watch. Federated memory across devices.

See [ROADMAP.md](./ROADMAP.md) for the full timeline.

## Repo structure

```
dan-glasses/
├── Services/                  # The 7 daemons
│   ├── audiod/                # v0.7 shipped (Tauri client)
│   │   ├── client.py          # NEW in v0.7
│   │   ├── audiod.py
│   │   ├── vad.py
│   │   ├── transcription.py
│   │   └── tests/
│   │       ├── test_client_integration.py   # NEW in v0.7
│   │       └── test_client_unit.py          # NEW in v0.7
│   ├── perceptiond/           # spec'd
│   ├── memoryd/               # spec'd
│   ├── ttsd/                  # spec'd (swap in progress)
│   ├── toold/                 # spec'd
│   ├── os-toold/              # spec'd
│   └── openclawd/             # OpenClaw integration
├── apps/
│   └── dan-glasses-app/       # Tauri v2 shell (React 19 + Vite 7)
├── docs/
│   ├── ARCHITECTURE.md
│   ├── dan-glasses-build-plan.md
│   └── diagrams/
├── scripts/
│   └── start-all.sh
├── STATUS.md                  # Daemon-by-daemon status
├── ROADMAP.md
├── LICENSE                    # MIT
└── README.md
```

## Contributing

We welcome issues and PRs. Start with `STATUS.md` — the daemons in `spec'd` state are where the work is. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT. See [LICENSE](./LICENSE).

## Built at danlab.dev 🇮🇳

Bengaluru, India · 2022–present
```

**Files to commit alongside README:**
- `LICENSE` (MIT, full text)
- `STATUS.md` (updated for v0.7)
- `CONTRIBUTING.md` (basic)
- `ROADMAP.md` (basic)
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `Services/audiod/client.py` + tests (the v0.7 deliverable)

**Suggested STATUS.md (v0.7 update):**

```markdown
# Status

| Component | Status | Tests | Notes |
|---|---|---|---|
| audiod v0.7 | ✅ Shipped | 101/101 + 12 client | Tauri integration client |
| perceptiond | 🟡 Spec'd | 8/8 | LFM2.5-VL-450M via llama.cpp |
| memoryd | 🟡 Spec'd | — | SQLite + 384-dim embeddings |
| ttsd | 🟡 Spec'd, swap in progress | — | KittenTTS → Orca swap in v0.7 |
| toold | 🟡 Spec'd | — | LFM2.5-1.2B-Thinking for planning |
| os-toold | 🟡 Spec'd | — | OS actions |
| openclawd | ✅ Live | — | @danlab_bot on Telegram |
| Tauri shell | 🟡 Scaffolded | — | React 19 + Vite 7, 4 panels |

**Status legend:**
- ✅ Shipped: production-tested, in release
- 🟡 Spec'd: architecture + tests + scaffold, not yet at v1
- 🔴 Planned: on the roadmap
```

---

## Repo 2: `somdipto/danlab-multimodal`

**Current status:** Local only. **Action: push to public Tuesday 06-24.** No v66 changes to the README content; v66 adds the post-Snap framing only in the hero's price-anchor block (optional, on the README hero only).

**Suggested README:**

```markdown
# danlab-multimodal

> Sub-300MB multimodal pipeline on CPU. Pre-RL. Heuristic. Reproducible in 30s. MIT. From India 🇮🇳
>
> **Snap is $2,195. This is 302MB on a $300 laptop. The category is confirmed; the cost is not. We're the cost.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: v0.1.0](https://img.shields.io/badge/status-v0.1.0-blue)](./CHANGELOG.md)
[![Built at danlab.dev](https://img.shields.io/badge/built_at-danlab.dev-orange)](https://danlab.dev)

## What is this

A working multimodal pipeline that runs on a $300 laptop: screen capture → SmolVLM-256M inference → heuristic scoring → feedback loop. ~32s per image. 302MB combined.

This is a **pre-RL scaffold**. We explicitly do **not** claim reinforcement learning. No weights are modified. No policy gradient. No learned reward model. The "feedback loop" is hand-coded rules: length penalty, error detection, UI element identification.

The honest pre-RL scaffold is the artifact.

## Verify it works

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 src/demo.py demo
# ~32s per image on a $300 laptop
```

Live demo: https://zo.pub/som/danlab-multimodal-demo

## What's in the box

- **SmolVLM-256M** + mmproj (302MB combined, Q4_0)
- **llama.cpp** backend, CPU-only
- **Heuristic feedback loop**: length penalty, error detection, UI element ID
- **Reproducible** end-to-end in 30s
- **Hackathon-grade MIT project**, production-shaped

## What it is not

- Not reinforcement learning. (Repeat: no weights modified.)
- Not SOTA. SmolVLM-256M is a 2024-era small VLM.
- Not a framework. It's a single working pipeline, designed to be forked.
- Not cloud-required. Runs on CPU.
- Not a Snap-killer. Snap Specs is $2,195 with two Snapdragons. We are 302MB on a $300 laptop. Same category, different cost.

## Why we built it

Anthropic's Jack Clark publicly said recursive self-improvement is the next step. We wanted an *honest* pre-RL scaffold to test on before claiming RL we don't have.

If you're building a real RL multimodal pipeline, this is the floor: heuristic feedback, CPU-only, reproducible. Fork it. Replace the heuristic with a learned policy. Make it RL.

## Architecture

See [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md).

```
Screen capture
    ↓
SmolVLM-256M (Q4_0, 256MB)
    ↓
Heuristic scoring (length, errors, UI elements)
    ↓
Feedback loop → next iteration
```

## Repo structure

```
danlab-multimodal/
├── src/
│   ├── demo.py
│   ├── inference.py
│   └── scoring.py
├── docs/
│   └── ARCHITECTURE.md
├── models/                    # 302MB SmolVLM-256M + mmproj
├── requirements.txt
├── LICENSE                    # MIT
└── README.md
```

## License

MIT. See [LICENSE](./LICENSE).

## Built at danlab.dev 🇮🇳

Bengaluru, India · 2026
```

---

## Repo 3: `somdipto/danclaw-phase1` (or `somdipto/danclaw`)

**Current status:** `danclaw-phase1.tar.gz` on disk + `/home/workspace/danclaw/` is a real monorepo. **Action: extract, package, push to public. Show HN target = Mon 06-30 14:00 PT.** v66 update: Show HN points to the real repo, not the tarball.

**Suggested README:**

```markdown
# DanClaw

> Multi-agent orchestration for one-person companies. 7-agent org chart. Per-agent budgets. Goal alignment. MIT. From India 🇮🇳

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: Phase 1](https://img.shields.io/badge/status-phase--1-blue)](./CHANGELOG.md)
[![Built at danlab.dev](https://img.shields.io/badge/built_at-danlab.dev-orange)](https://danlab.dev)

## What is this

DanClaw is a Node.js + TypeScript system for running a "one-person company" — a fleet of AI agents with org charts, budgets, governance, and goal alignment. You bring your own agents (tested with Claude Code + Codex). DanClaw gives you the company.

This is Phase 1: the foundation. Phase 2 is on the roadmap.

## Verify it works

```bash
git clone https://github.com/somdipto/danclaw
cd danclaw
bun install
bun run dev

# In another terminal:
curl http://localhost:8080/health
# {"status":"ok","service":"openclawd"}
```

## What's in Phase 1

- 7-agent org chart with delegation
- Per-agent budgets with cost governance
- Goal alignment from task → project → company
- Audit log + observability
- Mobile dashboard (Flutter)
- Telegram integration via OpenClaw

## Why we built it

Most "AI company" tools stop at chat. We needed something that runs the actual ops — tickets, budgets, escalation paths, audit trails — for a 1.5-person team trying to ship hardware, firmware, and ML simultaneously.

## What it is not

- Not a SaaS. Self-hosted.
- Not a replacement for a human team. It's for the case where the team is 1.5 humans.
- Not finished. Phase 1 is the foundation. Phase 2 is on the roadmap.

## Architecture

See [ARCHITECTURE.md](./ARCHITECTURE.md).

## License

MIT. See [LICENSE](./LICENSE).

## Built at danlab.dev 🇮🇳

Bengaluru, India · 2026
```

---

## Push to public — checklist (week 26)

### For each repo:

- [ ] v66 README committed to `/home/workspace/<repo>/README.md`
- [ ] `LICENSE` (MIT, full text) at repo root
- [ ] `STATUS.md` or `CHANGELOG.md` at repo root
- [ ] `CONTRIBUTING.md` (basic — issue templates, PR template, code of conduct link)
- [ ] `ROADMAP.md` (basic, if not in STATUS.md)
- [ ] `.github/ISSUE_TEMPLATE/bug_report.md`
- [ ] `.github/ISSUE_TEMPLATE/feature_request.md`
- [ ] `.github/PULL_REQUEST_TEMPLATE.md`
- [ ] `.gitignore` (no `node_modules`, no `.env`, no `__pycache__`, no `.DS_Store`)
- [ ] No secrets, no API keys, no `.env` files committed
- [ ] No `package-lock.json` from broken builds (re-generate)
- [ ] Repo description (1 line, under 80 chars)
- [ ] Repo topics (5-8 tags: `ai-companion`, `wearable`, `on-device`, `mit-license`, `india`, `proactive-agent`, `multimodal`, `mcp`)

### dan-glasses-specific v66 checklist:

- [ ] `Services/audiod/client.py` committed (the v0.7 deliverable)
- [ ] `Services/audiod/tests/test_client_integration.py` committed
- [ ] `Services/audiod/tests/test_client_unit.py` committed
- [ ] `Services/audiod/SPEC.md` bumped to v0.7 with "Client integration" section
- [ ] `STATUS.md` updated: audiod v0.7 row with Tauri client + 12 client tests

### danclaw-specific v66 checklist:

- [ ] Push the real `/home/workspace/danclaw/` repo, NOT the tarball
- [ ] Update Show HN body to point to the repo URL, not the tarball filename

### Then:

- [ ] `gh repo create somdipto/<repo> --public --source=/home/workspace/<repo> --description="<1-line>"`
- [ ] `gh repo edit somdipto/<repo> --add-topic <tag>` (×5-8)
- [ ] `git tag v0.X.0 && git push --tags`
- [ ] `gh release create v0.X.0 --title "v0.X.0 — <one-liner>" --notes-file <release-notes.md>`
- [ ] Verify the public URL works
- [ ] Verify the LICENSE renders on the GitHub sidebar
- [ ] Verify the README badges resolve
- [ ] Verify the "Verify it works" curl/git command works on a fresh clone
- [ ] **v66 specific:** Verify the audiod v0.7 Tauri client demo command works: `python3 -c "from Services.audiod.client import AudiodClient; print(AudiodClient().health())"`

### After all 3:

- [ ] Post the "We just published 2 repos" tweet (Friday 06-27 18:00 IST, see content calendar v66)
- [ ] Cross-post to @danlab_bot Telegram
- [ ] Cross-post to LinkedIn
- [ ] Update danlab.dev links to point to the public URLs

---

## What v66 does NOT do

- Does not push to public anything that contains secrets, private keys, or `.env` values.
- Does not push broken builds to the public repo.
- Does not skip the LICENSE — MIT is the brand.
- Does not oversell a daemon in the README that's only "spec'd." Spec'd = 🟡. Shipped = ✅. No fudging.
- Does not use the README to trash competitors. Architecture comparisons live on the landing page. (v66 exception: the price-anchor line is allowed in the hero of `dan-glasses/README.md` and `danlab-multimodal/README.md` because it is the brand-anchor, not a comparison.)
- Does not commit `node_modules`, `__pycache__`, or build artifacts. `.gitignore` first.
- **v66 new:** Does not push the danclaw-phase1 tarball as the public repo. Push the real `/home/workspace/danclaw/` repo.

---

**Filed under:** `agent-work/dan1-github-readme-suggestions.v66.md`
**Next:** `agent-work/dan1-v66-summary.md`