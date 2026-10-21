// Comportamiento común de todas las páginas
(()=>{
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
// aparición escalonada al hacer scroll
const els=[...document.querySelectorAll('.rv')];
if('IntersectionObserver' in window&&!reduce){
 const io=new IntersectionObserver(es=>{
  es.filter(e=>e.isIntersecting).forEach((e,i)=>{e.target.style.transitionDelay=(i*70)+'ms';e.target.classList.add('in');io.unobserve(e.target);});
 },{threshold:.08});
 els.forEach(el=>io.observe(el));
}else els.forEach(el=>el.classList.add('in'));
// foco que sigue al ratón dentro de cada tarjeta
document.querySelectorAll('.t').forEach(t=>t.addEventListener('pointermove',e=>{
 const r=t.getBoundingClientRect();t.style.setProperty('--mx',(e.clientX-r.left)+'px');t.style.setProperty('--my',(e.clientY-r.top)+'px');
}));
// animaciones solo cuando se ven
if('IntersectionObserver' in window){const vo=new IntersectionObserver(es=>es.forEach(e=>e.target.classList.toggle('play',e.isIntersecting)),{threshold:.2});document.querySelectorAll('.viz').forEach(v=>vo.observe(v));}else document.querySelectorAll('.viz').forEach(v=>v.classList.add('play'));
// barra superior pegada arriba
const f=()=>document.body.classList.toggle('stuck',scrollY>8);addEventListener('scroll',f,{passive:true});f();
// los personajes del Consejo hablan por turnos
const m=document.querySelectorAll('.council span');
if(m.length&&!reduce){let i=0;setInterval(()=>{m.forEach(e=>e.classList.remove('talk'));m[i%m.length].classList.add('talk');i++},1400)}
// cintas de «Con qué trabajo»: se duplica la lista solo para el bucle visual, oculta a lectores de pantalla
if(!reduce)document.querySelectorAll('.marq .track').forEach(t=>{[...t.children].forEach(li=>{const c=li.cloneNode(true);c.setAttribute('aria-hidden','true');t.appendChild(c)});t.closest('.marq').classList.add('loop')});
// categorías del índice de proyectos: «Todos» y tres pestañas; la elegida queda marcada y se ven sus proyectos (flechas para moverse)
const ct=[...document.querySelectorAll('.ct')];
if(ct.length){
 const sel=(b,focus)=>{ct.forEach(x=>{const on=x===b;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;const p=document.getElementById(x.getAttribute('aria-controls'));p.hidden=!on;if(on)p.querySelectorAll('.rv').forEach(r=>r.classList.add('in'));});if(focus)b.focus();};
 ct.forEach((b,i)=>{b.addEventListener('click',()=>sel(b));
  b.addEventListener('keydown',e=>{const k={ArrowRight:1,ArrowLeft:-1}[e.key];if(k){e.preventDefault();sel(ct[(i+k+ct.length)%ct.length],true);}});});
 // si se llega con #categoría (por ejemplo /proyectos/#aula), se elige esa
 const h=location.hash.slice(1),pre=ct.find(b=>b.id==='cg-'+h);if(pre)sel(pre);}
// El Consejo de Clío: las seis caras hablan por turnos (se puede pulsar en cada una y pausar)
document.querySelectorAll('.cq-board').forEach(bd=>{
 const team=bd.querySelector('.cq-team'),ms=[...team.querySelectorAll('.cq-m')],say=bd.querySelector('.cq-say'),line=team.querySelector('.cq-line i'),play=bd.querySelector('.cq-play');
 const red=matchMedia('(prefers-reduced-motion: reduce)').matches;let i=0,run=!red,t=null,vis=false;
 const col=m=>m.querySelector('svg').style.getPropertyValue('--c');
 const set=k=>{i=k;const last=ms.length-1;
  ms.forEach((m,j)=>{const on=j===k;m.classList.toggle('on',on);m.classList.toggle('talk',on&&!red);m.setAttribute('aria-pressed',on);m.classList.toggle('rev',k===last&&j<last);});
  if(line)line.style.setProperty('--p',k/last);
  const m=ms[k];say.style.setProperty('--c',col(m));
  say.querySelector('.cq-k').textContent=k+1;say.querySelector('b').textContent=m.dataset.n;say.querySelector('.cq-r').textContent=m.dataset.r;say.querySelector('p').textContent=m.dataset.t;
  const f=m.querySelector('.cq-face').getBoundingClientRect(),r=say.getBoundingClientRect();say.style.setProperty('--x',(f.left+f.width/2-r.left)+'px');};
 const go=()=>{clearInterval(t);t=null;if(run&&vis)t=setInterval(()=>set((i+1)%ms.length),2600);};
 const lab=()=>{play.textContent=run?'Pausar':'Reproducir';play.setAttribute('aria-label',run?'Pausar la animación':'Reproducir la animación');};
 ms.forEach((m,j)=>{m.style.setProperty('--c',col(m));m.addEventListener('click',()=>{run=false;lab();go();set(j);});});
 play.addEventListener('click',()=>{run=!run;lab();if(run)set((i+1)%ms.length);go();});
 lab();
 new IntersectionObserver(es=>es.forEach(e=>{vis=e.isIntersecting;go();}),{threshold:.35}).observe(bd);
 // el bocadillo guarda siempre el alto del texto más largo: así lo de debajo no se mueve al cambiar de pensador
 const fit=()=>{say.style.minHeight='';const p=say.querySelector('p'),nb=say.querySelector('b'),nr=say.querySelector('.cq-r'),keep=[p.textContent,nb.textContent,nr.textContent];let h=0;
  ms.forEach(m=>{p.textContent=m.dataset.t;nb.textContent=m.dataset.n;nr.textContent=m.dataset.r;h=Math.max(h,say.offsetHeight);});
  [p.textContent,nb.textContent,nr.textContent]=keep;say.style.minHeight=h+'px';};
 fit();if(document.fonts)document.fonts.ready.then(fit);
 addEventListener('resize',()=>{fit();set(i);});set(0);
});
})();

// logo del menú: al pulsarlo, el templo hace su animación y después va al inicio
document.addEventListener('click',e=>{const b=e.target.closest('.brand');if(!b||e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;
 if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
 e.preventDefault();b.classList.remove('tap');void b.offsetWidth;b.classList.add('tap');
 setTimeout(()=>{if(new URL(b.href,location.href).pathname!==location.pathname||location.search||location.hash)location.href=b.href;},520);
});

// Asistente: cada chat se anima al verse en pantalla y vuelve a empezar cada vez que se vuelve a ver
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.querySelectorAll('.bchat').forEach(c=>{c.classList.add('anim');
 new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){c.classList.remove('go');void c.offsetWidth;c.classList.add('go');}}),{threshold:.45}).observe(c);});
// La IA también miente: «Ver la solución» funde la imagen en la solución y despliega la leyenda (y vuelve)
document.querySelectorAll('.flip').forEach(f=>{const b=f.querySelector('.flip-b'),l=f.querySelector('.flip-ley');
 b.addEventListener('click',()=>{const on=f.classList.toggle('on');b.setAttribute('aria-pressed',on);b.textContent=on?'Volver a la imagen':'Ver la solución';l.setAttribute('aria-hidden',!on);});});
