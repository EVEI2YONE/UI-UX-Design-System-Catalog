# 19 — Open knowledge work and evidence handoff

**Purpose:** durable, independently reviewable work packages for the gaps that still require observation, product/security decisions or maintainer acceptance. This is **repository documentation only**, not visitor-facing catalog copy and not a new canonical registry.

**Status:** all five missing knowledge contracts **authored in existing canonical guidance**, with five open evidence/implementation follow-ups; **no reviewer assigned by name**, no human approval and no deployment. The [historical KG-01–KG-12 audit](03-knowledge-gap-audit.md) is preserved, and the [current knowledge-gap assessment](17-concept-inventory-and-decisions.md) differentiates recorded, implemented, automated-tested, human-approved and production-adopted states.

| Package | Durable record | Owner role needed | Exit evidence |
| --- | --- | --- | --- |
| KG-07 | [Accessibility, themes and performance](gap-work/kg07-accessibility-performance.md) | Accessibility, visual design and performance | Human AT/keyboard/contrast/zoom/RTL and measured performance |
| KG-08 | [Maintainability/source readability](gap-work/kg08-source-readability.md) | Design-system engineer | Source review and behavior-preserving decisions |
| KG-10 | [Security, hosting and release](gap-work/kg10-release-security-hosting.md) | Repository maintainer and security/release reviewer | Hosting/CSP decisions, dependency licenses/security and signoff |
| KG-11 | [Source copy and optional distribution](gap-work/kg11-source-usability.md) | Developer-experience reviewer | Task evidence and explicit copy/download/packaging disposition |
| KG-12 | [Discovery research](gap-work/kg12-discovery-research.md) | UX researcher and agent discovery reviewer | Real task-retrieval study and measured baseline |

The other KG identifiers retain their detailed implemented/partially verified disposition in [the closure ledger](17-concept-inventory-and-decisions.md); this index does not pretend they have received human release approval. The [ten durable concept decisions](concepts/decision-manifest.json) continue separately from these *verification and release* work packages.

## Separation from the public site

The visual catalog presents canonical **design guidance**, live source-linked examples and meaningful maturity labels. Original "Batch N", "Phase N", project PR/process notes and source evidence histories remain available in the repository, but are not user-facing page headlines or promotional content. Phase reference appendices are redundant with the real preview/source panel and are omitted from visitor-facing rendering; substantive batch-authored design guidance remains visible under domain-specific headings.

## Maintaining the record

When a reviewer completes an item, provide real evidence, a named decision and date, amend the relevant work package, and update the [release risk register](16-phase-10-release-readiness.md). Keep unresolved packages even if a future release deliberately excludes their related feature. Do not add unreviewed candidates to `catalog/index.json`, and do not promote a knowledge lifecycle status solely because CI passes.

**Release remains NO-GO** until the human/security/hosting gates are explicitly cleared. Draft [PR #16](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/16) remains unmerged.

## Canonical knowledge now authored

Each work package links to the substantive new contract in its existing canonical knowledge owner: [maintainability](../../architecture/component-model.md#executable-reference-maintainability-and-composition-contract), [a11y/performance](../../guidance/accessibility.md#reference-state-accessibility-theme-and-performance-acceptance-matrix), [source reuse](../../architecture/component-contracts.md#source-exploration-reuse-and-distribution-contract), [discovery research](../../guidance/ux-measurement.md#catalog-discoverability-and-source-trust-study-protocol), and [security/hosting](../../governance/quality-gates.md#static-visual-catalog-hosting-supply-chain-and-preview-security-gate). See the [fresh-context, source and acceptance ledger](20-knowledge-development-batches.md) for precise existing coverage and the unchanged human verification requirements.
