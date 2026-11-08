/* Deterministic synthetic Button scenarios. No product API, real identity or writes. */
(function (scope) {
  "use strict";
  scope.CatalogScenarios = Object.freeze([
    Object.freeze({ id: "default", label: "Default action", config: Object.freeze({ label: "Save changes", variant: "primary" }) }),
    Object.freeze({ id: "secondary", label: "Secondary action", config: Object.freeze({ label: "Cancel", variant: "secondary" }) }),
    Object.freeze({ id: "danger", label: "Destructive style", config: Object.freeze({ label: "Delete draft", variant: "danger" }) }),
    Object.freeze({ id: "pending", label: "Pending action", config: Object.freeze({ label: "Saving…", loading: true }) }),
    Object.freeze({ id: "disabled", label: "Unavailable action", config: Object.freeze({ label: "Submit", disabled: true }) }),
    Object.freeze({ id: "long", label: "Long translated-like label", config: Object.freeze({ label: "Save changes to this workspace and notify everyone involved" }) })
  ]);
})(globalThis);
