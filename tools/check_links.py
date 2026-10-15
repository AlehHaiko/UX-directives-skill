#!/usr/bin/env python3
"""Check every local link and anchor in a built site.

Run from the repository root:
    python3 tools/check_links.py [DIR] [--base /path/] [--skill FILE]
DIR is the built site (default site). --base is the URL path it is served from (default "/").
Checks every href and src in the HTML pages, and every url in assets/search-index.js.
External links (a scheme, or a leading //) are counted and never fetched.
Then checks the packaged skill: SKILL.md inside FILE (default ux-directives.skill) must equal
ux-directives/SKILL.md byte for byte.
Prints three summary lines, then one "file -> target" line per miss. Exit code 1 on any miss
or on a skill that does not match. No dependencies.
"""
import argparse
import json
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ORIGIN = "http://site.invalid"  # stand-in host: local URLs are resolved against it and never requested
INDEX = "assets/search-index.js"
INDEX_VAR = "window.BB_INDEX="
EXTERNAL = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:|//")
SKILL_SRC = Path("ux-directives/SKILL.md")  # the skill folder's SKILL.md, relative to the repository root
SKILL_ZIP = "ux-directives.skill"


class Page(HTMLParser):
    """Collects a page's links, its anchors and its <base href>."""

    def __init__(self):
        super().__init__()
        self.links, self.anchors, self.base = [], set(), None

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value is None:
                continue
            if key == "id" or (key == "name" and tag == "a"):
                self.anchors.add(value)
            elif key in ("href", "src"):
                if tag != "base":
                    self.links.append(value)
                elif self.base is None:
                    self.base = value


def index_urls(root):
    """The url of every entry in the search index; empty if the site has none."""
    path = root / INDEX
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    start = text.find(INDEX_VAR)
    if start < 0:
        sys.exit(f"{INDEX}: {INDEX_VAR} not found")
    entries, _ = json.JSONDecoder().raw_decode(text, start + len(INDEX_VAR))
    return [e["url"] for e in entries if "url" in e]


def skill_check(path):
    """One line on the packaged skill, and whether its SKILL.md equals the folder's byte for byte."""
    src = SKILL_SRC.read_bytes()
    try:
        with zipfile.ZipFile(path) as z:
            packed = z.read(SKILL_SRC.as_posix())
    except (OSError, zipfile.BadZipFile, KeyError) as e:
        return f"skill {path}: cannot read {SKILL_SRC.as_posix()} ({e}), mismatch", False
    if packed == src:
        return f"skill {path}: SKILL.md matches {SKILL_SRC.as_posix()} ({len(src)} bytes)", True
    return (f"skill {path}: SKILL.md {len(packed)} bytes, {SKILL_SRC.as_posix()} {len(src)} bytes, mismatch; "
            f"rebuild the archive"), False


def main():
    ap = argparse.ArgumentParser(description="Check local links and anchors in a built site.")
    ap.add_argument("dir", nargs="?", default="site", metavar="DIR", help="the built site (default: site)")
    ap.add_argument("--base", default="/", help='URL path the site is served from (default "/")')
    ap.add_argument("--skill", default=SKILL_ZIP, metavar="FILE", help=f"the packaged skill to compare with {SKILL_SRC} (default: {SKILL_ZIP})")
    args = ap.parse_args()
    root = Path(args.dir)
    if not root.is_dir():
        sys.exit(f"{root}: not a folder")
    base = "/" + args.base.strip("/") + "/" if args.base.strip("/") else "/"

    pages = {}
    for path in sorted(root.rglob("*.html")):
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        pages[path.relative_to(root).as_posix()] = page

    misses = []

    def check(source, here, ref, count):
        """Resolve ref against here; count it and record a miss."""
        if EXTERNAL.match(ref):
            count["external"] += 1
            return
        count["links"] += 1
        url = urlsplit(urljoin(here, ref))
        path = unquote(url.path)
        rel = path[len(base):] if path.startswith(base) else None
        if rel is not None and (rel == "" or rel.endswith("/")):
            rel += "index.html"
        if rel is None or not (root / rel).is_file():
            count["missing"] += 1
            misses.append(f"{source} -> {ref}")
            return
        if url.fragment and rel.endswith(".html"):
            count["anchors"] += 1
            if unquote(url.fragment) not in pages[rel].anchors:
                count["anchors_missing"] += 1
                misses.append(f"{source} -> {ref}")

    site = dict.fromkeys(("links", "missing", "anchors", "anchors_missing", "external"), 0)
    for name, page in pages.items():
        here = ORIGIN + base + name
        if page.base is not None:
            here = urljoin(here, page.base)
        for ref in page.links:
            check(name, here, ref, site)

    # the search script puts index urls into pages as they are, so they resolve like any page's links
    index = dict(site, links=0, missing=0, anchors=0, anchors_missing=0, external=0)
    for ref in index_urls(root):
        check(INDEX, ORIGIN + base, ref, index)

    print(f"pages {len(pages)}, local links checked {site['links']}, missing {site['missing']}, "
          f"anchors checked {site['anchors']}, anchors missing {site['anchors_missing']}, "
          f"external skipped {site['external']}")
    print(f"index links checked {index['links']}, missing {index['missing']}, "
          f"anchors checked {index['anchors']}, anchors missing {index['anchors_missing']}")
    skill_line, skill_ok = skill_check(args.skill)
    print(skill_line)
    for miss in misses:
        print(miss)
    return 1 if misses or not skill_ok else 0


if __name__ == "__main__":
    sys.exit(main())
