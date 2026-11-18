# Batch 17 — framework-aware application architecture: context and gap ledger

**Date:** 2026-11-07. **PR:** #8 (draft). **Prior head:** `52e747954bcdfa28a794d12a6f59f41efd4a48dd`. **Scope:** knowledge/documentation only; no target application repository provided.

## Context collected before drafting

| Source | Existing coverage | Gap classification |
| --- | --- | --- |
| `architecture/application-architecture.md` (Batch 13) | Context-first selection and example prototype/MVP/modular/enterprise trees | incomplete: examples are generic and routing conventions are explicitly deferred |
| `architecture/module-boundaries-and-developer-navigation.md` (Batch 14) | Feature/domain/shared ownership and developer navigation | incomplete: no decision rules for router-owned vs feature-owned files |
| `architecture/architecture-evolution.md` (Batch 15) | Incremental migration and architecture fitness | incomplete: no framework-specific route preservation scenarios |
| `architecture/enterprise-and-multiapp.md` (Batch 16) | Repository topology and multi-app ownership | already covered at topology level; do not duplicate |
| `patterns/navigation.md` / `pattern.navigation` | User-facing navigation semantics | adjacent knowledge, not source folder or framework rules |

## Primary source ledger (consulted 2026-11-07)

| Evidence | Official reference | Applicability and limitation |
| --- | --- | --- |
| App Router route groups do not appear in URL; layout interactions matter | [Next.js route groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups) | App Router only; compare installed framework version |
| Next.js has special route files and permits alternative organization | [Next.js project structure](https://nextjs.org/docs/app/getting-started/project-structure) | Do not enforce one `src/features` layout |
| Angular guide prefers feature areas, colocated tests/templates/styles | [Angular style guide](https://angular.dev/style-guide) | Angular-specific conventions, not React layout prescription |
| React Router file conventions are optional and support route folders | [React Router file route conventions](https://reactrouter.com/how-to/file-route-conventions) | Requires the chosen routing mode and corresponding configuration |

## Decision and patch

**Knowledge gap KG-11: framework-specific adaptation of scalable source structures.** Classified `incomplete`, not `missing all guidance`. Added `architecture.framework-aware` as a separate canonical page because route-file mechanics differ materially from general component and feature ownership. Keep the generic model in Batch 13 and avoid copying its complete profiles into this page.

Changes: framework adaptation decision rules; illustrative Next.js, Angular and React Router trees; route vs shared feature placement table; migrations that preserve deep links, layouts, route lifecycle, server/client and accessibility; limitations for unresearched frameworks. Update root/architecture/catalog/agent lookup, regression tests and this evidence ledger.

## Validation

Run the catalog validator and unittest discovery on the **final PR head**. The first CI status after commits may be pending; record the exact run and do not infer pass from a prior run. These docs have **NOT VERIFIED** application behavior, developer lookup speed, a11y, performance or changes in lines of code. Status remains `proposed`.
