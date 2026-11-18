# B06 context gate — consistency, interaction-test evidence and catalog retrieval

**Collected before B06 edits:** 2026-11-07. **Base:** `main` SHA `00df3f2055396e586fbb5ffa07e4a80dc8312e8e`. **Working branch:** `knowledge/icon-interaction-system-b01-b06`; GitHub compare before B06: 54 commits ahead, 0 behind, 29 changed files. **Single PR** to be opened after B06 quality documentation and tests are committed.

## Inspected source and existing owners

- `AGENTS.md`, `CONTRIBUTING.md`, `catalog/index.json` (53 entries in branch vs 52 in main; exactly one B01 addition), `scripts/validate_catalog.py`, `scripts/find_concept.py`, `governance/quality-gates.md`, `foundations/iconography-and-semantics.md`, `architecture/component-contracts.md`, `components/button/spec.md`, and B01–B05 regression tests and progress ledger.
- Canonical `governance.quality` already owns documentation validation, actual evidence status, interaction/accessibility/locale acceptance, and lookup integrity. Extend it for CKG-18/19 instead of introducing a second QA concept.
- Canonical `foundation.icon-semantics` already owns semantic roles, glyph context, labels, host states, RTL and target size. Extend it for CKG-05 icon consistency review; no universal brand glyph catalogue or Lucide dependency.
- B01–B05 contracts cover CKG-01–04 and CKG-06–17; B06 should **not rewrite** their guidance. Existing tests assert retrieval and text semantics only, not browser conformance.
- GitHub repo CI `.github/workflows/catalog-validation.yml` runs `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` on pull requests or `main` pushes. It does not run on pushes to this working branch. Local Git clone was attempted again for B06 and failed due to unavailable DNS resolution for `github.com`.

## B06 gap disposition

| Gap | Existing owner | Missing reusable addition | Action |
| --- | --- | --- | --- |
| CKG-05 icon consistency | `foundation.icon-semantics` | Registry review rubric: duplicated intent/glyph, ambiguous icon-only meaning, RTL and visual/status consistency, migration and manual evidence | Extend icon semantics |
| CKG-18 interaction-state tests | `governance.quality` | Task-representative assertion and manual test recipes for icon-only Button, nested menus, pending/uncertain outcome, row-removal focus, sequential flow, responsive/locale states | Extend quality gates |
| CKG-19 task retrieval | `governance.quality`, `catalog/index.json`, `scripts/find_concept.py` | Positive/negative queries and cross-batch lookup regression; registry aliases, section/agent navigation and ownership checks | Extend quality gates and tests |

## Evidence classification and acceptance

- The GitHub connector can confirm paths, content and commit/ref comparisons. This alone **cannot** execute Python, confirm no broken local links repo-wide, or prove WCAG/UX outcomes.
- The authoritative catalog validator and tests require an executable working tree or CI after PR. Do not label them PASS without actual output. After PR, inspect check results when available and document failures and remaining unknowns.
- Positive and negative tests must not overfit aliases: one task query should resolve to its owner; closely related component/quality concepts should remain separate. New tests should avoid requiring an arbitrary registry count beyond actual uniqueness and expected ID existence.
- Manual UI tests require actual implementing app, supported browser/device/AT environment and reviewer. Mark **NOT VERIFIED**; no user study, rendered UI or production implementation is available in the docs-only catalog.
- Acceptance: record CKG-05/18/19 contract decisions, update registry/navigation/tests, run available source-level checks where possible, summarize batch coverage/unknowns in progress ledger, then open one PR against `main` with explicit CI and review gates.
