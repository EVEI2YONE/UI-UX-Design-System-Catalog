# File upload and attachment workflows

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Safely select, inspect, validate and submit files while preserving user understanding of transfer progress, storage status and retryable failures.

**Use when:** A task needs one or multiple documents, images or other attachments to complete an action.

**Avoid when:** A server-side import pipeline, public publishing flow or asset management product requires a separate feature contract in addition to this baseline.

**Ownership:** The pattern defines client-side file selection and user-facing lifecycle; consuming apps own storage, malware checks, format restrictions, authorization, resumability and retention.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Select | Offer visible file picker and optional drop zone | Keyboard-equivalent selection and descriptive requirements |
| Review | Show filename, type, size and safe removal/replacement | Clarify order and per-file limits |
| Transfer | Show queued/uploading/progress separately from uploaded | No false success before server confirmation |
| Validate | Explain rejected types, limits, safety checks and partial success | Keep unrelated valid attachments |
| Recover/submit | Retry idempotently where safe, remove stale items and continue | Clarify if file is attached to final submission |

## Design decisions

- Choose filenames and structured text rather than relying on thumbnails, icon color or hover.
- Provide accessible browse input; drag-and-drop must never be the only upload path.
- Distinguish bytes transferred from server scanning/processing and final attachment acceptance.
- Avoid duplicate uploads on reconnection; document how partially uploaded files are cleaned up and whether users can cancel.
- Do not promise confidentiality, security scanning or deletion based solely on client UI state.

## Inclusive operation, content, theming and locale

Keep each stage reachable by keyboard and screen reader with understandable headings, action labels, error associations and focus continuation. Make destructive or irreversible effects explicit; use semantic status tokens rather than color alone. Check content-driven reflow, long translation strings, RTL and locale-specific formats, high contrast, reduced motion, narrow devices and interrupted network states. Separate simulated UI from verified service behavior.

## Example and anti-example

**Illustrative example:** An expense form attaches three receipts, reports one oversized file, retains the other two and offers a correctable retry.

**Anti-example:** A progress bar reaches 100%, immediately announces all files saved, then silently loses the upload during server validation.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| File picker, drag alternative, remove/replace, multiple files | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Timeout, partial acceptance, duplicate retry and cancelled upload | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Screen reader progress, long names, mobile/RTL and privacy language | Record observed result, applicable cohort and environment | NOT VERIFIED |

Primary outcome: task success on the full journey, with errors, recovery and abandonment measured using explicit denominators. Research baselines and product usage are unknown; no human study, backend integration or accessibility compliance is claimed.

## Sources, related concepts and limitations

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual source, not evidence that this workflow has been tested.
- [HTML file input](https://html.spec.whatwg.org/multipage/input.html#file-upload-state-%28type=file%29) — contextual source, not evidence that this workflow has been tested.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), [UX measurement](../../knowledge/guidance/ux-measurement.md) and [Content design](../../knowledge/guidance/content-design-and-ux-writing.md).
- Follow product-specific legal, privacy, security and lifecycle constraints; this is a reusable reference pattern, not a production service.
