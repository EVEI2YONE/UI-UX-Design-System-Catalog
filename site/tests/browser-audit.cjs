/* Browser verification for the read-only UI/UX documentation site.
 * CI checks the catalog shell; it does not certify consuming applications.
 */
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const {chromium}=require('playwright');
const axe=require('axe-core');
const base=process.env.CATALOG_BASE_URL||'http://127.0.0.1:8765';
const entries=require('../../catalog/index.json').entries;
const out=path.join(__dirname,'..','artifacts','browser');
fs.mkdirSync(out,{recursive:true});

async function axeCheck(page, route, results) {
  await page.goto(base+route,{waitUntil:'load'});
  await page.addScriptTag({content:axe.source});
  const report=await page.evaluate(async()=>window.axe.run(document,{
    runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}
  }));
  const severe=report.violations.filter(v=>['serious','critical'].includes(v.impact));
  results.push({route,violations:severe.map(v=>({
    id:v.id,impact:v.impact,nodes:v.nodes.length,description:v.description
  }))});
  assert.equal(severe.length,0,route+' severe axe issues: '+severe.map(v=>v.id).join(', '));
}

async function run() {
  assert.equal(entries.length,new Set(entries.map(e=>e.id)).size);
  assert.ok(entries.length>=92);
  assert.ok(entries.every(e=>!Object.hasOwn(e,'implementation')),
    'The catalog must contain no executable component registrations');
  const browser=await chromium.launch({headless:true});
  const results=[],jsErrors=[];
  try {
    const page=await browser.newPage({viewport:{width:1440,height:900},reducedMotion:'reduce'});
    page.on('pageerror',err=>jsErrors.push(err.message));
    await page.goto(base+'/tasks/',{waitUntil:'load'});
    assert.equal(await page.locator('article.task-card').count(),7);
    assert.equal(await page.getByRole('link',{name:'Narrow a long list'}).getAttribute('href'),
      '/catalog/patterns/search-filter/');
    await page.goto(base+'/catalog/',{waitUntil:'load'});
    assert.equal(await page.locator('article.card').count(),entries.length);
    assert.equal(await page.locator('[data-interactive]').count(),0);
    assert.equal(await page.locator('#interactive-only').count(),0);
    assert.equal(await page.locator('article.card .kind-label').count(),entries.length);
    assert.equal(await page.locator('iframe').count(),0);
    await page.locator('#catalog-filter').fill('recover from a failed submission');
    assert.ok(await page.locator('article.card:visible a[href="/catalog/patterns/forms/"]').count()>0);
    await page.locator('#catalog-filter').fill('human approval queue');
    assert.equal(await page.locator('article.card:visible').count(),1);
    assert.equal(await page.locator('article.card:visible a').getAttribute('href'),
      '/catalog/features/review-workspace/');
    await page.locator('article.card:visible a').click();
    assert.equal(await page.locator('h1').innerText(),'Review Workspace');
    assert.equal(await page.locator('.meta code').first().innerText(),'feature.review-workspace');
    assert.equal(await page.locator('.meta').getByText('Implementation').count(),0);
    assert.equal(await page.locator('iframe').count(),0);
    assert.equal(await page.getByRole('link',{name:/View Markdown source/}).count(),1);
    assert.equal(await page.locator('.jump-nav a').filter({hasText:'Example'}).count(),0);
    results.push({check:'task-first and canonical source discovery',pass:true});

    await page.goto(base+'/search/?utm=keep&q=button&category=components&interactive=1',{waitUntil:'load'});
    assert.equal(await page.locator('#catalog-filter').inputValue(),'button');
    assert.equal(await page.locator('[data-filter="components"]').getAttribute('aria-pressed'),'true');
    assert.ok((await page.locator('article.card:visible').count())>0);
    assert.ok(!new URL(page.url()).searchParams.has('interactive'),
      'Legacy preview-only links must be canonicalized without preview filtering');
    assert.equal(new URL(page.url()).searchParams.get('utm'),'keep');
    await page.locator('#catalog-filter').fill('unmatchable_query_xzy');
    assert.equal(await page.locator('article.card:visible').count(),0);
    assert.equal(await page.locator('#empty-results').isVisible(),true);
    await page.locator('#clear-filters').click();
    assert.equal(await page.locator('#catalog-filter').inputValue(),'');
    assert.equal(await page.locator('article.card:visible').count(),entries.length);
    results.push({check:'filtering, URL migration and reset',pass:true});

    await page.goto(base+'/catalog/?q=table',{waitUntil:'load'});
    assert.equal(await page.locator('#catalog-filter').inputValue(),'table');
    await page.locator('[data-filter="patterns"]').click();
    assert.equal(new URL(page.url()).searchParams.get('category'),'patterns');
    await page.goBack({waitUntil:'load'});
    assert.equal(new URL(page.url()).searchParams.get('category'),null);
    assert.equal(await page.locator('#catalog-filter').inputValue(),'table');
    results.push({check:'browser history restores documentation filters',pass:true});

    await page.goto(base+'/search/?category=%3Cscript%3E&interactive=yes&q='+'x'.repeat(500),{waitUntil:'load'});
    assert.equal((await page.locator('#catalog-filter').inputValue()).length,200);
    assert.equal(await page.locator('[data-filter="all"]').getAttribute('aria-pressed'),'true');
    assert.ok(!new URL(page.url()).searchParams.has('interactive'));
    assert.ok(!new URL(page.url()).searchParams.has('category'));
    assert.equal(await page.locator('script:not([src])').count(),0);
    results.push({check:'safe URL state and no inline executable preview source',pass:true});

    const noJS=await browser.newPage({javaScriptEnabled:false,viewport:{width:390,height:844}});
    await noJS.goto(base+'/catalog/',{waitUntil:'load'});
    assert.equal(await noJS.locator('article.card:visible').count(),entries.length);
    assert.equal(await noJS.locator('#filter-controls').isVisible(),false);
    await noJS.screenshot({path:path.join(out,'catalog-nojs-mobile.png')});
    await noJS.close();

    const component='/catalog/components/button/';
    await page.goto(base+component,{waitUntil:'load'});
    assert.equal(await page.locator('iframe').count(),0);
    assert.equal(await page.locator('.meta').getByText('Review status').count(),1);
    const nav=await page.locator('.jump-nav a').allInnerTexts();
    assert.equal(nav.at(0),'Guidance');
    assert.equal(nav.at(-1),'Source');
    assert.ok(nav.includes('States'));
    for(const href of await page.locator('.jump-nav a').evaluateAll(xs=>xs.map(x=>x.getAttribute('href')))){
      assert.ok(await page.locator(href).count()>0,'jump target '+href);
    }
    await page.screenshot({path:path.join(out,'component-guidance-desktop.png')});
    results.push({check:'component concept page remains documentation-only',pass:true});

    for(const width of [320,375,768,1440]) {
      await page.setViewportSize({width,height:900});
      for(const route of ['/catalog/','/catalog/components/button/']) {
        await page.goto(base+route,{waitUntil:'load'});
        const over=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
        assert.ok(over<=2,route+' overflows '+width+' viewport by '+over+' px');
      }
    }
    await page.setViewportSize({width:390,height:844});
    await page.goto(base+'/catalog/',{waitUntil:'load'});
    await page.screenshot({path:path.join(out,'catalog-mobile.png')});
    results.push({check:'reflow across 320, 375, 768, 1440 px',pass:true});

    const audit=await browser.newPage({viewport:{width:1280,height:900},reducedMotion:'reduce'});
    for(const route of ['/','/tasks/','/catalog/','/search/?q=button&category=components',
                        component,'/catalog/features/review-workspace/',
                        '/catalog/foundations/design-tokens/']){
      await axeCheck(audit,route,results);
    }
    await audit.close();
    assert.deepEqual(jsErrors,[]);
    fs.writeFileSync(path.join(out,'documentation-browser-audit.json'),JSON.stringify({
      catalogCount:entries.length,checks:results,jsErrors,environment:'desktop Chromium emulation',
      limitations:'No physical mobile, screen-reader, product service or user study conformance claim'
    },null,2)+'\n');
    console.log('PASS: '+entries.length+' documentation entries; '+results.length+
      ' browser/axe checks; no preview frames, serious/critical axe findings or JS errors');
  } finally {await browser.close();}
}
run().catch(err=>{console.error(err.stack||err);process.exitCode=1;});
