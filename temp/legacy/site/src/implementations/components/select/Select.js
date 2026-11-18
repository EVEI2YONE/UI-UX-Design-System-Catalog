/* Native select reference. Option sourcing and permissions remain application-owned. */
(function(scope){"use strict";
function mount(container,options){
const cfg=Object.assign({id:"reference-select",label:"Preferred region",hint:"Choose one region.",value:"",required:false,disabled:false,loading:false,error:"",options:[{value:"",label:"Choose a region"},{value:"north",label:"North"},{value:"south",label:"South"},{value:"west",label:"West"}],onChange:function(){}},options||{});
const group=document.createElement("div");group.className="reference-field";
const label=document.createElement("label");label.htmlFor=cfg.id;label.textContent=cfg.label+(cfg.required?" (required)":"");
const select=document.createElement("select");select.id=cfg.id;select.name=cfg.id;select.className="reference-control";select.disabled=Boolean(cfg.disabled||cfg.loading);select.required=Boolean(cfg.required);
cfg.options.forEach(function(item){const option=document.createElement("option");option.value=item.value;option.textContent=item.label;option.disabled=Boolean(item.disabled);select.appendChild(option);});
select.value=cfg.value;
const hint=document.createElement("p");hint.id=cfg.id+"-hint";hint.className="reference-help";hint.textContent=cfg.loading?"Options are loading. Please try again shortly.":cfg.hint;
group.append(label,select,hint);const ids=[hint.id];
if(cfg.error){const error=document.createElement("p");error.id=cfg.id+"-error";error.className="reference-error";error.textContent=cfg.error;select.setAttribute("aria-invalid","true");group.append(error);ids.push(error.id);}
select.setAttribute("aria-describedby",ids.join(" "));
select.addEventListener("change",function(){cfg.onChange(select.value);});
container.replaceChildren(group);return select;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
