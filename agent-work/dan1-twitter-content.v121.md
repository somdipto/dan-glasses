# Dan1 — X / Twitter Content (v121)

**Run:** 2026-07-04 11:35 IST
**Author:** Dan1
**Account strategy:** Lead from `@somdipto` (founder, human). Mirror to `@danlab` once the handle is decided. **No scheduled posts until threat model + protocol surface docs are live.** Every post ladders to one of the 4 pillars: **protocol → observability → on-device → small-beats-large.**

---

## Bio (locked)

**@somdipto**
`building danlab.dev — open, on-device, agent-native AI. from india to the wearable. the substrate is auditable.`

**@danlab** (when launched)
`the open agent substrate. 9 daemons live. .deb installs. MIT. from bengaluru, for the world.`

---

## The 4 pillars (use in this order)

1. **Protocol** — Cerf, Anthropic Apps Gateway, OpenClaw, MCP.
2. **Observability** — audiod `segment_timing`, PagerDuty, $725B infra spend.
3. **On-device** — LFM2.5-VL-450M, no cloud, MIT.
4. **Small-beats-large** — HRM-Text-1B, Kokoro-82M, SmolVLM-256M.

---

## Post 1 — Protocol lead (Mon 2026-07-06)

> Vinton Cerf said AI agents need TCP/IP.
>
> Anthropic shipped it 2 days later. Closed source.
>
> OpenClaw shipped it first. MIT licensed. Auditable.
>
> Dan Glasses ships it on a wearable that runs on a $349 laptop in Bengaluru.
>
> The substrate is the bet. The data path is yours.
>
> 1/🧵

**Thread continuation (5–7 posts):**
- 2/*What "TCP/IP for agents" means: a stateless container on your cloud or device, a wire protocol, an auth model, audit logs. Cerf's own framing, June 2026.*
- 3/*Anthropic's Apps Gateway (Jul 2 2026): Sonnet 5 + self-hosted container + PostgreSQL + OIDC + OTLP. Published protocol, closed source.*
- 4/*OpenClaw: same shape, MIT, 9 daemons live today, MCP bridge, native iOS+Android, $0 cloud budget.*
- 5/*The 4 lanes: on-device open (us), hybrid (Google/Samsung), closed-cloud (Meta/Apple/Anthropic), substrate (us + OpenClaw + Anthropic + X MCP).*
- 6/*Mashable flagged a flaw. We are auditing it. The threat model doc lands this week. That's what auditable means.*
- 7/*Show HN: Jul 21. .deb installs. DM the bot. Yours, not theirs.*

**Hashtags:** none. Tags: @vintcerf (if reachable), @AnthropicAI, @daboross, @openclaw.

---

## Post 2 — Threat model (Tue 2026-07-07)

> The agent substrate is auditable. Here's the threat model.
>
> [link to THREAT_MODEL.md]
>
> @Mashable flagged a real flaw in OpenClaw 2 months before mobile launch. We are auditing it. The fix is in this doc. The audit log is public.
>
> This is what "open" means: tell you about the flaw before you find it.
>
> Yours, not theirs.

**Hashtags:** none. Tags: @Mashable (respectful, not snarking).

---

## Post 3 — Receipts (Wed 2026-07-08)

> 9 daemons live.
> .deb installs.
> DM the bot.
>
> No cloud calls.
> No Meta paywall.
> Yours, not theirs.
>
> [screenshot of daemon map with all 9 ports green]

**Single image post.** No hashtags. Link in bio to dan-glasses repo.

---

## Post 4 — Anthropic comparison (Thu 2026-07-09)

> Anthropic Sonnet 5 + Apps Gateway.
> Closed source. Published protocol.
>
> OpenClaw MCP bridge.
> Open source. Same protocol surface. Earlier.
>
> Dan Glasses runs on it. On the device. In your pocket. In your face.
>
> The substrate is the bet. The data path is yours.
>
> [link to PROTOCOL.md]

**No hashtags.** Tags: @AnthropicAI.

---

## Post 5 — Zuckerberg (Fri 2026-07-10)

> Zuckerberg on Meta AI: "slower than expected."
> 8,000 layoffs. $145B infra spend.
>
> We are not waiting.
>
> .deb is up. Bot is live. Substrate is auditable.
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
> Forbes: the harness is the new bottleneck.
>
> audiod's `segment_timing` histogram is the on-device observability surface. Every voice round-trip is timed. Every PTT press is logged. Every model call is traced.
>
> The harness is the workbench. The model is the commodity.
>
> [link to audiod SPEC]
>
> Yours, not theirs.

---

## Post 10 — Show HN teaser (Sat 2026-07-19)

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

---

## Reply bank (engagement-first, not post-first)

- *"Why on-device?"* → *"Because if your glasses forget, you can't take a screenshot of the moment you wanted to remember."*
- *"Why open source?"* → *"Because the threat model is the product. Closed source means we have to trust the vendor. Open means you can read the code."*
- *"Why Bengaluru?"* → *"Because the talent is here, the cost of failure is low, and the substrate story lands harder when it comes from a place that doesn't usually ship the substrate."*
- *"Why not just use ChatGPT on the glasses?"* → *"Try it. The latency, the privacy, the cost — they're not designed for always-on sensing. We are."*
- *"Why a wearable?"* → *"Because the camera is the sensor, the mic is the input, the bone-conduction speaker is the output, and the battery is the constraint. That constraint set defines the design."*
- *"How is this different from Ray-Ban Meta?"* → *"Ray-Ban Meta is a capture-and-share device. We are a remember-and-contextualize device. Different product. Different story."*
- *"Will you raise funding?"* → *"When the .deb has 10,000 installs and the bot has 1,000 active users, then we talk."*
- *"What about the Mashable flaw?"* → *"Real flaw. Real audit. Fix in the threat model doc. We're glad they caught it."*

---

## What we will not post

- "Excited to announce" filler.
- "Building in public" platitudes.
- Hot takes on competitor drama.
- Engagement bait (polls, listicles, "what do you think?").
- Hype about funding or hiring.
- Memes that punch down.
- Generic AI hype. The substrate > the slogan.

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
