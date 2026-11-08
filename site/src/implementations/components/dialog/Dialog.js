/* Native modal dialog shell. No destructive task implementation or persistence. */
(function(scope){"use strict";
function mount(container,options){
const cfg=Object.assign({id:"reference-dialog",title:"Review changes",description:"Confirm the next step.",confirmLabel:"Continue",open:true,loading:false,mode:"default",onActivate:function(){},onClose:function(){}},options||{});
const host=document.createElement("div");host.className="reference-dialog-host";
const trigger=document.createElement("button");trigger.type="button";trigger.className="reference-trigger";trigger.textContent="Open dialog";
const dialog=document.createElement("dialog");dialog.className="reference-dialog";
dialog.setAttribute("aria-labelledby",cfg.id+"-title");dialog.setAttribute("aria-describedby",cfg.id+"-description");
const title=document.createElement("h2");title.id=cfg.id+"-title";title.textContent=cfg.title;
const description=document.createElement("p");description.id=cfg.id+"-description";description.textContent=cfg.description;
const actions=document.createElement("div");actions.className="reference-dialog-actions";
const cancel=document.createElement("button");cancel.type="button";cancel.className="reference-cancel";cancel.textContent="Cancel";
const confirm=document.createElement("button");confirm.type="button";confirm.className="reference-confirm";confirm.textContent=cfg.confirmLabel;confirm.disabled=Boolean(cfg.loading);
actions.append(cancel,confirm);dialog.append(title,description,actions);host.append(trigger,dialog);
container.replaceChildren(host);
function open(){if(!dialog.open){dialog.showModal();cancel.focus();}}
function close(reason){if(dialog.open)dialog.close();cfg.onClose(reason);}
trigger.addEventListener("click",open);
cancel.addEventListener("click",function(){close("cancel");});
confirm.addEventListener("click",function(){if(!confirm.disabled){cfg.onActivate();close("confirm");}});
dialog.addEventListener("close",function(){if(trigger.isConnected)trigger.focus();});
dialog.addEventListener("cancel",function(){cfg.onClose("escape");});
if(cfg.loading){const status=document.createElement("p");status.className="reference-help";status.textContent="Example action in progress.";status.setAttribute("role","status");dialog.insertBefore(status,actions);}
if(cfg.open)open();
return dialog;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
