# Find UI/UX guidance by user task

Choose the user's problem before choosing a component. The [task index](index.json) contains discoverability phrases and pointers to **canonical** concept IDs, not duplicated normative instructions. Task cards are rendered at `/tasks/` by the frontend shell.

## Supported tasks

| User goal | Primary concept |
| --- | --- |
| Narrow a long list | [Search and filtering](../specifications/patterns/search-and-filter.md) |
| Compare records quickly | [Data tables](../specifications/patterns/data-tables.md) |
| Find a way forward from an empty screen | [Interaction recovery](../specifications/patterns/interaction-states-and-recovery.md) |
| Complete a form in the right order | [Form composition](../specifications/patterns/forms.md) |
| Recover from a failed submission | [Form validation](../specifications/patterns/forms.md) |
| Submit something consequential | [Task flows](../specifications/patterns/task-flows-and-information-architecture.md) |
| Confirm an irreversible action | [Dialog](../specifications/components/dialog/spec.md) |

| Select or create multiple category tags | [Content taxonomy](../knowledge/guidance/content-architecture-and-taxonomy.md) |
| Manage an item from a card | [Collection views](../specifications/patterns/collection-and-feed-views.md) |
| Archive versus delete a record | [Reversible actions](../specifications/patterns/advanced-interactions-and-reversible-actions.md) |
| Save a dependent item without losing form state | [Component contracts](../knowledge/architecture/component-contracts.md) |
| Manage related records from a collection card | [Master-detail](../specifications/patterns/master-detail-exploration.md) |
| Drill down from a KPI card | [Data visualization](../knowledge/guidance/data-visualization-and-dashboards.md) |

| Edit a related record without nested dialogs | [Master-detail task surfaces](../specifications/patterns/master-detail-exploration.md#choose-one-task-surface-across-detail-edit-and-history) |

Each task points to related components, content guidance and recovery rules. Choose a pattern after checking the actual context, risks, accessibility requirements and research evidence; a phrase match does not replace user research.
