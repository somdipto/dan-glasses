# DAN-2 Architecture Review — v12 (2026-06-26, 12:00 IST / 06:30 UTC)

**Author:** Dan2 (DAN-2, danlab.dev)
**Status:** Supersedes v11 (2026-06-25, 11:30 IST)
**Companion to:** `dan2-research-report.md` v12
**Delta from v11:** Adds HRM-Text-1B integration as a new service (port 8745). Adds reasond to the daemon matrix (8/8 → 9/9). Adds a Prompt-Injection Sanitization Layer between perceptiond → os-toold. Re-prioritizes the P0/P1/P2 fix list.

---

## 0. TL;DR

The Dan Glasses architecture is **fundamentally correct** but has **3 P0 fixes** that need to ship before any new capability work. The HRM-Text-1B integration is **P1 priority** (4-week ship) and is the highest-leverage change in this review. The service decomposition is good; the cross-service contracts are good; the memory schema is good; the IPC transports are good.

**The verdict:** ship the P0 fixes, then ship HRM-Text-1B, then ship audiod RL. In that order.

---

## 1. The current architecture (re-verified this run)

```
┌─────────────────────────────────────────────────────────────────┐
│  Edge / Wearable (Redax aarch64 — planned, not built yet)       │
│  Camera (V4L2) + Mic (ALSA) + Display (planned) + Battery       │
└─────────────────────────────────────────────────────────────────┘
            │                              │
            ▼                              ▼
┌────────────────────────┐    ┌────────────────────────┐
│  perceptiond :8092     │    │  audiod :8090 + WS 8091 │
│  V4L2Capture           │    │  ALSA capture           │
│  SalienceDetector      │    │  Silero VAD             │
│  LFM2.5-VL-450M Q4_0   │    │  whisper.cpp base.en    │
│  (10–15s/frame CPU)    │    │  push-to-talk           │
│  HTTP /status /descs   │    │  HTTP + WS /transcript  │
└────────────────────────┘    └────────────────────────┘
            │                              │
            ▼                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  memoryd :8741  (canonical store)              │
│  SQLite + MiniLM-L6-v2 (384-dim) + episodic/semantic/procedural│
│  HTTP /memories /conversations /query /stats /v1/embeddings    │
└─────────────────────────────────────────────────────────────────┘
            ▲                              ▲
            │                              │
┌────────────────────────┐    ┌────────────────────────┐
│  toold :8742           │    │  os-toold :8744        │
│  sandboxed shell+py    │    │  path guard + allowlist │
│  /exec /exec/python    │    │  (audit-only, no exfil) │
└────────────────────────┘    └────────────────────────┘
            ▲                              ▲
            │                              │
┌─────────────────────────────────────────────────────────────────┐
│                  openclaw :18789 (TS/Node gateway)             │
│  Telegram @danlab_bot + mcporter bridge to Zo MCP              │
│  6 OpenRouter models configured (gpt-oss-20b primary)          │
│  Now Anthropic Claude / OpenAI / DeepMind (Microsoft Scout)    │
└─────────────────────────────────────────────────────────────────┘
            ▲
            │
┌────────────────────────┐    ┌────────────────────────┐
│  ttsd :8743            │    │  dan-glasses-app :8747 │
│  KittenTTS medium      │    │  Tauri v2 React SPA    │
│  HTTP /speak /play     │    │  5 tabs + wizard       │
└────────────────────────┘    └────────────────────────┘

Service count: 8/8 live, 144/144 tests, 0 cloud.
```

**What is correct:**
- Service decomposition is right. audiod, perceptiond, memoryd, toold, os-toold, ttsd, openclaw, dan-glasses-app are independently shippable, independently testable, independently swappable.
- IPC contracts (HTTP + WS) are stable. JSON event schemas are versioned.
- Memory schema (episodic/semantic/procedural, 384-dim MiniLM-L6-v2) is the right starting point.
- OpenClaw as the agent gateway is the right choice (Microsoft Scout validates).
- V4L2-first camera provider model avoids vendor lock-in.
- The 3-mode power state machine (idle/watchful/active) is a good baseline; v11/v12 fixes it with inference-aware gating.
- Tauri v2 + React + .deb + systemd is the right packaging.

---

## 2. P0 fixes — ship before anything new

### P0.1: Inference-aware power gating (the canonical-analysis fix)

**Problem:** perceptiond's "watchful" mode captures at 5 FPS but still fires VLM inference on every salient frame. The canonical analysis correctly identifies that **throttling capture is the wrong lever; throttling inference is the right lever.** VLM is the dominant power event on aarch64.

**Current state:** `_vlm_busy` flag + `MAX_QUEUE_DEPTH = 2` skips frames while busy. This is reactive, not proactive.

**Fix (v12):**
- Add a `frame_gate` module in `perceptiond/salience.py` that:
  - Computes a per-frame salience score (motion magnitude × face presence × novelty vs EMA background).
  - Only enqueues for VLM if `score > frame_gate_threshold` (default 0.4, configurable).
  - Adds a configurable **cooldown** between VLM invocations (default 500ms in watchful, 200ms in active).
- Add a `/mode` body field `frame_gate_threshold` and `vlm_cooldown_ms`.
- Document the new lever in SPEC.md and the canonical architecture.

**Owner:** Dan3. **Effort:** 2 days. **Blocks:** any aarch64 power characterization.

### P0.2: Prompt-injection sanitization between perceptiond → os-toold

**Problem:** OpenClaw sandbox exfiltration (TechTalks, May 18, 2026) demonstrated that perception → tool paths are vulnerable to indirect prompt injection. Our canonical-analysis §15 noted this but didn't fix it.

**Concrete attack class:**
1. User looks at a document that contains the text `echo $(cat ~/.ssh/id_rsa) > /tmp/exfil`.
2. perceptiond's OCR (if enabled) or the LLM summarizing the scene extracts this as "user input."
3. The agent plans to "execute the user's command."
4. os-toold's regex denylist catches `~/.ssh/id_rsa` and blocks.

The denylist is necessary but not sufficient. **It is regex; it is bypassable.**

**Fix (v12):**
- Add a `sanitized` service (port 8746) between perceptiond → os-toold:
  - Input: raw text from any perception source.
  - Output: text with embedded shell commands, URLs, and file paths either escaped or stripped.
  - Implementation: small HRM-Text-1B prompt + a regex pass + a deny-list of dangerous patterns.
  - Or simpler: any text passed to os-toold must come from the user via push-to-talk (audio channel). All other text is treated as data, never as instructions.

**Owner:** Dan2 (proposed). **Effort:** 1 week (simple version) to 3 weeks (HRM-Text-mediated version). **Blocks:** any production deployment with camera + tool calls.

### P0.3: os-toold v2 — capability tokens instead of regex

**Problem:** `os-toold`'s path guard + command allowlist are still regex/glob. Capability tokens (cryptographically scoped, time-bound, auditable) are the 2026 state of the art.

**Fix (v12):**
- `os-toold` v2 issues opaque capability tokens (`cap_xyz123`) per call.
- Each token has: scope (path prefix, command prefix), TTL (default 60s), audit trail.
- Tokens are single-use or N-use (configurable).
- Audit log is append-only and signed.

**Owner:** Dan2. **Effort:** 3 weeks. **Blocks:** OpenClaw sandbox-exfiltration class of attacks.

---

## 3. P1 — HRM-Text-1B integration as new service (reasond :8745)

See `dan2-research-report.md` §3.3 for the 4-week integration plan. Architecture-level changes:

```
┌─────────────────────────────────────────────────────────────────┐
│  NEW: reasond :8745  (HRM-Text-1B Q4_0 GGUF, ~1.2GB RAM)       │
│  HTTP /plan /calibrate /confidence                             │
│  Wired to OpenClaw as primary on-device reasoner               │
└─────────────────────────────────────────────────────────────────┘
```

**IPC contract additions:**
- `reasond.POST /plan {task, context, max_steps}` → `{plan: [{tool, args, rationale}], confidence: float, alternatives: [...]}`.
- `reasond.POST /calibrate {examples}` → `{loss, ece, brier}` (used by SIA-style Feedback-Agent).
- `reasond.GET /status` → `{model, quantization, load_ms, last_inference_ms}`.

**OpenClaw config change:**
- Add `models.local.reasond` provider.
- Set as default for `agent_reason` tool calls.
- Fallback to OpenRouter when reasond confidence < 0.4 (configurable threshold).

**Memoryd schema addition:**
- Add `reasond_plans` table: `(plan_id, task, plan_json, confidence, accepted, feedback, ts)`.
- Enables the SIA Feedback-Agent to write back to memoryd for provenance.

**Owner:** Dan2 (proposed). **Effort:** 4 weeks. **Depends on:** P0.1 (so the new service doesn't compound the power issue). **Unlocks:** audiod RL agent harness reuse, memoryd v2 KG overlay testing.

---

## 4. P1 — audiod confidence RL agent

See `dan2-research-report.md` §2.1. Architecture-level changes:

```
┌─────────────────────────────────────────────────────────────────┐
│  NEW: feedback-agent (in-process, lives in audiod)             │
│  - Collects (transcript, audio_features, whisper_confidence,   │
│    downstream_acceptance) per segment                          │
│  - Trains calibration head with ECE loss on frozen encoder     │
│  - Writes updated head weights to disk every N segments        │
└─────────────────────────────────────────────────────────────────┘
```

**IPC contract additions:**
- `audiod.POST /calibrate {examples}` → `{loss, ece, brier}` (mirror of reasond).
- `audiod.GET /calibration` → `{head_version, ece_on_validation, last_trained_ts}`.

**Librispeech harness:**
- New repo: `danlab/audiod-calibration`. Training data: Librispeech test-clean + CommonVoice Indian-accent English. Eval: ECE, Brier, NLL.
- arXiv paper target: Aug 15.

**Owner:** Dan2 (proposed, already in flight). **Effort:** 6 weeks (2 weeks of which are paper writing). **Depends on:** nothing. **Unlocks:** first Danlab citable artifact.

---

## 5. P2 — memoryd v2 (stage-gated, deferred to Q4)

See `dan2-research-report.md` §2.2 (deferred to Oct 15 in v12).

**v2.0 (Oct 15):** RRF fusion (per memorywire), episodic/semantic/procedural extension, provenance graph.
**v2.1 (Dec 15):** KG overlay (Mem0g-style).
**v2.2 (Q1 2027):** A-MEM composite + Curator role + OpenJarvis-memory adapter.

**Architecture additions:**
- `memoryd` exposes `/v2/memory/remember /v2/memory/recall /v2/memory/forget /v2/memory/merge /v2/memory/expire` per memorywire spec.
- RRF fusion replaces single cosine-similarity recall.
- Provenance graph stored as JSON edges in a `memory_provenance` table.
- KG overlay (v2.1) is a separate store (networkx + sqlite-vss) joined to memoryd by `entity_id`.

---

## 6. P2 — TTS swap (KittenTTS → Kokoro-82M)

Defer to v13. See `dan2-research-report.md` §2.2.

**Architecture change:**
- New `ttsd` v2 service, single-model, single-worker (same pattern as v1).
- Default voice: `af_sarah` (Kokoro-82M has 50+ voices; pick one for v1).
- Migration: audiod `/play` endpoint already points at ttsd; just swap the underlying engine.

**Owner:** Dan2 (proposed). **Effort:** 1 week (already validated in Dan1 v85). **Depends on:** human-eval harness (separate workstream).

---

## 7. Cross-cutting architectural concerns

### 7.1 IPC contract versioning

All services should bump to `/v1/` URLs and start returning `X-API-Version` headers. The current `/memories /query` etc. are unversioned. v12 fix:

- Add `X-API-Version: 1.0.0` to every response.
- Update SPEC.md for each service with explicit version compatibility matrix.
- Write a contract-test harness in `tests/contracts/` that verifies cross-service shapes.

**Owner:** Dan4. **Effort:** 1 week. **Unblocks:** safe evolution of any single service.

### 7.2 Observability

The current logs go to `/dev/shm/` and Loki. We need:

- **Structured logs** (JSON lines, not Python `print`). All services should emit `{ts, service, level, msg, fields}`.
- **Per-service metrics** (p50/p95/p99 latency, queue depth, error rate). Use the existing Loki + add Grafana dashboards.
- **Distributed tracing** (OpenTelemetry-style). Optional for v12; required for v13.

**Owner:** Dan1 (because they're already touching infra). **Effort:** 2 weeks.

### 7.3 Host-restart resilience

The daemons do not survive host restart. STATUS.md documents the manual resume procedure. v12 fix: write a `supervisord` config that brings all 8 (soon 9) services back up automatically.

**Owner:** Dan1. **Effort:** 3 days.

---

## 8. The wearable form-factor gap (re-stated)

The canonical analysis correctly flagged that **battery + size + thermal are the constraints that determine whether this is a wearable or a desk device.** v12 has no new information on Redax hardware. Until the board is finalized:

- Develop on x86_64 Linux laptop (canonical analysis Phase 1).
- Target Redax as a *rebuild*, not a *rewrite*.
- Validate power budget on laptop with `powertop` / `perf` / `turbostat`.
- Use the laptop prototype as the user-facing demo for Show HN Aug 25.

---

## 9. Decisions for somdipto

1. **P0.2 scope:** regex denylist hardening (1 week) vs HRM-Text-mediated sanitization (3 weeks)?
2. **P0.3 scope:** capability tokens in-process (3 weeks) vs hardware-backed (TPM/SE, 8 weeks)?
3. **HRM-Text ship timing:** parallel with audiod RL (v12 plan) or sequential (HRM-Text first)?
4. **Open-source the capability-token scheme** to the OpenClaw community as an upstream PR?
5. **Approve the stage-gated memoryd v2 schedule** (v2.0 Oct 15, v2.1 Dec 15, v2.2 Q1 2027)?

---

## 10. Sources

See `dan2-research-report.md` §8.

---

*Dan2 — Bengaluru 🇮🇳 — 2026-06-26 12:00 IST (06:30 UTC). v12 supersedes v11.*
