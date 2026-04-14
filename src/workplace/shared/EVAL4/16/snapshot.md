You are given a task context consisting of an overall objective and previously validated claims.

Use the validated claims below as already-established evidence. You must treat them as available facts for reasoning and planning. Do not ignore them. Build on them.

# Task Objective
I went on a three-day trip, starting in Cape Kiwanda on the first day, traveling to Shoshone Falls Park on the second day, and arriving at the American Heritage Center on the third day. I remember seeing some type of shrew that is apparently endemic to one of the areas we were in, but I can't remember its scientific name. It was at least 150 mm long. What was the scientific name of the one I am trying to remember? Use animalia.bio to source the info.

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
- C1 | The user went on a three-day trip.
- C2 | Cape Kiwanda was the location visited on the first day of the trip.
- C3 | Shoshone Falls Park was the location visited on the second day of the trip.
- C4 | The American Heritage Center was the location visited on the third day of the trip.
- C5 | The user saw a type of shrew during the trip.
- C6 | The shrew observed is endemic to one of the areas visited during the trip.
- C7 | The user needs to identify the scientific name of the shrew.
- C8 | The information source to use is animalia.bio.
- C9 | Baird's shrew (Sorex bairdi) is a species of mammal in the family Soricidae.
- C10 | Baird's shrew is endemic to northwest Oregon.
- C11 | Pacific shrew is endemic to western Oregon in the United States.
- C12 | Pacific shrew is native to western Oregon from Siltcoos lake to the coast going from the border line of Douglas and Lane counties continuing south to the northern parts of California.
- C13 | Pacific shrew is an insectivore.
- C14 | Pacific shrew is solitary.
- C15 | Pacific shrew is not a rare sight.
- C16 | Many species of mammals live in Oregon, which include opossums, shrews, moles, little pocket mice, great basin pocket mice, and dark kangaroo mouse.
- C17 | Baird's shrew fur is darker brown in winter than in summer.
- C18 | Males and females of Baird's shrew are about the same size.
- C19 | Baird's shrew feeds on insects, worms, snails, and spiders.
- C20 | Baird's shrew shares the forests of its range with six other species of shrew, such as the Pacific shrew.
- C21 | Baird's shrew body length ranges from 100 to 143 mm.
- C22 | Pacific shrew is the only shrew in Oregon without a tine on the anteromedial surface of the first upper incisor but with a posteriomedial ridge visible in anterior view through the gap between the incisors.
- C23 | Pacific shrew is often found in moist wooded areas with fallen decaying logs and brushy vegetation.
- C24 | Lesser forest shrew (Sylvisorex oriundus) is a species of mammal in the family Soricidae endemic to northeastern Democratic Republic of the Congo.
- C25 | Southeastern shrew is nocturnal.
- C26 | Southeastern shrews are active both day and night, spending most of their time in the burrows of other animals and rooting beneath the leaf litter on the forest floor.
- C27 | Southeastern shrew has a diet consisting primarily of spiders, as well as the larvae of butterflies, moths, slugs, and beetles.
- C28 | The six national wildlife refuges in the Nestucca Bay area include Cape Meares, Oregon Islands, Three Arch Rocks, Bandon Marsh, Nestucca Bay, and Siletz Bay.
- C29 | The northern Idaho ground squirrel (Urocitellus brunneus) is a species of the largest genus of ground squirrels.
- C30 | Shrews are very active animals with voracious appetites.
- C31 | Shrews do not hibernate but are capable of entering torpor.
- C32 | Niobe's shrew (Crocidura niobe) is a species of mammal in the family Soricidae.
- C33 | Niobe's shrew is native to the Albertine Rift montane forests.
- C34 | The Cinereus shrew (Sorex cinereus) is a small mole-like mammal found in the northern parts of North America.
- C35 | Cinereus shrews prefer humid areas with high levels of vegetation to hide in.
- C36 | Cinereus shrews are active day and night year-round.
- C37 | Cinereus shrews can eat three times their weight a day due to their high metabolism.
- C38 | Cinereus shrews are carnivores and herbivores (granivores).
- C39 | No overall population estimate is available for the Cinereus shrew according to the IUCN Red List.
- C40 | Pacific shrews are vermivorous, eating worms including annelids and nematodes.
- C41 | Pacific shrews are solitary animals that live singly and meet only for courtship and mating.
- C42 | Not much is known about the population of the Pacific shrew.
- C43 | The Masked Shrew (Sorex cinereus) occurs in Idaho.
- C44 | The southern short-tailed shrew (Blarina carolinensis) is a gray, short-tailed shrew that inhabits the eastern United States.
- C45 | Southern short-tailed shrews are carnivorous animals.
- C46 | Little is known about the mating system in Southern short-tailed shrews.
- C47 | There are no major threats to Southern short-tailed shrews at present.
- C48 | The IUCN Red List and other sources do not provide the Southern short-tailed shrew total population size.
- C49 | The long-clawed shrew (Sorex unguiculatus) is a species of shrew.
- C50 | An adult long-clawed shrew has a weight of less than 20 grams.
- C51 | The long-clawed shrew is distributed through the uplands of northeastern Asia, including northeastern North Korea.
- C52 | Red squirrel breeding may occur from March to September, but most activity occurs in the spring, between March and May.
- C53 | Red squirrel litter size varies from 2 to 9 young with an average of 5.2.
- C54 | The red squirrel is found throughout the northern boreal forest across Canada and the northern tier of states.
- C55 | Red squirrels store cones in small depressions in the ground away from their middens.
- C56 | Only the larger red squirrel middens seem to hold more than one winter's supply of food.
- C57 | Early foresters in Idaho would collect cones and their seeds from red squirrel middens for their tree nurseries.
- C58 | In the fall grizzlies seek out red squirrel middens where they eat the whitebark seeds from the cones stored by the red squirrel.
- C59 | The Pacific shrew (Sorex pacificus) is the largest brown shrew in western Oregon.
- C60 | The Pacific shrew weighs between ten and eighteen grams.
- C61 | The Pacific shrew has a total length (including tail) of 135 to 160 millimeters.
- C62 | The dwarf shrew (Sorex nanus) is a species of mammal in the family Soricidae.
- C63 | The dwarf shrew is endemic to Arizona, Colorado, Montana, Nebraska, New Mexico, South Dakota, Utah, and Wyoming in the United States.
- C64 | The dwarf shrew usually weighs 1.8 to 3.2 grams.
- C65 | The dwarf shrew changes its pelage (fur) based on the season to aid in hiding from predators.
- C66 | Dwarf shrews are found in dry brushy slopes in Colorado around 1,670 meters.
- C67 | In the past, mammalogists considered the dwarf shrew to be a rare species.
- C68 | The Inyo shrew is endemic to eastern California and to Nevada, in the Western United States.
- C69 | The American pygmy shrew (Sorex hoyi) is a small mole-like mammal.
- C70 | The American pygmy shrew was first discovered in 1831 by naturalist William Cane in Georgian Bay, Parry Sound.
- C71 | American pygmy shrews are solitary animals.
- C72 | American pygmy shrews are active year-round due to their high metabolism.
- C73 | American pygmy shrews are carnivores (insectivores).
- C74 | The American Pygmy Shrew (Sorex hoyi) has USFWS regulatory status of no special status.
- C75 | The American Pygmy Shrew has IUCN conservation status of Least Concern.
- C76 | The American Pygmy Shrew has WYNDD rank of G5, S1.
- C77 | The vagrant shrew (Sorex vagrans) is also known as the wandering shrew.
- C78 | Vagrant shrews are generally red brown in color with white or grey underparts.
- C79 | Coastal populations of vagrant shrews can be much darker, being almost black on the upper parts of the body.
- C80 | The basal metabolic rate of vagrant shrews is 5.4 ml O2/g/h.
- C81 | There is no evidence of torpor in vagrant shrews in winter.
- C82 | Vagrant shrews construct shallow cup-shaped nests, up to 8 cm (3.1 in) across, from vegetation and animal hair throughout most of the year.
- C83 | Vagrant shrews primarily breed between April and June.
- C84 | Births of vagrant shrews may occur as early as February, or as late as September.
- C85 | The Arizona shrew (Sorex arizonae) is a species of shrew native to North America.
- C86 | The Arizona shrew has a head and body 5 to 7 cm (2.0 to 2.8 in) in length.
- C87 | Arizona shrews inhabit primary forest with heavy undergrowth.
- C88 | Arizona shrews are believed to have diverged from the closely related Merriam's shrew relatively recently, during the late Pleistocene or early Holocene.
- C89 | Bobcat (Lynx rufus) is found in Idaho.
- C90 | Groundhog (Marmota monax) is found in Idaho.
- C91 | Pronghorn (Antilocapra americana) is found in Idaho.
- C92 | White-Tailed Deer (Odocoileus virginianus) is found in Idaho.
- C93 | Painted Turtle is found in Idaho.
- C94 | Idaho has 24 endemic animal species.
- C95 | California Dancer (Argia agrioides) is found in Idaho.
- C96 | Canada lynx (Lynx canadensis) is found in Idaho.
- C97 | Grizzly bear (Ursus arctos horribilis) is found in Idaho.
- C98 | North American wolverine (Gulo gulo luscus) is found in Idaho.
- C99 | The Nature Conservancy's conservation efforts in North Idaho focus on protecting grizzly bear habitat from development.
- C100 | Grizzly bears need to move throughout the landscape to use different habitats and maintain genetic diversity for species survival.
- C101 | North American beaver (Castor canadensis) plays a crucial role in Idaho by maintaining and shaping aquatic habitats.
- C102 | Teton Creek in Eastern Idaho provides critical spawning habitat for Yellowstone cutthroat trout.
- C103 | The Nature Conservancy has stewarded and restored Silver Creek for more than 40 years.
- C104 | Silver Creek is a thriving ecosystem for wild trout, hundreds of bird species, and animals like coyotes, bobcats, and moose.
- C105 | Bobcats (Lynx rufus) live in a variety of habitats including forests and deserts.
- C106 | Bobcats have been seen in many Idaho cities.
- C107 | BLM managed lands in Idaho encompass 10 diverse ecoregions.
- C108 | BLM managed lands in Idaho provide habitat for native plants, mammals, birds, reptiles, amphibians, and fish.
- C109 | 19 species in Idaho are listed as threatened or endangered under the Endangered Species Act.
- C110 | Coyotes are found in Idaho.
- C111 | Moose are found in Idaho.
- C112 | Yellowstone cutthroat trout are found in Idaho.
- C113 | Northern flying squirrel is found in Idaho.
- C114 | The dwarf shrew is a very small species of shrew.
- C115 | Dwarf shrew is not endemic to one location because it is found in 8 states.
- C116 | Body length data for dwarf shrew was not provided in the fetched content.
- C117 | The northern Idaho ground squirrel and the Southern Idaho ground squirrel were previously considered conspecific, together called the Idaho ground squirrel.
- C118 | Pelecanus halieus is a small fossil pelican.
- C119 | Pelecanus halieus was described by Alexander Wetmore.
- C120 | Pelecanus halieus was found in Late Pliocene deposits at Hagerman, Idaho.
- C121 | There are three endemic animal species listed for Idaho on the Animalia.bio website.
- C122 | The Idaho Ground Squirrel is listed as an endemic animal of Idaho.
- C123 | Pelecanus halieus is listed as an endemic animal of Idaho.