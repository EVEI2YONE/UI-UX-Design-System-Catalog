"""Repeatable build-size, content-security and source integrity guards.

These are lab/build budgets, not field Web Vitals or accessibility certification.
"""
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "site"))
import build


class QualityBudgets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temp.name) / "site"
        build.build(cls.output)
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_static_boot_assets_within_baseline_budgets(self):
        assets = self.output / "assets"
        sizes = {name: (assets / name).stat().st_size for name in ("styles.css", "search.js")}
        self.assertLess(sizes["styles.css"], 32768, sizes)
        self.assertLess(sizes["search.js"], 8192, sizes)
        print("Build asset sizes (bytes):", sizes)

    def test_no_executable_preview_assets_or_frames_are_generated(self):
        self.assertFalse((self.output / "previews").exists())
        self.assertFalse((self.output / "reference").exists())
        self.assertFalse((self.output / "assets/preview-runner.js").exists())
        self.assertFalse((self.output / "assets/preview-host.css").exists())
        for entry in self.entries:
            content=(self.output / build.route(entry).lstrip("/") / "index.html").read_text(encoding="utf-8")
            with self.subTest(entry=entry["id"]):
                self.assertNotIn("<iframe",content)
                self.assertNotIn("<script>",content)
                self.assertNotIn("Inspect implementation source",content)
                self.assertIn('href="/assets/styles.css"',content)
                self.assertIn('href="https://github.com/',content)

    def test_entry_routes_are_unique_and_owned_by_canonical_registry(self):
        routes = [build.route(entry) for entry in self.entries]
        self.assertEqual(len(routes), len(set(routes)))
        self.assertEqual(len({entry["id"] for entry in self.entries}), len(self.entries))
        self.assertGreaterEqual(len(self.entries), 54)


if __name__ == "__main__":
    unittest.main()
