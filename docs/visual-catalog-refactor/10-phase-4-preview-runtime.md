# 10 — Phase 4: interactive preview runtime and source parity

**Branch / PR:** `docs/visual-catalog-refactor-blueprint` / draft PR #16  
**Phase:** 4 — live preview foundation  
**Scope:** trusted, repository-owned reference implementations and sandboxed previews; no installable packages or product backend  
**State:** implementation committed, automated gate subject to current head CI, human browser/AT review pending

## Context gathered before implementation

Phase 3 uses `site/build.py` as a dependency-free static compiler for 53 registered canonical concepts and already provides static documentation, navigation, search and specification-only fallbacks. Phase 2 introduced an optional `implementation` object with `source_path`, `scenario_manifest`, `preview_path` and lifecycle status, with strict source-path validation. The existing [Button contract](../../components/button/spec.md) defines native button semantics, pending and disabled behavior, focus, variants, token roles, responsive and localization requirements. There was no actual preview source registered before this phase.

## Key architecture decisions

| ID | Decision | Rationale and boundary |
| --- | --- | --- |
| P4-D01 | Retain the static documentation site | Adding React/Next.js for one preview would impose additional build and package overhead unrelated to source retrieval |
| P4-D02 | Implement the initial reference in reviewed classic JavaScript | The same executable file can be displayed verbatim and run directly with no transpilation; React/TSX bundling deferred until warranted |
| P4-D03 | Generate a preview page only for entries with registered implementation metadata | Prevents fictional previews and duplication of catalog identity |
| P4-D04 | Put each live example in an iframe with `sandbox="allow-scripts"` and no `allow-same-origin` | Isolates child DOM/state from the documentation host; not a permission to execute untrusted code |
| P4-D05 | Derive source viewer output from the exact checked-in file copied for execution | Eliminates manually copied source snippets or a second implementation |
| P4-D06 | Use colocated deterministic scenarios and shared runner | Supports repeatable behavior, theme switching and reset without a backend |
| P4-D07 | Keep all other catalog entries in spec-only mode | No preview registration until real file and scenario manifest exist |
| P4-D08 | Keep catalog review status `proposed`, implementation status `reference` | Executable example is not proof of production readiness, WCAG conformance or real-user validation |

## Artifacts

| Path | Role |
| --- | --- |
| `site/src/implementations/components/button/Button.js` | Actual native Button implementation, no product calls |
| `site/src/implementations/components/button/Button.css` | Semantic theme-aware scoped button styling |
| `site/src/implementations/components/button/scenarios.js` | Six frozen, synthetic scenarios: default, secondary, danger, pending, disabled, long label |
| `site/src/previews/preview-runner.js` | Reusable scenario/theme/reset controls and local activation feedback |
| `site/src/previews/preview-host.css` | Standalone preview controls and responsive stage styling |
| `site/build.py` | Copies registered source/scenarios/styles, generates sandboxed preview route and verbatim source view |
| `site/static/styles.css` | Interactive reference panel and source inspector presentation |
| `catalog/index.json` | Registers `component.button` implementation and canonical preview route |
| `site/tests/test_build.py` | Source-to-output parity, iframe isolation and spec-only fallback tests |
| `site/tests/button-runtime.test.cjs` | Executes real Button source in deterministic DOM fixture |
| `tests/test_visual_catalog_metadata.py` | Validates registered Button while preserving five other controls as spec-only |
| `.github/workflows/catalog-validation.yml` | Runs existing catalog, static site and new Node reference tests |

## Functional behavior and limitations

The Button reference uses a real native HTML `button` with type `button`, named action variants, pending/disabled guards and a status element for the pending example. The preview runner offers a scenario selector, light/dark/high-contrast modes and a reset. Activation changes only an in-frame synthetic status message—**it never calls a production API or implies a successful server write**.

The source viewer's content comes directly from `Button.js` and is HTML-escaped for the documentation page. The generated frame loads the copied `Button.js` plus the colocated scenario file and CSS. No arbitrary user-typed code is evaluated or imported by this implementation.

This is a **trusted code reference** sandbox, not a general multi-tenant code execution service. A future React/TypeScript example will need an explicit bundling and isolation contract; do not rename this classic-script runtime to suggest generic TSX support.

## Acceptance matrix

| Check | Evidence | Status |
| --- | --- | --- |
| Existing canonical IDs and lookup unchanged | Catalog `index.json` adds only Button implementation metadata; existing IDs/paths retained | Structural, subject to CI |
| Real registered source file and scenarios exist | Source + colocated `scenarios.js`, CSS committed | PRESENT |
| Preview and source viewer use identical file | Build copies source; site parity test compares bytes and references | Automated test |
| Safe preview isolation | `sandbox="allow-scripts"` without `allow-same-origin`, deterministic fixture | Code + static test |
| Scenario/theme/reset UI | `preview-runner.js` and host controls | Implemented, real browser QA NOT VERIFIED |
| Native Button activation and pending/disabled behavior | Node executes the same source in a deterministic DOM fixture | Automated test |
| Remaining 52 entries remain spec-only | Build tests sample Input; no other implementation registered | Static test |
| Registry validator and old tests | Existing GitHub catalog workflow | Await current head CI evidence |
| Manual screen reader, focus and contrast | Actual browser/assistive review | NOT VERIFIED |
| Mobile/zoom/RTL and forced-colors | Actual browser review | NOT VERIFIED |
| Web performance, CLS/INP/LCP | Deployment/lab measurement | NOT VERIFIED |
| Deployment / third-party licensing/security review | Hosting and release owner | NOT APPROVED |

## Gates and handoff

Run `python3 scripts/validate_catalog.py`, `python3 -m unittest discover -s tests -v`, `python3 site/build.py`, `python3 -m unittest discover -s site/tests -v`, `node --test site/tests/button-runtime.test.cjs`, and the JavaScript syntax checks specified in GitHub Actions. Record the actual resulting commit and workflow conclusion; do not infer test outcomes from file creation.

Before starting broad Phase 5 work, test the running preview in at least one desktop and mobile browser, inspect keyboard focus, zoom, contrast and screen-reader announcements, and confirm the no-write scenario behavior. Record deviations for Phase 8, retaining `reference` status until required evidence is accepted.

**Roll back** by removing the optional Button implementation metadata and generated reference source registration; the static Button spec and agent lookup must remain intact. The root registry still owns discovery.
