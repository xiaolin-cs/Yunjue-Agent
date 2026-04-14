You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Narrow the Pulitzer Prize winners for History from the years 1990 to 1995 down to those who have either worked as a professor at an Ivy League institution or as a professor at one of the top 25 schools for history programs according to the QS World University Rankings in 2023.

# Current Instruction
**T5** — Filter the Pulitzer Prize winners for History from 1990 to 1995 to include only those who have worked as a professor at an Ivy League institution

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
- C1 | Harvard University ranked 1st in QS World University Rankings by Subject 2023 for History with a score of 98.8.
- C2 | University of Oxford ranked 2nd in QS World University Rankings by Subject 2023 for History with a score of 97.5.
- C3 | Harvard University is located in Cambridge, United States.
- C4 | University of Oxford is located in Oxford, United Kingdom.
- C5 | Sapienza University of Rome ranked 1st in QS World University Rankings by Subject 2023 for Classics and Ancient History with a score of 98.7.
- C6 | Sapienza University of Rome is located in Rome, Italy.
- C7 | University of Cambridge is located in Cambridge, United Kingdom.
- C8 | QS World University Rankings 2023 include almost 1,500 institutions from around the world.
- C9 | QS World University Rankings 2023 is based on 8 key ranking indicators.
- C10 | Fudan University ranked 2nd in QS World University Rankings for Classics and Ancient History 2026 with a score of 95.5.
- C11 | Peking University ranked 3rd in QS World University Rankings for Classics and Ancient History 2026 with a score of 91.9.
- C12 | Fudan University is located in Shanghai, China (Mainland).
- C13 | Peking University is located in Beijing, China (Mainland).
- C14 | Yale University ranked 4th in QS Subject Rankings for History 2026 with a score of 92.4.
- C15 | Stanford University ranked 5th in QS Subject Rankings for History 2026 with a score of 89.8.
- C16 | Columbia University ranked 6th (equal) in QS Subject Rankings for History 2026 with a score of 89.3.
- C17 | Princeton University ranked 8th in QS Subject Rankings for History 2026 with a score of 89.2.
- C18 | University of Pennsylvania ranked 23rd in QS Subject Rankings for History 2026 with a score of 81.5.
- C19 | University of Wisconsin–Madison ranked 42nd (equal) in QS Subject Rankings for History 2026 with a score of 77.2.
- C20 | Brown University ranked 49th in QS Subject Rankings for History 2026 with a score of 76.1.
- C21 | Yale University is located in United States.
- C22 | Stanford University is located in United States.
- C23 | Columbia University is located in United States.
- C24 | Princeton University is located in United States.
- C25 | University of Pennsylvania is located in United States.
- C26 | University of Wisconsin–Madison is located in United States.
- C27 | Brown University is located in United States.
- C28 | The Pulitzer Prizes have been honoring excellence in journalism and the arts since 1917.
- C29 | The Pulitzer Prizes are administered by Columbia University.
- C30 | The Pulitzer Prizes office is located at 709 Pulitzer Hall, 2950 Broadway, New York, NY 10027.
- C31 | The 2020 Journalism Pulitzer Prize contest deadline exists.
- C32 | Prize winners can be browsed by year on the Pulitzer Prizes website.
- C33 | The Pulitzer Prizes website offers a 'Pulitzer On The Road' program or section.
- C34 | Eight research schools make up the Ivy League.
- C35 | Harvard University is an Ivy League school.
- C36 | Yale University is an Ivy League school.
- C37 | Princeton University is an Ivy League school.
- C38 | Columbia University is an Ivy League school.
- C39 | Brown University is an Ivy League school.
- C40 | Cornell University is an Ivy League school.
- C41 | Dartmouth College is an Ivy League school.
- C42 | The Ivy League officially refers to a collegiate athletic conference.
- C43 | All eight Ivy League schools established academic, athletic, and financial standards governing intercollegiate athletics in 1954.
- C44 | Stanford University is not an Ivy League school.
- C45 | MIT is not an Ivy League school.
- C46 | Duke is not an Ivy League school.
- C47 | University of Chicago is not an Ivy League school.
- C48 | Cornell University is located in New York.
- C49 | Acceptance rates for Ivy League schools typically range from about 4% to 10%.
- C50 | Students can transfer to Ivy League schools.
- C51 | Harvard has 13 schools and institutes in addition to the undergraduate college.
- C52 | Harvard has the top-ranked U.S. medical school.
- C53 | Yale has 13 professional schools in addition to Yale College and Yale Graduate School of Arts and Sciences.
- C54 | Yale has the country's top-ranked law school.
- C55 | University of Pennsylvania has the Wharton School as one of its highly ranked graduate schools.
- C56 | Cornell has seven undergraduate colleges and schools.
- C57 | Each of Cornell's undergraduate colleges and schools admits its own students and provides its own faculty.
- C58 | Columbia University is made up of three undergraduate schools: Columbia College, the Fu Foundation School of Engineering and Applied Science, and the School of General Studies.
- C59 | Princeton is ranked the nation's top college overall by U.S. News.
- C60 | U.S. News & World Report ranks Ivy League schools against other national universities.
- C61 | Ivy Plus universities include Stanford, MIT, University of Chicago, Duke, Caltech, Johns Hopkins, Northwestern, Emory, Vanderbilt, Rice, and Georgetown.
- C62 | Ivy Plus universities are considered as prestigious as various Ivy League schools.
- C63 | The London School of Economics and Political Science (LSE) ranks 6th in the QS World University Rankings by Subject 2023 for History with an overall score of 91.2.
- C64 | University of California, Berkeley (UCB) ranks 7th in the QS World University Rankings by Subject 2023 for History with an overall score of 91.1.
- C65 | University of California, Los Angeles (UCLA) ranks 9th in the QS World University Rankings by Subject 2023 for History with an overall score of 88.8.
- C66 | University of Chicago ranks 11th in the QS World University Rankings by Subject 2023 for History with an overall score of 87.2.
- C67 | UCL ranks 12th in the QS World University Rankings by Subject 2023 for History with an overall score of 86.2.
- C68 | National University of Singapore (NUS) ranks 13th in the QS World University Rankings by Subject 2023 for History with an overall score of 85.6.
- C69 | Australian National University (ANU) ranks 13th in the QS World University Rankings by Subject 2023 for History with an overall score of 85.6.
- C70 | University of Michigan-Ann Arbor ranks 15th in the QS World University Rankings by Subject 2023 for History with an overall score of 84.9.
- C71 | University of Toronto ranks 15th in the QS World University Rankings by Subject 2023 for History with an overall score of 84.9.
- C72 | Leiden University ranks 17th in the QS World University Rankings by Subject 2023 for History with an overall score of 84.7.
- C73 | The University of Tokyo ranks 19th in the QS World University Rankings by Subject 2023 for History with an overall score of 84.1.
- C74 | Université Paris 1 Panthéon-Sorbonne ranks 20th in the QS World University Rankings by Subject 2023 for History with an overall score of 83.5.
- C75 | King's College London ranks 21st in the QS World University Rankings by Subject 2023 for History with an overall score of 83.4.
- C76 | The University of Edinburgh ranks 21st in the QS World University Rankings by Subject 2023 for History with an overall score of 83.4.
- C77 | Cornell University ranks 23rd in the QS World University Rankings by Subject 2023 for History with an overall score of 82.7.
- C78 | Johns Hopkins University ranks 26th in the QS World University Rankings by Subject 2023 for History with an overall score of 81.7.
- C79 | Ludwig-Maximilians-Universität München ranks 27th in the QS World University Rankings by Subject 2023 for History with an overall score of 81.6.
- C80 | Freie Universitaet Berlin ranks 28th in the QS World University Rankings by Subject 2023 for History with an overall score of 81.3.
- C81 | The University of Manchester ranks 28th in the QS World University Rankings by Subject 2023 for History with an overall score of 81.3.
- C82 | University of North Carolina at Chapel Hill ranks 30th in the QS World University Rankings by Subject 2023 for History with an overall score of 81.2.
- C83 | The QS World University Rankings by Subject 2023 for History includes 231 results.
- C84 | The London School of Economics and Political Science (LSE) is located in London, United Kingdom.
- C85 | University of California, Berkeley (UCB) is located in Berkeley, United States.
- C86 | Doris Kearns Goodwin is an American biographer, historian, and political commentator.
- C87 | Doris Kearns Goodwin taught at Harvard University as a professor of government for ten years.
- C88 | Doris Kearns Goodwin authored The Fitzgeralds and the Kennedys: An American Saga.
- C89 | Doris Kearns Goodwin authored Team of Rivals: The Political Genius of Abraham Lincoln.
- C90 | Doris Kearns Goodwin authored The Bully Pulpit: Theodore Roosevelt, William Howard Taft, and the Age of Journalism.
- C91 | Doris Kearns Goodwin authored Lyndon Johnson and the American Dream.
- C92 | Doris Kearns Goodwin authored No Ordinary Time: Franklin and Eleanor Roosevelt: The Home Front in World War II.
- C93 | Doris Kearns Goodwin won the New York Historical Society's inaugural American History Book Prize.
- C94 | The Corporation appointed Doris Kearns Goodwin to the position of non-tenured professor of Government for a three-year term.
- C95 | The plagiarism controversy caused Doris Kearns Goodwin to resign from the Pulitzer Prize.
- C96 | Doris Kearns Goodwin was born on January 4, 1943, in Brooklyn, New York, U.S.
- C97 | Doris Kearns Goodwin was named a White House fellow in 1967.
- C98 | President Johnson asked Doris Kearns Goodwin to help with his memoirs despite the fact that Doris Kearns Goodwin had cowritten an article critical of the Vietnam War.
- C99 | Team of Rivals: The Political Genius of Abraham Lincoln was in part the basis for Steven Spielberg's film Lincoln.
- C100 | Steven Spielberg's film Lincoln earned 12 Academy Award nominations.
- C101 | Daniel Day-Lewis won an Academy Award for his portrayal of the 16th president in Steven Spielberg's film Lincoln.
- C102 | Team of Rivals is often cited as an inspiration for business and political leaders, including President Barack Obama.
- C103 | Doris Kearns Goodwin was the first historian to receive the Lincoln Leadership Prize from the Abraham Lincoln Presidential Library Foundation in 2016.
- C104 | Doris Kearns Goodwin is a partner in Pastimes Productions.
- C105 | Doris Kearns Goodwin authored six critically acclaimed and New York Times bestselling books prior to a certain point.
- C106 | Lyndon Johnson and the American Dream drew upon interviews with President Lyndon Johnson.
- C107 | The plagiarism in The Fitzgeralds and the Kennedys was apparently unintentional.
- C108 | The senior faculty of the Government department met fairly recently to consider the Kearns decision and passed the nomination to Dean Rosovsky.
- C109 | Dean Rosovsky may have asked for department members to write revised letters of recommendation advising him of their position on Kearns.