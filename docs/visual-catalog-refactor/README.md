# Visual Catalog Refactor — documentation pack

**Status:** proposal / awaiting review  
**Source repository:** [UI-UX-Design-System-Catalog](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog)  
**Audited main SHA:** `3b933abea778122dece31af7496f409028ed6198` (2026-11-08)  
**Delivery boundary:** planning documentation only; no website, runtime component, feature, registry migration, or release implemented.

## Executive decision

Keep the existing knowledge catalog as the **canonical source of design guidance and discovery metadata**, and add a **visual website containing actual, isolated, interactive reference implementations**. Do **not** introduce installable UI packages at this stage. Preserve `catalog/index.json` and its stable IDs; avoid a competing website registry. Implement a compact website shell and one vertical slice before expanding to feature-complete examples.

The site is a *reference implementation environment*, not an assurance that a screenshot represents real behavior or that a simulated feature can enforce product authorization.

## Single-PR execution policy

**All future overhaul phases are planned as successive commit groups on draft PR [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16), not separate implementation PRs.** Keep the PR in draft during implementation and use the phase acceptance matrix in [06 — Migration and PR roadmap](06-migration-pr-roadmap.md). There are **11 numbered phases (0–10)** from baseline inventory through release review; only planning documents are implemented now. Do not label later phases complete without runtime evidence, review and tests.

## Reading order and decisions

| Document | Question answered | Output |
| --- | --- | --- |
| [01 — Folder and file blueprint](01-folder-file-blueprint.md) | What goes where, what stays and what changes? | Target tree; move/add/keep matrix; dependency rules |
| [02 — Concepts and coverage expansion](02-concepts-and-content-plan.md) | Which components, patterns and features deserve visual examples? | Existing canonical targets; staged backlog; promotion criteria |
| [03 — Knowledge gap audit](03-knowledge-gap-audit.md) | What is genuinely missing, incomplete or simply not implemented? | Evidence-backed KG ledger, uncertainty, research priority |
| [04 — Registry and agent discovery](04-registry-agent-discovery.md) | How do humans and agents find exactly the same references? | Backwards-compatible metadata extension and search contract |
| [05 — Preview and quality contracts](05-preview-quality-contracts.md) | How does a working example prove its behavior and quality? | Fixture, interaction, performance, readability and a11y contracts |
| [06 — Migration and PR roadmap](06-migration-pr-roadmap.md) | How is the overhaul delivered within this same PR? | Eleven sequential phase gates, deliverables, acceptance and rollback |

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
