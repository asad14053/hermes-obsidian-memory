# AIVC Literature Radar — 2026-10-14

## Scope and evidence quality

Previous run: 2026-10-12 10:06:20 UTC, as supplied in this job and recovered from session cron_b7fccc11fa73_20261012_100032. This selection covers October 12–13 publications/postings. October 12 publisher dates have no release time, so their being strictly later than the previous run is unverified. Temporal Attention is a newly journal-published update of an earlier arXiv preprint, not a new October invention. No selected retrieved abstract contained a withdrawal notice. All reported results are author claims, not independently reproduced.

Live web searches covered virtual cells, perturbation prediction, single-cell transformers, spatial biology and neurodevelopmental foundation models. The arXiv date-filtered API could not be extracted (unexpected content type); web searches substituted. Coverage is not a complete census. BioMod full-method extraction failed/truncated; SPACER is subscription-limited. PULSE and the two PLOS PDFs yielded substantial text with page/section provenance, but not exhaustive supplements. No experiments or repositories were executed/audited.

No live vault read/search tool is exposed in this run: tool discovery returned only session_search. Comparison therefore uses recovered note payloads, not a live vault-wide audit. The October 12 literature note payload (session cron_b7fccc11fa73_20261012_100032, message 8539) records the proposed identity + environment → representation → virtual instrument design and cell-type-stratified neighborhoods. The October 12 weekly plan (session cron_952fb3b6f0a6_20261012_020051, message 8456) prioritizes an aging/AD premise/access COMMIT/NO-GO decision, GeneBridge measured-versus-imputed SCZ effect concordance/null calibration, and an optional donor-held-out measured-target context-value pilot. These are recovered records, not verified current implementation status.

None of the October 12 selections (CEE, RNA fingerprinting, DEPICT, CellMAPP/CHART, CosMx point-process study) is repeated. Two assistant-history searches using selected titles, method names and DOI suffixes returned no matches. This does not prove absence from current vault notes or earlier differently titled versions.

Related: [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/important-decisions]], [[02_Projects/AIVC/literature/2026-10-12-literature-radar]], [[09_Planning/weekly-strategies/2026-10-12-AIVC-GeneBridge-weekly-strategy]].

## 1. READ NOW — BioMod

Citation: Meng L, Zhu J, Han B, et al. BioMod: Biological Module Tokenization for Single-Cell Foundation Modeling. bioRxiv v1, posted October 13, 2026. DOI: 10.64898/2026.10.12.758490.
Source: https://www.biorxiv.org/content/10.64898/2026.10.12.758490v1
PDF: https://www.biorxiv.org/content/10.64898/2026.10.12.758490v1.full.pdf
Evidence: official abstract and posting footer; PDF p. 1 confirms authors, model size and date. HTML .full returned abstract/metadata rather than full methods.

Research problem: Gene-by-gene tokenization forces models to infer higher-order biological organization from sparse expression and increases sequence length.
Method: 660 overlapping biological-module tokens built from curated pathways and data-driven gene programs; high-ratio masked-module pretraining with an asymmetric decoder. A 50-million-parameter model pretrained on approximately 73 million human cells.
Key result: Authors claim state-of-the-art results across annotation, zero-shot batch integration, perturbation-response prediction and drug-response forecasting, with single-GPU inference. Exact effect sizes and evaluation splits could not be audited; do not treat the ranking as independently verified.
What is new: Intermediate biological modules between genes and cells are the representational unit, rather than simply adding graph edges to gene tokens.
Why it matters for AIVC: A direct comparator for biological-prior-guided representation learning. A generic claim that pathways/GRNs plus a transformer improve biological interpretability is insufficient differentiation. Test what spatial context adds beyond module compression.
What is bad / limitations: Preprint; abstract-level performance evidence in this review. Donor/target holdout, pretraining overlap, module-construction leakage, baseline fairness and code/checkpoint availability remain unaudited. Module compression could suppress within-pathway or rare-gene responses; this is a testable concern, not a demonstrated failure. Single-GPU inference does not imply inexpensive pretraining.
Future research idea: Compare gene tokens, fixed pathway summaries and learned module tokens under identical target/donor holdouts, then add cell-type-stratified spatial context. Score both gene-level response directions and pathway-level recovery. Fit learned modules using training data only; include matched shuffled-context controls and strong low-rank baselines.

## 2. READ NOW — SPACER

Citation: Yao J, Shim JS, Wong K, et al. Interpretable AI model reveals spatial codes of cell recruitment in tissues. Nature Biomedical Engineering, published October 13, 2026. DOI: 10.1038/s41551-026-01804-6.
Source: https://www.nature.com/articles/s41551-026-01804-6
Evidence: publisher abstract/date recovered via the publisher's cookie-query URL; Data availability and extended figure captions from the main page. Full main methods are subscription-limited. Institutional news provides corroboration, not independent replication: https://medicalxpress.com/news/2026-10-ai-tool-reveals-immune-cells.html

Research problem: Spatial maps show where cells reside but do not directly identify molecular features associated with recruitment/engagement.
Method: Interpretable multi-instance learning over spatially resolved transcriptomics, learning gene-level recruitment rules from local cellular organization. Do not mislabel it as a graph transformer.
Key result: Across 37 SRT datasets spanning human tumors and mouse heart, authors report 4–21-fold improvements in tasks recovering biologically meaningful recruitment signals. They identify mucin-associated barriers to T-cell engagement and local antigen presentation as a dominant correlate. This fold range spans different tasks; it is not a universal accuracy gain.
What is new: A recruitment-centered, interpretable tissue-context formulation instead of spatial clustering or pairwise ligand–receptor scoring alone.
Why it matters for AIVC: A concrete context-model baseline for the environment branch. Neighborhoods and interpretable gene scores alone are not sufficient novelty; demonstrate added value for predicting measured responses in new donors and interventions.
What is bad / limitations: Recruitment associations are not automatically causal intervention rules or a dynamic cell simulator. Cancer/heart evidence does not establish brain/SCZ transfer. Exact task metrics and splits remain unaudited. The paper links gastric CosMx data to Zenodo 10.5281/zenodo.21267094, but the retrieved Zenodo record labels files restricted; do not assume immediate access. Other listed public data include GEO GSE300147, GSE298932 and GSE299032, but downloads were not tested.
Future research idea: Compare interpretable multi-instance neighborhood summaries with graph attention in neural/glial data, evaluated on donor-held-out measured perturbations. Use cell-type/composition-matched shuffled neighborhoods to test whether local context contributes beyond composition; causal claims require actual intervention evidence.

## 3. READ NOW — Sparse neuronal C4 elevation

Citation: Sánchez-Carbonell M, Bolshakova S, Ávila-Pagán JE, et al. Sparse neuronal C4 elevation induces network-wide transcriptomic and lipid-droplet remodeling in the cortical microenvironment. PLOS Computational Biology 22(10):e1014871. Published October 12, 2026. DOI: 10.1371/journal.pcbi.1014871.
Source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014871
PDF: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1014871&type=printable
Evidence: PDF pp. 1–3 abstract/introduction, p. 4 model description, p. 11 spatial quantification. It is an experimental disease-mechanism paper, not a novel ML architecture.

Research problem: Can focal elevation of a schizophrenia-linked complement gene reshape the surrounding cortical microenvironment?
Method: Sparse mouse C4 overexpression in approximately 2% of prefrontal cortical neurons, bulk RNA-seq, projection onto a cortical single-cell reference, and MFISH/PLIN2 imaging.
Key result: Broad lipid/cholesterol, synaptic, vascular and immune/stress transcriptional changes; increased Hmgcr in neighboring GFP-negative cells and increased local lipid-droplet burden support a non-cell-autonomous component. Global correspondence with human SCZ synaptic proteomics is limited, despite selective gene/pathway overlap.
What is new: Evidence linking sparse neuronal C4 perturbation to neighboring-cell lipid-associated responses, extending beyond a synapse-elimination-only interpretation.
Why it matters for AIVC: A particularly relevant biological motivation for separating directly perturbed sender cells from unperturbed receivers in the environment branch. This is more specific to the user's SCZ/cortical program than generic tumor benchmarks.
What is bad / limitations: Mouse developmental overexpression is not human C4A variation or adult DLPFC schizophrenia. Bulk RNA-seq/reference projection does not measure cell-type-specific perturbation effects directly. GFP-negative neighbors are not automatically astrocytes or microglia; nuclear-centered imaging ROIs also warrant care. It is not a ready-made whole-transcriptome single-cell spatial perturbation benchmark. The paper states code/count matrices will be available at https://github.com/Cruz-Martin-Lab/C4-OE-CorticalRNAseq ; repository release was not independently checked.
Future research idea: In a feasible human neuron–glia co-culture, predict receiver lipid-response programs conditional on sender C4 perturbation and neighborhood composition, with independent donor and imaging validation. First establish measured-data/experimental access; do not assume this study supplies all training data.

## 4. SAVE — PULSE

Citation: Schweiger HE, Robbins A, Hernandez S, et al. A foundation model for brain organoid network dynamics uncovers intrinsic computation and convergent disease phenotypes. bioRxiv v1, posted October 13, 2026. DOI: 10.64898/2026.10.11.758231.
Source: https://www.biorxiv.org/content/10.64898/2026.10.11.758231v1
PDF: https://biorxiv.org/content/10.64898/2026.10.11.758231v1.full.pdf
Evidence: PDF pp. 1–5, Summary and Results, especially lines 94–154. UCSC-led with collaborators including Jubao Duan, Alex Pollen and Aparna Bhaduri; affiliations verified on title page.

Research problem: Hand-selected spike statistics and task-specific decoders make functional neural phenotypes hard to compare across genotypes and protocols.
Method: Population Unified Latent Space Embedding (PULSE), a roughly 12-million-parameter Mamba-2 state-space model with autoregressive next-20-ms spike prediction, stimulation conditioning and a common latent representation. Developed using over 900 hours of HD-MEA recordings; human organoids were held out of pretraining. It is not a transformer and not an RNA foundation model.
Key result: Detects accelerated maturation in held-out 16p11.2-deletion organoids and a network-coordination change shared with SHANK3 deficiency. The reference forecasting model beat an exponentially weighted moving-average baseline on correlation in held-out mouse cultures, but not on bits/spike or skill. This qualification is explicit in Results and should accompany the positive findings.
What is new: A common functional coordinate system for comparing neural circuits across genetic perturbations, preparation protocols and stimulation tasks.
Why it matters for AIVC: Suggests a future functional output beyond expression reconstruction, aligned with a neurobiology-focused faculty program. It does not demonstrate that RNA predictions imply functional rescue.
What is bad / limitations: Small human line diversity; repeated recordings/organoids are not independent donors. The 16p11.2 deletion and control lines are not described as an isogenic pair in the retrieved Results, unlike the SHANK3 comparison. Correlation gains alone do not establish calibrated unseen-culture forecasting. Paired RNA–electrophysiology access is unverified.
Future research idea: With matched perturbation/RNA/MEA data, test whether predicted transcriptional program changes forecast held-out functional network phenotypes. Require donor- and organoid-level splits and functional calibration, not just latent separation. Save for a later validation arm rather than expanding this week's pilot.

## 5. SAVE — Temporal attention for cell fate

Citation: Bürger F, Dias Gomes M, Granada AE, Moreau N, Bozek K. Understanding cell fate decisions with temporal attention. PLOS Computational Biology 22(10):e1014813. Published October 12, 2026. DOI: 10.1371/journal.pcbi.1014813.
Source: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014813
PDF: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1014813&type=printable
Earlier preprint: https://arxiv.org/abs/2603.16562v1
Evidence: journal PDF pp. 1–8, §§2.1–2.4 and 3.1; attention masking analysis pp. 11–12. The journal says up to 8 hours before an event; the older preprint search excerpt says 10 hours. Use the journal's 8-hour claim, not a blended version. Full revision history was not audited.

Research problem: Can dynamic morphology and molecular-reporter activity predict divergent cell fates under chemotherapy?
Method: ResNet50 frame embeddings, temporal Transformer and attention/masking analyses on tracked live-cell imaging with p53, circadian and cell-cycle reporters. Main task is apoptosis versus mitosis.
Key result: Balanced accuracy 0.94 and F1 approximately 0.93 on held-out trajectories; morphology-feature baseline balanced accuracy 0.90. Temporal truncation supports predictive signal up to 8 hours before events. This does not mean the 0.94 score holds at every horizon.
What is new: New journal publication of an existing model, with useful temporal truncation and attention-faithfulness diagnostics; not a new October foundation architecture.
Why it matters for AIVC: A model-audit pattern for dynamic virtual instruments: ask when prediction becomes informative and verify whether removing purportedly important inputs degrades prediction.
What is bad / limitations: §2.4 explicitly uses random cell-trajectory splitting, not experiment/donor-held-out evaluation; shared-video/lineage dependence is a leakage risk, not proven contamination. Event-conditioned trajectories and fate-dependent sequence lengths may provide shortcuts. Post-treatment observations are not pretreatment counterfactual response predictions. Attention masking supports model reliance, not causal biological mechanisms.
Future research idea: Build fixed-horizon, predeclared-window outcome prediction with video/donor/lineage holdouts and length-only plus morphology baselines. Test whether temporal and spatial context add independent value; assess time-to-event modeling rather than interpreting absence of an observed event as survival.

## Research-program implication

BioMod is the immediate architectural comparator; SPACER is the environment-model comparator; sparse C4 elevation supplies the clearest SCZ-linked sender/receiver motivation. The defensible differentiator remains measured, context-dependent intervention response under donor/target shift, not simply adding biological priors or interpretable attention. PULSE and Temporal Attention are future functional/temporal extensions, not reasons to expand the current scope. No selected paper establishes an aging/AD premise for the K99 automatically.

## Persistence and remaining gaps

Submitted through obsidian_remember to this canonical vault-relative path. The write tool's response is the only persistence confirmation available: independent read-back cannot be performed with the exposed tools. No canonical design facts, deadlines, task tracker, GitHub state or implementation were changed. Live vault comparison, exhaustive prior-version deduplication, BioMod benchmark audit, SPACER full methods and code/data execution remain incomplete.
