---
type: errors-fixes
project: "AIVC"
status: planning
last_updated: 2026-10-10
confidence: medium
---

# AIVC — Errors and Fixes

- No stable implementation bug history is available yet.

## Evaluation-design pitfalls and fixes

- **Pitfall:** Treating a full-rank context × perturbation design as causal identification. **Fix:** separately document the exposure/intervention, confounder rationale, practical overlap, biological replication, and whether the estimand is observational or interventional.
- **Pitfall:** Treating “wins in four of five folds” as independent replication. **Fix:** use donor-level uncertainty and a prespecified meaningful-effect threshold; retrain within resampling when claiming full-pipeline uncertainty.
- **Pitfall:** Validating on only nominally significant measured genes. **Fix:** report the full frozen common-gene universe; keep selected-gene sign concordance as a transparent secondary diagnostic and redo selection inside resampling when making inferential claims.
- **Pitfall:** Conflating refitted no-context ablations with frozen-model input replacements. **Fix:** use the former to test incremental information and the latter to test fitted reliance; neither alone establishes biological causality.
- **Pitfall:** Tuning transfer or calibration rules on final-test responses. **Fix:** declare any target-calibration sample separately and protect the final test from model selection.

Source: [[02_Projects/AIVC/reviews/2026-10-06-NIA-K99-study-section-review]]. These are reusable design safeguards, not confirmed implementation bugs.
