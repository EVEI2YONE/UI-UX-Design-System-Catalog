"""Composable, accessible page shell and discovery views.

Purpose: build navigation, metadata, cards and task entry points from read-only data.
Context: used by site/build.py at static generation; no backend, auth or writes.
Relevance: one consistent shell lets users distinguish concept type, review
maturity and whether an interactive example exists.
"""
import html

NAV = (("/", "Home", "home"), ("/tasks/", "Tasks", "tasks"),
       ("/catalog/", "Browse", "browse"), ("/search/", "Search", "search"))


def navigation(active):
    return "".join('<a href="' + url + '"' +
                   (' aria-current="page" class="active"' if key == active else "") +
                   ">" + label + "</a>" for url, label, key in NAV)


def resource_kind(entry):
    return {
        "guideline": "Guideline", "contract": "Contract", "policy": "Policy",
        "checklist": "Checklist", "specification": "Specification",
        "example": "Example",
    }.get(entry["kind"], entry["kind"].title())


def implementation_label(entry):
    return "Interactive reference available" if entry.get("implementation") else "No runnable reference"


def concept_metadata(entry):
    fields = (("Canonical ID", entry["id"]), ("Knowledge layer", entry["layer"]),
              ("Resource type", resource_kind(entry)), ("Review status", entry["status"]),
              ("Implementation", implementation_label(entry)))
    cells = []
    for label, value in fields:
        display = ("<code>" + html.escape(value) + "</code>") if label == "Canonical ID" else ("<strong>" + html.escape(value) + "</strong>")
        cells.append("<div><span>" + html.escape(label) + "</span>" + display + "</div>")
    return '<section class="meta" aria-label="Concept metadata">' + "".join(cells) + "</section>"


def concept_card(entry, category, url, terms):
    available = "true" if entry.get("implementation") else "false"
    return ('<article class="card" data-interactive="' + available + '" data-category="' +
            html.escape(category, quote=True) + '" data-search="' + html.escape(terms, quote=True) +
            '"><a href="' + html.escape(url, quote=True) + '"><span class="category">' +
            html.escape(category.title()) + '</span><h3>' + html.escape(entry["title"]) +
            '</h3><p>' + html.escape(entry["summary"]) +
            '</p><span class="availability">' + html.escape(resource_kind(entry)) +
            ' · ' + html.escape(implementation_label(entry)) +
            '</span><span class="card-foot"><code>' + html.escape(entry["id"]) +
            '</code><span aria-hidden="true">↗</span></span></a></article>')


def task_index(tasks, routes):
    cards = []
    for task in tasks:
        refs = [task["primary_id"], *task.get("related_ids", [])]
        related = ", ".join('<a href="' + html.escape(routes[ref], quote=True) + '">' +
                            html.escape(ref) + '</a>' for ref in refs)
        cards.append('<article class="task-card"><p class="task-category">' +
                     html.escape(task["group"]) + '</p><h2><a href="' +
                     html.escape(routes[task["primary_id"]], quote=True) + '">' +
                     html.escape(task["title"]) + '</a></h2><p>' +
                     html.escape(task["summary"]) + '</p><p class="task-related"><strong>Use with:</strong> ' +
                     related + '</p></article>')
    return '<section class="task-grid" aria-label="Find guidance by user task">' + "".join(cards) + '</section>'
