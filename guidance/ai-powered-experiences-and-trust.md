# AI-powered experiences, transparency and calibrated trust

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose and boundaries

Help people understand what an AI feature can and cannot do, judge its results appropriately, correct mistakes, and remain in control. **Use when** a product generates, classifies, summarizes, recommends, searches with AI, or provides predictive output. **Avoid when** using a model's confident tone, a decorative AI badge, or unverifiable numeric confidence as evidence of correctness.

This entry owns **AI-specific expectation setting, uncertainty, output provenance and correction**. [Content design](content-design-and-ux-writing.md) owns general wording, [privacy and trust](privacy-consent-and-trust.md) owns personal-data choices, [interaction recovery](../patterns/interaction-states-and-recovery.md) owns generic failures, and [agentic actions](../patterns/agentic-actions-and-approvals.md) owns tool-use side effects and approval.

## Expectations, evidence and output contract

| Decision | Explain or provide | Failure to avoid |
| --- | --- | --- |
| Entry / onboarding | Specific task benefit, AI involvement, known limitations, user control and fallback | “Intelligent” or “always correct” without task meaning |
| Data use | What content/context is available to the feature, retention/permission choice where applicable | Suggesting a model has access to a file or site when it does not |
| Generated answer | Distinguish generated synthesis, retrieved source material and user-provided data | Fabricated citations or claims of browsing/verification |
| Uncertainty | State meaningful unknowns or conflicting evidence and ways to verify | Invented calibrated percentages and misleading certainty |
| Recommendation | Present scope, key supporting factors, alternatives and material consequences | Opaque “best” labels for consequential decisions |
| Correction | Permit edit, reject, rerun, report error or switch to a reliable manual path | Forced acceptance of generated content |
| Changing behavior | Explain substantial feature/model changes where they alter expectations | Quietly changing what a previously familiar action does |
| Sensitive use | Stronger human review, product-policy restrictions and escalation | Using generic AI text as sole authority for high-stakes action |

**No blanket confidence score.** A numeric percentage belongs in the interface only if its meaning, calibration on relevant cases, denominator, uncertainty and user comprehension are validated; it must not be invented from the wording of a model response. A statement such as “Sources disagree; review the linked records” may be more useful.

### Evidence and provenance

When claims depend on external data, distinguish source availability from the model's own assertions. Link to real, authorized sources where possible and name freshness or retrieval limits. A source link does not itself validate the user's interpretation. Do not fabricate internal model reasoning or imply that a post-hoc explanation is necessarily the actual decision mechanism. For generated changes, show a reviewable difference or source-to-output comparison when appropriate.

## Lifecycle and states

```text
Discover capability -> choose scope/data -> generate or retrieve
  -> pending / partially streamed / failed / uncertain / complete
  -> inspect evidence and limitations -> accept, edit, reject or retry
  -> confirm saved user outcome -> feedback and correction
```

Treat streaming text as **provisional** until the system reaches a confirmed finish state. A polished answer is not proof that a tool call succeeded. For failed retrieval or unavailable sources, explain what was **not** checked and offer a path to continue without invented evidence.

### Illustrative example

A person requests a summary of uploaded project notes. The experience discloses that the result is AI-generated, identifies **which notes were actually available**, links to relevant original excerpts when supported, flags ambiguous action owners, and lets the person correct the proposed action list before exporting.

**Anti-example:** The product displays “Verified by AI — 99% accurate,” invents links to nonexistent documents, and silently submits recommendations to teammates.

## Accessibility, localization and evaluation

- Keep AI disclosure, source links, correction and any manual alternative perceivable to keyboard and screen-reader users; avoid hover-only citations or status badges relying on color.
- Preserve focus while streaming. Avoid announcing every token via live regions; provide manageable completion summaries and accessible references.
- Validate long multilingual answers, locale-specific examples, translated labels, mixed LTR/RTL citations, large text and narrow screens. Do not assume a model supports every language/locale equally.
- Test interruptions and regenerate/correct flows without unexpectedly discarding the user's input; honor reduced motion and sensible progress feedback.
- Research whether real users can **identify uncertainty**, **distinguish source from synthesis**, **reject an incorrect answer**, and **continue manually**. Record subgroup/task limitations, not just aggregate preference.

| Check | Status | Evidence needed |
| --- | --- | --- |
| Capability and limitation comprehension | NOT VERIFIED | Task study for target use cases |
| Source provenance and truthful data access | NOT VERIFIED | Retrieval and cited-output test fixtures |
| Uncertainty calibration and false-confidence risks | NOT VERIFIED | Domain-specific model evaluation + user comprehension |
| Correction, opt-out and manual alternative | NOT VERIFIED | End-to-end flow tests |
| Accessibility, locale and privacy | NOT VERIFIED | Screen reader/keyboard/RTL plus data-owner review |

## Sources and limitations

- [Google People + AI Guidebook: Explainability + Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) (consulted 2026-11-07): professional guidance about calibrated trust, explanations and confidence; not a universal normative standard or validated score threshold.
- [Google People + AI Guidebook: Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/) (consulted 2026-11-07): user correction and feedback mechanisms; requires task-level testing.
- [Microsoft Research: Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/group/customer-insights-research/articles/guidelines-for-human-ai-interaction-eighteen-best-practices-for-human-centered-ai-design/) (published 2019): 18 design guidelines and CHI-era empirical evaluation; not a blanket endorsement of current generative models.
- [NIST AI 600-1, Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (published 2024-07-26): voluntary risk management considerations; not product certification.

**Canonical ID:** `guidance.ai-experiences` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [privacy and trust](privacy-consent-and-trust.md), [content design](content-design-and-ux-writing.md), [research methods](ux-research-methods.md), [agentic actions](../patterns/agentic-actions-and-approvals.md), [multimodal conversations](../patterns/conversational-voice-and-multimodal-ux.md).
