---
type: methods
project: "AIVC"
status: active
last_updated: 2026-09-12
confidence: high
---

# AIVC — Methods

## Candidate families

- Graph neural networks.
- Graph + transformer hybrids.
- Pure transformer with genes as tokens.
- Causal/perturbation-response models.
- Multi-view representation learning.

## Pure-transformer idea previously discussed

- Remove explicit graph.
- Gene = token.
- Input diseased expression + perturbation/desired-state information.
- Predict treated/target response.
- Relationships learned through attention.
- Evaluate whether attention generalizes rather than learns shortcuts.

## Core questions

- Which graph is biologically justified?
- Static or learned/updateable graph?
- Gene graph, cell graph, or multi-scale?
- How to represent perturbation?
- How to handle unseen perturbations?
- How to add spatial context?
