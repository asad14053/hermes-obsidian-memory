---
type: hpc
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# HPC — HGCC

## Identity/root
- User path identity: `mjabin`
- GeneBridge root: `/beegfs/labs/hulab/projects/mjabin/GeneBridge`

## Resource preferences
- Earlier typical jobs: 160 GB / 16 CPUs.
- ✅ DECISION: heavy 23-donor work → **200 GB RAM / 16 CPUs**, parallelize donors when safe.
- Historical interactive example: 8 CPUs / 64 GB / 4 h.

## Storage
- BeeGFS project storage for large data.
- Historical home quota: 50 GB.
- `dtn01.hgcc` referenced for transfer.
- Avoid large data in home.

## Workflow
- SLURM arrays for donor parallelism.
- `%A_%a` log naming.
- Inspect both stdout/stderr before changing code.
- Verify CLI parser options before resubmitting.
