# Phase Thirteen: production workflow (master "Phase Thirteen"), 2026-11-18

Status: workflow definition only. Detailed editing execution is reserved for a later phase (as the master says). Tools named below exist in the repo today unless marked "none yet". Who does each step (people, hours, software) is UNKNOWN; "Responsible" names a role, not a person. Every video passes the same gates in order; steps 1 to 7 end before any script is written.

Roles (placeholders): O owner (approvals), R researcher, W writer, D designer, E editor, V voice, Q quality reviewer (a human who checks every number, manual check C5).

| # | Step | Required inputs | Expected outputs | Quality checklist | Relevant documents / tools | Responsible | Approval |
|---|---|---|---|---|---|---|---|
| 1 | Topic discovery | competitor DB, Trends, search, news, owner ideas | candidate list with dates | topic not from one-day news only; source dated | `09_TOPIC_DISCOVERY`, DB | R | none |
| 2 | Topic validation | candidate | Phase Four scorecard row, gates G1 to G4, Phase Ten note | 4 gates pass; trend not declining; research date recorded | `17_TOPIC_VALIDATION` | R | O approves topic |
| 3 | Research collection | approved topic | source pack: primary URLs, tables, dates, screenshots | every number has a primary source or a SECONDARY label | `24_SOURCE_DATA_AND_REFERENCES` | R | none |
| 4 | Video angle development | source pack | one-paragraph angle and "what competitors miss" | answers Phase Eight section 4 questions | `22_ORIGINALITY_...` | R, W | none |
| 5 | Title development | angle | 5+ titles scored (8 criteria) | claims true; forecast vs fact wording; no template echo | Phase Nine format | W | none |
| 6 | Thumbnail concept | angle, titles | 3 concepts with the 9 fields | one idea, 1 to 4 words, no look-alike; phone-size legibility | Phase Nine | D | none |
| 7 | Packaging approval | titles, thumbnails | approved title + thumbnail pair | combined packaging check; Packaging SOP and checklist | DS-000011 SOP | O | **O approves** (gate before any script) |
| 8 | Script research | approved pair | outline with sources per beat | primary data on screen planned | source pack | R | none |
| 9 | Script writing | outline | script saved as `productions/<project>/**/*SCRIPT*.md` with title/channel/images header | own words; no competitor text; sources section | `scripts/check_slop_risk.py` | W | none |
| 10 | Script analysis | script | slop gate verdict, findings, checklist C1 to C5 shown to owner | gate not FAIL; verdict shown; a PASS is a proxy only | `check_slop_risk.py`, framework plan via `run_youtube_intelligence.py --framework-plan` (structural only) | Q | O sees verdict |
| 11 | Hook analysis | script | hook notes: first 5 s, 5 to 15 s | contradiction in the first lines; no greeting; no unsourced number | Phase E hook models | Q | none |
| 12 | Intro analysis | script | intro length and promise check | payoff promised early; no padding | DS-000011 Intro Analyzer (heuristic only) | Q | none |
| 13 | Visual storyboard | final script | shot list: chart per beat, source tag on screen | one chart per beat; own style (branding direction) | `yios-visual-storyboard` skill (existing) | D | none |
| 14 | Asset research | storyboard | licensed or self-made assets, data files | licences recorded; no competitor images | `docs/LOCAL_MEDIA_AVAILABILITY.md`; media root rule | D | none |
| 15 | Animation and editing | assets, voiceover | rough cut | real data; labelled voice policy followed; detailed system reserved for a later phase | none yet | E, V | none |
| 16 | Quality control | rough cut | fixed cut | every number re-checked against source (C5); captions; audio | checklist | Q | O sign-off |
| 17 | Copyright / originality audit | final cut, script, thumbnail | audit note | R1 to R7 clean, C1 to C5 confirmed, synthetic-content disclosure if realistic AI visuals (C3) | AI-SLOP-RISK-RULES, official page 14328491 | Q | O |
| 18 | Upload preparation | final video | title, description with sources, chapters, A/B variants set up (long-form only, up to 3, winner by watch time) | description lists sources; thumbnails legible at phone size | official page 16391400 | O | O |
| 19 | Publishing | prepared upload | published video | human cadence (C1); Phase Ten re-check within 7 days for news topics | calendar | O | O |
| 20 | Performance analysis | Studio data after 7 and 28 days | review note | compare within our own channel only; never against competitors' public views | Phase Fourteen | O, R | O |

## Handoff and storage rules (repo policy)
- Keep media outside temporary folders; resolve through `YIOS_MEDIA_ROOT`; originals preserved and checksummed; no raw video through GitHub.
- No scripts, branches, merges or commits without owner go; the research folder is untracked on the current branch.
- One owner per task; two-Mac claim rules in AGENTS.md apply to shared steps.

## Gaps
- No software or hours are named; capacity is UNKNOWN, so the number of videos per week stays provisional.
- `production_pipeline.py validate` (repo root) runs the gate for `productions/` projects; a project folder for this channel has not been created (needs owner go).
- Voice, music and stock licensing sources are undecided.
