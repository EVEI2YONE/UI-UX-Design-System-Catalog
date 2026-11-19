# Accessibility

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose

Accessibility is a design and delivery requirement, not a visual polish phase. Use [WCAG 2.2 AA](../../governance/references.md) as the default applicable **web target** and WAI-ARIA APG for complex widgets; native semantic HTML is preferable where it meets the task. Do not claim conformance without scenario-specific evidence.

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

Automated checks alone cannot establish accessibility compliance. Treat blockers in core flows as release-significant. Related: [component contracts](../architecture/component-contracts.md) and [interaction states](../../specifications/patterns/interaction-states-and-recovery.md).

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

Use [WCAG 2.2](../../governance/references.md) for the precise normative success criteria and exceptions rather than turning these scenario descriptions into invented numeric thresholds. Mark each check `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` with reason; do not claim blanket compliance from an empty scan.

## Connected journey evidence, not isolated controls

Audit **entry -> record action -> modal/form -> validation or submission -> updated list -> resumed focus** as one continuous task. Check that a keyboard user can reach every step and can identify where they are after an item disappears, scope changes or a modal closes. Prefer native buttons/links in table action cells and genuine `<dialog>` semantics; avoid turning a whole `<tr>` into a pseudo-button when a discrete control conveys the action clearly.

Capture actual focus destinations, screen-reader announcements, keyboard activation (including Space for buttons), unexpected draft loss, background operability, Escape/cancel behavior, and change-of-context communication. Separate source-observed semantics from tested failure: a suspicious pattern is an audit candidate, **not** automatic proof of WCAG failure. Use [data tables](../../specifications/patterns/data-tables.md) and the [dialog contract](../../specifications/components/dialog/spec.md) for the canonical ownership details. No Little Wins runtime accessibility verification was performed in this guidance.

## Inclusive wireframe stress review

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

Record the target standard/scope per product (for web, evaluate applicable [WCAG 2.2](https://www.w3.org/TR/WCAG22/) criteria; for native, use relevant platform expectations). Document product-specific exclusions with rationale rather than silently asserting `NOT APPLICABLE`. This guidance does not certify a screenshot or product. Related: [adaptive composition](mobile-and-adaptive-platform-ux.md), [internationalization](internationalization.md), [wireframe methodology](wireframe-methodology.md) and [quality gates](../../governance/quality-gates.md).

## Documentation browser versus consuming-product verification

The catalog website is a **static knowledge browser**, not a runnable component gallery or proof of product accessibility. Apply the appropriate check to the surface being evaluated; a Markdown or build pass cannot establish WCAG conformance in an unrelated application.

| Surface | What can be verified | What it does **not** establish |
| --- | --- | --- |
| Catalog source and generated pages | Canonical links, headings, semantic navigation, search/filter interaction, keyboard navigation, reflow and contrast **of the browser itself** | Behavior of a proposed Button, Dialog, workflow, account setting or other consuming-product implementation |
| Static design, wireframe or written component contract | Intended task order, accessible labels, state coverage, expected focus transitions and test criteria | Runtime focus, actual screen-reader speech, service outcomes or device adaptation |
| Implemented component in a consuming product | Names, roles, values, focus order/return, keyboard/touch equivalence, errors, zoom, RTL and contrast in actual supported states | Completeness of an end-to-end journey, authorization or backend correctness without integration checks |
| Connected user journey | Entry through confirmation/recovery and resumption, including permissions, session changes, failure and data preservation | Universal compliance outside tested browsers, assistive technologies and contexts |

### Task-based accessibility acceptance scenarios

Select relevant rows for each real product; mark results with device, browser, OS, assistive technology, scenario and reviewer. The entries below are **test plans**, not executed results.

| Scenario | Observable acceptance | Failure/recovery expectation |
| --- | --- | --- |
| First action and navigation | Landmarks and headings orient the user; actionable names describe destinations; keyboard order follows task meaning | Focus stays visible and no essential action requires a gesture |
| Loading, error and retry | Pending, invalid, confirmed and unknown outcomes have truthful status; errors identify affected fields and corrections | Preserve entered data, prevent unsafe duplicate activation and provide a recoverable next step |
| Dialog or composite interaction | Keyboard model matches native semantics or the relevant WAI-ARIA APG pattern; opening and closing focus are predictable | Return focus to a meaningful surviving destination; no keyboard trap |
| Empty, filtered empty and permission-denied states | Different causes and available actions are distinguishable without color alone | Offer a meaningful reset, request or explanation without misleading authorization claims |
| Themes, zoom and text expansion | Measure effective contrast in supported modes, focus visibility, reflow and 200%/400% zoom where applicable | Do not clip actions or infer compliance from semantic token names |
| Language, RTL and motion preferences | Meaningful order, localized labels, bidirectional text, translated expansion, reduced motion and forced colors work in scope | Keep essential feedback available without animation or a particular visual direction |

For web, determine applicable [WCAG 2.2](https://www.w3.org/TR/WCAG22/) success criteria, including exceptions: normal text contrast is generally 4.5:1, large text 3:1 and applicable non-text UI/graphics 3:1. WCAG 2.2 **Focus Not Obscured (Minimum)** (2.4.11) is AA; **Focus Appearance** (2.4.13) is AAA. Use the [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) for complex widget interaction patterns while preferring native semantics when sufficient. These references define expectations, not an automatic pass.

### Evidence and performance boundaries

For the catalog browser, record source revision, route, viewport/zoom, browser/OS, input method, automated-scan scope, manual observations and actual failures. Automated axe-type checks cover only evaluated rules and states. For a product, additionally record its implementation revision and assistive-technology versions; do not reuse the catalog browser's test result as product evidence.

Keep **static bundle size**, **lab rendering**, **field Web Vitals** and **task completion** separate. A stylesheet-size budget is not LCP/INP/CLS evidence. Measure in context and use [web.dev's current Web Vitals definitions](https://web.dev/articles/vitals) when applicable; report cohorts, units, percentile, environment and sampling limitations. Never substitute illustrative source examples for measured performance.

**Record template:** concept ID; consuming product (or catalog browser); scenario/state; expected versus observed result; theme, locale and viewport; input/assistive technology; method/tool/version; date; owner; evidence link; severity; disposition. Use `PASS`, `FAIL`, `NOT VERIFIED` or `NOT APPLICABLE` with a reason. A proposed contract remains proposed until independently reviewed; the existence of this checklist is not a completed evaluation.

## Applying this guidance: decision and evidence check

**Representative decision to evaluate:** Carry out keyboard, screen-reader, reflow, theme and RTL checks on a real consuming journey; record browser, assistive technology, product version and results. Define the intended cohort and task, initial conditions, competing option, observable user outcome and relevant accessibility, language and privacy constraints. Keep assumed behavior separate from user evidence; examples are illustrative unless results are directly recorded.

**Acceptance record:** Name the selected research or audit method, eligible population, task and metric denominator where applicable, observed versus expected outcome, source version and unresolved validity limitations. Do not treat a worked example as a completed study. For web accessibility only, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) gives relevant criteria; it cannot validate a UX hypothesis or provide a product baseline.

