---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-10-05
status: active
created: 2026-10-05
last_updated: 2026-10-05
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-09-28-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-10-04-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-10-02-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The September 28 deliverables remain undocumented as completed. AIVC still has no frozen NIA premise, protected benchmark, or confirmed result; the October 4 mock review remains **Overall Impact 8 / STAGNANT**. GeneBridge remains the nearest publishable asset, but its current canonical result note contains historical values that still require verification from current files. The October 2 literature radar raises the evidentiary bar: evaluate context-specific information separately from identity/shared effects, establish metric sensitivity with controls, and prove that a model uses biological context rather than merely containing it.

This is therefore another evidence-and-decision week, but with no expansion of scope. Carrying forward the same bottlenecks is intentional: unfinished high-value gates should be closed rather than replaced by new plans. The unresolved SCZ-versus-NIA aging/AD focus must be made explicit; this strategy does not silently convert the SCZ-centered AIVC program into an aging/AD project.

## #1 MUST DO — Close the NIA aging/AD premise and access gate

**SCIENTIFIC QUESTION**  
Is there one accessible aging/AD-relevant neural or glial system in which a defined context or exposure modifies a measured perturbation response across independent biological units, with sufficient overlap to estimate a context-by-perturbation effect and a feasible experimental validation route?

**WHY NOW**  
This is the repeated fatal K99 weakness and remains the number-one action in the October 4 reviewer critique. Without a selected population, exposure, perturbation class, endpoint, donor-resolved design, and assay access, neither an architecture nor the SCZ GeneBridge asset can support an NIA premise. The decision has already slipped across multiple weeks; it must now end in commit/no-go rather than another candidate list.

**HYPOTHESIS**  
At least one candidate system has a prespecified cell population, aging/AD-relevant context, limited perturbation class, matched controls, measured response endpoint, independent biological replication, donor-held-out evaluation, and prospective validation access such that context is not synonymous with cohort, platform, dose, or time.

**EXPERIMENT**  
Time-box the feasibility audit to two working days. For each serious candidate, verify accession or collaborator access; donor/replicate identity; age, pathology, or experimentally induced context; cell population; perturbation and control; dose and time; batch/platform; measured response space; and raw/count-level availability. Build a context × perturbation × donor support table and proposed design matrix before downloading full matrices. Test rank, positivity/overlap, and whether donor-held-out folds are possible. Select exactly one population, one context/exposure, one perturbation class, one primary response endpoint, one prediction estimand, and one prospective intervention contrast. Name one primary dataset plus either an independent validation dataset or a committed collaborator assay. If no system passes, record a formal no-go and the minimum collaborator-generated pilot needed.

**DATA REQUIRED**  
Verified sample-level metadata and accessions; donor or biological-replicate IDs; age/pathology/exposure labels; perturbation/control, dose, and time; cell population; batch and platform; measured response genes/modules and functional endpoint; raw/count-level availability; cross-dataset endpoint compatibility; and written evidence of prospective assay access when public validation data are insufficient. GeneBridge cannot be counted as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata and identification audit first: contingency/support tables, design-matrix rank, positivity checks, donor-grouped split generation, fold-local preprocessing rules, and replicate-level precision planning. Keep prediction and intervention targets distinct:

```text
Prediction: m(c,e,p,x) = E[Y | C=c, E=e, P=p, X=x]
Intervention: E[Y(e,p) - Y(e,p0)]
Factorial functional endpoint: F ~ context * perturbation + batch + (1 | donor)
```

The actual assay must determine nesting, response family, and any dose/time terms. Do not rely on cell counts as biological replication.

**BASELINE**  
The null feasibility position is that no eligible design exists because context is confounded with cohort/platform or donor–context–perturbation support is inadequate. If the gate passes, preregister control mean, perturbation mean, nearest-neighbor transfer, and additive ridge without context as initial computational baselines.

**METRIC**  
Primary gate metric: a full-rank design in which the prespecified context-by-perturbation coefficient is identifiable with independent biological replication and a donor-held-out test. Secondary: biological-unit counts per stratum, matched-control completeness, overlap fraction, endpoint compatibility, projected interval width, and availability of independent validation. The downstream benchmark plan must include negative controls and a positive/sensitivity control capable of showing that the chosen metric can detect meaningful response information.

**SUCCESS CRITERION**  
By the end of day two, freeze `aging_AD_AIVC_premise_v1.md` with one biological question, population, context, perturbation class, measured endpoint, exact estimands, verified data/access table, donor-resolved support table, design-rank report, split plan, simple baselines, metric-sensitivity controls, precision-based decision rule, and prospective validation route. A documented no-go also successfully closes the decision gate, but it blocks an NIA-ready computational premise until the specified pilot or collaboration exists.

**FAILURE INTERPRETATION**  
Failure to find a replicated, full-rank design means available data cannot support the proposed NIA claim. It does not justify pooling incompatible cohorts, treating cross-sectional AD tissue as a perturbation response, or relabeling SCZ data. The correct next action would be to secure a collaborator-generated pilot or reconsider whether NIA is the right mechanism.

**EXPECTED OUTPUT**  
`aging_AD_AIVC_premise_v1.md`; verified dataset/access table; context × perturbation × donor support table; design-rank and overlap report; donor split plan; data dictionary; validation-access statement; and explicit commit/no-go decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Lock GeneBridge disease-effect preservation evidence

**SCIENTIFIC QUESTION**  
When measured Xenium genes are masked and imputed, does the final GeneBridge method preserve donor-level SCZ effect sizes and directions across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the strongest near-term publication and preliminary-data asset. Its canonical results still report historical counts and rankings that require verification, while the final method panel, versions, donor/fold accounting, and disease-effect concordance package remain unfinished. Reconstruction accuracy is not enough to justify biological discovery from imputed genes.

**HYPOTHESIS**  
The verified final GeneBridge method will preserve measured held-out-gene SCZ diagnosis effects better than layer-mean and nonspatial baselines, with stable concordance across folds and no excess disease discoveries under covariate-aware donor-level null resampling.

**EXPERIMENT**  
Freeze paths/checksums for measured and imputed outputs, software/model versions, all three gene-fold manifests, the 24-donor reference cohort, the 23-donor analysis cohort, Br6432 exclusion, and any additional exclusions. Aggregate measured and imputed values to identical donor × layer units for every eligible measured-but-held-out gene. Before examining method comparisons, audit design rank and freeze the primary formula and normalized scale. Apply the same model to measured outcomes and every verified method. Compare diagnosis coefficients and uncertainty, then evaluate null behavior using covariate-aware donor-level resampling; never permute cells or layers as independent units.

**DATA REQUIRED**  
Measured expression for the 300 Xenium genes; three fold manifests; current prediction files for every verified final-panel method; donor, diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; software/model versions; current job logs and output files; and a separately harmonized reference-paper gene universe.

**MODEL / METHOD**  
For gene `g`, donor `d`, and layer `l`, use the same declared transformation and 161 donor × layer units for measured and imputed outcomes:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Use the estimable repeated-donor implementation appropriate to the final software. Add no run/slide term unless a blinded rank/confounding audit, completed before effect comparison, shows that one prespecified term is estimable and required. Bootstrap donors for coefficient-concordance uncertainty and use one multiplicity universe shared across methods.

**BASELINE**  
Measured held-out genes as truth; layer-specific gene mean; a verified nonspatial imputation baseline; SpaGE; and every method actually present in the current final panel. Do not assume the remembered method list or the historical ENVI ranking.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients across all eligible held-out genes. Secondary: sign concordance; calibration slope/intercept; coefficient RMSE; donor-bootstrap confidence intervals; fold stability; discovery precision/recall at frozen thresholds; and donor-level null false-positive/discovery behavior.

**SUCCESS CRITERION**  
Produce a file-traceable all-fold package with complete donor accounting and one frozen formula. A method can support expanded-gene biological interpretation only if the donor-bootstrap interval supports positive effect concordance, sign concordance is at least 80% among genes with measured nominal `p < 0.05`, calibration is not materially biased, and donor-level null resampling shows no excess discoveries. Report all methods and folds regardless of whether any method passes.

**FAILURE INTERPRETATION**  
Strong expression reconstruction with weak, unstable, or biased disease-effect concordance means imputed genes should not support SCZ discovery claims. The publishable result then becomes a rigorous benchmark with a clear downstream-use boundary. A changed winner after reconstruction indicates pipeline/version instability that must be resolved before manuscript figures are trusted.

**EXPECTED OUTPUT**  
Canonical method/version/checksum table; verified donor/exclusion/fold manifest; exact formula and transformation; measured-versus-imputed coefficient-concordance figure and table; donor-bootstrap intervals; null-calibration figure; manuscript-ready result paragraph; and evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Run the first measured-target AIVC context-value audit on GeneBridge

**SCIENTIFIC QUESTION**  
Does local multicellular environment add reproducible information for predicting measured held-out Xenium activity genes in unseen donors beyond identity and simple pooled-context summaries, and does the fitted model actually use that context?

**WHY NOW**  
AIVC still has no executed benchmark. GeneBridge provides an available donor-structured test of the identity-plus-environment premise. The October 2 literature radar shows why final-state accuracy alone is inadequate: identity must be separated from context-specific information, metric sensitivity must be checked, and biological-input utilization must be tested. This pilot can justify or stop more complex context modeling without claiming perturbation, causality, aging, or AD evidence.

**HYPOTHESIS**  
Cell-type-stratified local expression summaries will improve measured held-out-gene prediction on unseen donors relative to identity-only ridge, and the gain will disappear when context is replaced or shuffled within support-matched cell-type/layer/technical strata.

**EXPERIMENT**  
Reuse Priority #2's verified donors and gene folds. Split donors before fitting normalization, feature selection, modules, or hyperparameters. Use only measured Xenium inputs and targets; exclude the focal cell from its neighborhood. Predefine radii, cell-type strata, minimum-neighbor rules, deployment-available covariates, and one coarse pathway/module endpoint alongside gene-level targets. Under identical protected folds and tuning budgets, fit M0 identity-only ridge, M1 identity plus cell-type-stratified pooled-context ridge, and M2 a capacity-limited residual MLP using the same inputs. For the frozen best context model, perform support-matched context replacement and within-stratum shuffling. Do not introduce attention, a graph, a conditional VAE, imputed targets, diagnosis labels, or test-donor preprocessing.

**DATA REQUIRED**  
Measured Xenium expression; cell coordinates; cell-type and layer labels; donor/run/slide metadata; the three observed/held-out-gene manifests; QC/exclusion rules; locked 23-donor cohort; and prespecified gene-to-program definitions derived without final-test outcomes.

**MODEL / METHOD**  
Use regularized multi-output regression for M0/M1 and one small residual MLP for M2. Neighborhood features are training-defined, cell-type-stratified means at prespecified radii with focal-cell exclusion. Use grouped nested cross-validation by donor. The primary paired contrast is:

```text
DeltaL_d = L_d(M0) - L_d(M1)
```

Estimate uncertainty by donor bootstrap. Refitted M0 versus M1 tests available context information; frozen-checkpoint support-matched replacement tests fitted reliance. Report gene-level and prespecified pathway/module resolution separately.

**BASELINE**  
Training-fold global gene mean; cell-type/layer mean; identity-only ridge; and identity plus unstratified pooled-neighborhood ridge. M1 must beat the strongest simple baseline before M2 or future attention/graph models are justified.

**METRIC**  
Primary: donor-averaged measured-target loss on held-out genes, summarized as the paired M1-versus-M0 donor contrast. Secondary: per-gene Spearman correlation and RMSE; pathway/module recovery; performance by layer/cell type/fold; calibration; support-matched replacement loss; shuffled-context control; and sensitivity to radius and neighbor count. Include a benchmark-sensitivity positive control and verify that it separates from the null before interpreting a model tie as biological failure.

**SUCCESS CRITERION**  
Context advances only if M1 beats M0 in at least four of five prespecified donor-held-out outer folds, the donor-bootstrap 95% interval for paired improvement excludes zero, the benchmark sensitivity control behaves as expected, the gain is not reproduced by shuffled/replaced context, and no single donor or layer explains it. M2 is retained only if it improves over M1 under the same protected folds. Otherwise, identity-only or pooled context becomes the justified endpoint and hierarchical attention is stopped.

**FAILURE INTERPRETATION**  
No M1 gain with a functioning sensitivity control means this target and scale do not support the claimed environmental contribution. No model separation with a failed sensitivity control is inconclusive. Gain under shuffled or replaced context suggests leakage, technical spatial autocorrelation, or proxy use. A gain confined to one donor/layer indicates limited transport. None of these outcomes supports perturbation or causal claims.

**EXPECTED OUTPUT**  
Versioned data contract and configuration; donor/fold manifests and leakage checks; M0/M1/M2 predictions; metric-sensitivity control result; donor-level paired-loss figure; replacement/shuffle utilization audit; subgroup stability table; first registered result in [[02_Projects/AIVC/experiments-and-results]]; and a clear advance/stop decision for hierarchical context modeling.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 7/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop architecture expansion and broad virtual-cell literature collection this week.** Do not spend time on GNN-versus-transformer design, graph priors, multimodal conditional VAEs, cross-species modules, portals, or additional architecture diagrams until Priority #3 demonstrates leakage-resistant context value beyond pooled summaries and Priority #1 establishes an eligible NIA premise. These activities currently add complexity without closing a scientific or grant-critical evidence gap.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-10-02-literature-radar]]
- [[02_Projects/AIVC/reviews/2026-10-04-NIA-K99-study-section-review]]
- [[09_Planning/weekly-strategies/2026-09-28-AIVC-GeneBridge-weekly-strategy]]
- [[09_Planning/active-tasks]]
- [[09_Planning/unanswered-questions]]
