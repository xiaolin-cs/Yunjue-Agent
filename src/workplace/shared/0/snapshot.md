You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Consider the OECD countries whose total population was composed of at least 20% of foreign-born populations as of 2023 (according to the Observatory of Migration at the university of Oxford). Amongst them, which country saw their overall criminality score increase by at least +0.2 point between 2021 and 2023 and their resilience score decrease by more than 0.3 between these same dates (according to the Organised Crime Index)?

# Current Instruction
**T5** — Identify the country or countries that satisfy both conditions: criminality score increase of at least +0.2 points and resilience score decrease of more than 0.3 points between 2021 and 2023.

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

### Prior Claims
- C1 | The task requires identifying OECD countries with at least 20% foreign-born population as of 2023 according to the Observatory of Migration at the University of Oxford.
- C2 | The task requires filtering countries by criminality score increase of at least +0.2 points between 2021 and 2023 according to the Organised Crime Index.
- C3 | The task requires filtering countries by resilience score decrease of more than 0.3 points between 2021 and 2023 according to the Organised Crime Index.
- C4 | The Observatory of Migration at the University of Oxford is the data source for foreign-born population percentages in OECD countries.
- C5 | The Organised Crime Index is the data source for criminality and resilience scores.
- C6 | The analysis requires data from two specific time points: 2021 and 2023.
- C7 | The tool guidance suggests extracting data from Organised Crime Index visualizations showing criminality and resilience score changes between 2021-2023.
- C8 | The task involves intersection of three criteria: foreign-born population threshold, criminality score change, and resilience score change.
- C9 | The foreign-born population threshold is measured as a percentage of total population.
- C10 | The criminality score change threshold is a minimum increase of 0.2 points.
- C11 | The resilience score change threshold is a decrease exceeding 0.3 points.
- C12 | Luxembourg has a foreign-born population of 50% of its total population.
- C13 | Switzerland has a foreign-born population of 31% of its total population.
- C14 | Canada has a foreign-born population of 22% of its total population.
- C15 | Sweden has a foreign-born population of 20% of its total population.
- C16 | Germany has a foreign-born population of 17% of its total population.
- C17 | Spain has a foreign-born population of 16% of its total population.
- C18 | The United Kingdom has a foreign-born population of 14% of its total population.
- C19 | France has a foreign-born population of 13% of its total population.
- C20 | Italy has a foreign-born population of 10% of its total population.
- C21 | Japan has a foreign-born population of 2% of its total population.
- C22 | Mexico has a foreign-born population of 1% of its total population.
- C23 | Data on foreign-born population percentages in OECD countries comes from the OECD's International Migration Database accessed via The Migration Observatory at the University of Oxford.
- C24 | The OECD is an international organization of 38 countries that promotes policies to improve global economic and social well-being.
- C25 | Mexico, Japan, and Poland are highly ethnically homogenous.
- C26 | At the time of the 2021/22 Census, 16% of people in the United Kingdom had been born abroad.
- C27 | Permanent-type migration to OECD countries reached a record level in 2022 with more than 6 million new permanent immigrants not including Ukrainian refugees.
- C28 | Hawaii and South Dakota both had unemployment rates of 2.2%, the lowest unemployment rates in the United States.
- C29 | Hawaii saw a 0.8% year-over-year drop in unemployment rate.
- C30 | Foreign population consists of people who still have the nationality of their home country.
- C31 | In many Western OECD countries, foreign-origin populations including first- and second-generation immigrants are projected to become the majority in the second half of the 21st century.
- C32 | Countries such as the United States, United Kingdom, Germany, and Sweden could see over 50% of their populations being of foreign origin by 2050-2080 if current demographic trends continue.
- C33 | Foreign-born individuals alone remain a minority ranging from 10% to 20% in most OECD countries.
- C34 | Urban areas like London, Brussels, and parts of the United States are already majority-minority.
- C35 | The Global Organized Crime Index 2023 was released by the Global Initiative Against Transnational Organized Crime.
- C36 | 83% of the world's population lives in conditions of high criminality according to the Global Organized Crime Index 2023.
- C37 | Europe shows the greatest continental increase in criminality between 2021 and 2023.
- C38 | Europe's resilience to organized crime has grown only marginally between 2021 and 2023.
- C39 | Africa saw the smallest continental increase in criminality between 2021 and 2023.
- C40 | All criminal actor types strengthened their presence on the African continent in a post-COVID environment.
- C41 | All ten original criminal markets in Africa saw increased scores between 2021 and 2023.
- C42 | The Index interactive website allows users to sort and compare scores for criminal markets.
- C43 | The Index interactive website includes a criminality heatmap detailing a country's criminality score on a scale of 1 to 10.
- C44 | Human trafficking score in Europe increased by 0.18 between 2021 and 2023.
- C45 | Extortion and protection racketeering score in Europe increased by 0.38 between 2021 and 2023.
- C46 | Arms trafficking score in Europe increased by 0.27 between 2021 and 2023.
- C47 | Counterfeit goods score in Europe increased by 0.20 between 2021 and 2023.
- C48 | Illicit trade of excise consumer goods score in Europe decreased by 0.01 between 2021 and 2023.
- C49 | Flora crimes score in Europe increased by 0.23 between 2021 and 2023.
- C50 | Fauna crimes score in Europe increased by 0.38 between 2021 and 2023.
- C51 | Non-renewable resource crimes score in Europe increased by 0.33 between 2021 and 2023.
- C52 | Heroin trade score in Europe increased by 0.40 between 2021 and 2023.
- C53 | Cannabis trade score in Europe increased by 0.11 between 2021 and 2023.
- C54 | Synthetic drug trade score in Europe increased by 0.20 between 2021 and 2023.
- C55 | Financial crimes score in Europe increased by 0.07 between 2021 and 2023.
- C56 | Mafia-style groups score in Europe increased by 0.03 between 2021 and 2023.
- C57 | Criminal networks score in Europe increased by 0.22 between 2021 and 2023.
- C58 | State-embedded actors score in Europe increased by 0.15 between 2021 and 2023.
- C59 | Foreign actors score in Europe increased by 0.02 between 2021 and 2023.
- C60 | Private sector actors score in Europe increased by 0.06 between 2021 and 2023.
- C61 | Government transparency and accountability score in Europe decreased by 0.09 between 2021 and 2023.
- C62 | International cooperation score in Europe increased by 0.05 between 2021 and 2023.
- C63 | National policies and laws score in Europe decreased by 0.03 between 2021 and 2023.
- C64 | Judicial system and detention score in Europe decreased by 0.01 between 2021 and 2023.
- C65 | Law enforcement score in Europe increased by 0.14 between 2021 and 2023.
- C66 | Territorial integrity score in Europe decreased by 0.08 between 2021 and 2023.
- C67 | Anti-money laundering score in Europe increased by 0.09 between 2021 and 2023.
- C68 | Venezuela has a crime index of 80.7 according to Numbeo 2025.
- C69 | Haiti has a crime index of 78.9 according to Numbeo 2025.
- C70 | Afghanistan has a crime index of 75.1 according to Numbeo 2025.
- C71 | Honduras has a crime index of 72.0 according to Numbeo 2025.
- C72 | Peru has a crime index of 67.1 according to Numbeo 2025.
- C73 | Jamaica has a Numbeo Crime Index of 67.4 in the 2025 dataset.
- C74 | South Africa has a crime index of 74.5 according to Numbeo 2026.
- C75 | Dominican Republic has a crime index of 60.0 according to Numbeo 2026.
- C76 | United States has a crime index of 49.2 according to Numbeo 2026.
- C77 | South Korea has a crime index of 29.0 according to Numbeo 2026.
- C78 | Czech Republic has a crime index of 26.4 according to Numbeo 2026.
- C79 | China has a crime index of 23.1 according to Numbeo 2026.
- C80 | Widespread unemployment adds fuel for many crimes in Venezuela, such as robbery and assault.
- C81 | The criminal markets score is represented by the pyramid base size on a scale ranging from 1 to 10.
- C82 | The resilience score is represented by the panel height in the Global Organized Crime Index visualization.
- C83 | The heatmap is composed of two main components: criminality and resilience to organized crime.
- C84 | Myanmar has the highest criminality score of 8.08 in the 2025 Global Organized Crime Index.
- C85 | Colombia ranks second in criminality with a score of 7.82 in the 2025 Global Organized Crime Index.
- C86 | Paraguay ranks fifth in criminality with a score of 7.48 in the 2025 Global Organized Crime Index.
- C87 | Congo, Dem. Rep. ranks sixth in criminality with a score of 7.47 in the 2025 Global Organized Crime Index.
- C88 | South Africa ranks seventh in criminality with a score of 7.43 in the 2025 Global Organized Crime Index.
- C89 | Nigeria ranks eighth in criminality with a score of 7.32 in the 2025 Global Organized Crime Index.
- C90 | Lebanon ranks ninth in criminality with a score of 7.30 in the 2025 Global Organized Crime Index.
- C91 | Türkiye ranks tenth in criminality with a score of 7.20 in the 2025 Global Organized Crime Index.
- C92 | Tuvalu has the lowest criminality score of 1.53 in the 2025 Global Organized Crime Index.
- C93 | Myanmar's criminality score decreased by 0.07 from the previous index period.
- C94 | Myanmar has a resilience score of 1.46 in the 2025 Global Organized Crime Index.
- C95 | The Global Organized Crime Index is funded in part by a grant from the United States Department of State.
- C96 | ENACT is funded by the European Union and implemented by the Institute for Security Studies and INTERPOL, in affiliation with the Global Initiative Against Transnational Organized Crime.
- C97 | The Index Podcast is a deep dive into the Global Organized Crime Index.
- C98 | Sweden's capital is Stockholm.
- C99 | Sweden's population is 10,569,709.
- C100 | Sweden's gross domestic product (GDP) is USD 610,118 million.
- C101 | Sweden's area is 528,861 square kilometers.
- C102 | Sweden's Organized Crime Index criminality score in 2025 is 4.73.
- C103 | Sweden is predominantly a destination country for human trafficking, with victims subjected to sexual and labour exploitation.
- C104 | Most human trafficking victims in Sweden come from West Africa, Eastern Europe and Asia.
- C105 | Labour trafficking in Sweden targets workers in sectors such as forestry, construction and automotive repair.
- C106 | Sweden acts as both a destination and transit point for human smuggling.
- C107 | People from Afghanistan, Egypt, Morocco, West Africa and Eastern Europe make up a substantial share of the smuggled population in Sweden.
- C108 | Extortion and protection racketeering have grown significantly in Sweden, making Sweden one of the most affected countries in Northern Europe.
- C109 | Illicit firearms in Sweden include automatic and semi-automatic weapons, grenades and explosives, many of which originate from the Balkans and Eastern Europe.
- C110 | The counterfeit goods market in Sweden primarily involves fashion items, electronics and luxury goods, sourced from East Asia and Europe.
- C111 | High excise taxes in Sweden have contributed to a thriving market for illicit alcohol and tobacco.
- C112 | Swedish customs reported a sharp increase in cigarette interceptions in 2023 compared to the previous year.
- C113 | The overall illegal cigarette market in Sweden is perceived to be in decline.
- C114 | Flora crimes in Sweden are primarily linked to illegal logging and the unregistered timber trade.
- C115 | Fauna crime in Sweden has seen an expansion in recent years, driven by illegal poaching and trophy hunting.
- C116 | Wolves, bears and lynx are frequent targets of poaching in Sweden.
- C117 | The discovery of rare earth elements, as well as graphite and iron deposits in Sweden, has sparked concerns about illegal mining and resource exploitation.
- C118 | Sweden remains a destination market for heroin, with supply chains linked to Afghanistan via the Balkans.
- C119 | The cocaine market in Sweden is expanding, driven by organized crime groups and transnational cartels.
- C120 | Stockholm serves as the key hub for cocaine distribution in Sweden.
- C121 | Over the last decade, Sweden has seen a sharp rise in gang violence, with killings and bombings becoming more frequent.
- C122 | The surge in gang activity in Sweden is closely linked to the cocaine trade, fuelling inter-gang rivalries.
- C123 | The illegal cannabis market in Sweden is commonplace, with Sweden acting as both a source and destination.
- C124 | Synthetic drugs in Sweden, including methamphetamine, amphetamines and 3-CMC, are widely available.
- C125 | A significant share of synthetic drugs in Sweden is manufactured in Swedish laboratories.
- C126 | Authorities in Sweden have reported an increase in overdoses involving synthetic opioids.
- C127 | Sweden has experienced a sharp rise in cybercrime, including ransomware attacks and data breaches.
- C128 | Sweden has been targeted by foreign hacker groups, including Russian actors, in several cyber-attacks.
- C129 | Since joining NATO in March 2024, Sweden has faced numerous influence operations and cyber disruptions.
- C130 | Financial crime continues to increase in Sweden, with fraud the most common offence.
- C131 | Criminal networks in Sweden have exploited welfare systems, particularly by establishing private clinics to embezzle public health funds.
- C132 | Reports from 2024 identify fraud as the fastest-growing crime type in Sweden, marked by a surge in social engineering scams and card fraud.
- C133 | Mafia-style actors in Sweden are largely limited to outlaw motorcycle gangs, which play a prominent role in drug trafficking and other illicit markets.
- C134 | Members of outlaw motorcycle gangs in Sweden established private healthcare clinics as fronts to divert public funds.
- C135 | Illicit profits from healthcare fraud operations by biker gangs in Sweden are estimated to be twice the value of the drug trade.
- C136 | Swedish criminal networks are primarily composed of loosely organized street gangs, involved in drug trafficking, arms smuggling, human smuggling and extortion.
- C137 | Gangs in Sweden reportedly recruit over a thousand people annually, targeting minors and vulnerable youth.
- C138 | In November 2024, Swedish authorities reported a rise in gang violence, driven in part by the use of social media to recruit children as young as 11 for contract killings and drug distribution.
- C139 | State-embedded actors play a limited role in Sweden's organized crime landscape.
- C140 | Foreign actors are a significant presence in Sweden's organized crime landscape, particularly in drug trafficking and firearms smuggling.
- C141 | Most foreign criminal groups in Sweden originate from Western Asia or the Balkans.
- C142 | Ethnic Albanian organizations play a central role in controlling smuggling routes through Swedish ports, facilitating drug trafficking from Latin America into Europe.
- C143 | Foreign criminal networks in Sweden are concentrated in urban centres such as Stockholm, Malmö and Gothenburg, but also operate in smaller cities such as Sundsvall, Uppsala and Helsingborg.
- C144 | Private-sector involvement in organized crime in Sweden remains limited, though concerns persist regarding biker gangs using private companies to commit welfare fraud and exploit Sweden's tax system.
- C145 | Sweden maintains a strong governance framework, consistently demonstrating respect for the rule of law and other fundamental principles.
- C146 | In July 2024, the Swedish government introduced stricter penalties for gun crimes and established security zones to address rising violence.
- C147 | Sweden is highly engaged in international cooperation to combat organized crime, participating actively in Europol and INTERPOL, and maintaining established extradition agreements and intelligence-sharing mechanisms.
- C148 | In November 2024, Sweden moved to join the Macolin Convention, aimed at combating match-fixing and corruption in sport.
- C149 | In February 2024, Sweden introduced its first national strategy explicitly targeting organized crime.
- C150 | Sweden's judicial system remains robust, but concerns have emerged regarding judicial independence and prison capacity.
- C151 | In response to escalating gang violence, the Swedish government has intensified law enforcement efforts in recent years, including the deployment of military personnel to support police operations.
- C152 | A 2024 investigation identified security risks involving at least 30 Swedish police officers, resulting in dismissals.
- C153 | In response to rising insecurity from gang violence and terrorism concerns, Sweden has reintroduced border controls and tightened security at key entry points.
- C154 | Sweden maintains a highly developed anti-money laundering framework, with strict financial reporting requirements and stepped-up enforcement measures introduced in 2024.
- C155 | In October 2024, the Swedish government proposed new measures allowing anonymous testimonies in gang-related trials.
- C156 | Sweden enforces strict drug laws, which have contributed to high drug-related mortality rates.
- C157 | The 2024 National Strategy against Organized Crime in Sweden includes provisions to enhance civil society involvement.