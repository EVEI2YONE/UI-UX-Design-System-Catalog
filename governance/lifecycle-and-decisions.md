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

## Definition of done for a proposed catalog entry

Before requesting `experimental` or `stable`, capture: a canonical ID and working path; user/design decision; use and avoid cases; evidence and standards scope; example and anti-example; component/state implications; accessibility/i18n/theme considerations; an owner; date; test results; consumer impact and migration notes. A `stable` guideline may remain documentation-only; code maturity must be tracked separately.

**Review transitions:**
- `proposed → experimental`: assigned owner, bounded trial context and explicit unknowns.
- `experimental → stable`: reviewed evidence for the stated artifact type, consumers and maintenance plan.
- `stable → deprecated`: replacement or stop-using rationale, affected consumers, migration path and sunset review.
- `deprecated → removed`: link/reference preservation and compatibility implications documented.

**Decision-record example (illustrative):** `DS-EXAMPLE-01` — reuse existing Dialog shell for destructive tasks; keep confirmation text, access checks and mutations in the feature; reconsider if the shell cannot satisfy tested focus and modal semantics. Owner: unassigned; review: pending. This is not an approved project decision.

## Agent-first catalog maintenance

Every canonical record must include immutable ID, path, lifecycle status, `owner` (explicitly `unassigned` where unknown), nullable review date, `use_when`, `avoid_when`, `related` and `depends_on`. Relationships in `depends_on` must be acyclic; `related` indicates optional supplementary reading, not mandatory prerequisites.

**Proposed maintenance cadence:** review ownership and the applicability of authoritative references quarterly, but do not assign a review date or promote an entry without an actual reviewer and recorded evidence. Record affected consumers, migration path, source/edition, test results and unresolved risks in each PR. If a canonical path moves, preserve IDs and provide a redirect or compatibility note. Documentation status is never proof that framework-specific code is deployed.
