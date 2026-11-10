/* Real Chromium browser smoke + automated axe checks for trusted visual references.
 * Runs against a locally served static build, not a production deployment.
 * Manual screen reader and mobile device reviews remain separate.
 */
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const {chromium}=require('playwright');
const axe=require('axe-core');
const base=process.env.CATALOG_BASE_URL||'http://127.0.0.1:8765';
const registry=require('../../catalog/index.json').entries;
const interactive=registry.filter(entry=>entry.implementation);
const output=path.join(__dirname,'..','artifacts','phase8');
fs.mkdirSync(output,{recursive:true});
const issues=[];
function note(message){issues.push(message);console.error('FAIL '+message);}
async function checks(){
 const browser=await chromium.launch({headless:true});
 try {
  const page=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base+'/catalog/',{waitUntil:'load'});
  assert.equal(await page.locator('article.card').count(),registry.length);
  await page.locator('#catalog-filter').fill('loading button');
  assert.ok(await page.locator('article.card:visible').count()>0,'task search returns at least one result');
  // Human-facing discovery should resolve the same canonical task as agent lookup.
  await page.locator('#catalog-filter').fill('human approval queue');
  assert.equal(await page.locator('article.card:visible').count(),1);
  assert.equal(await page.locator('article.card:visible a').getAttribute('href'),'/catalog/features/review-workspace/');
  await page.locator('article.card:visible a').click();
  assert.equal(await page.locator('h1').innerText(),'Review Workspace');
  assert.equal(await page.locator('.meta code').first().innerText(),'feature.review-workspace');
  assert.ok(await page.getByRole('link',{name:/View Markdown source/}).count()>0);
  await page.goto(base+'/catalog/',{waitUntil:'load'});
  // Distinguish executable references and keep their status separate from review maturity.
  assert.equal(await page.locator('article.card[data-interactive="true"]').count(),interactive.length);
  await page.locator('#interactive-only').check();
  assert.equal(await page.locator('article.card:visible').count(),interactive.length);
  assert.ok(await page.locator('article.card:visible .availability').first().innerText().then(s=>s.includes('Interactive reference')));
  await page.locator('#catalog-filter').fill('unmatchable_query_xzy');
  assert.equal(await page.locator('article.card:visible').count(),0);
  assert.equal(await page.locator('#empty-results').isVisible(),true);
  await page.locator('#clear-filters').click();
  assert.equal(await page.locator('#catalog-filter').inputValue(),'');
  assert.equal(await page.locator('#interactive-only').isChecked(),false);
  assert.equal(await page.locator('article.card:visible').count(),registry.length);
  const noJS=await browser.newPage({javaScriptEnabled:false});
  await noJS.goto(base+'/catalog/',{waitUntil:'load'});
  assert.equal(await noJS.locator('article.card').count(),registry.length,'browse stays usable without JS');
  assert.equal(await noJS.locator('#filter-controls').isVisible(),false,'JS-only filter controls are not shown as dead controls');
  assert.equal(await noJS.locator('article.card:visible').count(),registry.length);
  await noJS.setViewportSize({width:390,height:844});
  await noJS.screenshot({path:path.join(output,'phase3-catalog-nojs-mobile.png')});
  await noJS.close();

  for(const width of [320,375,768,1440]){
   await page.setViewportSize({width,height:900});
   await page.goto(base+'/catalog/',{waitUntil:'load'});
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
   if(overflow>2)note('Catalog overflows viewport '+width+'px by '+overflow+'px');
  }
  await phase3(browser,errors);
  await phase3CorrectionRegressions(browser);
  await page.setViewportSize({width:1440,height:900});
  await page.goto(base+'/catalog/components/button/',{waitUntil:'load'});
  const frame=page.frameLocator('iframe[title*="isolated interactive reference"]');
  await frame.locator('#scenario').selectOption('pending');
  assert.equal(await frame.locator('button.reference-button').isDisabled(),true);
  await frame.locator('#scenario').selectOption('default');
  await frame.locator('button.reference-button').click();
  assert.match(await frame.locator('#preview-result').innerText(),/No server action was performed/);
  await frame.locator('#theme').selectOption('dark');
  assert.equal(await frame.locator('html').getAttribute('data-theme'),'dark');
  await frame.locator('#reset').click();
  assert.equal(await frame.locator('#scenario').inputValue(),'default');
  assert.equal(await frame.locator('#theme').inputValue(),'light');

  // A correction is an interaction in the current scenario, not a scenario reset.
  for(const [component,value] of [['input','person@example.test'],['field','Research team']]){
   await page.goto(base+'/catalog/components/'+component+'/',{waitUntil:'load'});
   const control=page.frameLocator('iframe');
   await control.locator('#scenario').selectOption('invalid');
   await control.locator('.reference-control').fill(value);
   assert.equal(await control.locator('.reference-error').isVisible(),false);
   assert.equal(await control.locator('.reference-control').getAttribute('aria-invalid'),null);
   assert.equal(await control.locator('.reference-control').evaluate(el=>el===document.activeElement),true);
   await control.locator('#theme').selectOption('dark');
   assert.equal(await control.locator('.reference-control').inputValue(),value);
   await control.locator('.reference-control').fill('');
   assert.equal(await control.locator('.reference-error').isVisible(),true);
  }

  await page.goto(base+'/catalog/patterns/forms/',{waitUntil:'load'});
  const form=page.frameLocator('iframe');
  await form.locator('#scenario').selectOption('invalid');
  assert.equal(await form.locator('.pattern-errors').isVisible(),true);
  await form.locator('#scenario').selectOption('unknown');
  await form.locator('#demo-name').fill('Taylor');
  await form.locator('#demo-email').fill('taylor@example.test');
  await form.locator('button[type="submit"]').click();
  assert.equal(await form.locator('button[type="submit"]').isDisabled(),true);
  assert.match(await form.locator('.pattern-feedback').innerText(),/unknown/i);

  await page.goto(base+'/catalog/features/review-workspace/',{waitUntil:'load'});
  const review=page.frameLocator('iframe');
  await review.getByRole('button',{name:'Return for changes',exact:true}).click();
  await review.getByRole('textbox',{name:'Decision reason'}).fill('Please add a date.');
  assert.equal(await review.locator('#review-reason-error').isVisible(),false);
  assert.equal(await review.locator('#review-reason').getAttribute('aria-invalid'),null);
  await review.getByRole('button',{name:'Return for changes',exact:true}).click();
  await review.getByRole('button',{name:'Resolve simulated request'}).click();
  assert.equal(await review.locator('button[data-record]').count(),3);
  assert.equal(await review.getByRole('button',{name:'Community garden update · REV-101',exact:true}).count(),0);
  assert.equal(await review.getByRole('button',{name:'Approve',exact:true}).count(),0);
  assert.equal(await review.getByRole('button',{name:'Next pending item'}).evaluate(el=>el===document.activeElement),true);
  assert.equal(await review.locator('#preview-result').isVisible(),false);
  await review.getByRole('button',{name:'Next pending item'}).click();
  assert.equal(await review.locator('.review-detail h3').innerText(),'Accessible event announcement');
  assert.equal(await review.locator('.review-detail h3').evaluate(el=>el===document.activeElement),true);
  for(let count=3;count>0;count--){
   await review.getByRole('button',{name:'Approve',exact:true}).click();
   await review.getByRole('button',{name:'Resolve simulated request'}).click();
   assert.equal(await review.locator('button[data-record]').count(),count-1);
   if(count>1)await review.getByRole('button',{name:'Next pending item'}).click();
  }
  assert.match(await review.locator('.review-detail').innerText(),/All caught up/);
  assert.equal(await review.getByRole('button',{name:'Approve',exact:true}).count(),0);
  await page.screenshot({path:path.join(output,'review-completed.png'),fullPage:true});
  await review.locator('#scenario').selectOption('unknown');
  await review.getByRole('button',{name:'Approve',exact:true}).click();
  await review.getByRole('button',{name:'Resolve simulated request'}).click();
  assert.equal(await review.getByRole('button',{name:'Verify record status'}).count(),1);
  await review.getByRole('button',{name:'Verify record status'}).click();
  assert.match(await review.locator('.review-status').innerText(),/still unknown/i);
  assert.equal(await review.getByRole('button',{name:'Approve',exact:true}).count(),0);

  // Automated DOM checks run inside each sandboxed, opaque-origin frame.
  for(const entry of interactive){
   const route=entry.implementation.preview_path+'/';
   await page.goto(base+route,{waitUntil:'load'});
   const iframe=await page.locator('iframe').elementHandle();
   assert.ok(iframe,'preview iframe exists for '+entry.id);
   const content=await iframe.contentFrame();
   await content.waitForSelector('#scenario option',{state:'attached'});
   await content.addScriptTag({content:axe.source});
   const report=await content.evaluate(async()=>window.axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}}));
   const serious=report.violations.filter(v=>['critical','serious'].includes(v.impact));
   if(serious.length)note(entry.id+' axe serious/critical: '+serious.map(v=>v.id+' ('+v.nodes.length+')').join(', '));
   const results={id:entry.id,url:route,violations:report.violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.length,help:v.help}))};
   fs.writeFileSync(path.join(output,entry.id+'.json'),JSON.stringify(results,null,2));
  }
  await page.goto(base+'/catalog/features/review-workspace/',{waitUntil:'load'});
  await page.screenshot({path:path.join(output,'review-desktop.png'),fullPage:true});
  await page.setViewportSize({width:375,height:812});
  await page.screenshot({path:path.join(output,'review-mobile.png'),fullPage:true});
  if(errors.length)note('Page errors: '+errors.join(' | '));
  await page.close();
 } finally {await browser.close();}
}

/* Phase 3 regressions: F4 compact mobile filters, F9 URL-backed state, F8 detail navigation.
 * Viewports are CSS-pixel emulation in desktop Chromium; not physical-device or screen reader testing. */
const visibleCard=()=>{const c=document.querySelector('article.card:not([hidden])');if(!c)return null;
 const t=c.querySelector('h3').getBoundingClientRect();const b=c.querySelector('.availability').getBoundingClientRect();return {top:t.top,badge:b.bottom};};
const pageOverflow=p=>p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
async function state(p){return p.evaluate(()=>({q:document.getElementById('catalog-filter').value,
 interactive:document.getElementById('interactive-only').checked,
 category:document.querySelector('[data-filter][aria-pressed="true"]').dataset.filter,
 pressed:document.querySelectorAll('[data-filter][aria-pressed="true"]').length,
 visible:document.querySelectorAll('article.card:not([hidden])').length,
 count:document.getElementById('result-count').textContent,search:location.search,history:history.length}));}
async function phase3(browser,errors){
 const total=registry.length;
 // F4 — first result within the audit target at 390x844, categories collapsed, availability toggle visible.
 const mobile=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
 mobile.on('pageerror',e=>errors.push(e.message));
 for(const route of ['/catalog/','/search/']){
  await mobile.goto(base+route,{waitUntil:'load'});
  const first=await mobile.evaluate(visibleCard);
  if(first.top>640)note(route+' first result title top '+first.top+'px exceeds 640px at 390x844');
  if(first.badge>844)note(route+' first availability badge below the 844px fold');
  assert.equal(await mobile.locator('#category-panel').evaluate(el=>el.open),false,'categories collapse on narrow screens');
  assert.equal(await mobile.locator('#interactive-only').isVisible(),true);
  assert.equal(await mobile.locator('#result-count').isVisible(),true);
 }
 await mobile.screenshot({path:path.join(output,'phase3-search-mobile.png')});
 await mobile.goto(base+'/catalog/',{waitUntil:'load'});
 await mobile.locator('#category-panel summary').focus();
 await mobile.keyboard.press('Enter');
 assert.equal(await mobile.locator('#category-panel').evaluate(el=>el.open),true,'Enter opens category disclosure');
 await mobile.locator('[data-filter="patterns"]').focus();
 await mobile.keyboard.press('Space');
 assert.equal(await mobile.locator('[data-filter="patterns"]').getAttribute('aria-pressed'),'true');
 await mobile.locator('#category-panel summary').focus();
 await mobile.keyboard.press('Enter');
 assert.equal(await mobile.locator('#category-panel').evaluate(el=>el.open),false);
 assert.equal(await mobile.locator('#category-summary').innerText(),'Patterns','collapsed summary keeps active category');
 assert.match(await mobile.locator('#active-filters').innerText(),/1 filter active: Patterns/);
 assert.equal(await mobile.locator('#reset-filters').isVisible(),true);
 for(const [width,height] of [[320,700],[375,812],[768,900]]){
  await mobile.setViewportSize({width,height});
  for(const route of ['/catalog/','/search/']){
   await mobile.goto(base+route+'?category=patterns&interactive=1',{waitUntil:'load'});
   const overflow=await pageOverflow(mobile);
   if(overflow>2)note(route+' with filters overflows '+width+'px by '+overflow+'px');
  }
 }
 await mobile.close();

 // F9 — deep links, reload, fresh session, history policy, invalid input, clear on both routes.
 for(const route of ['/catalog/','/search/']){
  const u=await browser.newPage({reducedMotion:'reduce'});
  u.on('pageerror',e=>errors.push(e.message));
  const deep=base+route+'?utm=keep&q=button&category=components&interactive=1';
  await u.goto(deep,{waitUntil:'load'});
  let s=await state(u);
  assert.equal(s.q,'button');assert.equal(s.category,'components');assert.equal(s.pressed,1);assert.equal(s.interactive,true);
  assert.ok(s.visible>0&&s.visible<total,route+' deep link filters results');
  assert.equal(s.count,s.visible+' of '+total+' concepts');
  assert.match(s.search,/utm=keep/,'unrelated parameters are preserved');
  const deepState=s;
  await u.reload({waitUntil:'load'});
  s=await state(u);
  for(const key of ['q','category','interactive','visible','count'])assert.equal(s[key],deepState[key],'reload keeps '+key);
  const ctx=await browser.newContext();const shared=await ctx.newPage();
  await shared.goto(u.url(),{waitUntil:'load'});
  s=await state(shared);
  for(const key of ['q','category','interactive','visible','count'])assert.equal(s[key],deepState[key],'shared URL keeps '+key);
  await ctx.close();

  await u.goto(base+route,{waitUntil:'load'});
  const start=(await state(u)).history;
  await u.evaluate(()=>{window.__announcements=0;new MutationObserver(()=>{window.__announcements+=1;})
   .observe(document.getElementById('result-status'),{childList:true,characterData:true,subtree:true});});
  await u.locator('#catalog-filter').pressSequentially('dialog',{delay:40});
  await u.waitForTimeout(1300);
  s=await state(u);
  assert.equal(s.q,'dialog');assert.match(s.search,/q=dialog/);
  assert.equal(s.history,start,'typing replaces the history entry instead of adding one per keystroke');
  assert.ok(await u.evaluate(()=>window.__announcements)<=1,'status announces once after typing settles');
  assert.equal(await u.locator('#catalog-filter').evaluate(el=>el===document.activeElement),true,'focus stays in search');
  await u.locator('[data-filter="components"]').click();
  assert.equal((await state(u)).history,start+1);
  await u.locator('#interactive-only').check();
  s=await state(u);
  assert.equal(s.history,start+2);assert.match(s.search,/interactive=1/);assert.match(s.search,/category=components/);
  await u.goBack();
  s=await state(u);
  assert.equal(s.interactive,false);assert.equal(s.category,'components');assert.equal(s.q,'dialog');
  await u.goBack();
  s=await state(u);
  assert.equal(s.category,'all');assert.equal(s.q,'dialog');assert.equal(s.pressed,1);
  await u.goForward();
  s=await state(u);
  assert.equal(s.category,'components');assert.equal(s.count,s.visible+' of '+total+' concepts');
  assert.equal(new URL(u.url()).pathname,route,'no unintended route change');

  await u.goto(base+route+'?category=%3Cscript%3E&interactive=yes&q='+'x'.repeat(500),{waitUntil:'load'});
  s=await state(u);
  assert.equal(s.category,'all');assert.equal(s.interactive,false);assert.equal(s.q.length,200);
  assert.doesNotMatch(s.search,/category=|interactive=/,'invalid values are dropped from the canonical URL');
  assert.equal(await u.locator('script:not([src])').count(),0);

  await u.goto(base+route+'?q=unmatchable_query_xzy&category=patterns&interactive=1',{waitUntil:'load'});
  assert.equal(await u.locator('#empty-results').isVisible(),true);
  await u.locator('#clear-filters').click();
  s=await state(u);
  assert.equal(s.q,'');assert.equal(s.interactive,false);assert.equal(s.category,'all');assert.equal(s.visible,total);
  assert.equal(s.count,total+' of '+total+' concepts');assert.equal(s.search,'','clear returns URL to defaults');
  assert.equal(await u.locator('#catalog-filter').evaluate(el=>el===document.activeElement),true,'focus returns to search');
  assert.equal(await u.locator('#reset-filters').isVisible(),false);
  await u.close();
 }

 // F8 — jump navigation targets, keyboard activation, table scroll affordance, no page overflow.
 for(const [width,height] of [[390,844],[1440,900]]){
  const d=await browser.newPage({viewport:{width,height},reducedMotion:'reduce'});
  d.on('pageerror',e=>errors.push(e.message));
  await d.goto(base+'/catalog/components/button/',{waitUntil:'load'});
  assert.deepEqual(await d.locator('.jump-nav a').allInnerTexts(),['Example','Guidance','States','Source']);
  for(const link of await d.locator('.jump-nav a').all()){
   const hash=await link.getAttribute('href');
   await d.goto(base+'/catalog/components/button/',{waitUntil:'load'});
   await d.locator('.jump-nav a[href="'+hash+'"]').focus();
   await d.keyboard.press('Enter');
   await d.waitForFunction(h=>location.hash===h,hash);
   const top=await d.locator(hash).evaluate(el=>el.getBoundingClientRect().top);
   if(top<-1||top>height/2)note('jump '+hash+' did not bring its section into view at '+width+'px (top '+top+')');
  }
  if(width<600){
   await d.goto(base+'/catalog/components/button/#doc-states',{waitUntil:'load'});
   await d.screenshot({path:path.join(output,'phase3-button-states-mobile.png')});
   const wrap=d.locator('#doc-states');
   assert.equal(await wrap.getAttribute('data-overflow'),'true');
   assert.equal(await wrap.locator('.table-hint').isVisible(),true,'scroll hint visible on narrow screens');
   const region=wrap.locator('.table-scroll');
   assert.equal(await region.getAttribute('tabindex'),'0');
   await region.focus();
   for(let i=0;i<20;i++){await d.keyboard.press('ArrowRight');await d.waitForTimeout(40);}
   await region.evaluate(el=>new Promise(r=>setTimeout(r,300)));
   const reach=await region.evaluate(el=>{const last=el.querySelector('th:last-child').getBoundingClientRect();return last.right-el.getBoundingClientRect().right;});
   if(reach>2)note('rightmost table column not reachable by keyboard scrolling ('+reach+'px hidden)');
  } else {
   assert.equal(await d.locator('#doc-states').getAttribute('data-overflow'),'false');
   assert.equal(await d.locator('#doc-states .table-hint').isVisible(),false,'no hint when the table fits');
  }
  await d.goto(base+'/catalog/foundations/design-tokens/',{waitUntil:'load'});
  const spec=await d.locator('.jump-nav a').allInnerTexts();
  assert.ok(!spec.includes('Example')&&spec.includes('Guidance')&&spec.at(-1)==='Source','spec-only pages link no example');
  await d.close();
 }
 // Axe serious/critical on the changed shell pages (preview iframes are scanned separately above).
 for(const [width,height] of [[390,844],[1440,900]]){
  const a=await browser.newPage({viewport:{width,height}});
  for(const route of ['/catalog/','/search/?q=button&category=components&interactive=1','/catalog/components/button/','/catalog/foundations/design-tokens/']){
   await a.goto(base+route,{waitUntil:'load'});
   await a.addScriptTag({content:axe.source});
   const report=await a.evaluate(async()=>window.axe.run({exclude:[['iframe']]},{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}}));
   const serious=report.violations.filter(v=>['critical','serious'].includes(v.impact));
   if(serious.length)note(route+' at '+width+'px axe serious/critical: '+serious.map(v=>v.id+' ('+v.nodes.length+')').join(', '));
  }
  await a.close();
 }
 // 320px approximates 400% zoom of a 1280px window (reflow), not browser zoom itself.
 const narrow=await browser.newPage({viewport:{width:320,height:700},reducedMotion:'reduce'});
 await narrow.goto(base+'/catalog/',{waitUntil:'load'});
 const routes=await narrow.evaluate(()=>Array.from(document.querySelectorAll('article.card a'),a=>a.getAttribute('href')));
 assert.equal(routes.length,registry.length);
 for(const route of routes){
  await narrow.goto(base+route,{waitUntil:'domcontentloaded'});
  const overflow=await pageOverflow(narrow);
  if(overflow>2)note(route+' overflows 320px by '+overflow+'px');
 }
 await narrow.close();
}

/* History and disclosure corrections: full-page Chromium coverage. */
async function phase3CorrectionRegressions(browser){
 const results=[];
 const snap=async p=>p.evaluate(()=>({
  url:location.pathname+location.search,
  q:document.querySelector('#catalog-filter').value,
  category:document.querySelector('[data-filter][aria-pressed="true"]').dataset.filter,
  interactive:document.querySelector('#interactive-only').checked,
  visible:document.querySelectorAll('article.card:not([hidden])').length,
  history:history.length
 }));
 for(const route of ['/catalog/','/search/']){
  for(const action of ['patterns','checkbox','keyboard','reset']){
   for(const delay of (['patterns','checkbox'].includes(action)?[0,100,230]:[0])){
    const p=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
    try{
     await p.goto(base+route);
     const h=(await snap(p)).history;
     await p.locator('#catalog-filter').fill('form');
     if(delay)await p.waitForTimeout(delay);
     if(action==='patterns')await p.locator('[data-filter="patterns"]').click();
     else if(action==='checkbox')await p.locator('#interactive-only').check();
     else if(action==='keyboard'){await p.locator('[data-filter="patterns"]').focus();await p.keyboard.press('Enter');}
     else await p.locator('#reset-filters').click();
     const pushed=await snap(p);
     assert.equal(pushed.history,h+1);
     await p.goBack();
     const previous=await snap(p);
     assert.equal(previous.url,route+'?q=form',route+action+' previous URL');
     assert.equal(previous.q,'form');
     assert.equal(previous.category,'all');
     assert.equal(previous.interactive,false);
     await p.waitForTimeout(400);
     assert.deepEqual(await snap(p),previous,'late timer rewrote browser Back state');
     await p.goForward();
     assert.deepEqual(await snap(p),pushed,'Forward did not restore filters');
     if(route==='/catalog/'&&action==='patterns'&&delay===0){
      await p.goBack();
      await p.screenshot({path:path.join(output,'phase3-D01-back-preserves-query.png')});
     }
     results.push({route,action,delay,status:'PASS',pushed,previous});
    }finally{await p.close();}
   }
  }
  const p=await browser.newPage();
  try{
   await p.goto(base+route+'?q=form');
   await p.locator('[data-filter="patterns"]').click();
   await p.locator('#catalog-filter').fill('table');
   await p.goBack();
   await p.waitForTimeout(450);
   assert.equal((await snap(p)).url,route+'?q=form','popstate must cancel stale debounce');
   await p.goto(base+route);
   await p.locator('#catalog-filter').fill('table');
   await p.locator('[data-filter="components"]').click();
   await p.locator('#interactive-only').check();
   const full=await snap(p);
   await p.goBack();
   const cat=await snap(p);
   assert.equal(cat.url,route+'?q=table&category=components');
   await p.goBack();
   assert.equal((await snap(p)).url,route+'?q=table');
   await p.goForward();
   assert.deepEqual(await snap(p),cat);
   await p.goForward();
   assert.deepEqual(await snap(p),full);
   results.push({route,action:'two toggles + stale popstate',status:'PASS'});
  }finally{await p.close();}
 }
 const m=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
 try{
  await m.goto(base+'/catalog/');
  const ax=async()=>{
   const cdp=await m.context().newCDPSession(m);
   try{
    const {root}=await cdp.send('DOM.getDocument');
    const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:root.nodeId,selector:'#category-panel summary'});
    const {nodes}=await cdp.send('Accessibility.queryAXTree',{nodeId});
    const el=nodes.find(n=>n.role?.value==='DisclosureTriangle');
    return {name:el?.name?.value,expanded:el?.properties?.find(x=>x.name==='expanded')?.value?.value};
   }finally{await cdp.detach();}
  };
  await m.locator('#category-panel summary').focus();
  assert.deepEqual(await ax(),{name:'Category: All',expanded:false});
  await m.screenshot({path:path.join(output,'phase3-D02-category-390.png')});
  await m.keyboard.press('Enter');
  assert.deepEqual(await ax(),{name:'Category: All',expanded:true});
  await m.locator('[data-filter="patterns"]').click();
  assert.deepEqual(await ax(),{name:'Category: Patterns',expanded:true});
  results.push({action:'D02 disclosure AX name+expanded',status:'PASS'});
  await m.setViewportSize({width:768,height:900});
  await m.goto(base+'/search/');
  const pos=await m.evaluate(visibleCard);
  await m.screenshot({path:path.join(output,'phase3-D04-search-768x900.png')});
  assert.ok(pos.badge<=900,'768px first badge ends at '+pos.badge);
  assert.ok(await pageOverflow(m)<=2);
  results.push({action:'D04 768px search badge',status:'PASS developer Chromium only',pos});
 }finally{await m.close();}
 fs.writeFileSync(path.join(output,'phase3-QA-corrections.json'),JSON.stringify(results,null,2)+'\n');
 console.log('PASS '+results.length+' Phase 3 QA correction cases');
}

checks().then(()=>{
 if(issues.length){console.error(issues.length+' browser/a11y failures');process.exitCode=1;}
 else console.log('PASS: Chromium smoke, all preview frames axe serious/critical, screenshots and responsive shell');
}).catch(e=>{console.error(e.stack||e);process.exitCode=1;});
