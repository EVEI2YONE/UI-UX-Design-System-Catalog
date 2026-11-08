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


## Collaborative reviews and shared-value journeys (2026-11-07)

Use journey-aligned metrics instead of generic dashboard engagement. Prioritize **submission completion** (server-confirmed successful contributions / eligible started attempts), **review turnaround** (median and p75 elapsed from submission to first substantive decision), **return/rework** (returned submissions / eligible reviewed submissions, with reasons), **review correctness** (authorized corrections and error-severity categories), **reward fulfillment** (fulfilled / eligible requested, with pending age), and **scope confusion** (project-switch recovery or wrong-scope attempts from qualitative research). Record eligible cohort, event version, timezone, deduplication and cancellation separately. Compare owner-managed and independently authenticated workflows only if those distinct populations exist.

For toggled-off features, mark related metrics **NOT APPLICABLE** to the disabled period, not zero performance. For offline/timeouts, distinguish server-confirmed transactions from UI requests. Never capture contribution descriptions, private member details, or other sensitive content in telemetry. No Little Wins baseline or causal effect has been verified in this catalog change.

## B04 — interaction-effort measurement without click-count tunnel vision (CKG-14; proposed 2026-11-07)

**Purpose:** test whether an interaction consolidation or stable action region improves real user tasks while protecting comprehension, safety and inclusive access. This extends the existing [TCR, time, errors and privacy contract](#core-metrics); [advanced interactions](../patterns/advanced-interactions-and-reversible-actions.md) owns choosing buttons, toolbars, menus, split actions and shortcuts. [Task flows](../patterns/task-flows-and-information-architecture.md) owns spatial/next-action layout and scope.

### Operational task-cost worksheet

Fix a **task start** and **authoritative completion** event, eligible cohort, observed device/input modality, viewport/zoom and same work complexity before comparing versions. Optional, secondary effort measures follow; none replaces successful completion.

| Measure | Operational definition and unit | Interpretation / limit |
| --- | --- | --- |
| Pointer travel | Sum of distances between successive task-relevant pointer positions in **CSS pixels** during eligible pointer tasks; record sampling/missingness and normalization by task/viewport when comparing | Describes travel burden, not motor effort or universally optimal pixels; not applicable to keyboard-only attempts |
| Pointer target relocations | Count of unexpected action-target position changes during the same task, especially after async updates | May reveal unstable actions; distinguish deliberate responsive reflow |
| Click/tap activations | Count **intentional activations** per eligible task attempt, separated by successful, cancelled and incomplete attempts | Fewer clicks is not inherently better if confirmations protect users |
| Keyboard navigation effort | Tab/Shift+Tab/arrow activations or focus transitions to target, with missed/stranded focus reported separately | Modality-specific; do not compare raw counts to mouse travel |
| Scroll/viewport interruptions | Count of substantial manual scroll changes or independent scroll-container switches on the way to the next required action; define threshold before study | Detects reorientation, not a universal optimum |
| Re-entry and re-selection | Count of repeated entries of unchanged values or repeated item selections caused by refresh/navigation | Must distinguish deliberate correction or change in authorized scope |
| Time to next actionable item | Elapsed **milliseconds/seconds from authoritative completion of prior item** to first intentional action on the next **eligible** item; report unavailable/abandoned cases separately | Do not measure from an optimistic click; do not exclude slow or failed attempts silently |
| Comprehension/safety | Rate of users who can correctly predict consequences, plus task errors, duplicate attempts, permission/scope confusion and recovery | Guardrail against overcompressed, ambiguous controls |

**For pointer telemetry**, record only consented, minimized, task-scoped interaction measurements; do not collect raw screen recordings, exact private text, sensitive item coordinates, names or identifiers without explicit privacy/legal review. In many cases moderated observation, aggregate interaction counts and coarse positioning categories are preferable to collecting continuous trajectories.

### Study and inference protocol

1. State the **hypothesis** (e.g., keeping a review action bar stable reduces re-selection), selected task, candidate variants, eligible user cohort, baseline and target condition. If actual baseline is unavailable, label it **UNKNOWN** rather than inventing counts.
2. Define **confirmed success** independently of UI intent. Preserve failure, cancellation, partial and uncertain outcomes in the denominator policy; do not classify them all as valid zero-duration successes.
3. Compare equivalent tasks under matched devices, viewports, zoom, task complexity, input modality and permissions. Include novice and returning users when relevant; describe observed differences without causal claims unless the study design justifies them.
4. Report TCR, error severity, time distributions and recovery alongside any pointer/step reduction. Stratify keyboard, touch and assistive technology separately; never give nonpointer attempts a fabricated pointer distance of zero.
5. Review discoverability, comprehension, focus, translation/RTL, touch, safety and server-correctness guardrails; do not adopt an optimization if fewer actions increase consequential mistakes.
6. Record consent/data minimization, versioned instrumentation, missing events, confidence limitations, decision owner, rollout/rollback and actual PASS/FAIL/NOT VERIFIED results.

**Illustrative example:** version A requires choosing a new record after each acknowledged review; version B presents the next eligible item in a stable pane. Compare completion, decision correctness, time-to-next-action, focus recovery and deliberate stops across matched sessions. Without observed attempts, both a faster pointer path and its actual benefit remain hypotheses.

**Anti-example:** declare a 50% UX improvement because a prototype uses two buttons instead of four, while ignoring hidden Reject, lost keyboard access, unverified approvals and users who abandon the task.

### B04 verification status

| Evidence | Required before claiming improvement | Status |
| --- | --- | --- |
| Task definition, cohort and baseline | Versioned start/success events, validated attempts and sampling | NOT VERIFIED |
| Input-modality coverage | Pointer, keyboard, touch, assistive technology where applicable | NOT VERIFIED |
| Outcome and error safeguards | TCR, server correctness, recovery, scope/permission errors | NOT VERIFIED |
| Privacy-respecting instrumentation | Purpose limitation, data minimization, consent and retention review | NOT VERIFIED |
| Controlled/observational interpretation | Study design, uncertainty, consistent comparable tasks | NOT VERIFIED |

**References:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [Nielsen Norman Group: Measuring UX](https://www.nngroup.com/articles/which-ux-research-methods/) (method-selection starting point, not proof of a specific metric threshold), and [experimentation guidance](experimentation-and-causal-evidence.md) (consulted 2026-11-07). Context: proposed Little Wins B06 effort metrics and B07 action-consolidation patterns; product baselines remain unknown.


## Catalog discoverability and source-trust study protocol

The catalog supports *two different journeys*: a person browsing a source-linked visual reference and an agent retrieving a canonical ID with a deterministic lexical ranker. Successful automation for those journeys is not evidence that representative people or independent agents find the right design rule or judge its trust correctly.

### Test questions and hypotheses

| Job | Research question | Acceptable evidence |
| --- | --- | --- |
| Find a control contract | Can a user identify the correct canonical owner from a natural-language task? | First chosen concept, correction path and rationale |
| Understand spec-only status | Can a user tell proposed guidance from runnable reference and from certified library? | User explanation without prompting, misinterpretation notes |
| Find relevant recovery guidance | Can a participant distinguish unknown outcome, known failure and retry safety? | Selected canonical concept and reason for action |
| Reuse source safely | Can a developer locate JS, CSS, fixtures, adapter and installation constraints? | Files found, omitted dependencies and unauthorized production assumptions |
| Distinguish approval workflows | Does a user choose human Review Workspace versus AI-agent delegated approval appropriately? | Correct task-owner selection and reasoning |
| Search an unfamiliar synonym | Does `synthetic review` reveal a gap that a reasonable user could recover from? | Query sequence, no-result behavior, fallback navigation, candidate synonyms |

### Study design before collecting results

Specify study owner, study date, target roles (designer, frontend engineer, accessibility reviewer, agent/tool integrator), experience level, device/assistive-technology context, number invited/completed and any exclusions. Recruit people who have not authored the catalog where feasible. Use neutral tasks without canonical ID or direct solution terms. Randomize or counterbalance task order across participants to limit learning effects. Record whether participants received training or saw previous solutions.

For a paired human/agent comparison, provide agents the same user intent, allowed tools, repository revision and explicit constraints. Preserve the actual prompts, retrieved IDs, rank, sources inspected, tool version and outcomes. Distinguish ranking correctness from whether the selected guidance actually resolves the user's need. Do not aggregate human and machine "success" into one indistinguishable score.

### Measures and reporting

| Measure | Definition | Watch out for |
| --- | --- | --- |
| First-hit relevance | Eligible tasks where first opened/selected result is correct, divided by eligible tasks | Rank one is not always uniquely correct for ambiguous terms |
| Task completion | Tasks resolved to a suitable canonical source with correct applicability, divided by eligible tasks attempted | A correct clicked URL without comprehension is incomplete |
| Time to first useful concept | Elapsed time from task start to first suitable source, by task/participant | Include failures/censoring rather than dropping them |
| Query reformulations | Number and category of edited phrases before a useful result | High counts may mean vague task phrasing, not only a ranking defect |
| Incorrect maturity inference | Tasks where user treats proposal or mock adapter as production approval | Source preview presentation may amplify misplaced trust |
| Dependency completeness | Required source/scenario/style/adapter files correctly identified divided by required files | One file found does not prove safe integration |
| Accessible task recovery | Screen-reader/keyboard user can find an error/empty state and continue | Distinguish information access from a completed workflow |

Use counts and denominators, per-task context, failures, median and spread where sample size supports them; do not invent statistical significance from a tiny exploratory study. Keep qualitative remarks anonymized and separate direct observations from researcher inference. Never collect passwords, production records or sensitive identities for the study.

### Relevance changes and governance

1. Freeze a registry revision and run the existing `tests/fixtures/phase9_retrieval_cases.json` suite as the automated *baseline*.
2. Record new organic queries, intended task, all plausibly relevant canonical owners and the participant's expectation. A query like `settings` can correctly yield multiple results; no forced winner.
3. Classify failure: missing concept, poor alias, unclear title/summary, incorrect task hierarchy, source-status confusion, rendering/navigation problem or inadequate user training.
4. Suggest the smallest remedy: clearer public wording or synonym, navigation signpost, linked related concept, task-specific index alias, or a genuinely missing contract. Avoid changing scoring weights to mask ambiguous data.
5. Review candidate improvements against the unchanged exact ID/alias ranking, all historical fixtures, known misses and human outcomes. If an alias creates an overlap, record the tradeoff explicitly.
6. Re-run comparable tasks with a separately documented sample. Report adverse effects and follow-up questions instead of claiming a universal discovery improvement.

### Worked hypothetical analysis (not a study result)

Suppose a developer searches for "synthetic review", sees no result, then finds `feature.review-workspace` through "human approval queue". This would show *recovery through reformulation*, not first-hit success. A candidate alias is only justified if review confirms the phrase refers to that human review workflow rather than an agent approval or testing concept. Record that distinction and test both before changing the index.

**Current evidence:** the deterministic agent lookup has curated acceptance fixtures, and real Chromium confirmed a scripted human approval queue route. **NOT VERIFIED:** participant cohort, independently observed task completion, source-comprehension baseline and agent/human comparative study. No such study has been run. This protocol is documented knowledge; [KG-12 work package](../docs/visual-catalog-refactor/gap-work/kg12-discovery-research.md) remains open for actual research.
