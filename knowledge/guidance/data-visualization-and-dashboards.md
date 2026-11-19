# Data visualization and dashboards

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence

## Purpose and boundary

Make chart and dashboard choices around the question users need to answer, data integrity, and accessible equivalent understanding. **Use** for trends, category comparisons, relationships, KPIs and monitoring. **Avoid** a chart when a sentence or [data table](../../specifications/patterns/data-tables.md) better serves the task. Product/data teams own values, data rights, validity and alert thresholds; this entry describes presentation and verification.

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

## Scoped overview cards, activity summaries and drill-down

An overview is a **task and navigation surface**, not an instruction to fit every chart into cards. First name the decision ("what changed?", "where should I act?", "which scope?") and then choose the smallest truthful representation.

| Question or intent | Initial surface | Drill-down / alternative |
| --- | --- | --- |
| What is the confirmed total now? | Labeled KPI with scope, unit, period and freshness | Detail table with numerator/denominator and calculation definition |
| What happened recently? | Bounded activity preview with actor/time/action and "View activity" | Filterable accessible timeline; no invented aggregate chart |
| Which project needs attention? | Project summaries with status and one clear next action | Scoped project view, not silently filtered workspace totals |
| Is the trend changing? | Short textual trend or small plot only when reliable historical data exists | Accessible chart + equivalent table/text and explicit gaps |
| Who or what contributed? | Linked record/person summary only when authorized | Permissions-aware detail; do not infer cause from correlated activity |

**Scope and metric definition:** Every displayed number specifies `metric name | scope type + stable scope ID | eligible cohort | numerator/denominator or aggregation | unit | time window/time zone | data authority | freshness | filters | access policy`. Workspace, project, person and activity scopes must be distinguishable in labels, breadcrumbs and deep links. Decide whether a filter affects *this component*, *this view* or *the entire workspace*; do not let a project filter silently change global totals, reward counts or unrelated cards. If counts are partial, estimated, delayed or access-limited, say so near the number.

**Composition examples (illustrative prose):**
- **Compact workspace overview:** current workspace identity, two meaningful scoped indicators, one high-priority action, a bounded recent-activity preview and a link to full activity. No mini-chart if the question is only "what needs attention?".
- **Record/project summary card:** title link, active/archived state, one scoped count with unit/period, recent change and a clear destination; prefer [collection card composition](../../specifications/patterns/collection-and-feed-views.md#actionable-record-cards-and-related-item-disclosure) over adding more controls to a KPI.
- **Project-detail analysis:** project breadcrumbs, date range and filter state, trend comparison where warranted, accessible summary/table, and a return route restoring the overview's scope and focus. Keep a narrow-screen priority order: task and status first, data preview second, rich analysis after explicit navigation.

**Correct scope example:** "Workspace · 18 active records · as of 09:00 UTC" remains the workspace total while "Project Atlas · 4 active records · same time" is separately labeled. Drill-down retains `project=Atlas` and the chosen period; Back restores the previous workspace filter. **Anti-example:** Selecting Atlas silently changes the unlabeled global "18" card to "4", then Back loses the period and selected record. These values are synthetic and not real metrics.

**State contract:** Loading and partial data must not show a cached value as current; no activity is different from no access; unavailable/archived scope retains context and explains limits; a changed reporting period recalculates labels/denominators coherently; stale/failed data provides a timestamp and retry or last-confirmed fallback. Provide chart-equivalent text/table, keyboard-accessible drill-downs, meaningful units/time zones, 320px/zoom reflow, long translations and RTL-safe reading order.

**Acceptance (runtime and comprehension NOT VERIFIED):** Verify distinct workspace/project/person scopes, stable period/filter/back behavior, denominator and freshness labeling, permission-limited and partial states, narrow-screen navigation, keyboard/screen-reader table parity and no false causal story. A data owner must validate calculations; representative users must test comprehension separately. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) supports applicable accessibility checks, while [USWDS data visualizations](https://designsystem.digital.gov/components/data-visualizations/) is illustrative public-sector guidance; neither proves metric correctness or task success in a consuming application.

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

Related: [Data tables](../../specifications/patterns/data-tables.md), [UX measurement](ux-measurement.md), [accessibility](accessibility.md), [internationalization](internationalization.md), [cognitive load](cognitive-load-and-decisions.md).

## Applying this guidance: decision and evidence check

**Representative decision to evaluate:** Validate one chart-versus-table decision with an actual user task. Define the intended cohort and task, initial conditions, competing option, observable user outcome and relevant accessibility, language and privacy constraints. Keep assumed behavior separate from user evidence; examples are illustrative unless results are directly recorded.

**Acceptance record:** Name the selected research or audit method, eligible population, task and metric denominator where applicable, observed versus expected outcome, source version and unresolved validity limitations. Do not treat a worked example as a completed study. For web accessibility only, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) gives relevant criteria; it cannot validate a UX hypothesis or provide a product baseline.

