#!/usr/bin/env python3
"""Generate static, accessible catalog pages from the canonical repository files."""
import argparse
import html
import json
import os
import re
import shutil
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from catalog.core.navigation import CATEGORIES as CORE_CATEGORIES, category as core_category, route as core_route
from catalog.core.discovery import load_tasks, validate_tasks, terms_by_concept
from shell.components import navigation, concept_card, concept_metadata, task_index
def source_repo_url(reference):
    """Build a repository source link for a reviewed branch or immutable SHA."""
    if (not isinstance(reference, str) or not reference or
            not re.fullmatch(r"[A-Za-z0-9._/-]+", reference) or
            reference.startswith(("/", ".")) or ".." in PurePosixPath(reference).parts):
        raise ValueError("Unsafe source revision")
    return ("https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/blob/" +
            quote(reference, safe="/-_.") + "/")


REPO = source_repo_url(os.environ.get("CATALOG_SOURCE_REF", "main"))
CATEGORIES = CORE_CATEGORIES
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
HEAD = re.compile(r"^(#{1,6})\s+(.+)$")
ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s+(.+)$")


def category(item):
    """Return stable, concept-ID-based category from the catalog shell."""
    return core_category(item)


def route(item):
    """Return a stable public URL independent of source file placement."""
    return core_route(item)


def target_url(target, source, by_path):
    parsed = urlparse(html.unescape(target.strip()))
    if parsed.scheme in ("http", "https", "mailto"):
        return target
    if parsed.scheme or target.startswith(("//", "/", "\\")):
        return None
    if not parsed.path:
        return "#" + quote(parsed.fragment, safe="-_") if parsed.fragment else None
    parts = []
    for part in (PurePosixPath(source).parent / parsed.path).parts:
        if part == "..":
            if not parts:
                return None
            parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    path = "/".join(parts)
    url = route(by_path[path]) if path in by_path else REPO + quote(path, safe="/-_.")
    return url + ("#" + quote(parsed.fragment, safe="-_") if parsed.fragment else "")


def inline(text, source, by_path):
    replacements = []
    def insert(markup):
        mark = "CATALOGPLACEHOLDER" + str(len(replacements)) + "TOKEN"
        replacements.append((mark, markup))
        return mark
    def linked(match):
        url = target_url(match.group(2), source, by_path)
        label = html.escape(match.group(1))
        return insert('<a href="' + html.escape(url, quote=True) + '">' + label + "</a>") if url else label
    text = LINK.sub(linked, text)
    text = re.sub(r"\x60([^\x60\n]+)\x60", lambda m: insert("<code>" + html.escape(m.group(1)) + "</code>"), text)
    text = html.escape(text)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    for mark, markup in replacements:
        text = text.replace(mark, markup)
    return text


def public_guidance(content, source, by_path):
    """Render concept-first source Markdown without silently hiding its prose."""
    return render_md(content, source, by_path)


def render_md(content, source, by_path):
    lines = content.replace("\r\n", "\n").split("\n")
    out, anchors, i = [], set(), 0
    fence = chr(96) * 3
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith(fence):
            language = re.sub(r"[^a-z0-9_-]", "", line.strip()[3:].split(" ")[0].lower())
            code = []
            i += 1
            while i < len(lines) and not lines[i].lstrip().startswith(fence):
                code.append(lines[i])
                i += 1
            i += 1
            # Focusable so long code lines can be scrolled with the keyboard on narrow screens.
            out.append('<pre tabindex="0"><code class="language-' + language + '">' + html.escape("\n".join(code)) + "</code></pre>")
            continue
        heading = HEAD.match(line)
        if heading:
            level, title = min(len(heading.group(1)) + 1, 6), heading.group(2)
            anchor = re.sub(r"[^a-z0-9-]", "-", title.lower().replace(" ", "-")).strip("-") or "section"
            base, n = anchor, 1
            while anchor in anchors:
                n += 1
                anchor = base + "-" + str(n)
            anchors.add(anchor)
            out.append('<h' + str(level) + ' id="' + anchor + '">' + inline(title, source, by_path) + '</h' + str(level) + '>')
            i += 1
            continue
        if line.strip() == "---":
            out.append("<hr>")
            i += 1
            continue
        if line.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i][1:].strip())
                i += 1
            out.append("<blockquote><p>" + inline(" ".join(block), source, by_path) + "</p></blockquote>")
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.fullmatch(r"[\s:|\-]+", lines[i + 1]) and "---" in lines[i + 1]:
            headers = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append('<div class="table-wrap"><p class="table-hint" aria-hidden="true">Scroll sideways for more columns <span>→</span></p>'
                       '<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table><thead><tr>')
            out.extend('<th scope="col">' + inline(h, source, by_path) + "</th>" for h in headers)
            out.append("</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>")
                out.extend("<td>" + inline(cells[j] if j < len(cells) else "", source, by_path) + "</td>" for j in range(len(headers)))
                out.append("</tr>")
                i += 1
            out.append("</tbody></table></div></div>")
            continue
        m = ITEM.match(line)
        if m:
            ordered = m.group(1).endswith(".")
            tag = "ol" if ordered else "ul"
            out.append("<" + tag + ">")
            while i < len(lines):
                item = ITEM.match(lines[i])
                if not item or item.group(1).endswith(".") != ordered:
                    break
                val = item.group(2)
                if val.startswith(("[ ] ", "[x] ", "[X] ")):
                    val = ("☑ " if val[1].lower() == "x" else "☐ ") + val[4:]
                out.append("<li>" + inline(val, source, by_path) + "</li>")
                i += 1
            out.append("</" + tag + ">")
            continue
        block = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not (HEAD.match(lines[i]) or ITEM.match(lines[i]) or lines[i].lstrip().startswith((fence, "|", ">")) or lines[i].strip() == "---"):
            block.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(block), source, by_path) + "</p>")
    return "\n".join(out)


def page(title, subtitle, content, active="browse"):
    nav = navigation(active)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="color-scheme" content="light dark"><title>' + html.escape(title) + ' | UI/UX Design Catalog</title>'
            '<link rel="stylesheet" href="/assets/styles.css"><link rel="stylesheet" href="/assets/shell/shell.css"><script defer src="/assets/shell/query.js"></script><script defer src="/assets/search.js"></script></head><body>'
            '<a class="skip" href="#main">Skip to main content</a><header class="topbar"><div class="topbar-inner">'
            '<a class="brand" href="/"><span class="mark" aria-hidden="true">◈</span>UI/UX <strong>Catalog</strong></a>'
            '<nav aria-label="Primary">' + nav + '</nav><a class="repo" href="https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog">Repository ↗</a></div></header>'
            '<main id="main" class="container"><div class="intro"><p class="eyebrow">DESIGN KNOWLEDGE / REFERENCE</p><h1>' +
            html.escape(title) + '</h1><p class="subtitle">' + html.escape(subtitle) + '</p></div>' + content +
            '</main><footer>Canonical knowledge comes from Markdown and the registry; no executable UI library is shipped. '
            '<a href="https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/blob/main/CONTRIBUTING.md">Contributing</a>.</footer></body></html>')


def write(out, url, content):
    file = out / url.lstrip("/") / "index.html"
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")


TASK_LOOKUP = []


def card(e, task_terms=None):
    """Generate an accessible resource card using semantic kind and task aliases."""
    terms = " ".join([e["id"], e["title"], e["summary"], *e["aliases"], *e["domains"],
                      *e.get("capabilities", []), *(task_terms or {}).get(e["id"], [])]).lower()
    return concept_card(e, category(e), route(e), terms,
                        [v for task in TASK_LOOKUP for v in [task["title"], *task["intent_phrases"]] if task["primary_id"] == e["id"]],
                        [v for task in TASK_LOOKUP for v in [task["title"], *task["intent_phrases"]] if e["id"] in task.get("related_ids", [])])


STATES_HEADING = re.compile(
    r"^state\b|\bstates\b|\bstate\s+(?:model|matrix|contract|lifecycle|inventory)\b|\bstate$", re.I)
GENERATED_IDS = ("doc-guidance", "doc-states", "doc-source")


def section_navigation(guidance):
    """Return (guidance_html, nav_html) linking only sections that exist on the page."""
    ids = re.findall(r'\bid="([^"]+)"', guidance)
    clash = set(ids) & set(GENERATED_IDS)
    if clash or len(ids) != len(set(ids)):
        raise ValueError("Duplicate or reserved guidance anchor: " + ", ".join(sorted(clash) or ids))
    states = None
    for match in re.finditer(r'<h([23]) id="([^"]+)">(.*?)</h\1>', guidance):
        if STATES_HEADING.search(re.sub(r"<[^>]+>", "", html.unescape(match.group(3))).strip()):
            states = match.group(2)  # reuse the existing Markdown heading anchor
            break
    if states is None:
        table = re.search(r'<div class="table-wrap">(?=(?:(?!</thead>).)*?<th scope="col">States?</th>)', guidance, re.S)
        if table:
            states = "doc-states"
            # Keep the existing fragment on the wrapper; name its target and the focusable
            # scroll region without changing the document's other table landmarks.
            table_html = guidance[table.end():].replace(
                'role="region" aria-label="Scrollable table"',
                'role="region" aria-label="States table"', 1)
            guidance = (guidance[:table.start()] +
                        '<div class="table-wrap" id="doc-states" tabindex="-1" role="region" aria-label="States">' +
                        table_html)
    links = [("doc-guidance", "Guidance")]
    links += [(states, "States")] if states else []
    links.append(("doc-source", "Source"))
    nav = ('<nav class="jump-nav" aria-label="On this page"><span class="jump-label" aria-hidden="true">On this page</span><ul>' +
           "".join('<li><a href="#' + html.escape(anchor, quote=True) + '">' + label + '</a></li>' for anchor, label in links) +
           '</ul></nav>')
    return guidance, nav


def build(out):
    entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
    tasks = load_tasks(ROOT)
    global TASK_LOOKUP
    TASK_LOOKUP = tasks
    validate_tasks(tasks, entries)
    task_terms = terms_by_concept(tasks)
    by_path = {e["path"]: e for e in entries}
    if len(by_path) != len(entries) or len({route(e) for e in entries}) != len(entries):
        raise ValueError("Duplicate canonical path or visual route")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(SITE / "static", out / "assets")
    ordered = sorted(entries, key=lambda e: (CATEGORIES.index(category(e)), e["title"]))
    cards = "".join(card(e, task_terms) for e in ordered)
    chips = "".join('<button class="chip" type="button" data-filter="' + cat + '" aria-pressed="' +
                    ("true" if cat == "all" else "false") + '">' + cat.title() + "</button>" for cat in ("all", *CATEGORIES))
    tools = ('<section class="tools" aria-label="Search and filter concepts"><label for="catalog-filter">Search concepts</label>'
             '<input id="catalog-filter" type="search" placeholder="Search by task, name or capability" autocomplete="off" maxlength="200">'
             # Filter controls need the enhancement script; they stay hidden (not dead) without JS.
             '<div class="filter-row" id="filter-controls" hidden>'
             '<details class="filter-panel" id="category-panel" open><summary>Category: <span id="category-summary">All</span><span class="category-chevron" aria-hidden="true"></span></summary>'
             '<div class="chips" role="group" aria-label="Filter categories">' + chips + '</div></details>'
             '</div>'
             '<div class="tools-status"><p class="count" id="result-count">' + str(len(entries)) + ' concepts</p>'
             '<p class="active-filters" id="active-filters" hidden></p>'
             '<button type="button" class="reset-filters" id="reset-filters" hidden>Reset filters</button></div>'
             '<p class="visually-hidden" id="result-status" role="status" aria-live="polite" aria-atomic="true"></p>'
             '<noscript><p class="count">Filtering needs JavaScript; all ' + str(len(entries)) + ' entries are listed below.</p></noscript></section>')
    grid = ('<section id="entry-grid" class="grid" aria-label="Catalog entries">' + cards + '</section>'
            '<div id="empty-results" hidden><p>No matching concepts. Try a different task or category.</p>'
            '<button type="button" id="clear-filters">Clear search and filters</button></div>')
    write(out, "/tasks/", page("Start with a user task", "Browse by what a user needs to accomplish.",
        task_index(tasks, {entry["id"]: route(entry) for entry in entries}), "tasks"))
    write(out, "/catalog/", page("Explore the catalog", "Browse the canonical components, patterns and design guidance.", tools + grid))
    write(out, "/search/", page("Find the right guidance", "Search by name, user task or canonical ID.", tools + '<p class="hint">Without JavaScript, all entries remain listed below. Agents can search the JSON registry directly.</p>' + grid, "search"))
    write(out, "/", page("Make better interfaces, deliberately.", "A searchable reference of concepts and design guidance.",
        '<div class="actions"><a class="primary" href="/tasks/">Start with a task →</a><a href="/catalog/">Browse ' + str(len(entries)) + ' concepts</a><a href="/search/">Search the catalog</a></div>'
        '<section class="benefits"><div><h2>Canonical knowledge</h2><p>One registry and source of design guidance.</p></div>'
        '<div><h2>Clear concept contracts</h2><p>Explore decision rules, states, accessibility and source evidence.</p></div>'
        '<div><h2>Agent-friendly</h2><p>Stable IDs, readable pages and source links.</p></div></section>', "home"))
    records = []
    for e in entries:
        canonical = ROOT / e["path"]
        if not canonical.is_file():
            raise FileNotFoundError(e["path"])
        info = concept_metadata(e)
        refs = set(e.get("related", []) + e.get("depends_on", []))
        rel = [r for r in entries if r["id"] in refs]
        related = ('<section class="related"><h2>Related guidance</h2><div>' +
                   "".join('<a href="' + route(r) + '">' + html.escape(r["title"]) + ' ↗</a>' for r in rel) +
                   '</div></section>') if rel else ""
        src = REPO + quote(e["path"], safe="/-_.")
        guidance, jump = section_navigation(public_guidance(canonical.read_text(encoding="utf-8"), e["path"], by_path))
        body = ('<p class="breadcrumb"><a href="/catalog/">Catalog</a> / ' + category(e).title() + '</p>' + jump + info +
                '<div class="doc-grid"><article class="markdown" id="doc-guidance" aria-label="Canonical guidance">' + guidance +
                '</article><aside id="doc-source" aria-labelledby="doc-source-title"><h2 id="doc-source-title">Source of truth</h2>'
                '<p>These contracts are maintained in the repository.</p>'
                '<a href="' + src + '">View Markdown source ↗</a></aside></div>' + related)
        write(out, route(e), page(e["title"], e["summary"], body))
        records.append({"id": e["id"], "title": e["title"], "path": e["path"], "url": route(e),
                        "category": category(e), "summary": e["summary"], "status": e["status"],
                        "aliases": e["aliases"], "capabilities": e.get("capabilities", [])})
    (out / "catalog-search.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS:", len(entries), "canonical pages and 4 index pages generated")
    return len(entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=SITE / "dist")
    args = parser.parse_args()
    build(args.output.resolve())
