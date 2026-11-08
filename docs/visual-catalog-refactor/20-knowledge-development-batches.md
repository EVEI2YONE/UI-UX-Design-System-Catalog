# 20 — Knowledge development: five context-gathered work packages

**Recorded:** 2026-11-08 · **Single PR:** [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16), `docs/visual-catalog-refactor-blueprint` · **Canonical registry:** 54 entries, unchanged · **Status:** all five **guidance authoring** tasks committed; human/production evidence explicitly remains open.

This ledger documents the **fresh-context gate before each package**. It distinguishes *observed repository context*, *external normative reference*, *our added synthesis*, and *unverified acceptance*. It is a review artifact, not a competing catalog ID registry. The implementation's technical source and earlier reviews remain linked in their existing files.

## KG-08 — Maintainability and composition architecture

**Before editing, repository head:** `a4a11fa04c32ba6fe8ff7a2a0aeb26b25e3398bb` (same draft PR, base `main` at `3b933abea778122dece31af7496f409028ed6198`).

**Read and compared:** `architecture/component-model.md`, `architecture/component-contracts.md`, `architecture/module-boundaries-and-developer-navigation.md`, `foundations/design-tokens-and-themes.md`, `governance/quality-gates.md`, KG-08 work package, source files `Button.js` and `Form.js`.

**Existing coverage:** Reuse/extend/compose, ownership, APIs, tokens, quality evidence and module import rules already exist. An extra canonical "maintainability" concept would duplicate them. The source-linked form is compact; the actual composed pattern code does not import a shared packaged Button. No measured developer comprehension or human source review exists.

**Addition:** [Component model — executable reference maintainability](../../architecture/component-model.md#executable-reference-maintainability-and-composition-contract) defines a layered source ownership matrix, state/DOM readability requirements, extraction decisions, CSS/token reuse boundaries, file co-location and review evidence. **Decision:** extend canonical component model; no new ID, package or implemented refactor.

**Acceptance:** Knowledge authored; actual per-file readability observations, named review and any code refactoring still **NOT VERIFIED**.

## KG-07 — Accessibility, theme and performance

**Before editing, repository head:** `39535b44ef32ccf86f95b2ceb59fca4eabe41b5a`.

**Read and compared:** `guidance/accessibility.md`, `guidance/performance-and-perceived-speed.md`, `guidance/internationalization.md`, `foundations/design-tokens-and-themes.md`, KG-07 work package, `site/src/previews/preview-host.css` and `site/tests/browser-audit.cjs`.

**Existing coverage:** The repository already names semantics, keyboard, WCAG 2.2 AA, localization and field-vs-lab metrics. Existing Chromium tests scan default frames but do not prove manual AT, color-pair contrast, RTL/zoom or field Web Vitals. A standalone token playground is not actually registered.

**External reference checked:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) including 1.4.10 reflow, 2.4.11 Focus Not Obscured (AA) and 2.4.13 Focus Appearance (AAA); [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/); [DTCG format 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) (final Community Group report, **not** a W3C Recommendation); [Core Web Vitals thresholds](https://web.dev/articles/vitals) (field LCP, INP, CLS, 75th percentile).

**Addition:** [Accessibility — reference-state acceptance matrix](../../guidance/accessibility.md#reference-state-accessibility-theme-and-performance-acceptance-matrix) specifies default/pending/error/denied/unknown, focus and announcements, themes, zoom/reflow, RTL, reduced motion, forced colors, manual evidence format and lab/field interpretation. **Decision:** extend accessibility guidance rather than duplicating performance/tokens pages. Keep performance definitions and token mapping with their existing owners.

**Acceptance:** Guidance authored; human AT/contrast/reflow verification and production field performance **NOT VERIFIED**.

## KG-11 — Source usability and distribution

**Before editing, repository head:** `840b389d24a20cf4859c0ea4036952606b43473f`.

**Read and compared:** `architecture/component-contracts.md`, `architecture/module-boundaries-and-developer-navigation.md`, `CONTRIBUTING.md`, actual `site/build.py` source-inspector assembly, `site/README.md` and KG-11 work package.

**Existing coverage:** Source parity, registered implementation/source paths, preview styles, scenario files and optional mock adapter already exist. The source inspector renders exact checked-in JS. A source-copy button, complete packaged download and distribution lifecycle do not.

**Addition:** [Component contracts — source exploration and reuse](../../architecture/component-contracts.md#source-exploration-reuse-and-distribution-contract) defines visible provenance/dependency disclosure, exact-source copy semantics, keyboard feedback, attribution and licensing, optional download manifests and criteria for a separately supported package. **Decision:** no package and no unverified one-click-copy claim; defer these optional UI capabilities pending developer task evidence.

**Acceptance:** Guidance authored; source-copy feature, complete download, real consumer reuse and license clearance **NOT VERIFIED / NOT IMPLEMENTED**.

## KG-12 — Human and agent discovery

**Before editing, repository head:** `9171afafe8a98e1337d93972be96ea51ff1b0c68`.

**Read and compared:** `guidance/ux-measurement.md`, `patterns/task-flows-and-information-architecture.md`, `AGENTS.md`, `scripts/find_concept.py`, Phase 9 retrieval fixture, `catalog/README.md` and KG-12 work package.

**Existing coverage:** Task-flow guidance and UX metrics, a deterministic lexical ranker, curated regression queries and a real scripted Chromium route test already exist. No participant study, observed human task baseline or comparable independent agent-user research has occurred. "Synthetic review" is a recorded no-result query.

**Addition:** [UX measurement — catalog discoverability protocol](../../guidance/ux-measurement.md#catalog-discoverability-and-source-trust-study-protocol) records participant/agent task design, query and semantic-failure categories, denominators, source-trust comprehension checks, agent/tool provenance, privacy-safe observations and alias-change governance. **Decision:** retain existing ranking until research justifies a change.

**Acceptance:** Research protocol authored; user recruitment, observations, time-to-useful-answer and before/after comparison **NOT VERIFIED**.

## KG-10 — Security, hosting and deployment

**Before editing, repository head:** `979ba5828ba940fff4eaa799cf83c5ca4d38ca97`.

**Read and compared:** `governance/quality-gates.md`, `governance/lifecycle-and-decisions.md`, Phase 10 release decision, `.github/workflows/catalog-validation.yml`, `site/build.py`, `site/README.md` and KG-10 work package.

**Existing coverage:** Static builder, root-absolute URL paths, reference iframe `sandbox="allow-scripts"`, CI-only `npm install --no-package-lock`, source-ref pinning and unapproved hosting/security decisions. No live site CSP or lockfile/license audit exists. The Phase 10 NO-GO remains valid.

**External reference checked:** [OWASP CSP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html), [MDN iframe sandbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox), [npm ci](https://docs.npmjs.com/cli/commands/npm-ci/). The sample CSP is explicitly a **review starting point**, not a configured or tested header.

**Addition:** [Quality gates — hosting, supply chain and preview security](../../governance/quality-gates.md#static-visual-catalog-hosting-supply-chain-and-preview-security-gate) describes origin/base-path selection, pinned source provenance, iframe/CSP threat boundaries, reproducible locked CI dependencies, license and privacy requirements, host-specific security validation and rollback evidence. **Decision:** no host/deploy, no silent addition of sandbox permissions, and no claim of security approval.

**Acceptance:** Guidance authored; lockfile, license/vulnerability evidence, host/CSP policy, public deployment and named release approval **NOT VERIFIED**.

## Consolidated handoff and invariants

| Work package | Canonical content | Documentary outcome | Still requires observation/decision |
| --- | --- | --- | --- |
| KG-08 | Component model | **FILLED — guidance authored** | Human source audit and any actual refactor |
| KG-07 | Accessibility | **FILLED — verification matrix authored** | Manual AT/contrast/RTL/zoom and field metrics |
| KG-11 | Component contracts | **FILLED — source reuse contract authored** | Copy/download decision, integration usability and licensing |
| KG-12 | UX measurement | **FILLED — study protocol authored** | Participant and agent research |
| KG-10 | Quality gates | **FILLED — release governance authored** | Hosting/CSP/SCA/license signoff and deployment decision |

**No new canonical IDs; no change to 54 registered concepts; no deployment or package release; no claimed user research.** Each open work-package file remains as a durable record for actual validation, not a duplicate missing knowledge section. Keep [Phase 10's release NO-GO](16-phase-10-release-readiness.md) until its evidence and owner gates are satisfied.

## Verification plan

Run `python3 scripts/validate_catalog.py`, root `unittest` discovery (including [knowledge coverage regressions](../../tests/test_knowledge_development.py)), `python3 site/build.py`, site `unittest`, Node source tests and Chromium/axe CI. Test that all five new canonical sections are reachable, have appropriate source/measurement qualifiers, are distinct from historical provenance notes, and do not introduce visible phase/batch/PR labels. CI completion demonstrates repository contract consistency, **not** human review.
