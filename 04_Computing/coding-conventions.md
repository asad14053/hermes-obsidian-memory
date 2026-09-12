---
type: coding-conventions
project: ""
status: active
last_updated: 2026-09-12
confidence: high
---

# Coding Conventions / Working Style

- Prefer copy/paste-ready terminal commands.
- For terminal-only file creation use `cat > file <<'EOF'`.
- Before changing working files:
  1. inspect,
  2. back up,
  3. minimal change,
  4. validate syntax,
  5. test.
- For Docker/Compose, inspect current setup before adding services.
- Do not install a second reverse proxy when Traefik already handles TLS.
- For HPC, separate test/full modes and use arrays for donors.
- Preserve raw counts and derived layers distinctly in AnnData.
- Never silently mutate metadata semantics.
- Put exact model formulas in DE scripts/outputs.
- Verify code changes through execution/logs, not assumption.
