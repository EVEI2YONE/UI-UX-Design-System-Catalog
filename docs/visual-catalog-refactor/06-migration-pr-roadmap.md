# 06 — Migration plan, PR sequence and acceptance matrix

## Strategy — single PR, phase-gated overhaul

**Delivery vehicle:** existing draft PR #16, branch `docs/visual-catalog-refactor-blueprint`, targeting `main`. The phases below are **sequential commit groups on this same branch and PR**, not independent PRs. Keep the PR draft until the complete scope has passed review and quality gates. Do not merge an intermediate phase; each completed phase should have its own commit(s), evidence note, and an updated PR checklist. Some later phases can be deferred only through an explicit scope decision recorded in the PR, not by calling incomplete work finished.

This is a substantial PR. Use phase checkpoints to make review tractable, with stable commits and narrow diffs per phase. Do not force-push to hide reviewed changes. The primary site reference implementations are embedded in `site/`, not published as an npm package.

## Phase plan — all on PR #16

| Phase | Goal and main locations | Dependency | Required completion evidence |
| --- | --- | --- | --- |
| **0. Baseline and inventory** | Lock `main` SHA; inventory registry IDs, links, specs, existing tests and agent lookup results; add gap mapping under `docs/visual-catalog-refactor/` | None | Baseline manifest; paths and links; repeatable lookup queries; risks and decisions |
| **1. Taxonomy and canonical contracts** | Confirm foundations/primitives/components/patterns/features boundaries; extend `architecture/` guidance and `features/` specs only after catalog-first search | 0 | No duplicated canonical concepts; owner/decision log; feature acceptance contract |
| **2. Metadata and discovery compatibility** | Add optional preview/source/capability fields to `catalog/schema.json` and `catalog/index.json`; update Python validator/search tests and `AGENTS.md` | 1 | Existing aliases/IDs unchanged; schema strict; lookup regressions pass |
| **3. Site foundation and static browser** | Create `site/` runtime/build; responsive shell, IA, route resolution, search/filter, static Markdown entry pages and spec-only fallback | 2 | Build/typecheck; keyboard search/navigation; canonical paths resolve with no JS-heavy preview dependency |
| **4. Design foundation and live preview engine** | Establish semantic tokens/themes, preview isolation, deterministic fixtures, scenario/reset controls, actual source viewer and source-to-render mapping | 3 | Preview imports actual implementation; no duplicated sample code; theme/reflow/source parity tests |
| **5. Core working controls** | Implement Button, Input/Field, Select, Checkbox, Dialog under `site/src/implementations/components/`, linked to existing specs | 4 | Interaction states, keyboard/focus, async and error handling; screenshots and test logs |
| **6. Composed patterns** | Implement validated form, navigation, search/filter/data table and recovery demos where justified by canonical patterns | 5 | Loading/empty/partial/error/retry; long text, mobile, accessible table and clear semantics |
| **7. Feature-complete reference vertical slice** | Add `features/review-workspace/` spec + genuine executable `site/src/implementations/features/review-workspace/` with mock adapter; optionally second data-workspace slice if approved | 6 | End-to-end synthetic review flow, permissions simulation, unknown outcome, conflict and focus recovery; no production writes |
| **8. Quality, accessibility, performance and readability** | Harden all implemented site and reference surfaces; add browser/a11y/visual/performance CI plus human QA evidence | 3–7 | Measured budgets and environments; browser/AT matrix; source readability review; no P0 blockers |
| **9. Agent retrieval, governance and handoff** | Verify task-based search, stable IDs, relations and source trace; update README/CONTRIBUTING/AGENTS and adoption examples | 2–8 | Human + agent retrieval scenarios pass; docs accurate; migration and rollback reviewed |
| **10. Release readiness and PR closeout** | Final diff/code review, dependency/license/security scan, deployment decision (deployment itself optional), branch reconciliation and approval | 0–9 | Complete evidence table, named approvals, no unverified PASS; PR ready-for-review only after gates |

**Recommended first usable milestone:** through phase 5, with a functioning static catalog and working core controls. **Recommended full refactor milestone:** through phase 9, including one fully simulated feature reference and quality evidence. Phase 10 is review/approval, not automatic deployment.

### Phase exit and change-control protocol

For **every** phase: (a) record the commit SHA and changed paths in the PR body or a phase ledger; (b) run the applicable existing Python catalog checks and new site tests when available; (c) capture results as PASS/FAIL/NOT VERIFIED with environment and date; (d) inspect backwards compatibility and preview behavior; (e) log open gaps. A phase marked complete cannot rely on unexecuted tests. Missing manual accessibility or performance evidence remains NOT VERIFIED.

**Phase dependencies are hard gates:** don't index an unbuilt preview; don't present a feature as interactive before the source/viewer is tested; don't claim quality before exercising real browser behavior. Revise scope if a phase exposes a different need, rather than inventing new components to fill an arbitrary quota.

### What stays out of scope

Published packages, replacing the existing knowledge model, live product API integrations, production authentication, user data, dynamic CMS, arbitrary code execution, and automatic deployment/merge. A site feature should remain reproducible using synthetic fixtures and inspectable source.

## Ownership and approvals

| Area | Suggested accountable reviewer |
| --- | --- |
| Catalog IDs and schema | Catalog maintainer / agent search owner |
| Site shell and frontend architecture | Frontend engineer |
| Component contract and behavior | Design systems engineer |
| Feature contracts / adapter boundary | Product UX + frontend engineer |
| Accessibility / content | Accessibility reviewer + UX writer |
| Performance and runtime security | Performance engineer + application security |
| Release approval | Repository maintainer and hosting owner |

Assign actual people in the PR; no owner is inferred from GitHub permissions.

## Build-order versus user-impact priority

**P0** blocking privacy, security, severe accessibility, data loss or critical regression issues outrank all phases. **P1** serves human and agent ability to locate the right concept and inspect it. Minimal P3 foundations (registry schema and stable preview runner) must be engineered early because they unlock P1 outcomes. P2 covers browsing IA and search relevance; P4 onboarding/how-to-consume guidance; P5 quick wins; P6 secondary feature references; P7 decorative polish.

## Acceptance matrix

| Quality gate | Required proof | Status at plan creation |
| --- | --- | --- |
| Reference catalog separation | Same repo, canonical guidance outside `site/` | CONFIRMED in architecture |
| Existing registry baseline | IDs, fields, strict schema and lookup documented | OBSERVED |
| Catalog schema migration | Optional fields added without breaking lookup | NOT IMPLEMENTED |
| Website documentation | Static routes and spec-only fallback | NOT IMPLEMENTED |
| Source-to-preview integrity | Preview imports live implementation, no duplicate mock | NOT IMPLEMENTED |
| Core component behavior | Keyboards, focus, state/error tests | NOT VERIFIED |
| Feature synthetic-data safety | No external writes or real credentials | NOT IMPLEMENTED |
| Browser responsive/a11y | 320/375/768/1024/1440, zoom, AT, themes | NOT VERIFIED |
| Performance/readability | Benchmarks and representative usability tests | NOT VERIFIED |
| Agent retrieval | ID/aliases/related preserved; scenario lookups added | NOT IMPLEMENTED |
| Deployment / rollback | Approved host, CSP, release & revert plan | NOT APPROVED |

## Exact commands to retain

```sh
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/find_concept.py "loading button" --json
```

Additional commands for typecheck/build/Playwright/lint are **TBD** until a site framework is chosen, configured and committed. Do not report these as executed merely because they appear here.

## Risk register and mitigation

| Risk | Severity | Mitigation |
| --- | --- | --- |
| Duplicated catalog metadata in site | High | Generate UI from `catalog/index.json`; no second manually edited index |
| JSON schema breakage | High | Optional typed fields; version and old-query regressions |
| Visual preview inconsistent with source | High | Import and test the same source, use automated source path checks |
| Demo described as production-ready | High | Visible reference/synthetic state and separate evidence statuses |
| Malicious browser-side code execution | High | No arbitrary code input; fixed trusted imports, CSP/sandbox |
| Feature demo leaks secrets or performs writes | High | Local fixtures, deterministic mock adapters, no real endpoints |
| Heavy site bundle / poor search access | Medium | Static docs and lazy previews; test no-JS browsing |
| Low-contrast or inaccessible preview controls | High | Semantic tokens, keyboard/manual gates |
| Library complexity creep | Medium | Defer packages; component-first, one feature pilot |
| Uncontrolled URL moves | Medium | Preserve IDs/docs paths, redirects and link checks |

## Rollback playbook

1. Keep all existing Markdown and registry entries intact until corresponding site routes are verified.
2. If schema migration breaks agents, revert only schema/registry optional-field changes and regenerated site assets; old lookup remains supported.
3. If a preview fails, disable its optional mapping so a spec-only page remains available.
4. If a site release fails, roll back the site deployment without altering canonical knowledge.
5. Never rewrite review dates, evidence or lifecycle statuses to make a failed gate look passed.

## Decision record

- **Chosen direction (proposed):** one knowledge catalog + embedded visual site + executable reference examples.
- **Explicitly deferred:** npm packages, separate component registry, hosted code editor, dynamic CMS, general-purpose MCP server.
- **First implementation pilot:** `component.button` after site shell/preview foundations; later generic review workspace after controls/patterns are exercised.
- **Delivery unit:** One draft PR #16 containing sequential phase commits, with a recorded gate before readiness for merge.
- **Open decisions:** site host and framework (Next.js suggested, not mandated), preview sandboxing mode, source-viewer licensing, public deployment policy, actual owners and test thresholds.

## Repository discipline

For **this initiative**, keep work on the existing PR #16 feature branch and land successive, reviewable phase commits on that branch; do not open a new PR for each phase. Reconcile with `main` before final review and rerun impacted tests. Do not merge or deploy without explicit owner approval. This document alone does not authorize implementation claims.
