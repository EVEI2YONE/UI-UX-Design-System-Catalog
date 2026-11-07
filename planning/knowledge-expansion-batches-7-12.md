# Proposed UI/UX knowledge expansion — Batches 7–12

**Status:** Rolling plan; Batches 7–10 have proposed documentation committed to cumulative PR #5. No human or production verification is implied.  
**Base:** `main` (the branch was created from `main`).  
**Scope:** Reusable design knowledge in this catalog, not target application code.  
**Existing work:** Batches 1–6 are documented in the root README and remain unchanged.

## Principles for every batch

1. Search `catalog/index.json`, aliases, canonical pages, and nested README files **before** declaring a gap. Reuse, extend, consolidate, or create only with a documented reason.
2. Keep additions specific and testable: user task, when to use/avoid, decision rules, tradeoffs, positive/negative examples, accessibility, localization/RTL, theme/responsive concerns, performance, and verification.
3. Cite authoritative external references with source date/edition, scope, known limitations, and review owner. Distinguish normative platform rules from empirical UX hypotheses.
4. Follow `CONTRIBUTING.md`: update canonical concept pages, catalog registry, relevant README indexes, changelog and lookup examples/tests. Keep status `proposed` until reviewed.
5. Validate `python3 scripts/validate_catalog.py` and any relevant lookup/regression tests; record actual results. Do not claim real-user testing or WCAG compliance from documentation checks.
6. Keep each batch reviewable as a distinct commit group and context ledger **within cumulative draft PR #5**. Continue the existing branch, validate before review, and never merge or modify `main` without approval.

## Batch overview

| Batch | Theme | Candidate topics | Initial disposition | Gate |
| --- | --- | --- | --- | --- |
| **7** | Research and product understanding | UX research methodology; mental models and journey mapping; behavioral psychology/cognitive load | New guidance or extend UX measurement/task-flow concepts after search | Research plan and sample journey/test artifacts with explicit evidence limits |
| **8** | Content, discovery and task completion | Content design/UX writing; complex forms/data entry; search/filter/sort/discovery; customer-support/service recovery | Extend existing forms, search and recovery patterns **before** creating new entries | Complete states, error copy, no-results flow and keyboard/RTL checks |
| **9** | Trust and resilient journeys | Privacy/trust/ethical UX; authentication/account lifecycle; notifications/attention; offline-first/sync/conflict recovery | Reuse interaction-state and accessibility guidance; add only missing cross-cutting rules | Consent/non-deceptive UX checks, account recovery and failure-path walkthroughs |
| **10** | Dense and platform-specific interfaces | Data visualization/dashboards; mobile/native UX; advanced interactions; enterprise/role-based workflows | Extend existing data tables, role-aware workspace and component-contract entries | Data table/chart accessibility, keyboard/mobile equivalents, permissions |
| **11** | AI and multimodal experiences | AI-powered and agentic UX; multimodal/voice/conversational interfaces | Dedicated guidance only after checking existing guidance/roles | Disclosure, uncertainty, control/approval, reversal, safe failure and accessibility |
| **12** | Evaluation, performance and delivery | Operational/perceived performance UX; experimentation/A/B testing; DesignOps/design-to-code handoff | Expand metrics, quality gates and governance before introducing new structures | Core Web Vitals definitions, experiment guardrails, visual regression and release evidence |

## Detailed scope and expected outputs

### Batch 7 — Research and product understanding
- Methods selection: discovery vs evaluative research, interviews, contextual inquiry, usability tests, diary studies and surveys.
- Evidence quality: recruitment, sampling, bias, participant safety, triangulation and clear observed/inferred labels.
- Task analysis, mental models, jobs-to-be-done, journey maps and service blueprints, with examples.
- Cognitive load and decision-complexity heuristics; avoid treating named UX laws as universal deterministic rules.
- **Deliverable:** one or more canonical research/guidance pages with an example research plan, study checklist and findings-to-design-decision trace.

### Batch 8 — Content, discovery and task completion
- Content strategy: terminology, plain language, labels, microcopy, error/help text, tone, readability and localization.
- Form patterns: validation timing, required/optional conventions, multi-step progress, autosave/resume, autofill, corrections and partial submissions.
- Search/discovery: query entry, results relevance, filters, sorting, empty/zero-result states, pagination and accessibility.
- Help/service recovery: contextual guidance, escalation, support status, complaint and failed-workflow recovery.
- **Deliverable:** extend existing `patterns/forms*`, search/filtering and interaction-recovery concepts where available; add reusable content guidance only when absent.

### Batch 9 — Trust and resilient journeys
- Transparent consent, data minimization, permission prompts, deletion, dark-pattern avoidance and trustworthy defaults.
- Authentication: sign-in, passkeys, MFA, account recovery, session expiry and high-risk action confirmation; refer to security authorities rather than making unverified security claims.
- Notifications: urgency, preference control, frequency, interruption and accessibility.
- Offline/async resilience: retries, optimistic updates, pending vs saved, sync conflicts and preservation of user work.
- **Deliverable:** reusable decision rules and critical-path state/recovery matrices.

### Batch 10 — Dense and platform-specific interfaces
- Dashboards and visualization: chart choice, axes, legends, text alternatives, tables, color and cognitive load.
- Mobile/native: platform conventions, touch gestures and alternatives, safe areas, deep links and adaptive layouts.
- Advanced interactions: bulk operations, drag/drop alternatives, shortcuts, menus, command palettes, undo/redo.
- Enterprise: permissions, multi-role workspaces, approvals, audit trails and dense operations.
- **Deliverable:** extend `patterns/data-tables*` and `patterns/role-aware-workspaces-and-context-switching.md` when appropriate, not duplicates.

### Batch 11 — AI and multimodal experiences
- AI expectations, disclosure, provenance, uncertainty and fallback.
- Agent autonomy: preview plans, scoped permissions, user confirmation for consequential changes, observability, interrupts and reversal.
- Feedback, correction, escalation and failure recovery.
- Voice/conversation: turn-taking, transcript and non-audio equivalents, multimodal continuity and privacy controls.
- **Deliverable:** AI/agentic interaction guidance with examples and a risk/approval ladder.

### Batch 12 — Evaluation, performance and delivery
- Operational UX: loading strategies, latency budgets, Core Web Vitals, network/device constraints and progressive enhancement.
- Experimentation: hypothesis, unit of randomization, segmentation, guardrails, sample considerations and avoiding false causal claims.
- Design-to-code/DesignOps: design-token interchange, specs, review gates, screenshot/visual regression, ownership and adoption.
- **Deliverable:** strengthen existing `guidance/ux-measurement.md`, governance checks and compatible architecture pages.

## Reference research queue (verify freshness while implementing)

- Nielsen Norman Group: https://www.nngroup.com/articles/
- GOV.UK Design System: https://design-system.service.gov.uk/patterns/
- U.S. Web Design System: https://designsystem.digital.gov/
- W3C WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C Internationalization: https://www.w3.org/International/
- web.dev Core Web Vitals: https://web.dev/articles/vitals
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Google People + AI: https://pair.withgoogle.com/
- OWASP: https://owasp.org/

## Acceptance checklist per batch

- [ ] Existing entries and synonyms searched; each candidate marked missing/incomplete/stale/undiscoverable/already covered/out-of-scope.
- [ ] Reuse/adapt/create decision and owner documented.
- [ ] Source-backed examples, anti-examples, and actionable acceptance tests written.
- [ ] Registry, root/nested README navigation, related concepts and changelog updated if needed.
- [ ] Documentation/lookup validation actually run and outputs recorded.
- [ ] Accessibility, i18n/RTL, responsive/theme and performance applicability reviewed.
- [ ] Batch included as a separately reviewable commit group on cumulative PR #5; no default-branch push and no unapproved merge.

## Suggested implementation order

**Batch 7 → Batch 8 → Batch 9 → Batch 10 → Batch 11 → Batch 12**, but elevate Batch 11 if AI/agent products are near-term targets. Batches 8 and 9 may proceed in parallel after the inventory; Batch 12 measurement rules can be applied as cross-cutting acceptance checks from the outset.

**Out of scope:** production component code, published status promotions, actual user tests, and claims that candidates are all verified missing in a target application. Catalog guidance is added batch-by-batch to PR #5.
