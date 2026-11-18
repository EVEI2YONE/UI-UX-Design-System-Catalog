(function(scope){"use strict";scope.CatalogScenarios=Object.freeze([
{id:"default",label:"Default field",config:{label:"Workspace name",hint:"A name visible to team members."}},
{id:"required",label:"Required field",config:{label:"Workspace name",required:true,hint:"This field is required before submission."}},
{id:"invalid",label:"Linked error",config:{label:"Workspace name",required:true,value:"!",error:"Enter at least two characters.",validate:function(value){return value.trim().length<2?"Enter at least two characters.":"";}}},
{id:"corrected",label:"Corrected field",config:{label:"Workspace name",required:true,value:"Design team"}},
{id:"readonly",label:"Read only",config:{label:"Workspace name",value:"Design team",readOnly:true}},
{id:"long",label:"Long labels and help",config:{label:"Name displayed to collaborators across all connected workspaces",hint:"This longer explanatory sentence tests reflow at reduced viewport widths."}}
]);})(globalThis);
