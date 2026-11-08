# 17 — Durable concept inventory and decision ledger

**Date:** 2026-11-08 · **Repository:** [draft PR #16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16) · **Decision authority:** human catalog/design owner, unassigned  
**Purpose:** close the *knowledge preservation* gap left by Phases 0–10: keep all proposed concepts reviewable even when they are **not** promoted into the canonical registry or implemented. This document records decisions, not approval to implement, merge or publish.

## Ownership and status contract

- **Canonical** = a reviewed/registered concept identity lives in `catalog/index.json`; the Markdown at its `path` is the normative source. Its separate review lifecycle `status` may still be `proposed`.
- **Candidate** = an explicitly noncanonical concept brief under `docs/visual-catalog-refactor/concepts/`, indexed only in [the decision manifest](concepts/decision-manifest.json). A proposed identifier is **not an allocated canonical ID** and does **not** create an executable preview.
- **Disposition** describes what happened to the *proposal*: `registered-reference` (new spec and checked-in code, human review still pending), `covered-existing` (existing canonical guidance/implementation is the current owner; a larger proposed experience may remain unverified), or `deferred` (concept retained for evidence/ownership review, not rejected).
- **Rejected / merged** require a written owner decision and a destination or rationale; no such decision has been approved for these ten concepts.
- **Verification** is orthogonal: authored, implemented, CI-tested, manually reviewed and production adopted are different evidence states. These records do not confer adoption, review date or ownership.

The [machine-readable decision manifest](concepts/decision-manifest.json) is a **derived governance inventory** for the concept briefs, never an alternative to `catalog/index.json`. The [preservation tests](../../tests/test_concept_preservation.py) enforce identities, referenced files and nonregistration of deferred proposals.

## Stage 3: five feature concept decisions

| Origin | Durable concept artifact | Disposition | Canonical ownership / action |
| --- | --- | --- | --- |
| F-01 Review Workspace | [Canonical feature specification](../../features/review-workspace/spec.md) | **Registered reference**; `feature.review-workspace` exists, `status=proposed`; synthetic example implemented and tested | Human approval queue, not AI-agent tool approval; retain until owner validation |
| F-02 Data Management Workspace | [F-02 concept brief](concepts/f02-data-workspace.md) | **Deferred**; proposed `feature.data-workspace` not registered | Existing `pattern.data-tables` + `pattern.search-filter`; require distinct cross-pattern orchestration evidence |
| F-03 Settings Center | [F-03 concept brief](concepts/f03-settings-center.md) | **Deferred**; proposed `feature.settings-center` not registered | Extend existing `pattern.account-settings-portal` rather than duplicating it; prove executable-specific gap |
| F-04 Onboarding Workflow | [F-04 concept brief](concepts/f04-onboarding-flow.md) | **Deferred**; proposed `feature.onboarding-flow` not registered | `pattern.task-flows`, `pattern.forms` and recovery; justify independent progress/resume contract |
| F-05 Analytics Overview | [F-05 concept brief](concepts/f05-analytics-overview.md) | **Deferred**; proposed `feature.analytics-overview` not registered | `guidance.data-visualization`, measurement and tables; require trustworthy metric context and accessibility evidence |

**F-01 caveat:** its code is a synthetic reference and the canonical review status is still `proposed`. Registration is a factual state, not human acceptance of the reuse hypothesis. The other four concepts are **not discarded** and must not be called implemented or published.

## Stage 2: five composition concepts and overlaps

| Origin | Durable concept artifact | Disposition | Existing owner / decision |
| --- | --- | --- | --- |
| C-01 Search/filter collection | [C-01 brief](concepts/c01-search-filter-collection.md) | **Covered-existing** | `pattern.search-filter` and `pattern.data-tables` have source-linked examples; no extra feature justified yet |
| C-02 Responsive information dashboard | [C-02 brief](concepts/c02-responsive-information-dashboard.md) | **Deferred** | `guidance.data-visualization`; overlaps F-05 analytics overview; no fabricated metrics |
| C-03 Feedback center | [C-03 brief](concepts/c03-feedback-center.md) | **Deferred** | `pattern.feedback`, `pattern.interaction-recovery`, `pattern.notifications-attention`; no duplicate normative feedback source |
| C-04 Workspace navigation shell | [C-04 brief](concepts/c04-workspace-navigation-shell.md) | **Covered-existing** | `pattern.navigation` (interactive preview) and `pattern.role-aware-workspaces` (canonical guidance); full shell integration remains unverified |
| C-05 Onboarding composition | [C-05 brief](concepts/c05-onboarding-composition.md) | **Deferred** | Existing forms/task-flows/recovery; overlaps F-04; no fake resume persistence |

**Coverage is not implementation certification.** C-01 and C-04 refer to portions of existing patterns; their complete candidate compositions were **not** promoted into independent features. Future changes require explicit decision evidence.

## Stage 1: mapped concepts preserved by canonical owners

The original [concept expansion plan](02-concepts-and-content-plan.md) also listed existing references for `component.button`, `component.input`, `component.field`, `component.dialog`, `pattern.forms`, `pattern.navigation`, `pattern.interaction-recovery` and `foundation.design-tokens`. They were **not** new conceptual gaps requiring duplicate IDs: the original canonical documents remain authoritative. Six component and five pattern examples were committed under Phases 4–6. A **standalone foundation token playground** was *proposed*, but was not registered as an independent source-linked implementation; the theme controls used by previews do not by themselves constitute the full token playground. Keep that distinction for prioritization.

## Knowledge-gap audit closure ledger (KG-01 through KG-12)

This table updates the **2026-11-08 baseline** in [the original gap audit](03-knowledge-gap-audit.md); it does not overwrite historical classifications or claim that implementation proves human acceptance.

| Gap | Knowledge artifact and observed resolution | State remaining |
| --- | --- | --- |
| KG-01 Registry-to-preview contract | `catalog/schema.json`, `scripts/validate_catalog.py`, `catalog/index.json` optional typed mappings | **Implemented / automated validated**; canonical review pending |
| KG-02 True source/preview parity | `site/build.py`, source inspector, site tests and Phase 4 ledger | **Implemented / automated validated**; human code review pending |
| KG-03 Catalog IA and fallback | `site/build.py` + static site, Phase 3 and Chromium evidence | **Implemented / automated tested**; human visual review pending |
| KG-04 Synthetic isolated scenarios | `site/src/previews/`, real fixture sources and Review Workspace adapter | **Implemented / automated tested**; security signoff pending |
| KG-05 Full feature contracts | `features/review-workspace/spec.md` canonical; F-02–F-05 briefs above | **One specified reference; four candidate briefs preserved**; cross-product reuse unverified |
| KG-06 Core control previews | Six component implementation folders, catalog metadata and Phase 5 tests | **Implemented / automated tested**; AT signoff pending |
| KG-07 Theme/contrast/performance verification | Preview themes, Phase 8 Chromium/axe and build-size budgets | **Partial verification**; manual contrast/AT and production Web Vitals not verified |
| KG-08 Readability and maintainability guidance | Existing typography/content/architecture guidance; code-readability follow-up in Phase 8 ledger | **Previously covered**; independent source readability review not verified |
| KG-09 Agent discovery for previews | `AGENTS.md`, Phase 9 fixtures, source audits and preserved resolver | **Implemented / automated tested**; documented `synthetic review` miss remains |
| KG-10 Deployment/security/performance | Phase 10 risk register and CI checks | **Unresolved release gate**: hosting/base path/CSP, dependency licenses, security approval and field metrics |
| KG-11 Searchable source / optional distribution | Verbatim source inspector in site; no installable packages by design | **Partially met**: source inspection works, copy/download convenience unimplemented; distribution deferred intentionally |
| KG-12 Discoverability research | Agent task regression and sampled Chromium human-facing query in Phase 9 | **Partially tested**: no actual participant research, task-success benchmark or usability baseline |

**No gap should be reported fully closed solely because a document exists.** The terms above deliberately separate **concept recorded**, **implementation delivered**, **automated evidence**, **human acceptance**, and **production adoption**.

## Rejection, merging, and promotion procedure

1. Search the canonical registry by exact ID, aliases, intended task and related owner before proposing a new canonical entry.
2. Read the relevant [candidate brief](concepts/decision-manifest.json) and existing normative guidance; write down the **reuse/extend/merge/create** decision and why the current owner is insufficient.
3. Supply credible evidence across at least two independent application contexts or a documented strategic exception; specify accessibility, localization, responsive, performance, error/recovery and service boundaries.
4. Name the responsible catalog/design reviewer, record their actual decision and date, and update the candidate brief and decision manifest together. Do not invent an owner or date.
5. **Only after review**, create any new canonical `features/<slug>/spec.md` and registry `id`; add implementation metadata only when actual source and scenarios exist. Preserve existing canonical IDs and link prior decisions.
6. Run the catalog validator, source/provenance/route tests, browser CI where applicable and the concept preservation suite. If a concept is rejected or merged, preserve its concept history and point to the canonical destination.

## Signoff and handoff

**Documentary completeness:** all **five Stage 3 feature concepts** and all **five Stage 2 compositions** have durable references; nine now have dedicated candidate briefs, and F-01 has its existing canonical specification.  
**Human concept disposition signoff:** **NOT RECORDED**. `owner=unassigned` is not approval.  
**Production release:** remains **NO-GO** under [Phase 10 review](16-phase-10-release-readiness.md), draft PR #16.  
**No canonical mutation:** the 54 registry entries and lookup ranking remain unchanged by this inventory.

## Visitor-facing copy and unresolved knowledge follow-up

The site retains canonical subject matter but removes build-phase, batch and PR tracking language from page presentation. Source Markdown keeps its original historical text and anchor IDs for provenance. The open review/release/research evidence gaps are now independently recorded as five role-scoped [durable work packages](19-open-knowledge-work.md), with automated preservation tests, without treating the packages as canonical concepts.
