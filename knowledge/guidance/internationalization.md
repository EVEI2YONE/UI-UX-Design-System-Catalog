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


## Text-expansion and RTL wireframe composition review (proposed Batch 4, 2026-11-07)

**Use when:** static screen concepts contain translated labels, variable data, dates/amounts, long validation instructions or bidirectional navigation. **Avoid when:** an English-only screenshot is treated as proof of localization, exact expansion factors are invented as universal, or every icon/number/logo is mirrored indiscriminately.

For each representative wireframe, specify **content language/locale and direction**, mark displayed copy as `KNOWN` (approved) or `ILLUSTRATIVE` (synthetic), and create additional **stress variants** when supported locales or tasks require them:

- **Extended copy:** replace short headings, buttons and errors with meaning-preserving long test text. Check visually for wrapping, hierarchy preservation, actions/disclosures remaining readable and growth in page length. Synthetic growth is an early screen-design probe, *not* linguistic or runtime verification.
- **RTL and mixed direction:** illustrate logical start/end groups, back/forward navigation cues where direction-aware, and names, numbers, IDs, dates or URLs with mixed scripts. Do not blindly flip brand marks or numeric values. If RTL support is unknown, label the depiction `ASSUMED`; if out of scope, record the product decision and reason.
- **Locale-sensitive information:** leave enough space for formatted currency/dates/units and plural forms, without fabricating a supported locale or changing transaction values. Exact rendered formats need real localization resources and testing.
- **Accessible labels and status:** depict the *intended* pairing of field label, hint, error and focus target after translation; verify actual semantics only in the implementation.

**Handoff matrix:** `screen_id | locale/direction (KNOWN/ASSUMED) | source copy | expanded or bidi example | affected navigation/actions | intended reflow | depiction status | actual localization/AT test status`.

**Synthetic example:** A right-to-left account-settings mock keeps a long translated section heading and mixed-direction account ID readable, while the return affordance is direction-aware; mark all language as illustrative unless reviewed by a qualified speaker. **Anti-example:** a fixed-width tab silently truncates the only security-setting description, and an English label is overlaid on an RTL screenshot with no content direction plan.

**Verification:** compare translated resources and real typography at representative windows; test bidi controls, focus order, mixed-direction data, zoom and validation with supported locales and assistive technologies. A wireframe alone remains **NOT VERIFIED** for localization support or accessibility. Related: [adaptive UX](mobile-and-adaptive-platform-ux.md), [accessibility](accessibility.md), [task flow composition](../patterns/task-flows-and-information-architecture.md).
