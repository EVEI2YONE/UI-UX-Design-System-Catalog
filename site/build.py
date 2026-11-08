#!/usr/bin/env python3
"""Generate static, accessible catalog pages from the canonical repository files."""
import argparse
import html
import json
import os
import re
import shutil
from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(__file__).resolve().parent
def source_repo_url(reference):
    """Build a repository source link for a reviewed branch or immutable SHA."""
    if (not isinstance(reference, str) or not reference or
            not re.fullmatch(r"[A-Za-z0-9._/-]+", reference) or
            reference.startswith(("/", ".")) or ".." in PurePosixPath(reference).parts):
        raise ValueError("Unsafe source revision")
    return ("https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/blob/" +
            quote(reference, safe="/-_.") + "/")


REPO = source_repo_url(os.environ.get("CATALOG_SOURCE_REF", "main"))
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


# Website copy intentionally omits repository migration history. These filters
# affect only rendered HTML; the canonical Markdown and its historical anchors
# stay intact in Git and remain accessible through the source link.
INTERNAL_REFERENCE_HEADING = re.compile(
    r"^#{2}\s+Phase\s+[4-9]\s+.*(?:reference|implementation)", re.I)
INTERNAL_STAGE = re.compile(r"\b(?:Phase|Batch)\s*\d+(?:\s*[-–]\s*\d+)?\b", re.I)
INTERNAL_PR = re.compile(r"\b(?:draft\s+)?PR\s*#\d+\b", re.I)


def public_markdown(content):
    """Hide implementation-only reference addenda, not substantive batch guidance."""
    lines = content.splitlines()
    kept, suppress = [], False
    for line in lines:
        heading = HEAD.match(line)
        if heading and len(heading.group(1)) <= 2:
            if INTERNAL_REFERENCE_HEADING.match(line):
                suppress = True
                continue
            suppress = False
        if not suppress:
            kept.append(line)
    return "\n".join(kept)


def public_label(value):
    """Convert process-oriented visible labels into lasting subject labels."""
    value = re.sub(r"^\s*(?:Batch\s*\d+\s*(?:extension|boundary)?\s*[-–—:]?\s*)", "", value, flags=re.I)
    value = re.sub(r"\s*[-–—:]?\s*(?:proposed\s+)?(?:Batch|Phase)\s*\d+\b(?:\s+proposal)?", "", value, flags=re.I)
    value = INTERNAL_STAGE.sub("catalog update", value)
    value = INTERNAL_PR.sub("repository review", value)
    value = re.sub(r"^\\s*B\\d{2}\\s*[-–—:]\\s*", "", value, flags=re.I)
    value = re.sub(r"\\b(?:CKG|KG)-\\d+(?:[-–]\\d+)?\\b", "", value, flags=re.I)
    leading = " " if value[:1].isspace() else ""
    trailing = " " if value[-1:].isspace() else ""
    cleaned = re.sub(r"\s{2,}", " ", value).strip()
    return leading + cleaned + trailing if cleaned else value


class PublicCopy(HTMLParser):
    """Edit only visible text, never hrefs, IDs, code or raw examples."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts, self.literal_depth = [], 0

    def handle_starttag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())
        if tag in ("pre", "code"):
            self.literal_depth += 1

    def handle_endtag(self, tag):
        self.parts.append("</" + tag + ">")
        if tag in ("pre", "code"):
            self.literal_depth = max(0, self.literal_depth - 1)

    def handle_startendtag(self, tag, attrs):
        self.parts.append(self.get_starttag_text())

    def handle_data(self, data):
        self.parts.append(data if self.literal_depth else public_label(data))

    def handle_entityref(self, name):
        self.parts.append("&" + name + ";")

    def handle_charref(self, name):
        self.parts.append("&#" + name + ";")

    def handle_comment(self, data):
        self.parts.append("<!--" + data + "-->")

    def clean(self, markup):
        self.feed(markup)
        self.close()
        return "".join(self.parts)


def public_guidance(content, source, by_path):
    return PublicCopy().clean(render_md(public_markdown(content), source, by_path))


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



def reference_preview(entry, out):
    """Render the exact checked-in trusted JS implementation, source, and scenarios."""
    impl = entry.get("implementation")
    if impl is None:
        return ('<section class="spec"><span class="spec-icon" aria-hidden="true">▧</span>'
                '<div><h2>Specification only</h2><p>No working reference implementation is registered. '
                'This content documents design guidance, not tested UI.</p></div></section>')
    if impl["preview_path"].rstrip("/") != route(entry).rstrip("/"):
        raise ValueError("Preview URL must match canonical entry route: " + entry["id"])
    if impl["status"] not in ("reference", "experimental", "verified"):
        raise ValueError("Unsupported preview status")
    root_impl = (ROOT / "site/src/implementations").resolve()
    source = (ROOT / impl["source_path"]).resolve()
    manifest = (ROOT / impl["scenario_manifest"]).resolve()
    if not source.is_file() or not manifest.is_file() or not source.is_relative_to(root_impl) or not manifest.is_relative_to(root_impl):
        raise ValueError("Missing/unsafe registered source or scenario manifest")
    if source.parent != manifest.parent or source.suffix != ".js" or manifest.suffix != ".js":
        raise ValueError("Preview runner requires colocated classic JavaScript references")
    name = entry["id"]
    base = out / "reference" / name
    base.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, base / "source.js")
    shutil.copyfile(manifest, base / "scenarios.js")
    # Optional, colocated, reviewed synthetic adapter for multi-step references.
    adapter = source.parent / "mock-adapter.js"
    adapter_script = ""
    adapter_view = ""
    if adapter.is_file():
        if not adapter.resolve().is_relative_to(root_impl):
            raise ValueError("Unsafe mock adapter location")
        shutil.copyfile(adapter, base / "mock-adapter.js")
        adapter_script = '<script src="/reference/' + html.escape(name, quote=True) + '/mock-adapter.js"></script>'
        adapter_view = ('<details class="source-details"><summary>Inspect synthetic adapter source</summary>'
                        '<p>In-memory fixtures only. No real authorization or persistence.</p>'
                        '<pre><code>' + html.escape(adapter.read_text(encoding="utf-8")) + '</code></pre></details>')
    stylesheet = source.with_suffix(".css")
    if stylesheet.is_file():
        shutil.copyfile(stylesheet, base / "source.css")
    else:
        raise ValueError("Preview requires colocated source CSS: " + str(stylesheet))
    frame = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
             '<meta name="viewport" content="width=device-width,initial-scale=1">'
             '<title>Interactive reference: ' + html.escape(entry["title"]) + '</title>'
             '<link rel="stylesheet" href="/assets/preview-host.css">'
             '<link rel="stylesheet" href="/reference/' + html.escape(name, quote=True) + '/source.css">'
             '</head><body><p class="note">Synthetic interactive reference · no network writes or backend authorization</p>'
             '<div class="controls"><div class="control"><label for="scenario">Scenario</label><select id="scenario"></select></div>'
             '<div class="control"><label for="theme">Theme</label>'
             '<select id="theme"><option value="light">Light</option><option value="dark">Dark</option>'
             '<option value="contrast">High contrast</option></select></div>'
             '<div class="control"><button id="reset" type="button">Reset example</button></div></div>'
             '<div class="stage"><div id="stage"></div></div>'
             '<p class="result" id="preview-result" role="status" aria-live="polite"></p>'
             '<script src="/reference/' + html.escape(name, quote=True) + '/scenarios.js"></script>'
             + adapter_script +
             '<script src="/reference/' + html.escape(name, quote=True) + '/source.js"></script>'
             '<script src="/assets/preview-runner.js"></script></body></html>')
    write(out, "/previews/" + name + "/", frame)
    source_text = html.escape(source.read_text(encoding="utf-8"))
    return ('<section class="live-preview" aria-label="Working reference preview">'
            '<div class="preview-heading"><div><p class="preview-kicker">LIVE REFERENCE · SYNTHETIC DATA</p>'
            '<h2>Interactive example</h2><p>Rendered from the actual reference source. '
            'Not a certified production component.</p></div></div>'
            '<iframe title="' + html.escape(entry["title"], quote=True) +
            ' — isolated interactive reference" src="/previews/' + html.escape(name, quote=True) +
            '/" sandbox="allow-scripts" loading="lazy" referrerpolicy="no-referrer"></iframe>'
            '<details class="source-details"><summary>Inspect implementation source</summary>'
            '<p>This is the same checked-in file loaded by the reference preview. '
            'Scenario definitions are maintained beside it.</p>'
            '<p><code>' + html.escape(impl["source_path"]) + '</code></p>'
            '<pre><code>' + source_text + '</code></pre></details>' + adapter_view + '</section>')



def build(out):
    entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
    by_path = {e["path"]: e for e in entries}
    if len(by_path) != len(entries) or len({route(e) for e in entries}) != len(entries):
        raise ValueError("Duplicate canonical path or visual route")
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copytree(SITE / "static", out / "assets")
    shutil.copyfile(SITE / "src/previews/preview-runner.js", out / "assets/preview-runner.js")
    shutil.copyfile(SITE / "src/previews/preview-host.css", out / "assets/preview-host.css")
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
    write(out, "/", page("Make better interfaces, deliberately.", "A visual, searchable design reference with interactive examples backed by real source code.",
        '<div class="actions"><a class="primary" href="/catalog/">Browse ' + str(len(entries)) + ' concepts →</a><a href="/search/">Search by task</a></div>'
        '<section class="benefits"><div><h2>Canonical knowledge</h2><p>One registry and source of design guidance.</p></div>'
        '<div><h2>Real reference source</h2><p>Explore interactive examples and inspect the code behind them.</p></div>'
        '<div><h2>Agent-friendly</h2><p>Stable IDs, readable pages and source links.</p></div></section>', "home"))
    records = []
    for e in entries:
        canonical = ROOT / e["path"]
        if not canonical.is_file():
            raise FileNotFoundError(e["path"])
        info = ('<section class="meta" aria-label="Concept metadata"><div><span>Canonical ID</span><code>' + html.escape(e["id"]) +
                '</code></div><div><span>Knowledge layer</span>' + html.escape(e["layer"]) + '</div><div><span>Artifact type</span>' +
                html.escape(e["kind"]) + '</div><div><span>Review status</span><strong>' + html.escape(e["status"]) + '</strong></div></section>')
        preview = reference_preview(e, out)
        refs = set(e.get("related", []) + e.get("depends_on", []))
        rel = [r for r in entries if r["id"] in refs]
        related = ('<section class="related"><h2>Related guidance</h2><div>' +
                   "".join('<a href="' + route(r) + '">' + html.escape(r["title"]) + ' ↗</a>' for r in rel) +
                   '</div></section>') if rel else ""
        src = REPO + quote(e["path"], safe="/-_.")
        body = ('<p class="breadcrumb"><a href="/catalog/">Catalog</a> / ' + category(e).title() + '</p>' + info + preview +
                '<div class="doc-grid"><article class="markdown" aria-label="Canonical guidance">' +
                public_guidance(canonical.read_text(encoding="utf-8"), e["path"], by_path) +
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
