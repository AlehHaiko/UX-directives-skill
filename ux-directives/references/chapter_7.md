# Chapter 7: Trust, Safety & Responsibility

> **How systems earn trust, preserve user agency, and uphold responsibility.**
>
> Trust is now a core usability property, not an afterthought.

**Mission statement:** Establish and preserve user trust by ensuring transparency, informed agency, and clear accountability in system behavior.

## 7.1 Consent & Control

> Who decides and when.

**Ask yourself:** “Do users of your system retain control over actions affecting them or their data?”

**Mission:** Ensure users retain agency by enabling informed choices and control over permissions.

**Executive brief:** The system must preserve ongoing user control and earn trust through behavior.

### Key heuristics

- Consent must remain reviewable, modifiable, and revocable at any time.
- User controls must produce meaningful system change.
- The scope of consent must be clearly defined.
- Users must be able to revoke consent without harm or friction.
- Automated processes must remain subject to user interruption.
- Control mechanisms must scale with consequence severity.
- Consequential actions must require clear user acknowledgment.
- Consent must not be broadened without renewed permission.
- System behavior must consistently reflect granted permissions.

### Core questions

- “Do users retain meaningful control? Does the system continuously respect it?”
- “Can users grant, withdraw, and trust control at all times?”

### Focus areas

- **Temporal-first:** “Can users change their mind without penalty?” “Does consent remain valid when context changes?”
- **Scope-aware:** “What exactly have users agreed to? Where does it apply?” “Does control align with consequence?”
- **Failure-aware:** “What happens if control is unclear or contested?” “Does the system default to restraint when uncertain?”
- **AI-aware:** “Does automation remain subordinate to consent?” “Is inferred intent treated as permission or authority?”

### Directives

- **71/01—Design consent as a continuous capability.** Allow users to review, modify, and revoke consent at any time.
- **71/02—Ensure user controls produce actual system change.** Do not offer settings that lack meaningful impact.
- **71/03—Make the scope of control explicit.** Define clearly what actions or data are governed by consent.
- **71/04—Enable simple and penalty-free withdrawal.** Ensure users can revoke participation without harm.
- **71/05—Keep automated processes interruptible.** Preserve user authority over automated actions.
- **71/06—Scale control mechanisms with risk levels.** Increase oversight and safeguards for high-consequence actions.
- **71/07—Do not allow implicit or overreaching defaults.** Require explicit user acknowledgment for consequential actions.
- **71/08—Preserve consent integrity across updates.** Do not broaden authority without renewed permission.
- **71/09—Enforce consent consistently in system behavior.** Ensure actions align with stated permissions at all times.

### Executive summary

- Consent & Control is continuous user authority, not one-time permission.
- It ensures users can understand, modify, and revoke system power at any time.
- The system must make the scope and consequence of consent explicit and enforceable.
- Controls must produce real behavioral change and remain interruptible for automated processes.
- Oversight must scale with risk, and authority must never expand without renewed permission.
- Consent & Control succeeds when system behavior consistently aligns with user intent and granted authority.

### Success indicators

- Users can clearly see what they are agreeing to.
- Users can review and change permissions at any time.
- System controls produce real and immediate changes.
- Users can withdraw consent without penalty.
- Automated actions remain interruptible and under user control.

**One-line summary:** Before users can trust a system, they must retain meaningful control over what it does on their behalf.

## 7.2 Transparency

> Why systems behave as they do.

**Ask yourself:** “Can users of your system understand and influence behavior when needed?”

**Mission:** Ensure users understand system behavior by making processes and outcomes visible.

**Executive brief:** The system must ensure its behavior is understandable and controllable.

### Key heuristics

- Transparency must enable trust and user intervention.
- Explanations must provide sufficient detail for informed decisions without excess.
- Inputs, triggers, and outcomes must be traceable.
- Confidence indicators must reflect actual reliability.
- Higher-consequence outcomes must receive deeper explanation.
- Explanations must be accompanied by meaningful correction mechanisms.
- Explanations must simplify without misrepresenting behavior.
- Explanations must appear before or during consequential impact.
- Explanations must exclude unnecessary technical detail.

### Core questions

- “Is the system understandable enough to be trusted and correctable?”
- “Can users see what is happening and fix it when it is wrong?”

### Focus areas

- **Understanding-first:** “Can users explain what the system is doing? Do they know why?” “Is cause-and-effect visible, not just inferred?”
- **Action-first:** “What can users do when they disagree with the system?” “Can corrections be made without escalation or special expertise?”
- **Risk-aware:** “Is opacity minimized and proportional to risk?” “Are critical decisions more transparent than trivial ones?”
- **AI-aware:** “Does the system reveal uncertainty and limits?” “Are explanations faithful to actual behavior?”

### Directives

- **72/01—Design transparency to support trust and intervention.** Ensure explanations empower user correction, not passive observation.
- **72/02—Provide decision-relevant clarity.** Deliver explanations sufficient for informed action without overwhelming detail.
- **72/03—Expose causal relationships.** Make inputs, triggers, and outcomes traceable.
- **72/04—Communicate uncertainty proportionally.** Align confidence indicators with actual reliability.
- **72/05—Increase explanatory depth for high-risk outcomes.** Provide greater insight where stakes are higher.
- **72/06—Enable correction mechanisms alongside explanation.** Pair visibility with meaningful user action.
- **72/07—Ensure explanatory accuracy with simplicity.** Simplify without misrepresenting system behavior.
- **72/08—Deliver explanations at the point of impact.** Provide visibility before or while a consequence unfolds, not after.
- **72/09—Curate explanations for relevance.** Do not overwhelm users with unnecessary technical detail.

### Executive summary

- Transparency is actionable clarity, not passive disclosure.
- It reveals causal relationships so users can understand inputs, triggers, and outcomes.
- The system must provide decision-relevant explanations aligned with actual reliability and uncertainty.
- Explanatory depth must scale with risk and appear at the point of impact.
- Visibility must be paired with meaningful correction or intervention mechanisms.
- Transparency succeeds when users can interpret system behavior accurately and act on it confidently.

### Success indicators

- Users can see how system actions lead to outcomes.
- Important inputs, triggers, and results are visible.
- The system communicates uncertainty clearly.
- Explanations appear when they are relevant to user decisions.
- Users can act to correct or adjust outcomes.

**One-line summary:** Before users can rely on a system, they must be able to understand what it is doing and why.

## 7.3 Error Communication

> How systems communicate when things go wrong.

**Ask yourself:** “Does your system help users recover instead of assigning blame?”

**Mission:** Ensure users respond appropriately to issues by explaining errors clearly without vagueness or blame.

**Executive brief:** The system must communicate errors in ways that support users, not judge them.

### Key heuristics

- Errors must be framed as system conditions, not user faults.
- Error messaging must use system-owned, respectful language.
- Failure communication must remain calm and respectful.
- Failures must be described clearly in understandable language.
- Error messages must specify where and why the issue occurred.
- Clear guidance for resolution and continuation must accompany errors.
- Language urgency must match actual impact.
- Technical causes must be translated into user-relevant terms.
- Failure messaging must support continued engagement.

### Core questions

- “When errors occur, does the system guide and support users, or assign blame?”
- “Do error messages help users recover effectively?”

### Focus areas

- **Tone-first:** “Does the system speak with users, not at them?” “Is the language calm and respectful under failure?”
- **Action-first:** “Does the message explain what to do next?” “Can users fix the problem without guessing?”
- **Trust-aware:** “Does the error handling build confidence rather than anxiety?” “Would users feel safe making mistakes?”
- **AI-aware:** “Are uncertainty and system limits communicated?” “Does automation take responsibility for its failures?”

### Directives

- **73/01—Frame errors as system conditions.** Never attribute failures to users.
- **73/02—Use system-owned language in error messaging.** Communicate accountability clearly and respectfully.
- **73/03—Maintain calm, respectful tone.** Do not use language that induces stress or defensiveness.
- **73/04—Provide clear explanation of failures.** Describe what occurred in plain language.
- **73/05—Localize and specify error context.** Identify where and why issues occurred.
- **73/06—Include actionable recovery guidance.** Provide clear instructions for resolution and continuation.
- **73/07—Calibrate language to consequence.** Match urgency and emphasis to actual impact.
- **73/08—Translate technical causes into user-relevant language.** Do not expose internal system terminology unnecessarily.
- **73/09—Protect user confidence after failure.** Ensure messaging supports continued engagement.

### Executive summary

- Error Communication frames failures as system conditions, not user faults.
- It communicates accountability clearly, calmly, and respectfully.
- The system must explain what occurred, where it occurred, and why it matters in user-relevant language.
- Messages must include actionable guidance that supports immediate recovery and continuation.
- Tone and urgency must align proportionally with actual consequence.
- Error Communication succeeds when users remain confident, informed, and able to proceed after failure.

### Success indicators

- Error messages clearly explain what happened.
- The system takes responsibility for the problem.
- Messages use calm and respectful language.
- Errors identify where the problem occurred.
- Users are given clear steps to resolve the issue.

**One-line summary:** Before users can recover from failure, they must be spoken to clearly and respectfully.

## 7.4 Data Integrity

> Whether data can be trusted.

**Ask yourself:** “Can users of your system trust their data is safe, accurate, and handled as expected?”

**Mission:** Ensure users trust outcomes by preserving accuracy and handling data reliably.

**Executive brief:** The system must preserve data integrity even when users are not watching.

### Key heuristics

- Information must remain accurate across time and state changes.
- Primary records must not be silently overwritten by derived values.
- Data must be protected against duplication, omission, and misapplication.
- State changes must be atomic or reversible.
- Data correctness must persist through retries and interruptions.
- Automated processes must maintain data accuracy and wholeness at scale.
- Users must be able to inspect and confirm data correctness.
- Accumulating data inconsistencies must be detected and addressed proactively.
- Correctness must persist without constant manual monitoring.

### Core questions

- “Does the system keep user data complete and accurate over time and during failures?”
- “Is data reliable even when the user is absent?”

### Focus areas

- **Custody-first:** “What happens to users’ data when they leave the system?” “Who is responsible for maintaining it at all times?”
- **Failure-aware:** “Does data survive crashes, retries, and partial operations?” “Are edge cases treated as first-class scenarios?”
- **Change-aware:** “Does data remain valid through updates and migrations?” “Are transformations reversible or auditable?”
- **AI-aware:** “Are inferred or generated data clearly marked?” “Does learning ever overwrite the original source of truth?”

### Directives

- **74/01—Design for temporal data correctness.** Ensure information remains accurate across time and state changes.
- **74/02—Protect primary source data.** Prevent silent overwriting of original records by derived values.
- **74/03—Safeguard completeness and scope.** Detect and prevent duplication, omission, or misapplication of data.
- **74/04—Ensure atomic or reversible state changes.** Do not expose users to unstable intermediate states.
- **74/05—Protect data during partial failures.** Design systems to maintain correctness through retries and interruptions.
- **74/06—Enforce integrity in automated processes.** Ensure scale and automation preserve correctness and reliability.
- **74/07—Provide mechanisms for data verification.** Allow users to inspect and confirm accuracy.
- **74/08—Detect and remediate accumulating inconsistencies.** Monitor for cascading data errors proactively.
- **74/09—Design integrity to operate without constant oversight.** Ensure correctness persists without manual monitoring.

### Executive summary

- Data Integrity is preserved correctness over time, not temporary accuracy.
- It ensures information remains complete, consistent, and reliable across state changes and automation.
- The system must protect primary data, prevent silent corruption, and avoid unstable intermediate states.
- Integrity mechanisms must withstand interruption, scale, and partial failure without manual oversight.
- Verification and remediation must be built in, not retrofitted after error accumulation.
- Data Integrity succeeds when correctness persists predictably without requiring constant user vigilance.

### Success indicators

- Data remains accurate and consistent across actions and time.
- Original records are protected from unintended overwriting.
- Data is not duplicated, lost, or applied incorrectly.
- System changes occur reliably without unstable intermediate states.
- Users can inspect and verify the correctness of important data.

**One-line summary:** Before users can trust outcomes, they must trust how their data is handled.

## 7.5 Privacy

> What happens to personal information.

**Ask yourself:** “Do users of your system know and control what personal information it collects, keeps, and shares?”

**Mission:** Ensure users keep control of personal information by collecting the minimum, explaining its use, and honoring their choices.

**Executive brief:** The system must treat personal information as the user’s, held in trust for a stated purpose.

### Key heuristics

- Collection must be limited to what the stated purpose requires.
- The purpose of every collection must be stated at the point of collection.
- Defaults must favor privacy.
- Users must be able to see what is held about them.
- Users must be able to correct, export, and delete their information.
- Sharing with third parties must require explicit, specific consent.
- Retention must be limited and stated.
- Privacy controls must be reachable where the related data is used.
- Privacy choices must persist across sessions, devices, and updates.

### Core questions

- “What personal information does the system collect, and why?”
- “Can users see, change, and remove it?”

### Focus areas

- **Minimization-first:** “Is every field needed for the stated purpose?” “What could be collected less precisely?”
- **Visibility-aware:** “Can users see everything held about them?” “Is the purpose stated where data is collected?”
- **Control-aware:** “Can users export or delete their data without contacting support?” “Are privacy settings near the features they affect?”
- **AI-aware:** “Is personal information used to train models?” “Can users exclude their data from learning?”

### Directives

- **75/01—Collect the minimum.** Request only the personal information the stated purpose requires.
- **75/02—State purpose at collection.** Explain why information is needed where and when it is requested.
- **75/03—Default to privacy.** Set the most protective option as the default.
- **75/04—Make held data visible.** Let users see all personal information the system holds about them.
- **75/05—Enable correction, export, and deletion.** Provide direct controls without requiring support contact.
- **75/06—Require specific consent for sharing.** Do not share personal information with third parties under general or implied consent.
- **75/07—Limit and state retention.** Keep personal information only as long as stated, then remove it.
- **75/08—Place privacy controls in context.** Offer privacy choices where the related data is used.
- **75/09—Preserve privacy choices.** Ensure settings persist across sessions, devices, and updates.

### Executive summary

- Privacy is the user’s control over personal information, not a policy document.
- It limits what is collected to what a stated purpose requires.
- The system must default to protection and state purpose at the point of collection.
- Users must be able to see, correct, export, and delete what is held about them.
- Sharing and retention must be specific, consented, and limited.
- Privacy succeeds when users know what the system holds and why, and can change it at any time.

### Success indicators

- Only necessary personal information is requested.
- The purpose of collection is stated where data is entered.
- Protective options are the default.
- Users can view, export, and delete their data directly.
- Privacy choices persist across sessions and updates.

**One-line summary:** Before users can share personal information, they must know it remains theirs.

## 7.6 Non-Manipulation

> How the system influences user choices.

**Ask yourself:** “Does your system influence users only in ways they would endorse if they saw how it works?”

**Mission:** Ensure users act on their own intent by excluding interface techniques that exploit bias, pressure, or concealment.

**Executive brief:** The system must persuade only through information, never through deception, pressure, or friction against the user’s interest.

### Key heuristics

- Influence must be transparent to the person influenced.
- Leaving must be as easy as joining.
- Costs and conditions must be disclosed before commitment.
- Urgency and scarcity signals must be true.
- Declining an offer must not be framed as a fault.
- Options against the system’s interest must be equally visible.
- Consent must not be obtained through pre-checked or bundled choices.
- Interface patterns must not exploit habit to trigger unintended actions.
- Engagement features must not override users’ stated limits.

### Core questions

- “Would users endorse this design if they understood how it influences them?”
- “Is the user’s easiest path also the one in the user’s interest?”

### Focus areas

- **Symmetry-first:** “Is canceling as easy as subscribing?” “Is ‘no’ as visible as ‘yes’?”
- **Truth-aware:** “Are countdowns, stock levels, and popularity claims real?” “Are total costs visible before commitment?”
- **Pressure-aware:** “Does wording shame a refusal?” “Does the interface interrupt to push a choice?”
- **AI-aware:** “Does personalization exploit known weaknesses?” “Can conversational agents pressure users in ways a static interface could not?”

### Directives

- **76/01—Influence only transparently.** Use persuasion users could recognize and endorse.
- **76/02—Make exit as easy as entry.** Provide cancellation, unsubscribing, and deletion with no more steps than signing up.
- **76/03—Disclose costs before commitment.** Show full price, recurring charges, and conditions before users agree.
- **76/04—Use only true urgency and scarcity.** Do not display timers, stock levels, or demand signals that are not real.
- **76/05—Do not shame refusal.** Phrase declining options neutrally.
- **76/06—Give equal visibility to all options.** Do not hide or de-emphasize choices that work against the system’s interest.
- **76/07—Obtain consent explicitly.** Do not pre-check, bundle, or hide consent choices.
- **76/08—Do not exploit habit.** Avoid moving or restyling controls so that routine actions trigger unintended results.
- **76/09—Honor users’ limits.** Do not let engagement features override time, spending, or notification limits users set.

### Executive summary

- Non-Manipulation is influence through information, not through exploitation.
- It excludes deception, pressure, concealment, and asymmetric friction.
- The system must make exit as easy as entry and disclose costs before commitment.
- Urgency, scarcity, and consent must be truthful and explicit.
- Options against the system’s interest must be as visible as options for it.
- Non-Manipulation succeeds when users would make the same choice with full knowledge of how the interface works.

### Success indicators

- Canceling takes no more steps than signing up.
- Full costs are visible before commitment.
- Urgency and scarcity claims are true.
- Declining options are neutral and equally visible.
- Consent choices are unchecked by default and specific.

**One-line summary:** Before users can trust a system’s guidance, it must never work against them.

