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

## Translation-ready component review

A shared control receives contextually translated labels from its consumer or localization layer. Avoid building a sentence from separately translated fragments. Store message keys with translator context, use locale-aware formatters, and keep the component's public contract independent of English word order.

**Illustrative message contract:**

```text
results.summary = "{count, plural, one {# result} other {# results}}"
pagination.status = "Page {current} of {total}"
```

These are examples of message intent, not a complete message catalog or assurance of grammatical correctness in every locale.

| Case | Expected review |
| --- | --- |
| Longer translation | Labels wrap/reflow without covering actions or truncating essential content |
| RTL page | Logical start/end spacing; direction-aware navigation; stable mixed-direction data |
| Numbers/dates | Formatting follows the active locale; numeric values are not string-concatenated |
| Field validation | Error text and accessibility names are translated together |
| Language change | Language metadata, focus context and announced content remain meaningful |

**Disposition:** explicitly record supported locales, whether RTL is supported, pseudolocalization results and unresolved linguistic review. Testing one RTL sample does not prove support for all scripts. See [component contracts](../architecture/component-contracts.md).


## Settings language and region journeys — account batch 3 (KG-018–019)

A product language selector must list supported names in a recognizable form, preserve the user's task context and switch interface language only when message resources and accessible document language metadata are ready. If a language is unavailable, do not pretend a browser translation is a supported product locale.

Keep **UI language**, **date/number locale**, **timezone**, **billing currency** and **content translation language** separate when their behavior differs; explain account-synced versus device-local choices. A timezone change should preview a meaningful example and re-evaluate upcoming schedule displays while preserving underlying instants. Never change a purchase price/currency silently on a locale change.

| Scenario | Expected test |
| --- | --- |
| Switch language mid-edit | Explicitly preserve or warn about unsaved changes; focus remains meaningful |
| Long/pseudo-localized strings | Settings navigation, inline controls and dialogs reflow |
| RTL locale | Direction-aware routes, mixed-direction identifiers, keyboard and focus |
| Timezone change | DST boundary, locale formatting, activity timestamps and notification schedules |
| Offline/unknown save | Preserve accurate effective-vs-pending language choice |

**Status:** product checks NOT VERIFIED. Related: [account settings](../patterns/account-and-settings-portal.md), [notification preferences](../patterns/notifications-and-attention.md), [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) (consulted 2026-11-07).
