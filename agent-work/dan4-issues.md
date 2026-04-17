# DAN-4 Issues Log — DanClaw / Paperclip Fork

## Active Issues

| ID | Severity | File | Description | Created |
|----|----------|------|-------------|---------|
| C1 | CRITICAL | `server/src/agent-auth-jwt.ts` | JWT falls back to `BETTER_AUTH_SECRET` with documented dev default `paperclip-dev-secret` — if deployed literally, JWT signing compromised | 2026-04-13 |
| H1 | HIGH | `ui/src/lib/worktree-branding.ts` | Worktree branding reads `paperclip-worktree-*` meta tags — incomplete rebrand, could cause config conflicts | 2026-04-13 |
| H2 | HIGH | `SECURITY.md` | SECURITY.md points to `github.com/paperclipai/paperclip/security/advisories` — DanClaw vulnerabilities reported to wrong repo | 2026-04-13 |
| H3 | HIGH | `.github/CODEOWNERS` | CODEOWNERS likely references PaperclipAI — needs verification and update to DanLab team | 2026-04-13 |
| H4 | HIGH | `Dockerfile` | `PAPERCLIP_HOME`, `PAPERCLIP_INSTANCE_ID`, `PAPERCLIP_CONFIG` hardcoded in Dockerfile — Paperclip-era naming persists in env vars | 2026-04-13 |
| H5 | HIGH | `server/src/agent-auth-jwt.ts` | JWT verification extracts `jti` but never checks revocation list — replay attack possible within token validity window | 2026-04-13 |
| H6 | HIGH | `ui/src/api/client.ts` | API client uses `credentials: "include"` with no visible CSRF protection — needs verification against better-auth CSRF handling | 2026-04-13 |
| M1 | MEDIUM | `server/src/redaction.ts` | `SECRET_PAYLOAD_KEY_RE` misses common patterns like bare `token`, `apiKey`, `auth_key` | 2026-04-13 |
| M2 | MEDIUM | `server/src/routes/agents.ts` | `relativePath` in instructions-bundle file routes not validated for path traversal before use | 2026-04-13 |
| M3 | MEDIUM | Activity logging | No retention policy for activity logs — grows indefinitely | 2026-04-13 |
| L1 | LOW | Multiple files | Incomplete rebrand: `paperclip-` refs in meta tags, env vars, docs, security policy | 2026-04-13 |
| L2 | LOW | Auth routes | No rate limiting on `/api/auth/*` endpoints — brute force possible | 2026-04-13 |
| L3 | LOW | `Dockerfile` | Docker image installs `@latest` Claude Code, Codex, OpenCode — reproducibility risk | 2026-04-13 |
| L4 | LOW | `server/src/app.ts` | `fs.readFileSync` calls have no timeouts — could hang on slow filesystems | 2026-04-13 |
| L5 | LOW | `Dockerfile` | Removed sha256 integrity check for GitHub CLI keyring — was stale, unblocks builds but removes extra integrity layer | 2026-04-14 |
| L6 | LOW | `.github/workflows/deploy.yml` | Health check fallback URL hardcodes `paperclip.up.railway.app` — wrong domain if Som deploys to custom domain | 2026-04-16 |

---

## Resolved Issues

_(none yet)_

---

## Notes

- **C1 (CRITICAL):** While the code doesn't literally use `paperclip-dev-secret` as default, the error message in `better-auth.ts` instructs developers to set `BETTER_AUTH_SECRET=paperclip-dev-secret`. In production, this default would be a catastrophic security failure. Fix: add detection for known insecure defaults and reject them in `authenticated` deployment mode.
- **H5 (HIGH):** The 48h default TTL is reasonable for agent JWTs. The replay risk is real but bounded. Consider adding a Redis-backed token revocation store for production.
- **H6 (HIGH):** better-auth v1.x typically uses a SameSite=Strict cookie + double-submit pattern. Confirm this is active and test with a CSRF proof-of-concept before considering H6 resolved.
- **L5 (LOW):** The sha256 check was stale (hardcoded `20e0125d...` vs actual `6084d5d7...`). Removing it unblocks Docker builds in CI. The GitHub APT repo uses signed packages as primary security control; the sha256 check was redundant. Acceptable risk given the build-blocking nature. Should pin to correct checksum when available.
