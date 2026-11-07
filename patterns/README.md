# Patterns and experiences

Patterns explain how multiple components support a task in context. Pages and user journeys are composed experiences, not replacements for reusable controls.

- [Task flows and information architecture](task-flows-and-information-architecture.md): navigation, progressive disclosure, wayfinding, task-first flow design.
- [Role-aware workspaces and context switching](role-aware-workspaces-and-context-switching.md): multiple authorized roles, workspace routing, customer previews, privileged impersonation boundaries.
- [Interaction states and recovery](interaction-states-and-recovery.md): loading, empty, error, offline, destructive actions, retry and focus recovery.

Related: [design principles](../foundations/design-principles.md), [accessibility](../guidance/accessibility.md), [measurement](../guidance/ux-measurement.md).

**Agent retrieval:** use `pattern.task-flows` for task/navigation design and `pattern.interaction-recovery` for error, pending and retry behavior. Read their canonical paths from [the registry](../catalog/index.json); follow `related` IDs for accessibility and metrics only as relevant. See [AGENTS.md](../AGENTS.md).

## Batch 5 composed patterns

These are **proposed composition specifications**, not runtime implementations. Start with the canonical IDs in [the registry](../catalog/index.json), then follow dependency contracts.

- [Form composition and validation](forms.md) — `pattern.forms`, fields, validation, async submit and recovery
- [Navigation and wayfinding](navigation.md) — `pattern.navigation`, active routes, landmarks, deep links and keyboard menus
- [Search and filtering](search-and-filter.md) — `pattern.search-filter`, queries, selected filters, no-results and failed requests
- [Data tables and collection actions](data-tables.md) — `pattern.data-tables`, semantics, sorting, selection and pagination
- [Feedback and status messaging](feedback.md) — `pattern.feedback`, banners, inline status, transient notices and announcements

Use the existing [task-flow](task-flows-and-information-architecture.md) and [interaction-recovery](interaction-states-and-recovery.md) guidance as the shared decision layer rather than copying it into every pattern.
