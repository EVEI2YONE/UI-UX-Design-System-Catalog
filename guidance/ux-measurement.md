# UX measurement

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose

Measure whether people can complete valuable tasks and understand interfaces. Design polish, survey sentiment and business conversion are not substitutes for observed task success.

## Core metrics

| Measure | Definition / caution |
| --- | --- |
| Task Completion Rate (TCR) | Completed target tasks / eligible task attempts; define cohort, retries, window and event |
| Time on Task | Start-to-success duration; report median/distribution and incomplete attempts separately |
| User Error Rate | Explicit mistakes or recovery events per attempt; distinguish severity and cause |
| Step abandonment | Eligible entrants to step who leave before success / entrants; do not infer why without evidence |
| Conversion | Goal completions / eligible population; define business context and guardrails |
| SUS | Standard 10-item scale transformed to a 0–100 **score**, not a percentage of people |
| CES | Task-specific perceived effort; state question and whether high/low is better |
| NPS | Promoters minus detractors as percentage points; broad recommendation intent, not task usability |

## Measurement contract

Define the user problem, target segment, success event/denominator, primary outcome, guardrails, baseline availability, privacy constraints, analysis window and decision rule. Do not embed form data, secrets or direct identifying information in telemetry. Combine usability observation and quantitative results; avoid causal claims from uncontrolled before/after changes.

**Example:** measure whether people submit a form successfully after validation improvements, track error severity and keyboard regressions, and compare eligible cohorts. **Anti-example:** interpret SUS 82 as “82% of users like it”.

## Verification

Record instrumentation quality and missing baselines as **unknown**, not zero. State which testing actually happened. Related: [task flows](../patterns/task-flows-and-information-architecture.md) and [quality gates](../governance/quality-gates.md).

## Journey measurement worksheet

Use this worksheet before instrumenting a task. Do not assign a target until baseline and product constraints are understood.

| Field | Example definition for a form task (illustrative) |
| --- | --- |
| Eligible attempt | User opens the form with permission to submit |
| Start event | `task_started` once per attempt |
| Success event | Server-confirmed `task_succeeded`, not merely a button click |
| Failure events | `validation_error`, `task_failed` with non-sensitive reason categories |
| TCR | Successful eligible attempts / all eligible attempts in the agreed window |
| Guardrails | Duplicate submissions, critical errors, keyboard access, latency |
| Segments | Device/input, first-time vs returning; only where privacy and sample size permit |
| Baseline | `UNKNOWN` until events and cohort quality are checked |

Record event version, deduplication rule, session/attempt timeout, retry treatment, analysis window, missing events and privacy review. Prefer aggregate or pseudonymous measurement; never collect form secrets or input contents. Distinguish abandonment from deliberate cancellation and failures from unobserved outcomes. Compare distributions and qualitative sessions before attributing changes to a UI edit.

**Decision gate:** specify evidence needed to ship, iterate or rollback (including accessibility and performance regressions). An observed improvement does not itself establish causation.

## Batch 12 extension — experiment, field performance and task metrics

The existing task-success contract remains authoritative for user outcomes. For rendering and responsiveness use [performance and perceived speed](performance-and-perceived-speed.md); for causal comparisons use [experimentation and causal evidence](experimentation-and-causal-evidence.md). Good web performance or a significant experiment is not automatically evidence of task success or accessibility.

| Evidence type | Define with | Do not infer |
| --- | --- | --- |
| Core Web Vitals | p75 LCP/INP/CLS, period, real-user coverage, page/route and mobile/desktop cohort | Every user had a fast page, or the task was completed |
| Task readiness | Time from entry to useful actionable content, user job, low-end device conditions | Skeleton/loading feedback means content is ready |
| Server-confirmed action | Actual backend result, unique attempt, retry/duplicate classification and timeout | Button tap or early UI update means persistence |
| A/B experiment | Randomization unit, planned allocation, exposure, one primary outcome, guardrails, uncertainty, sample-ratio mismatch and preplanned stopping | Before/after correlations or post-hoc slices prove causation |
| Delivery/rollout | Version, actual release cohort, defects/AT and privacy guardrails, rollback owner | A green catalog validator proves a real product works |

**Illustrative instrumentation:** For an application confirmation flow, count only backend-confirmed completions toward successful attempts; log non-sensitive failure categories and deduplicate retries. If controlled experimentation is used, check exposure/assignment integrity and SRM before interpreting any apparent lift. Without valid randomization, describe changes as observational.

For **web** journeys, current external good thresholds are LCP ≤2.5 seconds, INP ≤200 milliseconds and CLS ≤0.1 at the 75th percentile, considered separately for mobile and desktop. This is not a universal native-app SLA. Any baseline, budget, variant effect or claim of improvement remains UNKNOWN until real evidence exists.

**Inclusion/privacy:** Minimize sensitive telemetry and small cohort disclosures; examine low-end devices, input modalities, assistive technologies, locales and accessibility failure reports alongside aggregate metrics. Treat field/lab differences as questions to investigate.

Sources consulted 2026-11-07: [web.dev Web Vitals](https://web.dev/articles/vitals), [User-centric performance metrics](https://web.dev/articles/user-centric-performance-metrics), and [Microsoft Research SRM guidance](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/). This is proposed measurement guidance, not measured application data.
