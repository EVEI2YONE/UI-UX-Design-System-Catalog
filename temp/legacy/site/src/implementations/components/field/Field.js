/* Field composition owns naming/help/error association; validation is supplied by caller. */
(function(scope){"use strict";
function mount(container,options){
const cfg=Object.assign({id:"reference-field",label:"Workspace name",hint:"Enter the name people will recognize.",value:"",required:false,error:"",disabled:false,readOnly:false,onChange:function(){}},options||{});
const wrapper=document.createElement("div");wrapper.className="reference-field";
const label=document.createElement("label");label.htmlFor=cfg.id;label.textContent=cfg.label+(cfg.required?" (required)":"");
const control=document.createElement("input");control.id=cfg.id;control.name=cfg.id;control.type="text";control.className="reference-control";control.value=cfg.value;control.required=Boolean(cfg.required);control.disabled=Boolean(cfg.disabled);control.readOnly=Boolean(cfg.readOnly);
const hint=document.createElement("p");hint.id=cfg.id+"-hint";hint.className="reference-help";hint.textContent=cfg.hint;
  const error=document.createElement("p");error.id=cfg.id+"-error";error.className="reference-error";
  wrapper.append(label,control,hint,error);
  function showError(message){
    error.textContent=message||"";error.hidden=!message;
    control.setAttribute("aria-describedby",hint.id+(message?" "+error.id:""));
    if(message)control.setAttribute("aria-invalid","true");
    else control.removeAttribute("aria-invalid");
  }
  showError(cfg.error);
  control.addEventListener("input",function(){
    // The caller supplies the rule. Updating feedback never remounts the control.
    if(typeof cfg.validate==="function")showError(cfg.validate(control.value));
    cfg.onChange(control.value);
  });
container.replaceChildren(wrapper);return control;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
