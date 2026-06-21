# Dan2 — Dan Glasses Architecture Review
**Date:** 2026-06-14
**Status:** Final v1
**Scope:** Problems, risks, suggested improvements for the Dan Glasses desktop + wearable architecture

---

## 0. TL;DR

The Dan Glasses architecture is **in better shape than the canonical PRD implies**. The 106/106 green tests across 5 daemons + Tauri frontend + OpenClaw gateway make the desktop prototype **demo-ready today**. The canonical PRD is stale on language split (Python daemons, not Rust) and IPC transport (HTTP loopback, not Unix socket). The architecture's biggest gaps are: (1) **no watchdog** on openclaw-gateway, (2) **no wearable silicon characterization**, (3) **memoryd v1 too weak for prod**, (4) **PRD/build plan/implementation have diverged**.

This review does **not** duplicate `ARCHITECTURE-FLAWS-BEFORE-CODE.md` (20 issues from April 2026) or `dan-glasses-v1-canonical-analysis.md`. It re-prioritizes against the **shipped reality** (June 14 2026) and the **2026 AGI/edge-AI landscape**.

---

## 1. What is correct (don't change)

| Decision | Status | Why correct |
|---|---|---|
| **Tauri v2 + .deb + systemd** | Locked | Flatpak/AppImage can't handle systemd, udev, or privileged install. Debian is right. |
| **OpenClaw orchestration (TypeScript/Node)** | Locked | Microsoft Scout is built on OpenClaw. Compliance wedge is the differentiator. |
| **V4L2-first generic camera provider** | Locked | Avoids vendor lock-in. CrabCamera wraps V4L2 for Tauri. |
| **SQLite + Markdown + vectors memory core** | Locked | Only architecture that satisfies offline, inspectable, durable, low complexity. |
| **Model delivery on first run, not in .deb** | Locked | Keep .deb small; download weights on first run. |
| **Service health contracts schema** | Locked | Per-service healthy / degraded / failed states defined. |
| **Failure handling matrix** | Locked | Restart / fallback / degraded / deep recovery paths. |
| **Repo shape (apps/, services/, shared/, packaging/)** | Locked | Clean separation. |
| **Idempotent installer scripts with upgrade preservation** | Locked | Upgrade must not delete user memory. |
| **Salience-based VLM inference gating (perceptiond v4)** | Shipped | Replaces FPS-based throttling. Right lever. |
| **Real RFC 6455 WebSocket (audiod v2.4)** | Shipped | 66/66 tests. Frontend LiveTranscript connects. |
| **Schema-conformance pinned event shape (audiod)** | Shipped | test_event_schema_conformance.py is the contract. |

---

## 2. Critical gaps (must fix before wearable)

### Gap 1: No watchdog on openclaw-gateway or the 6 daemons

**Severity:** CRITICAL
**Location:** `packaging/systemd/` (PRD claims restart policies; not enforced)
**Symptom:** If openclaw-gateway crashes, the entire orchestration layer is dead. The 6 Python daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold) are also unmanaged — they were started manually by dan1 during build.

**Fix (5 minutes):**
```bash
# Register all 7 daemons as supervised services
register_user_service --label "openclaw-gateway" --mode "http" --local_port 18789 \
  --entrypoint "/usr/local/bin/openclaw" --workdir "/opt/openclaw" --public false
register_user_service --label "audiod" --mode "http" --local_port 8090 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/audiod/audiod.py"
register_user_service --label "perceptiond" --mode "http" --local_port 8092 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/perceptiond/perceptiond.py"
register_user_service --label "memoryd" --mode "http" --local_port 8741 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/memoryd/memoryd.py"
register_user_service --label "toold" --mode "http" --local_port 8742 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/toold/toold.py"
register_user_service --label "ttsd" --mode "http" --local_port 8743 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/ttsd/ttsd.py"
register_user_service --label "os-toold" --mode "http" --local_port 8744 \
  --entrypoint "python3 /home/workspace/dan-glasses/Services/os-toold/os_toold.py"
```

**Acceptance:**
- `service_doctor` returns `healthy` for all 7.
- `kill -9` on any daemon → auto-restart within 5 seconds.
- openclaw-gateway crash → session resumes from last checkpoint (need to implement checkpoint persistence, see Gap 2).

**Priority:** **Day 1, not later.**

### Gap 2: No session checkpoint / resume for openclaw-gateway

**Severity:** HIGH
**Location:** openclaw-gateway
**Symptom:** PRD Section 10.3 claims "Session state persisted to memoryd / Auto-restart gateway / Resume session from last checkpoint." This does not exist in code.

**Fix (1-2 days):**
- Persist session state to memoryd on every message turn (id, role, content, metadata).
- On gateway startup, query memoryd for last active session_id.
- Resume by replaying context window from memoryd.
- Add a "checkpoint" heartbeat every 10s.

**Acceptance:**
- `kill -9 openclaw-gateway; sleep 3; gateway auto-restart` → user can continue from last message with full context.

### Gap 3: Canonical PRD is stale vs shipped reality

**Severity:** HIGH
**Location:** `PRD.md`, `docs/dan-glasses-build-plan.md`, `INDEX.md`, `AGENTS.md`
**Symptoms:**
- PRD says "Rust microservices, IPC via Unix sockets" — actual stack is **Python daemons on TCP localhost**.
- INDEX.md says "Services/{perceptiond,audiod,memoryd,os-toold,toold}" — actually 6 (ttsd, zo-mcp-bridge added).
- Build plan says "LFM2.5-VL-450M" as primary vision — actually `SmolVLM-256M` is what's deployed (LFM2.5 download script ready but model not on HF GGUF mirror yet).
- PRD says "develop on x86_64 laptop, deploy on Redax aarch64" — Redax board finalization still TBD.
- PRD says "memoryd uses vectors in-process with optional Qdrant migration" — actually all-MiniLM-L6-v2 in SQLite BLOB, no Qdrant in production.

**Fix (4-6 hours):**
- Reconcile `PRD.md` to match the actual deployed stack (Python daemons + HTTP loopback + LFM2.5-VL-450M-with-SmolVLM-fallback + memoryd with all-MiniLM-L6-v2 + 6 services + openclaw-gateway + zo-mcp-bridge + Tailscale-future).
- Update `INDEX.md` to list all 7 daemons + 2 bridges.
- Add a "PRD reconciliation log" at the top of each canonical doc with the date + what changed.
- Move the "wearable ambition" to a separate `docs/dan-glasses-wearable-v1-spec.md` so the desktop prototype and the wearable don't fight.

**Acceptance:**
- A new engineer can read PRD.md + INDEX.md + AGENTS.md and know exactly what's running on the laptop prototype, with no contradictions.

### Gap 4: VLM power draw uncharacterized

**Severity:** CRITICAL for wearable, MEDIUM for laptop
**Location:** perceptiond
**Symptom:** LFM2.5-VL-450M is the primary vision model, but no power/latency numbers on target hardware (Redax, Hailo-10H, GAP9, Monako Glass). For wearable, this is everything. For laptop, it's AC-powered so less critical.

**Fix (Month 1):**
- $150-500 in dev kits: **Hailo-10H M.2** + RPi 5, **GAP9 dev kit** + Prophesee GENX320.
- Measure LFM2.5-VL-450M Q4_0 on Hailo-10H, SmolVLM-256M on GAP9, VLMCache + V5e-0 in perceptiond.
- Lock sub-1W wearable path by end of Month 1.

**Acceptance:**
- Measured: watts, ms latency, FPS, accuracy degradation, thermal envelope.
- Form factor decision tree locked.

### Gap 5: memoryd v1 too weak for production

**Severity:** HIGH
**Location:** memoryd, port 8741
**Symptom:** Single embedding model (all-MiniLM-L6-v2, 384d), no temporal index, no skill consolidation, no proactive retrieval, no dual-process (System 1/System 2), no visual memory, no proactive agent behavior. Good for prototype, not for v1 wearable.

**Fix (Month 3):** memoryd v2 v1.0 — see `dan2-model-analysis.md` and `dan2-agi-roadmap.md` for full design.
- 6-core stack: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram
- 12-16 weeks, 1 ML engineer, $0 compute
- Open-source release target: September 2026

### Gap 6: No latency SLOs

**Severity:** MEDIUM
**Location:** All daemons
**Symptom:** audiod SPEC has 400-700ms end-to-end target. perceptiond has sub-250ms. memoryd, toold, ttsd, os-toold have no SLOs. No p95 measurements. No alerting when SLO violated.

**Fix (1 week):**
- Define p50 + p95 + p99 latency SLOs for every daemon endpoint.
- Instrument with `time.perf_counter()` in each handler.
- Log to Loki with structured fields.
- Add a `daemon_latency_dashboard` panel to the Tauri app.

**Acceptance:**
- Every daemon has documented + instrumented SLOs.
- Tauri app shows real-time latency dashboard.

### Gap 7: No provenance / event-tracing across daemon chain

**Severity:** MEDIUM
**Location:** audiod → memoryd → openclaw-gateway → Telegram
**Symptom:** Each daemon logs locally, but there's no causal chain "user said X → audiod transcribed X → memoryd stored memory Y → openclaw-gateway routed to Telegram Z."

**Fix (1-2 weeks):**
- Every event gets a `trace_id` (UUID) at audiod capture.
- trace_id propagated through memoryd, openclaw-gateway, Telegram.
- Loki query by trace_id returns the full chain.
- Required for: debugging, audit, compliance (OWASP AIUC-1, Agent 365).

**Acceptance:**
- `loki_query(trace_id=X)` returns all events for that trace.

### Gap 8: No security review of perception → os-toold path

**Severity:** HIGH for v1 wearable, MEDIUM for laptop
**Location:** perceptiond → openclaw-gateway → os-toold
**Symptom:** OCR text in camera frames could contain malicious commands. Prompt injection via vision input. PRD mentions "argument hashing and audit log" but not input sanitization.

**Fix (2-4 weeks):**
- Sanitize all OCR text against a denylist before passing to os-toold.
- Add prompt-injection guard for VLM outputs (DUAL-Bench-style evaluation).
- Add per-user allowlist for os-toold commands.
- Audit log every os-toold invocation with trace_id + source frame.
- Required for: Microsoft Scout compliance wedge (OS-toold v2 GA target Month 3).

**Acceptance:**
- DUAL-Bench over-refusal rate <5% on adversarial vision inputs.
- All os-toold invocations have audit log entries.

### Gap 9: Bootstrap wizard underspecified

**Severity:** MEDIUM
**Location:** `apps/dan-glasses-app/src/components/BootstrapWizard.tsx`
**Symptom:** 7-step wizard exists (memoryd, toold, ttsd, audiod, perceptiond, TTS playback, memory write) but no state machine for retries, no offline skip behavior, no first-run failure recovery.

**Fix (1-2 days):**
- State machine with retry/timeout/fallback per step.
- Skip behavior for offline + offline-only installs.
- First-run failure recovery (which step failed → which daemons are unhealthy → can user proceed degraded?).

**Acceptance:**
- Wizard handles 100% failure modes gracefully (camera permission denied, model download fails, microphone blocked, etc.).

### Gap 10: Wake word implementation path unclear

**Severity:** MEDIUM
**Location:** audiod
**Symptom:** v1 is push-to-talk only. Wake word deferred to v1.5. No feature gate architecture. No audio pipeline diagram showing wake word insertion point.

**Fix (v1.5, defer):**
- Add `wakewordd` service (separate from audiod) with Silero VAD-style on-device model.
- Audio pipeline: mic → wakewordd (always-on) → audiod (VAD + STT) → ...
- Spike in v1.5 (Month 6-9).

**Acceptance:**
- "Hey Dan" wake word <500ms latency, <5% false positive rate on 100h test set.

### Gap 11: Package signing mechanism undefined

**Severity:** LOW (defer to v1.5)
**Symptom:** PRD Section 12 says "sign package" but mechanism not specified.

**Fix (defer):**
- Sigstore (preferred for open-source + GPG key management is a pain).
- Detached checksums/signatures for downloaded models.

**Acceptance:**
- .deb signed with Sigstore, verification step in install wizard.

### Gap 12: IPC transport not locked to Unix socket

**Severity:** LOW
**Symptom:** PRD says "Unix socket or gRPC." Actual stack: HTTP on TCP loopback.

**Decision:** **Keep HTTP on TCP loopback.** Reasons:
- FastAPI + Tauri Rust + TypeScript WS all natively support HTTP. No Unix socket FFI complexity.
- localhost:port is just as fast as Unix socket for this use case.
- Easier debugging (curl from terminal).
- Future Tailscale Serve exposure is HTTP-native.

**Don't change.** Update PRD to match.

### Gap 13: No GPU/NPU acceleration path defined for wearable

**Severity:** CRITICAL for wearable
**Symptom:** LFM2.5-VL-450M inference — is there a GPU? NPU? CPU only? On aarch64 wearable, GPU is likely needed.

**Fix (Month 1):**
- Spike LFM2.5-VL-450M on Hailo-10H M.2 (sub-1.5W target).
- Spike SmolVLM-256M on GAP9 + event camera (sub-1W target).
- Pick the path by end of Month 1.

---

## 3. Wearable-specific gaps (the open questions)

### Gap 14: Form factor constraints undefined

**Severity:** CRITICAL for wearable
**Symptom:** No target weight, no PCB dimensions, no temple/arm thickness, no battery placement.

**Fix (Month 1):**
- Pick a form factor: **Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP**.
- Measure: weight, dimensions, battery, thermal.
- Document physical constraints in `docs/dan-glasses-wearable-v1-spec.md`.

**Default plan (until measured):**
- **Weight target:** <50g (matches Monako Glass, Brilliant Labs Halo)
- **Battery life target:** 4-6h at 5W average (PRD says 4h; canonical says 6h; reconcile)
- **BOM target:** $149-349 (Brilliant Labs Halo $349, Monako Glass $399 — the open-source AI glasses price class)
- **Display:** None for v1 (camera + voice only, like Brilliant Labs Halo). Display glasses v2 in 2027+.

### Gap 15: Sub-1W wearable path unmeasured

**Severity:** CRITICAL for wearable
**Symptom:** All power draw estimates in PRD are planning estimates. OpenGlass achieves 11.8h on 200mAh = sub-1W. Monako Glass 4h on 300mAh = ~0.3W average screen-on.

**Fix (Month 1):**
- Measure LFM2.5-VL-450M on Hailo-10H. Sub-1.5W sustained at 4 FPS = wearable path locked.
- Measure SmolVLM-256M on GAP9 + event camera. 11.8h on 200mAh = sub-1W path validated.
- Document measurements in `docs/dan-glasses-wearable-power-budget.md`.

### Gap 16: Thermal management undefined

**Severity:** HIGH for wearable
**Symptom:** PRD says "Max surface temperature 40°C, passive cooling only." But no thermal model.

**Fix (Month 1):**
- Spreadsheet thermal model: power × time × thermal mass = temperature.
- Validate with actual measurement on the dev kit.
- Define thermal throttle: drop to minimal model (Gemma 4 1B or similar) at 42°C.

**Default plan:**
- **Sleep:** 0.5W (camera off, mic ready)
- **Watchful:** 2W (2 FPS capture, no VLM)
- **Active:** 5-8W (VLM on salient frames only)
- **Burst:** 8-13W (TTS + VLM spike)
- **Drowsy:** 0.3W (no VLM, motion detection only)
- **Deep sleep:** 0.1W (camera off, audiod off)

### Gap 17: VLM fallback path undefined

**Severity:** MEDIUM
**Symptom:** PRD mentions "Gemma fallback" but doesn't define activation/deactivation logic.

**Fix (Month 2):**
- VLM ladder: LFM2.5-VL-450M (primary, 209MB) → Gemma 4 1B (thermal fallback, ~1GB) → text-only (extreme fallback, no VLM at all).
- Auto-detect thermal pressure (CPU temp sensor or power monitor).
- Smooth handoff: when thermal threshold reached, pre-warm fallback model in background.

### Gap 18: 8GB RAM minimum — achievable in glasses?

**Severity:** HIGH for wearable
**Symptom:** PRD says "8GB preferred, 4GB minimum for reduced profile." Most consumer smart glasses have 2-4GB.

**Decision:**
- For 2026 wearable, target **4GB LPDDR5** (achievable in Monako Glass-class form factor).
- For 2027 wearable, 8GB LPDDR5X with BitNet-VLM.
- For 2028+ wearable, 16GB with full multimodal.

### Gap 19: Storage weight tradeoffs undefined

**Severity:** LOW
**Symptom:** 128GB eMMC vs 64GB vs 32GB — no minimum viable storage defined.

**Decision:**
- **Primary:** 64GB eMMC (Brilliant Labs Halo reference, sufficient for models + memory + logs).
- **Storage hierarchy:** models (1GB LFM2.5-VL + 74MB whisper + 25MB KittenTTS + 90MB memoryd embeddings) + memory (10K memories × 1KB each = 10MB, scalable) + logs (Loki-rotated, 1GB max).
- **Don't store raw video frames.** Salient events only, descriptions in memoryd.

### Gap 20: Degraded service modes for wearable

**Severity:** MEDIUM
**Symptom:** Section 7.8 says "perceptiond and audiod may enter degraded mode" but never defines WHAT / WHEN / HOW.

**Fix (Month 1):**
- Per-service degraded matrix:

| Service | Healthy | Degraded | Failed |
|---|---|---|---|
| perceptiond | Camera + VLM responding | Camera only (2 FPS, no VLM) | No frames (camera off) |
| audiod | Mic + VAD + STT | Mic only (VAD on, no STT) | No audio (mic off) |
| memoryd | SQLite + vectors | SQLite only (no embeddings) | No memory (read-only) |
| toold | TTS responding | Slow synthesis (medium model) | No output (text fallback to Telegram) |
| os-toold | Commands executing | Slow exec (timeout 30s) | Blocked (deny-by-default) |

- UI: Tauri app shows degraded state in DaemonHealth.tsx.
- Recovery: auto-restart on health endpoint timeout.

---

## 4. AGI / self-improving gaps (for the wearable's intelligence layer)

### Gap 21: memoryd v2 v1.0 (the September 2026 bet)

**Severity:** CRITICAL for the AGI roadmap
**Fix:** See `dan2-agi-roadmap.md` Month 3.

### Gap 22: SIA-H fork in `danlab-multimodal`

**Severity:** HIGH
**Fix:** Fork SIA (arXiv 2605.27276, May 2026, MIT) into `danlab-multimodal`. 2-week experiment, single ML engineer, $0 compute. Validate the +25% on a Dan Glasses-relevant benchmark (e.g., desktop screen understanding).

**Acceptance:**
- `danlab-multimodal` runs SIA-H on SmolVLM-256M.
- Harness updates are logged.
- Weight updates are deferred to SIA-W+H spike in Month 3.

### Gap 23: SkillOpt integration for Dan1/Dan2/Dan3/Dan4

**Severity:** HIGH
**Fix:** Anthropic SkillOpt + Microsoft SkillOpt (both Build 2026 / Fable 5 launches, June 2 / June 9 2026) treat skill-document evolution as a first-class primitive. Implement the skill-document evolution loop for the 4 Dan agent workspaces.

**Acceptance:**
- Dan1, Dan2, Dan3, Dan4 each have a SKILL.md that is versioned, with provenance, with verifier-graded evolution.
- Skill document is trainable. "Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters."

### Gap 24: Compliance wedge for v1 wearable (os-toold v2)

**Severity:** HIGH
**Fix:** os-toold v2 with OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft Agent 365 + MXC + Apple Core AI compliance. Ship by end of Month 3.

**Why:** Microsoft Scout runs on OpenClaw. The compliance wedge is open-source on top of the same runtime. Microsoft Scout "addicted users" memo leak (404 Media, June 4-9 2026) opens the regulatory window.

**Acceptance:**
- os-toold v2 passes OWASP AIUC-1 controls.
- Microsoft Agent 365 compatibility for Scout-like agents.
- Apple Core AI extension skeleton for future iOS-side integration.

---

## 5. AGI roadmap gaps (for the long-term vision)

### Gap 25: No explicit AGI north-star metric

**Severity:** MEDIUM
**Symptom:** SOUL.md and PRD say "advancing AGI" but no measurable north-star.

**Fix:** Adopt **LongMemEval > 70%** as the v1 AGI north-star metric.
- Hindsight achieves 91.4% at scale (research ceiling).
- SuperLocalMemory V3.3 achieves 70.4% zero-LLM (credible open-source target).
- memoryd v2 v1.0 should hit >70% on LongMemEval out of the box.

### Gap 26: No formal safety review of self-improving harness

**Severity:** HIGH (for SIA-W+H in production)
**Symptom:** SIA-H is auditable. SIA-W+H is not (per the Hexo Labs paper, weight updates can be poisoned).

**Fix:**
- Per-user-isolated weights.
- Audit log of every weight delta (with verifier score).
- "Harness Updating Is Not Harness Benefit" (arXiv 2605.30621) — train the focal model to load and follow its own harness.
- PopuLoRA populations (TrueSkill cross-eval) for safety.

**Acceptance:**
- Weight update requires (a) verifier score above threshold, (b) human approval for >5% delta, (c) rollback capability.

---

## 6. Suggested improvements (prioritized)

### Priority 1: Day 1 fixes (5 minutes each)
1. Register all 7 daemons as supervised services (`register_user_service`).
2. Add `daemon_latency_dashboard` to Tauri app.
3. Add `trace_id` propagation across all daemons.
4. Update `INDEX.md` to list all 7 daemons + 2 bridges.

### Priority 2: Week 1-2 (hours-days each)
5. Reconcile `PRD.md` + `INDEX.md` + `AGENTS.md` with shipped reality.
6. Implement session checkpoint / resume for openclaw-gateway.
7. Add latency SLOs + instrumentation to all daemons.
8. Bootstrap wizard state machine (retry, skip, fallback).
9. per-service degraded mode matrix + UI.

### Priority 3: Month 1 (the wearable silicon bet)
10. Buy dev kits: Hailo-10H M.2 + RPi 5, GAP9 dev kit + Prophesee GENX320.
11. Measure LFM2.5-VL-450M on Hailo-10H. Sub-1.5W sustained at 4 FPS = wearable path locked.
12. Measure SmolVLM-256M on GAP9 + event camera. 11.8h on 200mAh = sub-1W validated.
13. Form factor decision tree locked: 4 paths (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP).
14. Fork SIA-H into `danlab-multimodal`. 2-week experiment.
15. Spike Gemma 4 12B Q4_K_M in perceptiond (laptop prototype VLM lock).
16. Spike LFM2.5-Audio-1.5B in audiod + ttsd (end-to-end audio-language).
17. Implement Anthropic SkillOpt + Microsoft SkillOpt for Dan1/Dan2/Dan3/Dan4.
18. Begin AHE + Self-Harness + HarnessForge integration for openclaw-gateway.
19. Begin HeLa-Mem Hebbian distillation study in memoryd v2.
20. memoryd v2 v1.0 design — 6-core stack.

### Priority 4: Months 2-3 (the September 2026 GA wedge)
21. memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public. **The bet.**
22. SIA-W+H spike (harness + weights) in `danlab-multimodal`. Train the 1.2B focal model.
23. PopuLoRA populations in `danlab-multimodal`.
24. os-toold v2 GA with ACS + Agent 365 + OWASP + Apple Core AI compliance.
25. Brilliant Labs Halo integration or reference design.
26. Microsoft IQ (Work IQ GA June 16) integration as context layer for memoryd v2.
27. VLMCache + V5e-0 in perceptiond (1.4-3.8× VLM speedup).
28. Salience CNN in perceptiond (replace EMA + Haar cascade).
29. Gemma 4 QAT variant spike (72% VRAM reduction).

### Priority 5: Months 4-12 (production + wearable pilot)
30. memoryd v2 v2.0 (11-component stack).
31. Form factor decision + hardware lock.
32. 50-100 wearable pilot users.
33. Open agent standard v1 draft.
34. 10K+ wearable units shipped.
35. 100K+ MAU on desktop companion.

---

## 7. Anti-recommendations (don't do)

1. **Don't rewrite OpenClaw in Rust.** It is correct as TypeScript/Node. The compliance wedge is the differentiator, not the runtime.
2. **Don't call it "RL."** Stay with "pre-RL scaffold" or "self-improving." The semantic war on "RL" labels is real in 2026.
3. **Don't run weight updates in v1.** SIA shows the harness-only path is already +25% on legal, +12% on kernel speed. The "RL" label is earned when (a) harness updates are logged, (b) weight updates are auditable, and (c) both are independently reviewable.
4. **Don't service-ize memoryd v2 prematurely.** One process with 3 internal modules (ingest / retrieve / consolidate). Split only if profiling proves the bottleneck at 10K+ memories / 10K+ queries / day.
5. **Don't try to LoRA-tune the user's brain model in v1.** The failure modes are not debuggable. **Context management > weight updates** for personal AI.
6. **Don't pick a wearable silicon path without measuring it.** $150-500 in dev kits is the single most important investment in Month 1.
7. **Don't keep the canonical PRD as the source of truth.** Reconcile the PRD, the build plan, the analysis, and the work pads. Either update the canonical doc to match reality, or flag the wearable ambition as a separate workstream.
8. **Don't bet the wearable path on Snapdragon-class silicon.** It will draw 2-5W sustained. Sub-1W is a GAP9 + event camera (2026) or BitNet-VLM (2027) target.
9. **Don't put OpenClaw on the wearable.** Run it in the user's EigenCloud container (or laptop). The laptop version is fine because the laptop is AC-powered.
10. **Don't ship a 1-bit VLM.** BitNet b1.58 is text-only. The VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.

---

## 8. What's working well (don't change)

- The 106/106 green tests across 5 daemons + Tauri frontend + OpenClaw gateway.
- The salience-based VLM inference gating in perceptiond v4 (the right lever).
- The schema-conformance pinned event shape in audiod.
- The MCP-bridge integration in openclaw (Telegram channel, Zo MCP bridge wired).
- The .deb + systemd + OpenClaw + Tauri v2 + V4L2 + SQLite + vector stack.
- The repository structure (apps/, services/, shared/, packaging/).
- The LFM2.5-VL-450M-with-SmolVLM-fallback approach (graceful degradation when model not on HF mirror).
- The fact that v1 desktop prototype is demo-ready.

---

## 9. Open questions for somdipto

See `dan2-research-report.md` Section 7 (10 open questions).

Top 3:
1. **Target battery life / weight / BOM for v1 wearable?** (PRD says 4h, <50g, $99-149. Industry references: Brilliant Labs Halo 14h, 40g, $349. Monako Glass 4-8h, 48g, $399.)
2. **Ship the desktop prototype first, or the wearable?** (Desktop is demo-ready now. Wearable is 12-18 months out.)
3. **Open-source Dan Glasses now or wait for wearable?** (Brilliant Labs Halo is open-source from day 1. The wedge is stronger if we open-source now.)

---

## 10. Sources

Same as `dan2-research-report.md` Section 8. Key new sources:
- Brilliant Labs Halo (June 2026, $349, 40g, 14h) [^1]
- Monako Glass (Aug 2026, 48g, Linux, $399) [^2]
- OpenGlass (arXiv 2606.07431, June 2026) [^3]
- Microsoft Scout "addicted users" memo leak (404 Media, June 4-9 2026) [^4]
- Microsoft Scout (Build 2026, June 2) [^5]
- Microsoft Work IQ (GA June 16, 2026) [^6]
- Microsoft Project Solara (Build 2026) [^7]
- Apple Siri AI 12GB gate (iOS 27 Sept 2026) [^8]
- Apple Glasses N50 (Late 2027) [^9]
- Anthropic Fable 5 / Mythos (June 9, 2026) [^10]
- METR Frontier Risk Report (Feb-Mar 2026) [^11]
- SIA: Self Improving AI with Harness & Weight Updates (arXiv 2605.27276) [^12]
- BitNet b1.58 (ENERZAi on QCS6490 Hexagon) [^13]
- Litespark (arXiv 2605.06485) [^14]
- VLMCache (ACM 2026) [^15]
- V5e-0 (Self-Speculative Decoding for VLMs) [^16]
- LFM2.5-VL-450M (Liquid AI, May 2026) [^17]
- Hindsight (4-lever memory, 91.4% LongMemEval) [^18]
- SuperLocalMemory V3.3 (70.4% LongMemEval zero-LLM) [^19]
- Mem0 (arXiv 2504.19413) [^20]
- AEL (Agent Evolving Learning) [^21]
- DPCM (Dual-Process Cognitive Memory) [^22]
- LightGMEM (Graph Memory) [^23]
- SkillOpt (Trajectory-Derived Compilation) [^24]
- SkillsVote (Lifecycle Governance) [^25]
- CMM (Cognitive Memory Manager) [^26]
- SkillCompiler (Cross-Platform IR) [^27]
- SkillCompiler's 94.8% proactive trigger rate [^28]
- The Living Wiki (Schema-Driven LLM KB) [^29]
- HERO (Hindsight-Enhanced Reflection) [^30]
- PAM (Parameters as Agentic Memory) [^31]
- TRACE (Capability-Targeted Agentic Training) [^32]
- Meta-Harness (TerminalBench-2 #1) [^33]
- Tenure (89/89 precision, sub-15ms retrieval) [^34]
- VisualMem (arXiv 2605.28806) [^35]
- Decagon Proactive Agents (93% DuetBench) [^36]
- Cognee (self-improving cognify pipeline) [^37]

[^1]: https://quasa.io/video/brilliant-labs-halo-open-source-ai-glasses-for-curious-minds
[^2]: https://www.timesofai.com/news/monako-glass-custom-linux-computer-glasses/
[^3]: https://arxiv.org/abs/2606.07431
[^4]: https://windowsforum.com/threads/microsoft-scout-always-on-work-agent-openclaw-governance-security-risks.421703
[^5]: https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/
[^6]: https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
[^7]: https://arstechnica.com/gadgets/2026/06/microsofts-project-solara-is-an-android-os-designed-for-agents-instead-of-apps/
[^8]: https://www.macrumors.com/2026/05/31/apple-glasses-late-2027-report/
[^9]: https://www.macobserver.com/news/apple-delays-smart-glasses-again-vision-air-still-expected-by-2029/
[^10]: https://www.linkedin.com/posts/kai-t-williams_this-week-anthropics-internal-think-tank-activity-7468690513249107968-hqua
[^11]: https://metr.org/blog/2026-05-19-frontier-risk-report
[^12]: https://arxiv.org/html/2605.27276v2
[^13]: https://www.edge-ai-vision.com/2026/06/running-bitnet-on-qualcomm-hexagon-with-custom-1-58-kernels
[^14]: https://arxiv.org/html/2605.06485v2
[^15]: https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^16]: https://openreview.net/forum?id=GpFgbKW7PR
[^17]: https://huggingface.co/LiquidAI/LFM2.5-VL-450M
[^18]: https://github.com/vectorize-io/hindsight
[^19]: https://github.com/SuperLocalMemory/SuperLocalMemoryV3
[^20]: https://arxiv.org/abs/2504.19413
[^21]: https://openreview.net/forum?id=dtPo105y8x
[^22]: https://openreview.net/forum?id=ywl53zPXu0
[^23]: https://openreview.net/forum?id=FCQR2oceJ1
[^24]: https://openreview.net/forum?id=2ONrrPIFYi
[^25]: https://openreview.net/forum?id=kj068rI9Uh
[^26]: https://openreview.net/forum?id=yCsHQnvvWY
[^27]: https://openreview.net/forum?id=baOeYyuxty
[^28]: https://openreview.net/forum?id=baOeYyuxty
[^29]: https://openreview.net/forum?id=e64EcfHp8L
[^30]: https://openreview.net/forum?id=CFnfsORP7Y
[^31]: https://openreview.net/forum?id=ptIjkWmtl9
[^32]: https://openreview.net/forum?id=p37UqCmcxG
[^33]: https://openreview.net/forum?id=2Tx03Dan7u
[^34]: https://arxiv.org/html/2605.11325v2
[^35]: https://arxiv.org/abs/2605.28806v1
[^36]: https://www.decagon.ai
[^37]: https://www.cognee.ai
