# Wireframe knowledge expansion — shared batch tracker

**Status:** proposed / in progress; documentation-only. This is a coordination ledger, **not** canonical design guidance.

- Repository: `EVEI2YONE/UI-UX-Design-System-Catalog`
- Base branch: `main`
- Base commit at branch creation: `6ed00199047488d8d5f42886112a35639fffe3ef` (2026-11-07)
- Working branch: `docs/wireframe-knowledge-batches-2026-11-07`
- Review process: one draft PR accumulates independently reviewed batches; no merge without authorization.
- Current baseline observations: root `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `catalog/index.json`, `catalog/schema.json`, and `catalog/README.md` inspected at `main`. The README describes 49 proposed catalog entries. Existing candidates include `principle.visual-hierarchy`, `pattern.task-flows`, `pattern.interaction-recovery`, `guidance.accessibility`, `guidance.internationalization`, and `governance.quality`. Proposed mappings below are **not** ownership decisions until contextual review.

## Per-batch execution rule

Before **each** batch's substantive knowledge commit: fetch the latest branch and `main` refs; inspect `AGENTS.md`, `CONTRIBUTING.md`, registry/schema, related canonical entries, aliases, section READMEs, tests, relevant authoritative sources and any prior batch changes. Record source observation vs inferred recommendation, classify REUSE / EXTEND / CREATE / DEFER, and check for conflicts. Implement only the justified delta. Run available catalog validation and tests, record actual results or `NOT VERIFIED`, and commit with a batch-specific message. Do not claim image-based illustration proves behavior, accessibility, or production implementation. Keep plugin-specific instructions outside canonical knowledge.

## Batch progress

| Batch | Priority | Scope | Status | Initial likely canonical ownership (verify on execution) | Validation |
| --- | --- | --- | --- | --- | --- |
| B0 | gate | Baseline and canonical inventory | COMPLETE — policy/registry/related-page overlap inspected for B1; ongoing per-batch discovery remains required | registry and repository policy | NOT VERIFIED |
| B1 | P0 | Fidelity, outcomes and prototype escalation | CONTENT COMMITTED — proposed, pending human review | CREATE `guidance.wireframe-methodology`; REUSE hierarchy/flows/recovery/quality owners | Repository validation/tests NOT VERIFIED; manual UX NOT VERIFIED |
| B2 | P0 | Task-to-screen composition and alternatives | NOT STARTED | `principle.visual-hierarchy`, `pattern.task-flows` | NOT VERIFIED |
| B3 | P1 | State annotations and recovery | NOT STARTED | `pattern.interaction-recovery` | NOT VERIFIED |
| B4 | P1 | Responsive, reflow, long text and RTL | NOT STARTED | `guidance.mobile-adaptive`, `guidance.accessibility`, `guidance.internationalization` | NOT VERIFIED |
| B5 | P1 | Static visual QA and evidence | NOT STARTED | `governance.quality` | NOT VERIFIED |
| B6 | P2 | Synthetic examples, aliases and lookup regression | NOT STARTED | canonical examples, `catalog/index.json`, tests | NOT VERIFIED |
| B7 | gate | Integrate READMEs, registry, changelog, source ledger, validate and hand off | NOT STARTED | discoverable navigation and quality gates | NOT VERIFIED |
| B8 | optional | Plugin consumer instruction integration validation | DEFERRED, outside canonical catalog PR | external consumer instructions | NOT VERIFIED |

## Before marking any batch complete

- Cite actual source files and canonical IDs, plus source edition/date, evidence and limitations.
- Explain reuse/extension/create/defer choice and identify reviewer/owner as unassigned where appropriate.
- Preserve proposed lifecycle for new entries and `reviewed_at: null` until human review.
- Include use/avoid rules, design decisions, examples/anti-examples and verification expectations.
- Update affected registry metadata, index READMEs, changelog and lookup tests whenever applicable.
- Run `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` where executable.
- Keep outstanding questions and unexecuted manual/interactive/accessibility checks explicitly `NOT VERIFIED`.

## Integration contract for downstream design agents (to complete in B7)

Retrieve by task/alias from `catalog/index.json`; read canonical `path`, positive/negative usage constraints, `related` and `depends_on`; distinguish required design context from labeled assumptions; specify at least two structurally meaningful alternatives when warranted; annotate static states and prototype escalation; evaluate image output without claiming validated implementation. This is a **proposed acceptance target**, not yet implemented canonical authority.

## B1 context and decision (2026-11-07)

- **Observed:** `main` commit `6ed00199047488d8d5f42886112a35639fffe3ef` and PR #11 tracker head were checked. Canonical registry previously had 49 proposed entries. `principle.visual-hierarchy` covers screen priorities; `pattern.task-flows` covers task map and exits; `pattern.interaction-recovery` covers state recovery; `governance.quality` covers evidence. No dedicated registry entry for wireframe fidelity/prototype escalation was present after alias/title scan.
- **Decision:** CREATE one `guidance.wireframe-methodology` entry for representation fidelity, design question, evidence/assumption labels and static-to-interactive gate. REUSE/DEFER composing alternatives to B2, states to B3, adaptive/RTL to B4, visual QA to B5, retrieval expansion to B6. No plugin-specific operating rules.
- **External research:** NN/g (2016 fidelity taxonomy; current review 2026-11-07), NN/g Usability 101 and W3C WCAG 2.2 (normative only for applicable implementation), listed in references. Synthesis and examples are proposed rather than observed user outcomes.
- **Validation:** catalog Python validator and Python test suite NOT VERIFIED because a complete checkout could not be obtained in this runtime. Static registry shape/id/ref check may be performed separately. No interface implementation or visual/a11y testing was performed.
- **Unresolved:** assign human owner/review; confirm which user-study questions demand working interaction per product; validate image readability and copy in generated assets (B5).
