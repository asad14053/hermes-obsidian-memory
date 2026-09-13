---
type: papers
project: ""
status: active
last_updated: 2026-09-12
confidence: medium
---

# Important Papers / References

## SCZ spatial transcriptomics reference
- bioRxiv DOI `10.64898/2026.02.16.706214`
- Main downstream concordance reference.
- Six figures were discussed as matching/comparison targets.

## PDGrapher
- Important for perturbation-response graph modeling / AIVC.
- User studied graph construction/update, inputs, and tier concepts.

## CellOT
- Causal/perturbation modeling reference.
- ⚠️ Verify exact benchmark numbers from paper before reuse.

## SpaGE
- Spatial gene-expression imputation reference.
- ⚠️ Verify exact benchmark numbers from paper before formal use.

## ENVI
- Reported best-performing imputation method in current GeneBridge benchmark.

## AIVC literature radar — 2026-09-12

Baseline note: the two earlier scheduled runs on 2026-09-12 failed before producing a report or durable literature update. Existing AIVC paper memory contained PDGrapher, CellOT, SpaGE, and ENVI; the papers below were not present in that note. Primary-source abstracts/full-text were checked on arXiv. No schizophrenia-specific paper was strong enough for this top-five set.

### READ NOW — GeneGeoFlow
- Citation: Li Q, Chi Y, Song L, et al. *Control-Anchored Residual Flow Matching Conditioned on Gene Geometry for Virtual Cell Perturbation Modeling*. arXiv:2608.06824v1 (2026-08-07). https://arxiv.org/abs/2608.06824v1
- Contribution: perturbation-conditioned multi-scale geometry from Gene Ontology and control-derived coexpression conditions a control-anchored residual flow; avoids treating a stable association graph as the actual intervention-response pathway.
- Reported result: Pearson Delta 0.8979 on Norman additive and 0.9088 on five held-out ComboSciPlex drug combinations.
- AIVC implication: strongest direct challenge to a fixed-GRN/GNN design; structural priors should guide representation while perturbation-specific dynamics are learned separately.
- Limitation: reported headline evidence is narrow and condition-level; cross-dataset, disease, donor, and spatial-context transport are not established.
- Research idea: learn cell-type- and spatial-niche-conditioned spectral geometry for DLPFC, with causal direction constraints and held-out-donor/perturbation tests.

### READ NOW — BioM-JEPA
- Citation: Wang Y, Zang Z, Liu Y, Lei Z, Li SZ. *BioM-JEPA: joint-embedding prediction of graph-connected gene blocks in single cells*. arXiv:2608.05928v1 (2026-08-06). https://arxiv.org/abs/2608.05928v1
- Contribution: JEPA student-teacher pretraining predicts representations of STRING/coexpression-connected gene blocks rather than reconstructing individual sparse genes; uses linear attention.
- Reported result: lowest aggregate perturbation-response error among evaluated CellBench models; 5.75× higher fine-tuning and 3.76× higher held-out embedding throughput than scFoundation in one matched hPancreas experiment.
- AIVC implication: supports gene modules as the computational unit and gives a scalable alternative to both gene-token transformers and graph message passing.
- Limitation: the graph is stable/associational rather than causal or context-specific, and the perturbation evidence concerns representation quality rather than a complete generative response simulator.
- Research idea: pretrain a DLPFC healthy/SCZ graph-block JEPA, then attach a perturbation-trained transformer/flow decoder and test whether disease-state modules improve unseen-perturbation transfer.

### READ NOW — DeMixPert
- Citation: Liu J, Cao X, Li Y, et al. *DeMixPert: Decomposed Response Modeling with Gaussian Mixtures for OOD Single-Cell Perturbation Prediction*. arXiv:2608.23114v1 (2026-08-24). https://arxiv.org/abs/2608.23114v1
- Contribution: explicitly separates basal-state systematic response, embedding-derived perturbation-specific response, and stochastic population variation; models heterogeneity with reusable Gaussian prototypes plus an invertible network.
- Reported result: best perturbation discrimination and energy distance across four reported benchmarks versus GEARS, scGPT, GenePert, scDFM, and STATE; abstract claims superior unseen-perturbation performance.
- AIVC implication: exposes a likely failure of monolithic graph/transformer predictors—shared response programs can dominate metrics while target-specific biology is missed.
- Limitation: dataset-specific gene spaces and no reported cross-dataset transfer; component identifiability and dependence on frozen scGPT target embeddings remain concerns.
- Research idea: decompose response into disease baseline, cell-type/niche context, perturbation-specific effect, and residual heterogeneity, then require each component to pass targeted biological metrics.

### READ NOW — PopPert
- Citation: Wang H, Qi J, Feng H, Lai B. *PopPert: Population-level Joint-Distribution Modeling for Single-Cell Perturbation Prediction*. arXiv:2609.01357v1 (2026-09-01). https://arxiv.org/abs/2609.01357v1
- Contribution: models control-to-perturbed changes directly at the population-distribution level, using gene marginals plus a low-rank Gaussian copula, rather than pretending destructive scRNA-seq provides paired cells.
- Reported result: superior aggregate performance across genetic and chemical benchmarks for DE recovery, perturbation-effect estimation, and multivariate distribution matching.
- AIVC implication: suggests that population-distribution prediction should be the primary objective; single-cell mappings should be treated as latent/non-identifiable unless additional assumptions are justified.
- Limitation: fixed shared factor loadings and a Gaussian copula restrict nonlinear/context-specific dependence; population summaries may hide rare subpopulation trajectories. The paper explicitly leaves context-dependent loadings, richer copulas, and calibrated uncertainty for future work.
- Research idea: use graph- or transformer-conditioned copula/flow factors that vary by cell type, donor, disease, and spatial niche, with calibrated uncertainty for rare SCZ cell states.

### READ NOW — VCBench/in-the-wild benchmark
- Citation: Mao X, Zhang S, Wen Q, et al. *Benchmarking virtual cell models for in-the-wild perturbation response*. arXiv:2604.27646v1 (2026-04-30). https://arxiv.org/abs/2604.27646v1
- Contribution: standardized modular evaluation under unseen cell contexts, unseen perturbations, and cross-dataset generalization; directly tests whether benchmark success survives realistic shifts.
- Key result: performance is highly context- and metric-dependent; common simplified setups overestimate practical capability and naive data aggregation can degrade results.
- AIVC implication: should shape the evaluation plan before architecture decisions and is highly fundable as rigor/reproducibility infrastructure for a K99/R00.
- Limitation: it is an evaluation framework rather than a mechanistic model; conclusions remain bounded by included datasets, shifts, and metrics.
- Research idea: build a schizophrenia/DLPFC AIVC benchmark with held-out donor, diagnosis, cell type, perturbation, spatial region, and dataset splits; require naive baselines, uncertainty, DE/module recovery, and causal/transport diagnostics.

### Synthesis / next action
The clearest program is not “GNN versus transformer.” Use graph-connected modules for representation (BioM-JEPA), keep stable graph geometry separate from learned perturbation dynamics (GeneGeoFlow), decompose target-specific and stochastic effects (DeMixPert), train/evaluate at the population-distribution level (PopPert), and make in-the-wild transport across donors/disease/spatial contexts the decisive benchmark (VCBench). Next action: turn these five design constraints into an AIVC architecture-and-evaluation matrix before selecting a backbone.
