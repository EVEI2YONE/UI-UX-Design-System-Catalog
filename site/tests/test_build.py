"""Build and static catalog contract tests (no browser conformance claims)."""
import html
from html.parser import HTMLParser
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent
sys.path.insert(0, str(SITE))
import build as site_build


class SiteBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.temp.name) / "public"
        cls.count = site_build.build(cls.out)
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_every_canonical_entry_has_static_page(self):
        self.assertEqual(self.count, len(self.entries))
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                page = self.out / site_build.route(entry).lstrip("/") / "index.html"
                self.assertTrue(page.is_file(), str(page))
                text = page.read_text(encoding="utf-8")
                self.assertIn(entry["id"], text)
                self.assertIn('aria-label="Canonical guidance"', text)

    def test_browse_and_search_work_without_js(self):
        browse = (self.out / "catalog/index.html").read_text(encoding="utf-8")
        search = (self.out / "search/index.html").read_text(encoding="utf-8")
        for content in (browse, search):
            self.assertEqual(content.count('class="card"'), len(self.entries))
            self.assertIn('class="skip"', content)
            self.assertIn('id="entry-grid"', content)
        self.assertIn('aria-pressed="true"', browse)

    def test_task_first_page_exposes_canonical_task_routes(self):
        tasks = (self.out / "tasks/index.html").read_text(encoding="utf-8")
        home = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Start with a user task", tasks)
        self.assertIn("Narrow a long list", tasks)
        self.assertIn("/catalog/patterns/search-filter/", tasks)
        self.assertIn("/catalog/components/dialog/", tasks)
        self.assertIn('href="/tasks/"', home)
        self.assertIn('class="skip"', tasks)

    def test_all_concepts_are_readable_without_executable_examples(self):
        self.assertFalse((self.out / "previews").exists())
        self.assertFalse((self.out / "reference").exists())
        self.assertFalse((self.out / "assets/preview-runner.js").exists())
        self.assertFalse((self.out / "assets/preview-host.css").exists())
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                self.assertNotIn("implementation", entry)
                text=(self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                self.assertIn("View Markdown source",text)
                self.assertIn('aria-label="Canonical guidance"',text)
                self.assertNotIn('data-interactive=',text)
                self.assertNotIn('class="live-preview"',text)
                self.assertNotIn("<iframe",text)
                self.assertNotIn('id="doc-example"',text)

    def test_public_site_hides_project_phase_and_batch_labels(self):
        import re
        from html.parser import HTMLParser

        class Headings(HTMLParser):
            def __init__(self):
                super().__init__()
                self.depth = 0
                self.headings = []
            def handle_starttag(self, tag, attrs):
                if tag in ("h2", "h3", "h4", "h5", "h6"):
                    self.depth += 1
            def handle_endtag(self, tag):
                if tag in ("h2", "h3", "h4", "h5", "h6"):
                    self.depth = max(0, self.depth - 1)
            def handle_data(self, data):
                if self.depth:
                    self.headings.append(data)

        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                text = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                parser = Headings()
                parser.feed(text)
                self.assertNotRegex(" ".join(parser.headings), re.compile(r"\\b(?:batch|phase)\\s*\\d+\\b", re.I))

        button = (self.out / "catalog/components/button/index.html").read_text(encoding="utf-8")
        self.assertNotIn("Phase 4 reference implementation", button)
        self.assertNotIn("Interactive example", button)
        self.assertIn("icon-only", button.lower())
        guidance = (self.out / "catalog/patterns/forms/index.html").read_text(encoding="utf-8")
        self.assertNotIn("Phase 6 executable pattern reference", guidance)
        self.assertIn("complex forms", guidance.lower())

    def test_public_pages_contain_no_visible_phase_batch_or_pr_markers(self):
        import re
        from html.parser import HTMLParser

        class VisibleText(HTMLParser):
            def __init__(self):
                super().__init__()
                self.skip = 0
                self.parts = []
            def handle_starttag(self, tag, attrs):
                if tag in ("code", "pre", "script", "style"):
                    self.skip += 1
            def handle_endtag(self, tag):
                if tag in ("code", "pre", "script", "style"):
                    self.skip = max(0, self.skip - 1)
            def handle_data(self, text):
                if self.skip == 0:
                    self.parts.append(text)

        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                html = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                parser = VisibleText()
                parser.feed(html)
                text = " ".join(parser.parts)
                self.assertNotRegex(text, re.compile(r"\\b(?:phase|batch)\\s*\\d+\\b|\\bPR\\s*#\\d+\\b", re.I))

    def test_canonical_markdown_is_current_concept_content(self):
        path = ROOT / "specifications/components/button/spec.md"
        source = path.read_text(encoding="utf-8")
        self.assertNotIn("## Batch", source)
        self.assertNotIn("## Phase", source)
        self.assertNotIn("Interactive reference", source)
        rendered = site_build.public_guidance(source, "specifications/components/button/spec.md", {})
        self.assertIn("icon-only", rendered.lower())
        self.assertNotIn("Phase 4 reference implementation", rendered)

    def test_search_export_matches_registry(self):
        records = json.loads((self.out / "catalog-search.json").read_text(encoding="utf-8"))
        self.assertEqual({r["id"] for r in records}, {e["id"] for e in self.entries})
        self.assertEqual(len({r["url"] for r in records}), len(records))
        self.assertTrue(all(r["url"].startswith("/catalog/") for r in records))

    def test_static_assets_exist(self):
        self.assertTrue((self.out / "assets/styles.css").is_file())
        self.assertTrue((self.out / "assets/search.js").is_file())
        self.assertTrue((self.out / "index.html").is_file())

    def test_markdown_escaping_and_safe_url(self):
        docs = {"specifications/components/button/spec.md": {"id": "component.button", "path": "specifications/components/button/spec.md"}}
        body = site_build.render_md(
            "# Heading\n\nUnsafe <script>alert(1)</script>\n\n[unsafe](javascript:alert(1))\n\n[button](spec.md)\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n",
            "specifications/components/button/spec.md", docs
        )
        self.assertNotIn("<script>", body)
        self.assertNotIn('href="javascript:', body)
        self.assertIn("&lt;script&gt;", body)
        self.assertIn('/catalog/components/button/', body)
        self.assertIn("<table>", body)

    def test_routes_use_canonical_ids_not_titles(self):
        control = {"id": "component.button", "path": "specifications/components/button/spec.md", "title": "Renamed!?"}
        self.assertEqual(site_build.route(control), "/catalog/components/button/")
        self.assertEqual(site_build.category({"id": "pattern.settings", "path": "specifications/patterns/settings.md"}), "patterns")

    def test_duplicate_routes_fail_closed(self):
        existing = {"id": "component.button", "path": "specifications/components/button/spec.md"}
        duplicate = {"id": "other.button", "path": "specifications/components/another/spec.md"}
        self.assertEqual(site_build.route(existing), site_build.route(duplicate))

    def test_phase3_compact_filter_markup(self):
        import re
        for name in ("catalog", "search"):
            with self.subTest(page=name):
                text = (self.out / name / "index.html").read_text(encoding="utf-8")
                # Native disclosure keeps every category chip; JS-only controls are hidden, not dead, without JS.
                self.assertIn('<details class="filter-panel" id="category-panel" open>', text)
                self.assertIn('<div class="filter-row" id="filter-controls" hidden>', text)
                self.assertEqual(len(re.findall(r'data-filter="([a-z]+)"', text)), 1 + len(site_build.CATEGORIES))
                self.assertNotIn('id="interactive-only"', text)
                self.assertIn('id="category-summary">All<', text)
                self.assertIn('<span class="category-chevron" aria-hidden="true"></span>', text)
                self.assertIn('id="active-filters" hidden', text)
                self.assertIn('id="clear-filters"', text)
                # A single polite, atomic status region; the visible count is not itself live.
                self.assertEqual(text.count('role="status"'), 1)
                self.assertIn('id="result-status" role="status" aria-live="polite" aria-atomic="true"', text)
                self.assertIn("<noscript>", text)

    def test_phase3_jump_navigation_targets_existing_unique_sections(self):
        import re
        with_states = 0
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                text = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                ids = re.findall(r'\bid="([^"]+)"', text)
                self.assertEqual(len(ids), len(set(ids)), "duplicate IDs")
                nav = re.search(r'<nav class="jump-nav" aria-label="On this page">(.*?)</nav>', text)
                self.assertIsNotNone(nav)
                links = re.findall(r'<a href="#([^"]+)">([^<]+)</a>', nav.group(1))
                labels = [label for _, label in links]
                for anchor, _ in links:
                    self.assertIn(anchor, ids, "dead jump link #" + anchor)
                self.assertEqual(labels[-1], "Source")
                self.assertIn("Guidance", labels)
                self.assertNotIn("Example", labels)
                self.assertNotIn('id="doc-example"', text)
                with_states += "States" in labels
                # Jump navigation precedes metadata and the example/spec notice.
                self.assertLess(text.index('class="jump-nav"'), text.index('class="meta"'))
        self.assertGreater(with_states, 0)
        button = (self.out / "catalog/components/button/index.html").read_text(encoding="utf-8")
        self.assertIn('<a href="#doc-states">States</a>', button)
        forms = (self.out / "catalog/patterns/forms/index.html").read_text(encoding="utf-8")
        self.assertIn('<a href="#task-flow-and-states">States</a>', forms, "reuses Markdown heading anchor")

    def test_phase3_states_table_jump_has_specific_named_region(self):
        table_pages = []
        for entry in self.entries:
            page = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
            if '<a href="#doc-states">States</a>' not in page:
                continue
            table_pages.append(entry["id"])
            with self.subTest(entry=entry["id"]):
                self.assertEqual(page.count('id="doc-states"'), 1)
                self.assertIn(
                    '<div class="table-wrap" id="doc-states" tabindex="-1" role="region" aria-label="States">',
                    page)
                target = page.split('id="doc-states"', 1)[1].split('</div></div>', 1)[0]
                self.assertIn('aria-label="States table"', target)
        self.assertGreaterEqual(len(table_pages), 11, table_pages)

        sample = site_build.render_md(
            "| State | Behavior |\n| --- | --- |\n| Idle | Ready |\n",
            "specifications/components/button/spec.md", {})
        output, links = site_build.section_navigation(sample)
        self.assertIn('href="#doc-states"', links)
        self.assertIn('aria-label="States table"', output)
        self.assertNotIn('aria-label="Scrollable table"', output)

    def test_phase3_reserved_anchor_collision_fails_closed(self):
        with self.assertRaises(ValueError):
            site_build.section_navigation('<h2 id="doc-source">Source</h2>')

    def test_phase3_tables_keep_focusable_region_and_scroll_hint(self):
        body = site_build.render_md("| A | B |\n| --- | --- |\n| 1 | 2 |\n", "specifications/components/button/spec.md", {})
        self.assertIn('<div class="table-wrap"><p class="table-hint" aria-hidden="true">', body)
        self.assertIn('<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table>', body)
        self.assertTrue(body.endswith("</table></div></div>"))
        code = site_build.render_md("```text\n" + "x" * 300 + "\n```\n", "specifications/components/button/spec.md", {})
        self.assertIn('<pre tabindex="0"><code class="language-text">', code)


if __name__ == "__main__":
    unittest.main()
