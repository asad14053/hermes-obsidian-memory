---
type: infrastructure
project: "Hermes"
status: active
last_updated: 2026-09-12
confidence: high
---

# AI / Agent Infrastructure

## Hostinger VPS
- always-on Hermes orchestration
- Docker services
- browser/tools
- Obsidian memory
- scheduling

## Docker
- Hermes project: `/docker/hermes-agent-dvoy`
- Hermes container: `hermes-agent-dvoy-hermes-agent-1`
- Traefik container: `traefik-zbwr-traefik-1`

## Reverse proxy
- Traefik TLS + Let’s Encrypt.
- Hermes internal port 4860.
- ✅ use `expose`, not random public mapping.

## Obsidian
- host: `/docker/hermes-agent-dvoy/data/obsidian-vault`
- container: `/opt/data/obsidian-vault`
- canonical long-term human-readable memory.

## Home workstation
- local LM Studio + GPUs for zero-cost inference/embeddings.
- Tailscale was discussed as a preferred private-network option.
