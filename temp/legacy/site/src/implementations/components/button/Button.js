/* Actual native-button reference implementation, not the site catalog chrome.
 * Contract: components/button/spec.md. Browser module API: CatalogReference.mount.
 */
(function (scope) {
  "use strict";
  function mount(container, options) {
    if (!container || typeof container.replaceChildren !== "function") {
      throw new TypeError("Button requires a DOM container");
    }
    const config = Object.assign({
      label: "Save changes", variant: "primary", size: "medium",
      disabled: false, loading: false, onActivate: function () {}
    }, options || {});
    if (!["primary", "secondary", "danger"].includes(config.variant)) {
      throw new TypeError("Unknown button variant");
    }
    if (!["small", "medium", "large"].includes(config.size)) {
      throw new TypeError("Unknown button size");
    }
    const button = document.createElement("button");
    button.type = "button";
    button.className = "reference-button reference-button--" + config.variant +
      " reference-button--" + config.size;
    button.disabled = Boolean(config.disabled || config.loading);
    button.textContent = config.label;
    if (config.loading) {
      button.setAttribute("aria-disabled", "true");
      button.setAttribute("aria-describedby", "button-progress");
      const state = document.createElement("span");
      state.id = "button-progress";
      state.className = "reference-button-status";
      state.setAttribute("role", "status");
      state.textContent = "Action in progress";
      container.replaceChildren(button, state);
    } else {
      container.replaceChildren(button);
    }
    button.addEventListener("click", function () {
      if (!button.disabled) config.onActivate();
    });
    return button;
  }
  scope.CatalogReference = Object.freeze({ mount: mount });
})(globalThis);
