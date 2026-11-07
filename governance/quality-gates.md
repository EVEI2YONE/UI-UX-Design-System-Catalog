# Design and catalog quality gates

**Kind:** checklist · **Status:** proposed · **Primary layer:** cross-cutting

Use `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` per check and provide evidence, date, owner, and scope. Passing documentation validation **does not** imply component accessibility or user-journey success.

| Gate | Required evidence |
| --- | --- |
| User value | User job, context, success condition and assumptions |
| Reuse | Existing concept search, aliases, reuse/extend/create rationale |
| Architecture | Correct tier, stable API or concept boundaries, owner |
| Interaction | Relevant state matrix, async/error/recovery, focus and touch |
| Design | Hierarchy, signifiers, spacing, primary action and content growth |
| Styling/themes | Token roles, theme variants, scoped styling, responsive behavior |
| Accessibility | Semantic and keyboard expectations; manual and automated test log |
| Localization | Externalized copy, locale formats, translation growth, RTL disposition |
| UX measurement | Defined events, denominators, cohorts, missing baselines and privacy |
| Catalog integrity | Unique ID, canonical path, index/README links, status and version |
| Delivery | Actual validation output, PR review, compatibility and rollback notes |

## Documentation checks

```bash
python3 scripts/validate_catalog.py
```

This checks *document structure and lookup integrity only*. Example manual checks—keyboard, screen reader, reflow, contrast, RTL, light/dark, reduced motion—remain `NOT VERIFIED` until performed on an actual implementation.

## Priority and release decisions

P0 accessibility/safety/privacy/security/data-loss and critical regressions override the normal migration ranking. The user-impact order for product modernization is P1 core workflows, P2 IA/navigation, P3 minimal foundations/components, P4 onboarding/change management, P5 high-friction quick wins, P6 secondary experiences, P7 cosmetic polish. Engineering prerequisites may execute earlier than a higher-value product change. Do not invent usage frequency or test outcomes.

## Per-batch evidence record

For PRs that expand existing scaffold entries, reviewers should see a batch label, canonical paths touched, the design decisions added, known limitations, and check results. A useful definition includes an actionable rule, example/anti-example, a verification method and an identified owner or explicitly unassigned ownership. Avoid promoting entries solely because documentation validation passes.

| Check | Current documentation-only interpretation |
| --- | --- |
| Registry integrity | Existing stable IDs and paths remain unchanged unless intentionally migrated |
| Markdown navigation | Relative links and section/root index references resolve |
| Content completeness | Decisions, counterexamples, scenarios and limitations provided |
| Code a11y / RTL / runtime UX | NOT APPLICABLE to docs-only changes; downstream behavior NOT VERIFIED |
| Research baseline | UNKNOWN unless measured with documented cohort/denominator |

Record actual script output in the PR, and keep code/UX claims distinct from validation of Markdown files.
