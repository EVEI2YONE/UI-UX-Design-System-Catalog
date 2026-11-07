# Catalog lifecycle and decision policy

**Kind:** policy · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose

Keep reusable design knowledge trustworthy, discoverable, owned and compatible with downstream consumers. A shared concept must justify its maintenance burden.

## Decision order

1. User safety, privacy and non-negotiable constraints.
2. Core task completion and accessibility.
3. Comprehension, information architecture and consistency.
4. Reuse and long-term code stewardship.
5. Theming, localization, performance and flexibility.
6. Aesthetic polish and novelty.

| Decision | Favor when | Beware |
| --- | --- | --- |
| Reuse | Existing meaning, behavior and states fit | Brittle overrides or misleading semantics |
| Extend | Small, explainable variant with a stable API | Combinatorial Boolean props |
| Compose | Business workflow uses stable components | Business state leaking into primitives |
| Create shared | Cross-context need, clear owner, tests and API | One-off, unstable requirements |
| Keep app-local | Domain-specific or experimental | Reimplementing proven shared contracts |
| Merge/deprecate | Duplication or obsolete pattern documented | Breaking consumers without migration |

## Lifecycle labels

- **`proposed`:** draft concept under review; no production claim.
- **`experimental`:** intentionally limited trial with known risks.
- **`stable`:** reviewed guidance or artifact with a maintenance owner and evidence; not necessarily coded or deployed.
- **`deprecated`:** no new usage; replacement and migration documented.
- **`removed`:** intentionally retired with historic traceability.

## Decision record

Record ID, date, scope, problem/user task, alternatives, rationale, owner, evidence source/version, affected consumers, status and revisit trigger. When moving/renaming an entry, preserve its canonical ID wherever possible and note redirects. Keep breaking changes reviewable and versioned.

## Verification

Confirm no duplicate or orphaned entry, a named owner or explicitly `unassigned`, source currency, catalog registry/index synchronization, and documented unknowns. Use [quality gates](quality-gates.md). Never claim a PR, merge or test was completed without a verified result.