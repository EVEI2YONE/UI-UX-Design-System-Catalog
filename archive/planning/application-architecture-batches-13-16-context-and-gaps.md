# Application architecture Batches 13–16 — context and gap ledger

**Date:** 2026-11-07. **Catalog base:** `main` at `85910b2b129a9fc4e51db9130b85e991d084c2e3`. **PR:** #8 (draft). **Source status:** catalog documentation only, all new entries proposed. No target application was named for implementation or audited at a pinned app SHA.

## Context collected before each batch

| Batch | Existing canonical sources inspected | Actual knowledge gap / decision | Outcome |
| --- | --- | --- | --- |
| 13 — Selection | `architecture/component-model.md`; `architecture/README.md`; `governance/quality-gates.md`; `catalog/README.md`; `CONTRIBUTING.md` | Existing model covers component tiers and slice extraction but not profile selection by application scale/complexity. | New `architecture.application-selection` with prototype/MVP/modular/multi-app examples. |
| 14 — Modularity and DX | `architecture/component-model.md`, `architecture/component-contracts.md`, `governance/lifecycle-and-decisions.md`, Batch 13 selection | Existing UI boundary policy does not specify app feature/domain/shared ownership or navigation from developer tasks. | New `architecture.module-boundaries` with import constraints, public interfaces and discoverability checks. |
| 15 — Evolution | `architecture/component-model.md` Batch 9 extraction guidance; `governance/quality-gates.md`; Batches 13–14 | Existing incremental component extraction and release tests are good; application-level scale transitions and fitness measurements are underspecified. | New `architecture.evolution` with evidence triggers, one-slice migrations, baseline/rollback and fitness indicators. |
| 16 — Enterprise | `governance/lifecycle-and-decisions.md`, `architecture/component-model.md`, Batches 13–15 | Multi-application topology, package ownership and independent deployment tradeoffs lack dedicated decision guidance. | New `architecture.enterprise-multiapp` comparing modular monolith, monorepo, multirepo and microfrontends. |

## Scope and coverage disposition

| Candidate gap | Disposition | Canonical owner |
| --- | --- | --- |
| Complexity-adaptive profiles and reference trees | missing dedicated guidance → added proposed | `architecture.application-selection` |
| Feature/domain/shared module boundaries | existing component-level guidance incomplete for apps → extended concept | `architecture.module-boundaries` |
| Reuse decisions and oversized universal components | already in component model; app-level application added | `architecture.component-model` + `architecture.module-boundaries` |
| Developer findability and module navigation | app-level gap → added proposed | `architecture.module-boundaries` |
| Change-safe architectural transitions | component extraction documented, app-level scale evolution incomplete → added | `architecture.evolution` |
| Fitness metrics and regression gates | quality tests exist, app-architecture measures incomplete → added | `architecture.evolution`; `governance.quality` |
| Monorepo/multirepo/microfrontend selection | no dedicated treatment → added proposed | `architecture.enterprise-multiapp` |
| Multi-team ownership and compatibility | generic lifecycle documented, app/package decisions incomplete → extended | `architecture.enterprise-multiapp`; `governance.lifecycle` |

## Applicability limits and sources

The four guides derive baseline reuse/contract principles from the existing catalog and add generalized decision heuristics. They do **not** establish that any real repo has architecture defects, or that one layout reduces code by a measured percentage. Example TS/web trees are illustrative, with routing conventions explicitly subject to framework documents.

Authoritative references for downstream implementations (verify version/applicability at use time):
- [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) — optional TypeScript build boundaries, not a universal directory convention.
- [Next.js project organization](https://nextjs.org/docs/app/getting-started/project-structure) — framework route/layout conventions, not universal domain architecture.
- [Nx concept guide](https://nx.dev/concepts/decisions/why-monorepos) — one tooling vendor's monorepo tradeoffs, not neutral empirical superiority.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — applicable accessibility criteria to preserve during UI architecture changes.

## Validation and disposition

The repo's stdlib validator and unit suite are the specified checks: `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`. Record CI output from the *final* PR head, not from previous runs. Manual keyboard/screen-reader, locale/theme, actual developer lookup and application integration tests: **NOT VERIFIED** (documentation only). Keep the PR in draft until review; no merge or application code changes are authorized.

## Open questions for a real target app

Actual user journeys, measured developer findability, critical workflow baselines, current import graph, ownership, official framework constraints, and deploy requirements remain target-specific and must be collected at the start of each future app migration.
