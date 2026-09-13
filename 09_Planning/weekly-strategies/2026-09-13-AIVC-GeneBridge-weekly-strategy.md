---
type: weekly-research-strategy
projects: [AIVC, GeneBridge]
week_of: 2026-09-13
status: active
created: 2026-09-13
last_updated: 2026-09-13
confidence: medium
---

# Weekly research strategy — AIVC / GeneBridge

## PI judgment

The program is blocked by two evidence gaps, not by a lack of model ideas: AIVC has no frozen estimand, dataset, or baseline result, while GeneBridge’s strongest results remain historical/unverified. This week should convert both into auditable evidence. Do not start a novel architecture.

There is a strategic contradiction to resolve explicitly: [[02_Projects/AIVC/goals|AIVC goals]] currently define SCZ as the disease focus, whereas the [[02_Projects/AIVC/reviews/2026-09-12-NIA-K99-study-section-review|latest NIA K99 review]] concludes that a competitive NIA application must be organized around aging/AD. For this week, retain SCZ/GeneBridge as publication work, preliminary evidence of spatial-genomics capability, and a possible secondary transport stress test—not as a co-equal NIA aim. This is a weekly strategy, not a permanent change to the canonical AIVC goal.

## #1 MUST DO — Freeze the aging/AD context-value benchmark

**SCIENTIFIC QUESTION**  
Do age- and AD-associated basal cellular states provide reproducible information about perturbation-response distributions beyond perturbation identity, cell type, and simple control-state summaries?

**WHY NOW**  
The latest NIH critique identifies the absence of one aging/AD question, one estimand, selected datasets, leakage-resistant splits, and a go/no-go threshold as the fatal K99 gap. The recent literature also shows that graph-versus-transformer comparisons are no longer a sufficient novelty claim. This benchmark must be fixed before architecture work.

**HYPOTHESIS**  
Age/AD context modifies the population distribution of perturbation responses, so a context-conditioned additive model will outperform an otherwise identical context-agnostic model on donors and perturbations excluded from training.

**EXPERIMENT**  
Produce and freeze a one-page benchmark specification, then run a data-feasibility audit. Select exactly one primary public aging/AD perturbation-response dataset and one independent validation dataset. Define the unit of analysis, control and perturbation populations, primary population-level response estimand, eligible cell types, donor/perturbation/context holdouts, covariates, leakage controls, negative controls, and one primary endpoint before fitting any new model. Create fold manifests from metadata and verify that every test donor and test perturbation is absent from training. If no public dataset jointly supports age/AD context, perturbation, and donor holdout, document that negative finding and choose the closest experimentally defensible system rather than relabeling cross-sectional AD tissue as perturbation data.

**DATA REQUIRED**  
Single-cell perturbation-response counts or normalized expression; matched controls; perturbation identity and dose/time; donor identifiers; age or aging condition; AD/pathology or disease-state annotation; cell type; batch; and an independent dataset with a compatible response gene/module space. Spatial context is optional for this first premise test and must not be inferred from unmatched tissue sections.

**MODEL / METHOD**  
Population-level change in expression distributions. Primary contrast: context-conditioned additive/ridge model versus the same model without age/AD context. Preprocessing, feature selection, normalization, and tuning are fit within training folds only. Use donor- and perturbation-grouped cross-validation; reserve the external dataset for final transport testing. Define uncertainty by donor bootstrap or conformal intervals where sample size permits.

**BASELINE**  
Control mean/no-change; perturbation-wise mean response; additive linear/ridge model without aging/AD context; nearest-neighbor response transfer. An established perturbation model may be added only after these four are working.

**METRIC**  
One prespecified primary metric: energy distance between predicted and observed perturbed populations. Secondary metrics: Pearson correlation of perturbation-induced mean change, DE-gene precision/recall, gene-module score error, and interval coverage/calibration.

**SUCCESS CRITERION**  
By week’s end: a frozen, versioned one-page premise/benchmark sheet; one primary and one external dataset with verified metadata/data access; executable fold manifests with zero donor or perturbation overlap; and a quantitative go/no-go rule fixed before model fitting. The scientific premise advances only if the context-conditioned baseline improves the primary metric by at least 10% relative to the strongest context-agnostic simple baseline across a majority of held-out folds and the direction replicates externally. Mark the 10% threshold as provisional until variance from the feasibility run supports a power calculation.

**FAILURE INTERPRETATION**  
If eligible data do not exist, the current NIA premise is not computationally testable without collaborator-generated data. If context adds no reproducible predictive value, do not force an age/spatial conditioning story; narrow the biological regime or reconsider NIA positioning.

**EXPECTED OUTPUT**  
`aging_AD_AIVC_premise_v1.md`, dataset eligibility table, data dictionary, fold manifests, leakage audit, and a frozen analysis configuration.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 10/10  
**PUBLICATION VALUE:** 8/10

## #2 SHOULD DO — Lock the GeneBridge evidence package and test downstream validity

**SCIENTIFIC QUESTION**  
Does the selected imputation method preserve donor-level SCZ effect estimates across cortical layers when genes are genuinely measured but masked, rather than merely scoring well on cell-level reconstruction metrics?

**WHY NOW**  
GeneBridge is the strongest existing publication asset and the clearest preliminary evidence of cohort-scale spatial-genomics execution, but the method table, donor list, DE formula, and reported DE counts are still marked unverified. Publication and K99 credibility require one canonical, reproducible result package.

**HYPOTHESIS**  
ENVI—or whichever method wins after verification—will preserve measured held-out-gene SCZ log-fold changes and effect directions better than nonspatial and naive baselines under fold-local masking, without generating excess null associations.

**EXPERIMENT**  
Rebuild the canonical six-method benchmark from current output files and verify the 24-donor reference list, 23-donor analysis cohort, exclusions, fold manifests, and method versions. For every held-out Xenium gene, aggregate both measured counts and fold-predicted values to the same 161 donor-by-layer units. Fit an identical prespecified layer-adjusted diagnosis model to measured and imputed values. Compare effect estimates, directions, rankings, discoveries, and null behavior. Include diagnosis-label permutation at the donor level. Keep donor-level, layer/domain-level, and cell-type claims separate.

**DATA REQUIRED**  
The 300 measured Xenium genes; three held-out-gene folds; predictions from the verified final method panel; donor, diagnosis, age, sex, layer, slide/run, QC, and exclusion metadata; current DE outputs; and the reference-paper gene/effect table restricted to a comparable gene universe and analysis unit.

**MODEL / METHOD**  
Donor-by-layer pseudobulk with repeated donor handling. Freeze one formula after checking estimability and donor/batch confounding; the candidate specification is `expression ~ Dx + Age + Sex + layer + run_or_slide`, with donor modeled as a block/random intercept. Apply the identical model to measured and imputed held-out genes. Do not include both run and slide unless the design matrix is full-rank. Record software, normalization, contrasts, multiple-testing universe, and exact formula.

**BASELINE**  
Measured held-out genes as ground truth; layer-specific gene mean; nonspatial imputation baseline; SpaGE; and every method in the verified final comparison panel. Do not assume the remembered six-method list is canonical until outputs confirm it.

**METRIC**  
Primary: Spearman correlation between measured and imputed diagnosis log-fold changes across held-out genes. Secondary: sign concordance, slope/intercept calibration, RMSE of log-fold change, overlap and precision/recall for measured DE genes at prespecified thresholds, rank stability, permutation false-positive rate, and concordance with the reference paper only after harmonizing gene universe and analysis unit.

**SUCCESS CRITERION**  
A single canonical results directory and signed-off table in which all values trace to files; complete donor accounting; one exact estimable DE formula; and measured-versus-imputed validation for all three folds. Biological downstream validity is supported if the selected method reaches Spearman rho ≥ 0.70 for diagnosis log-fold changes, ≥80% direction concordance among genes with measured nominal `p < 0.05`, and no excess discoveries under donor-level diagnosis permutations. Treat these thresholds as prespecified working criteria and report confidence intervals, not only pass/fail.

**FAILURE INTERPRETATION**  
Strong reconstruction with weak effect-size concordance means the method is unsuitable for disease DE claims and the paper should emphasize imputation benchmarking rather than expanded-gene discovery. Method rankings that change under canonical reruns indicate pipeline/version instability that must be fixed before manuscript figures.

**EXPECTED OUTPUT**  
Canonical method table, verified donor/exclusion manifest, exact DE specification, measured-versus-imputed concordance figure, permutation/null-QC figure, reference-paper concordance table, and an updated [[02_Projects/GeneBridge/experiments-and-results|GeneBridge results note]] backed by current files.

**COMPLEXITY:** MEDIUM  
**K99 VALUE:** 7/10  
**PUBLICATION VALUE:** 10/10

## #3 OPTIONAL — Execute the first AIVC baseline and context ablation

**SCIENTIFIC QUESTION**  
Under strict donor- and perturbation-held-out evaluation, is any learnable signal present beyond naive population-response transfer, and does aging/AD context improve it?

**WHY NOW**  
AIVC currently has no baseline result. One small, reproducible baseline would be more informative than further GNN/transformer design and would expose data, split, and metric failures early. This begins only after Priority #1 is frozen.

**HYPOTHESIS**  
A regularized additive model using basal state, perturbation identity/embedding, and age/AD context will outperform naive response transfer; removing context will produce a measurable loss on held-out donors and perturbations.

**EXPERIMENT**  
On the primary dataset selected in Priority #1, run control mean, perturbation mean, nearest-neighbor transfer, and regularized additive models on the frozen folds. Compare the additive model with and without aging/AD context. Do not train a GNN, transformer, flow, or graph-JEPA this week. Save predictions at the population level and run the complete frozen evaluation, including donor bootstrap uncertainty and a shuffled-context negative control.

**DATA REQUIRED**  
The quality-controlled primary dataset, frozen fold manifests, response-gene/module set, covariates, perturbation annotations, and the analysis configuration produced in Priority #1.

**MODEL / METHOD**  
Multi-output ridge or reduced-rank regression for mean response, plus empirical residual resampling for a simple population-distribution prediction. Nested tuning inside training donors only. Context ablation removes age/AD variables while keeping features, folds, capacity, and tuning budget matched.

**BASELINE**  
No-change/control mean; perturbation-wise mean; nearest-neighbor perturbation transfer; additive model without context.

**METRIC**  
Frozen primary energy distance; secondary mean-delta correlation, DE precision/recall, module-score error, perturbation discrimination, and 90% interval coverage.

**SUCCESS CRITERION**  
A fully reproducible end-to-end run with predictions and metrics for every frozen fold. Proceed to architecture development only if the additive model beats the strongest naive baseline and the context term gives the prespecified ≥10% primary-metric improvement across a majority of folds without improvement after context-label shuffling.

**FAILURE INTERPRETATION**  
If all models match naive baselines, the dataset/estimand may lack predictable signal. If shuffled context performs similarly, apparent context gain is leakage or confounding. Either result blocks complex model development until the design is repaired.

**EXPECTED OUTPUT**  
Versioned baseline code/configuration, fold-level metric table, context-ablation plot, calibration plot, failure log, and the first entry in the [[02_Projects/AIVC/experiments-and-results|AIVC experiment registry]].

**COMPLEXITY:** HIGH  
**K99 VALUE:** 9/10  
**PUBLICATION VALUE:** 9/10

## STOP / deprioritize

**Stop broad architecture comparison, paper accumulation, and “GNN versus transformer” design work this week.** It has low marginal scientific value before the biological question, population-level estimand, datasets, splits, simple baselines, and downstream GeneBridge validity are fixed. Resume architecture work only if Priority #3 establishes a real, leakage-resistant prediction gap that a more complex model could plausibly solve.

## Evidence used

- [[02_Projects/AIVC/current-state|AIVC current state]]
- [[02_Projects/AIVC/experiments-and-results|AIVC experiments/results]]
- [[02_Projects/AIVC/todo-and-next-actions|AIVC next actions]]
- [[02_Projects/GeneBridge/current-state|GeneBridge current state]]
- [[02_Projects/GeneBridge/experiments-and-results|GeneBridge experiments/results]]
- [[02_Projects/GeneBridge/todo-and-next-actions|GeneBridge next actions]]
- [[05_Learning/important-papers|AIVC literature radar — 2026-09-12]]
- [[02_Projects/AIVC/reviews/2026-09-12-NIA-K99-study-section-review|NIA K99 reviewer critique — 2026-09-12]]
- [[09_Planning/active-tasks|Active tasks]]
- [[09_Planning/unanswered-questions|Unanswered questions]]
