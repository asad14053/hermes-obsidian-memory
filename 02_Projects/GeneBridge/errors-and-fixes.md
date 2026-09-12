---
type: errors-fixes
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Errors and Fixes

## Downloader argument mismatch

Observed:
`download_24_common_xenium_visium.py: error: unrecognized arguments: --donor Br6432`

Lesson:
- inspect parser options before donor-specific reruns.
- relevant historical files:
  - `scripts/slurm/download_xenium.slurm`
  - `logs/download_xenium/%A_%a.*`
  - `data/metadata/download_manifest_24_common.csv`

## Conda failure

Observed:
`ModuleNotFoundError: No module named 'conda'`
from a Spack Miniconda path.

Lesson:
- when shell conda is broken, use direct interpreter/env paths.

## spatialLIBD

- Initial layer-adjusted DE hit a `spatialLIBD` error.
- Rerun later passed.
- ⚠️ VERIFY exact fix from logs before recreating environment.

## Br6432

- Corruption led to downstream exclusion.

## Result-count / formula sensitivity

- Prior discussions compared substantially different result counts (~34,987 vs ~48,300 in one workflow).
- User asked whether added slice/run covariates could affect results.
- ✅ LESSON: compare only after matching formula, unit of analysis, filtering, gene universe, domain definitions, and sample inclusion.
