---
type: agent-system
project: "Hermes"
status: active
last_updated: 2026-09-13
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

## Codex

- OAuth command used/planned: `hermes auth add openai-codex`.
- Goal: use included ChatGPT/Codex allowance for hard coding without separate API token billing.
- ⚠️ VERIFY exact models exposed by current subscription/client.

## UI

- Official dashboard chat is terminal/TUI-like.
- A separate Hermes Workspace frontend was discussed for graphical chat.
- ⚠️ verify third-party frontend provenance/security before production install.
