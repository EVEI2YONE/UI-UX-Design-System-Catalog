# Reusable component specifications

These are **proposed, platform-neutral contracts**, not framework implementations or verified accessible components. Each directory has one canonical `spec.md` registered in [catalog/index.json](../catalog/index.json). Agent consumers should resolve the concept ID first, then read the specification and relevant dependencies.

| Component | Canonical ID | Decision supported |
| --- | --- | --- |
| [Button](button/spec.md) | `component.button` | Action versus navigation, loading and activation |
| [Input](input/spec.md) | `component.input` | Single-line entry, semantics and validation hooks |
| [Select](select/spec.md) | `component.select` | Bounded choices, native versus custom widget |
| [Checkbox](checkbox/spec.md) | `component.checkbox` | Independent choice and mixed selection |
| [Dialog](dialog/spec.md) | `component.dialog` | Modal shell, focus lifecycle and dismissal |
| [Field and error](field/spec.md) | `component.field` | Labels, help and error associations |

## Adoption and review

Start with [component boundaries](../architecture/component-model.md) and [contract guidelines](../architecture/component-contracts.md). Keep business validation, requests and product-specific modal flows outside these shared contracts. Review [accessibility](../guidance/accessibility.md), [i18n](../guidance/internationalization.md) and [interaction recovery](../patterns/interaction-states-and-recovery.md) for each implemented consumer.

All owners are **unassigned**, statuses **proposed**, and manual checks **NOT VERIFIED**. Do not advertise runnable components or checked WCAG conformance.


## Batch 7 — stateful native-dialog integration

The [Dialog contract](dialog/spec.md) now calls out focus/dismissal, stateful unsaved forms, confirmed async outcomes and fallback focus when the invoking record disappears. This extends its existing canonical ID; it does not certify an implementation. See [Batch 7 context ledger](../archive/planning/little-wins-batch-7-context-and-gap-ledger.md).

## Icon-bearing controls — Batch 1 (proposed)

Use [icon semantics](../foundations/iconography-and-semantics.md) to decide whether an icon is decorative, informative or attached to a named action. The existing [Button specification](button/spec.md) owns activation and pending/disabled states; use its icon-only action extension rather than creating a second icon button primitive. Source examples remain illustrative and require real keyboard, screen-reader and touch testing.

## B02 — coordinated component events (proposed)

Use the [component event ownership and composite anatomy contract](../architecture/component-contracts.md#batch-2--composite-anatomy-and-event-coordination-ckg-04-ckg-0608-proposed-2026-11-07) when composing Button, Field, Input, Select, Checkbox and Dialog with sibling views, contextual menus or collections. Each primitive emits meaningfully named events; the feature coordinates shared state and business commands. No existing base control is replaced by a new event wrapper.
