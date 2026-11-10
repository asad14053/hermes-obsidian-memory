---
tags: [AIVC, literature-radar, perturbation-prediction, graph-transformer, causal-ML, spatial-transcriptomics, evaluation, disease-genetics]
date: 2026-11-06
previous_cutoff: 2026-11-04T10:04:55Z
screened_through: 2026-11-06T10:02:43Z
---

# AIVC Literature Radar — 2026-11-06

Compared candidates with the 2026-11-04 radar note (GeneRegulatorySystems.jl, ARCADE, CNN-CR motif vocabulary, RFA, and source-shortcut diagnostics). The five papers below were newly posted on bioRxiv on 4 November and were not in that report. Findings are author-reported preprint results. No new schizophrenia-specific study met the top-five threshold.

## 1. SPEAR — READ NOW
**Citation:** Verma S, Wang M, Kadadi SD, Lanman NA, Mohammadi S, Grama A. *Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling.* bioRxiv 2026.11.02.763678, posted 2026-11-04. https://doi.org/10.64898/2026.11.02.763678

- **Research problem:** Gene tokens lack a biologically meaningful order, while fixed co-expression masks cannot represent perturbation-dependent regulatory rewiring.
- **Method:** SPEAR is a flow-based generative perturbation model. It embeds genes with graph-Laplacian spectral coordinates derived from a control co-expression graph, then updates per-gene rotary positions from perturbation-conditioned hidden states at every transformer layer.
- **Key result:** Across genetic, pharmacological, and cytokine benchmarks, the authors report strong recovery of differential expression, response distributions, and perturbation identity; learned positional relations also align with known TF-target relations. Ablations with permuted or freely learned coordinates did not reproduce the spectral-prior benefit.
- **What is new:** It treats a biological graph as a continuous positional geometry rather than a fixed adjacency mask, while permitting context-dependent reorganization inside attention.
- **What is bad:** The starting graph is observational co-expression, and learned attention/position changes do not establish causal rewiring. The evaluation does not demonstrate donor-disjoint DLPFC or disease-context transport, so strong benchmark performance may not survive the AIVC target domain.
- **Why it matters for AIVC:** This is the closest new architecture to a Biology + Perturbation Graph Transformer and supplies a concrete alternative to both static GNN propagation and orderless transformers.
- **Future idea:** Implement spectral gene coordinates plus perturbation-, donor-, cell-type-, and neighborhood-conditioned repositioning; compare against pure transformer, static-mask, GNN, permuted-graph, and learned-graph controls under target/donor/context holdouts.

## 2. RAPTORGraph — READ NOW
**Citation:** Adhisantoso YG, Schröder SK, Greß M, Hernaez M, Voges J. *RAPTORGraph: graph-based pathway modeling for causal discovery in single-cell perturbations.* bioRxiv 2026.11.03.763980, posted 2026-11-04. https://doi.org/10.64898/2026.11.03.763980

- **Research problem:** Dense causal encoders can let a known intervention spill across many latent variables, violating single-node intervention assumptions; curated pathway masks also impose confirmatory bias.
- **Method:** A β-VAE uses a learned GraphPathway encoder, intervention-guided preconditioning to isolate each perturbed gene's latent effect, and optimal-transport alignment of unpaired control and perturbed populations.
- **Key result:** The authors report a better reconstruction/distribution-matching trade-off and stronger prediction of unseen non-additive combinations than prior causal representation methods, plus interpretable latent meta-pathways and a graph among them.
- **What is new:** It combines learned graph pathways with explicit anti-spillover intervention preconditioning instead of forcing data through fixed pathway annotations.
- **What is bad:** OT alignment is an inferred coupling, not observed cell-level counterfactual truth. Causal identifiability depends on strong model and intervention assumptions, and the closed-world known-target setting does not establish transport to unseen donors, brain contexts, or disease mechanisms.
- **Why it matters for AIVC:** It offers a direct test of whether graph structure adds mechanistic value beyond response prediction, and highlights intervention spillover as a failure mode for latent pathway models.
- **Future idea:** Add an intervention-locality penalty and learned pathway graph to the AIVC, then test whether latent interventions recover held-out combinatorial effects and known SCZ-relevant regulator programs without degrading response calibration.

## 3. Perturbscape — READ NOW
**Citation:** Turhan B, Lee H, Liu D, et al. *Perturbation-induced gene programs map the hidden regulatory architecture of complex diseases.* bioRxiv 2026.11.03.762080v2, posted 2026-11-04. https://doi.org/10.64898/2026.11.03.762080

- **Research problem:** Steady-state atlases miss disease-relevant trans-regulatory programs that appear only after perturbation.
- **Method:** Perturbscape learns multiscale perturbation-specific programs using differential expression/co-expression, PCA/cNMF, linear and kernel contrastive PCA, ContrastiveVI, and Hotspot, then integrates them with GWAS heritability to prioritize perturbations, genes, and pathways.
- **Key result:** Across 15,859 perturbation-context profiles, seven Perturb-seq systems, and 53 traits, programs were up to 4.3-fold more heritability-informative than steady-state prioritization and perturbation-specific programs scored 2.5–5.3-fold higher than pooled/control/DE summaries. It also recovered context-specific trans-eQTL support and neuronal-subclass-specific autism programs.
- **What is new:** It connects experimentally induced trans programs to common-disease genetics at perturbation and cellular-context resolution rather than treating GWAS and Perturb-seq as separate layers.
- **What is bad:** Heritability enrichment prioritizes associations, not causal response prediction; combining many learners and selecting disease-weighted meta-programs creates substantial modeling/selection degrees of freedom. There is no schizophrenia-specific validation.
- **Why it matters for AIVC:** This supplies the missing bridge from an AIVC predictor to a K99 disease-genetics aim: ranking perturbations by whether their downstream programs capture disease liability.
- **Future idea:** Build a SCZ-DLPFC Perturbscape layer over neuronal/glial perturbation atlases, require conditional enrichment beyond steady-state DLPFC annotations, and experimentally test top convergent regulators in iPSC-derived cortical cells.

## 4. Foundation-model audit — READ NOW
**Citation:** Cupaioli F, Merelli I. *Where single-cell foundation models help: a benchmark of annotation, perturbation and regulatory inference against simple baselines.* bioRxiv 2026.11.03.763968, posted 2026-11-04. https://doi.org/10.64898/2026.11.03.763968

- **Research problem:** Determine where single-cell foundation models add information beyond task-matched simple baselines across annotation, perturbation, and GRN inference.
- **Method:** The study compares scGPT, Geneformer V1/V2, Nicheformer, scFoundation, CellOracle, STATE and other supervised models against matched baselines in cell lines, primary cells, brain organoids, and lung cancer, with sample-identity checks, negative contrasts, replicate-aware ground truth, and expression-matched deletion controls.
- **Key result:** FMs clearly helped cross-species annotation (human→mouse accuracy 0.98 for Nicheformer versus 0.68 best baseline), but within-species embeddings were near PCA. Zero-shot K562 knockouts often got direction but not magnitude; in organoids, only 12–35% of predicted deletion effects remained gene-specific after expression matching. Geneformer V2 GRNs enriched patient tumor DE genes more than co-expression (2.9× versus 2.0×).
- **What is new:** The expression-matched deletion test and negative/replicate contrasts directly separate target-specific perturbation information from the trivial fact that an expressed input gene was removed.
- **What is bad:** Several organoid comparisons have one library per line/time point and cannot distinguish model differences from clone/donor effects; zero-shot token deletion is not equivalent to an experimentally measured perturbation. The broad benchmark does not deeply optimize every model.
- **Why it matters for AIVC:** It defines minimum credibility tests for the program: PCA/mean/linear baselines, target-expression matching, replicate-level truth, donor-disjoint splits, negative contrasts, direction and magnitude metrics, and patient-level validation.
- **Future idea:** Make an `aivc-audit` suite that fails a model unless response gains persist after target-expression matching and exceed negative donor/clone/batch contrasts on held-out DLPFC donors.

## 5. CRISP — SAVE
**Citation:** Sasson J, Niasoff B, Karin J, Ezraty Y, Nitzan M. *Uncovering cross-signal interactions in single-cell and spatial omics.* bioRxiv 2026.11.03.763866, posted 2026-11-04. https://doi.org/10.64898/2026.11.03.763866

- **Research problem:** Cell state contains interacting signals—disease, space, time, cell cycle, and response—but standard factorization emphasizes disentanglement and can miss the interaction itself.
- **Method:** CRISP compares multiple probabilistic signal-specific projections of each cell to quantify coupling, localize the cells carrying it, and identify associated genes.
- **Key result:** In simulations and four single-cell/spatial datasets, it recovered tunable signal coupling; localized loss of zonation-position coupling in fibrotic hepatocytes; resolved asymmetric TGF-β/EMT/cell-cycle coupling; and identified delayed hepatocytes during infection.
- **What is new:** It makes interaction between latent biological signals an explicit, cell-localized object rather than a nuisance to remove.
- **What is bad:** Coupling between learned projections is associative and depends on signal labels/projection quality; no perturbation ground truth shows that identified genes drive the interaction, and no neural-disease/donor-generalization study is included.
- **Why it matters for AIVC:** A DLPFC virtual cell should model interactions such as disease × cortical layer × cell type × neighborhood × perturbation, not just additive covariates.
- **Future idea:** Use CRISP-style interaction scores as both diagnostics and auxiliary targets, testing whether an AIVC preserves reproducible SCZ-by-layer and perturbation-by-neighborhood coupling under donor holdout and spatial-label permutation.
