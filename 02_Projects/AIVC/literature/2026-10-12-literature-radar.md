# AIVC Literature Radar — 2026-10-12

## Scope, continuity and limitations

Search window: previous run 2026-10-09 10:05:05 UTC through this October 12 scheduled run. Selected papers were posted October 9–11, or newly journal-published October 9. Exact within-day release times for October 9 bioRxiv/Cell items were unavailable: these are same-day boundary candidates, not proven post-10:05 releases. RNA fingerprinting is a journal-publication update of a 2025 preprint, not a newly invented method.

Current searches used arXiv API, bioRxiv date/category API and publisher/institutional sources. Some API pages and PDFs were truncated or failed; results are a ranked selection from retrieved literature, not a complete publication census. No retrieved selected abstract contained a withdrawal notice. Numerical results are author-reported, not reproduced. Full methods were not recovered for CEE, DEPICT, CellMAPP/CHART or the CosMx study; limitations below distinguish study scope from reviewer concerns. No code execution or repository audit was possible.

Live Obsidian search/read and terminal tools are not exposed in this run; discovery returned only session_search. Deduplication used conversation history, including the actual October 9 radar note payload (session cron_b7fccc11fa73_20261009_100015, message 7476). None of that run's five selections is repeated. Searches for RNA fingerprinting and the exact DOI suffixes 756157, 757470, 756019, 752923 returned no prior assistant matches. This does NOT prove absence from all current vault notes.

Design comparison uses the October 9 radar's sourced AIVC-methods synopsis and the October 12 weekly-strategy note payload recovered in session cron_952fb3b6f0a6_20261012_020051, message 8454. The proposed identity + environment → representation → virtual instrument framework includes cell-type-stratified neighborhood features; graph/transformer/cVAE expansions remain proposals, not established results. The newest recovered weekly strategy prioritizes a bounded aging/AD premise/access decision, GeneBridge disease-effect validation, and an optional donor-held-out measured-target context-value baseline before architecture expansion. These literature recommendations do not change those priorities, canonical project facts, or the SCZ-centered disease focus.

Reference notes: [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/important-decisions]], [[02_Projects/AIVC/literature/2026-10-09-literature-radar]], [[09_Planning/weekly-strategies/2026-10-12-AIVC-GeneBridge-weekly-strategy]].

## 1. READ NOW — Cause-excluded Effect Evaluation

Citation: Hu J, Qi X, Tian L, Yan J, Liu N, Li X. Cause-excluded Effect Evaluation: a framework for the faithful assessment of genetic perturbation target identification. bioRxiv v1, posted October 11, 2026. DOI: 10.64898/2026.10.03.752923.
Source: https://www.biorxiv.org/content/10.64898/2026.10.03.752923v1
Metadata and abstract verified through: https://api.biorxiv.org/details/biorxiv/2026-10-11/2026-10-12/0/json?category=bioinformatics . Direct abstract/full HTML/PDF requests failed or timed out.

Research problem: Inverse perturbation target identification can appear accurate because cells exposed to test perturbations were included during fitting or because the target gene's own expression change reveals its identity.
Method: CEE separates train/test perturbation targets, removes target-gene self-effects and evaluates candidate targets in downstream response space.
Key result: Authors report that simple structure-based methods consistently outperform complex deep models across 16 single-cell perturbation datasets; recoverable signal is associated with low-rank and additive response structure.
What is new: An evaluation framework isolating downstream response information from direct target-expression clues, rather than another larger predictor.
Why it matters for AIVC: Directly tests whether a target-selection or desired-state module has learned response biology rather than target identity. Supports the current baseline-first strategy and raises the bar for graph/transformer novelty.
What is bad / limits: This is an inverse-target-identification benchmark, not proof that deep models cannot improve forward prediction, combinations or donor transfer. Full methods, exact comparators, mask construction and deployment assumptions could not be audited. Target removal can discard legitimate direct effects; it defines a harder downstream-only estimand rather than universally replacing full-response evaluation.
Future idea: Develop a neuronal target-ranking benchmark with held-out perturbations and donors, reporting both full-response and downstream-only scores. Compare low-rank/additive baselines with the same graph and transformer models. Ensure masking does not itself encode target identity and keep final-test responses out of fitting/tuning.
Evidence: official bioRxiv API abstract and metadata only.

## 2. READ NOW — RNA fingerprinting

Citation: Grabski IN, Lee J, Blair JD, Dalgarno C, Mascio I, Bradu A, Knowles DA, Satija R. Mapping transcriptional responses to cellular perturbation dictionaries with RNA fingerprinting. Cell (2026), publication announced October 9 by NYGC. Publisher identifier S0092-8674(26)01119-0.
Source: https://www.cell.com/cell/abstract/S0092-8674(26)01119-0
Publication/results confirmation: https://www.nygenome.org/news-events/news/rna-fingerprinting-helps-scientists-trace-what-drives-changes-inside-cells/
Earlier version read: https://www.biorxiv.org/content/10.1101/2025.09.19.676866v1.full . Its v1 appeared in September 2025. Journal full text was blocked; journal-versus-preprint changes were not exhaustively compared.

Research problem: Link observed cellular responses to plausible upstream perturbations while retaining uncertainty among perturbations with similar effects.
Method: Multi-condition latent factor model estimates denoised reference fingerprints; Bayesian regression maps queries to one or more fingerprints and summarizes ambiguity using credible sets.
Key result: NYGC reports identification of BCR from drug-response matches to genome-wide perturbation references; dose-dependent broad HDAC effects for putatively HDAC6-selective drugs; experimental follow-up supporting RPL10/RPL24 involvement in p53 responses to ribosomal stress.
What is new: Newly journal-published, not a new October method. The methodological contribution is uncertainty-aware perturbation-dictionary matching at cellular resolution, including ambiguous and combined explanations.
Why it matters for AIVC: A concrete inverse-response baseline and uncertainty layer for target nomination, connecting the user's statistical-genetics background to virtual-cell methodology. Compare against it before claiming target discovery from attention maps or latent proximity.
What is bad / limits: Dictionary incompleteness and cell-context mismatch restrict interpretations. A credible set reflects the statistical model and available candidates; matching an observational SCZ signature to an experimental fingerprint does not establish the cause of SCZ or therapeutic benefit. The Cell publication date is confirmed institutionally, not through accessible publisher metadata.
Future idea: Create context-conditioned credible sets for neural/glial perturbation candidates, with explicit no-match/abstention behavior. Test their coverage and ranking under donor/context shift using measured perturbations, then assess robustness under a CEE-style downstream-only diagnostic. CEE does not itself establish a flaw in this paper.
Evidence: preprint Introduction, Results opening/figure 1; NYGC publication announcement sections on drugs, p53 and immune responses.

## 3. READ NOW — DEPICT

Citation: Ma S, Yan S, Wen X, et al. DEPICT enables sample-centric therapeutic prioritization across evolving and spatially heterogeneous tumor states. bioRxiv v1, posted October 9, 2026. DOI: 10.64898/2026.10.07.756157.
Source: https://www.biorxiv.org/content/10.64898/2026.10.07.756157v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.07.756157v1.full.pdf

Research problem: Rank interventions within a biological context rather than merely predict isolated drug–sample responses.
Method: Sample-centric deep learning integrates transcriptomic and mutational features with prior alteration–therapy relationships. Trained on 231,880 cell-line–drug pairs spanning 941 cancer cell lines and 289 compounds.
Key result: Authors report transfer without retraining to independent cell lines, induced resistant states, and primary lung tumors/organoids. Spatial predictions of regional therapeutic heterogeneity were recapitulated in matched multiregional organoid drug-response assays.
What is new: A within-sample prioritization formulation plus a spatial-to-functional experimental validation chain, rather than spatial visualization alone.
Why it matters for AIVC: Useful precedent for connecting a context-aware virtual instrument to an experimentally measured decision endpoint. It makes a clearer grant validation story than reconstruction accuracy alone.
What is bad / limits: Cancer viability/response ranking is not transcriptome-wide perturbation simulation or neural/SCZ transfer. Organoids may not preserve the original tissue microenvironment. Full split design, donor counts, ranking loss and quantitative gains were not recovered; these are verification items, not established flaws. Do not infer causal neighborhood effects from the reported spatial associations.
Future idea: After a neural/glial perturbation system is secured, compare within-donor intervention rankings from identity-only and context-aware models; validate a prespecified small set with independent functional assays. Keep dose/time and donor splits fixed.
Evidence: official abstract and posting footer; PDF title/author page confirms date, but extraction stopped near the abstract.

## 4. SAVE — CellMAPP / CHART

Citation: Coelho PP, Leote AC, Yao H, et al. Archetype analysis of multiplexed antibody imaging reveals interpretable morphological programs in optical pooled screens. bioRxiv v1, posted October 9, 2026. DOI: 10.64898/2026.10.07.757470. Genentech-led; senior authors include Singh, Marioni and Regev.
Source: https://www.biorxiv.org/content/10.64898/2026.10.07.757470v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.07.757470v1.full.pdf

Research problem: Determine which imaging channels add useful perturbation information and convert opaque morphology features into interpretable biological readouts.
Method: CellMAPP combines optical pooled screens and iterative antibody imaging; CHART uses marker-specific archetypes, multimodal-LLM annotations and integrated morphological programs. Demonstration: 17 markers and 524 genetic perturbations in MCF-7 cells.
Key result: Authors report broader perturbation-hit recovery with multiplexing, but some phenotypes are better recovered using selected feature subsets rather than all features. Cross-marker programs expose coordinated organelle changes and regulators of phenotypes such as micronuclei.
What is new: Interpretable marker-wise morphological programs and an empirical audit of complementary versus diluting modalities.
Why it matters for AIVC: A possible future virtual-instrument output beyond RNA. Challenges the assumption that adding every modality or channel necessarily improves useful perturbation information.
What is bad / limits: Main demonstration is an MCF-7 cancer-cell system, not neuronal tissue. MLLM labels are not independent mechanistic validation, and readable archetypes do not establish causal GRNs. No paired RNA–imaging training resource or donor-generalization result was verified here.
Future idea: Once suitable paired measurements exist, predict held-out perturbation effects on marker-specific morphology programs alongside RNA; require multimodal gains over RNA-only and imaging-only baselines, with training-only channel selection. This is a future direction, not a reason to expand architecture this week.
Evidence: official abstract and PDF page 1, including date and authors.

## 5. READ NOW — Patient-specific limits of spatial inference

Citation: Carcanholo FP, Cassiano MHA, Panepucci EM, Laurini MP, Malta TM. Point-Process Modelling of Cell-Type Interaction Structure in CosMx Glioma Data for Hypothesis-Driven Tumor Inference from scRNA-seq. bioRxiv v1, posted October 10, 2026. DOI: 10.64898/2026.10.02.756019.
Source: https://www.biorxiv.org/content/10.64898/2026.10.02.756019v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.02.756019v1.full.pdf

Research problem: Can molecular state recover spatial context after tissue dissociation, and does this relation transfer across patients?
Method: Fine-mesh log-Gaussian Cox process models derive conditional spatial intensity and tumor-proximity phenotypes from CosMx; transcript abundance or pathway features predict those phenotypes. Dataset comprises eight GBM specimens and 2,427,362 cells.
Key result: Transcriptomic predictors outperformed metabolic pathway scores, but leave-one-patient-out evaluation reduced performance, and patient-wise harmonization did not restore cross-patient transportability.
What is new: A spatial-statistical context representation with a directly relevant negative transfer result—not a graph-transformer claim.
Why it matters for AIVC: Direct warning for transferring environment representations or inferred spatial context from GeneBridge: many cells cannot substitute for independent donors, and alignment alone may not repair patient-specific molecular–spatial relationships.
What is bad / limits: Small biological cohort, GBM rather than SCZ, and observational proximity rather than measured signaling or intervention effects. External nonspatial score stratification cannot by itself validate reconstructed spatial truth. Full effect-size and pipeline-leakage audit remains unavailable.
Future idea: In the existing donor-held-out AIVC context-value pilot, stratify gains by architecture shift and compare simple neighborhood summaries with a point-process context representation only after the baseline passes. Report transport failure and abstention rather than hiding it through pooled cell-level metrics.
Evidence: official abstract and posting footer; PDF first page. Extractor metadata falsely said January 1; official footer/API/PDF consistently show October 10 and take precedence.

## Research-program implication

The near-term opportunity is not another architecture diagram: establish downstream-response generalization and uncertainty under donor/context shift, then connect predictions to an independent functional assay. CEE + RNA fingerprinting provide complementary evaluation and inference ideas; DEPICT provides a validation pattern. CHART is a future multimodal extension. None supplies an aging/AD premise or SCZ causal evidence automatically.

## Persistence status

This note was submitted through obsidian_remember to the canonical vault-relative path. Independent read-back is unavailable because no current-vault read tool is exposed; do not describe persistence as independently verified. No task, deadline, canonical design or research result was altered.
