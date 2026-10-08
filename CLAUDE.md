# CLAUDE.md

This repository holds *The Blue Book of UX Directives* by Aleh Haiko in two forms:

- `ux-directives/` — a Claude skill: `SKILL.md` plus the full book in `references/` (`index.md`, `chapter_1.md` … `chapter_9.md`).
- `site/` — the book as a static website, published by Vercel at https://lab.alehhaiko.com on every push to `main`.

`ux-directives.skill` is a zip of `ux-directives/` for installing the skill in Claude.

## Source of truth

The Markdown in `ux-directives/references/` is the only source of the book's text. The skill and the website both come from it.

- To change the book, edit the Markdown, then rebuild the site.
- To change the website's layout, styles or behavior, edit `tools/build_site.py` (templates, CSS and JS live in it), then rebuild.
- Never edit files in `site/` by hand, except the static favicons in `site/assets/` (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`). The next build overwrites everything else.

Rebuild from the repository root (Python 3, no dependencies):

```
python3 tools/build_site.py
```

`--out PATH` writes the complete site (pages, assets and copies of the favicons) to another folder instead of `site/`; it combines with `--base` and refuses a non-empty folder that has no `index.html`.

The build prints the page count (72 pages: 1 home, 9 chapters, 62 subcategories). If it changes, a chapter or subcategory heading was added, renamed or removed.

## After changing the Markdown

Rebuild `ux-directives.skill` so the packaged skill matches the folder:

```
rm -f ux-directives.skill && zip -r -X -D ux-directives.skill ux-directives -x '*.DS_Store'
```

## Checks

There are no automated tests. These are the checks, in the order the work rules use them.

**Quick check (every pass).** From the repository root:

```
python3 tools/build_site.py && git diff --stat
```

Healthy output: `Built 72 pages: 1 home, 9 chapters, 62 subcategories; 555 directive IDs indexed.` `site/` then holds 73 HTML files: the 72 pages plus `404.html`. The diff touches only the files the pass meant to change (a template or CSS/JS change rewrites all 72 pages and `site/assets/`; that is expected).

**Local preview.** `file://` loads pages without CSS and JS, so serve the folder:

```
python3 -m http.server 8000 -d site
```

Open `http://localhost:8000/`. Check at 360px wide and at desktop width, in light and dark themes.

**Review by the owner (the "ready for check" step).** Push the branch. Vercel builds a preview for every branch except `main`:

```
https://ux-directives-git-<branch>-alehhaiko-6562s-projects.vercel.app/
```

Previews require being signed in to Vercel. The fingerprint is the short hash of the branch's last commit (`git rev-parse --short HEAD`); report it with "Ready for check".

**Release.** After the owner's go, fast-forward `main` to the branch and push. Vercel publishes `main` to https://lab.alehhaiko.com within a minute.

**Commits.** Use the owner's time zone: `TZ=America/Los_Angeles git commit ...`.

## Book conventions

- Directive IDs are `<chapter><subcategory>/<number>`, for example `32/02`; subcategory 9.10 uses `910/05`. IDs are stable: never renumber.
- Repealed IDs (`15/03`, `22/02`, `22/03`, `94/06`, `94/09`) stay in the text with a pointer to their replacement.
- Em dashes are unspaced (`word—word`).
- Directives are imperative, terse and absolute. Keep that register.

## Reviewing the website

Use the `ux-directives` skill to audit the site against the book itself: findings cite directive IDs in the format given in `ux-directives/SKILL.md`.
