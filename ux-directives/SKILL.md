---
name: ux-directives
description: Apply "The Blue Book of UX Directives: A Uniform Code for Human-Centered Digital Systems" by Aleh Haiko — 550 numbered, command-form UX directives (IDs like 32/02) in 9 chapters, from human cognition to AI-mediated interaction. Use this skill whenever the user asks to audit, review, or critique a UI, screen, flow, prototype, screenshot, PRD, spec, or AI feature against UX principles; asks which principles or directives apply to a design problem (onboarding, errors, navigation, forms, notifications, defaults, consent, privacy, AI explainability, confidence, trust); wants UX requirements or acceptance criteria written; or mentions the Blue Book, "UX directives", or a directive ID — even if they do not name the book.
---

# The Blue Book of UX Directives

A doctrine of Human-Centered Systems Engineering written as a field manual: terse, absolute, command-form. Every directive has a stable ID and is meant to be met, not debated. Use it to judge designs and to state requirements, and always cite the exact directives you rely on, so the reader can look them up and the claim can be checked.

## Files

- `references/index.md` — start here. Preface, how the book is organized, the four **general provisions**, and one table per chapter with every subcategory: what it governs, its "Ask yourself" question, and its directive ID range. It is small enough to read whole and is the map for everything else.
- `references/chapter_1.md` … `chapter_9.md` — the chapters. Read only the ones the task needs; together they are large.

| Chapter | File | Covers |
|---|---|---|
| 1 Human Cognition & Behavior | `chapter_1.md` | attention, cognitive load, recognition, mental models, metaphors, learnability, simplicity, decision-making |
| 2 Information Architecture & Wayfinding | `chapter_2.md` | hierarchy, discoverability, navigation, progressive disclosure, state, explorability, search & labeling |
| 3 Interaction Mechanics & Agency | `chapter_3.md` | interface objects, affordances, direct manipulation, feedback, efficiency, Fitts's law, input |
| 4 System Behavior & Workflow Logic | `chapter_4.md` | defaults, anticipation, autonomy, error prevention, recovery, work protection, latency |
| 5 Visual Communication | `chapter_5.md` | visual hierarchy, contrast, readability, accessibility, density, color semantics, aesthetics, motion |
| 6 Consistency & Coherence | `chapter_6.md` | consistency, conventions, patterns, design system integrity |
| 7 Trust, Safety & Responsibility | `chapter_7.md` | consent & control, transparency, error communication, data integrity, privacy, non-manipulation |
| 8 Adaptation & Evolution | `chapter_8.md` | continuity, scalability, observability, validation, personalization |
| 9 AI-Mediated Interaction | `chapter_9.md` | human oversight, learning consent, predictability, explainability, confidence, graceful failure, provenance, bias, trust calibration, non-anthropomorphism |

### How a chapter file is laid out

Each chapter opens with `# Chapter N: Title`, an intro and a mission statement. Each subcategory is a `## N.M Name` section with the same blocks in the same order: a `> Governs` line, **Ask yourself**, **Mission**, **Executive brief**, `### Key heuristics`, `### Core questions`, `### Focus areas`, `### Directives`, `### Executive summary`, `### Success indicators`, **One-line summary**.

Directive lines look like this:

```
- **32/02—Provide clear signifiers for all actionable elements.** Attach meaningful visual cues to all interactive elements.
```

The ID is `<chapter><subcategory>/<number>`: `32/02` is chapter 3, subcategory 3.2, directive 2. Subcategory 9.10 uses three digits (`910/05`). To jump to one directive, search the chapter file for its ID (for example `grep -n "32/02" references/chapter_3.md`); to find directives by theme, search the chapter files for a keyword.

## Rules of use

These keep answers faithful to the book; each exists because a reader will check the citation.

1. **Cite exactly.** Quote the ID and the directive title verbatim, as in `32/02—Provide clear signifiers for all actionable elements.` Never invent an ID, merge two directives into one, or paraphrase a title into something the book does not say. If nothing in the book covers a point, say so plainly instead of stretching a directive to fit.
2. **Repealed IDs.** Five IDs are repealed: `15/03`, `22/02`, `22/03`, `94/06`, `94/09`. Each points to the directive that replaced it. If one is asked about or would apply, give the replacement and say it replaces the repealed ID. Never cite a repealed directive as live.
3. **General provisions apply everywhere.** Proportionality, automation rigor, "confirm only the irreversible", and "automation is offered, not imposed" (see `index.md`) govern every chapter. Use them to weigh findings: a safeguard that is too heavy for a low-stakes action is a finding too, not only a missing one.
4. **The earliest layer governs.** Chapters 1–8 are layers of one interaction (human → information → action → system behavior → visual form → coherence → trust → evolution). When the same concern shows up in several chapters, cite the earliest layer as the rule and the later ones as its applications.
5. **Chapter 9 only for probabilistic or learning systems.** Use it when the system's output can be wrong in ways no fixed rule predicts (LLM features, recommendations, predictions, systems that learn from users). Where a chapter 9 directive specializes a general one, the general directive still applies — cite both.
6. **Keep the register.** Directives are imperatives. When you turn them into requirements or fixes, keep them concrete and testable rather than softening them into suggestions.

## Workflows

### Explain or look up a directive

Find its chapter from the first digit of the ID, search the file for the ID, and give the title and body verbatim, then the subcategory it belongs to (name and what it governs) and, if useful, its sibling directives. If the ID is repealed, follow rule 2.

### Find the directives for a topic

1. Read `references/index.md` and pick the subcategories whose "Governs" and "Ask yourself" match the topic. Topics usually span several layers; for example, onboarding touches 1.6 Learnability, 2.2 Discoverability, 2.4 Progressive Disclosure and 4.1 Defaults.
2. Read only those subcategories in the chapter files.
3. Answer grouped by subcategory: the subcategory's "Ask yourself" question, then the directives that matter for this case with IDs and titles, each with one line on how it applies here. Prefer the few that decide the case over a long list.

### Audit a design, flow, or spec

Follow the steps in order. Each one closes a way an audit goes wrong: directives matched by title alone, hidden content taken as visible, a directive stretched to fit, the same ID both violated and met.

1. **Know the artifact and the source.** Identify the user's task, the states shown, and what the system does on its own. Name the source you have: a *text conversion* (fetched or extracted text), the *page source* (markup, styles, scripts), or the *rendered page* (a screenshot, a live view, a prototype). A text conversion flattens closed menus, collapsed panels and off-screen content into what reads like visible text; treat such content as visible only when the markup or a rendering confirms it.
2. **Pick subcategories by their questions.** Read `references/index.md` and put each subcategory's "Ask yourself" question to the artifact. Pick the subcategories whose question the artifact raises, not the ones whose name or directive titles match a keyword.
3. **Read each picked section in full before any verdict.** In the chapter file, read the subcategory's `## N.M` section: the `> Governs` line, **Ask yourself**, and every directive under `### Directives`, title and body. The body says what the directive requires; a title alone does not. A subcategory whose section you have not read in full goes neither into Coverage nor into a citation.
4. **Judge against the text.** For each directive that bears on the artifact, decide: violated, met, or not checkable from this source. Cite a directive only when its text, as written, covers the evidence. If nothing in the book covers a point, say so (rule 1).
5. **Self-check before output.** Go through the draft and fix it until every line holds:
   - Each cited directive: reread its title and body; they describe the evidence given. If not, re-cite or drop it.
   - No ID is both in the findings and in Already meets. A directive met in one place and violated in another is a finding; its Evidence says where it is met.
   - Already meets is held to the same bar as findings: concrete evidence from the source you saw that satisfies the directive as written. The absence of a visible problem is not evidence that a directive is met.
   - Every ID exists in the book, and every title is verbatim.
   - Every finding that rests only on a text conversion is marked.
6. **Report** in this form unless the user asks for another:

```
Source: <text conversion | page source | rendered page> — <what exactly: URL, file, screenshot>

| # | Finding | Directive | Severity |
|---|---|---|---|
| 1 | <short name of the problem> | <ID>—<directive title> | High |

### 1. <Short name of the problem>
Evidence: <what is visible or written that shows it — concrete, from the source>
Fix: <the specific change that would satisfy the directive>

### Coverage
| Subcategory | What was checked |
|---|---|
| <N.M Name> | <the parts of the artifact put to its question> |

### Already meets
- <ID>—<directive title>: <the evidence that meets it>

### Not checked
- <what the source did not show, for example error states missing from a screenshot>
```

Sort the table by severity: High, then Medium, then Low, judged by consequence to the user (general provision 1: proportionality). Evidence and Fix follow in the table's order, one block per `#`. A finding that rests only on a text conversion carries `(text conversion only)` in its Finding cell and its Evidence. When the source is a text conversion, Not checked says that it may include content hidden on the page, such as closed menus and collapsed panels. List anything you could not see as not checked instead of guessing.

### Write requirements or acceptance criteria

Turn each relevant directive into a testable statement that keeps its ID as the trace, for example: `[44/04] Invalid input is flagged at the field as soon as it is entered, before the user submits the form.` Use the subcategory's **Success indicators** as a source for measurable criteria.

## Source

Aleh Haiko, *The Blue Book of UX Directives: A Uniform Code for Human-Centered Digital Systems* — https://alehhaiko.com/ux/
