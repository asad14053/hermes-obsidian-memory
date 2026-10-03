---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-09-26
last_updated: 2026-09-26
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-09-20-NIA-K99-study-section-review]]"
---

# AIVC as a potential NIA K99/R00 — skeptical study-section review

## Bottom line

**Overall Impact: 8/9. Status: STAGNANT for NIA application readiness, despite improved design documentation.**

The September 23 user-supplied outline changes what can legitimately be reviewed: there is now a concrete identity–environment UR/VI design, not merely a list of GNN/Transformer interests. It does not establish an implementation, a prediction result, an aging/AD dataset, or an intervention-validation pathway. The decisive new methodological concern is that **predicting an identity-matched cell in another observed neighborhood does not validate the response of the original cell to a changed environment**. The proposed evaluation tests conditional prediction, not an identified intervention effect.

The NIA weakness remains separate and unresolved: the documented empirical foundation is SCZ cortical genomics, while the proposed NIA application has no selected aging/AD system or evidence that its spatial context changes an experimentally measured response. A better architecture diagram does not close either gap.

This review evaluates the documented program, not the candidate's undisclosed work or intrinsic ability. “Not documented” is not a claim that work has not occurred elsewhere. Scores are provisional reviewer-style judgments on the requested 1–9 scale, with 1 best; they are neither an actual NIH review nor a funding probability or an average of criterion scores.

## What changed since September 20

| Item | New evidence | Effect on assessment |
|---|---|---|
| Scientific design | User-supplied PDF and multimodal diagram preserved September 23 | A real design advance. Review its actual prediction targets and assumptions rather than substituting earlier assistant proposals. |
| Validation specification | PDF proposes cell-level identity-matched environment swaps; diagram explicitly includes donor-held-out tests | These are distinct specifications. The diagram improves the split plan but does not solve causal identification. |
| Architecture scope | PDF: 20 μm pooled neighborhoods and attention head. Diagram: multimodal inputs, multi-scale attention, perturbation encoder and conditional VAE | More concrete, but substantially greater data and implementation burden. Neither version was selected as the definitive implementation. |
| Project results | No new baseline, fold manifest, ablation or validation result found in reviewed project notes | No score improvement justified. |
| Literature | September 25 radar supplies directly relevant input-use and lightweight-context comparisons | Raises the standard for demonstrating that environment and intervention branches add useful information. |
| Candidate framing | September 26 profile records a confirmed AI/ML-for-Genomics-and-Neurobiology faculty identity | Clearer positioning, not a training plan, ownership agreement or preliminary result. |
| Funding intelligence | Actual September 25 funding-job response reports blocked monitoring, not a clean negative search | Funding changes and eligibility remain unverified; do not inherit a “nothing changed” conclusion from nested historical SILENT outputs. |

**Authority correction:** [[02_Projects/AIVC/project-outline]] records the user's intended design. Earlier aging/AD hypotheses, energy-distance endpoints, thresholds and aims in reviews/weekly strategies are assistant recommendations, not approved replacements of that design. The PDF has no mandated disease; the diagram explicitly includes SCZ/NTC. This review recommends an NIA-specific adaptation without changing the broader program's disease scope.

# SIGNIFICANCE — 7

## Why should NIA care?

A credible NIA question would identify a specific aging/AD-associated tissue environment that alters a consequential neural or glial response, and demonstrate when predicting that environment improves intervention prioritization. The deliverable must be a biological inference or validated response prediction—not simply a larger transcriptomic atlas or more accurate expression reconstruction.

The current notes do not select the population, aging or pathology contrast, exposure, intervention, response program or functional phenotype. Age as a covariate and AD as a future application are insufficient. Chronological aging, AD pathology and experimentally induced stress must be distinguished; they are not interchangeable operational definitions.

The relationship to aging/AD is therefore **proposed, not convincing on current evidence**. A computationally strong observational project could still be significant, but it would need an explicit aging/AD biological question and should not advertise causal response validation it has not performed.

## SCZ: useful breadth or loss of focus?

SCZ is the genuine current empirical base and should not be erased. GeneBridge can demonstrate spatial-analysis competence and support an initial measured-target pipeline check. It cannot supply AD or perturbation preliminary evidence. For this NIA application, SCZ should be a bounded methods-development resource or later transport comparison, not a parallel disease aim. A joint SCZ/AD aim would need a shared, prespecified biological mechanism and estimand; none is documented.

If the chosen science remains SCZ-specific, retain that identity rather than relabeling it for NIA. Institute fit is a strategic decision, not an architecture feature.

# INNOVATION — 6

## What could be novel?

The defensible contribution is to establish **when measured tissue context provides transferable response information beyond cell identity, when it does not, and which experimentally supported context changes alter cellular function**. That requires context-use falsification, donor-level transport, uncertainty and experimental discrimination of competing predictions.

The existing outline instead risks equating novelty with combining foundation-model embeddings, neighborhood pooling, attention, imputation and a generative head. Those components may be useful, but their combination alone is not a persuasive innovation claim.

## Current literature pressure

SpaFactor's versioned abstract describes multi-scale context, low-dimensional gene programs and a residual MLP, with author-reported performance across five cohorts.[1] This is a histology-to-expression task, not proof that the same method solves AIVC. It nevertheless motivates a simple pooled-context/low-rank comparator before claiming hierarchical attention is necessary.

CellAudit separates executable input access, fitted input dependence and target-relevant predictive contribution; its abstract reports a predictor that scored well while remaining invariant to compound replacement.[2] AIVC must therefore demonstrate useful reliance on environment and perturbation inputs separately; an active code branch, nonzero attention or output sensitivity is not enough.

The [[02_Projects/AIVC/literature/2026-09-25-literature-radar|September 25 radar]] also identifies DePass as multimodal-integration competition, Hou et al. as an identification caution, and PRAXIS as evidence bookkeeping. Those are secondary radar assessments in this review, not independently re-audited methods or evidence of AIVC performance. Neither integration quality nor auditable execution establishes biological intervention validity.

## Claims likely to be challenged

- **“Counterfactual response”:** currently a model-generated contrast unless an intervention estimand and identification assumptions are justified.
- **“Dynamics from snapshots”:** cross-sectional variation does not specify time, transition order or a dynamical law.
- **“Stable identity”:** identity markers and foundation-model embeddings may also encode activity, disease, stress and environment.
- **“Mechanistic attention”:** attribution is not identification of regulation.
- **“Multimodal universal representation”:** shared donors do not imply paired cells or registered tissue sections.
- **“Joint gene-and-environment interventions”:** separate datasets may not identify their interaction.
- **“Aging-aware”:** requires a biologically defined aging context and evidence beyond age-label association.

# CENTRAL HYPOTHESIS

## What the current design actually tests

The user-supplied outline supports a testable **predictive** hypothesis: local environment adds held-out measured-activity information beyond identity. It has not yet made its stronger intervention interpretation testable. There is no frozen NIA-specific central hypothesis in the reviewed project notes.

## One stronger central hypothesis — proposed, not adopted

**In one defined human neural cell population, an AD-associated inflammatory microenvironment modifies the population response to a prespecified perturbation class; measured baseline neighborhood programs will therefore improve response prediction across held-out donors beyond cell identity alone, and controlled manipulation of that microenvironment will reproduce the prespecified response direction and functional consequence.**

This deliberately narrows to an AD-associated environment rather than treating every aging/AD state as equivalent. Inflammation is a proposed focus, not a discovered project result or selected system. Before use in an application, specify the cell population, exposure, intervention class, measured program, functional endpoint and attainable effect size. If data support a different process, change the hypothesis before looking at protected outcomes.

**Falsification:** no incremental context benefit; gain reproduced by appropriate matched shuffling; failure in independent donors; or a controlled exposure producing a different response from the registered prediction. Prediction and causal validation are separate tests; success in one does not rescue failure in the other.

# SPECIFIC AIMS

No finalized K99 Specific Aims page is documented. “Task 3.1” and “Task 3.2” in the supplied broad outline are not an approved K99 aims page. Atlas curation, a portal, multimodal alignment, new attention, a generative model, gene interventions and biological validation are excessive scope for the current evidence base.

## Proposed narrower structure

### Aim 1 — Establish the incremental predictive value and limits of measured AD-relevant spatial context

Use one eligible neural/glial system and a fixed measured activity target. Compare identity-only, pooled-context and a modest context-aware model on locked donor splits. Audit context replacement, spatial scale, target leakage and external transfer.

- **Deliverables:** accession/metadata manifest, train/test donor manifest, measured-target predictions, per-donor loss contrasts, context-shuffle controls and supported-query boundaries.
- **Success:** a prespecified meaningful held-out benefit with uncertainty at the biological-replicate level and corroboration in an independent cohort or prospectively reserved donors.
- **Failure:** report a context-use boundary; do not claim that architecture complexity will manufacture a missing biological premise.

### Aim 2 — Test a small, predefined environment-by-perturbation response contrast

Use a named collaborator and an accessible experimental system. Select hypotheses from biological rationale and simple-model predictions as well as AIVC, so the experiment can proceed if a complex model loses. Measure expression response and one functional phenotype.

- **Deliverables:** prospective protocol, blinded prediction set, baseline versus model predictions, intervention-effect estimates, functional endpoint and failure analysis.
- **Success:** replicate a registered response contrast across independent biological replicates with appropriately estimated uncertainty.
- **Failure:** distinguish failed prediction, unsuccessful exposure/perturbation, assay inadequacy and a falsified biological hypothesis using manipulation checks and controls.

### R00 expansion — transport and independent validation platform

Extend only the supported question to additional donors and a defined context shift; establish a portable experimental partnership or data-generation capability. Do not make broad cross-disease or joint-intervention generalization the default R00 promise.

**Aim judgment:** logically connected, potentially measurable, not yet feasible on the documented resources. Aim 2 is architecture-independent only if its biological contrast, assay and access are fixed in advance. If it depends entirely on Aim 1 discovering an effect, the proposal remains serial and fragile. Obtain premise/feasibility evidence before submission; do not defer every foundational uncertainty into funded aims. These two aims are a recommended scope reduction, not an approved scientific decision.

# APPROACH — 8

## 1. Identity-matched environment swapping is not causal validation

The PDF proposes matching cells with similar identity but different neighborhoods, substituting the neighborhood embedding and predicting the matched cell's observed activity. This compares different cells. Unmeasured cell state, donor, layer, pathology, technical quality or survival can differ despite a similar embedding.

The observable target is a conditional mean such as `m(c,e,x) = E[Y | C=c, E=e, X=x]`. The proposed contrast `m(c,e',x) - m(c,e,x)` is not automatically the intervention contrast `E[Y(e') - Y(e) | C=c, X=x]`.

An intervention interpretation needs a well-defined manipulable exposure, consistency, relevant overlap and sufficient control of confounding. Spatial interference also matters: changing neighbors can affect other cells and the focal cell's identity/activity. A matched observational swap can test predictive transport within observed support; it cannot supply a paired counterfactual ground truth. Rename its purpose accordingly.

## 2. Identity can contain the answer—or remove part of the effect

DE-derived identity markers, activity genes and embeddings must be selected or fitted only within training data. Keep outcome genes out of focal-cell identity inputs and out of any imputation-derived route that reconstructs them. An encoder may encode activity through correlated proxies even with disjoint gene sets; quantify this rather than assuming perfect disentanglement.

For interventions, use baseline identity when available. Holding a post-exposure identity embedding fixed may condition on a mediator and remove the response being studied. If only endpoint snapshots exist, report the resulting estimand and assumptions rather than calling the representation stable by construction.

## 3. Spatial and cross-modal leakage

- Split donors before feature selection, imputation, alignment, module discovery, tuning and model selection.
- Hold all modalities and sections from a test donor out of training for a donor-generalization claim; adjacent sections are not independent biological replication.
- Remove self-neighbors and investigate segmentation spillover and near-duplicate cells.
- Register which neighbor measurements are available at deployment. Measured test-tissue neighbors may be legitimate inputs for a conditional prediction task; future/post-intervention target measurements are not legitimate predictors of an unobserved response.
- Distinguish an inductive unseen-donor test from a transductive setting using the full test tissue; neither should be mislabeled.
- GeneBridge's held-out-gene folds test missing-gene prediction, not unseen-donor or unseen-intervention generalization.
- The [[02_Projects/GeneBridge/datasets|dataset note]] explicitly warns that donor labels do not establish identical sections or spatial alignment.

## 4. Imputation is not independent ground truth

Training on confidence-weighted imputed targets and evaluating against the same imputer can reward imitation rather than biology. Primary evaluation must use measured held-out outcomes; imputed targets can be a separate auxiliary experiment. Reliability weights need empirical calibration on genuinely held-out measured genes, including difficult and rare states.

Propagate uncertainty or run measured-only sensitivity analyses before downstream disease claims. Cross-modal alignment must not remove the disease response as batch. No matched Xenium/snRNA-seq/Visium/Perturb-seq inventory is established by the architecture diagram.

## 5. Joint-intervention support is absent

Spatial observations without perturbation and dissociated perturbation data without spatial exposures do not, by themselves, establish `environment × intervention` response interactions. A zero perturbation code labels control; it does not create an observed control for every niche. Classify queries as environment-only, perturbation-only or joint, with separate support and validation requirements. Abstain from unsupported combinations rather than presenting them as therapeutic predictions.

## 6. Concrete implementation ambiguities in the supplied designs

- The PDF's `4g` attention indexing and aggregation shape need a tensor-level specification.
- If the intended sparsity penalty is L1 on nonnegative softmax-normalized attention weights, its value is constant and cannot induce sparsity. This is a conditional defect, not a claim that the source actually selected that penalty. Specify the penalty and its target explicitly; entropy, pre-normalization gates and sparse normalization have different effects.
- The diagram's `q(z|c,e,p)` does not specify how observed response `y` enters variational training. If a conventional conditional VAE is intended, document the training posterior, conditional prior, decoder likelihood and inference-time sampling; do not silently repair the diagram into an implemented model.
- Explain how `L_identity` relates to the total loss and how auxiliary objectives are tuned without test-outcome access.
- The listed encoder alternatives do not all imply the displayed raw embedding size. Document actual shapes, checkpoint and trainable parameters.

These are solvable design issues, but demonstrate why the diagram is not an implementation or feasibility result.

## 7. Confounding, sample units and statistical plan

Relevant candidates include donor, age, sex, disease/pathology, layer, cell composition, tissue quality, postmortem interval and batch; prospective assays additionally need dose, time, culture preparation and intervention efficiency. Choose adjustment from a causal/data-generating rationale and design-matrix checks, not by adding every variable. Do not remove genuine mediators when estimating a total effect.

For a first measured-activity test, a proposed exact baseline specification is:

```text
M0: Y_u = alpha + B_C C_u + B_X X_u + epsilon_u
M1: Y_u = alpha + B_C C_u + B_E E_u + B_X X_u + epsilon_u
```

Here `Y` is a frozen measured activity vector, `C` uses permitted identity inputs, `E` is a fixed neighborhood summary and `X` contains prespecified deployment-available covariates. Fit regularized multi-output regression with inner training-donor tuning. An interaction/MLP extension is a distinct comparison, not silently included in M1. Donor ID itself must not become an unseen-donor predictor.

For a proposed prospective functional endpoint, a starting model is:

```text
F ~ exposure * perturbation + Age + Sex + batch + (1 | donor)
```

This is a proposal, not an existing analysis. Freeze the actual exposure coding, response distribution, dose/time, covariates, additional nested experimental-unit terms and estimable contrasts from the real design. If donor is not the relevant independent unit, replace the unit explicitly. Random effects cannot repair complete confounding.

Primary prediction metric: donor-averaged measured-target loss, with training-defined scaling and paired differences between models. Bootstrap or otherwise resample independent biological units; cells and folds are not independent replicates. For an explicitly distributional perturbation task, a population-distance endpoint may be appropriate, but **energy distance is not automatically the right primary endpoint for the PDF's conditional-mean task**.

Freeze response genes/modules, missingness, model-selection budget, multiplicity family, calibration target and meaningful improvement before protected testing. Earlier 10% gain and GeneBridge concordance cutoffs remain provisional planning thresholds, not established standards or achieved results. Use replicate-level variance and biological importance to justify thresholds and sample size.

## 8. Generalization and validation

Separate tests of unseen donor, tissue section, environment, intervention and dataset. Success under one does not establish all five. Match replacement controls within plausible cell-type/layer/technical strata and available support; arbitrary swaps can produce failures that merely reveal impossible inputs.

Measure both prediction sensitivity and useful incremental loss reduction. Refit ablated models to test information value, and separately use frozen-checkpoint replacements to test fitted reliance. Keep a final cohort untouched by both analyses. Biological interpretation requires a measured intervention and functional endpoint, not merely attention maps or expression similarity.

# PRELIMINARY DATA

## What is already documented

1. **Relevant human cortical spatial-genomics work.** GeneBridge notes describe a 24-donor reference cohort, a 23-donor downstream cohort after Br6432 exclusion, targeted Xenium measurement, donor/layer metadata and gene-wise evaluation infrastructure. These are documented project assets; current underlying files were not executed or revalidated in this review.
2. **Historical computational results.** [[02_Projects/GeneBridge/experiments-and-results]] records pseudobulk and DE summaries, explicitly marked historical/verify. They are not upgraded here to a locked result table, replicated biological discovery or proof of ENVI superiority.
3. **A concrete proposed AIVC design.** The supplied PDF and diagram establish inputs, target classes, UR/VI construction and evaluation ideas. They count as design evidence, not experimental preliminary data.

## What is missing from the reviewed record

- A selected aging/AD dataset/system with access, sample inventory, identifiable contrast and validation route.
- A completed `aging_AD_AIVC_premise_v1.md`; filename search found no premise artifact.
- A frozen AIVC target, implemented baseline, executable fold manifest, measured-target prediction or input-use audit.
- Current file-verified GeneBridge method results, full donor accounting and measured-versus-imputed disease-effect preservation.
- Demonstrated multimodal registration and cross-modal donor exclusion.
- Observed environment-by-intervention response support, functional validation or prospective results.
- Power/precision, compute/resource budget, named training team, collaboration commitments and portable R00 ownership.

The vault's [[02_Projects/AIVC/experiments-and-results]] still explicitly states that no finalized benchmark/result set is confirmed. Literature findings are not applicant preliminary data.

# CAREER DEVELOPMENT — Investigator 6; Environment 5

The documented computational, engineering and spatial-genomics background is relevant. A complete biosketch, publication/contribution record and training commitments were not reviewed, so neither score should be read as a comprehensive assessment of the person or institution.

A credible K99 rationale would be the transition from observational human cortical genomics to experimentally grounded, transportable context-response modeling. “Learn Transformers” is not sufficient differentiation from ordinary technical skill acquisition.

| Training gap | Required mentored activity | Verifiable milestone |
|---|---|---|
| Aging/AD biology | Named aging/AD co-mentor; focused biological training tied to the selected system | Defend one disease-relevant mechanism, assay and confounder model |
| Intervention design | Named experimental collaborator; hands-on or embedded assay/design training | Register and complete a limited exposure/perturbation experiment |
| Identification and transport | Causal/statistical mentorship and explicit estimand training | Write the causal assumptions, overlap checks and supported-query policy |
| Reliable spatial ML | Nested donor validation, imputation calibration and uncertainty training | Release a reproducible measured-target benchmark with negative controls |
| Independence and leadership | Mentoring committee, grantsmanship and collaboration/resource planning | Written ownership/resource boundary and executable R00 launch plan |

This is a proposed training matrix. No mentors beyond the documented current relationships, available facilities, courses, percentages of effort or commitments are invented. Attach actual people, activities, time allocations, evaluation schedule and transition criteria before claiming a K99 plan exists.

Institutional reputation is not a substitute for access to an aging/AD validation system. The Environment score reflects documentation gaps, not an assertion that Emory lacks facilities.

# INDEPENDENCE

The program does not yet read unambiguously as the candidate's future laboratory. The primary mentor's documented domain includes multi-view/multi-section/multi-sample spatial integration; a spatial integration portal and expanded imputation are therefore insufficient evidence of separation.

The PDF's title begins “4.3 Thrust 3,” suggesting a broader document context, but authorship, grant ownership and resource portability cannot be inferred from that label. Establish in writing which questions, code, data, collaborations and aims belong to the candidate and can continue independently. Do not assume mentor overlap proves dependence; document the boundary.

An independent niche could center on **falsifiable context-response models, supported intervention queries, donor-level transport and prospective validation in aging neural systems**. It becomes credible through candidate-led datasets/benchmarks, first-author methodological work, an experimental partnership and portable resources—not by naming a framework AIVC.

- **R01 trajectory:** a focused mechanistic/response program with replicated context effects and functional validation.
- **NSF CAREER trajectory:** a generalizable methodological contribution to reliable context-conditioned prediction, with an integrated education plan; merely applying existing ML to an AD dataset is not enough.
- **Faculty laboratory:** a reusable inference/validation platform rather than a single mentor-controlled dataset or unvalidated architecture.

These are possible trajectories, not verified current solicitations or eligibility determinations.

# NIH-style scores

| Criterion | Score | Rationale |
|---|---:|---|
| **Overall Impact** | **8** | Concrete design, but no demonstrated NIA premise, AIVC result, identified intervention-validation path, or documented training/independence structure. |
| Significance | 7 | Potentially consequential context-response question; actual aging/AD biology and endpoint remain unselected. |
| Investigator | 6 | Relevant computational/spatial experience; transition evidence and complete candidate record unavailable. |
| Innovation | 6 | Testable context-use and supported transport could differentiate the program; architecture combination alone does not. |
| Approach | 8 | Observational swap cannot validate intervention response; no implemented baseline, feasible data contract or prospective protocol. |
| Environment | 5 | Strongly relevant institutional/mentor context is documented, but specific aging/AD resources and commitments are not. |

All scores remain unchanged from September 20. Better documentation exposes precise, repairable problems but is not evidence that those problems are solved.

# Required summary

## TOP 3 STRENGTHS

1. **Relevant empirical starting point:** donor-structured human cortical spatial genomics and GeneBridge provide a concrete technical base, albeit with current result verification still outstanding.
2. **A now-explicit, falsifiable design:** identity and environment branches, measured activity targets and donor-held-out evaluation can be tested independently rather than debated only at the architecture level.
3. **A potentially coherent independent question:** establish when tissue context improves transportable response prediction and validate the limits experimentally, consistent with the confirmed AI/ML-for-genomics-and-neurobiology career identity.

## TOP 3 MAJOR RISKS

1. **Causal overclaim:** identity-matched observational swaps are being asked to support intervention-response claims they cannot validate by themselves.
2. **NIA fit and feasibility:** no selected aging/AD system, eligible response dataset, biological endpoint or committed validation route is documented; SCZ assets cannot fill those gaps by relabeling.
3. **Execution and independence:** multimodal scope is expanding ahead of the first result, while training, assay access and portable ownership remain unspecified.

## TOP 3 EXPERIMENTS TO PRIORITIZE

### 1. Measured-target environment-value and input-use falsification

**Prerequisite:** name the dataset, donor manifest, available inputs, activity target and deployment task. For NIA preliminary evidence, the system must have a genuine aging/AD contrast. A GeneBridge/SCZ pilot is useful engineering evidence but must be labeled as such.

Run identity-only ridge, identity-plus-pooled-neighborhood ridge, a small pooled-context MLP and only then the PDF attention head, under identical donor-held-out splits and tuning budgets. Use measured targets, exclude target leakage, and compare both refitted ablations and frozen-checkpoint matched context replacements. Report per-donor loss differences and uncertainty; include plausible shuffled-context and spatial controls. A nonzero output change without target-loss improvement fails the useful-input claim. Do not begin with the full conditional VAE.

### 2. GeneBridge measured-versus-imputed disease-effect preservation

Lock current measured/imputed files, donor exclusions, gene folds and normalization. Use identical donor-layer units and an explicit repeated-donor model for measured and predicted outcomes, for example `expression ~ Dx + Age + Sex + layer + batch + (1 | donor)`, only after confirming the selected batch term is estimable and the outcome/error model is appropriate. This formula is proposed, not the verified historical model. Compare effect estimates, direction, calibration and uncertainty over the same gene universe; assess null behavior with donor-level permutations only where exchangeability is defensible, otherwise use an appropriate covariate-aware resampling procedure. This tests downstream biological validity, not AD or perturbation competence.

### 3. Small prospective environment-by-perturbation validation

In one accessible aging/AD-relevant neural or glial system, manipulate a defined exposure and a limited perturbation set with matched controls, randomized allocation where feasible, independent biological replication, manipulation checks and a prespecified functional endpoint. Freeze baseline and AIVC predictions before measurement. Size the independent replicates from pilot variability, not cell count. This can directly test the hypothesis; a new atlas or another imputed transcriptome cannot substitute for it.

## ONE STRONG CENTRAL HYPOTHESIS

In one defined human neural cell population, an AD-associated inflammatory microenvironment modifies the population response to a prespecified perturbation class; measured baseline neighborhood programs will improve held-out-donor response prediction beyond identity alone, and controlled manipulation of that environment will reproduce the registered response direction and functional consequence.

## ONE-SENTENCE FUTURE-LAB VISION

My laboratory will develop and experimentally test reliable models of how tissue environments shape cellular responses in aging human neural systems, with explicit limits on donor transport and intervention claims.

# Comparison status: STAGNANT

The design is **better specified** than on September 20; the application is **not better evidenced**. Do not repeat the previous review's claim that only generic architecture discussions exist. Conversely, do not count the new diagram, faculty-search framing or additional papers as preliminary data. No documented result warrants a better overall score, and the new critique does not justify worsening a score merely because ambiguity has become visible.

The funding-monitoring gap is newly clarified by reading the actual latest response. It is not a scientific deterioration, but it prevents reliance on the funding feed for current rules or deadlines.

# Number-one action this week

**Complete the NIA feasibility gate before further architecture expansion:** write `aging_AD_AIVC_premise_v1.md` from verified metadata, naming one aging/AD system, one cell population, one measured response target, the actual donor-resolved dataset/access status, and one feasible intervention-validation route. Explicitly separate the observational prediction estimand from the intervention claim. If no eligible data or validation route exists, record that no-go result rather than relabeling SCZ data; define the minimum collaborator-generated experiment needed.

The immediate next analysis after a positive gate is Experiment 1—not another multimodal architecture. A small SCZ measured-target pilot need not wait for an AD perturbation dataset, but it must not be presented as establishing the NIA premise.

# Evidence and retrieval limits

- Canonical vault: `/opt/data/obsidian-vault`.
- Read AIVC overview, current state, user-supplied outline, methods, datasets, goals, decisions, experiments/results and next actions; read the complete September 20 review across retrieved sections.
- Read the original two-page outline PDF via document extraction; the extracted mathematical layout is partly malformed. Exact architecture details are grounded in the preserved intake note with PDF-page/diagram-module attribution. The original diagram was not newly visually inspected in this run.
- Read GeneBridge current state, datasets, methods, experiments/results and next actions; research overview/interests; learning-paper memory; active tasks, unanswered questions and September 21 weekly strategy; identity/career and collaborators.
- Requested `05_Papers_and_Learning/` and `09_Open_Loops/` do not exist; searched/read their canonical counterparts `05_Learning/` and `09_Planning/`.
- Read the full [[02_Projects/AIVC/literature/2026-09-25-literature-radar|September 25 literature radar]] and September 23 radar scope/initial item. Fresh arXiv API retrieval verified the versioned abstracts of SpaFactor and CellAudit; no code reproduction or new full-paper audit is claimed. Their findings remain author-reported preprint evidence.
- The supplied context_from blocks were truncated and contained nested old outputs. Recovered the exact latest funding response from [[Hermes/Conversations/2026-09-25/cron_b006ab3b7fec_20260925_130011|September 25 funding-job conversation]], final Assistant section: monitoring was blocked and there were no verified findings. No current NIH deadline, eligibility change or institute priority is asserted here. Official-policy verification remains outside this scientific review.
- Prior comparison: [[02_Projects/AIVC/reviews/2026-09-20-NIA-K99-study-section-review]].
- No underlying HPC analysis or biological experiment was run. This artifact is a grounded review, not a new project result. Primary project facts and approved disease scope have not been rewritten.

## Sources

[1] http://arxiv.org/abs/2609.28563v1 — SpaFactor: Lightweight Spatial Context-Aware Gene Program Modeling for Histology-to-Transcriptomics Inference
[2] http://arxiv.org/abs/2609.27234v1 — Discover, Falsify, Revise: Auditing Input-Use Claims from Source Code to Predictive Contribution in Agent-Discovered Cell Models

