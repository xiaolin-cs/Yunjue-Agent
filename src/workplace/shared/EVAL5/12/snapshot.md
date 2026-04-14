You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Among Jakks Pacific, Hasbro, Mattel, and Funko which company had the highest debt-to-capital ratio for the fiscal year ended December 31, 2023? Use the SEC website and filings.

# Current Instruction
**T5** — Compare debt-to-capital ratios for Jakks Pacific, Hasbro, Mattel, and Funko to determine which company had the highest ratio

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
- C1 | Funko, Inc. has CIK number 0001704711.
- C2 | Funko, Inc. has a mailing address of 2802 WETMORE AVE EVERETT WA 98201.
- C3 | Funko, Inc. has a business phone number of 425-783-3616.
- C4 | Funko, Inc. operates under SIC code 3944.
- C5 | SIC code 3944 corresponds to GAMES, TOYS & CHILDREN'S VEHICLES (NO DOLLS & BICYCLES).
- C6 | Funko, Inc. is located in Washington state.
- C7 | Funko, Inc. has a fiscal year end date of December 31.
- C8 | Funko, Inc. is classified under CF Office 04 Manufacturing.
- C9 | Funko, Inc. filed a 10-K annual report on 2026-03-12 with accession number 0001704711-26-000020.
- C10 | Jakks Pacific has CIK number 0001009829.
- C11 | Jakks Pacific filed a 10-K annual report for fiscal year 2023 on 2024-03-15.
- C12 | Hasbro has CIK number 0000046080.
- C13 | Hasbro filed a 10-K annual report for fiscal year 2023 on 2024-02-28.
- C14 | Hasbro's 10-K for fiscal year 2023 has accession number 0000046080-24-000034.
- C15 | Mattel has CIK number 0000063276.
- C16 | Mattel filed a 10-K annual report for fiscal year 2023 on 2024-03-15.
- C17 | Mattel's 10-K for fiscal year 2023 has accession number 0001628280-24-011371.
- C18 | Mattel's 10-K for fiscal year 2023 is located at URL https://www.sec.gov/Archives/edgar/data/63276/000162828024011371/0001628280-24-011371-index.htm.
- C19 | Funko's 10-K for fiscal year 2023 has accession number 0001704711-24-000013.
- C20 | JAKKS PACIFIC INC filed a Form 10-K Annual report with SEC Accession No. 0001185185-24-000243.
- C21 | The Form 10-K filing date for JAKKS PACIFIC INC was 2024-03-15.
- C22 | The period of report for JAKKS PACIFIC INC Form 10-K is 2023-12-31.
- C23 | The main Form 10-K document is named jakkspacif20231231_10k.htm and has size 2823918 bytes.
- C24 | JAKKS PACIFIC INC filed EXHIBIT 3.4 with filename ex_639085.htm and size 53029 bytes.
- C25 | The complete submission text file is named 0001185185-24-000243.txt and has size 11376283 bytes.
- C26 | JAKKS PACIFIC INC filed XBRL TAXONOMY EXTENSION SCHEMA with filename jakk-20231231.xsd and size 73562 bytes.
- C27 | JAKKS PACIFIC INC mailing address is 2951 28TH STREET SANTA MONICA CA 90405.
- C28 | JAKKS PACIFIC INC business phone number is 424-268-9444.
- C29 | JAKKS PACIFIC INC has EIN 954527222.
- C30 | JAKKS PACIFIC INC state of incorporation is Delaware.
- C31 | JAKKS PACIFIC INC fiscal year end is 1231.
- C32 | JAKKS PACIFIC INC film number is 24753087.
- C33 | JAKKS PACIFIC INC SIC code is 3944.
- C34 | JAKKS PACIFIC INC operates in CF Office 04 Manufacturing.
- C35 | The filing date for SEC Accession No. 0001704711-24-000013 was 2024-03-07.
- C36 | Funko, Inc. has EIN 000000000.
- C37 | Funko, Inc. has film number 24730652.
- C38 | SIC code 3944 belongs to CF Office 04 Manufacturing.
- C39 | The primary 10-K document is fnko-20231231.htm with size 2157734 bytes.
- C40 | The filing includes exhibit EX-4.2 named exhibit42.htm with size 38279 bytes.
- C41 | The filing includes graphic file fnko-20231231_g1.jpg with size 12337 bytes.
- C42 | The filing includes XBRL taxonomy extension schema document fnko-20231231.xsd with size 77047 bytes.
- C43 | The Form 10-K filing type falls under Act 34.
- C44 | The primary 10-K document uses iXBRL format.
- C45 | Funko's total debt as of December 31, 2023 was $153.1 million.
- C46 | Funko's Term Loan Facility balance as of December 31, 2023 was $139.5 million.
- C47 | The analysis requires SEC filings for Jakks Pacific for fiscal year ended December 31, 2023 to complete the comparison.
- C48 | The analysis requires SEC filings for Hasbro for fiscal year ended December 31, 2023 to complete the comparison.
- C49 | The provided information contains only Funko's detailed financial data for fiscal year ended December 31, 2023.