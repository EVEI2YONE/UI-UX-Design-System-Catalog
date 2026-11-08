# 15 — Phase 9: agent discovery, governance and release handoff

**Delivery:** draft PR [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16), branch `docs/visual-catalog-refactor-blueprint` targeting `main`  
**Phase scope:** retrieval parity, stable canonical identity, source provenance, contribution contracts and Phase 10 readiness  
**Date:** 2026-11-08  
**Status:** automated acceptance **PASS** at commit `0580c5f18bbc416bae0ab5d3179556a313d7621e` — [GitHub Actions run 42488859952](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42488859952). Both catalog/provenance and Chromium jobs passed. Human review, production security, manual AT and deployment remain **PENDING / NOT VERIFIED**.

## Context gathered

Phase 8 produced a statically generated catalog with **54** entries, **12** interactive references and **42** spec-only entries, with Chromium/axe and source-level test evidence. There is one authoritative `catalog/index.json` identity index, readable Markdown specifications, strict optional `implementation` metadata, `scripts/find_concept.py` for weighted agent retrieval, and `site/build.py` generating browse routes and a derived `catalog-search.json`.

The baseline `main` commit audited at Phase 0 was `3b933abea778122dece31af7496f409028ed6198`, with 53 concepts. The only new canonical concept in the refactor is `feature.review-workspace`; legacy identities, paths and reviewed status values were preserved in the Phase 7 comparison. All 54 canonical records remain `proposed`; 12 implementations are independently marked `reference`. These are not approval, product integration or live deployment claims.

## Decisions and artifacts

| ID | Decision | Location / consequence |
| --- | --- | --- |
| P9-D01 | Registry remains the only source of canonical ID/alias/status/document path | `catalog/index.json`; no second manual website index |
| P9-D02 | Keep legacy lookup ranking unchanged (exact ID > alias > title > text) | `scripts/find_concept.py` unchanged; existing queries protected |
| P9-D03 | Treat task retrieval as measurable acceptance with expected ownership and negative cases | `tests/fixtures/phase9_retrieval_cases.json` and `tests/test_phase9_discovery.py` |
| P9-D04 | Treat website route and rendered source as derived contract, not authority | Static build and source-parity tests verify entries and preview code |
| P9-D05 | Emit CI-only provenance/retrieval evidence from canonical inputs | `scripts/audit_discovery.py`, artifact `catalog-discovery-audit` |
| P9-D06 | Separate normative guidance claims from source-code and observed verification claims | `AGENTS.md`, `CONTRIBUTING.md`, `catalog/README.md` |
| P9-D07 | Record known misses without silently retuning search weights | `synthetic review` query intentionally recorded as a gap |
| P9-D08 | Keep PR draft through Phase 10 human/release and external-review gates | No default-branch changes or deployment approved |
| P9-D09 | Pin generated GitHub source URLs to a validated review revision in CI | `CATALOG_SOURCE_REF` is validated; GitHub Actions uses PR head SHA, local builds default to `main` unless explicitly configured |

## Human and agent journeys and provenance

**Human journey:** open locally generated `/catalog/`, search for `human approval queue`, open `/catalog/features/review-workspace/`, read the canonical specification, inspect the code, scenarios and synthetic adapter, and follow cross-reference links. Chromium checks the search-to-canonical-detail route as a real interaction.

**Agent journey:** execute `python3 scripts/find_concept.py "human approval queue" --json --limit 5`, select canonical `feature.review-workspace`, inspect `features/review-workspace/spec.md`, then inspect `site/src/implementations/features/review-workspace/ReviewWorkspace.js`, colocated `scenarios.js` and `mock-adapter.js` if the task concerns executable behavior. Check `avoid_when`, related IDs, review status, and supporting test evidence. Never assume synthetic authorization or server persistence.

**Distinct authority case:** human record moderation is `feature.review-workspace`; AI-agent delegated tool approval is `pattern.agentic-actions`. These are related but not interchangeable. The exact phrase `synthetic review` currently has no lookup result and is a known search-coverage gap. Ambiguous `settings` may return several valid concepts; don't force one owner without disambiguation.

### Trace example

| Claim type | Required source | Example |
| --- | --- | --- |
| Normative guidance | Canonical ID + Markdown `path` | `component.dialog` → `components/dialog/spec.md` |
| Executable reference | `implementation.source_path`, scenario and preview route | `feature.review-workspace` → checked-in `ReviewWorkspace.js` + fixtures |
| Synthetic backend boundary | Colocated mock adapter and spec | `mock-adapter.js` cannot enforce production authorization |
| Verified source behavior | Named test, workflow SHA and result | Node review-workspace behavioral tests |
| Automated a11y finding | Axe JSON report + browser environment | Phase 8 CI artifacts; default preview states only |
| Human accessibility claim | Named reviewer, assistive technology, scenario, observed result | **NOT VERIFIED**, do not assert |
| Production performance/security | Deployment and field measurements or security signoff | **NOT VERIFIED / NOT APPROVED** |

## Automated regression plan

The curated fixture contains task-positive queries for the six controls, five patterns, review workspace, existing architectural and guidance records; negative queries; and an ambiguous settings case. Positive tests require the *expected first canonical ID*, negative cases require no result, and ambiguity tests require a valid concept among the results rather than asserting one arbitrary top hit.

`tests/test_phase9_discovery.py` also checks each canonical path, relation target and generated HTML page, every source/scenario file, every live preview route/sandbox and bytes of generated copied reference source, all spec-only fallbacks, and exact parity of the derived website search export with the registry.

`scripts/audit_discovery.py` emits `site/artifacts/phase9/discovery-audit.json` with all canonical IDs, reference/scenario paths, preview routes, review status, task-query outcomes and errors. **It is generated evidence, not a second registry.** The existing GitHub workflow runs the audit as a required validation step and uploads its output.

Commands:

```sh
python3 scripts/validate_catalog.py
python3 scripts/audit_discovery.py --output site/artifacts/phase9/discovery-audit.json
python3 -m unittest discover -s tests -v
python3 site/build.py
python3 -m unittest discover -s site/tests -v
```

Browser interaction and automated axe checks run in the existing GitHub Actions Chromium job. They are not an accessibility or security certification.

## Acceptance matrix

| Gate | Evidence | Status |
| --- | --- | --- |
| 54 canonical entries and 12 source-linked references | Derived registry audit and source test | **PASS** in run 42488859952 |
| Existing ID/alias/title ranking unchanged | `find_concept.py` not modified, old lookup tests retained | **PASS** in run 42488859952 |
| Curated task retrieval, explicit misses and ambiguity | Phase 9 cases + Python tests | **PASS** in run 42488859952 |
| Generated website and agent lookup share canonical metadata | Website search export parity test; real browser human approval search | **PASS** in run 42488859952 |
| Implementation source/scenario/route provenance | Source-byte parity, route checks, fallback coverage | **PASS** in run 42488859952 |
| Agent protocol and contributor governance | Updated `AGENTS.md`, `CONTRIBUTING.md`, `catalog/README.md` and root/site navigation | Committed |
| Reviewable CI evidence | Derived JSON and browser reports uploaded | **PRESENT:** discovery artifact `13621036004`; browser artifact `13620596346` |
| Manual UI/UX visual and content review | Named reviewer and findings log | **NOT VERIFIED** |
| Assistive technology, 200–400% zoom, RTL, forced colors | Actual devices/AT and reviewer evidence | **NOT VERIFIED** |
| Third-party security/license/CSP review | Named release/security reviewer and decisions | **NOT VERIFIED** |
| Public hosting and absolute/root URL handling | Deployment choice and base-path/source-ref review | **NOT APPROVED** |
| Real-user Core Web Vitals and actual adoption | Deployed measurement and consumer integration | **NOT VERIFIED** |

## Known gaps and release risks

1. **Semantic ranking limitations.** Task search is lexical, exact ID/alias weighted; the phrase `synthetic review` remains a documented miss. Do not solve this by indiscriminately ranking capability keywords or polluting aliases; evaluate a relevance corpus and owner intent first.
2. **Preview/source link revision handling — addressed for CI.** Static source links are now generated using validated `CATALOG_SOURCE_REF` (CI pins the PR head SHA); ordinary local builds default to `main` unless a reviewed branch/SHA is supplied. Public hosting, route base paths and CSP are still Phase 10 decisions.
3. **Review status not promoted.** All guidance remains proposed and reference status does not mean enterprise support, production-ready API, WCAG-certified accessibility, tested localization or real permission enforcement.
4. **Manual gates pending.** Phase 8 generated screenshots and axe reports, but visual approval, AT walkthroughs and zoom/RTL/forced-color checks have not been completed.
5. **Preview runtime constraints.** Browser examples are trusted classic JavaScript, not a generic TSX/React bundler, installable design-system library or untrusted code sandbox.
6. **Demo-only decision semantics.** Review Workspace has a synthetic adapter and intentional unknown-result lock; real consumer authorization, idempotency, reconciliation and auditing remain app-owned.
7. **Catalog content fidelity.** Minimal Markdown rendering may not cover every advanced Markdown construct. Representative long-form content needs visual owner review.

## Phase 10 handoff — decisions required from maintainers

- Confirm scope and canonical taxonomy; approve or reject the new `feature.review-workspace` concept and its reuse claim. Resolve ownership (records currently say `unassigned`), and whether any entry should remain proposed or be promoted after actual review.
- Inspect the Phase 8 screenshots and all axe reports, triage non-critical findings, and complete manual browser/AT/keyboard/zoom/RTL/forced-color and long-text tests. Record reviewer, date, environment, observation and fix.
- Verify the final PR comparison with `main`, full Python/Node/Chromium CI and task retrieval report; don't merge if a required gate fails.
- Decide static hosting and base path. Current generated route/asset paths assume root hosting; ensure published builds use an appropriate source revision, CSP, trusted preview isolation and license/dependency review.
- Preserve the 53 original IDs and all canonical links. If an isolated implementation fails, remove optional source metadata and revert its preview files while retaining the spec; only remove the new feature entry through a separately reviewed decision.
- Confirm no untracked release promises or product integrations; keep PR in **draft** until required human approvals are recorded.

**No default-branch merge, deployment or owner acceptance is implied by completion of this phase.**

## Phase 9 automated evidence snapshot (2026-11-08)

[CI run 42488859952](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42488859952) completed with **SUCCESS** at `0580c5f18bbc416bae0ab5d3179556a313d7621e`: both the `check-catalog` job and the `Chromium interaction and axe smoke` job passed. The run includes the new curated retrieval corpus, 54-entry source and relation verification, 12-reference source parity, safe source-ref URL test, root/site test suites and human approval queue browser journey.

GitHub retained the generated **`catalog-discovery-audit` artifact ID `13621036004`** (derived task and provenance report) and **`catalog-browser-audit` artifact ID `13620596346`** (automated axe reports and screenshots). The artifacts provide inspectable machine evidence but **not** human approval or independently measured field performance. Later documentation-only changes should receive their own final head check before merge.
