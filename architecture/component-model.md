# Component model

**Kind:** guideline · **Status:** proposed · **Primary layer:** components

## Purpose

Preserve coherent, reusable interfaces without placing every app feature in one shared library. Reuse must improve maintenance and task quality, not merely reduce file counts.

| Level | Owns | Must not own | Examples |
| --- | --- | --- | --- |
| Foundations/tokens | Color intent, typography, spacing, motion | Product business state | `color.text.primary` |
| Primitives | Semantic layout and presentation building blocks | Requests/workflow orchestration | `Stack`, `Text` |
| Components | Stable presentation or interaction contracts | App-specific API calls | `Button`, `Select`, `Dialog` |
| Patterns/features | Composition, task logic, contextual validation | Reimplemented shared primitives | Search panel, account form |
| Pages/modal flows | Routes, user journey, page-level information architecture | Separate ad-hoc component system | Settings, onboarding |

## Reuse decision

- **Reuse** when meaning, states and behavior already match.
- **Extend** when a small semantic variant keeps the contract testable.
- **Compose** when the requirement is a business workflow built from stable parts.
- **Keep app-local** for one-off or fast-changing domain logic.
- **Create shared** after demonstrated repeat use or clear cross-product leverage, with an owner and testable API.
- **Merge/deprecate** competing variants when they are equivalent; provide a migration path.

**Avoid:** `UniversalForm` with dozens of Boolean props and internal business APIs. Prefer shared field, label, error and layout controls composed into task-specific forms.

## Verification

Check existing catalog synonyms and imports before adding a duplicate. Record consumers, ownership, stable public API, token usage, accessibility states, migration impact and expected tests. Related: [component contracts](component-contracts.md), [lifecycle policy](../governance/lifecycle-and-decisions.md).