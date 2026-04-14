You are given a task context consisting of an overall objective, previously validated claims, and the current instruction to execute.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
Among Jakks Pacific, Hasbro, Mattel, and Funko which company had the highest debt-to-capital ratio for the fiscal year ended December 31, 2023? Use the SEC website and filings.

# Current Instruction
**T16** — Parse the downloaded Jakks Pacific text file to extract consolidated balance sheet data showing total debt and total stockholders' equity as of December 31, 2023

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
- C1 | The task requires identifying which company among Jakks Pacific, Hasbro, Mattel, and Funko had the highest debt-to-capital ratio for the fiscal year ended December 31, 2023.
- C2 | Jakks Pacific is one of the four companies to be analyzed for debt-to-capital ratio.
- C3 | Hasbro is one of the four companies to be analyzed for debt-to-capital ratio.
- C4 | Funko is one of the four companies to be analyzed for debt-to-capital ratio.
- C5 | The fiscal year period under analysis is the year ended December 31, 2023.
- C6 | The data source to be used is the SEC website and filings.
- C7 | The metric to be calculated and compared is the debt-to-capital ratio.
- C8 | The fetch_web_content tool should be used to search and navigate SEC EDGAR to locate 10-K filings for each company for fiscal year 2023.
- C9 | The download_file tool should be used to download the identified 10-K filing documents in HTML or PDF format from SEC to local storage.
- C10 | The extract_pdf_text tool should be used to extract text content from downloaded PDF 10-K filings if needed.
- C11 | The execute_python tool should be used to calculate debt-to-capital ratios from extracted financial data and determine which company has the highest ratio.
- C12 | 10-K filings are the type of SEC filing documents that contain the required financial information.
- C13 | SEC EDGAR is the system to navigate for locating company filings.
- C14 | JAKKS PACIFIC INC has CIK number 0001009829.
- C15 | JAKKS PACIFIC INC has a mailing address at 2951 28TH STREET SANTA MONICA CA 90405.
- C16 | JAKKS PACIFIC INC has a business phone number 424-268-9444.
- C17 | JAKKS PACIFIC INC operates under SIC code 3944.
- C18 | SIC code 3944 represents GAMES, TOYS & CHILDREN'S VEHICLES (NO DOLLS & BICYCLES).
- C19 | JAKKS PACIFIC INC is located in California.
- C20 | JAKKS PACIFIC INC has a fiscal year end date of 1231 (December 31).
- C21 | JAKKS PACIFIC INC filed a 10-K on 2026-03-02 with accession number 0001185185-26-000723.
- C22 | A download attempt for the URL https://www.sec.gov/Archives/edgar/data/1009829/000118518524000243/0001185185-24-000243-index.htm failed after 3 attempts.
- C23 | The file_size value is null for the failed download.
- C24 | The success status of the download operation is false.
- C25 | The SEC EDGAR filing identifier is 0001185185-24-000243.
- C26 | The CIK (Central Index Key) associated with the filing is 1009829.
- C27 | Hasbro, Inc. has CIK number 0000046080.
- C28 | Hasbro, Inc. is classified under SIC code 3944, which corresponds to 'Games, Toys & Children's Vehicles (No Dolls & Bicycles)'.
- C29 | Hasbro, Inc. is incorporated in Rhode Island (RI).
- C30 | Hasbro, Inc. has a fiscal year end date of December 28 (1228).
- C31 | Hasbro, Inc. was formerly named 'Hasbro Inc' with filings through July 2, 2019.
- C32 | Hasbro, Inc. has a mailing address at 1027 Newport Avenue, Pawtucket, RI 02861-0200.
- C33 | Hasbro, Inc. has a business phone number 4014318697.
- C34 | Hasbro, Inc. is assigned to SEC filing office 04 (Manufacturing).
- C35 | Hasbro, Inc. filed a 10-K annual report on February 25, 2026, with accession number 0000046080-26-000011.
- C36 | Funko, Inc. has CIK number 0001704711.
- C37 | Funko, Inc.'s mailing address is 2802 Wetmore Ave, Everett, WA 98201.
- C38 | Funko, Inc.'s business phone number is 425-783-3616.
- C39 | Funko, Inc. is classified under SIC code 3944 for Games, Toys & Children's Vehicles (No Dolls & Bicycles).
- C40 | Funko, Inc.'s state location is Washington (WA).
- C41 | Funko, Inc.'s fiscal year end is December 31 (1231).
- C42 | Funko, Inc. is under CF Office 04 Manufacturing.
- C43 | Funko, Inc. filed a 10-K annual report on 2026-03-12 with accession number 0001704711-26-000020.
- C44 | The 10-K filing on 2026-03-12 has film number 26748338.
- C45 | JAKKS PACIFIC, INC. filed a 10-K document type.
- C46 | JAKKS PACIFIC, INC. had 10,798,353 common stock shares outstanding as of March 15, 2024.
- C47 | JAKKS PACIFIC, INC. has ICFR auditor attestation flag set to true.
- C48 | JAKKS PACIFIC, INC. auditor is BDO USA, P.C.
- C49 | JAKKS PACIFIC, INC. film number is 24753087.
- C50 | Hasbro, Inc. filed a 10-K document type.
- C51 | Hasbro, Inc.'s common stock trades under the symbol HAS.
- C52 | Hasbro, Inc.'s entity public float as of July 2, 2023 was $8,933,575,963.
- C53 | Hasbro, Inc. had 138,791,480 common stock shares outstanding as of February 13, 2024.
- C54 | Portions of Hasbro, Inc.'s definitive proxy statement for the 2024 Annual Meeting of Shareholders are incorporated by reference into Part III of the 10-K report.
- C55 | Hasbro, Inc. has filed all required reports under Section 13 or 15(d) of the Securities Exchange Act of 1934 during the preceding 12 months.
- C56 | Mattel Inc is incorporated in Delaware.
- C57 | Mattel Inc's CIK number is 0000063276.
- C58 | Mattel Inc's SIC code is 3942.
- C59 | SIC code 3942 corresponds to 'Dolls & Stuffed Toys'.
- C60 | Mattel Inc's fiscal year end is December 31.
- C61 | Mattel Inc's mailing address is 333 Continental Blvd, El Segundo, CA 90245.
- C62 | Mattel Inc's business phone number is 310-252-2000.
- C63 | Mattel Inc is classified under CF Office 04 Manufacturing.
- C64 | Mattel Inc filed a 10-K annual report on February 23, 2026.
- C65 | Funko, Inc. filed a 10-K document type.
- C66 | Funko, Inc.'s tax identification number is 35-2593276.
- C67 | Funko, Inc.'s Class A Common Stock has par value $0.0001.
- C68 | Funko, Inc. is not a well-known seasoned issuer.
- C69 | Funko, Inc.'s entity public float was $372.3 million as of June 30, 2023.
- C70 | Funko, Inc. had 50,792,897 shares of Class A Common Stock outstanding as of March 5, 2024.
- C71 | Funko, Inc.'s 10-K includes consolidated statements of operations, comprehensive income, balance sheets, stockholders' equity, and cash flows.
- C72 | Funko, Inc. incorporates portions of its definitive Proxy Statement for the 2024 Annual Meeting of Stockholders by reference in Part III of its 10-K.
- C73 | The page fetch failed due to anti-bot protection.
- C74 | The blocking reason includes structural issue 'no_content_elements'.
- C75 | The blocking reason includes 'script_heavy_shell' characteristic.
- C76 | The fetched page contains 6302 bytes of data.
- C77 | The page response size is 6393 bytes.
- C78 | The page contains 61 visible characters.
- C79 | Jakks Pacific filed Form 10-K for fiscal year 2023 (ended December 31, 2023) on March 15, 2024.
- C80 | Mattel's 10-K for fiscal year 2023 has accession number 0001628280-24-011371.
- C81 | Funko filed Form 10-K for fiscal year 2023 (ended December 31, 2023) on March 7, 2024.
- C82 | Funko's CIK number is 0001704711.
- C83 | Funko's 10-K for fiscal year 2023 has accession number 0001704711-24-000013.
- C84 | XBRL viewer pages for Jakks Pacific, Hasbro, Mattel, and Funko were accessed but returned only structural metadata without actual balance sheet or debt ratio data.
- C85 | The Jakks Pacific XBRL viewer URL is https://www.sec.gov/cgi-bin/viewer?action=view&cik=1009829&accession_number=0001185185-24-000243&xbrl_type=v.
- C86 | Direct access to Jakks Pacific's 10-K HTML document at https://www.sec.gov/ix?doc=/Archives/edgar/data/1009829/000118518524000243/jakkspacif20231231_10k.htm was blocked by anti-bot protection.
- C87 | The anti-bot protection blocking Jakks Pacific's 10-K HTML document reported structural issues: no_content_elements and script_heavy_shell (6302 bytes, 61 chars visible).
- C88 | Direct access to Hasbro's 10-K HTML document at https://www.sec.gov/ix?doc=/Archives/edgar/data/46080/000004608024000034/has-20231231.htm was blocked by anti-bot protection.
- C89 | The document filename is fnko-20231231.htm.
- C90 | The document date reference in the filename is 2023-12-31.
- C91 | JAKKS Pacific, Inc. has an IRS Employer Identification Number of 95-4527222.
- C92 | JAKKS Pacific, Inc. is classified as an Accelerated Filer under SEC regulations.
- C93 | The aggregate market value of JAKKS Pacific, Inc.'s common equity held by non-affiliates as of June 30, 2023 was $142,701,187.
- C94 | JAKKS Pacific, Inc. is a leading multi-product line, multi-brand toy company that designs, produces, markets, sells and distributes toys and related kid-targeted consumer products.
- C95 | JAKKS Pacific, Inc. focuses its business on acquiring or licensing well-recognized intellectual property, trademarks and/or brand names, most with long product histories (evergreen brands).
- C96 | JAKKS Pacific, Inc. produces action figures and accessories based on licensed characters including Nintendo, Sonic the Hedgehog, and Apex Legends franchises, and proprietary brands including Creepy Crawlers.
- C97 | JAKKS Pacific, Inc. produces toy vehicles including Xtreme Power Dozer, Xtreme Power Dump Truck, XPV, Road Champs, Fly Wheels, and AirTitans inflatable remote-control dinosaur.
- C98 | JAKKS Pacific, Inc. produces dolls and accessories based on licenses including Disney Wish, Disney Encanto, Disney ILY 4EVER, Disney Frozen, Disney Princess, and Minnie Mouse.
- C99 | JAKKS Pacific, Inc. produces infant and pre-school toys based on PBS's Daniel Tiger's Neighborhood and in-house brands such as Perfectly Cute and collectable plush Ami Amis.
- C100 | JAKKS Pacific, Inc. produces foot-to-floor ride-on products based on Fisher-Price, Nickelodeon, and Hasbro licenses.
- C101 | JAKKS Pacific, Inc. produces outdoor activity toys including ReDo Skateboard Co. and junior sports toys including Sky Ball hyper-charged balls, SportsZone sport sets, and Wave Hoop toy hoops marketed under the Maui brand.
- C102 | JAKKS Pacific, Inc. produces board games under the brand JAKKS Wild Games, including Temple Raider, K.O. Corral, and Galactic JAXX.
- C103 | JAKKS Pacific, Inc.'s three largest customers are Target, Walmart, and Amazon, which accounted for 30.3%, 20.8%, and 10.5% respectively of net sales in 2023.
- C104 | No customer other than Target, Walmart, and Amazon accounted for more than 10% of JAKKS Pacific, Inc.'s net sales in 2023.
- C105 | JAKKS Pacific, Inc. sells products through its own in-house sales staff and independent sales representatives to various retail channels including toy and mass-market retail chain stores, department stores, office supply stores, drug and grocery store chains, club stores, dollar stores, toy specialty stores and wholesalers.
- C106 | JAKKS Pacific, Inc. generally sells products to customers on open account with payment terms typically varying from 30 to 90 days or pursuant to letters of credit.
- C107 | JAKKS Pacific, Inc. contracts the manufacture of most of its products to unaffiliated manufacturers located principally in China.
- C108 | JAKKS Pacific, Inc. contracts the manufacture of certain products from Hong Kong Meisheng Cultural Company Limited (Meisheng), which involved payments to Meisheng of approximately $75.7 million for the year ended December 31, 2023.
- C109 | As of December 31, 2023, Meisheng owns 5.2% of JAKKS Pacific, Inc.'s outstanding common stock.
- C110 | Zhao Xiaoqiang, one of JAKKS Pacific, Inc.'s directors, is executive director of Meisheng.
- C111 | In 2023, 61.4% of JAKKS Pacific, Inc.'s net sales were made in the third and fourth quarters.
- C112 | Generally, the first quarter is the period of lowest shipments and sales in JAKKS Pacific, Inc.'s business and in the toy industry, and therefore it is also the least profitable quarter due to various fixed costs.
- C113 | Sales of JAKKS Pacific, Inc.'s products generated outside the United States were approximately $153.7 million, or 21.6% of total net sales in 2023.
- C114 | In 2020, JAKKS Pacific, Inc. migrated from a distributor model to selling direct in Spain, Italy, France and Mexico.
- C115 | JAKKS Pacific, Inc. utilizes warehouses in the United Kingdom, the Netherlands, and Italy (opened in 2023) to support sales expansion in Europe.
- C116 | As of December 31, 2023, JAKKS Pacific, Inc. had approximately 659 employees (including temporary and seasonal employees) working in over 10 countries worldwide.
- C117 | JAKKS Pacific, Inc.'s license agreements generally require the company to make specified minimum royalty payments.
- C118 | JAKKS Pacific, Inc. has license agreements with Nickelodeon, Disney, Pixar, Marvel, NBC Universal, Microsoft, Sega, Sony, Netflix, and WarnerMedia.
- C119 | JAKKS Pacific, Inc.'s tools, dies and molds had a net book value of $13.7 million as of December 31, 2023.
- C120 | Substantially all of JAKKS Pacific, Inc.'s tools, dies and molds are located in China.
- C121 | According to Toy Association, Inc., total retail sales of toys (excluding video games) in the United States were approximately $28.0 billion in 2023.
- C122 | JAKKS Pacific, Inc. entered into a binding definitive agreement with JPMorgan Chase for an asset-based credit line in June 2021.
- C123 | JAKKS Pacific, Inc. has entered into an At the Market Issuance Sales Agreement (ATM Agreement) pursuant to which the company may issue up to $75.0 million of common stock.
- C124 | Stephen G. Berman is JAKKS Pacific, Inc.'s Chairman and Chief Executive Officer.
- C125 | Stephen G. Berman is under contract with JAKKS Pacific, Inc. through 2026.
- C126 | JAKKS Pacific, Inc. experienced a threat to the security of its computer systems in December 2022 which resulted in the leakage of certain data, including information about employees.
- C127 | The December 2022 cybersecurity incident at JAKKS Pacific, Inc. did not result in material damage to operations or cash flow.
- C128 | JAKKS Pacific, Inc.'s common stock trades under the symbol JAKK on The NASDAQ Global Select Market.
- C129 | The closing sale price of JAKKS Pacific, Inc.'s common stock on June 30, 2023 was $19.97.
- C130 | Payments to Meisheng were approximately $75.7 million for the year ended December 31, 2023.
- C131 | Royalties payable to inventors and developers generally range from 1% to 5% of the wholesale sales price for each unit of a product sold by JAKKS Pacific, Inc.
- C132 | JAKKS Pacific, Inc. has on file with the SEC an effective registration statement pursuant to which it may issue up to $150 million of securities.
- C133 | The $150 million shelf registration capacity will be reduced by any amount of securities sold pursuant to the ATM Agreement.
- C134 | Stephen G. Berman is under contract through 2026.
- C135 | The United States is the world's largest toy market, followed by China, Japan and Western Europe.
- C136 | Hasbro and Mattel are the two largest United States toy companies.
- C137 | The LEGO Group is headquartered in Denmark.
- C138 | XBRL viewer pages for the four companies were accessed but returned only structural metadata without balance sheet or debt ratio data.
- C139 | Direct HTML document access for Jakks Pacific fiscal year 2023 10-K was blocked by anti-bot protection.
- C140 | Direct HTML document access for Hasbro fiscal year 2023 10-K was blocked by anti-bot protection.
- C141 | Index file download for SEC filings failed with 403 Forbidden error.
- C142 | No validated claims contain total debt figures for Jakks Pacific as of December 31, 2023.
- C143 | No validated claims contain total debt figures for Hasbro as of December 31, 2023.
- C144 | No validated claims contain total debt figures for Funko as of December 31, 2023.
- C145 | The complete submission text file URL for Mattel fiscal year 2023 10-K is https://www.sec.gov/Archives/edgar/data/63276/000162828024011371/0001628280-24-011371.txt.
- C146 | The complete submission text file URL for Funko fiscal year 2023 10-K is https://www.sec.gov/Archives/edgar/data/1704711/000170471124000013/0001704711-24-000013.txt.
- C147 | The debt-to-capital ratio calculation formula is total debt divided by the sum of total debt and total stockholders' equity.
- C148 | All four companies filed 10-K reports for fiscal year 2023 ended December 31, 2023.
- C149 | The validated claims establish filing metadata including CIK numbers, accession numbers, and filing dates for all four companies.
- C150 | The task cannot be completed based on currently validated claims alone because actual financial data from balance sheets has not been successfully extracted.
- C151 | The file path for the Hasbro 10-K 2023 complete document is /tmp/hasbro_10k_2023_complete.txt
- C152 | The Hasbro 10-K 2023 complete document file size is 21402920 bytes
- C153 | The file operation for the Hasbro 10-K 2023 complete document was successful