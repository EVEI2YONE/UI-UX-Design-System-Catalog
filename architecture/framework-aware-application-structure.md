# Framework-aware application structure and route ownership

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** pending

## Batch 17 context-first coverage audit

[Application selection](application-architecture.md) gives complexity-based profiles; [module boundaries](module-boundaries-and-developer-navigation.md) defines feature/domain/shared ownership; [evolution](architecture-evolution.md) covers safe migration. The missing knowledge is **adapting those profiles to frameworks where file location or filename has runtime meaning**. An illustrative `src/app/routes/` architecture can be harmful when interpreted as a required location in a framework with its own routing rules.

Before recommending a structure, inspect and record: pinned repository revision, framework/version, routing mode, actual route and layout conventions, data-loading and mutation mechanisms, server/client execution boundaries, current feature and shared imports, nested layout behavior, deep links, tests and existing conventions. **Do not select a framework from a generic architecture diagram.**

## Invariants that apply across frameworks

- Keep the framework's special routing, bootstrap and configuration files where its documented mechanism expects them.
- Treat a route as an entry adapter for the user journey, not automatically the owner of all reusable domain logic.
- Colocate route-exclusive presentation, tests and styles when the router permits it; promote code outside a route only when multiple contexts actually consume it or ownership requires it.
- Domain invariants and reusable UI contracts remain discoverable via feature/domain/shared ownership, regardless of routing shape.
- Only create `api/`, `hooks/`, `state/` and similar subfolders when there is enough owned code to warrant them.
- Protect path, params, deep links, layout hierarchy, pending/error behavior, permissions, accessibility focus and server/client execution behavior during moves.

## Framework mapping examples

Illustrative trees demonstrate ownership, **not** copy-paste starter templates or version-independent syntax.

### Next.js App Router

```text
src/
  app/
    (workspace)/
      projects/
        page.tsx              # route entry
        loading.tsx           # route loading UI if appropriate
  features/
    projects/
      ProjectList.tsx
      project-actions.ts
      index.ts
  shared/
    ui/
```

The App Router uses filesystem-defined route segments and special files. Parenthesized route groups organize routes without adding segments to URLs; they can also influence layout boundaries. Next.js permits colocating project files within route segments, so `features/` outside `app/` is an **option**, not a Next.js requirement. Choose route colocation for route-only code, and an external feature when multiple routes actually share an owner. Keep server-only code out of client imports; check current Next.js official runtime and file conventions before moving components. Do not suggest moving `page.tsx` into an arbitrary feature tree or treating `(group)` as a URL segment.

Source: [Next.js App Router route groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups) and [Next.js project organization](https://nextjs.org/docs/app/getting-started/project-structure).

### Angular

```text
src/
  main.ts
  app/
    projects/
      project-list/
        project-list.ts
        project-list.html
        project-list.css
        project-list.spec.ts
      project-data.ts
    shared/
      ui/
```

Angular's official style guide favors organizing by feature area, colocating related component files and tests, and avoiding large top-level folders grouped only by code type. Do not force a React-style `features/projects/hooks/` tree onto Angular; respect Angular's component, template and dependency-injection conventions. Keep files named consistently with the project's prevailing style and the Angular guide.

Source: [Angular style guide](https://angular.dev/style-guide).

### React Router (framework mode)

```text
app/
  root.tsx
  routes.ts                 # route configuration
  routes/
    projects/
      route.tsx             # if using supported file-route conventions
      project-form.tsx
      project-data.server.ts
  features/
    projects/
      project-rules.ts
```

React Router supports route configuration; its optional file-route conventions use `@react-router/fs-routes` and route modules can live in folders alongside route-owned helpers. **Do not assume file routing is enabled** or that every `app/routes` file must become a route regardless of configuration. Prefer colocated route-only files when supported; share stable business logic through explicit feature APIs.

Source: [React Router file-route conventions](https://reactrouter.com/how-to/file-route-conventions).

### Other UI frameworks and native apps

For Vue, SvelteKit, Nuxt, Remix-derived systems, mobile or desktop applications, **inspect official framework/platform rules at the target version before generating a proposed tree**. Preserve required route/platform entry points and map the same ownership decisions to native conventions. This batch does not claim validated recipes for frameworks it has not researched.

## Route-local versus feature-shared decision

| Situation | Recommended owner | Why |
| --- | --- | --- |
| A card used only on one page | Route-local component | Maximum locality, no premature public API |
| Shared project editor across several routes | `projects` feature | One workflow contract and consumer boundary |
| Shared accessible Dialog shell | Shared UI / design system | Stable semantics and focus contract |
| Business rule used by project approval and billing | Explicit domain owner, when semantics agree | Avoid divergent invariants |
| Loading/error UI tied to a particular router boundary | Router's supported convention | Retain route lifecycle semantics |
| Authorization and mutation checks | Server/domain/service boundary | A client-side folder convention is not a security boundary |

## Migration acceptance and anti-patterns

Inventory URLs and route hierarchy; capture navigation, deep links, layouts, loading/error/not-found, route data and mutation flows, SSR/client boundaries, focus/keyboard behavior and locale/theme states. Move one route/feature at a time; use compatibility exports only as needed; run framework-specific build, routing and integration tests; retain rollback instructions.

**Anti-pattern:** copy a generic `src/app/routes/` diagram into a Next.js project, moving special files and changing page URLs while calling the refactor structural only.

**Better:** preserve `app/.../page.tsx` as a thin route adapter while extracting reusable project workflow code into its existing or newly justified owner, checking before/after route behavior.

## Evidence and limitations

Sources are official framework guides consulted 2026-11-07. Conventions can change across framework releases and optional router modes; re-check the applicable version at implementation time. No target application was audited or migrated. Example file structures are proposed and do not demonstrate build, performance, accessibility or DX improvements.
