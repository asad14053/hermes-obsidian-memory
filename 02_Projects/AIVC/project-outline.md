---
type: project-outline
project: "AIVC"
status: proposed-design
last_updated: 2026-09-23
received: 2026-09-23
confidence: high
provenance: user-supplied-pdf-and-diagram
source_pdf: "[[02_Projects/AIVC/sources/2026-09-23/AIVC_Broad_idea.pdf]]"
source_diagram: "[[02_Projects/AIVC/sources/2026-09-23/upload_20260923_082638_1.png]]"
---

# AIVC — User-supplied project outline

## Authority and status

Asad supplied the PDF and accompanying architecture image on September 23, 2026 and explicitly requested that they be saved in memory. This note records the supplied project design; the original files are preserved unchanged. Confidence refers to faithful documentation, **not** scientific validation.

These are primary sources for the user's intended AIVC concept, ahead of earlier assistant-generated reconstructions of that intent. They describe proposed methods and evaluations, not completed implementation, selected dataset accessions, or experimental results. The PDF and image differ in scope; neither was explicitly declared to replace the other. Their relationship and remaining design differences are preserved below rather than silently resolved.

The PDF is titled **“4.3 Thrust 3: From Spatial Omics Atlases to Predictive Virtual Cell Models”** and has two text-bearing pages. The accompanying image is titled **“AIVC: Multimodal Spatial Virtual Cell Model”**, subtitled **“From multimodal data to context-aware counterfactual cellular responses.”** The PDF's internal metadata records July 26, 2026; September 23 is the receipt date, not an inferred scientific revision date. Authorship and proposal ownership are not inferred from PDF software metadata.

## Core concept

AIVC separates relatively stable **cell identity** from **local microenvironment**, combines them into a **universal representation (UR)**, and uses a task-specific **virtual instrument (VI)** to predict cell-type-specific activity. Counterfactual queries keep identity fixed while changing the environment. The accompanying multimodal diagram additionally introduces explicit gene perturbations and a conditional generative model. [PDF pp. 1–2; diagram modules 2–7]

## A. Broad outline in the PDF

### Task 3.1 — Harmonize spatial omics atlases

Curate major spatial omics atlas datasets and develop a graphical portal to search, compare, and reuse them. Address overlapping samples, inconsistent metadata, and heterogeneous data structures across platforms, studies, and time points. Task 3.2 builds on this harmonized resource. [PDF p. 1, Overview]

### Task 3.2 — Predict activity under counterfactual microenvironments

The proposed rationale is that large collections of static single-cell-resolution spatial transcriptomics snapshots sample diverse environments and biological conditions, supporting learning of identity–environment–activity relationships. The document proposes that these relationships can support activity-dynamics prediction; this is a scientific premise, not an established causal or longitudinal result. [PDF p. 1, Task 3.2]

**Step 1: Construct the UR.**

- Cluster cells and identify cell-type marker genes through differential expression.
- Encode each cell's marker profile using a foundation model such as **scGPT or UCE**, giving identity embedding \(c_u\).
- Identify neighboring cells within a predefined **\(r=20\,\mu\mathrm{m}\)** radius.
- For each neighboring cell type \(m\), compute a distance-weighted average of expression, weighting closer cells more heavily.
- Assemble the cell-type-stratified environment \(e_u=(e_{u,1},e_{u,2},\ldots,e_{u,M})\).
- Combine identity and environment: \(f_u=(c_u,e_u)\). [PDF p. 1, Step 1]

**Step 2: Train the VI.**

- Within each cell type, identify activity-state genes that distinguish functional substates.
- Target \(y_u\) is the expression vector of those activity-state genes for the cell's type.
- Apply feature-specific attention to the UR, followed by a prediction head, to predict \(\hat y_u\).
- Train with gradient descent using **MSE plus an attention sparsity penalty**.
- The document proposes using attention to examine identity-marker and neighboring-cell-type contributions. These attention patterns would be model attributions, not experimentally established regulatory mechanisms. [PDF p. 1, Step 2 and Fig. 6]

**Source notation retained, not repaired:** The printed attention equations use \(h_u^i=q^i\tanh(f_u^i)\), a softmax denominator written \(\sum_{i=1}^{4g}\exp(h_u^i)\), and an aggregation written \(\sum_{i=1}^{4g}a_u^if_u^i\). The meaning of \(4g\), index reuse, and intended aggregation shape are not fully defined. Fig. 6 labels identity inputs “Cell-type house keeping genes,” while the prose specifies DE-derived cell-type marker genes. Preserve that distinction for implementation clarification. [PDF p. 1]

**Step 3: Counterfactual queries.**

Hold \(c_u\) fixed and change \(e_u\) to \(e'_u\), for example by adding/removing neighboring cell types, changing neighbor activity states, or relocating a cell to another neighborhood:

\[
\Delta y_u=VI(c_u,e'_u)-VI(c_u,e_u).
\]

Intended use: generate testable cell–cell interaction hypotheses, prioritize microenvironmental factors, and evaluate experimental designs in silico before wet-lab experiments. [PDF p. 2, Step 3]

**Proposed evaluation:** Split cells into training and validation sets; match a training cell to a validation cell with similar identity but different environment. Replace the training cell's environmental embedding with the matched validation cell's embedding and compare the prediction to that validation cell's observed activity. The PDF does not specify donor-held-out splitting here. Tune neighborhood radius and VI architecture. [PDF p. 2, evaluation and alternatives]

**References as supplied, not independently bibliographically verified during intake:** Cui H et al., *scGPT: toward building a foundation model for single-cell multi-omics using generative AI*, Nature Methods 2024, 21(8):1470–1480; Rosen Y et al., *Universal cell embedding provides a foundation model for cell biology*, Nature 2026:1–9. [PDF p. 2]

## B. Multimodal architecture in the accompanying diagram

All dimensions, modalities, losses, and evaluation criteria below are **proposed diagram specifications**, not confirmed implementation or data availability.

### 1. Inputs

| Source | Intended contribution |
|---|---|
| Xenium | 300 measured genes, imputed transcriptome, spatial coordinates `(x, y)`, cell segmentation |
| snRNA-seq | Whole transcriptome, reference cell-type labels, multiple donors; identity teacher |
| Visium | Regional/layer/domain programs and SCZ versus NTC spatial patterns |
| Perturb-seq | CRISPR gene perturbations, expression changes, multiple cell types |
| Metadata | Donor, diagnosis `(SCZ/NTC)`, cortical layer, batch/technical covariates |

No matched cross-modal donor inventory or specific Perturb-seq accession is established by this diagram. [Module 1]

### 2. Cell identity encoder

Identity genes → **UCE / scGPT or scVI** → raw embedding shown as **1280** → projection MLP → **\(c_u\), 256 dimensions**. Contrastive alignment with snRNA-seq is labeled \(L_{identity}\). The image lists model alternatives; the shown raw dimension should not be assumed to apply automatically to every alternative. [Module 2]

### 3. Spatial microenvironment encoder

- Multi-scale neighborhoods: **0–20, 20–50, 50–100 μm**.
- Neighbor features: identity \(c_j\), activity state \(s_j\), cell type \(t_j\), relative position `(Δx, Δy, distance)`, layer/domain, and expression/imputation reliability \(R_j\).
- Neighbor tokens \(n_{uj}\): **256 dimensions**.
- Hierarchical cross-attention: target-cell queries over neighbors → cell-type pooling → type-level attention.
- Output \(e_u\): **256 dimensions**. [Module 3]

### 4. Perturbation encoder

Perturbed gene and intervention type **KO/KD/OE/...** → perturbation embedding \(p\): **128 dimensions**. No-perturbation code: \(p_0=0\). [Module 4]

### 5. Universal representation

Concatenate \(c_u\), \(e_u\), and elementwise interaction \(c_u\odot e_u\), each shown as 256 dimensions, into **768 dimensions**; a fusion MLP produces **\(z_u^{UR}\), 256 dimensions**. [Module 5]

### 6. Virtual instrument

A **conditional VAE** receives the UR and perturbation embedding. The figure labels the encoder **\(q(z\mid c,e,p)\)** and decoder **\(p(y\mid z,c,e,p)\)**, with latent \(z\) and KL regularization. These labels are preserved as drawn; the figure alone does not fully specify the training posterior, prior, or likelihood. [Module 6]

### 7. Outputs and counterfactuals

- Gene-level expression for cell-type-specific activity genes and pathway/program scores.
- Environment-only: \(VI(c,e',p_0)\).
- Gene perturbation: \(VI(c,e,p_g)\).
- Joint change: \(VI(c,e',p_g)\).
- \(\Delta y\) denotes predicted response. [Module 7]

### 8. Objectives

- \(L_{obs}\): measured expression.
- \(L_{imp}\): imputed expression, weighted by confidence \(R_{uj}\).
- \(L_{align}\): cross-modal alignment with snRNA-seq and Visium.
- \(L_{pert}\): perturbation-response expression changes.
- \(L_{KL}\): VAE regularization.
- \(L_{att}\): attention regularization, **entropy + sparsity**.

\[
L=\lambda_1L_{obs}+\lambda_2L_{imp}+\lambda_3L_{align}+\lambda_4L_{pert}+\beta L_{KL}+\lambda_5L_{att}.
\]

The diagram does not resolve how the separately labeled \(L_{identity}\) is incorporated into this total. [Modules 2 and 8]

### 9. Evaluation and uses

- Prediction: Pearson, Spearman, R², RMSE, MAE; DE direction and pathway recovery for perturbations.
- Generalization: donor-held-out cross-validation, held-out layers/neighborhoods, unseen perturbations/cell types.
- Interpretation: attention by cell type, distance, layer, diagnosis; neighborhood ablations; counterfactual tests; SCZ versus NTC environmental effects.
- Applications: responses in novel environments, candidate microenvironmental drivers, therapeutic-target/experiment prioritization, and a **hypothesis-generating virtual cell for brain disease**. [Module 9]

## Differences and relationship to existing memory

| Issue | PDF | Accompanying diagram |
|---|---|---|
| Scope | Atlas curation/portal plus spatial prediction | Expanded multimodal spatial and gene-intervention architecture |
| Neighborhood | Distance-weighted, cell-type-stratified expression at 20 μm | Multi-scale neighborhoods and hierarchical cross-attention |
| VI | Attention and prediction head; MSE + sparsity | Conditional VAE with multiple objectives |
| Intervention | Alter local environment | Alter environment, gene perturbation, or both |
| Validation | Cell split and identity-matched environment swap | Explicit donor-held-out and other generalization tests |
| Disease | No specific disease mandated in these pages | Explicit SCZ/NTC and brain-disease context |

The uploads are more concrete than the previous generic architecture notes. They **do not establish an approved switch to aging/AD**, nor do they establish that earlier pure-transformer alternatives have been formally rejected. Earlier NIA K99 reviews and weekly strategies are assistant-generated critiques/proposals and must not be substituted for the user-supplied outline. Their requirements are specific to the proposed NIA application, not the definition of the broad AIVC program.

The baseline PDF design and expanded image should remain distinguishable until the user selects an implementation version. Counterfactual simulation remains a proposed prediction use; causal identification, observed intervention validation, and completed model performance are not established by either source.

## Preserved sources and verification

- [[02_Projects/AIVC/sources/2026-09-23/AIVC_Broad_idea.pdf|Original two-page outline PDF]] — SHA-256 `f81b8f5c8562b35a8e804f4b29c8b925338a3d7a32c30a7a5582fc8cae0fcc3c`.
- [[02_Projects/AIVC/sources/2026-09-23/upload_20260923_082638_1.png|Original multimodal architecture diagram]] — SHA-256 `8f482c194bbbb0d3113fce0c6c88f6fc6537bbd5cf174f22a9bb795d979e4495`.

Both vault copies were byte-verified against the supplied attachments. The PDF's two pages were text-extracted; its embedded Fig. 6 was rendered and visually inspected. The uploaded diagram was visually inspected, including rechecking the attention-loss and UR labels.

Related: [[02_Projects/AIVC/overview]], [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/current-state]].
