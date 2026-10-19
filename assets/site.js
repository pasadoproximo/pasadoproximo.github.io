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
// categorías del índice de proyectos: cada botón despliega sus proyectos debajo; solo una abierta a la vez
const cg=[...document.querySelectorAll('.cg')];
if(cg.length){
 const set=(b,o)=>{b.setAttribute('aria-expanded',o);const p=document.getElementById(b.getAttribute('aria-controls'));p.hidden=!o;if(o)p.querySelectorAll('.rv').forEach(r=>r.classList.add('in'));};
 const open=(b,o)=>{const y=b.getBoundingClientRect().top;if(o)cg.forEach(x=>{if(x!==b)set(x,false)});set(b,o);
  const dy=b.getBoundingClientRect().top-y;if(Math.abs(dy)>1)scrollBy({top:dy,behavior:'instant'});};
 cg.forEach(b=>b.addEventListener('click',()=>open(b,b.getAttribute('aria-expanded')!=='true')));
 // si se llega con #categoría, se abre esa
 const h=location.hash.slice(1),pre=cg.find(b=>b.id==='cg-'+h);if(pre)set(pre,true),cg.forEach(x=>{if(x!==pre)set(x,false)});}
})();
