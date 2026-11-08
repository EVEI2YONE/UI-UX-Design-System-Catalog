# 11 — Phase 5: core UI component reference implementations

**PR:** [#16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16) · **Branch:** `docs/visual-catalog-refactor-blueprint`  
**Scope:** Input, Field, Select, Checkbox, Dialog · **Existing Button:** retained from Phase 4  
**Status:** implementation committed and source-behavior tests passed in GitHub Actions; human browser/AT review and any final head CI remain explicit gates.

## Context gathered before edits

The canonical contracts `components/{input,field,select,checkbox,dialog}/spec.md` already specify the expected semantics. Input/Field require persistent labels and linked help/error; Select prefers native controls; Checkbox needs a true indeterminate state; Dialog requires modal semantics, initial focus, Escape and focus return. Existing `site/build.py` supports only trusted colocated classic JavaScript source, `scenarios.js` and a source-named CSS file. The shared preview runner previously supported only Button's `onActivate`.

The new work **does not introduce a component package, unreviewed custom combobox, new registry concept IDs or a second implementation framework**.

## Delivered reference source and scenarios

| Canonical ID | Actual source path | Representative scenarios and state handling |
| --- | --- | --- |
| `component.input` | `site/src/implementations/components/input/Input.js` | Empty, filled, invalid, read-only, disabled, long label; native input + `aria-describedby` |
| `component.field` | `site/src/implementations/components/field/Field.js` | Default, required, error, corrected, read-only, long label/help; explicit label/error association |
| `component.select` | `site/src/implementations/components/select/Select.js` | Empty, selected, missing required, unavailable option, loading choices, long choices; native select |
| `component.checkbox` | `site/src/implementations/components/checkbox/Checkbox.js` | Checked, unchecked, mixed, disabled, required/error, long label; native checkbox with `indeterminate` |
| `component.dialog` | `site/src/implementations/components/dialog/Dialog.js` | Confirmation, consequence-focused, pending, long text, close/reopen; native `showModal()` and focus-return intent |

Each folder additionally contains its own `scenarios.js` fixture and theme-aware `<Name>.css`. The source viewer and the iframe load the **same exact committed implementation**, with file-byte parity enforced by site tests.

The existing Button remains `component.button` and continues to reuse the same preview host. The runner now accepts synthetic `onChange` and `onClose` callbacks in addition to `onActivate`. No callbacks call external endpoints or persist data.

## Compatibility and provenance decisions

1. All 53 original canonical concept IDs and document paths remain intact; five *optional* `implementation` entries were added to existing component records. The resulting six registered controls have `implementation.status = reference`, while knowledge review status remains `proposed`.
2. All non-component catalog entries remain specification-only. No feature or pattern implementation has been registered in Phase 5.
3. References are **single-purpose executable teaching examples**, not production packages; the consuming app supplies validation, permissions, API data, status confirmation and persistence.
4. All previews remain in script-only sandboxed iframes; user-provided arbitrary source is not evaluated.
5. Native platform elements are preferred to reimplementing focus, keyboard and screen-reader behavior through custom divs.
6. Shared CSS demonstrates light/dark/high-contrast token roles, but actual contrast ratios, forced-colors behavior, 400% zoom, RTL and assistive-technology results require real browser verification.

## Automated acceptance and evidence

| Check | Evidence | Result |
| --- | --- | --- |
| Existing 53-entry registry and search | Root Python validator and unittest workflow | PASS on Phase 5 implementation CI |
| Six canonical component previews generated and source matched | `site/tests/test_build.py` | PASS on Phase 5 implementation CI |
| Five real controls and scenarios execute | `site/tests/core-controls-runtime.test.cjs` | PASS on Phase 5 implementation CI |
| JavaScript parse validity | `node --check` for all component sources and scenarios | PASS on Phase 5 implementation CI |
| Existing Button regression | `site/tests/button-runtime.test.cjs` | PASS on Phase 5 implementation CI |
| Source/render parity and sandbox flags | Python site tests | PASS on Phase 5 implementation CI |
| Real keyboard, screen-reader and browser-native `dialog` behavior | Must inspect a real browser/device | NOT VERIFIED |
| Mobile/zoom/dark/contrast visual readability | Must capture and inspect UI at actual viewports | NOT VERIFIED |
| Performance and Core Web Vitals | No deployed/representative measurements | NOT VERIFIED |

**GitHub Actions evidence:** [Validate catalog workflow 42485592631](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42485592631) succeeded on implementation/CI commit `ec180ed5a95a348df5cb224880c691ac28a830ad`. Subsequent documentation-only commits require their own latest-head check.

## Known limitations requiring review

- Node tests use a minimal DOM fixture and do **not** establish actual native keyboard behavior, browser focus handling, input method support or assistive-technology announcements.
- The Dialog reference uses a native `<dialog>` and explicit close actions. Escape, platform focus return, initial focus and narrow viewport scrolling must be tested in an actual browser before claiming verified behavior.
- `aria-describedby`/error linkage is checked structurally. Correct timing and user comprehension of validation messages remain a separate UX/manual quality decision.
- The Select reference models unavailable/loading data via fixtures, not actual async networking, authorization or option sourcing. Custom combobox variants remain out of scope.
- The Checkbox mixed state indicates a parent-group example and is not a three-valued business persistence model.
- The references use scoped `reference-*` CSS and semantic tokens. Shared token abstraction, dependency management and exhaustive cross-theme contrast review remain future quality work.
- Phase 4/5 preview format is reviewed classic JS in sandboxed static iframes. This does not claim generic TSX/React preview support or production-ready reusable packages.

## Phase 5 exit gate

**Implementation and automated CI:** PASS on implementation commit as linked. **Human design/architecture approval and actual browser/accessibility review:** PENDING. Remain draft; Phase 6 should build composed patterns only after the preview/component contracts are checked against representative real browser interactions. Do not change lifecycle statuses to stable based on automated tests alone.
