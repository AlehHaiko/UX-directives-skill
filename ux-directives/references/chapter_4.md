# Chapter 4: System Behavior & Workflow Logic

> **How the system behaves over time, across steps, and in response to user action.**
>
> These determine whether the system works with the user or against them.

**Mission statement:** Ensure systems behave coherently over time, across steps, and in response to user actions, supporting work rather than obstructing it.

## 4.1 Defaults

> What a system chooses on users’ behalf.

**Ask yourself:** “Do defaults in your system reliably help users without harming control or trust?”

**Mission:** Ensure users start efficiently by providing appropriate preset choices.

**Executive brief:** The system must treat defaults as accountable decisions on users’ behalf, not neutral conveniences.

### Key heuristics

- Every default must represent a deliberate behavioral commitment.
- Defaults must reduce user workload.
- The consequences of accepting a default must be clear.
- The scope of default effects must be visible.
- Defaults must be easily changeable.
- Changing or applying defaults must not silently destroy user work.
- Defaults may adapt to task or environment when appropriate.
- Defaults that users consistently correct must be removed or revised.

### Core questions

- “Do defaults guide effectively without restricting control?”
- “Can users see, understand, and override them?”

### Focus areas

- **Agency-first:** “Where is the system acting instead of asking?” “What decisions are pre-selected for the user?”
- **Risk-aware:** “What happens if the default is accepted blindly?” “Is the default safe under uncertainty?”
- **Transparency-aware:** “Are the reasons for defaults visible and understandable?” “Can users predict the impact of accepting or changing defaults?”
- **AI-aware:** “Is the default static or inferred from user activity by the system?” “Does adaptation remain predictable over time?”

### Directives

- **41/01—Treat defaults as intentional decisions.** Design every default as a behavioral commitment, not a temporary filler.
- **41/02—Use defaults to remove effort.** Make sure defaults reduce user workload, not introduce hesitation.
- **41/03—Make default implications explicit.** Ensure users understand what accepting a default will do.
- **41/04—Clarify the scope of default effects.** Indicate whether a default applies locally, globally, or persistently.
- **41/05—Ensure defaults are easily overridable.** Allow users to change defaults without friction.
- **41/06—Protect user work when defaults change.** Prevent silent data loss or destructive resets triggered by defaults.
- **41/07—Adapt defaults to context when appropriate.** Use task or environment signals to refine default values responsibly.
- **41/08—Remove unreliable or misleading defaults.** Eliminate defaults that users consistently correct.

### Executive summary

- Defaults are behavioral commitments, not placeholder values.
- They shape user action by defining what happens if no change is made.
- The system must design defaults to reduce effort while making their implications explicit.
- Defaults must be easily overridable and never silently compromise user work.
- Context-aware defaults are valid only when they align with user intent and expectation.
- Defaults succeed when users rarely need to change them and never suffer from accepting them.

### Success indicators

- Default settings reduce the amount of work users must do.
- Users can clearly see what the default choice will do.
- The scope of a default is easy to understand.
- Defaults can be changed quickly and easily.
- Defaults match common user needs and rarely require correction.

**One-line summary:** Before users can begin efficiently, the system must make reasonable choices on their behalf.

## 4.2 Anticipation

> What a system brings forward proactively.

**Ask yourself:** “Does your system surface the next likely need for users without commandeering?”

**Mission:** Ensure users act with less effort by predicting and supporting likely needs.

**Executive brief:** The system must anticipate user needs without overriding user control.

### Key heuristics

- Anticipatory behavior must remove friction, not display intelligence.
- Anticipatory features must maintain user agency.
- Users must recognize when the system is predicting or assisting.
- Anticipatory assistance must appear at the moment it supports the current task phase.
- Anticipation must be based on current task, state, and history.
- Anticipatory interventions must be limited.
- Users must be able to dismiss or ignore anticipatory assistance without penalty.
- Incorrect anticipatory actions must be easy to ignore or reverse.

### Core questions

- “Does the system anticipate user needs without taking control?”
- “Is help timely, helpful, and under user control?”

### Focus areas

- **User-agency first:** “Does anticipation assist decision-making rather than preempt it?” “Can users easily ignore or decline suggestions?”
- **Timing-aware:** “Is help delivered neither too early nor too late?” “Does anticipation reduce preparation work effectively?”
- **Transparency-aware:** “Are predictions and suggestions understandable?” “Can users see why the system anticipates certain actions?”
- **AI-aware:** “Are predictions legible and bounded?” “Does learning improve assistance without reducing trust?”

### Directives

- **42/01—Use anticipation to reduce user effort.** Design anticipatory behavior to remove friction rather than demonstrate intelligence.
- **42/02—Preserve user control in anticipatory features.** Offer suggestions rather than automatic irreversible decisions.
- **42/03—Make anticipatory behavior perceptible.** Ensure users recognize when the system is assisting or predicting.
- **42/04—Deliver anticipation at the moment of relevance.** Trigger assistance only when it meaningfully supports the current task phase.
- **42/05—Base anticipation on current context.** Use task, state, and history signals to ensure relevance.
- **42/06—Limit anticipatory interventions.** Do not overwhelm with excessive or unnecessary suggestions.
- **42/07—Ensure anticipatory assistance is optional.** Allow users to dismiss or ignore suggestions without penalty.
- **42/08—Minimize the cost of incorrect anticipation.** Ensure mistaken suggestions are easy to ignore or reverse.

### Executive summary

- Anticipation is friction reduction, not intelligence display.
- It assists by predicting relevance without removing user control.
- The system must make anticipatory behavior perceptible and contextually justified.
- Anticipatory suggestions must be optional, limited, and easily dismissible.
- Incorrect anticipation must carry minimal cost and never compromise user work.
- Anticipation succeeds when assistance feels timely, helpful, and fully subordinate to user intent.

### Success indicators

- The system offers helpful suggestions that reduce user effort.
- Suggestions appear when they are relevant to the current task.
- Users can clearly see when the system is making a suggestion.
- Suggestions are easy to accept, ignore, or dismiss.
- Incorrect suggestions do not interrupt work or create extra effort.

**One-line summary:** Before users are forced to search or prepare, the system must already be ready.

## 4.3 Autonomy

> How much control users retain.

**Ask yourself:** “Do users of your system retain meaningful control over consequential actions?”

**Mission:** Ensure users delegate safely by enabling controlled system actions without loss of oversight and control.

**Executive brief:** The system must preserve real user control over delegated actions.

### Key heuristics

- System behavior must support, not replace, user decision-making.
- Consequential automation must require user awareness and consent.
- Users must be able to override, pause, or modify automated processes.
- Automated activity and intent must be perceptible.
- System-initiated actions must be undoable or revisable.
- User control requirements must increase with consequence severity.
- Automation must not be enforced solely for efficiency gains.
- Users must be able to inspect and adjust persistent automation and history.
- Automation must strengthen users’ sense of control and capability.

### Core questions

- “Which decisions are made by the user, and which by the system?”
- “Can users see, understand, and control delegation?”

### Focus areas

- **Control-first:** “Can users always override the system?” “Is delegation deliberate or implicit?”
- **Risk-aware:** “What happens if the system is wrong?” “Are high-risk actions ever taken without consent?”
- **Transparency-aware:** “Are system decisions and rationale visible to the user?” “Can users predict when and why the system will act?”
- **AI-aware:** “Is automation advisory or authoritative?” “Does learning expand capability without reducing user control?”

### Directives

- **43/01—Design system behavior to preserve human agency.** Ensure automation supports rather than replaces user decision-making.
- **43/02—Require explicit delegation of automated behavior.** Do not perform consequential automation without user awareness and consent.
- **43/03—Provide meaningful intervention mechanisms.** Enable users to override, pause, or modify automated processes.
- **43/04—Make automated state and intent visible.** Ensure users understand what the system is doing and why.
- **43/05—Ensure reversibility of automated outcomes.** Allow users to undo or revise system-initiated actions.
- **43/06—Calibrate autonomy according to risk level.** Increase user control requirements as consequence severity rises.
- **43/07—Prioritize agency over raw efficiency.** Avoid enforcing automation solely for speed gains.
- **43/08—Preserve autonomy across time horizons.** Enable users to inspect and adjust persistent settings and historical automation.
- **43/09—Design automation to reinforce user confidence.** Ensure system behavior strengthens users’ sense of control and capability.

### Executive summary

- Autonomy is preserved human agency, not unrestricted automation.
- It ensures the system supports decisions without replacing them.
- The system must require explicit delegation for consequential automated behavior.
- Automated state, intent, and outcomes must remain visible, controllable, and reversible.
- Autonomy must be calibrated to risk, increasing user control as consequence severity rises.
- Autonomy succeeds when automation strengthens users’ sense of control rather than diminishing it.

### Success indicators

- Users remain in control of important decisions.
- Automated actions occur with user awareness or consent.
- Users can pause, modify, or override automation.
- The system clearly shows what automation is doing.
- Automated actions can be undone or corrected.

**One-line summary:** Before users can trust a system, they must feel it acts with them, not for them.

## 4.4 Error Prevention

> How mistakes are avoided.

**Ask yourself:** “Is it easier for users of your system to perform correct actions than incorrect ones?”

**Mission:** Ensure users avoid mistakes by constraining risky actions while avoiding unnecessary restriction.

**Executive brief:** The system must prevent errors by shaping actions before mistakes occur.

### Key heuristics

- Design must prevent errors structurally, not rely on recovery.
- Impossible or unsuccessful configurations must be structurally constrained.
- Correct and safe actions must require the least effort.
- Potential errors must surface at the earliest viable moment.
- Hidden or invisible modes must be eliminated or minimized.
- Protective friction must scale with consequence severity.
- Confirmation dialogs must be rare and contextually justified.
- Exploration must be safe and penalty-free.
- Defaults and automation must minimize harm and clarify consequences.

### Core questions

- “Does the system make correct actions easy and errors hard or impossible?”
- “Is doing the right thing the path of least resistance?”

### Focus areas

- **Constraint-first:** “What invalid states are blocked rather than corrected later?” “What actions are structurally impossible by design?”
- **Risk-aware:** “Are dangerous actions harder to perform than safe ones?” “Is friction calibrated to the level of risk?”
- **Workflow-aware:** “Where in the workflow could errors occur?” “Is prevention happening early enough? How are errors prevented?”
- **AI-aware:** “Does automation reduce errors, or create new failure modes?” “Are predictions constrained to safe outcomes?”

### Directives

- **44/01—Design to prevent errors proactively.** Prioritize structural prevention over post-error recovery.
- **44/02—Eliminate invalid states through constraint.** Prevent users from entering configurations that cannot succeed.
- **44/03—Make safe and correct actions easiest to perform.** Design workflows so desirable behavior requires the least effort.
- **44/04—Surface potential errors at the earliest viable moment.** Provide validation before consequences escalate.
- **44/05—Eliminate or minimize hidden modes.** Ensure users are not required to remember invisible states to avoid errors.
- **44/06—Adjust safeguards according to consequence severity.** Increase friction proportionally for high-risk actions.
- **44/07—Use confirmation dialogs sparingly and meaningfully.** Avoid habituating users to dismiss warnings automatically.
- **44/08—Allow safe exploration without penalty.** Design guardrails that protect without discouraging learning.
- **44/09—Ensure defaults and automation reduce error risk.** Design automated behavior to minimize harm and clarify consequences.

### Executive summary

- Error Prevention is structural constraint, not reactive correction.
- It eliminates invalid states and makes safe actions the path of least resistance.
- The system must surface risk early and prevent escalation before consequences occur.
- Safeguards must scale with severity while avoiding habitual, meaningless warnings.
- Hidden modes and invisible conditions are liabilities that invite error.
- Error Prevention succeeds when harmful outcomes are difficult to produce and safe exploration remains possible.

### Success indicators

- The interface prevents invalid or impossible actions.
- Safe and correct actions are the easiest to perform.
- Potential errors are identified before they cause problems.
- High-risk actions require additional confirmation or safeguards.
- Users can explore and try actions without causing harm.

**One-line summary:** Before errors occur, the system must quietly prevent them.

## 4.5 Recovery

> How mistakes are repaired.

**Ask yourself:** “Can users of your system recover from failure quickly without penalty or loss?”

**Mission:** Ensure users can correct errors by enabling easy reversal and penalty-free recovery.

**Executive brief:** The system must enable safe, confident continuation after errors.

### Key heuristics

- Failure must be treated as an expected condition within workflows.
- Undo functionality must be consistent, predictable, and comprehensive.
- User actions must be reversible wherever possible.
- User data must be preserved during correction or failure events.
- Permanent consequences must be unmistakably clear and explicitly acknowledged.
- User context must remain intact during and after recovery.
- Users must be able to resume progress immediately after correction.
- Alternative recovery mechanisms must be available where appropriate.
- Recovery must function across crashes, pauses, and connectivity loss.

### Core questions

- “Can users recover from errors quickly and safely, without losing context or confidence?”
- “Is returning to a safe state clear and reliable?”

### Focus areas

- **Undo-first:** “Is undo predictable, reliable, and sufficient?” “Which actions are reversible? Which are not?”
- **Context-aware:** “Does recovery preserve the user’s position and work?” “Can users resume without rebuilding prior progress?”
- **Trust-aware:** “Does recovery feel forgiving or punitive?” “Does the system blame or assist?”
- **AI-aware:** “When automation fails, can users intervene and recover?” “Does recovery reveal causes, not just effects?”

### Directives

- **45/01—Design with failure as an expected condition.** Build recovery mechanisms as core workflow features.
- **45/02—Provide reliable undo functionality.** Ensure undo is consistent, predictable, and comprehensive.
- **45/03—Maximize reversibility of user actions.** Design systems so users can act without fear of permanent harm.
- **45/04—Protect user data during recovery.** Prevent loss of work during error correction or failure events.
- **45/05—Make irreversible actions unmistakably clear.** Require explicit acknowledgment for permanent consequences.
- **45/06—Preserve context during recovery.** Ensure users remain oriented after correcting errors.
- **45/07—Provide forward guidance after recovery.** Enable users to resume progress immediately after correction.
- **45/08—Offer multiple recovery mechanisms.** Supplement undo with version history, restore points, or alternative correction paths.
- **45/09—Design recovery for interruption scenarios.** Ensure resilience across crashes, pauses, and connectivity loss.

### Executive summary

- Recovery assumes failure as a normal condition, not an exception.
- It enables users to act without fear of irreversible harm.
- The system must provide reliable undo, reversibility, and protected data integrity.
- Irreversible consequences must be unmistakable and explicitly acknowledged.
- Recovery must preserve context and support immediate forward progress.
- Recovery succeeds when errors, interruptions, and failures do not permanently disrupt work or confidence.

### Success indicators

- Users can easily undo actions and correct mistakes.
- Most actions can be reversed without permanent loss.
- User data and work are protected during errors or failures.
- Irreversible actions are clearly indicated before they occur.
- After recovery, users can quickly continue their work.

**One-line summary:** Before mistakes become failures, users must be able to recover.

## 4.6 Work Protection

> How effort is preserved over time.

**Ask yourself:** “Is user work protected in your system against interruption, failure, and error?”

**Mission:** Ensure users do not lose progress by safeguarding ongoing work.

**Executive brief:** The system must protect user work under all reasonable conditions.

### Key heuristics

- User time, thought, and intent must be treated as high-value data.
- Workflows must assume interruption and failure as normal conditions.
- Work must be saved automatically and continuously.
- Actions must preserve original work whenever possible.
- Permanent deletion must be unmistakable and intentional.
- Partial and intermediate states must be preserved throughout progression.
- Work must remain intact across sessions and devices.
- Users must perceive that their work is preserved.
- Preserved work must be restorable or reversible.

### Core questions

- “Does the system protect user effort from loss?”
- “Can work survive failures, interruptions, or mistakes?”

### Focus areas

- **Continuity-first:** “What happens to work if users leave, crash, or disconnect?” “Can they safely stop and resume later?”
- **Scope-aware:** “Which work is protected? Which is not?” “When does protection start?”
- **Trust-aware:** “Would users feel safe investing significant effort?” “Does the system earn long-term trust?”
- **AI-aware:** “Can automation destroy user work silently?” “Is generated or inferred work equally protected?”

### Directives

- **46/01—Treat user effort as high-value data.** Design systems to preserve time, thought, and intent embedded in user work.
- **46/02—Design for interruption and failure by default.** Build resilience into workflows as a baseline condition.
- **46/03—Implement automatic and continuous saving.** Do not rely on manual save actions for data preservation.
- **46/04—Favor non-destructive workflows.** Design actions so original work remains recoverable.
- **46/05—Require explicit confirmation for destructive actions.** Make permanent deletion unmistakable and intentional.
- **46/06—Protect drafts and intermediate states.** Preserve partial work throughout task progression.
- **46/07—Ensure cross-session and cross-device continuity.** Maintain work integrity across time and environments.
- **46/08—Communicate protection status clearly.** Provide visible indicators that work is preserved.
- **46/09—Integrate recovery into protection systems.** Ensure preserved work can be restored or rolled back reliably.

### Executive summary

- Work Protection treats user effort as high-value data, not disposable input.
- It preserves time and progress across interruption, failure, and transition.
- The system must default to automatic, continuous, and non-destructive preservation.
- Destructive actions must be explicit and recoverable wherever possible.
- Protection must extend across sessions, devices, and intermediate states.
- Work Protection succeeds when users trust that their effort is safe and their progress cannot be silently lost.

### Success indicators

- User work is saved automatically and continuously.
- Drafts and partial work are preserved during tasks.
- Work remains intact across interruptions and session changes.
- Destructive actions require clear confirmation.
- Users can restore or recover previously saved work.

**One-line summary:** Before users invest effort, they must trust it will not be lost.

## 4.7 Latency

> How temporal constraints influence workflows.

**Ask yourself:** “Does your system preserve user momentum under delay?”

**Mission:** Ensure users maintain flow by minimizing delays and communicating wait states.

**Executive brief:** The system must preserve user momentum by controlling both real and perceived latency.

### Key heuristics

- Interaction must preserve user cognitive flow.
- User input must receive instant perceptual response.
- System activity must remain perceptible during processing.
- Delays must not halt all interaction unnecessarily.
- Initiation and completion must be separated when feasible.
- Dependent sequential requests must be minimized.
- Waiting states must not impose additional cognitive decisions.
- Progress feedback must be accurate and proportionate.
- Usability must be maintained under slow or unstable conditions.

### Core questions

- “Does the system preserve user momentum despite delays?”
- “Is latency absorbed or does it interrupt thinking and flow?”

### Focus areas

- **Perception-first:** “Do pauses force users to wait, or let them continue working?” “Is time experienced as friction, or is it masked by progress?”
- **Workflow-aware:** “Does delay block progress, or just slow completion?” “Can users stay productive during unavoidable waits?”
- **Communication-aware:** “Does silence cause users to doubt the system?” “Is delay explained clearly and promptly?”
- **AI-aware:** “Does AI hide latency, or add to it?” “Are long-running operations staged to preserve flow?”

### Directives

- **47/01—Design to preserve user momentum.** Minimize interruptions that break cognitive flow.
- **47/02—Provide instant acknowledgment of user input.** Respond perceptually even if processing continues.
- **47/03—Reduce perceived latency through visible system activity.** Do not allow silent waiting states.
- **47/04—Keep users productively occupied during delays.** Prevent blocking states that halt all interaction.
- **47/05—Separate initiation from completion when possible.** Allow background processing without freezing interaction.
- **47/06—Minimize dependent sequential requests.** Reduce cumulative delays caused by repeated server interactions.
- **47/07—Avoid requiring decisions during idle delays.** Do not compound waiting with cognitive effort.
- **47/08—Provide truthful and proportional progress feedback.** Avoid misleading estimates or cosmetic animations.
- **47/09—Ensure graceful degradation under poor conditions.** Maintain usability during slow or unstable performance.

### Executive summary

- Latency is disruption of cognitive momentum, not just elapsed time.
- It interrupts flow when system response lags behind user intent.
- The system must acknowledge input immediately, even if processing continues.
- Waiting states must be visible, truthful, and non-blocking whenever possible.
- Interaction must remain productive during delay, with graceful degradation under poor conditions.
- Latency succeeds when users perceive continuity of control despite underlying processing time.

### Success indicators

- The system acknowledges user input immediately.
- Users can see that the system is processing work.
- Waiting states are clearly communicated.
- Users can continue working while background tasks run.
- Slow performance does not block essential tasks.

**One-line summary:** Before users lose momentum, the system must respond.
