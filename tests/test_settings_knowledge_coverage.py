"""Focused regression coverage for cumulative Settings knowledge batches.

Documentation-only checks. They are not proof of product functionality,
WCAG conformance, authorization, event integrity or timezone behavior.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

CANONICAL_ID = "pattern.account-settings-portal"
CANONICAL_PATH = "patterns/account-and-settings-portal.md"
BATCH_HEADINGS = (
    "Workspace configuration foundation — Settings knowledge Batch 1",
    "Settings knowledge Batch 2 — feature and policy configuration",
    "Settings knowledge Batch 3 — time and personal preferences",
    "Settings knowledge Batch 4 — configuration governance and audit",
)
KNOWLEDGE_GAPS = ("KG-001", "KG-002", "KG-003", "KG-004",
                  "KG-005", "KG-006", "KG-007", "KG-008")
QUERIES = (
    "settings configuration registry",
    "settings permission matrix",
    "settings save recovery",
    "feature settings dependencies",
    "review policy transition",
    "settings reporting timezone",
    "effective display preference",
    "configuration audit events",
)


class SettingsKnowledgeCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(
            (ROOT / "catalog/index.json").read_text(encoding="utf-8"))
        cls.text = (ROOT / CANONICAL_PATH).read_text(encoding="utf-8")

    def test_unique_canonical_owner(self):
        entries = self.registry["entries"]
        matches = [e for e in entries if e["id"] == CANONICAL_ID]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["path"], CANONICAL_PATH)
        self.assertEqual(matches[0]["status"], "proposed")
        self.assertEqual(len(entries), len({e["id"] for e in entries}))

    def test_all_batches_and_gaps_documented(self):
        for heading in BATCH_HEADINGS:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.text)
        for gap in KNOWLEDGE_GAPS:
            with self.subTest(gap=gap):
                self.assertIn(gap, self.text)

    def test_task_queries_retrieve_canonical_settings(self):
        for query in QUERIES:
            with self.subTest(query=query):
                result = lookup(self.registry["entries"], query, limit=3)
                self.assertTrue(result)
                self.assertEqual(result[0]["id"], CANONICAL_ID)

    def test_navigation_and_evidence_boundaries(self):
        for path in ("README.md", "patterns/README.md", "CHANGELOG.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            self.assertIn("Settings", text)
            self.assertIn("Batch 4", text)
        self.assertIn("NOT VERIFIED", self.text)
        self.assertIn("DEC-010", self.text)
        self.assertIn("not", self.text.lower())


if __name__ == "__main__":
    unittest.main()
