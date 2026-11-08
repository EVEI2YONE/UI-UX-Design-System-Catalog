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


## Reference-state accessibility, theme and performance acceptance matrix

This matrix specializes the existing accessibility contract for a **source-linked visual catalog**. It is normative *guidance for verification*, not evidence that all reference scenarios pass. The live examples run under a restricted iframe and use in-memory fixtures; automated axe results address only configured rules and tested states.

| Scenario / mode | Semantics and interaction | Evidence to collect | Failure handling |
| --- | --- | --- | --- |
| Default interactive state | Native role/name/value, visible labels, focus order matching visual task | Accessibility tree, keyboard walkthrough, contrast sampling | Repair wrong accessible name/role before adding custom ARIA |
| Loading/pending | State accurately announced once; duplicate action blocked without losing orientation | Speech output and repeated-key test; whether focus remains findable | Preserve inputs; do not announce success early |
| Invalid input and known error | Programmatic field association, actionable error summary, focused recovery point | Keyboard entry, screen reader announcement and corrected resubmit | Keep entered values, don't move focus to hidden fields |
| Empty and no matches | Differentiate zero records from filtered zero results and connectivity errors | Screen reader headings/status, filter count, reset path | Provide reversible next step |
| Permission denied/readonly | Semantics distinguish actual readonly from unavailable controls | Keyboard inspection with unavailable action and explanation | Never imply a visual control is a server permission check |
| Unknown outcome | Explicitly unconfirmed result; no blind retry; status verification action when available | Human walkthrough of lost acknowledgement and focus | Preserve context and require authoritative reconciliation |
| Dialog/opening menu | Focus moves into content, Escape/close contract, focus returns to a meaningful surviving trigger | Keyboard-only and NVDA/VoiceOver observed sequences | Avoid focus to detached elements and keyboard traps |
| Light/dark/contrast modes | Text, nontext components, focus rings and errors contrast appropriately in each mode | Measured color pairs and visual screenshots in each mode | Don't infer contrast from color token names |
| Reflow/text growth | 320 CSS-pixel equivalent without lost functionality; exceptions for legitimately two-dimensional tables | 200% and 400% zoom, line wrapping, 320/375 CSS-pixel checks, long labels | Allow logical scrolling within actual tables, not whole-page horizontal scrolling |
| RTL/mixed direction | Logical reading/navigation order and nonmirrored data or logos | Arabic/Hebrew-like long text and LTR number/code samples, focus order | Change logical CSS and direction-aware icons, not every symbol |
| Reduced motion/forced colors | No animation-only status, system colors preserved, no invisible action outline | Operating-system preference and forced-colors screenshots | Keep visible focus and meaningful status without motion |

### Theme and token verification procedure

A semantic token role is not proof that its foreground/background combination meets contrast requirements. Test actual rendered foreground against its effective background for each mode and interactive state, including focus and disabled explanatory text. For WCAG 2.2 AA, normal text generally needs 4.5:1, large text 3:1, and many meaningful nontext UI boundaries/graphics 3:1; inspect applicable exceptions in the criterion before asserting pass. Test on both the catalog chrome and iframe content because their theme inheritance is distinct. Record token pair, resolved CSS values, surface/state, measurement method, browser, date and reviewer.

Choose an explicit theme state policy: changing a theme should not silently remount a form and erase edits; expose the active mode and retain meaningful selected state. If a future standalone token playground is proposed, register it only with a real source file, deterministic mode/state scenarios and contrast/test evidence. The current theme dropdown on previews does **not** by itself demonstrate a reusable token tooling product.

### Performance measurement and evidence boundary

Separate **build payload size** (local file bytes), **lab rendering** (device/network/throttling), **field Web Vitals** (real users), and **task outcome** (time to complete a meaningful action). Label each measurement's environment, units, tool, median/percentile and scenario. A passing 32 KiB stylesheet cap, 8 KiB search script cap or 64 KiB reference resource cap is a static budget, not LCP/INP/CLS evidence.

For a planned public deployment, collect 75th-percentile field LCP, INP and CLS by appropriate page cohort, with consent/privacy-safe instrumentation and sufficient samples. Use the then-current Core Web Vitals definitions and good/needs-improvement thresholds from [web.dev](https://web.dev/articles/vitals); do not extrapolate synthetic localhost results. For source previews, also measure selection and confirmation latency under a bounded many-record fixture; record if a long table, Markdown source inspector or synchronous render causes noticeable interaction delay. Do not define an arbitrary "good" interaction budget without measurement context.

### Manual review record template

Record **reference ID / scenario / theme / viewport and zoom / browser and OS / assistive technology and version / input method / expected result / observed result / severity / reviewer / date / evidence link / disposition**. Use `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` with reason. Submit one record per meaningful failed scenario, not one blanket pass for twelve references. Automated axe scan coverage must be listed separately from manual results.

**Standards and provenance:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) covers reflow (1.4.10) and focus not obscured (2.4.11); focus appearance (2.4.13) is AAA, not part of an unqualified AA claim. [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) provides patterns, not authorization for nonsemantic widgets. [Design Tokens Community Group 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) is a final *Community Group* report, not a W3C Recommendation; token exchange compliance does not demonstrate UI accessibility.

**Evidence state:** the checklist is now **documented**; a human-reviewed matrix and deployed performance remain **NOT VERIFIED**. The [gap work record](../docs/visual-catalog-refactor/gap-work/kg07-accessibility-performance.md) owns the remaining evidence.
