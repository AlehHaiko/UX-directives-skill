
(function(){
  var root=document.documentElement;
  // sticky cover: --cover-h comes from CSS alone, so it follows the width; land a #id clear of it
  var cv=document.querySelector('body>.cover');
  // narrow screens: the banner condenses to one line once the page has scrolled by the height it gives up
  // (the text has then passed under it, so nothing moves); it stays full while one of its arrows or its emblem has focus
  if(cv){var narrow=matchMedia('(max-width: 860px)'),craf=0;
    var cmin=function(){craf=0;var cs=getComputedStyle(root),t=parseFloat(cs.getPropertyValue('--cover-full'))-parseFloat(cs.getPropertyValue('--cover-h'));
      cv.classList.toggle('is-min',narrow.matches&&t>0&&scrollY>t&&!cv.contains(document.activeElement))};
    var creq=function(){if(!craf)craf=requestAnimationFrame(cmin)};
    cmin();addEventListener('scroll',creq,{passive:true});narrow.addEventListener('change',cmin);cv.addEventListener('focusout',creq);cv.addEventListener('focusin',creq)}
  // the Contents banner's emblem shows its quote (.hm.is-q) while a mouse is on the mark itself: the drawn square of svg.hm-mark, grown or not.
  // The mark and the quote keep it, with the strip between the two, so the pointer can reach the text; anywhere else it goes after HM_OUT.
  // The zone is worked out from coordinates, not from :hover: the mark moves and grows under a pointer that stands still.
  // Keyboard focus shows the quote too (CSS), and only the keyboard gives that focus: a press on the mark does not.
  // Touch: a tap on the mark shows the quote and the next tap hides it; a tap on the quote keeps it; a touch anywhere else and a scroll of the page hide it.
  // The quote can be selected: it stays while a selection is being dragged, wherever the pointer goes, and a selection in it is dropped when it hides
  var hm=cv&&cv.querySelector('.hm'),hmMark=hm&&hm.querySelector('.hm-mark'),hmQ=hm&&hm.querySelector('.hm-q'),hmOn={},hmT=0,hmTouch=false,hmSel=false,HM_OUT=200;
  function hmSet(k,v){hmOn[k]=v;var on=!!(hmOn.over||hmOn.tap),s=on?null:getSelection();
    if(s&&s.rangeCount&&hmQ.contains(s.anchorNode))s.removeAllRanges();hm.classList.toggle('is-q',on)}
  function hmIn(x,y,r){return x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom}
  // 1: on the mark (where it is now, or where it rests: the top of .hm, centred); 2: on the shown quote or between it and the mark; 0: elsewhere
  function hmAt(e){if(cv.classList.contains('is-min'))return 0;
    var x=e.clientX,y=e.clientY,r=hmMark.getBoundingClientRect(),b=hm.getBoundingClientRect(),w=parseFloat(getComputedStyle(hmMark).width),l=b.left+(b.width-w)/2;
    if(hmIn(x,y,r)||hmIn(x,y,{left:l,right:l+w,top:b.top,bottom:b.top+w}))return 1;
    if(!hm.matches('.is-q,:focus-visible'))return 0;
    var q=hmQ.getBoundingClientRect();return hmIn(x,y,{left:q.left,right:q.right,top:Math.min(q.top,r.bottom),bottom:q.bottom})?2:0}
  function hmOut(){if(hmOn.over&&!hmT&&!hmSel)hmT=setTimeout(function(){hmT=0;hmSet('over',false)},HM_OUT)}
  if(hm){cv.addEventListener('pointermove',function(e){if(e.pointerType==='touch')return;var z=hmAt(e);
      if(z===1||z===2&&hmOn.over){clearTimeout(hmT);hmT=0;if(!hmOn.over)hmSet('over',true)}else hmOut()});
    cv.addEventListener('pointerleave',function(e){if(e.pointerType!=='touch')hmOut()});
    // a press on the mark does not focus the emblem; a press on its texts starts a selection, and the focus that came with it is given back
    // when the button is released (giving it back at once would stop the selection)
    hm.addEventListener('mousedown',function(e){if(hmMark.contains(e.target))e.preventDefault()});
    hmQ.addEventListener('pointerdown',function(e){if(e.pointerType!=='touch')hmSel=true});
    ['pointerup','pointercancel'].forEach(function(t){document.addEventListener(t,function(e){
      if(document.activeElement===hm&&!hm.matches(':focus-visible'))hm.blur();
      if(hmSel){hmSel=false;if(!hmAt(e))hmOut()}},true)});
    hm.addEventListener('pointerdown',function(e){hmTouch=e.pointerType==='touch'});
    hm.addEventListener('click',function(e){if(hmTouch&&hmAt(e)===1)hmSet('tap',!hmOn.tap)});
    document.addEventListener('pointerdown',function(e){if(hmOn.tap&&!(cv.contains(e.target)&&hmAt(e)))hmSet('tap',false)},true);
    addEventListener('scroll',function(){if(hmOn.tap)hmSet('tap',false)},{passive:true})}
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
  // opened from the keyboard (kb), the focus goes to the current page's item, which the menu has just shown; its chapter folded, to the first control
  function setNav(open,keep,kb){var was=document.body.classList.contains('nav-open');document.body.classList.toggle('nav-open',open);scrim.hidden=!open;sync();
    [].forEach.call(document.querySelectorAll('body>*,.shell>*'),function(n){if(!n.matches('.top,.shell,.sidebar,.scrim,.tip,script'))n.inert=open});
    if(open){var f=side.querySelector('a[href],button'),c=kb&&side.querySelector('[aria-current]');showCur();
      if(c&&!c.closest('[hidden]'))focusTarget(c);else if(f)f.focus({preventScroll:true})}else if(was&&!keep)mb.focus({preventScroll:true})}
  // an opened menu shows where the reader is: the current page's item is brought into view, by the shortest way and at once
  function showCur(){var c=side.querySelector('[aria-current]');if(c)c.scrollIntoView({block:'nearest',behavior:'instant'})}
  function sync(){var open=mobile.matches?document.body.classList.contains('nav-open'):!root.classList.contains('side-hidden');
    var t=mobile.matches?(open?'Close panel':'Open panel'):(open?'Hide panel':'Show panel');
    mb.setAttribute('aria-expanded',open);mb.setAttribute('aria-label',t)}
  function setSide(hidden){root.classList.toggle('side-hidden',hidden);sync();if(!hidden)showCur();try{localStorage.setItem('bb-side',hidden?'hidden':'shown')}catch(e){}}
  if(mb){mb.addEventListener('click',function(e){if(mb.matches(':hover'))mb.classList.add('pv-off');if(mobile.matches)setNav(!document.body.classList.contains('nav-open'),false,e.detail===0);else setSide(!root.classList.contains('side-hidden'))});
    scrim.addEventListener('click',function(){setNav(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!e.defaultPrevented&&mobile.matches&&document.body.classList.contains('nav-open'))setNav(false)});
    mobile.addEventListener('change',function(){if(!mobile.matches)setNav(false,true);else sync()});sync();
    // the icon's hover preview is off from a click until the pointer leaves
    mb.addEventListener('pointerleave',function(){mb.classList.remove('pv-off')});}
  // tooltips: one styled label under an icon-only control; its text is the control's aria-label (the home link's: its emblem's hidden text, while the emblem shows).
  // Hover shows it after TIP_DELAY, at once if another tooltip was showing within TIP_CHAIN; keyboard focus shows it at once; touch: a long press (below).
  // A click and Escape hide it, and it does not return while the pointer stays on the same control.
  // The footer's links and its consent button have it too: each keeps its word as its name, and the tooltip's text is its aria-description: where the link leads, what the button offers.
  // So do the links that open in a new tab (the text links that carry the mark, the GitHub button): their tooltip says so. A text link has none on touch: its long press is the system's link menu
  var TIP_SEL='.menu-btn,.theme-btn,.brand,.search-x,.r-x,.cv-arr,a.cn,.chev,.foot a,.foot-b,.consent-x,.code-copy,.st-dot,a[target=_blank]',TIP_DELAY=400,TIP_CHAIN=300;
  var tip=document.createElement('div'),tipOwn=null,tipOver=null,tipT=0,tipGone=0,tipMute=false,tipPin=false,hintT=0,hintDue=false,HINT_HOLD=4000,canHover=matchMedia('(hover:hover)');
  tip.className='tip';tip.setAttribute('aria-hidden','true');document.body.appendChild(tip);
  function tipCtl(n){var el=n&&n.closest?n.closest(TIP_SEL):null;return el&&tipText(el)?el:null}
  // centred on the control, 8px clear of the viewport's edges, and on the page's side of it: under a control of the header; above a control of the footer
  // or of the consent bar, and above any control that has no room below. With no room above, under it after all.
  // A chapter chevron has the next chevron right under it: its tooltip stands beside it, on the right, or on the left when the right has no room;
  // it stays level with its row up to the viewport's very edge (an 8px margin there would push it onto the row above)
  function tipPlace(){if(!tipOwn)return;var r=tipOwn.getBoundingClientRect();if(!r.width&&!r.height){tipHide();return}
    var w=tip.offsetWidth,h=tip.offsetHeight,vw=root.clientWidth,cx=r.left+r.width/2,side=tipOwn.matches('.chev'),x,y,up=false,sl=false;
    if(side){sl=r.right+6+w>vw-8;x=Math.round(sl?r.left-6-w:r.right+6);y=Math.round(Math.max(0,Math.min(r.top+r.height/2-h/2,innerHeight-h)))}
    else{x=Math.round(Math.max(8,Math.min(cx-w/2,vw-w-8)));up=(tipPin||tipOwn.closest('.consent,.foot')||r.bottom+6+h>innerHeight-8)&&r.top-6-h>=8;y=Math.round(up?r.top-6-h:r.bottom+6)}
    tip.classList.toggle('up',up);tip.classList.toggle('at-r',side&&!sl);tip.classList.toggle('at-l',sl);tip.style.left=x+'px';tip.style.top=y+'px';
    tip.style.transformOrigin=side?(sl?'100% 50%':'0 50%'):(cx-x)+'px '+(up?'100%':'0')}
  // the one exception: a chapter chevron keeps its label and its tooltip names what a click does to the list (the words of "Collapse all" / "Expand all")
  function tipText(el){if(el.matches('.brand')){var m=el.querySelector('.brand-m');return m&&m.offsetWidth?m.textContent:''}
    return el.matches('.chev')?(el.getAttribute('aria-expanded')==='true'?'Collapse':'Expand'):el.getAttribute('aria-label')||el.getAttribute('aria-description')}
  function tipShow(el,say){clearTimeout(tipT);clearTimeout(hintT);hintDue=false;var t=say||tipText(el);if(!t)return;tipPin=!!say;tipOwn=el;tip.textContent=t;tipPlace();if(tipOwn)tip.classList.add('on')}
  function tipHide(){clearTimeout(tipT);clearTimeout(hintT);tipPin=hintDue=false;if(tipOwn){tipOwn=null;tipGone=Date.now();tip.classList.remove('on')}}
  // a hint: the same label shown by script over a control, above it, with words of its own (the answer just given, over the footer's consent button).
  // It is pinned: it stays HINT_HOLD whatever the pointer and the focus do elsewhere, longer while the pointer is on it or on its control, and then leaves
  // as any tooltip does. A click on its control, Escape, another control's tooltip or a resize end it at once
  function hintShow(el,say){tipShow(el,say);if(!tipOwn)return;
    hintT=setTimeout(function(){hintDue=true;if(!(canHover.matches&&(el.matches(':hover')||tip.matches(':hover'))))tipHide()},HINT_HOLD)}
  // a click or Escape may move the focus by script (the menu closing): that focus shows no tooltip
  function tipDismiss(keep){if(!keep)tipHide();tipMute=true;setTimeout(function(){tipMute=false},0)}
  document.addEventListener('pointerover',function(e){
    if(e.pointerType==='touch'||!canHover.matches||tip.contains(e.target))return;
    if(tipPin){if(hintDue&&tipCtl(e.target)!==tipOwn)tipHide();return}
    var el=tipCtl(e.target);if(el===tipOver)return;tipOver=el;clearTimeout(tipT);
    if(!el){if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();return}
    if(tipOwn||Date.now()-tipGone<TIP_CHAIN)tipShow(el);else tipT=setTimeout(function(){tipShow(el)},TIP_DELAY)});
  root.addEventListener('pointerleave',function(e){if(e.pointerType==='touch')return;if(tipPin){if(hintDue)tipHide();return}tipOver=null;if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();else clearTimeout(tipT)});
  document.addEventListener('focusin',function(e){var el=tipCtl(e.target);if(el&&!tipMute&&el.matches(':focus-visible'))tipShow(el)});
  document.addEventListener('focusout',function(e){if(tipOwn&&!tipPin&&tipCtl(e.target)===tipOwn&&tipOver!==tipOwn)tipHide()});
  document.addEventListener('click',function(e){
    // the click of a release that ended a long press: it does nothing and the tooltip stays
    if(holdEat&&Date.now()-holdEat<HOLD_EAT){holdEat=0;e.preventDefault();e.stopImmediatePropagation();return}
    tipDismiss(tipPin&&tipCtl(e.target)!==tipOwn)},true);
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
    var el=e.touches.length===1?tipCtl(e.target):null;if(!el||el.matches('.ext-w>a'))return;
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
    var cueGo=function(e,el,hd){if(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
      // where the jump will stop: the heading's line (the sticky heading's mark), kept within the page
      var d=topOf(el)-(parseFloat(getComputedStyle(el).scrollMarginTop)||0);
      cueY=Math.max(0,Math.min(scrollY+d,root.scrollHeight-innerHeight));
      cueEl=hd;if(Math.abs(cueY-scrollY)<1){cueNow();return}
      addEventListener('scroll',cueWait,{passive:true});addEventListener('scrollend',cueEnd);
      // the jump can start a few frames late: give it 400ms before taking "no scroll" for an answer
      clearTimeout(cueT);cueT=setTimeout(cueNow,400)};
    links.forEach(function(a){var el=document.getElementById(a.getAttribute('href').slice(1));if(!el)return;
      // #directives is the mark before the sticky heading: the jump is measured on the mark, the cue plays on the heading
      var hd=el.classList.contains('dh-mark')?el.nextElementSibling:el;
      if(!a.closest('.nav-sec'))hd.addEventListener('animationend',function(e){if(e.target===hd&&/^bb-cue-/.test(e.animationName))hd.classList.remove('cue')});
      a.addEventListener('click',function(e){cueGo(e,el,hd)})});
    // a button in the page's text that leads to one of its sections ("Install skill" on the skill's page) lands as a line of "On this page" does: the same jump, the same cue
    [].forEach.call(document.querySelectorAll('.sk-cta a[href^="#"]'),function(a){var el=document.getElementById(a.getAttribute('href').slice(1));
      if(el)a.addEventListener('click',function(e){cueGo(e,el,el)})});
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
    // the heading also moves with no scroll and no resize of the window: the menu shown or hidden changes the column's width,
    // the text above reflows and the heading leaves or takes its stuck place. The column's own box tells of every such change
    var col=dh.closest('.main');if(col&&window.ResizeObserver)new ResizeObserver(req).observe(col);
    // links to the heading: a native jump lands by its stuck place, so go to the mark's line and set hash and focus by hand
    // (location.hash, not pushState: it moves :target too; the scroll it starts is replaced by the one below)
    [].forEach.call(document.querySelectorAll('a[href="#directives"]'),function(a){a.addEventListener('click',function(e){
      if(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;e.preventDefault();
      var y=scrollY+mk.getBoundingClientRect().top-(parseFloat(getComputedStyle(mk).scrollMarginTop)||0);
      if(location.hash!=='#directives')location.hash='directives';
      focusTarget();scrollTo(0,Math.max(0,Math.min(y,root.scrollHeight-innerHeight)))})});}
  // analytics consent: the choice lives in localStorage "ah-consent" ("granted" or "denied"; the portfolio the book is read under keeps the same key).
  // Until there is one the bar is shown and Google Analytics is not loaded (ahGa, the page's head: it loads on alehhaiko.com alone, the bar shows on every host).
  // Storage that fails keeps the choice for this page: the bar comes back on the next load.
  // The text's second line says what holds now: analytics stays off until allowed, is on, or is off; the words that carry it are bold.
  // The answer that holds is not offered again: its button states the fact instead ("Analytics allowed", "Analytics declined"), aria-disabled, so it keeps
  // its place in the Tab order and is read out, and a press on it does nothing.
  // The body keeps the bar's height free at its bottom, so the footer can be scrolled clear of it.
  // Brought back from the footer with an answer given, the bar has a cross: it and Escape close the bar and change nothing, and the focus returns to the footer's button.
  // An answer given, the footer's button says so once in a hint over it ("You allowed analytics", "You declined analytics"): at once if the button is in view,
  // or when it first comes into view; after the reload that follows a withdrawal, on the new page.
  // The answer is also said aloud, in a status line that is not drawn (.consent-say): what was answered and where to change it.
  // The footer's button says "GA on" or "GA off" (data-ga; the words are in the page, CSS shows the one that holds) and shows the bar again, with the focus on the button that can be pressed.
  // Declining after analytics was allowed removes Google Analytics' cookies (_ga, _ga_*: this host's and .alehhaiko.com's) and loads the page anew,
  // without it; the focus then goes to the text, as after any answer.
  var cb=document.querySelector('.consent'),CONSENT='ah-consent',consent=null;
  try{consent=localStorage.getItem(CONSENT)}catch(e){}
  if(consent!=='granted'&&consent!=='denied')consent=null;
  function consentRoom(){root.style.setProperty('--consent-h',cb.hidden?'0px':cb.offsetHeight+'px')}
  var CONSENT_SAYS={granted:'You <strong>allowed</strong> it. Current state is <strong>on</strong>.',denied:'You <strong>declined</strong> it. Current state is <strong>off</strong>.'};
  var CONSENT_ACT={granted:'Allow analytics',denied:'Decline analytics'},CONSENT_FACT={granted:'Analytics allowed',denied:'Analytics declined'};
  function consentShow(on){
    if(on){cb.querySelector('.consent-s').innerHTML=CONSENT_SAYS[consent]||'It stays <strong>off</strong> unless you allow it.';
      [].forEach.call(cb.querySelectorAll('[data-consent]'),function(b){var v=b.dataset.consent,is=v===consent;
        b.textContent=(is?CONSENT_FACT:CONSENT_ACT)[v];if(is)b.setAttribute('aria-disabled','true');else b.removeAttribute('aria-disabled')})}
    var can=on&&!!consent;cb.classList.toggle('can-close',can);cx.hidden=!can;
    cb.hidden=!on;consentRoom()}
  var CONSENT_HINT={granted:'You allowed analytics',denied:'You declined analytics'},hintIO=null;
  function consentHint(){if(hintIO){hintIO.disconnect();hintIO=null}if(!cs||!window.IntersectionObserver||!CONSENT_HINT[consent])return;var say=CONSENT_HINT[consent];
    hintIO=new IntersectionObserver(function(en){if(!en[en.length-1].isIntersecting)return;hintIO.disconnect();hintIO=null;hintShow(cs,say)},{threshold:1});hintIO.observe(cs)}
  var csay=document.querySelector('.consent-say'),CONSENT_SAY={granted:'You allowed analytics. Change it with GA in the footer.',denied:'You declined analytics. Change it with GA in the footer.'};
  // the line is emptied first and filled a moment later, so the same words are read out again after the same answer
  function consentSay(){if(!csay||!CONSENT_SAY[consent])return;csay.textContent='';setTimeout(function(){csay.textContent=CONSENT_SAY[consent]},100)}
  function consentClose(){consentShow(false);if(cs)cs.focus({preventScroll:true})}
  var cs=document.querySelector('.foot-b'),cx=document.querySelector('.consent-x');
  function consentMark(){if(cs)cs.dataset.ga=consent==='granted'?'on':'off'}
  if(cb){
    consentMark();
    var consentX=0,consentY=0;cb.addEventListener('pointerdown',function(e){consentX=e.clientX;consentY=e.clientY});
    cb.addEventListener('click',function(e){var b=e.target.closest('[data-consent]');if(!b||b.getAttribute('aria-disabled')==='true')return;
      // the buttons' words can be selected: a pointer's click that moved over HOLD_MOVE since it went down, or leaves a selection in the button, was a drag, not a press
      var sel=getSelection();if(e.detail&&(Math.hypot(e.clientX-consentX,e.clientY-consentY)>HOLD_MOVE||sel&&!sel.isCollapsed&&b.contains(sel.anchorNode)))return;
      var was=consent;consent=b.dataset.consent;
      try{localStorage.setItem(CONSENT,consent)}catch(err){}
      consentShow(false);consentMark();
      if(consent==='denied'&&was==='granted'){
        document.cookie.split(';').forEach(function(c){var n=c.split('=')[0].trim();if(!/^_ga(_|$)/.test(n))return;
          ['',';domain='+location.hostname,';domain=.alehhaiko.com'].forEach(function(d){document.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/'+d})});
        try{sessionStorage.setItem(CONSENT+'-focus','1')}catch(err){}
        location.reload();return}
      if(consent==='granted')ahGa();
      focusTarget(document.getElementById('main'));consentHint();consentSay()});
    cx.addEventListener('click',consentClose);
    // Escape closes the bar that the cross can close, last of three: the open drawer takes the key first, then the search (its list, its text, its focus:
    // every Escape pressed in it). The key is read on its way down, before the drawer's and the field's own handlers change what it is asked about
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!cb.hidden&&!cx.hidden&&!document.body.classList.contains('nav-open')&&!(e.target.closest&&e.target.closest('.search')))consentClose()},true);
    if(window.ResizeObserver)new ResizeObserver(consentRoom).observe(cb);else addEventListener('resize',consentRoom);
    if(cs)cs.addEventListener('click',function(){if(hintIO){hintIO.disconnect();hintIO=null}consentShow(true);cb.querySelector('[data-consent]:not([aria-disabled="true"])').focus({preventScroll:true})});
    try{if(sessionStorage.getItem(CONSENT+'-focus')){sessionStorage.removeItem(CONSENT+'-focus');focusTarget(document.getElementById('main'));consentHint();consentSay()}}catch(e){}
    if(!consent)consentShow(true)}
  // text to copy (the skill's page): the button copies its box's text and says so, in the pinned hint over it and in the status line that is not drawn;
  // its sign is a tick for 2s. Where the clipboard cannot be written, the text is selected, so the reader's own copy is one key away
  // (and the hint that says so stays until that selection is gone)
  var skSay=document.querySelector('.sk-say');
  [].forEach.call(document.querySelectorAll('.code-copy'),function(b){var c=b.parentNode.querySelector('code'),okT=0;
    function done(ok){var t=ok?'Copied':'Not copied: the text is selected, copy it yourself';b.classList.toggle('is-ok',ok);b.parentNode.classList.toggle('is-ok',ok);clearTimeout(okT);
      if(ok){okT=setTimeout(function(){b.classList.remove('is-ok');b.parentNode.classList.remove('is-ok')},2000);hintShow(b,t)}
      // not copied: the hint is the only sign, so it does not leave by the clock. It stays while the text it speaks of stays selected,
      // and goes with the selection (or with a press on the button, Escape or a resize, as any pinned hint does)
      else{tipShow(b,t);var gone=function(){var g=getSelection();if(g.rangeCount&&!g.isCollapsed&&c.contains(g.anchorNode))return;
        document.removeEventListener('selectionchange',gone);if(tipOwn===b)tipHide()};setTimeout(function(){document.addEventListener('selectionchange',gone)},0)}
      if(skSay){skSay.textContent='';setTimeout(function(){skSay.textContent=t},50)}}
    function byHand(){var r=document.createRange(),g=getSelection(),ok=false;r.selectNodeContents(c);g.removeAllRanges();g.addRange(r);
      try{ok=document.execCommand('copy')}catch(e){}if(ok)g.removeAllRanges();done(ok)}
    b.addEventListener('click',function(){if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(c.textContent).then(function(){done(true)},byHand);else byHand()})});
  // scheme 1 (the skill's page): the parts of an ID. A part is a button, the three one Tab stop: the arrow keys, Home and End move between them.
  // What is lit is the part under the pointer, else the one the keyboard focused (a pointer's own focus lights nothing), else the pressed one (a click, a tap, Enter or Space press a part; the same again releases it).
  // A name lights its part too, and a press on a name, off its link, presses the part. Lit: the part, its line and its name (style.css, .on)
  var idg=document.querySelector('.sch-id');
  if(idg){var idPs=[].slice.call(idg.querySelectorAll('.id-p')),idAll=[].slice.call(idg.querySelectorAll('[data-p]')),idPin=null,idHov=null,idFoc=null;
    var idShow=function(){var k=idHov||idFoc||idPin;idg.classList.toggle('has-on',!!k);idAll.forEach(function(n){n.classList.toggle('on',n.dataset.p===k)})};
    var idPress=function(k){idPin=idPin===k?null:k;idPs.forEach(function(p){p.setAttribute('aria-pressed',p.dataset.p===idPin)});idShow()};
    var idGo=function(i){i=Math.max(0,Math.min(idPs.length-1,i));idPs.forEach(function(p,j){p.tabIndex=j===i?0:-1});idPs[i].focus()};
    idPs.forEach(function(p,i){p.setAttribute('role','button');p.tabIndex=i?-1:0;p.setAttribute('aria-pressed','false');p.setAttribute('aria-describedby','id-l-'+p.dataset.p);
      p.addEventListener('focus',function(){idFoc=p.matches(':focus-visible')?p.dataset.p:null;idShow()});p.addEventListener('blur',function(){idFoc=null;idShow()});
      p.addEventListener('keydown',function(e){if(e.ctrlKey||e.metaKey||e.altKey)return;var k=e.key,to=k==='ArrowRight'||k==='ArrowDown'?i+1:k==='ArrowLeft'||k==='ArrowUp'?i-1:k==='Home'?0:k==='End'?idPs.length-1:null;
        if(to!==null){e.preventDefault();idGo(to)}else if(k==='Enter'||k===' '){e.preventDefault();idPress(p.dataset.p)}})});
    idg.addEventListener('click',function(e){var n=e.target.closest('.id-p,.id-l');if(n&&!e.target.closest('a'))idPress(n.dataset.p)});
    idg.addEventListener('pointerover',function(e){if(e.pointerType==='touch')return;var n=e.target.closest('.id-p,.id-l');idHov=n?n.dataset.p:null;idShow()});
    idg.addEventListener('pointerleave',function(){idHov=null;idShow()})}
  // a box whose content changes takes its new height as the menu's lists fold (style.css, .sk-h): from the height it has to the height its new content needs,
  // then the height is its content's again. With reduced motion the change is at once
  function skGrow(box,change){var h0=box.offsetHeight,h1;clearTimeout(box._g);box.classList.remove('sk-h');box.style.height='';change();h1=box.offsetHeight;
    if(h0===h1||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    box.style.height=h0+'px';void box.offsetHeight;box.classList.add('sk-h');box.style.height=h1+'px';
    box._g=setTimeout(function(){box.classList.remove('sk-h');box.style.height=''},480)}
  // the step shown and the role chosen are kept for the tab's session, so a reader who follows a link from a role and comes back finds the page as it was left
  var skSt={};try{skSt=JSON.parse(sessionStorage.getItem('bb-skill')||'{}')||{}}catch(e){}
  function skKeep(k,v){skSt[k]=v;try{sessionStorage.setItem('bb-skill',JSON.stringify(skSt))}catch(e){}}
  // scheme 2 (the skill's page): the steps. Without script they are a list; here one shows at a time. The rail's rings go to their steps, Previous and Next step,
  // and so do the left and right arrow keys while the focus is in the figure; a button with nowhere to go stays in the Tab order and says so (aria-disabled).
  // The ring of the step shown says so (aria-current); a status line that is not drawn says the step and its name after each change
  var stg=document.querySelector('.sch-st');
  if(stg){var stI=[].slice.call(stg.querySelectorAll('.st-i')),stD=[].slice.call(stg.querySelectorAll('.st-rail .st-dot')),stL=[].slice.call(stg.querySelectorAll('.st-ln')),
      stP=stg.querySelector('.st-prev'),stN=stg.querySelector('.st-next'),stSay=stg.querySelector('.st-say'),stAt=-1;
    var stBox=stg.querySelector('.st-list');
    var stSet=function(i){i=Math.max(0,Math.min(stI.length-1,i));if(i===stAt)return;var d=i<stAt?-1:1,first=stAt<0;stAt=i;
      // the focus on a link in the step that is being folded goes to the ring of the step shown: it stays in the figure, and the arrow keys go on working
      var lost=stI.some(function(li,j){return j!==i&&li.contains(document.activeElement)});
      var show=function(){stI.forEach(function(li,j){if(j===i)li.removeAttribute('hidden');else li.setAttribute('hidden','until-found');li.classList.remove('in')})};
      if(first)show();else skGrow(stBox,show);if(lost){tipDismiss();stD[i].focus()}
      if(!first){stI[i].style.setProperty('--st-d',d);void stI[i].offsetWidth;stI[i].classList.add('in')}
      stD.forEach(function(b,j){b.classList.toggle('is-cur',j===i);b.classList.toggle('is-done',j<i);if(j===i)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current')});
      stL.forEach(function(l,j){l.classList.toggle('is-done',j<i)});
      stP.setAttribute('aria-disabled',i===0);stN.setAttribute('aria-disabled',i===stI.length-1);
      skKeep('s',i);if(!first)stSay.textContent='Step '+(i+1)+' of '+stI.length+': '+stI[i].querySelector('.st-h').textContent};
    stg.classList.add('is-js');stg.querySelector('.st-ctl').hidden=false;stg.querySelector('.st-rail').hidden=false;stSet(+skSt.s||0);
    // find-in-page lands in a folded step: that step is shown
    stI.forEach(function(li,j){li.addEventListener('beforematch',function(){stSet(j)})});
    stD.forEach(function(b,j){b.addEventListener('click',function(){stSet(j)})});
    stP.addEventListener('click',function(){stSet(stAt-1)});stN.addEventListener('click',function(){stSet(stAt+1)});
    stg.addEventListener('keydown',function(e){if(e.ctrlKey||e.metaKey||e.altKey||e.shiftKey)return;
      var k=e.key==='ArrowLeft'?-1:e.key==='ArrowRight'?1:0;if(!k)return;e.preventDefault();stSet(stAt+k);
      // on the rail the focus goes with the step, as the choice goes with the focus among the roles
      // the focus this moves shows no tooltip (as after Enter on a ring): the step's name has just appeared right under the rail, and the tooltip would lie over it
      if(document.activeElement.classList.contains('st-dot')){tipDismiss();stD[stAt].focus()}})}
  // scheme 3 (the skill's page): the roles. One choice of eight: a radio group, one Tab stop; the arrow keys move the choice round the group, Home and End take its ends.
  // Each of the three boxes shows the chosen role's answer and takes its height (skGrow), so the names over them stand still. The table says the same for a page without script: here it is hidden
  var rlg=document.querySelector('.sch-rl');
  if(rlg){var rlB=[].slice.call(rlg.querySelectorAll('[role="radio"]')),rlS=[].slice.call(rlg.querySelectorAll('.rl-s')),rlT=document.querySelector('.tbl'),rlAt=-1;
    var rlSet=function(i,go){var first=rlAt<0;rlAt=i;skKeep('r',i);rlB.forEach(function(b,j){b.setAttribute('aria-checked',j===i);b.tabIndex=j===i?0:-1});
      rlS.forEach(function(box){var show=function(){[].forEach.call(box.children,function(v,j){if(j===i)v.removeAttribute('hidden');else v.setAttribute('hidden','until-found')})};
        if(first)show();else skGrow(box,show)});if(go)rlB[i].focus()};
    rlB.forEach(function(b,i){b.addEventListener('click',function(){rlSet(i)});
      b.addEventListener('keydown',function(e){if(e.ctrlKey||e.metaKey||e.altKey)return;var n=rlB.length,k=e.key,
        to=k==='ArrowRight'||k==='ArrowDown'?(i+1)%n:k==='ArrowLeft'||k==='ArrowUp'?(i+n-1)%n:k==='Home'?0:k==='End'?n-1:null;
        if(to!==null){e.preventDefault();rlSet(to,true)}})});
    rlg.hidden=false;if(rlT)rlT.hidden=true;rlSet(Math.min(rlB.length-1,Math.max(0,+skSt.r||0)));
    // find-in-page lands in a folded answer: its role is chosen
    rlS.forEach(function(box){[].forEach.call(box.children,function(v,j){v.addEventListener('beforematch',function(){rlSet(j)})})})}
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
  // ---- a Recent entry leaves: it fades and gives up its height on --soft while what follows rides up into its place on --spring
  // (the menu's fold and a card's lift). Storage and the option list change at the click; the node goes when the motion ends
  var LEAVE=450,hov=null,gapA=null;
  // reduced motion: the entry is gone at once; the focus and the announcement are the same
  function calm(){return matchMedia('(prefers-reduced-motion:reduce)').matches}
  function leaving(){return !res.hidden&&!!res.querySelector('.r-out')}
  function ease(n){return getComputedStyle(root).getPropertyValue(n).trim()||'ease-out'}
  function near(li,dir){do li=li[dir];while(li&&li.classList.contains('r-out'));return li&&li.classList.contains('r-hist')?li:null}
  // said by #q-status once the list is quiet; emptied first, so the same words are said again after a second removal
  function tell(t){if(status)status.textContent='';say(t)}
  function stays(li){do li=li.nextElementSibling;while(li&&li.classList.contains('r-out'));return li}
  // a collapsed row still has the grid's gap after it: the next row that stays takes the gap back as a negative margin at the
  // collapse's pace, and hands it on if it leaves too
  function drop(rec){if(rec.m)rec.m.cancel();rec.m=null;if(rec.on)rec.on._m=rec.on._m.filter(function(r){return r!==rec});rec.on=null}
  function carry(rec,li){var t=rec.m?rec.m.currentTime:0,nx=stays(li);drop(rec);if(!nx)return;
    rec.m=nx.animate({marginTop:['0px',-rec.gap+'px']},{duration:LEAVE,easing:ease('--soft'),fill:'forwards',composite:'add'});rec.m.currentTime=t;rec.on=nx;(nx._m=nx._m||[]).push(rec)}
  function out(li,x,mark,all){
    if(li.classList.contains('r-out'))return false;
    var h=li.getBoundingClientRect().height,gap=parseFloat(getComputedStyle(res).rowGap)||0,d=h+gap,soft=ease('--soft'),spring=ease('--spring'),rec={gap:gap,m:null,on:null},i=items.indexOf(x),n;
    saveHist(hist().filter(function(e){return e.url!==x.url}));
    // no longer an option: the arrows skip it and the rest are numbered anew
    if(i>-1)items.splice(i,1);sel=-1;q.removeAttribute('aria-activedescendant');
    li.className+=' r-out'+(mark?' '+mark:'');li.removeAttribute('role');li.removeAttribute('id');li.setAttribute('aria-hidden','true');li.inert=true;
    [].forEach.call(res.querySelectorAll('li[role=option]'),function(l,k){l.id='r'+k;l.removeAttribute('aria-selected')});
    // the heading's count follows at the click; with the last entry, or all of them, the heading leaves as it is
    var c=res.querySelector('.r-c'),left=res.querySelectorAll('.r-hist:not(.r-out)').length;if(c&&left&&!all)c.textContent=left;
    if(calm()){(li._m||[]).forEach(drop);li.remove();if(!res.querySelector('.r-hist'))close();return true}
    (li._m||[]).forEach(function(r){carry(r,li)});li._m=null;if(!all)carry(rec,li);
    // the last entry takes the heading and "Clear history" with it: the list closes when it is gone
    if(!res.querySelector('.r-hist:not(.r-out)'))[].forEach.call(res.querySelectorAll('.r-head'),function(n){n.inert=true;n.animate({opacity:[1,0]},{duration:LEAVE,easing:soft,fill:'forwards'})});
    // the layout moves what follows at the collapse's pace; the difference to the spring is added as a transform that ends at 0
    if(!all&&spring!==soft)for(n=li.nextElementSibling;n;n=n.nextElementSibling){
      n.animate({transform:['translateY(0)','translateY('+-d+'px)']},{duration:LEAVE,easing:spring,composite:'add'});
      n.animate({transform:['translateY(0)','translateY('+d+'px)']},{duration:LEAVE,easing:soft,composite:'add'})}
    li.animate({height:[h+'px','0px'],opacity:[1,0]},{duration:LEAVE,easing:soft,fill:'forwards'}).onfinish=function(){
      if(li.parentNode!==res)return;
      drop(rec);li.remove();
      if(leaving())return;
      if(gapA){gapA.cancel();gapA=null}
      if(!res.querySelector('.r-hist'))close();
      // the tooltip does not return while the pointer stays: the button that arrived under it is, to the tooltip, the control just clicked
      if(hov){tipOver=tipCtl(hov.isConnected?hov:null);hov=null}
      var f=document.activeElement;if(res.contains(f)&&f.matches('.r-x:focus-visible'))tipShow(f)};
    return true}
  // "Clear history": every entry leaves in the same motion, then the list closes. Nothing stays to ride up or to take the gaps
  // back, so the list's own gap closes at the collapse's pace; a new render (refresh) drops that animation
  function outAll(mark){var ls=[].slice.call(res.querySelectorAll('.r-hist:not(.r-out)')),xs=items.slice();if(!ls.length)return;
    if(!calm())gapA=res.animate({rowGap:[getComputedStyle(res).rowGap,'0px']},{duration:LEAVE,easing:ease('--soft'),fill:'forwards'});
    ls.forEach(function(li,i){out(li,xs[i],mark,true)});saveHist([])}
  // while entries leave, the buttons that pass under a resting pointer raise no tooltip
  res.addEventListener('pointerover',function(e){if(leaving()){hov=e.target;e.stopPropagation()}});
  res.addEventListener('pointerleave',function(){hov=null});
  // a press that lands on a leaving entry, before the next one is under the pointer, does nothing: the focus stays where it is
  res.addEventListener('mousedown',function(e){if(leaving()&&!e.target.closest('a,button'))e.preventDefault()});
  function showHist(){
    var h=hist();res.innerHTML='';sel=-1;off=0;items=[];q.removeAttribute('aria-activedescendant');say('');
    if(!h.length){res.hidden=true;q.setAttribute('aria-expanded','false');return}
    // the heading's row ends with "Clear history": it comes before the entries on the screen and in the Tab order
    var head=document.createElement('li');head.className='r-head';head.innerHTML='<span class="r-n">Recent<span class="r-sr">, </span><span class="bul" aria-hidden="true"></span><span class="r-c">'+h.length+'</span></span><button type="button" class="r-clear">Clear history</button>';
    head.querySelector('button').addEventListener('click',function(e){e.stopPropagation();var b=e.currentTarget;outAll(canHover.matches&&b.matches(':hover')||b.matches(':focus-visible')?'r-brick':'');q.focus({preventScroll:true});tell('History cleared')});
    res.appendChild(head);
    h.forEach(function(x,i){
      var li=document.createElement('li');li.setAttribute('role','option');li.id='r'+i;li.className='r-hist rc'+x.c;
      li.innerHTML='<a href="'+x.url+'"><span class="r-id">'+x.id+'</span><span class="r-t">'+hl(x.title,[])+'</span>'+(x.q?'<span class="r-q">'+hl(x.q,[])+'</span>':'')+'</a>'
        +'<button type="button" class="r-x" aria-label="Remove from history"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M5.4 5.4l9.2 9.2M14.6 5.4l-9.2 9.2"/></svg></button>';
      li.querySelector('.r-x').addEventListener('click',function(e){e.preventDefault();e.stopPropagation();
        var b=e.currentTarget,held=canHover.matches&&b.matches(':hover')||b.matches(':focus-visible');
        var to=near(li,'nextElementSibling')||near(li,'previousElementSibling'),still=calm();
        if(!out(li,x,held?'r-brick r-tint':''))return;
        // the focus goes to the button of the entry that takes this one's place: the next, else the previous, else the field.
        // Its tooltip waits for the motion's end, where the button comes to rest; with no motion the button is there already
        tipMute=!still;(to?to.querySelector('.r-x'):q).focus({preventScroll:true});tipMute=false;
        // no motion: the next entry's button is under the pointer at once. To the tooltip it is the control just clicked,
        // so the tooltip does not return while the pointer stays (a click from the keyboard has no pointer place)
        if(still&&e.detail)tipOver=tipCtl(document.elementFromPoint(e.clientX,e.clientY));
        tell('Removed from history')});
      res.appendChild(li);items.push(x);
    });
    res.hidden=false;q.setAttribute('aria-expanded','true');
    res.scrollTop=0;
  }
  function refresh(){if(gapA){gapA.cancel();gapA=null}q.parentNode.classList.toggle('has-val',!!q.value);if(q.value.trim())run();else showHist()}
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
  // the focus returning to the field while entries leave keeps the list as it is: a new render would cut the motion
  q.addEventListener('focus',function(){if(ic){ic.classList.remove('pop');void ic.offsetWidth;ic.classList.add('pop')}if(!leaving())refresh()});
  if(ic)ic.addEventListener('animationend',function(){ic.classList.remove('pop')});
  q.parentNode.classList.toggle('has-val',!!q.value);
})();
