/* Reference native input: components/input/spec.md. No feature validation or writes. */
(function(scope) {
"use strict";
function mount(container, options) {
  const cfg=Object.assign({ id:"reference-input",label:"Email address",type:"email",value:"",hint:"Used only for this example.",disabled:false,readOnly:false,required:false,error:"",onChange:function(){} },options||{});
  if (!["text","email","search","tel","url","number"].includes(cfg.type)) throw new TypeError("Unsupported input type");
  const group=document.createElement("div");group.className="reference-field";
  const label=document.createElement("label");label.htmlFor=cfg.id;label.textContent=cfg.label+(cfg.required?" (required)":"");
  const input=document.createElement("input");input.id=cfg.id;input.name=cfg.id;input.type=cfg.type;
  input.value=cfg.value;input.disabled=Boolean(cfg.disabled);input.readOnly=Boolean(cfg.readOnly);input.required=Boolean(cfg.required);
  input.className="reference-control";if(cfg.type==="email")input.autocomplete="email";
  const help=document.createElement("p");help.id=cfg.id+"-hint";help.className="reference-help";help.textContent=cfg.hint;
  const desc=[help.id];
  if(cfg.error){const err=document.createElement("p");err.id=cfg.id+"-error";err.className="reference-error";err.textContent=cfg.error;input.setAttribute("aria-invalid","true");desc.push(err.id);group.append(label,input,help,err);}
  else group.append(label,input,help);
  input.setAttribute("aria-describedby",desc.join(" "));
  input.addEventListener("input",function(){cfg.onChange(input.value);});
  container.replaceChildren(group);return input;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
