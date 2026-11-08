# Accessibility, theme and performance evidence

**Knowledge-gap IDs:** KG-07  
**Status:** knowledge specification FILLED; verification/implementation follow-up OPEN, no human approval  
**Origin:** [original gap audit](../03-knowledge-gap-audit.md) and [durable concept / closure ledger](../17-concept-inventory-and-decisions.md)  
**Recorded:** 2026-11-08 · **Accountability:** Accessibility reviewer, visual design owner and performance owner (role only; no named assignee)

## Why the gap remains

Automated browser and axe evidence is narrower than human accessibility and deployed performance acceptance. A standalone semantic token playground was proposed in Stage 1 but is not implemented as such.

## Recommended work

Review all preview scenarios in actual browsers and screen readers, manual keyboard/task recovery, zoom at 200–400%, forced colors/contrast, RTL and reduced motion. Evaluate whether a standalone token playground provides distinct reusable value and require source/fixture/contrast tests before registering an implementation. Record lab and eventual field LCP/INP/CLS with deployment parameters.

## Acceptance evidence required

Signed scenario-level reviewer matrix with device/AT/browser versions, measured ratios where appropriate, screenshots with findings and remedies, and real hosting/network metrics.

## Nonclaims and deferral rule

No WCAG certification, field Core Web Vitals or token-playground registration is implied by existing automated CI.

This is a **repository-only durable follow-up**, not a live website concept, canonical catalog ID or a new executable implementation. Keep status open until the specified review produces evidence; if the requirement is rejected or waived, record the responsible owner and decision rather than silently deleting the work package. The current [Phase 10 release no-go review](../16-phase-10-release-readiness.md) remains in force.

## Knowledge-development delivery and evidence split

**Canonical knowledge:** [New substantive guidance](../../../guidance/accessibility.md#reference-state-accessibility-theme-and-performance-acceptance-matrix). A scenario-by-scenario focus, AT, contrast, theme, zoom, RTL and performance evidence matrix is now authored. No actual human assistive-technology signoff, color-pair certification or production Core Web Vitals are established.

**Context and research ledger:** [Five context-gathered knowledge packages](../20-knowledge-development-batches.md). This work package remains open only for the outstanding observed evidence, implementation or human decision—not because the guidance is still missing.
