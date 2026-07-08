# DAN-4 — TTS + Memory + Tool + Wizard Stream

**Date:** 2026-07-08
**Mission:** TTS + Memory services (toold + memoryd) + bootstrap wizard UI.

## Status snapshot (entry)

| Service  | Port | File                                                 | Running? |
| -------- | ---- | ---------------------------------------------------- | -------- |
| memoryd  | 8741 | `Services/memoryd/memoryd.py`                        | yes (loading model) |
| toold    | 8742 | `Services/toold/toold.py`                            | yes |
| ttsd     | 8743 | `Services/ttsd/ttsd.py`                              | yes (KittenTTS) |
| os-toold | 8744 | `Services/os-toold/os_toold.py`                      | yes (other) |
| app      | 8744 | `Services/dan-glasses-app/server.py`                 | yes |

App is at `apps/dan-glasses-app/` (React + Tauri). SPECs already exist for all three services. Existing wizard polls `/health` aggregator and does a full TTS/memory/tool roundtrip.

## Tasks

- [ ] Verify all 3 services' /health + /ready
- [ ] Run memoryd tests + toold tests + ttsd tests
- [ ] Validate the React wizard builds and serves
- [ ] Tighten any stale gaps (model loading is the long pole)
- [ ] Update scratch pad with results

## Run order
1. memoryd (model warmup is slow, ~25s)
2. toold (instant)
3. ttsd (KittenTTS first call slow, ~3.8s)
4. wizard (build + smoke test)
