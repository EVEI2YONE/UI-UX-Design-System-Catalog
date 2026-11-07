# Internationalization and bidirectional support

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose

Design layouts and messages that survive changes in language, writing system, direction and regional formats.

## Contract

- Externalize interface copy and accessible names into translation resources; avoid concatenated translated sentence fragments.
- Use contextual ICU-like plural/select messages where supported; allow variable reordering and translator context.
- Use locale-appropriate dates, numbers, currency, addresses, sorting and units.
- Handle text expansion, varying glyph metrics and line breaking; avoid fixed heights or essential single-line truncation.
- Prefer CSS logical properties (`margin-inline`, `inset-inline-end`) and direction-aware navigation icons for RTL. Never mirror universally recognizable symbols, logos or numbers by default.
- Verify mixed LTR/RTL text, language announcements, forms, error messages, focus order, calendars, pagination and tooltips.

**Example:** translated message with named placeholders in a flexible form. **Anti-example:** `"Page " + page + " of " + total` in a rigid-width header.

## Verification

At minimum test the default locale, pseudolocalized long labels, locale formatting and an RTL locale if supported. If RTL is out of product scope, label it **not applicable** with rationale, rather than claiming coverage. Related: [accessibility](accessibility.md) and [design principles](../foundations/design-principles.md).