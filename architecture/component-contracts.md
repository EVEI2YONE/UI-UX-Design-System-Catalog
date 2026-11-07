# Component contracts

**Kind:** contract · **Status:** proposed · **Primary layer:** components

## Purpose

A shared component needs a stable, inspectable contract before it is marked ready for cross-context adoption. This is a reusable **specification checklist**, not a coded component.

## Required contract

1. **Identity:** durable ID, name, role, owner, version, status, consumers, use/avoid.
2. **Anatomy:** slots, content hierarchy, variants/sizes, reasonable defaults and invalid combinations.
3. **States:** applicable default, hover, focus-visible, pressed/selected, disabled/readonly, loading, success, warning, error and empty states.
4. **Interaction:** pointer, keyboard, touch, focus lifecycle, Escape behavior, async feedback, validation and recovery.
5. **Content:** label semantics, truncation, long strings, localization/plurals, RTL, text growth and icon meaning.
6. **Styling:** semantic token dependencies, scoped styles, responsive layout, light/dark/high-contrast, reduced motion.
7. **Evidence:** examples/anti-patterns, unit/interaction/visual checks, known failures, compatibility and migration notes.

## Example: Dialog shell versus destructive task

**Shared Dialog contract:** role/modality, focus entry and containment as appropriate, Escape/close, focus return, accessible name and description, backdrop behavior, resize and scroll. Refer to the [WAI-ARIA Authoring Practices Guide](../governance/references.md) for tested interaction patterns.

**Account deletion flow (not shared Dialog contract):** account context, destructive action, confirmation copy, user-specific validation, service call, recovery alternatives, and domain metrics.

## Verification matrix starter

| Scenario | Behavior to verify | Result |
| --- | --- | --- |
| Keyboard only | All controls reachable and operable; focus visible | NOT VERIFIED |
| Short and translated labels | No essential truncation or overflow | NOT VERIFIED |
| Loading and error | Feedback, prevention of duplicate action, recovery | NOT VERIFIED |
| Zoom, narrow container, touch | Layout reflows; targets operable | NOT VERIFIED |
| Theme variants | Contrast and focus across applicable modes | NOT VERIFIED |

Use [the entry template](../templates/concept-entry.md) to record an actual component specification. Do not mark this sample matrix as tested.

## Example contract: asynchronous action button (illustrative)

- **Purpose:** initiate a non-navigation action; use a link for navigation.
- **Anatomy:** required accessible label, optional icon, focus treatment, optional progress indicator.
- **API decisions:** `variant` expresses meaning (primary/secondary/destructive), `size` expresses density, `disabled` prevents activation; `loading` communicates pending work. Keep invalid combinations documented rather than adding unrelated Boolean flags.
- **Interaction:** native `button` semantics where possible, Enter/Space activation, visible focus, no duplicate submission while pending, meaningful result/error feedback. Do not make a disabled control the only way to learn why a task is unavailable.
- **Presentation:** semantic action/focus/status tokens, content-sized layout, long-label wrapping, theme and reduced-motion behavior. Icons must not be the sole signal for destructive intent.

| State | Behavior | Verification target |
| --- | --- | --- |
| Idle | Action is available and named | Pointer, keyboard, assistive technology |
| Focus-visible | Focus indication is discernible | Tab navigation across themes |
| Pending | Repeat activation is prevented without losing task context | Async success/failure path |
| Failed | Error explains recovery; entered content retained | Screen reader and retry |
| Disabled | Reason discoverable from adjacent content where needed | Alternative instructions |

**Scope boundary:** the button does not own payment, account deletion, telemetry payloads, or network retries. A feature decides if retries are safe. Test a real implementation before marking any row PASS. Related: [interaction recovery](../patterns/interaction-states-and-recovery.md).

## Batch 12 extension — versioned design-to-code handoff

Every real implementation should be traceable to a versioned canonical component contract. Document these fields before treating a shared component as ready for consumers:

| Field | Required contract |
| --- | --- |
| Source and ownership | Canonical ID, design/spec revision, owner, affected consumers, approved usage |
| Semantics and API | Correct native role, props/slots, events, defaults, invalid combinations and focus lifecycle |
| Complete states | Focus, disabled, pending, error, success, empty, selected, destructive, long text and RTL where applicable |
| Design tokens | Semantic roles, optional component aliases, all relevant modes/themes, justified overrides |
| Layout and content | Content-driven responsive rules, zoom, translations, plural formats, logical directions |
| Integration boundaries | Network, authorization and product telemetry remain feature-owned |
| Test evidence | Actually observed interaction/AT tests, browser/device matrix, reproducible screenshot diffs and known gaps |
| Migration/release | Version/compatibility, consumer update, rollout, revert plan and responsible reviewers |

**Positive example (illustrative):** A shared Dialog contract describes opening/closing focus, modal background, validation and delayed actions. A screenshot test confirms visuals at a pinned viewport; a separate keyboard/screen-reader test validates behavior, and feature engineering verifies destructive request authorization.

**Anti-example:** An engineer guesses a new focus state from a design screenshot, updates golden images in bulk and assumes the component is semantically correct. Automated image diffs cannot prove focus or authorization.

This is a contract template, not a code implementation or a declared Storybook/Playwright dependency. Related: [quality gates](../governance/quality-gates.md), [tokens](../foundations/design-tokens-and-themes.md), [lifecycle policy](../governance/lifecycle-and-decisions.md). Sources (consulted 2026-11-07): [Storybook UI testing](https://storybook.js.org/docs/writing-tests/index), [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).


## Batch 2 — composite anatomy and event coordination (CKG-04, CKG-06–08; proposed 2026-11-07)

**Scope:** reusable platform-neutral contracts for events *within* and *between* UI components. This extends the existing state/interaction checklist; it does not define application commands, invent a transport API, or require a custom framework state manager. The [icon semantics contract](../foundations/iconography-and-semantics.md) owns icon meanings, [interaction recovery](../patterns/interaction-states-and-recovery.md) owns authoritative result/uncertainty and later focus continuation, and [accessibility](../guidance/accessibility.md) owns inclusive requirements.

### CKG-04 — composite anatomy and icon/event ownership

For every repeated composition, document each **slot/part**, its semantic host, whether it is interactive, source of accessible name, event and state owner, keyboard model and target. Do not attach independent activation to a decorative SVG or a non-interactive visual wrapper.

| Slot or part | Correct host and event owner | Invalid/unsafe composition |
| --- | --- | --- |
| Labeled button with leading icon | Native Button owns activation; icon is decorative when label already names the action | Both button and nested icon handle clicks |
| Icon-only action in a collection item | A separately named Button owns its target-specific action; parent item owns display/selection | Whole clickable card contains another Button and both fire |
| Input with clear action | Input owns text editing; separate Clear Button dispatches clear request to feature/form owner | Clear icon becomes a raw SVG click target or submits the form accidentally |
| Disclosure with state glyph | Disclosure Button owns expanded state and `aria-expanded`; glyph follows the host state | Rotation alone communicates expanded/collapsed state |
| Field with error | Field links label/help/error IDs; Input/Select owns value; feature owns validation outcome | Icon-only error with no linked readable message |
| Menu button and popup | Trigger owns open request; menu primitive owns item focus and keyboard semantics; feature handles selected command | Generic list given menu roles without menu keyboard behavior |
| Tab/list/row group | Group manages selected/active item and roving focus **only when widget pattern requires it**; child actions are distinct controls | Every child and parent intercepts arrow keys or one `onClick` covers unrelated actions |

**Use existing native and accessible library controls first.** A Card is not inherently clickable; if navigation is intended, make an explicit link area and sibling action buttons, or structure a single non-nested anchor when there are no independent interactive descendants. Avoid blanket `stopPropagation()` as the normal solution to invalid nesting: fix semantic boundaries and only stop event bubbling when a documented interaction truly requires it.

### CKG-06 — three event ownership layers

| Layer | Owns | Does not own | Example |
| --- | --- | --- | --- |
| **Component event** | Native input/activation, local visual state, focus, intent signal and accessible semantics | Backend authorization, network retries, domain result | `onValueChange(value)`, `onOpenChange(open)`, `onActivate()` |
| **Feature/workflow command** | Coordinates sibling state, validation, selected item, pending operations and explicit request/response lifecycle | Pretending an optimistic view is a committed domain outcome | `requestReview(itemId, decision)` checks and dispatches a validated command |
| **Domain/authoritative outcome** | Server-owned policy, persisted revision, entitlement and consequential result; feature reconciles response | Inference from color, icon or client click | `reviewConfirmed` after validated server response |

**Do not confuse intent with completion.** Clicking "Approve" is an intent; it is not equivalent to server-confirmed approval. A shared button may display `pending`, but a feature/controller owns whether to retry, reconcile, advance or report an uncertain outcome. Commands with meaningful effects need appropriate server-side authorization and repeat-submission safety. If the outcome is uncertain, preserve intent/context for a safe reconciliation; never automatically replay a potentially non-idempotent command.

An event contract should document: **name and semantic intent; source/target; trigger modalities; payload and identity; local/controlled state preconditions; whether it is cancellable; synchronous UI changes; async boundary; response/error branches; affected sibling components; focus/announcement; recovery and tests.** Avoid vague `onAction` when the consumer cannot determine what action occurred, and avoid leaking unstructured browser events as the only feature-level API where a typed semantic value would be clearer.

### CKG-07 — cross-component coordination contract

One parent workflow/controller should own the **shared task state** when sibling components need to react. Each child exposes a meaningful event without importing or mutating its siblings directly.

```text
User → labeled input/control → semantic component event
     → feature coordinator → validate / update controlled task state
     → [local state projection to siblings] and/or authorized service command
     → pending feedback → confirmed/failed/uncertain result reconciliation
     → visible status + appropriate focus/continuation contract
```

| Composition | Shared owner | Child input event | Sibling reaction | Failure contract |
| --- | --- | --- | --- | --- |
| Search field + filter select + results | Search/filter feature | `queryChanged(text)`, `filterChanged(key)` | Applied criteria, result count, list and reset state update coherently | Preserve edited criteria; do not render a fetch failure as zero results |
| Collection row + overflow action + dialog | Collection/task feature | `menuRequested(itemId)`, `decisionRequested(itemId, action)` | Only targeted item, menu, dialog, loading row and status update | Keep identity/version, restore logical focus if row removed; avoid duplicate action |
| Field + validation summary | Form feature | `valueChanged(value)`, `submitRequested()` | Field error, summary link, pending state and submit availability align | Preserve input and focus intended field or error target |

The selection, sorting, pagination, authorization and result correctness of a product remain **feature/service concerns**. A reusable collection surface must not acquire general-purpose permissions/HTTP calls merely to reduce local wiring.

**Illustrative React-style composition — two sibling controls with one owner** (pseudocode, not an exported API):

```tsx
function SearchPanel({ search, results }) {
  const [draftQuery, setDraftQuery] = useState("");
  // Search/domain layer owns how/when results are fetched.
  return (
    <section aria-label="Find items">
      <label htmlFor="item-query">Search items</label>
      <input
        id="item-query"
        value={draftQuery}
        onChange={(event) => setDraftQuery(event.currentTarget.value)}
      />
      <button type="button" onClick={() => search(draftQuery)}>
        Search
      </button>
      <ResultsView items={results} />
    </section>
  );
}
```

The component does **not** equate `draftQuery` with the applied server query; a real feature should separately represent pending, applied, error and stale results. This illustration assumes `ResultsView` is provided by the consumer and does not establish runtime or accessibility verification.

### CKG-08 — controlled state, nested events and invalid combinations

- **Single source of truth:** if a parent owns selection, open state, query or progress, children receive the current value and emit proposed changes; they do not maintain an unsynchronized second authoritative copy.
- **Local/default state:** an uncontrolled component may hold ephemeral state if the consumer does not need to coordinate or persist it. Define exactly how `defaultValue` differs from `value`, and what happens on remount. Do not silently switch between controlled and uncontrolled ownership mid-lifecycle.
- **Transactional state:** editing a draft, submitting a command and displaying the persisted outcome are separate states; a single `isDone` Boolean cannot safely represent them all.
- **Nested interactions:** links, buttons, menu items and checkbox selections need distinct semantic hit areas and handlers; no event doubling from parent/child activation. Use `type="button"` for non-submit form actions.
- **Composite keyboard semantics:** choose the *actual* widget pattern (Tabs, Listbox, Menu, Grid, Disclosure, Dialog). Do not combine roles, `aria-selected`, `aria-pressed` and roving tab stops indiscriminately. Follow the corresponding WAI-ARIA APG pattern when a custom composite is unavoidable.
- **Event payloads:** carry stable item identifiers and authorized task context; do not rely on a mutable array index after filtering, sorting or pagination. Check current object/version before committing a consequential change.
- **Invalid combinations:** disabled + activatable; pending + duplicate submit; closed dialog + live modal focus trap; deleted item + stale-target action; decorative icon + independent keyboard stop; `selected` used to mean `approved`; checked value and visual indicator out of sync.

**Review checklist for every composite:** semantic elements and slots; owner of each state; emitted events; handler called exactly once; preconditions; pending/error path; focus entry/return; keyboard/touch equivalents; feedback; long labels/RTL; responsive/zoom; server authority if any. A menu/combobox or sortable grid must demonstrate its appropriate keyboard model before using that role.

### B02 verification matrix (documentation only)

| Check | Expected evidence | Current status |
| --- | --- | --- |
| Typed semantic events and ownership boundary | Implemented component + feature integration tests for event once and owner handoff | NOT VERIFIED |
| Controlled/uncontrolled selection consistency | Change, reset, remount, prop update and failure tests | NOT VERIFIED |
| Nested actions and accessible semantics | Keyboard, screen-reader and pointer tests on card/menu/row interactions | NOT VERIFIED |
| Async pending and authoritative outcomes | Mocked delayed, failed, conflicted and uncertain responses + no duplicate dispatch | NOT VERIFIED |
| Responsive, touch, translated labels, RTL | Actual device/viewport and locale inspection | NOT VERIFIED |
| Catalog retrieval, links and schema | Catalog validator and unit tests | NOT VERIFIED until executed |

**Adoption/migration:** keep existing canonical controls; add composition contracts at feature boundaries, remove overlapping parent/child event handlers, and migrate only consumers that need coordinated state. This is not a new universal event bus, state machine library, UI package, or application API.

**Source references (consulted 2026-11-07):** [WAI-ARIA APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/), [Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/), [Dialog Modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/). The user-task motivation was informed by [Little Wins B03 component architecture](https://github.com/EVEI2YONE/Little_Wins/blob/main/docs/little-wins/ui-knowledge/batch-03-component-architecture.md) and B07 action consolidation, whose application-specific contracts are not automatically universal.
