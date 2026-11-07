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
        self.assertEqual(found[0]['id'], 'component.button')

    def test_filter(self):
        found = lookup(self.entries, 'theme', layer='tokens')
        self.assertEqual([x['id'] for x in found], ['foundation.design-tokens'])

    def test_unknown(self):
        self.assertEqual(lookup(self.entries, 'quasar pineapple nebula'), [])


    def test_task_flow_alias(self):
        found = lookup(self.entries, 'information architecture')
        self.assertEqual(found[0]['id'], 'pattern.task-flows')

    def test_recovery_intent(self):
        found = lookup(self.entries, 'network timeout')
        self.assertEqual(found[0]['id'], 'pattern.interaction-recovery')

    def test_keyboard_accessibility(self):
        found = lookup(self.entries, 'keyboard navigation')
        self.assertEqual(found[0]['id'], 'guidance.accessibility')

    def test_translation_intent(self):
        found = lookup(self.entries, 'text expansion')
        self.assertEqual(found[0]['id'], 'guidance.internationalization')

    def test_batch2_cross_references(self):
        ids = {entry['id'] for entry in self.entries}
        for ident in ('pattern.task-flows', 'pattern.interaction-recovery',
                      'guidance.accessibility', 'guidance.internationalization'):
            entry = next(e for e in self.entries if e['id'] == ident)
            self.assertEqual(entry['status'], 'proposed')
            self.assertEqual(entry['owner'], 'unassigned')
            self.assertIsNone(entry['reviewed_at'])
            self.assertTrue(entry['use_when'])
            self.assertTrue(entry['avoid_when'])
            self.assertTrue(entry['related'])
            for ref in entry['related'] + entry['depends_on']:
                self.assertIn(ref, ids)
                self.assertNotEqual(ref, ident)


    def test_measurement_intent(self):
        found = lookup(self.entries, 'task completion rate')
        self.assertEqual(found[0]['id'], 'guidance.ux-measurement')

    def test_lifecycle_intent(self):
        found = lookup(self.entries, 'catalog promotion')
        self.assertEqual(found[0]['id'], 'governance.lifecycle')

    def test_quality_intent(self):
        found = lookup(self.entries, 'documentation checks')
        self.assertEqual(found[0]['id'], 'governance.quality')

    def test_batch3_registry_metadata_and_references(self):
        ids = {entry['id'] for entry in self.entries}
        for ident in ('guidance.ux-measurement', 'governance.lifecycle', 'governance.quality'):
            entry = next(e for e in self.entries if e['id'] == ident)
            self.assertEqual(entry['status'], 'proposed')
            self.assertEqual(entry['owner'], 'unassigned')
            self.assertIsNone(entry['reviewed_at'])
            self.assertTrue(entry['use_when'] and entry['avoid_when'] and entry['related'])
            for ref in entry['related'] + entry['depends_on']:
                self.assertIn(ref, ids)
                self.assertNotEqual(ref, ident)


    def test_batch4_component_lookup(self):
        cases = {
            'loading button': 'component.button',
            'email input': 'component.input',
            'native select': 'component.select',
            'indeterminate checkbox': 'component.checkbox',
            'modal dialog': 'component.dialog',
            'field error': 'component.field',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query)[0]['id'], expected)

    def test_batch4_canonical_paths_and_refs(self):
        ids = {e['id'] for e in self.entries}
        for component in ('button', 'input', 'select', 'checkbox', 'dialog', 'field'):
            e = next(x for x in self.entries if x['id'] == 'component.' + component)
            self.assertEqual(e['path'], f'components/{component}/spec.md')
            self.assertTrue((ROOT / e['path']).is_file())
            self.assertEqual(e['kind'], 'specification')
            self.assertEqual(e['status'], 'proposed')
            self.assertEqual(e['owner'], 'unassigned')
            self.assertIsNone(e['reviewed_at'])
            self.assertTrue(e['use_when'] and e['avoid_when'])
            for ref in e['related'] + e['depends_on']:
                self.assertIn(ref, ids)

if __name__ == '__main__':
    unittest.main()
