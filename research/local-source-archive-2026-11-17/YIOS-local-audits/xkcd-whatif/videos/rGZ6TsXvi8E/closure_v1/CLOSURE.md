# rGZ6TsXvi8E: visual-only closure (contract v1; LOCAL ONLY)

## Evidence base
- **Source:** the sha re-computed from the file matches the manifest (checks.json V1, 1e4498d5…). 3117 frames. Every frame is measured and covered exactly once (V2).
- **Reused:** the rv1 ledger (109 segments, 55 holds) and its measurements. rv1 left 11 segments unviewed (622 frames).
- **New in closure_v1/:**
  - native frames;
  - holds_01..14.jpg, all 55 holds, viewed;
  - activity_grid_a.jpg: every frame of G0004, G0012, G0016, G0018 and G0030 at 1/8 scale, viewed;
  - activity_grid_b.jpg: all 436 frames of G0078 and G0080 at 1/8 scale, viewed;
  - g78_80_samples.jpg: 8 native frames at 0.3 scale, used for text;
  - strips of every frame of G0040, G0052, G0054, G0058, G0072, G0088 and G0094, viewed;
  - residue_crops.png;
  - per-frame change series and checks.json.
- **Disclosure:** the grids are at 1/8 scale.

## V4/V5 resolutions
| Seg | rv1 | Resolution |
|---|---|---|
| G0004 f162–267 (f161 onset) | MEDIUM POP_ON_SEQUENCE | **Not pops.** Each new sun **slides out** of the previous one, stepping right and down; suns below the horizon turn grey (fill change as they cross). The red X, the green ✓, then a second red X and the red dotted verticals **fade in**. f161 (in-hold, 272 px component) is the onset slide of the first copy. |
| G0012 f331–351 | MEDIUM | Cut to a grey sun below the horizon at left. A yellow sun slides up out of it, then a grey copy slides down right. A red X pops (f351). |
| G0016 f390–394 | MEDIUM | 5-f **shutter/door-open reveal**: the yellow square skews into a hinged panel and opens on a window with a hatted stick figure; a red X pops. |
| G0018 f425–460 | MEDIUM | Sun copies slide out step by step along the horizon. The last one gains wobble lines and a `BRWWAAK` crack label. |
| G0030 f629–672 | MEDIUM | A sun slides down behind the mountain and turns grey, then a yellow copy slides up on the right. |
| G0040 f857 | LOW, "INFERRED small zoom" | **Zoom refuted.** It is a 1-frame pop of the black `1000 km/h` arrow label: the bbox is local (742–895, 852–951) and the next frame is 0 px. |
| G0052 f1068 | LOW, NO_VISIBLE_CHANGE | **Resolved:** a 1-frame pop of a second car with a red arrow (4.4k px; next frame 0). |
| G0054 f1125 | LOW | 1-frame pop of a further car and red arrow pair. |
| G0058 f1276–1283 | MEDIUM | 8-f **cross-dissolve**: `NORTH POLE, 90°N` → `LONGYEARBYEN, 78°N`; the seals and ice dissolve out and the hills and car dissolve in. |
| G0072 f1682–1685 | — | Sun chain built in 4 f (suns slide in successively). |
| G0078 f1782–1997 | MEDIUM, 210 f unviewed | Cut to a grey map of northern Norway with a dark night region. The red `NW` with up arrows is replaced by `DAY` / `NIGHT` labels and then by red `SW` with down arrows (f1921). At f1922 the map changes to a close view with a car on a road, and a **DAY / SUNSET / NIGHT** band with a red glow enters lower-left and **sweeps up-right** across the map; an inset with suns appears top-right (f1997). |
| G0080 f2074–2293 | MEDIUM, 214 f unviewed | The terminator band keeps sweeping past the car. The inset **grows**, adding sun copies one after another (2 → 8 suns, the later ones grey). Cut at f2293 to the presenter at a laptop. |
| **Hold G0087 f2471–2473** | not in ledger | **Ledger correction:** `ARCTIC CIRCLE` keeps **typing** during this "hold" (letter components 625–1238 px). The write-on runs continuously f2469–2476 across G0086, G0087 and G0088. |
| G0094 f2672–2675 | MEDIUM | 4-f build: the church and steeple appear, a small figure and the sun pop, then a grey ground band wipes down with the Svalbard map and the `LONGYEARBYEN` label. |

**Other hold residue:** f3001 is NOISE (11 px). Hold-pair shifts (max 384 px) fall between states separated by cuts or slides within one shot ID. No camera moves were found.

## V6 creative (text read from native holds)
- **Text:**
  - `NOT A SUNSET`, `NOT TOUCHING THE HORIZON (YET)`;
  - `BRWWAAK`;
  - `SUNSET ZONE`, `W` / `E`, black and red `1000 km/h`, `OH NO!`;
  - `NORTH POLE, 90°N`, `LONGYEARBYEN, 78°N`, `~55 min`, `WEST`, `355 mph`;
  - `NW`, `SW`, `DAY` / `SUNSET` / `NIGHT`;
  - `PyEphem` (third-party software name), `ARCTIC CIRCLE`, `~95 min`, `LONGYEARBYEN`;
  - `WHAT ARE YOU DOING?` / `LENGTHENING THE SUNSET` / `PUSHING BACK THE NIGHT` / `GIVING ME A LITTLE MORE TIME` / `HERE WITH YOU.`
- **Colour:**
  - flat yellow sun discs (saturated accent) on off-white;
  - **saturated PAINTED_PLATE sunset**, bookending the video;
  - a dark-grey GLOW plate with a white light source;
  - twilight gradient plates (blue/magenta);
  - grey MAP_TOUR maps with a reddish terminator glow;
  - a pastel orange/red dashed sunset-zone band on the globe;
  - red and green marks.
  - No photographs and no full-frame red.
- **INFERRED rv1 claims tested:**
  - the G0040 zoom is refuted;
  - G0050 "zoom out" is NOT re-tested here (left INFERRED as in rv1);
  - "POP_ON_SEQUENCE" in G0004, G0012, G0018 and G0030 is corrected to slide-out sequences.
- **Originality flags:** the software logo/name must not be reused. The closing lines are original text in the source but should **not be reused verbatim**.

## V7
- `reconstruction_blueprint_v2.md`: per-state prompts, motion, continuity, QA and originality.
- **Format:** an ORDINARY explainer Short with a MAP_TOUR middle and a painted bookend. Dev-library observation only.
- The grey maps are **not** MAP_FILL (achromatic), and the terminator sweep is not a camera instance. This video is therefore **not** a positive case for either v9 feature.

## Status
**VISUAL_ANALYSIS_COMPLETE** (visual-only contract v1). visual_script_mapping, audio and AV are out of scope and remain unsigned.
