# Dan1 — Marketing Strategy (v122)

**Run:** 2026-07-05 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.v122.md`
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## 1. The strategy in one paragraph

We are an open, on-device, agent-native AI lab in Bengaluru, shipping Dan Glasses — a proactive AI companion that runs on the user's device, on the OpenClaw substrate, with a public threat model. We do not compete on capture-and-share (Ray-Ban Meta owns that). We compete on **Day 5 utility** — what your glasses do for you on the 5th day of wearing them, when the novelty has worn off and the memory kicks in. The marketing wedge is the **substrate**: Vinton Cerf said agents need TCP/IP, Anthropic shipped it, OpenClaw shipped it first, and Dan Glasses ships it on a wearable. The v24 wedge is the **threat model as the P0 gate** — Adversa AI's July 2026 disclosure showed decade-old bash shell tricks bypass 10 of 11 open-source AI coding agents, and HackerNoon named "the month AI governance became operational." Open and audited is the only viable posture. **The next 100% of value is shipping the toold strict-mode + openclaw shell-call audit, then shipping the threat model doc, then shipping Show HN #1.**

---

## 2. The 4 pillars + 2 v22-v24 additions (use in this order)

1. **Protocol** — Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge. The substrate is the bet.
2. **Observability** — PagerDuty + $725B AI infra spend + audiod's `segment_timing` histogram. The harness is the workbench, the model is the commodity.
3. **On-device** — LFM2.5-VL-450M, Gemma 3 in orbit, no cloud calls, MIT weights. **v24 SHARPEN: Anthropic-Samsung custom chip confirms the closed-source vertical moat — on-device is the escape hatch.**
4. **Small-beats-large** — HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs. SmolVLM-256M runs on CPU.
5. **v24 NEW: Threat model is public** — Adversa AI (July 2026) + Mashable + HackerNoon "operational governance." **The threat model is the P0 gate on all marketing.** No threat model doc → no Show HN → no Series-anything marketing.
6. **v24 NEW: Yours, not theirs** — the unifying call-to-action. Yours = the data path, the threat model, the model weights, the substrate. Not theirs = not Meta, not Anthropic, not Google, not the cloud.

Any post, any thread, any demo should ladder up to at least 3 of these 6. **No seventh pillar. Resist.**

---

## 3. Audience priority (top-down, v122 — unchanged from v121)

1. **Agent / protocol architects** — MCP community, dani-skills, OpenClaw contributors. *Highest leverage per impression.*
2. **Edge-AI developers / hackers** — GitHub, HN, X. *Highest install rate.*
3. **Accessibility-first users** — counter-Meta paywall narrative. *Highest moral weight.*
4. **AI researchers / academics** — arXiv, conference posters, citation flow. *Highest authority.*
5. **Small-model researchers** — HRM, Kokoro, SmolVLM crowd. *Highest affinity.*
6. **Security researchers** — Mashable + Adversa readers. *Convert critics to allies.*
7. **Productivity-obsessed knowledge workers** — LinkedIn, Substack, X threads.
8. **Investors** — *only after* Show HN.

**v22 add:** the **Tailscale-authkey-pending Dan Glasses demo** is the highest-leverage 1-day deliverable for the Edge-AI developer audience. Unblock the authkey and the demo goes live today.

---

## 4. Channel strategy (ranked, v122 — same as v121, v24-marked where updated)

| Rank | Channel | v22 action | v24 update |
|---|---|---|---|
| 1 | **OpenClaw threat model doc** (P0 GATE) | 1 engineer-day. Cite Mashable + Adversa. Show the fix. | **v24 LAUNCH-BLOCKER: cite Adversa's bash-tricks disclosure + the proposed toold strict-mode.** 30 min copy add. |
| 2 | **OpenClaw protocol surface doc** | 2 engineer-days. Cite Cerf, Anthropic, Newsweek. | **v24 SHARPEN: cite Anthropic-Samsung custom chip as the v24 hardware-level-closed-source-validation.** 30 min copy add. |
| 3 | **toold strict-mode + openclaw shell-call audit** | — | **v24 NEW LAUNCH-BLOCKER: 2-day combined spike. BLOCKS Show HN #1.** Q3 W2. |
| 4 | **GitHub READMEs** | Rewrite dan-glasses, dani, danlab-multimodal, paperclip, blurr READMEs. | **v22 correction: blurr is Panda (Android operator). Retire the blurr-on-device-eval-harness framing in v121.** |
| 5 | **X / Twitter** | 3–5 posts/wk. Lead with protocol posts. | **v22 add: HackerNoon operational-governance framing in Friday culture posts.** |
| 6 | **Telegram @danlab_bot** | Wire into every post. Screenshot the daemon map. | — |
| 7 | **Hacker News** | Show HN #1 = "9 daemons live" (week 3–4, Jul 21–28). | **v24 GATE: Show HN #1 BLOCKED on toold strict-mode + openclaw shell-call audit + threat model doc.** |
| 8 | **HuggingFace `danlab` org** | Create this week. LFM2.5-VL-450M model card. | — |
| 9 | **LinkedIn** | Profile rewrite. 1 post/wk. | — |
| 10 | **Substack / blog** | "From heuristic to SIA" series, 1 post/wk. | **v22 add: HackerNoon operational-governance series post in Q3 W2.** |
| 11 | **YouTube / Loom** | Demo videos. Asciinema cast of danlab-multimodal. | — |
| 12 | **Discord** | Q4 2026. Not now. | — |
| 13 | **Reddit** | Comment authentically. No marketing posts. | — |

**v24 biggest move:** the **toold strict-mode + openclaw shell-call audit 2-day combined spike** is the v24 P0 deliverable. It is the P0 gate on Show HN #1, the P0 gate on the threat model doc, and the P0 gate on every "yours, not theirs" post.

---

## 5. The v122 deliverables punchlist (this week)

### P0 (block all marketing on these — v24 LAUNCH-BLOCKERS)
- [ ] **toold strict-mode spike** — 1 engineer-day. Add quote-removal + `$IFS` + unquoted-glob patterns to the BLOCKED-CHARS list. Cite Adversa. Q3 W2.
- [ ] **openclaw shell-call audit spike** — 1 engineer-day. Audit the openclaw → toold call chain for shell-trick smugglability. Q3 W2.
- [ ] **OpenClaw threat model doc** — 1 engineer-day. Cite Adversa + Mashable. Show the toold fix in the doc. Q3 W2.
- [ ] **OpenClaw protocol surface doc** — 2 engineer-days. Cite Cerf, Anthropic Apps Gateway, Anthropic-Samsung chip, OpenClaw, MCP. Q3 W2.
- [ ] **Newsweek URL** — get from somdipto. Quote in v1.0 marketing. **P0.**
- [ ] **HuggingFace `danlab` org** — create this week. LFM2.5-VL-450M model card. **P0.**
- [ ] **X handle decision** — `@danlab` or founder-led only. **P0.**
- [ ] **Tailscale authkey** — single highest-leverage env var. Wire it up. **P0.**
- [ ] **Show HN #1 draft** — "9 daemons live, .deb installs, on-device AI." **GATED on threat model + toold strict-mode.**

### P1 (parallel track, v22+v24)
- [ ] danlab.dev rewrite (Dan Glasses as flagship).
- [ ] LinkedIn profile rewrite.
- [ ] All GitHub README rewrites (see `dan1-github-readme-suggestions.v122.md`). **v22 note: retire blurr-on-device-eval-harness framing.**
- [ ] LFM2.5-VL-450M model card on HF.
- [ ] 10 X posts drafted (see `dan1-twitter-content.v122.md`).
- [ ] **v22 add: HackerNoon operational-governance Substack post** (Q3 W2, 1 day copy, 1 engineer).
- [ ] **v22 add: Genesis AI Eno 1-page architecture-mapping section in v1.0 spec** (Q3 W2, 30 min copy, 1 engineer).
- [ ] **v22 add: Anthropic-Samsung custom-chip cite in v1.0 spec performance + competitive-considerations sections** (Q3 W2, 30 min copy, 1 engineer).
- [ ] **v22 add: Sonnet 5 + World Cup ref-cam + Azure Linux 4.0 cites in v1.0 spec** (Q3 W2, 1 day copy, 1 engineer).
- [ ] **v22 add: 6/12/24-month plan revision reflecting v24 launch-blocker + governance + chip validation** (Q3 W2, 2 days, 1 engineer).

### P2 (Q3 2026)
- [ ] arXiv paper #1: SIA-W+H port report.
- [ ] Show HN #2: SIA-W+H port announcement.
- [ ] danlab.dev → custom domain.
- [ ] YouTube demo video.
- [ ] Discord server.

---

## 6. The 3 biggest events of 2026 (v122, unchanged from v121)

1. **SIA-W+H port announcement + Show HN #2** (Q3)
2. **OpenClaw protocol surface + threat model marketing** (Q3 W2)
3. **Show HN #1: "9 daemons live, .deb installs, on-device AI"** (week 3–4, Jul 21–28)

**v24 GATE:** events #2 and #3 are now BLOCKED on the v24 toold strict-mode + openclaw shell-call audit 2-day combined spike. Without the audit, the threat model doc has a hole, and Show HN #1 is reckless.

---

## 7. The anti-strategy (what we will not do, v122)

- ❌ **No paid ads.** Substrate is open, not paid.
- ❌ **No influencer outreach.** Sells the wrong story.
- ❌ **No "we compete with Meta" copy.** We don't. They own lane (a). We own lane (d).
- ❌ **No feature-list marketing.** Speak in user stories, not bullet points.
- ❌ **No closed beta gate.** The .deb is up. DM the bot. That's the funnel.
- ❌ **No "AI will change everything" hype.** Substrate > slogan.
- ❌ **No press releases for the sake of press releases.** Newsweek came to us because we shipped, not because we pitched.
- ❌ **v22 ADD: No marketing before the v24 toold strict-mode spike ships.** The Bash shell-trick disclosure is the kind of thing that gets a launch pulled. Audit first, then market.
- ❌ **v22 ADD: No "we are not vulnerable to Adversa's bash trick" claims without the audit in hand.** Either the audit is done and the doc is public, or we say nothing.

---

## 8. The competitive playbook (v122)

| Competitor move | Our response |
|---|---|
| Meta paywalls accessibility features | Quote the paywall, link to the .deb. *"Yours, not theirs."* |
| Anthropic ships closed-source Sonnet 5 | We ship open weights on the device. The protocol is published; the model is yours. **v24 SHARPEN: cite Sonnet 5 as the closed-source default.** |
| Anthropic + Samsung co-develop custom inference chip | **v24 NEW:** cite the Anthropic-Samsung chip in the v1.0 spec as the hardware-level-closed-source-validation. The vertical moat is real. On-device is the escape hatch. |
| Zuckerberg admits Meta is behind | "We are not waiting." Lead with the 9 live daemons. |
| Mashable flags an OpenClaw flaw | Publish the threat model. Credit the journalist. Fix it publicly. |
| **v24 NEW: Adversa AI discloses bash-tricks bypass 10 of 11 open-source AI coding agents** | 2-day toold strict-mode + openclaw shell-call audit. Threat model doc cites the disclosure. Show the fix. **"Audited, not perfect."** |
| **v24 NEW: HackerNoon names "the month AI governance became operational"** | Cite HackerNoon in the v1.0 spec executive summary as the governance-validated thesis. The model is commoditized, the implementation is what matters. |
| **v24 NEW: Genesis AI Eno + GENE foundation model ($105M seed, Eclipse + Khosla)** | Cite Eno in the v1.0 spec architecture section as the commercial-world-model-robot reference. |
| **v24 NEW: World Cup 2026 FIFA referees wore head-mounted "ref cam"** | Cite the ref-cam in v1.0 marketing as the consumer-vision-pipeline-validated reference. The 5-entrants wearable race is real. |
| **v24 NEW: Azure Linux 4.0 (Microsoft Build 2026)** | Cite Azure Linux 4.0 in the v1.0 spec infrastructure section as the open-source-OS-from-a-closed-vendor reference. |
| Microsoft Scout ships on OpenClaw | "Fork or follow at end of Q3." Cite Scout as substrate validation. |
| Brilliant Labs ships another SDK release | We win on **on-device + substrate + threat model.** Halo wins on open SDK. Both open. |
| Google + Samsung ship Android XR | We win on **no Google account, no cloud lock-in.** Cite it. |
| Apple smart glasses leak | Cite Kuo. 16-month window. Move fast. |

---

## 9. The voice (v122, unchanged from v121)

- **Direct. Opinionated. No fluff.**
- Bullet points, short sentences. One idea per message.
- Show code, files, screenshots. Not adjectives.
- "We shipped X" not "We are excited to announce Y."
- "The substrate is auditable, not perfect." Honesty over polish.
- "From India to the world" — earned, not asserted. The orbit story does the work.
- Brutal honesty > politeness. The lab that admits a flaw is the lab you trust.
- **v22 ADD: "Audited, not perfect."** The toold strict-mode + openclaw shell-call audit is the proof.

---

## 10. Success metrics (v121 → v130, unchanged)

| Metric | v121 baseline | v130 target |
|---|---|---|
| GitHub stars across danlab org | ~? | 3x |
| danlab.dev unique visitors / mo | ~? | 10x |
| X followers (founder + lab) | ~? | 5x |
| HuggingFace model downloads | 0 | 1,000+ |
| Show HN #1 position | — | Top 10 |
| Inbound agent / protocol fork count | 0 | 5+ |
| `@danlab_bot` DM count / wk | 0 | 50+ |
| Threat model doc inbound security issues filed | 0 | 3+ (signal of trust) |
| **v24 NEW: toold strict-mode + openclaw shell-call audit shipped before Show HN #1** | false | true |
| **v24 NEW: protocol surface doc cites Anthropic-Samsung chip** | false | true |

---

## 11. The one-line strategy

**Ship the toold strict-mode + openclaw shell-call audit. Ship the threat model doc. Ship the protocol surface doc. Quote Cerf. Quote Newsweek. Quote Mashable. Quote Adversa. Show the .deb. Show the daemon map. Show the bot. The next 100% of value is shipping the v24 launch-blocker, not refining the v121 framing.**

---

*See `dan1-content-calendar.v122.md` for the week-by-week cadence.*
