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

## AIVC literature radar — 2026-09-16

Search window: after the prior radar run on 2026-09-12 12:33 UTC through 2026-09-16. The five records below were checked against the previous radar output/session; none had been reported there. No new schizophrenia-specific single-cell or perturbation paper met the top-five threshold.

### READ NOW — Causal path analysis across perturbational and population single-cell data
- Citation: Park K, Li H. *Causal Path Analysis from Perturbational and Population-Scale Single-Cell Data with Multiscale Confounding and Measurement Error*. arXiv:2609.16510v1 (2026-09-15). https://arxiv.org/abs/2609.16510v1
- Contribution: transfers only an ancestral ordering/scaffold from Perturb-seq, then re-estimates direct edges and gene-to-phenotype effects in the target population; uses cell- and subject-level surrogate variables plus errors-in-variables correction.
- Reported result: simulations show lower DAG, outcome-regression, and total-causal-effect error than naive, SVA-only, or EIV-only variants. In an AML example (30 subjects, 25 genes), 21 genes had nonzero estimated total effects; their signs agreed with adjusted marginal effects 81% of the time (rho=0.57).
- AIVC implication: a principled route for transporting perturbational structure into human donor/disease data without assuming the complete cell-line GRN transfers unchanged.
- Limitation: requires the external ancestral set to contain every true parent, exclude descendants, and preserve order; assumes a linear acyclic SEM and restrictive error/confounding structure. The real-data demonstration is small and non-interventional at the clinical-outcome level.
- Research idea: use CRISPR/Perturb-seq only to constrain candidate causal order, then re-estimate cell-type-specific DLPFC edges and SCZ-relevant path effects with donor-level outcomes and measurement-error correction.

### READ NOW — Immune World Model
- Citation: Cui T, Wang X, Li Z, et al. *An immune world model for multiscale forecasting and therapeutic hypothesis generation*. arXiv:2609.14709v1 (2026-09-13). https://arxiv.org/abs/2609.14709v1
- Contribution: an action-conditioned hierarchical state-transition model links cell programs, tissue immune context, and patient state; supports bounded sequential/combinatorial rollouts. A governed evolutionary “AI Scientist” selected the final frozen configuration.
- Reported result: on the displayed Parse PBMC few-shot benchmark, Pearson-delta rose from 0.309 (cell mean), 0.427 (additive), and 0.462 (Rhaister) to 0.495; the paper also evaluates 23 unseen perturbation pairs and nominates IL-36gamma plus SIRPalpha inhibition.
- AIVC implication: useful blueprint for making an AIVC explicitly multiscale and action-conditioned instead of a single expression predictor, and for separating model development from locked confirmation.
- Limitation: all analyses reuse public data; the therapeutic combination is a prospectively testable hypothesis, not experimental validation. Cross-scale rollouts join heterogeneous datasets and therefore are not evidence of one identified causal process.
- Research idea: build a DLPFC world model with separate intracellular, spatial-niche, and donor/disease states, but require each transition and any cross-scale rollout to pass held-out-donor and prospective perturbation checks.

### READ NOW — scKITE
- Citation: Zhang H, Bao J, Ma M, et al. *Towards a knowledge-enhanced single-cell foundation model*. arXiv:2609.14970v1 (2026-09-14). https://arxiv.org/abs/2609.14970v1
- Contribution: adds temporary cell-annotation and gene-regulatory auxiliary decoders to a shared transcriptomic Transformer during pretraining; discards them afterward. The design tests knowledge supervision as an alternative scaling axis to more cells/parameters.
- Reported result: across four pretraining scales, knowledge enhancement gave an average 28.8% relative downstream improvement over the same model without it; with 179,067 pretraining profiles, scKITE reportedly outperformed much larger scFMs on annotation, integration, and GEARS-based perturbation tests.
- AIVC implication: directly supports the hypothesis that a modest model with explicit regulatory/annotation supervision may beat brute-force transcriptome scaling; relevant to a GRN-plus-transformer AIVC.
- Limitation: auxiliary labels/regulons are noisy and partly circular products of existing annotations and inferred GRNs; perturbation evidence uses frozen embeddings inside GEARS rather than validating a complete generative virtual cell. Independent, donor/disease/spatial transport is unproven.
- Research idea: pretrain with DLPFC cell-identity and context-specific regulon supervision, then ablate each knowledge source under sealed donor, diagnosis, and perturbation splits to test whether knowledge—not label leakage—drives gains.

### SAVE — RAGCell
- Citation: Liu T, Zhang F, Chen J, et al. *RAGCell: Retrieval-Augmented Generation as Supervision for Versatile Single-cell Analysis*. arXiv:2609.14147v1 (2026-09-12). https://arxiv.org/abs/2609.14147v1
- Contribution: builds cell- and feature-level text knowledge bases with LLMs, aligns a lightweight patch Transformer to those embeddings, and retrieves text representations at inference.
- Reported result: training cost is reported below one tenth of pretraining-based scFMs. On Tabula Sapiens Immune, macro-F1 was 0.723 versus 0.691 for scFoundation; on fetal bone marrow, RAGCell was only third on macro-F1 (0.74 versus 0.78 for scFoundation).
- AIVC implication: retrieval can externalize biological knowledge and lower compute, potentially useful as an annotation/mechanism sidecar rather than the causal dynamics core.
- Limitation: some prompts explicitly contain cell type or drug-sensitivity labels, creating a circular-supervision/leakage risk; LLM-generated biology can hallucinate; performance is mixed on rare/developmental populations; this is not a perturbation-response simulator.
- Research idea: retrieve only provenance-tracked pathway/target evidence unavailable from test labels, then measure incremental value over expression-only, PCA, and curated-database controls.

### SAVE — HyCLoST
- Citation: Vega D, Cárdenas P, Ceballos H, Manrique L, Arbeláez P. *Hyperbolic Contrastive Learning with Entailment for Spatial Transcriptomics*. arXiv:2609.16207v1; accepted MICCAI 2026 (2026-09-14). https://arxiv.org/abs/2609.16207v1
- Contribution: maps UNI2-h histology and Geneformer expression embeddings into a shared Lorentz space; combines hyperbolic contrastive learning with directional gene-to-image entailment and kNN expression retrieval.
- Reported result: across 26 SpaRED datasets, mean MSE was 0.899 and PCC 0.431, reported as 6% lower MSE and 8% higher PCC than the next best; it ranked first on 10/26 datasets.
- AIVC implication: hierarchical geometry and directional cross-modal constraints may be useful for spatial context encoders and morphology-expression alignment.
- Limitation: predicts only the top 128 or 32 spatially autocorrelated genes and uses training-set kNN retrieval; it does not model interventions, causal regulation, disease transfer, or whole-transcriptome dynamics. “Gene entails image” is an inductive assumption, not identified causality.
- Research idea: use hyperbolic geometry for DLPFC cell-niche-program hierarchies, but attach it to a perturbation-trained population decoder and test against Euclidean, graph, and simple kNN baselines.

### Program synthesis / next action
The most consequential new constraint is transportability: use perturbational networks as partial ordering information, not a fixed GRN, and re-estimate effects in the target donor/disease population. Pair that with a hierarchical action-conditioned world model, but do not treat cross-dataset rollouts as causal validation. Immediate design update: add (1) a perturbational scaffold versus target-population re-estimation module, (2) explicit cell/tissue/donor state levels, and (3) leakage audits for every biological-knowledge supervision source.

## AIVC literature radar — 2026-09-18

Search window: after the prior radar run on 2026-09-16 through 2026-09-18 10:01 UTC. arXiv date-bounded searches covered single-cell, perturbation/virtual-cell, spatial transcriptomics, transcriptomics, gene regulation, and q-bio categories, with complementary web/bioRxiv searches. Only one genuinely new paper cleared the relevance and novelty threshold; no schizophrenia-specific paper qualified. This record was checked against the 2026-09-12 and 2026-09-16 radar outputs and was not previously reported.

### READ NOW — CellRFT
- Citation: Yan J, Liu L, Guo H, et al. *CellRFT: Reinforcement Fine-Tuning for Single-Cell Perturbation Modeling*. arXiv:2609.19970v1 (2026-09-17). https://arxiv.org/abs/2609.19970v1
- Research problem: perturbation generators optimize reconstruction, denoising, or distribution-matching surrogates, while evaluation uses non-differentiable population-level biological metrics; reducing the training loss therefore need not improve the biology being judged.
- Method: policy-gradient fine-tuning generates multiple candidate cell populations per perturbation, assigns each set a population-level Cell-Eval reward, shares its group-relative advantage across constituent denoising trajectories, and uses hierarchical aggregation that averages within global-response, differential-expression, and perturbation-discrimination categories before averaging categories. The framework was applied to scratch-trained and pretrained/fine-tuned PerturbDiff.
- Reported result: on the Replogle benchmark (2,023 perturbations across K562, RPE1, Jurkat, and HepG2; HepG2 as target context), scratch PerturbDiff + CellRFT improved all 13 reported metrics. Examples: DE overlap 0.190→0.236, log-fold-change Spearman 0.342→0.452, AUPRC 0.210→0.270, and cosine perturbation discrimination 0.575→0.697. Applied after PerturbDiff pretraining/fine-tuning, it improved 9/13 metrics but reduced all three perturbation-discrimination scores. Hierarchical full-reward training improved all 11 directly studied reward metrics and beat flat averaging in mean gain.
- AIVC implication: the AIVC objective should be treated as a multi-objective biological specification, not a generic denoising loss. CellRFT also supplies a useful diagnostic: optimize candidate metrics separately to map which readouts reinforce or conflict before fixing the final objective.
- What is new: it aligns policy-gradient units with population-level single-cell evaluation and analyzes reward complementarity/redundancy instead of merely adding one pathway or GRN reward.
- What is bad: evidence is limited to one processed Replogle benchmark, one target cell line, and variants of one diffusion backbone; no held-out donor, disease, chemical, combination, spatial, or cross-dataset validation is shown. Optimizing benchmark metrics risks metric overfitting/reward hacking; the paper itself finds recall-driven precision/Pearson collapse and degradation of discrimination after some fine-tuning. Metrics are proxies, not mechanistic or causal validity, and code was only promised at v1.
- Research idea: add a sealed reward-design phase to the DLPFC/SCZ AIVC: estimate a reward-interaction matrix across DE/module recovery, perturbation identity, pathway direction, population distance, donor transport, calibration, and spatial-niche fidelity on training/validation donors only; then hierarchically fine-tune with a compact Pareto-safe reward subset and evaluate once on untouched donors, perturbations, diagnoses, and datasets.

### Program update
Do not make CellRFT the core architecture. Use it as a late-stage alignment and evaluation-stress-test layer after the population-level, transport-aware model is validated against simple baselines. Pre-register protected metrics and sealed test contexts so direct reward optimization cannot turn the benchmark into the training target.

## AIVC literature radar — 2026-09-21

### Scope, continuity, and evidence limits

Intended interval: after the September 18 radar through this September 21 scheduled run. Three newly surfaced papers were selected, rather than padding the list to five. scMGFGRN v1 was posted September 19. match-seq v1 and scHPGT were published September 18; the exact public posting times relative to the prior run at approximately 10:02 UTC were not available, so these are boundary-day discoveries, not proven post-cutoff publications. DOI-embedded dates are not posting dates.

Live vault read/search tools were unavailable in this run. Comparison used supplied recalled Obsidian reviews and session-history copies of the September 18 radar and September 21 weekly strategy, not a fresh filesystem audit. A targeted session-history search found no previous assistant mention of match-seq, scMGFGRN, or scHPGT; this is partial deduplication, not a complete vault search. CellRFT was previously reported and is not repeated.

Discovery included date-targeted web searches for perturbation models, virtual cells, single-cell transformers, GRNs, spatial models and schizophrenia, plus arXiv API queries. Some API and publisher extractions failed or timed out; successful arXiv queries for single-cell and transcriptomics were inspected. No exhaustive-coverage claim is made. scHPGT assessment is abstract-level because publisher full-text/PDF access failed. match-seq PDF Results/Discussion and the scMGFGRN manuscript were read. No newly qualifying schizophrenia-specific paper was verified.

### 1. READ NOW — match-seq / Perturb-match

**Citation:** Du PP, Kohno ST, Wang M, et al. *In vivo intercellular CRISPR screens using viral proximity barcoding reveal regulators of tumor-immune interactions*. bioRxiv, version 1, posted September 18, 2026. DOI: 10.64898/2026.09.16.752238.
**Source:** https://www.biorxiv.org/content/10.64898/2026.09.16.752238v1
**Full text:** https://www.biorxiv.org/content/10.64898/2026.09.16.752238v1.full.pdf
**Status:** preprint; boundary-day discovery.

- **Research problem:** Conventional pooled CRISPR fitness screens miss perturbations whose important effects occur in neighboring cells rather than in the perturbed cell's abundance.
- **Method:** match-seq transfers RNA barcodes from genetically defined sender cells to nearby receiver cells using PEG10 virus-like particles. Perturb-match combines this proximity readout with pooled CRISPR and scRNA-seq to associate sender perturbations with receiver composition and transcriptional state. Barcode-mixture regression estimates receiver response relative to safe-control senders.
- **Key result:** The screen targeted 132 genes across nine tumors and profiled 149,726 cells after QC. Tgfb1 and Nectin3 loss showed little pooled fitness effect but suppressed growth when deleted throughout tumors. Immune-cell depletion supported distinct effectors: CD8 T cells/macrophages for Tgfb1, CD4 T cells for Traf7, and NK cells for Nectin3. Sources: PDF pp. 5–6, 8, 10–13; Fig. 4.
- **What is new:** Sequencing-based, highly multiplexed proximity information connects a genetic intervention in one population to responses in another, with functional validation beyond expression prediction.
- **Why it matters for AIVC:** This supplies an experimental precedent for a spatially informed perturbation model, unlike attaching unrelated spatial context to dissociated perturbation data. It supports modeling both cell-intrinsic and receiver/niche effects. Relative to the current notes' missing eligible data design, it is a candidate methodological benchmark—not an aging/AD dataset or evidence for the NIA premise.
- **What is bad / limitations:** Main screen is a murine tumor system, not human brain or aging. Labels reflect a proximity kernel rather than direct contact: labeling probability halves every 46 micrometers, and the median 90th-percentile receiver distance is within 250 micrometers. Multiple barcodes per receiver complicate attribution. PEG10 reduced, but did not eliminate, transcriptomic effects (1,184 significant DE genes versus infection-naive macrophages in the characterization experiment). Spatial calibration used one tumor section. Treat inferred edges as noisy exposure measurements, not established signaling pathways. Sources: PDF pp. 3, 5–6, 8.
- **Future research idea (proposal, not result):** Develop a population-response benchmark with separate sender and receiver outcomes, an explicit probabilistic exposure graph, tumor-held-out evaluation, and degree-preserving shuffled-graph controls. Test whether measured neighborhood information improves receiver prediction over cell-intrinsic and perturbation-mean baselines. A later neural co-culture adaptation would require new feasibility evidence and collaborators; it is not demonstrated by this paper.

### 2. READ NOW — scHPGT (abstract-level assessment)

**Citation:** Cheng Z, Zhang J, Zhang S. *Regulatory-prior-guided attention preserves biological structure during unpaired single-cell RNA–ATAC integration*. Bioinformatics, btag696, published September 18, 2026. DOI: 10.1093/bioinformatics/btag696.
**Source:** https://doi.org/10.1093/bioinformatics/btag696
**Verified metadata and abstract:** https://api.crossref.org/works/10.1093/bioinformatics/btag696
**Status:** journal article; boundary-day discovery; quantitative/full-text evaluation unresolved.

- **Research problem:** Distribution-matching integration of unpaired RNA and ATAC can incorrectly align biologically distinct, condition-specific, or unmatched states.
- **Method:** Modality-specific encoders, a cross-modal Transformer with gene–peak regulatory-prior-constrained attention, and a domain-adversarial shared latent space.
- **Key result:** The publisher-deposited abstract reports improvements in clustering agreement, label transfer, and biological structure preservation across PBMC3k, mouse spleen, CITE-seq/ASAP-seq PBMC, and PBMC10k. Partial-overlap and condition-shift experiments reportedly align shared populations without forcing unmatched states into correspondence. No numerical effect sizes were verified.
- **What is new:** The important design emphasis is prior-guided alignment that preserves unmatched and condition-specific states, rather than maximizing modality mixing alone.
- **Why it matters for AIVC:** Your context-conditioned AIVC must preserve SCZ/AD/age-associated basal differences rather than erase them as batch effects. This is closely related prior-guided Transformer work and further weakens a generic claim that adding regulatory edges to attention is the main innovation. It is an integration model, not a perturbation-trained response simulator.
- **What is bad / limitations:** Assessment is limited to the abstract. Robustness to incorrect regulatory priors, strict donor holdouts, and numerical gains could not be audited. The stated benchmarks are immune systems; the accessible evidence does not establish neural, disease-perturbation, or external intervention generalization. Attention-derived regulatory links are not proof of causality.
- **Future research idea (proposal, not result):** Prespecify a condition-preservation stress test for a future paired-data-eligible DLPFC AIVC: compare no integration, aggressive alignment, and prior-guided alignment under donor/context holdouts; require improvement in independent response prediction without loss of measured disease-effect directions or collapse of unmatched cell states. Corrupt and shuffle priors to test whether gains depend on genuine regulatory information.

### 3. SAVE — scMGFGRN

**Citation:** Zhong L, Yan B, Wang J, Xie M. *Multi-model biological and sequence information fusion for gene regulatory network inference from single-cell transcriptomics*. bioRxiv, version 1, posted September 19, 2026. DOI: 10.64898/2026.09.13.751326.
**Source:** https://www.biorxiv.org/content/10.64898/2026.09.13.751326v1
**Full text read:** https://www.biorxiv.org/content/10.64898/2026.09.13.751326v1.full.pdf
**Status:** preprint; verified post-cutoff publication.

- **Research problem:** GRN link prediction underuses complementary transcriptomic, ontology, promoter-sequence, and trajectory information.
- **Method:** Denoising autoencoder for expression-derived features; Slingshot pseudotime followed by a bidirectional GRU; GAT on the GO hierarchy; DNABERT-2 promoter embeddings; gated multi-head attention fusion; supervised TF–target edge classification.
- **Key result:** Across seven human/mouse benchmark datasets, the authors report mean STRING TFs+500 AUROC of 94.03% versus 91.19% for scMGATGRN. In Table 1, the full model's AUROC is 0.9486 versus 0.9116 for DAE+Bi-GRU. Sources: Results IV.A and IV.D/Table 1. These are authors' reported numbers, not reproduced benchmarks.
- **What is new:** The combined representation and gated fusion of GO hierarchy, promoter sequence, expression, and pseudotime; not a new demonstration that graph attention alone recovers causal regulation.
- **Why it matters for AIVC:** This is directly overlapping prior art for a biology-informed graph/attention model. It may provide a candidate structural-prior baseline, but does not predict full post-intervention expression distributions and should not displace the simple response baselines in the weekly strategy.
- **What is bad / limitations:** Methods III.F uses balanced sampled TF–target pairs and fivefold cross-validation, not demonstrated held-out-donor/perturbation transport. Pairwise splits can retain gene identities across folds. STRING functional associations and ChIP binding are imperfect proxies for direct causal regulation. Pseudotime is not measured intervention time; adding bidirectional sequence modeling does not solve identification. GO-informed input followed by GO-enrichment validation is not independent evidence. Prospective perturbation validation is absent from the reported analyses. Interpretation of attention as mechanism is too strong.
- **Future research idea (proposal, not result):** Audit prior value under TF/gene-family and donor holdouts with annotation-version freezing. Compare expression-only, GO-only, sequence-only, full fusion, and degree-preserving shuffled graphs. The decisive endpoint should be held-out perturbation-response improvement and calibration, not recovery of familiar database edges.

### Program implication and exclusions

The useful gap is not another GAT/Transformer hybrid: it is reliably measured context, preservation of biological condition effects, and transport of intervention responses. match-seq offers a spatial-intervention measurement precedent; scHPGT offers a disease-signal-preservation design test; scMGFGRN provides overlapping architectural prior art. None establishes an eligible aging/AD dataset pair, project preliminary data, or a completed experiment. The September 21 strategy's premise/data audit remains the first dependency.

Older or unverified-date candidates were not used to fill the five-paper request: REN-former was first posted September 15; FOCST September 8; CIPHER June 4; the SCZ cilia CROP-seq preprint June 10. MitoSpace's September 20 news report was not substituted for verified paper-level publication metadata. MIRCID and other arXiv candidates did not have post-cutoff public availability verified in this run.

Persistence status: appended through obsidian_remember; no live read-back capability was available to independently verify the final note contents. Canonical project goals, datasets, tasks, and results were not changed.
