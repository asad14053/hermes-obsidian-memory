---
type: datasets
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Datasets

## Xenium

- GEO: `GSE307404`
- Metadata: `data/metadata/xenium_sample_metadata_24_common.csv`
- File list: `data/metadata/geo_filelists/GSE307404_Xenium_filelist.txt`
- Historical archive size: ~231 GB.
- Downstream: 23 donors after Br6432 exclusion.

### Donors remembered from array context

Br1113, Br1139, Br2039, Br2421, Br2719, Br5314, Br5373, Br5400, Br5436, Br5588, Br5590, Br5622, Br5639, Br5746, Br5931, Br5973, Br6032, Br6389, Br6432, Br6437, Br6496, Br8433, Br8667.

⚠️ VERIFY complete 24-donor list; this remembered list contains 23 names and may omit one donor.

### Example metadata

- Br6496 — SCZ, M, age 38.10.
- Br8433 — NTC, M, age 47.95.
- Br8667 — NTC, F, age 37.33.
- Br8772 — SCZ, F, age 57.80 appeared in cohort discussion; ⚠️ VERIFY exact cohort membership.

### Br8667 key files

- `spatial_data_xenium_Br8667_vista.h5ad`
- `spatial_data_xenium_Br8667_vista_qc.h5ad`

## Visium

- GEO: `GSE307403`
- File list: `data/metadata/geo_filelists/GSE307403_Visium_filelist.txt`
- Cohort context: 63 donors; historically 31 controls + 32 SCZ.
- Imported SpatialExperiment: `28916 × 113927`
- RDS: `data/processed/visium/spatialDLPFC_Visium_sce_light.RDS`

## snRNA-seq / Huuki-Myers

- Input: `data/processed/snrnaseq/sce_DLPFC_annotated/`
- Source pair: `se.rds` + `assays.h5`
- Canonical references:
  - `seq_data_huuki_snrna_9samples_excluding_xenium_overlap.h5ad`
  - `seq_data_huuki_snrna_9brains_excluding_Br8667.h5ad`

## Matching constraint

Br2039 example:
- Visium: `GSM9223410_Br2039-V12F14-057_C1_barcodes.tsv.gz`
- Xenium: `GSM9223468_Br2039-cell_boundaries.csv.gz`

✅ DECISION: donor labels do not prove identical tissue section or exact spatial alignment.
