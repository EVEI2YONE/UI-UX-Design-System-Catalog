# Task flows and information architecture

**Kind:** guideline · **Status:** proposed · **Primary layer:** experiences

## Purpose

Design around high-value user tasks instead of page inventories or decorative consistency. Establish content grouping, navigation and entry points that make intended actions discoverable.

## Task-first flow map

```text
entry -> orientation -> decision -> input -> pending -> success
                                   \-> error -> recovery/retry
                                   \-> cancel/exit
```

Record user cohort, context, success condition, primary action, safe exit, and failure branches. Add empty, no-permission, expired-session, partial-failure and offline states as applicable. Include keyboard, mobile and assistive-technology equivalents.

## Information architecture checks

- Group content around user mental models and jobs rather than the organization chart.
- Use specific, predictable labels; preserve deep links and routes during navigation changes.
- Distinguish main navigation, contextual actions, filters, search and breadcrumbs.
- Use progressive disclosure for advanced details, but never hide safety-critical information.
- Treat extra clicks as a hypothesis about friction: sometimes an explicit review step improves comprehension and trust.

**Example:** search results expose clear filters, total/empty context, next actions and recovery from a failed query. **Anti-example:** important filters are only discoverable from an icon without a label and disappear after an error.

## Verification

Test representative first-time and returning tasks, navigate with keyboard, inspect narrow and zoomed layouts, and compare task completion and step abandonment with a documented baseline. See [UX measurement](../guidance/ux-measurement.md).