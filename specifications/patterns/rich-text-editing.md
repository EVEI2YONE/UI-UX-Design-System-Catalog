# Rich-text editing

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help users author structured, formatted content while preserving semantic meaning, editing selection, draft integrity and safe publication. This pattern composes an editing surface, toolbar, validation, persistence and preview; it is not a replacement for a simple textarea.

**Use when:** People need headings, lists, links, emphasis, tables, media or other semantic formatting beyond plain multiline text.

**Avoid when:** Plain text, Markdown source editing or constrained fields meet the task without complex formatting, or a full collaborative document engine needs an app-specific design.

**Ownership:** The pattern owns UX choices, composition, editing semantics and recovery. The chosen editor implementation owns model/selection operations and DOM synchronization; the service owns sanitizer rules, storage, versioning, authorization, publishing and conflict resolution.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Choose model | State supported structures, formats and whether formatting survives import/paste/export. | No hidden stripping of essential content without a preview or explanation. |
| Edit | Expose meaningful structure and formatting with discoverable controls, selection cues, undo and redo. | Support IME, keyboard text-editing conventions and robust caret restoration. |
| Paste/insert | Choose plain/structured paste behavior; validate links, attachments and allowed embeddings. | Avoid unsafe HTML execution and misleading previews; report unsupported content. |
| Save/preview | Distinguish unsaved, saving, saved, error and conflict; show actual preview constraints. | Preserve selections and content across validation and retry; no false saved claim. |
| Publish/recover | Validate final semantics, permissions and audience, with truthful published status and revision history. | Do not automatically publish on formatting or leave draft loss unexplained. |

## Decision rules and tradeoffs

- Prefer native text controls when formatting is unnecessary; choose a bounded document model and supported structural schema before selecting an editor library.
- Formatting must convey semantics rather than only visual style: headings should be headings, lists should be real lists and links should have meaningful text.
- Document editor focus, active formatting, toolbar shortcuts and text-selection recovery; a toolbar should not collapse or replace the user's selected range unexpectedly.
- Define how paste strips dangerous content, handles media and preserves meaningful structure; sanitize on the service independent of the editor.
- Treat inserted objects, embedded media and uploaded attachments as separately validated resources with visible alternatives and recoverable errors.
- Preserve draft and history across interrupted saves, version conflicts and navigation; coordinate publication decisions with the existing Content Publishing pattern.

## Interaction, accessibility, layout and localization

- Editing and formatting actions must be available via keyboard, with clear names and pressed/current states where appropriate; shortcuts cannot block basic OS/assistive-text operations.
- Provide headings/list tools and navigation through document structure, not only visual buttons. Verify editing behavior with screen readers and IME composition.
- Focus should remain in or return predictably to the editor after toolbar use. Maintain caret, selection and undo history after panel changes.
- Reflow long content and translated toolbars; support RTL paragraphs, mixed-direction links, high contrast and reduced motion without hiding formatting meaning.

Use semantic tokens for text, status, surfaces and focus; verify theme/high contrast, reduced motion, text growth, zoom and RTL in consuming products. All asynchronous success claims must reflect authoritative outcomes rather than purely optimistic presentation.

## Example and anti-example

**Illustrative example:** A support author creates semantic headings, a numbered list and a descriptive link, previews the published article, encounters a save conflict, and keeps both the working draft and a way to reconcile.

**Anti-example:** A custom contenteditable area changes all formatting into styled spans, loses the caret when a toolbar opens, and silently drops pasted content after saving.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Keyboard and assistive selection/formatting, heading/list/link semantics | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| Pasted HTML, invalid links, media upload failure and sanitizer parity | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| IME, bidi paragraphs, undo/redo, focus and long-document performance | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| Autosave failure, version conflict, preview fidelity and draft retention | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |

This is a proposed conceptual pattern. No released editor, live data service, production behavior, user study or accessibility certification is supplied. Actual capability, legal/data handling and risk limits require review.

## Sources, applicability and related concepts

- [HTML editing model](https://html.spec.whatwg.org/multipage/interaction.html#editing) — reference context; verify current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — reference context; verify current edition and applicability.
- Related canonical concepts: [Textarea](../components/textarea/spec.md), [Content publishing](content-creation-and-publishing.md), [Commenting and annotations](commenting-and-annotations.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** A product-specific feature must own real data persistence, authorization and performance verification.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Exercise paste sanitization and draft restore after failure. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

