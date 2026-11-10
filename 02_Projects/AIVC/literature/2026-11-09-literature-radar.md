---
tags: [AIVC, literature-radar, perturbation-prediction, causal-GRN, single-cell-foundation-model, regulatory-genomics, agentic-world-model]
date: 2026-11-09
previous_cutoff: 2026-11-06T10:02:43Z
---

# AIVC Literature Radar — 2026-11-09

Compared with [[2026-11-06-literature-radar]] (SPEAR, RAPTORGraph, Perturbscape, foundation-model audit, CRISP). These five are absent from that note and from prior radar session history. CausalODE and scDisentangle were posted on November 6; MUSS (November 5), the low-rank decoder audit (November 4), and CellCanon (November 4) were newly surfaced omissions whose upload dates precede the exact previous cutoff. Results below are author-reported; only the low-rank audit states peer acceptance (NeurIPS 2026). No new schizophrenia-specific paper met the threshold.

## 1. Low-rank decoder reliability audit — READ NOW
**Citation:** Zhang Z, Huang Y, Feng F, Liu J. *A low-rank decoder bottleneck bounds reliability in foundation-model perturbation prediction.* arXiv:2611.05849v1, 2026. Accepted at NeurIPS 2026. https://arxiv.org/abs/2611.05849v1

- **Problem:** Aggregate scores do not tell whether an individual virtual-cell prediction is reliable.
- **Method/result:** Mechanistic audit of STATE's state-transition decoder paired with SE-600M, scGPT, and Tahoe-x1 across four CRISPRi cell lines. Its first attention block collapses prediction into 4–32 training-derived directions; accuracy declines with response distance to training data. Predicted nearest-neighbor distance correlates with per-perturbation PDC at mean |Spearman rho| 0.81 (oracle 0.88) and transfers across encoders/cell lines.
- **New:** Links an internal low-rank circuit to interpolation-limited reliability and supplies a deployable per-prediction confidence score.
- **Bad:** Specific to the ST decoder and mostly pseudobulk PDC; strict family holdout weakened or reversed the confidence relationship in RPE1, and combinatorial/donor/disease transport was not tested.
- **AIVC value/idea:** Require support-distance calibration and abstention. Test whether graph/transformer variants still predict outside the training-response subspace under donor × target × context holdouts.

## 2. CausalODE — READ NOW
**Citation:** Qian W, Song Y, Welch JD. *Inferring gene regulatory networks from single-cell perturbation data by optimizing causal reach of latent mediator dynamics.* bioRxiv 2026.11.05.764481, posted 2026-11-06. https://doi.org/10.64898/2026.11.05.764481

- **Problem:** Perturb-seq GRN methods poorly represent nonlinear feedback, transient RNA kinetics, and unmeasured protein mediators; expression error does not validate graph quality.
- **Method/result:** Differentiable ODE with latent protein dynamics, feedback, and a causal-reach objective requiring perturbation-responsive genes to be downstream. It reports higher graph AUPRC/top-edge precision in simulation and ~60%/80% gains over the strongest comparator on causal reach in CaRPool-seq/Norman data; edges enrich orthogonal regulatory evidence and distinguish held-out non-additive pairs.
- **New:** Makes intervention reachability a trainable and real-data graph-evaluation criterion while modeling latent mediator dynamics.
- **Bad:** Real-data causal reach is partly self-referential because the same intervention-response pattern defines the objective and metric; ChIP/STRING enrichment remains indirect, and latent proteins are inferred rather than measured.
- **AIVC value/idea:** Use causal reach as an auxiliary loss and falsification metric, but require held-out perturbations plus independent TF-binding/protein/time-course evidence and rewired-graph controls in SCZ-relevant cells.

## 3. scDisentangle — READ NOW
**Citation:** El Mejjad S, Enezari S, Bedraoui A, et al. *scDisentangle: sequential disentanglement for single-cell perturbation response prediction.* bioRxiv 2026.11.04.764292, posted 2026-11-06. https://doi.org/10.64898/2026.11.04.764292

- **Problem:** Perturbation models often reproduce population means while erasing source-cell identity and context-dependent response heterogeneity.
- **Method/result:** Sequentially decomposes known attributes and residual latent factors; counterfactuals swap the perturbation attribute while preserving cell-specific residuals. It beats deep and naive baselines on cytokine, infection, and held-out genetic-combination tasks (top-20-DEG R² delta 81.9% vs 67.4% match-mean) and predicts donor-specific cardiac CD8 states from blood.
- **New:** Identity-preserving, coarse-to-fine counterfactual generation without adversarial independence or distribution matching, plus an explicit source-cell proximity metric.
- **Bad:** Source-cell identity is unobserved across destructive scRNA-seq, so proximity is a structural preference rather than true paired counterfactual validation; disease examples are retrospective and not donor-held-out DLPFC perturbations.
- **AIVC value/idea:** Add identity-preserving residuals to the AIVC and test them with lineage/clone or repeated-donor evidence; compare against context-mean and match-mean baselines before claiming cell-resolved counterfactuals.

## 4. MUSS — READ NOW
**Citation:** Zheng K, Vahidi A, Jin L, et al. *MUSS: A Multi-scale and Sequence-based Model for Single-cell Gene Regulation.* arXiv:2611.08086v1, 2026. https://arxiv.org/abs/2611.08086v1

- **Problem:** Sequence models lack cell resolution, while single-cell token models lose DNA regulatory grammar and cannot generalize to unseen genes/peaks.
- **Method/result:** Frozen AlphaGenome sequence embeddings feed peak self-attention and bidirectional, distance-biased peak–gene cross-attention; peak masking and paired scATAC/scRNA training align sequence with cell state. MUSS retains positive single-cell PCC on unseen sequences across four datasets and improves enhancer–gene retrieval (micro-AUPRC 0.1271 vs 0.0834 Borzoi and 0.0532 PCA+Ridge).
- **New:** A sequence-grounded graph-transformer-like regulatory layer that transfers beyond a fixed gene/peak vocabulary.
- **Bad:** Mostly PBMC/hematopoietic data, expensive quadratic peak attention, paired ATAC–RNA dependence, several single-run results, and enhancer links use incomplete proxy truth rather than perturbational validation.
- **AIVC value/idea:** Initialize AIVC gene/edge representations with sequence + accessibility, then test whether they improve unseen-gene perturbation response beyond distance-only, expression-only, AlphaGenome-only, and permuted-link controls in neuronal cells.

## 5. CellCanon — SAVE
**Citation:** Liang Z, Zhuang S, Jiao X, Chen H. *CellCanon: An Agentic Cellular World Model for Prediction, Explanation, and Observation-Driven Updating.* arXiv:2611.05890v1, 2026. https://arxiv.org/abs/2611.05890v1

- **Problem:** Virtual-cell predictions, mechanistic explanations, and updates from new experiments are usually separate and not jointly provenance-tracked.
- **Method/result:** A shared world state links retrieved drug/target/pathway evidence, an observation atlas, MLP response heads, generated cells, source-checked explanations, and fixed-weight updates. On 339 held-out SciPlex3 conditions it reports +63.3% DE AUPRC and +17.3% macro-F1 over metric-specific best baselines; one measured context per drug improves unmeasured-context prediction.
- **New:** Treats a virtual cell as a revisable evidence-and-observation system rather than only a predictor.
- **Bad:** One drug screen, three cancer lines, 2,931-gene panel, simulated feedback rather than prospective experiments, and evidence retrieval may aid interpolation without establishing mechanism; the broad “world model” label exceeds the demonstrated scope.
- **AIVC value/idea:** Build a provenance-aware SCZ AIVC ledger that links each prediction to support distance, graph/sequence evidence, uncertainty, and subsequent Xenium/iPSC measurements, but keep this outside the predictive-core novelty claim until prospectively validated.
