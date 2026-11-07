# UI/UX Design System Catalog

> **Status:** proposal scaffold (v0.1.0). A catalog of reusable design knowledge, not a published UI component library or a claim of accessibility conformance.

**Purpose.** Make UI/UX decisions easy to find, explain, review, implement, and validate. The catalog is for designers, engineers, researchers, accessibility reviewers, product teams, and AI agents. Entries specify *why and when* to use a concept, *how* it affects components and product journeys, and *what evidence* is needed before adoption.

## Find the right guidance

| If you need to... | Start here |
| --- | --- |
| Select wireframe fidelity or decide when interaction is required | [Wireframe methodology](guidance/wireframe-methodology.md) |
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
