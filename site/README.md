# Embedded visual catalog website (Phases 3–9)

This directory contains the working **static knowledge browser with isolated live reference previews** for the UI/UX Design System Catalog. It is built from the repository's canonical Markdown and catalog/index.json, not a second manually maintained knowledge database.

## Build and serve locally

Requires **Python 3.10+** to build, using only its standard library; **Node.js 18+** is needed only to run the reference behavior tests. No npm install, UI package publishing, application backend or deployment account is required.

    python3 site/build.py
    python3 -m unittest discover -s site/tests -v
    node --test site/tests/button-runtime.test.cjs
    node --test site/tests/core-controls-runtime.test.cjs
    node --test site/tests/patterns-runtime.test.cjs
    node --test site/tests/review-workspace-runtime.test.cjs
    python3 -m http.server 8000 --directory site/dist

Open http://localhost:8000/ in a browser. Do not open generated pages via file:// because absolute asset URLs assume a server root.

The build emits site/dist/ (generated; do not commit it). Serve at the **site root** for Phase 3. Hosting from a repository-named GitHub Pages subpath requires a configured base-path strategy in a later deployment review; do not imply root-relative links will work under an arbitrary subpath.

## What Phase 3 implements

- Static home, browse, search, and individual concept pages for every registered entry.
- Deterministic routes from canonical ID and its owning Markdown folder, rather than mutable display names or registry layer.
- Responsive layout and semantic navigation, visible keyboard focus, skip link, source provenance and related concept links.
- A zero-dependency Markdown renderer supporting headings, paragraphs, ordinary links, bold/emphasis, inline and fenced code, lists, quotes and tables. Repository-authored content is HTML-escaped; it deliberately does not execute embedded HTML or JavaScript.
- Progressive client-side text and category filtering of **pre-rendered cards**. With JavaScript disabled, the cards and source text remain navigable via links or browser Find.
- An explicit **Specification only** state for concepts with no implementation metadata. This build does not render Phase 4+ interactive source code; it refuses to imply one exists.
- A derived catalog-search.json file as a static convenience output, not a new canonical registry.

## Ownership and source boundaries

- Canonical identity, aliases, relationships, and review status: ../catalog/index.json
- Canonical norms and contracts: existing ../components/, ../patterns/, ../guidance/, etc.
- Static catalog shell: site/build.py, site/static/
- Executable reference sources: site/src/implementations/ (12 reviewed-source examples, not released packages)
- Shared iframe preview isolation/scenarios: site/src/previews/ and colocated implementation scenario manifests
- Build output: site/dist/ (ignored, generated)
- Build/regression tests: site/tests/

Phase 4 **now registers one actual executable reference** for `component.button`: the build copies its checked-in classic JavaScript and colocated styles/scenarios into generated preview assets, renders the exact implementation in a sandboxed iframe, and shows that same source text on the catalog entry page. Entries without a reference remain `Specification only`. This is a **reference**, not a published production library or accessibility certification.

## Performance and readability approach

All canonical documentation and cards are available in HTML before JS. Site search works by filtering pre-rendered cards and does not fetch records as the user types. Only one small JavaScript file is used for progressive filtering. CSS uses system fonts to avoid third-party font requests, plus responsive layouts, dark-mode preferences, reduced-motion handling, readable line lengths and horizontally scrollable tables. Actual browser responsiveness, screen reader behavior, field Core Web Vitals and long-content reflow still require runtime inspection.

## Security and limitations

- This is a **trusted repository-content renderer**, not a general Markdown sanitizer for untrusted user submissions. Do not pipe arbitrary user-provided Markdown through it.
- Unsupported Markdown (some nested lists, raw HTML, sophisticated tables and footnotes) may display conservatively as text rather than achieving full CommonMark parity. Phase 3 should check representative lengthy catalog pages and decide whether a full parser is justified.
- URLs with unsupported schemes are not emitted as clickable links.
- There is no remote search API, dynamic CMS, user login, real writes, arbitrary code execution or editable preview environment.
- Deployment, licensing, live browser verification and content security policy decisions belong to later gates.

## Phase 4 — preview runtime contract

The catalog's canonical `implementation` metadata is authoritative for preview identity and source paths; the site compiles the allowed, checked-in assets instead of executing user-supplied source or maintaining a second concept database.

- **Reference implementation:** `site/src/implementations/components/button/Button.js`; native semantic button behavior and accessible status messaging. The checked-in CSS file `Button.css` provides semantic preview theme variables.
- **Scenario manifest:** `site/src/implementations/components/button/scenarios.js`; deterministic, synthetic configurations for default, secondary, danger, loading, disabled and long-label states.
- **Shared preview host:** `site/src/previews/preview-runner.js` and `preview-host.css`; controls for scenario, light/dark/high-contrast theme and reset.
- **Isolation:** a static iframe with `sandbox="allow-scripts"` and **no** `allow-same-origin`, form, navigation or top-level permissions. The child does not access parent catalog state; the browser UI never evaluates arbitrary code input.
- **Source parity:** `site/build.py` copies the registered source file to the generated preview, and escapes/presents that same original file under “Inspect implementation source.” Build/tests verify matching contents and references.
- **Fallback:** all other concept entries remain static documentation until they have valid implementation metadata and real source/scenarios. The preview runner currently supports colocated **classic JavaScript** files; TSX/React bundling remains a later explicit design decision.

`node --test site/tests/button-runtime.test.cjs` tests button activation, pending/disabled behavior and the fixture contract using the *same real source*, without implying browser focus, layout or screen-reader verification. The Python site suite checks registration, sandboxing, generated source parity, routes and spec-only fallback. The iframe is a reference sandbox, not a robust security boundary for arbitrary untrusted code: only repository-reviewed, trusted examples are permitted.

See [Phase 4 evidence ledger](../docs/visual-catalog-refactor/10-phase-4-preview-runtime.md).

## Phase 5 — core controls now demonstrated

The live catalog registers all six current canonical component specifications as **reference** implementations (Button, Input, Select, Checkbox, Dialog and Field). The five newly added references use native platform controls and provide synthetic state cases for default/filled, invalid/help, readonly/disabled, loading or long content as applicable. Dialog uses the native `showModal()` API; the preview runner supports `onChange` and `onClose` for local feedback.

Each new control lives in `site/src/implementations/components/<name>/` as a source `.js` file, colocated `scenarios.js` and matching CSS. `site/build.py` derives the iframe and code viewer directly from the registered files; unregistered concepts remain **Specification only**. The references deliberately have no product-specific APIs or persistence and do not constitute an npm component package.

Node source-level tests in `site/tests/core-controls-runtime.test.cjs` check label/error links, select option states, checkbox mixed state, dialog callback/focus-return intent, and no duplicate business side effects. These tests cannot substitute for real browser/keyboard/screen-reader testing. See [Phase 5 evidence ledger](../docs/visual-catalog-refactor/11-phase-5-core-controls.md).

## Phase 6 — working composed pattern references

Five existing canonical pattern concepts now have real source-linked, interactive examples: [forms](../patterns/forms.md), [navigation](../patterns/navigation.md), [search/filter](../patterns/search-and-filter.md), [data tables](../patterns/data-tables.md), and [interaction recovery](../patterns/interaction-states-and-recovery.md). Their sources live under `site/src/implementations/patterns/` with colocated `scenarios.js` and CSS. The source viewer reads exactly the checked-in file executed inside the existing sandboxed iframe. The pattern viewport is taller than the core component preview to accommodate errors, tables and multiple actions.

Form validation and simulated service outcomes preserve values and distinguish a known error from an unknown result; navigation includes active location semantics and disclosure; search/filter exposes honest empty/error states; tables are semantic, paginated and use only local selection; recovery refuses a duplicate submission while the outcome is unknown. All are **synthetic examples**, not product integrations or persisted features. Current pattern references are standalone classic JavaScript using native controls; literal reuse of the individual component runtime scripts remains an explicit architecture follow-up rather than a claim of package-level composition.

`node --test site/tests/patterns-runtime.test.cjs` checks scenario registration and the actual source's form validation, filtering, paging and recovery transition logic. Python site tests check all five source paths and preview frames. Real keyboard, assistive technology, zoom/RTL, visual and performance verification remains pending. Details: [Phase 6 evidence ledger](../docs/visual-catalog-refactor/12-phase-6-composed-patterns.md).

## Phase 7 — complete synthetic feature reference

A single new canonical feature, [Review Workspace](../features/review-workspace/spec.md) (`feature.review-workspace`), demonstrates a human review queue with record selection, detail evidence, reason capture, approve/return/reject decisions, explicit pending/confirmed/denied/conflict/error/unknown outcomes, and focus recovery intent. It uses only synthetic fixture records and an in-memory adapter; **no server, authorization enforcement, persistence, audit or real business rules**.

Sources: `site/src/implementations/features/review-workspace/ReviewWorkspace.js`, `mock-adapter.js`, `scenarios.js`, `ReviewWorkspace.css`. The preview build copies the reviewed `mock-adapter.js` before the actual UI source, and exposes both scripts verbatim in source viewers. All scripts remain inside the existing trusted-source iframe sandbox with `allow-scripts` but no `allow-same-origin`. The example's local status verification intentionally remains unresolved after lost acknowledgement; it must not pretend a backend was queried.

The registry is now **54 entries**, with 6 components, 5 patterns and 1 feature linked to actual reference sources; the other 42 entries remain specification-only. Existing canonical IDs and paths are preserved. `node --test site/tests/review-workspace-runtime.test.cjs` tests the adapter decisions and source-level UI state transitions using the same checked-in code. This does not establish actual browser keyboard/focus, assistive-technology compatibility, responsive contrast or production readiness. See [Phase 7 evidence](../docs/visual-catalog-refactor/13-phase-7-review-workspace.md).

## Phase 8 — automated real-browser and accessibility gates

The repository now runs a separate **Chromium interaction/axe CI job** as well as the existing catalog/static/source tests. The browser job serves the generated `site/dist/`, checks search/no-JS, browse-shell reflow at 320/375/768/1440px, real Button and form interactions, synthetic Review Workspace unknown-outcome behavior and automated `axe-core` WCAG-tagged tests in **all 12 sandboxed preview frames**. It uploads machine-readable accessibility reports and desktop/mobile screenshots as the `catalog-browser-audit` GitHub Actions artifact. See [Phase 8 gate/results](../docs/visual-catalog-refactor/14-phase-8-quality-gates.md) and [successful run 42487307587](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42487307587).

The build also enforces static boot CSS **under 32 KiB**, search JS **under 8 KiB** and each compiled preview source/fixture/style set **under 64 KiB**. These are local engineering budgets, not field Core Web Vitals. Browser testing identified a real form/sandbox interaction issue and a duplicate-submit risk under unknown outcomes; both are fixed, and theme switching no longer remounts the editable example. Manual screen readers, full keyboard task review, 200–400% zoom, RTL, visual screenshot inspection and production performance remain **NOT VERIFIED**; don't claim WCAG conformance based on a green axe job.

Browser audit dependencies are installed only in CI, not needed by a visitor or to build the site. For a local browser run, follow the commands in `catalog-validation.yml` and launch `node site/tests/browser-audit.cjs` with a static server running on port 8765.

## Phase 9 — human and agent discovery parity

The canonical registry and this static site serve the same **54** entries. The website's `catalog-search.json` is **generated**, not a separate registry. The curated [Phase 9 task corpus](../tests/fixtures/phase9_retrieval_cases.json) checks expected first matches for component, pattern, feature and guidance tasks. [Phase 9 tests](../tests/test_phase9_discovery.py) verify all document routes, relationships, 12 implementation/fixture sources, and website search export parity. A contributor can generate a reproducible [provenance report](../scripts/audit_discovery.py):

```sh
python3 scripts/audit_discovery.py --output site/artifacts/phase9/discovery-audit.json
python3 -m unittest discover -s tests -v
```

CI preserves the report as the `catalog-discovery-audit` workflow artifact. Real Chromium also tests that a **human approval queue** task search opens `feature.review-workspace`, matching the canonical agent resolver. The recorded `synthetic review` miss is a discovery gap, **not** grounds to silently rewrite ranking logic. See the [Phase 9 handoff](../docs/visual-catalog-refactor/15-phase-9-agent-governance-handoff.md).

To reuse a reference, start with the canonical spec, source and scenarios; treat code as educational/synthetic until reviewed for the target application. Source links default to `main` for ordinary local builds but can be pinned to a verified branch name or immutable commit with `CATALOG_SOURCE_REF=docs/visual-catalog-refactor-blueprint python3 site/build.py`. GitHub Actions uses the PR head SHA automatically, so generated links refer to the code under review. The site still has no public deployment; root-path hosting and CSP decisions remain Phase 10 release tasks.

## Visitor-facing documentation versus repository evidence

The website deliberately does **not** expose project phase/batch identifiers or PR tracking language in the rendered canonical guidance. The site generator preserves substantive design rules from older batch-authored sections under neutral, topic-based headings and keeps their original anchors for existing deep links. Implementation-only phase appendices are omitted from website rendering because the real interactive preview and source inspector already communicate the current capability. All original Markdown remains unchanged and accessible through its source link.

This is presentation filtering only, not deletion of design knowledge or a rewrite of the canonical registry. The dedicated [concept decisions](../docs/visual-catalog-refactor/17-concept-inventory-and-decisions.md) and [open knowledge work](../docs/visual-catalog-refactor/19-open-knowledge-work.md) remain in repository documentation, outside the public catalog. The visitor-facing regression suite checks all canonical routes for visible internal stage/PR markers. Open work packages do not count as released features or accepted evidence.
