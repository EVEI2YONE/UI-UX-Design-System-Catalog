# Conversational, voice and multimodal UX

**Kind:** guideline · **Status:** proposed · **Primary layer:** experiences

## Purpose and boundary

Design AI and non-AI conversational experiences that remain understandable, interruptible and accessible when people switch between text, speech, images and graphical controls. **Use when** a task supports chat, dictation, spoken assistants, speech output, multimodal attachments or cross-channel handoff. **Avoid when** a simple labeled form, search, or command is more reliable or when speech is the only viable access route without an equivalent supported option.

This pattern owns **turn-taking, speech/text continuity, transcript/edit affordances, interruption and modality transitions**. [AI experience guidance](../guidance/ai-powered-experiences-and-trust.md) owns disclosure and output uncertainty; [agentic actions](agentic-actions-and-approvals.md) owns permissions/approvals for consequential tool use. Voice recognition or synthesis is not proof of a model's understanding or task completion.

## Modality choice and task context

| Situation | Design expectation | Failure to avoid |
| --- | --- | --- |
| Typing a request | Visible editable input, clear send/cancel, attachments distinguished by type | Silent loss of unsent drafts |
| Speaking | Explicit microphone state/permission, understandable listening/processing/speaking status | Hidden hot mic, ambiguous “listening” |
| Recognition result | Let user inspect and correct recognized names, numbers and targets, especially before actions | Treating uncertain transcript as confirmed authorization |
| Spoken response | Natural pacing, user pause/stop/repeat and accessible companion text when supported | Audio-only critical detail with no alternative |
| Image/visual input | Explain what media is accessible and what may be misinterpreted; show attached item, permission and removal controls | Claiming visual access without actually having the image |
| Voice + visual output | Maintain shared task context and compatible summaries across modalities | Inconsistent task state or different apparent actions |
| Connection or capture failure | Distinguish no recording, recording lost, transcription pending and server rejection | Inventing the missing words or claiming a saved transcript |
| Consequential action | Surface inspectable exact target and approval through an accessible modality | Speech-only confirmation for hard-to-review irreversible effects |

## Conversation and interruption contract

```text
Choose modality -> permission and ready state -> user input / upload
  -> capturing -> partial recognition / correction -> committed intent
  -> understanding / clarifying -> tentative answer or proposed action
  -> final confirmed response / approved side effect / failure
  -> continue, interrupt, switch modality, edit or exit
```

- Clearly distinguish *user is speaking*, *microphone capturing*, *speech being transcribed*, *assistant generating*, *assistant speaking*, and *agent executing a tool*. These do not necessarily happen sequentially in realtime systems.
- Support turn-taking, interruption (“barge-in”), stop speaking, cancel recording, repeat, and a manual send option when compatible with the platform. A stop of audio playback **does not undo a confirmed external tool action**.
- If input recognition has low confidence or could change an account, date, amount, person or destination, ask a concise clarification and display the interpreted value in an editable form.
- Textual companion content and non-audio pathways should cover essential information and actions. For web, apply relevant WCAG 2.2 criteria and platform-specific equivalents; do not assume a generated transcript always reflects what was spoken.
- Preserve user-provided context when switching text ↔ voice, but make scope and recording/storage/retention clear. Allow removing attachments or ending capture within the actual capability.
- Keep each tool's authorization boundary independent from conversational modality. A spoken “yes” alone must not bypass product policy for consequential side effects.
- Avoid excessive anthropomorphic cues that obscure limitations, and show when AI is generating or interpreting content.

## Illustrative interaction

A person says, “Move the Tuesday meeting to three.” The system shows its transcription, notices that two meetings match, presents the two names as accessible selectable choices, and confirms the selected time and time zone. It asks for explicit review before any calendar mutation, then announces the **verified** result via text and optional audio.

**Anti-example:** Recognition hears “fifteen” as “fifty,” the system performs a transfer while speaking “Done,” and the only correction mechanism is an inaccessible voice command.

## Privacy and inclusive operation

- Explain when the microphone/camera is active and what is recorded/uploaded; do not misrepresent browser speech recognition as universally on-device or offline.
- Offer alternatives for speech impairments, non-standard accents/dialects, background noise, silent environments and users who cannot hear audio output.
- Support different speaking speeds, pauses, turn-taking expectations and accent/language switching; avoid interpreting silence automatically as consent.
- Keep usable keyboard, switch, touch and screen-reader paths; focus should not jump on every streamed token. Long transcripts need headings, speaker labels and keyboard navigation.
- Test RTL/mixed-script text, localized names/numbers/times, bilingual speech and transcripts. Don't assume automatic language detection or translation accuracy across locales.
- On mobile and split-view screens keep live mic/stop/approval controls reachable; honor reduced motion and battery/network interruptions.

## Evaluation matrix

| Scenario | Status | Required evidence |
| --- | --- | --- |
| Turn taking, barge-in, stop, pause and correction | NOT VERIFIED | Timed task sessions with real interruptions |
| Correct capture of names/numbers/accents | NOT VERIFIED | Representative speech recordings + error review |
| Text/non-audio alternatives and assistive technology | NOT VERIFIED | Manual keyboard/AT task tests |
| Permission, capture, retention and media controls | NOT VERIFIED | Privacy and platform implementation review |
| Tool approval independent of voice/text mode | NOT VERIFIED | Security-controlled side-effect tests |
| Network loss, reconnect and modality switching | NOT VERIFIED | Integrated recovery tests |

For voice interactions, measure task outcome **separately** from recognition error, spoken response latency, false turn boundaries, user interruptions and connection failures. Report tested language, devices, acoustics and access needs; do not invent speech accuracy percentages.

## Sources and limits

- [OpenAI, Voice agents](https://developers.openai.com/api/docs/guides/voice-agents) (consulted 2026-11-07): architecture and evaluation dimensions for voice assistants; provider-specific implementation guidance, not universal UX requirements.
- [OpenAI, Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations) (consulted 2026-11-07): interruption, event and transcript state; not evidence of app correctness.
- [MDN SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) (consulted 2026-11-07): limited browser support; speech recognition can involve network processing, not necessarily offline or private.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): relevant web accessibility criteria for control, alternatives and input; not a multimodal UX certification.
- [Google People + AI, Explainability + Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/) (consulted 2026-11-07): expectations and user understanding across modes; professional guidance.

**Canonical ID:** `pattern.multimodal-conversation` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [AI experiences](../guidance/ai-powered-experiences-and-trust.md), [agentic actions](agentic-actions-and-approvals.md), [accessibility](../guidance/accessibility.md), [mobile adaptation](../guidance/mobile-and-adaptive-platform-ux.md), [content design](../guidance/content-design-and-ux-writing.md).
