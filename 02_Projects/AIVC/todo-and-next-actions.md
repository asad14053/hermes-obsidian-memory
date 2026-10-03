---
type: todo
project: "AIVC"
status: active
last_updated: 2026-10-03
confidence: medium
---

# AIVC — TODO and Next Actions

## Priority 1 — Freeze the premise and benchmark

- TODO Resolve program scope explicitly: keep canonical AIVC SCZ-centered with a separate NIA aging/AD feasibility branch, or approve an aging/AD organizing question. Do not let grant framing silently replace the user-supplied SCZ design.
- TODO Complete a bounded aging/AD feasibility audit with one system/population, context or exposure, perturbation class, measured endpoint, donor/replicate metadata, identifiable donor-level design, and feasible validation route. End with a documented **commit/no-go**.
- TODO If the feasibility gate passes, write `aging_AD_AIVC_premise_v1.md` with exactly one aging/AD question and one population-level response estimand; select primary and external-validation datasets and verify donor, perturbation, age/disease context, cell type, batch, dose, and time metadata.
- TODO Prespecify donor-, perturbation-, context-, and dataset-held-out splits; generate fold manifests and verify zero donor or perturbation overlap.
- ? UNCERTAIN The primary metric and numerical improvement threshold are provisional until the estimand and endpoint are selected. Energy distance is suitable only for a distributional target, and the prior ≥10% rule is not an approved project decision.

## Priority 2 — Establish a baseline before architecture work

- TODO Run no-change/control-mean, perturbation-mean, nearest-neighbor transfer, and additive/ridge baselines on the frozen folds for the selected estimand.
- TODO Run a bounded SCZ engineering pilot on locked GeneBridge donor splits and measured Xenium targets: compare identity-only, identity plus cell-type-stratified pooled context, and a small context MLP; include focal-cell exclusion, fold-local preprocessing, and matched replacement/shuffle tests.
- TODO Label the GeneBridge pilot as SCZ engineering evidence only—not aging/AD, causal, or perturbation evidence.
- TODO Create the experiment registry when the first baseline run is complete.

## Deferred until the premise is supported

- TODO Define graph construction/update rules and compare graph, transformer, and hybrid models only after a leakage-resistant baseline establishes a real prediction gap.
- TODO Decide whether and how GeneBridge spatial context enters AIVC without implying perturbation evidence that GeneBridge does not contain.
