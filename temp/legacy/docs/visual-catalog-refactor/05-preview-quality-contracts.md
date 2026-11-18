# 05 — Implementation preview, quality and readability contracts

## Preview model

The website renders **actual reference source code** for an entry, not a decorative imitation. An entry can have many scenarios (default, pending, invalid, success, unknown result, permission denied), and each scenario uses seeded synthetic data, no real credentials or external writes, and a deterministic reset. A preview cannot imply backend authorization or transaction success.

## Required files per demonstrated entry

```text
site/src/implementations/components/button/
├── Button.tsx              # actual reference implementation
├── Button.module.css       # scoped token-driven styling
├── scenarios.ts            # fixture IDs and state setup
├── preview.tsx             # wires real implementation to scenario host
└── Button.test.tsx         # interaction/keyboard/semantic tests
```

For a feature add typed adapter interfaces and `mock-adapter.ts`, with test cases for concurrency, ambiguity and recovery. Do not embed real product API clients.

## Scenario matrix

| Level | Scenarios required |
| --- | --- |
| Control | Default, hover/focus where meaningful, disabled/read-only, loading, error, long label and translated/RTL where supported |
| Pattern | Initial, empty, loading, valid, invalid, recoverable network error, retry, success; verify focus and announcement |
| Feature | First use, data, empty, loading, partial, permission denied, validation error, dropped acknowledgement, stale revision/conflict, retry/resume, complete, long data |
| All applicable | Keyboard, screen reader, narrow and wide viewport, 200%/400% zoom, high contrast, reduced motion |

## Human-facing visual quality

Check readable type scaling, line lengths, contrast, white-space grouping, scannability, stable actions, helpful copy, density (compact and comfortable only if needed), non-color signifiers, focus visibility, content expansion and zoom. Test long labels, mixed-direction content and realistic data; do not optimize for a perfect synthetic screenshot alone.

## Developer readability

- Prefer small named components, clear props and owned state, not giant context-dependent wrappers or variant explosions.
- Keep UI-only code separate from fixtures, adapters and business commands.
- Use semantic tokens and scoped styles, document any justified inline runtime value.
- Use stable typed interfaces, limited exported API surfaces, explicit dependencies and predictable error states.
- Source shown on the website must be identical to the implementation used for the preview.

## Performance quality

For the site: static or server-rendered documentation and indexes; load interactive components only where needed; reserve preview height to avoid layout shifts; avoid high-cost preview bundles on catalog listing pages. Profile an actual implementation on representative devices/networks. Capture lab CPU/network settings and results. Evaluate user-facing LCP, INP and CLS for deployed pages at appropriate percentile segmentation where field data exist. No universal per-component performance score is implied by application Core Web Vitals.

For feature previews: bound rendered records, paginate or virtualize only when justified and tested with accessibility, avoid enormous synchronous fixtures, cancel/clean up asynchronous work, prevent artificial duplicate renders or runaway polling, test at least one constrained/long-data case and record source/bundle impact. Choose budgets based on baseline measurements and representative consumers.

## Security, privacy and resilience

- Synthetic fixtures and identifiers only; no real accounts, tokens, personal submissions or secrets in screenshots or URLs.
- Preview 'Approve' or 'Save' controls cannot call production endpoints; fake adapters are local and resettable.
- Preview execution is isolated from catalog chrome; prevent actions from navigating or overwriting shared search state.
- Apply safe CSP/iframe boundaries where appropriate. Do not evaluate arbitrary supplied JSX/JS in the browser.
- An optimistic demo response is never presented as a verified server outcome; model pending, uncertain and confirmed separately.
- Respect reduced-motion preferences and do not use animation as the only status indicator.

## Evidence status model

Use **distinct dimensions**: `spec_reviewed`, `implementation_present`, `automated_tested`, `browser_reviewed`, `human_accessibility_reviewed`, `performance_measured`, `integration_validated`. Each is PASS/FAIL/NOT VERIFIED/N/A with evidence link, date, environment and reviewer. A catalog entry may remain `proposed` even if a working preview exists.

## Required CI and manual gates

| Gate | CI | Human review |
| --- | --- | --- |
| Registry and discovery | Python schema, links, alias regression | Search relevance for real tasks |
| Build | Typecheck, lint, production build | Browser smoke on deploy preview |
| Interaction | Unit/integration/state scenarios | Keyboard-only and error recovery |
| Accessibility | Automated axe-type checks | Screen reader, focus and zoom |
| Themes/locales | CSS/token checks, visual snapshots | Contrast, reflow, RTL when applicable |
| Performance | Bundle/build budgets and lab regression | Representative network/device review |
| Readability | Source lint and documentation completeness | Comprehension and visual hierarchy |
| Evidence | File/link consistency | Named owner signoff where required |

## Failure and rollback

A broken site should not block direct Markdown/JSON retrieval; the repo's search tooling remains useful. If a preview fails, disable only its registered preview mapping and show the spec-only page. Revert an isolated site feature PR rather than rewriting canonical guidance or the app. All tests are **NOT VERIFIED** for this planning document; the table specifies future checks, not passes.
