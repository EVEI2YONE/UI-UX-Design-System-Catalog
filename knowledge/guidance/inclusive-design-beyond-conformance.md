# Inclusive design beyond conformance

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundary

Explore permanent, temporary and situational access needs, literacy levels, language contexts and environmental constraints. Complement, never replace, testable accessibility requirements.

**Use when:** Researching or designing a journey that should remain understandable across varied capabilities, contexts and prior knowledge.

**Avoid when:** Replacing WCAG criteria, accessibility reviews or consultation with general statements about inclusion.

**Accountability:** Design/research teams investigate barriers; product owners prioritize accommodations; accessibility reviewers verify specific requirements.

## Decision rules and tradeoffs

- Identify representative task barriers in cognition, reading, motor access, sensory context, time pressure, signal quality and familiarity.
- Provide alternative input and output routes where one interaction excludes people: keyboard versus drag, text versus chart, plain instructions versus unexplained icon.
- Avoid treating any demographic group as homogeneous and avoid guessing private attributes from observed behavior.
- Test plain-language comprehension, memory demands and error recovery alongside semantics, contrast, focus and reflow.
- Record evidence, meaningful exceptions and expert-user tradeoffs; do not strip critical capabilities in the name of simplicity.

## Decision matrix

| Context | Question | Decision support |
| --- | --- | --- |
| Motor access | Is precise dragging essential? | Keyboard and alternate move action |
| Cognitive load | Must details be recalled across screens? | Recognition, context and safe recovery |
| Environmental factors | Can the task survive interruption? | Reliable progress and offline policy |
| Language and literacy | Are consequences understandable? | Plain language and contextual examples |

## Example and anti-example

**Illustrative example:** A booking form supports a calendar picker and text date entry, explains availability and lets users correct mistakes without restarting.

**Anti-example:** Calling a workflow inclusive because an automated scan passes even though all important actions need fine pointer movements.

## Inclusive operation and verification

Use meaningful headings, accessible descriptions, appropriate focus, recovery and language. Review translated content, RTL, zoom/reflow, high contrast, touch and reduced motion where relevant. No mockup alone proves accessible behavior.

| Check | Evidence needed | Status |
| --- | --- | --- |
| Mixed input methods and realistic task constraints | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| Manual assistive-technology and cognitive walkthrough | Observed application or research evidence with scope and limitations | NOT VERIFIED |
| Translated text, zoom and reduced-motion checks | Observed application or research evidence with scope and limitations | NOT VERIFIED |

This concept is proposed guidance, not a real-user study, implementation, compliance claim or independently approved design standard.

## Source references and related concepts

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — review scope and edition for the consuming context.
- [W3C internationalization](https://www.w3.org/International/quicktips/) — review scope and edition for the consuming context.
- Related canonical sources: [Accessibility](accessibility.md), [Cognitive load](cognitive-load-and-decisions.md), [Mobile and adaptive](mobile-and-adaptive-platform-ux.md).
- Record a human owner, review date, evidence and known limitations before changing the proposed status.
