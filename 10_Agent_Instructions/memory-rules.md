---
type: memory-rules
project: ""
status: active
last_updated: 2026-09-12
confidence: high
---

# Memory Rules

## Canonical sources
- Obsidian = durable project knowledge.
- Hermes internal memory = operational agent experience/preferences.
- Raw chats/logs = archive, not canonical.

## Before asking user
1. Search `00_Profile/context-index.md`.
2. Search project-specific current-state notes.
3. Search decisions/errors notes.
4. Ask only when missing or conflicting.

## Retrieval
- Load only relevant notes.
- Prefer latest dated state.
- For projects prioritize:
  - `current-state.md`
  - `important-decisions.md`
  - `environment-and-paths.md`
  - `todo-and-next-actions.md`

## Write memory only for
- verified decision,
- verified result,
- stable preference,
- reusable fix,
- important path/config,
- active next action.

## Do not write
- guesses,
- transient debugging noise,
- secrets,
- unverified model claims.

## Conflict policy
- `⚠️ VERIFY` = possibly stale.
- `? UNCERTAIN` = incomplete recollection.
- Do not overwrite conflicting facts without evidence.
