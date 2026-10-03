---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-09-21
status: active
created: 2026-09-21
last_updated: 2026-09-21
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-09-13-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-09-20-NIA-K99-study-section-review]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

Last week's three deliverables remain undocumented: the aging/AD premise and eligible dataset pair, the GeneBridge measured-versus-imputed disease-effect test, and the first AIVC baseline. The September 20 NIH review therefore remains **Overall Impact 8 / STAGNANT**. The September 18 literature radar raises the benchmark-overfitting bar—especially through CellRFT—but does not change the immediate scientific bottleneck.

This week is a forced evidence week. Priority #1 is a kill-or-commit test of whether the NIA premise is testable with existing data. Priority #2 protects the nearest publication. Priority #3 begins only if Priority #1 produces an eligible design. The unresolved contradiction remains explicit: canonical AIVC goals are SCZ-centered, whereas an NIA K99 requires direct aging/AD evidence. This strategy does not silently redefine the canonical program.

## #1 MUST DO — Kill-or-commit audit for the aging/AD perturbation premise

**SCIENTIFIC QUESTION**  
Does an identifiable public-data design exist in which age- or AD-associated basal context can be tested as a modifier of perturbation response in a defined human neural or glial population, rather than being perfectly confounded with donor, cohort, platform, or dataset?

**WHY NOW**  
This is the unchanged fatal K99 gap. Repeated architecture discussion and literature accumulation have produced no premise artifact, dataset pair, fold manifest, or preliminary result. Until the same perturbations and matched controls can be compared across multiple donors and contexts, an “aging-aware AIVC” is not an executable scientific program.

**HYPOTHESIS**  
At least one primary and one independent perturbation dataset have sufficient donor-level metadata, repeated perturbations across aging/AD contexts, compatible neural/glial populations, and response-space overlap to estimate context-by-perturbation effects without making context equivalent to dataset.

**EXPERIMENT**  
Perform a metadata-first eligibility audit before downloading or modeling full expression matrices. For each plausible dataset, record donor, age, diagnosis/pathology or aging condition, cell type, perturbation identity, matched control, dose, time, batch, platform, gene space, replicate structure, and access status. Build a perturbation × context × donor overlap table and test whether the proposed primary contrast is estimable. Select exactly one biological system, one cell population, one perturbation class, one primary dataset, and one external dataset. Freeze the population-response estimand, inferential unit, covariates, missingness rules, internal grouped folds, external transport rule, and protected endpoint. Generate machine-readable fold manifests and automated zero-overlap checks. If no pair passes, record a formal negative feasibility result and define the minimum collaborator-generated experiment required; do not substitute cross-sectional AD tissue or unmatched spatial data.

**DATA REQUIRED**  
Public sample/cell metadata and accessions; donor and context labels; perturbation/control, dose, and time annotations; cell-type labels; batch/platform; raw or count-level expression availability; gene/module overlap; and independent-dataset compatibility. GeneBridge is not eligible because it has no perturbation response.

**MODEL / METHOD**  
Design and identifiability audit, not a complex predictor. Use contingency/overlap tables, design-matrix rank checks, donor- and perturbation-grouped split generation, fold-local preprocessing rules, and a donor-level precision or power calculation for the context-by-perturbation contrast. Define population distributions as the primary response unit because destructive single-cell assays do not supply paired-cell counterfactuals.

**BASELINE**  
The null feasibility claim: context is inseparable from dataset/cohort or there is inadequate repeated donor–perturbation overlap. For the eventual benchmark, freeze four simple comparators now: no-change/control mean, perturbation-wise mean, nearest-neighbor response transfer, and additive/ridge without aging/AD context.

**METRIC**  
Primary audit metric: number and fraction of candidate perturbations that remain estimable after requiring repeated donor support in both contexts and zero train/test donor overlap. Secondary: donor count per context, perturbation overlap, matched-control coverage, design-matrix rank, gene/module overlap, and projected uncertainty for the context effect.

**SUCCESS CRITERION**  
By the end of Priority #1, `aging_AD_AIVC_premise_v1.md` is frozen from verified metadata and names one estimable biological contrast, primary/external dataset pair, inferential unit, folds, protected metric, four baselines, negative controls, and variance-informed go/no-go rule. Every test donor is absent from training, and context is not perfectly confounded with dataset. A documented no-eligible-pair result also counts as a successful decision outcome, but it blocks computational aging/AD claims and triggers collaborator-generated data planning.

**FAILURE INTERPRETATION**  
No eligible pair means the current NIA premise cannot be established from available public data. That is not a cue to relax eligibility, pool incompatible studies, or relabel SCZ data; it means the project needs a prospective perturbation system before an NIA application can be credible.

**EXPECTED OUTPUT**  
`aging_AD_AIVC_premise_v1.md`; dataset eligibility matrix; perturbation × context × donor overlap table; data dictionary; fold manifests; leakage report; power/precision note; and either a committed dataset pair or a formal no-go record with minimum data-generation requirements.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 7/10

## #2 SHOULD DO — Test whether GeneBridge preserves disease effects, not just expression

**SCIENTIFIC QUESTION**  
When Xenium genes are measured but masked, does the selected imputation method preserve donor-level SCZ effect sizes and directions across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the strongest near-term publication asset and the clearest evidence that the candidate can execute donor-structured spatial genomics. Yet its final method panel, complete donor/fold accounting, exact DE model, and historical ENVI/DE summaries remain unverified. A manuscript cannot rest on reconstruction metrics if imputation distorts the biological contrast used downstream.

**HYPOTHESIS**  
The canonically selected method will reproduce measured held-out-gene SCZ log-fold changes better than naive and nonspatial baselines while maintaining calibrated null behavior under donor-level diagnosis permutation.

**EXPERIMENT**  
Lock the current result files, software/model versions, three gene folds, 24-donor reference list, 23-donor analysis cohort, Br6432 exclusion, and all other exclusions. For every measured-but-held-out Xenium gene, aggregate measured counts and each method's imputed values to identical donor × layer units. Fit one identical, estimable layer-adjusted diagnosis model to measured and imputed outcomes. Use a donor block/random intercept for repeated layers; include either run or slide only if needed and estimable, never both by default. Compare effect estimates across all folds, then permute diagnosis at the donor level while preserving each donor's layers. Keep donor-level inference separate from layer/domain and cell-type claims.

**DATA REQUIRED**  
Measured values for all 300 Xenium genes; three held-out-gene fold manifests; predictions from the verified final method panel; donor, diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; and current—not remembered—DE and benchmark outputs.

**MODEL / METHOD**  
Donor × layer pseudobulk with an exact prespecified formula such as `expression ~ Dx + Age + Sex + layer + run_or_slide`, with donor handled as the repeated-measure block/random intercept. The final formula is chosen only after rank/confounding checks and is then applied unchanged to measured and imputed data. Bootstrap donors for uncertainty and control multiplicity over the same held-out-gene universe for every method.

**BASELINE**  
Measured held-out genes as ground truth; layer-specific gene mean; a nonspatial imputation baseline; SpaGE; and every method confirmed in the canonical final panel. Do not assume the remembered six-method list or ENVI's lead until current outputs reproduce it.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ log-fold changes across held-out genes. Secondary: sign concordance, regression slope/intercept, log-fold-change RMSE, rank stability, discovery precision/recall at frozen thresholds, donor-bootstrap intervals, and donor-label-permutation false-positive rate.

**SUCCESS CRITERION**  
A file-traceable results package covers all three folds and all eligible held-out genes, with complete donor accounting and one exact DE specification. Working biological-validity criteria remain Spearman rho ≥ 0.70, ≥80% sign concordance among genes with measured nominal `p < 0.05`, and no excess discoveries relative to the prespecified donor-permutation null; report confidence intervals and full results even if thresholds fail.

**FAILURE INTERPRETATION**  
Good reconstruction with weak effect concordance means imputed values should not support expanded-gene SCZ discovery; the paper should emphasize benchmarking and define the downstream-use boundary. A changed winner after canonical rerunning indicates pipeline/version instability, not a biological result.

**EXPECTED OUTPUT**  
Canonical method/version table; verified donor/exclusion and fold manifests; exact DE formula; measured-versus-imputed effect-concordance figure and table; permutation/null-QC figure; and an evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 7/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Run the first leakage-resistant AIVC context-value baseline

**SCIENTIFIC QUESTION**  
If Priority #1 identifies an eligible system, does age/AD context add reproducible predictive information for population perturbation response beyond perturbation identity, basal control state, and naive transfer?

**WHY NOW**  
AIVC has no experimental result. One sealed baseline/context-ablation run would provide more scientific information than another architecture proposal and would directly test the K99 premise. It starts only after Priority #1 freezes the design; otherwise it is deferred rather than improvised.

**HYPOTHESIS**  
A regularized additive model conditioned on age/AD basal context will reduce held-out population-response error relative to its capacity-matched context-agnostic version, and the gain will disappear when context labels are shuffled.

**EXPERIMENT**  
On the frozen primary dataset, run no-change/control-mean, perturbation-mean, nearest-neighbor transfer, and additive/ridge models. Compare matched additive models with and without context using identical folds, features, tuning budgets, and preprocessing. Keep all preprocessing inside training folds. Evaluate held-out donors and perturbations; perform donor bootstrap and context-label shuffling. Apply the frozen winner once to the external dataset without retuning. Do not introduce a GNN, Transformer, flow model, graph prior, or reward fine-tuning in this run.

**DATA REQUIRED**  
The eligible primary and external datasets, data dictionary, fold manifests, basal controls, perturbation labels, context/covariates, response genes/modules, and frozen configuration from Priority #1.

**MODEL / METHOD**  
Multi-output ridge or reduced-rank regression for mean response, with empirical residual resampling for a simple population prediction. Tune only within training donors. Estimate uncertainty by donor bootstrap. Protect external data and final metrics from model and reward selection.

**BASELINE**  
No-change/control mean; perturbation-wise mean; nearest-neighbor response transfer; and the matched additive model without age/AD context.

**METRIC**  
Primary: energy distance between predicted and observed perturbed populations. Secondary: perturbation-induced mean-change correlation, response-module error, DE recovery, perturbation discrimination, and interval coverage. Report each category separately; do not hide a discrimination loss inside an aggregate score.

**SUCCESS CRITERION**  
The additive model first beats the strongest naive baseline. Context then provides at least the variance-informed improvement frozen in Priority #1—provisionally a ≥10% reduction in energy distance across a majority of held-out folds—with donor-level uncertainty supporting benefit, no comparable gain under shuffled context, and the same direction of effect in the untouched external dataset.

**FAILURE INTERPRETATION**  
No gain over naive transfer means the estimand or dataset lacks useful predictable signal. A gain reproduced by shuffled labels indicates leakage/confounding. Internal gain without external transport suggests cohort/platform dependence or genuine context specificity that must be disentangled. Any of these outcomes blocks complex architecture work but remains a useful boundary-condition result.

**EXPECTED OUTPUT**  
Versioned baseline code/configuration; fold-level predictions and metrics; context-ablation and shuffle-control plots; donor-bootstrap intervals; external no-retuning result; failure log; and the first entry in the [[02_Projects/AIVC/experiments-and-results|AIVC experiment registry]].

**COMPLEXITY:** HIGH  
**K99 VALUE:** 9/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop broad architecture design and opportunistic paper accumulation this week.** GNN-versus-Transformer comparisons, graph construction, foundation-model embeddings, and CellRFT-style reward optimization have low scientific value until an eligible aging/AD design, simple baseline, and protected evaluation exist. Resume them only if Priority #3 reveals a leakage-resistant prediction gap that complexity could plausibly solve.

## Evidence used

- [[02_Projects/AIVC/current-state|AIVC current state]]
- [[02_Projects/AIVC/important-decisions|AIVC decisions]]
- [[02_Projects/AIVC/experiments-and-results|AIVC experiments/results]]
- [[02_Projects/AIVC/todo-and-next-actions|AIVC next actions]]
- [[02_Projects/GeneBridge/current-state|GeneBridge current state]]
- [[02_Projects/GeneBridge/methods|GeneBridge methods]]
- [[02_Projects/GeneBridge/datasets|GeneBridge datasets]]
- [[02_Projects/GeneBridge/experiments-and-results|GeneBridge experiments/results]]
- [[02_Projects/GeneBridge/todo-and-next-actions|GeneBridge next actions]]
- [[05_Learning/important-papers|AIVC literature radar through 2026-09-18]]
- [[02_Projects/AIVC/reviews/2026-09-20-NIA-K99-study-section-review|Latest NIH reviewer critique]]
- [[09_Planning/weekly-strategies/2026-09-13-AIVC-GeneBridge-weekly-strategy|Previous weekly strategy]]
- [[09_Planning/active-tasks|Active tasks]]
- [[09_Planning/unanswered-questions|Unanswered questions]]
