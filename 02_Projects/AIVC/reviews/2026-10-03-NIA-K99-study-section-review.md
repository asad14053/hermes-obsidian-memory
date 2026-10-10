---
type: nih-review
project: AIVC
mechanism: NIA K99/R00
status: critical-review
created: 2026-10-03
last_updated: 2026-10-03
overall_impact: 8
comparison_status: STAGNANT
confidence: medium
previous_review: "[[02_Projects/AIVC/reviews/2026-09-27-NIA-K99-study-section-review]]"
new_project_results_verified: false
material_methodological_update: true
---

# AIVC as a potential NIA K99/R00 — skeptical study-section review

## Bottom line

**Overall Impact: 8/9. Status: STAGNANT in application readiness.** The reviewed record still lacks a selected aging/AD system, a demonstrated AIVC response-prediction result, an intervention-validation route, and a concrete training/independence package. This is a document-based assessment, not evidence that no work has occurred outside the vault. Scores are provisional NIH-style judgments on the requested scale, with 1 best; they are neither an official review nor an arithmetic average.

**The material change since September 27 is methodological, not project progress:** the October 2 literature requires a stronger benchmark decision rule. Accurate final expression is insufficient evidence of context-specific response recovery, but failure under an insensitive metric is also insufficient evidence that a model or biological premise has failed.[1][3] The next experiment must establish both that its endpoint can detect relevant signal and that context improves the selected response beyond identity/shared effects. More architecture cannot substitute for either test.

The primary NIA weakness remains the missing biological premise and feasible validation system. Calibrating metrics does not solve that institute-fit problem.

## Evidence hierarchy and comparison with the previous review

The [[02_Projects/AIVC/project-outline|September 23 user-supplied outline]] governs intended science. Its PDF proposes identity/environment activity prediction; the diagram adds multimodal alignment, explicit perturbations and a conditional VAE. They remain distinct specifications. The diagram and [[02_Projects/AIVC/goals|canonical goals]] are SCZ-centered; an aging/AD branch is an application-specific recommendation, not an approved replacement.

| Gate | September 27 | October 3 |
|---|---|---|
| Scientific specification | Concrete PDF/diagram, unresolved differences | Same source; no confirmed implementation version |
| NIA premise | Population, exposure, intervention, endpoint and access unselected | Still open in October 3 task list; no premise-named artifact found |
| AIVC results | No confirmed benchmark | Results note unchanged; no new execution package found in searched notes |
| GeneBridge | Useful assets; historical results need verification | Same status; no new file-verified disease-effect preservation package |
| Validation | Observational swaps are not intervention truth | No documented prospective intervention result or committed assay route |
| Training/independence | Team, milestones and portable ownership incomplete | No new commitments found |
| Planning | Feasibility gate recommended | September 28 strategy and October 3 tasks sharpen commit/no-go; not completion |
| Literature | September 25 radar | October 2 radar adds metric calibration and recoverable-resolution constraints |
| Funding | Monitoring incomplete | October 2 final funding response also says verification was impossible |

Comparison source: [[02_Projects/AIVC/reviews/2026-09-27-NIA-K99-study-section-review]]. Planning sources: [[09_Planning/weekly-strategies/2026-09-28-AIVC-GeneBridge-weekly-strategy]], [[02_Projects/AIVC/todo-and-next-actions]], [[09_Planning/active-tasks]].

**Why STAGNANT rather than GETTING WEAKER:** new literature changes the test required, not the applicant's measured performance. No result supports either upgrading readiness or worsening the score merely because time passed. Cleaner tasks and more papers are not preliminary data.

# SIGNIFICANCE — 7

## Why should NIA care?

A defensible application would show that a defined aging- or AD-related environment changes a biologically consequential response in a selected neural/glial population, and that measuring that environment improves transportable prediction or intervention selection. The current notes establish interest in that question, not its premise. A generic virtual cell with AD mentioned as a future application is not enough for this proposed NIA framing.

Specify separately: chronological age, disease pathology, induced exposure, cell state and functional impairment. They are not interchangeable. An age covariate does not establish an aging mechanism; an acute stress assay does not automatically represent chronic AD. State what the selected model captures and what it cannot claim.

**SCZ:** GeneBridge is a genuine methodological starting point for spatial measurement and donor-level analysis. It should support preparation or a tightly bounded transport test, not a parallel disease aim without a shared mechanism. There is no documented shared intervention-response mechanism connecting SCZ and AD here. If the strongest actual question remains SCZ, preserve it and reconsider institute fit rather than cosmetically relabeling the disease.

Evidence: [[01_Research/research-overview]], [[01_Research/scientific-interests]], [[02_Projects/AIVC/datasets]], [[02_Projects/AIVC/goals]].

# INNOVATION — 6

**Potentially original:** identifying when measured tissue context supplies additional, reproducible response information across donors; defining the biological resolution at which predictions are useful; and testing selected contrasts experimentally.

**Not sufficient novelty:** assembling scGPT/UCE, neighborhood attention, imputation, a perturbation embedding and a conditional VAE. Those are components in the proposed outline, not evidence that the combination solves a new biological problem.

### New literature that changes the review

1. **Metric sensitivity must be established before ranking models.** Miller et al. introduce a positive-control/calibration framework and show that common perturbation metrics can obscure useful signal; some deep models outperform uninformative baselines under calibrated metrics.[1] Reviewer implication: do not declare a universal failure of deep learning from raw MSE, and do not select favorable metrics after seeing model rankings. A perturbation-outcome-informed positive control is an evaluation diagnostic, not a deployable predictor or proof of biological causality.
2. **State recognition is not context-specific response prediction.** Huang et al.'s preprint distinguishes preserved identity/shared effects from compressed context-specific response differences, and reports that supported resolution can differ between gene-level and predefined pathway outputs.[3] Reviewer implication: report response components and precision, not only final-expression correlation. This abstract-level evidence does not establish a universal biological predictability ceiling or a DLPFC result.
3. **Information encoded is not information used.** Fang et al. audit biological reasoning models and find that informative representations can contribute little to some models' performance, while other systems do benefit.[2] Reviewer implication: pair refitted ablations with frozen-model input replacement. These LLM-linked results motivate an audit; they do not establish that the proposed AIVC ignores its inputs.
4. The [[02_Projects/AIVC/literature/2026-10-02-literature-radar|October 2 radar]] also identifies ProxiNet as a proximity-transfer comparator and CycloCross as a later cross-species comparator. These two descriptions are secondary-note context only in this review. Neither justifies expanding the immediate aims, and inferred proximity cannot substitute for observed intervention exposure.

**Claims reviewers would challenge:** “counterfactual validation” by matching different cells; “universal” representations from narrow assays; mechanism inferred from attention; dynamics inferred from static snapshots; joint intervention effects learned from non-overlapping spatial and perturbation datasets; and biological improvement inferred from better reconstruction alone.

# CENTRAL HYPOTHESIS

The existing outline supplies a testable conditional-prediction premise—environment adds activity information beyond identity—but no frozen NIA-specific hypothesis. The stronger causal interpretation remains unvalidated.

## One strong central hypothesis — proposed, not adopted

**In a prespecified human neural/glial population, a defined AD-associated inflammatory exposure modifies the response to a limited perturbation class; pre-intervention neighborhood programs predict that modification across held-out donors beyond identity and shared perturbation effects, and controlled exposure manipulation reproduces the predicted response direction and a prespecified functional consequence.**

Inflammation is a proposed narrowing, not a finding or selected assay. Population, exposure, perturbation, dose, timing, response program and functional endpoint must be selected from verified access and biology before this becomes an application hypothesis.

Falsifiers: adequate-precision experiments show no context modification; context gives no additional response information under sensitive metrics; apparent benefit survives appropriate null-context controls; transport fails; or a properly executed manipulation contradicts the registered contrast. An insensitive assay/metric yields an inconclusive test, not automatic biological falsification.

# SPECIFIC AIMS

No finalized K99 Specific Aims page is documented. The outline's atlas portal plus full simulator is not automatically a feasible career-award structure. The following is a proposed restricted structure, conditional on pre-submission feasibility evidence.

## Aim 1 — Establish whether AD-relevant context supports transferable response prediction

Select one system and measured response at a preregistered gene/program resolution. Establish assay repeatability and metric sensitivity. Compare no-change/control, shared perturbation, additive/identity and minimal context-interaction predictors on protected donor splits. Distinguish prediction of observed activity from prediction of an unobserved perturbation response.

**Measurable deliverables:** accession/access and overlap inventory; fixed estimand and inputs; donor/modality split manifest; positive/negative controls; held-out predictions; donor-level paired loss and response-recovery estimates; useful-input audit; independent validation or a justified restricted generalization claim.

**Resilience:** retain a simple model if complexity fails. If fine-grained responses are poorly measured but a biologically justified, predeclared program is repeatable, report both endpoints and the supported resolution. Do not redefine the primary outcome after inspecting the final test. If context itself adds no supported value, report the boundary rather than inventing a larger architecture.

## Aim 2 — Test one environment-by-perturbation interaction experimentally

Use a limited factorial design in a committed neural/glial system, with manipulation checks, biological replication, controls and a functional readout. Choose at least one contrast independently justified by biology so the entire experiment does not depend on a winning Aim 1 model. Freeze competing predictions before measurement.

**Measurable deliverables:** documented assay access and protocol; randomized exposure/perturbation assignments where feasible; measured expression/program and functional contrasts; replicate-level uncertainty; separation of failed manipulation, failed prediction and falsified biology.

**Resilience:** a failed sophisticated model leaves a valid biological interaction test and baseline comparison. An unavailable assay or unmeasurable response is a feasibility failure, not a fallback to computational “validation.”

## R00 direction — Transport and delimit a supported mechanism

Extend the validated question to one defined donor/context shift, using candidate-controlled software/data access and an independent experimental partnership. Do not promise simultaneous cross-species, cross-disease, unseen-target and joint-environment transport.

**Aim assessment:** logically connected and potentially independent enough, but not yet shown feasible. Portal development, multimodal atlas construction, new attention, a generative model and prospective biology should not all be core deliverables. A fundamental premise/access gate must be closed before submission, not delegated wholesale to the award.

# APPROACH — 8

## 1. Freeze the estimand and information set

The PDF's identity-matched swap compares different observed cells. Matching does not eliminate donor, layer, pathology, state, selection or technical differences, and is not paired counterfactual ground truth.

```text
Conditional activity: m(c,e,x) = E[Y | C=c, E=e, X=x]
Simulated contrast: m(c,e',x) - m(c,e,x)
Intervention contrast: E[Y(e') - Y(e) | baseline C=c, X=x]
```

An intervention interpretation additionally needs a well-defined exposure, consistency, overlap and defensible confounding/selection assumptions or an experimental design. Neighbor interventions create interference: define the exposure mapping and randomized unit, not just individual-cell treatment labels. Identity measured after exposure may encode part of the response; holding it fixed can change the estimand.

## 2. Audit leakage and measurement

- Split biological donors before fitting preprocessing, feature selection, alignment, imputation, modules or tuning. Group all linked sections/modalities and repeated samples. Audit foundation-model reference overlap where knowable; document unknown overlap.
- Disjoint identity and target genes do not demonstrate causal disentanglement. Correlated proxies, response-informed labels and post-exposure identity remain concerns.
- Define deployment availability. Measured neighbors in an observed test tissue can be legitimate for conditional prediction; future response measurements cannot be inputs to forecasting that response. Keep those tasks separate.
- Remove focal self-neighbors, check segmentation spillover and technical spatial dependence, and prespecify radius/density/edge handling.
- Match modalities explicitly. A shared donor ID does not prove spatial registration or cell pairing.
- Prefer measured held-out targets; do not score an imputer against its own pseudo-labels. Imputation confidence needs validation, not merely a weight in the loss.
- Gene-held-out evaluation is not donor-held-out evaluation. Unseen donors, perturbations and contexts require separately named tests and uncertainty, not one undifferentiated generalization claim.

Sources: [[02_Projects/AIVC/project-outline]], [[02_Projects/GeneBridge/datasets]], [[02_Projects/GeneBridge/methods]].

## 3. Joint interventions remain unsupported by unpaired data alone

Unperturbed spatial tissue plus dissociated Perturb-seq does not automatically identify environment-by-perturbation effects. An environment code and a perturbation code can be combined computationally without the combination being empirically identified. Tabulate context × perturbation × donor support, controls, dose and time. Separate environment-only, perturbation-only and joint-query validity; abstain outside supported combinations. A zero perturbation embedding is not a measured control in every context.

## 4. Statistical models and decision rules — proposed, not executed

For the measured-target SCZ engineering pilot, nested ridge baselines are:

```text
M0: Y_u = alpha + B_C C_u + B_X X_u + epsilon_u
M1: Y_u = alpha + B_C C_u + B_E E_u + B_X X_u + epsilon_u
```

C is permitted identity information, E a frozen cell-type-stratified neighborhood summary, X deployment-available covariates, and Y measured held-out targets. Tune within training donors. Compare a small interaction/MLP extension separately. A categorical test-donor effect is not an available learned predictor for a new donor.

For a genuinely replicated perturbation assay, define response on a common prespecified scale:

```text
Delta_d,e,p = mean(Y_d,e,p) - mean(Y_d,e,p0)
Context modification_p = Delta_e1,p - Delta_e0,p
```

Use matched controls at the correct biological level; quantify uncertainty in both treated and control measurements. Report full state prediction, shared perturbation response, and context-specific deviation separately. Learn shared-effect/nuisance terms from training data or cross-fitting; do not residualize using pooled final-test outcomes and then claim prospective prediction. Test-derived contrasts may define evaluation truth, but cannot become prediction inputs or model-selection targets.

For a continuous prospective functional endpoint, a candidate formula is:

```text
F_d,e,p,r = beta0 + betaE*E_e + betaP*P_p + betaEP*(E_e*P_p)
            + betaB*Batch_r + b_d + epsilon_d,e,p,r
b_d ~ Normal(0, sigma_d^2)
```

Here r denotes an assay replicate, not a cell. Specify actual nesting, randomization and donor structure before adoption; add age/sex or other covariates only when justified and estimable. If the endpoint is not continuous, choose its appropriate response family. A random intercept does not repair a rank-deficient or completely confounded design.

**Metric amendment to the prior review:** retain absolute error for its stated prediction target, but do not treat it as a complete assay of perturbation specificity. Before model comparison, test whether positive controls separate from negative controls at the selected response resolution.[1][3] Use independent biological replicates when available; splitting cells alone measures sampling repeatability, not cross-donor reproducibility. Outcome-informed interpolated controls belong only in a preregistered evaluation diagnostic. Freeze gene/program sets, weights and ranking rules in development data; isolate any final-test-derived evaluation quantities from fitting and adaptive selection.

Use paired donor/biological-unit contrasts and confidence intervals; cells and cross-validation folds are not independent replicates. Resample at the unit appropriate to each transport claim. Base precision on pilot biological variance, not cell count. Freeze the tested multiplicity family. Do not substitute an arbitrary percentage or energy-distance threshold for an estimand-matched endpoint.

## 5. Input use, robustness and implementation

Refitted removal tests available information; frozen-checkpoint replacement tests fitted reliance. Require target-loss or response-recovery consequences, not output movement alone. Use support-matched replacements and report out-of-distribution sensitivity separately. Null replacements must preserve appropriate cell-type/layer/technical structure without preserving the exact signal being tested.

The PDF's `4g` notation/aggregation remains underspecified; the diagram does not completely define VAE posterior/prior/likelihood or incorporate `L_identity` explicitly into the total loss. If sparsity is L1 on normalized nonnegative attention, it will not encourage sparse weights; the source does not confirm that choice. These are design clarifications, not observed code defects. Fixing them would not resolve the missing biological premise.

# PRELIMINARY DATA

## WHAT I ALREADY HAVE — documented assets, not newly revalidated results

1. Human SCZ/DLPFC spatial-genomics work and GeneBridge data infrastructure: targeted Xenium, Visium and snRNA-seq references; donor/layer metadata; documented 24-donor reference and 23-donor downstream cohort after Br6432 exclusion; held-out-gene evaluation design. Current source files and complete donor accounting were not independently revalidated here.
2. Historical GeneBridge pseudobulk/DE analyses and metadata-recovery records. The notes explicitly require verification before using remembered discovery counts, model rankings or final-panel claims. These are not locked current preliminary findings.
3. A concrete AIVC identity/environment design preserved from user-provided sources. This is design evidence, not an executed benchmark, intervention result or aging/AD dataset.

Sources: [[02_Projects/GeneBridge/current-state]], [[02_Projects/GeneBridge/experiments-and-results]], [[02_Projects/GeneBridge/datasets]], [[02_Projects/AIVC/project-outline]].

## WHAT IS STILL MISSING

- One verified aging/AD population, context, perturbation, response and functional endpoint; accessible data/assay and biological rationale.
- Completed premise/access/overlap audit and documented commit/no-go.
- AIVC code/run provenance, split manifests, baseline predictions, sensitive response metrics, leakage checks and input-use results.
- Evidence that context improves the response of interest rather than donor/cell identity recognition; independent validation.
- Verified GeneBridge method/version and donor accounting; measured-versus-imputed disease-effect preservation and null calibration.
- Prospective intervention feasibility/results, manipulation checks and a precision plan.
- Named mentor commitments, training activities, ownership boundaries and portable R00 resources.

The [[02_Projects/AIVC/experiments-and-results|AIVC results note]] still states that no finalized benchmark/result set is confirmed. Literature findings are not applicant preliminary data.

# CAREER DEVELOPMENT — Investigator 6; Environment 5

The [[00_Profile/identity-and-career|profile]] documents computational/engineering experience and current human cortical genomics work, while explicitly distinguishing emerging AIVC, perturbation and aging/AD directions. This is not a complete biosketch/publication audit.

**Why K99:** a credible need is the transition from observational spatial prediction to biologically grounded, experimentally tested response inference. “I need to learn Transformers” is too generic and does not explain a mentored research-development program.

| Training gap | Needed activity/commitment | Verifiable milestone |
|---|---|---|
| Aging/AD mechanism | Named co-mentor and focused system-specific training | Defensible exposure, cell population and functional endpoint |
| Experimental intervention | Embedded assay training and committed collaborator access | Controlled pilot, manipulation checks, variance estimate |
| Identification and transport | Causal/statistical mentorship | Written estimands, assumptions, overlap and uncertainty audit |
| Reliable biological ML | Measured-target, metric-calibration and replicate design practice | Reproducible protected benchmark with controls |
| Independent leadership | Grantsmanship, mentoring and resource planning | Candidate-owned question/code and R00 launch package |

None of these commitments is documented as secured. Supply actual people, activity frequency, protected time, evaluation milestones and responsibility. Environment score reflects unverified access and commitments, not a negative claim about Emory's facilities. Investigator score reflects the incomplete application record, not a definitive assessment of capability.

# INDEPENDENCE

The proposed program is not yet demonstrably portable or distinct from the mentor's integration program. [[00_Profile/collaborators-and-roles]] describes the advisor's multi-view/multi-section/multi-sample spatial-integration focus. A new integration portal alone would not establish separation. The outline's “Thrust 3” label does not establish authorship, ownership or permission to take the work.

Write down candidate-owned scientific questions, code/data rights, manuscripts, permitted R00 extensions, collaborators and resources that remain accessible after departure. The distinctive niche should be **validated context-dependent response prediction and its limits**, not simply more integration.

- **R01 trajectory:** one biologically supported context-response mechanism, external replication and functional consequences.
- **NSF CAREER trajectory:** generalizable methods for reliable context-conditioned inference, uncertainty and evaluation, with an integrated education program.
- **Future laboratory:** reusable, candidate-controlled computational infrastructure plus independent experimental partnerships.

These are proposed trajectories, not current funding-opportunity or eligibility determinations.

# NIH-STYLE SCORES

| Criterion | Score | Decisive reason |
|---|---:|---|
| **Overall Impact** | **8** | Missing NIA premise, executed evidence, intervention feasibility and transition package |
| Significance | 7 | Potentially relevant biology; actual aging/AD question and endpoint unselected |
| Investigator | 6 | Relevant foundation; full record and targeted development plan not assessable |
| Innovation | 6 | Validity/transport could distinguish; component assembly alone does not |
| Approach | 8 | No verified data contract/result; observational causal overclaim and uncalibrated response-testing plan |
| Environment | 5 | Relevant institution, but specific assay/training access uncommitted in record |

Scores are unchanged from September 27. The new metric critique changes the required evidence, not the score in the absence of new project results.

# TOP 3 STRENGTHS

1. Real human cortical spatial-genomics experience and donor-structured GeneBridge assets.
2. An explicit identity/environment design that permits direct falsification through measured-target baselines and controlled input-use tests.
3. A possible independent niche joining reliable prediction, biological resolution and intervention validation rather than another architecture alone.

# TOP 3 MAJOR RISKS

1. **NIA premise/access failure:** no selected aging/AD system, consequential endpoint or feasible intervention-validation path.
2. **Invalid evidence of response prediction:** observational swaps, identity recognition, imputed targets or insensitive aggregate metrics could be mistaken for validated context-dependent intervention effects.
3. **Execution/independence failure:** scope exceeds demonstrated results while training commitments, ownership and portable resources remain undocumented.

# TOP 3 EXPERIMENTS I SHOULD PRIORITIZE

## 1. Calibrated context-value test on measured outcomes

After the NIA access gate, compare identity/additive and minimal context predictors on locked donor splits. Establish metric sensitivity and independent-replicate signal before interpreting rankings. For perturbation data, test response beyond shared perturbation effects at prespecified gene/program resolution; for a GeneBridge-only pilot, test measured conditional activity and explicitly exclude perturbation/AD claims. Add support-matched frozen-model replacement and refitted no-context controls.

**Required output:** data/input contract, reproducible predictions, positive/negative-control calibration, paired biological-unit uncertainty, context-use audit and a pass/fail/inconclusive conclusion. Advance only when context benefit is meaningful, robust and not reproduced by null inputs. A failed positive-control separation makes that endpoint inconclusive; it does not justify declaring the biological premise false.

## 2. GeneBridge disease-effect preservation

Verify current output versions, donor/exclusion and gene-fold manifests. Fit the same locked repeated-donor specification on measured and held-out-gene imputed outcomes. Following the newer September 28 strategy, a proposed starting specification on a common declared normalized scale is:

```text
y_gdl ~ Dx_d + scale(Age_d) + Sex_d + layer_l + (1 | donor_d)
```

Audit rank and confounding before adding any run/slide covariate; version the decision before comparing methods. Do not silently inherit the older review's generic batch term. Compare diagnosis coefficients, signs, calibration and uncertainty over a common gene universe. Use donor-level, covariate-aware null resampling where justified, not cell permutations.

**Required output:** traceable method/data manifest, coefficient-concordance and null-calibration figures, and a bounded claim about whether imputation supports disease inference. This protects publication evidence; it is not aging/AD intervention evidence.

## 3. Limited prospective context × perturbation experiment

Secure one eligible neural/glial system and independently justified contrast. Randomize or otherwise rigorously control exposure and perturbation, verify manipulation, measure a frozen program plus functional endpoint, and replicate at the biological experimental unit. Freeze simple-baseline and model predictions before outcomes are observed.

**Required output:** protocol/access commitment, variance-informed replication plan, measured interaction and functional response with uncertainty, and explicit prediction-versus-biology adjudication. If access is absent, record that blocker rather than presenting an in-silico contrast as validation.

# ONE-SENTENCE FUTURE-LAB VISION

My laboratory will develop and experimentally test reliable models of how tissue environments shape cellular responses in aging human neural systems, with explicit limits on biological resolution and transport across donors.

# NUMBER-ONE ACTION THIS WEEK

**Close the NIA premise/access gate within two working days:** document one aging/AD population, exposure, perturbation class, measured response, donor-resolved data/access and feasible validation route in `aging_AD_AIVC_premise_v1.md`, ending in commit/no-go. Add a prespecified positive-control/negative-control metric-sensitivity check and a context-specific response endpoint to the benchmark plan before using model rankings to decide success or failure. If no eligible system exists, specify the minimum collaborator-generated pilot instead of relabeling SCZ assets.

This is a proposed deliverable, not a file created or an experiment performed by this review. The SCZ engineering pilot can proceed as bounded preparation; it cannot close the NIA gate alone.

# Sources, coverage and limits

- Reviewed the canonical AIVC outline, overview/state, goals, methods, decisions, datasets, results, tasks and September 27 review; GeneBridge state/methods/datasets/results/tasks; research/profile/collaborator notes; learning references; planning tasks/questions and September 28 strategy.
- Requested `05_Papers_and_Learning/` and `09_Open_Loops/` are absent. Used canonical `05_Learning/` and `09_Planning/`; absence of those aliases is not missing knowledge.
- Read the latest [[02_Projects/AIVC/literature/2026-10-02-literature-radar|literature note]] and recovered the final Assistant output from [[Hermes/Conversations/2026-10-02/cron_b7fccc11fa73_20261002_100047|its actual job conversation]], not nested historical prompt material.
- Recovered the final Assistant section of [[Hermes/Conversations/2026-10-02/cron_b006ab3b7fec_20261002_130023|October 2 funding output]]. It explicitly says the scan and funding-note update could not be performed. This is a coverage gap, not evidence of no new funding changes. No fresh official-policy scan or current eligibility/deadline determination is claimed here.
- Fresh primary retrieval: Miller article abstract/main text through metric definitions and model-comparison design; Fang versioned arXiv API abstract; Huang version-1 bioRxiv abstract. No claim of full supplementary audit, full-text review of the two preprints, or independent numerical reproduction. Primary quantitative headlines were not needed for this critique.
- Did not execute HPC analyses, train AIVC, revalidate GeneBridge result files, or perform biological experiments. Source attachments were not re-rendered; the canonical intake note supplies their provenance.
- External claims below use the task citation ledger; local project facts use explicit wikilinks. Interpretations, hypotheses, aims and experiment designs are reviewer proposals rather than source-established facts.
- Scheduled delivery is limited to the requested score, biggest weakness and weekly action. A short alert is warranted because the metric-sensitivity decision rule materially changes the prior benchmark recommendation, despite unchanged scores.

## Sources

[1] https://www.nature.com/articles/s41587-026-03307-w — Deep learning perturbation models can outperform baselines on calibrated metrics
[2] https://export.arxiv.org/api/query?id_list=2610.00898v1 — When Do Biological Reasoning Models Use Their Biological Inputs?
[3] https://www.biorxiv.org/content/10.64898/2026.09.30.755756v1 — The recoverable resolution of cellular perturbation-response prediction
