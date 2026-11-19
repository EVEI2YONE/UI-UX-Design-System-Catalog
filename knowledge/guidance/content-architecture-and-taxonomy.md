# Content architecture, taxonomy and findability

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundary

Design the structure of content types, naming, metadata, classification, relationships and retrieval paths. Complement interface navigation and UX writing without owning their presentation.

**Use when:** A product has many content types or reusable records, conflicting labels, filters, categories, tags or search results.

**Avoid when:** The task is solely rewriting a sentence or changing a one-page heading; use Content Design or Task Flows.

**Accountability:** Content/IA owners define taxonomies and content models; feature teams implement browsing; governance maintains vocabulary and migration decisions.

## Decision rules and tradeoffs

- Inventory real user questions and nouns before modeling content; avoid department structures as the sole navigation model.
- Define canonical entities, required/optional metadata, relationships, status, lifecycle and permission-aware visibility.
- Choose controlled categories versus user-defined tags deliberately; manage synonyms, ambiguity and renamed categories.
- Make findability work across navigation, search, filtering and links; define empty and ambiguous result handling.
- Preserve redirects and stable identifiers through taxonomy change and evaluate actual findability rather than directory neatness.

## Decision matrix

| Context | Question | Decision support |
| --- | --- | --- |
| Categorization | Can an item belong in multiple areas? | Single/multi-taxonomy rules and explanation |
| Label ambiguity | Can readers distinguish neighboring concepts? | Canonical names, synonyms and disambiguation |
| Metadata | Which fields support filtering and recognition? | Source, permissions, quality and optionality |
| Evolution | How are renamed categories handled? | Versioned migration and redirects |

## Example and anti-example

**Illustrative example:** A support knowledge base groups help articles by user task and device, supports legacy-term aliases and offers related-content links.

**Anti-example:** Each team creates its own 'Getting started' category so navigation and search give contradictory answers.

## Creatable multi-select classifications: reuse, create and persist

Choose the **domain relationship** before choosing chips. A selected chip expresses membership in a resource, not ownership of the category definition. Do not substitute labels for stable identities or silently create reusable categories while a user is only typing a search.

| User need | Prefer | Avoid / tradeoff |
| --- | --- | --- |
| One fixed value | Native select or radio group | No creatable multi-select unless genuinely multi-valued |
| Several controlled values, short list | Checkbox group or multi-select listbox | Chips and search add unnecessary complexity for a small stable set |
| Several reusable values, long searchable library | Searchable multi-select with removable selected tokens | Keep results and selected state distinct; keyboard and AT testing are essential |
| Allow users to create reusable values | Explicit "Create [label]" action followed by verified selection | Never create solely on blur or treat an unconfirmed string as a persistent ID |
| Unrestricted personal terms | Free-form tags with explicit ownership/visibility policy | Do not silently promote user-generated labels to a global vocabulary |

**Identity and scope:** Represent a definition as `{category_id, scope_id, canonical_label, status, aliases}`; represent membership as `{resource_id, category_id}`. This is conceptual notation, not a mandated API. Labels are display text, may be renamed/translated and are not unique identifiers. Define scope-specific uniqueness/collation, alias and capitalization policy in the domain service. The feature controls permission to create/edit definitions and associations; the selection UI displays pending/confirmed membership, not the authorization boundary. If the interface includes an "All categories" filter, make it an explicit *filter mode*, not a category ID; specify whether selected categories combine by ANY or ALL, and whether none means unfiltered or empty results.

| State | User-facing behavior | Persistence / recovery |
| --- | --- | --- |
| Query / no match | Suggestions update without changing selected membership; empty results explain create eligibility | No definition created by search |
| Highlight result | Distinguish active suggestion from committed membership | Enter/activation selects only that stable ID |
| Token selected / removed | Expose a named remove action per token; move focus predictably after removal | Deselect association only; do not delete reusable definition |
| Create pending | Display submitted label and pending state; prevent duplicate request on repeated activation | Resolve a verified ID or report unknown result; deduplicate safely |
| Duplicate / alias / renamed | Explain existing match and offer reuse; display latest permitted name | Preserve canonical ID and historical membership |
| Archived / unavailable choice | Show why it cannot be added; preserve historical membership when policy permits | Do not silently delete reference; prevent unauthorized new association |
| Invalid / max count / network unknown | Keep query, selected tokens and error instructions together | Reconcile definitive ID/membership before retry; retain draft |

**Illustrative path:** A team selects two existing labels, explicitly creates a third, waits for confirmed category identity, then saves the resource-to-category memberships. Later a label is archived: its historical association remains explainable but cannot be newly assigned without permission. **Anti-example:** Use displayed label as the database key; deleting a chip deletes the global category and alters all records.

**Accessible composition and acceptance (NOT VERIFIED):** Use [Combobox](../../specifications/components/combobox/spec.md) for searchable single-value suggestion focus, [Listbox](../../specifications/components/listbox/spec.md) or checkboxes for multiselection where appropriate, [Field](../../specifications/components/field/spec.md) for labeled errors, [Button](../../specifications/components/button/spec.md) for explicit Create/Remove, and [Forms](../../specifications/patterns/forms.md) for submission. Do **not** infer a multi-select combobox role from the single-select APG Combobox example. Test typing and IME, Arrow/Escape/Enter, selected-option announcement, token removal by keyboard, screen-reader label, touch targets, 320px/200% zoom, long translations and RTL; assert no phantom creation or relation deletion. Source interpretation: [WAI-ARIA APG Combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) describes combobox popup interactions; [APG Listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) describes single/multiple selection and explicitly cautions against interactive descendants in options; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs applicable accessible operations. The composed domain flow is proposed guidance, not a tested APG widget or a certified implementation.

## Inclusive operation and verification

Use meaningful headings, accessible descriptions, appropriate focus, recovery and language. Review translated content, RTL, zoom/reflow, high contrast, touch and reduced motion where relevant. No mockup alone proves accessible behavior.

| Check | Evidence needed | Status |
| --- | --- | --- |
| Can representative readers find content via task labels and search? | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| Are renamed and unavailable items recoverable? | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| Do headings, localized categories and deep links remain accessible? | Observed application or research evidence with scope and limitations | NOT VERIFIED |

This concept is proposed guidance, not a real-user study, implementation, compliance claim or independently approved design standard.

## Source references and related concepts

- [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) — review scope and edition for the consuming context.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — review scope and edition for the consuming context.
- Related canonical sources: [Task flows](../../specifications/patterns/task-flows-and-information-architecture.md), [Content design](content-design-and-ux-writing.md), [UX research](ux-research-methods.md).
- Record a human owner, review date, evidence and known limitations before changing the proposed status.

## Practical decision and validation boundary

**Illustrative decision question:** Run a small label-discovery or tree-test task. State when to apply the guidance, what alternative would better serve a different context and which actual user or developer task would change the decision. Do not infer successful usability, accessibility or business outcomes from a well-worded scenario.

**Acceptance:** Trace applicable claims to current primary/platform sources and specify their limitations; for behavioral claims, record eligible cohort, observation method, expected success/error state, measurement context and review owner. For interactive web surfaces, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs relevant inclusive design checks; the guideline alone does not establish conformance. Any missing applied evidence stays **NOT VERIFIED**.

