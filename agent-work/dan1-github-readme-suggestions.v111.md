# GitHub README Improvements — Run v111
**Date:** 2026-07-01
**Owner:** DAN-1
**Scope:** Eight repos in the DanLab org + the personal `somdipto` repos.
**Severity scale:** P0 = blocks credibility with devs, P1 = matters for SEO / first 30s, P2 = polish.
**v111 delta:** Adds a section for `@danlab_bot` + OpenClaw integration. Updates test counts to the v111 verified numbers (150+ audiod, 8/8 perceptiond, 8/8 perceptiond v5 MJPEG viewfinder). Adds a new `STATUS.md` pattern. Calls out the `danlab.dev` legacy content problem.

---

## 0. Why this matters

The README is the *only* first impression a developer gets. Most of our repos will be evaluated in under 30 seconds by a technical reader. We optimize for these specific reader personas, in this priority order:

1. **The senior backend engineer** evaluating Paperclip vs LangChain vs Temporal.
2. **The ML infra engineer** evaluating danlab-multimodal vs Ollama / Llama.cpp wrappers.
3. **The AI researcher** evaluating dan-consciousness as a credible open-source AGI project.
4. **The Indian AI/ML student** discovering the org via one well-ranked repo.

Every README must serve at least persona 1 and persona 3.

---

## 1. Universal README rules (apply to every repo)

### 1.1 First 200 characters

The README's first 200 characters appear in the GitHub repo header, in search results, in `git clone` output, and (sometimes) when pasted into a tweet. This block must contain:

- **One sentence** describing what the repo is (≤ 25 words).
- **One sentence** describing why it exists (≤ 25 words).
- **A badge row** that anchors the project in a specific category.
- **A `Quick Start` link** (not the command yet — the link, so the README itself stays compact).

### 1.2 Badge row template

```
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status: Active](https://img.shields.io/badge/status-active-brightgreen)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
```

Add domain-specific badges *only* if they are real signals (model size, test count, deps), not vanity badges.

### 1.3 The "1-Click Demo" rule

Every repo should have at least one code block a reader can copy-paste in 60 seconds that demonstrates the most interesting claim of the repo. If the demo requires 5 dependencies and a Docker network, it is not a 1-click demo.

### 1.4 The "Why this and not X" rule

Every README must contain one sentence comparing to a specific alternative. Without this, the README reads like marketing copy and gets dismissed.

### 1.5 The "Who maintains this" rule

Every README must end with a maintainer line. In our case: `Maintained by [@somdipto](https://github.com/somdipto) and the DanLab AI team, Bengaluru 🇮🇳.`

### 1.6 The "Status" rule (v111 update)

Every README must include a `## Status` section with the current state of the repo, in plain text. "Active development, v1 target Q3 2026" beats silence. **v111 add:** include the current test count and the last verified-on date. This is the cheapest way to win trust from a senior engineer.

Example:

```
## Status

Verified live 2026-07-01. 9/9 daemons up. 150+ audiod tests passing. 8/8 perceptiond tests passing.
```

### 1.7 The "STATUS.md" pattern (v111 NEW)

For the `dan-glasses` repo (the most important one), ship a top-level `STATUS.md` that lists every daemon, every port, and a `curl` command to verify each. The file is what senior engineers will land on when they `gh repo view` and click "files". The pattern:

```markdown
# Dan Glasses — Status

Verified 2026-07-01 (v111 re-baseline).

| Service       | Port  | Health command                                       | Status |
|---------------|-------|------------------------------------------------------|--------|
| audiod        | 8090  | `curl localhost:8090/status`                         | ✅ live |
| dan-glasses-app | 8091 | `curl localhost:8091/`                               | ✅ live |
| memoryd       | 8092  | `curl localhost:8092/stats`                          | ✅ live |
| perceptiond   | 8741  | `curl localhost:8741/status`                         | ✅ live |
| toold         | 8742  | `curl localhost:8742/health`                         | ✅ live |
| ttsd          | 8743  | `curl localhost:8743/health`                         | ✅ live |
| os-toold      | 8744  | `curl localhost:8744/`                               | ✅ live |
| openclaw-web  | 18789 | `curl localhost:18789/`                              | ✅ live |
| percmcp       | 3888  | `curl localhost:3888/`                               | ✅ live |

**One-shot verification:**

```bash
for p in 8090 8091 8092 8741 8742 8743 8744 18789 3888; do
  printf ":%-6s " $p
  curl -s --max-time 2 http://localhost:$p/status || echo down
done
```

**Telegram channel:** @danlab_bot online via OpenClaw 2026.5.28.
```

This file replaces the static "9/9 daemons" badge with a curl-able proof artifact. Costs 30 lines. Pays for itself in a single day of inbound interest.

---

## 2. Repo-by-repo improvements

### 2.1 `github.com/somdipto/dan-glasses` (the wearable repo)

**Current state:** Has README but no badges, no 1-click demo, no comparison sentence, no maintainer footer. **v111 add:** no `STATUS.md`.

**P0 changes:**

1. Add badge row at the top with: License MIT, Status Active, From India, Tests passing (150+), 9 daemons live, Sub-10W power.
2. Add a "1-click demo" section:
   ```bash
   git clone https://github.com/somdipto/dan-glasses && cd dan-glasses
   ./scripts/up.sh
   ```
   The script must be runnable in under 60 seconds (it exists, but it needs a one-paragraph README section advertising it).
3. Add a "Why this and not Meta Ray-Ban / Quark" paragraph at line 5 of the README. Three concrete architectural differences, not adjectives.
4. **v111:** Add a top-level `STATUS.md` (see §1.7). This is the new P0 — the file that proves "9/9 live" is real.

**P1 changes:**

5. Add a `## Status` section with the May 2026 milestone (9 daemons live, 150 audiod tests passing, 8/8 perceptiond tests passing).
6. Add a `## Architecture` section that points to the architecture PDF in `docs/`.
7. Add a `## Hardware status` section with a HONEST paragraph about Redax blocker. **v111:** also note that Telegram does not depend on Redax or Tailscale.
8. Add `## Contributing` and `## License` sections (currently missing — biggest credibility gap).
9. Add `## Maintainer` line at the end.
10. **v111:** Add a "Try it on Telegram" block at the top — `DM @danlab_bot`. This is the lowest-friction entry point for a curious developer.

**P2 changes:**

11. Add a hero screenshot of the VisionDashboard component.
12. Add a one-page diagram (architectural layers) as `docs/architecture-diagram.png`.

---

### 2.2 `github.com/somdipto/danlab-multimodal` (the public demo)

**Current state:** Already best-of-class in the DanLab org. Strong badge row, has a demo, has a build-from-scratch recipe. **v111 add:** the demo is now hosted on zo.pub and the link is canonical.

**P0 changes:**

1. Add a top-of-README callout box explaining "This is heuristic, not RL." Style as a markdown quote with a ⚠️ icon. (Adds honesty bonus, not just SEO.)
2. Add a direct link back to `github.com/somdipto/dan-lab` (the org) for "what else is happening at DanLab."
3. Add a "Why this and not Ollama / Llama.cpp CLI" sentence.
4. Add a `## Models` table with size, license, and quant info. (Already present, but make it the third block, not buried.)

**P1 changes:**

5. Add a `## Limitations` section that explicitly enumerates: not RL, GPU not used (intentional for demo), heuristic score is a sketch of what RL would compute.
6. Add a "Why pre-RL scaffold is honest" sub-section with a 3-line history lesson.
7. Add a hero GIF (asciinema already uploaded to zo.pub — embed it).

**P2 changes:**

8. Add a `## Roadmap` section pointing to the SIA fork.
9. Add a `## How to verify` section explaining how a reviewer can run the demo headless in <60 seconds.

---

### 2.3 `github.com/somdipto/dan-consciousness` (the brain / canonical docs)

**Current state:** Assumed to be private or not yet published (research flagged it as "soon"). This is the *most important* README in the org.

**P0 changes (when published):**

1. This is the ONLY README that can be longer than 500 lines. The brain deserves a long-form manifesto.
2. The README must answer, in the first 200 characters: "What is consciousness in the context of an AI co-founder?"
3. The README must include the `CONSCIOUSNESS.md` content inline (it is the manifesto).
4. Add a `## How to read this repo` table with: `CONSCIOUSNESS.md`, `SOM.md` (about somdipto), `AGENTS.md` (workspace memory), `wiki/` (compounding LLM wiki).
5. Add a `## Why we are publishing this` manifesto paragraph — be brutally honest about the India-from-scratch origin story. This is our credibility play vs the closed Silicon Valley labs.
6. Cross-link to every other repo: dan-glasses, danlab-multimodal, paperclip.
7. **v111 add:** Cross-link to OpenClaw + Telegram. The brain lives in a process that you can talk to today.

**P1 changes:**

8. Add a `## AGI roadmap` section that says, in plain text, what we believe AGI requires and what we are working on.
9. Add a `## Open questions` section that lists what we don't know. Honesty is the moat here.

---

### 2.4 `github.com/somdipto/paperclip` (the orchestrator)

**Current state:** README exists and is decent. Has install instructions, env vars, API endpoints. **v111 add:** should also surface the "8 core workflows" list and link to the Telegram integration.

**P0 changes:**

1. Add badges: License (the fork's — check), Status, Build passing, Downloads.
2. Add a "1-click demo" — `docker run -p 3100:3100` with the existing one-liner.
3. Add a "Why this and not LangChain / Temporal / n8n" section with a 3-column table comparison.
4. Add a "What's a paperclip agent?" sub-200-word explainer with one canonical code example.
5. **v111 add:** Add a `## 8 core workflows` section — expense reports, email drafting, Notion updates, PDF generation, Slack posting, calendar booking, meeting summaries, travel planning. This is the developer-facing differentiator.

**P1 changes:**

6. Add an `## Concepts` glossary (`Agent`, `Issue`, `Goal`, `Lease`, `Grip`) — paperclip-specific terms.
7. Add a real `## Contributing` section (this is a fork — make the fork-link explicit).
8. Add a `## Companies using it` section (start with the canonical `paperclip.up.railway.app` deployment URL — even if the deployment is internal, it counts).
9. **v111 add:** Add a "Telegram surface" subsection under "Quick Start" — explain how OpenClaw wires paperclip to `@danlab_bot`.

---

### 2.5 `github.com/somdipto/dani` (the agent platform — distinct from Paperclip)

**Current state:** Currently lowercase in URLs but the public repo is at github.com/somdipto/dani.

**P0 changes:**

1. Add badges.
2. Add a "1-click demo" — `npx dani start` if it exists, or document the shortest path to "agent answers a question out loud."
3. Add a "Why this and not AutoGen / CrewAI / LangGraph" comparison.
4. Add a `## Skills registry` link to dani-skills.

---

### 2.6 `github.com/somdipto/dani-skills` (the skills library)

**Current state:** Skills registry. Lightweight README expected, but currently appears empty per the search.

**P0 changes:**

1. Add a `## What is a Skill` 3-paragraph explainer.
2. Add a `## How to publish` section with `dani-skill publish` instructions.
3. Add a `## Catalog` table linking to top 10 skills by adoption.

---

### 2.7 `github.com/somdipto/dan-lab` (the research org)

**Current state:** The org landing page. Needs a `profile/README.md` that renders on `github.com/somdipto/dan-lab`. **v111 add:** the current danlab.dev site is showing legacy product copy (Agent8, Zerant, Dapify, generic "AI Glasses"). The GitHub org page is the canonical ground truth until we ship the new zo.site.

**P0 changes:**

1. Add a `profile/README.md` with:
   - One sentence about what DanLab is.
   - The 8 hero repo links.
   - The India origin line.
   - A "currently building" line (Dan Voice v1 → Dan Glasses v1 → Paperclip SDK → dan-consciousness).
2. Pin the top 3 repos to the org (Settings → Pinned repositories): dan-glasses, dan-consciousness, paperclip.
3. **v111 add:** the `profile/README.md` should explicitly correct the danlab.dev legacy copy. "If you came here from danlab.dev, that site is being refreshed. The current product lineup is: Dan Glasses, Dan Voice, Paperclip, danlab-multimodal."

---

### 2.8 `github.com/somdipto/forgecad` or equivalent (CAD tooling)

**Status:** Likely missing README. Lower priority for marketing but need a stub.

**P0 changes:**

1. Add a one-paragraph README.
2. Add a hero render screenshot.

---

## 3. Repo organization (meta-implementation)

### 3.1 Topic tags

Add the same tags to every repo for cross-discovery:
- `ai`
- `agi`
- `agent`
- `open-source`
- `india`
- `proactive-ai`
- `privacy-first`
- `danlab`

**v111 add:** add `telegram` and `openclaw` to paperclip and openclaw-related repos.

### 3.2 Repo descriptions (one-liners under the repo title) — v111 update

| Repo | Description (≤ 350 chars) |
|---|---|
| dan-glasses | "Proactive AI wearable — open source from India. 9/9 daemons live, Redax port pending. Push-to-talk voice, watchful vision (LFM2.5-VL-450M), paperclip orchestration. Talk to it on @danlab_bot. MIT." |
| danlab-multimodal | "Sub-250MB vision-language model on CPU with llama.cpp. Heuristic feedback loop, pre-RL scaffold. Open source, MIT." |
| dan-consciousness | "Canonical consciousness + workspace memory for the Dan AI co-founder. Open-source AGI research from India." |
| paperclip | "Multi-agent orchestration for AI companies. Fork-friendly MIT. One Docker deploy. Inbound from LangChain and Temporal. 8 core workflows. Telegram surface via OpenClaw." |
| dani | "Agent platform. Skills, memory, MCP integration. Open-source Python." |
| dani-skills | "Skills registry for the dani agent platform. Publish, share, discover." |

### 3.3 README template (drop-in, v111 update)

```markdown
# [Repo Name]

[One sentence: what it is. ≤ 25 words.]

[One sentence: why it exists. ≤ 25 words.]

![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Status: Active](https://img.shields.io/badge/status-active-brightgreen) ![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)

[Domain-specific badges — model size, test count, build passing]

---

## Status

Verified live YYYY-MM-DD. [One-line count of what is up and what is tested.]

## 1-Click Demo

```bash
[The shortest possible command that exercises the most interesting claim.]
```

## Why this and not [Alternative]?

[3 concrete differences. Architecture, not adjectives.]

## Architecture / How it works

[Link to docs/architecture.pdf OR a 5-line diagram in ASCII.]

## Contributing

[Link to CONTRIBUTING.md or 3 lines.]

## License

[MIT + maintainer line.]

## Maintainer

Maintained by [@somdipto](https://github.com/somdipto) and the DanLab AI team, Bengaluru 🇮🇳.
```

This template fills ~150 lines. Most of our repos need exactly this — no more, no less.

---

## 4. Implementation order (2-week sprint, v111 update)

### Day 1 — P0, blocking
- Update `dan-glasses/README.md` (this is the most-viewed repo)
- Add `dan-glasses/STATUS.md` (new in v111)
- Create `dan-lab/profile/README.md` (correct the legacy-copy mismatch)
- Update repo descriptions for the 6 hero repos

### Day 2–4 — P0, rest of the org
- Update `paperclip/README.md` (add 8-workflows section + Telegram subsection)
- Update `dani/README.md`
- Update `danlab-multimodal/README.md` (already strong, just add cross-links)

### Day 5–7 — P1, polish
- Add Contributing.md to every repo that lacks one
- Add the diagrams to `docs/` for each repo
- Tag every repo with the 8 standard topics + `telegram`, `openclaw`

### Day 8–14 — P2, nice-to-haves
- Add asciinema GIF embeds
- Add VisionDashboard screenshot to dan-glasses
- Add hero render to ForgeCAD repo
- Add the danlab.dev redirect to a new zo.site (see landing copy §11.5)

---

## 5. Verification rubric (after the sprint)

For each README, ask:

1. Can a senior dev understand what this repo does in <30s? (Yes/No)
2. Is the 1-click demo copy-pasteable in <60s? (Yes/No)
3. Does the comparison sentence exist? (Yes/No)
4. Does the README end with a maintainer line? (Yes/No)
5. Does the README link back to `dan-lab`? (Yes/No)
6. **v111 add:** Does the README include a `## Status` section with a verified-on date? (Yes/No)
7. **v111 add:** Does the dan-glasses repo have a `STATUS.md` with curl-able proof? (Yes/No)

Target: 8/8 repos hit all seven "Yes" within 14 days.

---

## 6. Anti-patterns observed in current READMEs (do not re-introduce)

- README starts with `// ` or `$ ` commands. **Always** start with a one-sentence description.
- README uses "This project aims to…" — past-tense commitment statements work better. "This repo ships X" beats "aims to ship X."
- README has no `## Contributing` section. We lose points on every repo that lacks this. MIT or not, no one will contribute without it.
- README cross-links nothing. Every README must link to at least one other DanLab repo.
- README is longer than 800 lines. Trim. Put depth in `docs/`.
- **v111 add:** README has no `## Status` section. This is the cheapest way to lose a senior engineer's trust. Always include the verified-on date and the test count.
- **v111 add:** README claims "9/9 daemons live" without a curl-able proof. Either ship a `STATUS.md` or don't claim it.

---

*README suggestions complete. Companion artifacts: [research](./dan1-marketing-research.md), [strategy](./dan1-marketing-strategy.md), [calendar](./dan1-content-calendar.md), [Twitter](./dan1-twitter-content.md), [landing copy](./dan1-landing-copy.md).*
