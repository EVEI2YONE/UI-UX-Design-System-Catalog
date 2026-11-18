# Catalog remediation verification — 2026-11-07

## Baseline and scope
- Baseline main: `1261bc88ff42ea066d2dcc38d535956d118dd70a`
- Remediation branch: `docs/catalog-integrity-remediation-2026-11-07`
- Registry: 49 canonical entries, all proposed at the baseline; no intentional ID, path, status or catalog schema migration.
- Archived 17 historical `planning/*.md` ledgers into `archive/planning/`, removed root `.gitkeep`, and migrated Markdown references and regression fixture paths.
- Consolidated active navigation in root README and AGENTS; preserved dated batch information in the archive and changelog.
- Updated `catalog/README.md` to describe current required retrieval metadata and historic counts accurately.
- Hardened the stdlib validator against missing/nonobject registry entries and invalid primary field types, with negative-test coverage.

## CI evidence
The preceding integrated change head `3b5ccffb2f9bda419ebcbb8798f1cf8f0e2ea359` passed [Validate catalog run #42359895679](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42359895679) (catalog integrity, lookup smoke test, unittests). This result verifies that preceding head **only**.

**Final verification rule:** the final PR head must have its own successful CI run. The PR description records the final-head result after completion; this historical report does not claim future runs already passed.

## Boundaries
Automated checks verify supported catalog integrity and documented lookups. They do not certify full JSON Schema semantics, external resource availability, implementation correctness, security, UX measurement or WCAG conformance. Historical PR and product research statements are snapshots, not live status.
