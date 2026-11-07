# Standards and research references

**Status:** curated starting points (reviewed for this scaffold: 2026-11-07). Standards indicate intended requirements and patterns, **not** verified conformance of this catalog or any application.

| Source | Version/status | Intended use and limits |
| --- | --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | W3C Recommendation | Default applicable web accessibility target; AA is a target, not a claim of passing. |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Maintained security guidance; reviewed 2026-11-07 | Deny by default, least privilege, per-request authorization; not evidence of UI usability. |\n| [AWS IAM role switching](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) | Product documentation; reviewed 2026-11-07 | Illustrative active-role/switch-back precedent, not a universal UX standard. |\n| [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) | W3C WAI practice guidance | Keyboard and semantic patterns for complex widgets; prefer native HTML where appropriate. |
| [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) | W3C guidance | Language metadata, localization, direction and content flexibility. |
| [Design Tokens Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) | Final W3C Community Group report, 2025-10-28 | Vendor-neutral typed design-token interchange. **Not** a W3C standards-track Recommendation. |
| [Design Tokens Community Group FAQ](https://www.designtokens.org/faq/) | Project documentation | Format adoption and status context; verify applicability to toolchain. |

## Internal source lineage

Initial concepts are a selective synthesis of the user-provided **UI/UX Design System Architect v1.1** materials: `02_component_architecture.md`, `03_tokens_themes.md`, `05_ux_interaction.md`, `06_accessibility.md`, `07_internationalization.md`, `08_metrics.md`, `09_quality_gates.md`, `10_catalog_first_knowledge_audit.md`, and associated catalog entry/governance templates. Those materials are not automatically a published design standard, and this scaffold does not include a copy of the agent operating contract.

## Evidence hygiene

New guidance should capture a source URL, edition/date, scope, limitations, last review date and owner. Prefer primary authoritative references for normative claims, and actual user research or telemetry for product outcomes. Label hypotheses as hypotheses. If a source is inaccessible, mark it unverified rather than fabricating a quotation or result.
## Batch 7 research and cognitive-design sources (proposed guidance)

- [Nielsen Norman Group: When to Use Which UX Research Methods](https://www.nngroup.com/articles/which-ux-research-methods/) — research-purpose and method-selection framework; professional guidance, not universal sampling thresholds.
- [GOV.UK Service Manual: User Research](https://www.gov.uk/service-manual/user-research) — research planning, recruitment and inclusive service research; contextualize outside government services.
- [Nielsen Norman Group: Mental Models](https://www.nngroup.com/articles/mental-models/) — explain expectations and conceptual mismatches; do not invent prevalence from examples.
- [Nielsen Norman Group: Journey Mapping](https://www.nngroup.com/articles/journey-mapping-101/) — map scope, stages and evidence; distinguish inferred from researched journeys.
- [W3C COGA: Making Content Usable](https://www.w3.org/TR/coga-usable/) — W3C Working Group Note, non-normative supplemental cognitive accessibility guidance, not WCAG conformance criteria.

Added to the research queue on 2026-11-07; individual source publication dates and applicability must be verified in each knowledge review. Human review is not claimed.
