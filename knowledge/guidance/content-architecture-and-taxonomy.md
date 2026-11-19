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
