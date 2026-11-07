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

## Batch 12 extension — DesignOps and design-to-code lifecycle

When a proposal becomes a real component, track **design decisions, code delivery and evidence separately**. This extends the existing lifecycle policy rather than adding a parallel governance entry.

1. **Intake:** record task, existing concept/alias search, reuse/extend/create rationale, consumers, product risks and owner.
2. **Design-ready:** supply stable role, states/variants, responsive behavior, localization/RTL, accessibility/focus and semantic token intent. State any unknowns.
3. **Build-ready:** engineering and designer agree on public API, feature/domain boundaries, versioned token formats, supported runtimes, compatibility and rollback.
4. **Review-ready:** compare actual code/stories with the contract; verify keyboard/screen reader, interactive failure states, visual diffs, themes, large text and supported locales.
5. **Release-ready:** record consumer impact, deprecation/version notice, real build/test evidence, staged rollout/monitoring and responsible on-call/rollback owners.
6. **Maintain:** monitor adoption, defects, support feedback, reference editions and migration; do not promote to stable without artifact-specific review.

| Asset | Where truth lives | Responsible review |
| --- | --- | --- |
| Design intent and canonical decision | Catalog ID, version and research/decision record | Design system / UX owner |
| Token schema and role mapping | Versioned token source and platform transform outputs | Token/library maintainer |
| Component contract | Owned API, semantics, states and compatibility notes | UI engineering + design |
| Product permissions, validation and data effects | Feature service and integration | Feature/security owner |
| Visual acceptance | Reviewed reference snapshots and documented approved differences | Design + engineering |
| Release, actual task and perf metrics | Deployment/monitoring and experiment system | Product/delivery owner |

**Illustrative handoff:** An input control gains an error description. Handoff records the error association and focus behavior, token/RTL scenarios, migration for consumers, screen reader tests and rollback. **Anti-example:** A design frame is treated as an implementation specification and a build ships without keyboard/validation behavior.

**Boundary:** a polished design, a passing catalog validator, a component story, and a deployed accessible user journey are different artifacts with different evidence. Follow [quality gates](quality-gates.md), [component contracts](../architecture/component-contracts.md), and [tokens](../foundations/design-tokens-and-themes.md). No actual toolchain or release is claimed by this proposed process.

## Settings-specific lifecycle application (KG-014, PR #13; proposed 2026-11-07)

The general lifecycle states above govern **catalog concepts**, not product setting values. For settings with stored values and versioned clients, use the [per-setting transition matrix](../patterns/account-and-settings-portal.md#settings-knowledge-batch-3--configuration-lifecycle-and-migration-kg-014-proposed-2026-11-07) to review missing defaults, key/label renames, split/merge, scope/authority changes, deprecation, and removal. A renamed control must not silently reset an explicit choice; a moved setting must not silently broaden who it affects. Keep app-specific storage migrations and permission checks with the product owner. Product/runtime migration tests remain **NOT VERIFIED** until actually executed.
