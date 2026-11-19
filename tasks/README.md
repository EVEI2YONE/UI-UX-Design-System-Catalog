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

Each task points to related components, content guidance and recovery rules. Choose a pattern after checking the actual context, risks, accessibility requirements and research evidence; a phrase match does not replace user research.
