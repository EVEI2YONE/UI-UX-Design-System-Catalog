"""Regression tests for catalog retrieval. Run: python3 -m unittest discover -s tests -v"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from find_concept import lookup  # noqa: E402


class LookupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / 'catalog/index.json').read_text())['entries']

    def test_exact_id_first(self):
        found = lookup(self.entries, 'architecture.component-contracts')
        self.assertEqual(found[0]['id'], 'architecture.component-contracts')

    def test_alias_ranking(self):
        found = lookup(self.entries, 'component hierarchy')
        self.assertEqual(found[0]['id'], 'architecture.component-model')

    def test_task_phrase(self):
        found = lookup(self.entries, 'loading button')
        self.assertEqual(found[0]['id'], 'architecture.component-contracts')

    def test_filter(self):
        found = lookup(self.entries, 'theme', layer='tokens')
        self.assertEqual([x['id'] for x in found], ['foundation.design-tokens'])

    def test_unknown(self):
        self.assertEqual(lookup(self.entries, 'quasar pineapple nebula'), [])


if __name__ == '__main__':
    unittest.main()
