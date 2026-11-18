/* Node smoke tests execute the same five JS files used in the iframe.
 * They verify semantics and callbacks in a small fixture, not browser a11y.
 */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

function node(tag) {
  const listeners = {};
  const attributes = {};
  return {
    tagName: tag.toUpperCase(), id: '', name: '', textContent: '', value: '',
    disabled: false, readOnly: false, required: false, checked: false, indeterminate: false,
    attributes, listeners, children: [], open: false, isConnected: true,
    setAttribute(key, value) { attributes[key] = String(value); },
    getAttribute(key) { return attributes[key]; },
    removeAttribute(key) { delete attributes[key]; },
    append(...children) { this.children.push(...children); },
    appendChild(child) { this.children.push(child); return child; },
    insertBefore(child) { this.children.push(child); return child; },
    replaceChildren(...children) { this.children = children; },
    addEventListener(name, fn) { listeners[name] = fn; },
    dispatch(name) { if (listeners[name]) listeners[name]({type: name}); },
    click() { if (!this.disabled) this.dispatch('click'); },
    focus() { this.focused = true; },
    showModal() { this.open = true; },
    close() { this.open = false; this.dispatch('close'); }
  };
}
function load(name) {
  const folder = path.join(__dirname, '..', 'src', 'implementations', 'components', name);
  const context = {document: {createElement: node}};
  context.globalThis = context;
  const filename = name.charAt(0).toUpperCase() + name.slice(1) + '.js';
  vm.runInNewContext(fs.readFileSync(path.join(folder, filename), 'utf8'), context, {filename});
  vm.runInNewContext(fs.readFileSync(path.join(folder, 'scenarios.js'), 'utf8'), context, {filename: 'scenarios.js'});
  return context;
}
function scenarioSmoke(name, minimum) {
  const context = load(name);
  assert.equal(typeof context.CatalogReference.mount, 'function');
  assert.ok(Array.isArray(context.CatalogScenarios));
  assert.ok(context.CatalogScenarios.length >= minimum);
  assert.equal(new Set(context.CatalogScenarios.map(item => item.id)).size, context.CatalogScenarios.length);
}
test('all five references expose distinct deterministic states', () => {
  for (const name of ['input','field','select','checkbox','dialog']) scenarioSmoke(name, 5);
});
test('Input keeps persistent visible label and linked error and emits native input value', () => {
  const context = load('input'), container = node('div'); let observed;
  const control = context.CatalogReference.mount(container, {id:'email', value:'bad', error:'Correct the email', onChange: v => {observed=v;}});
  const children = container.children[0].children;
  assert.equal(children[0].htmlFor, 'email');
  assert.equal(control.tagName, 'INPUT');
  assert.equal(control.attributes['aria-invalid'], 'true');
  assert.equal(control.attributes['aria-describedby'], 'email-hint email-error');
  control.value = 'good@example.test'; control.dispatch('input');
  assert.equal(observed, 'good@example.test');
});
test('Field links label, help and error and never validates or submits itself', () => {
  const context = load('field'), container = node('div');
  const control = context.CatalogReference.mount(container, {id:'workspace', error:'Enter two characters', required:true});
  assert.equal(container.children[0].children[0].htmlFor, 'workspace');
  assert.equal(control.required, true);
  assert.equal(control.attributes['aria-describedby'], 'workspace-hint workspace-error');
});
test('Select is native and represents unavailable options and selection', () => {
  const context = load('select'), container = node('div'); let observed;
  const control = context.CatalogReference.mount(container, {value:'south',options:[{value:'north',label:'North',disabled:true},{value:'south',label:'South'}],onChange: v=>observed=v});
  assert.equal(control.tagName, 'SELECT');
  assert.equal(control.value,'south');
  assert.equal(control.children[0].disabled,true);
  control.value='north';control.dispatch('change');assert.equal(observed,'north');
});
test('Checkbox uses real mixed state and native change', () => {
  const context=load('checkbox'), container=node('div');let observed;
  const control=context.CatalogReference.mount(container,{indeterminate:true,onChange:v=>observed=v});
  assert.equal(control.type,'checkbox');assert.equal(control.indeterminate,true);
  control.checked=true;control.dispatch('change');assert.equal(observed,true);
});
test('Dialog uses native showModal, cancel, Escape callback and return focus', () => {
  const context=load('dialog'), container=node('div');let dismissed,activated=0;
  const dialog=context.CatalogReference.mount(container,{onClose:reason=>dismissed=reason,onActivate:()=>activated++});
  assert.equal(dialog.tagName,'DIALOG');assert.equal(dialog.open,true);
  assert.equal(dialog.attributes['aria-labelledby'],'reference-dialog-title');
  assert.equal(dialog.attributes['aria-describedby'],'reference-dialog-description');
  const host=container.children[0],trigger=host.children[0],actions=dialog.children[2],cancel=actions.children[0],confirm=actions.children[1];
  assert.equal(cancel.focused,true);
  confirm.click();assert.equal(activated,1);assert.equal(dismissed,'confirm');
  assert.equal(dialog.open,false);assert.equal(trigger.focused,true);
  trigger.click();assert.equal(dialog.open,true);dialog.dispatch('cancel');assert.equal(dismissed,'escape');
});
test('Dialog disabled confirm cannot send action while pending', () => {
  const context=load('dialog'),container=node('div');let activated=0;
  const dialog=context.CatalogReference.mount(container,{loading:true,onActivate:()=>activated++});
  const actions=dialog.children.find(c=>c.className==='reference-dialog-actions');
  const confirm=actions.children[1];assert.equal(confirm.disabled,true);
  confirm.click();assert.equal(activated,0);
});

test('consumer validation corrects Input/Field errors without replacing the editing control', () => {
  for (const name of ['input','field']) {
    const context=load(name), container=node('div');
    const invalid=context.CatalogScenarios.find(s=>s.id==='invalid');
    const control=context.CatalogReference.mount(container,invalid.config);
    const error=container.children[0].children.find(n=>n.className==='reference-error');
    control.focus();
    control.value=name==='input'?'still invalid':'!';control.dispatch('input');
    assert.equal(control.getAttribute('aria-invalid'),'true');assert.equal(error.hidden,false);
    control.value=name==='input'?'person@example.test':'Research team';control.dispatch('input');
    assert.equal(control.getAttribute('aria-invalid'),undefined);
    assert.equal(error.hidden,true);assert.equal(error.textContent,'');
    assert.equal(control.getAttribute('aria-describedby'),control.id+'-hint');
    assert.equal(container.children[0].children[1],control);assert.equal(control.focused,true);
    control.value='';control.dispatch('input');
    assert.equal(control.getAttribute('aria-invalid'),'true');assert.equal(error.hidden,false);
  }
});
