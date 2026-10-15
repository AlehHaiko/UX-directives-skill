# CLAUDE.md

This repository holds *The Blue Book of UX Directives* by Aleh Haiko in two forms:

- `ux-directives/` — a Claude skill: `SKILL.md` plus the full book in `references/` (`index.md`, `chapter_1.md` … `chapter_9.md`).
- `site/` — the book as a static website, read at https://alehhaiko.com/ux/. Vercel publishes it on every push to `main` at https://ux-directives.vercel.app, and the portfolio site proxies `/ux/` to that address. `site/vercel.json` (the Vercel project's Root Directory is `site`, so a `vercel.json` at the repository root is never read) holds redirects only: every path on the old host `lab.alehhaiko.com` goes to the same path under https://alehhaiko.com/ux/ (308).

`ux-directives.skill` is a zip of `ux-directives/` for installing the skill in Claude.

## Source of truth

The Markdown in `ux-directives/references/` is the only source of the book's text. The skill and the website both come from it.

- To change the book, edit the Markdown, then rebuild the site.
- To change the website's layout, styles or behavior, edit `tools/build_site.py` (templates, CSS and JS live in it), then rebuild.
- Never edit files in `site/` by hand, except the static favicons in `site/assets/` (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`) and `site/vercel.json`. The build does not write or remove these; it overwrites everything else.

Rebuild from the repository root (Python 3, no dependencies):

```
python3 tools/build_site.py
```

This is the normal build: it is made for `/ux/` (`--base` defaults to `/ux/`). Pages link to each other relatively, so the base shows in one place only, `<base href="/ux/">` in `404.html`; every page but `404.html` carries `<link rel="canonical">` with its address under https://alehhaiko.com/ux/. `--base PATH` builds for another path.

`--out PATH` writes the complete site (pages, assets and copies of the favicons) to another folder instead of `site/`; it combines with `--base` and refuses a non-empty folder that has no `index.html`.

The build prints the page count (73 pages: 1 home, 9 chapters, 62 subcategories, 1 skill page). If it changes, a chapter or subcategory heading was added, renamed or removed.

`skill.html` ("Skill for Claude") is the one page that is not the book: what the skill does, how to install it and how to audit with it. Its text and its three diagrams live in `tools/build_site.py` (`SKILL_*`, `scheme_*`, `render_skill`); it is not in the search index.

## After changing the Markdown

Rebuild `ux-directives.skill` so the packaged skill matches the folder:

```
rm -f ux-directives.skill && zip -r -X -D ux-directives.skill ux-directives -x '*.DS_Store'
```

**Version.** The skill's version is the line `Version X.Y.Z` directly under the first heading of `ux-directives/SKILL.md`. The build reads it and shows `(vX.Y.Z)` beside both download links on `skill.html`; without the line the build stops and writes nothing. A branch that changes anything in `ux-directives/` raises the version in that same branch: a wording edit raises the third digit (`1.1.1` → `1.1.2`), a change in how the skill behaves raises the second (`1.1.1` → `1.2.0`). Then rebuild `ux-directives.skill` and the site.

## Checks

There are no automated tests. These are the checks, in the order the work rules use them.

**Quick check (every pass).** From the repository root:

```
python3 tools/build_site.py && git diff --stat
```

Healthy output: `Built 73 pages: 1 home, 9 chapters, 62 subcategories, 1 skill page; 555 directive IDs indexed.` `site/` then holds 74 HTML files: the 73 pages plus `404.html`. The diff touches only the files the pass meant to change (a template or CSS/JS change rewrites all 73 pages and `site/assets/`; that is expected).

**Link check (every pass, with the quick check).** From the repository root:

```
python3 tools/check_links.py --base /ux/
```

Healthy output, three lines:

```
pages 74, local links checked 8481, missing 0, anchors checked 2045, anchors missing 0, external skipped 456
index links checked 617, missing 0, anchors checked 555, anchors missing 0
skill ux-directives.skill: SKILL.md matches ux-directives/SKILL.md (10826 bytes)
```

The first line covers every `href` and `src` in the HTML pages, the second every `url` in `assets/search-index.js`. Each miss follows as a `file -> target` line, and the exit code is 1. The third line compares `SKILL.md` inside `ux-directives.skill` with `ux-directives/SKILL.md` byte for byte; on a mismatch it names both sizes and the exit code is 1: rebuild the archive. `--skill FILE` checks another archive. The byte count changes with `SKILL.md`. External links are counted, never fetched; the 73 canonical links are among them. `--base /ux/` is the base `site/` is built for: without the flag the links of `404.html` are reported missing (83). For a build made with `--out PATH`, run `python3 tools/check_links.py PATH --base /ux/`. The counts change when the book or the templates gain or lose links; `missing` stays 0.

**Local preview.** `file://` loads pages without CSS and JS, so serve the folder:

```
python3 -m http.server 8000 -d site
```

Open `http://localhost:8000/`. Check at 360px wide and at desktop width, in light and dark themes. `404.html` resolves its links under `/ux/`, so served this way, from the root, it has no styles; to see it, serve the folder under `/ux/`.

**Review by the owner (the "ready for check" step).** Push the branch. Vercel builds a preview for every branch except `main`:

```
https://ux-directives-git-<branch>-alehhaiko-6562s-projects.vercel.app/
```

Previews require being signed in to Vercel. A preview serves the site from its root, so its 404 page has no styles; that is expected. The fingerprint is the short hash of the branch's last commit (`git rev-parse --short HEAD`); report it with "Ready for check".

**Release.** After the owner's go, fast-forward `main` to the branch and push. Vercel publishes `main` within a minute; the book is then at https://alehhaiko.com/ux/.

**Skill release.** A merge that changes anything in `ux-directives/` ends with a tag and a GitHub release of the version in `SKILL.md`, with `ux-directives.skill` attached. On `main`, after the push, for version `X.Y.Z`:

```
git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z
gh release create vX.Y.Z ux-directives.skill --title "vX.Y.Z" --notes "..."
```

The notes say what changed for someone using the skill. A merge that leaves `ux-directives/` alone gets no tag and no release.

**Commits.** Use the owner's time zone: `TZ=America/Los_Angeles git commit ...`.

## Book conventions

- Directive IDs are `<chapter><subcategory>/<number>`, for example `32/02`; subcategory 9.10 uses `910/05`. IDs are stable: never renumber.
- Repealed IDs (`15/03`, `22/02`, `22/03`, `94/06`, `94/09`) stay in the text with a pointer to their replacement.
- Em dashes are unspaced (`word—word`).
- Directives are imperative, terse and absolute. Keep that register.

## Reviewing the website

Use the `ux-directives` skill to audit the site against the book itself: findings cite directive IDs in the format given in `ux-directives/SKILL.md`.
