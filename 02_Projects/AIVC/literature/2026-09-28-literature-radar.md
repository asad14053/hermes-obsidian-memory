---
type: literature-radar
project: AIVC
run_date: 2026-09-28
previous_run: 2026-09-25T10:07:24
status: partial-coverage-primary-source-triage
---

# AIVC Literature Radar — 2026-09-28

## Scope, continuity, and verification

Three ranked recommendations, not five padded items. Target window begins after the supplied previous run, September 25 at 10:07:24 UTC. Pop-Corn and SpaCEy have September 26 publication/posting dates. PerturbBridge has a September 25 posting date and a Crossref DOI creation timestamp of 19:05:11 UTC, after the prior run; exact bioRxiv first-publication time was not independently recovered. Treat it as a likely in-window posting, with this within-day timing caveat. DOI date strings are not posting dates: Pop-Corn's DOI contains September 25 but Crossref explicitly records September 26 posting; PerturbBridge's DOI contains September 24 but Crossref records September 25 posting.

Searches covered arXiv, bioRxiv and publisher results for perturbation prediction, virtual cells, spatial/multimodal models and regulatory architectures. arXiv API extraction failed on XML content type. Category listings were stale/inconsistent (July, September 24), and date-filtered searches returned old work. Therefore this is not exhaustive coverage and does not establish that no other qualifying papers exist. PDFs for the two bioRxiv papers could not be retrieved. A large batch of publisher extractions spilled to a local file inaccessible to this run; unread portions were not treated as reviewed. Evidence below comes from accessible abstracts, publisher-indexed result/method passages and Crossref metadata, not reproduced experiments.

Direct Obsidian read/search and filesystem execution tools were not exposed. Project comparison uses the September 25 literature note recovered from session history: session cron_952fb3b6f0a6_20260928_020030, tool message 4559, which preserved the newer September 23 user outline. Working design: identity + environment → universal representation (UR) → virtual instrument (VI) → cell-type-specific activity; hold identity fixed during environment swaps. PDF specifies 20 μm cell-type-stratified neighborhoods, attention, MSE plus sparsity, identity-matched environment swaps. Companion diagram separately proposes multi-scale hierarchical cross-attention, Xenium/snRNA-seq/Visium/Perturb-seq, confidence-weighted imputation, perturbation embeddings, conditional VAE and donor-held-out tests. These remain proposals, not established results. Neither source supersedes the other; older aging/AD recommendations do not override the user's SCZ/NTC design.

Prior run recommendations were CellAudit, DePass, SpaFactor, Hou et al., and PRAXIS; none repeated. Session searches for Pop-Corn, PerturbBridge's identifier, SpaCEy and other screened names returned no previous matches. This is history-based deduplication, not a fresh vault-wide duplicate check. This additive note changes no canonical project facts. Note read-back is unavailable in this run; writing-tool acknowledgement is the only save confirmation.

## 1. Pop-Corn — READ NOW

**Citation:** Chen, J., Cui, Y., Shao, Y., Sun, N., & Martinez, M. R. (2026). *Pop-Corn: Predicting Perturbation Phenotype Effects Across Single-Cell and Spatial Contexts*. bioRxiv, version 1. Posted September 26, 2026. DOI: 10.64898/2026.09.25.754560.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.25.754560v1

**Metadata verification:** https://api.crossref.org/works/10.64898/2026.09.25.754560

**Research problem:** Predict cell-type/state composition shifts under unseen genetic perturbations; accurate mean expression is not necessarily accurate population composition.

**Method:** Directly predicts composition instead of reconstructing expression and assigning states downstream. The indexed figure legend describes aggregated cell representations with cell- and bag-level supervision. Spatial extension predicts neighborhood composition and uses perturbation-conditioned attention for interaction hypotheses. Full architecture and loss details were not verified.

**Key result (author-reported):** On the primary T-cell benchmark, better held-out-perturbation composition prediction and state-diversity preservation than evaluated expression-prediction pipelines. Also reports spatial-neighborhood predictions and retrospective virtual-screen prioritization. No numerical effect size is asserted here because the accessible abstract does not supply it.

**Why it matters for AIVC:** Direct challenge to an MSE-centered identity/environment → activity model. Activity changes within a cell type and changes in the abundance of that type are different endpoints. Fixed identity is a useful controlled query, but does not describe cell-state redistribution or selective survival by itself.

**What is new:** Direct composition-first perturbation modeling spanning dissociated populations and local spatial neighborhoods, rather than treating proportions as a downstream byproduct of expression prediction.

**What is bad / limitation assessment:** Coarse composition can miss molecular mechanisms. Label/state definitions influence the target; apparent state emergence can reflect detection thresholds. Relative abundance alone does not identify absolute survival/proliferation. Attention is not causal cell-cell signaling, and retrospective prioritization is not prospective validation. SCZ/DLPFC transfer is unproven in reviewed evidence.

**Future idea (proposal):** Add separate expression/activity and composition heads to AIVC. On held-out perturbations and donors, test whether environment information improves both, using no-environment and composition-only baselines plus orthogonal survival/proliferation measurements where available.

## 2. PerturbBridge — READ NOW

**Citation:** Liu, Z., Jiang, C., Yang, C., & Liu, X. (2026). *PerturbBridge: Conditional Latent Schrödinger Bridge for Single-Cell Perturbation Prediction*. bioRxiv, version 1. Posted September 25, 2026; within-day timing caveat above. DOI: 10.64898/2026.09.24.754259.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.24.754259v1.full

**Metadata verification:** https://api.crossref.org/works/10.64898/2026.09.24.754259

**Research problem:** Destructive RNA profiling yields unpaired control/perturbed populations; high-dimensional sparse observations complicate stochastic population transport.

**Method:** β-TCVAE-style latent representation, interpolation-consistency regularization, a perturbation-conditioned approximation to a latent Schrödinger bridge, and endpoint maximum mean discrepancy (MMD) regularization.

**Key result (author-reported):** Competitive performance across evaluated metrics and claimed state-of-the-art differential-expression recovery on Norman CRISPR and Sci-Plex3 chemical perturbations. Magnitudes, split rigor and complete comparison set were not verified from full text.

**Why it matters for AIVC:** Relevant alternative to a conditional-VAE or deterministic MSE decoder. It explicitly treats the target as a distribution rather than an individually identifiable treated counterpart. Identity-matched observational environment swaps still lack true single-cell counterfactual ground truth.

**What is new:** The particular combination of compact latent bridge learning, decoded-interpolation consistency and endpoint distribution matching; stochastic transport and VAEs individually are not new.

**What is bad / limitation assessment:** A learned bridge is not proof of causal dynamics or the true cellular path. Latent compression and interpolation assumptions may remove rare or nonlinear responses. Reviewed evidence does not establish donor-held-out spatial/neural transfer, SCZ validation or robustness to unseen biological contexts. Abstract-level triage only.

**Future idea (proposal):** Compare a neighborhood-conditioned latent bridge against AIVC's conditional-VAE and deterministic heads under identical donor/perturbation splits. Evaluate differential expression, distributional fit and state proportions separately; retain capacity-matched and no-context baselines.

## 3. SpaCEy — READ NOW (spatial validation design)

**Citation:** Rifaioglu, A. S., Ervin, E. H., Sarigun, A., Germen, D., Bodenmiller, B., Tanevski, J., & Saez-Rodriguez, J. (2026). *SpaCEy links spatial tissue patterns to clinical outcomes using explainable graph neural networks*. Nature Communications 17, 10232. Published September 26, 2026. DOI: 10.1038/s41467-026-77924-z.

**Source:** https://www.nature.com/articles/s41467-026-77924-z

**Metadata verification:** https://api.crossref.org/works/10.1038/s41467-026-77924-z

**Research problem:** Link molecular tissue organization to clinically meaningful outcomes rather than only spatial clustering.

**Method:** Cell graphs from spatial proteomic marker abundance, without predefined cell-type/region labels as model inputs; outcome prediction with a compact-subgraph/marker explainer. Publisher passages describe patient-separated evaluation and comparisons with pseudobulk-marker and cell-composition survival baselines.

**Key result (author-reported, publisher Results/Fig. 5):** Mean test C-index 0.720 ± 0.061 in JacksonFischer versus 0.617 ± 0.092 for the best evaluated non-spatial baseline; 0.688 ± 0.038 in METABRIC versus 0.570 ± 0.071. Patient-separated splits were used. Removing explainer-important nodes damaged predictions/ranking more than removing matched non-important nodes. These are cohort-specific evaluations, not demonstrated train-on-one-cohort/test-on-another transfer.

**Why it matters for AIVC:** Makes spatial context earn its role against strong non-spatial baselines and supplies a template for testing claimed explanatory neighborhoods. Particularly relevant to the identity/environment decomposition and claims that 20 μm or multiscale context adds information beyond composition and focal-cell state.

**What is new:** Annotation-agnostic graph inputs with spatial/molecular explanation linked to clinical endpoints. This is a newly published journal version of earlier SpaCEy preprint work, not a first-ever method announcement. No prior report was found in accessible session history.

**What is bad / limitation assessment:** Cancer spatial proteomics and survival association are not neuronal perturbation biology. Model-input deletion establishes predictive sensitivity, not a biological intervention. ROI sampling and limited marker panels constrain context; explanations inherit prediction errors. Patient-separated splitting does not remove all clinical confounding.

**Future idea (proposal):** Adapt matched-neighborhood deletion/shuffling tests to AIVC, preserving cell-type composition and focal identity. Require donor-held-out gains over expression-only, composition-only and coordinate-only baselines before interpreting spatial attention as biologically meaningful.

## Screening exclusions / not additional recommendations

- **RMGAT**, DOI 10.1186/s12859-026-06641-7: useful DLPFC negative-result ablations, but Crossref record already existed September 25 at 03:03:14 UTC, before the prior run. Excluded rather than mislabeled new. Its EdgeMLP/self-expression null results and contrastive p=0.024 (not Bonferroni-significant) remain possible catch-up reading, not today's recommendation.
- **scSTAMP-seq**, DOI 10.1038/s41587-026-03328-5: journal publication September 25, Crossref creation 09:02:31 UTC, before prior run. Excluded on timing; also has earlier preprint provenance.
- **SpaDPG**, publisher PII S1051200426006330: online September 25, but exact within-day eligibility unresolved; spatial-domain rather than perturbation evidence. Not used to pad the list.
- **Pheno-GS**, arXiv:2609.27633: September 23 submission/September 24 announcement, before window.
- **MoCoP v2**, arXiv:2609.30433: September 24 submission; first eligible announcement timing not established. Not promoted as new.

## Research-program implication

Proposed priority, not an existing commitment: define AIVC's estimand before enlarging the architecture—within-cell-type activity, cell-state composition, or a joint distribution. A K99/publication claim should specify the held-out biological context and orthogonal endpoint, not just a graph-transformer module. No new AIVC experiment, funding eligibility, disease-mechanism finding or completed milestone is implied by this literature review.
