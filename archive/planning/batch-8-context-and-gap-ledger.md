# Batch 8 — context-first knowledge gap ledger

**Date:** 2026-11-07  
**Catalog:** `EVEI2YONE/UI-UX-Design-System-Catalog`  
**Baseline:** default branch `main`, 23 registered concepts when this independent batch started.  
**Status:** Proposed documentation, pending human review and full repository validation.  
**Integration:** Batch 8 is included in the cumulative Batch 7–12 draft PR #5 through a merge commit preserving both batches' histories. Recheck against `main` before final merge.

## Initial catalog inventory and gap disposition

| ID | Topic | Existing canonical evidence on main | Classification | Decision and proposed result |
| --- | --- | --- | --- | --- |
| KG-8-01 | Content design / UX writing | `guidance/internationalization.md`, `foundations/design-principles.md` mention copy, semantics and labels but not content strategy or microcopy lifecycle | Incomplete / missing dedicated guidance | **Create** `guidance.content-design` with task language, content state matrix, maintenance, acceptance |
| KG-8-02 | Complex forms | `pattern.forms`, `component.field`, `pattern.interaction-recovery` already cover composition and general errors | Incomplete depth, **not absent** | **Extend** `pattern.forms` for validation timing, multifield summaries, save/resume, autofill, review and failure |
| KG-8-03 | Search/discovery | `pattern.search-filter`, `pattern.data-tables`, task-flow guidance already cover basic query and filters | Incomplete depth, **not absent** | **Extend** `pattern.search-filter` for query mode, facets, sorting, pagination, result context and accessibility |
| KG-8-04 | Cross-channel service recovery | `pattern.interaction-recovery` and `pattern.feedback` address UI state, but not support handoff/case status or returning from another channel | Missing reusable cross-channel boundary | **Create** `pattern.service-recovery`; reuse existing error mechanics by reference |

This matrix is a **catalog knowledge audit**, not evidence of defects in a particular application.

## External context and limitations

- [GOV.UK content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/) and [clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/): help shape task-led copy; public-service context may not match commercial apps.
- [GOV.UK error summary](https://design-system.service.gov.uk/components/error-summary/) and [validation](https://design-system.service.gov.uk/patterns/validation/): accessible field recovery and input retention; specific GOV.UK component rules should not be imposed universally.
- [W3C WAI form instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) and [validation](https://www.w3.org/WAI/tutorials/forms/validation/): first-party accessible input principles; implementation checks still required.
- [USWDS search](https://designsystem.digital.gov/components/search/) and [pagination](https://designsystem.digital.gov/components/pagination/), [DWP filter design notes](https://design-system.dwp.gov.uk/contribute/filters/design-notes): useful search/filter reference patterns; DWP notes reflect context-specific, evolving research.
- [GOV.UK planned outage](https://design-system.service.gov.uk/patterns/service-unavailable-pages/), [unexpected problem](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/) and [support operations](https://www.gov.uk/service-manual/helping-people-to-use-your-service/set-up-and-manage-user-support): support state and handoff; actual support channels must be verified by each product.

**External research accessed 2026-11-07.** Source content supports design options and review questions; it does not prove this catalog or any target UI is accessible or successful.

## Ownership and implementation boundary

- Existing canonical IDs are preserved: `pattern.forms`, `pattern.search-filter`, `pattern.interaction-recovery`, `component.field`.
- Added IDs: `guidance.content-design`, `pattern.service-recovery`; owner `unassigned`, reviewed_at `null`, status `proposed`.
- No framework, runtime code, backend, support system, users or metrics are invented.
- No default-branch edits, production implementation or merge is in scope.

## Required gates

- [x] Inspect current catalog canonical references and alias index before drafting.
- [x] Gather external research and record applicability and limits.
- [x] Reuse/extend canonical forms/search rather than duplicate them.
- [x] Update guide entries, root/nested readmes, registry, agent paths, changelog and references.
- [ ] Run `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` in an environment with repository access.
- [ ] Perform manual screen reader, keyboard, zoom, locale/RTL and real user research on actual implementing products (not testable by a docs-only catalog change).
- [ ] Obtain human owner and evidence approval before status promotion.

PR review should confirm all internal links, lookup relevance and compatibility with other batches in cumulative PR #5.
