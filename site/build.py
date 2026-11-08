#!/usr/bin/env python3
"""Generate static, accessible catalog pages from the canonical repository files."""
import argparse
import html
import json
import re
import shutil
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(__file__).resolve().parent
REPO = "https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/blob/main/"
CATEGORIES = ("components", "patterns", "features", "foundations", "architecture", "guidance", "governance", "other")
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
HEAD = re.compile(r"^(#{1,6})\s+(.+)$")
ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s+(.+)$")


def category(item):
    first = PurePosixPath(item["path"]).parts[0]
    return first if first in CATEGORIES else "other"


def route(item):
    segment = item["id"].split(".", 1)[-1].lower()
    slug = re.sub(r"[^a-z0-9-]+", "-", segment).strip("-")
    if not slug:
        raise ValueError("Invalid canonical ID: " + item["id"])
    return "/catalog/" + category(item) + "/" + slug + "/"


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
            out.append('<pre><code class="language-' + language + '">' + html.escape("\n".join(code)) + "</code></pre>")
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
            out.append('<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table><thead><tr>')
            out.extend('<th scope="col">' + inline(h, source, by_path) + "</th>" for h in headers)
            out.append("</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>")
                out.extend("<td>" + inline(cells[j] if j < len(cells) else "", source, by_path) + "</td>" for j in range(len(headers)))
                out.append("</tr>")
                i += 1
            out.append("</tbody></table></div>")
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
    nav = "".join('<a href="' + url + '"' + (' aria-current="page" class="active"' if name == active else "") + ">" + label + "</a>"
                  for url, label, name in (("/", "Home", "home"), ("/catalog/", "Browse", "browse"), ("/search/", "Search", "search")))
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="color-scheme" content="light dark"><title>' + html.escape(title) + ' | UI/UX Design Catalog</title>'
            '<link rel="stylesheet" href="/assets/styles.css"><script defer src="/assets/search.js"></script></head><body>'
            '<a class="skip" href="#main">Skip to main content</a><header class="topbar"><div class="topbar-inner">'
            '<a class="brand" href="/"><span class="mark" aria-hidden="true">◈</span>UI/UX <strong>Catalog</strong></a>'
            '<nav aria-label="Primary">' + nav + '</nav><a class="repo" href="https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog">Repository ↗</a></div></header>'
            '<main id="main" class="container"><div class="intro"><p class="eyebrow">DESIGN KNOWLEDGE / REFERENCE</p><h1>' +
            html.escape(title) + '</h1><p class="subtitle">' + html.escape(subtitle) + '</p></div>' + content +
            '</main><footer>Canonical knowledge comes from Markdown and the registry. Interactive previews are labeled separately. '
            '<a href="https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/blob/main/CONTRIBUTING.md">Contributing</a>.</footer></body></html>')


def write(out, url, content):
    file = out / url.lstrip("/") / "index.html"
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")


def card(e):
    terms = " ".join([e["id"], e["title"], e["summary"], *e["aliases"], *e["domains"], *e.get("capabilities", [])]).lower()
    return ('<article class="card" data-category="' + category(e) + '" data-search="' + html.escape(terms, quote=True) +
            '"><a href="' + route(e) + '"><span class="category">' + category(e).title() + '</span><h3>' +
            html.escape(e["title"]) + '</h3><p>' + html.escape(e["summary"]) +
            '</p><span class="card-foot"><code>' + html.escape(e["id"]) + '</code><span aria-hidden="true">↗</span></span></a></article>')


def build(out):
    entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
    by_path = {e["path"]: e for e in entries}
    if len(by_path) != len(entries) or len({route(e) for e in entries}) != len(entries):
        raise ValueError("Duplicate canonical path or visual route")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(SITE / "static", out / "assets")
    ordered = sorted(entries, key=lambda e: (CATEGORIES.index(category(e)), e["title"]))
    cards = "".join(card(e) for e in ordered)
    chips = "".join('<button class="chip" type="button" data-filter="' + cat + '" aria-pressed="' +
                    ("true" if cat == "all" else "false") + '">' + cat.title() + "</button>" for cat in ("all", *CATEGORIES))
    tools = ('<section class="tools"><label for="catalog-filter">Search concepts</label>'
             '<input id="catalog-filter" type="search" placeholder="Search by task, name or capability" autocomplete="off">'
             '<div class="chips" aria-label="Filter categories">' + chips + '</div>'
             '<p class="count" id="result-count" role="status">' + str(len(entries)) + ' concepts</p></section>')
    grid = '<section id="entry-grid" class="grid" aria-label="Catalog entries">' + cards + '</section><p id="empty-results" hidden>No matching concepts.</p>'
    write(out, "/catalog/", page("Explore the catalog", "Browse the canonical components, patterns and design guidance.", tools + grid))
    write(out, "/search/", page("Find the right guidance", "Search by name, user task or canonical ID.", tools + '<p class="hint">Without JavaScript, all entries remain listed below. Agents can search the JSON registry directly.</p>' + grid, "search"))
    write(out, "/", page("Make better interfaces, deliberately.", "A visual, searchable and agent-readable design knowledge base. Live examples will appear only when actually implemented.",
        '<div class="actions"><a class="primary" href="/catalog/">Browse ' + str(len(entries)) + ' concepts →</a><a href="/search/">Search by task</a></div>'
        '<section class="benefits"><div><h2>Canonical knowledge</h2><p>One registry and source of design guidance.</p></div>'
        '<div><h2>Real reference source</h2><p>Future previews render source-controlled examples.</p></div>'
        '<div><h2>Agent-friendly</h2><p>Stable IDs, readable pages and source links.</p></div></section>', "home"))
    records = []
    for e in entries:
        canonical = ROOT / e["path"]
        if not canonical.is_file():
            raise FileNotFoundError(e["path"])
        info = ('<section class="meta" aria-label="Concept metadata"><div><span>Canonical ID</span><code>' + html.escape(e["id"]) +
                '</code></div><div><span>Knowledge layer</span>' + html.escape(e["layer"]) + '</div><div><span>Artifact type</span>' +
                html.escape(e["kind"]) + '</div><div><span>Review status</span><strong>' + html.escape(e["status"]) + '</strong></div></section>')
        preview = ('<section class="spec"><span class="spec-icon" aria-hidden="true">▧</span><div><h2>' +
                   ("Reference registered" if e.get("implementation") else "Specification only") + '</h2><p>' +
                   ("This Phase 3 site does not render interactive examples yet." if e.get("implementation") else
                    "No working reference implementation is registered. This content documents design guidance, not tested UI.") + '</p></div></section>')
        refs = set(e.get("related", []) + e.get("depends_on", []))
        rel = [r for r in entries if r["id"] in refs]
        related = ('<section class="related"><h2>Related guidance</h2><div>' +
                   "".join('<a href="' + route(r) + '">' + html.escape(r["title"]) + ' ↗</a>' for r in rel) +
                   '</div></section>') if rel else ""
        src = REPO + quote(e["path"], safe="/-_.")
        body = ('<p class="breadcrumb"><a href="/catalog/">Catalog</a> / ' + category(e).title() + '</p>' + info + preview +
                '<div class="doc-grid"><article class="markdown" aria-label="Canonical guidance">' +
                render_md(canonical.read_text(encoding="utf-8"), e["path"], by_path) +
                '</article><aside><h2>Source of truth</h2><p>These contracts are maintained in the repository.</p>'
                '<a href="' + src + '">View Markdown source ↗</a></aside></div>' + related)
        write(out, route(e), page(e["title"], e["summary"], body))
        records.append({"id": e["id"], "title": e["title"], "path": e["path"], "url": route(e),
                        "category": category(e), "summary": e["summary"], "status": e["status"],
                        "aliases": e["aliases"], "capabilities": e.get("capabilities", [])})
    (out / "catalog-search.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS:", len(entries), "canonical pages and 3 index pages generated")
    return len(entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=SITE / "dist")
    args = parser.parse_args()
    build(args.output.resolve())
