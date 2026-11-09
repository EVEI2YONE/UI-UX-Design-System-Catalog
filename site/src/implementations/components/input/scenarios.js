(function(scope){"use strict";scope.CatalogScenarios=Object.freeze([
{id:"empty",label:"Empty email",config:{label:"Email address",value:""}},
{id:"filled",label:"Existing value",config:{label:"Email address",value:"person@example.test"}},
{id:"invalid",label:"Validation error",config:{label:"Email address",value:"invalid-address",error:"Enter an address such as name@example.com.",validate:function(value){return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim())?"":"Enter an address such as name@example.com.";}}},
{id:"readonly",label:"Read-only",config:{label:"Email address",value:"account@example.test",readOnly:true}},
{id:"disabled",label:"Disabled",config:{label:"Email address",value:"account@example.test",disabled:true,hint:"This field cannot be changed here."}},
{id:"long",label:"Long translated label",config:{label:"Email address used for all notifications about your workspace",value:"example@example.test"}}
]);})(globalThis);
