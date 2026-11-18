# UX research methods and evidence

**Kind:** guideline · **Status:** proposed · **Primary layer:** context

## Purpose and scope

Select research methods that answer a decision-relevant question about user needs or interface usability. Product analytics, stakeholder opinions and a prototype walkthrough can inspire questions but are not substitutes for research with intended users. This is a general research protocol, **not** a claim that any catalog guidance has been empirically validated.

## When to use / avoid

- **Use when:** unfamiliar needs, conflicting design hypotheses, uncertain critical journeys, accessibility risk, launch decisions or unexplained task abandonment.
- **Avoid when:** the question is already answered by trustworthy recent research in the same context; when a study cannot influence a decision; or when collecting participants or sensitive data without an agreed ethical and privacy process.

## Method-selection guide

| Question | Useful approach | Evidence limit |
| --- | --- | --- |
| What jobs, constraints, workarounds and language do people use? | Contextual inquiry, observations, interviews or diary studies | Small qualitative samples illuminate possibilities, not population prevalence |
| Can representative users complete a specified task? Where do they struggle? | Moderated usability testing; accessible devices and assistive tech when relevant | Performance depends on task realism and recruitment; don't treat researcher assistance as success |
| Can many users complete a narrow, stable flow without moderation? | Unmoderated task study with observable completion criteria and safeguards | Weak for discovering motives; instrumentation failures can hide difficulty |
| How often is a defined problem or attitude reported? | Designed survey with an explicit sampling frame and neutral questions | Self-report and selection effects; cannot establish observed behavior |
| Where do instrumented users abandon a flow? | Privacy-respecting funnel/event analysis | Locates possible friction, not why; incomplete events distort denominators |
| Is one design better under controlled conditions? | Experiment or comparative task study with a predeclared outcome | Requires adequate design, power, guardrails and interpretation; see [UX measurement](ux-measurement.md) |

Choose methods according to **behavior vs reported attitudes**, **qualitative vs quantitative evidence**, and **generative vs evaluative purpose**. Combine methods when different questions require different evidence; do not treat a single method as universally sufficient.

## Study plan contract

Before recruiting, record:
1. **Decision:** What will change if the finding supports or rejects the hypothesis?
2. **Research questions and assumptions:** Specific, falsifiable where possible; not leading the participant toward a preferred UI.
3. **Users and context:** Eligibility, task frequency/criticality, novice/expert, language, device, assistive technology and access needs.
4. **Method and tasks:** Realistic neutral scenarios, success/failure indicators, moderation, capture and analysis method.
5. **Sample and limitations:** Why the chosen participants cover the key variation; convenience recruitment, missing segments, sampling and researcher bias.
6. **Ethics:** Informed consent, accommodations, compensation, safety/escalation for sensitive topics, collection minimization, retention and restricted raw access.
7. **Analysis and decision rule:** How observations, severity, contradictory findings and uncertainty will be recorded; whether to iterate or commission further research.

Do not universalize a fixed participant number; method, risk, variability and research objective determine sample requirements. Recruit iteratively when possible and explicitly document excluded segments.

## Session and synthesis procedure

1. Pilot the guide, tasks and accessible prototype; verify technical setup and non-sensitive example data.
2. Welcome participants, explain voluntary participation and consent, then ask non-leading questions; observe what they **do** separately from what they **say**.
3. Capture timestamped behavior, participant-reported statements and researcher interpretation as distinct fields.
4. Synthesize by user task and scenario; group repeated obstacles, exceptions and contradictions, not just majority opinions.
5. Tag each finding: observed evidence, segment, severity, confidence, alternative explanations, affected decisions and follow-up.
6. Share a redacted, decision-oriented summary with owners and connect improvements to measurable task criteria.

**Illustrative study:** A settings form is frequently abandoned (analytics signal). Observe eligible people attempt the task on their actual input methods; note hesitation and errors; run an optional post-task effort question. Compare with event counts; do not declare the reason from analytics alone.

**Anti-example:** “Five users liked this screen” becomes “95% of customers prefer it” or a critical accessibility flow is excluded because recruiting those users is inconvenient.

## Deliverable template

| Field | Example (illustrative only) |
| --- | --- |
| Research question | Can first-time users find and change notification preferences? |
| Decision supported | Keep existing navigation vs move preferences under Account |
| Participants | New users and returning users; include relevant access needs |
| Task / success | Change an example preference without moderator guidance |
| Evidence | Task result, observed path/errors, participant remarks, assistive setup |
| Outcome | Reuse / revise / research further; owner and follow-up date |
| Confidence | Moderate only for studied tasks/participants; generalization unknown |

## Evidence and verification

- **Catalog-document review:** proposed; human review NOT VERIFIED.
- **Usability and accessibility testing of a real product:** NOT VERIFIED.
- **Research findings / baseline:** none supplied; do not fabricate participants, TCR or representativeness.
- **Relevant acceptance:** a reviewer can trace each design recommendation to an observation, a documented inference, or a testable hypothesis.

## Sources, applicability and related concepts

- [Nielsen Norman Group, When to Use Which User-Experience Research Methods](https://www.nngroup.com/articles/which-ux-research-methods/) (2022; reviewed July 2026): method dimensions; descriptive professional framework, not a guaranteed sample recipe.
- [GOV.UK, Plan user research for your service](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service) (2016; consulted 2026-11-07): practical service-research planning and inclusive recruitment; adapt to product context.
- [GOV.UK, Plan a round of user research](https://www.gov.uk/service-manual/user-research/plan-round-of-user-research) (2016; consulted 2026-11-07): objectives, consent, participant logistics and analysis.

**Canonical ID:** `guidance.ux-research` · **Owner:** unassigned · **Last human review:** none; proposed on 2026-11-07.  
**Related:** [UX measurement](ux-measurement.md), [journey mapping](mental-models-and-journeys.md), [task flows](../patterns/task-flows-and-information-architecture.md), [accessibility](accessibility.md).
