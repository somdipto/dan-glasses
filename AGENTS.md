# AGENTS.md — Dan Glasses Workspace

## Project Context
Dan Glasses: wearable AI companion. Voice + vision + memory + TTS, OpenClaw orchestration, edge hardware (Redax aarch64 + Linux laptop x86_64).

## Key Decisions (Locked)
- Vision: LFM2.5-VL-450M via llama.cpp GGUF Q4_0
- STT: whisper.cpp via whisper-cpp-plus-rs (async + VAD)
- TTS: KittenTTS base (<25MB)
- Orchestration: OpenClaw gateway (TypeScript/Node)
- Frontend: Tauri v2 + React
- Camera: V4L2 + CrabCamera plugin
- Memory: SQLite + in-process vectors
- Packaging: .deb + systemd (NOT Flatpak/AppImage)
- Build: Desktop prototype first (x86_64), then Redax (aarch64)

## Critical Risks
1. VLM power draw uncharacterized — dominant power event
2. OpenClaw is TS/Node — not Rust, but accepted as orchestration layer
3. Redax hardware timeline unknown — software dev on x86_64 laptop
4. Form factor constraints (weight, battery) not finalized

## Build Priority
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

## File Locations
- Canonical docs: `docs/`
- Dev notes: `agent-work/`
- Frontend: `apps/dan-glasses/`
- Services: `Services/{perceptiond,audiod,memoryd,os-toold,toold}/`
- Shared types: `shared/`
- Packaging: `packaging/{debian,systemd}/`
