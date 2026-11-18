# Little Wins Settings knowledge — Batch 5 closure and integration crosswalk

**Date:** 2026-11-07 · **Catalog:** `EVEI2YONE/UI-UX-Design-System-Catalog` · **Cumulative draft PR:** [#12](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/12) · **Branch:** `docs/settings-knowledge-batches-2026-11-07` · **State:** proposed, unmerged.

## Fresh context collected before Batch 5

- Re-fetched `main` baseline and compared the current shared branch: at start of batch, 20 commits ahead, zero behind; reviewed the canonical registry, contributing/agent contracts, quality gates, existing account/settings batch history, earlier Little Wins feature lifecycle ledger, and Settings Batches 1–4.
- Rechecked the user-supplied **cleaned F20 Little Wins snapshot** locally. Its revamped route catalog defines `/w/:workspaceId/settings` as a management route, but there is **no** `app/w/[workspaceId]/settings/page.tsx`. The old Settings UI was removed in the user-provided cleaned snapshot.
- Little Wins product decision register: `DEC-004` owner-operated MVP is **proposed**, `DEC-009` review atomicity **open**, `DEC-010` reporting calendar semantics/timezone **open**, `DEC-014` points corrections after redemption **open**. Do not label these approved.
- `shell/context/display-preferences.ts` persists only `light` / `high-contrast` and `comfortable` / `compact` as browser-local UI preferences. `server/modules/history/index.ts` uses UTC for reporting. `server/modules/reviews/index.ts` defines `approval_required` and capability-gated `trusted_recorder_acceptance`. The legacy `settings` domain command changes group metadata and three feature booleans. This is **source evidence**, not an implemented new Settings experience or runtime test result.
- Canonical disposition: **extend** `pattern.account-settings-portal` (single owner); **reuse** `pattern.task-flows` for capability matrices, `pattern.interaction-recovery` for review states, `pattern.role-aware-workspaces` for authorization/audit visibility, `foundation.design-tokens` for appearance, `guidance.internationalization` for locale, `guidance.privacy-trust` for retention, and `pattern.offline-sync`/`pattern.forms` for state recovery.

## Eight-gap traceability matrix

| Gap | Knowledge delivered on PR #12 | Existing canonical owner | Little Wins affected consumer | Remaining product decision / required proof |
| --- | --- | --- | --- | --- |
| KG-001 Configuration registry | Batch 1: key, scope, type, default, effective value, persistence, version, dependencies, owner/evidence | [Settings portal](../../patterns/account-and-settings-portal.md#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07) | Future Settings page, workspace APIs, feature state | Choose authoritative config storage/write API; verify integration and migration |
| KG-003 Authorization & scope | Batch 1: separate server read/write capability and tenant validation | [Settings portal](../../patterns/account-and-settings-portal.md#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07), role-aware workspaces | Owner-only route `/w/:workspaceId/settings`, workspace service | Confirm actor model and direct request denials; DEC-004 proposed |
| KG-006 Saving & recovery | Batch 1: dirty/save/validation/version conflicts/timeout propagation | Settings portal, forms, offline recovery | Revamped mutations and display provider | Define transactional save strategy; test concurrent writes and failure recovery |
| KG-002 Feature dependencies | Batch 2: stored flags versus effective capabilities, UI consequence and pending-work disclosure | [Settings portal](../../patterns/account-and-settings-portal.md#settings-knowledge-batch-2--feature-and-policy-configuration-proposed-2026-11-07), task-flows | Points, Challenges, Rewards, pending redemptions | Confirm each disable/re-enable transition; DEC-014 open; test all 8 flag combinations |
| KG-005 Review policy transitions | Batch 2: mode activation, queued requests, policy version, historic outcomes | Settings portal, interaction recovery | Review service, submissions, points credits | DEC-009 open; capability gate is not implemented authorization for independent recorders |
| KG-004 Time/reporting | Batch 3: timezone boundary, event-date selection, DST, historical re-bucketing and cache | [Settings portal](../../patterns/account-and-settings-portal.md#settings-knowledge-batch-3--time-and-personal-preferences-proposed-2026-11-07), internationalization | History and period queries | **DEC-010 open**; UTC only in F20; do not expose timezone control yet |
| KG-008 Display preferences | Batch 3: device/account scope, effective mode, saved-vs-session and fallback | Settings portal, design tokens, accessibility | Existing display preference provider and Settings appearance panel | Reuse browser-local provider; no dark/system/account-sync claim; browser/a11y verification |
| KG-007 Configuration audit | Batch 4: event identity, actor, revision, safe summaries, access, retention and reversal | [Settings portal](../../patterns/account-and-settings-portal.md#settings-knowledge-batch-4--configuration-governance-and-audit-proposed-2026-11-07), privacy, role-aware | Future workspace configuration history | No confirmed config event store/viewer; agree security/legal ownership, retention, redaction and data correction |

**Scope:** These are knowledge coverage links, **not implementation status**. The generic canonical entry is proposed; affected consumers require separate product-level implementation, authorization and runtime tests.

## Proposed Settings MVP contract to implement after PR review

1. Route and server-protected owner workspace context; render available Sections (General, Features, Appearance). Do not assume unfinished tabs exist.
2. General: group/workspace name and description with server-side persistence, explicit validation, user-visible save and recovery.
3. Features: Points, Challenges, Rewards backed by domain-approved dependency/transition rules; preserve historical records and pending-work management. Verify effective actions, not just visible toggles.
4. Appearance: reuse `light`/`high-contrast` and `comfortable`/`compact`; store separately from workspace policy.
5. Show current approval and UTC reporting mode **read-only** where truthful until DEC-009 / DEC-010 and capability/security requirements are resolved.
6. People & access, export, audited settings history, advanced roles and additional display modes remain future work until their underlying contracts and actual capabilities are implemented.

## Batch 5 verification ledger

| Gate | Result | Evidence and limitation |
| --- | --- | --- |
| Context refreshed | PASS (source/connector review) | Main/branch compare, catalog concepts and locally mounted cleaned F20 snapshot |
| Reuse versus duplicate catalog entry | PASS (source review) | Single canonical `pattern.account-settings-portal`; no new concept ID added |
| Gap coverage | PASS (document check) | KG-001 through KG-008 mapped to Batches 1–4 and consumers above |
| Registry structure and discoverability | PASS (focused connector inspection) | JSON parses, IDs unique, relevant aliases, root/nested navigation and changelog are linked |
| Markdown cleanup | PASS (focused source check) | Corrected escaped code delimiters introduced during Batch 1 |
| Regression test coverage authored | PASS (source review) | [Settings lookup and gap checks](../../tests/test_settings_knowledge_coverage.py) |
| `python3 scripts/validate_catalog.py` | NOT VERIFIED | GitHub connector supports file reads/writes but not local checkout execution; direct Git access from this environment could not resolve GitHub |
| `python3 -m unittest discover -s tests -v` | NOT VERIFIED | Test file authored but not executed in repository runtime |
| Full Markdown links, manual UX, WCAG, RTL, browser API and authorization | NOT VERIFIED | Requires repository CI/product runtime and human review |
| Product decisions DEC-004/009/010/014 | OPEN / PROPOSED | Defined in F20 decision register, not resolved by knowledge guidance |
| PR review and merge | NOT VERIFIED / NOT MERGED | Keep draft until engineering/catalog reviewers validate |

**Review owner:** unassigned. **Catalog lifecycle:** proposed; no claim of a production Settings implementation, audit event service, security approval, or verified accessibility.

## Review and acceptance handoff

- Run `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` on the PR head; fix failures before requesting review. Run a full relative-link/anchor check if CI does not already cover anchors.
- Review the canonical Settings portal for non-duplicative contracts, accurate links and policy boundaries. Assign catalog, application, security and privacy reviewers as appropriate.
- In the **Little Wins product repository**, log decisions for configuration API, feature transition semantics, review policy, timezone, and audit retention. Keep product changes in their own PR; PR #12 is documentation knowledge only.
- Confirm manual keyboard/focus, screen reader, high-contrast/density, zoom and RTL readiness in the implemented Settings experience, not from this catalog text.
- Reconcile with `main` and any overlapping active PR before marking PR #12 ready for review. Do not merge the shared PR until all review gates have evidence.

## Closure disposition

All eight **knowledge topics are documented**, with one canonical Settings owner and explicit reusable links. Batch 5 closes the documentation **coverage mapping**, not implementation or formal validation. Remaining work is the unexecuted repository test suite, human review, product decisions and application implementation.
