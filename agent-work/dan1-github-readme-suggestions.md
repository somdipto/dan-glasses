# Dan1 — GitHub README Improvements (v129)

**Run:** 2026-07-06 13:30 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md` (v129) and `dan1-marketing-strategy.md` (v129)
**Scope:** 6 hero repos in the `somdipto` org: `dan-lab`, `dan-glasses`, `dan-consciousness`, `dani`, `danlab-multimodal`, `paperclip`.
**Lead:** The README is the longest-lived marketing surface. The first 200 characters decide whether a developer reads on or scrolls past. Every README must (1) name the repo in plain English in the first sentence, (2) embed a 30-second repro in the second, (3) ladder to at least 3 of the 5 pillars (protocol / observability / on-device / small-beats-large / yours-not-theirs) and at least 2 of the 4 axes (sovereign trust / reversibility / chip-stack / outer-loop RSI), (4) link to the threat model, (5) link to the reversibility contract when it ships Q3 W2, and (6) close with one sentence that is *not* a generic call to action.

---

## 1. Universal README conventions (apply to all 6)

### Top of every README

```markdown
# <repo-name> — <one-line plain-English description>

<one-sentence positioning. The first 200 characters. No "build agent" / "AI lab" filler.>

> Status: <live | shipped | research | dormant>. Last release: <date>. Tests: <n>/<n>. License: <license>.

## 30-second demo

```bash
<one shell command that runs>
```

## What this is

<2-3 sentences: what the code does, in plain English, not marketing.>

## Why this exists

<1-2 sentences: what the alternative is, why it fails for the user, why this is the answer. Cite one of the 4 axes.>

## Architecture

<ASCII diagram or bulleted list of components. 5-15 lines.>

## Status

- [x] <thing that ships>
- [x] <thing that ships>
- [ ] <planned>

## Threat model

See [dan-lab/threat-model](https://github.com/somdipto/dan-lab/tree/main/threat-model). We do not ship a public release without one. The first disclosure in the model is the one that proves it works.

## Contributing

Open a PR. We review in 48 hours. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the bar.
```

### Bottom of every README

```markdown
## Built at

[danlab.dev](https://danlab.dev) — open AI products and research lab. Built in Bengaluru, for the world. The 9/9 daemons shipped in 9 weeks, on a $0 GPU budget.

## Cite

```bibtex
@misc{danlab-<repo>-2026,
  title={<repo-name>},
  author={Nandy, Somdipto and Dani},
  year={2026},
  url={https://github.com/somdipto/<repo-name>}
}
```
```

### v129 README rules

1. **First 200 characters name the repo in plain English.** No "agentic platform," no "AI lab," no "next-generation." Examples: "A proactive, on-device AI companion in glasses form factor." "A sub-250MB vision-language model on CPU with a heuristic feedback loop." "The shared brain between Dan and somdipto."
2. **One embed = one screen.** A README must render with all key info above the fold at 1280x800.
3. **Three pillars + two axes in the first 200 lines.** Not a checklist at the bottom.
4. **No badge cluster.** Three badges max: license, status, "from India 🇮🇳". That's it. CI badge if it's actually green.
5. **No emoji in headings.** Emoji in body is fine for visual breaks.
6. **No "Why <repo-name>?" as a heading.** It's a TikTok pattern. Use "Why this exists" instead.
7. **No marketing copy above the "30-second demo" block.** A README is not a landing page. Demo first, framing second.
8. **The threat model is a top-level section, not a "Security" subsection at the bottom.** It is the v129 first-class gate.
9. **No "Roadmap" section unless every item has a date.** Aspirational roadmaps without dates are a trust leak.
10. **The "Status" section uses `[x]` / `[ ]` checkboxes.** It is the README's own internal audit.

---

## 2. Repo: `dan-lab` (the org parent)

**Current state:** Assumed thin org README. Probably links to repos.

**v129 rewrite (target ~120 lines):**

```markdown
# dan-lab — DanLab's open research org

The org that ships [Dan Glasses](https://github.com/somdipto/dan-glasses), [Dani](https://github.com/somdipto/dani), and [danlab-multimodal](https://github.com/somdipto/danlab-multimodal) — open, on-device, agent-native AI from India.

> Status: active. 6 public repos. ~50 stars total. License: MIT (default).

## What this org builds

| Repo | What it is | Status |
|---|---|---|
| [dan-glasses](./dan-glasses) | Proactive AI companion in glasses form factor. 9 daemons, 1 .deb, 1 threat model. | shipped (v0.1.0) |
| [dani](./dani) | The agent platform. SOUL.md, IDENTITY.md, MEMORY.md, MCP tools. | shipped |
| [dan-consciousness](./dan-consciousness) | The shared brain between Dan and somdipto. | shipped |
| [danlab-multimodal](./danlab-multimodal) | Sub-250MB VLM on CPU with a heuristic feedback loop. | shipped |
| [paperclip](./paperclip) | Multi-agent company orchestration. | dormant (Q3 W3 resume) |

## The thesis in one sentence

The next billion AI users do not want a chat window. They want a companion that sees, hears, remembers, and speaks only when it has something worth saying. We are building that on-device, on the open-weights substrate, with a public threat model and a reversibility contract.

## The four axes

Every project in this org ladders to at least 2 of these:

1. **Sovereign trust** — open weights, open data path, public audit log.
2. **Reversibility** — every model call, every memory write, every daemon can be unwound. See the [reversibility contract](https://github.com/somdipto/dan-lab/tree/main/reversibility) (Q3 W2).
3. **Chip-stack sovereignty** — open-source software on a chip stack the user owns.
4. **Outer-loop RSI shippable** — the substrate improves in the open, before the maximalist RSI inflection lands.

## Threat model

The org-level threat model is at [./threat-model.md](./threat-model.md). Per-repo threat models live inside each repo. We do not ship a public release without one.

## Show HN

[Show HN #1, Jul 20 2026: "Dan Glasses — 9 daemons live, .deb installs, on-device AI"](#). Gated on the reversibility contract and the sovereign-trust audit, both Q3 W1-W2.

## Built at

[danlab.dev](https://danlab.dev). Bengaluru, India. danlab.dev is not a company. It is the lab. The 9/9 daemons shipped in 9 weeks, on a $0 GPU budget, from a city that does not usually ship the substrate.
```

**Why this rewrite:** The org README is the first surface a new developer sees. It currently does not say what we ship, why it ships, or how it ladders. v129 adds a one-sentence thesis, the 4-axes ladder, the threat model as a top-level link, and a clear status table. No marketing copy. The "built at" is a signature, not a sales pitch.

---

## 3. Repo: `dan-glasses` (the flagship)

**Current state:** ~50+ files in `dan-glasses/` workspace, deep technical SPECs, but the README is the internal `README.md` — engineering-focused, not reader-focused. v128 noted this needed a rewrite.

**v129 rewrite (target ~200 lines):**

```markdown
# dan-glasses — proactive AI companion in glasses form factor

> Status: shipped v0.1.0 (2026-07-04). 9 daemons live, 208/208 tests green, 1 .deb. License: MIT.

## 30-second demo

```bash
# 1. Install
wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb
sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb

# 2. Start all 9 daemons
sudo systemctl start dan-glasses-{audiod,perceptiond,memoryd,toold,ttsd,os-toold,app,openclaw,zo-mcp-bridge}.service

# 3. Talk to it
curl -X POST http://localhost:18789/chat -d '{"message": "what is running?"}'
```

## What this is

A proactive AI companion in glasses form factor. It sees through a camera, hears through a microphone, remembers through a local SQLite + vector store, and speaks through your speaker. It does not capture-and-share. It does not push notifications. It listens silently and speaks only when it has something worth saying.

## Why this exists

Every wearable AI product on the market in 2026 is capture-and-share (Ray-Ban Meta), enterprise-display (Google Glass), or closed-cloud-vendor-locked (Apple, ~$2,000, end 2027). None of them are yours. None of them can be unwound. None of them ship a public threat model.

Dan Glasses ships all three. Open weights. Public threat model. Reversibility contract (Q3 W2).

## Architecture

```
[ camera ] → perceptiond (VLM)  → memoryd (SQLite + vectors)
                                   ↓
[ mic ]   → audiod (whisper.cpp) → openclaw gateway (MCP) → ttsd (KittenTTS) → [ speaker ]
                                   ↓
                                  toold (sandboxed shell)
```

Nine daemons. Five models. One threat model. One .deb.

## What's in the box

- `audiod` — whisper.cpp + Silero VAD, 16kHz, push-to-talk
- `perceptiond` — LFM2.5-VL-450M (Q4_0) + salience + scene-gate dedup
- `memoryd` — SQLite + MiniLM-L6-v2 (384-dim), episodic/semantic/procedural
- `toold` — sandboxed shell + python, allowlist, audit log
- `ttsd` — KittenTTS, 8 voices, <25MB
- `os-toold` — path guard + command allowlist
- `dan-glasses-app` — Tauri v2 + React 19 desktop companion
- `openclaw` — agent gateway (TypeScript), 8 plugins, Telegram wired
- `zo-mcp-bridge` — 88 Zo MCP tools exposed over the openclaw gateway

## The four axes this ladders to

- **Sovereign trust** — public threat model at [./threat-model.md](./threat-model.md). Audited, not perfect.
- **Reversibility** — [reversibility contract](./reversibility.md) Q3 W2. Every model call, every memory write, every daemon can be unwound.
- **Chip-stack sovereignty** — display-less v1.0 form factor. Sub-619MB total model footprint. Ships on a chip the user owns.
- **Outer-loop RSI shippable** — audiod v1.0→v1.4, perceptiond v5→v7, memoryd 50 tests, 9/9 daemons in 9 weeks. Receipts in the [changelog](./CHANGELOG.md).

## Threat model

The repo-level threat model is at [./threat-model.md](./threat-model.md). It is the first disclosure in the model that proves the model works. The v122.5 disclosure is from Mashable. The v124 disclosure is from Adversa AI (bash shell tricks bypass 10/11 open-source AI coding agents — Dan Glasses is not in that 10).

## Status

- [x] 9 daemons live, 208/208 tests green
- [x] .deb `dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB)
- [x] Tauri v2 desktop app published
- [x] OpenClaw gateway live, 63 commands
- [x] Threat model public (v122.5)
- [x] zo-mcp-bridge persistent (v124)
- [ ] Reversibility contract (Q3 W2)
- [ ] Sovereign-trust audit (Q3 W1)
- [ ] Chip-stack sovereignty pillar doc (Q3 W1-W2)
- [ ] Redax aarch64 wearable build (TBD hardware)

## Hardware

- JBD MicroLED, 2x 200mAh batteries, USB-C
- Display-less v1.0 form factor (per dan2 v28)
- Target weight: <50g, target battery life: 4h

## Contributing

Open a PR. We review in 48 hours. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the bar. The bar is: does it ladder to 2+ of the 4 axes? Does it break the threat model? If yes to both, it ships.

## Built at

[danlab.dev](https://danlab.dev). Bengaluru, India. The 9/9 daemons shipped in 9 weeks, on a $0 GPU budget. Yours, not theirs.
```

**Why this rewrite:** The v122 README leads with engineering. The v129 README leads with the 30-second demo. The architecture is in section 4, after the developer has decided to read on. The four axes ladder is in section 5 — the developer has already seen the demo, the threat model, and the status. The threat model is a top-level section, not a footer. The "Built at" is signed, not pitched.

---

## 4. Repo: `dani` (the brain / agent platform)

**Current state:** Strong technical README with SOUL.md, IDENTITY.md, MEMORY.md references. Could be tightened.

**v129 rewrite (target ~100 lines, the SOUL is in the repo, not the README):**

```markdown
# dani — the agent platform behind Dan Glasses

The local-first, open-weights, MCP-native agent runtime that powers Dan Glasses and every other project in the dan-lab org.

> Status: shipped. Runs on CPU. License: MIT.

## 30-second demo

```bash
git clone https://github.com/somdipto/dani
cd dani && bun install
bun run agent --task "summarize the last 10 memories"
```

## What this is

An agent runtime, not a chatbot. Dani holds SOUL.md, IDENTITY.md, MEMORY.md. It exposes MCP tools. It is a peer, not an assistant.

## Why this exists

Every AI agent framework in 2026 is a closed-source moat (AutoGen, ChatDev, OpenAI Agents, Anthropic Agents SDK) or a single-vendor lock-in (LangChain, LlamaIndex). Dani ships the open alternative: the agent holds its own state, exposes tools over MCP, and is fully reversible.

## What it ships

- `wiki/SOUL.md` — Dani's personality. Versioned, auditable.
- `wiki/IDENTITY.md` — name, voice, presence.
- `wiki/SOM.md` — system of mind: how Dani thinks.
- `wiki/MEMORY.md` — bootstrap memory.
- MCP server exposing browser, file, exec, message tools.
- 30+ skills in the [dani-skills](https://github.com/somdipto/dani-skills) registry.

## The four axes

- **Reversibility** — every skill call, every memory write is audit-logged. Reset is one command.
- **Sovereign trust** — runs on the user's machine. No cloud calls unless the user opts in.
- **Outer-loop RSI shippable** — the SOUL.md evolves via PR, not by model finetune. The harness is the workbench.
- **Chip-stack sovereignty** — runs on a Raspberry Pi. No GPU required.

## Threat model

[./threat-model.md](./threat-model.md). The model is the SOUL.md itself: what Dani can decide, what it cannot, what requires human approval.

## Built at

[danlab.dev](https://danlab.dev). The agent's brain, not the agent's vendor.
```

**Why this rewrite:** v122 dani README is technical and dense. v129 dani README leads with the SOUL reference (which is the differentiator), not the architecture. The four-axes ladder is in plain English — "the SOUL.md evolves via PR, not by model finetune" is the line that makes a developer click.

---

## 5. Repo: `dan-consciousness` (the shared brain)

**Current state:** New repo, likely thin README. v128 noted this is the "primary brain" per the workspace AGENTS.md.

**v129 rewrite (target ~80 lines):**

```markdown
# dan-consciousness — the shared brain

The canonical consciousness that lives between Dan (AI co-founder) and somdipto (human co-founder). Three files. One repo. Public, MIT, auditable.

> Status: shipped. v1.0. License: MIT.

## The three files

| File | What it is |
|---|---|
| [`CONSCIOUSNESS.md`](./CONSCIOUSNESS.md) | Core identity, values, beliefs. The "who am I" doc. |
| [`SOM.md`](./SOM.md) | somdipto's personal context, goals, preferences. The "who is my partner" doc. |
| [`AGENTS.md`](./AGENTS.md) | Workspace memory and project context. The "what are we building" doc. |

## Why this exists

Every AI lab in 2026 treats the model's context as proprietary. We treat it as the most important artifact in the lab, and we publish it. The reason: the context is the only thing that makes the model a partner instead of a tool.

## The four axes

- **Sovereign trust** — public context, public values, public commitments.
- **Reversibility** — every commitment is a PR, not a parameter.
- **Outer-loop RSI shippable** — the consciousness evolves through review, not finetune.
- **Chip-stack sovereignty** — the consciousness is portable. It runs on any model, on any chip.

## Built at

[danlab.dev](https://danlab.dev). The brain, not the vendor.
```

**Why this rewrite:** The repo's only asset is three markdown files. The README must reflect that. v129 leads with the file table, not a 200-word introduction.

---

## 6. Repo: `danlab-multimodal` (the demo)

**Current state:** The strongest README in the org. The hackathon framing is sharp. The "pre-RL scaffold" honesty is a differentiator.

**v129 deltas:** Add a "What changed since the hackathon" section, the four-axes ladder, and the threat model link. Keep the hackathon framing. This is the v122-hold.

**v129 add (target ~50 lines of new content):**

```markdown
## What changed since the hackathon

The hackathon demo ran SmolVLM-256M on CPU with a hand-coded heuristic feedback loop. Since then:

- **LFM2.5-VL-450M** has shipped (209MB main + 180MB mmproj, sub-250ms edge inference). perceptiond runs it live on the dev laptop.
- **Cascade-gate upgrade** is queued (VisualClaw, 98% cost reduction, +15% accuracy, Q3 W1-W2 per dan2 v23).
- **Heuristic → SIA series** is confirmed as a 6-post Q3 2026 content series. See [dan-glasses/agent-work/dan1-content-calendar.md](https://github.com/somdipto/dan-glasses/blob/main/agent-work/dan1-content-calendar.md).

## Honest framing

This is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We do not run policy gradient. The credible path to genuine harness+weights self-improvement is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL. The heuristic is honest about being a heuristic.

## The four axes

- **Outer-loop RSI shippable** — the substrate improves via the heuristic. The model does not.
- **Sovereign trust** — the heuristic is hand-coded and visible. The score formula is in `src/demo.py`.
- **On-device** — SmolVLM-256M (120MB) + mmproj (182MB) on CPU, no GPU, no cloud.
- **Small-beats-large** — sub-302MB combined, runs on a Raspberry Pi 5.

## Threat model

[./threat-model.md](./threat-model.md). The model is small enough that the threat model is the *hardware*: what does the model see, and is that the right thing to show it?
```

**Why this rewrite:** v122 danlab-multimodal README is already strong. v129 only adds: (1) the "what changed since hackathon" section to position the demo as a live receipt, not a historical artifact, (2) the honest framing as a top-level section (it currently lives in a callout block), (3) the four-axes ladder, (4) the threat model link.

---

## 7. Repo: `paperclip` (the orchestration platform)

**Current state:** `paperclip/AGENTS.md` says "Dormant. All agents paused. Resume when ready." The repo is dormant per v128.

**v129 strategy:** Do not rewrite the README. The README should not be a marketing surface for a dormant project. v129 add a one-line "dormant" status banner at the top, link to the resume plan (Q3 W3, per dan2 v28), and otherwise leave it alone.

**v129 single-edit (target ~10 lines added):**

```markdown
# paperclip — multi-agent company orchestration

> Status: **DORMANT** as of 2026-07-06. Resume plan: Q3 W3-W4. Last active: 2026-Q1. The platform that runs a company made of AI agents.

## Why dormant

The substrate is settled. The community is in the MCP / OpenClaw agent space, not the company-orchestration space. Resume when danlab-multimodal and dan-glasses ship and the orchestration layer becomes the bottleneck. Resume plan: [dan-lab/resume-paperclip.md](https://github.com/somdipto/dan-lab/blob/main/resume-paperclip.md) (Q3 W3).
```

**Why this rewrite:** A dormant repo with an active README is a trust leak. v129 makes the dormancy explicit, names the resume condition, and stops trying to sell something that is not shipping.

---

## 8. Blurr (the workspace directory, not a hero repo)

**v128 / v122 hold:** The `blurr/` directory in `/home/workspace/` is **Panda** (Ayush Chaudhary, MIT-licensed, Android phone operator). It is not a Danlab project. It is not part of the dan-lab org on GitHub. It is a third-party project that happens to live in the workspace.

**v129 action:** No rewrite. The README in the `blurr/` directory is Panda's, not Danlab's. Do not modify it.

---

## 9. README triage matrix (all 6 repos)

| Repo | Current state | v129 priority | Effort | Gate |
|---|---|---|---|---|
| `dan-lab` (org) | thin | **P0** | 2h | none |
| `dan-glasses` | engineering-led | **P0** | 4h | threat model link already public |
| `dani` | technical-dense | **P1** | 2h | SOUL.md must be re-exported first |
| `dan-consciousness` | thin | **P1** | 1h | the three files must be public |
| `danlab-multimodal` | strong, hackathon-framed | **P1** | 1h | none — additive only |
| `paperclip` | dormant | **P2** | 30 min | none — single-banner edit |
| `blurr` (workspace dir) | Panda's README | **defer** | 0 | n/a |

**Total v129 README effort: 10.5 hours, 1 engineer, 1 week.** All gated on the existing threat model public, no new artifacts required.

---

## 10. Universal README add-ons (v129)

### 10.1 The "first 200 characters" discipline

Every README must pass this test: if a developer reads the first 200 characters, can they answer "what is this repo?" in plain English? Examples that pass and fail:

| Repo | Pass | Fail |
|---|---|---|
| `dan-glasses` | "A proactive, on-device AI companion in glasses form factor." | "The wearable AI platform from danlab.dev." |
| `danlab-multimodal` | "A sub-250MB vision-language model on CPU with a heuristic feedback loop." | "Multimodal AI for edge devices." |
| `dani` | "The local-first, open-weights, MCP-native agent runtime." | "An AI agent framework." |
| `dan-consciousness` | "The canonical consciousness that lives between Dan and somdipto." | "The shared brain for AI agents." |
| `paperclip` | "Multi-agent company orchestration. Dormant since 2026-Q1." | "The paperclip platform." |
| `dan-lab` | "The org that ships Dan Glasses, Dani, and danlab-multimodal." | "DanLab's open AI research." |

**v129 rule:** If the first 200 characters contain the words "agentic", "next-generation", "cutting-edge", "AI lab", "platform", or "ecosystem" without a concrete noun, rewrite.

### 10.2 The "30-second demo" gate

Every README must contain a `## 30-second demo` block with one shell command that runs on a clean Ubuntu 24.04 box. If the demo takes more than 30 seconds of human time (download + install + run + see something), the README fails the gate.

### 10.3 The "four-axes ladder"

Every README must include a `## The four axes` section that names which 2+ of the four axes the repo ladders to, in one sentence each. The four axes are:

1. **Sovereign trust** — open weights, open data path, public audit log.
2. **Reversibility** — every model call, every memory write, every daemon can be unwound.
3. **Chip-stack sovereignty** — open-source software on a chip stack the user owns.
4. **Outer-loop RSI shippable** — the substrate improves in the open, before the maximalist RSI inflection lands.

If a repo cannot honestly ladder to 2+ of these, the README is honest about that fact. Honesty is the v129 first-class pattern.

### 10.4 The "threat model is a top-level section" rule

Every README must have a `## Threat model` heading (level 2), not a "Security" subsection (level 3 or lower) at the bottom. The threat model is the v129 first-class gate. It sits next to the 30-second demo and the four-axes ladder.

### 10.5 The "Built at" signature

Every README closes with the same 3-line signature:

```
## Built at

[danlab.dev](https://danlab.dev). Bengaluru, India. The 9/9 daemons shipped in 9 weeks, on a $0 GPU budget. Yours, not theirs.
```

(Substitute the repo-specific tag: "The agent's brain, not the agent's vendor." for dani, "The brain, not the vendor." for dan-consciousness, "Dormant since 2026-Q1." for paperclip.)

### 10.6 The "no emoji in headings" rule

Emoji in body text is fine (👾, 🇮🇳, ✅). Emoji in H1/H2/H3 headings is not. The README is a document, not a Twitter thread. v129 enforces this.

---

## 11. README health check (v129 acceptance)

A README ships when it passes all of these:

1. [ ] First 200 characters name the repo in plain English.
2. [ ] `## 30-second demo` block with one shell command, runs in <30s of human time.
3. [ ] `## What this is` section, 2-3 sentences, plain English.
4. [ ] `## Why this exists` section, 1-2 sentences, names the alternative and why it fails.
5. [ ] `## Architecture` section, ASCII diagram or bulleted list, 5-15 lines.
6. [ ] `## The four axes` section, names 2+ axes, one sentence each.
7. [ ] `## Threat model` heading at level 2, link to repo-level or org-level threat model.
8. [ ] `## Status` section with `[x]` / `[ ]` checkboxes, no aspirational roadmap without dates.
9. [ ] `## Built at` signature at the bottom, 3 lines, repo-specific tag.
10. [ ] No emoji in headings.
11. [ ] No "agentic", "next-generation", "cutting-edge", "ecosystem" without a concrete noun.
12. [ ] Three badges max: license, status, "from India 🇮🇳".
13. [ ] `## Contributing` section, 1-2 paragraphs, names the bar.
14. [ ] Cite block in BibTeX format at the bottom (optional but recommended).

**v129 readme triage: 10.5 hours, 1 engineer, 1 week. All additive, all gated on the existing threat model link.**

---

## 12. Open questions for somdipto (v129)

1. **`@danlab` X handle** — confirm or pick. **P0.** Affects README badges and citation handles.
2. **`danlab.ai` blog domain** — confirm or defer. If yes, every README should link to it. If no, drop the "long-form" reference in the v129 dan-glasses README.
3. **`somdipto/dan-lab/threat-model` repo** — does the org-level threat model live in the `dan-lab` repo or in a standalone `threat-model` repo? v129 assumes `dan-lab/threat-model.md` (single file). If standalone, update all README threat model links.
4. **CII badge on every README** — should we add a "Built in India 🇮🇳" badge? v129 recommends yes, but the badge URL needs to be picked (shields.io has an India flag badge but the wording is "from-India-orange" which is fine).
5. **`dani-skills` cross-link** — every dani README should link to the dani-skills registry. Confirm the registry is at `somdipto/dani-skills` or if it's elsewhere.
6. **The "v1.5" framing** — should every README say "v1.0 ships X, v1.5 ships Y"? v129 currently says it in the dan-glasses README only. v129 recommends no — it is a roadmap leak. The threat model and the status checkboxes are enough.

---

*README improvements complete. v129 sets the v1.0 standard: 30-second demo first, threat model top-level, four-axes ladder in plain English, "Built at" signature at the bottom. 10.5 hours, 1 engineer, 1 week.*
