# Data visualization and dashboards

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose and boundary

Make chart and dashboard choices around the question users need to answer, data integrity, and accessible equivalent understanding. **Use** for trends, category comparisons, relationships, KPIs and monitoring. **Avoid** a chart when a sentence or [data table](../patterns/data-tables.md) better serves the task. Product/data teams own values, data rights, validity and alert thresholds; this entry describes presentation and verification.

## Match representation to the question

| Question | Start with | Review for |
| --- | --- | --- |
| What is the confirmed current value? | Labeled KPI: unit, period, cohort, freshness | Missing denominator or stale data |
| How does a value change over time? | Line chart and a plain-language trend summary | Gaps falsely joined; ambiguous date range |
| Which categories differ? | Bar chart with consistent, meaningful baseline | Truncated bar scale exaggerating differences |
| How are observations distributed? | Histogram, box plot, or table based on data literacy | Unexplained bins, missing samples/outliers |
| Are quantities associated? | Scatter plot with clearly named axes | Implied causality from correlation |
| Which records need action? | Sortable/filterable data table with relevant summary | Actions available only via hover on a mark |

Choose familiar forms and meaningful labels. Avoid decorative 3D, gratuitous dual axes, unverified forecasts and using colors with no alternative. A nonzero line-chart axis can be appropriate when transparently labeled; bar lengths should not misrepresent relative magnitude.

## Chart and KPI contract

For each visualization record: **user decision; intended audience; data source; definition; time range and timezone; value/axis units; aggregation/denominator; missing or suppressed data; update freshness; default filter state; selected scale; takeaway; accessible alternative; interaction and export permission**. Make actual, target, forecast and estimate visually and textually distinguishable. A data table helps expose individual values but does not always communicate the chart's overall *narrative*, so provide a text summary of key relationships and uncertainty.

Interactive charts must not require hover, precise pointing or color recognition to retrieve essential information. Define keyboard focus, filtering and tooltip access, focus restoration, meaningful announcements, and equivalent table or drilldown. Charts with role-restricted breakdowns need server-side authorization for underlying data, screenshots and exports.

## Dashboard composition and failure states

- Order panels by primary decision or urgent action, not arbitrary card arrangements. Group related KPIs under clear headings.
- Make the scope of a filter obvious: global dashboard, panel group, or chart only. Preserve accessible filter control state.
- Use clear empty, filtered-to-zero, restricted, loading, stale, partial-error, delayed-update and failed states. Never present stale values as current.
- Responsive layouts may stack visualizations, swap to an accessible data summary or allow localized horizontal scrolling; do not silently hide crucial comparisons.
- Support text scaling, keyboard and screen reader interaction, high contrast, color-blind-friendly encodings, translated units/labels and RTL without mechanically flipping quantitative axes.

**Illustrative example:** A weekly service dashboard labels a line chart's time period and current update timestamp, explains that completion rose while sample volume fell, and provides authorized table data.

**Anti-example:** A full-screen unlabeled red/green dashboard truncates axes and shows a 12% increase without baseline, denominator or update date.

## Verification

| Check | Status | Evidence needed |
| --- | --- | --- |
| Task, chart selection and narrative comprehension | NOT VERIFIED | Study with target users and realistic datasets |
| Calculations, denominators and freshness | NOT VERIFIED | Data owner and test fixtures |
| Screen-reader/table/text summary parity | NOT VERIFIED | Manual AT testing |
| Color/scale/keyboard/mobile/RTL/zoom | NOT VERIFIED | Supported device/locale matrix |
| Authorization of drilldowns/exports | NOT VERIFIED | Security tests |

## Sources, applicability and related concepts

- [USWDS Data visualizations](https://designsystem.digital.gov/components/data-visualizations/) (consulted 2026-11-07): accessibility and narrative guidance, **guidance-only**, not a shipped chart library.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): applicable web accessibility criteria; not a chart quality or user comprehension certification.
- [WAI-ARIA APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) (consulted 2026-11-07): applies to an actual interactive grid keyboard model, not ordinary read-only HTML tables.

**Canonical ID:** `guidance.data-visualization` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [Data tables](../patterns/data-tables.md), [UX measurement](ux-measurement.md), [accessibility](accessibility.md), [internationalization](internationalization.md), [cognitive load](cognitive-load-and-decisions.md).
