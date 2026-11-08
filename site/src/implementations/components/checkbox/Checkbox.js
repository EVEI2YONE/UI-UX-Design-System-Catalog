/* Native checkbox, including mixed-state semantics. No implicit persistence. */
(function(scope){"use strict";
function mount(container,options){
const cfg=Object.assign({id:"reference-checkbox",label:"Receive updates",hint:"Changes remain local to this preview.",checked:false,indeterminate:false,disabled:false,required:false,error:"",onChange:function(){}},options||{});
const group=document.createElement("div");group.className="reference-field reference-check-field";
const row=document.createElement("div");row.className="reference-check-row";
const input=document.createElement("input");input.type="checkbox";input.id=cfg.id;input.name=cfg.id;input.checked=Boolean(cfg.checked);input.indeterminate=Boolean(cfg.indeterminate);input.disabled=Boolean(cfg.disabled);input.required=Boolean(cfg.required);
const label=document.createElement("label");label.htmlFor=cfg.id;label.textContent=cfg.label+(cfg.required?" (required)":"");
row.append(input,label);group.appendChild(row);
const help=document.createElement("p");help.id=cfg.id+"-hint";help.className="reference-help";help.textContent=cfg.hint;group.appendChild(help);const ids=[help.id];
if(cfg.error){const err=document.createElement("p");err.id=cfg.id+"-error";err.className="reference-error";err.textContent=cfg.error;input.setAttribute("aria-invalid","true");group.appendChild(err);ids.push(err.id);}
input.setAttribute("aria-describedby",ids.join(" "));
input.addEventListener("change",function(){cfg.onChange(input.checked);});
container.replaceChildren(group);return input;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
