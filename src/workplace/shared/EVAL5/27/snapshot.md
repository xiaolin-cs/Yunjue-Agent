You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Obama's White House reports that a man named Frank Cordie started a brick company in 2010, in hopes of revitalizing a city's brick industry. What are the names of the streets that the elementary schools are on in this city's school district? The schools must teach up to grade 5.

# Current Instruction
**T4** — Search for elementary schools in the school district of the city where Frank Cordie started the brick company

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
- C1 | Mexico, MO is known as the Fire Brick Capital of the World.
- C2 | A.P. Green Refractories was a leading refractory manufacturing company located in Mexico, MO.
- C3 | Frank Cordie took his first job after college at a refractory plant in Mexico, MO.
- C4 | Frank Cordie spent 25 years working in the brick-manufacturing industry.
- C5 | Frank Cordie returned to Mexico, MO as the Vice President of Manufacturing for A.P. Green Refractories.
- C6 | Frank Cordie is the CEO of Mid America Brick.
- C7 | Frank Cordie began a process to bring brick manufacturing back to Mexico, MO in December 2006.
- C8 | Mid America Brick was unveiled on June 25, 2010.
- C9 | 400 community members attended the unveiling of Mid America Brick.
- C10 | Mid America Brick was founded 100 years after the founding of A.P. Green at the same location.
- C11 | Mid America Brick is helping to lead a revitalization of Mexico, MO.
- C12 | Mid America Brick provides an independent, local source of bricks for residential and commercial construction in Missouri and surrounding states.
- C13 | A photo of Mid America Brick CEO Frank Cordie at the company's plant in Mexico, MO was taken on July 6, 2011.
- C14 | The photo of Frank Cordie was taken by employees of Mid America Brick.
- C15 | Frank Cordie hosted and assisted with a White House Business Council Roundtable held in Mexico, Missouri.
- C16 | Frank Cordie is described as an energetic entrepreneur.
- C17 | Mid America Brick's plant is located in Mexico, MO.
- C18 | Eugene Field Elementary is one of the best elementary schools in Mexico 59 district.
- C19 | Hawthorne Elementary is one of the best elementary schools in Mexico 59 district.
- C20 | McMillan Early Learning Center is one of the best elementary schools in Mexico 59 district.
- C21 | Mexico School District 59 is a public school district in Missouri.
- C22 | Mexico School District 59 teachers have had 12 projects funded on DonorsChoose.
- C23 | Mexico 59 School District is located in Mexico, Missouri.
- C24 | Hawthorne Elementary School has a GreatSchools Rating of 3 out of 10.
- C25 | Eugene Field Elementary School has a GreatSchools Rating of 2 out of 10.
- C26 | Mexico High School has a National Honor Society program.
- C27 | The National Honor Society emblem represents four pillars: scholarship, service, character, and leadership.
- C28 | Hawthorne Elementary students in grades 3-5 participate in a Healthy Snacks-Kitchen Safety program.
- C29 | 141 students were honored for academic achievement at Mexico School District 59.
- C30 | Mexico Middle School hosted a school health fair providing students with physicals and preventive health screenings during the school day.
- C31 | McMillan Early Learning Center serves students in grades Pre-K through K.
- C32 | McMillan Early Learning Center is located at 1101 E Anderson St in Mexico, MO 65265.
- C33 | Dr. Casey Echelmeier is the Assistant Principal at McMillan Early Learning Center.
- C34 | Aszura Nunnelly is the Principal's Secretary at McMillan Early Learning Center.
- C35 | The phone number for McMillan Early Learning Center is 573-581-5029.
- C36 | The Kindergarten school day at McMillan Early Learning Center starts at 7:54 a.m.
- C37 | Parents as Teachers is a free service provided by Mexico Public Schools.
- C38 | Mexico School District #59 has a total of 2,426 students across all grades.
- C39 | All students in grades 3-8 and 11 in Missouri take the grade level assessment in English Language Arts and Mathematics.
- C40 | Katie Lehnen is the Principal of Hawthorne Elementary School.
- C41 | Brett Davis is the Assistant Principal of Hawthorne Elementary School.
- C42 | Brandi Schlemmer is the Principal's Secretary at Hawthorne Elementary School.
- C43 | Tiana Cook is the Attendance Secretary at Hawthorne Elementary School.
- C44 | Hawthorne Elementary School is located at 1250 W. Curtis Street, Mexico.
- C45 | Hawthorne Elementary School's phone number is 573-581-3064.
- C46 | The school day at Hawthorne Elementary School runs from 7:54 a.m. to 3:00 p.m.
- C47 | Car riders and walkers may enter Hawthorne Elementary School building at 7:24 a.m.
- C48 | Morning meeting begins in the gym at Hawthorne Elementary School at 7:39 a.m.
- C49 | All visitors to Hawthorne Elementary School must use the buzz-in system at the front entrance.
- C50 | Changes in afternoon pickup arrangements at Hawthorne Elementary School must be reported to the office by 2:30 p.m.
- C51 | Second grade lunch at Hawthorne Elementary School is from 10:45 a.m. to 11:05 a.m.
- C52 | Mexico School District #59 Central Office is located at 2101 Lakeview, Mexico, MO 65265.
- C53 | Mexico School District #59 communications email is communications@mexico.k12.mo.us.
- C54 | Mexico Public School District is an equal opportunity employer.
- C55 | Mexico Public School District prohibits discrimination and harassment on the basis of race, color, national origin, sex, age, ancestry, religion, or disability.
- C56 | Hawthorne Elementary School provides access to Clever for students.
- C57 | Mexico School District #59 has buildings including McMillan ELC, Eugene Field, Hawthorne, Mexico Middle, Mexico High, Mexico Education Center, and Hart Career Center.