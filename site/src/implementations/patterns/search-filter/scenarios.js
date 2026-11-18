(function(scope){"use strict";scope.CatalogScenarios=Object.freeze([
{id:"results",label:"Matching results",config:{query:"review",status:"all"}},
{id:"filtered",label:"Filtered collection",config:{status:"open"}},
{id:"no-matches",label:"Zero matching results",config:{query:"not-in-data"}},
{id:"empty",label:"Genuinely empty dataset",config:{state:"empty"}},
{id:"pending",label:"Pending lookup",config:{state:"pending",query:"review"}},
{id:"error",label:"Service error",config:{state:"error",query:"review"}}
]);})(globalThis);
