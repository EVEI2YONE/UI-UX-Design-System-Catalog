# Responsive spatial composition

**Kind:** guideline · **Status:** proposed · **Primary layer:** foundations · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundary

Choose content-driven layouts, density and spatial hierarchy across viewport/container sizes while preserving reading order, focus continuity and necessary actions.

**Use when:** A component or screen must operate within narrow panes, split windows, zoomed layouts and large canvases instead of fixed device mockups.

**Avoid when:** Creating device-brand-specific breakpoints without a content need, or treating responsiveness as visual resizing alone.

**Accountability:** Foundations establish spatial guidance; components own container-level behavior; features own task hierarchy and page transitions.

## Decision rules and tradeoffs

- Start from the smallest usable content and introduce breakpoints where the content actually needs a different arrangement.
- Preserve logical reading/DOM order after visual reflow; CSS order changes must not reverse keyboard sequence.
- Use intrinsic sizing, reasonable min/max dimensions and container queries for local adaptation where supported.
- When columns collapse, decide which context is primary and how selection, scroll and focus persist.
- Use logical properties, flexible text blocks and wrapping for zoom, dynamic type, RTL and translated content.
- Add density variations only where evidence supports compact/comfortable needs.

## Decision matrix

| Context | Question | Decision support |
| --- | --- | --- |
| Compact | What must remain visible? | Single-column primary task and explicit actions |
| Wide | Which additional context is valuable? | Secondary pane without duplicated commands |
| Zoom | Are text and error messages clipped? | Content height grows and reflows |
| RTL | Do spatial starts and ends still match intent? | Reading order and logical-property review |

## Example and anti-example

**Illustrative example:** A reviewer dashboard shows list/detail columns on wide screens and a clear list-to-detail route on narrow screens without losing selection.

**Anti-example:** A fixed desktop form shrinks to 320 CSS pixels, clipping its field labels and submit action.

## Inclusive operation and verification

Use meaningful headings, accessible descriptions, appropriate focus, recovery and language. Review translated content, RTL, zoom/reflow, high contrast, touch and reduced motion where relevant. No mockup alone proves accessible behavior.

| Check | Evidence needed | Status |
| --- | --- | --- |
| Content breakpoints and container resizing | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| Keyboard order and zoom/reflow with long localized copy | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| RTL, high contrast, touch targets and reduced-motion | Observed application or research evidence with scope and limitations | NOT VERIFIED |

This concept is proposed guidance, not a real-user study, implementation, compliance claim or independently approved design standard.

## Source references and related concepts

- [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — review scope and edition for the consuming context.
- [W3C i18n](https://www.w3.org/International/quicktips/) — review scope and edition for the consuming context.
- Related canonical sources: [Practical styling](practical-ui-styling-recipes.md), [Tokens and themes](design-tokens-and-themes.md), [Mobile and adaptive](../guidance/mobile-and-adaptive-platform-ux.md).
- Record a human owner, review date, evidence and known limitations before changing the proposed status.
