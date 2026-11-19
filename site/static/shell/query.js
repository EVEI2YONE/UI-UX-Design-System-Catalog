/* Deterministic, read-only browser discovery. Mirror the CLI's exact-ID/alias/task ranking. */
(function () {
  "use strict";
  function normalize(value) {
    return String(value || "").toLocaleLowerCase().replace(/_/g, " ").replace(/[^\p{L}\p{N}]+/gu, " ").trim().replace(/\s+/g, " ");
  }
  function terms(value) { return normalize(value).split(" ").filter(Boolean); }
  function matches(haystack, queryTerms) {
    var searchable = normalize(haystack);
    return queryTerms.every(function (term) { return searchable.includes(term); });
  }
  function phrases(value) { return String(value || "").split("|").map(normalize).filter(Boolean); }
  function rank(entry, query) {
    var q = normalize(query);
    if (!q) return 0;
    var id = normalize(entry.id), title = normalize(entry.title);
    var aliases = phrases(entry.aliases), primary = phrases(entry.primaryTasks), related = phrases(entry.relatedTasks);
    if (id === q) return 100;
    if (aliases.includes(q)) return 90;
    if (title === q) return 80;
    if (primary.includes(q)) return 85;
    if (related.includes(q)) return 35;
    if (!matches(entry.search, terms(q))) return -1;
    if (title.includes(q)) return 70;
    if (aliases.some(function (alias) { return alias.includes(q); })) return 60;
    if (id.includes(q)) return 55;
    return 10;
  }
  var api = { normalize: normalize, terms: terms, matches: matches, rank: rank };
  if (typeof window !== "undefined") window.CatalogQuery = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
}());
