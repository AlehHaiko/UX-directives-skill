# Chapter 9: AI-Mediated Interaction

> **How users interact with systems whose behavior is probabilistic or changes through learning.**
>
> These constrain intelligent systems to support human judgment without replacing it.

**Mission statement:** Ensure intelligent systems support human judgment responsibly by making system behavior understandable, controllable, and trustworthy.

## 9.1 Human Oversight

> Who remains accountable.

**Ask yourself:** “Is human responsibility in your system explicit and exercisable at all times?”

**Mission:** Ensure users remain in control by enabling monitoring and intervention while avoiding blind automation.

**Executive brief:** AI systems must keep an identifiable human accountable for outputs that may be wrong in ways no fixed rule predicts.

### Key heuristics

- Responsibility within automated systems must remain clearly assigned to a human actor.
- Monitoring and intervention responsibilities must be clearly defined.
- System actions, state, and rationale must be sufficiently exposed for review.
- Decision power must be proportionate to consequence severity.
- Humans must be able to influence outcomes before harm occurs.
- Systems must allow interruption and correction during execution.
- Automated processes must not perform irreversible actions without human confirmation.
- Human involvement must increase as risk increases.
- Automated decisions must be logged and reviewable.
- Humans must be able to disagree with and correct automated outcomes.

### Core questions

- “When the system acts, does a clearly identified human bear responsibility?”
- “Can that person actually understand and intervene?”

### Focus areas

- **Accountability-first:** “Who answers for this outcome?” “Where does responsibility land when automation acts?”
- **Control-first:** “Can a human stop, change, or reverse the action?” “Is oversight real, or just symbolic?”
- **Governance-aware:** “Is there a clear escalation path for intervention?” “Are roles and decision rights explicitly defined?”
- **AI-aware:** “Are automated actions bounded and explainable?” “Does AI behavior remain subordinate to human accountability?”

### Directives

- **91/01—Preserve human accountability in automated systems.** Ensure responsibility remains clearly assigned to a human actor.
- **91/02—Define oversight roles explicitly.** Clarify who is responsible for monitoring and intervention.
- **91/03—Provide sufficient visibility into system behavior.** Expose actions, state, and rationale necessary for oversight.
- **91/04—Align oversight authority with risk and consequence.** Grant decision power proportionate to accountability.
- **91/05—Enable real-time intervention capabilities.** Ensure humans can meaningfully influence outcomes before harm occurs.
- **91/06—Design for safe, preemptive intervention.** Support interruption and correction during execution.
- **91/07—Maintain interruptibility of automated processes.** Prevent irreversible actions without human confirmation.
- **91/08—Calibrate oversight rigor to consequence severity.** Increase human involvement for high-risk scenarios.
- **91/09—Ensure traceability of automated decisions.** Maintain logs and records to support review and accountability.
- **91/10—Design systems to enable meaningful override.** Support human disagreement and correction of automated outcomes.

### Executive summary

- Human Oversight is preserved accountability in automated systems, not symbolic supervision.
- It ensures an identifiable human answers for outputs that can be wrong without warning.
- The system must provide sufficient visibility, traceability, and rationale to enable informed intervention.
- Oversight authority and rigor must scale with risk and consequence severity.
- Automated processes must remain interruptible, reversible, and subject to meaningful override.
- Human Oversight succeeds when automation strengthens human judgment without displacing responsibility.

### Success indicators

- Human responsibility for automated outcomes is clearly defined.
- System actions and state are visible to human overseers.
- Humans can intervene before harmful outcomes occur.
- Automated processes remain interruptible and overridable.
- System decisions are traceable for review and accountability.

**One-line summary:** Before intelligence can act, responsibility must remain human.

## 9.2 Learning Consent

> What a system may learn and apply.

**Ask yourself:** “Do users of your system authorize what it learns from them and how it applies it?”

**Mission:** Ensure users decide what the system learns from them and how learned behavior is applied.

**Executive brief:** AI systems must learn from users, and act on what they learn, only within consent users can review and revoke.

### Key heuristics

- Learning from user data must be treated as authority delegated by the user.
- Users must know what the system learns from them and for what purpose.
- The scope of learning must be explicit: which data, which features, and for how long.
- Consent rigor must increase with the sensitivity of what is learned.
- Learned behavior must not drive consequential actions without separate authorization.
- Users must be able to inspect and correct what the system has learned about them.
- Withdrawing consent must remove learned data and behavior without loss of user work.
- The scope of learning must not broaden without renewed consent.
- Inferred preferences must remain subordinate to explicit user instructions.

### Core questions

- “What has the system learned from users, and did they agree to it?”
- “Can users see it, correct it, or make the system forget it?”

### Focus areas

- **Delegation-first:** “What is the system learning without being asked?” “Which learned behaviors act without explicit confirmation?”
- **Scope-aware:** “Which data and features does learning cover?” “Is consent global or limited to a specific context?”
- **Change-aware:** “What happens to learned behavior when users withdraw consent?” “Can learning be paused without losing core functionality?”
- **AI-aware:** “Is inferred intent being treated as permission?” “Does learning expand authority without explicit approval?”

### Directives

- **92/01—Treat learning from users as delegated authority.** Require explicit consent before user data shapes system behavior.
- **92/02—Make learning consent clear and comprehensible.** Explain what is learned, from which data, and for what purpose.
- **92/03—Expose the scope of learning.** Indicate which data, features, and time periods learning covers.
- **92/04—Scale consent rigor with sensitivity.** Require stronger acknowledgment for learning from personal or high-impact data.
- **92/05—Separate learning from acting.** Require distinct authorization before learned behavior drives consequential actions.
- **92/06—Make learned behavior inspectable and correctable.** Allow users to see and edit what the system has learned about them.
- **92/07—Ensure learning can be withdrawn.** Remove learned data and behavior when users revoke consent, without loss of their work.
- **92/08—Prevent silent scope expansion.** Require renewed consent if learning extends to new data or purposes.
- **92/09—Do not treat inference as instruction.** Keep inferred preferences subordinate to what users explicitly state.

### Executive summary

- Learning Consent treats learning from users as delegated authority, not a by-product of use.
- It requires explicit, comprehensible consent before user data shapes system behavior.
- The system must make the scope, purpose, and sensitivity of learning clear.
- Learning and acting on what was learned must be authorized separately.
- Users must be able to inspect, correct, and withdraw what the system has learned.
- Learning Consent succeeds when system adaptation remains fully subordinate to explicit user intent.

### Success indicators

- Users know what the system learns from them.
- Learning occurs only after explicit consent.
- Users can see and correct what the system has learned.
- Withdrawing consent removes learned data and behavior.
- Changes to the scope of learning require renewed consent.

**One-line summary:** Before a system learns from users, users must choose what it may learn.

## 9.3 Predictability

> Why stability matters more than surprise.

**Ask yourself:** “Can users of your system reliably predict its behavior?”

**Mission:** Ensure users anticipate predictable outcomes by stabilizing system behavior and minimizing unexpected results.

**Executive brief:** AI systems must behave predictably to earn user trust.

### Key heuristics

- System actions must align with established user expectations.
- Variation across comparable scenarios must be explained or expected.
- Stable behavioral patterns must be exposed over internal complexity.
- System variability must be constrained and clearly communicated.
- Users must be told when identical inputs can produce different outputs.
- Output variability must stay within communicated bounds.
- Meaningful changes to system logic must not occur silently.
- Behavioral transparency must increase as automation increases.
- Scaling and updates must preserve established behavioral expectations.

### Core questions

- “Is the system’s behavior predictable enough for users to rely on it?”
- “Does it behave the way users expect?”

### Focus areas

- **Expectation-first:** “Can users form reliable expectations about behavior?” “Do similar inputs produce similar outcomes?”
- **Boundary-aware:** “Where does predictability end? Is that clear?” “Are edge cases predictable or at least signaled?”
- **Consistency-aware:** “Are patterns uniform across screens, states, and contexts?” “Does the system reinforce learned expectations over time?”
- **AI-aware:** “Is variability explainable and bounded?” “Does AI learning improve reliability without surprising users?”

### Directives

- **93/01—Design behavior users can reliably anticipate.** Ensure system actions align with established expectations.
- **93/02—Explain variation across comparable scenarios.** When similar inputs yield different outputs, show why or show that variation is expected.
- **93/03—Expose stable behavioral patterns, not internal complexity.** Prioritize outcome clarity over algorithmic explanation.
- **93/04—Constrain and signal system variability.** Communicate when behavior may differ from prior patterns.
- **93/05—Make output variability explicit.** Tell users when the same input can yield different results.
- **93/06—Keep variability within stated bounds.** Do not let outputs vary beyond the range users were led to expect.
- **93/07—Prevent unannounced behavioral drift.** Communicate meaningful changes to system logic.
- **93/08—Strengthen predictability in automated workflows.** Increase behavioral transparency as autonomy rises.
- **93/09—Preserve expectation stability during scaling and updates.** Ensure expansion does not invalidate prior learning.

### Executive summary

- Predictability is reliable expectation alignment, not rigid uniformity.
- It ensures users can anticipate outcomes based on prior interaction.
- The system must produce consistent results in comparable contexts and signal meaningful variability.
- Probabilistic variability must be explicit and kept within stated bounds.
- Behavioral drift and logic changes must be communicated before they invalidate prior learning.
- Predictability succeeds when users can act confidently because system behavior remains stable, transparent, and foreseeable.

### Success indicators

- System behavior matches user expectations.
- Similar actions produce consistent results in similar situations.
- Users can anticipate the outcome of their actions.
- Output variability is clearly communicated.
- Behavioral changes are announced and explained.

**One-line summary:** Before users can rely on intelligent behavior, they must be able to anticipate it.

## 9.4 Explainability

> How results are understood.

**Ask yourself:** “Can users understand and contest outcomes in your system?”

**Mission:** Ensure users understand outputs by providing clear reasoning and context.

**Executive brief:** AI systems must explain individual outputs that no fixed rule produced, well enough to accept or contest them.

### Key heuristics

- Explanations must directly support informed user decisions.
- Explanations must surface outcome-influencing factors in user-relevant terms.
- Explanations must address the specific output, not only the system in general.
- Explanations must be faithful to what actually produced the output.
- Explanations must show which inputs would change the outcome.
- Explanation mechanisms must strengthen as automation increases.
- Users must be able to question and challenge outcomes with understanding.

### Core questions

- “Is the system’s output clear enough for users to accept, reject, or correct it?”
- “Can users make reliable judgments about the result?”

### Focus areas

- **Judgment-first:** “Can users tell whether the output makes sense in this context?” “Do they know when to rely on it and when not to?”
- **Action-first:** “What can users do if they believe the result is wrong?” “Is disagreement actionable or only theoretical?”
- **Boundary-aware:** “Which parts of the output are certain? Which are inferred?” “Where does explanation end? Is that limit clear?”
- **AI-aware:** “Is AI’s reasoning transparent enough to support user judgment?” “Are inferred or generated elements clearly distinguishable from deterministic results?”

### Directives

- **94/01—Design explanations to enable informed judgment.** Ensure explanatory content directly supports user decisions.
- **94/02—Surface causal factors rather than technical mechanisms.** Explain what influenced the outcome in user-relevant terms.
- **94/03—Explain the individual output.** Give the reasons for this result in this case, not only a general account of how the model works.
- **94/04—Keep explanations faithful to the model.** Do not present plausible rationales that did not produce the output.
- **94/05—Show what would change the outcome.** Indicate which inputs, if different, would have produced a different result.
- **94/06—Repealed.** Merged into 72/05—Increase explanatory depth for high-risk outcomes.
- **94/07—Increase transparency as autonomy increases.** Strengthen explanation mechanisms in automated workflows.
- **94/08—Enable informed disagreement.** Allow users to challenge outcomes with understanding.
- **94/09—Repealed.** Merged into 72/06—Enable correction mechanisms alongside explanation.

### Executive summary

- Explainability is decision-supporting clarity, not technical disclosure.
- It reveals causal factors in user-relevant terms rather than exposing internal mechanisms.
- The system must explain individual outputs faithfully, including what would have changed them.
- Explanatory depth follows the general provisions on proportionality and automation rigor.
- Explanation must enable informed disagreement and meaningful corrective action.
- Explainability succeeds when users can understand, question, and responsibly act on system outcomes.

### Success indicators

- Users can understand why the system produced a result.
- Explanations focus on factors that influenced the outcome.
- Explanations appear when users need to make decisions.
- Users can see what would have changed the result.
- Users can question or correct system outcomes with understanding.

**One-line summary:** Before users can trust outcomes, they must understand them well enough to agree or disagree.

## 9.5 Confidence Signaling

> How certainty and uncertainty are conveyed.

**Ask yourself:** “Does your system signal uncertainty to users honestly and actionably?”

**Mission:** Ensure users calibrate trust by communicating uncertainty appropriately.

**Executive brief:** AI systems must signal confidence in ways users can reliably act on.

### Key heuristics

- Expressed confidence must reflect actual system reliability.
- Uncertainty must be surfaced directly, not implied through silence.
- Different sources of uncertainty must be clearly distinguished.
- Presentation polish must not imply greater accuracy than exists.
- Confidence signaling must increase in clarity and prominence as consequence increases.
- Confidence signals must inform recommended action thresholds.
- Expressed confidence levels must remain consistent across updates.
- Confidence signaling must strengthen as workflows become more automated.
- Confidence and uncertainty signals must remain perceivable under urgency.

### Core questions

- “Does the system clearly communicate how reliable its output is?”
- “Do users know what to do when confidence is low?”

### Focus areas

- **Calibration-first:** “Is confidence proportional to certainty?” “Does the system avoid overstating or understating reliability?”
- **Action-first:** “What should users do when confidence is low?” “Is uncertainty accompanied by clear guidance?”
- **Risk-aware:** “Do higher-risk outcomes get stronger signaling?” “Are low-confidence results clearly marked?”
- **AI-aware:** “Does the system distinguish fact, inference, and guess?” “Is uncertainty exposed, not hidden behind fluent output?”

### Directives

- **95/01—Calibrate confidence to actual reliability.** Refrain from overstating certainty in system outputs.
- **95/02—Surface uncertainty explicitly.** Ensure absence of signal does not imply correctness.
- **95/03—Differentiate uncertainty sources.** Clarify whether uncertainty arises from missing data, model limits, or ambiguity.
- **95/04—Separate presentation fluency from reliability.** Prevent polished output from implying unwarranted accuracy.
- **95/05—Scale confidence signaling to risk level.** Increase clarity and prominence for high-impact decisions.
- **95/06—Tie confidence signals to recommended action.** Provide guidance when reliability falls below threshold.
- **95/07—Maintain stable calibration across updates.** Safeguard against unexplained shifts in expressed confidence levels.
- **95/08—Increase signaling rigor in automated workflows.** Strengthen transparency when actions are delegated.
- **95/09—Ensure clarity under high-pressure conditions.** Design signals that remain perceivable during urgency.

### Executive summary

- Confidence Signaling is calibrated reliability communication, not rhetorical certainty.
- It aligns expressed confidence with actual system performance and limitations.
- The system must make uncertainty explicit and differentiate its sources clearly.
- Fluency of presentation must never imply accuracy beyond verified reliability.
- Confidence signals must scale with risk, autonomy, and decision impact.
- Confidence Signaling succeeds when users interpret system outputs with appropriately calibrated trust.

### Success indicators

- Confidence levels match the system’s actual reliability.
- Uncertainty is clearly indicated when results may be incorrect.
- Different sources of uncertainty are distinguishable.
- Polished presentation does not imply false certainty.
- Confidence signals clearly guide user decisions.

**One-line summary:** Before trust can be calibrated, confidence and uncertainty must be visible.

## 9.6 Graceful Failure

> What happens when intelligence breaks.

**Ask yourself:** “Does your system behave responsibly when intelligence fails?”

**Mission:** Ensure users recover from system limitations by degrading safely without abrupt breakdown.

**Executive brief:** AI systems must behave responsibly even when intelligence fails.

### Key heuristics

- Systems must assume incorrect outputs will occur and default to safe containment.
- Failures must remain within controlled boundaries.
- Uncertain actions must be declined, not executed unreliably.
- Uncertainty, refusal, or degraded performance must be clearly communicated.
- Autonomous action must decrease as uncertainty increases.
- High-impact capabilities must be restricted when reliability drops.
- Conservative modes or human oversight must activate under failure conditions.
- User data and task continuity must remain intact during failure events.
- Systems must support correction, override, or safe continuation after failure.

### Core questions

- “When intelligence fails, does the system remain safe, controlled, and accountable?”
- “Can users rely on it even when intelligence is degraded?”

### Focus areas

- **Safety-first:** “What happens when the model is uncertain or incorrect?” “Does failure reduce harm, or could it make things worse?”
- **Control-first:** “Does the system defer to human control when needed?” “Are risky actions blocked when confidence drops?”
- **Transparency-first:** “Is failure visible and acknowledged?” “Does the system admit its limits instead of improvising?”
- **AI-aware:** “Are model errors clearly communicated to users?” “Does intelligent behavior stay predictable and bounded even under failure?”

### Directives

- **96/01—Design systems to fail safely by default.** Assume incorrect outputs will occur and plan containment accordingly.
- **96/02—Contain failure within controlled boundaries.** Prevent cascading or system-wide consequences.
- **96/03—Implement conservative refusal policies.** Decline uncertain actions rather than generate unreliable outputs.
- **96/04—Communicate failure transparently.** Clearly indicate uncertainty, refusal, or degraded performance.
- **96/05—Increase restraint as uncertainty rises.** Reduce autonomous action under low confidence.
- **96/06—Restrict high-impact capabilities when reliability drops.** Align action permissions with certainty levels.
- **96/07—Provide explicit, safe fallback paths.** Activate conservative modes or human oversight when failure conditions arise.
- **96/08—Protect user progress during failure events.** Ensure data and task continuity remain intact.
- **96/09—Enable structured recovery after failure.** Support correction, override, or safe continuation.

### Executive summary

- Graceful Failure is controlled degradation, not uncontrolled breakdown.
- It assumes error and uncertainty as normal conditions and plans containment in advance.
- The system must restrict, refuse, or reduce action as reliability declines.
- Failure states must be transparent, bounded, and aligned with consequence severity.
- User progress and data must remain protected during degraded operation.
- Graceful Failure succeeds when incorrect or uncertain outcomes are contained without cascading harm or loss of trust.

### Success indicators

- The system limits harm when errors occur.
- Failures are contained and do not spread across the system.
- The system clearly communicates when it cannot complete a task.
- Uncertain situations lead to conservative or safe system behavior.
- Users can recover and continue work after a failure.

**One-line summary:** Before intelligence can be trusted, failure must be survivable.

## 9.7 Provenance

> What data influenced outcomes.

**Ask yourself:** “Can users of your system see what data shaped an outcome and its scope?”

**Mission:** Ensure users can verify origins by exposing data and decision sources.

**Executive brief:** AI systems must show which data—training, retrieved, or supplied at inference—shaped an output, so users can judge trust in context.

### Key heuristics

- Outcomes must be traceable to identifiable sources.
- Data sources must be reviewable and inspectable.
- Contributions from multiple origins must be distinguished and labeled.
- Derived outputs must remain linked to original data.
- The relevance of sources to the current situation must be indicated.
- Timestamps and update cycles must be communicated.
- Incomplete or ambiguous sourcing must be clearly highlighted.
- Traceability mechanisms must strengthen as automation scales.
- Users must be able to question and verify inputs through visible provenance.

### Core questions

- “What sources and data contributed to this result?”
- “Are they appropriate and trustworthy for this context?”

### Focus areas

- **Source-first:** “Where did this information come from?” “What evidence supports it?”
- **Context-aware:** “Is the data valid for this decision?” “Has context changed since the data was gathered?”
- **Trust-aware:** “What assumptions does this data carry?” “Is anything missing, outdated, or misleading?”
- **AI-aware:** “Are training, retrieval, and inference-time data clearly distinguished?” “Is synthetic or generated data labeled transparently?”

### Directives

- **97/01—Trace outcomes to identifiable sources.** Ensure users can see where information originates.
- **97/02—Make data sources accessible and reviewable.** Provide inspectable references for inputs and influences.
- **97/03—Attribute composite inputs explicitly.** Distinguish and label contributions from training data, retrieved sources, and user-supplied input.
- **97/04—Maintain traceability through transformations.** Ensure derived outputs link back to original data.
- **97/05—Surface contextual suitability of sources.** Indicate when data may not apply to the current situation.
- **97/06—Display data recency clearly.** Communicate timestamps and update cycles for inputs.
- **97/07—Signal incomplete or uncertain origins.** Highlight missing attribution or ambiguous sourcing.
- **97/08—Increase provenance rigor in automated systems.** Strengthen traceability as automation scales.
- **97/09—Enable challenge through traceability.** Design systems so users can question and verify inputs.

### Executive summary

- Provenance is traceable origin, not opaque output.
- It enables users to see where information comes from and how it was formed.
- The system must make sources, transformations, and composite contributions inspectable and attributable.
- Recency, contextual suitability, and uncertainty of inputs must be explicit.
- Traceability rigor must increase as automation and scale increase.
- Provenance succeeds when users can verify, question, and trust outputs through visible lineage.

### Success indicators

- Users can see where information comes from.
- Data sources are visible and easy to inspect.
- Contributions from multiple sources are clearly identified.
- Derived results link back to their original data.
- Users can verify and question the origin of information.

**One-line summary:** Before users can judge results, they must know what informed them.

## 9.8 Bias Management

> Where distortions may arise.

**Ask yourself:** “Are sources of bias in your system visible and mitigable to users?”

**Mission:** Ensure users receive fair outcomes by detecting and mitigating bias.

**Executive brief:** AI systems learn bias from their data, so they must identify systematic bias and enable responsible correction.

### Key heuristics

- Bias must be treated as a systemic risk, not an isolated defect.
- Bias risks must be assessed and mitigated before deployment.
- Systems must be instrumented to detect bias actively.
- Bias must be evaluated based on measurable outcome effects.
- Bias mitigation rigor must scale with domain consequence.
- Potential bias risks must be visible where relevant.
- Users must have mechanisms to report, correct, or override biased outcomes.
- Autonomous decisions must be limited where fairness risks are high.

### Core questions

- “Where is the system likely to fail certain people or cases?”
- “What is the accountable response when it does?”

### Focus areas

- **Detection-first:** “Who might the system disadvantage by design?” “What patterns of error repeat across groups or contexts?”
- **Action-first:** “What safeguards activate when bias is detected?” “Can users escalate, override, or compensate?”
- **Risk-aware:** “What harm could bias cause?” “Are responses calibrated to the level of risk?”
- **AI-aware:** “Is bias in training data visible and mitigated?” “Does AI learning amplify or reduce disparities over time?”

### Directives

- **98/01—Treat bias as a systemic risk.** Design structural safeguards rather than ad hoc corrections.
- **98/02—Integrate bias prevention into design.** Assess and mitigate bias risks before deployment.
- **98/03—Instrument systems to detect bias proactively.** Measure fairness rather than assuming neutrality.
- **98/04—Evaluate bias by outcome impact.** Prioritize measurable effects over stated intentions.
- **98/05—Calibrate bias safeguards to domain risk.** Increase rigor in high-consequence environments.
- **98/06—Surface fairness indicators where relevant.** Make potential bias risks perceptible to users.
- **98/07—Provide actionable mitigation pathways.** Enable reporting, correction, or override when bias is detected.
- **98/08—Escalate to human review in sensitive contexts.** Limit autonomous decisions where fairness risks are high.

### Executive summary

- Bias Management treats bias as a systemic risk, not an isolated defect.
- It embeds structural safeguards into design rather than relying on reactive correction.
- The system must instrument, measure, and evaluate bias by observable outcome impact.
- Safeguards and human review must scale with domain risk and consequence severity.
- Fairness indicators and mitigation pathways must be visible and actionable.
- Bias Management succeeds when inequitable outcomes are detected early and corrected before harm propagates.

### Success indicators

- The system monitors outcomes for potential bias.
- Fairness risks are visible when they affect decisions.
- Bias detection is based on measurable outcomes.
- Users can report or correct biased results.
- Sensitive decisions allow human review or intervention.

**One-line summary:** Before intelligent output can be used responsibly, bias must be exposed and managed.

## 9.9 Trust Calibration

> How reliance is adjusted over time.

**Ask yourself:** “Is user trust aligned with actual system capability over time?”

**Mission:** Ensure users rely appropriately by aligning perceived and actual system capability without overtrust or undertrust.

**Executive brief:** AI systems must actively maintain appropriate user trust over time.

### Key heuristics

- User reliance must match actual system reliability.
- Defaults, messaging, and permissions must track measured reliability over time.
- Trust mechanisms must adjust to task type and risk domain.
- Consistent experiential reliability must underpin trust.
- Reliance on delegated actions must be monitored and adjusted.
- Reliance mechanisms must be monitored and adjusted over time.
- Increased reliance must follow demonstrable performance improvement.
- Trust signals and permissions must decrease when performance declines.
- Overtrust and undertrust must be addressed before patterns solidify.

### Core questions

- “Is user trust proportional to actual system reliability?”
- “Does trust stay aligned with reality as the system evolves?”

### Focus areas

- **Calibration-first:** “Are users overrelying or underrelying on the system?” “Does observed behavior indicate misplaced confidence?”
- **Drift-aware:** “How can trust drift be detected over time?” “Do improvements or degradations adjust reliance appropriately?”
- **Transparency-aware:** “Are changes in reliability communicated clearly?” “Can users see when updates affect system behavior?”
- **AI-aware:** “Does AI learning change reliability without changing signals?” “Are updates recalibrating trust honestly and visibly?”

### Directives

- **99/01—Align user reliance with actual system reliability.** Design mechanisms that prevent both overreliance and avoidance.
- **99/02—Keep trust signals current with measured performance.** Update defaults, messaging, and permissions as measured reliability changes over time.
- **99/03—Calibrate trust contextually.** Adjust signaling and controls according to task and risk domain.
- **99/04—Reinforce trust through consistent outcomes.** Prioritize experiential reliability over declarative assurance.
- **99/05—Track reliance in delegated workflows.** Monitor whether users over- or under-rely on delegated actions and adjust oversight accordingly.
- **99/06—Continuously reassess trust alignment.** Monitor and adjust reliance mechanisms over time.
- **99/07—Signal reliability improvements transparently.** Increase permitted reliance only when performance demonstrably improves.
- **99/08—Reduce trust signals when performance declines.** Promptly adjust confidence and permissions in response to degradation.
- **99/09—Provide immediate feedback to correct miscalibration.** Address overtrust or undertrust before patterns solidify.

### Executive summary

- Trust Calibration aligns user reliance with actual system reliability, not perceived competence.
- It prevents both overreliance and avoidance by synchronizing signals with measured performance.
- The system must calibrate confidence, defaults, and permissions according to task risk and context.
- Trust must be reinforced through consistent outcomes, not declarative assurance.
- Reliance on delegated actions must be monitored, not assumed.
- Trust Calibration succeeds when reliance adjusts dynamically as performance improves or degrades.

### Success indicators

- User reliance matches the system’s actual reliability.
- Confidence signals reflect real system performance.
- Trust signals adjust according to task risk and context.
- Consistent outcomes reinforce appropriate user trust.
- The system corrects overtrust or undertrust through clear feedback.

**One-line summary:** Before trust can be stable, it must match actual system capability.

## 9.10 Non-Anthropomorphism

> How to prevent false human attribution.

**Ask yourself:** “Does your system present itself honestly to users as a tool, not a human agent?”

**Mission:** Ensure users form accurate mental models by presenting the system as a tool while avoiding human-like cues.

**Executive brief:** AI systems must avoid human-like framing or language that may imply sentient comprehension.

### Key heuristics

- System design must prevent false human attribution.
- Cues must not imply human emotion, empathy, or intent.
- Language must reflect functional capability, not awareness or desire.
- Outputs must be framed as computational processes, not deliberate acts.
- System constraints, uncertainties, and boundaries must be clearly communicated.
- Responsibility must not shift to a system persona.
- Metaphors must avoid implying thought, belief, or motive.
- Polished interaction must not imply comprehension or epistemic authority.
- Human-like interaction patterns must be reduced in high-risk contexts.

### Core questions

- “Does the system clearly communicate what it is?”
- “Does it prevent users from attributing human intent, understanding, or agency?”

### Focus areas

- **Mental-model first:** “What does the interface teach users about the system?” “Is the interface encouraging accurate understanding or social projection?”
- **Responsibility-aware:** “Does personification obscure accountability?” “Are decisions framed as system behavior rather than human judgment?”
- **Interaction-aware:** “Is system feedback interpreted without anthropomorphizing?” “Does the UI reinforce correct causal reasoning about the system?”
- **AI-aware:** “Are uncertainty and limits made explicit?” “Does language exaggerate intelligence, care, or agency?”

### Directives

- **910/01—Design to prevent false human attribution.** Actively discourage mental models that treat the system as a person.
- **910/02—Prevent cues that imply human emotion or intent.** Do not simulate empathy or consciousness to increase engagement.
- **910/03—Use language that reflects functional capability.** Avoid phrasing that implies awareness, desire, or understanding.
- **910/04—Represent system agency truthfully.** Frame outputs as computational processes, not deliberate actions.
- **910/05—Make system limitations explicit.** Clearly communicate constraints, uncertainties, and boundaries.
- **910/06—Preserve human accountability in system framing.** Ensure responsibility is not shifted to the system persona.
- **910/07—Prefer functional metaphors over social metaphors.** Refrain from metaphors that imply thought, belief, or motive.
- **910/08—Separate fluency from epistemic authority.** Prevent polished interaction from implying comprehension.
- **910/09—Limit human-like interaction patterns in high-risk contexts.** Reduce social signaling where overtrust would be harmful.

### Executive summary

- Non-Anthropomorphism prevents false human attribution, not expressive interaction.
- It ensures users understand the system as a computational process, not a person with intent or emotion.
- The system must use functional language and avoid cues that imply awareness, belief, or motive.
- Fluency of interaction must never imply comprehension or epistemic authority.
- Limitations, boundaries, and accountability must remain explicit and human-centered.
- Non-Anthropomorphism succeeds when users reason about capability accurately without projecting agency where none exists.

### Success indicators

- The system is presented as a tool, not a person.
- Language describes functions rather than thoughts or feelings.
- The system’s limits and uncertainties are clearly communicated.
- Responsibility remains clearly attributed to human actors.
- Polished responses do not imply human understanding or intent.

**One-line summary:** Before users can understand what the system is, it must not present itself as a human agent.
