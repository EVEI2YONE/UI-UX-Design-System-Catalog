# Tabs and tab panels

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Present a small set of peer views within one context, with one associated tab panel visible at a time.

**Use when:** The views are siblings with short predictable labels, and changing between them should not lose the task context.

**Avoid when:** Steps in a mandatory sequence, top-level site navigation, or content better shown together with headings.

## Ownership and decision rules

Tablist owns selected tab, panel labeling, keyboard model and panel visibility; feature owns data loading and route/deep-link persistence.

- Document automatic versus manual activation: automatic only when panel content is ready without perceptible latency.
- Use the APG tablist/tab/tabpanel relationship; selected state and panel visibility must stay synchronized.
- Preserve panel-specific draft state when users switch, unless clearing is explicitly required and explained.
- Provide useful fallback and route handling if tabs represent shareable destinations; avoid using tabs to hide required fields.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Selected | One selected tab and associated panel visible | Correct aria-selected and controls relationship |
| Focus without selection | Manual activation model preserves selection | Visible focused tab distinct from selected |
| Panel pending/error | Retain orientation and safe retry | Status tied to the active panel |
| Narrow width | Tabs may scroll or adopt another explicit navigation pattern | Focus order and tab names remain available |

## Keyboard, focus and inclusive operation

- Tab enters the tab list and reaches the panel according to the chosen model.
- Left/Right or Up/Down and Home/End follow APG orientation; Enter/Space activates when manual.
- When the selected tab is removed, choose a documented adjacent focus/selection fallback.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** A record detail view has Overview, Activity and History tabs with each panel labeled and deep-linked.

**Anti-example:** Using tabs as a hidden stepper in a checkout that must collect inputs in order.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Automatic/manual activation with keyboard and focus | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Deep links, panel errors, panel drafts and dynamically removed tabs | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Screen reader relationships, zoom, long RTL labels | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.
