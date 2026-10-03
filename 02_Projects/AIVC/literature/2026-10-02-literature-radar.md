# AIVC Literature Radar — 2026-10-02

## Scope, provenance, and limitations

Intended window: after the previous run, 2026-09-30 10:07:21 UTC, through this scheduled run. Selected papers have first-publication/posting dates September 30–October 1. The two September 30 bioRxiv papers have day-level dates only; publication after the exact previous-run timestamp is not established. They are newly surfaced in this run, not verified hour-level additions.

Direct vault search/read tools were unavailable in this session. Comparison used recalled Obsidian review material and session-history copies of the user's AIVC notes (September 12 methods/goals/decisions), plus the September 30 radar and October 1 Morning Brief. This is NOT a fresh audit of current canonical notes. The relevant documented goals are graph-vs-pure-transformer comparison, unseen-perturbation generalization, explicit/testable graph assumptions, multimodal/spatial context, and schizophrenia relevance. Recalled later reviewer material raises aging/AD/K99 evaluation and validation needs. No project status or canonical design facts were changed.

Deduplication: none of the five selected titles matches the recovered September 30 selections (BioPert, LangPatch, DRIFT, SpatialTRACE, CancerZigZag). Exact-title/identifier searches in available session history found no earlier reports of today's selections. This does not establish vault-wide uniqueness. arXiv API returned 'Rate exceeded'; discovery continued through web search and primary pages. Several full-text extractions were partial; evidence depth is specified below. Results are author-reported, not independently reproduced. Critiques and research ideas below are analyst assessments, not claims made by the authors.

## 1. READ NOW — Recoverable resolution / context geometry compression

Citation: Huang, Y., Wang, H., Li, C. & Wilson, P. (2026). The recoverable resolution of cellular perturbation-response prediction. bioRxiv v1, posted October 1, 2026. DOI: 10.64898/2026.09.30.755756.
Source: https://www.biorxiv.org/content/10.64898/2026.09.30.755756v1
PDF examined: https://www.biorxiv.org/content/10.64898/2026.09.30.755756v1.full.pdf
Evidence: PDF introduction/results pp. 2–4 and methods pp. 11–12; extraction was truncated elsewhere and some equations were garbled.

Research problem: High accuracy for final expression may hide failure to predict how a perturbation acts differently across donors or cellular contexts.
Method: Separate baseline identity, shared perturbation response, and context-specific response. Evaluate guide-/replicate-disjoint truth, held-donor prediction, official zero-shot State outputs, and target-sealed completion of a replicated Tahoe drug-response matrix.
Key result: In the T-cell analysis, state Pearson correlation was approximately 0.989 while donor-specific response R-squared was non-positive for ridge, bilinear, and MLP predictors. In an all-but-one completion setting with 4,649 of 4,650 entries observed, full-response recovery reached 0.6945 but context-specific recovery was 0.1107. Recovery is the paper's cross-replicate statistic, NOT ordinary R-squared. Predefined pathway summaries were more recoverable than gene-level profiles.
New: Explicit 'identity–operator gap' and context geometry compression distinguish context recognition from recovery of a context-dependent response rule. The contribution is an evaluation framework and empirical diagnosis, not a new large architecture.
AIVC relevance: Direct challenge to the premise that a richer cell/context embedding necessarily makes environment-dependent perturbation responses predictable. Supports a focused K99 aim on demonstrated, recoverable response resolution rather than whole-transcriptome simulation claims.
Weakness: The evidence is conditional on tested datasets, information sets, estimators and definitions. It does not prove an irreducible biological or universal model limit. State cytokine uncertainty was wide; the paper notes missing donor/replicate metadata for that analysis. No direct SCZ/DLPFC intervention validation.
Future idea: Compare identity-only, perturbation-only and identity-plus-neighborhood models on donor-held-out response residuals, with independent replicate ceilings and both gene- and prespecified pathway-level endpoints. Ask whether spatial context increases recoverable response information rather than only identifying tissue or donor.

## 2. READ NOW — Calibrated perturbation metrics

Citation: Miller, H. E., Mejia, G. M., Leblanc, F. J. A., Swain, B., Wang, B. & de Lima Camillo, L. P. (2026). Deep learning perturbation models can outperform baselines on calibrated metrics. Nature Biotechnology, published online October 1, 2026. DOI: 10.1038/s41587-026-03307-w.
Source: https://www.nature.com/articles/s41587-026-03307-w
Author/date verification: https://api.crossref.org/works/10.1038/s41587-026-03307-w
Evidence: Article abstract/main text and portions of methods, especially Figures 1–2 and model descriptions. Not a full supplementary-table audit.

Research problem: Do apparently weak perturbation models lack biological signal, or do evaluation metrics fail to detect that signal?
Method: Construct a DEG-informed interpolated-duplicate positive control, use a mean negative control, and measure metric sensitivity with dynamic range fraction (DRF); assess 14 datasets and 18 metrics and benchmark diverse model families.
Key result: Weighted/rank-based metrics better distinguish informative controls from null predictors. scGPT and GEARS often beat uninformative baselines under better-calibrated metrics; newer models perform more strongly. PRESAGE exceeded the additive baseline on 15 of 18 metrics in Wessels23. This is not universal dominance on every dataset.
New: Positive-control calibration tests the benchmark's ability to detect perturbation-specific information, rather than interpreting baseline rankings without checking metric sensitivity.
AIVC relevance: Refines, rather than removes, the requirement to beat simple baselines. A graph-transformer comparison needs credible controls, multiple prespecified metrics and strong contemporary comparators; raw MSE alone is inadequate evidence for either success or failure.
Weakness: The positive control uses measured perturbation outcomes and DEG statistics; it is a benchmark diagnostic, not a deployable unseen-target predictor or an absolute performance ceiling. DEG weighting and control choices influence conclusions. Calibrated metrics do not establish tissue-level causality or clinical utility.
Future idea: Build a preregistered AIVC evaluation suite with replicate positive controls, mean/linear/additive negatives, weighted error, retrieval and residual response metrics. Keep test-derived calibration quantities confined to evaluation, never training or model selection.

## 3. READ NOW — Biological-input utilization audit

Citation: Fang, A., Thoduguli, N., Fesser, L., Zhang, H., Kakade, S. & Zitnik, M. (2026). When Do Biological Reasoning Models Use Their Biological Inputs? arXiv:2610.00898v1, submitted October 1, 2026.
Source: https://arxiv.org/abs/2610.00898v1
Evidence: Primary abstract/author list and introduction excerpt; detailed methods/tables were not fully extracted.

Research problem: Does high accuracy mean a biological reasoning model actually uses its biological foundation-model representations?
Method: Across six models, shuffle or perturb biological inputs while holding other inputs fixed, create conflicts between representations and biological text, fit linear probes and inspect reasoning traces/checkpoints.
Key result: BioReason and BioReason-Pro followed conflicting text in 97.9% and 99.7% of cases. Their relevant biological representations contained task information detectable by linear probes, but contributed little to overall model performance. Other tested systems, including CellWhisperer, did benefit from biological inputs; this is not a blanket failure of multimodal biology models.
New: Separates information present in an encoder from information actually used by the downstream model. Higher post-training accuracy did not necessarily increase biological-input contribution.
AIVC relevance: Direct operational test of the existing goal to distinguish attention-based generalization from shortcuts. A graph, spatial encoder or language-derived prior can be present yet functionally ignored.
Weakness: The audited systems are primarily LLM-linked reasoning models, not all perturbation simulators. Conflicting/shuffled inputs can be out of distribution; utilization changes alone do not establish causal correctness.
Future idea: Audit graph/transformer AIVC models with matched, missing and within-cell-type permuted neighborhood inputs, degree-preserving graph rewiring, and text-versus-expression conflicts. Compare performance loss with a linear probe on the same encoder outputs.

## 4. READ NOW — ProxiNet

Citation: Zhan, Y., Yan, B., Zhang, A., Kellis, M. & Sun, N. (2026). ProxiNet transfers spatially learned cellular proximity to dissociated single-cell transcriptomes. bioRxiv v1, posted September 30, 2026. DOI: 10.64898/2026.09.25.754372.
Source: https://www.biorxiv.org/content/10.64898/2026.09.25.754372v1
Evidence: Primary metadata/abstract and PDF opening. PDF body, quantitative effect sizes, architecture details and split integrity were not fully audited.

Research problem: Dissociated single-cell RNA-seq lacks observed cellular neighborhoods.
Method: Learn pairwise proximity signatures from spatially supervised transcriptomic references, transfer them to dissociated cells and use gradient-based attribution to examine predictive programs.
Key result: Authors report proximity prediction across brain regions and technologies, including zero-shot cross-technology transfer, recovery of anatomical structure in coordinate-known data, and an AD-associated inferred neighborhood at 8 months with astrocyte/neuron transcriptional differences. No numerical accuracy is asserted here because benchmark tables were not inspected.
New: Transferable pairwise proximity is the representation, rather than merely assigning cell types or reconstructing complete coordinates.
AIVC relevance: A concrete candidate baseline/comparator for adding neighborhood priors to nonspatial training data and for GeneBridge-linked context modeling; includes brain and AD applications.
Weakness: Predicted proximity is not an observed neighbor, a measured ligand–receptor interaction, or an intervention effect. Cell-type/anatomical shortcuts and disease-domain shift must be tested. Inferring neighbors from expression and then predicting expression can create circular evidence.
Future idea: Compare actual spatial neighbors, ProxiNet-derived neighbors, cell-type-matched null neighbors and no-neighborhood inputs on held-out donors. Measure added perturbation-response information and uncertainty, not merely reconstruction.

## 5. SAVE — CycloCross

Citation: Hacquard, O., Tokuta, Y., Imoto, Y., Nakamura, T., Deguchi, S., Nagano, M., Saitou, M. & Hiraoka, Y. (2026). CycloCross: Adversarial single-cell RNA-seq data translation across species. bioRxiv v1, posted September 30, 2026. DOI: 10.64898/2026.09.24.754263.
Source: https://www.biorxiv.org/content/10.64898/2026.09.24.754263v1
Evidence: Primary metadata and abstract; PDF extraction was partial and did not support a numerical benchmark comparison.

Research problem: One-to-one ortholog mapping excludes gene duplications, losses and functional divergence in cross-species single-cell modeling.
Method: CycleGAN-based adversarial translation of observed source-species scRNA-seq into target-species profiles without a priori gene correspondences.
Key result: Reports mouse–macaque–human germ-cell translation preserving developmental temporal patterns, interpolation/extrapolation at missing time points, and more plausible generation in limited-data settings. Magnitudes and benchmark fairness remain unaudited.
New: Orthology-free profile translation learns cross-species mappings from real source cells rather than requiring fixed gene correspondences or generating only from noise.
AIVC relevance: A potential comparator for a later mouse-to-human transfer aim, not a reason to expand the immediate SCZ/DLPFC architecture.
Weakness: Adversarial distribution matching and cycle consistency do not uniquely identify biological correspondence. Germ-cell developmental transfer is not neuronal disease or perturbation validation; plausible synthetic states can still be mechanistically wrong.
Future idea: Benchmark orthology-free and orthology-constrained transport on matched mouse/human perturbation signatures, using held-out interventions and known conserved-response anchors. Reject mappings that improve distributional similarity but reverse response direction.

## Synthesis and proposed next action

These papers support a validation-first AIVC contribution: calibrate metrics, isolate context-specific response beyond identity/shared effects, and prove that biological inputs are used. Graph/transformer novelty alone remains insufficient. Proposed next experiment: on a locked donor-level split, compare simple baselines and a minimal context model with input-shuffling controls, reporting replicate-calibrated gene/pathway response recovery. This is a proposal, not a created task or completed experiment.

Excluded from the five: EpiZoo first posted September 29 (outside window); Chen & Hicks virtual-spatial-transcriptomics v2 posted October 1 but explicitly leaves main conclusions unchanged; Count Flow Map v2 was revised September 30, but the revision's substantive novelty was not established. Do not label these as new first-publication findings in this run.
