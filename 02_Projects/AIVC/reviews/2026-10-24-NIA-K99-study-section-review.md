---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-10-24
last_updated: 2026-10-24
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-10-18-NIA-K99-study-section-review]]"
new_project_results_verified: false
material_update: true
material_update_type: literature-informed-review-not-project-progress
---

# AIVC as a potential NIA K99/R00 — October 24 review

## Verdict

**Overall Impact: 8/9. Status: STAGNANT compared with October 18.** The application still lacks a selected aging/AD biological question supported by verified data, an executable validation route, and a committed training/independence package. The reviewed record does not document a completed AIVC benchmark. Architecture refinement cannot substitute for these prerequisites.

These are provisional, document-based reviewer judgments—not an NIH decision, a funding forecast, or an average of criterion scores. Missing application evidence is not proof that no work occurred elsewhere.

**New since the previous review:** the October 21–23 literature reports materially narrow the architectural novelty claim and sharpen the required comparison: separate the contribution of spatial context, perturbation representation, and prediction head. This is a review update, not evidence of applicant progress.[1][2] The premise-and-access decision remains the first action; do not expand the immediate GeneBridge pilot to implement every new paper.

## Evidence and coverage

Canonical sources examined include:

- [[02_Projects/AIVC/project-outline]], [[02_Projects/AIVC/current-state]], [[02_Projects/AIVC/overview]], [[02_Projects/AIVC/goals]], [[02_Projects/AIVC/datasets]], [[02_Projects/AIVC/experiments-and-results]], [[02_Projects/AIVC/important-decisions]], and [[02_Projects/AIVC/todo-and-next-actions]].
- [[02_Projects/GeneBridge/current-state]], [[02_Projects/GeneBridge/datasets]], [[02_Projects/GeneBridge/methods]], and [[02_Projects/GeneBridge/experiments-and-results]].
- [[01_Research/research-overview]], [[01_Research/scientific-interests]], the relevant sections of [[05_Learning/important-papers]], [[05_Learning/learning-goals]], [[09_Planning/active-tasks]], [[09_Planning/unanswered-questions]], and [[09_Planning/future-plans]].
- [[00_Profile/identity-and-career]], [[00_Profile/collaborators-and-roles]], [[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]], and the October 18 review.
- October 21 and 23 literature reports in full; focused methods/results/limitations passages from the October 19 report. The October 23 funding conversation's actual final Assistant section was recovered rather than interpreting the recursively truncated prompt as a completed funding scan.[3]

The requested `05_Papers_and_Learning/` and `09_Open_Loops/` folders are absent; their canonical equivalents are `05_Learning/` and `09_Planning/`. A vault-wide filename search found no premise artifact. Current project and task notes continue to mark that decision as incomplete. No HPC execution, raw-data audit, or unpublished laboratory-record audit was performed.

**Provenance boundary:** literature claims below are attributed to the retrieved internal radar reports, not independently refetched primary papers or reproduced experiments. Their incomplete full-text audits remain limitations. The October 23 funding radar explicitly reports an incomplete check; this is not evidence of unchanged policy.[3] Current eligibility, deadlines, institute participation, and NOFO-specific review requirements remain unverified. This review makes no administrative eligibility determination.

## Comparison with October 18

| Dimension | October 18 | October 24 |
|---|---|---|
| Aging/AD premise and data access | Unresolved | Still unresolved in reviewed notes; no premise artifact found |
| Executed AIVC evidence | No confirmed benchmark | No confirmed benchmark |
| GeneBridge preliminary evidence | Historical outputs awaiting verification | No newly certified outputs |
| Innovation | Architecture alone insufficient | More direct competition; representation-versus-head controls now specifically motivated |
| Validation | Measured targets, nuisance-aware baselines, controlled response test | Same core requirements; stronger model-to-experiment comparator and explicit factorized benchmark recommendation |
| Training and independence | Commitments undocumented | No new commitment package found |
| Funding coverage | October 16 check incomplete | October 23 check also incomplete |

**Status: STAGNANT, not GETTING WEAKER.** Literature competition warrants revising the rationale, but does not by itself justify a worse score. Updated notes and more detailed proposed controls are documentation progress, not new preliminary data.

# SIGNIFICANCE — 7

### Why should NIA care?

A defensible NIA proposal would establish how a specific aging/AD-relevant tissue environment changes a defined cellular response, then show that the finding improves an experiment, mechanistic conclusion, or intervention-prioritization decision. The current notes do not select that population, context, intervention, or endpoint. “Virtual cells for brain disease” does not supply the missing biological premise.

The documented foundation is human postmortem SCZ/DLPFC spatial genomics. Adjusting for age does not turn a disease comparison into aging research; adding an AD paragraph does not supply an AD mechanism. An inflammatory exposure would need a specific disease rationale and stated model limitations, not an assumption that any inflammation is an AD model. Sources: [[01_Research/research-overview]], [[00_Profile/identity-and-career]].

### Does SCZ add breadth or create distraction?

SCZ supports the applicant's preparation and can provide an engineering test bed or a later bounded transport contrast. A co-equal SCZ disease aim in this NIA proposal would dilute the question unless a shared mechanism and feasible cross-context experiment are demonstrated. Keep the canonical SCZ program intact. A conclusion that the NIA branch is not ready is preferable to relabeling the strongest existing science. Source: [[02_Projects/AIVC/goals]].

# INNOVATION — 6

**Potentially novel:** experimentally validated prediction of a context-specific response, with measurement-aware uncertainty and explicit limits on donor/context transfer.

**Not sufficient:** a foundation-model cell encoder plus local attention, a perturbation embedding, and a conditional VAE. These are proposed components, not a demonstrated scientific contribution. The user-supplied PDF and diagram remain distinct specifications; neither is evidence of implementation. Source: [[02_Projects/AIVC/project-outline]].

### What the latest literature changes

| Reported work | Novelty or rigor challenge | Consequence for this proposal |
|---|---|---|
| Tessera | The October 21 report describes pretrained cell representations with geometry-aware spatial attention and masked expression training | Identity plus neighborhood attention is not a sufficient standalone innovation claim; reconstruction is still distinct from intervention prediction |
| Cole et al., revised perturbation-prediction preprint | The October 23 report describes strong prior-knowledge perturbation embeddings with simple predictors; some generative comparisons were evaluated only by mean response | Separate embedding quality from head complexity; a mean-only benchmark cannot settle distributional utility |
| GeoSinkhorn Flow | The report describes geometry-aware conditional population transport | Consider a distributional comparator only if the eventual endpoint is a response distribution; distinguish abundance from within-state change |
| DynaVelo | The report describes experimentally tested rescue predictions in mouse B cells | Model-to-experiment validation is a concrete comparator; it does not establish neural/AD feasibility |
| Gate-based importance study | The report describes a simulated EEG counterexample in which gate rankings disagree with retrained ablations | Prediction, predictive reliance, and causal mechanism must be evaluated separately; this is an analogy, not a direct failure of AIVC |

All descriptions in this table are attributed to the radar assessments and retain their evidence-depth and transfer limitations.[1][2]

**New discriminating comparison:** on a future eligible perturbation benchmark, hold cell-state/context inputs fixed while crossing perturbation embedding choices with simple versus complex response heads. Then ablate spatial context under equal information access. Otherwise an apparent AIVC gain can be attributed to a better perturbation representation rather than neighborhood reasoning. Cell-identity embeddings and gene-perturbation embeddings are not interchangeable.[2]

Do not require all these models for the first pilot. The immediate conditional-activity test should remain small and nuisance-aware. Reviewers would challenge “universal,” “causal counterfactual,” “dynamics from static snapshots,” “attention reveals regulation,” and “therapeutic discovery” without separate supporting experiments.

# CENTRAL HYPOTHESIS

A testable identity–environment premise exists, but a frozen NIA-specific central hypothesis is not documented.

## One stronger central hypothesis — proposed, not adopted

> In one prespecified human neural/glial population, a defined AD-relevant microenvironmental exposure modifies the response to a limited gene-perturbation class; baseline neighborhood programs predict the context-by-perturbation interaction across held-out donors beyond intrinsic cell state, assay nuisance, and the shared perturbation effect, and controlled manipulation reproduces the predicted direction of a prespecified molecular response and functional endpoint.

This is a hypothesis template, not a selected mechanism. Population, exposure, perturbation, dose/time, molecular program, and functional assay must be selected from accessible evidence. “AD-relevant” must be justified independently rather than inferred from the model.

**Falsification:** a sufficiently precise absence of the interaction, or reproducibly opposite response after successful manipulation, challenges the biological premise. A weak assay, failed manipulation, or wide interval is inconclusive. If a simple model succeeds while attention adds nothing, the architecture claim fails—not necessarily the biological hypothesis.

# SPECIFIC AIMS

No finalized Specific Aims page was identified. The following structure is a reviewer proposal, not an adopted project plan.

| Aim | Measurable deliverable | Independence and failure branch |
|---|---|---|
| **K99 Aim 1: quantify context-dependent responses in one accessible aging/AD-relevant system** | Frozen estimand, verified support/access, grouped splits, measured-response benchmark, simple baselines and calibrated uncertainty | Retain a valid simple model if the complex model fails; distinguish precise null from low precision |
| **K99 Aim 2: experimentally test one prespecified context × perturbation interaction** | Manipulation checks, independent biological replication, molecular and functional outcomes, frozen predictions | Include an independently motivated biological contrast rather than depending entirely on an Aim 1 top-ranked hit |
| **R00 direction: define where the response mechanism and predictor transfer** | One bounded external population/context test, replication, support diagnostics and abstention criteria | Prespecified transfer-failure analysis defines limits; it need not rescue a universal-model claim |

The aims are logically connected and can be measurable, but their feasibility is not established. Independent biological contrasts reduce algorithmic dependence; they do not remove shared dependence on access and assay capability. The R00 launch must have a usable baseline and accessible system even if the novel architecture fails. If the underlying biological premise fails, the response is a justified scientific revision—not pretending the original aims succeeded.

A portal, atlas harmonization, de novo foundation-model training, multimodal integration, unseen perturbations, and prospective rescue should not all be obligatory K99 deliverables.

# APPROACH — 8

## 1. Separate prediction from intervention

```text
Conditional prediction: m(c,e,x) = E[Y | C=c, E=e, X=x]
Model-input contrast: m(c,e1,x) - m(c,e0,x)
Intervention contrast: E[Y(e1) - Y(e0) | baseline C=c, X=x]
```

These are different estimands. Identity matching pairs different cells, not both potential outcomes of one cell. Identity markers or embeddings can encode disease activity, outcome information, or post-exposure mediators. Disjoint identity/target genes alone do not establish disentanglement. A fixed identity under an exposure change is a modeling assumption requiring sensitivity analysis.

Unpaired static spatial tissue and unrelated dissociated Perturb-seq do not automatically identify a joint environment-by-intervention response. The diagram's zero perturbation embedding is a code convention, not proof of a measured control. Static snapshots do not establish time-resolved dynamics. Source: [[02_Projects/AIVC/project-outline]].

## 2. Declare the information contract and block leakage

- Measured neighborhoods in a new tissue can be legitimate inputs to conditional activity prediction. Post-treatment measurements cannot serve as pretreatment inputs for a response that has not happened.
- Split linked donors and modalities before outcome-informed feature selection, imputation, alignment, module learning, nuisance fitting, and tuning. Audit pretraining/reference exposure, including unknown overlap.
- Make measured genes primary validation targets. Teacher-imputed targets risk measuring agreement with the teacher rather than biology. Held-out genes do not demonstrate held-out-donor generalization.
- Exclude the focal cell from its neighborhood. Audit segmentation spillover, boundaries, density, and radius sensitivity. Shared donor IDs do not prove identical tissue sections or valid registration.
- In GeneBridge, verify the full donor inventory rather than reconstructing it from the remembered list. The dataset note explicitly flags that list as incomplete. Source: [[02_Projects/GeneBridge/datasets]].

## 3. Confounding and measurement

Tabulate context × perturbation × independent biological unit, including controls, dose/time, batch and platform. Full-rank regression does not establish causal identification or practical overlap. Random effects cannot repair complete context–cohort confounding.

Compare with target-independent assay-nuisance baselines; recurring technical spatial patterns can survive donor holdouts. A library-size feature that includes masked target genes can violate a held-out-target contract. Density and morphology can also carry genuine biology: residualization is a sensitivity analysis, not proof of causality. Temporal-state correction should not become an obligatory new preprocessing step merely because the latest radar raises it as a possible alternative explanation; its validity in these cortical samples is not established.[2]

## 4. Keep the first context test bounded

```text
M0:  Y_u = alpha + B_C C_u + B_X X_u + epsilon_u
MQ:  Y_u = alpha + B_C C_u + B_X X_u + B_Q Q_u + epsilon_u
MQE: Y_u = alpha + B_C C_u + B_X X_u + B_Q Q_u + B_E E_u + epsilon_u
DeltaL_d = L_d(strongest eligible simple baseline) - L_d(context model)
```

C denotes permitted identity inputs; X design covariates; Q justified target-independent nuisance; E fixed context features. Fit regularized models under identical nested donor splits. Include cell-type/layer means, pooled neighborhoods, simple multiscale context, and cell-type-stratified context. Match loss to the measured endpoint.

Refitted context removal measures added predictive information; frozen-model replacement measures reliance under the chosen replacement distribution. Attention values or output movement do not identify a biological mechanism. Support-matched replacements can preserve correlated information, so residual predictive gain is not automatically leakage.

## 5. Response-specific evaluation and biological validation

For an eligible design on a declared common endpoint scale:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
I_p = E_d[Delta_d,e1,p - Delta_d,e0,p]
Y_d,b,r = beta0 + betaE*E + betaP*P + betaEP*(E*P)
          + gamma_batch + b_d + epsilon_d,b,r
```

The mixed model is illustrative for a continuous endpoint, not a frozen formula for an unknown assay. Specify the distribution, assignment unit, nesting, and random-effect structure from the actual design. Allow donor response heterogeneity when supported; cells and technical wells do not replace independent biological units. Spatial interference also affects what a treatment contrast means.

Separate final-state accuracy, shared perturbation response, context-specific interaction recovery, and changes in cell abundance. Report donor/biological-unit effect sizes and uncertainty, not only cell-wise correlations. Better diversity alone can reward noise; a mean-only score can miss relevant heterogeneity.

Use positive/negative controls to establish endpoint sensitivity; keep outcome-informed calibration separate from deployable prediction and protected testing. Tune on training/validation units only. Repeated folds share training data and are not independent replications. A bootstrap of fixed held-out predictions quantifies a narrower uncertainty than refitting the entire modeling procedure; specify which claim the interval supports.

The weekly strategy's interval/null thresholds are proposed operating rules, not validated universal standards. Define a practical effect threshold and resampling assumptions before final testing; an interval excluding zero is not alone proof of useful biology. Source: [[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]].

## 6. Unresolved implementation specifications

The PDF leaves attention notation, aggregation shape, and the exact sparsity penalty unresolved. L1 on normalized nonnegative softmax weights would be constant, but the source does not specify L1; this is a conditional caution, not a discovered bug. The diagram leaves the conditional-VAE prior/posterior, likelihood, and identity-loss integration incompletely specified. Resolve these only when that model is justified by a baseline gap. Source: [[02_Projects/AIVC/project-outline]].

# PRELIMINARY DATA

## WHAT I ALREADY HAVE

1. **Documented preparation and assets:** cohort-scale human cortical spatial genomics, metadata/QC work, donor–layer analyses, and a held-out-gene evaluation design. Sources: [[01_Research/research-overview]], [[02_Projects/GeneBridge/methods]].
2. **Historical GeneBridge outputs:** metadata recovery, pseudobulk and diagnosis-analysis records with paths/job references. Current numbers, the final method panel and the reported method ranking still require output-file verification. Source: [[02_Projects/GeneBridge/experiments-and-results]].
3. **Concrete AIVC design evidence:** a user-supplied UR/VI outline and a distinct multimodal perturbation diagram. These support a proposed plan, not model performance. Source: [[02_Projects/AIVC/project-outline]].

## WHAT IS STILL MISSING

- Selected aging/AD population, exposure, intervention and endpoint with verified data/access and biological replication.
- An executed AIVC baseline package: code/configuration, registry, manifests, measured predictions, all comparators, leakage audit, uncertainty and advance/stop/inconclusive decision.
- Current verification of GeneBridge outputs, preservation of measured disease effects and calibrated null behavior.
- A measured context-dependent perturbation result and functional validation route.
- Named training commitments, candidate ownership, and portable R00 resources.

The AIVC results note still explicitly says no finalized benchmark/result set is confirmed. No historical numerical result is newly certified here. Papers from other laboratories are not the applicant's preliminary data.

# CAREER DEVELOPMENT — Investigator 6; Environment 5

A coherent K99 need would be the transition from observational spatial genomics to experimentally grounded, context-dependent response modeling. “Learning GNNs and transformers” alone is too generic to justify mentored support.

| Training gap | Needed commitment | Assessable milestone |
|---|---|---|
| Aging/AD biology | Named system-relevant co-mentor and structured training | Defensible premise, exposure and endpoint with explicit model limitations |
| Perturbation/functional assays | Assay mentor, access, responsibilities and protected effort | Manipulation/variance pilot and preregistered validation |
| Identification and transport | Quantitative training tied to the actual design | Support audit, appropriate uncertainty, calibration and external test |
| Measurement-aware modeling | Assay-error and reproducibility mentorship | Leakage-resistant measured-target benchmark |
| Independent leadership | Grantsmanship, supervision and ownership plan | Candidate-controlled R00 launch package |

Jian Hu is the documented current advisor. No aging/AD co-mentor, assay access, or institutional commitment is inferred from that fact. The notes describe the mentor-associated spatial-integration program; the application must state what training is new, who provides it, and which intellectual direction the candidate owns. Sources: [[00_Profile/collaborators-and-roles]], [[05_Learning/learning-goals]].

Investigator and environment scores are low-confidence judgments of incomplete application evidence, not judgments of inherent ability or Emory's general resources. A publication/role inventory and commitment letters are needed before a firmer candidate assessment. Administrative K99 eligibility and transition requirements need a separate current official-source check.[3]

# INDEPENDENCE

This can become an independent program if its organizing question is **when tissue environments change cellular responses and where those predictions fail to transfer**. Another integration platform alone risks appearing to extend the mentor's established spatial-integration direction. The source PDF's “Thrust 3” label does not establish applicant ownership.

Document explicitly: candidate-owned questions/software, portable datasets, what remains with the mentor, permission to continue relevant analyses, prospective assay partnerships, and the minimum resources required at an R00 institution. A prospective assay that disappears with the postdoc is not a launch plan. Sources: [[00_Profile/collaborators-and-roles]], [[02_Projects/AIVC/project-outline]].

- **R01 potential:** a replicated, bounded context-dependent mechanism with functional consequences and a tractable next biological question.
- **NSF CAREER potential:** a generalizable methodological contribution in measurement-aware prediction, uncertainty or transport, integrated with a substantive education program. This is a scientific trajectory, not an eligibility determination.
- **Faculty-program potential:** one persistent question spanning a small number of supported systems—not a catalog of architectures and diseases.

The current notes support a plausible direction, not a demonstrated independent launch package.

# NIH-STYLE SCORES

Scale: 1 is best, 9 is worst. These are the user's requested mock categories, not a claim that they exhaust the applicable K99 review framework.

| Criterion | Score | Main reason |
|---|---:|---|
| **Overall Impact** | **8** | NIA premise/access, executed response evidence and training/independence package remain unresolved |
| Significance | 7 | Important potential question, but aging/AD mechanism and endpoint unselected |
| Investigator | 6 | Relevant preparation; targeted development and ownership package incomplete |
| Innovation | 6 | Response validation could distinguish the work; architecture alone is increasingly hard to defend |
| Approach | 8 | No confirmed AIVC benchmark; identification, measurement, support and validation gaps |
| Environment | 5 | Specific mentorship, assay access and portable resources undocumented |

All scores remain unchanged from October 18. More literature is not preliminary progress, and passage of time alone does not warrant a score penalty.

# TOP 3 STRENGTHS

1. Documented human cortical spatial-genomics preparation with traceable GeneBridge analysis assets.
2. A concrete identity/environment premise that can be falsified with measured targets and small models.
3. A possible independent direction in validated context-dependent response and transport, if biological access and ownership are secured.

# TOP 3 MAJOR RISKS

1. **NIA fit and feasibility:** no selected aging/AD question with verified response data and an executable validation route.
2. **Claim–evidence mismatch:** observational prediction, teacher reconstruction, or input sensitivity being presented as causal intervention biology.
3. **Execution and differentiation:** architecture accumulation without a result package, strong representation-controlled baselines, committed training, or portable R00 resources.

# TOP 3 EXPERIMENTS I SHOULD PRIORITIZE

## 1. Nuisance-aware measured-target context-value experiment

After freezing donor and target manifests, compare the small models above on measured targets under nested donor splits. Include target-independent nuisance, pooled/multiscale summaries, focal-cell exclusion, refitted ablations, and support-matched replacement diagnostics. Report donor-level loss changes, practical magnitude, uncertainty, sensitivity controls, and an advance/stop/inconclusive decision.

**Output:** reproducible manifest/configuration, all baseline predictions and one decisive context-value figure. If run only in GeneBridge, label it **SCZ conditional-prediction engineering**, not aging/AD or perturbation evidence. Do not add the entire new literature model list to this experiment.

## 2. GeneBridge disease-effect preservation and null calibration

Verify current methods, prediction files, exclusions, and gene folds. On one frozen measured/imputed gene universe and donor × layer unit, fit the same estimable model to each method. Proposed formula:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Freeze transformation, repeated-donor implementation, technical terms and testing family after the design audit. Compare coefficient magnitude/direction, calibration and uncertainty against simple/nonspatial baselines. Use valid donor-level covariate-aware null resampling; redo outcome-based selection inside the appropriate resampling procedure. No arbitrary cell-wise label shuffle.

**Output:** all-method coefficient-concordance and null-calibration package with a bounded manuscript conclusion. Reconstruction quality alone does not authorize biological claims about imputed genes.

## 3. Controlled context × perturbation pilot

Secure one aging/AD-relevant neural/glial system and one independently justified contrast. Where feasible randomize exposure and intervention, verify manipulation, freeze simple/context-aware predictions, and measure one molecular program plus a functional endpoint across independent biological replicates. Use pilot variance and assignment structure to plan precision, not an invented sample-size target.

**Output:** access/protocol evidence, manipulation checks, response-interaction estimate with uncertainty, and a later independent confirmation plan. The reported DynaVelo rescue example is a validation standard, not evidence that a neural rescue assay is already available.[2]

For subsequent modeling, separate perturbation embeddings and response heads before crediting context. That comparison belongs here once response data exist, not in the initial non-perturbational GeneBridge pilot.

# ONE-SENTENCE FUTURE-LAB VISION

My laboratory will develop and experimentally test measurement-aware models of how tissue environments shape cellular responses in aging human neural systems, with explicit limits on transfer across donors and contexts.

This is a proposed NIA-oriented vision, not a replacement for canonical SCZ scope.

# NUMBER-ONE ACTION THIS WEEK

**Close the aging/AD premise-and-access decision with COMMIT or NO-GO.** Produce `02_Projects/AIVC/aging_AD_AIVC_premise_v1.md` identifying one population, exposure, perturbation class, measured endpoint, verified biological-unit support, information boundaries, and named validation route. If no system meets the requirements, document NO-GO and the minimum missing collaborator pilot. Do not create a fictional commitment or renew architecture planning instead of making the decision.

The action itself is unchanged; the new literature clarifies how the eventual response benchmark must isolate context from representation/head effects. No scientific scope change, experiment, collaborator commitment or funding eligibility decision has been made on the user's behalf.

## Sources

[1] file:///opt/data/obsidian-vault/02_Projects/AIVC/literature/2026-10-21-literature-radar.md — October 21 AIVC Literature Radar — internal assessment
[2] file:///opt/data/obsidian-vault/02_Projects/AIVC/literature/2026-10-23-literature-radar.md — October 23 AIVC Literature Radar — internal assessment
[3] file:///opt/data/obsidian-vault/Hermes/Conversations/2026-10-23/cron_b006ab3b7fec_20261023_130043.md — October 23 NIA Funding Radar — final Assistant section
