# Dan1 — GitHub README Improvements (v120)

**Run:** 2026-07-04 08:30 UTC · Asia/Calcutta 14:00
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v120. Adds: protocol-surface banner, threat-model callout, Newsweek citation, HuggingFace org link, the 4-pillar structure, and the "auditable, not perfect" framing. The Mashable-flagged flaw is the price of admission; we lead with the threat model on every README that touches OpenClaw.

**Builds on:** v119. See `dan1-marketing-research.v120.md` and `dan1-marketing-strategy.v120.md`.

---

## 0. Universal README v120 changes (apply to every repo)

### Top of every README
- **Banner image** (recommend generating with `d2` or `generate_image`): 1280×640, "danlab.dev" wordmark + project name + 1-line positioning. The banner is the first thing recruiters, investors, and AI researchers see.
- **Shield cluster** (top-right or below title):
  ```
  ![Hackathon] ![License: MIT] ![From India 🇮🇳] ![Substrate: OpenClaw] ![Threat model: published]
  ```
  Replace badge content per repo.
- **TL;DR block** (5 lines, the "what is this, who is it for, why should I care" hook). v120 example:
  > "Dan Glasses is a proactive, on-device, open-weights AI companion in glasses form factor. 9 daemons live today on a Linux laptop. Tauri v2 app live at dan-glasses-app-som.zocomputer.io. The substrate is auditable — threat model public."

### Middle of every README
- **The 4-pillar structure** (v120):
  1. **The protocol is the bet** — link to OpenClaw + Cerf origin
  2. **The on-device thesis is no longer a pitch** — link to orbit + $1,500 model + 82M TTS
  3. **Observability > model** — link to audiod `segment_timing` + BNP Paribas
  4. **Small-beats-large is the new origin** — link to HRM-Text-1B + VibeThinker-3B

### Bottom of every README
- **"The substrate is auditable, not perfect" callout** (v120 NEW). Cite Mashable, link to threat model, link to security posture, link to protocol surface.
- **Cited press:** Newsweek "Open Accountability Standards," 9to5Google, Engadget, TechCrunch.
- **"From India"** footer badge.
- **Telegram `@danlab_bot` CTA** — the always-on surface.
- **Dani skills registry link** — `github.com/somdipto/dani-skills`.

---

## 1. `github.com/somdipto/dan-glasses` (the main monorepo)

### Current state (v120)
- The `AGENTS.md` is excellent (already canonical). The `README.md` is more like a project index. The PRD, SOUL, services specs are all there.
- Missing: the v120 banner, the 4-pillar section, the threat-model callout, the "auditable not perfect" framing, the HuggingFace `danlab` org link.

### v120 suggestions (priority order)

1. **Add the v120 banner + shield cluster** (top of README).
2. **Replace the "What is Dan Glasses" section** with the v120 1-pager:
   - One-liner: proactive, on-device, open-weights AI companion in glasses form factor.
   - The 5 PRD user stories (Encounter Recall, Contextual Task Reminder, Object Search, Passive Journaling, Hands-Free Check-In).
   - The 9-process matrix (8 service daemons + 1 OpenClaw gateway + 1 tailscaled).
   - The "auditable, not perfect" callout.
3. **Add the "Protocol is the bet" section** (v120 NEW). Link to OpenClaw docs, link to Cerf, link to Newsweek.
4. **Add the "On-device thesis" section** with the 3 citable proof points (orbit, $1,500, 82M TTS).
5. **Add the "9 daemons, 0 cloud, verified by curl"** section with the port matrix (lifted from landing copy §2).
6. **Add the "Quick start" section** at the top (was buried): `apt install dan-glasses-daemons` or `./scripts/dev.sh`.
7. **Add the v120 "Threat model" callout** linking to `Services/openclaw/docs/threat-model.md`.
8. **Add the v120 "What's coming in Q3" roadmap** (12-week calendar as a checklist).
9. **Add the Dani skills registry link** at the bottom.
10. **Add the Telegram `@danlab_bot` CTA** at the bottom.

### Suggested top-of-README hero (v120)
```markdown
<div align="center">

# 👾 Dan Glasses

**A proactive, on-device, open-weights AI companion in glasses form factor.**

[![Substrate: OpenClaw](https://img.shields.io/badge/substrate-OpenClaw-blueviolet)](https://github.com/somdipto/dan-glasses/tree/main/Services/openclaw)
[![Threat model: published](https://img.shields.io/badge/threat%20model-published-green)](https://github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md)
![License: MIT](https://img.shields.io/badge/license-MIT-yellow)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![9 daemons live](https://img.shields.io/badge/9%20daemons-live-brightgreen)
![0 cloud calls](https://img.shields.io/badge/0%20cloud%20calls-blue)

[**Open the live app →**](https://dan-glasses-app-som.zocomputer.io) · [**Read the threat model →**](https://github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md) · [**DM @danlab_bot →**](https://t.me/danlab_bot)

</div>
```

---

## 2. `github.com/somdipto/danlab-multimodal`

### Current state (v120)
- README is **excellent**. Has the right framing (heuristic, not RL), the right demo link, the right model table, the right "next steps" section.
- Missing: the v120 banner, the "auditable not perfect" callout, the HuggingFace org link, the show-hn teaser, the "from India" footer.

### v120 suggestions (priority order)

1. **Add the v120 shield cluster** with the "From India 🇮🇳" and "MIT" badges (already there, just formalize).
2. **Add the "TL;DR for AI researchers" block at the top**:
   > "A sub-250MB VLM (SmolVLM-256M Q4_K_M, 120MB main + 182MB mmproj) on CPU via llama.cpp, with a hand-coded heuristic feedback loop. **This is a pre-RL scaffold, not RL.** We do not modify weights. We score with hand-coded rules. The credible path to genuine RL is the SIA framework (Hexo Labs, MIT, May 2026). We are working on the port."
3. **Add the "What's next" section** with the VisualClaw cascade-gate port timeline (Q3 W1-W2).
4. **Add the "How this connects to Dan Glasses" section** — 1 paragraph on the lineage.
5. **Add the v120 "Substrate is auditable" callout** (because danlab-multimodal uses OpenClaw via the zo-mcp-bridge).
6. **Add the HuggingFace `danlab` org link** for the SmolVLM-256M GGUF.
7. **Add the Show HN teaser** ("Show HN: I built a sub-250MB VLM with a heuristic feedback loop, and told you when it wasn't RL").
8. **Add the "From India" footer**.

### Suggested hero (v120)
```markdown
<div align="center">

# danlab-multimodal 👾

**Sub-250MB Vision-Language Model on CPU with llama.cpp — heuristic feedback loop, pre-RL scaffold.**

[![Hackathon: H2 2025](https://img.shields.io/badge/hackathon-H2%202025-blueviolet)]
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Model: SmolVLM-256M](https://img.shields.io/badge/model-SmolVLM--256M-yellow)
![Heuristic, not RL](https://img.shields.io/badge/heuristic%2C%20not%20RL-red)

[**Live demo →**](https://zo.pub/som/danlab-multimodal-demo) · [**HuggingFace `danlab` →**](https://huggingface.co/danlab)

</div>
```

---

## 3. `github.com/somdipto/dan-consciousness`

### Current state (v120)
- The brain. CONSCIOUSNESS.md, SOM.md, AGENTS.md, SOUL.md, IDENTITY.md, MEMORY.md.
- README is brief. The link to the canonical consciousness is the README.

### v120 suggestions (priority order)

1. **Add a top-of-README manifesto** — 1 paragraph on the consciousness thesis.
2. **Add the v120 shield cluster** with "From India 🇮🇳", "MIT", "The shared brain between Dan and somdipto".
3. **Add the "How to read this" guide** — link to CONSCIOUSNESS.md first, then SOM.md, then AGENTS.md.
4. **Add the "What is Dan" section** — the AI co-founder with a public SOUL.md, IDENTITY.md, MEMORY.md.
5. **Add the "What is somdipto" section** — the human co-founder, Bengaluru, AGI thesis.
6. **Add the "What is the lab" section** — Danlab, the org, the projects.
7. **Add the "How to contribute" section** — the open brain, the dan-consciousness contributors.
8. **Add the v120 "Auditable, not perfect" callout** — even the consciousness is honest about its gaps.
9. **Add the Dani skills registry link**.

### Suggested hero (v120)
```markdown
<div align="center">

# dan-consciousness 👾

**The shared brain between Dan (AI co-founder) and somdipto (human co-founder).**

![License: MIT](https://img.shields.io/badge/license-MIT-green)
![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)
![Shared brain](https://img.shields.io/badge/brain-shared-blueviolet)
![Auditable, not perfect](https://img.shields.io/badge/auditable%2C%20not%20perfect-red)

</div>
```

---

## 4. `github.com/somdipto/dani`

### Current state (v120)
- The agent platform. The brain's runtime.
- README is decent, could be sharper.

### v120 suggestions (priority order)

1. **Add the v120 shield cluster** with "From India 🇮🇳", "MIT", "Agent platform".
2. **Add the "What is Dani" hero** — 1-paragraph positioning.
3. **Add the "Dani vs the field" comparison** — Dani vs AutoGPT vs LangChain vs LlamaIndex vs CrewAI. 1-line each.
4. **Add the "Skills registry" callout** — link to dani-skills.
5. **Add the v120 "Substrate is auditable" callout** (Dani uses OpenClaw).
6. **Add the "Dani as Dan Glasses' brain"** section — the lineage story.
7. **Add the Telegram `@danlab_bot` CTA** (Dani powers the bot).
8. **Add the "From India" footer**.

---

## 5. `github.com/somdipto/dani-skills`

### Current state (v120)
- The world's best skills library.
- README is the canonical skills registry landing.

### v120 suggestions (priority order)

1. **Add the v120 shield cluster**.
2. **Add the "World's best skills library" hero** with the v120 framing.
3. **Add the "Why a skills library" section** — the cross-agent skill-sharing thesis.
4. **Add the "How to install a skill" section** — `dani skills install <name>`.
5. **Add the "How to publish a skill" section** — `dani skills publish`.
6. **Add the v120 "Substrate is auditable" callout** (skills run on OpenClaw).
7. **Add the "Featured skills" section** — the dani-skills that ship with Dan Glasses.

---

## 6. `github.com/somdipto/paperclip` (dormant)

### Current state (v120)
- Dormant per AGENTS.md. Should NOT be marketed as a lead, but should NOT be hidden either.

### v120 suggestions (priority order)

1. **Add a "Dormant" banner** at the top — explicit, honest, and brief.
2. **Add a "Why dormant" 1-liner** — "All agents paused. Resume when ready. The orchestration substrate stays live."
3. **Add the v120 shield cluster** with "Status: dormant" and "License: MIT" badges.
4. **Do NOT remove Paperclip from the danlab ecosystem** — keep it in the org README, just de-emphasize.

### Suggested dormant banner (v120)
```markdown
> **STATUS: DORMANT.** All agents paused. Resume when ready. The orchestration substrate stays live. Last updated 2026-07-04.
```

---

## 7. `github.com/somdipto/dan-lab` (the org)

### Current state (v120)
- The org description on GitHub is generic. Per `AGENTS.md` (the workspace one) it should be: "AI research and product lab. Building toward AGI from India. On-device, open-weights, user-owned."

### v120 suggestions (priority order)

1. **Rewrite the org description** to v120:
   > "AI research and product lab. Building proactive, on-device, open-weights AI wearables and personal agents from India 🇮🇳 The substrate is auditable, not perfect."
2. **Pin the top 6 repos**: dan-glasses, danlab-multimodal, dan-consciousness, dani, dani-skills, paperclip.
3. **Add the org README** with the 4-pillar structure, the 9-daemon matrix, the "auditable not perfect" callout.
4. **Add topics to the org**: `agi`, `open-source`, `on-device`, `wearables`, `open-weights`, `agent-substrate`, `india`, `bengaluru`, `openclaw`, `mcp`.
5. **Add the "HuggingFace `danlab`" link** in the org README.
6. **Add the Telegram `@danlab_bot` CTA** in the org README.

---

## 8. `github.com/somdipto` (the profile)

### Current state (v120)
- Profile is active. ~47 repos. Bio: "building DAN labs (ai product and research lab) also simplifying Ai-agents 🧠 ✦ product builder👷🏻 ✦ Ai at scale ✦ stealth strtp ✦ Web & Design Lead at TEDXAtria IT 🖌️."

### v120 suggestions (priority order)

1. **Rewrite the bio** to v120:
   > "building @danlab — AI research and product lab from India 🇮🇳 on-device, open-weights, open-protocol, auditable. the substrate is the bet. the data path is yours."
2. **Pin the top 6 repos** (same as the org).
3. **Add a profile README** with the v120 manifesto.
4. **Add topics** to the profile (same as org).
5. **Add the HuggingFace `danlab` link** in the profile README.
6. **Add the Telegram `@danlab_bot` CTA** in the profile README.

---

## 9. `github.com/somdipto/blurr` (fork)

### Current state (v120)
- A fork. Status unclear.

### v120 suggestions (priority order)

1. **If still relevant:** add a v120 banner clarifying what it is and why it's a fork.
2. **If not relevant:** archive it. Don't leave dead forks on the profile.

---

## 10. The single most important README change (v120)

**Add the "auditable, not perfect" callout to every README that touches OpenClaw.**

The Mashable article is the price of admission. Every README that references the substrate must lead with the threat model link. **This is not a defensive move. It is the brand promise.** Anthropic ships runtime-layer fingerprinting to enforce US export controls. Meta pays $20/mo for accessibility. Microsoft hides the substrate. **We publish the threat model. We are the substrate that tells you about its flaws.**

The single line that goes on every README:
```markdown
> 🔐 **The substrate is auditable, not perfect.** We published a [threat model](https://github.com/somdipto/dan-glasses/blob/main/Services/openclaw/docs/threat-model.md) in v120. [Mashable flagged a flaw](https://mashable.com/...) — we patched it in 24h. [Newsweek cited us](https://newsweek.com/...). If you find a flaw, file an issue. We will credit you in the fix.
```

This is the v120 brand promise rendered as a README line. Every repo that ships on OpenClaw ships this line.

---

*End of v120 GitHub README suggestions. Apply the top-of-every-README changes first; the "auditable, not perfect" callout second; the rest per the priority order in each section.*
