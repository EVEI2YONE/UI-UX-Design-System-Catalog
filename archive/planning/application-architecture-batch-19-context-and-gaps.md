# Batch 19 — practical architecture reference examples: context and gap ledger

**Date:** 2026-11-07 · **PR:** #8 (draft) · **Prior head:** `6225114fb5c01f8ed241c5062f4b359c5ec75ebc` · **Scope:** documentation and illustrative examples only.

## Context gathered at the start of Batch 19

| Existing canonical source | Coverage already available | Specific unresolved gap |
| --- | --- | --- |
| `architecture/application-architecture.md` (Batch 13) | Prototype/MVP/modular/multi-app trees and selection | Standalone structures without connected developer tasks |
| `architecture/module-boundaries-and-developer-navigation.md` (Batch 14) | Feature/domain/shared imports and discoverability | No task-to-file reference covering several stages |
| `architecture/architecture-evolution.md` (Batch 15) | One-slice migration protocol | No concrete duplicated-form before/after illustration |
| `architecture/enterprise-and-multiapp.md` (Batch 16) | Topology, package ownership and integration concerns | No shared-contract vs app-specific workflow walkthrough |
| `architecture/framework-aware-application-structure.md` (Batch 17) | Route convention mapping | Examples should not supersede required route conventions |
| `architecture/architecture-enforcement-and-ci.md` (Batch 18) | Lint graph/Nx configurations and caveats | Needs concrete violations tied to developer tasks |
| `templates/concept-entry.md` | Example vs tested implementation evidence distinctions | New examples must remain explicitly proposed and non-runnable |

**Finding KG-13 — incomplete connected examples:** Existing files contain useful fragments but not a cohesive, stage-spanning walkthrough connecting a user task, an owner, a source tree, an import contract, a migration and a test plan. Add one dedicated example concept, not another parallel policy or generated application scaffold.

## Decisions

- Use three small TypeScript/React-oriented examples: prototype, MVP-to-modular project editor, multi-app enterprise. Keep the example placement illustrative and defer actual route conventions to the installed framework.
- Demonstrate **where files live**, representative **allowed and forbidden imports**, real **reuse decisions** and a **vertical-slice migration**.
- Keep module ownership and topology principles canonical in Batches 13–18; avoid duplicating those chapters.
- Do not add a production UI package, a build tool, or synthetic performance claims to this documentation-only catalog.
- Preserve user-impact quality: draft saving, permissions, error recovery, focus, translation/reflow and rollout evidence remain required for an actual app.

## Verification scope

Catalog validator, link checks and lookup tests can prove documentation and registry integrity. The TypeScript snippets do not constitute a runnable app and **have not** undergone typechecking, bundling, browser testing, accessibility testing or observed DX measurement. These remain NOT VERIFIED in the implementation worksheet. Entry status remains proposed.

## Related source constraints

The current project/source catalog guidance is the basis for these examples. Next.js, Angular and React Router route layout must be adapted to the *actual version and mode* using [framework-aware guidance](../../architecture/framework-aware-application-structure.md), rather than silently assuming one generic routing tree fits all stacks.
