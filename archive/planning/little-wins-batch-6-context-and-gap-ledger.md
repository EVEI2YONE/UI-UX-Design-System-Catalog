# Batch 6 — Little Wins data lifecycle and migration context/gap ledger

**Date:** 2026-11-07 · **Branch:** `docs/little-wins-platform-collaboration-gaps` · **PR:** [#7](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/7) · **Status:** proposed docs-only guidance; not merged, not an application implementation.

## Context intake before editing

**Target input:** user-supplied `Little_Wins_Source.zip` archive (source snapshot; no verified GitHub target SHA). Inspected its `README.md`, `features/contributions/domain.ts`, `app/api/workspace/route.ts` and directory/migration inventory. The README describes a Sites-native owner-operated pilot with D1 storage and compare-and-swap revisions; its finalized external architecture draft was not supplied.

**Source-observed:** `normalizeProjects` assigns legacy unscoped challenges/submissions to `general`, retaining their IDs and point transactions. The API `read()` archives sample groups from active `groups` into `archivedSampleGroups` using a revision-checked UPDATE, so an otherwise read-oriented call can change persisted storage. GET omits archived samples from its visible result. POST retries revision conflicts up to four times. The state is an aggregate JSON payload per authenticated owner; the code does not establish a user-facing export or restore capability. No production restore exercise or load baseline was available.

**Avoid misclassification:** missing export/restore in the app is app-specific; the reusable catalog knowledge gap is the under-specified *decision and verification contract* for archive, migration, user-facing portability and rollback. A database backup is not necessarily an end-user export. An archived record is not erased. Production deployment assurance remains NOT VERIFIED.

## Canonical discovery and gap decisions

| KG ID | Existing canonical entry checked | Classification | Reusable addition | Disposition |
| --- | --- | --- | --- | --- |
| KG-LW06-01 | `guidance.privacy-trust` / `guidance/privacy-consent-and-trust.md` already mentions delete/download and retention | Incomplete | Archive/delete/retention distinctions, export/import contract, corrections and privacy-sensitive history | Extend, not create |
| KG-LW06-02 | `pattern.offline-sync` / `patterns/offline-sync-and-conflicts.md` already addresses conflicting writes and uncertain persistence | Incomplete | Idempotent aggregate migrations, read-side writes, schema versions, restoration and revision conflicts | Extend, not create |
| KG-LW06-03 | `governance.quality` / `governance/quality-gates.md` already covers generic rollback and concurrency | Incomplete | Negative migration, restore, export, ledger and contention acceptance cases | Extend, not create |
| KG-LW06-04 | Root/nested README and `AGENTS.md` lookup | Discoverability | Link canonical entries and context ledger without duplicate IDs | Index updates |

**Other sources checked:** `patterns/service-recovery-and-support.md`, `patterns/interaction-states-and-recovery.md`, `planning/batch-12-context-and-gap-ledger.md`, `catalog/index.json`, `CONTRIBUTING.md`. No new catalog registry entry, duplicate guideline, new schema, or product code is needed.

## Reference applicability

- [UK ICO data protection by design and default](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-by-design-and-by-default): privacy minimization and lifecycle considerations; jurisdiction-specific, not a universal rule for Little Wins.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): authorization and secure operations starting points, not deployed-product validation.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/): web accessibility target for control and status UX; not a claim of passing.
- [MDN IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) and [Storage quotas and eviction](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria): relevant if a client local draft mechanism is designed, not proof that Little Wins uses IndexedDB.
- [Cloudflare D1 documentation](https://developers.cloudflare.com/d1/): platform-specific backup/export capabilities must be checked for the actual deployment and plan. Do not infer that they are installed, scheduled or tested.

Reference links are pointers for review, not asserted to have been live-verified this batch.

## Batch acceptance and verification

- PASS (connector evidence): fetched existing source documents and repository guidance before proposing changes; preserved canonical IDs; updated root/nested README and AGENTS navigation; commits confined to catalog documentation branch.
- NOT VERIFIED (until CI finishes): `python3 scripts/validate_catalog.py`; `python3 -m unittest discover -s tests -v`; Markdown link checking. Do not mark documentation CI passing until a GitHub Actions result confirms it.
- NOT VERIFIED (product/runtime): user-facing export, backups, actual restore, migration fixture tests, concurrent mutation performance, privacy-law assessment, production Sites authentication, browser accessibility and user studies.
- Review owner: unassigned; human product/security/privacy review required before using these proposed guidelines as release gates.

## User-value rationale and next step

Preserving a trustworthy history and clear archive/export/recovery semantics matters more than visual refinement in a contribution-and-rewards workflow. Keep this batch in the existing draft PR #7 for review. No target implementation PR was requested.
