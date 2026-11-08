# Field and error

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

Compose a persistent label, description, control slot and contextual validation feedback as one understandable form field. **Use** across Input, Select, Checkbox groups and other labeled controls. **Avoid** baking domain validation rules or submit requests into the wrapper.

## Ownership and contract

Field owns association of label, help, required indication, error identification and layout. The child control owns input semantics and value. The feature owns whether a value is valid, when validation occurs, and what the corrective copy says. Illustrative API: `controlId`, `label`, `hint`, `required`, `error` with stable message ID, and a control slot receiving description/error associations.

| State | Behavior | Verification |
| --- | --- | --- |
| Default | Label remains visible; help is available | Click label, accessible name |
| Required | Requirement conveyed via words/semantics, not color alone | Screen reader |
| Invalid | Actionable message linked to the control | `aria-describedby`/error linkage as appropriate |
| Corrected | Error updates without stale references | Focus and announcement behavior |
| Disabled or readonly | Meaning explained consistently with child control | Keyboard and content review |

**Invalid combinations:** Multiple controls with a duplicated label ID; error text shown only in red; a visually hidden label without an accessible equivalent; an inaccessible tooltip as the sole explanation.

## Tokens, responsiveness and localization

Use semantic text/muted/error/spacing/focus tokens. Layout uses logical properties, wraps long help messages, supports translated validation and remains usable in narrow and zoomed containers. Error summaries for whole forms belong to composed patterns, but should link to individual field errors.

## Example and anti-example

**Illustrative:** A labeled email field shows a linked message, "Enter a valid email address," and preserves input for correction. **Anti-example:** A generic red banner lists errors without naming controls or allowing navigation to them.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Contract/association review | NOT VERIFIED | Owner unassigned |
| Label/help/error semantics and keyboard | NOT VERIFIED | Requires running implementation |
| Translation, reflow and contrast | NOT VERIFIED | Consumer tests required |
| Error lifecycle and focus recovery | NOT VERIFIED | Feature tests required |

**Canonical ID:** `component.field` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** consolidate repeated label/help/error wrappers without centralizing validation business rules. Proposed documentation only.

Related: [Input](../input/spec.md), [Select](../select/spec.md), [Checkbox](../checkbox/spec.md), [accessibility](../../guidance/accessibility.md), [interaction recovery](../../patterns/interaction-states-and-recovery.md). Reference: [WCAG 2.2](../../governance/references.md).

## Phase 5 executable reference (2026-11-08; verification scope)

An actual [Field reference implementation](../../site/src/implementations/components/field/Field.js), its [synthetic scenario manifest](../../site/src/implementations/components/field/scenarios.js), and token-aware [preview styles](../../site/src/implementations/components/field/Field.css) now exist in the embedded visual catalog. The catalog renders the checked-in reference source and exposes the same source for inspection. This **does not** promote the specification out of `proposed` or establish production adoption, WCAG conformance, real persistence or business validation. The earlier evidence table records the historical documentation-only state; keyboard/AT, real-browser behavior, long-content and visual performance still require observed review. See [Phase 5 gate](../../docs/visual-catalog-refactor/11-phase-5-core-controls.md).
