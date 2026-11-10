---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-10-17
last_updated: 2026-10-17
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-10-11-NIA-K99-study-section-review]]"
new_project_results_verified: false
material_methodological_update: true
---

# AIVC as a potential NIA K99/R00 — skeptical review

## Bottom line

**Overall Impact: 8/9. Status: STAGNANT relative to October 11.** The reviewed record still does not establish an executable aging/AD biological premise, an AIVC benchmark result, or a committed response-validation route. New literature sharpens the required controls; it does not supply your preliminary data. The biggest weakness remains institute-specific premise and feasibility, not the choice of neural architecture.

**New methodological emphasis:** a donor-held-out neighborhood gain can still reflect reproducible measurement artifacts rather than biology. The first context-value experiment needs an assay-nuisance comparator and a plan for distinguishing technical spatial structure from biological context. This is a concrete addition to the prior review, not evidence that contamination has occurred in your implementation.

These are provisional document-based judgments, not actual NIH scores. Overall impact is not an average. Investigator and environment scores have limited confidence without a complete biosketch, candidate statement, letters, training plan and resource commitments. Absence from the reviewed notes does not establish that no work occurred elsewhere.

The authoritative scientific concept remains [[02_Projects/AIVC/project-outline|the user-supplied PDF and separate multimodal diagram]]. Neither establishes an adopted aging/AD focus. [[02_Projects/AIVC/goals|Canonical goals]] remain SCZ-centered. Every proposed hypothesis, aim and experiment below is a reviewer recommendation, not an approved scope change or an executed result.

## Evidence reviewed and limits

- AIVC: outline, overview, current state, goals, datasets, experiments/results and next actions.
- GeneBridge: current state, datasets, methods and experiments/results.
- Research overview/interests, learning goals/important papers, collaborators, active tasks and unanswered questions.
- [[09_Planning/weekly-strategies/2026-10-12-AIVC-GeneBridge-weekly-strategy|October 12 weekly strategy]] and the complete [[02_Projects/AIVC/reviews/2026-10-11-NIA-K99-study-section-review|October 11 review]].
- October 12, 14 and 16 literature notes, including their explicit retrieval and verification limitations.
- Actual final Assistant sections of [[Hermes/Conversations/2026-10-16/cron_b7fccc11fa73_20261016_100013|October 16 literature output]] and [[Hermes/Conversations/2026-10-16/cron_b006ab3b7fec_20261016_130050|October 16 funding output]], recovered from saved conversations because supplied context contained truncated prompts rather than usable conclusions.

The requested `05_Papers_and_Learning/` and `09_Open_Loops/` folders do not exist here; their canonical equivalents `05_Learning/` and `09_Planning/` were searched. A vault-wide premise-filename search returned no artifact, and the reviewed current project/task notes still leave the decision open. This is not an audit of unmounted HPC results or private communications.

**Literature provenance:** numbered citations below point to the retrieved internal radar reports. Their primary-source links and section/page provenance are available there. This review did not independently fetch the papers or reproduce their results. Abstract-level findings remain abstract-level. No numerical paper advantage is newly endorsed.

**Funding coverage:** the October 16 funding output explicitly says the check was incomplete and no verified funding alerts were generated. This does not mean there were no policy changes. Eligibility, deadline and current NOFO compatibility remain unverified here; no current administrative determination is made. See [[09_Planning/active-tasks#Funding|funding follow-up]].

## Comparison with the previous review

| Area | October 11 | October 17 evidence | Judgment |
|---|---|---|---|
| NIA premise/access | Unselected system and validation route | October 12 strategy requests closure; no completed premise found | Unchanged |
| AIVC results | No confirmed benchmark | Results note still planning-stage | Unchanged |
| GeneBridge evidence | Historical assets; current verification missing | Same warnings and unresolved inventory | Unchanged |
| Novelty and controls | Context prediction/transport already crowded | New reports strengthen simple multi-scale, assay-nuisance and downstream-response comparisons | Review specification improves; application evidence does not |
| SCZ versus aging/AD | Scope unresolved | SCZ-relevant sender/receiver literature provides a more specific alternative, not an NIA premise | Requires an explicit strategic choice |
| Career and independence | Commitments undocumented | No new named assay/training/portability package found | Unchanged |
| Funding monitoring | Incomplete October 9 check | October 16 also incomplete | Coverage gap persists |

**STAGNANT**, not IMPROVING. I am not worsening scores simply because more days passed or more competing papers appeared. The October 12 plan's closure target is not documented as met; that is an evidence-management and execution concern, not proof that the task was never attempted. Another review or strategy note does not count as progress on the experiment.

# SIGNIFICANCE — 7

## Why should NIA care?

A convincing NIA application must explain a specific aging/AD-related biological problem and why the proposed measurements and predictions change an experimental or mechanistic decision. “A spatial virtual cell could eventually help AD” is insufficient. Choose one population, one context, one limited intervention class and one consequential endpoint; establish that the chosen exposure actually represents the bounded aging/AD process being claimed.

Your documented core is cohort-scale SCZ molecular mapping in postmortem DLPFC. It provides preparation in spatial genomics, not aging/AD response evidence. Age as an adjustment covariate is not an aging experiment; brain tissue is not automatically AD-relevant; an acute inflammatory exposure is not equivalent to aged human tissue. Source: [[01_Research/research-overview]].

## Does SCZ provide breadth or dilute the proposal?

For an NIA proposal, retain SCZ/GeneBridge as methodological preparation or a tightly bounded secondary transport test. A co-equal SCZ aim would dilute the application unless a shared mechanism and feasible cross-context experiment are established.

The October 14 radar reports sparse neuronal C4 perturbation with neighboring-cell responses, but also warns that developmental mouse overexpression, bulk/reference projection and imaging do not supply a ready-made human single-cell spatial perturbation benchmark.[2] **Reviewer interpretation:** this is a more concrete motivation for the existing SCZ sender/receiver program than a generic AD label. It is not a reason to rebrand C4 work as aging. If that biological direction remains strongest, keep it and leave the NIA branch explicitly unready rather than forcing institute fit.

# INNOVATION — 6

The potentially distinct contribution is **reliable, experimentally checked context-dependent response prediction with explicit transport and measurement limits**. The component list—foundation-model identity encoding, spatial pooling/attention, perturbation embedding and conditional VAE—is not itself sufficient novelty.

### What the new literature changes

- The October 16 radar describes **stipple** as separating spatial measurement variation from biological variation, while acknowledging identifiability assumptions and warning against transferring a Visium capture model directly to Xenium.[3] **Implication:** assay nuisance is part of the scientific identification problem, not just a preprocessing footnote.
- The same radar describes **SpatialZoomer** as multi-scale spectral spatial feature extraction and reports observational AD-associated signals; its full results were not available to that review.[3] **Implication:** multiscale neighborhoods are not a sufficient innovation claim. Use inexpensive multiscale features as a fair comparator; do not infer intervention prediction from observational AD associations.
- The October 14 report identifies **BioMod** and **SPACER** as overlapping representation/context work, with incomplete full-method audits.[2] **Implication:** biological modules and interpretable neighborhood scores need endpoint-specific differentiation, not another architecture-combination claim.
- **CEE/RNA fingerprinting**, as assessed on October 12, distinguish downstream response evidence from target self-expression and ambiguous dictionary matching.[1] **Implication:** if target nomination enters the grant, evaluate forward response prediction and inverse target identification separately. Target masking defines a downstream-only diagnostic; it is not automatically the correct primary metric for all forward tasks.
- The October 16 report describes **CellNet** as an alternative identity/missing-gene encoder and **TAKO** as topology-based ranking rather than signed full-expression prediction.[3] **Implication:** encoder choice is replaceable infrastructure, and ranking baselines must be compared on ranking—not substituted for response calibration.

Do not implement all these methods now. Select the simplest relevant comparison with matched inputs, supervision, information access and tuning. A strong, bounded biological test can justify a small model. A complex model that reconstructs expression does not justify a mechanism claim.

Claims reviewers would challenge: “universal,” “causal counterfactual,” “dynamics from static snapshots,” “first identity–environment model,” “attention reveals mechanism,” and “therapeutic target discovery.” None is established by the current project evidence.

# CENTRAL HYPOTHESIS

The outline provides a testable conditional-prediction premise: local environment may contain activity information beyond cell identity. It does **not** document a frozen NIA-specific central hypothesis.

## One stronger central hypothesis — proposed, not adopted

> In one prespecified human neural/glial population, a defined AD-associated inflammatory exposure modifies the response to a limited gene-perturbation class; pre-intervention neighborhood programs predict this modification across held-out donors beyond identity, assay nuisance and the shared perturbation effect, and controlled exposure manipulation reproduces the predicted direction of a prespecified molecular response and functional endpoint.

This remains a hypothesis template until population, exposure, intervention, dose/time, endpoints and access are selected from evidence. Inflammation is a proposed narrowing device, not an observed result or an approved new disease focus.

**Falsification:** with successful manipulation, adequate support, a sensitive endpoint and sufficient precision, a negligible interaction or a response opposite the registered prediction challenges the hypothesis. Failed manipulation, insensitive metrics, low precision or unavailable data are inconclusive. If a simple predictor succeeds and attention adds nothing, the architecture rationale fails—not necessarily the biological premise.

# SPECIFIC AIMS

No finalized Specific Aims page was found in the reviewed project notes. Proposed structure:

| Aim | Measurable output | Independence and fallback |
|---|---|---|
| **K99 Aim 1: quantify context-dependent response in one accessible aging/AD-relevant system** | Data contract, donor/support audit, protected measured-response test, simple-model comparison, nuisance controls and uncertainty | Retain a valid simple predictor; do not change the endpoint to rescue the architecture |
| **K99 Aim 2: test one context × perturbation interaction experimentally** | Manipulation checks, independent biological replication, registered molecular and functional outcomes | Include a biologically motivated contrast chosen independently of model rankings, so a model failure does not erase the experiment |
| **R00 direction: establish where the supported mechanism and predictor transport** | One external donor/context shift, measured replication and a prespecified support/abstention rule | A transfer failure yields a bounded mechanism/transport result rather than a universal claim |

These aims connect logically and reduce algorithmic dependence. They are **not yet demonstrably feasible**: they share unresolved system and assay access. An independent biological contrast cannot fix missing access. Atlas curation, a portal, foundation-model training, multimodal generation and prospective response biology should not all be required K99 deliverables. The broad PDF's resource-building thrust can be supporting infrastructure rather than a stand-alone grant aim.

# APPROACH — 8

## 1. Distinguish estimands and permitted information

```text
Conditional activity: m(c,e,x) = E[Y | C=c, E=e, X=x]
Model-input contrast: m(c,e',x) - m(c,e,x)
Intervention contrast: E[Y(e') - Y(e) | baseline C=c, X=x]
```

These are different. The PDF's identity-matched swap pairs different cells; it does not observe both potential outcomes of one cell. Matching cannot by itself remove donor, disease, layer or assay confounding. Identity genes/embeddings may encode post-exposure mediators or target information. Disjoint identity and activity gene sets do not prove disentanglement. Source: [[02_Projects/AIVC/project-outline]].

For prediction in a new measured tissue, its observed neighborhoods can be legitimate inputs. For predicting an unobserved perturbation response, those same post-treatment measurements cannot be treated as pre-treatment inputs. Freeze the intended deployment information before constructing the benchmark.

The diagram's environment-only, perturbation-only and joint queries require distinct support. Unpaired spatial snapshots and dissociated Perturb-seq do not automatically identify the joint response. A zero perturbation code does not establish a measured control. Full-rank regression is not causal identification or adequate overlap. Static snapshots do not supply temporal response trajectories.

## 2. New requirement: separate biological context from assay structure

**Reviewer-proposed comparison**, using measured targets and identical protected donor splits:

```text
M0: Y_u = alpha + B_C C_u + B_X X_u + epsilon_u
MQ: Y_u = alpha + B_C C_u + B_X X_u + B_Q Q_u + epsilon_u
MQE: Y_u = alpha + B_C C_u + B_X X_u + B_Q Q_u + B_E E_u + epsilon_u
Primary added-context contrast: DeltaL_d = L_d(MQ) - L_d(MQE)
```

C is permitted identity information, X prespecified biological/design covariates, Q independently justified assay/QC information, and E a fixed neighborhood summary. Ridge regularization and transformations are training-selected. Compare MQE with both the strongest nuisance-aware simple baseline and an unstratified pooled-context model, not only M0.

- Audit available QC, cell area/segmentation, slide/run, tissue-edge and spatial detection patterns. Do not assume every QC covariate exists or is purely technical.
- A nuisance field estimated from final-test target expression can leak the answer. Total counts containing masked target genes can also violate a held-out-gene contract. Use target-independent measurements or explicitly permitted observed-input genes, with frozen fitting rules.
- Do not automatically regress out density, morphology or spatial structure: they can carry real exposure effects. Specify a measurement/confounding rationale and report sensitivity to adjustment. Loss of gain after adjustment can reflect overadjustment as well as technical confounding.
- Nuisance and biology may be non-identifiable from counts alone. An orthogonal assay, technical replicate or controlled exposure is stronger evidence than residualization alone.
- Donor holdouts do not remove a technical gradient that recurs across donors. Cross-assay validation adds evidence but must not confound assay with disease/context.

This is a control specification, **not** a demand to add a new neural nuisance branch or adopt stipple unchanged.

## 3. Leakage, data and generalization audit

- Split donors and linked samples/modalities before learned feature selection, normalization, imputation, alignment, module construction and tuning. Freeze permissible deterministic processing of new samples separately from fitted adaptation.
- Audit reference/pretraining overlap. Unknown overlap must be disclosed, not declared absent. Holdout genes, donors, perturbation targets, contexts and platforms answer different generalization questions.
- Exclude the focal cell from its neighborhood. Check segmentation spillover, cortical boundaries, neighbor counts and radius sensitivity.
- Resolve donor and section identity separately; a matching donor is not spatial registration. The [[02_Projects/GeneBridge/datasets|GeneBridge inventory]] still warns that its remembered donor list is incomplete.
- Make measured targets primary. Agreement with imputed pseudo-labels may reproduce the teacher rather than biological truth. Keep imputation fold-local and assess its uncertainty.
- Tabulate context × perturbation × biological-unit support, controls, dose/time, batch and platform. A donor random effect cannot repair complete context–cohort confounding.
- Evaluate transport under bounded shifts and report support gaps/abstention. Many cells do not replace biological replication.

## 4. Response inference and statistical weaknesses

For a supported factorial experiment on a declared common scale:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
Interaction_p = E_d[Delta_d,e1,p - Delta_d,e0,p]
F_d,b,r = beta0 + betaE E + betaP P + betaEP E*P + gamma_batch + b_d + epsilon_d,b,r
```

The last expression is an illustrative Gaussian mixed model for a continuous functional endpoint, not a frozen analysis for unknown data. Choose the response family, nesting and covariance structure to match the actual assay. Randomize at the appropriate culture/region unit when cells interfere; independent cells within the same treated culture are not independent treatment assignments. Propagate treated/control uncertainty.

Report final-state accuracy, shared perturbation effects and context-specific response recovery separately. Pair response diversity with accuracy and null calibration. Estimate biological-unit uncertainty and practical effect size, not just a significant cell-level p-value.

Use positive/negative sensitivity controls fixed before final testing. A metric unable to distinguish its controls cannot establish model equivalence or refute the premise. Keep outcome-informed calibration distinct from deployment predictors and protect the final test.

The October 12 strategy's four-of-five-fold and significance thresholds remain **proposed heuristics**, not approved standards. Folds share training observations; fold wins are not independent replication. A confidence interval above zero is not sufficient evidence of a biologically important improvement. Establish meaningful effect/precision criteria from pilot variance and disclose whether bootstrap inference conditions on trained models or repeats the full selection pipeline.

Refitted no-context ablation tests added information. Frozen-checkpoint context replacement tests reliance under the declared replacement distribution. A support-matched shuffle that preserves predictive proxies need not erase all gain; neither residual gain nor output movement alone identifies leakage or biology.

## 5. Architecture specification gaps

Clarify identity markers versus housekeeping genes, the PDF's undefined attention dimensions, its sparsity objective, the diagram's conditional-VAE posterior/prior and how the identity loss enters total loss. L1 cannot sparsify normalized nonnegative softmax weights, but the source never specifies L1; this is a conditional warning, not a confirmed implementation bug. Keep the PDF and diagram distinct until an implementation is chosen. Source: [[02_Projects/AIVC/project-outline]].

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. **Documented preparation:** cohort-scale human cortical spatial-genomics work, metadata/QC, donor–layer analysis and held-out-gene evaluation design. Sources: [[01_Research/research-overview]], [[02_Projects/GeneBridge/methods]].
2. **Historical GeneBridge assets:** recovered slide/run metadata, pseudobulk and diagnosis analyses with referenced files/jobs. Their current values and final model rankings remain explicitly marked for verification. Source: [[02_Projects/GeneBridge/experiments-and-results]].
3. **A concrete AIVC design:** identity/environment decomposition, baseline spatial prediction and an expanded multimodal perturbation architecture. This is design evidence, not preliminary performance. Source: [[02_Projects/AIVC/project-outline]].

## WHAT IS STILL MISSING

- One selected aging/AD premise with verified access, biological-unit support and independent validation.
- A registered AIVC run: code/configuration, donor and gene manifests, leakage audit, measured predictions, nuisance controls, uncertainty and advance/stop/inconclusive decision.
- Current-file verification of GeneBridge outputs and disease-effect preservation/null calibration, beyond reconstruction.
- Measured context-dependent perturbation evidence and a functional validation endpoint.
- Named aging/AD and experimental mentorship, specific training commitments, ownership and portable R00 resources.

[[02_Projects/AIVC/experiments-and-results|The results note]] still states that no finalized AIVC benchmark/result set is confirmed. No numerical GeneBridge result or method ranking is newly certified. External papers, reviews and diagrams are not your preliminary data.

# CAREER DEVELOPMENT

A credible K99 need is the transition from observational spatial genomics to experimentally grounded inference about context-dependent responses. “Learn GNNs and transformers” alone is too generic and disconnected from the proposed biological deliverable.

| Training gap | Required documented plan | Milestone |
|---|---|---|
| Aging/AD biology | Named system-relevant co-mentor, activities and feedback | Defensible premise, endpoint and disease-model boundaries |
| Perturbation/functional experimentation | Assay mentor, responsibilities, protected access and effort | Successful manipulation/variance pilot and registered validation |
| Identification and transport | Quantitative mentor tied to actual design | Estimand, confounding/support audit, valid uncertainty and external test |
| Measurement-aware biological ML | Training in assay error, information boundaries and reproducibility | Nuisance-aware measured-target benchmark |
| Independent leadership | Grantsmanship, supervision and ownership planning | Candidate-controlled R00 launch package |

The [[05_Learning/learning-goals|learning goals]] establish relevant interests, not a committed career-development program. [[00_Profile/collaborators-and-roles|Jian Hu is documented as the current advisor]]; do not invent an aging/AD co-mentor or assume collaborator assay access. Investigator 6 reflects incomplete application evidence, not a definitive assessment of capability. Environment 5 reflects missing project-specific commitments, not a negative judgment of Emory's general resources.

# INDEPENDENCE

The documented mentor program includes multi-view/multi-section/multi-sample spatial integration. A new integration platform alone may look like continuation rather than a candidate-owned laboratory. The PDF's “Thrust 3” title does not settle authorship or ownership. Source: [[00_Profile/collaborators-and-roles]], [[02_Projects/AIVC/project-outline]].

Define the candidate-owned question, mentor overlap, code/data and manuscript boundaries, permitted portable resources, and assay partnerships that persist after departure. The R00 must not rely on access that terminates with the postdoc.

- **R01 potential:** a reproducible context-dependent mechanism connected to functional consequences, supported across bounded systems.
- **NSF CAREER potential:** general methods for measurement-aware prediction, transport and uncertainty with a substantive education program; this is a possible trajectory, not an eligibility determination.
- **Faculty-program potential:** a persistent scientific question about when tissue context changes cellular response—not an expanding list of model architectures and diseases.

At present the record suggests a possible future laboratory, not a documented independent launch plan.

# NIH-STYLE SCORES

| Criterion | Score | Rationale |
|---|---:|---|
| **Overall Impact** | **8** | NIA premise/access, executed response evidence and independence package unresolved |
| Significance | 7 | Important potential problem; aging/AD mechanism and endpoint not selected |
| Investigator | 6 | Relevant preparation; targeted training and ownership evidence incomplete |
| Innovation | 6 | Validated transport/response contribution possible; generic architecture crowded |
| Approach | 8 | No verified AIVC benchmark or data contract; identification, measurement and validation risks |
| Environment | 5 | Specific assay access, mentors and portable resources undocumented |

Scores unchanged from October 11. These are the requested mock criteria, not a claim that they exhaust the applicable K99 review framework. Candidate, career plan and mentor commitments remain central to this assessment.

# TOP 3 STRENGTHS

1. A documented cortical spatial-genomics foundation with donor-structured GeneBridge work that can demonstrate rigorous execution once current outputs are verified.
2. A concrete identity/environment premise that can be tested cheaply on measured targets before architectural expansion.
3. A potentially distinct program in experimentally tested context-dependent response and transport, rather than integration alone.

# TOP 3 MAJOR RISKS

1. **NIA fit and feasibility:** no selected aging/AD system with verified measured-response and assay access.
2. **Claim–evidence mismatch:** spatial prediction could reflect technical fields or proxies, while simulated contrasts are described as causal intervention effects.
3. **Execution and independence:** expanding model scope without a locked result package, committed training/validation team or portable candidate-owned R00 resources.

# TOP 3 EXPERIMENTS I SHOULD PRIORITIZE

## 1. Nuisance-aware measured-target context-value experiment

After the data/access gate, run M0, MQ and MQE plus simple pooled/multiscale context under identical nested donor splits. Use measured targets, focal-cell exclusion, target-independent nuisance information and sensitivity controls. Report paired donor-level loss differences, practical effect size, uncertainty and support-matched reliance diagnostics.

**Deliverable:** data/configuration manifests, reproducible predictions, biological-versus-technical sensitivity analysis and advance/stop/inconclusive decision. If only GeneBridge is available, label this **SCZ conditional-prediction engineering**—not aging/AD, perturbation or causal evidence. An unidentifiable technical/biological decomposition should be reported as such, not solved rhetorically with residualization.

## 2. GeneBridge disease-effect preservation and null calibration

Verify current method versions, donor/exclusion inventory, files and gene folds. On a common measured-versus-imputed gene universe, normalized scale and donor × layer units, assess diagnosis coefficient magnitude, direction and calibration using the proposed primary formula:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Freeze the estimable formula and repeated-donor implementation after a blinded rank/confounding audit; technical terms require justification and support. Compare all current methods, training-derived layer means and a verified nonspatial baseline. Use donor-level uncertainty and covariate-aware null resampling, not cell permutations. Repeat outcome-based gene selection inside inferential resampling when reporting selected subsets.

**Deliverable:** traceable manifest, coefficient-concordance and calibration figures, null report and manuscript-ready bounded conclusion. Reconstruction leadership is not automatically disease-effect preservation.

## 3. Controlled context × perturbation pilot

Secure one human neural/glial system and an independently justified contrast. Where feasible, randomize context and perturbation, verify manipulation, freeze predictions from a simple and context-aware model, and measure a response program plus a functional endpoint with independent biological replication. Use pilot variance for precision planning; match assignment and inference to culture/region nesting and interference.

**Deliverable:** named access commitment, protocol, manipulation controls and interaction estimate with uncertainty. Missing access is a feasibility block. The October 16 radar warns that its HSV-1 spatial example has one animal per condition and separate modality cohorts; that candidate must not be promoted to the sole confirmatory benchmark.[3]

# ONE-SENTENCE FUTURE-LAB VISION

My laboratory will develop and experimentally test measurement-aware models of how tissue environments shape cellular responses in aging human neural systems, with explicit limits on transfer across donors and contexts.

This is a proposed NIA-oriented vision, not a replacement for the canonical SCZ program.

# NUMBER-ONE ACTION THIS WEEK

**Close—not renew—the aging/AD premise-and-access decision.** Produce `02_Projects/AIVC/aging_AD_AIVC_premise_v1.md` with one population, context, perturbation class, measured endpoint, verified biological-unit support and named validation route, ending in **COMMIT** or **NO-GO**. Add an explicit assay-nuisance versus biological-context audit and the baseline/calibration/test information boundary. If no eligible system is supported, record the no-go and the minimum collaborator pilot needed; do not let architecture work substitute for this decision.

This is still the unresolved prior-week dependency. The new literature changes its technical acceptance criteria, not its completion status. No decision or commitment is made on the user's behalf by this review.

## Persistence and verification scope

The full review is saved in the canonical vault and indexed from AIVC overview/current state. Local evidence links and numbered radar citations are checked before delivery. No HPC experiments or biological results were executed or certified; no canonical scientific goals, dataset ownership or mentor commitments were changed. The substantive new information is the nuisance-aware context test and revised literature comparison; the score remains unchanged.

## Sources

[1] file:///opt/data/obsidian-vault/02_Projects/AIVC/literature/2026-10-12-literature-radar.md — AIVC Literature Radar — 2026-10-12 (internal report)
[2] file:///opt/data/obsidian-vault/02_Projects/AIVC/literature/2026-10-14-literature-radar.md — AIVC Literature Radar — 2026-10-14 (internal report)
[3] file:///opt/data/obsidian-vault/02_Projects/AIVC/literature/2026-10-16-literature-radar.md — AIVC Literature Radar — 2026-10-16 (internal report)
