/* Pattern: composed form with synthetic validation, pending, and unknown outcomes. */
(function(scope){"use strict";
function validate(name,email){const errors={};if(name.trim().length<2)errors.name="Enter at least two characters.";if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.trim()))errors.email="Enter a valid email address.";return errors;}
function mount(container,config){
const cfg=Object.assign({state:"initial",name:"",email:""},config||{});
container.innerHTML='<form class="pattern-card" novalidate><h3>Workspace profile</h3><p class="pattern-note">Synthetic form. No information is saved.</p><div class="pattern-errors" tabindex="-1" hidden></div><label for="demo-name">Display name</label><input id="demo-name" name="name" autocomplete="name" aria-describedby="demo-name-help"><p id="demo-name-help" class="pattern-help">How your name appears to collaborators.</p><label for="demo-email">Email address</label><input id="demo-email" name="email" type="email" autocomplete="email"><div class="pattern-actions"><button type="submit">Save example</button><button type="reset" class="pattern-secondary">Clear form</button></div><p class="pattern-feedback" role="status" aria-live="polite"></p></form>';
const form=container.querySelector("form"),name=form.elements.namedItem("name"),email=form.elements.namedItem("email"),summary=container.querySelector(".pattern-errors"),status=container.querySelector(".pattern-feedback"),submit=form.querySelector('button[type="submit"]');
name.value=cfg.name;email.value=cfg.email;
function clearErrors(){summary.hidden=true;summary.replaceChildren();for(const input of [name,email]){input.removeAttribute("aria-invalid");input.removeAttribute("aria-errormessage");const error=container.querySelector("#"+input.id+"-error");if(error)error.remove();}}
function setErrors(errors){clearErrors();const keys=Object.keys(errors);if(!keys.length)return false;const heading=document.createElement("strong");heading.textContent="Check these fields:";const list=document.createElement("ul");summary.append(heading,list);keys.forEach(function(key){const input=key==="name"?name:email;const li=document.createElement("li");const link=document.createElement("a");link.href="#"+input.id;link.textContent=errors[key];link.addEventListener("click",function(event){event.preventDefault();input.focus();});li.append(link);list.append(li);input.setAttribute("aria-invalid","true");const id=input.id+"-error";input.setAttribute("aria-errormessage",id);let message=container.querySelector("#"+id);if(!message){message=document.createElement("p");message.id=id;message.className="pattern-error";input.insertAdjacentElement("afterend",message);}message.textContent=errors[key];});summary.hidden=false;summary.focus();status.textContent="Form was not submitted. Correct the listed fields.";return true;}
function finish(kind){submit.disabled=kind==="uncertain"||kind==="success";status.textContent=kind==="uncertain"?"Status unknown. Do not submit again until the server result has been verified.":kind==="error"?"Simulated service error. Your entries are still here. You may retry.":"Example validated locally. Nothing was saved to a server.";}
form.addEventListener("submit",function(e){e.preventDefault();if(setErrors(validate(name.value,email.value)))return;clearErrors();submit.disabled=true;status.textContent="Checking simulated submission…";finish(cfg.state==="unknown"?"uncertain":cfg.state==="server-error"?"error":"success");});
form.addEventListener("reset",function(event){
  // Resetting form fields must never silently unlock an uncertain mutation.
  if(cfg.state==="unknown"){event.preventDefault();status.textContent="Outcome still unknown. Verify authoritative status before retrying; clearing the form cannot unlock this request.";return;}
  clearErrors();submit.disabled=false;status.textContent="Form cleared. Nothing was saved.";
});
if(cfg.state==="invalid"){setErrors(validate(name.value,email.value));}
if(cfg.state==="pending"){submit.disabled=true;status.textContent="Simulated pending request. Duplicate submission unavailable.";}
return form;
}
scope.CatalogReference=Object.freeze({mount:mount,validate:validate});
})(globalThis);
