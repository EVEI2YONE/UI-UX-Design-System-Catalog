/* Pattern: actual accessible table with local paging, selection and non-persistent bulk action. */
(function(scope){"use strict";
const ITEMS=Object.freeze(Array.from({length:13},(_,i)=>Object.freeze({id:"T-"+String(i+1).padStart(2,"0"),name:"Example task "+(i+1),status:i%3===0?"Closed":"Open"})));
function page(items,index,size){const count=Math.max(1,Math.ceil(items.length/size));const safe=Math.max(0,Math.min(index,count-1));return {items:items.slice(safe*size,(safe+1)*size),index:safe,count:count};}
function mount(container,config){const cfg=Object.assign({state:"results",page:0},config||{});
container.innerHTML='<section class="pattern-card"><h3>Task collection</h3><p class="pattern-note">Synthetic records; selection and bulk actions are local examples.</p><div class="pattern-table-wrap"><table><caption>Example tasks by status</caption><thead><tr><th scope="col">Select</th><th scope="col">Task ID</th><th scope="col">Title</th><th scope="col">Status</th></tr></thead><tbody></tbody></table></div><div class="pattern-actions"><button type="button" class="pattern-secondary" data-action="previous">Previous page</button><span class="pattern-page"></span><button type="button" class="pattern-secondary" data-action="next">Next page</button><button type="button" data-action="bulk">Mark selected (demo)</button></div><p class="pattern-feedback" role="status" aria-live="polite"></p></section>';
const tbody=container.querySelector("tbody"),status=container.querySelector(".pattern-feedback"),pageText=container.querySelector(".pattern-page"),prev=container.querySelector('[data-action="previous"]'),next=container.querySelector('[data-action="next"]'),bulk=container.querySelector('[data-action="bulk"]');
const checked=new Set();let index=cfg.page;
function draw(){tbody.replaceChildren();if(cfg.state==="loading"){status.textContent="Loading synthetic task records…";return;}if(cfg.state==="error"){status.textContent="Simulated service error. No results were returned; do not treat this as an empty collection.";return;}
const dataset=cfg.state==="empty"?[]:ITEMS,visible=page(dataset,index,5);index=visible.index;
visible.items.forEach(function(item){const tr=document.createElement("tr"),td=document.createElement("td"),box=document.createElement("input");box.type="checkbox";box.checked=checked.has(item.id);box.setAttribute("aria-label","Select task "+item.id);box.addEventListener("change",function(){if(box.checked)checked.add(item.id);else checked.delete(item.id);status.textContent=checked.size+" tasks selected.";});td.append(box);tr.append(td);[item.id,item.name,item.status].forEach(value=>{const cell=document.createElement("td");cell.textContent=value;tr.append(cell);});tbody.append(tr);});
pageText.textContent=dataset.length?"Page "+(index+1)+" of "+visible.count:"No pages";prev.disabled=index===0||!dataset.length;next.disabled=index>=visible.count-1||!dataset.length;bulk.disabled=!checked.size;
status.textContent=cfg.state==="empty"?"No tasks are available.":visible.items.length+" rows displayed; "+dataset.length+" total tasks.";}
prev.addEventListener("click",function(){index=Math.max(0,index-1);draw();});next.addEventListener("click",function(){index++;draw();});
bulk.addEventListener("click",function(){status.textContent=checked.size+" tasks selected. This example did not change any saved records.";});
draw();return tbody;
}
scope.CatalogReference=Object.freeze({mount:mount,page:page});
})(globalThis);
