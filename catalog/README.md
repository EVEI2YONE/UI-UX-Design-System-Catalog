# Catalog lookup registry

[`index.json`](index.json) is the **canonical metadata inventory**. Each entry has a stable ID, canonical path, summary, synonyms (`aliases`), primary conceptual layer, content kind, status, and multiple topical `domains`.

## Search

```bash
python3 scripts/find_concept.py focus
python3 scripts/find_concept.py "error recovery"
python3 scripts/find_concept.py --layer intelligence
python3 scripts/find_concept.py --domain accessibility
```

An empty query lists all entries. Search matches partial text across titles, IDs, summaries, aliases and domains. Multiple entries may share an alias: this is useful when the same task spans concepts. Registry results point to one canonical page per entry.

## Levels and categories

- `layer` represents the concept's primary position in the **10-layer conceptual taxonomy** (`context`, `principles`, `behavior`, `tokens`, `foundations`, `primitives`, `components`, `patterns`, `experiences`, `intelligence`, or `cross-cutting`).
- `kind` describes the artifact, such as `guideline`, `contract`, `policy`, or `checklist`.
- `domains` are cross-cutting topical search terms; they do not force duplicate copies of a page.
- `status` describes the **catalog entry's review lifecycle**, not a claim that code exists.

The registry is intended for discoverability, not an implementation API. If a concept moves, preserve its ID, update the canonical path, and provide redirects/migration where old links were published. See [Contributing](../CONTRIBUTING.md).
## Agent-oriented lookup

The [JSON Schema](schema.json) describes the registry record. Every current entry requires `use_when`, `avoid_when`, `related`, `depends_on`, `owner`, and nullable `reviewed_at`; this applies to all 49 entries, including those introduced after the scaffold batches. The registry remains the only machine-readable metadata source. Related references are canonical IDs, not duplicate Markdown files.

```bash
python3 scripts/find_concept.py 'loading button' --json
python3 scripts/find_concept.py architecture.component-model
python3 -m unittest discover -s tests -v
```

Results are ranked by exact ID, exact alias, exact title, then partial text matches. Read and verify the returned entry; rank is not a recommendation or quality certification. See [agent protocol](../AGENTS.md).


## Measurement and governance queries

```bash
python3 scripts/find_concept.py 'task completion rate' --json
python3 scripts/find_concept.py 'catalog promotion' --json
python3 scripts/find_concept.py 'documentation checks' --json
```

These resolve to canonical guidance, lifecycle policy and quality checklist entries. All remain `proposed`; no observed UX outcomes or implementation conformance are implied.

## Batch 6 — consistent agent retrieval

All entries, including [role-aware workspaces](../patterns/role-aware-workspaces-and-context-switching.md), now provide owner, review date, use/avoid guidance, related IDs and dependencies. The resolver normalizes case/punctuation, ranks exact IDs and aliases first, supports `--status` and `--limit`, and excludes `avoid_when` from positive search scoring. That field still appears in JSON results so agents can interpret contraindications.

```bash
python3 scripts/find_concept.py 'role switching' --json --limit 3
python3 scripts/find_concept.py 'modal-dialog' --status proposed
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

The [schema](schema.json) specifies the complete metadata contract; the standard-library validator checks selected structural and reference invariants but does not implement a complete JSON Schema engine. Documentation checks do not establish verified accessibility or implemented component quality.


## Batch 10 — task-based retrieval coverage

At the historical Batch 10 snapshot, 40 concepts were canonical (the current registry contains 49); retrieval metadata now maps user task phrases such as `hosted authentication`, `human approval workflow`, `feature flags`, `data migration`, `clickable row`, `dialog focus return` and `global CSS` to their owning pages. This is alias and `use_when` enrichment, not concept creation or promotion. See [Batch 10 evidence ledger](../archive/planning/little-wins-batch-10-context-and-gap-ledger.md) and [regression tests](../tests/test_little_wins_knowledge_coverage.py). Rank indicates retrieval relevance, not implementation correctness.

## Application architecture task lookup (Batches 13–16)

Use `architecture.application-selection` for profiles and example trees, `architecture.module-boundaries` for feature/domain/shared ownership and developer findability, `architecture.evolution` for migration/fitness, and `architecture.enterprise-multiapp` for monorepo/multirepo/microfrontend selection. These are proposed application-code guidelines rather than a restructuring of the catalog itself. [Batch context and coverage](../archive/planning/application-architecture-batches-13-16-context-and-gaps.md).

## Batch 17 framework-aware architecture lookup

Resolve `architecture.framework-aware` for applying application/feature organization without overriding Next.js App Router, Angular or React Router file conventions. Start with `architecture.application-selection` and `architecture.module-boundaries` for generalized ownership decisions. See [Batch 17 context](../archive/planning/application-architecture-batch-17-context-and-gaps.md).

## Batch 18 architecture-enforcement lookup

Use `architecture.enforcement-ci` for example boundary lint, graph cycle detection, Nx project constraints, exception review and CI rollout. This is distinct from `architecture.module-boundaries`, which owns the application design decisions. [Batch 18 source and gap ledger](../archive/planning/application-architecture-batch-18-context-and-gaps.md).

## Batch 19 applied architecture examples

Use `architecture.reference-examples` for prototype/MVP/enterprise developer-task-to-file walkthroughs and before/after modularity decisions. Selection and module contracts remain canonical in `architecture.application-selection` and `architecture.module-boundaries`. [Batch 19 context](../archive/planning/application-architecture-batch-19-context-and-gaps.md).

## Batch 20 — architecture coverage and selection

The [architecture index](../architecture/README.md) is the human task-first entrypoint to the seven application architecture concepts introduced in Batches 13–19. The [closure audit](../archive/planning/application-architecture-batch-20-closure-audit.md) documents canonical ownership, lookup coverage, historical context and unverified application outcomes. Prefer existing IDs over creating redundant concept entries.

## Account/settings portal retrieval

Start with `pattern.account-settings-portal` for settings IA, profile management, contact verification and save state. Use `pattern.billing-subscription-settings` for plans, payment and invoices. For credentials use `pattern.authentication-lifecycle`; for privacy rights `guidance.privacy-trust`; for alerts `pattern.notifications-attention`; for user language `guidance.internationalization`; for appearance `foundation.design-tokens`; for authorization `pattern.role-aware-workspaces`. See [three-batch audit ledger](../archive/planning/account-settings-batch-progress.md). All entries are proposed; no live account portal or payment system is asserted.

## Wireframe methodology (proposed, PR #11)

Use `guidance.wireframe-methodology` for low/mid/high visual fidelity, static-image limitations and when to escalate to an interactive prototype. Continue to use `pattern.task-flows` for task composition, `pattern.interaction-recovery` for states, and `governance.quality` for verification. The registry status is **proposed**, not implemented or reviewed.

## Task-to-screen composition (proposed B2)

Use `pattern.task-flows` for minimum design context, screen sequence, action continuity, structurally meaningful alternatives and comparison criteria; use `principle.visual-hierarchy` for within-screen action priority. `guidance.wireframe-methodology` remains the owner of fidelity and escalation. All remain proposed and require verification for real products.

## Static state coverage (proposed wireframe B3)

Use `pattern.interaction-recovery` for `wireframe state coverage`, `static wireframe state matrix`, and `state annotation handoff`. Its canonical page owns the state inventory and screenshot/annotation evidence boundary. It does not establish functioning permission checks or real recovery behavior; follow `guidance.wireframe-methodology` for prototype escalation.

## Responsive and inclusive wireframe lookup (proposed B4)

`guidance.mobile-adaptive` owns responsive wireframe composition and viewport matrix queries; `guidance.accessibility` owns inclusive static design review and annotated zoom/focus expectations; `guidance.internationalization` owns long-text, RTL and bidi wireframe stress review. These extend existing proposed IDs and do not certify responsive behavior or WCAG conformance.
