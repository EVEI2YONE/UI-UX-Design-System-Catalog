# UI/UX Design System Catalog

> **Status:** proposal scaffold (v0.1.0). A catalog of reusable design knowledge, not a published UI component library or a claim of accessibility conformance.

**Purpose.** Make UI/UX decisions easy to find, explain, review, implement, and validate. The catalog is for designers, engineers, researchers, accessibility reviewers, product teams, and AI agents. Entries specify *why and when* to use a concept, *how* it affects components and product journeys, and *what evidence* is needed before adoption.

## Find the right guidance

| If you need to... | Start here |
| --- | --- |
| Establish visual hierarchy, spacing, and affordances | [Design principles](foundations/design-principles.md) |
| Create a theme or rationalize raw values | [Tokens and themes](foundations/design-tokens-and-themes.md) |
| Decide primitive vs component vs pattern vs feature | [Component model](architecture/component-model.md) |
| Specify a new or changed reusable component | [Component contracts](architecture/component-contracts.md) and [entry template](templates/concept-entry.md) |
| Design role-based portals, previews or workspace switching | [Role-aware workspaces and context switching](patterns/role-aware-workspaces-and-context-switching.md) |
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

## Definition batches (proposal)

The scaffold is being expanded in reviewable **documentation batches**, each using the existing canonical IDs rather than introducing placeholder component implementations:

1. **Foundations and architecture:** [design principles](foundations/design-principles.md), [token authoring](foundations/design-tokens-and-themes.md), [component model](architecture/component-model.md), and [component contracts](architecture/component-contracts.md).
2. **Flows and inclusive behavior:** [task flows](patterns/task-flows-and-information-architecture.md), [recovery states](patterns/interaction-states-and-recovery.md), [accessibility](guidance/accessibility.md), and [internationalization](guidance/internationalization.md).
3. **Measurement and governance:** [UX measurement](guidance/ux-measurement.md), [lifecycle](governance/lifecycle-and-decisions.md), and [quality gates](governance/quality-gates.md).

These are **proposed guidance definitions**. Component implementations, manual accessibility testing and user research remain outside this PR.

## Agent-first lookup

Agents should begin with [AGENTS.md](AGENTS.md), query [the canonical registry](catalog/index.json) with the [lookup tool](scripts/find_concept.py), then open only the relevant source pages. The [catalog schema](catalog/schema.json) defines optional retrieval metadata. IDs, status and source paths remain canonical; no published component implementations are implied.

**Batch 2 agent lookup:** [Patterns](patterns/README.md) and [cross-cutting guidance](guidance/README.md) now expose task-flow, recovery, accessibility and localization canonical IDs through the same registry. These remain proposed guidance, not verified product implementations.

**Batch 3 agent lookup:** [UX measurement](guidance/ux-measurement.md) and [governance](governance/README.md) now expose metrics, lifecycle and quality-gate concepts through the same registry. Retrieval metadata is present for all three scaffold-definition batches; the separately documented role-aware workspace entry remains unchanged.

## Batch 4 — core component contracts

Find individually retrievable proposed specifications for [Button, Input, Select, Checkbox, Dialog and Field/Error](components/README.md). They extend the existing architecture guidance, include state and inclusive-design checks, and are **not** implemented packages or tested components.

## Batch 5 — composed patterns

[Forms, navigation, search/filtering, data tables and feedback](patterns/README.md) now have canonical, agent-retrievable pattern specifications. These compose the [Batch 4 component contracts](components/README.md) and existing guidance without becoming product-specific feature implementations. All remain proposed and unverified on real user interfaces.

## Batch 6 — agent catalog maturity

The [agent lookup protocol](AGENTS.md), [catalog registry](catalog/README.md), [validation script](scripts/validate_catalog.py) and [governance rules](governance/lifecycle-and-decisions.md) now cover complete lookup metadata, deterministic retrieval, cross-references and dependency cycles for all registered concepts. No concept was automatically promoted from `proposed`, and documentation validation is not product accessibility certification.

## Batch 7 — research and product understanding (proposed)

[UX research methods](guidance/ux-research-methods.md), [mental models and journey mapping](guidance/mental-models-and-journeys.md), and [cognitive load](guidance/cognitive-load-and-decisions.md) add evidence-led research and task-design guidance. All three are `proposed`, not user-validated findings or implemented components. The [batch plan](planning/knowledge-expansion-batches-7-12.md) records the expansion scope.

## Batch 8 — content, discovery and task completion (proposed)

[Content design and UX writing](guidance/content-design-and-ux-writing.md) and [service recovery and support handoff](patterns/service-recovery-and-support.md) are new proposed catalog guidance. Existing [form](patterns/forms.md) and [search/filter](patterns/search-and-filter.md) specifications now include complex data entry, validation, save/resume, facets, sorting, pagination and recovery. No production code, real-user studies or manual accessibility verification are implied. This content follows Batch 7 on the cumulative knowledge-expansion branch and PR #5.

## Batch 9 — trust and resilient journeys (proposed)

[Privacy, consent and trustworthy UX](guidance/privacy-consent-and-trust.md), [authentication and account lifecycle](patterns/authentication-and-account-lifecycle.md), [notifications and attention management](patterns/notifications-and-attention.md), and [offline synchronization and conflict recovery](patterns/offline-sync-and-conflicts.md) are four new **proposed** guidance entries. Reuse the existing [role-aware](patterns/role-aware-workspaces-and-context-switching.md), [feedback](patterns/feedback.md), and [interaction-recovery](patterns/interaction-states-and-recovery.md) patterns instead of duplicating those contracts. The [Batch 9 context and gap ledger](planning/batch-9-context-and-gap-ledger.md) records evidence and decisions. No production code, compliance, or test claims are made.

## Batch 10 — dense and platform-specific interfaces (proposed)

New [data visualization](guidance/data-visualization-and-dashboards.md), [mobile/adaptive UX](guidance/mobile-and-adaptive-platform-ux.md) and [advanced interaction](patterns/advanced-interactions-and-reversible-actions.md) guidance complements expanded [data tables](patterns/data-tables.md) and [role-aware workspaces](patterns/role-aware-workspaces-and-context-switching.md). The [context and gap ledger](planning/batch-10-context-and-gap-ledger.md) explains reuse decisions and research references. These are proposed docs, not tested components or verified product performance.

## Batch 11 — AI and multimodal experiences (proposed)

New [AI-powered experiences](guidance/ai-powered-experiences-and-trust.md), [agentic actions and approvals](patterns/agentic-actions-and-approvals.md), and [conversational/voice/multimodal](patterns/conversational-voice-and-multimodal-ux.md) guidance separates generated outputs from verified evidence, tool plans from completed actions, and speech capture from confirmed user intent. The [context and gap ledger](planning/batch-11-context-and-gap-ledger.md) records existing concept boundaries and source limitations. These are proposed documents, not a deployed assistant, implemented authorization mechanism, or real-user/voice-accessibility test.

## Batch 12 — evaluation, performance and delivery (proposed)

New [performance and perceived speed](guidance/performance-and-perceived-speed.md) and [UX experimentation](guidance/experimentation-and-causal-evidence.md) guidance complements expanded [UX measurement](guidance/ux-measurement.md), [quality gates](governance/quality-gates.md), [catalog lifecycle](governance/lifecycle-and-decisions.md), [component handoff](architecture/component-contracts.md), and [design-token interchange](foundations/design-tokens-and-themes.md). The [context-first gap ledger](planning/batch-12-context-and-gap-ledger.md) separates current source guidance from real product evidence. This concludes planned Batches 7–12 on cumulative draft PR #5; all newly added concepts are still proposed and require human review before any merge.


## Little Wins knowledge-gap batches (proposed, 2026-11-07)

A source-based review of a Sites-hosted, owner-operated contribution-tracking pilot identified reusable extensions to **existing** catalog IDs, without introducing a second component taxonomy or new login requirement:

1. [Authentication and account lifecycle](patterns/authentication-and-account-lifecycle.md) — inventory host identity before recommending new sign-in.
2. [Role-aware workspaces](patterns/role-aware-workspaces-and-context-switching.md) and [interaction recovery](patterns/interaction-states-and-recovery.md) — managed profiles, human review versions, point/reward outcomes.
3. [Quality gates](governance/quality-gates.md) — negative authorization, concurrency, replay, and runtime validation.
4. [Task flows](patterns/task-flows-and-information-architecture.md) and [UX measurement](guidance/ux-measurement.md) — group/project scope, optional features, collaboration measures.
5. [Agent lookup protocol](AGENTS.md) — evidence-first retrieval and correction/regression prevention.

These are documentation proposals only. They do not certify a Sites deployment, imply individual member accounts, or verify a production application. No catalog IDs or registry schema are added because canonical guidance already exists.


## Batch 6 — data lifecycle and migration safety (proposed, 2026-11-07)

For archive/retention and trustworthy export/delete journeys, start with [privacy and consent](guidance/privacy-consent-and-trust.md). For revisioned aggregate migrations, concurrent edits and restoration, follow [offline/sync/conflicts](patterns/offline-sync-and-conflicts.md). [Quality gates](governance/quality-gates.md) documents verification scenarios. The [Batch 6 context and gap ledger](planning/little-wins-batch-6-context-and-gap-ledger.md) traces source evidence, limitations and reuse decisions. These are extensions of canonical IDs, not shipped exports, restored backups or new components.


## Batch 7 — accessible record-action journeys (proposed, 2026-11-07)

For actionable record lists, read [data tables](patterns/data-tables.md) before making an entire row keyboard-focusable. Use the [Dialog component contract](components/dialog/spec.md) for native dialog focus, dismissal, unsaved edits and completion; test the end-to-end route through [accessibility](guidance/accessibility.md) and [quality gates](governance/quality-gates.md). See the [Batch 7 evidence ledger](planning/little-wins-batch-7-context-and-gap-ledger.md). These are proposed checks, not proof of Little Wins WCAG conformance.


## Batch 8 — capability dependencies and safe feature toggles (proposed, 2026-11-07)

For independently stored settings with dependent actions, use [task-flow capability matrices](patterns/task-flows-and-information-architecture.md), [paused-state recovery](patterns/interaction-states-and-recovery.md), and [configuration quality gates](governance/quality-gates.md). The [Batch 8 context and gap ledger](planning/little-wins-batch-8-context-and-gap-ledger.md) documents Little Wins' points/rewards/challenges behavior and unresolved policy questions. No product flags or permissions were implemented; no runtime behavior was verified.


## Batch 9 — safe component and styling modernization (proposed, 2026-11-07)

For large route modules and partially adopted UI libraries, follow the [component model's incremental extraction guidance](architecture/component-model.md), [design-token/global-CSS migration guidance](foundations/design-tokens-and-themes.md) and [quality gates](governance/quality-gates.md). The [Batch 9 source/gap ledger](planning/little-wins-batch-9-context-and-gap-ledger.md) explains Little Wins' page, existing UI controls and stylesheet evidence. No component implementation, source code refactor or new catalog ID is included.


## Batch 10 — knowledge coverage and lookup regression closure (proposed, 2026-11-07)

The [cross-batch coverage and validation ledger](planning/little-wins-batch-10-context-and-gap-ledger.md) maps all ten Little Wins-derived documentation batches to existing canonical IDs, evidence boundaries and unresolved product tests. The [canonical registry](catalog/index.json) now includes task-oriented aliases for hosted identity, human review, feature dependencies, data migrations, table actions and styling migration. [Lookup regression tests](tests/test_little_wins_knowledge_coverage.py) exercise these searches. No new concept IDs or product implementation were introduced, and passing catalog CI does not certify Little Wins UX or security.

## Application code architecture (proposed, Batch 13)

For **how to structure an application repository**, rather than the catalog itself, start with [application architecture selection](architecture/application-architecture.md). Compare prototype, MVP, growing modular product and multi-application profiles using actual team/domain/change evidence. The [component model](architecture/component-model.md) continues to own UI component tiers; the [architecture index](architecture/README.md) links both. Guidance is proposed, not an audited app implementation.
