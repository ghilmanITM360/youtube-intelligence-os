# Slot 07 · Short · Fact-check (Claude self-review; no expert review)
Access date for web/agency sources: 2026-11-24. Reproduce calculations with `python3 scripts/finding_checks.py` (fall/orbit/tide/light-time) in this package. Full ledger: `../../08_MASTER_CLAIM_LEDGER.csv`.

## Scenario definition
Real lunar laser ranging: a pulse sent from an Earth station to an Apollo retroreflector array and back; no hypothetical.

## Claim-by-claim table
| claim ID | script claim | type | source | location / detail | status |
|---|---|---|---|---|---|
| V07-C01 | A laser fired at the Moon returns light about two and a half seconds later. | observed fact | Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | about 2.5 s (APOLLO paper sections 5.2.1, 6; NIST page) | SOURCE_CHECKED |
| V07-C02 | Apollo crews left arrays of small corner mirrors on the Moon; each sends light back toward its source. | observed fact | Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | retroreflector arrays (Apollo 11, 14, 15) described in the paper | SOURCE_CHECKED |
| V07-C03 | The first echo was caught in August 1969, less than two weeks after the first landing. | observed fact | NIST, The Moon and back in 2.5 seconds | first echo 1 Aug 1969 (Lick); Apollo 11 landing 20 Jul 1969 | SOURCE_CHECKED |
| V07-C04 | Light needs about 1.3 seconds to cross the gap. | calculation | NASA NSSDC Moon fact sheet | 384,400 km / c | CALCULATED_SELF_REVIEW |
| V07-C05 | The Moon's distance changes, so the round trip runs from about 2.4 to 2.7 seconds. | calculation | NASA NSSDC Moon fact sheet | perigee 363,300 km and apogee 405,500 km (mean values) | CALCULATED_SELF_REVIEW |
| V07-C06 | A single pulse carries about three hundred quadrillion photons. | observed fact | Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | APOLLO 115 mJ, 532 nm pulse: ~3e17 photons (section 3.2.4) | SOURCE_CHECKED |
| V07-C07 | Most pulses bring back nothing detectable; in one set of runs the average was a fraction of a photon per pulse. | observed fact | Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | 0.25 (8 min), 0.23 (10,000 shots), 0.135 (5,000 shots) photons per shot, Apollo 15 array | SOURCE_CHECKED |
| V07-C08 | Stations fire thousands of pulses and add up the rare returns; in the best cases this pins the distance down to about a millimetre. | observed fact | Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | ~225-1,300 photons for a 1 mm normal point; 1.2 mm one-sigma in a 10,000-shot run | SOURCE_CHECKED |

## Sources and links (read depth stated)
| source | link / local reference | read depth |
|---|---|---|
| Murphy et al., APOLLO: the Apache Point Observatory Lunar Laser-ranging Operation (arXiv:0710.0890) | https://arxiv.org/abs/0710.0890 | FULL_TEXT_EXTRACTION (fetch-tool; figures unseen) |
| NIST, The Moon and back in 2.5 seconds | https://www.nist.gov/history/moon-and-back-25-seconds | EXTRACT_SUMMARY (earlier session) |
| NASA NSSDC Moon fact sheet | https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | EXTRACT_SUMMARY (earlier session) |

## Calculations and units
| claim | calculation / model output | assumptions | uncertainty / limit |
|---|---|---|---|
| V07-C02 | corner-cube property (textbook) | - | corner-cube counts not stated in the text read |
| V07-C03 | 12 days | - | - |
| V07-C04 | 1.282 s | mean distance | - |
| V07-C05 | 2.424 s - 2.705 s (extremes 2.38-2.71 s) | mean perigee/apogee | - |
| V07-C06 | 115 mJ / 3.7e-19 J = 3.1e17 | specific to APOLLO's laser | other stations differ |

## Known
- APOLLO paper: 115 mJ, 532 nm pulses (~3e17 photons); round trip ~2.5 s; average returns 0.135-0.25 photons per pulse on the Apollo 15 array; ~225-1,300 photons for a 1 mm normal point; 1.2 mm one-sigma in a 10,000-shot run.
- NIST: first echo 1 Aug 1969.
- NSSDC: mean perigee 363,300 km, apogee 405,500 km.

## Assumed
- Light-time = 2d/c with mean perigee/apogee.

## Uncertain
- Per-station return rates vary; later APOLLO runs exceeded one photon per shot (snippet, not read); extraction-level reading of the paper.

## Competing interpretation or earlier statements
- The earlier blueprint claimed an unsourced "one photon returns" twist; the primary paper says averages are below one photon per pulse.

## Required reviewer or source follow-up
- Read Murphy 2013 (PDF unreadable by the fetch tool); optional LLR instrument expert.

## What the script may claim
- Round trip about 2.4-2.7 s; most pulses return nothing detectable at APOLLO; best cases ~1 mm precision.

## What the script may NOT claim
- No claim that every pulse returns one photon; no universal photon-return rate.
