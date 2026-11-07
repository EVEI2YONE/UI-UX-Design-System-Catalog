# Accessibility

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose

Accessibility is a design and delivery requirement, not a visual polish phase. Use [WCAG 2.2 AA](../governance/references.md) as the default applicable **web target** and WAI-ARIA APG for complex widgets; native semantic HTML is preferable where it meets the task. Do not claim conformance without scenario-specific evidence.

## Contract

- **Semantics:** real buttons/links, descriptive names, headings and landmarks, labels and errors linked to fields.
- **Keyboard and focus:** reachable actions, logical order, visible focus; documented Escape and dialog focus entry/return.
- **Visual and touch:** contrast, reflow/zoom, text readability, non-color-only indicators, forgiving targets and accessible gesture alternatives.
- **Motion and feedback:** reduced-motion preferences, restrained animation, appropriate announcements for async completion and errors.
- **Robustness:** verify disabled, error, loading, narrow screen and translated-label states; high contrast and different input methods.

## Minimum evidence

| Check | Method | Initial status |
| --- | --- | --- |
| Automated issues | Lint / axe-type scan | NOT VERIFIED |
| Keyboard-only critical flow | Manual | NOT VERIFIED |
| Zoom/reflow and touch | Manual | NOT VERIFIED |
| Screen reader announcements | Manual spot check | NOT VERIFIED |
| Theme contrast and focus | Manual/automated | NOT VERIFIED |
| Long translated labels and RTL when applicable | Manual/pseudolocalized | NOT VERIFIED |

Automated checks alone cannot establish accessibility compliance. Treat blockers in core flows as release-significant. Related: [component contracts](../architecture/component-contracts.md) and [interaction states](../patterns/interaction-states-and-recovery.md).