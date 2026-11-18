# Catalog integrity remediation audit (2026-11-07)

Baseline: `1261bc88ff42ea066d2dcc38d535956d118dd70a` on `main`. Scope: documentation, lookup registry, provenance, validation, and testing. No product implementation or accessibility audit.

## Source-of-truth policy

- `catalog/index.json`: canonical concept IDs, paths, lifecycle statuses, retrieval metadata.
- `catalog/schema.json`: complete machine-readable metadata contract.
- Canonical concept pages: design guidance and limitations.
- Root/section READMEs and `AGENTS.md`: task-first navigation and retrieval procedure.
- `CHANGELOG.md` and dated archival ledgers: historical changes, research decisions and context.
- Scripts/tests/CI: documentation integrity, **not** UX, accessibility or production certification.

## Baseline observations

- 49 registered concepts at the baseline; all marked `proposed`.
- `catalog/README.md` contains a historical count of 40 and an outdated description implying that retrieval metadata was only provided for the first scaffold entries.
- The stdlib validator implements only a subset of schema validation and can throw an exception on malformed fields instead of reporting a diagnostic.
- README/AGENTS/CHANGELOG accumulate chronological batch notes that obscure current task-first instructions.
- Seventeen `planning/*.md` files hold historical audit/progress material, including Little Wins and application architecture context. Preserve rather than delete; any move must update links and tests.
- Root `.gitkeep` is unnecessary now that the repository contains tracked content.
- Application-named retrieval tests contain useful general regression coverage; preserve scenarios while removing archival-path coupling.

## Preservation and non-goals

Do not change canonical IDs, paths or statuses merely to simplify the tree. Keep historical commit/PR claims as explicitly dated snapshots, not current assertions. Do not mark runtime, human accessibility or user research verification PASS based on a Markdown validator. Avoid mass edits to canonical UX recommendations in this maintenance PR.

## Phase checkpoints

1. Baseline and classification (this document).
2. Registry contract/documentation and validator correctness.
3. Provenance archive and link/reference migration.
4. Current-first READMEs, agent instructions and changelog.
5. Regression tests and CI.
6. Final-head verification and PR evidence.
