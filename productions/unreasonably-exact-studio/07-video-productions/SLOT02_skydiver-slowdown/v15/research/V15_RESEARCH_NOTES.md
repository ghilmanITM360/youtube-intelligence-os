# V15 research notes

What I checked before changing the film, and what it changed.

## Sources read

| Source | What it says (paraphrased) | Used for |
|---|---|---|
| [NASA Glenn: Drag Equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-equation/) | Drag = Cd × ½ρV² × A. It grows with air density, with speed squared, and with the drag coefficient and reference area. Cd is found experimentally, for example in a wind tunnel. | The model (`tools/model.py`) already uses this form. V15 drives cloth and airflow intensity from drag/weight = ½ρv²·CdA/(mg), so the picture reacts to **density and speed together**, not speed alone. |
| [NASA Glenn: Drag Coefficient](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/drag-coefficient/) | Cd folds shape and inclination into one number. | Fixed posture = fixed CdA. The small limb motions in V15 stay within a few degrees (knees ±2.6°, wrists ±4°), so they do not imply a posture change. The end card still says that changing posture changes the outcome. |
| [USPA: Foundations of Flight, Neutral Body Position](https://www.uspa.org/foundations-of-flight-neutral-body-position) | Belly-to-earth neutral: hips forward and down, arch from the hips, hands in front of and about level with the shoulders, elbows slightly below the shoulders, knees about shoulder-width apart, lower legs a little past 90°, toes pointed, "strong but relaxed". | The Codex side pose already matches this. V15 animates around it: relaxed oscillation of the lower legs and hands, not a stiff hold. |
| [USPA Learning FAQ](http://www.uspa.org/discover/faqs/learning) | Typical freefall speed is about 120 mph. Freefall lasts 30–60 s. | Sanity check: the model's peak of 81 m/s (≈181 mph) comes from its 10 km start in thin air. That is why the film keeps saying "a model", and the assumptions line stays. |
| [USPA SIM Category A](https://uspa.org/skydiveschool/A) | Students practise the basic arch, then a neutral position. | Same as above. |
| Earlier saved references in `research/screens/` (NASA falling-object FBD, Physics Classroom skydiver diagrams, ticker-tape diagrams) | Free-body arrows drawn from the centre of mass. Equal-time position marks show changing speed. | Kept the centre-of-mass arrows and the equal-time trail. |

## Freefall footage

I did **not** watch real skydiving video in a browser for this version.

- I could not review moving footage in real time with sound.
- Frame grabs from copyrighted footage cannot go into the deliverable anyway.

What I relied on instead: the USPA position description above and the existing Codex artwork, which was drawn to that brief. What reference footage typically shows (fabric flutter on sleeves and trouser legs, small hand and lower-leg trims, a still head) is general knowledge. It is not a citation.

## Motion-design tools reviewed

| Tool | What it actually is | Decision |
|---|---|---|
| HyperFrames (+ animation / keyframes / audio skills, installed in `~/.claude/skills/`) | HTML/GSAP compositions rendered to video, with an audio layer that has a "voiceover carve" (cuts the speech band of a bed under the voice) | **Used the technique, not the renderer.** V15's mix applies a speech-band carve (1–4.5 kHz, −6 dB extra under speech) in `tools/mix_v15.py`, following the HyperFrames audio guidance that voice/bed fights live in 1–3 kHz. Porting a 25-shot cairo film to HTML would have replaced a reliable, reproducible pipeline for no gain. |
| Motion graphics / general-video skills | HyperFrames workflows | Not used; same reason. |
| HumanCraft guides (`~/Downloads/HumanCraft_*`) | Written guidance on layer-based animation and parallax | Principles applied: mesh deformation instead of cut-out joints, secondary motion, depth layers moving at different rates. |
| Anidoodle (`~/GhilmanProjects/testingsvideos/vendor/anidoodle`, Apache-2.0) | Code-drawn, hand-drawn-style illustration and film engine (32 styles) | **Not used.** Its look would replace the approved Codex character and painted environment. The brief requires preserving the established visual identity. |
| Claude Animated Shorts, EffectCraft, Three.js Skills, Hand-Drawn Explainer, FFmpeg Skill | Not found on this machine (searched `~` to depth 4 and the skills folder) | Not evaluated beyond their absence. FFmpeg itself is used directly for encoding, loudness and QA. |
