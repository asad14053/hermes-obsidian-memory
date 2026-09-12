---
type: environment
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Environment and Paths

## Root
`/beegfs/labs/hulab/projects/mjabin/GeneBridge`

## Python
- Env: `/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_scanpy`
- Direct interpreter: `/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_scanpy/bin/python`

## R
`/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_r`

Historical intended R stack:
SpatialExperiment, SingleCellExperiment, SummarizedExperiment, scuttle, scran, scater, DelayedArray, HDF5Array, spatialLIBD, zellkonverter, tidyverse, ggplot2, patchwork, cowplot, data.table.

## Imputation env
- Historical name: `Imputation`
- PyTorch 2.1.2
- CUDA reported False in VISTA context.

## SLURM
- Earlier jobs: 160 GB / 16 CPUs.
- ✅ DECISION: future heavy 23-donor work → **200 GB / 16 CPUs**, parallelize donors when safe.
- Interactive example: 8 CPUs / 64 GB / 4 h.

## Storage
- BeeGFS project storage.
- Historical home quota: 50 GB.
- `dtn01.hgcc` referenced for transfer.
