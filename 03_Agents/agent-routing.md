---
type: routing
project: "Hermes"
status: active
last_updated: 2026-09-12
confidence: medium
---

# Agent Routing

## Goal
Best quality while avoiding paid API tokens.

## Conceptual routing
- Scientific reasoning / papers / writing → strongest free general reasoner; historically Gemma 4 31B.
- Autonomous execution / browser / terminal / repo → Nex N2.5 Mini.
- Focused code repair → Laguna XS 2.1.
- Figures/screenshots → Ling 3.0 Flash VL.
- Video/audio → Nemotron Nano Omni.
- Memory retrieval → local Nomic embeddings.
- High-value coding → ChatGPT Codex OAuth when included.

## Historical Codex plan
A previous plan discussed Luna/Terra/Sol and an “Astra” lane.
⚠️ VERIFY exact current model names/availability before configuring aliases.

## Rule
- One primary model per task.
- Escalate only on failure/high-stakes verification.
- Avoid model roulette.
- Preserve free request quota.
