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
- **Future candidate domains:** content design, data visualization, trust/privacy UX, platform adaptations, performance resilience, AI interaction patterns, and design-tool interoperability. Add these when a reusable need and owner are identified; do not create empty folders for them.

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
