# AIVC Literature Radar — 2026-10-09

## Scope and evidence

Window: after previous run 2026-10-07 10:06:12 UTC through this October 9 scheduled run. This shortlist contains three new bioRxiv v1 preprints posted October 8, one substantive October 8 revision (Mechanisms Matter v3), and one newly published PNAS article (LCD; publisher search result dates it October 8, issue October 13) whose preprint dates to January. Do not represent the revision or journal publication as first disclosure. All performance statements are author-reported, not reproduced.

Live vault read/search and terminal tools are not exposed in this run; tool discovery returned only session_search. Comparison uses actual Obsidian note text recovered from cron_d2277f698e9f_20261004_210004, message 6098. [[02_Projects/AIVC/methods]] (updated September 23), lines 11–17: identity + environment → universal representation → virtual instrument → activity. PDF specification: scGPT/UCE identity embedding, 20 μm cell-type-stratified distance-weighted neighbor expression, feature attention, prediction head, MSE plus sparsity. Accompanying diagram separately proposes multimodal inputs, hierarchical cross-attention, perturbation embedding and conditional VAE. These are distinct proposed specifications, not a verified merged implementation. [[02_Projects/AIVC/important-decisions]], lines 11–17, prioritizes held-out perturbation generalization and a frozen estimand/benchmark over architecture novelty. [[02_Projects/AIVC/todo-and-next-actions]], updated October 3, lines 19–29, requires simple baselines before architecture development and labels GeneBridge spatial reconstruction as engineering, not causal evidence.

Continuity: previous October 7 report recovered in session cron_b7fccc11fa73_20261007_100008, message 6979. None of its five papers (MERFISH screen, CardamomOT, VIMA, GP-DHT, STARIT) is repeated. Conversation-history search for Mechanisms Matter, Latent causal diffusions, VINTER, HyperCom and scStable returned no matches. This is not a current vault-wide duplicate audit.

Coverage: searched arXiv, bioRxiv and publisher sources, including current arXiv q-bio listings. arXiv API extraction failed on XML content type; listing extraction and web search were alternatives. Some full-text attempts failed with HTTP errors or rate limits. Source footer/PDF posting dates override erroneous extraction metadata that labels multiple bioRxiv entries January 1. No withdrawal notice appeared in the retrieved abstracts. Numerical gains not recoverable from reliable prose are omitted. No implementation, repository execution or citation-count audit was performed.

## 1. READ NOW — Mechanisms Matter: Transportability of Cellular Perturbation Effects

Citation: Qi S, Chapfuwa P. Mechanisms Matter: Transportability of Cellular Perturbation Effects. bioRxiv, v3, posted October 8, 2026. DOI 10.64898/2026.05.08.723625.
Source: https://www.biorxiv.org/content/10.64898/2026.05.08.723625v3
PDF: https://www.biorxiv.org/content/10.64898/2026.05.08.723625v3.full.pdf

Research problem: When can a perturbation response learned in one cell context transfer to another, and when do standard prediction metrics conceal failure?
Method: Causal transportability analysis; CAUSALDGP, a semi-synthetic simulator with context-specific regulatory mechanisms and baseline programs; response-diversity diagnostics based on Vendi score. Benchmarks six deep models and five simple baselines.
Key result: Cross-context performance often falls to simple-baseline levels; lower concordance of transcriptome-wide perturbation impact tracks worse transfer. Tested models fail under mechanism changes in the examined synthetic settings. This is not a theorem that transfer is universally impossible whenever any graph edge changes.
What is new: The explicitly documented v3 revision adds simulator validation, scLDM and STATE-Geneformer baselines, transcriptome-wide impact as a mechanistic-divergence proxy, and null-calibrated Vendi scoring. The original preprint is older.
Why it matters for AIVC: Similar identity embeddings or aligned expression distributions do not establish that a VI can transport effects across cell types, donors or disease states. Directly challenges a universal-representation transfer claim.
What is bad / limitations: The simulator uses linear stationary latent dynamics, negative-binomial observations and invariant emission across contexts; this deliberately controlled setting does not capture all biological or platform shifts. Real-data impact concordance is an empirical proxy, not proof of causal-mechanism identity. Estimating that proxy from held-out responses would leak outcomes; it is retrospective unless a permitted calibration set is specified.
Future research idea: Evaluate a context-aware VI against naive pooling and simple response baselines on held-out context × perturbation pairs. Use a prespecified calibration subset to estimate transfer reliability and abstain for unsupported contexts; never use scored test responses to choose the transfer gate.
Evidence: abstract and revision footnote; PDF pp. 1–4, sections 2.1–2.3. Proposition 1 makes direct transfer perturbation-specific, not a requirement that entire regulatory matrices be identical.

## 2. READ NOW — Latent causal diffusions for single-cell perturbation modeling

Citation: Lorch L, Zhang J, Bunne C, Krause A, Schölkopf B, Uhler C. Latent causal diffusions for single-cell perturbation modeling. PNAS (2026). DOI 10.1073/pnas.2602630123. Publisher search metadata reports October 8 online publication, October 13 issue.
Source: https://www.pnas.org/doi/10.1073/pnas.2602630123
Earlier preprint: arXiv:2601.15341v1, January 20, 2026, https://arxiv.org/abs/2601.15341v1 . Journal-versus-preprint changes were not exhaustively audited.

Research problem: Predict unseen combinations while separating measurement noise from biological variation and exposing gene-level regulatory mechanisms.
Method: Latent causal diffusion (LCD) represents gene regulation as stationary stochastic differential equations under a count measurement model. Perturbations shift a shared neural hidden state; combinations add perturbation embeddings. CLIPR linearizes the learned system through perturbation responses to estimate direct gene–gene effects.
Key result: Authors report improved prediction of distributional shifts for unseen perturbation combinations versus established approaches; CLIPR recovers ground-truth structures in simulations and interpretable modules in a genome-wide K562 screen. Its identification guarantee is under linear-drift assumptions, not unrestricted nonlinear biological causality. No unverified numerical gain is supplied.
What is new: Explicit regulatory dynamics, measurement-noise separation and perturbation-based causal linearization in a single predictive framework. Newly published journal version, not a newly invented October method.
Why it matters for AIVC: A substantive mechanistic comparator for the proposed graph-transformer/cVAE VI; clarifies the difference between an interpretable response-generating mechanism and an attention map.
What is bad / limitations: Assumes approximately steady-state measurements; model restricts how interventions enter hidden dynamics. Unseen combinations of learned interventions do not establish transfer to wholly unseen targets, donors or tissues. Stationary distributions alone do not universally identify arbitrary dynamics; causal claims depend on interventions and model assumptions. Reported modeling scale is around a thousand genes, not an unrestricted whole-cell simulation.
Future research idea: Compare LCD with additive, ridge and graph-transformer/cVAE heads on identical held-out combination folds in a neuronal perturbation dataset; test whether baseline spatial context adds predictive value without interpreting attention as causality.
Evidence: PNAS abstract; Results subsections A Causal Generative Model of the Transcriptome and Estimating Causal Dependencies in Stationary Diffusions; figure 1. Full publisher text was partly retrieved; date/author metadata corroborated via publisher search and original preprint.

## 3. READ NOW — VINTER: a generative vision-language model for annotating and interrogating spatial tissues

Citation: Wu J, Xu W, Zhuang Y, Zhang Y, Loza Lopez MDJ, Yang Y, Nakai K. VINTER: a generative vision-language model for annotating and interrogating spatial tissues. bioRxiv v1, posted October 8, 2026. DOI 10.64898/2026.10.01.752251.
Source: https://www.biorxiv.org/content/10.64898/2026.10.01.752251v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.01.752251v1.full.pdf

Research problem: Jointly read tissue morphology, focal expression and neighborhood evidence, then inspect which inputs support an annotation.
Method: UNI histopathology encoder plus LLaVA-1.5/Vicuna-7B; alignment on 1.45 million histology-caption pairs. Ranked gene-name lists separately encode focal and neighborhood expression. Dedicated class tokens yield class-support probabilities; gene-list edits hold images fixed. Methods use the top 20 focal and top 10 neighborhood genes within a fold-specific panel, averaging six nearest spots; expression magnitudes are not supplied.
Key result: Authors report stronger cortical-layer annotation than spatial-domain comparators, external breast-cancer transfer without target labels, and transfer to Visium HD/Xenium without retraining. Neighborhood-only edits expose programs affecting predicted TLS maturity. No fabricated accuracy percentage is quoted.
What is new: Editable focal/neighborhood molecular inputs in a multimodal generative decoder. This is unusually close conceptual overlap with AIVC's identity/environment separation, including DLPFC and Xenium relevance.
Why it matters for AIVC: A useful environment-representation comparator and a warning that neighborhood-conditioned predictions plus input editing alone are insufficient novelty or causal evidence.
What is bad / limitations: Input edits are explicitly not biological perturbations. DLPFC benchmarking holds out adjacent section pairs, while training includes the other pair from the same donor; 35% of held-out spots are used for checkpoint selection. It is therefore not a clean unseen-donor evaluation. Supervised class prediction against clustering methods is not a matched-supervision architecture comparison. Raw class probabilities are not cell fractions or automatically calibrated uncertainty; ranked lists discard expression magnitude.
Future research idea: Benchmark a small, numeric identity-plus-context model against VINTER-style ranked-token context under true donor-held-out folds and spatially separated validation. Then test whether neighborhood-edit predictions track measured receiver responses in an independent perturbation assay.
Evidence: PDF Methods subsections Model architecture and inputs, Model training, DLPFC benchmark, Class probabilities and input edits. The paper explicitly states that edits are to model input, not biological perturbations.

## 4. SAVE — HyperCom: a hypergraph-based method to infer cell-resolved cell-cell communication

Citation: Moy JK, Przytycki PF. HyperCom: a hypergraph-based method to infer cell-resolved cell-cell communication. bioRxiv v1, posted October 8, 2026. DOI 10.64898/2026.09.30.755742.
Source: https://www.biorxiv.org/content/10.64898/2026.09.30.755742v1

Research problem: Cell-type aggregation can obscure heterogeneous sender/receiver behavior within annotations.
Method: Hypergraph constructed from known ligand–receptor interactions and individual-cell expression; graph diffusion assigns continuous sender-to-receiver scores for each interaction and ranks interactions globally or by condition.
Key result: Abstract reports validation on physical-contact, spatial and multicondition datasets supporting cell-resolved communication inference. Numerical gains were not verified. Authors provide an R implementation, but repository execution was not tested.
What is new: Cell-type-agnostic hypergraph diffusion retaining individual-cell variation rather than only cell-type-averaged ligand–receptor scores.
Why it matters for AIVC: A biologically structured alternative to the current cell-type-stratified 20 μm neighborhood average and a comparator for learned attention.
What is bad / limitations: Expression plus a ligand–receptor database yields communication hypotheses, not verified signal transmission or causal effects. Database incompleteness, missing protein activity and targeted spatial-panel coverage can distort apparent edges. Cell-level scores do not replace donor-level replication. Full text could not be retrieved after HTML/PDF alternatives, so assessment remains abstract-level.
Future research idea: Add training-fold-only HyperCom-style context features to the same small response predictor and compare against pooled context, shuffled/rewired ligand–receptor graphs and no-context baselines; validate on measured non-autonomous responses, not expression correlation alone.
Evidence: official abstract and posting footer. Domain caveats cross-checked against the bioSkills spatial-communication guide retrieved at https://raw.githubusercontent.com/GPTomics/bioSkills/master/spatial-transcriptomics/spatial-communication/SKILL.md .

## 5. SAVE — scStable: assessing scRNA-seq analysis stability under bulk-derived between-sample variation

Citation: Jiang C, Li JJ. scStable: assessing scRNA-seq analysis stability under bulk-derived between-sample variation. bioRxiv v1, posted October 8, 2026. DOI 10.64898/2026.10.01.755876.
Source: https://www.biorxiv.org/content/10.64898/2026.10.01.755876v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.01.755876v1.full.pdf

Research problem: Single-sample or sparsely replicated single-cell studies cannot directly establish stability across biological samples.
Method: Learn between-sample variability from multi-sample bulk RNA-seq and inject it into a single-cell reference while retaining cell-level heterogeneity; generate synthetic samples for stability assessment.
Key result: In gastric-cancer data with 21 matched scRNA-seq/bulk profiles, authors report better reproduction of between-sample variation than ZINB-WaVE, subsampling or Gaussian noise. Demonstrates stability-based DE prioritization and clustering/hyperparameter choice.
What is new: Explicit use of external bulk-derived biological-sample variation rather than treating cell resampling as donor variation.
Why it matters for AIVC: Could stress-test whether representation or graph conclusions survive plausible donor variation, supporting statistical rigor in a K99 design.
What is bad / limitations: Bulk variation can reflect composition, disease or batch, and transferring it to cell-specific states requires assumptions. Synthetic donors are not independent biological replicates, prospective validation or a substitute for actual held-out donors. Full PDF extraction failed; official abstract and PDF-indexed introduction were available, so no detailed algorithm claim is inferred.
Future research idea: Use compatible external brain bulk data for a sensitivity analysis of AIVC graph-versus-no-graph rankings, then compare predicted stability against real held-out DLPFC donors. Keep synthetic results separate from biological validation and fit all reference transformations within training scope.
Evidence: official abstract/footer and PDF-indexed introduction.

## Research-program implication

The strongest opportunity is a calibrated, context-aware perturbation model with explicit limits on when effects transport. Novelty should be demonstrated through unseen-context performance and experimental response validation, not solely through graph/transformer labels or neighborhood input edits. VINTER especially makes a leakage-resistant donor-held-out comparison and measured perturbation endpoints important. These papers do not by themselves establish an aging/AD system or justify relabeling SCZ work for NIA.

## Persistence and scope

Submitted as a literature note to the canonical vault-relative path. Live independent read-back is unavailable in this run; the obsidian_remember acknowledgement is the only write confirmation. No canonical design, task status, owner, deadline or grant aim was changed.
