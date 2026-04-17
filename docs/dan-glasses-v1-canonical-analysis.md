# Dan Glasses v1 Canonical — Full Analysis
# Status: Updated from dan-glasses-architecture-v1-canonical.pdf (2026-04-16)

## Document Scope

- 27-page canonical handoff doc
- Tauri v2 + .deb + systemd
- OpenClaw orchestration only
- LFM2.5-VL-450M vision, whisper.cpp STT, KittenTTS TTS
- SQLite + Markdown + vectors memory core
- V4L2-first generic camera
- Dual target: Redax aarch64 + Linux laptop x86_64

---

## STRENGTHS

### Architecture Decisions
1. **OpenClaw-only orchestration** — clean scope, no dual-runtime ambiguity
2. **Tauri v2 + .deb + systemd** — right call for this product. Flatpak/AppImage can't handle systemd units, udev, and privileged install actions. Debian packaging is the correct primary path.
3. **V4L2-first camera** — generic provider model avoids vendor lock-in. Correct decision.
4. **Memory: SQLite + Markdown + vectors** — the only architecture that satisfies: offline, inspectable, durable, low complexity. Correct canonical core.
5. **Model delivery on first run** — .deb should not ship large weights. Correct.
6. **Service health contracts** — well-defined ServiceHealth schema with degraded modes.
7. **Failure handling matrix** — solid recovery paths for each failure mode.
8. **Repo shape** — clean separation: apps/, services/, shared/, packaging/

### Process & Pipeline
9. **Idempotent installer scripts** — upgrade must not delete user memory. Locked correctly.
10. **Bootstrap artifact schema** — state.json, models.json, etc. gives recovery a fighting chance.
11. **5-phase implementation plan** — logical ordering, Phase 0 is packaging skeleton which is right.
12. **Adaptation FPS modes** (2/5/10) — good intention, good foundation.

---

## PROBLEMS AND RISKS

### 🔴 CRITICAL — Battery & Power (User's Primary Concern)

**1. Adaptive FPS throttles capture, not inference.**
Section 10.10 defines:
- idle: 2 FPS capture
- watchful: 5 FPS capture
- active burst: 10 FPS capture

But every captured frame still goes through the full perception pipeline:
- Frame gate decision: 5-20ms/frame
- OCR on candidate frame: 40-150ms
- VLM inference on candidate frame: 150-800ms (LFM2.5-VL-450M)

So at 2 FPS idle, you're still firing VLM inference every 500ms on average. That's the wrong lever.

**What you actually need:**
- Inference batching or gate-at-threshold (e.g., only run VLM when frame-delta exceeds a salience threshold)
- Drowsy mode: reduce to 0.5 FPS + no VLM, only motion detection
- Sleep mode: camera off, services idle, wake on voice trigger
- Thermal throttle: drop to minimal model (Gemma fallback) when temperature exceeds threshold

**2. No power budget defined.**
Section 10.11 says "keep average low enough for always-on desk mode" — but no numbers. What is the target? 5W average? 10W? 2W? For a wearable glasses form factor, this is everything.

**3. No battery capacity target.**
The Redax reference profile specifies CPU/RAM/storage but says nothing about:
- Battery chemistry (LiPo? Li-ion?固态?)
- Target battery life (2h? 4h? 8h?)
- Charge method (USB-C PD? Mag-safe? Wireless?)
- Physical weight constraint for a wearable

**4. LFM2.5-VL-450M power draw uncharacterized.**
The spec names LFM2.5-VL-450M as primary vision but gives no power draw estimate. At what resolution? What batch size? What quantization? Without this, thermal design is guesswork.

**5. Concurrent service power stack not modeled.**
At any given moment you could have:
- perceptiond (camera + VLM)
- audiod (whisper.cpp, always-on mic potentially)
- memoryd (SQLite + vector index)
- os-toold
- openclaw-gateway

No power budget stack or priority queuing under battery pressure.

### 🔴 CRITICAL — Size & Form Factor (User's Primary Concern)

**1. Zero physical constraints defined.**
The spec defines software architecture in detail but has:
- No target weight for the glasses
- No target dimensions
- No temple/arm thickness constraint
- No nose bridge / fit constraint
- No display type ( waveguide? projector? no display?)

Without these, the engineering team cannot size the PCB, select components, or design the enclosure.

**2. Storage hierarchy assumes datacenter proximity.**
128GB eMMC is listed as preferred. But if this is a wearable, every gram matters. 128GB eMMC vs. 64GB vs. 32GB has direct weight and cost implications. The spec doesn't give a minimum viable storage for the glasses form factor.

**3. 8GB RAM minimum — is this achievable in glasses?**
8GB LPDDR in a glasses form factor with heat management is non-trivial in 2026. Most consumer smart glasses have 2-4GB. The spec says "8GB preferred, 4GB minimum for reduced profile." This is likely aspirational for the Redax board, not the glasses frame itself.

### 🟡 MEDIUM — Architectural Gaps

**6. OpenClaw as sole orchestrator — what happens when it crashes?**
Section 7.9 IPC contracts list services and their transports, but there's no watchdog/fallback mechanism if openclaw-gateway itself fails mid-session. Does the UI auto-restart it? Is there a session recovery path?

**7. No explicit GPU/acceleration contract.**
LFM2.5-VL-450M inference — is there a GPU target? NPU? Or CPU only? For aarch64 on Redax, GPU acceleration is likely needed. The spec does not specify whether the VLM runs on GPU, NPU, or CPU. This is a fundamental deployment decision.

**8. audiod push-to-talk default is safe but limits UX.**
Section 10.5 says "push-to-talk or explicit recording trigger" — wake word is deferred. This is the right call for v1 given battery, but it limits the hands-free UX. The spec should note that wake-word is a v1.5 or v2 target, not just "experimental."

**9. Memory provider promotion gates are not testable.**
Section 17.5 says optional providers must beat canonical on p95 read/write latency, retrieval quality, and crash recovery. But there are no benchmarks or acceptance criteria defined for these gates. "Promoting" Mem0 or MemPalace in v1.5 will be a judgment call with no quantitative threshold.

**10. Package signing — mechanism not defined.**
Section 12 says "sign package" but doesn't specify: GPG? Sigstore? Only mentions "signed .deb" and "detached checksums/signatures where applicable." For a product claiming security integrity, this needs a concrete mechanism.

**11. Bootstrap wizard is underspecified.**
Phase 0 calls for "bootstrap wizard UI" but there's no spec for: what does the wizard show? How does it handle retries? What's the UX for camera permission denied? This is a critical user-facing component that needs wireframes and state machine.

### 🟢 MINOR — Clarity Improvements

**12. Redax is still a codename, not a finalized hardware spec.**
The spec uses "Redax reference hardware profile" which means the board is still in flux. Implementation decisions for Redax-specific camera bridges, GPIO, or power management are impossible to finalize until hardware is locked.

**13. Obsidian MCP as "optional adapter" — worth watching.**
Obsidian MCP is a great developer workflow but the spec correctly notes it's a mirror, not canonical store. This is right, but as the product grows, pressure to make Obsidian primary will increase. The spec should define a hard line: canonical stays SQLite unless a future promotion gate is formally passed.

**14. Hermes one-provider constraint correctly flagged.**
Section 17.5 correctly notes that Hermes allows one external provider at a time — which makes it incompatible with the canonical multi-adapter architecture goal. This is good research grounding.

**15. No mention of security attack surface.**
os-toold executes commands with guardrails. But what about: prompt injection via camera frames? OCR text that contains malicious commands that bypass the denylist? The spec mentions "argument hashing and audit log" but doesn't address input sanitization on the perception → os-toold path.

---

## BATTERY & SIZE DEEP DIVE

**If we assume Dan Glasses is a true wearable (not just a laptop tethered camera):**

### Power Budget Model (Planning Estimates)

```
Component           Idle     Watchful   Active
-------------------------------------------------
openclaw-gateway    0.5W     0.5W       0.8W
memoryd (SQLite)    0.2W     0.2W       0.3W
os-toold            0.1W     0.1W       0.2W
audiod (mic ready)  0.3W     0.3W       0.5W
perceptiond (cam)   0.5W     0.8W       2.5W  ← biggest variable
LFM2.5-VL-450M      0W       0W         3-8W ← likely largest draw
KittenTTS (spike)   0W       0W         1-2W
-------------------------------------------------
Estimated total     ~1.6W    ~1.9W      ~8-13W
```

For a wearable with 2-4 hour target battery life:
- At 5W average: ~2500mAh at 3.7V → real battery weight
- At 10W average: ~5000mAh at 3.7V → very heavy for glasses

**Key insight:** VLM inference is the dominant power event. Throttling capture FPS is the wrong lever. Throttling VLM inference frequency (frame gate decisions, batching, salience threshold) is the right lever.

### Form Factor Constraints Needed

To make this real for glasses:
- PCB area: what max dimensions?
- Heat dissipation: passive? active fan? (can't run a fan in glasses)
- Battery placement: temples? bridge? distributed?
- Weight target: <50g? <80g?

These must be defined before the spec can be considered a true product handoff, not just a software architecture doc.

---

## VERDICT

**What this doc does well:**
Software architecture is thorough, well-researched, and locked correctly. The service topology, IPC contracts, memory architecture, and install pipeline are production-grade. The research grounding matrix is excellent.

**What it critically lacks:**
Battery and size are not just "important" — they are the constraints that will determine whether this product can be a true wearable or is forced to be a tethered/desk-only device. The spec needs:

1. A power budget table with target, measured, and ceiling values per component
2. A thermal design note (passive only? what max temp for skin contact?)
3. Physical constraints: weight, dimensions, battery placement
4. VLM inference power characterization (quantized? what resolution? GPU or CPU?)
5. Wake/sleep/throttle state machine as first-class architecture, not deferred

**Without these, the spec is a strong Linux app architecture but an incomplete wearable product spec.**

---

## RECOMMENDED ADDITIONS TO SPEC

1. Section 10.13: Power and Thermal Architecture
2. Section 10.14: Physical Form Factor Constraints
3. Section 10.15: VLM Power and Performance Characterization
4. Section 10.16: Adaptive Power State Machine (wake/sleep/throttle/deep-idle)
5. Update Section 10.11 with actual planning targets in Watts, not abstract descriptions

---

*Analysis complete. Ready to incorporate updated canonical architecture.*