You are given a task context consisting of an overall objective and previously validated claims.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
I'd like you to analyze the top five universities in Mexico for 2021-2022, according to the Center for World University Rankings. Identify the city in which each of the top five is based, and tell me, using World Population Review's 2022 population figures, the name of the university located in the least-populated city.

# Constraints
- Use the validated claims as prior evidence.
- First determine whether the current claims are sufficient to directly complete the Task Objective.
- If the Task Objective is already solvable from the claims, provide the answer in `## Final Conclusion`.
- If the Task Objective is not yet solvable, do not force a conclusion. Instead, use `## Reasoning & Plan` to explain what missing information is needed, and provide the next best instruction(s) to execute.
- Do not ask for user clarification.
- Keep the reasoning concise but operational.
- In `## Final Conclusion`, every factual statement must be supported by evidence already listed in `## Key Findings & Evidence`.

## Key Findings & Evidence
Use the following prior CLAIMS as established evidence. Preserve their identifiers and statuses.

## Reasoning & Plan
* **Analysis:** 
  - Task Objective: [Restate the task objective briefly.]
  - Sufficiency Check: Determine whether the validated claims already contain enough information to fully answer the Task Objective.
  - Gap Check: If not sufficient, identify exactly what is missing.

* **Plan:** 
  - If sufficient: explain how you will synthesize the existing claims into the final answer.
  - If insufficient: propose the next concrete instruction(s) that should be executed to obtain the missing evidence.
  - Prefer instructions that are atomic, directly verifiable, and dependency-aware.
  - If insufficient: propose the tool call(s) required to execute the instruction(s) when necessary.

### Prior Claims
- C1 | The task requires analyzing the top five universities in Mexico for 2021-2022 according to the Center for World University Rankings.
- C2 | The task requires identifying the city in which each of the top five universities is based.
- C3 | The task requires using World Population Review's 2022 population figures.
- C4 | The task requires determining which university is located in the least-populated city among the top five.
- C5 | A web search tool can be used to find the Center for World University Rankings page for Mexico's top universities 2021-2022.
- C6 | A web search tool can be used to find World Population Review's 2022 city population data.
- C7 | A fetch_web_text tool can extract text content from the CWUR rankings page.
- C8 | A fetch_web_text tool can extract text content from population data pages to identify universities, their cities, and population figures for comparison.
- C9 | National Autonomous University of Mexico ranked 397 in Quality of Education in the 2021-2022 CWUR ranking.
- C10 | Columbia University ranked 7th globally in the CWUR 2021-2022 World University Rankings.
- C11 | Columbia University had a Quality of Education rank of 5 in CWUR 2021-2022.
- C12 | University of Pennsylvania ranked 9th globally in the CWUR 2021-2022 World University Rankings.
- C13 | Rockefeller University ranked 49th globally in the CWUR 2021-2022 World University Rankings.
- C14 | Vanderbilt University ranked 53rd globally in the CWUR 2021-2022 World University Rankings.
- C15 | Purdue University ranked 61st globally in the CWUR 2021-2022 World University Rankings.
- C16 | Purdue University had a Quality of Education rank of 35 in CWUR 2021-2022.
- C17 | University of Florida ranked 86th globally in the CWUR 2021-2022 World University Rankings.
- C18 | University of Florida had a Quality of Education rank of 47 in CWUR 2021-2022.
- C19 | University of Arizona ranked 93rd globally in the CWUR 2021-2022 World University Rankings.
- C20 | University of Iowa ranked 145th globally in the CWUR 2021-2022 World University Rankings.
- C21 | University of Chicago ranked 7th globally in the CWUR 2022-2023 World University Rankings.
- C22 | Cornell University ranked 14th globally in the CWUR 2022-2023 World University Rankings.
- C23 | University of Washington ranked 25th globally in the CWUR 2022-2023 World University Rankings.
- C24 | University rankings in Mexico employ bibliometric, reputational, and webometric methodological frameworks.
- C25 | Bibliometric rankings focus on quantitative measures of research output and impact using databases such as Scopus or Web of Science.
- C26 | The h-index quantifies an institution's research influence by balancing publication quantity and citation quality.
- C27 | Reputational rankings rely on subjective evaluations gathered through surveys of academics, employers, and alumni.
- C28 | Webometric rankings assess an institution's digital footprint and online visibility as proxies for engagement and accessibility.
- C29 | Webometric rankings measure elements like volume of web pages, downloadable files, and external backlinks from search engine data.
- C30 | Common ranking indicators include student-faculty ratios as proxies for teaching quality.
- C31 | Internationalization metrics include the proportion of international students, staff, or collaborative publications.
- C32 | Latin American-focused rankings recalibrate weights to account for emerging economy dynamics such as lower baseline research funding.
- C33 | Center for World University Rankings (CWUR) is a leading consulting organization and publisher of the largest academic ranking of global universities.
- C34 | CWUR publishes the only global university ranking that measures quality of education, training of students, and prestige of faculty without relying on surveys and university data submissions.
- C35 | QS World University Rankings 2022 includes 1,300 institutions.
- C36 | National Autonomous University of Mexico has 35 rankings tracked by University Guru as of 2026.
- C37 | Columbia University is located in the USA.
- C38 | University of Pennsylvania is located in the USA.
- C39 | Rockefeller University is located in the USA.
- C40 | Vanderbilt University is located in the USA.
- C41 | Purdue University is located in the USA.
- C42 | University of Florida is located in the USA.
- C43 | University of Arizona is located in the USA.
- C44 | University of Iowa is located in the USA.
- C45 | Harvard University ranked 1st in the CWUR World University Rankings 2020-21.
- C46 | Harvard University is located in the USA.
- C47 | Duke University ranked 20th in the CWUR World University Rankings 2020-21.
- C48 | Duke University is located in the USA.
- C49 | Duke University had a score of 88.2 in the CWUR 2020-21 ranking.
- C50 | University of Virginia ranked 64th in the CWUR World University Rankings 2020-21.
- C51 | University of Virginia is located in the USA.
- C52 | University of Chicago is located in the USA.
- C53 | Cornell University is located in the USA.
- C54 | University of Washington is located in the USA.
- C55 | Yale University ranked 9th in the CWUR World University Rankings 2025.
- C56 | Yale University is located in the USA.
- C57 | Brown University ranked 71st in the CWUR World University Rankings 2025.
- C58 | Brown University is located in the USA.
- C59 | CINVESTAV ranks 598th in the world according to CWUR 2021-22.
- C60 | CINVESTAV is ranked 2nd nationally in Mexico.
- C61 | CINVESTAV has an overall score of 73.2 in CWUR 2021-22.
- C62 | National Polytechnic Institute ranks 640th in the world according to CWUR 2021-22.
- C63 | National Polytechnic Institute is ranked 3rd nationally in Mexico.
- C64 | National Institute of Public Health (INSP) ranks 1121st in the world according to CWUR 2021-22.
- C65 | National Institute of Public Health (INSP) is ranked 6th nationally in Mexico.
- C66 | Ibero-American University ranks 1156th in the world according to CWUR 2021-22.
- C67 | Ibero-American University is ranked 8th nationally in Mexico.
- C68 | The National Polytechnic Institute was established in Mexico in 1936.
- C69 | The National Polytechnic Institute is considered to be the most prestigious public technological higher education center in Mexico.
- C70 | The National Polytechnic Institute strives to support Mexico's industrialization and development processes.
- C71 | More than 166,700 students are currently enrolled in the National Polytechnic Institute.
- C72 | The National Polytechnic Institute is located at Miguel Bernard 39, Col. Residencial La Escalera, Delegación Gustavo A.
- C73 | The National Polytechnic Institute is one of the largest public universities in Mexico with 171,581 students at the high school, undergraduate and postgraduate levels.
- C74 | The National Polytechnic Institute is organized around 98 academic units.
- C75 | The National Polytechnic Institute includes 18 vocational high schools that operate as CECyT.
- C76 | Most of the National Polytechnic Institute vocational high schools are in Greater Mexico City.
- C77 | The National Polytechnic Institute main campus is named Unidad Profesional Adolfo López Mateos.
- C78 | The National Polytechnic Institute Zacatenco Unit is located in Gustavo A. Madero, CDMX, Mexico.
- C79 | Escuela Superior de Ingeniería Química e Industrias Extractivas is located at the National Polytechnic Institute Zacatenco Unit.
- C80 | Dirección de Administración Escolar (DAE) - IPN is located at the National Polytechnic Institute Zacatenco Unit.
- C81 | Puerta 9 IPN Zacatenco is located at the National Polytechnic Institute Zacatenco Unit.
- C82 | Universidad Iberoamericana (IBERO) is a private, Jesuit university.
- C83 | Universidad Iberoamericana is located in Mexico City.
- C84 | The university's flagship campus is located in the Santa Fe district of Mexico City.
- C85 | Universidad Iberoamericana's motto is 'La verdad'.
- C86 | Universidad Iberoamericana seeks emotional maturity and a sense of ethical responsibility in its students and graduates.
- C87 | The Santa Fe area is Mexico City's most important business district.
- C88 | Universidad Iberoamericana's address is Prolongación Paseo de Reforma 880 Lomas de Santa Fe, C.P. 01219, México City.
- C89 | The Mexico City campus hosts approximately 12,000 students.
- C90 | Cuernavaca's 2026 population is estimated at 1,172,340.
- C91 | Mexico has a population of about 129 million in 2022.
- C92 | Mexico is the 10th most populated country in the world.
- C93 | Cuernavaca has an area of 1,190 square kilometers.
- C94 | In 1950, the population of Cuernavaca was 36,944.
- C95 | Cuernavaca represents a 1.38% annual population change.
- C96 | Cuernavaca population estimates and projections come from the latest revision of the UN World Urbanization Prospects.
- C97 | Cuernavaca estimates represent the Urban agglomeration of Cuernavaca, which typically includes Cuernavaca's population in addition to adjacent suburban areas.
- C98 | Cuernavaca is a city in Mexico.
- C99 | Instituto Nacional de Salud Pública operates under the Secretariat of Health of Mexico.
- C100 | Instituto Nacional de Salud Pública is headquartered in Cuernavaca, Morelos.
- C101 | The National Institute of Public Health of Mexico contact email is comunicacion@insp.mx.
- C102 | The National Institute of Public Health of Mexico phone number is (777)329 3000.
- C103 | The Mexican National Institute of Public Health began as School of Sanitation, founded on March 23rd, 1922.
- C104 | At the beginning of the 1960s, the School of Sanitation changed its name to Mexican School of Public Health.
- C105 | The Center for Population Health Research is part of the National Institute of Public Health.
- C106 | The Center for Population Health Research is located at 655 University Avenue, Santa María Ahuacatitlan, 62100 Cuernavaca, Morelos, Mexico.
- C107 | Instituto Nacional de Salud Publica is an academic institution whose central commitment to Mexican society is to offer research results to relevant public health problems to prevent and control diseases.
- C108 | The population of 3 years and over that speaks at least one indigenous language in Cuernavaca was 3,950 inhabitants.
- C109 | Indigenous language speakers in Cuernavaca correspond to 1.04% of the total population.
- C110 | In 2020, 89,500 people or 30.4% of the population of Cuernavaca held a Bachelor's Degree.
- C111 | Cuernavaca is likely one of the origins of the Mesoamerican civilization along with Chalcatzingo.
- C112 | Buses run from Mexico City's Terminal de Autobuses del Sur to Cuernavaca.
- C113 | Terminal de Autobuses del Sur is located near Taxqueña metro station.
- C114 | Limited bus runs operate from Terminal de Autobuses del Norte bus station to Cuernavaca.
- C115 | Pullman de Morelos operates buses to Casino de la Selva Terminal in Cuernavaca.
- C116 | Teopanzolco archaeological site is located at calle Río Balsas s.n., Colonia Vista Hermosa.
- C117 | Plaza Cuernavaca is an open-air mall on Plan de Ayala Street.
- C118 | El Faisan is a high-end restaurant featuring Yucatecan food in Cuernavaca.
- C119 | El Faisan is located on Emiliano Zapata and on Rio Mayo in Cuernavaca.
- C120 | On weekends, visitors arrive in Cuernavaca from Mexico City and head to night clubs.
- C121 | National Autonomous University of Mexico is located in Mexico City.
- C122 | CINVESTAV's primary campus is situated in Zacatenco, Mexico City.
- C123 | CINVESTAV was founded in 1961.
- C124 | National Polytechnic Institute (IPN) main campus is situated on approximately 530 acres (2.1 km2) in north Mexico City.
- C125 | Ibero-American University's flagship campus is located in the Santa Fe district of Mexico City.
- C126 | Mexico City metropolitan area had a population of approximately 21.2 million people according to World Population Review 2022 data.
- C127 | Mexico City is the most populous metropolitan area in the Western Hemisphere.