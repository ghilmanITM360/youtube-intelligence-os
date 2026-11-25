# START HERE — Unreasonably Exact: 10 What If-style story blueprints (2026-11-24)

Blueprint research only. Not scripts, not approvals, not publication permission. SELF-REVIEW: no qualified reviewer has examined anything. The calendar file and the repo were not modified (nothing committed or pushed).

Folder: `~/Documents/YIOS-local-audits/2026-11-24-what-if-10-story-blueprints/`
Repo used: `/Users/ghilmanislam360/Documents/youtube-intelligence-os`, branch `research/what-if-channel-strategy-2026-11-18`.

## Status of each video
| # | Day | Format | Working title | Status | Biggest open issue | Blueprint |
|---|---|---|---|---|---|---|
| 1 | 1 | Long | Would a Fall From Space Make You Hit the Ground Faster? | BLUEPRINT READY FOR OWNER REVIEW | landing-speed value depends on drag (164–204 km/h); 100 km segment is model-only | [01](blueprints/01_LONG_HIGHER_FALL.md) |
| 2 | 4 | Short | Why Can a Skydiver Slow Down Without a Parachute? | BLUEPRINT READY FOR OWNER REVIEW | same drag review | [02](blueprints/02_SHORT_SKYDIVER_SLOWDOWN.md) |
| 3 | 7 | Short | Why Does a Signal Take a Day to Reach Voyager 1? | BLUEPRINT READY FOR OWNER REVIEW | NASA status must be re-checked on the release day | [03](blueprints/03_SHORT_VOYAGER_SIGNAL.md) |
| 4 | 10 | Long | Could One Sideways Jump Put You in Orbit? | BLUEPRINT READY FOR OWNER REVIEW | overlap with "Little Planet"; toy model must be labelled | [04](blueprints/04_LONG_TINY_WORLD_ORBIT.md) |
| 5 | 13 | Short | Could You Jump Off a Moon and Never Come Back? | PARTIAL — NEEDS SOURCE/CALCULATION | Mars-pull twist is a sphere-model hypothesis; needs a shape-model check | [05](blueprints/05_SHORT_PHOBOS_ESCAPE.md) |
| 6 | 16 | Long | Why Would a Reply From Voyager Take Two Days? | PARTIAL — NEEDS SOURCE/CALCULATION (+ editorial decision) | stretched-Short risk; 2024 precedent only at snippet level; status unknown | [06](blueprints/06_LONG_VOYAGER_REPLY.md) |
| 7 | 19 | Short | How Long Does a Laser Take to Reach the Moon and Return? | PARTIAL — NEEDS SOURCE/CALCULATION | photon-return twist needs the primary paper | [07](blueprints/07_SHORT_LUNAR_LASER.md) |
| 8 | 22 | Long | What Would Happen to the Ocean If the Moon Vanished? | PARTIAL — NEEDS SOURCE/CALCULATION | ocean response and decay time unsourced; tilt/spin claims gated | [08](blueprints/08_LONG_MOON_OCEAN.md) |
| 9 | 25 | Short | Would Earth Still Have Tides Without the Moon? | BLUEPRINT READY FOR OWNER REVIEW | "about a fifth" only with the 13–35 % range and caveats | [09](blueprints/09_SHORT_SOLAR_TIDES.md) |
| 10 | 28 | Short | How Far Has a Human Been From Every Other Person? | BLUEPRINT READY FOR OWNER REVIEW — NEEDS EDITORIAL DECISION | exact-question overlap with Munroe's "Loneliest Human" | [10](blueprints/10_SHORT_FARTHEST_HUMAN.md) |

6 ready for owner review (one with an editorial decision), 4 partial, 0 blocked.
Neutron-star Long: unchanged future candidate on HOLD (not researched, not inserted).

## Files
- `00_MASTER_DIRECTIVE.md` (full instruction), `01_RULES_AND_SUCCESS_CRITERIA.md`, `02_PROGRESS_CHECKPOINT.md`
- `03_SOURCE_REGISTER.csv` (36 sources, with what was actually read), `04_OPEN_QUESTIONS_AND_DECISIONS.md`
- `05_EXISTING_RESEARCH_AND_REFERENCE_MAP.md`, `06_TEN_VIDEO_REFERENCE_AND_ORIGINALITY_CROSSWALK.csv`
- `07_CLAIM_AND_SOURCE_LEDGER.csv` (claim IDs V01-C01 … V10-C07, NS-01), `08_CALCULATIONS_AND_ASSUMPTIONS.md`
- `09_CALENDAR_COHERENCE_AND_DEPENDENCIES.md`, `10_SELF_REVIEW_AND_OPEN_ISSUES.md`
- `blueprints/` (10 files, sections A–J), `scripts/` (calculation code, raw NOAA data, outputs, table builders, validator)

## Read first
1. `10_SELF_REVIEW_AND_OPEN_ISSUES.md` §3 (what was not done) and §4 (what needs an expert).
2. `09_CALENDAR_COHERENCE_AND_DEPENDENCIES.md` §4 (issues A–D with alternatives).
3. `04_OPEN_QUESTIONS_AND_DECISIONS.md` (owner decisions).

## Re-run
```bash
cd ~/Documents/YIOS-local-audits/2026-11-24-what-if-10-story-blueprints
python3 scripts/fall_model.py; python3 scripts/orbit_small_world.py; python3 scripts/phobos_escape.py; python3 scripts/light_time_tides_isolation.py
python3 scripts/build_tables.py; python3 scripts/build_ledger.py; python3 scripts/validate_outputs.py
```
