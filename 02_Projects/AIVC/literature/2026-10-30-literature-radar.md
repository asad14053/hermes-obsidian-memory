# AIVC Literature Radar — 2026-10-30

Search window: after the 2026-10-28 10:06 UTC radar through 2026-10-30 10:02 UTC. Duplicate check used the prior radar history and the existing dated literature-memory sequence. All findings below are preprints; results are author-reported.

## 1. Learning developmental dynamics from lineage context
- Citation: Gowri G, Fishman N, Colgan WN, et al. *Learning developmental dynamics from lineage context*. arXiv:2610.40447v1. Submitted 2026-10-29.
- URL: https://arxiv.org/abs/2610.40447v1
- Triage: READ NOW.
- Problem/method: Learn multicellular developmental dynamics from relatives' cell states using lineage inpainting, a tree-structured transformer with stochastic interpolants.
- Key result: In a lineage-traced mouse embryogenesis atlas, recovered convergence events not resolved by expression alone; unperturbed training produced counterfactuals agreeing with several observed phenotypes, including a single-cell Tbx5-knockout response.
- New: Treats lineage-tree context as a first-class generative conditioning structure rather than representing each cell independently.
- Weakness: Counterfactual agreement is not broad causal validation; only one explicitly named single-cell knockout result, with no donor, neural-disease, or spatial-neighborhood transfer test.
- AIVC implication: Context can include lineage/history, not only current cell state and neighbors.
- Research idea: Add lineage/state-history tokens to the AIVC and compare expression-only, neighborhood-only, lineage-only, and combined models under unseen-target and unseen-donor neural perturbations.

## 2. Scalable variant-to-function screens using prime editing perturb-seq
- Citation: De Jonghe J, Armas Reyes M, Jamieson C, Christensen JB, Opzoomer JW, et al. *Scalable variant-to-function screens using prime editing perturb-seq*. bioRxiv 2026.10.28.762453. Posted 2026-10-28.
- URL: https://www.biorxiv.org/content/10.64898/2026.10.28.762453v1
- Triage: READ NOW.
- Problem/method: PEP-seq couples prime editing to time-resolved single-cell transcriptomics for direct endogenous variant-to-function mapping.
- Key result: 2,164 guides generated 749,110 transcriptomes; detected nonsense-mediated decay, and intended eQTL targets were frequently the strongest affected transcript within 1 Mb after locus-size correction, with effects associated with nearby open chromatin.
- New: Expands Perturb-seq from gene perturbations to programmed endogenous variants at scale.
- Weakness: The abstract does not establish transfer across cell types, donors, neural systems, or disease contexts, and this is an experimental platform rather than an AIVC predictor.
- AIVC implication: Supplies causal variant-level response data and a prospective benchmark for genotype-conditioned virtual cells.
- Research idea: Build a SCZ-focused PEP-seq panel and test whether sequence/chromatin priors plus cell state predict held-out regulatory-variant responses better than eQTL and additive baselines.

## 3. Environmental risk reshapes high-confidence schizophrenia risk genes during a developmental window of vulnerability
- Citation: Brack A, Phadke RA, Fournier L, Boberg MJ, Salgado M, Cruz-Martín A. *Environmental risk reshapes high-confidence schizophrenia risk genes during a developmental window of vulnerability*. bioRxiv 2026.10.27.762379v1. Posted 2026-10-28.
- URL: https://www.biorxiv.org/content/10.64898/2026.10.27.762379v1
- Triage: READ NOW.
- Problem/method: Combines a mouse early-life-stress model with 24-plex single-cell mFISH registered to the Allen Mouse Brain Atlas; profiles ten original SCHEMA genes, C4b, and activity markers across 1.29M cells and four ages.
- Key result: Risk-gene upregulation peaked at P21 and was region/cell-type selective; Sp4 and Cacna1g had distinct temporal responses; C4b rose across neuronal and glial populations, and P10 C4b effects correlated with P21 Grin2a effects across regional cell types.
- New: Provides a spatial, developmental gene-by-environment response map for high-confidence SCZ genes.
- Weakness: Targeted 24-gene panel, mouse LBN model, prominent hypothalamic signal, and no direct human DLPFC or causal perturbation validation.
- AIVC implication: SCZ response prediction should condition jointly on genotype/risk gene, environmental exposure, developmental age, region, and cell type.
- Research idea: Train a developmental stress-conditioned graph model and test whether it predicts held-out gene-by-age-by-region effects, then evaluate conservation in human DLPFC organoids or postmortem spatial data.

## 4. Joint localization and testing reveals spatial context of differential expression
- Citation: Stotzem N, Chang S, Cai N, Casale FP. *Joint localization and testing reveals spatial context of differential expression*. bioRxiv 2026.10.28.758685. Posted 2026-10-29.
- URL: http://biorxiv.org/lookup/doi/10.64898/2026.10.28.758685
- Triage: SAVE.
- Problem/method: SpaceDX uses gene-specific attention-based spatial weighting to jointly test subject-level differential expression and localize contributing tissue patterns without predefined regions.
- Key result: Detected 45.8% more DE genes than regional DESeq2 pseudobulk in a mouse chronic-stress study; combining SpaceDX with DESeq2 increased discovery by 19.1% in an Alzheimer model.
- New: Learns gene-specific spatial support while performing cross-subject association testing.
- Weakness: Attention maps are associational; extra discoveries do not by themselves prove biological validity, causality, or immunity to cell-composition and capture-field confounding.
- AIVC implication: Offers an output-level way to test whether predicted condition effects localize to the correct tissue contexts.
- Research idea: Use SpaceDX-like maps as auxiliary supervision/evaluation for DLPFC AIVC predictions and require gains to survive shuffled-neighborhood and technical-field controls.

## 5. Ground-truth evaluation of sparse autoencoder features on spatial, single-cell and language-model embeddings
- Citation: Shahsavand A, Forghani S, Akbarzadeh S, Mahdavi Sabet F. *Ground-truth evaluation of sparse autoencoder features on spatial, single-cell and language-model embeddings*. bioRxiv 2026.10.27.762296v1. Posted 2026-10-29.
- URL: https://www.biorxiv.org/content/10.64898/2026.10.27.762296v1
- Triage: SAVE.
- Problem/method: Evaluates sparse-autoencoder interpretability against known concepts in spatial transcriptomics, Geneformer, synthetic cell states, and a small language model; compares single fits, five-fit consensus, and sparsity-matched rotations.
- Key result: Single SAEs covered more concepts but reproduced only 27–46% of features; five-fit consensus reached 78–98% reproducibility and retained purer programs than varimax, but lost some lineages and weak planted states.
- New: Demonstrates with ground truth that feature reproducibility alone is not evidence of biological meaning and provides concept coverage/purity baselines.
- Weakness: Known concepts are limited proxies; no perturbation-response or causal evaluation, and consensus can erase weak biology.
- AIVC implication: Any mechanistic claims from latent features or attention should be tested against known concepts and matched linear/rotation baselines.
- Research idea: Create an AIVC interpretability suite with planted pathways, known perturbation programs, SCZ cell states, multi-seed stability, concept coverage, purity, and predictive intervention tests.
