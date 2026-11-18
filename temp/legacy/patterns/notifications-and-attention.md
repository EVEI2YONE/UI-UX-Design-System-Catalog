# Notifications and attention management

**Kind:** guideline · **Status:** proposed · **Primary layer:** patterns

## Purpose and ownership

Help people notice consequential changes without exhausting attention, leaking private information or disguising marketing as urgency. **Use when** deciding which events deserve in-app, email, push or background delivery and what preference controls are needed. **Avoid when** using a generic alert/toast component as an opt-in communications policy.

[Feedback and status messaging](feedback.md) owns **in-context** alert and toast presentation. This pattern owns **delivery eligibility, priority, channel, timing, deduplication and preference management**. Product and notification-service teams own real event semantics, allowed channels, frequency caps and delivery guarantees.

## Priority and channel decisions

| Event | Default design direction | Risk |
| --- | --- | --- |
| Current action succeeded/failed | In-context persistent or suitable nonblocking feedback | Duplicating the same result as push and email |
| Action requires timely response | Durable inbox plus optional urgency-appropriate channel when authorized | Interruption without relevance or actionability |
| Security-sensitive account change | Policy-owned account record and approved secure alert | Exposing identifying or private details in lock screen preview |
| Routine background activity | Grouped digest or inbox, configurable where appropriate | Notification flood |
| Low-priority update | Noninterruptive discoverable state | Manufactured urgency or engagement loops |
| Critical service failure | Reliable in-product recovery plus support channel, not toast-only | Alert vanishes before user can act |

## State lifecycle

```text
Event -> relevance and audience check -> sensitivity/urgency -> permission + app preference
  -> deduplicate and choose channel/timing -> deliver / create durable record
  -> read, dismiss, mute, act or adjust -> authorized return to task
```

- Request browser/system permission in meaningful task context and through deliberate user interaction where platforms require it. Detect unsupported and denied states; do not repeatedly nag.
- Treat **OS/browser permission**, **application categories**, **email opt-in** and **in-app inbox** as separate choices, with accurate effective state.
- Give the user a reasonable way to manage frequency, channel or category when product rules allow. Explain when nonoptional security/transactional messages differ.
- If notifications deep-link to private data, revalidate authorization and current role/session. Do not trust a previous device state.
- Avoid duplicate alerts across tabs/devices when possible; never claim exactly-once delivery without backend evidence.
- A red badge means only what the associated data actually counts (unread, outstanding, etc.). Do not confuse unread items with urgent tasks.
- Keep critical information available without requiring acceptance of push when feasible and appropriate.
- Limit sensitive lock-screen previews, and avoid presenting personal data on shared surfaces.

## Example and anti-example

**Illustrative example:** A user opts into deadline reminders for a project, selects email or browser notifications where available and can inspect the same deadline in an accessible in-app inbox. Multiple routine changes are grouped rather than sent as separate interruptions.

**Anti-example:** Permission is declined but the app repeats native prompts; promotional updates look like security alerts, and a notification preview reveals private account information.

## Accessibility, localization and recovery

- Keep notifications readable with clear action names, accessible inbox landmarks and non-push paths.
- Announce meaningful in-app events with restrained live regions; avoid competing screen-reader speech and surprise focus moves.
- Support keyboard and touch dismiss, mute, mark-as-read and settings; honor reduced motion.
- Localize categories, counts, times, time zones, date urgency and long text; check RTL.
- If a permission is denied or push unsupported, explain in-product alternatives without claiming the user can enable it inside the app.

## Verification

| Check | Status | Evidence |
| --- | --- | --- |
| Effective permissions and category preferences | NOT VERIFIED | Browser/device + backend checks |
| Relevance, deduplication, priority and timing | NOT VERIFIED | Event simulation and policy review |
| Deep links respect active auth/role | NOT VERIFIED | Security and navigation tests |
| Keyboard, screen reader, reflow and RTL | NOT VERIFIED | End-to-end task checks |
| User ability to control attention and find critical tasks | NOT VERIFIED | Research and analytics |

## Source ledger

- [MDN Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) (accessed 2026-11-07): browser permission and service-worker behavior, subject to browser capability.
- [MDN Using the Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API) (accessed 2026-11-07): permission best practices, platform limitations; not a universal product policy.
- [Apple web push](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers) (accessed 2026-11-07): Apple platform-specific constraints.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): web accessibility criteria.

**Canonical ID:** `pattern.notifications-attention` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [feedback](feedback.md), [privacy](../guidance/privacy-consent-and-trust.md), [service recovery](service-recovery-and-support.md), [content design](../guidance/content-design-and-ux-writing.md), [authentication](authentication-and-account-lifecycle.md).


## Notification preferences inside settings — account batch 3 (KG-014–015)

For each event class, expose only genuinely supported delivery channels and distinguish `on` (effective), `requested` (pending), `blocked` (browser/device permission), `ineligible` (policy), and `failed` (delivery configuration). Explicitly label mandatory security/transactional messages separately from opt-in promotions and configurable reminders.

**Contract:** event/category → user-facing purpose and optional/mandatory classification → channel choice → cadence/digest → quiet hours/timezone if offered → save state → authoritative effective setting. Quiet hours must disclose exceptions for urgent or legally required notifications; use the person's chosen timezone and handle daylight saving transitions. If the product has no digest or quiet-hours service, omit those controls rather than promising them.

**Test cases (NOT VERIFIED):** email unsubscribe scoped to category, revoked push permission, cross-device preference state, one event via multiple channels, quiet-hour boundary/DST, in-app accessibility, service outage and delayed preference propagation. Test actual delivery independently of settings-save success.

**Example:** “Weekly product digest · Email · Fridays, local time,” with the actual effective timezone and clear stop option. **Anti-example:** a universal “Mute all” switch that silently suppresses mandatory security notices or appears effective despite denied OS permission. Related: [account settings](account-and-settings-portal.md), [privacy](../guidance/privacy-consent-and-trust.md).
