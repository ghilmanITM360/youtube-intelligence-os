# Scientific comprehension QA: ROUGH_CUT_V2 (2026-11-26)

**Method and limits.** I checked each concept against the brief's structure: show the object, then what happens, then why, then the result. Evidence is code, the claims ledger and V2 stills. These are my own reading of the pictures, **not a viewer test**. No child, teenager or adult has watched V2, so whether people of every age understand it is **not verified**. The muted-viewer protocol below is ready to run.

## Concept by concept

### Laser aimed at the Moon (0–7.6 s)

- **Object:** The observatory, its telescope and the Moon are all in frame from frame 0.
- **What happens:** The shutter opens and the telescope swings up.
- **Why:** On "Not to light it up", a floodlight cone appears, gets a NO mark and collapses (the wrong idea is shown and rejected). On "question", brackets lock onto the Moon.
- **Result:** We are asking the Moon a question.
- **Verdict:** OK. The NO mark reads as "not this" without words.

### One pulse, real time (7.6–11.4 s)

- **Object:** A single dot, labelled "pulse drawn as a dot · real time".
- **What happens:** It takes 1.28 s to reach the Moon.
- **Why:** Light takes time to cross the distance.
- **Result:** It lands as the narrator says "reflector", and the camera pushes in to the Apollo 11 site.
- **Verdict:** OK.

### Round trip (11.8–25.5 s)

- **Object:** The stopwatch, plus out and back lanes in two colours.
- **What happens:** The stopwatch runs to 2.56 s. The legs separate into 1.28 s + 1.28 s.
- **Why:** "There and back."
- **Result:** "A little over a second each way."
- **Verdict:** OK. The outward (warm) and return (cool) journeys are distinct.

### Changing distance (26.2–30.6 s)

- **Object:** The Moon on a to-scale schematic.
- **What happens:** It moves between 357,000 and 407,000 km while the stopwatch range follows (2.38–2.72 s).
- **Why:** A longer path takes more time.
- **Result:** "The timing changes too."
- **Verdict:** OK. A longer journey is shown as more time on the same stopwatch.

### Why would light come back? (31–40 s)

- **What happens:** Light scatters off bare ground in every direction.
- **Why:** "Did someone leave a mirror?" An imagined dashed mirror appears with a "?".
- **Result:** "Actually, yes." The real array replaces the imagined mirror.
- **Verdict:** Weak spot. The dashed box at 39 s is generic. It is on screen for only 0.3 s, and is flagged for V3.

### Retroreflector (40–51 s)

- **Object:** An astronaut sets down an Apollo-style 10×10 array.
- **What happens:** The camera pushes into one corner cube, then the cutaway shows a ray entering and leaving parallel.
- **Why:** Three perpendicular faces send light back the way it came.
- **Result:** "Back toward where it came from."
- **Verdict:** OK. The behaviour is shown qualitatively (return to source), as the brief asks. The V2 fix removes the pixelated frames that broke the push.

### Weak return (51–60 s)

- **What happens:** The return dot comes home in real time, landing on "return". The returning cone is drawn far wider than the telescope ("widths not to scale").
- **Result:** "Almost none of the light makes it back."
- **Verdict:** OK.

### Few photons, many pulses (60.6–67.5 s)

- **Object:** A sparse raster with one row per pulse; most rows stay empty.
- **What happens:** On "A few photons", three dots light up one by one (new in V2; V1 showed the histogram at this moment).
- **Verdict:** Improved. The big empty field around the dots is still large on a phone.

### Atmosphere (67.5–71 s), new in V2

- **Object:** The air layer, labelled "air".
- **What happens:** The real pulse (warm dot) slows while crossing the air. A hollow "no air" twin does not slow.
- **Why:** The air delays the light.
- **Result:** It arrives late, shown as a "delay" bracket. Just after "atmosphere", the late tick slides back and is marked "corrected".
- **Verdict:** Matches claim C09's rule (a delay and a correction tick, no number). The slowdown is labelled "hugely exaggerated" (the real effect is ~1.5–2 m of path).
- **Risk:** A young viewer may not connect "corrected" with "scientists account for it". The narration says it at the same moment.

### Repeated measurements (60–75 s)

- **What happens:** The histogram peak emerges from flat noise as pulses accumulate. It pops on "returns" (B29b).
- **Verdict:** OK. The emerging peak builds the result gradually.

### Precision (75–78 s)

- **What happens:** A caliper closes to "about 1 millimetre", shown against "in about 384,000 km".
- **Verdict:** OK (claim C10).

### Divide by two (80–88 s)

- **What happens:** The stopwatch sweeps to 2.56 s. The formula d = c × t / 2 is built term by term. On "divide by two", the path bar folds in half.
- **Verdict:** OK. The total round trip is visibly split into equal one-way halves.

### Final composition (88–96 s)

- **What happens:** Pull back to the orbit. Each faint return drops a measured point. The opening reticle locks on the Moon again.
- **Verdict:** OK for meaning. The composition is small and empty (flagged for V3).

## Science checks run in code

**Gap scenes** (`gaps.check_all`): 6/6 pass.

| Check | Result |
|---|---|
| G12 distance range | 357,000–407,000 km |
| G12 stopwatch range | 2.382–2.715 s |
| G12 Moon wobble | to scale |
| G22 return pulse | real time |
| G30 text on screen | text check |
| G29 order | the pulse through air arrives after the twin, and the correction lands after "atmosphere" |

**Proof checks** were unchanged by V2, apart from the P13 dissolve timing and the obs_rig blend. They are re-run in `FINAL_PRODUCTION_QA.md`.

## Muted-viewer protocol (to run with real people; not run)

1. Show `ROUGH_CUT_V2_PREMIUM.mp4` muted, with no captions, to at least three viewers aged about 10, about 15 and an adult.
2. Ask:
   - (a) What is being sent to the Moon?
   - (b) Does it come back, and why?
   - (c) Why is the time divided by two?
   - (d) What does the air do?
3. Record their words verbatim in `qa/MUTED_VIEWER_TEST.md`. A concept passes if 2 of 3 viewers state it.
