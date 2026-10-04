const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {chromium} = require('playwright');
const os = require('node:os');
const base=fs.mkdtempSync(path.join(os.tmpdir(),'codexlab-ui-')), skill=path.resolve(process.argv[2] || path.join(__dirname,'../skills/codexlab'));
console.log('Browser artifacts: '+base);
const source=fs.readFileSync(path.join(skill,'assets/ui/role-picker.html'),'utf8');
const catalog=JSON.parse(fs.readFileSync(path.join(skill,'references/catalog.json'),'utf8'));
const slots=['pi','literature','method','experiment','reviewer'];
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_CHANNEL ? {channel:process.env.CHROMIUM_CHANNEL} : {})}), errors=[];
 try{
  async function fixture(mode='none',options=null,saved=null){
   const page=await browser.newPage({viewport:{width:736,height:1100},colorScheme:'light'});page.on('pageerror',error=>errors.push(error.message));
   await page.evaluate(({mode,saved})=>{
    window.calls=[];window.saves=[];window.clipboardTexts=[];
    Object.defineProperty(navigator,'clipboard',{configurable:true,value:['clipboard','clipboard-denied'].includes(mode) ? {writeText:async text=>{window.clipboardTexts.push(text);if(mode==='clipboard-denied')throw Error('Permission denied');}} : undefined});
    if(mode!=='none')window.openai={widgetState:saved,setWidgetState:value=>{window.saves.push(value);if(mode==='storage-fails')throw Error('storage unavailable');return Promise.resolve();}};
    if(['host','reject'].includes(mode))window.openai.sendFollowUpMessage=value=>{window.calls.push(value);return mode==='reject' ? Promise.reject(Error('cancelled')) : new Promise(resolve=>window.finish=resolve);};
   },{mode,saved});
   const html=options ? source.replace(/(<script id="codexlab-picker-options" type="application\/json">).*?(<\/script>)/s,'$1'+JSON.stringify(options)+'$2') : source;
   await page.setContent(html);return page;
  }
  async function chosen(page){return page.locator('.team [data-slot]').evaluateAll(nodes=>Object.fromEntries(nodes.map(node=>[node.dataset.slot,node.querySelector('.chosen-name').textContent])));}
  async function teamFor(page,goal='explore'){await page.locator(`[data-goal="${goal}"]`).click();await page.locator('.next').click();}
  const page=await fixture();
  assert.deepEqual(await page.locator('#codexlab-style-catalog').evaluate(node=>JSON.parse(node.textContent)),catalog);
  assert.equal(await page.locator('[data-goal]:visible').count(),4);
  assert.equal(await page.locator('.primary:visible').count(),1);
  assert.equal(await page.locator('.next').isDisabled(),true);
  assert.equal(await page.locator('.profiles').isVisible(),false);
  assert.equal(await page.locator('.confirm').isVisible(),false);
  assert.equal(await page.locator('[data-goal][aria-pressed="true"]').count(),0);
  await page.locator('.lab').screenshot({path:path.join(base,'start-desktop.png')});
  await teamFor(page);
  assert.deepEqual(await chosen(page),{pi:'Orion',literature:'Atlas',method:'Nova',experiment:'暂不启用',reviewer:'暂不启用'});
  assert.equal(await page.locator('.primary:visible').count(),1);
  assert.equal(await page.locator('.confirm').textContent(),'选中指令，手动复制');
  assert.equal(await page.locator('.prompt').isVisible(),false);
  assert.equal(await page.locator('.presets').isVisible(),false);
  await page.locator('[data-edit="method"]').click();
  assert.equal(await page.locator('.category-select').inputValue(),'method');
  assert.equal(await page.locator('[data-profile]:visible').count(),3);
  await page.locator('[data-profile="Theo"]').click();
  assert.equal((await chosen(page)).method,'Theo');
  assert.equal((await chosen(page)).literature,'Atlas');
  await page.locator('.back-team').click();
  assert.ok((await page.locator('.reason').textContent()).includes('按你的选择调整'));
  await page.locator('.back-start').click();
  assert.equal((await chosen(page)).method,'Theo','Back navigation must preserve adjustment');
  await page.locator('[data-goal="explore"]').click();
  assert.equal((await chosen(page)).method,'Theo','Re-selecting the same use must not discard an adjusted team');
  await page.locator('.next').click();
  assert.equal((await chosen(page)).method,'Theo');
  await page.locator('.advanced summary').click();
  for(const preset of catalog.presets){await page.locator(`[data-preset="${preset.id}"]`).click();assert.deepEqual(await chosen(page),Object.fromEntries(slots.map(id=>[id,preset.selection[id] || '暂不启用'])));}
  await page.locator('[data-edit="pi"]').click();assert.equal(await page.locator('.disable-role').isVisible(),false);
  for(const id of slots.slice(1)){await page.locator('.category-select').selectOption(id);await page.locator('.disable-role').click();assert.equal((await page.locator('.profile-detail').textContent()).trim(),'');}
  await page.locator('.back-team').click();assert.ok((await page.locator('.team-size').textContent()).includes('当前 1 个角色'));
  await page.locator('.confirm').click();
  assert.equal(await page.locator('.command').getAttribute('open'),'');
  assert.equal(await page.locator('.prompt').evaluate(node=>node.selectionEnd-node.selectionStart),(await page.locator('.prompt').inputValue()).length);
  assert.equal(await page.evaluate(()=>window.calls.length),0);
  const clipboard=await fixture('clipboard');await teamFor(clipboard,'idea');await clipboard.locator('.confirm').click();
  assert.equal(await clipboard.evaluate(()=>window.clipboardTexts.length),1);assert.ok((await clipboard.locator('.status').textContent()).includes('发送后，才会确认'));
  assert.equal(await clipboard.evaluate(()=>window.calls.length),0);
  const denied=await fixture('clipboard-denied');await teamFor(denied);await denied.locator('.confirm').click();
  assert.equal(await denied.locator('.confirm').textContent(),'选中指令，手动复制');assert.equal(await denied.locator('.prompt').isVisible(),true);
  await denied.locator('.confirm').click();assert.equal(await denied.evaluate(()=>window.clipboardTexts.length),1,'Denied clipboard falls back to manual selection without repeated writes');
  const live=await fixture('host');await teamFor(live,'experiment');
  assert.deepEqual(await live.evaluate(()=>[window.calls.length,window.saves.length>0]),[0,true]);
  await live.locator('.confirm').click();assert.equal(await live.locator('.back-start').isDisabled(),true);assert.equal(await live.locator('[data-edit="method"]').isDisabled(),true);
  await live.locator('.confirm').evaluate(node=>node.click());assert.equal(await live.evaluate(()=>window.calls.length),1);
  assert.equal(await live.evaluate(()=>window.calls[0].prompt),'$codexlab 团队配置：PI=Aster；文献=Atlas；方法=Nova；实验=Forge；审查=Sage。先只配置团队，不开始研究。');
  await live.evaluate(()=>window.finish());await live.waitForFunction(()=>document.querySelector('.status').textContent.includes('以聊天回复为准'));
  assert.equal(await live.locator('.confirm').isDisabled(),true);assert.equal(await live.locator('[data-step="chat"]').getAttribute('aria-current'),'step');
  const rejected=await fixture('reject');await teamFor(rejected);await rejected.locator('.confirm').click();assert.equal(await rejected.evaluate(()=>window.calls.length),1);assert.equal(await rejected.locator('.confirm').isDisabled(),false);assert.equal(await rejected.locator('.prompt').isVisible(),true);
  const legacy=await fixture('state',null,{modelContent:{prototype:'CodexLab v2',selected:['Atlas','Nova','Forge','Sage','Unknown'],scope:'team-configuration-only'}});
  assert.equal(await legacy.locator('.team-view').isVisible(),true);assert.equal((await chosen(legacy)).pi,'Aster');assert.deepEqual(await legacy.evaluate(()=>[window.calls.length,window.saves.length]),[0,0]);
  await legacy.locator('[data-edit="method"]').click();
  await legacy.evaluate(()=>window.dispatchEvent(new CustomEvent('openai:set_globals',{detail:{globals:{widgetState:{modelContent:{prototype:'CodexLab v2',schemaVersion:2,selection:{pi:'Quinn',literature:'Atlas',method:'Mira',experiment:null,reviewer:'Sage'},scope:'team-configuration-only'}}}}})));
  assert.equal(await legacy.locator('.edit-view').isVisible(),true,'Delayed state must not interrupt an opened editor');
  assert.equal((await chosen(legacy)).pi,'Aster');
  const explicit={selection:{pi:'Quinn',literature:'Flint',method:'Mira',experiment:null,reviewer:'Rook'},ignoreSavedState:true};
  const confirmed=await fixture('state',explicit,{modelContent:{prototype:'CodexLab v2',schemaVersion:2,selection:{pi:'Aster',literature:'Atlas',method:'Nova',experiment:'Forge',reviewer:'Sage'},scope:'team-configuration-only'}});
  assert.equal((await chosen(confirmed)).pi,'Quinn');assert.ok((await confirmed.locator('.draft-note').textContent()).includes('已确认'));
  await confirmed.locator('[data-edit="method"]').click();await confirmed.locator('.back-team').click();assert.ok((await confirmed.locator('.draft-note').textContent()).includes('已确认'),'Navigation alone must not relabel an unchanged confirmed team');
  const draft=await fixture('state');await teamFor(draft,'idea');const draftPrompt=await draft.locator('.prompt').inputValue();
  await draft.evaluate(()=>window.dispatchEvent(new CustomEvent('openai:set_globals',{detail:{globals:{widgetState:{modelContent:{prototype:'CodexLab v2',schemaVersion:2,selection:{pi:'Aster',literature:'Atlas',method:'Nova',experiment:null,reviewer:null},scope:'team-configuration-only'}}}}})));
  assert.equal(await draft.locator('.prompt').inputValue(),draftPrompt,'Delayed state must not overwrite a local choice');
  const hydration=await fixture('state');await hydration.evaluate(()=>window.dispatchEvent(new CustomEvent('openai:set_globals',{detail:{globals:{widgetState:{modelContent:{prototype:'CodexLab v2',schemaVersion:2,selection:{pi:'Quinn',literature:'Atlas',method:'Mira',experiment:null,reviewer:'Sage'},scope:'team-configuration-only'}}}}})));
  assert.equal(await hydration.locator('.team-view').isVisible(),true);assert.equal((await chosen(hydration)).pi,'Quinn');
  const storage=await fixture('storage-fails');await teamFor(storage);assert.equal((await chosen(storage)).pi,'Orion');
  const keyboard=await fixture();await keyboard.locator('[data-goal="explore"]').focus();await keyboard.keyboard.press('Enter');await keyboard.locator('.next').focus();await keyboard.keyboard.press('Enter');
  assert.equal(await keyboard.locator('.team-view').isVisible(),true);await keyboard.locator('[data-edit="method"]').focus();await keyboard.keyboard.press('Enter');await keyboard.locator('.category-select').selectOption('experiment');assert.equal(await keyboard.locator('.panel-title').textContent(),'实验科学家');
  const layouts=[];
  for(const width of [320,390,736]){
   const preview=await fixture();await preview.setViewportSize({width,height:1100});
   const startHeight=await preview.locator('.lab').evaluate(root=>Math.ceil(root.getBoundingClientRect().height));await preview.locator('.lab').screenshot({path:path.join(base,`start-${width}.png`)});
   await teamFor(preview);const teamHeight=await preview.locator('.lab').evaluate(root=>Math.ceil(root.getBoundingClientRect().height));
   assert.ok(await preview.locator('#codexlab-role-picker').evaluate(root=>root.scrollWidth<=root.clientWidth));
   await preview.locator('.lab').screenshot({path:path.join(base,`team-${width}.png`)});
   await preview.locator('[data-edit="method"]').click();assert.ok(await preview.locator('#codexlab-role-picker').evaluate(root=>root.scrollWidth<=root.clientWidth));await preview.locator('.lab').screenshot({path:path.join(base,`edit-${width}.png`)});
   await preview.locator('.back-team').click();await preview.locator('.confirm').click();await preview.waitForFunction(()=>{const prompt=document.querySelector('.prompt');return prompt.scrollHeight<=prompt.clientHeight;});
   layouts.push({width,startHeight,teamHeight,overflow:false});
  }
  await clipboard.emulateMedia({colorScheme:'dark'});await clipboard.locator('.lab').screenshot({path:path.join(base,'team-dark.png')});
  assert.deepEqual(errors,[]);
  const result={firstScreen:'four uses; no preselection; one primary action',teamReview:'Chinese responsibilities + per-row editing',profileAndPresetSelection:'PASS',navigationPreservesChoice:'PASS',clipboardAndManualFallback:'PASS',hostBridge:'PASS (mock)',noAutomaticResearchOrSend:true,legacyAndExplicitAndDelayedState:'PASS',keyboard:'native buttons/select PASS',layouts,pageErrors:errors};
  fs.writeFileSync(path.join(base,'browser-results.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
