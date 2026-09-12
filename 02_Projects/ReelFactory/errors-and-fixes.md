---
type: errors-fixes
project: "ReelFactory"
status: active
last_updated: 2026-09-12
confidence: high
---

# Reel Factory — Errors and Fixes

## Bengali TTS

- A test produced repetitive/nonsensical syllables.
- ✅ LESSON: validate TTS independently before batch enabling.
- ✅ DECISION: maintain no-audio fallback.

## Code/config stability

- Historical snippets became malformed during iterative editing.
- ✅ LESSON: keep config/orchestrator in version control and syntax-test before batch jobs.

## GPU constraint

- Three GPUs may exist physically, but motherboard supports only two simultaneously.
