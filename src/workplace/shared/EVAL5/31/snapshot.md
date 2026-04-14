You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
According to the Our World in Data migration chart and the IMF’s World Economic Outlook 2023 GDP per capita data, which countries had an absolute change in the total number of emigrants between 3 million and 4 million from 1990 to 2024, a relative change in emigrants above 100% from 1990 to 2024, and a GDP per capita above $2,000 in 2023?

# Current Instruction
**T5** — List sheets in the IMF World Economic Outlook 2023 Excel file to identify the GDP per capita data location

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
- C1 | The International Monetary Fund (IMF) published the World Economic Outlook titled 'Global Economy in Flux, Prospects Remain Dim' in October 2025.
- C2 | Monaco has a GDP per capita of $256,581 according to World Bank data from 2023.
- C3 | The United States has a GDP per capita of $89,599.
- C4 | The United States ranks 11th in GDP per capita globally.
- C5 | Greenland has a GDP per capita of $58,499 according to World Bank data from 2023.
- C6 | U.S. Virgin Islands has a GDP per capita of $44,321 according to World Bank data from 2022.
- C7 | Puerto Rico has a GDP per capita of $39,854.
- C8 | Turks and Caicos has a GDP per capita of $37,507 according to World Bank data from 2024.
- C9 | Anguilla has a GDP per capita of $28,850 according to United Nations data from 2023.
- C10 | Antigua and Barbuda has a GDP per capita of $22,314.
- C11 | Curaçao has a GDP per capita of $21,062 according to World Bank data from 2023.
- C12 | Curaçao ranks 77th in GDP per capita globally.
- C13 | Costa Rica has a GDP per capita of $19,104.
- C14 | Cuba has a GDP per capita of $18,329 according to United Nations data from 2023.
- C15 | Cuba ranks 84th in GDP per capita globally.
- C16 | Montserrat has a GDP per capita of $18,197 according to United Nations data from 2023.
- C17 | Montserrat ranks 86th in GDP per capita globally.
- C18 | Trinidad and Tobago has a GDP per capita of $18,121.
- C19 | St. Vincent and the Grenadines has a GDP per capita of $11,132.
- C20 | Bosnia and Herzegovina has a GDP per capita of $9,648.
- C21 | Timor-Leste has a GDP per capita of $1,508.
- C22 | Eritrea has a GDP per capita of $656 according to United Nations data from 2023.
- C23 | The World Bank publishes GDP per capita data measured in PPP (current international dollars).
- C24 | The Bahamas has a GDP per capita of 40.41 thousand U.S. dollars according to IMF data.
- C25 | Côte d'Ivoire has a GDP per capita of 3.29 thousand U.S. dollars according to IMF data.
- C26 | Hong Kong SAR has a GDP per capita of 59 thousand U.S. dollars according to IMF data.
- C27 | Macao SAR has a GDP per capita of 77.44 thousand U.S. dollars according to IMF data.
- C28 | Marshall Islands has a GDP per capita of 9.39 thousand U.S. dollars according to IMF data.
- C29 | North Macedonia has a GDP per capita of 11.53 thousand U.S. dollars according to IMF data.
- C30 | Papua New Guinea has a GDP per capita of 2.56 thousand U.S. dollars according to IMF data.
- C31 | São Tomé and Príncipe has a GDP per capita of 4.59 thousand U.S. dollars according to IMF data.
- C32 | South Africa has a GDP per capita of 6.83 thousand U.S. dollars according to IMF data.
- C33 | Asia and Pacific region has a GDP per capita of 9.59 thousand U.S. dollars according to IMF data.
- C34 | The IMF DataMapper publishes economic indicators from 13 datasets.
- C35 | Our World in Data publishes GDP per capita data for 2024.
- C36 | The IMF World Economic Outlook database is available on the IMF's website at www.imf.org.
- C37 | The World Economic Outlook database includes data on Real GDP growth.
- C38 | The United Nations Department of Economic and Social Affairs published the International Migrant Stock 2024 dataset (POP/DB/MIG/Stock/Rev.2024).
- C39 | In the new edition of the International Migrant Stock data, a total of 60 countries and areas received a full reassessment of trends in the number of international migrants residing in the territory.
- C40 | Our World in Data processes data from the United Nations Department of Economic and Social Affairs for migration statistics.
- C41 | The United Nations Population Division defines an international migrant as someone who has been living for one year or longer in a country other than the one in which he or she was born.
- C42 | Data on asylum seekers is sourced from the United Nations High Commissioner for Refugees (UNHCR).
- C43 | Data on internal displacement is sourced from the Internal Displacement Monitoring Centre (IDMC).
- C44 | Migration has been an important source of economic development and poverty reduction.
- C45 | Remittances, the transfer of money from migrants working overseas to family or friends in their home country, can be an important source of income in many countries.
- C46 | Our World in Data is a project of Global Change Data Lab, a nonprofit based in the UK (Reg. Charity No. 1186433).
- C47 | Our World in Data charts, articles, and data are licensed under CC BY, unless stated otherwise.
- C48 | Migration Policy Institute provides a map showing the immigrant and emigrant populations by country of origin and destination.
- C49 | The IMF World Economic Outlook Database (October 2023) contains data on national accounts, inflation, unemployment rates, balance of payments, fiscal indicators, and trade for countries and country groups.
- C50 | The World Economic Outlook (WEO) database is published twice a year in April and October in conjunction with the biannual flagship World Economic Outlook report.
- C51 | The October 2025 WEO Database Appendix is a vintage-specific appendix to the World Economic Outlook (WEO) database, compiled as a downloadable PDF.
- C52 | The WEO Historical Forecasts Database is a comprehensive archive of the IMF's World Economic Outlook historical forecasts, providing past projections for key macroeconomic indicators across countries and regions.
- C53 | According to the October 2025 WEO, GDP per capita in current prices for emerging market and developing economies is 7.36 thousand U.S. dollars per capita.
- C54 | The WEO is prepared by the IMF staff.
- C55 | Afghanistan has no data available for GDP per capita in current prices in the IMF WEO database.
- C56 | The IMF provides Frequently Asked Questions for the World Economic Outlook (WEO) data, organized by topic to explain database publication, data coverage, specific series definitions, country group classifications, forecast methodology, and common usage issues.
- C57 | UNHCR publishes a Refugee Population Statistics Database with annual statistics for 2024.
- C58 | Our World in Data has 13,899 charts across 126 topics.
- C59 | Mental health care is scarce everywhere but in poor countries it barely exists.
- C60 | Depression, anxiety, and other mental health problems are common everywhere.
- C61 | Madagascar has an informal employment share of approximately 96% in 2023.
- C62 | Angola has an informal employment share of approximately 71% to 96% in 2023.
- C63 | Norway has an informal employment share of approximately 1.2% in 2023.
- C64 | Poland has an informal employment share of approximately 7.7% in 2023.
- C65 | Three-quarters of the world's countries had unemployment rates below 10% last year according to International Labour Organization data.
- C66 | Outside rich countries, widespread informal work means unemployment rates are low.
- C67 | The share of immigrants in high-income countries doubled between 1990 and 2020.
- C68 | The global suicide rate peaked near 15 per 100,000 people in 1995.
- C69 | Child mortality in China spiked to about 1 in 3 children during the Great Leap Forward from 1958 to 1962.
- C70 | High-income countries spend about $66 per person per year on mental health care.
- C71 | The Varieties of Democracy (V-Dem) project publishes data and research on democracy and human rights.
- C72 | The V-Dem snapshot contains all 531 V-Dem indicators and 251 indices plus 62 other indicators from other data sources.
- C73 | V-Dem only provides regime data since Bangladesh's independence in 1971.
- C74 | Today, one in seven people in high-income countries are immigrants.
- C75 | Pew Research Center is a nonpartisan, nonadvocacy fact tank that informs the public about the issues, attitudes and trends shaping the world.
- C76 | Pew Research Center is a subsidiary of The Pew Charitable Trusts, its primary funder.
- C77 | Madagascar, Angola, India, Bolivia, Peru, and Egypt have very high informal employment shares ranging from about 96% to 71%.