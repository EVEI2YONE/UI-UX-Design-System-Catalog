# [Feature reference title]

**Artifact:** experience concept specification · **Catalog status:** proposed · **Review:** NOT VERIFIED

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
**Guidance provides:** [composition decisions, accessible interactions, relevant states and failure/recovery requirements]

## Journey and states

| Stage | Input / user action | UI state | Authoritative or simulated outcome | Focus/recovery |
| --- | --- | --- | --- | --- |
| Entry | [selection] | initial/loading/empty | [service-defined result or unknown] | [focus target] |
| Inspect | [detail] | loaded/partial | [service-defined result or unknown] | [focus target] |
| Decide | [command] | pending/denied/error | [not a security gate] | [restore path] |
| Confirm | [verify result] | confirmed/unknown/conflict | [verified service result or unresolved state] | [next action] |

Specify cancel, retry, stale versions, double activation, lost acknowledgement, low connection and data growth as applicable. Never claim a business mutation is complete from a local click.

## Dependencies and ownership

- **Foundations:** [canonical IDs]
- **Components:** [canonical IDs]
- **Patterns:** [canonical IDs]
- **Other guidelines:** [accessibility, performance, i18n, content]
- **Do not duplicate:** [specific existing contract sections]

## Documentation and traceability

- **Canonical source:** `specifications/experiences/[slug]/spec.md` (concept guidance only)
- **Decision rationale:** [use/avoid, meaningful alternatives and scenario boundaries]
- **Design review scenarios:** [loaded, empty, pending, denied, error, unknown, responsive, localized]
- **Source applicability:** [standards edition, jurisdiction, limitations, review owner]
- **External implementation evidence:** [only if a consuming application independently supplies verified evidence]

## Readability, accessibility, performance and locale

Document navigation hierarchy, copy/error comprehension, accessible roles/names, keyboard/focus, screen-reader announcements, zoom, theme, contrast, touch, RTL and translation growth. Identify constrained device and large-dataset cases and performance measurement plan; no invented benchmark.

## Evidence

| Check | Status | Evidence |
| --- | --- | --- |
| Existing concept/synonym search | NOT VERIFIED | |
| Cross-context reuse rationale | NOT VERIFIED | |
| Contract/UX peer review | NOT VERIFIED | |
| Concept source, registry and link integrity | NOT VERIFIED | |
| Keyboard/AT and responsive testing | NOT VERIFIED | |
| Performance/readability review | NOT VERIFIED | |
| Agent retrieval regression | NOT VERIFIED | |

## Lifecycle, limitations, migration

Owner, version, review date, known unknowns, adoption constraints, compatibility policy and rollback plan. A **stable specification** does not certify the behavior of any product implementation; no executable code belongs in this repository. Link to [lifecycle policy](../governance/lifecycle-and-decisions.md) and [quality gates](../governance/quality-gates.md).
