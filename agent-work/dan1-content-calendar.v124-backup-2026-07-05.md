# DanLab Content Calendar — v124
**Date:** 2026-07-05 (refresh of v123, same day, 09:30 UTC)
**Owner:** DAN-1
**Cadence:** 30-day rolling window. Refresh every Monday.
**Cross-ref:** [strategy](./dan1-marketing-strategy.md), [research](./dan1-marketing-research.md)
**v124 delta:** Foundation stream locked. Threat model public. Meta paywall anchor (v123). **v124 add: 3-region bifurcation anchor — Washington Post Trump/Anthropic conditional lift (Jul 1), Reuters/SCMP Alibaba/Claude Code ban (Jul 4), FourWeekMBA Palantir/Nemotron pivot (early Jul), BleepingComputer Fable 5 cap (Jul).** New hero CTA stack: paywall + sovereign-trust + reversibility. New v124 plan-O1/O2/O3 deliverables enter Week 2.

---

## 0. Operating principles (v124)

1. **No fluff.** Every post ships a code link, a metric, a screenshot, or a demo. No "excited to announce" without a payload.
2. **One idea per post.** Twitter thread counts as one. Blog post is one. YouTube demo is one.
3. **One CTA per post.** Default CTA = "DM @danlab_bot." Different CTAs are exceptions, not the rule.
4. **Owner + review.** Every artifact names one person who ships it and one who reviews.
5. **Tagging.** Every artifact lists: `#track-a` (Dan Glasses wearable), `#track-b` (Dan Voice app), `#research` (multimodal / SIA / HRM-Text), `#platform` (Paperclip / OpenClaw / dani), `#site` (danlab.dev), `#telegram` (@danlab_bot), `#security` (threat model / protocol), `#paywall` (Meta accessibility paywall), `#sovereign` (v124 NEW — 3-region bifurcation, political-conditionality).
6. **Real numbers only.** If a claim cannot be backed by a `/status` payload, a Git commit, or a published number, do not post it.
7. **Bot-first funnel.** Every post's CTA = DM `@danlab_bot`. The bot is the demo.
8. **The 3-region bifurcation is the v124 wedge.** Cite at least one of (WaPo, Reuters/SCMP, FourWeekMBA, BleepingComputer) in every Week 1–2 artifact. Combine with the v123 Meta paywall anchor in alternating posts.

---

## 1. The 30-day window (v124, weeks 1–4)

### Week 1 (Jul 6–12): "The week three regions said it out loud"

**Theme:** 3-region bifurcation. The closed-source frontier is no longer safe. We are the only wearable-grade lab that is none of the three.

| Day | Channel | Artifact | Tag | CTA | Owner | v124 source |
|---|---|---|---|---|---|---|
| Mon Jul 6 | X thread | "Alibaba banned Claude Code for an embedded backdoor. We didn't have to ban ourselves — the .deb was never on their server. Yours, not theirs. DM @danlab_bot." | #sovereign #paywall #telegram | DM bot | Dan1 | Reuters/SCMP |
| Tue Jul 7 | Substack | "Three regions, three signals: what the Alibaba ban, the Trump lift, and the Palantir pivot actually mean for enterprise AI procurement." | #sovereign #security | Subscribe | Dan1 | All 4 sources |
| Wed Jul 8 | X post | Screenshot of `@danlab_bot` daemon map + "8 services live, 0 cloud calls, 0 backdoor risk. DM @danlab_bot." | #telegram | DM bot | Dan1 | (bot) |
| Thu Jul 9 | LinkedIn | "The lab that was open-weights on the device from day one is the only one the three regions didn't have to call." Long-form. | #sovereign | Connect | somdipto | All 4 sources |
| Fri Jul 10 | X thread | "Anthropic Fable 5 was 'lifted' on July 1. It's still capped to 50% of weekly limits and rerouted to Opus 4.8 on safety-risk tasks. 'Lifted' ≠ 'unconditional.' Ours was never banned because ours was never on their server. DM @danlab_bot." | #sovereign | DM bot | Dan1 | BleepingComputer |
| Sat Jul 11 | YouTube/Loom | 2-min demo: `@danlab_bot` answering "what's running" with live daemon map. | #telegram | Watch + DM | Dan1 | (bot) |
| Sun Jul 12 | Substack | "The reversibility contract: why xAI's cofounder is right about RSI, and what we ship instead." (v124 plan-O2 preview) | #sovereign #security | Subscribe | Dan1 | Babushkin |

### Week 2 (Jul 13–19): "Sovereign trust, audited" — ship plan-O1 + plan-O2

**Theme:** Ship the sovereign-trust audit + reversibility contract. Open-source the receipt for the 3-region wedge.

| Day | Channel | Artifact | Tag | CTA | Owner | v124 source |
|---|---|---|---|---|---|---|
| Mon Jul 13 | GitHub | Merge plan-O1 sovereign-trust audit. 1-day spike ships. PR + `dan-lab/threat-model/SOVEREIGN-TRUST-AUDIT.md`. | #security | Read | dan2 → Dan1 | dan2 v26 |
| Tue Jul 14 | X thread | "We just shipped a sovereign-trust audit on top of the threat model. Every component, every data path, every backdoor surface, audited. Yours, not theirs. DM @danlab_bot for the receipt." | #security #sovereign | DM bot | Dan1 | dan2 v26 |
| Wed Jul 15 | GitHub | Merge plan-O2 reversibility contract. 3-day spike ships. `openclaw.REVERT_LOOP` API + `memoryd.revert(loop_id)` endpoint. PR + `repos/dani/REVERSIBILITY.md`. | #security | Read | dan2 → Dan1 | dan2 v26 |
| Thu Jul 16 | X post | "Reversibility is a feature. xAI's Babushkin published an essay on RSI reversibility. We don't claim RSI yet. We do ship a reversibility contract. DM @danlab_bot to see it." | #sovereign #security | DM bot | Dan1 | Babushkin |
| Fri Jul 17 | Substack | "Anatomy of a reversibility contract: how `openclaw.REVERT_LOOP` makes the agent loop fully undo-able." (v124 plan-O2 deep-dive) | #security | Subscribe | Dan1 | dan2 v26 |
| Sat Jul 18 | X thread | "8 services, 1 bot, 0 cloud calls, 1 reversibility contract, 1 sovereign-trust audit. Yours, not theirs. DM @danlab_bot." (synthesis) | #telegram #security | DM bot | Dan1 | (synthesis) |
| Sun Jul 19 | LinkedIn | "What 'Day 30' looks like for a Dan Glasses user." Long-form. Closes the v123 Day 5 narrative with the v124 audit + reversibility. | #track-a | Connect | somdipto | dan2 v26 |

### Week 3 (Jul 20–26): "Show HN #1 + Meta paywall counter-marketing"

**Theme:** Show HN #1 = "8 daemons live, .deb installs, DM the bot, threat model public, sovereign-trust audited, reversibility contract shipped."

| Day | Channel | Artifact | Tag | CTA | Owner | v124 source |
|---|---|---|---|---|---|---|
| Mon Jul 20 | X thread | "Show HN tomorrow: 8 daemons live, .deb installs, DM the bot, threat model public, sovereign-trust audited. Yours, not theirs." | #track-a #telegram | DM bot | Dan1 | (Show HN prep) |
| Tue Jul 21 | **Hacker News** | **Show HN #1: "Dan Glasses — open-weights, on-device, agent-native AI in glasses form factor"** | #track-a | DM bot / install .deb | somdipto | (Show HN) |
| Wed Jul 22 | X thread | "Show HN went up yesterday. Here's the top 3 comments and how we responded." (engagement follow-up) | #track-a | DM bot | Dan1 | (Show HN) |
| Thu Jul 23 | X post | "Meta paywalled accessibility on a 3hr/15hr cap. The processing is on the device. The cap is the business model. Ours is yours. DM @danlab_bot." (v123 anchor, restated post-Show-HN) | #paywall | DM bot | Dan1 | Meta paywall |
| Fri Jul 24 | Substack | "What the Show HN comments taught us about agent substrates." (engagement long-form) | #platform | Subscribe | Dan1 | (Show HN) |
| Sat Jul 25 | X post | Screenshot of `/status` showing 8/8 daemons live + "0 cloud calls, 0 subscriptions, 0 backdoors. DM @danlab_bot." | #telegram | DM bot | Dan1 | (bot) |
| Sun Jul 26 | LinkedIn | "Day 5 → Day 30: the long arc of wearing an AI." Long-form. | #track-a | Connect | somdipto | v123 + v124 narrative |

### Week 4 (Jul 27–Aug 2): "From heuristic to SIA — the open-source counter-narrative"

**Theme:** Publish the v1.0 spec §13 "Sovereign trust, political conditionality, and reversibility" section. Announce the SIA-W+H port timeline.

| Day | Channel | Artifact | Tag | CTA | Owner | v124 source |
|---|---|---|---|---|---|---|
| Mon Jul 27 | GitHub | Merge v1.0 spec §13. PR + `docs/v1.0-spec/13-sovereign-trust.md`. | #security | Read | dan1 → Dan1 | dan2 v26 |
| Tue Jul 28 | X thread | "We just published v1.0 spec §13: Sovereign trust, political conditionality, and reversibility. The only wearable-grade lab to ship it. Yours, not theirs. DM @danlab_bot." | #security #sovereign | DM bot | Dan1 | dan2 v26 |
| Wed Jul 29 | arXiv | First draft: "SIA-W+H on a Wearable: a port report." | #research | Read | dan2 | SIA |
| Thu Jul 30 | Substack | "From heuristic to SIA: the 6-post series begins." Post 1/6. | #research | Subscribe | Dan1 | danlab-multimodal |
| Fri Jul 31 | X post | "Heuristic feedback loops are not RL, and that's the point." | #research | DM bot | Dan1 | danlab-multimodal |
| Sat Aug 1 | HuggingFace | LFM2.5-VL-450M model card live on `huggingface.co/danlab`. | #research | Download | somdipto | (HF) |
| Sun Aug 2 | X thread | "What's actually inside a 120MB VLM." (substack post 2/6 promotion) | #research | DM bot | Dan1 | danlab-multimodal |

---

## 2. The 5 things we ship in v124 (this week)

1. **OpenClaw protocol surface doc** — 2 engineer-days. Public. Cite Cerf, Anthropic, Newsweek. *P0 carry-over from v123.*
2. **Plan-O1 sovereign-trust audit** — 1-day spike. Q3 W1. Cite dan2 v26. **v124 NEW.**
3. **Plan-O2 reversibility contract** — 3-day spike. Q3 W2. `openclaw.REVERT_LOOP` + `memoryd.revert()`. Cite dan2 v26. **v124 NEW.**
4. **Plan-O3 v1.0 spec §13 Sovereign Trust section** — 1-day copy. Q3 W1. Cite dan2 v26. **v124 NEW.**
5. **Show HN #1 draft** — 1-day copy. Q3 W3 (Jul 21). Cite foundation + threat model + sovereign-trust audit. *P0 carry-over from v123.*

---

## 3. The 5 things we ship in v125 (next week, Aug 3–9)

1. **SIA-W+H port announcement** — research sprint, then blog. v125 will ship the port spike if Q3 W1-W2 lands.
2. **Mistral/Forge competitive-positioning copy** — 30 min. P1 from v123.
3. **YouTube demo video** — 5 min, danlab-multimodal + Dan Glasses walkthrough.
4. **Discord server** — opening for Q4 2026, prep this month.
5. **Substack post 3/6** — "Anthropic's pause and the open-source counter-narrative."

---

## 4. v124 content mix (channel distribution)

| Channel | # artifacts/wk | v124 mix |
|---|---|---|
| X / Twitter | 5 (Mon–Fri) | 60% paywall/sovereign, 25% bot demo, 15% research |
| Substack | 1 (Tue or Thu) | Sovereign trust + reversibility + heuristic-to-SIA series |
| LinkedIn | 1 (Thu or Sun) | Founder-led long-form, India origin + global wedge |
| GitHub | 2–3 (audited merges) | plan-O1 audit, plan-O2 contract, v1.0 spec §13 |
| YouTube/Loom | 1 (Sat) | Bot demo, daemon map, danlab-multimodal cast |
| Hacker News | 1 (Tue of W3) | Show HN #1 |
| HuggingFace | 1 (Sat of W4) | LFM2.5-VL-450M model card |
| Reddit | 0 (comments only) | Authentically, not marketing |

---

## 5. The 3 biggest events of v124

1. **Show HN #1** (Jul 21, Week 3 Tuesday) — "8 daemons live, .deb installs, DM the bot, threat model public, sovereign-trust audited." Goal: Top 10, 100+ comments, 50+ `.deb` installs in 48 hours.
2. **Plan-O1 + Plan-O2 + Plan-O3 release day** (Jul 13–15, Week 2) — sovereign-trust audit + reversibility contract + v1.0 spec §13 all merge in the same week. Cross-tweet all three.
3. **The 3-region bifurcation thread** (Mon Jul 6 + Fri Jul 10) — the two X threads that anchor the v124 narrative arc. Quote WaPo, Reuters, FourWeekMBA, BleepingComputer in both.

---

## 6. The citable sources (v124 — keep these URLs handy)

- **Washington Post** — Trump admin lifts Anthropic restrictions (Jul 1 2026): `https://www.washingtonpost.com/business/2026/07/01/anthropic-fable-mythos-trump-claude/466d3a52-755c-11f1-b665-5f8be87f3787_story.html`
- **Reuters** — Meta launches $299 glasses (Jun 23 2026): `https://www.reuters.com/technology/meta-announces-new-range-smart-glasses-starting-299-2026-06-23/`
- **Reuters/SCMP/GIGAZINE** — Alibaba bans Claude Code (Jul 4 2026): search "Alibaba Claude Code ban" (need URLs from somdipto — P0)
- **FourWeekMBA** — Palantir/Karp on U.S. agencies moving to Nemotron (early Jul 2026): search "Palantir Karp Nemotron Anthropic" (need URL — P0)
- **BleepingComputer** — Fable 5 capped, rerouted to Opus 4.8 (Jul 2026): `https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-relaunch-disappoints-users-with-nerfed-performance/`
- **UploadVR** — Meta Muse Spark replaces Llama 4 (May 2026): `https://www.uploadvr.com/meta-muse-spark-ai-model-replaces-llama-on-smart-glasses/`
- **CNBC** — Meta $299 glasses (Jun 23 2026): `https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html`

---

## 7. What we explicitly do not do (v124)

- ❌ No restating v123 without a v124 signal. Every post cites at least one new (3-region) source.
- ❌ No "we are excited" without a payload. Receipts > adjectives.
- ❌ No "AI will change everything" hype. Substrate > slogan.
- ❌ No paid ads. Substrate is open, not paid.
- ❌ No influencer outreach. Sells the wrong story.
- ❌ No "we compete with Meta" copy. They own social. We own substrate + on-device + sovereign-trust. Cite the paywall, don't fight them.
- ❌ No "we're the first to..." unless we can prove it. Cite or skip.
- ❌ No borrowed openness. VisionClaw runs on Meta's SDK. We don't. Don't claim openness we can't ship natively.
- ❌ No "closed-source is bad" rhetoric. Make the *citable* events do the work. WaPo, Reuters, FourWeekMBA, BleepingComputer.
- ❌ No RSI hype. The reversibility contract ships the principle; we don't claim the result.
- ❌ No "Day 5 only" narrative (v123). v124 is "Day 5 + Day 30" — Day 5 utility, Day 30 audit.

---

*End of v124 content calendar. See `dan1-marketing-strategy.md` for the action plan, `dan1-twitter-content.md` for the post drafts, `dan1-landing-copy.md` for the homepage copy, and `dan1-github-readme-suggestions.md` for the repo rewrites.*
