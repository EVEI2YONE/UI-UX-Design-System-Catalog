# Synthetic wireframe cases and retrieval regression bank — Batch 6

**Status:** proposed reference examples for PR #11, 2026-11-07. **Non-canonical fixture document:** guidance continues to live at the IDs below, not in this archive. This is not a production screenshot set, actual user research, or a benchmark of generated images. All actors, tasks, data and interface labels below are **ILLUSTRATIVE**, unless explicitly stated otherwise.

## How to use these cases

For each task, retrieve the expected concept by ID/alias from [the registry](../../catalog/index.json), read its [canonical page](../../AGENTS.md), then combine related constraints only as needed. Run the positive and negative checks with the companion Python regression tests. A lookup PASS means **registry routing** worked; it does not prove that a generated design is correct. A human must still inspect images using `governance.quality`, test interaction through a prototype where necessary, and label unverified product claims.

| Case | User task (synthetic) | Primary canonical owner | Positive expectation | Negative / boundary expectation |
| --- | --- | --- | --- | --- |
| WRF-01 fidelity | Plan an appointment-selection concept for an early architecture review | `guidance.wireframe-methodology` → [methodology](../../guidance/wireframe-methodology.md) | Low/mid-fidelity choice is tied to the question; unknown availability is ILLUSTRATIVE | A convincing appointment screenshot is not a real reservation or working calendar |
| WRF-02 comparison | Compare selecting a saved report in list→detail versus list+panel layouts | `pattern.task-flows` → [task composition](../../patterns/task-flows-and-information-architecture.md); `principle.visual-hierarchy` → [hierarchy](../../foundations/design-principles.md) | Same task and constraints; two genuinely structural alternatives, primary next action and safe exit | A palette swap does not count as an alternative; mock export permissions are not evidence |
| WRF-03 pending | Show a submitted export request after a network timeout | `pattern.interaction-recovery` → [state coverage](../../patterns/interaction-states-and-recovery.md) | Ready/pending/unknown/confirmed distinction, preserve context and annotate safe status lookup | Do not call an unknown result `success` or blindly replay a possibly non-idempotent request |
| WRF-04 responsive | Show saved-record selection for compact and wide windows | `guidance.mobile-adaptive` → [adaptive layout](../../guidance/mobile-and-adaptive-platform-ux.md); `guidance.accessibility` → [inclusive review](../../guidance/accessibility.md) | Single-list/detail and two-pane representations preserve meaningful next steps | A shrunken wide screenshot is not reflow; observed keyboard/focus behavior NOT VERIFIED |
| WRF-05 locale | Review an account settings header with longer translated text and mixed RTL/LTR account IDs | `guidance.internationalization` → [localization](../../guidance/internationalization.md) | Long-label and direction variants keep meaning, numbers and primary action visible | Blind mirroring, fake translated accuracy, and claims of working RTL are not acceptable |
| WRF-06 image QA | Inspect a generated payment confirmation mock with garbled fee copy | `governance.quality` → [image QA](../../governance/quality-gates.md) | Compare image against approved copy, flag clipped fees and invented payment completion, log artifact ID | Aesthetic polish is not WCAG conformance, successful charge, or a manual PASS without inspecting the image |

## Worked example A — positive structured alternatives, WRF-02

**Illustrative brief:** A team member wants to locate a saved report and request an export. Export capability and access policy are **ASSUMED**, not observed. The design question is whether a separate detail page or in-context panel better supports comparing report metadata before acting.

**Option A:** list → selected report details → review/request action. A compact layout can show details as a new route; it must annotate a safe return preserving the selected record and filters.

**Option B:** list + inline details/review panel, preserving the same report metadata and task. A compact presentation may use a separate sheet or detail route, to be reviewed rather than assumed to function.

**Positive review:** same audience, report identifiers, permissions warning, next-action language and example content; different information grouping; recorded hypotheses about comparison ease versus density; no declared winner before user evidence.

**Anti-example:** two screenshots differ only by brand colors, one includes “Export completed” despite no request confirmation, and both omit a way to return. Mark structural alternative and outcome assertions **FAIL** for the proposed depiction if actually observed in the image; otherwise **NOT VERIFIED**.

**Retrieval checks:** `task to screen composition` and `structural wireframe alternatives` → `pattern.task-flows`; `primary action hierarchy` → `principle.visual-hierarchy`; `wireframe methodology` → `guidance.wireframe-methodology`.

## Worked example B — error recovery and static evidence, WRF-03

**Illustrative screen IDs:** `S3-ready`, `S3-pending`, `S3-unknown`, `S3-failed`, `S3-confirmed`. User-initiated export has an unknown outcome after loss of connection. The `S3-unknown` image should explicitly say outcome unknown, retain report context, and annotate a legitimate status-check path **only if the product provides one**.

**Positive review:** state inventory distinguishes pending from confirmed; the screen-to-screen table separates **SHOWN** imagery from **ANNOTATED** behavior; retry policy is unresolved pending server semantics; focus/announcements are written as intended requirements, **NOT VERIFIED**.

**Anti-example:** a static spinner caption “automatically retries safely” or a green check after the timeout without confirmed server evidence. Neither an image nor the documentation test can establish transaction idempotence.

**Retrieval checks:** `static wireframe state matrix` → `pattern.interaction-recovery`; `wireframe visual QA` → `governance.quality` only for artifact inspection, not retry semantics.

## Worked example C — mobile, text growth and bidi, WRF-04/05

**Illustrative task:** Find a saved record and review its settings. Compact representation uses list→detail; wide representation uses two panes. A language stress variant uses deliberately long placeholder labels and mixed-direction strings. These are **not actual approved translations**.

**Positive review:** screen IDs identify viewport/locale, current selected item and recovery; critical controls do not intentionally disappear; logical navigation and direction-aware icons are specified; missing intermediate viewport and live reflow behavior are labeled **NOT SHOWN / NOT VERIFIED**.

**Anti-example:** desktop screenshot scaled down, action text clipped, account ID order corrupted by indiscriminate mirroring, and a caption claiming “RTL accessible on all devices.” A static concept is insufficient for all such runtime claims.

**Retrieval checks:** `wireframe viewport matrix` → `guidance.mobile-adaptive`; `wireframe text expansion` → `guidance.internationalization`; `inclusive wireframe review` → `guidance.accessibility`.

## Worked example D — generated content honesty, WRF-06

**Synthetic issue log, not an actual image review:**

| Field | Example value |
| --- | --- |
| artifact_id + revision | `EXAMPLE-payment-r0` (fictional; no artifact exists) |
| screen / state | `S5-confirmation`, illustrative desktop |
| source copy | `Fee: $12.50` (fictional test text only) |
| hypothetical observation | Image shows `Fee: $1250` and `Payment processed` with no backend evidence |
| expected decision if actually observed | **FAIL / blocker** for material copy and ungrounded payment claim; revise and re-inspect |
| actual inspection result | **NOT VERIFIED** — no image exists/was inspected |

**Anti-example:** a QA report prelabels the hypothetical defect as a completed inspection or accepts “passes all accessibility tests” solely because the image has readable typography.

## Regression scope and negative-intent safety

The [resolver](../../scripts/find_concept.py) intentionally scores `id`, `title`, `summary`, `aliases`, `domains` and `use_when` for positive discovery, **not `avoid_when`**. Therefore a term appearing only in the negative contraindications should not become a positive match. This is a *retrieval integrity test*, not automatic design-quality judgment. Regression tests should:

1. Assert task/alias routing for WRF-01–06 and retain established owner IDs (no duplicate canonical pages).
2. Confirm exact IDs and aliases take precedence over partial generic text.
3. Confirm negative-only wording cannot cause lookup hits in a deliberately constructed fixture.
4. Confirm page existence, `status: proposed`, `owner: unassigned`, `reviewed_at: null`, and references for the covered concepts.
5. Confirm this example bank contains both positive and anti-examples with explicit **NOT VERIFIED** limitations.

**Source lineage:** derived from the current canonical B1–B5 pages, documented patterns and registry resolver. These are new **synthetic test scenarios**, not external publications or real app observations. Images, user studies, keyboard, screen reader, zoom, localization quality, backend permissions and generated-copy accuracy: **NOT VERIFIED**. Review owner: unassigned.
