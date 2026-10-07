# Chapter 3: Interaction Mechanics & Agency

> **How users act on systems and exercise control through interaction.**
>
> These determine whether interaction is physically, perceptually, and temporally efficient, and whether users feel in control.

**Mission statement:** Enable users to act on systems efficiently, predictably, and with a clear sense of control over their actions and outcomes.

## 3.1 Human-Interface Objects

> What users act upon.

**Ask yourself:** “Are all interactive objects in your system clearly defined, stable, and understandable?”

**Mission:** Ensure users can act on interface elements by making objects identifiable and operable.

**Executive brief:** The system must provide clear, stable human-interface objects that users can understand and act upon confidently.

### Key heuristics

- Interaction must be organized around objects users can reason about.
- Exposed objects must align with user understanding, not internal storage models.
- Each object must maintain a clear and singular conceptual identity.
- Meaningful objects must be visible or inspectable in interaction.
- Available actions must correspond to the object’s conceptual type.
- Distinct behaviors must be represented by distinct objects.
- Interaction patterns must consistently reinforce what an object represents.
- Established object behavior must remain stable over time.

### Core questions

- “What objects does the system show? What does each mean?”
- “Can users identify and understand each object clearly?”

### Focus areas

- **Mental-model first:** “What can users point to and recognize as a distinct ‘thing’?” “What entities does the interface teach users to think with?”
- **Action-sensitive:** “What actions belong to this object alone?” “What changes when the user acts on it?”
- **Error-prevention:** “Could objects be confused with one another?” “Does any object behave inconsistently or ambiguously?”
- **AI-aware:** “Is the object acting, or just being acted upon?” “Does it suggest intelligence or agency it does not have?”

### Directives

- **31/01—Design interaction around user-reasonable objects.** Structure the interface according to objects users can reason about.
- **31/02—Model objects for user reasoning, not system storage.** Expose conceptual objects that align with user understanding rather than internal data structures.
- **31/03—Ensure each object has a clear and stable identity.** Do not assign multiple conflicting meanings to a single object.
- **31/04—Make meaningful objects visible or inspectable.** Avoid invisible entities in core interactions.
- **31/05—Align actions with object type.** Ensure available actions are consistent with the object’s conceptual identity.
- **31/06—Separate objects when behavior diverges.** Do not overload one object with incompatible interaction rules.
- **31/07—Ensure behavior reinforces object identity.** Use consistent interaction patterns to teach what an object represents.
- **31/08—Maintain predictable object behavior over time.** Do not alter interaction rules for established objects.

### Executive summary

- Human-Interface Objects are conceptual entities for user reasoning, not reflections of internal data structures.
- They define what the user can act upon and how the system is understood.
- The system must model objects according to user-reasonable concepts, not storage logic.
- Each object must have a clear, stable identity with actions consistent with its type.
- Object visibility and inspectability are prerequisites of correct interaction.
- Human-Interface Objects succeed when behavior consistently reinforces what an object is and what can be done with it.

### Success indicators

- Interface objects represent things users can easily understand.
- Each object has a clear and stable identity.
- Important objects are visible or easy to inspect.
- Available actions match what the object represents.
- Objects behave consistently across the system.

**One-line summary:** Before users can act with confidence, they must know what they are acting on.

## 3.2 Affordances

> How action is perceived.

**Ask yourself:** “Are possible actions in your system perceptually obvious to users at the moment of use?”

**Mission:** Ensure users know how to act by signaling possible actions clearly.

**Executive brief:** The system must make possible actions immediately perceivable without instruction.

### Key heuristics

- Possible actions must be perceptually evident without instruction.
- All actionable elements must carry clear visual cues.
- Interactive elements must be visually distinguishable from informational content.
- Static elements must not display visual cues that suggest interactivity.
- Disabled options must be immediately recognizable as non-actionable.
- Similar actions must share consistent visual and behavioral cues.
- Affordances must allow confident action without prior conceptual mastery.
- Clear affordances must reduce reliance on memory and guesswork.
- Affordances must remain clearly perceivable as system complexity grows.

### Core questions

- “What actions are immediately visible and actionable?”
- “Can users tell what they can do at a glance?”

### Focus areas

- **Perceptual-first:** “What invites interaction without explanation?” “What looks clickable or usable?”
- **Error-prevention:** “Which actions are possible? Which are not?” “Could anything be mistaken for an action it is not?”
- **State-aware:** “Do affordances update clearly when state changes?” “Are disabled or unavailable actions easy to distinguish?”
- **AI-aware:** “Does adaptive behavior stay visibly actionable?” “Are changes in available options perceptible?”

### Directives

- **32/01—Design affordances to be perceptually evident.** Ensure users can immediately understand possible actions without instruction.
- **32/02—Provide clear signifiers for all actionable elements.** Attach meaningful visual cues to all interactive elements to clearly convey their affordances.
- **32/03—Make interactive elements visually distinguishable.** Use deliberate styling and spacing to clearly distinguish interactive elements from informational content.
- **32/04—Eliminate false affordances.** Do not present elements as interactive if they do not respond to action.
- **32/05—Visually distinguish unavailable actions.** Ensure disabled or inapplicable options are clearly indicated.
- **32/06—Maintain consistent affordance patterns.** Use uniform visual and behavioral cues for similar actions.
- **32/07—Enable safe action before full understanding.** Design affordances so users can act confidently without prior conceptual mastery.
- **32/08—Use affordances to minimize memory and guesswork.** Leverage clear affordances to reduce cognitive load so users do not have to recall.
- **32/09—Ensure affordances remain legible as complexity increases.** Prevent action cues from degrading under density or scale.

### Executive summary

- Affordances are perceptible action possibilities, not decorative styling.
- They allow users to understand what can be done without instruction or recall.
- The system must make all actionable elements visibly and behaviorally evident.
- False or ambiguous affordances corrupt trust and increase cognitive load.
- Consistent, distinguishable cues are prerequisites of reliable interaction.
- Affordances succeed when users can act safely and confidently, even before full understanding.

### Success indicators

- Possible actions are easy to recognize at a glance.
- Interactive elements clearly look interactive.
- Non-interactive elements do not appear clickable or actionable.
- Unavailable actions are clearly indicated.
- Similar actions use consistent visual and behavioral cues.

**One-line summary:** Before users can act correctly, they must perceive how action is possible.

## 3.3 Direct Manipulation

> How action is executed.

**Ask yourself:** “Can users of your system act directly on visible objects with safe, reversible results?”

**Mission:** Ensure users feel in control by enabling immediate interaction with objects.

**Executive brief:** The system must enable direct, safe, and controllable action on human-interface objects.

### Key heuristics

- Interactions must be built around visible, understandable objects, not hidden commands.
- The gap between user intent and system action must be minimal.
- Scope and consequence must be visible before execution.
- Feedback must be immediate and sustained during manipulation.
- System response must preserve the perception of control.
- Required motor precision must correspond to risk and frequency.
- Interaction modes must not shift invisibly.
- Actions must be recoverable through dependable undo and correction mechanisms.
- Reversibility must replace excessive confirmation gating.

### Core questions

- “Can users act directly on what they see, and undo it if needed?”
- “Do actions feel immediate and reversible?”

### Focus areas

- **Perceptual-first:** “Can users see something, act on it, and instantly see the result?” “Does it feel like direct manipulation rather than issuing commands?”
- **Safety-first:** “Can users explore without fear of permanent mistakes?” “Is undo easy and always available?”
- **Control-aware:** “Does the system respond right away?” “Is the impact of an action clear before it is finalized?”
- **AI-aware:** “Does AI support user control rather than override it?” “Can automated actions be paused or stopped?”

### Directives

- **33/01—Design interactions around visible objects.** Build interactions on objects that users can see and understand, not hidden or abstract commands.
- **33/02—Minimize abstraction between intent and action.** Reduce mental translation required to achieve outcomes.
- **33/03—Make scope and consequence visible before action.** Ensure users understand what will be affected prior to execution.
- **33/04—Provide immediate and continuous feedback.** Maintain tight feedback loops during user manipulation.
- **33/05—Ensure responsive interaction latency.** Preserve the perception of control through timely system response.
- **33/06—Match required precision to consequence.** Avoid demanding fine motor accuracy for low-risk or common actions.
- **33/07—Minimize or eliminate hidden interaction modes.** Ensure users do not unknowingly switch behavioral contexts.
- **33/08—Make actions reversible.** Provide reliable undo or recovery mechanisms.
- **33/09—Favor reversibility over confirmation gating.** Design systems so undo replaces excessive confirmation dialogs.

### Executive summary

- Direct Manipulation is visible, continuous interaction with meaningful objects, not abstract command entry.
- It minimizes the distance between user intent and system effect.
- The system must make scope, consequence, and feedback perceptible before and during action.
- Responsive latency and matched precision are prerequisites of perceived control.
- Hidden modes and invisible context shifts undermine directness and trust.
- Direct Manipulation succeeds when users feel in control because action and outcome remain tightly coupled and reversible.

### Success indicators

- Users interact with visible objects, not hidden commands.
- The effect of an action is clear before it is performed.
- The system responds immediately to user actions.
- Feedback appears continuously as users manipulate objects.
- Actions can be easily undone or reversed.

**One-line summary:** Before users can feel in control, they must be able to act directly on what they see.

## 3.4 Feedback

> How action is confirmed.

**Ask yourself:** “Does your system acknowledge users’ actions promptly and truthfully?”

**Mission:** Ensure users understand outcomes by providing timely and clear responses.

**Executive brief:** The system must acknowledge actions clearly and respond in ways users can trust.

### Key heuristics

- Every meaningful user action must produce a visible system response.
- Acknowledgment must occur without delay.
- Feedback must indicate that user intent was understood and accepted.
- Feedback must communicate what changed, not merely that activity occurred.
- Feedback must clarify what was affected before and after execution.
- Distinct outcomes must produce distinct feedback signals.
- Feedback must represent state accurately and proportionally.
- Essential feedback must remain visible until resolved.
- Feedback must include clear next steps when errors occur.

### Core questions

- “Does the system acknowledge actions clearly, quickly, and accurately?”
- “Can users understand and rely on what happened?”

### Focus areas

- **Timing-first:** “Was the system’s response immediate?” “Was there any doubt about whether the action succeeded?”
- **Meaning-first:** “Does feedback explain what actually happened?” “Can users distinguish success, partial success, or failure?”
- **Trust-first:** “Is uncertainty communicated honestly?” “Does feedback ever mislead by omission?”
- **AI-aware:** “Is the system’s confidence proportional to its certainty?” “Does feedback distinguish guesses from facts?”

### Directives

- **34/01—Acknowledge every user action.** Ensure all meaningful actions produce visible system responses.
- **34/02—Provide immediate acknowledgment.** Respond to actions without delay to prevent duplicate input and uncertainty.
- **34/03—Confirm user intent explicitly.** Indicate the system understood and accepted the intended action.
- **34/04—Ensure feedback conveys meaningful outcome.** Communicate what changed or occurred, not merely that activity happened.
- **34/05—Make scope and consequence explicit in feedback.** Clarify what was affected before and after execution.
- **34/06—Differentiate feedback by outcome.** Use distinct signals for success, partial completion, warning, and failure states.
- **34/07—Ensure feedback is accurate and proportional.** Prevent conveying false accuracy or overconfidence.
- **34/08—Persist critical feedback until resolved.** Do not allow essential information to disappear prematurely.
- **34/09—Provide recovery guidance within feedback.** Offer clear next steps when errors or exceptions occur.

### Executive summary

- Feedback is visible system response, not mere activity indication.
- It confirms that user intent was received and what outcome occurred.
- The system must acknowledge every meaningful action immediately and proportionally.
- Feedback must make scope, consequence, and state change explicit.
- Critical signals must persist and differentiate success, warning, and failure clearly.
- Feedback succeeds when users understand what happened, why it happened, and what to do next.

### Success indicators

- Every user action receives a visible response.
- The system responds immediately to user input.
- Feedback clearly shows what changed or happened.
- Different outcomes are clearly distinguished.
- Feedback remains visible until the user understands the result.

**One-line summary:** Before users can trust their actions, they must know what the system did in response.

## 3.5 User Efficiency

> Why interaction quality matters.

**Ask yourself:** “Does your system measurably reduce users’ time and effort for real tasks?”

**Mission:** Ensure users complete tasks quickly by eliminating unnecessary steps and redundancy.

**Executive brief:** The system must optimize for user speed and effort, not visible system activity.

### Key heuristics

- Human time must be treated as the primary cost in design decisions.
- Efficiency must be evaluated across complete workflows.
- Design must reduce friction that slows user progress.
- Redundant and unnecessary input must be removed.
- Preventable delays must not interrupt task flow.
- Speed improvements must not reduce understanding.
- Automation must reduce steps without increasing supervision.
- Efficiency must account for error and recovery time.
- Efficiency must remain high during prolonged interaction.

### Core questions

- “Does the interaction save the user time and effort, and reduce errors?”
- “Is the user actually faster, or is the system just looking busier?”

### Focus areas

- **Human-cost focused:** “Does this save user time, or just machine time?” “Where is effort being spent: by the user or by the system?”
- **Workflow-level:** “Does it shorten the overall task from start to finish?” “Is it optimizing steps, or actual outcomes?”
- **Outcome-aware:** “Is the interaction improving real results, not just activity?” “Does it make the user’s goal easier to achieve?”
- **AI-aware:** “Does automation reduce human effort, or require supervision?” “Does assistance eliminate steps, or add interpretation work?”

### Directives

- **35/01—Prioritize human time as the primary cost.** Favor design decisions that save user time over system convenience.
- **35/02—Evaluate efficiency across complete workflows.** Optimize full task completion time, not isolated interaction speed.
- **35/03—Optimize for user throughput.** Reduce friction that slows progress regardless of system performance metrics.
- **35/04—Prevent redundant or corrective input.** Cut re-entry, unnecessary formatting, and avoidable corrections.
- **35/05—Remove blocking latency wherever possible.** Eliminate preventable delays that interrupt task flow and break user momentum.
- **35/06—Preserve clarity while optimizing speed.** Ensure acceleration does not reduce understanding.
- **35/07—Use automation to reduce user steps.** Avoid introducing automation that increases monitoring or correction burden.
- **35/08—Design to minimize error and recovery cost.** Account for correction time as part of user efficiency.
- **35/09—Optimize efficiency for prolonged use.** Ensure productivity remains high during extended interaction.

### Executive summary

- User Efficiency is respect for human time, not system throughput.
- It is measured across complete workflows, not isolated interaction speed.
- The system must remove friction, redundancy, and preventable latency from task flow.
- Automation must reduce user steps without increasing supervision or correction cost.
- Speed must preserve clarity.
- Acceleration that degrades understanding is false efficiency.
- User Efficiency succeeds when sustained interaction increases productivity without increasing cognitive or recovery burden.

### Success indicators

- Tasks can be completed quickly without unnecessary steps.
- Users can complete full workflows without repeated or redundant input.
- The system responds without delays that interrupt progress.
- Automation reduces the number of actions users must perform.
- Efficiency improves as users gain experience.

**One-line summary:** Before users can feel productive, the system must not waste their time or effort.

## 3.6 Fitts’s Law

> The governing physical constraint on all interaction.

**Ask yourself:** “Are frequent or critical targets in your system fast and easy to acquire physically?”

**Mission:** Ensure users can target actions easily by optimizing size and distance of interactive elements.

**Executive brief:** Interaction speed is constrained by physical targeting, not just system performance.

### Key heuristics

- High-frequency targets must be placed within short motor reach.
- Target size must correspond to usage frequency and consequence.
- Routine or low-risk actions must not demand fine motor accuracy.
- Screen boundaries must be leveraged for frequent or critical actions.
- High-value actions must be the easiest to acquire.
- Unnecessary target acquisitions must be eliminated.
- Layout must prioritize motor efficiency over visual symmetry alone.
- Target design must account for device-specific motor constraints.
- Design must reduce repeated acquisition costs during sustained use.
- Motor performance principles must inform layout before testing.

### Core questions

- “Is the physical effort to interact minimized?”
- “Is slowness due to user movement and precision, not system lag?”

### Focus areas

- **Motor-control focused:** “How far must the user move? How precise must they be?” “Do routine actions demand unnecessary precision?”
- **Workflow-aware:** “How many target acquisitions does the task require?” “Which targets dominate the time cost of the workflow?”
- **Device-agnostic:** “Does the interaction respect human motor limits across devices?” “Would it feel slow on any input method?”
- **AI-aware:** “Can AI assist by reducing required movement or precision?” “Does automation make interaction smoother without adding cognitive load?”

### Directives

- **36/01—Minimize distance to high-frequency targets.** Place commonly used controls within short motor reach.
- **36/02—Size interactive targets according to frequency and consequence.** Make important or frequent actions larger and easier to acquire.
- **36/03—Avoid unnecessary precision requirements.** Do not require fine motor accuracy for routine or low-risk actions.
- **36/04—Use screen edges strategically for frequent or critical actions.** Leverage boundaries to reduce motor effort.
- **36/05—Align target accessibility with usage frequency and importance.** Ensure high-value actions are easiest to acquire.
- **36/06—Reduce unnecessary target acquisitions.** Eliminate redundant steps to decrease total motor effort.
- **36/07—Prioritize motor efficiency over visual symmetry.** Design layouts according to acquisition performance, not aesthetic balance alone.
- **36/08—Adapt target design to input modality.** Account for device-specific motor constraints in layout and sizing decisions.
- **36/09—Optimize for cumulative motor efficiency.** Design to reduce repeated acquisition costs during sustained use.
- **36/10—Apply motor performance principles proactively.** Use Fitts’s Law to inform design decisions before usability testing.

### Executive summary

- Fitts’s Law governs motor effort, not visual arrangement.
- It predicts movement time from target distance and width; accuracy enters through the speed–accuracy trade-off.
- The system must make frequent and high-value actions largest and easiest to acquire.
- Design must reduce unnecessary precision and redundant target acquisition.
- Motor efficiency must take precedence over aesthetic symmetry and arbitrary layout decisions.
- Fitts’s Law succeeds when repeated interaction minimizes cumulative motor effort over sustained use.

### Success indicators

- Frequently used controls are easy to reach.
- Important actions have larger and easier targets.
- Routine actions do not require precise pointing.
- High-value actions are placed close to where users interact.
- Users can perform repeated actions quickly and comfortably.

**One-line summary:** Before interaction can feel fast, physical effort must be respected.

## 3.7 Input

> How users enter information.

**Ask yourself:** “Can users of your system enter information quickly and correctly the first time?”

**Mission:** Ensure users provide information with minimal effort and error by shaping input around what they know and how they express it.

**Executive brief:** The system must accept input in the form users have it, not in the form the system stores it.

### Key heuristics

- Users must not be asked for information the system already has.
- Input formats must accept how users naturally express values.
- Constraints must be visible before input, not discovered after.
- Validation must occur as early as possible without interrupting entry.
- Errors must be indicated at the field where they occur.
- The input method must match the type of data.
- Entered data must survive errors and interruptions.
- Required and optional input must be clearly distinguished.
- Input effort must match the value of the information to the user.

### Core questions

- “Does the system ask only for what it needs, in a form users can provide?”
- “Can users enter information correctly without trial and error?”

### Focus areas

- **Effort-first:** “What is asked that the system could infer or already knows?” “How many steps does one piece of information take?”
- **Format-aware:** “Does the field accept common formats?” “Are constraints shown before entry?”
- **Error-aware:** “When is invalid input detected?” “Is entered data kept after an error?”
- **AI-aware:** “Is predicted input distinguishable from what users typed?” “Can users reject autofill easily?”

### Directives

- **37/01—Ask only for what is needed.** Do not request information the system already has or does not use.
- **37/02—Accept natural formats.** Parse common ways users express dates, numbers, names, and addresses.
- **37/03—Show constraints before entry.** State limits, formats, and requirements before users type.
- **37/04—Validate early without interrupting.** Check input as it is completed, not on submission and not on every keystroke.
- **37/05—Locate errors at their source.** Indicate the exact field and the correction needed.
- **37/06—Match the control to the data.** Use the input method that fits the type, range, and frequency of the value.
- **37/07—Preserve entered data.** Keep all valid input through errors, navigation, and interruptions.
- **37/08—Distinguish required from optional.** Mark which input is needed to proceed.
- **37/09—Separate suggested input from entered input.** Make autofill and predictions visible as suggestions until users accept them.

### Executive summary

- Input is the user’s transfer of information to the system, not form filling.
- It succeeds or fails on effort and first-time accuracy.
- The system must ask only for what it needs and accept it in natural formats.
- Constraints must be visible before entry, and errors located at their source.
- Entered data must never be lost to an error or interruption.
- Input succeeds when users provide correct information once, without guessing the system’s rules.

### Success indicators

- Users are not asked for information the system already has.
- Common formats are accepted without correction.
- Constraints are visible before typing.
- Errors point to the field and the fix.
- Entered data survives errors and interruptions.

**One-line summary:** Before the system can act on information, users must be able to give it without friction.

