---
type: agent-system
project: "Hermes"
status: active
last_updated: 2026-10-03
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

- Google Calendar OAuth was verified with a live API read on 2026-09-21, but scheduled runs from 2026-09-29 through 2026-10-02 reported the authorization expired or revoked and could not read the calendar.
- Authorization is Calendar-only; Gmail, Drive, Docs, Sheets, and Contacts were not granted access.
- ⚠️ VERIFY Calendar access after rotating the OAuth Desktop client credentials and reauthorizing; do not treat the September 21 success as current operational status.
- `Morning Brief` job `4a6f759f0b6f` is active, read-only, delivered to Telegram, and scheduled at `0 12 * * *` UTC (verified 2026-09-26).
- ⚠️ VERIFY whether the intended delivery requirement is fixed at 12:00 UTC (8:00 AM EDT / 7:00 AM EST) or should remain at one local America/Atlanta time throughout daylight-saving changes.

## Vault Git backup

- ⚠️ VERIFY / unresolved as of 2026-10-03: local `main` and `origin/main` remain at `c6865a7` (`2026-09-13T02:23:13Z`), while newer tracked modifications and untracked vault notes exist.
- The 2026-09-26 backup aborted before commit/push because the public key derived from `/opt/data/.ssh/id_ed25519` did not match the backup job's configured expected public key.
- Next action: confirm the intended GitHub deploy-key identity, reconcile the configured expected public key with the existing key only after ownership is established, then rerun and verify the backup commit remotely. Do not overwrite the private key merely to make the check pass.

## Codex

- OAuth command used/planned: `hermes auth add openai-codex`.
- Goal: use included ChatGPT/Codex allowance for hard coding without separate API token billing.
- ⚠️ VERIFY exact models exposed by current subscription/client.

## UI

- Official dashboard chat is terminal/TUI-like.
- A separate Hermes Workspace frontend was discussed for graphical chat.
- ⚠️ verify third-party frontend provenance/security before production install.
