/* Generic human-review workspace. Purely synthetic reference behavior.
 * The application owns all real authorization, server mutation and audit.
 */
(function(scope){"use strict";
function make(tag,className,text){
  const element=document.createElement(tag);
  if(className)element.className=className;
  if(text!==undefined)element.textContent=text;
  return element;
}
function mount(container,options){
  const cfg=Object.assign({mode:"default",selected:"REV-101",canDecide:true,records:null},options||{});
  if(!scope.ReviewWorkspaceAdapter)throw new Error("Missing synthetic adapter");
  const adapter=scope.ReviewWorkspaceAdapter.makeAdapter({
    outcome:({denied:"denied",conflict:"conflict",error:"error",unknown:"unknown"})[cfg.mode]||"confirmed",
    canDecide:cfg.canDecide!==false&&cfg.mode!=="readonly",records:cfg.records||scope.ReviewWorkspaceAdapter.seed
  });
  const state={selected:cfg.selected,phase:"idle",action:null,note:"",locked:false};
  const root=make("section","review-workspace");
  const heading=make("h2","review-title","Review queue");
  const intro=make("p","review-note","Synthetic decisions only. No real records, authorization or writes.");
  const status=make("p","review-status","");status.setAttribute("role","status");status.setAttribute("aria-live","polite");
  const layout=make("div","review-layout");
  const left=make("section","review-queue"),right=make("section","review-detail");
  left.setAttribute("aria-label","Pending review items");right.setAttribute("aria-label","Selected item details");
  layout.append(left,right);root.append(heading,intro,status,layout);container.replaceChildren(root);
  function notice(message){status.textContent=message;}
  function button(label,onClick,secondary){
    const b=make("button",secondary?"review-button review-button-secondary":"review-button",label);
    b.type="button";b.addEventListener("click",onClick);return b;
  }
  function setSelected(id){if(state.locked)return;state.selected=id;state.phase="idle";state.action=null;state.note="";render();const detailHeading=right.querySelector("h3");if(detailHeading)detailHeading.focus();}
  function request(action){
    if(state.locked)return;
    if(!cfg.canDecide||cfg.mode==="readonly"){notice("Read only: decision actions are unavailable.");return;}
    const record=adapter.get(state.selected);if(!record)return;
    if(action!=="approve"&&!state.note.trim()){state.phase="validation";state.action=action;render();const input=right.querySelector("textarea");if(input)input.focus();return;}
    state.action=action;state.phase="pending";state.locked=true;render();
    // Intentional explicit pending step. No simulated server response until the user resolves it.
    notice("Simulated request pending. Choose Resolve simulated request to inspect its outcome.");
  }
  function resolve(){
    if(state.phase!=="pending")return;
    const record=adapter.get(state.selected);
    const result=adapter.decide({id:record.id,revision:record.revision,action:state.action,reason:state.note});
    state.locked=result.kind==="unknown";
    state.phase=result.kind;render();notice(result.message);
    if(result.kind==="confirmed"){const next=left.querySelector("button[data-record]");if(next)next.focus();else heading.focus();}
    else if(result.kind==="unknown"){const verify=right.querySelector('button[data-verify]');if(verify)verify.focus();}
    else {const details=right.querySelector("h3");if(details)details.focus();}
  }
  function verify(){
    if(state.phase!=="unknown")return;
    const result=adapter.verify(state.selected);notice(result.message);
    // Do not unlock an unknown mutation unless authoritative confirmation is available.
    if(result.kind==="confirmed"){state.phase="confirmed";state.locked=false;render();}
  }
  function render(){
    left.replaceChildren();right.replaceChildren();
    const queueHeading=make("h3","","Items to inspect");left.append(queueHeading);
    if(cfg.mode==="loading"){left.append(make("p","review-note","Loading synthetic records…"));right.append(make("p","review-note","Select a record when loading finishes."));return;}
    if(cfg.mode==="queue-error"){left.append(make("p","review-error","Unable to load the simulated queue. This is not an empty queue."));right.append(make("p","","Retry requires a new scenario or a real service adapter."));return;}
    const records=cfg.mode==="empty"?[]:adapter.list();
    if(!records.length){left.append(make("p","review-note","There are no records awaiting review."));right.append(make("p","review-note","Nothing selected."));return;}
    const list=make("ul","review-records");
    const visible=records.slice(0,12); // explicit bounded reference size
    visible.forEach(function(record){
      const item=make("li");const selected=state.selected===record.id;
      const b=button(record.title+" · "+record.id,function(){setSelected(record.id);},true);
      b.dataset.record=record.id;
      if(selected)b.setAttribute("aria-current","true");
      if(state.locked)b.disabled=true;
      item.append(b);list.append(item);
    });left.append(list);
    if(records.length>visible.length)left.append(make("p","review-note","Showing first 12 synthetic records."));
    let record=adapter.get(state.selected);
    if(!record){record=records[0];state.selected=record.id;}
    const title=make("h3","",record.title);title.tabIndex=-1;right.append(title);
    const meta=make("p","review-meta","Record "+record.id+" · Revision "+record.revision+" · "+record.status);
    const description=make("p","review-summary",record.summary);right.append(meta,description);
    const label=make("label","","Decision reason");label.htmlFor="review-reason";
    const textarea=make("textarea","review-reason");textarea.id="review-reason";textarea.rows=3;textarea.value=state.note;textarea.disabled=state.locked;
    textarea.setAttribute("aria-describedby","review-reason-help");
    textarea.addEventListener("input",function(){state.note=textarea.value;});
    const help=make("p","review-note","Required to return or reject; optional to approve.");
    help.id="review-reason-help";right.append(label,textarea,help);
    if(state.phase==="validation"){textarea.setAttribute("aria-invalid","true");const error=make("p","review-error","Enter a reason before returning or rejecting.");error.id="review-reason-error";textarea.setAttribute("aria-describedby","review-reason-help review-reason-error");right.append(error);}
    const actions=make("div","review-actions");
    if(state.phase==="pending"){actions.append(button("Resolve simulated request",resolve));right.append(actions,make("p","review-warning","Simulated pending outcome; duplicate decisions are locked."));return;}
    if(state.phase==="unknown"){const v=button("Verify record status",verify);v.dataset.verify="true";actions.append(v);right.append(actions,make("p","review-warning","Outcome unknown. Decision controls remain locked; do not resubmit."));return;}
    if(state.phase==="confirmed"){right.append(make("p","review-success","Simulated decision confirmed. No real backend changed."));}
    else if(state.phase==="denied"){right.append(make("p","review-error","Permission denied by synthetic adapter. Only an authoritative service can grant access."));}
    else if(state.phase==="conflict"){right.append(make("p","review-warning","The record revision is stale. Reinspect current evidence; this reference cannot override it."));}
    else if(state.phase==="error"){right.append(make("p","review-error","Known simulated service failure. Your reason and selection are preserved."));}
    const denied=cfg.mode==="readonly"||cfg.canDecide===false||state.phase==="denied"||state.phase==="conflict"||state.locked;
    for(const [verb,label] of [["approve","Approve"],["return","Return for changes"],["reject","Reject"]]){
      const b=button(label,function(){request(verb);},verb!=="approve");
      b.disabled=denied;actions.append(b);
    }right.append(actions);
    if(denied)right.append(make("p","review-note","Decision controls unavailable in this scenario."));
  }
  heading.tabIndex=-1;render();
  if(cfg.mode==="readonly")notice("Read-only scenario: you may inspect but cannot decide.");
  else if(cfg.mode==="loading")notice("Simulated queue is loading.");
  else if(cfg.mode==="queue-error")notice("Simulated queue request failed.");
  else notice("Select a record, inspect its details, then choose a simulated decision.");
  return Object.freeze({root:root,adapter:adapter,diagnostics:adapter.diagnostics});
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
