---
type: project-state
project: "ReelFactory"
status: active
last_updated: 2026-09-12
confidence: high
---

# Reel Factory — Current State

## Historical local stack

- Windows.
- Python 3.14.5.
- pip 26.1.2.
- git 2.52.0.
- Node 24.14.0.
- npm 11.9.0.
- Docker 29.7.2.
- FFmpeg with `h264_nvenc` / `hevc_nvenc`.

## LM Studio

- Server historically on port `1234`.
- `qwen3-8b` (~5.03 GB) loaded.
- `text-embedding-nomic-embed-text-v1.5` (~84 MB).
- `/v1/models` and `/v1/chat/completions` tested.

## GPU

- RTX 3060 12 GB GPUs.
- Historically 3 available; motherboard supports 2.
- Observed usage during tests:
  - GPU0 ~6.8 GB
  - GPU1 ~5.5 GB

## Routing code

Historical config used `model`, `base_url`, `temperature`, `/chat/completions`.
Route classes included:
`historical_specific`, `person_specific`, `institution_specific`, `geopolitical_map`, `generic_concept`.

⚠️ VERIFY current code/config paths.
