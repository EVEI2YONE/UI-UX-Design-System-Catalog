# Design foundations

This section defines consistent design decision-making before component-level styling. Start with [design principles](design-principles.md) to clarify hierarchy, signifiers and user tasks, then use [design tokens and themes](design-tokens-and-themes.md) to encode roles and variants.

- [Design principles](design-principles.md) — hierarchy, consistency, grouping, progressive disclosure, signifiers and recovery.
- [Visual design craftsmanship](visual-design-craftsmanship.md) — composition, typography, palette construction, spatial rhythm and art-direction briefs (KG-01–05); reference research, abstraction, direction exploration and tradeoff selection (KG-11–14).
- [Practical UI styling recipes](practical-ui-styling-recipes.md) — layouts, surfaces, imagery, interface archetypes and purposeful motion (KG-06–10).
- [Design tokens and themes](design-tokens-and-themes.md) — reference → semantic → component aliases, light/dark/high-contrast mappings and token hygiene.

Related: [component model](../architecture/component-model.md), [accessibility](../guidance/accessibility.md), and [quality gates](../governance/quality-gates.md).
**For agents:** resolve the registry IDs `principle.visual-hierarchy`, `foundation.visual-craftsmanship`, `foundation.practical-styling` and `foundation.design-tokens` using [the lookup registry](../catalog/index.json) before reading these canonical pages; see [AGENTS.md](../AGENTS.md).

**Batch 12 token delivery:** [Design tokens and themes](design-tokens-and-themes.md) now specifies versioned DTCG interchange, alias/theme checks, platform transforms and migration evidence. The 2025.10 format is a stable Community Group report, not a W3C Recommendation or evidence that a platform exporter is installed.


## Batch 9 — global CSS to semantic tokens

[Design tokens and themes](design-tokens-and-themes.md) now gives a staged selector, value and consumer migration plan for large global stylesheets, with compatibility and reflow checks. The [Batch 9 context ledger](../archive/planning/little-wins-batch-9-context-and-gap-ledger.md) documents the motivating source. No framework replacement or actual token export is claimed.

**Wireframe hierarchy (proposed B2):** [Design principles](design-principles.md) define context, content hierarchy and primary/secondary actions in a screen. Use [task flows](../patterns/task-flows-and-information-architecture.md) for structurally meaningful alternatives and evaluation, and [wireframe methodology](../guidance/wireframe-methodology.md) for fidelity.
