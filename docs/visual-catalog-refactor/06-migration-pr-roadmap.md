# 06 — Migration plan, PR sequence and acceptance matrix

## Strategy

Build a single, small visual vertical slice under the existing catalog. Keep knowledge and registry compatibility intact. Document first, create a minimal executable site second, and only then broaden components and feature references. Do not publish packages, deploy to production or merge without separate review.

## Suggested PRs

| PR | Scope | Dependency | Exit criteria |
| --- | --- | --- | --- |
| 0 — Architecture plan | This documentation pack | Current `main` | Reviewer approves boundaries, taxonomy, schema migration and first vertical slice |
| 1 — Registry contract | Optional preview/source/capability fields, schema migration, examples, agent instructions and lookup tests | PR0 | Existing ID/alias lookup unchanged; validator + unit tests pass |
| 2 — Site skeleton | `site/` routing, catalog search, static docs, layout, spec-only fallback | PR1 | Build passes; existing entries show correct specs and routes without previews |
| 3 — First working component | Token foundation + Button implementation and live scenario viewer | PR2 | Real source rendered; keyboard and source parity tests; visual evidence recorded |
| 4 — Core components | Input/Field, Select, Checkbox, Dialog and state examples | PR3 | No duplicate primitives; contrast/focus/reflow tests on each |
| 5 — First composed pattern | Async form + uncertain-result recovery, or navigation pattern | PR4 | Interaction/cancellation/recovery checks pass |
| 6 — Feature pilot | Generic review workspace spec, adapter and interactive source demo | PR5 | No product APIs; decision context, uncertainty, focus and responsive behavior tested |
| 7 — QA/retrieval hardening | Cross-browser/a11y/perf benchmarks, agent search scenarios, docs handoff | PR2–6 | Evidence-linked quality matrix; documented deferred issues |
| 8 — Optional deployment | Hosting and public documentation exposure after owner approval | PR7 | Security, performance, release and rollback approvals |

The numbers are **proposed PR units**, not PRs already opened.

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
- **First implementation pilot:** `component.button` then a generic review workspace after infrastructure and controls have been exercised.
- **Open decisions:** site host and framework (Next.js suggested, not mandated), preview sandboxing mode, source-viewer licensing, public deployment policy, actual owners and test thresholds.

## Repository discipline

All implementation PRs must branch from current `main`, use narrowly scoped changes, record real test results, and seek review. This documentation pack is not authorization to merge or deploy.
