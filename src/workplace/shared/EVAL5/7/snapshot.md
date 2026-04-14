You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Which champion was picked most often by the losing team's top laner in the 2013 North American League Championship Series Summer Finals?

# Current Instruction
**T4** — Search for detailed match data and champion picks from the 2013 North American League Championship Series Summer Finals games

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
- C1 | The NA LCS 2013 Summer split was the second split of the 2013 North American LCS season.
- C2 | The top six teams advanced to the Playoffs in the NA LCS 2013 Summer split.
- C3 | The NA LCS 2013 Summer Playoffs were played in a single-elimination format.
- C4 | Team SoloMid had a 14-14 record in the NA LCS 2013 Summer split.
- C5 | BloodWater played for Team Vulcun in the NA LCS 2013 Summer split.
- C6 | Dyrus played for Team SoloMid in the NA LCS 2013 Summer split.
- C7 | Reginald played for Team SoloMid in the NA LCS 2013 Summer split.
- C8 | TheOddOne played for Team SoloMid in the NA LCS 2013 Summer split.
- C9 | WildTurtle played for Team SoloMid in the NA LCS 2013 Summer split.
- C10 | Xpecial played for Team SoloMid in the NA LCS 2013 Summer split.
- C11 | Xmithie played for Team Vulcun in the NA LCS 2013 Summer split.
- C12 | Eight teams competed in a round robin group stage in the NA LCS 2013 Summer split.
- C13 | Each team played all other teams in the NA LCS 2013 Summer regular season.
- C14 | Team SoloMid defeated Cloud9 at the North American League of Legends Championship Series Summer Finals.
- C15 | Cloud9 had a 15-2 record at one point during the NA LCS 2013 Summer split.
- C16 | Cloud9 destroyed TSM in week 6 of the NA LCS 2013 Summer split.
- C17 | Velocity got 2 victories versus CLG and Vulcun in the NA LCS 2013 Summer split.
- C18 | The NA LCS Season 3 Summer Playoffs took place from August 30, 2013, to September 1, 2013.
- C19 | Riot Games organized the NA LCS Season 3 Summer Playoffs.
- C20 | The Grand Finals of the NA LCS Season 3 Summer Playoffs were best of five, and all other matches were best of three.
- C21 | The total prizepool for the NA LCS Season 3 Summer Playoffs was $100,000 US Dollars.
- C22 | TSM placed second in the NA LCS Season 3 Summer Playoffs and received $25,000.
- C23 | Team Vulcun placed third in the NA LCS Season 3 Summer Playoffs and received $15,000.
- C24 | Dignitas placed fourth in the NA LCS Season 3 Summer Playoffs and received $10,000.
- C25 | Counter Logic Gaming (CLG) placed fifth in the NA LCS Season 3 Summer Playoffs.
- C26 | Team Curse placed sixth in the NA LCS Season 3 Summer Playoffs.
- C27 | TSM defeated CLG 2-0 in the NA LCS Season 3 Summer Playoffs Quarterfinals.
- C28 | Dignitas defeated Team Curse 2-1 in the NA LCS Season 3 Summer Playoffs Quarterfinals.
- C29 | Team Vulcun defeated Dignitas 2-0 in the NA LCS Season 3 Summer Playoffs Third-Place Match.
- C30 | CLG defeated Team Curse 2-0 in the NA LCS Season 3 Summer Playoffs Fifth-Place Match.
- C31 | CLG finished sixth in the NA LCS Season 3 Summer Season.
- C32 | The Cloud9 roster at the NA LCS Season 3 Summer Playoffs consisted of Balls, Meteos, Hai, Sneaky, and LemonNation, with Alex Penn as coach.
- C33 | The TSM roster at the NA LCS Season 3 Summer Playoffs consisted of Dyrus, TheOddOne, Reginald, WildTurtle, and Xpecial.
- C34 | The Team Vulcun roster at the NA LCS Season 3 Summer Playoffs consisted of Sycho Sid, Xmithie, mancloud, Zuna, and BloodWater.
- C35 | The Dignitas roster at the NA LCS Season 3 Summer Playoffs consisted of KiWiKiD, Crumbz, scarra, imaqtpie, and Patoy.
- C36 | The CLG roster at the NA LCS Season 3 Summer Playoffs consisted of Nien, bigfatlp, Link, Doublelift, and Chauster, with MonteCristo as coach.
- C37 | The broadcast talent for the NA LCS Season 3 Summer Playoffs included Jatt, Phreak, Riv, and Kobe.
- C38 | Jatt served as a Color Caster for the NA LCS Season 3 Summer Playoffs.
- C39 | Phreak served as a Play-by-Play and Color Caster for the NA LCS Season 3 Summer Playoffs.
- C40 | Riv served as a Play-by-Play Caster for the NA LCS Season 3 Summer Playoffs.
- C41 | Kobe served as a Color Caster for the NA LCS Season 3 Summer Playoffs.
- C42 | The Riot Season 3 Championship Series was the first season of North America's fully professional League of Legends league.
- C43 | Xpecial was interviewed after TSM's Quarterfinals victory over CLG.
- C44 | Crumbz was interviewed after Dignitas's Quarterfinals victory over Team Curse.
- C45 | Nien was interviewed after CLG's Fifth-Place Match victory over Team Curse.
- C46 | Dyrus was interviewed after TSM's Semifinals victory over Team Vulcun.
- C47 | Hai was interviewed after Cloud9's Semifinals victory over Dignitas.
- C48 | Zuna was interviewed after Team Vulcun's Third-Place Match victory over Dignitas.
- C49 | Balls, Meteos, Hai, Sneaky, LemonNation, Alex Penn, and Jack were interviewed after Cloud9's Finals victory over TSM.
- C50 | TSM was the losing team in the 2013 North American League Championship Series Summer Finals.
- C51 | Dyrus was TSM's top laner in the NA LCS Season 3 Summer Playoffs.
- C52 | Three finals games were played between Cloud9 and TSM on September 1-2, 2013.
- C53 | The Match History page contains columns for Date, Blue team, Red team, Winner, Bans, Picks, and Rosters.
- C54 | The specific champion picks for individual finals games are not displayed in the retrieved text content from the Match History page.
- C55 | A Picks and Bans page exists at https://lol.fandom.com/wiki/NA_LCS/Season_3/Summer_Playoffs/Picks_and_Bans that may contain detailed champion pick data.
- C56 | The losing team's top laner in the 2013 NA LCS Summer Finals was Dyrus from TSM.
- C57 | TheOddOne was on TSM's roster in the 2013 NA LCS Summer Playoffs.
- C58 | Xpecial was on TSM's roster in the 2013 NA LCS Summer Playoffs.
- C59 | TSM picked Zac in the top lane position in Grand Finals Game 1 against Cloud9.
- C60 | TSM picked Sona in Grand Finals Game 1 against Cloud9.
- C61 | Dyrus played Zac in Grand Finals Game 1 for TSM.
- C62 | Zac was picked twice by TSM's top laner across all three Grand Finals games.
- C63 | Zac was the most frequently picked champion by TSM's top laner Dyrus in the 2013 NA LCS Summer Finals.
- C64 | Cloud9 won Grand Finals Game 1 against TSM.