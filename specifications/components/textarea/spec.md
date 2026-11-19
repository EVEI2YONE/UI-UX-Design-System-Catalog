# Textarea and long-form input

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Collect multi-line text with appropriate affordances for length, editing, persistence and validation.

**Use when:** The task requires paragraphs, notes, explanations or another value that needs line breaks.

**Avoid when:** Short structured values suit Input, or a rich editor would introduce unjustified formatting complexity.

## Ownership and decision rules

Textarea owns editing semantics, label/help/error association, resize behavior and value reporting; consuming features own autosave, content policy, limits and submission.

- Use native textarea semantics and a persistent visible label; specify expected content instead of using placeholder as sole guidance.
- When a length limit applies, explain it before the user reaches it; report counters or errors without announcing every keystroke.
- Allow vertical resizing or content growth, including when translation and zoom increase the content; avoid fixed-height clipping.
- For drafts or autosave, distinguish locally edited, saving, saved, failed and conflict states. Do not clear typed text on rejection.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Empty / populated | Multi-line editing, line breaks preserved | Accessible label and description |
| Focus / composing | Caret and IME composition stay stable | No disruptive rerender |
| Too long / invalid | Explain correction and preserve text | Associated error and possible count status |
| Saving / failed | Report authoritative persistence outcome | No false saved claim |

## Keyboard, focus and inclusive operation

- Native Enter adds a line break; do not hijack it for submission unless a clearly documented alternative exists.
- Tab normally leaves the control; keyboard shortcuts must not block text editing or assistive technology.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** A review form asks for a reason in a labeled multi-line textarea and retains the text after a failed submission.

**Anti-example:** Using an expanding single-line input that clips written content or clears it after a network timeout.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| IME composition, paste, long content, resize and zoom | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Error association, optional counter announcement and draft failure | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| RTL, long translations, mobile keyboard and screen reader | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://html.spec.whatwg.org/multipage/form-elements.html#the-textarea-element); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.

## Decision example and verification boundary

**Illustrative scenario (not a user study):** Write a long multilingual draft, lose network access during autosave, reconnect and reconcile without silent data loss. The consumer owns product data and permissions; the shared specification owns semantic behavior, presentation and focus. Choose simpler native controls where they satisfy the user task.

**Acceptance evidence to collect:** Check textarea growth, caret position, save states, conflict warning, keyboard and translated content. Record tool/browser, owner, expected versus observed behavior, locale and unresolved cases; actual runtime results remain **NOT VERIFIED** until executed.

**Source applicability:** [Relevant W3C guidance](https://www.w3.org/WAI/tutorials/forms/) informs the interaction choices, not production conformance or independent review. Keep implementation-specific details with the consumer.

