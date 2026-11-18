/* Pattern: semantic links, current destination, responsive disclosure. */
(function(scope){"use strict";
function mount(container,config){
const cfg=Object.assign({active:"projects",collapsed:false,long:false},config||{});
container.innerHTML='<section class="pattern-card"><h3>Workspace navigation</h3><button type="button" class="pattern-secondary pattern-menu" aria-controls="pattern-primary-links" aria-expanded="true">Toggle menu</button><nav aria-label="Example workspace sections" id="pattern-primary-links"><ul class="pattern-nav"><li><a href="#overview" data-route="overview">Overview</a></li><li><a href="#projects" data-route="projects">Projects</a></li><li><a href="#activity" data-route="activity">Activity</a></li><li><a href="#settings" data-route="settings">Settings</a></li></ul></nav><p class="pattern-feedback" role="status" aria-live="polite"></p></section>';
const button=container.querySelector(".pattern-menu"),nav=container.querySelector("nav"),status=container.querySelector(".pattern-feedback");
const links=Array.from(nav.querySelectorAll("a"));
if(cfg.long)links[1].textContent="Projects, workspaces and shared activity";
function activate(key){links.forEach(function(a){if(a.dataset.route===key){a.setAttribute("aria-current","page");}else{a.removeAttribute("aria-current");}});status.textContent="Example location: "+key+". URL routing remains application-owned.";}
links.forEach(a=>a.addEventListener("click",function(e){e.preventDefault();activate(a.dataset.route);}));
function setOpen(open){nav.hidden=!open;button.setAttribute("aria-expanded",String(open));}
button.addEventListener("click",function(){setOpen(nav.hidden);if(nav.hidden)button.focus();});
nav.addEventListener("keydown",function(e){if(e.key==="Escape"&&!nav.hidden){setOpen(false);button.focus();}});
activate(cfg.active);setOpen(!cfg.collapsed);return nav;
}
scope.CatalogReference=Object.freeze({mount:mount});
})(globalThis);
