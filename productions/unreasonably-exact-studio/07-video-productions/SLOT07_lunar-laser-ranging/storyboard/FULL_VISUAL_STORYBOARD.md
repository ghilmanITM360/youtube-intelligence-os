# Full visual storyboard: Slot 07, Lunar Laser Ranging

**Text storyboard, no art yet.** Generated from `narration/NARRATION_TO_VISUAL_MAP.csv`, `NARRATION_BEAT_MAP.csv`, `tools/storyboard_data.py` and `MASTER_ASSET_MANIFEST.csv`. Times are from the approved recording (92.53 s). Phrase edges are measured (+-0.02 s); word anchors are estimates (+-0.12 s). Vertical 9:16, 1080x1920 final. **Nothing here has been watched or listened to by a human**, and there is no animatic yet (G2).

## Rules that apply to every shot

- **Colour grammar:** outbound light warm, return light cool, for the whole film. Earth is at the bottom and the Moon at the top of every schematic frame.
- **Model classes** (from the beat map): actual object, simplified scientific illustration, time-compressed, magnified, non-scale diagram, artistic, educational symbol. Light and photons are never drawn as real visible objects.
- **Reveal order:** the reflector hardware first appears at B17; B05 shows only a ring on the Moon.
- **No on-screen text** except symbols and numbers from the claims ledger; words appear only if the voice is ever muted.
- **Caption band** at the bottom: exact numbers fixed at G5 (playbook section 13). Key subjects stay out of it.
- **Observatory** is a generic, labelled illustration (never captioned "Apache Point"). **Astronaut** is not named on screen (source only a snippet).

## Owner decisions (all settled 2026-11-26; none blocks research or production planning)

1. ~~Voice~~ **DECIDED: the generated narration is the production timing reference; the original WAV is preserved.** The human listening check (G1) stays mandatory before publication and is NOT PERFORMED.
2. ~~C06 "tiny fraction"~~ **DECIDED: keep the recorded line.** The footprint inset at B20 is mandatory (picture rule, ledger C06).
3. ~~B29b~~ **DECIDED: keep it, because it is in the recording** ("And somehow those incredibly faint returns let them measure the distance", 68.56 to 72.65 s).
4. ~~Non-scale schematic~~ **DECIDED: a clearly identified not-to-scale Earth-Moon schematic is allowed where necessary** (true spacing is about 30 Earth diameters); disclose it once on screen or in the caption plan.

## Scenes

| Scene | Beats | Start | End | Length | Story job |
|---|---|---|---|---|---|
| S01 The question | B01 to B04 | 0.00 | 8.04 | 8.0 s | Ground view: a laser is aimed at the Moon to ask it a question. |
| S02 The stopwatch | B05 to B11 | 8.04 | 25.62 | 17.6 s | Schematic: the target, then the timed round trip, then each leg. |
| S03 The distance moves | B12 to B13 | 26.46 | 29.82 | 3.4 s | Top-down orbit view: distance changes, so the time changes. |
| S04 Why would light come back? | B14 to B16 | 31.06 | 36.08 | 5.0 s | Stop, then a bare surface that would not return light, then the imagined mirror. |
| S05 The reveal | B17 to B18 | 37.21 | 41.93 | 4.7 s | Lunar surface: the reflector is real and astronauts placed it. |
| S06 The corner trick | B19 to B21 | 42.71 | 48.53 | 5.8 s | Real array to optical cross-section: why light returns toward its source. |
| S07 The return | B22 to B25 | 49.58 | 57.56 | 8.0 s | Back at the telescope: it looks for the return; almost none arrives. |
| S08 A few photons | B26 to B30 | 58.69 | 74.05 | 15.4 s | Statistics: few photons per pulse, many pulses, a peak, a precise measurement. |
| S09 The formula | B31 to B36 | 75.29 | 85.00 | 9.7 s | The round-trip path becomes a one-way distance. |
| S10 The Moon moves | B37 to B39 | 86.31 | 92.15 | 5.8 s | Closing pull-back; each faint return is a measurement. |

---

## S01: The question (Ground view: a laser is aimed at the Moon to ask it a question.)

### B01  0.00 to 2.77 s  (hook, artistic)

> Imagine pointing a powerful laser at the moon.

| | |
|---|---|
| Frame (9:16) | Observatory (dome, slit opening) lower-centre; Moon high in the upper third; ridge line across the lower third. |
| Camera | ground-level vertical frame, locked wide, 3% push over the phrase |
| Action | dome slit opens; stars drift with Earth rotation (sidereal rate, barely visible) |
| Anchor | word "laser" at 1.76 s (estimate +-0.12 s) |
| Layers | FG: rock props, antenna mast / MG: dome + telescope slit / BG: Moon, stars, mountain ridge |
| Graphics | none (no text; title card only if G5 wants it) |
| Science state | Moon high in sky (artistic: enlarged); observatory on Earth; geometry here is NOT to scale |
| Sound | night ambience (wind, distant insect/hum), dome motor starts on "laser" |
| Viewer must understand | a laser is about to be aimed at the Moon from Earth |
| Reveal / transition | Moon rises into frame above the dome on "laser" / cold open, no transition |
| Assets | `OBS_001_EXTERIOR` `OBS_002_DOME` `OBS_006_DOME_SLIT` `OBS_004_MOUNTAINS` `OBS_005_NIGHT_SKY` `OBS_007_PROPS` `TEL_001_HOUSING` `TEL_002_MOUNT` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `RIG_002_TELESCOPE_DOME` |

### B02  3.47 to 4.32 s  (misconception, artistic)

> Not to light it up.

| | |
|---|---|
| Frame (9:16) | Same frame held; a dashed floodlight cone rises from the dome toward the Moon, then a crossed-out ring over it. |
| Camera | same frame, hold |
| Action | imagined floodlight beam swells toward the Moon on "light", then dims and gets a crossed-out ring on "up" |
| Anchor | word "light" at 3.87 s (estimate +-0.12 s) |
| Layers | FG: none / MG: dashed imagined beam / BG: Moon |
| Graphics | optional icon: crossed-out lightbulb (no text) |
| Science state | rejected interpretation only (artistic, flagged as imagined: dashed outline, no real beam) |
| Sound | soft "no" tick on "up" |
| Viewer must understand | the point is not to illuminate the Moon |
| Reveal / transition | a lit-up Moon glow appears then is wiped away on "up" / none |
| Assets | `OBS_001_EXTERIOR` `OBS_002_DOME` `OBS_006_DOME_SLIT` `OBS_004_MOUNTAINS` `OBS_005_NIGHT_SKY` `OBS_007_PROPS` `TEL_001_HOUSING` `TEL_002_MOUNT` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `OPT_001_LIGHT_PULSE` `MG_005_LABELS` |

### B03  5.02 to 6.18 s  (setup, artistic)

> To ask it a question.

| | |
|---|---|
| Frame (9:16) | Dome fills the lower two-thirds after the push-in; the telescope inside the slit tips up; a dot-built question mark floats in the upper third. |
| Camera | slow push-in (115%) on the dome, motivated by "ask it" |
| Action | telescope tilts up toward the Moon on "ask"; "?" built from marker dots |
| Anchor | word "a" at 5.60 s (estimate +-0.12 s) |
| Layers | FG: telescope / MG: dome / BG: sky |
| Graphics | "?" mark (code-drawn, one symbol) |
| Science state | experiment = send a signal, wait for the answer |
| Sound | servo whirr as telescope tilts |
| Viewer must understand | the experiment is a question asked with light |
| Reveal / transition | a question mark forms from the pulse-marker dots on "question" / push-in toward the dome slit |
| Assets | `OBS_001_EXTERIOR` `OBS_002_DOME` `OBS_006_DOME_SLIT` `OBS_004_MOUNTAINS` `OBS_005_NIGHT_SKY` `OBS_007_PROPS` `TEL_001_HOUSING` `TEL_002_MOUNT` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `RIG_002_TELESCOPE_DOME` `MG_005_LABELS` |

### B04  7.16 to 8.04 s  (event, educational symbol)

> You fire a pulse

| | |
|---|---|
| Frame (9:16) | Aperture centred in the middle third; flash at its centre; the pulse marker streaks up and leaves the top of the frame. |
| Camera | locked; 2-frame flash then pulse races up and out of frame |
| Action | one short pulse, not a continuous beam; pulse head crisply emitted |
| Anchor | word "pulse" at 7.73 s (estimate +-0.12 s) |
| Layers | FG: pulse marker / MG: aperture flash / BG: sky |
| Graphics | stopwatch hidden until B06 |
| Science state | t=0 s on the stopwatch; pulse marker = educational symbol (light is invisible in vacuum) |
| Sound | sharp laser "thock" (illustrative, flagged as not literal) |
| Viewer must understand | a single short pulse is sent |
| Reveal / transition | single pulse leaves the aperture exactly on "pulse" / cut to Earth-Moon schematic after pulse clears frame |
| Assets | `TEL_001_HOUSING` `TEL_003_APERTURE` `OBS_005_NIGHT_SKY` `OPT_001_LIGHT_PULSE` `RIG_004_CAMERA_MULTIPLANE` |

---

## S02: The stopwatch (Schematic: the target, then the timed round trip, then each leg.)

### B05  8.04 to 10.24 s  (setup, non-scale diagram)

> at a reflector sitting on the lunar surface.

| | |
|---|---|
| Frame (9:16) | Earth limb as an arc across the bottom, Moon in the upper third, pulse crossing the gap on a vertical path; a ring lands on the Moon (ring only, no hardware). |
| Camera | pull back to a space view in which Earth and Moon share one frame |
| Action | pulse crosses the gap and a pulsing ring lands on the Moon near-side (Mare Tranquillitatis region, Apollo 11 site) on "reflector" |
| Anchor | word "reflector" at 8.43 s (estimate +-0.12 s) |
| Layers | FG: pulse / MG: Earth limb bottom, Moon top / BG: star field |
| Graphics | highlight ring + one-word label "reflector" only if the voice is ever muted |
| Science state | schematic: NOT TO SCALE (true spacing is ~30 Earth diameters); pulse position matches t=0 -> on the way |
| Sound | low whoosh (illustrative) then soft target ping |
| Viewer must understand | there is a target on the Moon that the light is aimed at |
| Reveal / transition | ring marks the landing region on the Moon on "reflector" (a ring and dot only, NOT the hardware: the answer comes at B17-B18) / match cut: ground view -> schematic Earth-Moon view (Moon stays on the same screen spot) |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `OPT_001_LIGHT_PULSE` `MG_006_HIGHLIGHT` `RIG_001_GLOBE_LIGHTING` `RIG_004_CAMERA_MULTIPLANE` |

### B06  11.28 to 13.93 s  (question, non-scale diagram)

> Now, how long before that light comes home?

| | |
|---|---|
| Frame (9:16) | Same space frame; stopwatch top-centre inside the safe area; the pulse restarts from Earth. |
| Camera | locked schematic frame, stopwatch top-centre in the safe area |
| Action | stopwatch appears and begins counting; pulse starts outbound again on "light" for the real timing |
| Anchor | word "how" at 11.42 s (estimate +-0.12 s) |
| Layers | FG: stopwatch / MG: pulse / BG: Earth, Moon, stars |
| Graphics | MG_001_STOPWATCH |
| Science state | clock running real time: 0.00 -> 1.28 s (mean one-way) must complete before the Moon is reached |
| Sound | single soft tick per second of the clock (illustrative) |
| Viewer must understand | we are timing how long the light takes to come back |
| Reveal / transition | stopwatch (0.00 s) fades in on "how long" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_007_PATH_ARROWS` `OPT_001_LIGHT_PULSE` `SCI_001_LIGHT_TIME` |

### B07  15.20 to 16.41 s  (reveal, real time (2.56 s inside 3.3 s of speech))

> About two and a half seconds.

| | |
|---|---|
| Frame (9:16) | Stopwatch enlarged in the upper third showing 2.56 s; the pulse arrives back at Earth at the bottom. |
| Camera | locked; slight punch-in (118%) onto the stopwatch on "half" |
| Action | pulse arrives back at Earth as the timer lands on 2.56 s; stopwatch pulses once |
| Anchor | word "seconds." at 16.14 s (estimate +-0.12 s) |
| Layers | FG: stopwatch / MG: pulse / BG: Earth, Moon |
| Graphics | MG_001_STOPWATCH final value |
| Science state | mean round trip 2.564 s = 2 x 384,400 km / c (recomputed); script says "about two and a half" and 2.56 is consistent |
| Sound | stopwatch stop click |
| Viewer must understand | the whole round trip takes about 2.5 s |
| Reveal / transition | stopwatch freezes on 2.56 s on "seconds"; digits show 2.56 / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `OPT_001_LIGHT_PULSE` `SCI_001_LIGHT_TIME` |

### B08  17.45 to 19.34 s  (misconception, non-scale diagram)

> Wait, that's there and back.

| | |
|---|---|
| Frame (9:16) | Vertical path with a two-way arrow along it: warm going up, cool coming down. |
| Camera | locked; gentle pull to include both ends of the path |
| Action | outbound path lights, return path lights in a different tint on "and back" |
| Anchor | word "and" at 18.69 s (estimate +-0.12 s) |
| Layers | FG: direction arrows / MG: path line / BG: Earth, Moon |
| Graphics | two-way arrow, outbound/return colours |
| Science state | colour grammar: outbound = warm, return = cool, both on the same line (consistent for the whole film) |
| Sound | two soft pings (out then back), illustrative |
| Viewer must understand | the 2.5 s includes both directions |
| Reveal / transition | a bold two-way arrow appears over the path on "and" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_007_PATH_ARROWS` `MG_006_HIGHLIGHT` `OPT_001_LIGHT_PULSE` |

### B09  19.82 to 21.12 s  (correction, non-scale diagram)

> Not two and a half seconds each way.

| | |
|---|---|
| Frame (9:16) | Stopwatch with a bracket over the whole trip, a small x on one leg, then the split into halves. |
| Camera | locked |
| Action | stopwatch face shows a bracket spanning the whole trip, then a small "x" on one leg on "not"; the split appears on "each way" |
| Anchor | word "way." at 20.91 s (estimate +-0.12 s) |
| Layers | FG: stopwatch / MG: path / BG: Earth, Moon |
| Graphics | bracket + split marker |
| Science state | one leg = 1.28 s; whole = 2.56 s |
| Sound | none |
| Viewer must understand | it is not 2.5 s in each direction |
| Reveal / transition | the "2.5 s" is split into halves on "each way" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_007_PATH_ARROWS` `SCI_001_LIGHT_TIME` |

### B10  21.83 to 23.61 s  (explain, time-real, non-scale position)

> A little over a second to reach the moon

| | |
|---|---|
| Frame (9:16) | Pulse climbs the path from Earth to the Moon; the leg timer reads 1.28 s on arrival. |
| Camera | locked; outbound leg highlighted |
| Action | pulse travels Earth -> Moon in 1.28 s real time (the speech phrase is 1.78 s, so start on "A") |
| Anchor | word "moon" at 23.48 s (estimate +-0.12 s) |
| Layers | FG: pulse / MG: path / BG: Earth, Moon |
| Graphics | leg timer 1.28 s |
| Science state | real-time clock, 1.28 s one way (mean); leg label "1.28 s" appears at arrival |
| Sound | faint whoosh rising |
| Viewer must understand | the first leg is about 1.3 s |
| Reveal / transition | outbound leg counts 0 -> 1.28 s and the pulse lands on the Moon on "moon" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_007_PATH_ARROWS` `OPT_001_LIGHT_PULSE` `SCI_001_LIGHT_TIME` |

### B11  24.08 to 25.62 s  (explain, time-real, non-scale position)

> and a little over a second to return.

| | |
|---|---|
| Frame (9:16) | Pulse descends in the return colour; the two legs sum on the stopwatch to 2.56 s. |
| Camera | locked; return leg highlighted in the return colour |
| Action | pulse travels Moon -> Earth in 1.28 s; legs sum on the stopwatch |
| Anchor | word "return." at 25.32 s (estimate +-0.12 s) |
| Layers | FG: pulse / MG: path / BG: Earth, Moon |
| Graphics | leg timer; sum 2.56 |
| Science state | two legs of 1.28 s = 2.56 s |
| Sound | whoosh falling, soft arrival ping |
| Viewer must understand | the second leg is the same length |
| Reveal / transition | return leg counts 1.28 -> 2.56 s, pulse reaches Earth on "return" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_007_PATH_ARROWS` `OPT_001_LIGHT_PULSE` `SCI_001_LIGHT_TIME` |

---

## S03: The distance moves (Top-down orbit view: distance changes, so the time changes.)

### B12  26.46 to 28.72 s  (explain, magnified (eccentricity exaggerated))

> And because the moon's distance keeps changing,

| | |
|---|---|
| Frame (9:16) | Top-down orbit view: Earth lower-centre, Moon on an exaggerated ellipse, ruler line between them with a live value. |
| Camera | top-down orbit view; ruler between Earth and Moon |
| Action | Moon moves from perigee to apogee; ruler length updates |
| Anchor | word "keeps" at 28.06 s (estimate +-0.12 s) |
| Layers | FG: ruler / MG: Moon / BG: Earth, stars |
| Graphics | distance ruler with live km value (km shown only if sourced) |
| Science state | range about 357,000 to 407,000 km (C03, NASA); eccentricity exaggerated and disclosed |
| Sound | low pad swell (illustrative) |
| Viewer must understand | the Earth-Moon distance is not constant |
| Reveal / transition | Moon slides along an exaggerated elliptical path on "keeps changing" / wipe to a top-down orbit diagram |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_002_RULER` `SCI_002_ORBIT_GEOMETRY` `RIG_001_GLOBE_LIGHTING` |

### B13  28.72 to 29.82 s  (explain, magnified)

> the timing changes too.

| | |
|---|---|
| Frame (9:16) | Same orbit view; the stopwatch beside the ruler follows the distance (2.38 s near, 2.71 s far). |
| Camera | same orbit view; stopwatch tied to ruler |
| Action | timer readout follows the ruler: shorter distance -> shorter time |
| Anchor | word "too." at 29.58 s (estimate +-0.12 s) |
| Layers | FG: stopwatch / MG: Moon / BG: Earth |
| Graphics | timer driven by state(tm) from the same model as the ruler |
| Science state | round trip 2.38 s at the near extreme, 2.71 s at the far extreme (C04, derived from C03) |
| Sound | none |
| Viewer must understand | distance change changes the time |
| Reveal / transition | timer readout moves 2.38 -> 2.71 s as the Moon moves, on "changes" / return to the main schematic |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_002_RULER` `SCI_001_LIGHT_TIME` `SCI_002_ORBIT_GEOMETRY` |

---

## S04: Why would light come back? (Stop, then a bare surface that would not return light, then the imagined mirror.)

### B14  31.06 to 31.49 s  (pause, artistic)

> But hold on.

| | |
|---|---|
| Frame (9:16) | Everything stops; the Moon slowly grows to fill the centre of the frame; no other element. |
| Camera | all motion stops; Moon slowly fills frame on "on" |
| Action | full stop of pulse and timer; held beat (the 0.9 s pause after "on" is the hold) |
| Anchor | word "hold" at 31.17 s (estimate +-0.12 s) |
| Layers | FG: none / MG: Moon / BG: space |
| Graphics | none |
| Science state | none |
| Sound | music-free silence; low room tone only |
| Viewer must understand | the story pivots to a new question |
| Reveal / transition | everything holds still on "hold" / freeze + fade graphics to black-blue |
| Assets | `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` |

### B15  32.37 to 33.65 s  (question, simplified)

> Why would the light come back at all?

| | |
|---|---|
| Frame (9:16) | Camera pushes down onto grey regolith, horizon in the upper third; the pulse lands and scatter arrows fan out in every direction. |
| Camera | push toward the bare lunar surface |
| Action | light hits dark regolith and is absorbed/scattered in all directions: no return |
| Anchor | word "all?" at 33.49 s (estimate +-0.12 s) |
| Layers | FG: pulse / MG: regolith / BG: lunar horizon |
| Graphics | scatter arrows (code-drawn) |
| Science state | plain regolith scatters light broadly; almost nothing returns toward the source (qualitative, sourced at C06) |
| Sound | dull thud (illustrative) |
| Viewer must understand | a flat surface would not send the light back |
| Reveal / transition | a faint pulse reaches the Moon and does nothing (scatters dark) on "come back" / none |
| Assets | `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `OPT_001_LIGHT_PULSE` `OPT_007_SCATTER` `MOON_002_TERRAIN_SURFACE` `MOON_003_HORIZON` `MOON_005_PROPS` |

### B16  34.56 to 36.08 s  (question, artistic)

> Did someone leave a mirror on the moon?

| | |
|---|---|
| Frame (9:16) | Surface close view; a dashed ghost mirror lies flat in the middle of the frame with a question ring. |
| Camera | lunar surface close view |
| Action | ghost of a flat mirror drawn dashed on the surface (imagined), with a question ring |
| Anchor | word "moon?" at 35.96 s (estimate +-0.12 s) |
| Layers | FG: none / MG: imagined mirror / BG: lunar surface |
| Graphics | dashed outline only |
| Science state | imagined object, drawn dashed so the viewer does not take it as real |
| Sound | faint wind-chime sting (illustrative) |
| Viewer must understand | viewer guesses a mirror |
| Reveal / transition | a mirror silhouette ghost appears and is questioned on "mirror" / none |
| Assets | `MOON_002_TERRAIN_SURFACE` `MOON_003_HORIZON` `MOON_005_PROPS` `MG_005_LABELS` |

---

## S05: The reveal (Lunar surface: the reflector is real and astronauts placed it.)

### B17  37.21 to 38.10 s  (reveal, actual object)

> Actually, yes.

| | |
|---|---|
| Frame (9:16) | The ghost dissolves and the real array appears in the same spot, small push; the answer arrives here and not earlier. |
| Camera | hold, tiny push |
| Action | the real array pops in as the dashed ghost dissolves |
| Anchor | word "yes." at 37.90 s (estimate +-0.12 s) |
| Layers | FG: reflector array / MG: regolith / BG: lunar horizon |
| Graphics | none |
| Science state | real equipment (appearance from Apollo photography, to be researched) |
| Sound | warm sting (illustrative) |
| Viewer must understand | the answer is yes: there is real hardware |
| Reveal / transition | dashed mirror is replaced by the real reflector assembly on "yes" / match cut to the lunar-surface sequence |
| Assets | `MOON_002_TERRAIN_SURFACE` `MOON_003_HORIZON` `MOON_005_PROPS` `RETRO_001_ASSEMBLY` |

### B18  38.65 to 41.93 s  (explain, actual object (illustrated from references))

> Apollo astronauts left special reflectors on the lunar surface.

| | |
|---|---|
| Frame (9:16) | Low wide view: array in the midground, astronaut kneeling beside it left of centre, black sky above, horizon in the upper third. |
| Camera | low lunar-surface view, slow parallax |
| Action | astronaut kneels and aligns the array, then steps back (vacuum motion, no cloth flutter) |
| Anchor | word "special" at 39.90 s (estimate +-0.12 s) |
| Layers | FG: astronaut / MG: array / BG: regolith, horizon, black sky |
| Graphics | none |
| Science state | Apollo 11, 14 and 15 each placed an array (C05); film shows the Apollo 11 site (A7L suit, 100-cube array); naming Aldrin awaits a primary source |
| Sound | suit-contact thuds only as illustrative foley; no air |
| Viewer must understand | humans placed this equipment |
| Reveal / transition | astronaut walks in and sets the array on "left" / none |
| Assets | `MOON_002_TERRAIN_SURFACE` `MOON_003_HORIZON` `MOON_005_PROPS` `RETRO_001_ASSEMBLY` `MOON_006_SITE_DRESSING` `MOON_007_DUST` `ASTRO_010_POSE_SET` `ASTRO_011_SHADOW` `RIG_003_ASTRONAUT_POSE` |

---

## S06: The corner trick (Real array to optical cross-section: why light returns toward its source.)

### B19  42.71 to 44.18 s  (explain, simplified)

> Their corners have a clever trick.

| | |
|---|---|
| Frame (9:16) | Array grid fills the frame, macro push to one cube, then its cross-section appears in the same position. |
| Camera | push-in then a clean side cross-section of one corner cube |
| Action | array zooms to one cube, then a simplified cross-section appears |
| Anchor | word "trick." at 43.96 s (estimate +-0.12 s) |
| Layers | FG: cube / MG: cutaway / BG: neutral |
| Graphics | cross-section labels (no text) |
| Science state | a corner cube has three mutually perpendicular faces (simplified cross-section) |
| Sound | tick-lock sting |
| Viewer must understand | the corner has a special shape |
| Reveal / transition | camera pushes into one corner cube and the housing becomes a cutaway on "trick" / push-in / cutaway transition |
| Assets | `RETRO_002_CUBE_ARRAY` `RETRO_005_CUBE_3FACE` `RETRO_003_CUBE_CUTAWAY` `BG_003_NEUTRAL_CUTAWAY` `RIG_004_CAMERA_MULTIPLANE` |

### B20  44.78 to 46.98 s  (explain, simplified)

> They redirect a tiny fraction of incoming light

| | |
|---|---|
| Frame (9:16) | Cutaway centred on a neutral field; rays enter at several angles and leave parallel to how they came in; a small third-face inset in one corner; on "tiny fraction" a second small inset shows the km-wide beam footprint with the array as a tiny marker (required by the C06 decision). |
| Camera | locked on the cutaway |
| Action | rays at several incoming angles bounce off the faces and exit parallel to how they entered; on "tiny fraction" a small corner inset shows the km-wide beam footprint with the 46 cm array as a tiny marker inside it (C06 picture rule, owner-decided 2026-11-26) |
| Anchor | word "light" at 46.92 s (estimate +-0.12 s) |
| Layers | FG: rays / MG: cube / BG: neutral |
| Graphics | ray animation + footprint inset (OPT_002, magnified, no numbers) |
| Science state | C06 (CLOSED, owner kept the recorded line): the cube returns what enters it exactly back toward the source; the tiny fraction is the part of the km-wide beam the 46 cm array catches. The inset is REQUIRED so the sentence is not heard as a weak reflector. Show the ray returning in full, no absorption |
| Sound | none |
| Viewer must understand | light bounces and comes back parallel |
| Reveal / transition | a ray enters, reflects off the faces, exits on "light" / none |
| Assets | `RETRO_003_CUBE_CUTAWAY` `RETRO_005_CUBE_3FACE` `OPT_004_CORNER_PATHS` `OPT_002_BEAM_SPREAD` `SCI_005_CORNER_CUBE` `BG_003_NEUTRAL_CUTAWAY` |

### B21  46.98 to 48.53 s  (explain, simplified)

> back toward where it came from.

| | |
|---|---|
| Frame (9:16) | Cutaway on the left, ghosted flat mirror on the right (A/B): the mirror deflects the ray away, the cube sends it back. |
| Camera | locked, then widen slightly |
| Action | a ghosted straight mirror deflects light away, the cube sends it back toward the source (A/B contrast) |
| Anchor | word "from." at 48.31 s (estimate +-0.12 s) |
| Layers | FG: rays / MG: cube / BG: neutral |
| Graphics | A/B contrast marker |
| Science state | flat mirror reflects at the angle (away), corner cube reflects back toward source (qualitative) |
| Sound | two short pings |
| Viewer must understand | corner cube returns light to its source, unlike a flat mirror |
| Reveal / transition | exit ray lines up with the entry ray on "from" / none |
| Assets | `RETRO_003_CUBE_CUTAWAY` `OPT_004_CORNER_PATHS` `SCI_005_CORNER_CUBE` `MG_006_HIGHLIGHT` `BG_003_NEUTRAL_CUTAWAY` |

---

## S07: The return (Back at the telescope: it looks for the return; almost none arrives.)

### B22  49.58 to 50.10 s  (transition, artistic)

> Back on Earth,

| | |
|---|---|
| Frame (9:16) | Ground view again: dome and slit in the lower half, a ray arrives from the top of the frame to the telescope. |
| Camera | return to the observatory view |
| Action | the ray exits the cube and the frame cuts to the incoming ray at the telescope |
| Anchor | word "Earth," at 49.86 s (estimate +-0.12 s) |
| Layers | FG: none / MG: dome / BG: night sky |
| Graphics | none |
| Science state | none |
| Sound | ambience returns |
| Viewer must understand | we are back at the observatory |
| Reveal / transition | cut to Earth on "Earth" / hard match cut: reflector ray -> telescope ray |
| Assets | `OBS_001_EXTERIOR` `OBS_002_DOME` `OBS_006_DOME_SLIT` `OBS_004_MOUNTAINS` `OBS_005_NIGHT_SKY` `OBS_007_PROPS` `TEL_001_HOUSING` `TEL_002_MOUNT` `RIG_002_TELESCOPE_DOME` `OPT_001_LIGHT_PULSE` `RIG_004_CAMERA_MULTIPLANE` |

### B23  50.10 to 51.69 s  (explain, simplified)

> a telescope looks for the return.

| | |
|---|---|
| Frame (9:16) | Telescope cutaway: primary mirror in the lower half, the return path to the detector box highlighted by a ring. |
| Camera | cutaway view into the telescope showing the receive path |
| Action | telescope tracks the Moon; the detector box highlights |
| Anchor | word "return." at 51.39 s (estimate +-0.12 s) |
| Layers | FG: telescope / MG: detector / BG: dome interior |
| Graphics | highlight ring |
| Science state | detector is where returned photons are counted |
| Sound | quiet electronics hum |
| Viewer must understand | the same telescope looks for the return |
| Reveal / transition | telescope aims at the Moon and a detector lights on "return" / none |
| Assets | `OBS_003_INTERIOR` `TEL_001_HOUSING` `TEL_002_MOUNT` `TEL_004_PRIMARY_CUTAWAY` `TEL_005_DETECTOR_BOX` `MG_006_HIGHLIGHT` `OPT_001_LIGHT_PULSE` |

### B24  53.10 to 54.17 s  (setup, artistic)

> And here's the really strange part.

| | |
|---|---|
| Frame (9:16) | Aperture again, slow push-in, the background dimming toward black. |
| Camera | slow push-in on the aperture |
| Action | background dims |
| Anchor | word "part." at 53.99 s (estimate +-0.12 s) |
| Layers | FG: none / MG: aperture / BG: dome |
| Graphics | none |
| Science state | none |
| Sound | low drone swell (illustrative) |
| Viewer must understand | something surprising is coming |
| Reveal / transition | light dims on "strange" / none |
| Assets | `TEL_003_APERTURE` `OBS_003_INTERIOR` |

### B25  55.05 to 57.56 s  (explain, non-scale, magnified spread)

> Almost none of the light makes it back to the detector.

| | |
|---|---|
| Frame (9:16) | Wide vertical schematic: outbound cone widens from Earth with the array disc inside it at the Moon; the return cone widens again to a tiny telescope disc at Earth. |
| Camera | wide schematic of the whole path (Earth, Moon, both footprints) |
| Action | two cones: the outbound beam spreads wide, the array is a tiny disc inside it, the return cone spreads again and the telescope is a tiny disc inside that |
| Anchor | word "light" at 55.92 s (estimate +-0.12 s) |
| Layers | FG: cones / MG: array disc / BG: Earth, Moon |
| Graphics | two cone markers, no text |
| Science state | two-leg geometric loss; the return fraction is extremely small (C07: about 1 in 25 million photons even finds the array; show cones, no numbers) |
| Sound | none |
| Viewer must understand | only a tiny part of the light gets back |
| Reveal / transition | beam footprint widens on its way to the Moon and again on the way back; return glow shrinks on "none" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `OPT_002_BEAM_SPREAD` `OPT_001_LIGHT_PULSE` |

---

## S08: A few photons (Statistics: few photons per pulse, many pulses, a peak, a precise measurement.)

### B26  58.69 to 61.65 s  (explain, educational symbol)

> Scientists have to collect just a few returning photons

| | |
|---|---|
| Frame (9:16) | Dark field with a thin time axis across the middle third; a few dots land on it. |
| Camera | detector close-up |
| Action | sparse detection dots land on a time axis |
| Anchor | word "photons" at 61.29 s (estimate +-0.12 s) |
| Layers | FG: markers / MG: axis / BG: dark |
| Graphics | timeline axis |
| Science state | educational markers (photons are not visible objects) |
| Sound | quiet clicks (illustrative) |
| Viewer must understand | a few photons are caught |
| Reveal / transition | single detector click marks appear on "photons" / none |
| Assets | `OPT_003_PHOTON_MARKER` `MG_004_HIST` `BG_002_DARK_FIELD` |

### B27  61.65 to 63.04 s  (explain, time-compressed)

> from many laser pulses.

| | |
|---|---|
| Frame (9:16) | Same axis, wider; dots pile up pulse after pulse and a histogram peak grows; pulse counter in one corner. |
| Camera | same plot, wider |
| Action | many pulses repeat; each adds its few dots to the same time axis and a peak emerges |
| Anchor | word "pulses." at 62.60 s (estimate +-0.12 s) |
| Layers | FG: histogram / MG: counter / BG: dark |
| Graphics | histogram, pulse counter |
| Science state | statistics: random background plus a stable peak (qualitative; counts illustrative, labelled) |
| Sound | clicks accelerating then settling |
| Viewer must understand | a signal emerges only after many pulses |
| Reveal / transition | pulse counter ticks up and dots stack into a histogram on "pulses" / none |
| Assets | `MG_004_HIST` `OPT_006_ACCUM` `OPT_003_PHOTON_MARKER` `BG_002_DARK_FIELD` `SCI_003_STATS` |

### B28  63.71 to 64.72 s  (emphasis, educational symbol)

> A few photons.

| | |
|---|---|
| Frame (9:16) | Three dots centred, each with a soft ring; everything else dark. |
| Camera | push into three dots |
| Action | only three dots, held, each with a soft ring |
| Anchor | word "few" at 64.02 s (estimate +-0.12 s) |
| Layers | FG: dots / MG: none / BG: dark |
| Graphics | none |
| Science state | illustrative count (not a data claim) |
| Sound | three clear clicks |
| Viewer must understand | it really is only a few |
| Reveal / transition | three individual dots light and hold on "few photons" / none |
| Assets | `OPT_003_PHOTON_MARKER` `BG_002_DARK_FIELD` |

### B29  65.52 to 67.68 s  (explain, magnified)

> They even account for the effects of Earth's atmosphere.

| | |
|---|---|
| Frame (9:16) | Side view: the beam passes a wavy band of air above the Earth limb at the bottom; the footprint wobbles. |
| Camera | side view of the beam through the atmosphere |
| Action | the beam passes a turbulent layer, the footprint wobbles and the arrival time is a little uncertain |
| Anchor | word "atmosphere." at 67.21 s (estimate +-0.12 s) |
| Layers | FG: beam / MG: atmosphere / BG: Earth limb |
| Graphics | wavy distortion marker |
| Science state | air bends and delays light slightly; scientists correct for it (sourced at C09) |
| Sound | low airy texture |
| Viewer must understand | air slightly affects the signal and is corrected for |
| Reveal / transition | atmosphere layer blurs/bends the beam on "atmosphere" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_003_ATMOSPHERE` `EARTH_006_ATMOS_SLICE` `OPT_005_ATMOS_DISTORT` `OPT_001_LIGHT_PULSE` `BG_001_SPACE` |

### B29b  68.56 to 72.65 s  (explain, time-compressed)

> And somehow those incredibly faint returns let them measure the distance

| | |
|---|---|
| Frame (9:16) | Histogram in the middle third; the peak sharpens. |
| Camera | locked on the histogram |
| Action | peak sharpens as measurements accumulate |
| Anchor | word "returns" at 70.59 s (estimate +-0.12 s) |
| Layers | FG: histogram / MG: none / BG: dark |
| Graphics | peak marker |
| Science state | the peak position = round-trip time |
| Sound | soft lock tone |
| Viewer must understand | the faint returns still give a measurement |
| Reveal / transition | dots on the histogram resolve into one clean peak on "returns" / none |
| Assets | `MG_004_HIST` `SCI_003_STATS` `BG_002_DARK_FIELD` |

### B30  72.65 to 74.05 s  (payoff, time-compressed)

> with remarkable precision.

| | |
|---|---|
| Frame (9:16) | Tight on the peak; an error bar shrinks around it. |
| Camera | tight on the peak |
| Action | error bar shrinks as repeats accumulate |
| Anchor | word "precision." at 73.53 s (estimate +-0.12 s) |
| Layers | FG: peak / MG: error bar / BG: dark |
| Graphics | error bar |
| Science state | about 1 mm of distance = 6.7 ps of round-trip time (derived 2d/c); mm-level precision sourced at C10 |
| Sound | soft chime |
| Viewer must understand | the result is very precise |
| Reveal / transition | precision readout appears on "precision" (number only after C10 is sourced) / none |
| Assets | `MG_004_HIST` `MG_005_LABELS` `SCI_003_STATS` `SCI_001_LIGHT_TIME` `BG_002_DARK_FIELD` |

---

## S09: The formula (The round-trip path becomes a one-way distance.)

### B31  75.29 to 75.93 s  (transition, non-scale diagram)

> So how does it work?

| | |
|---|---|
| Frame (9:16) | Details fade; only the Earth-Moon path line remains (Earth bottom, Moon top). |
| Camera | plain schematic view |
| Action | details fade, the path remains |
| Anchor | word "work?" at 75.86 s (estimate +-0.12 s) |
| Layers | FG: none / MG: path / BG: space |
| Graphics | none |
| Science state | none |
| Sound | none |
| Viewer must understand | the explanation is about to simplify |
| Reveal / transition | everything simplifies to the plain Earth-Moon line on "work" / clean wipe to the model view |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_007_PATH_ARROWS` |

### B32  77.06 to 78.15 s  (explain, non-scale diagram)

> A cosmic stopwatch.

| | |
|---|---|
| Frame (9:16) | Stopwatch drops in at the top; the pulse makes the trip once more. |
| Camera | locked |
| Action | stopwatch drops in, pulse makes the trip once more |
| Anchor | word "stopwatch." at 77.78 s (estimate +-0.12 s) |
| Layers | FG: stopwatch / MG: pulse / BG: path |
| Graphics | none |
| Science state | real-time trip 2.56 s |
| Sound | tick |
| Viewer must understand | the clock measures the light journey |
| Reveal / transition | stopwatch shown with a cosmic backdrop on "stopwatch" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_007_PATH_ARROWS` `OPT_001_LIGHT_PULSE` `SCI_001_LIGHT_TIME` |

### B33  79.00 to 80.06 s  (explain, non-scale diagram)

> Take the round trip time,

| | |
|---|---|
| Frame (9:16) | The whole path is bracketed; the stopwatch value turns into the symbol t. |
| Camera | locked |
| Action | the full path is bracketed; the stopwatch value becomes the symbol t |
| Anchor | word "time," at 79.76 s (estimate +-0.12 s) |
| Layers | FG: bracket / MG: path / BG: space |
| Graphics | t symbol |
| Science state | formula step 1: t = round-trip time |
| Sound | soft tick |
| Viewer must understand | step one is the round-trip time |
| Reveal / transition | round-trip bracket labelled "t" on "time" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_001_STOPWATCH` `MG_003_FORMULA` `MG_007_PATH_ARROWS` `SCI_001_LIGHT_TIME` |

### B34  80.64 to 81.95 s  (explain, non-scale diagram)

> multiply it by the speed of light,

| | |
|---|---|
| Frame (9:16) | A bar as long as the whole path appears; the t bracket is multiplied by c. |
| Camera | locked |
| Action | the t bracket is multiplied by c; a long bar shows the round-trip path length |
| Anchor | word "light," at 81.85 s (estimate +-0.12 s) |
| Layers | FG: bar / MG: formula / BG: space |
| Graphics | c x t |
| Science state | formula step 2: L = c x t (total path, both legs) |
| Sound | rising sweep |
| Viewer must understand | multiplying by the speed of light turns time into total path length |
| Reveal / transition | c x t builds and the full path length bar appears on "light" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_003_FORMULA` `MG_002_RULER` `MG_007_PATH_ARROWS` `SCI_001_LIGHT_TIME` |

### B35  82.60 to 83.32 s  (explain, non-scale diagram)

> then divide by two.

| | |
|---|---|
| Frame (9:16) | The bar folds at the Moon: out-and-back becomes one leg. |
| Camera | locked |
| Action | the bar visibly folds at the Moon: out-and-back becomes one leg |
| Anchor | word "two." at 83.13 s (estimate +-0.12 s) |
| Layers | FG: bar / MG: fold / BG: space |
| Graphics | /2 |
| Science state | formula step 3: d = c x t / 2 (outbound only) |
| Sound | fold click |
| Viewer must understand | dividing by two gives just the one-way distance |
| Reveal / transition | path folds in half on "two": the bar halves, one leg remains / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_003_FORMULA` `MG_002_RULER` `MG_007_PATH_ARROWS` `SCI_001_LIGHT_TIME` |

### B36  84.32 to 85.00 s  (payoff, non-scale diagram)

> That's your distance.

| | |
|---|---|
| Frame (9:16) | The ruler between Earth and Moon fills; the distance readout appears. |
| Camera | locked |
| Action | ruler between Earth and Moon fills with the resulting distance |
| Anchor | word "distance." at 84.60 s (estimate +-0.12 s) |
| Layers | FG: ruler / MG: value / BG: Earth, Moon |
| Graphics | distance readout |
| Science state | d = c x 2.564 s / 2 = 384,400 km at the mean (derived; matches the sourced mean once C03 is verified) |
| Sound | soft chime |
| Viewer must understand | the distance is the answer |
| Reveal / transition | distance value appears on "distance" / none |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_003_FORMULA` `MG_002_RULER` `SCI_001_LIGHT_TIME` `SCI_002_ORBIT_GEOMETRY` |

---

## S10: The Moon moves (Closing pull-back; each faint return is a measurement.)

### B37  86.31 to 88.45 s  (closing, non-scale diagram)

> The moon isn't just hanging in the sky.

| | |
|---|---|
| Frame (9:16) | Long pull-back: Earth at the bottom with night lights on its dark side, Moon in the upper third drifting slowly. |
| Camera | long slow pullback to a wide space view |
| Action | Moon drifts slowly; gentle parallax between Earth and Moon |
| Anchor | word "in" at 87.74 s (estimate +-0.12 s) |
| Layers | FG: none / MG: Moon / BG: Earth, stars |
| Graphics | none |
| Science state | the Moon moves; geometry kept consistent with the declared model |
| Sound | no sound design beyond a soft pad (illustrative) |
| Viewer must understand | the Moon is a moving object we can track |
| Reveal / transition | camera pulls back to a wide shot as the Moon is shown in space on "hanging" / slow pullback |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `EARTH_004_NIGHT_LIGHTS` `SCI_002_ORBIT_GEOMETRY` `RIG_001_GLOBE_LIGHTING` `RIG_004_CAMERA_MULTIPLANE` |

### B38  89.29 to 90.31 s  (closing, educational symbol)

> With each faint return,

| | |
|---|---|
| Frame (9:16) | One small, dim pulse arrives at the Earth limb; very restrained. |
| Camera | locked |
| Action | a single faint pulse arrives at Earth |
| Anchor | word "return," at 90.00 s (estimate +-0.12 s) |
| Layers | FG: pulse / MG: none / BG: Earth |
| Graphics | none |
| Science state | a faint return (small, dim) |
| Sound | single soft ping |
| Viewer must understand | each tiny return is a measurement |
| Reveal / transition | one last faint return arrives on "return" / none |
| Assets | `OPT_001_LIGHT_PULSE` `OPT_003_PHOTON_MARKER` `EARTH_001_SURFACE` `EARTH_003_ATMOSPHERE` `BG_001_SPACE` |

### B39  90.31 to 92.15 s  (closing, non-scale diagram)

> we can measure where it is.

| | |
|---|---|
| Frame (9:16) | Ruler settles at the measured distance; the Moon holds still; the room tone fades out. |
| Camera | locked |
| Action | ruler settles at the measured distance and the Moon holds |
| Anchor | word "is." at 91.99 s (estimate +-0.12 s) |
| Layers | FG: ruler / MG: Moon / BG: Earth |
| Graphics | readout |
| Science state | final distance state |
| Sound | final soft chime then 1.5 s room tone |
| Viewer must understand | the distance can be measured |
| Reveal / transition | ruler value settles on "is" / fade to end card |
| Assets | `EARTH_001_SURFACE` `EARTH_002_CLOUDS` `EARTH_003_ATMOSPHERE` `EARTH_005_TERMINATOR` `MOON_001_GLOBE` `MOON_004_GLOBE_SHADE` `BG_001_SPACE` `SCI_004_SCALES` `MG_002_RULER` `SCI_001_LIGHT_TIME` `SCI_002_ORBIT_GEOMETRY` |

---

## Not in this storyboard on purpose

- **Control-room workstations, rear/walking/top astronaut views, reflector top view:** the brief lists them, but no beat shows them. Add them only if a beat changes (the manifest has no row for them).
- **Apollo 14 and 15 arrays:** the narration says "Apollo astronauts left special reflectors" and C05 is sourced for all three, but the film shows the Apollo 11 site only.
- **Sound design cue sheet** and **captions**: later phases; the sound column above is the draft.
