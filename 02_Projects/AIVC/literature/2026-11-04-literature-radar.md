---
tags: [AIVC, literature-radar, perturbation-prediction, spatial-transcriptomics, gene-regulation, evaluation]
date: 2026-11-04
previous_cutoff: 2026-11-02T10:05:21Z
---

# AIVC Literature Radar — 2026-11-04

Screened bioRxiv and arXiv-related search results after the previous radar cutoff and compared candidates against prior radar entries. The five selections below were newly posted on bioRxiv on 3 November 2026 and were not previously reported. No new schizophrenia-specific paper was strong enough to displace them; ARCADE is directly relevant to human DLPFC. Findings are author-reported preprint results.

## 1. GeneRegulatorySystems.jl — READ NOW
**Citation:** Maischak L, Jordan D, Manolache S, Drost H-G. *Simulating the dynamics of gene regulatory systems at cellular scale.* bioRxiv 2026.11.01.763459, posted 2026-11-03. https://doi.org/10.64898/2026.11.01.763459

- **Research problem:** Biophysically detailed stochastic GRN models are usually restricted to small circuits, while genome-scale simulators sacrifice mechanism and intervention realism.
- **Method:** GeneRegulatorySystems.jl implements exact stochastic chemical-master-equation simulation of nonlinear gene expression, feedback, RNAi, protein-mediated degradation, and protein complexes. A domain-specific language specifies interventions and single-cell experimental protocols.
- **Key result:** The proof-of-principle system scales mechanistic simulations to tens of thousands of genes and reproduces canonical small-system behavior while supporting genome-scale virtual experiments.
- **What is new:** It supplies an intervention-capable, mechanistic simulator and experimental grammar at a scale useful for synthetic training and falsification of learned virtual cells.
- **What is bad:** It is a simulator, not an inferred or experimentally validated human-cell model. Genome-scale kinetic parameters and GRN topology remain largely unknown; exact simulation of an assumed mechanism does not make the mechanism correct.
- **Why it matters for AIVC:** It could generate controlled ground truth for testing whether the AIVC recovers causal edges, nonlinear feedback, stochasticity, and intervention effects—questions that observational benchmarks cannot identify.
- **Future research idea:** Build synthetic DLPFC-like GRNs with known feedback and hidden variables, render scRNA-seq-like snapshots, and compare graph transformer, pure transformer, and latent-closure models on response prediction plus causal-edge recovery.

## 2. ARCADE — READ NOW
**Citation:** Su Q. *ARCADE disentangles cell abundance from continuous transcriptional state in spatial transcriptomics.* bioRxiv 2026.10.28.762703, posted 2026-11-03. https://doi.org/10.64898/2026.10.28.762703

- **Research problem:** In mixed spatial spots, a local expression shift can be explained either by changed cell-type abundance or by changed state within a cell type, making spatial-state inference non-identifiable.
- **Method:** ARCADE first constructs a consensus-filtered single-cell reference, estimates cell-type composition, then models continuous intratype programs around that fixed compositional anchor.
- **Key result:** It reports better deconvolution and more stable state inference in simulated and semi-synthetic benchmarks; in matched human DLPFC spatial proteogenomic data it separates localized cell enrichment from astrocyte and microglial activation programs.
- **What is new:** Explicitly sequences abundance inference before state inference rather than asking one latent model to disentangle both simultaneously.
- **What is bad:** Evidence centers on simulations/semi-synthetic data and one DLPFC application; there is no perturbation ground truth, donor-generalization result, or proof that the inferred state programs are causal environmental effects. It is also a single-author preprint.
- **Why it matters for AIVC:** Your spatial AIVC must not interpret neighborhood-associated composition as a context-induced state response. ARCADE supplies a direct nuisance-control strategy for DLPFC.
- **Future research idea:** Add an abundance-anchored nuisance branch to the AIVC and require neighborhood tokens to predict within-cell-type residual response under donor holdout, compared with composition-only and shuffled-neighborhood controls.

## 3. Compact regulatory motif vocabulary / CNN-CR — READ NOW
**Citation:** Shen S, Wang W. *A compact motif vocabulary is differentially interpreted across human cell types.* bioRxiv 2026.11.01.763377, posted 2026-11-03. https://doi.org/10.64898/2026.11.01.763377

- **Research problem:** Determine whether cell-type-specific expression requires distinct cis-regulatory vocabularies or context-dependent interpretation of a shared vocabulary.
- **Method:** CNN-CR is an interpretable convolutional model trained to predict gene expression across 116 human biosamples; motif compression, held-out-context tests, chromatin gating, ChIP-seq occupancy, fine-mapped variants, and genome-scale perturbation evidence are combined.
- **Key result:** Dozens of recurrent motif families retain most predictive information from much larger cell-specific vocabularies and transfer to excluded contexts. Context acts through chromatin accessibility and reader identity; motifs are conserved and enriched at fine-mapped regulatory variants.
- **What is new:** A compact shared sequence vocabulary plus context-specific access/reader interpretation offers a parsimonious alternative to a separate regulatory graph for every cell state.
- **What is bad:** Expression prediction across biosamples is not single-cell perturbation forecasting, and motif/reader associations do not uniquely identify causal regulatory paths. Neural disease and donor transfer are not established.
- **Why it matters for AIVC:** It argues for separating invariant motif tokens from context-dependent gating rather than encoding all context in mutable GRN edges.
- **Future research idea:** Use shared motif-family tokens as fixed gene priors and learn donor/cell-type/neighborhood gates; test whether this improves held-out SCZ regulatory-variant and perturbation responses over static GRNs and unconstrained gene embeddings.

## 4. Relative Forest Accessibility (RFA) — READ NOW
**Citation:** Timofeev A, Bratishchikov A, Anufriev A. *Continuous Topological Accessibility (RFA) as a 3D-Aware GRN Filter: Anticorrelation with eQTL and No Prediction of ΔRNA.* bioRxiv 2026.11.02.763620, posted 2026-11-03. https://doi.org/10.64898/2026.11.02.763620

- **Research problem:** Test whether continuous accessibility propagated over Hi-C topology improves regulatory-target filtering or predicts expression changes.
- **Method:** RFA solves a Markov diffusion system over Hi-C contacts seeded by TF or ATAC peaks, then evaluates promoter TF counts, eQTL-linked genes, and MCF10A-to-MCF7 expression change with permutation and bootstrap controls.
- **Key result:** One-dimensional distance beat RFA for promoter TF counts (AUC 0.976 versus 0.836); the eQTL relationship was anticorrelated and attributable to local distance decay rather than loops/TADs; RFA did not predict ΔRNA (Spearman ρ=0.005, permutation p=0.87, 95% CI −0.040 to 0.053; n=1,730).
- **What is new:** A useful negative result with explicit nulls showing that a biologically appealing 3D-topology prior can add no predictive information and even reverse expected sign.
- **What is bad:** Only selected chromosomes/cell lines and coarse resolutions are tested, so the null does not rule out cell-type-specific enhancer-promoter contacts, neural tissue, or perturbation-specific 3D effects.
- **Why it matters for AIVC:** It directly warns against assuming Hi-C-derived graph edges are causal or useful; every graph prior needs matched simple-distance and local-accessibility baselines.
- **Future research idea:** Benchmark DLPFC Hi-C/ABC/GRN priors against 1D distance, accessibility-only, degree-preserving rewires, and learned graphs under donor/target holdouts; retain 3D edges only if they improve response prediction beyond these controls.

## 5. Source-shortcut diagnostic — SAVE
**Citation:** Ayaz H, Verma P, Ali MM, Oladimeji O, Ibitoye AO. *When perfect is a warning: explanations expose shortcuts that accuracy hides in cancer gene-expression classifiers.* bioRxiv 2026.11.02.763649, posted 2026-11-03. https://doi.org/10.64898/2026.11.02.763649

- **Research problem:** Detect models that classify data source rather than biology when labels are confounded with cohort or laboratory.
- **Method:** Six model families, including a tabular foundation model, are audited with a label-free explanation-consistency score that exploits source effects being shared across tissues while genuine cancer effects vary by tissue.
- **Key result:** Models reached AUC 1.000 on TCGA-tumor versus GTEx-normal training data but mislabeled 80–97% of tumor-adjacent normals and 100% in an independent cohort; a few matched normals removed most of the shortcut. The explanation score raised no false alarms in tested controls and transferred to unseen model/data types.
- **What is new:** Converts cross-context consistency of feature explanations into a label-free source-confounding diagnostic.
- **What is bad:** It is a bulk cancer-classification study, not perturbation prediction; explanation methods can themselves be unstable, and the diagnostic relies on source artifacts being more invariant across tissues than biology.
- **Why it matters for AIVC:** High donor/lab/disease discrimination or response accuracy can be entirely technical. This reinforces existing AIVC notes that donor-, lab-, and experiment-disjoint splits are acceptance criteria, not optional analyses.
- **Future research idea:** Audit AIVC residuals and feature attributions for lab/batch-invariant shortcut directions, then test whether matched controls and nuisance-adversarial training remove them without erasing SCZ and perturbation signals.
