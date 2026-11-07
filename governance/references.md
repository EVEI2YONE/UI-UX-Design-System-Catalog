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

## Batch 8: content, forms, discovery and service recovery (review queue, 2026-11-07)

| Source | Applicability and limits |
| --- | --- |
| [GOV.UK content design](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/) | User-needs-first writing and content maintenance; public-service context, adapt to product vocabulary. |
| [GOV.UK clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/) | Descriptive headings and scannability; not a universal content length quota. |
| [GOV.UK validation pattern](https://design-system.service.gov.uk/patterns/validation/) and [error summary](https://design-system.service.gov.uk/components/error-summary/) | Recoverable form errors, input retention, focus and summary links; service-specific implementation guidance, not universal component mandate. |
| [W3C WAI forms instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) and [validation](https://www.w3.org/WAI/tutorials/forms/validation/) | Accessible labels, instructions and validation; live system semantics must still be tested. |
| [USWDS search](https://designsystem.digital.gov/components/search/) and [pagination](https://designsystem.digital.gov/components/pagination/) | Search/pagination component guidance; does not prove application relevance or ranking quality. |
| [DWP filter design notes](https://design-system.dwp.gov.uk/contribute/filters/design-notes) | Emerging research on deliberate vs live filters; context-specific, not universal rule. |
| [GOV.UK service unavailable](https://design-system.service.gov.uk/patterns/service-unavailable-pages/) and [service problems](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/) | Distinguish planned outage from unexpected failure and explain saved data; government service context. |
| [GOV.UK user support operations](https://www.gov.uk/service-manual/helping-people-to-use-your-service/set-up-and-manage-user-support) | Cross-channel support and contact metrics; operational guidance, not evidence of this product's support capability. |

These URLs were inspected as research starting points on 2026-11-07; source editions/changes must be rechecked on future reviews. No live product tests or external content endorsements are claimed.

## Batch 9: trust and resilient journeys (source review 2026-11-07)

| Source | Applicability and limit |
| --- | --- |
| [UK ICO data protection by design/default](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-by-design-and-by-default) | Updated 2026-02-05; UK GDPR-focused, context-specific legal review still required. |
| [FTC, Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) | 2022 staff report on deceptive design; not a universal prescriptive UX standard. |
| [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) | Final July 2025 authentication assurance guidance, particularly relevant to U.S. federal programs; security owner must assess applicability. |
| [W3C Understanding WCAG 2.2 SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) | Explains accessible authentication at Level AA; not proof of any product's conformance. |
| [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Maintained engineering guidance; not human-usability study. |
| [MDN Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) and [Apple web push](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers) | Browser/platform permission, device and service-worker details; implementation and user preference policies differ. |
| [MDN Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API), [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) | Background Sync has limited support; local storage retention and security must be evaluated. |

External pages were checked for research context on 2026-11-07. They do not certify this catalog or a target application.

## Batch 10: charts, mobile/adaptive UX, advanced interactions and enterprise (reviewed 2026-11-07)

| Source | Applicability and limits |
| --- | --- |
| [USWDS Data visualizations](https://designsystem.digital.gov/components/data-visualizations/) | Guidance-only chart accessibility and narrative examples; not a shipped chart library or statistical validation. |
| [Apple HIG Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Updated 2026-09-09; Apple layout, safe areas, Dynamic Type and window adaptation; not universal web/Android guidance. |
| [Android Adapt layouts](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) and [navigation patterns](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns) | Android adaptive layout, window-size and nav patterns; SDK/device review required. |
| [W3C WCAG 2.2 Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements) | Applicable web AA criterion requiring a non-drag single-pointer alternative; keyboard access separately required. |
| [WAI-ARIA APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) | Keyboard semantics for deliberately implemented interactive grids; not ordinary HTML tables. |
| [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Security requirement for server-side authorization and object scope; not user-experience verification. |

All are guidance or standards references, not evidence of an actual tested product. See [Batch 10 context ledger](../archive/planning/batch-10-context-and-gap-ledger.md).

## Batch 11: AI and multimodal experience sources (reviewed 2026-11-07)

| Source | Applicability and limits |
| --- | --- |
| [Google People + AI, Explainability and Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) and [Feedback and Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) | Professional UX principles for calibrated trust, evidence, uncertainty and user controls; not a mandated confidence scoring formula. |
| [Microsoft Research, Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/group/customer-insights-research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/) | Research-based guidelines published 2019; helpful for behavior over time, failure and correction but not current-model certification. |
| [NIST AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Published 2024-07-26; voluntary cross-sector AI risk reference, not an endorsement of this catalog's illustrative approval levels. |
| [OpenAI, Agent guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) and [Agents SDK human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) | Runtime-specific pause/approval/rejection patterns, enforcement and unsafe replay caveats; not automatically present in every agent implementation. |
| [OpenAI, Voice agents](https://developers.openai.com/api/docs/guides/voice-agents) and [Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) | Voice-specific tool and turn-taking considerations; not universal architecture requirements. |
| [MDN SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) | Limited support and possible server-based processing; do not claim offline or device-local recognition on all platforms. |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Web accessibility target; real app evaluation and assistive testing remain necessary. |

**Source interpretation:** normative accessibility criteria, voluntary risk guidance, historical UX research and provider-specific implementation docs have different authority. All are context for proposed knowledge, not tests of an actual product. [Batch 11 ledger](../archive/planning/batch-11-context-and-gap-ledger.md).

## Batch 12: performance, experimentation and design-to-code (research 2026-11-07)

| Source | Applicability and limitations |
| --- | --- |
| [web.dev Web Vitals](https://web.dev/articles/vitals) and [threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds) | Current web good targets: p75 LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 on real visits, segmented by mobile/desktop; not native-device guarantees or proof of task success. |
| [web.dev User-centric performance metrics](https://web.dev/articles/user-centric-performance-metrics), [Optimize INP](https://web.dev/articles/optimize-inp), [Optimize CLS](https://web.dev/articles/optimize-cls) | Field vs lab and responsiveness/shift guidance; product telemetry, baseline and controlled tests are still required. |
| [Microsoft Research diagnosing SRM](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/) and [data quality](https://www.microsoft.com/en-us/research/articles/data-quality-fundamental-building-blocks-for-trustworthy-a-b-testing-analysis/) | Experiment assignment, logging/missingness and sample-ratio mismatch; not a universal power calculator or statistical sign-off. |
| [Microsoft Research: trustworthy A/B analysis](https://www.microsoft.com/en-us/research/publication/trustworthy-analysis-of-online-a-b-tests-pitfalls-challenges-and-solutions/) | 2017 research on randomization and variance assumptions; select statistical methods for actual design. |
| [GOV.UK User research in live](https://www.gov.uk/service-manual/user-research/user-research-in-live) | A/B testing is a complement to usability and qualitative research, not a replacement. |
| [Optimizely statistical methods](https://www.optimizely.com/field-notes/articles/how-to-choose-the-right-stats-engine) | 2026 vendor guidance on fixed-horizon and sequential testing; not independent validation of any product algorithm. |
| [DTCG Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) and [format FAQ](https://www.designtokens.org/faq/) | Stable 2025 Community Group token interchange, not W3C Recommendation or the experimental 2026 preview; converter support must be tested. |
| [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) and [Storybook tests](https://storybook.js.org/docs/writing-tests/index) | Visual snapshot/stories can support review with pinned environment, but do not replace actual keyboard, AT or user-task tests. |

Sources are decision references as of 2026-11-07, not a claim of implementation/tool installation. See [Batch 12 context ledger](../archive/planning/batch-12-context-and-gap-ledger.md).
