---
type: literature-radar
project: AIVC
run_date: 2026-09-30
previous_run: 2026-09-28T10:05:48
status: primary-source-triage-partial-coverage
---

# AIVC Literature Radar — 2026-09-30

## Scope and evidence boundaries

Five ranked papers follow. Target window: after the supplied previous run, September 28 at 10:05:48 UTC. DRIFT was submitted September 28 at 13:12:33 UTC (verified on export.arxiv.org/abs/2609.35106). LangPatch was submitted September 29 (arXiv search metadata and versioned HTML header). BioPert and SpatialTRACE were posted September 29 (explicit bioRxiv posting text, not their DOI date strings). CancerZigZag was submitted September 29 at 14:54:14 UTC (export.arxiv.org/abs/2609.37735). These are preprints; results below are author-reported, not independently reproduced. No withdrawal notice appeared in the retrieved abstracts. No citation counts or unverified journal acceptance claims are used.

Coverage limits: arXiv API extraction failed with unsupported XML content type. Category listings were inconsistently stale, including September 21/28 and a May listing from the export host. Search results and extraction sometimes omitted most of a page or returned only an abstract at a PDF URL; retries via HTML, PDF and export.arxiv.org recovered the evidence specified below, not a complete systematic review. BioPert PDF yielded actual page-labelled text on one retrieval; a later larger-budget retry returned only sparse passages, not the omitted middle. A complete split/code audit was not possible. No terminal, filesystem read/search, or live Obsidian lookup tool is exposed in this run.

## Comparison with existing AIVC notes and deduplication

Project comparison is history-based, not a fresh vault read. Recovered the actual September 28 radar write payload and final report from session cron_b7fccc11fa73_20260928_100005, messages 4710–4712. That note preserved the September 23 design: identity + environment → universal representation (UR) → virtual instrument (VI) → cell-type-specific activity; identity-matched environment swaps; 20 μm cell-type-stratified neighborhoods, attention, MSE plus sparsity. A companion diagram separately proposes multiscale hierarchical cross-attention, Xenium/snRNA-seq/Visium/Perturb-seq integration, confidence-weighted imputation, perturbation embeddings, conditional VAE and donor-held-out tests. These remain proposals, not completed experiments. Neither source is assumed to supersede the other.

The September 28 weekly strategy recovered from session history prioritizes a context-value audit against identity-only and pooled-neighborhood baselines, measured held-out targets, and donor-held-out evaluation. Its aging/AD grant feasibility recommendations do not establish a user-approved shift away from SCZ/DLPFC.

Previously recommended Pop-Corn, PerturbBridge and SpaCEy are not repeated. The prior note also identifies September 25 recommendations CellAudit, DePass, SpaFactor, Hou et al. and PRAXIS. Exact-name/identifier searches of assistant/tool session history found no previous reports of DRIFT, P2P, LangPatch, SpatialTRACE or BioPert. CancerZigZag is dated after the prior run. Live vault-wide duplicate checking remains unverified.

This is an additive literature note, not an update to canonical project facts. The writing tool can acknowledge the write, but an independent exact-target read-back is unavailable; persistence is not independently verified.

## 1. BioPert — READ NOW

**Citation:** Kaufmann, L., Le Breton, L., Carraz-Billat, E., Fournier, Q., & Lemieux, S. (2026). *A biological-response compound representation allows chemical perturbation prediction across cell lines*. bioRxiv v1. Posted September 29, 2026. DOI: 10.64898/2026.09.28.755146.

**Source URL:** https://www.biorxiv.org/content/10.64898/2026.09.28.755146v1

**Evidence:** Abstract; PDF pp. 1–3 and Methods 4.5 passages retrieved from https://www.biorxiv.org/content/biorxiv/early/2026/09/29/2026.09.28.755146.full.pdf ; posting corroborated by https://api.crossref.org/works/10.64898/2026.09.28.755146 .

**Metadata conflict:** The PDF lists Kaufmann then Le Breton and marks both as equal contributors; the bioRxiv article-info page lists Le Breton then Kaufmann. Citation above follows the PDF actually read. Generic extractor metadata saying January 1 conflicts with explicit September 29 posting text and Crossref; the generic date is discarded.

**Research problem:** How to encode drugs for predicting context-dependent transcriptional response when chemical similarity is a poor proxy for biological effects.

**Method:** Concatenate the target cell line's mean untreated expression with a matched drug-response delta profile measured in a reference cell line; fit a small MLP to target delta expression. The reference signature embeds dose/time effects. Comparators include molecular fingerprints, structure-derived foundation-model embeddings, random vectors and copying the reference response. This is population-mean response prediction, not a generated distribution of individual counterfactual cells.

**Key result:** Reports Pearson correlation 0.79 on Tahoe-100M, an improvement of 0.34 over the next-best representation, and only 0.15 on LINCS. It outperforms copying the reference response; a C32/cobimetinib example recovers pathway changes differing in direction from the reference. The large dataset difference is linked by the authors to reproducibility/batch effects. These are reported benchmark summaries, not universal accuracy guarantees or independently verified donor/compound double-holdout performance.

**Why it matters for your AIVC:** A direct challenge to making graph-versus-transformer architecture the central novelty. A measured perturbation representation plus a simple model may be a stronger baseline than a large model with weak inputs. Your proposed identity-plus-environment factorization should be compared with a simple baseline using target identity and a measured reference response before adding graph attention.

**What is new:** Uses experimental response signatures as transferable chemical-perturbation representations and isolates representation quality with simple downstream models.

**What is bad / limitation assessment:** Needs an experimentally measured signature for each compound and matched dose/time; not assay-free discovery of never-profiled drugs. Chemical-only methods receive less experimental information, so the result should not be framed as architecture superiority. LINCS performance is modest. Full split auditing, new-donor/neural transfer, prospective validation and SCZ relevance remain unverified here.

**Future research idea — proposal:** Test reference-response-conditioned AIVC with a factorial baseline panel: target identity alone; identity + chemical features; identity + reference response; and identity + reference response + measured neighborhood context. Hold out target donors/contexts and separately perturbations, and report exactly what reference experiments remain available at inference. Test whether context improves delta-expression and an orthogonal phenotype beyond the reference-response MLP.

## 2. LangPatch — READ NOW

**Citation:** Shen, J., Gao, J., & Lei, B. (2026). *Language as the Interface: Foundation-Model Contrastive Learning Links Transcriptomes and Electrophysiology*. arXiv:2609.37024v1, September 29.

**Source URL:** https://arxiv.org/abs/2609.37024v1

**Evidence:** Versioned abstract/HTML, plus indexed full-text passages from https://arxiv.org/html/2609.37024 describing results and transfer. Whole-paper extraction was incomplete.

**Research problem:** Link neuronal transcriptomic state to functional electrophysiological measurements with limited paired Patch-seq data.

**Method:** A shared frozen text encoder embeds gene descriptions and verbalized electrophysiological records. GenePT representations are adapted and aligned with electrophysiology using lightweight projections and paired contrastive learning. The indexed text describes a training-cohort-conditioned adapter; this is not a spatial-neighborhood encoder.

**Key result:** Reports best mean transcriptome-to-electrophysiology correlation among the evaluated foundation-model/representation-learning methods across mouse visual cortex, mouse motor cortex and human cortex. Cross-modal alignment FOSCTTM is 0.107/0.135 versus JAMIE's 0.208/0.222 in the two mouse cohorts (lower is better). Mouse-to-human transfer retains 47% of in-domain correlation, or 58% on acute-slice recordings. Retention is not absolute correlation. Indexed text also reports 44% retention for a plain GenePT MLP, an important modest-margin baseline comparison.

**Why it matters for your AIVC:** Gives a concrete functional endpoint for UR → VI rather than equating expression reconstruction with neuronal activity. Relevant to a brain-focused program and a future K99 validation strategy, but not itself schizophrenia or perturbation evidence.

**What is new:** A common language-embedding interface connects molecular descriptions and measured electrophysiological features with relatively lightweight paired alignment, rather than simply scaling transcriptomic pretraining.

**What is bad / limitation assessment:** Observational paired prediction does not establish perturbation causality or tissue-environment effects. Human transfer remains attenuated. Indexed text notes that only the proposed adapter uses training-cell labels, so equal-supervision baselines are necessary before attributing all gains to language alignment. Donor-held-out rigor and complete split construction were not independently audited.

**Future research idea — proposal:** Validate a constrained AIVC functional head against measured Patch-seq physiology, comparing it with ridge/MLP, cell-subclass means, and frozen GenePT under identical donor/lab splits. Only then test context or perturbation conditioning in a dataset that actually measures those factors; current GeneBridge data cannot be assumed to contain paired electrophysiology.

## 3. DRIFT — READ NOW

**Citation:** Bounoua, M., Franzese, G., & Michiardi, P. (2026). *DRIFT: Disentangled Responsive-Invariant Flow Transport for Single-Cell Perturbation Prediction*. arXiv:2609.35106v1. Submitted September 28, 13:12:33 UTC.

**Source URL:** https://arxiv.org/abs/2609.35106v1

**Evidence:** Abstract and selective HTML passages at https://arxiv.org/html/2609.35106v1 ; exact metadata at https://export.arxiv.org/abs/2609.35106 . PDF attempts did not recover a complete PDF text.

**Research problem:** Predict unpaired perturbation responses without transporting intrinsic cell-to-cell variation as though it were an intervention effect.

**Method:** A variational encoder separates invariant and responsive latent blocks through conditional priors and an information-theoretic invariance constraint. Conditional flow matching transports only the responsive block, conditioned on the perturbation and invariant state. Retrieved appendix passages describe biological perturbation features and an MSE decoder.

**Key result:** Authors report outperforming the strongest published comparator in combinatorial and unseen-perturbation settings. An extracted table omitted its column headings; numerical entries from that fragment are not assigned metrics or quoted as verified effect sizes.

**Why it matters for your AIVC:** Closely overlaps the proposed fixed-identity/changing-environment logic and offers a direct alternative to the conditional-VAE/MSE head. It makes the assumption that a latent component is truly invariant explicit and therefore testable.

**What is new:** Combines constrained invariant/responsive decomposition with flexible transport restricted to the responsive subspace, rather than relying on a prescribed latent shift or graph edit.

**What is bad / limitation assessment:** An invariance regularizer does not identify true biological invariants or a causal counterfactual mapping from unpaired data. Perturbations can genuinely change identity; suppressing such changes can be a modeling error. Appendix text says evaluation uses '1000 test-selected genes' and some baselines are reported from prior work. Audit gene-selection rules and common preprocessing before interpreting superiority; test-selected evaluation panels are not automatically training leakage. Spatial, neural and prospective generalization are not established by reviewed evidence.

**Future research idea — proposal:** Compare full-latent and responsive-only transport with a simple conditional head under identical donor/perturbation splits. Include identity-changing perturbations and test whether an adaptive invariant block preserves real transitions better than unconditional fixed-identity constraints.

## 4. SpatialTRACE — SAVE

**Citation:** Monell, A. T., Gogate, A. A., Patravali, D., Abadie, K., Yeo, G. W., Goldrath, A. W., & Heeg, M. (2026). *SpatialTRACE predicts anatomical axes and regions in spatial transcriptomics and microscopy*. bioRxiv v1. Posted September 29. DOI: 10.64898/2026.09.23.753836.

**Source URL:** https://www.biorxiv.org/content/10.64898/2026.09.23.753836v1.full

**Evidence:** Retrieved bioRxiv abstract and explicit posting date. This is abstract-level triage, not a full Methods review.

**Research problem:** Obtain tissue-wide anatomical coordinates/regions without manually annotating every section.

**Method:** SpatialTRACE-Graph combines expression and spatial neighborhoods to propagate sparse anatomical supervision. SpatialTRACE-Image is a multiscale vision transformer trained on graph-generated predictions to infer axes/regions from DAPI microscopy alone.

**Key result:** Reports axis prediction in held-out mouse-intestine sections with as few as 10 annotated training villi, and region identification including Peyer's patches. Application to infection-associated T cells illustrates anatomical redistribution under retinoic-acid receptor inhibition; the abstract compares individual treated/vehicle sections and does not establish a replicated treatment-effect estimate.

**Why it matters for your AIVC:** A potential anatomy-conditioned environment encoder for cortical depth/layers and a way to test whether local neighborhoods add information beyond anatomical position. That matters because layer structure can masquerade as environmental effects in SCZ/DLPFC.

**What is new:** Sparse graph-based anatomical annotation distilled into DAPI-only image inference, bridging spatial transcriptomics and routine microscopy.

**What is bad / limitation assessment:** Intestinal axes are not cortical lamination; no demonstrated DLPFC transfer. Teacher-generated labels can propagate graph errors into image predictions. Held-out sections are not necessarily held-out animals/donors. This is anatomy estimation, not a perturbation-response simulator or causal signaling model.

**Future research idea — proposal:** Test continuous cortical-depth conditioning against categorical layer labels and local neighborhoods. Train annotation models using training donors only, and require independent anatomical labels and measured held-out genes on test donors before claiming environmental benefit.

## 5. CancerZigZag — SAVE

**Citation:** Schlüter, J., & Schönhuth, A. (2026). *CancerZigZag: Iterative Seed-Anchored Diffusion for Generative Modeling of Single-Cell State Transitions*. arXiv:2609.37735v1. Submitted September 29, 14:54:14 UTC. arXiv comments report acceptance for oral presentation at ISCB-AI 2026; not treated as journal peer review.

**Source URL:** https://arxiv.org/abs/2609.37735v1

**Evidence:** Abstract and introduction at https://arxiv.org/html/2609.37735v1 ; metadata from https://export.arxiv.org/abs/2609.37735 . Indexed methods passages describe patient-wise training/held-out seed separation; complete model selection and benchmark auditing remain unverified.

**Research problem:** Explore disease-associated cell states when data are cross-sectional and no paired healthy-to-disease trajectories exist.

**Method:** Train a diffusion model exclusively on tumor-derived epithelial cells; repeatedly partially perturb and denoise held-out healthy-like seed cells to generate stochastic candidate-state clouds, without paired training or classifier guidance during generation.

**Key result:** Across colorectal, breast, lung and renal cancer contexts, candidate clouds contain tumor-associated outputs for each evaluated seed. Seed-dependent structure is clearest in colorectal cancer, weaker in lung, and limited in breast/renal settings. Representative candidates show directional agreement with held-out expression shifts. No validated healthy-to-tumor progression prediction or general benchmark win is claimed.

**Why it matters for your AIVC:** Directly exposes a failure mode of identity-matched environment swaps: outputs can look like the target condition while losing meaningful dependence on the starting cell. Its explicit distinction between reference-conditioned exploration and causal trajectory simulation is valuable for SCZ cross-sectional claims.

**What is new:** Iterative seed-anchored diffusion with an explicit analysis of target-distribution displacement versus residual seed dependence, rather than equating plausible generated cells with true transitions.

**What is bad / limitation assessment:** No paired/longitudinal ground truth; classifier agreement is not a validated biological trajectory. Seed identity can wash out, and representative-candidate selection needs auditing. No demonstrated neural or perturbation transfer. Lower priority than direct perturbation benchmarks.

**Future research idea — proposal:** Add an identity-retention audit to AIVC environment-swap experiments: compare outputs from matched real seeds, shuffled seeds and identity-free target-distribution sampling. Require measured, seed-specific response information beyond merely becoming target-like; label unpaired outputs as hypotheses until prospectively tested.

## Screening decisions and program implication

P2P (arXiv:2609.34391v1) is scientifically relevant but excluded from the five strict-window recommendations: its submission timestamp, September 28 at 06:06:06 UTC, precedes the supplied cutoff. Search results associate it with a September 29 listing, but the exact listing entry could not be independently recovered because category pages were stale. It may qualify by public-announcement time; that remains unresolved, so do not silently reclassify submission time as publication time. CellRFT was submitted September 17 and excluded as older. Already reported papers were not recycled.

Research interpretation, not a new commitment: representation quality, genuinely independent biological splits, and orthogonal functional endpoints look more defensible than expanding graph/transformer complexity now. BioPert challenges the input representation, DRIFT challenges the fixed-identity assumption, LangPatch supplies a functional-validation template, SpatialTRACE isolates anatomy, and CancerZigZag warns that target-looking outputs are not validated counterfactuals. None establishes that your proposed AIVC already predicts perturbations, explains SCZ, or meets K99 preliminary-data requirements.
