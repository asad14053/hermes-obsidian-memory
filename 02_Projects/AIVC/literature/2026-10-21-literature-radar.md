# AIVC Literature Radar — 2026-10-21

## Scope and evidence status

Cutoff: previous run 2026-10-19 10:06:18 UTC, as provided in the job. All selected papers have verified post-cutoff v1 submission/posting dates: Bolero October 20; Tessera October 20 17:32:57 UTC; VampPrior Unleashed October 19 21:40:49 UTC; HistoLoop October 20 15:05:54 UTC; SFABC October 19 13:22:08 UTC. Dates come from versioned arXiv abstract histories and Bolero's PDF footer, not DOI date strings or search-engine metadata. Bolero's extracted webpage incorrectly supplied January 1 metadata; the PDF explicitly says posted October 20, 2026. The Arc announcement agrees.

Results are author-reported, not independently reproduced. Versioned abstracts and PDF excerpts were inspected; PDF outputs omit their middles, so this is NOT a complete methods or benchmark audit. No withdrawal notice was visible on the selected abstract records. Tessera reports NeurIPS 2026 AI4DD workshop acceptance, not main-track acceptance. No journal acceptance was verified for the other selections.

Tools available in this run support web retrieval, session history and Obsidian append, but not direct vault search/read or terminal execution. A tool-discovery attempt returned only session_search. Therefore comparison uses recovered records of prior Obsidian notes, not fresh canonical reads. The October 19 radar was recovered from session cron_b7fccc11fa73_20261019_100042, message 10516 (write payload) and 10518 (final report). Its selection was SubcellPert, scMagnify, MOFI, Distributed biological reasoning and Causal Integrated Gradients; none is repeated here. Session search for Bolero, Tessera, VampPrior, HistoLoop, DGP-LA and Simulation-free approximate returned no matches. This is history-level deduplication, NOT verified vault-wide deduplication. Independent note read-back is unavailable; do not claim it was performed.

Search coverage: arXiv date-bounded single-cell/virtual-cell/spatial API query succeeded, returning six candidates; perturbation-specific API attempts failed twice. Web searches supplemented this with bioRxiv and publisher results. DGP-LA was investigated but excluded because PubMed dates publication October 12, before cutoff. REST was excluded because its arXiv submission timestamp precedes the cutoff. The result is the best matched shortlist among retrieved candidates, not an exhaustive census.

## Comparison to recovered AIVC notes

The recovered October 19 radar describes the proposed scGPT/UCE cell-identity encoder plus cell-type-stratified 20 μm environmental expression. A separate diagram proposes hierarchical attention, perturbation embeddings and a conditional VAE. These remain distinct proposed specifications, not a verified implemented model. Recovered October 19 strategy favors a nuisance-aware measured-target context-value pilot and defers architecture expansion. The October 19 faculty-intelligence record also says AD/aging is a future extension, not a replacement for canonical SCZ scope.

Tessera is the closest direct competitor to the identity-plus-environment representation. Bolero raises the bar for cell-state-conditioned regulation and neural biological specificity. VampPrior challenges whether a latent-prior improvement can achieve benefits attributed to a more elaborate encoder. HistoLoop supplies a recurrent-context comparator, not a perturbation simulator. SFABC supplies a mechanistic uncertainty alternative for small modules, not a genome-wide foundation model.

References: [[02_Projects/AIVC/methods]], [[02_Projects/AIVC/current-state]], [[02_Projects/AIVC/literature/2026-10-19-literature-radar]], [[09_Planning/weekly-strategies/2026-10-19-AIVC-GeneBridge-weekly-strategy]]. No canonical project facts or task priorities were modified.

## 1. READ NOW — Bolero

**Citation:** Liu H, Mao S, Gallent T, et al. Predicting cell-state-specific gene regulation from DNA across species. bioRxiv v1, posted October 20, 2026. DOI: 10.64898/2026.10.19.760026.
**Source:** https://www.biorxiv.org/content/10.64898/2026.10.19.760026v1
**PDF:** https://www.biorxiv.org/content/10.64898/2026.10.19.760026v1.full.pdf
**Additional primary institutional explanation:** https://arcinstitute.org/news/bolero
**Problem:** Sequence-to-function models commonly fix cell-state labels, whereas cell-state models lack DNA-level regulatory inputs; neither alone solves state-specific variant and response prediction.
**Method:** Sequence-to-function transformer conditioned on atlas-derived cell-state embeddings and additional biological variables. The Arc explanation describes dynamically generated additive weights at each transformer layer. AP-1 activity supplies a continuous conditioning axis. The paper reports training on 10.7 million cells, 33 datasets and six mammals.
**Key result:** Authors report matching/exceeding specialized models, resolving cortical regional/developmental gradients, extrapolating to absent cell states, and predicting activity-regulated accessibility without stimulation data for training. Predictions across 84 mammals suggest AP-1 responses are less conserved than baseline accessibility. These are predictive results, not an independently established causal law. [Abstract/PDF first page; Arc How Bolero Works.]
**What is new:** A state-conditioned sequence model joins DNA grammar, cellular identity and continuous activity rather than attaching a fixed categorical cell label.
**Why it matters for AIVC:** Directly raises the novelty bar for claiming cell-identity-conditioned regulation. Neural/cortical demonstrations and noncoding variant interpretation could connect SCZ genetics to a constrained AIVC hypothesis. However, Bolero's cellular state is not a measured spatial-neighborhood intervention.
**What is weak / unresolved:** AP-1 conditioning is narrower than general unseen CRISPR/drug-response prediction. Predictive changes under an activity score are not automatically identified intervention effects. The retrieved excerpts do not establish spatial-environment causality or SCZ efficacy. Full split, embedding-construction and variant-validation audits remain necessary. The Arc announcement uses a different draft title and 10.8-million dataset wording; use the actual preprint title and its 10.7-million training figure in citations.
**Future research idea (proposal, not result):** For SCZ-linked regulatory variants, compare sequence-plus-cell-state predictions with a neighborhood-conditioned extension; test whether neighborhood adds predictive value on measured neural stimulation responses in held-out donors, beyond state, cortical layer and composition. Start with one biologically justified pathway rather than a universal virtual cell.
**Decision:** READ NOW for mechanistic positioning and a genetics-to-cell-state bridge; no immediate architecture expansion implied.

## 2. READ NOW — Tessera

**Citation:** Dehghani Amirabad A, Khodabandeh Yalabadi A, Moskalev A, et al. Spatially Informed and Direction Sensitive Representation Learning for Spatial Transcriptomics. arXiv:2610.28579v1, October 20, 2026. Authors report acceptance at NeurIPS 2026 AI4DD workshop.
**Source:** https://arxiv.org/abs/2610.28579v1
**PDF:** https://arxiv.org/pdf/2610.28579v1
**Problem:** Distance-only neighborhoods lose directional organization, while absolute coordinates bind representations to arbitrary slide locations; conventional gene selection can miss spatially informative expression.
**Method:** Spatially informed gene ranking feeds a pretrained scRNA-seq foundation-model encoder. A geometry-aware spatial attention aggregator uses learned 2D rotary positional encoding; masked-cell expression reconstruction supplies training supervision. [PDF Introduction/Fig. 1.]
**Key result:** Authors report stronger representations on held-out tissues/technologies and zero-shot use of contexts up to 16× larger than training contexts. This is a context-size generalization claim, not a 16× accuracy gain. [Abstract.]
**What is new:** Joint spatially informed gene selection and translation-invariant, direction-sensitive relative-position attention.
**Why it matters for AIVC:** Closest new competition to the proposed cell-identity-plus-environment design. A frozen cell embedding plus spatial attention is no longer a sufficient novelty claim; the contribution needs a demonstrable response-prediction or generalization advantage.
**What is weak / unresolved:** Masked expression reconstruction does not establish perturbation prediction. Its appendix explicitly shows fixed learned direction fields are sensitive to rotating the tissue; translation invariance is not rotation invariance. The direction needs anatomical meaning or a controlled orientation protocol. Quantitative representation tables and leakage controls were not fully audited.
**Future research idea:** Compare the existing cell-type-stratified 20 μm neighborhood summary with distance-only attention and direction-aware attention in a donor-held-out measured-target pilot. Include slide rotations and laminar-axis normalization to distinguish anatomy from acquisition orientation. For a later intervention dataset, ask whether the geometry helps response prediction rather than only reconstruction.
**Decision:** READ NOW; prioritize as a competing baseline/design critique.

## 3. SAVE — VampPrior Unleashed

**Citation:** Stirn AA, Rajagopal A, Knowles DA, Huynh G. VampPrior Unleashed. arXiv:2610.27322v1, October 19, 2026.
**Source:** https://arxiv.org/abs/2610.27322v1
**PDF:** https://arxiv.org/pdf/2610.27322v1
**Problem:** VampPrior ties prior and posterior covariance parameters and assumes uniform mixture weights, constraining density fitting and cluster recovery.
**Method:** Decouple prior-component covariance from the encoder covariance, then replace uniform weights with a Dirichlet-process mixture. Applied as a prior replacement in scVI; no new graph or transformer is necessary. [Abstract/Introduction.]
**Key result:** Authors report improved model evidence, integration and clustering across six single-cell atlases. Appendix E explicitly documents donor–cell-type confounding and warns that batch mixing metrics may reward loss of biological structure. [Abstract/Introduction; Appendix E/Table 4.]
**What is new:** Changes the latent prior rather than adding encoder complexity, improving the evidence-versus-clustering tradeoff.
**Why it matters for AIVC:** Relevant to the separately proposed conditional-VAE branch and to strong probabilistic baselines. It challenges any claim that improved embeddings necessarily demonstrate better biological-context reasoning.
**What is weak / unresolved:** Integration/clustering and model evidence do not demonstrate unseen-perturbation prediction, calibrated response uncertainty or preservation of SCZ disease effects. Donor-biological confounding makes attractive mixed embeddings insufficient evidence of success. Extending the prior to a conditional response model is a proposed application, not a reported result here.
**Future research idea:** Hold architecture and training budget fixed while swapping standard Gaussian, mixture and unleashed priors; evaluate measured-target prediction, disease-effect preservation and response calibration in donor holdouts, not just scIB scores.
**Decision:** SAVE as a targeted low-complexity baseline; inspect before committing to a conditional VAE.

## 4. SAVE — HistoLoop

**Citation:** Liu Z, Liu J, Li S, Feng Y, Wang Q. HistoLoop: Iterative Contextual Inference with a Looped Transformer for Histology-Based Spatial Gene Expression Prediction. arXiv:2610.28339v1, October 20, 2026.
**Source:** https://arxiv.org/abs/2610.28339v1
**PDF:** https://arxiv.org/pdf/2610.28339v1
**Problem:** Spatial predictors often aggregate context without rebuilding that context from updated spot representations.
**Method:** Persistent spot states generate coarse-to-fine context tokens, a shared spatial transformer processes them, cross-attention retrieves contextual evidence, and memory-mediated updates feed the next refinement step. The appendix clarifies memory resets for each forward pass and is not carried between sections. [Introduction; Appendix C.]
**Key result:** Under HEST-Bench's predefined HVG50 protocol, reported macro gene-wise Pearson correlation is 0.480 versus 0.435 for MoLF, the strongest evaluated comparator, over six cancer-specific tasks spanning five organs and a five-seed protocol. Do not extrapolate this restricted benchmark to genome-wide accuracy. [PDF Introduction.]
**What is new:** State-dependent reconstruction of context between recurrent refinement steps, not simply multiscale inputs.
**Why it matters for AIVC:** Supplies a concrete alternative to the proposed one-pass hierarchical context encoder. A recurrent neural computation is not, however, a biological time-course model.
**What is weak / unresolved:** Cancer H&E-to-expression prediction on 50 genes is not neural perturbation prediction. Pearson correlation does not establish calibrated counts or preserved disease contrasts. Full patient-level splits, image-backbone exposure and compute matching remain audit items, not demonstrated defects.
**Future research idea:** Only after a basic context-value signal exists, test shared-weight recurrent context against one-pass attention at matched parameter/compute budgets, evaluating measured neural genes in held-out donors and keeping recurrence separate from claims about biological dynamics.
**Decision:** SAVE; useful architecture comparator, lower immediate priority than Tessera/Bolero.

## 5. SAVE — Simulation-free approximate Bayesian computation (SFABC)

**Citation:** Li Z, Barahona M, Thomas P. Simulation-free approximate Bayesian computation for stochastic reaction networks. arXiv:2610.26361v1, submitted October 19, 2026; PDF internally dated October 20.
**Source:** https://arxiv.org/abs/2610.26361v1
**PDF:** https://arxiv.org/pdf/2610.26361v1
**Problem:** Inferring stochastic reaction-network parameters through approximate Bayesian computation commonly requires costly repeated Gillespie simulation.
**Method:** Chemical Master Equation constraints define convex feasibility/optimization tests for whether proposed kinetic parameters are compatible with observations, avoiding trajectory simulations and explicit likelihood solutions. The authors prove posterior convergence under specified limiting conditions, including zero tolerances. [Abstract/Introduction.]
**Key result:** Reported synthetic benchmarks match simulation-based inference accuracy at lower computational cost; experimental applications infer transcriptional bursting from snapshot, time-resolved and cell-cycle-resolved single-cell measurements. No unverified numerical speedup is quoted. [Abstract/Introduction.]
**What is new:** Mechanistic, simulation-free Bayesian inference with a systematically refinable approximation, rather than amortizing simulations with another neural surrogate.
**Why it matters for AIVC:** A distinct methodological opportunity: a small, uncertainty-aware mechanistic component can complement learned representations and support more specific causal hypotheses than a generic graph model.
**What is weak / unresolved:** Depends on the reaction-model specification; inference of its parameters is not discovery of arbitrary genome-wide networks. Convergence in limiting settings does not guarantee practical finite-budget calibration. Snapshot data do not generally identify absolute kinetic timescales; temporal measurements are a separate evidence requirement. Large-network scalability is not established by the inspected excerpts.
**Future research idea:** For a single validated neural response module, compare a kinetic Bayesian model with a learned response model on held-out time-course measurements, testing interval coverage and parameter identifiability before attempting any genome-wide hybrid.
**Decision:** SAVE for a later mechanistic methods direction; not this week's foundation-model implementation.

## Program implication and next action

Read Bolero and Tessera first. The more defensible publication/K99 question is whether spatial environment adds reproducible predictive information about a measured response beyond cell identity, regulatory sequence and nuisance covariates—not whether a GNN/transformer can be assembled. These papers motivate discriminating baselines and falsifiable tests; they do not establish the user's preliminary data, aging relevance, or feasibility of a full virtual cell.

No deadlines or obligations are inferred from these papers. Proposed experiments have no assigned owner/due date. The bioSkills machine-learning/model-validation guide was retrieved as reference and informed grouped-split/leakage caution: https://raw.githubusercontent.com/GPTomics/bioSkills/main/machine-learning/model-validation/SKILL.md . No pipelines, repositories, diagrams or external tasks were created. Next verification gap: fresh canonical AIVC-note comparison, vault-wide duplicate check and independent read-back of this literature note when vault read tools are restored.
