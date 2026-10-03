---
type: literature-index
project: "AIVC"
status: active
last_updated: 2026-10-03
confidence: medium
---

# AIVC — Important Literature

This is a curated project index, not a claim that findings were reproduced in AIVC. Quantitative results below remain author-reported unless explicitly stated otherwise.

## Evaluation and recoverable response

### Miller et al. — calibrated perturbation metrics

- **Citation:** Miller HE, Mejia GM, Leblanc FJA, Swain B, Wang B, de Lima Camillo LP. *Deep learning perturbation models can outperform baselines on calibrated metrics.* Nature Biotechnology (2026). DOI: `10.1038/s41587-026-03307-w`.
- **Source:** https://www.nature.com/articles/s41587-026-03307-w
- **Durable use:** Calibrate evaluation metrics with informative positive and negative controls before interpreting baseline/model rankings. Keep outcome-derived calibration quantities out of training and model selection.
- **AIVC implication:** Beating simple baselines remains necessary, but raw MSE or another uncalibrated metric is not enough to establish success or failure.
- **Evidence limit:** The positive control is a benchmark diagnostic, not a deployable predictor or proof of causality.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-02-literature-radar]].

### Huang et al. — recoverable resolution of context-specific response

- **Citation:** Huang Y, Wang H, Li C, Wilson P. *The recoverable resolution of cellular perturbation-response prediction.* bioRxiv v1 (2026). DOI: `10.64898/2026.09.30.755756`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.09.30.755756v1
- **? UNCERTAIN:** Preprint; the radar review was based on partial PDF extraction, and the conclusions are conditional on the tested datasets, information sets, estimators, and definitions.
- **Durable use:** Evaluate context/donor-specific response recovery separately from final-state expression correlation or context recognition. Use independent replicate ceilings where available and report gene- and prespecified pathway-level endpoints.
- **AIVC implication:** A richer context embedding does not by itself demonstrate recovery of an environment-dependent response rule.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-02-literature-radar]].

## Spatial-context validation

### SpaCEy — spatial signal must beat non-spatial controls

- **Citation:** Rifaioglu AS et al. *SpaCEy links spatial tissue patterns to clinical outcomes using explainable graph neural networks.* Nature Communications 17, 10232 (2026). DOI: `10.1038/s41467-026-77924-z`.
- **Source:** https://www.nature.com/articles/s41467-026-77924-z
- **Durable use:** Treat the work as a validation-design comparator: require donor/patient-separated evaluation and show that spatial context adds value beyond expression-only, composition-only, and other non-spatial controls.
- **AIVC implication:** Matched neighborhood deletion or shuffling can test predictive dependence, but model-input deletion and attention sensitivity are not biological interventions or causal validation.
- **Evidence limit:** Cancer spatial proteomics and survival prediction do not establish neural perturbation-response validity.
- **Radar source:** [[02_Projects/AIVC/literature/2026-09-28-literature-radar]].
