You are given a task context consisting of an overall objective and previously validated claims.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
I'm researching extreme weather in the United States. Between 2017 and 2021 (inclusive), which year saw flood-related fatalities in over 20 states, with over 100 total deaths (with all states combined)? This includes both flash flooding and river flooding. Use National Weather Service and NOAA data.

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
- C1 | The research task focuses on extreme weather in the United States between 2017 and 2021 inclusive.
- C2 | The task requires identifying a year with flood-related fatalities in over 20 states.
- C3 | Flash flooding and river flooding are both included in the flood-related fatalities count.
- C4 | National Weather Service data should be used for this research.
- C5 | The fetch_web_content tool can retrieve flood fatality data pages from NOAA and National Weather Service websites for 2017-2021.
- C6 | The download_file tool can download data files in CSV, Excel, or PDF formats containing flood statistics from official sources.
- C7 | The parse_pdf_text tool can extract text from PDF reports if flood data is provided in PDF format.
- C8 | The extract_tabular_data tool can parse HTML tables containing flood fatality statistics by state and year.
- C9 | The execute_python tool can analyze collected data to count states with flood deaths and total fatalities per year.
- C10 | The execute_python tool can identify which year or years meet the criteria of over 20 states and over 100 total deaths.
- C11 | The National Weather Service provides U.S. Natural Hazard Statistics on weather-related fatalities, injuries, and damages.
- C12 | Storm Data database comprises information from NWS forecast offices in the 50 states, Puerto Rico, Guam, and the Virgin Islands.
- C13 | NOAA National Centers for Environmental Information provides public data access through the Storm Events Database.
- C14 | Weather Related Fatality and Injury Statistics include data categories for Cold, Flood, Heat, Lightning, Tornado, Tropical Cyclone, Wind, and Winter Storm.
- C15 | Weather Related Fatality and Injury Statistics are available for years 1995 through 2024.
- C16 | An 80-Year List of Severe Weather Fatalities is available as a separate resource.
- C17 | Preliminary Hazardous Weather Statistics for 2023 are available online.
- C18 | Hurricane/Tropical Cyclone event fatalities, injuries, and damage estimates are attributed only to wind.
- C19 | Tropical cyclone hazards such as storm surge inundation, rainfall-induced flooding, and tornadoes are listed within separate event types in the database.
- C20 | National Weather Service issues Tropical Cyclone Reports available at www.hurricanes.gov/data/tcr/index.php.
- C21 | The Centers for Disease Control and Prevention is the official government source of cause of death in the United States, including weather-related fatalities.
- C22 | The National Weather Service National Headquarters is located at 1325 East West Highway, Silver Spring, MD 20910.
- C23 | Weather.gov provides local weather forecasts.
- C24 | Weather.gov provides aviation weather information.
- C25 | Weather.gov provides rivers and lakes information.
- C26 | Weather.gov provides hurricane information.
- C27 | Weather.gov provides sunrise and sunset information.
- C28 | The National Weather Service runs the SKYWARN Storm Spotters program.
- C29 | The National Weather Service operates the TsunamiReady program.
- C30 | The National Weather Service maintains a presence on X (formerly Twitter).
- C31 | The National Weather Service provides RSS feeds.
- C32 | The National Hurricane Center is accessible through Weather.gov.
- C33 | Weather.gov provides damage, fatality, and injury statistics.
- C34 | Weather.gov provides astronomical data.
- C35 | Archived weather data is available through NCDC (National Climatic Data Center).
- C36 | The Storm Events Database documents the occurrence of storms and other significant weather phenomena having sufficient intensity to cause loss of life, injuries, significant property damage, and/or disruption to commerce.
- C37 | The Storm Events Database documents rare, unusual weather phenomena that generate media attention, such as snow flurries in South Florida or the San Diego coastal area.
- C38 | The Storm Events Database currently contains data from January 1950 to December 2025.
- C39 | Due to changes in data collection and processing procedures over time, there are unique periods of record available depending on the event type in the Storm Events Database.
- C40 | NCEI has performed data reformatting and standardization of event types in the Storm Events Database.
- C41 | NCEI has not changed any data values for locations, fatalities, injuries, damage, narratives and any other event specific information in the Storm Events Database.
- C42 | Users can register their email address with NCEI to receive future information regarding access system downtime, data issues, new features and general news about the Storm Events Database.
- C43 | The Storm Events Database website is accessible at www.ncei.noaa.gov/stormevents/.
- C44 | Bulk data from the Storm Events Database are available in comma-separated files (CSV) format.
- C45 | Storm Events Database bulk data can be accessed via FTP at ftp://ftp.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/.
- C46 | Detailed information about Storm Events Database fields and columns is available in a PDF document named Storm-Data-Bulk-csv-Format.pdf.
- C47 | Documentation on the Storm Events Database file naming convention is available in a README file.
- C48 | The Storm Events Database website provides links to external resources including NOAA's SPC Reports, NOAA's SPC WCM Page, and NOAA's NWS Damage Assessment Toolkit.
- C49 | NOAA's NWS provides documentation for the Storm Events Database available at https://www.nws.noaa.gov/directives/sym/pd01016005curr.pdf.
- C50 | The Storm Events Database website provides information about the Tornado EF Scale at https://www.spc.noaa.gov/efscale.
- C51 | The directory /pub/data/swdi/stormevents/csvfiles/ contains storm events data files organized by year from 1950 to 2025.
- C52 | The directory contains three types of storm event files: details, fatalities, and locations.
- C53 | Storm event detail files are named with the pattern StormEvents_details-ftp_v1.0_dYYYY_c20260323.csv.gz where YYYY represents the year.
- C54 | The data files were last modified on 2026-03-23 for most years.
- C55 | The directory contains a README file last modified on 2026-03-24 12:05 with size 2013 bytes.
- C56 | The directory contains a file named Storm-Data-Bulk-csv-Format.pdf with size 341218 bytes last modified on 2026-03-11 12:00.
- C57 | The directory contains a legacy subdirectory last modified on 2014-05-14 11:00.
- C58 | The directory contains a file named ugc_areas.csv with size 924123 bytes last modified on 2014-02-18 09:15.
- C59 | Storm event detail files range in size from 10508 bytes for 1950 to 15695066 bytes for 2011.
- C60 | Storm event detail file sizes generally increase over time from early years to recent years.
- C61 | Storm event fatality files are significantly smaller than detail files, ranging from 286 bytes to 14785 bytes.
- C62 | All storm events data files are compressed in gzip format with .csv.gz extension.
- C63 | The file version identifier v1.0 is consistent across all storm events data files.
- C64 | The creation timestamp c20260323 appears in the filename of all storm events data files.
- C65 | A file named fatalities_2021.csv.gz exists at the path /u/xlin4/Projects/multi-agent/Yunjue-Agent/fatalities_2021.csv.gz
- C66 | The file fatalities_2021.csv.gz has a size of 13322 bytes
- C67 | The 2017 fatality dataset contains a column named 'FAT_YEARMONTH'.
- C68 | A KeyError occurred when attempting to access the column 'EVENT_TYPE' in the 2017 fatality dataset.
- C69 | The sample data includes a fatality record with FAT_YEARMONTH value 201702.
- C70 | The error occurred at line 24 of the executed Python code.
- C71 | The error originated from a pandas DataFrame __getitem__ operation attempting to access a non-existent column.
- C72 | A file exists at path '/u/xlin4/Projects/multi-agent/Yunjue-Agent/details_2021.csv.gz'.
- C73 | The file 'details_2021.csv.gz' has a size of 10563953 bytes.
- C74 | The file operation for 'details_2021.csv.gz' completed successfully.
- C75 | The NWS hazstat pages for flood statistics for the year 2017 return 'Page Not Found' errors.
- C76 | NOAA NCEI Storm Events Database provides bulk CSV downloads for fatality data.
- C77 | The event details data file for 2017 was successfully downloaded to /u/xlin4/Projects/multi-agent/Yunjue-Agent/details_2017.csv.gz.
- C78 | The event details data file for 2017 has a size of 9343148 bytes.
- C79 | The fatality data files do not contain an EVENT_TYPE column.
- C80 | The EVENT_TYPE column is needed to filter flood events from the fatality data.
- C81 | The fatality data contains an EVENT_ID field that can be used to join with event details data.