#!/usr/bin/env python3
"""Build the static site for The Blue Book of UX Directives.

Source of truth: ux-directives/references/*.md (the same files the skill uses).
Run from the repository root:
    python3 tools/build_site.py [--base /path/] [--out PATH]
--base is the URL path the site is served from (default "/").
--out is the folder the site is written to (default site/).
Writes the HTML pages and 404.html to the output folder and refreshes its assets/. No dependencies.
Favicons in site/assets/ are static files and are not touched; a build to another folder copies them there.
"""
import argparse
import html
import json
import math
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "ux-directives" / "references"
SITE = ROOT / "site"  # default output directory (the Vercel root); home of the hand-kept favicons
FAVICONS = ("favicon.ico", "favicon-32.png", "apple-touch-icon.png")

BOOK_TITLE = "The Blue Book of UX Directives"
BOOK_SUBTITLE = "A Uniform Code for Human-Centered Digital Systems"
AUTHOR = "Aleh Haiko"

# Chapter palettes, taken from the author's cover SVGs (dark, overlay, overlay opacity, light text, accent)
# and bookmark colors from the original pages.
PALETTE = {
    1: ("#241328", "#513956", 0.2, "#ffd6df", "#ee82ee", "#9065b0"),
    2: ("#1c1f26", "#323642", 0.2, "#f0f7e3", "#3ee439", "#448361"),
    3: ("#091c16", "#134949", 0.2, "#ceece6", "#00ffff", "#337ea9"),
    4: ("#2a040e", "#611c31", 0.1, "#ffe1c3", "#ffa528", "#d9730d"),
    5: ("#110c33", "#2c4597", 0.1, "#e1ebea", "#fff500", "#cb912f"),  # accent was #e7fb0b (lime); pure yellow, same contrast class
    6: ("#151627", "#373b55", 0.2, "#e1dee5", "#ffd596", "#9f6b53"),
    7: ("#192125", "#343e41", 0.4, "#e8e9e5", "#ffa500", "#d9730d"),
    8: ("#1b1831", "#4a4378", 0.2, "#e7e6ef", "#1ef58d", "#448361"),
    9: ("#241d1c", "#3f3632", 0.4, "#fbead9", "#28fff1", "#337ea9"),
}

SECTIONS = [  # (key, emoji, title, arrow-to-name)
    ("ask", "🤔", "First, ask yourself", False),
    ("mission", "🫡", "Mission statement", False),
    ("heuristics", "🚀", "Key heuristics", True),
    ("brief", "☝️", "Executive brief", False),
    ("core", "🤔", "Core questions", True),
    ("focus", "🧐", "Focus areas", False),
    ("directives", "🧬", "UX directives", True),
    ("summary", "⚡", "Executive summary", False),
    ("indicators", "😎", "Success indicators", False),
    ("oneline", "☝️", "One-line summary", False),
]


# ---------------------------------------------------------------- markdown helpers
def inline(text):
    """Escape and render inline markdown: links, **bold**, *italic*, `code`."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", out)
    return out


def md_blocks(text):
    """Render a small markdown subset (paragraphs, lists, blockquotes, h2/h3) to HTML."""
    lines = text.strip("\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        m = re.match(r"^(#{2,3}) (.+)$", ln)
        if m:
            lvl = len(m.group(1))
            out.append(f'<h{lvl} id="{slug(m.group(2))}">{inline(m.group(2))}</h{lvl}>')
            i += 1
            continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].lstrip())
                i += 1
            out.append("<blockquote>" + md_blocks("\n".join(buf)) + "</blockquote>")
            continue
        if re.match(r"^(- |\d+\. )", ln):
            ordered = bool(re.match(r"^\d+\. ", ln))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{2,3} |>|- |\d+\. )", lines[i]):
            buf.append(lines[i])
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")
    return "\n".join(out)


def slug(s):
    s = s.lower().replace("&", "and").replace("’s ", " ").replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- parsing
def bullets(block):
    return [re.sub(r"^- ", "", l) for l in block.split("\n") if l.startswith("- ")]


def parse_section(sec, chapter):
    head = re.match(r"## (\d+)\.(\d+) (.+)\n", sec)
    num = int(head.group(2))
    s = {
        "chapter": chapter,
        "num": num,
        "code": f"{chapter}.{num}",
        "name": head.group(3).strip(),
    }
    s["governs"] = re.search(r"^> (.+)$", sec, re.M).group(1).strip()
    for key, label in [("ask", "Ask yourself"), ("mission", "Mission"),
                       ("brief", "Executive brief"), ("oneline", "One-line summary")]:
        m = re.search(rf"^\*\*{label}:\*\* (.+)$", sec, re.M)
        s[key] = m.group(1).strip() if m else ""
    parts = re.split(r"^### (.+)$", sec, flags=re.M)
    blocks = {parts[k].strip(): parts[k + 1] for k in range(1, len(parts) - 1, 2)}
    s["heuristics"] = bullets(blocks["Key heuristics"])
    s["core"] = bullets(blocks["Core questions"])
    s["summary"] = bullets(blocks["Executive summary"])
    s["indicators"] = bullets(blocks["Success indicators"])
    s["focus"] = []
    for b in bullets(blocks["Focus areas"]):
        m = re.match(r"\*\*(.+?):\*\* (.+)$", b)
        qs = re.findall(r"“[^”]+”", m.group(2))
        s["focus"].append((m.group(1), qs or [m.group(2)]))
    s["directives"] = []
    for b in bullets(blocks["Directives"]):
        m = re.match(r"\*\*(\d{2,3}/\d{2}) ?— ?(.+?)\*\* (.+)$", b)
        did, title, body = m.groups()
        rep = None
        if title == "Repealed.":
            r = re.match(r"Merged into (\d{2,3}/\d{2}) ?— ?(.+)$", body)
            rep = (r.group(1), r.group(2)) if r else None
        s["directives"].append({"id": did, "title": title, "body": body, "repealed": rep})
    s["file"] = f"{chapter}-{num}-{slug(s['name'])}.html"
    return s


def parse_chapter(path):
    t = path.read_text(encoding="utf-8")
    h1 = re.match(r"^# Chapter (\d+): (.+)$", t, re.M)
    n = int(h1.group(1))
    pre = t.split("\n## ")[0]
    intro = [l[2:].replace("**", "") for l in pre.split("\n") if l.startswith("> ") and l[2:].strip()]
    mission = re.search(r"^\*\*Mission statement:\*\* (.+)$", pre, re.M).group(1)
    secs = [parse_section(x, n) for x in re.split(r"^(?=## \d+\.\d+ )", t, flags=re.M)[1:]]
    return {"n": n, "title": h1.group(2).strip(), "intro": intro, "mission": mission,
            "subs": secs, "file": f"chapter-{n}-{slug(h1.group(2))}.html"}


def parse_index():
    t = (REF / "index.md").read_text(encoding="utf-8")
    keep = []
    for name in ("Preface", "How this book is organized", "General provisions"):
        m = re.search(rf"^## {re.escape(name)}\n(.*?)(?=^## |^Use this index)", t, re.M | re.S)
        if m:
            keep.append((name, m.group(1)))
    return keep


# ---------------------------------------------------------------- rendering
ICON_SEARCH = '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M13 13l4.5 4.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


# ---- selection and hover tints
# Each tint keeps the chapter's hue (OKLCH) and is solved for a fixed contrast against the page background,
# so the selected item and the hover look equally strong in every chapter and theme.
def srgb_to_lin(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def lin_to_srgb(c): return 12.92*c if c<=0.0031308 else 1.055*c**(1/2.4)-0.055
def hex2rgb(h): return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def rgb2hex(c): return '#%02x%02x%02x'%tuple(round(min(1,max(0,v))*255) for v in c)
def rgb2oklch(c):
    r,g,b=[srgb_to_lin(v) for v in c]
    l=0.4122214708*r+0.5363325363*g+0.0514459929*b; m=0.2119034982*r+0.6806995451*g+0.1073969566*b; s=0.0883024619*r+0.2817188376*g+0.6299787005*b
    l,m,s=[x**(1/3) for x in (l,m,s)]
    L=0.2104542553*l+0.7936177850*m-0.0040720468*s; A=1.9779984951*l-2.4285922050*m+0.4505937099*s; B=0.0259040371*l+0.7827717662*m-0.8086757660*s
    return L,math.hypot(A,B),math.atan2(B,A)
def oklch2rgb(L,C,h):
    A,B=C*math.cos(h),C*math.sin(h)
    l=(L+0.3963377774*A+0.2158037573*B)**3; m=(L-0.1055613458*A-0.0638541728*B)**3; s=(L-0.0894841775*A-1.2914855480*B)**3
    r=4.0767416621*l-3.3077115913*m+0.2309699292*s; g=-1.2684380046*l+2.6097574011*m-0.3413193965*s; b=-0.0041960863*l-0.7034186147*m+1.7076147010*s
    return [lin_to_srgb(v) for v in (r,g,b)]
def lum(c): return sum(w*srgb_to_lin(v) for v,w in zip(c,(.2126,.7152,.0722)))
def cr(a,b): x,y=lum(a),lum(b); return (max(x,y)+.05)/(min(x,y)+.05)
def ingamut(c): return all(-1e-4<=v<=1+1e-4 for v in c)
def tint(accent,bg,target,chroma):
    """Accent hue at the lightness that gives `target` contrast against bg (darker on light bg, lighter on dark bg)."""
    _,C0,h=rgb2oklch(hex2rgb(accent)); C=min(C0,chroma); bgc=hex2rgb(bg); light=lum(bgc)>.5
    lo,hi=(0.3,1.0) if light else (0.0,0.7)
    for _ in range(60):
        L=(lo+hi)/2; c=C
        rgb=oklch2rgb(L,c,h)
        while not ingamut(rgb) and c>0: c-=0.002; rgb=oklch2rgb(L,c,h)
        k=cr(rgb,bgc)
        if light: (lo,hi)=(lo,L) if k<target else (L,hi)
        else: (lo,hi)=(L,hi) if k<target else (lo,L)
    return rgb2hex(rgb)

TINT_TARGETS = {  # (background, contrast, max chroma)
    "sel-l": ("#ffffff", 1.30, .09), "hov-l": ("#ffffff", 1.15, .07),
    "sel-d": ("#191919", 1.45, .07), "hov-d": ("#191919", 1.20, .05),
    # one step denser than selected, same hue: the chevron's block while it is pointed at, focused or pressed
    "live-l": ("#ffffff", 1.45, .11), "live-d": ("#191919", 1.70, .09),
    # one more step: the edge of the chevron's box while its fill is the step above
    "deep-l": ("#ffffff", 1.60, .13), "deep-d": ("#191919", 1.95, .11),
}
# Chapter 5: yellow darkened to the common target turns olive, so it keeps a lighter, purer lemon
# (selected 1.20 instead of 1.30, hover 1.10 instead of 1.15; light theme only).
TINT_OVERRIDES = {5: {"sel-l": ("#ffffff", 1.20, .16), "hov-l": ("#ffffff", 1.10, .12), "live-l": ("#ffffff", 1.30, .20), "deep-l": ("#ffffff", 1.40, .24)}}
TINTS = {n: {k: tint(v[4], *TINT_OVERRIDES.get(n, {}).get(k, t)) for k, t in TINT_TARGETS.items()}
         for n, v in PALETTE.items()}

# Landing-cue ring (reduced motion): the chapter accent, mixed with black in OKLab by the smallest whole
# percentage that gives 3:1 against the page background; None if no step does (the ring then uses --link).
def cue_mix(accent, bg):
    L,C,h=rgb2oklch(hex2rgb(accent)); bgc=hex2rgb(bg)
    return next((p for p in range(101) if cr(oklch2rgb(L*(1-p/100),C*(1-p/100),h),bgc)>=3), None)
CUE_MIX = {v[4]: [cue_mix(v[4], "#ffffff"), cue_mix(v[4], "#191919")] for v in PALETTE.values()}  # accent: [light %, dark %]


def chapter_vars(n):
    d, m, o, l, a, b = PALETTE[n]
    t = TINTS[n]
    return (f"--ch-dark:{d};--ch-mid:{m};--ch-mid-op:{o};--ch-light:{l};--ch-accent:{a};"
            f"--ch-sel-l:{t['sel-l']};--ch-hov-l:{t['hov-l']};--ch-sel-d:{t['sel-d']};--ch-hov-d:{t['hov-d']};"
            f"--ch-live-l:{t['live-l']};--ch-live-d:{t['live-d']};--ch-deep-l:{t['deep-l']};--ch-deep-d:{t['deep-d']};")


# Restores the menu before first paint: saved open/closed state, current chapter open, saved scroll position.
NAV_RESTORE = ("(function(){var st={},y=null,sb=document.getElementById('sidebar');"
               "function set(d,v){d.querySelector('.chev').setAttribute('aria-expanded',v);var p=d.querySelector('.nav-ch-c');"
               "if(v)p.removeAttribute('hidden');else p.setAttribute('hidden','until-found')}"
               "try{st=JSON.parse(localStorage.getItem('bb-nav')||'{}');y=sessionStorage.getItem('bb-nav-y')}catch(e){}"
               "[].forEach.call(sb.querySelectorAll('.nav-ch'),function(d){var k=d.dataset.ch;"
               "if(d.hasAttribute('data-here')){set(d,true);st[k]=true}else if(k in st)set(d,!!st[k]);});"
               "try{localStorage.setItem('bb-nav',JSON.stringify(st))}catch(e){}"
               "if(y!==null){sb.scrollTop=+y}else{var c=sb.querySelector('[aria-current]');"
               "if(c&&c.offsetTop>sb.clientHeight-40)sb.scrollTop=c.offsetTop-sb.clientHeight/2;}})();")


def norm_base(path):
    """The site's base path with one leading and one trailing slash: "" and "/" give "/", "book" gives "/book/"."""
    path = path.strip().strip("/")
    return f"/{path}/" if path else "/"


def layout(title, body, chapters, current_file="", current_ch=None, toc="", desc="", cover_html="", base_href=None, noindex=False, nav_sec=""):
    # Pages link to each other relatively and need no <base>. base_href is for a page served at any URL depth.
    base_tag = f'<base href="{esc(base_href)}">\n' if base_href else ""
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    # nav_sec: the page's "On this page" items, repeated under the current menu item where that list is hidden (style.css, .nav-sec)
    # a chapter page's go under the chapter row, outside the list the chevron folds; the home page's under "Contents"
    sec = f'<ol class="nav-sec">{nav_sec}</ol>' if nav_sec else ""
    nav = []
    for c in chapters:
        here = c["n"] == current_ch  # this page belongs to the chapter
        items = "".join(
            (f'<li><span class="nav-cur" aria-current="page"><span class="num">{s["code"]}</span>{esc(s["name"])}</span>{sec}</li>'
             if s["file"] == current_file else
             f'<li><a href="{s["file"]}"><span class="num">{s["code"]}</span>{esc(s["name"])}</a></li>')
            for s in c["subs"])
        label = f'<span class="nav-ch-n">{c["n"]}.</span><span class="nav-ch-l">{esc(c["title"])}</span>'
        # the toggle is a button of its own, next to the title: no control sits inside another
        # open/closed lives in two attributes: aria-expanded on the button, hidden on the list (app.js, navSet)
        chev = (f'<button class="chev" type="button" aria-expanded="{"true" if here else "false"}" '
                f'aria-controls="nav-ch-{c["n"]}" aria-label="Chapter {c["n"]} subcategories"></button>')
        if here:  # row toggles the list; never links to the current chapter
            cur = ' aria-current="page"' if c["file"] == current_file else ""
            head = f'<div class="nav-ch-h"><span class="nav-ch-t"{cur}>{label}</span>{chev}</div>'
        else:     # title opens the chapter page (the chapter is expanded there); the chevron toggles the list
            head = f'<div class="nav-ch-h"><a class="nav-ch-t" href="{c["file"]}">{label}</a>{chev}</div>'
        closed = "" if here else ' hidden="until-found"'  # until-found: find-in-page still reaches a closed list
        nav.append(
            f'<div class="nav-ch" data-ch="{c["n"]}"{" data-here" if here else ""} style="{chapter_vars(c["n"])}">'
            f'{head}{sec if c["file"] == current_file else ""}<div class="nav-ch-c" id="nav-ch-{c["n"]}"{closed}><ul>{items}</ul></div></div>')
    toc_style = f' style="{chapter_vars(current_ch)}"' if current_ch else ""
    toc_html = f'<aside class="toc"{toc_style} aria-label="On this page"><p class="toc-h">On this page</p>{toc}</aside>' if toc else ""
    return f"""<!doctype html>
<html lang="en" class="preload">
<head>
<meta charset="utf-8">
{base_tag}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc or BOOK_SUBTITLE)}">
{robots}<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css">
<link rel="expect" href="#page-ready" blocking="render">
<script>document.documentElement.classList.add('cvc');try{{var t=localStorage.getItem('bb-theme');if(t)document.documentElement.dataset.theme=t;if(localStorage.getItem('bb-side')==='hidden')document.documentElement.classList.add('side-hidden');}}catch(e){{}}</script>
</head>
<body class="has-toc">
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="top-in">
  <button class="menu-btn" aria-label="Hide panel" aria-expanded="true" aria-controls="sidebar"><svg class="ic-panel" viewBox="0 0 20 20" aria-hidden="true"><rect x="2.75" y="3.75" width="14.5" height="12.5" rx="2.5"/><rect class="col" x="4.75" y="5.75" width="4" height="8.5" rx="1"/></svg><svg class="ic-burger" viewBox="0 0 20 20" aria-hidden="true"><path class="l1" d="M3.5 6h13"/><path class="l2" d="M3.5 10h13"/><path class="l3" d="M3.5 14h13"/></svg></button>
  <a class="brand" href="index.html"><span class="brand-t">{BOOK_TITLE}</span></a>
  <a class="brand-m" href="index.html" aria-label="Contents">{HM_MARK.format(stroke="currentColor")}</a>
  <div class="search">
    <label class="sr" for="q">Search directives</label>
    <span class="search-ic">{ICON_SEARCH}</span>
    <input id="q" type="search" placeholder="Search directives…" autocomplete="off" spellcheck="false" autocapitalize="off" autocorrect="off" role="combobox" aria-autocomplete="list" aria-controls="results" aria-expanded="false">
    <kbd>/</kbd>
    <button type="button" class="search-x" tabindex="-1" aria-label="Clear search">×</button>
    <ol id="results" class="results" role="listbox" hidden></ol>
    <div id="q-status" class="sr" role="status" aria-live="polite"></div>
  </div>
  <button class="theme-btn" aria-label="Switch to dark theme"><span class="sun">☀︎</span><span class="moon">☾</span></button>
</div></header>
{cover_html}
<div class="shell">
  <nav id="sidebar" class="sidebar" aria-label="Chapters">
    <div class="nav-head">{'<span class="nav-home is-cur" aria-current="page">Contents</span>' if current_file == 'index.html' else '<a class="nav-home" href="index.html">Contents</a>'}<button class="nav-toggle" type="button" data-state="collapse"><span class="l-c">Collapse all</span><span class="l-e">Expand all</span></button></div>
    {sec if current_file == 'index.html' else ''}{''.join(nav)}
  </nav>
  <script>{NAV_RESTORE}</script>
  <main id="main" class="main">
{body}
  </main>
  <span id="page-ready" hidden></span>
  {toc_html}
</div>
<div class="scrim" hidden></div>
<script src="assets/search-index.js"></script>
<script src="assets/app.js"></script>
</body>
</html>
"""


GO = '<span class="go" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'
CHEV_L = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'


def cover_arrows(nav):
    """Prev/next arrows at the banner's edges, in reading order. nav = (prev, next), each (label, href, …) or None."""
    prev, nxt = nav
    out = ""
    if prev:
        out += f'<a class="cv-arr cv-prev" href="{prev[1]}" aria-label="Previous: {esc(prev[0])}">{CHEV_L}</a>'
    if nxt:
        out += f'<a class="cv-arr cv-next" href="{nxt[1]}" aria-label="Next: {esc(nxt[0])}">{CHEV_R}</a>'
    return out


def crumb_nav(ch, prev, nxt):
    """Prev/next pair at the right end of the breadcrumbs (same steps as the banner arrows and the pager)."""
    def btn(p, cls, svg, word):
        if not p:
            return f'<span class="cn {cls} is-off" aria-hidden="true">{svg}</span>'
        return f'<a class="cn {cls}" href="{p[1]}" aria-label="{word}: {esc(p[0])}">{svg}</a>'
    return (f'<nav class="cnav" aria-label="Previous and next page" style="{chapter_vars(ch["n"])}">'
            + btn(prev, "cn-prev", CHEV_L, "Previous") + btn(nxt, "cn-next", CHEV_R, "Next") + '</nav>')


def cover(ch, s=None, nav=(None, None)):
    """Banner in the chapter palette."""
    if not s:
        return (f'<div class="cover cover-css cover-ch" style="{chapter_vars(ch["n"])}"><div class="cover-in">'
                f'<span class="cv-1"><span class="cv-n">{ch["n"]}.</span> {esc(ch["title"])}</span>{cover_arrows(nav)}</div></div>')
    return (f'<div class="cover cover-css" style="{chapter_vars(ch["n"])}"><div class="cover-in">'
            f'<span class="cv-1"><span class="cv-n">{ch["n"]}.</span> {esc(ch["title"])}</span>'
            f'<h1 class="cv-2"><span class="cv-n"><span class="cv-c" aria-hidden="true">{ch["n"]}.</span>{s["num"]}<span class="cv-d">.</span></span> {esc(s["name"])}</h1>{cover_arrows(nav)}</div></div>')


# Emoji sit inside the colored blocks (left column), not in the section headings.
CALL_EMOJI = {"mission": "🫡", "heuristics": "🚀", "brief": "☝️", "core": "🤔", "summary": "⚡", "indicators": "😎", "oneline": "☝️"}
HEAD_EMOJI = {"directives": "🧬"}  # the only section heading that keeps its emoji


def call(key, cls, inner):
    em = CALL_EMOJI.get(key)
    if not em:
        return f'<div class="call {cls}">{inner}</div>'
    return (f'<div class="call {cls} has-em"><span class="call-em" aria-hidden="true">{em}</span>'
            f'<div class="call-body">{inner}</div></div>')


def sec_head(key, name):
    _, emoji, title, arrow = next(x for x in SECTIONS if x[0] == key)
    tail = f' <span class="arrow" aria-hidden="true">→</span> <span class="to">{esc(name)}</span>' if arrow else ""
    em = f'<span class="em" aria-hidden="true">{HEAD_EMOJI[key]}</span> ' if key in HEAD_EMOJI else ""
    return f'<h2 id="{key}">{em}{title}{tail}</h2>'


def render_sub(ch, s, prev, nxt, chapters):
    name = s["name"]
    cv = cover(ch, s, (prev, nxt))
    out = [f'<div class="page-head"><div class="crumbs-row"><p class="crumbs"><a href="index.html">Contents</a> <span class="sep" aria-hidden="true">❯</span> '
           f'<a href="{ch["file"]}">{ch["n"]}. {esc(ch["title"])}</a> <span class="sep" aria-hidden="true">❯</span> <span class="crumb-cur" aria-current="page">{s["num"]}. {esc(name)}</span></p>'
           f'{crumb_nav(ch, prev, nxt)}</div><p class="lede">{inline(s["governs"])}</p></div>']
    out.append(f'<section>{sec_head("ask", name)}<blockquote class="q">{inline(s["ask"])}</blockquote></section>')
    out.append(f'<section>{sec_head("mission", name)}{call("mission", "c-peach", inline(s["mission"]))}</section>')
    out.append(f'<section>{sec_head("heuristics", name)}'
               + call("heuristics", "c-blue", "<ol>" + "".join(f"<li>{inline(x)}</li>" for x in s["heuristics"]) + "</ol>") + "</section>")
    out.append(f'<section>{sec_head("brief", name)}{call("brief", "c-peach", inline(s["brief"]))}</section>')
    out.append(f'<section>{sec_head("core", name)}'
               + call("core", "c-pink lines", "".join(f"<p>{inline(x)}</p>" for x in s["core"])) + "</section>")
    fa = "".join(f'<h3 class="fa">{inline(lbl)}</h3><blockquote class="q">'
                 + "".join(f"<p>{inline(q)}</p>" for q in qs) + "</blockquote>" for lbl, qs in s["focus"])
    out.append(f'<section>{sec_head("focus", name)}{fa}</section>')
    cards = []
    for d in s["directives"]:
        anchor = d["id"].replace("/", "-")
        if d["repealed"]:
            tid, ttitle = d["repealed"]
            target = DIR_INDEX.get(tid)
            href = f'{target}#{tid.replace("/", "-")}' if target else "#"
            cards.append(
                f'<article class="dir repealed" id="{anchor}"><p class="dir-meta">'
                f'<a class="chip" href="#{anchor}">Directive<span class="bul" aria-hidden="true"></span>{d["id"]}</a>'
                f'<span class="chip rep">Repealed</span></p>'
                f'<p class="dir-body">Merged into <a href="{href}"><span class="mono">{tid}</span>—{inline(ttitle)}</a></p></article>')
        else:
            cards.append(
                f'<article class="dir" id="{anchor}"><p class="dir-meta">'
                f'<a class="chip" href="#{anchor}">Directive<span class="bul" aria-hidden="true"></span>{d["id"]}</a></p>'
                f'<h3 class="dir-title">{inline(d["title"])}</h3><p class="dir-body">{inline(d["body"])}</p></article>')
    out.append(f'<section style="{chapter_vars(ch["n"])}"><span class="dh-mark" aria-hidden="true"></span>{sec_head("directives", name)}<div class="dirs">{"".join(cards)}</div></section>')
    out.append(f'<section>{sec_head("summary", name)}'
               + call("summary", "c-yellow", "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in s["summary"]) + "</ul>") + "</section>")
    out.append(f'<section>{sec_head("indicators", name)}'
               + call("indicators", "c-green", "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in s["indicators"]) + "</ul>") + "</section>")
    out.append(f'<section>{sec_head("oneline", name)}{call("oneline", "c-peach", inline(s["oneline"]))}</section>')
    out.append(pager(prev, nxt))
    items = "".join(f'<li><a href="#{k}">{t}</a></li>' for k, _, t, _ in SECTIONS)
    title = f'{s["code"]} {name}—{BOOK_TITLE}'
    return layout(title, "\n".join(out), chapters, s["file"], ch["n"], f"<ol>{items}</ol>", s["governs"], cv, nav_sec=items)


def pager(prev, nxt):
    def link(p, cls, arrow_left):
        if not p:
            return f'<span class="{cls} empty"></span>'
        lbl, href, n = p
        d = ('<span class="pg-dir"><span class="pg-ar">←</span> Previous</span>' if arrow_left
             else '<span class="pg-dir">Next <span class="pg-ar">→</span></span>')
        inner = d + f'<span class="pg-t">{esc(lbl)}</span>'
        return f'<a class="{cls}" href="{href}" style="{chapter_vars(n)}">{inner}</a>'
    return f'<nav class="pager" aria-label="Pages">{link(prev, "pg prev", True)}{link(nxt, "pg next", False)}</nav>'


def render_chapter(ch, prev, nxt, chapters):
    tiles = "".join(
        f'<a class="tile" href="{s["file"]}"><span class="card-n">{s["num"]}.</span><span class="tile-t">{esc(s["name"])}</span>'
        f'<span class="tile-gov">{inline(s["governs"])}</span>'
        f'<span class="tile-ask">{inline(s["ask"])}</span>'
        f'<span class="card-foot"><span class="tile-count">{len([d for d in s["directives"] if not d["repealed"]])} directives</span>{GO}</span></a>'
        for s in ch["subs"])
    # the intro's first line is the page h1, styled like a subcategory's "Governs" line (p.lede; that page's h1 is the banner name)
    intro = "".join(f"<h1>{inline(x)}</h1>" if i == 0 else f"<p>{inline(x)}</p>" for i, x in enumerate(ch["intro"]))
    cv = cover(ch, None, (prev, nxt))
    body = (f'<div class="page-head"><div class="crumbs-row"><p class="crumbs"><a href="index.html">Contents</a> <span class="sep" aria-hidden="true">❯</span> <span class="crumb-cur" aria-current="page">{ch["n"]}. {esc(ch["title"])}</span></p>'
            f'{crumb_nav(ch, prev, nxt)}</div>'
            f'{intro}</div>'
            f'<section><h2 id="mission">Mission statement</h2>{call("mission", "c-peach", inline(ch["mission"]))}</section>'
            f'<section><h2 id="subcategories">Subcategories</h2><div class="tiles" style="{chapter_vars(ch["n"])}">{tiles}</div></section>'
            + pager(prev, nxt))
    items = '<li><a href="#mission">Mission statement</a></li><li><a href="#subcategories">Subcategories</a></li>'
    return layout(f'{ch["n"]}. {ch["title"]}—{BOOK_TITLE}', body, chapters, ch["file"], ch["n"], f"<ol>{items}</ol>", ch["mission"], cv, nav_sec=items)


# The book's emblem: on the Contents banner and, on phones, the header's home link.
HM_MARK = ('<svg class="hm-mark" viewBox="676 37 98 98" aria-hidden="true" fill="none" stroke="{stroke}">'
           '<rect x="685" y="54" width="80" height="80"/><circle cx="725" cy="86" r="48"/>'
           '<path d="M723,132l-4-49-30-24v-1l36,16,36-16v1l-30,24-4,49h-4Z"/><path d="M720,63l5-5,5,5-5,6-5-6Z"/></svg>')

# Contents banner, after the author's Notion cover (11-01__Hero__Cover.svg): emblem and two lines on #1829c4.
HOME_COVER = ('<div class="cover cover-home"><div class="cover-in"><div class="hm" role="img" aria-label="Human-Centered Systems Engineering">'
              + HM_MARK.format(stroke="#fff") +
              '<span class="hm-t">Human-Centered Systems Engineering</span></div>{arrows}</div></div>')


def render_home(chapters, front):
    total = sum(1 for c in chapters for s in c["subs"] for d in s["directives"])
    active = sum(1 for c in chapters for s in c["subs"] for d in s["directives"] if not d["repealed"])
    subs = sum(len(c["subs"]) for c in chapters)
    grid = "".join(
        f'<a class="ch-card" href="{c["file"]}" style="{chapter_vars(c["n"])}">'
        f'<span class="card-n">{c["n"]}.</span><span class="ch-card-t">{esc(c["title"])}</span>'
        f'<span class="ch-card-d">{inline(c["intro"][0]) if c["intro"] else ""}</span>'
        f'<span class="card-foot"><span class="ch-card-c">{len(c["subs"])} subcategories</span>{GO}</span></a>' for c in chapters)
    sections = "".join(f'<section class="prose">{md_blocks("## " + n + chr(10) + b)}</section>' for n, b in front)
    items = '<li><a href="#chapters">Chapters</a></li>' + "".join(f'<li><a href="#{slug(n)}">{n}</a></li>' for n, _ in front)
    cv = HOME_COVER.format(arrows=cover_arrows((None, (f'1. {chapters[0]["title"]}', chapters[0]["file"]))))
    body = (f'<div class="hero"><p class="hero-k">{AUTHOR}</p><h1>{BOOK_TITLE}</h1><p class="hero-s">{BOOK_SUBTITLE}</p>'
            f'<p class="hero-stats"><span><b>9</b> chapters</span><span><b>{subs}</b> subcategories</span>'
            f'<span><b>{active}</b> directives</span><span class="muted">{total - active} repealed IDs</span></p></div>'
            f'<section><h2 id="chapters">Chapters</h2><div class="ch-grid">{grid}</div></section>' + sections)
    return layout(BOOK_TITLE, body, chapters, "index.html", None, f"<ol>{items}</ol>", cover_html=cv, nav_sec=items)


# Under <base>, "#main" would resolve to the home page, so the skip link moves focus itself.
SKIP_FIX = ("<script>document.querySelector('.skip').addEventListener('click',function(e){e.preventDefault();"
            "var m=document.getElementById('main');m.setAttribute('tabindex','-1');m.focus()})</script>")


def render_404(chapters):
    """The page the host serves for any unknown URL, at any depth: every link resolves against <base href>."""
    # the quote is the book's own pattern: a markdown blockquote inside .prose, as on the Contents page
    quote = md_blocks("> “Some things are better not seen, and some things are better lost than found.” \U0001F609\n"
                      ">\n> **Stephen King,** The Dead Zone (1979)")
    body = ('<div class="page-head"><h1>Page not found</h1>'
            '<p>No page of the book lives at this address.</p>'
            f'<div class="prose">{quote}</div>'
            '<p><a href="index.html">Go to Contents</a></p></div>' + SKIP_FIX)
    return layout(f"Page not found—{BOOK_TITLE}", body, chapters, "404.html",
                  cover_html=HOME_COVER.format(arrows=""), base_href=BASE, noindex=True)


# ---------------------------------------------------------------- build
DIR_INDEX = {}
BASE = "/"  # URL path the site is served from; set by --base


def main(base="/", out=None):
    global BASE
    BASE = norm_base(base)
    HERE = Path(out).expanduser().resolve() if out else SITE
    ASSETS = HERE / "assets"
    # an existing folder is taken for an earlier build only by its index.html; anything else is left alone
    if HERE.exists() and not HERE.is_dir():
        sys.exit(f"Error: {HERE} is not a folder. Nothing was written.")
    if HERE.is_dir() and any(HERE.iterdir()) and not (HERE / "index.html").is_file():
        sys.exit(f"Error: {HERE} is not empty and has no index.html, so it is not an earlier build of this site. "
                 "Nothing was written. Give --out an empty or new folder.")
    HERE.mkdir(parents=True, exist_ok=True)
    chapters = [parse_chapter(REF / f"chapter_{i}.md") for i in range(1, 10)]
    for c in chapters:
        for s in c["subs"]:
            for d in s["directives"]:
                DIR_INDEX[d["id"]] = s["file"]
    front = parse_index()
    seq = []
    for c in chapters:
        seq.append(("ch", c))
        seq.extend(("sub", c, s) for s in c["subs"])

    def label(item):
        if item[0] == "ch":
            return (f'{item[1]["n"]}. {item[1]["title"]}', item[1]["file"], item[1]["n"])
        return (f'{item[2]["code"]} {item[2]["name"]}', item[2]["file"], item[1]["n"])

    expected = {"index.html", "404.html"} | {c["file"] for c in chapters} | {s["file"] for c in chapters for s in c["subs"]}
    for f in HERE.glob("*.html"):
        if f.name not in expected:  # remove pages whose subcategory was renamed or removed
            try:
                f.unlink()
            except OSError as e:
                print(f"Warning: could not remove stale page {f.name}: {e}")
    (HERE / "index.html").write_text(render_home(chapters, front), encoding="utf-8")
    for i, item in enumerate(seq):
        prev = label(seq[i - 1]) if i > 0 else ("Contents", "index.html", item[1]["n"])
        nxt = label(seq[i + 1]) if i + 1 < len(seq) else None
        if item[0] == "ch":
            html_ = render_chapter(item[1], prev, nxt, chapters)
            (HERE / item[1]["file"]).write_text(html_, encoding="utf-8")
        else:
            html_ = render_sub(item[1], item[2], prev, nxt, chapters)
            (HERE / item[2]["file"]).write_text(html_, encoding="utf-8")

    (HERE / "404.html").write_text(render_404(chapters), encoding="utf-8")  # not counted as a page of the book

    idx = []
    for c in chapters:
        for s in c["subs"]:
            idx.append({"t": "s", "c": c["n"], "id": s["code"], "title": s["name"], "body": s["governs"], "url": s["file"]})
            for d in s["directives"]:
                body = d["body"] if not d["repealed"] else "Repealed—merged into " + d["repealed"][0]
                title = d["title"] if not d["repealed"] else "Repealed"
                idx.append({"t": "d", "c": c["n"], "id": d["id"], "title": title, "body": body,
                            "url": s["file"] + "#" + d["id"].replace("/", "-"), "sub": s["code"] + " " + s["name"]})
    ASSETS.mkdir(exist_ok=True)
    if HERE != SITE.resolve():  # the favicons are kept by hand in site/assets/; any other folder gets copies
        for name in FAVICONS:
            shutil.copyfile(SITE / "assets" / name, ASSETS / name)
    # the search vocabulary (spelling, phrases, synonyms) is data: tools/search_vocab.json
    vocab = json.loads((ROOT / "tools" / "search_vocab.json").read_text(encoding="utf-8"))
    (ASSETS / "search-index.js").write_text(
        "window.BB_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";\n"
        + "window.BB_CHAPTERS=" + json.dumps({c["n"]: c["title"] for c in chapters}, ensure_ascii=False, separators=(",", ":")) + ";\n"
        + "window.BB_VOCAB=" + json.dumps(vocab, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    # search results carry their chapter's tints (class rc1…rc9)
    rc = "".join(f".rc{n}{{--ch-sel-l:{t['sel-l']};--ch-hov-l:{t['hov-l']};--ch-sel-d:{t['sel-d']};--ch-hov-d:{t['hov-d']}}}" for n, t in TINTS.items())
    (ASSETS / "style.css").write_text(CSS + "/* search result tints */\n" + rc + "\n", encoding="utf-8")
    (ASSETS / "app.js").write_text(JS.replace("__CUE_MIX__", json.dumps(CUE_MIX, separators=(",", ":"))), encoding="utf-8")
    n_dirs = sum(1 for x in idx if x["t"] == "d")
    print(f"Built {1 + len(seq)} pages: 1 home, {len(chapters)} chapters, {len(seq) - len(chapters)} subcategories; {n_dirs} directive IDs indexed.")


CSS = r"""
:root{
  --bg:#ffffff;--bg-soft:#f7f6f3;--text:#37352f;--muted:var(--text);--line:#e9e9e7;--link:#1929c4;
  --peach:#fbecdd;--blue:#e7f3f8;--pink:#f9e8ef;--yellow:#fbf3db;--green:#e8f1ec;--gray:#f1f1ef;--quote:#d44c47;
  --chip:#e9e5f2;--chip-t:#4b3c63;--shadow:0 1px 2px rgba(15,15,15,.06);--marker:#38222c;--arrow:#b83d80;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  --spring:ease-out;--soft:ease-out;
  --top:56px;--cover-h:125px;--side:280px;--toc:220px;--measure:760px;--shell:1340px;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#191919;--bg-soft:#202020;--text:#e6e6e4;--muted:var(--text);--line:#2f2f2f;--link:#7fb8e6;
  --peach:#3a2a1f;--blue:#1c2c37;--pink:#38222c;--yellow:#3a321d;--green:#1f2f27;--gray:#252525;--quote:#e06c66;
  --chip:#2f2a3a;--chip-t:#d6cdea;--shadow:none;--marker:#f3cfdc;--arrow:#f08cc0;color-scheme:dark;}}
:root[data-theme="dark"]{
  --bg:#191919;--bg-soft:#202020;--text:#e6e6e4;--muted:var(--text);--line:#2f2f2f;--link:#7fb8e6;
  --peach:#3a2a1f;--blue:#1c2c37;--pink:#38222c;--yellow:#3a321d;--green:#1f2f27;--gray:#252525;--quote:#e06c66;
  --chip:#2f2a3a;--chip-t:#d6cdea;--shadow:none;--marker:#f3cfdc;--arrow:#f08cc0;color-scheme:dark;}
@supports (transition-timing-function:linear(0, 1)){:root{
  --spring:linear(0, 0.042, 0.145, 0.282, 0.432, 0.579, 0.712, 0.825, 0.916, 0.985, 1.033, 1.063, 1.079, 1.084, 1.08, 1.072, 1.06, 1.048, 1.035, 1.024, 1.015, 1.007, 1.001, 0.997, 0.995, 0.993, 0.993, 0.993, 0.994, 0.995, 0.996, 0.997, 1);  /* damped spring, ~8% overshoot */
  --soft:linear(0, 0.029, 0.099, 0.189, 0.285, 0.381, 0.471, 0.552, 0.624, 0.687, 0.741, 0.787, 0.825, 0.857, 0.884, 0.906, 0.924, 0.939, 0.951, 0.96, 0.968, 0.975, 0.98, 0.984, 0.987, 0.99, 0.992, 0.994, 0.995, 0.996, 0.997, 0.997, 1);}}  /* critically damped spring, no overshoot */
*{box-sizing:border-box;--ch-sel:var(--ch-sel-l);--ch-hov:var(--ch-hov-l);--ch-live:var(--ch-live-l);--ch-deep:var(--ch-deep-l)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) *{--ch-sel:var(--ch-sel-d);--ch-hov:var(--ch-hov-d);--ch-live:var(--ch-live-d);--ch-deep:var(--ch-deep-d)}}
:root[data-theme="dark"] *{--ch-sel:var(--ch-sel-d);--ch-hov:var(--ch-hov-d);--ch-live:var(--ch-live-d);--ch-deep:var(--ch-deep-d)}
@media (prefers-reduced-motion:no-preference){html.smooth{scroll-behavior:smooth}@view-transition{navigation:auto}}
.top{view-transition-name:top}.sidebar{view-transition-name:sidebar}
body>.cover{view-transition-name:cover}.cover .cv-1{view-transition-name:cv-ch}.cover .cv-2{view-transition-name:cv-sub}
/* page content: the old page leaves quickly, the new one fades in; chrome and banner stay put */
::view-transition-group(sidebar),::view-transition-new(sidebar){animation:none}::view-transition-old(sidebar){animation:none;opacity:0}
::view-transition-old(root){animation:.12s ease-out both bb-fade-out}
::view-transition-new(root){animation:.22s ease-out .06s both bb-fade-in}
@keyframes bb-fade-out{to{opacity:0}}@keyframes bb-fade-in{from{opacity:0}}
/* banner: chapter line shrinks upward, subcategory line grows in under it (and the reverse) */
::view-transition-group(cv-ch),::view-transition-group(cv-sub){animation-duration:.55s;animation-timing-function:var(--soft)}
::view-transition-old(cv-ch),::view-transition-new(cv-ch),::view-transition-old(cv-sub),::view-transition-new(cv-sub){animation-duration:.55s;height:100%}
::view-transition-new(cv-sub):only-child{animation:.55s var(--spring) both bb-sub-in}
::view-transition-old(cv-sub):only-child{animation:.3s ease-out both bb-sub-out}
@keyframes bb-sub-in{from{opacity:0;transform:translateY(60%) scale(.55)}}
@keyframes bb-sub-out{to{opacity:0;transform:translateY(60%) scale(.55)}}
.preload *{transition:none!important}
/* anchors clear the sticky header and banner; set on targets (not as scroll-padding) so typing in the header search never scrolls the page */
[id]{scroll-margin-top:calc(var(--top) + var(--cover-h,0px) + 16px)}
.search input{scroll-margin:0}
body{margin:0;background:var(--bg);color:var(--text);font:500 16px/1.6 var(--sans);-webkit-font-smoothing:antialiased}
a{color:var(--link);text-decoration:none}
/* every hover look sits in @media (hover:hover): on touch it would stay on the element last tapped */
@media (hover:hover){a:hover{text-decoration:underline}}
.mono,code,kbd{font-family:var(--mono)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.skip{position:absolute;left:-999px;top:8px;background:var(--text);color:var(--bg);padding:8px 12px;border-radius:6px;z-index:100}.skip:focus{left:8px}
:focus-visible{outline:2px solid var(--link);outline-offset:2px;border-radius:4px}
/* targets that only scripts focus (a heading after an in-page link, main after the skip link) are not controls: no ring */
[tabindex="-1"]:focus{outline:none}

/* top bar */
.top{position:sticky;top:0;z-index:30;height:var(--top);background:var(--bg);border-bottom:1px solid var(--line)}
/* header content sits on the same 1440px grid as the page: menu button over the sidebar, theme button over the toc */
.top-in{height:100%;max-width:var(--shell);margin:0 auto;display:flex;align-items:center;gap:16px;padding:0 20px}
.brand{color:var(--text);font-weight:650;letter-spacing:-.01em;white-space:nowrap}@media (hover:hover){.brand:hover{text-decoration:none}}
.brand-m{display:none;flex:none;place-items:center;width:36px;height:36px;border-radius:8px;color:var(--text)}.brand-m .hm-mark{width:24px}
.search{position:relative;margin-left:auto;width:min(420px,45vw)}
.search input{width:100%;height:36px;border:1px solid var(--line);background:var(--bg-soft);color:var(--text);border-radius:8px;padding:0 36px 0 34px;font:inherit;font-size:14px}
.search input::-webkit-search-cancel-button{display:none}
.search input:focus,.search input:focus-visible{outline:none;border-color:color-mix(in srgb,var(--text) 35%,var(--bg));box-shadow:0 0 0 3px color-mix(in srgb,var(--text) 10%,transparent)}
.search input::placeholder{color:var(--ph,#6b6b6b);opacity:1}  /* the one grey text on the site */
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .search input{--ph:#9b9b99}}:root[data-theme="dark"] .search input{--ph:#9b9b99}
.search-ic{position:absolute;left:10px;top:9px;width:18px;height:18px;color:var(--muted);pointer-events:none}
.search-ic.pop{animation:bb-pop .55s var(--spring)}
@keyframes bb-pop{35%{transform:scale(1.3)}}
/* "/" focuses search from anywhere; the hint is plain text and hides while typing */
.search kbd{position:absolute;right:12px;top:8px;font-size:13px;color:var(--ph,#6b6b6b);line-height:20px;pointer-events:none;transition:opacity .2s var(--soft)}
.search:focus-within kbd,.search.has-val kbd{opacity:0}
/* clear button in the "/" slot, only while the field has text; the look is .r-x, the hit area is the field height */
.search-x{position:absolute;z-index:0;top:0;right:0;width:36px;height:36px;display:none;padding:0;border:0;background:transparent;color:var(--text);font-size:18px;line-height:1;cursor:pointer}
.search.has-val .search-x{display:block}
.search-x::before{content:"";position:absolute;z-index:-1;inset:5px;border-radius:6px}
@media (hover:hover){.search-x:hover::before{background:var(--bg)}}
.results{position:absolute;top:42px;left:0;right:0;max-height:70vh;overflow:auto;overscroll-behavior:contain;margin:0;padding:8px;list-style:none;display:grid;gap:6px;background:var(--bg-soft);border:1px solid var(--line);border-radius:10px;box-shadow:0 12px 32px rgba(0,0,0,.18)}
.results li a{display:block;padding:10px 12px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--text);line-height:1.35}
@media (hover:hover){.results li a:hover{background:var(--ch-hov,var(--bg));border-color:var(--ch-sel,var(--line));text-decoration:none}}
.results li[aria-selected="true"] a{background:var(--ch-hov,var(--bg));border-color:var(--ch-sel,var(--line));text-decoration:none}
.results .r-id{font-family:var(--mono);font-size:12px;color:var(--muted);margin-right:8px}
.results .r-t{font-weight:650}.results .r-b{display:block;margin-top:4px;font-size:13px;color:var(--muted)}
.results mark{background:var(--ch-sel,var(--yellow));color:inherit;border-radius:3px;padding:0 1px}
.results .r-empty{padding:10px;color:var(--muted)}
/* a link inside a sentence row is a text link, not a result card */
.results .r-empty a{display:inline;padding:0;border:0;border-radius:0;background:none;color:var(--link)}
@media (hover:hover){.results .r-empty a:hover{display:inline;padding:0;border:0;border-radius:0;background:none;color:var(--link)}.results .r-empty a:hover{text-decoration:underline}}
/* the suggestion has no chapter tint, so its hover and selection show on the border */
@media (hover:hover){.results .r-fix a:hover{border-color:var(--link)}}
.results .r-fix[aria-selected="true"] a{border-color:var(--link)}
.results[hidden]{display:none}
.results{scrollbar-width:thin;scrollbar-color:transparent transparent;scrollbar-gutter:stable}
.results.is-scrolling{scrollbar-color:color-mix(in srgb,var(--text) 40%,transparent) transparent}
.results::-webkit-scrollbar{width:8px}.results::-webkit-scrollbar-track{background:transparent}.results::-webkit-scrollbar-thumb{background:transparent;border-radius:8px}
.results.is-scrolling::-webkit-scrollbar-thumb{background:color-mix(in srgb,var(--text) 40%,transparent)}
.results li{position:relative}
.results .r-head{display:flex;justify-content:space-between;align-items:center;padding:2px 4px 0;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
.results .r-q{display:block;margin-top:4px;font-size:12px;font-family:var(--mono)}
.results .r-x{position:absolute;top:6px;right:6px;width:26px;height:26px;border:0;border-radius:6px;background:transparent;color:var(--text);font-size:18px;line-height:1;cursor:pointer}
@media (hover:hover){.results .r-x:hover{background:var(--bg-soft)}}
.results .r-hist a{padding-right:38px}
.results .r-clear{font:inherit;font-size:12px;font-weight:600;color:var(--text);background:transparent;border:1px solid var(--line);border-radius:6px;padding:4px 10px;cursor:pointer;justify-self:start}
@media (hover:hover){.results .r-clear:hover{background:var(--bg)}}
.theme-btn,.menu-btn{flex:none;width:36px;height:36px;border:0;background:transparent;color:var(--text);border-radius:8px;cursor:pointer;font-size:16px}
.theme-btn span{display:inline-block}.theme-btn .moon{display:none}
.theme-btn.turn span{animation:bb-turn .6s var(--spring)}
@keyframes bb-turn{from{transform:rotate(-120deg) scale(.5);opacity:0}}
:root[data-theme="dark"] .theme-btn .sun{display:none}:root[data-theme="dark"] .theme-btn .moon{display:inline-block}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .theme-btn .sun{display:none}:root:not([data-theme="light"]) .theme-btn .moon{display:inline-block}}
.menu-btn{display:grid;place-items:center;padding:0}
.menu-btn svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round}
.ic-panel .col{fill:currentColor;stroke:none;transform-box:fill-box;transform-origin:left center;transition:transform .5s var(--spring),opacity .3s var(--soft)}
.ic-burger{display:none}.ic-burger path{transform-box:fill-box;transform-origin:center;transition:transform .5s var(--spring),opacity .2s var(--soft)}
/* shown: filled column; hidden: empty column that slides out on hover as a preview */
.side-hidden .ic-panel .col{transform:scaleX(0);opacity:0}
/* hover previews the click: the column leaves a shown panel's icon and returns to a hidden one's; after a click, not until the pointer has left */
@media (hover:hover){.side-hidden .menu-btn:hover:not(.pv-off) .ic-panel .col{transform:none;opacity:1}
  :root:not(.side-hidden) .menu-btn:hover:not(.pv-off) .ic-panel .col{transform:scaleX(0);opacity:0}}
/* tooltip of an icon-only control: one element, placed by script under the control (above it with .up); the shadow is the results list's */
.tip{position:fixed;left:0;top:0;z-index:60;width:max-content;max-width:min(320px,calc(100vw - 16px));padding:5px 9px;border:1px solid var(--text);border-radius:6px;background:var(--text);color:#fff;
  font-size:12px;font-weight:500;line-height:1.35;text-align:center;box-shadow:0 12px 32px rgba(0,0,0,.18);opacity:0;visibility:hidden;transform:translateY(-4px) scale(.94);
  transition:opacity .15s var(--soft),transform .15s var(--soft),visibility 0s .15s}
.tip.up{transform:translateY(4px) scale(.94)}
/* beside a chapter chevron, so the chevron below stays free: to its right (.at-r), to its left (.at-l) when the right has no room */
.tip.at-r{transform:translateX(-4px) scale(.94)}.tip.at-l{transform:translateX(4px) scale(.94)}
.tip.on{opacity:1;visibility:visible;transform:none;transition:opacity .18s var(--soft),transform .4s var(--spring),visibility 0s}
/* the gap to the control belongs to the tooltip, so the pointer can cross it */
.tip::before{content:"";position:absolute;left:0;right:0;top:-7px;height:7px}.tip.up::before{top:auto;bottom:-7px}
.tip.at-r::before,.tip.at-l::before{top:0;bottom:0;width:7px;height:auto}.tip.at-r::before{left:-7px;right:auto}.tip.at-l::before{left:auto;right:-7px}
:root[data-theme="dark"] .tip{background:#2f2f2f;color:var(--text);border-color:#474747}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .tip{background:#2f2f2f;color:var(--text);border-color:#474747}}

/* shell */
.shell{--side-w:var(--side);display:grid;grid-template-columns:var(--side-w) minmax(0,1fr) var(--toc);max-width:var(--shell);margin:0 auto;overflow-x:clip;transition:grid-template-columns .45s var(--soft)}
.sidebar{width:var(--side);transition:transform .45s var(--soft),opacity .3s var(--soft),visibility 0s}
@media (min-width:861px){.side-hidden .shell{--side-w:0px}.side-hidden .sidebar{transform:translateX(-100%);opacity:0;visibility:hidden;transition:transform .45s var(--soft),opacity .3s var(--soft),visibility 0s .45s}}
.sidebar{position:sticky;top:calc(var(--top) + var(--cover-h));height:calc(100vh - var(--top) - var(--cover-h));overflow:auto;scrollbar-gutter:stable;padding:36px 12px 40px 20px;font-size:14px;scrollbar-width:thin;scrollbar-color:transparent transparent}
.sidebar.is-scrolling{scrollbar-color:color-mix(in srgb,var(--text) 40%,transparent) transparent}
.sidebar::-webkit-scrollbar{width:8px}.sidebar::-webkit-scrollbar-track{background:transparent}
.sidebar::-webkit-scrollbar-thumb{background:transparent;border-radius:8px}
.sidebar.is-scrolling::-webkit-scrollbar-thumb{background:color-mix(in srgb,var(--text) 40%,transparent)}
.nav-head{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:6px}
.nav-home{display:block;flex:1;padding:6px 8px;border-radius:6px;color:var(--text);font-weight:600}
.nav-toggle{flex:none;display:grid;text-align:center;font:inherit;font-size:12px;color:var(--text);background:transparent;border:1px solid var(--line);border-radius:6px;padding:3px 8px;cursor:pointer}
@media (hover:hover){.nav-toggle:hover{background:var(--bg-soft)}}
.nav-toggle>span{grid-area:1/1}
.nav-toggle[data-state="collapse"] .l-e,.nav-toggle[data-state="expand"] .l-c{visibility:hidden}
.nav-toggle,.nav-home,.nav-ch-h,.nav-ch li a{transition:background-color .35s var(--soft)}
.nav-home.is-cur{background:var(--bg-soft);text-decoration:none}
@media (hover:hover){a.nav-home:hover{background:var(--bg-soft);text-decoration:none}}
.nav-home.is-cur{cursor:default}
.nav-ch-h{display:flex;align-items:stretch;cursor:pointer;border-radius:6px;font-weight:600}
.nav-ch-t{flex:1;min-width:0;display:flex;gap:6px;align-items:center;padding:6px 0 6px 8px;color:var(--text);border-radius:6px;line-height:1.3}
.nav-ch-n{flex:none;align-self:flex-start}.nav-ch-l{flex:1;min-width:0}@media (hover:hover){.nav-ch-t:hover{text-decoration:none}}
.nav-ch-h:has(.nav-ch-t[aria-current]){background:var(--ch-sel)}
.nav-ch-t[aria-current]{font-weight:700}
/* the chevron is the toggle: a button, a 34px strip at the row's end, separate from the title link */
.chev{appearance:none;border:0;margin:0;padding:0;background:none;font:inherit;color:inherit;cursor:pointer;flex:none;width:34px;display:grid;place-items:center;border-radius:6px;transition:background-color .35s var(--soft)}
/* the glyph is the text colour, a little lighter at rest; the button's states are its block's background alone */
.chev::before{content:"";width:6px;height:6px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;opacity:.75;transform:translateX(-1px) rotate(-45deg);transition:transform .6s var(--spring),opacity .35s var(--soft)}
.chev[aria-expanded="true"]::before{transform:translateY(-1px) rotate(45deg)}
@media (hover:hover){
  /* neighbour: pointer or keyboard focus on the title next to it (a link to another chapter) */
  .nav-ch-h:has(a.nav-ch-t:hover) .chev,.nav-ch-h:has(a.nav-ch-t:focus-visible) .chev{background:var(--ch-sel)}
  /* live: pointer or focus on the chevron itself; pointer on the current chapter's row, where the title folds the list too */
  .chev:hover,.chev:focus-visible,.nav-ch[data-here] .nav-ch-h:hover .chev{background:var(--ch-live)}
  .chev:hover::before,.chev:focus-visible::before,.nav-ch[data-here] .nav-ch-h:hover .chev::before{opacity:1}
}
/* no hover to announce it, so the toggle is drawn as a button, the way "Expand all" is. The strip, as tall as the row,
   is still what is pressed; what is seen is a box inside it (::after): the border, radius and height of .nav-toggle
   (12px text at line height 1.6, 3px padding, 1px border), its right edge under that button's. It sits at the title's
   first line (6px padding, 14px text at 1.3), so boxes of rows one under another keep a gap, and so does the glyph.
   The box's fill (--chev-bg) at rest: grey when folded, the chapter's hover tint when open; the current chapter's,
   open or folded, its selected tint (never grey); pressed: one step denser. A coloured box has a coloured edge
   (--chev-bd): the chapter's tint one step denser than the fill; the grey edge belongs to the grey box alone */
@media (hover:none){
  .chev{padding:calc(6px + 14px * 1.3 / 2 - 3px) 0 0 6px;place-items:start center;position:relative;--chev-bg:var(--line);--chev-bd:var(--line)}
  .chev::after{content:"";box-sizing:border-box;position:absolute;right:0;top:calc(6px + 14px * 1.3 / 2 - (12px * 1.6 + 8px) / 2);width:28px;height:calc(12px * 1.6 + 8px);border:1px solid var(--chev-bd);border-radius:6px;background:var(--chev-bg);transition:background-color .35s var(--soft),border-color .35s var(--soft)}
  .chev::before{position:relative;z-index:1}
  .chev:focus-visible{outline:none}.chev:focus-visible::after{outline:2px solid var(--link);outline-offset:2px}
  .chev[aria-expanded="true"]{--chev-bg:var(--ch-hov);--chev-bd:var(--ch-sel)}
  .nav-ch[data-here] .chev{--chev-bg:var(--ch-sel);--chev-bd:var(--ch-live)}
  .chev:active,.nav-ch[data-here] .chev:active,.nav-ch[data-here] .nav-ch-h:active .chev{--chev-bg:var(--ch-live);--chev-bd:var(--ch-deep)}
  .chev:active::before,.nav-ch[data-here] .nav-ch-h:active .chev::before{opacity:1}
}
:root{interpolate-size:allow-keywords}
.nav-ch-c{block-size:0;overflow:hidden;transition:block-size .45s var(--soft),content-visibility .45s allow-discrete}
.nav-ch-c:not([hidden]){block-size:auto}
/* the hover fills only where there is a hover: on touch they would stay on the row last tapped */
@media (hover:hover){.nav-ch li a:hover{background:var(--ch-hov);color:var(--text);text-decoration:none}.nav-ch-h:hover{background:var(--ch-hov)}}
.nav-ch ul{list-style:none;margin:2px 0 8px;padding:0 0 0 16px}
.nav-ch li a,.nav-ch .nav-cur{display:flex;gap:8px;padding:4px 8px;border-radius:6px;color:var(--muted);line-height:1.4}
.nav-ch .nav-cur{cursor:default;background:var(--ch-sel);color:var(--text);font-weight:700}
/* the page's sections under the current item: shown only where "On this page" is hidden (see responsive)
   their text starts in a column the menu already has. Under a subcategory: the subcategory names' column,
   past the number (.num: 2.4em of 12px) and the 8px gap */
.nav-sec{display:none;list-style:none;margin:2px 0 4px;padding:0 0 0 calc(2.4 * 12px + 8px);font-size:13px}
.nav-ch .nav-sec a.is-active{background:var(--ch-sel);color:var(--text);font-weight:700}
/* under a chapter row: the same column, reached without the subcategory list's 16px */
.nav-ch>.nav-sec{padding-left:calc(16px + 2.4 * 12px + 8px)}
/* under "Contents" (home page) the list is outside every chapter: the same items in the colours of "Contents" itself,
   their text where chapter 1's title starts. An unseen "1." set as the chapter numbers are (.nav-ch-n in .nav-ch-h)
   and the row's 6px gap stand before each item, so the column holds in any font */
.sidebar>.nav-sec{margin:-4px 0 6px;padding-left:0}
.sidebar>.nav-sec li{display:flex}
.sidebar>.nav-sec li::before{content:"1.";flex:none;visibility:hidden;font-size:14px;font-weight:600;line-height:1;margin-right:6px}
.sidebar>.nav-sec a{flex:1;min-width:0}
.sidebar>.nav-sec a{display:flex;padding:4px 8px;border-radius:6px;color:var(--muted);line-height:1.4;transition:background-color .35s var(--soft)}
@media (hover:hover){.sidebar>.nav-sec a:hover{background:var(--bg-soft);color:var(--text);text-decoration:none}}
.sidebar>.nav-sec a.is-active{background:var(--bg-soft);color:var(--text);text-decoration:none}
.sidebar>.nav-sec a.is-active{font-weight:700}
@media (hover:none){
  /* one geometry for every filled shape in the menu, taken from the chevron's box (above): 1.5px clear of its row's top and bottom
     (the box in a one-line row), 6px corners, and the box's right edge. Rows keep their height and text its place:
     what a shape gives up in padding it takes back as margin */
  .nav-ch li a,.nav-ch .nav-cur,.sidebar>.nav-sec a{margin-block:1.5px;padding-block:2.5px}
  .nav-ch li{display:flow-root}  /* the margins stay inside the row: rows do not move closer */
  /* under the current subcategory: the list's 2px and the pill's 1.5px would merge into 2px; its 4px below goes to the row,
     where it merges with what follows as it did */
  .nav-ch .nav-cur+.nav-sec{margin:3.5px 0 0}.nav-ch li:has(>.nav-sec){margin-bottom:4px}
  /* a title and the button beside it are two objects: the title's fill stops 3px short of the button.
     The current chapter's fill moves from the row to its title; the title's text keeps its width */
  .nav-ch-h:has(.nav-ch-t[aria-current]){background:none}
  .nav-ch-t[aria-current],.nav-ch[data-here] .nav-ch-h:has(.chev[aria-expanded="false"]) .nav-ch-t{background:var(--ch-sel);margin:1.5px -3px 1.5px 0;padding:4.5px 3px 4.5px 8px}
  /* (the second selector: a subcategory's chapter, folded. The current item is out of sight, so its chapter's title carries the mark) */
  /* "Contents" and "Expand all" are such a pair too: the pill is as tall as that button, level with it, and stops 3px short of it */
  .nav-home{margin:calc((14px * 1.6 + 12px - 12px * 1.6 - 8px) / 2) -5px calc((14px * 1.6 + 12px - 12px * 1.6 - 8px) / 2) 0;padding:calc((12px * 1.6 + 8px - 14px * 1.6) / 2) 13px calc((12px * 1.6 + 8px - 14px * 1.6) / 2) 8px}
}
.nav-ch .num{font-family:var(--mono);font-size:12px;min-width:2.4em;color:var(--text);padding-top:1px}
.main{--pad:clamp(16px,3vw,40px);min-width:0;padding:28px var(--pad) 80px}
.main>*{max-width:var(--measure);margin-left:max(0px,calc((100% - var(--measure)) / 2));margin-right:auto;transition:max-width .45s var(--soft),margin-left .45s var(--soft)}
@media (min-width:861px){.side-hidden{--measure:900px}.side-hidden .main>*{margin-left:max(0px,calc(100% - var(--measure)))}}
.toc{position:sticky;top:calc(var(--top) + var(--cover-h));height:calc(100vh - var(--top) - var(--cover-h));overflow:auto;padding:44px 16px 28px;font-size:13px}
.toc-h{margin:0 0 8px;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;font-size:11px}
.toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--line)}
.toc a{display:block;padding:4px 12px;color:var(--muted);margin-left:-1px;border-left:2px solid transparent}
.toc a{border-radius:0 6px 6px 0;transition:background-color .35s var(--soft)}
@media (hover:hover){.toc a:hover{color:var(--text);text-decoration:none;background:var(--ch-hov,var(--bg-soft))}.toc:not([style]) a:hover{background:var(--bg-soft)}}
.toc a.is-active{color:var(--text);border-left-color:var(--text);font-weight:700}

/* covers */
/* full-width band under the top bar; its content stays within the 1440px layout */
.cover{position:sticky;top:var(--top);z-index:25;height:var(--cover-h);overflow:hidden;background:var(--ch-dark)}
.cover-in{position:relative;height:100%;max-width:var(--shell);margin:0 auto;padding:0 16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;text-align:center}
.cover img{display:block;width:100%;height:100%;object-fit:cover}
.cover-css{background:linear-gradient(color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent),color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent)),var(--ch-dark)}
.cv-1{color:var(--ch-light);font-size:15px;text-transform:uppercase;letter-spacing:.12em;font-weight:500;line-height:1}
.cover-ch .cv-1{margin:0;font-size:24px;letter-spacing:.08em;line-height:1;text-transform:uppercase}
.cv-2{margin:0;color:var(--ch-accent);font-size:30px;font-weight:600;letter-spacing:-.005em;line-height:1}
.cv-n{font-family:var(--mono);font-weight:500}.cv-c{display:none}
.cover-home{background:#1829c4}
/* the 1500x260 Notion composition, scaled by .8 to fit the 1500x200 banner */
.hm{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px}
.hm-mark{width:49px;overflow:visible;stroke-width:1.25}
.hm-t{color:#fff;font-size:21px;font-weight:500;letter-spacing:.08em;line-height:1;text-transform:uppercase}
/* prev/next arrows at the banner's edges */
/* the link is a tall 80px strip (easy to hit); the visible 40px circle sits 30px from the edge */
/* each arrow's hit area runs from the banner edge to the text column; the 40px circle sits 30px from the edge */
.cv-arr{position:absolute;top:0;bottom:0;z-index:1;display:block;width:max(80px,calc((100% - var(--measure)) / 2));color:var(--ch-accent);opacity:.6;
  transition:opacity .3s var(--soft),background-color .3s var(--soft)}
.cv-arr::before{content:"";position:absolute;top:50%;width:40px;height:40px;margin-top:-20px;border-radius:50%;transition:background-color .3s var(--soft)}
.cv-arr svg{position:absolute;top:50%;margin-top:-11px}
.cv-prev::before{left:20px}.cv-prev svg{left:29px}.cv-next::before{right:20px}.cv-next svg{right:29px}
/* hover: a soft glow around the arrow (no hard edge), plus the lit circle */
.cv-arr{--glow:color-mix(in srgb,var(--ch-accent) 16%,transparent)}.cover-home .cv-arr{--glow:rgba(255,255,255,.13)}
.cv-arr::after{content:"";position:absolute;inset:0;z-index:-1;opacity:0;transition:opacity .35s var(--soft)}
.cv-prev::after{background:radial-gradient(ellipse 260px 110px at 40px 50%,var(--glow),transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 48px);mask-image:linear-gradient(90deg,transparent,#000 48px)}
.cv-next::after{background:radial-gradient(ellipse 260px 110px at calc(100% - 40px) 50%,var(--glow),transparent);-webkit-mask-image:linear-gradient(270deg,transparent,#000 48px);mask-image:linear-gradient(270deg,transparent,#000 48px)}
@media (hover:hover){.cv-arr:hover::after{opacity:1}}
.cv-arr svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.cv-prev{left:10px}.cv-next{right:10px}
@media (hover:hover){.cover:hover .cv-arr{opacity:1}}
.cv-arr:focus-visible{opacity:1}
@media (hover:none){.cv-arr{opacity:1}}
@media (hover:hover){.cv-arr:hover{text-decoration:none;outline-offset:-4px}}
.cv-arr:focus-visible{text-decoration:none;outline-offset:-4px}
.cv-arr:focus-visible{outline-color:var(--ch-accent)}.cover-home .cv-arr:focus-visible{outline-color:#fff}
@media (hover:hover){.cv-arr:hover::before{background:color-mix(in srgb,var(--ch-accent) 16%,transparent)}}
.cv-arr:focus-visible::before{background:color-mix(in srgb,var(--ch-accent) 16%,transparent)}
.cover-home .cv-arr{color:#fff}@media (hover:hover){.cover-home .cv-arr:hover::before{background:rgba(255,255,255,.14)}}
.cover-home .cv-arr:focus-visible::before{background:rgba(255,255,255,.14)}

/* page head */
.page-head{position:relative;margin-top:-6px}
.crumbs-row{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:22px 0 0}
.crumbs{font-size:13px;color:var(--muted);margin:0}
.crumb-cur{color:var(--ph,#6b6b6b)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .crumb-cur{--ph:#9b9b99}}:root[data-theme="dark"] .crumb-cur{--ph:#9b9b99}
.cnav{display:flex;flex:none;height:20px;align-items:center}
.cn{display:grid;place-items:center;width:24px;height:24px;border-radius:6px;color:var(--text)}
.cn svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
a.cn{transition:background-color .25s var(--soft)}@media (hover:hover){a.cn:hover{background:var(--ch-hov);text-decoration:none}}
.cn.is-off{opacity:.25}.crumbs .sep{margin:0 6px;color:var(--arrow);font-size:.85em}.crumbs a{color:var(--muted)}
h1,.lede{font-size:clamp(28px,4.2vw,40px);line-height:1.15;letter-spacing:-.02em;margin:40px 0 18px;font-weight:700}
h2{font-size:22px;line-height:1.3;margin:36px 0 12px;letter-spacing:-.01em;font-weight:650;display:flex;flex-wrap:wrap;align-items:baseline;gap:0 8px}
h2 .em{font-size:20px}h2 .arrow{color:var(--arrow);font-weight:500}h2 .to{font-weight:650}
section>h2{margin-top:36px}
/* landing cue: the heading a click in "On this page" lands on twitches from the centre of its text;
   with reduced motion a ring flashes round its text instead and fades outward
   (app.js adds .cue once the scroll stops and sets --cue-x, the text box --cue-bx/-by/-bw/-bh, and the colours --cue-l, --cue-d) */
:root{--cue-scale:1.03;--cue-dip:.99;--cue-dur:.3s;--cue-r:12px;--cue-ring-w:3px;--cue-ring-gap:6px;--cue-ring-spread:8px;--cue-ring-dur:.9s;--cue-c:var(--cue-l,var(--link))}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--cue-c:var(--cue-d,var(--link))}}
:root[data-theme="dark"]{--cue-c:var(--cue-d,var(--link))}
.cue{transform-origin:var(--cue-x,50%) center;animation:bb-cue-twitch var(--cue-dur) ease-in-out}
@keyframes bb-cue-twitch{40%{transform:scale(var(--cue-scale))}75%{transform:scale(var(--cue-dip))}}
/* of .9s: full by 60ms, held to 210ms, then fading while the gap grows by the spread */
@keyframes bb-cue-ring{0%{opacity:0}6.67%{opacity:1}23.33%{opacity:1;inset:calc(var(--cue-by) - var(--cue-ring-gap)) auto auto calc(var(--cue-bx) - var(--cue-ring-gap));width:calc(var(--cue-bw) + 2 * var(--cue-ring-gap));height:calc(var(--cue-bh) + 2 * var(--cue-ring-gap));animation-timing-function:ease-out}
  100%{opacity:0;inset:calc(var(--cue-by) - var(--cue-ring-gap) - var(--cue-ring-spread)) auto auto calc(var(--cue-bx) - var(--cue-ring-gap) - var(--cue-ring-spread));width:calc(var(--cue-bw) + 2 * (var(--cue-ring-gap) + var(--cue-ring-spread)));height:calc(var(--cue-bh) + 2 * (var(--cue-ring-gap) + var(--cue-ring-spread)))}}
@media (prefers-reduced-motion:reduce){
  .cue{position:relative}
  .cue::before{content:"";position:absolute;box-sizing:border-box;inset:calc(var(--cue-by) - var(--cue-ring-gap)) auto auto calc(var(--cue-bx) - var(--cue-ring-gap));width:calc(var(--cue-bw) + 2 * var(--cue-ring-gap));height:calc(var(--cue-bh) + 2 * var(--cue-ring-gap));
    border:var(--cue-ring-w) solid var(--cue-c);border-radius:var(--cue-r);pointer-events:none;opacity:0;animation:bb-cue-ring var(--cue-ring-dur) linear!important}
}

/* blocks */
.q{margin:4px;padding:2px 0 2px 10px;border-left:3px solid var(--quote)}
.q p{margin:0}
.call{border-radius:12px;padding:16px 20px 16px 20px}
.call.has-em{display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:10px;align-items:start}
.call-em{font-size:24px;line-height:25.6px}
.call p{margin:0}.call.lines p+p{margin-top:2px}
.call ol,.call ul{margin:0;padding-left:22px}.call li+li{margin-top:6px}
.call ol li::marker{font-family:var(--mono);font-size:.9em;color:var(--marker);font-weight:600}
.c-peach{background:var(--peach)}.c-blue{background:var(--blue)}.c-pink{background:var(--pink)}
.c-yellow{background:var(--yellow)}.c-green{background:var(--green)}
h3.fa{font-size:15px;margin:16px 0 8px;font-weight:650}
.dirs{display:grid;gap:12px}
.dir{background:#f7f9fb;border-radius:12px;padding:10px 20px 20px}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .dir:not(.repealed){background:#22282b}}
:root[data-theme="dark"] .dir:not(.repealed){background:#22282b}
.dir:target{box-shadow:0 0 0 2px var(--ring,var(--ch-dark))}
.dir:not(.repealed){cursor:default}
/* hover: the active card comes forward, the others step back (repealed cards stay put) */
/* the "UX directives" heading stays under the banner while its cards scroll */
#directives{--bleed:var(--pad,16px);--fade:rgba(15,23,42,.06);position:sticky;top:calc(var(--top) + var(--cover-h));z-index:5;background:var(--bg);margin:24px calc(-1 * var(--bleed)) 0;padding:12px var(--bleed)}
/* shadow: a soft strip below the heading only, fading out toward both ends */
#directives::after{content:"";position:absolute;left:0;right:0;top:100%;height:10px;pointer-events:none;opacity:0;transition:opacity .3s var(--soft);
  background:linear-gradient(var(--fade),transparent);-webkit-mask-image:linear-gradient(90deg,transparent,#000 15%,#000 85%,transparent);mask-image:linear-gradient(90deg,transparent,#000 15%,#000 85%,transparent)}
#directives.is-stuck::after{opacity:1}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) #directives{--fade:rgba(0,0,0,.30)}}
:root[data-theme="dark"] #directives{--fade:rgba(0,0,0,.30)}
.dh-mark{display:block;height:0}
/* --dh-h is the measured height of the sticky heading (it wraps on narrow screens) */
.dir{scroll-margin-top:calc(var(--top) + var(--cover-h,0px) + var(--dh-h,56px) + 16px)}
.dir{--dir-shadow:0 12px 28px -10px rgba(15,23,42,.22),0 2px 6px rgba(15,23,42,.06);transition:transform .5s var(--spring),box-shadow .35s var(--soft)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .dir{--dir-shadow:0 12px 28px -10px rgba(0,0,0,.7),0 2px 6px rgba(0,0,0,.4)}}
:root[data-theme="dark"] .dir{--dir-shadow:0 12px 28px -10px rgba(0,0,0,.7),0 2px 6px rgba(0,0,0,.4)}
@media (hover:hover){
  .dirs:has(.dir:not(.repealed):hover) .dir:not(.repealed):not(:hover){transform:scale(.985)}
  .dir:not(.repealed):hover{transform:scale(1.015);box-shadow:var(--dir-shadow);position:relative;z-index:1}
  .dir:target:not(.repealed):hover{box-shadow:0 0 0 2px var(--ring,var(--ch-dark)),var(--dir-shadow)}
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .dir:target{--ring:var(--ch-accent)}}
:root[data-theme="dark"] .dir:target{--ring:var(--ch-accent)}
.dir-meta{display:flex;align-items:center;gap:2px;font-size:11px}
.chip{background:var(--ch-sel);color:var(--text);padding:1px 6px;border-radius:4px;font-family:var(--mono);font-weight:600}
.chip{display:inline-flex;align-items:center;gap:6px}
.chip .bul{flex:none;width:3px;height:3px;border-radius:50%;background:currentColor}  /* drawn, so its size does not depend on the font */
.chip.rep{background:transparent;border:1px solid var(--line);color:var(--muted)}
.dir-title{font-size:16px;margin:0;font-weight:650}
.dir-body{margin:0}
.dir.repealed{background:transparent;border:1px dashed var(--line)}
.dir.repealed .dir-body{color:var(--muted);margin:0}

/* pager */
.pager{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:48px;padding-top:8px}
.pg{display:flex;flex-direction:column;gap:4px;padding:12px 16px;border-radius:10px;color:var(--text);transition:background-color .35s var(--soft),transform .6s var(--spring)}
@media (hover:hover){.pg:not(.empty):hover{text-decoration:none;background:var(--ch-hov);transform:translateY(-4px) scale(1.02)}}
.pg.next{text-align:right;align-items:flex-end}
.pg-dir{font-size:12px;color:var(--muted)}
.pg-ar{display:inline-block;transition:transform .5s var(--spring)}
@media (hover:hover){.pg.prev:hover .pg-ar{transform:translateX(-4px)}.pg.next:hover .pg-ar{transform:translateX(4px)}}
.pg-t{display:flex;gap:8px;align-items:center;font-weight:600}

/* home */
.hero{padding:16px 0 8px}
.hero-k{margin:0;color:var(--muted);font-size:13px;letter-spacing:.14em;text-transform:uppercase}
.hero h1{font-size:clamp(32px,5.4vw,52px);margin:28px 0 6px}
.hero-s{font-size:19px;color:var(--muted);margin:0 0 16px}
.hero-stats{display:flex;flex-wrap:wrap;gap:8px 20px;margin:0;font-size:14px;color:var(--muted)}
.hero-stats b{color:var(--text);font-family:var(--mono)}
.ch-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
.ch-card{display:grid;grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto auto 1fr;column-gap:6px;row-gap:12px;min-height:170px;padding:16px;border-radius:12px;
  background:linear-gradient(color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent),color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent)),var(--ch-dark);color:var(--ch-light)}
.ch-card{transition:transform .5s var(--spring),box-shadow .35s var(--soft)}
@media (hover:hover){
  .ch-card:hover{text-decoration:none}
  .ch-card:hover{transform:scale(1.03);box-shadow:0 14px 30px -10px rgba(15,23,42,.35),0 2px 6px rgba(15,23,42,.08);position:relative;z-index:1}
}
.ch-card-t{color:var(--ch-accent);font-weight:650;font-size:18px;line-height:1.15}
.ch-card-d{font-size:13px;line-height:1.3}
.ch-card-c{font-size:12px;font-family:var(--mono)}
.prose h2{margin-top:44px}.prose h2+*{margin-top:0}
.prose blockquote{margin:18px 0;padding:2px 0 2px 18px;border-left:3px solid var(--quote)}
.prose blockquote p{margin:8px 0}
.prose ul,.prose ol{padding-left:22px}.prose ol li::marker{font-weight:700}.prose li+li{margin-top:6px}

/* chapter tiles */
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
.tile{display:grid;grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto auto auto 1fr;column-gap:6px;row-gap:12px;min-height:170px;padding:16px;border-radius:12px;color:var(--ch-light);
  background:linear-gradient(color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent),color-mix(in srgb,var(--ch-mid) calc(var(--ch-mid-op)*100%),transparent)),var(--ch-dark)}
.tile{transition:transform .5s var(--spring),box-shadow .35s var(--soft)}
/* hover: like directive cards, the active tile comes forward, the others step back */
@media (hover:hover){
  .tile:hover{text-decoration:none}
  .tile:hover{transform:scale(1.03);box-shadow:0 14px 30px -10px rgba(15,23,42,.35),0 2px 6px rgba(15,23,42,.08);position:relative;z-index:1}
}
.tile-t{color:var(--ch-accent);font-weight:650;font-size:18px;line-height:1.15}
/* hanging number: everything else lines up with the title text */
.card-n{grid-column:1;grid-row:1;color:var(--ch-accent);font-weight:650;font-size:18px;line-height:1.15}
.tile>:not(.card-n),.ch-card>:not(.card-n){grid-column:2}
.card-foot{align-self:end}
.tile-count,.ch-card-c{transition:color .3s var(--soft)}
@media (hover:hover){.tile:hover .tile-count,.ch-card:hover .ch-card-c{color:var(--ch-accent)}}
.tile-gov{font-size:14px;line-height:1.3;font-weight:500}.tile-ask{font-size:13px;line-height:1.3}
.tile-count{font-size:12px;font-family:var(--mono)}
.card-foot{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:8px}
.go{display:grid;color:var(--ch-accent);transition:transform .5s var(--spring)}
.go svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
@media (hover:hover){.tile:hover .go,.ch-card:hover .go{transform:translateX(5px)}}

/* responsive */
@media (max-width:1180px){body.has-toc .shell{grid-template-columns:var(--side-w) minmax(0,1fr)}.toc{display:none}.nav-sec{display:block}}
@media (max-width:860px){
  .shell,body.has-toc .shell{grid-template-columns:minmax(0,1fr)}
  :root{--cover-h:88px;--cover-full:88px}
  /* condensed banner: once the page is scrolled the banner is one 40px line with the page's own name.
     --cover-h is the condensed height (the sticky heading and anchors clear that); the banner keeps its full
     88px in the flow (height + margin), so the text under it does not move when it changes state */
  :root.cvc{--cover-h:40px}
  .cover{height:var(--cover-full);transition:height .18s ease,margin-bottom .18s ease}
  .cover.is-min{height:var(--cover-h);margin-bottom:calc(var(--cover-full) - var(--cover-h))}
  .cover.is-min .cover-in{padding:0 16px}
  .cover.is-min .cv-arr,.cover.is-min .hm-mark,.cover:not(.cover-ch).is-min .cv-1{display:none}
  .cover.is-min .cv-1,.cover.is-min .cv-2,.cover.is-min .hm-t{max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;line-height:1.3}
  .cover.is-min .cv-2{font-size:17px}.cover-ch.is-min .cv-1{font-size:13px}.cover.is-min .hm-t{font-size:12px}
  .cover.is-min .hm{padding:0 16px}
  /* "2. Discoverability" reads "2.2 Discoverability": the chapter number appears, the dot after the subcategory number takes no room */
  .cover.is-min .cv-c{display:inline}.cover.is-min .cv-d{font-size:0}
  /* the sticky heading is just "UX directives": the banner above it names the subcategory; the name stays for screen readers */
  #directives .arrow{display:none}#directives .to{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
  .cover-in{gap:8px;padding:0 52px}.cv-1{font-size:11px}.cv-2{font-size:21px}.cover-ch .cv-1{font-size:17px}
  .hm{gap:8px}.hm-mark{width:34px}.hm-t{font-size:14px}.cv-arr{width:52px}.cv-prev::before{left:6px}.cv-prev svg{left:15px}.cv-next::before{right:6px}.cv-next svg{right:15px}.cv-prev{left:0}.cv-next{right:0}
  .sidebar{position:fixed;left:0;top:var(--top);bottom:0;width:min(86vw,320px);height:auto;background:var(--bg);z-index:40;transform:translateX(-102%);visibility:hidden;overscroll-behavior:contain;transition:transform .2s ease,visibility 0s .2s}
  body.nav-open .sidebar{transform:none;visibility:visible;transition:transform .2s ease,visibility 0s}
  body.nav-open{overflow:hidden}
  .ic-panel{display:none}.ic-burger{display:block}
  body.nav-open .ic-burger .l1{transform:translateY(4px) rotate(45deg)}
  body.nav-open .ic-burger .l2{opacity:0}
  body.nav-open .ic-burger .l3{transform:translateY(-4px) rotate(-45deg)}
  .scrim{position:fixed;inset:var(--top) 0 0 0;background:rgba(0,0,0,.35);z-index:35}
  .top-in{padding:0 16px;gap:10px}
  .brand-t{display:inline-block;max-width:34vw;overflow:hidden;text-overflow:ellipsis;vertical-align:bottom}
  .search{width:auto;flex:1}.search kbd{display:none}
  /* touch targets: the field and its clear button are 44px tall; the hover square of the button stays 26px */
  .search input{height:44px;padding:0 10px 0 32px}.search.has-val input{padding-right:44px}
  .search-ic{top:13px}
  .search-x{width:44px;height:44px}.search-x::before{inset:9px}
  /* the list leaves the field's column: under the header, the screen's width less 16px gutters, as tall as the screen allows.
     Fixed resolves against the viewport: the header sticks at 0, so the list starts 6px under it */
  .results{position:fixed;top:calc(var(--top) + 6px);left:16px;right:16px;max-height:calc(100vh - var(--top) - 22px);max-height:calc(100dvh - var(--top) - 22px)}
  .main{padding:16px 16px 64px}
  .pager{grid-template-columns:1fr}
  .pg.next{text-align:left;align-items:flex-start}
}
/* phones: the field gets the title's room; the emblem stands in for it as the home link */
@media (max-width:520px){.brand{display:none}.brand-m{display:grid}.top-in{gap:8px}}
@media (prefers-reduced-motion:reduce){@view-transition{navigation:none}*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}
  /* the tooltip keeps its fade and loses its move */
  .tip,.tip.up,.tip.at-r,.tip.at-l{transform:none;transition:opacity .15s linear,visibility 0s .15s!important}.tip.on{transition:opacity .15s linear,visibility 0s!important}}
@media print{.top,.sidebar,.toc,.pager,.scrim{display:none!important}.shell{display:block}.main{padding:0}}
"""

JS = r"""
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
  if(location.hash){var tg=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(tg)setTimeout(function(){tg.scrollIntoView({behavior:'instant'})},0)}
  // enable transitions only after the first frames, so restored state does not animate
  requestAnimationFrame(function(){requestAnimationFrame(function(){root.classList.remove('preload')})});
  // smooth scrolling only after the page has settled, so a link to #id lands instantly
  addEventListener('load',function(){setTimeout(function(){root.classList.add('smooth')},100)});
  // in-page links: smooth scroll (CSS) and move focus to the target
  function focusTarget(el){if(!el||!el.nodeType)el=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;if(!el.matches('a[href],button,input,select,textarea,[tabindex]'))el.setAttribute('tabindex','-1');el.focus({preventScroll:true})}
  addEventListener('hashchange',focusTarget);
  // theme
  var tb=document.querySelector('.theme-btn'),sysDark=matchMedia('(prefers-color-scheme: dark)');
  function isDark(){return root.dataset.theme?root.dataset.theme==='dark':sysDark.matches}
  // the button names the theme a click switches to
  function themeLabel(){var t=isDark()?'Switch to light theme':'Switch to dark theme';tb.setAttribute('aria-label',t)}
  if(tb){tb.addEventListener('click',function(){
    root.dataset.theme=isDark()?'light':'dark';themeLabel();
    tb.classList.remove('turn');void tb.offsetWidth;tb.classList.add('turn');
    try{localStorage.setItem('bb-theme',root.dataset.theme)}catch(e){}
  });sysDark.addEventListener('change',themeLabel);themeLabel()}
  // mobile nav
  var mb=document.querySelector('.menu-btn'),scrim=document.querySelector('.scrim'),side=document.getElementById('sidebar');
  var mobile=matchMedia('(max-width: 860px)');
  // opening moves focus into the menu; closing returns it to the button (unless keep)
  // while the mobile menu is open, everything but the top bar and the menu is inert (Tab cannot reach the page under the scrim)
  function setNav(open,keep){var was=document.body.classList.contains('nav-open');document.body.classList.toggle('nav-open',open);scrim.hidden=!open;sync();
    [].forEach.call(document.querySelectorAll('body>*,.shell>*'),function(n){if(!n.matches('.top,.shell,.sidebar,.scrim,.tip,script'))n.inert=open});
    if(open){var f=side.querySelector('a[href],button');if(f)f.focus({preventScroll:true})}else if(was&&!keep)mb.focus({preventScroll:true})}
  function sync(){var open=mobile.matches?document.body.classList.contains('nav-open'):!root.classList.contains('side-hidden');
    var t=mobile.matches?(open?'Close panel':'Open panel'):(open?'Hide panel':'Show panel');
    mb.setAttribute('aria-expanded',open);mb.setAttribute('aria-label',t)}
  function setSide(hidden){root.classList.toggle('side-hidden',hidden);sync();try{localStorage.setItem('bb-side',hidden?'hidden':'shown')}catch(e){}}
  if(mb){mb.addEventListener('click',function(){if(mb.matches(':hover'))mb.classList.add('pv-off');if(mobile.matches)setNav(!document.body.classList.contains('nav-open'));else setSide(!root.classList.contains('side-hidden'))});
    scrim.addEventListener('click',function(){setNav(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!e.defaultPrevented&&mobile.matches&&document.body.classList.contains('nav-open'))setNav(false)});
    mobile.addEventListener('change',function(){if(!mobile.matches)setNav(false,true);else sync()});sync();
    // the icon's hover preview is off from a click until the pointer leaves
    mb.addEventListener('pointerleave',function(){mb.classList.remove('pv-off')});}
  // tooltips: one styled label under an icon-only control; its text is the control's aria-label.
  // Hover shows it after TIP_DELAY, at once if another tooltip was showing within TIP_CHAIN; keyboard focus shows it at once; touch never.
  // A click and Escape hide it, and it does not return while the pointer stays on the same control.
  var TIP_SEL='.menu-btn,.theme-btn,.brand-m,.search-x,.r-x,.cv-arr,a.cn,.chev',TIP_DELAY=400,TIP_CHAIN=300;
  var tip=document.createElement('div'),tipOwn=null,tipOver=null,tipT=0,tipGone=0,tipMute=false,canHover=matchMedia('(hover:hover)');
  tip.className='tip';tip.setAttribute('aria-hidden','true');document.body.appendChild(tip);
  function tipCtl(n){return n&&n.closest?n.closest(TIP_SEL):null}
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
  function tipText(el){return el.matches('.chev')?(el.getAttribute('aria-expanded')==='true'?'Collapse':'Expand'):el.getAttribute('aria-label')}
  function tipShow(el){clearTimeout(tipT);var t=tipText(el);if(!t)return;tipOwn=el;tip.textContent=t;tipPlace();if(tipOwn)tip.classList.add('on')}
  function tipHide(){clearTimeout(tipT);if(tipOwn){tipOwn=null;tipGone=Date.now();tip.classList.remove('on')}}
  // a click or Escape may move the focus by script (the menu closing): that focus shows no tooltip
  function tipDismiss(){tipHide();tipMute=true;setTimeout(function(){tipMute=false},0)}
  document.addEventListener('pointerover',function(e){
    if(e.pointerType==='touch'||!canHover.matches||tip.contains(e.target))return;
    var el=tipCtl(e.target);if(el===tipOver)return;tipOver=el;clearTimeout(tipT);
    if(!el){if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();return}
    if(tipOwn||Date.now()-tipGone<TIP_CHAIN)tipShow(el);else tipT=setTimeout(function(){tipShow(el)},TIP_DELAY)});
  root.addEventListener('pointerleave',function(){tipOver=null;if(tipOwn&&!tipOwn.matches(':focus-visible'))tipHide();else clearTimeout(tipT)});
  document.addEventListener('focusin',function(e){var el=tipCtl(e.target);if(el&&!tipMute&&el.matches(':focus-visible'))tipShow(el)});
  document.addEventListener('focusout',function(e){if(tipOwn&&tipCtl(e.target)===tipOwn&&tipOver!==tipOwn)tipHide()});
  document.addEventListener('click',tipDismiss,true);
  document.addEventListener('keydown',function(e){if(e.key==='Escape')tipDismiss()},true);
  addEventListener('scroll',tipPlace,{passive:true,capture:true});addEventListener('resize',tipHide);document.addEventListener('input',tipPlace);
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
    var mix=__CUE_MIX__[acc];
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
      if(!a.closest('.nav-sec'))el.addEventListener('animationend',function(e){if(e.target===el&&/^bb-cue-/.test(e.animationName))el.classList.remove('cue')});
      a.addEventListener('click',function(e){if(e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
        // where the jump will stop: the heading's line (the sticky heading's mark), kept within the page
        var d=topOf(el)-(parseFloat(getComputedStyle(el).scrollMarginTop)||0);
        cueY=Math.max(0,Math.min(scrollY+d,root.scrollHeight-innerHeight));
        cueEl=el;if(Math.abs(cueY-scrollY)<1){cueNow();return}
        addEventListener('scroll',cueWait,{passive:true});addEventListener('scrollend',cueEnd);
        // the jump can start a few frames late: give it 400ms before taking "no scroll" for an answer
        clearTimeout(cueT);cueT=setTimeout(cueNow,400)})});
  }
  // directives heading: shadow only while stuck under the banner
  var dh=document.getElementById('directives');
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
      var y=scrollY+mk.getBoundingClientRect().top-(parseFloat(getComputedStyle(dh).scrollMarginTop)||0);
      if(location.hash!=='#directives')location.hash='directives';
      focusTarget();scrollTo(0,Math.max(0,Math.min(y,root.scrollHeight-innerHeight)))})});}
  // search
  var q=document.getElementById('q'),res=document.getElementById('results'),idx=window.BB_INDEX||[],chTitles=window.BB_CHAPTERS||{},vocab=window.BB_VOCAB||{},words={},sel=-1,items=[];
  if(!q)return;
  function norm(s){return s.toLowerCase().replace(/[’']/g,'')}
  // result count for screen readers, announced once typing pauses
  var status=document.getElementById('q-status'),sayT;
  function say(t){clearTimeout(sayT);sayT=setTimeout(function(){if(status)status.textContent=t},400)}
  function close(){res.hidden=true;sel=-1;q.setAttribute('aria-expanded','false');q.removeAttribute('aria-activedescendant')}
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
  // ---- no results: suggest a correction (27/08)
  // true if the query finds anything, counting the any-word fallback
  function finds(v){var gs=groups(v);return idx.some(function(x){return gs.some(function(g){return g.some(function(t){return at(x._h,t)})})})}
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
  // the query with every word that alone finds nothing replaced by its nearest candidate; null unless that query finds results.
  // If it finds nothing, the correction runs once more without the candidates that find nothing alone
  function correct(raw){
    function attempt(skip){
      var changed=false,out=raw.trim().split(/\s+/).map(function(w){
        var n=norm(w),fix=/^[a-z]+$/.test(n)&&!finds(n)&&nearest(n,skip);
        if(fix)changed=true;return fix||w}).join(' ');
      return changed&&finds(norm(out))?out:null}
    return attempt()||attempt(deadWords())}
  function applyFix(li){q.value=li.getAttribute('data-q');q.parentNode.classList.add('has-val');run();q.focus({preventScroll:true})}
  function run(){
    var v=norm(q.value.trim());res.innerHTML='';sel=-1;
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
    items=scored.slice(0,30).map(function(p){return p[1]});
    var n=scored.length,count=!n?'No results':n>30?'Showing 30 of '+n+' results':n===1?'1 result':n+' results';
    if(any)count='No directive matches all words. Showing '+(n>30?'30 of '+n+' that match':n===1?'the 1 that matches':n+' that match')+' any.';say(count);
    // nothing at all: say what happened, suggest a correction, offer a way out. The suggestion is an option
    // (arrows reach it, Enter or a click runs it); the two sentences are not. #q-status says the same text.
    if(!items.length){
      var fix=correct(q.value),l1='The book has no directive on “'+q.value.trim()+'”.',l3='Try a broader word, or browse the Contents.';
      say(l1+(fix?' Did you mean '+fix+'? ':' ')+l3);
      res.innerHTML='<li class="r-empty" role="presentation">'+escH(l1)+'</li>'
        +(fix?'<li role="option" id="r0" class="r-fix" data-q="'+escH(fix).replace(/"/g,'&quot;')+'"><a href="#">Did you mean <span class="r-t">'+escH(fix)+'</span>?</a></li>':'')
        +'<li class="r-empty" role="presentation">Try a broader word, or browse the <a href="index.html">Contents</a>.</li>'}
    // the same count, visible: a heading row, not an option (arrows skip it; #q-status does the announcing);
    // the any-word notice is a sentence, so it takes the plain look of the no-match line (.r-empty)
    else{var head=document.createElement('li');head.className=any?'r-empty':'r-head';head.setAttribute('role','presentation');head.setAttribute('aria-hidden','true');head.textContent=count;res.appendChild(head)}
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
        +'<button type="button" class="r-x" aria-label="Remove from history">×</button>';
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
  res.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var li=a.closest('li');if(li.classList.contains('r-fix')){e.preventDefault();e.stopPropagation();applyFix(li);return}var i=[].indexOf.call(res.querySelectorAll('li[role=option]'),li);if(i>-1&&items[i]&&!li.classList.contains('r-hist'))remember(items[i])});
  function move(d){var lis=res.querySelectorAll('li[role=option]');if(!lis.length)return;sel=(sel+d+lis.length)%lis.length;lis.forEach(function(l,i){l.setAttribute('aria-selected',i===sel)});lis[sel].scrollIntoView({block:'nearest'});q.setAttribute('aria-activedescendant','r'+sel)}
  q.addEventListener('input',refresh);
  // the clear button: empties the field, keeps the focus in it (no blur on mousedown) and shows Recent
  var qx=q.parentNode.querySelector('.search-x');
  if(qx){qx.addEventListener('mousedown',function(e){e.preventDefault()});
    qx.addEventListener('click',function(){q.value='';say('');q.focus({preventScroll:true});refresh()})}
  q.addEventListener('keydown',function(e){
    if(e.key==='ArrowDown'){e.preventDefault();if(res.hidden)refresh();else move(1)}
    else if(e.key==='ArrowUp'){e.preventDefault();if(res.hidden)refresh();else move(-1)}
    // Enter on a closed list reopens the results for the current query; on an open list it follows the selection
    else if(e.key==='Enter'){if(res.hidden){if(q.value.trim()){e.preventDefault();run()}return}var lis=res.querySelectorAll('li[role=option]');var li=lis[sel]||lis[0];if(li&&li.classList.contains('r-fix')){e.preventDefault();applyFix(li);return}if(li){var a=li.querySelector('a');if(!li.classList.contains('r-hist')&&items[sel<0?0:sel])remember(items[sel<0?0:sel]);location.href=a.href}}
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
  document.addEventListener('click',function(e){if(!e.target.closest('.search')){res.hidden=true;q.setAttribute('aria-expanded','false')}});
  var ic=document.querySelector('.search-ic');
  q.addEventListener('focus',function(){if(ic){ic.classList.remove('pop');void ic.offsetWidth;ic.classList.add('pop')}refresh()});
  if(ic)ic.addEventListener('animationend',function(){ic.classList.remove('pop')});
  q.parentNode.classList.toggle('has-val',!!q.value);
})();
"""

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build the static site for The Blue Book of UX Directives.")
    ap.add_argument("--base", default="/", metavar="PATH",
                    help='URL path the site is served from, for example "/book/" (default: "/")')
    ap.add_argument("--out", default=None, metavar="PATH",
                    help="folder the site is written to (default: site/)")
    args = ap.parse_args()
    main(args.base, args.out)
