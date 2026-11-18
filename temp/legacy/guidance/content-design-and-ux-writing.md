# Content design and UX writing

**Kind:** guideline · **Status:** proposed · **Primary layer:** principles

## Purpose and use boundary

Design interface language and information structure so users can find, understand, decide and complete their tasks. Content design includes what information is necessary, where it appears, its timing and lifecycle—not merely proofreading microcopy. **Use** for navigation labels, instructions, forms, search results, help, status, empty states and consequential decisions. **Avoid** replacing user research with a universal tone-of-voice formula or concealing material consequences to shorten text.

## Decision rules

| Decision | Prefer | Avoid |
| --- | --- | --- |
| Start from a task | Lead with the user goal, next action and decision-critical facts | Internal department labels or a feature inventory |
| Use familiar words | Language people use in research, with consistent terminology | Different names for the same concept or unexplained jargon |
| Build scannable content | Descriptive headings, front-loaded sentences, short focused paragraphs and meaningful lists | Vague titles such as “More information”; heading hierarchy used only for appearance |
| Write actions | Specific verb-and-object labels that predict the outcome | Ambiguous “Submit”, “Go”, “Click here” when context does not clarify |
| Explain requirements | Label input, units, formats, requirements, consequences and data use before needed | Placeholder-only labels and surprise validation rules |
| Support recovery | Say what happened, what remains saved, what to do next and when to seek help | Blame, unsupported reassurance, error codes without guidance |
| Match tone to risk | Clear, respectful, non-promotional language for money, privacy and destructive actions | Humor or urgency that distracts from informed consent |
| Keep content maintained | Content owner, source of truth, review cadence and expired-content disposition | Unowned help articles that contradict the live product |

### Interface copy contract

For every high-impact phrase record **user goal, moment, constraint, proposed copy, information source, translated message key, intended announcement/focus, owner and evidence of comprehension**. Keep component shells responsible for stable semantics; domain owners supply workflow-specific language and policy decisions. A toast or banner should not be the only place to learn an irreversible outcome. When a change affects user trust, compliance, price or data deletion, obtain domain review.

**Illustrative example — destructive action:**
- Action: **Delete saved draft** (not “Continue”).
- Explanation: “This draft will be permanently deleted. Submitted applications are not affected.” *Only use this copy if the system actually behaves that way.*
- Confirmation and cancellation labels must be distinct; never claim an undo path that does not exist.

**Anti-example:** “Something went wrong” disappears after three seconds following a failed payment while leaving users unsure if they were charged.

## Content by state

| State | Minimum information |
| --- | --- |
| First use | Why this task matters, where to begin, expected inputs and optional guidance |
| Empty | What the absence means and an appropriate next step; distinguish no items from no permission |
| Pending | What is in progress, whether users can continue, and any material wait or exit constraints |
| Validation error | Specific correction, connected to its input; whole-form summary when appropriate |
| Service failure | What is known or unknown about saved work, safe retry, alternate route and support |
| Success | Confirm the actual persisted outcome and available follow-up actions |
| Irreversible action | Consequences, scope, alternatives and truthful confirmation behavior |

## Accessibility, localization and content lifecycle

- Use semantic headings and real link text; preserve visible labels so assistive technology users can orient before entering forms.
- Do not rely on icons, color, visual placement, punctuation or emojis to communicate essential meaning.
- Externalize messages with translator context. Support plural/select expressions and locale-specific values; avoid concatenated sentence fragments, English-specific word order and hard-coded left/right.
- Test at narrow/reflowed widths and large text; essential content must not vanish under truncation.
- Distinguish support content from errors and keep it accessible without hovering. Consider language literacy and cognitive load, including genuine alternatives such as examples or steps.
- Inventory content ownership, review triggers and retirement when the related UI or policy changes.

## Acceptance and verification

| Check | Status | Evidence needed |
| --- | --- | --- |
| Task and terminology review | NOT VERIFIED | Representative tasks, terms and comprehension observation |
| Keyboard/screen reader headings and labels | NOT VERIFIED | Actual rendered implementation |
| Locales, RTL, plurals, large text and reflow | NOT VERIFIED | Supported-language matrix |
| Critical policy/trust content | NOT VERIFIED | Product owner/security/legal review as applicable |
| Content maintenance ownership | NOT VERIFIED | Named owner and review trigger |

**Illustrative review task:** Ask eligible users to locate and cancel a pending request. Record whether they can predict the consequences from headings, links, prompts and confirmation text without assistance.

## Sources, applicability and related concepts

- [GOV.UK content design principles](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/) (accessed 2026-11-07): user-needs-first content and ownership, drawn from government service context.
- [GOV.UK clear content structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/) (accessed 2026-11-07): descriptive headings, scannability and link structure; adapt to a product's own information needs.
- [W3C WAI form instructions](https://www.w3.org/WAI/tutorials/forms/instructions/) (accessed 2026-11-07): accessible labels, required information and format instructions.
- [GOV.UK error messages](https://design-system.service.gov.uk/components/error-message/) (accessed 2026-11-07): actionable field errors and preserving input; local implementation guidance is not a universal widget specification.

**Canonical ID:** `guidance.content-design` · **Owner:** unassigned · **Human review date:** null. Guidance proposed 2026-11-07; product tests not performed.  
**Related:** [form composition](../patterns/forms.md), [search/filtering](../patterns/search-and-filter.md), [service recovery](../patterns/service-recovery-and-support.md), [localization](internationalization.md), [accessibility](accessibility.md).
