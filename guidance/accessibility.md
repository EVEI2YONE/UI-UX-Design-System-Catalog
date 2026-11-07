# Accessibility

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose

Accessibility is a design and delivery requirement, not a visual polish phase. Use [WCAG 2.2 AA](../governance/references.md) as the default applicable **web target** and WAI-ARIA APG for complex widgets; native semantic HTML is preferable where it meets the task. Do not claim conformance without scenario-specific evidence.

## Contract

- **Semantics:** real buttons/links, descriptive names, headings and landmarks, labels and errors linked to fields.
- **Keyboard and focus:** reachable actions, logical order, visible focus; documented Escape and dialog focus entry/return.
- **Visual and touch:** contrast, reflow/zoom, text readability, non-color-only indicators, forgiving targets and accessible gesture alternatives.
- **Motion and feedback:** reduced-motion preferences, restrained animation, appropriate announcements for async completion and errors.
- **Robustness:** verify disabled, error, loading, narrow screen and translated-label states; high contrast and different input methods.

## Minimum evidence

| Check | Method | Initial status |
| --- | --- | --- |
| Automated issues | Lint / axe-type scan | NOT VERIFIED |
| Keyboard-only critical flow | Manual | NOT VERIFIED |
| Zoom/reflow and touch | Manual | NOT VERIFIED |
| Screen reader announcements | Manual spot check | NOT VERIFIED |
| Theme contrast and focus | Manual/automated | NOT VERIFIED |
| Long translated labels and RTL when applicable | Manual/pseudolocalized | NOT VERIFIED |

Automated checks alone cannot establish accessibility compliance. Treat blockers in core flows as release-significant. Related: [component contracts](../architecture/component-contracts.md) and [interaction states](../patterns/interaction-states-and-recovery.md).

## Component acceptance scenarios

For each *implemented* critical task, document the assistive technology/input combination, browser/viewport, expected behavior, actual result, severity, owner, and retest. Automated scans detect subsets of issues; manual keyboard, screen-reader and zoom checks are still required.

| Scenario | Acceptance expectation | Evidence to record |
| --- | --- | --- |
| Keyboard from entry to completion | All necessary actions operable, focus visible, sensible sequence | Focus path and blocked step |
| Error and correction | Invalid control named, error associated, recovery works without losing input | Accessibility tree/announcement observation |
| Modal open and close | Name and modality correct, focus enters, background unavailable when modal, focus returns sensibly | Entry and exit focus targets |
| Zoom and narrow layout | Essential content and actions remain usable without two-dimensional page scrolling where WCAG requires reflow | Zoom level, viewport, screenshot and exceptions |
| Touch and alternatives | Targets/spacing meet applicable criteria; gestures have alternatives | Device/input and target behavior |
| Motion and themes | Reduced-motion preference honored; focus and status distinguishable | Mode, preference and contrast measurements |

Use [WCAG 2.2](../governance/references.md) for the precise normative success criteria and exceptions rather than turning these scenario descriptions into invented numeric thresholds. Mark each check `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` with reason; do not claim blanket compliance from an empty scan.


## Batch 7 — connected journey evidence, not isolated controls (2026-11-07)

Audit **entry -> record action -> modal/form -> validation or submission -> updated list -> resumed focus** as one continuous task. Check that a keyboard user can reach every step and can identify where they are after an item disappears, scope changes or a modal closes. Prefer native buttons/links in table action cells and genuine `<dialog>` semantics; avoid turning a whole `<tr>` into a pseudo-button when a discrete control conveys the action clearly.

Capture actual focus destinations, screen-reader announcements, keyboard activation (including Space for buttons), unexpected draft loss, background operability, Escape/cancel behavior, and change-of-context communication. Separate source-observed semantics from tested failure: a suspicious pattern is an audit candidate, **not** automatic proof of WCAG failure. Use [data tables](../patterns/data-tables.md) and the [dialog contract](../components/dialog/spec.md) for the canonical ownership details. No Little Wins runtime accessibility verification was performed in this batch.


## Inclusive wireframe stress review (proposed Batch 4, 2026-11-07)

A static wireframe may record *intended* reading order, focus sequence, labels, error association, target discoverability and reflow; it cannot demonstrate native semantics, screen-reader output, touch activation or a WCAG pass. Distinguish **VISUALLY DEPICTED**, **ANNOTATED INTENT**, **NOT SHOWN**, and **IMPLEMENTATION TEST NOT VERIFIED** in every handoff.

**Use when:** reviewing compact, zoomed, translated or state-rich wireframe compositions before prototype escalation. **Avoid when:** checking contrast in a generated screenshot is taken to establish conformance, or annotation replaces manual testing of a live control.

| Inclusive stress case | Wireframe evidence | Actual acceptance still requires |
| --- | --- | --- |
| Zoom / reflow / narrow reading | Stacked order, essential text and actions remain visible in representative compositions | Browser at required zoom/reflow settings and real DOM content |
| Keyboard / focus / dialogs | Numbered *proposed* focus route, initial/return focus intent, safe exit and status target | Keyboard-only and screen-reader interaction with a prototype or product |
| Long labels / error text | Untruncated instructions and actionable recovery copy at representative expanded lengths | Rendering with actual font metrics and translated content |
| Touch and non-pointer access | Visibly discoverable actions, labels for icon-only buttons and gesture alternatives | Target sizing, touch/keyboard/switch behavior on actual implementation |
| Color, contrast and status | Status has legible text, shape/icon or language rather than color alone | Measured contrast and assistive announcement verification |

**Synthetic example:** A compact form mock shows a two-line submit label and inline error with a callout “Intended: announce validation errors and focus summary.” That callout is an interaction **requirement**, not evidence that the behavior works. **Anti-example:** a mock's green badge says “WCAG AA passed” without semantics, measured contrast, assistive tech or keyboard tests.

Record the target standard/scope per product (for web, evaluate applicable [WCAG 2.2](https://www.w3.org/TR/WCAG22/) criteria; for native, use relevant platform expectations). Document product-specific exclusions with rationale rather than silently asserting `NOT APPLICABLE`. This guidance does not certify a screenshot or product. Related: [adaptive composition](mobile-and-adaptive-platform-ux.md), [internationalization](internationalization.md), [wireframe methodology](wireframe-methodology.md) and [quality gates](../governance/quality-gates.md).
