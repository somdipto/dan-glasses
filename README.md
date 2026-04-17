# Dan Glasses 👾

AI wearable + desktop companion. Vision, voice, memory — built from India.

## Status

**Software:** Ready to build (LFM2.5-VL-450M, whisper.cpp, KittenTTS, OpenClaw, Tauri v2 all released)

**Hardware:** Track B blocked on Redax board finalization

---

## Quick Start

```bash
# Desktop prototype (Track A — start here)
cd dan-glasses
./scripts/dev.sh
```

## Architecture

```
dan-glasses/
├── dan-glasses-app/    # Tauri v2 React frontend
├── services/            # Rust microservice binaries
│   ├── perceptiond/     # Camera + VLM inference
│   ├── audiod/         # Audio capture + VAD + STT
│   ├── memoryd/         # SQLite + vector store
│   ├── os-toold/        # Command execution guardrails
│   └── toold/          # TTS synthesis
├── shared/              # IPC types + contracts
├── models/              # Model weights (downloaded on first run)
├── packaging/           # .deb + systemd units
├── scripts/             # Dev helpers, build scripts
└── docs/                # Specs, analysis, build plan
```

## Build Tracks

| Track | Target | Status |
|-------|--------|--------|
| **A: Desktop** | x86_64 Linux laptop | Start now — 2-4 weeks to prototype |
| **B: Wearable** | Redax aarch64 | Blocked on hardware |

## Tech Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Orchestration | OpenClaw | TypeScript gateway + Rust services |
| Frontend | Tauri v2 | Rust backend + React, CrabCamera plugin |
| Vision | LFM2.5-VL-450M | GGUF Q4_0 (glasses), Q5_0 (laptop) |
| STT | whisper.cpp | base.en model, async + VAD |
| TTS | KittenTTS | <25MB, base variant |
| Memory | SQLite + flat vectors | In-process, no external deps |
| Camera | V4L2 | Linux native, provider model |

## Key Decisions

- **Vector store:** Flat in-process index → migrate to Qdrant in v2 if needed
- **STT model:** base.en (74MB) — right accuracy/size balance
- **VLM quantization:** Q4_0 for glasses, Q5_0 for laptop prototype
- **TTS variant:** base — good quality at reasonable size

## Open Risks

1. VLM power draw uncharacterized (3-8W estimate per inference burst)
2. Physical/form factor constraints not defined (weight, dimensions, battery)
3. Redax hardware not finalized

## Docs

- `docs/dan-glasses-architecture-v1-canonical.pdf` — Full canonical spec (27 pages)
- `docs/dan-glasses-build-plan.md` — Phase-by-phase build plan
- `docs/dan-glasses-v1-canonical-analysis.md` — Critical analysis of the spec
