/* Search shell: small pure helpers for progressive filtering; no fetch, persistence or global event listeners. */
(function () {
  "use strict";
  function terms(value) { return String(value || "").trim().toLocaleLowerCase().split(/\s+/).filter(Boolean); }
  function matches(haystack, termsList) {
    var text = String(haystack || "").toLocaleLowerCase();
    return termsList.every(function (term) { return text.includes(term); });
  }
  var api = { terms: terms, matches: matches };
  if (typeof window !== "undefined") window.CatalogQuery = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
}());
