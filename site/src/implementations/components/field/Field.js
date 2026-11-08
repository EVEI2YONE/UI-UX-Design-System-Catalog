/* Field composition owns naming/help/error association; validation is supplied by caller. */
(function(scope){"use strict";
function mount(container,options){
const cfg=Object.assign({id:"reference-field",label:"Workspace name",hint:"Enter the name people will recognize.",value:"",required:false,error:"",disabled:false,readOnly:false,onChange:function(){}},options||{});
const wrapper=document.createElement("div");wrapper.className="reference-field";
const label=document.createElement("label");label.htmlFor=cfg.id;label.textContent=cfg.label+(cfg.required?" (required)":"");
const control=document.createElement("input");control.id=cfg.id;control.name=cfg.id;control.type="text";control.className="reference-control";control.value=cfg.value;control.required=Boolean(cfg.required);control.disabled=Boolean(cfg.disabled);control.readOnly=Boolean(cfg.readOnly);
const hint=document.createElement("p");hint.id=cfg.id+"-hint";hint.className="reference-help";hint.textContent=cfg.hint;
const described=[hint.id];wrapper.append(label,control,hint);
if(cfg.error){const error=document.createElement("p");error.id=cfg.id+"-error";error.className="reference-error";error.textContent=cfg.error;control.setAttribute("aria-invalid","true");described.push(error.id);wrapper.append(error);}
control.setAttribute("aria-describedby",described.join(" "));
control.addEventListener("input",function(){cfg.onChange(control.value);});
container.replaceChildren(wrapper);return control;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
