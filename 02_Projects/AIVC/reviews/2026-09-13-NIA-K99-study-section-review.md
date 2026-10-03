---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-09-13
last_updated: 2026-09-13
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-09-12-NIA-K99-study-section-review]]"
---

# AIVC as a potential NIA K99/R00 — skeptical study-section review

## Bottom line

This remains an early research-program concept, not an application-ready NIA K99/R00. The planning is more disciplined than in the previous review: the notes now identify a population-level perturbation-response estimand, donor/perturbation/context holdouts, simple baselines, a provisional go/no-go rule, and the need to make aging/AD the organizing NIA question. None of those planning decisions has yet produced scientific evidence.

The fatal weakness is unchanged: there is no selected aging/AD perturbation system, verified primary and external dataset pair, AIVC baseline, context-ablation result, aging/AD biological endpoint, or prospective validation plan. The only documented empirical foundation is GeneBridge, an SCZ spatial-imputation project whose key method ranking, donor inventory, differential-expression model, and disease results remain marked for verification. That establishes relevant computational experience but not the premise of an aging virtual cell.

A study section would likely regard the project as high-risk methods development seeking an NIA home before establishing that aging or AD meaningfully changes perturbation response. The application should not be submitted until the context-value premise survives a leakage-resistant feasibility test and the candidate has a credible aging/AD and experimental mentor structure.

## Change since the previous review

### What improved

1. [[02_Projects/AIVC/important-decisions|AIVC decisions]] now require the biological question, population-level estimand, datasets, splits, baselines, and go/no-go rule to be frozen before architecture development.
2. [[09_Planning/weekly-strategies/2026-09-13-AIVC-GeneBridge-weekly-strategy|The weekly strategy]] specifies a falsifiable first premise test: compare matched context-conditioned and context-agnostic additive models under held-out donors and perturbations, using energy distance as the primary endpoint and shuffled-context controls.
3. The notes explicitly distinguish the NIA-facing aging/AD program from SCZ/GeneBridge and prohibit relabeling SCZ work as aging research.

### What did not improve

1. No premise sheet, dataset eligibility table, data dictionary, fold manifest, or leakage audit is documented.
2. No AIVC experiment has been run; [[02_Projects/AIVC/experiments-and-results|the experiment note]] still contains no benchmark or result.
3. GeneBridge findings remain historical or unverified rather than a locked preliminary-data package.
4. No aging/AD biological collaborator, perturbation collaborator, training plan, facility access, or letter of commitment is documented.
5. The latest supplied NIA/K99 funding-radar output reported no new opportunity or mechanism change; no current NOFO-specific requirement is therefore treated as established here.

**Comparison judgment:** review preparedness is improving, but the evidentiary status is **STAGNANT**.

## Evidence reviewed and boundaries

- AIVC overview, state, goals, methods, datasets, experiments/results, decisions, and next actions.
- GeneBridge overview, state, goals, methods, datasets, experiments/results, decisions, and next actions.
- Research overview and scientific interests.
- [[05_Learning/important-papers|AIVC literature radar — 2026-09-12]].
- Active tasks, unanswered questions, future plans, and the 2026-09-13 weekly research strategy.
- [[00_Profile/identity-and-career|Identity and career]], [[00_Profile/collaborators-and-roles|collaborators and roles]], and [[07_People/important-collaborators|important collaborators]].
- [[02_Projects/AIVC/reviews/2026-09-12-NIA-K99-study-section-review|Previous NIA K99 review]].
- Latest supplied NIA/K99 funding-radar output, which was silent.

The requested folders `05_Papers_and_Learning/` and `09_Open_Loops/` are not present in the canonical vault. Their apparent current equivalents, `05_Learning/` and `09_Planning/`, were reviewed. No missing experiment, aim, result, collaborator, or access commitment was inferred.

# NIH criterion review

## SIGNIFICANCE — score 7

### Why should NIA care?

NIA could care about a rigorously demonstrated failure of perturbation-response models under aging and AD context shifts. A model that predicts which neural or glial populations respond differently because of age- or AD-associated basal state could eventually support target prioritization, resilience studies, or intervention design. That would address a recognizable barrier: most perturbation models are trained in cell lines, young systems, pooled donors, or simplified contexts and may not transport to aged human biology.

The present notes do not demonstrate that barrier in an aging/AD system. They assert a plausible context-dependence problem but provide no data showing that age, AD state, or an aging-relevant niche modifies perturbation response after donor, cell-type, batch, and technical factors are controlled. Until that interaction is observed and replicated, the project is a methods hypothesis rather than an NIA-significant biological premise.

### Is the relationship to aging, AD, or neurodegeneration convincing?

No. It is currently strategic rather than empirical.

- The canonical AIVC goal remains disease-relevant virtual-cell modeling for SCZ.
- No aging/AD cohort or perturbation dataset is selected.
- No neuropathology, cognitive, resilience, senescence, inflammatory, proteostatic, synaptic, metabolic, or neurodegenerative endpoint is selected.
- No age-dependent or AD-dependent response result exists.
- GeneBridge is a cross-sectional SCZ spatial-transcriptomics/imputation study, not a perturbation experiment.
- Age as a covariate in an SCZ differential-expression model is not evidence about aging biology.
- Spatial context has not been linked to perturbation response in matched tissue or experimental systems.

The proposal needs one defined biological failure mode in aging/AD—not a list of diseases, model classes, and modalities.

### Does SCZ add useful breadth or make the proposal unfocused?

As a co-equal disease program, SCZ makes an NIA application unfocused. It also creates the appearance that the institute was chosen after the method.

SCZ can contribute only in bounded roles:

1. evidence that the candidate can execute cohort-scale human cortical spatial analyses;
2. a secondary transport stress test after the aging/AD premise is established; or
3. a contrast for distinguishing aging/AD-specific response programs from generic cortical disease programs.

SCZ should not become a separate K99 aim, and GeneBridge should not be described as aging preliminary data.

## INNOVATION — score 6

### What could be genuinely novel

The most defensible innovation is a linked scientific and statistical framework that:

- treats perturbation response as a change in a population distribution rather than an unobserved cell-to-cell trajectory;
- tests whether aging/AD basal state contributes reproducible predictive information beyond perturbation identity, cell type, and control-state summaries;
- separates stable biological priors from perturbation-specific dynamics and residual heterogeneity;
- evaluates transport across donors, perturbations, contexts, and datasets with uncertainty calibration; and
- validates a small number of predictions against both transcriptional modules and an aging/AD-relevant functional phenotype.

The innovation is the estimand, context-effect question, transport design, and validation—not the choice of a graph neural network or transformer.

### What already exists

The latest literature radar substantially narrows permissible novelty claims:

- GeneGeoFlow already separates graph-derived geometry from perturbation-conditioned dynamics.
- BioM-JEPA already predicts graph-connected gene-block representations.
- DeMixPert already decomposes basal, perturbation-specific, and stochastic response.
- PopPert already models perturbation response at the population joint-distribution level.
- VCBench already emphasizes unseen perturbations, contexts, and cross-dataset transport.
- Graph priors, gene-token transformers, foundation-model embeddings, multimodal integration, and spatial conditioning are established method categories.

### What sounds incremental

- comparing GNN, transformer, and hybrid backbones;
- using genes or modules as tokens;
- adding STRING, GO, coexpression, or regulatory edges;
- adding disease or age labels as covariates;
- appending spatial embeddings to a perturbation predictor;
- imputation followed by differential expression;
- applying an existing foundation model to AD data.

### Claims reviewers would challenge

- **Causal:** no intervention-based identification strategy is documented.
- **Mechanistic:** expression prediction alone does not establish mechanism.
- **Virtual cell:** condition-level expression prediction is narrower than a cellular simulator.
- **Aging-aware:** including age as a feature does not establish age-dependent biology.
- **Spatially informed:** unmatched postmortem spatial data cannot be assumed to encode the niche of an independent perturbation assay.
- **Generalizable:** random-cell splits or target embeddings can conceal donor and perturbation leakage.
- **Therapeutic rescue:** no rescue phenotype, intervention, or functional validation is defined.
- **Interpretable graph:** static association edges are not intervention pathways.

## CENTRAL HYPOTHESIS

### Current state

AIVC still has no finalized central hypothesis in its canonical goals. The weekly strategy contains a provisional, testable premise, but it has not been frozen in the requested premise document or tied to a selected biological system.

### One stronger central hypothesis

**Age- and AD-associated basal cellular states reproducibly modify the population distribution of transcriptional responses to perturbation; therefore, a model that explicitly separates basal context, perturbation-specific effects, and residual heterogeneity will predict responses in held-out donors and an independent dataset more accurately and with better-calibrated uncertainty than an otherwise matched context-agnostic model.**

This hypothesis is falsifiable. It fails if age/AD context gives no reproducible gain over matched context-agnostic baselines, if gains disappear after donor/batch control or context-label shuffling, if they do not replicate externally, or if predicted response modules lack biological validity.

This hypothesis should be narrowed to one cell population, perturbation class, disease stage/context, and biological endpoint once dataset feasibility is known. Spatial niche should not be placed in the central hypothesis unless the selected data measure spatial context and perturbation response in a defensibly linked system.

## SPECIFIC AIMS

No finalized Specific Aims page exists. A defensible structure would be:

### Aim 1 — Establish whether aging/AD context changes perturbation-response distributions

Select one aging/AD-relevant experimental system and one population-level response estimand. Build donor-, perturbation-, context-, and dataset-held-out evaluations. Compare no-change, perturbation-mean, nearest-neighbor, and regularized additive baselines with and without aging/AD context. Use fold-local preprocessing and shuffled-context negative controls.

**Measurable output:** a frozen benchmark, a quantified context effect with uncertainty, and an external replication result.

**Failure resilience:** even a negative result yields a rigorous boundary on where aging/AD context is predictive. It would, however, invalidate the current central premise and require reframing rather than automatic progression.

### Aim 2 — Develop and test a decomposed population-response model

Separate basal state/context, perturbation-specific response, and residual population heterogeneity. Compare against matched-capacity additive, graph, transformer, and established perturbation baselines only after Aim 1 establishes a prediction gap.

**Measurable output:** prespecified improvement in energy distance plus secondary response-effect, module, perturbation-discrimination, and calibration metrics under held-out donors and perturbations.

**Failure resilience:** if the complex model fails, retain the strongest simple model and test when context matters. Do not make Aim 3 dependent on architectural superiority.

### Aim 3 — Validate transportability and biological relevance

Test the selected model and benchmark findings in an independent dataset and prospectively evaluate a small set of prespecified predictions in an aging/AD-relevant neural or glial system. Validate response direction, module activity, heterogeneity, calibration, and one functional phenotype.

**Measurable output:** external transport performance and prospective validation of a limited prediction set.

**Failure resilience:** conduct the independent-dataset and experimentally measured response analyses regardless of whether the novel architecture wins. Use a staged validation ladder and predefined interpretation for failed predictions.

### Aim structure judgment

- **Logical connection:** potentially strong if all aims use one aging/AD system, response estimand, and biological question.
- **Independence:** currently incomplete; Aim 2 depends on Aim 1 premise support, and Aim 3 could depend on Aim 2 predictions. Prespecify baseline-derived and model-independent analyses in Aims 2 and 3.
- **Feasibility:** not established because datasets, computational scale, experimental system, collaborators, and milestones are missing.
- **Measurability:** potentially strong because the weekly strategy proposes grouped splits, a primary metric, negative controls, and a provisional threshold.
- **Failure resilience:** acceptable only if the application states that a failed context effect changes the scientific direction rather than being rescued by a more complex architecture.

## APPROACH — score 8

### Fundamental modeling assumptions

1. Age/AD state is measured well enough to distinguish biological context from technical degradation and cohort structure.
2. The same perturbation is observed across enough donors and contexts to estimate effect modification rather than confounding.
3. Basal transcriptomic state contains reproducible information about response beyond cell type and perturbation identity.
4. Public perturbation systems are sufficiently relevant to aged human neural biology to support an NIA claim.
5. Population distributions are the appropriate estimand for destructive single-cell assays; individual-cell counterfactual mappings are generally not identified.
6. A decomposition into basal, perturbation-specific, and residual components is identifiable or at least diagnostically useful.
7. Cross-dataset differences can be separated from true context-dependent response.
8. Any graph or module prior helps prediction without being misinterpreted as a causal intervention network.
9. Spatial measurements from GeneBridge can contribute only if linked to the perturbation system without donor, section, or modality leakage.
10. Imputed expression preserves disease-effect estimates; GeneBridge has not yet established this.

### Data limitations

- AIVC has no canonical dataset.
- No dataset is documented as jointly containing perturbation, matched control, donor, age/aging condition, AD/pathology state, relevant neural cell type, dose/time, and external replication structure.
- Public perturbation datasets may be dominated by cell lines, young donors, pooled cells, single time points, or non-neural systems.
- GeneBridge contains 23 usable donors, seven cortical layers, and a targeted 300-gene panel, but no perturbation-response measurement.
- GeneBridge donor membership, final method panel, canonical outputs, and disease-analysis results still require verification.
- Cross-sectional postmortem AD/SCZ states cannot be treated as interventions.
- Matching donor labels across Xenium and Visium does not prove section alignment.
- Rare subpopulation responses may be poorly estimated by aggregate distribution metrics.

### Confounding and identification

The core threat is that “aging/AD context” will proxy batch, tissue quality, disease severity, cell composition, postmortem interval, platform, or donor cohort. A valid design must establish overlap and repeated perturbations across contexts. If all AD samples occur in one dataset and all controls in another, disease-context effects are not identifiable separately from dataset effects.

Prespecify handling of age, diagnosis/pathology, sex, ancestry, postmortem interval, brain pH, RNA/tissue quality, medication, smoking/substance exposure, cause of death, batch, library depth, dose, time, cell type/state, cortical region/layer, and donor-level repeated measures where available. Do not adjust for variables that are mediators without stating the estimand.

Age must be more than a nuisance covariate, but apparent age effects must survive sensitivity analyses for technical degradation and survivor/cohort effects. AD diagnosis should not substitute for continuous pathology or stage if those are available.

### Leakage risks

- cell-level splits that retain the same donor in train and test;
- perturbation holdouts whose targets, combinations, or close analogues are encoded in pretrained embeddings;
- full-dataset normalization, feature selection, graph construction, module discovery, or batch correction before splitting;
- tuning on the external dataset;
- test-donor spatial neighbors, matched modalities, or derived embeddings entering training;
- balancing folds or selecting genes using outcomes from held-out data;
- diagnosis-correlated imputation that inflates downstream differential expression;
- reporting the best metric, perturbation subset, cell type, or context after model comparison;
- random graph or spatial ablations that do not preserve degree, density, or capacity and therefore produce unfair comparisons.

Every split should be materialized as a versioned manifest and audited for zero donor and perturbation overlap. Nested tuning must occur within training donors only.

### Statistical weaknesses

- No power or precision analysis exists for detecting context-by-perturbation interactions.
- The provisional 10% improvement threshold is not justified by observed variance.
- Energy distance can be dominated by abundant cell states and global shifts; rare-state and perturbation-specific metrics are needed.
- Mean-delta correlation can look strong while missing response direction or differentially expressed genes.
- Multiple testing across genes, modules, cell types, perturbations, contexts, models, and metrics invites selective reporting.
- Calibration and coverage require enough independent donors; cells are not independent biological replicates.
- Hyperparameter uncertainty and model-selection optimism are unaddressed.
- GeneBridge has seven layer observations per donor; repeated-donor handling and the exact estimable differential-expression formula remain unfrozen.
- Imputation uncertainty is not propagated into GeneBridge disease-effect estimates.
- External replication criteria and compatibility of gene/module spaces are not defined.

A statistical analysis plan should name one primary endpoint, one primary contrast, one inferential unit, grouped resampling, multiplicity control, confidence intervals, missing-data handling, and a rule for failed external transport.

### Validation weaknesses

The current validation plan exists only as a proposed ladder. There is no documented experimental system, collaborator, perturbation set, assay, sample size, endpoint, or access commitment.

A credible ladder is:

1. fold-local internal validation across held-out donors and perturbations;
2. external dataset transport without retuning;
3. negative controls, context shuffling, label permutation, and graph/spatial ablations;
4. replication of response effects and modules, not only global expression similarity;
5. prospective perturbation validation in an aging/AD-relevant neural or glial system;
6. one functional phenotype tied to the biological question.

Without steps 2 and 5, claims should remain computational and predictive. Without a functional phenotype, “mechanistic” and “rescue” claims are not credible.

### Generalization

The decisive claim should be transport across donors and datasets within one aging/AD biological question. Cross-disease transport to SCZ is secondary and should occur only after the NIA premise is established. Failure to transport can be informative only if the design can distinguish biological context specificity from platform and cohort effects.

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. **Relevant computational identity:** training and current work in computational genomics, statistical genetics, spatial transcriptomics, and human DLPFC.
2. **Cohort-scale spatial infrastructure:** a working 23-donor Xenium SCZ/control cohort with seven layers and 161 valid donor-by-layer pseudobulk units.
3. **A held-out-gene benchmark design:** 300 measured genes split into three folds balanced by expression, dispersion, detection, and Moran’s I.
4. **Reported imputation performance:** ENVI is recorded as the leading method, but the final panel and canonical result table remain unverified.
5. **Historical downstream analysis:** donor-layer pseudobulk, recovered slide/run metadata, and layer-adjusted SCZ differential expression. Historical counts are explicitly marked for verification and therefore should not be presented as final preliminary data.
6. **A current state-of-the-art map:** recent papers establish relevant constraints around population-level estimands, decomposed response modeling, graph-connected modules, separation of structural priors from perturbation dynamics, and realistic transport evaluation.
7. **Improved rigor planning:** a prespecified benchmark outline, negative controls, baseline hierarchy, and provisional go/no-go logic now exist in planning notes.

These items demonstrate technical readiness for spatial cohort analysis and benchmark design. They do not demonstrate aging/AD biology, perturbation prediction, causality, mechanistic insight, or virtual-cell validity.

## WHAT IS STILL MISSING

1. A selected aging/AD biological question, cell population, perturbation class, and functional endpoint.
2. A verified primary perturbation dataset and an independent validation dataset with adequate donor/context overlap.
3. A frozen premise sheet, data dictionary, eligibility table, fold manifests, and leakage audit.
4. Any AIVC baseline or context-ablation result.
5. Evidence that aging/AD context improves response prediction beyond matched context-agnostic baselines.
6. Power/precision justification and a data-supported success threshold.
7. External replication and uncertainty calibration.
8. Prospective biological perturbation validation.
9. A validated GeneBridge method table, donor manifest, differential-expression model, and measured-versus-imputed effect concordance analysis.
10. Propagation of imputation uncertainty into downstream inference.
11. A documented K99 mentor team covering aging/AD biology, perturbation experimentation, and causal/probabilistic modeling.
12. Training activities, milestones, responsible conduct, quantitative benchmarks, and transition criteria.
13. A written boundary between the candidate’s program and Jian Hu’s spatial integration program.
14. Letters or documented commitments for data, experimental systems, and validation resources.

# CAREER DEVELOPMENT — weakness incorporated under Investigator

## What still needs to be learned?

The record does not yet present a structured training-needs argument. A credible plan should identify gaps in:

- aging, AD, and neurodegeneration biology;
- neural/glial perturbation systems and experimental design;
- causal inference, effect modification, and transportability;
- probabilistic generative modeling and uncertainty calibration;
- grouped and cross-dataset single-cell benchmarking;
- prospective validation design;
- leadership, grantsmanship, and management of experimental collaborations.

“Learn GNNs and transformers” is too generic for a K99 and does not establish a protected mentored-training need.

## Why is a K99 needed?

The defensible transition is from demonstrated spatial-statistical genomics in human SCZ cortex to an independent program in context-dependent perturbation response in aging/AD. The K99 would be needed to acquire aging biology, perturbation experimentation, causal/transport methods, and prospective validation experience that is not documented in the candidate’s current record.

That argument remains unwritten and unsupported by a named training plan. Without it, reviewers may ask why this is not simply a methods project performed under the current mentor or an R21-style pilot.

## How does the training differ from the mentor’s program?

Jian Hu’s documented project framing covers statistical integration of multi-view, multi-section, and multi-sample spatial transcriptomics to decipher disease mechanisms. GeneBridge’s imputation and spatial cohort integration overlap that domain substantially.

The candidate’s distinct training and ownership must center on:

- intervention and perturbation-response estimands;
- context-effect identification;
- population-distribution modeling;
- transport across donors and datasets;
- calibrated uncertainty; and
- prospective aging/AD experimental validation.

An external aging/AD biological mentor and an experimental perturbation mentor are currently missing from the documented team. A quantitative-methods mentor may also be needed if causal transport and probabilistic modeling are central.

## How does the R00 become independent?

A credible boundary is:

- **K99:** establish the aging/AD context-value benchmark, complete targeted training, develop the first decomposed population-response model, and validate a small number of predictions using mentor-supported data and collaborators.
- **R00:** build an independent program that generates and models perturbation atlases across aged human neural cell states and tissue contexts, with open transport benchmarks and prospective experimental cycles.

Transition milestones should include a frozen benchmark, a leakage-resistant baseline, evidence for or against context dependence, external transport, calibrated uncertainty, at least one prospectively tested prediction, a first-author methods/biology output, and an independent data/validation plan not controlled by the primary mentor.

# INDEPENDENCE

The current record does not yet unmistakably describe the candidate’s future laboratory. GeneBridge demonstrates a useful platform but remains close to the mentor’s spatial-integration domain. AIVC is broad, and broad labels do not establish ownership.

A defensible independent niche is:

**transportable, uncertainty-aware population perturbation modeling under age, disease, donor, and tissue-context shifts.**

The candidate must own the biological question, estimand, benchmark, context-identification strategy, model, and validation cycle. Merely connecting existing foundation models to spatial embeddings would not establish independence.

### Natural funding trajectory

- **R01:** prospective modeling and experimental testing of context-dependent perturbation responses in aging/AD across cohorts and systems.
- **NSF CAREER:** general methods for transportable, uncertainty-aware virtual-cell prediction, open benchmarks, and computational training.
- **Independent faculty program:** a coherent methods-and-biology laboratory only if it includes prospective data generation or durable experimental partnerships. Otherwise, it risks remaining a sequence of retrospective integration and benchmarking projects.

# NIH-style scores

| Criterion | Score | Reviewer rationale |
|---|---:|---|
| **Overall Impact** | **8** | The direction could matter, but the NIA premise, dataset, preliminary AIVC evidence, aging/AD endpoint, validation access, career plan, and independence structure remain absent. Planning gains do not offset foundational evidence gaps. |
| **Significance** | **7** | Context-dependent response in aging/AD could be important, but no aging/AD response effect or defined biological problem is documented. |
| **Investigator** | **6** | Relevant spatial-genomics execution is documented, but perturbation modeling, aging/AD expertise, prospective validation, and independent ownership are not. |
| **Innovation** | **6** | The integrated estimand and transport framework could be novel; its individual components are established, and no implementation or result yet differentiates the program. |
| **Approach** | **8** | No eligible dataset pair, power rationale, finalized aims, baseline, external replication, experimental system, or validation result exists. Confounding and identifiability may be fatal. |
| **Environment** | **5** | Emory and the current mentor plausibly provide a strong genomics environment, but no aging/AD mentor, perturbation facility, experimental collaborator, dataset access, or commitment is documented. |

# Required summary

## TOP 3 STRENGTHS

1. Demonstrated infrastructure and experience for cohort-scale human cortical spatial-genomics analysis with donor and layer structure.
2. Increasingly rigorous evaluation logic: population-level estimands, grouped holdouts, simple baselines, negative controls, external transport, and explicit go/no-go decisions.
3. A potentially independent bridge from spatial/statistical genomics to context-dependent perturbation-response modeling—if aging/AD biology and prospective validation become real rather than aspirational.

## TOP 3 MAJOR RISKS

1. **Fatal NIA-premise risk:** no selected aging/AD system or evidence that aging/AD context changes perturbation response.
2. **Approach/credibility risk:** no AIVC result, eligible dataset pair, identified context effect, external replication, experimental validation, or functional endpoint; causal/mechanistic/virtual-cell claims would be overstated.
3. **Career/independence risk:** the empirical base remains SCZ spatial integration close to the mentor’s program, while the candidate’s aging/AD expertise, mentor team, training need, and independent R00 resources are undocumented.

## TOP 3 EXPERIMENTS TO PRIORITIZE

### 1. Aging/AD perturbation-data feasibility audit and context-value baseline

Select exactly one primary system and one external dataset. Verify donor, perturbation, dose/time, age/aging or AD context, cell type, batch, and response-gene/module compatibility. Freeze donor/perturbation/context splits. Compare matched additive models with and without aging/AD context against no-change, perturbation-mean, and nearest-neighbor baselines. Include shuffled-context controls and donor-bootstrap uncertainty. This experiment decides whether the NIA premise exists.

### 2. Leakage-resistant GeneBridge downstream-validity experiment

Lock the donor list, fold manifests, method versions, and exact repeated-donor differential-expression model. For every held-out measured gene, compare measured and imputed SCZ effect estimates on the same donor-layer units. Evaluate effect-size correlation, sign concordance, calibration, false discoveries under donor-level label permutation, and uncertainty. This can become defensible preliminary evidence of rigorous spatial modeling, but not aging or perturbation evidence.

### 3. Small prospective aging/AD-relevant perturbation validation

With a documented collaborator, select a limited perturbation set in one neural or glial aging/AD-relevant system. Prespecify response modules, population heterogeneity metrics, uncertainty calibration, and one functional phenotype. Test predictions prospectively and include negative controls. Keep the experiment small enough to complete during K99 feasibility work.

## ONE STRONG CENTRAL HYPOTHESIS

Age- and AD-associated basal cellular states reproducibly modify the population distribution of transcriptional responses to perturbation; therefore, explicitly separating basal context, perturbation-specific effects, and residual heterogeneity will improve held-out-donor and external-dataset prediction and uncertainty calibration relative to a matched context-agnostic model.

## ONE-SENTENCE FUTURE-LAB VISION

My laboratory will build and experimentally test transportable, uncertainty-aware models that predict how aging human neural cell populations respond to genetic and pharmacologic perturbations across donors, disease states, and tissue contexts.

# Comparison with previous review

## Status: STAGNANT

The previous review assigned Overall Impact 8 and identified the absence of an aging/AD premise, dataset, AIVC baseline, validation plan, and career-development structure as foundational weaknesses. The new weekly strategy and AIVC decisions respond correctly at the planning level, so the conceptual design is less diffuse. However, none of the named artifacts or experiments is documented as complete, and no result has changed the scientific premise. Overall Impact therefore remains **8**, and the program remains **STAGNANT** rather than improving scientifically.

# Number-one action this week

**Complete and freeze `aging_AD_AIVC_premise_v1.md` using verified metadata from one primary and one independent dataset: one aging/AD question, one cell population, one perturbation class, one population-level estimand, grouped fold manifests, four simple baselines, one primary metric, shuffled-context controls, and a variance-informed go/no-go rule. If no eligible dataset pair exists, document that result and secure a collaborator-generated perturbation system before further architecture work.**
