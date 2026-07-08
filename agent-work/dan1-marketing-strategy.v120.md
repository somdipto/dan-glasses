# Dan1 — Marketing Strategy (v120)

**Run:** 2026-07-04 08:30 UTC · Asia/Calcutta 14:00
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Window:** 2026-07-07 → 2026-09-28 (Q3, 12 weeks)
**Status:** v120. The strategy is the same shape as v119, with the protocol surface promoted to the lead and the security audit as the gate.

**Builds on:** v119, v118, dan1-marketing-research.v120.md.

---

## TL;DR — The Strategy in 60 Seconds

**Goal:** Make Danlab the lab the AGI-and-on-device community cites when they want to say "an open lab shipped it first."

**Lead story (v120):** *Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable. Newsweek cited us. Mashable flagged a flaw. We are auditing the flaw. The substrate is auditable, not perfect.*

**Three engines:**
1. **Substrate engine** (week 1–2): OpenClaw protocol surface, threat model, security posture, HuggingFace org.
2. **Receipts engine** (week 3–4): Show HN #1 with 9 live daemons, 0 cloud, verified by curl.
3. **Research engine** (week 5–12): VisualClaw cascade-gate, HRM-Text-1B integration, SIA-W+H port, Show HN #2, arXiv preprint.

**The one constraint that gates everything:** **the OpenClaw security audit must close before the protocol surface marketing lands.** The Mashable flaw is the price of admission. v120 is the first marketing run that says "we are not perfect" out loud. That honesty is the moat.

**The one env var that gates the demo:** `TAILSCALE_AUTHKEY` from somdipto. The moment it lands, the tailnet demo is a 30-second video and a tweet.

---

## 1. Strategic posture (v120)

### Where we are
- **8 service daemons live, verified by curl.** 1 Tauri v2 app published. 1 Telegram bot wired. 0 cloud calls. ~160 audiod tests passing.
- **Foundation is durable.** The 9-process stack has been v118-validated.
- **The substrate is now public.** OpenClaw iOS + Android shipped. Newsweek cited. Mashable flagged.

### Where we are going (Q3 2026)
- **From "an interesting wearable" to "the lab that shipped the agent substrate audibly before Anthropic, and told you about the flaw before it shipped."**
- **The protocol surface is the new origin pillar.** Cerf's framing is now citable. Anthropic is now a competitor. The lead must sharpen.

### What we are NOT
- We are not anti-cloud. We are on-device, open-weights, open-protocol, auditable.
- We are not the Sarvam story. We are not the Vayu story. We are the wearable side of the open AGI substrate.
- We are not Anthropic. We are not Meta. We are not Microsoft. We are not Apple. **We are the on-device implementation layer at $349 once, on a Bengaluru laptop, with a published threat model.**

### What changed in v120
- **v119 lead:** protocol is the bet (Cerf + OpenClaw + Anthropic Apps Gateway).
- **v120 lead:** protocol is the bet, **and the substrate is auditable, and we are not pretending it is perfect.** The Mashable article is a feature, not a bug, if we respond correctly.

---

## 2. The four pillars (v120)

### Pillar 1 — The protocol is the bet
- **Claim:** Vinton Cerf said it. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable.
- **Evidence:** `github.com/somdipto/dan-glasses/Services/openclaw/`, `arxiv.org/abs/...` (Anthropic Apps Gateway), Cerf's Open Frontier / Laude Institute talk (June 30 2026).
- **CTA:** OpenClaw protocol surface doc (publish week 1).
- **Risk:** Mashable-flagged flaw. Mitigation: 1-day threat model audit, ship with the protocol surface.

### Pillar 2 — The on-device thesis is no longer a pitch
- **Claim:** A 4B VLM is in orbit. A 1B reasoning model was trained for $1,500. An 82M TTS model beat ElevenLabs.
- **Evidence:** Loft Orbital Yam-9 (NASA JPL, April 2026), HRM-Text-1B (Sapient, June 2026, $1,500 from scratch), Kokoro-82M (Apache-2.0, 100+ languages, 82M params, beat ElevenLabs on 45-day test).
- **CTA:** HuggingFace `danlab` org + model cards (publish week 2).
- **Risk:** None. The evidence is peer-reviewed.

### Pillar 3 — Observability > model
- **Claim:** $725B AI infra spend. PagerDuty on agent model drift. The workbench, not the tool, is the wedge.
- **Evidence:** BNP Paribas ($725B AI infra, Forbes, July 2 2026), PagerDuty Jenn Tejada (Forbes, July 2 2026), audiod `segment_timing` histogram shipped to Loki (v1.3).
- **CTA:** audiod observability surface blog post (publish week 2).
- **Risk:** None. The wedge is real and validated.

### Pillar 4 — Small-beats-large is the new origin
- **Claim:** HRM-Text-1B (1B params, $1,500 from scratch, Apache-2.0) is the SOTA small-reasoning model. VibeThinker-3B scored 94.3 on AIME.
- **Evidence:** Sapient HRM-Text-1B (June 2026), VibeThinker-3B.
- **CTA:** HRM-Text-1B integration post + HuggingFace model card (publish week 9–10).
- **Risk:** None. We are integrating, not claiming we trained it.

---

## 3. The 12-week plan (v120)

### Weeks 1–2: Foundation sharpening (substrate + HuggingFace)
- Week 1: OpenClaw threat model doc, protocol surface doc, security posture doc. **3 docs, 1 week, 1 message.**
- Week 2: HuggingFace `danlab` org, LFM2.5-VL-450M model card, SmolVLM-256M model card, MiniLM-L6-v2 model card. audiod observability surface blog post.

### Weeks 3–4: Show HN #1
- Week 3: Show HN warmup. Tailscale demo (when authkey lands). 9 daemons, 0 cloud, verified by curl. India-to-the-world manifesto.
- Week 4: Show HN. Tue Jul 28. "9 daemons live. 0 cloud. From India." Cross-post everywhere. Live in chat 12 hours.

### Weeks 5–6: Cascade-gate port (VisualClaw)
- Week 5: perceptiond cascade-gate spike. 98% cost reduction target.
- Week 6: Cascade-gate merged. +15% accuracy on EgoSchema. Deep-dive blog post.

### Weeks 7–8: Dan Voice ecosystem + v1.5 spec
- Week 7: Dan Voice teaser. From glasses to earbuds. Same substrate.
- Week 8: Dan Glasses v1.5 spec locked. TTS: Kokoro-82M. STT: whisper.cpp + Silero. Reasoning: HRM-Text-1B.

### Weeks 9–10: HRM-Text-1B integration
- Week 9: HRM-Text-1B integration spike. audiod post-processor swap.
- Week 10: HRM-Text-1B merged. 4x speedup. Apache-2.0. $1,500 from scratch.

### Weeks 11–12: SIA-W+H port + Show HN #2
- Week 11: SIA-W+H port branch. arXiv preprint v1.
- Week 12: Show HN #2. Tue Sep 22. "Open RSI. On a wearable. Open source. Open weights." Weekly build-in-public #12.

---

## 4. The 10-step marketing narrative (v120, sharpened)

1. **BBC Meta paywall** (Jun 30 2026, BBC) — Conversation Focus paywalled. 3h/mo free, $20/mo for 15h.
2. **Apple $1,200+ glasses** (delayed to end 2027) — Kuo: Vision Pro line killed, all resources to glasses.
3. **Anthropic Mythos 5 Glasswing** (May 2026, expanding Jul 2026) — gated to ~100 US critical-infrastructure partners, now expanding internationally.
4. **GLM-5.2 MIT-licensed** (Jun 2026) — Chinese open-weights SOTA.
5. **Palantir + NVIDIA sovereign Nemotron** (May 2026) — on-prem vertical.
6. **$14.5B / 120 days / 6-vendor** (Jun 2026) — Microsoft + AWS + OpenAI + Anthropic + Google + IBM/Red Hat all shipping agentic workbenches.
7. **DoD GenAI.mil 1.7M** (Jun 2026) — US Department of Defense ships GenAI.mil, 1.7M users.
8. **GPT-5.6 government-gating** (Jun 2026) — OpenAI's frontier agent gated to gov-tier customers.
9. **Vinton Cerf: agents need TCP/IP** (Jun 30 2026) — Cerf at Open Frontier / Laude Institute.
10. **Newsweek Open Accountability + Anthropic Claude Apps Gateway + OpenClaw iOS+Android + X MCP** (Jun 30–Jul 2 2026) — **v120 NEW:** the substrate is shipping. Newsweek cited OpenClaw. Mashable flagged a flaw. We are auditing it.

**The 10-step is the v1.0 press kit.** Every post, every pitch, every DM ends with a step from the 10.

---

## 5. The channel mix (v120, refined)

| Channel | Cadence | Lead post (week 1) | Conversion |
|---|---|---|---|
| **X / Twitter** | 3–5/wk | "We audited the substrate. Here's the 1-day spike." | DM @danlab_bot |
| **Substack / danlab.ai** | 1/wk | "Vinton Cerf said AI agents need TCP/IP" | Email + danlab.ai |
| **GitHub** | 1–3/wk | OpenClaw threat model v1, protocol surface v1, security posture v1 | Stars + forks + Dani skills |
| **Hacker News (Show HN)** | 2 in Q3 | Week 4 + Week 12 | Comments + GitHub stars |
| **Telegram (@danlab_bot)** | Always-on | DM the bot, the bot answers | Daemon stack reachable |
| **HuggingFace** | 1–2/wk | LFM2.5-VL-450M model card, HRM-Text-1B model card | Model downloads |
| **LinkedIn** | 1/wk | "From India to the world" | Hiring + investor pipeline |
| **Reddit** | Comments only, no posts | r/LocalLLaMA, r/MachineLearning, r/india | DM @danlab_bot |
| **YouTube / Loom** | 1/quarter | Show HN video, cascade-gate demo | Show HN embedding |
| **arXiv** | 1 in Q3 (week 11) | SIA-W+H preprint v1 | Citations |
| **Discord** | Q4 launch | TBD | Community |
| **Newsweek (organic citation)** | 1 | "Open Accountability Standards" article | Press + citations |

---

## 6. The brand promise (v120)

**One sentence:** *We build the on-device, open-weights, open-protocol, auditable AI substrate for the wearable era — from India, with the threat model public, with the substrate honest about its flaws.*

**The three promises:**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall.
2. **The protocol is the bet.** Cerf said it. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on a wearable.
3. **Auditable, not perfect.** The threat model is public. The flaws are flagged. The fixes are shipped.

**The one anti-promise:**
- *We are not the cheapest. We are not the shiniest. We are the most honest.*

---

## 7. KPIs (v120, 12 weeks)

| KPI | Target | Method |
|---|---|---|
| **X followers** | +5,000 | 50 posts at ~100 net followers each |
| **GitHub stars (dan-glasses)** | +1,500 | Show HN #1 + SIA-W+H port |
| **Telegram bot DMs/week** | 50+ | Wire bot into every post |
| **HuggingFace downloads** | 5,000+ across 4 model cards | LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B, MiniLM |
| **Show HN #1 points** | 200+ | Tue Jul 28 |
| **Show HN #2 points** | 300+ | Tue Sep 22 |
| **Substack subscribers** | +500 | 12 essays, ~42 subs/essay |
| **arXiv citations** | 5+ by end of Q4 | SIA-W+H preprint |
| **Media mentions** | 5+ tier-2 (TechCrunch, Mashable, Forbes, Newsweek, BBC) | Newsweek already done, Mashable already done |
| **Discord waitlist** | 200+ by end of Q4 | Tally form, week 12 |

**The one KPI that matters most:** **Show HN #1 points + Show HN #2 points.** Two well-timed HN posts in one quarter is the single most credible marketing outcome we can produce. The points are the proof. The points are the SEO. The points are the inbound.

---

## 8. Risks (v120)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **OpenClaw security flaw unfixed by Show HN** | Medium | High | 1-day threat model audit, ship security posture doc week 1 |
| **Tailscale authkey not set by Show HN** | High | Low | Tailnet demo is a stretch goal, not the lead |
| **HRM-Text-1B integration slips** | Medium | Low | Fallback: LFM2.5-1.2B-Thinking stays as v1.5 plan-B |
| **Show HN #1 tanks** | Low | Medium | Tighter preview, internal dry-run with 5 dan-consciousness contributors |
| **Cascade-gate port slips past week 6** | Medium | Low | Fallback: ship the heuristic loop as the lead, cascade-gate as v1.5 stretch |
| **Mashable becomes a major story** | Low | High | Threat model doc ships week 1, security posture doc ships week 1 |
| **Sarvam or Vayu ships a similar wearable first** | Low | Medium | Lead with the protocol surface + threat model, not the hardware |
| **Microsoft Scout ships the OpenClaw-on-wearable story first** | Low | Medium | Differentiate on the threat model + the wearable form factor |

---

## 9. The five next decisions for somdipto (v120)

1. **OpenClaw security audit (1 day, 1 engineer):** go this week? **v120 P0.**
2. **OpenClaw protocol surface doc (2 days, 1 engineer):** ship week 1? **v120 P0.**
3. **HuggingFace `danlab` org creation:** authorize Dan1 to create this week? **v120 P0.**
4. **Tailscale authkey:** set this week? **v120 P0.**
5. **Show HN #1 timing:** Tue Jul 28 OK? **v120 P0.**

---

*End of v120 strategy. See `dan1-content-calendar.v120.md` for the 90-day posting schedule.*
