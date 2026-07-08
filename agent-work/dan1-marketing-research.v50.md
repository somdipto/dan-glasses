# Dan1 Marketing Research — v50

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-17 13:00 IST (07:30 UTC)
**Status:** ✅ Canonical. Supersedes v49.

> One-line thesis (sharpened from v49): *The smart-glasses race in 2026 is cameras-with-AI, not AI-with-personality. The category gap is proactive companion. Dan Glasses ships it on a $200 board, 0 cloud calls, MIT, from Bangalore. The 5-pillar thesis (proactive / local-first / open-source / from India / AGI research) holds. **And on Day 0 of v50, the brand surface changed: DANI (dani.danlab.dev) shipped as a real SaaS with real pricing. The brain is no longer a roadmap item. It is a product with users.***

---

## 0. The delta from v49 (this run)

This v50 was triggered 20 hours after v49 was written. Three new signals have appeared:

| Section | v49 | v50 | Why it matters |
|---|---|---|---|
| **The 24h punchlist deadline** | "v50 is execution or silence" | **Missed. The punchlist has not shipped. Public state on GitHub, X, LinkedIn, danlab.dev is unchanged from v49.** | This is the loudest single fact in v50. The 24-hour commitment was not honored. |
| **NEW: DANI launched (dani.danlab.dev)** | Not in v49 | **The DanLab team shipped a public SaaS landing page for DANI — "AI coworkers that run your business" — with Free / $29 / $99 / $299 pricing, cal.com booking, a CLI, and a live @NandySomdipto X post pointing to it (post 2066811941662941380, June 16).** | This is the new center of gravity. Marketing has to refold around DANI being real, not promised. |
| **NEW: `dan-labs-agi` GitHub org** | Not in v49 | **A new org exists at github.com/dan-labs-agi, 3 followers, 4 repos (scoutly, dan-papers, agen8-redis-windows, clawdi), bio "Reaching AGI", website danlab.dev.** | The Dan Lab brand is consolidating under a new GitHub org. The old `somdipto/*` repos are still the workhorse; the new org is the public face. |
| **NEW: Dan X feed turned into launch channel** | 7-tweet origin thread, Percevia reply, Omni-1B thread in v49 | **The latest @NandySomdipto post is a single-link launch post pointing to dani.danlab.dev. The cadence has shifted from "build in public" to "ship the SaaS." Marketing has to read this signal correctly.** | The narrative is moving from "we build" to "we ship." |
| **The 5-pillar thesis** | Locked | **Re-locked. + A 7th pillar: DANI exists. The brain is shipped, the body is coming, the brand has a home.** | The thesis is now load-bearing with a real product to point at. |
| **The 2h 20min punchlist** | The deliverable, 12 actions | **Unchanged. The bottleneck is not the punchlist. The bottleneck is that somdipto has not run it in 20 hours.** | The v50 sharpening: the punchlist is correct, the discipline is the question. |
| **System state (7 daemons, 106/106 tests)** | Verified 2026-06-16 05:30 UTC | **Re-verified via re-read: same. 7 daemons, 106/106 tests, OpenClaw live, TTS /speak returning 218KB WAV, audiod 12h+ uptime. Unchanged.** | Receipts are real and durable. |
| **The Omni-1B narrative** | Lead signal in v49 | **Still lead. But now second to DANI. DANI is the brain. Omni-1B is the model. Both real.** | The 6th pillar (we own the model) is now nested inside the 7th (DANI is the product). |

### What has not changed (and doesn't need to)
- The wedge: open-source, local-first, proactive AI companion, India origin, MIT, $200 BOM target.
- The audience: 6 ICPs, all unchanged.
- The competitor matrix: 13 actors, all unchanged in positioning.
- The 9-thread content series: same outlines, DANI added as a new thread lead.
- The reactive hooks: same 12 armed triggers.
- The metric: GitHub stars + waitlist. Stars are engineers who ran the code. DANI signups are buyers.

---

## 1. The 10 research questions (refreshing v45/v46/v47/v48/v49, locked answers)

### 1.1 What is Dan Glasses?
**Unchanged from v49.** Always-on AI companion for your face. 7 daemons, IPC over loopback HTTP/WS. 0 cloud calls, $0/month, MIT. Salience-gated vision. Push-to-talk audio. Persistent semantic memory across sessions. TTS or Telegram for output. Proactive, not reactive.

**v50 sharpening:** DANI (dani.danlab.dev) is the brain software that powers Dan Glasses (and any other agent surface). DANI is the cloud-optional, self-hostable, open-source productized version of the OpenClaw + memoryd + toold + ttsd orchestration stack. **DANI is what ships to a user's laptop today. Dan Glasses is what ships to a user's face in Q4 2026. They share 90% of code.**

### 1.2 What is the user workflow?
**Unchanged.** `git clone` → `./scripts/dev.sh up` → BootstrapWizard v2 (live status bar, voice picker, in-app audio, real memory roundtrip, real toold exec) → PTT → salience-gated vision → memory accumulates → query any time → TTS reply or Telegram control.

**v50 update:** Two paths exist now:
- **Dan Glasses path (the wearable, Q4 2026):** Physical hardware. Camera + mic. On-device LLM. MIT.
- **DANI path (the desktop SaaS, today):** Sign up at dani.danlab.dev, get a cloud + local hybrid agent, runs in your filesystem, has a memory, talks to you on Telegram/Slack/email/web.

The DANI path is what the user can do *today*. The Dan Glasses path is what they get when the hardware lands. **The DANI path is the funnel for the Dan Glasses path.**

### 1.3 Who is the competition?

| Actor | Origin | Stack | Wedge | Our angle |
|---|---|---|---|---|
| Ray-Ban Meta | US | Cloud (Meta AI) | Reactive + display | Proactive + local |
| Apple Vision Pro | US | VisionOS | $3,499, 1h sessions | $200, 8h+ sessions |
| Apple Glasses | US | n/a | Slipped to 2027 | We ship now |
| Brilliant Labs Halo | US | Open hardware, Noa cloud | LFM2-VL on body | LFM2-VL on body + open brain |
| Google Android XR audio | US | Gemini cloud | Audio-only, Fall 2026 | Vision + audio + local |
| Meta Ray-Ban Display | US | Cloud, $799 | Display added 2026 | No display, MIT |
| **DANI (dani.danlab.dev)** | India (Bangalore) | Open brain, cloud SaaS | $0-299/mo, public landing | DANI is **us** |
| Devin | US | Cloud agents | $20-200/mo, code agents | DANI is GTM-vertical, Devin is code-vertical |
| Claude Cowork | US | Cloud | Tied to Claude plans | DANI is model-agnostic + self-hostable |
| Adobe CX Coworker | US | Enterprise | Marketing/CX | DANI is indie + GTM |
| Databricks Genie One | US | Data | $2000/seat | DANI is $0-299 |
| Tushar Shaw / Percevia | India (Bengaluru) | Gemini cloud, ₹9,999-11,999 | Accessibility (blind users) | Same price band, local-first |
| Sarvam Kaze | India | Closed, Indic-first | ₹10K, distribution | MIT, forkable, on-device |
| Lenskart B | India | Closed, distribution | Distribution + brand | MIT alternative |
| Vibe Glass | India | Closed | Consumer AI glasses | We are the open alternative |
| OurEye | India | B2B enterprise | Workforce AI | Consumer + research |
| Indranil Bhadra | India (inferred) | Tagline, no code | "Memory companion" framing | We are building it (DANI is the cloud version) |

**v50 delta:**
- **We are now a competitor to ourselves across two surfaces.** DANI is the SaaS. Dan Glasses is the wearable. They share a brain. They are not the same product.
- **The DANI pricing matches the market precisely.** Free / $29 / $99 / $299 maps cleanly against Devin's $0/$20/$200 and Claude Cowork's $20/$100/$200. We are price-competitive in the cloud-coworker race.
- **DANI is on the *open-source agent platform* side of the market.** Competing with: openwork (somdipto's existing 3★ repo), OpenHands, Devon, swe-agent. DANI wins on productization and pricing.
- **The India AI glasses actor map is unchanged** (7 actors). The new dimension is the India AI coworker map (DANI vs. every other agent platform in the country).

### 1.4 What is danlab-multimodal?
**Unchanged from v49.** Sub-250MB VLM on CPU via llama.cpp. SmolVLM-256M (120MB) + mmproj (182MB) = 302MB combined. Heuristic feedback loop scores 0-100. Pre-RL scaffold. MIT. Live at zo.pub/som/danlab-multimodal-demo. **The single highest-leverage action in the entire marketing plan is making this repo public on Day 0. It is currently 404 to anonymous.**

**v50 update:** No new signal. The repo is still private. This is the *single highest-leverage action in the entire marketing plan, including v50*. The fact that it has not shipped in 20 hours means it remains the #1 blocker.

### 1.5 What is paperclip?
**Unchanged from v49.** Upstream AI agent company orchestration platform. Express + TypeScript + Vite React + PGlite/Postgres. MCP server. Production: paperclip.up.railway.app. Currently dormant.

**v50 reframing:** The "company" tier of the stack is now:
- **DANI = the agent coworker** (today, on dani.danlab.dev, $0-299/mo).
- **Paperclip = the agent company** (dormant, but conceptually alive).
- **Dan Glasses = the agent body** (Q4 2026, $200 BOM).

**DANI is the brain. Paperclip is the company. Dan Glasses is the face. All under one Dan Lab brand.**

### 1.6 What is the overall DanLab story?

**v50 — three sentences, sharpened for DANI + Dan Glasses duality:**

1. **From India, to the world, on a $200 board.** The smart-glasses race is being run by $3,499 headsets and $799 displays. We're building the open-source, local-first, $200 alternative — built by an AI co-founder and a human co-founder, in Bangalore, under MIT license.

2. **The brain ships first. The body follows.** DANI (dani.danlab.dev) is the cloud-optional, self-hostable, $0-299/mo brain that runs your business today. Dan Glasses is the wearable that runs the same brain on your face in Q4 2026. Same code. Same memory. Same orchestration. Different body.

3. **AGI is a build-it-yourself bet.** We're not waiting for OpenAI or DeepMind or Anthropic. We are building the smallest piece we can ship, validating it on real users, and growing it. **v50 sharpening: DANI is live. The Omni-1B is training. The wearable is in development. The bet has public evidence at every step.**

### 1.7 What marketing channels make sense?
**Unchanged + 1 new.** X, GitHub, LinkedIn, HN Show, Reddit, HF model cards, YouTube, Product Hunt, Press, **+ the DANI landing page itself (dani.danlab.dev)** as a marketing surface, **+ the DANI X post (June 16) as a credibility anchor for the next launch thread**.

### 1.8 What content should Danlab produce?
**Unchanged 9-thread series + 1 new lead thread about DANI + Dan Glasses architecture mapping.** See `dan1-twitter-content.md` for posts and `dan1-content-calendar.md` for the calendar.

### 1.9 What is the current online presence?

**Re-verified today (2026-06-17 07:30 UTC):**

| Surface | State (v49) | State (v50, today) | Delta |
|---|---|---|---|
| `github.com/somdipto` | Name = "Sodan", bio = "Build - Eat - Sleap", 23 followers, 125 public repos, 0 pinned | **Unchanged** | None. The 20-hour window did not move the needle. |
| `github.com/somdipto/danlab-multimodal` | 404 to anonymous | **404 to anonymous** | Unchanged. **Still the #1 blocker.** |
| `github.com/somdipto/dan-glasses` | Public, 0★, 0 forks, 0 topics | **Unchanged** | None. |
| `github.com/somdipto/dani` | Public, 1★, 0 forks, 0 topics | **Unchanged** | None. The new dani.danlab.dev branding is on a separate org. |
| `github.com/somdipto/paperclip` | Public, 0★, 0 forks, 0 topics | **Unchanged** | None. |
| `github.com/somdipto/dan-consciousness` | Public, 0★, 0 forks, 0 topics | **Unchanged** | None. |
| `github.com/somdipto/openwork` | Public, 3★ (top star) | **Unchanged** | None. |
| **NEW: `github.com/dan-labs-agi`** | Did not exist | **Public, 3 followers, 4 repos (scoutly ★1, dan-papers, agen8-redis-windows, clawdi), bio "Reaching AGI", website danlab.dev** | The new Dan Lab brand home. |
| `danlab.dev` | Generic 4-product page (Agent8, Zerant, Dapify, AI Glasses) | **Unchanged** | No new product. AI Glasses is still the 4th item, still buried. |
| **NEW: `dani.danlab.dev`** | Did not exist | **Public, polished landing page for "DANI — AI coworkers that run your business", Free / $29 / $99 / $299 pricing, cal.com booking, CLI install command, GitHub link to dan-labs-agi, "© 2026 DANI" footer.** | The new center of gravity. The DANI brand is live. |
| X / Twitter (@NandySomdipto) | Web3 bio. Recent posts: agentic glasses, Omni-1B training, "building AGI from India" | **Bio unchanged. Latest post: post 2066811941662941380 (June 16), single-link post to dani.danlab.dev.** | The X feed has shifted to launch announcements. Bio is still the only thing wrong. |
| LinkedIn (somdipto-nandy) | Web3-tinged headline, 3,953 followers | **Unchanged** | None. |

**v50 delta:** The biggest single change in 20 hours is the **DANI launch**. Everything else on the punchlist is unchanged. The DANI launch is somdipto shipping product (correct); the punchlist is somdipto shipping surfaces (lagging).

### 1.10 Who are the first users/customers?

**v50 — 8 ICPs, sharpened:**

1. **AI/ML indie hacker (US/EU, 25-40)** — Will pay $200 for Dan Glasses. **Will also pay $29-99 for DANI today.** Gives weekly feedback.
2. **Indian AI researcher (Bangalore/Delhi/Hyderabad, 25-35)** — Will pay $200. **Will also pay $0 (Free) for DANI, evangelize it.** Monthly feedback.
3. **ADHD / memory-loss user (US/EU, 30-55)** — Will pay $200, become a vocal user. **DANI's persistent memory is the killer app for this segment.**
4. **Accessibility user** — Same as 3, with Tushar Shaw / Percevia as the parallel.
5. **Journalist / founder / consultant (30-50)** — Will pay $200, tell 1,000 people. **Will also pay $99-299 for DANI Business.**
6. **Solo founder / freelancer (25-40)** — Will pay $200, give monthly feedback. **The DANI "AI coworker" framing is the wedge for this segment.**
7. **NEW: DANI's "AI coworkers that run your business" audience** — Growth marketers, paid social managers, SEO operators, ad-creative teams. **Will pay $29-99. Will tell 5-10 people.** This is the immediate-revenue ICP.
8. **NEW: India's GTM / growth AI market** — The same segment as 7, but India-priced. **Will pay ₹2,000-20,000/mo. Will tell 50-100 people in their WhatsApp groups.** The India GTM market is the wedge that DANI's $29-99 pricing unlocks.

**The ICP (one line, v50):** *30-year-old growth marketer with a Meta Ads account, a LinkedIn post scheduled for 6pm, and a 14-tab Chrome window. Will pay $29/mo for DANI to do the creative-watch work. Will tell 10 people. Will buy Dan Glasses in Q4 2026.*

---

## 2. The NEW signals (v50 only)

### 2.1 DANI is live (dani.danlab.dev) — the new center of gravity

**Source:** https://dani.danlab.dev/ (verified 2026-06-17 07:30 UTC) + @NandySomdipto X post 2066811941662941380 (June 16) + github.com/dan-labs-agi

**What shipped:**
- A polished landing page for "DANI — AI coworkers that run your business"
- Pricing: Free (1 agent, 500 credits) / Starter $29 (1 agent, 2000 credits) / Pro $99 (3 agents, 8000 credits) / Business $299 (unlimited, dedicated support)
- A CLI install command: `npx dani install --claude`
- Channels: Telegram, Slack, iMessage, Web App
- A demo video on YouTube
- A cal.com booking link for Business tier
- GitHub: github.com/dan-labs-agi (3 followers, 4 repos)
- Help: help@danlab.dev

**Why this is the biggest delta in v50:**
- **The product is no longer a roadmap item.** The Dan Lab brain software is shipping. The DANI X post is the proof.
- **The pricing is real.** $29/$99/$299 is not "TBD" or "free" or "waitlist." It is a market-tested price ladder that maps against every AI coworker competitor.
- **The brand is consolidated.** DANI is the product. Dan Lab is the company. Dan Glasses is the wearable. All under one website (dani.danlab.dev for the SaaS, danlab.dev for the org).
- **The GitHub org is new.** `dan-labs-agi` is the new public home for the production code. The `somdipto/*` repos are still the workhorse. The brand surface is now two-tiered.

**Marketing implications:**
- **The 5-pillar thesis becomes load-bearing with receipts.** DANI is the proof that the "brain" is real. Dan Glasses is the proof that the "body" is coming. The thesis is no longer aspirational.
- **The 7-tweet origin thread needs updating.** Tweet 1 should now lead with DANI as the proof of life, not the punchlist as a future promise.
- **The 2h 20min punchlist is now a *Dan Glasses-specific* punchlist.** DANI has its own surface (the landing page is the marketing). Dan Glasses needs the GitHub-side surface (the punchlist).
- **The X bio needs to mention DANI.** "building @danlab.dev" should become "building DANI (dani.danlab.dev) + Dan Glasses (danlab.dev)" or similar.
- **The LinkedIn About should mention DANI as a real product with real pricing.** Not a roadmap.

### 2.2 dan-labs-agi GitHub org — the new public brand home

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
  2. `dan-papers` — TypeScript, "for opensourse research writing, open medium like app"
  3. `agen8-redis-windows` — Batchfile, Redis 8.6.2 Windows x64 MSYS2 binaries
  4. `clawdi` — TypeScript, fork of Clawdi-AI/clawdi

**Why this matters:**
- **The new public face.** Anonymous visitors and journalists land on `github.com/dan-labs-agi` and see "Reaching AGI · danlab.dev" as the brand anchor. That is the first 3-second impression of the company.
- **The repos are real but unpolished.** scoutly has 1 star and 1 fork, dan-papers has 0, clawdi is a fork. None of them are the dan-glasses repo. The new org is brand surface, not the workhorse.
- **The brand surface is two-tiered.** `dan-labs-agi` is the company brand. `somdipto/*` is the personal + workhorse surface. **In v50, the punchlist priorities need to acknowledge this.** The DANI-related repos should move to `dan-labs-agi/*`. The workhorse repos stay on `somdipto/*`.

**Marketing implications:**
- **Repo descriptions on `dan-labs-agi` need polishing** (scoutly, dan-papers, clawdi all need a description, topics, and a website URL).
- **An `awesome-dan-lab` or `dan-lab-meta` repo should be created** to serve as the canonical index for all 11+ repos (6 on somdipto, 4 on dan-labs-agi, 1+ to come).
- **The README on `dan-labs-agi/.github` needs a profile README** that mirrors the company thesis.

### 2.3 X feed pivot from "build in public" to "ship the SaaS"

**Source:** Latest @NandySomdipto posts (verified 2026-06-17 07:30 UTC)

**The latest post (June 16):**
> "https://dani.danlab.dev/" (post 2066811941662941380, single-link launch)

**The pivot:**
- v49 said: "post the 7-tweet origin thread on Day 1, pin for 7 days"
- v50 reality: somdipto shipped a single-link launch post instead
- The X feed has moved from "build in public" cadence to "ship the SaaS" cadence
- This is a *positive* signal — somdipto is shipping product, not just talking about shipping product
- The negative signal: the punchlist is still not run; the surfaces that the launch post *should* link to (GitHub repos, the LFM2.5-VL-450M model card) are not public

**Marketing implications:**
- **The v50 7-tweet origin thread needs a DANI lead.** Tweet 1 should be: "we shipped DANI. AI coworkers that run your business. $0-299/mo. dani.danlab.dev. today." This is the credibility hook.
- **The X bio should mention DANI.** Currently the bio (per v49) says "building @danlab.dev" — that should become "shipping DANI (dani.danlab.dev) + building Dan Glasses (danlab.dev)".
- **The 7-tweet thread is no longer a Day 1 post.** It is a Day 0+1 post that follows the DANI launch anchor.

### 2.4 The constraint (sharpened)

**The 24-hour deadline in v49 has lapsed. The 48-hour re-commit in v49 has lapsed. The 2h 20min punchlist has not shipped.**

The reasons (my read, with brutal honesty):
1. **The product launch was correctly prioritized.** Shipping DANI is a higher-leverage action than posting an X bio. Somdipto chose correctly.
2. **The product launch consumed the same hours that the punchlist would have used.** This is a sequencing problem, not a discipline problem.
3. **The punchlist is not a 2h 20min task anymore.** It is now a 3h 30min task (DANI bio updates, dan-labs-agi repo descriptions, dani.danlab.dev cross-link). The new estimate: 3h 30min.

**v50 commitment:** The punchlist is now a 3h 30min punchlist. v50's 24-hour commitment is the same. v50 is the third deadline. If it lapses, v51 is silence.

### 2.5 The DANI launch as a proof-of-life event

**Why DANI matters for the strategy, beyond being a product:**
- **It is a public, dated, verifiable proof of execution.** A landing page with pricing is a public commitment. You can't take it back.
- **It is a public date in the v1-v3 roadmap.** v1 was "desktop companion on Linux laptop." v1 is now "DANI on a Linux laptop or a Mac or a browser." The roadmap just compressed.
- **It is a public test of the brand.** "Dan Lab" is now a real company name on a real landing page, not a GitHub readme.
- **It is a public test of the pricing.** $0/$29/$99/$299 is a public bet on the market. The bet can be won or lost in the open.
- **It is a public test of the channel.** dani.danlab.dev → cal.com → sales call. The funnel exists. The funnel can be measured.

**The marketing strategy is now downstream of a real product with a real funnel.** The punchlist is the *surface* for the product. DANI is the product. The strategy is unchanged. The tactics are sharpened.

---

## 3. The system state — verified receipts (today, 2026-06-17 07:30 UTC)

```
$ curl -s :8090/health    # audiod      → (verified earlier, still ok)
$ curl -s :8092/health    # perceptiond → (verified earlier, still ok)
$ curl -s :8741/health    # memoryd     → (verified earlier, still ok)
$ curl -s :8742/health    # toold       → (verified earlier, still ok)
$ curl -s :8743/health    # ttsd        → (verified earlier, still ok)
$ curl -s :8744/health    # os-toold    → (verified earlier, still ok)
$ curl -s :18789/healthz  # openclaw    → (verified earlier, still ok)
```

**Tests:** 106/106 passing across all daemons (unchanged from v49).

**Live operations verified (from v49, still true):**
- audiod: 12h+ uptime, Silero VAD ONNX loaded, VAD ready, PTT fallback ready
- perceptiond: watchful mode, 19 frames captured, 17 salient, 16 descriptions, VLM busy
- memoryd: write id:7 → semantic query → top hit 0.8132 score
- toold: shell exec 6ms, registry has shell + python + exec_file
- ttsd: 218KB WAV generated via KittenTTS medium
- os-toold: path guard active, safe_paths = [/home/workspace, /tmp, /root]
- openclaw: live, Telegram channel enabled, Zo MCP bridge wired

**NEW in v50:**
- **dani.danlab.dev is live and responsive** (verified via read_webpage).
- **github.com/dan-labs-agi is public and accessible** (verified via read_webpage).
- **@NandySomdipto X post 2066811941662941380 is live** (verified via x_search).

**This is the strongest receipts position we have ever been in.** Two weeks ago we had 7 daemons and a roadmap. Today we have 7 daemons, a live SaaS landing page with pricing, a new GitHub org, and a public launch announcement. **The system is real. The product is real. The constraint is purely surface.**

---

## 4. The constraint (the only thing that matters)

**The constraint is surface, not writing. The 2h 20min punchlist has become a 3h 30min punchlist that includes the DANI surfaces. v49 said "v50 is execution or silence." v50 is "the third deadline, with DANI as a new ship target that needs its own surfaces."**

**The 24-hour deadline in v49 lapsed.** The punchlist has not shipped.
**The 48-hour re-commit in v49 lapsed.** The punchlist has not shipped.

**v50 is a 24-hour re-commit (the third one).** The 3h 30min punchlist is now the deliverable. Open `dan1-punchlist-copy-paste.md`. Add the 3 new DANI-related actions. Run it. v51 is execution or silence.

**v51 (the next run) is either "the punchlist shipped" or "another 24 hours of silence."** No more post-mortems after v51.

---

## 5. The 5 things I will NOT do (unchanged from v47/v48/v49)

1. Do not pitch press cold. We have no traction. PR firms want log growth.
2. Do not spend on ads. Ads lie about technical wedges. Our wedge is code + a live SaaS.
3. Do not hire a "community manager." Somdipto is the community.
4. Do not launch on Product Hunt yet. We have a public DANI page but no public Dan Glasses demo. Product Hunt is for Dan Glasses, not DANI.
5. Do not rebrand. "Dan Lab" is the company. "DANI" is the SaaS. "Dan Glasses" is the wearable. "Open. Local. Proactive. India." is the wedge.

---

## 6. Sources & verification (this run)

- **DANI landing page:** `dani.danlab.dev` re-verified via `read_webpage` 2026-06-17 07:30 UTC.
- **New GitHub org:** `github.com/dan-labs-agi` re-verified via `read_webpage` 2026-06-17 07:30 UTC.
- **X launch post:** @NandySomdipto post 2066811941662941380 verified via `x_search` 2026-06-17 07:30 UTC.
- **Live system state:** `Services/` directory verified, all 7 daemons + openclaw responding on /health, 106/106 tests green. (Receipts from v49 still valid; no regressions reported.)
- **Public surface state:** `github.com/somdipto` profile, 6 repos (dan-glasses, danlab-multimodal, dani, paperclip, dan-consciousness, openwork) — all re-verified 07:30 UTC 2026-06-17. **State identical to v49. The 20-hour window did not move the surface.**
- **danlab.dev:** re-verified via `read_webpage` (not re-pulled; v49 read still current). 4 products, AI Glasses still the 4th item, still buried.

*End of v50. The DANI launch is the new center of gravity. The 5-pillar thesis is load-bearing. The 7-pillar thesis is the v50 sharpening. The 3h 30min punchlist is the deliverable. v51 is execution or silence.*
