# Synthetic visual refinement example bank — KG-17

**Status:** proposed illustrative documentation, **not a canonical concept**, rendered screenshots, or measured UX evidence. **Owner:** unassigned. Guidance lives in [quality gates](../governance/quality-gates.md#visual-craftsmanship-review-and-corrective-iteration--batch-4-kg-15-and-kg-16-proposed-2026-11-07) and [visual foundations](visual-design-craftsmanship.md). This file provides worked **written** before/after scenarios to help reviewers practice precise criticism and correction.

## Repeatable practice method

For every example, preserve the user task, copy, data, state and viewport; identify the defect, owning token/component and smallest change; state the expected outcome as a **hypothesis**; list required re-render and independent accessibility/behavior tests. Do not equate a visually improved description with an actual improvement in user success.

| Case | Task / visual defect (BEFORE — synthetic) | Proposed adjustment (AFTER — illustrative) | What must be verified |
| --- | --- | --- | --- |
| VIS-EX-01 — crowded dashboard | A service manager needs to find urgent records. Eight equally bright metric cards and heavy shadows dominate the page; critical overdue table starts far below. | Quiet neutral panels; one contextual exception cue with icon/text; put action-required table at a clear scan position; keep figures and freshness labels. | Side-by-side same-data captures narrow/wide; contrast and status non-color cues; task finding with representative users remains NOT VERIFIED. |
| VIS-EX-02 — typographic discord | User reviews an account form. Title, help text and labels mix three fonts; a long translated heading clips. | One accessible body family and one purposeful display role; consistent hierarchy and fluid text container; preserve exact content and semantic heading order. | Render fallback fonts, long locale, zoom/reflow, errors and focus; screenshot alone cannot verify assistive semantics. |
| VIS-EX-03 — floating-card inflation | Analyst compares plans. Each plan has a different radius, shadow, inset and accent; price fields do not align. | Standard card and consistent comparison rows; reserve emphasis for a meaningful selection, keep prices/terms equally visible; use shared surface tokens. | Compare same plan facts on compact/wide, keyboard selection, screen reader, color/contrast and no hidden terms. |
| VIS-EX-04 — editorial hero excess | Reader needs introductory instructions. Large decorative media displaces task-critical instructions and CTA. | Restrained hero height, heading/body rhythm, visible initial guidance, media crop chosen for context rather than spectacle. | Mobile viewport, text alternatives, content visibility, loading/layout shift, performance with images, and keyboard reading order. |
| VIS-EX-05 — motion overload | User saves a settings change. A bouncing button and toast imply success before server confirmation. | Quiet pressed/busy feedback, persistent correct result announcement after confirmed response; reduced-motion variant retains understandable state. | Actual async failure/timeout handling, focus, screen reader announcements, repeated submissions, reduced motion. |
| VIS-EX-06 — inconsistent error state | Form error wraps into the next button, changing layout rhythm and obscuring Cancel. | Reserve flexible error flow space rather than fixed height; wrap naturally with semantic field association and consistent section spacing. | Error text at longest supported locale, narrow/zoom, focus/keyboard, screen reader field-error announcement; re-render exact changed state. |

## Fully worked example — VIS-EX-01

**Task and baseline:** Service manager scans open cases to locate overdue action items. Desktop 1280px and compact 375px, English, light mode, same fictional cases. **All observations below are hypothetical descriptions; there are no underlying images.**

**BEFORE (synthetic):** Eight equal saturated cards at the top compete with the overdue table. The table starts below multiple blocks of visually similar dashboard content. All cards have a pronounced shadow although none is elevated relative to the rest.

**Review log:** `VIS-EX-01 | synthetic scenario | 1280px/light/default | eight competing colorful KPIs overshadow urgent table | hierarchy/MAJOR | undifferentiated emphasis | reduce accent saturation; move urgent table into stronger scan position | owner TBD | same-context screenshot + user task | NOT VERIFIED`.

**Smallest change:** Keep numbers and time windows intact. Reorder sections based on the user's task; define one semantic highlight for overdue status with an accompanying label; use quiet surfaces and one controlled shadow/elevation rule. Keep a truthful source/date visible.

**AFTER (proposed):** Primary heading identifies the current queue and reporting period. One focused overdue summary leads into the actionable table; other KPIs remain accessible in a less visually dominant group. The chosen type scale and surfaces remain token-backed.

**Verification plan:** Take fixed-font, fixed-content screenshots at desktop and compact widths; visually inspect contrast, table alignment and wrapping; run keyboard/screen-reader and zoom tests on the actual implementation; observe representative users locating overdue cases. Mark all tests **NOT VERIFIED** until actually run. A better screenshot does not prove faster task completion.

**Anti-example:** swap every card to a fashionable gradient and declare the dashboard “more modern” without checking whether the urgent table is still easy to find.

## Example submission template

```text
ID / task:
Artifact + revision / environment:
State, viewport, theme, locale, font:
Before: observable issue (or SYNTHETIC if no artifact exists):
Severity + craftsmanship lens:
Smallest proposed design change:
Owning token/component:
After: same-condition capture / NOT VERIFIED:
Regression states checked:
Accessibility and user-task evidence:
Reviewer and disposition:
```

**Known limitations:** No images, licensed assets, code changes or user studies were created for this example bank. The examples teach disciplined critique—not a validated universal visual style. See [quality gates](../governance/quality-gates.md), [styling recipes](practical-ui-styling-recipes.md), [design tokens](design-tokens-and-themes.md), [accessibility](../guidance/accessibility.md) and [UX research](../guidance/ux-research-methods.md).
