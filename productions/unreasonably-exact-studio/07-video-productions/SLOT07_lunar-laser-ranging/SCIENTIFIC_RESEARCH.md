# Scientific research, Slot 07 (accessed 2026-11-26)

Claim-by-claim results are in `SCIENTIFIC_CLAIMS_LEDGER.csv` (13 rows, C01-C13). This file records **how** each source was read, so the confidence is honest.

## How sources were read

| Source | Read by | Confidence |
|---|---|---|
| NASA NSSDCA Moon Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html | me, in the built-in browser (full page text) | VERIFIED |
| ILRS "Apollo and Luna Reflectors", https://ilrs.gsfc.nasa.gov/missions/satellite_missions/current_missions/ap11_reflector.html | me, in the browser (text and screenshot) | VERIFIED |
| Murphy 2013, "Lunar laser ranging: the millimeter challenge", arXiv:1309.6294 | a subagent, via the ar5iv HTML copy (about 80 of 129 thousand characters verbatim; Secs 5.3 onward summary only) | V-2nd; sections cited per figure |
| Murphy et al. 2008, APOLLO instrument paper, arXiv:0710.0890 | a subagent, via ar5iv (Abstract to Sec 3.3 verbatim) | V-2nd |
| UCSD "Lunar Retroreflectors", https://tmurphy.physics.ucsd.edu/apollo/lrrr.html | a subagent (full page) | V-2nd |

The arXiv PDF could not be opened in the browser (it triggers a file download; a save dialog was shown to you and I did not retry), so nothing was downloaded by me.

## What the film may now say (all sourced)

- Mean distance 384,400 km; range about 357,000 to 407,000 km; round trip about 2.56 s on average, about 2.38 to 2.71 s over the cycle (C01-C04).
- Apollo 11 and 14: 100 fused-silica corner cubes, 3.8 cm each, on a 46 cm panel; Apollo 15: 300 cubes; sites Sea of Tranquility, Fra Mauro, Hadley Rille; two French-built 14-cube arrays on Luna 17 and 21 (C05).
- A corner cube returns light back exactly the way it came (C06).
- Of a launched beam, about 1 photon in 25 million even finds the Apollo 11 array (1.9 km spot for 1 arcsec seeing); the return then spreads again; total throughput about 1e-18 (C07).
- Best-case return: about 3 photons per shot (Apollo 15 on the 3.5 m APOLLO telescope), far fewer at smaller stations; laser 532 nm, about 90 ps pulse, 20 Hz (C08).
- The atmosphere adds about 1.5 m of delay at zenith, modelled from pressure measurements (C09).
- 1 mm of one-way range is 6.7 ps of round-trip time; modern precision is millimetres (C10).

## The C06 correction (changed from the first draft)

First draft: "misleading". After reading Murphy and UCSD: the *reflector* returns the light that enters it, but the *array* catches only about one photon in 25 million of the beam, so "a tiny fraction of incoming light" is **true if "incoming light" means the whole beam** and **false if read as what the reflector sends back**. It is ambiguous, not wrong. The picture rule in the ledger removes the ambiguity (show the km-wide footprint against the 46 cm array). **Owner decision 2026-11-26: keep the recorded line; the footprint inset at B20 is mandatory.** The recording was not changed.

## Not found / not done

- The exact atmospheric-correction method (Murphy Secs 5.3-5.4) was not read verbatim.
- Apollo 11 deployment details (astronaut, date) came from search snippets (JPL caption, Wikipedia), not the primary page; do not put names on screen yet.
- No ILRS station-by-station return statistics were found.
- **No video was watched.** The brief's video analysis (`research/video_analysis/`) is NOT PERFORMED; an agent can inspect pages and still frames but cannot honestly claim to have watched footage.
