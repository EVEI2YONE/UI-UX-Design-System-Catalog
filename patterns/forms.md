# Form composition and validation

**Kind:** specification · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Compose labeled controls into a task with understandable validation, submit, cancellation and recovery. **Use** for data entry workflows with multiple fields or steps. **Avoid** introducing a universal form component that contains product-specific business rules, network APIs or a proliferation of unrelated Boolean variants.

## Composition and ownership

Use [Field](../components/field/spec.md) for label, help and error associations; [Input](../components/input/spec.md), [Select](../components/select/spec.md), [Checkbox](../components/checkbox/spec.md) for input; [Button](../components/button/spec.md) for commands. A feature owns the form schema, authorization, validation policy, persistence, event instrumentation and service requests. Do not move server validation or routing into shared primitives.

## Task flow and states

| State | User-visible behavior | Acceptance observation |
| --- | --- | --- |
| Initial / partially entered | Persistent labels and optional help; values retained | Logical keyboard sequence and clear primary action |
| Client error | Explain corrections next to controls; optional summary links to errors | Errors programmatically associated; no color-only signaling |
| Pending submit | Preserve values and prevent accidental duplicate mutations | Meaningful progress with focus context retained |
| Server error / offline | State which data was saved and how to retry safely | No input loss; avoid retry when outcome is uncertain |
| Success / exit | Confirm persisted outcome, next step and safe cancellation path | Task can complete and resume appropriately |

For multi-step forms, label progress, preserve previous values, and clearly distinguish irreversible actions from routine Next/Back. Do not assume every form needs multiple steps or a blocking dialog.

## Responsive, theme, localization and accessibility

Allow long labels/errors to wrap and form columns to collapse without changing reading/focus order. Use semantic surface, error and focus tokens; check contrast in supported themes and reduced-motion behavior. Use locale-aware input hints and formatting, externalized messages, RTL-aware logical spacing and mixed-script data checks. Prefer native controls and document required, disabled and readonly semantics.

## Examples and verification

**Illustrative good:** A profile form keeps entered values when the server rejects one field; the error summary links to a labeled invalid field. **Anti-example:** A one-size-fits-all Form fetches user records internally and discards all fields on validation failure.

| Check | Status | Evidence needed |
| --- | --- | --- |
| Design/contract owner review | NOT VERIFIED | Consumer and validation ownership |
| Keyboard, errors, screen reader | NOT VERIFIED | Run with real fields and submit outcomes |
| Narrow/zoom, translation and RTL | NOT VERIFIED | Long strings, mixed direction |
| Async recovery and duplicate prevention | NOT VERIFIED | Timeout, retry, server error tests |

**Canonical ID:** `pattern.forms` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** consolidate repeated field/submit compositions while keeping task policy local. Documentation-only.

Related: [task flows](task-flows-and-information-architecture.md), [recovery](interaction-states-and-recovery.md), [accessibility](../guidance/accessibility.md), [measurement](../guidance/ux-measurement.md). Standards: [WCAG 2.2](../governance/references.md) and native platform semantics where applicable.
