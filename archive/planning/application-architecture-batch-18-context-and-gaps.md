# Batch 18 — architecture enforcement and CI: context and gap ledger

**Date:** 2026-11-07 · **PR:** #8 (draft) · **Prior head:** `d634b1fc440f966d99f46778d1521d5ae583cd2b` · **Scope:** proposed knowledge, not application changes.

## Context gathered before Batch 18

| Existing source | What it already owns | Distinct unresolved decision |
| --- | --- | --- |
| `architecture/module-boundaries-and-developer-navigation.md` (Batch 14) | Feature/domain/shared responsibility, one-way imports and public interfaces | Says to enforce boundaries, but gives no tested mechanism or known blind spots |
| `architecture/architecture-evolution.md` (Batch 15) | Migration strategy, architecture fitness and rollback | Needs a staged legacy-violation to blocking-CI transition |
| `architecture/framework-aware-application-structure.md` (Batch 17) | Framework route ownership and preserved special files | Requires resolver- and route-aware enforcement rather than generic alias assumptions |
| `governance/quality-gates.md` | Documentation versus runtime test status and architecture acceptance | No tool-specific validation matrix for false negatives, exceptions or CI rollout |
| `catalog/index.json` + retrieval suite | Canonical metadata, lookup and tests | Needs an explicit entry for hands-on architecture enforcement knowledge |

**Finding — KG-12 (incomplete coverage):** The catalog has enforceable *principles* but not actionable implementation recipes or safeguards against misleading CI passes. Add one proposed page `architecture.enforcement-ci`, preserving prior pages as owners of design decisions and general quality gates.

## Primary-source verification (2026-11-07)

| Source | Supported statement | Qualification |
| --- | --- | --- |
| [ESLint no-restricted-imports](https://eslint.org/docs/latest/rules/no-restricted-imports) | Supports scoped static import restrictions with patterns and messages | Does not cover dynamic imports; literal specifier matching can miss relative alias alternatives |
| [dependency-cruiser rules](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md) | Can identify circular dependencies and `from`/`to` path constraints | Accuracy requires correct resolver and project config |
| [dependency-cruiser CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md) | `--config` and error reporter can fail on error-severity violations | Example is not evidence tools are installed |
| [Nx module boundaries](https://nx.dev/docs/features/enforce-module-boundaries) | Tags and `@nx/enforce-module-boundaries` can restrict project dependencies | JS/TS rule is project-based; cross-language conformance is separate |
| [Nx boundary rule options](https://nx.dev/docs/kb/enforce-module-boundaries) | Supports per-project-tag dependency constraints | `type:feature` alone does not isolate sibling features |

## Batch decisions

- **Do not** install ESLint, Nx or dependency-cruiser in the docs-only catalog: no application import graph is present.
- Describe a tool selection path by codebase need rather than a universally mandatory stack.
- Provide explicit positive and negative import fixtures, aliases/relative-import caveats, CI rollout, exception expiration and test evidence.
- Keep module ownership guidance canonical in Batch 14 and migrations canonical in Batch 15; do not duplicate either chapter.
- Do not confuse documentation regression tests for executable validation of JavaScript config fragments.

## Verification boundaries

Catalog validation + unittest discovery on final PR head: check and record actual GitHub Actions result. No JS/TS project lint run, runtime graph verification, performance/UX measurement or accessibility tests were executed here. These remain **NOT VERIFIED** for any implementing application. All content status: `proposed`.
