# [Feature reference title]

**Artifact:** feature reference specification · **Catalog status:** proposed · **Implementation:** NOT PRESENT · **Review:** NOT VERIFIED

## Identity and discovery

- **Proposed canonical ID:** `feature.[stable-slug]` (register only after duplicate/synonym review)
- **User job / audience:** [specific cross-product task and users]
- **When useful:** [observable contexts]
- **Avoid when:** [single control/pattern enough; product-specific needs]
- **Cross-context justification:** [two independent use cases or documented strategic need]
- **Owner:** unassigned
- **Existing canonical owners:** [IDs, paths, links; no duplicate definitions]

## Scope, task and integration boundaries

**Entry conditions:** [what user knows and is allowed to do]  
**Successful completion:** [observable outcome, not just button click]  
**Explicit non-goals:** [product APIs, auth, server-side state invariants, domain calculations]  
**Consuming app provides:** [typed data/command adapters, permissions source, product semantics, persistence verification]  
**Reference provides:** [composition, accessible interactions, rendering, pending/errors, scenario fixtures]

## Journey and states

| Stage | Input / user action | UI state | Authoritative or simulated outcome | Focus/recovery |
| --- | --- | --- | --- | --- |
| Entry | [selection] | initial/loading/empty | [simulated] | [focus target] |
| Inspect | [detail] | loaded/partial | [simulated] | [focus target] |
| Decide | [command] | pending/denied/error | [not a security gate] | [restore path] |
| Confirm | [verify result] | confirmed/unknown/conflict | [explicit simulation] | [next action] |

Specify cancel, retry, stale versions, double activation, lost acknowledgement, low connection and data growth as applicable. Never claim a business mutation is complete from a local click.

## Dependencies and ownership

- **Foundations:** [canonical IDs]
- **Components:** [canonical IDs]
- **Patterns:** [canonical IDs]
- **Other guidelines:** [accessibility, performance, i18n, content]
- **Do not duplicate:** [specific existing contract sections]

## Preview and implementation binding (Phase 2+)

- **Documentation:** `features/[slug]/spec.md` (normative)
- **Implementation:** `site/src/implementations/features/[slug]/` (only when real)
- **Scenarios:** [deterministic data, synthetic adapter; reset and failure modes]
- **URL:** [optional future preview path, not claimed live]
- **Source view:** [must show actual implementation code]
- **Mock safety:** [no network writes, real credentials, personal data or implied server authorization]

## Readability, accessibility, performance and locale

Document navigation hierarchy, copy/error comprehension, accessible roles/names, keyboard/focus, screen-reader announcements, zoom, theme, contrast, touch, RTL and translation growth. Identify constrained device and large-dataset cases and performance measurement plan; no invented benchmark.

## Evidence

| Check | Status | Evidence |
| --- | --- | --- |
| Existing concept/synonym search | NOT VERIFIED | |
| Cross-context reuse rationale | NOT VERIFIED | |
| Contract/UX peer review | NOT VERIFIED | |
| Source and preview parity | NOT VERIFIED | |
| Keyboard/AT and responsive testing | NOT VERIFIED | |
| Performance/readability review | NOT VERIFIED | |
| Agent retrieval regression | NOT VERIFIED | |

## Lifecycle, limitations, migration

Owner, version, review date, known unknowns, adoption constraints, compatibility policy and rollback plan. A **stable specification** does not certify a **stable implementation**. Link to [lifecycle policy](../governance/lifecycle-and-decisions.md) and [quality gates](../governance/quality-gates.md).
