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
| B1 | P0 | Fidelity, outcomes and prototype escalation | CONTENT COMMITTED — proposed, pending human review | CREATE `guidance.wireframe-methodology`; REUSE hierarchy/flows/recovery/quality owners | CI PASS: 59 tests; validator PASS (50 IDs, 8 READMEs, 587 links); manual UX NOT VERIFIED |
| B2 | P0 | Task-to-screen composition and alternatives | CONTENT COMMITTED — proposed, awaiting human review | EXTEND `principle.visual-hierarchy`, `pattern.task-flows`; REUSE `guidance.wireframe-methodology` | CI PASS: 62 tests; validator PASS (50 IDs, 8 READMEs, 598 links); manual UX NOT VERIFIED |
| B3 | P1 | State annotations and recovery | CONTENT COMMITTED — proposed, human review pending | EXTEND `pattern.interaction-recovery`; REUSE forms/feedback/offline/accessibility and B1 methodology | CI PASS: 65 tests; validator PASS (50 IDs, 8 READMEs, 606 links); runtime/manual UX NOT VERIFIED |
| B4 | P1 | Responsive, reflow, long text and RTL | CONTENT COMMITTED — proposed, human review pending | EXTEND `guidance.mobile-adaptive`, `guidance.accessibility`, `guidance.internationalization`; REUSE B1 and B3 | CI PASS: 69 tests; validator PASS (50 IDs, 8 READMEs, 616 links); manual runtime NOT VERIFIED |
| B5 | P1 | Static visual QA and evidence | CONTENT COMMITTED — proposed, pending human review | EXTEND `governance.quality`; REUSE visual hierarchy, content and wireframe method owners | CI PASS: 73 tests; validator PASS (50 IDs, 8 READMEs, 624 links); image QA NOT VERIFIED |
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
- **Validation:** GitHub Actions `Validate catalog` run `42367470810` (head `c1b1bf8421b1f5ea3258c04fdd3629724155a042`) PASSED: 59 Python unittest cases, including new wireframe lookups; validator reports 50 unique concepts, 8 section READMEs and 587 relative links. Local checkout unavailable; CI provided actual execution evidence. No interface implementation or visual/a11y testing was performed.
- **Unresolved:** assign human owner/review; confirm which user-study questions demand working interaction per product; validate image readability and copy in generated assets (B5).

## B2 context and decision (2026-11-07)

- **Branch/main snapshot:** `main` at `6ed00199047488d8d5f42886112a35639fffe3ef`; PR #11 head inspected at `67f781df944e29e9e453af9b7ee32ba1d73a467a` before editing. AGENTS, CONTRIBUTING, registry/schema, B1 methodology, task-flow/hierarchy pages, research and QA pages, nested READMEs and test style rechecked.
- **Observed coverage:** `principle.visual-hierarchy` already defines task/action hierarchy; `pattern.task-flows` defines entry-to-recovery mapping. Neither had a complete brief/assumption and substantive screen-alternative comparison workflow.
- **Decision:** EXTEND two canonical concepts and task-search metadata. REUSE B1 fidelity, recovery, accessibility and quality concepts. DEFER state annotations to B3, adaptive testing to B4 and image inspection to B5. No new ID.
- **Source ledger:** GOV.UK Service Standard user needs (updated 2022-05-30), GOV.UK user-needs research and Home Office designer role standard (checked 2026-11-07); the two-variant rule and brief format are proposed catalog synthesis, not universally mandated standards.
- **Validation:** GitHub Actions `Validate catalog` run `42367684276` PASSED on commit `83c7a245442d74a943f8cd6fd211f89a84e1d473`: 62 unittest tests (including 3 new composition tests); 50 unique concepts, 8 section READMEs, 598 relative links. Tracker-only follow-up commits were not separately executed at the time of this record; live-image, real-user, keyboard, assistive-tech, responsive and implemented behavior NOT VERIFIED.
- **Unresolved:** comparisons need real user-task evidence for a winner; sensitive authorization, pricing, and data constraints cannot be assumed as implemented.

## B3 context and decision (2026-11-07)

- **Fresh repository evidence:** `main` still at `6ed00199047488d8d5f42886112a35639fffe3ef`; draft PR #11 head before edit `8ebf048f464c0295df4988a463905ef52e50f194`. Rechecked AGENTS, CONTRIBUTING, schema, 50-entry registry, interaction-recovery page, B1 methodology, B2 composition, accessibility, QA, section indexes, existing test style and source ledger.
- **Observed overlap:** `pattern.interaction-recovery` already owns pending, empty, error, permission, success and safe retry. Specialized `pattern.forms`, `pattern.feedback` and `pattern.offline-sync` own their detailed behaviors. Gap: a tool-neutral static representation matrix, annotation handoff and explicit depiction-versus-runtime evidence distinction.
- **Disposition:** EXTEND `pattern.interaction-recovery`; REUSE B1 fidelity and B2 task context; DEFER viewport/RTL stress tests to B4 and image quality to B5; CREATE none.
- **Sources:** existing proposed repository pages, W3C WCAG 2.2, WAI-ARIA APG and WAI forms validation guidance; latter links are applicability references, not independent current-web verification. Proposed state-to-screen fields and synthetic export example are synthesis, not observed product evidence.
- **Validation:** GitHub Actions run `42368095022` on B3 content/tracker commit `88a49d850041030dfda6c2353c7da70ec567913c` PASS: 65 Python tests including 3 new state-coverage tests; 50 unique concepts, 8 section READMEs and 606 relative links. Actual runtime authorization, data persistence, human task results, keyboard/AT, translated labels and responsive state transitions NOT VERIFIED.

## B4 context and disposition (2026-11-07)

- **Fresh baseline:** `main` at `6ed00199047488d8d5f42886112a35639fffe3ef`, PR #11 head before editing `e7909eec42ae54bfdb004b9a8e43134dbe0f3d34`. Re-read AGENTS/CONTRIBUTING, schema and 50-entry registry, B1–B3 guidance, adaptive/accessibility/i18n pages, quality expectations, indexes and lookup-test conventions.
- **Observed ownership:** adaptive layout/window decisions already belong to `guidance.mobile-adaptive`; keyboard/zoom/accessibility evidence belongs to `guidance.accessibility`; locale expansion and RTL belong to `guidance.internationalization`. Distinct gap: screen-image stress variants and a cross-viewport handoff/evidence matrix.
- **Decision:** EXTEND those three owners and aliases; REUSE B1 fidelity and B3 state coverage. CREATE none; DEFER direct image QA to B5, expanded examples/retrieval to B6.
- **Sources:** reused existing standards/source ledger references to WCAG 2.2, W3C Internationalization Quick Tips, Apple HIG and Android adaptive guidance. No newly verified external content. Viewport examples and review fields are catalog synthesis; no claim of universal breakpoint or WCAG pass.
- **Validation:** GitHub Actions `Validate catalog`, run `42368345996`, check-catalog succeeded on B4 content commit `c3e991b138cd2b49318315b970baae00afe99fb5`: 69 unittest cases including 4 new B4 cases, 50 unique concepts, 8 section READMEs and 616 relative links. Subsequent reference/tracker-only commits were not part of that specific run. Actual device resize, browser reflow/zoom, long-copy translation quality, RTL, focus/AT and real-user evidence **NOT VERIFIED**.

## B5 context and disposition (2026-11-07)

- **Fresh snapshot:** `main` at `6ed00199047488d8d5f42886112a35639fffe3ef`, PR #11 head before B5 `5c2d2dd7042fb8bc075c3ddfe790c28b35a9d3eb`. Inspected current AGENTS/CONTRIBUTING, schema and 50-entry index, quality gates, B1–B4 concepts, generated AI trust and content guidance, nested indexes, source ledger and test style.
- **Ownership decision:** `governance.quality` already owns evidence and review gates, so EXTEND rather than CREATE. REUSE `principle.visual-hierarchy`, `guidance.content-design`, `guidance.wireframe-methodology`, state/recovery and adaptive/i18n guidance; DEFER case library and expanded retrieval scenarios to B6.
- **Added knowledge:** rendered-image visual QA rubric, task/wording alignment, clipped or distorted generated content, false capability/transaction assertions, consistent variant/state presentation, severity, issue log and exact artifact/revision traceability.
- **Source status:** proposed synthesis from current catalog; W3C WAI Easy Checks and WCAG 2.2 referenced for applicability, not independently fetched in this batch and not image-only conformance proof.
- **Verification:** GitHub Actions `Validate catalog` run `42368545863` on B5 test/content commit `e38cc2dc7540895eec22c63743b7ec14c664f704` **PASS**: 73 Python tests including four new B5 lookup tests; 50 unique concepts, 8 section READMEs and 624 relative links. Subsequent discovery/source/tracker-only commits were not in that run. No actual wireframe images available/inspected, no live product, human task study, keyboard/screen reader, zoom/RTL or backend check: **NOT VERIFIED**.
