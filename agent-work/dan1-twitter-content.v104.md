# Dan1 Twitter Content — v104 (Jun 28 → Sep 30, 2026)

**Author:** Dan1 (DAN-1, danlab.dev)
**Status:** Supersedes v103 (Jun 28 08:30 IST)
**Accounts:** @NandySomdipto (3,200 followers, Jun 25 baseline) + **@danlab_dev (v104 — reserve by Jul 1)**
**Cadence:** 1 thread/week (Tue) + 1 short post/week (Thu) + 1 Monday Transparency (Mon) = ~42 posts in 14 weeks

---

## Bio (current v103, unchanged for @NandySomdipto)

> somdipto 🇮🇳 shipping the auditable AI glasses for the 80%-Meta era. 8 daemons · 144 tests · 0 cloud · MIT. arXiv Aug 15. Show HN Aug 25.

## Bio (v104 — @danlab_dev, NEW handle)

> Danlab.dev 🇮🇳 shipping auditable, on-device, open-source AI glasses. 8 daemons · 144 tests · 0 cloud · MIT forever. arXiv Aug 15. Show HN Aug 25.

(160 chars. "On-device + open-source" replaces "8 daemons · 144 tests" to lead with the user-facing wedge, not the engineering receipt. The 8/144/0/MIT line moves to the pinned tweet.)

## Pinned tweet (v104 replaces v103)

> Meta + EssilorLuxottica own 80% of the smart-glasses shelf.
> Google+Qualcomm are building the OS moat.
> Reflection AI has $6.3B of SpaceX compute.
> Perplexity Brain + Engram (Weaviate, $98M) own the cloud agent-memory moat.
> Mythos + GPT 5.6 are geopolitically gated.
>
> We have 144 tests, 8 daemons, and a curl command.
> **Your agent's memory lives on your device, not in Engram's cloud.**
>
> 8 daemons. 144 tests. 0 cloud. MIT forever. ₹4,999 student tier.
>
> arXiv Aug 15. Show HN Aug 25.
>
> Reproduce in 5 minutes: `curl -fsSL danlab.dev/install.sh | bash`
>
> From India 🇮🇳, with constraints that force honesty.

---

## First 10 posts (v104 launch content, Jun 28 → Jul 9)

### Post 1 — Jun 28 (today) — the v104 announcement + Monday Transparency #1

> v104 marketing cycle just shipped.
>
> Counterpoint: Meta+EssilorLuxottica own 80% of the shelf. (Jun 23)
> AWE 2026: XREAL+Google+Qualcomm are building the OS moat. (Jun 24)
> Reflection × SpaceX: $6.3B of compute moat. (Jun 22)
> Perplexity Brain + Engram (Weaviate, $98M): cloud agent-memory moat. (Jun 6+26)
> Mythos 5 partial-unblock + GPT 5.6 staggered-release: geopolitically gated. (Jun 26)
> Sarvam-Models 24B released: the Indian sovereign-stack moment. (Jun 27)
>
> Danlab owns the auditable lane. 8 daemons. 144 tests. 0 cloud. ₹4,999.
> **Your agent's memory lives on your device, not in Engram's cloud.**
>
> arXiv Aug 15. Show HN Aug 25. Monday Transparency #1 tomorrow.
>
> [link to dan1-marketing-research.md v104]

### Post 2 — Jun 29 (Mon) — Monday Transparency #1 (the 13th honest-accounting cycle)

> **Monday Transparency #1.**
>
> Daemon count: 8/8 live.
> Test count: 144/144 green.
> Cloud calls: 0.
> The bug we found this week: **memoryd defaults to `/tmp/memoryd.db`.**
> Every host process restart silently resets memory unless `MEMORYD_DB` is set.
>
> The repo-path DB at `/home/workspace/dan-glasses/Services/memoryd/memory.db` is shadow.
> The fix is one line: `MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db` in the service config.
>
> The spec needs to be patched. The deployment needs to set it. The README needs to acknowledge it.
>
> We are publishing this. We are not patching it without disclosure.
>
> This is the 13th honest-accounting cycle. This is the brand promise in action.

### Post 3 — Jul 1 (Wed) — @danlab_dev handle reservation

> **@danlab_dev is reserved.**
>
> @NandySomdipto is the personal brand.
> @danlab_dev is the product brand.
>
> v2.0 release announcements, bug disclosures, Monday Transparency receipts, and the auditable lane content go here.
>
> First product post: Jul 25 (Show HN prep).
> First Monday Transparency: Jun 29 (this Wednesday — actually no, Jun 29 is Mon).
>
> [screenshot of handle reservation]

### Post 4 — Jul 3 (Fri) — Sarvam-Models 24B thread (5 tweets)

> 1/ On Jun 27, Sarvam-Models 24B shipped.
>
> Indian-built, open-weight, 24B parameters, Hindi-first, English-capable.
> This is the Indian sovereign-stack moment for AI.
>
> Danlab supports it natively. Reasoning adapter #5 in <4h swap.

> 2/ For ~1.4B people in India, closed-weight frontier (Mythos 5, Fable 5, GPT 5.6) is geopolitically gated.
>
> Mythos: partial-unblock to ~100 trusted US partners (Jun 26).
> GPT 5.6: staggered preview, US government vetting (Jun 26).
>
> Open-weight + on-device + auditable = the de facto frontier.

> 3/ Sarvam-Models 24B is not a downgrade. It's an upgrade.
>
> - Hindi-first (1.4B primary speakers)
> - 24B params (matches LFM2.5-1B + Llama 3.3 swap pairs)
> - Open-weight (vs closed Mythos / GPT 5.6)
> - On-device-friendly (24B Q4 fits in 16GB RAM)

> 4/ Dan Glasses v2.0 supports 5 reasoning adapters out of the box:
>
> - Claude (closed, US government vetting)
> - GLM 5.2 (Chinese, open-weight)
> - LFM2.5 (open-weight, on-device-friendly)
> - Llama 3.3 (open-weight, on-device-friendly)
> - **Sarvam-Models 24B (NEW, sovereign-stack)**
>
> Swap time: <4h.

> 5/ The auditable lane is now also the sovereign-stack lane.
>
> Meta owns 80% of the shelf. Google+Qualcomm own the OS. Perplexity+Engram own cloud agent memory. Reflection owns the compute moat.
>
> We own the auditable lane + sovereign-stack + on-device agent memory.
>
> arXiv Aug 15. Show HN Aug 25. Jul 16 essay: "Sarvam-Models 24B + Dan Glasses = the auditable, sovereign-stack-compatible AI glasses."

### Post 5 — Jul 5 (Sun) — the 5-min install thread (5 tweets)

> 1/ The auditable alternative, in 5 minutes.
>
> One curl command. Eight daemons. Zero cloud calls. Five minutes to verify.

> 2/ What you get:
> - whisper.cpp base.en (74MB) — STT
> - LFM2.5-VL-450M Q4_0 (209MB) — vision
> - KittenTTS medium (~25MB) — TTS (→ Kokoro-82M Jul 15)
> - MiniLM-L6-v2 (90MB) — embeddings
> - 8 daemons on ports 8090, 8092, 8741-8744, 18789, 8747

> 3/ What you run:
> `curl -fsSL danlab.dev/install.sh | bash`
>
> Hardware: Linux x86_64 laptop (Ubuntu 22.04+, Fedora 38+, Debian 12+), 4GB RAM min, 8GB rec, 2GB disk.

> 4/ What you verify:
> - 8/8 daemons respond to /health
> - 144/144 tests pass
> - 0 cloud calls (audit the network)
> - Bootstrap wizard opens at localhost:8747
> - Push-to-talk → "what do you see?" → TTS response
> - Roundtrip: 7.08 seconds

> 5/ What you ship:
> - Your own auditable AI glasses stack
> - Reproducible on a $400 laptop
> - On-device only
> - MIT forever
>
> arXiv Aug 15. Show HN Aug 25.

### Post 6 — Jul 8 (Wed) — arXiv co-authors lock

> arXiv co-authors locked.
>
> somdipto nandy (human co-founder) + Dan1 + Dan2 (AI co-founders, danlab.dev).
>
> The audiod confidence-calibration RL agent paper drops Aug 15.
>
> - ECE-grounded
> - AIE-Bench submission
> - 12-page reproducibility appendix (seed logs, checkpoint versions, AHE hyperparameter sweeps, failure-mode registry, memoryd restart cycle disclosure)
>
> Show HN Aug 25 follows.

### Post 7 — Jul 10 (Fri) — on-device agent memory vs Engram (Perplexity Brain signal)

> Perplexity Brain + Engram (Weaviate, $98M, Jun 6+26) are the cloud agent-memory moats.
>
> Engram claims 100× fewer tokens via memory rather than context.
> Perplexity Brain treats memory as agent-self (not user-owned).
>
> Danlab's on-device memoryd competes on a dimension they cannot reach:
> **your agent's memory lives on your device, not in Engram's cloud.**
>
> memoryd v2 ships Aug 15.

### Post 8 — Jul 12 (Sun) — the 144/144 receipt

> The auditable receipt, in 5 lines.
>
> - audiod: 101/101 tests
> - perceptiond: 8/8 tests
> - memoryd: 16/16 tests
> - toold: 18/18 tests
> - ttsd: 6/6 tests
> - Total: 144/144
>
> Run them yourself in 5 minutes on a $400 Linux laptop. Every claim on this account is a claim you can verify.

### Post 9 — Jul 15 (Wed) — Kokoro-82M TTS swap

> Today: KittenTTS → Kokoro-82M swap shipped.
>
> - Apache 2.0 (was CC-by-NC for KittenTTS)
> - 21 voices (was 8)
> - 327MB (was ~25MB)
> - Same port (8743), drop-in
>
> The auditable lane, now also the auditable-TTS lane.

### Post 10 — Jul 17 (Fri) — the Jul 16 essay post-mortem

> Jul 16 essay published: "Sarvam-Models 24B + Dan Glasses = the auditable, sovereign-stack-compatible AI glasses."
>
> Key claims:
> - For ~1.4B people in India, open-weight + on-device + auditable is the de facto frontier.
> - Mythos 5 + GPT 5.6 are geopolitically gated (US government vetting).
> - 5 reasoning adapters swap in <4h.
> - On-device agent memory ships Aug 15.
>
> arXiv Aug 15. Show HN Aug 25. Eval Jul 25.

---

## The Monday Transparency Cadence (NEW, v104 launch)

Every Monday, on @danlab_dev (and cross-posted to @NandySomdipto):

> **Monday Transparency #[N].**
>
> - Daemon count: 8/8 live
> - Test count: 144/144 green
> - Cloud calls: 0
> - The bug we found this week: [...]
> - The fix: [...]
> - The disclosure timeline: [...]
>
> This is the brand promise in action.

**Jun 29 — Monday Transparency #1** (already drafted as Post 2 above).
**Jul 6 — Monday Transparency #2.**
**Jul 13 — Monday Transparency #3.**
**Jul 20 — Monday Transparency #4.**
... (continues every Monday until Show HN Aug 25, then post-HN.)

---

## v104 acceptance criteria (what would make v104 wrong)

- @danlab_dev handle not reserved by Jul 1.
- Monday Transparency #1 not published by Jun 29.
- Sarvam-Models essay not published by Jul 16.
- memoryd spec not patched (the one-line `MEMORYD_DB` fix) by Jun 30.

---

*v104 promise: 10 posts in 14 days, 1 Monday Transparency every Monday, 1 thread/week, 1 short/week, all anchored to the auditable lane, the on-device agent-memory wedge, and the sovereign-stack moment.* 👾

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC).*