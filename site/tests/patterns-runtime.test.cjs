/* Execute the real source algorithms and scenario registries.
 * A DOM fixture is NOT a browser accessibility or visual verification.
 */
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const patternSources = [
  ['form','Form'],['navigation','Navigation'],['search-filter','SearchFilter'],
  ['data-tables','DataTables'],['recovery','Recovery']
];
function load(folder, file) {
  const dir = path.join(__dirname,'..','src','implementations','patterns',folder);
  const context = {document: {}};
  context.globalThis = context;
  vm.runInNewContext(fs.readFileSync(path.join(dir,file+'.js'),'utf8'),context,{filename:file+'.js'});
  vm.runInNewContext(fs.readFileSync(path.join(dir,'scenarios.js'),'utf8'),context,{filename:'scenarios.js'});
  return context;
}
test('five pattern references contain trusted source, distinct fixtures and a mount API',()=>{
  for(const [dir,file] of patternSources){
    const context=load(dir,file);
    assert.equal(typeof context.CatalogReference.mount,'function',dir);
    assert.ok(context.CatalogScenarios.length>=5,dir);
    assert.equal(new Set(context.CatalogScenarios.map(s=>s.id)).size,context.CatalogScenarios.length,dir);
    for(const scenario of context.CatalogScenarios){
      assert.equal(typeof scenario.config,'object');
      assert.equal(typeof scenario.label,'string');
    }
  }
});
test('form validation distinguishes user errors without server requests',()=>{
  const {validate}=load('form','Form').CatalogReference;
  assert.deepEqual(Object.keys(validate('A','bad')).sort(),['email','name']);
  assert.deepEqual(Object.keys(validate('Taylor','taylor@example.test')),[]);
  assert.deepEqual(Object.keys(validate('  ','taylor@example.test')),['name']);
});
test('search uses query and structured status constraints, not hidden data',()=>{
  const {filter}=load('search-filter','SearchFilter').CatalogReference;
  const fixtures=[{name:'Accessibility review',status:'open'},{name:'Navigation review',status:'closed'}];
  assert.equal(filter(fixtures,'review','open').length,1);
  assert.equal(filter(fixtures,'review','all').length,2);
  assert.equal(filter(fixtures,'unmatched','all').length,0);
});
test('pagination produces bounded stable pages and safe empty state',()=>{
  const {page}=load('data-tables','DataTables').CatalogReference;
  const items=Array.from({length:13},(_,id)=>({id}));
  assert.equal(page(items,0,5).items.length,5);
  assert.equal(page(items,1,5).items[0].id,5);
  assert.equal(page(items,2,5).items.length,3);
  assert.equal(page(items,100,5).index,2);
  assert.equal(page([],100,5).items.length,0);
  assert.equal(page([],100,5).index,0);
});
test('unknown operation outcome cannot trigger unverified duplicate submit',()=>{
  const {next}=load('recovery','Recovery').CatalogReference;
  assert.equal(next('initial','submit'),'pending');
  assert.equal(next('pending','lose-ack'),'unknown');
  assert.equal(next('unknown','submit'),'unknown');
  assert.equal(next('unknown','verify'),'confirmed');
  assert.equal(next('pending','fail'),'error');
  assert.equal(next('error','submit'),'pending');
  assert.equal(next('unknown','reset'),'initial');
});
