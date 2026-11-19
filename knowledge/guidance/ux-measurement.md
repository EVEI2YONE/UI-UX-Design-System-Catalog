# UX measurement

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose

Measure whether people can complete valuable tasks and understand interfaces. Design polish, survey sentiment and business conversion are not substitutes for observed task success.

## Measurement decision — specify before collecting events

1. Define **one user task** and eligible population, including start, authoritative success, failure, cancellation and timeout outcomes.
2. Choose a **primary outcome** (usually task success or error severity), and guardrails (accessibility, data correctness, privacy and retention). A lower click count is not success by itself.
3. Record numerator, denominator, unit, device/input/locale, observation window, sample/exclusion rules, event instrumentation version and missingness.
4. Compare matched conditions or specify randomization, assignment unit and analysis before exposure. Without a baseline, write **UNKNOWN**, not zero.
5. Report uncertainty, sample context, outliers, missing events, decision owner, changes to make and rollback criteria.

**Example metric card (synthetic):** "Eligible completed form submissions / all eligible form attempts started during a seven-day window"; verify completion from the service, include failed/abandoned attempts in the denominator policy, and segment keyboard/touch without treating either as a lesser cohort. Do not record private form contents. These are definitions, **not measured values**.

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

Record instrumentation quality and missing baselines as **unknown**, not zero. State which testing actually happened. Related: [task flows](../../specifications/patterns/task-flows-and-information-architecture.md) and [quality gates](../../governance/quality-gates.md).

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

## Experiment, field performance and task metrics

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

## Collaborative reviews and shared-value journeys

Use journey-aligned metrics instead of generic dashboard engagement. Prioritize **submission completion** (server-confirmed successful contributions / eligible started attempts), **review turnaround** (median and p75 elapsed from submission to first substantive decision), **return/rework** (returned submissions / eligible reviewed submissions, with reasons), **review correctness** (authorized corrections and error-severity categories), **reward fulfillment** (fulfilled / eligible requested, with pending age), and **scope confusion** (project-switch recovery or wrong-scope attempts from qualitative research). Record eligible cohort, event version, timezone, deduplication and cancellation separately. Compare owner-managed and independently authenticated workflows only if those distinct populations exist.

For toggled-off features, mark related metrics **NOT APPLICABLE** to the disabled period, not zero performance. For offline/timeouts, distinguish server-confirmed transactions from UI requests. Never capture contribution descriptions, private member details, or other sensitive content in telemetry. No Little Wins baseline or causal effect has been verified in this catalog change.

## Interaction-effort measurement without click-count tunnel vision

When comparing a consolidated toolbar or successive-review flow, use [advanced interactions](../../specifications/patterns/advanced-interactions-and-reversible-actions.md) for control design and [task flows](../../specifications/patterns/task-flows-and-information-architecture.md) for action location. Keep completion, accuracy and safety ahead of interaction counts.

| Secondary measure | Operational definition and caution |
| --- | --- |
| Pointer travel distance | Task-relevant movement in CSS pixels for observed pointer sessions; **not applicable** to keyboard-only input |
| Keyboard navigation effort | Meaningful focus transitions or key activations before the required action; count stranded/misdirected focus separately |
| Time to next action | Time from **authoritatively confirmed prior completion** to a deliberate next eligible action; exclude no eligible next task with reason |
| Re-entry / re-selection | Repeated unchanged inputs or item choice caused by interface interruption; distinguish deliberate corrections |
| Comprehension and errors | Prediction of consequences, duplicate action attempts, recovery and permission confusion—mandatory guardrails |

**Evaluation protocol:** define baseline and variant task, eligibility, matched contexts, input modes, start/success, dropouts and missing data. Compare distribution, TCR and errors alongside secondary costs; do not infer causality from convenience samples or call fewer steps universally better. Collect only consented, minimized interaction data; sensitive text and continuous pointer recordings are not necessary for a task-cost audit.

**Illustrative scenario:** A review queue offers a stable next-item panel after confirmation. Compare corrected decisions, time-to-next-action, focus return, cancellations and unknown acknowledgements, not merely click totals. **All proposed gains are NOT VERIFIED.**

## Catalog discoverability and source-trust study protocol

The catalog serves both people browsing source-linked guidance and deterministic search agents. Internal lookup tests do **not** establish that people find, understand or trust the correct concept.

### Representative discovery tasks and reporting

| Task | Observable outcome | Guardrail |
| --- | --- | --- |
| Find a Button or Dialog contract from task language | **First-hit relevance**: canonical first selected concept matches the predetermined task owner | No assisted hints or hidden reranking between participants |
| Recover from an unknown submission result | Participant distinguishes known failure from unknown outcome and chooses safe next step | Do not reward an unsafe duplicate submit |
| Distinguish a proposal from an implementation | Participant correctly identifies `proposed` and E0 as unverified documentation | No claim that a working component or test result exists |
| Find and reuse source responsibly | Participant opens source, understands owner, related rules and evidence limitations | No copied incomplete example treated as production code |

**Study contract:** pre-register a small set of representative tasks and target answers; choose and report recruiting criteria, participant count, ability and role diversity, modality (pointer/keyboard/screen reader where available), environment, query vocabulary and task order. Observe first choice, recovery path, correction count, time and trust comprehension. Protect confidentiality, do not prompt the target answer, and log zero-result/abandoned attempts instead of excluding them.

**Worked hypothetical analysis (not a study result):** If five sample users independently choose the correct source first and two recover after a wrong first hit, report 5/7 first-hit and 7/7 eventual discovery **as illustrative arithmetic only**. Actual participant outcomes, confidence intervals and usability gains are NOT VERIFIED until observations exist.

**Decision and governance:** measure pre/post against the same task set; track true positives and false confidence from query ranking. Require review before changing search aliases or hidden relevance weights, test direct links/keyboard/empty states, and record traceable evidence. See [experiment design](experimentation-and-causal-evidence.md), [UX research methods](ux-research-methods.md) and [quality gates](../../governance/quality-gates.md).

**Source scope:** [NN/g's research-method selection](https://www.nngroup.com/articles/which-ux-research-methods/) distinguishes behavioral observation from attitude surveys; it does not provide user results for this catalog. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) provides applicable accessibility outcomes, not an analytics denominator. The `SUS` total is a transformed 0–100 questionnaire score, **not** a percent of users or a task success rate. No actual participant study was conducted for this entry.
