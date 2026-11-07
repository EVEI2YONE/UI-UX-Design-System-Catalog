# Component contracts

**Kind:** contract · **Status:** proposed · **Primary layer:** components

## Purpose

A shared component needs a stable, inspectable contract before it is marked ready for cross-context adoption. This is a reusable **specification checklist**, not a coded component.

## Required contract

1. **Identity:** durable ID, name, role, owner, version, status, consumers, use/avoid.
2. **Anatomy:** slots, content hierarchy, variants/sizes, reasonable defaults and invalid combinations.
3. **States:** applicable default, hover, focus-visible, pressed/selected, disabled/readonly, loading, success, warning, error and empty states.
4. **Interaction:** pointer, keyboard, touch, focus lifecycle, Escape behavior, async feedback, validation and recovery.
5. **Content:** label semantics, truncation, long strings, localization/plurals, RTL, text growth and icon meaning.
6. **Styling:** semantic token dependencies, scoped styles, responsive layout, light/dark/high-contrast, reduced motion.
7. **Evidence:** examples/anti-patterns, unit/interaction/visual checks, known failures, compatibility and migration notes.

## Example: Dialog shell versus destructive task

**Shared Dialog contract:** role/modality, focus entry and containment as appropriate, Escape/close, focus return, accessible name and description, backdrop behavior, resize and scroll. Refer to the [WAI-ARIA Authoring Practices Guide](../governance/references.md) for tested interaction patterns.

**Account deletion flow (not shared Dialog contract):** account context, destructive action, confirmation copy, user-specific validation, service call, recovery alternatives, and domain metrics.

## Verification matrix starter

| Scenario | Behavior to verify | Result |
| --- | --- | --- |
| Keyboard only | All controls reachable and operable; focus visible | NOT VERIFIED |
| Short and translated labels | No essential truncation or overflow | NOT VERIFIED |
| Loading and error | Feedback, prevention of duplicate action, recovery | NOT VERIFIED |
| Zoom, narrow container, touch | Layout reflows; targets operable | NOT VERIFIED |
| Theme variants | Contrast and focus across applicable modes | NOT VERIFIED |

Use [the entry template](../templates/concept-entry.md) to record an actual component specification. Do not mark this sample matrix as tested.