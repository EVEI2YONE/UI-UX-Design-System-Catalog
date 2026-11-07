# Navigation and wayfinding

**Kind:** specification · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Compose navigation landmarks, links, active-location cues and back/escape paths that make essential tasks discoverable. **Use** for persistent app navigation, contextual subnavigation and breadcrumbs. **Avoid** reorganizing routes based solely on a visual trend or adding duplicate menus that obscure current location.

## Composition and ownership

The pattern selects between primary navigation, contextual links, breadcrumbs and optional search based on task and information architecture. Use semantic links and native landmarks; a Button remains an action, not a link surrogate. Features own permitted destinations and routing; authorization is enforced by the product, not by hiding a navigation item alone. Cross-reference [role-aware contexts](role-aware-workspaces-and-context-switching.md) when multiple workspaces exist.

## State and route matrix

| Context | Expected behavior | Failure or recovery |
| --- | --- | --- |
| Default and active route | Current destination recognizable beyond color | Clear heading, current-location semantics |
| Deep link / refresh | Valid route opens directly with context | Preserve stable URLs or documented redirects |
| Narrow viewport / zoom | Key destinations remain accessible | Menu expansion, keyboard close and focus return |
| Loading / permission change | Navigation preserves orientation | Do not expose unauthorized content |
| Back / search context | Browser history and task context understandable | Avoid dropping filters or unsaved work unexpectedly |

## Inclusive, responsive and localized contract

Mark navigation landmarks clearly when multiple are present. Maintain meaningful link text and visible focus; keyboard order follows reading order, and expanded menus must have specified open/close interactions. Use logical positioning for RTL; do not indiscriminately mirror logos or universal symbols. Validate long translated labels and orientation at zoom/reflow. Use semantic tokens for active/focus states; never encode current location by color alone.

## Examples and verification

**Illustrative good:** A deep link opens the intended section, highlights the active destination and preserves a clear return path. **Anti-example:** Mobile navigation is only revealed on hover or breaks the browser Back action.

| Check | Status | Evidence needed |
| --- | --- | --- |
| IA and destination inventory | NOT VERIFIED | Actual product tasks, route map |
| Keyboard, focus and landmarks | NOT VERIFIED | Real navigation implementation |
| Deep links, history, permission states | NOT VERIFIED | Product integration tests |
| Translation, RTL, zoom and themes | NOT VERIFIED | Supported locale and device matrix |

**Canonical ID:** `pattern.navigation` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** preserve old links and task completion when changing IA. This is a documentation contract, not an implemented router.

Related: [task-flow guidance](task-flows-and-information-architecture.md), [workspaces](role-aware-workspaces-and-context-switching.md), [accessibility](../guidance/accessibility.md), [design principles](../foundations/design-principles.md). Standards: [WCAG 2.2](../governance/references.md).
