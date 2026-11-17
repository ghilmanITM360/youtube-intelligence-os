# EDITING DNA

Regenerated from `01_master_data/MASTER_SHOTS.csv` (200 shots). The prior
version claimed "Shot Type: UNKNOWN — 200" and "Transition Type: CUT — 200"
(i.e. literally every shot uniformly "CUT"), which does not match the actual
`TRANSITION_IN`/`TRANSITION_OUT` text in the schema — these are real free-text
fields, not a fixed enum, and are not uniform.

## Shot Transitions (measured, normalized)

`TRANSITION_IN` (146 non-empty as a cut-type keyword, 50 as a specific named motion description, 2 as literal `START`, 2 empty):

| TRANSITION_IN category | Count |
|---|---|
| Cut-family (CUT / HARD CUT / Hard cut / etc., case-insensitive) | 146 |
| Named motion description (e.g. "TAP cloud appears in one frame") | 50 |
| START (first shot of video) | 2 |
| Empty | 2 |

`TRANSITION_OUT`:

| TRANSITION_OUT category | Count |
|---|---|
| Named motion description | 125 |
| Cut-family | 60 |
| Empty (last shot of video, no exit) | 15 |

Shots overwhelmingly *enter* via a hard cut (73%) but *exit* via a specific named motion that triggers the next shot (62.5%) — the cut happens at the boundary, but what's documented as causing it differs by direction (entry = editorial cut event, exit = the last visual action before that cut).

## Shot Duration

- Total shots: 200
- Mean duration: 10.54s, median: 7.77s, range: 1.54–78.91s (the shortest is `how_long_could_you_drive_towards_the_sunset` S13; the 78.9s outlier is `worlds-largest-cities-what-if` S02, a single long continuous-pan shot — see `ASSET_DNA.md`'s note on that video's backbone map asset)
- A temporal-integrity pass corrected 132/200 shots whose `START_SEC`/`END_SEC` had been zeroed out during an earlier aggregation bug (7 videos' frame-index `TIMELINE.csv` values were never converted to seconds) — see `CONTINUATION_HANDOFF.md` for the full repair log. The duration distribution above reflects the corrected data; the previous 8.32s mean / 5.00s median were computed over the same corrupted zeros this pass fixed.

## Camera State (see `VISUAL_DNA.md` for the state-level breakdown)

89.8% of states report a LOCKED- or STATIC-family camera state — shot-to-shot change in this corpus is driven by hard cuts and illustrated content replacement, not camera movement.

## What is NOT supported by current data

- No fade/cross-dissolve transitions were found in `TRANSITION_IN`/`TRANSITION_OUT` text across the corpus — the schema has no such category, so this document makes no claim about them beyond noting hard cuts dominate.
- "Cut timing relative to sentence boundaries" is not computed here; see `AUDIO_VISUAL_SYNC_DNA.md`'s `STATE_CHANGE ↔ speech` section for the closest measured equivalent (66.8% of state changes occur during/near an active word).
