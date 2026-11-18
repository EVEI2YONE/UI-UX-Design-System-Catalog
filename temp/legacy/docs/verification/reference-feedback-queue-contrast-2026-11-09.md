# Reference feedback, review queue and contrast follow-up

## Scope and source

This work extends PR #18 at `8e6bb3f03a0d64b98d907191dff1fae730dc8ddd`. The same PR now includes discovery availability labels, combined interactive/category/search filtering, empty-results recovery, filter alignment and content-sized badges together with the reference-behavior and contrast fixes below. Canonical source identity and the existing proposed/reference distinctions are preserved.

The changes address stale validation feedback, completed records remaining actionable in the pending review queue, conflicting preview status, and enabled-control contrast. They remain synthetic reference behavior, not backend authorization, persistence or production certification.

## Behavior and acceptance

- Input and Field accept an optional **caller-supplied** `validate(value)` callback returning corrective text or an empty string. The invalid scenario owns its demo rule; the primitive only refreshes error text, visibility and associations on native input. With no callback, the caller-provided static error contract is unchanged. Corrections preserve the editing element, value and focus; invalidating the value again restores the error. The email demo is a simple format illustration, not address or deliverability verification.
- Review reason correction updates its own error and `aria-invalid` in place. Whitespace-only reasons remain invalid for return/reject.
- Approved, returned and rejected records leave the pending list after confirmed outcomes. Completed detail stays visible as a receipt, without another decision form. **Next pending item** moves to a pending record and focuses its detail heading. The final decision produces an empty pending queue and a focused completion heading. The synthetic adapter refuses a second decision on a completed record even at its latest revision.
- Review Workspace owns its status channel. The generic preview-host status is hidden/empty for that feature, avoiding “No action taken yet” underneath a pending/confirmed/unknown result.
- Enabled control boundaries use `#637f94` in light mode (4.21:1 against white; 3.79:1 against `#eef4f8`). Dark-theme action text/hover colors are adjusted to meet the sampled 4.5:1 text target, with explicit light borders where necessary. Decorative surface dividers remain separate. Automated semantic-color checks cover six components, five patterns, Review Workspace and preview/catalog controls; they do not establish complete WCAG conformance.

## Hosting verification boundary

The repository documents a root-path static build served with Python's `http.server`. It does not declare a current production URL or a production hosting configuration. The connected Sites account has an existing **UI/UX Catalog — PR #16 Test** deployment:

- URL: https://ui-ux-catalog-pr16-test.smooth-brain-2400.chatgpt.site
- Site version: 2; source deployment commit: `b11713b4db734ee40f4aa3d392c6d11b253aef47` (hosting-source provenance, not asserted to be this repository's HEAD).
- Deployed embedded behavior: **NOT VERIFIED**. The browser reached the site's ChatGPT login gate. Automatic approval review rejected initiating sign-in because explicit sign-in authorization is required. No authentication bypass, access change or redeployment was attempted.
- Managed local embedded behavior: **BLOCKED**. In this managed browser, sandboxed frames showed unstyled host controls and no scenario options. The same result persisted when the audit wrapper used Python's `SimpleHTTPRequestHandler`, without the earlier live-reload server. The same routes worked standalone. The cause has not been established; sandbox/isolation was not weakened.
- CI's embedded browser checks use the repository's own root static server in GitHub Actions. The added regressions exercise error correction, preserved focus, review completion, next-item navigation, final completion and absence of the generic feature status **inside the existing sandboxed frames**. The CI result is reported on the PR, separately from the still-blocked deployed verification.

## Checks executed before PR

- PASS: `python3 site/build.py` — 54 canonical pages plus three index pages.
- PASS: `python3 scripts/validate_catalog.py` — 54 concepts, eight section READMEs, 1,126 relative links.
- PASS: `python3 -m unittest discover -s tests -q` — 136 tests.
- PASS: `python3 -m unittest discover -s site/tests -q` — 21 tests.
- PASS: `node --test site/tests/*runtime.test.cjs site/tests/contrast.test.cjs` — 30 tests.
- PASS: managed-browser standalone Field correction clears the error and retains the edited value/focus.
- NOT VERIFIED here: deployed embedded interaction, screen reader, touch devices, forced colors, full zoom/RTL and cross-browser accessibility.

No release, merge, hosted update or accessibility certification is implied. The next deployed check requires authorization for the existing site's ChatGPT sign-in; a successful CI run does not substitute for it.
