# Dan Glasses — Architecture Flaw Review
# Status: Pre-Implementation Critical Review
# Date: 2026-04-17

---

## EXECUTIVE SUMMARY

The architecture is **solid as a Linux desktop app**. The wearable ambition is where it falls apart — power, thermal, and form factor are undefined. 20 issues found across 4 severity levels. 7 are critical and must be resolved before any code is written.

---

## CRITICAL — Will fail or cause major harm

### 1. FPS throttling is NOT VLM throttling
**Location:** Section 10.10 (Adaptive FPS)

Adaptive 2/5/10 FPS caps camera capture rate. But every captured frame still runs:
- Frame gate: 5-20ms
- OCR on candidate frame: 40-150ms
- VLM inference: 150-800ms (LFM2.5-VL-450M)

At 2 FPS idle, you're still firing the full inference pipeline every 500ms. The power lever being adjusted (camera FPS) is not the dominant power consumer (VLM inference).

**Fix required:** Salience-threshold-based inference gate. Frames are captured at low FPS but VLM only fires when frame delta exceeds a threshold. Proper drowsy/sleep state machine as first-class architecture.

---

### 2. No power budget defined
**Location:** Section 10.11

"Keep average low enough for always-on desk mode" — zero numbers. No target watts. No battery chemistry. No battery life target (2h? 4h? 8h?).

For a wearable product this is everything. Without a power budget:
- Cannot size battery
- Cannot select components
- Cannot design thermal management
- Cannot make trade-off decisions (more VLM vs. longer battery life)

**Fix required:** Define target power envelope: target watts, ceiling watts, battery capacity, target battery life.

---

### 3. LFM2.5-VL-450M power draw completely uncharacterized
**Location:** Section 10.3 (Vision Stack)

The spec names LFM2.5-VL-450M as primary vision but gives no power estimate. Critical unknowns:
- Q4_0 quantized or fp16?
- GPU, NPU, or CPU inference?
- Measured latency on aarch64 target?
- Power draw per inference at what batch size?

Without this, VLM can consume 3-15W and the product dies in 30 minutes.

**Fix required:** Benchmark LFM2.5-VL-450M on target hardware (or comparable aarch64 board). Get real power/latency numbers before architecture is locked.

---

### 4. Form factor constraints are absent
**Location:** Section 4.6 (Redax Hardware Profile)

The spec defines software architecture in detail but has:
- No target weight
- No PCB dimensions
- No temple/arm thickness constraint
- No nose bridge/fit constraint
- No display type (waveguide? projector? no display?)
- No battery placement strategy

**Fix required:** Define physical constraints before hardware selection or enclosure design begins.

---

### 5. OpenClaw gateway has no watchdog or recovery
**Location:** Section 7 (Runtime Service Contracts)

If openclaw-gateway crashes mid-session, there is:
- No automatic restart
- No session recovery path
- No fallback orchestration

This is the entire orchestration layer. One crash and the user is stuck.

**Fix required:** Add watchdog systemd unit with restart policy. Define session recovery mechanism.

---

### 6. Python services have no supervision model defined
**Location:** Section 8.8 (Implementation Stack)

audiod, memoryd, and perceptiond are Python 3.11. But the spec never says HOW they run:
- Bare Python scripts with no supervision?
- systemd services with restart policies?
- Processes spawned by OpenClaw gateway?

This changes error handling, logging, restart behavior, and crash recovery entirely.

**Fix required:** Explicitly define process supervision for each service. Recommended: systemd units for all services.

---

### 7. Python GIL conflicts with real-time audio requirements
**Location:** Section 8.8 + audio pipeline design

Streaming VAD + PCM chunk buffering + whisper inference requires tight, bounded latency. Python's GIL and GC pauses are real problems for real-time audio pipelines. The build plan acknowledges this concern but doesn't prescribe a solution, deferring to "v1.5."

This is not a plan — it's a punt.

**Fix required:** Either (a) specify Rust for audiod with FFI to whisper.cpp, or (b) define a strict audio latency budget and instrument Python audiod to prove it stays within bounds. No deferring without a concrete trigger condition.

---

## ARCHITECTURAL GAPS — Missing pieces that will block implementation

### 8. Bootstrap wizard is not specified
**Location:** Section 6 + Phase 0

Phase 0 calls for a "bootstrap wizard UI" but there are no:
- Wireframes or flow diagrams
- State machine with error transitions
- Retry UX for camera permission denied
- Offline skip behavior
- First-run failure recovery

This is the first UI the user sees. It needs to be designed before implementation.

---

### 9. Package signing mechanism undefined
**Location:** Section 12 (Release Pipeline)

"Sign package" appears but doesn't specify: GPG? Sigstore? Something else? For a security product claiming integrity, this cannot be ambiguous.

Also missing: model file signature verification. Only checksums mentioned — no signature-based verification for downloaded models.

---

### 10. Wake word has no concrete plan
**Location:** Section 10.5 (Voice Stack)

v1 has push-to-talk only. Wake word is "v1.5 / experimental." But there's no:
- Feature gate architecture (how does wake word slot in?)
- Timeline or trigger condition
- Audio pipeline diagram showing wake word insertion point

Pressure to add it will come early. Without a plan, it will get bolted on poorly.

---

### 11. Memory provider promotion gates not benchmarked
**Location:** Section 17.5

Optional providers (Mem0, MemPalace) must beat canonical on p95 read/write latency and retrieval quality. But there are:
- No benchmarks defined
- No latency thresholds
- No retrieval quality metrics
- No acceptance criteria

"Promotion" will always be a judgment call with no quantitative basis.

---

### 12. IPC transport not locked
**Location:** Section 7.9

"Unix socket or local RPC" for several paths — but not chosen. Unix sockets are faster and simpler for local services. gRPC adds dependencies and complexity. This affects serialization, error handling, and service decomposition decisions.

**Fix required:** Lock to Unix socket for all local service communication. RPC/serde_JSON is sufficient for this scale.

---

### 13. No GPU/NPU acceleration path defined
**Location:** Section 10.3 + aarch64 target

LFM2.5-VL-450M on Redax aarch64 — is there a GPU? NPU? Which inference path: GGUF via llama.cpp, ONNX via Olive, or MLX? The spec names no acceleration target. This is a fundamental deployment decision that affects performance entirely.

---

## IMPLEMENTATION RISKS — Will cause problems during development

### 14. Python stack inconsistency without justification
**Location:** Section 8.8

- os-toold: Rust (correct — security-critical)
- audiod: Python 3.11 (but executes model outputs as audio)
- memoryd: Python 3.11 (but does vector search)
- perceptiond: Python 3.11 (but does image processing)

The language split has no stated justification. If it's performance, Python doesn't serve audio or vector search well. If it's security, audiod is also security-relevant. The split feels arbitrary.

---

### 15. Redax hardware is a moving target
**Location:** Section 4.6

"Redax reference hardware profile" means the board isn't finalized. Camera bridges, GPIO, power management, and thermal design all depend on finalized hardware. Building against a moving target risks significant rework when hardware locks.

**Mitigation:** Build against x86_64 laptop as primary dev target. Redax-specific code isolated behind hardware abstraction.

---

### 16. No VLM fallback defined
**Location:** Section 10.3

The spec mentions "Gemma fallback" but doesn't define:
- How the system decides to switch to fallback
- How state transfers to the fallback model
- What degraded UX looks like
- How to switch back

---

### 17. Degraded service modes undefined
**Location:** Section 7.8

Section 7 says "perceptiond and audiod may enter degraded mode" but never defines:
- WHAT degraded modes exist for each service
- WHAT triggers degraded mode
- HOW the UI communicates degraded state
- HOW to recover from degraded mode

---

## MINOR — Clarify before implementation

### 18. Storage weight tradeoffs not discussed
128GB eMMC vs 64GB vs 32GB has direct weight and cost implications for glasses. No minimum viable storage defined for the wearable form factor.

---

### 19. No security review of perception → os-toold path
OCR text could contain malicious commands that bypass the denylist. Camera frames could contain prompt injection. The spec mentions audit logging but not input sanitization on the perception → reasoning → action path.

---

### 20. No quantified latency targets
p95 STT latency, TTS latency, VLM inference latency, memory retrieval latency — none specified with numbers. Without latency budgets, we can't define performance success criteria.

---

## RECOMMENDED ACTIONS BEFORE CODE

### Must do (blocks all implementation):
- [ ] Get LFM2.5-VL-450M benchmark data on comparable aarch64 hardware
- [ ] Define power budget: target W, ceiling W, battery capacity, battery life target
- [ ] Design inference gate properly: salience threshold, not FPS threshold
- [ ] Lock IPC transport: Unix sockets + serde_JSON
- [ ] Define supervision model for all Python services (systemd units)

### Must do (blocks Phase 1 start):
- [ ] Write bootstrap wizard state machine + flow
- [ ] Define degraded modes for each service with recovery paths
- [ ] Choose package signing mechanism (recommend GPG)
- [ ] Document VLM fallback activation/deactivation logic

### Should do (before Phase 2):
- [ ] Define physical form factor constraints
- [ ] Define thermal design constraints (passive only? max skin contact temp?)
- [ ] Lock GPU/NPU acceleration path for aarch64
- [ ] Write memory provider promotion gate benchmarks

---

## WHAT THE ARCHITECTURE GETS RIGHT

To be fair — the following are genuinely solid and don't need changing:
- Tauri v2 + .deb + systemd (correct deployment choice)
- OpenClaw as sole orchestration runtime
- V4L2-first generic camera provider model
- SQLite + Markdown + vectors memory architecture
- Whisper.cpp for STT + KittenTTS for TTS (correct stack)
- Model download on first run, not in .deb
- Service health contracts schema
- Failure handling matrix
- Repo shape (apps/, services/, shared/, packaging/)
- Idempotent installer scripts with upgrade preservation

---

*Review complete. Ready to update canonical doc or create action plan on request.*
