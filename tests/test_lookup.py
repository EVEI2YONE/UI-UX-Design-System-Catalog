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


    def test_batch5_pattern_lookup(self):
        cases = {
            'form composition': 'pattern.forms',
            'primary navigation': 'pattern.navigation',
            'search filtering': 'pattern.search-filter',
            'sortable table': 'pattern.data-tables',
            'toast notification': 'pattern.feedback',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query)[0]['id'], expected)

    def test_batch5_pattern_contracts(self):
        ids = {entry['id'] for entry in self.entries}
        expected_paths = {
            'forms': 'patterns/forms.md',
            'navigation': 'patterns/navigation.md',
            'search-filter': 'patterns/search-and-filter.md',
            'data-tables': 'patterns/data-tables.md',
            'feedback': 'patterns/feedback.md',
        }
        for item, path in expected_paths.items():
            with self.subTest(item=item):
                entry = next(e for e in self.entries if e['id'] == 'pattern.' + item)
                self.assertEqual(entry['path'], path)
                self.assertTrue((ROOT / path).is_file())
                self.assertEqual(entry['kind'], 'specification')
                self.assertEqual(entry['status'], 'proposed')
                self.assertEqual(entry['owner'], 'unassigned')
                self.assertIsNone(entry['reviewed_at'])
                self.assertTrue(entry['use_when'] and entry['avoid_when'])
                for ref in entry['related'] + entry['depends_on']:
                    self.assertIn(ref, ids)


    def test_batch6_role_metadata_complete(self):
        entry = next(e for e in self.entries if e['id'] == 'pattern.role-aware-workspaces')
        for field in ('use_when', 'avoid_when', 'related', 'depends_on', 'owner', 'reviewed_at'):
            self.assertIn(field, entry)
        self.assertEqual(entry['status'], 'proposed')
        self.assertEqual(entry['owner'], 'unassigned')

    def test_batch6_normalization_and_filters(self):
        self.assertEqual(lookup(self.entries, 'role_aware-workspaces')[0]['id'],
                         'pattern.role-aware-workspaces')
        self.assertEqual(lookup(self.entries, 'modal-dialog')[0]['id'], 'component.dialog')
        self.assertEqual(lookup(self.entries, 'loading button', limit=1)[0]['id'],
                         'component.button')
        self.assertEqual(lookup(self.entries, status='stable'), [])

    def test_batch6_negative_guidance_not_positive_search(self):
        from find_concept import score
        entry = {'id': 'sample.noop', 'title': 'Noop', 'summary': 'example',
                 'aliases': [], 'domains': [], 'use_when': [],
                 'avoid_when': ['secret negative marker']}
        self.assertEqual(score(entry, 'secret negative marker'), -1)

    def test_batch6_invalid_references_and_types(self):
        from validate_catalog import main
        # The validator runs against the real checkout; this test checks
        # the canonical registry contract without mutating repository data.
        registry = json.loads((ROOT / 'catalog/index.json').read_text())
        ids = {entry['id'] for entry in registry['entries']}
        paths = [entry['path'] for entry in registry['entries']]
        self.assertEqual(len(paths), len(set(paths)))
        for entry in registry['entries']:
            self.assertTrue(set(('use_when', 'avoid_when', 'related',
                                 'depends_on', 'owner', 'reviewed_at')) <= set(entry))
            self.assertIsInstance(entry['use_when'], list)
            self.assertIsInstance(entry['avoid_when'], list)
            self.assertIsInstance(entry['owner'], str)
            for target in entry['related'] + entry['depends_on']:
                self.assertIn(target, ids)
        self.assertEqual(main(), 0)

    def test_batch6_dependency_graph_acyclic(self):
        graph = {e['id']: e['depends_on'] for e in self.entries}
        visited, active = set(), set()
        def walk(ident):
            self.assertNotIn(ident, active)
            if ident in visited:
                return
            active.add(ident)
            for child in graph[ident]:
                walk(child)
            active.remove(ident)
            visited.add(ident)
        for ident in graph:
            walk(ident)


    def test_batch9_trust_and_resilience_lookup(self):
        cases = {
            'privacy UX': 'guidance.privacy-trust',
            'passkeys': 'pattern.authentication-lifecycle',
            'notification fatigue': 'pattern.notifications-attention',
            'sync conflict': 'pattern.offline-sync',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result, f'Missing match for {query}')
                self.assertEqual(result[0]['id'], expected)

    def test_batch9_canonical_paths_statuses_and_refs(self):
        paths = {
            'guidance.privacy-trust': 'guidance/privacy-consent-and-trust.md',
            'pattern.authentication-lifecycle': 'patterns/authentication-and-account-lifecycle.md',
            'pattern.notifications-attention': 'patterns/notifications-and-attention.md',
            'pattern.offline-sync': 'patterns/offline-sync-and-conflicts.md',
        }
        ids = {e['id'] for e in self.entries}
        for ident, path in paths.items():
            with self.subTest(ident=ident):
                entry = next(e for e in self.entries if e['id'] == ident)
                self.assertEqual(entry['path'], path)
                self.assertTrue((ROOT / path).is_file())
                self.assertEqual(entry['status'], 'proposed')
                self.assertEqual(entry['owner'], 'unassigned')
                self.assertIsNone(entry['reviewed_at'])
                self.assertTrue(entry['use_when'] and entry['avoid_when'])
                for target in entry['related'] + entry['depends_on']:
                    self.assertIn(target, ids)
                    self.assertNotEqual(target, ident)


    def test_batch10_chart_mobile_and_advanced_lookup(self):
        cases = {
            'data visualization': 'guidance.data-visualization',
            'dashboard design': 'guidance.data-visualization',
            'adaptive layout': 'guidance.mobile-adaptive',
            'safe area': 'guidance.mobile-adaptive',
            'command palette': 'pattern.advanced-interactions',
            'drag and drop': 'pattern.advanced-interactions',
            'approval workflow': 'pattern.role-aware-workspaces',
            'editable data grid': 'pattern.data-tables',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                found = lookup(self.entries, query, limit=1)
                self.assertTrue(found, f'Missing match for {query}')
                self.assertEqual(found[0]['id'], expected)

    def test_batch10_new_guidance_paths_and_refs(self):
        expected = {
            'guidance.data-visualization': 'guidance/data-visualization-and-dashboards.md',
            'guidance.mobile-adaptive': 'guidance/mobile-and-adaptive-platform-ux.md',
            'pattern.advanced-interactions': 'patterns/advanced-interactions-and-reversible-actions.md',
        }
        ids = {x['id'] for x in self.entries}
        for ident, path in expected.items():
            with self.subTest(ident=ident):
                entry = next(x for x in self.entries if x['id'] == ident)
                self.assertEqual(entry['path'], path)
                self.assertTrue((ROOT / path).is_file())
                self.assertEqual(entry['kind'], 'guideline')
                self.assertEqual(entry['status'], 'proposed')
                self.assertEqual(entry['owner'], 'unassigned')
                self.assertIsNone(entry['reviewed_at'])
                self.assertTrue(entry['use_when'] and entry['avoid_when'])
                for target in entry['related'] + entry['depends_on']:
                    self.assertIn(target, ids)
                    self.assertNotEqual(target, ident)


    def test_batch11_ai_agent_multimodal_lookup(self):
        cases = {
            'AI transparency': 'guidance.ai-experiences',
            'AI provenance': 'guidance.ai-experiences',
            'human in the loop': 'pattern.agentic-actions',
            'agentic UX': 'pattern.agentic-actions',
            'AI agent approval': 'pattern.agentic-actions',
            'voice UX': 'pattern.multimodal-conversation',
            'speech interaction': 'pattern.multimodal-conversation',
            'barge in': 'pattern.multimodal-conversation',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                results = lookup(self.entries, query, limit=1)
                self.assertTrue(results, f'No match for {query}')
                self.assertEqual(results[0]['id'], expected)

    def test_batch11_canonical_guards_and_related_concepts(self):
        expected = {
            'guidance.ai-experiences': 'guidance/ai-powered-experiences-and-trust.md',
            'pattern.agentic-actions': 'patterns/agentic-actions-and-approvals.md',
            'pattern.multimodal-conversation': 'patterns/conversational-voice-and-multimodal-ux.md',
        }
        ids = {e['id'] for e in self.entries}
        for ident, path in expected.items():
            with self.subTest(ident=ident):
                entry = next(e for e in self.entries if e['id'] == ident)
                self.assertEqual(entry['path'], path)
                self.assertTrue((ROOT / path).is_file())
                self.assertEqual(entry['status'], 'proposed')
                self.assertEqual(entry['owner'], 'unassigned')
                self.assertIsNone(entry['reviewed_at'])
                self.assertEqual(entry['kind'], 'guideline')
                self.assertTrue(entry['use_when'] and entry['avoid_when'])
                for link in entry['related'] + entry['depends_on']:
                    self.assertIn(link, ids)
                    self.assertNotEqual(link, ident)


    def test_batch12_performance_experiment_and_handoff_lookup(self):
        cases = {
            'Core Web Vitals': 'guidance.performance-experience',
            'performance budget': 'guidance.performance-experience',
            'perceived speed': 'guidance.performance-experience',
            'real user monitoring': 'guidance.performance-experience',
            'A/B testing': 'guidance.experimentation',
            'sample ratio mismatch': 'guidance.experimentation',
            'experiment guardrails': 'guidance.experimentation',
            'sequential testing': 'guidance.experimentation',
            'component spec': 'architecture.component-contracts',
            'catalog promotion': 'governance.lifecycle',
        }
        for query, expected in cases.items():
            with self.subTest(query=query):
                found = lookup(self.entries, query, limit=1)
                self.assertTrue(found, f'Missing match for {query}')
                self.assertEqual(found[0]['id'], expected)

    def test_batch12_new_paths_and_integrity(self):
        paths = {
            'guidance.performance-experience': 'guidance/performance-and-perceived-speed.md',
            'guidance.experimentation': 'guidance/experimentation-and-causal-evidence.md',
        }
        ids = {entry['id'] for entry in self.entries}
        for ident, path in paths.items():
            with self.subTest(ident=ident):
                entry = next(x for x in self.entries if x['id'] == ident)
                self.assertEqual(entry['path'], path)
                self.assertEqual(entry['kind'], 'guideline')
                self.assertTrue((ROOT / path).is_file())
                self.assertEqual(entry['status'], 'proposed')
                self.assertEqual(entry['owner'], 'unassigned')
                self.assertIsNone(entry['reviewed_at'])
                self.assertTrue(entry['use_when'] and entry['avoid_when'])
                for target in entry['related'] + entry['depends_on']:
                    self.assertIn(target, ids)
                    self.assertNotEqual(target, ident)

if __name__ == '__main__':
    unittest.main()
