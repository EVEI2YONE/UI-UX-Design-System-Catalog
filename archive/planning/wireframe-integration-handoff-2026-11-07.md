# Wireframe knowledge expansion — integration handoff (B0–B7)

**Date:** 2026-11-07 · **Review state:** proposal / documentation delivery only · **Owner:** unassigned · **PR:** [#11](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/11), draft and unmerged when this handoff was prepared.

This file is **handoff documentation, not a second source of canonical UX rules**. Retrieve the current IDs and paths from [the catalog index](../../catalog/index.json) and consult [AGENTS](../../AGENTS.md). Do not import plugin invocation instructions into the catalog.

## Gap disposition and canonical ownership

| Batch / gap | Disposition | Canonical ID and source path | Provenance boundary |
| --- | --- | --- | --- |
| B0 catalog overlap and baseline | REUSE registry and governance | `catalog/index.json`, `AGENTS.md`, `CONTRIBUTING.md` | GitHub repository observed; baseline main `6ed00199047488d8d5f42886112a35639fffe3ef` |
| B1 fidelity and prototype escalation | CREATE one new proposed concept | `guidance.wireframe-methodology` — [guidance/wireframe-methodology.md](../../guidance/wireframe-methodology.md) | Catalog synthesis with cited practitioner and W3C context, not validated users |
| B2 minimum brief, screens and alternatives | EXTEND existing owners | `pattern.task-flows` — [patterns/task-flows-and-information-architecture.md](../../patterns/task-flows-and-information-architecture.md); `principle.visual-hierarchy` — [foundations/design-principles.md](../../foundations/design-principles.md) | Proposed compositional rubric and synthetic comparison, not proven usability |
| B3 states, unknown outcome and recovery | EXTEND existing owner | `pattern.interaction-recovery` — [patterns/interaction-states-and-recovery.md](../../patterns/interaction-states-and-recovery.md) | State and annotation synthesis; specialized forms/feedback/offline owners reused |
| B4 responsive, zoom, expansion and RTL | EXTEND existing owners | `guidance.mobile-adaptive` — [guidance/mobile-and-adaptive-platform-ux.md](../../guidance/mobile-and-adaptive-platform-ux.md); `guidance.accessibility` — [guidance/accessibility.md](../../guidance/accessibility.md); `guidance.internationalization` — [guidance/internationalization.md](../../guidance/internationalization.md) | Representative screen stress cases, not responsive/AT/localization implementation tests |
| B5 visual image inspection and evidence | EXTEND existing owner | `governance.quality` — [governance/quality-gates.md](../../governance/quality-gates.md) | Proposed inspection rubric; no actual generated images inspected |
| B6 examples, anti-examples, retrieval | REUSE canonical owners, CREATE noncanonical fixture | [synthetic example bank](wireframe-synthetic-example-bank-2026-11-07.md), `tests/test_wireframe_examples_retrieval.py` | Original synthetic text; no real app screenshots, users or external assets |
| B7 integration, validation and handoff | EXTEND agent/catalog/root navigation; CREATE noncanonical handoff and regression | This file, `tests/test_wireframe_integration_handoff.py`, applicable READMEs and PR | CI catalog integrity tests only; remaining product checks unverified |
| B8 downstream Product Design execution | DEFER | Outside this tool-neutral canonical PR | Consumer-specific behavior and tool setup require separate integration testing |

**No canonical entries were superseded or deprecated.** The new B1 concept and all previously existing owners remain `status: proposed`, `owner: unassigned`, `reviewed_at: null` unless a future human review changes their metadata. The repository total at B7 context review is **50 unique entries**, one new since the 49-entry baseline. Historical batch counts are snapshots, not live metrics.

## Downstream design-agent integration contract

For an image-based wireframe request, consumers should:

1. **Retrieve the task owner**, not every page. Read `catalog/index.json`; use `python3 scripts/find_concept.py "wireframe methodology" --json`, `"task to screen composition"`, `"wireframe state coverage"`, `"responsive wireframe composition"`, `"wireframe text expansion"` or `"wireframe visual QA"` as appropriate. Resolve the returned canonical `path`, not a copy of this handoff.
2. **Establish context and evidence** using B1/B2. Record user, immediate task, entry and scope, success, constraints, supported platform, approved content, `KNOWN` versus `ASSUMED`, and `ILLUSTRATIVE` fake data. Do not guess financial/security/permission details as working product requirements.
3. **Compose and compare** with `pattern.task-flows` and `principle.visual-hierarchy`. Provide two genuinely different structural alternatives when a design decision warrants it, or explain why only one safe alternative is appropriate. Do not conflate cosmetic variants with structural choices.
4. **Annotate states and adaptations** with `pattern.interaction-recovery`, `guidance.mobile-adaptive`, `guidance.accessibility`, `guidance.internationalization`. State what is `SHOWN`, `ANNOTATED`, `NOT SHOWN`, `NOT APPLICABLE` (with rationale) and implementation **NOT VERIFIED**.
5. **Review the actual image** against the task brief and source copy using `governance.quality`: legibility, clipping, hierarchy, distorted labels/values, state and cross-screen consistency, invented capabilities, and issue evidence. If no image was produced/inspected, **image QA NOT VERIFIED**.
6. **Escalate based on the question**, not apparent visual polish. Use an interactive prototype for transitions, task walkthroughs, focus or data preservation; use real application tests for permission, persistence, accessibility, responsive rendering, backend status and user outcomes.
7. **Record handoff evidence**: canonical ID + path, option decision/rationale, source/assumptions, screen IDs, artifact IDs/revision, unshown states/viewports/locales, findings, reviewer/date, source of truth for copy and separate `PASS`/`FAIL`/`NOT VERIFIED` check statuses. Avoid pretending a catalog CI PASS verified the UI.

**Worked lookup:** `python3 scripts/find_concept.py "wireframe visual QA" --json` → `governance.quality` → `governance/quality-gates.md`; for fidelity use `guidance.wireframe-methodology`; for screen composition `pattern.task-flows`. The [WRF-01–06 synthetic examples](wireframe-synthetic-example-bank-2026-11-07.md) supply positive/anti-examples for retrieval rehearsal. This is a **consumer contract proposal**, not a tested invocation inside any specific Product Design plugin.

## Acceptance, CI and evidence status

| Check | B7 expectation | Current evidence |
| --- | --- | --- |
| New/duplicate canonical IDs | 50 total, 50 unique; exactly one new `guidance.wireframe-methodology` | Repository metadata inspected at B7 context review; verify again in CI |
| Stable paths and links | Canonical pages, navigation, example links and handoff links resolve | Repository validator in GitHub Actions after B7 commits |
| Registry and lookup tests | Deterministic positive, exact-alias and negative-only matching; integrated B1–B6 cases | Unittest discovery in GitHub Actions after B7 commits |
| Documentation lifecycle | All relevant entries proposed/unassigned/unreviewed | Integration test and registry inspection |
| Visual wireframe artifact | Review an actual generated and identified image | **NOT VERIFIED**; no image artifact in B1–B7 |
| Real users/task completion | Observed task walkthroughs and comparison results | **NOT VERIFIED** |
| Interaction/backend/permissions | Executable navigation, saved data, real confirmation/retry/security | **NOT VERIFIED** |
| Web/native accessibility | Keyboard, AT, contrast, reflow, zoom, touch | **NOT VERIFIED** |
| Locale correctness | Approved translations and RTL/mixed-direction device rendering | **NOT VERIFIED** |
| External link freshness and third-party rights | Revalidate cited sources, confirm scope/license before reuse | **NOT VERIFIED**; no third-party image assets introduced |
| Human publication approval | Named reviewer/owner, review date and PR decision | **NOT VERIFIED**; leave draft/unmerged |

## Review questions / next consumer work

- Assign canonical concept owner and reviewer; verify that research/service references remain accessible and accurately scoped.
- Trial a **real image-based wireframe** task against WRF-01–06; inspect raster output for text/data hallucinations, semantic gaps, missing states and cross-viewport issues. Record exact artifact ID and reviewer outcome.
- Exercise a task-complete interactive prototype where focus, transitions, retry, navigation/permission or persistence are in question.
- For each actual supported locale/platform, test the implementation before claiming accessibility, responsive behavior or localization quality.
- Confirm consumer integration in its own environment; do not claim ChatGPT Product Design automatically consumed this catalog because a GitHub PR exists.

## Branch and PR policy

All B0–B7 documentation work accumulates on `docs/wireframe-knowledge-batches-2026-11-07`, targeting `main` through [draft PR #11](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/11). Batch commits are already on the same PR. **Do not merge, mark review passed or promote status automatically.** See the [batch tracker](wireframe-knowledge-batches-2026-11-07.md) and [changelog](../../CHANGELOG.md) for recorded progress and source boundaries.

## B7 GitHub Actions execution record (2026-11-07)

- **Initial test-first CI failure:** workflow `42370481609` at commit `7ad1e27d23a4183694f85455f83cabacd81287b4` ran before navigation was updated; 1 of 83 tests failed because `AGENTS.md` did not yet link this handoff. This was a sequencing defect, **corrected** by subsequent commits.
- **Integrated CI PASS:** workflow `42370511127` on commit `eaa1b5380251b77b6ecebd5d11fbd36659f96b1f`, job `128397497783`: 83 Python tests **PASSED**; catalog validator reported **50 unique concepts, 8 section READMEs, 665 relative links checked**. This included the four new cumulative B7 integration tests. Source links outside repository, manual UX, actual wireframes and runtime behavior remained **NOT VERIFIED**.
- Changes to this dated evidence ledger after that CI commit are **documentation-only** and were not included in the referenced run. Do not infer a later independent CI run without checking the commit run history.
