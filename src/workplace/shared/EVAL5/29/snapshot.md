You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
By using the NHS website for “Shoulder Pain”, which of the possible causes of the condition creates symptoms like poor balance and coordination?

# Current Instruction
**T4** — Identify which cause of shoulder pain from the NHS webpage is associated with symptoms of poor balance and coordination

# Constraints
- Use the validated claims as prior evidence.
- First determine whether the current claims are sufficient to directly complete the Task Objective.
- If the Task Objective is already solvable from the claims, provide the answer in `## Final Conclusion`.
- If the Task Objective is not yet solvable, do not force a conclusion. Instead, execute the current instructions and collect the information that may be helpful for solving the Task Objective.
- Do not ask for user clarification.
- Keep the reasoning concise but operational.
- In `## Final Conclusion`, every factual statement must be supported by evidence already listed in `## Key Findings & Evidence`.

## Key Findings & Evidence
Use the following prior CLAIMS as established evidence. Preserve their identifiers and statuses.

## Reasoning & Plan
* **Analysis:** 
  - Task Objective: [Restate the task objective briefly.]
  - Current Instruction: [Restate the instruction briefly.]
  - Sufficiency Check: Determine whether the validated claims already contain enough information to fully answer the Task Objective.
  - Gap Check: If not sufficient, identify exactly what is missing.

* **Plan:** 
  - If sufficient: explain how you will synthesize the existing claims into the final answer.
  - If insufficient: propose the next concrete instruction(s) that should be executed to obtain the missing evidence.
  - Prefer instructions that are atomic, directly verifiable, and dependency-aware.
  - If insufficient: propose the tool call(s) required to execute the instruction(s) when necessary.

### Prior Claims
- C1 | Shoulder pain can be caused through injury.
- C2 | ACJ pain causes pain on the outside of the shoulder and often into the upper arm.
- C3 | Shoulder impingement is where a tendon inside the shoulder swells and rubs against tissue or bone, causing pain as the arm is lifted.
- C4 | A person should see a GP if shoulder pain does not go away after a few weeks.
- C5 | A physiotherapist can diagnose shoulder impingement.
- C6 | A GP can prescribe a stronger painkiller for shoulder impingement if needed.
- C7 | A person should seek urgent medical advice if an injury to the shoulder has caused significant pain and weakness or difficulty lifting the arm up.
- C8 | A person should seek urgent medical advice if they have noticed any unusual lump or swelling around the neck, shoulder, or arm.
- C9 | A person should seek urgent medical advice if they have hot red skin in the region of pain.
- C10 | A person should seek urgent medical advice if they are feeling unwell or have a fever since shoulder pain started.
- C11 | A person should contact their GP or TIMS if pain is getting worse or not improving despite taking painkillers and doing the recommended exercises.
- C12 | People should try to use their shoulder more because exercise really helps the shoulder and can relieve pain.
- C13 | If a person has any issues with circulation or sensation, they should not use ice or heat as a treatment for shoulder pain.
- C14 | Osteoarthritis of the shoulder is a common condition related to shoulder pain.
- C15 | If shoulder pain symptoms worsen or fail to improve, it is important to seek an assessment by a physiotherapist.
- C16 | Physiotherapy assessment is often possible at GP surgery for shoulder pain.
- C17 | If a person develops sudden marked weakness in shoulder or arm, the person should seek an assessment as soon as possible at GP surgery, preferably with a physiotherapist.
- C18 | GP or physiotherapist can assess and advise whether a person with sudden shoulder or arm weakness requires further investigations or scans.
- C19 | Common conditions related to shoulder pain include osteoarthritis of the shoulder, rotator cuff related shoulder pain, and acromioclavicular joint pain.
- C20 | Rotator cuff related shoulder pain presents with pain over outside of shoulder that can refer down the arm.
- C21 | The shoulder is a ball and socket joint.
- C22 | The shoulder is made up of three bones called the collar bone (clavicle), shoulder blade (scapula), and the long bone of the arm (humerus).
- C23 | There are four particular muscles in the shoulder called the rotator cuff.
- C24 | Rotator cuff muscles work to keep the shoulder held into its socket.
- C25 | Self-help measures are the initial treatment for most shoulder pain.
- C26 | Common shoulder conditions include rotator cuff injuries, frozen shoulder (adhesive capsulitis), shoulder impingement, arthritis, shoulder dislocation, and labral tear.
- C27 | A person usually needs to do self-management things for 2 weeks before shoulder pain starts to ease.
- C28 | A pharmacist can help with shoulder pain.
- C29 | The Chartered Society of Physiotherapy provides video exercises for shoulder pain.
- C30 | A GP will examine a person to work out what is causing shoulder pain.
- C31 | The number of physiotherapy sessions a person may have depends on the cause of shoulder pain.
- C32 | Common causes of non-traumatic shoulder and elbow issues exist.
- C33 | British Elbow and Shoulder Society (BESS) has useful information to assist patients with shoulder or elbow conditions.
- C34 | BESS provides advice and videos demonstrating exercises to help shoulder pain and elbow stiffness.
- C35 | American Academy of Orthopaedic Surgeons (AOSS) provides helpful information on shoulder and elbow conditions.
- C36 | NHS Inform has useful links and information about self-management of shoulder conditions including self-help guides, tips on recovery, exercises, and treatments.
- C37 | Shoulder exercises should be performed for 6 to 8 weeks to prevent pain from returning.
- C38 | Paracetamol is a recommended painkiller for shoulder pain.
- C39 | Ibuprofen is a recommended painkiller for shoulder pain.
- C40 | A pack of frozen peas wrapped in a tea towel can be applied to the shoulder for up to 20 minutes, 3 times a day.
- C41 | An urgent GP appointment is needed if a person has sudden or very bad shoulder pain.
- C42 | NHS 111 can be contacted for urgent shoulder pain concerns.
- C43 | A person may be able to self-refer for physiotherapy from NHS community musculoskeletal services without needing a GP referral.
- C44 | A GP may send a patient for tests such as an X-ray to check the cause of shoulder pain.
- C45 | GP treatments for shoulder pain may include stronger medicine or injections to ease pain and swelling.
- C46 | Physiotherapy is available through the NHS, but waiting times can be long.
- C47 | Physiotherapy can be obtained privately for shoulder pain.
- C48 | Pain and stiffness that does not go away over months or years may be caused by frozen shoulder.
- C49 | Tingling, numbness, weak arm, and feelings of the shoulder clicking or locking may be caused by shoulder instability.
- C50 | Pain on top of the shoulder where the collarbone and shoulder joint meet may be caused by problems in the acromioclavicular joint.
- C51 | Completely stopping use of the shoulder can prevent it from getting better.
- C52 | Slouching when sitting should be avoided for shoulder pain management.
- C53 | Rolling shoulders or bringing the neck forward should be avoided for shoulder pain management.
- C54 | Strenuous self-made exercises or heavy gym equipment should be avoided for shoulder pain management.
- C55 | Joint hypermobility syndrome is when a person has very flexible joints.
- C56 | People with joint hypermobility syndrome often get tired, even after rest.
- C57 | A GP will usually test for joint hypermobility syndrome by checking the flexibility of joints using the Beighton scoring system.
- C58 | A GP may refer a patient to a physiotherapist, occupational therapist or podiatrist for specialist advice regarding joint hypermobility syndrome.
- C59 | Paracetamol may help to ease joint pain in joint hypermobility syndrome.
- C60 | Ibuprofen comes as tablets, gels and sprays.
- C61 | A GP may be able to prescribe stronger painkillers for joint hypermobility syndrome.
- C62 | A GP may be able to refer a patient in severe pain to a pain clinic to help cope with pain.
- C63 | Having warm baths can help ease joint pain and stiffness in joint hypermobility syndrome.
- C64 | Low-impact exercise like swimming or cycling is recommended for people with joint hypermobility syndrome who have not been active before.
- C65 | Wearing supportive shoes can help manage joint hypermobility syndrome.
- C66 | Wearing special insoles (orthotics) in shoes can help if a podiatrist has recommended them for joint hypermobility syndrome.
- C67 | The NHS website page on joint hypermobility syndrome was last reviewed on 30 August 2023.