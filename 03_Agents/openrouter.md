---
type: model-provider
project: "Hermes"
status: active
last_updated: 2026-09-12
confidence: high
---

# OpenRouter

## Policy

- Goal: **$0 additional token spend**.
- Use `:free` endpoints unless explicitly approved otherwise.
- Verify free availability/rate limits before production.
- Review provider data-use policy for unpublished/confidential work.

## Free models evaluated

### Reasoning
- `google/gemma-4-31b-it:free`
- `google/gemma-4-26b-a4b-it:free`

### Agent/coding
- `nex-agi/nex-n2.5-mini:free`
- `poolside/laguna-xs-2.1:free`

### Vision/multimodal
- `inclusionai/ling-3.0-flash-vl:free`
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`

### Retrieval
- `nvidia/nemotron-3-embed-1b:free`
- `nvidia/llama-nemotron-embed-vl-1b-v2:free`
- `nvidia/llama-nemotron-rerank-vl-1b-v2:free`

### TTS
- `fish-audio/s2.1-pro-free:free`
- `deepgram/flux-tts:free`

## Historical quality-first roles

- Gemma 4 31B → thinker/scientific explainer.
- Nex N2.5 Mini → autonomous execution/browser/terminal/code.
- Laguna XS 2.1 → specialist code repair.
- Ling 3.0 Flash VL → screenshots/figures/plots.
- Nemotron Omni → video/audio perception.

⚠️ VERIFY current endpoint IDs/status.
