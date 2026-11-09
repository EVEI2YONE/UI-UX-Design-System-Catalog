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
  await page.locator('#catalog-filter').fill('unmatchable_query_xzy');
  assert.equal(await page.locator('article.card:visible').count(),0);
  assert.equal(await page.locator('#empty-results').isVisible(),true);
  await page.locator('#catalog-filter').fill('');
  const noJS=await browser.newPage({javaScriptEnabled:false});
  await noJS.goto(base+'/catalog/',{waitUntil:'load'});
  assert.equal(await noJS.locator('article.card').count(),registry.length,'browse stays usable without JS');
  await noJS.close();

  for(const width of [320,375,768,1440]){
   await page.setViewportSize({width,height:900});
   await page.goto(base+'/catalog/',{waitUntil:'load'});
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
   if(overflow>2)note('Catalog overflows viewport '+width+'px by '+overflow+'px');
  }
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
checks().then(()=>{
 if(issues.length){console.error(issues.length+' browser/a11y failures');process.exitCode=1;}
 else console.log('PASS: Chromium smoke, all preview frames axe serious/critical, screenshots and responsive shell');
}).catch(e=>{console.error(e.stack||e);process.exitCode=1;});
