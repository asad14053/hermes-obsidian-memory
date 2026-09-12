---
type: research-overview
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# Research Overview

## Central theme

Map the spatial molecular architecture of schizophrenia at cohort scale in human postmortem DLPFC while preserving cortical geography and expanding molecular coverage.

## Modalities

- snRNA-seq — broad transcriptome, no native tissue coordinates.
- Visium — spatial transcriptome at spot-level resolution.
- Xenium — high spatial/cellular resolution with targeted panel.

## Current core workflow

1. Build/QC Xenium cohort.
2. Harmonize donor/diagnosis/layer metadata.
3. Evaluate missing-gene imputation.
4. Select best model.
5. Expand molecular coverage while preserving cells/domains/donors/diagnosis.
6. Perform cohort-level SCZ analyses.
7. Compare with reference SCZ spatial-transcriptomics paper.

## Cohort context

- Visium: 63 donors, historically 31 controls + 32 SCZ.
- Xenium: 24 matched donors, historically 12 controls + 12 SCZ.
- Br6432 excluded downstream due corruption → 23-donor working cohort.
- Core Xenium evaluation panel: 300 genes.

## Main branches

- [[02_Projects/GeneBridge/overview|GeneBridge]]
- [[02_Projects/AIVC/overview|AIVC]]
