# AIVC Literature Radar — 2026-10-05

## Run status: partial coverage; not a fresh five-paper shortlist

Window: after 2026-10-02 10:07:21 UTC, the previous-run timestamp supplied in the job, through the current scheduled run. No set of five qualifying new papers was established. Do not treat the candidates below as five fresh first-publication findings or fill missing slots with prior-run papers.

Live web discovery covered virtual cells, single-cell perturbation prediction, causal extrapolation, gene/graph transformers and spatial transcriptomics. The date-bounded arXiv API request failed; the bioRxiv date API extraction encountered HTTP 429. Alternative web search, arXiv's sorted search page, primary abstract pages and versioned full texts were used. Search indexing/date filters returned older work and incomplete results. This is insufficient to conclude that no new papers exist.

Direct Obsidian search/read tools and filesystem tools were unavailable. Comparison used session-history copies of the September 12 AIVC methods/goals/decisions and the October 2 radar's complete saved-note payload and final report. This is not a current canonical-vault audit. Supported design interests: graph versus pure-transformer comparison, explicit/testable graph assumptions, unseen-perturbation generalization, multimodal/spatial conditioning and schizophrenia/DLPFC relevance. No canonical project status was changed.

Deduplication: recovered all five October 2 selections and excluded them from today's recommendations: recoverable resolution/CGC, calibrated perturbation metrics, biological-input utilization, ProxiNet, CycloCross. Chen & Hicks spatial-expression paper v2 was also considered by the prior run and is excluded again. Session searches for 2609.34482, 708202, Risk-Calibrated, and Benchmarking niche found no matches; this is not proof of vault-wide uniqueness.

## 1. SAVE — recently revised causal-methods candidate

Citation: Yang, F., Lei, H., Chen, Y. & Du, J.-H. (2026). Risk-Calibrated Balancing for High-Dimensional Causal Extrapolation. arXiv:2609.34482v2.
Source: https://arxiv.org/abs/2609.34482v2
Full text examined: https://arxiv.org/html/2609.34482v2
Comparison version: https://arxiv.org/html/2609.34482v1
Freshness: v1 September 28; v2 October 2 at 15:43:37 UTC, definitively after the supplied previous-run timestamp. This is a revision, not a newly introduced paper. Both versions already contain the central method and theory; available text comparison does not establish a new methodological contribution specific to v2.

Research problem: Covariate balancing under weak source–target overlap can concentrate weights and increase variance, so better balance need not improve counterfactual prediction.
Method: Ridge augmentation of normalized base weights, with penalty selected by target-specific conditional prediction risk. Decomposes risk into remaining imbalance and weight-induced variance; feasible tuning uses an independent target evaluation sample.
Key result: Authors report lower prediction error for most perturbation–outcome pairs relative to each base estimator in a K562 Perturb-seq setting with 48 control profiles and 500 covariate dimensions. Simulation results favor the spectral target-aware rule over source-only tuning in most tested configurations. Results are author-reported; no reproduction or complete application-table audit was performed.
What is new in the paper: Explicit risk-based tuning for the target counterfactual mean rather than relying on balance alone; theory links covariance geometry, mean shift and weight concentration to extrapolation risk. Not a new graph or transformer architecture.
Why it matters for AIVC: Adds a useful statistical baseline and overlap diagnostic when comparing graph/transformer models across cellular contexts. Warns that integration/alignment success is not evidence of reliable response transfer.
What is weak: Causal interpretation requires consistency, unconfoundedness and positivity in the chosen features. Theory depends on predictive-model and asymptotic assumptions. It does not recover causal effects under arbitrary hidden confounding or zero support. Model-based counterfactual prediction intervals are explicitly NOT frequentist confidence intervals for a fixed ATT. K562 evidence does not establish transport to neuronal disease contexts.
Future research idea (analyst proposal): Compare simple ridge, risk-calibrated balancing and AIVC context models across donor/cell-type-held-out splits stratified by overlap. Investigate an abstention rule for poorly supported contexts; this rule is proposed, not established by the paper.
Evidence locations: arXiv submission history; full-text Sections 1.1, 2.1–2.3, 4.3 and 5.2. Mathematical notation was partially lost in extraction; do not implement from this extracted text alone.

## 2. SAVE — spatial benchmark revision; exact cutoff uncertain

Citation: Wang, Y., Chen, Y., Yang, L., Wang, C., Cai, J. & Xin, H. (2026). Benchmarking niche identification via domain segmentation for spatial transcriptomics data. bioRxiv, version 3. DOI: 10.64898/2026.02.27.708202.
Source: https://www.biorxiv.org/content/10.64898/2026.02.27.708202v3
PDF examined: https://www.biorxiv.org/content/10.64898/2026.02.27.708202v3.full.pdf
Freshness: v3 posted October 2, 2026. Posting time is unavailable, so its order relative to the prior run is unresolved. Earlier-version retrieval failed; substantive revision novelty is unverified. Treat as a newly surfaced candidate, not a verified newly published method.

Research problem: Spatial clusters that maximize transcriptomic/compositional homogeneity may not recover functional multicellular niches.
Method: Expert-annotated human reactive lymph-node CosMx reference; comparison of 16 domain-segmentation algorithms; preprocessing, core-lineage weighting, mixed-niche simulations, DLPFC and embryonic mouse brain comparisons, and scalability evaluation.
Key result: Authors report that most default methods fail to match biologically annotated niche boundaries. Weighting core functional lineages improves niche recovery for selected frameworks, including GraphST and MENDER.
What is new in the paper: Explicitly distinguishes anatomical/domain segmentation from functional niche identification and tests failure under peripheral-cell mixing. No confirmed new contribution specific to v3 can be asserted.
Why it matters for AIVC: Spatial domains or cortical layers should not automatically be treated as causal signaling neighborhoods. Relevant to choosing the cell-level graph or context tokens for GeneBridge-linked AIVC conditioning.
What is weak: Main functional reference is a manually annotated lymph-node setting, not schizophrenia perturbation data. Annotation and lineage weighting encode prior knowledge; gains need independent tissue validation and protection against using evaluation labels to tune features. Spatial architecture agreement does not establish signaling causality or perturbation-response benefit.
Future research idea (analyst proposal): Compare k-nearest-neighbor graphs, domain-based context and lineage/signaling-weighted overlapping neighborhoods in a locked donor-held-out AIVC benchmark. Evaluate response residuals rather than cluster-label agreement alone.
Evidence locations: PDF Abstract, Introduction and Section 2.1. Detailed benchmark tables were not fully audited; no numerical superiority estimate is asserted.

## Additional exclusions and unresolved leads

- Fang et al., arXiv:2610.00898: already reported October 2; excluded.
- Huang et al., recoverable resolution: already reported October 2; excluded.
- Chen & Hicks, bioRxiv 2026.09.15.751768v2: PDF confirms October 1, and prior radar already screened it; excluded.
- scLDM, PMID 42804716, DOI 10.1093/bioinformatics/btag727: primary metadata says September 28; excluded from new window.
- scEGFlow, arXiv:2610.02232v1: abstract page says submitted September 27, while sorted search lists originally announced October. Public availability after the cutoff was not established; excluded rather than treating its October identifier as a publication date.
- Arc 2026 Challenge data-generation blog: October 1 and not a paper; excluded.

## Proposed next action and gaps

Retain these as provisional revision candidates, not a replacement five-paper fresh list. A complete rerun needs live canonical-vault reads plus working date-indexed discovery, exact posting/version histories and material-change checks. The useful research distinction is separate validation of context representation, overlap-supported transport, and perturbation-response accuracy. No tasks or calendar records were created.
