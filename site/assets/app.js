
(function(){
  var root=document.documentElement;
  // sticky cover: keep anchors clear of it
  var cv=document.querySelector('body>.cover');
  function coverH(){root.style.setProperty('--cover-h',(cv?cv.offsetHeight:0)+'px')}
  coverH();addEventListener('resize',coverH);
  if(location.hash){var tg=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(tg)setTimeout(function(){tg.scrollIntoView({behavior:'instant'})},0)}
  // enable transitions only after the first frames, so restored state does not animate
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.remove('preload')})});
  // smooth scrolling only after the page has settled, so a link to #id lands instantly
  addEventListener('load',function(){setTimeout(function(){root.classList.add('smooth')},100)});
  // in-page links: smooth scroll (CSS) and move focus to the target
  function focusTarget(){var el=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;if(!el.matches('a[href],button,input,select,textarea,[tabindex]'))el.setAttribute('tabindex','-1');el.focus({preventScroll:true})}
  addEventListener('hashchange',focusTarget);
  // theme
  var tb=document.querySelector('.theme-btn');
  if(tb)tb.addEventListener('click',function(){
    var dark=root.dataset.theme?root.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme=dark?'light':'dark';
    tb.classList.remove('turn');void tb.offsetWidth;tb.classList.add('turn');
    try{localStorage.setItem('bb-theme',root.dataset.theme)}catch(e){}
  });
  // mobile nav
  var mb=document.querySelector('.menu-btn'),scrim=document.querySelector('.scrim'),side=document.getElementById('sidebar');
  var mobile=matchMedia('(max-width: 860px)');
  // opening moves focus into the menu; closing returns it to the button (unless keep)
  function setNav(open,keep){var was=document.body.classList.contains('nav-open');document.body.classList.toggle('nav-open',open);scrim.hidden=!open;sync();
    if(open){var f=side.querySelector('a[href],button,summary');if(f)f.focus({preventScroll:true})}else if(was&&!keep)mb.focus({preventScroll:true})}
  function sync(){var open=mobile.matches?document.body.classList.contains('nav-open'):!root.classList.contains('side-hidden');
    var t=mobile.matches?(open?'Close navigation':'Open navigation'):(open?'Hide navigation':'Show navigation');
    mb.setAttribute('aria-expanded',open);mb.setAttribute('aria-label',t);mb.title=t}
  function setSide(hidden){root.classList.toggle('side-hidden',hidden);sync();try{localStorage.setItem('bb-side',hidden?'hidden':'shown')}catch(e){}}
  if(mb){mb.addEventListener('click',function(){if(mobile.matches)setNav(!document.body.classList.contains('nav-open'));else setSide(!root.classList.contains('side-hidden'))});
    scrim.addEventListener('click',function(){setNav(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!e.defaultPrevented&&mobile.matches&&document.body.classList.contains('nav-open'))setNav(false)});
    mobile.addEventListener('change',function(){if(!mobile.matches)setNav(false,true);else sync()});sync();}
  // chapter menu: independent sections, remembered across pages, collapse/expand all
  // (open/closed state and scroll position are restored inline, before first paint)
  var chs=[].slice.call(document.querySelectorAll('.nav-ch')),tg=document.querySelector('.nav-toggle'),st={};
  try{st=JSON.parse(localStorage.getItem('bb-nav')||'{}')}catch(e){}
  function label(){if(tg)tg.dataset.state=chs.some(function(d){return d.open})?'collapse':'expand'}
  // a row that links to another chapter: that chapter will be open on arrival
  chs.forEach(function(d){var a=d.querySelector('summary a');if(a)a.addEventListener('click',function(){st[d.dataset.ch]=true;try{localStorage.setItem('bb-nav',JSON.stringify(st))}catch(e){}})});
  function save(){chs.forEach(function(d){st[d.dataset.ch]=d.open});try{localStorage.setItem('bb-nav',JSON.stringify(st))}catch(e){}label()}
  chs.forEach(function(d){d.addEventListener('toggle',save)});
  if(tg)tg.addEventListener('click',function(){var any=chs.some(function(d){return d.open});chs.forEach(function(d){d.open=!any});save()});
  label();
  // sidebar scrollbar only while scrolling
  var sb=document.querySelector('.sidebar'),sbt;
  if(sb)sb.addEventListener('scroll',function(){sb.classList.add('is-scrolling');clearTimeout(sbt);sbt=setTimeout(function(){sb.classList.remove('is-scrolling')},900)},{passive:true});
  // remember the menu's scroll position for the next page
  if(sb)addEventListener('pagehide',function(){try{sessionStorage.setItem('bb-nav-y',sb.scrollTop)}catch(e){}});
  // toc highlight
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  if(links.length&&'IntersectionObserver' in window){
    var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
    var obs=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.remove('is-active')});var a=map[e.target.id];if(a)a.classList.add('is-active');}})},{rootMargin:'-'+(70+(cv?cv.offsetHeight:0))+'px 0px -60% 0px'});
    Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)obs.observe(el)});
  }
  // directives heading: shadow only while stuck under the banner
  var dh=document.getElementById('directives');
  if(dh){var mk=document.querySelector('.dh-mark'),raf=0;
    var stick=function(){raf=0;var t=parseFloat(getComputedStyle(dh).top)||0,m=parseFloat(getComputedStyle(dh).marginTop)||0;
      var natural=mk.getBoundingClientRect().top+m,top=dh.getBoundingClientRect().top;
      dh.classList.toggle('is-stuck',natural<t-0.5&&top>t-0.5)};
    var req=function(){if(!raf)raf=requestAnimationFrame(stick)};
    addEventListener('scroll',req,{passive:true});addEventListener('scrollend',stick);addEventListener('resize',req);stick();}
  // search
  var q=document.getElementById('q'),res=document.getElementById('results'),idx=window.BB_INDEX||[],sel=-1,items=[];
  if(!q)return;
  function norm(s){return s.toLowerCase().replace(/[’']/g,'')}
  // result count for screen readers, announced once typing pauses
  var status=document.getElementById('q-status'),sayT;
  function say(t){clearTimeout(sayT);sayT=setTimeout(function(){if(status)status.textContent=t},400)}
  function close(){res.hidden=true;sel=-1;q.setAttribute('aria-expanded','false');q.removeAttribute('aria-activedescendant')}
  idx.forEach(function(x){x._h=norm(x.id+' '+x.title+' '+x.body+' '+(x.sub||''))});
  function hl(s,terms){var o=s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]});terms.forEach(function(t){if(t.length<2)return;o=o.replace(new RegExp('('+t.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});return o}
  function run(){
    var v=norm(q.value.trim());res.innerHTML='';sel=-1;
    if(!v){res.hidden=true;q.setAttribute('aria-expanded','false');say('');return}
    var terms=v.split(/\s+/),scored=[];
    idx.forEach(function(x){
      if(!terms.every(function(t){return x._h.indexOf(t)>-1}))return;
      var s=0,tl=norm(x.title),id=x.id;
      terms.forEach(function(t){if(id.indexOf(t)===0)s+=50;if(tl.indexOf(t)>-1)s+=10;});
      if(x.t==='s')s+=5;if(x.title==='Repealed')s-=20;
      scored.push([s,x]);
    });
    scored.sort(function(a,b){return b[0]-a[0]});
    items=scored.slice(0,30).map(function(p){return p[1]});
    var n=scored.length;say(!n?'No results':n>30?'Showing 30 of '+n+' results':n===1?'1 result':n+' results');
    if(!items.length){res.innerHTML='<li class="r-empty">No directives match “'+hl(q.value,[])+'”.</li>'}
    items.forEach(function(x,i){
      var li=document.createElement('li');li.setAttribute('role','option');li.id='r'+i;li.className='rc'+x.c;
      li.innerHTML='<a href="'+x.url+'"><span class="r-id">'+hl(x.id,terms)+'</span><span class="r-t">'+hl(x.title,terms)+'</span><span class="r-b">'+hl(x.body,terms)+(x.sub?' · '+hl(x.sub,terms):'')+'</span></a>';
      res.appendChild(li);
    });
    res.hidden=false;q.setAttribute('aria-expanded','true');
  }
  var rst;res.addEventListener('scroll',function(){res.classList.add('is-scrolling');clearTimeout(rst);rst=setTimeout(function(){res.classList.remove('is-scrolling')},900)},{passive:true});
  // ---- history: results opened from search, newest first (max 8)
  var HK='bb-search-hist';
  function hist(){try{return JSON.parse(localStorage.getItem(HK)||'[]')}catch(e){return[]}}
  function saveHist(h){try{localStorage.setItem(HK,JSON.stringify(h))}catch(e){}}
  function remember(x){var h=hist().filter(function(e){return e.url!==x.url});h.unshift({id:x.id,title:x.title,c:x.c,url:x.url,q:q.value.trim()});saveHist(h.slice(0,8))}
  function showHist(){
    var h=hist();res.innerHTML='';sel=-1;items=[];say('');
    if(!h.length){res.hidden=true;q.setAttribute('aria-expanded','false');return}
    var head=document.createElement('li');head.className='r-head';head.textContent='Recent';res.appendChild(head);
    h.forEach(function(x,i){
      var li=document.createElement('li');li.setAttribute('role','option');li.id='r'+i;li.className='r-hist rc'+x.c;
      li.innerHTML='<a href="'+x.url+'"><span class="r-id">'+x.id+'</span><span class="r-t">'+hl(x.title,[])+'</span>'+(x.q?'<span class="r-q">'+hl(x.q,[])+'</span>':'')+'</a>'
        +'<button type="button" class="r-x" aria-label="Remove from history" title="Remove">×</button>';
      li.querySelector('.r-x').addEventListener('click',function(e){e.preventDefault();e.stopPropagation();saveHist(hist().filter(function(e2){return e2.url!==x.url}));showHist();q.focus({preventScroll:true})});
      res.appendChild(li);items.push(x);
    });
    var foot=document.createElement('li');foot.className='r-foot';
    foot.innerHTML='<button type="button" class="r-clear">Clear history</button>';
    foot.querySelector('button').addEventListener('click',function(e){e.stopPropagation();saveHist([]);showHist();q.focus({preventScroll:true})});
    res.appendChild(foot);res.hidden=false;q.setAttribute('aria-expanded','true');
  }
  function refresh(){q.parentNode.classList.toggle('has-val',!!q.value);if(q.value.trim())run();else showHist()}
  // remember what was opened from the list
  res.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var li=a.closest('li');var i=[].indexOf.call(res.querySelectorAll('li[role=option]'),li);if(i>-1&&items[i]&&!li.classList.contains('r-hist'))remember(items[i])});
  function move(d){var lis=res.querySelectorAll('li[role=option]');if(!lis.length)return;sel=(sel+d+lis.length)%lis.length;lis.forEach(function(l,i){l.setAttribute('aria-selected',i===sel)});lis[sel].scrollIntoView({block:'nearest'});q.setAttribute('aria-activedescendant','r'+sel)}
  q.addEventListener('input',refresh);
  q.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();if(res.hidden)refresh();else move(1)}
    else if(e.key==='ArrowUp'){e.preventDefault();if(res.hidden)refresh();else move(-1)}
    else if(e.key==='Enter'){if(res.hidden)return;var lis=res.querySelectorAll('li[role=option]');var li=lis[sel]||lis[0];if(li){var a=li.querySelector('a');if(!li.classList.contains('r-hist')&&items[sel<0?0:sel])remember(items[sel<0?0:sel]);location.href=a.href}}
    // Escape: first closes the list and keeps the text, second clears the text, third leaves the field
    else if(e.key==='Escape'){
      if(!res.hidden){e.preventDefault();close()}
      else if(q.value){e.preventDefault();q.value='';q.parentNode.classList.remove('has-val');say('')}
      else q.blur()}
  });
  // "/" focuses search; typing a letter or digit anywhere outside a field goes into search
  document.addEventListener('keydown',function(e){
    var el=document.activeElement,inField=el&&(/input|textarea|select/i.test(el.tagName)||el.isContentEditable);
    if(inField||e.ctrlKey||e.metaKey||e.altKey)return;
    if(e.key==='/'){e.preventDefault();q.focus({preventScroll:true});return}
    if(e.key.length===1&&/[\p{L}\p{N}]/u.test(e.key)){e.preventDefault();q.focus({preventScroll:true});q.value+=e.key;refresh()}
  });
  document.addEventListener('click',function(e){if(!e.target.closest('.search')){res.hidden=true;q.setAttribute('aria-expanded','false')}});
  var ic=document.querySelector('.search-ic');
  q.addEventListener('focus',function(){if(ic){ic.classList.remove('pop');void ic.offsetWidth;ic.classList.add('pop')}refresh()});
  if(ic)ic.addEventListener('animationend',function(){ic.classList.remove('pop')});
  q.parentNode.classList.toggle('has-val',!!q.value);
})();
