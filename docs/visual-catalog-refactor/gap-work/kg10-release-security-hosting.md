# Hosting, CSP, dependency and release decision

**Knowledge-gap IDs:** KG-10  
**Status:** knowledge specification FILLED; verification/implementation follow-up OPEN, no human approval  
**Origin:** [original gap audit](../03-knowledge-gap-audit.md) and [durable concept / closure ledger](../17-concept-inventory-and-decisions.md)  
**Recorded:** 2026-11-08 · **Accountability:** Repository maintainer and security/release reviewer (role only; no named assignee)

## Why the gap remains

The site builds as a root-hosted static artifact, but no hosting origin, subpath strategy, headers, dependency license/security signoff, or real release authorization has been accepted.

## Recommended work

Choose hosting/base path and source-ref policy; produce reviewed CSP and framing/header configuration; lock and audit CI dependency tree and licenses; assess source and synthetic adapter threat boundaries; document preview artifact retention; reconcile PR with main before approval.

## Acceptance evidence required

Published hosting proposal and header test, reproducible dependency lock/SCA and license report, named reviewer signoffs and final updated CI/diff evidence.

## Nonclaims and deferral rule

No public deployment, production security guarantee or license clearance is asserted.

This is a **repository-only durable follow-up**, not a live website concept, canonical catalog ID or a new executable implementation. Keep status open until the specified review produces evidence; if the requirement is rejected or waived, record the responsible owner and decision rather than silently deleting the work package. The current [Phase 10 release no-go review](../16-phase-10-release-readiness.md) remains in force.

## Knowledge-development delivery and evidence split

**Canonical knowledge:** [New substantive guidance](../../../governance/quality-gates.md#static-visual-catalog-hosting-supply-chain-and-preview-security-gate). A host/base-path, CSP/iframe, locked dependency, license, release and rollback governance checklist is authored. No host or CSP has been configured and no security/license review signed off.

**Context and research ledger:** [Five context-gathered knowledge packages](../20-knowledge-development-batches.md). This work package remains open only for the outstanding observed evidence, implementation or human decision—not because the guidance is still missing.
