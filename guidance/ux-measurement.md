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
