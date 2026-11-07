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

## Flow specification and acceptance example

Record a task as **entry → orientation → choose → act → pending → outcome → recover/exit**. For each transition document user intent, destination, data preserved, error states, keyboard/focus destination and any authorization constraint. Navigation changes need deep-link and browser-history checks; do not break direct entry to a valid route in order to simplify the menu.

**Illustrative flow: finding a saved item**

| Step | Visible information | Next action | Exceptional state |
| --- | --- | --- | --- |
| Entry | Current section and clear page heading | Open search | Expired session: explain and provide safe sign-in return |
| Search | Query, filters and result count | Open result | No results: offer query edit/reset |
| Detail | Item title, context and related actions | Return to results | No access: explain availability without exposing private data |
| Return | Preserved query and prior position | Continue selection | Stale item: refresh without silently discarding context |

**IA acceptance:** primary routes and labels are distinguishable; landmarks and headings form a predictable hierarchy; filter and back behavior are consistent; direct links and narrow/reflowed views function; empty/error branches have recoverable next steps. Validate the model with task observation and task completion, not click count alone.


## Multi-scope task context and optional features (2026-11-07)

**Observed example:** Little Wins scopes Overview, Review and History by project, but Members and Rewards by group. Groups own membership/points, while projects own challenges/submissions. Moving a challenge recalculates project progress without moving the submission or point ledger.

**Guidance:** before drawing navigation, make a resource/scope matrix (account -> workspace -> group -> project -> record) with visible scope for every list, aggregate, action and deep link. Keep the active project explicit where data is project-filtered; distinguish global/group-wide views with their own headings and filter affordances. Verify changing project with unsaved forms, old links, return navigation and no-results states. Avoid suggesting a product-wide project filter that misleadingly narrows group-wide rewards.

**Feature flags:** document whether points, challenges and rewards are independent, which actions disappear, what previously earned records remain visible, and what happens after re-enabling. Never delete historical data just because a feature is hidden. Clarify the owner and dependency policy for any derived totals.

**Example:** a Review queue heading says “Reading project”, while Rewards says “All group rewards”. **Anti-example:** the same ambiguous project chip suggests that group-wide balances are filtered to a project.

**Checks:** scope matrix for every route; accessible focus/context announcements; empty and revoked-project states; localized labels; restored history and balances on feature toggle; no unintended mutations when moving a challenge.


## Batch 8 — capability dependencies and configuration-state journeys (2026-11-07)

**Purpose:** extend the earlier multi-scope/optional-feature guidance with a testable **capability matrix**, not an assumption that independently stored toggles represent independent user capabilities. Use when owners can pause/re-enable optional tasks or features whose actions depend on other features. Avoid prescribing universal flag names, infrastructure or authorization from a UI control.

**Context-first trigger:** Little Wins persists `pointsEnabled`, `rewardsEnabled` and `challengesEnabled` independently on each group. Its redemption command requires **both points and rewards**, whereas challenges have separate visibility. The Rewards navigation is hidden when either prerequisite is off, yet the Rewards page contains a paused-state notice and preserves existing requests. These are source-observed behaviors, not live UI test results.

**Define before implementation:**
1. **Configuration versus capability:** map each stored flag to the actual action preconditions and derived availability. Define one centralized, documented capability predicate per protected action; a hidden tab does not authorize or block a direct command.
2. **State matrix:** enumerate every meaningful flag combination (three booleans imply eight configurations), including dependent UI, server action, existing record visibility, history, settings labels and recovery route. A paused state may differ from hidden, disabled, read-only or permission-denied.
3. **Transition contract:** distinguish disable -> paused, paused -> enabled, flag edits during an in-flight operation, and stale tabs. Explain whether work in progress finishes, is rejected safely or must be retried.
4. **Reversibility and historical integrity:** never delete previously approved entries, ledger transactions, reservations or challenge records merely to hide a feature. Determine what past data remains visible, downloadable or actionable and who may manage pending requests.
5. **Discoverability:** if navigation disappears but requests remain pending, provide a deliberate authorized route to review/manage those requests; do not assume a deep link is discoverable.
6. **Scope and roles:** group versus project flags, defaults for new groups, membership permissions and deployment gating are distinct decisions. Keep one source of truth for actual action availability; test a denied direct command independently of visual gating.

**Illustrative capability table (Little Wins source, simplified):**

| Points | Rewards | Challenges | Redeem new reward | Challenge task | Historical points/redemptions |
| --- | --- | --- | --- | --- | --- |
| On | On | Either | Available if balance and permissions permit | Depends on challenges | Must preserve |
| Off | On | Either | Unavailable | Depends on challenges | Must preserve |
| On | Off | Either | Unavailable | Depends on challenges | Must preserve |
| Off | Off | Either | Unavailable | Depends on challenges | Must preserve |

This table describes the relevant domain command and UX intent; it does not claim that all combinations have been tested in production.

**Good:** settings explain “Turning off points pauses new reward requests; previous requests remain available to manage.” **Anti-example:** disabling points silently hides the only path to an outstanding reward request while an API still accepts a stale or unauthorized command.

**Verification:** eight-configuration state table, direct API action for each configuration, pending-work and history preservation, settings confirmation, stale-tab race, re-enable with intact balances, keyboard/read-only affordances, localized labels, mobile navigation and permission differences. Report missing browser/API evidence as **NOT VERIFIED**.
