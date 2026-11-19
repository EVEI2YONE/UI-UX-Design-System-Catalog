const test = require('node:test');
const assert = require('node:assert/strict');
const query = require('../static/shell/query.js');
test('search shell accepts multi-word natural-language queries without mutation', () => {
  assert.deepEqual(query.terms('  Recover  from A failed submission  '),
    ['recover', 'from', 'a', 'failed', 'submission']);
  assert.equal(query.matches('Form · recover from a failed submission', query.terms('failed submission')), true);
  assert.equal(query.matches('Form · field errors', query.terms('destructive action')), false);
  assert.deepEqual(query.terms(''), []);
});
