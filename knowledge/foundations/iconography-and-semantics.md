# Icon semantics and accessible icon controls

**Kind:** contract · **Status:** proposed · **Primary layer:** foundations · **Canonical ID:** `foundation.icon-semantics` · **Owner:** unassigned · **Human review:** pending (`reviewed_at: null`) · **Draft:** 2026-11-07

## Purpose and boundary

Give design systems a consistent, inspectable decision rule for icons inside controls, navigation and feedback. **Use when** selecting a reusable icon family, assigning an action or status symbol, or building an icon-only control. **Avoid when** a symbol adds no recognition value, replaces an essential visible label, or is used to hide a consequential action.

This is a **platform-neutral specification**, not an icon package, approved glyph mapping, automated accessibility guarantee or universal brand style. A product chooses and verifies its own installed exports and semantics. [Practical UI styling recipes](practical-ui-styling-recipes.md) owns broader visual craftsmanship and imagery. [Button](../../specifications/components/button/spec.md) owns activation; [component contracts](../architecture/component-contracts.md) own general states; [feedback](../../specifications/patterns/feedback.md) owns communicating domain results. This page owns the *semantic relationship between an icon, its host component and user meaning*.

## Decide the role before selecting a glyph

| Intent in context | Default | Accessible meaning and failure to prevent |
| --- | --- | --- |
| Decoration repeating nearby text | Decorative icon, hidden from assistive technology when appropriate | It adds no second "Save Save" announcement |
| Informative status or category | Expose text plus optional icon, or a meaningful equivalent accessible name | A colored check is not evidence of backend success |
| Triggering an action | Native host Button with named verb/object, icon optional | The SVG never owns click/keyboard handlers or authorization |
| Navigation or disclosure | Host link or correctly modeled disclosure/menu control | An arrow alone does not reveal destination/state or force RTL mirroring |
| Consequential or ambiguous task | Visible descriptive label and impact context | Do not hide deletion/approval behind an unlabeled glyph |

First identify semantic intent and consumer task, then choose a coherent glyph family and optical size. The catalog **never** defines a universal icon map or claims recognition rates from pictogram appearance. Related: [Button](../../specifications/components/button/spec.md) (activation), [feedback](../../specifications/patterns/feedback.md) (status) and [interaction recovery](../../specifications/patterns/interaction-states-and-recovery.md) (unknown outcomes).

## Semantic icon registry: one meaning, explicit context

Start with the user's recognizable **verb/object or status label**; only then decide whether an icon improves scanning, recognition or wayfinding. Maintain a single product-level semantic registry with **intent ID, human meaning, host role, glyph choice, visible text requirement, accessible-name source, decorative/informative status, RTL behavior, visual token, owner and lifecycle**. This is distinct from importing an arbitrary pictogram by filename.

| Semantic intent (illustrative) | Role | Text/accessible meaning | Icon selection caution |
| --- | --- | --- | --- |
| `action.add` | Action inside a button | "Add project" / specific object, not "Plus" | A plus alone may be ambiguous |
| `action.edit` | Action | "Edit contribution" | Display the target when repeated in rows |
| `action.delete` | Consequential action | "Delete item" + impact where needed | Never rely on red or trash glyph alone |
| `action.more` | Menu trigger | "More actions for [item]" | Must expose actual menu behavior and focus |
| `disclosure.expand` | State signifier for host trigger | "Show details", `aria-expanded` on button | Direction can depend on orientation and writing mode |
| `status.pending` | Informative | Visible "Pending review" | Do not confuse pending business state with an active loading spinner |
| `status.approved` | Informative | Visible "Approved" only after authoritative confirmation | A check on a decision button does **not** mean approval occurred |
| `nav.back` | Navigation | Visible/contextual "Back to projects" | Directional glyph may mirror in RTL; verify context |

Example mappings are **intent IDs, not universally mandated icons**. Record alternatives or deprecated symbols rather than proliferating competing names. Do not present the product logo, emoji or brand artwork as part of an interchangeable action-glyph registry.

## Classify the icon's role before coding

**Host owns the interaction.** In a named Button, Link, switch or disclosure control, the icon is generally decorative and its action meaning comes from host text or an accessible name. Informative status needs a readable word/status, not just color or a glyph. If a visual control has no reliable accessible name, its role is not complete. Do not nest independent interactive SVGs inside a clickable parent.

### Icon-only action state and geometry contract

| State or context | Contract and accessible alternative | Check |
| --- | --- | --- |
| Idle / hover / focus | Descriptive action name and visible focus, not a tooltip-only affordance | Keyboard Enter/Space, pointer and touch |
| Pressed / toggled | Expose pressed/expanded/checked **only on the correctly modeled host** | Assistive role/state and false toggles |
| Pending / unknown result | Preserve layout/context, prevent unsafe duplicate submit, announce pending/unknown truthfully | Delayed service and lost acknowledgement |
| Disabled / permission revoked | Explain why in adjacent accessible text when relevant | Keyboard and authorized scope |
| Success / failure | Confirm state only after authoritative result; offer recovery | Error, retry and partial completion |
| Narrow / zoom / locale / RTL | Keep hit target usable, labels localizable and direction-sensitive symbols appropriate | Reflow, forced colors, reduced motion and translated growth |

**Glyph versus hit target:** a 16–24 CSS-pixel drawing may sit inside a substantially larger interactive area. [WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum) has a 24×24 CSS-pixel AA target requirement with specified exceptions; check the *actual target and exception*, not just icon dimensions. Non-text contrast and focus criteria must likewise be evaluated in the implemented host.

**RTL:** use logical leading/trailing slots; mirror meaningful directional navigation icons when appropriate, not brands, clocks, numbers or status symbols automatically. Localize `aria-label` and nearby text together.

## Illustrative code: host owns the event

```tsx
import { Pencil, MoreHorizontal } from "lucide-react";

// Illustrative React markup; not a published catalog component.
// The icon is decorative because the Button has a clear text label.
<button type="button" onClick={onEdit}>
 <Pencil aria-hidden="true" focusable="false" /> Edit contribution
</button>

// Icon-only action, when context makes its meaning sufficiently discoverable.
<button
 type="button"
 aria-label={`More actions for ${itemTitle}`}
 aria-haspopup="menu"
 aria-expanded={menuOpen}
 onClick={toggleMenu}
>
 <MoreHorizontal aria-hidden="true" focusable="false" />
</button>
```

The example assumes an implementation with appropriate focus, menu semantics, stable IDs and a complete keyboard interaction pattern. Verify package exports and local menu library behavior. Prefer an existing accessible menu/button primitive over implementing a custom popup. Do **not** use `role="menu"` for a generic disclosure if it does not implement menu keyboard behavior.

**Anti-example:** a tiny clickable `<Trash2 />` icon inside a clickable card deletes a record without label or confirmation; it has nested click propagation, no named keyboard target, and potentially irreversible side effects.

## Verification owner and evidence rule

Use the **single acceptance matrix at the end** of this document for registered intent, accessible host behavior, zoom/touch, theme, translations/RTL and pending/unknown outcomes. A source-only registry review can establish semantic consistency in writing, but actual accessible-name computation, focus and recognition require rendered consumers and representative tests. Until then the status is **NOT VERIFIED**.

## Sources and provenance

- [WAI-ARIA APG Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) — button activation and expanded-state semantics (consulted 2026-11-07).
- [WAI-ARIA APG Menu Button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) — only when implementing a real menu-button interaction (consulted 2026-11-07).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — applicable text/non-text contrast, name/role/value, keyboard and target-size criteria (consulted 2026-11-07; applicability must be assessed per control).
- [Lucide accessibility guidance](https://github.com/lucide-icons/lucide/blob/main/docs/how-to/accessibility.md) — decorative vs meaningful icons and visible labels (consulted 2026-11-07; implementation library/version specific).

Motivating example: [Little Wins icon knowledge ](https://github.com/EVEI2YONE/Little_Wins/blob/main/docs/little-wins/ui-knowledge/batch-05-iconography-and-affordances.md) (app-local proposals, not observed user comprehension or general icon mandates).

**Related canonical IDs:** `foundation.practical-styling`, `component.button`, `architecture.component-contracts`, `guidance.accessibility`, `guidance.internationalization`, `pattern.feedback`, `pattern.interaction-recovery`. **Lifecycle:** proposed, owner unassigned, no human review or product tests recorded.

## Icon-consistency audit and evolution

**Scope:** review whether a product's chosen icon family and semantic intent registry remain coherent as new components are added. This is a **decision and audit contract**, not a universal glyph set, a Lucide export list, or evidence of implementation. General visual craftsmanship stays with [practical styling](practical-ui-styling-recipes.md); controls own actual activation through their [component contracts](../architecture/component-contracts.md); verification ownership is [quality gates](../../governance/quality-gates.md).

### A reviewable semantic icon registry entry

Record one canonical `semanticIntent` (verb/object or status), human meaning, role, approved glyph and package/version, visible/accessible label source, host component, visual token, applicable RTL treatment, owner, current consumers, lifecycle state and migration aliases. Preserve distinguishing context: the same icon may be appropriate for two actions with **different explicit labels**, but never imply the two actions have identical consequences.

### Consistency and collision matrix

| Compare | Conformance decision | Escalation trigger |
| --- | --- | --- |
| Same intent / different glyphs | Prefer one product meaning, document context and migration aliases | Conflicting destructive or high-value action labels |
| Same glyph / different verbs | Different contextual accessible labels must distinguish consequences | Approval, selection and confirmed success confused |
| Decorative vs interactive use | Decorative SVG is hidden; named host owns activation | Bare clickable SVG or nested targets |
| Pending vs completed | Product feature confirms authoritative status before visual success | Optimistic green check misstates server outcome |
| Themes, locale and density | Consistent optical size plus focus, contrast, meaningful RTL | Icon-only disclosure disappears on zoom/forced colors |

### Audit and migration sequence

1. Inventory **rendered** icons and permitted users in representative journeys; do not treat unused imports as adoption.
2. Compare each actual glyph with registry meaning, host accessible name, permission, state transitions and RTL behavior; classify ambiguity and severity.
3. Resolve collisions through clearer text/context before changing glyph shape; document aliases and safe deprecation.
4. Migrate one host component and its consumers at a time. Record state, theme/locale/zoom and focus regressions, then remove obsolete glyph mappings after tests.
5. Escalate any actionable icon without accessible name, concealed destructive intent or status falsely announcing server success. This is a product defect **if observed in a product**, not a demonstrated defect in this specification.

### Verification and adoption

| Check | Scope/evidence | Status |
| --- | --- | --- |
| Registry intent collision audit | Product glyph mapping, live consumers and semantic labels | NOT VERIFIED |
| Glyph package/version and theme consistency | Actual installed assets, rendering across modes | NOT VERIFIED |
| Native roles, keyboard/AT and target size | Browser/device and screen-reader test log, WCAG applicability | NOT VERIFIED |
| Pending/failed/uncertain icon timing | Authorized service/integration scenarios | NOT VERIFIED |
| Translation, RTL and visual reflow | Supported locale and responsive matrix | NOT VERIFIED |

**References (consulted 2026-11-07):** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [MDN aria-hidden](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-hidden). Audit outcomes remain app-specific; no new packaged component is provided.

**Primary reference scope:** [WAI-ARIA APG Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/) defines web button keyboard and naming expectations; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines applicable accessibility outcomes; [MDN aria-hidden](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-hidden) explains hiding decorative content. None prescribes a specific icon library or demonstrates that users recognize a glyph. The visual [styling recipes](practical-ui-styling-recipes.md) govern stroke and placement.
