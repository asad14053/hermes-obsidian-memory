---
type: literature-index
project: "AIVC"
status: active
last_updated: 2026-10-10
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

### Qi and Chapfuwa — transportability depends on mechanism

- **Citation:** Qi S, Chapfuwa P. *Mechanisms Matter: Transportability of Cellular Perturbation Effects.* bioRxiv v3 (2026). DOI: `10.64898/2026.05.08.723625`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.05.08.723625v3
- **Durable use:** Treat cross-context perturbation transfer as a supported-mechanism question. Similar embeddings or aligned expression distributions do not establish transport; compare against simple response baselines and prespecify when to abstain.
- **Evidence limit:** Results are author-reported and partly semi-synthetic. Mechanistic-divergence diagnostics estimated from protected test responses would leak outcomes.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

### Yang et al. — risk-calibrated causal extrapolation

- **Citation:** Yang F, Lei H, Chen Y, Du J-H. *Risk-Calibrated Balancing for High-Dimensional Causal Extrapolation.* arXiv:2609.34482v2 (2026).
- **Source:** https://arxiv.org/abs/2609.34482v2
- **Durable use:** Add overlap and weight-concentration diagnostics to transport benchmarks, and separate a permitted target-calibration sample from the protected final test.
- **Evidence limit:** This is a revision candidate, not a newly introduced method. It does not solve hidden confounding or zero support.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-05-literature-radar]].

### Lorch et al. — latent causal diffusions

- **Citation:** Lorch L, Zhang J, Bunne C, Krause A, Schölkopf B, Uhler C. *Latent causal diffusions for single-cell perturbation modeling.* PNAS (2026). DOI: `10.1073/pnas.2602630123`.
- **Source:** https://www.pnas.org/doi/10.1073/pnas.2602630123
- **Durable use:** Use as a mechanistic comparator for additive, ridge, graph-transformer, and conditional-VAE response models; keep causal interpretation tied to interventions and explicit model assumptions.
- **Evidence limit:** Author-reported performance; steady-state and intervention-entry assumptions do not establish transfer to unseen donors, tissues, or wholly unseen targets.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

## Spatial-context validation

### Jin et al. — spatial perturbation screening of non-autonomous effects

- **Citation:** Jin K et al. *MERFISH-based pooled genetic screening reveals cell non-autonomous phenotypes in intact tissue.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.06.756924`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.06.756924v1
- **Durable use:** A candidate measured-response benchmark for sender-to-receiver effects. Before use, verify downloadable assignments, animal identifiers, controls, baseline-available inputs, and receiver-cell endpoints; hold out animals and perturbed genes.
- **Evidence limit:** Mouse liver is not human brain or aging/AD, and post-treatment neighborhood expression cannot be treated as a baseline predictor of the same response.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-07-literature-radar]].

### Wang et al. — domains are not automatically functional niches

- **Citation:** Wang Y, Chen Y, Yang L, Wang C, Cai J, Xin H. *Benchmarking niche identification via domain segmentation for spatial transcriptomics data.* bioRxiv v3 (2026). DOI: `10.64898/2026.02.27.708202`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.02.27.708202v3
- **Durable use:** Do not treat cortical layers or spatial clusters as validated signaling neighborhoods. Evaluate context features on held-donor measured outcomes rather than cluster-label agreement alone.
- **? UNCERTAIN:** The substantive novelty of v3 versus earlier versions was not verified; the main reference is a manually annotated lymph-node setting.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-05-literature-radar]].

### Wu et al. — VINTER identity/environment comparator

- **Citation:** Wu J et al. *VINTER: a generative vision-language model for annotating and interrogating spatial tissues.* bioRxiv v1 (2026). DOI: `10.64898/2026.10.01.752251`.
- **Source:** https://www.biorxiv.org/content/10.64898/2026.10.01.752251v1
- **Durable use:** Compare AIVC against a simple donor-held-out identity-plus-context representation and test whether input-edit predictions track independent measured responses.
- **Evidence limit:** Input edits are not biological perturbations. The reported DLPFC setup is not clean unseen-donor evaluation because paired sections from a donor can span train and holdout, and part of the holdout supports checkpoint selection.
- **Radar source:** [[02_Projects/AIVC/literature/2026-10-09-literature-radar]].

### SpaCEy — spatial signal must beat non-spatial controls

- **Citation:** Rifaioglu AS et al. *SpaCEy links spatial tissue patterns to clinical outcomes using explainable graph neural networks.* Nature Communications 17, 10232 (2026). DOI: `10.1038/s41467-026-77924-z`.
- **Source:** https://www.nature.com/articles/s41467-026-77924-z
- **Durable use:** Treat the work as a validation-design comparator: require donor/patient-separated evaluation and show that spatial context adds value beyond expression-only, composition-only, and other non-spatial controls.
- **AIVC implication:** Matched neighborhood deletion or shuffling can test predictive dependence, but model-input deletion and attention sensitivity are not biological interventions or causal validation.
- **Evidence limit:** Cancer spatial proteomics and survival prediction do not establish neural perturbation-response validity.
- **Radar source:** [[02_Projects/AIVC/literature/2026-09-28-literature-radar]].
