---
type: project-overview
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Overview

## Objective

- Expand molecular coverage of high-spatial-resolution Xenium data for schizophrenia while preserving cells, cortical domains/layers, donors, and diagnosis.
- Benchmark missing-gene imputation with held-out Xenium genes.
- Select a robust method for downstream cohort analysis.
- Compare SCZ differential-expression results with the reference spatial-transcriptomics paper.

## Scientific context

- Human postmortem DLPFC.
- SCZ vs NTC/control.
- Modalities: Xenium, Visium, snRNA-seq.
- Presentation title: **“Mapping the Spatial Molecular Architecture of Schizophrenia at Cohort Scale.”**

## Project root

`/beegfs/labs/hulab/projects/mjabin/GeneBridge`

## Current method status

- ✅ DECISION: ENVI was reported as the best-performing imputation method.
- Other models historically included VISTA, GIMVI, Tangram, SpaGE, TransIMP.
- ⚠️ VERIFY final six-method set/table before publication/presentation.

## Downstream state

- 23 usable Xenium donors after Br6432 exclusion.
- 7 cortical layers/domains.
- 161 donor × layer pseudobulk samples.
- 300 measured genes in the core Xenium panel.

## Project notes

- [[02_Projects/GeneBridge/current-state|Current state]]
- [[02_Projects/GeneBridge/goals|Goals]]
- [[02_Projects/GeneBridge/decisions|Important decisions]]
- [[02_Projects/GeneBridge/datasets|Datasets]]
- [[02_Projects/GeneBridge/methods|Methods]]
- [[02_Projects/GeneBridge/experiments-and-results|Experiments and results]]
- [[02_Projects/GeneBridge/environment-and-paths|Environment and paths]]
- [[02_Projects/GeneBridge/errors-and-fixes|Errors and fixes]]
- [[02_Projects/GeneBridge/todo-and-next-actions|TODO and next actions]]
