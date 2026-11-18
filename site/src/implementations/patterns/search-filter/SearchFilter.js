/* Pattern: local search/filter with honest no-results and error states. */
(function(scope){"use strict";
const DATA=Object.freeze([{id:"1",name:"Accessibility review",status:"open"},{id:"2",name:"Navigation audit",status:"closed"},{id:"3",name:"Input readability",status:"open"},{id:"4",name:"Performance analysis",status:"open"},{id:"5",name:"Localization review",status:"closed"}]);
function filter(items,query,state){const q=query.trim().toLocaleLowerCase();return items.filter(x=>(state==="all"||x.status===state)&&x.name.toLocaleLowerCase().includes(q));}
function mount(container,config){const cfg=Object.assign({query:"",status:"all",state:"results"},config||{});
container.innerHTML='<section class="pattern-card"><h3>Find review tasks</h3><div class="pattern-filters"><div><label for="pattern-query">Search task title</label><input id="pattern-query" type="search"></div><div><label for="pattern-status">Status</label><select id="pattern-status"><option value="all">All statuses</option><option value="open">Open</option><option value="closed">Closed</option></select></div></div><button class="pattern-secondary" type="button" id="pattern-clear">Clear filters</button><p class="pattern-feedback" role="status" aria-live="polite"></p><ul class="pattern-results"></ul></section>';
const query=container.querySelector("#pattern-query"),status=container.querySelector("#pattern-status"),output=container.querySelector(".pattern-feedback"),results=container.querySelector(".pattern-results");
query.value=cfg.query;status.value=cfg.status;
function refresh(){results.replaceChildren();
if(cfg.state==="error"){output.textContent="Simulated search service error. Criteria are preserved; retry when service is available.";return;}
if(cfg.state==="pending"){output.textContent="Updating simulated results. Query and filters are preserved.";return;}
const found=filter(cfg.state==="empty"?[]:DATA,query.value,status.value);output.textContent=found.length+" matching tasks. Status: "+status.value+".";
if(!found.length){const li=document.createElement("li");li.textContent=cfg.state==="empty"?"No tasks are available yet.":"No matches. Change your query or clear filters.";results.append(li);return;}
found.forEach(function(item){const li=document.createElement("li");li.textContent=item.name+" — "+item.status;results.append(li);});}
query.addEventListener("input",refresh);status.addEventListener("change",refresh);
container.querySelector("#pattern-clear").addEventListener("click",function(){query.value="";status.value="all";refresh();query.focus();});
refresh();return results;
}
scope.CatalogReference=Object.freeze({mount:mount,filter:filter});
})(globalThis);
