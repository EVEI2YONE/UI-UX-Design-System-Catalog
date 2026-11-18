/* Phase 7 tests: execute the actual synthetic adapter and reference source.
 * This DOM fixture is not a substitute for browser, screen-reader or visual QA.
 */
const test=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');
const dir=path.join(__dirname,'..','src','implementations','features','review-workspace');
function element(tag){
 const attrs={},listeners={};
 return {
 tagName:tag.toUpperCase(),className:'',textContent:'',id:'',value:'',dataset:{},children:[],disabled:false,
 setAttribute(k,v){attrs[k]=String(v);},
 getAttribute(k){return attrs[k];},
 removeAttribute(k){delete attrs[k];},
 addEventListener(k,fn){listeners[k]=fn;},
 replaceChildren(...children){this.children=children;},
 append(...children){this.children.push(...children);},
 appendChild(child){this.children.push(child);return child;},
 focus(){this.focused=true;},
 querySelector(selector){
   const all=this.querySelectorAll(selector);return all.length?all[0]:null;
 },
 querySelectorAll(selector){
   let candidates=[];function walk(e){for(const child of e.children||[]){candidates.push(child);walk(child);}}walk(this);
   if(selector==='h3')return candidates.filter(x=>x.tagName==='H3');
   if(selector==='textarea')return candidates.filter(x=>x.tagName==='TEXTAREA');
   if(selector==='button[data-record]')return candidates.filter(x=>x.tagName==='BUTTON'&&x.dataset.record!==undefined);
   if(selector==='button[data-next]')return candidates.filter(x=>x.tagName==='BUTTON'&&x.dataset.next!==undefined);
   if(selector==='button[data-verify]')return candidates.filter(x=>x.tagName==='BUTTON'&&x.dataset.verify!==undefined);
   return [];
 },
 click(){if(!this.disabled&&listeners.click)listeners.click({type:'click'});},
 input(value){this.value=value;if(listeners.input)listeners.input({type:'input'});}
 };
}
function run(){
 const sandbox={document:{createElement:element}};sandbox.globalThis=sandbox;
 for(const filename of ['mock-adapter.js','scenarios.js','ReviewWorkspace.js'])
  vm.runInNewContext(fs.readFileSync(path.join(dir,filename),'utf8'),sandbox,{filename});
 return sandbox;
}
test('metadata and scenario contract covers error, permission, conflict and long data',()=>{
 const ctx=run(), ids=ctx.CatalogScenarios.map(x=>x.id);
 for(const id of ['loaded','empty','loading','queue-error','readonly','denied','conflict','error','unknown','long','many'])assert.ok(ids.includes(id),id);
 assert.equal(new Set(ids).size,ids.length);
});
test('adapter is deterministic and cannot write through network',()=>{
 const ctx=run(),a=ctx.ReviewWorkspaceAdapter.makeAdapter();
 const item=a.get('REV-101');assert.equal(item.status,'pending');
 const result=a.decide({id:item.id,revision:item.revision,action:'approve',reason:''});
 assert.equal(result.kind,'confirmed');assert.equal(a.get(item.id).status,'approved');assert.equal(a.diagnostics().commands,1);
 assert.equal(a.get('REV-102').status,'pending');
});
test('adapter denies unauthorized or outdated mutation',()=>{
 const ctx=run(),base={id:'REV-101',revision:1,action:'approve',reason:''};
 for(const opts of [{canDecide:false},{outcome:'denied'}]){
  const a=ctx.ReviewWorkspaceAdapter.makeAdapter(opts);
  assert.equal(a.decide(base).kind,'denied');assert.equal(a.get(base.id).status,'pending');
 }
 const a=ctx.ReviewWorkspaceAdapter.makeAdapter();
 assert.equal(a.decide({...base,revision:900}).kind,'conflict');
 assert.equal(a.get(base.id).status,'pending');
});
test('unknown outcome prevents optimistic confirmation and requires reconciliation',()=>{
 const ctx=run(),a=ctx.ReviewWorkspaceAdapter.makeAdapter({outcome:'unknown'});
 const base={id:'REV-101',revision:1,action:'approve',reason:''};
 assert.equal(a.decide(base).kind,'unknown');
 assert.equal(a.get(base.id).status,'pending');
 const verify=a.verify(base.id);assert.equal(verify.kind,'unresolved');
 assert.equal(a.diagnostics().verifications,1);
});
test('workspace renders selected detail, validates reason and confirms through explicit pending',()=>{
 const ctx=run(),host=element('div');
 const workspace=ctx.CatalogReference.mount(host,{mode:'default'});
 assert.equal(host.children[0],workspace.root);
 const queue=workspace.root.children[3].children[0],detail=workspace.root.children[3].children[1];
 assert.ok(queue.querySelectorAll('button[data-record]').length>=3);
 assert.equal(detail.querySelector('h3').textContent,'Community garden update');
 let buttons=detail.children.find(x=>x.className==='review-actions').children;
 buttons.find(x=>x.textContent==='Reject').click();
 assert.ok(detail.children.some(x=>x.className==='review-error'));
 const textarea=detail.querySelector('textarea');textarea.input('Needs a clearer description');
 buttons=detail.children.find(x=>x.className==='review-actions').children;
 buttons.find(x=>x.textContent==='Reject').click();
 assert.ok(detail.children.some(x=>x.className==='review-warning'));
 assert.equal(workspace.diagnostics().commands,0);
 const resolve=detail.children.find(x=>x.className==='review-actions').children[0];resolve.click();
 assert.equal(workspace.diagnostics().commands,1);
 assert.equal(workspace.adapter.get('REV-101').status,'rejected');
});
test('workspace keeps unknown outcome locked, no duplicate command',()=>{
 const ctx=run(),host=element('div');
 const workspace=ctx.CatalogReference.mount(host,{mode:'unknown'});
 const detail=workspace.root.children[3].children[1];
 let actions=detail.children.find(x=>x.className==='review-actions').children;
 actions.find(x=>x.textContent==='Approve').click();
 actions=detail.children.find(x=>x.className==='review-actions').children;
 actions[0].click();
 assert.equal(workspace.diagnostics().commands,1);
 actions=detail.children.find(x=>x.className==='review-actions').children;
 assert.equal(actions.length,1);assert.equal(actions[0].textContent,'Verify record status');
 actions[0].click();
 assert.equal(workspace.diagnostics().commands,1);
 assert.equal(workspace.diagnostics().verifications,1);
});
test('read-only scenario cannot initiate a decision',()=>{
 const ctx=run(),host=element('div');const workspace=ctx.CatalogReference.mount(host,{mode:'readonly'});
 const detail=workspace.root.children[3].children[1],actions=detail.children.find(x=>x.className==='review-actions').children;
 assert.ok(actions.every(x=>x.disabled));assert.equal(workspace.diagnostics().commands,0);
});

function actions(detail){return detail.children.find(x=>x.className==='review-actions').children;}
test('reason correction clears and restores feedback in place',()=>{
 const ctx=run(),workspace=ctx.CatalogReference.mount(element('div'),{});
 const detail=workspace.root.children[3].children[1];
 actions(detail).find(x=>x.textContent==='Return for changes').click();
 const field=detail.querySelector('textarea'),error=detail.children.find(x=>x.id==='review-reason-error');
 field.input('   ');assert.equal(field.getAttribute('aria-invalid'),'true');assert.equal(error.hidden,false);
 field.input('Add a date.');assert.equal(field.getAttribute('aria-invalid'),undefined);assert.equal(error.hidden,true);
 assert.equal(field.getAttribute('aria-describedby'),'review-reason-help');assert.equal(detail.querySelector('textarea'),field);
 field.input('');assert.equal(error.hidden,false);assert.equal(field.getAttribute('aria-invalid'),'true');
});
test('confirmed items leave pending queue; next action and final completion have valid focus',()=>{
 const ctx=run(),workspace=ctx.CatalogReference.mount(element('div'),{});
 const queue=workspace.root.children[3].children[0],detail=workspace.root.children[3].children[1];
 for(let remaining=4;remaining>0;remaining--){
  actions(detail).find(x=>x.textContent==='Approve').click();
  actions(detail)[0].click();
  assert.equal(queue.querySelectorAll('button[data-record]').length,remaining-1);
  assert.equal(detail.children.some(x=>x.className==='review-actions'),false);
  const next=detail.querySelector('button[data-next]');
  if(remaining>1){assert.equal(next.focused,true);next.click();assert.equal(detail.querySelector('h3').focused,true);}
  else {assert.equal(next,null);assert.equal(detail.querySelector('h3').focused,true);assert.ok(detail.children.some(x=>/All caught up/.test(x.textContent)));}
 }
 assert.equal(workspace.diagnostics().commands,4);
});
test('adapter refuses another decision on a completed record at its latest revision',()=>{
 const adapter=run().ReviewWorkspaceAdapter.makeAdapter();
 adapter.decide({id:'REV-101',revision:1,action:'approve',reason:''});
 const record=adapter.get('REV-101');
 assert.equal(adapter.decide({id:record.id,revision:record.revision,action:'reject',reason:'Repeat'}).kind,'conflict');
 assert.equal(adapter.get(record.id).status,'approved');assert.equal(adapter.get(record.id).revision,2);
});
