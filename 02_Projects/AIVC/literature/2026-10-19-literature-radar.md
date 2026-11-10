# AIVC Literature Radar — 2026-10-19

## Scope, continuity and verification

Target cutoff: previous run 2026-10-16 10:03:39 UTC (user-provided). This is a qualified five-paper shortlist, NOT five certified post-cutoff publications: SubcellPert and scMagnify were posted/published October 17; MOFI and Distributed AI Agents were posted October 16, with exact time unresolved; Causal Integrated Gradients was submitted October 15 but appears in the verified October 19 arXiv q-bio.QM new/cross-list announcements. Treat CIG as a newly listed catch-up, not a new post-cutoff submission.

Current primary pages were fetched. Assessments below distinguish author-reported results from agent criticism/proposed experiments. No code or results were independently reproduced. No withdrawal notices were visible on selected preprint pages. SubcellPert/scMagnify assessment is abstract-level; attempts to obtain full text returned abstract pages or failed. MOFI and distributed-agent PDFs yielded partial extracts, not complete methods. CIG HTML yielded introduction and Appendix L, with the middle omitted. Do not infer an exhaustive full-paper review.

Direct canonical vault read/search tools are unavailable in this run. Session history recovered a prior read of the October 16 radar (session cron_ff43f193a578_20261018_130039, message 10147), identifying stipple, SpatialZoomer, CellNet, TAKO and HSV-1 as the preceding selection. Those are not repeated. Session searches for all selected new titles/identifiers returned no matches; this is not vault-wide deduplication. Project comparison uses the October 19 weekly-strategy write payload recovered from session cron_952fb3b6f0a6_20261019_020009, message 10405, plus historical methods excerpts. These are historical records, not fresh reads of canonical notes. Independent read-back of this appended note is unavailable.

Current web searches covered virtual cells, perturbation prediction, spatial transcriptomics, single-cell transformers/graphs, multiomics and causal interpretation. arXiv API and bioRxiv API fetches failed; publisher pages and arXiv listings were used instead. One paginated arXiv recent page returned stale August content and was excluded; the q-bio.QM/new page explicitly showed October 19. Search-date filters were not trusted without page dates. This is incomplete retrieval coverage, not evidence that no other relevant papers exist.

## Project comparison

Recovered context: the PDF design proposes scGPT/UCE identity plus cell-type-stratified 20 μm environmental expression; a separate diagram proposes hierarchical attention, perturbation embeddings and a conditional VAE. They remain distinct proposed specifications. The October 19 strategy prioritizes an aging/AD premise-and-access decision, GeneBridge disease-effect preservation, and only then a nuisance-aware measured-target context-value pilot. It explicitly defers architecture expansion. No new literature result is an AIVC experimental result; none establishes SCZ or aging/AD intervention validity.

References: [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/current-state]], [[02_Projects/AIVC/literature/2026-10-16-literature-radar]], [[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]].

## 1. READ NOW — SubcellPert

**Citation:** Wang J, Cao H, Dang X, et al. SubcellPert: Benchmarking Subcellular Perturbation Prediction. bioRxiv v1, posted October 17, 2026. DOI: 10.64898/2026.10.11.758305. Not peer reviewed.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.11.758305v1
**Problem:** Gene-count prediction ignores perturbation-induced intracellular RNA localization.
**Method:** A benchmark of 14 imaging datasets, 13.88 million cells and 3.65 billion RNA molecules. Separately trained Oracle tasks predict 2D coordinates given exact target counts; Joint tasks predict counts and coordinates. Eight baselines include resampling, classical transport and frozen foundation-model adapters, with perturbation/context holdouts.
**Key result:** Authors report Gaussian transport gives the lowest Oracle spatial error on eight of eleven cellular-context OOD datasets. Better centroids can accompany worse radial distributions; 19 of 190 Joint adapter fits retain source counts after validation. [Primary abstract.]
**What is new:** Explicit separation of abundance and subcellular localization with audits that expose failure hidden by aggregate spatial accuracy.
**Why it matters for AIVC:** A direct benchmark challenge to the idea that a larger biological model is necessarily better. Xenium supports a future subcellular extension, but intracellular localization is not the same task as the proposed intercellular neighborhood encoder.
**What is weak / unresolved:** Oracle uses unavailable target counts and must not be presented as deployable end-to-end prediction. Normalized 2D geometry and measured gene panels constrain scope. Frozen adapters do not settle comparisons against well-trained specialized models. No SCZ/AD transfer is established by the abstract.
**Future idea:** After the current context-value pilot succeeds, compare nuisance-aware simple transport against a context-conditioned model on a measured-target Joint task, jointly evaluating count calibration, radial distributions and donor generalization. Audit cell geometry and composition rather than rewarding centroid accuracy alone.
**Decision:** READ NOW for benchmark design; do not expand this week's implementation scope.

## 2. READ NOW — scMagnify

**Citation:** Chen X, Yan X, Shen B, et al. Decomposing multi-scale dynamic regulation from single-cell multiomics with scMagnify. Nature Communications, published October 17, 2026. DOI: 10.1038/s41467-026-78441-9. Peer-reviewed early article.
**Source:** https://www.nature.com/articles/s41467-026-78441-9
**Problem:** Reconstructing time-lagged and combinatorial regulation from chromatin accessibility and expression.
**Method:** Deep learning with Granger-causality-based multi-scale GRN reconstruction; tensor decomposition extracts combinatorial TF modules and time-lag activation profiles; an intercellular communication module links signals to transcription.
**Key result:** Authors report recovery of known lineage regulators in human hematopoiesis and mouse pancreas, and signaling-to-transcription cascades associated with pathological epithelial changes in kidney injury. Numerical advantage was not available in the retrieved abstract. [Primary abstract.]
**What is new:** Connects multi-lag GRN decomposition, TF combinations and intercellular signaling rather than relying on a single static graph.
**Why it matters for AIVC:** Relevant competition for the biological environment-to-regulation story. A generic graph-attention layer is not enough to distinguish AIVC; added value must concern measured context-dependent response and transfer.
**What is weak / unresolved:** Granger predictability does not by itself identify intervention effects. Temporal ordering, omitted variables and inferred communication require scrutiny. Retrieved material does not establish unseen-perturbation prediction or neural disease transfer.
**Future idea:** Compare a static GRN prior with time-lagged TF-module priors on a genuinely time-resolved neural/glial perturbation dataset, testing measured responses in held-out biological units. Require a real temporal design before adopting the dynamic interpretation.
**Decision:** READ NOW for competitive positioning and GRN-prior design.

## 3. SAVE — MOFI

**Citation:** Shen J, Zhang Z, Peng H, et al. MOFI reveals dynamic multi-omics coordination during cell fate progression. bioRxiv v1, posted October 16, 2026. DOI: 10.64898/2026.10.09.757904. Not peer reviewed; cutoff-day timing unresolved.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.09.757904v1
**Problem:** Paired multiomics snapshots do not observe continuous trajectories of the same cells.
**Method:** A dynamically constrained integration framework jointly models modality-specific dynamics, cross-omics correspondence and shared population growth. The partially extracted PDF discusses optimal transport; detailed objectives and evaluation splits were not fully inspected.
**Key result:** Authors report reconstruction of RNA-ATAC nephron progression, perturbation-responsive hematopoietic lineage redistribution, and brain-organoid maturation/interneuron allocation. No quantitative superiority claim is made here. [Primary abstract; PDF pp. 2–4 partially extracted.]
**What is new:** Population growth and cross-modal dynamics are modeled jointly rather than treating multimodal integration as a static embedding problem.
**Why it matters for AIVC:** A useful comparator for the proposed conditional VAE/virtual-instrument branch and a neural-development dataset lead. It highlights the need to separate state change from population redistribution.
**What is weak / unresolved:** Requires paired, time-indexed modalities; current cross-sectional SCZ tissue is not equivalent. Matching marginals does not uniquely establish single-cell trajectories or causal effects. Neural-development demonstrations are not aging/AD validation.
**Future idea:** Test whether separating population growth/composition from within-cell state change improves prediction of context-by-perturbation effects in a replicated neural time course, against static multimodal and additive baselines.
**Decision:** SAVE until a suitable dataset and response estimand are fixed.

## 4. SAVE — Distributed biological reasoning

**Citation:** Sun A, Park JJ, DeTomaso D, et al. Distributed AI agents enable comprehensive discovery of biological insights at scale. bioRxiv v1, posted October 16, 2026. DOI: 10.64898/2026.10.15.759436. Not peer reviewed; cutoff-day timing unresolved.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.15.759436v1
**Problem:** Biological interpretation becomes a bottleneck in large perturbation atlases.
**Method:** Many perturbation-scoped agents analyze facets of a whole-brain Perturb-seq experiment, followed by cross-perturbation synthesis; evaluations include held-out effects and blinded expert assessment. Team includes Scripps/HHMI, OpenAI, PerturbAI and UCSD.
**Key result:** Authors report recovery of source-manuscript conclusions without giving agents the manuscript, prediction of held-out perturbation effects, and expert preference for distributed over single-agent interpretations. Thousands of agents ran in minutes; the months-of-human-analysis comparison is estimated, not a measured controlled human trial. [Primary abstract; partial PDF Results/Figs. 1, 3, 4.]
**What is new:** Perturbation-level decomposition and study-wide synthesis with blinded evaluation, rather than only a single conversational assistant.
**Why it matters for AIVC:** Potential downstream interpretation/prioritization layer for neural perturbation results—not a replacement for a predictive virtual cell. Could help nominate focused follow-up experiments once validated outputs exist.
**What is weak / unresolved:** Manuscript withholding alone does not rule out knowledge contamination. Expert preference is not prospective biological validation. Compute/cost matching and independent replication need review. Employment/founder conflicts involving OpenAI and PerturbAI are declared.
**Future idea:** Use a small, budget-matched, evidence-cited agent ensemble to rank experimentally testable SCZ perturbation hypotheses; evaluate prospectively against a single-agent system and a non-LLM enrichment baseline with hidden perturbation outcomes.
**Decision:** SAVE; no agent infrastructure build before the core AIVC baseline is established.

## 5. READ NOW — Causal Integrated Gradients (new listing / catch-up)

**Citation:** Michiels J, Ismail A, De Vos M, Sifrim A. Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths. arXiv:2610.22126v1, submitted October 15, 2026; included in October 19 q-bio.QM new cross-list announcements. Not peer reviewed in the inspected record. NOT a certified post-cutoff submission.
**Source:** https://arxiv.org/abs/2610.22126v1
**Inspected HTML:** https://arxiv.org/html/2610.22126v1
**Listing evidence:** https://arxiv.org/list/q-bio.QM/new (retrieved heading: Monday, 19 October 2026).
**Problem:** Standard attribution can rank downstream correlated targets above upstream transcription factors; graph-aware Shapley methods can be costly.
**Method:** Causal integrated/expected gradients route attribution paths using a supplied causal graph and deterministic surrogate, decomposing direct and descendant-mediated effects.
**Key result:** Authors report causal-Shapley-like accuracy at lower runtime on synthetic data and better TF prioritization on Dyngen and interferon-beta stimulation than graph-agnostic comparators. Appendix L documents systematic indirect-effect misallocation under non-additive mechanisms and substantial error when parent edges are omitted. [Abstract, Introduction, Appendix L/Table L.1.]
**What is new:** Graph-informed causal paths within scalable gradient attribution, distinct from merely using a graph inside the predictor.
**Why it matters for AIVC:** Provides a testable alternative to treating attention weights as mechanism. Relevant to the proposed biology/perturbation graph transformer, but interpretation is conditional on the supplied graph and surrogate.
**What is weak / unresolved:** It is not causal discovery. Incorrect or incomplete GRNs and non-additive regulation can distort mediated attribution even when overall rankings look good. Real interferon stimulation is not a complete TF-intervention ground truth.
**Future idea:** Benchmark attribution stability across alternative neural GRNs, edge dropout and held-out CRISPR regulators; test both regulator ranking and mediated-effect calibration rather than just prediction accuracy.
**Decision:** READ NOW for interpretation safeguards; listed separately as catch-up because submission predates the cutoff.

## Research-program implication

The most defensible opportunity is not another larger graph/transformer architecture. It is a carefully specified, nuisance-aware test of whether context changes a measured perturbation response, with strong simple baselines, explicit state-versus-composition separation and interpretation tested against intervention evidence. SubcellPert adds evaluation requirements; scMagnify raises the mechanistic competition; CIG warns that even graph-aware explanations depend on assumptions. These do not resolve the existing NIA premise/access gap.

## Follow-up / unresolved

Canonical vault-wide deduplication and independent read-back of this note remain blocked by absent read/search tools. No canonical project status, task priority or implementation claim was changed. CodaST was investigated but not selected: its publisher preview verifies the method/results but not a reliable within-window online-publication date. No five-post-cutoff claim should be made from this run.
