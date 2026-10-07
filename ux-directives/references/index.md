# The Blue Book of UX Directives—Index

A Uniform Code for Human-Centered Digital Systems, by Aleh Haiko (https://www.alehhaiko.com/the-blue-book-of-ux-directives).

9 chapters, 62 subcategories, 555 directive IDs, including repealed ones. Directive IDs are `<chapter><subcategory>/<nn>` (e.g. `44/03` = ch. 4, subcat. 4.4, directive 3; subcategory 9.10 uses three-digit IDs like `910/05`).

## Preface

This book establishes a doctrine of **Human-Centered Systems Engineering** for the design, governance, and evolution of digital systems.

**How to read this book:** This is written as a **field manual**, not an essay—*terse*, *absolute*, and *command-form* by design. The register is deliberate: it is the doctrine language of the U.S. Army, where I served, carried into the discipline of human-centered systems.

- “*Directives are written to be met, not debated.*”
- “*A standard you can defer is not a standard.*”

The purpose of the book is to **codify enforceable standards** that can be consistently applied, tested, and upheld across teams and systems—serving, for now, as a scaffold for best practices rather than a showcase of their practical application, which is reserved for future work.

**This edition serves three functions:**

1. Defines non-negotiable, human-centered principles that must guide digital system behavior.
2. Provides operational directives for translating those principles into product requirements and engineering decisions.
3. Creates a shared organizational framework for evaluating, auditing, and evolving UX and AI-mediated systems.

> “Those who are in love with **practice without knowledge** are like the sailor who gets into a ship without rudder or compass and who never can be certain whither he is going. **Practice must always be founded on sound theory**.”
>
> **Leonardo da Vinci.** From “[The Notebooks of Leonardo Da Vinci](https://en.wikiquote.org/wiki/Leonardo_da_Vinci)”. I. Prolegomena and General Introduction to the Book on Painting (between 1480 and 1519).

## How this book is organized

**Two parts:** Chapters 1–8 codify principles that hold for any interactive system. They are arranged as layers of the interaction—the human, information, action, system behavior, visual form, coherence, trust, and evolution over time. A concept is governed in the earliest layer where it arises and referenced from later ones.

Chapter 9 stands apart by design. It governs systems whose behavior is probabilistic or changes through learning—systems that can be wrong in ways no fixed rule predicts. These principles are still forming and have not yet settled into industry standards, so they are kept separate rather than folded into the general chapters. Where a chapter 9 directive specializes a general one, the general directive still applies.

**Outcomes, laws, and practices:** Most subcategories govern a property of the system. A few govern something else and are placed where they apply: 1.7 Simplicity is the outcome of chapter 1; 3.5 User Efficiency is the goal of chapter 3, and 3.6 Fitts’s Law is the physical law it obeys; 6.4 Design System Integrity, 8.3 Observability, and 8.4 Validation are practices of the team that builds the system.

**Repealed directives:** A directive that duplicated another keeps its ID, is marked *Repealed*, and points to the directive that replaces it. IDs are never reused.

## General provisions

These provisions apply to every chapter. Directives that restate them locally are their applications.

1. **Proportionality.** The strength of every safeguard, signal, and explanation scales with the consequence of the action it governs.
2. **Automation rigor.** The more a system acts on its own, the stronger its oversight, explanation, and validation must be.
3. **Confirm only the irreversible.** Reversibility replaces confirmation; explicit confirmation is reserved for actions that cannot be undone.
4. **Automation is offered, not imposed.** Automation that reduces effort must remain optional and subordinate to user intent.

Use this index to pick the relevant subcategories, then read only the matching `chapter_N.md` file.

## Chapter 1: Human Cognition & Behavior—`chapter_1.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 1.1 | Attention & Focus | What users can attend to at any moment. | “Does your system occupy users’ attention only when it directly advances their goals?” | 11/01–11/09 |
| 1.2 | Cognitive Load | How much mental effort interaction demands. | “Does your system make users think unnecessarily during interactions?” | 12/01–12/10 |
| 1.3 | Recognition | Whether users can easily recognize instead of remember. | “Can users of your system interact correctly through recognition without relying on recall?” | 13/01–13/10 |
| 1.4 | Mental Models | How users believe a system works. | “Do users form accurate beliefs to predict your system’s behavior correctly?” | 14/01–14/09 |
| 1.5 | Metaphors | How abstract systems become understandable. | “Does this metaphor help users understand your system without introducing false assumptions?” | 15/01–15/09 |
| 1.6 | Learnability | How users progress from novices to competent users. | “Can users of your system achieve competency quickly without long-term penalties?” | 16/01–16/09 |
| 1.7 | Simplicity | An emergent outcome of disciplined design. | “Do users of your system find it easy to use?” | 17/01–17/09 |
| 1.8 | Decision-Making | How users choose between options. | “Can users of your system make sound choices without being overloaded or steered?” | 18/01–18/09 |

## Chapter 2: Information Architecture & Wayfinding—`chapter_2.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 2.1 | Information Hierarchy | What matters most and why. | “Is what matters most perceptually obvious to your users before they act?” | 21/01–21/09 |
| 2.2 | Discoverability | What systems reveal they can do. | “Can users of your system discover core capabilities without instruction?” | 22/01–22/09 |
| 2.3 | Navigation | How users move and stay oriented. | “Can users move in your system without losing orientation or context?” | 23/01–23/09 |
| 2.4 | Progressive Disclosure | How complexity is revealed safely. | “Does complexity in your system appear to users gradually without surprise or loss of control?” | 24/01–24/09 |
| 2.5 | State | What a system remembers for users. | “Does your system reliably remember and reveal state that affects users’ outcomes?” | 25/01–25/09 |
| 2.6 | Explorability | How users learn through safe exploration. | “Can users of your system safely learn by doing without fear of damage?” | 26/01–26/09 |
| 2.7 | Search & Labeling | How users find what they cannot see. | “Can users of your system find information by name, even when they do not know where it is?” | 27/01–27/09 |

## Chapter 3: Interaction Mechanics & Agency—`chapter_3.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 3.1 | Human-Interface Objects | What users act upon. | “Are all interactive objects in your system clearly defined, stable, and understandable?” | 31/01–31/08 |
| 3.2 | Affordances | How action is perceived. | “Are possible actions in your system perceptually obvious to users at the moment of use?” | 32/01–32/09 |
| 3.3 | Direct Manipulation | How action is executed. | “Can users of your system act directly on visible objects with safe, reversible results?” | 33/01–33/09 |
| 3.4 | Feedback | How action is confirmed. | “Does your system acknowledge users’ actions promptly and truthfully?” | 34/01–34/09 |
| 3.5 | User Efficiency | Why interaction quality matters. | “Does your system measurably reduce users’ time and effort for real tasks?” | 35/01–35/09 |
| 3.6 | Fitts’s Law | The governing physical constraint on all interaction. | “Are frequent or critical targets in your system fast and easy to acquire physically?” | 36/01–36/10 |
| 3.7 | Input | How users enter information. | “Can users of your system enter information quickly and correctly the first time?” | 37/01–37/09 |

## Chapter 4: System Behavior & Workflow Logic—`chapter_4.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 4.1 | Defaults | What a system chooses on users’ behalf. | “Do defaults in your system reliably help users without harming control or trust?” | 41/01–41/08 |
| 4.2 | Anticipation | What a system brings forward proactively. | “Does your system surface the next likely need for users without commandeering?” | 42/01–42/08 |
| 4.3 | Autonomy | How much control users retain. | “Do users of your system retain meaningful control over consequential actions?” | 43/01–43/09 |
| 4.4 | Error Prevention | How mistakes are avoided. | “Is it easier for users of your system to perform correct actions than incorrect ones?” | 44/01–44/09 |
| 4.5 | Recovery | How mistakes are repaired. | “Can users of your system recover from failure quickly without penalty or loss?” | 45/01–45/09 |
| 4.6 | Work Protection | How effort is preserved over time. | “Is user work protected in your system against interruption, failure, and error?” | 46/01–46/09 |
| 4.7 | Latency | How temporal constraints influence workflows. | “Does your system preserve user momentum under delay?” | 47/01–47/09 |

## Chapter 5: Visual Communication—`chapter_5.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 5.1 | Visual Hierarchy | What the eye sees first. | “Is priority in your system visually clear before reading?” | 51/01–51/09 |
| 5.2 | Contrast | What can be distinguished at all. | “Can users of your system distinguish important elements under real conditions?” | 52/01–52/08 |
| 5.3 | Readability | How easily content can be consumed. | “Can users of your system read and sustain comprehension effortlessly?” | 53/01–53/09 |
| 5.4 | Accessibility | Whether content can be perceived by all users. | “Can users with varied abilities perceive and act effectively in your system?” | 54/01–54/09 |
| 5.5 | Information Density | How much can be held in view. | “Is information density in your system calibrated for thinking, not scanning?” | 55/01–55/09 |
| 5.6 | Color Semantics | How meaning and state are reinforced. | “Do colors in your system communicate stable, trustworthy meaning?” | 56/01–56/08 |
| 5.7 | Functional Aesthetics | What drives emotional and credibility dimensions. | “Does visual design of your system support user trust and recede during work?” | 57/01–57/09 |
| 5.8 | Motion | How movement communicates change. | “Does motion in your system explain what changed without slowing or distracting users?” | 58/01–58/09 |

## Chapter 6: Consistency & Coherence—`chapter_6.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 6.1 | Consistency | How to preserve stable meaning over time. | “Can users of your system rely on learned behavior across time and context?” | 61/01–61/09 |
| 6.2 | Conventions | How systems align with external user expectations. | “Does your system honor established user expectations?” | 62/01–62/08 |
| 6.3 | Patterns | How to scale behavior without fragmentation. | “Does the growth of your system preserve user-learned patterns rather than replace them?” | 63/01–63/09 |
| 6.4 | Design System Integrity | How systems maintain coherence as they evolve. | “Will your system remain coherent as it evolves?” | 64/01–64/08 |

## Chapter 7: Trust, Safety & Responsibility—`chapter_7.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 7.1 | Consent & Control | Who decides and when. | “Do users of your system retain control over actions affecting them or their data?” | 71/01–71/09 |
| 7.2 | Transparency | Why systems behave as they do. | “Can users of your system understand and influence behavior when needed?” | 72/01–72/09 |
| 7.3 | Error Communication | How systems communicate when things go wrong. | “Does your system help users recover instead of assigning blame?” | 73/01–73/09 |
| 7.4 | Data Integrity | Whether data can be trusted. | “Can users of your system trust their data is safe, accurate, and handled as expected?” | 74/01–74/09 |
| 7.5 | Privacy | What happens to personal information. | “Do users of your system know and control what personal information it collects, keeps, and shares?” | 75/01–75/09 |
| 7.6 | Non-Manipulation | How the system influences user choices. | “Does your system influence users only in ways they would endorse if they saw how it works?” | 76/01–76/09 |

## Chapter 8: Adaptation & Evolution—`chapter_8.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 8.1 | Continuity | How understanding is preserved across updates. | “Can your system change without breaking user understanding or work?” | 81/01–81/09 |
| 8.2 | Scalability | Whether patterns survive growth. | “Does your interaction model remain understandable to users as it scales?” | 82/01–82/09 |
| 8.3 | Observability | How user behavior is measured. | “Can user-visible problems in your system be detected early on?” | 83/01–83/09 |
| 8.4 | Validation | How correctness is maintained over time. | “Is the design of your system continuously validated against real use?” | 84/01–84/10 |
| 8.5 | Personalization | How the system adapts to the individual. | “Does personalization in your system help each user without making the system unpredictable?” | 85/01–85/09 |

## Chapter 9: AI-Mediated Interaction—`chapter_9.md`

| # | Subcategory | Governs | Ask yourself | Directives |
|---|---|---|---|---|
| 9.1 | Human Oversight | Who remains accountable. | “Is human responsibility in your system explicit and exercisable at all times?” | 91/01–91/10 |
| 9.2 | Learning Consent | What a system may learn and apply. | “Do users of your system authorize what it learns from them and how it applies it?” | 92/01–92/09 |
| 9.3 | Predictability | Why stability matters more than surprise. | “Can users of your system reliably predict its behavior?” | 93/01–93/09 |
| 9.4 | Explainability | How results are understood. | “Can users understand and contest outcomes in your system?” | 94/01–94/09 |
| 9.5 | Confidence Signaling | How certainty and uncertainty are conveyed. | “Does your system signal uncertainty to users honestly and actionably?” | 95/01–95/09 |
| 9.6 | Graceful Failure | What happens when intelligence breaks. | “Does your system behave responsibly when intelligence fails?” | 96/01–96/09 |
| 9.7 | Provenance | What data influenced outcomes. | “Can users of your system see what data shaped an outcome and its scope?” | 97/01–97/09 |
| 9.8 | Bias Management | Where distortions may arise. | “Are sources of bias in your system visible and mitigable to users?” | 98/01–98/08 |
| 9.9 | Trust Calibration | How reliance is adjusted over time. | “Is user trust aligned with actual system capability over time?” | 99/01–99/09 |
| 9.10 | Non-Anthropomorphism | How to prevent false human attribution. | “Does your system present itself honestly to users as a tool, not a human agent?” | 910/01–910/09 |
