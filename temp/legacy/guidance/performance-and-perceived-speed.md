# Performance, perceived speed and resilient task feedback

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose and boundaries

Design experiences that respond predictably while real page loading, interaction work and network outcomes occur. **Use when** choosing loading states, progressive rendering, task-level feedback, performance budgets and performance evidence. **Avoid when** treating visual animation, skeletons or perceived speed as proof the service completed a request. This is a UX decision contract; engineering owns measurement instrumentation, rendering, back-end reliability, caching, security and platform performance.

[Interaction recovery](../patterns/interaction-states-and-recovery.md) owns generic pending, error and retry semantics; [offline synchronization](../patterns/offline-sync-and-conflicts.md) owns local versus server-confirmed persistence; [UX measurement](ux-measurement.md) owns outcome definitions and denominators.

## Measurement: distinguish field from lab and web vitals from task outcomes

Core Web Vitals apply to **web experiences**. Current web.dev 'good' targets are assessed at the **75th percentile of page visits**, with mobile and desktop segmented separately, not as promises to every user:

| Metric | Good threshold | Measures | Does not prove |
| --- | --- | --- | --- |
| Largest Contentful Paint (LCP) | **≤ 2.5 seconds** | Main visible content load performance | That a user can complete the task or that all data is ready |
| Interaction to Next Paint (INP) | **≤ 200 ms** | Responsiveness to qualifying page interactions | That a network request or business mutation succeeded |
| Cumulative Layout Shift (CLS) | **≤ 0.1** | Unexpected visual layout instability | That all controls are accessible or semantically correct |

**Field / real-user monitoring (RUM):** observed visits, real devices/networks and interactions, with opt-in/collection scope, sampling/coverage, metric version, route and cohort defined. **Lab/synthetic:** repeatable controlled scenarios useful for regression and diagnosis; a clean lab score must not be described as a measured real-user experience. Collect navigation vs in-app transition and task-specific outcome timing separately when relevant; no single metric establishes overall usability.

For a *task* define user-perceived response, time to actionable content, time from submit to server-confirmed result, failure/timeout and recovery. Instrument with privacy constraints and actual event names/denominators; avoid secrets and high-cardinality personal payloads.

## Performance and feedback decisions

| Situation | UX response | Failure/verification concern |
| --- | --- | --- |
| First page render | Prioritize meaningful text and actionable shell; reserve content dimensions and progressively load noncritical assets | A skeleton that never resolves or makes key content inaccessible |
| Long data fetch | Meaningful loading status and persistent task context; optional skeleton if accurately shaped | Layout jumps, repeated focus moves, useless full-page blocker |
| Button/action pending | Immediate acknowledgment, actual pending state, duplicate-mutation protection | “Saved” before server confirmation, false optimism |
| Optimistic update | Use only where reversal/reconciliation is genuinely supported; make pending and failure recoverable | Irreversible or financially consequential outcome portrayed as final |
| Background refresh | Keep current data readable with clearly labeled freshness if stale or partial | Silently replace data while user is reading or editing |
| Network deterioration | Explain what can still be done; preserve work when technically supported | Blind retries for non-idempotent submissions |
| Heavy animation / media | Support reduced motion and throttle work; favor clarity over ornamental smoothness | Animated skeleton or chart harming attention/AT access |
| Low-powered device | Test under constrained CPU, memory, input and bandwidth; avoid all-or-nothing hydration | Desktop synthetic pass hides mobile or assistive-device failures |

Use **progressive enhancement** when possible: essential content, navigation and forms should remain useful in supported degraded scenarios. Don't claim functionality without JavaScript for a feature that actually requires it. Reserve image/media and late-data space to reduce layout shifts without arbitrarily hiding important content.

## Performance review and experiment worksheet

| Field | Example (illustrative, not measured) |
| --- | --- |
| User job | Find and update an existing request |
| Outcome | Confirmed edit without duplicate submission |
| Web vital evidence | p75 LCP / INP / CLS segmented by actual mobile and desktop visits |
| Task-specific evidence | Entry → actionable UI; submit → server confirmation; timeout/retry proportion |
| Conditions | Low-powered device, slow network, large content, keyboard, translated label |
| Baseline and budget | UNKNOWN until measured; budget and owner agreed before rollout |
| Release guardrails | No significant task-completion, accessibility, data-loss or duplication regression |

### Positive / negative example

**Illustrative good:** A form immediately acknowledges Save, retains focus and input, shows “Saving…” then “Saved” only when the backend confirms. If the response is lost, it shows “Status unknown; check saved version” rather than automatically resubmitting.

**Anti-example:** The screen removes a spinner in 200 ms and announces “Complete” while a slow financial transaction still has an unknown server outcome.

## Acceptance and evidence

1. Record which route, device/network segments, tasks and metric instruments were tested; keep missing data as UNKNOWN.
2. Run laboratory performance under repeatable constrained conditions and field monitoring where consent/privacy permit; investigate disagreement rather than replacing one with the other.
3. Confirm keyboard, screen reader, zoom/reflow, motion preferences, long translations, RTL and error/partial/offline states in a **real implementation**.
4. Distinguish frontend paint, visible task readiness and backend commit. Test double activation, interrupted response and idempotent retry.
5. A performance target is **not** evidence of actual measured quality. No live measurements or code profiling were performed for this proposed entry.

| Check | Status |
| --- | --- |
| Field Core Web Vitals and task-level baseline | NOT VERIFIED |
| Lab synthetic and low-end device scenarios | NOT VERIFIED |
| Real application error, recovery and duplicate mutation | NOT VERIFIED |
| Manual accessibility and internationalization | NOT VERIFIED |
| Validated perf budget, product owner and rollout decision | NOT VERIFIED |

## Sources and limitations

- [web.dev Web Vitals](https://web.dev/articles/vitals) and [threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds) (consulted 2026-11-07): web p75 LCP, INP and CLS good thresholds; targets can evolve and are **not** generic native-platform SLA thresholds.
- [web.dev User-centric performance metrics](https://web.dev/articles/user-centric-performance-metrics) (consulted 2026-11-07): lab vs field evidence and user-perceived/task-specific measurement.
- [web.dev Optimize INP](https://web.dev/articles/optimize-inp) and [Optimize CLS](https://web.dev/articles/optimize-cls) (consulted 2026-11-07): diagnose responsiveness and reserve loading space; engineering implementation guidance.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): separate accessibility obligations remain; Web Vitals pass is not WCAG conformance.

**Canonical ID:** `guidance.performance-experience` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [UX measurement](ux-measurement.md), [interaction recovery](../patterns/interaction-states-and-recovery.md), [offline synchronization](../patterns/offline-sync-and-conflicts.md), [quality gates](../governance/quality-gates.md), [experimentation](experimentation-and-causal-evidence.md).
