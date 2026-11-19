"""Verify visual craftsmanship topics, evidence boundaries and canonical lookup.

This is source-level knowledge coverage, not rendered product or accessibility testing.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup

class VisualCraftsmanshipTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {e["id"]: e for e in cls.entries}

    def test_retrieval(self):
        mapping = {
            "visual craftsmanship": "foundation.visual-craftsmanship",
            "inspiration research": "foundation.visual-craftsmanship",
            "design direction selection": "foundation.visual-craftsmanship",
            "styling recipes": "foundation.practical-styling",
            "motion design": "foundation.practical-styling",
            "visual craftsmanship critique": "governance.quality",
            "render inspect refine": "governance.quality",
            "visual craftsmanship workflow": "governance.quality",
        }
        for phrase, expected in mapping.items():
            with self.subTest(phrase=phrase):
                matches = lookup(self.entries, phrase, limit=1)
                self.assertTrue(matches, phrase)
                self.assertEqual(matches[0]["id"], expected)

    def test_canonical_owners_remain_distinct(self):
        self.assertEqual(len(self.entries), len(self.by_id))
        for identifier in ("foundation.visual-craftsmanship", "foundation.practical-styling",
                           "governance.quality", "foundation.design-tokens",
                           "guidance.accessibility", "guidance.wireframe-methodology"):
            self.assertIn(identifier, self.by_id)

    def test_visual_decision_topics_remain_findable(self):
        sources = {
            "foundation.visual-craftsmanship": ("optical balance", "typography", "color composition", "art direction", "inspiration"),
            "foundation.practical-styling": ("layout", "surfaces", "iconography", "motion"),
            "governance.quality": ("visual critique", "evidence", "accessibility"),
        }
        for identifier, topics in sources.items():
            source = (ROOT / self.by_id[identifier]["path"]).read_text(encoding="utf-8").casefold()
            for topic in topics:
                with self.subTest(concept=identifier, topic=topic):
                    self.assertIn(topic.casefold(), source)

    def test_workflow_links_guidance_and_discloses_limits(self):
        path = ROOT / "governance/visual-craftsmanship-workflow.md"
        workflow = path.read_text(encoding="utf-8")
        for topic in ("Reference", "Explore directions", "Compose the UI", "Render and inspect",
                      "Validate behavior", "NOT VERIFIED", "synthetic"):
            self.assertIn(topic.casefold(), workflow.casefold())
        governance = (ROOT / "governance/README.md").read_text(encoding="utf-8")
        agent = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("visual-craftsmanship-workflow.md", governance)
        self.assertIn("visual-design-craftsmanship.md", agent)
        for item in self.entries:
            for target in item.get("related", []) + item.get("depends_on", []):
                self.assertIn(target, self.by_id)
