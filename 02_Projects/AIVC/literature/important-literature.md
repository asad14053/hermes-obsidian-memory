---
type: literature-index
project: "AIVC"
status: active
last_updated: 2026-11-07
confidence: medium
---

# AIVC — Important Literature

This is a curated project index, not a claim that findings were reproduced in AIVC. Quantitative results below remain author-reported unless explicitly stated otherwise.

## Evaluation and recoverable response

### Hu et al. — Cause-excluded Effect Evaluation (CEE)

- **Citation:** Hu J, Qi X, Tian L, Yan J, Liu N, Li X. *Cause-excluded Effect Evaluation: a framework for the faithful assessment of genetic perturbation target identification.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.03.752923`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.03.752923v1
- **Durable use:** Separate train/test targets, remove direct target-gene self-effects, and score downstream response space when testing whether target recovery reflects response biology rather than target-expression clues. Report this alongside, not instead of, full-response evaluation.
- **? UNCERTAIN:** Full methods, comparators, masking construction, and deployment assumptions were not audited; this is an inverse-target-identification framework, not proof against deep forward-prediction models.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-12-literature-radar]].

### Miller et al. — calibrated perturbation metrics

- **Citation:** Miller HE, Mejia GM, Leblanc FJA, Swain B, Wang B, de Lima Camillo LP. *Deep learning perturbation models can outperform baselines on calibrated metrics.* Nature Biotechnology (2026). DOI: `10.1038/s41587-026-03307-w`.
- **Source:** https://www.nature.com/articles/s41587-026-03307-w
- **Durable use:** Calibrate evaluation metrics with informative positive and negative controls before interpreting baseline/model rankings. Keep outcome-derived calibration quantities out of training and model selection.
- **AIVC implication:** Beating simple baselines remains necessary, but raw MSE or another uncalibrated metric is not enough to establish success or failure.
- **Evidence limit:** The positive control is a benchmark diagnostic, not a deployable predictor or proof of causality.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-02-literature-radar]].

### Huang et al. — recoverable resolution of context-specific response

- **Citation:** Huang Y, Wang H, Li C, Wilson P. *The recoverable resolution of cellular perturbation-response prediction.* bioRxiv v1 (2026). DOI: `10.64898/2026.09.30.755756`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.09.30.755756v1
- **? UNCERTAIN:** Preprint; the radar review was based on partial PDF extraction, and the conclusions are conditional on the tested datasets, information sets, estimators, and definitions.
- **Durable use:** Evaluate context/donor-specific response recovery separately from final-state expression correlation or context recognition. Use independent replicate ceilings where available and report gene- and prespecified pathway-level endpoints.
- **AIVC implication:** A richer context embedding does not by itself demonstrate recovery of an environment-dependent response rule.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-02-literature-radar]].

### Qi and Chapfuwa — transportability depends on mechanism

- **Citation:** Qi S, Chapfuwa P. *Mechanisms Matter: Transportability of Cellular Perturbation Effects.* bioRxiv v3 (2026). DOI: `10.64898/2026.05.08.723625`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.05.08.723625v3
- **Durable use:** Treat cross-context perturbation transfer as a supported-mechanism question. Similar embeddings or aligned expression distributions do not establish transport; compare against simple response baselines and prespecify when to abstain.
- **Evidence limit:** Results are author-reported and partly semi-synthetic. Mechanistic-divergence diagnostics estimated from protected test responses would leak outcomes.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

### Cole et al. — separate perturbation representation from prediction head

- **Citation:** Cole E, Huizing GJ, Addagudi S, et al. *Foundation Models Improve Perturbation Response Prediction.* bioRxiv, revised October 22, 2026. DOI: `10.64898/2026.02.18.706454`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.02.18.706454
- **Durable use:** Factor perturbation representation and response head independently. Include prior-knowledge embeddings with simple kNN/lasso or ridge heads, stratify by replicate/signal reliability, and score mean effects and full distributions separately.
- **Evidence limit:** Author-reported revised-preprint results; reducing distributional outputs to means cannot establish that generative models add no value for heterogeneity. Predominant tasks were not human-brain donor/context transfer.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-23-literature-radar]].

### Karbalayghareh et al. — DynaVelo experimental-validation standard

- **Citation:** Karbalayghareh A, Pelzer B, Chin CR, et al. *Deep dynamical models of single-cell multiomic velocities predict loss-of-function and rescue perturbations in B cells.* Nature Biotechnology (2026). DOI: `10.1038/s41587-026-03348-1`.
- **Source:** https://www.nature.com/articles/s41587-026-03348-1
- **Durable use:** Distinguish model plausibility from experimentally checked intervention prioritization. A future AIVC claim should show that context changes a useful prediction and improves experimental prioritization, not only reconstruction or plausible regulatory edges.
- **Evidence limit:** The author-reported rescue evidence is specific to a murine B-cell system and does not validate human cortex, SCZ, or genome-wide unseen-target transfer.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-23-literature-radar]].

### Xu et al. — GeoSinkhorn population-distribution comparator

- **Citation:** Xu K, Wilkinson A, Ni S, et al. *GeoSinkhorn Flow: Geometry-Aware Flow Matching for Perturbation-Conditioned Dynamics in Single cell Data Phenoscapes.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.16.759724`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.16.759724v1
- **Durable use:** Score within-cell-state response and abundance/composition change separately, fit geometry using training donors/conditions only, and include transport plus embedding-kNN baselines before attributing gains to a graph transformer.
- **Evidence limit:** Author-reported preprint results; smooth transport paths are not observed lineage trajectories or identified mechanisms, and neural/SCZ transfer is unestablished.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-23-literature-radar]].

### Yang et al. — risk-calibrated causal extrapolation

- **Citation:** Yang F, Lei H, Chen Y, Du J-H. *Risk-Calibrated Balancing for High-Dimensional Causal Extrapolation.* arXiv:2609.34482v2 (2026).
- **Source:** https://arxiv.org/abs/2609.34482v2
- **Durable use:** Add overlap and weight-concentration diagnostics to transport benchmarks, and separate a permitted target-calibration sample from the protected final test.
- **Evidence limit:** This is a revision candidate, not a newly introduced method. It does not solve hidden confounding or zero support.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-05-literature-radar]].

### Lorch et al. — latent causal diffusions

- **Citation:** Lorch L, Zhang J, Bunne C, Krause A, Schölkopf B, Uhler C. *Latent causal diffusions for single-cell perturbation modeling.* PNAS (2026). DOI: `10.1073/pnas.2602630123`.
- **Source:** https://www.pnas.org/doi/10.1073/pnas.2602630123
- **Durable use:** Use as a mechanistic comparator for additive, ridge, graph-transformer, and conditional-VAE response models; keep causal interpretation tied to interventions and explicit model assumptions.
- **Evidence limit:** Author-reported performance; steady-state and intervention-entry assumptions do not establish transfer to unseen donors, tissues, or wholly unseen targets.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

### Wang and Oba — TAKO topology baseline

- **Citation:** Wang H, Oba K. *Topology-adjusted knockout (TAKO): interpretable in silico single-gene knockout ranking on wild-type single-cell gene regulatory networks.* Frontiers in Bioinformatics 6:1924703 (2026). DOI: `10.3389/fbinf.2026.1924703`.
- **Source:** https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2026.1924703/full
- **Durable use:** Retain a transparent, training-free topology/correlation comparator before claiming added value from a biology-informed graph transformer. Evaluate response ranking, direction, and magnitude separately.
- **Evidence limit:** TAKO discards regulatory sign, does not generate a full expression response, and its retrieved real-data validation covered two knockout targets.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-16-literature-radar]].

## Representation and architecture comparators

### Meng et al. — BioMod module tokenization

- **Citation:** Meng L, Zhu J, Han B, et al. *BioMod: Biological Module Tokenization for Single-Cell Foundation Modeling.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.12.758490`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.12.758490v1
- **Durable use:** Compare gene tokens, fixed pathway summaries, and learned module tokens under identical donor/target holdouts before treating pathway/module priors as AIVC novelty; fit learned modules using training data only.
- **? UNCERTAIN:** Preprint; exact gains, split integrity, pretraining overlap, baseline fairness, and code/checkpoint availability were not audited.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-14-literature-radar]].

## Spatial-context validation

### Dehghani Amirabad et al. — Tessera direction-aware spatial comparator

- **Citation:** Dehghani Amirabad A, Khodabandeh Yalabadi A, Moskalev A, et al. *Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics.* arXiv:2610.28579v1 (2026).
- **Source:** https://arxiv.org/abs/2610.28579v1
- **Durable use:** Compare cell-type-stratified pooled context, distance-only attention, and direction-aware attention on donor-held-out measured targets. Include slide-rotation and anatomical-axis controls; translation invariance is not rotation invariance.
- **Evidence limit:** Author-reported preprint/workshop results; masked-expression reconstruction does not establish perturbation prediction or spatial-environment causality.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-21-literature-radar]].

### Jackson, Gorin, and Pachter — biological versus technical spatial variation

- **Citation:** Jackson KC, Gorin G, Pachter L. *Biological and technical spatial variation in spatial transcriptomics.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.13.758896`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.13.758896v1
- **Durable use:** Test whether context-model gains survive explicit assay/capture-gradient nuisance adjustment and validation against an independent assay; a residual spatial pattern or prediction gain is not automatically microenvironmental causation.
- **? UNCERTAIN:** Preprint; absolute capture efficiency is not identifiable from counts alone, and domain annotations and within-domain assumptions influence separation.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-16-literature-radar]].

### Li et al. — SpatialZoomer multi-scale comparator

- **Citation:** Li X, Fan Y, Han Y, et al. *SpatialZoomer: multi-scale feature analysis of spatial transcriptomics.* Nature Biomedical Engineering (2026). DOI: `10.1038/s41551-026-01800-w`.
- **Source:** https://www.nature.com/articles/s41551-026-01800-w
- **Durable use:** Compare fixed-radius aggregation, simple multi-scale features, and learned attention under identical donor-held-out measured-response endpoints; adding scales alone is not sufficient methodological novelty.
- **? UNCERTAIN:** Full results were unavailable in the radar review, and the October 14 publication was a boundary-day candidate with unresolved release time.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-16-literature-radar]].

### Yao et al. — SPACER recruitment model

- **Citation:** Yao J, Shim JS, Wong K, et al. *Interpretable AI model reveals spatial codes of cell recruitment in tissues.* Nature Biomedical Engineering (2026). DOI: `10.1038/s41551-026-01804-6`.
- **Source:** https://www.nature.com/articles/s41551-026-01804-6
- **Durable use:** Use interpretable neighborhood/recruitment summaries as an environment-branch baseline and test composition-matched shuffled neighborhoods; show added value on measured responses in held-out donors before claiming mechanism.
- **Evidence limit:** Recruitment associations in cancer and heart are not causal intervention rules or evidence of transfer to brain/SCZ; full methods and split details were not audited.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-14-literature-radar]].

### Sánchez-Carbonell et al. — sparse neuronal C4 elevation

- **Citation:** Sánchez-Carbonell M, Bolshakova S, Ávila-Pagán JE, et al. *Sparse neuronal C4 elevation induces network-wide transcriptomic and lipid-droplet remodeling in the cortical microenvironment.* PLOS Computational Biology 22(10):e1014871 (2026). DOI: `10.1371/journal.pcbi.1014871`.
- **Source:** https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014871
- **Durable use:** Motivates explicit sender-versus-receiver context modelling for the SCZ-centered program and independent imaging validation of neighboring-cell responses.
- **Evidence limit:** Mouse developmental C4 overexpression is not human C4A variation, adult DLPFC schizophrenia, or a ready-made single-cell spatial perturbation benchmark.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-14-literature-radar]].

### Carcanholo et al. — patient-specific limits of spatial inference

- **Citation:** Carcanholo FP, Cassiano MHA, Panepucci EM, Laurini MP, Malta TM. *Point-Process Modelling of Cell-Type Interaction Structure in CosMx Glioma Data for Hypothesis-Driven Tumor Inference from scRNA-seq.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.02.756019`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.02.756019v1
- **Durable use:** Many cells do not replace independent donors. Report donor-held-out transport failure and abstention rather than pooled-cell performance, and do not assume harmonization repairs patient-specific molecular–spatial relations.
- **Evidence limit:** Eight GBM specimens, observational proximity rather than measured signaling, and no complete effect-size or leakage audit in the radar review.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-12-literature-radar]].

### Jin et al. — spatial perturbation screening of non-autonomous effects

- **Citation:** Jin K et al. *MERFISH-based pooled genetic screening reveals cell non-autonomous phenotypes in intact tissue.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.06.756924`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.06.756924v1
- **Durable use:** A candidate measured-response benchmark for sender-to-receiver effects. Before use, verify downloadable assignments, animal identifiers, controls, baseline-available inputs, and receiver-cell endpoints; hold out animals and perturbed genes.
- **Evidence limit:** Mouse liver is not human brain or aging/AD, and post-treatment neighborhood expression cannot be treated as a baseline predictor of the same response.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-07-literature-radar]].

### Wang et al. — domains are not automatically functional niches

- **Citation:** Wang Y, Chen Y, Yang L, Wang C, Cai J, Xin H. *Benchmarking niche identification via domain segmentation for spatial transcriptomics data.* bioRxiv v3 (2026). DOI: `10.64898/2026.02.27.708202`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.02.27.708202v3
- **Durable use:** Do not treat cortical layers or spatial clusters as validated signaling neighborhoods. Evaluate context features on held-donor measured outcomes rather than cluster-label agreement alone.
- **? UNCERTAIN:** The substantive novelty of v3 versus earlier versions was not verified; the main reference is a manually annotated lymph-node setting.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-05-literature-radar]].

### Wu et al. — VINTER identity/environment comparator

- **Citation:** Wu J et al. *VINTER: a generative vision-language model for annotating and interrogating spatial tissues.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.01.752251`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.01.752251v1
- **Durable use:** Compare AIVC against a simple donor-held-out identity-plus-context representation and test whether input-edit predictions track independent measured responses.
- **Evidence limit:** Input edits are not biological perturbations. The reported DLPFC setup is not clean unseen-donor evaluation because paired sections from a donor can span train and holdout, and part of the holdout supports checkpoint selection.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

### SpaCEy — spatial signal must beat non-spatial controls

- **Citation:** Rifaioglu AS et al. *SpaCEy links spatial tissue patterns to clinical outcomes using explainable graph neural networks.* Nature Communications 17, 10232 (2026). DOI: `10.1038/s41467-026-77924-z`.
- **Source:** https://www.nature.com/articles/s41467-026-77924-z
- **Durable use:** Treat the work as a validation-design comparator: require donor/patient-separated evaluation and show that spatial context adds value beyond expression-only, composition-only, and other non-spatial controls.
- **AIVC implication:** Matched neighborhood deletion or shuffling can test predictive dependence, but model-input deletion and attention sensitivity are not biological interventions or causal validation.
- **Evidence limit:** Cancer spatial proteomics and survival prediction do not establish neural perturbation-response validity.
- **Radar source:** [[02_Projects/AIVC/literature/2026-09-28-literature-radar]].

## Recent radar additions — October 26–30, 2026

### Huang — clone-aware perturbation reliability

- **Citation:** Huang X. *Shared clones make random cell halves look reproducible in pooled screens.* arXiv:2610.32962v1 (2026). https://arxiv.org/abs/2610.32962v1
- **Durable use:** For future cultured perturbation benchmarks, split by independent transduction/culture/donor units and test clone-disjoint reliability; random-cell agreement can overstate reproducibility when descendants of one founder cross both partitions.
- **? UNCERTAIN:** Preprint and system-dependent; the reported artifact must not be projected onto postmortem Xenium data or every neural perturbation model.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-26-literature-radar]].

### Batique et al. — uncertainty must add error information

- **Citation:** Batique T et al. *Probabilistic uncertainty in virtual spatial transcriptomics from histology is largely redundant with the predicted mean.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.23.760875`.
- **Durable use:** Evaluate calibration, error ranking and selective prediction separately; require uncertainty to identify errors beyond predicted-mean-only baselines before calling a probabilistic decoder useful.
- **Evidence limit:** Author-reported preprint, mainly within-cohort virtual ST; no direct AIVC or human DLPFC validation.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-26-literature-radar]].

### Luan — centered cross-context transfer baseline

- **Citation:** Luan H et al. *Centered cross-context perturbation transfer on the public 2025 Virtual Cell Challenge benchmark.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.20.760514`.
- **Durable use:** Include centered transfer and simple ridge/kNN comparators, and score response direction, ranking and magnitude separately before attributing gains to graph or decoder complexity.
- **Evidence limit:** Retrospective author-reported comparison with reconstructed anchors; not evidence of blind-competition superiority or neural/SCZ transfer.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-26-literature-radar]].

### Wei et al. — unified perturbational modeling

- **Citation:** Wei Z et al. *How Much Can AI Virtual Cells Gain from Unified Perturbational Modeling?* bioRxiv v1 (2026). DOI: `10.64898/2026.10.25.761625`.
- **Durable use:** Treat gene-panel alignment, modality/context coverage and data scale as separate contributors. A later graph/transformer model should use a data/parameter-matched UPM-style baseline before claiming architecture novelty.
- **Evidence limit:** Large author-reported preprint; held-out cell-line results do not establish independent-donor, disease-tissue or spatial-neural generalization.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-28-literature-radar]].

### Chen et al. — donor-held-out evaluation is not optional

- **Citation:** Chen X et al. *Evaluation design shapes estimates of cross-donor generalization in single-cell classification of cell-type.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.26.761949`.
- **Durable use:** Report random-cell versus donor-held-out performance and their optimism gap; donor adjustment does not replace donor-separated testing, and donor holdout still does not prove cross-site or cross-assay transport.
- **Evidence limit:** Classification in PBMC/lung, not AIVC response prediction or DLPFC disease modeling.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-28-literature-radar]].

### De Jonghe et al. — prospective variant-to-function data source

- **Citation:** De Jonghe J et al. *Scalable variant-to-function screens using prime editing perturb-seq.* bioRxiv (2026). DOI: `10.64898/2026.10.28.762453`.
- **Durable use:** Consider endogenous variant-to-function Perturb-seq as a future prospective benchmark for genotype-conditioned response prediction, with sequence/chromatin and additive baselines.
- **? UNCERTAIN:** Abstract-level preprint evidence; no demonstrated transfer to human neural donors, SCZ or spatial context, and no current access decision.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-30-literature-radar]].

## Recent radar additions — November 2–6, 2026

### GENESIS — replicate-reliability ceiling

- **Citation:** Conci R et al. *Single-cell perturbation prediction near experimental reproducibility with GENESIS.* bioRxiv 2026.10.30.763081. https://doi.org/10.64898/2026.10.30.763081
- **Durable use:** Compare future AIVC response predictions with independent-repeat reliability and use distributional metrics; treat coverage/design depth as a comparator rather than assuming architecture is the bottleneck.
- **Evidence limit:** Author-reported preprint; unseen-donor, neural and spatial transfer are not established.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-02-literature-radar]].

### ARCADE — abundance versus within-cell-type state

- **Citation:** Su Q. *ARCADE disentangles cell abundance from continuous transcriptional state in spatial transcriptomics.* bioRxiv 2026.10.28.762703. https://doi.org/10.64898/2026.10.28.762703
- **Durable use:** Separate composition/abundance from within-cell-type state before interpreting neighborhood-associated expression as context-induced response; require composition-only and shuffled-neighborhood controls.
- **Evidence limit:** Simulated/semi-synthetic and one DLPFC application; no perturbation ground truth or donor-generalization result.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-04-literature-radar]].

### RFA — negative topology-control result

- **Citation:** Timofeev A et al. *Continuous Topological Accessibility (RFA) as a 3D-Aware GRN Filter.* bioRxiv 2026.11.02.763620. https://doi.org/10.64898/2026.11.02.763620
- **Durable use:** Require Hi-C/3D graph priors to beat one-dimensional distance, accessibility-only, and rewired controls on the target response; do not infer causal utility from biologically plausible edges.
- **Evidence limit:** Limited cell-line/chromosome scope; the negative result does not rule out neural or perturbation-specific 3D effects.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-04-literature-radar]].

### SPEAR and RAPTORGraph — graph architecture comparators

- **Citations:** Verma S et al. *Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling.* bioRxiv 2026.11.02.763678. https://doi.org/10.64898/2026.11.02.763678; Adhisantoso YG et al. *RAPTORGraph.* bioRxiv 2026.11.03.763980. https://doi.org/10.64898/2026.11.03.763980
- **Durable use:** Treat spectral gene geometry, learned pathway structure, intervention-locality and anti-spillover penalties as explicit comparators/ablations if a later AIVC architecture is justified.
- **Evidence limit:** Observational graphs, inferred couplings and latent intervention assumptions do not establish causal rewiring or transport to human DLPFC/SCZ.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-06-literature-radar]].

### Foundation-model audit — minimum credibility controls

- **Citation:** Cupaioli F, Merelli I. *Where single-cell foundation models help.* bioRxiv 2026.11.03.763968. https://doi.org/10.64898/2026.11.03.763968
- **Durable use:** Include expression-matched deletion and negative contrasts, replicate-aware ground truth, donor/clone-disjoint splits, and matched PCA/mean/linear baselines before claiming foundation-model or perturbation gains.
- **Evidence limit:** Some organoid comparisons have limited independent libraries; zero-shot token deletion is not measured perturbation truth.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-06-literature-radar]].

### Perturbscape — possible disease-genetics bridge

- **Citation:** Turhan B et al. *Perturbation-induced gene programs map the hidden regulatory architecture of complex diseases.* bioRxiv 2026.11.03.762080v2. https://doi.org/10.64898/2026.11.03.762080
- **Durable use:** Consider perturbation-specific programs as a future bridge between response prediction and disease-genetic prioritization, requiring enrichment beyond steady-state annotations and independent neural/SCZ validation.
- **Evidence limit:** No schizophrenia-specific validation; multiple learner/selection steps create modeling degrees of freedom.
- **Radar source:** [[02_Projects/AIVC/literature/2026-11-06-literature-radar]].
