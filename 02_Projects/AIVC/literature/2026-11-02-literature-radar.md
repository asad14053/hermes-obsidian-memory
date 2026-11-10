---
tags: [AIVC, literature-radar, perturbation-prediction, spatial-transcriptomics, gene-regulation]
date: 2026-11-02
previous_cutoff: 2026-10-30T10:00:00Z
---

# AIVC Literature Radar — 2026-11-02

Screened arXiv's 30 October/2 November announcements and bioRxiv posts through 2 November against prior AIVC radar reports. The five selections below were submitted after the prior 10:00 UTC cutoff or posted afterward. No new schizophrenia-specific paper was strong enough to displace these methodological papers. Findings are author-reported preprint results unless noted.

## 1. GENESIS — READ NOW
**Citation:** Conci R, D'Ascenzo D, Cultrera di Montesano S, Raghavan S, Winter PS, Van Allen EM, Crawford L, Lotter W. *Single-cell perturbation prediction near experimental reproducibility with GENESIS.* bioRxiv 2026.10.30.763081 (posted 2026-11-01). https://doi.org/10.64898/2026.10.30.763081

- **Problem:** Predict full response distributions across the combinatorial space of context, perturbation, dose, and experimental covariates.
- **Method:** A lightweight covariate-conditioned generator trained with the energy score, a strictly proper distributional scoring rule; evaluation calibrates model error against independently repeated measurements of the same condition.
- **Key result:** On Tahoe-100M and a large PBMC cytokine atlas, GENESIS reportedly beat existing generators and statistical baselines and approached repeat-experiment reproducibility. Under a fixed cell budget, covering more conditions shallowly improved prediction more than deeply profiling fewer conditions.
- **What is new:** Couples a simple distributional predictor to an experimental reproducibility ceiling and converts that comparison into an experimental-design result.
- **What is bad:** Abstract-level evidence does not establish unseen-donor, unseen-lab, neural, or spatial transfer. “Near reproducibility” may be condition- and metric-specific, and the model's simplicity may exploit dense support in these atlases.
- **AIVC relevance:** This is a direct benchmark target for AIVC: report performance as a fraction of donor/condition replicate reliability, not raw correlation alone.
- **Suggested study:** Under a fixed DLPFC/organoid cell budget, compare broad-low-depth versus narrow-high-depth designs over donor × target × cell type × neighborhood, with reliability-normalized distributional metrics.

## 2. SMFNet/PRISM — READ NOW
**Citation:** Schwämmle T, Diamant N, Badayeva Y, Kleinendorst R, Kundaje A, Krebs AR. *SMFnet reveals principles of combinatorial transcription factor assembly.* bioRxiv 2026.10.30.762954 (posted 2026-10-31). https://doi.org/10.64898/2026.10.30.762954

- **Problem:** Population-average accessibility predictors hide distinct single-molecule TF/nucleosome configurations supported by the same regulatory sequence.
- **Method:** SMFNet is a sequence-conditioned diffusion model for distributions of single-molecule accessibility profiles; PRISM attributes individual molecular states to sequence features. In silico motif screens test TF identity, partner, and spacing effects.
- **Key result:** Motif perturbations redistributed predicted molecular states as expected; endogenous natural variants supported TF-specific effects on accessibility, nucleosome positioning, and combinatorial assembly.
- **What is new:** Predicts a distribution over molecular chromatin states rather than an averaged accessibility track and links state-specific outputs to experimentally perturbed motifs.
- **What is bad:** Accessibility-state prediction is not transcriptomic perturbation prediction; the abstract does not establish broad cell-context/donor transfer or whether inferred assemblies are unique causal explanations.
- **AIVC relevance:** Provides a stronger sequence/regulatory prior than static gene-gene edges for SCZ variant-to-response modeling.
- **Suggested study:** Encode promoter/enhancer state distributions as gene-node priors and test whether they improve held-out SCZ regulatory-variant response prediction beyond expression, sequence embeddings, and static GRNs.

## 3. Co2ODE — READ NOW
**Citation:** de Pomereu T, Fröhlich F. *Co2ODE: Conditionally Coarse-Grained Model Discovery for Rewiring in Biochemical Networks.* arXiv:2610.41634v1 (submitted 2026-10-30 12:10 UTC). https://arxiv.org/abs/2610.41634v1

- **Problem:** Context rewires only part of a biochemical network, but sparse correlated measurements cannot identify a complete mechanistic model.
- **Method:** A conditional mask selects rewired markers for a sparse neural or symbolic ODE; a VAE compresses omitted variables into a learned closure term.
- **Key result:** On single-cell phosphoproteomics across 30 cancer-relevant overexpressions, a 10-dimensional model matched a full 30-marker neural ODE. Marker choice scarcely affected fit, and a prior could change selected markers without reducing accuracy.
- **What is new:** Explicitly separates a small interpretable rewiring module from a learned closure for unresolved biology.
- **What is bad:** The main result is also an identifiability warning: equally predictive subnetworks can disagree mechanistically. Evidence is limited to a small cancer phosphoprotein panel.
- **AIVC relevance:** High predictive accuracy or stable graph attention cannot validate the AIVC's inferred GRN. Causal-edge claims need interventions that distinguish competing graphs.
- **Suggested study:** Add a latent closure to the perturbation graph transformer, enumerate equivalently predictive edge sets, and use active perturbation selection to maximize graph discrimination in neural cells.

## 4. LOCOGEN — SAVE
**Citation:** Jeong D, Bourdim M, Lotfollahi M. *Locality-Controlled Out-of-Distribution Guidance for Robust Regulatory DNA Sequence Design.* arXiv:2610.41736v1; NeurIPS 2026. https://arxiv.org/abs/2610.41736v1

- **Problem:** Reward-guided regulatory-DNA generation can optimize predicted activity by leaving plausible sequence space or damaging motif grammar.
- **Method:** Sampling-time guidance on a frozen diffusion model; an invariance-learned motif mask protects sensitive positions while OOD damping constrains background positions. Evaluation separates activity, novelty, and plausibility.
- **Key result:** Across HepG2, K562, and SK-N-SH, LOCOGEN reached a property–novelty–plausibility regime missed by tested baselines.
- **What is new:** Controls where guidance acts rather than only its magnitude, and makes reward hacking visible through a three-axis evaluation.
- **What is bad:** Success is based on predictive scores with no wet-lab validation stated; three cell lines do not establish donor/tissue transfer. It addresses sequence design, not cell-state response simulation.
- **AIVC relevance:** Any inverse-design layer that proposes perturbations should preserve regulatory constraints and report plausibility/novelty separately from predicted rescue.
- **Suggested study:** Constrain AIVC-designed enhancer edits to motif-preserving regions, then compare predicted SCZ-program rescue, OOD distance, and orthogonal sequence-model plausibility before experimental selection.

## 5. Multi-scale WSI GNN — SAVE
**Citation:** Andrade M, Almeida J, Santiago C, Barata C. *From WSIs to Bulk, Spatial and Single-Cell Transcriptomics via Multi-Scale Graph Neural Networks.* arXiv:2610.41692v1 (submitted 2026-10-30 12:59 UTC). https://arxiv.org/abs/2610.41692v1

- **Problem:** Infer molecular profiles across bulk, spatial-patch, and single-cell scales from routine histopathology.
- **Method:** UNI2-h morphology features plus patch- and cell-level spatial graphs; direct supervision and cross-scale consistency losses combine TCGA, Visium, and Xenium across lung, kidney, and breast cancer.
- **Key result:** Five-fold results: bulk PCC 0.881 (TCGA), patch PCC 0.509 (Visium) and 0.786 (Xenium), and cell PCC 0.396 (Xenium). Molecular signatures supported tumor classification, spatial hazard mapping, and survival analysis, though measured expression remained better for survival.
- **What is new:** One graph hierarchy learns jointly from differently granular molecular supervision rather than training separate bulk/spatial/cell predictors.
- **What is bad:** Cell-level recovery is moderate and uneven; evaluation is cancer-only, Xenium-gene-limited, affected by small cohorts/segmentation/batch, and does not test perturbations or causal neighborhood effects.
- **AIVC relevance:** Morphology can be an auxiliary context channel and, critically, a baseline: apparent spatial-context gains may be predictable from tissue structure alone.
- **Suggested study:** Add histology/morphology tokens to the AIVC and require environmental-graph gains to exceed morphology-only, coordinate-only, and shuffled-neighborhood controls under held-out donors and genes.
