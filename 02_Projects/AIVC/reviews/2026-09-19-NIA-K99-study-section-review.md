---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-09-19
last_updated: 2026-09-19
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-09-13-NIA-K99-study-section-review]]"
---

# AIVC as a potential NIA K99/R00 — skeptical study-section review

## Bottom line

This is still not an application-ready NIA K99/R00. Since the [[02_Projects/AIVC/reviews/2026-09-13-NIA-K99-study-section-review|September 13 review]], the vault documents no completed premise sheet, aging/AD perturbation dataset audit, fold manifest, leakage audit, baseline, context ablation, external validation, prospective experiment, GeneBridge verification package, mentor-team plan, or independence agreement. The exact action identified as the prior review’s number-one priority remains open.

The scientific concept is plausible but unsubstantiated: age- and AD-associated cellular states may alter perturbation response, but no selected system or result shows that this effect exists, is identifiable apart from donor and dataset structure, or is large enough to support prediction. The empirical record remains a schizophrenia spatial-imputation project, not an aging/AD perturbation program.

The literature moved while the project did not. Recent papers now cover transport of perturbational scaffolds into target populations, multiscale action-conditioned world models, knowledge-enhanced single-cell transformers, spatial representation learning, decomposed population-response modeling, and direct optimization of population-level biological metrics. CellRFT in particular shows that optimizing evaluation metrics can improve some endpoints while degrading perturbation discrimination. This raises the standard for innovation and makes sealed test contexts, protected metrics, and biological validation mandatory. It does not supply preliminary data for this proposal.

A study section would likely conclude that the candidate has relevant computational potential but has not established an NIA-specific premise, feasible data structure, protected mentored-training need, or credible path to prospective validation. The likely Overall Impact remains **8**.

## Change since the previous review

### What changed

1. The [[05_Learning/important-papers|literature memory]] added six relevant papers after the prior review, including work on target-population causal re-estimation, multiscale action-conditioned models, knowledge supervision, spatial representation, and reinforcement fine-tuning against population-level metrics.
2. The latest literature makes several broad innovation claims less defensible and adds a new risk: metric optimization can reward benchmark-specific behavior while harming biological discrimination.
3. The latest supplied NIA/K99 funding-radar outputs were silent. No new NOFO, eligibility rule, deadline, or NIA priority is therefore treated as established in this review.

### What did not change

1. [[02_Projects/AIVC/experiments-and-results|AIVC experiments and results]] still documents no benchmark or result.
2. [[02_Projects/AIVC/datasets|AIVC datasets]] still names no canonical primary or external aging/AD perturbation dataset.
3. `aging_AD_AIVC_premise_v1.md`, the eligibility table, data dictionary, fold manifests, leakage audit, and frozen analysis configuration are not documented.
4. The canonical [[02_Projects/AIVC/goals|AIVC goal]] remains SCZ-focused; the aging/AD direction remains a weekly K99 strategy rather than an approved scientific program with evidence.
5. GeneBridge’s method ranking, full donor inventory, exact DE specification, and disease-effect results remain marked for verification.
6. No aging/AD mentor, perturbation-experiment mentor, validation collaborator, facility access, or letter of commitment is documented.
7. No career-development plan or written boundary from Jian Hu’s spatial-integration program is documented.

**Comparison judgment: STAGNANT.** Planning is no more complete than it was on September 13, no scientific premise has been tested, and the competitive novelty bar has risen.

## Evidence reviewed and boundaries

Reviewed:

- AIVC overview, current state, goals, datasets, methods, decisions, experiments/results, and next actions.
- GeneBridge overview, current state, datasets, methods, experiments/results, and next actions.
- Research overview, active tasks, unanswered questions, and the September 13 weekly strategy.
- [[05_Learning/important-papers|AIVC literature radar]] through September 18, including CellRFT.
- [[02_Projects/AIVC/reviews/2026-09-13-NIA-K99-study-section-review|Previous NIA K99 review]].
- Identity/career and collaborator notes.
- Latest supplied NIA/K99 funding-radar outputs, both silent.

The requested folders `05_Papers_and_Learning/` and `09_Open_Loops/` do not exist in the canonical vault. Their apparent equivalents, `05_Learning/` and `09_Planning/`, were reviewed. No missing aim, result, collaborator, dataset access, or commitment was inferred. Historical or explicitly unverified GeneBridge values are not treated as final preliminary results.

# NIH criterion review

## SIGNIFICANCE — score 7

### Why should NIA care?

NIA could care if the project demonstrates a specific and consequential failure of current perturbation-response models in aged or AD-relevant neural biology. A successful program could establish when cellular response cannot be transported from young, pooled, cell-line, or context-poor systems into aged human neural or glial states, and could improve target prioritization by predicting context-specific benefit, resistance, or toxicity.

That significance must be biological, not merely algorithmic. The proposal needs to connect prediction to one aging or AD process—such as microglial inflammatory response, proteostatic stress, synaptic resilience, lysosomal dysfunction, senescence, metabolic stress, or another explicitly selected mechanism—and to one measurable functional endpoint. “Better virtual-cell prediction” by itself is not an NIA health problem.

### Is the aging/AD/neurodegeneration relationship convincing?

No. It remains strategic rather than empirical.

- No aging/AD perturbation system has been selected.
- No eligible primary/external dataset pair has been verified.
- No cell population, perturbation class, disease stage, response module, or functional endpoint is fixed.
- No result shows an age-by-perturbation or AD-context-by-perturbation effect.
- No analysis separates age/AD state from donor, cohort, platform, batch, tissue quality, or cell-composition effects.
- No prospective aging/AD validation system or collaborator is documented.
- Cross-sectional postmortem disease expression cannot substitute for a perturbation-response experiment.

Until the context effect is observed under a defensible design and replicated externally, NIA relevance is an asserted application area rather than the scientific premise.

### Does SCZ add breadth or make the proposal unfocused?

SCZ makes the application unfocused if presented as a co-equal disease aim. It also risks revealing that the method preceded the NIA question.

SCZ/GeneBridge can serve only three bounded functions:

1. establish the candidate’s ability to analyze cohort-scale human cortical spatial data;
2. provide a later negative-control or transport stress test; and
3. help distinguish aging/AD-specific response programs from generic cortical disease signals.

GeneBridge should not be presented as aging preliminary data, and age adjustment in an SCZ DE model is not aging biology. An NIA K99 should not include a separate SCZ aim unless the institute-specific rationale is unusually strong and the aging program is already established.

## INNOVATION — score 6

### What could be genuinely novel?

The defensible innovation is not a new backbone. It is a linked biological and statistical program that:

- defines perturbation response at the population-distribution level for destructive single-cell assays;
- estimates whether age/AD basal state reproducibly modifies response beyond perturbation identity, cell type, donor, and control-state summaries;
- separates basal context, perturbation-specific effects, and residual heterogeneity;
- transports predictions across donors and datasets with calibrated uncertainty;
- protects evaluation from leakage and metric overfitting; and
- validates selected predictions with both transcriptional modules and one aging/AD-relevant functional phenotype.

A stronger innovation claim would be: **identify the boundary conditions under which perturbation knowledge can be transported into aged human neural contexts, then build a calibrated population-response model that respects those boundaries.**

### What already exists?

The current literature sharply limits novelty claims:

- PopPert already frames perturbation prediction at the population joint-distribution level.
- DeMixPert already decomposes basal, perturbation-specific, and stochastic response.
- GeneGeoFlow already separates structural gene geometry from perturbation-conditioned dynamics.
- BioM-JEPA already predicts graph-connected gene-block representations.
- VCBench already emphasizes unseen contexts, unseen perturbations, and cross-dataset transport.
- Recent causal-path work already proposes transferring a perturbational ordering scaffold and re-estimating edges/effects in the target donor population.
- The Immune World Model already presents hierarchical action-conditioned transitions across cell, tissue, and patient scales.
- scKITE already uses regulatory and annotation supervision during single-cell Transformer pretraining.
- HyCLoST already combines spatial image and expression representations in hierarchical geometry.
- CellRFT already fine-tunes perturbation generators against non-differentiable population-level biological metrics and demonstrates metric conflicts.

These papers do not solve the aging/AD problem, but they remove novelty from generic claims about population modeling, graph-informed transformers, multiscale world models, context conditioning, or biological-metric optimization.

### What sounds incremental?

- comparing GNN, Transformer, and hybrid architectures;
- using genes or modules as tokens;
- adding STRING, GO, coexpression, or inferred-GRN edges;
- appending age, disease, or spatial embeddings as covariates;
- applying a foundation model to an AD dataset;
- adding a reinforcement-learning stage to optimize benchmark metrics;
- imputation followed by DE without effect-preservation validation;
- calling cross-dataset prediction a “world model” without an identified transition process;
- treating an external perturbational network as valid unchanged in aged human tissue.

### Which claims would reviewers challenge?

- **“Causal”:** no identification strategy, intervention design, or defensible transport assumptions are fixed.
- **“Mechanistic”:** expression prediction and attention/graph weights are not mechanisms.
- **“Virtual cell”:** a condition-level transcriptomic predictor is narrower than a simulator of cell state and function.
- **“Aging-aware”:** including age or AD labels does not prove effect modification.
- **“Spatially informed”:** unmatched postmortem spatial data do not identify the niche of an independent perturbation experiment.
- **“Generalizable”:** donor leakage, target-embedding leakage, preprocessing leakage, and dataset confounding remain unaddressed.
- **“Biologically aligned”:** directly optimizing DE or discrimination metrics can overfit the benchmark and trade one biological property for another.
- **“Therapeutic”:** no intervention, rescue phenotype, efficacy readout, or toxicity endpoint exists.
- **“Independent”:** the empirical program remains close to the mentor’s spatial-integration domain.

## CENTRAL HYPOTHESIS

### Current state

No central hypothesis is frozen in the canonical AIVC goals. The weekly strategy contains a testable premise, but it has not been tied to a verified system or converted into a completed premise artifact.

### One strong central hypothesis

**Age- and AD-associated basal states in a defined human neural cell population reproducibly modify the population distribution of responses to a defined perturbation class; therefore, a model that separates basal context, perturbation-specific effects, and residual heterogeneity will improve held-out-donor and external-dataset prediction and uncertainty calibration over an otherwise matched context-agnostic model, and its highest-confidence response modules will predict a prespecified aging/AD-relevant functional phenotype.**

This is testable only after replacing each “defined” placeholder with one actual system. It is falsified if context adds no reproducible value, if the gain disappears with donor/batch adjustment or context-label shuffling, if it fails external transport, or if predicted modules do not track the functional endpoint.

# SPECIFIC AIMS

No finalized Specific Aims page exists. The following structure is defensible only after Aim 1 feasibility data exist.

## Aim 1 — Establish whether aging/AD context modifies perturbation response

Select one neural or glial population, one aging/AD context, one perturbation class, and one population-level estimand. Audit one primary and one external dataset. Compare matched context-conditioned and context-agnostic additive models against no-change, perturbation-mean, and nearest-neighbor baselines under donor-, perturbation-, and dataset-held-out evaluation.

- **Output:** eligibility table, data dictionary, frozen folds, leakage audit, estimated context effect with donor-level uncertainty, and external replication.
- **Measurable:** one primary metric, one primary contrast, confidence interval, context-shuffle control, and prespecified go/no-go rule.
- **Failure resilience:** a negative result establishes a boundary condition but invalidates the current central premise. The proposal must state how the biological scope changes rather than proceeding unchanged.

## Aim 2 — Develop a transportable, decomposed population-response model

Model basal context, perturbation-specific response, and residual heterogeneity. Compare against matched-capacity simple models and established perturbation methods. Keep structural priors separate from learned perturbation dynamics. If any metric-based fine-tuning is used, optimize only within training/validation donors and preserve protected test metrics and contexts.

- **Output:** calibrated population-response predictions and a map of where context helps or fails across perturbations and donors.
- **Measurable:** frozen energy-distance or equivalent primary endpoint, response-effect/module metrics, perturbation discrimination, calibration/coverage, and computational cost.
- **Failure resilience:** retain the strongest simple model and complete the context-boundary analyses even if the novel architecture fails. Aim 2 should not depend on a complex model winning.

## Aim 3 — Validate transportability and biological relevance prospectively

Without retuning, test the selected model on the external dataset. Prospectively measure a small number of prespecified perturbations in one aging/AD-relevant neural or glial system. Evaluate response direction, modules, heterogeneity, uncertainty, and one functional phenotype. Include model-selected and baseline-selected predictions so the experiment does not depend on Aim 2 superiority.

- **Output:** external transport result and prospective validation of a limited prediction set.
- **Measurable:** prespecified effect directions, module scores, functional endpoint, calibration, and negative controls.
- **Failure resilience:** the experiment can compare simple and complex predictors even if the central model underperforms; failed predictions must be reported and used to delimit transportability.

## Aim structure judgment

- **Logical connection:** potentially strong if every aim uses one biological question and response estimand.
- **Independence:** inadequate unless Aims 2 and 3 include baseline-derived analyses that proceed after a failed architecture. A failed context effect in Aim 1 still undermines the central hypothesis.
- **Feasibility:** currently unestablished because the data pair, sample structure, computational benchmark, experimental system, collaborators, and budget are unknown.
- **Measurability:** potentially good; the planning notes already propose grouped folds, a primary endpoint, negative controls, and a go/no-go threshold.
- **Resilience:** acceptable for model failure, not for premise failure. The application should distinguish these explicitly.

## APPROACH — score 8

### Modeling assumptions

1. Age/AD context is measured independently enough from cohort and technical structure to estimate effect modification.
2. Perturbations repeat across enough donors and contexts to identify context-by-perturbation effects.
3. Basal state adds predictive information beyond cell type, perturbation identity, and control summaries.
4. Public experimental systems are relevant to aged human neural biology.
5. Population distributions are the appropriate estimand; cell-to-cell counterfactual maps are not observed in destructive assays.
6. Basal, perturbation-specific, and residual components are sufficiently identifiable to be scientifically interpretable.
7. Dataset/platform shifts can be separated from biological context shifts.
8. Any graph or prior improves prediction without being misrepresented as a causal intervention network.
9. Metrics used for training do not become invalidated as unbiased evaluation endpoints.
10. Transcriptional response is meaningfully linked to the selected functional phenotype.

These assumptions are not yet tested.

### Data limitations

- No canonical AIVC dataset exists.
- No dataset is documented as jointly containing perturbation, matched control, donor, age/aging or AD context, relevant neural cell type, dose/time, and adequate replication.
- No compatible external dataset is identified.
- Common perturbation resources emphasize cell lines, young or pooled systems, narrow times, and non-neural contexts.
- If AD and control contexts come from different datasets, diagnosis and dataset are not separable.
- GeneBridge has spatial resolution and donor structure but no perturbation response and only a targeted 300-gene Xenium panel.
- GeneBridge’s complete 24-donor inventory is unresolved in the notes, and its 23-donor downstream results remain historical or unverified.
- Rare-state responses may be lost in global population metrics.
- No sample-size or detectable-effect calculation exists.

### Confounding and identification

“Aging/AD context” may proxy donor cohort, platform, batch, tissue degradation, postmortem interval, brain pH, library quality, cell composition, region/layer, medication, disease severity, survivor effects, ancestry, sex, or exposure history. A valid design needs overlap: the same perturbations across multiple donors and contexts within a structure that does not perfectly confound context with dataset.

The analysis plan must prespecify the estimand and treatment of age, diagnosis/pathology, sex, ancestry, postmortem interval, tissue/RNA quality, medication, smoking/substance exposure, cause of death, dose, time, cell type/state, region/layer, and repeated donor measurements. It must not adjust for mediators without stating the target estimand.

External perturbational networks can constrain candidate structure, but their direct effects should be re-estimated in the target population. Assuming an entire cell-line GRN transfers unchanged into aged human neural cells is not defensible.

### Leakage and benchmark overfitting

Major risks include:

- cell-level splits retaining the same donor across train and test;
- close perturbation analogues leaking through target embeddings or pretrained representations;
- normalization, feature selection, batch correction, graph construction, module discovery, or retrieval databases fit before splitting;
- test labels entering biological-knowledge prompts or auxiliary supervision;
- tuning on the external dataset;
- test-donor spatial neighbors or matched modalities entering training;
- selecting response genes or metrics after seeing held-out outcomes;
- diagnosis-correlated imputation inflating DE;
- reporting the best cell type, perturbation subset, or metric after model comparison;
- using the same biological metrics for reinforcement fine-tuning and final evidence;
- unfair graph/spatial ablations that change degree, density, or capacity.

Every split should be a versioned manifest with automated zero-overlap checks. Tuning must be nested within training donors. Any CellRFT-like alignment should use development metrics only; final claims require untouched donors, perturbations, datasets, and preferably a functional endpoint not used as a reward.

### Statistical weaknesses

- Cells are not independent biological replicates; donors or experimental units must drive uncertainty.
- No power or precision analysis exists for context-by-perturbation interactions.
- The provisional 10% improvement threshold is not justified by observed variance or clinical/biological importance.
- Energy distance can be dominated by abundant states and global shifts.
- Mean-delta correlation can conceal wrong DE direction, rare-state failure, or poor calibration.
- Multiplicity spans genes, modules, cell types, perturbations, contexts, models, and metrics.
- Hyperparameter and model-selection uncertainty are ignored.
- Calibration cannot be claimed from many cells but few donors.
- Cross-dataset gene/module compatibility is undefined.
- External replication criteria and a rule for incompatible assays are missing.
- GeneBridge’s repeated-donor DE model and imputation-uncertainty propagation remain unfrozen.

The statistical plan needs one inferential unit, primary contrast, primary endpoint, grouped resampling scheme, multiplicity strategy, missing-data rule, confidence intervals, calibration definition, and failed-transport interpretation.

### Biological validation gaps

No prospective system, collaborator, assay, perturbation set, sample size, endpoint, or resource commitment is documented. A credible ladder is:

1. fold-local internal validation across held-out donors and perturbations;
2. context-shuffling, label-permutation, and leakage-negative controls;
3. external-dataset transport without retuning;
4. validation of perturbation effects and modules, not only global similarity;
5. prospective testing in an aging/AD-relevant neural or glial system; and
6. one functional phenotype tied to the biological question.

Without external transport and prospective validation, claims must remain computational. Without a functional phenotype, “mechanistic,” “therapeutic,” and “rescue” claims are unsupported.

### Generalization

The decisive claim should be transport across donors and datasets within one aging/AD question. Generalization across unrelated cell lines is insufficient. Cross-disease transport to SCZ can be secondary only after the NIA premise is established. Failures are interpretable only if the design distinguishes biological context specificity from platform, cohort, and assay incompatibility.

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. **Relevant computational background:** documented work in computational genomics, statistical genetics, spatial transcriptomics, and human DLPFC.
2. **Cohort-scale spatial infrastructure:** a working 23-donor Xenium SCZ/control downstream cohort with seven layers and 161 donor-by-layer units.
3. **Held-out-gene benchmark design:** 300 measured genes divided into three folds balanced by expression, dispersion, detection, and Moran’s I.
4. **Metadata recovery and downstream pipeline:** recovered slide/run fields, donor-layer pseudobulk, and a layer-adjusted DE workflow.
5. **Historical imputation and DE results:** ENVI is recorded as leading and historical DE counts are recorded, but both are explicitly marked for verification and cannot be treated as locked evidence.
6. **Current methodological map:** the literature notes identify realistic constraints around population estimands, decomposition, structural priors, target-population re-estimation, transport evaluation, hierarchical modeling, and metric conflicts.
7. **A rigorous proposed benchmark logic:** grouped holdouts, simple baselines, context ablation, negative controls, external transport, and a provisional go/no-go rule are written as plans.

This supports feasibility for computational spatial-genomics work. It does not support aging/AD biology, perturbation prediction, virtual-cell validity, causality, mechanism, or prospective experimental execution.

## WHAT IS STILL MISSING

1. One selected aging/AD biological question, neural cell population, perturbation class, and functional endpoint.
2. A verified primary perturbation dataset and independent external dataset with usable donor/context overlap.
3. A frozen premise sheet, eligibility table, data dictionary, fold manifests, leakage audit, and analysis configuration.
4. Any AIVC baseline, context ablation, or uncertainty result.
5. Evidence that aging/AD context adds predictive information after donor and technical control.
6. Data-supported power/precision and success thresholds.
7. External replication without retuning.
8. Prospective aging/AD-relevant perturbation validation.
9. A canonical GeneBridge method table, complete donor/exclusion manifest, exact DE model, and measured-versus-imputed disease-effect concordance.
10. Propagation of imputation uncertainty into downstream inference.
11. A named aging/AD mentor, experimental perturbation mentor, and, if needed, causal/probabilistic methods mentor.
12. Data, facility, and validation commitments.
13. A training plan with activities, milestones, evaluation, and transition criteria.
14. A written scientific and resource boundary from Jian Hu’s program.
15. Evidence of ownership that can persist into the R00 institution.

# CAREER DEVELOPMENT — weakness under Investigator

## What does the candidate still need to learn?

A defensible K99 training gap includes:

- aging, AD, and neurodegeneration biology;
- neural/glial perturbation systems and experimental design;
- causal effect modification and transportability;
- probabilistic population modeling and calibrated uncertainty;
- grouped and cross-dataset single-cell benchmarking;
- prospective validation and functional assay design; and
- grantsmanship, team leadership, and management of experimental collaborations.

“Learn GNNs and Transformers” is not an adequate K99 training need. It is generic technical development and does not explain why protected mentored time is required.

## Why is a K99 needed?

The plausible transition is from human cortical spatial/statistical genomics in SCZ to an independent program in context-dependent perturbation response in aging/AD. The K99 would provide biological, experimental, causal/transport, and prospective-validation training not documented in the current record.

That rationale remains unwritten. Without named mentors, training activities, measurable milestones, and evidence that these capabilities are unavailable in the current arrangement, reviewers may see a methods pilot rather than a mentored career transition.

## How must training differ from the mentor’s program?

Jian Hu’s documented program centers on statistical integration of multi-view, multi-section, and multi-sample spatial transcriptomics. GeneBridge overlaps that area closely. The candidate’s distinct ownership should center on:

- intervention and perturbation-response estimands;
- age/disease context-effect identification;
- population-distribution prediction;
- donor/dataset transport and calibrated uncertainty; and
- prospective aging/AD experimental validation.

The mentor team should add documented expertise in aging/AD biology and neural perturbation experiments. A quantitative co-mentor may be needed if causal transport and probabilistic modeling are central. The application must state what intellectual property, code, datasets, collaborations, and scientific questions the candidate can take to the R00 phase.

## How should K99 and R00 differ?

- **K99:** establish the aging/AD context-value premise, complete targeted training, build and benchmark the first decomposed population-response model, and prospectively test a small number of predictions using mentor-supported resources.
- **R00:** create an independent perturbation-and-modeling program across aged human neural cell states and tissue contexts, with open transport benchmarks, experimentally generated data, and iterative prediction-validation cycles.

Transition milestones should include: frozen benchmark; leakage-resistant baseline; quantified context effect or principled negative result; external transport; calibrated uncertainty; at least one prospectively tested prediction; a first-author output; a documented independent data/validation pipeline; and resources not controlled exclusively by the primary mentor.

# INDEPENDENCE

The current record does not yet look unmistakably like the candidate’s future laboratory. GeneBridge is useful but close to the mentor’s spatial-integration program. AIVC is broad enough to sound generic, and no unique dataset, experimental partnership, or validated framework establishes ownership.

The defensible independent niche is:

**transportable, uncertainty-aware population perturbation modeling under age, disease, donor, and tissue-context shifts, coupled to prospective neural validation.**

The candidate must own the biological question, estimand, benchmark, transport assumptions, model, experimental prioritization, and validation cycle. Connecting foundation-model embeddings to spatial features would not establish independence.

### Natural funding trajectory

- **R01:** generate and prospectively test context-dependent perturbation maps in aging/AD across donors, cell states, and experimental systems.
- **NSF CAREER:** develop general transportable and uncertainty-aware virtual-cell methods, open benchmarks, and computational training infrastructure.
- **Independent faculty program:** integrate statistical genomics, population-response modeling, and durable experimental partnerships in iterative prediction-validation studies.

This trajectory is credible only if the R00 is not dependent on the current mentor’s unpublished data, personnel, or core scientific aims.

# NIH-style scores

| Criterion | Score | Reviewer rationale |
|---|---:|---|
| **Overall Impact** | **8** | Potentially important direction, but no NIA-specific premise, eligible dataset pair, AIVC result, functional endpoint, external replication, prospective validation, career plan, or independence structure is documented. |
| **Significance** | **7** | Context-dependent response in aging/AD could matter, but the biological problem and context effect remain hypothetical. |
| **Investigator** | **6** | Relevant computational/spatial experience is documented; aging/AD, perturbation modeling, prospective experimentation, and independent ownership are not. The vault lacks a full biosketch/publication record, limiting confidence in this score. |
| **Innovation** | **6** | The integrated context-identification and transport framework could be distinctive, but most component methods now exist and no result differentiates this program. |
| **Approach** | **8** | The project lacks a viable data design, power rationale, finalized aims, baseline, external transport, experimental system, and validation result; confounding and benchmark overfitting could be fatal. |
| **Environment** | **5** | Emory and the current mentor plausibly provide strong genomics support, but no aging/AD mentor, perturbation collaborator, facility/access plan, or commitment is documented. |

# Required summary

## TOP 3 STRENGTHS

1. Relevant computational and spatial-genomics infrastructure for donor-structured human cortical analysis.
2. A sound proposed rigor framework: population-level estimand, grouped holdouts, simple baselines, context ablation, leakage controls, external transport, and uncertainty.
3. A potentially independent scientific niche at the intersection of statistical genomics, transportability, and perturbation response—if it becomes anchored in one aging/AD system and prospective validation.

## TOP 3 MAJOR RISKS

1. **Fatal NIA-premise risk:** no selected aging/AD perturbation system and no evidence that aging/AD context modifies response.
2. **Approach and credibility risk:** no AIVC result, eligible dataset pair, leakage audit, external replication, prospective experiment, or functional endpoint; direct optimization of benchmark metrics could further overstate performance.
3. **Career and independence risk:** the empirical base remains unverified SCZ spatial-imputation work close to the mentor’s domain, with no documented aging/AD training team or portable R00 program.

## TOP 3 EXPERIMENTS TO PRIORITIZE

### 1. Aging/AD perturbation-data feasibility audit plus context-value baseline

Select one primary and one independent system. Verify donor, perturbation, dose/time, context, cell type, batch, and response-space compatibility. Freeze grouped splits. Run no-change, perturbation-mean, nearest-neighbor, and additive/ridge baselines with and without aging/AD context. Include context shuffling, donor bootstrap uncertainty, and an external no-retuning test. This decides whether the NIA premise exists.

### 2. GeneBridge measured-versus-imputed disease-effect preservation

Lock the donor list, fold manifests, model versions, and repeated-donor DE specification. For every genuinely measured but held-out Xenium gene, compare measured and imputed SCZ log-fold changes on identical donor-layer units. Quantify effect correlation, sign concordance, calibration, RMSE, discovery behavior, and donor-level permutation false positives. This can establish rigorous computational competence, not aging or perturbation biology.

### 3. Small prospective aging/AD-relevant perturbation experiment

With a named collaborator, test a limited perturbation set in one neural or glial aging/AD-relevant system. Prespecify response modules, distributional metrics, uncertainty, negative controls, and one functional phenotype. Compare predictions from the strongest simple baseline and any complex model. Do not wait for a grand virtual-cell architecture.

## ONE STRONG CENTRAL HYPOTHESIS

Age- and AD-associated basal states in a defined human neural cell population reproducibly modify population-level responses to a defined perturbation class; therefore, separating basal context, perturbation-specific effects, and residual heterogeneity will improve held-out-donor and external-dataset prediction and calibration over a matched context-agnostic model, while identifying response modules that predict a prespecified aging/AD-relevant functional phenotype.

## ONE-SENTENCE FUTURE-LAB VISION

My laboratory will build and experimentally test transportable, uncertainty-aware models that predict how aging human neural cell populations respond to genetic and pharmacologic perturbations across donors, disease states, and tissue contexts.

# Comparison with the previous review

## Status: STAGNANT

The September 13 review assigned Overall Impact 8 and identified the absent aging/AD premise, dataset pair, baseline, validation access, career plan, and independence structure as foundational weaknesses. Every one of those gaps remains documented as open. The new literature improves awareness but not preparedness; it narrows available novelty claims and introduces stronger concerns about metric optimization and benchmark overfitting. No evidence warrants a better score, and the lack of progress over the review interval does not yet justify a worse score. Overall Impact remains **8**.

# Number-one action this week

**Complete and freeze `aging_AD_AIVC_premise_v1.md` from verified metadata for one primary and one independent dataset, specifying one aging/AD question, one cell population, one perturbation class, one population-level estimand, executable donor/perturbation-held-out fold manifests, four simple baselines, one protected primary metric, shuffled-context controls, and a variance-informed go/no-go rule. If no eligible dataset pair exists, document that negative result and secure a collaborator-generated perturbation system before doing further architecture work.**
