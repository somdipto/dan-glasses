# Dan Glasses — High Priority Build Plan
# Status: Research Complete, Ready for Implementation
# Date: 2026-04-17

---

## EXECUTIVE SUMMARY

The Dan Glasses app is buildable today — here's the key finding:

**What blocks immediate development:** Hardware finalization (Redax board), not software architecture or model availability.

**What's ready NOW:**
- LFM2.5-VL-450M: Released April 11, 2026 — sub-250ms edge inference, 512×512, GGUF/ONNX available
- whisper.cpp: Production-grade STT, multiple Rust bindings with VAD, GPU acceleration
- KittenTTS: <25MB, state-of-the-art, ONNX/WASM, CPU-friendly
- OpenClaw: Released late 2025, TypeScript/Node, MCP tools, multi-agent, policy enforcement
- Tauri v2: CrabCamera plugin exists for cross-platform camera, mature plugin ecosystem

**The build plan: Develop on Linux laptop (x86_64) targeting Redax (aarch64) as deployment. This gives us:**
1. A fully functional prototype we can demo and test NOW
2. A clear migration path to the wearable form factor when hardware is ready
3. Zero hardware dependency for software development

---

## TECH STACK CONFIRMATION

### Vision: LFM2.5-VL-450M ✅ READY
- Released April 11, 2026 by Liquid AI
- 450M params, sub-250ms inference, 512×512 images
- SigLIP2 NaFlex encoder (not ResNet/ViT — better for edge)
- GGUF version available for llama.cpp — confirmed working (mlx-vlm issue workaround)
- ONNX export via Liquid4All/onnx-export: fp32, fp16, q4, q8 precisions
- HuggingFace: LiquidAI/LFM2.5-VL-450M
- Architecture: LFM2.5-base + 400M SigLIP2 NaFlex + efficient projector
- Context: 32,768 tokens
- License: Research/commercial (check Liquid AI license)

Key insight: This is the best-fit VLM for edge wearables right now. Small, fast, purpose-built for on-device.

### STT: whisper.cpp ✅ READY
- C/C++ with mature Rust bindings
- Options:
  - `tazz4843/whisper-rs`: Classic bindings, archived to Codeberg but maintained
  - `operator-kit/whisper-cpp-plus-rs`: Has async/Tokio, VAD (Silero), real-time PCM streaming
  - `cjpais/transcribe-rs`: Multi-engine (Whisper + Parakeet + others), ONNX support
- GPU: Vulkan, Metal, CUDA, ROCm all supported
- Quantization: integer quantization, zero-runtime allocations
- VAD: Built-in, plus Silero integration in plus-rs
- Cross-platform: macOS, iOS, Android, Linux, Windows, WebAssembly, Raspberry Pi

Recommended for Dan Glasses: whisper-cpp-plus-rs (async, VAD, real-time streaming)

### TTS: KittenTTS ✅ READY
- <25MB total (Mini model: 80M params but still tiny)
- Three variants: default, base, mini (quality: default > base > mini, speed: inverse)
- Neural text-to-speech, state-of-the-art quality for size class
- ONNX export available, WASM browser runner exists
- CPU-friendly, designed for edge deployment
- License: Need to verify (repo: KittenML/KittenTTS)

Key advantage: Under 25MB means it can ship in the .deb without bloating it.

### Orchestration: OpenClaw ✅ READY
- Released: Late 2025 (free, open-source)
- Language: TypeScript/Node.js
- Stars: 464+ on awesome-openclaw, active development
- Architecture:
  - openclaw-gateway: Control plane (channels, routing, cron, agent registry, session store)
  - openclaw-runtime: Per-agent process (isolation, scaling)
  - Six core components: Gateway, Agent, Tools, Workspace, Sessions, Nodes
- MCP Server: Proposed in Issue #53215, tools exposed as MCP tools
- Multi-agent: Octopus Orchestrator (Issue #64435) — parallel arms, missions, grips, claims, leases
- Policy: tools.deny/allow, per-agent filtering, security-focused
- Memory: Bootstrap (session-start) + Semantic (on-demand via memory/search)
- Workspace files: AGENTS.md, SOUL.md, USER.md, MEMORY.md, IDENTITY.md, HEARTBEAT.md, TOOLS.md

Key concern: TypeScript/Node.js — but this is the correct call for an agent framework. Rust would be ideal for low-level services but OpenClaw's tooling ecosystem is TypeScript-native.

### Frontend: Tauri v2 ✅ READY
- Language: Rust backend + web frontend (React/Svelte/Vue)
- Plugins:
  - CrabCamera (crates.io/crabcamera): Cross-platform camera for Tauri, zero Qt dependencies
  - File system, shell, clipboard, dialog, notification, os, process, etc.
- Packaging: .deb + systemd (correct choice, not Flatpak/AppImage)
- V2 improvements: Better plugin system, improved mobile support, enhanced security

Key advantage: Small bundle size (~10MB vs Electron's ~150MB), native performance, Rust safety.

### Camera: V4L2 ✅ READY
- Linux Video4Linux2: Standard Linux camera API
- CrabCamera wraps V4L2 access for Tauri
- Provider model (per spec): generic V4L2 provider avoids vendor lock-in
- Formats: YUYV, MJPG, NV12 — all standard

### Memory: SQLite + Markdown + Vectors ✅ READY
- Per canonical spec
- SQLite: User data, session state, settings
- Markdown files: Bootstrap memory (AGENTS.md, etc.)
- Vector store: Semantic recall
- Option to mirror to Obsidian MCP (per spec, optional adapter)

---

## BUILD STRATEGY

### Core Principle: Build NOW, Migrate Later

**Develop on x86_64 Linux laptop, targeting Redax (aarch64) as deployment.**

This means:
- All code is portable — same Rust/Tauri works on both
- Services run identically on laptop and Redax
- We can demo TODAY without waiting for Redax hardware
- Migration to Redax = rebuild, not rewrite

### Two Build Tracks

**Track A: Desktop Prototype (Start immediately)**
- Target: Developer's Linux laptop (x86_64)
- Form factor: Desktop companion app with USB camera or integrated webcam
- Purpose: Validate all software, prove the concept, early demos
- When ready: 2-4 weeks for working prototype

**Track B: Wearable Implementation (Hardware-dependent)**
- Target: Redax aarch64 board in glasses form factor
- Requires: Redax board finalized, camera module selected, thermal design validated
- Purpose: True wearable product
- When ready: TBD — blocked on hardware

---

## PHASE 1: Desktop Prototype (Weeks 1-4)

### Goal: Fully functional desktop companion app running all services

### Week 1: Foundation
- [ ] Initialize Tauri v2 project with React frontend
- [ ] Set up logging: structured logging to /dev/shm/, Loki integration
- [ ] Verify Rust toolchain: 1.75+, correct target triples
- [ ] Set up workspace: apps/dan-glasses/, services/, shared/, packaging/
- [ ] Initialize Git, AGENTS.md, SOUL.md, MEMORY.md workspace files
- [ ] Set up systemd unit files (for future .deb)

### Week 2: Core Services
- [ ] Deploy OpenClaw gateway on laptop
- [ ] Verify agent loop: message → session → tool → response
- [ ] Configure channels: Telegram (primary), fallback to terminal
- [ ] Set up workspace files: AGENTS.md, SOUL.md, IDENTITY.md
- [ ] Verify MCP tool registration (browser, file, exec, message)
- [ ] Set up cron and heartbeat automation

### Week 3: Perception Pipeline
- [ ] Integrate whisper.cpp via whisper-cpp-plus-rs
  - [ ] Audio capture (CrabCamera or ALSA)
  - [ ] VAD (Silero) for voice activity detection
  - [ ] Real-time streaming transcription
  - [ ] Push-to-talk activation (per spec v1)
- [ ] Integrate LFM2.5-VL-450M via llama.cpp
  - [ ] Camera capture (CrabCamera)
  - [ ] Frame → VLM → description pipeline
  - [ ] 512×512 input, sub-250ms target
  - [ ] Salience-based gating (NOT fixed FPS — per critical analysis)
- [ ] Verify perception → memory → reasoning flow

### Week 4: Output & Polish
- [ ] Integrate KittenTTS
  - [ ] Text → speech pipeline
  - [ ] Audio output (speaker or headphone)
  - [ ] Latency target: <500ms for short responses
- [ ] Implement adaptive power states (laptop is AC-powered, but architecture must be correct)
  - [ ] Watchful mode: 5 FPS capture, VLM on motion
  - [ ] Active mode: 10 FPS capture, VLM continuous
  - [ ] Drowsy mode: 0.5 FPS, motion detection only
  - [ ] Sleep mode: camera off, mic ready, wake on voice trigger
- [ ] Bootstrap wizard UI (Tauri frontend)
  - [ ] Camera permission flow
  - [ ] Model download on first run
  - [ ] Initial setup (language, preferences)
- [ ] Service health contracts and degraded modes

### Week 4 End State: DEMO-READY
A desktop companion app that:
1. Listens to voice commands via push-to-talk
2. Captures camera frames, runs VLM inference
3. Responds via TTS
4. Remembers context via SQLite + vector memory
5. Runs OpenClaw agent orchestration
6. Connected to Telegram for control

---

## PHASE 2: Service Isolation (Weeks 5-8)

### Goal: Transform prototype into proper service architecture

### Week 5-6: Service Decomposition
- [ ] Extract perceptiond: V4L2 → frame processing → VLM
  - [ ] Standalone Rust binary
  - [ ] IPC: Unix socket or gRPC
  - [ ] ServiceHealth schema with degraded modes
- [ ] Extract audiod: Audio capture → VAD → transcription
  - [ ] Standalone Rust binary
  - [ ] IPC: Unix socket or gRPC
- [ ] Extract memoryd: SQLite + vector store
  - [ ] Standalone Rust binary
  - [ ] IPC: Unix socket or gRPC
  - [ ] Obsidian MCP adapter (optional)
- [ ] Extract os-toold: Command execution with guardrails
  - [ ] Standalone Rust binary
  - [ ] IPC: Unix socket or gRPC
- [ ] Extract toold: KittenTTS synthesis
  - [ ] Standalone Rust binary
  - [ ] IPC: Unix socket or gRPC

### Week 7-8: OpenClaw Integration
- [ ] Verify OpenClaw gateway orchestrates all services
- [ ] Implement per-service health monitoring
- [ ] Add failure handling matrix (per spec Section 9)
- [ ] Implement recovery paths: restart, fallback, degraded operation
- [ ] Verify IPC contracts (Section 7.9) match actual implementation
- [ ] Add OpenClaw MCP tools for: perception, memory, os-toold, tts

### Week 8 End State: ARCHITECTURE COMPLETE
All services isolated, OpenClaw orchestrating, ready for:
- Systemd packaging (.deb)
- Redax migration (aarch64 rebuild)
- Wearable form factor adaptation

---

## PHASE 3: Wearable Adaptation (TBD — Hardware Dependent)

### Pre-requisites:
- Redax board finalized and available
- Camera module selected (V4L2 compatibility)
- Thermal design validated (passive only for glasses)
- Physical constraints defined: weight, dimensions, battery placement

### Key Changes for Wearable:
1. **Power architecture**: Implement power state machine (Section 10.16 from analysis)
2. **Thermal management**: Passive cooling only, Gemma fallback at temp threshold
3. **Form factor**: Reduce PCB, optimize component placement
4. **Battery**: USB-C PD charging, target 4h battery life
5. **Camera**: V4L2 provider with selected hardware module

---

## COMPONENT STATUS TABLE

| Component | Status | Integration Path | Notes |
|-----------|--------|-----------------|-------|
| LFM2.5-VL-450M | ✅ Ready | llama.cpp GGUF or ONNX Runtime | Released April 11, 2026 |
| whisper.cpp | ✅ Ready | whisper-cpp-plus-rs (async + VAD) | Production grade |
| KittenTTS | ✅ Ready | ONNX Runtime or direct Python | <25MB, CPU-friendly |
| OpenClaw | ✅ Ready | npm install, gateway config | TypeScript/Node |
| Tauri v2 | ✅ Ready | cargo install tauri-cli | CrabCamera plugin exists |
| CrabCamera | ✅ Ready | crates.io/crabcamera | Cross-platform, no Qt |
| V4L2 | ✅ Ready | Linux native | Provider model per spec |
| SQLite | ✅ Ready | rusqlte or sqlite3 crate | Per spec architecture |
| Vector store | ⚠️ Choose | Qdrant? Arrow? Chroma? | Need to decide — per spec memoryd |

---

## DECISIONS REQUIRED

### 1. Vector Store Choice
Per canonical spec, memoryd uses vectors for semantic recall. Options:
- **Qdrant**: Full-featured, Rust-native, but heavier
- **Chroma**: Simple, but Python dependency
- **Arrow** (memory-map vectors): Lightweight, but less mature
- **Usocket vectors**: Per spec, something local

Recommendation: Start with in-process vector store (e.g., `vectors` crate or simple flat index) to avoid dependency complexity. Migrate to Qdrant if needed.

### 2. STT Model Size
 whisper.cpp models: tiny.en (39MB), base.en (74MB), small.en (244MB), medium.en (766MB)

Recommendation for glasses form factor: `base.en` (74MB) — good accuracy, reasonable size. tiny.en for thermal-constrained scenarios.

### 3. VLM Quantization
LFM2.5-VL-450M via GGUF: Q4_0 (default), Q5_0, Q8_0

Recommendation: Q4_0 for glasses (balance of size/quality). Q5_0 for laptop prototype (better quality, AC-powered).

### 4. TTS Variant
KittenTTS: default, base, mini

Recommendation: `base` for prototype. `mini` for glasses (if quality acceptable).

---

## CRITICAL RISKS

### Risk 1: Redax Hardware Timeline ⚠️ HIGH
- **Impact**: Software complete but no target hardware
- **Mitigation**: Develop on x86_64 laptop, target Redax as rebuild not rewrite
- **Timeline impact**: Unknown — hardware not publicly available

### Risk 2: LFM2.5-VL-450M Power Draw 🔴 CRITICAL
- **Impact**: VLM inference is dominant power event, specs don't characterize draw
- **Mitigation**: Implement salience-based gating, not fixed FPS. Plan for thermal fallback (Gemma).
- **Need**: Actual power measurements on target hardware (aarch64)

### Risk 3: OpenClaw TypeScript Runtime 🔴 CRITICAL
- **Impact**: OpenClaw is TS/Node, not Rust — conflict with spec's Rust service orientation
- **Mitigation**: Accept OpenClaw as orchestration layer. Services (perceptiond, audiod, memoryd, toold) remain Rust.
- **Architecture**: OpenClaw gateway → services via IPC (not in-process)

### Risk 4: Form Factor Constraints 🟡 MEDIUM
- **Impact**: 8GB RAM, 128GB eMMC may not be achievable in glasses
- **Mitigation**: Define minimum viable config (4GB RAM, 32GB storage). Plan weight target (<50g).
- **Need**: Hardware team input on physical constraints

---

## BUILD PRIORITY ORDER

```
1. Tauri project setup + logging
2. OpenClaw gateway on laptop
3. Audio pipeline (whisper.cpp + VAD)
4. Vision pipeline (LFM2.5-VL-450M + camera)
5. TTS pipeline (KittenTTS)
6. Memory (SQLite + vectors)
7. Service decomposition
8. Bootstrap wizard
9. systemd packaging
10. Redax migration
```

---

## IMMEDIATE NEXT STEPS (Day 1)

1. **Initialize Tauri v2 project**
   ```bash
   npm create tauri-app@latest dan-glasses
   cd dan-glasses
   # Select: React, TypeScript, Cargo, Rust backend
   ```

2. **Install OpenClaw**
   ```bash
   # Check official docs for npm install
   npm install -g openclaw
   openclaw --version
   ```

3. **Set up development workspace**
   ```bash
   mkdir -p ~/danlab/dan-glasses
   cd ~/danlab/dan-glasses
   mkdir -p apps/ services/ shared/ packaging/
   touch AGENTS.md SOUL.md MEMORY.md
   ```

4. **Download initial models**
   - whisper.cpp base.en model (~74MB)
   - LFM2.5-VL-450M GGUF Q4_0 (~450MB)
   - KittenTTS base model (~25MB)

5. **First test**: Run OpenClaw gateway, verify agent loop

---

## SUCCESS METRICS

### Week 4 (Desktop Prototype):
- [ ] Push-to-talk voice → response via TTS (end-to-end <3s)
- [ ] Camera frame → VLM → description (end-to-end <1s)
- [ ] Memory persists across sessions (SQLite verified)
- [ ] Telegram control connected and working
- [ ] All services healthy, degraded modes tested

### Week 8 (Architecture Complete):
- [ ] All services running as isolated Rust binaries
- [ ] OpenClaw orchestrating all services via IPC
- [ ] .deb package builds successfully
- [ ] Service health contracts implemented
- [ ] Failure handling matrix tested

### Wearable Ready (TBD):
- [ ] Power state machine operational
- [ ] Thermal throttle implemented
- [ ] <50g weight achieved
- [ ] 4h battery life validated
- [ ] Redax build passes all tests

---

*Build plan complete. Ready to execute.*