# AIVC Literature Radar — 2026-10-26

## Window, evidence and continuity

Cutoff: previous run completed 2026-10-23 10:09:03 UTC, supplied by cron. Four new first versions and one revised preprint selected. Huang's arXiv submission history gives October 23 at 17:53:14 UTC. Batique et al. was posted October 24; Luan et al. and ALHENA were posted October 25; scLSD is an October 25 revision of a March preprint. Posting labels, not DOI date strings or erroneous extractor metadata saying January 1, establish freshness. The scLSD revision note reports new benchmarking and experimental-data comparisons; individual additions were not version-diffed. Preserve its dated PDF rather than invent a revision number.

All results are author-reported, not independently reproduced. Most assessments are based on substantive primary abstracts. Additional uncertainty-paper methods, results and limitations were recovered through indexed primary-PDF text. Full-text/PDF retrieval was attempted, but one combined output spilled to an inaccessible local cache and other extractions were incomplete; no complete full-paper audit is claimed. No withdrawal notice appeared in the inspected records.

Available tools: web search/extract, session recall, Obsidian append. Discovery exposed no direct vault search/read, filesystem, terminal, or skill-manager capability. Consequently current canonical notes could not be read afresh, local cached full text could not be paged, and this append cannot be independently read back. Tool acceptance is not independent verification. Do not treat this run as verified vault-wide deduplication or a completed full-text methods audit.

Continuity recovered from prior radar session cron_b7fccc11fa73_20261023_100008, message 11643, and the October 26 strategy session cron_952fb3b6f0a6_20261026_020028, message 12682. Previous radar selections were DynaVelo, GeoSinkhorn Flow, Foundation Models Improve Perturbation Response Prediction, Gate-Based Feature Importance, and scRhythmBayes. None is repeated. Two history searches covering current titles, method names and IDs found no previous assistant matches. This establishes history-level deduplication only.

Comparison basis: recovered Obsidian material describes scGPT/UCE identity plus cell-type-stratified environmental expression, with graph/attention/perturbation-decoder extensions proposed, not a verified implementation. The latest strategy prioritizes a nuisance-aware measured-target context-value test in held-out donors before architecture expansion. Canonical disease focus remains schizophrenia/human DLPFC; NIA aging/AD feasibility is a separate branch. Relevant notes: [[02_Projects/AIVC/current-state]], [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/literature/2026-10-23-literature-radar]], [[09_Planning/weekly-strategies/2026-10-26-AIVC-GeneBridge-weekly-strategy]].

Search coverage: targeted arXiv, bioRxiv and publisher searches; bioRxiv bioinformatics and recent listings; arXiv q-bio listing. The date-bounded arXiv API could not be extracted because of an unexpected content type. Broad web searches and primary listings were used instead. Some listings/extracts were partial or stale; this is a best-match shortlist, not an exhaustive census. Domain reference consulted: https://raw.githubusercontent.com/GPTomics/bioSkills/main/machine-learning/model-validation/SKILL.md .

## 1. READ NOW — Shared clones inflate perturbation reproducibility

**Citation:** Huang X. Shared clones make random cell halves look reproducible in pooled screens. arXiv:2610.32962v1 (2026), submitted October 23, 17:53:14 UTC.
**Source:** https://arxiv.org/abs/2610.32962v1
**HTML:** https://arxiv.org/html/2610.32962v1
**Research problem:** Random-cell split-half agreement is used to define reliable perturbations and benchmark ceilings, but descendants of the same transduced founder can appear in both halves.
**Method:** Compare random halves with independent transductions using null perturbations; test clone-disjoint splits using T-cell receptor constant regions or vector clone barcodes; relate shared expression components to effective clone number. [Abstract.]
**Key result:** In a primary T-cell screen, null perturbations aligned almost always between random halves but only about half the time between independent replicates. Clone-disjoint halves largely removed the excess agreement. Most evaluated cross-state transfer models fell below a perturbation-agnostic baseline when scored against another transduction. The reported artifact was much smaller in cell lines and smallest in non-dividing neurons. [Abstract; indexed PDF introductory results.]
**What is new:** A specific, experimentally anchored diagnosis of hidden clone-level pseudoreplication in reliability labels and perturbation-transfer benchmarks—not merely a generic warning about train/test leakage.
**Why it matters for AIVC:** Donor holdout alone may be insufficient for future cultured neural perturbation datasets if transductions, clones or cultures remain shared across evaluation units. It also qualifies the October 23 recommendation to stratify by reproducible perturbation signal: reliability must be estimated from genuinely independent units.
**What is weak / unresolved:** Preprint evidence; the magnitude is system dependent and smaller in the reported non-dividing neural data. Clone-disjoint splitting is a diagnostic, not proof that every batch or biological dependence is removed. Do not assert that this artifact exists in the user's postmortem Xenium data or that every perturbation model fails.
**Future research idea:** Build a neural perturbation evaluation with independent culture/transduction/donor units, null guides and clone-aware diagnostics. Compare apparent context gains and reliability ceilings under random-cell versus independent-unit scoring while holding the response predictor fixed.
**Decision:** READ NOW for benchmark design and K99 rigor, before selecting a perturbation dataset.

## 2. READ NOW — Uncertainty can be calibrated yet uninformative

**Citation:** Batique T, Nonchev K, Koelzer VH, Ratsch G. Probabilistic uncertainty in virtual spatial transcriptomics from histology is largely redundant with the predicted mean. bioRxiv v1, posted October 24, 2026. DOI: 10.64898/2026.10.23.760875.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.23.760875v1
**PDF:** https://www.biorxiv.org/content/10.64898/2026.10.23.760875v1.full.pdf
**Research problem:** Determine whether a predicted expression distribution identifies unreliable predictions, rather than merely reflecting expression-dependent variance.
**Method:** Across melanoma, lung and kidney cancer cohorts, compare probabilistic likelihoods, approximate Bayesian uncertainty and histology-free/training-free controls. Evaluate calibration and error informativeness after accounting for predicted mean, plus selective utility. The primary text describes frozen image embeddings with expression readouts. [Abstract; PDF Introduction, Methods 3.1, Discussion.]
**Key result:** The predicted mean largely explains uncertainty–error association; residual information about large errors is weak. Histology-free distributions can achieve comparable calibration. Uncertainty can still flag some synthetic image artifacts, so the finding is not that it is universally useless. [Abstract; PDF Results and Limitations.]
**What is new:** A mean-conditioned evaluation framework distinguishing calibrated distributions from uncertainty that adds useful per-prediction error information in virtual ST.
**Why it matters for AIVC:** A probabilistic decoder or uncertainty-aware GeneBridge extension cannot support reliability claims through calibration alone. Evaluate whether uncertainty identifies wrong spatial predictions beyond what expression magnitude already reveals.
**What is weak / unresolved:** Primarily within-cohort held-out-patient evaluation, no real scanner/staining/batch shifts; one frozen image encoder excludes representation uncertainty; measured ST noise cannot be separated from model error without replicate measurements. The trunk was not optimized for state-of-the-art expression prediction. Results are not a direct test of the proposed AIVC decoder. [PDF section 6.]
**Future research idea:** On protected measured Xenium targets, test error ranking and selective prediction against predicted-mean-only baselines, stratified by gene/cell type and evaluated by donor. Then assess genuine cohort/assay shift separately; keep calibration, error informativeness and out-of-distribution detection as distinct endpoints.
**Decision:** READ NOW for evaluation design; potential rigorous methods contribution rather than another architecture branch.

## 3. READ NOW — Centered cross-context perturbation transfer

**Citation:** Luan H, Chen L, Yu G, Yang Y. Centered cross-context perturbation transfer on the public 2025 Virtual Cell Challenge benchmark. bioRxiv v1, posted October 25, 2026. DOI: 10.64898/2026.10.20.760514.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.20.760514v1
**Research problem:** Transfer expression directions and differential-expression priority between cellular contexts without a large response model.
**Method:** Center an independent KOLF2.1J perturbation source using known training targets; transfer response signs and magnitude ranks; combine with a differential-expression kernel fit to H1 CRISPRi training targets; render predicted means using isotonic regression. [Abstract.]
**Key result:** On retrospectively evaluated public TEST100, reported DES 0.371834, PDS 0.8614 and MAE 0.302206. With reconstructed historical anchors the composite was 0.341344 versus archived champion 0.340052. Source centering improved development PDS across all three training folds and official validation. [Abstract.] Values are copied as author-reported, not recalculated or reproduced.
**What is new:** A compact, explicitly centered cross-context transfer procedure that separates response direction, ranking and mean calibration.
**Why it matters for AIVC:** A direct simple comparator for a biology-plus-perturbation graph transformer. Better context alignment may matter more than decoder sophistication. Separate the value of additional response data from the value of architecture.
**What is weak / unresolved:** Retrospective comparison uses an external source released in 2026 against a 2025 competition, with reconstructed scoring anchors. It is NOT evidence of winning the original blind competition under identical information. The abstract reports higher DES but lower PDS and zero normalized MAE contributions for both methods; composite superiority is not superiority on every endpoint. Complete leakage, source-overlap and model-freezing audits remain undone. No neural/SCZ validation was established.
**Future research idea:** Under an identical external-data budget, compare centered response transfer, ridge/kNN and the proposed graph transformer on unseen targets and independent neural donors/contexts; evaluate signs, DE ranking and magnitude separately. Add spatial context only after these controls are fixed.
**Decision:** READ NOW as a baseline and a warning against headline leaderboard comparisons.

## 4. SAVE — ALHENA

**Citation:** Giraud-Sauveur F, Blampey Q, Marza P, Benkirane H, Vakalopoulou M, Cournède PH, Christodoulidis S. ALHENA, an H&E encoder distilled from transcriptomic foundation models for multi-scale slide analysis. bioRxiv v1, posted October 25, 2026. DOI: 10.64898/2026.10.20.760439.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.20.760439v1
**Research problem:** Make cell- and neighborhood-level transcriptomic information useful when only histology is available at deployment.
**Method:** Adapt a pretrained H&E encoder using pairwise similarities from frozen cell and neighborhood transcriptomic teachers, without direct gene-level training targets. Training uses paired H&E–Xenium data; inference uses H&E alone. [Abstract.]
**Key result:** Trained on 25 Xenium sections from 13 organs and more than 8 million cells; authors report improved patient-level signature prediction, local gene-expression readouts and cell-type separability while largely retaining general pathology performance. External H&E atlas-label transfer was reported without retuning. No numerical superiority is claimed here because the comparative tables were not audited. [Abstract.]
**What is new:** Multi-scale transcriptomic similarity distillation rather than direct gene regression, connecting cell and neighborhood representations to an image-only deployment interface.
**Why it matters for AIVC:** Directly relevant to identity-plus-environment representation design and a potential lower-cost deployment path. It also reduces the novelty of merely adding a neighborhood teacher or multiscale encoder.
**What is weak / unresolved:** Millions of cells do not substitute for independent tissue/patient diversity. Full split construction, teacher exposure and external neural-domain transfer require checking. Morphology-derived representations do not establish perturbation responsiveness, causal context effects or accurate unseen genes in SCZ cortex.
**Future research idea:** After measured context value is established, test whether a frozen neighborhood teacher can be distilled into H&E while preserving held-out-donor prediction gains. Compare cell-only versus cell-plus-neighborhood teachers, matching training tissues and auditing teacher exposure.
**Decision:** SAVE for a later multimodal deployment branch; do not add it to the immediate measured-target pilot.

## 5. SAVE — scLSD, revised preprint

**Citation:** Poursina A, Hajhashemi S, Saberi A, Mikaeili Namini A, Madrigal A, Emad A, Najafabadi HS. A latent space thermodynamic model of cell differentiation. bioRxiv, revision posted October 25, 2026; originally a March preprint. DOI: 10.64898/2026.03.04.709512.
**Source:** https://www.biorxiv.org/content/10.64898/2026.03.04.709512
**Dated revision:** https://www.biorxiv.org/content/biorxiv/early/2026/10/25/2026.03.04.709512.full.pdf
**Research problem:** Infer continuous differentiation dynamics, fate commitment and plasticity from time-ordered single-cell measurements.
**Method:** Jointly learn latent cell states, a differentiable Waddington-like potential and local entropy associated with plasticity; use a neural ODE to reconstruct developmental trajectories. [Abstract.]
**Key result:** Authors report recovery of lineage hierarchies, fate prediction for unseen cell types, and improved directional/fate accuracy over tested trajectory methods. In silico regulator perturbations reshape the learned landscape. The revision note announces new benchmarks and experimental-data comparisons; the precise change set and numerical gains were not verified. [Abstract and revision footnote.]
**What is new:** A potential-plus-plasticity formulation for latent cellular dynamics. This run's new event is the expanded revision, not first disclosure of scLSD.
**Why it matters for AIVC:** An alternative dynamical inductive bias to graph attention or a generic conditional decoder, especially if the independent program later includes measured developmental neural perturbation time series.
**What is weak / unresolved:** A learned landscape and simulated gene perturbations do not uniquely identify causal mechanisms. Time-ordered developmental evidence does not automatically transfer to mature postmortem DLPFC. Potential-based dynamics impose assumptions that should be tested, not sold as proof of physical thermodynamics. This assessment is abstract-level; the PDF extraction mostly recovered headers/footers rather than usable methods.
**Future research idea:** In an actual neural differentiation time course, compare context-conditioned potential dynamics with an unconstrained neural ODE and simple transfer, holding out both interventions and independent cultures. Ask whether environment improves measured fate/response prediction rather than landscape appearance.
**Decision:** SAVE for a future time-resolved experimental branch; no immediate architecture expansion.

## Program implication and proposed actions

The strongest immediate contribution is evaluation, not a new transformer: independent-unit perturbation reliability, uncertainty informativeness beyond predicted mean, and fair data-matched simple transfer baselines. ALHENA and scLSD are later branches. These are proposed research ideas, not assigned obligations, new deadlines, completed experiments or demonstrated grant feasibility. No project scope, tracker, calendar, GitHub record or canonical implementation specification was changed. This note is the only requested literature-memory write; independent read-back is unavailable in this run.
