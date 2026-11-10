---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-10-19
status: active
created: 2026-10-19
last_updated: 2026-10-19
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-10-12-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-10-18-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-10-16-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The evidence state is still stalled: no finalized AIVC benchmark is documented, GeneBridge's current notes still contain historical values that require verification, and the October 18 mock NIA review remains **Overall Impact 8/9 — STAGNANT**. The repeated aging/AD premise-and-access task was not documented as completed last week. This week should force that binary decision, finish the nearest manuscript-grade GeneBridge analysis, and start an AIVC context test only from the resulting locked manifests.

The October 16 literature raises the bar for the AIVC pilot: donor holdout is insufficient if a model can exploit reproducible assay gradients; fixed-radius and simple multi-scale context must precede learned attention; measured targets, not imputed pseudo-labels, must determine success. The three priorities below are sequential rather than three parallel projects.

## #1 MUST DO — Close the NIA aging/AD premise with COMMIT or NO-GO

**SCIENTIFIC QUESTION**  
Is there one accessible aging/AD-relevant neural or glial system in which a defined context or exposure modifies a measured response to a limited perturbation class across independent biological units, with an executable validation route?

**WHY NOW**  
This remains the fatal K99 weakness after several weekly plans. Until population, context, perturbation, endpoint, support, and assay access are fixed, architecture work cannot generate NIA preliminary evidence. A documented no-go is more valuable than another unranked dataset list.

**HYPOTHESIS**  
At least one public or collaborator-accessible system has replicate-resolved controls and perturbations in both prespecified contexts, usable dose/time and batch metadata, practical overlap, and independent or prospective validation access without context being inseparable from cohort or platform.

**EXPERIMENT**  
Time-box the audit to two working days and no more than three candidate systems. For each, verify accession or written collaborator access; biological-unit IDs; population; aging/AD context or justified exposure; perturbation/control; dose/time; batch/platform; measured molecular and functional endpoints; and raw/count availability. Build the context × perturbation × biological-unit support table and design matrix before downloading full expression matrices. Select exactly one system and estimand, or issue NO-GO with the minimum collaborator-generated pilot required.

**DATA REQUIRED**  
Sample-level metadata and access evidence; donor/replicate IDs; context, perturbation, control, population, dose, time, batch, and platform; measured endpoint definitions; raw/count availability; and evidence for an independent dataset or prospective assay. GeneBridge cannot be counted as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata/support audit, design-rank and overlap diagnostics, confounding map, donor/replicate-grouped split plan, and precision calculation at the true biological-unit level. Declare deployment-available inputs and separate calibration from protected testing. Full rank alone does not establish causal identification or adequate support.

**BASELINE**  
The null baseline is **no eligible NIA design**. If a system passes, preregister control mean, shared perturbation mean, nearest-context transfer, and additive ridge without a context × perturbation term before any AIVC model.

**METRIC**  
Binary eligibility gate: an estimable context × perturbation response with independent biological replication, matched controls, practical overlap, protected testing, and a named validation route. Secondary diagnostics are units per stratum, missing-control rate, context–cohort/platform confounding, projected interval width, and endpoint compatibility.

**SUCCESS CRITERION**  
By the end of working day two, save one premise artifact with the exact population, context, perturbation class, response estimand, verified access/support table, confounding and overlap audit, split plan, endpoint, simple baselines, precision-based decision rule, nuisance-information boundary, validation route, and explicit **COMMIT** or **NO-GO**. Either binary outcome completes this priority.

**FAILURE INTERPRETATION**  
If no system passes, the present evidence cannot support the proposed NIA context-dependent perturbation claim. Do not pool incompatible cohorts, relabel cross-sectional disease tissue as intervention data, or convert the SCZ GeneBridge cohort into aging/AD evidence. Failure to make the decision after the time box is an execution failure, not scientific uncertainty.

**EXPECTED OUTPUT**  
`02_Projects/AIVC/aging_AD_AIVC_premise_v1.md`, ending in COMMIT or NO-GO and specifying the next executable experiment or the minimum missing pilot.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Finish the GeneBridge disease-effect preservation package

**SCIENTIFIC QUESTION**  
When measured Xenium genes are hidden and imputed, does the final GeneBridge method preserve donor-level SCZ diagnosis-effect direction and magnitude across cortical layers without generating false disease associations?

**WHY NOW**  
GeneBridge is the nearest publishable asset and the strongest available evidence of execution for a K99 and faculty program. The current record still relies on historical DE counts, an unverified method panel, and an incomplete remembered donor list. Reconstruction metrics alone do not justify biological claims from imputed genes.

**HYPOTHESIS**  
On the same 161 donor × layer units and complete eligible held-out-gene universe, the verified final GeneBridge method will preserve measured SCZ coefficients better than the strongest simple/nonspatial imputation baseline while maintaining calibrated donor-level null behavior.

**EXPERIMENT**  
Freeze prediction paths and checksums, software/model versions, the actual final method panel, all three gene-fold manifests, the 24-donor reference inventory, the 23-donor analysis cohort, Br6432 exclusion, and every other exclusion. Aggregate measured and imputed values to identical donor × layer units. After a blinded rank/confounding audit, freeze one transformation, gene universe, repeated-donor implementation, diagnosis formula, and multiple-testing rule. Fit the same model to measured values and each verified method; bootstrap donors for uncertainty and use covariate-aware donor-level diagnosis resampling for null calibration. Repeat any outcome-based gene selection inside each resample.

**DATA REQUIRED**  
Measured 300-gene Xenium data; predictions from every method represented by current outputs; three gene-fold manifests; donor, diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; current logs and versions; and a separately harmonized reference-paper gene universe.

**MODEL / METHOD**  
Primary proposed model, retained only if estimable under the verified metadata:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Use the repeated-donor method supported by the final software. Add run or slide only if prespecified and estimable; do not include both merely because they exist. Use donor bootstrap, not cell or layer bootstrap, and donor-level covariate-aware null resampling.

**BASELINE**  
Measured held-out genes are truth. Comparators are training-derived layer-specific gene mean, one verified nonspatial imputation baseline, SpaGE if present in current outputs, and every method actually in the final panel. Do not assume the remembered six-method list or ENVI's historical lead.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients across the complete eligible held-out-gene universe. Secondary: sign concordance, coefficient RMSE, calibration slope/intercept, donor-bootstrap intervals, fold stability, discovery overlap at frozen thresholds, and diagnosis-resampling false-positive/discovery behavior.

**SUCCESS CRITERION**  
The all-fold, all-method package must be delivered regardless of outcome. A claim that imputation preserves disease effects advances only if the final method beats the strongest simple/nonspatial baseline on the primary metric with a donor-bootstrap 95% interval for the improvement above zero, measured–imputed concordance is positive with no material systematic calibration bias, and null resampling shows no excess discoveries at the declared threshold. No poor method, fold, or gene may be omitted post hoc.

**FAILURE INTERPRETATION**  
Good reconstruction with weak, unstable, or biased diagnosis-effect concordance means imputed genes should not support SCZ discovery claims. That negative benchmark is still publishable if complete and calibrated. A changed method winner or inconsistent donor/fold inventory indicates pipeline-version instability and blocks final manuscript figures.

**EXPECTED OUTPUT**  
Verified method/version/checksum table; donor/exclusion/fold manifest; frozen analysis specification; measured-versus-imputed coefficient figure and table; donor-bootstrap and null-calibration report; manuscript-ready conclusion; and an evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Run a nuisance-aware measured-target AIVC context-value test

**SCIENTIFIC QUESTION**  
Does local multicellular context improve prediction of measured held-out Xenium targets in unseen donors beyond identity, design covariates, target-independent assay nuisance, and simple pooled or multi-scale context summaries?

**WHY NOW**  
AIVC still lacks one registered benchmark. The October 16 radar shows why the earlier context test is insufficient: technical spatial fields can mimic biological neighborhoods, and simple multi-scale features are strong comparators. This pilot is justified only after Priority #2 locks donor and gene-fold manifests. It is SCZ conditional-prediction engineering—not aging/AD, perturbation, or causal evidence.

**HYPOTHESIS**  
Cell-type-stratified local measured-expression summaries contain donor-transportable predictive information beyond identity and target-independent nuisance covariates; the gain will exceed pooled/multi-scale baselines and support-matched context-shuffle nulls without being driven by one donor, layer, density regime, or spatial assay field.

**EXPERIMENT**  
Split donors before normalization, feature construction, nuisance estimation, feature selection, or tuning. Use measured Xenium inputs and targets only; exclude the focal cell from each neighborhood. Freeze target-independent nuisance variables, radius/scale set, cell-type strata, minimum-neighbor rules, and one pathway/module endpoint without protected-test outcomes. Under identical nested donor-grouped folds and tuning budgets compare: identity/design only (M0), identity/design plus nuisance (MQ), MQ plus pooled fixed-radius context, MQ plus simple multi-scale context, and MQ plus cell-type-stratified context. Fit one small residual MLP only if the stratified linear model first beats all simpler comparators. Run support-matched replacement and within-stratum shuffle diagnostics on the frozen model.

**DATA REQUIRED**  
Measured Xenium expression; coordinates; cell type and layer; donor, run, slide, density and QC metadata; locked exclusions and gene folds; target-independent nuisance definitions; and pathway/module definitions fixed without final-test information.

**MODEL / METHOD**  
Use regularized multi-output regression for primary comparisons with nested donor-grouped tuning:

```text
M0:  Y = identity + design
MQ:  Y = identity + design + target-independent nuisance
MQE: Y = identity + design + target-independent nuisance + context
Delta L_d = L_d(MQ) - L_d(MQE)
```

Treat nuisance adjustment as sensitivity analysis, not proof of biological causality: morphology and density may contain biology, and residualization can overcorrect. Frozen-checkpoint replacement tests reliance under a chosen replacement distribution, not mechanism.

**BASELINE**  
Training-fold global mean; cell-type/layer mean; M0; MQ; MQ plus unstratified pooled context; and MQ plus a simple fixed multi-scale summary. Learned attention, graph models, and conditional VAEs are excluded from this week's comparison.

**METRIC**  
Primary: donor-averaged protected-test loss and paired donor-level reduction for MQE versus the strongest eligible baseline. Secondary: per-gene Spearman correlation and RMSE, calibration, donor/layer stability, empirical shuffle-null percentile, spatial/nuisance-field alignment, radius sensitivity, density sensitivity, and replacement response.

**SUCCESS CRITERION**  
Advance richer context modeling only if the stratified context model improves on the strongest nuisance-aware simple baseline, the donor-bootstrap 95% interval for paired improvement excludes zero and exceeds a practical threshold fixed from control/replicate variability before final testing, the gain exceeds the 95th percentile of the support-matched shuffle null, and no single donor, layer, density regime, or inferred technical field explains it. Retain the MLP only if it adds protected-test value over the linear context model.

**FAILURE INTERPRETATION**  
A precise null result with functioning sensitivity controls argues against the chosen target/scale as an AIVC context benchmark. Gain reproduced by matched shuffles or aligned with nuisance fields suggests leakage, technical spatial structure, or proxy use. Gain confined to one donor/layer indicates poor transport. Sensitivity-control failure is inconclusive. None of these outcomes establishes perturbation biology.

**EXPECTED OUTPUT**  
Versioned data contract and registry entry; locked manifests; leakage/nuisance audit; all baseline predictions; donor-level paired-loss and shuffle-null figures; subgroup stability table; update to [[02_Projects/AIVC/experiments-and-results]]; and an explicit advance/stop/inconclusive decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop architecture expansion.** Do not spend this week adding GNN, transformer, hierarchical-attention, conditional-VAE, multimodal, or “universal” components. Until the measured-target baseline demonstrates context value beyond nuisance-aware simple comparators, this work adds implementation debt without resolving the biological premise, publication claim, or K99 weakness.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-10-16-literature-radar]]
- [[02_Projects/AIVC/reviews/2026-10-18-NIA-K99-study-section-review]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[09_Planning/weekly-strategies/2026-10-12-AIVC-GeneBridge-weekly-strategy]]
- [[09_Planning/active-tasks]]
