# UI/UX Design System Catalog


> **Status:** proposal scaffold (v0.1.0). A catalog of reusable design knowledge, not a published UI component library or a claim of accessibility conformance.

**Purpose.** Make UI/UX decisions easy to find, explain, review, implement, and validate. The catalog is for designers, engineers, researchers, accessibility reviewers, product teams, and AI agents. Entries specify *why and when* to use a concept, *how* it affects components and product journeys, and *what evidence* is needed before adoption.

## Find the right guidance

| If you need to... | Start here |
| --- | --- |
| Deliver an end-to-end visual design from brief through styling, rendering, critique and evidence | [Visual craftsmanship workflow](governance/visual-craftsmanship-workflow.md) |
| Select wireframe fidelity or decide when interaction is required | [Wireframe methodology](guidance/wireframe-methodology.md) |
| Critique a rendered UI, iterate screenshots and study before/after styling examples | [Visual craftsmanship quality gates](governance/quality-gates.md#visual-craftsmanship-review-and-corrective-iteration--batch-4-kg-15-and-kg-16-proposed-2026-11-07) and [synthetic refinement examples](foundations/visual-refinement-examples.md) |
| Review image-based wireframe QA, states and consumer retrieval | [Quality gates](governance/quality-gates.md), [interaction recovery](patterns/interaction-states-and-recovery.md), [wireframe integration handoff](archive/planning/wireframe-integration-handoff-2026-11-07.md) |
| Gather visual references, compare art directions and select a style with documented tradeoffs | [Visual design craftsmanship — Batch 3](foundations/visual-design-craftsmanship.md#batch-3--art-direction-research-exploration-and-selection-kg-1114-proposed) |
| Choose a coherent aesthetic direction, typography, color and layout rhythm | [Visual design craftsmanship](foundations/visual-design-craftsmanship.md) |
| Apply layout, card, image, icon and motion styling recipes | [Practical UI styling recipes](foundations/practical-ui-styling-recipes.md) |
| Establish visual hierarchy, spacing, and affordances | [Design principles](foundations/design-principles.md) |
| Create a theme or rationalize raw values | [Tokens and themes](foundations/design-tokens-and-themes.md) |
| Choose prototype, MVP, growing or enterprise app code structure | [Application architecture selection](architecture/application-architecture.md) |
| Organize features, domains, and developer navigation | [Module boundaries and developer navigation](architecture/module-boundaries-and-developer-navigation.md) |
| Adapt app structure to Next.js, Angular or React Router | [Framework-aware application structure](architecture/framework-aware-application-structure.md) |
| Decide between monorepo, multirepo or microfrontends | [Enterprise and multi-app architecture](architecture/enterprise-and-multiapp.md) |
| Migrate or measure application modularity | [Architecture evolution and fitness](architecture/architecture-evolution.md) |
| Enforce feature/module import boundaries in CI | [Architecture enforcement and CI guardrails](architecture/architecture-enforcement-and-ci.md) |
| Explore prototype, MVP and enterprise code-layout examples | [Application architecture reference examples](architecture/application-architecture-reference-examples.md) |
| Decide primitive vs component vs pattern vs feature | [Component model](architecture/component-model.md) |
| Specify a new or changed reusable component | [Component contracts](architecture/component-contracts.md) and [entry template](templates/concept-entry.md) |
| Organize profile, security and personal preferences in a settings portal | [Account and settings portal](patterns/account-and-settings-portal.md) |
| Design billing details, subscription changes or invoices | [Billing and subscription settings](patterns/billing-and-subscription-settings.md) |
| Design role-based portals, previews or workspace switching | [Role-aware workspaces and context switching](patterns/role-aware-workspaces-and-context-switching.md) |
| Compose task-specific wireframe screens and compare structural alternatives | [Task flows and information architecture](patterns/task-flows-and-information-architecture.md) and [visual hierarchy](foundations/design-principles.md) |
| Simplify navigation or a critical task | [Task flows and information architecture](patterns/task-flows-and-information-architecture.md) |
| Design loading, error, or destructive states | [Interaction states and recovery](patterns/interaction-states-and-recovery.md) |
| Design and test keyboard, focus, contrast, touch, or zoom | [Accessibility](guidance/accessibility.md) |
| Support translations, long labels, and RTL | [Internationalization](guidance/internationalization.md) |
| Define success beyond aesthetic preference | [UX measurement](guidance/ux-measurement.md) |
| Write clear labels, instructions, error and status copy | [Content design and UX writing](guidance/content-design-and-ux-writing.md) |
| Design complex forms, safe search, filtering and sorting | [Form composition](patterns/forms.md) and [search/filtering](patterns/search-and-filter.md) |
| Recover a failed user task across service and support channels | [Service recovery and support handoff](patterns/service-recovery-and-support.md) |
| Choose a UX study or evaluate evidence quality | [UX research methods](guidance/ux-research-methods.md) |
| Understand expectations and end-to-end journeys | [Mental models and journey mapping](guidance/mental-models-and-journeys.md) |
| Reduce memory and decision burden | [Cognitive load and decision design](guidance/cognitive-load-and-decisions.md) |
| Design perceived speed, loading and field performance evidence | [Performance and perceived speed](guidance/performance-and-perceived-speed.md) |
| Design controlled A/B studies and trustworthy causal analysis | [UX experimentation](guidance/experimentation-and-causal-evidence.md) |
| Hand off design tokens and components for real releases | [Lifecycle and decisions](governance/lifecycle-and-decisions.md) and [component contracts](architecture/component-contracts.md) |
| Explain AI capabilities, uncertainty, evidence and correction | [AI-powered experiences](guidance/ai-powered-experiences-and-trust.md) |
| Design AI tools with scoped approval and verified outcomes | [Agentic actions and approvals](patterns/agentic-actions-and-approvals.md) |
| Support accessible voice, chat and multimodal workflows | [Conversational, voice and multimodal UX](patterns/conversational-voice-and-multimodal-ux.md) |
| Present accessible KPIs, charts and dashboard data | [Data visualization and dashboards](guidance/data-visualization-and-dashboards.md) |
| Adapt navigation and tasks for mobile/native windows | [Mobile and adaptive platform UX](guidance/mobile-and-adaptive-platform-ux.md) |
| Design bulk actions, drag alternatives, command palettes and undo | [Advanced interactions](patterns/advanced-interactions-and-reversible-actions.md) |
| Define enterprise approval and audit-view journeys | [Role-aware workspaces](patterns/role-aware-workspaces-and-context-switching.md) |
| Build privacy-respecting choices and account deletion flows | [Privacy, consent and trustworthy UX](guidance/privacy-consent-and-trust.md) |
| Plan sign-in, passkeys, MFA, expiry and recovery | [Authentication and account lifecycle](patterns/authentication-and-account-lifecycle.md) |
| Control alert urgency, channels, and user attention | [Notifications and attention](patterns/notifications-and-attention.md) |
| Handle offline drafts, sync and conflicting edits | [Offline work and synchronization](patterns/offline-sync-and-conflicts.md) |
| Reuse, extend, merge, deprecate, or review guidance | [Lifecycle and decisions](governance/lifecycle-and-decisions.md) and [quality gates](governance/quality-gates.md) |

**Search by word, synonym, or ID:** [`catalog/index.json`](catalog/index.json) is the canonical machine-readable lookup registry. See [lookup instructions](catalog/README.md). Example:

```bash
python3 scripts/find_concept.py "focus recovery"
python3 scripts/find_concept.py dialog
python3 scripts/find_concept.py --layer components
```

## Browse by domain

| Section | What lives there |
| --- | --- |
| [Foundations](foundations/README.md) | Principles, semantic tokens, theme architecture, visual rules |
| [Core components](components/README.md) | Proposed contracts for Button, Input, Select, Checkbox, Dialog and Field/Error |
| [Architecture](architecture/README.md) | Primitive/component/pattern boundaries, shared contracts |
| [Patterns](patterns/README.md) | IA, task flows, interaction states, recovery |
| [Guidance](guidance/README.md) | Accessibility, internationalization, research and metrics |
| [Governance](governance/README.md) | Decision policy, ownership, quality gates, references |
| [Templates](templates/README.md) | Standard entry format for expanding the catalog |
| [Catalog index](catalog/README.md) | Stable concept IDs, titles, aliases, domains, levels, status |

## How the concepts relate

This **conceptual 10-layer map** spans: (1) human/product context, (2) design principles, (3) interaction/behavior, (4) design tokens/themes, (5) design foundations, (6) primitives, (7) components, (8) patterns, (9) product experiences, and (10) experience intelligence. The layers organize *knowledge* and are **not a mandatory directory tree or strict engineering dependency order**.

Practical UI composition typically follows **foundations/tokens → primitives → components → patterns/features → pages and flows**. Accessibility, internationalization, governance, quality, and adoption apply **across** this structure. A reusable `Dialog` is a component; a delete-account dialog is a product-specific flow composed with that component.

## What is and is not included

- **Included:** guidance, contracts, reference patterns, decision rules, examples/anti-patterns, evidence expectations, and concept metadata.
- **Not included yet:** compiled tokens, framework-specific components, Storybook previews, product app code, or independently verified UX research. Do not mistake a specification for a working implementation.
- **Future candidate domains:** further platform-specific and product-derived gaps must be validated before adding duplicate concepts. Add these when a reusable need and owner are identified; do not create empty folders for them.

## How to use an entry

1. Search the registry by task or alias; follow its **canonical path**.
2. Read **when to use / avoid**, constraints, tradeoffs, and related concepts.
3. Decide **reuse / adapt / compose / create / deprecate** using [governance guidance](governance/lifecycle-and-decisions.md).
4. Record assumptions and verify accessibility, localization, responsive states, interactions, and task impact with [quality gates](governance/quality-gates.md).
5. Submit any catalog change through a reviewable PR following [CONTRIBUTING](CONTRIBUTING.md).

## Entry status and evidence

All initial concept entries are **`proposed`**, pending review. Valid lifecycle labels: `proposed`, `experimental`, `stable`, `deprecated`, `removed`. A `stable` **guideline** is still not evidence of a production-ready coded component. Tests not executed must be marked `NOT VERIFIED` rather than `PASS`.

## Maintain and validate

The standard library is sufficient; no package install is required:

```bash
python3 scripts/validate_catalog.py
```

The validator checks registered paths, IDs, titles, statuses, directory indexes and relative Markdown link targets. It cannot verify WCAG compliance, product quality, external website availability, or the claims inside prose.

## Sources and provenance

This proposal was derived from the supplied **UI/UX Design System Architect v1.1** instruction package (particularly the component, token, UX, accessibility, i18n, metrics, catalog, and governance guidance). It selectively translates reusable knowledge into catalog pages; operational agent instructions are not imported as design authority. External standards are linked in [References](governance/references.md) with dates and scope. See [Changelog](CHANGELOG.md) for release notes.

**Repository license:** not specified in the starting repository. Contributors should resolve licensing before distributing third-party code or assets; no license is implied by public visibility.

## Current maintenance and historical evidence

The [catalog registry](catalog/index.json) provides the current concept inventory (49 proposed entries at the 2026-11-07 baseline; the shared wireframe PR adds a proposed 50th entry). Do not treat counts in dated archival ledgers as present-day inventory. All canonical pages describe design knowledge rather than published components or verified application behavior.

Detailed batch progress, source audits, PR snapshots and product-specific case studies are preserved in [the historical archive](archive/README.md). The [changelog](CHANGELOG.md) records changes; [contributing](CONTRIBUTING.md) and [agent guidance](AGENTS.md) define the current operating workflow.

## Wireframe catalog integration (proposed PR #11)

The [B0–B7 cumulative handoff](archive/planning/wireframe-integration-handoff-2026-11-07.md) maps each gap to its canonical ID, current evidence and outstanding verification. The [synthetic example bank](archive/planning/wireframe-synthetic-example-bank-2026-11-07.md) is illustrative, not canonical guidance. Look up concepts through `catalog/index.json`; consumer agents must inspect the actual generated image and use a prototype or implementation for interaction/accessibility claims. No real images, user studies or runtime accessibility checks were performed for this documentation set: **NOT VERIFIED**.

## Support This Project

[![Support on Ko-fi](https://img.shields.io/badge/Support%20on-Ko--fi-13C3FF?logo=ko-fi&logoColor=white)](https://ko-fi.com/S5C12A839Y)

## Settings configuration knowledge (cumulative draft)

For workspace-scoped configuration contracts, server-side authorization, and safe save/recovery behavior, begin with [Account and settings portal — Batch 1](patterns/account-and-settings-portal.md#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07). Continue using [role-aware workspaces](patterns/role-aware-workspaces-and-context-switching.md) for authorization context and [forms](patterns/forms.md) for shared control behavior. This is proposed guidance, not a shipped Little Wins Settings page.

Settings Batch 2: [feature dependency disclosures and review-policy transitions](patterns/account-and-settings-portal.md#settings-knowledge-batch-2--feature-and-policy-configuration-proposed-2026-11-07) extend the existing settings portal; capability truth tables and paused-work recovery remain in their existing canonical patterns.

Settings Batch 3: [timezone/reporting configuration and personal preference scope](patterns/account-and-settings-portal.md#settings-knowledge-batch-3--time-and-personal-preferences-proposed-2026-11-07) reuse the canonical [theme system](foundations/design-tokens-and-themes.md) and [internationalization](guidance/internationalization.md) guidance. A selectable timezone is a product decision, not a shipped default.

Settings Batch 4: [configuration audit events, access and safe reversals](patterns/account-and-settings-portal.md#settings-knowledge-batch-4--configuration-governance-and-audit-proposed-2026-11-07) extend the existing settings portal. Privacy/retention and delegated-access rules remain with their canonical guidance.

**Settings knowledge Batches 1–5:** [closure, gap coverage and validation handoff](archive/planning/little-wins-settings-batches-1-5-closure-2026-11-07.md) records the eight-gap crosswalk, evidence limits, product decisions and outstanding tests. Read the [canonical settings portal](patterns/account-and-settings-portal.md) for reusable rules; the closure ledger is not an additional concept.

## Batch 1 — Icon semantics and accessible controls (proposed, 2026-11-07)

For an [icon intent registry, accessible icon-only action and state/target guidance](foundations/iconography-and-semantics.md), use `foundation.icon-semantics`. For appearance alone (stroke, optical sizing, icon and illustration craftsmanship), keep using `foundation.practical-styling`. The [Button contract](components/button/spec.md) specifies how its host activates and handles pending/disabled states. These are proposed knowledge specifications, not published UI assets.

## Batch 2 — component events and coordination (proposed, 2026-11-07)

The [canonical component contract](architecture/component-contracts.md#batch-2--composite-anatomy-and-event-coordination-ckg-04-ckg-0608-proposed-2026-11-07) now covers host/slot ownership, local events versus feature commands versus domain outcomes, sibling coordination, controlled state and nested-interaction pitfalls. Retrieve `architecture.component-contracts`; do not infer an implemented component library or measured behavior.

## Batch 3 — state and sequential workflow handoffs (proposed, 2026-11-07)

For icon/status timing and focus when a selected item is updated or removed, see [interaction recovery](patterns/interaction-states-and-recovery.md) (`pattern.interaction-recovery`). For stable actions and selecting the next eligible task only after an authoritative outcome, see [task flows](patterns/task-flows-and-information-architecture.md) (`pattern.task-flows`). These are proposed contracts, not measured reductions in pointer travel or an implemented review controller.

## Batch 4 — action choice and interaction-cost evidence (proposed, 2026-11-07)

See [advanced interactions](patterns/advanced-interactions-and-reversible-actions.md) for when to prefer explicit Buttons, toolbars, overflow, split actions, shortcuts or confirmations (`pattern.advanced-interactions`); use [UX measurement](guidance/ux-measurement.md) for input-specific effort measures and task-success guardrails (`guidance.ux-measurement`). Both extend existing proposed concepts, not a new packaged component or validated efficiency improvement.

## Batch 5 — styling architecture and reuse inventory (proposed, 2026-11-07)

Use [practical styling](foundations/practical-ui-styling-recipes.md) (`foundation.practical-styling`) for utility-first styling ownership, [architecture enforcement](architecture/architecture-enforcement-and-ci.md) (`architecture.enforcement-ci`) for baseline-aware CSS/variant drift checks, and [component model](architecture/component-model.md) (`architecture.component-model`) for component inventory-to-contract mapping. These extend three existing concepts; no packaged Tailwind theme, automated code linter or product accessibility result is claimed.

## Batch 6 — icon consistency, interaction verification and discovery (proposed, 2026-11-07)

Use [icon semantics](foundations/iconography-and-semantics.md) for icon-intent collision and consistency review (CKG-05), and [quality gates](governance/quality-gates.md) for real interaction-state test scenarios and task-based canonical retrieval (CKG-18/19). The shared B01–B06 branch adds catalog guidance and regression tests only; human review, actual browser accessibility, user outcomes and production adoption require separate evidence.

## Visual catalog refactor proposal (2026-11-08)

The [visual catalog documentation pack](docs/visual-catalog-refactor/README.md) proposes an embedded reference website with real interactive component and feature examples, backed by the existing canonical registry and Markdown guidance. It includes a [folder and file blueprint](docs/visual-catalog-refactor/01-folder-file-blueprint.md), [concept backlog](docs/visual-catalog-refactor/02-concepts-and-content-plan.md), [knowledge-gap audit](docs/visual-catalog-refactor/03-knowledge-gap-audit.md), [agent search compatibility contract](docs/visual-catalog-refactor/04-registry-agent-discovery.md), [preview quality gates](docs/visual-catalog-refactor/05-preview-quality-contracts.md), and [migration roadmap](docs/visual-catalog-refactor/06-migration-pr-roadmap.md). Those six documents preserve the original *planning baseline*. Phases 3–9 now add a local static site with 12 source-linked interactive reference examples, audited through CI. The references are not published packages, live product integrations or a deployed public service.

## Local visual catalog site (Phase 3, 2026-11-08)

A working **static catalog browser** now lives under [site/](site/README.md). It generates browsable pages directly from the existing Markdown and canonical registry, with responsive layouts, client-enhanced search and a clear **Specification only** fallback for entries without an implementation. To build locally, run `python3 site/build.py`; serve the generated `site/dist/` from its root using `python3 -m http.server 8000 --directory site/dist`. This is **not yet a deployed website**. Phases 4–7 added actual source-linked interactive previews for six core controls, five composed patterns and one synthetic Review Workspace; these are reference examples, not production-ready packages or real business integrations. Review the [Phase 3 evidence ledger](docs/visual-catalog-refactor/09-phase-3-site-foundation.md) for CI results and unverified browser accessibility/performance checks.

## Current visual catalog and agent discovery (Phases 3–9, 2026-11-08)

The source-derived site and lookup registry share **54** canonical concepts: **12** real, sandboxed interactive references (6 controls, 5 patterns, 1 Review Workspace) and **42** specification-only entries. No concept review status has been promoted from `proposed`, and no public deployment is claimed. See [site build and preview guidance](site/README.md).

- For people: build and serve `site/dist/` locally; browse by category or task, open a canonical guidance page and inspect the registered source/preview. The website is generated from Markdown and `catalog/index.json` rather than a second source of identity.
- For AI agents: run `python3 scripts/find_concept.py "human approval queue" --json`, read the canonical `path`, then inspect optional source/scenarios when they exist. Review `avoid_when` and real evidence rather than treating rank as an endorsement.
- For maintainers: run `python3 scripts/audit_discovery.py --output site/artifacts/phase9/discovery-audit.json`, the root/site tests and the GitHub Actions Chromium quality workflow. This records retrieval and provenance without editing the ranker or duplicating the registry.

The [Phase 9 discovery and governance handoff](docs/visual-catalog-refactor/15-phase-9-agent-governance-handoff.md), [agent protocol](AGENTS.md) and [contribution guide](CONTRIBUTING.md) describe ownership, traceability, known retrieval gaps, adoption boundaries and release checks. **Manual screen-reader, comprehensive keyboard, zoom/RTL, screenshot visual review, real product integration, security signoff and field Web Vitals remain unverified.** Phase 10 documented a **NO-GO for release** until those decisions receive named approvals; see the [Phase 10 release readiness review](docs/visual-catalog-refactor/16-phase-10-release-readiness.md) before marking [draft PR #16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16) ready for final review.

## Preserved concept candidates (post-Phase-10 knowledge follow-up)

The [durable concept inventory and decision ledger](docs/visual-catalog-refactor/17-concept-inventory-and-decisions.md) explicitly tracks all five proposed Stage 3 feature concepts and five Stage 2 composition ideas, including [nine individual unregistered concept briefs](docs/visual-catalog-refactor/concepts/decision-manifest.json) and the implemented Review Workspace specification. Deferred candidates are recorded **without** allocating new `catalog/index.json` IDs or implying human approval. The ledger separately reassesses all 12 original knowledge gaps as implemented, partly verified, already covered or still open.
