---
type: todo
project: "AIVC"
status: active
last_updated: 2026-09-13
confidence: medium
---

# AIVC — TODO and Next Actions

## Priority 1 — Freeze the premise and benchmark

- TODO Write `aging_AD_AIVC_premise_v1.md` with exactly one aging/AD question and one population-level response estimand.
- TODO Select one primary public perturbation-response dataset and one independent validation dataset; verify donor, perturbation, age/disease-context, cell-type, batch, dose, and time metadata.
- TODO Prespecify donor-, perturbation-, context-, and dataset-held-out splits; generate fold manifests and verify zero donor or perturbation overlap.
- TODO Freeze the primary energy-distance metric, negative controls, and a provisional go/no-go rule of at least 10% improvement over the strongest context-agnostic simple baseline across a majority of held-out folds, with the direction replicated externally.

## Priority 2 — Establish a baseline before architecture work

- TODO Run no-change/control-mean, perturbation-mean, nearest-neighbor transfer, and additive/ridge baselines on the frozen folds.
- TODO Compare the matched additive model with and without aging/AD context; include shuffled-context and donor-bootstrap checks.
- TODO Create the experiment registry when the first baseline run is complete.

## Deferred until the premise is supported

- TODO Define graph construction/update rules and compare graph, transformer, and hybrid models only after a leakage-resistant baseline establishes a real prediction gap.
- TODO Decide whether and how GeneBridge spatial context enters AIVC without implying perturbation evidence that GeneBridge does not contain.
