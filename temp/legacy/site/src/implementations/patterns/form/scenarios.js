(function(scope){"use strict";scope.CatalogScenarios=Object.freeze([
{id:"initial",label:"Initial form",config:{state:"initial"}},
{id:"invalid",label:"Validation errors",config:{state:"invalid",name:"A",email:"invalid"}},
{id:"ready",label:"Valid entry",config:{name:"Taylor",email:"taylor@example.test"}},
{id:"pending",label:"Pending request",config:{state:"pending",name:"Taylor",email:"taylor@example.test"}},
{id:"service-error",label:"Recoverable service error",config:{state:"server-error",name:"Taylor",email:"taylor@example.test"}},
{id:"unknown",label:"Uncertain outcome",config:{state:"unknown",name:"Taylor",email:"taylor@example.test"}}
]);})(globalThis);
