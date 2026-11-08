# Embedded visual catalog website (Phase 3)

This directory contains the working **static knowledge browser** for the UI/UX Design System Catalog. It is built from the repository's canonical Markdown and catalog/index.json, not a second manually maintained knowledge database.

## Build and serve locally

Requires **Python 3.10+**, using only the standard library. No installable UI component package, npm registry, application backend or deployment account is required.

    python3 site/build.py
    python3 -m unittest discover -s site/tests -v
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

An implementation registered in catalog metadata cannot be previewed by Phase 3's static generator. It is clearly labeled "Reference registered" with a non-interactive message until Phase 4 provides a vetted preview renderer. Do not turn such a message into proof that the renderer has been implemented.

## Performance and readability approach

All canonical documentation and cards are available in HTML before JS. Site search works by filtering pre-rendered cards and does not fetch records as the user types. Only one small JavaScript file is used for progressive filtering. CSS uses system fonts to avoid third-party font requests, plus responsive layouts, dark-mode preferences, reduced-motion handling, readable line lengths and horizontally scrollable tables. Actual browser responsiveness, screen reader behavior, field Core Web Vitals and long-content reflow still require runtime inspection.

## Security and limitations

- This is a **trusted repository-content renderer**, not a general Markdown sanitizer for untrusted user submissions. Do not pipe arbitrary user-provided Markdown through it.
- Unsupported Markdown (some nested lists, raw HTML, sophisticated tables and footnotes) may display conservatively as text rather than achieving full CommonMark parity. Phase 3 should check representative lengthy catalog pages and decide whether a full parser is justified.
- URLs with unsupported schemes are not emitted as clickable links.
- There is no remote search API, dynamic CMS, user login, real writes, arbitrary code execution or editable preview environment.
- Deployment, licensing, live browser verification and content security policy decisions belong to later gates.
