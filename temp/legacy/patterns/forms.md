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

## Batch 8 extension — complex forms and data entry

### Plan the input before composing fields

Start from a user task, the minimum information truly needed and why each answer is required. Avoid collecting information simply because a database column exists. Separate **optional**, **required**, **conditional**, **prefilled**, and **review-only** information; explain unknowns and consent before asking for sensitive values. Prefer a single flow when short and understandable; split into steps only when meaningful groups, interruption risk or review needs justify extra navigation.

| Design choice | Decision rule | Test |
| --- | --- | --- |
| Field and format | Select input behavior matching real data; show units and realistic examples, accept harmless format variation | Localized entry, paste, screen reader and autofill |
| Validation timing | Avoid interrupting typing. Validate on submit by default; use post-field or inline checks where immediate feedback helps and does not create anxiety or conflict | Correcting a field never loses cursor focus or data |
| Error summary | For multi-field submit failures, expose a page-level summary linking to invalid fields plus linked inline messages; make focus behavior and announcements explicit | Keyboard and screen reader can find each error |
| Multi-step progress | Explain current step, overall scope if known, and safe back/edit/cancel | Back and browser history preserve entries |
| Save and resume | Communicate whether values are saved, where they are stored, expiry if known, and what happens across devices or sessions | Close/reopen, signed-out, offline and expired session |
| Pre-fill/autofill | Use standard autocomplete purposes, user-visible review and correction; never assume prefilled personal details remain correct | Correct with keyboard and translated labels |
| Final review | Expose consequential details and correction links before irreversible submission; server confirms outcome | Transaction status and duplicate-submit behavior |
| Retry after uncertainty | Confirm server state before repeating a potentially non-idempotent action | Simulate lost response after completed mutation |

**Example (illustrative):** An address application is split into Contact → Address → Review only if a study shows the grouping helps. Saved values remain available when users navigate backward; “Review” clearly distinguishes a draft from a submitted request.

**Anti-example:** A six-step wizard silently auto-saves nothing but displays “Saved” at each step, then resets all values after a timeout.

### Submission error semantics and copy

- Distinguish input validation errors (specific correction) from service failures (status and safe retry); [service recovery](service-recovery-and-support.md) governs escalation beyond the current task.
- Link errors to [Field and error](../components/field/spec.md) semantics. For longer forms or multiple invalid fields use navigable summary links and preserve all input. Avoid duplicate or endlessly repeating live announcements.
- Say what can be corrected and how, not just “Invalid value.” Do not expose private account, permissions or eligibility information through validation text.
- Product constraints may justify different validation timing; document rationale and test against the users and devices involved.
- Where supported, provide copy that is accurate for every state: **Not submitted**, **Saving draft**, **Draft saved**, **Submission pending**, **Submitted**, or **Status unknown**. Never claim persistence without confirmation.

### Form QA scenarios

1. Empty submit, a single incorrect field, multiple incorrect fields and correction after returning from error summary.
2. Keyboard-only, screen-reader navigation, 200% text and narrow/400% reflow as applicable to supported web targets.
3. Long localized copy, locale-specific date/number formatting, mixed LTR/RTL data, autofill and paste.
4. Browser back/forward, interrupted connection, expired session, repeated button activation, and partial/missing server response.
5. Review and cancel before an irreversible operation, plus actual persisted-status verification.

**Sources (reviewed 2026-11-07):** [GOV.UK recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) and [Error summary](https://design-system.service.gov.uk/components/error-summary/) present a UK public-service reference pattern, not an unconditional prescription for every product; [W3C WAI form instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) and [Validating input](https://www.w3.org/WAI/tutorials/forms/validation/) describe accessible input guidance. Server-side validation remains essential for integrity/security.
Related content: [content design](../guidance/content-design-and-ux-writing.md).

## Phase 6 executable pattern reference (2026-11-08)

The visual catalog now includes an actual [Form composition implementation](../site/src/implementations/patterns/form/Form.js), its [deterministic synthetic scenarios](../site/src/implementations/patterns/form/scenarios.js), and [scoped demonstration styles](../site/src/implementations/patterns/form/Form.css). The executable source used by the sandboxed preview is displayed verbatim in the site's source inspector. This is a **reference demonstration**, not a product backend, a verified end-to-end integration or a published package. Canonical review status remains `proposed`. Actual keyboard/AT behavior, responsive visuals, localization, measured performance and authoritative service integration are **NOT VERIFIED** by the Node/Python source tests. See the [Phase 6 evidence ledger](../docs/visual-catalog-refactor/12-phase-6-composed-patterns.md).
