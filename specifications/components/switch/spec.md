# Switch and immediate toggle

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Expose an explicit binary on/off state, most often a setting that takes effect on activation. A Switch is not a substitute for consent or a choice set.

**Use when:** A setting is truly binary and the consequence of changing its state is immediate and understandable.

**Avoid when:** The user must explicitly submit a form later, the option is consent to terms, or a third/mixed state exists.

## Ownership and decision rules

The shared control owns visible on/off affordance and accessible state; the feature owns saved preference, permission, optimistic update and rollback.

- Use a stable action label describing the setting; announce state separately rather than changing the accessible name from Enable to Disable.
- Define whether activation is immediate or requires explicit Save. Avoid a visual on state when persistence is pending or failed.
- If an async update fails, revert to the last confirmed state or present a clearly unresolved state with retry.
- Prefer native checkbox semantics with appropriate labeling where practical; custom switch roles require valid keyboard and state handling.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Off / on | Two stable, distinguishable states | Expose checked state and name |
| Pending | Prevent contradictory repeated actions; show saving state | Announce progress sparingly |
| Rejected | Restore confirmed value; show next step | Preserve focus and explain error |
| Unavailable | Show why control cannot change | Disabled or readonly semantics match behavior |

## Keyboard, focus and inclusive operation

- Space activates a focused switch; pointer and touch activation must be equivalent.
- Avoid unexpected navigation or losing focus after changing a setting.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** A user enables email summaries and immediately sees Saving then On after server confirmation.

**Anti-example:** Showing On optimistically forever even after the save fails or using a switch for a legal agreement.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Persisted versus pending state; duplicate activation | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Keyboard and screen reader name/role/state | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Long translated labels, target size and contrast | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://www.w3.org/WAI/ARIA/apg/patterns/switch/); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.
