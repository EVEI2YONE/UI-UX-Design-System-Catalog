/* Regression checks for authored semantic color pairs, not WCAG certification.
 * Actual browser/forced-color rendering and assistive technology need separate checks.
 */
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'..');
function luminance(hex){
 const full=hex.length===3?hex.split('').map(c=>c+c).join(''):hex;
 const rgb=[0,2,4].map(i=>parseInt(full.slice(i,i+2),16)/255).map(c=>c<=.04045?c/12.92:((c+.055)/1.055)**2.4);
 return rgb.reduce((s,c,i)=>s+c*[.2126,.7152,.0722][i],0);
}
function contrast(a,b){const values=[luminance(a),luminance(b)].sort((a,b)=>a-b);return (values[1]+.05)/(values[0]+.05);}
function tokens(text,mode){
 const rule=mode==='light'?text.match(/:root\{([^}]+)\}/):text.match(new RegExp('\\[data-theme="'+mode+'"\\]\\{([^}]+)\\}'));
 assert.ok(rule,'missing theme '+mode);
 return Object.fromEntries([...rule[1].matchAll(/--([a-z-]+):#([a-f0-9]{3,6})\b/g)].map(m=>[m[1],m[2]]));
}
function check(a,b,min,label){assert.ok(a&&b,'missing color '+label);const ratio=contrast(a,b);assert.ok(ratio>=min,label+' '+ratio.toFixed(2)+':1 < '+min+':1');}
test('all core references keep enabled borders distinct and text readable across themes',()=>{
 for(const name of ['input','select','checkbox','field','dialog','button']){
  const file=path.join(root,'src','implementations','components',name,name[0].toUpperCase()+name.slice(1)+'.css');
  const css=fs.readFileSync(file,'utf8');
  for(const mode of ['light','dark','contrast']){
   const t=tokens(css,mode),label=name+'/'+mode;
   if(name==='button'){
    check(t['button-outline'],t['button-secondary-bg'],3,label+' secondary boundary');
    check(t['button-secondary-text'],t['button-secondary-bg'],4.5,label+' secondary text');
    for(const role of ['bg','bg-hover','danger-bg','danger-hover'])check(t['button-text'],t['button-'+role],4.5,label+' '+role+' text');
   }else{
    check(t['ref-border'],t['ref-surface'],3,label+' boundary');
    check(t['ref-text'],t['ref-surface'],4.5,label+' text');
    check(t['ref-error'],t['ref-surface'],4.5,label+' error');
   }
  }
 }
});
test('review workspace and pattern controls meet sampled border and text contrast targets',()=>{
 const files=[['features/review-workspace/ReviewWorkspace.css','rw','bg','fg','border'],...['form/Form','navigation/Navigation','search-filter/SearchFilter','data-tables/DataTables','recovery/Recovery'].map(f=>['patterns/'+f+'.css','p','bg','ink','line'])];
 for(const [file,p,bg,fg,border] of files){
  const css=fs.readFileSync(path.join(root,'src','implementations',file),'utf8');
  for(const mode of ['light','dark','contrast']){
   const t=tokens(css,mode),label=file+'/'+mode;
   check(t[p+'-'+border],t[p+'-'+bg],3,label+' boundary');
   check(t[p+'-'+fg],t[p+'-'+bg],4.5,label+' text');
   check(t[p+'-muted'],t[p+'-'+bg],4.5,label+' helper');
   check(t[p+'-error'],t[p+'-'+bg],4.5,label+' error');
   check(t[p+'-action'],t[p+'-action-text']||'fff',4.5,label+' action text');
  }
 }
});
test('preview toolbar and catalog search use the stronger enabled-control token',()=>{
 const host=fs.readFileSync(path.join(root,'src','previews','preview-host.css'),'utf8');
 const border=host.match(/--preview-control-border:#([a-f0-9]+)/)[1];
 check(border,'fff',3,'preview light border');
 assert.match(host,/border:1px solid var\(--preview-control-border\)/);
 const chrome=fs.readFileSync(path.join(root,'static','styles.css'),'utf8');
 const control=chrome.match(/--control-border:#([a-f0-9]+)/)[1];
 check(control,'fff',3,'catalog search');
 assert.match(chrome,/border:1px solid var\(--control-border\)/);
});
