# AIVC Literature Radar — 2026-10-28

## Window and continuity

Previous radar completed 2026-10-26 10:06 UTC. All five selected preprints were first posted by bioRxiv on 2026-10-27, confirmed through Crossref `posted` metadata and primary bioRxiv records. No selected title or DOI appeared in prior AIVC radar session history. Current direct vault-read/search capability was unavailable; comparison therefore uses the latest recovered AIVC literature/state notes from the October 26 radar and weekly strategy. Those notes describe an identity-plus-environment model (scGPT/UCE identity plus cell-type-stratified environmental expression), possible graph/attention/perturbation-decoder extensions, and an immediate priority to establish nuisance-aware measured-target context value under donor holdout before expanding architecture. Canonical disease focus remains schizophrenia in human DLPFC.

All performance results below are author-reported preprint results, not independent reproductions. Full primary text was inspected for UPM; primary abstracts and indexed PDF text were used for the other papers. No withdrawal notice was observed.

## 1. READ NOW — Unified Perturbational Modeling (UPM)

**Citation:** Wei Z, Ye Y, Cui S, Ma W, You Y. *How Much Can AI Virtual Cells Gain from Unified Perturbational Modeling?* bioRxiv v1, posted 2026-10-27. DOI: 10.64898/2026.10.25.761625.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.25.761625v1

**Research problem:** AIVC predictors are usually specialized to one gene panel, perturbation type, or cellular context; heterogeneous Perturb-seq resources cannot be pooled naively.

**Method:** A VAE-based predictor adds (1) Ensembl-based union-gene channel alignment, (2) perturbation-type-specific inputs projected into a shared perturbation space, and (3) joint embeddings of expression values and gene identities. The full model has more than one billion parameters and was trained on 89.7 million cells from 71 contexts, drawn from a 110-million-cell collection spanning 22,768 genes and CRISPRi, CRISPRa, drugs, and cytokines. The decoder predicts an expression change added to the control input; combined-perturbation embeddings are averaged.

**Key result:** Authors report the highest PES and gene-wise response correlation among evaluated genetic-perturbation models, improvement over State on five held-out Tahoe-100M cell lines and over Stack on cytokines, gains for combinations, and a 40% downstream-accuracy improvement for recapitulating HSC-target knockdowns.

**What is new:** The contribution is not a new graph architecture; it is explicit *unification* across gene panels, intervention modalities, and contexts at unusually large scale, with component ablations and one model handling several response regimes.

**Why it matters for the current AIVC:** This is the strongest new challenge to architecture-first planning. A large, relatively conventional VAE trained on heterogeneous perturbational data may gain more from alignment and coverage than a bespoke graph transformer. The current measured-target, donor-held-out context-value test remains the correct first experiment. Any later graph/transformer claim should be evaluated on top of a fixed unification/data budget and against UPM-style alignment.

**What is bad / unresolved:** Parameter scale, data scale, and the three unification modules are intertwined in the headline model; a decisive compute/data-matched comparison is still needed. Held-out cell lines do not establish generalization to independent laboratories, donors, disease tissue, or spatial neural context. Averaging perturbation embeddings is a weak mechanistic model of combinations. The principal outputs remain RNA proxies; there is no SCZ/DLPFC validation or prospective experiment in the inspected evidence.

**Future research idea:** Build a compact “UPM-lite” baseline on identical genes, donors, perturbations, and training cells, then add the AIVC environmental graph while keeping parameter count and data fixed. Test whether neighborhood context improves unseen-target and unseen-donor response prediction beyond unified alignment alone.

## 2. READ NOW — BLOOM virtual embryo model

**Citation:** Liang Z, Li S, Li B, Huang Y, Yu L. *BLOOM: Biologically Informed Flow Matching for Transcriptomic Virtual Embryo Modeling.* bioRxiv v1, posted 2026-10-27. DOI: 10.64898/2026.10.26.761895.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.26.761895v1

**Research problem:** Generate heterogeneous single-cell expression populations at queried developmental stages from destructively sampled time-series atlases, including interpolation and longer rollouts.

**Method:** Conditional flow matching with a shared cell encoder, permutation-invariant stage pooling, recurrent temporal context, optimal-transport pseudo-trajectories, and learned gates for developmental age, hierarchical cell identities, anatomical context, gene programs, developmental graphs, and weighted TF–target networks. Biological priors condition both a Gaussian base distribution and the flow generator.

**Key result:** Across prenatal mouse development, visual-cortex maturation, and multi-organ endothelial development, authors report first rank among 22 forecasting baselines for stage-averaged gene and cell correlations. They also report interpolation, bidirectional reconstruction, history/future rollouts, and input-based in-silico gene perturbations.

**What is new:** A single generative framework combines ordered population history with multiple biological priors at both initialization and generation stages. It is close in spirit to a biology-plus-context model, but uses gated conditioning and flow matching rather than a graph transformer.

**Why it matters for the current AIVC:** BLOOM narrows the novelty of simply combining regulatory graphs, biological modules, context, and a generative decoder. A defensible independent contribution would be measured *spatial microenvironment value*, disease/SCZ relevance, and intervention generalization—not another list of priors. Visual-cortex data make its design especially worth inspecting.

**What is bad / unresolved:** Pseudo-trajectories are inferred correspondences, not observed lineages. Performance at measured held-out stages does not validate extrapolated pre-/post-observation rollouts. The reported gene perturbations alter inputs; the inspected evidence does not show independent measured perturbation-response validation. Mouse development is not mature human DLPFC disease biology.

**Future research idea:** Use BLOOM’s gated-prior design as a comparator, but replace broad developmental priors with measured local-cell composition and ligand–receptor context. Evaluate only held-out neural donors/perturbations and require gains over identity-only and shuffled-neighborhood controls.

## 3. SAVE — Molecular context for brain-specific NDD gene function

**Citation:** Djokic M, Karunanithi S, Welzel M, Kielisch F, Luck K. *Cellular context defines brain-specific functions of genes associated with neurodevelopmental disorders.* bioRxiv v1, posted 2026-10-27. DOI: 10.64898/2026.10.26.761783.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.26.761783v1

**Research problem:** Explain why genes without brain-preferential expression can nevertheless produce brain-specific disease phenotypes.

**Method:** Harmonize spatiotemporal transcriptome datasets across tissues and developmental stages for about 1,000 NDD genes, then combine tissue-agnostic PPI networks with the expression resource to infer brain-specific partners. The authors experimentally test QRICH1 interactions and disease variants.

**Key result:** Only about 10% of the NDD genes were brain-preferentially expressed. The framework nominated brain-specific partners for 22 uniformly expressed genes; QRICH1 interactions were experimentally supported and disrupted by disease-associated variants.

**What is new:** It operationalizes tissue context as a filter on otherwise tissue-agnostic interaction networks and provides targeted experimental validation—evidence that expression specificity alone misses disease-relevant function.

**Why it matters for the current AIVC:** This supports the central rationale for an environment/context encoder: disease-relevant function can emerge from context-conditioned partners rather than cell identity or gene expression alone. It also suggests a stronger biological interpretation target than attention maps: context-specific interaction hypotheses.

**What is bad / unresolved:** “Context” here is primarily tissue/developmental transcriptomic context plus prior PPIs, not measured single-cell spatial neighborhoods. The experimental validation centers on one Mendelian NDD gene, not schizophrenia, polygenic risk, perturbation forecasting, or DLPFC. Twenty-two nominations are hypothesis generators, not a general causal map.

**Future research idea:** For SCZ-prioritized genes, construct cell-type- and spatial-neighborhood-conditioned interaction candidates in DLPFC; test whether those candidates explain held-out perturbation effects better than expression level, generic PPI degree, and cell identity alone.

## 4. SAVE — ProtCell single-cell proteomics foundation model

**Citation:** Hu B, Li Z, Jiang Q, Yin Q, Liu Z, Jiang R. *ProtCell: a foundation model for single-cell proteomics.* bioRxiv v1, posted 2026-10-27. DOI: 10.64898/2026.10.22.760932.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.22.760932v1

**Research problem:** Targeted single-cell protein assays use small, non-identical panels, fragmenting cell-state information across experiments.

**Method:** A transformer encoder combines protein-identity and continuous-abundance embeddings and is pretrained by masked abundance modeling on approximately 380 million cells from 98 datasets. Learned cell/protein representations support label transfer, batch correction, protein reconstruction, and panel design.

**Key result:** Authors report transferable annotation and integration, reconstruction beyond measured panels, recovery of an unmeasured cytotoxic protein program enriched in NK and memory CD8 T cells, and compact panels retaining reconstruction/classification information.

**What is new:** Very large-scale protein-specific pretraining and use of learned dependencies not only for imputation but for measurement-panel design.

**Why it matters for the current AIVC:** A future multimodal AIVC should predict orthogonal functional readouts, not RNA alone. ProtCell offers a protein representation/measurement-design branch that could support prospective validation and K99 rigor after transcriptomic context value is established.

**What is bad / unresolved:** It is not a perturbation-response model. Imputed unmeasured proteins can reflect learned correlation rather than causal or truly observed protein biology. The conceptual niche overlaps earlier transformer proteomics models such as scpFormer, so novelty depends on scale, evaluation quality, and panel-design evidence. No neural/SCZ application is established.

**Future research idea:** Use ProtCell-style panel optimization to design a small neural/glial protein panel that maximizes discrimination among predicted perturbation responses; validate the proteins prospectively rather than treating imputation as ground truth.

## 5. SAVE — Donor-aware evaluation of cell-type classifiers

**Citation:** Chen X, Li J, Battle A. *Evaluation design shapes estimates of cross-donor generalization in single-cell classification of cell-type.* bioRxiv v1, posted 2026-10-27. DOI: 10.64898/2026.10.26.761949.

**Source:** https://www.biorxiv.org/content/10.64898/2026.10.26.761949v1

**Research problem:** Determine when random cell splits overstate generalization because cells from the same donor appear in train and test partitions.

**Method:** Compare random-cell and donor-held-out cell-type classification across multiple expression representations and PBMC/lung datasets; test persistence after batch-covariate adjustment and donor mixed-effects modeling; include near-ceiling datasets and a randomized-label floor control.

**Key result:** Random cell splits consistently yielded higher macro-F1 than donor-held-out evaluation in PBMC and lung. The gap persisted after covariate adjustment and mixed modeling, but was minimal in near-ceiling kidney/pancreas/blood settings and at the randomized-label floor.

**What is new:** The useful refinement is regime dependence: split bias is neither universally huge nor fixed; it is most visible when the task has learnable donor-associated structure and is not already at ceiling/floor.

**Why it matters for the current AIVC:** It directly supports the existing decision to use held-out donors for context-value estimation. It also argues for reporting both absolute held-out performance and the random-vs-donor optimism gap rather than treating donor adjustment as a substitute for donor holdout.

**What is bad / unresolved:** This is cell-type classification, not perturbation response, causal inference, spatial prediction, or disease modeling. Results from PBMC/lung may not quantify the effect in postmortem DLPFC. Donor holdout still does not guarantee cross-site, cross-assay, or independent-culture generalization.

**Future research idea:** For every AIVC ablation, report a generalization profile across random-cell, donor-held-out, and site/assay-held-out splits. Test whether the environmental module’s gain survives as transfer distance increases.

## Program implication

The immediate program decision does not change: prove measured spatial-context value under donor holdout before architecture expansion. UPM is the most important new comparator because it separates data unification from architectural novelty. BLOOM shows that gated developmental and regulatory priors plus flow matching already occupy much of the proposed design space. The strongest differentiated direction remains a rigorously evaluated, spatially contextual, disease-relevant neural AIVC with independent-unit validation and orthogonal readouts. No project tracker, implementation specification, deadline, or grant claim was changed.
