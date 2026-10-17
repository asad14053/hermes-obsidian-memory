---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-10-10
last_updated: 2026-10-10
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-10-06-NIA-K99-study-section-review]]"
new_project_results_verified: false
material_methodological_update: true
---

# AIVC as a potential NIA K99/R00 — skeptical review

## Bottom line

**Overall Impact: 8/9 — STAGNANT.** The documented program still lacks a selected aging/AD biological question with an accessible response-validation system, an executed AIVC benchmark, and a committed career-development/independence package. These are application-readiness judgments, not proof that no work occurred outside the vault. Scores are provisional, document-based, with 1 best; they are not an NIH decision or an arithmetic average.

**New since the October 6 review:** the October 9 literature adds a more direct novelty challenge to editable neighborhood-conditioned prediction and stronger reasons to evaluate context-specific response diversity and transport failure. A new diagram would not answer either challenge. The priority remains an evidence-backed aging/AD premise-and-access decision, not another model component.

The scientific authority remains [[02_Projects/AIVC/project-outline|the September 23 user-supplied outline]]. Its PDF and multimodal diagram are distinct proposed specifications. [[02_Projects/AIVC/goals|Canonical goals]] remain SCZ-centered. The NIA-oriented hypothesis and aims below are **reviewer proposals**, not an approved disease-focus change.

## Evidence, coverage and comparison

Reviewed AIVC outline, state, goals, results, datasets, tasks and overview; GeneBridge datasets, methods, state, results and tasks; research overview/interests; profile and mentor context; learning references; active tasks/questions; October 5 weekly strategy; October 7 and October 9 literature notes; and the complete October 6 review. Requested `05_Papers_and_Learning/` and `09_Open_Loops/` are absent; canonical equivalents `05_Learning/` and `09_Planning/` were used. A vault-wide premise-filename search returned no artifact; broader research/planning searches found proposed deliverables, not a completed decision.

Recovered the final Assistant sections of the October 9 literature and funding conversations rather than relying on recursively embedded prompts. The actual [[Hermes/Conversations/2026-10-09/cron_b006ab3b7fec_20261009_130052|funding output]] reports an incomplete check, not no changes. The current [[02_Projects/AIVC/literature/2026-10-09-literature-radar|literature note]] is present and readable in the canonical vault.

Fresh external checks: bioRxiv HTML returned HTTP 429; its public API supplied the Mechanisms Matter v3 and VINTER v1 abstracts/version records. The arXiv API and HTML supplied LCD v1. These checks support the narrow claims below, not independent reproduction or a complete methods audit. The direct NIA K99 page returned HTTP 405. An official NIH K99 overview was retrieved, but it does not close the NIA-specific funding-monitoring gap. No current NIA deadline, eligibility determination, funding change, or absence of change is asserted.

| Evidence area | Change versus October 6 | Readiness consequence |
|---|---|---|
| Aging/AD premise and access | Still an open task; no completed premise/commit/no-go found | Dominant blocker unchanged |
| AIVC execution | Results note still confirms no finalized benchmark/result set | No improvement established |
| GeneBridge | Historical assets remain documented; current-output verification not supplied | Preparation, not newly verified results |
| Literature | New transport and neighborhood-editing comparators | Narrower defensible novelty claim; new evaluation requirements |
| Funding | October 9 check incomplete; only general NIH overview recovered here | NIA-specific status remains unverified |
| Training and independence | No new assay, co-mentor, ownership or portability commitment found in reviewed notes | Unchanged |

**Status: STAGNANT, not GETTING WEAKER.** The literature increases competitive pressure, but no new result directly disproves the project. It does not justify mechanically worsening the score. Repeated plans also do not justify improving it.

# SIGNIFICANCE — 7

**Why should NIA care?** A convincing proposal would explain how a defined aging/AD-associated environment changes a consequential response in a specified neural/glial population, and why predicting that modification would change an experiment or mechanistic conclusion. “Virtual cells can eventually help AD” does not establish that premise.

The actual [[01_Research/research-overview|research program]] is centered on SCZ DLPFC spatial genomics. An age covariate, brain tissue, or inflammatory annotation does not itself establish an aging mechanism. Chronological aging, AD pathology, acute exposure and disease-associated cell state are different constructs. A proposed acute exposure must be justified as modeling a specific component of AD biology, not a complete substitute for aged human tissue.

**SCZ should supply methodological preparation, not a co-equal disease aim.** GeneBridge can demonstrate donor-aware spatial measurement and a conditional-prediction pilot. A second disease aim is justified only by a prespecified shared mechanism and affordable transport test. Otherwise it makes the NIA story unfocused. If the best-supported biological question remains SCZ, retain it rather than changing disease labels to chase institute fit.

# INNOVATION — 6

The defensible opportunity is **measured context-dependent response prediction with explicit limits on when responses transport**. An identity encoder, neighborhood attention, imputation and conditional VAE are implementation choices, not demonstrated novel capability.

## New literature pressure

1. **Editable neighborhood inputs are not sufficient novelty.** VINTER's retrieved abstract describes a model reading histology, measured expression and neighborhood together, with molecular evidence editable while holding the image fixed.[3] This overlaps with the broad idea of interrogating neighborhood-conditioned predictions. It does not prove equivalence to AIVC's activity/perturbation endpoint. Different endpoints must not be collapsed into a leaderboard comparison. The October 9 radar's detailed DLPFC split criticism was not freshly rechecked against full text here; it is not needed to establish this narrower overlap.
2. **Representation similarity is not evidence of response transport.** Mechanisms Matter v3 frames cross-context generalization around shared causal mechanisms and reports a cross-context gap often reaching simple-baseline performance in its evaluated systems.[2] That is author-reported evidence, not a universal impossibility theorem. The same abstract describes response-diversity diagnostics aimed at detecting mode collapse missed by per-perturbation metrics.[2] AIVC should therefore test whether different perturbations and contexts produce distinguishable, correct response contrasts, not merely accurate average expression.
3. **Mechanistic response modeling is established competing work.** LCD v1 reports unseen-combination distributional prediction and explicitly limits its CLIPR causal-identification guarantee to linear drift.[4] This is a useful comparator when the endpoint and data permit it—not permission to call attention weights causal, or evidence of unrestricted new-target/tissue transfer. The primary source checked here is the January arXiv version; the radar's October journal publication is not treated as first disclosure.

**Reviewer-challenged claims:** “universal,” “causal counterfactual,” “dynamics from static atlases,” “first identity–environment virtual cell,” and “therapeutic prioritization.” Each needs a bounded domain, matching evaluation and evidence beyond reconstruction. Do not add VINTER/LCD-sized implementation obligations to rescue novelty; first show a biological prediction gap that a small model can address.

# CENTRAL HYPOTHESIS

The current design supports a testable conditional-prediction premise—environment may add activity information beyond identity—but not a frozen NIA-specific central hypothesis.

**Proposed central hypothesis, not an adopted project fact:**

> In one prespecified human neural/glial population, a defined AD-associated inflammatory exposure modifies the response to a limited gene-perturbation class; pre-intervention neighborhood programs predict this modification across held-out donors beyond cell identity and the shared perturbation effect, and controlled exposure manipulation reproduces the predicted direction of a prespecified response program and functional endpoint.

This is stronger because it specifies an interaction and a falsification route. It is still incomplete until population, exposure, perturbation, timing, endpoint, meaningful effect and assay access are selected. Inflammation is a candidate narrowing strategy, not evidence already obtained.

Falsification: a precisely estimated negligible interaction, no meaningful incremental context value with a sensitive endpoint, or a successful controlled manipulation contradicting the registered prediction. Failed manipulation, poor support, or imprecise estimates are inconclusive. A successful simple baseline may support the biology while refuting the need for the proposed architecture.

# SPECIFIC AIMS

No finalized Specific Aims page is documented. Proposed restricted structure:

| Aim | Measurable deliverable | Independence and fallback |
|---|---|---|
| **K99 Aim 1: quantify context-dependent response in one system** | Verified data/access contract; locked donor splits; simple baselines; measured response contrasts; calibrated uncertainty and context-value test | Keep the simplest supported predictor. A null premise is reported rather than hidden by changing targets |
| **K99 Aim 2: experimentally test a limited context × perturbation interaction** | Assay commitment; manipulation checks; registered transcript/program and functional endpoints; biological replication | Include a biologically justified contrast selected independently of Aim 1 model rankings, so validation does not require an architecture win |
| **R00 direction: transport and delimit a supported response mechanism** | One external donor/context shift; measured replication; prespecified support/abstention rule; candidate-controlled resources | Narrow transport scope if it fails; a mechanism-based fallback must be possible without universal transfer |

These aims are connected but not fully independent: all depend on access to a valid biological system. That shared prerequisite must be resolved before submission. An independently motivated assay contrast reduces algorithmic dependence; it does not solve absent assay access. Atlas curation, a portal, new foundation-model training, multimodal generation and prospective biology cannot all be mandatory aims.

# APPROACH — 8

## 1. Separate the estimands

```text
Conditional activity: m(c,e,x) = E[Y | C=c, E=e, X=x]
Model-input contrast: m(c,e',x) - m(c,e,x)
Intervention contrast: E[Y(e') - Y(e) | baseline C=c, X=x]
```

The PDF's identity-matched swap compares different observed cells; it is not paired counterfactual ground truth. Donor, layer, disease state and technical effects can remain confounded after embedding matching. Identity measured after exposure may encode a mediator or response. Disjoint input/target genes alone do not establish disentanglement. A full-rank design establishes algebraic estimability, not causal identification or adequate overlap.

The diagram's environment-only, perturbation-only and joint queries need separate support. Unpaired spatial and dissociated Perturb-seq collections do not automatically identify an environment-by-perturbation interaction. A zero perturbation embedding is not a measured control in every environment. Static snapshots do not establish temporal dynamics.

## 2. Data, leakage and generalization

- Split donors and linked modalities/sections before feature selection, response-program discovery, imputation, alignment and tuning. Audit reference/pretraining overlap; disclose unknown overlap.
- Define deployment-available inputs. Observed neighbors in a new tissue can be legitimate for conditional activity prediction. Their post-treatment responses cannot predict the same unobserved future response as if available at baseline.
- Separate donor, gene, perturbation, context and platform holdouts. A gene-held-out reconstruction result is not donor generalization; unseen combinations of known interventions are not unseen-target prediction.
- Exclude focal cells from neighborhoods. Audit segmentation spillover, density, boundaries, layer structure and technical spatial autocorrelation.
- Verify cross-modal donor identity, tissue section and registration separately. [[02_Projects/GeneBridge/datasets|The dataset note]] explicitly warns that matching donor labels does not establish aligned sections.
- Use measured targets for primary evaluation. Predicting an imputer's pseudo-labels may demonstrate imitation of the imputer, not biological recovery.
- Tabulate donor × context × perturbation support, matched controls, dose, time, batch and platform. No causal claim survives context perfectly confounded with cohort or platform.
- Use actual biological replicates for uncertainty. The October 7/9 radar candidates may inform sensitivity analyses or assay precedents; neither a mouse-liver precedent nor synthetic sample variation establishes this project's aging/AD system or independent donors.

These are risks in a proposed design, not implementation bugs verified in running code. Source: [[02_Projects/AIVC/project-outline]].

## 3. Statistical plan and baselines

For a measured-target GeneBridge engineering pilot, freeze:

```text
M0: Y_u = alpha + B_C C_u + B_X X_u + epsilon_u
M1: Y_u = alpha + B_C C_u + B_E E_u + B_X X_u + epsilon_u
DeltaL_d = L_d(M0) - L_d(M1)
```

Use nested donor-grouped tuning of regularization. C is permitted identity information, E a prespecified numeric context summary, and X deployment-available covariates. Include training-fold means, cell-type/layer means and unstratified pooled context. A small nonlinear extension follows only if the question requires it. Freeze target genes/programs, normalization, neighborhood rules and tuning budgets before protected testing.

For actual intervention measurements on a common declared scale:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
Interaction_p = E_d[Delta_d,e1,p - Delta_d,e0,p]
Functional endpoint: F ~ context * perturbation + batch + (1 | donor)
```

The expression for the interaction assumes the required donor/context support or a justified alternative design. The actual assay determines response family, nesting, assignment unit and estimable covariates. Random intercepts cannot repair complete confounding. Spatial interference may require culture/region-level assignment and analysis; receiver cells are not independent interventions.

Report final-state accuracy, shared perturbation effects and context-specific response recovery separately. Propagate uncertainty from treated and control groups. Use positive/sensitivity and negative controls. Prespecify meaningful effect and interval-width targets from pilot variance rather than importing arbitrary improvement percentages.

## 4. New transport and model-use safeguards

- **Do not build a retrospective “transfer-confidence” gate.** Response concordance computed using final test outcomes may explain a failure after the fact, but cannot be deployed to forecast that same response. If target responses are allowed for calibration, identify a separate calibration subset and give comparators equivalent access. Freeze gate thresholds before final scoring.
- **Evaluate diversity without rewarding noise.** Correct mean expression can coexist with near-identical predicted perturbation responses. Compare response contrasts with a shared-response baseline and a null-calibrated diversity diagnostic, while checking accuracy/calibration. More varied predictions are not automatically more correct. This is a proposed evaluation addition, not a claim that AIVC currently exhibits mode collapse.
- **Separate refitted ablations from fitted reliance.** Refitting without context tests incremental information; replacing context in a frozen model tests reliance under that replacement distribution. Attention magnitude or output movement alone establishes neither usefulness nor a mechanism.
- **Do not require every gain to vanish after a shuffle.** The October 5 strategy's disappearance criterion is too absolute: a support-matched replacement can preserve correlated information or leave other predictive inputs intact. Specify what the replacement destroys, retain support checks, and interpret the loss change jointly with refitted ablations. A surviving gain warrants investigation; it is not by itself proof of leakage.
- **Do not treat cross-validation folds as independent replications.** Overlapping training sets make “four of five folds” a stability heuristic. Distinguish donor-level variation conditional on fitted models from uncertainty in the entire selection/training pipeline; refit in resampling if that broader uncertainty is claimed.

The PDF's attention notation, sparsity objective and the diagram's VAE posterior/prior remain incompletely specified. L1 on normalized nonnegative attention would be constant, but that exact implementation has not been documented. These specification issues are secondary to the missing biological system.

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. **Documented cortical spatial-genomics experience and GeneBridge infrastructure:** Xenium/Visium/snRNA-seq context, donor/layer metadata, gene-fold workflows and downstream-analysis experience. These are documented assets, not fresh inspection of underlying HPC files.
2. **Historical GeneBridge analyses:** metadata recovery, donor-layer pseudobulk and diagnosis analyses are recorded. Current-file verification is explicitly outstanding. No historical DE counts or method ranking are promoted to newly verified results.
3. **A concrete AIVC proposed design:** the original outline and diagram define an identity/environment concept, candidate methods and evaluations. They establish planning progress, not a trained model or AD perturbation result.

Evidence: [[02_Projects/GeneBridge/current-state]], [[02_Projects/GeneBridge/experiments-and-results]], [[02_Projects/GeneBridge/methods]], [[02_Projects/AIVC/project-outline]]. The incomplete remembered donor-list warning remains unresolved.

## WHAT IS STILL MISSING

- A selected aging/AD population, exposure, intervention and measured endpoint with verified data support and assay access.
- Versioned AIVC code/configuration, donor/fold manifest, leakage audit, simple baseline predictions, controls and quantitative results.
- A prospective or genuinely independent measured response-validation route, with manipulation checks and biological-unit precision planning.
- A current GeneBridge disease-effect preservation/null-calibration package, not reconstruction alone.
- Named development commitments, candidate ownership and a portable R00 launch plan.

[[02_Projects/AIVC/experiments-and-results|The AIVC results note]] still states that no finalized benchmark/result set is confirmed. New papers, reviews and proposed aims are not preliminary data.

# CAREER DEVELOPMENT

NIH's general K99 overview describes a transition from mentored research to independent faculty research; the application must explain why this specific development period is necessary.[5] This does not establish Asad's eligibility: the same official page directs applicants to opportunity-specific eligibility requirements.[5]

The credible training need is **moving from observational spatial genomics to experimentally grounded response inference**, not generic exposure to Transformers.

| Development gap | Required commitment | Observable milestone |
|---|---|---|
| Aging/AD mechanism | Named system-relevant co-mentor | Defensible population/exposure/endpoint premise |
| Intervention biology | Assay mentor/collaborator, access, responsibilities and protected training | Successful manipulation and variance pilot |
| Identification/transport | Statistical/causal mentorship | Estimand, support/confounding audit and honest transport limits |
| Reliable biological ML | Protected evaluation and replicate-aware inference training | Reproducible benchmark with sensitivity controls |
| Independent leadership | Grantsmanship, supervision, ownership and resource negotiation | Candidate-owned question and portable R00 package |

No reviewed note establishes these commitments. Add named people, meeting cadence, effort, activities and measurable milestones. Investigator 6 reflects incomplete application evidence, not a definitive ability judgment; a full biosketch/publication review was not performed. Environment 5 reflects undocumented project-specific access and commitments, not a negative assessment of Emory facilities.

# INDEPENDENCE

[[00_Profile/collaborators-and-roles|Mentor context]] emphasizes multi-view, multi-section and multi-sample spatial integration. Another integration platform may read as an extension of the mentor's program. The source PDF's “Thrust 3” title does not establish candidate ownership.

A plausible independent niche is **experimentally tested context-dependent response inference and its limits**. Make candidate versus mentor questions, code/data rights, manuscript boundaries, portable compute/data and durable assay partnerships explicit. The R00 cannot depend on access that ends on departure.

- **R01 trajectory:** a supported response mechanism, replicated interaction and consequential functional endpoint.
- **NSF CAREER trajectory:** generalizable prediction/transport/uncertainty methodology linked to a concrete education program.
- **Independent faculty program:** one coherent question with expandable biological settings, not a list of architectures and diseases.

These are possible trajectories, not current funding or eligibility determinations.

# NIH-STYLE SCORES

| Criterion | Score (1 best; 9 worst) | Reason |
|---|---:|---|
| **Overall Impact** | **8** | NIA premise, execution, validation access and transition package remain unsupported |
| Significance | 7 | Potential importance; no selected aging/AD mechanism and consequential endpoint |
| Investigator | 6 | Relevant preparation; targeted development package and full application evidence absent |
| Innovation | 6 | Validated context-response transport could distinguish; component assembly and input edits do not |
| Approach | 8 | No established data contract/results; identification, leakage, calibration and validation risks |
| Environment | 5 | Specific assay access, mentorship commitments and portable resources undocumented |

All scores are unchanged from October 6. Overall impact is not calculated by averaging criteria.

# TOP 3 STRENGTHS

1. Documented human cortical spatial-genomics experience and a donor-structured GeneBridge foundation.
2. A concrete identity/environment design that can be tested cheaply with measured targets and simple baselines.
3. A potentially independent niche linking context prediction to experimentally measured response biology, rather than integration alone.

# TOP 3 MAJOR RISKS

1. **NIA premise and feasibility:** no selected aging/AD question with an accessible response-validation system.
2. **Evidence mismatch:** observational activity prediction, input edits or aligned embeddings may be sold as causal intervention prediction or transport.
3. **Execution and ownership:** architecture scope outruns results; assay access, training commitments and candidate-controlled R00 resources remain unresolved.

# TOP 3 EXPERIMENTS I SHOULD PRIORITIZE

## 1. Measured-outcome context-value and transport-failure test

After selecting a feasible system, compare identity/shared-response baselines against simple context-conditioned models under protected donor/context splits. Separate final-state, shared-response and interaction endpoints; include sensitivity controls and biological-unit uncertainty. For intervention data, test whether predicted response diversity is correct rather than merely nonzero. Any target calibration must be distinct from final testing.

**Output:** data contract, folds, baseline predictions, context-value effect and uncertainty, calibration/control results and advance/stop/inconclusive decision. If only GeneBridge is accessible, conduct the measured-activity SCZ pilot and label it conditional-prediction engineering—not aging/AD, perturbation or causal evidence.

## 2. GeneBridge disease-effect preservation and null calibration

Verify method versions, output paths, donor/exclusion manifests and gene folds. Compare measured versus held-out-gene imputed values on the same declared normalized scale and common gene universe:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Freeze the formula after rank/confounding checks; add run/slide only if justified and estimable. Assess diagnosis coefficient direction, magnitude, calibration and uncertainty, with covariate-aware donor-level null resampling. Never use cell permutations as independent diagnosis randomizations. Report the full eligible gene universe; nominal-significance-selected sign concordance is secondary and selection must be accounted for in inferential resampling.

**Output:** traceable manifests, coefficient-concordance and null-calibration results, and a bounded conclusion about downstream use. A reconstruction winner need not preserve disease effects.

## 3. Controlled context × perturbation pilot

Secure one neural/glial system and one independently motivated biological contrast. Randomize/control exposure and perturbation where feasible; verify manipulation; freeze predictions; measure a response program plus functional endpoint with independent biological replication. Match assignment and analysis to interference and nesting.

**Output:** assay/access commitment, pilot-based precision plan, measured interaction with uncertainty, and comparison to the registered prediction. Failed manipulation is not model falsification. Missing access is blocked feasibility, not permission to substitute an in-silico experiment.

# ONE-SENTENCE FUTURE-LAB VISION

My laboratory will develop and experimentally test reliable models of how tissue environments shape cellular responses in aging human neural systems, with explicit limits on transport across donors and biological contexts.

This is a proposed NIA-oriented vision, not a replacement for the canonical SCZ program.

# NUMBER-ONE ACTION THIS WEEK

**Within two working days, close the aging/AD premise-and-access decision.** Produce `aging_AD_AIVC_premise_v1.md` naming one population, exposure, perturbation class, measured endpoint, donor-resolved support and a feasible named validation route; conclude **commit/no-go**. Include confounding/overlap reasoning and an explicit distinction between baseline, calibration and final-test information. If nothing passes, document the minimum collaborator-generated pilot and stop presenting the NIA branch as computationally ready.

The new literature sharpens the information-access contract, but does not replace this action. No completed premise, assay commitment or experiment is claimed in this review.

## Verification and provenance

- No canonical goal, historical result, mentor commitment or proposed aim was promoted to an established fact.
- Local claims use vault wikilinks. Primary external claims use a task-specific citation ledger with retrieved evidence; author-reported results are not reproduced results.
- Current NIA funding coverage remains incomplete; the general NIH overview does not establish NIA-specific eligibility or deadlines.
- No model training, HPC-output verification or wet-lab experiment was performed during this review.
- Citation ledger and source extracts: `/opt/data/cache/citations/aivc-review-2026-10-10/`.
- Full review is saved in the canonical vault; scheduled delivery is limited to overall score, biggest weakness and the number-one action.

## Sources

[2] https://api.biorxiv.org/details/biorxiv/10.64898/2026.05.08.723625
    > "Predicting cellular responses to perturbations across biological contexts is central to drug development, yet deep learning models often fail to outperform simple baselines."
    > "Leveraging causal transportability theory, we show that cross-context generalization is governed by shared causal mechanisms, not merely distributional similarity."
    > "Further, we adapt the Vendi score to the perturbation setting to quantify effective response diversity and diagnose mode collapse, a failure mode invisible to standard per-perturbation metrics."
    > "Extensive experiments across six deep learning models and five simple baselines on semi-synthetic and real Perturb-seq datasets reveal a cross-context generalization gap: performance under cross-context splits drops substantially, often to simple baseline levels."
[3] https://api.biorxiv.org/details/biorxiv/10.64898/2026.10.01.752251
    > "Spatial transcriptomics links gene expression to tissue structure, yet current models learn embeddings whose meaning is assigned afterwards or read histology without measured expression."
    > "Here we introduce VINTER, a generative vision-language model aligned on 1.45 million histology-caption pairs that reads histology, measured gene expression and spatial neighbourhood as one sequence."
    > "It returns the probability of every tissue class, and because genes enter as text, its molecular evidence can be edited with the image held fixed."
[4] https://arxiv.org/html/2601.15341v1
    > "CLIPR provably identifies causal effects under a linear drift assumption"
    > "LCD outperforms established approaches in predicting the distributional shifts of unseen perturbation combinations in single-cell RNA-sequencing screens while simultaneously learning a mechanistic dynamical system of gene regulation."
[5] https://grants.nih.gov/funding/activity-codes/K99 — NIH K99 activity-code overview
    > "This program is designed to facilitate a timely transition of outstanding postdoctoral researchers or clinician-scientists from mentored research positions to independent, tenure-track or equivalent faculty positions, and to provide independent NIH research support during the transition that will help these individuals launch competitive, independent research careers."
    > "Carefully read the Eligibility section of the funding opportunity for opportunity-specific PD/PI eligibility requirements."
