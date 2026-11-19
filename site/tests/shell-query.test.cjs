const test = require('node:test');
const assert = require('node:assert/strict');
const query = require('../static/shell/query.js');

const forms = {
  id: 'pattern.forms', title: 'Form composition and validation',
  aliases: 'forms | validation', primaryTasks: 'Recover from a failed submission | form submission failed',
  relatedTasks: 'Submit something consequential', search: 'forms form composition and validation recover from a failed submission'
};
const recovery = {
  id: 'pattern.interaction-recovery', title: 'Interaction states and recovery',
  aliases: 'recovery | interaction states', primaryTasks: 'Recover from no results',
  relatedTasks: 'Recover from a failed submission', search: 'interaction states recovery recover from a failed submission'
};

test('normalizes punctuation and Unicode for task-oriented lookup', () => {
  assert.deepEqual(query.terms('  Recover  from A failed submission  '),
    ['recover', 'from', 'a', 'failed', 'submission']);
  assert.deepEqual(query.terms('fOrM_submission'), ['form', 'submission']);
  assert.deepEqual(query.terms('مرحبا  بالعالم'), ['مرحبا', 'بالعالم']);
  assert.equal(query.matches('Form · recover from a failed submission', query.terms('failed submission')), true);
  assert.equal(query.matches('Form · field errors', query.terms('destructive action')), false);
  assert.deepEqual(query.terms(''), []);
});

test('uses canonical ID, alias, title and primary-task ranking', () => {
  assert.equal(query.rank(forms, 'pattern.forms'), 100);
  assert.equal(query.rank(forms, 'validation'), 90);
  assert.equal(query.rank(forms, 'Form composition and validation'), 80);
  assert.equal(query.rank(forms, 'recover from a failed submission'), 85);
  assert.equal(query.rank(recovery, 'recover from a failed submission'), 35);
  assert.ok(query.rank(forms, 'recover from a failed submission') >
    query.rank(recovery, 'recover from a failed submission'));
  assert.equal(query.rank(forms, 'unrelated tree widget'), -1);
  assert.equal(query.rank(forms, ''), 0);
});
