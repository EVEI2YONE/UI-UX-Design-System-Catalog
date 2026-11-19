# Catalog retrieval and editorial contract

This is a proposed UI/UX guidance knowledge base, not an installed UI package, a web product's security authority, or independently verified user research.

1. **Begin with a user goal.** Resolve `tasks/index.json` or run `python3 scripts/find_concept.py "recover from a failed submission" --json`.
2. **Resolve canonical identity.** `catalog/index.json` owns IDs, aliases, status, relationships and source paths. Do not invent IDs for page-level task shortcuts.
3. **Read the source.** Read only relevant canonical Markdown and follow `related`/`depends_on` IDs. Check `use_when`, `avoid_when`, `owner`, `reviewed_at` and evidence limits.
4. **Separate knowledge from proof.** A proposed guideline is not approved; a reference implementation is not production code; automated checks are not user studies or complete accessibility certification.
5. **Choose reuse first.** If guidance is incomplete, extend the owning concept after inspecting existing sources. New concepts require a distinct reusable decision and updated registry/schema/validation.
6. **Avoid history in knowledge.** Write the current concept, principles, decision rules, anti-patterns, examples and verification. Do not narrate commits, PRs, phases, batch numbers or prior drafting.
7. **Verify changes.** Run the catalog validator, editorial lint, deterministic lookup tests and static-site/interactive checks before submitting an independently reviewable PR. Human approval is required to change a concept's reviewed status or to merge.

## Useful starting points

- [Find by task](tasks/README.md)
- [Concept inventory](catalog/README.md)
- [Navigation and task search shell](catalog/core/README.md)
- [Frontend view shell](site/shell/README.md)
- [Quality and evidence requirements](governance/quality-gates.md)
- [Accessibility](knowledge/guidance/accessibility.md), [localization](knowledge/guidance/internationalization.md), and [design craftsmanship](knowledge/foundations/visual-design-craftsmanship.md)
- [Components](specifications/components/README.md), [patterns](specifications/patterns/README.md), [application architecture](knowledge/architecture/README.md)

Repository-specific operational details are not standalone reusable design guidance; place them next to the relevant tool/script and keep canonical concept pages concept-only.
