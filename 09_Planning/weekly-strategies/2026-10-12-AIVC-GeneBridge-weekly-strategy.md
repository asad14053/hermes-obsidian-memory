---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-10-12
status: active
created: 2026-10-12
last_updated: 2026-10-12
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-10-05-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-10-11-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-10-09-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The evidence state has not materially advanced: the October 11 mock NIA review remains **Overall Impact 8/9 — STAGNANT**, no AIVC benchmark is registered, and the current GeneBridge note still contains historical results that have not been verified from current files. The October 9 literature further narrows the defensible AIVC contribution: demonstrate context-dependent prediction and its transport boundary against simple baselines; do not treat identity similarity, input editing, response diversity, or architectural complexity as proof of mechanism.

This week must close one strategic decision and produce one manuscript-grade result package. The three priorities below are deliberately sequential. The aging/AD audit ends after two working days with either commit or no-go. The GeneBridge evidence package then receives the main execution time. The AIVC pilot begins only after its donor and gene-fold manifests are locked. This strategy does not silently replace the canonical SCZ-centered AIVC program with aging/AD.

## #1 MUST DO — Force a commit/no-go decision on the NIA aging/AD premise

**SCIENTIFIC QUESTION**  
Is there one accessible aging/AD-relevant neural or glial system in which a defined context modifies a measured response to a limited perturbation class across independent biological units, with enough support to estimate and validate the context-by-perturbation effect?

**WHY NOW**  
This is the repeated fatal weakness in the latest K99 critique and has remained open across several weekly plans. Until the population, context, perturbation, endpoint, donor support, and validation route are fixed, additional AIVC design work cannot become NIA preliminary evidence. The correct outcome this week may be a documented no-go rather than another candidate list.

**HYPOTHESIS**  
At least one public or collaborator-accessible system has donor- or replicate-resolved controls and perturbations in both prespecified contexts, a measured molecular response endpoint, adequate overlap, and a feasible independent or prospective validation route without context being perfectly confounded with cohort, platform, dose, or time.

**EXPERIMENT**  
Time-box the audit to two working days and at most three serious candidate systems. For each, verify accession or collaborator access; biological-unit IDs; age, pathology, or experimentally induced context; neural/glial population; perturbation and control; dose and time; batch/platform; measured endpoints; and raw/count-level availability. Construct the context × perturbation × biological-unit support table and design matrix before downloading full expression matrices. Assess rank, overlap, confounding, donor-held-out splitting, and endpoint compatibility. Select exactly one population, one context, one perturbation class, one primary response endpoint, and one validation route—or record no-go and the minimum collaborator-generated pilot needed.

**DATA REQUIRED**  
Sample-level metadata and data-access evidence; donor or biological-replicate IDs; context, perturbation, control, dose, time, population, batch, and platform fields; measured response genes/programs and any functional endpoint; raw/count availability; and written evidence of an independent dataset or prospective assay route. GeneBridge cannot be counted as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata audit, contingency/support tables, design-matrix rank diagnostics, overlap/positivity assessment, confounding map, donor-grouped fold plan, and replicate-level precision calculation. Keep the targets distinct:

```text
Conditional prediction: m(c,e,p,x) = E[Y | C=c, E=e, P=p, X=x]
Response contrast: Δd,e,p = mean(Yd,e,p) − mean(Yd,e,p0)
Context interaction: E[Δd,e1,p − Δd,e0,p]
```

Full rank is necessary but not sufficient; the audit must also establish practical overlap, biological replication, deployment-available inputs, and a non-leaking calibration/test boundary.

**BASELINE**  
The null position is no eligible NIA design. If one passes, preregister control mean, perturbation mean, nearest-context transfer, and additive ridge without context as the first computational baselines.

**METRIC**  
Primary gate: an estimable context-by-perturbation contrast with independent biological replication and a protected donor/replicate-held-out test. Secondary diagnostics: biological units per stratum, matched-control completeness, overlap, context–cohort/platform confounding, projected interval width, endpoint compatibility, and validation access.

**SUCCESS CRITERION**  
By the end of working day two, save one premise artifact containing the exact question and estimand, verified accession/access table, support table, rank/confounding/overlap audit, protected split plan, simple baselines, primary endpoint, precision-based go/no-go rule, and named validation route. A formal no-go counts as successful closure, but it means the current NIA branch is not ready until the specified pilot or collaboration exists.

**FAILURE INTERPRETATION**  
No eligible system means the available evidence cannot support the proposed NIA context-dependent perturbation claim. It does not license pooling incompatible cohorts, calling cross-sectional AD tissue a perturbation experiment, or relabeling SCZ data. Repeated failure to complete the bounded audit is an execution problem and should trigger explicit deprioritization of the NIA branch.

**EXPECTED OUTPUT**  
`02_Projects/AIVC/aging_AD_AIVC_premise_v1.md` with a verified data/access table, context × perturbation × biological-unit support table, design-rank/confounding/overlap report, split and calibration/test plan, validation-access statement, and explicit **COMMIT** or **NO-GO** decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Produce the GeneBridge disease-effect preservation result

**SCIENTIFIC QUESTION**  
When measured Xenium genes are masked and imputed, does the final GeneBridge method preserve donor-level SCZ diagnosis-effect directions and magnitudes across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the nearest publishable asset and the strongest available evidence of research execution for a K99 and faculty program. The current vault still records only historical DE values and unverified method rankings. Expression reconstruction alone cannot justify biological interpretation of imputed genes; a disease-effect preservation and null-calibration result can.

**HYPOTHESIS**  
On identical donor × layer units and a common eligible held-out-gene universe, the verified final GeneBridge method will show stronger measured-versus-imputed SCZ coefficient concordance than layer-mean and verified nonspatial baselines, while donor-level null resampling remains calibrated.

**EXPERIMENT**  
Freeze the current prediction paths, checksums, software/model versions, three gene-fold manifests, 24-donor reference inventory, 23-donor analysis cohort, Br6432 exclusion, and all additional exclusions. Aggregate measured and imputed expression to the same donor × layer units. Before comparing methods, audit design rank and freeze the normalized scale, eligible gene universe, repeated-donor implementation, and diagnosis formula. Fit the identical model to measured outcomes and every verified final-panel method. Compare diagnosis coefficients across all folds; quantify uncertainty by resampling donors and null behavior by covariate-aware donor-level diagnosis resampling. If significance-based subsets are reported, repeat selection inside resampling.

**DATA REQUIRED**  
Measured 300-gene Xenium matrix; current predictions for every verified final-panel method; three gene-fold manifests; donor, diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; software versions and current job logs; and a separately harmonized reference-paper gene universe.

**MODEL / METHOD**  
Use one declared transformation and the same donor × layer observations for truth and predictions:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Use the repeated-donor implementation supported by the final software. Add a technical term only if a blinded rank/confounding audit shows it is estimable and prespecified. Estimate coefficient-concordance uncertainty with donor bootstrap and false-positive behavior with donor-level, covariate-aware null resampling—not cell or layer permutations.

**BASELINE**  
Measured held-out genes as truth; training-derived layer-specific gene mean; one verified nonspatial imputation baseline; SpaGE if present in the current panel; and every method actually represented by current outputs. Do not assume the historical six-method list or ENVI ranking.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients over the complete eligible held-out-gene universe. Secondary: sign concordance, coefficient RMSE, calibration slope/intercept, donor-bootstrap intervals, fold stability, discovery precision/recall at frozen thresholds, and null false-positive/discovery behavior.

**SUCCESS CRITERION**  
Deliver the all-fold package regardless of outcome. Biological interpretation of imputed genes advances only if the final method beats the strongest simple/nonspatial baseline on the primary metric, the donor-bootstrap 95% interval for measured–imputed coefficient correlation is above zero, complete-universe sign concordance exceeds the prespecified donor-null reference, calibration shows no material systematic bias, and null resampling shows no excess discoveries. No method or fold may be omitted because it performs poorly.

**FAILURE INTERPRETATION**  
Good reconstruction but weak, unstable, or biased disease-effect concordance means imputed genes should not support SCZ discovery claims. That remains a publishable benchmark if the limitation is quantified. A changed winner or inconsistent donor/fold inventory indicates pipeline-version instability and blocks manuscript figures until resolved.

**EXPECTED OUTPUT**  
Canonical method/version/checksum table; verified donor/exclusion/fold manifest; frozen formula and transformation; measured-versus-imputed coefficient-concordance figure and table; donor-bootstrap and null-calibration report; manuscript-ready result paragraph; and evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Run the first measured-target AIVC context-value baseline

**SCIENTIFIC QUESTION**  
Does local multicellular context improve prediction of measured held-out Xenium activity genes in unseen donors beyond identity and simple pooled-neighborhood summaries, and is any gain stronger than support-matched shuffled-context nulls?

**WHY NOW**  
AIVC has no registered benchmark. GeneBridge offers a bounded engineering test of the identity-plus-environment premise using measured targets and donor structure. The October 9 literature makes the standard clear: context-conditioned output or response diversity is not enough; context must improve protected prediction relative to simple baselines, and transport limits must be visible. This remains SCZ conditional-prediction evidence, not aging/AD, perturbation, or causal evidence.

**HYPOTHESIS**  
Cell-type-stratified local measured-expression summaries contain donor-transportable information beyond identity-only and unstratified pooled-context baselines, producing a positive donor-level loss reduction that exceeds a support-matched context-shuffle null.

**EXPERIMENT**  
Reuse Priority #2's locked donors and gene folds. Split donors before normalization, feature construction, feature selection, or tuning. Use only measured Xenium inputs and targets; exclude the focal cell from every neighborhood. Freeze radii, cell-type strata, minimum-neighbor rules, permitted covariates, and one pathway/module endpoint. Under identical nested donor-grouped folds and tuning budgets, fit identity-only ridge, identity plus unstratified pooled context, identity plus cell-type-stratified context ridge, and only then one capacity-limited residual MLP. For the frozen best context model, run support-matched context replacement and within-stratum shuffle nulls. Do not add attention, a graph, a conditional VAE, diagnosis labels, imputed targets, or test-donor preprocessing.

**DATA REQUIRED**  
Measured Xenium expression; cell coordinates; cell-type and layer labels; donor/run/slide metadata; locked donor exclusions; three observed/held-out-gene manifests; QC rules; and pathway/module definitions fixed without final-test outcomes.

**MODEL / METHOD**  
Regularized multi-output regression for all primary comparisons and one small residual MLP only after the stratified linear context model beats simpler baselines. Use training-defined neighborhood summaries and nested donor-grouped cross-validation. Primary paired contrast:

```text
ΔL_d = L_d(identity-only) − L_d(stratified-context)
```

Use donor bootstrap for uncertainty. Compare the observed gain with the empirical distribution from support-matched shuffles; treat frozen-model replacement as a reliance diagnostic, not proof of causality.

**BASELINE**  
Training-fold global gene mean; cell-type/layer mean; identity-only ridge; and identity plus unstratified pooled-neighborhood ridge. The stratified context model must beat the strongest simple baseline before any nonlinear model is scientifically justified.

**METRIC**  
Primary: donor-averaged held-out measured-target loss and its paired donor-level reduction. Secondary: per-gene Spearman correlation and RMSE, pathway/module recovery, calibration, fold/donor/layer stability, empirical shuffle-null percentile, replacement sensitivity, radius sensitivity, and neighbor-count sensitivity.

**SUCCESS CRITERION**  
Advance context modeling only if the stratified context model beats the strongest simple baseline in at least four of five prespecified outer folds, the donor-bootstrap 95% interval for paired improvement excludes zero, the observed gain exceeds the 95th percentile of the support-matched shuffle null, and no single donor or layer explains the result. Retain the MLP only if it adds protected-test improvement over the linear context model. Otherwise stop hierarchical context architecture work for this endpoint and scale.

**FAILURE INTERPRETATION**  
A null result with a functioning sensitivity control argues that the chosen targets and neighborhood scale do not support the environmental-information claim. Failure of the sensitivity control is inconclusive. Gains reproduced by matched shuffles suggest leakage, technical spatial autocorrelation, or proxy use; gains restricted to one donor/layer indicate poor transport. None of these outcomes establishes perturbation-response biology.

**EXPECTED OUTPUT**  
Versioned data contract/configuration; donor and gene-fold manifests; leakage audit; baseline predictions; donor-level paired-loss figure; empirical shuffle/replacement audit; subgroup stability table; first registered result in [[02_Projects/AIVC/experiments-and-results]]; and an explicit advance/stop decision for richer context models.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 7/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop architecture expansion this week.** Do not spend research time adding GNN, transformer, hypergraph, conditional-VAE, multimodal, or “universal” components before the measured-target context baseline passes. Architecture work currently increases implementation debt without resolving the NIA premise, GeneBridge publication claim, or AIVC's core context-value question.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/overview]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/AIVC/important-decisions]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-10-09-literature-radar]]
- [[02_Projects/AIVC/reviews/2026-10-11-NIA-K99-study-section-review]]
- [[09_Planning/weekly-strategies/2026-10-05-AIVC-GeneBridge-weekly-strategy]]
- [[09_Planning/active-tasks]]
