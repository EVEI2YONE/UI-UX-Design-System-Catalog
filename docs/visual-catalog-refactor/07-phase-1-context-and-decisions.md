# 07 — Phase 1 context review, taxonomy and decision ledger

**Phase:** 1 — architecture and canonical contracts  
**Branch/PR:** `docs/visual-catalog-refactor-blueprint` / #16  
**Audit source:** target branch derived from `main` SHA `3b933abea778122dece31af7496f409028ed6198`  
**Status:** proposed architecture, not reviewed or approved; no runtime implementation

## Context gathered before modification

The actual repository has **53 registered canonical concepts**, `schema_version: 0.1.0`, and existing catalog `layer` values: `principles`, `foundations`, `tokens`, `components`, `experiences`, `behavior`, `cross-cutting`, `intelligence`, `patterns` and `context`. The registry schema defines additional possible layers, including `primitives`. **These values classify knowledge and need not map one-to-one to source folders or the site's visual tabs.** Phase 1 must not rename them in bulk.

Six specification owners already exist in `components/`: Button, Input, Select, Checkbox, Dialog and Field. These are proposed specifications, not runtime controls. Canonical owners for existing foundation, architecture, task patterns and settings-related experiences must be reused. Site-based visual examples have not been verified.

### Sources examined

| Source | Context and consequence |
| --- | --- |
| `catalog/index.json`, `catalog/schema.json` | Current identity layer and strict schema; defer additions to Phase 2 |
| `architecture/component-model.md` | Already defines foundations → primitives → components → patterns/features → pages; clarify feature reference distinction without wholesale rewrite |
| `architecture/component-contracts.md` | States, semantics, API, performance-related and evidence requirements; extend by reference, don't restate |
| `architecture/module-boundaries-and-developer-navigation.md` | Product feature/domain vs shared UI separation; keep no backend in site |
| `governance/lifecycle-and-decisions.md` | Reuse decision order, lifecycle, owner and evidence gates |
| `components/README.md` | Six controls and no executable implementation assertion |
| `patterns/account-and-settings-portal.md` | Extensive existing settings composition; don't create duplicate normative settings guidance |
| `patterns/agentic-actions-and-approvals.md` | Human/AI approval separation and consequences; generic human-review feature is not automatically identical to agentic tool approval |
| `patterns/data-tables.md`, `patterns/search-and-filter.md` | Data management task building blocks already addressed |
| `templates/concept-entry.md`, `AGENTS.md`, `CONTRIBUTING.md` | Existing canonical publication and retrieval rules |
| `docs/visual-catalog-refactor/01–06` | Prior architecture options, scope and single-PR execution plan |

## Catalog-first disposition

| Candidate | Existing owner / relevant canon | Decision | Why |
| --- | --- | --- | --- |
| Button/Input/Select/Checkbox/Dialog/Field | `component.*` existing specs | **Reuse** | Do not create a parallel primitive catalog |
| Generic form, navigation, data table, filtering | `pattern.forms`, `pattern.navigation`, `pattern.data-tables`, `pattern.search-filter` | **Compose / visualize** | Existing rules cover behaviors; site demos can show them |
| Settings center | `pattern.account-settings-portal` | **Extend/reference, don't duplicate** | Already unusually comprehensive account and settings source |
| Agentic approvals | `pattern.agentic-actions` | **Reuse where applicable** | Applies to agent delegated operations, not every human-admin decision |
| Generic human review workspace | `pattern.interaction-recovery`, `pattern.data-tables` and component contracts | **Candidate feature reference** | Cross-step decision/evidence/focus/uncertainty may justify a new example; register only after full spec |
| Data workspace | `pattern.data-tables`, `pattern.search-filter` | **Candidate feature reference** | No new table primitive needed |
| Dashboard, onboarding | Existing chart/UX and task-flow guidance | **Defer feature registration** | Not needed for first vertical slice |
| Website catalog shell, routes, preview runner | No executable site established in reviewed docs | **New site layer** | Site chrome is not canonical component guidance |

## Phase 1 taxonomy decision: two orthogonal axes

**Axis A — Knowledge classification (canonical registry):** existing `layer`, `kind` and durable `id` remain unchanged. A pattern currently classified as `experiences` stays in that layer; website tabs do not require bulk reclassification.

**Axis B — Executable representation (future site):** foundations; primitives; controls; composed patterns; feature references; product-specific application experiences **outside** the catalog. This classifies the **reference code that may demonstrate a concept**, not necessarily the concept's registry layer.

### Dependency and ownership rules

```text
Canonical knowledge (registry ID + Markdown)
  └── links -> optional executable reference
                  foundations + primitives
                       ↓
                    components
                       ↓
                 composed patterns
                       ↓
                 feature references
                       ↓
                consuming application
```

A feature reference may depend on components/patterns and synthetic adapters but **not** import a real consuming application API, permissions provider, points system, identity configuration or database. Core components never depend on a feature reference. Site browse/search chrome stays separate from cataloged working examples. The site renders source-controlled real implementations; it must never substitute a nonfunctional visual approximation.

## Decisions

| ID | Decision | Status | Rationale | Revisit trigger |
| --- | --- | --- | --- | --- |
| P1-D01 | Preserve canonical registry IDs, paths and current layers | Proposed | Avoid agent lookup regressions | Phase 2 schema requirements |
| P1-D02 | Maintain `components/*/spec.md` and `patterns/*.md` as normative owners | Proposed | Existing contracts are extensive | Evidence of duplicate/obsolete owner |
| P1-D03 | Add `features/README.md` as **classification/navigation only** | Proposed | Clarifies reusable feature vs app-specific page | Phase 7 feature spec |
| P1-D04 | Add an unregistered feature reference authoring template | Proposed | Makes completeness/adapter boundary explicit without false implementation status | Phase 7 pilot |
| P1-D05 | Use `site/src/implementations/` for executable examples, separate from site chrome | Proposed | One rendered source, no packages | Actual site build |
| P1-D06 | Keep app credentials, backend auth, domain mutations and persistence outside the site | Proposed | Safe and portable examples | Scope/security review |
| P1-D07 | Do not register speculative feature IDs or mark previews live | Proposed | No fabricated canon, no dead preview links | Reviewed spec + implementation |
| P1-D08 | Extend the existing component model by cross-link, not new ontology | Proposed | Keeps current source of truth | Explicit reviewer request |

## Open questions requiring follow-up, not invented answers

- Is the chosen site framework Next.js or a leaner static site stack? Phase 3 should decide using the site's actual requirements.
- Do preview examples need iframe isolation by default, or CSS/JS isolation with stronger sandboxing only for selected cases? Phase 4 risk assessment.
- Should a review workspace target general administrative decisions, AI-agent approval, or both? Phase 7 task scope and reuse analysis.
- What are the real hosting permissions, deployment posture, reviewers, supported locales and browser matrix? Phase 8/10.
- What baseline bundle/performance budgets and human retrieval success rates can be measured? Phase 8/9.

## Phase acceptance and evidence status

| Requirement | Result |
| --- | --- |
| Gather existing canonical model/registry/context first | Observed in GitHub reads |
| Classify without duplicates | Proposed classification documented; reviewer approval pending |
| Feature acceptance contract available | New template + feature README proposed |
| Registered IDs and schema unchanged in Phase 1 | Must verify in branch diff |
| Documentation/reference link integrity | To verify with available checks |
| Existing Python catalog validator/unit tests | NOT VERIFIED until executed |
| Manual/browser/assistive technology checks | NOT APPLICABLE to this docs-only phase; future implementation NOT VERIFIED |

**Phase gate:** request review of this ledger and the narrow architecture appendices; do not claim the taxonomy is approved because it is written.
