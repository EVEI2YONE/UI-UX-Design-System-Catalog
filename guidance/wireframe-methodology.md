# Wireframe methodology and prototype escalation

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting
**Canonical ID:** `guidance.wireframe-methodology` · **Owner:** unassigned · **Human review:** pending (`reviewed_at: null`)

## Purpose and boundary

Use tool-neutral wireframes to answer a *specified design question* about a user task quickly, before investing in production UI. A wireframe is a proposed representation, **not** an implemented, tested or accessible interface. A static image, screen sequence and interactive prototype are distinct deliverables. Fidelity of **visuals**, **content**, and **interaction** can differ independently; a photorealistic image has zero implemented interaction unless separately demonstrated.

This concept owns representation fidelity, review intent, uncertainty disclosure, and escalation to an interaction prototype. Screen/task hierarchy belongs to [design principles](../foundations/design-principles.md) and [task flows](../patterns/task-flows-and-information-architecture.md); annotated exceptions and recovery belong to [interaction states](../patterns/interaction-states-and-recovery.md); actual implementation evidence belongs to [quality gates](../governance/quality-gates.md).

## When to use / avoid

- **Use when:** exploring early screen structure; agreeing on content priorities and major navigation; comparing layout ideas; preparing an annotated design for stakeholder or moderated user feedback; deciding how much prototyping is needed.
- **Avoid when:** presenting an image as working software; asserting validated focus, responsive behavior, accessibility or performance; treating synthetic content as researched customer language; using a static mock to resolve a task requiring real transitions, input, gestures, permissions, persistence or recovery.
- **Escalate:** when the design question cannot be answered from a still image or annotated sequence, build a task-complete interactive prototype with a declared test scope; for implementation claims, inspect and test the actual product.

## Fidelity selection: choose the smallest representation that answers the question

| Representation | Intended decision and typical output | Useful for | Not evidence of |
| --- | --- | --- | --- |
| **Low-fidelity / schematic** | Which regions, steps and actions exist? Sketch, grayscale blocks, plain labels, rough sequence | Early IA, task decomposition, divergent structures | Final typography, precise spacing, behavior, readability in product |
| **Mid-fidelity / structured** | Which information hierarchy, labels and component roles best support the task? Legible content, reasonable grouping and annotated states | Comparing layouts, reviewing CTA priority, representative copy, initial task walkthrough | Final branding, actual data validity, keyboard support, runtime reflow |
| **High-fidelity / visual mock** | Does the intended visual treatment communicate hierarchy and feel credible? Realistic scale, tokens, content and imagery where authorized | Visual direction, handoff discussion, content realism and visual QA | Click functionality, full accessibility, responsive implementation or production readiness |
| **Interactive prototype** (independent dimension) | What happens when people act, navigate, encounter errors or recover? Clickable or executable task paths and representative states | Task usability evaluation, interaction sequencing, focus/keyboard checks *if implemented* | Backend correctness, production safety, complete accessibility or product release readiness |

Fidelity is **not** a mandatory progression: start with a rough but interactive flow where transitions dominate; retain low visual fidelity during user testing when appropriate. More polish increases review cost and may encourage mistaken assumptions of completeness. Select by **decision/question, audience, uncertainty, and available verification**, not by a tool's rendering capability.

## Minimum wireframe evidence contract

Every wireframe set should identify: (1) user/cohort and task; (2) design question and success condition; (3) known inputs vs explicit assumptions and invented placeholder content; (4) represented screen/flow and selected fidelity dimensions; (5) primary action and expected next step; (6) states, viewports and locales shown versus *not represented*; (7) decisions requested and feedback questions; (8) review owner and evidence/verification status.

Use a consistent annotation key outside the screen where possible: **KNOWN** (provided/observed), **ASSUMED** (unvalidated design hypothesis), **ILLUSTRATIVE** (fictional text/data), **NOT SHOWN** (omitted state/viewport), **IMPLEMENTED / VERIFIED** only with separate executable/test evidence. Keep image labels and callouts legible; transcribe important text in an accompanying source-of-truth note if image generation distorts it. No label in an image establishes a backend capability or permission model.

## When interaction is necessary: decision gate

Move from static representation to a prototype when the evaluation depends on:
1. Multi-step navigation, branching, back/forward history, or preserved form input.
2. Keyboard/focus semantics, screen-reader announcements, timed behavior, gestures, drag alternatives or motion.
3. Validation, empty/loading/error/success states, permissions, retry, approval, offline behavior or irreversible actions.
4. Responsive reflow, zoom, long-text clipping or dynamically changing content.
5. Quantitative task-completion evidence or observations of users executing the flow without a facilitator inventing behavior.

An annotated story or manually facilitated paper prototype **can** support early conceptual feedback; describe the facilitator's simulated transitions, not pretend interactions are implemented. Prototypes must disclose fake data, mocked services, stubbed error paths and excluded branches. Even a working demo does not certify production behavior.

## Reusable synthetic examples and anti-examples

**Example A — early appointment selection (low fidelity).** A grayscale sequence shows service selection, available times and confirmation; one dominant “Choose time” action per step. A margin note says “ILLUSTRATIVE times; inventory availability NOT VERIFIED.” The review asks whether the order and exit path make sense. **Avoid:** a polished calendar with unsupported real-time availability and a “Booking confirmed” success claim.

**Example B — compare two settings approaches (mid fidelity).** Option A groups notification controls by event; Option B groups by delivery channel. Both use the same representative user task and content, with clear assumptions and the decision “which makes muting critical alerts easiest to predict?” **Avoid:** variants that merely swap colors and call the difference a task-flow alternative (see [task flows](../patterns/task-flows-and-information-architecture.md), Batch 2).

**Example C — payment recovery (interactive escalation).** A still image can illustrate field priority, but evaluating failed authorization, input preservation, retry and focus requires explicit state transitions and a representative interactive flow. **Avoid:** treating a static error banner as proof that recovery works.

## Limitations and verification

| Review question | Static wireframe | Required evidence for stronger claim |
| --- | --- | --- |
| Is the task and action hierarchy intelligible? | Expert review / qualitative hypothesis | Representative task observation |
| Are all critical states depicted and labeled? | Inspect annotated screen set | State inventory and prototype/runtime path checks |
| Does the layout work when resized or zoomed? | Separate illustrative viewport images only | Browser/device reflow test on an implementation |
| Is the experience keyboard/screen-reader accessible? | Annotation of *intended* behavior only | Semantic implementation, keyboard and assistive-technology tests |
| Does submission/permission/retry actually succeed? | Never established by illustration | Runtime/service tests and authorized backend evidence |
| Is generated copy accurate? | Image may contain incorrect text | Compare every essential label/value against approved text source |

**Evidence at proposal time:** literature/context review only. No real users recruited, no live UI rendered, and no application accessibility, responsiveness, performance or interaction tests executed: **NOT VERIFIED**. The catalog validator checks documentation integrity, not UX quality.

## Sources, tradeoffs and related concepts

- [Nielsen Norman Group, *UX Prototypes: Low Fidelity vs. High Fidelity*](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) (K. Pernice, 2016-12-18; reviewed 2026-11-07). Professional UX research guidance on distinguishing visual, content and interaction fidelity; **not** a normative standard.
- [Nielsen Norman Group, *Usability 101*](https://www.nngroup.com/articles/usability-101-introduction-to-usability/) (reviewed 2026-11-07). Iterative early testing; not proof of outcomes for a specific wireframe.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (W3C Recommendation). Applies to actual web content as appropriate; a screenshot cannot establish conformance.

Related: [task flows](../patterns/task-flows-and-information-architecture.md), [visual hierarchy](../foundations/design-principles.md), [interaction recovery](../patterns/interaction-states-and-recovery.md), [accessibility](accessibility.md), [mobile/adaptive UX](mobile-and-adaptive-platform-ux.md), [quality gates](../governance/quality-gates.md). No existing concept is deprecated; downstream plugin-specific tool execution remains outside this page.
