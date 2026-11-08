/* Shared runner for trusted, registry-bound reference implementations.
 * Loaded in sandboxed iframe; never receives arbitrary user source.
 */
(function (scope) {
  "use strict";
  function start() {
    const scenarios = scope.CatalogScenarios;
    const reference = scope.CatalogReference;
    const select = document.getElementById("scenario");
    const theme = document.getElementById("theme");
    const stage = document.getElementById("stage");
    const output = document.getElementById("preview-result");
    const reset = document.getElementById("reset");
    if (!Array.isArray(scenarios) || !scenarios.length ||
        !reference || typeof reference.mount !== "function" ||
        !select || !theme || !stage || !output || !reset) {
      throw new Error("Preview contract failed: missing trusted implementation, scenarios or host controls");
    }
    scenarios.forEach(function (scenario) {
      const option = document.createElement("option");
      option.value = scenario.id;
      option.textContent = scenario.label;
      select.appendChild(option);
    });
    function render() {
      const scenario = scenarios.find(function (item) { return item.id === select.value; });
      if (!scenario) throw new Error("Unknown scenario");
      document.documentElement.dataset.theme = theme.value;
      output.textContent = scenario.config.loading
        ? "Simulated pending state. No request was sent."
        : scenario.config.disabled
          ? "Action unavailable in this example."
          : "No action taken yet.";
      const config = Object.assign({}, scenario.config, {
        onActivate: function () {
          output.textContent = "Example activated. No server action was performed.";
        },
        onChange: function (value) {
          output.textContent = "Local example changed: " + String(value) + ". Nothing was saved.";
        },
        onClose: function (reason) {
          output.textContent = "Dialog closed (" + String(reason) + "). No server action was performed.";
        }
      });
      reference.mount(stage, config);
      // Changing the scenario replaces controls; restore focus to the selector
      // rather than leaving keyboard users on a detached DOM node.
    }
    select.value = scenarios[0].id;
    select.addEventListener("change", function () { render(); select.focus(); });
    theme.addEventListener("change", function () {
      // Theme switches must not reset a user-editable scenario. Keep the
      // implementation mounted and update inherited semantic theme tokens.
      document.documentElement.dataset.theme = theme.value;
    });
    reset.addEventListener("click", function () {
      select.value = scenarios[0].id;
      theme.value = "light";
      render();
      reset.focus();
    });
    render();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start, { once: true });
  } else {
    start();
  }
})(globalThis);
