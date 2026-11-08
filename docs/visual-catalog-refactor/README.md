# Visual Catalog Refactor — documentation pack

**Status:** Phases 0–9 delivered on draft PR #16; automated acceptance recorded per phase, final human/release approval pending  
**Source repository:** [UI-UX-Design-System-Catalog](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog)  
**Audited main SHA:** `3b933abea778122dece31af7496f409028ed6198` (2026-11-08)  
**Delivery boundary:** the website and 12 interactive references are implemented on the draft PR branch. No public deployment, package release, main-branch merge, real product integration or final reviewer approval is claimed.

## Executive decision

Keep the existing knowledge catalog as the **canonical source of design guidance and discovery metadata**, and add a **visual website containing actual, isolated, interactive reference implementations**. Do **not** introduce installable UI packages at this stage. Preserve `catalog/index.json` and its stable IDs; avoid a competing website registry. Implement a compact website shell and one vertical slice before expanding to feature-complete examples.

The site is a *reference implementation environment*, not an assurance that a screenshot represents real behavior or that a simulated feature can enforce product authorization.

## Single-PR execution policy

**All overhaul phases are successive commit groups on draft PR [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16), not separate implementation PRs.** Keep the PR in draft during implementation and use the phase acceptance matrix in [06 — Migration and PR roadmap](06-migration-pr-roadmap.md). There are **11 numbered phases (0–10)** from baseline inventory through release review. Phases 0–9 contain committed plans, source and automated evidence; Phase 10 final release review is not complete. Do not equate completed automated checks with human visual/AT approval.

## Reading order and decisions

| Document | Question answered | Output |
| --- | --- | --- |
| [01 — Folder and file blueprint](01-folder-file-blueprint.md) | What goes where, what stays and what changes? | Target tree; move/add/keep matrix; dependency rules |
| [02 — Concepts and coverage expansion](02-concepts-and-content-plan.md) | Which components, patterns and features deserve visual examples? | Existing canonical targets; staged backlog; promotion criteria |
| [03 — Knowledge gap audit](03-knowledge-gap-audit.md) | What is genuinely missing, incomplete or simply not implemented? | Evidence-backed KG ledger, uncertainty, research priority |
| [04 — Registry and agent discovery](04-registry-agent-discovery.md) | How do humans and agents find exactly the same references? | Backwards-compatible metadata extension and search contract |
| [05 — Preview and quality contracts](05-preview-quality-contracts.md) | How does a working example prove its behavior and quality? | Fixture, interaction, performance, readability and a11y contracts |
| [06 — Migration and PR roadmap](06-migration-pr-roadmap.md) | How is the overhaul delivered within this same PR? | Eleven sequential phase gates, deliverables, acceptance and rollback |
| [07 — Phase 1 context and decisions](07-phase-1-context-and-decisions.md) | How do existing knowledge concepts map to executable site tiers? | Context audit, source ownership, non-duplication decisions and open questions |
| [08 — Phase 2 metadata compatibility](08-phase-2-registry-compatibility.md) | How do we add source/preview metadata without disrupting search? | Schema changes, validator coverage, test limitations and release gates |
| [09 — Phase 3 site foundation](09-phase-3-site-foundation.md) | How is the website generated from canonical knowledge? | Working static site architecture, CI evidence, visual QA and deployment limitations |
| [10 — Phase 4 preview runtime](10-phase-4-preview-runtime.md) | How do source, scenarios and preview controls stay identical and isolated? | Actual Button reference, safe runner, test and manual QA gates |
| [11 — Phase 5 core controls](11-phase-5-core-controls.md) | How do the remaining five canonical controls become executable references? | Native Input, Field, Select, Checkbox, Dialog demos and CI evidence |
| [12 — Phase 6 composed patterns](12-phase-6-composed-patterns.md) | How are existing interaction patterns represented by real examples? | Forms, navigation, search/filter, tables and safe recovery demos with test gates |
| [13 — Phase 7 Review Workspace](13-phase-7-review-workspace.md) | How is one complete feature implemented with a safe synthetic service boundary? | Canonical feature contract, in-memory adapter, working queue/decision states and CI evidence |
| [14 — Phase 8 quality gates](14-phase-8-quality-gates.md) | What does real Chromium, axe and build-budget CI actually prove? | QA findings, fixed defects, browser artifacts, manual review requirements |
| [15 — Phase 9 agent discovery and governance](15-phase-9-agent-governance-handoff.md) | Can agents and humans find canonical guidance, implementation sources and evidence reliably? | Retrieval acceptance corpus, provenance audit, contributor/agent protocol and Phase 10 handoff |

## Non-negotiable boundaries

- `foundations/`, `architecture/`, `guidance/`, `patterns/`, `governance/`, `components/`, `catalog/`, `templates/`, `scripts/` and `archive/` remain canonical knowledge areas.
- The website **reads** the authoritative registry and Markdown. Site-specific route maps and generated indexes are derived outputs, never rival sources of canonical identity.
- Implementation code lives under `site/src/implementations/`; catalog website chrome lives under `site/src/catalog-ui/`. Keep these separate.
- A feature reference may emulate a service using deterministic synthetic fixtures; it may not claim production security, persistence or business authorization.
- Entries retain original statuses until their owners review evidence. A working preview is not by itself proof of WCAG conformance or production readiness.
- Maintain an agent-compatible static retrieval path: GitHub Markdown, JSON, stable IDs, `AGENTS.md`, and `scripts/find_concept.py`.
- Scope this phase to **documentation and architecture**, not site implementation, public deployment or package publishing.

## Evidence baseline

Repository inspection confirmed `catalog/index.json` with existing `schema_version: 0.1.0`, `catalog/schema.json` with `additionalProperties: false`, six component specifications (Button, Input, Select, Checkbox, Dialog, Field), existing pattern and cross-cutting guidance, `AGENTS.md` retrieval instructions, and `scripts/validate_catalog.py` guidance. The README identifies the repository as a proposal scaffold, not a production component library.

## Source links

- [Canonical registry](../../catalog/index.json), [schema](../../catalog/schema.json), [agent lookup](../../AGENTS.md), [contribution policy](../../CONTRIBUTING.md)
- [Component model](../../architecture/component-model.md), [component specifications](../../components/README.md), [patterns](../../patterns/README.md)
- [Performance guidance](../../guidance/performance-and-perceived-speed.md), [accessibility guidance](../../guidance/accessibility.md), [quality gates](../../governance/quality-gates.md)

**PR status:** This pack is proposed on a feature branch. A pull request, if opened, is not adoption or implementation.
