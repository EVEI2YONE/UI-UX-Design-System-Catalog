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
