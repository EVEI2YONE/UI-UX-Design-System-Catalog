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


## Task-to-screen wireframe composition and meaningful alternatives (proposed Batch 2, 2026-11-07)

**Use when:** a task brief must become a reviewable wireframe screen or small screen sequence, or when comparing structurally distinct layout hypotheses. **Avoid when:** requirements for the user, task or critical constraints are unavailable and cannot be defensibly labeled as assumptions; a decorative reskin is presented as a second concept; or an image is mistaken for working behavior. For fidelity/escalation see [wireframe methodology](../guidance/wireframe-methodology.md). For within-screen emphasis see [visual hierarchy](../foundations/design-principles.md). For runtime state/retry semantics see [interaction recovery](interaction-states-and-recovery.md).

### Minimum context and assumption gate

Before composing, record the following in a **brief contract**, separating evidence from decisions:

| Field | Required for a defensible wireframe | Evidence rule |
| --- | --- | --- |
| User and immediate job | Which actor is doing what, and why | Provided/researched = **KNOWN**; otherwise **ASSUMED** and review before commitment |
| Entry point and current context | How the user gets here and what object/workspace they act on | Do not invent account access, product scope or navigation routes as observed |
| Desired success and next action | What counts as completion and what action advances it | Product-defined success is **KNOWN** only if documented |
| Available content/data | Required fields, constraints, useful labels and empty values | Synthetic examples visibly **ILLUSTRATIVE**, not real availability or real user copy |
| Safety, permission and data constraints | What cannot be omitted, edited, assumed or exposed | Unknown high-risk assumptions block claims of ready-to-implement behavior |
| Platform and representation | Supported surface, intended viewport(s), fidelity and image/interactive limits | Mark unrepresented viewports, states or locales **NOT SHOWN** |

If an input is missing, continue with a reversible **labeled assumption** only if it cannot alter safety, entitlement, financial terms or the user's ability to complete the core task. Otherwise mark the decision **BLOCKED / NEEDS CONTEXT**, draw neutral placeholders if useful, and do not assert a capability. Do not make up research participants, funnel metrics or application implementation.

### Task-to-screen construction steps

1. **Identify the task slice:** entry → orient → understand choices → act → pending → result → recover/exit. Select only the screen(s) needed to answer the current decision; include the predecessor/successor as annotations where not depicted.
2. **Order the information:** show task/scope/heading first, then required context and content, choice/input area, primary next action, secondary/back/help actions, and feedback/recovery cues. Preserve disclosed constraints and irreversible consequences.
3. **Compose using existing patterns:** prefer recognizable navigation, fields, selection, review and feedback components; note borrowed canonical concepts. Do not copy platform-specific behavior without verifying relevance.
4. **Show continuity:** label what data carries forward, where back/cancel leads, and where the success and failure branches reconnect. A screen image may *annotate* but cannot demonstrate persistence, keyboard order, history or authorization.
5. **Write evaluation questions:** can the user determine where they are, what they must decide, what happens next, and how to return or recover? Link unknowns to research/interactive prototype needs, not speculative confidence scores.

### Structural alternatives: decision, not decoration

Explore **at least two meaningful approaches when the task has a genuine unresolved structural choice** (if only one safe approach remains, document why variants are deferred). Keep the same audience, task, constraints and representative content across variants. Vary one or more decision-bearing dimensions:

- **Information grouping:** stepwise wizard versus single contextual form; by object versus by task, if each supports the same outcome.
- **Navigation architecture:** list-to-detail versus in-context detail, while preserving orientation and back behavior.
- **Choice/progressive disclosure:** show all essential options versus guided progressive selection without hiding safety-critical information.
- **Review position:** inline review versus separate confirmation for consequential actions; never omit confirmation solely to reduce clicks.

A second image with only colors, typography, rounded corners, or decorative rearrangement is **not** a meaningful task-to-screen alternative. Do not manufacture an intentionally inferior variant to guarantee a favorite wins. Label the **hypothesis**, expected advantage, possible harm and evidence needed for each candidate.

### Decision matrix and synthetic worked example

Score comparatively using **qualitative observations**, not fabricated numeric ratings: task clarity, discoverability, hierarchy, cognitive burden, reversibility/recovery, accessibility and translation risks, scope fit, and prototype/test cost. Record **supported / uncertain / risk** with an explicit reason and whether evidence was expert review or observed user behavior. User task tests should decide contested claims when practical.

**Synthetic task:** a team member needs to select a saved report and export a permitted view. **KNOWN for this example only:** user goal is selecting an existing report; the existence of actual exports and permissions is **NOT VERIFIED**.

| Candidate | Structural choice | Hypothesis | Risk or test question |
| --- | --- | --- | --- |
| A: list → details → export review | Separate selection and review steps | Rich context supports accurate report choice | Extra navigation; test whether return keeps the selected report |
| B: list with inline details and review panel | Same task without leaving list context | Faster comparison of several reports | Dense panel may obscure scope/permission warnings on narrow viewports |

Both must show report identity, selection context, permission unknowns, primary action, back/cancel, and an annotation of result/recovery. **Anti-example:** Variant B is Variant A with a blue button; one mock silently assumes export permission and labels the action “Exported” without implementation. **Decision:** no winner without task evidence; choose what to prototype based on risk and the key unanswered question.

### Handoff and verification contract

For each option deliver: brief contract with KNOWN/ASSUMED/ILLUSTRATIVE/BLOCKED fields; screen ID and flow location; hierarchy annotations; primary/secondary action map; state and data continuity annotations; structural-difference statement; comparison matrix; canonical citations; and an explicit **NOT IMPLEMENTED** statement for static images. Attach actual visual artifacts only where available and label generated text/data for independent copy review.

**Review gates:** (1) all required context accounted for or visibly flagged; (2) no invented rights, data or implementation; (3) action names lead to the stated outcome; (4) at least two non-cosmetic variants when warranted; (5) no critical information or safe exit lost; (6) risk/uncertainty and next validation method stated; (7) readable composition and accessibility expectations identified without conformance claims. Executable keyboard, screen reader, zoom, localization and real-user tests remain **NOT VERIFIED** unless individually performed.

**Sources and interpretation:** [GOV.UK Service Standard, understanding user needs](https://www.gov.uk/service-manual/service-standard/point-1-understand-user-needs) (updated 2022-05-30; checked 2026-11-07) supports grounding the brief in user needs and testing assumptions; [GOV.UK user-needs research](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) (checked 2026-11-07) distinguishes observed needs from stakeholder assumptions; [Home Office designer role standard](https://design.homeoffice.gov.uk/design-and-content/professional-standards/designer-role-standard) (checked 2026-11-07) describes using multiple design approaches in alpha. The specific brief, comparison rubric and two-variant decision rule above are **proposed catalog synthesis**, not mandated GOV.UK standards or empirically validated thresholds.


## B03 — spatial continuity and sequential task progress (CKG-11/12; proposed 2026-11-07)

**Scope:** how a flow keeps the current object, next action, selection and task location predictable across repeated items. This extends the task-first map, not a universal requirement to automate review queues. [Interaction recovery](interaction-states-and-recovery.md#b03--iconstate-synchronization-and-post-mutation-focus-continuity-ckg-0910-proposed-2026-11-07) owns outcome truth and focus fallback. [Component contracts](../architecture/component-contracts.md) owns event boundaries. B04 owns action-control consolidation and effort measurement.

### CKG-11 — spatial continuity before action compression

Map the user task as **last necessary input → decision control → result/status → likely next action** for pointer, touch and keyboard. Preserve stable placement and visual identity of the primary controls when only selected-item content changes. This is a *layout hypothesis* to test against actual work, not a mandatory fixed pixel distance.

| Context | Preferred behavior | Caveat/verification |
| --- | --- | --- |
| Repeated list/detail decisions | Keep selected item and decision controls in a predictable region | Do not trap the UI in an inaccessible fixed pane; test screen reader reading order |
| Form submit and next input | Place submit feedback and continuation near the form result when appropriate | Never hide essential errors outside viewport or behind a persistent bar |
| Collection filters and detail navigation | Preserve applied filter/sort, selection, scroll or equivalent return context | Do not leak search terms in URLs when sensitive |
| Narrow mobile / zoom | Move or wrap action area while preserving a usable reading and focus order | Avoid sticky controls overlapping fields, virtual keyboard or safe areas |
| Async status changes | Keep action target geometry as stable as possible | No shifting destructive target under the pointer on delayed refresh |
| Context changes | Revalidate active workspace, item eligibility and relevant permissions | Do not silently reuse participant/project identifiers across scopes |

**Review method:** capture representative task start, last input, relevant decision, feedback and next-action locations; record avoidable navigation, scroll changes, target relocations, focus jumps and lost context. Test whether stable placement improves task success and perceived clarity for relevant users. Pointer distance alone does not demonstrate improved usability; keyboard, touch, zoom and safety constraints can justify different placement. The numeric metric definition belongs to [UX measurement](../guidance/ux-measurement.md), not this flow pattern.

### CKG-12 — feature-owned sequential workflow contract

Use a sequential controller only when the user deliberately processes multiple related items and the next item can be selected unambiguously, safely and accessibly. Feature code owns permissions, eligibility, ordering, note/validation requirements and server mutation. It composes existing controls rather than replacing Button, collection, Dialog or menu primitives.

```text
ready / queue overview
  -> item selected (identity + revision + context)
  -> optional note/edit/validation
  -> decision requested (one explicit outcome)
  -> pending (disable duplicate consequential action)
  -> acknowledged by authoritative service
  -> reconciled with current permitted queue state
  -> result communicated (status + focus)
  -> next eligible selected OR user stops / returns / loads more

pending
  -> validation error: retain item/notes; correct and resubmit
  -> definite failure: explain and permit safe retry if justified
  -> unknown outcome: reconcile; DO NOT automatically retry or advance
  -> stale revision / permission changed: revalidate and explain
```

| Transition requirement | Feature contract |
| --- | --- |
| Eligibility | Select only from current authorized, eligible items at the appropriate scope; do not assume stale client list means permission |
| Next selection | Confirm outcome and reconcile relevant reads before choosing next; use stable identity/order and avoid silently skipping work |
| Pending mutation | Lock conflicting commands on the active item; preserve contextual note and selection while result is unknown |
| Skip/stop | Always provide an explicit non-mutating skip, back-to-queue or stop route as applicable; skip must not imply a decision |
| Exhausted currently loaded set | Offer Load More/refresh if there could be additional items; distinguish subset exhaustion from all work complete |
| Confirmation/reason | Preserve distinct actions, their required explanations and consequential review before commit |
| Focus and announcements | Make next item's heading/identity discoverable, focus logical target after actual transition, announce confirmed outcome sparingly |
| Changed filter/scope | Revalidate next item in the new context; do not carry subject or authorization from another workspace |
| No next item | Show truthful completion/empty/loading state with return navigation, not a stalled action bar |

**Good example (illustrative):** after a confirmed and reconciled review decision, the workflow selects the next *currently eligible* record in the same stable pane, updates its heading and actions, and deliberately moves focus to the new record's heading or safe review target; Stop and Skip remain discoverable. **Counterexample:** clicking Reject immediately clears the record and opens the next one even though its required reason was invalid or the network outcome remains unknown.

**Exceptions:** automatic next-item selection is inappropriate where a decision requires a separate review, where the user may wish to inspect the result, when task frequency/ordering is uncertain, or where access/eligibility cannot be confirmed. An explicit Next button may be safer than automatic advancement. Do not claim speed benefits without observed testing.

### B03 task-flow verification — proposed, not product-tested

| Acceptance scenario | Expected evidence | Status |
| --- | --- | --- |
| Decision success and valid continuation | Confirm/reconcile first; correct next identity, stable region and focus | NOT VERIFIED |
| Validation, conflict, uncertain result | Same item/input retained; no unsafe advance or replay | NOT VERIFIED |
| Permission, scope and pagination changes | Revalidate next eligibility, distinguish loaded subset from total work | NOT VERIFIED |
| Skip/stop, empty, long queue | Clear non-mutating exits, no phantom completed items | NOT VERIFIED |
| Keyboard, screen reader, touch and zoom | Navigation/focus predictable across content changes | NOT VERIFIED |
| User research and task metrics | Recorded task success, errors, context loss and travel with baseline | NOT VERIFIED |

**Sources and applicability:** [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for relevant focus/keyboard semantics (consulted 2026-11-07); product-inspired examples from [Little Wins UI knowledge](https://github.com/EVEI2YONE/Little_Wins/tree/main/docs/little-wins/ui-knowledge/). These documents do not certify interaction improvements or backend behavior.
