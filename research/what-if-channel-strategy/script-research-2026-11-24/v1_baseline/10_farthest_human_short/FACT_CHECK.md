# Slot 10 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A record question: the greatest documented distance between a human and the nearest other human (Guinness "most isolated human being"), Apollo 15, 1971; plus the April 2026 Artemis II records for contrast.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V10-C01 | The question is about distance to the nearest other person, not distance from Earth. | definition | Guinness World Records, Most isolated human being | record definition: farthest removed from nearest living fellow human | SOURCE_CHECKED |
| V10-C02 | In 1971 Apollo 15's Al Worden orbited the Moon alone while his two crewmates were on the surface; Guinness lists 3,596 km to his nearest fellow human. | observed fact | Guinness World Records, Most isolated human being | 3,596.4 km (2,234.69 mi), 30 Jul-1 Aug 1971 | TIME_SENSITIVE_RECHECK |
| V10-C03 | The Moon is about 3,500 km across. | calculation | NASA NSSDC Moon fact sheet | 2 x 1,737.4 km | CALCULATED_SELF_REVIEW |
| V10-C04 | Worden was on the far side about 120 km up and his crewmates on the near side; the Moon's width plus his height lands close to the record (our estimate, not Guinness's method). | calculation | Apollo Flight Journal entries on Apollo 15 solo orbit (web-search results) | 2R + h = 3,596.4 -> h = 121.6 km; Apollo 15 orbit ~97-124 km in flight-journal snippets | HYPOTHESIS |
| V10-C05 | Earth did not matter: everyone else was hundreds of thousands of km away. | calculation | NASA NSSDC Moon fact sheet | Moon perigee ~356,400 km (extreme) | CALCULATED_SELF_REVIEW |
| V10-C06 | In April 2026 the Artemis II crew travelled farther from Earth than anyone before. | observed fact | NASA, Artemis II crew eclipses record for farthest human spaceflight (2026-04-06) | passed Apollo 13's record on 6 Apr 2026 at 248,655 miles | SOURCE_CHECKED |
| V10-C07 | There were four of them, together. | observed fact | NASA, Artemis II crew eclipses record for farthest human spaceflight (2026-04-06) | crew: Wiseman, Glover, Koch, Hansen | SOURCE_CHECKED |
| V10-C08 | Isolation counts your nearest neighbour, not your distance from home. | definition | Guinness, Artemis astronauts break record for farthest distance between humans (April 2026) | Worden still holds 'most isolated'; Artemis II-Tiangong separation (419,656 km) is a different record | SOURCE_CHECKED |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| Guinness World Records, Most isolated human being | https://www.guinnessworldrecords.com/world-records/66111-most-isolated-human-being | EXTRACT_SUMMARY (fetch tool) |
| NASA NSSDC Moon fact sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | EXTRACT_SUMMARY (earlier session) |
| Apollo Flight Journal entries on Apollo 15 solo orbit (web-search results) | https://www.nasa.gov/history/afj/ap15fj/ | SNIPPET_ONLY |
| NASA, Artemis II crew eclipses record for farthest human spaceflight (2026-04-06) | https://www.nasa.gov/news-release/nasas-artemis-ii-crew-eclipses-record-for-farthest-human-spaceflight | EXTRACT_SUMMARY (fetch tool) |
| Guinness, Artemis astronauts break record for farthest distance between humans (April 2026) | https://www.guinnessworldrecords.com/news/2026/4/artemis-astronauts-break-record-for-farthest-distance-between-humans-during-epic-mission | EXTRACT_SUMMARY (fetch tool) |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V10-C03 | 3,474.8 km | mean radius | - |
| V10-C04 | 2R + h | far-side alignment with the landing site | Guinness method unstated; mission-report check pending |

## Known
- Guinness: Alfred M. Worden, Apollo 15 CM pilot, 30 Jul-1 Aug 1971, 3,596.4 km (2,234.69 mi) from his nearest living fellow human; Worden still holds it per Guinness April 2026.
- NASA: Artemis II passed Apollo 13's distance record on 6 Apr 2026 at 248,655 miles from Earth; four crew.
- Guinness April 2026: Artemis II vs Tiangong separation 419,656 km (different record).

## Assumed
- Far-side orbit alignment with the landing site and orbit height ~120 km (our geometry, not Guinness's stated method).

## Uncertain
- Altitude/method unstated; Apollo 15 orbit figures vary 97-124 km in flight-journal snippets; records may change.

## Competing interpretation or earlier statements
- Different definitions: nearest-person isolation vs farthest-from-Earth vs farthest-apart groups.

## Required reviewer or source follow-up
- Apollo 15 mission report for orbit altitude/apse alignment; re-open Guinness on release day.

## What the script may claim
- The record holder and Guinness figure as stated; the geometry as an estimate; the Artemis II distinction.

## What the script may NOT claim
- No claim that Guinness used 2R+h; no claim the record cannot be broken.
