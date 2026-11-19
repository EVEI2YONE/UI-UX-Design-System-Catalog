# Disclosure and accordion

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Reveal or hide subordinate content with an explicit expanded/collapsed control. A group of disclosures may be called an accordion.

**Use when:** Secondary, optional or lengthy detail can be collapsed without hiding information necessary to make a safe primary decision.

**Avoid when:** The content is mandatory for task completion, the UI needs mutually exclusive navigation panels, or a full dialog is more appropriate.

## Ownership and decision rules

Each disclosure owns a named trigger and expanded state; the feature owns the semantic content, persistence policy and whether multiple sections may stay open.

- Prefer native details/summary when its behavior and supported styling meet the requirement.
- For custom controls, use a real button with aria-expanded and a stable aria-controls target as appropriate.
- State clearly whether multiple panels can stay open and whether their expansion persists across refresh/navigation.
- Do not use collapse to hide critical validation, safety or price information; ensure headings remain navigable.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Collapsed | Trigger identifies hidden content | Expanded state false |
| Expanded | Associated content readable and keyboard reachable | Expanded state true and DOM visibility coherent |
| Nested or multiple | Hierarchy remains understandable | No confusing duplicate landmark labels |
| Dynamic removal | Move focus if its control disappears | No focus stranded in hidden content |

## Keyboard, focus and inclusive operation

- Enter and Space activate custom disclosure buttons; native summary uses native keyboard behavior.
- When content closes while focus is inside it, restore focus to a visible trigger.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** A support article groups optional troubleshooting details under labeled expandable headings.

**Anti-example:** Hiding a mandatory payment warning in a collapsed section while the user confirms a purchase.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Expanded state with pointer, keyboard and screen reader | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Focus retention on collapse, nested disclosures and heading order | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Reflow, long localized headings, reduced motion | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.
