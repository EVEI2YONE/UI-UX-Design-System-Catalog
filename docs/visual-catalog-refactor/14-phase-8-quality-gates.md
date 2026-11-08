# 14 — Phase 8: accessibility, performance, readability and real-browser verification

**Delivery:** PR [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16), branch `docs/visual-catalog-refactor-blueprint`  
**Baseline:** 54 canonical concepts: 12 executable references and 42 specification-only entries  
**Automated gate:** **PASS** on commit `453cb41074b4517e297006d223006fbece85a1d7` — [GitHub Actions run 42487307587](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42487307587).  
**Human visual, assistive-technology, security and production performance gate:** **NOT VERIFIED**.

## Scope and evidence discipline

Phase 8 strengthens the *real* catalog and its reference implementation examples. It does not claim that a successful `axe-core` run means WCAG conformance, that a Chromium screenshot has been manually reviewed, or that local static bundle-size checks measure real-user Core Web Vitals.

The quality job is separate from the Python/catalog unit-test job. **Both jobs passed** in the linked run. The workflow uploaded `catalog-browser-audit` artifact ID `13620360441` (12 machine-readable per-reference automated accessibility reports and desktop/mobile Review Workspace screenshots). Artifact collection is evidence availability, **not** visual approval.

## Quality changes

| Path | Change | Why |
| --- | --- | --- |
| `site/tests/browser-audit.cjs` | Real Chromium smoke for browse/search/no-JS, responsive shell, Button/theme/reset, form unknown outcome, Review Workspace decision + verification; axe checks inside 12 sandboxed frames | Existing Node DOM fixtures cannot detect browser-specific behavior |
| `.github/workflows/catalog-validation.yml` | Adds Chromium/axe CI job, local static server and uploaded screenshots/JSON reports | Repeatable, inspectable QA without deploying the site |
| `site/tests/test_quality.py` | Build-time asset-size limits, all preview source-size limits, duplicate route and trusted iframe/source integrity checks | Protect static site loading and safe generated content |
| `site/src/previews/preview-runner.js` | Switch themes without remounting and losing user-entered state; restore scenario-selector focus | Prevent unexpected content/focus loss |
| `site/src/implementations/patterns/form/Form.js` | Guard known/unknown outcome resubmission and handle synthetic click without iframe form-post permission | Prevent false retry and correct sandboxed browser behavior |
| `site/tests/browser-audit.cjs` subsequent fixes | Supply valid form data before testing outcome; wait for native option attachment rather than visibility | Make browser checks exercise actual intended behavior |

## CI checks — actual results

| Verification | Coverage | Result |
| --- | --- | --- |
| Existing canonical registry validator and agent lookup | 54 entries, links, existing aliases and related IDs | PASS |
| Python root and static site tests | All generated pages, source parity, isolation and spec fallback | PASS |
| Node source tests and syntax checks | 6 components, 5 patterns and Review Workspace including synthetic adapter | PASS |
| Build-time payload budgets | Site CSS under **32 KiB**, site search JS under **8 KiB**, each reference's combined source/scenarios/styles under **64 KiB** | PASS |
| Chromium interactive smoke | Task search, zero results, no-JS listing, default Button/theme/reset, form validation and unknown state, Review Workspace unknown state | PASS |
| Chromium shell viewport reflow | Catalog page at **320, 375, 768, 1440 CSS pixels**, no document-level horizontal overflow | PASS |
| Automated axe audit | **All 12 reference preview frames**, default scenario, WCAG 2.0/2.1/2.2 A/AA rule tags; no axe **critical/serious** violations | PASS for the scanned states/rules |
| Artifact upload | Per-preview axe JSON and Review Workspace desktop/mobile screenshots | PRESENT |
| Real screen readers/AT and keyboard-only end-to-end review | NVDA, VoiceOver, focus paths, announcements across *all* scenarios | NOT VERIFIED |
| All responsive/zoom/RTL/forced-color scenarios | 200–400% zoom, actual mobile devices, RTL and forced-colors | NOT VERIFIED |
| Full visual review | Human inspection of generated screenshots, hierarchy and content | NOT VERIFIED |
| Production LCP/INP/CLS and field percentile measurements | Real deployment and real-user data | NOT VERIFIED |
| User research and comprehension of decisions | Representative users and task success | NOT VERIFIED |
| Security/privacy and hosting hardening | Threat model, CSP, dependencies and release policy | NOT APPROVED |

**Interpretation:** the build-size checks are engineering budgets, *not* evidence of field performance. The axe scan blocks **serious/critical** failures only; moderate/minor findings may remain and must be evaluated, not silently treated as compliant. The actual artifact contains the detailed per-frame findings for follow-up.

## Findings discovered by running an actual browser

1. **Form sandbox incompatibility — fixed.** The preview intentionally omits `allow-forms`; relying solely on a native submission event prevented the synthetic action from running in real Chromium. The form now intercepts button activation while retaining a semantic form and submission handler, with no permission to post real forms.
2. **Recovery lock — fixed.** A simulated unknown outcome previously could re-enable the form's submit control. The form now remains locked until authoritative reconciliation, and a reset cannot silently make retry safe.
3. **Preview theme reset — fixed.** A theme change originally remounted the current example, discarding edits. Theme controls now change tokens without remounting; scenario changes intentionally reset state and restore selector focus.
4. **Test harness correction — fixed.** The browser test must enter valid values before exercising an unknown outcome, and wait for native select options to be attached rather than visible. Neither correction changes production reference semantics.
5. **Remaining architectural concern.** Several Phase 4–7 sources are dense/minimally formatted and duplicate limited CSS patterns; human developer-readability review and any shared token extraction remain open. Do not mark them as fully refactored solely because lint/syntax tests pass.

## Manual quality-review matrix before release

| Surface | Inspect manually | Suggested gate evidence |
| --- | --- | --- |
| Catalog browser and search | Actual mobile layout, 200%/400% zoom, keyboard order, skip links, no-JS fallback, dark mode, long titles | Screenshots, screen recordings or reviewer notes and reproduction details |
| Six controls | Native keyboard semantics, focus visibility, validation announcements, disabled/read-only distinction, contrast/high contrast | Per-state browser/AT notes |
| Five composed patterns | Focus after errors, form retry lock, table keyboard/pagination, navigation Escape and current-page semantics, empty/error distinctions | Workflow outcomes and AT observations |
| Review Workspace | Selection focus, reason validation, pending duplicate action, confirmed vs unknown messaging, conflict/permission errors, queue at narrow widths | Human-assisted task walkthrough + source contract review |
| Runtime isolation | Iframe sandbox, no real writes/secrets, source parity and safe preview resource policy | Security reviewer signoff and CSP/hosting decision |
| Performance | Lab profile under constrained CPU/network, rendering long docs, measuring browser interaction, eventual production 75th percentile CWV | Device/network/environment with LCP/INP/CLS data |
| Content & localization | Truncation, large translated text, RTL reading order, consequences and plain-language recovery | UX writing/i18n review |
| Visual craftsmanship | Review screenshots and physical devices at comfortable/compact widths | Named reviewer, date, observations, remediation status |

## How to rerun

From the repository root:

```sh
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 site/build.py
python3 -m unittest discover -s site/tests -v
node --test site/tests/button-runtime.test.cjs
node --test site/tests/core-controls-runtime.test.cjs
node --test site/tests/patterns-runtime.test.cjs
node --test site/tests/review-workspace-runtime.test.cjs
```

For the actual browser check, use the [catalog-validation GitHub Actions workflow](../../.github/workflows/catalog-validation.yml) or install the workflow's pinned Playwright/axe versions, install Chromium, serve `site/dist/` at `http://127.0.0.1:8765`, and run `node site/tests/browser-audit.cjs`. The browser job downloads external testing dependencies **in CI only**, not for site visitors. Its screenshots/reports remain build artifacts, not committed binary fixtures.

## Gate outcome and handoff

**Phase 8 automated QA gate: PASS.** **Phase 8 manual acceptance: PENDING.** Keep PR #16 in draft. Phase 9 may document human/agent retrieval regression and evidence handoff, but neither automated axe nor a green CI suite authorizes claiming the website fully accessible, production-performant, secure, or reviewed by actual users.
