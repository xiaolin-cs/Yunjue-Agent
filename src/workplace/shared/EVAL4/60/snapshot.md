You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
According to the National Park Service, using their NPSpecies data, compare the number of Non-native birds at Zion National Park, Canyonlands National Park, and Arches National Park. List all of the common names of these non-native bird species within the park with the largest number of non-native bird species in alphabetical order.

# Current Instruction
**T7** — Sort the common names of non-native bird species from the park with the largest number of non-native bird species in alphabetical order.

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
- C1 | The National Park Service maintains NPSpecies data for national parks.
- C2 | NPSpecies data contains information about bird species at national parks.
- C3 | Zion National Park has NPSpecies data available.
- C4 | Canyonlands National Park has NPSpecies data available.
- C5 | Bird species in NPSpecies data have common names recorded.
- C6 | The task requires identifying the park with the largest number of non-native bird species among Zion, Canyonlands, and Arches.
- C7 | The task requires listing common names of non-native birds alphabetically for the park with the most non-native bird species.
- C8 | NPSpecies data may be available in CSV or Excel format for download.
- C9 | Web search can be used to discover URLs for NPSpecies data pages.
- C10 | Text extraction from web pages can identify data download links for NPSpecies.
- C11 | Downloaded NPSpecies files can be parsed to extract species information.
- C12 | Python can be used to filter non-native birds from NPSpecies data.
- C13 | Python can be used to sort common names alphabetically.
- C14 | Vegetation Mapping Inventory Project data for Zion National Park were originally delivered in a Microsoft Access PLOTs database format.
- C15 | Species with 'Present' status occur in park with current, reliable evidence available.
- C16 | NPS Geodiversity Atlas contains data on the range of geology, cave/karst, and soil resources in parks.
- C17 | IRMA Services provides data sets for applications including park units, taxonomy, NPSpecies, park statistics, Data Store, landscape dynamics, and hydrographic impairment.
- C18 | National Capital Region Network (NCRN) has a goal to develop and maintain verified, substantiated, and certified vascular plant and vertebrate species lists for each network park.
- C19 | NCRN uses NPSpecies as the tool for meeting species list development and maintenance goals.
- C20 | NPSpecies version 1.9.3.24963-20240824-030002 is accessible through the IRMA Portal.
- C21 | Certified species lists from 312 US National Park Units are available from the NPSpecies IRMA database as of 05-Nov-2014.
- C22 | NPSpecies allows users to view, print, or download a checklist or more detailed species lists for a park.
- C23 | Species lists are works in progress with changes and updates made as more is learned.
- C24 | A primary goal of network monitoring is to develop and maintain certified species lists for vascular plants and vertebrate animals in each network park.
- C25 | ZION_AA-Species.csv is an open format data package from Zion National Park.
- C26 | Water quality and quantity data are available from NPS monitoring locations.
- C27 | NPS water quality data from lab samples are loaded from STORET.
- C28 | NPSpecies is operated by the National Park Service.
- C29 | The National Park Service is part of the U.S. Department of the Interior.
- C30 | NPSpecies is associated with Natural Resource Stewardship and Science division.
- C31 | NPSpecies search results can be displayed as a checklist.
- C32 | NPSpecies results can be sorted by Category Sort, Order, Family, and Scientific Name.
- C33 | NPSpecies is accessible through the IRMA Portal.
- C34 | NPSpecies requires users to choose a park as a required search criterion.
- C35 | The GitHub repository 'NPSpecies_US_NationalParks' by davidye007 contains a CSV file named 'NPS_Species_Present.csv'.
- C36 | The NPS_Species_Present.csv file contains columns including Park Code, Park Name, Category, Order, Family, Taxon Code, TSN, Taxon Record Status, Scientific Name, Common Names, Record Status, Occurrence, Nativeness, and Abundance.
- C37 | Acadia National Park has the park code ACAD.
- C38 | Alces alces (Moose) is present in Acadia National Park.
- C39 | Pensoft provides a downloadable CSV file at zookeys.pensoft.net/article/9420/download/csv/21/ containing species data.
- C40 | The Pensoft CSV file contains data for species Pseudopotamilla cf. P. reniformis.
- C41 | The Pensoft CSV file contains data for species Bispira manicata.
- C42 | Crematogaster buddhae Forel, 1902 is listed for Haryana with an Erroneous locality status.
- C43 | Crematogaster walshi Forel, 1902 is listed for Haryana, Himachal Pradesh, Punjab, Rajasthan, and Uttar Pradesh with an Erroneous locality status.
- C44 | Meranoplus rothneyi Forel, 1902 is listed for Haryana, Himachal Pradesh, and Punjab with an Erroneous locality status.
- C45 | Messor himalayanus (Forel, 1902) is listed for Haryana and Uttar Pradesh as a Misidentification of Messor instabilis.
- C46 | Monomorium dichroum Forel, 1902 is listed for Punjab with an Erroneous locality status.
- C47 | Monomorium monomorium Bolton, 1987 has uncertain taxonomic status and needs extensive taxonomic work.
- C48 | The GitHub repository tracykteal/data contains a species.csv file in the biology/data_orig directory.
- C49 | The tracykteal/data repository is used for Data Carpentry workshops.
- C50 | The GitHub repository veekun/pokedex contains a pokemon.csv file in the pokedex/data/csv directory.
- C51 | The pokemon.csv file contains columns including id, identifier, species_id, height, weight, base_experience, order, and is_default.
- C52 | The GitHub repository weecology/bibliometrics contains a keyword.csv file.
- C53 | The weecology/bibliometrics repository was last updated on July 7, 2024.
- C54 | A CSV file named NPS_Species_Present.csv exists at the file path /u/xlin4/Projects/multi-agent/Yunjue-Agent/
- C55 | The file NPS_Species_Present.csv has a size of 17770868 bytes
- C56 | The file access operation for NPS_Species_Present.csv was successful
- C57 | Acadia National Park (park code ACAD) contains Moose (Alces alces) as a mammal species.
- C58 | Northern White-tailed Deer (Odocoileus virginianus) in Acadia National Park are Native and Abundant.
- C59 | Coyote (Canis latrans) in Acadia National Park are Non-native and Common.
- C60 | Red Fox (Vulpes vulpes) in Acadia National Park have an Unknown nativeness status and are Common.
- C61 | Bobcat (Lynx rufus) in Acadia National Park are Non-native with Unknown abundance.
- C62 | River Otter (Lutra canadensis) in Acadia National Park are Native and Common.
- C63 | Fisher (Martes pennanti) in Acadia National Park are Native and Rare.
- C64 | Black Bear (Ursus americanus) in Acadia National Park are Native with Occasional abundance.
- C65 | Acadia National Park contains bird species including Bald Eagle (Haliaeetus leucocephalus).
- C66 | Peregrine Falcon (Falco peregrinus) in Acadia National Park are Non-native and Uncommon.
- C67 | Common Loon (Gavia immer) in Acadia National Park are Native and Common.
- C68 | Black-capped Chickadee (Poecile atricapillus) in Acadia National Park are Native and Abundant.
- C69 | Acadia National Park contains reptile species including Common Snapping Turtle (Chelydra serpentina).
- C70 | Ringneck Snake (Diadophis punctatus) in Acadia National Park are Native and Common.
- C71 | Acadia National Park contains amphibian species including American Toad (Bufo americanus).
- C72 | Spring Peeper (Pseudacris crucifer) in Acadia National Park are Native and Abundant.
- C73 | Acadia National Park contains fish species including American Eel (Anguilla rostrata).
- C74 | Brook Trout (Salvelinus fontinalis) in Acadia National Park are Native and Common.
- C75 | Acadia National Park contains vascular plant species including Yarrow (Achillea millefolium var. millefolium).
- C76 | Common Dandelion (Taraxacum officinale ssp. officinale) in Acadia National Park is Non-native and Common.
- C77 | The dataset uses TSN (Taxonomic Serial Number) as a taxonomic identifier system.
- C78 | Occurrence status values in the dataset include Present and Probably Present.
- C79 | Nativeness status values in the dataset include Native, Non-native, and Unknown.
- C80 | Abundance status values in the dataset include Rare, Uncommon, Occasional, Common, Abundant, and Unknown.
- C81 | Record Status values in the dataset include Approved and In Review.
- C82 | Acadia National Park contains species from multiple taxonomic categories including Mammal, Bird, Reptile, Amphibian, Fish, and Vascular Plant.
- C83 | The dataset includes both native and non-native species across all taxonomic categories.
- C84 | Some species in Acadia National Park have unknown nativeness status.