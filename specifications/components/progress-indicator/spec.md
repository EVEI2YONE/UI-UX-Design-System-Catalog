# Progress indicator

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Communicate how a known task advances, including when progress is measurable and when only activity or stage is known. A visible animation or completed bar must never substitute for an authoritative operation outcome.

**Use when:** A task has a meaningful waiting period, distinct stages or a measurable portion of work remaining.

**Avoid when:** A value represents a static score (use a meter), a brief action needs only an unobtrusive status label, or a fake percentage would imply unavailable precision.

**Ownership:** The component owns progress presentation, label, value semantics, accessible description and visual variants. The pattern or feature owns real progress data, cancellation, retry, readiness and confirmed completion.

## Decision framework and variants

| Variant | Fit | Required behavior | Main risk |
| --- | --- | --- | --- |
| Determinate | Known task extent and valid numerator/denominator | Show current value relative to finite min/max; ensure visual and accessible values match. | Never infer percentage from elapsed animation time. |
| Indeterminate | A task is running but its total work is unknown | Show status and appropriately indeterminate semantics; omit a fabricated current value. | Do not make it look precisely 50% complete. |
| Stage-based | Discrete steps are known, but time or effort per step differs | Name current step and count only when the full set is actually known. | Never equate completing a step with persisted success. |
| Segmented or multi-job | Independent units have meaningful subtasks | Expose clear labels and whether values can be combined. | Avoid averaging differently weighted tasks without explanation. |
| Completed / failed / paused | Operation reports a verifiable terminal or paused outcome | Separate bar appearance from success/error message and next action. | Never call 100% upload processed when server validation remains. |

## Component contract

- Choose native HTML progress semantics when available; custom progressbar roles need a stable accessible name and truthful min/max/current states.
- Use values only for measured progress. For indeterminate progress omit a numeric value rather than inventing a percent or ETA.
- Do not misuse progressbar for a static measurement; a meter is a different semantic role and should express a known range instead.
- When a unit is not naturally a percentage, expose a coherent units label or value text; do not show contradictory numbers in adjacent text and ARIA.
- Use the feature's actual completion state to determine success or failure. Transfer progress, server processing and final confirmation may require separate stages.
- Do not automatically focus a progress display. Prefer a concise status region for important stage changes; avoid announcing continuous small updates.
- Offer cancellation only if supported and clarify what Cancel stops, including any already running or irreversible work.

## States and semantics

| State | Visible presentation | Programmatic / interaction expectation |
| --- | --- | --- |
| Not started | No misleading active progress animation | Label and status reflect inactivity |
| Active determinate | Stable track, fill and readable value | Accessible current/min/max and contextual name |
| Active indeterminate | Active status with no artificial numeric value | Accessible indefinite progress indication and optional status |
| Paused or stalled | Explicit reason/last update, next step when known | Distinct from loading and failure |
| Failed or cancelled | Explanation and supported recovery; do not display success | Focus stays on meaningful task context |
| Complete | Explicit confirmed outcome and next action | Announce completion once when it matters |

## Keyboard, focus, accessibility and localization

- The indicator itself normally does not need Tab focus; use labeled status text and accessible progress semantics rather than placing focus on decoration.
- Keyboard users must reach genuine Cancel/Retry buttons separately, with associated operation names and safe focus return.
- Do not use rapidly changing live regions; important transitions can be announced with a single concise status rather than every numeric tick.

Use semantic tokens for focus, surfaces, text and state, and distinguish meaning beyond color or movement. Validate long translated labels, bidi/RTL content, 200–400% zoom/reflow, high contrast, touch access and reduced motion for the chosen variant. Actual native support and custom assistive-technology behavior must be tested, not inferred from markup alone.

## Example and anti-example

**Illustrative example:** A media import shows 60% of bytes transferred, then 'Validating files' with unknown duration, then 'Import complete' only after server confirmation.

**Anti-example:** An animated bar counts to 100% regardless of response, announces success and disables retry while server processing is still unresolved.

## Evidence and verification

| Scenario | Required observation | Status |
| --- | --- | --- |
| Determinate versus indeterminate semantic value with screen readers | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| Correct units, reduced-motion visuals, stale and cancelled task states | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| Failure/unknown reconciliation with actual service and duplicate activation | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| High contrast, long localized status, RTL, zoom and no focus theft | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |

This document defines a proposed conceptual contract. It does not supply executable source, an independently reviewed design, validated production behavior or accessibility certification.

## Sources, applicability and related concepts

- [HTML progress element](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element) — normative or reference context; verify which behavior applies to the chosen native/custom implementation.
- [WAI-ARIA Progressbar pattern](https://www.w3.org/WAI/ARIA/apg/patterns/progressbar/) — normative or reference context; verify which behavior applies to the chosen native/custom implementation.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — normative or reference context; verify which behavior applies to the chosen native/custom implementation.
- Related canonical sources: [Interaction states and recovery](../../patterns/interaction-states-and-recovery.md), [Data export and background jobs](../../patterns/data-export-and-background-jobs.md), [File upload](../../patterns/file-upload-and-attachments.md), [Accessibility](../../../knowledge/guidance/accessibility.md).
- **Scope limit:** Product data, permission enforcement, persistence and backend lifecycle remain feature-owned, not component-owned.
