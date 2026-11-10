---
type: errors-fixes
project: "AIVC"
status: planning
last_updated: 2026-11-07
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
- **Pitfall:** Interpreting donor-held-out spatial/context prediction gains as neighborhood biology without excluding capture gradients or composition proxies. **Fix:** prespecify assay-specific nuisance adjustment plus composition-matched and shuffled-neighborhood controls; require independent-assay confirmation before biological interpretation. **⚠️ VERIFY:** preprint-derived safeguard, not an AIVC result or adopted architecture change.
- **Pitfall:** Treating attention weights, learned gates, or graph-aware attributions as mechanistic or causal evidence. **Fix:** separate predictive reliance from biological mechanism; compare against refit-based removal with plausible-support replacements and independent perturbation evidence. Graph-aware attribution remains conditional on the supplied graph and can fail with omitted edges or non-additive regulation. **⚠️ VERIFY:** preprint- and simulation-derived safeguard, not an AIVC result.

## New reusable safeguards — November 2026 radar

- **Pitfall:** Calling a response model successful without comparing it with experimental repeatability. **Fix:** report a replicate-reliability ceiling and distributional scores where repeat data exist; keep this as a benchmark reference, not evidence of transfer to neural donors.
- **Pitfall:** Treating neighborhood-associated expression as a context-induced state change when cell-type abundance shifted. **Fix:** separate composition/abundance from within-cell-type state and include composition-only and shuffled-neighborhood controls.
- **Pitfall:** Assuming a biologically plausible Hi-C or learned graph prior is predictive or causal. **Fix:** require it to beat simple distance, accessibility-only and degree-preserving controls on protected target-response tests.
- **Pitfall:** Using expression-matched token deletion or random cell splits as perturbation evidence. **Fix:** use target-expression-matched negative contrasts, replicate-aware ground truth, and donor/clone/independent-unit-disjoint evaluation.

Sources: [[02_Projects/AIVC/reviews/2026-10-06-NIA-K99-study-section-review]]; [[02_Projects/AIVC/literature/2026-10-16-literature-radar]]; [[02_Projects/AIVC/literature/2026-10-19-literature-radar]]; [[02_Projects/AIVC/literature/2026-10-23-literature-radar]]; [[02_Projects/AIVC/literature/2026-11-02-literature-radar]]; [[02_Projects/AIVC/literature/2026-11-04-literature-radar]]; [[02_Projects/AIVC/literature/2026-11-06-literature-radar]]. These are reusable design safeguards, not confirmed implementation bugs.
