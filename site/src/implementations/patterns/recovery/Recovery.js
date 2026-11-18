/* Pattern: distinguish unknown outcomes from failed operations; no automated unsafe retry. */
(function(scope){"use strict";
const STATES=Object.freeze({initial:"Not submitted",pending:"Submitting example…",error:"Request failed. No confirmed change; you may retry.",unknown:"Outcome unknown. Verify current server state before repeating the action.",confirmed:"Operation confirmed by a simulated authoritative check."});
function next(state,action){if(action==="reset")return "initial";if(action==="submit"&&(state==="initial"||state==="error"))return "pending";if(action==="fail"&&state==="pending")return "error";if(action==="lose-ack"&&state==="pending")return "unknown";if(action==="verify"&&state==="unknown")return "confirmed";return state;}
function mount(container,config){const cfg=Object.assign({state:"initial"},config||{});
container.innerHTML='<section class="pattern-card"><h3>Safe submission recovery</h3><p class="pattern-note">Synthetic state machine. It cannot change real data.</p><p class="pattern-feedback" role="status" aria-live="polite"></p><div class="pattern-actions"><button type="button" data-action="submit">Submit example</button><button type="button" class="pattern-secondary" data-action="fail">Simulate failure</button><button type="button" class="pattern-secondary" data-action="lose-ack">Lose acknowledgement</button><button type="button" class="pattern-secondary" data-action="verify">Verify state</button><button type="button" class="pattern-secondary" data-action="reset">Start over</button></div></section>';
const status=container.querySelector(".pattern-feedback");let state=cfg.state;
function render(){status.textContent=STATES[state];for(const button of container.querySelectorAll("[data-action]")){const action=button.dataset.action;button.disabled=action!=="reset"&&next(state,action)===state;}}
container.querySelectorAll("[data-action]").forEach(button=>button.addEventListener("click",function(){state=next(state,button.dataset.action);render();}));
render();return container;
}
scope.CatalogReference=Object.freeze({mount:mount,next:next});
})(globalThis);
