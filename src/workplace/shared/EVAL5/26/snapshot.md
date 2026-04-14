You are given a task context consisting of an overall objective and previously validated claims.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
In the 2019 UK parliamentary election, in Sheffield and Bristol, which candidates received a vote share of above 50% in constituencies that had a turnout of at least 60%?

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
- C1 | Thangam Debbonaire (Labour) won Bristol West in the 2019 general election with 47,213 votes (65.9% vote share).
- C2 | Annabel Tall (Conservative) received 9,877 votes (13.8% vote share) in Bristol West in the 2019 general election.
- C3 | Molly Scott Cato (Green Party) received 9,216 votes (12.9% vote share) in Bristol West in the 2019 general election.
- C4 | Stephen Williams (Liberal Democrat) received 5,201 votes (7.3% vote share) in Bristol West in the 2019 general election.
- C5 | Jodian Rodgers (Money Free Party) received 101 votes (0.1% vote share) in Bristol West in the 2019 general election.
- C6 | Labour's vote share in Bristol West increased by 30.3 percentage points compared to the 2017 general election.
- C7 | Green Party vote share in Bristol West decreased by 14.0 percentage points compared to the 2017 general election.
- C8 | Karin Smyth (Labour) held Bristol South in the 2019 general election.
- C9 | Kerry McCarthy (Labour) was re-elected as MP for Bristol East in the 2019 general election.
- C10 | Darren Jones (Labour) was re-elected as MP for Bristol North West in the 2019 general election.
- C11 | Darren Jones increased his majority in Bristol North West by nearly 1,000 votes in the 2019 general election.
- C12 | Boris Johnson was the leader of the Conservative Party in the 2019 United Kingdom general election.
- C13 | Jeremy Corbyn was the leader of the Labour Party in the 2019 United Kingdom general election.
- C14 | The Conservative Party won 365 seats in the 2019 United Kingdom general election.
- C15 | The Labour Party won 202 seats in the 2019 United Kingdom general election.
- C16 | The Labour Party received 10,269,051 votes (32.1% vote share) in the 2019 United Kingdom general election.
- C17 | The SNP won 48 seats in the 2019 United Kingdom general election.
- C18 | The Liberal Democrats won 11 seats in the 2019 United Kingdom general election.
- C19 | The SNP received 1,242,380 votes (3.9% vote share) in the 2019 United Kingdom general election.
- C20 | The Liberal Democrats received 3,696,419 votes (11.6% vote share) in the 2019 United Kingdom general election.
- C21 | Nicola Sturgeon was the leader of the SNP in the 2019 United Kingdom general election.
- C22 | Jo Swinson was the leader of the Liberal Democrats in the 2019 United Kingdom general election.
- C23 | Jo Swinson lost her seat in East Dunbartonshire in the 2019 United Kingdom general election.
- C24 | The 2019 United Kingdom general election was held on 12 December 2019.
- C25 | The Liberal Democrats saw an increase of 4.2 percentage points in their overall vote share compared to the 2017 general election.
- C26 | Over five million votes went to parties other than Labour and the Conservatives in England in the 2019 general election (nearly 18.9% of the vote).
- C27 | Sheffield Hallam is a UK parliamentary constituency.
- C28 | In the 2019 general election, Labour held Sheffield Hallam.
- C29 | Olivia Blake (Labour) won Sheffield Hallam in 2019 with 19,709 votes.
- C30 | Labour's vote share in Sheffield Hallam decreased by 3.7% compared to 2017.
- C31 | Laura Gordon (Liberal Democrat) came second in Sheffield Hallam in 2019 with 18,997 votes.
- C32 | Ian Walker (Conservative) came third in Sheffield Hallam in 2019 with 14,696 votes.
- C33 | Natalie Thomas (Green) received 1,630 votes in Sheffield Hallam in 2019.
- C34 | Green Party received 2.9% vote share in Sheffield Hallam in 2019.
- C35 | Terence McHale (Brexit Party) received 1,562 votes in Sheffield Hallam in 2019.
- C36 | The Brexit Party received 2.7% vote share in Sheffield Hallam in 2019.
- C37 | Michael Virgo (UKIP) received 168 votes in Sheffield Hallam in 2019.
- C38 | UKIP received 0.3% vote share in Sheffield Hallam in 2019.
- C39 | Elizabeth Aspden (Independent) received 123 votes in Sheffield Hallam in 2019.
- C40 | Sheffield Hallam had 72,763 registered voters in 2019.
- C41 | Turnout in Sheffield Hallam in 2019 was 78.2%.
- C42 | Jared O'Mara (Labour) won Sheffield Hallam in 2017 with 21,881 votes.
- C43 | Nick Clegg (Liberal Democrat) came second in Sheffield Hallam in 2017 with 19,756 votes.
- C44 | John Thurley (UKIP) received 929 votes in Sheffield Hallam in 2017.
- C45 | Logan Robin (Green Party) received 823 votes in Sheffield Hallam in 2017.
- C46 | Steven Winstone (Social Democratic Party) received 70 votes in Sheffield Hallam in 2017.
- C47 | Social Democratic Party received 0.1% vote share in Sheffield Hallam in 2017.
- C48 | Peter Garbutt (Green Party) received 1,772 votes in Sheffield Hallam in 2015.
- C49 | Carlton Reeve (Independent) received 249 votes in Sheffield Hallam in 2015.
- C50 | Steve Clegg (English Democrats) received 167 votes in Sheffield Hallam in 2015.
- C51 | English Democrats received 0.3% vote share in Sheffield Hallam in 2015.
- C52 | Jim Stop the Fiasco Wild (Independent) received 97 votes in Sheffield Hallam in 2015.
- C53 | In the 2019 UK general election, Conservatives won a majority with 365 seats.
- C54 | Democratic Unionist Party won 8 seats in the 2019 UK general election.
- C55 | Other parties won 15 seats in the 2019 UK general election.
- C56 | 326 seats are needed to win a majority in the UK general election.
- C57 | The constituency identifier for Sheffield Hallam is E14000922.
- C58 | The general election for Sheffield South East constituency was held on 12 December 2019.
- C59 | The Sheffield South East election was part of the general election for the 58th Parliament of the United Kingdom.
- C60 | Clive Betts of Labour held the Sheffield South East seat between 6 May 2010 and 30 May 2024.
- C61 | The Labour Party lost 59 seats compared to the preceding general election.
- C62 | Dennise Dawson of UKIP received 2,820 votes in Sheffield South East.
- C63 | Colin Ross of the Liberal Democrats received 1,432 votes in Sheffield South East.
- C64 | Ishleen Oberoi of the Social Democratic Party received 102 votes in Sheffield South East.
- C65 | Boris Johnson became Conservative Party leader on 23 July 2019.
- C66 | Boris Johnson's seat was Uxbridge and South Ruislip.
- C67 | Jeremy Corbyn's seat was Islington North.
- C68 | Jo Swinson's seat was East Dunbartonshire.
- C69 | Candidates gaining 5% or less of the vote share forfeit their deposit under section 13(b) of the Representation of the People Act 1985.
- C70 | Sheffield South East is a parliamentary constituency in the United Kingdom.
- C71 | Marc Bayliss was the Conservative candidate in Sheffield South East in the 2019 general election.
- C72 | Kirk Kus was the Brexit Party candidate in Sheffield South East in the 2019 general election.
- C73 | Rajin Chowdhury was the Liberal Democrat candidate in Sheffield South East in the 2019 general election.
- C74 | Alex Martin was the Yorkshire Party candidate in Sheffield South East in the 2019 general election.
- C75 | The Yorkshire Party received 966 votes in Sheffield South East in the 2019 general election.
- C76 | Sheffield South East had 67,832 registered voters in the 2019 general election.
- C77 | The turnout in Sheffield South East in the 2019 general election was 61.9%.
- C78 | Turnout in Sheffield South East decreased by 1.3% compared to 2017.
- C79 | Lindsey Cawrey was the Conservative candidate in Sheffield South East in the 2017 general election.
- C80 | A general election for the constituency of Bristol North West was held on 12 December 2019.
- C81 | The general election on 12 December 2019 was an election to the 58th Parliament of the United Kingdom.
- C82 | Vote change percentages for Bristol North West are calculated according to changes since the preceding general election and take no account of intervening by-elections.
- C83 | A notional election to the 58th Parliament of the United Kingdom for the constituency area of Bristol North West forms part of the notional general election on 12 December 2019.
- C84 | BBC News, ITV News, Sky News and the Press Association together produced estimates of the 2019 general election result as if new constituencies had been in existence.
- C85 | Karin Smyth is Labour's MP for Bristol South.
- C86 | Karin Smyth held onto her seat in Bristol South in the 2019 general election.
- C87 | Kerry McCarthy is Labour MP for Bristol East.
- C88 | The Greens doubled the party's votes in Bristol East compared to the 2017 election.
- C89 | The Greens made a 9,000 vote dent in Labour's majority in Bristol East in the 2019 election.
- C90 | Bristol East was the Greens' number one target seat in the 2019 election.
- C91 | Darren Jones is Labour's MP for Bristol North West.
- C92 | The 2019 general election turnout in Bristol was the highest in a generation.
- C93 | Bristol bucked the national trend for turnout in the 2019 general election.
- C94 | Bristol East saw an increase in voter numbers in the 2019 general election.
- C95 | The Bristol North West election was part of the general election for the 58th Parliament of the United Kingdom.
- C96 | Labour held Bristol North West constituency in the December 2019 general election.
- C97 | Darren Jones won with a majority of 5,692 votes in Bristol North West.
- C98 | The majority in Bristol North West was 10.2% of the vote.
- C99 | The turnout in Bristol North West was 73.3%.
- C100 | The electorate of Bristol North West was 76,273.
- C101 | The valid vote count in Bristol North West was 55,885.
- C102 | The invalid vote count in Bristol North West was 169.
- C103 | Darren Jones's vote share decreased by 1.7% compared to the preceding general election.
- C104 | Mark Weston was the Conservative party candidate in Bristol North West.
- C105 | Mark Weston received 21,638 votes in Bristol North West.
- C106 | Mark Weston's vote share decreased by 3.1% compared to the preceding general election.
- C107 | Chris Coleman was the Liberal Democrat party candidate in Bristol North West.
- C108 | Chris Coleman received 4,940 votes in Bristol North West.
- C109 | Heather Mack was the Green Party candidate in Bristol North West.
- C110 | Heather Mack received 1,977 votes in Bristol North West.
- C111 | Heather Mack's vote share increased by 1.2% compared to the preceding general election.
- C112 | The writ for the Bristol North West election was issued on 5 November 2019.
- C113 | The result for Bristol North West was declared at 03:24 on 13 December 2019.