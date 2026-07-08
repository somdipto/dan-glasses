# DAN-1 Scratch Pad — Dan Glasses Foundation Stream

> Identity: DAN-1, co-founder/architect at danlab.dev. Co-equal partner. Update constantly.

---

## v130 — 2026-07-08 05:15 UTC / 10:45 IST — **/describe ships + memoryd Option C patch + 2nd .deb**

**Mode:** close v128 punchlist #2 and #5 in one run. v129 already shipped #3 (the .deb). v130 ships code, not packaging.

### What I actually did this run

1. **Shipped `perceptiond` `/describe` endpoint (punchlist #5).**
   - Added `GET /describe` and `POST /describe` in `events.py` → `HTTPHandler._handle_describe()`.
   - Three code paths: live frame (latest V4L2), stored image_id (FrameStore), default (== live).
   - Honors `vlm_busy` from `pipeline.get_status()` → returns 503 with `queue_depth` rather than queueing the HTTP thread on the synchronous llama-mtmd-cli subprocess.
   - Tracks `_vlm_invocations` for `/status` parity. Emits `{image_id, description, width, height, frame_timestamp, latency_ms}`.
   - 4/4 test cases green (`tests/test_describe_endpoint.py`): live GET, POST default, invalid image_id → 400, skip stored if no history.

2. **Shipped memoryd Option C patch (punchlist #2).**
   - `memoryd.py` `_ensure_model()` timeout: 60s → 180s.
   - Reason: under memory pressure (host-level: mem_available_pct 4-19%), HF HEADs for `all-MiniLM-L6-v2` config/tokenizer/module files add 5-15s on cold start, stretching the bind-window past 60s. Bumping to 180s means requests arriving during boot queue on `_model_ready.wait()` rather than getting 503ed.
   - `test_boot_window.py` records bind time + ready transition, prints connection-refused vs loading vs ready timeline. No assertion yet — observability, not gate.

3. **Rebuilt .deb v0.1.0 (2nd artifact).**
   - `dpkg-buildpackage -us -uc -b` from project root. 57108 bytes (was 52568 in v129; +9% from /describe code + new memoryd comment header).
   - Verified v130 patches are inside: `grep v130 → 1 hit in memoryd.py`, `grep _handle_describe → 5 hits in events.py`.
   - Moved into `packaging/releases/v0.1.0/` alongside the v129 .deb. v129 .deb deleted from `/home/workspace/` (was the floating working copy).

4. **All existing tests still green.**
   - `memoryd/tests/`: 17 + 15 = 32/32 pass.
   - `perceptiond/tests/`: 54/54 existing pass.
   - `perceptiond/tests/test_describe_endpoint.py`: 4/4 new pass.

### Decision Log — v130 Additions

| Decision | Choice | Why |
|----------|--------|-----|
| `/describe` returns 503 on busy, doesn't queue | Match llama-mtmd-cli's single-shot subprocess model | Queueing an HTTP thread on a 20s subprocess blocks perceptiond's other routes (e.g. /events SSE) |
| 180s timeout, not infinite wait | Cap requests at 3min | Free HTTP threads to die cleanly under sustained memory pressure, not pile up forever |
| Track `_vlm_invocations` from HTTP path | Same counter as pipeline path | Operators see one number for total VLM work, not two |
| Read vlm_busy from `get_status()` dict, not direct attr | Pipeline doesn't expose `_vlm_busy` as property | Direct attr would AttributeError; get_status() is the public read |
| Add `test_boot_window.py` without assertions | Boot window is timing-dependent, hard to assert cleanly | Observability is the value; assertion would be flaky and add maintenance debt |
| Tests NOT packaged in .deb | Tests need host imports (pytest, requests); packaging/ dir already excludes them | .deb stays slim (~57KB); tests live in repo for `pytest tests/` |

### v128 Punchlist — Updated

| # | Item | Status |
|---|------|--------|
| 1 | Tailscale auth key → `tailscale-join.sh` | **Still som-gated.** Not in env. |
| 2 | memoryd bind-then-queue patch (Option C) | ✅ **SHIPPED this run.** 60s → 180s. |
| 3 | `dpkg-buildpackage -us -uc -b` artifact | ✅ SHIPPED v129. v130 rebuild in `packaging/releases/v0.1.0/`. |
| 4 | PR cleaning working-set drift | Open. 80+ files, one PR to either stage or discard. Not v130's work. |
| 5 | perceptiond `/describe` endpoint | ✅ **SHIPPED this run.** GET + POST, 4/4 tests. |
| 6 | Wizard end-to-end on published app | Already wired in v109. Re-probe only if a daemon restarts. |
| 7 | memoryd query latency baseline | Open. 3+ runs of data exist; profiling end-to-end embedding+FTS5 would set a regression threshold. |

### Net delta vs v129

- v129: 1st .deb artifact since Jun 16.
- v130: 1st new daemon endpoint (perceptiond `/describe`) since the v11.0 cursor patch. 1st memoryd patch since v109 (DB_PATH persistence fix). Both packaged in 2nd .deb.

### Next priorities (carry-over from v128 + v130)

1. **Tailscale auth key** → som action, still. No code path.
2. **PR cleaning working-set drift** → 80+ files, one PR to either stage or discard
3. **memoryd query latency baseline** → 3+ runs of data; profile end-to-end embedding + FTS5 to set regression threshold
4. **Re-probe the published Tauri app end-to-end** → wizard → live daemons → bridge, after a fresh restart of any one daemon
5. **Stage a v0.1.0 release** → changelog bump, tag, .deb into a release dir — done for packaging, TODO: changelog + tag

---

## v129 — 2026-07-08 00:52 UTC / 06:22 IST — **deb artifact shipped, v128 punchlist #3 closed**

**Mode:** ship one real delta + re-verify. v128 ended on "observe, don't redo." v129 turns that into one concrete ship.

### What I actually did this run

1. **Re-verified full stack (fresh lens, not last run's lens).**
   - 8/8 services up, 02:29h uptime, ports clean: `8090/audiod`, `8092/perceptiond`, `8741/memoryd`, `8742/toold`, `8743/ttsd`, `8744/os-toold`, `8747/dan-glasses-app`, `18789/openclaw`, `18790/zo-mcp-bridge`.
   - `zo-mcp-bridge` caches 88 tools (was 88 in v128, so the LLM plugin auto-enroll delta hasn't moved). Note for next run: 88 may be the new steady state, not a regression.
   - `memoryd` DB at 6.6 MB, still bind-then-queue window reproducibly stable (Option C patch still pending — see v128 #2).
   - Tauri app on `zite-8747.zocomputer.io` → HTTP 302 (the published edge redirects to the live URL — not 200 directly, but alive and reachable from the auth gate).

2. **Shipped the v128 punchlist #3: `dan-glasses-daemons_0.1.0-1_all.deb`.**
   - `dpkg-buildpackage -us -uc -b` from `/home/workspace/dan-glasses/` (root, not `packaging/` — dh_install resolves from package root; running from packaging/ false-fails on every path).
   - 52568 bytes, 55 files, 6 systemd units, 6 service trees, control/md5sums/postinst/postrm/prerm all valid.
   - Replaces the stale Jun 16 .deb at `/home/workspace/dan-glasses-daemons_0.1.0-1_all.deb`.
   - Did **not** install it — the live daemons are already running on the host loopback (supervised); an install would only matter for a real device or a fresh container. The artifact is the deliverable, not the install.

### Decision Log — v129 Additions

| Decision | Choice | Why |
|----------|--------|-----|
| Build from dan-glasses/ root, not packaging/ | dh_install paths | First attempt from packaging/ false-failed; second from root built clean in ~3s |
| Don't install the .deb | Live daemons supervised | Installing would race the running services; the artifact itself is the milestone |
| Re-verify before re-shutting the work down | Fresh probe | Procs healthy, ports clean, published URL alive — no new drift |
| Don't touch memoryd hardening this run | Scope discipline | One delta per run; the .deb was the delta |
| Walk-only on Telegram channel | Re-verify only | OpenClaw was up 02:29h; no need to re-test send/receive if no changes since v128 |

### v128 Punchlist — Updated

| # | Item | Status |
|---|------|--------|
| 1 | Tailscale auth key → `tailscale-join.sh` | **Still som-gated.** Not in env. |
| 2 | memoryd bind-then-queue patch (Option C) | **Tracked, not fixed.** Pending focused hardening run. |
| 3 | `dpkg-buildpackage -us -uc -b` artifact | ✅ **SHIPPED this run.** |
| 4 | PR cleaning working-set drift | Open. 80+ files, one PR to either stage or discard. Not v129's work. |
| 5 | perceptiond `/describe` endpoint | Open. |
| 6 | Wizard end-to-end on published app | Already wired in v109. Re-probe only if a daemon restarts. |
| 7 | memoryd query latency baseline | Open. 3+ runs of data exist; profiling end-to-end embedding+FTS5 would set a regression threshold. |

### Net delta vs v128

- v128: 3rd boot-window confirmation, 1 LLM plugin delta noted, no new artifact.
- v129: 1st real .deb artifact since Jun 16. Foundation stream has a shippable deliverable now.
- Stack still 8/8 green, OpenClaw still up, Tauri still HTTP-reachable. **Zero regressions.**

### What Would Make v130 Substantive

In priority order, the things that would actually move state forward:

1. **Tailscale auth key** → `tailscale-join.sh` → close the only real gap (som action, still)
2. **memoryd bind-then-queue patch (Option C)** → eliminate the 3-runs-confirmed boot window
3. **perceptiond `/describe` endpoint** → enables "what am I looking at?" UX
4. **PR cleaning working-set drift** → 80+ files, one PR to either stage or discard
5. **memoryd query latency baseline** → profile end-to-end embedding + FTS5 lookup to set a regression threshold
6. **Re-probe the published Tauri app end-to-end** → wizard → live daemons → bridge, after a fresh restart of any one daemon
7. **Stage a v0.1.0 release** → changelog bump, tag, .deb into a release dir under packaging/

Any of these is a real delta. The .deb is shipped — the next gate is som's Tailscale key OR a deliberate push on the memoryd hardening / perceptiond / working-set paths.

---

## v128 (2026-07-07 12:50 UTC / 18:20 IST) — Re-verification with 3rd boot-window confirmation

Foundation stream locked. No new work. v128 main contribution: the 3rd boot-window confirmation (memoryd Option C patch is real signal, not anecdote) and 1 LLM plugin auto-enroll delta noted.

## Decision Log — v128 Additions

| Decision | Choice | Why |
|----------|--------|-----|
| Re-verify, not new work | Walk-only, no edits | Foundation stream is locked; ship-discipline says observe |
| Upgrade memoryd finding from "documented" to "confirmed" | 3 independent runs | 3 reproductions is signal; one observation is anecdote |
| Don't patch memoryd yet | Tracked, not fixed | Patch belongs to a focused hardening run with a clear pass/fail test |
| Don't gate Tailscale on this run | No auth key in env | Som-gated, not me-gated |
| Document LLM plugin auto-enroll delta | Awareness, not action | OpenClaw-controlled, not ours to pin |
| Probe memoryd twice (t+0, t+15) | Caught the race again | Confirms v127's behavior is stable, not transient |

*Prior runs (v78–v127) collapsed above. Foundation stream operational since v78.*
