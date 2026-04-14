You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Find the votes that passed in the US House of Representatives between December 1st 2023 and December 10th 2023 (inclusive), with over a 90% "yea" vote (not including "present" or "not voting" votes). Out of these votes, find the ones where there were no “present” votes. Finally, in which of these votes were the “nay” votes mostly made up of Republican representatives (include votes where the “nay” votes were made up of exactly 50% Republican representatives). Include all votes made in the House of Representatives, including those regarding amendments, bills, resolutions, motions and ordering the previous question.

# Current Instruction
**T5** — Filter the votes with over 90% yea votes to include only votes where there were zero present votes

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
- C1 | The task requires finding votes that passed in the US House of Representatives between December 1st 2023 and December 10th 2023 (inclusive).
- C2 | The votes must have over 90% 'yea' votes, not including 'present' or 'not voting' votes in the calculation.
- C3 | The final filtering criterion is that 'nay' votes were mostly made up of Republican representatives.
- C4 | The task includes all votes made in the House of Representatives, including those regarding amendments, bills, resolutions, motions and ordering the previous question.
- C5 | The fetch_vote_data tool can retrieve US House voting records for the specified date range (December 1-10, 2023).
- C6 | The parse_vote_details tool can extract vote counts including yea, nay, present, and not voting from each vote record.
- C7 | The parse_vote_details tool can extract party breakdowns from each vote record.
- C8 | The filter_data tool can apply multi-stage filtering for greater than 90% yea votes, zero present votes, and majority Republican nay votes.
- C9 | The calculate_value tool can compute percentages for yea votes to enable filtering criteria.
- C10 | A subprocess execution error occurred when attempting to fetch vote data.
- C11 | The PROPUBLICA_API_KEY environment variable is not available in the execution environment.
- C12 | The fetch_from_propublica function raised an exception due to missing PROPUBLICA_API_KEY.
- C13 | The system attempted a fallback to fetch_from_clerk_website after the ProPublica API failure.
- C14 | The fetch_house_votes function found no votes for the specified date range in House records.
- C15 | The fallback fetch_from_clerk_website method also failed with an exception stating no votes were found.
- C16 | The final exception message indicates both the primary error (PROPUBLICA_API_KEY not available) and the fallback error (no votes found for the specified date range in House records).
- C17 | The error originated from the file fetch_vote_data.py in the dynamic_tools_25 directory.
- C18 | The vote data fetch operation involves checking both the chamber parameter and a date range (start_dt and end_dt).
- C19 | The system has at least two data sources for vote information: ProPublica API and the Clerk website.
- C20 | The current instruction is to extract vote counts including yea, nay, present, and not voting from each voting record between December 1st 2023 and December 10th 2023.
- C21 | The validated claims C1-C9 establish task requirements and available tools.
- C22 | Claims C10-C19 document a failed attempt to fetch vote data due to missing API key and no votes found in fallback sources.
- C23 | No actual voting records have been successfully retrieved.
- C24 | Without successful vote data retrieval, the system cannot extract vote counts or proceed with any analysis.
- C25 | The fetch_vote_data tool has failed through both its primary ProPublica API method and fallback Clerk website method.
- C26 | According to C14-C16, the Clerk website fallback reported no votes found for the specified date range in House records.
- C27 | There are two possible explanations for the fallback failure: either there genuinely were no House votes during December 1-10, 2023, or the data source is inaccessible or unavailable.
- C28 | There are no alternative tools available to fetch voting data beyond the failed fetch_vote_data tool.
- C29 | The current instruction cannot be completed due to failed data retrieval.
- C30 | The fetch_vote_data tool failed with error message PROPUBLICA_API_KEY not available.
- C31 | The Clerk website fallback method failed with message no votes found for the specified date range in House records.
- C32 | The task requires calculating the percentage of yea votes to filter for greater than 90%.
- C33 | The task requires identifying votes with zero present votes.
- C34 | The task requires determining party composition of nay votes to find Republican-majority opposition.
- C35 | The fetch_vote_data tool returned an empty array with zero voting records.
- C36 | The empty result indicates the tool is functioning correctly but found no votes in the specified date range.
- C37 | The task requires votes from the US House between December 1-10, 2023.
- C38 | Zero voting records exist for the US House of Representatives between December 1-10, 2023.
- C39 | The answer to the task is zero votes satisfy the criteria.