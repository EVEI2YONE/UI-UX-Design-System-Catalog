# Phase 3 — Mobile discovery and navigation

Status: **implemented on draft PR #20, awaiting independent QA**. Developer self-checks are recorded below; they are **not** QA signoff. The immutable implementation SHA is recorded in the PR #20 description and the developer-to-QA handoff (a commit cannot contain its own SHA).

## Source baseline
- Canonical catalog repository: `EVEI2YONE/UI-UX-Design-System-Catalog`
- Starting `main`: `13d8292850db76e5435f81cc74f5f6b7fc869762`
- Baseline merged change: PR #18 (discovery and reference-behavior corrections)
- Source: rendered visual audit of PR #18, 2026-11-09, findings F4, F8 and F9.

## Goals and scope
1. **F4 — Mobile discovery:** At 390 × 844 CSS pixels, show the first result title and availability without scrolling; target title at or above 640 CSS pixels. Keep category filters accessible through compact controls, with visible active selection and a clear recovery action. Verify at 320 and 768 pixels.
2. **F9 — URL-backed search state:** Query, category and interactive-only state survive refresh, shared links, Back and Forward. Preserve filter behavior and search focus; avoid noisy announcements and excessive history entries.
3. **F8 — Detail navigation:** Provide top-of-page jump navigation for Example, Guidance, States and Source when the corresponding sections exist. Improve readability of mobile documentation tables without losing columns or keyboard access. Test reflow at narrow widths and zoom.
4. **Continuity:** Preserve 54 canonical concept identities, all 12 reference implementations, proposed/reference labeling, existing semantics, sandbox isolation and existing regression coverage.

## Investigation before implementation
- Inspect `site/build.py` page generator for browse/search duplication and detail-page section markup.
- Inspect `site/static/search.js` for current URL parameter parsing and filter handling.
- Inspect `site/static/styles.css` and mobile breakpoints for filter density, focus visibility, and scrollable tables.
- Review existing Playwright browser audit and test harness; add regression assertions before UI changes.
- Confirm deployment and manual accessibility limitations described in `docs/verification/reference-feedback-queue-contrast-2026-11-09.md`.

## Implementation slices (pending code review)
- A. Mobile filter layout and accessible disclosure with active-filter summary.
- B. Shareable URL-backed state with deterministic navigation behavior.
- C. Detail page section links, focused navigation and responsive documentation affordances.
- D. Responsive, keyboard, reduced-motion and automated regression checks, with screenshot-based verification.

## Acceptance gate
- CI catalog validation, site build, Python/Node/browser tests pass.
- Focus order, keyboard and screen-reader behavior explicitly assessed where tools permit; manual items marked NOT VERIFIED otherwise.
- No new canonical registry entries or dependency/platform changes without separate approval.
- PR remains draft until code, tests and visual verification are reviewed. No auto-merge.

## Source inspection findings — after PR creation

Context source: live `main` at `13d8292850db76e5435f81cc74f5f6b7fc869762`; no Phase 3 UI change has been made.

- **Mobile filter layout (F4):** `site/build.py` emits search, then nine always-visible category chips, then interactive-only checkbox and results count inside a padded `.tools` section. `site/static/styles.css` retains 24px tool padding, 18px chip top margin, 54px desktop container top padding (36px at <=600px), and no mobile chip disclosure. A semantic `<details>` disclosure or accessible button/panel needs a specific no-JS policy; keep category choices usable without JavaScript.
- **URL state (F9):** `site/static/search.js` initializes only `q` from location.search; `category` always starts at `all`, interactive-only starts unchecked, and changes only update the DOM. Plan bounded `q`, `category`, `interactive` parameters, validation of category values against the rendered chips, `replaceState` for typing and `pushState` for deliberate filter actions if practical, and a `popstate` restore path. Check both `/catalog/` and `/search/`.
- **Detail navigation (F8):** `site/build.py` currently renders breadcrumb, metadata, preview/spec notice and canonical markdown `article` plus source aside, but no page-level jump navigation. `render_md` produces heading anchors; section links should reference actual present headings, avoid duplicate IDs, and distinguish preview section from markdown sections. Tables are wrapped by `<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table">`; CSS enforces `min-width:480px` and overflow:auto; add a visible scroll hint and confirm focus/reflow rather than removing access.
- **Existing tests:** `site/tests/browser-audit.cjs` already checks 320/375/768/1440 widths for page-level horizontal overflow, task search, filter combination, clear reset and sandboxed reference previews. It does **not** yet test mobile first-result position, collapsed filter operability, URL reload/history persistence, section jump links or table-scroll discovery.
- **Constraints:** Existing catalog uses stdlib-generated static pages, lightweight JS, and sandboxed iframes. Maintain progressive enhancement and canonical content. The original audit's 390px captures were desktop Chromium responsive viewports, not physical-device tests.

## Proposed acceptance test matrix
| Area | Test |
| --- | --- |
| 320 / 390px | first card title and availability visible above fold; active filters discoverable and operable by keyboard |
| 768 / 1440px | tools and grid keep readable density and no page overflow |
| URL | direct deep link, reload, copy/paste, clear, Back and Forward preserve query/category/interactive state |
| Details | top jump links reach existing Example, Guidance, States and Source regions; no missing targets or duplicated IDs |
| Tables | all columns reachable with keyboard, horizontal-scroll affordance visible, no document-wide horizontal scroll |
| Accessibility | focus order, labels, dark mode, reduced motion, 200/400% zoom manually verified where available; otherwise explicitly NOT VERIFIED |

## Implementation record (developer, 2026-11-09)

Baseline reconciled before editing: PR #20 head `c506228a6826e88597d4e0f2a728087d29de50b0`, `main` `13d8292850db76e5435f81cc74f5f6b7fc869762` — both matched the handoff; no Phase 3 UI code existed, so nothing was duplicated or overwritten.

### F4 — compact mobile discovery
- `site/build.py` tools markup: search label/input, then a native `<details id="category-panel">` whose `<summary>` reads **Category: <current>**, containing all nine `aria-pressed` category chips (`role="group"`), followed by the always-visible **Interactive examples only** checkbox.
- Status row: visible count (`#result-count`), active-filter summary (`#active-filters`, e.g. "1 filter active: Patterns") and a **Reset filters** button shown only when state differs from default. The existing empty-state `#clear-filters` is unchanged and shares the same reset routine.
- `search.js` collapses the disclosure at `max-width: 600px` and opens it on wider screens until the person toggles it. CSS tightens intro/tools spacing at <= 600px only.
- No-JS policy: the filter row (`#filter-controls`) is rendered `hidden` and revealed by the script, so JS-less visitors are not shown inert chips; all 54 cards remain listed and a `<noscript>` line says filtering needs JavaScript.
- Developer measurement (desktop Chromium 141 headless, CSS-pixel viewports): first card title top at 390x844 — `/catalog/` **559px** (was 743), `/search/` **596px** (was 826); availability badge bottom 698 / 734px (<= 844). 320x700: 559 / 641px. No page-level horizontal overflow at 320/375/390/768/1440.
- Accepted trade-off: at 768px and 1440px the first title moves ~10-50px lower than before because the disclosure summary occupies a row (768: 715px vs 663px; 1440: 661px vs 652px); it remains within the 900px viewport. Flagged for reviewer judgement.

### F9 — URL-backed state
- Schema: `q` (trimmed, max 200 chars), `category` (must equal a rendered chip value; `all` default is omitted), `interactive=1`. Unknown/invalid values fall back to defaults and are removed from the URL with `replaceState` on load; unrelated query parameters and the hash are preserved.
- History policy: typing -> debounced (300 ms) `replaceState`; category chip, interactive toggle, Reset/Clear -> one `pushState` (only when the URL changes); `popstate` restores controls, `aria-pressed`, count and cards without writing history or moving focus.
- Announcements: the visible count is no longer a live region; a single visually hidden `role="status"` (`#result-status`, polite, atomic) is updated 900 ms after typing settles or 150 ms after a deliberate toggle.
- Clear/Reset returns controls and URL to defaults and focuses search. Behaviour is identical on `/catalog/` and `/search/`.

### F8 — detail navigation and tables
- Every concept page gets `<nav aria-label="On this page">` before metadata, linking only sections that exist: **Example** (`#doc-example`, the sandboxed live preview — 12 reference pages only), **Guidance** (`#doc-guidance`, the canonical article), **States** (reuses an existing Markdown heading anchor such as `#task-flow-and-states`; otherwise the first table whose first column header is "State(s)" gets `#doc-states`; present on 24 of 54 pages), **Source** (`#doc-source`, the "Source of truth" aside, now `aria-labelledby` its heading).
- `section_navigation()` fails the build on duplicate guidance IDs or collisions with the reserved `doc-*` IDs. Heading levels are unchanged.
- Tables are wrapped in `.table-wrap` with a visible "Scroll sideways for more columns" hint (`aria-hidden`; shown at <= 600px without JS, and exactly when the table overflows with JS) plus edge scroll shadows. The focusable `role="region"` / `tabindex="0"` scroll container is unchanged.
- Fenced code blocks render as `<pre tabindex="0">` so overflowing code is keyboard-scrollable (fixes a pre-existing axe `scrollable-region-focusable` finding on spec pages at 390px).

### Regression coverage added
- `site/tests/test_build.py`: compact filter markup, single live region, jump links resolve to unique existing IDs on all 54 pages, no Example link on spec-only pages, States anchor reuse, reserved-ID collision fails closed, table hint/region and focusable code markup.
- `site/tests/browser-audit.cjs` (`phase3()`): 390x844 first-result/badge position on both routes, collapsed disclosure keyboard operation and summary, overflow with filters at 320/375/768, deep link/reload/fresh-context share, history (no per-keystroke entries; push per toggle; Back/Forward), invalid/oversized params, zero-result clear + focus, both routes, live-region announcement count, jump-link keyboard activation and target scroll at 390/1440, table hint + keyboard scroll reaching the last column, spec-only nav, axe serious/critical on changed shell pages (iframes excluded; previews keep their own scan), no-JS hidden filter controls, and page overflow on all 54 detail pages at 320px (approximates 400% zoom reflow of a 1280px window; not true browser zoom).

### Not verified by the developer
Screen reader output, physical touch devices, real browser zoom at 200%/400%, forced-colors/high-contrast OS modes, RTL, non-Chromium browsers and hosted/deployed embeds. These remain for independent QA (TEST_MATRIX A01/A02/G01) and must be reported as NOT_RUN/BLOCKED if not executed.
