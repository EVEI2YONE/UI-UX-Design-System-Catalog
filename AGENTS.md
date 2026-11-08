# Agent lookup protocol

This repository is a **reference catalog of proposed UI/UX knowledge**, not a shipped component package. Begin with [the canonical registry](catalog/index.json), not a recursive read of all Markdown.

1. Search by exact canonical ID or task: `python3 scripts/find_concept.py "loading button" --json`. For aliases, the resolver ranks exact IDs first, then exact aliases, then title/text. Its ranking is a convenience, not a guarantee that a result fits the task.
2. Read the returned `path` and check `status`, `kind`, `owner`, `reviewed_at`, `use_when` and `avoid_when` where present. `proposed` is not approved or implemented.
3. Follow `related` and `depends_on` canonical IDs only as needed. The registry is the **single** source of identity and retrieval metadata; Markdown pages own guidance and examples.
4. Cite the canonical ID and relative path when using guidance. Distinguish catalog rules from evidence about a target application. Do not claim tested accessibility, production code or benchmarked UX without independent proof.
5. Prefer reuse/extension before creating a new concept. If introducing one, update `catalog/index.json`, the relevant section README, sources/verification, and tests.

For visual reference gathering, reference-to-rule translation or selecting between aesthetic directions, retrieve `foundation.visual-craftsmanship` and its Batch 3 decision packet; use `guidance.ux-research` for participant studies and `guidance.wireframe-methodology` for prototype fidelity. Provisional visual preferences are not tested user outcomes.

For high-fidelity or rendered UI visual critique, retrieve `governance.quality` Batch 4 visual craftsmanship review (KG-15/16), then `foundation.visual-craftsmanship` and `foundation.practical-styling` for rationale and remediations. Use the [synthetic visual refinement example bank](foundations/visual-refinement-examples.md) for KG-17; do not treat its fictional before/after descriptions as inspected artifacts.

For end-to-end visual design or KG-18 handoff requests, start with [visual craftsmanship workflow](governance/visual-craftsmanship-workflow.md) and use its stage-to-canonical-ID map. That guide is non-canonical; actual normative ownership remains with registry IDs `foundation.visual-craftsmanship`, `foundation.practical-styling`, `governance.quality`, and platform/accessibility owners. Check implementation and manual evidence before claiming completion.

## Current retrieval guidance

Use the canonical index and exact IDs first, then read task-relevant source pages. For application structure use [architecture navigation](architecture/README.md); for component contracts use [component navigation](components/README.md); for tasks and journeys use [patterns](patterns/README.md); for UX research, accessibility and cross-cutting rules use [guidance](guidance/README.md).

All catalog entries are currently proposed. Do not infer a published component, tested deployment, accessibility certification or approved standard from registry metadata or the documentation validator. Product-specific case studies and historical batch context live in the [archive](archive/README.md); follow the current canonical pages instead of applying historic PR assumptions.

Before contributions, validate the registry and run the Python test suite. Preserve IDs, update links and lookup assertions when renaming/moving files, and record unexecuted manual or product tests as NOT VERIFIED.

## Image-based wireframe consumer lookup (proposed PR #11)

For task-to-screen wireframing, retrieve `guidance.wireframe-methodology` first for fidelity and static-image boundaries, then `pattern.task-flows` and `principle.visual-hierarchy` for composition. Use `pattern.interaction-recovery`, `guidance.mobile-adaptive`, `guidance.accessibility`, `guidance.internationalization` and `governance.quality` only where relevant. See the [cumulative wireframe integration handoff](archive/planning/wireframe-integration-handoff-2026-11-07.md) for B0–B7 disposition and [synthetic cases](archive/planning/wireframe-synthetic-example-bank-2026-11-07.md) for positive/negative retrieval rehearsal. Canonical registry pages, not the handoff, own the design rules. Do not treat static images as working behavior or claim actual product testing from catalog CI.

## Icon-bearing control retrieval (proposed Batch 1)

Search `foundation.icon-semantics` for icon meanings, decorative/informative roles, icon-only button naming, target geometry and RTL. Search `component.button` for button activation and its state contract. Prefer the canonical entry to copying a product-specific Lucide mapping; the catalog specifies meaning and contracts, not a production icon package. No human/component verification was performed by a documentation-only batch.

## Batch 2 — composite interaction lookup

For “component event ownership”, “cross component events”, “nested interactive controls” or “controlled uncontrolled state”, retrieve **existing** canonical ID `architecture.component-contracts`. Use `component.button` and `foundation.icon-semantics` for host activation and icon meaning, respectively; use `pattern.interaction-recovery` for server-outcome uncertainty and focus recovery. B02 does not introduce a second concept ID, global event bus or verified production behavior.

## Batch 3 — action continuation and focus retrieval

Search `pattern.interaction-recovery` for “icon state synchronization”, “post mutation focus”, “focus after item removal” and “pending confirmed icon”. Search `pattern.task-flows` for “sequential task controller”, “next eligible item”, “stable action region” and “pointer travel continuity”. Read `foundation.icon-semantics` for semantic glyph roles and `architecture.component-contracts` for event ownership; neither replaces the workflow's authoritative mutation/reconciliation logic. B03 tests are documentation-level; product UX and accessibility remain NOT VERIFIED.

## Batch 4 — action consolidation and effort retrieval

Resolve `pattern.advanced-interactions` for “action consolidation decision matrix”, “split button safety”, “contextual action toolbar”, “control overloading” or “primary versus overflow actions”. Resolve `guidance.ux-measurement` for “pointer travel distance”, “time to next action”, “keyboard navigation effort” and “interaction cost measurement”. Use B03 `pattern.task-flows` for spatial layout/next-item progression, not to redefine the metric; all UX improvements require actual task evidence.

## Batch 5 — styling and component ownership retrieval

For “utility-first styling ownership” or “tailwind shadcn component styling”, retrieve `foundation.practical-styling`; for “visual redundancy enforcement”, “CSS ownership lint” or “variant explosion lint”, retrieve `architecture.enforcement-ci`; for “component inventory to contract mapping”, “installed versus used components” or “duplicate primitive audit”, retrieve `architecture.component-model`. Retain `foundation.design-tokens` for token definitions and modes. B05 is documentation-only; do not infer actual CI linting or visual QA.

## Batch 6 — final icon and interaction verification retrieval

Resolve `foundation.icon-semantics` for “icon consistency audit” and “icon intent collision review”. Resolve `governance.quality` for “interaction state test matrix”, “icon interaction testing”, “catalog retrieval regression” and the cumulative B01–B06 evidence gate. Use the canonical owners returned by `scripts/find_concept.py`, not repeated guidance from historical batch ledgers. Automated catalog tests cannot prove screen-reader, keyboard, touch, responsive or live network behavior.

## Visual catalog reference lookup (Phase 2 metadata, 2026-11-08)

Continue to resolve `catalog/index.json` by **canonical ID or task query**, then read the Markdown `path` and existing `related`/`depends_on` IDs before relying on a visual example. The optional `capabilities` array contains functional labels for future filters; the current `find_concept.py` ranking is unchanged and does not automatically consider them.

An `implementation` object appears **only when actual reference code and a scenario manifest are committed under `site/src/implementations/`**. When present, inspect the `source_path` and `scenario_manifest`, then use `preview_path` as a human preview link if the site is actually deployed. No field implies a public deployment, server-side authority, production adoption, or tested accessibility. `status=verified` requires a linked evidence record and reviewer interpretation; metadata itself is not proof.

If `implementation` is absent, treat the entry as **specification only** and do not invent a preview URL or code path. The site browser may show a non-interactive fallback, but the canonical knowledge remains independently readable from Markdown/JSON. The site must not contain a second manually curated identity index.

See [Phase 2 registry contract](docs/visual-catalog-refactor/08-phase-2-registry-compatibility.md).
