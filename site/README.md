# Embedded visual catalog website (Phases 3–4)

This directory contains the working **static knowledge browser and an isolated live reference preview** for the UI/UX Design System Catalog. It is built from the repository's canonical Markdown and catalog/index.json, not a second manually maintained knowledge database.

## Build and serve locally

Requires **Python 3.10+** to build, using only its standard library; **Node.js 18+** is needed only to run the reference behavior tests. No npm install, UI package publishing, application backend or deployment account is required.

    python3 site/build.py
    python3 -m unittest discover -s site/tests -v
    node --test site/tests/button-runtime.test.cjs
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
- Future executable examples: site/src/implementations/ (Phase 4+; not yet present)
- Future preview isolation and scenarios: site/src/previews/ (Phase 4+; not yet present)
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
