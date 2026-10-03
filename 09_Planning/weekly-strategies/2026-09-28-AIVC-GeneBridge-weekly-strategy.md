---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-09-28
status: active
created: 2026-09-28
last_updated: 2026-09-28
confidence: medium
previous_strategy: "[[09_Planning/weekly-strategies/2026-09-21-AIVC-GeneBridge-weekly-strategy]]"
latest_nih_review: "[[02_Projects/AIVC/reviews/2026-09-27-NIA-K99-study-section-review]]"
latest_literature_radar: "[[02_Projects/AIVC/literature/2026-09-25-literature-radar]]"
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The prior week's three deliverables remain undocumented. AIVC still has no frozen NIA premise or executed baseline, GeneBridge's historical results remain unverified, and the September 27 mock review remains **Overall Impact 8 / STAGNANT**. The September 25 literature radar strengthens one conclusion: useful context dependence must be demonstrated against simple pooled-context controls and frozen-model replacement tests; attention, reconstruction, and multimodal integration are not evidence by themselves.

This is therefore a decision-and-evidence week, not an architecture week. Priority #1 is a time-boxed K99 feasibility gate. Priority #2 protects the nearest publishable asset. Priority #3 generates the first direct test of AIVC's identity-plus-environment premise using measured Xenium targets, while remaining explicitly a SCZ engineering/premise pilot rather than aging/AD or perturbation evidence. The unresolved SCZ-versus-NIA focus is not silently resolved here.

## #1 MUST DO — Close the NIA premise gate with a commit/no-go decision

**SCIENTIFIC QUESTION**  
Is there an accessible aging/AD-relevant neural or glial system in which environmental context modifies a measured perturbation response across independent biological units, with enough overlap to distinguish context from donor, dataset, platform, dose, and time?

**WHY NOW**  
This is the repeated fatal K99 weakness and the unfinished #1 task from last week. Another week of model design without establishing data and assay feasibility increases scope but not grant credibility. The gate must now end in a documented commit or no-go, not another candidate list.

**HYPOTHESIS**  
At least one system has a prespecified cell population, exposure/context, perturbation class, measured response, repeated donor support, matched controls, and a credible validation route such that the context-by-perturbation contrast is estimable without making context synonymous with cohort.

**EXPERIMENT**  
Time-box the audit to two working days. For every serious candidate, verify accession/access, donor/biological-replicate identity, age/pathology or experimentally induced context, cell type, perturbation, control, dose, time, batch, platform, response genes/modules, and assay access. Construct context × perturbation × donor tables and the planned design matrix; test rank, overlap, and whether held-out donors can be formed before downloading full matrices. Select exactly one population, context, perturbation class, primary response endpoint, observational prediction estimand, and prospective intervention contrast. Name one primary dataset and either an independent validation dataset or a committed collaborator assay. If none passes, issue a formal no-go and define the minimum prospective experiment required.

**DATA REQUIRED**  
Verified sample-level metadata and accessions; donor/replicate IDs; age, diagnosis/pathology, or exposure labels; perturbation/control, dose, and time; cell population; batch/platform; measured response space; raw/count-level availability; cross-dataset gene/module compatibility; and written evidence of prospective assay access if public external validation is unavailable. GeneBridge is not eligible as aging/AD perturbation evidence.

**MODEL / METHOD**  
Metadata/design audit first. Use contingency tables, design-matrix rank and positivity checks, donor-grouped split generation, fold-local preprocessing rules, and replicate-level precision calculations. Keep the two targets distinct: `m(c,e,p,x) = E[Y | C=c,E=e,P=p,X=x]` for prediction versus `E[Y(e,p)-Y(e,p0)]` or the selected factorial contrast for intervention. For a prospective functional endpoint, the starting formula is `F ~ context * perturbation + batch + (1 | donor)`; dose/time and nesting must be fixed from the actual assay before adoption.

**BASELINE**  
The null feasibility position: no eligible design exists because context is confounded with cohort/platform or repeated donor–perturbation support is inadequate. If the gate passes, pre-register control mean, perturbation mean, nearest-neighbor transfer, and additive ridge without context as computational baselines.

**METRIC**  
Primary gate metric: whether the selected context-by-perturbation coefficient is identifiable in a full-rank design with independent biological replication and a donor-held-out test. Secondary: donor/replicate count by cell-context-perturbation stratum, matched-control completeness, overlap fraction, response-space compatibility, projected interval width, and availability of an independent validation route.

**SUCCESS CRITERION**  
By the end of day two, freeze `aging_AD_AIVC_premise_v1.md` containing one biological question, one population, one context, one perturbation class, one measured endpoint, exact estimands, verified data/access, donor-resolved design, split manifest, simple baselines, negative controls, precision-based go/no-go rule, and prospective validation route. A formal no-go also closes the gate successfully as a decision, but it blocks an NIA-ready computational premise until the specified experiment or collaboration exists.

**FAILURE INTERPRETATION**  
Failure to find a full-rank, replicated design means public data cannot support the proposed NIA claim. It does not justify pooling incompatible cohorts, treating cross-sectional AD tissue as perturbation response, or relabeling SCZ assets. The next grant action would be securing collaborator-generated pilot data or reconsidering whether NIA is the right mechanism.

**EXPECTED OUTPUT**  
`aging_AD_AIVC_premise_v1.md`; one verified dataset/access table; one context × perturbation × donor overlap table; design-rank report; donor split manifest; data dictionary; validation-access statement; and a signed-off commit/no-go decision.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 6/10

## #2 SHOULD DO — Lock GeneBridge disease-effect preservation evidence

**SCIENTIFIC QUESTION**  
When measured Xenium genes are masked and imputed, does the final GeneBridge method preserve donor-level SCZ effect sizes and directions across cortical layers without creating false disease associations?

**WHY NOW**  
GeneBridge is the strongest near-term publication and preliminary-work asset, but the final method panel, donor/fold accounting, exact DE model, historical significance counts, and reported ENVI lead are still marked for verification. Reconstruction metrics alone cannot justify downstream biological discovery.

**HYPOTHESIS**  
The selected spatial imputation method will recover measured held-out-gene SCZ effects more faithfully than layer-mean and nonspatial baselines while showing no excess diagnosis discoveries under donor-level null resampling.

**EXPERIMENT**  
Freeze checksums/paths for current measured and imputed outputs, software/model versions, all three gene folds, the 24-donor reference cohort, the 23-donor analysis cohort, Br6432 exclusion, and all additional exclusions. Aggregate measured and imputed values to identical donor × layer units for every eligible measured-but-held-out gene. Before viewing method comparisons, check design rank and freeze the primary model. Apply it unchanged to measured outcomes and every method. Compare gene-wise diagnosis coefficients and uncertainty, then assess null behavior using a covariate-aware donor-level resampling scheme; do not permute cells or layers independently.

**DATA REQUIRED**  
Measured expression for the 300 Xenium genes; three fold manifests; current predictions for every verified final-panel method; donor, Dx, age, sex, layer, run/slide, QC, and exclusion metadata; software/model versions; current job logs and output files; and the reference-paper gene universe for a separately harmonized comparison.

**MODEL / METHOD**  
Primary repeated-donor model for each gene on the declared common normalized scale: `y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l`, with donor as the repeated-measure block/random intercept. Use the same 161 donor × layer units and the same transformation for measured and imputed outcomes. Add no run/slide term to the primary model unless a blinded rank/confounding audit made before effect comparison shows that one prespecified term is both estimable and required; any such change must be versioned before fitting all methods. Bootstrap donors for coefficient-concordance uncertainty and apply one multiplicity universe shared across methods.

**BASELINE**  
Measured held-out genes as ground truth; layer-specific gene mean; a nonspatial imputation baseline; SpaGE; and every method actually verified in the final panel. Do not assume the remembered six-method list or ENVI ranking.

**METRIC**  
Primary: Spearman correlation between measured and imputed SCZ diagnosis coefficients across all eligible held-out genes. Secondary: sign concordance; regression slope/intercept; coefficient RMSE; donor-bootstrap confidence intervals; rank stability across folds; discovery precision/recall at frozen thresholds; and donor-level null false-positive behavior.

**SUCCESS CRITERION**  
Produce a file-traceable package covering all three folds and all eligible held-out genes with complete donor accounting and one frozen primary formula. A method supports expanded-gene biological interpretation only if the donor-bootstrap interval supports positive effect concordance, sign concordance is at least 80% among genes with measured nominal `p < 0.05`, calibration is not materially biased, and null resampling shows no excess discoveries. Retain full results even if no method passes; thresholds are interpretation gates, not filters for reporting.

**FAILURE INTERPRETATION**  
Strong expression reconstruction but weak or biased disease-effect concordance means imputed genes cannot support SCZ discovery claims; the manuscript should become a benchmarking paper with an explicit downstream-use boundary. A different winner after rerunning indicates pipeline/version instability that must be resolved before manuscript figures are trusted.

**EXPECTED OUTPUT**  
Canonical method/version/checksum table; verified donor/exclusion/fold manifest; exact model and transformation; measured-versus-imputed coefficient-concordance figure and table; donor-bootstrap intervals; null-QC figure; manuscript-ready result paragraph; and an evidence-backed update to [[02_Projects/GeneBridge/experiments-and-results]].

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 8/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Run the first measured-target AIVC context-value audit on GeneBridge

**SCIENTIFIC QUESTION**  
Does local multicellular environment improve prediction of measured held-out Xenium activity genes across unseen donors beyond cell identity and simple pooled-context summaries, and does the fitted model use context in a target-relevant way?

**WHY NOW**  
AIVC has no benchmark result. GeneBridge offers an immediately available, donor-structured engineering test of the outline's identity-plus-environment premise. CellAudit shows that input sensitivity is not useful contribution, while SpaFactor shows that simple pooled context may capture most apparent spatial benefit. This pilot can establish or falsify the need for complex attention without pretending to test perturbations, causality, aging, or AD.

**HYPOTHESIS**  
Cell-type-stratified local expression summaries will reduce measured held-out-gene error on unseen donors relative to identity-only ridge, and the benefit will disappear under support-matched context replacement or donor-preserving context shuffling.

**EXPERIMENT**  
Use only measured Xenium genes and the existing three held-out-gene folds. Split donors before normalization fitting, feature selection, module construction, hyperparameter tuning, or imputation. Exclude each focal cell from its neighborhood and predefine radii, cell-type strata, minimum-neighbor rules, and deployment-available covariates. Fit nested models under identical donor folds and tuning budgets: M0 identity-only ridge; M1 identity plus cell-type-stratified pooled context ridge; M2 the same inputs with a small residual MLP. For the frozen best context model, replace context with support-matched alternatives within cell type/layer/technical strata and quantify target-loss change. Do not use imputed targets, diagnosis labels, test-donor preprocessing, attention, a graph, or a conditional VAE.

**DATA REQUIRED**  
Measured Xenium expression; cell coordinates; cell-type and layer labels; donor/run/slide metadata; three observed/held-out gene manifests; QC/exclusion rules; and the locked 23-donor analysis cohort. Priority #2's donor and fold verification must be reused rather than recreated.

**MODEL / METHOD**  
Regularized multi-output regression for M0/M1 and one capacity-limited residual MLP for M2. Neighborhood features are training-defined, cell-type-stratified means at prespecified radii with focal-cell exclusion. Use grouped nested cross-validation by donor. Primary paired comparison is `ΔL_d = L_d(M0) - L_d(M1)` on measured held-out genes; estimate uncertainty by donor bootstrap. Frozen-checkpoint matched replacement tests fitted reliance, while refitted M0 versus M1 tests available predictive information.

**BASELINE**  
Global/training-fold gene mean; cell-type/layer mean; identity-only ridge; and identity plus unstratified pooled-neighborhood ridge. M1 must beat the strongest simple baseline before M2 or any future attention model is scientifically justified.

**METRIC**  
Primary: donor-averaged measured-target loss on held-out genes, reported as paired donor-level M1-versus-M0 difference. Secondary: per-gene Spearman correlation and RMSE; layer/cell-type stability; calibration; benefit across gene folds; matched-replacement loss gain; shuffled-context control; and sensitivity to neighborhood radius and neighbor count.

**SUCCESS CRITERION**  
Context passes only if M1 improves measured-target loss over M0 in at least four of five prespecified donor-held-out outer folds, the donor-bootstrap 95% interval for the paired improvement excludes zero, the gain is not reproduced by shuffled or support-mismatched context, and no single donor or layer explains the result. M2 is retained only if it improves over M1 under the same protected folds. Otherwise, simple identity or pooled context becomes the justified baseline and complex attention is not advanced.

**FAILURE INTERPRETATION**  
No M1 gain means this target and scale do not support the claimed environmental contribution. Gain under shuffled/replaced context indicates leakage, technical spatial autocorrelation, or proxy use. Internal gain confined to one layer/donor indicates limited transport rather than a universal representation. These outcomes are valuable boundary results but cannot support causal or perturbation claims.

**EXPECTED OUTPUT**  
Versioned data contract and configuration; donor/fold manifests and leakage checks; M0/M1/M2 predictions; donor-level paired-loss figure; replacement/shuffle audit; subgroup stability table; one experiment-registry entry in [[02_Projects/AIVC/experiments-and-results]]; and a clear advance/stop decision for hierarchical attention.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 7/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop expanding the architecture or collecting broad virtual-cell papers this week.** Do not spend time on GNN-versus-transformer design, graph priors, multimodal conditional VAEs, agentic execution layers, or portal work until Priority #3 demonstrates measured, leakage-resistant context value beyond pooled summaries and Priority #1 establishes an eligible NIA premise. These activities currently add complexity without resolving the scientific bottlenecks.

## Evidence used

- [[02_Projects/AIVC/current-state]]
- [[02_Projects/AIVC/methods]]
- [[02_Projects/AIVC/experiments-and-results]]
- [[02_Projects/AIVC/todo-and-next-actions]]
- [[02_Projects/GeneBridge/current-state]]
- [[02_Projects/GeneBridge/methods]]
- [[02_Projects/GeneBridge/datasets]]
- [[02_Projects/GeneBridge/experiments-and-results]]
- [[02_Projects/GeneBridge/todo-and-next-actions]]
- [[02_Projects/AIVC/literature/2026-09-25-literature-radar]]
- [[02_Projects/AIVC/reviews/2026-09-27-NIA-K99-study-section-review]]
- [[09_Planning/weekly-strategies/2026-09-21-AIVC-GeneBridge-weekly-strategy]]
- [[09_Planning/active-tasks]]
- [[09_Planning/unanswered-questions]]
