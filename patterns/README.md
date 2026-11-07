# Patterns and experiences

Patterns explain how multiple components support a task in context. Pages and user journeys are composed experiences, not replacements for reusable controls.

- [Task flows and information architecture](task-flows-and-information-architecture.md): navigation, progressive disclosure, wayfinding, task-first flow design.
- [Role-aware workspaces and context switching](role-aware-workspaces-and-context-switching.md): multiple authorized roles, workspace routing, customer previews, privileged impersonation boundaries.
- [Interaction states and recovery](interaction-states-and-recovery.md): loading, empty, error, offline, destructive actions, retry and focus recovery.

Related: [design principles](../foundations/design-principles.md), [accessibility](../guidance/accessibility.md), [measurement](../guidance/ux-measurement.md).

**Agent retrieval:** use `pattern.task-flows` for task/navigation design and `pattern.interaction-recovery` for error, pending and retry behavior. Read their canonical paths from [the registry](../catalog/index.json); follow `related` IDs for accessibility and metrics only as relevant. See [AGENTS.md](../AGENTS.md).
