"""Synthetic design examples remain findable and explicitly not user-study results."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "knowledge/foundations/visual-refinement-examples.md"


class VisualExamplesTests(unittest.TestCase):
    def test_six_curated_synthetic_scenarios(self):
        text = EXAMPLES.read_text(encoding="utf-8")
        for n in range(1, 7):
            self.assertIn(f"VIS-EX-{n:02d}", text)
        self.assertIn("NOT VERIFIED", text)
        self.assertIn("hypothesis", text.lower())

    def test_examples_point_to_canonical_owners(self):
        text = EXAMPLES.read_text(encoding="utf-8")
        self.assertIn("governance/quality-gates.md", text)
        self.assertIn("visual-design-craftsmanship.md", text)
