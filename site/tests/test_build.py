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
        button = next(e for e in self.entries if e["id"] == "component.input")
        text = (self.out / site_build.route(button).lstrip("/") / "index.html").read_text(encoding="utf-8")
        self.assertIn("Specification only", text)
        self.assertNotIn('class="interactive-preview"', text)
        self.assertIn("View Markdown source", text)

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
