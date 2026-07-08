# Dan1 — X / Twitter Content (v122)

**Run:** 2026-07-05 13:00 IST
**Author:** Dan1
**Account strategy:** Lead from `@somdipto` (founder, human). Mirror to `@danlab` once the handle is decided. **Posts #1 and #2 are GATED on the v24 threat model + toold strict-mode + openclaw shell-call audit shipping. No audit, no post.** Every post ladders to one of the 4 pillars + 2 v24 additions: **protocol → observability → on-device → small-beats-large → threat-model-is-public → yours-not-theirs.**

---

## Bio (locked)

**@somdipto**
`building danlab.dev — open, on-device, agent-native AI. from india to the wearable. the substrate is auditable.`

**@danlab** (when launched)
`the open agent substrate. 9 daemons live. .deb installs. MIT. from bengaluru, for the world.`

---

## The 6-step pillar checklist (apply to every post)

Before posting, ask:

1. **Protocol** — does this post ladder to Cerf, Anthropic Apps Gateway, OpenClaw, MCP?
2. **Observability** — does this post reference audiod `segment_timing`, PagerDuty, the $725B infra spend?
3. **On-device** — does this post name a model, a daemon, or a port?
4. **Small-beats-large** — does this post cite HRM-Text-1B, Kokoro-82M, SmolVLM-256M?
5. **Threat-model-is-public (v24 ADD)** — does this post link to the threat model doc, or cite Adversa / Mashable / HackerNoon / Anthropic-Samsung?
6. **Yours-not-theirs (v24 ADD)** — does this post say "audited, not perfect" instead of "secure"?

If the post fails step 5 or 6, it doesn't ship.

---

## Post 1 — Cerf / protocol lead (Mon 2026-07-06 — GATED on threat model doc live)

> Vinton Cerf said AI agents need TCP/IP.
>
> Anthropic shipped it 2 days later. Closed source. Closed weights. Now closed silicon — Anthropic is co-developing a custom inference chip with Samsung.
>
> OpenClaw shipped it first. MIT licensed. Auditable.
>
> Dan Glasses ships it on a wearable that runs on a $349 laptop in Bengaluru.
>
> The substrate is the bet. The data path is yours. The threat model is public.
>
> 1/🧵

**Thread continuation (5–7 posts):**
- 2/*What "TCP/IP for agents" means: a stateless container on your cloud or device, a wire protocol, an auth model, audit logs. Cerf's own framing, June 2026.*
- 3/*Anthropic's Apps Gateway (Jul 2 2026): Sonnet 5 + self-hosted container + PostgreSQL + OIDC + OTLP. Published protocol, closed source, closed silicon.*
- 4/*OpenClaw: same shape, MIT, 9 daemons live today, MCP bridge, native iOS+Android, $0 cloud budget.*
- 5/*The 4 lanes: on-device open (us), hybrid (Google/Samsung), closed-cloud (Meta/Apple/Anthropic), substrate (us + OpenClaw + Anthropic + X MCP).*
- 6/*@Mashable flagged a flaw. @AdversaAI just flagged bash-tricks bypass 10 of 11 open-source AI coding agents. We are auditing both. The fix is in the threat model doc. That's what auditable means.*
- 7/*Show HN: Jul 21. .deb installs. DM the bot. Yours, not theirs.*

**Hashtags:** none. Tags: @vintcerf (if reachable), @AnthropicAI, @daboross, @openclaw, @AdversaAI.

**GATE:** DO NOT POST until `dan-glasses/THREAT_MODEL.md` is live. If the gate slips, the thread moves with the doc.

---

## Post 2 — Threat model lead (Tue/Wed 2026-07-07/08 — GATED on threat model doc live)

> The agent substrate is auditable. Here's the threat model.
>
> [link to THREAT_MODEL.md]
>
> @Mashable flagged a real flaw in OpenClaw 2 months before mobile launch. @AdversaAI just disclosed bash-tricks bypass 10 of 11 open-source AI coding agents.
>
> We are auditing both. The toold fix is shipped (quote-removal + $IFS + unquoted-glob patterns). The openclaw → toold call chain is audited.
>
> The fix is in this doc. The audit log is public.
>
> This is what "open" means: tell you about the flaw before you find it.
>
> Audited, not perfect. Yours, not theirs.

**Hashtags:** none. Tags: @Mashable (respectful), @AdversaAI (credit), @daboross.

**GATE:** DO NOT POST until the threat model doc is live AND the toold fix PR is merged.

---

## Post 3 — Receipts (Wed 2026-07-08)

> 9 daemons live.
> .deb installs.
> DM the bot.
>
> No cloud calls.
> No Meta paywall.
> Audited, not perfect.
>
> Yours, not theirs.
>
> [screenshot of daemon map with all 9 ports green]

**Single image post.** No hashtags. Link in bio to dan-glasses repo.

**GATE:** OK to post on Wed regardless of threat model gate — the daemon map is the receipt, the threat model is the context. If threat model doc is live by Wed, link it in a reply.

---

## Post 4 — Anthropic + Anthropic-Samsung (Thu 2026-07-09 — v24 ADD)

> Anthropic Sonnet 5 + Apps Gateway.
> Closed source. Closed weights.
> Now closed silicon — Anthropic is co-developing a custom inference chip with Samsung.
>
> OpenClaw MCP bridge.
> Open source. Same protocol surface. Earlier.
>
> Dan Glasses runs on it. On the device. In your pocket. In your face.
>
> The substrate is the bet. The data path is yours.
>
> [link to PROTOCOL.md]
>
> v24 cite: @TechCrunch + @FourWeekMBA on the Anthropic-Samsung chip deal.

**No hashtags.** Tags: @AnthropicAI.

---

## Post 5 — Zuckerberg (Fri 2026-07-10)

> Zuckerberg on Meta AI: "slower than expected."
> 8,000 layoffs. $145B infra spend.
>
> We are not waiting.
>
> .deb is up. Bot is live. Substrate is auditable. Audited, not perfect.
>
> 9 daemons, MIT, $349 laptop, Bengaluru.
>
> Yours, not theirs.

**No hashtags.**

---

## Post 6 — HuggingFace (Mon 2026-07-13)

> LFM2.5-VL-450M is live on HuggingFace under the danlab org.
>
> 209MB. Vision-language. MIT.
>
> Runs on a laptop. No cloud.
>
> [link to HF model card]
>
> Same architecture class as the 4B Gemma 3 NASA put in orbit.
>
> Small beats large. Yours, not theirs.

**Tags:** @huggingface.

---

## Post 7 — Heuristic ≠ RL (Tue 2026-07-14)

> "Heuristic feedback loop" sounds like RL. It isn't.
>
> danlab-multimodal ships a pre-RL scaffold. The agent proposes a change. A heuristic scores it. The change is applied if the score improves. No gradient. No reward model.
>
> It's the cheapest possible improvement loop, and it works.
>
> [link to danlab-multimodal repo + asciinema]
>
> 1/🧵

**Thread:** 3–4 posts on the loop, the score function, the bench.

---

## Post 8 — Inside a 120MB VLM (Wed 2026-07-15)

> What's actually inside a 120MB VLM:
>
> - SmolVLM-256M (Q4_K_M, 120MB main)
> - SigLIP vision tower (182MB mmproj)
> - llama.cpp runtime
> - heuristic feedback loop
>
> Runs on CPU. 2-second latency on a $349 laptop.
>
> [code snippet from the repo]
>
> Small beats large. Yours, not theirs.

---

## Post 9 — Observability > model (Fri 2026-07-17)

> PagerDuty: agent model drift is the new outage.
> BNP Paribas: $725B AI infra spend in 2026.
> @HackerNoon: the month AI governance became operational.
>
> audiod's `segment_timing` histogram is the on-device observability surface. Every voice round-trip is timed. Every PTT press is logged. Every model call is traced.
>
> The harness is the workbench. The model is the commodity.
>
> [link to audiod SPEC]
>
> Audited, not perfect. Yours, not theirs.

---

## Post 10 — Show HN teaser (Sat 2026-07-19 — GATED on v24 audit + threat model doc)

> Show HN on Tuesday.
>
> "9 on-device AI daemons. .deb installs. DM the bot."
>
> Top of the page. Every comment answered. No marketing.
>
> Bring questions about the substrate. Bring questions about the threat model. Bring questions about the wearable.
>
> See you at 8am Pacific.
>
> Yours, not theirs.

**GATE:** DO NOT POST until v24 toold strict-mode + openclaw shell-call audit + threat model doc are all live.

---

## Reply bank (engagement-first, not post-first)

- *"Why on-device?"* → *"Because if your glasses forget, you can't take a screenshot of the moment you wanted to remember."*
- *"Why open source?"* → *"Because the threat model is the product. Closed source means we have to trust the vendor. Open means you can read the code. The threat model doc is at dan-glasses/THREAT_MODEL.md. Audited, not perfect."*
- *"Why Bengaluru?"* → *"Because the talent is here, the cost of failure is low, and the substrate story lands harder when it comes from a place that doesn't usually ship the substrate."*
- *"Why not just use ChatGPT on the glasses?"* → *"Try it. The latency, the privacy, the cost — they're not designed for always-on sensing. We are. And we audit our own substrate so you don't have to take our word for it."*
- *"Why a wearable?"* → *"Because the camera is the sensor, the mic is the input, the bone-conduction speaker is the output, and the battery is the constraint. That constraint set defines the design."*
- *"How is this different from Ray-Ban Meta?"* → *"Ray-Ban Meta is a capture-and-share device. We are a remember-and-contextualize device. Different product. Different story. Different threat model — ours is public."*
- *"Will you raise funding?"* → *"When the .deb has 10,000 installs and the bot has 1,000 active users, then we talk."*
- *"What about the Mashable flaw?"* → *"Real flaw. Real audit. Fix in the threat model doc. We're glad they caught it."*
- *"What about the Adversa bash-trick class?"* → *"We just shipped the toold strict-mode fix — quote-removal, $IFS spacing, unquoted-glob patterns. The openclaw → toold call chain is audited. The fix is in the threat model doc."*
- *"What about the Anthropic-Samsung chip?"* → *"Closed silicon. Closed weights. Closed protocol. The escape hatch is on-device + open-weights + auditable substrate. That's us."*
- *"What about the HackerNoon 'month AI governance became operational' framing?"* → *"The advantage is shifting from who builds the best model to who controls the conditions under which model capability is accessed, secured, and deployed. We are the audited-not-perfect path."*

---

## What we will not post

- "Excited to announce" filler.
- "Building in public" platitudes.
- Hot takes on competitor drama.
- Engagement bait (polls, listicles, "what do you think?").
- Hype about funding or hiring.
- Memes that punch down.
- Generic AI hype. The substrate > the slogan.
- **v22 ADD: any post that says "secure" without "audited."** The threat model is the product. The audit is the proof.
- **v22 ADD: any post that name-drops Adversa or Mashable without linking the threat model doc.** Credit the auditor, then link the audit.

---

## Posting cadence (locked)

- **Mon:** lead post (longest thread, biggest claim).
- **Tue–Thu:** receipts / model cards / threat model.
- **Fri:** culture / origin / "from India" (subtle, not jingoistic).
- **Sat:** quiet day. Reply-only.
- **Sun:** internal review, no posts.

**3–5 posts/wk. Never more than 1 thread/wk. Always respond to every reply within 4 hours during work hours IST.**

---

## The single rule

**Every post should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**

---

*v121 lead: protocol → observability → on-device → small-beats-large. v22 extensions: + threat-model-is-public + yours-not-theirs. Use all 6 in this order.*
