# UX Directives — Claude Skill

> A Claude skill that applies **The Blue Book of UX Directives** to design work: audits, design reviews, topic lookups and requirements — every finding cited by directive ID.

**Author: [Aleh Haiko](https://alehhaiko.com/)** · **Read the book: [alehhaiko.com/ux](https://alehhaiko.com/ux/)** · **Full guide: [Skill for Claude](https://alehhaiko.com/ux/skill.html)**

---

## What is this?

*The Blue Book of UX Directives: A Uniform Code for Human-Centered Digital Systems* — 9 chapters, 62 subcategories and 550 numbered, command-form directives (IDs like `32/02`), from human cognition to AI-mediated interaction. It is written as a field manual of Human-Centered Systems Engineering: terse, absolute, command-form.

The skill gives Claude the full text of the book. Claude then cites the exact directive, ID and title, instead of paraphrasing UX advice from memory. A finding becomes a rule anyone on the team can look up and check.

**What it can do**

- **Cite exactly.** The book is bundled whole, so the title is quoted, not recalled.
- **Find the directives for a topic** through an index of all 62 subcategories and their “Ask yourself” questions.
- **Audit what it is shown** — screenshots, code, specs, flows — as Violates / Evidence / Fix / Severity.
- **Write requirements** traced to directive IDs.
- **Explain any ID,** including the five repealed ones and what replaced them.

**What it cannot do**

- **See what it is not shown.** A state nobody opened stays unchecked.
- **Measure on its own.** Pixels, contrast and timing are measured only when the agent has a browser and uses it.
- **Know your history.** A deliberate decision looks like a defect unless it is listed as one.
- **Know thresholds the book does not state.** Pair it with [WCAG](https://www.w3.org/TR/WCAG22/).
- **Replace research.** Severity is a judgment by consequence, not data about your users.

Who it might be for, a worked example and how to make audits sharper: [Skill for Claude](https://alehhaiko.com/ux/skill.html).

---

## Install

### Claude.ai

1. Download [`ux-directives.skill`](https://github.com/AlehHaiko/UX-directives-skill/raw/main/ux-directives.skill). It is a zip of the [`ux-directives/`](./ux-directives) folder.
2. In Claude, open **Settings → Skills** and upload the file.
3. Make sure the skill is turned on.

Claude uses the skill on its own when a task calls for it. You don’t need to name it. Anthropic’s guide: [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### Claude Code

```
git clone https://github.com/AlehHaiko/UX-directives-skill.git
cp -R UX-directives-skill/ux-directives ~/.claude/skills/
```

`~/.claude/skills/` makes the skill available in all your projects. To share it with a team, put it in the repository’s `.claude/skills/` and commit it. Claude loads it when relevant, or you type `/ux-directives`. Docs: [Claude Code skills](https://code.claude.com/docs/en/skills).

---

## First prompts

**Audit:**

```
Audit our account settings screen against the UX Directives. [screenshot]
```

**Find by topic:**

```
We're redesigning onboarding — new users get a 9-step tour before they can do anything. What does the Blue Book say?
```

**Requirements:**

```
Write acceptance criteria for an LLM that drafts support replies the agent can send or edit.
```

**Explain an ID:**

```
What does directive 22/02 say, and how does it apply to an icon-only toolbar?
```

---

## The 9 chapters

| # | Chapter | Governs |
|---|---------|---------|
| 1 | **Human Cognition & Behavior** | Attention, cognitive load, recognition, mental models, metaphors, learnability, simplicity, decision-making |
| 2 | **Information Architecture & Wayfinding** | Information hierarchy, discoverability, navigation, progressive disclosure, state, explorability, search & labeling |
| 3 | **Interaction Mechanics & Agency** | Interface objects, affordances, direct manipulation, feedback, efficiency, Fitts's law, input |
| 4 | **System Behavior & Workflow Logic** | Defaults, anticipation, autonomy, error prevention, recovery, work protection, latency |
| 5 | **Visual Communication** | Visual hierarchy, contrast, readability, accessibility, information density, color semantics, aesthetics, motion |
| 6 | **Consistency & Coherence** | Consistency, conventions, patterns, design system integrity |
| 7 | **Trust, Safety & Responsibility** | Consent & control, transparency, error communication, data integrity, privacy, non-manipulation |
| 8 | **Adaptation & Evolution** | Continuity, scalability, observability, validation, personalization |
| 9 | **AI-Mediated Interaction** | Human oversight, learning consent, predictability, explainability, confidence, graceful failure, provenance, bias, trust calibration, non-anthropomorphism |

---

## Repository structure

```
UX-directives-skill/
├── README.md
├── LICENSE
├── ux-directives.skill        ← packaged skill (zip of ux-directives/)
├── ux-directives/             ← the skill
│   ├── SKILL.md               ← when and how Claude uses the book
│   └── references/
│       ├── index.md           ← map: chapters, subcategories, general provisions
│       └── chapter_1.md … chapter_9.md
├── site/                      ← the book as a static website (alehhaiko.com/ux/), generated
├── tools/
│   └── build_site.py          ← builds site/ from ux-directives/references/
├── CLAUDE.md                  ← instructions for Claude Code in this repository
└── .github/ISSUE_TEMPLATE/feedback.md
```

The previous version of the skill (a single `SKILL.md` that relied on project knowledge) is kept under the tag [`v1`](../../tree/v1).

---

## Website

[alehhaiko.com/ux](https://alehhaiko.com/ux/) is the book as a static website. Vercel publishes the `site/` folder on every push to `main`.

`site/` is generated: do not edit its HTML, CSS or JS by hand. Change the book in `ux-directives/references/*.md` (or the page templates, styles and scripts in `tools/build_site.py`), then rebuild from the repository root:

```
python3 tools/build_site.py
```

The script needs Python 3 and nothing else. It rewrites every page in `site/` and the files in `site/assets/`; the favicons in `site/assets/` are static and stay as they are.

---

## Contributing

The UX Directives is a living doctrine. If you have feedback on specific directives, encounter edge cases, or want to propose additions, open an issue using the feedback template or start a thread in [Discussions](https://github.com/AlehHaiko/UX-directives-skill/discussions).

---

## License

What can be given away without losing it must be free.

MIT — see [LICENSE](./LICENSE)

Favicon: the rocket emoji from [Noto Emoji](https://github.com/googlefonts/noto-emoji) by Google, used under its open-source license.
