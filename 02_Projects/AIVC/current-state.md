---
type: project-state
project: "AIVC"
status: active
last_updated: 2026-11-08
confidence: medium
---

# AIVC — Current State

- Learning/design phase.
- Prior work covered PDGrapher, CellOT, causal ML networks, graph structure for ST, pure-transformer alternatives, perturbation masks, target-response prediction.
- User has specifically asked:
  - model inputs,
  - latent confounders,
  - graph construction/update,
  - code/data graph representation,
  - “tier 2” meaning in method context.
- ? UNCERTAIN exact current implementation branch/repository.

## Evidence gaps affecting the next phase

### Source update — September 23, 2026

- The user supplied a two-page broad outline and a multimodal architecture diagram, now preserved in [[02_Projects/AIVC/project-outline]]. A concrete proposed UR/VI architecture and evaluation plan are therefore documented; implementation and experimental completion are not established by this upload.
- The PDF proposes 20 μm cell-type-stratified distance-weighted neighborhoods, attention-based activity prediction, and identity-matched environment-swap validation. The image proposes a richer multimodal, multi-scale conditional-VAE extension and explicit donor-held-out tests. Neither was designated to replace the other.
- The image explicitly includes SCZ/NTC brain context; the broad PDF does not mandate a disease. Prior NIA aging/AD recommendations remain application-specific assistant proposals, not an approved replacement of the user's research scope.

### Latest review context — November 8, 2026

- The [[02_Projects/AIVC/reviews/2026-11-08-NIA-K99-study-section-review|November 8 NIA K99 review]] remains **Overall Impact 8/9 — STAGNANT** relative to November 7. No newly documented aging/AD premise-and-access decision, executed AIVC benchmark, frozen GeneBridge evidence package, or committed training/independence package was found; this does not establish absence of work elsewhere.
- The latest supplied literature and funding outputs remain November 6. Literature monitoring adds comparators and safeguards rather than project results; the funding check could not access official sources, so eligibility, deadlines, NOFOs, and policy changes remain unverified.
- The first action remains the aging/AD premise-and-access **COMMIT/NO-GO**. Canonical SCZ scope is unchanged.

### Previous review context — November 7, 2026

- The [[02_Projects/AIVC/reviews/2026-11-07-NIA-K99-study-section-review|November 7 NIA K99 review]] remained **Overall Impact 8/9 — STAGNANT** relative to November 1. No newly documented aging/AD premise-and-access decision, executed AIVC benchmark, frozen GeneBridge evidence package, or committed training/independence package was found; this does not establish absence of work elsewhere.
- November 2–6 literature monitoring strengthened controls for replicate ceilings, composition versus state, graph priors, perturbation specificity, and independent-unit splits. These narrow architecture-only novelty but do not provide project results.
- The November 6 funding radar could not access live official sources, so current eligibility, deadlines, NOFOs, and policy changes remain unverified. The first action remains the aging/AD premise-and-access **COMMIT/NO-GO**. Canonical SCZ scope is unchanged.

### Previous review context — November 1, 2026

- The [[02_Projects/AIVC/reviews/2026-11-01-NIA-K99-study-section-review|November 1 NIA K99 review]] remains **Overall Impact 8/9 — STAGNANT** relative to October 31. No newly documented benchmark, aging/AD premise/access decision, frozen GeneBridge evidence package, or training/independence commitment was found; this does not establish absence of work elsewhere.
- At the November 1 review cutoff, the latest available literature radar was October 30 and added comparators and safeguards, not project results. Subsequent November 2–6 monitoring is summarized below. The supplied October 30 funding output was `[SILENT]` and supplied no official eligibility/deadline determination.
- The first action remains the aging/AD premise-and-access **COMMIT/NO-GO**. Canonical SCZ scope was not changed.

### Previous review context — October 31, 2026

- The [[02_Projects/AIVC/reviews/2026-10-31-NIA-K99-study-section-review|October 31 NIA K99 review]] remained **Overall Impact 8/9 — STAGNANT** relative to October 25. No newly documented benchmark, completed aging/AD premise/access decision, frozen GeneBridge result package, or training/independence commitment was found in the reviewed notes; this does not establish absence of work elsewhere.
- October 26–30 monitoring strengthened independent-unit, donor-aware, transfer, uncertainty and interpretation controls and further narrowed architecture-only novelty. These are literature-derived constraints, not project results. The October 30 funding output was `[SILENT]` and supplied no official eligibility/deadline determination.
- The first action remained the aging/AD premise-and-access **COMMIT/NO-GO**. Canonical SCZ scope was not changed.

### Research monitoring — November 2–6, 2026

- The November 2–6 radar adds evaluation constraints, not an AIVC result or scope change. GENESIS makes replicate-reliability ceilings and distributional scoring useful benchmark references; its reported transfer is not established for unseen neural donors or spatial tissue.
- ARCADE reinforces separating cell-type abundance from within-cell-type state before interpreting neighborhood-associated expression as context response. RFA is a useful negative-result warning: 3D/topological graph priors must beat simple distance/accessibility controls rather than being assumed useful.
- SPEAR and RAPTORGraph provide architecture comparators—spectral gene geometry, learned pathway structure and intervention-locality controls—but observational graphs, inferred couplings and latent spillover do not establish causal rewiring or transport to DLPFC/SCZ.
- The foundation-model audit strengthens minimum controls: expression-matched deletion/negative contrasts, replicate-aware ground truth, donor/clone-disjoint splits, and matched simple baselines. Perturbscape suggests a future perturbation-to-disease-genetics bridge, but reports no schizophrenia-specific validation.
- These are author-reported preprint findings and design safeguards, not reproduced AIVC results. The execution order remains: aging/AD premise-and-access **COMMIT/NO-GO**, GeneBridge evidence freeze, then a bounded SCZ context-value pilot; no architecture expansion is justified yet.

### Previous review context — October 25, 2026

- The [[02_Projects/AIVC/reviews/2026-10-25-NIA-K99-study-section-review|October 25 NIA K99 review]] remained **Overall Impact 8/9 — STAGNANT** relative to October 24. No newly documented benchmark, completed aging/AD premise/access decision, or training/independence commitment was found in the reviewed notes; this does not establish absence of work elsewhere.
- The October 23 literature and incomplete funding output were already incorporated. The full review was saved; duplicate Telegram delivery was suppressed. This was a documentation update, not scientific progress or a change to canonical SCZ scope.

### Previous review context — October 24, 2026

- The [[02_Projects/AIVC/reviews/2026-10-24-NIA-K99-study-section-review|October 24 NIA K99 review]] remains **Overall Impact 8/9 — STAGNANT** relative to October 18. No new benchmark, completed aging/AD premise/access decision, or training/independence commitment was verified in the reviewed notes; this does not rule out work elsewhere.
- New reviewer analysis, not project progress: October 21–23 literature narrows architecture-only novelty. On a future eligible perturbation benchmark, separate perturbation representation, response head, and added spatial context; do not conflate gene-perturbation embeddings with cell-identity embeddings or impose this expanded comparison on the initial GeneBridge pilot.
- The October 23 funding output was recovered and remains incomplete; current policy/eligibility changes are unverified. The premise-and-access COMMIT/NO-GO remains the first action. Canonical SCZ scope is unchanged.

### Research monitoring — October 26–30, 2026

- Recent radar reports strengthen evaluation safeguards rather than add a new AIVC architecture: use independent biological-unit/clone-aware splits for perturbation data, test uncertainty for error-ranking information beyond the predicted mean, and compare data-unification/centered-transfer baselines before graph or transformer claims. These are literature-derived recommendations, not AIVC results.
- UPM and BLOOM further narrow architecture-only novelty; spatial-context value, disease-relevant neural transfer, and independent-unit/orthogonal-readout validation remain the plausible differentiators. No completed AIVC benchmark or scope change was documented.
- The October 30 radar adds potential future inputs—variant-to-function Perturb-seq and SCZ environment-by-developmental context—but neither establishes current data access or a validated AIVC premise. ? UNCERTAIN transfer from mouse or non-neural systems to human DLPFC.

### Previous review context — October 18, 2026

- The [[02_Projects/AIVC/reviews/2026-10-18-NIA-K99-study-section-review|October 18 NIA K99 review]] remains **Overall Impact 8/9 — STAGNANT** relative to October 17. No material new project result, premise/access decision, training commitment or funding verification was found in the reviewed record; work elsewhere is not ruled out. The October 16 radar and its nuisance-aware recommendations were already incorporated yesterday.
- The full review was saved; duplicate Telegram delivery was suppressed. This is a documentation update, not scientific progress or a change to canonical SCZ scope.

### Research monitoring — October 19–23, 2026

- [[02_Projects/AIVC/literature/2026-10-19-literature-radar|October 19]], [[02_Projects/AIVC/literature/2026-10-21-literature-radar|October 21]], and [[02_Projects/AIVC/literature/2026-10-23-literature-radar|October 23]] monitoring added competitive baselines and validation safeguards for spatial context, perturbation representation, transport, experimental rescue validation, and model interpretation.
- These are author-reported literature findings and assistant recommendations. No AIVC run, aging/AD premise decision, collaborator commitment, funding verification, or approved scope change was documented.

### Previous review context — October 17, 2026

- The latest [[02_Projects/AIVC/reviews/2026-10-17-NIA-K99-study-section-review|NIA K99 review]] remains **Overall Impact 8/9 — STAGNANT** relative to October 11. No new AIVC result, completed aging/AD premise/access decision, or committed training/independence package was found in the reviewed notes; this does not establish absence of work elsewhere.
- New review recommendation, not an adopted architecture change: the first measured-target context test should compare against assay-nuisance-aware simple baselines. Donor holdouts alone do not rule out reproducible technical spatial structure. Nuisance variables must respect held-out-target and deployment-information boundaries; residualization can also remove biology and does not establish causal identification.
- October 12–16 literature reports strengthen the multi-scale/context baseline and sender/receiver validation requirements. Their findings remain attributed to the radar reports, not independently reproduced results. The October 16 funding check was incomplete; current eligibility/deadline changes remain unverified.
- The October 12 strategy's premise-and-access **COMMIT/NO-GO** remains undocumented as completed. Canonical SCZ goals are unchanged.

### Previous review context — October 11, 2026

- The October 11 [[02_Projects/AIVC/reviews/2026-10-11-NIA-K99-study-section-review|NIA K99 review]] recorded **Overall Impact 8/9 — STAGNANT** with no material evidence change since October 10. This is a reviewer-style assessment, not a scientific result.
- The October 9 literature, assessed in the October 10 review, sharpens the novelty challenge to editable neighborhood-conditioned predictions and the need for context-specific response/transport validation. Any target-response calibration must be separate from final testing; more diverse predictions alone are not evidence of correct biology. No new project result was verified.
- No executable aging/AD question, frozen premise artifact, AIVC benchmark result, intervention-validation access, or committed training/independence package is documented.
- The October 5 weekly strategy sharpened deliverables but did not add completed evidence. A full-rank design is necessary for algebraic estimability but does not establish causal identification, adequate overlap, or freedom from hidden confounding.
- The next decision remains a bounded aging/AD premise-and-access audit ending in **commit/no-go**. If no eligible system exists, document the minimum collaborator-generated pilot rather than relabeling SCZ data.
- ? UNCERTAIN The canonical goal remains SCZ-centered, while an aging/AD branch is being evaluated for NIA fit. No permanent disease-focus change has been approved.
