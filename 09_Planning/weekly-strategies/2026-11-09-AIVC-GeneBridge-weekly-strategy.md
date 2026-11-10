---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-11-09
status: active
created: 2026-11-09
last_updated: 2026-11-09
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-11-02-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-11-08-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-11-06-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The three scientific gates from last week remain undocumented as complete. The November 8 mock NIA review is still **Overall Impact 8/9 — STAGNANT**: no aging/AD premise-and-access decision, executed AIVC benchmark, frozen GeneBridge evidence package, or committed training/independence package was found. Current GeneBridge numerical summaries and ENVI leadership remain historical and marked `VERIFY`; AIVC still has no confirmed result set. The November 6 literature radar adds strong architecture comparators and audit controls, but no applicant-generated evidence and no schizophrenia-specific result that changes execution order.

Do not create new aims to escape unfinished work. This week has three sequential priorities. Priority #1 is a two-working-day decision gate. Priority #2 receives the main analysis effort. Priority #3 starts only after the GeneBridge donor, exclusion, method, and fold manifests are frozen. Canonical AIVC remains SCZ-centered; aging/AD remains a separate NIA feasibility branch unless explicitly adopted later.

## #1 MUST DO — Issue the NIA aging/AD premise-and-access COMMIT/NO-GO

**SCIENTIFIC QUESTION**  
Is there one accessible aging/AD-relevant human neural or glial system in which a defined context or exposure modifies response to a bounded perturbation class across independent biological units, with matched controls and a feasible experimental validation route?

**WHY NOW**  
This remains the fatal NIA feasibility gap after repeated weekly plans. Without one population, context, perturbation, endpoint, support structure, access path, and validation assay, more grant prose or model design cannot improve the K99. A documented NO-GO is useful because it prevents an unfundable premise from consuming further effort.

**HYPOTHESIS**  
At least one of no more than three candidate systems has sufficient biological-unit replication and practical context-by-perturbation overlap to estimate a prespecified interaction, with usable dose/time and batch metadata, a measured molecular response, and an independent or prospective validation route.

**EXPERIMENT**  
Time-box a metadata-and-access audit to two working days and at most three candidate systems. Before downloading full matrices, verify the accession or written access; population; aging/AD relevance; context/exposure; perturbation and matched control; dose and time; donor/animal/independent-culture identifiers; batch/platform; molecular and functional endpoints; raw/count availability; and validation access. Build a context × perturbation × biological-unit support table and design matrix. Select exactly one system and one response estimand, or issue NO-GO and define the minimum collaborator-generated pilot required.

**DATA REQUIRED**  
Sample-level metadata; independent biological-unit IDs; context/exposure, perturbation, control, population, dose, time, batch, and platform fields; endpoint definitions; raw/count availability; access evidence; and written evidence for an independent dataset or prospective assay. GeneBridge cannot count as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata/support audit; design-rank, overlap, confounding, and weight-concentration diagnostics; biological-unit-grouped split plan; deployment-input declaration; and precision assessment at the true assignment unit. For an eligible repeated-measures system, prespecify the context-by-perturbation interaction, adapting likelihood and random effects to the assay:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
I_p = E_d[Delta_d,e1,p - Delta_d,e0,p]
Y_d,b,r = beta0 + betaE*E + betaP*P + betaEP*(E*P)
          + gamma_batch + b_d + epsilon_d,b,r
```

Full rank is necessary but does not establish identification, overlap, or adequate precision.

**BASELINE**  
Gate baseline: no eligible NIA design. If a system passes, preregister no-change/control mean, shared perturbation mean, nearest-context transfer, and additive ridge without an environment × perturbation term before any AIVC architecture.

**METRIC**  
Primary: binary eligibility for an estimable context × perturbation response with independent biological replication, matched controls, practical overlap, protected testing, and a named validation route. Secondary: biological units per stratum, missing-control rate, context–cohort/platform confounding, support/weight concentration, projected interval width, and endpoint compatibility.

**SUCCESS CRITERION**  
By the end of working day two, save `02_Projects/AIVC/aging_AD_AIVC_premise_v1.md` with exactly one population, context/exposure, perturbation class, dose/time, response estimand, verified support table, confounding/overlap audit, grouped split plan, endpoint, simple baselines, precision rule, validation route, and explicit **COMMIT** or **NO-GO**. COMMIT requires every eligibility element; a defensible NO-GO completes the gate.

**FAILURE INTERPRETATION**  
If no candidate passes, current evidence cannot support the proposed NIA context-dependent perturbation premise. Do not pool incompatible cohorts, relabel cross-sectional tissue as intervention data, or treat SCZ GeneBridge as aging/AD evidence. Failure to issue either decision after the time box is an execution failure, not scientific uncertainty.

**EXPECTED OUTPUT**  
One premise-and-access decision artifact ending in COMMIT or NO-GO, plus either an executable benchmark specification or the minimum missing collaborator pilot.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Freeze and execute the GeneBridge disease-effect preservation benchmark

**SCIENTIFIC QUESTION**  
When measured Xenium genes are masked and imputed, does the final GeneBridge method preserve donor-level SCZ diagnosis-effect direction and magnitude across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the nearest publishable asset and the strongest current evidence of independent execution in human cortical spatial genomics. Yet the method panel, complete donor inventory, fold manifests, versions, checksums, and reported DE results are not frozen in the vault. Reconstruction accuracy alone cannot justify biological discovery from imputed genes.

**HYPOTHESIS**  
Across every eligible held-out Xenium gene in all three prespecified folds and identical donor × layer units, the final verified method preserves measured SCZ coefficients better than the strongest simple or nonspatial baseline while maintaining calibrated donor-level null behavior.

**EXPERIMENT**  
Freeze prediction paths and checksums, software/model versions, actual method panel, all three gene-fold manifests, the complete 24-donor reference inventory, the 23-donor analysis cohort, Br6432 exclusion, and every other exclusion. Aggregate measured and imputed values to the same donor × layer units. Before method comparison, freeze one transformation, eligible-gene universe, repeated-donor implementation, diagnosis contrast, covariates, and multiplicity family after rank/confounding checks. Fit the identical model to measured values and every verified method. Bootstrap donors for uncertainty and run covariate-aware donor-level diagnosis resampling for null calibration; repeat any outcome-based gene selection inside each resample.

**DATA REQUIRED**  
Measured 300-gene Xenium data; predictions for every verified method; three fold manifests; complete donor inventory; diagnosis, age, sex, layer, run/slide, QC, and exclusion metadata; current logs, software/model versions, and checksums; and a separately harmonized reference-paper gene universe.

**MODEL / METHOD**  
Primary proposed model, retained only if the verified design is estimable:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Use the repeated-donor method supported by the final software. Add run or slide only if prespecified and estimable; do not add both simply because both exist. Use donor bootstrap—not cell or layer bootstrap—and donor-level covariate-aware null resampling.

**BASELINE**  
Measured held-out genes are ground truth. Comparators: training-derived layer-specific gene mean, one verified nonspatial imputation baseline, SpaGE if present in current outputs, and every method actually represented in the final panel. Do not assume the remembered six-method list or ENVI's historical lead.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients over the complete eligible held-out-gene universe. Secondary: sign concordance, coefficient RMSE, calibration slope/intercept, donor-bootstrap intervals, fold stability, discovery overlap under frozen thresholds, and diagnosis-resampling false-positive/discovery behavior.

**SUCCESS CRITERION**  
Deliver the complete all-fold, all-method package regardless of outcome. Claim disease-effect preservation only if the final method beats the strongest simple/nonspatial baseline on the primary metric, the donor-bootstrap 95% interval for that improvement is above zero, measured–imputed concordance is positive without material systematic calibration bias, and null resampling shows no excess discoveries at the declared threshold. No weak method, fold, or gene may be omitted post hoc.

**FAILURE INTERPRETATION**  
Good reconstruction with weak, unstable, or biased diagnosis-effect concordance means imputed genes should not support SCZ discovery claims. A complete negative benchmark is still publication-relevant. A changed winner or inconsistent donor/fold inventory indicates pipeline-version instability and blocks manuscript figures until resolved.

**EXPECTED OUTPUT**  
Verified method/version/checksum table; donor/exclusion/fold manifest; frozen analysis specification; measured-versus-imputed coefficient figure and table; donor-bootstrap and null-calibration report; manuscript-ready conclusion; and an evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Execute the first nuisance-aware measured-target AIVC context-value test

**SCIENTIFIC QUESTION**  
Does local multicellular context improve prediction of measured held-out Xenium targets in unseen donors beyond intrinsic identity, design covariates, target-independent assay nuisance, and simple pooled or multiscale context summaries?

**WHY NOW**  
AIVC still has no executed benchmark. The latest literature makes architecture-only novelty weak and reinforces replicate-aware truth, independent biological-unit splits, expression-matched or support-matched negatives, and strong simple baselines. The first result should determine whether spatial context contains reproducible predictive information at all. Start only after Priority #2 locks donor, exclusion, and gene-fold manifests.

**HYPOTHESIS**  
Cell-type-stratified local measured-expression summaries contain donor-transportable information beyond intrinsic identity and target-independent nuisance; their gain exceeds pooled/multiscale comparators and support-matched shuffle nulls and is not explained by one donor, layer, density regime, or technical spatial field.

**EXPERIMENT**  
Split donors before normalization, feature construction, nuisance estimation, feature selection, or tuning. Use measured Xenium inputs and measured targets only; exclude the focal cell from every neighborhood. Freeze target-independent nuisance variables, radii/scales, cell-type strata, minimum-neighbor rules, and one pathway/module endpoint without final-test outcomes. Under identical nested donor-grouped folds and tuning budgets, compare identity/design only, identity/design plus nuisance, pooled fixed-radius context, simple multiscale context, and cell-type-stratified context. Fit one small residual MLP only if the stratified linear model first beats every simpler comparator. Run support-matched replacement and within-stratum shuffle diagnostics on the frozen model.

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

Nuisance adjustment is a sensitivity analysis, not proof of biological causality. Frozen-checkpoint replacement tests predictive reliance under the selected replacement distribution, not mechanism.

**BASELINE**  
Training-fold global mean; cell-type/layer mean; M0; MQ; MQ plus unstratified pooled context; and MQ plus fixed multiscale context. Exclude graph models, transformers, conditional VAEs, spectral repositioning, pathway-graph modules, perturbation embeddings, and interpretability modules from this pilot.

**METRIC**  
Primary: donor-averaged protected-test loss and paired donor-level loss reduction for cell-type-stratified MQE versus the strongest eligible baseline. Secondary: per-gene Spearman correlation and RMSE, calibration, donor/layer stability, empirical shuffle-null percentile, spatial/nuisance-field alignment, radius and density sensitivity, and replacement response.

**SUCCESS CRITERION**  
Advance richer context modeling only if the stratified context model improves on the strongest nuisance-aware simple baseline, the donor-bootstrap 95% interval for paired improvement excludes zero and exceeds a practical threshold frozen from control/replicate variability before final testing, the gain exceeds the 95th percentile of the support-matched shuffle null, and no single donor, layer, density regime, or technical field explains it. Retain the MLP only if it adds protected-test value over the linear context model.

**FAILURE INTERPRETATION**  
A precise null with functioning controls argues against the chosen target/scale as an AIVC context benchmark. Gain reproduced by matched shuffles or aligned with technical fields indicates leakage, assay structure, or proxy use. Gain confined to one donor or layer indicates poor transport. Failed controls make the result inconclusive. None of these outcomes tests perturbation biology.

**EXPECTED OUTPUT**  
Versioned data contract and experiment-registry entry; locked manifests; leakage/nuisance audit; all baseline predictions; donor-level paired-loss and shuffle-null figures; subgroup-stability table; update to [[02_Projects/AIVC/experiments-and-results]]; and an explicit advance/stop/inconclusive decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop architecture and literature expansion this week.** Do not add a GNN, graph transformer, SPEAR-style spectral repositioning, RAPTORGraph-style pathway module, conditional VAE, foundation-model branch, Perturbscape layer, multimodal integration branch, or another broad literature review. These are future comparisons, not current bottlenecks. They add implementation and planning debt without closing the NIA feasibility gate, validating the GeneBridge publication claim, or establishing that AIVC spatial context has measurable value.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-11-06-literature-radar]]
- [[02_Projects/AIVC/reviews/2026-11-08-NIA-K99-study-section-review]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[09_Planning/active-tasks]]
- [[09_Planning/unanswered-questions]]
- [[09_Planning/weekly-strategies/2026-11-02-AIVC-GeneBridge-weekly-strategy]]
