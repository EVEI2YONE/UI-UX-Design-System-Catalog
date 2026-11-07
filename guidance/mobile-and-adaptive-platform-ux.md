# Mobile and adaptive platform UX

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose and use boundary

Adapt experiences to the **available window**, input mode and platform conventions while keeping tasks comprehensible and accessible. **Use** for mobile web, native iOS and Android, tablets, split-screen and desktop window resizing. **Avoid** treating a fixed device type or one breakpoint as a universal UX contract, or importing platform-only controls into unrelated web contexts.

Native SDK/API behavior, permission handling and navigation are owned by each platform implementation. Cross-platform guidance can share design principles without enforcing identical native interaction mechanics.

## Adaptive decision matrix

| Dimension | Design decision | Acceptance scenario |
| --- | --- | --- |
| Window constraints | Reflow, reveal or change navigation/pane presentation for usable width and height | Compact phone, wide tablet, split view, resizing |
| Safe areas and system UI | Keep critical controls clear of cutouts, OS bars and software keyboard | Open keyboard, rotate, resize |
| Navigation and return | Preserve valid deep links, system back behavior, selection and task context | Detail → back, external link → return, expired session |
| Input methods | Discoverable controls with touch, keyboard, switch and pointer equivalents | No hover-only actions or swipe-only deletion |
| Text and appearance | Dynamic Type/scaled text, large zoom, theme and contrast | Long titles, large system text, translated errors |
| Device permissions | Request in meaningful context, explain decline and fallback | Camera denied, OS permission revoked |
| Disruption | Explain pending/saved states and preserve safe edits | Background/foreground, low connectivity |
| Language and RTL | Logical direction, locale formatting and source-order consistency | Long mixed-direction labels, numeric data |

## Interaction and layout rules

- Start with the user's highest-value tasks, not a desktop screenshot scaled down. Changes to navigation must not remove essential commands or escape paths.
- Choose navigation suited to actual window size and hierarchy. For example, a compact nav bar may become an expanded rail on large Android screens; this is an example, not a mandate for web or iOS.
- Define responsive transitions including selected item, keyboard focus and route history. When switching one- to two-pane views, preserve task state and screen-reader context.
- Avoid placing primary actions behind the virtual keyboard or under system gesture areas. Respect safe areas and provide content scroll affordances.
- Use native semantics and controls where suitable. For drag, swipe, long press or multi-pointer interactions, offer pointer/keyboard-accessible alternatives; [advanced interactions](../patterns/advanced-interactions-and-reversible-actions.md) owns that contract.
- Do not truncate safety, privacy, cost, or permission information to fit compact screens. Keep warnings and confirmations understandable.

**Illustrative good:** A records app uses a single list/details flow on a compact screen and a two-pane layout in a resized tablet window, retaining the selected record and an accessible back path. After dynamic text scaling, labels wrap and actions stay visible.

**Anti-example:** Rotating a phone clears an unsaved form, while a gesture-only archive action is unreachable with switch or keyboard access.

## Required verification

Test: minimum and maximum supported windows; intermediate resize; orientation and split view; virtual keyboard; text scaling/zoom; OS back; deep links and reauthentication; focus after pane changes; touch/keyboard/screen reader; reduced motion; supported locales and RTL; denied permission, interruptions and slow network. Define applicable WCAG 2.2 targets for web, and native-platform accessibility expectations separately. Do not infer implementation conformance from documentation.

| Check | Status | Evidence |
| --- | --- | --- |
| Platform navigation and safe-area behavior | NOT VERIFIED | Device/SDK matrix |
| Adaptive resize, large text and keyboard overlap | NOT VERIFIED | Device/reflow tests |
| Touch, pointer, keyboard and AT parity | NOT VERIFIED | Task-based manual tests |
| Locale/RTL and background/resume | NOT VERIFIED | Localization and interruption tests |
| User-task success | NOT VERIFIED | Study and baseline |

## Sources and limits

- [Apple Human Interface Guidelines: Layout](https://developer.apple.com/design/human-interface-guidelines/layout) (updated 2026-09-09, consulted 2026-11-07): Apple-specific guidance for hierarchy, safe areas and adaptable windows.
- [Android Developers: Adapt layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) and [Layouts and navigation patterns](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns) (consulted 2026-11-07): Android-specific adaptive navigation and resizing.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): applicable web criteria for reflow, target size and dragging; not a universal native app rule.

**Canonical ID:** `guidance.mobile-adaptive` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [accessibility](accessibility.md), [internationalization](internationalization.md), [task flows](../patterns/task-flows-and-information-architecture.md), [advanced interactions](../patterns/advanced-interactions-and-reversible-actions.md), [offline sync](../patterns/offline-sync-and-conflicts.md).
