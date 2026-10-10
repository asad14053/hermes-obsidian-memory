---
type: agent-system
project: "Hermes"
status: active
last_updated: 2026-10-10
confidence: high
---

# Hermes

## Deployment

- Self-hosted on Hostinger VPS in Docker.
- Image: `ghcr.io/hostinger/hvps-hermes-agent:latest`
- Project: `/docker/hermes-agent-dvoy`
- Compose: `/docker/hermes-agent-dvoy/docker-compose.yml`
- Container historically: `hermes-agent-dvoy-hermes-agent-1`
- Internal port: `4860`

## Traefik / HTTPS

- Traefik container: `traefik-zbwr-traefik-1`
- `web` → `:80`
- `websecure` → `:443`
- cert resolver: `letsencrypt`
- HTTP→HTTPS redirect enabled
- Docker provider enabled
- `exposedByDefault=false`
- Historical host: `hermes-agent-dvoy.srv1974961.hstgr.cloud`
- Let’s Encrypt certificate validated successfully.
- ✅ DECISION: Hermes uses internal `expose: "4860"` behind Traefik rather than random public port.

## Obsidian

- Host: `/docker/hermes-agent-dvoy/data/obsidian-vault`
- Container: `/opt/data/obsidian-vault`
- Env: `OBSIDIAN_VAULT_PATH=/opt/data/obsidian-vault`
- Volume: `./data:/opt/data`
- Read/mount test succeeded with `Hermes-Test.md`.
- ✅ Hermes read/write access to the canonical vault is verified; scheduled curation can update notes under `/opt/data/obsidian-vault`.

## Google Calendar and Morning Brief

- Google Calendar OAuth was restored and returned `AUTHENTICATED` on 2026-10-06. Morning Brief runs subsequently read calendar events on October 8 and 9.
- Authorization is Calendar-only; Gmail, Drive, Docs, Sheets, and Contacts were not granted access.
- `Morning Brief` job `4a6f759f0b6f` is active, read-only, delivered to Telegram, and scheduled at `0 12 * * *` UTC (verified 2026-09-26).
- ⚠️ VERIFY whether the intended delivery requirement is fixed at 12:00 UTC (8:00 AM EDT / 7:00 AM EST) or should remain at one local America/Atlanta time throughout daylight-saving changes.

## Vault Git backup

- The backup succeeded on 2026-10-03 at 09:02 UTC: commit `d3f1b3de0463fb6a178039ab65bbb201053c2462` changed 140 files, was pushed to `origin/main`, and was verified remotely.
- ⚠️ VERIFY / stale as of the 2026-10-10 03:01 UTC health check: local `main` and `origin/main` still matched at `d3f1b3d`, but newer vault content was not yet backed up. The next weekly backup was scheduled for 09:00 UTC on October 10.
- The earlier deploy-key mismatch is historical; do not overwrite `/opt/data/.ssh/id_ed25519` merely to satisfy a key check if it recurs. Establish key ownership first.

## Bangladesh Monitor jobs

- ✅ DECISION: As of 2026-10-06, the Daily Bangladesh Ministry Signal Scanner (`c965622f69d0`), Daily Bangladesh-Breaking Story Trigger (`044d1d265167`), and Weekly-YT Bangladesh Editorial (`4653bac71ce2`) require reports and saved Markdown in fluent standard Bengali.
- Proper names, acronyms, technical terms, document titles, numbers, and URLs may remain in their original form when needed for accuracy.

## Scheduled-job reliability

- ⚠️ VERIFY why some scheduled sessions lack required tools: AI/news jobs on October 4 and 10 and NIA funding jobs on October 5 and 9 reported unavailable web and/or vault access; Bangladesh scanner runs on October 7 and 9 repeatedly retried `web_search` until the loop guardrail stopped them.
- Missing-tool output means **monitoring incomplete**, not “no news” or “no funding changes.” Jobs should fail fast after a repeated backend error and change strategy rather than issue the same search call dozens of times.

## Codex

- OAuth command used/planned: `hermes auth add openai-codex`.
- Goal: use included ChatGPT/Codex allowance for hard coding without separate API token billing.
- ⚠️ VERIFY exact models exposed by current subscription/client.

## UI

- Official dashboard chat is terminal/TUI-like.
- A separate Hermes Workspace frontend was discussed for graphical chat.
- ⚠️ verify third-party frontend provenance/security before production install.
