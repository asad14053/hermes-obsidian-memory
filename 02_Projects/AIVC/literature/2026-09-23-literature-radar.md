---
type: literature-radar
project: AIVC
run_date: 2026-09-23
previous_run: 2026-09-21T10:06:21
status: source-verified-abstract-level-triage
---

# AIVC Literature Radar — 2026-09-23

## Scope, provenance, and limitations

Five ranked papers, all first posted on bioRxiv September 22–23, 2026, after the previous run. Dates are server posting dates, not dates embedded in DOI strings. All are preprints, not peer-reviewed publications. Recommendations, weaknesses, and future ideas below are assessments; reported results are authors' claims. No quantitative improvement is asserted where the retrieved abstract supplies none.

Primary discovery sources: [bioRxiv bioinformatics interval API](https://api.biorxiv.org/details/biorxiv/2026-09-22/2026-09-23?category=bioinformatics) and [bioRxiv systems biology interval API](https://api.biorxiv.org/details/biorxiv/2026-09-21/2026-09-23?category=systems_biology). Targeted web and arXiv searches were also performed. One expanded arXiv API query returned an internal error; coverage is not exhaustive. Some bioRxiv/PDF requests timed out or returned only abstracts/opening pages. The selected records were verified in primary bioRxiv API metadata; this is NOT a full-paper methods/supplement audit.

Project comparison uses the user-supplied September 12 AIVC note contents recovered from session history and the September 19 NIA K99 review recalled in this run. Relevant notes: [[02_Projects/AIVC/overview]], [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/important-decisions]], [[02_Projects/AIVC/reviews/2026-09-19-NIA-K99-study-section-review]]. These describe graph-versus-transformer comparison, testable graph assumptions, unseen-perturbation generalization, spatial context, and unresolved aging/AD experimental premise. They do not establish a validated AIVC implementation. The September 12 SCZ focus and September 19 aging/AD proposal framing are distinct contexts, not evidence that the project officially changed disease focus.

Direct vault read/search tools were not exposed in this run. Deduplication used supplied recalled notes and session history, NOT a current vault-wide audit. Recovered September 21 recommendations were match-seq/Perturb-match, scHPGT, and scMGFGRN; none is repeated here. Session searches found no matches for the selected titles/identifiers, which is not proof of absence from the entire vault. This note is an additive literature assessment, not a modification of canonical project facts. Independent read-back of this note is unavailable with this run's tools.

## 1. DeepSCENIC — READ NOW

**Citation:** Partel, G.; De Winter, S.; Konstantakos, V.; Blaauw, C. H.; Aerts, S. (2026). *DeepSCENIC: transfer learning from sequence-to-function models enables causal gene regulatory network inference*. bioRxiv, v1, posted September 22, 2026. DOI: 10.64898/2026.09.18.752607.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.18.752607v1

**Evidence read:** Server metadata and abstract; PDF opening page. Full methods and numerical comparisons were not retrieved.

**Research problem:** Sequence-to-function models lack explicit cellular TF context; conventional GRN inference often lacks enhancer sequence grammar.

**Method:** Transfer pretrained Enformer/Borzoi representations into single-cell multiome modeling to connect TFs, regulatory elements, and target genes and simulate cis/trans perturbations. Aerts lab, VIB/KU Leuven.

**Key result, author-reported:** Enhancer–gene predictions improve over correlation baselines against CRISPRi screens; predicted melanoma knockdown effects agree with experimental time series. Mouse–human cortex analyses recover conserved TF programs, with top enhancers tested in reporter assays. No verified numerical effect size available in the retrieved material.

**What is new:** A sequence-informed, context-dependent regulatory framework that integrates enhancer grammar and trans-cellular state rather than treating biological topology as a generic fixed graph.

**Why it matters for AIVC:** Direct competitor/prior for the gene-expression + epigenetic-state design. Raises the novelty bar beyond adding a graph to a transformer; supplies a biologically anchored TF→enhancer→gene alternative to undirected coexpression priors.

**What is weak / unresolved:** The word causal in the title does not establish every inferred edge or arbitrary counterfactual. Reported cortex conservation is not evidence of successful SCZ/AD intervention prediction. Requires a leakage audit of pretrained sequence models, enhancer validation sets, donor splits, and perturbation supervision. Scope of these limitations is our assessment, not an asserted defect demonstrated by full-text review.

**Future research idea:** Compare a sequence-informed TF→enhancer→gene prior, a rewired prior, and a pure transformer under identical held-out-gene and held-out-donor evaluation; test whether spatial context adds independent value in neuronal systems.

## 2. SPECTRA — READ NOW

**Citation:** Calabrò, M.; Sheehan, P.; Cambuli, F.; Sottoriva, A. (2026). *SPECTRA: predicting cellular perturbation responses with Graph Learning over Gene Regulatory Networks*. bioRxiv, v1, posted September 22, 2026. DOI: 10.64898/2026.09.21.752624.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.21.752624v1

**Evidence read:** Server metadata/abstract and PDF opening page. Human Technopole; first author also Politecnico di Milano.

**Research problem:** Sparse genuine response genes and heterogeneous perturbation efficacy are difficult to recover with opaque latent-shift predictors.

**Method:** Encode control cells variationally; inject perturbations locally into a GRN and propagate them through a directed heterophilic GNN decoder. Node representations integrate expression, pretrained transcriptomic context, and prior regulatory topology. This is not established as a graph transformer by the retrieved source.

**Key result, author-reported:** Improved recovery of sparse perturbation effects on a large-scale CRISPRi benchmark, assessed with DEG precision, F1, and AUPRC; selected predicted effects checked against known orthogonal biology. Numerical gains and the exact held-out scheme remain unverified.

**What is new:** Explicit intervention-as-signal propagation on a directed regulatory network, rather than only a latent state displacement.

**Why it matters for AIVC:** Direct overlap with the biology + perturbation graph design. It should be a comparator before claiming architectural novelty for local perturbation injection or graph propagation.

**What is weak / unresolved:** The retrieved evidence describes one benchmark; it does not establish cross-donor, cross-cell-type, combination, or unseen-target generalization. A graph pathway that is readable is not automatically mechanistically correct. Check degree bias, graph provenance, DEG threshold sensitivity, and whether training/test perturbations contaminate the prior.

**Future research idea:** Run matched directed-graph, undirected-graph, degree-preserving-rewired, and pure-transformer models; evaluate unseen-target DEG AUPRC and effect direction with and without spatial neighborhoods.

## 3. Speciesformer — READ NOW, provisional pending benchmark audit

**Citation:** Wang, J.; Dong, J.; Li, G.; Fang, C.; Liu, L.; Gao, X. (2026). *Speciesformer learns conserved cellular states for cross-species generative virtual cell modeling*. bioRxiv, v1, posted September 23, 2026. DOI: 10.64898/2026.09.22.752128.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.22.752128v1

**Evidence read:** Primary bioRxiv API record and abstract. Direct landing-page and PDF retrieval timed out. Corresponding affiliation: KAUST.

**Research problem:** Distinguish transferable biological programs from species-, tissue-, and cell-context-specific variation while predicting cellular state transitions.

**Method:** Pretraining on SpeciesCorpus, reported as 131 million cells from 11 species, 154 tissues, and more than 923 cell types. Species-specific genes map into a shared evolution-informed space, coupled to a generative model conditioned on biological text and interventions.

**Key result, author-reported:** Cross-species representation transfer, bidirectional transcriptome/text generation, and post-perturbation prediction in previously unobserved cellular contexts. The abstract does not provide numerical benchmark gains, split definitions, or prospective validation.

**What is new:** A shared evolutionary representation joined to semantic generation and intervention-conditioned state transitions in one virtual-cell framework.

**Why it matters for AIVC:** Raises the bar for a generic multimodal or perturbation-conditioned transformer; offers a candidate baseline for mouse-to-human transfer relevant to disease model systems.

**What is weak / unresolved:** Scale is not proof of causal or OOD generalization. Need to audit atlas overlap, homolog leakage, intervention-text information leakage, and whether unseen context also means unseen target. No verified evidence here establishes SCZ/AD efficacy or superiority over simple baselines.

**Future research idea:** Freeze a cross-species encoder, add a small human-brain regulatory/spatial adapter, and test on held-out human neuronal perturbations against gene-orthology transfer and expression-only baselines.

## 4. Selective depletion of upper-layer SST interneurons in SCZ — READ NOW

**Citation:** Endresz, N.; Fafouti, M. E.; Arbabi, K.; Zhou, X.; DeLong, T.; Gonzalez-Burgos, G.; Duncan, L.; Sibille, E.; Tripathy, S. J. (2026). *Selective depletion of upper-layer somatostatin interneuron subtypes in schizophrenia*. bioRxiv, v1, posted September 22, 2026. DOI: 10.64898/2026.09.18.752621.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.18.752621v1

**Evidence read:** Primary API metadata and landing-page abstract. Corresponding affiliation: Centre for Addiction and Mental Health.

**Research problem:** Does reduced inhibitory/SST signal in SCZ reflect altered within-cell expression, depletion of specific subtypes, or both?

**Method:** Harmonize seven prefrontal postmortem snRNA-seq datasets to fine-grained cell taxonomy; meta-analyze abundance and expression; validate with spatial transcriptomics and examine genetic-risk enrichment.

**Key result, author-reported:** In 298 controls and 171 SCZ samples, SST expression decreases across the subclass while particular upper-layer SST subtypes are depleted and L6b excitatory abundance increases. Spatial confirmation uses 12 controls and 12 SCZ. Depleted SST subtypes enrich SCZ genetic risk, express HCN1, partially correspond to CALB1 double-bouquet cells, and overlap populations reported vulnerable early in AD.

**What is new:** Separates subclass-wide expression changes from finer subtype abundance changes, with spatial corroboration and a potential SCZ–AD vulnerability connection. Biological rather than new architecture contribution.

**Why it matters for AIVC:** Gives a concrete layer/subtype-aware prediction target and an important failure mode: a model can mistake altered composition for a perturbation response. The spatial cohort size resembles historical GeneBridge metadata, but size alone cannot establish dataset identity or independence.

**What is weak / unresolved:** Postmortem association cannot prove cell death, rescue, or a shared SCZ/AD causal mechanism. Check donor/accession overlap, annotation uncertainty, compositional effects, and diagnosis/medication/technical confounding before using it as external validation. This paper alone does not establish an NIA aging premise.

**Future research idea:** Jointly model upper-layer SST subtype abundance and within-subtype state, validate with measured spatial markers rather than imputed expression, and separately test intervention hypotheses in a matched experimental system.

## 5. mc-ASTRA — SAVE

**Citation:** Ramirez Flores, R. O.; Kruger Serrano, K. S.; Gaspar Vieira, F.; Vulliard, L.; Saez-Rodriguez, J. (2026). *mc-ASTRA maps population-level variation to interpretable multicellular tissue organization processes*. bioRxiv, v1, posted September 22, 2026. DOI: 10.64898/2026.09.18.752722.

**Source:** https://www.biorxiv.org/content/10.64898/2026.09.18.752722v1

**Evidence read:** Primary bioRxiv API record/abstract. Landing/full-text retrieval timed out. Corresponding affiliation: EMBL-EBI. Repository linked by authors: https://github.com/saezlab/mc-astra (not independently executed or inspected).

**Research problem:** Existing methods separate sample-level variation from interpretable multicellular/spatial processes.

**Method:** Combine flexible semi-supervised factor models with molecular, cell-composition, and spatial descriptors, sample-level technical/clinical covariates, and biological priors to construct interpretable tissue-state maps.

**Key result, author-reported:** Demonstrations across multiple single-cell and spatial datasets identify coordinated multicellular programs and describe tissue-remodeling trajectories. No numerical predictive superiority or intervention benchmark is established by the abstract.

**What is new:** An integrated sample-level framework connecting diverse tissue descriptors to interpretable multicellular programs; not a new perturbation foundation model.

**Why it matters for AIVC:** Useful lower-complexity baseline for the claim that spatial/multicellular context adds information beyond expression alone. It also keeps the donor/sample as the analysis unit instead of treating cells as independent replicates.

**What is weak / unresolved:** Combines existing models/tools; representation and interpretation are not causal response prediction. Supervision/biological priors may encode phenotype labels or confounding unless preprocessing and factor fitting are confined to training donors.

**Future research idea:** Derive tissue factors within training donors only, condition a perturbation predictor on them, and compare expression-only, composition-only, and spatial-context factors on held-out donors.

## Program-level implication — recommendation, not a project decision

The strongest novelty pressure comes from DeepSCENIC and SPECTRA; Speciesformer makes a generic foundation-model scaling pitch harder to distinguish. A sharper AIVC test is whether sequence-informed regulation and measured tissue context improve held-out intervention prediction beyond matched graph/pure-transformer and simple context baselines. Keep observational SCZ subtype vulnerability, aging/AD rationale, and experimental perturbation evidence separate. Freeze the prediction target, data provenance, leakage-safe folds, and negative controls before expanding architecture scope.

## Ranked IDs for downstream morning brief

1. DeepSCENIC — 10.64898/2026.09.18.752607v1 — READ NOW.
2. SPECTRA — 10.64898/2026.09.21.752624v1 — READ NOW.
3. Speciesformer — 10.64898/2026.09.22.752128v1 — READ NOW (provisional).
4. Selective depletion of upper-layer somatostatin interneuron subtypes in schizophrenia — 10.64898/2026.09.18.752621v1 — READ NOW.
5. mc-ASTRA — 10.64898/2026.09.18.752722v1 — SAVE.

Run-day brief: use ranks 1–2. Off-day brief: use ranks 3–5 with this run date and a stale notice. Do not silently renumber or repeat ranks 1–2 on off-days.
