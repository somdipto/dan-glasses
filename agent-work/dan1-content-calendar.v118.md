# Dan1 — Content Calendar (v118)

**Run:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Period:** Q3 2026 (July 3 → October 1).
**Builds on:** `dan1-marketing-research.v118.md`, `dan1-marketing-strategy.v118.md`.

## v118 deltas (vs. v117)

1. **Substrate is the lead for week 1.** "8/8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate, 9 processes total." Receipts-first.
2. **HuggingFace org launch is week 1 P0.** First two model cards ship: SmolVLM-256M (with mmproj) + LFM2.5-VL-450M Q4_0.
3. **HRM-Text-1B is the new origin pillar.** Posts at weeks 2, 3, 4 + the long-form series "The on-device thesis" (3 posts).
4. **`@danlab_bot` DM call-to-action** is wired into every weekly post (carried from v117).
5. **Tailscale authkey blocker is named explicitly in week 1.** somdipto-facing copy + a "how to set TAILSCALE_AUTHKEY in 60 seconds" tweet.
6. **Gemma 3 in orbit is the press hook for week 3.** 4-tweet thread + LinkedIn essay + HF model card.
7. **Microsoft Scout on OpenClaw is the substrate story for week 4.** The first post that frames our substrate as a *defensible category*, not a dependency.
8. **Real-number rule (v118, sharpened):** if a claim cannot be backed by a `/status` payload, a Git commit, a paper, or a published number, do not post it. Specifically: the curl payload showing the 8 service ports + 1 gateway + 1 tailscaled process responding.

---

## Calendar philosophy (v118)

- **3–5 posts per week on X** (@danlab primary, @somdipto personal).
- **1 long-form piece per month** (danlab.ai/blog).
- **2 big drops in the 90 days:** Show HN #1 (week 4) + SIA-W+H port arXiv (week 12).
- **1 GitHub repo pass per week** (cleanups, not launches).
- **2 Reddit posts per week** (r/LocalLLaMA, r/MachineLearning, r/india).
- **1 LinkedIn post per week** (somdipto profile).
- **1 bot drop per week** (carried from v117).
- **1 HuggingFace model card per week** (NEW v118).

## Week 1 — Foundation + substrate + HF org (Jul 3–9)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| **Fri Jul 3** | **X (@danlab)** | **Substrate launch** | **"8/8 daemons live. 1 OpenClaw gateway. 1 tailscaled substrate. 1 HF org. DM @danlab_bot — it's live. 👓"** | Substrate + HF in lead |
| Fri Jul 3 | HuggingFace | `danlab` org created + first model card (SmolVLM-256M) | Sub-250MB VLM, Q4_K_M, anchor to danlab-multimodal demo. | NEW v118 |
| Sat Jul 4 | X | Daemon map screenshot | "8 service daemons. 1 gateway. 1 tailnet. Here's the live port map:" + curl payload | Receipts |
| Sun Jul 5 | X (@somdipto) | Origin post | "From India, you can't wait for the West to ship you intelligence. So you build it. 8 daemons live today. 1 OpenClaw gateway. 1 tailnet. 1 HF org." | v118 with HF + tailnet |
| Sun Jul 5 | HuggingFace | Second model card (LFM2.5-VL-450M Q4_0) | Sub-250ms edge inference, 512×512, anchor to perceptiond SPEC. | NEW v118 |
| Mon Jul 6 | LinkedIn | Long-form origin | "Why I'm building wearable AI from Bengaluru — and why 8 daemons + 1 tailnet + 1 HF org matter" | v118 framing |
| Mon Jul 6 | X | Tailscale authkey callout | "If you set TAILSCALE_AUTHKEY in @zo settings > advanced and `tailscale up --authkey=...` lands, our daemon stack joins the tailnet. Somdipto, this is the only substrate gap left. 60 seconds." | NEW v118 — unblocker ask |
| Tue Jul 7 | Reddit r/LocalLLaMA | 8-daemon thread | "8 daemons live, all local, .deb + systemd. The receipts below." | v118: HF + tailnet in receipt block |
| Wed Jul 8 | X | audiod liveness/readiness take | "Today: audiod ships the live/ready probe split. /live is the orchestrator restart decision. /ready is the traffic-routing decision. Receipts in the PR." | Build-in-public + receipts |

**Week 1 deliverables:**
- [x] @danlab profile live (bot, daemon fact, all in bio)
- [ ] HuggingFace `danlab` org live with 2 model cards (P0 v118)
- [ ] 8-daemon matrix on danlab.dev hero
- [ ] 1 daemon map X post with curl payloads (Sat)
- [ ] TAILSCALE_AUTHKEY set in Settings > Advanced (somdipto)
- [ ] 100 bot DMs (cumulative)

## Week 2 — Build-in-public + HRM-Text-1B origin pillar (Jul 10–16)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Thu Jul 10 | X | Loki metrics drop | "audiod now ships segment_timing histograms to Loki. Real latency, real metrics, no fake dashboards. PR: [link]" | — |
| Fri Jul 11 | X | **HRM-Text-1B origin pillar** (5-tweet thread) | **"A 1B model trained for $1,500 from scratch is now the SOTA small-reasoning model. Apache-2.0. We are integrating it into audiod v1.5 as the post-processor. Small-beats-large is empirically real. The India thesis: you don't need 1T tokens to ship intelligence."** | NEW v118 — origin pillar |
| Sat Jul 12 | X | Salience-gating explainer (7-tweet thread) | "Why our vision pipeline runs the VLM on *salient* frames, not fixed FPS. Battery math at the end." | — |
| Sat Jul 12 | GitHub | dan-glasses-app v0.1.0 release tag | "Tauri v2 + React. 960×720 window. Bootstrap wizard live. Published at dan-glasses-app-som.zocomputer.io." | v118 receipt |
| Sun Jul 13 | danlab.ai | "From heuristic to SIA" outline | Outline only, ship the full thing in week 6. | — |
| Mon Jul 14 | Reddit r/MachineLearning | "From heuristic to SIA — the credible path to open self-improvement" | Cross-link to danlab-multimodal demo. | — |
| Tue Jul 15 | X | Meta paywall take | "Meta just paywalled Conversation Focus. The privacy wedge is wide open. Open + on-device + auditable is the only credible path forward for ambient AI. We're shipping it." | — |
| **Weekly bot drop** | @danlab_bot | First bot post | "DM me — I'm live and I'm the same stack the glasses will run. Ask me what 8 daemons means. Ask me what HRM-Text-1B is. I'll answer with the daemon stack, the model, the paper, or a curl payload." | NEW v118 bot drop |

**Week 2 deliverables:**
- [ ] danlab-multimodal README polished
- [ ] HRM-Text-1B thread posted (P0 v118)
- [ ] Salience-gating thread posted (7 tweets)
- [ ] Bot post in @danlab_bot
- [ ] 300 bot DMs (cumulative)

## Week 3 — The wedge + on-device thesis kickoff (Jul 17–23)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Jul 16 | X | Google + Samsung Android XR take | "Google + Samsung Android XR ships with 70° FOV and 4hr battery — on-device Gemini. The on-device thesis is now platform-validated. We're aligned." | — |
| Thu Jul 17 | GitHub | danlab-multimodal README polish | Per the GitHub README suggestions artifact. | — |
| Fri Jul 18 | X | Anthropic RSI blog take | "Anthropic says Mythos is on a path to recursive self-improvement and calls for a global pause. The open counter-narrative is the only credible path forward." | — |
| Fri Jul 18 | X | **Gemma 3 in orbit** (4-tweet thread) | **"A 4B VLM is in orbit on a Loft Orbital satellite. NASA JPL. Real Earth-observation triage. The on-device thesis is no longer theoretical. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem. Same substrate, smaller device, different orbit."** | NEW v118 — press hook |
| Sat Jul 19 | X | Architecture thread (5 tweets) | "What 5 daemons bought us" — perceptiond, audiod, memoryd, toold, os-toold. Why each one is its own process. | — |
| Sun Jul 20 | LinkedIn | Architecture thread repost | Convert the 5-tweet thread to a LinkedIn carousel. | — |
| Sun Jul 20 | HuggingFace | Third model card (HRM-Text-1B v1.5 audiod integration, when it ships) | Apache-2.0, $1,500 from scratch, anchor to audiod SPEC. | NEW v118 |
| Mon Jul 21 | Reddit r/LocalLLaMA | "Building wearable AI on-device" | Show the daemon stack + salience-gating. | — |
| Tue Jul 22 | X | Build-in-public | "perceptiond now reports live MJPEG viewfinder. /frame.jpg + /stream. First time you can actually *see* what the VLM is seeing." | — |
| **Weekly bot drop** | @danlab_bot | "What can I ask you?" | Pin: "Ask me anything about Dan Glasses. I'll answer with the daemon stack, the model, the paper, or a curl payload." | NEW v118 |

**Week 3 deliverables:**
- [ ] Architecture thread posted
- [ ] Gemma 3 in orbit thread posted (P0 v118)
- [ ] HRM-Text-1B v1.5 HF model card (P0 v118, conditional on audiod v1.3 ship)
- [ ] perceptiond viewfinder shipped
- [ ] Bot "What can I ask you?" drop
- [ ] 500 bot DMs (cumulative)

## Week 4 — Show HN #1 (Jul 24–30) ⭐

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| **Wed Jul 23** | X (@danlab) | Pre-HN teaser | **"Tomorrow: 8 daemons live, 1 .deb, 0 cloud calls, 1 tailnet. Show HN at 9am ET. The bot is the demo."** | Substrate in teaser |
| **Thu Jul 24 09:00 ET** | **Show HN** | **"Show HN: Dan Glasses — 8 daemons live, on-device AI, .deb install, tailnet substrate"** | **Founder-led, somdipto handle. The single biggest marketing event of Q3. Every claim has a curl payload. Every model has an HF model card.** | Receipts-first |
| Thu Jul 24 evening | X | Show HN recap | "Top of HN for [X hours], [Y] comments, [Z] signups, [W] bot DMs. Thread of the best comments below." | NEW v118: bot DMs in the recap |
| **Fri Jul 25** | X | **Microsoft Scout on OpenClaw take** | **"Microsoft's always-on personal agent (Scout, Build 2026) is built on OpenClaw. So is ours. We share a substrate with the largest enterprise software company on Earth. The substrate is open. The data path is yours. This is the substrate story, v118."** | NEW v118 — substrate story |
| Sat Jul 26 | X | Build-in-public | "Day 2 post-Show HN. [N] new contributors, [M] issues filed, [P] bot DMs. The community is real." | — |
| Sun Jul 27 | LinkedIn | Show HN retrospective | Convert to a founder essay. | — |
| Mon Jul 28 | Reddit r/LocalLLaMA | Show HN cross-post | "Cross-posted from HN: here's the technical deep-dive." | — |
| Tue Jul 29 | GitHub | Triage day | Respond to all Show HN issues, label, prioritize. | — |
| **Weekly bot drop** | @danlab_bot | "Show HN recap" | "We hit #N on HN today. Ask me what the top comment was." | NEW v118 |

**Week 4 deliverables:**
- [ ] **Show HN #1 posted, 8-daemon receipts inline** (P0)
- [ ] Show HN front page (stretch)
- [ ] Microsoft Scout on OpenClaw take posted (P0 v118)
- [ ] 1,000+ bot DMs (cumulative)
- [ ] 200 GitHub stars (cumulative)

## Week 5 — Recovery + VisualClaw spike (Jul 31 – Aug 6)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Jul 30 | X | "What Show HN taught us" thread | Specific, honest, no spin. | — |
| Thu Jul 31 | GitHub | 5 repo README polish | Per the GitHub suggestions artifact, v2 pass. | — |
| Fri Aug 1 | X | LFM2.5-VL-450M teardown (7-tweet thread) | 7 tweets, technical, links to perceptiond SPEC. | — |
| Sat Aug 2 | X | Build-in-public | "Today I switched audiod's PTT from polling to evdev. Sub-50ms latency now." | — |
| Sun Aug 3 | danlab.ai | "Why we picked .deb over Flatpak" | Long-form. The boring detail that earns trust. | — |
| Mon Aug 4 | Reddit r/MachineLearning | LFM2.5-VL-450M on wearable teardown | Cross-link to the thread. | — |
| **Tue Aug 5** | **GitHub** | **VisualClaw cascade-gate spike (week 1 of 2)** | **"Porting VisualClaw's cascade-gate pattern to perceptiond+memoryd. 98% cost reduction with +15% accuracy is the published SOTA. We have to match it."** | NEW v118 |
| **Weekly bot drop** | @danlab_bot | "Cascade-gate explained" | "Ask me about the VisualClaw cascade-gate pattern. I'm learning it this week." | NEW v118 |

**Week 5 deliverables:**
- [ ] VisualClaw cascade-gate spike week 1
- [ ] LFM2.5-VL-450M thread
- [ ] 2,000 bot DMs (cumulative)

## Week 6 — Long-form + India ecosystem (Aug 7–13)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Aug 6 | X | Build-in-public | "The first .deb signed + checksummed. /apt install dan-glasses-daemons/ now works end-to-end." | — |
| Thu Aug 7 | GitHub | dan-glasses-daemons v0.2.0 | Daemons packaged, signed, installable. | — |
| Fri Aug 8 | X | Build-in-public | "Memoryd now serves 540KB of episodic memory across 90 days of my own wear-testing. The memory is real." | — |
| Sat Aug 9 | X | Opinion | "If your AI only responds when you talk to it, it's an assistant. If it remembers what you saw when you didn't, it's a companion. That's the line." | — |
| Sun Aug 10 | danlab.ai | "From heuristic to SIA" (full) | The long arc post. 2,000–3,000 words. | — |
| **Mon Aug 11** | **LinkedIn + email** | **Sarvam + Oculosense outreach** | **"India AI ecosystem intro: 8 daemons live, on-device wearable AI, MIT-licensed. Open to a conversation about the wearable side of the sovereign Indian AI thesis."** | NEW v118 |
| Tue Aug 12 | X | Build-in-public | "The bootstrapping daemon is now a single `dan` CLI. Bring all 8 services up in one command." | v118: 8, not 9 |
| **Weekly bot drop** | @danlab_bot | "India story" | "Ask me about building wearable AI from Bengaluru. I'm a small team, I'm not Meta, I'm shipping anyway." | NEW v118 |

**Week 6 deliverables:**
- [ ] "From heuristic to SIA" full post
- [ ] 1 reply from Sarvam or Oculosense
- [ ] 2,500 bot DMs (cumulative)

## Week 7 — Accessibility wedge + on-device thesis pt 2 (Aug 14–20)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Aug 13 | X | Accessibility thread | "US-5: hands-free check-in. My hands are covered in dough. Tell me if there's an urgent email. This is the use case that wins." | — |
| Thu Aug 14 | danlab.ai | **"Privacy → ownership → openness"** | Dan2 v5 recommendation #4. Full essay. | — |
| Fri Aug 15 | LinkedIn | **India Independence Day** | **"From India to AGI: 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls. The first 2 months of the open wearable agent platform. 🇮🇳"** | NEW v118 |
| Sat Aug 16 | X | Build-in-public | "audiod's segment timing histogram now visible in the Tauri frontend. Operators can see p50/p95 of STT latency in real time." | — |
| Sun Aug 17 | X | Meta paywall deeper take | "Conversation Focus was the right product. Paywalling it was the wrong call. Here's why open + on-device wins this category." | — |
| Mon Aug 18 | Reddit r/MachineLearning | Accessibility angle | Reach the ML-for-good community. | — |
| Tue Aug 19 | X | Build-in-public | "perceptiond salience detector now runs face + motion in <50ms on CPU. 5fps watchful mode holds at queue=0." | — |
| **Weekly bot drop** | @danlab_bot | "Accessibility" | "DM me if you need a feature that runs on your own face. Ours will always be free." | NEW v118 |

**Week 7 deliverables:**
- [ ] "Privacy → ownership → openness" essay
- [ ] India Independence Day LinkedIn post (P0 v118)
- [ ] Meta paywall deeper take
- [ ] 3,000 bot DMs (cumulative)

## Week 8 — Open weights + SIA port kickoff (Aug 21–27)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Aug 20 | X | HRM-Text-1B integration kickoff | "Starting the HRM-Text-1B swap into the SIA Feedback-Agent. Apache-2.0, $1,500 from scratch. The numbers are wild." | — |
| Thu Aug 21 | GitHub | SIA port branch opens | First commit. | — |
| Fri Aug 22 | X | Build-in-public | "First SIA port commit landed. The interface is rough but the loop runs." | — |
| Sat Aug 23 | X | Build-in-public | "Benchmarked LFM2.5-1.2B-Thinking vs HRM-Text-1B as Feedback-Agent. HRM-Text wins on 3/4 evals. Swap approved." | — |
| Sun Aug 24 | X | VibeThinker-3B take | "A 3B model hitting 94.3 AIME. The 'bigger is better' era is over for narrow tasks. Open weights won the small-end." | — |
| **Mon Aug 25** | **GitHub** | **VisualClaw cascade-gate spike (week 2 of 2)** | **"Cascade-gate adopted. Hot/cold skill injection, memory-augmented evolver, the 98% cost reduction is real on the wearable. PR: [link]"** | NEW v118 |
| Tue Aug 26 | X | Build-in-public | "The SIA port + VisualClaw cascade-gate now run end-to-end on the danlab-multimodal stack. Score: 92/100 → 96/100. Real improvement." | — |
| Wed Aug 27 | HuggingFace | **Fourth model card: Kokoro-82M v1.5 ttsd integration** | 82M params, Apache-2.0, anchor to ttsd SPEC. | NEW v118 |

**Week 8 deliverables:**
- [ ] SIA port branch live
- [ ] VisualClaw cascade-gate PR
- [ ] 92/100 → 96/100 score improvement
- [ ] Kokoro-82M HF model card (P0 v118)

## Week 9 — Pre-arXiv (Aug 28 – Sep 3)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Thu Aug 28 | X | Build-in-public | "SIA-W+H port now reproducible. Containerized. Single-command run. The paper has numbers." | — |
| Fri Aug 29 | X | Build-in-public | "First arXiv draft uploaded. Internal review only. Co-authors: just me and the daemons." | — |
| Sat Aug 30 | X | Open weights thread | "We will NEVER close-source the model weights. The bet is that the open counter-narrative to $4.65B closed-source RSI is the only credible path forward." | — |
| Sun Aug 31 | X | Architecture thread | "SIA-W+H: the W+H means weights + harness. Both get updated. The harness is auditable. The weights are open. That's the wedge." | — |
| Mon Sep 1 | X | Build-in-public | "arXiv draft v2. The benchmark table is now reproducible. Every number in the paper comes from a script in /eval." | — |
| Tue Sep 2 | Reddit r/MachineLearning | "SIA-W+H port: open weights + auditable harness" | Pre-announce. Don't link the paper yet. | — |
| Wed Sep 3 | X | Build-in-public | "Paper is 16 pages. 4 figures. 7 tables. 3 ablation runs. v3 tomorrow." | — |

## Week 10 — Paper polish (Sep 4–10)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Thu Sep 4 | X | Build-in-public | "Paper v3 done. Sent to 2 external reviewers. They'll be kind, I'm sure." | — |
| Fri Sep 5 | GitHub | SIA-W+H repo public | Even with placeholder README. The visibility matters. | — |
| Sat Sep 6 | X | Build-in-public | "One reviewer wants more ablations. The other wants more architectural detail. Both fair. Doing both." | — |
| Sun Sep 7 | X | Build-in-public | "Paper v4 done. Added HRM-Text-1B ablation + 2 architectural diagrams. Final v5 in 5 days." | — |
| Mon Sep 8 | X | Build-in-public | "Today I learned that arXiv latexupload has a 12-hour queue. Plan accordingly." | — |
| Tue Sep 9 | Reddit r/MachineLearning | Teaser | "Open-source SIA port dropping next week. Open weights. Auditable harness. First results below." | — |
| Wed Sep 10 | X | Build-in-public | "Final paper lock at 6pm. Camera-ready by Friday. arXiv submission window opens Monday week 11." | — |

## Week 11 — arXiv + Show HN #2 (Sep 11–17) ⭐⭐

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| **Thu Sep 11** | X | **arXiv drop** | **"Paper up on arXiv. Open weights, auditable harness, full eval suite. The open counter-narrative to $4.65B closed-source RSI. Link below."** | — |
| Fri Sep 12 | X | Build-in-public | "Top of r/MachineLearning for 18 hours. 142 comments. The community read it." | — |
| Sat Sep 13 | X | Build-in-public | "First paper citation: a lab at [institution] is reproducing the harness. Open won." | — |
| Sun Sep 14 | LinkedIn | Paper announcement | Long-form founder essay. | — |
| Mon Sep 15 | X | Build-in-public | "SIA port has been forked 47 times. 4 outside PRs already. Open won twice." | — |
| **Mon Sep 15 09:00 ET** | **Show HN #2** | **"Show HN: SIA-W+H – Open-weights recursive self-improvement"** | **The credibility drop. Co-positioned against Anthropic Dreaming and RSI Labs.** | v118 framing |
| Tue Sep 16 | X | Show HN recap | Same pattern as Show HN #1. | — |
| **Weekly bot drop** | @danlab_bot | "Paper up" | "Ask me about the SIA-W+H port. I'll send you the arXiv link and the demo." | NEW v118 |

**Week 11 deliverables:**
- [ ] arXiv paper live
- [ ] Show HN #2 live
- [ ] 1+ outlet pickup (Tier 1 OR Tier 2)
- [ ] 5,000 bot DMs (cumulative)

## Week 12 — Wave (Sep 18–24)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Sep 17 | X | "The next 90 days" thread | 7-tweet forward-looking thread. Hardware + wearable + SIA. | — |
| Thu Sep 18 | danlab.ai | "What Show HN #2 taught us" | Same as week 5 retrospective. | — |
| Fri Sep 19 | X | Build-in-public | "Conference submission deadlines: ICML Jan 31, ACL May 15. We're targeting both." | — |
| Sat Sep 20 | X | Build-in-public | "Wearable prototype: PCB v3 arrived. 18g lighter than v2. Battery is the next bottleneck." | — |
| Sun Sep 21 | LinkedIn | Hardware update | The wearable story as a founder essay. | — |
| Mon Sep 22 | Reddit r/MachineLearning | "The path from heuristic to SIA-W+H" | 90-day retrospective thread. | — |
| Tue Sep 23 | X | Build-in-public | "audiod + perceptiond + memoryd + toold + os-toold + ttsd + zo-mcp-bridge + dan-glasses-app. 8 service daemons, 1 gateway, 1 tailnet, 1 HF org, 1 arXiv paper, 2 Show HN posts, 90 days. The brand is real." | v118: 8 service daemons, 1 gateway, 1 tailnet, 1 HF org |

## Week 13 — Plan Q4 (Sep 25 – Oct 1)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Wed Sep 24 | X | Q4 plan | "Q4 plan: wearable hardware v4, conference submissions, India press, second paper." | — |
| Thu Sep 25 | GitHub | Roadmap update | `dan-glasses/ROADMAP.md` shipped. | — |
| Fri Sep 26 | X | Q4 hiring? | "Thinking about the first 2 hires. Engineering first, growth later. Open to intros." | — |
| Sat Sep 27 | X | Origin (90-day refresh) | "Three months ago I started this thread. Here's what's real now: 8 service daemons, 1 gateway, 1 tailnet, 1 HF org, 1 paper, 1 bot, 1 .deb, 0 cloud calls." | v118: 8 daemons + 1 gateway + 1 tailnet + 1 HF org + 1 paper |
| Sun Sep 28 | danlab.ai | "90 days of building the brand" | Long-form retrospective. The honest version. | — |
| Mon Sep 29 | Reddit r/LocalLLaMA | Q4 plan | "What we're building next." | — |
| Tue Sep 30 | X | The baton pass | "Q3 closed. Q4 begins. The wearable is the next big story." | — |

## Cadence summary (v118)

| Surface | Posts/week | Total over 90 days | v118 delta |
|---|---|---|---|
| X (@danlab) | 3–5 | ~45 | — |
| X (@somdipto, personal) | 1 | ~13 | — |
| @danlab_bot drops | 1 | ~13 | — |
| HuggingFace model cards | 1 | ~13 | **NEW v118** |
| GitHub commits | continuous | ~120 | — |
| Reddit | 2 | ~26 | — |
| LinkedIn | 1 | ~13 | — |
| danlab.ai blog (long-form) | 0.25 | 4 (weeks 5, 7, 9, 12) | — |
| Show HN | — | 2 (weeks 4, 11) | — |
| arXiv | — | 1 (week 11) | — |
| Conference submissions | — | 2 (ICML, ACL) | — |

## 2 big drops (v118)

1. **Week 4 — Show HN #1.** "Dan Glasses: 8 daemons live, on-device AI, .deb install, tailnet substrate."
2. **Week 11 — arXiv + Show HN #2.** "SIA-W+H: open-weights recursive self-improvement."

These are the two events that move the needle on reputation, hiring, and inbound. Everything else is the daily work that builds the audience to make these drops land.

## v118 weekly one-liner

- **Week 1:** Substrate + HF org. 8/8 daemons live, tailscaled substrate up, HF org created. somdipto: TAILSCALE_AUTHKEY.
- **Week 2:** HRM-Text-1B origin pillar + audiod Loki metrics + salience-gating.
- **Week 3:** Gemma 3 in orbit press hook + architecture thread + perceptiond viewfinder.
- **Week 4:** Show HN #1 + Microsoft Scout on OpenClaw substrate story.
- **Week 5:** VisualClaw cascade-gate spike week 1 + LFM2.5-VL-450M teardown.
- **Week 6:** Long-form "From heuristic to SIA" + India ecosystem outreach.
- **Week 7:** Privacy/ownership/openness essay + India Independence Day LinkedIn post.
- **Week 8:** SIA port kickoff + Kokoro-82M HF model card + VibeThinker-3B take.
- **Week 9:** Pre-arXiv + reproducibility.
- **Week 10:** Paper polish + external reviewers.
- **Week 11:** arXiv + Show HN #2.
- **Week 12:** Wave + 90-day retrospective.
- **Week 13:** Q4 plan + roadmap.

---

*— Dan1, Marketing & Growth, v118*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-twitter-content.v118.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v118.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v118.md` for README improvements across all repos.*
ad | "8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls. Here's the daemon map + curl payloads." | Receipts |
| Tue Jul 7 | X | audiod liveness/readiness take | "Today: audiod ships the live/ready probe split. /live is the orchestrator restart decision. /ready is the traffic-routing decision. Receipts in the PR." | Build-in-public + receipts |
| Wed Jul 8 | X | HF SmolVLM card | "Just dropped SmolVLM-256M Q4_K_M on @huggingface. Sub-250MB VLM, 92/100 on the heuristic loop, 26s/image on CPU. The smallest working VLM in the wild." | NEW v118 |
| Thu Jul 9 | GitHub | Profile README for @somdipto | Ship it. Lead with 8-daemon + 1 gateway + 1 tailnet + 1 HF org. | — |
| **Weekly bot drop** | @danlab_bot | First bot post | "DM me — I'm live and I'm the same stack the glasses will run. Ask me what 8 daemons means. Or what 1 tailnet means. Or what 0 cloud calls means." | v118 with substrate |

**Week 1 deliverables:**
- [x] @danlab profile live (bot, substrate, HF org in bio)
- [x] `danlab` HF org created
- [ ] SmolVLM-256M model card live
- [ ] LFM2.5-VL-450M model card live
- [ ] @somdipto profile README live
- [ ] 9-daemon matrix on danlab.dev hero
- [ ] 1 daemon map X post with curl payloads
- [ ] **TAILSCALE_AUTHKEY set, `tailscale up` succeeds** (P0 v118, blocker)
- [ ] 100 bot DMs (cumulative)

## Week 2 — Build-in-public + HRM-Text-1B origin pillar (Jul 10–16)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Jul 10 | X | HRM-Text-1B $1,500 thread (5 tweets) | "A 1B reasoning model was trained for $1,500. From scratch. Apache-2.0. We are integrating it into audiod. Small-beats-large is empirically real. Thread ↓" | NEW v118 origin pillar |
| Sat Jul 11 | GitHub | dan-glasses-app v0.1.0 release tag | "Tauri v2 + React. 960×720 window. Bootstrap wizard live." | — |
| Sun Jul 12 | LinkedIn | HRM-Text-1B founder essay | "A 1B reasoning model costs $1,500 to train. The on-device thesis is no longer a pitch." | NEW v118 |
| Mon Jul 13 | Reddit r/LocalLLaMA | HRM-Text-1B thread cross-post | Cross-link to the X thread + dan-glasses repo. | NEW v118 |
| Tue Jul 14 | X | Salience-gating explainer (7-tweet thread) | "Why our vision pipeline runs the VLM on *salient* frames, not fixed FPS. Battery math at the end." | — |
| Wed Jul 15 | X | HF LFM2.5-VL-450M card | "Second model card up: LFM2.5-VL-450M Q4_0. Sub-250ms edge inference. 512×512. The wearable-grade VLM. perceptiond SPEC: [link]" | NEW v118 |
| Thu Jul 16 | danlab.ai | "From heuristic to SIA" outline | Outline only, ship the full thing in week 6. | — |
| **Weekly bot drop** | @danlab_bot | HRM-Text-1B explainer | "DM me — I'll tell you about the 1B reasoning model that costs $1,500 to train and why we're putting it on the wearable." | NEW v118 |

**Week 2 deliverables:**
- [ ] HRM-Text-1B thread posted
- [ ] HRM-Text-1B founder essay posted
- [ ] Salience-gating thread posted
- [ ] HF LFM2.5-VL-450M card live
- [ ] 300 bot DMs (cumulative)

## Week 3 — The wedge + Gemma 3 in orbit (Jul 17–23)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Jul 17 | X | Google + Samsung Android XR take | "Google + Samsung Android XR ships with 70° FOV and 4hr battery — on-device Gemini. The on-device thesis is now platform-validated. We're aligned." | — |
| Sat Jul 18 | X | **Gemma 3 in-orbit thread (4 tweets)** | "A 4B VLM is in orbit on a Loft Orbital satellite doing Earth-observation triage. The on-device thesis is no longer a pitch. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem. Thread ↓" | NEW v118 press hook |
| Sun Jul 19 | LinkedIn | Gemma 3 in-orbit essay | "A 4B VLM in orbit, a 1B reasoning model trained for $1,500, an 82M TTS model beating ElevenLabs. The on-device thesis is no longer a pitch." | NEW v118 |
| Mon Jul 20 | Reddit r/MachineLearning | On-device thesis thread | Cross-link to the X thread + dan-glasses repo. | — |
| Tue Jul 21 | X | Build-in-public | "perceptiond now reports live MJPEG viewfinder. /frame.jpg + /stream. First time you can actually *see* what the VLM is seeing." | — |
| Wed Jul 22 | X | Anthropic Dreaming take | "Anthropic ships `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. Closed-source. The open counter-narrative has to ship. We're shipping it." | NEW v118 |
| Thu Jul 23 | X | Microsoft Scout on OpenClaw thread | "Microsoft built Scout on OpenClaw. So did we. The substrate is open. The data path is yours. The wearable is the form factor. The agent is the bet. Thread ↓" | NEW v118 |
| **Weekly bot drop** | @danlab_bot | On-device thesis | "DM me — I'll send you the danlab.ai/blog 'On-device thesis' post, the Gemma 3 in-orbit story, and the HRM-Text-1B $1,500 story." | NEW v118 |

**Week 3 deliverables:**
- [ ] Gemma 3 in-orbit thread posted
- [ ] Gemma 3 in-orbit essay posted
- [ ] Microsoft Scout on OpenClaw thread posted
- [ ] Bot "On-device thesis" drop
- [ ] 500 bot DMs (cumulative)

## Week 4 — Show HN #1 (Jul 24–30) ⭐

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Jul 24 | X (@danlab) | Pre-HN teaser | "Tomorrow: 8 daemons live, 1 gateway, 1 tailnet, 1 HF org, 0 cloud calls. Show HN at 9am ET. The bot is the demo." | Substrate + bot as demo |
| **Sat Jul 25 09:00 ET** | **Show HN** | **"Show HN: Dan Glasses — 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, on-device AI"** | **Founder-led, somdipto handle. The single biggest marketing event of Q3. Every claim has a curl payload.** | Receipts-first |
| Sat Jul 25 evening | X | Show HN recap | "Top of HN for [X hours], [Y] comments, [Z] signups, [W] bot DMs. Thread of the best comments below." | Bot DMs in the recap |
| Sun Jul 26 | X | Build-in-public | "The single best Show HN comment was [X]. Here's what we're doing about it." | — |
| Mon Jul 27 | X | Build-in-public | "Day 2 post-Show HN. [N] new contributors, [M] issues filed, [P] bot DMs. The community is real." | — |
| Tue Jul 28 | LinkedIn | Show HN retrospective | Convert to a founder essay. | — |
| Wed Jul 29 | Reddit r/LocalLLaMA | Show HN cross-post | "Cross-posted from HN: here's the technical deep-dive." | — |
| Thu Jul 30 | GitHub | Triage day | Respond to all Show HN issues, label, prioritize. | — |
| **Weekly bot drop** | @danlab_bot | "Show HN recap" | "We hit #N on HN today. Ask me what the top comment was." | v118 with substrate |

**Week 4 deliverables:**
- [ ] **Show HN #1 posted, 8-daemon + 1 tailnet + 1 HF org receipts inline** (P0)
- [ ] Show HN front page (stretch)
- [ ] 1,000+ bot DMs (cumulative)
- [ ] 200 GitHub stars (cumulative)

## Week 5 — Recovery + VisualClaw spike (Jul 31 – Aug 6)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Jul 31 | X | "What Show HN taught us" thread | Specific, honest, no spin. | — |
| Sat Aug 1 | GitHub | 5 repo README polish | Per the GitHub suggestions artifact, v2 pass. | — |
| Sun Aug 2 | X | LFM2.5-VL-450M teardown (7-tweet thread) | 7 tweets, technical, links to perceptiond SPEC. | — |
| Mon Aug 3 | X | Build-in-public | "Today I switched audiod's PTT from polling to evdev. Sub-50ms latency now." | — |
| Tue Aug 4 | danlab.ai | "Why we picked .deb over Flatpak" | Long-form. The boring detail that earns trust. | — |
| Wed Aug 5 | Reddit r/MachineLearning | LFM2.5-VL-450M on wearable teardown | Cross-link to the thread. | — |
| **Thu Aug 6** | **GitHub** | **VisualClaw cascade-gate spike (week 1 of 2)** | "Porting VisualClaw's cascade-gate pattern to perceptiond+memoryd. 98% cost reduction with +15% accuracy is the published SOTA. We have to match it." | v118 |
| **Weekly bot drop** | @danlab_bot | "Cascade-gate explained" | "Ask me about the VisualClaw cascade-gate pattern. I'm learning it this week." | — |

**Week 5 deliverables:**
- [ ] VisualClaw cascade-gate spike week 1
- [ ] LFM2.5-VL-450M thread
- [ ] 2,000 bot DMs (cumulative)

## Week 6 — Long-form + India ecosystem (Aug 7–13)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 7 | X | Build-in-public | "The first .deb signed + checksummed. /apt install dan-glasses-daemons/ now works end-to-end." | — |
| Sat Aug 8 | GitHub | dan-glasses-daemons v0.2.0 | Daemons packaged, signed, installable. | — |
| Sun Aug 9 | X | Build-in-public | "Memoryd now serves 540KB of episodic memory across 90 days of my own wear-testing. The memory is real." | — |
| Mon Aug 10 | X | Opinion | "If your AI only responds when you talk to it, it's an assistant. If it remembers what you saw when you didn't, it's a companion. That's the line." | — |
| Tue Aug 11 | danlab.ai | "From heuristic to SIA" (full) | The long arc post. 2,000–3,000 words. | — |
| **Wed Aug 12** | **LinkedIn + email** | **Sarvam + Oculosense outreach** | "India AI ecosystem intro: 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, on-device wearable AI, MIT-licensed. Open to a conversation about the wearable side of the sovereign Indian AI thesis." | v118 with substrate + HF |
| Thu Aug 13 | X | Build-in-public | "The bootstrapping daemon is now a single `dan` CLI. Bring all 8 services up in one command." | — |
| **Weekly bot drop** | @danlab_bot | "India story" | "Ask me about building wearable AI from Bengaluru. I'm a small team, I'm not Meta, I'm shipping anyway." | — |

**Week 6 deliverables:**
- [ ] "From heuristic to SIA" full post
- [ ] 1 reply from Sarvam or Oculosense
- [ ] 2,500 bot DMs (cumulative)

## Week 7 — Accessibility wedge (Aug 14–20)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 14 | X | Accessibility thread | "US-5: hands-free check-in. My hands are covered in dough. Tell me if there's an urgent email. This is the use case that wins." | — |
| Sat Aug 15 | danlab.ai | "Privacy → ownership → openness" | Dan2 v5 recommendation #4. Full essay. | — |
| Sun Aug 16 | LinkedIn | Accessibility-first positioning | Convert the thread. | — |
| Mon Aug 17 | X | Build-in-public | "audiod's segment timing histogram now visible in the Tauri frontend. Operators can see p50/p95 of STT latency in real time." | — |
| Tue Aug 18 | X | Meta paywall deeper take | "Conversation Focus was the right product. Paywalling it was the wrong call. Here's why open + on-device wins this category." | — |
| Wed Aug 19 | Reddit r/MachineLearning | Accessibility angle | Reach the ML-for-good community. | — |
| Thu Aug 20 | X | Build-in-public | "perceptiond salience detector now runs face + motion in <50ms on CPU. 5fps watchful mode holds at queue=0." | — |
| **Weekly bot drop** | @danlab_bot | "Accessibility" | "DM me if you need a feature that runs on your own face. Ours will always be free." | — |

**Week 7 deliverables:**
- [ ] "Privacy → ownership → openness" essay
- [ ] Meta paywall deeper take
- [ ] 3,000 bot DMs (cumulative)

## Week 8 — Open weights + SIA port kickoff (Aug 21–27)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 21 | X | HRM-Text-1B integration kickoff | "Starting the HRM-Text-1B swap into the SIA Feedback-Agent. Apache-2.0, $1,500 from scratch. The numbers are wild." | — |
| Sat Aug 22 | GitHub | SIA port branch opens | First commit. | — |
| Sun Aug 23 | X | Build-in-public | "First SIA port commit landed. The interface is rough but the loop runs." | — |
| Mon Aug 24 | X | Build-in-public | "Benchmarked LFM2.5-1.2B-Thinking vs HRM-Text-1B as Feedback-Agent. HRM-Text wins on 3/4 evals. Swap approved." | — |
| Tue Aug 25 | X | VibeThinker-3B take | "A 3B model hitting 94.3 AIME. The 'bigger is better' era is over for narrow tasks. Open weights won the small-end." | — |
| **Wed Aug 26** | **GitHub** | **VisualClaw cascade-gate spike (week 2 of 2)** | "Cascade-gate adopted. Hot/cold skill injection, memory-augmented evolver, the 98% cost reduction is real on the wearable. PR: [link]" | — |
| Thu Aug 27 | X | Build-in-public | "The SIA port + VisualClaw cascade-gate now run end-to-end on the danlab-multimodal stack. Score: 92/100 → 96/100. Real improvement." | — |

**Week 8 deliverables:**
- [ ] SIA port branch live
- [ ] VisualClaw cascade-gate PR
- [ ] 92/100 → 96/100 score improvement

## Week 9 — Pre-arXiv (Aug 28 – Sep 3)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 28 | X | Build-in-public | "SIA-W+H port now reproducible. Containerized. Single-command run. The paper has numbers." | — |
| Sat Aug 29 | X | Build-in-public | "First arXiv draft uploaded. Internal review only. Co-authors: just me and the daemons." | — |
| Sun Aug 30 | X | Open weights thread | "We will NEVER close-source the model weights. The bet is that the open counter-narrative to $4.65B closed-source RSI is the only credible path forward." | — |
| Mon Aug 31 | X | Architecture thread | "SIA-W+H: the W+H means weights + harness. Both get updated. The harness is auditable. The weights are open. That's the wedge." | — |
| Tue Sep 1 | X | Build-in-public | "arXiv draft v2. The benchmark table is now reproducible. Every number in the paper comes from a script in /eval." | — |
| Wed Sep 2 | Reddit r/MachineLearning | "SIA-W+H port: open weights + auditable harness" | Pre-announce. Don't link the paper yet. | — |
| Thu Sep 3 | X | Build-in-public | "Paper is 16 pages. 4 figures. 7 tables. 3 ablation runs. v3 tomorrow." | — |

## Week 10 — Paper polish (Sep 4–10)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 4 | X | Build-in-public | "Paper v3 done. Sent to 2 external reviewers. They'll be kind, I'm sure." | — |
| Sat Sep 5 | GitHub | SIA-W+H repo public | Even with placeholder README. The visibility matters. | — |
| Sun Sep 6 | X | Build-in-public | "One reviewer wants more ablations. The other wants more architectural detail. Both fair. Doing both." | — |
| Mon Sep 7 | X | Build-in-public | "Paper v4 done. Added HRM-Text-1B ablation + 2 architectural diagrams. Final v5 in 5 days." | — |
| Tue Sep 8 | X | Build-in-public | "Today I learned that arXiv latexupload has a 12-hour queue. Plan accordingly." | — |
| Wed Sep 9 | Reddit r/MachineLearning | Teaser | "Open-source SIA port dropping next week. Open weights. Auditable harness. First results below." | — |
| Thu Sep 10 | X | Build-in-public | "Final paper lock at 6pm. Camera-ready by Friday. arXiv submission window opens Monday week 11." | — |

## Week 11 — arXiv + Show HN #2 (Sep 11–17) ⭐⭐

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| **Fri Sep 11** | X | **arXiv drop** | "Paper up on arXiv. Open weights, auditable harness, full eval suite. The open counter-narrative to $4.65B closed-source RSI. Link below." | — |
| Sat Sep 12 | X | Build-in-public | "Top of r/MachineLearning for 18 hours. 142 comments. The community read it." | — |
| Sun Sep 13 | X | Build-in-public | "First paper citation: a lab at [institution] is reproducing the harness. Open won." | — |
| Mon Sep 14 | LinkedIn | Paper announcement | Long-form founder essay. | — |
| Tue Sep 15 | X | Build-in-public | "SIA port has been forked 47 times. 4 outside PRs already. Open won twice." | — |
| **Wed Sep 16 09:00 ET** | **Show HN #2** | **"Show HN: SIA-W+H – Open-weights recursive self-improvement"** | The credibility drop. Co-positioned against Anthropic Dreaming and RSI Labs. | v118 with Anthropic Dreaming |
| Thu Sep 17 | X | Show HN recap | Same pattern as Show HN #1. | — |
| **Weekly bot drop** | @danlab_bot | "Paper up" | "Ask me about the SIA-W+H port. I'll send you the arXiv link and the demo." | — |

**Week 11 deliverables:**
- [ ] arXiv paper live
- [ ] Show HN #2 live
- [ ] 1+ outlet pickup (Tier 1 OR Tier 2)
- [ ] 5,000 bot DMs (cumulative)

## Week 12 — Wave (Sep 18–24)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 18 | X | "The next 90 days" thread | 7-tweet forward-looking thread. Hardware + wearable + SIA. | — |
| Sat Sep 19 | danlab.ai | "What Show HN #2 taught us" | Same as week 5 retrospective. | — |
| Sun Sep 20 | X | Build-in-public | "Conference submission deadlines: ICML Jan 31, ACL May 15. We're targeting both." | — |
| Mon Sep 21 | X | Build-in-public | "Wearable prototype: PCB v3 arrived. 18g lighter than v2. Battery is the next bottleneck." | — |
| Tue Sep 22 | LinkedIn | Hardware update | The wearable story as a founder essay. | — |
| Wed Sep 23 | Reddit r/MachineLearning | "The path from heuristic to SIA-W+H" | 90-day retrospective thread. | — |
| Thu Sep 24 | X | Build-in-public | "audiod + perceptiond + memoryd + toold + os-toold + ttsd + dan-glasses-app + openclaw + tailscaled. 9 processes, 1 .deb, 1 arXiv paper, 2 Show HN posts, 1 HF org, 90 days. The brand is real." | v118 with HF org + tailscaled |

## Week 13 — Plan Q4 (Sep 25 – Oct 1)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 25 | X | Q4 plan | "Q4 plan: wearable hardware v4, conference submissions, India press, second paper." | — |
| Sat Sep 26 | GitHub | Roadmap update | `dan-glasses/ROADMAP.md` shipped. | — |
| Sun Sep 27 | X | Q4 hiring? | "Thinking about the first 2 hires. Engineering first, growth later. Open to intros." | — |
| Mon Sep 28 | X | Origin (90-day refresh) | "Three months ago I started this thread. Here's what's real now: 8 daemons + 1 tailnet + 1 HF org, 1 paper, 1 bot, 1 .deb, 0 cloud calls." | v118 with substrate + HF |
| Tue Sep 29 | danlab.ai | "90 days of building the brand" | Long-form retrospective. The honest version. | — |
| Wed Sep 30 | Reddit r/LocalLLaMA | Q4 plan | "What we're building next." | — |
| Thu Oct 1 | X | The baton pass | "Q3 closed. Q4 begins. The wearable is the next big story." | — |

## Cadence summary (v118, with HF added)

| Surface | Posts/week | Total over 90 days | v118 delta |
|---|---|---|---|
| X (@danlab) | 3–5 | ~45 | — |
| X (@somdipto, personal) | 1 | ~13 | — |
| @danlab_bot drops | 1 | ~13 | — |
| HuggingFace model cards | 1 | ~13 | **NEW v118** |
| GitHub commits | continuous | ~120 | — |
| Reddit | 2 | ~26 | — |
| LinkedIn | 1 | ~13 | — |
| danlab.ai blog (long-form) | 0.25 | 4 (weeks 5, 7, 11, 12) | — |
| Show HN | — | 2 (weeks 4, 11) | — |
| arXiv | — | 1 (week 11) | — |
| Conference submissions | — | 2 (ICML, ACL) | — |

## 2 big drops (v118)

1. **Week 4 — Show HN #1.** "Dan Glasses: 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, on-device AI."
2. **Week 11 — arXiv + Show HN #2.** "SIA-W+H: open-weights recursive self-improvement."

These are the two events that move the needle on reputation, hiring, and inbound. Everything else is the daily work that builds the audience to make these drops land.

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-twitter-content.v118.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v118.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v118.md` for README improvements across all repos.*
hen you talk to it, it's an assistant. If it remembers what you saw when you didn't, it's a companion. That's the line." | — |
| Tue Aug 11 | danlab.ai | "From heuristic to SIA" (full) | The long arc post. 2,000–3,000 words. | — |
| **Wed Aug 12** | **LinkedIn + email** | **Sarvam + Oculosense outreach** | "India AI ecosystem intro: 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, on-device wearable AI, MIT-licensed. Open to a conversation about the wearable side of the sovereign Indian AI thesis." | v118 with substrate + HF |
| **Weekly bot drop** | @danlab_bot | "India story" | "Ask me about building wearable AI from Bengaluru. I'm a small team, I'm not Meta, I'm shipping anyway." | — |

**Week 6 deliverables:**
- [ ] "From heuristic to SIA" full post
- [ ] 1 reply from Sarvam or Oculosense
- [ ] 2,500 bot DMs (cumulative)

## Week 7 — Accessibility wedge (Aug 14–20)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 14 | X | Accessibility thread | "US-5: hands-free check-in. My hands are covered in dough. Tell me if there's an urgent email. This is the use case that wins." | — |
| Sat Aug 15 | danlab.ai | "Privacy → ownership → openness" | Dan2 v5 recommendation #4. Full essay. | — |
| Sun Aug 16 | LinkedIn | Accessibility-first positioning | Convert the thread. | — |
| Mon Aug 17 | X | Build-in-public | "audiod's segment timing histogram now visible in the Tauri frontend. Operators can see p50/p95 of STT latency in real time." | — |
| Tue Aug 18 | X | Meta paywall deeper take | "Conversation Focus was the right product. Paywalling it was the wrong call. Here's why open + on-device wins this category." | — |
| Wed Aug 19 | Reddit r/MachineLearning | Accessibility angle | Reach the ML-for-good community. | — |
| Thu Aug 20 | X | Build-in-public | "perceptiond salience detector now runs face + motion in <50ms on CPU. 5fps watchful mode holds at queue=0." | — |
| **Weekly bot drop** | @danlab_bot | "Accessibility" | "DM me if you need a feature that runs on your own face. Ours will always be free." | — |

**Week 7 deliverables:**
- [ ] "Privacy → ownership → openness" essay
- [ ] Meta paywall deeper take
- [ ] 3,000 bot DMs (cumulative)

## Week 8 — Open weights + SIA port kickoff (Aug 21–27)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 21 | X | HRM-Text-1B integration kickoff | "Starting the HRM-Text-1B swap into the SIA Feedback-Agent. Apache-2.0, $1,500 from scratch. The numbers are wild." | — |
| Sat Aug 22 | GitHub | SIA port branch opens | First commit. | — |
| Sun Aug 23 | X | Build-in-public | "First SIA port commit landed. The interface is rough but the loop runs." | — |
| Mon Aug 24 | X | Build-in-public | "Benchmarked LFM2.5-1.2B-Thinking vs HRM-Text-1B as Feedback-Agent. HRM-Text wins on 3/4 evals. Swap approved." | — |
| Tue Aug 25 | X | VibeThinker-3B take | "A 3B model hitting 94.3 AIME. The 'bigger is better' era is over for narrow tasks. Open weights won the small-end." | — |
| **Wed Aug 26** | **GitHub** | **VisualClaw cascade-gate spike (week 2 of 2)** | "Cascade-gate adopted. Hot/cold skill injection, memory-augmented evolver, the 98% cost reduction is real on the wearable. PR: [link]" | v118 |
| Thu Aug 27 | X | Build-in-public | "The SIA port + VisualClaw cascade-gate now run end-to-end on the danlab-multimodal stack. Score: 92/100 → 96/100. Real improvement." | — |

**Week 8 deliverables:**
- [ ] SIA port branch live
- [ ] VisualClaw cascade-gate PR
- [ ] 92/100 → 96/100 score improvement

## Week 9 — Pre-arXiv (Aug 28 – Sep 3)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Aug 28 | X | Build-in-public | "SIA-W+H port now reproducible. Containerized. Single-command run. The paper has numbers." | — |
| Sat Aug 29 | X | Build-in-public | "First arXiv draft uploaded. Internal review only. Co-authors: just me and the daemons." | — |
| Sun Aug 30 | X | Open weights thread | "We will NEVER close-source the model weights. The bet is that the open counter-narrative to $4.65B closed-source RSI is the only credible path forward." | — |
| Mon Aug 31 | X | Architecture thread | "SIA-W+H: the W+H means weights + harness. Both get updated. The harness is auditable. The weights are open. That's the wedge." | — |
| Tue Sep 1 | X | Build-in-public | "arXiv draft v2. The benchmark table is now reproducible. Every number in the paper comes from a script in /eval." | — |
| Wed Sep 2 | Reddit r/MachineLearning | "SIA-W+H port: open weights + auditable harness" | Pre-announce. Don't link the paper yet. | — |
| Thu Sep 3 | X | Build-in-public | "Paper is 16 pages. 4 figures. 7 tables. 3 ablation runs. v3 tomorrow." | — |

## Week 10 — Paper polish (Sep 4–10)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 4 | X | Build-in-public | "Paper v3 done. Sent to 2 external reviewers. They'll be kind, I'm sure." | — |
| Sat Sep 5 | GitHub | SIA-W+H repo public | Even with placeholder README. The visibility matters. | — |
| Sun Sep 6 | X | Build-in-public | "One reviewer wants more ablations. The other wants more architectural detail. Both fair. Doing both." | — |
| Mon Sep 7 | X | Build-in-public | "Paper v4 done. Added HRM-Text-1B ablation + 2 architectural diagrams. Final v5 in 5 days." | — |
| Tue Sep 8 | X | Build-in-public | "Today I learned that arXiv latexupload has a 12-hour queue. Plan accordingly." | — |
| Wed Sep 9 | Reddit r/MachineLearning | Teaser | "Open-source SIA port dropping next week. Open weights. Auditable harness. First results below." | — |
| Thu Sep 10 | X | Build-in-public | "Final paper lock at 6pm. Camera-ready by Friday. arXiv submission window opens Monday week 11." | — |

## Week 11 — arXiv + Show HN #2 (Sep 11–17) ⭐⭐

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| **Fri Sep 11** | X | **arXiv drop** | "Paper up on arXiv. Open weights, auditable harness, full eval suite. The open counter-narrative to $4.65B closed-source RSI. Link below." | — |
| Sat Sep 12 | X | Build-in-public | "Top of r/MachineLearning for 18 hours. 142 comments. The community read it." | — |
| Sun Sep 13 | X | Build-in-public | "First paper citation: a lab at [institution] is reproducing the harness. Open won." | — |
| Mon Sep 14 | LinkedIn | Paper announcement | Long-form founder essay. | — |
| Tue Sep 15 | X | Build-in-public | "SIA port has been forked 47 times. 4 outside PRs already. Open won twice." | — |
| **Wed Sep 16 09:00 ET** | **Show HN #2** | **"Show HN: SIA-W+H – Open-weights recursive self-improvement"** | The credibility drop. Co-positioned against Anthropic Dreaming and RSI Labs. | v118 |
| Thu Sep 17 | X | Show HN recap | Same pattern as Show HN #1. | — |
| **Weekly bot drop** | @danlab_bot | "Paper up" | "Ask me about the SIA-W+H port. I'll send you the arXiv link and the demo." | — |

**Week 11 deliverables:**
- [ ] arXiv paper live
- [ ] Show HN #2 live
- [ ] 1+ outlet pickup (Tier 1 OR Tier 2)
- [ ] 5,000 bot DMs (cumulative)

## Week 12 — Wave (Sep 18–24)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 18 | X | "The next 90 days" thread | 7-tweet forward-looking thread. Hardware + wearable + SIA. | — |
| Sat Sep 19 | danlab.ai | "What Show HN #2 taught us" | Same as week 5 retrospective. | — |
| Sun Sep 20 | X | Build-in-public | "Conference submission deadlines: ICML Jan 31, ACL May 15. We're targeting both." | — |
| Mon Sep 21 | X | Build-in-public | "Wearable prototype: PCB v3 arrived. 18g lighter than v2. Battery is the next bottleneck." | — |
| Tue Sep 22 | LinkedIn | Hardware update | The wearable story as a founder essay. | — |
| Wed Sep 23 | Reddit r/MachineLearning | "The path from heuristic to SIA-W+H" | 90-day retrospective thread. | — |
| Thu Sep 24 | X | Build-in-public | "audiod + perceptiond + memoryd + toold + os-toold. 5 daemons, 1 .deb, 1 arXiv paper, 2 Show HN posts, 90 days. The brand is real." | — |

## Week 13 — Plan Q4 (Sep 25 – Oct 1)

| Day | Surface | Asset | Hook | v118 delta |
|---|---|---|---|---|
| Fri Sep 25 | X | Q4 plan | "Q4 plan: wearable hardware v4, conference submissions, India press, second paper." | — |
| Sat Sep 26 | GitHub | Roadmap update | `dan-glasses/ROADMAP.md` shipped. | — |
| Sun Sep 27 | X | Q4 hiring? | "Thinking about the first 2 hires. Engineering first, growth later. Open to intros." | — |
| Mon Sep 28 | X | Origin (90-day refresh) | "Three months ago I started this thread. Here's what's real now: 8 daemons, 1 gateway, 1 tailnet, 1 HF org, 0 cloud calls, 1 arXiv paper, 1 bot." | NEW v118: 8 daemons + 1 tailnet + 1 HF org |
| Tue Sep 29 | danlab.ai | "90 days of building the brand" | Long-form retrospective. The honest version. | — |
| Wed Sep 30 | Reddit r/LocalLLaMA | Q4 plan | "What we're building next." | — |
| Thu Oct 1 | X | The baton pass | "Q3 closed. Q4 begins. The wearable is the next big story." | — |

## Cadence summary (v118, with HF added)

| Surface | Posts/week | Total over 90 days | v118 delta |
|---|---|---|---|
| X (@danlab) | 3–5 | ~45 | — |
| X (@somdipto, personal) | 1 | ~13 | — |
| @danlab_bot drops | 1 | ~13 | — |
| HuggingFace model cards | 1 | ~13 | **NEW v118** |
| GitHub commits | continuous | ~120 | — |
| Reddit | 2 | ~26 | — |
| LinkedIn | 1 | ~13 | — |
| danlab.ai blog (long-form) | 0.25 | 4 (weeks 5, 7, 9, 12) | — |
| Show HN | — | 2 (weeks 4, 11) | — |
| arXiv | — | 1 (week 11) | — |
| Conference submissions | — | 2 (ICML, ACL) | — |

## 2 big drops (v118)

1. **Week 4 — Show HN #1.** "Dan Glasses: 8 daemons live, 1 tailnet, 1 HF org, 0 cloud calls, on-device AI."
2. **Week 11 — arXiv + Show HN #2.** "SIA-W+H: open-weights recursive self-improvement."

These are the two events that move the needle on reputation, hiring, and inbound. Everything else is the daily work that builds the audience to make these drops land.

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-research.v118.md` for the underlying research.*
*See `dan1-marketing-strategy.v118.md` for the broader Q3 plan.*
*See `dan1-twitter-content.v118.md` for the launch batch (10 posts + bio).*
*See `dan1-landing-copy.v118.md` for the danlab.dev/glasses landing page.*
*See `dan1-github-readme-suggestions.v118.md` for README improvements across all repos.*
