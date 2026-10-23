/* Progreso del curso: el script de la maqueta 1-home.html tal cual. En las páginas interiores no hay
   secciones [data-lesson]: los segmentos quedan como los deja el HTML y solo avanza la barra fina. */
(function(){
  var segs=document.querySelectorAll('#prog .seg'),lbl=document.getElementById('proglbl');
  var secs=Array.prototype.slice.call(document.querySelectorAll('[data-lesson]'));
  var bar=document.querySelector('.barra > div');
  function update(){
    var max=document.documentElement.scrollHeight-window.innerHeight;
    if(secs.length){
      var y=window.scrollY+window.innerHeight*0.45, cur=1;
      secs.forEach(function(s){ if(y>=s.offsetTop) cur=parseInt(s.getAttribute('data-lesson'),10); });
      if(max>0 && window.scrollY>=max-4) cur=5;
      segs.forEach(function(el,i){ el.style.background = i<cur-1 ? '#5E7D3A' : (i===cur-1 ? (cur===5 && window.scrollY>=max-4 ? '#5E7D3A' : '#A3322A') : '#E1E6F0'); });
      var pct=Math.round(cur/5*100);
      var done=(cur===5 && window.scrollY>=max-4); lbl.textContent= done ? 'Curso completado · 100 %' : 'Lección '+cur+' de 5 · '+pct+' %'; lbl.style.color= done ? '#5E7D3A' : '';
    }
    if(bar){ var p=max>0?Math.min(100,Math.round(window.scrollY/max*100)):100; /* sin scroll ya se ve todo (Contacto) */ bar.style.width=p+'%'; }
  }
  window.addEventListener('scroll',update,{passive:true}); window.addEventListener('resize',update); update();

  // Menú plegado en móvil
  var mb=document.querySelector('.menu-b'), cab=document.querySelector('header.cab');
  if(mb) mb.addEventListener('click',function(){ var a=cab.classList.toggle('abierto'); mb.setAttribute('aria-expanded',a); });

  // Actividad ramificada: mostrar u ocultar el feedback de la opción elegida
  document.querySelectorAll('.rama').forEach(function(r){
    var ops=r.querySelectorAll('button.opt'), fbs=r.querySelectorAll('.fb');
    ops.forEach(function(o){ o.addEventListener('click',function(){
      ops.forEach(function(x){ x.setAttribute('aria-pressed', x===o); });
      fbs.forEach(function(f){ f.hidden = f.getAttribute('data-op')!==o.getAttribute('data-op'); });
    }); });
  });

  // Filtros de /proyectos/: ocultan fichas y filas de las demás categorías (sin JavaScript se ve todo)
  var fs=document.querySelectorAll('button.filter');
  fs.forEach(function(f){ f.addEventListener('click',function(){
    var c=f.getAttribute('data-cat');
    fs.forEach(function(x){ x.classList.toggle('on',x===f); x.setAttribute('aria-pressed',x===f); });
    document.querySelectorAll('main [data-cat]:not(button)').forEach(function(el){ el.hidden = c!=='todos' && el.getAttribute('data-cat')!==c; });
  }); });
})();
