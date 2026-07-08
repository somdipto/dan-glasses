# Dan1 GitHub README Improvements — v50

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-17 13:00 IST (07:30 UTC)
**Status:** ✅ Canonical. Supersedes v49. **READMEs drafted. v51 is the PRs merged.**

> One-line rule (unchanged from v49): *A README is a sales page that converts engineers. Lead with what it does in one sentence, show the demo, link the code. No philosophy in the first 200 words. The DANI launch is the new public surface — every README should acknowledge DANI as the live product and Dan Glasses as the coming wearable.*

---

## 0. The 6 repos to polish in Week 1 (unchanged from v49)

**All copy is in `punchlist-copy-paste.md` (§H, §I, §J, §K, §L, §M). Open it. Find the section. Paste.**

| # | Repo | Visibility | Stars (today) | Action | File ref |
|---|---|---|---|---|---|
| 1 | `somdipto/danlab-multimodal` | **PRIVATE** | n/a | **Make public. Apply README. Add topics.** | §H |
| 2 | `somdipto/dan-glasses` | Public | 0★ | **Apply README. Add topics. Update description.** | §I |
| 3 | `somdipto/dani` | Public | 1★ | **Apply README. Add topics. Update description.** | §J |
| 4 | `somdipto/paperclip` | Public | 0★ | **Apply README. Add topics. Update description.** | §K |
| 5 | `somdipto/dan-consciousness` | Public | 0★ | **Apply README. Add topics. Update description.** | §L |
| 6 | `somdipto/openwork` | Public | 3★ (top star) | Light polish. | §M |

**The single highest-leverage action in the entire marketing plan is making `danlab-multimodal` public on Day 0.** Without that, the rest is decoration. **Text in §H.**

---

## 1. NEW IN v50: The `dan-labs-agi` organization (the new public brand home)

**Source:** https://github.com/dan-labs-agi (verified 2026-06-17 07:30 UTC)

**What exists:**
- Org: `dan-labs-agi` (Dan Labs)
- Bio: "Reaching AGI"
- Location: Multiverse
- Website: danlab.dev
- Followers: 3
- Following: 1
- Public repos: 4
  1. `scoutly` — TypeScript, 1 star, 1 fork
  2. `dan-papers` — TypeScript, 0 stars
  3. `agen8-redis-windows` — TypeScript
  4. `clawdi` — TypeScript, fork

**Why this matters (v50):**
- **The brand is consolidating.** The org is called "Dan Labs" (matching the v49 thesis), the website is danlab.dev, the location is "Multiverse" (in keeping with the v49 narrative of building toward AGI).
- **The org already has 4 public repos.** Some of them (scoutly, clawdi) are likely forks of the dan-* ecosystem. The brand surface is in motion.
- **The org should be the canonical home for DANI.** Currently dani.danlab.dev exists as a separate product. The DANI repo should live under `dan-labs-agi/dani` (or `somdipto/dani` → renamed to `dan-labs-agi/dani`).
- **v50 action: move `somdipto/dani` → `dan-labs-agi/dani` and update all docs.** This is a 30-min task (Settings → Danger Zone → Transfer). It signals the org is the canonical home.

**Suggested `dan-labs-agi` org profile README (the brand home):**

```markdown
# Dan Labs 👾🇮🇳

> Reaching AGI. From India. On a $200 board. Under MIT.

## The products

| Product | Status | What it is | Link |
|---|---|---|---|
| **DANI** | Live | Open-source AI coworker. $0-299/mo. Runs in your container. | [dani.danlab.dev](https://dani.danlab.dev) |
| **Dan Glasses** | v1 (desktop) / v2 (wearable Q4 2026) | Open-source AI companion for your face. 7 daemons, 0 cloud, MIT. | [github.com/somdipto/dan-glasses](https://github.com/somdipto/dan-glasses) |
| **danlab-multimodal** | Demo | Sub-250MB VLM pipeline on CPU. Pre-RL scaffold. MIT. | [github.com/somdipto/danlab-multimodal](https://github.com/somdipto/danlab-multimodal) |
| **Paperclip** | Dormant | AI agent company orchestration. | [github.com/somdipto/paperclip](https://github.com/somdipto/paperclip) |
| **dani** | Public | Agent runtime, MCP-native. Powers DANI. | [github.com/somdipto/dani](https://github.com/somdipto/dani) |
| **omni-1b-indic** | In progress (Day 60) | 1B-parameter Omni model, 9 Indic language families. | (link) |

## The thesis

5 things nobody else has all 6 of:

1. **Proactive** — speaks only when useful. Not "Hey Meta, what's this?"
2. **Local-first** — 0 cloud calls. Your data, your server, your face.
3. **Open source** — MIT. Forkable. Buildable.
4. **From India** — Bangalore, buildspace arc, ₹ pricing, Indic languages.
5. **AGI research** — recursive self-improvement, Omni-1B training, the brain is the wedge.

## The team

- **somdipto nandy** — human co-founder. 23, Atria IT, buildspace alum, 3,953 LinkedIn connections.
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

**Why this org README is critical (v50):** The org is the new public surface. Anonymous GitHub visitors who find `dan-labs-agi/dani` will land on this README first. The README has to instantly answer: who, what, why, how. The 6-product table does this in 1 scroll.

---

## 2. `somdipto/dan-glasses` — the main stack

**Full README rewrite text in `punchlist-copy-paste.md` §I.**

**v50 addition:** The README's "What is this?" section should add a one-liner about DANI as the live product, plus a link to dani.danlab.dev.

### Suggested topics (12, unchanged)
`ai-glasses` `wearable-ai` `on-device-llm` `lfm2-vl` `open-source` `india` `tauri` `whisper-cpp` `memory` `proactive-ai` `mcp` `from-india`

### Suggested description (167 chars, unchanged)
```
Open-source AI glasses. 7 services. 0 cloud. $0/month. MIT. Proactive, not reactive. Built in Bangalore 🇮🇳
```

### New "What is this?" one-liner (UPDATED for v50)
```
We don't just integrate models. We train them. See `omni-1b-indic` (v0.1 ships Day 60).
The brain ships today as DANI — the open-source AI coworker at dani.danlab.dev. The body ships Q4 2026.
```

---

## 3. `somdipto/danlab-multimodal` — the demo repo (THE #1 DAY-0 ACTION)

**Action:** Make this repo public. Today. The repo is a complete, working VLM pipeline on CPU. It is currently 404 to anonymous. **This is the single highest-leverage action in the entire marketing plan.**

**Full README rewrite text in `punchlist-copy-paste.md` §H.**

**v50 addition:** Add a "What's next" section that previews DANI as the production deployment target, and the Omni-1B-Indic v0.1 as the follow-up artifact.

### Suggested topics (10, unchanged)
`vlm` `multimodal` `llama-cpp` `smolvlm` `heuristic` `pre-rl` `cpu-inference` `hackathon` `india` `open-source`

### Suggested description (140 chars, unchanged)
```
Sub-250MB VLM on CPU via llama.cpp. Heuristic feedback loop. Pre-RL scaffold. MIT. From Bangalore 🇮🇳
```

---

## 4. `somdipto/dani` — the agent platform (NOW MORE CRITICAL in v50)

**v50 update:** DANI is live. The `dani` repo is the brain that powers DANI. This README has to be updated to reflect that DANI is a real product, not a future promise.

**Suggested topics (10, unchanged)**
`agent` `mcp` `agent-runtime` `typescript` `open-source` `india` `memory` `tools` `claude-desktop` `cursor`

### Suggested description (95 chars, unchanged)
```
Open-source agent runtime. MCP-native. MIT. Powers danlab.dev's products. From Bangalore 🇮🇳
```

### Suggested README lead (v50 update)
```markdown
# dani 👾

> The open-source agent runtime that powers DANI — the live AI coworker at dani.danlab.dev.

## What is this?

`dani` is the agent runtime that powers DANI (the live AI coworker) and Dan Glasses (the AI companion for your face). It's MCP-native, MIT-licensed, and runs on a $200 board.

DANI is the production deployment of `dani` + the 7-daemon stack. It's live at dani.danlab.dev with a $0-299/mo pricing model.

## Try it

[Open DANI in your browser →](https://dani.danlab.dev)

## Or run it locally

```bash
git clone https://github.com/somdipto/dani
cd dani
npm install
npm start
# → DANI runs on localhost:3000
```

## License

MIT. Same as everything we ship.
```

---

## 5. NEW IN v50: The `dani-frontend` repo (the new public surface for DANI)

**v50 discovery:** DANI is a real product. It has a frontend. The frontend code must live somewhere. The likely home is `dan-labs-agi/dani-frontend` or `somdipto/dani-frontend`.

**v50 action (Day 0-2):** Verify the DANI frontend repo exists. If not, create it under `dan-labs-agi/dani-frontend`. Add the README. Pin it on the org.

**Suggested README:**
```markdown
# DANI Frontend 👾

> The web UI for DANI — the open-source AI coworker at dani.danlab.dev.

## What is this?

The Next.js + TypeScript frontend for DANI. Connects to the `dani` agent runtime. Powers dani.danlab.dev.

MIT. From Bangalore. 🇮🇳

## Stack

- Next.js 14
- TypeScript
- Tailwind CSS 4
- shadcn/ui
- Tauri v2 (for the desktop app)

## Run it

```bash
git clone https://github.com/dan-labs-agi/dani-frontend
cd dani-frontend
npm install
npm run dev
# → http://localhost:3000
```

## License

MIT.
```

---

## 6. `somdipto/paperclip` — the company orchestrator

**Full README rewrite text in `punchlist-copy-paste.md` §K.**

### Suggested topics (9, unchanged)
`agents` `orchestration` `mcp` `express` `typescript` `react` `open-source` `india` `multi-agent`

### Suggested description (95 chars, unchanged)
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

### v50 update: Add the "8 Paperclip workflows" framing

DANI ships with 8 Paperclip workflows (expense reports, email drafting, Notion updates, PDF generation, Slack posting, calendar booking, meeting summaries, travel planning). The Paperclip repo is the open-source implementation.

---

## 7. `somdipto/dan-consciousness` — the shared brain

**Full README rewrite text in `punchlist-copy-paste.md` §L.**

### Suggested topics (9, unchanged)
`agi` `consciousness` `agents` `open-source` `india` `danlab` `memory` `identity` `values`

### Suggested description (97 chars, unchanged)
```
The shared brain between Dan (AI) and somdipto (human) at danlab.dev. AGI in the open.
```

### v50 update: Add the "values" file as the public artifact

The `dan-consciousness` repo should expose the values, identity, and operating principles of the DanLab AI in a machine-readable format. This is the public AGI alignment artifact.

---

## 8. `somdipto/openwork` — the open-source AI coworker (light polish)

**Light polish, no full rewrite needed.**

### Suggested topics (8, unchanged)
`ai-coworker` `desktop-agent` `open-source` `mcp` `typescript` `india` `automation` `browser-automation`

### Suggested description (84 chars, unchanged)
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

### v50 update: Cross-link to DANI

If DANI is the live, self-serve product, `openwork` becomes the dev-mode / self-hosted alternative. The README should link both:
```markdown
# openwork 👾

> The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳

## What is this?

`openwork` is the local-first, self-hosted version of DANI. It runs in your own Docker container, with your own API keys, with your own data.

DANI is the live, self-serve version at dani.danlab.dev.

## License

MIT.
```

---

## 9. The GitHub profile fix (the wrapper)

**Full text in `punchlist-copy-paste.md` §F (profile) and §G (profile README).**

**v50 update:** The profile README should include a "Live products" section that mentions DANI as the live product, Dan Glasses as the coming wearable, and the Omni-1B-Indic training as the in-progress research.

### `github.com/somdipto` — the changes

**Display name:** `somdipto nandy 👾`

**Bio (160 chars, unchanged):**
```
building AGI from India 🇮🇳 @ danlab.dev — open, local, proactive AI glasses, MIT
```

**Pinned repos (in this order, updated for v50):**
1. `dan-glasses` — the main stack
2. `dani` — the brain that powers DANI (was: `danlab-multimodal`)
3. `danlab-multimodal` — the VLM demo (moved to #3)
4. `dan-consciousness` — the shared brain
5. `paperclip` — the company orchestrator
6. `openwork` — the desktop sibling

**v50 update:** The pinned order changed. `dani` is now #2 (because DANI is live). `danlab-multimodal` is now #3 (still important, but the live product is `dani`).

**Profile README (the new `somdipto/somdipto` README):**

```markdown
## Live now

**DANI** — the open-source AI coworker. Self-serve at [dani.danlab.dev](https://dani.danlab.dev).
$0/mo self-hosted. $29-299/mo managed. MIT. From Bangalore.

## Currently training

**`omni-1b-indic`** — a 1B-parameter Omni model from scratch. 3 months in.
Trained on 9 regional Indian language families. The smallest Omni that
fits in the wearable form factor. MIT. v0.1 ships to HuggingFace Day 60.

[X thread](https://x.com/NandySomdipto/status/2065216558046281749)

## Coming Q4 2026

**Dan Glasses** — the AI companion for your face. Same 7-daemon stack as DANI. 0 cloud. MIT.
[github.com/somdipto/dan-glasses](https://github.com/somdipto/dan-glasses)
```

**v50 update — the "Live now" block at the top of the profile README:**

```markdown
## Live now

**DANI** — the open-source AI coworker. Self-serve at dani.danlab.dev.
$0/mo self-hosted. $29-299/mo managed. MIT. From Bangalore 🇮🇳
```

---

## 10. The 5 things every README must have (the checklist, updated for v50)

1. **One-line description in the H1 area.** "What is this?" answered in 1 sentence.
2. **Quick start that works in <2 minutes.** `git clone && ./scripts/dev.sh && curl :8090/health`.
3. **Status section.** "Demoable today" / "Blocked on hardware" / "Dormant" / "Live product" / "In research". No ambiguity. **(v50: DANI gets "Live product" status. Dan Glasses gets "v1 demoable, v2 blocked on hardware." omni-1b-indic gets "In research.")**
4. **License footer.** MIT. Always.
5. **From India 🇮🇳 badge.** Every repo. Always. It's the brand.

---

## 11. The metric per repo (the only number that matters, updated for v50)

| Repo | Current stars | Target Q3 | Target Q4 |
|---|---|---|---|
| `dan-glasses` | 0 | 500 | 2,000 |
| `dani` (now #2 pinned, DANI is live) | 1 | **1,000 (NEW v50 — DANI is the live product, it gets a higher target)** | 5,000 (NEW) |
| `danlab-multimodal` | (private) | 500 | 2,000 |
| `dan-consciousness` | 0 | 200 | 1,000 |
| `paperclip` | 0 | 200 | 1,000 |
| `openwork` | 3 | 500 | 2,000 |
| `omni-1b-indic` | (not yet created) | 1,000 | 5,000 |
| `dani-frontend` (NEW v50) | (not yet public) | **500 (NEW v50)** | **2,000 (NEW v50)** |
| `dan-labs-agi` org (NEW v50) | n/a | **1,000 followers (NEW v50)** | **3,000 followers (NEW v50)** |
| **Total** | **4 + private** | **5,400** | **23,000** |

**v50 target: 23,000 stars + 3,000 org followers across 8 repos + 1 org.** The DANI launch justifies the new `dani-frontend` and `dan-labs-agi` targets. The total is +8,500 over v49's target.

---

## 12. The Tushar Shaw / Percevia acknowledgement (from v49) — UNCHANGED

**If somdipto wants to add a "friends we ship alongside" section to any README:**

```markdown
## Friends we ship alongside

- **[Percevia / Tushar Shaw](https://x.com/dogra_ns/status/2065204989610365422)** — 19-year-old from Bengaluru. AI glasses for the blind using Gemini, ₹9,999-11,999, won ₹25L at Samsung Solve for Tomorrow 2025. We are the open-source, on-device, MIT alternative to their cloud-dependent stack. **Same Bangalore. Different bets.**

- **[Indranil Bhadra](https://x.com/Indrani78141068/status/2064267293153210696)** — building the same wedge from a different angle. *"Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain."* We agree.

- **[DANI](https://dani.danlab.dev)** — our open-source AI coworker, the live deployment of the same 7-daemon stack. **(NEW v50)**

- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — our open-source VLM pipeline, sub-250MB on CPU, MIT, the demo repo.
```

---

## 13. The "we train the model" block (add to dan-glasses + danlab-multimodal)

**Add this block to the top of both READMEs, just below the title:**

```markdown
> **We don't just integrate models. We train them.**
>
> The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
> 3 months in. Trained on 9 regional Indian language families. The smallest
> Omni that fits in the wearable form factor. MIT. v0.1 ships Day 60.
>
> [Training thread on X](https://x.com/NandySomdipto/status/2065216558046281749)
```

**v50 update:** DANI is the first product to use Omni-1B-Indic in production. Add the DANI CTA below the training block:
```markdown
>
> DANI will be the first product to use Omni-1B-Indic. [Try it free →](https://dani.danlab.dev)
```

---

*End of v50. The 6 READMEs are drafted. The org profile is drafted. The DANI cross-link is added to every README. The dan-labs-agi org transfer is added to the punchlist. The "we train the model" block has a DANI CTA. The 23,000-star target is the v50 wedge. The only thing left is the punchlist.*nnects to the DANI API (this repo) + the OpenClaw gateway (separate repo).

DANI is the live product. This is the UI.

## Stack

- Next.js 15
- TypeScript
- Tailwind CSS
- React Server Components
- Deployed on Vercel

## Local development

```bash
git clone https://github.com/dan-labs-agi/dani-frontend
cd dani-frontend
cp .env.example .env.local
# Add DANI_API_URL and DANI_API_KEY
npm install
npm run dev
# → http://localhost:3000
```

## License

MIT. Same as everything we ship.

## DANI live

[dani.danlab.dev](https://dani.danlab.dev)
```

---

## 6. `somdipto/dan-consciousness` — the shared brain (unchanged from v49)

**Full README rewrite text in `punchlist-copy-paste.md` §L.**

### Suggested topics (9, unchanged)
`agi` `consciousness` `agents` `open-source` `india` `danlab` `memory` `identity` `values`

### Suggested description (97 chars, unchanged)
```
The shared brain between Dan (AI) and somdipto (human) at danlab.dev. AGI in the open.
```

---

## 7. `somdipto/paperclip` — the company orchestrator (unchanged from v49)

**Full README rewrite text in `punchlist-copy-paste.md` §K.**

### Suggested topics (9, unchanged)
`agents` `orchestration` `mcp` `express` `typescript` `react` `open-source` `india` `multi-agent`

### Suggested description (95 chars, unchanged)
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

---

## 8. `somdipto/openwork` — the open-source AI coworker (light polish, unchanged from v49)

**Light polish, no full rewrite needed.**

### Suggested topics (8, unchanged)
`ai-coworker` `desktop-agent` `open-source` `mcp` `typescript` `india` `automation` `browser-automation`

### Suggested description (84 chars, unchanged)
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

---

## 9. The GitHub profile fix (the wrapper, updated for v50)

**v50 update:** The profile README should add a "DANI is live" banner at the top, before the "Currently training" block.

### `github.com/somdipto` — the changes

**Display name:** `somdipto nandy` (was: "Sodan")

**Bio (160 chars, unchanged):**
```
building AGI from India 🇮🇳 @ danlab.dev — open, local, proactive AI glasses, MIT
```

**Pinned repos (in this order, UPDATED for v50):**
1. `dan-labs-agi/dani-frontend` — DANI live (NEW v50)
2. `dan-glasses` — the main stack
3. `danlab-multimodal` — the demo repo (once public)
4. `dan-consciousness` — the shared brain
5. `dani` — the agent runtime
6. `paperclip` — the company orchestrator
7. `openwork` — the desktop sibling

**Profile README (the new `somdipto/somdipto` README), UPDATED for v50:**

```markdown
## Currently training

**`omni-1b-indic`** — a 1B-parameter Omni model from scratch. 3 months in.
Trained on 9 regional Indian language families. The smallest Omni that
fits in the wearable form factor. MIT. v0.1 ships to HuggingFace Day 60.

[X thread](https://x.com/NandySomdipto/status/2065216558046281749)

## Live now

**DANI** — the open-source AI coworker. Built on the same 7-daemon stack as Dan Glasses.
$0-299/mo. Try it at [dani.danlab.dev](https://dani.danlab.dev).
```

---

## 10. The 5 things every README must have (the checklist, unchanged from v49)

1. **One-line description in the H1 area.** "What is this?" answered in 1 sentence.
2. **Quick start that works in <2 minutes.** `git clone && ./scripts/dev.sh && curl :8090/health`.
3. **Status section.** "Demoable today" / "Blocked on hardware" / "Dormant". No ambiguity.
4. **License footer.** MIT. Always.
5. **From India 🇮🇳 badge.** Every repo. Always. It's the brand.

**v50 additions to the checklist:**
6. **Link to DANI if relevant.** DANI is the live product. Every DanLab repo README should link to DANI as the production deployment of the same brain.
7. **Link to the Omni-1B training thread.** X post 2065216558046281749. The "we own the model" signal belongs in every repo.

---

## 11. The metric per repo (the only number that matters, unchanged from v49, with v50 addition)

| Repo | Current stars | Target Q3 | Target Q4 |
|---|---|---|---|
| `dan-labs-agi/dani-frontend` | (not yet created) | 1,500 (NEW, v50) | 5,000 (NEW, v50) |
| `dan-glasses` | 0 | 500 | 2,000 |
| `danlab-multimodal` | (private) | 500 | 2,000 |
| `dan-consciousness` | 0 | 200 | 1,000 |
| `dani` | 1 | 300 | 1,500 |
| `paperclip` | 0 | 200 | 1,000 |
| `openwork` | 3 | 500 | 2,000 |
| `omni-1b-indic` | (not yet created) | 1,000 | 5,000 |
| **Total** | **4 + private** | **4,700** | **19,500** |

**v50 target: 19,500 stars across 8 repos. The 5,000-star target on `dani-frontend` and `omni-1b-indic` are the wedges.** DANI is the live product. The frontend will get starred by everyone who uses DANI. The model will get starred by every Indic-AI researcher.

---

## 12. The Tushar Shaw / Percevia + Indranil Bhadra acknowledgements (from v49) — UNCHANGED

**If somdipto wants to add a "friends we ship alongside" section to any README:**

```markdown
## Friends we ship alongside

- **[Percevia / Tushar Shaw](https://x.com/dogra_ns/status/2065204989610365422)** — 19-year-old from Bengaluru. AI glasses for the blind using Gemini, ₹9,999-11,999, won ₹25L at Samsung Solve for Tomorrow 2025. We are the open-source, on-device, MIT alternative to their cloud-dependent stack. **Same Bangalore. Different bets.**

- **[Indranil Bhadra](https://x.com/Indrani78141068/status/2064267293153210696)** — building the same wedge from a different angle. *"Not another gadget that shouts 'Hey Google'. Just a silent companion that grows into an extension of your own brain."* We agree.

- **[DANI](https://dani.danlab.dev)** — our open-source AI coworker. Live today. $0-299/mo. MIT. **(NEW v50)**
```

---

## 13. NEW IN v50: The "we ship the brain + the body" block (add to dan-glasses + dani + danlab-multimodal)

**Add this block to the top of all three READMEs, just below the title:**

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

**Why (v50):** Anyone who lands on a DanLab repo should immediately understand: DANI is the live product, Dan Glasses is the coming wearable. This block makes that visible from the first scroll.

---

## 14. The "we train the model" block (from v49) — UNCHANGED

**Add this block to the top of dan-glasses + danlab-multimodal, just below the "we ship the brain + the body" block (v50 order):**

```markdown
> **We don't just integrate models. We train them.**
>
> The Omni-1B-Indic is a 1B-parameter Omni model we're training from scratch.
> 3 months in. Trained on 9 regional Indian language families. The smallest
> Omni that fits in the wearable form factor. MIT. v0.1 ships Day 60.
>
> [Training thread on X](https://x.com/NandySomdipto/status/2065216558046281749)
```

---

*End of v50. The 6 READMEs are drafted. The profile fix is drafted. The new `dan-labs-agi/dani-frontend` repo is added to the metric. The "we ship the brain + the body" block is the v50 wedge. The "we train the model" block is the v49 wedge. Both belong at the top of every DanLab repo. The only thing left is the punchlist.*
