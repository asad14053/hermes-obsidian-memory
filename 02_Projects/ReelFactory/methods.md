---
type: methods
project: "ReelFactory"
status: active
last_updated: 2026-09-12
confidence: high
---

# Reel Factory — Methods

1. Topic/hook.
2. Research + validation.
3. Script.
4. Asset plan.
5. Media acquisition.
6. Text/layout.
7. Optional voice/music.
8. FFmpeg/NVENC render.
9. QA.
10. Batch scheduling.

## Cost routing

- Local Qwen for bulk.
- Free cloud only when local quality is insufficient.
- Strong models only for hard research/synthesis.

## Audio

- ✅ DECISION: audio/TTS switchable off without regenerating script/assets.
- Preferred control: `--no-audio` or `audio.enabled=false`.
