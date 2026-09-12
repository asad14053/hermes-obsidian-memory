---
type: decisions
project: "GeneBridge"
status: active
last_updated: 2026-09-12
confidence: high
---

# GeneBridge — Important Decisions

- ✅ Br6432 excluded from downstream cohort due corruption.
- ✅ 300-gene, 3-fold gene-wise held-out evaluation is the core benchmark.
- ✅ Use raw counts for Xenium input/ground truth where specified.
- ✅ ENVI is the method to emphasize unless newer validated results supersede it.
- ✅ Use donor × layer pseudobulk for cohort DE rather than treating cells as independent donors.
- ✅ Do not assume same-donor Visium/Xenium are the same section or spatially aligned.
- ✅ Presentation emphasizes biology/spatial problem before imputation.
- ✅ Always record exact DE formula/covariates.
- ✅ Preserve donor, slide, run date, Dx, age, sex, and layer provenance.
