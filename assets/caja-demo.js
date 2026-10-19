// Animación «Así se usa la caja» (página del Repositorio digital).
// Reproduce la Caja de herramientas actual con sus datos reales (/herramientas/tools.js):
// - buscar: solo aparecen las fichas que coinciden;
// - elegir qué quieres hacer: la categoría se despliega en lágrima, con sus pestañas, y se ve la ficha;
// - «Detalles» abre más ideas para clase y «Abrir» lleva a la herramienta.
// Las cuatro categorías replican TASKS de /herramientas/index.html: si cambian allí, cambiarlas aquí.
(()=>{
 const R=document.getElementById('cd');
 if(!R||typeof TOOLS==='undefined'||typeof SECTIONS==='undefined')return;
 const GOALS=[
  ['aula:geohis','aula:cienc','aula:arte','aula:ia','aula:equipo','recursos:sa','recursos:form'],
  ['aula:crear','docente:crear','docente:ia','recursos:img'],
  ['aula:part','docente:eval'],
  ['docente:gestion','docente:org']
 ];
 // escenas: una búsqueda (q) o un objetivo elegido, y la herramienta que muestra la caja
 const SCENES=[{q:'línea del tiempo',id:'timetoast'},{id:'kahoot'},{id:'geogebra'}]
  .map(s=>({...s,t:TOOLS.find(t=>t.id===s.id)})).filter(s=>s.t)
  .map(s=>({...s,key:s.t.s+':'+s.t.cat,k:GOALS.findIndex(g=>g.includes(s.t.s+':'+s.t.cat))})).filter(s=>s.k>=0);
 if(!SCENES.length)return;
 const esc=x=>String(x).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 const short=x=>/^no necesita/i.test(x)?'Sin cuenta':String(x).split(/;| \(/)[0].trim();
 const Q=R.querySelector('.cd-q'),SUB=R.querySelector('.cd-sub'),B=R.querySelector('.cd-pause');
 const slotB=R.querySelector('.cd-browse .cd-slot'),slotR=R.querySelector('.cd-res .cd-slot'),stage=R.querySelector('.cd-stage');
 const tabs=[...R.querySelectorAll('.cd-tab')];
 const card=t=>{const aula=t.s==='aula',name=t.n.replace(/\s*\(.*\)/,'');
  const facts=aula?[t.c,short(t.cta)]:[short(t.coste)];
  return `<div class="cd-card"><div class="cd-ch"><span class="cd-lg"><img src="/herramientas/logos/${t.id}.png?v=3" alt="" width="19" height="19" onerror="this.replaceWith(document.createTextNode('${esc(name[0])}'))"></span><b>${esc(name)}</b></div>`+
   `<p class="cd-lead">${esc(aula?t.a:t.p)}</p><p class="cd-ex"><b>Ejemplo:</b> ${esc(t.i[0])}</p>`+
   `<div class="cd-facts">${facts.map(f=>`<span class="${/^sin cuenta|gratu|incluido/i.test(f)?'ok':''}">${esc(f)}</span>`).join('')}</div>`+
   `<div class="cd-more"><span class="cd-mh">Más ideas para clase</span><ul>${t.i.slice(1).map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`+
   `<div class="cd-foot"><span class="cd-open">Abrir ↗</span><span class="cd-det">Detalles</span></div></div>`;};
 // pestañas de la categoría elegida: las categorías de los datos que tienen herramientas
 const subs=k=>GOALS[k].filter(key=>TOOLS.some(t=>t.s+':'+t.cat===key)).map(key=>{const [s,c]=key.split(':');return {key,n:SECTIONS[s].cats[c]};});
 const drawSub=(k,sel)=>{SUB.innerHTML=subs(k).map(x=>`<span data-key="${x.key}" class="${x.key===sel?'on':''}">${esc(x.n)}</span>`).join('');};
 const C=()=>R.querySelector('.cd-card');
 // altura de la escena más alta con los detalles abiertos: la animación no hace saltar la página
 const reserve=()=>{stage.style.minHeight='';const keep=[R.className,slotB.innerHTML,slotR.innerHTML,SUB.innerHTML];let mx=0;
  SCENES.forEach(s=>{R.className='cd shown open'+(s.q?' search':'');drawSub(s.k,s.key);(s.q?slotR:slotB).innerHTML=card(s.t);C().classList.add('more');mx=Math.max(mx,stage.offsetHeight);(s.q?slotR:slotB).innerHTML='';});
  [R.className,slotB.innerHTML,slotR.innerHTML,SUB.innerHTML]=keep;stage.style.minHeight=mx+'px';};
 const still=matchMedia('(prefers-reduced-motion: reduce)');
 let i=0,timers=[],paused=false,seen=true;
 const clear=()=>{timers.forEach(clearTimeout);timers=[];};
 const at=(ms,f)=>timers.push(setTimeout(f,ms));
 const reset=()=>{R.className='cd';R.dataset.s='1';tabs.forEach(x=>x.classList.remove('on','press'));Q.textContent='';slotB.innerHTML='';slotR.innerHTML='';SUB.innerHTML='';};
 const play=()=>{clear();const sc=SCENES[i%SCENES.length];reset();
  let t0=600;
  if(sc.q){
   at(t0,()=>R.classList.add('search'));
   [...sc.q].forEach((ch,n)=>at(t0+n*70,()=>{Q.textContent+=ch}));t0+=sc.q.length*70+400;
   at(t0,()=>{R.classList.add('search');slotR.innerHTML=card(sc.t);R.classList.add('shown');R.dataset.s='2';});
  }else{
   at(t0,()=>tabs[sc.k].classList.add('press'));t0+=500;
   const list=subs(sc.k),first=list[0].key;
   at(t0,()=>{tabs[sc.k].classList.remove('press');tabs[sc.k].classList.add('on');R.classList.add('open');drawSub(sc.k,first);R.dataset.s='2';
    if(first===sc.key){slotB.innerHTML=card(sc.t);R.classList.add('shown');}});
   if(first!==sc.key){t0+=900;
    at(t0,()=>SUB.querySelector(`[data-key="${sc.key}"]`).classList.add('press'));
    at(t0+250,()=>{drawSub(sc.k,sc.key);slotB.innerHTML=card(sc.t);R.classList.add('shown');});t0+=250;}
  }
  at(t0+1700,()=>C()&&C().classList.add('pressd'));
  at(t0+2000,()=>{const c=C();if(c){c.classList.remove('pressd');c.classList.add('more');}});
  at(t0+4400,()=>{R.dataset.s='3';});
  at(t0+6000,()=>{i++;if(!paused&&seen)play();});};
 const showStill=()=>{clear();reset();const sc=SCENES.find(s=>!s.q)||SCENES[0];
  if(sc.q){R.className='cd shown search';Q.textContent=sc.q;slotR.innerHTML=card(sc.t);}
  else{R.className='cd shown open';tabs[sc.k].classList.add('on');drawSub(sc.k,sc.key);slotB.innerHTML=card(sc.t);}
  C().classList.add('more');R.dataset.s='2';};
 const icon=p=>p?'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5v14l12-7z"/></svg>':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
 const setPause=p=>{paused=p;B.innerHTML=icon(p);B.setAttribute('aria-label',p?'Reanudar la animación':'Pausar la animación');if(p)clear();else play();};
 const start=()=>{if(still.matches){B.hidden=true;showStill();}else{B.hidden=false;paused=false;B.innerHTML=icon(false);play();}};
 B.addEventListener('click',()=>setPause(!paused));
 still.addEventListener('change',start);
 R.hidden=false;reserve();
 let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(reserve,200)});
 if(document.fonts)document.fonts.ready.then(reserve);
 if('IntersectionObserver' in window)new IntersectionObserver(([e])=>{const was=seen;seen=e.isIntersecting;if(seen&&!was&&!paused&&!still.matches)play();if(!seen)clear();}).observe(R);
 document.addEventListener('visibilitychange',()=>{if(document.hidden)clear();else if(seen&&!paused&&!still.matches)play();});
 start();
})();
