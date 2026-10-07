# Chapter 1: Human Cognition & Behavior

> **How humans perceive, think, remember, and decide during interaction with the system.**
>
> These govern whether the interface can be understood at all.

**Mission statement:** Ensure systems respect the limits and strengths of human perception, attention, memory, and decision-making so interfaces can be understood and used with confidence.

## 1.1 Attention & Focus

> What users can attend to at any moment.

**Ask yourself:** “Does your system occupy users’ attention only when it directly advances their goals?”

**Mission:** Ensure users attend to what matters by prioritizing and timing signals appropriately, free from distraction or visual noise.

**Executive brief:** The system must earn users’ attention only when it clearly advances their goals.

### Key heuristics

- Attention must be justified by value.
- What matters now must dominate perception.
- Focus may be broken only to prevent greater harm.
- Attention must support forward movement.
- Primary tasks must come first unless background systems become crucial to outcomes.
- Task context must remain stable across interaction.
- Work resumption must be immediate and predictable.
- Motion must clarify state change.
- Calm must serve as a performance condition, not as decoration.

### Core questions

- “Does the system earn users’ attention when it asks for it?”
- “Are attention demands justified, clear, and timely?”

### Focus areas

- **Proportion-aware:** “Is this interruption justified?” “Is the demand on attention proportional to its value or risk?”
- **Action-aware:** “What must the user notice immediately? What can wait?” “Does the signal guide action, or just announce itself?”
- **Context-aware:** “Is attention aligned with the user’s current task or goals?” “Does timing respect what the user is doing rather than disrupt it?”
- **AI-aware:** “Why is this being surfaced now? What happens if it is ignored?” “Is this guidance or attention capture?”

### Directives

- **11/01—Require attention to be earned.** Do not introduce signals that do not justify their cognitive cost.
- **11/02—Prioritize relevance over visibility.** Emphasize what matters now and deliberately de-emphasize everything else.
- **11/03—Interrupt only when necessary.** Break focus solely when inaction would cause greater harm than interruption.
- **11/04—Guide attention toward action.** Use emphasis to support task progress, not novelty or decoration.
- **11/05—Enforce foreground–background discipline.** Keep background activity unobtrusive unless user outcomes depend on awareness.
- **11/06—Preserve task continuity.** Ensure users can always resume without questioning their previous state.
- **11/07—Design explicitly for re-entry.** Assume interruption and make recovery fast, clear, and predictable.
- **11/08—Use motion to clarify change.** Apply animated transitions only to explain state transitions, not to attract attention.
- **11/09—Treat calm as a functional requirement.** Use silence, restraint, and visual economy as active design tools.

### Executive summary

- Attention is a scarce resource that must be justified, not claimed.
- Responsibility for focus lies with the system, not the user.
- User attention must be earned by the system through relevance.
- The system is responsible for protecting user focus and task continuity.
- Any interruption or signal must justify its cost by directly advancing users’ work.
- Attention & Focus succeeds when users progress without distraction and resume without disorientation.

### Success indicators

- The primary task is unmistakable.
- Visual and behavioral hierarchy makes priorities clear.
- Competing signals are restrained.
- Interruptions occur only when justified and timely.
- Users can easily resume their task after interruption.

**One-line summary:** Before users can act effectively, they must clearly see what deserves their attention right now.

## 1.2 Cognitive Load

> How much mental effort interaction demands.

**Ask yourself:** “Does your system make users think unnecessarily during interactions?”

**Mission:** Ensure users can think efficiently by minimizing unnecessary mental effort.

**Executive brief:** The system must minimize users’ cognitive load by doing the work they do not need to think about.

### Key heuristics

- Interaction must operate within finite cognitive limits.
- Systems must assume users are already mentally occupied.
- Cognition must be directed toward user goals, not system mechanics.
- The system must remember whenever it reasonably can.
- Critical state must be perceptible without mental reconstruction.
- Correct action must not depend on guesswork.
- Predictability must convert reasoning into automated response.
- Tasks must not be fragmented or fatigued by unnecessary micro-decisions.
- Automation must reduce effort without increasing supervision.
- Design must account for cumulative cognitive cost.

### Core questions

- “What mental effort could the system handle but currently falls on the user?”
- “Who is doing the work? The user or the system?”

### Focus areas

- **Responsibility-first:** “What cognitive work is unnecessarily offloaded to the user?” “Where is the system failing to carry its share of thinking?”
- **Decision-aware:** “What must users remember, interpret, compare, or decide?” “What decisions exist only because the interface forces them?”
- **Efficiency-aware:** “Could mental effort be reduced with better design or automation?” “Are repeated or tedious tasks unnecessarily taxing users?”
- **AI-aware:** “What thinking persists despite automation?” “Is AI actually helping, or just showing intelligence without acting?”

### Directives

- **12/01—Design for finite cognitive capacity.** Do not demand sustained attention, memory, or decision-making beyond what is strictly necessary for the task.
- **12/02—Assume users are already cognitively occupied.** Design with cognitive courtesy as a baseline responsibility.
- **12/03—Minimize interface thinking.** Ensure users think about their work and goals, not about how the system operates.
- **12/04—Require the system to remember on users’ behalf.** Do not make users recall what the system can present for recognition.
- **12/05—Make state visible to reduce mental bookkeeping.** Do not hide information to avoid errors or uncertainty.
- **12/06—Eliminate interpretive burden.** Do not require guessing scope, state, or consequences in order to proceed correctly.
- **12/07—Use consistency to convert reasoning into habit.** Make system behavior predictable to replace conscious reasoning with habitual response.
- **12/08—Reduce decision density.** Keep users from making frequent or unnecessary micro-decisions within a single task flow.
- **12/09—Ensure automation removes work rather than adds supervision.** Do not introduce automation that requires constant monitoring, correction, or verification.
- **12/10—Design for sustained use.** Treat small inefficiencies as compounding costs that accumulate into fatigue over time.

### Executive summary

- Cognitive Load is the cost imposed on finite human cognitive resources.
- It must be minimized so users think about their goals, not about how the system works.
- Human cognitive capacity is easily exhausted.
- The system is responsible for minimizing unnecessary mental effort.
- Decision density and hidden conditions must be reduced to prevent cumulative fatigue.
- Cognitive Load succeeds when interaction feels effortless.

### Success indicators

- The task can be completed without unnecessary thinking about the interface.
- Information is visible so users do not need to rely on memory.
- System state and next steps are easy to understand.
- Decisions within the task are few and meaningful.
- Automation reduces work instead of adding supervision.

**One-line summary:** Before users can think about their goals, they must not be forced to think about the interface.

## 1.3 Recognition

> Whether users can easily recognize instead of remember.

**Ask yourself:** “Can users of your system interact correctly through recognition without relying on recall?”

**Mission:** Ensure users act through recognition by making options and states visible and eliminating recall burden and ambiguity.

**Executive brief:** The system must replace memory with visibility so users can act immediately.

### Key heuristics

- Action must be guided by recognition rather than recall.
- Known information must be presented directly, not recalled from memory.
- Outcome-relevant state must remain perceptible at all times.
- Choices must appear at the moment of decision.
- Consistent placement must reinforce recognition over time.
- Meaningful differences must be visually or behaviorally evident.
- Recovery paths must be visible and accessible.
- Returning users must reorient through visible cues, not memory.
- Visual economy must not remove essential cues.
- Visible cues must be favored over memory to keep interfaces usable at scale.

### Core questions

- “Can users act by recognition rather than recall?”
- “Does the system make the right information visible at the moment of choice?”

### Focus areas

- **Recognition-first:** “What is visible right away that would otherwise need to be remembered?” “Where is recall being required when recognition would work?”
- **Action-ready:** “Are options, state, and consequences clear at the moment of action?” “Can new or infrequent users act correctly without prior knowledge?”
- **Context-aware:** “Is recognition aligned with users’ current task and goals?” “Does the system surface relevant cues when and where they are needed?”
- **AI-aware:** “Does the system reveal what it knows instead of relying on user recall?” “Is intelligence being used to expose state, not to demand recall?”

### Directives

- **13/01—Favor recognition over recall.** Design interfaces so users can act by seeing and choosing rather than by remembering and reconstructing.
- **13/02—Substitute memory with perception wherever possible.** Present information whenever possible so users do not have to remember it.
- **13/03—Make action-relevant state continuously visible.** Do not hide state that influences outcomes or availability.
- **13/04—Expose choices at the point of decision.** Ensure users can see available options when they need to choose, not before or after.
- **13/05—Maintain spatial stability to reinforce recognition.** Keep controls and feedback in consistent locations so recognition replaces recall over time.
- **13/06—Make meaningful differences perceptible.** Do not require users to remember rules or exceptions to distinguish safe actions from risky ones.
- **13/07—Support error recovery through recognition.** Provide visible history and undo so users can recover without relying on memory.
- **13/08—Design for infrequent and returning use through recognition.** Ensure users can reorient and resume work without relying on memory or relearning prior knowledge.
- **13/09—Do not sacrifice recognition for minimalism.** Visual restraint must not remove cues users rely on to recognize actions, state, or structure.
- **13/10—Design recognition-based interfaces to scale.** Prefer recognition over training so usability does not degrade as systems grow in scope or complexity.

### Executive summary

- Recognition must replace recall as the primary interaction strategy.
- It allows users to act by seeing rather than remembering.
- Recognition is faster, safer, and more reliable than recall.
- The system must make key information visible at the moment of action.
- Immediate user action is the practical payoff of recognition.
- Recognition succeeds when users can orient, choose, and recover without relying on recall.

### Success indicators

- Users can act by seeing options, not remembering them.
- Information needed for action is visible when decisions are made.
- System state and available actions are easy to recognize.
- Controls and feedback appear in stable and predictable locations.
- Users can recover and resume work without relying on memory.

**One-line summary:** Before users can decide confidently, they must be able to recognize rather than remember.

## 1.4 Mental Models

> How users believe a system works.

**Ask yourself:** “Do users form accurate beliefs to predict your system’s behavior correctly?”

**Mission:** Ensure users can predict system behavior by aligning with their existing mental models.

**Executive brief:** The system must actively shape accurate mental models or users will form their own, often incorrect ones.

### Key heuristics

- System behavior must intentionally shape the mental model users form.
- Correct understanding must emerge from consistent interaction and feedback.
- Similar actions must produce similar outcomes across contexts.
- Users must be able to trace how actions lead to results.
- Behavior-influencing states must be visible.
- System behavior must align with user intuition, not technical convenience.
- Departures from established patterns must be prominent and justified.
- Metaphors must strengthen correct behavioral expectations.
- Mental models must support consistent recovery and cross-context application.

### Core questions

- “What do users think the system does?”
- “Does that understanding let them reason, predict, and recover correctly?”

### Focus areas

- **Responsibility-forward:** “What understanding is the interface teaching?” “What beliefs does it actively reinforce?”
- **Expectation-aligned:** “Can users reliably predict what will happen next?” “Does the system behave as they expect?”
- **Structure-aware:** “Does the interface reveal how the system works, not just outcomes?” “Are relationships, rules, and dependencies visible and understandable?”
- **AI-aware:** “What does the user think the system knows, decides, or controls?” “Does AI encourage accurate understanding or anthropomorphic illusion?”

### Directives

- **14/01—Design explicitly for the mental model users will form.** Do not allow users to infer core system behavior accidentally or inconsistently.
- **14/02—Design consistent system behavior to teach the correct mental model.** Do not rely on documentation to teach users the correct mental model.
- **14/03—Maintain consistent behavior to keep users’ mental models stable.** Similar actions must produce similar results across contexts.
- **14/04—Make causality visible and traceable.** Users must be able to perceive how actions lead to outcomes.
- **14/05—Make states visible when they influence behavior or outcome.** Avoid hidden conditions, as they corrupt learned mental models.
- **14/06—Design for behavioral coherence rather than technical convenience.** Prioritize behavior that is intuitive to users over internal system logic.
- **14/07—Make behavioral deviations explicit and justified.** Do not introduce unannounced changes to established patterns.
- **14/08—Design metaphors that reinforce correct mental models.** Avoid metaphors that teach incorrect rules about system behavior.
- **14/09—Design mental models that support recovery and transfer.** Ensure users can use their understanding to correct errors and apply knowledge across contexts.

### Executive summary

- Mental Models are explanatory structures users form about how the system works.
- They are inevitable and continuously active.
- Users form beliefs whether the system intends them to or not.
- Mental Models determine whether users can reason correctly about action and consequence.
- The system must teach the correct model through consistent behavior, not documentation.
- Mental Models succeed when users can predict outcomes, recover from errors, and transfer knowledge across contexts.

### Success indicators

- The system behaves in ways users can easily understand.
- Similar actions produce similar results across the system.
- Users can see how their actions lead to outcomes.
- Important system states are visible and easy to recognize.
- Users can use their understanding to fix mistakes and continue working.

**One-line summary:** Before users can trust the system, they must be able to reason about how it works.

## 1.5 Metaphors

> How abstract systems become understandable.

**Ask yourself:** “Does this metaphor help users understand your system without introducing false assumptions?”

**Mission:** Ensure users grasp new concepts by mapping them to familiar ones.

**Executive brief:** Metaphors must clarify the system, or they must not be used at all.

### Key heuristics

- Metaphors must only exist to improve understanding.
- Metaphors must enable correct reasoning about system behavior.
- Metaphors must not introduce false rules or expectations.
- Structural clarity must take precedence over literal resemblance.
- Metaphorical framing must match actual system outcomes.
- The limits of a metaphor must be perceptible through behavior.
- Metaphors must not create unwarranted confidence.
- Symbolic metaphors must be supported by consistent structural cues.
- Metaphors must evolve or be removed when they obstruct clarity or growth.

### Core questions

- “Does this metaphor help users understand the system accurately?”
- “Does it clarify how the system works, or mislead users?”

### Focus areas

- **Cognition-aware:** “What does this metaphor teach about how the system works?” “Does it improve or confuse the user’s mental model?”
- **Constraint-aware:** “Where does the metaphor break down?” “What false expectations might it create?”
- **Communication-aware:** “Is the metaphor clear and unambiguous to users?” “Does it highlight important concepts without misleading?”
- **AI-aware:** “Does this metaphor overstate intelligence, agency, or understanding?” “Is AI explaining behavior, or making the system seem human?”

### Directives

- **15/01—Use metaphors only to improve understanding.** Do not introduce metaphors solely for aesthetic purposes that do not clarify system behavior.
- **15/02—Ensure metaphors support accurate reasoning.** Allow users to infer correct behavior from metaphors, not merely recognize them, and avoid metaphors that introduce false constraints or misleading expectations.
- **15/03—Repealed.** Merged into 15/02—Ensure metaphors support accurate reasoning.
- **15/04—Prioritize functional clarity over literal realism.** Choose metaphors that reveal structure and causality.
- **15/05—Align metaphors with actual system consequences.** Do not allow metaphorical framing to suggest outcomes the system cannot produce.
- **15/06—Make the limits of metaphors clear through behavior.** Ensure users are not surprised when the system diverges from metaphorical expectations.
- **15/07—Remove metaphors that create false confidence.** Avoid metaphorical framing that increases misunderstanding or overconfidence.
- **15/08—Support abstract metaphors with strong structural cues.** Reinforce abstract framing so users can reliably anticipate system behavior.
- **15/09—Evolve or abandon metaphors that constrain growth.** Do not preserve metaphors that obstruct system understanding or capability.

### Executive summary

- Metaphors are cognitive scaffolds for reasoning, not decorative themes.
- They exist to improve understanding by revealing structure and causality.
- Every metaphor shapes how users reason about the system.
- The system must ensure metaphors support accurate inference about real consequences.
- Abstract metaphors require strong structural support to maintain clarity.
- Metaphors succeed when users reason correctly about the system without being constrained or deceived by the analogy.

### Success indicators

- Metaphors help users understand how the system works.
- The metaphor allows users to predict what actions will do.
- The metaphor does not create misleading expectations.
- The system behaves consistently with the metaphor it uses.
- Users can understand the system even when the metaphor reaches its limits.

**One-line summary:** Before users can understand a new system, they must be able to relate it to something they already know.

## 1.6 Learnability

> How users progress from novices to competent users.

**Ask yourself:** “Can users of your system achieve competency quickly without long-term penalties?”

**Mission:** Ensure users can reach competence quickly through progressive understanding.

**Executive brief:** The system must enable rapid learning without imposing long-term inefficiency.

### Key heuristics

- Systems must enable rapid progression to user competence.
- Early success must not undermine long-term efficiency.
- Capability must be reinforced through use, not instruction alone.
- Early guidance must enable eventual user independence.
- Complexity must unfold without concealing capability.
- Behavioral patterns must generalize across contexts for knowledge transfer.
- Errors must be recoverable to encourage exploration.
- Core behaviors must align with established expectations where appropriate.
- Guidance must decrease as competence increases.

### Core questions

- “Does the system help users get started quickly and keep improving over time?”
- “Does it support learning now without slowing users down later?”

### Focus areas

- **Lifecycle-focused:** “How fast can beginners become productive? How far can they grow?” “Does learning this system compound over time or level off?”
- **Design-responsibility:** “What does the interface teach through use?” “Where does it depend on extra explanations instead of clear design?”
- **Growth-aware:** “Does the system encourage ongoing skill development?” “Are learning opportunities aligned with users’ evolving goals?”
- **AI-aware:** “Does AI help users learn faster, or make them reliant on it?” “Is it teaching understanding, or just masking complexity?”

### Directives

- **16/01—Design for speed to user competence and ease of growth.** Measure learnability by how quickly and smoothly users become competent with the system.
- **16/02—Optimize beyond first-use success.** Ensure early success does not compromise long-term efficiency or mastery.
- **16/03—Enable learning through interaction.** Design workflows so capability is discovered and reinforced through use rather than dependent on instruction.
- **16/04—Design constraints that enable transition to user autonomy.** Ensure early guidance supports later independence without structural reset.
- **16/05—Reveal complexity progressively without concealing capability.** Advanced features must remain discoverable as user competence increases.
- **16/06—Use consistency to facilitate learning transfer.** Ensure system behaviors and interaction patterns generalize across contexts.
- **16/07—Make errors safe and recoverable.** Design error handling that encourages user experimentation and reduces hesitation.
- **16/08—Leverage familiar conventions and prior knowledge.** Align core system behaviors with existing user expectations where appropriate.
- **16/09—Adapt assistance to user competence growth.** Ensure guidance decreases as user expertise increases, avoiding permanent dependency.

### Executive summary

- Learnability is an accelerated path to competence, not superficial simplicity.
- It is a progression, not a moment, essential for rapid competence and ongoing growth.
- The system must enable learning through interaction without reliance on instruction.
- Safe exploration must be allowed, with any errors being understandable and recoverable.
- Consistency and familiar conventions support learning transfer and help reveal deeper complexity.
- Learnability succeeds when users transition from novice to expert without relearning the system.

### Success indicators

- New users can complete basic tasks quickly.
- Users learn how the system works through normal use.
- Features and capabilities become discoverable as users gain experience.
- Errors are safe and easy to recover from.
- Users become faster and more confident with continued use.

**One-line summary:** Before users can become proficient, they must be able to become competent quickly.

## 1.7 Simplicity

> An emergent outcome of disciplined design.

**Ask yourself:** “Do users of your system find it easy to use?”

**Mission:** Ensure users experience clarity by reducing unnecessary complexity while avoiding oversimplification or loss of capability.

**Executive brief:** True simplicity emerges from correct handling of cognition, not from visual minimalism.

### Key heuristics

- Simplicity must emerge from structural clarity, not visual reduction.
- Systemic complexity must be reduced before visual complexity.
- Task flows must minimize unnecessary user choices.
- Core capabilities must remain clearly visible and accessible.
- System clarity must not depend on user memory, search, or inference.
- Complexity must be revealed progressively without hiding essentials.
- System behavior must remain consistent and expected.
- User context must remain intact across interaction.
- Clarity and efficiency must endure under prolonged use.

### Core questions

- “Does the system truly reduce complexity, or just push it onto the user?”
- “Does it feel simple, calm, and reliable over time?”

### Focus areas

- **Anti-illusion:** “Is the system genuinely simple, or merely hiding complexity?” “What complexity was actually removed, and what was just shifted?”
- **Confidence-preserving:** “Can users act without guessing or double-checking?” “Does the system behave predictably?”
- **Transparency-aware:** “Are the system’s operations and decisions clear to users?” “Can they see how complexity is being handled or automated?”
- **AI-aware:** “Does AI make tasks easier, or add new mental work?” “Does automation clarify what to do, or create hidden complexity?”

### Directives

- **17/01—Treat simplicity as a structural outcome, not a visual treatment.** Design for clarity of structure and workflow rather than surface minimalism.
- **17/02—Simplify underlying workflows before simplifying screens.** Prioritize removing systemic complexity over masking it visually.
- **17/03—Reduce decision density rather than feature count.** Minimize unnecessary user choices within task flows.
- **17/04—Keep essential capabilities visible and accessible.** Do not conceal functionality required for successful use.
- **17/05—Do not create cosmetic minimalism by shifting cost to users.** Ensure system simplicity does not rely on user memory, search, or guesswork.
- **17/06—Use progressive disclosure to manage depth without hiding essentials.** Ensure advanced system capability is accessible without compromising clarity.
- **17/07—Ensure predictable and consistent behavior.** Avoid unexpected outcomes that disrupt user understanding.
- **17/08—Preserve user context and continuity.** Prevent unnecessary context loss across actions and transitions.
- **17/09—Design simplicity for sustained interaction.** Ensure system clarity and user efficiency hold under prolonged use.

### Executive summary

- Simplicity is structural clarity, not surface minimalism.
- It is achieved by removing systemic complexity, not by hiding it.
- The system must absorb complexity so users do not have to.
- Predictable behavior and preserved context are prerequisites of simplicity.
- It emerges when cognitive load, memory, learning, and structure are handled correctly.
- Simplicity succeeds when clarity and efficiency endure under prolonged, real-world use.

### Success indicators

- Tasks can be completed without unnecessary steps.
- Choices within a task are limited and clear.
- Important features remain visible and easy to access.
- System behavior is predictable and easy to understand.
- Users can complete work without confusion or extra effort.

**One-line summary:** Before users can feel confident, the system must not demand unnecessary effort.

## 1.8 Decision-Making

> How users choose between options.

**Ask yourself:** “Can users of your system make sound choices without being overloaded or steered?”

**Mission:** Ensure users decide well by presenting options, trade-offs, and consequences in a form they can compare.

**Executive brief:** The system must structure choices so users can compare them, not merely see them.

### Key heuristics

- The number of simultaneous options must stay within what users can compare.
- Options must be presented in comparable terms.
- Trade-offs between options must be explicit.
- Consequences of each option must be visible before commitment.
- The order and framing of options must not bias the choice.
- Decisions that can be deferred must not be forced.
- Irreversible decisions must be separated from routine ones.
- Previous choices must be available as reference.
- Recommended options must state why they are recommended.

### Core questions

- “Can users compare options and understand what each will lead to?”
- “Is the choice the user’s, or has the interface already made it?”

### Focus areas

- **Comparison-first:** “Are options shown in the same terms and units?” “Can users see differences without switching views?”
- **Consequence-aware:** “Is the outcome of each choice visible before it is made?” “Which choices are irreversible?”
- **Bias-aware:** “Does order, size, or default pre-select an option?” “Is the framing neutral?”
- **AI-aware:** “Are recommendations explained?” “Can users decide against the recommendation without friction?”

### Directives

- **18/01—Limit simultaneous options.** Present no more choices at once than users can meaningfully compare.
- **18/02—Present options in comparable terms.** Use the same attributes, units, and order for every option.
- **18/03—Make trade-offs explicit.** Show what each option gains and what it gives up.
- **18/04—Show consequences before commitment.** Ensure users see what each choice will do before they make it.
- **18/05—Neutralize choice architecture.** Do not let order, emphasis, or framing push users toward an option the system prefers.
- **18/06—Allow decisions to be deferred.** Do not force a choice that the task does not yet require.
- **18/07—Separate consequential decisions from routine ones.** Make irreversible choices visually and behaviorally distinct.
- **18/08—Keep prior decisions available.** Let users see what they chose before and why.
- **18/09—Justify recommendations.** State the reason for any recommended option and keep alternatives equally reachable.

### Executive summary

- Decision-Making is structured comparison, not a list of options.
- It allows users to weigh alternatives by their consequences.
- The system must present options in comparable terms with explicit trade-offs.
- Choice architecture must inform without steering.
- Consequential decisions must be distinct from routine ones and deferrable when possible.
- Decision-Making succeeds when users choose confidently and would choose the same again with full information.

### Success indicators

- Users can compare options without switching views.
- Trade-offs and consequences are visible before a choice is made.
- Option order and emphasis do not favor the system’s preference.
- Irreversible choices are clearly distinguished.
- Recommendations come with reasons and visible alternatives.

**One-line summary:** Before users can choose well, options must be comparable and consequences visible.

