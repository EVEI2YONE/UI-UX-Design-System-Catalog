# Input

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

A single-line editable field for short text and appropriately typed values. **Use** when the user needs to enter or edit a concise value. **Avoid** for paragraphs (use a textarea), mutually exclusive known options (consider Select/radios) or hidden business logic disguised as input.

## Ownership and contract

Input owns native editing semantics, focus, value/disabled/readonly presentation, label and description associations, and error-state hooks. A consuming Field can compose labels and messages; feature code owns validation rules, submission and server calls. Illustrative API: `id`, `name`, `value`, `onChange`, `type`, `autocomplete`, `required`, `readOnly`, `disabled`, `aria-describedby`/error linkage. Prefer native input types that accurately reflect the data and input method.

| State | Behavior | Verification |
| --- | --- | --- |
| Empty and filled | Show value without depending on placeholder as sole label | Accessible name and persistent visible label |
| Focus | Preserve caret and visible indicator | Keyboard navigation and zoom |
| Invalid | Identify actionable correction and link error to control | Screen-reader label/error and focus |
| Readonly | Content remains perceivable without editing | Distinguish from disabled |
| Disabled / pending | Unavailable state remains understandable | Do not silently discard user entry |

**Invalid combinations:** Error messages must not reference absent IDs; `readonly` is not a substitute for `disabled`; placeholder text must not be the only field name.

## Tokens, responsiveness and localization

Use text, surface, border, error and focus semantic tokens. Accommodate autofill, long values, zoom/reflow, mobile keyboards and translation growth in labels/errors. Direction-sensitive text input (for example numbers or mixed-script identifiers) must be tested rather than globally reversed in RTL contexts.

## Example and anti-example

**Illustrative:** An email input has a persistent label, appropriate autocomplete, a linked correction message and preserved value on server error. **Anti-example:** The placeholder "Email" disappears on typing and a red border is the only error indicator.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Contract and design review | NOT VERIFIED | Owner unassigned |
| Native keyboard/editing behavior | NOT VERIFIED | Requires real browser/platform |
| Error announcement and translated text | NOT VERIFIED | Requires implementation |
| Autofill/zoom/RTL/theme tests | NOT VERIFIED | Consumer-specific |

**Canonical ID:** `component.input` · **Owner:** unassigned · **Review date:** not reviewed

Related: [Field and error](../field/spec.md), [component contracts](../../../knowledge/architecture/component-contracts.md), [accessibility](../../../knowledge/guidance/accessibility.md), [internationalization](../../../knowledge/guidance/internationalization.md). Primary standards starting point: [WCAG 2.2](../../../governance/references.md).

## Decision scenario, evidence and acceptance

**Decision:** Use a native typed input for concise values; use Select for bounded known options and Textarea for multiline content. Field owns label and error composition.

**Illustrative scenario (not a completed study):** Enter a long name with an IME, receive validation only after composition commits, correct it and resubmit without erased valid text or displaced caret.

**Acceptance:** Verify composition events, keyboard editing, label and error associations, long translations, zoom/reflow and RTL text direction in the consuming form. Record the environment, owner, expected/actual results and evidence links; until executed, runtime outcomes remain **NOT VERIFIED**.

**Source scope:** [Applicable reference](https://www.w3.org/WAI/tutorials/forms/validation/) informs the design decision. WAI covers accessible errors; a real IME/browser test is still necessary. A reference is not proof of adoption, conformance or an independent review.

