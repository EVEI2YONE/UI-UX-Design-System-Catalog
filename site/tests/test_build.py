"""Build and static catalog contract tests (no browser conformance claims)."""
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

    def test_unimplemented_entries_advertise_spec_only(self):
        button = next(e for e in self.entries if e["id"] == "pattern.task-flows")
        text = (self.out / site_build.route(button).lstrip("/") / "index.html").read_text(encoding="utf-8")
        self.assertIn("Specification only", text)
        self.assertNotIn('class="interactive-preview"', text)
        self.assertIn("View Markdown source", text)

    def test_all_six_registered_control_previews(self):
        controls = [e for e in self.entries if e["id"].startswith("component.")]
        self.assertEqual(len(controls), 6)
        for entry in controls:
            with self.subTest(entry=entry["id"]):
                detail = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                frame = (self.out / "previews" / entry["id"] / "index.html").read_text(encoding="utf-8")
                original = (ROOT / entry["implementation"]["source_path"]).read_text(encoding="utf-8")
                copied = (self.out / "reference" / entry["id"] / "source.js").read_text(encoding="utf-8")
                self.assertIn('sandbox="allow-scripts"', detail)
                self.assertNotIn('sandbox="allow-scripts allow-same-origin"', detail)
                self.assertEqual(original, copied)
                self.assertIn("Inspect implementation source", detail)
                self.assertIn('src="/reference/' + entry["id"] + '/source.js"', frame)
                self.assertIn('src="/reference/' + entry["id"] + '/scenarios.js"', frame)
                self.assertTrue((self.out / "reference" / entry["id"] / "source.css").is_file())

    def test_five_composed_pattern_previews_match_canonical_registration(self):
        expected = {
            "pattern.forms", "pattern.navigation", "pattern.search-filter",
            "pattern.data-tables", "pattern.interaction-recovery"
        }
        actual = [e for e in self.entries if e["id"] in expected]
        self.assertEqual(len(actual), 5)
        for entry in actual:
            with self.subTest(entry=entry["id"]):
                impl = entry["implementation"]
                self.assertEqual(impl["status"], "reference")
                page = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                frame = (self.out / "previews" / entry["id"] / "index.html").read_text(encoding="utf-8")
                source = (ROOT / impl["source_path"]).read_text(encoding="utf-8")
                copied = (self.out / "reference" / entry["id"] / "source.js").read_text(encoding="utf-8")
                scenarios = (self.out / "reference" / entry["id"] / "scenarios.js").read_text(encoding="utf-8")
                self.assertEqual(source, copied)
                self.assertIn('sandbox="allow-scripts"', page)
                self.assertNotIn("allow-same-origin", page)
                self.assertIn("Inspect implementation source", page)
                self.assertIn("CatalogScenarios", scenarios)
                self.assertIn('src="/reference/' + entry["id"] + '/source.js"', frame)
                self.assertTrue((self.out / "reference" / entry["id"] / "source.css").is_file())

    def test_review_workspace_has_real_source_and_synthetic_adapter(self):
        feature = next(e for e in self.entries if e["id"] == "feature.review-workspace")
        self.assertEqual(feature["implementation"]["status"], "reference")
        page = (self.out / site_build.route(feature).lstrip("/") / "index.html").read_text(encoding="utf-8")
        frame = (self.out / "previews" / feature["id"] / "index.html").read_text(encoding="utf-8")
        directory = ROOT / "site/src/implementations/features/review-workspace"
        generated = self.out / "reference" / feature["id"]
        self.assertIn('sandbox="allow-scripts"', page)
        self.assertNotIn("allow-same-origin", page)
        self.assertIn("Inspect implementation source", page)
        self.assertIn("Inspect synthetic adapter source", page)
        self.assertEqual((directory / "ReviewWorkspace.js").read_bytes(), (generated / "source.js").read_bytes())
        self.assertEqual((directory / "mock-adapter.js").read_bytes(), (generated / "mock-adapter.js").read_bytes())
        self.assertEqual((directory / "scenarios.js").read_bytes(), (generated / "scenarios.js").read_bytes())
        self.assertIn('src="/reference/feature.review-workspace/mock-adapter.js"', frame)
        self.assertIn('src="/reference/feature.review-workspace/source.js"', frame)
        self.assertIn("Synthetic interactive reference", frame)

    def test_all_unimplemented_entries_stay_spec_only(self):
        for entry in self.entries:
            if "implementation" in entry:
                continue
            with self.subTest(entry=entry["id"]):
                page = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
                self.assertIn("Specification only", page)
                self.assertNotIn('sandbox="allow-scripts"', page)

    def test_button_real_preview_matches_registered_source(self):
        entry = next(e for e in self.entries if e["id"] == "component.button")
        self.assertEqual(entry["implementation"]["status"], "reference")
        text = (self.out / site_build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
        frame = (self.out / "previews/component.button/index.html").read_text(encoding="utf-8")
        src = (ROOT / entry["implementation"]["source_path"]).read_text(encoding="utf-8")
        rendered = (self.out / "reference/component.button/source.js").read_text(encoding="utf-8")
        scenarios = (self.out / "reference/component.button/scenarios.js").read_text(encoding="utf-8")
        self.assertIn('sandbox="allow-scripts"', text)
        self.assertNotIn('allow-same-origin', text)
        self.assertIn("Inspect implementation source", text)
        self.assertIn("Interactive example", text)
        self.assertEqual(src, rendered)
        self.assertIn("CatalogReference", src)
        self.assertIn("CatalogScenarios", scenarios)
        self.assertIn('src="/reference/component.button/source.js"', frame)
        self.assertIn('src="/reference/component.button/scenarios.js"', frame)
        self.assertIn('src="/assets/preview-runner.js"', frame)

    def test_preview_runner_assets_and_isolated_host(self):
        self.assertTrue((self.out / "assets/preview-runner.js").is_file())
        self.assertTrue((self.out / "assets/preview-host.css").is_file())
        text = (self.out / "previews/component.button/index.html").read_text(encoding="utf-8")
        for label in ("Scenario", "Theme", "Reset example", "High contrast"):
            self.assertIn(label, text)
        self.assertNotIn("https://", text)

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
        self.assertIn("Interactive example", button)
        self.assertIn("icon-only", button.lower())
        guidance = (self.out / "catalog/patterns/forms/index.html").read_text(encoding="utf-8")
        self.assertNotIn("Phase 6 executable pattern reference", guidance)
        self.assertIn("complex forms", guidance.lower())

    def test_canonical_markdown_and_historical_anchors_are_preserved(self):
        path = ROOT / "components/button/spec.md"
        source = path.read_text(encoding="utf-8")
        self.assertIn("## Batch 1 extension", source)
        self.assertIn("## Phase 4 reference", source)
        rendered = site_build.public_guidance(source, "components/button/spec.md", {})
        self.assertIn("icon-only", rendered.lower())
        self.assertIn('id="batch-1-extension', rendered)
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
        docs = {"components/button/spec.md": {"id": "component.button", "path": "components/button/spec.md"}}
        body = site_build.render_md(
            "# Heading\n\nUnsafe <script>alert(1)</script>\n\n[unsafe](javascript:alert(1))\n\n[button](spec.md)\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n",
            "components/button/spec.md", docs
        )
        self.assertNotIn("<script>", body)
        self.assertNotIn('href="javascript:', body)
        self.assertIn("&lt;script&gt;", body)
        self.assertIn('/catalog/components/button/', body)
        self.assertIn("<table>", body)

    def test_routes_use_canonical_ids_not_titles(self):
        control = {"id": "component.button", "path": "components/button/spec.md", "title": "Renamed!?"}
        self.assertEqual(site_build.route(control), "/catalog/components/button/")
        self.assertEqual(site_build.category({"id": "pattern.settings", "path": "patterns/settings.md"}), "patterns")

    def test_duplicate_routes_fail_closed(self):
        existing = {"id": "component.button", "path": "components/button/spec.md"}
        duplicate = {"id": "other.button", "path": "components/another/spec.md"}
        self.assertEqual(site_build.route(existing), site_build.route(duplicate))


if __name__ == "__main__":
    unittest.main()
