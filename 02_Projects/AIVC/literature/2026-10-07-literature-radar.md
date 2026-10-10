# AIVC Literature Radar — 2026-10-07

## Scope, evidence and continuity

Search window: after the preceding run, 2026-10-05 10:05:45 UTC, through this scheduled run. Five selected papers have publisher/preprint posting dates of October 6. New journal publication is NOT necessarily first disclosure of a method. CardamomOT, VIMA and STARIT have earlier preprints; journal-versus-preprint changes were not exhaustively audited. Results below are author-reported, not independently reproduced. Selected abstracts and accessible methods/results/discussion passages were reviewed; complete full-text audits were not possible for all papers.

The previous October 5 report was recovered from session cron_b7fccc11fa73_20261005_100047, message 5927: risk-calibrated balancing (arXiv:2609.34482v2) and niche-identification benchmarking (10.64898/2026.02.27.708202v3). Neither is repeated. Searches of accessible conversation history for CardamomOT, GP-DHT, STARIT, VIMA and 756924 returned no matches. This is NOT equivalent to a live vault-wide duplicate audit.

Live vault read/search and terminal tools were unavailable in this run. Design comparison instead uses actual note text recovered from session cron_d2277f698e9f_20261004_210004, message 6098: [[02_Projects/AIVC/methods]], last_updated 2026-09-23, cites [[02_Projects/AIVC/project-outline]]. PDF design: scGPT/UCE identity embedding plus 20 μm cell-type-stratified distance-weighted neighbor expression → feature attention → activity head; MSE plus sparsity. Diagram: multimodal inputs, multiscale hierarchical cross-attention, interaction features, perturbation embedding, conditional VAE and confidence-weighted imputation losses. These remain distinct proposed specifications, not a verified combined implementation. No new model results are inferred.

Coverage limitations: intermittent search backend failures, date-filtered arXiv API extraction returned an unusable/ambiguous flattened response, several full-text extractions were partial, and some large responses spilled to files inaccessible with the current tool set. Alternative publisher/search/bioRxiv sources were used. This is a ranked shortlist, not an exhaustive census. TempoBridge (arXiv:2610.04945v1) was excluded because its October 4 submission predates the cutoff and later announcement timing was not verified. CellART and CCI-seq had October 5 publication dates without verified post-cutoff timestamps and were not included.

## 1. READ NOW — Amplification-free MERFISH pooled genetic screening

Citation: Jin K, Saunders RA, Zhang J, Lu J, Halpern AA, Sandhu J, Pan X, Wang CY, Li AM, Allen WE, Weissman JS, Zhuang X. MERFISH-based pooled genetic screening reveals cell non-autonomous phenotypes in intact tissue. bioRxiv v1, posted October 6, 2026. DOI: 10.64898/2026.10.06.756924.
Source: https://www.biorxiv.org/content/10.64898/2026.10.06.756924v1
Evidence: abstract and explicit posted-date footer at https://www.biorxiv.org/content/10.64898/2026.10.06.756924v1.full . Extractor header incorrectly said Published 2026-01-01; the source's explicit Posted October 06, 2026 is used instead.

Problem: Measure how a targeted cell's genetic perturbation affects both that cell and its neighbors in intact tissue.
Method: Direct-hybridization, amplification-free MERFISH jointly reads perturbation barcodes and endogenous transcripts in a genetic-mosaic mouse liver screen.
Key result: Authors report approximately 10-fold greater perturbation-barcode recovery and 2.5-fold greater endogenous-transcript recovery versus their previous amplification-based workflow; approximately 200 hepatocyte targets and 1.5 million profiled cells. Observations include local accumulation of pDC-like cells around V-ATPase-impaired hepatocytes and vascular angiogenic responses near Vhl-perturbed hepatocytes.
What is new: Improved joint perturbation/spatial readout at scale with explicit non-autonomous phenotypes; not the first spatial perturbation assay.
AIVC relevance: Directly relevant evidence for the environment branch and sender-to-receiver response prediction, stronger than reconstructing observational spatial expression. A candidate benchmark, not a confirmed downloaded/usable dataset.
What is bad / limits: Mouse liver rather than human brain or aging/AD; targeted imaging does not give unrestricted transcriptome coverage. Local associations do not by themselves identify every signaling mediator. Data access, animal-level replication, assignments and split feasibility remain unverified. Post-treatment neighborhood expression must not be used to predict the same post-treatment response as if available at baseline.
Future idea: Predict unperturbed receiver-cell responses from sender perturbation and an explicitly available baseline neighborhood representation. Hold out animals and perturbed genes, compare against identity-only and distance/composition baselines, and stratify effects by receiver lineage and distance.

## 2. READ NOW — CardamomOT

Citation: Maugé Y, Ventre E. CardamomOT: A mechanistic optimal transport-based framework for gene regulatory network inference, trajectory reconstruction and generative modeling. PLOS Computational Biology 22(10):e1014838. Published October 6, 2026.
Source: https://doi.org/10.1371/journal.pcbi.1014838
Citation verified: https://journals.plos.org/ploscompbiol/article/citation?id=10.1371/journal.pcbi.1014838
Prior preprint inspected (specific version): https://www.biorxiv.org/content/10.64898/2026.03.31.715390v2.full . This establishes prior disclosure, not journal-specific novelty.

Problem: Infer regulatory structure and dynamics from destructive temporal RNA snapshots when the governing protein trajectories are unobserved.
Method: Mechanistic optimal transport jointly reconstructs GRNs and latent protein trajectories; uses actual time labels and kinetic-rate priors. The underlying model includes transcriptional bursting, translation and degradation.
Key result: The journal abstract reports improved GRN and trajectory reconstruction over comparators on simulated datasets. Experimental reconstructions of trajectories, velocity fields, latent proteins and GRNs are mutually consistent and consistent with known biology. The calibrated model generates testable unseen-perturbation predictions; this should not be restated as prospective experimental validation.
What is new: Joint mechanistic GRN/latent-dynamics calibration and generative simulation; a newly published journal version of an existing preprint.
AIVC relevance: A mechanistic comparator to a graph-transformer/cVAE virtual instrument, especially for separating credible dynamics from expression reconstruction. Also challenges an assumption that identity stays fixed through all perturbations.
What is bad / limits: Requires informative time-course data and kinetic/model assumptions; latent protein dynamics are inferred, not directly observed. Accuracy on model-generated data does not establish unrestricted real-world causal identification. Cross-sectional DLPFC cannot simply replace the required time series. No verified numerical effect size is quoted.
Future idea: On a small time-resolved neuronal regulatory module, compare mechanistic transport, graph-transformer and simple response baselines under held-out perturbations; test sensitivity to kinetic priors and identity-changing interventions.

## 3. READ NOW — VIMA

Citation: Reshef YA et al. Accurate and well-powered case–control analysis of spatial molecular data. Nature Methods. Published October 6, 2026.
Source: https://www.nature.com/articles/s41592-026-03236-1
Supporting publisher briefing: https://www.nature.com/articles/s41592-026-03242-3 (October 6; explicitly identifies the original article).
Prior preprint: https://www.biorxiv.org/content/10.1101/2025.02.07.637149v1 (earlier title: Powerful and accurate case-control analysis of spatial molecular data with deep learning-defined tissue microniches). Journal publication is new; the core method is not a first announcement.

Problem: Detect disease-associated spatial structures without reducing all cells and neighborhoods to discrete annotations.
Method: Ensemble variational autoencoders encode tissue patches into numeric fingerprints; data-dependent overlapping microniches are meta-analyzed for abundance association with case-control status, with permutation-based inference described in the repository/methods.
Key result: Journal abstract reports calibrated, powerful and spatially accurate simulation results, plus applications spanning three diseases and spatial modalities that recover known biology and identify additional spatial features. No unverified disease-specific effect sizes are supplied.
What is new: Flexible overlapping, continuous-feature-informed neighborhood association testing rather than only discrete cell-type/niche proportions.
AIVC relevance: A strong observational baseline for the environmental representation and an immediately relevant SCZ spatial-analysis comparator. Can test whether attention adds more than better neighborhood summaries.
What is bad / limits: Case-control association is not a perturbation simulator or causal environmental effect. Donor-level confounding and sample integration require scrutiny; many patches do not create independent biological replicates. Disease-relevant features must not be removed as batch effects.
Future idea: Compare the proposed 20 μm neighbor summary against VIMA-derived microniche features in donor-level SCZ analyses; freeze feature learning and evaluate transfer to independent perturbation outcomes before making causal claims.

## 4. SAVE — GP-DHT

Citation: Yan S, Yu Q, Dai W, Cheng X. GP-DHT: A dual-head transformer with supervised contrastive learning for shared-gene pretraining and single-cell GRN prediction. PLOS ONE 21(10):e0359164. Published October 6, 2026.
Source: https://doi.org/10.1371/journal.pone.0359164
Citation verified: https://journals.plos.org/plosone/article/citation?id=10.1371/journal.pone.0359164
Evidence: abstract; sections 2.1, 2.2, 3, 3.1 and 3.7 available through publisher extraction.

Problem: Infer TF-target links from noisy, sparse single-cell expression.
Method: Shared human/mouse gene-space pretraining, multi-relational gene-cell heterograph, dual-head Transformer for link classification and gene-pair supervised contrastive learning. Supervised fine-tuning/evaluation is within each BEELINE dataset.
Key result: Authors report the full model is more robust than its ablated variants to sparsity, noise and reduced data. Evaluation uses three-fold TF-level holdouts and pooled test predictions. Numerical headline gains were not independently recovered and are not quoted.
What is new: Combines heterogeneous graph representation, shared-gene pretraining and complementary classification/contrastive objectives; meaningful methodological overlap with the broad biology-plus-graph-transformer concept.
AIVC relevance: A candidate regulatory-prior baseline and a warning that architecture labels alone are not a novelty claim.
What is bad / limits: GRN link prediction is not perturbation-response prediction. Putative hard negatives are unlabeled edges rather than established biological absences. Cross-species pretraining is not proof of zero-shot species transfer. Post-hoc attribution is explicitly distinct from causal validation.
Future idea: Compare GP-DHT-derived, curated, coexpression, rewired and no-graph priors using the same downstream held-out perturbation benchmark and leakage-controlled training pipeline.

## 5. SAVE — STARIT

Citation: Velazquez D, Hallinan C, An R, Clifton K, Fan J. Spatial Transcriptomics As Rasterized Image Tensors (STARIT) characterizes cell states with subcellular molecular heterogeneity. PLOS Computational Biology 22(10):e1014845. Published October 6, 2026.
Source: https://doi.org/10.1371/journal.pcbi.1014845
Prior preprint indexed as December 22, 2025, DOI 10.64898/2025.12.18.695193; prior existence corroborated by https://pubmed.ncbi.nlm.nih.gov/41497642/ . Newly published journal article, not first method disclosure.
Evidence: publisher abstract/results; sections 2.4 and 3 for orientation confounding and runtime.

Problem: Conventional cell-by-gene counts discard intracellular RNA localization that can distinguish cell states.
Method: Rasterizes transcript coordinates within segmented cells into gene-image tensors; pretrained computer-vision models extract features for downstream clustering, with optional expression-based feature weighting.
Key result: In the reported noisy simulation, feature weighting recovers four designed groups with ARI 1.0 while count-based analysis still merges localization-defined states. Real-data applications include mouse-brain osmFISH and bacterial MERFISH. This is not a general real-tissue accuracy estimate.
What is new: Preserves subcellular molecular organization in a representation usable by vision models.
AIVC relevance: The proposed identity embedding plus cell-level neighborhood averages can miss intracellular state; a potential complementary modality, not an automatic replacement for the environment branch.
What is bad / limits: Sensitivity to segmentation, orientation and detection noise; bacterial clusters can reflect trivial rotations. Synthetic perfect separation does not validate disease or perturbation prediction, and serial rasterization has nontrivial cost.
Future idea: Test a rotation-controlled, segmentation-robust intracellular localization encoder on Xenium, asking whether it improves held-donor state/response residuals beyond count, morphology and cell-type baselines.

## Research-program implication

Prioritize a falsifiable neighborhood-conditioned perturbation experiment over another architectural addition. First audit the new MERFISH screen for accessible perturbation assignments, animal identifiers, untreated controls and receiver-cell endpoints. Use a mechanistic comparator for dynamics and an observational spatial comparator for context, while keeping those claims separate. None of these papers establishes the user's missing aging/AD experimental system or validation partnership.

## Persistence status

This note was submitted through obsidian_remember to the canonical vault-relative literature path. Independent live read-back is unavailable in this run; the tool's write acknowledgement is the only write confirmation. No canonical design, task owner, deadline or grant aim was modified.
