(function(scope){"use strict";const regions=[{value:"",label:"Choose a region",disabled:true},{value:"north",label:"North"},{value:"south",label:"South"},{value:"west",label:"West",disabled:true}];scope.CatalogScenarios=Object.freeze([
{id:"empty",label:"Unselected",config:{options:regions}},
{id:"selected",label:"Selected option",config:{options:regions,value:"south"}},
{id:"invalid",label:"Missing required choice",config:{options:regions,required:true,error:"Select a region before continuing."}},
{id:"disabled-option",label:"Unavailable option",config:{options:regions,value:"north",hint:"West is temporarily unavailable."}},
{id:"loading",label:"Loading options",config:{loading:true,options:[{value:"",label:"Loading choices…"}]}},
{id:"long",label:"Long translated options",config:{label:"Choose the delivery service region",options:[{value:"",label:"Choose a delivery service region"},{value:"long",label:"Northern coastal distribution and international logistics district"}],value:"long"}}
]);})(globalThis);
