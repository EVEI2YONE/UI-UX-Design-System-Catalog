# 09 — Phase 3 static catalog website: context, decisions and evidence

**Phase:** 3 — site foundation and static browser
**Branch / PR:** docs/visual-catalog-refactor-blueprint / #16
**Implementation status:** working static build committed, CI passes, visual/human verification pending
**Base catalog:** 53 registered concepts, six canonical component specifications and no registered executable previews

## Context and technology decision

The catalog's canonical data is already Markdown plus JSON, with deterministic Python lookup and validation. Phase 3 requires readable static content, deterministic URLs, browse/search, responsive shell, source provenance and explicit spec-only fallback; **it does not yet require a React runtime, interactive demonstrations or published packages**.

**Decision P3-D01:** implement a standard-library Python static site compiler with small CSS/JS assets instead of selecting Next.js prematurely. This keeps the website directly derived from canonical sources, buildable with the existing CI Python environment and fully browseable without JavaScript. Phase 4 must evaluate whether its live React/TSX previews can mount in isolated bundles or frames without forcing the entire documentation website to adopt a client-side framework. Next.js remains an option if concrete later requirements justify a migration.

## Files and ownership

| File | Purpose |
| --- | --- |
| site/build.py | Reads catalog/index.json and canonical Markdown; validates unique routes and generates static HTML and JSON |
| site/static/styles.css | Responsive, light/dark, reduced-motion-aware site layout, card and Markdown styling |
| site/static/search.js | Optional in-page category/search filtering; cards exist without JavaScript |
| site/tests/test_build.py | Static page, source path, route, safe-link and fallback tests |
| site/README.md | Build/serve instructions, constraints and boundaries |
| .github/workflows/catalog-validation.yml | Adds actual site build and tests after root registry validation |
| .gitignore | Excludes site/dist and Python caches |

**Generated outputs (not source):** site/dist/index.html, site/dist/catalog/index.html, site/dist/search/index.html, site/dist/catalog/<category>/<slug>/index.html for each canonical concept, site/dist/catalog-search.json and site/dist/assets. The JSON is derived and never a competing registry.

## User and agent journeys

1. A human enters /catalog/, browses categorized cards, optionally searches by task or capability, and opens the canonical entry detail route.
2. The detail page renders the existing Markdown as readable HTML, exposes its canonical ID, layer, artifact kind, review status, relationships and source link.
3. When no implementation metadata exists, the page says **Specification only**. The site's current build cannot execute registered references yet, so it also explicitly labels that limitation rather than faking a preview.
4. With JavaScript disabled, all cards remain in pre-rendered HTML, and standard browser Find and direct links remain useful. An AI agent can continue to read catalog/index.json, source Markdown and scripts/find_concept.py independent of the site.

## Architecture invariants

- Canonical ID determines the slug; **the owning Markdown folder**, not registry knowledge layer, determines the browse category. Route uniqueness is a build gate.
- The root registry, canonical paths and IDs remain immutable inputs. Phase 3 does not alter catalog/index.json or the agent lookup ranking.
- Original document H1 is downgraded to H2 inside the page's single page-level H1; headings and table semantics are preserved for common Markdown.
- HTML in Markdown is escaped; links with unsupported schemes are not clickable.
- Site shell and documentation render without fetching remote services. Search is progressive enhancement.
- No static screenshot or synthetic click is claimed to implement a future control/feature. The source of Phase 4 previews remains site/src/implementations/.

## Test and evidence table

| Gate | Evidence | State |
| --- | --- | --- |
| Root catalog validator and full legacy tests | GitHub Actions 42484650867, workflow Validate catalog | PASS |
| Static build over all 53 canonical entries | Same CI run, site/build.py | PASS |
| Site structural and source/fallback unit tests | Same CI run, unittest discover -s site/tests | PASS |
| Readable without JS by construction | Pre-rendered cards, navigation and documents; inspected by tests | STATIC CONTRACT PASS; HUMAN BROWSER NOT VERIFIED |
| Agent canonical registry not reclassified | GitHub base-to-branch comparison from Phase 2 | PASS |
| Mobile layout, colors, focus, dark mode | CSS rules present | IMPLEMENTED IN CODE; BROWSER QA NOT VERIFIED |
| Interactive components / live previews | Out of scope before Phase 4 | NOT IMPLEMENTED |
| Real-world performance / Core Web Vitals | No deployed measurement available | NOT VERIFIED |
| Screen readers / keyboard / zoom | Requires actual browser/assistive validation | NOT VERIFIED |
| Deployment / public URL / CSP | Separate owner/hosting decision | NOT APPROVED |

[GitHub Actions run 42484650867](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42484650867) completed successfully for implementation commit ae5ca3e6512ae60431ba22f3fc145c348961fdcc. Later documentation-only commits require their own head validation for final review.

## Known limitations and Phase 4/8 tasks

- The Markdown renderer supports common repository constructs, but not the entire CommonMark/GFM specification (complex nested lists, raw HTML, footnotes, escaped pipes in tables, advanced heading anchor parity). Inspect representative long files and improve or replace the parser if actual content exhibits loss.
- Root-relative /assets and route paths require host-root deployment. A GitHub Pages project subpath needs explicit base URL handling before deployment.
- Search is literal token matching against pre-rendered card text; it is **not** a replacement for the canonical weighted agent resolver. User search relevance studies remain Phase 9.
- No image-based screenshot verification was performed. Dark mode, 320px-viewport reflow, screen reader, touch and visual polish need observed QA in Phase 8.
- Website text uses system fonts and no runtime third-party asset fetches, but actual bundle/paint/interaction measurements remain unavailable until served and tested.
- Phase 4 must define preview isolation, React/TSX bundling, safe synthetic fixtures and source parity on top of (or deliberately revising) this static foundation.

## Gate decision

**Automated Phase 3 build + test gate: PASS.** Full phase acceptance remains subject to human design/architecture review and real-browser/assistive checks. PR #16 stays draft, and Phase 4 is not claimed complete.
