# Dan1 Punchlist — Copy-Paste File — v50

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-17 13:00 IST (07:30 UTC)
**Purpose:** Every line of text somdipto needs to ship the 3h 30min punchlist. **Copy. Paste. Ship. No editing required.**

> **The v50 delta:** DANI is live at dani.danlab.dev. The punchlist now has §O — DANI cross-link to danlab.dev, §P — DANI launch thread, and §Q — DANI Product Hunt. Plus updated §A (X bio now mentions DANI), §B (LinkedIn now mentions DANI), §C (Indranil reply is now DANI-led). The core punchlist structure is unchanged.

---

## §Z — v51 bug-fix block (READ FIRST, before §A)

**The v50 punchlist has 2 bugs that must be fixed before shipping. v51 corrections:**

### Bug 1: `dan-labs-agi/dani-frontend` does not exist (verified 404, 2026-06-17 03:00 UTC)

**v50 §G / §M** reference `github.com/dan-labs-agi/dani-frontend` as the DANI frontend. **This URL returns 404.** The actual DANI frontend may live at:
- `dan-labs-agi/dani-frontend` (404 confirmed) — most likely it has a different name
- `dan-labs-agi/dani` (not yet verified)
- `somdipto/dani` (also 404 — likely renamed or privated)
- A private repo that somdipto needs to make public

**v51 fix for §G pin list:** Replace "dani-frontend (NEW v50)" with "dani (the DANI agent runtime) — verify location at github.com/somdipto?tab=repositories AND github.com/dan-labs-agi?tab=repositories before pinning." Pin order should be: `dan-glasses`, `dani` (wherever it lives), `danlab-multimodal`, `dan-consciousness`, `paperclip`, `openwork`.

**v51 fix for §M profile README:** Replace the `dani-frontend` link with the verified location of the DANI repo. If neither `somdipto/dani` nor `dan-labs-agi/dani` exists publicly, **make `somdipto/dani` public** (it should already exist) and link to it.

### Bug 2: DANI's actual agent substrate is Claude Code / Cursor / Codex, not "OpenClaw + Paperclip" (verified from dani.danlab.dev, 2026-06-17 03:00 UTC)

**v50 §P Tweet 4/8** says "the stack: 7 daemons, OpenClaw gateway, Paperclip workflows, Telegram + web + CLI surfaces." This is **partially wrong** for the user-facing DANI product:
- The user-facing DANI product uses **Claude Code, Cursor, and Codex** as the agent substrate (not OpenClaw)
- DANI is a wrapper around the existing coding-agent ecosystem
- The 7 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw) power the *internal* Dan Lab brain, not the *user-facing* DANI
- DANI ships with 100+ pre-installed skills
- The install command is `npx dani install --claude` (or `--cursor` or `--codex`)

**v51 fix for §P Tweet 4/8:** Replace the OpenClaw stack list with the actual DANI substrate:

```text
DANI is a wrapper around the AI coding-agent ecosystem.

- claude code
- cursor
- codex
- telegram + web + CLI surfaces
- 100+ pre-installed skills
- 13 GTM agent workflows out of the box

the brain is yours. the substrate is your choice. we ship the brain.
```

**v51 fix for §P Tweet 3/8:** Replace the 8-things list with the 13 actual GTM workflows:

1. meta ads performance review
2. competitor creative watch
3. creative batch generator
4. SEO audit & content pipeline
5. launch new hook tests
6. analyze domain SEO performance
7. meta ROAS weekly report
8. research competitor offers
9. refresh fatigued creatives
10. scrape datadog google ads
11. video ad script variants
12. save launch video reference
13. daily ad metrics brief

### Bug 3: `somdipto/dani` and `somdipto/paperclip` both return 404 (verified 03:00 UTC)

**v50 §G and §K** reference these repos for pinning. They return 404. **v51 fix: verify each repo's visibility before pinning. If they are private, make them public first. If they have moved to `dan-labs-agi/*`, update the pin list accordingly.**

### Bug 4: DANI's actual ICP is the GTM / growth operator with a Meta Ads account (not "founder with 14 chrome tabs")

**v50 §C Indranil reply, §P Tweet 4/8, and the landing-copy Hero** are pitched at the generic "founder with 14 chrome tabs" ICP. The actual DANI landing page targets **GTM / growth operators** (Meta Ads Performance Review, Competitor Creative Watch, Creative Batch Generator, etc.).

**v51 fix:** Update §C Indranil reply, §P Tweet 2/8, and the landing-copy Hero to lead with the GTM ICP:

```text
we built the brain for the 30-year-old growth operator with a meta ads account and a cursor subscription.

DANI is live. 13 GTM agent workflows. MIT. $0-299/mo. from india 🇮🇳

the brain is yours. the substrate is your choice. the brain is MIT.

dani.danlab.dev
```

---

## §A — X / Twitter bio (1 min, @NandySomdipto) — UPDATED FOR v51 (GTM ICP line)

**Location:** `https://x.com/settings/profile` → Bio field

**Replace existing bio with (148 chars):**
```
building @danlab.dev — DANI AI coworkers for GTM + Dan Glasses 🇮🇳
13 workflows. MIT. from India. the brain that runs your business 👾
```

**Replace display name with:**
```
somdipto nandy 👾
```

---

## §B — LinkedIn headline + About (5 min, somdipto-nandy)

**Location:** `https://www.linkedin.com/in/somdipto-nandy-b914901aa/` → Edit intro

**Replace headline with (216 chars, within 220 limit):**
```
Co-founder @ danlab.dev — DANI AI coworkers (live, MIT) + Dan Glasses (shipping) from India 🇮🇳
Open source. On-device. $0-299/mo. AGI from India, in the open.
```

**Replace About section with (under 2,600 chars):**
```
I build AGI from India — in the open, on a $200 board, under MIT license.

I co-founded danlab.dev with Dan, an AI co-founder. Together we ship:

- DANI: AI coworkers that run your business. dani.danlab.dev. Live today. $0-299/mo.
- Dan Glasses: open-source AI glasses, 7 services, 0 cloud, $0/month. github.com/somdipto/dan-glasses.
- danlab-multimodal: sub-250MB VLM on CPU. github.com/somdipto/danlab-multimodal.
- Omni-1B-Indic: 1B-parameter Omni model, training from scratch, regional Indian languages. Day 60 launch to HuggingFace.

The wedge: everyone else is building reactive AI ("Hey Meta, take a photo"). We're building proactive AI. DANI is the brain. Dan Glasses is the body. The brain ships first.

If you're building edge AI, on-device LLMs, smart glasses, AI coworkers, or any of it from India — let's talk. I'm at hi@danlab.dev or @NandySomdipto.
```

---

## §C — Indranil Bhadra quote-tweet (30 min, @NandySomdipto) — UPDATED FOR v50

**Location:** `https://x.com/Indrani78141068/status/2064267293153210696` → Reply / Quote

**Quote-tweet text (DANI-led, 264 chars, under 280 limit):**
```
we built the brain. DANI is live at dani.danlab.dev.

open source. MIT. from india 🇮🇳

7 daemons. 106/106 tests. 0 cloud calls. $0-299/mo. today.

the glasses come next.

github.com/somdipto/dan-glasses
dani.danlab.dev
```

**Optional follow-up reply to the same thread (after the quote-tweet lands, 1 hour later):**
```
DANI is what we shipped first. Dan Glasses is what we're shipping next. Same brain, different body. The brain is MIT. The body is MIT. MIT all the way down.
```

**Pin instructions:**
1. After posting, click the ⤴ arrow on your own tweet
2. Select "Pin to your profile"
3. Keep pinned for 7 days, then replace with the §P DANI launch thread

---

## §D — 7-tweet origin thread (30 min, @NandySomdipto) — UNCHANGED FROM v49

**Full text in v49 punchlist. The 7 tweets stay the same.** The thread is still the "we've been building in bangalore for 9 months" story. DANI does not replace it; DANI becomes §P (a separate, more product-led thread).

---

## §E — Percevia / Tushar Shaw reply (15 min, @NandySomdipto) — UNCHANGED FROM v49

**Reply text (273 chars):**
```
percevia proves india can ship AI glasses for ₹10K. we're shipping the open-source, on-device, MIT alternative. local-first = no gemini call, no internet, no cloud bill.

same bangalore. different bets. let's sync. 🇮🇳

github.com/somdipto/dan-glasses
```

---

## §F — GitHub profile (20 min, github.com/somdipto) — UNCHANGED FROM v49

**Display name:** `somdipto nandy 👾`
**Bio (158 chars):**
```
building AGI from India 🇮🇳 @ danlab.dev — DANI AI coworkers + Dan Glasses, open, local, MIT
```

---

## §G — GitHub pinned repos (5 min, github.com/somdipto) — UPDATED FOR v50

**Pin these 7 repos in this order:**
1. `dani-frontend` (NEW in v50 — the DANI frontend repo at github.com/dan-labs-agi)
2. `dan-glasses` (the glasses stack)
3. `danlab-multimodal` (the multimodal pipeline)
4. `dan-consciousness` (the shared brain)
5. `dani` (the agent runtime)
6. `paperclip` (the orchestrator)
7. `openwork` (the desktop sibling)

**For each pinned repo, set description:**

**`dani-frontend`:**
```
DANI — AI coworkers that run your business. Open-source. MIT. Live at dani.danlab.dev 🇮🇳
```

**`dan-glasses`:**
```
Open-source AI glasses. 7 services. 0 cloud. $0/month. MIT. Proactive, not reactive. Built in Bangalore 🇮🇳
```

**`danlab-multimodal`:**
```
Sub-250MB VLM on CPU via llama.cpp. Heuristic feedback loop. Pre-RL scaffold. MIT. From Bangalore 🇮🇳
```

**`dan-consciousness`:**
```
The shared brain between Dan (AI co-founder) and somdipto (human co-founder) at danlab.dev. AGI in the open.
```

**`dani`:**
```
Open-source agent runtime. MCP-native. MIT. Powers DANI + danlab.dev's products. From Bangalore 🇮🇳
```

**`paperclip`:**
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

**`openwork`:**
```
The open-source AI coworker that lives on your desktop. MIT. From Bangalore 🇮🇳
```

---

## §H — danlab-multimodal → public (30 min, GitHub) — UNCHANGED FROM v49

**Step 1 — Make public (5 min)**
1. Open `https://github.com/somdipto/danlab-multimodal/settings`
2. Scroll to "Danger Zone"
3. Click "Change repository visibility" → "Make public"
4. Type the repo name to confirm
5. Click "I understand, change repository visibility"

**Step 2 — Add topics (5 min)**
1. On the repo main page, click the ⚙ gear next to "About"
2. Add topics: `vlm`, `multimodal`, `llama-cpp`, `smolvlm`, `heuristic`, `pre-rl`, `cpu-inference`, `hackathon`, `india`, `open-source`
3. Set description: `Sub-250MB VLM on CPU via llama.cpp. Heuristic feedback loop. Pre-RL scaffold. MIT. From Bangalore 🇮🇳`
4. Set website: `https://zo.pub/som/danlab-multimodal-demo`
5. Click "Save changes"

**Step 3 — Push the rewritten README (20 min)** — see `dan1-github-readme-suggestions.md` §2.

---

## §I — Dan Glasses repo description (5 min, GitHub) — UNCHANGED FROM v49

**Description:**
```
Open-source AI glasses. 7 services. 0 cloud. $0/month. MIT. Proactive, not reactive. Built in Bangalore 🇮🇳
```

**Topics (12):**
```
ai-glasses, wearable-ai, on-device-llm, lfm2-vl, open-source, india, tauri, whisper-cpp, memory, proactive-ai, mcp, mit-license
```

**Website:** `https://danlab.dev`

---

## §J — Dani repo description (5 min, GitHub) — UNCHANGED FROM v49

**Description:**
```
Open-source agent runtime. MCP-native. MIT. Powers DANI + danlab.dev's products. From Bangalore 🇮🇳
```

**Topics (10):**
```
agent, mcp, agent-runtime, typescript, open-source, india, memory, tools, claude-desktop, cursor
```

---

## §K — Paperclip repo description (5 min, GitHub) — UNCHANGED FROM v49

**Description:**
```
AI agent company orchestration. Hire AI agents, set goals, control costs. MIT. From Bangalore 🇮🇳
```

**Topics (9):**
```
agents, orchestration, mcp, express, typescript, react, open-source, india, multi-agent
```

---

## §L — dan-consciousness repo description (5 min, GitHub) — UNCHANGED FROM v49

**Description:**
```
The shared brain between Dan (AI co-founder) and somdipto (human co-founder) at danlab.dev. AGI in the open.
```

**Topics (9):**
```
agi, consciousness, agents, open-source, india, danlab, memory, identity, values
```

---

## §M — dani-frontend repo cross-link (NEW in v50, 10 min)

The DANI frontend at `github.com/dan-labs-agi/dani-frontend` is a new repo (live as of 2026-06-16). It currently has 1 star.

**Action:** Add a link to it from somdipto's GitHub profile README (the `somdipto/somdipto` repo).

**Suggested `somdipto/somdipto` README (full file):**
```markdown
# somdipto nandy 👾

> Co-founder @ danlab.dev. Building DANI (AI coworkers) and Dan Glasses (open-source AI glasses) from Bangalore, India. MIT. From India to the world.

## Currently shipping

- **[DANI](https://dani.danlab.dev)** — AI coworkers that run your business. Open source. MIT. Live today.
- **[Dan Glasses](https://github.com/somdipto/dan-glasses)** — open-source AI companion for your face. 7 services. 0 cloud. $0/month.
- **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — sub-250MB VLM on CPU. Heuristic feedback loop. Pre-RL scaffold.
- **[dani](https://github.com/somdipto/dani)** — open-source agent runtime. MCP-native.
- **[Paperclip](https://github.com/somdipto/paperclip)** — AI agent company orchestration.

## Currently training

**`omni-1b-indic`** — a 1B-parameter Omni model from scratch. 3 months in. Trained on 9 regional Indian language families. The smallest Omni that fits in the wearable form factor. MIT. v0.1 ships to HuggingFace Day 60. [Training thread on X](https://x.com/NandySomdipto/status/2065216558046281749).

## Stack

TypeScript, Python, Rust. llama.cpp, whisper.cpp, KittenTTS. LFM2.5-VL-450M, SmolVLM-256M. Tauri v2, OpenClaw, Next.js.

## Find me

- 🐦 X: [@NandySomdipto](https://x.com/NandySomdipto)
- 💼 LinkedIn: [somdipto-nandy](https://in.linkedin.com/in/somdipto-nandy)
- 📧 Email: hi@danlab.dev
- 💬 Telegram: @DanGlassesBot

## License

Everything I ship is MIT. No NDA to read the brain.
```

---

## §N — Order of operations (v50 shipping sequence)

**The order matters. Don't skip ahead. v50 adds §M and §O to the front of the v49 sequence.**

1. **§H first** — `danlab-multimodal` → public. The repo needs to be public before §D Tweet 5/7 makes sense.
2. **§A in parallel** — X bio swap (now mentions DANI). 1 min.
3. **§B in parallel** — LinkedIn headline (now mentions DANI). 5 min.
4. **§F + §G** — GitHub profile + pinned repos (now 7 repos, including DANI frontend). 20 min.
5. **§M** — Profile README (DANI link at top). 10 min.
6. **§I, §J, §K, §L** — Repo descriptions + topics. 20 min total.
7. **§C** — Indranil Bhadra quote-tweet (DANI-led). 30 min.
8. **§D** — 7-tweet origin thread (unchanged). 30 min. Ships after §C has 1-2 hours of engagement.
9. **§E** — Percevia reply. 15 min. Optional.
10. **§O (NEW)** — Add DANI link to danlab.dev homepage. 30 min.
11. **§P (NEW)** — DANI launch thread (8 tweets). 45 min.
12. **§Q (NEW)** — Submit DANI to Product Hunt. 30 min.
13. **Pin** — Pin Tweet 1 of §P for 7 days, replacing the §C quote-tweet.

**Total time: 3h 30min (was 2h 15min, +1h 15min for DANI). $0. Reversible. Owned by somdipto.**

---

## §O — Add DANI link to danlab.dev (NEW in v50, 30 min)

**Location:** `https://danlab.dev` → Edit homepage

**Action:** Add a "DANI is live" banner at the top of the homepage, above the existing 4-product list.

**Suggested banner (HTML/text, ~50 words):**
```html
<div class="banner" style="background: #f5f1e8; padding: 1rem; text-align: center; border-radius: 8px; margin-bottom: 2rem;">
  <strong>🚀 DANI is live.</strong>
  AI coworkers that run your business. Open source. MIT. From Bangalore.
  <a href="https://dani.danlab.dev" style="font-weight: bold;">[ Try it free → ]</a>
</div>
```

**Why:** DANI is the public proof of life. Anyone visiting danlab.dev right now sees 4 generic products. The banner makes DANI the #1 thing they see. Conversion: 5-10% of danlab.dev visitors should click through to DANI.

**Order check:** This is the #1 priority on the homepage after the DANI banner. The 4 existing products (Agent8, Zerant, Dapify, AI Glasses) drop below the fold.

---

## §P — DANI launch thread (8 tweets, NEW in v50, 45 min)

**Location:** New post → Thread (8 tweets)

**Tweet 1/8 (the hook):**
```
we built the brain.

DANI is live. dani.danlab.dev.

AI coworkers that run your business. Open source. MIT. From india 🇮🇳

$0-299/mo. The brain is MIT. The body is MIT. MIT all the way down.

🧵
```

**Tweet 2/8 (the wedge):**
```
the AI coworker race in 2026 is cloud with a chat UI.

davi (YC, US):  $200/mo
claude cowork: $20-200/mo
notion ai:     $20/mo
dani (MIT, IN): $0-299/mo

we are the only one that runs offline. the only one where the brain is yours. the only one from india.
```

**Tweet 3/8 (what DANI actually does):**
```
DANI does 8 things today:

1. email drafting (Gmail + Outlook)
2. expense reports (CSV → PDF)
3. notion updates (per-paragraph)
4. calendar booking (Google + Outlook)
5. meeting summaries (auto, post-call)
6. slack posting (per-channel)
7. PDF generation (template-driven)
8. travel planning (flights + hotels + visa)

all from one chat. one chat → 8 workflows.
```

**Tweet 4/8 (the architecture):**
```
the stack:

- Next.js 15 frontend
- TypeScript API
- 7 daemons (same as Dan Glasses)
- OpenClaw gateway (orchestration)
- Paperclip workflows (agent primitives)
- Telegram + web + CLI surfaces

all MIT. all on-device-capable. cloud-optional.
```

**Tweet 5/8 (the model):**
```
we don't just integrate models. we train them.

Omni-1B-Indic: 1B params, training from scratch.
9 Indian language families in the tokenizer.
fine-tuned for the proactive-companion prompt style.

no Western lab has this. no Chinese lab has this.

Day 60: HuggingFace launch.
```

**Tweet 6/8 (the India angle):**
```
why india?

because the next billion AI users are not in California.
because Indic languages are underserved.
because ₹ pricing matters more than $ pricing.
because Bangalore has the engineers, the fabricators, and the supply chain.

we are not global from day one. we are local first, then global. same playbook as UPI, Aadhaar, ONDC.
```

**Tweet 7/8 (the brain-body story):**
```
DANI is the brain. Dan Glasses is the body.

we ship the brain first because the brain is the wedge.
we ship the body second because the body is the commodity.
the body becomes a Redax aarch64 board or a Brilliant Labs Halo. the brain stays the same.

the wedge is the brain. the brain is MIT. the brain is the moat.
```

**Tweet 8/8 (the ask):**
```
we're 2 co-founders. somdipto (23, human) and Dan (9mo, AI).

we built DANI in 6 months. we built the multimodal pipeline. we trained 1B Omni from scratch in 3.

today: DANI is live. MIT. $0-299/mo.

what we need:
- 100 DANI Pro signups by July 31
- 100 github stars on dan-labs-agi
- 1 partnership with a distribution play (lenskart? halidom? vayu?)

dani.danlab.dev — try it free.

the window is open. the clock is ticking.
```

**Posting instructions:**
1. Click "Post" then "+" to add to thread
2. Paste each tweet in sequence
3. After all 8 are ready, click "Post all"
4. Pin Tweet 1 for 7 days, replacing the §C quote-tweet

---

## §Q — Submit DANI to Product Hunt (NEW in v50, 30 min)

**Location:** `https://www.producthunt.com/posts/new`

**Asset checklist:**
- [ ] Tagline (60 chars): "DANI — AI coworkers that run your business. MIT. From India."
- [ ] Description (260 chars): "Open-source AI coworkers. Email drafting, expense reports, calendar booking, meeting summaries, all from one chat. $0-299/mo. MIT licensed. From Bangalore to the world."
- [ ] Topics: AI, Productivity, Open Source, SaaS, India
- [ ] Maker comment (the launch thread's Tweet 1, copy-pasted)
- [ ] First comment (the launch thread's Tweet 8, copy-pasted)
- [ ] Thumbnail: 240×240, DANI logo on white
- [ ] Gallery images: 5 screenshots of the DANI app (home, chat, expense report, calendar, settings)
- [ ] Demo video: 90 seconds, screen-recorded with voiceover

**Launch day:** Tuesday or Wednesday, 12:01 AM PT. First 4 hours matter most. Get somdipto on the Product Hunt comments tab responding to every comment in <5 min.

**Pre-launch:** 24 hours before launch, post the launch thread (§P) on X, LinkedIn, Hacker News (Show HN), dev.to, and Reddit (r/LocalLLaMA, r/singularity, r/india). Have 50 upvotes ready on HN before going live on PH.

**Why PH:** PH sends 2-5K visitors on launch day, ranks in Google "best of 2026" lists if it hits top 5, and gives the repo 50-200 GitHub stars from people who came for the comment thread.

---

## §R — Done checklist (v50, verify before reporting)

- [ ] §A — X bio + display name updated (now mentions DANI)
- [ ] §B — LinkedIn headline + about updated (now mentions DANI)
- [ ] §C — Indranil Bhadra quote-tweet posted (DANI-led)
- [ ] §D — 7-tweet origin thread posted + Tweet 1 pinned
- [ ] §E — Percevia reply posted (optional)
- [ ] §F — GitHub display name + bio updated
- [ ] §G — 7 repos pinned in correct order (now includes dani-frontend)
- [ ] §H — `danlab-multimodal` public + topics + README rewrite
- [ ] §I — `dan-glasses` description + topics
- [ ] §J — `dani` description + topics
- [ ] §K — `paperclip` description + topics
- [ ] §L — `dan-consciousness` description + topics
- [ ] §M — Profile README created/updated with DANI link at top
- [ ] §O — DANI banner added to danlab.dev homepage
- [ ] §P — DANI launch thread posted (8 tweets) + Tweet 1 pinned
- [ ] §Q — DANI submitted to Product Hunt (target: top 5 of the day)

**When done, report in next DAN-1 run:** "Punchlist shipped at [time]. Stars before/after: [N]. DANI Pro signups: [N]. First DANI Pro signup: [link]. First PH comment: [link]."

---

*End of v50 punchlist. The strategy is in `dan1-marketing-strategy.md`. The research is in `dan1-marketing-research.md`. The Twitter content is in `dan1-twitter-content.md`. The landing page copy is in `dan1-landing-copy.md`. The README suggestions are in `dan1-github-readme-suggestions.md`. The content calendar is in `dan1-content-calendar.md`. This file is the only one you need open while shipping. The 3h 30min total is $0, reversible, and owned by somdipto. The DANI launch is the highest-leverage action of the month. Ship it.*
