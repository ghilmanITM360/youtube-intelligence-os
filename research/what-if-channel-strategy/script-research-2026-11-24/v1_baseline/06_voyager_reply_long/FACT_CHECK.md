# Slot 06 · Long · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
A real historical repair (Voyager 1, Nov 2023 - Apr 2024) viewed through the light-time delay; plus a dated status of the Nov 2026 outage. No hypothetical dialogue.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V06-C01 | On 18 April 2024 engineers sent a message to Voyager 1 and two days later learned it had worked. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | fix sent 18 Apr; heard back 20 Apr | SOURCE_CHECKED |
| V06-C02 | Voyager 1 was launched in 1977 and is the most distant human-made object. | observed fact | NASA Voyager 1 mission pages (launch date, speed) via web search | NASA mission page: launched 5 Sept 1977; JPL page title 'most distant human-made object' | SOURCE_CHECKED |
| V06-C03 | A signal needed about 22.5 hours each way in April 2024; so each question is worth about two days. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | 'about 22.5 hours' each way; ~45 h round trip is arithmetic | SOURCE_CHECKED |
| V06-C04 | On 14 November 2023 Voyager 1 stopped sending readable data but still received commands; about five months without usable health/status data. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | fault began 14 Nov 2023; usable data returned 20 Apr 2024 | SOURCE_CHECKED |
| V06-C05 | Even with idle antennas, five months allows fewer than ninety attempts at a two-day cycle. | calculation | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | 158 days x 24 h / 45 h = 84 | CALCULATED_SELF_REVIEW |
| V06-C06 | By March 2024 the fault was traced to one of three onboard computers (flight data subsystem); one memory chip had stopped working, holding part of its software. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | diagnosis section | SOURCE_CHECKED |
| V06-C07 | The chip could not be repaired, so the team split the code into sections stored in different places, adjusted them to work together and updated references. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | fix section | SOURCE_CHECKED |
| V06-C08 | They began with the section that packages engineering data, sent on 18 April; on 20 April the spacecraft answered and engineers could see health data for the first time in five months. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | timing section | SOURCE_CHECKED |
| V06-C09 | NASA said the team would spend the following weeks moving the other affected software, including parts needed to return science data. | observed fact | NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | remaining-work section | SOURCE_CHECKED |
| V06-C10 | As of late November 2026 Voyager 1 is about 26 billion km away, one light-day, so each way takes 24 hours. | observed fact | NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | 25.9 billion km; 24 h each way | TIME_SENSITIVE_RECHECK |
| V06-C11 | On 14 November 2026 the team found Voyager 1 had stopped sending science and engineering data; a carrier signal still arrives; NASA suspects an onboard computer but says it is unconfirmed; diagnosis may take weeks or longer; I could not find a later update. | observed fact | NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | blog 2026-11-18 (updated 2026-11-20); search 2026-11-24 | TIME_SENSITIVE_RECHECK |
| V06-C12 | The two faults are three years apart on the same calendar date; NASA has not said they are linked. | calculation | NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | 2023-11-14 and 2026-11-14 | CALCULATED_SELF_REVIEW |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| NASA Voyager blog 'NASA's Voyager 1 Resumes Sending Engineering Updates to Earth' (2024-04-22) | https://science.nasa.gov/blogs/voyager/2024/04/22/nasas-voyager-1-resumes-sending-engineering-updates-to-earth/ | EXTRACT_SUMMARY (fetch tool) |
| NASA Voyager 1 mission pages (launch date, speed) via web search | https://science.nasa.gov/mission/voyager/voyager-1/ | SNIPPET_ONLY |
| NASA release 'Voyager 1 makes history reaching one light-day' (2026-11-19) and NASA Voyager blog 2026-11-18 (page updated 2026-11-20) | https://science.nasa.gov/blogs/voyager/2026/11/18/voyager-1-engineers-analyze-data-issue-ready-to-confirm-light-day/ | EXTRACT_SUMMARY (fetch tool) |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V06-C03 | 2 x 22.5 = 45 h | - | 24e9 km gives 22.2 h; NASA rounds |
| V06-C05 | upper bound | antenna always free; 45 h cycle | ignores scheduling and analysis time |
| V06-C10 | d/c | - | time-sensitive |
| V06-C12 | date arithmetic | - | NASA says the team is using 2023 experience and checking a link to an October 2026 pause |

## Known
- NASA 2024-04-22: fault from 14 Nov 2023; cause traced to one of three onboard computers (FDS) in March 2024; chip failed; code split and relocated; command sent 18 Apr; reply 20 Apr; about 22.5 h each way.
- NASA 2026-11-18/20: one light-day (25.9 billion km); no science/engineering data since 14 Nov 2026; carrier received; diagnosis may take weeks or longer.

## Assumed
- Fewer than ninety attempts = upper bound at 45 h per cycle ignoring scheduling.
- The "patient" analogy is illustrative.

## Uncertain
- 2026 cause and outcome unknown; NASA wording may change; post-April-2024 progress not read here.

## Competing interpretation or earlier statements
- The calendar title asks "why would a reply take two days"; the script answers that and reframes to repair. Alternative view: this could be only a Short (see STATUS).

## Required reviewer or source follow-up
- Production-day NASA recheck; read the 2024-04-04 NASA post and later 2024 updates.
- Optional spacecraft-engineer review of the "split and relocate" description.

## What the script may claim
- The 2024 timeline as NASA states it; the 2026 status as NASA states it, dated.

## What the script may NOT claim
- No claim that Voyager will reply; no claim about the 2026 cause; no invented engineer dialogue.
