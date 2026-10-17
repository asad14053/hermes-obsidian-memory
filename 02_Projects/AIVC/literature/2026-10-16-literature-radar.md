# AIVC Literature Radar — 2026-10-16

## Scope and verification limits

Target window: since the supplied previous run, 2026-10-14 10:05:37 UTC, through this scheduled run. Five selected papers below have primary-source publication/posting dates of October 14–15. Exact publication times for the October 14 journal articles were unavailable, so those are boundary-day candidates, not certified post-cutoff arrivals. Rankings and research ideas are agent assessments; published results are author-reported, not independently reproduced.

Tools in this run expose web search/extraction, session history and Obsidian append, but no vault search/read, filesystem or execution tools. Direct comparison against the current canonical AIVC notes and independent read-back of this note cannot be completed. Session-history searches for the selected titles/identifiers found no matches; this does NOT certify vault-wide deduplication. The supplied prior output contains a truncated prompt rather than the previous paper list. An attempted lookup of the apparent prior session ID did not resolve. Do not label these definitively unreported until the literature index can be read.

Project comparison uses the historical September 23 note-update payload recovered from session cron_b7fccc11fa73_20260921_100029, message 3664: identity + environment -> universal representation -> virtual instrument -> activity. The PDF specifies scGPT/UCE identity embedding and 20 μm cell-type-stratified distance-weighted neighborhoods; the separate diagram proposes multi-scale hierarchical cross-attention, perturbation embeddings, conditional VAE and confidence-weighted imputation. These remain distinct proposed specifications, not implemented results. References: [[02_Projects/AIVC/project-outline]], [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/current-state]]. Current canonical status was not freshly read.

Search covered virtual cells, perturbation prediction, graph/transformer single-cell models and spatial transcriptomics using current web results and arXiv recent listings. The arXiv Atom endpoint failed extraction with CRAWL_UNEXPECTED_CONTENT_TYPE; primary HTML/PDF retrieval provided the fallback. No withdrawal notices were seen on selected preprint pages. Full texts were partially extracted for stipple, CellNet, TAKO and the HSV-1 study; SpatialZoomer assessment is limited to the publisher abstract, figure descriptions, data/code availability and bibliographic record. No citation-count or code-execution verification was performed.

## 1. READ NOW — stipple: biological versus technical spatial variation

**Citation:** Jackson KC, Gorin G, Pachter L. Biological and technical spatial variation in spatial transcriptomics. bioRxiv, version 1, posted October 15, 2026. DOI: 10.64898/2026.10.13.758896. Preprint, not peer reviewed.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.13.758896v1
**Full text:** https://www.biorxiv.org/content/10.64898/2026.10.13.758896v1.full.pdf

**Research problem:** Spatial gene patterns can arise from cell/domain identity, local biology or spatially varying measurement efficiency. An environment encoder can inadvertently learn the last of these.

**Method / novelty:** stipple couples a bursty-transcription negative-binomial observation model to a smooth spatial capture field. Domain-aware residual analysis distinguishes domain-variable genes, shared-field-aligned patterns and residual spatially variable genes. This is a generative measurement model rather than treating every spatial correlation as biological.

**Key result:** In simulations, conditioning on the fitted field separated field-independent spatial variation from technical-field-aligned signals more effectively than the tested library-size normalization/regression workflows. The real-data analysis includes the Maynard human DLPFC Visium dataset. [PDF pp. 2–4, Results; Fig. 2.]

**Why it matters:** Directly challenges the interpretation of the AIVC environment branch and imputed spatial inputs. A spatial prediction gain is not evidence of microenvironmental causation if capture gradients explain it.

**What is bad / limitations:** Absolute capture efficiency is not identifiable from counts alone; the model anchors its scale using assumptions. Domain annotations and within-domain assumptions influence separation. Do not equate a residual spatial pattern with a causal cell-cell interaction, or transfer a Visium capture model to Xenium without validation. [PDF pp. 8–9, Estimation of Average Capture Probability.]

**Future research idea:** Add an explicit assay-specific nuisance branch and compare biological-neighborhood prediction before/after nuisance adjustment on donor-held-out DLPFC data, validating retained spatial signals against an independent assay. This is a proposed experiment, not an adopted architecture change.

## 2. READ NOW — SpatialZoomer

**Citation:** Li X, Fan Y, Han Y, et al. SpatialZoomer: multi-scale feature analysis of spatial transcriptomics. Nature Biomedical Engineering (2026), published October 14. DOI: 10.1038/s41551-026-01800-w. Boundary-day candidate; time of publication unresolved.

**Source:** https://www.nature.com/articles/s41551-026-01800-w

**Research problem:** Relevant spatial information occurs at cell, niche and tissue-domain scales; a fixed neighborhood can miss it.

**Method / novelty:** Spectral graph low-pass filters extract multi-scale molecular features; partitioning a cross-scale similarity map identifies critical scales automatically.

**Key result:** Authors report scale-specific Alzheimer's disease progression signals, spatial-context-dependent tumor cell subtypes and comparable or superior single-scale benchmark performance with low computational requirements. No numerical advantage is asserted here because the full results were not available. [Publisher abstract; Figs. 1–6.]

**Why it matters:** A strong, relatively simple comparator for both the fixed 20 μm PDF design and the diagram's hierarchical neighborhood attention. Merely adding multiple scales is unlikely to establish AIVC methodological novelty.

**What is bad / limitations:** Feature extraction and observational disease associations do not establish interventional prediction. Smoothing could mix identities or preserve technical gradients; these are audit concerns, not demonstrated failures. Subscription access limits the current review.

**Future research idea:** Compare fixed-radius aggregation, SpatialZoomer features and learned multi-scale attention under identical donor-held-out folds; require the learned model to improve an independently measured response endpoint, not only clustering.

## 3. READ NOW — CellNet

**Citation:** Lian X, Liu P, Tan J, Tan L, Li C, Zou Q, Lin C, Zeng X. Panoramic modelling of single-cell transcriptomes at scale with CellNet. arXiv:2610.21943v1, submitted October 15, 2026. Preprint.

**Source:** https://arxiv.org/abs/2610.21943v1
**Full text:** https://arxiv.org/html/2610.21943v1

**Research problem:** Fixed gene vocabularies and gene-token costs limit coverage, particularly non-coding transcripts and cross-species expression prediction.

**Method / novelty:** Evo 2 DNA-derived gene features define species-specific expression-image layouts; a DINOv3 backbone performs multiview latent learning with a gene-conditioned expression decoder. Pretraining covers 231 million cell profiles from 40 species. Its image layout is a computational gene layout, NOT physical tissue space. [Sections 2.1–2.2.]

**Key result:** In the reported donor-held-out Tabula Sapiens evaluation, tissue-equally weighted Macro-F1 is 0.621 versus 0.589 for the strongest comparison pipeline, TranscriptFormer. For withheld coding targets detected in at least 20% of cells, mean gene-wise PCC is 0.365 in PBMCs and 0.241 in developing brain. [Sections 2.2, 2.4.]

**Why it matters:** A concrete alternative for AIVC's identity encoder and GeneBridge-related missing-gene inputs; it broadens non-coding coverage rather than merely increasing model size.

**What is bad / limitations:** Expression recovery and condition recognition do not demonstrate unseen-intervention prediction. Cross-species transfer is task dependent; some animal tasks favor UCE/TranscriptFormer. Positive-cell intensity correlations are not interchangeable with all-cell correlations. Pretraining overlap, reference adaptation and target selection need independent audit. [Sections 2.2–2.5.]

**Future research idea:** Freeze CellNet as one identity-encoder arm against scGPT/UCE, keep environment and response heads fixed, and test donor-held-out neural perturbation prediction with observed-only versus imputed inputs.

## 4. SAVE — TAKO

**Citation:** Wang H, Oba K. Topology-adjusted knockout (TAKO): interpretable in silico single-gene knockout ranking on wild-type single-cell gene regulatory networks. Frontiers in Bioinformatics 6:1924703 (2026), published October 14. DOI: 10.3389/fbinf.2026.1924703. Boundary-day candidate.

**Source:** https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2026.1924703/full
**PDF:** https://www.frontiersin.org/journals/bioinformatics/articles/10.3389/fbinf.2026.1924703/pdf

**Research problem:** Prioritize genes affected by a knockout when only wild-type transcriptomes are available.

**Method / novelty:** Infer a directed network, convert it into non-negative transition dynamics, remove incoming/outgoing edges of the knockout node and compare wild-type versus modified stationary propagation under the same restart distribution. Training-free topological sensitivity, not a full post-KO expression generator. [PDF pp. 2–3.]

**Key result:** Mixed global performance versus absolute Pearson correlation in SERGIO and measured Trem2/Nkx2-1 KO evaluations; more measured DE genes appear among the top-ranked targets in both real examples. The authors explicitly do not claim general response-prediction superiority. [Abstract; Results.]

**Why it matters:** A cheap topology baseline against which a biology-informed graph transformer must demonstrate added value. It also separates network sensitivity from causal expression prediction.

**What is bad / limitations:** Non-negative transitions discard regulatory sign; the score does not predict expression-change direction. Real-data validation covers two KO targets, with cell-level DE labels explicitly described as descriptive rather than replicate-aware causal inference. Structural-edge recovery in SERGIO is not full-response validation. [PDF pp. 3, 11–12.]

**Future research idea:** Benchmark signed, context-conditioned graph priors against TAKO and correlation under unseen-target splits, using replicate-aware perturbation endpoints and reporting response magnitude, direction and ranking separately.

## 5. SAVE — HSV-1 multimodal microglial remodeling

**Citation:** Frietze S, Lunn C, Oldham D, Boyd JR, Bubak AN, Saucedo AB, et al. Intranasal HSV-1 infection drives region-specific interferon-dominant microglial remodeling. PLoS Pathogens 22(10):e1014684 (2026), published October 14. DOI: 10.1371/journal.ppat.1014684. Publisher currently labels this an uncorrected proof. Boundary-day candidate.

**Source:** https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1014684

**Research problem:** Determine how a biological exposure changes regulatory state in spatially restricted brain environments.

**Method / novelty:** Mouse infection-versus-mock study combines paired snRNA/snATAC profiling with spatial transcriptomics and proteomics in a separate cohort. Selected for perturbation-plus-spatial evidence, not a novel ML architecture. [Results: Single-cell multiome and spatial transcriptomic profiling; Fig. 1.]

**Key result:** IFN-responsive microglial/macrophage states and STAT/IRF-associated programs coincide with viral-antigen-positive brainstem regions. It provides an experimentally altered environment, but not direct validation of each inferred regulatory edge. [Abstract; Results.]

**Why it matters:** A candidate exploratory test case for separating identity from local environment, and an example of multimodal validation requirements for the AIVC proposal. It does not establish schizophrenia relevance or human DLPFC transfer.

**What is bad / limitations:** Spatial data comprise one animal per condition; multiple ROIs are not independent animal replicates. Whole-brain multiome and brainstem spatial measurements come from separate cohorts, not the same cells. Thus this is unsuitable as the sole confirmatory benchmark or as evidence of general causal GRN recovery. [Fig. 1 caption explicitly states animal-level sample size and cohort separation.]

**Future research idea:** Pilot prediction of regional IFN response using identity plus local context, then design independently replicated, matched spatial/perturbation sampling before claiming generalization. For K99 planning, treat this as exploratory evidence only.

**Data provenance:** Publisher lists GSE324176 for GeoMx WTA and GSE324144 for single-cell multiome; repository availability was not independently checked.

## Selection and next-action summary

Read order: stipple -> SpatialZoomer -> CellNet. Their joint implication is to separate assay effects from neighborhood biology, use a simple multi-scale comparator, and treat foundation-model encoding as a replaceable component rather than the claimed innovation. TAKO supplies a transparent graph baseline. The HSV-1 study supplies a biological validation example with substantial replication limitations.

Excluded from this new-publication list after date verification: arXiv:2610.18880v1 is dated October 1 despite appearing in a later cross-list; arXiv:2610.19029v1 is dated October 13. Do not relabel a cross-list or recent discovery as a new submission. No tasks, architecture decisions or canonical project-state notes were changed.

Persistence status: this note is submitted through the Obsidian append tool. Independent read-back is unavailable in this session; any claim of a verified vault-wide literature-index update would be unsupported.
