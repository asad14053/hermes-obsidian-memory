---
type: methods
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Methods

## 3-fold held-out-gene evaluation

- 300 Xenium genes.
- 3-fold gene-wise CV.
- Per fold: ~200 observed + ~100 held out.
- Fold balancing used:
  - log mean expression,
  - dispersion,
  - detection fraction (>0),
  - Moran’s I.

### Deliverables

- `fold_k_observed_genes.h5ad`
- `fold_k_heldout_genes.h5ad`
- `gene_metrics_and_fold_assignment.h5ad`
- `fold_manifest.json`

## Metrics

- Spearman correlation coefficient (SCC)
- SSIM
- RMSE
- MAE
- Jensen–Shannon divergence
- NMI
- ARI
- Moran’s I

## Models

- ENVI — reported best.
- VISTA.
- GIMVI.
- Tangram.
- SpaGE.
- TransIMP.
- ⚠️ VERIFY final six-method panel.

## VISTA

- Python: `src/imputation/VISTA/run_vista_fold.py`
- SLURM: `scripts/slurm/imputation/run_vista_ex5_3fold_array.slurm`
- Historical env: PyTorch 2.1.2; CUDA False in one context.

## Downstream DE

- Donor × layer pseudobulk.
- Layer-adjusted workflow.
- Script: `scripts/slurm/imputation/DE/03_layer_adjusted_de_array.slurm`
- Formulas discussed included:
  - `expression ~ Dx + Age + Sex`
  - expanded versions including slice/run terms.
- ✅ DECISION: always state exact formula/covariates when comparing outputs.
