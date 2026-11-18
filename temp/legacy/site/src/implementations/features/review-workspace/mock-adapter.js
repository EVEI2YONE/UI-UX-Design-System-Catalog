/* Synthetic, deterministic, in-memory human-review adapter.
 * Never talks to any server. It demonstrates outcome classification, not authorization.
 */
(function(scope) {
"use strict";
const SEED=Object.freeze([
  Object.freeze({id:"REV-101",title:"Community garden update",summary:"A member submitted a brief project update for editorial review.",revision:1,status:"pending"}),
  Object.freeze({id:"REV-102",title:"Accessible event announcement",summary:"A draft event notice includes a location, time and access notes.",revision:2,status:"pending"}),
  Object.freeze({id:"REV-103",title:"Neighborhood cleanup report",summary:"A project report includes a short description and attached evidence summary.",revision:1,status:"pending"}),
  Object.freeze({id:"REV-104",title:"Volunteer activity summary",summary:"A summary of volunteer activities requires a final reviewer decision.",revision:3,status:"pending"})
]);
function copy(record) {return Object.assign({},record);}
function makeAdapter(options) {
  const settings=Object.assign({outcome:"confirmed",records:SEED,canDecide:true},options||{});
  let records=settings.records.map(copy);
  let lastUnknown=null,confirmed=null,commands=0,verifications=0;
  function list(){return records.map(copy);}
  function get(id){const match=records.find(x=>x.id===id);return match?copy(match):null;}
  function decide(request){
    commands++;
    if(!settings.canDecide||settings.outcome==="denied")return {kind:"denied",message:"You cannot decide this record in the simulated role."};
    const record=records.find(x=>x.id===request.id);
    if(!record)return {kind:"conflict",message:"This review item is no longer available."};
    if(record.status!=="pending")return {kind:"conflict",message:"This review item already has a confirmed decision."};
    if(record.revision!==request.revision||settings.outcome==="conflict")return {kind:"conflict",message:"This record changed since it was opened. Inspect a fresh version."};
    if(settings.outcome==="error")return {kind:"error",message:"The simulated service failed before confirming a change."};
    if(settings.outcome==="unknown"){
      lastUnknown={id:request.id,action:request.action};
      return {kind:"unknown",message:"The acknowledgement was lost. Verify the record before another decision."};
    }
    record.status=request.action==="approve"?"approved":request.action==="return"?"returned":"rejected";
    record.revision++;
    confirmed={id:request.id,action:request.action,status:record.status};
    return {kind:"confirmed",record:copy(record),message:"Simulated decision confirmed: "+record.status+"."};
  }
  function verify(id){
    verifications++;
    if(!lastUnknown||lastUnknown.id!==id)return {kind:"unresolved",message:"No uncertain decision is available for verification."};
    // An unknown result is NOT promoted to confirmed merely because the client asks.
    // This fixture intentionally remains unresolved so the user cannot blindly retry.
    return {kind:"unresolved",message:"Simulated authoritative status is still unknown. Ask an administrator to reconcile this record before repeating the decision."};
  }
  return Object.freeze({list,get,decide,verify,
    diagnostics:function(){return {commands,verifications,lastUnknown:lastUnknown?copy(lastUnknown):null,confirmed:confirmed?copy(confirmed):null};}});
}
scope.ReviewWorkspaceAdapter=Object.freeze({makeAdapter:makeAdapter,seed:SEED});
})(globalThis);
