# Chapter 6: Consistency & Coherence

> **How systems remain predictable, learnable, and unified as they scale.**
>
> These enable learning transfer and reduce friction at scale.

**Mission statement:** Make systems predictable and learnable by preserving coherence across interactions, patterns, and time as products scale.

## 6.1 Consistency

> How to preserve stable meaning over time.

**Ask yourself:** “Can users of your system rely on learned behavior across time and context?”

**Mission:** Ensure users predict outcomes by maintaining stable behavior and meaning.

**Executive brief:** The system must preserve stable meaning as it evolves.

### Key heuristics

- Learned interaction patterns must transfer across contexts without reinterpretation.
- Behavioral consistency must take precedence over visual uniformity.
- Unnecessary behavioral variation must be eliminated.
- Similar actions must produce similar results.
- Departures from standard patterns must be clearly indicated.
- Meaningful behavioral shifts must be communicated and justified.
- Interaction logic must remain stable across sessions and versions.
- Consistency must be governed across the entire system.
- Personalization must not alter fundamental interaction rules.

### Core questions

- “Does what users learn today stay valid across the system and over time?”
- “Will similar actions behave the same way next time?”

### Focus areas

- **Behavior-first:** “Does this act the same way everywhere?” “Are similar elements treated consistently?”
- **Change-aware:** “When behavior changes, is that made clear?” “Are existing mental models respected or disrupted?”
- **System-wide:** “Does consistency hold across screens, states, and devices?” “Is consistency intentional or accidental?”
- **AI-aware:** “Does adaptive behavior maintain core invariants?” “Does learning improve outcomes without breaking expectations?”

### Directives

- **61/01—Preserve learned behavior across contexts.** Ensure interaction patterns transfer without reinterpretation.
- **61/02—Prioritize behavioral consistency over visual uniformity.** Do not allow identical appearances to mask different behaviors.
- **61/03—Eliminate unnecessary behavioral variation.** Prevent forcing users to re-evaluate familiar patterns.
- **61/04—Design for predictable interaction outcomes.** Ensure similar actions yield similar results.
- **61/05—Make exceptions explicit.** Indicate clearly when standard patterns do not apply.
- **61/06—Introduce changes transparently and deliberately.** Communicate and justify meaningful shifts in behavior.
- **61/07—Maintain consistency across sessions and versions.** Preserve interaction logic for returning users.
- **61/08—Govern consistency at system scale.** Prevent isolated design decisions that conflict with global patterns.
- **61/09—Preserve core interaction invariants in adaptive systems.** Ensure personalization does not alter fundamental rules.

### Executive summary

- Consistency is preserved behavioral logic, not visual uniformity.
- It allows learned interaction patterns to transfer without reinterpretation.
- The system must ensure similar actions produce similar outcomes across contexts and time.
- Exceptions and changes must be explicit, deliberate, and justified.
- Consistency must be governed at system scale, even in adaptive or personalized environments.
- Consistency succeeds when users rely on prior knowledge without hesitation or surprise.

### Success indicators

- Similar actions produce similar results across the system.
- Interaction patterns behave the same in different contexts.
- Users do not need to relearn familiar actions.
- Exceptions to patterns are clearly indicated.
- Behavior remains stable across sessions and updates.

**One-line summary:** Before users can operate confidently, they must be able to rely on what they have already learned.

## 6.2 Conventions

> How systems align with external user expectations.

**Ask yourself:** “Does your system honor established user expectations?”

**Mission:** Ensure users transfer prior knowledge by aligning with familiar standards.

**Executive brief:** The system must honor established conventions to preserve user trust.

### Key heuristics

- Interaction must align with established platform conventions.
- Conventional interaction patterns must be used to reduce onboarding friction.
- Familiar visual forms must match their expected behavior.
- Conventional and non-conventional patterns must not be mixed without clear boundaries.
- Departures from convention must provide clear functional benefit.
- Unconventional behavior must be clearly signaled and confined.
- Primary and high-frequency workflows must adhere to convention.
- Conventional behavior must extend consistently across supported input methods.

### Core questions

- “Does the system follow familiar platform conventions?”
- “Are users’ prior expectations respected, not broken?”

### Focus areas

- **Trust-transfer:** “Can users rely on what they already know?” “Is familiarity honored or violated?”
- **Scope-aware:** “Where does the system intentionally diverge?” “Are deviations obvious and justified?”
- **Consistency-aware:** “Are patterns consistent across the system, not just within a single platform?” “Does interface behavior match learned expectations?”
- **AI-aware:** “Does adaptive behavior preserve platform norms?” “Is novelty overriding what users already know?”

### Directives

- **62/01—Align with established platform conventions.** Design in accordance with shared behavioral expectations.
- **62/02—Leverage familiar interaction patterns.** Use conventional behaviors to reduce onboarding friction.
- **62/03—Ensure behavioral fidelity to conventional forms.** Do not replicate familiar visuals without matching expected behavior.
- **62/04—Apply conventions consistently.** Do not mix conventional and non-conventional patterns without clear boundaries.
- **62/05—Deviate from conventions only with clear benefit.** Ensure convention departures improve function meaningfully.
- **62/06—Signal deviations clearly and confine them locally.** Make unconventional behavior obvious and contained.
- **62/07—Prioritize convention adherence in primary workflows.** Protect high-frequency tasks from unnecessary novelty.
- **62/08—Use conventions to maintain cross-modality consistency.** Ensure conventional behavior extends to all supported inputs.

### Executive summary

- Conventions are shared behavioral expectations, not stylistic mimicry.
- They reduce cognitive load by leveraging what users already know.
- The system must honor established patterns in behavior, not just appearance.
- Deviations from convention must provide clear functional benefit and be explicitly signaled.
- Primary workflows must prioritize adherence to convention over novelty.
- Conventions succeed when familiarity accelerates competence without sacrificing clarity or control.

### Success indicators

- The interface follows familiar platform patterns.
- Common actions behave as users expect.
- Visual patterns match the behavior users anticipate.
- Unconventional behavior is clearly indicated.
- Primary workflows rely on familiar interaction patterns.

**One-line summary:** Before users can understand a system quickly, it must respect what they already know.

## 6.3 Patterns

> How to scale behavior without fragmentation.

**Ask yourself:** “Does the growth of your system preserve user-learned patterns rather than replace them?”

**Mission:** Ensure users scale understanding by reusing interaction solutions.

**Executive brief:** The system must scale by reusing patterns, not by teaching new ones.

### Key heuristics

- Recurring structures must preserve learned behavior.
- Reused visuals must preserve their associated interaction logic.
- Existing patterns must be reused unless they cannot serve the need.
- Patterns must remain consistent across contexts.
- Patterns must function reliably in varied situations.
- New capability must extend established patterns without breaking logic.
- Departures from established patterns must be intentional and clearly signaled.
- Meaningful changes to patterns must be clearly communicated.
- Patterns must be formalized as shared system contracts.

### Core questions

- “Does the system reuse proven solutions so new features feel familiar?”
- “Can the system grow without breaking what users already know?”

### Focus areas

- **Learning-transfer:** “Where can users apply what they have already learned?” “Do new features reuse existing interaction logic?”
- **Structure-aware:** “Is complexity added through repetition or invention?” “Are new surfaces composed of familiar parts?”
- **Consistency-aware:** “When patterns evolve, is the change made explicit?” “Are old patterns deprecated responsibly?”
- **AI-aware:** “Does generative UI respect established patterns?” “Is variation constrained by pattern rules?”

### Directives

- **63/01—Use patterns to preserve learned behavior.** Design recurring structures to reduce reinterpretation.
- **63/02—Ensure behavioral consistency within patterns.** Do not reuse visuals without preserving interaction logic.
- **63/03—Prefer reuse over unnecessary invention.** Introduce new patterns only when existing ones cannot serve the need.
- **63/04—Apply patterns comprehensively across contexts.** Prevent fragmenting pattern logic within the system.
- **63/05—Design patterns for cross-context scalability.** Ensure recurring structures function reliably in varied situations.
- **63/06—Extend patterns incrementally during growth.** Add capability without breaking established logic.
- **63/07—Limit and signal deviations from established patterns.** Ensure exceptions are intentional and explicit.
- **63/08—Evolve patterns transparently.** Communicate meaningful pattern changes to prevent forced relearning.
- **63/09—Formalize patterns as shared system contracts.** Maintain documentation to preserve coherence across teams.

### Executive summary

- Patterns are reusable interaction contracts, not recurring visual motifs.
- They preserve learned behavior by stabilizing structure and logic across contexts.
- The system must reuse and extend patterns before inventing new ones.
- Pattern behavior must remain consistent, scalable, and comprehensively applied.
- Deviations and evolutions must be intentional, explicit, and governed at system scale.
- Patterns succeed when growth adds capability without forcing users to relearn how the system works.

### Success indicators

- Recurring interactions follow the same structure and behavior.
- Similar tasks use the same patterns across the system.
- Visual patterns match consistent interaction behavior.
- New features reuse existing patterns whenever possible.
- Changes to established patterns are clear and intentional.

**One-line summary:** Before a system can scale, interaction solutions must be reusable and recognizable.

## 6.4 Design System Integrity

> How systems maintain coherence as they evolve.

**Ask yourself:** “Will your system remain coherent as it evolves?”

**Mission:** Ensure system coherence by enforcing shared components and rules while avoiding affordance drift.

**Executive brief:** The system must maintain coherent behavior as it scales.

### Key heuristics

- Internal consistency must be maintained before scope is expanded.
- Components must be anchored in explicit governing principles.
- System standards must translate into real constraints in design and code.
- The system must provide clear paths for adding new patterns without fragmentation.
- Governance mechanisms must be clear, efficient, and actionable.
- System changes must be deliberate, documented, and communicated.
- Standards must endure under rapid expansion and deadline pressure.
- Accumulating inconsistencies must be tracked, documented, and refactored regularly.

### Core questions

- “Does the design system stay coherent as the product and teams grow?”
- “Will it hold together over time?”

### Focus areas

- **Governance-first:** “Can teams extend the system without breaking it?” “Is there a clear, maintainable path for change?”
- **Stress-aware:** “Does the design system degrade gracefully under pressure?” “Will high-pressure situations cause divergence or preserve consistency?”
- **Adoption-aware:** “Is it easier for teams to follow the system than bypass it?” “Does the system encode decisions, not just components?”
- **AI-aware:** “Do generative tools respect system constraints?” “Is AI output bounded by system rules?”

### Directives

- **64/01—Prioritize systemic coherence over breadth.** Maintain internal consistency before expanding scope.
- **64/02—Define and enforce governing principles.** Anchor components in stable rules, not isolated artifacts.
- **64/03—Make system standards enforceable.** Ensure guidelines translate into constraints in design and code.
- **64/04—Enable safe extension of the system.** Provide structured paths to add new patterns without fragmentation.
- **64/05—Establish clear and efficient governance mechanisms.** Balance oversight with practicality for contributors.
- **64/06—Manage and communicate system changes transparently.** Ensure updates are deliberate and documented.
- **64/07—Design systems to withstand rapid growth and deadlines.** Ensure standards remain intact under institutional pressure.
- **64/08—Monitor and address accumulating design debt.** Refactor inconsistencies regularly before fragmentation accelerates.

### Executive summary

- Design System Integrity is systemic coherence, not component accumulation.
- It preserves governing principles as the foundation of all extensions and growth.
- The system must enforce standards through constraints in both design and code.
- Extensions and changes must be structured, transparent, and governed deliberately.
- Integrity must withstand rapid growth, deadlines, and institutional pressure.
- Design System Integrity succeeds when expansion strengthens coherence without causing fragmentation.

### Success indicators

- Components follow the same rules across the system.
- Design and code implementations remain aligned.
- New components extend the system without breaking existing patterns.
- Changes to the system are documented and communicated.
- The system remains consistent as the product grows.

**One-line summary:** Before coherence can be preserved at scale, it must be actively protected.
