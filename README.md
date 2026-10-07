# UX Directives — Claude Skill

> A Claude skill that applies **The Blue Book of UX Directives** to design work: audits, design reviews, topic lookups, and requirements — every finding cited by directive ID.

**Author: [Aleh Haiko](https://www.alehhaiko.com)** · **Read the book online: [lab.alehhaiko.com](https://lab.alehhaiko.com)**

---

## What is this?

*The Blue Book of UX Directives* is a field manual of Human-Centered Systems Engineering: 9 chapters, 62 subcategories and 550 numbered, command-form directives (IDs like `32/02`), from human cognition to AI-mediated interaction.

This skill bundles the full text of the book, so Claude cites exact directives instead of paraphrasing from memory. When it is installed, Claude will:

- **Audit designs, flows and specs** — each finding names the violated directive (ID and title), the evidence, the fix and a severity weighed by consequence.
- **Find the directives for a topic** — onboarding, errors, navigation, consent, AI explainability, and so on, grouped by subcategory.
- **Write requirements and acceptance criteria** traced to directive IDs.
- **Explain any directive by ID**, including repealed IDs and what replaced them.

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

## Install

Download [`ux-directives.skill`](./ux-directives.skill) from this repository and add it to Claude as a skill (in Claude's settings, where skills are managed). The file is a zip of the [`ux-directives/`](./ux-directives) folder, so you can also upload that folder zipped.

Claude uses the skill on its own when a task calls for it. You don't need to mention the skill by name.

---

## Example prompts

```
Audit our account settings screen against the UX Directives. [screenshot]
```

```
We're redesigning onboarding — new users get a 9-step tour before they can do anything. What does the Blue Book say?
```

```
Write acceptance criteria for an LLM that drafts support replies the agent can send or edit.
```

```
What does directive 22/02 say, and how does it apply to an icon-only toolbar?
```

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
├── site/                      ← the book as a static website (lab.alehhaiko.com)
└── .github/ISSUE_TEMPLATE/feedback.md
```

The previous version of the skill (a single `SKILL.md` that relied on project knowledge) is kept under the tag [`v1`](../../tree/v1).

---

## Contributing

The UX Directives is a living doctrine. If you have feedback on specific directives, encounter edge cases, or want to propose additions, please open an issue using the feedback template.

---

## License

MIT — see [LICENSE](./LICENSE)
