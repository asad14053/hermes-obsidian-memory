# Source extracts for 2026-11-08 morning research

Linked brief: [[../2026-11-08-morning-research]]

## [1] Apiiro: coding agents leaking credentials

Apiiro research found 2,539 real secrets in 1,994 public GitHub repositories: database passwords, cloud keys, API tokens, SSH root logins.

Out of 104,185 public copies of this file on GitHub, 1,122 hold a real secret.

No credential was used or tested, and no host was contacted. "Real secret" means a credential that matches a provider format or points at a public host, not one known to be valid.

Source: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again

## [2] Anthropic: Claude Code permissions

When you choose "Yes, and don't ask again" and the approval saves permanently, such as for a Bash command or a WebFetch domain, Claude Code saves the rule to `.claude/settings.local.json` at the root of the git repository, resolved through worktrees to the main checkout.

Source: https://code.claude.com/docs/en/permissions

## [3] Anthropic: Claude Code settings

Claude Code adds it to your global git excludes the first time it writes the file, so it stays out of your commits; if you create the file by hand, add it to `.gitignore` yourself.

Source: https://code.claude.com/docs/en/settings

## [4] The Hacker News

Apiiro's search of public GitHub found 104,185 copies of the file in 103,617 repositories, its research write-up shows. About 1.1% of them, or 1,122 copies, hold at least one secret. Together they hold 1,379 different secrets.

Source: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html

## [5] DeepMind working paper: restricted-oracle roots

With the same algorithm, polynomials and bounds, the first root took 391 CPU core-years, 3.5 times less than the original computation. Two cooperating AI agents designed, ran and debugged this computation in under four days.

Important: Our results don't threaten deployed cryptosystems today that are based on 2048-bit and larger RSA.

Source: https://storage.googleapis.com/deepmind-media/papers/Faster_Affine_Root_and_a_1024bit%20Computation.pdf

## [6] DeepMind working paper: fan factories

At leading order, that is, with the o(1) terms set to zero, a precomputation of one factorization lets each further 1024-bit integer be factored at about 1/58 of the cost of factoring it with the NFS, 30 times less than with MNFS.

The results hold under the standard heuristics of NFS analyses, and the algebraic identities and exact feasibility witnesses behind them are machine-checked in Lean 4.

Source: https://storage.googleapis.com/deepmind-media/papers/Fan_Factories_Multiple_Number_Fields_in_Factorization_Factories_and_Batch_NFS.pdf

## [8] The Verge: New Matrix reporting

New Matrix is on the list of approved firms, yet its offices are empty, "a hollow gray shell with wires dangling from the ceiling where lights should be."

Source: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government

## [10] Bureau of Industry and Security

BIS will now review export license applications for the Nvidia H200, AMD MI325X, and similar chips on a case-by-case basis provided certain security requirements are met.

Source: https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china

## [11] Federal Register

The Bureau of Industry and Security (BIS) is revising its license review policy for exports of certain semiconductors to China and Macau, changing it from a presumption of denial to a case-by-case review.

Source: https://www.federalregister.gov/documents/2026/01/15/2026-00789/revision-to-license-review-policy-for-advanced-computing-commodities

## [12] Reuters: H200 approvals and delivery status in May

The U.S. has cleared around 10 Chinese firms to buy Nvidia's second-most powerful AI chip, the H200, but not a single delivery has been made so far, three people familiar with the matter said.

Source: https://www.reuters.com/business/retail-consumer/us-clears-h200-chip-sales-10-china-firms-nvidia-ceo-looks-breakthrough-2026-05-14

## [14] Tech AI Latest: measured versus theoretical RSA claims

The first result concerns digital signatures. DeepMind says the agents designed a new algorithm for forging RSA signatures when an attacker controls only a small part of the signed data, such as a 32-byte fingerprint, and estimates that it improves on the best previously known attack by about 1,600 times for 1024-bit keys. DeepMind describes this figure as a theoretical estimate.

Source: https://techailatest.news/cybersecurity/google-deepmind-ai-agents-rsa-1024-weaknesses

## Coverage gaps

- The New York Times investigation at `https://www.nytimes.com/2026/11/07/business/economy/nvidia-chips-chinese-firms.html` returned 403 to extraction, had no archive snapshot, and could not be opened because the configured real-profile browser was unavailable. The brief therefore attributes the New Matrix details to The Verge's direct summary.
- X extraction for Pushmeet Kohli's DeepMind announcement failed, so the technical claims rely on the two working papers and a dated secondary report.
- No independent reproduction of DeepMind's new cryptanalytic methods was found in this run.
