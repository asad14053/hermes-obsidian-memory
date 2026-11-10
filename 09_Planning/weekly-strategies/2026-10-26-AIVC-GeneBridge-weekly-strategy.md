---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-10-26
status: active
created: 2026-10-26
last_updated: 2026-10-26
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-10-25-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-10-23-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The project remains evidence-limited, not idea-limited. The October 25 mock review remains **Overall Impact 8/9 — STAGNANT**: no aging/AD premise-and-access decision, no executed AIVC benchmark, and no verified current GeneBridge result package. Last week's three deliverables are still undocumented as complete. They remain the correct priorities, but this week they must be treated as sequential gates with frozen outputs rather than extended planning.

The October 23 literature sharpens the design rather than expanding the scope: perturbation representation, response head, and spatial context must eventually be varied separately; transport is a serious comparator; attention is not mechanistic evidence; and useful intervention prioritization requires experimental validation. None of that justifies adding architecture before establishing that measured spatial context adds predictive value. Canonical AIVC remains SCZ-centered unless the user explicitly changes it; the aging/AD work below is a separate NIA feasibility branch.

## #1 MUST DO — Close the NIA aging/AD premise-and-access gate

**SCIENTIFIC QUESTION**  
Is there one accessible aging/AD-relevant neural or glial system in which a defined environment or exposure modifies a measured response to a limited perturbation class across independent biological units, with a feasible validation route?

**WHY NOW**  
This is still the fatal K99 weakness and has remained incomplete across multiple weekly plans. Without a selected population, context, intervention, endpoint, biological replication, and access path, neither model building nor grant prose can create NIA preliminary evidence. A documented NO-GO is more useful than another candidate-data list.

**HYPOTHESIS**  
At least one public or collaborator-accessible system contains controls and the same perturbation class in two prespecified aging/AD-relevant contexts, with replicate-resolved metadata, usable dose/time and batch information, practical overlap, a measured molecular response, and an independent or prospective validation route.

**EXPERIMENT**  
Time-box a feasibility audit to two working days and at most three candidate systems. For each candidate, verify accession or written access; biological-unit IDs; population; aging/AD relevance; exposure/context; perturbation and matched control; dose/time; batch/platform; molecular and functional endpoints; and count/raw-data availability. Build the context × perturbation × biological-unit support table and design matrix before downloading full matrices. Select exactly one system and one response estimand, or issue NO-GO and define the minimum collaborator-generated pilot needed.

**DATA REQUIRED**  
Sample-level metadata and access evidence; donor/animal/independent-culture IDs; context, perturbation, control, cell population, dose, time, batch, and platform; endpoint definitions; raw/count availability; and evidence for an independent dataset or prospective assay. GeneBridge must not be counted as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata/support audit; design-rank, overlap, and confounding diagnostics; biological-unit-grouped split plan; deployment-input declaration; and precision assessment on the true biological units. If an eligible design exists, prespecify an interaction estimand such as:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
I_p = E_d[Delta_d,e1,p - Delta_d,e0,p]
Y_d,b,r = beta0 + betaE*E + betaP*P + betaEP*(E*P)
          + gamma_batch + b_d + epsilon_d,b,r
```

The exact likelihood and repeated-measures structure must follow the selected assay. Full rank alone does not establish identification or adequate support.

**BASELINE**  
The gate baseline is **no eligible NIA design**. For a passing system, preregister no-change/control mean, shared perturbation mean, nearest-context transfer, and additive ridge without an environment × perturbation term before any AIVC model.

**METRIC**  
Primary: binary eligibility for an estimable context × perturbation response with independent biological replication, matched controls, practical overlap, protected testing, and a named validation route. Secondary: biological units per stratum, missing-control rate, context–cohort/platform confounding, support/weight concentration, projected interval width, and endpoint compatibility.

**SUCCESS CRITERION**  
By the end of working day two, save `02_Projects/AIVC/aging_AD_AIVC_premise_v1.md` with exactly one population, context, perturbation class, response estimand, verified access/support table, confounding and overlap audit, grouped split plan, endpoint, simple baselines, precision-based decision rule, validation route, and explicit **COMMIT** or **NO-GO**. COMMIT requires every eligibility element; producing a defensible NO-GO still completes the decision task.

**FAILURE INTERPRETATION**  
If no candidate passes, current evidence cannot support the proposed NIA context-dependent perturbation premise. Do not pool incompatible cohorts, relabel cross-sectional disease tissue as intervention data, or convert the SCZ GeneBridge cohort into aging/AD evidence. Failure to issue either decision after the time box is execution failure, not scientific uncertainty.

**EXPECTED OUTPUT**  
One premise-and-access decision artifact ending in COMMIT or NO-GO, plus either the next executable benchmark specification or the minimum missing collaborator pilot.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Lock the GeneBridge disease-effect preservation package

**SCIENTIFIC QUESTION**  
When measured Xenium genes are hidden and imputed, does the final GeneBridge method preserve donor-level SCZ diagnosis-effect direction and magnitude across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the nearest manuscript-grade asset and the clearest evidence that the independent program can execute cohort-scale spatial genomics. The vault still contains historical DE counts, a reported ENVI lead, an unverified final method panel, and a 24-donor inventory whose remembered list contains only 23 names. Reconstruction accuracy alone does not justify biological discovery from imputed genes.

**HYPOTHESIS**  
Across all eligible held-out Xenium genes from all three folds and the same verified 23-donor × 7-layer analysis units, the final method will preserve measured SCZ coefficients better than the strongest simple/nonspatial imputation baseline while maintaining calibrated donor-level null behavior.

**EXPERIMENT**  
Freeze prediction paths and checksums, software/model versions, the actual method panel, all three gene-fold manifests, the complete 24-donor reference inventory, the 23-donor analysis cohort, Br6432 exclusion, and every other exclusion. Aggregate measured and imputed values to identical donor × layer units. After a blinded rank/confounding audit, freeze one transformation, complete eligible gene universe, repeated-donor implementation, diagnosis contrast, exact model, and multiplicity rule. Fit the same analysis to measured values and every verified method. Bootstrap donors for uncertainty and perform covariate-aware donor-level diagnosis resampling for null calibration; repeat any outcome-based gene selection within each resample.

**DATA REQUIRED**  
Measured 300-gene Xenium data; prediction outputs for every verified method; three fold manifests; complete donor inventory; diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; current logs, software/model versions, and checksums; and a separately harmonized reference-paper gene universe.

**MODEL / METHOD**  
Primary proposed formula, retained only if the verified design is estimable:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Use the repeated-donor method supported by the final software. Add run or slide only if prespecified and estimable; do not include both merely because both exist. Use donor bootstrap rather than cell or layer bootstrap and donor-level covariate-aware null resampling.

**BASELINE**  
Measured held-out genes are ground truth. Comparators: training-derived layer-specific gene mean, one verified nonspatial imputation baseline, SpaGE if present in current outputs, and every method actually represented in the final panel. Do not assume the remembered six-method list or ENVI's historical lead.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients over the complete eligible held-out-gene universe. Secondary: sign concordance, coefficient RMSE, calibration slope/intercept, donor-bootstrap intervals, fold stability, discovery overlap at frozen thresholds, and diagnosis-resampling false-positive/discovery behavior.

**SUCCESS CRITERION**  
Deliver the complete all-fold, all-method package regardless of outcome. Advance the claim that imputation preserves disease effects only if the final method beats the strongest simple/nonspatial baseline on the primary metric with a donor-bootstrap 95% interval for the improvement above zero, measured–imputed concordance is positive without material systematic calibration bias, and null resampling shows no excess discoveries at the declared threshold. No poor method, fold, or gene may be omitted post hoc.

**FAILURE INTERPRETATION**  
Good reconstruction with weak, unstable, or biased diagnosis-effect concordance means imputed genes should not support SCZ discovery claims. That complete negative benchmark remains publishable. A changed winner or inconsistent donor/fold inventory indicates pipeline-version instability and blocks manuscript figures until resolved.

**EXPECTED OUTPUT**  
Verified method/version/checksum table; donor/exclusion/fold manifest; frozen analysis specification; measured-versus-imputed coefficient figure and table; donor-bootstrap and null-calibration report; manuscript-ready conclusion; and an evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Execute the first nuisance-aware measured-target AIVC context-value test

**SCIENTIFIC QUESTION**  
Does local multicellular context improve prediction of measured held-out Xenium targets in unseen donors beyond identity, design covariates, target-independent assay nuisance, and simple pooled or multiscale context summaries?

**WHY NOW**  
AIVC still has no completed benchmark. The latest literature makes architecture-only novelty weaker: strong transport and prior-knowledge/simple-head comparators matter, and learned gates or attention cannot establish mechanism. The immediate pilot should therefore ask only whether spatial context contains reproducible predictive information. Start it only after Priority #2 locks donor, exclusion, and gene-fold manifests. This is SCZ conditional-prediction engineering—not aging/AD, perturbation, or causal evidence.

**HYPOTHESIS**  
Cell-type-stratified local measured-expression summaries contain donor-transportable information beyond intrinsic identity and target-independent nuisance; the gain will exceed pooled/multiscale comparators and support-matched shuffle nulls and will not be driven by one donor, layer, density regime, or technical spatial field.

**EXPERIMENT**  
Split donors before normalization, feature construction, nuisance estimation, feature selection, or tuning. Use measured Xenium inputs and targets only and exclude the focal cell from each neighborhood. Freeze target-independent nuisance variables, radii/scales, cell-type strata, minimum-neighbor rules, and one pathway/module endpoint without final-test outcomes. Under identical nested donor-grouped folds and tuning budgets compare identity/design only, identity/design plus nuisance, pooled fixed-radius context, simple multiscale context, and cell-type-stratified context. Fit one small residual MLP only if the stratified linear model first beats every simpler comparator. Run support-matched replacement and within-stratum shuffle diagnostics on the frozen model.

**DATA REQUIRED**  
Measured Xenium expression; coordinates; cell type and layer; donor, run, slide, density, morphology/QC metadata; locked exclusions and gene folds; target-independent nuisance definitions; and pathway/module definitions frozen without final-test information.

**MODEL / METHOD**  
Regularized multi-output regression with nested donor-grouped tuning:

```text
M0:  Y = identity + design
MQ:  Y = identity + design + target-independent nuisance
MQE: Y = identity + design + target-independent nuisance + context
Delta L_d = L_d(MQ) - L_d(MQE)
```

Use nuisance adjustment as a sensitivity analysis, not proof of biological causality. Frozen-checkpoint replacement measures predictive reliance under the selected replacement distribution, not mechanism.

**BASELINE**  
Training-fold global mean; cell-type/layer mean; M0; MQ; MQ plus unstratified pooled context; and MQ plus simple fixed multiscale context. Exclude learned attention, graph models, conditional VAEs, transport models, and perturbation embeddings from this week's pilot.

**METRIC**  
Primary: donor-averaged protected-test loss and paired donor-level loss reduction for cell-type-stratified MQE versus the strongest eligible baseline. Secondary: per-gene Spearman correlation and RMSE, calibration, donor/layer stability, empirical shuffle-null percentile, spatial/nuisance-field alignment, radius and density sensitivity, and replacement response.

**SUCCESS CRITERION**  
Advance richer context modeling only if the stratified context model improves on the strongest nuisance-aware simple baseline, the donor-bootstrap 95% interval for paired improvement excludes zero and exceeds a practical threshold frozen from control/replicate variability before final testing, the gain exceeds the 95th percentile of the support-matched shuffle null, and no single donor, layer, density regime, or technical field explains it. Retain the MLP only if it adds protected-test value over the linear context model.

**FAILURE INTERPRETATION**  
A precise null with functioning controls argues against the chosen target/scale as an AIVC context benchmark. Gain reproduced by matched shuffles or aligned with technical fields indicates leakage, technical spatial structure, or proxy use. Gain confined to one donor/layer indicates poor transport. Failed sensitivity controls are inconclusive. None of these outcomes tests perturbation biology.

**EXPECTED OUTPUT**  
Versioned data contract and experiment-registry entry; locked manifests; leakage/nuisance audit; all baseline predictions; donor-level paired-loss and shuffle-null figures; subgroup-stability table; update to [[02_Projects/AIVC/experiments-and-results]]; and an explicit advance/stop/inconclusive decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop architecture expansion.** Do not spend this week adding a GNN, transformer, hierarchical attention, conditional VAE, multimodal branch, transport decoder, or “universal” component. Until a measured-target baseline demonstrates context value beyond nuisance-aware simple comparators, architecture work adds implementation debt without resolving the publication claim, K99 premise, or independent-program question.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/overview]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-10-23-literature-radar]]
- [[02_Projects/AIVC/literature/important-literature]]
- [[02_Projects/AIVC/reviews/2026-10-25-NIA-K99-study-section-review]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/datasets]]
- [[02_Projects/GeneBridge/methods]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]]
- [[09_Planning/active-tasks]]
