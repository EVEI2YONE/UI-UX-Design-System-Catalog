/* Execute the exact browser reference source with a minimal deterministic DOM fixture.
 * Does not replace real browser, screen reader, focus or layout verification.
 */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const root = path.join(__dirname, '..', 'src', 'implementations', 'components', 'button');
const implementation = fs.readFileSync(path.join(root, 'Button.js'), 'utf8');
const scenariosSource = fs.readFileSync(path.join(root, 'scenarios.js'), 'utf8');

function makeElement(tag) {
  const attributes = {};
  const listeners = {};
  return {
    tagName: tag.toUpperCase(), attributes, listeners, disabled: false,
    children: [], textContent: '', type: '', className: '',
    setAttribute(name, value) { attributes[name] = value; },
    addEventListener(name, callback) { listeners[name] = callback; },
    click() { if (!this.disabled && listeners.click) listeners.click(); },
    replaceChildren(...children) { this.children = children; }
  };
}
function environment() {
  const sandbox = { document: { createElement: makeElement } };
  sandbox.globalThis = sandbox;
  vm.runInNewContext(implementation, sandbox, { filename: 'Button.js' });
  vm.runInNewContext(scenariosSource, sandbox, { filename: 'scenarios.js' });
  return sandbox;
}

test('working source exposes six deterministic synthetic scenarios', () => {
  const context = environment();
  assert.equal(context.CatalogScenarios.length, 6);
  assert.equal(new Set(context.CatalogScenarios.map(x => x.id)).size, 6);
  assert.ok(context.CatalogScenarios.every(x => Object.isFrozen(x)));
});

test('semantic button owns activation without network calls', () => {
  const context = environment();
  const container = makeElement('div');
  let activations = 0;
  const button = context.CatalogReference.mount(container, {
    label: 'Save changes', onActivate() { activations += 1; }
  });
  assert.equal(button.tagName, 'BUTTON');
  assert.equal(button.type, 'button');
  assert.equal(button.textContent, 'Save changes');
  assert.equal(container.children[0], button);
  button.click();
  assert.equal(activations, 1);
});

test('pending state prevents activation and provides announced status', () => {
  const context = environment();
  const container = makeElement('div');
  let activations = 0;
  const button = context.CatalogReference.mount(container, {
    label: 'Saving…', loading: true, onActivate() { activations += 1; }
  });
  assert.equal(button.disabled, true);
  assert.equal(button.attributes['aria-disabled'], 'true');
  assert.equal(button.attributes['aria-describedby'], 'button-progress');
  assert.equal(container.children[1].attributes.role, 'status');
  button.click();
  assert.equal(activations, 0);
});

test('disabled state is non-activating; invalid variants fail', () => {
  const context = environment();
  const container = makeElement('div');
  let activations = 0;
  const button = context.CatalogReference.mount(container, {
    disabled: true, onActivate() { activations += 1; }
  });
  button.click();
  assert.equal(activations, 0);
  assert.throws(() => context.CatalogReference.mount(container, { variant: 'unexpected' }), /Unknown button variant/);
});
