
(function(){
  var root=document.documentElement;
  // sticky cover: --cover-h comes from CSS alone, so it follows the width; land a #id clear of it
  var cv=document.querySelector('body>.cover');
  // narrow screens: the banner condenses to one line once the page has scrolled by the height it gives up
  // (the text has then passed under it, so nothing moves); it stays full while one of its arrows has focus
  if(cv){var narrow=matchMedia('(max-width: 860px)'),craf=0;
    var cmin=function(){craf=0;var cs=getComputedStyle(root),t=parseFloat(cs.getPropertyValue('--cover-full'))-parseFloat(cs.getPropertyValue('--cover-h'));
      cv.classList.toggle('is-min',narrow.matches&&t>0&&scrollY>t&&!cv.contains(document.activeElement))};
    var creq=function(){if(!craf)craf=requestAnimationFrame(cmin)};
    cmin();addEventListener('scroll',creq,{passive:true});narrow.addEventListener('change',cmin);cv.addEventListener('focusout',creq)}
  // enable transitions only after the first frames, so restored state does not animate
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.remove('preload')})});
  // smooth scrolling only after the page has settled, so a link to #id lands instantly
  addEventListener('load',function(){setTimeout(function(){root.classList.add('smooth')},100)});
  // in-page links: smooth scroll (CSS) and move focus to the target
  function focusTarget(el){if(!el||!el.nodeType)el=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;if(el.classList.contains('dh-mark'))el=el.nextElementSibling;if(!el.matches('a[href],button,input,select,textarea,[tabindex]'))el.setAttribute('tabindex','-1');el.focus({preventScroll:true})}
  addEventListener('hashchange',focusTarget);
  // theme
  var tb=document.querySelector('.theme-btn'),sysDark=matchMedia('(prefers-color-scheme: dark)');
  function isDark(){return root.dataset.theme?root.dataset.theme==='dark':sysDark.matches}
  // the button names the theme a click switches to
  function themeLabel(){var t=isDark()?'Switch to light theme':'Switch to dark theme';tb.setAttribute('aria-label',t)}
  if(tb){tb.addEventListener('click',function(){
    if(tb.matches(':hover'))tb.classList.add('pv-off');
    // a click that lands on the system theme forgets the stored choice, so the site follows the system again
    var next=isDark()?'light':'dark',sys=(next==='dark')===sysDark.matches;
    if(sys)delete root.dataset.theme;else root.dataset.theme=next;themeLabel();
    tb.classList.remove('turn');void tb.offsetWidth;tb.classList.add('turn');
    try{if(sys)localStorage.removeItem('bb-theme');else localStorage.setItem('bb-theme',next)}catch(e){}
  });
    // the hover preview comes back once the pointer has left; the icon morphs again once the turn is over
    tb.addEventListener('pointerleave',function(){tb.classList.remove('pv-off')});
    tb.addEventListener('animationend',function(e){if(e.animationName==='bb-turn')tb.classList.remove('turn')});
    sysDark.addEventListener('change',themeLabel);themeLabel()}
  // mobile nav
  var mb=document.querySelector('.menu-btn'),scrim=document.querySelector('.scrim'),side=document.getElementById('sidebar');
  var mobile=matchMedia('(max-width: 860px)');
  // opening moves focus into the menu; closing returns it to the button (unless keep)
  // while the mobile menu is open, everything but the top bar and the menu is inert (Tab cannot reach the page under the scrim)
  function setNav(open,keep){var was=document.body.classList.contains('nav-open');document.body.classList.toggle('nav-open',open);scrim.hidden=!open;sync();
    [].forEach.call(document.querySelectorAll('body>*,.shell>*'),function(n){if(!n.matches('.top,.shell,.sidebar,.scrim,.tip,script'))n.inert=open});
    if(open){var f=side.querySelector('a[href],button');if(f)f.focus({preventScroll:true});showCur()}else if(was&&!keep)mb.focus({preventScroll:true})}
  // an opened menu shows where the reader is: the current page's item is brought into view, by the shortest way and at once
  function showCur(){var c=side.querySelector('[aria-current]');if(c)c.scrollIntoView({block:'nearest',behavior:'instant'})}
  function sync(){var open=mobile.matches?document.body.classList.contains('nav-open'):!root.classList.contains('side-hidden');
    var t=mobile.matches?(open?'Close panel':'Open panel'):(open?'Hide panel':'Show panel');
    mb.setAttribute('aria-expanded',open);mb.setAttribute('aria-label',t)}
  function setSide(hidden){root.classList.toggle('side-hidden',hidden);sync();if(!hidden)showCur();try{localStorage.setItem('bb-side',hidden?'hidden':'shown')}catch(e){}}
  if(mb){mb.addEventListener('click',function(){if(mb.matches(':hover'))mb.classList.add('pv-off');if(mobile.matches)setNav(!document.body.classList.contains('nav-open'));else setSide(!root.classList.contains('side-hidden'))});
    scrim.addEventListener('click',function(){setNav(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!e.defaultPrevented&&mobile.matches&&document.body.classList.contains('nav-open'))setNav(false)});
    mobile.addEventListener('change',function(){if(!mobile.matches)setNav(false,true);else sync()});sync();
    // the icon's hover preview is off from a click until the pointer leaves
    mb.addEventListener('pointerleave',function(){mb.classList.remove('pv-off')});}
  // tooltips: one styled label under an icon-only control; its text is the control's aria-label (the home link's: its emblem's hidden text, while the emblem shows).
  // Hover shows it after TIP_DELAY, at once if another tooltip was showing within TIP_CHAIN; keyboard focus shows it at once; touch: a long press (below).
  // A click and Escape hide it, and it does not return while the pointer stays on the same control.
  var TIP_SEL='.menu-btn,.theme-btn,.brand,.search-x,.r-x,.cv-arr,a.cn,.chev',TIP_DELAY=400,TIP_CHAIN=300;
  var tip=document.createElement('div'),tipOwn=null,tipOver=null,tipT=0,tipGone=0,tipMute=false,canHover=matchMedia('(hover:hover)');
  tip.className='tip';tip.setAttribute('aria-hidden','true');document.body.appendChild(tip);
  function tipCtl(n){var el=n&&n.closest?n.closest(TIP_SEL):null;return el&&tipText(el)?el:null}
  // under the control and centred on it, 8px clear of the viewport's edges; above it when there is no room below.
  // A chapter chevron has the next chevron right under it: its tooltip stands beside it, on the right, or on the left when the right has no room;
  // it stays level with its row up to the viewport's very edge (an 8px margin there would push it onto the row above)
  function tipPlace(){if(!tipOwn)return;var r=tipOwn.getBoundingClientRect();if(!r.width&&!r.height){tipHide();return}
    var w=tip.offsetWidth,h=tip.offsetHeight,vw=root.clientWidth,cx=r.left+r.width/2,side=tipOwn.matches('.chev'),x,y,up=false,sl=false;
    if(side){sl=r.right+6+w>vw-8;x=Math.round(sl?r.left-6-w:r.right+6);y=Math.round(Math.max(0,Math.min(r.top+r.height/2-h/2,innerHeight-h)))}
    else{x=Math.round(Math.max(8,Math.min(cx-w/2,vw-w-8)));up=r.bottom+6+h>innerHeight-8&&r.top-6-h>=8;y=Math.round(up?r.top-6-h:r.bottom+6)}
    tip.classList.toggle('up',up);tip.classList.toggle('at-r',side&&!sl);tip.classList.toggle('at-l',sl);tip.style.left=x+'px';tip.style.top=y+'px';
    tip.style.transformOrigin=side?(sl?'100% 50%':'0 50%'):(cx-x)+'px '+(up?'100%':'0')}
  // the one exception: a chapter chevron keeps its label and its tooltip names what a click does to the list (the words of "Collapse all" / "Expand all")
  function tipText(el){if(el.matches('.brand')){var m=el.querySelector('.brand-m');return m&&m.offsetWidth?m.textContent:''}
    return el.matches('.chev')?(el.getAttribute('aria-expanded')==='true'?'Collapse':'Expand'):el.getAttribute('aria-label')}
  function tipShow(el){clearTimeout(tipT);var t=tipText(el);if(!t)return;tipOwn=el;tip.textContent=t;tipPlace();if(tipOwn)tip.classList.add('on')}
  function tipHide(){clearTimeout(tipT);if(tipOwn){tipOwn=null;tipGone=Date.now();tip.classList.remove('on')}}
  // a click or Escape may move the focus by script (the menu closing): that focus shows no tooltip
  function tipDismiss(){tipHide();tipMute=true;setTimeout(function(){tipMute=false},0)}
  document.addEventListener('pointerover',function(e){
    if(e.pointerType==='touch'||!canHover.matches||tip.contains(e.target))return;
    var el=tipCtl(e.target);if(el===tipOver)return;tipOver=el;clearTimeout(tipT);
    if(!el){if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();return}
    if(tipOwn||Date.now()-tipGone<TIP_CHAIN)tipShow(el);else tipT=setTimeout(function(){tipShow(el)},TIP_DELAY)});
  root.addEventListener('pointerleave',function(e){if(e.pointerType==='touch')return;tipOver=null;if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();else clearTimeout(tipT)});
  document.addEventListener('focusin',function(e){var el=tipCtl(e.target);if(el&&!tipMute&&el.matches(':focus-visible'))tipShow(el)});
  document.addEventListener('focusout',function(e){if(tipOwn&&tipCtl(e.target)===tipOwn&&tipOver!==tipOwn)tipHide()});
  document.addEventListener('click',function(e){
    // the click of a release that ended a long press: it does nothing and the tooltip stays
    if(holdEat&&Date.now()-holdEat<HOLD_EAT){holdEat=0;e.preventDefault();e.stopImmediatePropagation();return}
    tipDismiss()},true);
  document.addEventListener('keydown',function(e){if(e.key==='Escape')tipDismiss()},true);
  addEventListener('scroll',tipPlace,{passive:true,capture:true});addEventListener('resize',tipHide);document.addEventListener('input',tipPlace);
  // touch: a press of HOLD on one of these controls shows its tooltip, and the release then does nothing; a release before that, a move over HOLD_MOVE
  // or a cancelled touch leaves a tap what it was. The tooltip hides HOLD_OUT after the release or at the next touch.
  // The browser's own long-press menu is off on these controls while a finger is on one (a mouse's right click keeps it)
  var HOLD=500,HOLD_MOVE=10,HOLD_OUT=1500,HOLD_EAT=800,holdT=0,holdEl=null,holdX=0,holdY=0,holdOn=false,holdEat=0,holdOutT=0;
  function holdStop(){clearTimeout(holdT);holdT=0;holdEl=null}
  function holdEnd(e){var shown=holdOn&&!!holdEl;holdStop();if(!shown)return;
    if(e.type==='touchend'){holdEat=Date.now();if(e.cancelable)e.preventDefault()}
    holdOutT=setTimeout(function(){holdOn=false;tipHide()},HOLD_OUT)}
  document.addEventListener('touchstart',function(e){
    clearTimeout(holdOutT);holdStop();if(holdOn){holdOn=false;tipHide()}
    var el=e.touches.length===1?tipCtl(e.target):null;if(!el)return;
    holdEl=el;holdX=e.touches[0].clientX;holdY=e.touches[0].clientY;
    holdT=setTimeout(function(){holdT=0;holdOn=true;tipShow(el)},HOLD)},{passive:true,capture:true});
  document.addEventListener('touchmove',function(e){
    if(holdT&&Math.hypot(e.touches[0].clientX-holdX,e.touches[0].clientY-holdY)>HOLD_MOVE)holdStop()},{passive:true,capture:true});
  document.addEventListener('touchend',holdEnd,{passive:false,capture:true});
  document.addEventListener('touchcancel',holdEnd,{passive:true,capture:true});
  document.addEventListener('contextmenu',function(e){if(holdEl&&tipCtl(e.target))e.preventDefault()},true);
  // chapter menu: independent sections, remembered across pages, collapse/expand all
  // (open/closed state and scroll position are restored inline, before first paint)
  var chs=[].slice.call(document.querySelectorAll('.nav-ch')),tg=document.querySelector('.nav-toggle'),st={};
  try{st=JSON.parse(localStorage.getItem('bb-nav')||'{}')}catch(e){}
  function navOpen(d){return d.querySelector('.chev').getAttribute('aria-expanded')==='true'}
  function navSet(d,v){d.querySelector('.chev').setAttribute('aria-expanded',v);var p=d.querySelector('.nav-ch-c');if(v)p.removeAttribute('hidden');else p.setAttribute('hidden','until-found')}
  function label(){if(tg)tg.dataset.state=chs.some(navOpen)?'collapse':'expand'}
  // a row that links to another chapter: that chapter will be open on arrival
  chs.forEach(function(d){var a=d.querySelector('.nav-ch-h a');if(a)a.addEventListener('click',function(){st[d.dataset.ch]=true;try{localStorage.setItem('bb-nav',JSON.stringify(st))}catch(e){}})});
  function save(){chs.forEach(function(d){st[d.dataset.ch]=navOpen(d)});try{localStorage.setItem('bb-nav',JSON.stringify(st))}catch(e){}label()}
  // a click anywhere on the row but its link toggles the list (the button's Enter and Space arrive as clicks); find-in-page opens a closed list it lands in
  chs.forEach(function(d){d.querySelector('.nav-ch-h').addEventListener('click',function(e){if(e.target.closest('a'))return;navSet(d,!navOpen(d));save()});
    d.querySelector('.nav-ch-c').addEventListener('beforematch',function(){navSet(d,true);save()})});
  if(tg)tg.addEventListener('click',function(){var any=chs.some(navOpen);chs.forEach(function(d){navSet(d,!any)});save()});
  label();
  // sidebar scrollbar only while scrolling
  var sb=document.querySelector('.sidebar'),sbt;
  if(sb)sb.addEventListener('scroll',function(){sb.classList.add('is-scrolling');clearTimeout(sbt);sbt=setTimeout(function(){sb.classList.remove('is-scrolling')},900)},{passive:true});
  // remember the menu's scroll position for the next page
  if(sb)addEventListener('pagehide',function(){try{sessionStorage.setItem('bb-nav-y',sb.scrollTop)}catch(e){}});
  // toc highlight: the last heading at or above the line anchors land on (scroll-margin-top, +1px for fractions)
  // the same sections are listed twice: in "On this page" and, where that is hidden, under the menu's current item (.nav-sec)
  var links=[].slice.call(document.querySelectorAll('.toc a,.nav-sec a'));
  if(links.length){
    var heads=[],picked=null,traf=0,tmk=document.querySelector('.dh-mark');
    var treq=function(){if(!traf)traf=requestAnimationFrame(mark)};
    links.forEach(function(a){var el=document.getElementById(a.getAttribute('href').slice(1));if(!el)return;
      heads.push({a:a,el:el});if(location.hash==='#'+el.id)picked=el;
      a.addEventListener('click',function(e){picked=el;treq();
        // phones: a tap in the open menu closes it, which unlocks the page, and focus goes to the section
        if(!(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)&&mobile.matches&&document.body.classList.contains('nav-open')&&a.closest('.nav-sec')){setNav(false,true);focusTarget(el)}})});
    // the directives heading is sticky: the mark before it keeps its natural place
    var topOf=function(el){return (el.id==='directives'&&tmk?tmk:el).getBoundingClientRect().top};
    var mark=function(){traf=0;if(!heads.length)return;
      var L=(parseFloat(getComputedStyle(heads[0].el).scrollMarginTop)||0)+1,cur=null;
      heads.forEach(function(h){if(topOf(h.el)<=L)cur=h.el});
      // at the end of the page the last headings cannot reach the line: the clicked one if it is on screen, else the last
      if(scrollY>0&&scrollY+innerHeight>=root.scrollHeight-1){var p=null;
        heads.forEach(function(h){if(h.el===picked){var r=h.el.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)p=h.el}});
        cur=p||heads[heads.length-1].el}
      heads.forEach(function(h){h.a.classList.toggle('is-active',h.el===cur)})};
    // a click is "just clicked" only until the reader scrolls by hand
    ['wheel','touchstart','keydown','mousedown'].forEach(function(t){addEventListener(t,function(){picked=null},{passive:true})});
    addEventListener('scroll',treq,{passive:true});addEventListener('resize',treq);addEventListener('load',treq);mark();
  }
  // landing cue: a click in "On this page" or in the menu's list of sections marks the heading it lands on once the scroll stops (style.css, .cue)
  var toc=document.querySelector('.toc');
  if(toc){var cueEl=null,cueY=0,cueT=0,acc=getComputedStyle(toc).getPropertyValue('--ch-accent').trim();
    // ring colour per theme: the chapter accent, darkened where the build found it below 3:1 on the page background
    var mix={"#ee82ee":[10,0],"#3ee439":[20,0],"#00ffff":[28,0],"#ffa528":[15,0],"#fff500":[30,0],"#ffd596":[25,0],"#ffa500":[15,0],"#1ef58d":[24,0],"#28fff1":[28,0]}[acc];
    if(mix)['--cue-l','--cue-d'].forEach(function(k,i){if(mix[i]!==null)root.style.setProperty(k,mix[i]?'color-mix(in oklab,'+acc+',#000 '+mix[i]+'%)':acc)});
    var cueNow=function(){clearTimeout(cueT);removeEventListener('scroll',cueWait);removeEventListener('scrollend',cueEnd);
      var el=cueEl;cueEl=null;if(!el)return;el.classList.remove('cue');
      // the twitch grows from the centre of the text, not of the column-wide box; the ring wraps the same text box
      var rg=document.createRange();rg.selectNodeContents(el);var tr=rg.getBoundingClientRect(),er=el.getBoundingClientRect();
      el.style.setProperty('--cue-x',(tr.left+tr.width/2-er.left)+'px');
      [['bx',tr.left-er.left],['by',tr.top-er.top],['bw',tr.width],['bh',tr.height]].forEach(function(v){el.style.setProperty('--cue-'+v[0],v[1]+'px')});
      void el.offsetWidth;el.classList.add('cue')};
    // scrollend where the browser has it (only at the jump's own stop, not an earlier scroll's); elsewhere 100ms without a scroll event
    var cueEnd=function(){if(Math.abs(scrollY-cueY)<2)cueNow()};
    var cueWait=function(){clearTimeout(cueT);cueT=setTimeout(cueNow,100)};
    links.forEach(function(a){var el=document.getElementById(a.getAttribute('href').slice(1));if(!el)return;
      // #directives is the mark before the sticky heading: the jump is measured on the mark, the cue plays on the heading
      var hd=el.classList.contains('dh-mark')?el.nextElementSibling:el;
      if(!a.closest('.nav-sec'))hd.addEventListener('animationend',function(e){if(e.target===hd&&/^bb-cue-/.test(e.animationName))hd.classList.remove('cue')});
      a.addEventListener('click',function(e){if(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
        // where the jump will stop: the heading's line (the sticky heading's mark), kept within the page
        var d=topOf(el)-(parseFloat(getComputedStyle(el).scrollMarginTop)||0);
        cueY=Math.max(0,Math.min(scrollY+d,root.scrollHeight-innerHeight));
        cueEl=hd;if(Math.abs(cueY-scrollY)<1){cueNow();return}
        addEventListener('scroll',cueWait,{passive:true});addEventListener('scrollend',cueEnd);
        // the jump can start a few frames late: give it 400ms before taking "no scroll" for an answer
        clearTimeout(cueT);cueT=setTimeout(cueNow,400)})});
  }
  // directives heading: shadow only while stuck under the banner
  var dh=document.querySelector('h2.dh');
  if(dh){var mk=document.querySelector('.dh-mark'),raf=0;
    var stick=function(){raf=0;var t=parseFloat(getComputedStyle(dh).top)||0;
      var natural=mk.getBoundingClientRect().top,top=dh.getBoundingClientRect().top;
      dh.classList.toggle('is-stuck',natural<t-0.5&&top>t-0.5)};
    var req=function(){if(!raf)raf=requestAnimationFrame(stick)};
    var headH=function(){root.style.setProperty('--dh-h',dh.offsetHeight+'px')};
    headH();addEventListener('resize',headH);
    addEventListener('scroll',req,{passive:true});addEventListener('scrollend',stick);addEventListener('resize',req);stick();
    // links to the heading: a native jump lands by its stuck place, so go to the mark's line and set hash and focus by hand
    // (location.hash, not pushState: it moves :target too; the scroll it starts is replaced by the one below)
    [].forEach.call(document.querySelectorAll('a[href="#directives"]'),function(a){a.addEventListener('click',function(e){
      if(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;e.preventDefault();
      var y=scrollY+mk.getBoundingClientRect().top-(parseFloat(getComputedStyle(mk).scrollMarginTop)||0);
      if(location.hash!=='#directives')location.hash='directives';
      focusTarget();scrollTo(0,Math.max(0,Math.min(y,root.scrollHeight-innerHeight)))})});}
  // search
  var q=document.getElementById('q'),res=document.getElementById('results'),idx=window.BB_INDEX||[],chTitles=window.BB_CHAPTERS||{},vocab=window.BB_VOCAB||{},words={},sel=-1,items=[],off=0;
  if(!q)return;
  function norm(s){return s.toLowerCase().replace(/[’']/g,'')}
  // result count for screen readers, announced once typing pauses
  var status=document.getElementById('q-status'),sayT;
  function say(t){clearTimeout(sayT);sayT=setTimeout(function(){if(status)status.textContent=t},400)}
  // a closed list keeps no selection: the next opening renders it anew
  function close(){res.hidden=true;sel=-1;q.setAttribute('aria-expanded','false');q.removeAttribute('aria-activedescendant');
    [].forEach.call(res.querySelectorAll('[aria-selected]'),function(l){l.removeAttribute('aria-selected')})}
  // the chapter title (BB_CHAPTERS, by chapter number x.c) is searched but never shown
  idx.forEach(function(x){x._h=norm(x.id+' '+x.title+' '+x.body+' '+(x.sub||'')+' '+(chTitles[x.c]||''))});
  // the book's words with their frequencies, most frequent first: counted once from the text the matcher searches,
  // split where at() sees a word start; the search suggests the nearest one for a misspelled query word.
  // The vocabulary's word keys and the words of its phrase keys are candidates too, with frequency 0 unless the book has them
  (function(){var f={},k;
    idx.forEach(function(x){x._h.split(/[^a-z0-9]+/).forEach(function(w){if(w.length>1&&/^[a-z]+$/.test(w))f[w]=(f[w]||0)+1})});
    function add(w){if(/^[a-z]+$/.test(w)&&!f[w])f[w]=0}
    for(k in vocab.words||{})add(k);
    for(k in vocab.phrases||{})k.split(' ').forEach(add);
    Object.keys(f).sort(function(a,b){return f[b]-f[a]||(a<b?-1:1)}).forEach(function(w){words[w]=f[w]})})();
  function escH(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
  // a term matches only where a word starts: at the start of the text or after a non-alphanumeric character
  function at(h,t){var i=-1;while((i=h.indexOf(t,i+1))>-1){if(!i||!/[a-z0-9]/.test(h.charAt(i-1)))return true}return false}
  // marks what the matcher matched: the same word starts, longest term first
  function hl(s,terms){
    var ts=terms.filter(function(t){return t.length>1}).sort(function(a,b){return b.length-a.length}).map(function(t){return t.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&')});
    if(!ts.length)return escH(s);
    var re=new RegExp('(^|[^a-z0-9])('+ts.join('|')+')','ig'),o='',last=0,m;
    while((m=re.exec(s))){var st=m.index+m[1].length;o+=escH(s.slice(last,st))+'<mark>'+escH(m[2])+'</mark>';last=re.lastIndex=st+m[2].length}
    return o+escH(s.slice(last))}
  // query -> groups of alternatives (vocabulary: tools/search_vocab.json); an entry matches a group if any member matches
  function groups(v){
    var sp=vocab.spelling||{},ph=vocab.phrases||{},wd=vocab.words||{},out=[],k;
    for(k in sp)v=v.split(k).join(sp[k]);
    var w=v.split(/\s+/),max=1;
    for(k in ph)max=Math.max(max,k.split(' ').length);
    for(var i=0;i<w.length;){
      for(var n=Math.min(max,w.length-i),p=null;n>1&&!(p=ph[w.slice(i,i+n).join(' ')]);n--);
      if(p){out.push(p.slice());i+=n;continue}
      var t=w[i++],g=[t].concat(wd[t]||[]);
      // a plural also tries its singular and the singular's synonyms
      if(t.length>3&&t.charAt(t.length-1)==='s'){var b=t.slice(0,-1);g=g.concat([b],wd[b]||[])}
      out.push(g.filter(function(m,j){return g.indexOf(m)===j}));
    }
    return out}
  // ---- no results, or only any-word matches: suggest a correction (27/08)
  // true if the query finds anything, counting the any-word fallback
  function finds(v){var gs=groups(v);return idx.some(function(x){return gs.some(function(g){return g.some(function(t){return at(x._h,t)})})})}
  // true if some entry matches every word of the query
  function findsAll(v){var gs=groups(v);return idx.some(function(x){return gs.every(function(g){return g.some(function(t){return at(x._h,t)})})})}
  // Damerau-Levenshtein distance (adjacent transpositions count as one edit)
  function dist(a,b){
    var m=a.length,n=b.length,p2,p=[],c,i,j;
    for(j=0;j<=n;j++)p[j]=j;
    for(i=1;i<=m;i++){
      c=[i];
      for(j=1;j<=n;j++){
        c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a.charAt(i-1)===b.charAt(j-1)?0:1));
        if(i>1&&j>1&&a.charAt(i-1)===b.charAt(j-2)&&a.charAt(i-2)===b.charAt(j-1))c[j]=Math.min(c[j],p2[j-2]+1);
      }
      p2=p;p=c;
    }
    return p[n]}
  // the nearest candidate: 1 edit for words up to 5 letters, 2 for longer. At equal distance a candidate that starts with
  // the typed word wins; the list is most frequent first, so any other tie keeps the more frequent. skip: candidates left out
  function nearest(w,skip){
    var lim=w.length>5?2:1,best=null,bd=lim+1,bp=false,k,d,pre;
    for(k in words){
      if(skip&&skip[k]||Math.abs(k.length-w.length)>lim)continue;
      d=dist(w,k);pre=k.indexOf(w)===0;
      if(d<bd||d===bd&&pre&&!bp){bd=d;bp=pre;best=k}}
    return best}
  // candidates that find nothing alone (they only work inside a vocabulary phrase), found on first use
  var dead;
  function deadWords(){if(!dead){dead={};for(var k in words)if(!words[k]&&!finds(k))dead[k]=1}return dead}
  // the query with every word that alone finds nothing replaced by its nearest candidate; null unless that query finds results
  // (ok: the test it has to pass, finds by default). If it fails, the correction runs once more without the candidates that find nothing alone
  function correct(raw,ok){
    function attempt(skip){
      var changed=false,out=raw.trim().split(/\s+/).map(function(w){
        var n=norm(w),fix=/^[a-z]+$/.test(n)&&!finds(n)&&nearest(n,skip);
        if(fix)changed=true;return fix||w}).join(' ');
      return changed&&(ok||finds)(norm(out))?out:null}
    return attempt()||attempt(deadWords())}
  function fixLi(fix){return '<li role="option" id="r0" class="r-fix" data-q="'+escH(fix).replace(/"/g,'&quot;')+'"><a href="#">Did you mean <span class="r-t">'+escH(fix)+'</span>?</a></li>'}
  function applyFix(li){q.value=li.getAttribute('data-q');q.parentNode.classList.add('has-val');run();q.focus({preventScroll:true})}
  // all: the cap of 30 is lifted (only showAll passes it; every other call caps again)
  function run(all){
    var v=norm(q.value.trim());res.innerHTML='';sel=-1;off=0;q.removeAttribute('aria-activedescendant');
    if(!v){res.hidden=true;q.setAttribute('aria-expanded','false');say('');return}
    var gs=groups(v),terms=[].concat.apply([],gs),scored=[],some=[],any=false;
    idx.forEach(function(x){
      var s=0,hit=0,tl=norm(x.title),id=x.id;
      gs.forEach(function(g){
        if(!g.some(function(t){return at(x._h,t)}))return;
        hit++;if(g.some(function(t){return id.indexOf(t)===0}))s+=50;if(g.some(function(t){return at(tl,t)}))s+=10;
      });
      if(!hit)return;
      if(x.t==='s')s+=5;if(x.title==='Repealed')s-=20;
      (hit<gs.length?some:scored).push([s,x,hit]);
    });
    // nothing matches every group: fall back to entries matching any, most groups first, then the usual score
    if(!scored.length&&gs.length>1&&some.length){any=true;scored=some}
    scored.sort(function(a,b){return any&&b[2]-a[2]||b[0]-a[0]});
    var n=scored.length,cut=n>30&&all!==true;
    items=(cut?scored.slice(0,30):scored).map(function(p){return p[1]});
    var count=!n?'No results':cut?'Showing 30 of '+n+' results':n===1?'1 result':n+' results';
    if(any)count='No directive matches all words. Showing '+(cut?'30 of '+n+' that match':n===1?'the 1 that matches':n+' that match')+' any.';
    // any-word matches only: a typo in one word may hide an exact match. Suggest the correction if it matches every word
    var anyFix=any&&correct(q.value,findsAll);
    say(count+(anyFix?' Did you mean '+anyFix+'?':''));
    // nothing at all: say what happened, suggest a correction, offer a way out. The suggestion is an option
    // (arrows reach it, Enter or a click runs it); the two sentences are not. #q-status says the same text.
    if(!items.length){
      var fix=correct(q.value),l1='The book has no directive on “'+q.value.trim()+'”.',l3='Try a broader word, or browse the Contents.';
      say(l1+(fix?' Did you mean '+fix+'? ':' ')+l3);
      res.innerHTML='<li class="r-empty" role="presentation">'+escH(l1)+'</li>'
        +(fix?fixLi(fix):'')
        +'<li class="r-empty" role="presentation">Try a broader word, or browse the <a href="index.html">Contents</a>.</li>'}
    // the same count, visible: a heading row, not an option (arrows skip it; #q-status does the announcing);
    // the any-word notice is a sentence, so it takes the plain look of the no-match line (.r-empty)
    else{var head=document.createElement('li');head.className=any?'r-empty':'r-head';head.setAttribute('role','presentation');head.setAttribute('aria-hidden','true');head.textContent=count;res.appendChild(head);
      // the suggestion follows the any-word notice as the first option; the results are numbered after it
      if(anyFix){res.insertAdjacentHTML('beforeend',fixLi(anyFix));off=1}}
    items.forEach(function(x,i){
      var li=document.createElement('li');li.setAttribute('role','option');li.id='r'+(i+off);li.className='rc'+x.c;
      li.innerHTML='<a href="'+x.url+'"><span class="r-id">'+hl(x.id,terms)+'</span><span class="r-t">'+hl(x.title,terms)+'</span><span class="r-b">'+hl(x.body,terms)+(x.sub?' · '+hl(x.sub,terms):'')+'</span></a>';
      res.appendChild(li);
    });
    // over 30: the last option shows the rest (arrows reach it, Enter or a click runs it), the look of the suggestion row
    if(cut)res.insertAdjacentHTML('beforeend','<li role="option" id="r'+(30+off)+'" class="r-more"><a href="#"><span class="r-t">Show all '+n+' results</span></a></li>');
    res.hidden=false;q.setAttribute('aria-expanded','true');
    // a new list starts at its top; "Show all" continues the same list, so it keeps its place
    if(all!==true)res.scrollTop=0;
  }
  // the same query without the cap; the 31st result takes the selection (keys: the focus stays in the field) or the focus
  function showAll(keys){
    run(true);var i=30+off,li=res.querySelectorAll('li[role=option]')[i];if(!li)return;
    if(keys){sel=i;li.setAttribute('aria-selected','true');li.scrollIntoView({block:'nearest'});q.setAttribute('aria-activedescendant','r'+i)}
    else li.querySelector('a').focus()}
  var rst;res.addEventListener('scroll',function(){res.classList.add('is-scrolling');clearTimeout(rst);rst=setTimeout(function(){res.classList.remove('is-scrolling')},900)},{passive:true});
  // ---- history: results opened from search, newest first (max 8)
  var HK='bb-search-hist';
  function hist(){try{return JSON.parse(localStorage.getItem(HK)||'[]')}catch(e){return[]}}
  function saveHist(h){try{localStorage.setItem(HK,JSON.stringify(h))}catch(e){}}
  function remember(x){var h=hist().filter(function(e){return e.url!==x.url});h.unshift({id:x.id,title:x.title,c:x.c,url:x.url,q:q.value.trim()});saveHist(h.slice(0,8))}
  function showHist(){
    var h=hist();res.innerHTML='';sel=-1;off=0;items=[];q.removeAttribute('aria-activedescendant');say('');
    if(!h.length){res.hidden=true;q.setAttribute('aria-expanded','false');return}
    var head=document.createElement('li');head.className='r-head';head.textContent='Recent';res.appendChild(head);
    h.forEach(function(x,i){
      var li=document.createElement('li');li.setAttribute('role','option');li.id='r'+i;li.className='r-hist rc'+x.c;
      li.innerHTML='<a href="'+x.url+'"><span class="r-id">'+x.id+'</span><span class="r-t">'+hl(x.title,[])+'</span>'+(x.q?'<span class="r-q">'+hl(x.q,[])+'</span>':'')+'</a>'
        +'<button type="button" class="r-x" aria-label="Remove from history"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5.4 5.4l9.2 9.2M14.6 5.4l-9.2 9.2"/></svg></button>';
      // an entry removed from a scrolled list: the list stays where it was (the focus going to the field renders it once more).
      li.querySelector('.r-x').addEventListener('click',function(e){e.preventDefault();e.stopPropagation();saveHist(hist().filter(function(e2){return e2.url!==x.url}));var y=res.scrollTop;showHist();q.focus({preventScroll:true});res.scrollTop=y;
        // the click hid the tooltip; the next entry's button is now under the pointer: to the tooltip it is the control just clicked,
        // so the tooltip does not return while the pointer stays (a click from the keyboard has no pointer place)
        if(e.detail)tipOver=tipCtl(document.elementFromPoint(e.clientX,e.clientY))});
      res.appendChild(li);items.push(x);
    });
    var foot=document.createElement('li');foot.className='r-foot';
    foot.innerHTML='<button type="button" class="r-clear">Clear history</button>';
    foot.querySelector('button').addEventListener('click',function(e){e.stopPropagation();saveHist([]);showHist();q.focus({preventScroll:true})});
    res.appendChild(foot);res.hidden=false;q.setAttribute('aria-expanded','true');
    res.scrollTop=0;
  }
  function refresh(){q.parentNode.classList.toggle('has-val',!!q.value);if(q.value.trim())run();else showHist()}
  // remember what was opened from the list
  res.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var li=a.closest('li');if(li.classList.contains('r-fix')){e.preventDefault();e.stopPropagation();applyFix(li);return}if(li.classList.contains('r-more')){e.preventDefault();e.stopPropagation();showAll(false);return}var i=[].indexOf.call(res.querySelectorAll('li[role=option]'),li)-off;if(i>-1&&items[i]&&!li.classList.contains('r-hist'))remember(items[i])});
  function move(d){var lis=res.querySelectorAll('li[role=option]');if(!lis.length)return;sel=sel<0?(d<0?lis.length-1:0):(sel+d+lis.length)%lis.length;lis.forEach(function(l,i){l.setAttribute('aria-selected',i===sel)});lis[sel].scrollIntoView({block:'nearest'});q.setAttribute('aria-activedescendant','r'+sel)}
  q.addEventListener('input',refresh);
  // Tab or Shift+Tab that takes the focus out of the list closes it; the focus goes where the browser's own order puts it
  var tabOut=false;
  res.addEventListener('keydown',function(e){if(e.key==='Tab'){tabOut=true;setTimeout(function(){tabOut=false},0)}});
  res.addEventListener('focusout',function(e){if(tabOut&&!res.contains(e.relatedTarget))close()});
  // the clear button: empties the field, keeps the focus in it (no blur on mousedown) and shows Recent;
  // it follows the field in the Tab order, and its Enter and Space arrive as clicks
  var qx=q.parentNode.querySelector('.search-x');
  if(qx){qx.addEventListener('mousedown',function(e){e.preventDefault()});
    qx.addEventListener('click',function(){q.value='';say('');q.focus({preventScroll:true});refresh()})}
  q.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();if(res.hidden)refresh();else move(1)}
    else if(e.key==='ArrowUp'){e.preventDefault();if(res.hidden)refresh();else move(-1)}
    // Enter on a closed list reopens the results for the current query; on an open list it follows the selection
    else if(e.key==='Enter'){if(res.hidden){if(q.value.trim()){e.preventDefault();run()}return}var lis=res.querySelectorAll('li[role=option]');var li=lis[sel]||lis[0];if(li&&li.classList.contains('r-fix')){e.preventDefault();applyFix(li);return}if(li&&li.classList.contains('r-more')){e.preventDefault();showAll(true);return}if(li){var a=li.querySelector('a'),it=items[(sel<0?0:sel)-off];if(!li.classList.contains('r-hist')&&it)remember(it);location.href=a.href}}
    // Escape: first closes the list and keeps the text, second clears the text, third leaves the field
    else if(e.key==='Escape'){
      if(!res.hidden){e.preventDefault();close()}
      else if(q.value){e.preventDefault();q.value='';q.parentNode.classList.remove('has-val');say('')}
      else q.blur()}
  });
  // "/" focuses search from anywhere outside a field
  document.addEventListener('keydown',function(e){
    var el=document.activeElement,inField=el&&(/input|textarea|select/i.test(el.tagName)||el.isContentEditable);
    if(inField||e.ctrlKey||e.metaKey||e.altKey)return;
    if(e.key==='/'){e.preventDefault();q.focus({preventScroll:true})}
  });
  document.addEventListener('click',function(e){if(!e.target.closest('.search'))close()});
  var ic=document.querySelector('.search-ic');
  q.addEventListener('focus',function(){if(ic){ic.classList.remove('pop');void ic.offsetWidth;ic.classList.add('pop')}refresh()});
  if(ic)ic.addEventListener('animationend',function(){ic.classList.remove('pop')});
  q.parentNode.classList.toggle('has-val',!!q.value);
})();
