# UX experimentation and causal evidence

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose and boundaries

Determine whether a specific product change causes a relevant user outcome under a trustworthy experiment design. **Use when** two sufficiently safe variants can be allocated fairly and evaluated with reliable measurements. **Avoid when** a team lacks an ethical/accessible comparison, the question is fundamentally qualitative, the expected effect cannot be measured reliably, or traffic is too limited for a useful conclusion.

[UX measurement](ux-measurement.md) owns basic outcomes, event denominators and UX metrics; [research methods](ux-research-methods.md) owns the choice between research methods. This entry owns **experimental assignment, design, inference quality, guardrails and decision process**. Statistics and privacy teams must approve a specific analysis, not infer validity from a pattern document.

## Pre-register an experiment contract

Record before exposing participants:

| Field | Contract |
| --- | --- |
| Decision and hypothesis | What action will change, what mechanism is expected, and which observation would not support it |
| Target population | Eligibility, sample frame, geography/locale, access needs, excluded users and practical ethical constraints |
| Unit of randomization | User/account/session/tenant/cluster, chosen to limit spillover and dependence; record persistent assignment strategy |
| Variants and exposure | True control, exact changed elements, traffic split, first exposure event and treatment fidelity |
| Outcome | One primary task outcome with versioned definition, denominator and analysis window; supporting diagnostics |
| Guardrails | Accessibility, safety, privacy, conversion/task errors, crashes, latency, equity and support burden |
| Statistical plan | Planned minimum detectable effect, variance/power assumptions, sample and duration, uncertainty intervals, stopping/monitoring rule |
| Data quality | Event loss, duplicates, sample ratio mismatch (SRM), missingness, assignment integrity, simultaneous experiments |
| Decision policy | Ship/iterate/reject/rollback, owner, what makes results inconclusive and follow-up qualitative research |

Use an **A/A dry run** when instrumenting a new experimentation system to catch assignment and logging problems; an A/A success does not prove future A/B outcomes. Preserve both intended assignment and observed exposure, taking care not to condition analysis on outcomes caused by treatment.

## Trustworthy execution and analysis

1. Randomize at a defensible unit and keep assignment stable; document users/tenants who can cross variants or devices. If users influence one another, account for clusters/interference.
2. Validate the **sample ratio mismatch** against the **planned allocation**, using a statistical test appropriate for the allocation and sample. A detected SRM is a data-integrity blocker; diagnose before trusting a positive result.
3. Predefine primary vs exploratory measures; consider multiple comparisons and cohort slicing. Post-hoc selection may generate hypotheses, not a confirmed primary success.
4. Choose **fixed-horizon** or a properly specified **sequential/anytime-valid** method up front. Do not repeatedly peek at ordinary fixed-horizon p-values and stop as soon as one crosses a threshold.
5. Evaluate an effect estimate with confidence/credible interval and practical magnitude, not only a binary p-value or a “lift” screenshot.
6. Look for guardrail deterioration, accessibility harms, failure segments and device/locale differences; disclose power limits before attributing apparent subgroups.
7. Distinguish *statistically inconclusive* from *no effect*; treat missing, duplicate and imbalanced events as data-quality uncertainty.
8. Review the real product task and participation context. A measurable click increase can be a misleading optimization if users cannot complete the job or support complaints rise.
9. Document the release state and rollback method. The experiment's allocation system must not silently change server-side authorization.

## Example and anti-example

**Illustrative design:** A product tests clearer review-stage labels against the current form. It randomizes by authorized user ID, predefines server-confirmed successful submissions per eligible task attempt, checks SRM and event completeness, and monitors field errors, accessibility regressions and latency as guardrails. A task study investigates why outcomes differ.

**Anti-example:** A dashboard tests eight button variants, changes traffic allocation after seeing early results, checks p-values each hour, selects a “winning” segment that wasn't preplanned and claims statistically proven causation despite an SRM.

## Evidence and release worksheet

| Check | Status | Minimum evidence |
| --- | --- | --- |
| Hypothesis, assignment unit, analysis/stopping plan | NOT VERIFIED | Registered plan and variant policy |
| SRM, exposure and instrumentation health | NOT VERIFIED | Sample counts, test result, missingness |
| Primary metric, interval and practical effect | NOT VERIFIED | Reproducible analysis with uncertainty |
| Safety, accessibility and locale guardrails | NOT VERIFIED | Multi-device audits and segment analysis |
| Human/subject-matter review and ship decision | NOT VERIFIED | Owners, signoffs and rollback |
| User research on reasons for observed change | NOT VERIFIED | Study transcripts/findings with limitations |

**Causal-claim rule:** with valid randomization, reliable observation, stable assignment and appropriate inference, an experiment may support a limited causal inference **for its studied population and conditions**. A before/after change, a poorly powered test or an SRM-affected result does not establish causal benefit.

## Sources and applicability

- [Microsoft Research: Diagnosing Sample Ratio Mismatch in A/B Testing](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) (2020; consulted 2026-11-07): assignment, logging and analysis bias; practitioner explanation of SRM as a must-investigate quality problem.
- [Microsoft Research: Data Quality for Trustworthy A/B Testing](https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) (2021; consulted 2026-11-07): metric, logging and selection-quality cautions.
- [Microsoft Research: Trustworthy analysis of online A/B tests](https://www.microsoft.com/en-us/research/publication/trustworthy-analysis-of-online-a-b-tests-pitfalls-challenges-and-solutions/) (2017): randomization-unit assumptions and variance pitfalls; research context, not a packaged sample-size rule.
- [Optimizely: Fixed horizon, Bayesian, or sequential](https://www.optimizely.com/field-notes/articles/how-to-choose-the-right-stats-engine) (2026; consulted 2026-11-07): vendor explanation of sequential monitoring; **not** neutral proof of correctness for a specific product/tool.
- [GOV.UK Service Manual: User research in live](https://www.gov.uk/service-manual/user-research/user-research-in-live) (2016; consulted 2026-11-07): A/B testing as one method among qualitative user research and analytics; public-service context.

**Canonical ID:** `guidance.experimentation` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [UX measurement](ux-measurement.md), [UX research](ux-research-methods.md), [quality gates](../governance/quality-gates.md), [privacy/trust](privacy-consent-and-trust.md), [performance experience](performance-and-perceived-speed.md).
