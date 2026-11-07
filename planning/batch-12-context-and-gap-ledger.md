# Batch 12 — Evaluation, performance and delivery context-first gap ledger

**Date:** 2026-11-07 · **Branch/PR:** cumulative draft [PR #5](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/5) on `docs/ux-knowledge-expansion-batches-7-12`. **Status:** proposed guidance, not a product launch or certification.

## Canonical catalog intake before writing

Reviewed the 38-entry registry at Batch 11 completion, especially `guidance.ux-measurement`, `guidance.ux-research`, `governance.quality`, `governance.lifecycle`, `foundation.design-tokens`, `architecture.component-contracts`, `architecture.component-model`, the section indexes, `CONTRIBUTING.md` and the Batches 7–12 plan.

| Candidate | Existing knowledge and gap | Disposition |
| --- | --- | --- |
| Operational/perceived performance | Interaction recovery describes pending/timeout; UX measurement defines task success. Neither defines web performance metrics, field-vs-lab evidence, progressive readiness or performance budgets. | **Create** `guidance.performance-experience`; **extend** `guidance.ux-measurement` and `governance.quality`, reuse recovery/offline semantics |
| Experimentation/A/B testing | UX measurement mentions observational causal limits, but not randomization, sample ratio mismatch, A/A checks, stopping rules and experiment guardrails. | **Create** `guidance.experimentation`; **extend** `guidance.ux-measurement` and release quality checks; do not duplicate research-method choice |
| DesignOps/design-to-code handoff | Existing component contracts, token architecture, lifecycle and release quality gates already define the correct ownership boundaries, but they lack a versioned source-to-code evidence bundle. | **Extend** `architecture.component-contracts`, `foundation.design-tokens`, `governance.lifecycle`, `governance.quality`; **no new governance ID** |

The audit concerns this repository's reusable knowledge, **not observed defects in a target app**.

## Research sources and applicability

- [web.dev Core Web Vitals](https://web.dev/articles/vitals) and [threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds), consulted 2026-11-07: current good web p75 thresholds LCP ≤2.5s, INP ≤200ms, CLS ≤0.1. These are web field indicators, not proof of native app UX or individual task completion.
- [web.dev User-centric performance metrics](https://web.dev/articles/user-centric-performance-metrics), [Optimize INP](https://web.dev/articles/optimize-inp) and [Optimize CLS](https://web.dev/articles/optimize-cls), consulted 2026-11-07: field/lab distinctions, responsiveness/shift causes, and constraints on loading feedback.
- [Microsoft Research, Diagnosing SRM](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/), [Data Quality for Trustworthy A/B testing](https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) and [Trustworthy analysis of online A/B tests](https://www.microsoft.com/en-us/research/publication/trustworthy-analysis-of-online-a-b-tests-pitfalls-challenges-and-solutions/), published 2017–2021, consulted 2026-11-07: randomization, exposure/metric validity and causal inference limits; not a fixed sample-size recipe.
- [GOV.UK User research in live](https://www.gov.uk/service-manual/user-research/user-research-in-live), consulted 2026-11-07: A/B alongside qualitative methods; public-service context.
- [Optimizely fixed/sequential testing explainer](https://www.optimizely.com/field-notes/articles/how-to-choose-the-right-stats-engine), 2026: vendor-provided, not a neutral guarantee for a particular statistics implementation.
- [DTCG Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), final W3C Community Group report published 2025-10-28: **stable** interchange specification, **not a W3C Recommendation**. Do not treat the 2026 preview drafts as normative.
- [Playwright screenshot comparisons](https://playwright.dev/docs/test-snapshots) and [Storybook UI testing](https://storybook.js.org/docs/writing-tests/index), consulted 2026-11-07: optional tooling examples, **not** installed or executed in this catalog.

## Acceptance and evidence contract

- [x] Search current canonical registry, aliases and relevant existing pages before declaring gaps.
- [x] Research authoritative performance, experiment, token and visual-regression sources; distinguish standards from platform/vendor practices.
- [x] Add new concepts only for distinct performance and causal-experiment decisions; extend existing DesignOps ownership/lifecycle instead of duplicating it.
- [x] Record examples, anti-examples, performance/experiment and inclusive test cases; preserve proposed status and existing IDs.
- [x] Update canonical index, navigation/agent discovery, source ledger, changelog and regression tests.
- [ ] Confirm complete repository CI `scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` for the exact batch commit; append observed run ID and result.
- [ ] Obtain actual product performance baselines and application-level experiment, token export, visual, keyboard/screen-reader, RTL and release testing. **NOT VERIFIED**.
- [ ] Assign responsible human owners and review source editions. New concepts remain `proposed`, `owner: unassigned`, `reviewed_at: null`.

**Scope:** Proposed knowledge and test contracts only; no app code, product experimentation, CI visual tool installation, metrics collection, lifecycle promotion or unapproved merge.
