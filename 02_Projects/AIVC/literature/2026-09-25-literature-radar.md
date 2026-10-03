---
type: literature-radar
project: AIVC
run_date: 2026-09-25
previous_run: 2026-09-23T10:08:23
status: primary-source-triage-with-coverage-gaps
---

# AIVC Literature Radar — 2026-09-25

## Scope and evidence

Five ranked papers newly published or announced since the previous run. Date eligibility uses public arXiv announcement/cross-listing as well as journal publication, NOT submission timestamps alone. CellAudit was submitted September 23 at 02:07:27 UTC, before the previous run, but appears under September 24 in arXiv's q-bio.QM announcements. SpaFactor's abstract lists submission September 23 at 09:59:22 UTC, also before the cutoff, and it appears under September 25 in q-bio.QM. These are newly announced items, not claims that all five were first submitted after the cutoff. Hou et al. was submitted September 23 at 23:57:50 UTC; PRAXIS September 24 at 08:29:53 UTC. DePass was published September 24, confirmed by publisher and Crossref.

Primary discovery/verification: https://arxiv.org/list/q-bio.QM/recent and https://arxiv.org/list/q-bio.QM/recent?show=50; arXiv date-bounded query for perturbation AND cell; individual versioned abstracts/HTML/PDF; DePass publisher page and https://api.crossref.org/works/10.1038/s41556-026-02067-8. The first date-bounded arXiv query produced relevant records, but a second single-cell/transcriptomics query missed items recovered by category listings. Search-engine date filters also returned old papers. bioRxiv interval endpoints repeatedly failed/time-out, so bioRxiv coverage is incomplete. Do not infer that nothing new appeared there.

This is literature triage, not reproduced benchmarking. CellAudit methods sections were retrieved; some long-page material was omitted. DePass abstract, data/code availability and extended-data captions were retrieved, but main methods were subscription-limited. SpaFactor abstract and methods/ablation excerpts were retrieved. Hou et al. and PRAXIS had primarily abstract/opening-page coverage. No code was executed. Results are author-reported; weaknesses and research ideas are our assessments unless explicitly described as reported limitations. Four arXiv preprints are not established as peer reviewed; DePass is a Nature Cell Biology technical report.

## Project context — newer user outline takes precedence

Comparison is against the September 23 user-supplied outline preserved in [[02_Projects/AIVC/project-outline]], recovered from the actual note-writing/verification conversation via session_search (session cron_b7fccc11fa73_20260921_100029, messages 3662–3668), not from a fresh vault read. It supersedes generic earlier reconstructions of intended architecture. Core: identity + environment → universal representation (UR) → virtual instrument (VI) → cell-type-specific activity; keep identity fixed for environment changes. The PDF specifies 20 μm cell-type-stratified neighborhoods, attention, MSE plus sparsity, and identity-matched environment swaps. The companion diagram separately proposes multi-scale hierarchical cross-attention, Xenium/snRNA-seq/Visium/Perturb-seq, confidence-weighted imputation, gene perturbation embeddings, and a conditional VAE with donor-held-out tests. Neither source was designated to replace the other; both remain proposed designs, not established results. Earlier NIA aging/AD recommendations do not override the user-supplied SCZ/NTC design.

Direct Obsidian read/search and filesystem execution tools were not exposed in this run. The previous September 23 report was recovered from session history: DeepSCENIC, SPECTRA, Speciesformer, upper-layer SST interneuron depletion in SCZ, and mc-ASTRA. None is repeated. Session searches for all selected method names/identifiers returned no prior matches, but this is not a vault-wide deduplication guarantee. This is an additive literature note, not a revision of canonical project facts. An independent live read-back of this note cannot be performed with the exposed tools.

## 1. CellAudit — READ NOW

**Citation:** Li, Mengran; Li, Bo; Zhang, Chengyang; Yan, Yang; Xu, Jinfeng; Tang, Zhenchao (2026). *Discover, Falsify, Revise: Auditing Input-Use Claims from Source Code to Predictive Contribution in Agent-Discovered Cell Models*. arXiv:2609.27234v1. Submitted September 23; q-bio.QM announcement September 24.

**Source:** https://arxiv.org/abs/2609.27234v1
**Methods read:** https://arxiv.org/html/2609.27234v1, abstract and Sections 1–5.

**Research problem:** A response predictor can score well while ignoring the intervention it claims to use.

**Method:** Separate source-code consumption, fitted input dependence, and target-relevant predictive contribution. Combine code inspection with matched input replacements on frozen checkpoints, preserving other inputs; register replacements, group-level uncertainty and audit rules. Use evidence to guide agent-generated model revisions.

**Key result:** On BBBC047, an agent-selected predictor achieved Global PCC 0.3153 versus 0.3142 for control-only while remaining exactly invariant to compound replacement. Singleton key–value attention blocked the compound-query route. Among 48 audited candidates, 47 changed predictions on compound replacement in both held-out folds, but only 20 had target-loss gain intervals above zero in both folds. sci-Plex audit-feedback improvements had intervals spanning zero. Compound-use support did not persist after fixed-design refitting on an independent cohort, while dose contribution did.

**What is new:** Makes executable input-use claims falsifiable separately from prediction accuracy; response sensitivity alone is not sufficient evidence of useful input use.

**AIVC relevance:** Directly tests whether VI(c,e,p) uses neighborhood e and intervention p rather than predicting cell identity. Particularly relevant to hierarchical attention and identity-preserving environment swaps: nonzero attention or good reconstruction does not establish useful environment dependence.

**What is weak / unresolved:** Matched replacements test predictive reliance, not biological causality. Replacement support matters. BBBC036 and BBBC047 are linked rather than independent cohorts. sci-Plex splits hold out compound–cell-line combinations while both marginals are observed; this is not unseen-compound discovery. Evidence that the audit improves agentic search is suggestive, not conclusive.

**Future research idea:** Freeze an AIVC checkpoint and audit identity, neighborhood and perturbation branches separately using replacements matched for cell type, layer and experimental context; evaluate incremental measured activity-gene prediction over identity-only baselines on held-out donors. Keep donor selection and imputation fitting isolated from test data.

## 2. Causal discovery under selection and latent variables — READ NOW

**Citation:** Hou, Xiaotian; Park, Kwangmoon; Li, Hongzhe (2026). *Statistical Inference for Causal Discovery under Selection and Latent Variables via Single-Target Interventions*. arXiv:2609.28856v1. Submitted September 23, 23:57:50 UTC. University of Pennsylvania.

**Source:** https://arxiv.org/abs/2609.28856v1
**Evidence:** arXiv API abstract; https://arxiv.org/html/2609.28856v1 and PDF opening material.

**Research problem:** Hidden regulators and selection through cell survival, acquisition or preprocessing can corrupt GRN discovery from observational/interventional data.

**Method:** System-induced subgraphs represented through maximal ancestral graphs; two-stage model-free testing with single-target and soft interventions, explicitly allowing latent variables and selection.

**Key result:** API abstract states that interventions on every observed system variable suffice for unique identification and are necessary in the worst case; reports asymptotic family-wise error control conditional on sufficient first-stage power and quadratic constraint-query complexity. Illustration uses interferon-β-stimulated A549 Perturb-seq. The HTML abstract uses stronger shorthand necessity/sufficiency wording; retain the qualified API claim pending theorem-level review.

**What is new:** Connects intervention coverage, causal identifiability, computational query efficiency and error control under latent confounding/selection rather than assuming an observed-variable DAG.

**AIVC relevance:** Explains why identity-matched observational environment swaps do not automatically identify causal microenvironment effects. Suggests that uncertain/confounded regulatory edges should not be treated as a fully known causal prior.

**What is weak / unresolved:** Full identification requires extensive intervention coverage under assumptions; query complexity is not total computational cost or finite-sample power. Large numbers of genes, weak perturbations and selective cell loss may challenge applicability. A549 illustration is not demonstrated human-brain transfer. No response-prediction superiority is asserted here.

**Future research idea:** Construct an uncertainty-aware regulatory prior on a small experimentally covered neuronal gene panel; compare it with coexpression, directed prior and rewired controls while varying perturbation coverage and simulated selection.

## 3. DePass — READ NOW for multimodal representation

**Citation:** Li, Wei; Jiang, Yuanxiang; Zhao, Qingqing; Xu, Yang; Dai, Deli; Rong, Yu; Zhao, Xin; Zhang, Han (2026). *The dual-enhanced graph learning framework DePass allows paired data integration in single-cell and spatial multiomics*. Nature Cell Biology, published September 24. DOI: 10.1038/s41556-026-02067-8.

**Source:** https://www.nature.com/articles/s41556-026-02067-8
**Date/citation:** https://api.crossref.org/works/10.1038/s41556-026-02067-8

**Research problem:** Noise compounds across multi-omics assays, while integration methods often specialize in either single-cell or spatial data.

**Method:** Coupled enhancement–integration graph learning iteratively denoises paired modalities and refines joint embeddings.

**Key result:** Reports superior integration across six modalities, nine tissue types and thirteen platforms, and immune-niche/tumour substructure in in-house colorectal data. Extended-data captions show a cross-section RNA-to-protein prediction evaluation: models trained on Section 1 with raw/enhanced data and tested on raw RNA from Section 2. No independently verified numerical effect-size summary is available from the accessible text.

**What is new:** Noise enhancement and representation integration are coupled in a framework used across paired single-cell and spatial settings, rather than a generic graph added to one modality.

**AIVC relevance:** Comparator for the diagram's multimodal UR, confidence-weighted imputed expression and alignment losses. Provides a concrete warning that an integrated representation is a distinct objective from intervention prediction.

**What is weak / unresolved:** Requires paired data; not automatically usable for unmatched Xenium, snRNA-seq, Visium and Perturb-seq cohorts. Denoising could smooth disease/rare-state effects; that is a risk to test, not a demonstrated flaw. Better integration or cross-section protein prediction does not establish counterfactual validity or independent-donor transfer.

**Future research idea:** Compare raw-measured, DePass-enhanced and GeneBridge-confidence-weighted inputs to the same VI; score measured held-out activity genes and rare/layer-specific SCZ signals, never imputed targets alone.

**Reproducibility pointers from publisher, not executed:** https://github.com/zhanglabNKU/DePass ; https://depass.readthedocs.io/en/latest/ ; data DOI 10.5281/zenodo.21736075.

## 4. SpaFactor — SAVE as a lightweight context baseline

**Citation:** Ruan, Shiting; Ling, Xitong; He, Qiming; Yan, Ziyou; Yuan, Huaitian; Guan, Tian; Xiao, Ying; Guan, Xu; He, Yonghong (2026). *SpaFactor: Lightweight Spatial Context-Aware Gene Program Modeling for Histology-to-Transcriptomics Inference*. arXiv:2609.28563v1. Abstract lists submitted September 23, 09:59:22 UTC; q-bio.QM announcement September 25.

**Source:** https://arxiv.org/abs/2609.28563v1
**Excerpts:** https://arxiv.org/html/2609.28563v1 and https://arxiv.org/pdf/2609.28563

**Research problem:** Predict spatial expression from histology while capturing neighborhood context and coordinated gene programs without an elaborate graph prediction head.

**Method:** Frozen GigaPath image embeddings plus parameter-free local/regional within-slide summaries, a residual MLP for low-dimensional program activities, and shared gene loadings. The prediction head is lightweight relative to alternatives; the pretrained image backbone is not cost-free.

**Key result:** Reports best aggregate performance across five public cohorts, especially spatially variable genes. The retrieved ablation says removing both neighborhood summaries reduces Gene PCC by 2.37 percentage points and VR-PCC by about four; regional context alone recovers most performance.

**What is new:** Multi-scale context and shared program factorization provide a simpler alternative to complex graph heads.

**AIVC relevance:** Challenges whether the proposed hierarchical multi-scale cross-attention is necessary. Spatial benefit can come from simple neighborhood summaries rather than attention itself. This uses image-derived, not AIVC expression-derived, context, so a direct transfer is a proposed adaptation.

**What is weak / unresolved:** Observational histology-to-expression prediction, not perturbation response. Latent programs are not automatically mechanistic GRNs. Disease/donor transfer and pretrained-backbone leakage require audit; full benchmark protocol was not completely retrieved.

**Future research idea:** Build a donor-held-out expression-context analogue: concatenate identity with cell-type-stratified multi-radius mean features, predict low-rank activity programs with an MLP, and compare against the PDF attention head and diagram's hierarchical attention under identical folds.

## 5. PRAXIS-VirtualCell — SAVE

**Citation:** Ma, Zhenyu; Jiang, Xukai (2026). *PRAXIS-VirtualCell: A Programmable and Trustworthy Framework for Agentic Virtual Cell Experiments*. arXiv:2609.29221v1. Submitted September 24; announced September 25. Shandong University.

**Source:** https://arxiv.org/abs/2609.29221v1
**Evidence:** API abstract and https://arxiv.org/pdf/2609.29221v1 opening pages; HTML unavailable.

**Research problem:** Heterogeneous data, predictors, intervention specifications and validation evidence lack a common auditable execution structure.

**Method:** Modular data/model/perturbation/adaptor/runtime/evidence organization, biological contracts and evidence-aware execution; agent orchestration translates natural-language questions into traceable virtual experiments.

**Key result:** Reports task support spanning E. coli, yeast and human K562, distinguishing supported predictions, extrapolation and abstention. The retrieved evidence provides no quantitative accuracy improvement and does not establish one transferable cross-species predictive model.

**What is new:** A framework for organizing virtual experiments and their evidence, rather than a new response-prediction architecture.

**AIVC relevance:** Useful for separately tracking the baseline PDF and expanded conditional-VAE design, and labeling environment-only, gene-only and joint queries by supporting data and validation status.

**What is weak / unresolved:** Auditable execution is not biological validity. Abstract-level evidence cannot establish useful uncertainty calibration or superiority over task-specific pipelines. Agentic infrastructure is lower priority than a validated AIVC baseline.

**Future research idea:** Give each VI query an explicit evidence record: observed assay support, intervention/context range, donor scope, measured-versus-imputed inputs, model version and an abstention reason for unsupported joint interventions.

## Program implication — recommendation, not a canonical design change

A strong next experiment is not another architecture expansion: establish whether environment and perturbation inputs add reproducible, measured-target predictive value beyond identity-only and simple pooled-context baselines. CellAudit supplies the falsification discipline; Hou et al. defines a causal-identification caution; DePass supplies representation competition; SpaFactor supplies a complexity control; PRAXIS supplies evidence bookkeeping. None establishes SCZ/AD therapeutic validity or an NIA-ready aging premise.

## Stable ranks for downstream brief

1. CellAudit — arXiv:2609.27234v1 — READ NOW.
2. Causal discovery under selection and latent variables — arXiv:2609.28856v1 — READ NOW.
3. DePass — DOI:10.1038/s41556-026-02067-8 — READ NOW (representation).
4. SpaFactor — arXiv:2609.28563v1 — SAVE (baseline).
5. PRAXIS-VirtualCell — arXiv:2609.29221v1 — SAVE.

Run-day selection: ranks 1–2. Off-day selection: ranks 3–5, labeled stale with this run date. Preserve ranks; do not replace ranks 3–5 with repeated 1–2.
