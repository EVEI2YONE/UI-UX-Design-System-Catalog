/* Progressive enhancement only; all catalog entries remain visible without JS. */
(() => {
  "use strict";
  const root = document.getElementById("entry-grid");
  const search = document.getElementById("catalog-filter");
  const count = document.getElementById("result-count");
  const empty = document.getElementById("empty-results");
  if (!root || !search) return;
  const cards = Array.from(root.querySelectorAll(".card"));
  const chips = Array.from(document.querySelectorAll("[data-filter]"));
  let category = "all";
  function update() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    cards.forEach((card) => {
      const content = card.dataset.search || "";
      const matches = terms.every((term) => content.includes(term));
      const matchesCategory = category === "all" || category === card.dataset.category;
      const show = matches && matchesCategory;
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (count) count.textContent = String(visible) + " of " + String(cards.length) + " concepts";
    if (empty) empty.hidden = visible !== 0;
  }
  search.addEventListener("input", update);
  chips.forEach((button) => button.addEventListener("click", () => {
    category = button.dataset.filter || "all";
    chips.forEach((chip) => chip.setAttribute("aria-pressed", String(chip === button)));
    update();
  }));
  const params = new URLSearchParams(window.location.search);
  const initial = params.get("q");
  if (initial) search.value = initial.slice(0, 200);
  update();
})();
