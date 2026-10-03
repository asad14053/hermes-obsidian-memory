---
type: project-state
project: "AIVC"
status: active
last_updated: 2026-09-23
confidence: medium
---

# AIVC — Current State

- Learning/design phase.
- Prior work covered PDGrapher, CellOT, causal ML networks, graph structure for ST, pure-transformer alternatives, perturbation masks, target-response prediction.
- User has specifically asked:
  - model inputs,
  - latent confounders,
  - graph construction/update,
  - code/data graph representation,
  - “tier 2” meaning in method context.
- ? UNCERTAIN exact current implementation branch/repository.

## Evidence gaps affecting the next phase

### Source update — September 23, 2026

- The user supplied a two-page broad outline and a multimodal architecture diagram, now preserved in [[02_Projects/AIVC/project-outline]]. A concrete proposed UR/VI architecture and evaluation plan are therefore documented; implementation and experimental completion are not established by this upload.
- The PDF proposes 20 μm cell-type-stratified distance-weighted neighborhoods, attention-based activity prediction, and identity-matched environment-swap validation. The image proposes a richer multimodal, multi-scale conditional-VAE extension and explicit donor-held-out tests. Neither was designated to replace the other.
- The image explicitly includes SCZ/NTC brain context; the broad PDF does not mandate a disease. Prior NIA aging/AD recommendations remain application-specific assistant proposals, not an approved replacement of the user's research scope.

### Prior review context — September 20, 2026

- No frozen prediction estimand, primary aging/AD perturbation dataset, external validation dataset, leakage-resistant fold manifest, or AIVC baseline result is documented.
- No prospective perturbation validation, aging/AD functional endpoint, or defined K99 career-development plan is documented.
- The 2026-09-20 NIA K99 review again rated the current concept Overall Impact 8/9 and **STAGNANT**: no new scientific result, premise artifact, dataset pair, baseline, context ablation, external validation, or training/independence plan is documented. Recent literature raises the novelty and benchmark-overfitting bar but does not add project evidence. This is a reviewer-style assessment, not a scientific result.
- ? UNCERTAIN The canonical goal remains SCZ-centered, while the NIA review and 2026-09-13 weekly strategy require aging/AD to be the organizing question for an NIA application. No permanent disease-focus change has been approved.
