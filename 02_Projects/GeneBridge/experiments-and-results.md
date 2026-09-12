---
type: experiments-results
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Experiments and Results

## Metadata recovery

Restored slide/run information via `sample_paths.csv`, adding:
- `slide_id`
- `run_date`

Metadata included:
- BrNum
- Dx
- Age
- Sex
- `predictions_smooth`
- `layer_annotation`

Key files:
- `data/metadata/xenium_DE_metadata_23.csv`
- `data/metadata/xenium_PI_run_metadata_24.csv`
- `xenium_DE_metadata_23_validation.txt`

## Pseudobulk

- 23 donors
- 7 layers
- 161 donor × layer samples
- 300 genes
- 161/161 valid
- 3 Br5373 unannotated cells excluded
- min cells 743
- max cells 26,781

## Layer-adjusted DE

Historical summary:
- block correlation `0.6090113`
- nominal p<0.05 `53`
- FDR<0.10 `9`
- FDR<0.05 `2`
- up FDR<0.10 `4`
- down FDR<0.10 `5`

Output patterns:
- `*_layer_adjusted_SCZ_DE_summary.csv`
- `*_layer_adjusted_SCZ_DE_dx_results.csv`

## Historical job IDs

- ENVI donor × layer pseudobulk: `4272389` — 23 PASS.
- Layer-adjusted DE: `4272422`.
- Later download/build IDs included `4339921` and `4340416` range.

⚠️ Historical only; verify current files/status.
