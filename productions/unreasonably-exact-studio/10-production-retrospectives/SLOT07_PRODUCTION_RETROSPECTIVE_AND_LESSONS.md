# Slot 07 production retrospective and lessons

**Film:** *How Long Does a Laser Take to Reach the Moon and Back?*, V3. The owner selected it as the final version and accepted its visual quality on 2026-11-26.
**Compared with:** Slot 02 *Why Can a Skydiver Slow Down Without a Parachute?*, V15. The owner approved it as the production master on 2026-11-25.
**Written:** 2026-11-26 by Claude, from the files on disk.

**Paths and tags.** `S07/` means `07-video-productions/SLOT07_lunar-laser-ranging/`. `S02/` means `07-video-productions/SLOT02_skydiver-slowdown/v15/`. The Slot 02 history is in the master playbook (§3, §4, §18), which audited it on 2026-11-25. Claims are tagged:
- **[V]**: verified in a file;
- **[M]**: measured in that production;
- **[I]**: inferred, with the reasoning given;
- **[E]**: an estimate.

---

## 1. Summary

1. **Slot 07 took three cut versions; Slot 02 took fifteen.** Slot 07 went from narration to the owner-selected V3 in one calendar day (2026-11-26) [V: file times]. Slot 02 needed V1–V7 earlier, and V8–V15 in one day [V: playbook §4.1].
2. **The difference came mostly from process, not talent or tools.** Both films used the same kind of renderer (custom Python, design units, pure functions of time). What changed in Slot 07:
   - real references were collected before any art was made;
   - Codex was driven from the CLI with one deliverable per run, editing a master;
   - Claude measured every asset;
   - each mechanism was built as a moving proof before the cut.
3. **The early Slot 07 art still failed the way Slot 02's art did.** Four multi-asset batches produced 0 approved images. The process was fixed the same day (root causes R1–R10). After that, 13 of 16 runs were usable.
4. **Owner-driven revision rounds fell** from many in Slot 02 (nine screenshots at V10, an opening complaint at V12, an audio complaint at V14) to **one** in Slot 07: six screenshot defects between V2 and V3.
5. **Not proven:** nobody has listened to either film's final mix as a recorded check, and neither film has been published. So nothing here is evidence about audience retention.

## 2. Production efficiency

| Measure | Slot 02 Skydiver (V15) | Slot 07 Lunar laser (V3) |
|---|---|---|
| Film | 110.04 s, 24 fps, 2,641 frames, 25 shots [V] | 96.000 s, 30 fps, 2,880 frames, 17 segments [V] |
| Versions to final | 15 (V1–V7 earlier; V8–V15 on 2026-11-25, about one per hour [I]) | 3 cut versions (V1 12:20, V2 13:17, V3 14:51 on 2026-11-26 [V: folder times]) after 13 proofs (P01–P13) and 3 opening treatments |
| Owner revision rounds recorded | V10 (9 screenshots), V12 (opening), V14 (audio), plus several un-recorded reviews [V/I] | 1 (V2 → V3, 6 screenshot defects D01–D06) [V] |
| Late narration change | Yes: 78.2 s → Hamza's 110 s take at V14, needing a 0.26–1.40× warp [V] | Yes, but early: the V2 take (10:39) arrived **before** the cut, and proofs were re-timed by word-edge warp [V] |
| Architecture changes forced by art | 4 (limb rigs → whole poses → constrained side rig → continuous drawing + mesh warp) [V] | 0 to the renderer. One rig change: shoulder skinning v2 instead of new art [V] |
| Final render | full film, single command (`tools/build_v15.sh`) [V] | ~13 min full render plus 2 frame-accurate patches (75.0–78.2 s, 81.6–88.1 s) [V] |

**Why Slot 07 was cheaper:**
- **Reuse of the system.** The engine (`uemotion`), the gates and the caption and sound methods came from the Slot 02 lessons in the playbook.
- **Proof-first construction.** Every scene was built as a proof with its own asserts, then assembled by `roughcut.py`, which keeps each proof's own clocks. A change re-renders one segment, not the film.
- **Narration fixed early.**
- **Fewer, earlier owner decisions.** The owner settled the voice timing, the C06 line and the non-scale schematic at the start (`S07/PROGRESS_LOG.md`, "recovery from the owner audit").

## 3. Number of artwork attempts

| | Slot 02 | Slot 07 |
|---|---|---|
| Multi-asset requests | V9 request (9 families); V10 package (73 layers, 65 integrated); V11 retired 45 limb layers; V12 package "NOT READY TO ANIMATE"; V13 elbow/neck repairs rejected [V: playbook §4.2] | Batches 0, 0b, 1, 2: 27 delivered PNGs, **0 approved** [V: dashboard; root-cause audit] |
| Single-deliverable runs | none recorded | **16 runs**, 1–4 min each: 13 usable, 3 rejected (R2b, B5L2, B5PR2) [V: `S07/codex_handoff/runs/`] |
| Runs whose art is in the final film | the final character is one continuous Codex drawing; the rest is code [V] | 7: B3M terrain; B4L, B4L2 and B4P observatory; B5PA astronaut; B5PR reflector; B1c clouds. Also the batch 0b cube parts and batch 1 cloud tiles, composited by Claude [V] |
| Public-domain data used directly | none | NASA Blue Marble, Black Marble and LROC maps, for Earth and Moon [V] |

## 4. Recurring asset-generation failures (both films)

| Failure | Slot 02 | Slot 07 | Root cause (S07 audit ID) |
|---|---|---|---|
| Views disagree; identity drifts | "different person" face, smiling 3/4, gloves grey vs bare (V10–V13) | retro frame top/side views redrew the hardware | No master; each view generated from text (R2) |
| References ignored | not checked | no image reached the generator in batches 0–2 | Nothing attached or required (R1) |
| Unwanted backgrounds and fringes | RGB under zero alpha (707 px in a V11 layer) | backdrops, soft fringes, RGB under alpha 0 in 8 files | Generated transparency (R7) |
| Several drawings in one image | not recorded | 3/4 and front view side by side | "same as" wording (R4) |
| Wrong numbers | dial at 4 sizes; drag 1.5× weight | tilt 35–39° vs 23° | Unmeasurable numbers in prompts (R5); a wrong brief (R10) |
| Joints and overlap | round joint discs, limbs "bolted on" | near-shoulder gap at P05 | Baked overlap ends; rigid swing about one pivot (R8, R17) |
| Self-report trusted | "candidate/not approved" repeated, then dropped from the docs | Codex marked everything "blocked" and stopped after one try | Nobody re-checked the file (R9) |

The lesson that covers all of these: **the generator is reliable only when it gets one task, an attached master or references, and a measurable test, and when somebody other than the generator runs that test.**

## 5. Successful Codex corrections

| Run | Correction | Result |
|---|---|---|
| R2a | side view of the retroreflector, edited from the 3/4 master against a 23° construction guide | tilt 23.6°, one component; candidate [M] |
| B4L2 | open the dome slit in the building layer, keeping everything else | IoU 0.992 vs the closed layer; used in the film [M] |
| B4P | clean sky and mountain plate from the master (building removed) | top 500 rows differ by 2.98/255; used in the film [M] |
| B5PA / B5PR | split the approved astronaut+reflector composition into two layers, hidden parts painted | restack IoU 0.983; used in the film [M] |
| **Failed: R2b** | one-defect fix of R2a's base | tilt regressed 23.6° → 14.7°. Rejected. This is where the rule "re-measure all earlier passes" came from |
| **Failed: B5PR2** | draw the 10×10 cube grid on the panel | IoU 0.327: the whole object was redrawn. Rejected. Claude composited the 100 approved cube instances in code instead |
| **Failed: B5L2** | small shoulder cap on a full canvas | no alpha 0 anywhere. Rejected. This is where the rule "small parts on tight canvases" came from |

## 6. Rigging improvements

| | Slot 02 | Slot 07 |
|---|---|---|
| Approach that worked | a continuous drawing deformed by a 32 px mesh warp (knees ±2.6°, wrists ±4°, cloth ripple driven by drag/weight) [V] | rigid layered rigs with **Claude-measured** pivots in JSON (RIG_002 observatory; RIG_003 arms; the carry interaction) [V] |
| Path to it | four architecture changes, each forced by failed art | the first rig plan held. One fix (shoulder skinning v2) replaced a commissioned art repair |
| Tests | `cloth_warp.py` checks, `v15.py --check` | P04, P05 and P06 asserts: slit clip, monotonic slew, shoulder gap ≤ 86 px of 15,361, glove-to-bar error 0.000, release after touch-down |

**Why rigid rigs were enough in Slot 07.** The subjects are hard-surface (observatory, telescope, a pressurised suit) and they move little. **Neither approach is universal.** Use mesh deformation for soft bodies and clothing in air. Use rigid layers with measured pivots for hardware and spacesuits. The playbook (§15) adds that cloth flutter must not be used in vacuum.

## 7. Opening hook improvements

| | Slot 02 | Slot 07 |
|---|---|---|
| Problem | V12: the figure was 15–20 px tall at the lower right, the ground filled 55 % of the frame, and a cloud wiped the whole frame (owner at 0:00/0:01/0:03) | V2: static hold 2.6–3.9 s, with 30 of 60 frames at 2–4 s frozen [M] |
| Fix | V13: a four-layer parallax opening, with mid-scale clouds below the subject | V3: an aim line traces from the telescope to the Moon on "at the moon". The camera tilts along it in one continuous move. A charge glow fills the pause. The floodlight cone grows out of the line on "Not to light it up" [V] |
| Check | owner review | a 0–10 s proof rendered **first**. A self-check (no static hold 2–4 s, minimum screen speed 38 u/s) caught a camera rest at 2.19 s that a still would have hidden [M] |

## 8. Scientific storytelling

- **Slot 02:** the net force is only 0.9–3.6 % of weight. It took six designs to settle on one scale from the centre of mass, plus one disclosed ×8 lens.
- **Slot 07** started from a scientific visual design: 13 concepts, each with a muted-viewer test, in `S07/SCIENTIFIC_VISUAL_DESIGN.md`. Its models are code with asserts:
  - the stopwatch is driven only by model time, and reads exactly 2.56 with the turnaround at 1.28 [M];
  - d = c × t / 2 is built from the stopwatch value and the bar labels, and the bar folds exactly on "two." [M];
  - corner-cube exit rays are antiparallel to the entry rays (dot −1.0) [M];
  - the photon rain lets no photon into the telescope except the one detected on "detector" [M].
- **The V2 → V3 lesson (D06):** a translucent triangle *showed* that light spreads, but nothing showed light *missing* the telescope. The V3 rain-and-one-photon design shows the relationship.

## 9. Typography

| | Slot 02 | Slot 07 |
|---|---|---|
| On-screen text | V8 put a two-line headline on every shot. A 39-item text audit (V12) followed; labels are now used only where a mark needs a name | V2 had 8 kinds of pill and about 78 s of badges. V3 has 11 timed sentence-case notes (31.5 s) from one table [M] |
| Faces | caption face in the V15 tools | Comic Neue (OFL) for captions **and** labels. Geometric maths face for the formula (D12: "t" read as "†"). Mono for numbers |
| Open | caption position not tested against the Shorts UI | the same, and the ~12 pt notes have not been checked on a phone |

## 10. Realistic artwork

- **Slot 07's look:** "painterly-clean realistic". Soft painted forms, true silhouettes, one sun from the upper left, no outlines.
- **How it was built:** NASA photographs (Apollo 11/12/15 surface frames, AS11-40-5952 for the retroreflector) and real observatory photos (APO 3.5 m, VLT, WIYN) were attached to every master run.
- **Data instead of generation:** Earth and Moon are NASA maps rendered on a sphere with one film-wide sun, not generated images.
- **Style decision:** the open style question (W38, near-photoreal vs painterly) was settled when the owner accepted the V3 look.
- **Slot 02 contrast:** its environment moved from procedural geometry (the V9 objection: "clean but geometric") to painted landscapes, then farmsteads and tree crowns. The character's identity drifted across views until V15 used one continuous drawing.

## 11. Music and sound design

| | Slot 02 V15 | Slot 07 V3 |
|---|---|---|
| Music | none | Small_Variables.mp3: 134.98 BPM, F major (estimated). Four bars repeated, with the seam at 55.58 s [M] |
| Separation | voice-minus-background median 20.7 dB (from 10.5 dB in V14) [M] | music 21.0 dB under the voice (per-section 19–23 dB) [M] |
| Ducking | ambience −12 dB, effects −9 dB, plus a 1–4.5 kHz −6 dB carve | music −6 dB, plus −4 dB at 1–4 kHz; SFX −8 dB |
| Cues | reveal sounds cut from 11 to 5; generated only | 115 → 51 cues, 14 logged removals, accents retuned to F major |
| Rights | publication mix has generated sound and the owner's recording only. The library clips are in a review mix only | publication candidate = RIGHTS_CLEAR (synthesized only). The music mix is private review until licence evidence exists |
| Loudness | −16 LUFS | −16.4 LUFS, −2.0 dBTP (both mixes) |
| Human listening | not recorded | **NOT PERFORMED** |

## 12. Remaining limitations

1. **No human listening** of either final mix is on record.
2. **The Slot 07 music licence is unverified.**
3. **No muted-viewer, comprehension or Shorts-UI caption test** exists for either film.
4. In Slot 07, two disclosure notes overlap at 13.75–15.2 s ("Not to scale" plus "Slowed down").
5. `S07/MASTER_ASSET_MANIFEST.csv` still shows every asset as PLANNED. The truth is in `ASSET_GENERATION_TRACKER.csv` and the new `11-production-management/REUSABLE_ASSET_INDEX.csv`.
6. `S07/scientific_model/` is an empty folder. The models live in the proof code and `animation/selftest.py`.
7. The engine is bound to its film:
   - `uemotion/narration.py` loads the film's narration files at import;
   - `tokens.py` resolves fonts three folders up;
   - the formula uses the macOS system font Arial Bold.
   A new film copies the engine and supplies its own `narration.py` (`05-animation-engine/ENGINE_GUIDE.md`).
8. The two V3 patches were spliced by hand. The current source already contains them, so a fresh full render needs no splice; this has not been re-run end to end, because re-rendering would overwrite the locked files.
9. Slot 07's Codex verdicts are spread over three files (the root-cause audit, `CODEX_PROGRESS.csv` and the tracker).

## 13. How the next films reach this quality with fewer revisions

The ESTIMATES are reasoned from the two productions, not measured.

1. **Start from the library.** Earth, Moon, the observatory, the astronaut, the stopwatch, the pulse and the parallax camera are in `04-shared-assets/` and `05-animation-engine/`. For Slot 03 (Voyager) the new art reduces to the Voyager spacecraft and a DSN dish (`11-production-management/NEXT_VIDEO_BRIEF_SLOT03.md`).
2. **Lock the narration before the shot design,** and design on real word times. Both films lost time when the voice changed; Slot 02 lost far more because the change came late.
3. **Run a reference sprint, then the masters, on day one.** Up to four parallel single-deliverable Codex runs at effort `high`, each with 2–3 attached references. Claude cuts, registers and rigs while Codex draws.
4. **One moving proof per mechanism,** with asserts, before the cut. Render the 0–10 s opening first and run the inactivity check on it.
5. **Write the disclosure table and the cue sheet before rendering,** with one reason per cue. Build the rights-clear mix in parallel.
6. **Run the three independent reviews** (decoded frames, science asserts, technical) before the owner sees anything. In Slot 07 these found five defects the automated checks had passed.
7. **Ask the owner for the human gates early:**
   - listening on phone and headphones;
   - a muted-viewer test;
   - the music licence.
   These are the only remaining blockers for both finished films.

With these, a Short that reuses the library should need **one owner review round [E]**, against six or more for Slot 02 and two for Slot 07.
