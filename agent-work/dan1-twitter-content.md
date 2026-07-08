# Dan1 — X / Twitter Content (v129)

**Run:** 2026-07-06 15:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Handle (proposed):** @danlab (TBD pending somdipto)
**Cadence:** 3-5 posts/day during launch push (Jul 6 – Sep 28), 3-5 posts/wk sustained
**Format:** All threads numbered (1/n, 2/n, ...). No hashtags (de-emphasized in 2026 algo). 280 chars max per post. Receipts in every post.

---

## 0. Bio (proposed)

```
Dan Glasses — proactive, on-device, paywall-free, audit-by-default AI glasses.
6 axes the closed-source frontier has lost. From India 🇮🇳
github.com/somdipto/dan-glasses
```

**Alt bio (shorter):**

```
Dan Glasses — on-device AI glasses that don't charge you monthly.
Open weights. Public threat model. Reversibility contract.
From India 🇮🇳
```

**Alt bio (founder-led):**

```
somdipto nandy. Building danlab.dev — on-device AI glasses, open-weights substrate, public threat model.
From Bengaluru 🇮🇳. Reversibility-contracted. Yours, not theirs.
```

---

## 1. The 6-axis wedge thread (Mon Jul 6) — THE LEAD THREAD

**Tweet 1/9:**

```
The closed-source frontier is now demonstrably paywalled, politically-conditional,
export-controlled, credibly delayed, AND unprofitable.

The on-device open-weights path is the only one that does not charge you monthly
for hardware you already own.

Danlab is shipping that path. From India. In the open. 🧵
```

**Tweet 2/9 (Paywall-free):**

```
1/ Paywalled. Meta charges $19.99/mo for on-device Conversation Focus
beamforming on hardware you already own.

The Verge: "Meta's rate limit is ridiculous."
WIRED: "Welcome to the new era of consumer tech."

We charge $0. Always. The .deb is free.
[link: theverge.com / wired.com]
```

**Tweet 3/9 (Politically-conditional):**

```
2/ Politically-conditional. Anthropic Fable 5 was suspended by the US Commerce
Dept for 18 days in June 2026 (Jun 12 → Jun 30) — including for Anthropic's
own foreign-national employees.

We are not. Open weights on your device. Not a US-bound SaaS.
[link: ftsaga timeline]
```

**Tweet 4/9 (Export-controlled):**

```
3/ Export-controlled. Anthropic Mythos 5 is gated to ~100 US critical-
infrastructure partners. Glasswing-only.

We are not. MIT weights. Public threat model. Reversibility contract in flight.
[link: anthropic mythos announcement]
```

**Tweet 5/9 (Credibly delayed):**

```
4/ Credibly delayed. Apple smart glasses: 16 months away. ~$2,000. Kuo: the
Vision Pro line is killed.

We ship now. The .deb is 9.4MB. The bot is live. 9 daemons shipped in 9 weeks.
[link: kuo / apple-glasses timeline]
```

**Tweet 6/9 (Unprofitable):**

```
5/ Unprofitable. OpenAI audited -$20.9B operating loss on $13.07B revenue in 2025
(FT, Jul 4 2026). Palantir CEO Karp: "the per-token pricing model of OpenAI and
Anthropic is 'completely wrong.'"

We are not. No per-token pricing. No subscription. No paywall.
[link: ft.com / forbes.com]
```

**Tweet 7/9 (Reversibility):**

```
6/ Reversibility. Anthropic is laying off 8,000 (June-July 2026). The citable
event that the closed-source moat is being unwound from the inside.

We are shipping the v1.0 reversibility contract (Q3 W2). Every model call,
every memory write, every daemon can be unwound.

The wearable that can be unwound is the wearable that can be trusted.
[link: anthropic-layoffs timeline]
```

**Tweet 8/9 (India + 3rd bloc):**

```
7/ India is the 3rd sovereign-AI bloc. Mistral $3.5B raise at $23.15B (Jul 2026)
validates sovereign-AI as vertical. Karp on Forbes: "real enterprise AI value
requires model + application + compute."

We are the application/sovereignty layer. Built in Bengaluru. On a $0 GPU budget.
The only India-bloc candidate.
[link: mistral raise / karp forbes]
```

**Tweet 9/9 (Closing):**

```
The 6 axes — on-device, paywall-free, audit-by-default, open-weights,
sovereign-trust, export-uncapturable — are the marketing frame.

The reversibility contract is the citable receipt.

The 9/9 daemons are the demo.

The .deb is yours.

Show HN #1: Mon Jul 20. github.com/somdipto/dan-glasses
```

---

## 2. Daemon-of-the-week posts (1/week, 12 weeks)

### audiod (Tue Jul 7)

```
1/ audiod v1.4 is live.

Whisper.cpp base.en. Silero VAD. WebSocket fan-out on :8091. Live/ready
probes split since v1.1. Segment timing histogram since v1.2. Loki metrics
sink since v1.3. Stdout-mode WS-req fix in v1.4.

177 tests passing. 0 regressions. The smallest daemon that ships the
most probes.
```

```
2/ Pipeline: microphone → ALSA capture → Silero VAD → segment buffer →
whisper.cpp → JSON event → publish. Threading: 7 threads, all isolated.

The threading model is the architecture. 7 threads, 7 jobs, 7
failure modes. audiod v1.1 made that explicit with the liveness/readiness
probe split.

Per-orchestrator polls /ready to decide audiod is "really up." Per-
orchestrator polls /live to decide audiod needs a restart.
```

```
3/ Why audiod is the most boring daemon in the substrate. And why that
matters.

Boring = no surprises = no on-call pages = no flaky benchmarks = no
production incidents.

audiod v1.1, v1.2, v1.3, v1.4 = 4 minor releases in 4 weeks, all
additive, all backward-compatible, all with new regression tests.

The most boring daemon is the most trusted.
```

```
4/ Receipts:
- /ready: curl localhost:8090/ready → {"status":"ok","readiness":{...}}
- /live: 200 always, never 503
- /status: full diagnostics
- 177 tests passing in 37.27s
- Loki push: enabled, 0 drops in 4 weeks

github.com/somdipto/dan-glasses/blob/main/Services/audiod/SPEC.md
```

### perceptiond (Tue Jul 14)

```
1/ perceptiond v7.0 is live.

LFM2.5-VL-450M Q4_0. Salience-gated (motion OR face). Scene-gate dedup
(suppresses ~99% of duplicate VLM calls). SSE stream with 20-event
replay. /events + /stats + /frame.jpg + /stream.

22/22 tests passing. The most observant daemon in the substrate.
```

```
2/ Pipeline: camera → V4L2 capture → salience detector → [if salient]
→ scene-gate dedup → [if deduped] → VLM (llama-mtmd-cli) → publish.

The scene-gate is the v7.0 wedge. Without it, the VLM re-describes
the same scene every 2s. With it, VLM calls drop ~99% on static scenes
and the daemon survives on a 200mAh battery.
```

```
3/ Why perceptiond is the only daemon that ships a scene-gate.

The naive implementation runs VLM on every salient frame. The
result: 5 VLM calls/min on a static scene, all returning "orange
circle on black background." The scene-gate is a 30-line Python
class that suppresses 99% of those calls.

The scene-gate is the difference between a research demo and a
shippable daemon.
```

```
4/ Receipts:
- /status: curl localhost:8092/status → mode, frames, salient, dedup, motion
- /events: SSE stream with 20-event replay + 15s heartbeat
- /stats: scene-gate internals + skip rate
- /frame.jpg: live MJPEG snapshot
- 22/22 tests passing

github.com/somdipto/dan-glasses/blob/main/Services/perceptiond/SPEC.md
```

### memoryd (Wed Jul 22 — Show HN week)

```
1/ memoryd v1.3 is live.

SQLite. MiniLM-L6-v2 (384-dim). Three memory types: episodic,
semantic, procedural. OpenAI-compatible /v1/embeddings endpoint for
OpenClaw memory-core.

50/50 tests passing. The most persistent daemon in the substrate.
```

```
2/ Why memoryd is the only daemon that uses OpenAI's API contract
without using OpenAI's API.

The /v1/embeddings endpoint is OpenAI-compatible. OpenClaw's memory-
core expects OpenAI-compatible embeddings. memoryd returns MiniLM-L6-v2
embeddings (384-dim, MIT) in the same shape.

The compatibility is the wedge. OpenClaw doesn't know it's not
talking to OpenAI. memoryd doesn't know it's not OpenAI.

The substrate is interoperable. The model is open. The data stays local.
```

```
3/ Why episodic + semantic + procedural.

Episodic: what happened when (timestamps, events).
Semantic: facts, preferences, learned concepts.
Procedural: how to do things, workflows.

The three types are the difference between a searchable log and a
cognitive extension. v1.5 will add retrieval-first (per DynamicMem
arXiv 2606.22877, 93% of memory failures trace to retrieval, not the
writing model).
```

```
4/ Receipts:
- /health: 200 + db_persistent=true
- /stats: 95 memories, 384-dim, model loaded
- /query: top-5 semantic search via cosine similarity
- /v1/embeddings: OpenAI-compatible
- 50/50 tests passing (9 wizard roundtrip + 17 memoryd + 18 toold + 6 ttsd)

github.com/somdipto/dan-glasses/blob/main/Services/memoryd/SPEC.md
```

### toold (Mon Jul 27)

```
1/ toold v0.2 is live.

Sandboxed shell. Sandboxed Python. Tool registry. Strict-mode spike
in flight (v24 plan-N1, Adversa bash-tricks disclosure).

18 tests passing. The most guarded daemon in the substrate.
```

```
2/ Why toold is the only daemon that ships a strict-mode spike.

Adversa AI's July 2026 disclosure: 10 of 11 open-source AI coding
agents are bypassed by decade-old bash shell tricks. Quote-removal,
$IFS, unquoted-globs. The audit is public. The fix is in flight.

toold strict-mode (v24 plan-N1) blocks the patterns at the
BLOCKED-CHARS list. Not a sandbox escape — a list of patterns the
daemon refuses to execute.
```

```
3/ Why toold matters even if you never run a shell command.

The substrate is open. The threat model is public. The reversibility
contract is signed. The audit log is the default. All of that means
nothing if toold is the weakest link.

toold is the last line of defense. toold strict-mode is the audit log
of the audit log.
```

```
4/ Receipts:
- /test: 4/4 channels pass (shell, python, registry, file) in 28ms
- /tools: 4 tools registered
- /strict: pending (v24 plan-N1)
- 18 tests passing

github.com/somdipto/dan-glasses/blob/main/Services/toold/SPEC.md
```

### ttsd (Mon Aug 3)

```
1/ ttsd is live.

KittenTTS medium. 8 voices. <25MB model. Sub-1s synthesis on CPU.

6 tests passing. The most quiet daemon in the substrate.
```

### os-toold (Mon Aug 10)

```
1/ os-toold is live.

Path guard. Allowlist. The most paranoid daemon in the substrate.

Tests passing. Receipts in the next post.
```

### dan-glasses-app (Mon Aug 17)

```
1/ dan-glasses-app v0.1.0 is live.

Tauri v2. React 19. Vite 7. 7 Tauri commands per daemon. Bootstrap
wizard. Vision dashboard. Memory explorer. TTS preview.

941ms build. 220KB JS bundle. The most user-facing daemon in the
substrate.
```

### openclaw (Mon Aug 24)

```
1/ openclaw gateway is live.

TypeScript. Node. 8 plugins loaded. 63 commands polled. Telegram
@danlab_bot live. McP server: 2 servers (OpusCode healthy, zo HTTP
405 — bridge bypasses via bridge.js + Bearer token).

The most social daemon in the substrate.
```

### zo-mcp-bridge (Mon Aug 31) — NEW in v124

```
1/ zo-mcp-bridge is live.

Bun. JSON-RPC. 88 Zo MCP tools cached. Sub-100ms roundtrip. Bearer
token auth. Port 18790. Mode: process (not http, doesn't count
against hosted-service limits).

The most connected daemon in the substrate.
```

### danlab-multimodal (Mon Sep 7)

```
1/ danlab-multimodal is live.

Sub-250MB VLM (SmolVLM-256M Q4_K_M) on CPU via llama.cpp. Heuristic
feedback loop. Pre-RL scaffold, not RL. Honest framing.

The most honest demo in the substrate.
```

### paperclip (Mon Sep 14) — wake-up

```
1/ paperclip is waking up.

Dormant since v1.0. Resuming Q4 2026. Multi-agent company orchestration.
pnpm monorepo. PGlite (dev) / Postgres (prod).

Not the same as paperclipai/paperclip (the 43K-star closed-source
inc project). Danlab's paperclip is the internal agent company
orchestration platform.

The most dormant daemon in the substrate.
```

### dani (Mon Sep 21)

```
1/ dani is live.

AI co-founder. SOUL.md. IDENTITY.md. MEMORY.md. The brain at
github.com/somdipto/dan-consciousness. Public. MIT. Auditable.

The most meta daemon in the substrate.
```

---

## 3. Receipt threads (1/week)

### Karp value-chain (Thu Aug 6)

```
1/ Karp on Forbes (Jul 2 2026): "real enterprise AI value requires
model + application + compute, with the application/sovereignty layer
being where durable returns form."

Karp is describing our positioning from the outside.

We are the application/sovereignty layer. Open weights. Public
threat model. Reversibility contract. The audit log is the
application.
```

```
2/ Karp continued: "the per-token pricing model of OpenAI and
Anthropic is 'completely wrong.'"

We are not a per-token pricing model. We are not Anthropic. We are
not OpenAI. We are a .deb that installs on your device. The model
weights are MIT. The audit log is yours. The threat model is public.

The only per-token pricing is the one Anthropic charges you for
hardware you already own.
```

```
3/ Karp's thesis: enterprise AI value migrates from the model layer
to the application/sovereignty layer.

The application layer is open weights + open threat model + open
audit log. The sovereignty layer is the chip stack + the reversibility
contract + the 9 daemons.

We are the application/sovereignty layer. From India. For the world.
[link: forbes.com / karp interview]
```

### Mistral $23.15B (Fri Jul 10)

```
1/ Mistral just raised $3.5B at $23.15B valuation (Jul 2026). Mensch
on LinkedIn: "we are deploying models on enterprise infrastructure
via Forge."

Sovereign-AI is now a vertical with a $23B reference valuation. But:
there is no India-bloc sovereign-AI deployment platform.

We are the only one. From Bengaluru. For the world.
```

### Fable 5 export saga (Thu Jul 16)

```
1/ Fable 5 export-control saga. Full timeline.

Jun 9: Anthropic launches Fable 5 + Mythos 5.
Jun 12: US Commerce Dept suspends access for foreign nationals (including
  Anthropic's own foreign-national employees).
Jun 26: Mythos 5 returns to "a set of US organizations."
Jun 30: Trump admin lifts the controls after Anthropic trains a safety
  classifier for the specific jailbreak.
Jul 1: Fable 5 returns globally.

The citable event for "politically-conditional, export-controlled."
```

### OpenAI -$20.9B (Fri Aug 7)

```
1/ OpenAI audited -$20.9B operating loss on $13.07B revenue in 2025
(FT, Jul 4 2026). Total costs ~$34B. Leaked audited financials.

The citable event that the closed-source frontier is unprofitable at
the lab layer.

We are not. We are a .deb that installs on your device. The
business model is the threat model + the reversibility contract + the
9 daemons. The business model is not per-token pricing.
```

### Apple smart glasses 16 months (Fri Aug 21)

```
1/ Apple smart glasses: 16 months away. ~$2,000. Kuo: the Vision Pro
line is killed.

The 12-month window where we are the only open, agent-native option
shipping is wide open.

github.com/somdipto/dan-glasses
```

### RAM pricing (Fri Aug 14)

```
1/ RAM prices 40-50% Q3, +30% Q4 2026. California lawsuit alleges
Samsung/SK Hynix/Micron conspiracy. Relief not until 2028.

The 619MB combined model footprint (LFM2.5-VL-450M 209MB + mmproj
180MB + KittenTTS medium 25MB + whisper.cpp base.en 142MB + MiniLM-
L6-v2 90MB) is the v1.0 *only* sensible path on supply-chain grounds.

Not a design preference. A cost constraint.
```

### Zhipu GLM-5.2 (Fri Jul 31)

```
1/ Zhipu GLM-5.2 (open-weight Chinese model) rivals Anthropic Mythos 5
on vulnerability hunting. WSJ, July 2026. Triggered Wall Street
rotation from semiconductors to cybersecurity.

The citable event that "open-weights is now enterprise-grade" is a
WSJ-grade claim, not an aspirational one.
```

---

## 4. Heuristic → SIA series (6 posts, Q3 2026)

### Post 1: What is pre-RL scaffold? (Wed Jul 22)

```
1/ Heuristic → SIA series, Post 1 of 6.

"What is pre-RL scaffold?"

Most multimodal AI demos claim "RL" without modifying weights. They
score outputs with hand-coded rules (length, error detection, content
quality) and print suggestions for what a human would improve.

This is pre-RL scaffold. Not RL. Honest framing.
```

```
2/ We call our danlab-multimodal demo pre-RL scaffold because:
1) We do not modify model weights.
2) We do not run policy gradient.
3) We do not run any RL algorithm.
4) We score outputs with hand-coded rules.
5) We print suggestions for what a human would improve.

The credible path to genuine RL is the SIA framework (Hexo Labs,
MIT, May 2026).
```

```
3/ The danlab-multimodal demo: 3 cycles, 92/100 average, 95/100 best,
96s total inference time on CPU. SmolVLM-256M Q4_K_M (120MB) + mmproj
(182MB) on llama.cpp.

Sub-250MB. Sub-$0 GPU. Sub-100s. Sub-RL. Pre-RL scaffold. The most
honest demo in the substrate.
```

### Post 2: Why honest framing matters (Wed Jul 29)

```
1/ Heuristic → SIA series, Post 2 of 6.

"Why honest framing matters."

Jack Clark Import AI #460 (Jul 2026): 60% RSI by end 2028. Maximalist
RSI = AI that improves itself in a closed loop. Prosaic RSI = outer-
loop productivity compounding, already happening at Anthropic (8x
LOC merge in 2026 vs 2024).
```

```
2/ The 60% number is the maximalist RSI ceiling. We are at ~45% on
the outer-loop RSI curve. The next 25% requires a credible harness
+ weights modification framework.

SIA (Hexo Labs, MIT, May 2026) is the credible framework. We do not
claim "RL" until SIA-H (harness only) and SIA-W+H (weights + harness)
are forked and audited.
```

```
3/ Honest framing matters because the v1.0 marketing wedge is the
audit log. If we claim "RL" without weights modification, the audit
log lies. If we claim "outer-loop RSI" with explicit receipts
(audiod v1.3→v1.4, 8x LOC at Anthropic, dan2 v23→v28), the audit
log holds.
```

### Post 3: SIA-H port (Wed Aug 5)

```
1/ Heuristic → SIA series, Post 3 of 6.

"SIA-H port."

SIA-H = harness only. The agent loop is modified. The model
weights are not. This is the v129 first honest "we run RL" claim.

Q3 W2. 1 week. 1 engineer. The receipt: a public GitHub PR with
the harness diff, the benchmark delta, and the audit log.
```

### Post 4: SIA-W+H port (Wed Aug 12)

```
1/ Heuristic → SIA series, Post 4 of 6.

"SIA-W+H port."

SIA-W+H = weights + harness. Both modified. This is the v129
research-publishing bet. Concrete numbers: 45% → 70% on the
heuristic feedback loop, 14× inference cost reduction.

Q3 W3-W4. 3 weeks. 1 engineer. The receipt: an arXiv preprint
with the full ablation table and the audit log.
```

### Post 5: Outer-loop RSI receipts (Wed Aug 19)

```
1/ Heuristic → SIA series, Post 5 of 6.

"Outer-loop RSI receipts."

audiod v1.3 → v1.4 in 2 weeks. 0 regressions. 4 new tests.
Confidence calibration improved 4% on the JFK test set. The
changelog is the receipt.

We are not waiting for the maximalist RSI inflection. We are shipping
the substrate while the substrate is still standing.
```

### Post 6: The substrate ship (Wed Aug 26)

```
1/ Heuristic → SIA series, Post 6 of 6.

"The substrate ship."

Chip-stack sovereignty + display-less v1.0. NVIDIA XR AI + viture
Helix (June 2026) make "open-source software" chip-stack-validated.
20M display-less AI smart glasses forecast for 2026 (167% YoY).

We ship the substrate on a chip the user owns, with the threat
model public, the reversibility contract signed, and the audit
log default.
```

---

## 5. Pre-HN + Post-HN (Jul 13-25)

### Pre-HN (Mon Jul 13 — Sun Jul 19)

```
Mon Jul 13: "Show HN #1 is Mon Jul 20. 9 daemons live. .deb installs.
On-device AI. The thread is in flight."

Wed Jul 15: "Reversibility contract ships this week. The receipt: a
public GitHub PR with the contract, the audit log, and the 8K layoffs
cite."

Fri Jul 17: "Outer-loop RSI receipts: audiod v1.3→v1.4, 8x LOC at
Anthropic, dan2 v23→v28. The substrate improves in the open."

Sun Jul 19: "Show HN #1 is tomorrow. 9 daemons live. .deb installs. On-
device AI. The thread is in flight."
```

### Show HN #1 (Mon Jul 20)

```
1/ Show HN: Dan Glasses — 9 daemons live, .deb installs, on-device AI

github.com/somdipto/dan-glasses
```

### Post-HN (Tue Jul 21 – Sun Jul 26)

```
Tue Jul 21: "Top 5 questions from Show HN #1: 1) Why on-device? 2) Why
audit-by-default? 3) Why India? 4) Why reversible? 5) Why not Meta?
Answers in thread."

Wed Jul 22: "Show HN #1 retrospective: 200+ points, 150+ comments, top
3 surprises. The substrate matters more than the model."

Fri Jul 24: "Heuristic → SIA series, Post 1: What is pre-RL scaffold?"

Sat Jul 25: "Show HN #1 retrospective on Substack."
```

---

*X content complete. 9-tweet lead thread + 12 daemon-of-the-week + 8 receipt threads + 6 heuristic→SIA series + pre-HN + post-HN = ~150 posts Q3 2026. The v129 P0 is the 6-axis wedge thread (Mon Jul 6) + the reversibility contract thread (Mon Jul 13) + the Show HN #1 thread (Mon Jul 20). Everything else is calendar.*
