"""Preserve canonical concept identity, not obsolete candidate paperwork."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ConceptPreservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]

    def test_exactly_one_owner_and_real_source_for_every_concept(self):
        self.assertEqual(len(self.entries), 54)
        self.assertEqual(len({e["id"] for e in self.entries}), len(self.entries))
        self.assertEqual(len({e["path"] for e in self.entries}), len(self.entries))
        for item in self.entries:
            with self.subTest(id=item["id"]):
                self.assertTrue((ROOT / item["path"]).is_file())
                self.assertFalse(item["path"].startswith(("archive/", "docs/")))
                self.assertEqual(item["status"], "proposed")
                self.assertIsNone(item["reviewed_at"])

    def test_references_distinguish_executable_previews(self):
        references = [e for e in self.entries if e.get("implementation")]
        self.assertEqual(len(references), 12)
        for item in references:
            with self.subTest(id=item["id"]):
                self.assertEqual(item["implementation"]["status"], "reference")
                self.assertTrue((ROOT / item["implementation"]["source_path"]).is_file())
