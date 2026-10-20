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
// categorías del índice de proyectos: tres pestañas; la elegida queda marcada y se ven sus proyectos (flechas para moverse)
const ct=[...document.querySelectorAll('.ct')];
if(ct.length){
 const sel=(b,focus)=>{ct.forEach(x=>{const on=x===b;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;const p=document.getElementById(x.getAttribute('aria-controls'));p.hidden=!on;if(on)p.querySelectorAll('.rv').forEach(r=>r.classList.add('in'));});if(focus)b.focus();};
 ct.forEach((b,i)=>{b.addEventListener('click',()=>sel(b));
  b.addEventListener('keydown',e=>{const k={ArrowRight:1,ArrowLeft:-1}[e.key];if(k){e.preventDefault();sel(ct[(i+k+ct.length)%ct.length],true);}});});
 // si se llega con #categoría (por ejemplo /proyectos/#aula), se elige esa
 const h=location.hash.slice(1),pre=ct.find(b=>b.id==='cg-'+h);if(pre)sel(pre);}
})();
