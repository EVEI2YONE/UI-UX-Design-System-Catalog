(function(scope){"use strict";scope.CatalogScenarios=Object.freeze([
{id:"default",label:"Confirmation dialog",config:{title:"Review changes",description:"Would you like to continue?",confirmLabel:"Continue"}},
{id:"destructive",label:"Consequence-focused copy",config:{title:"Delete local draft?",description:"This is a simulated confirmation. No draft is stored or deleted.",confirmLabel:"Delete example draft"}},
{id:"pending",label:"Pending action",config:{title:"Saving changes",description:"The simulated request is still pending.",confirmLabel:"Saving…",loading:true}},
{id:"long",label:"Long content",config:{title:"Review changes affecting members of the entire workspace",description:"This longer description demonstrates how the native modal dialog shell handles content expansion and wrapping in a narrow viewing environment without losing the cancel action."}},
{id:"reopen",label:"Close and reopen",config:{title:"Settings",description:"Close this dialog, then use Open dialog to test focus return."}}
]);})(globalThis);
