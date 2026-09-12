---
type: routing-rules
project: ""
status: active
last_updated: 2026-09-12
confidence: medium
---

# Routing Rules

## Principle
Route by task; do not run every task through a chain of models.

## Preferred conceptual routing
- Scientific reasoning / paper synthesis / writing → strongest high-quality general reasoner; historically Gemma 4 31B in free OpenRouter stack.
- Autonomous execution / browser / terminal / repo → Nex N2.5 Mini.
- Focused code patch → Laguna XS 2.1.
- Figures/screenshots → Ling 3.0 Flash VL.
- Video/audio → Nemotron Nano Omni.
- Memory retrieval → local Nomic embeddings.
- High-value coding → ChatGPT Codex route when included.

## Escalation
- One primary model/task.
- Escalate only on failure, low confidence, or high-stakes verification.
- Bounded retries; summarize blockers rather than looping.

## Privacy
- Do not send unpublished/confidential work to a free endpoint without acceptable data policy.
- Prefer local/included private routes for sensitive research.
