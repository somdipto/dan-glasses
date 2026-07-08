# DAN-4 — TTS + Memory Stream

## Status: SHIPPED ✅

All four parts live and tested.

## Live services (2026-07-08 13:30 IST)

| svc | port | status | pid |
|---|---|---|---|
| memoryd | 8741 | ok | 4929 |
| toold | 8742 | ok | 117 |
| ttsd | 8743 | ok | 120 |
| audiod | 8090 | ok | 88 |
| perceptiond | 8092 | ok | 7161 |
| dan-glasses-app | 8747 | ok | 89 |

Aggregator: 5/5 up, ~30ms total latency.

## Part A — memoryd (Services/memoryd/memoryd.py)

- FastAPI + aiosqlite + sentence-transformers (all-MiniLM-L6-v2, 384-dim)
- WAL, NORMAL sync, persistent DB at .cache/dan-glasses/memoryd/state.db
- /health, /ready (180s wait for model), /memories, /conversations, /query
  (cosine via numpy), /memories/by-type/{type}, /memories/{id}, /stats,
  /v1/embeddings (OpenAI-compatible)
- 1011 memories already in DB (805 episodic, 95 procedural, 111 semantic)
- 32/32 tests green

## Part B — toold (Services/toold/toold.py)

- FastAPI + asyncio subprocess
- /exec (shell, allowlist blocks ;, |, \`, $(, >, <, newlines)
- /exec/python, /exec/file (.py → python3, .sh → bash)
- /registry CRUD + /registry/{name}/{enable,disable}
- /exec/with-tool uses registry templates
- /test self-probe exercises shell+python+registry+file
- 21/21 tests green

## Part C — ttsd (Services/ttsd/ttsd.py)

- KittenTTS Python API (model = "medium")
- 8 voices: expr-voice-{2,3,4,5}-{m,f}
- /speak → audio/wav (24kHz mono IEEE Float), ~199KB / ~2s latency
- /play → synthesize + aplay
- 6/6 tests green

## Part D — BootstrapWizard (apps/dan-glasses-app/src/components/BootstrapWizard.tsx)

- Polls /api/services/health every 3s (single round trip)
- Step list now: memoryd · toold · ttsd · audiod · perceptiond · **devices**
- "devices" step:
  - navigator.mediaDevices.enumerateDevices() (cams/mics/speakers count)
  - getUserMedia(audio) → 800ms analyser → peak RMS
  - Re-enumerate post-permission to unlock device labels
  - Detail line: "mic: 0.012 RMS · 2 cameras · mic error: ..."
- Final summary includes Devices check
- 55/55 dan-glasses-app tests green
- TypeScript typecheck clean, vite build clean (226 KB JS)

## Files changed

- Services/memoryd/* (already on master, just verified)
- Services/toold/* (already on master, just verified)
- Services/ttsd/* (already on master, just verified)
- apps/dan-glasses-app/src/components/BootstrapWizard.tsx (added device probe)
- agent-work/dan4.md (this file)

## Commit

7d729c0 — DAN-4: memoryd+toold+ttsd wiring, wizard device probe, full e2e green

## Test totals: 114/114

- memoryd: 32
- toold: 21
- ttsd: 6
- dan-glasses-app: 55
