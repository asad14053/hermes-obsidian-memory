---
type: methods
project: "AIVC"
status: active
last_updated: 2026-09-23
confidence: high
---

# AIVC — Methods

## User-supplied design — received September 23, 2026

The authoritative supplied design and page/module citations are in [[02_Projects/AIVC/project-outline]]. Its core is **identity + environment → universal representation (UR) → virtual instrument (VI) → cell-type-specific activity**, with identity held fixed for environment counterfactuals.

- **PDF specification:** scGPT/UCE identity embedding; 20 μm, cell-type-stratified distance-weighted neighbor expression; feature attention and prediction head; MSE plus sparsity.
- **Accompanying diagram:** Xenium, snRNA-seq, Visium, and Perturb-seq; multi-scale hierarchical cross-attention; identity/environment interaction features; perturbation embedding; conditional VAE; confidence-weighted imputed-expression and other losses.
- Preserve these as distinct proposed specifications, not one silently merged implementation. Dimensions, source equations, evaluation differences, and unresolved notation are documented in the outline. No new training or validation result was supplied.

## Earlier explorations

The alternatives below are historical discussion, not a substitute for the supplied outline; no formal rejection was inferred.

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
