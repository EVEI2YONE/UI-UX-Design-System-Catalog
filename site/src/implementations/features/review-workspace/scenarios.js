/* Deterministic synthetic review-workspace scenarios, selected by preview host. */
(function(scope){"use strict";
const longRecords=[
{id:"REV-LONG",title:"A particularly long multilingual-style review title that exercises narrow screen reflow and readable action labels",summary:"An extended, synthetic evidence description contains several sentences of context. It is not confidential and does not correspond to any real person or real review submission. A reviewer should be able to inspect this text without losing the queue context.",revision:2,status:"pending"},
{id:"REV-102",title:"Short follow-up",summary:"Another synthetic item for focus navigation.",revision:1,status:"pending"}
];
const many=Array.from({length:17},(_,i)=>({id:"REV-"+String(201+i),title:"Synthetic record "+(i+1),summary:"A non-sensitive simulated review record with bounded display.",revision:1,status:"pending"}));
scope.CatalogScenarios=Object.freeze([
{id:"loaded",label:"Loaded review queue",config:{mode:"default"}},
{id:"empty",label:"Empty review queue",config:{mode:"empty"}},
{id:"loading",label:"Initial loading",config:{mode:"loading"}},
{id:"queue-error",label:"Queue service failure",config:{mode:"queue-error"}},
{id:"readonly",label:"Read-only reviewer",config:{mode:"readonly"}},
{id:"denied",label:"Decision denied",config:{mode:"denied"}},
{id:"conflict",label:"Stale revision / conflict",config:{mode:"conflict"}},
{id:"error",label:"Known decision failure",config:{mode:"error"}},
{id:"unknown",label:"Lost acknowledgement",config:{mode:"unknown"}},
{id:"long",label:"Long content / reflow",config:{mode:"default",records:longRecords,selected:"REV-LONG"}},
{id:"many",label:"Large synthetic queue",config:{mode:"default",records:many,selected:"REV-201"}}
]);
})(globalThis);
