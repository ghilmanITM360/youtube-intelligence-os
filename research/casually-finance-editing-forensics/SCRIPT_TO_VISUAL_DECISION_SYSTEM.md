# Script-to-visual decision system (PRELIMINARY; design rules derived from observed co-occurrence in 10 Shorts)

These are **our rules inferred from what the sample does** (`ART_DIRECTION_INFERENCE`), not the creator's rules. For each sentence in the script, pick the first matching row, then apply the recipe in `KEYFRAME_RECIPE_LIBRARY.md`. Timing: cut or pop at 2-4 frames before the keyword onset; one new idea per scene.

| # | If the sentence... | Visual device | Operation | Recipe | Observed examples |
|---|---|---|---|---|---|
| 1 | opens the video with a claim or paradox | large character/object already on screen, caption appends | hook entrance (object motion matching the claim) | R01 | `Qof71Ef-3EU` S01; `HvnVO1_YrMQ` barrels; `7bm7XYssqlU` falling line |
| 2 | contains a number that carries the claim | hand-lettered number pops (red = bad/surprising, green = target/growth, black = neutral) | `OVERLAY_POP` on the keyword | R05 | '58%', '$429,000', '3%', '+1.8%' |
| 3 | cites a document, filing, article or official | screenshot full-bleed, push-in/scroll, highlight on the clause, presenter pops in | `CAMERA_SCROLL_ZOOM` + `HIGHLIGHT_SWEEP` | R07, R11 | `RB5zVghPor8` S08/S13; `ffIiiPLDFdM` S08; `7IMFHclDn8k` S13 |
| 4 | quotes a named person | bubble holding the quote beside a recurring official figure; highlight the key clause | bubble + text scroll | R07 | `RB5zVghPor8`, `7IMFHclDn8k` S17 |
| 5 | lists N things or steps | N props popped one at a time on each item's keyword; keep earlier props | sequential `POP_IN` | R03, R04 | bills `DEgQTSsSX9U`; DEBT docs `Es5c2MKzbDg`; buildings `7bm7XYssqlU` |
| 6 | explains a schedule/process over time | timeline line + unit props + end prop + label | progressive build | R04 | `DEgQTSsSX9U` f245-379 |
| 7 | compares A and B | one frame with both sides + divider/labels; or two charts together; X on rejected item, check on accepted | pops | R06 | `mT2hOLrCYSk` S19; `7bm7XYssqlU` S13; `Qof71Ef-3EU` S17 |
| 8 | negates ('isn't', 'except', 'not', 'doesn't') | red X, or a red word replaces the caption word, or a green check later undermined | `OVERLAY_POP` | R05, R10 | 'haven't' `Es5c2MKzbDg` f492; X over the paper `Qof71Ef-3EU` f219 |
| 9 | states a rising or falling quantity | draw a line/arrow left to right at constant speed; a falling line is red | `STROKE_REVEAL` linear | R01, R11 | `7bm7XYssqlU` f0-29; `Es5c2MKzbDg` f355-386 |
| 10 | personifies a country, institution or system | map/building/Earth character with eyes; bubble if it speaks | pop or scale-in; eye swap | R02, R10 | green US-map character (8/10 videos) |
| 11 | uses a metaphor verb (cut, tear, open, hand back, fade) | prop acts the verb | rotation, shape morph, drift, opacity fade | R12 | knife swing; torn bond; door swing; ? circle fade |
| 12 | is an aside, joke or analogy | one-scene pop-culture or analogy image | hard cut + hold | R10 | Shaq dunk; meme photo (rights!) |
| 13 | repeats an earlier sentence | return to the same scene sequence | hard cuts | R09 | `Qof71Ef-3EU` S01-S02 at 0 s and 26 s |
| 14 | is the last sentence | image of the thesis object, small character or larger key word; hold | pop or fade, then hold | R12, R13 | builder, crystal ball, '?' fade |
| 15 | needs dense evidence but no reading | montage of pages at 0.3-0.7 s, captions dropped | hard cuts | R09 | `Qof71Ef-3EU` f1936-2048 |

## Pacing rules
- New scene at every sentence boundary or pause >= 0.25 s; otherwise within a sentence only add objects.
- Target 1.7-4 s per scene; allow one long evidence scene (up to ~14 s) when a document is the point.
- Remove nothing within a scene; reset by cutting.
- Keep captions to ~5 words per chunk; show only the sentence being spoken; drop captions only for montage endings.

## Anti-patterns (not observed in the sample)
Fades/dissolves between scenes, bouncing/overshooting pops, ease-in-out on every move, long unreadable full-page screenshots held without a highlight, summary end cards, simultaneous introduction of two unrelated objects.

## Validation hook
Run `scripts/forensic_features.py` on your render and compare: hard cuts/min 12-24; events/min 40-70; static-frame share 60-90 %; median cut-to-word offset -150..+50 ms.
