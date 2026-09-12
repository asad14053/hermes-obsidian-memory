---
type: software-environments
project: ""
status: active
last_updated: 2026-09-12
confidence: high
---

# Software Environments

## GeneBridge Python
`/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_scanpy`

Direct Python:
`/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_scanpy/bin/python`

## GeneBridge R
`/beegfs/labs/hulab/projects/mjabin/conda_envs/genebridge_r`

## Historical Imputation env
- `Imputation`
- PyTorch 2.1.2
- CUDA False in one VISTA context.

## Local AI
- LM Studio
- Qwen3-8B historically loaded
- Nomic embedding model historically loaded

## Known caveat
`conda` previously failed with `ModuleNotFoundError: No module named 'conda'` from a Spack Miniconda path. Prefer direct interpreter paths if activation is unreliable.
