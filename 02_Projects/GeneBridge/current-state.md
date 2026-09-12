---
type: project-state
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Current State

## Xenium cohort

- Reference cohort: 24 donors.
- Working downstream cohort: 23 donors.
- ✅ DECISION: Br6432 excluded because of corruption.

## Layer mapping

- `spd01 → WMtz`
- `spd02 → L3/4`
- `spd03 → L6`
- `spd04 → WM`
- `spd05 → L5`
- `spd06 → L2/3`
- `spd07 → L1/M`

## Pseudobulk

- 23 donors.
- 7 layers.
- 161 donor × layer combinations.
- 300 genes.
- 161/161 valid.
- 3 unannotated Br5373 cells excluded.
- Historical cell-count range/sample: 743 to 26,781.

## Layer-adjusted DE — historical summary

- `block_correlation = 0.6090113`
- nominal `p < 0.05`: 53
- FDR `< 0.10`: 9
- FDR `< 0.05`: 2
- up at FDR `< 0.10`: 4
- down at FDR `< 0.10`: 5

⚠️ VERIFY these against latest output files before reporting.

## Reference-paper concordance

- Reference paper: bioRxiv DOI `10.64898/2026.02.16.706214`.
- Six figures were discussed as comparison targets.
- “17 SCZ genes” in a reference Figure 6 was noted.
- Key interpretation problem remains donor-level vs cell-type/layer/domain comparability.
