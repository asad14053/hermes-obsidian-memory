---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-09-20
last_updated: 2026-09-20
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-09-19-NIA-K99-study-section-review]]"
---

# AIVC as a potential NIA K99/R00 — skeptical study-section review

## Bottom line

This remains an early research-program concept, not an application-ready NIA K99/R00. Since the [[02_Projects/AIVC/reviews/2026-09-19-NIA-K99-study-section-review|September 19 review]], the canonical vault documents no new scientific result and no completion of the premise sheet, aging/AD perturbation-data audit, dataset pair, fold manifest, leakage audit, baseline, context ablation, external replication, prospective experiment, GeneBridge verification package, mentor plan, or independence agreement.

The core NIA premise is still hypothetical: age- or AD-associated basal state may modify perturbation response, but the program has not selected a biological system in which that interaction is observable and identifiable, much less shown that it is reproducible or predictive. The actual empirical foundation remains GeneBridge, a schizophrenia spatial-imputation project with important results still marked for verification. That work demonstrates relevant technical experience but is not aging/AD or perturbation preliminary evidence.

The likely Overall Impact remains **8**. This is not a writing problem. The weaknesses are absent premise evidence, unresolved data feasibility, no AIVC execution, no prospective validation path, and no documented career-development or independence structure.

## Change since the previous review

### What changed

1. No new AIVC or GeneBridge experimental evidence was found after the September 19 review.
2. The latest available AIVC literature radar remains the September 18 CellRFT update. It reinforces the prior warning that optimizing biological evaluation metrics can improve selected endpoints while degrading perturbation discrimination; it does not provide project preliminary data.
3. The latest supplied NIA/K99 funding-radar output remains silent. No new funding rule, deadline, eligibility change, or NIA priority is treated as established.

### What did not change

- `aging_AD_AIVC_premise_v1.md` does not exist in the canonical vault.
- [[02_Projects/AIVC/datasets|AIVC datasets]] still names no primary or independent aging/AD perturbation dataset.
- [[02_Projects/AIVC/experiments-and-results|AIVC experiments and results]] still contains no benchmark or result.
- [[02_Projects/AIVC/goals|AIVC goals]] remains SCZ-centered; aging/AD remains a proposed K99 direction rather than a documented scientific program.
- GeneBridge’s final method table, complete donor/fold manifest, exact DE specification, and measured-versus-imputed disease-effect preservation remain unverified.
- No aging/AD mentor, perturbation-experiment mentor, prospective-validation collaborator, facility commitment, or portable R00 resource is documented.

**Comparison judgment: STAGNANT.** The score is unchanged because no evidence changed. A one-day interval alone does not justify a worse score, but repeated review without execution is not progress.

## Evidence reviewed and boundaries

Reviewed:

- AIVC overview, current state, goals, datasets, methods, decisions, experiments/results, and next actions.
- GeneBridge overview, current state, experiments/results, and next actions.
- Research overview and scientific interests.
- Active tasks, unanswered questions, and the September 13 AIVC/GeneBridge strategy.
- AIVC literature memory through September 18, including CellRFT.
- The September 19 NIA K99 study-section review.
- Identity/career and collaborator notes.
- The latest supplied NIA/K99 funding-radar output, which was silent.

The requested folders `05_Papers_and_Learning/` and `09_Open_Loops/` do not exist. Their apparent canonical equivalents, `05_Learning/` and `09_Planning/`, were reviewed. No aim, result, dataset access, collaborator commitment, or progress was inferred where the notes were silent. Historical GeneBridge values marked for verification are not treated as locked preliminary results.

# NIH criterion review

## SIGNIFICANCE — score 7

### Why should NIA care?

NIA should care only if the project demonstrates a consequential and reproducible failure of perturbation-response models when they are transported into aged or AD-relevant human neural states. The health relevance would be the ability to predict context-specific benefit, resistance, or toxicity that young, pooled, cell-line, or context-agnostic systems miss.

That problem is potentially important, but the proposal must anchor it to one biological process and one functional consequence. Plausible examples include microglial inflammatory response, lysosomal dysfunction, proteostatic stress, senescence, metabolic stress, or synaptic resilience. “A more accurate virtual cell” is not itself an NIA significance argument.

### Is the aging/AD/neurodegeneration relationship convincing?

No. It is strategic, not empirical.

- No aging/AD perturbation system is selected.
- No neural or glial population, perturbation class, disease stage, response module, or functional endpoint is fixed.
- No primary/external dataset pair is verified.
- No age-by-perturbation or AD-context-by-perturbation effect is reported.
- No analysis distinguishes context from donor, cohort, assay, batch, tissue quality, or cell composition.
- No prospective aging/AD validation system or access commitment is documented.

Cross-sectional postmortem disease expression and statistical adjustment for age cannot substitute for perturbation-response evidence. Until the context effect survives grouped evaluation and external replication, NIA relevance is an asserted application area.

### Does SCZ add breadth or make the proposal unfocused?

SCZ makes the K99 unfocused if it becomes a co-equal disease aim. It also invites the criticism that the method was developed for SCZ and later relabeled for NIA.

GeneBridge can have only bounded roles:

1. evidence that the candidate can execute cohort-scale human cortical spatial genomics;
2. a later negative-control or transport stress test; and
3. a way to distinguish aging/AD-specific programs from generic cortical disease signals.

It is not aging preliminary data, and it should not be used to claim perturbation competence. A separate SCZ aim should be excluded from the NIA K99 unless the aging premise is first established and a narrow cross-disease comparison directly tests that premise.

## INNOVATION — score 6

### What could be genuinely novel?

The defensible innovation is an integrated biological-statistical program that:

- identifies when age/AD basal state changes perturbation-response distributions;
- uses population distributions rather than fictitious paired-cell counterfactuals for destructive assays;
- separates basal context, perturbation-specific response, and residual heterogeneity;
- quantifies transport across donors and datasets with calibrated uncertainty;
- protects final evaluation from donor leakage and metric optimization; and
- links predicted response modules to one prespecified aging/AD functional phenotype.

The strongest claim is not “a new virtual-cell architecture.” It is: **identify the boundary conditions under which perturbation knowledge transports into aged human neural contexts, then build and prospectively test a calibrated population-response model that respects those boundaries.**

### What already exists?

The literature removes novelty from most component claims:

- PopPert already frames prediction at the population joint-distribution level.
- DeMixPert already separates basal, perturbation-specific, and stochastic components.
- GeneGeoFlow already separates structural gene geometry from perturbation-conditioned dynamics.
- BioM-JEPA already predicts graph-connected gene-block representations.
- VCBench already emphasizes unseen contexts, unseen perturbations, and cross-dataset transport.
- Recent causal-path work already transfers a perturbational ordering scaffold and re-estimates effects in a target population.
- Immune World Model already uses hierarchical action-conditioned state transitions.
- scKITE already introduces regulatory and annotation supervision in single-cell Transformer pretraining.
- HyCLoST already combines spatial image and expression representations in hierarchical geometry.
- CellRFT already optimizes non-differentiable population-level metrics and exposes metric conflicts.

These methods do not solve aging/AD transport, but they make broad claims about graph priors, context conditioning, population prediction, world models, and biological reward optimization non-novel.

### What sounds incremental?

- comparing GNN, Transformer, and hybrid backbones;
- treating genes or modules as tokens;
- adding STRING, GO, coexpression, or inferred-GRN edges;
- adding age, diagnosis, or spatial embeddings as covariates;
- applying a foundation model to an AD dataset;
- reinforcement fine-tuning against the same metrics later reported as evidence;
- imputation followed by DE without effect-preservation tests;
- calling cross-dataset prediction a world model without an identified transition process.

### Claims reviewers will challenge

- **Causal:** no identification strategy or transport assumptions are fixed.
- **Mechanistic:** expression prediction, attention, and graph weights are not mechanisms.
- **Virtual cell:** a condition-level transcriptomic predictor is narrower than a cell-state/function simulator.
- **Aging-aware:** including age or AD labels does not establish effect modification.
- **Spatially informed:** unmatched spatial tissue does not identify the niche of an independent perturbation assay.
- **Generalizable:** grouped splits, fold-local preprocessing, and external transport are not implemented.
- **Biologically aligned:** optimizing a metric can overfit it or damage another biological property.
- **Therapeutic:** no rescue phenotype, efficacy endpoint, or toxicity endpoint exists.
- **Independent:** current empirical work remains close to the primary mentor’s spatial-integration program.

# CENTRAL HYPOTHESIS

## Current state

No central hypothesis is frozen in the canonical AIVC goals. The planning note contains a plausible premise, but it has no selected system or supporting result.

## One strong central hypothesis

**Age- and AD-associated basal states in a defined human neural cell population reproducibly modify the population distribution of responses to a defined perturbation class; therefore, a model that separates basal context, perturbation-specific effects, and residual heterogeneity will improve held-out-donor and external-dataset prediction and uncertainty calibration over an otherwise matched context-agnostic model, and its highest-confidence response modules will predict a prespecified aging/AD-relevant functional phenotype.**

This is falsifiable. It fails if context gives no reproducible benefit, the apparent gain disappears after donor/batch control or context-label shuffling, transport fails externally, or predicted modules do not track the functional phenotype. Every instance of “defined” must be replaced by a real system before this becomes an application hypothesis.

# SPECIFIC AIMS

No finalized Specific Aims page exists. The following structure is defensible only after Aim 1 feasibility evidence exists.

## Aim 1 — Determine whether aging/AD context modifies perturbation response

Select one neural or glial population, one aging/AD context, one perturbation class, and one population-level estimand. Audit one primary and one independent dataset. Under donor-, perturbation-, and dataset-held-out evaluation, compare matched context-conditioned and context-agnostic additive models against no-change, perturbation-mean, and nearest-neighbor baselines.

- **Output:** eligibility table, data dictionary, frozen folds, automated leakage report, context-effect estimate with donor-level uncertainty, and external replication.
- **Measurable:** one primary endpoint, one primary contrast, confidence interval, context-shuffle negative control, and prespecified go/no-go criterion.
- **Failure resilience:** a negative result defines a boundary condition but invalidates the current premise. The application cannot simply proceed to a complex model unchanged.

## Aim 2 — Build a transportable, decomposed population-response model

Model basal context, perturbation-specific response, and residual heterogeneity. Compare against matched-capacity simple models and established perturbation methods. Keep structural priors separate from learned response dynamics. If metric-based fine-tuning is used, restrict it to development donors and protect final metrics and contexts.

- **Output:** calibrated predictions and a map of where context helps, fails, or becomes nontransportable.
- **Measurable:** frozen population-distance endpoint, response/module metrics, perturbation discrimination, interval coverage, and computational cost.
- **Failure resilience:** retain the strongest simple model and complete context-boundary analyses if the novel architecture fails.

## Aim 3 — Test external transport and biological relevance prospectively

Without retuning, evaluate the selected model on the external dataset. Then prospectively test a small prespecified perturbation set in one aging/AD-relevant neural or glial system. Measure response direction, modules, heterogeneity, uncertainty, and one functional phenotype. Compare both model-selected and baseline-selected predictions.

- **Output:** external transport result and a limited prospective validation set.
- **Measurable:** prespecified effect directions, module scores, functional endpoint, calibration, and negative controls.
- **Failure resilience:** the experiment remains interpretable if the complex model fails because simple-model predictions are tested in parallel.

## Aim structure judgment

- **Logical connection:** potentially strong if all aims use one biological question and estimand.
- **Independence:** insufficient if Aims 2 and 3 require a complex model to win; baseline-based branches must be explicit.
- **Feasibility:** unestablished because data, compute, validation system, collaborator access, budget, and timeline are unknown.
- **Measurability:** potentially good because grouped folds, a primary metric, controls, and a go/no-go framework are already proposed.
- **Resilience:** acceptable for architecture failure, not for premise failure. The proposal must distinguish them.

## APPROACH — score 8

### Untested modeling assumptions

1. Age/AD context is not perfectly confounded with cohort, platform, batch, or donor composition.
2. The same perturbations repeat across enough donors and contexts to estimate effect modification.
3. Basal state adds information beyond perturbation identity, cell type, and simple control summaries.
4. Public perturbation systems are relevant to aged human neural biology.
5. Population distributions are the correct estimand for destructive single-cell assays.
6. Basal, perturbation-specific, and residual components are identifiable enough to interpret.
7. Dataset shift can be separated from biological context shift.
8. Structural priors can improve prediction without being misrepresented as causal networks.
9. Training rewards do not invalidate final metrics as independent evidence.
10. Transcriptional response predicts the selected functional phenotype.

### Data limitations

- No canonical AIVC dataset exists.
- No dataset is documented as jointly containing perturbation, control, donor, aging/AD context, relevant neural cell type, dose/time, and adequate replication.
- No compatible independent dataset is identified.
- If AD and control observations come from different datasets, diagnosis and dataset are inseparable.
- GeneBridge contains spatial and donor structure but no perturbation response and only a targeted 300-gene Xenium panel.
- GeneBridge’s complete donor accounting and downstream results remain partly unverified.
- No sample-size, detectable-interaction, or precision calculation exists.
- Global population metrics may hide rare but consequential response states.

### Confounding and identification

Age/AD context can proxy cohort, platform, batch, postmortem interval, brain pH, RNA/tissue quality, cell composition, region/layer, medication, disease severity, survivor effects, ancestry, sex, and exposure history. Identification requires overlap: the same perturbations observed across multiple donors and contexts within a design where context is not equivalent to dataset.

The analysis must prespecify the estimand and handling of age, diagnosis/pathology, sex, ancestry, tissue quality, postmortem interval, medication, smoking/substance exposure, dose, time, cell state, region/layer, and repeated donor measures. It must distinguish confounders from mediators.

Perturbational networks from other systems may constrain candidate order or structure, but direct effects must be re-estimated in the target population. Importing a cell-line GRN unchanged into aged human neural cells is not defensible.

### Leakage and benchmark overfitting

Major risks include:

- cell-level splits that retain donors across train and test;
- target-embedding leakage between related perturbations;
- normalization, feature selection, batch correction, graph construction, module discovery, or retrieval fit before splitting;
- test labels entering knowledge supervision, prompts, or annotations;
- tuning on the external dataset;
- test-donor spatial neighbors or modalities entering training;
- post hoc response-gene, subgroup, model, or metric selection;
- diagnosis-correlated imputation inflating DE;
- using the same metrics for reinforcement fine-tuning and final biological evidence;
- unfair graph/spatial ablations that alter capacity or graph density.

Every split needs a versioned manifest and automated zero-overlap checks. Preprocessing and tuning must be nested within training donors. A CellRFT-like stage must use development metrics only; final claims require untouched donors, perturbations, datasets, and a functional endpoint not used as a reward.

### Statistical weaknesses

- Cells are not independent biological replicates; donors or experimental units must drive uncertainty.
- No power analysis exists for context-by-perturbation interactions.
- The provisional 10% improvement threshold lacks a variance or biological-importance rationale.
- Energy distance may be dominated by abundant states and broad shifts.
- Mean-delta correlation can conceal wrong direction, rare-state failure, and poor calibration.
- Multiplicity spans genes, modules, cell types, perturbations, contexts, models, and metrics.
- Model-selection and hyperparameter uncertainty are ignored.
- Calibration cannot be inferred from many cells when donor count is small.
- Cross-dataset gene/module compatibility and assay-incompatibility rules are undefined.
- External replication criteria are not fixed.
- GeneBridge’s repeated-donor DE model and imputation-uncertainty propagation remain unresolved.

A credible statistical plan needs one inferential unit, primary contrast, primary endpoint, grouped resampling scheme, multiplicity strategy, missing-data rule, confidence-interval method, calibration definition, and interpretation of failed transport.

### Biological validation gaps

No experimental system, collaborator, assay, perturbation set, sample size, endpoint, or resource commitment is documented. The minimum validation ladder is:

1. fold-local internal validation across held-out donors and perturbations;
2. context shuffling, label permutation, and leakage-negative controls;
3. external transport without retuning;
4. validation of perturbation effects and modules, not global similarity alone;
5. prospective testing in an aging/AD-relevant neural or glial system; and
6. one functional phenotype tied to the biological question.

Without external and prospective validation, claims must remain computational. Without a functional phenotype, mechanistic, rescue, and therapeutic claims are unsupported.

### Generalization

The decisive claim should be donor and dataset transport within one aging/AD biological question. Performance across unrelated cell lines is insufficient. SCZ can be a secondary stress test only after the NIA premise is established. A failed transport result is interpretable only if platform and assay incompatibility can be separated from true biological context specificity.

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. Documented expertise in computational genomics, statistical genetics, spatial transcriptomics, and human DLPFC.
2. A working GeneBridge downstream framework for a 23-donor Xenium SCZ/control cohort, seven cortical domains, and 161 donor-by-layer units.
3. A held-out-gene design for 300 measured Xenium genes split into three folds.
4. Metadata recovery, donor-layer pseudobulk construction, and a layer-adjusted DE workflow.
5. Historical ENVI ranking and DE summaries, explicitly marked for verification.
6. A current methodological map covering population estimands, decomposition, structural priors, target-population re-estimation, transport, multiscale modeling, and metric conflicts.
7. A rigorous proposed benchmark logic: grouped holdouts, simple baselines, context ablation, negative controls, external transport, and go/no-go criteria.

This supports computational feasibility in spatial genomics. It does not support aging/AD biology, perturbation prediction, causal inference, virtual-cell validity, or prospective experimental execution.

## WHAT IS STILL MISSING

1. One selected aging/AD question, cell population, perturbation class, and functional endpoint.
2. A verified primary perturbation dataset and independent external dataset with usable overlap.
3. The premise sheet, eligibility table, data dictionary, fold manifests, leakage audit, and frozen configuration.
4. Any AIVC baseline, context-ablation, uncertainty, or calibration result.
5. Evidence that aging/AD context adds predictive information after donor and technical control.
6. Power/precision estimates and a justified success threshold.
7. External replication without retuning.
8. Prospective aging/AD perturbation validation.
9. A canonical GeneBridge method table, donor/exclusion manifest, DE model, and measured-versus-imputed disease-effect concordance.
10. Propagation of imputation uncertainty into downstream inference.
11. A named aging/AD mentor, experimental perturbation mentor, and quantitative mentor if required.
12. Data, facility, assay, and collaborator commitments.
13. A career-development plan with activities, milestones, evaluation, and transition criteria.
14. A written scientific/resource boundary from Jian Hu’s program.
15. Evidence that code, data access, collaborations, and scientific ownership can move to the R00 institution.

# CAREER DEVELOPMENT — Investigator score 6

### What remains to be learned?

A defensible training gap includes:

- aging, AD, and neurodegeneration biology;
- neural/glial perturbation systems and experimental design;
- causal effect modification and transportability;
- probabilistic population modeling and calibrated uncertainty;
- grouped and cross-dataset single-cell benchmarking;
- prospective validation and functional-assay design; and
- grantsmanship, leadership, and management of experimental collaborations.

“Learn GNNs and Transformers” is not a sufficient K99 training need. It is generic technical development and does not justify protected mentored time.

### Why is a K99 needed?

The credible transition is from human cortical spatial/statistical genomics in SCZ to an independent program in context-dependent perturbation response in aging/AD. K99 support could provide the biological, experimental, causal/transport, and validation training absent from the current record.

That rationale is not yet documented as a plan. Without named mentors, formal activities, measurable milestones, and evidence that these capabilities are unavailable in the current arrangement, reviewers can interpret this as a methods pilot rather than a mentored career transition.

### How must training differ from the primary mentor’s program?

Jian Hu’s documented program centers on statistical integration of multi-view, multi-section, and multi-sample spatial transcriptomics. GeneBridge overlaps directly with that domain. The candidate’s independent ownership should instead center on:

- intervention and perturbation-response estimands;
- age/disease effect-modification identification;
- population-distribution prediction;
- donor/dataset transport and calibrated uncertainty; and
- prospective aging/AD experimental validation.

Aging/AD biology and perturbation-experiment mentors are necessary. A causal/probabilistic methods mentor may also be needed. The application must explicitly state what code, questions, datasets, partnerships, and resources the candidate can take into the R00 phase.

### K99-to-R00 transition

- **K99:** establish the context-value premise, complete targeted training, build and benchmark the first decomposed population-response model, and prospectively test a small prediction set using committed mentor-supported resources.
- **R00:** generate and model perturbation data across aged human neural cell states and tissue contexts, maintain open transport benchmarks, and run iterative prediction-validation cycles under the candidate’s control.

Transition milestones should include a frozen benchmark, leakage-resistant baseline, quantified context effect or principled negative result, external transport, calibrated uncertainty, at least one prospectively tested prediction, a first-author output, and an independent validation pipeline not controlled exclusively by the primary mentor.

# INDEPENDENCE

The current record does not yet look unmistakably like the candidate’s future laboratory. GeneBridge is useful preliminary work but close to the mentor’s spatial-integration domain. AIVC is broad and currently has no unique data asset, experimental partnership, validated method, or demonstrated biological premise.

The defensible independent niche is:

**transportable, uncertainty-aware population perturbation modeling under age, disease, donor, and tissue-context shifts, coupled to prospective neural validation.**

The candidate must own the question, estimand, benchmark, transport assumptions, model, perturbation prioritization, and validation cycle. Merely adding foundation-model embeddings or spatial features will not establish independence.

### Future funding trajectory

- **R01:** generate and experimentally test context-dependent perturbation maps in aging/AD across donors, cell states, and systems.
- **NSF CAREER:** develop general transportable, uncertainty-aware virtual-cell methods, open benchmarks, and associated computational training infrastructure.
- **Independent laboratory:** combine statistical genomics, population-response modeling, and durable experimental partnerships in iterative prediction-validation studies.

This trajectory is credible only if R00 work does not depend on the primary mentor’s unpublished data, staff, or core aims.

# NIH-style scores

| Criterion | Score | Reviewer rationale |
|---|---:|---|
| **Overall Impact** | **8** | No NIA-specific premise evidence, eligible dataset pair, AIVC result, functional endpoint, external replication, prospective validation, training plan, or independence structure is documented. |
| **Significance** | **7** | Aging/AD context-dependent response could matter, but neither the biological problem nor the context effect is established. |
| **Investigator** | **6** | Relevant computational/spatial experience exists; aging/AD, perturbation modeling, prospective validation, and portable ownership are undocumented. The vault lacks a full biosketch/publication record, limiting confidence. |
| **Innovation** | **6** | Context identification plus transport and prospective validation could be distinctive, but most components exist and no result differentiates the program. |
| **Approach** | **8** | Data feasibility, power, aims, baseline, external transport, experimental system, and validation are absent; confounding and leakage could be fatal. |
| **Environment** | **5** | Emory and the primary mentor plausibly provide genomics strength, but no aging/AD mentor, perturbation collaborator, facility/access plan, or commitment is documented. |

# Required summary

## TOP 3 STRENGTHS

1. Relevant computational and spatial-genomics infrastructure for donor-structured human cortical analysis.
2. A sound proposed rigor framework: population estimand, grouped holdouts, simple baselines, context ablation, negative controls, external transport, and uncertainty.
3. A potentially independent niche joining statistical genomics, perturbation transportability, and prospective neural validation.

## TOP 3 MAJOR RISKS

1. **Fatal NIA-premise risk:** no selected aging/AD perturbation system and no evidence that aging/AD context modifies response.
2. **Approach/credibility risk:** no AIVC result, viable dataset pair, leakage audit, external replication, functional endpoint, or prospective experiment.
3. **Career/independence risk:** the empirical base remains unverified SCZ spatial-imputation work close to the mentor’s domain, without a documented aging/AD training team or portable R00 platform.

## TOP 3 EXPERIMENTS TO PRIORITIZE

### 1. Aging/AD perturbation-data feasibility audit and context-value baseline

Select one primary and one independent system. Verify donor, perturbation, dose/time, context, cell type, batch, and response-space compatibility. Freeze grouped splits. Run no-change, perturbation-mean, nearest-neighbor, and additive/ridge baselines with and without aging/AD context. Include context shuffling, donor-bootstrap uncertainty, and an external no-retuning test. This determines whether the NIA premise exists.

### 2. GeneBridge measured-versus-imputed disease-effect preservation

Lock the donor list, folds, model versions, and repeated-donor DE specification. For every measured-but-held-out Xenium gene, compare measured and imputed SCZ log-fold changes on identical donor-layer units. Quantify effect correlation, sign concordance, calibration, RMSE, discovery behavior, and donor-label-permutation false positives. This can establish rigorous computational competence, not aging or perturbation evidence.

### 3. Small prospective aging/AD-relevant perturbation experiment

With a named collaborator, test a limited perturbation set in one neural or glial aging/AD-relevant system. Prespecify response modules, population metrics, uncertainty, negative controls, and one functional phenotype. Compare predictions from the strongest simple baseline and any complex model. Do not wait for a grand virtual-cell architecture.

## ONE STRONG CENTRAL HYPOTHESIS

Age- and AD-associated basal states in a defined human neural cell population reproducibly modify population-level responses to a defined perturbation class; therefore, separating basal context, perturbation-specific effects, and residual heterogeneity will improve held-out-donor and external-dataset prediction and calibration over a matched context-agnostic model, while identifying response modules that predict a prespecified aging/AD-relevant functional phenotype.

## ONE-SENTENCE FUTURE-LAB VISION

My laboratory will build and experimentally test transportable, uncertainty-aware models that predict how aging human neural cell populations respond to genetic and pharmacologic perturbations across donors, disease states, and tissue contexts.

# Comparison with the previous review

## Status: STAGNANT

The September 19 review assigned Overall Impact 8 and identified the absent aging/AD premise, dataset pair, baseline, external and prospective validation, career plan, and independence structure as foundational weaknesses. Every gap remains open. No new evidence warrants a better score; the short interval and unchanged record do not yet justify a worse score. Overall Impact remains **8**.

# Number-one action this week

**Complete and freeze `aging_AD_AIVC_premise_v1.md` from verified metadata for one primary and one independent dataset, specifying one aging/AD question, one cell population, one perturbation class, one population-level estimand, executable donor/perturbation-held-out folds, four simple baselines, one protected primary metric, shuffled-context controls, and a variance-informed go/no-go rule. If no eligible dataset pair exists, record that negative result and secure a collaborator-generated perturbation system before doing further architecture work.**
