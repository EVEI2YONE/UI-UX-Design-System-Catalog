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

## Example contract: asynchronous action button (illustrative)

- **Purpose:** initiate a non-navigation action; use a link for navigation.
- **Anatomy:** required accessible label, optional icon, focus treatment, optional progress indicator.
- **API decisions:** `variant` expresses meaning (primary/secondary/destructive), `size` expresses density, `disabled` prevents activation; `loading` communicates pending work. Keep invalid combinations documented rather than adding unrelated Boolean flags.
- **Interaction:** native `button` semantics where possible, Enter/Space activation, visible focus, no duplicate submission while pending, meaningful result/error feedback. Do not make a disabled control the only way to learn why a task is unavailable.
- **Presentation:** semantic action/focus/status tokens, content-sized layout, long-label wrapping, theme and reduced-motion behavior. Icons must not be the sole signal for destructive intent.

| State | Behavior | Verification target |
| --- | --- | --- |
| Idle | Action is available and named | Pointer, keyboard, assistive technology |
| Focus-visible | Focus indication is discernible | Tab navigation across themes |
| Pending | Repeat activation is prevented without losing task context | Async success/failure path |
| Failed | Error explains recovery; entered content retained | Screen reader and retry |
| Disabled | Reason discoverable from adjacent content where needed | Alternative instructions |

**Scope boundary:** the button does not own payment, account deletion, telemetry payloads, or network retries. A feature decides if retries are safe. Test a real implementation before marking any row PASS. Related: [interaction recovery](../patterns/interaction-states-and-recovery.md).

## Batch 12 extension — versioned design-to-code handoff

Every real implementation should be traceable to a versioned canonical component contract. Document these fields before treating a shared component as ready for consumers:

| Field | Required contract |
| --- | --- |
| Source and ownership | Canonical ID, design/spec revision, owner, affected consumers, approved usage |
| Semantics and API | Correct native role, props/slots, events, defaults, invalid combinations and focus lifecycle |
| Complete states | Focus, disabled, pending, error, success, empty, selected, destructive, long text and RTL where applicable |
| Design tokens | Semantic roles, optional component aliases, all relevant modes/themes, justified overrides |
| Layout and content | Content-driven responsive rules, zoom, translations, plural formats, logical directions |
| Integration boundaries | Network, authorization and product telemetry remain feature-owned |
| Test evidence | Actually observed interaction/AT tests, browser/device matrix, reproducible screenshot diffs and known gaps |
| Migration/release | Version/compatibility, consumer update, rollout, revert plan and responsible reviewers |

**Positive example (illustrative):** A shared Dialog contract describes opening/closing focus, modal background, validation and delayed actions. A screenshot test confirms visuals at a pinned viewport; a separate keyboard/screen-reader test validates behavior, and feature engineering verifies destructive request authorization.

**Anti-example:** An engineer guesses a new focus state from a design screenshot, updates golden images in bulk and assumes the component is semantically correct. Automated image diffs cannot prove focus or authorization.

This is a contract template, not a code implementation or a declared Storybook/Playwright dependency. Related: [quality gates](../governance/quality-gates.md), [tokens](../foundations/design-tokens-and-themes.md), [lifecycle policy](../governance/lifecycle-and-decisions.md). Sources (consulted 2026-11-07): [Storybook UI testing](https://storybook.js.org/docs/writing-tests/index), [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).
