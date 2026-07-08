# Dan Glasses Architecture Review — v101 (Dan2, 2026-06-29)

**Author:** Dan2 (👾) | **Source:** 5-service SPECs + canonical analysis + v101 research
**Verdict:** Architecture is **structurally correct but functionally incomplete**. Two missing services block the product thesis.

---

## TL;DR

The 5-service decomposition (audiod / perceptiond / memoryd / toold / ttsd + OpenClaw gateway) is **the right shape** — it matches the agent-OS pattern Letta, Hermes, and OpenAI's agent SDK all converged on. Three problems to fix:

1. **No `learningd`** — without it we don't have self-improvement. This is the product bet.
2. **No `proactived`** — without it we don't have a companion. We have a chatbot.
3. **No service-mesh discipline** — mTLS, protobuf contracts, back-pressure, degradation policies are all absent.

Plus one structural redundancy to fix:
4. **Fast-path that skips memoryd** for trivial lookups (object detection, OCR).

---

## A. What's right (keep this)

### A1. Service decomposition matches the agent-OS pattern

| Our service | Letta equivalent | Hermes equivalent | OpenAI agent SDK equivalent |
|---|---|---|---|
| audiod | (external I/O) | terminal backend | tool input |
| perceptiond | persona model | context retrieval | vision tool |
| memoryd | core memory + archival | 4-layer memory | thread history |
| toold | tool call | function calling | function tools |
| ttsd | (external I/O) | chat transport | assistant output |
| OpenClaw | agent loop | gateway | runner |
| **— missing —** | **memory controller (RL-trained)** | **Skills system** | **memory tool** |
| **— missing —** | **scheduler** | **automations** | **trigger queue** |

Our decomposition is a strict subset of what's working in 2026. The gaps are precisely where we need to invest.

### A2. Locked model choices are correct

- **LFM2.5-VL-450M** for vision (Apr 2026, SOTA in class, bbox + function-calling, sub-250ms edge). ✓
- **whisper.cpp** for STT (whisper-tiny.en for floor, whisper-base for comfort). ✓
- **HRM-Text 1B** for reasoning planner. ⚠️ Caveat below.
- **OpenClaw (Bun/TS)** for gateway. ✓ Right tool for orchestration.
- **Tauri v2 + React** for client. ✓ Right tool for desktop-quality mobile app.

### A3. MCP-first interop future-proofs us

By making audiod / perceptiond / memoryd / toold / ttsd expose MCP endpoints, we instantly interop with 9,400+ MCP servers in 2026 (per digitalapplied / arxiv 2503.23278). This is the cheapest interop we can buy.

---

## B. What's wrong (fix this)

### B1. ⚠️ No `learningd` — the product bet is missing

**Problem:** Danlab's thesis is "AI that improves from use." The current architecture has `memoryd` that stores facts but **no service that improves the harness over time**. Without learningd, we are the same as every other chatbot.

**Reference:** Hermes Agent's Skills system (Nous, May 2026) is the canonical reference. Closed loop: extract what worked → write as Skill → reload on next similar interaction. Cache-aware so it doesn't grow the token bill. Bounded Skills store.

**Proposed spec shape for learningd:**

```
learningd
  - inputs: interaction logs from memoryd, user ratings (explicit + implicit)
  - state: Skills store (procedural memory), reward model (small, RL-trained)
  - outputs: new Skills (consumed by perceptiond/toold), updated reward weights
  - cadence: nightly extraction, weekly Skill promotion
  - owner: Dan4 (memoryd), assisted by Dan2 (eval harness)
```

**Why not a "self-rewriting" service in v1?** DGM-style self-modification is research-grade. The v1 bet is the *narrower* but shippable claim: skills extraction + RL-trained reward model. We expand to self-rewriting in 12 months.

### B2. ⚠️ No `proactived` — a glasses companion that doesn't initiate isn't a companion

**Problem:** The current architecture is purely request-response. Audiod captures speech → OpenClaw routes → response is rendered. The glasses do nothing when not spoken to. This isn't a companion. This is a voice assistant.

**Reference:** The "AI Purists" tribe (Solos AirGo V, Brilliant Labs Halo) all do *some* proactive behavior. The state-of-the-art is event-driven scheduling with salience weighting.

**Proposed spec shape for proactived:**

```
proactived
  - inputs: audiod events (doorbell, name spoken), perceptiond events ("phone detected in pocket"), calendar, time-of-day
  - state: salience model (small, learns from user dismissals), event log
  - outputs: interjection triggers sent to OpenClaw → perceptiond → ttsd
  - cadence: real-time for audiod, near-real-time for perceptiond
  - guardrails: quiet hours, learn from dismissal rate, never interject during conversation
  - owner: Dan2 (gateway/eval), assisted by Dan3 (perception)
```

**Why this matters for retention:** users churn on chatbots because there are no compounding benefits over time. A proactive companion that says "you've been looking at your phone for 20 minutes, want me to start focus mode?" — that's sticky. That's daily.

### B3. ⚠️ No service-mesh discipline — operationally fragile

**Problems:**
- mTLS between services: not specified
- protobuf contracts: services speak JSON/HTTP, fragile
- Back-pressure: what happens if perceptiond is slow?
- Degradation policy: what does the product do when whisper.cpp OOMs?
- Restart storms: 5 services bootstrapping at boot can deadlock
- Logs: structured logging with trace IDs is not specified

**Minimum viable mesh (v1 must-have):**
- protobuf + buf for service contracts
- mTLS (or local Unix socket for v1 single-device, mTLS for multi-device)
- Health endpoints + a 10s retry-with-exponential-backoff policy
- Structured logs with trace_id propagated from OpenClaw
- A degradation policy per service ("if X fails, fall back to Y")

**Owner:** Dan1 (ops + gateway), with input from Dan2 (eval).

### B4. ⚠️ Fast-path that skips memoryd

**Problem:** perceptiond → memoryd → ttsd is the round-trip for every query. For trivial lookups ("what's in front of me?", "read this text aloud"), the latency cost of memoryd retrieval is unnecessary.

**Proposal:** introduce a fast-path
**Proposal:** introduce a fast-path:
- `perceptiond.fast_query(image, prompt)` → returns text in <300ms without memoryd write
- `perceptiond.deep_query(image, prompt, conversation_id)` → returns text + writes to memoryd
- OpenClaw chooses based on prompt type (heuristic + LLM classifier)
- Result: trivial lookups feel instant; meaningful exchanges get memoryd grounding

**Expected outcome:** P50 conversation latency drops from ~1.5s to ~1.0s for many flows.

---

## C. Bottlenecks (ranked)

| Rank | Bottleneck | Severity | Mitigation | Owner |
|---|---|---|---|---|
| 1 | perceptiond combined audio+vision latency | High | LFM2.5-VL-450M Q4_0 + parallel audio pre-decode | Dan3, Dan2 |
| 2 | End-to-end conversation latency memoryd+perceptiond+ttsd | High | Fast-path bypassing memoryd | Dan2 |
| 3 | learningd Skill extraction cadence | Medium | Nightly batch, weekly promotion, on-device eval | Dan4 |
| 4 | ttsd first-byte latency | Medium | Switch to Kokoro-82M (~96× realtime GPU, stream first chunk) | Dan2 |
| 5 | memoryd vector search latency as store grows | Medium | Tiered HNSW (in-mem < 10K) + sqlite-vss (warm) | Dan4 |
| 6 | proactived salience model latency | Medium | Run small classifier (< 50M params) on frame events | Dan2 |
| 7 | toold permission decisions on each call | Low | Cache last-granted tools per session | Dan2 |
| 8 | OpenClaw gRPC overhead (if used) | Low | Local Unix socket for v1 | Dan2 |

---

## D. Failure modes (top 5 + responses)

1. **audiod crashes mid-conversation.**
   *Detection:* health endpoint stops responding.
   *Response:* OpenClaw restarts audiod, replays last 5s of audio from buffer, continues if context recoverable; asks "sorry, could you repeat that?" if not.

2. **perceptiond OOMs on long video.**
   *Detection:* OOM killer signal in logs.
   *Response:* perceptiond auto-shrinks input to 256×256, returns warning to OpenClaw. OpenClaw surfaces "vision limited" status.

3. **memoryd SQLite corruption.**
   *Detection:* integrity check on boot fails.
   *Response:* restore from last good snapshot, replay last 24h from episodic log.

4. **toold returns capability exceeded.**
   *Detection:* RPC error pattern.
   *Response:* OpenClaw downgrades to safe tool subset, falls back to "let me look that up" reply.

5. **HRM-Text produces nonsensical plan.**
   *Detection:* chat-head perplexity threshold.
   *Response:* fall back to chat-head baseline plan, log for offline analysis.

---

## E. Dependency asymmetry to fix

perceptiond depends on toold (function calling) but currently ttsd receives perceptiond output through memoryd. This means ttsd is *always* memoryd-bound. Replace with:

```
OpenClaw
  ├─ perceptiond.fast_query → ttsd (skip memoryd)
  ├─ perceptiond.deep_query → memoryd → ttsd
  └─ proactived.trigger → perceptiond → ttsd
```

This decouples the three patterns. Cleaner, faster, easier to instrument.

---

## F. Recommended additions for v1 (prioritized)

| Priority | Service | Owner | Cost | Payoff |
|---|---|---|---|---|
| P0 | **learningd** | Dan4 | ~2 weeks | The product bet — self-improvement |
| P0 | **proactived** | Dan2 | ~2 weeks | The product bet — companion not chatbot |
| P0 | protobuf contracts | Dan2 | ~1 week | Removes a class of integration bugs |
| P1 | Fast-path perceptiond | Dan3, Dan2 | ~3 days | Halves latency for trivial queries |
| P1 | degradation policies per service | Dan1 (ops) | ~1 week | Resilience to OOM/crash |
| P1 | SIA-eval harness wired into all services | Dan2 | ~2 weeks | Measurement-driven improvement |
| P2 | MCP exposure for public services | Dan2 | ~1 week | Ecosystem interop |
| P2 | Open-source reproducibility audit | Somdipto | ~1 week | "Yours, not theirs" story |

---

## G. What NOT to add to v1

- **robot / drone / embodied-AI integrations** — out of scope. Glasses only.
- **cloud sync of memories** — privacy story fails. Local-first only.
- **weight updates on device** — training infra is huge. Use SIA-style harness updates.
- **unified multimodal model (late-fusion VLM)** — modular is correct for edge.

---

## H. Open questions for somdipto

1. **HRM-Text chat head.** Which model? LFM2.5-1.2B-Instruct (best small chat), Phi-4-mini (best reasoning), fine-tune HRM-Text on chat?
2. **Multilingual at launch.** v1 English-only or English+Hindi? Affects TTS (KittenTTS multilingual vs Kokoro English-only) and STT (whisper-tiny vs whisper-tiny.en).
3. **Proactived aggressiveness.** Conservative vs aggressive? Affects retention curve shape.
4. **Brilliant Labs Halo.** Their re-launch is the closest competitor. Differentiate on openness+privacy, or capability?
5. **MCP exposure timing.** Ship MCP endpoints in v1 or wait for ecosystem stability?

---

## v101 changes from v100

- Added **learningd** and **proactived** as P0 additions.
- Pinned **fast-path perceptiond** design.
- Tightened failure-mode table to top 5 with concrete responses.
- Added **dependency asymmetry fix** (Section E).
- Pinned **service-mesh minimum viable requirements** (Section B3).
- Added **v1 additions prioritization table** (Section F).
