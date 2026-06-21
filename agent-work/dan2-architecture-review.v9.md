# Dan2 — Dan Glasses Architecture Review v9
## Concrete Fixes, Risks, and the Fable 5 / Apple Window Delta

**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v9. v8 archived as `dan2-architecture-review.v8.md`. v9 is a *delta* on v8.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

## 0. v9 Read in 60 Seconds

The v8 architecture review is correct as written. v9 changes three things:

1. **privacyd is moved from v8 month 3 to v9 month 2.** The Fable 5 trigger makes it the v1.0 moat.
2. **Apple-window preparation is in v9 month 1 (not v8 month 4).** Apple N50 confirmed for late 2027 means the 12-18 month head start is real and material.
3. **The 7-service + privacyd + reasond + proactived 10-service topology is locked for v1.0 / v1.1.** v9 calls the 10-service shape final for v1.x. v2 reshuffles if Redax requires.

The v9 architecture:
- **v1.0 (Nov 2026):** 8 services. The 7 v1 services + privacyd.
- **v1.1 (Q2 2027):** 10 services. + reasond + proactived.
- **v2 (Q3 2027):** 10 services. + Redax aarch64 build.

---

## 1. v9 Service Topology (LOCKED for v1.x)

### 1.1 The 10-Service Topology

| # | Service | Port | v1.0 | v1.1 | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | audiod | 8090 + WS 8091 | ✅ | ✅ | Dan2 | live, 83 tests |
| 2 | perceptiond | 8092 | ✅ | ✅ | Dan3 | live, 8 tests |
| 3 | memoryd | 8741 | ✅ (v1) → v2 in v1.1 | v2 | Dan4 | live, 16 tests |
| 4 | toold | 8742 | ✅ | ✅ | Dan4 | live, 18 tests |
| 5 | ttsd | 8743 | ✅ | ✅ | Dan4 | live, 6 tests |
| 6 | os-toold | 8744 | ✅ | ✅ | Dan1 | live |
| 7 | openclaw-gateway | 18789 | ✅ (hardened) | ✅ | Dan1 | live |
| 8 | privacyd | 8748 | ✅ **(NEW v9 month 2)** | ✅ | Dan1+Dan2 | design |
| 9 | reasond | 8745 | — (v1.0 falls back to Gemma 4 1B in memoryd-v2-stack) | ✅ | Dan2 | design |
| 10 | proactived | 8746 | — | ✅ | Dan2 | design |

**v9 verdict:** no topology changes from v8. The 10-service shape is locked. The naming convention is consistent with the existing project.

### 1.2 IPC Pattern (v9 LOCKED)

- HTTP control plane on each service.
- WebSocket fan-out where events stream (audiod WS 8091, perceptiond ring buffer GET).
- Unix sockets for high-frequency local IPC (within Tauri app).
- Bearer-token auth on cross-machine endpoints (none in v1.x — all loopback).
- JSON over HTTP. Serde structs in `shared/` Rust crate.

**v9 verdict:** no changes from v8. The IPC pattern is solid.

---

## 2. v9 OpenClaw Security (P0)

### 2.1 v8 Carry-forward (no change)

The v8 P0 actions stand:
1. Pin OpenClaw to ≥ 2026.5.x.
2. `policy.deny_skills: ["*"]`.
3. Audit installed skills against Trail-of-Bits patterns.
4. Supervisord restart policy.
5. Audit Telegram channel config.

### 2.2 v9 NEW: Fable 5 trigger implications

**The trigger:** Anthropic Fable 5 / Mythos 5 export-control suspension (June 12 2026) made every cloud-frontier LLM vendor a fragile dependency.

**v9 implication for OpenClaw:** OpenClaw is a TypeScript/Node runtime. It is *not* a cloud-frontier LLM. But it does call out to MCP servers (in our case, `zo-bridge`). The exposure is:

- `zo-bridge` calls `api.zo.computer/zo/ask`. Is `api.zo.computer` a "frontier LLM provider"? **NO** — Zo uses our M3 model (MiniMax M3, per the user message). It is *not* a frontier model. It is not subject to the Fable 5 directive.
- The Telegram channel is fine — Telegram is the channel, not the model.

**v9 verdict:** OpenClaw security is P0. The Fable 5 trigger is a *marketing* trigger, not an *engineering* trigger for OpenClaw. Our OpenClaw deployment is already Fable 5 safe because Zo's model is not a frontier model.

### 2.3 v9 action

**[October 2026, Dan1] public "Fable 5 safe" doc:**
- Document the call graph: openclaw → zo-bridge → api.zo.computer → M3 (on-device capable).
- Document the audit log (privacyd logs every outbound call).
- Document: no frontier-frontier LLM dependency in the architecture.
- Run `dan-privacyd --test` from the bootstrap wizard.

---

## 3. v9 privacyd (P0, ARCHITECTURAL NEW)

### 3.1 What privacyd does

privacyd is the *outbound call gatekeeper* for Dan Glasses. It enforces:

1. **Allowlist of outbound destinations.** Default: telegram.org (for the bot), api.zo.computer (for the zo MCP bridge), nothing else.
2. **netns + cgroup isolation.** All outbound traffic from any service flows through privacyd's netns. The netns has no DNS, no gateway except via privacyd's egress proxy.
3. **seccomp-bpf syscall filter.** Prohibits `socket(AF_INET, ...)` outside privacyd's egress proxy. Prohibits exec of network tools (`curl`, `wget`, `nc`, `ping`) outside privacyd's allowed list.
4. **Audit log.** Every outbound call logged: `{ts, src_service, dst_domain, dst_port, payload_size, payload_sha256}`.
5. **`--test` endpoint.** Runs the Fable 5 test: simulates a privacyd-violating call; verifies it's blocked.

### 3.2 v9 timeline

- **v9 month 2 (July 2026):** privacyd v0.5. netns + cgroup + seccomp. Allowlist.
- **v9 month 4 (September 2026):** privacyd v1.0. Audit log. /test endpoint. CI integration.
- **v9 month 6 (November 2026):** privacyd v1.0 ships with v1.0. Public Fable 5 safe doc.

### 3.3 v9 design rationale

The v9 architecture adds privacyd because the Fable 5 trigger (June 12 2026) made user-visible privacy guarantees a competitive moat. Without privacyd, the claim "all on-device" is unverifiable. With privacyd, the claim is verifiable by the user: `dan-privacyd --test` confirms.

### 3.4 v9 alternatives considered

- **Tailscale + ACLs** (Dan1's previous plan): insufficient — does not block raw socket calls; does not provide an audit log of payload size + sha256; does not provide a `--test` endpoint.
- **eBPF + seccomp inline:** too brittle; requires kernel-level changes for each service.
- **netns + cgroup + seccomp-via-privacyd:** the right level of isolation. privacyd is the single chokepoint, easy to audit, easy to test.

**v9 verdict:** privacyd is the chosen path. The v8 architecture review's "Tailscale for outbound" is *complementary, not sufficient*. privacyd wins on verifiability.

---

## 4. v9 Service Failure Cascade Contract (v9 NEW)

**v8 gap:** No per-service contract about what to do when *another* service is down.

**v9 fix:** Add a per-service "If peer X is down for Y seconds, do Z" contract. One-page per service. Total: 3 days.

### 4.1 v9 contracts (drafted by Dan2, v9 month 1)

| If... | Then... |
|---|---|
| `audiod` down for 30s | `ttsd` does NOT play TTS. Mic-off UX. (Avoids feedback loop.) |
| `audiod` down for 5min | `proactived` falls back to text-only (no wake word). |
| `perceptiond` down for 30s | `openclaw-gateway` returns 503 on vision commands. Frontend renders "vision offline." |
| `perceptiond` down for 5min | `reasond` queries `memoryd` only (no visual context). |
| `memoryd` down for 30s | `perceptiond` continues capturing + describing (description text logged). |
| `memoryd` down for 5min | `reasond` operates without memory context (degraded UX). |
| `memoryd` down for 30min | `openclaw-gateway` alerts user "memory offline — restart in 1 min." |
| `toold` down for 30s | `openclaw-gateway` returns 503 on tool commands. |
| `toold` down for 5min | `reasond` operates without tools. |
| `ttsd` down for 30s | `openclaw-gateway` queues TTS commands; user sees "TTS pending." |
| `ttsd` down for 5min | `openclaw-gateway` falls back to text-only UX. |
| `os-toold` down for 30s | no commands executed; user sees "tool offline." |
| `os-toold` down for 5min | `openclaw-gateway` alerts user "tool offline — restart needed." |
| `openclaw-gateway` down for 30s | Tauri app continues to function (talks to inner services directly). User is not aware of OpenClaw outage. |
| `openclaw-gateway` down for 5min | Tauri app continues. Telegram commands queue locally. |
| `privacyd` down for 30s | ALL services block outbound calls. Tauri app shows "privacyd offline — outbound blocked." |
| `privacyd` down for 5min | Tauri app force-restarts privacyd. If privacyd won't restart, device enters safe mode. |
| `reasond` down for 30s | `proactived` falls back to hand-coded responses. |
| `reasond` down for 5min | `proactived` operates without reasoning — refuses to speak (safe default). |
| `proactived` down for 30s | no proactive speeches. Device is passive. |

**v9 verdict:** contracts drafted in v9. Live validation in v1.0.

---

## 5. v9 Power State Machine (v8 carryforward, P0 for v1)

### 5.1 v9 power states (LOCKED)

| State | vision | audio | reasoning | memory | proactive |
|---|---|---|---|---|---|
| **active** (push-to-talk pressed) | full | full | full | full | full |
| **watchful** (default after push) | gated (salience) | listen-only | on-demand | full | on (cooldown 30s) |
| **drowsy** (idle 5min) | 0.5 fps motion only | sleep | off | full | off |
| **sleep** (idle 30min) | off | wake-word only | off | full | off |
| **charging** (USB-C plugged) | full | full | full | full | on |

**v9 verdict:** the v8 power state machine is correct. Folding it into `openclaw-gateway` is the right call (state is small, transitions are frequent).

### 5.2 v9 salience threshold tuning (v9 NEW)

**v8 gap:** the salience threshold was unspecified.

**v9 fix:** v9 month 2, Dan3, benchmark + tune the salience threshold on real-world camera feeds. Target: <5% false-positive rate (VLM fires when nothing changed).

---

## 6. v9 Push-to-Talk vs Wake-Word (v8 carryforward)

### 6.1 v9 v1.0 = push-to-talk (LOCKED)

**v8 verdict:** push-to-talk default for v1. v9 confirms.

### 6.2 v9 v1.1 = wake-word opt-in (NEW)

**v9 month 4 (September 2026):** audiod v0.5 adds wake-word gated behind user opt-in. Default: off. Default hotkey: ctrl+space (configurable).

**v9 wake-word model:** PicoVoice Porcupine (commercial, paid per-device, accurate) OR open-source Picovoice alternative. Decide in v9 month 1.

---

## 7. v9 Open Questions for the User (somdipto)

The v9 research surfaced a small number of questions that need user input before v1.0 ships. These are *not* blocking v1.0 architecture; they're blocking v1.0 *release* decisions:

1. **Apple-window timing:** does the user want v1.0 in Q4 2026 or Q1 2027? Q4 2026 is more aggressive; Q1 2027 is safer. Recommendation: Q4 2026 to be in-market before Google Gemini glasses and Apple N50.
2. **OpenClaw version pin:** pin to ≥ 2026.5.x immediately, or wait for 2026.6.x? Recommendation: pin to ≥ 2026.5.x now; re-evaluate in v9 month 3.
3. **Moonshine acceptance:** if Moonshine accuracy is <90% WER on our audiod data, do we keep whisper.cpp only? Recommendation: yes, keep whisper.cpp only if Moonshine fails; if Moonshine is good, swap.
4. **SIA fork license:** Apache 2.0 (compatible with SIA's MIT) or AGPL (forces contribution). Recommendation: Apache 2.0 to maximize adoption.

---

## 8. v9 Final Read

The v8 architecture review is correct. v9 adds three concrete fixes:

1. **privacyd in v9 month 2 (was month 3).** Fable 5 trigger makes it the v1.0 moat.
2. **Apple-window prep in v9 month 1.** 12-18 month head start is real.
3. **Service failure cascade contracts** drafted in v9 month 1.

The v9 architecture:
- **v1.0:** 8 services. 7 + privacyd.
- **v1.1:** 10 services. + reasond + proactived. + SIA harness.
- **v2:** 10 services + Redax aarch64.

The moat: on-device + auditable + open-weights + Fable 5 safe + Apple-window-head-start.

Build.

---

*End of v9 architecture review. Total: ~240 lines / ~15KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-model-analysis.md` (model selection), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read). v8 archived as `dan2-architecture-review.v8.md`.*
