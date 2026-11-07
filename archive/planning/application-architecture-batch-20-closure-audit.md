# Batch 20 — application architecture knowledge audit and closure ledger

**Date:** 2026-11-07 · **PR:** #8 (draft) · **Baseline head at audit start:** `1478e4718298e59eb3edfd914049452391d44919` · **Scope:** proposed documentation, metadata and CI coverage; not a production application audit.

## Audit context collected before edits

Reviewed current branch `catalog/index.json` (47 concepts, including 7 new application-architecture entries), `architecture/README.md`, root/agent/catalog indexes, quality gates, relevant architecture chapters, Batch 13–19 context ledgers, and corresponding retrieval tests. Prior Batch 19 head passed GitHub Actions run #143. Each later change requires its own final-head CI result.

### Gap reconciliation and canonical ownership

| Knowledge question | Canonical owner | Audit disposition |
| --- | --- | --- |
| Prototype vs MVP vs modular vs enterprise selection | `architecture.application-selection` | Covered as proposed guidance; **not** empirically benchmarked |
| Feature/domain/shared UI ownership, navigation | `architecture.module-boundaries` | Covered; application-specific ownership still UNKNOWN |
| Vertical-slice migration and architecture fitness | `architecture.evolution` | Covered; no measured target-app before/after outcomes |
| Monorepo, multirepo, modular monolith, microfrontends | `architecture.enterprise-multiapp` | Covered; topology choice must be evidence-based |
| Framework route semantics and colocation | `architecture.framework-aware` | Next.js, Angular and React Router examples; other frameworks require a fresh context audit |
| Enforceable architectural rules and CI rollout | `architecture.enforcement-ci` | Illustrative lint/graph/Nx recipes only; no actual app enforcement test |
| Prototype/MVP/enterprise task-to-file examples | `architecture.reference-examples` | Illustrative snippets and worksheets; not runnable starter applications |
| UI primitive, component and feature contract | `architecture.component-model` and `architecture.component-contracts` | Already covered; **do not** copy into application-specific chapters |
| Accessibility, user flow, localization and release evidence | Existing patterns, guidance and `governance.quality` | Cross-cutting and already canonical |

**Conclusion:** No eighth application architecture concept justified by this audit. The remaining actionable catalog problem was task-first discoverability, not another standalone rulebook. Keep all seven new entries in `proposed` status. No canonical ID migrations or duplicate page creation.

## Duplication and navigation review

- Existing `architecture/README.md` starts with component tier guidance then appends chronological batch sections; newcomers must scan Batch 9, 12 and 13–19 history to find architecture tasks.
- Root README includes the needed architecture links but places examples/enforcement before the profile selection decision. Reorder the application architecture rows from selection → boundaries → framework → topology → migration → enforcement → examples.
- Per-batch ledgers already preserve historical context; do not repeat all history in navigation. Replace the architecture section README with a task-to-concept table and one compact evidence/history index.
- Prior pages share standard reminders about unknown tests. This is necessary scope signaling, not evidence of duplicate canonical ownership; avoid risky bulk rewriting of reviewed pages.

## Verification matrix

| Check | Expected evidence | Status until final run |
| --- | --- | --- |
| Unique IDs and existing paths | `scripts/validate_catalog.py` | NOT VERIFIED for final head |
| Accurate task-first lookup | `scripts/find_concept.py` + cross-batch unittest assertions | NOT VERIFIED for final head |
| Seven new canonical entries proposed with owner/review metadata | Catalog regression assertions | NOT VERIFIED for final head |
| Ledger and navigation references | Local link validator and regression assertions | NOT VERIFIED for final head |
| Application source build, DX speed, code reduction, dependency graph | Named target app + baseline and tests | NOT VERIFIED |
| Keyboard/AT, localization, responsive, product journey | Application implementation and manual/automated evidence | NOT VERIFIED |

## Residual risks and later work (not automatically new batches)

1. **Framework breadth:** guidance currently illustrates Next.js, Angular and React Router; Vue/Nuxt/SvelteKit/native need a source- and version-specific assessment if a consumer actually uses them.
2. **Executable examples:** Batch 19 snippets are not installable projects; a future separate implementation may supply verified starters if an actual stack and maintainer justify them.
3. **Enforcement tools:** Batch 18 tool fragments and resolver details need testing in an actual application with installed versions and both allowed/forbidden import fixtures.
4. **Measured benefit:** repository duplication, dependency cycles, time-to-locate code, build timing, accessibility and product outcomes require a pinned target repo and measured baselines.
5. **Ownership and lifecycle:** all seven entries remain proposed/unassigned pending human review. Do not promote to stable based solely on documentation CI.

## Closure acceptance

Batch 20 closes **knowledge development** for this initiative after a final-head passing catalog validator, lookup smoke test and unittest suite, with explicit PR evidence. It does **not** attest that these rules are applied in an application or that the PR has been merged. Leave PR #8 in draft for owner review and any required corrections.
