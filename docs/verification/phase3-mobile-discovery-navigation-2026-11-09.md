# Phase 3 — Mobile discovery and navigation

Status: **planning / evidence collection**. This document opens a reviewable Phase 3 workstream; it does **not** claim the UI changes have been implemented.

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
