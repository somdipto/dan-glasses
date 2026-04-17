# Dan Glasses — Folder Index

```
dan-glasses/                           ← Project root
├── AGENTS.md                          ← Agent memory
├── SOUL.md                            ← Project personality
├── README.md                          ← Project overview
├── INDEX.md                           ← This file
│
├── apps/                              ← Application layer
│   └── dan-glasses-app/               ← Tauri v2 React frontend
│
├── Services/                          ← Rust microservice binaries
│   ├── perceptiond/                  ← Camera + VLM inference
│   ├── audiod/                        ← Audio capture + VAD + STT
│   ├── memoryd/                       ← SQLite + vector store
│   ├── os-toold/                      ← Command execution guardrails
│   └── toold/                         ← TTS synthesis
│
├── agent-work/                        ← Internal agent notes, reviews
│   ├── dan1.md, dan2.md, dan4.md     ← Agent journals
│   ├── dan4-reviews/                  ← Daily review logs
│   └── REVIEW_LOOP.md
│
├── shared/                            ← Shared types, IPC contracts
├── models/                            ← Model weights (downloaded on first run)
├── packaging/                         ← .deb + systemd units
│   ├── debian/
│   └── systemd/
├── scripts/                           ← Dev helpers, build scripts
├── tests/                             ← Test suites
├── research/                          ← Research notes
│
└── docs/                              ← Specs, analysis, build plan
    ├── dan-glasses-architecture-v1-canonical.pdf
    ├── dan-glasses-build-plan.md
    └── dan-glasses-v1-canonical-analysis.md
```

## Service Responsibilities

| Service | Responsibility | IPC |
|---------|---------------|-----|
| perceptiond | V4L2 → frame → LFM2.5-VL-450M → description | Unix socket or gRPC |
| audiod | ALSA → VAD (Silero) → whisper.cpp → text | Unix socket or gRPC |
| memoryd | SQLite + flat vector index | Unix socket or gRPC |
| os-toold | Sandboxed command execution | Unix socket or gRPC |
| toold | KittenTTS text → audio | Unix socket or gRPC |

## Model Weights (downloaded on first run)

| Model | Size | Purpose |
|-------|------|---------|
| LFM2.5-VL-450M Q4_0.gguf | ~450MB | Vision (glasses) |
| LFM2.5-VL-450M Q5_0.gguf | ~550MB | Vision (laptop prototype) |
| whisper base.en | 74MB | Speech-to-text |
| kitten-base | ~25MB | Text-to-speech |
