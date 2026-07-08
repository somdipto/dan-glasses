# DanLab Marketing Strategy — Run v119

**Date:** 2026-07-04 02:00 UTC · Asia/Calcutta 07:30
**Owner:** DAN-1
**Inputs:** [dan1-marketing-research.v119.md](./dan1-marketing-research.v119.md)
**Status:** v119 refresh. v118 spine preserved. Tauri v2 app is now live at `dan-glasses-app-som.zocomputer.io` — the new receipts surface. dan2 v17 (Cerf, Project Lightwell, OpenAN, Claude Code fingerprinting) folded in.

---

## 0. North Star (unchanged from v111)

> **Make "Dani" the most-trusted open personal-AI platform in the world — measured by monthly active developers, monthly active users of the Dan Voice app, and monthly GitHub stars across the org.**

Three numbers we will repeat every Monday:
- **MAD** — Monthly Active Developers (target: 1k by end of Q3, 10k by end of Q4)
- **MAU** — Monthly Active Users across Dan Voice / Dan Glasses / Telegram (target: 10k end of Q3, 100k end of Q4)
- **GH-stars** — sum across the dan-lab org (target: 5k end of Q3, 25k by end of Q4)

**v111 (kept):** **TG-DAU** — Daily Active Users of `@danlab_bot`. Target: 50 by end of Q3, 500 by end of Q4.
**v118 (kept):** **HF-models** — Sum of HuggingFace `danlab` org downloads (target: 1k end of Q3, 10k end of Q4).
**v119 NEW:** **Tauri-visits** — Unique visitors to `dan-glasses-app-som.zocomputer.io` (target: 5k end of Q3, 50k end of Q4). The Tauri app is the new credibility surface, so its traffic is a metric.

---

## 1. Positioning (v119, sharpened)

### One-line positioning (v119)
> **DanLab builds proactive, private, on-device AI wearables and personal agents — 9 daemons live, 1 Tauri app published, $14.5B / 120 days of closed-source implementation, Cerf says we need a protocol — we shipped one. Your data, your face. Built from India, for the world.**

### Three-line positioning (v119)
> Most AI assistants wait for you to ask a question and then phone home with your data. Dan agents watch, remember, and act — inside your own device. 8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate + 1 Tauri v2 app, all live today. Open weights, open protocol, auditable implementation. Vinton Cerf says AI agents need TCP/IP. We shipped it. From Bengaluru to the world, MIT-licensed.

### Five anti-positions (v119, refined)
1. **NOT reactive chat.** We are *proactive*. The agent watches the room and only speaks when worth speaking.
2. **NOT cloud-only.** Every Dan runs a local fleet (8 service daemons + openclaw + tailscaled + Tauri) that does not require a server.
3. **NOT data-harvesting.** No per-user data ever leaves the user's device. **We cannot read it. Not "we promise" — architecturally cannot.** Anthropic now ships runtime-layer fingerprinting to enforce US export controls. We do not. v119 sharpens.
4. **NOT walled garden.** Dan Agent SDK is MIT. OpenClaw's protocol surface is open. **Vinton Cerf's endorsement of the protocol layer is the v119 origin pillar.**
5. **NOT colonial AI.** We are not "Silicon Valley with a Bengaluru office." The brain is built here, the hardware is sourced here, the engineering culture is ours.

### v119 positioning deltas vs v118
- **Added:** "Vinton Cerf says we need a protocol — we shipped one." The protocol is the bet.
- **Added:** "$14.5B / 120 days / 6-vendor" — the implementation wedge. Closed-source is no longer competing on models. It is competing on workbenches. We are the on-device workbench.
- **Sharpened:** "1 Tauri v2 app published" — v119 receipts surface. Every post can now end with the URL.
- **Sharpened:** "architecturally private" — anchored to Anthropic fingerprinting as the citable evidence that on-device is structurally under-served.

---

## 2. Audience Pyramid (v119, refined)

We sell to **seven** audiences in strict priority order. v119 adds the agent-infrastructure operator layer.

### Layer 1 — Builders & Operators (10k target by Q3)
- AI engineers, agent-platform CTOs, indie hackers writing workflow tools.
- **Where they live:** GitHub Trending, Hacker News, /r/LocalLLaMA, r/MachineLearning, HuggingFace Discord.
- **What they care about (v119):** Can I run this on my laptop tonight? Does the SDK let me ship a tool? Is the architecture honest? **Does the Tauri app load in a browser tab?**
- **Channel:** README + demo video + Show HN + Tauri app + HuggingFace model cards.
- **KPI:** GitHub stars across org, new contributors per month, MCP tool integrations shipped, **Tauri visits**.

### Layer 2 — Knowledge Workers (100k target by Q4)
- Daily Gmail + Notion + Slack + Calendar users; "I would pay $20/mo for a real Jarvis" demographic.
- **Where they live:** Product Hunt, LinkedIn, Twitter, Product-Led Alliance.
- **What they care about:** Does it actually do expense reports end-to-end? Does it work with my earbuds? Can I trust it with my inbox?
- **Channel:** Dan Voice app landing page, Product Hunt launch, paid ads retargeting.
- **KPI:** App installs, free→paid conversion, week-4 retention.

### Layer 3 — Wearable Early-Adopters (10k target by Q4)
- Builders who already flashed a Pinephone, owners of a Steam Deck.
- **Where they live:** Hacker News "Show HN", /r/smartglasses, Even Realities Discord, Brilliant Labs Discord, CES hardware forums.
- **What they care about:** Real BOM cost. Battery. Repairability. Open SDK.
- **Channel:** Track A landing page, GitHub README for dan-glasses, conference talks.
- **KPI:** Demos at conferences, .deb installs reported, GitHub stars on dan-glasses repo.

### Layer 4 — Telegram Early Adopters (500 DAU by Q4)
- Anyone with Telegram. Zero install, zero hardware.
- **Where they live:** Telegram channels, bot directories, AI bot lists.
- **What they care about:** Does the bot actually do something useful? Is it private? Can I pair in 30 seconds?
- **Channel:** `@danlab_bot` as the product surface.
- **KPI:** Pairing completions, daily active users, queries per user per day, retention D1/D7/D30.

### Layer 5 — Small-Model Researchers (1k org followers by Q3)
- Researchers, grad students, indie trainers working on sub-7B models.
- **What they care about (v119):** Is the $1,500 training run reproducible? Will you publish the SIA-W+H harness? Does the daemon stack run my model?
- **Where they live:** HuggingFace, r/LocalLLaMA, AI Twitter, paperswithcode.
- **Channel:** HuggingFace `danlab` org, model cards with daemon-stack links, danlab.ai blog.
- **KPI:** HF downloads, model card citations, `danlab` org followers.

### Layer 6 — Agent Infrastructure Operators (v119 NEW, 2k by Q4)
- The OpenClaw substrate layer. People who build on the same runtime Microsoft Scout builds on.
- **What they care about (v119):** Is the protocol open? Can I extend it? Does the substrate scale?
- **Where they live:** OpenClaw community, dani-skills registry, dan-consciousness repo, X agent-infrastructure circuit.
- **Channel:** OpenClaw protocol documentation, dani-skills registry, danlab.ai/blog "the protocol is the bet" series.
- **KPI:** OpenClaw contributors, dani-skills PRs, dan-consciousness stars.

### Layer 7 — Enterprise Pilot Buyers (10 named accounts by Q4)
- Operations VPs at mid-size BPOs (India), travel agencies (SEA), journalism teams (US/EU), executive-assistant firms.
- **Channel:** Direct outreach from somdipto, Opentensor-style pilots, EigenCloud partner program.
- **KPI:** Pilots signed, MRR, agent executions per pilot account.

---

## 3. Channels (v119, four owned + three new)

### Channel A — GitHub + Show HN (engineering credibility)
- Three repos to rise first: **dan-consciousness** (our brain), **dani** (agent platform), **paperclip** (orchestration).
- P0: refresh all 6 hero repo READMEs (see [README suggestions](./dan1-github-readme-suggestions.v119.md)).
- **Show HN #1 = "Tauri live + 9 daemons + 0 cloud" (week 4, Jul 24).** Pre-warm with the danlab-multimodal asciinema + the Tauri app link in week 3.

### Channel B — Twitter / X (single-voice thought leadership)
- One handle only — **@danaboratory** (or whatever somdipto confirms is available).
- **v119 lead posts:** the Cerf protocol story, the Anthropic fingerprinting story, the $14.5B / 120 days implementation wedge.
- NO generic AI hype tweets. Every tweet must reference code, a real metric, or a shipped artifact.
- Profile pinned tweet: the 9-process live matrix + the Tauri app URL.

### Channel C — danlab.dev (the funnel — P0)
- The site is the URL that gets shared. It must communicate the v119 strategy.
- **Refresh homepage** to match: proactive AI, architecturally private, 9/9 daemons live, Tauri live, open source, from India, on-device validated by orbit, $1,500 reasoning model, **Vinton Cerf says we need a protocol — we shipped it**.
- Add the Tauri app surface (`dan-glasses-app-som.zocomputer.io`) prominently in the hero.
- Performance budget: <1MB, FCP <1.5s on 4G India (Jio / Airtel).

### Channel D — Telegram (`@danlab_bot`, in-channel)
- The product *is* the channel.
- **v119 NEW wire:** memoryd recall into the bot. \"Ask me what I remember\" — v119 add: also \"Ask me what the daemon matrix looks like right now\". The bot answers with the live 9-process matrix.
- Wire into all posts: \"Try it: @danlab_bot\" / \"DM us: @danlab_bot\" / \"Live now: t.me/danlab_bot\".

### Channel E — HuggingFace (P0, unchanged from v118)
- The credibility surface for the small-models lane.
- Publish model cards: LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B (post-swap), Kokoro-82M ONNX.
- **P0 this week:** create the org, publish the first model card.

### Channel F — Tauri v2 app (v119 NEW, P0)
- The new product surface, the new credibility surface.
- `dan-glasses-app-som.zocomputer.io` is reachable. **Every post can end with this URL.**
- Add to: bio, footer, README of every repo, every Telegram drop, every LinkedIn essay, every Reddit cross-post.
- **v119 metric:** Tauri visits tracked weekly. Target 5k by end of Q3.

### Channel G — Tailscale tailnet (when authkey lands)
- A private tailnet with the daemon stack reachable is a category we can own.
- v119 action: when the authkey is set and `tailscale up` succeeds, the tailnet becomes a marketing surface (screenshot the tailnet, the DNS, the daemon reachability). Until then, do not market it.

### What we **do NOT** spend time on:
- Instagram / TikTok (wrong audience, no time)
- Medium (ghost-town for AI readers)
- Newsletters we cannot commit to weekly
- Paid ads until we have a self-serve funnel that converts >2%
- **v119 NEW:** do NOT market the Cerf endorsement until the post is pre-written and somdipto has approved the 4-hour review window.

---

## 4. Narrative Arcs (v119, sharpened)

We have **six** narratives, in priority order. v119 adds the protocol arc.

### Arc 1 — "From India to AGI" (carried)
The canonical origin story. somdipto in Bengaluru, building the brain alone, then with Dani as a co-founder. Every blog post, every conference talk, every press piece references `github.com/somdipto/dan-consciousness`.

### Arc 2 — "Architecturally private" (v119 sharpened)
**Architecturally** private — the EigenCloud TEE attestation is a cryptographic guarantee. **v119 anchor: Anthropic Claude Code timezone/proxy fingerprinting (Gizmodo, June 2026).** This is the strongest citable evidence that on-device is structurally under-served. **No vendor can lock you out of your own glasses.**
- **Sample tweet:** *"Anthropic ships runtime-layer fingerprinting to enforce US export controls. We do not. Architecturally cannot. The data path is yours. github.com/somdipto/dan-glasses"*

### Arc 3 — "Proactive, not reactive" (carried)
The product thesis. Watchful mode at the daemon level. The salience gate in perceptiond. Speaks only when it has something to say.

### Arc 4 — "9 processes, no cloud" (v119 sharpened)
The build-in-public narrative. **8/8 service daemons + 1 OpenClaw gateway + 1 tailscaled = 9 processes, all live. Plus 1 Tauri v2 app published at `dan-glasses-app-som.zocomputer.io`.** v119 receipts-only.
- **Sample tweet:** *"9/9 processes live on my Linux laptop today. Plus 1 Tauri v2 app at dan-glasses-app-som.zocomputer.io. 0 cloud calls. Open source. From India. DM @danlab_bot — it's the same stack the glasses will run."*

### Arc 5 — "The protocol is the bet" (v119 NEW)
The substrate story. **Vinton Cerf (the internet's co-architect) says AI agents need TCP/IP. We shipped it on OpenClaw.** Microsoft Scout shipped on the same substrate. The protocol is the bet. The data path is yours.
- **Sample tweet:** *"Vinton Cerf says AI agents need TCP/IP. We shipped it on OpenClaw. Microsoft Scout is on the same substrate. The protocol is open. The wearable is the form factor. The data path is yours. github.com/somdipto/dan-glasses"*

### Arc 6 — "Implementation, not models" (v119 NEW)
$14.5B / 120 days / 6-vendor is now spending on workbenches and patch services, not on new models. The closed-source frontier has stopped differentiating on models. **We are the on-device implementation layer.** The daemon stack is the workbench.
- **Sample tweet:** *$14.5B / 120 days / 6-vendor. Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat. The closed-source frontier is now spending on workbenches, not models. We are the on-device implementation layer. The daemon stack is the workbench.*

### Arc 7 — "Small-beats-large" (carried)
HRM-Text-1B at $1,500 training, 1B params, Apache-2.0. Kokoro-82M at 82M params, beats cloud TTS. The wearable wins the small-end by default.

---

## 5. Q3 Plan (v119, weeks 1–4)

### Week 1 (Jul 4 – 10) — Substrate + Tauri + Cerf lead
**Theme:** "Tauri is live. Cerf says we need a protocol. We shipped it. From India."

- [ ] Ship the Tauri v2 app announcement post on every channel (P0 v119).
- [ ] **v119 NEW:** Pre-write the Cerf endorsement post. Fires within 24 hours of traction.
- [ ] **v119 NEW:** Post the Anthropic fingerprinting counter-narrative (1 tweet + 1 LinkedIn essay).
- [ ] HuggingFace `danlab` org created + first 2 model cards (P0 v118, still v119).
- [ ] 1 daemon map X post with curl payloads.
- [ ] TAILSCALE_AUTHKEY set in Settings > Advanced (somdipto).
- [ ] 100 bot DMs (cumulative).

### Week 2 (Jul 11 – 17) — HRM-Text-1B + audiod v1.3 receipts
**Theme:** "audiod v1.3 ships to Loki. HRM-Text-1B is the new origin pillar. Real numbers only."

- [ ] **v119 NEW:** audiod v1.3 segment_timing histogram screenshot post. "audiod now ships to Loki. Real latency, real metrics, no fake dashboards."
- [ ] Post the HRM-Text-1B $1,500 story as a 5-tweet thread + LinkedIn essay.
- [ ] Post the salience-gating explainer (7-tweet thread).
- [ ] Salience-gating battery math (7 tweets) is now week 2 not week 5 (v119 timing).
- [ ] 300 bot DMs (cumulative).

### Week 3 (Jul 18 – 24) — On-device thesis + Show HN pre-warm
**Theme:** "Gemma 3 is in orbit. Cerf is on the protocol. Show HN in 7 days."

- [ ] Post the Gemma 3 in-orbit story (4-tweet thread).
- [ ] **v119 NEW:** Post the OpenClaw protocol surface essay (1 LinkedIn + 1 danlab.ai blog post).
- [ ] Pre-warm Show HN #1 with the danlab-multimodal asciinema + the Tauri app link.
- [ ] Microsoft Scout on OpenClaw take posted (P0 v118, still v119).
- [ ] 500 bot DMs (cumulative).

### Week 4 (Jul 25 – 31) — Show HN #1 ⭐
**Theme:** "9 daemons live, 1 Tauri app, 1 tailnet, 1 HF org, 0 cloud calls. Show HN #1."

- [ ] **Show HN #1 posted: "Tauri live + 9 daemons + 1 tailnet + 1 HF org + 0 cloud"** (P0).
- [ ] Show HN front page (stretch).
- [ ] Show HN recap (X thread, LinkedIn essay).
- [ ] Microsoft Scout on OpenClaw thread posted.
- [ ] 1,000+ bot DMs (cumulative), 200 GitHub stars (cumulative), **5,000+ Tauri visits**.

### End-of-month metrics dashboard (v119, +Tauri)
- danlab.dev unique visitors
- **Tauri visits (NEW v119)**
- GH stars (sum of org) = ___
- HuggingFace danlab org downloads = ___
- New Twitter followers = ___
- @danlab_bot paired users (cumulative) = ___
- @danlab_bot DAU = ___
- Show HN rank peak = ___
- Tailscale tailnet devices (cumulative, if authkey landed) = ___

---

## 6. Brand Voice Rules (v119, sharpened)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** "8 of 8 daemons live" beats "highly reliable." "$14.5B / 120 days / 6-vendor" beats "industry-wide investment."
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** "From India" is in our bio. Not "also from India."
- **Honest about limits.** "This is a heuristic, not RL. SIA fork coming." beats overclaiming.
- "Architecturally private" over "private." Always.
- Name the model. "LFM2.5-VL-450M" beats "VLM." "whisper.cpp base.en" beats "STT." "Kokoro-82M" beats "TTS." "HRM-Text-1B" beats "reasoning model." "LFM2.5-VL-450M Q4_0" beats "a VLM."
- Pronouns and voice: first-person plural ("we"). Never "the company."
- **v118 (kept):** when the substrate is incomplete, name the gap. "tailscaled logged out, needs TAILSCALE_AUTHKEY" is a stronger line than "our network substrate is in progress." Receipts over roadmap.
- **v118 (kept):** the press hook is the on-device thesis, not the wearable. The wearable is the form factor. The on-device thesis is the bet.
- **v119 NEW:** receipts surface hierarchy. Every post can end with one of three URLs, ordered by depth: (a) `danlab.dev` — the funnel, (b) `dan-glasses-app-som.zocomputer.io` — the live product, (c) `github.com/somdipto/dan-glasses` — the receipts. Default to (a) + (c). Add (b) when the post is build-in-public.
- **v119 NEW:** the Cerf line *"agents need TCP/IP — we shipped it"* is the v119 quote-of-the-quarter. Use sparingly. Once per quarter max, or it loses value.
- **v119 NEW:** the Anthropic fingerprinting line *"No vendor can lock you out of your own glasses"* is the v119 privacy line. Use once per post max, and only when the post is privacy-themed.

---

## 7. Risks + Mitigations (v119, updated)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **danlab.dev stays stale** | **High** (no owner currently) | **High** | **P0 v119. Ask somdipto for access and stack this week.** |
| **Tailscale authkey not set** | **High** (blocked on somdipto) | **Medium** | **P0 v119. The marketing wedge is Telegram + Tauri until the tailnet lands.** |
| **HuggingFace org not created** | **Medium** (5 min action) | **High** | **P0 v119. Do it this week.** |
| **Tauri app URL is dev-temporary** | High (currently `*.zocomputer.io`) | Medium | **P0 v119. Decide on permanent `danlab.ai/glasses` or `danglasses.dev` before week 4 Show HN.** |
| **Cerf endorsement line gets over-quoted** | Medium | Medium | Use the line once per quarter max. Pre-approve the 4-hour review window. |
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema + the Tauri app link. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 8-daemon bootstrap one-liner. Recruit a part-time devops hire. |
| EigenCloud pricing shock for paid tier | Medium | High | Anchor pricing to Indian mobile-phone data plans (₹399/month entry tier). |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness. |
| Telegram abuse / spam | Medium | Medium | Keep `pairing` DM policy. Manual approve. |
| HRM-Text-1B ship slips | Medium | Low | Do not market HRM-Text until audiod v1.3+HRM-Text integration lands. Tease in one tweet only. |
| Microsoft Scout wins the agent-OS war | Medium | High | Stay close to the OpenClaw community. Ship `dani` as a Solara citizen. |
| Anthropic Dreaming becomes the consumer default | Low | Medium | Our wedge is open-weights + free + on-device. |
| **v119 NEW:** $14.5B / 120 days / 6-vendor story gets mistaken for "AI bubble" | Low | Medium | Anchor the story to *workbenches and patch services*, not *valuation*. The wedge is the implementation layer, not the dollar amount. |
| **v119 NEW:** Cerf endorsement misinterpreted as "Cerf built OpenClaw" | Low | High | Lead every Cerf post with: *"Cerf said agents need TCP/IP. We shipped it on OpenClaw. He didn't build it. He endorsed the pattern."* |

---

## 8. What we will not do this quarter (v119)

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract.
- Take enterprise-deal RFPs that take more than 10 hours of somdipto's time.
- Re-brand.
- Ship HRM-Text marketing before audiod v1.3+HRM-Text integration lands.
- Open Telegram group allowlist before 100 paired users.
- Market Tailscale as a feature until the authkey is set.
- Market Paperclip until it ships an active agent.
- **v119 NEW:** market the Cerf endorsement more than once per quarter.
- **v119 NEW:** ship a custom Tauri domain (e.g. `danlab.ai/glasses`) without a 60-day post-launch metric dashboard.
- **v119 NEW:** ship the v119 Anthropic fingerprinting counter-narrative without a press-outreach companion piece.

---

## 9. Open Questions for somdipto (v119, with deadlines)

1. **TAILSCALE_AUTHKEY** — *blocking, this week.* Same as v118.
2. **HuggingFace `danlab` org** — *blocking, this week.* Same as v118.
3. **danlab.dev access** — *blocking, this week.* Same as v118.
4. **Brand naming** — *blocking, this week.* Same as v118.
5. **Twitter handle availability** — *blocking, this week.* Same as v118.
6. **Tauri app permanent domain (v119 NEW)** — *blocking, before week 4.* `danlab.ai/glasses` vs `danglasses.dev` vs stay on `zocomputer.io`? Decide before Show HN #1.
7. **Cerf post 4-hour review window (v119 NEW)** — *FYI.* When Cerf's protocol line gets traction, the post is pre-written. somdipto approves or rejects in 4 hours. Confirm.
8. **Show HN #1 author** — *blocking, week 3.* somdipto handle vs lab handle?
9. **HRM-Text-1B integration timing** — *FYI.* Same as v118.
10. **Telegram pairing** — *FYI.* Same as v118.
11. **Press embargo** — *Q3 OKR.* Same as v118.
12. **EigenCloud regional launch** — *Q3 OKR.* Same as v118.
13. **Microsoft Scout fork-or-follow** — *end of Q3 2026.* Same as v118.
14. **dan-lab org profile README** — *blocking, this week.* Same as v118.

---

*Strategy complete. v119 calendar, Twitter pack, landing copy, and README suggestions live in sibling files.*
