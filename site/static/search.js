/* Progressive enhancement only; all catalog entries remain visible without JS. */
(() => {
  "use strict";
  // Detail pages: show the sideways-scroll hint only where a table really overflows.
  const tables = Array.from(document.querySelectorAll(".table-wrap"));
  if (tables.length) {
    const measure = () => tables.forEach((wrap) => {
      const region = wrap.querySelector(".table-scroll");
      if (region) wrap.dataset.overflow = String(region.scrollWidth > region.clientWidth + 1);
    });
    measure();
    window.addEventListener("resize", measure);
  }

  const root = document.getElementById("entry-grid");
  const search = document.getElementById("catalog-filter");
  if (!root || !search) return;
  const count = document.getElementById("result-count");
  const status = document.getElementById("result-status");
  const empty = document.getElementById("empty-results");
  const clear = document.getElementById("clear-filters");
  const reset = document.getElementById("reset-filters");
  const controls = document.getElementById("filter-controls");
  const panel = document.getElementById("category-panel");
  const summary = document.getElementById("category-summary");
  const active = document.getElementById("active-filters");
  const cards = Array.from(root.querySelectorAll(".card"));
  const originalOrder = new Map(cards.map((card, index) => [card, index]));
  const chips = Array.from(document.querySelectorAll("[data-filter]"));
  const valid = new Set(chips.map((chip) => chip.dataset.filter));
  const MAX_QUERY = 200;
  let category = "all";
  let announceTimer = 0;
  let typingTimer = 0;

  /* URL schema: q (text, <=200 chars) and category (a rendered chip value); 
     old interactive-only links are normalized to ordinary guidance search. */
  function readUrl() {
    const params = new URLSearchParams(window.location.search);
    const cat = params.get("category");
    return {
      q: (params.get("q") || "").slice(0, MAX_QUERY),
      category: cat && cat !== "all" && valid.has(cat) ? cat : "all"
    };
  }

  function stateUrl() {
    const params = new URLSearchParams(window.location.search);
    ["q", "category", "interactive"].forEach((key) => params.delete(key));
    const q = search.value.trim();
    if (q) params.set("q", q.slice(0, MAX_QUERY));
    if (category !== "all") params.set("category", category);
    const query = params.toString();
    return window.location.pathname + (query ? "?" + query : "") + window.location.hash;
  }

  /* History policy: typing replaces the current entry (debounced); deliberate actions
     (category and reset) push one entry; popstate restores without writing. */
  function cancelTyping() {
    window.clearTimeout(typingTimer);
    typingTimer = 0;
  }

  function writeUrl(mode) {
    cancelTyping();
    const next = stateUrl();
    if (next === window.location.pathname + window.location.search + window.location.hash) return;
    try {
      window.history[mode === "push" ? "pushState" : "replaceState"]({catalogFilters: true}, "", next);
    } catch (error) { /* Some sandboxed or file contexts reject history writes; filtering still works. */ }
  }

  // A deliberate action preserves pending typing in the entry before changing filters.
  function flushTyping() {
    if (typingTimer) writeUrl("replace");
  }

  function apply(state) {
    search.value = state.q;
    category = state.category;
    chips.forEach((chip) => chip.setAttribute("aria-pressed", String(chip.dataset.filter === category)));
  }

  function label(value) {
    const chip = chips.find((item) => item.dataset.filter === value);
    return chip ? chip.textContent.trim() : "All";
  }

  function update(announce) {
    let visible = 0;
    const rankings = cards.map((card) => ({
      card,
      rank: window.CatalogQuery.rank({
        id: card.dataset.id,
        title: card.dataset.title,
        aliases: card.dataset.aliases,
        primaryTasks: card.dataset.primaryTasks,
        relatedTasks: card.dataset.relatedTasks,
        search: card.dataset.search
      }, search.value)
    }));
    rankings.forEach(({card, rank}) => {
      const show = rank >= 0 && (category === "all" || category === card.dataset.category);
      card.hidden = !show;
      if (show) visible += 1;
    });
    // Restore canonical order for empty search; otherwise put exact task/alias matches first.
    rankings.sort((a, b) => b.rank - a.rank || originalOrder.get(a.card) - originalOrder.get(b.card));
    rankings.forEach(({card}) => root.appendChild(card));
    const text = String(visible) + " of " + String(cards.length) + " concepts";
    if (count) count.textContent = text;
    if (empty) empty.hidden = visible !== 0;
    const parts = [];
    if (category !== "all") parts.push(label(category));
    if (summary) summary.textContent = label(category);
    if (active) {
      active.hidden = parts.length === 0;
      active.textContent = parts.length ? parts.length + (parts.length === 1 ? " filter" : " filters") + " active: " + parts.join(", ") : "";
    }
    if (reset) reset.hidden = parts.length === 0 && !search.value.trim();
    // One polite announcement per settled change, not per keystroke.
    window.clearTimeout(announceTimer);
    if (status && announce) {
      announceTimer = window.setTimeout(() => {
        status.textContent = text + (parts.length ? ", " + parts.join(", ") : "");
      }, announce === "typing" ? 900 : 150);
    }
  }

  function resetAll() {
    flushTyping();
    apply({q: "", category: "all"});
    update("now");
    writeUrl("push");
    search.focus();
  }

  search.addEventListener("input", () => {
    update("typing");
    cancelTyping();
    typingTimer = window.setTimeout(() => writeUrl("replace"), 300);
  });
  chips.forEach((button) => button.addEventListener("click", () => {
    flushTyping();
    category = valid.has(button.dataset.filter) ? button.dataset.filter : "all";
    chips.forEach((chip) => chip.setAttribute("aria-pressed", String(chip === button)));
    update("now");
    writeUrl("push");
  }));
  clear?.addEventListener("click", resetAll);
  reset?.addEventListener("click", resetAll);
  window.addEventListener("popstate", () => { cancelTyping(); apply(readUrl()); update("now"); });

  // Compact mobile disclosure: categories start collapsed on narrow screens, open on wide ones,
  // until the person toggles the panel themselves.
  if (controls) controls.hidden = false;
  if (panel && window.matchMedia) {
    const narrow = window.matchMedia("(max-width: 600px)");
    let userToggled = false;
    panel.open = !narrow.matches;
    panel.querySelector("summary")?.addEventListener("click", () => { userToggled = true; });
    narrow.addEventListener?.("change", (event) => { if (!userToggled) panel.open = !event.matches; });
  }

  apply(readUrl());
  update(false);
  writeUrl("replace"); // canonicalize invalid or oversized values without adding history
})();
