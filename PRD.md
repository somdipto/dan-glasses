# Dan Glasses — Product Requirements Document

**Version:** 1.0  
**Status:** Draft  
**Date:** 2026-04-17  
**Owner:** DanLab (som/dan)

---

## 1. Vision & Position

Dan Glasses is an **AI-native wearable companion** — not a notification mirror or a camera with a speaker. It is a persistent, context-aware AI agent that perceives the world through vision and hearing, thinks silently, and speaks back only when needed.

The core proposition:
> "What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"

**Positioning:**
- Not Google Glass (enterprise display overlay)
- Not Ray-Ban Meta (capture + share, reactive)
- **Proactive AI companion** — observes, reasons, contextualizes, acts. Always-on sensing, selective output.

**Target user:** Technical early adopters, productivity-obsessed knowledge workers, accessibility-first users who want AI that works *with* them, not just responds *to* them.

---

## 2. Success Definition

Dan Glasses succeeds when:
1. A user wearing it for a full workday gets genuine utility (not novelty) — reminders about people they forgot, context they missed, tasks they deferred
2. The device disappears — it works silently in the background, surfacing only when valuable
3. The AI memory becomes a genuine cognitive extension, not a searchable log

**Not success:** Voice assistant with camera. Capture and share. Notification relay.

---

## 3. Core User Stories

### US-1: Encounter Recall
> "I met Priya at the conference yesterday but I can't remember her name or what we talked about. My glasses can tell me."

**Flow:** Camera captures encounter → person detected + named (with permission) → stored to memory → user queries → response.

### US-2: Contextual TaskReminder
> "My glasses noticed I walked past the pharmacy 3 times this week without picking up my prescription. Remind me next time I'm near one."

**Flow:** Location/visual pattern detected → crosses a user-defined threshold → proactive suggestion via TTS or Telegram.

### US-3: Object Search
> "I left my keys somewhere in the apartment. Ask my glasses."

**Flow:** User voice query → perception pipeline active → camera scan triggered → match found → location reported.

### US-4: Passive Journaling
> "What did I do on Tuesday that was different from usual?"

**Flow:** Daily capture stored → summaries generated → user asks free-form question → memory queried.

### US-5: Hands-Free Check-In
> "My hands are covered in dough. Tell me if there's an urgent email."

**Flow:** Push-to-talk → audiod → transcription → routing → memory check + email tool → TTS response.

---

## 4. System Architecture

### 4.1 Orchestration Layer
**OpenClaw** (TypeScript/Node.js) — gateway + agent runtime. Not Rust-native, but the correct choice given ecosystem maturity.

```
openclaw-gateway
├── agent-work/ (Dan1, Dan2, Dan4 defined here)
├── workspace/ (AGENTS.md, SOUL.md, IDENTITY.md, MEMORY.md)
└── channels: Telegram (primary), Terminal (debug)
```

### 4.2 Services (Rust binaries, IPC via Unix sockets)

| Service | Responsibility | Power State |
|---------|---------------|-------------|
| `perceptiond` | Camera → VLM → description | Active: 2.5-8W |
| `audiod` | Mic → VAD → STT → transcription | Watchful: 0.3W |
| `memoryd` | SQLite + vector store + markdown | Idle: 0.2W |
| `os-toold` | Command execution, guardrails | Idle: 0.1W |
| `toold` | TTS synthesis | Spike: 1-2W |

### 4.3 Models

| Task | Model | Size | Notes |
|------|-------|------|-------|
| Vision | LFM2.5-VL-450M | ~450MB Q4 | GGUF via llama.cpp, sub-250ms |
| STT | whisper.cpp base.en | 74MB | VAD via Silero |
| TTS | KittenTTS base | ~25MB | ONNX |

### 4.4 Build Strategy
**Develop on x86_64 Linux laptop. Deploy on Redax aarch64.** The software is portable — same Rust/Tauri runs on both. Prototype is demo-ready in 4 weeks on laptop.

---

## 5. Power & Thermal Architecture

### 5.1 Power Budget

| State | Estimated Draw | Notes |
|-------|---------------|-------|
| Sleep | ~0.5W | Camera off, mic ready, wake on voice |
| Idle (watchful) | ~2W | 2 FPS capture, no VLM |
| Active | ~8-13W | VLM running, TTS spiking |

**Target:** 4-hour battery life at 5W average → ~2500mAh @ 3.7V

### 5.2 Power State Machine

```
Sleep → (voice trigger) → Idle → (motion detected) → Watchful → (salience detected) → Active
                 ↑                                                        ↓
                 └──────────────── (timeout) ─────────────────────────────┘
```

- **Sleep:** Camera off, audiod in low-power wake mode
- **Idle:** 2 FPS capture, frame-delta check only (no VLM)
- **Watchful:** 5 FPS, VLM on motion salience threshold
- **Active:** 10 FPS, continuous VLM (throttle to Gemma fallback at 45°C)
- **Deep Idle:** User-initiated or 30min no interaction

### 5.3 Thermal Constraint
- **Max surface temperature:** 40°C (skin contact safety)
- **Cooling:** Passive only — no fan in glasses form factor
- **Thermal fallback:** Drop from LFM2.5-VL-450M to Gemma3-2B at 42°C

---

## 6. Physical Form Factor Constraints

### 6.1 Targets (to be validated with hardware team)

| Parameter | Target | Minimum |
|-----------|--------|---------|
| Total weight | <50g | <80g |
| Arm thickness | <7mm | <9mm |
| Frame width | 140mm | 135mm |
| Battery placement | Left temple | Distributed |
| Battery capacity | 2500mAh | 1500mAh |

### 6.2 Storage Tiers
- **Primary:** 64GB eMMC (recommended for glasses)
- **Secondary:** 128GB (if weight budget allows)
- **Model delivery:** On first run via download, not pre-shipped in .deb

---

## 7. Core Features (v1)

### 7.1 Perception Pipeline
- Camera capture via V4L2 (generic provider)
- Frame → VLM → structured description
- Salience-based gating: NOT fixed FPS. Run VLM only when frame-delta exceeds threshold
- Output: text description + embeddings → memoryd

### 7.2 Audio Pipeline
- Push-to-talk as default (wake word deferred to v1.5)
- VAD: Silero for voice activity detection
- STT: whisper.cpp base.en
- Real-time streaming transcription to OpenClaw

### 7.3 Memory
- SQLite: session state, user data, settings
- Markdown files: bootstrap (AGENTS.md, SOUL.md, etc.)
- Vector store: semantic recall (in-process flat index, migrate to Qdrant if needed)
- Optional: Obsidian MCP adapter (mirror only, not primary)

### 7.4 Output
- TTS: KittenTTS base variant, <25MB
- Response latency: <3s for voice queries
- Channel: Telegram (primary), speaker/headphone jack

### 7.5 OpenClaw Integration
- MCP tools for: perception, memory, os-toold, tts
- Agent workspace files: AGENTS.md (Dan1/Dan2/Dan4 personas), SOUL.md
- Channels: Telegram as primary, terminal as debug fallback

---

## 8. Non-Goals (v1)

- Wake word detection (deferred to v1.5)
- Real-time continuous vision (power constraint)
- Multi-user / household support (single user per device)
- Display overlay ( waveguide or projector)
- Cellular connectivity (Wi-Fi only)
- Social sharing (capture + post)

---

## 9. Packaging & Deployment

### 9.1 Delivery
- **Format:** .deb + systemd (correct choice, not Flatpak/AppImage)
- **Package signing:** GPG (concrete mechanism — not abstract "sign package")
- **Model delivery:** Download on first run, stored in ~/.dan-glasses/models/

### 9.2 Installer Properties
- Idempotent (upgrade does not delete user memory)
- Bootstrap wizard: camera permission, model download, language preference, Telegram pairing
- Detached signature + checksum verification

### 9.3 Bootstrap Artifact Schema
- `state.json`: current power state, service health
- `models.json`: downloaded model versions
- `memory/`: SQLite + markdown + vectors
- `logs/`: Loki-indexed structured logs

---

## 10. Failure Handling

### 10.1 Service Health Contract

| Service | Healthy | Degraded | Failed |
|---------|---------|----------|--------|
| perceptiond | Camera + VLM responding | Camera only | No frames |
| audiod | Mic + VAD + STT | Mic only | No audio |
| memoryd | SQLite + vectors | SQLite only | No memory |
| toold | TTS responding | Slow synthesis | No output |
| os-toold | Commands executing | Slow exec | Blocked |

### 10.2 Recovery Paths
1. **Restart:** Service-specific watchdog restarts crashed service
2. **Fallback:** e.g., TTS offline → Telegram text fallback
3. **Degraded:** e.g., memoryd vectors down → SQLite-only retrieval
4. **Deep recovery:** Bootstrapping from last state snapshot

### 10.3 OpenClaw Watchdog
If `openclaw-gateway` crashes mid-session:
- Session state persisted to memoryd
- Auto-restart gateway
- Resume session from last checkpoint

---

## 11. Open Questions

| Question | Priority | Owner |
|----------|----------|-------|
| Redax hardware finalization timeline | 🔴 Critical | Hardware |
| LFM2.5-VL-450M power draw characterization | 🔴 Critical | Research |
| Target battery life (4h? 6h?) | 🔴 Critical | Product |
| Physical constraint validation with engg | 🟡 Medium | Hardware |
| Wake word implementation path for v1.5 | 🟡 Medium | Research |
| Package signing key management | 🟡 Medium | Security |
| VLM GPU/NPU acceleration target | 🟡 Medium | Research |
| Thermal model validation (passive cooling) | 🟡 Medium | Hardware |

---

## 12. Success Metrics

### Week 4 (Desktop Prototype)
- [ ] Push-to-talk voice → TTS response <3s (end-to-end)
- [ ] Camera frame → VLM description <1s
- [ ] Memory persists across sessions
- [ ] Telegram connected and working
- [ ] All services healthy, degraded modes tested

### Week 8 (Architecture Complete)
- [ ] All services as isolated Rust binaries
- [ ] OpenClaw orchestrating via IPC
- [ ] .deb builds and installs cleanly
- [ ] Service health contracts implemented
- [ ] Failure handling matrix tested

### Wearable Ready (TBD — hardware-dependent)
- [ ] Power state machine operational
- [ ] Thermal throttle implemented
- [ ] <50g weight target met
- [ ] 4h battery life validated
- [ ] Redax build passes all tests

---

*PRD v1.0 — Dan Glasses. Ready for engineering review.*