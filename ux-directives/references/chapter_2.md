# Chapter 2: Information Architecture & Wayfinding

> **How users locate information, orient themselves, and move through the system.**
>
> These govern how users navigate, explore, and progress through the system.

**Mission statement:** Help users locate information, orient themselves, and move through systems without confusion, disorientation, or unnecessary effort.

## 2.1 Information Hierarchy

> What matters most and why.

**Ask yourself:** “Is what matters most perceptually obvious to your users before they act?”

**Mission:** Ensure users see what matters first by organizing content by priority.

**Executive brief:** The system must make what matters most obvious before users act.

### Key heuristics

- Order of importance must be decided before presentation is designed.
- Information of unequal importance must be ranked, not presented as equal.
- Hierarchy must be structurally defined before it is visually styled.
- Levels of importance must be identifiable without extended scanning.
- Related information must be grouped to expose meaningful relationships.
- Visual hierarchy must reflect user goals rather than internal system organization.
- Emphasis must adjust to user state and task phase.
- Layout must make the next action perceptually evident.
- Priority patterns must remain stable across views.

### Core questions

- “What feels most important at a glance?”
- “Is that the right thing to emphasize?”

### Focus areas

- **Perceptual-first:** “What do users notice first, and why?” “Is the visual emphasis correct?”
- **Decision-support:** “Is key information clear immediately?” “Does the layout reduce searching and interpreting?”
- **Context-aware:** “Does importance shift appropriately with user context?” “Are visual cues consistent and predictable as context changes?”
- **AI-aware:** “Is priority obvious right away? Or only clear after explanation?” “Does the system adjust emphasis to context without becoming confusing?”

### Directives

- **21/01—Rank information by importance before rendering it.** Decide what is primary, secondary, and tertiary independent of visual styling; 5.1 governs how that order is shown.
- **21/02—Do not flatten unequal information.** Keep the order of importance intact in structure, sequence, and grouping.
- **21/03—Define structural hierarchy before applying visual styling.** Use typography, spacing, and color to reinforce, not replace, structural priority.
- **21/04—Make priority immediately visible.** Ensure users can identify primary, secondary, and tertiary information without scanning extensively.
- **21/05—Group related information to expose relationships.** Use spatial and structural grouping to reduce interpretation cost.
- **21/06—Align visual dominance with user goals.** Ensure hierarchy reflects user intent, not internal system structure.
- **21/07—Adapt hierarchy to context and user task phase.** Adjust emphasis as user state and goals change to support efficient workflow completion.
- **21/08—Use hierarchy to reduce navigation and decision overhead.** Design layouts so the next action is evident to users without additional exploration.
- **21/09—Keep the order of importance stable across views.** Prevent shifts in priority that force users to relearn where key information lives.

### Executive summary

- Information Hierarchy is perceptual priority, not decorative styling.
- It establishes importance through structure before relying on text or visual flourish.
- The system must rank unequal information before it is rendered.
- Hierarchy must align with user goals, not internal architecture.
- Grouping, consistency, and contextual emphasis are prerequisites of clear hierarchy.
- Hierarchy succeeds when users know where to look and what to do without searching or deliberation.

### Success indicators

- The most important information stands out immediately.
- Visual weight clearly reflects differences in importance.
- Related information is grouped so relationships are easy to see.
- The next action is easy to identify.
- Hierarchy remains consistent across screens.

**One-line summary:** Before users can choose, they must understand what matters most.

## 2.2 Discoverability

> What systems reveal they can do.

**Ask yourself:** “Can users of your system discover core capabilities without instruction?”

**Mission:** Ensure users find available actions by exposing system capabilities clearly.

**Executive brief:** The system must visibly reveal what it can do without requiring explanation.

### Key heuristics

- All necessary capabilities must be visibly accessible.
- Actionable elements must carry the signifiers governed in 3.2 Affordances.
- Hidden or gesture-based interactions must be explicitly indicated.
- Relevant actions must appear within the user’s current context.
- Progressive disclosure must not obscure advanced capability.
- Critical functionality must be directly discoverable.
- Actionability must be reliably discoverable before it is optimized for speed.
- Discoverability must foster a sense of mastery and control.

### Core questions

- “Can users see what they can do, right when they need to?”
- “If they are new, is it obvious what actions are available?”

### Focus areas

- **Perceptual-first:** “What looks clickable or usable right now?” “What clearly invites action? What does not?”
- **Anti-accidental discovery:** “Are features intentionally revealed, or only found by accident?” “Would a careful user still discover them?”
- **State-aware:** “Do available actions change clearly with context?” “Are options visible, or dependent on memory?”
- **AI-aware:** “Does AI clearly surface useful options, or make users guess?” “Are capabilities explicit, or only implied through behavior?”

### Directives

- **22/01—Ensure all necessary capabilities are visibly accessible.** Accelerate confident engagement and product adoption by helping users quickly understand what they can do without training.
- **22/02—Repealed.** Merged into 32/02—Provide clear signifiers for all actionable elements.
- **22/03—Repealed.** Merged into 32/03—Make interactive elements visually distinguishable.
- **22/04—Use hidden or gesture-based interactions only with explicit signaling.** Prevent discoverability issues for essential tasks by ensuring users know those actions exist.
- **22/05—Surface actions when they become relevant.** Ensure users can discover appropriate actions within context rather than through explanation.
- **22/06—Ensure progressive disclosure does not obscure access.** Advanced capability must remain clearly reachable as complexity unfolds.
- **22/07—Design for intentional discovery.** Make critical functionality directly discoverable, not dependent on chance exploration.
- **22/08—Prioritize discoverability before optimizing efficiency.** Ensure actionable elements are found reliably before improving speed.
- **22/09—Design discoverability to build user confidence.** Guide users so they feel a sense of mastery and control over product capabilities.

### Executive summary

- Discoverability is visible capability, not accidental discovery.
- It ensures users can see what they can do without instruction or guesswork.
- The system must make all essential actions perceptible and clearly signified.
- Progressive disclosure must manage depth without obscuring access.
- Discoverability must precede efficiency.
- Speed is meaningless if actions cannot be found.
- Discoverability succeeds when users engage confidently, knowing what is possible and how to act.

### Success indicators

- Available actions are visible and easy to notice.
- Users can tell what the system can do before they need it.
- Users can find important features without training or instructions.
- Relevant actions appear when they are needed.
- Users can discover new capabilities as they continue using the system.

**One-line summary:** Before users can act, they must perceive what is possible.

## 2.3 Navigation

> How users move and stay oriented.

**Ask yourself:** “Can users move in your system without losing orientation or context?”

**Mission:** Ensure users move through the system predictably by providing clear paths and structure.

**Executive brief:** The system must enable movement without disorientation.

### Key heuristics

- Navigation must preserve user orientation at all times.
- Current user position must remain perceptually evident.
- Navigational hierarchy and relationships must be perceivable without memorization.
- Navigation controls must be visually and behaviorally clear.
- Navigational depth must be limited to preserve clarity.
- Interfaces must favor stable places over constant relocation.
- User state and progress must persist across navigation.
- User orientation must be maintained even after the destination is reached.
- Navigation must recede as user expertise increases.

### Core questions

- “Do users always know where they are, where they can go, and how to return?”
- “Does movement feel continuous and clear?”

### Focus areas

- **Orientation-first:** “Is orientation preserved as users move?” “Can they navigate without rebuilding a mental map each time?”
- **Structure-aware:** “Is the system’s structure visible through navigation?” “Does moving around clarify the structure, or hide it?”
- **State-aware:** “Is context maintained as users move?” “What changes during navigation? Is that obvious?”
- **AI-aware:** “If navigation adapts, does it still preserve a sense of place?” “Are changes in navigation visible and predictable?”

### Directives

- **23/01—Design navigation to preserve orientation at all times.** Ensure user movement never compromises users’ understanding of where they are.
- **23/02—Make current location continuously visible.** Do not require users to infer their position within the navigation structure.
- **23/03—Expose navigational structure perceptually.** Ensure users can perceive hierarchy and relationships without memorization.
- **23/04—Make navigation controls visually and behaviorally explicit.** Avoid ambiguous elements that obscure navigation options.
- **23/05—Limit navigational depth and complexity.** Favor breadth with clarity over deeply nested structures.
- **23/06—Favor stable places over constant movement.** Bring tools and content to users rather than forcing them to relocate.
- **23/07—Maintain user context across navigation.** Ensure state, progress, and understanding persist during transitions.
- **23/08—Prioritize orientation over mere reachability.** Maintain users’ sense of orientation even after they reach their destination.
- **23/09—Design navigation to recede as mastery develops.** Empower users’ expertise while keeping navigation unobtrusive.

### Executive summary

- Navigation is preserved orientation, not mere movement.
- It ensures users always know where they are, where they can go, and how to return.
- The system must make location and structure continuously visible.
- Navigation must reduce memory and inference, not depend on them.
- Stable places, shallow structure, and preserved context are prerequisites of navigational clarity.
- Navigation succeeds when users move confidently without losing their sense of place.

### Success indicators

- Users can always see where they are in the system.
- The structure of the system is easy to understand.
- Navigation controls are visible and clearly recognizable.
- Users can move between sections without losing context.
- Navigation remains consistent across the system.

**One-line summary:** Before users can go, they must know where they are and what moving will do.

## 2.4 Progressive Disclosure

> How complexity is revealed safely.

**Ask yourself:** “Does complexity in your system appear to users gradually without surprise or loss of control?”

**Mission:** Ensure users access complexity as needed by revealing information incrementally.

**Executive brief:** The system must reveal complexity gradually while preserving user control.

### Key heuristics

- Progressive disclosure must determine when complexity is revealed, not whether it exists.
- Functionality required for immediate task completion must remain accessible.
- Users must control when deeper complexity is revealed.
- Additional layers of capability must be perceptible and foreseeable.
- Early layers must introduce structures reused at deeper levels.
- Advanced functionality must remain clearly reachable.
- Context must remain intact across expansion and collapse.
- Users must be able to defer advanced learning without penalty.
- Progressive disclosure patterns must remain predictable across contexts.

### Core questions

- “Is complexity revealed gradually and at the user’s pace?”
- “Do users stay in control of when and how depth appears?”

### Focus areas

- **Control-first:** “What appears next? Is the reason clear?” “Can users anticipate what will be revealed?”
- **Structure-aware:** “Does each layer prepare users for the next?” “Is deeper functionality easy to discover without being forced?”
- **Failure-aware:** “What happens if users are not ready for more complexity?” “Can they ignore advanced features without penalty?”
- **AI-aware:** “Does AI reveal deeper options in a predictable way?” “Does adaptation respect user control over time?”

### Directives

- **24/01—Treat progressive disclosure as a timing strategy.** Manage when complexity is exposed to users rather than hiding it.
- **24/02—Never defer what the current task requires.** Disclose progressively only what the task does not need now.
- **24/03—Allow users to control when deeper complexity is revealed.** Avoid automatic or unexpected expansion of interface depth.
- **24/04—Make additional depth perceptible and predictable.** Signal further capabilities clearly, enabling users to prepare adequately.
- **24/05—Design early layers to scaffold later complexity.** Ensure initial views introduce structures and concepts that are reused at deeper levels.
- **24/06—Ensure deeper functionality remains clearly reachable.** Prevent burying advanced capability behind obscure paths.
- **24/07—Preserve context across progressive disclosures.** Do not require users to mentally reconstruct hidden information when expanding or collapsing views.
- **24/08—Allow complexity to be deferred without cost.** Ensure users can postpone advanced learning without blocking progress.
- **24/09—Maintain consistent progressive disclosure patterns.** Use predictable reveal mechanisms across contexts and screens.

### Executive summary

- Progressive Disclosure is a timing strategy, not a concealment strategy.
- It manages when complexity is revealed without hiding what is essential.
- The system must keep core capability accessible while allowing users to control deeper exploration.
- Additional depth must be perceptible, predictable, and structurally consistent.
- Early layers must scaffold later complexity rather than fragment it.
- Progressive disclosure succeeds when complexity can be deferred without cost or loss of context.

### Success indicators

- Essential actions are visible and available from the start.
- Additional options are revealed only when users choose to explore further.
- The presence of deeper features is clearly signaled.
- Advanced capabilities remain easy to reach when needed.
- Users keep their context when expanding or collapsing details.

**One-line summary:** Before users can master complexity, they must first feel competent.

## 2.5 State

> What a system remembers for users.

**Ask yourself:** “Does your system reliably remember and reveal state that affects users’ outcomes?”

**Mission:** Ensure users understand system status by making current state visible.

**Executive brief:** The system must remember for users in ways they can see and trust.

### Key heuristics

- System state must relieve users of reconstructing context.
- Outcome-relevant state must be perceptible.
- State affecting user work must be viewable and understandable.
- Different state types must be behaviorally and visually distinguishable.
- All meaningful state changes must be clearly indicated.
- Stored context must be modifiable and resettable.
- State must survive interruption and navigation.
- Remembered state must clearly reflect user intent.
- Stored state must be safeguarded for integrity, security, and privacy.

### Core questions

- “What is the system remembering for users?”
- “Can they see it, understand it, and control it?”

### Focus areas

- **Visibility-first:** “What state exists right now? Where is it visible?” “If users leave and return, what will still be there?”
- **Continuity-aware:** “Can users resume exactly where they stopped?” “What survives interruption? What does not?”
- **Control-aware:** “Can users reset, edit, or override what is remembered?” “Is saved state helping users, or getting in the way?”
- **AI-aware:** “What is explicitly set versus inferred?” “Does adaptive memory stay clear and understandable over time?”

### Directives

- **25/01—Design state to offload user memory.** Ensure the system remembers context so users do not have to reconstruct it.
- **25/02—Make outcome-relevant state visible.** Do not allow hidden conditions to influence results without perceptible indications.
- **25/03—Make sure state is inspectable.** Ensure users can view and understand the state that affects their work.
- **25/04—Differentiate state types explicitly.** Distinguish local, session, and persistent states in both behavior and presentation.
- **25/05—Signal all meaningful state changes.** Prevent modifications to state without clear and timely feedback.
- **25/06—Make state reversible and resettable.** Provide clear mechanisms to modify or undo stored context.
- **25/07—Persist state across interruptions.** Ensure work and context survive pauses, navigation, and session breaks.
- **25/08—Align remembered state with user intent.** Do not preserve or apply state that contradicts user expectations or goals.
- **25/09—Treat state as protected user data.** Apply integrity, security, and privacy safeguards to stored context.

### Executive summary

- State is remembered context, not invisible system memory.
- It offloads user memory by preserving what affects outcomes and continuity.
- The system must make relevant state visible, inspectable, and understandable.
- State types and changes must be explicit, not silently inferred.
- State must be reversible, persistent across interruption, and aligned with user intent.
- State succeeds when users never have to reconstruct what the system should already know.

### Success indicators

- The system remembers user context so users do not rely on memory.
- Important state information is visible and easy to understand.
- Changes in state are clearly signaled.
- Users can review, modify, or reset system state when needed.
- Work and context persist across navigation, pauses, and interruptions.

**One-line summary:** Before users can decide what to do next, they must know what has already happened.

## 2.6 Explorability

> How users learn through safe exploration.

**Ask yourself:** “Can users of your system safely learn by doing without fear of damage?”

**Mission:** Ensure users can explore safely by enabling reversible actions and risk-free discovery.

**Executive brief:** The system must support safe, optional exploration without making discovery a prerequisite for use.

### Key heuristics

- Users must be able to explore without fear of irreversible harm.
- Every meaningful action must be recoverable.
- Essential workflows must not depend on hidden discovery.
- Users must always know where they are and how to return.
- System limits must be explicit and perceivable.
- Exploration must reinforce cause-and-effect understanding.
- Discovery must reveal system structure, not isolated features.
- Multiple valid paths must be allowed, but meaning must remain consistent.
- Exploration must never corrupt user context or system state.

### Core questions

- “Can users explore safely and learn by doing?”
- “Can they experiment and recover without risk or confusion?”

### Focus areas

- **Safety-first:** “Can users try things without damaging their work?” “Is recovery easy and reliable?”
- **Structure-aware:** “Are there clear paths and landmarks while exploring?” “Does exploration reveal how the system is organized?”
- **Optional depth:** “Can users succeed without exploring deeply?” “Is exploration encouraged but never required?”
- **AI-aware:** “Does AI make exploration smoother, or unpredictable?” “Can users preview or understand effects before committing?”

### Directives

- **26/01—Ensure exploration is safe by design.** Safeguard users from any risk of irreversible damage or loss while exploring the product.
- **26/02—Provide strong recovery mechanisms.** Support undo, previews, and reversibility as structural prerequisites for exploration.
- **26/03—Keep exploration optional for task completion.** Ensure essential workflows function independently of hidden discoveries.
- **26/04—Provide stable landmarks for orientation.** Allow users to identify their location and return paths during exploration.
- **26/05—Make system boundaries explicit.** Reveal limits, constraints, and unavailable paths clearly.
- **26/06—Foster user learning through interaction and its consequences.** Design exploration so users develop understanding through visible cause and effect.
- **26/07—Leverage exploration to reveal system structure.** Ensure discovery reinforces conceptual understanding rather than just isolated feature exposure.
- **26/08—Allow multiple valid paths where appropriate.** Support flexible interaction paths without compromising clarity.
- **26/09—Preserve state integrity during exploration.** Ensure experimentation does not disrupt context or create unintended side effects.

### Executive summary

- Explorability is safe learning through interaction, not risky trial and error.
- It allows users to investigate the system without fear of irreversible harm.
- The system must provide recovery, reversibility, and protected state as prerequisites for exploration.
- Exploration must reinforce understanding of structure, not just expose isolated features.
- Stable landmarks and explicit boundaries are required for confident movement.
- Explorability succeeds when users can learn freely without compromising progress, data, or intent.

### Success indicators

- Users can explore the system without risking damage or data loss.
- Actions can be undone or safely reversed.
- Users can always see where they are and how to return.
- System limits and unavailable paths are clearly indicated.
- Exploration helps users understand how the system works.

**One-line summary:** Before users can learn a system, they must feel free to try.

## 2.7 Search & Labeling

> How users find what they cannot see.

**Ask yourself:** “Can users of your system find information by name, even when they do not know where it is?”

**Mission:** Ensure users locate information directly by providing reliable search and labels that match their vocabulary.

**Executive brief:** The system must let users find content by what they call it, not by where it is stored.

### Key heuristics

- Labels must use the users’ vocabulary, not internal terminology.
- The same thing must carry the same label everywhere.
- Search must be available wherever content exceeds what navigation can expose.
- Search must tolerate misspellings, synonyms, and partial input.
- Search scope must be visible.
- Results must be ranked by relevance to the user’s task.
- Results must show enough context to choose without opening each one.
- Empty results must offer a way forward.
- Search must respect the same permissions and states as navigation.

### Core questions

- “Can users find something they cannot see, using their own words?”
- “Do labels mean the same thing everywhere?”

### Focus areas

- **Vocabulary-first:** “Whose words do the labels use?” “Would a new user guess the right term?”
- **Scope-aware:** “What does this search cover?” “Is it obvious when results are filtered?”
- **Result-aware:** “Can users pick the right result from the list alone?” “What happens when nothing matches?”
- **AI-aware:** “Is semantic search predictable?” “Can users tell retrieved results from generated answers?”

### Directives

- **27/01—Label in the users’ vocabulary.** Name content and actions with the terms users use, not internal or technical terms.
- **27/02—Keep labels stable and unique.** Use one label for one thing across the system.
- **27/03—Provide search where navigation cannot scale.** Offer search when content outgrows what navigation can expose.
- **27/04—Make search forgiving.** Match misspellings, synonyms, and partial queries.
- **27/05—Show search scope.** Indicate what is being searched and which filters apply.
- **27/06—Rank by task relevance.** Order results by what the user most likely needs, not by storage order.
- **27/07—Give results enough context.** Show the information needed to choose a result without opening it.
- **27/08—Make empty results actionable.** Suggest corrections, broader scopes, or alternative paths.
- **27/09—Align search with navigation.** Ensure search results respect the same permissions, states, and labels as navigation.

### Executive summary

- Search & Labeling is retrieval by name, not by location.
- It lets users reach content they cannot see or do not know the place of.
- The system must label everything in the users’ vocabulary and keep labels stable.
- Search must be forgiving, scoped, and ranked by task relevance.
- Results and empty states must let users choose or continue without guessing.
- Search & Labeling succeeds when users find what they need by naming it.

### Success indicators

- Labels use terms users recognize.
- Each item has one label across the system.
- Users find content with imperfect queries.
- Search scope and filters are visible.
- Empty results offer a next step.

**One-line summary:** Before users can find what they cannot see, the system must understand what they call it.

