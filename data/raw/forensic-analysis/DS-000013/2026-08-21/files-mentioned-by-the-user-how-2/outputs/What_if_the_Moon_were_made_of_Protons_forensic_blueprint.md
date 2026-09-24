# What If the Moon Were Made of Protons? — Source-Grounded Video Forensic Reconstruction Blueprint

**MASTER_VIDEO_FORENSIC_SYSTEM v7.0 compliance report**  
**Source:** `What if the Moon were made of Protons_.mp4`  
**Analytical authority:** decoded source frames, adjacent source frames, measured timing, source audio, verified transcript, OCR, and metadata.  
**Evidence status:** SOURCE VIDEO INSPECTED — YES.

## Executive finding

This 88.136735-second portrait explainer is physically built from 14 major compositional shots, 39 meaningful stable visual states, and 28 observed animation/state-change events. Its production grammar is not broad cinematic animation. It is a controlled sequence of hand-drawn replacement states, deterministic text/number/arrow reveals, hard visual resets, and one long camera-subject-coupled black-hole expansion. The frame’s static coordinate system is usually more important than the moving element: explanatory geometry remains registered while one annotation changes. The most faithful rebuild is therefore predominantly replacement drawings, vector/text overlays, static holds, and 2.5D editor keyframes, with AI used only for isolated approximation where exact line registration is noncritical. **HIGH CONFIDENCE.**

The filename/title promises a Moon made of protons, but the verified narration asks about a proton Earth and an electron Moon. The source video itself consistently supports the latter. This may be a renamed file rather than the original packaging, so the report preserves the source premise and flags the packaging mismatch instead of silently rewriting it. **HIGH CONFIDENCE on source content; LOW CONFIDENCE on why the filename differs.**

## PASS 0 — Media inspection and source evidence

| Field | Measured value | Confidence |
|---|---:|---|

| Duration | 88.136735 s | HIGH |

| Video duration | 88.125000 s | HIGH |

| Resolution | 720 × 1280 | HIGH |

| Aspect ratio | 9:16 portrait | HIGH |

| Nominal FPS | 24.000 | HIGH |

| Orientation transform | identity; native portrait | HIGH |

| Video codec | H.264 / avc1 | HIGH |

| Video color | Rec.709, video range | HIGH |

| Estimated video bitrate | 253,490 bit/s | HIGH |

| Audio | present | HIGH |

| Audio codec | AAC | HIGH |

| Audio format | stereo, 44.1 kHz | HIGH |

| Estimated audio bitrate | 127,939 bit/s | HIGH |


**Decoded evidence:** 353 quarter-second overview frames; 2,116 source-cadence frames covering 00:00.000–01:28.125; 39 full-resolution 720×1280 keyframes; 5 atlas pages; 24 timestamped narration segments; 110 overview OCR detections plus 106 full-resolution selected-state detections. Dense cadence is approximately one frame per 41.667 ms.

**Evidence limitations:** exact original software, plug-ins, drawing frame rate, easing curves, fonts, AI models, lens, music title, and SFX library cannot be verified. Handwritten text is sometimes below OCR resolution; wording reported as exact is limited to high-confidence OCR and direct visual reading. No external public verification was needed for reconstruction.

### Audio forensic summary

The decoded PCM track is 88.095057 s, stereo 44.1 kHz, with absolute peak 0.844818, overall/mid RMS −18.83 dBFS, side RMS −35.48 dBFS, speech-region RMS −18.52 dBFS, and outside-transcript RMS −30.11 dBFS. The large mid/side gap indicates a strongly center-dominant mix consistent with narration. Three measured ≥150 ms intervals below −42 dBFS occur at 63.40–63.55, 66.95–67.20, and 86.70–88.10. The last interval is the final fade/ending silence. Distinct music, designed SFX, or ambience cannot be confidently isolated from the mixed track; narration is the only semantically verified element.

## PASS 1 — Major-shot EDL

| Shot | In | Out | Duration | Visual type | Transition in | Major function | Motion hero | Static anchor |
|---|---:|---:|---:|---|---|---|---|---|

| S01 | 00.000 | 05.458 | 05.458 | Whiteboard presenter + Earth/Moon field diagram | OPEN | Opening premise and charge-field setup | field drawing | board/presenter |

| S02 | 05.458 | 08.000 | 02.542 | Full-frame destructive flash | HARD CUT / graphic replacement | Immediate danger validation / pattern break | none; static blast hold | blast center |

| S03 | 08.000 | 19.542 | 11.542 | Macro-orbit vs atomic-orbit diagram | HARD CUT / graphic replacement | Build then reject the giant-hydrogen analogy | diagram/text additions | upper/lower diagram coordinates |

| S04 | 19.542 | 26.250 | 06.708 | Two-electron force comparison | HARD CUT / graphic replacement | Quantify electrostatic dominance over gravity | arrows/numbers | vertical particle axis |

| S05 | 26.250 | 38.958 | 12.708 | Whiteboard calculation + escalating rupture | HARD CUT / graphic replacement | Scale two-electron logic to an electron Moon | replacement drawings | board/presenter stage |

| S06 | 38.958 | 41.208 | 02.250 | Electron-Moon potential-energy diagram | HARD CUT / graphic replacement | Name the energy reservoir | none | sphere center |

| S07 | 41.208 | 43.958 | 02.750 | Radial electron-repulsion diagram | HARD CUT / graphic replacement | Visualize stored electrostatic energy | none | radial center |

| S08 | 43.958 | 46.583 | 02.625 | Dual space-time wells | HARD CUT / graphic replacement | Connect energy to relativistic curvature | none | grid horizon |

| S09 | 46.583 | 63.542 | 16.959 | Observable-universe equivalence diagram | HARD CUT / graphic replacement | Reveal universe-scale energy and black-hole outcome | marker/arrows/well/label | universe sphere and labels |

| S10 | 63.542 | 65.375 | 01.833 | Destroyed suburban neighborhood | HARD CUT / graphic replacement | Local consequence reset | none | ground band |

| S11 | 65.375 | 66.375 | 01.000 | Cosmic objects converging inward | SMASH CUT / polarity inversion | Scale consequence from local to cosmic | none | central black hole |

| S12 | 66.375 | 68.167 | 01.792 | Lone black hole on black | HARD CUT / graphic replacement | Hold the universe-collapse question | none | black field/ring center |

| S13 | 68.167 | 73.125 | 04.958 | Dark-energy comic diagram | HARD CUT / graphic replacement | Qualify the answer with uncertainty | annotation reveals | ring center |

| S14 | 73.125 | 88.137 | 15.012 | Starfield + continuously enlarging black-hole ring | SMASH CUT / polarity inversion | Explain causal delay, then land the dark-comic cutoff | ring expansion + text replacements | ring center and screen-space captions |


**Measured editing statistics:** total shots 14; average shot length 6.295 s; median 3.854 s; shortest S11 at 1.000 s; longest S09 at 16.959 s. Fastest cluster S10–S12 (three consequence resets across 4.625 s); slowest cluster S09 and S14 (proof assembly and final causal-delay payoff). Cuts usually coincide with a new argument, proof-completion, contradiction, or scale reset—not arbitrary time blocks.

## PASS 2 — Visual-state index

| Visual | State in | Representative frame | Shot | F-state | Literal stable configuration |
|---|---:|---:|---|---|---|

| V01 | 00.000 | 00.250 | S01 | F01.0 | Whiteboard premise |

| V02 | 00.708 | 01.250 | S01 | F01.1 | Proton-Earth radial field |

| V03 | 02.125 | 03.250 | S01 | F01.2 | Coupled Earth–Moon field |

| V04 | 05.458 | 06.500 | S02 | F02.0 | Destructive flash |

| V05 | 08.000 | 09.000 | S03 | F03.0 | Macroscopic orbit |

| V06 | 10.167 | 11.500 | S03 | F03.1 | Atomic analogue added |

| V07 | 13.417 | 13.750 | S03 | F03.2 | Atomic ORBIT label |

| V08 | 14.667 | 15.250 | S03 | F03.3 | Both systems labeled ORBIT |

| V09 | 16.542 | 18.000 | S03 | F03.4 | Macro analogy struck out |

| V10 | 19.542 | 20.500 | S04 | F04.0 | Two electrons |

| V11 | 21.458 | 21.750 | S04 | F04.1 | Opposing repulsion arrows |

| V12 | 22.750 | 23.250 | S04 | F04.2 | Twenty-order multiplier |

| V13 | 24.542 | 25.250 | S04 | F04.3 | Force comparison completed |

| V14 | 26.250 | 27.250 | S05 | F05.0 | Electron-Moon calculation |

| V15 | 28.292 | 28.750 | S05 | F05.1 | UH OH reaction |

| V16 | 29.083 | 29.500 | S05 | F05.2 | Board ruptures |

| V17 | 30.042 | 30.750 | S05 | F05.3 | PLEASE STOP plea |

| V18 | 31.833 | 32.250 | S05 | F05.4 | Downward interaction arrow |

| V19 | 32.750 | 34.250 | S05 | F05.5 | Red impact burst |

| V20 | 36.125 | 37.500 | S05 | F05.6 | Electron Moon explodes outward |

| V21 | 38.958 | 40.000 | S06 | F06.0 | Electrostatic potential energy |

| V22 | 41.208 | 42.500 | S07 | F07.0 | Potential energy as radial repulsion |

| V23 | 43.958 | 45.000 | S08 | F08.0 | Energy warps space-time |

| V24 | 46.583 | 47.500 | S09 | F09.0 | Observable-universe equivalence |

| V25 | 47.750 | 49.000 | S09 | F09.1 | Tiny Moon marker jitter |

| V26 | 54.792 | 56.000 | S09 | F09.2 | Compression arrows |

| V27 | 57.417 | 58.500 | S09 | F09.3 | Moon becomes black-hole well |

| V28 | 60.042 | 61.500 | S09 | F09.4 | BLACK HOLE label |

| V29 | 63.542 | 64.500 | S10 | F10.0 | Local destruction |

| V30 | 65.375 | 66.000 | S11 | F11.0 | Cosmic collapse montage |

| V31 | 66.375 | 67.500 | S12 | F12.0 | Lone black hole |

| V32 | 68.167 | 69.500 | S13 | F13.0 | Dark-energy uncertainty |

| V33 | 70.875 | 71.750 | S13 | F13.1 | String-theory aside |

| V34 | 73.125 | 74.250 | S14 | F14.0 | Nearby galaxy unaware |

| V35 | 76.583 | 77.000 | S14 | F14.1 | Business-as-usual dialogue |

| V36 | 78.375 | 78.750 | S14 | F14.2 | Even bigger problems |

| V37 | 80.042 | 81.500 | S14 | F14.3 | Problem finally comprehended |

| V38 | 83.417 | 84.250 | S14 | F14.4 | LA LA LA denial |

| V39 | 86.000 | 87.750 | S14 | F14.5 | Final giant ring |


States are created only for material changes in composition, diagram content, text, pose, object geometry, color function, or motion state. Compression noise and subpixel cadence differences were excluded. The tiny Moon-marker loop (V25) is retained because it is an observable replacement-drawing motion, while the final black-hole shot is represented by semantic text states plus start/end scale states rather than a false state for every intermediate frame.

## PASS 3–5 — Persistent assets, dense motion, and state chains

### Persistent asset manifest

| ID | Class | Persistent specification |
|---|---|---|

| C01 | Character | stick-figure presenter; oval head, thin limbs, black line |

| C02 | Character | bottom-right ‘stringy’ observer; white line on black |

| E01 | Environment | whiteboard/presenter stage |

| E02 | Environment | white negative-space technical diagram |

| E03 | Environment | black cosmic field / starfield |

| E04 | Environment | suburban destruction strip with gray ground |

| O01 | Object | proton Earth sphere |

| O02 | Object | electron Moon sphere |

| O03 | Object | single proton/electron symbols |

| O04 | Object | 10⁵³-electron Moon cluster |

| O05 | Object | observable-universe sphere |

| O06 | Object | black-hole point/ring/well family |

| I01 | Illustration | gray-white destructive flash |

| I02 | Illustration | two-well space-time grid |

| I03 | Illustration | cosmic-collapse object montage |

| G01 | Graphic | dashed orbit guide |

| G02 | Graphic | black explanatory arrows |

| G03 | Graphic | red strike-through loops |

| G04 | Graphic | repulsion-arrow system |

| G05 | Graphic | ≈ equivalence mark |

| G06 | Graphic | compression-arrow pair |

| G07 | Graphic | red dark-energy question cluster |

| D01 | Diagram | Earth–Moon electric-field board |

| D02 | Diagram | macro/atomic orbit comparison |

| D03 | Diagram | two-electron force comparison |

| D04 | Diagram | electrostatic PE versus E=mc² wells |

| D05 | Diagram | observable-universe-to-Moon equivalence |

| T01 | Text system | irregular hand-drawn black uppercase |

| T02 | Text system | scarce irregular red uppercase |

| T03 | Text system | small centered white uppercase on black |

| A01 | Audio | center-dominant English narration |


### Complete motion-event inventory

| Event | Source → target | Timestamp | Actual motion/change | Relationship | Primary method | AI suitability |
|---|---|---|---|---|---|---|

| A01 | V01/F01.0 → V02/F01.1 | 00:00.708 | replacement drawing / additive arrow reveal: radial arrows and darker Earth texture | STATE REPLACEMENT | REPLACEMENT DRAWINGS + editor cut | LOW |

| A02 | V02/F01.1 → V03/F01.2 | 00:02.125 | replacement field drawing: curved Earth–Moon field lines | STATE REPLACEMENT | REPLACEMENT DRAWINGS | LOW |

| A03 | V05/F03.0 → V06/F03.1 | 00:10.167 | additive diagram reveal: lower proton/electron orbit analogy | SEQUENTIAL | VECTOR MOTION / opacity or replacement drawing | LOW |

| A04 | V06/F03.1 → V07/F03.2 | 00:13.417 | text reveal: lower ORBIT label | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A05 | V07/F03.2 → V08/F03.3 | 00:14.667 | text reveal: upper ORBIT label | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A06 | V08/F03.3 → V09/F03.4 | 00:16.542 | red scribble reveal: red strike-through loops over upper system | SEQUENTIAL | VECTOR TRIM PATH / hand-drawn overlay | MEDIUM |

| A07 | V10/F04.0 → V11/F04.1 | 00:21.458 | opposed arrow reveal: two long force arrows | SIMULTANEOUS COUPLED | VECTOR MOTION / trim paths | LOW |

| A08 | V11/F04.1 → V12/F04.2 | 00:22.750 | number reveal: 10²⁰ multiplier | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A09 | V12/F04.2 → V13/F04.3 | 00:24.542 | equation and force-label reveal: central F marks and 10²⁰·F completion | SEQUENTIAL | EDITOR TEXT + VECTOR OVERLAY | LOW |

| A10 | V14/F05.0 → V15/F05.1 | 00:28.292 | text pop: UH OH caption | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A11 | V15/F05.1 → V16/F05.2 | 00:29.083 | replacement drawing / pose change: torn board border and presenter hands-to-head pose | SIMULTANEOUS COUPLED | REPLACEMENT DRAWINGS | LOW |

| A12 | V16/F05.2 → V17/F05.3 | 00:30.042 | text pop: PLEASE STOP! caption | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A13 | V17/F05.3 → V18/F05.4 | 00:31.833 | arrow reveal: downward interaction arrow | SEQUENTIAL | VECTOR TRIM PATH | LOW |

| A14 | V18/F05.4 → V19/F05.5 | 00:32.750 | impact pop: small red burst at Earth | SEQUENTIAL | SHAPE LAYER / replacement drawing | LOW |

| A15 | V19/F05.5 → V20/F05.6 | 00:36.125 | replacement explosion drawing: radial rays and electron symbols across board | STATE REPLACEMENT | REPLACEMENT DRAWINGS | MEDIUM |

| A16 | V24/F09.0 → V25/F09.1 | 00:47.750–00:54.750 | replacement-drawing jitter loop: tiny Moon marker | PERSISTENT LOOP | REPLACEMENT-DRAWING FRAME LOOP | LOW |

| A17 | V25/F09.1 → V26/F09.2 | 00:54.792 | two-arrow reveal: converging compression arrows | SIMULTANEOUS COUPLED | VECTOR TRIM PATHS | LOW |

| A18 | V26/F09.2 → V27/F09.3 | 00:57.417 | local state replacement: Moon marker becomes black-hole well | STATE REPLACEMENT | REPLACEMENT DRAWING / first-last-frame optional | MEDIUM |

| A19 | V27/F09.3 → V28/F09.4 | 01:00.042 | text reveal: BLACK HOLE label | SEQUENTIAL | EDITOR TEXT OVERLAY | LOW |

| A20 | V31/F12.0 → V32/F13.0 | 01:08.167 | red graphic reveal: DARK ENERGY text, question marks and arrows | SEQUENTIAL | EDITOR TEXT + VECTOR OVERLAY | LOW |

| A21 | V32/F13.0 → V33/F13.1 | 01:10.875 | character/caption reveal: bottom-right character and white caption | SIMULTANEOUS COUPLED | REPLACEMENT DRAWING + text overlay | LOW |

| A22 | V34/F14.0 → V39/F14.5 | 01:13.125–01:28.125 | continuous scale/reframe: black-hole ring with coordinated starfield approach | CAMERA-SUBJECT COUPLED / PERSISTENT | 2.5D EDITOR KEYFRAMES / HYBRID | MEDIUM |

| A23 | V34/F14.0 → V35/F14.1 | approximately 01:15.000 | white text replacement: PROBLEMS becomes BIGGER PROBLEMS | STATE REPLACEMENT over A22 | EDITOR TEXT REPLACEMENT | LOW |

| A24 | V34/F14.0 → V35/F14.1 | 01:16.583 | red text replacement: WHAT A BEAUTIFUL DAY becomes JUST MINDING MY OWN BUSINESS… | SIMULTANEOUS INDEPENDENT over A22 | EDITOR TEXT REPLACEMENT | LOW |

| A25 | V35/F14.1 → V36/F14.2 | 01:18.375 | white text replacement: BIGGER PROBLEMS becomes EVEN BIGGER PROBLEMS | STATE REPLACEMENT over A22 | EDITOR TEXT REPLACEMENT | LOW |

| A26 | V36/F14.2 → V37/F14.3 | 01:20.042 | red text replacement: JUST MINDING… becomes HO HUM | SIMULTANEOUS INDEPENDENT over A22 | EDITOR TEXT REPLACEMENT | LOW |

| A27 | V36/F14.2 → V37/F14.3 | approximately 01:21.000 | white text replacement: EVEN BIGGER PROBLEMS becomes three-line payoff | STATE REPLACEMENT over A22 | EDITOR TEXT REPLACEMENT | LOW |

| A28 | V37/F14.3 → V38/F14.4 | 01:23.417 | red text replacement: HO HUM becomes LA LA LA | SIMULTANEOUS INDEPENDENT over A22 | EDITOR TEXT REPLACEMENT | LOW |


**State-chain rule:** every A-event begins from the explicitly listed post-previous-event state. Hard cuts between shots are editing transitions in the EDL, not fabricated in-shot animation. Static shot bases therefore have no AI-motion prompt. The final shot’s A22 is a persistent camera-subject-coupled expansion; A23–A28 are independent text replacements composited over it.

## PASS 6 — ENGINE A: Script intelligence

### Verified transcript segments

| Segment | Start | End | Source transcription |
|---:|---:|---:|---|

| 01 | 00.000 | 03.680 | What if the Earth were made entirely of protons and the Moon were made entirely of electrons? |

| 02 | 04.320 | 07.620 | This is, by far, the most destructive what-if scenario to date. |

| 03 | 08.000 | 11.720 | You might imagine an electron moon orbiting a proton Earth, sort of like a gigantic hydrogen atom. |

| 04 | 11.960 | 13.180 | On one level, it sort of makes sense. |

| 05 | 13.460 | 15.540 | Electrons orbit protons, and moons orbit planets. |

| 06 | 16.020 | 19.020 | However, electron moons do not orbit proton planets. |

| 07 | 19.560 | 22.680 | If you put two negatively-charged electrons together, they try to fly apart with a force |

| 08 | 22.680 | 25.800 | of about 20 orders of magnitude stronger than the gravity pulling them together. |

| 09 | 26.180 | 28.880 | If you put 10 to the 53 electrons together to build a moon, |

| 10 | 28.880 | 31.420 | they push each other apart with an unbelievable amount of energy. |

| 11 | 31.820 | 35.360 | The moon and Earth would have no chance to gravitationally or even electrostatically influence |

| 12 | 35.360 | 38.500 | each other. The forces trying to blow each one apart would be far more powerful. |

| 13 | 38.960 | 42.040 | There is a huge amount of potential energy in this scenario, the energy that we imagine |

| 14 | 42.040 | 46.140 | would blast all those electrons apart. That energy warps space and time just like mass does. |

| 15 | 46.560 | 50.100 | The amount of energy in our electron moon, it turns out, is about equal to the total mass |

| 16 | 50.100 | 54.440 | and energy of the entire observable universe. An entire observable universe where the mass |

| 17 | 54.440 | 58.340 | energy concentrated into the space of our relatively small moon would warp space-time |

| 18 | 58.340 | 62.940 | so strongly that it would easily overpower even the repulsion of those 10 to the 53 electrons. |

| 19 | 63.500 | 66.760 | Would the attraction of this universe mass black hole cause the rest of the universe to collapse? |

| 20 | 67.140 | 71.140 | It's hard to say. The answer kind of depends on what the deal with dark energy is, and nobody |

| 21 | 71.140 | 75.940 | knows what the deal with dark energy is. But for the meantime, at least, nearby galaxies would be |

| 22 | 75.940 | 80.000 | safe, since the gravitational influence of the black hole can only expand outward at the speed |

| 23 | 80.000 | 83.820 | of light. Most of the universe around us would remain blissfully unaware of our ridiculous |

| 24 | 83.820 | 86.680 | electron experiment, until they suddenly... |


The transcript is machine-derived from the decoded source and reviewed against visible subject matter. The 24 raw segments are regrouped into 16 meaningful script beats below.

### A1 — Script grounding and loop tracking

| Beat | Timestamp | Spoken words / verified meaning | Function | Active viewer question | Loop status |
|---|---|---|---|---|---|

| B01 | 00:00.000–00:03.680 | What if the Earth were made entirely of protons and the Moon were made entirely of electrons? | HOOK / QUESTION | What exactly happens to this charged Earth–Moon system? | OPEN |

| B02 | 00:04.320–00:07.620 | This is, by far, the most destructive what-if scenario to date. | ESCALATION / VALUE PREVIEW | Why is it more destructive than every prior scenario? | ESCALATING |

| B03 | 00:08.000–00:11.720 | You might imagine an electron moon orbiting a proton Earth, sort of like a gigantic hydrogen atom. | SETUP / INTUITIVE MODEL | Does the giant-hydrogen analogy work? | OPEN |

| B04 | 00:11.960–00:15.540 | On one level, it sort of makes sense. Electrons orbit protons, and moons orbit planets. | EVIDENCE FOR INTUITION | What breaks the analogy? | ESCALATING |

| B05 | 00:16.020–00:19.020 | However, electron moons do not orbit proton planets. | REVERSAL | What force prevents the orbit? | REPLACED BY FORCE LOOP |

| B06 | 00:19.560–00:25.800 | Two negatively charged electrons try to fly apart with a force about 20 orders of magnitude stronger than gravity. | EXPLANATION / QUANTIFICATION | What happens when that imbalance is scaled to a Moon? | PARTIALLY ANSWERED |

| B07 | 00:26.180–00:31.420 | Ten to the 53 electrons assembled as a Moon push each other apart with unbelievable energy. | ESCALATION | How large is the energy reservoir? | OPEN |

| B08 | 00:31.820–00:38.500 | Internal forces overwhelm any gravitational or electrostatic influence between Moon and Earth. | CONSEQUENCE / MICRO-PAYOFF | Can anything contain the electrons? | PARTIALLY ANSWERED |

| B09 | 00:38.960–00:46.140 | The potential energy that would blast the electrons apart warps space and time just like mass. | CAUSAL BRIDGE | How much curvature does that energy create? | OPEN |

| B10 | 00:46.560–00:54.440 | The electron Moon’s energy is about equal to the total mass and energy of the observable universe. | MAJOR REVEAL | What happens when universe-scale energy is Moon-sized? | ESCALATING |

| B11 | 00:54.440–01:02.940 | Concentrating that mass-energy into a Moon-sized space creates curvature strong enough to overpower electron repulsion. | MEGA PAYOFF / BLACK-HOLE REVEAL | Does the resulting black hole collapse the universe? | OPEN |

| B12 | 01:03.500–01:06.760 | Would this universe-mass black hole cause the rest of the universe to collapse? | NEW QUESTION / ESCALATION | Will everything be pulled in? | OPEN |

| B13 | 01:07.140–01:15.940 | It is hard to say because the answer depends on unknown dark-energy behavior. | QUALIFICATION / UNCERTAINTY | What can be said with confidence? | PARTIALLY ANSWERED |

| B14 | 01:15.940–01:20.000 | Nearby galaxies would be safe for the meantime. | PARTIAL RELIEF | Why are they temporarily safe? | OPEN |

| B15 | 01:20.000–01:23.820 | The black hole’s gravitational influence can expand outward only at light speed. | EXPLANATION / CAUSAL DELAY | What happens when the influence arrives? | ESCALATING |

| B16 | 01:23.820–01:26.680 | Most of the universe remains blissfully unaware until they suddenly… | DARK-COMIC PAYOFF / CUTOFF | The ellipsis implies arrival without stating it. | ANSWERED BY VISUAL |

### A2 — Packaging promise

**TITLE PROMISE:** filename asks what happens if the Moon is made of protons. **THUMBNAIL PROMISE:** unavailable; cannot verify. **COMBINED CLICK QUESTION:** limited to the file-title premise. **EXPECTED PAYOFF:** a physics consequence for a proton Moon. **OPENING VALIDATION:** the source instead states proton Earth + electron Moon. **BODY DELIVERY:** strongly delivers the narrated charged-Earth/electron-Moon scenario. **FINAL PAYOFF MATCH:** strong match to narration, mismatch to filename. **CLASSIFICATION:** PARTIAL MATCH / possible renamed-file mismatch.

### A3 — Hook architecture

Context is one sentence and concrete. Relevance comes from familiar Earth and Moon objects. The explicit ‘most destructive’ superlative is the pattern break and value preview. Click validation occurs visually in V01–V04: the named bodies appear, charge fields are introduced, and a destructive flash arrives before eight seconds. The hook opens both a mechanism loop (‘what happens?’) and a scale loop (‘how destructive?’).

### A4 — Causal story spine

**SETUP:** proton Earth + electron Moon. **BUT:** a giant-hydrogen analogy seems plausible. **THEREFORE:** compare atomic and celestial orbits. **BUT:** like-charged electrons repel 10²⁰ times more strongly than gravity. **THEREFORE:** 10⁵³ electrons cannot form a stable Moon. **CONSEQUENCE:** their potential energy is enormous. **BUT:** energy gravitates. **THEREFORE:** universe-scale energy compressed to Moon scale makes a black hole. **ESCALATION:** could it collapse the universe? **PAYOFF:** influence propagates at light speed, so distant observers remain unaware—until the visual threat arrives. The spine is causal, not an ‘and then’ chain.

### A5 — Curiosity system

The main question expands from local orbital stability to internal electron repulsion, then to energy scale, black-hole formation, and universe collapse. Each answer replaces itself with a larger but causally linked question. Curiosity is **EXPANDING** through B12, then deliberately **STABLE** during the dark-energy qualification. The ending closes the causal-delay loop visually while leaving the spoken sentence suspended. No evidence supports accusing the piece of artificial delay; proof density remains high.

### A6 — Payoff ladder

**Micro payoff:** macro orbit analogy is false. **Larger payoff:** electrostatic force beats gravity by 20 orders. **Mega payoff:** 10⁵³ electrons store observable-universe-scale energy. **Ultimate payoff:** the energy collapses to a black hole whose influence reaches the universe only causally. Each payoff is earned by the preceding diagram and narration; the universe-energy reveal is the strongest surprise. The final cutoff is intentionally dark-comic rather than fully verbalized, and the expanding ring supplies closure.

### A7 — Logic audit

The local argument follows CLAIM → REASON → QUANTIFIED COMPARISON → SCALE-UP → RELATIVISTIC CONSEQUENCE. The weakest premise is the jump from enormous electrostatic potential energy to the exact observable-universe equivalence: the source states the equality but does not show a derivation. Likewise, dark energy is correctly framed as uncertainty rather than evidence. A rigorous long-form version would add one concise equation/source card before B10, but doing so would slow this short format. No internal contradiction is visible in the narrated chain.

### A8 — Emotion

Curiosity drives the opening; surprise lands at the orbit rejection; tension and humor combine through UH OH / PLEASE STOP; awe dominates the observable-universe comparison; fear appears in the black-hole question; relief is partial and ironic; closure arrives through dark comedy. These labels are grounded in spoken superlatives, visual reaction captions, scale reveals, and the final cutoff—not inferred audience metrics.

### A9 — Retention risks

**Opening risk:** the filename mismatch could confuse a viewer expecting a proton Moon. **Early-body risk:** the macro/atomic orbit diagram holds for 11.5 s, mitigated by staged labels and red rejection marks. **Midpoint risk:** the 38.96–46.58 energy bridge uses three rapid abstract diagrams and may require replay. **Pre-payoff risk:** the observable-universe infographic holds 16.96 s, but arrows/well/label provide sequential micro-payoffs. **CTA risk:** there is no CTA; the piece ends on story payoff. No drop percentages are claimed.

### A10 — Share and replay

Shareable moments: ‘most destructive’ flash (5.458 s), 10²⁰ force ratio (22.750 s), universe-energy equivalence (46.583 s), and the expanding-ring punchline (73.125 s onward). Positive replay candidate: the PE → E=mc² → observable-universe sequence. Confusion replay risk: why the energy’s gravity overpowers electron repulsion, because the derivation is asserted faster than it is shown.

### A11–A12 — CTA and next-video bridge

No subscribe/comment/playlist/product/community CTA is audible or visible. Classification: **N/A**, not ‘premature.’ There is no explicit next-video bridge. The ending chooses CURRENT PAYOFF → VISUALIZED IMPLICATION rather than routing attention elsewhere.

### A13 — Script consensus

**STRONG AGREEMENTS:** superb causal escalation; memorable quantified contrast; packaging validation within the source narration; visuals usually arrive on the explanatory noun. **IMPORTANT TRADEOFF:** speed preserves comedic force but removes derivational detail. **CRITICAL PROBLEM:** file-title premise and narrated premise differ. **HIGH PRIORITY:** ensure published title matches proton Earth/electron Moon, or rewrite the scenario consistently. **MEDIUM PRIORITY:** insert a five-second derivation card for the universe-energy equivalence. **HIGHEST-LEVERAGE FIX:** clarify the exact premise in title/thumbnail without weakening the ‘most destructive’ hook.

## PASS 7 — ENGINE B: Visual intelligence

### B1–B2 — Objective grounding and spatial geometry

The video uses three coordinate regimes: (1) a whiteboard occupying the top 40–45% with a presenter below; (2) centered white-field diagrams using strong vertical stacking; and (3) black cosmic frames anchored by a small luminous hole that grows into the final dominant circle. Numeric X/Y descriptions in the cards are approximate normalized visual maps, not pixel measurements. Diagrams maintain fixed centers while annotations enter, which makes registration part of the style.

### B3–B4 — Attention and dominance

Repeated eye path: largest dark sphere/central diagram → scarce red accent or new arrow → small equation/label → presenter reaction. Motion normally has the highest pull because only one local region changes. White-field shots are **CLEAN/CONTROLLED**; the radial-explosion and cosmic-collapse illustrations are intentionally **COMPETITIVE** but short. Red is scarce and therefore dominant wherever used.

### B5 — Cinematography

The visual language is flat, diagrammatic, and orthographic rather than lens-driven. Shot size is determined by page layout, not photographic focal length. Camera height and angle are effectively straight-on. Depth is encoded by overlap, scale, grid wells, and black-hole rings. Camera energy is generally locked; the principal exception is S14’s smooth push/scale into the black hole. Exact lens data is not applicable/verifiable.

### B6–B8 — Temporal change, editing, and visual retention

Most changes are ADDITIVE REVEAL, REPLACEMENT, TEXT CHANGED, or GRAPHIC MODIFICATION. Objects rarely translate. Hard cuts reset argument scale: board → minimal diagram → reaction board → energy diagram → cosmic consequence. Static periods are refreshed by a new annotation every roughly 1–4 s in technical shots. The longest visual base, S09, avoids fatigue through marker jitter, compression arrows, well transformation, and BLACK HOLE label.

### B9 — Information value

Essential: charge-field diagrams, 10²⁰ force comparison, 10⁵³ Moon calculation, PE/mass analogy, universe equivalence, black-hole well, light-speed ring. Explanatory/reinforcing: orbit labels, reaction captions, dark-energy cluster. Emotional: flash, torn board, neighborhood collapse, LA LA LA. Decorative content is minimal; removing star specks would reduce cosmic atmosphere but not core comprehension.

### B10–B12 — Object lifecycle, callbacks, continuity drift

O02 electron Moon moves from labeled sphere → atomic analogue → 10⁵³ cluster → explosive radial field → PE diagram → universe-energy dot → black-hole well. O06 black hole is introduced as a well, reused as a lone ring, contextualized by dark energy, and transformed into the final frame-filling threat. C01 presenter returns only in whiteboard sections and retains line identity; pose changes are deliberate replacement drawings. No unintended wardrobe/anatomy drift applies beyond the stylized figure. Diagram scale changes are functional, not continuity errors.

### B13 — Color

Dominant white/black establishes the scientific notebook. Gray is restricted to stipple, ground, and blast falloff. Saturated red appears only for contradiction, alarming numbers/reactions, dark-energy uncertainty, and the unaware-observer dialogue. Accent scarcity is extremely high, so red acts as an attention command. The palette inverts at S11: black becomes background and white becomes line/text, retaining the same binary DNA.

### B14 — Typography and graphics

Typography is irregular hand-drawn uppercase, horizontally centered near its referent, with exact formulas and numbers treated as deterministic overlays. Entry is normally an instant replacement/pop; text holds until the next state and disappears by cut or replacement. Graphics favor dashed circles, straight outlined arrows, loose red scribbles, radial lines, and simple wireframe grids. The final white captions stay centered inside the expanding ring while red dialogue remains fixed above-left.

### B15 — Visual DNA

**CHARACTER DNA:** minimal stick figures, pose carries emotion. **ENVIRONMENT DNA:** white page/board or black page/starfield. **COLOR DNA:** monochrome with scarce red. **LIGHTING DNA:** flat paper field; glow used only for flash/black hole. **GRAPHIC DNA:** hand-drawn line + stipple. **COMPOSITION DNA:** centered proof object with generous negative space. **CAMERA DNA:** locked frontal, one final push. **MOTION DNA:** discrete replacement states. **TRANSITION DNA:** hard semantic cuts. **B-ROLL DNA:** none; illustrations do the work. **DIAGRAM DNA:** one invariant coordinate frame plus one changing annotation.

## PASS 8–12 — ENGINE C: Per-visual reconstruction cards

The following 39 cards are self-contained. Each image prompt deliberately requests a text-free clean plate because exact lettering, numbers, and formulas are more faithfully added in the editor. Every actual A-event appears once as a full animation event card; hard-cut bases and static holds explicitly require no AI animation.


## V01 — 00.250s — Whiteboard premise

**SHOT:** S01  
**SOURCE REFERENCE FRAME:** [V01_0000250ms.jpg](moon_protons_forensics/keyframes/V01_0000250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 00.000s / 00.250s  
**DURATION TO NEXT MATERIAL STATE:** 0.708s  
**STATE ID:** F01.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a stick-figure presenter stands below a framed board showing a large Earth at upper center-left, a smaller Moon at upper right, and a dashed circular orbit. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A stick-figure presenter stands below a framed board showing a large Earth at upper center-left, a smaller Moon at upper right, and a dashed circular orbit. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “What if the Earth were made entirely of protons and the Moon were made entirely of electrons?”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** What if the Earth were made entirely of.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Concrete setup and immediate click validation.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Initial source state; no prior visual.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Concrete setup and immediate click validation. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** Earth–Moon board diagram.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: EARTH; MOON  
**VISUAL HERO:** Earth–Moon board diagram.  
**STATIC COORDINATE FRAME:** board/presenter.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Upper board occupies roughly Y 6–40; Earth centers near X 45/Y 22 at about 18% frame width; Moon sits near X 72/Y 22 at about 8%; presenter occupies lower-left X 10–38/Y 48–92; wide white negative space remains lower-right. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** Earth–Moon board diagram → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** Earth–Moon board diagram. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE. **BASE:** F01.0 within S01. **CHANGES:** Initial source state; no prior visual. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A stick-figure presenter stands below a framed board showing a large Earth at upper center-left, a smaller Moon at upper right, and a dashed circular orbit. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white field, thin imperfect black line, mid-gray stippled spheres. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A stick-figure presenter stands below a framed board showing a large Earth at upper center-left, a smaller Moon at upper right, and a dashed circular orbit. Exact composition: Upper board occupies roughly Y 6–40; Earth centers near X 45/Y 22 at about 18% frame width; Moon sits near X 72/Y 22 at about 8%; presenter occupies lower-left X 10–38/Y 48–92; wide white negative space remains lower-right. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white field, thin imperfect black line, mid-gray stippled spheres. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F01.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** EARTH; MOON Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white field, thin imperfect black line, mid-gray stippled spheres), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F01.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Whiteboard premise. **SHOT MEMBERSHIP:** S01 (0.000–5.458).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** none. **CURRENT:** F01.0. **NEXT:** F01.1. **TRANSITION INTO CURRENT:** Initial source state; no prior visual. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F01.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 0.708s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 00.708s, then use a local additive/replacement event into V02. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V01 as the exact observed state: Earth–Moon board diagram is the visual hero, board/presenter is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V02 — 01.250s — Proton-Earth radial field

**SHOT:** S01  
**SOURCE REFERENCE FRAME:** [V02_0001250ms.jpg](moon_protons_forensics/keyframes/V02_0001250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 00.708s / 01.250s  
**DURATION TO NEXT MATERIAL STATE:** 1.417s  
**STATE ID:** F01.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the same board and presenter remain fixed while straight black arrows radiate outward from the now densely stippled Earth. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The same board and presenter remain fixed while straight black arrows radiate outward from the now densely stippled Earth. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “Earth were made entirely of protons”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** Earth were made entirely of protons.  
**MOTION CUE:** A01  
**FUNCTION:** Turn the verbal charge premise into a visible outward-force field.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Radial arrows and darker Earth texture are added; board, Moon, labels, presenter, crop, and camera stay fixed.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Turn the verbal charge premise into a visible outward-force field. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** radial arrows around Earth.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: EARTH; MOON  
**VISUAL HERO:** radial arrows around Earth.  
**STATIC COORDINATE FRAME:** board/presenter.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Preserve V01 exactly; arrows occupy the board around Earth from approximately X 8–70/Y 7–37 without entering the presenter region. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** radial arrows around Earth → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** radial arrows around Earth. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** MODIFIED REUSE / ANIMATION END STATE. **BASE:** F01.1 within S01. **CHANGES:** Radial arrows and darker Earth texture are added; board, Moon, labels, presenter, crop, and camera stay fixed. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The same board and presenter remain fixed while straight black arrows radiate outward from the now densely stippled Earth. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The same board and presenter remain fixed while straight black arrows radiate outward from the now densely stippled Earth. Exact composition: Preserve V01 exactly; arrows occupy the board around Earth from approximately X 8–70/Y 7–37 without entering the presenter region. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F01.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** EARTH; MOON Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F01.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Proton-Earth radial field. **SHOT MEMBERSHIP:** S01 (0.000–5.458).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F01.0. **CURRENT:** F01.1. **NEXT:** F01.2. **TRANSITION INTO CURRENT:** Radial arrows and darker Earth texture are added; board, Moon, labels, presenter, crop, and camera stay fixed. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A01:** replacement drawing / additive arrow reveal; V01/F01.0 → V02/F01.1; 00:00.708; target radial arrows and darker Earth texture; relationship STATE REPLACEMENT.

### 17. WHY MOVE

**A01 — WHY:** Communicates positive-charge repulsion around Earth. **Direction:** outward from Earth follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** single-frame graphic change; amplitude/path radial; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** radial arrows and darker Earth texture. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A01: STATE REPLACEMENT** because communicates positive-charge repulsion around earth.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWINGS + editor cut. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A01 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A01 PASS:** source V01/F01.0; animate only radial arrows and darker Earth texture; target region X 8–70, Y 7–37; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A01 SOURCE FRAME STATE:** V01/F01.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V01. **SOURCE IMAGE PROMPT:** build V01 as a 720×1280 text-free hand-drawn clean plate: A stick-figure presenter stands below a framed board showing a large Earth at upper center-left, a smaller Moon at upper right, and a dashed circular orbit. Layout: Upper board occupies roughly Y 6–40; Earth centers near X 45/Y 22 at about 18% frame width; Moon sits near X 72/Y 22 at about 8%; presenter occupies lower-left X 10–38/Y 48–92; wide white negative space remains lower-right. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A01

**SOURCE STATE:** V01/F01.0  
**TARGET STATE:** V02/F01.1  
**TIMESTAMP:** 00:00.708  
**MOTION TYPE:** replacement drawing / additive arrow reveal  
**MOTION HERO / ALLOWED MOTION:** radial arrows and darker Earth texture  
**START STATE:** V01, matching the source description above.  
**END STATE:** V02, matching this card’s target configuration.  
**DIRECTION:** outward from Earth  
**SPEED:** single-frame graphic change  
**AMPLITUDE / PATH:** radial; ROI X 8–70, Y 7–37  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:00.708.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWINGS + editor cut. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Add only the observed black radial arrows around Earth and deepen the Earth’s stippled texture in one crisp replacement step. Preserve the board, Moon, labels, presenter, framing, white background and all screen positions exactly. Hold the completed field drawing.”  
**CHARACTER COUNT:** 279 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A01: duplicate the stable source precomp; isolate X 8–70, Y 7–37; execute REPLACEMENT DRAWINGS + editor cut; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 02.125s, then use a local additive/replacement event into V03. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V02 as the exact observed state: radial arrows around Earth is the visual hero, board/presenter is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V03 — 03.250s — Coupled Earth–Moon field

**SHOT:** S01  
**SOURCE REFERENCE FRAME:** [V03_0003250ms.jpg](moon_protons_forensics/keyframes/V03_0003250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 02.125s / 03.250s  
**DURATION TO NEXT MATERIAL STATE:** 3.333s  
**STATE ID:** F01.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the board now contains curved field lines wrapping between the large Earth and smaller Moon, while the presenter remains still beneath it. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The board now contains curved field lines wrapping between the large Earth and smaller Moon, while the presenter remains still beneath it. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “and the Moon were made entirely of electrons”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** and the Moon were made entirely of electrons.  
**MOTION CUE:** A02  
**FUNCTION:** Show attraction across the macro pair while preserving the charged-body setup.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Straight radial lines are replaced/extended by curved inter-body lines and arrowheads; all non-field elements remain registered.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Show attraction across the macro pair while preserving the charged-body setup. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** curved electric-field topology.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: EARTH; MOON  
**VISUAL HERO:** curved electric-field topology.  
**STATIC COORDINATE FRAME:** board/presenter.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Earth and Moon retain V02 coordinates; looping curves fill the board, concentrated between X 46–78/Y 9–35; presenter and lower white field are unchanged. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** curved electric-field topology → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** curved electric-field topology. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F01.2 within S01. **CHANGES:** Straight radial lines are replaced/extended by curved inter-body lines and arrowheads; all non-field elements remain registered. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The board now contains curved field lines wrapping between the large Earth and smaller Moon, while the presenter remains still beneath it. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The board now contains curved field lines wrapping between the large Earth and smaller Moon, while the presenter remains still beneath it. Exact composition: Earth and Moon retain V02 coordinates; looping curves fill the board, concentrated between X 46–78/Y 9–35; presenter and lower white field are unchanged. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F01.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** EARTH; MOON Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F01.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Coupled Earth–Moon field. **SHOT MEMBERSHIP:** S01 (0.000–5.458).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F01.1. **CURRENT:** F01.2. **NEXT:** F02.0. **TRANSITION INTO CURRENT:** Straight radial lines are replaced/extended by curved inter-body lines and arrowheads; all non-field elements remain registered. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A02:** replacement field drawing; V02/F01.1 → V03/F01.2; 00:02.125; target curved Earth–Moon field lines; relationship STATE REPLACEMENT.

### 17. WHY MOVE

**A02 — WHY:** Shows the charged bodies as an interacting system. **Direction:** curving between and around the bodies follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** single-frame graphic change; amplitude/path nested arcs; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** curved Earth–Moon field lines. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A02: STATE REPLACEMENT** because shows the charged bodies as an interacting system.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWINGS. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A02 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A02 PASS:** source V02/F01.1; animate only curved Earth–Moon field lines; target region X 7–91, Y 5–38; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A02 SOURCE FRAME STATE:** V02/F01.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V02. **SOURCE IMAGE PROMPT:** build V02 as a 720×1280 text-free hand-drawn clean plate: The same board and presenter remain fixed while straight black arrows radiate outward from the now densely stippled Earth. Layout: Preserve V01 exactly; arrows occupy the board around Earth from approximately X 8–70/Y 7–37 without entering the presenter region. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A02

**SOURCE STATE:** V02/F01.1  
**TARGET STATE:** V03/F01.2  
**TIMESTAMP:** 00:02.125  
**MOTION TYPE:** replacement field drawing  
**MOTION HERO / ALLOWED MOTION:** curved Earth–Moon field lines  
**START STATE:** V02, matching the source description above.  
**END STATE:** V03, matching this card’s target configuration.  
**DIRECTION:** curving between and around the bodies  
**SPEED:** single-frame graphic change  
**AMPLITUDE / PATH:** nested arcs; ROI X 7–91, Y 5–38  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:02.125.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWINGS. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Replace only the straight field drawing with the observed curved field-line network wrapping between Earth and Moon. Keep both spheres, EARTH and MOON labels, dashed orbit, board, presenter and white background perfectly registered. Hold on the completed line pattern.”  
**CHARACTER COUNT:** 283 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A02: duplicate the stable source precomp; isolate X 7–91, Y 5–38; execute REPLACEMENT DRAWINGS; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 05.458s, then use a hard cut into V04. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V03 as the exact observed state: curved electric-field topology is the visual hero, board/presenter is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V04 — 06.500s — Destructive flash

**SHOT:** S02  
**SOURCE REFERENCE FRAME:** [V04_0006500ms.jpg](moon_protons_forensics/keyframes/V04_0006500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 05.458s / 06.500s  
**DURATION TO NEXT MATERIAL STATE:** 2.542s  
**STATE ID:** F02.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a bright circular white blast dominates the upper-middle frame, surrounded by hand-drawn rays and gray falloff; the presenter recoils at lower left and board fragments angle inward from the edges. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A bright circular white blast dominates the upper-middle frame, surrounded by hand-drawn rays and gray falloff; the presenter recoils at lower left and board fragments angle inward from the edges. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “This is, by far, the most destructive what-if scenario to date.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** This is, by far, the most destructive what-if.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Immediate pattern break and consequence preview.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut replaces the whiteboard tableau with a full-frame impact illustration.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Immediate pattern break and consequence preview. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** central blast.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: No overlay text in this state.  
**VISUAL HERO:** central blast.  
**STATIC COORDINATE FRAME:** blast center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Blast center near X 59/Y 29 at about 24% frame width; presenter is cropped along left at X 0–28/Y 53–93; diagonal debris enters from all four sides; gray vignette fills the portrait frame. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** central blast → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** central blast. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F02.0 within S02. **CHANGES:** Hard cut replaces the whiteboard tableau with a full-frame impact illustration. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A bright circular white blast dominates the upper-middle frame, surrounded by hand-drawn rays and gray falloff; the presenter recoils at lower left and board fragments angle inward from the edges. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white core, light-to-mid gray vignette, black line fragments. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A bright circular white blast dominates the upper-middle frame, surrounded by hand-drawn rays and gray falloff; the presenter recoils at lower left and board fragments angle inward from the edges. Exact composition: Blast center near X 59/Y 29 at about 24% frame width; presenter is cropped along left at X 0–28/Y 53–93; diagonal debris enters from all four sides; gray vignette fills the portrait frame. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white core, light-to-mid gray vignette, black line fragments. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F02.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** No overlay text in this state. Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white core, light-to-mid gray vignette, black line fragments), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F02.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Destructive flash. **SHOT MEMBERSHIP:** S02 (5.458–8.000).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F01.2. **CURRENT:** F02.0. **NEXT:** F03.0. **TRANSITION INTO CURRENT:** Hard cut replaces the whiteboard tableau with a full-frame impact illustration. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** blast center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F02.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.542s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 08.000s, then use a hard cut into V05. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V04 as the exact observed state: central blast is the visual hero, blast center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V05 — 09.000s — Macroscopic orbit

**SHOT:** S03  
**SOURCE REFERENCE FRAME:** [V05_0009000ms.jpg](moon_protons_forensics/keyframes/V05_0009000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 08.000s / 09.000s  
**DURATION TO NEXT MATERIAL STATE:** 2.167s  
**STATE ID:** F03.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see on white, a large stippled sphere sits high-left of a small stippled sphere, enclosed by a dashed circular orbital guide. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** On white, a large stippled sphere sits high-left of a small stippled sphere, enclosed by a dashed circular orbital guide. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “You might imagine an electron moon orbiting a proton Earth”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** You might imagine an electron moon orbiting a.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Present the intuitive macro-orbit model cleanly before introducing its analogy.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut from the blast to a minimal clean diagram.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Present the intuitive macro-orbit model cleanly before introducing its analogy. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** upper two-body system.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: No overlay text in this state.  
**VISUAL HERO:** upper two-body system.  
**STATIC COORDINATE FRAME:** upper/lower diagram coordinates.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Diagram occupies upper half only; primary sphere near X 46/Y 19 at 20% width; secondary near X 72/Y 20 at 8%; dashed orbit spans X 21–79/Y 4–35; lower half is empty. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** upper two-body system → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** upper two-body system. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F03.0 within S03. **CHANGES:** Hard cut from the blast to a minimal clean diagram. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** On white, a large stippled sphere sits high-left of a small stippled sphere, enclosed by a dashed circular orbital guide. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray stipple. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. On white, a large stippled sphere sits high-left of a small stippled sphere, enclosed by a dashed circular orbital guide. Exact composition: Diagram occupies upper half only; primary sphere near X 46/Y 19 at 20% width; secondary near X 72/Y 20 at 8%; dashed orbit spans X 21–79/Y 4–35; lower half is empty. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray stipple. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F03.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** No overlay text in this state. Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray stipple), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F03.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Macroscopic orbit. **SHOT MEMBERSHIP:** S03 (8.000–19.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F02.0. **CURRENT:** F03.0. **NEXT:** F03.1. **TRANSITION INTO CURRENT:** Hard cut from the blast to a minimal clean diagram. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** upper/lower diagram coordinates; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F03.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.167s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 10.167s, then use a local additive/replacement event into V06. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V05 as the exact observed state: upper two-body system is the visual hero, upper/lower diagram coordinates is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V06 — 11.500s — Atomic analogue added

**SHOT:** S03  
**SOURCE REFERENCE FRAME:** [V06_0011500ms.jpg](moon_protons_forensics/keyframes/V06_0011500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 10.167s / 11.500s  
**DURATION TO NEXT MATERIAL STATE:** 3.250s  
**STATE ID:** F03.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the macro orbit remains above while a plus-sign nucleus, tiny electron, and second dashed orbit appear in the lower half. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The macro orbit remains above while a plus-sign nucleus, tiny electron, and second dashed orbit appear in the lower half. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “sort of like a gigantic hydrogen atom”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** sort of like a gigantic hydrogen atom.  
**MOTION CUE:** A03  
**FUNCTION:** Build a vertical visual analogy: celestial orbit above, atomic orbit below.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Lower atomic diagram is added; upper system stays pixel-registered.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Build a vertical visual analogy: celestial orbit above, atomic orbit below. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** two-level macro/atomic comparison.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: plus sign; electron symbol  
**VISUAL HERO:** two-level macro/atomic comparison.  
**STATIC COORDINATE FRAME:** upper/lower diagram coordinates.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Upper system remains V05; lower nucleus centers near X 49/Y 69 at 9% width, electron near X 74/Y 69 at 3%, dashed orbit spans X 26–79/Y 53–82. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** two-level macro/atomic comparison → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** two-level macro/atomic comparison. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** MODIFIED REUSE / ANIMATION END STATE. **BASE:** F03.1 within S03. **CHANGES:** Lower atomic diagram is added; upper system stays pixel-registered. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The macro orbit remains above while a plus-sign nucleus, tiny electron, and second dashed orbit appear in the lower half. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The macro orbit remains above while a plus-sign nucleus, tiny electron, and second dashed orbit appear in the lower half. Exact composition: Upper system remains V05; lower nucleus centers near X 49/Y 69 at 9% width, electron near X 74/Y 69 at 3%, dashed orbit spans X 26–79/Y 53–82. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F03.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** plus sign; electron symbol Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F03.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Atomic analogue added. **SHOT MEMBERSHIP:** S03 (8.000–19.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F03.0. **CURRENT:** F03.1. **NEXT:** F03.2. **TRANSITION INTO CURRENT:** Lower atomic diagram is added; upper system stays pixel-registered. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A03:** additive diagram reveal; V05/F03.0 → V06/F03.1; 00:10.167; target lower proton/electron orbit analogy; relationship SEQUENTIAL.

### 17. WHY MOVE

**A03 — WHY:** Creates the macro-versus-atomic comparison. **Direction:** appears in lower half follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** one-step reveal; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** upper/lower diagram coordinates; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** lower proton/electron orbit analogy. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A03: SEQUENTIAL** because creates the macro-versus-atomic comparison.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** VECTOR MOTION / opacity or replacement drawing. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A03 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A03 PASS:** source V05/F03.0; animate only lower proton/electron orbit analogy; target region X 25–80, Y 52–83; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A03 SOURCE FRAME STATE:** V05/F03.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V05. **SOURCE IMAGE PROMPT:** build V05 as a 720×1280 text-free hand-drawn clean plate: On white, a large stippled sphere sits high-left of a small stippled sphere, enclosed by a dashed circular orbital guide. Layout: Diagram occupies upper half only; primary sphere near X 46/Y 19 at 20% width; secondary near X 72/Y 20 at 8%; dashed orbit spans X 21–79/Y 4–35; lower half is empty. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A03

**SOURCE STATE:** V05/F03.0  
**TARGET STATE:** V06/F03.1  
**TIMESTAMP:** 00:10.167  
**MOTION TYPE:** additive diagram reveal  
**MOTION HERO / ALLOWED MOTION:** lower proton/electron orbit analogy  
**START STATE:** V05, matching the source description above.  
**END STATE:** V06, matching this card’s target configuration.  
**DIRECTION:** appears in lower half  
**SPEED:** one-step reveal  
**AMPLITUDE / PATH:** none; ROI X 25–80, Y 52–83  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:10.167.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** VECTOR MOTION / opacity or replacement drawing. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the lower atomic diagram in one clean step: a central plus-sign nucleus, tiny electron and dashed circular orbit. Preserve the upper Earth–Moon diagram, its scale and position, and all white negative space. End with both stacked systems fully visible.”  
**CHARACTER COUNT:** 278 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A03: duplicate the stable source precomp; isolate X 25–80, Y 52–83; execute VECTOR MOTION / opacity or replacement drawing; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 13.417s, then use a local additive/replacement event into V07. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V06 as the exact observed state: two-level macro/atomic comparison is the visual hero, upper/lower diagram coordinates is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V07 — 13.750s — Atomic ORBIT label

**SHOT:** S03  
**SOURCE REFERENCE FRAME:** [V07_0013750ms.jpg](moon_protons_forensics/keyframes/V07_0013750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 13.417s / 13.750s  
**DURATION TO NEXT MATERIAL STATE:** 1.250s  
**STATE ID:** F03.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the two stacked orbit diagrams remain unchanged and a hand-lettered ORBIT label appears above the lower atomic orbit. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The two stacked orbit diagrams remain unchanged and a hand-lettered ORBIT label appears above the lower atomic orbit. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “On one level, it sort of makes sense.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** On one level, it sort of makes sense..  
**MOTION CUE:** A04  
**FUNCTION:** Name the shared surface feature and guide comparison.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the lower label is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Name the shared surface feature and guide comparison. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** lower ORBIT label.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: ‘ORBIT’ above lower diagram  
**VISUAL HERO:** lower ORBIT label.  
**STATIC COORDINATE FRAME:** upper/lower diagram coordinates.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Label centers near X 50/Y 54, directly above the lower dashed circle; all diagrams retain V06 positions. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** lower ORBIT label → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** lower ORBIT label. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F03.2 within S03. **CHANGES:** Only the lower label is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The two stacked orbit diagrams remain unchanged and a hand-lettered ORBIT label appears above the lower atomic orbit. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The two stacked orbit diagrams remain unchanged and a hand-lettered ORBIT label appears above the lower atomic orbit. Exact composition: Label centers near X 50/Y 54, directly above the lower dashed circle; all diagrams retain V06 positions. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F03.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** ‘ORBIT’ above lower diagram Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F03.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Atomic ORBIT label. **SHOT MEMBERSHIP:** S03 (8.000–19.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F03.1. **CURRENT:** F03.2. **NEXT:** F03.3. **TRANSITION INTO CURRENT:** Only the lower label is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A04:** text reveal; V06/F03.1 → V07/F03.2; 00:13.417; target lower ORBIT label; relationship SEQUENTIAL.

### 17. WHY MOVE

**A04 — WHY:** Names the shared relationship under discussion. **Direction:** appears above lower orbit follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant pop; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** upper/lower diagram coordinates; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** lower ORBIT label. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A04: SEQUENTIAL** because names the shared relationship under discussion.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A04 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A04 PASS:** source V06/F03.1; animate only lower ORBIT label; target region X 40–60, Y 51–57; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A04 SOURCE FRAME STATE:** V06/F03.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V06. **SOURCE IMAGE PROMPT:** build V06 as a 720×1280 text-free hand-drawn clean plate: The macro orbit remains above while a plus-sign nucleus, tiny electron, and second dashed orbit appear in the lower half. Layout: Upper system remains V05; lower nucleus centers near X 49/Y 69 at 9% width, electron near X 74/Y 69 at 3%, dashed orbit spans X 26–79/Y 53–82. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A04

**SOURCE STATE:** V06/F03.1  
**TARGET STATE:** V07/F03.2  
**TIMESTAMP:** 00:13.417  
**MOTION TYPE:** text reveal  
**MOTION HERO / ALLOWED MOTION:** lower ORBIT label  
**START STATE:** V06, matching the source description above.  
**END STATE:** V07, matching this card’s target configuration.  
**DIRECTION:** appears above lower orbit  
**SPEED:** instant pop  
**AMPLITUDE / PATH:** none; ROI X 40–60, Y 51–57  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:13.417.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the hand-lettered word ‘ORBIT’ above the lower atomic orbit with an immediate clean pop. Keep both orbit diagrams, spheres, dashed paths, symbols, scale, crop and white background unchanged. Hold the label.”  
**CHARACTER COUNT:** 233 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A04: duplicate the stable source precomp; isolate X 40–60, Y 51–57; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 14.667s, then use a local additive/replacement event into V08. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V07 as the exact observed state: lower ORBIT label is the visual hero, upper/lower diagram coordinates is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V08 — 15.250s — Both systems labeled ORBIT

**SHOT:** S03  
**SOURCE REFERENCE FRAME:** [V08_0015250ms.jpg](moon_protons_forensics/keyframes/V08_0015250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 14.667s / 15.250s  
**DURATION TO NEXT MATERIAL STATE:** 1.875s  
**STATE ID:** F03.3

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see both stacked systems are now labeled ORBIT, with the upper label centered near the top margin and the lower label preserved. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** Both stacked systems are now labeled ORBIT, with the upper label centered near the top margin and the lower label preserved. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “Electrons orbit protons, and moons orbit planets.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** Electrons orbit protons, and moons orbit planets..  
**MOTION CUE:** A05  
**FUNCTION:** Complete the apparent parallel before the reversal.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the upper ORBIT label is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Complete the apparent parallel before the reversal. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** paired labels.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: ORBIT; ‘ORBIT’  
**VISUAL HERO:** paired labels.  
**STATIC COORDINATE FRAME:** upper/lower diagram coordinates.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Upper label centers X 50/Y 6; lower label centers X 50/Y 54; diagrams stay fixed. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** paired labels → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** paired labels. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F03.3 within S03. **CHANGES:** Only the upper ORBIT label is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Both stacked systems are now labeled ORBIT, with the upper label centered near the top margin and the lower label preserved. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. Both stacked systems are now labeled ORBIT, with the upper label centered near the top margin and the lower label preserved. Exact composition: Upper label centers X 50/Y 6; lower label centers X 50/Y 54; diagrams stay fixed. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F03.3, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** ORBIT; ‘ORBIT’ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F03.3. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Both systems labeled ORBIT. **SHOT MEMBERSHIP:** S03 (8.000–19.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F03.2. **CURRENT:** F03.3. **NEXT:** F03.4. **TRANSITION INTO CURRENT:** Only the upper ORBIT label is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A05:** text reveal; V07/F03.2 → V08/F03.3; 00:14.667; target upper ORBIT label; relationship SEQUENTIAL.

### 17. WHY MOVE

**A05 — WHY:** Completes the apparent analogy before its rejection. **Direction:** appears above upper orbit follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant pop; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** upper/lower diagram coordinates; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** upper ORBIT label. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A05: SEQUENTIAL** because completes the apparent analogy before its rejection.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A05 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A05 PASS:** source V07/F03.2; animate only upper ORBIT label; target region X 40–60, Y 3–9; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A05 SOURCE FRAME STATE:** V07/F03.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V07. **SOURCE IMAGE PROMPT:** build V07 as a 720×1280 text-free hand-drawn clean plate: The two stacked orbit diagrams remain unchanged and a hand-lettered ORBIT label appears above the lower atomic orbit. Layout: Label centers near X 50/Y 54, directly above the lower dashed circle; all diagrams retain V06 positions. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A05

**SOURCE STATE:** V07/F03.2  
**TARGET STATE:** V08/F03.3  
**TIMESTAMP:** 00:14.667  
**MOTION TYPE:** text reveal  
**MOTION HERO / ALLOWED MOTION:** upper ORBIT label  
**START STATE:** V07, matching the source description above.  
**END STATE:** V08, matching this card’s target configuration.  
**DIRECTION:** appears above upper orbit  
**SPEED:** instant pop  
**AMPLITUDE / PATH:** none; ROI X 40–60, Y 3–9  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:14.667.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the hand-lettered word ORBIT above the upper Earth–Moon system with an immediate clean pop. Preserve the lower ‘ORBIT’ label and both diagrams exactly in place. Keep the white background and frame locked, then hold.”  
**CHARACTER COUNT:** 242 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A05: duplicate the stable source precomp; isolate X 40–60, Y 3–9; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 16.542s, then use a local additive/replacement event into V09. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V08 as the exact observed state: paired labels is the visual hero, upper/lower diagram coordinates is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V09 — 18.000s — Macro analogy struck out

**SHOT:** S03  
**SOURCE REFERENCE FRAME:** [V09_0018000ms.jpg](moon_protons_forensics/keyframes/V09_0018000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 16.542s / 18.000s  
**DURATION TO NEXT MATERIAL STATE:** 3.000s  
**STATE ID:** F03.4

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see loose red diagonal loops cross out both upper spheres while the lower atomic orbit and both ORBIT labels remain intact. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** Loose red diagonal loops cross out both upper spheres while the lower atomic orbit and both ORBIT labels remain intact. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “However, electron moons do not orbit proton planets.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** However, electron moons do not orbit proton planets..  
**MOTION CUE:** A06  
**FUNCTION:** Visual contradiction: preserve the atomic truth while rejecting the macro inference.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Red strike-through loops are added over upper Earth and Moon only.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Visual contradiction: preserve the atomic truth while rejecting the macro inference. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** scarce red contradiction mark.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: ORBIT; ‘ORBIT’  
**VISUAL HERO:** scarce red contradiction mark.  
**STATIC COORDINATE FRAME:** upper/lower diagram coordinates.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Red strokes occupy X 31–83/Y 8–34 over only the upper system; lower system stays untouched and centered. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** scarce red contradiction mark → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** scarce red contradiction mark. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F03.4 within S03. **CHANGES:** Red strike-through loops are added over upper Earth and Moon only. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Loose red diagonal loops cross out both upper spheres while the lower atomic orbit and both ORBIT labels remain intact. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray, saturated red accent. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. Loose red diagonal loops cross out both upper spheres while the lower atomic orbit and both ORBIT labels remain intact. Exact composition: Red strokes occupy X 31–83/Y 8–34 over only the upper system; lower system stays untouched and centered. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray, saturated red accent. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F03.4, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** ORBIT; ‘ORBIT’ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray, saturated red accent), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F03.4. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Macro analogy struck out. **SHOT MEMBERSHIP:** S03 (8.000–19.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F03.3. **CURRENT:** F03.4. **NEXT:** F04.0. **TRANSITION INTO CURRENT:** Red strike-through loops are added over upper Earth and Moon only. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A06:** red scribble reveal; V08/F03.3 → V09/F03.4; 00:16.542; target red strike-through loops over upper system; relationship SEQUENTIAL.

### 17. WHY MOVE

**A06 — WHY:** Rejects the macro analogy while leaving the atomic diagram valid. **Direction:** diagonal loops across both upper spheres follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** fast one-beat draw; amplitude/path irregular diagonal loops; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** upper/lower diagram coordinates; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** red strike-through loops over upper system. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A06: SEQUENTIAL** because rejects the macro analogy while leaving the atomic diagram valid.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** VECTOR TRIM PATH / hand-drawn overlay. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A06 MEDIUM. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A06 PASS:** source V08/F03.3; animate only red strike-through loops over upper system; target region X 30–84, Y 7–35; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A06 SOURCE FRAME STATE:** V08/F03.3. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V08. **SOURCE IMAGE PROMPT:** build V08 as a 720×1280 text-free hand-drawn clean plate: Both stacked systems are now labeled ORBIT, with the upper label centered near the top margin and the lower label preserved. Layout: Upper label centers X 50/Y 6; lower label centers X 50/Y 54; diagrams stay fixed. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A06

**SOURCE STATE:** V08/F03.3  
**TARGET STATE:** V09/F03.4  
**TIMESTAMP:** 00:16.542  
**MOTION TYPE:** red scribble reveal  
**MOTION HERO / ALLOWED MOTION:** red strike-through loops over upper system  
**START STATE:** V08, matching the source description above.  
**END STATE:** V09, matching this card’s target configuration.  
**DIRECTION:** diagonal loops across both upper spheres  
**SPEED:** fast one-beat draw  
**AMPLITUDE / PATH:** irregular diagonal loops; ROI X 30–84, Y 7–35  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:16.542.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** VECTOR TRIM PATH / hand-drawn overlay. **AI SUITABILITY:** MEDIUM.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Draw only the observed loose red strike-through loops across the upper Earth and Moon in a quick single beat, then hold. Preserve both ORBIT labels, the lower atomic system, dashed paths, sphere geometry and white background exactly. No camera movement.”  
**CHARACTER COUNT:** 268 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A06: duplicate the stable source precomp; isolate X 30–84, Y 7–35; execute VECTOR TRIM PATH / hand-drawn overlay; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 19.542s, then use a hard cut into V10. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V09 as the exact observed state: scarce red contradiction mark is the visual hero, upper/lower diagram coordinates is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V10 — 20.500s — Two electrons

**SHOT:** S04  
**SOURCE REFERENCE FRAME:** [V10_0020500ms.jpg](moon_protons_forensics/keyframes/V10_0020500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 19.542s / 20.500s  
**DURATION TO NEXT MATERIAL STATE:** 1.916s  
**STATE ID:** F04.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see two small electron symbols sit on a blank white field, vertically separated along the frame centerline. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** Two small electron symbols sit on a blank white field, vertically separated along the frame centerline. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “If you put two negatively charged electrons together”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** If you put two negatively charged electrons together.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Reduce the problem to a minimal pair that can be quantitatively compared.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut clears the prior orbit analogy and introduces two isolated particles.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Reduce the problem to a minimal pair that can be quantitatively compared. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** two electron symbols.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: electron symbols  
**VISUAL HERO:** two electron symbols.  
**STATIC COORDINATE FRAME:** vertical particle axis.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Upper electron near X 50/Y 37; lower electron near X 50/Y 64; each about 4% frame width; otherwise empty white space. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** two electron symbols → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** two electron symbols. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F04.0 within S04. **CHANGES:** Hard cut clears the prior orbit analogy and introduces two isolated particles. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Two small electron symbols sit on a blank white field, vertically separated along the frame centerline. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. Two small electron symbols sit on a blank white field, vertically separated along the frame centerline. Exact composition: Upper electron near X 50/Y 37; lower electron near X 50/Y 64; each about 4% frame width; otherwise empty white space. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F04.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** electron symbols Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F04.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Two electrons. **SHOT MEMBERSHIP:** S04 (19.542–26.250).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F03.4. **CURRENT:** F04.0. **NEXT:** F04.1. **TRANSITION INTO CURRENT:** Hard cut clears the prior orbit analogy and introduces two isolated particles. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** vertical particle axis; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F04.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 1.916s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 21.458s, then use a local additive/replacement event into V11. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V10 as the exact observed state: two electron symbols is the visual hero, vertical particle axis is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V11 — 21.750s — Opposing repulsion arrows

**SHOT:** S04  
**SOURCE REFERENCE FRAME:** [V11_0021750ms.jpg](moon_protons_forensics/keyframes/V11_0021750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 21.458s / 21.750s  
**DURATION TO NEXT MATERIAL STATE:** 1.292s  
**STATE ID:** F04.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a long outlined arrow rises from the upper electron and a matching arrow points downward from the lower electron. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A long outlined arrow rises from the upper electron and a matching arrow points downward from the lower electron. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “they try to fly apart with a force”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** they try to fly apart with a force.  
**MOTION CUE:** A07  
**FUNCTION:** Make force direction immediately legible.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Two equal-looking arrows are added, pointing away from the pair’s center.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Make force direction immediately legible. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** opposed force arrows.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: electron symbols  
**VISUAL HERO:** opposed force arrows.  
**STATIC COORDINATE FRAME:** vertical particle axis.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Arrows align on X 50; upper extends Y 8–35, lower Y 67–94; particles remain at their V10 coordinates. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** opposed force arrows → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** opposed force arrows. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F04.1 within S04. **CHANGES:** Two equal-looking arrows are added, pointing away from the pair’s center. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A long outlined arrow rises from the upper electron and a matching arrow points downward from the lower electron. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A long outlined arrow rises from the upper electron and a matching arrow points downward from the lower electron. Exact composition: Arrows align on X 50; upper extends Y 8–35, lower Y 67–94; particles remain at their V10 coordinates. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F04.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** electron symbols Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F04.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Opposing repulsion arrows. **SHOT MEMBERSHIP:** S04 (19.542–26.250).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F04.0. **CURRENT:** F04.1. **NEXT:** F04.2. **TRANSITION INTO CURRENT:** Two equal-looking arrows are added, pointing away from the pair’s center. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A07:** opposed arrow reveal; V10/F04.0 → V11/F04.1; 00:21.458; target two long force arrows; relationship SIMULTANEOUS COUPLED.

### 17. WHY MOVE

**A07 — WHY:** Makes equal-and-opposite repulsion direction legible. **Direction:** upper arrow up, lower arrow down follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant/additive; amplitude/path straight vertical; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** vertical particle axis; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** two long force arrows. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A07: SIMULTANEOUS COUPLED** because makes equal-and-opposite repulsion direction legible.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** VECTOR MOTION / trim paths. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A07 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A07 PASS:** source V10/F04.0; animate only two long force arrows; target region X 43–57, Y 8–94; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A07 SOURCE FRAME STATE:** V10/F04.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V10. **SOURCE IMAGE PROMPT:** build V10 as a 720×1280 text-free hand-drawn clean plate: Two small electron symbols sit on a blank white field, vertically separated along the frame centerline. Layout: Upper electron near X 50/Y 37; lower electron near X 50/Y 64; each about 4% frame width; otherwise empty white space. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A07

**SOURCE STATE:** V10/F04.0  
**TARGET STATE:** V11/F04.1  
**TIMESTAMP:** 00:21.458  
**MOTION TYPE:** opposed arrow reveal  
**MOTION HERO / ALLOWED MOTION:** two long force arrows  
**START STATE:** V10, matching the source description above.  
**END STATE:** V11, matching this card’s target configuration.  
**DIRECTION:** upper arrow up, lower arrow down  
**SPEED:** instant/additive  
**AMPLITUDE / PATH:** straight vertical; ROI X 43–57, Y 8–94  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:21.458.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** VECTOR MOTION / trim paths. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal the two outlined force arrows together: the upper arrow extends straight upward from the upper electron and the lower arrow extends straight downward from the lower electron. Keep both particles and the white frame fixed. Complete once and hold.”  
**CHARACTER COUNT:** 267 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A07: duplicate the stable source precomp; isolate X 43–57, Y 8–94; execute VECTOR MOTION / trim paths; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 22.750s, then use a local additive/replacement event into V12. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V11 as the exact observed state: opposed force arrows is the visual hero, vertical particle axis is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V12 — 23.250s — Twenty-order multiplier

**SHOT:** S04  
**SOURCE REFERENCE FRAME:** [V12_0023250ms.jpg](moon_protons_forensics/keyframes/V12_0023250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 22.750s / 23.250s  
**DURATION TO NEXT MATERIAL STATE:** 1.792s  
**STATE ID:** F04.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the opposed arrows and electrons hold while 10²⁰ appears beside the lower arrow. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The opposed arrows and electrons hold while 10²⁰ appears beside the lower arrow. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “about 20 orders of magnitude stronger”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** about 20 orders of magnitude stronger.  
**MOTION CUE:** A08  
**FUNCTION:** Translate narration into a memorable numerical asymmetry.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the 10²⁰ multiplier is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Translate narration into a memorable numerical asymmetry. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** 10²⁰.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: 10²⁰  
**VISUAL HERO:** 10²⁰.  
**STATIC COORDINATE FRAME:** vertical particle axis.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Multiplier sits right of lower arrow near X 59/Y 76; arrows and particles remain registered. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** 10²⁰ → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** 10²⁰. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F04.2 within S04. **CHANGES:** Only the 10²⁰ multiplier is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The opposed arrows and electrons hold while 10²⁰ appears beside the lower arrow. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The opposed arrows and electrons hold while 10²⁰ appears beside the lower arrow. Exact composition: Multiplier sits right of lower arrow near X 59/Y 76; arrows and particles remain registered. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F04.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** 10²⁰ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F04.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Twenty-order multiplier. **SHOT MEMBERSHIP:** S04 (19.542–26.250).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F04.1. **CURRENT:** F04.2. **NEXT:** F04.3. **TRANSITION INTO CURRENT:** Only the 10²⁰ multiplier is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A08:** number reveal; V11/F04.1 → V12/F04.2; 00:22.750; target 10²⁰ multiplier; relationship SEQUENTIAL.

### 17. WHY MOVE

**A08 — WHY:** Quantifies the force ratio. **Direction:** appears right of lower arrow follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant pop; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** vertical particle axis; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** 10²⁰ multiplier. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A08: SEQUENTIAL** because quantifies the force ratio.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A08 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A08 PASS:** source V11/F04.1; animate only 10²⁰ multiplier; target region X 56–69, Y 72–82; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A08 SOURCE FRAME STATE:** V11/F04.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V11. **SOURCE IMAGE PROMPT:** build V11 as a 720×1280 text-free hand-drawn clean plate: A long outlined arrow rises from the upper electron and a matching arrow points downward from the lower electron. Layout: Arrows align on X 50; upper extends Y 8–35, lower Y 67–94; particles remain at their V10 coordinates. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A08

**SOURCE STATE:** V11/F04.1  
**TARGET STATE:** V12/F04.2  
**TIMESTAMP:** 00:22.750  
**MOTION TYPE:** number reveal  
**MOTION HERO / ALLOWED MOTION:** 10²⁰ multiplier  
**START STATE:** V11, matching the source description above.  
**END STATE:** V12, matching this card’s target configuration.  
**DIRECTION:** appears right of lower arrow  
**SPEED:** instant pop  
**AMPLITUDE / PATH:** none; ROI X 56–69, Y 72–82  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:22.750.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the exact multiplier 10²⁰ beside the lower arrow with a clean one-step pop. Keep both electrons, both arrows, their alignment, line weight, white background and all spacing unchanged. Hold the number legibly.”  
**CHARACTER COUNT:** 235 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A08: duplicate the stable source precomp; isolate X 56–69, Y 72–82; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 24.542s, then use a local additive/replacement event into V13. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V12 as the exact observed state: 10²⁰ is the visual hero, vertical particle axis is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V13 — 25.250s — Force comparison completed

**SHOT:** S04  
**SOURCE REFERENCE FRAME:** [V13_0025250ms.jpg](moon_protons_forensics/keyframes/V13_0025250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 24.542s / 25.250s  
**DURATION TO NEXT MATERIAL STATE:** 1.708s  
**STATE ID:** F04.3

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the central particles gain opposed small force arrows and F labels while the lower multiplier becomes 10²⁰·F. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The central particles gain opposed small force arrows and F labels while the lower multiplier becomes 10²⁰·F. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “than the gravity pulling them together”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** than the gravity pulling them together.  
**MOTION CUE:** A09  
**FUNCTION:** Complete the explanatory proof without changing the force diagram’s coordinate frame.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** F labels and central direction marks are added; 10²⁰ is completed as 10²⁰·F.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Complete the explanatory proof without changing the force diagram’s coordinate frame. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** force equations.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: F; 10²⁰·F  
**VISUAL HERO:** force equations.  
**STATIC COORDINATE FRAME:** vertical particle axis.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Tiny comparison marks occupy X 46–55/Y 48–56; lower equation remains beside the lower arrow near X 58/Y 76. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** force equations → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** force equations. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT + GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F04.3 within S04. **CHANGES:** F labels and central direction marks are added; 10²⁰ is completed as 10²⁰·F. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The central particles gain opposed small force arrows and F labels while the lower multiplier becomes 10²⁰·F. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The central particles gain opposed small force arrows and F labels while the lower multiplier becomes 10²⁰·F. Exact composition: Tiny comparison marks occupy X 46–55/Y 48–56; lower equation remains beside the lower arrow near X 58/Y 76. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F04.3, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** F; 10²⁰·F Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F04.3. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Force comparison completed. **SHOT MEMBERSHIP:** S04 (19.542–26.250).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F04.2. **CURRENT:** F04.3. **NEXT:** F05.0. **TRANSITION INTO CURRENT:** F labels and central direction marks are added; 10²⁰ is completed as 10²⁰·F. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A09:** equation and force-label reveal; V12/F04.2 → V13/F04.3; 00:24.542; target central F marks and 10²⁰·F completion; relationship SEQUENTIAL.

### 17. WHY MOVE

**A09 — WHY:** Completes the quantitative proof. **Direction:** appears near center and lower arrow follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** one-step reveal; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** vertical particle axis; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** central F marks and 10²⁰·F completion. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A09: SEQUENTIAL** because completes the quantitative proof.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT + VECTOR OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A09 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A09 PASS:** source V12/F04.2; animate only central F marks and 10²⁰·F completion; target region X 44–72, Y 45–82; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A09 SOURCE FRAME STATE:** V12/F04.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V12. **SOURCE IMAGE PROMPT:** build V12 as a 720×1280 text-free hand-drawn clean plate: The opposed arrows and electrons hold while 10²⁰ appears beside the lower arrow. Layout: Multiplier sits right of lower arrow near X 59/Y 76; arrows and particles remain registered. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A09

**SOURCE STATE:** V12/F04.2  
**TARGET STATE:** V13/F04.3  
**TIMESTAMP:** 00:24.542  
**MOTION TYPE:** equation and force-label reveal  
**MOTION HERO / ALLOWED MOTION:** central F marks and 10²⁰·F completion  
**START STATE:** V12, matching the source description above.  
**END STATE:** V13, matching this card’s target configuration.  
**DIRECTION:** appears near center and lower arrow  
**SPEED:** one-step reveal  
**AMPLITUDE / PATH:** none; ROI X 44–72, Y 45–82  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:24.542.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT + VECTOR OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Add only the observed central force marks and F labels, and complete the lower expression as 10²⁰·F. Preserve both electrons, long arrows, exact vertical alignment, white background and all existing geometry. Hold the finished comparison.”  
**CHARACTER COUNT:** 253 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A09: duplicate the stable source precomp; isolate X 44–72, Y 45–82; execute EDITOR TEXT + VECTOR OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 26.250s, then use a hard cut into V14. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V13 as the exact observed state: force equations is the visual hero, vertical particle axis is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V14 — 27.250s — Electron-Moon calculation

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V14_0027250ms.jpg](moon_protons_forensics/keyframes/V14_0027250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 26.250s / 27.250s  
**DURATION TO NEXT MATERIAL STATE:** 2.042s  
**STATE ID:** F05.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the presenter stands below a whiteboard bearing a red ‘200,000 MOLES OF MOLES’ note, a 10⁵³-electron cluster, a Moon-mass relation, and a small Earth cross-section. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** The presenter stands below a whiteboard bearing a red ‘200,000 MOLES OF MOLES’ note, a 10⁵³-electron cluster, a Moon-mass relation, and a small Earth cross-section. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “If you put 10 to the 53 electrons together to build a moon”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** If you put 10 to the 53 electrons.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Scale the two-particle force result into the Moon-sized object.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut returns to the recurring board/presenter environment with a new calculation.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Scale the two-particle force result into the Moon-sized object. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** 10⁵³ electron cluster.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: 200,000 MOLES OF MOLES; 10⁵³·e⁻; M_MOON ≈ 10⁵³·m_e  
**VISUAL HERO:** 10⁵³ electron cluster.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Board occupies Y 6–42; red heading X 9–39/Y 18–24; electron cluster X 43–59/Y 19–27; equation X 36–66/Y 30; Earth arc X 26–79/Y 35–40; presenter X 12–36/Y 51–92. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** 10⁵³ electron cluster → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** 10⁵³ electron cluster. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE WITH REUSED E01/C01. **BASE:** F05.0 within S05. **CHANGES:** Hard cut returns to the recurring board/presenter environment with a new calculation. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The presenter stands below a whiteboard bearing a red ‘200,000 MOLES OF MOLES’ note, a 10⁵³-electron cluster, a Moon-mass relation, and a small Earth cross-section. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray, red heading. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The presenter stands below a whiteboard bearing a red ‘200,000 MOLES OF MOLES’ note, a 10⁵³-electron cluster, a Moon-mass relation, and a small Earth cross-section. Exact composition: Board occupies Y 6–42; red heading X 9–39/Y 18–24; electron cluster X 43–59/Y 19–27; equation X 36–66/Y 30; Earth arc X 26–79/Y 35–40; presenter X 12–36/Y 51–92. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray, red heading. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** 200,000 MOLES OF MOLES; 10⁵³·e⁻; M_MOON ≈ 10⁵³·m_e Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray, red heading), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Electron-Moon calculation. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F04.3. **CURRENT:** F05.0. **NEXT:** F05.1. **TRANSITION INTO CURRENT:** Hard cut returns to the recurring board/presenter environment with a new calculation. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F05.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.042s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 28.292s, then use a local additive/replacement event into V15. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V14 as the exact observed state: 10⁵³ electron cluster is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V15 — 28.750s — UH OH reaction

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V15_0028750ms.jpg](moon_protons_forensics/keyframes/V15_0028750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 28.292s / 28.750s  
**DURATION TO NEXT MATERIAL STATE:** 0.791s  
**STATE ID:** F05.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the calculation remains unchanged while UH OH appears above the presenter’s head. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The calculation remains unchanged while UH OH appears above the presenter’s head. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “they push each other apart with an unbelievable amount of energy”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** they push each other apart with an unbelievable.  
**MOTION CUE:** A10  
**FUNCTION:** Convert abstract scale into a human reaction and comic beat.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the UH OH caption is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Convert abstract scale into a human reaction and comic beat. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** red calculation plus reaction caption.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: UH OH plus board equations  
**VISUAL HERO:** red calculation plus reaction caption.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Caption X 25–40/Y 53; board and presenter retain V14 geometry. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** red calculation plus reaction caption → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** red calculation plus reaction caption. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F05.1 within S05. **CHANGES:** Only the UH OH caption is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The calculation remains unchanged while UH OH appears above the presenter’s head. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray, red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The calculation remains unchanged while UH OH appears above the presenter’s head. Exact composition: Caption X 25–40/Y 53; board and presenter retain V14 geometry. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray, red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** UH OH plus board equations Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray, red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** UH OH reaction. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.0. **CURRENT:** F05.1. **NEXT:** F05.2. **TRANSITION INTO CURRENT:** Only the UH OH caption is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A10:** text pop; V14/F05.0 → V15/F05.1; 00:28.292; target UH OH caption; relationship SEQUENTIAL.

### 17. WHY MOVE

**A10 — WHY:** Turns numeric escalation into an emotional reaction. **Direction:** appears above presenter follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant comic beat; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** UH OH caption. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A10: SEQUENTIAL** because turns numeric escalation into an emotional reaction.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A10 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A10 PASS:** source V14/F05.0; animate only UH OH caption; target region X 23–42, Y 51–58; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A10 SOURCE FRAME STATE:** V14/F05.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V14. **SOURCE IMAGE PROMPT:** build V14 as a 720×1280 text-free hand-drawn clean plate: The presenter stands below a whiteboard bearing a red ‘200,000 MOLES OF MOLES’ note, a 10⁵³-electron cluster, a Moon-mass relation, and a small Earth cross-section. Layout: Board occupies Y 6–42; red heading X 9–39/Y 18–24; electron cluster X 43–59/Y 19–27; equation X 36–66/Y 30; Earth arc X 26–79/Y 35–40; presenter X 12–36/Y 51–92. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A10

**SOURCE STATE:** V14/F05.0  
**TARGET STATE:** V15/F05.1  
**TIMESTAMP:** 00:28.292  
**MOTION TYPE:** text pop  
**MOTION HERO / ALLOWED MOTION:** UH OH caption  
**START STATE:** V14, matching the source description above.  
**END STATE:** V15, matching this card’s target configuration.  
**DIRECTION:** appears above presenter  
**SPEED:** instant comic beat  
**AMPLITUDE / PATH:** none; ROI X 23–42, Y 51–58  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:28.292.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the hand-lettered caption UH OH above the presenter in one crisp comic pop. Preserve the presenter pose, full whiteboard calculation, red heading, electron cluster, Earth arc, frame and white background exactly. Hold the caption.”  
**CHARACTER COUNT:** 256 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A10: duplicate the stable source precomp; isolate X 23–42, Y 51–58; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 29.083s, then use a local additive/replacement event into V16. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V15 as the exact observed state: red calculation plus reaction caption is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V16 — 29.500s — Board ruptures

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V16_0029500ms.jpg](moon_protons_forensics/keyframes/V16_0029500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 29.083s / 29.500s  
**DURATION TO NEXT MATERIAL STATE:** 0.959s  
**STATE ID:** F05.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the board outline tears inward from the top and sides around the electron cluster, and the presenter now covers both ears. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The board outline tears inward from the top and sides around the electron cluster, and the presenter now covers both ears. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “unbelievable amount of energy”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** unbelievable amount of energy.  
**MOTION CUE:** A11  
**FUNCTION:** Escalate from calculation to physical consequence while keeping the same stage.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Board border and presenter pose are replaced; the central cluster and Earth remain as continuity anchors.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Escalate from calculation to physical consequence while keeping the same stage. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** torn board around electron cluster.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: 10⁵³·e⁻  
**VISUAL HERO:** torn board around electron cluster.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Torn frame intrudes at X 0–15, X 84–100 and top-center; cluster stays near X 50/Y 22; presenter centers X 24/Y 71 in a hands-to-head pose. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** torn board around electron cluster → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** torn board around electron cluster. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** REPLACEMENT DRAWING / ANIMATION END STATE. **BASE:** F05.2 within S05. **CHANGES:** Board border and presenter pose are replaced; the central cluster and Earth remain as continuity anchors. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The board outline tears inward from the top and sides around the electron cluster, and the presenter now covers both ears. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The board outline tears inward from the top and sides around the electron cluster, and the presenter now covers both ears. Exact composition: Torn frame intrudes at X 0–15, X 84–100 and top-center; cluster stays near X 50/Y 22; presenter centers X 24/Y 71 in a hands-to-head pose. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** 10⁵³·e⁻ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Board ruptures. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.1. **CURRENT:** F05.2. **NEXT:** F05.3. **TRANSITION INTO CURRENT:** Board border and presenter pose are replaced; the central cluster and Earth remain as continuity anchors. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A11:** replacement drawing / pose change; V15/F05.1 → V16/F05.2; 00:29.083; target torn board border and presenter hands-to-head pose; relationship SIMULTANEOUS COUPLED.

### 17. WHY MOVE

**A11 — WHY:** Physically escalates the energy while preserving the calculation’s center. **Direction:** board tears inward; arms rise follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** one abrupt beat; amplitude/path inward edge deformation; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** torn board border and presenter hands-to-head pose. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A11: SIMULTANEOUS COUPLED** because physically escalates the energy while preserving the calculation’s center.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWINGS. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A11 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A11 PASS:** source V15/F05.1; animate only torn board border and presenter hands-to-head pose; target region board edges plus presenter; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A11 SOURCE FRAME STATE:** V15/F05.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V15. **SOURCE IMAGE PROMPT:** build V15 as a 720×1280 text-free hand-drawn clean plate: The calculation remains unchanged while UH OH appears above the presenter’s head. Layout: Caption X 25–40/Y 53; board and presenter retain V14 geometry. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A11

**SOURCE STATE:** V15/F05.1  
**TARGET STATE:** V16/F05.2  
**TIMESTAMP:** 00:29.083  
**MOTION TYPE:** replacement drawing / pose change  
**MOTION HERO / ALLOWED MOTION:** torn board border and presenter hands-to-head pose  
**START STATE:** V15, matching the source description above.  
**END STATE:** V16, matching this card’s target configuration.  
**DIRECTION:** board tears inward; arms rise  
**SPEED:** one abrupt beat  
**AMPLITUDE / PATH:** inward edge deformation; ROI board edges plus presenter  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:29.083.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWINGS. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** YES—source and target states listed; use when testing AI.  
**AI PROMPT:** “Locked camera. In one abrupt replacement beat, change the board border to the observed inward-torn outline and change only the presenter into the hands-over-ears pose. Preserve the central 10⁵³ electron cluster, Earth arc, board scale, crop and white background. Hold the new drawing.”  
**CHARACTER COUNT:** 284 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A11: duplicate the stable source precomp; isolate board edges plus presenter; execute REPLACEMENT DRAWINGS; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 30.042s, then use a local additive/replacement event into V17. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V16 as the exact observed state: torn board around electron cluster is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V17 — 30.750s — PLEASE STOP plea

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V17_0030750ms.jpg](moon_protons_forensics/keyframes/V17_0030750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 30.042s / 30.750s  
**DURATION TO NEXT MATERIAL STATE:** 1.791s  
**STATE ID:** F05.3

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the ruptured board holds and PLEASE STOP! appears above the presenter, who continues covering both ears. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The ruptured board holds and PLEASE STOP! appears above the presenter, who continues covering both ears. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “The Moon and Earth would have no chance”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** The Moon and Earth would have no chance.  
**MOTION CUE:** A12  
**FUNCTION:** Sustain humor while the argument escalates.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the plea caption is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Sustain humor while the argument escalates. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** PLEASE STOP!.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PLEASE STOP!; 10⁵³·e⁻  
**VISUAL HERO:** PLEASE STOP!.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Caption X 7–42/Y 54; presenter lower-left/center; board occupies upper 45%. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** PLEASE STOP! → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** PLEASE STOP!. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F05.3 within S05. **CHANGES:** Only the plea caption is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The ruptured board holds and PLEASE STOP! appears above the presenter, who continues covering both ears. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The ruptured board holds and PLEASE STOP! appears above the presenter, who continues covering both ears. Exact composition: Caption X 7–42/Y 54; presenter lower-left/center; board occupies upper 45%. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.3, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PLEASE STOP!; 10⁵³·e⁻ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.3. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** PLEASE STOP plea. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.2. **CURRENT:** F05.3. **NEXT:** F05.4. **TRANSITION INTO CURRENT:** Only the plea caption is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A12:** text pop; V16/F05.2 → V17/F05.3; 00:30.042; target PLEASE STOP! caption; relationship SEQUENTIAL.

### 17. WHY MOVE

**A12 — WHY:** Sustains the comic escalation without moving the technical proof. **Direction:** appears above presenter follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** PLEASE STOP! caption. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A12: SEQUENTIAL** because sustains the comic escalation without moving the technical proof.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A12 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A12 PASS:** source V16/F05.2; animate only PLEASE STOP! caption; target region X 6–43, Y 52–58; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A12 SOURCE FRAME STATE:** V16/F05.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V16. **SOURCE IMAGE PROMPT:** build V16 as a 720×1280 text-free hand-drawn clean plate: The board outline tears inward from the top and sides around the electron cluster, and the presenter now covers both ears. Layout: Torn frame intrudes at X 0–15, X 84–100 and top-center; cluster stays near X 50/Y 22; presenter centers X 24/Y 71 in a hands-to-head pose. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A12

**SOURCE STATE:** V16/F05.2  
**TARGET STATE:** V17/F05.3  
**TIMESTAMP:** 00:30.042  
**MOTION TYPE:** text pop  
**MOTION HERO / ALLOWED MOTION:** PLEASE STOP! caption  
**START STATE:** V16, matching the source description above.  
**END STATE:** V17, matching this card’s target configuration.  
**DIRECTION:** appears above presenter  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 6–43, Y 52–58  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:30.042.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the hand-lettered caption PLEASE STOP! above the presenter. Preserve the torn board, presenter pose, electron cluster, Earth arc, existing marks, white background and every screen position exactly. Hold the caption with no other motion.”  
**CHARACTER COUNT:** 263 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A12: duplicate the stable source precomp; isolate X 6–43, Y 52–58; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 31.833s, then use a local additive/replacement event into V18. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V17 as the exact observed state: PLEASE STOP! is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V18 — 32.250s — Downward interaction arrow

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V18_0032250ms.jpg](moon_protons_forensics/keyframes/V18_0032250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 31.833s / 32.250s  
**DURATION TO NEXT MATERIAL STATE:** 0.917s  
**STATE ID:** F05.4

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a thin black arrow now points downward from the electron cluster toward the Earth arc inside the torn board. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A thin black arrow now points downward from the electron cluster toward the Earth arc inside the torn board. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “to gravitationally or even electrostatically influence each other”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** to gravitationally or even electrostatically influence each other.  
**MOTION CUE:** A13  
**FUNCTION:** Briefly test the inter-body interaction against the larger internal force.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** A single downward arrow is added between the cluster and Earth.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Briefly test the inter-body interaction against the larger internal force. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** downward arrow.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PLEASE STOP!; 10⁵³·e⁻  
**VISUAL HERO:** downward arrow.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Arrow aligns X 50 from Y 28 to Y 36; all other board and presenter elements are locked. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** downward arrow → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** downward arrow. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F05.4 within S05. **CHANGES:** A single downward arrow is added between the cluster and Earth. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A thin black arrow now points downward from the electron cluster toward the Earth arc inside the torn board. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A thin black arrow now points downward from the electron cluster toward the Earth arc inside the torn board. Exact composition: Arrow aligns X 50 from Y 28 to Y 36; all other board and presenter elements are locked. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.4, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PLEASE STOP!; 10⁵³·e⁻ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.4. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Downward interaction arrow. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.3. **CURRENT:** F05.4. **NEXT:** F05.5. **TRANSITION INTO CURRENT:** A single downward arrow is added between the cluster and Earth. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A13:** arrow reveal; V17/F05.3 → V18/F05.4; 00:31.833; target downward interaction arrow; relationship SEQUENTIAL.

### 17. WHY MOVE

**A13 — WHY:** Shows the attempted inter-body attraction before internal repulsion dominates. **Direction:** from electron cluster toward Earth follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** quick draw; amplitude/path straight vertical; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** downward interaction arrow. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A13: SEQUENTIAL** because shows the attempted inter-body attraction before internal repulsion dominates.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** VECTOR TRIM PATH. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A13 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A13 PASS:** source V17/F05.3; animate only downward interaction arrow; target region X 47–53, Y 27–37; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A13 SOURCE FRAME STATE:** V17/F05.3. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V17. **SOURCE IMAGE PROMPT:** build V17 as a 720×1280 text-free hand-drawn clean plate: The ruptured board holds and PLEASE STOP! appears above the presenter, who continues covering both ears. Layout: Caption X 7–42/Y 54; presenter lower-left/center; board occupies upper 45%. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A13

**SOURCE STATE:** V17/F05.3  
**TARGET STATE:** V18/F05.4  
**TIMESTAMP:** 00:31.833  
**MOTION TYPE:** arrow reveal  
**MOTION HERO / ALLOWED MOTION:** downward interaction arrow  
**START STATE:** V17, matching the source description above.  
**END STATE:** V18, matching this card’s target configuration.  
**DIRECTION:** from electron cluster toward Earth  
**SPEED:** quick draw  
**AMPLITUDE / PATH:** straight vertical; ROI X 47–53, Y 27–37  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:31.833.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** VECTOR TRIM PATH. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Draw only the thin black arrow downward from the 10⁵³ electron cluster to the Earth arc, completing the observed straight path once. Preserve the torn board, presenter, PLEASE STOP! caption, cluster, Earth and background exactly. Hold the arrow.”  
**CHARACTER COUNT:** 260 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A13: duplicate the stable source precomp; isolate X 47–53, Y 27–37; execute VECTOR TRIM PATH; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 32.750s, then use a local additive/replacement event into V19. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V18 as the exact observed state: downward arrow is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V19 — 34.250s — Red impact burst

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V19_0034250ms.jpg](moon_protons_forensics/keyframes/V19_0034250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 32.750s / 34.250s  
**DURATION TO NEXT MATERIAL STATE:** 3.375s  
**STATE ID:** F05.5

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a small red star-shaped impact mark appears where the downward arrow meets the Earth arc. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A small red star-shaped impact mark appears where the downward arrow meets the Earth arc. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “The forces trying to blow each one apart would be far more powerful.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** The forces trying to blow each one apart.  
**MOTION CUE:** A14  
**FUNCTION:** Mark the attempted coupling, then prepare the dominant outward explosion.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the red impact burst is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Mark the attempted coupling, then prepare the dominant outward explosion. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** red impact point.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PLEASE STOP!; 10⁵³·e⁻  
**VISUAL HERO:** red impact point.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Red burst centers near X 50/Y 36; its scale is under 5% frame width; torn board, cluster, presenter, and text remain fixed. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** red impact point → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** red impact point. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F05.5 within S05. **CHANGES:** Only the red impact burst is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A small red star-shaped impact mark appears where the downward arrow meets the Earth arc. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray, scarce red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A small red star-shaped impact mark appears where the downward arrow meets the Earth arc. Exact composition: Red burst centers near X 50/Y 36; its scale is under 5% frame width; torn board, cluster, presenter, and text remain fixed. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray, scarce red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.5, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PLEASE STOP!; 10⁵³·e⁻ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray, scarce red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.5. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Red impact burst. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.4. **CURRENT:** F05.5. **NEXT:** F05.6. **TRANSITION INTO CURRENT:** Only the red impact burst is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A14:** impact pop; V18/F05.4 → V19/F05.5; 00:32.750; target small red burst at Earth; relationship SEQUENTIAL.

### 17. WHY MOVE

**A14 — WHY:** Marks the arrow’s contact point and prepares the reversal. **Direction:** appears at arrow endpoint follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** small red burst at Earth. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A14: SEQUENTIAL** because marks the arrow’s contact point and prepares the reversal.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** SHAPE LAYER / replacement drawing. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A14 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A14 PASS:** source V18/F05.4; animate only small red burst at Earth; target region X 46–54, Y 33–39; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A14 SOURCE FRAME STATE:** V18/F05.4. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V18. **SOURCE IMAGE PROMPT:** build V18 as a 720×1280 text-free hand-drawn clean plate: A thin black arrow now points downward from the electron cluster toward the Earth arc inside the torn board. Layout: Arrow aligns X 50 from Y 28 to Y 36; all other board and presenter elements are locked. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A14

**SOURCE STATE:** V18/F05.4  
**TARGET STATE:** V19/F05.5  
**TIMESTAMP:** 00:32.750  
**MOTION TYPE:** impact pop  
**MOTION HERO / ALLOWED MOTION:** small red burst at Earth  
**START STATE:** V18, matching the source description above.  
**END STATE:** V19, matching this card’s target configuration.  
**DIRECTION:** appears at arrow endpoint  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 46–54, Y 33–39  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:32.750.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** SHAPE LAYER / replacement drawing. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Pop in only the small red star-shaped impact at the downward arrow’s contact point on Earth. Keep the arrow, electron cluster, torn board, presenter, captions, line work, crop and white background unchanged. Hold the red impact mark.”  
**CHARACTER COUNT:** 248 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A14: duplicate the stable source precomp; isolate X 46–54, Y 33–39; execute SHAPE LAYER / replacement drawing; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 36.125s, then use a local additive/replacement event into V20. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V19 as the exact observed state: red impact point is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V20 — 37.500s — Electron Moon explodes outward

**SHOT:** S05  
**SOURCE REFERENCE FRAME:** [V20_0037500ms.jpg](moon_protons_forensics/keyframes/V20_0037500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 36.125s / 37.500s  
**DURATION TO NEXT MATERIAL STATE:** 2.833s  
**STATE ID:** F05.6

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see dozens of black rays and small electron symbols radiate from the central 10⁵³ cluster across the torn board while the presenter stays frozen below. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** Dozens of black rays and small electron symbols radiate from the central 10⁵³ cluster across the torn board while the presenter stays frozen below. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “far more powerful”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** far more powerful.  
**MOTION CUE:** A15  
**FUNCTION:** Major visual payoff for the force-scale argument.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** A dense radial electron/ray drawing replaces the quiet board interior; static stage elements remain.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Major visual payoff for the force-scale argument. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** radial electron explosion.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PLEASE STOP!; 10⁵³·e⁻  
**VISUAL HERO:** radial electron explosion.  
**STATIC COORDINATE FRAME:** board/presenter stage.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Radial field fills board X 5–95/Y 5–42; center remains X 50/Y 22; lower presenter/caption region remains clear. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** radial electron explosion → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** radial electron explosion. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** REPLACEMENT DRAWING / ANIMATION END STATE. **BASE:** F05.6 within S05. **CHANGES:** A dense radial electron/ray drawing replaces the quiet board interior; static stage elements remain. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Dozens of black rays and small electron symbols radiate from the central 10⁵³ cluster across the torn board while the presenter stays frozen below. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray, small red impact. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. Dozens of black rays and small electron symbols radiate from the central 10⁵³ cluster across the torn board while the presenter stays frozen below. Exact composition: Radial field fills board X 5–95/Y 5–42; center remains X 50/Y 22; lower presenter/caption region remains clear. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray, small red impact. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F05.6, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PLEASE STOP!; 10⁵³·e⁻ Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray, small red impact), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F05.6. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Electron Moon explodes outward. **SHOT MEMBERSHIP:** S05 (26.250–38.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.5. **CURRENT:** F05.6. **NEXT:** F06.0. **TRANSITION INTO CURRENT:** A dense radial electron/ray drawing replaces the quiet board interior; static stage elements remain. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A15:** replacement explosion drawing; V19/F05.5 → V20/F05.6; 00:36.125; target radial rays and electron symbols across board; relationship STATE REPLACEMENT.

### 17. WHY MOVE

**A15 — WHY:** Pays off the internal-repulsion argument. **Direction:** outward from central cluster follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** one abrupt replacement; amplitude/path radial; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** board/presenter stage; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** radial rays and electron symbols across board. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A15: STATE REPLACEMENT** because pays off the internal-repulsion argument.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWINGS. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A15 MEDIUM. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A15 PASS:** source V19/F05.5; animate only radial rays and electron symbols across board; target region X 5–95, Y 4–43; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A15 SOURCE FRAME STATE:** V19/F05.5. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V19. **SOURCE IMAGE PROMPT:** build V19 as a 720×1280 text-free hand-drawn clean plate: A small red star-shaped impact mark appears where the downward arrow meets the Earth arc. Layout: Red burst centers near X 50/Y 36; its scale is under 5% frame width; torn board, cluster, presenter, and text remain fixed. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A15

**SOURCE STATE:** V19/F05.5  
**TARGET STATE:** V20/F05.6  
**TIMESTAMP:** 00:36.125  
**MOTION TYPE:** replacement explosion drawing  
**MOTION HERO / ALLOWED MOTION:** radial rays and electron symbols across board  
**START STATE:** V19, matching the source description above.  
**END STATE:** V20, matching this card’s target configuration.  
**DIRECTION:** outward from central cluster  
**SPEED:** one abrupt replacement  
**AMPLITUDE / PATH:** radial; ROI X 5–95, Y 4–43  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:36.125.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWINGS. **AI SUITABILITY:** MEDIUM.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** YES—source and target states listed; use when testing AI.  
**AI PROMPT:** “Locked camera. Replace only the quiet board interior with the observed dense radial electron explosion: black rays and electron symbols spread outward from the central 10⁵³ cluster in one abrupt beat. Preserve the torn frame, red impact, Earth arc, presenter and PLEASE STOP! caption. Hold.”  
**CHARACTER COUNT:** 290 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A15: duplicate the stable source precomp; isolate X 5–95, Y 4–43; execute REPLACEMENT DRAWINGS; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 38.958s, then use a hard cut into V21. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V20 as the exact observed state: radial electron explosion is the visual hero, board/presenter stage is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V21 — 40.000s — Electrostatic potential energy

**SHOT:** S06  
**SOURCE REFERENCE FRAME:** [V21_0040000ms.jpg](moon_protons_forensics/keyframes/V21_0040000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 38.958s / 40.000s  
**DURATION TO NEXT MATERIAL STATE:** 2.250s  
**STATE ID:** F06.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a centered circular Electron Moon packed with small electron dots sits on white with the label ELECTRON MOON above and PE_electrostatic below. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A centered circular Electron Moon packed with small electron dots sits on white with the label ELECTRON MOON above and PE_electrostatic below. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “There is a huge amount of potential energy in this scenario”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** There is a huge amount of potential energy.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Name and isolate the energy concept after the comic escalation.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut to a clean single-object technical diagram.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Name and isolate the energy concept after the comic escalation. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** electron-packed Moon.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: ELECTRON MOON; PE_ELECTROSTATIC  
**VISUAL HERO:** electron-packed Moon.  
**STATIC COORDINATE FRAME:** sphere center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Sphere centers X 50/Y 49 at about 31% frame width; top label Y 30; formula Y 66; remaining frame is empty. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** electron-packed Moon → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** electron-packed Moon. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F06.0 within S06. **CHANGES:** Hard cut to a clean single-object technical diagram. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A centered circular Electron Moon packed with small electron dots sits on white with the label ELECTRON MOON above and PE_electrostatic below. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black, gray stipple. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A centered circular Electron Moon packed with small electron dots sits on white with the label ELECTRON MOON above and PE_electrostatic below. Exact composition: Sphere centers X 50/Y 49 at about 31% frame width; top label Y 30; formula Y 66; remaining frame is empty. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black, gray stipple. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F06.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** ELECTRON MOON; PE_ELECTROSTATIC Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black, gray stipple), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F06.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Electrostatic potential energy. **SHOT MEMBERSHIP:** S06 (38.958–41.208).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F05.6. **CURRENT:** F06.0. **NEXT:** F07.0. **TRANSITION INTO CURRENT:** Hard cut to a clean single-object technical diagram. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** sphere center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F06.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.250s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 41.208s, then use a hard cut into V22. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V21 as the exact observed state: electron-packed Moon is the visual hero, sphere center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V22 — 42.500s — Potential energy as radial repulsion

**SHOT:** S07  
**SOURCE REFERENCE FRAME:** [V22_0042500ms.jpg](moon_protons_forensics/keyframes/V22_0042500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 41.208s / 42.500s  
**DURATION TO NEXT MATERIAL STATE:** 2.750s  
**STATE ID:** F07.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the Moon has been replaced by a white center from which many black rays terminate in electron symbols, with PE_electrostatic preserved below. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** The Moon has been replaced by a white center from which many black rays terminate in electron symbols, with PE_electrostatic preserved below. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “the energy that we imagine would blast all those electrons apart”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** the energy that we imagine would blast all.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Translate stored energy into its implied release direction.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard replacement/cut transforms the packed sphere into a radial electron field.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Translate stored energy into its implied release direction. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** radial electron field.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PE_ELECTROSTATIC  
**VISUAL HERO:** radial electron field.  
**STATIC COORDINATE FRAME:** radial center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Radial diagram centers X 50/Y 48 and spans X 10–90/Y 25–68; formula sits X 35–67/Y 69. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** radial electron field → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** radial electron field. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F07.0 within S07. **CHANGES:** Hard replacement/cut transforms the packed sphere into a radial electron field. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The Moon has been replaced by a white center from which many black rays terminate in electron symbols, with PE_electrostatic preserved below. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The Moon has been replaced by a white center from which many black rays terminate in electron symbols, with PE_electrostatic preserved below. Exact composition: Radial diagram centers X 50/Y 48 and spans X 10–90/Y 25–68; formula sits X 35–67/Y 69. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F07.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PE_ELECTROSTATIC Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F07.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Potential energy as radial repulsion. **SHOT MEMBERSHIP:** S07 (41.208–43.958).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F06.0. **CURRENT:** F07.0. **NEXT:** F08.0. **TRANSITION INTO CURRENT:** Hard replacement/cut transforms the packed sphere into a radial electron field. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** radial center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F07.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.750s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 43.958s, then use a hard cut into V23. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V22 as the exact observed state: radial electron field is the visual hero, radial center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V23 — 45.000s — Energy warps space-time

**SHOT:** S08  
**SOURCE REFERENCE FRAME:** [V23_0045000ms.jpg](moon_protons_forensics/keyframes/V23_0045000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 43.958s / 45.000s  
**DURATION TO NEXT MATERIAL STATE:** 2.625s  
**STATE ID:** F08.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a wireframe plane spans the upper-middle frame and drops into two vertical wells; the left is labeled PE_electrostatic and the right E=mc². Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A wireframe plane spans the upper-middle frame and drops into two vertical wells; the left is labeled PE_electrostatic and the right E=mc². **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “That energy warps space and time just like mass does.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** That energy warps space and time just like.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Bridge electrostatic potential energy to the relativistic black-hole consequence.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut from radial force diagram to a paired space-time analogy.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Bridge electrostatic potential energy to the relativistic black-hole consequence. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** two matched gravity wells.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PE_ELECTROSTATIC; E = mc²  
**VISUAL HERO:** two matched gravity wells.  
**STATIC COORDINATE FRAME:** grid horizon.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Grid horizon near Y 42; wells descend to Y 70 at X 25 and X 75; labels sit beneath each; top 35% and bottom 20% are white negative space. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** two matched gravity wells → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** two matched gravity wells. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F08.0 within S08. **CHANGES:** Hard cut from radial force diagram to a paired space-time analogy. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A wireframe plane spans the upper-middle frame and drops into two vertical wells; the left is labeled PE_electrostatic and the right E=mc². **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A wireframe plane spans the upper-middle frame and drops into two vertical wells; the left is labeled PE_electrostatic and the right E=mc². Exact composition: Grid horizon near Y 42; wells descend to Y 70 at X 25 and X 75; labels sit beneath each; top 35% and bottom 20% are white negative space. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F08.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PE_ELECTROSTATIC; E = mc² Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F08.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Energy warps space-time. **SHOT MEMBERSHIP:** S08 (43.958–46.583).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F07.0. **CURRENT:** F08.0. **NEXT:** F09.0. **TRANSITION INTO CURRENT:** Hard cut from radial force diagram to a paired space-time analogy. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** grid horizon; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F08.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.625s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 46.583s, then use a hard cut into V24. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V23 as the exact observed state: two matched gravity wells is the visual hero, grid horizon is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V24 — 47.500s — Observable-universe equivalence

**SHOT:** S09  
**SOURCE REFERENCE FRAME:** [V24_0047500ms.jpg](moon_protons_forensics/keyframes/V24_0047500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 46.583s / 47.500s  
**DURATION TO NEXT MATERIAL STATE:** 1.167s  
**STATE ID:** F09.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a large black sphere labeled as the observable universe sits near the top, an approximately-equal sign below it, and a tiny 3,475 km Moon marker near the lower-middle above ELECTRON MOON. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A large black sphere labeled as the observable universe sits near the top, an approximately-equal sign below it, and a tiny 3,475 km Moon marker near the lower-middle above ELECTRON MOON. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “The amount of energy in our electron moon, it turns out, is about equal to the total mass and energy of the entire observable universe.”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** The amount of energy in our electron moon,.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Deliver the video’s principal scale reveal.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut to a vertical size-and-energy equivalence infographic.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Deliver the video’s principal scale reveal. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** black observable-universe sphere.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: 93 BILLION LIGHTYEARS; E_OBSERVABLE UNIVERSE; ≈; 3,475 km; ELECTRON MOON  
**VISUAL HERO:** black observable-universe sphere.  
**STATIC COORDINATE FRAME:** universe sphere and labels.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Universe sphere centers X 50/Y 22 at 45% width; 93 BILLION LIGHTYEARS spans above; ≈ centers Y 49; tiny marker X 50/Y 66; ELECTRON MOON centers Y 87. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** black observable-universe sphere → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** black observable-universe sphere. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F09.0 within S09. **CHANGES:** Hard cut to a vertical size-and-energy equivalence infographic. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A large black sphere labeled as the observable universe sits near the top, an approximately-equal sign below it, and a tiny 3,475 km Moon marker near the lower-middle above ELECTRON MOON. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, dense black sphere, thin black annotations. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A large black sphere labeled as the observable universe sits near the top, an approximately-equal sign below it, and a tiny 3,475 km Moon marker near the lower-middle above ELECTRON MOON. Exact composition: Universe sphere centers X 50/Y 22 at 45% width; 93 BILLION LIGHTYEARS spans above; ≈ centers Y 49; tiny marker X 50/Y 66; ELECTRON MOON centers Y 87. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, dense black sphere, thin black annotations. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F09.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** 93 BILLION LIGHTYEARS; E_OBSERVABLE UNIVERSE; ≈; 3,475 km; ELECTRON MOON Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, dense black sphere, thin black annotations), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F09.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Observable-universe equivalence. **SHOT MEMBERSHIP:** S09 (46.583–63.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F08.0. **CURRENT:** F09.0. **NEXT:** F09.1. **TRANSITION INTO CURRENT:** Hard cut to a vertical size-and-energy equivalence infographic. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** universe sphere and labels; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F09.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 1.167s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 47.750s, then use a local additive/replacement event into V25. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V24 as the exact observed state: black observable-universe sphere is the visual hero, universe sphere and labels is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V25 — 49.000s — Tiny Moon marker jitter

**SHOT:** S09  
**SOURCE REFERENCE FRAME:** [V25_0049000ms.jpg](moon_protons_forensics/keyframes/V25_0049000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 47.750s / 49.000s  
**DURATION TO NEXT MATERIAL STATE:** 7.042s  
**STATE ID:** F09.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the equivalence diagram holds while the tiny Moon marker cycles through slightly different hand-drawn positions/shapes under the 3,475 km bracket. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The equivalence diagram holds while the tiny Moon marker cycles through slightly different hand-drawn positions/shapes under the 3,475 km bracket. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “equal to the total mass and energy”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** equal to the total mass and energy.  
**MOTION CUE:** A16  
**FUNCTION:** Keep the minute Moon scale perceptible without moving the proof’s coordinate frame.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the small Moon scribble uses replacement-drawing jitter; no semantic content changes.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Keep the minute Moon scale perceptible without moving the proof’s coordinate frame. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** tiny Moon marker.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: same as V24  
**VISUAL HERO:** tiny Moon marker.  
**STATIC COORDINATE FRAME:** universe sphere and labels.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** All text and the universe sphere remain fixed; movement is confined to roughly X 43–57/Y 64–70. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** tiny Moon marker → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** tiny Moon marker. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** REPLACEMENT-DRAWING LOOP / INTERMEDIATE STATE. **BASE:** F09.1 within S09. **CHANGES:** Only the small Moon scribble uses replacement-drawing jitter; no semantic content changes. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The equivalence diagram holds while the tiny Moon marker cycles through slightly different hand-drawn positions/shapes under the 3,475 km bracket. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The equivalence diagram holds while the tiny Moon marker cycles through slightly different hand-drawn positions/shapes under the 3,475 km bracket. Exact composition: All text and the universe sphere remain fixed; movement is confined to roughly X 43–57/Y 64–70. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F09.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** same as V24 Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F09.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Tiny Moon marker jitter. **SHOT MEMBERSHIP:** S09 (46.583–63.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F09.0. **CURRENT:** F09.1. **NEXT:** F09.2. **TRANSITION INTO CURRENT:** Only the small Moon scribble uses replacement-drawing jitter; no semantic content changes. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A16:** replacement-drawing jitter loop; V24/F09.0 → V25/F09.1; 00:47.750–00:54.750; target tiny Moon marker; relationship PERSISTENT LOOP.

### 17. WHY MOVE

**A16 — WHY:** Keeps the tiny object visible while the scale comparison remains readable. **Direction:** small lateral/shape variations follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** subtle irregular cycle; amplitude/path confined local wobble; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** universe sphere and labels; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** tiny Moon marker. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A16: PERSISTENT LOOP** because keeps the tiny object visible while the scale comparison remains readable.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT-DRAWING FRAME LOOP. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A16 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A16 PASS:** source V24/F09.0; animate only tiny Moon marker; target region X 43–57, Y 64–70; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A16 SOURCE FRAME STATE:** V24/F09.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V24. **SOURCE IMAGE PROMPT:** build V24 as a 720×1280 text-free hand-drawn clean plate: A large black sphere labeled as the observable universe sits near the top, an approximately-equal sign below it, and a tiny 3,475 km Moon marker near the lower-middle above ELECTRON MOON. Layout: Universe sphere centers X 50/Y 22 at 45% width; 93 BILLION LIGHTYEARS spans above; ≈ centers Y 49; tiny marker X 50/Y 66; ELECTRON MOON centers Y 87. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A16

**SOURCE STATE:** V24/F09.0  
**TARGET STATE:** V25/F09.1  
**TIMESTAMP:** 00:47.750–00:54.750  
**MOTION TYPE:** replacement-drawing jitter loop  
**MOTION HERO / ALLOWED MOTION:** tiny Moon marker  
**START STATE:** V24, matching the source description above.  
**END STATE:** V25, matching this card’s target configuration.  
**DIRECTION:** small lateral/shape variations  
**SPEED:** subtle irregular cycle  
**AMPLITUDE / PATH:** confined local wobble; ROI X 43–57, Y 64–70  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:47.750–00:54.750.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT-DRAWING FRAME LOOP. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Animate only the tiny Moon marker beneath the 3,475 km bracket with the observed subtle replacement-drawing jitter, shifting its scribbled shape by a few pixels without changing average position or size. Keep the universe sphere, labels, ≈ sign and white background fixed.”  
**CHARACTER COUNT:** 287 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A16: duplicate the stable source precomp; isolate X 43–57, Y 64–70; execute REPLACEMENT-DRAWING FRAME LOOP; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 54.792s, then use a local additive/replacement event into V26. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V25 as the exact observed state: tiny Moon marker is the visual hero, universe sphere and labels is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V26 — 56.000s — Compression arrows

**SHOT:** S09  
**SOURCE REFERENCE FRAME:** [V26_0056000ms.jpg](moon_protons_forensics/keyframes/V26_0056000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 54.792s / 56.000s  
**DURATION TO NEXT MATERIAL STATE:** 2.625s  
**STATE ID:** F09.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see two long diagonal arrows descend from the observable-universe sphere and converge on the tiny Moon marker. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** Two long diagonal arrows descend from the observable-universe sphere and converge on the tiny Moon marker. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “mass energy concentrated into the space of our relatively small moon”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** mass energy concentrated into the space of our.  
**MOTION CUE:** A17  
**FUNCTION:** Visualize concentration: same energy, drastically smaller region.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Two convergence arrows are added over the equivalence diagram.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Visualize concentration: same energy, drastically smaller region. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** converging arrows.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: same as V24  
**VISUAL HERO:** converging arrows.  
**STATIC COORDINATE FRAME:** universe sphere and labels.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Arrow tails begin near X 29/Y 40 and X 72/Y 40; arrowheads meet near X 46 and X 54/Y 66; all labels and objects remain registered. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** converging arrows → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** converging arrows. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC MODIFICATION / ANIMATION END STATE. **BASE:** F09.2 within S09. **CHANGES:** Two convergence arrows are added over the equivalence diagram. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Two long diagonal arrows descend from the observable-universe sphere and converge on the tiny Moon marker. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. Two long diagonal arrows descend from the observable-universe sphere and converge on the tiny Moon marker. Exact composition: Arrow tails begin near X 29/Y 40 and X 72/Y 40; arrowheads meet near X 46 and X 54/Y 66; all labels and objects remain registered. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F09.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** same as V24 Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F09.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Compression arrows. **SHOT MEMBERSHIP:** S09 (46.583–63.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F09.1. **CURRENT:** F09.2. **NEXT:** F09.3. **TRANSITION INTO CURRENT:** Two convergence arrows are added over the equivalence diagram. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A17:** two-arrow reveal; V25/F09.1 → V26/F09.2; 00:54.792; target converging compression arrows; relationship SIMULTANEOUS COUPLED.

**OTHER ACTIVE / PERSISTENT:** A16 marker loop ends as A17 begins.

### 17. WHY MOVE

**A17 — WHY:** Communicates concentration of universe-scale energy into Moon scale. **Direction:** downward from universe toward Moon follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** quick synchronized draw; amplitude/path two straight diagonals; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** universe sphere and labels; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** converging compression arrows. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A16 marker loop ends as A17 begins. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** YES. Use isolated text/vector passes over the pre-rendered A22 base; never regenerate the whole frame.

### 20. MOTION COUPLING CLASSIFICATION

**A17: SIMULTANEOUS COUPLED** because communicates concentration of universe-scale energy into moon scale.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** VECTOR TRIM PATHS. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A17 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A17 PASS:** source V25/F09.1; animate only converging compression arrows; target region X 26–74, Y 39–68; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A17 SOURCE FRAME STATE:** V25/F09.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V25. **SOURCE IMAGE PROMPT:** build V25 as a 720×1280 text-free hand-drawn clean plate: The equivalence diagram holds while the tiny Moon marker cycles through slightly different hand-drawn positions/shapes under the 3,475 km bracket. Layout: All text and the universe sphere remain fixed; movement is confined to roughly X 43–57/Y 64–70. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A17

**SOURCE STATE:** V25/F09.1  
**TARGET STATE:** V26/F09.2  
**TIMESTAMP:** 00:54.792  
**MOTION TYPE:** two-arrow reveal  
**MOTION HERO / ALLOWED MOTION:** converging compression arrows  
**START STATE:** V25, matching the source description above.  
**END STATE:** V26, matching this card’s target configuration.  
**DIRECTION:** downward from universe toward Moon  
**SPEED:** quick synchronized draw  
**AMPLITUDE / PATH:** two straight diagonals; ROI X 26–74, Y 39–68  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:54.792.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** VECTOR TRIM PATHS. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Draw the two long black arrows together from beneath the observable-universe sphere down toward the tiny Moon marker, following the observed converging diagonals. Preserve all labels, the sphere, marker, ≈ sign and white background exactly. Complete once and hold.”  
**CHARACTER COUNT:** 279 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A17: duplicate the stable source precomp; isolate X 26–74, Y 39–68; execute VECTOR TRIM PATHS; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 57.417s, then use a local additive/replacement event into V27. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V26 as the exact observed state: converging arrows is the visual hero, universe sphere and labels is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V27 — 58.500s — Moon becomes black-hole well

**SHOT:** S09  
**SOURCE REFERENCE FRAME:** [V27_0058500ms.jpg](moon_protons_forensics/keyframes/V27_0058500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 57.417s / 58.500s  
**DURATION TO NEXT MATERIAL STATE:** 2.625s  
**STATE ID:** F09.3

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the tiny Moon marker has become a horizontal rim with a deep tapered well extending downward, while compression arrows continue pointing to its mouth. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The tiny Moon marker has become a horizontal rim with a deep tapered well extending downward, while compression arrows continue pointing to its mouth. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “would warp space-time so strongly”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** would warp space-time so strongly.  
**MOTION CUE:** A18  
**FUNCTION:** Convert concentrated energy into the black-hole geometry.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** The local Moon marker region is replaced by a black-hole well; surrounding infographic is preserved.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Convert concentrated energy into the black-hole geometry. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** black-hole well.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: same as V24  
**VISUAL HERO:** black-hole well.  
**STATIC COORDINATE FRAME:** universe sphere and labels.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Well mouth spans X 39–61/Y 68; tapered shaft descends to Y 85; universe sphere, arrows, scale label, and bottom ELECTRON MOON text remain fixed. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** black-hole well → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** black-hole well. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** REPLACEMENT DRAWING / ANIMATION END STATE. **BASE:** F09.3 within S09. **CHANGES:** The local Moon marker region is replaced by a black-hole well; surrounding infographic is preserved. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The tiny Moon marker has become a horizontal rim with a deep tapered well extending downward, while compression arrows continue pointing to its mouth. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The tiny Moon marker has become a horizontal rim with a deep tapered well extending downward, while compression arrows continue pointing to its mouth. Exact composition: Well mouth spans X 39–61/Y 68; tapered shaft descends to Y 85; universe sphere, arrows, scale label, and bottom ELECTRON MOON text remain fixed. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F09.3, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** same as V24 Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F09.3. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Moon becomes black-hole well. **SHOT MEMBERSHIP:** S09 (46.583–63.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F09.2. **CURRENT:** F09.3. **NEXT:** F09.4. **TRANSITION INTO CURRENT:** The local Moon marker region is replaced by a black-hole well; surrounding infographic is preserved. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A18:** local state replacement; V26/F09.2 → V27/F09.3; 00:57.417; target Moon marker becomes black-hole well; relationship STATE REPLACEMENT.

### 17. WHY MOVE

**A18 — WHY:** Turns energy concentration into space-time collapse. **Direction:** well extends downward follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** abrupt explanatory change; amplitude/path vertical taper; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** universe sphere and labels; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** Moon marker becomes black-hole well. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A18: STATE REPLACEMENT** because turns energy concentration into space-time collapse.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWING / first-last-frame optional. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A18 MEDIUM. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A18 PASS:** source V26/F09.2; animate only Moon marker becomes black-hole well; target region X 38–62, Y 64–86; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A18 SOURCE FRAME STATE:** V26/F09.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V26. **SOURCE IMAGE PROMPT:** build V26 as a 720×1280 text-free hand-drawn clean plate: Two long diagonal arrows descend from the observable-universe sphere and converge on the tiny Moon marker. Layout: Arrow tails begin near X 29/Y 40 and X 72/Y 40; arrowheads meet near X 46 and X 54/Y 66; all labels and objects remain registered. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A18

**SOURCE STATE:** V26/F09.2  
**TARGET STATE:** V27/F09.3  
**TIMESTAMP:** 00:57.417  
**MOTION TYPE:** local state replacement  
**MOTION HERO / ALLOWED MOTION:** Moon marker becomes black-hole well  
**START STATE:** V26, matching the source description above.  
**END STATE:** V27, matching this card’s target configuration.  
**DIRECTION:** well extends downward  
**SPEED:** abrupt explanatory change  
**AMPLITUDE / PATH:** vertical taper; ROI X 38–62, Y 64–86  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 00:57.417.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWING / first-last-frame optional. **AI SUITABILITY:** MEDIUM.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** YES—source and target states listed; use when testing AI.  
**AI PROMPT:** “Locked camera. Transform only the tiny Moon-marker region into the observed black-hole well: a horizontal rim forms at the arrowheads and a narrow tapered shaft extends downward. Preserve the universe sphere, compression arrows, labels, scale bracket, ≈ sign and white background.”  
**CHARACTER COUNT:** 280 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A18: duplicate the stable source precomp; isolate X 38–62, Y 64–86; execute REPLACEMENT DRAWING / first-last-frame optional; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 60.042s, then use a local additive/replacement event into V28. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V27 as the exact observed state: black-hole well is the visual hero, universe sphere and labels is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V28 — 61.500s — BLACK HOLE label

**SHOT:** S09  
**SOURCE REFERENCE FRAME:** [V28_0061500ms.jpg](moon_protons_forensics/keyframes/V28_0061500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 60.042s / 61.500s  
**DURATION TO NEXT MATERIAL STATE:** 3.500s  
**STATE ID:** F09.4

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the completed universe-to-well diagram now includes BLACK HOLE to the right of the well rim. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The completed universe-to-well diagram now includes BLACK HOLE to the right of the well rim. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “it would easily overpower even the repulsion of those 10 to the 53 electrons.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** it would easily overpower even the repulsion of.  
**MOTION CUE:** A19  
**FUNCTION:** Name the final physical outcome and close the main explanatory loop.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the BLACK HOLE label is added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Name the final physical outcome and close the main explanatory loop. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** black-hole outcome.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: same as V24 plus BLACK HOLE  
**VISUAL HERO:** black-hole outcome.  
**STATIC COORDINATE FRAME:** universe sphere and labels.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Label sits X 64–84/Y 68; all prior elements retain V27 geometry. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** black-hole outcome → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** black-hole outcome. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F09.4 within S09. **CHANGES:** Only the BLACK HOLE label is added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The completed universe-to-well diagram now includes BLACK HOLE to the right of the well rim. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white and black. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. The completed universe-to-well diagram now includes BLACK HOLE to the right of the well rim. Exact composition: Label sits X 64–84/Y 68; all prior elements retain V27 geometry. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white and black. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F09.4, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** same as V24 plus BLACK HOLE Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white and black), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F09.4. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** BLACK HOLE label. **SHOT MEMBERSHIP:** S09 (46.583–63.542).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F09.3. **CURRENT:** F09.4. **NEXT:** F10.0. **TRANSITION INTO CURRENT:** Only the BLACK HOLE label is added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A19:** text reveal; V27/F09.3 → V28/F09.4; 01:00.042; target BLACK HOLE label; relationship SEQUENTIAL.

### 17. WHY MOVE

**A19 — WHY:** Names and closes the main physical payoff. **Direction:** appears right of well follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** universe sphere and labels; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** BLACK HOLE label. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A19: SEQUENTIAL** because names and closes the main physical payoff.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A19 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A19 PASS:** source V27/F09.3; animate only BLACK HOLE label; target region X 62–86, Y 65–72; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A19 SOURCE FRAME STATE:** V27/F09.3. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V27. **SOURCE IMAGE PROMPT:** build V27 as a 720×1280 text-free hand-drawn clean plate: The tiny Moon marker has become a horizontal rim with a deep tapered well extending downward, while compression arrows continue pointing to its mouth. Layout: Well mouth spans X 39–61/Y 68; tapered shaft descends to Y 85; universe sphere, arrows, scale label, and bottom ELECTRON MOON text remain fixed. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A19

**SOURCE STATE:** V27/F09.3  
**TARGET STATE:** V28/F09.4  
**TIMESTAMP:** 01:00.042  
**MOTION TYPE:** text reveal  
**MOTION HERO / ALLOWED MOTION:** BLACK HOLE label  
**START STATE:** V27, matching the source description above.  
**END STATE:** V28, matching this card’s target configuration.  
**DIRECTION:** appears right of well  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 62–86, Y 65–72  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:00.042.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the exact hand-lettered label BLACK HOLE to the right of the well rim. Preserve the observable-universe sphere, arrows, well, scale text, ≈ sign, ELECTRON MOON label, white background and all spacing. Hold the completed diagram.”  
**CHARACTER COUNT:** 255 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A19: duplicate the stable source precomp; isolate X 62–86, Y 65–72; execute EDITOR TEXT OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 63.542s, then use a hard cut into V29. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V28 as the exact observed state: black-hole outcome is the visual hero, universe sphere and labels is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V29 — 64.500s — Local destruction

**SHOT:** S10  
**SOURCE REFERENCE FRAME:** [V29_0064500ms.jpg](moon_protons_forensics/keyframes/V29_0064500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 63.542s / 64.500s  
**DURATION TO NEXT MATERIAL STATE:** 1.833s  
**STATE ID:** F10.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a hand-drawn suburban street is crushed inward: a car and foliage collapse from the left toward a central point while a house tilts in from the right above a flat gray ground band. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A hand-drawn suburban street is crushed inward: a car and foliage collapse from the left toward a central point while a house tilts in from the right above a flat gray ground band. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “Would the attraction of this universe-mass black hole cause the rest of the universe to collapse?”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** Would the attraction of this universe-mass black hole.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Ground the cosmic question in an instantly readable local consequence.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut from clean infographic to environmental destruction illustration.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Ground the cosmic question in an instantly readable local consequence. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** clean white negative space.  
**MAIN SUBJECT:** inward-collapsing car and house.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: No overlay text in this state.  
**VISUAL HERO:** inward-collapsing car and house.  
**STATIC COORDINATE FRAME:** ground band.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Action occupies middle X 0–100/Y 45–63; gray ground fills Y 64–100; upper 40% is white negative space. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** inward-collapsing car and house → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** inward-collapsing car and house. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F10.0 within S10. **CHANGES:** Hard cut from clean infographic to environmental destruction illustration. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** vertical hand-drawn educational explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A hand-drawn suburban street is crushed inward: a car and foliage collapse from the left toward a central point while a house tilts in from the right above a flat gray ground band. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** white, black line, gray ground. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 vertical hand-drawn educational explainer frame matching a minimalist scientific notebook animation. A hand-drawn suburban street is crushed inward: a car and foliage collapse from the left toward a central point while a house tilts in from the right above a flat gray ground band. Exact composition: Action occupies middle X 0–100/Y 45–63; gray ground fills Y 64–100; upper 40% is white negative space. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and clean white negative space. Palette: white, black line, gray ground. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F10.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** No overlay text in this state. Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, clean white negative space, flat lighting, palette (white, black line, gray ground), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F10.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Local destruction. **SHOT MEMBERSHIP:** S10 (63.542–65.375).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F09.4. **CURRENT:** F10.0. **NEXT:** F11.0. **TRANSITION INTO CURRENT:** Hard cut from clean infographic to environmental destruction illustration. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ground band; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F10.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 1.833s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 65.375s, then use a hard cut into V30. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V29 as the exact observed state: inward-collapsing car and house is the visual hero, ground band is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V30 — 66.000s — Cosmic collapse montage

**SHOT:** S11  
**SOURCE REFERENCE FRAME:** [V30_0066000ms.jpg](moon_protons_forensics/keyframes/V30_0066000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 65.375s / 66.000s  
**DURATION TO NEXT MATERIAL STATE:** 1.000s  
**STATE ID:** F11.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see on black, small planets, stars, people, and objects streak diagonally toward a glowing central black hole. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** On black, small planets, stars, people, and objects streak diagonally toward a glowing central black hole. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “cause the rest of the universe to collapse?”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** cause the rest of the universe to collapse?.  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Escalate the local collapse question to universe scale.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Smash cut/invert from white neighborhood scene to black cosmic montage.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Escalate the local collapse question to universe scale. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** central black-hole point.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: No overlay text in this state.  
**VISUAL HERO:** central black-hole point.  
**STATIC COORDINATE FRAME:** central black hole.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Central glow near X 48/Y 52; white outlined objects radiate across full frame with inward speed marks; black negative space dominates. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** central black-hole point → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** central black-hole point. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F11.0 within S11. **CHANGES:** Smash cut/invert from white neighborhood scene to black cosmic montage. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** On black, small planets, stars, people, and objects streak diagonally toward a glowing central black hole. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black field, white line objects and glow. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. On black, small planets, stars, people, and objects streak diagonally toward a glowing central black hole. Exact composition: Central glow near X 48/Y 52; white outlined objects radiate across full frame with inward speed marks; black negative space dominates. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black field, white line objects and glow. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F11.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** No overlay text in this state. Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black field, white line objects and glow), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F11.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Cosmic collapse montage. **SHOT MEMBERSHIP:** S11 (65.375–66.375).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F10.0. **CURRENT:** F11.0. **NEXT:** F12.0. **TRANSITION INTO CURRENT:** Smash cut/invert from white neighborhood scene to black cosmic montage. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** central black hole; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F11.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 1.000s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 66.375s, then use a hard cut into V31. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V30 as the exact observed state: central black-hole point is the visual hero, central black hole is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V31 — 67.500s — Lone black hole

**SHOT:** S12  
**SOURCE REFERENCE FRAME:** [V31_0067500ms.jpg](moon_protons_forensics/keyframes/V31_0067500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 66.375s / 67.500s  
**DURATION TO NEXT MATERIAL STATE:** 1.792s  
**STATE ID:** F12.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a tiny white-ringed black hole sits slightly below frame center on an otherwise almost pure black field. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is a stable static hold. **LITERAL FRAME DESCRIPTION:** A tiny white-ringed black hole sits slightly below frame center on an otherwise almost pure black field. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “It’s hard to say.”  
**VISUAL APPEARS:** BEFORE and THROUGH the matching idea.  
**TRIGGER WORD / IDEA:** It’s hard to say..  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** Pause after escalation and create room for uncertainty.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut removes all surrounding objects and leaves the black-hole anchor alone.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Pause after escalation and create room for uncertainty. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** small luminous ring.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: No overlay text in this state.  
**VISUAL HERO:** small luminous ring.  
**STATIC COORDINATE FRAME:** black field/ring center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring centers near X 50/Y 57 at roughly 8% width; all other space is black. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** small luminous ring → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** small luminous ring. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / STATIC HOLD. **BASE:** F12.0 within S12. **CHANGES:** Hard cut removes all surrounding objects and leaves the black-hole anchor alone. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A tiny white-ringed black hole sits slightly below frame center on an otherwise almost pure black field. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black with white-gray ring. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. A tiny white-ringed black hole sits slightly below frame center on an otherwise almost pure black field. Exact composition: Ring centers near X 50/Y 57 at roughly 8% width; all other space is black. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black with white-gray ring. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F12.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** No overlay text in this state. Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (black unless the listed state says otherwise).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black with white-gray ring), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F12.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Lone black hole. **SHOT MEMBERSHIP:** S12 (66.375–68.167).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F11.0. **CURRENT:** F12.0. **NEXT:** F13.0. **TRANSITION INTO CURRENT:** Hard cut removes all surrounding objects and leaves the black-hole anchor alone. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** black field/ring center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** none. **LOCKED:** entire frame. **OTHER ACTIVE EVENTS:** none. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. Hold the source image; do not generate AI video.

### 20. MOTION COUPLING CLASSIFICATION

**STATIC / NO COUPLING:** no in-shot movement exists to couple. Entry/exit is editorial.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F12.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 1.792s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 68.167s, then use a hard cut into V32. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V31 as the exact observed state: small luminous ring is the visual hero, black field/ring center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V32 — 69.500s — Dark-energy uncertainty

**SHOT:** S13  
**SOURCE REFERENCE FRAME:** [V32_0069500ms.jpg](moon_protons_forensics/keyframes/V32_0069500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 68.167s / 69.500s  
**DURATION TO NEXT MATERIAL STATE:** 2.708s  
**STATE ID:** F13.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see red DARK ENERGY lettering, question marks, and arrows appear at upper-left while the small black hole remains lower-right of that cluster. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** Red DARK ENERGY lettering, question marks, and arrows appear at upper-left while the small black hole remains lower-right of that cluster. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “The answer kind of depends on what the deal with dark energy is”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** The answer kind of depends on what the.  
**MOTION CUE:** A20  
**FUNCTION:** Name the uncertain variable using the only strong color accent in the cosmic section.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Red text and arrows are added; black hole remains fixed.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Name the uncertain variable using the only strong color accent in the cosmic section. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** red DARK ENERGY cluster.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: DARK ENERGY with question marks/arrows  
**VISUAL HERO:** red DARK ENERGY cluster.  
**STATIC COORDINATE FRAME:** ring center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Red cluster occupies X 8–49/Y 20–40; black hole centers X 54/Y 56; rest stays black. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** red DARK ENERGY cluster → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** red DARK ENERGY cluster. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** GRAPHIC + TEXT MODIFICATION / ANIMATION END STATE. **BASE:** F13.0 within S13. **CHANGES:** Red text and arrows are added; black hole remains fixed. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** Red DARK ENERGY lettering, question marks, and arrows appear at upper-left while the small black hole remains lower-right of that cluster. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white ring, saturated red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. Red DARK ENERGY lettering, question marks, and arrows appear at upper-left while the small black hole remains lower-right of that cluster. Exact composition: Red cluster occupies X 8–49/Y 20–40; black hole centers X 54/Y 56; rest stays black. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white ring, saturated red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F13.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** DARK ENERGY with question marks/arrows Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white ring, saturated red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F13.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Dark-energy uncertainty. **SHOT MEMBERSHIP:** S13 (68.167–73.125).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F12.0. **CURRENT:** F13.0. **NEXT:** F13.1. **TRANSITION INTO CURRENT:** Red text and arrows are added; black hole remains fixed. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A20:** red graphic reveal; V31/F12.0 → V32/F13.0; 01:08.167; target DARK ENERGY text, question marks and arrows; relationship SEQUENTIAL.

### 17. WHY MOVE

**A20 — WHY:** Introduces the unknown variable without moving the black-hole anchor. **Direction:** cluster appears upper-left follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** one-step reveal; amplitude/path radial annotations; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** DARK ENERGY text, question marks and arrows. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A20: SEQUENTIAL** because introduces the unknown variable without moving the black-hole anchor.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT + VECTOR OVERLAY. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A20 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A20 PASS:** source V31/F12.0; animate only DARK ENERGY text, question marks and arrows; target region X 7–51, Y 19–42; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A20 SOURCE FRAME STATE:** V31/F12.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V31. **SOURCE IMAGE PROMPT:** build V31 as a 720×1280 text-free hand-drawn clean plate: A tiny white-ringed black hole sits slightly below frame center on an otherwise almost pure black field. Layout: Ring centers near X 50/Y 57 at roughly 8% width; all other space is black. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A20

**SOURCE STATE:** V31/F12.0  
**TARGET STATE:** V32/F13.0  
**TIMESTAMP:** 01:08.167  
**MOTION TYPE:** red graphic reveal  
**MOTION HERO / ALLOWED MOTION:** DARK ENERGY text, question marks and arrows  
**START STATE:** V31, matching the source description above.  
**END STATE:** V32, matching this card’s target configuration.  
**DIRECTION:** cluster appears upper-left  
**SPEED:** one-step reveal  
**AMPLITUDE / PATH:** radial annotations; ROI X 7–51, Y 19–42  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:08.167.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT + VECTOR OVERLAY. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal only the red DARK ENERGY lettering with its observed question marks and outward arrows in the upper-left. Keep the small white-ringed black hole, black background, exact spacing and frame completely stable. Hold the red annotation cluster.”  
**CHARACTER COUNT:** 261 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A20: duplicate the stable source precomp; isolate X 7–51, Y 19–42; execute EDITOR TEXT + VECTOR OVERLAY; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 70.875s, then use a local additive/replacement event into V33. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V32 as the exact observed state: red DARK ENERGY cluster is the visual hero, ring center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V33 — 71.750s — String-theory aside

**SHOT:** S13  
**SOURCE REFERENCE FRAME:** [V33_0071750ms.jpg](moon_protons_forensics/keyframes/V33_0071750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 70.875s / 71.750s  
**DURATION TO NEXT MATERIAL STATE:** 2.250s  
**STATE ID:** F13.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a small white line character peeks from the bottom-right with MAYBE SOMETHING STRINGY? while the red dark-energy cluster and black hole remain. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A small white line character peeks from the bottom-right with MAYBE SOMETHING STRINGY? while the red dark-energy cluster and black hole remain. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “and nobody knows what the deal with dark energy is.”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** and nobody knows what the deal with dark.  
**MOTION CUE:** A21  
**FUNCTION:** Add a brief intellectual-comic aside without resolving the uncertainty.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Bottom-right character and white caption are added.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** ESSENTIAL / EXPLANATORY. **Purpose:** Add a brief intellectual-comic aside without resolving the uncertainty. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** red dark-energy cluster first, comic character second.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: DARK ENERGY; MAYBE SOMETHING STRINGY?  
**VISUAL HERO:** red dark-energy cluster first, comic character second.  
**STATIC COORDINATE FRAME:** ring center.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Character/caption occupies X 57–96/Y 77–98; dark-energy cluster and hole preserve V32 coordinates. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** red dark-energy cluster first, comic character second → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** red dark-energy cluster first, comic character second. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** MODIFIED REUSE / ANIMATION END STATE. **BASE:** F13.1 within S13. **CHANGES:** Bottom-right character and white caption are added. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A small white line character peeks from the bottom-right with MAYBE SOMETHING STRINGY? while the red dark-energy cluster and black hole remain. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, red, white. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. A small white line character peeks from the bottom-right with MAYBE SOMETHING STRINGY? while the red dark-energy cluster and black hole remain. Exact composition: Character/caption occupies X 57–96/Y 77–98; dark-energy cluster and hole preserve V32 coordinates. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, red, white. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F13.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** DARK ENERGY; MAYBE SOMETHING STRINGY? Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, red, white), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F13.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** String-theory aside. **SHOT MEMBERSHIP:** S13 (68.167–73.125).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F13.0. **CURRENT:** F13.1. **NEXT:** F14.0. **TRANSITION INTO CURRENT:** Bottom-right character and white caption are added. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A21:** character/caption reveal; V32/F13.0 → V33/F13.1; 01:10.875; target bottom-right character and white caption; relationship SIMULTANEOUS COUPLED.

### 17. WHY MOVE

**A21 — WHY:** Adds a concise string-theory joke while preserving uncertainty. **Direction:** appears from lower-right edge follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** single comic beat; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** bottom-right character and white caption. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A21: SIMULTANEOUS COUPLED** because adds a concise string-theory joke while preserving uncertainty.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** REPLACEMENT DRAWING + text overlay. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A21 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A21 PASS:** source V32/F13.0; animate only bottom-right character and white caption; target region X 56–97, Y 76–100; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A21 SOURCE FRAME STATE:** V32/F13.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V32. **SOURCE IMAGE PROMPT:** build V32 as a 720×1280 text-free hand-drawn clean plate: Red DARK ENERGY lettering, question marks, and arrows appear at upper-left while the small black hole remains lower-right of that cluster. Layout: Red cluster occupies X 8–49/Y 20–40; black hole centers X 54/Y 56; rest stays black. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A21

**SOURCE STATE:** V32/F13.0  
**TARGET STATE:** V33/F13.1  
**TIMESTAMP:** 01:10.875  
**MOTION TYPE:** character/caption reveal  
**MOTION HERO / ALLOWED MOTION:** bottom-right character and white caption  
**START STATE:** V32, matching the source description above.  
**END STATE:** V33, matching this card’s target configuration.  
**DIRECTION:** appears from lower-right edge  
**SPEED:** single comic beat  
**AMPLITUDE / PATH:** none; ROI X 56–97, Y 76–100  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:10.875.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** REPLACEMENT DRAWING + text overlay. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Locked camera. Reveal the small white line character at the bottom-right together with the caption MAYBE SOMETHING STRINGY? in one comic beat. Preserve the red DARK ENERGY cluster, small black hole, black background and every existing position exactly. Hold.”  
**CHARACTER COUNT:** 258 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A21: duplicate the stable source precomp; isolate X 56–97, Y 76–100; execute REPLACEMENT DRAWING + text overlay; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 73.125s, then use a hard cut into V34. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V33 as the exact observed state: red dark-energy cluster first, comic character second is the visual hero, ring center is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V34 — 74.250s — Nearby galaxy unaware

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V34_0074250ms.jpg](moon_protons_forensics/keyframes/V34_0074250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 73.125s / 74.250s  
**DURATION TO NEXT MATERIAL STATE:** 3.458s  
**STATE ID:** F14.0

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “But for the meantime, at least, nearby galaxies would be safe”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** But for the meantime, at least, nearby galaxies.  
**MOTION CUE:** A22  
**FUNCTION:** Begin the causal-delay explanation through deadpan personified dialogue.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Hard cut to a populated starfield; continuous zoom/black-hole expansion begins.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Begin the causal-delay explanation through deadpan personified dialogue. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** small black-hole ring.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: WHAT A BEAUTIFUL DAY; PROBLEMS  
**VISUAL HERO:** small black-hole ring.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring centers X 56/Y 56 at about 16% width; red caption X 15–41/Y 26–32; star specks fill the frame; center text is tiny but legible. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** small black-hole ring → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** small black-hole ring. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** NEW BASE / ANIMATION START STATE. **BASE:** F14.0 within S14. **CHANGES:** Hard cut to a populated starfield; continuous zoom/black-hole expansion begins. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white stars/ring/text, red dialogue. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. Exact composition: Ring centers X 56/Y 56 at about 16% width; red caption X 15–41/Y 26–32; star specks fill the frame; center text is tiny but legible. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white stars/ring/text, red dialogue. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.0, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** WHAT A BEAUTIFUL DAY; PROBLEMS Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white stars/ring/text, red dialogue), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.0. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Nearby galaxy unaware. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F13.1. **CURRENT:** F14.0. **NEXT:** F14.1. **TRANSITION INTO CURRENT:** Hard cut to a populated starfield; continuous zoom/black-hole expansion begins. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A22:** continuous scale/reframe; V34/F14.0 → V39/F14.5; 01:13.125–01:28.125; target black-hole ring with coordinated starfield approach; relationship CAMERA-SUBJECT COUPLED / PERSISTENT.

### 17. WHY MOVE

**A22 — WHY:** Visualizes the finite-speed arrival of gravitational influence. **Direction:** ring expands outward toward frame edges follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** steady slow acceleration impression; amplitude/path radial scale from fixed center; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** black-hole ring with coordinated starfield approach. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** none at this transition. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**A22: CAMERA-SUBJECT COUPLED / PERSISTENT** because visualizes the finite-speed arrival of gravitational influence.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** 2.5D EDITOR KEYFRAMES / HYBRID. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A22 MEDIUM. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A22 PASS:** source V34/F14.0; animate only black-hole ring with coordinated starfield approach; target region full frame; ring centered near X 56/Y 58; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** YES. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A22 SOURCE FRAME STATE:** V34/F14.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V34. **SOURCE IMAGE PROMPT:** build V34 as a 720×1280 text-free hand-drawn clean plate: A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. Layout: Ring centers X 56/Y 56 at about 16% width; red caption X 15–41/Y 26–32; star specks fill the frame; center text is tiny but legible. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A22

**SOURCE STATE:** V34/F14.0  
**TARGET STATE:** V39/F14.5  
**TIMESTAMP:** 01:13.125–01:28.125  
**MOTION TYPE:** continuous scale/reframe  
**MOTION HERO / ALLOWED MOTION:** black-hole ring with coordinated starfield approach  
**START STATE:** V34, matching the source description above.  
**END STATE:** V39, matching this card’s target configuration.  
**DIRECTION:** ring expands outward toward frame edges  
**SPEED:** steady slow acceleration impression  
**AMPLITUDE / PATH:** radial scale from fixed center; ROI full frame; ring centered near X 56/Y 58  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:13.125–01:28.125.  
**SIMULTANEOUS EVENTS:** none unless listed in relationship.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** 2.5D EDITOR KEYFRAMES / HYBRID. **AI SUITABILITY:** MEDIUM.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** YES—source and target states listed; use when testing AI.  
**AI PROMPT:** “Slowly push toward the black hole so its luminous ring expands from a small central circle to nearly the full frame by the end. Keep the ring center stable; star specks enlarge and drift outward consistently with the push. Preserve all caption layers in fixed screen space. Smooth continuous motion, no shake.”  
**CHARACTER COUNT:** 309 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A22: duplicate the stable source precomp; isolate full frame; ring centered near X 56/Y 58; execute 2.5D EDITOR KEYFRAMES / HYBRID; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 76.583s, then use a local additive/replacement event into V35. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V34 as the exact observed state: small black-hole ring is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V35 — 77.000s — Business-as-usual dialogue

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V35_0077000ms.jpg](moon_protons_forensics/keyframes/V35_0077000ms.jpg)  
**STATE IN / REPRESENTATIVE:** 76.583s / 77.000s  
**DURATION TO NEXT MATERIAL STATE:** 1.792s  
**STATE ID:** F14.1

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the black-hole ring is larger; red JUST MINDING MY OWN BUSINESS… replaces the first caption and white BIGGER PROBLEMS sits inside the ring. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The black-hole ring is larger; red JUST MINDING MY OWN BUSINESS… replaces the first caption and white BIGGER PROBLEMS sits inside the ring. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “since the gravitational influence of the black hole”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** since the gravitational influence of the black hole.  
**MOTION CUE:** A23; A24  
**FUNCTION:** Contrast complacent dialogue with visibly approaching danger.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Persistent ring expansion continues; red and white caption layers are replaced.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Contrast complacent dialogue with visibly approaching danger. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** expanding ring.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: JUST MINDING MY OWN BUSINESS…; BIGGER PROBLEMS  
**VISUAL HERO:** expanding ring.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring now spans roughly 28% width centered X 57/Y 57; red caption X 16–48/Y 25–32; white caption centers inside. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** expanding ring → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** expanding ring. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** MODIFIED REUSE / INTERMEDIATE STATE. **BASE:** F14.1 within S14. **CHANGES:** Persistent ring expansion continues; red and white caption layers are replaced. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The black-hole ring is larger; red JUST MINDING MY OWN BUSINESS… replaces the first caption and white BIGGER PROBLEMS sits inside the ring. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white, red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. The black-hole ring is larger; red JUST MINDING MY OWN BUSINESS… replaces the first caption and white BIGGER PROBLEMS sits inside the ring. Exact composition: Ring now spans roughly 28% width centered X 57/Y 57; red caption X 16–48/Y 25–32; white caption centers inside. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white, red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.1, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** JUST MINDING MY OWN BUSINESS…; BIGGER PROBLEMS Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white, red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.1. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Business-as-usual dialogue. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F14.0. **CURRENT:** F14.1. **NEXT:** F14.2. **TRANSITION INTO CURRENT:** Persistent ring expansion continues; red and white caption layers are replaced. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A23:** white text replacement; V34/F14.0 → V35/F14.1; approximately 01:15.000; target PROBLEMS becomes BIGGER PROBLEMS; relationship STATE REPLACEMENT over A22.

- **A24:** red text replacement; V34/F14.0 → V35/F14.1; 01:16.583; target WHAT A BEAUTIFUL DAY becomes JUST MINDING MY OWN BUSINESS…; relationship SIMULTANEOUS INDEPENDENT over A22.

**OTHER ACTIVE / PERSISTENT:** A22 persistent black-hole expansion.

### 17. WHY MOVE

**A23 — WHY:** Escalates wording with the approaching boundary. **Direction:** replacement inside ring follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

**A24 — WHY:** Sustains dramatic irony as danger approaches. **Direction:** replacement upper-left follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** PROBLEMS becomes BIGGER PROBLEMS; WHAT A BEAUTIFUL DAY becomes JUST MINDING MY OWN BUSINESS…. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A22 persistent black-hole expansion. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** YES. Use isolated text/vector passes over the pre-rendered A22 base; never regenerate the whole frame.

### 20. MOTION COUPLING CLASSIFICATION

**A23: STATE REPLACEMENT over A22** because escalates wording with the approaching boundary.; **A24: SIMULTANEOUS INDEPENDENT over A22** because sustains dramatic irony as danger approaches.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A23 LOW, A24 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A23 PASS:** source V34/F14.0; animate only PROBLEMS becomes BIGGER PROBLEMS; target region inside black-hole ring; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

**A24 PASS:** source V34/F14.0; animate only WHAT A BEAUTIFUL DAY becomes JUST MINDING MY OWN BUSINESS…; target region X 14–49, Y 23–34; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A23 SOURCE FRAME STATE:** V34/F14.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V34. **SOURCE IMAGE PROMPT:** build V34 as a 720×1280 text-free hand-drawn clean plate: A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. Layout: Ring centers X 56/Y 56 at about 16% width; red caption X 15–41/Y 26–32; star specks fill the frame; center text is tiny but legible. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

**A24 SOURCE FRAME STATE:** V34/F14.0. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V34. **SOURCE IMAGE PROMPT:** build V34 as a 720×1280 text-free hand-drawn clean plate: A sparse white starfield surrounds a small white-ringed black hole near the center; red WHAT A BEAUTIFUL DAY sits upper-left and small white PROBLEMS text sits inside the hole. Layout: Ring centers X 56/Y 56 at about 16% width; red caption X 15–41/Y 26–32; star specks fill the frame; center text is tiny but legible. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A23

**SOURCE STATE:** V34/F14.0  
**TARGET STATE:** V35/F14.1  
**TIMESTAMP:** approximately 01:15.000  
**MOTION TYPE:** white text replacement  
**MOTION HERO / ALLOWED MOTION:** PROBLEMS becomes BIGGER PROBLEMS  
**START STATE:** V34, matching the source description above.  
**END STATE:** V35, matching this card’s target configuration.  
**DIRECTION:** replacement inside ring  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI inside black-hole ring  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at approximately 01:15.000.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the same locked-center black-hole expansion. Replace only the white interior caption PROBLEMS with BIGGER PROBLEMS in one clean step. Keep the red caption in fixed screen space and preserve the ring motion, starfield, black background and all other geometry.”  
**CHARACTER COUNT:** 267 / 500  
**STATUS:** PASS

#### ANIMATION A24

**SOURCE STATE:** V34/F14.0  
**TARGET STATE:** V35/F14.1  
**TIMESTAMP:** 01:16.583  
**MOTION TYPE:** red text replacement  
**MOTION HERO / ALLOWED MOTION:** WHAT A BEAUTIFUL DAY becomes JUST MINDING MY OWN BUSINESS…  
**START STATE:** V34, matching the source description above.  
**END STATE:** V35, matching this card’s target configuration.  
**DIRECTION:** replacement upper-left  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 14–49, Y 23–34  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:16.583.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the smooth locked-center black-hole expansion. Replace only the red upper-left caption with JUST MINDING MY OWN BUSINESS… in one clean step. Keep the white interior text, ring, starfield, black background and every other element unchanged apart from the ongoing push.”  
**CHARACTER COUNT:** 276 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A23: duplicate the stable source precomp; isolate inside black-hole ring; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold; A24: duplicate the stable source precomp; isolate X 14–49, Y 23–34; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 78.375s, then use a local additive/replacement event into V36. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V35 as the exact observed state: expanding ring is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V36 — 78.750s — Even bigger problems

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V36_0078750ms.jpg](moon_protons_forensics/keyframes/V36_0078750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 78.375s / 78.750s  
**DURATION TO NEXT MATERIAL STATE:** 1.667s  
**STATE ID:** F14.2

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “can only expand outward at the speed of light”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** can only expand outward at the speed of.  
**MOTION CUE:** A25  
**FUNCTION:** Make causal propagation visible as a literal approaching boundary.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the white interior caption is replaced while A22 continues.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Make causal propagation visible as a literal approaching boundary. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** growing causal boundary.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: JUST MINDING MY OWN BUSINESS…; EVEN BIGGER PROBLEMS  
**VISUAL HERO:** growing causal boundary.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring about 35% frame width; starfield remains behind; captions stay registered in their screen regions. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** growing causal boundary → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** growing causal boundary. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / INTERMEDIATE STATE. **BASE:** F14.2 within S14. **CHANGES:** Only the white interior caption is replaced while A22 continues. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white, red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. The ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. Exact composition: Ring about 35% frame width; starfield remains behind; captions stay registered in their screen regions. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white, red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.2, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** JUST MINDING MY OWN BUSINESS…; EVEN BIGGER PROBLEMS Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white, red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.2. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Even bigger problems. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F14.1. **CURRENT:** F14.2. **NEXT:** F14.3. **TRANSITION INTO CURRENT:** Only the white interior caption is replaced while A22 continues. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A25:** white text replacement; V35/F14.1 → V36/F14.2; 01:18.375; target BIGGER PROBLEMS becomes EVEN BIGGER PROBLEMS; relationship STATE REPLACEMENT over A22.

**OTHER ACTIVE / PERSISTENT:** A22 persistent black-hole expansion.

### 17. WHY MOVE

**A25 — WHY:** Continues the size/verbal escalation. **Direction:** replacement inside ring follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** BIGGER PROBLEMS becomes EVEN BIGGER PROBLEMS. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A22 persistent black-hole expansion. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** YES. Use isolated text/vector passes over the pre-rendered A22 base; never regenerate the whole frame.

### 20. MOTION COUPLING CLASSIFICATION

**A25: STATE REPLACEMENT over A22** because continues the size/verbal escalation.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A25 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A25 PASS:** source V35/F14.1; animate only BIGGER PROBLEMS becomes EVEN BIGGER PROBLEMS; target region inside black-hole ring; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A25 SOURCE FRAME STATE:** V35/F14.1. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V35. **SOURCE IMAGE PROMPT:** build V35 as a 720×1280 text-free hand-drawn clean plate: The black-hole ring is larger; red JUST MINDING MY OWN BUSINESS… replaces the first caption and white BIGGER PROBLEMS sits inside the ring. Layout: Ring now spans roughly 28% width centered X 57/Y 57; red caption X 16–48/Y 25–32; white caption centers inside. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A25

**SOURCE STATE:** V35/F14.1  
**TARGET STATE:** V36/F14.2  
**TIMESTAMP:** 01:18.375  
**MOTION TYPE:** white text replacement  
**MOTION HERO / ALLOWED MOTION:** BIGGER PROBLEMS becomes EVEN BIGGER PROBLEMS  
**START STATE:** V35, matching the source description above.  
**END STATE:** V36, matching this card’s target configuration.  
**DIRECTION:** replacement inside ring  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI inside black-hole ring  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:18.375.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the same smooth black-hole push. Replace only the white interior caption BIGGER PROBLEMS with EVEN BIGGER PROBLEMS in one clean step. Preserve the red dialogue in fixed screen space, ring center, starfield motion, black background and all other geometry.”  
**CHARACTER COUNT:** 263 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A25: duplicate the stable source precomp; isolate inside black-hole ring; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 80.042s, then use a local additive/replacement event into V37. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V36 as the exact observed state: growing causal boundary is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V37 — 81.500s — Problem finally comprehended

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V37_0081500ms.jpg](moon_protons_forensics/keyframes/V37_0081500ms.jpg)  
**STATE IN / REPRESENTATIVE:** 80.042s / 81.500s  
**DURATION TO NEXT MATERIAL STATE:** 3.375s  
**STATE ID:** F14.3

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see a much larger ring encloses PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE, while red HO HUM sits above-left. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** A much larger ring encloses PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE, while red HO HUM sits above-left. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “Most of the universe around us would remain blissfully unaware”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** Most of the universe around us would remain.  
**MOTION CUE:** A26; A27  
**FUNCTION:** Escalate the wording in lockstep with the approaching ring while sustaining irony.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Red dialogue and white interior caption are independently replaced; ring expansion continues.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Escalate the wording in lockstep with the approaching ring while sustaining irony. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** large ring and three-line payoff caption.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: HO HUM; PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE  
**VISUAL HERO:** large ring and three-line payoff caption.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring spans roughly 55% frame width centered X 57/Y 59; three white lines center inside; red HO HUM sits X 28–43/Y 26–31. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** large ring and three-line payoff caption → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** large ring and three-line payoff caption. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / INTERMEDIATE STATE. **BASE:** F14.3 within S14. **CHANGES:** Red dialogue and white interior caption are independently replaced; ring expansion continues. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** A much larger ring encloses PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE, while red HO HUM sits above-left. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white, red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. A much larger ring encloses PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE, while red HO HUM sits above-left. Exact composition: Ring spans roughly 55% frame width centered X 57/Y 59; three white lines center inside; red HO HUM sits X 28–43/Y 26–31. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white, red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.3, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** HO HUM; PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white, red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.3. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Problem finally comprehended. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F14.2. **CURRENT:** F14.3. **NEXT:** F14.4. **TRANSITION INTO CURRENT:** Red dialogue and white interior caption are independently replaced; ring expansion continues. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A26:** red text replacement; V36/F14.2 → V37/F14.3; 01:20.042; target JUST MINDING… becomes HO HUM; relationship SIMULTANEOUS INDEPENDENT over A22.

- **A27:** white text replacement; V36/F14.2 → V37/F14.3; approximately 01:21.000; target EVEN BIGGER PROBLEMS becomes three-line payoff; relationship STATE REPLACEMENT over A22.

**OTHER ACTIVE / PERSISTENT:** A22 persistent black-hole expansion.

### 17. WHY MOVE

**A26 — WHY:** Maintains calm denial against growing visual threat. **Direction:** replacement upper-left follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

**A27 — WHY:** Delivers the verbal magnitude payoff. **Direction:** replacement inside ring follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** JUST MINDING… becomes HO HUM; EVEN BIGGER PROBLEMS becomes three-line payoff. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A22 persistent black-hole expansion. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** YES. Use isolated text/vector passes over the pre-rendered A22 base; never regenerate the whole frame.

### 20. MOTION COUPLING CLASSIFICATION

**A26: SIMULTANEOUS INDEPENDENT over A22** because maintains calm denial against growing visual threat.; **A27: STATE REPLACEMENT over A22** because delivers the verbal magnitude payoff.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A26 LOW, A27 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A26 PASS:** source V36/F14.2; animate only JUST MINDING… becomes HO HUM; target region X 26–45, Y 23–32; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

**A27 PASS:** source V36/F14.2; animate only EVEN BIGGER PROBLEMS becomes three-line payoff; target region inside black-hole ring; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A26 SOURCE FRAME STATE:** V36/F14.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V36. **SOURCE IMAGE PROMPT:** build V36 as a 720×1280 text-free hand-drawn clean plate: The ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. Layout: Ring about 35% frame width; starfield remains behind; captions stay registered in their screen regions. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

**A27 SOURCE FRAME STATE:** V36/F14.2. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V36. **SOURCE IMAGE PROMPT:** build V36 as a 720×1280 text-free hand-drawn clean plate: The ring continues enlarging behind the same red business-as-usual caption, while the interior text now reads EVEN BIGGER PROBLEMS. Layout: Ring about 35% frame width; starfield remains behind; captions stay registered in their screen regions. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A26

**SOURCE STATE:** V36/F14.2  
**TARGET STATE:** V37/F14.3  
**TIMESTAMP:** 01:20.042  
**MOTION TYPE:** red text replacement  
**MOTION HERO / ALLOWED MOTION:** JUST MINDING… becomes HO HUM  
**START STATE:** V36, matching the source description above.  
**END STATE:** V37, matching this card’s target configuration.  
**DIRECTION:** replacement upper-left  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 26–45, Y 23–32  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:20.042.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the locked-center black-hole expansion. Replace only the red upper-left dialogue with HO HUM in one clean step. Keep the white interior caption, starfield, ring glow, black background and all positions stable apart from the ongoing scale push.”  
**CHARACTER COUNT:** 252 / 500  
**STATUS:** PASS

#### ANIMATION A27

**SOURCE STATE:** V36/F14.2  
**TARGET STATE:** V37/F14.3  
**TIMESTAMP:** approximately 01:21.000  
**MOTION TYPE:** white text replacement  
**MOTION HERO / ALLOWED MOTION:** EVEN BIGGER PROBLEMS becomes three-line payoff  
**START STATE:** V36, matching the source description above.  
**END STATE:** V37, matching this card’s target configuration.  
**DIRECTION:** replacement inside ring  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI inside black-hole ring  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at approximately 01:21.000.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the same smooth push. Replace only the white interior text with three centered lines: PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE. Preserve exact screen-space registration of HO HUM, ring center, starfield, black background and all other elements.”  
**CHARACTER COUNT:** 262 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A26: duplicate the stable source precomp; isolate X 26–45, Y 23–32; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold; A27: duplicate the stable source precomp; isolate inside black-hole ring; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 83.417s, then use a local additive/replacement event into V38. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V37 as the exact observed state: large ring and three-line payoff caption is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V38 — 84.250s — LA LA LA denial

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V38_0084250ms.jpg](moon_protons_forensics/keyframes/V38_0084250ms.jpg)  
**STATE IN / REPRESENTATIVE:** 83.417s / 84.250s  
**DURATION TO NEXT MATERIAL STATE:** 2.583s  
**STATE ID:** F14.4

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the ring grows past two-thirds frame width; LA LA LA replaces HO HUM while the three-line white problem caption remains centered. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The ring grows past two-thirds frame width; LA LA LA replaces HO HUM while the three-line white problem caption remains centered. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “remain blissfully unaware of our ridiculous electron experiment”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** remain blissfully unaware of our ridiculous electron experiment.  
**MOTION CUE:** A28  
**FUNCTION:** Heighten dark comedy through deliberate denial as the threat fills the frame.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** Only the red caption is replaced; A22 continues.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** Heighten dark comedy through deliberate denial as the threat fills the frame. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** encroaching ring.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: LA LA LA; PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE  
**VISUAL HERO:** encroaching ring.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring approaches X 16–96/Y 33–91; red caption X 28–45/Y 25–30; white payoff text stays centered around Y 52. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** encroaching ring → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** encroaching ring. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** TEXT MODIFICATION / INTERMEDIATE STATE. **BASE:** F14.4 within S14. **CHANGES:** Only the red caption is replaced; A22 continues. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The ring grows past two-thirds frame width; LA LA LA replaces HO HUM while the three-line white problem caption remains centered. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white, red. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. The ring grows past two-thirds frame width; LA LA LA replaces HO HUM while the three-line white problem caption remains centered. Exact composition: Ring approaches X 16–96/Y 33–91; red caption X 28–45/Y 25–30; white payoff text stays centered around Y 52. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white, red. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.4, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** LA LA LA; PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white, red), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.4. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** LA LA LA denial. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F14.3. **CURRENT:** F14.4. **NEXT:** F14.5. **TRANSITION INTO CURRENT:** Only the red caption is replaced; A22 continues. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

- **A28:** red text replacement; V37/F14.3 → V38/F14.4; 01:23.417; target HO HUM becomes LA LA LA; relationship SIMULTANEOUS INDEPENDENT over A22.

**OTHER ACTIVE / PERSISTENT:** A22 persistent black-hole expansion.

### 17. WHY MOVE

**A28 — WHY:** Caps the denial joke while the ring overwhelms the frame. **Direction:** replacement upper-left follows the depicted force, causal path, or screen-space annotation location. **Speed/amplitude/type:** instant; amplitude/path none; the minimal change preserves reading and reference fidelity.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** HO HUM becomes LA LA LA. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A22 persistent black-hole expansion. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** YES. Use isolated text/vector passes over the pre-rendered A22 base; never regenerate the whole frame.

### 20. MOTION COUPLING CLASSIFICATION

**A28: SIMULTANEOUS INDEPENDENT over A22** because caps the denial joke while the ring overwhelms the frame.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** A28 LOW. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

**A28 PASS:** source V37/F14.3; animate only HO HUM becomes LA LA LA; target region X 27–47, Y 23–32; lock every unrelated pixel/overlay; composite only that ROI over the stable source. **Single-pass eligible:** NO / deterministic preferred. **All-AI isolation option:** run the same local pass, mask only the ROI, and accept increased geometry/text drift risk.

### 24. SOURCE IMAGE FOR EACH AI PASS

**A28 SOURCE FRAME STATE:** V37/F14.3. **SOURCE IMAGE TYPE:** REFERENCE FRAME or generated clean plate matching V37. **SOURCE IMAGE PROMPT:** build V37 as a 720×1280 text-free hand-drawn clean plate: A much larger ring encloses PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE, while red HO HUM sits above-left. Layout: Ring spans roughly 55% frame width centered X 57/Y 59; three white lines center inside; red HO HUM sits X 28–43/Y 26–31. Preserve source object count, scale, frontal camera, palette, line weight and negative space; add exact typography later.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

#### ANIMATION A28

**SOURCE STATE:** V37/F14.3  
**TARGET STATE:** V38/F14.4  
**TIMESTAMP:** 01:23.417  
**MOTION TYPE:** red text replacement  
**MOTION HERO / ALLOWED MOTION:** HO HUM becomes LA LA LA  
**START STATE:** V37, matching the source description above.  
**END STATE:** V38, matching this card’s target configuration.  
**DIRECTION:** replacement upper-left  
**SPEED:** instant  
**AMPLITUDE / PATH:** none; ROI X 27–47, Y 23–32  
**CAMERA:** locked unless A22 explicitly performs the coupled push.  
**TRIGGER:** narration/diagram step at 01:23.417.  
**SIMULTANEOUS EVENTS:** A22 persistent push.  
**STATIC ANCHORS:** every unrelated object, background, label, frame edge and coordinate reference.  
**CONFIDENCE:** HIGH for occurrence/direction; MEDIUM for subframe easing.  
**PRIMARY METHOD:** EDITOR TEXT REPLACEMENT. **AI SUITABILITY:** LOW.  
**MOTION-CUE CONFLICT:** source supports the described motion/change; no contradictory blur or directional marks.  
**FIRST/LAST FRAME:** NO—deterministic reveal/replacement is more exact.  
**AI PROMPT:** “Continue the locked-center black-hole expansion. Replace only the red upper-left caption HO HUM with LA LA LA in one clean step. Keep the three-line white payoff text fixed inside the ring, and preserve the starfield, ring glow, black background and all other geometry.”  
**CHARACTER COUNT:** 269 / 500  
**STATUS:** PASS

### 26. EDITOR / COMPOSITING BUILD

**LAYERS REQUIRED:** clean base plate, main-object/diagram layer, exact graphics, typography, red accent where applicable, and local masks/precomps. **BUILD ORDER:** A28: duplicate the stable source precomp; isolate X 27–47, Y 23–32; execute EDITOR TEXT REPLACEMENT; preserve exact registration; composite the changed region over the source; verify start/end and hold. **AFTER EFFECTS:** shape layers/trim paths/text/replacement precomps/2.5D scale as applicable. **PREMIERE/CAPCUT:** use PNG state replacements and exact overlay text; keyframe scale only for A22. Recreation method; original software not verified. **LEAKAGE RISKS:** background, text, geometry and identity drift; prevent by using the base plate outside the masked ROI.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 86.000s, then use a local additive/replacement event into V39. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V38 as the exact observed state: encroaching ring is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## V39 — 87.750s — Final giant ring

**SHOT:** S14  
**SOURCE REFERENCE FRAME:** [V39_0087750ms.jpg](moon_protons_forensics/keyframes/V39_0087750ms.jpg)  
**STATE IN / REPRESENTATIVE:** 86.000s / 87.750s  
**DURATION TO NEXT MATERIAL STATE:** 2.137s  
**STATE ID:** F14.5

### 1. WHAT THE VIEWER SEES

If you paused the video here, you would see the black-hole ring nearly touches the left and right frame edges; stars remain outside and the white three-line caption stays centered inside the black disk. Background/midground/foreground are deliberately flattened; object relationships are established by screen position, scale, overlap and line direction. The current motion state is an observed post-change or active-motion state. **LITERAL FRAME DESCRIPTION:** The black-hole ring nearly touches the left and right frame edges; stars remain outside and the white three-line caption stays centered inside the black disk. **Confidence: HIGH.**

### 2. SCRIPT ↔ VISUAL SYNC

**SPOKEN WORDS:** “until they suddenly…”  
**VISUAL APPEARS:** DURING the matching idea.  
**TRIGGER WORD / IDEA:** until they suddenly….  
**MOTION CUE:** No in-shot animation; state is reached by cut or held.  
**FUNCTION:** End on an unfinished causal sentence exactly as the danger overtakes the frame.

### 3. CHANGE FROM PREVIOUS

**ADDED / REMOVED / MOVED / ROTATED / REVOLVED / RESIZED / RECOLORED / REFRAMED / REPLACED / TEXT:** A22 reaches its observed end scale; the red dialogue has disappeared and the white payoff text remains.  
**STATIC:** the state’s coordinate frame, background polarity, unchanged objects, and registered proof geometry. No unobserved parallax, drift, wobble, lighting pulse, or camera breathing is introduced.

### 4. VISUAL PURPOSE

**Information class:** EMOTIONAL. **Purpose:** End on an unfinished causal sentence exactly as the danger overtakes the frame. If removed, the viewer would lose either the causal step, quantitative proof, scale transition, contradiction, or emotional punctuation tied to this narration beat.

### 5. CONSTRUCTION MAP

**BACKGROUND:** black negative space.  
**MAIN SUBJECT:** frame-filling black-hole boundary.  
**SECONDARY:** all support objects described in the literal state.  
**GRAPHICS:** dashed guides, arrows, line fields, stipple, or glow only where visible.  
**TEXT:** deterministic overlay: PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE  
**VISUAL HERO:** frame-filling black-hole boundary.  
**STATIC COORDINATE FRAME:** ring center and screen-space captions.  
**LAYER ORDER:** Layer 1 background field; Layer 2 environment/base geometry; Layer 3 main objects; Layer 4 proof graphics; Layer 5 exact black/white text; Layer 6 scarce red accents; Layer 7 local glow only if visible.

### 6. EXACT LAYOUT

**CANVAS:** 720×1280 portrait. **ASPECT RATIO:** 9:16.  
**MAIN / SECONDARY / CROP / MARGINS / DEPTH:** Ring exceeds 85% frame width, centered slightly right; upper and lower arcs crop near frame edges; center caption remains small and stable. Depth is graphic, not photographic.  
**NEGATIVE SPACE:** preserve all unoccupied regions; they stabilize reading.  
**PRIMARY EYE PATH:** frame-filling black-hole boundary → newly changed annotation or scarce red accent → supporting label/equation → contextual character/environment. Coordinates are approximate normalized visual maps, not pixel measurements.

### 7. ATTENTION ORDER

**FIRST LOOK:** frame-filling black-hole boundary. **SECOND LOOK:** any newly added arrow/text/contrast accent. **THIRD LOOK:** small formula, label, or character reaction. **WHY:** scale and tonal contrast establish the hero; sparse motion/replacement creates the next pull; typography resolves meaning last. **ATTENTION COMPETITION:** minimal except deliberately dense explosion/collapse states. **CONTROL DEVICE:** isolated change inside a stable coordinate frame. **CLASSIFICATION:** CONTROLLED.

### 8. IMAGE REUSE STATUS

**STATUS:** ANIMATION END STATE. **BASE:** F14.5 within S14. **CHANGES:** A22 reaches its observed end scale; the red dialogue has disappeared and the white payoff text remains. Reuse must preserve unchanged coordinates rather than regenerate the full frame.

### 9. IMAGE DNA

**OUTPUT TYPE:** black-field hand-drawn cosmic explainer frame. **SUBJECT / POSE / MATERIAL / ENVIRONMENT / GEOMETRY:** The black-hole ring nearly touches the left and right frame edges; stars remain outside and the white three-line caption stays centered inside the black disk. **CAMERA:** straight-on locked diagram/page view. **LIGHTING:** flat paper field or localized observed glow only. **COLOR:** black, white. **STYLE:** thin imperfect black ink, flat gray/stipple, sparse red, generous negative space. **TEXT:** overlay, not generated. **GRAPHICS:** exact deterministic paths wherever geometry matters.

### 10. EXACT STANDALONE IMAGE PROMPT

**EXACT STANDALONE IMAGE PROMPT:** Create a 720×1280 vertical 9:16 black-field hand-drawn cosmic explainer frame matching a minimalist scientific notebook animation. The black-hole ring nearly touches the left and right frame edges; stars remain outside and the white three-line caption stays centered inside the black disk. Exact composition: Ring exceeds 85% frame width, centered slightly right; upper and lower arcs crop near frame edges; center caption remains small and stable. Use thin slightly irregular hand-inked outlines, simple flat shapes, sparse stipple where visible, and black negative space. Palette: black, white. Use a straight-on flat diagram perspective with no photographic lens effect, no decorative texture, no extra objects, no particles unless explicitly described, and no camera tilt. Produce a clean plate without any letters, words, numbers, equations, plus/minus symbols, or captions; reserve the observed text regions as empty space for deterministic overlays. Preserve the stated object count, relative scale, screen positions, crop, line weight, background polarity, visual hierarchy and negative-space distribution with strict reference fidelity. This is the exact source-image state F14.5, not a stylistic variation.

### 11. TEXT BAKE / OVERLAY DECISION

**BAKE TEXT:** NO.  
**CLEAN PLATE REQUIREMENT:** generate the scene with all observed text zones empty; do not ask the image model to render letters, formulas, numbers, charge symbols, or captions.  
**TEXT OVERLAY SPEC:** PROBLEMS BIGGER / THAN YOU CAN / POSSIBLY IMAGINE Match source capitalization, line breaks, irregular hand-drawn weight, alignment, relative scale, and color (red/white as explicitly listed).

### 12. FIDELITY LOCK

**HUMAN PRODUCTION LOCK:** retain the same recurring character identity, pose/state, object count, object position, relative scale, map/diagram orientation, frontal camera, black negative space, flat lighting, palette (black, white), text plan, and empty-space pattern. **PROHIBITED CHANGES:** extra camera motion, lens effects, particles, glow pulses, background drift, random wobble, parallax, anatomy changes, decorative arrows, additional labels, or altered proof geometry.

### 13. IMAGE PROMPT COVERAGE AUDIT

**SUBJECT:** High. **POSE/STATE:** High. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High—clean plate plus exact overlay. **CONTINUITY:** High—persistent IDs and coordinate anchors specified. This audits prompt coverage, not generated-image fidelity.

### 14. FRAME STATE ID

**STATE:** F14.5. **SOURCE TYPE:** REFERENCE FRAME. **STABLE CONFIGURATION:** Final giant ring. **SHOT MEMBERSHIP:** S14 (73.125–88.137).

### 15. STATE-CHAIN POSITION

**PREVIOUS:** F14.4. **CURRENT:** F14.5. **NEXT:** final export. **TRANSITION INTO CURRENT:** A22 reaches its observed end scale; the red dialogue has disappeared and the white payoff text remains. **SEQUENCE RULE:** any later animation must use this current post-change state, not return to the original shot base.

### 16. COMPLETE MOTION EVENT INVENTORY

No new in-shot animation creates this state. It is an initial shot base, hard-cut replacement, continuous end state already governed by A22, or static hold. **ANIMATION REQUIRED:** NO for creating stillness.

**OTHER ACTIVE / PERSISTENT:** A22 persistent black-hole expansion.

### 17. WHY MOVE

No new motion is justified in this state. The image’s job is reading, comparison, consequence recognition, or a static pattern interrupt. Any AI-added drift would falsely imply new physics or steal attention.

### 18. WHAT STAYS STATIC

**STATIC ANCHORS:** ring center and screen-space captions; all objects not named as event targets; exact text layers except during their own replacement; background polarity; crop; line weight; lighting; and negative space. **WHY STATIC:** reading stability, comparison alignment, continuity, visual hierarchy, subject isolation, and prevention of cognitive overload.

### 19. MOTION INTERFERENCE ANALYSIS

**ALLOWED TO MOVE:** only the already-active A22 ring/starfield push. **LOCKED / MUST REMAIN STABLE:** all unrelated characters, diagrams, text, background regions, and camera unless A22 explicitly controls the push. **OTHER ACTIVE EVENTS:** A22 persistent black-hole expansion. **COULD THIS DISTURB ANOTHER MOVING ELEMENT?** NO. A local deterministic pass is sufficient.

### 20. MOTION COUPLING CLASSIFICATION

**PERSISTENT CAMERA-SUBJECT COUPLED:** A22 continues from V34 toward V39; later captions are independent screen-space layers.

### 21. RECOMMENDED PRODUCTION METHOD

**PRIMARY METHOD:** STATIC HOLD; enter/exit by editorial hard cut or graphic replacement. This choice follows reference fidelity: exact line geometry, typography, numbers, and diagram registration favor deterministic editor/replacement work; only coherent whole-frame scale motion is treated as 2.5D/hybrid. Original software is not verified.

### 22. AI SUITABILITY

**RATING:** N/A — static frame; generating motion would reduce fidelity. AI is least suitable for exact text, equations, arrow paths, diagram registration, and one-frame replacement states. Where rated MEDIUM, use AI only as an isolated approximation or first/last-frame pass and composite the accepted local region.

### 23. AI ISOLATION PLAN

No AI pass. Use the reference/generative master as a still, preserve it for the measured duration, and cut to the next state.

### 24. SOURCE IMAGE FOR EACH AI PASS

**SOURCE FRAME STATE:** F14.5. **SOURCE IMAGE TYPE:** REFERENCE FRAME / generated master image. No motion pass begins here unless the EDL cuts to the next shot.

### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS

**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold image for approximately 2.137s or until the measured cut/replacement. **AI PROMPT:** N/A. Static fidelity is achieved by not generating motion.

### 26. EDITOR / COMPOSITING BUILD

Place the verified still/clean plate on the timeline, add deterministic overlay text if specified, and hold. Do not add position, scale, opacity, blur, particle, or camera keyframes. Cut at the measured next boundary. Recreation method; original software not verified.

### 27. EDIT OUT / NEXT STATE

Hold until approximately 88.137s, then use a local additive/replacement event into END. Persistent elements are those shared by the same shot coordinate frame; changed elements are exactly those named in the next A-event or EDL shot replacement.

### 28. RECONSTRUCTION RULE

Reconstruct V39 as the exact observed state: frame-filling black-hole boundary is the visual hero, ring center and screen-space captions is the static coordinate reference, and only the explicitly inventoried event targets may move or change. Copy the production grammar and registration; do not add cinematic drift, decorative animation, invented text, or unobserved secondary motion.


## PASS 13 — Editing and audio reconstruction

### Editing grammar

Build each shot as a registered precomp. Establish its base plate, then add one local proof element at a time. Cut when the argument changes scale or domain; do not disguise semantic cuts with decorative transitions. S01, S03, S04, S05, S09, S13 and S14 contain meaningful state chains. S02, S06, S07, S08, S10, S11 and S12 are intentionally static bases/holds reached by hard cut. The repeated continuity device is not camera movement; it is the unchanged coordinate frame under an added arrow, label, equation, or replacement drawing.

**Fastest cluster:** 63.542–68.167 cycles local destruction → cosmic collapse → lone black hole in 4.625 s, driven by escalation and polarity inversion. **Slowest cluster:** 46.583–63.542 assembles the central proof; 73.125–88.137 lets a single physical motion carry the ending. **Cut motivations:** new argument, proof completion, contradiction, scale reset, or payoff—not beat-count uniformity.

### Audio map

| Audio element | Verified behavior | Visual relationship | Reconstruction |
|---|---|---|---|

| Narration | Center-dominant English speech, 24 source segments | Nearly every visual addition lands during the noun/claim it explains | Record dry, close narration; edit tightly; preserve brief natural gaps |

| Music | Cannot verify as a separable semantic layer | No source-grounded music cue is identified | Do not invent a track for fidelity; if a new production requires music, keep it subordinate and document it as a creative change |

| SFX | Cannot verify exact designed events | Visual flashes/cuts do not authorize invented effects | Rebuild with narration alone unless an audible event is independently confirmed |

| Ambience | No distinct ambience confidently isolated | White/black diagram environments are visually abstract | None required |

| Silence/fade | Measured low intervals 63.40–63.55, 66.95–67.20, 86.70–88.10 | Brief consequence resets and ending | Preserve the final low interval/fade; avoid filling it with extra audio |

## Thumbnail and Shorts extraction

### Thumbnail frame candidates

1. **00:06.500 / V04 — destructive flash.** Dominant object: huge white blast and recoiling stick figure. Mobile readability: high. Contradiction: tiny premise creates enormous destruction. Remove minor debris; enlarge blast/presenter; possible question: ‘THE MOST DESTRUCTIVE WHAT IF?’ Title relationship: strongest if title correctly states proton Earth/electron Moon.

2. **00:37.500 / V20 — 10⁵³ electron explosion.** Dominant object: radial electron burst on torn board. Mobile readability: medium-high. Remove small board equations; enlarge the 10⁵³ center and PLEASE STOP! reaction. Possible question: ‘WHAT HOLDS THIS TOGETHER?’

3. **01:01.500 / V28 — universe → black hole proof.** Dominant object: black universe sphere and converging arrows into a well. Mobile readability: medium; crop tighter to sphere/arrows/well and retain BLACK HOLE. Possible question: ‘A MOON WITH THE ENERGY OF THE UNIVERSE?’ This best represents the intellectual payoff.

4. **01:21.500 / V37 — expanding ring.** Dominant object: large luminous black-hole boundary with three-line caption. Mobile readability: high after enlarging text. Contradiction: calm HO HUM against approaching catastrophe. Possible question: ‘WOULD THE UNIVERSE NOTICE?’

### Shorts candidates

**Short A — ‘20 orders stronger’ (source 00:16.020–00:26.250, ≈10.2 s).** Hook: ‘Electron moons do not orbit proton planets.’ Core moment: two-electron arrows and 10²⁰·F. Payoff: electrostatic repulsion dwarfs gravity. Context required: one setup line identifying an electron Moon. Visuals: V09–V13. Use the standalone prompts and A07–A09 motion prompts. CTA: optional question, ‘What happens when there are 10⁵³ of them?’

**Short B — ‘A universe inside a Moon’ (source 00:38.960–01:03.000, ≈24 s).** Hook: stored energy gravitates like mass. Core moment: observable-universe sphere over tiny Moon. Payoff: black-hole well and BLACK HOLE label. Context: electron Moon stores extreme electrostatic PE. Visuals: V21–V28. Use A16–A19; keep equations as overlays. CTA: ‘Would it collapse the rest of the universe?’

**Short C — ‘They would not know yet’ (source 01:13.125–01:28.137, ≈15 s).** Hook: nearby galaxies are safe temporarily. Core: ring expands at light speed while captions escalate. Payoff: ‘until they suddenly…’ and frame-filling ring. Visuals V34–V39. Use deterministic A22 plus A23–A28 caption replacements. No extra CTA needed; the cutoff is the CTA-like replay device.

## PASS 14 — ENGINE D: Master production synthesis

### D1 — Story engine

**HOOK:** familiar system with impossible charges. **ESCALATION:** most destructive scenario; analogy rejected; force imbalance quantified; 10⁵³-particle scale. **REVERSAL:** the energy that should explode the Moon also gravitates and makes a black hole. **PAYOFF:** universe-scale consequences propagate causally, creating a dark-comic delay before arrival.

### D2 — Script engine

Mini-hooks are the giant-hydrogen analogy, ‘however’ reversal, 10²⁰ number, 10⁵³ scale, potential-energy bridge, observable-universe equivalence, and universe-collapse question. The BUT/THEREFORE spine prevents list-like sequencing. The payoff ladder grows mechanism → number → Moon → universe → causality. There is no CTA or next-video bridge; the ending spends its final attention on story closure.

### D3 — Visual engine

Composition uses top-board/lower-presenter, centered white-field proofs, and black-field cosmic scale. Camera is locked and frontal except the final push. Illustration is thin irregular ink with flat gray/stipple. B-roll is absent. Graphics and text are causal evidence, not decoration. Asset reuse is explicit: presenter, electron Moon, red accent, black-hole family, arrows, and typography recur in transformed roles.

### D4 — Motion engine

**What usually moves?** One annotation, replacement drawing, line/arrow, number, local pose, or final scale boundary. **What stays static?** Background, diagram frame, other labels, object centers, and proof geometry. **Static coordinate frame:** board border, vertical particle axis, centered diagram, universe sphere, or black-hole center. **Triggers:** spoken noun, quantified comparison, contradiction, or payoff word. **Isolation:** local vector/text/replacement passes over a base plate. **AI-friendly:** coherent ring push, loose red scribble, local transformation approximation. **Precise editor control:** all text, formulas, arrows, diagrams, and replacement drawings. **Single-pass:** only coupled physical actions with robust geometry; principally A22 if captions remain overlays. **Sequential states:** nearly every explanatory shot. **Simultaneous motion:** A07 arrows, A11 board/pose, A17 arrows, A22 ring/starfield. **Camera moves:** only A22. **Cut rather than animate:** when argument scale or visual domain changes.

**CREATOR MOTION FORMULA:** lock the explanatory coordinate frame → reveal one proof element → hold long enough to read → replace only the next local state → hard-cut when the argument changes scale → reserve continuous camera motion for the final causal payoff.

### D5 — AI reconstruction routing

**AI SINGLE-PASS STATES:** optional A06 scribble; optional A22 ring/starfield push. **AI MULTI-PASS STATES:** V35–V38 only if A22 base and caption regions are separately generated/masked; recommended captions remain editor layers. **AI STATE-CHAIN STATES:** optional A11, A15, A18 using listed first/last states. **FIRST/LAST FRAME STATES:** V15→V16, V19→V20, V26→V27, V34→V39. **HYBRID:** S14 continuous base motion plus deterministic captions. **EDITOR-ONLY:** all exact arrows, equations, labels, and most replacement drawings. **STATIC:** 11 source states require no generated motion.

### D6 — Image engine

**MASTER CHARACTER PROMPT:** Minimal hand-drawn stick-figure explainer character on a clean flat field; oval head without facial features, thin slightly irregular black ink limbs and torso, no clothing texture, readable pose silhouette, straight-on orthographic view, consistent proportions, generous negative space.

**MASTER OBJECT PROMPT:** Scientific explainer object rendered as a simple black/gray hand-inked diagram, thin imperfect outlines, sparse stipple or flat fill, exact count and relative scale, no photographic material, no invented labels, frontal geometry, isolated on clean white or black field.

**MASTER ENVIRONMENT PROMPT:** 9:16 minimalist notebook/whiteboard stage or black cosmic field; uncluttered flat background, strong central coordinate anchor, simple line-art environment only where required, no depth haze, no decorative particles beyond observed stars, no camera tilt.

**MASTER GRAPHIC PROMPT:** Thin hand-drawn arrows, dashed circles, radial fields, loose red contradiction marks, or wireframe grids with exact path and registration; single consistent line weight; no glow except observed black-hole/flash; reserve all typography for overlays.

**MASTER STYLE PROMPT:** 720×1280 vertical educational science animation frame, minimalist hand-drawn ink, irregular but controlled line, white/black polarity, flat gray and stipple, scarce saturated red, direct diagram hierarchy, large negative-space regions, no photorealism, no lens effects, no decorative motion cues.

**MASTER COLOR RULE:** white/black first, gray explanatory, red only for contradiction/alarm/uncertainty/dialogue. **MASTER TYPOGRAPHY RULE:** exact uppercase hand-drawn overlay; preserve wording, line breaks, alignment and screen-space hold; never rely on image generation for equations.

### D7 — Attention engine

Repeated eye path is central proof object → changed local element → scarce red accent or formula → human/comic reaction. Attention is controlled by motion scarcity: because most of the frame stays still, a small number pop or arrow reveal has high salience. In S14, the growing ring becomes the motion hero while captions stay small and fixed, producing threat without clutter.

### D8 — Callback engine

Electron Moon: introduced as a charged celestial object → reused as atomic analogue and 10⁵³ cluster → transformed into PE/explosion diagram → compressed to a tiny universe-energy marker → paid off as a black hole. Black hole: introduced as a local well → reused as lone cosmic anchor → contextualized by dark energy → transformed into the final causal boundary. Red: introduced as contradiction/alarm → reused for dark-energy uncertainty → paid off as unaware dialogue.

### D9 — Improvements

**CRITICAL — premise packaging. WHAT WORKS:** source narration is precise. **FRICTION:** filename says proton Moon, source says electron Moon/proton Earth. **WHY:** changes the physical scenario. **MINIMAL FIX:** correct title/filename. **AGGRESSIVE FIX:** rebuild title/thumbnail/opening as a single exact premise.

**HIGH — universe-energy derivation. WHAT WORKS:** reveal is memorable. **FRICTION:** equality is asserted. **WHY:** scientifically attentive viewers may question scale. **MINIMAL FIX:** add one compact equation/source card. **AGGRESSIVE FIX:** devote a 10–15 s derivation with dimensional assumptions.

**MEDIUM — abstraction density at 39–47 s. WHAT WORKS:** visual variety is high. **FRICTION:** three diagrams arrive rapidly. **WHY:** PE, curvature and mass-energy are conceptually distinct. **MINIMAL FIX:** retain one recurring Moon icon across all three. **AGGRESSIVE FIX:** animate a single state chain rather than three hard cuts.

**OPTIONAL — accessibility. WHAT WORKS:** high monochrome contrast. **FRICTION:** red/black handwriting is small in S14. **WHY:** mobile legibility. **MINIMAL FIX:** increase red caption size 15–20%. **AGGRESSIVE FIX:** add designed subtitles outside the proof geometry.

### D10 — New-topic translation

Use a new example topic such as ‘What if Earth were made of antimatter?’ without copying literal content.

| Original scene function | Original image mechanism | Original motion/edit mechanism | New-topic equivalent |
|---|---|---|---|

| Familiar premise | Labeled Earth/Moon board | two staged field replacements | labeled matter/antimatter Earth and incoming object; reveal annihilation relation |

| False intuition | paired macro/atomic orbit | labels then red strikeout | familiar energy intuition above, relativistic correction below; strike out invalid assumption |

| Quantitative proof | vertical arrows + 10²⁰·F | deterministic number/label reveal | matter–antimatter energy per kilogram with exact equation overlay |

| Scale escalation | whiteboard calculation ruptures | reaction text + replacement drawings | calculate total Earth mass-energy; presenter reacts; board replacement shows blast scale |

| Relativistic bridge | PE and E=mc² wells | hard graphic reset | compare chemical/nuclear energy to mass-energy on shared geometry |

| Mega payoff | universe sphere compressed to Moon | convergence arrows + local well transform | map released energy to planetary/stellar scale, then transform target locally |

| Causal-delay ending | growing black-hole ring | persistent 2.5D push + caption replacements | expanding radiation front with observers unaware until arrival |

**KEEP:** composition grammar, motion scarcity, isolation, proof pacing, transition logic, payoff ladder and asset callbacks. **CHANGE:** facts, objects, symbols, numbers, characters, labels, branding and literal imagery. **RULE:** copy production grammar, not surface content.

### D11 — Exact zero-to-final rebuild order

1. Lock the packaging promise to the actual proton-Earth/electron-Moon premise.

2. Record the 16 script beats and causal BUT/THEREFORE spine.

3. Build the 14-shot plan and 39-state timing map.

4. Create the 31 persistent assets with shared IDs and master line/color rules.

5. Generate/draw text-free master bases for every new shot coordinate frame.

6. Create every intermediate F-state required by the 28 A-events; never reuse F0 when F1 is required.

7. Add exact typography, equations, charge symbols and numbers as editor overlays.

8. Build replacement drawings for field changes, pose changes, explosions and local transforms.

9. Build exact arrows with shape layers/trim paths and exact text with opacity/replacement states.

10. Create A22 as one 15 s locked-center 2.5D push: ring scale plus starfield approach.

11. Composite A23–A28 as independent screen-space text replacements over A22.

12. Assemble the 14-shot EDL at measured boundaries; use hard cuts for semantic resets.

13. Lay in the center-dominant narration and preserve measured pauses/final fade.

14. Normalize line weight, white/black polarity, gray values and scarce red across shots.

15. Run continuity audit for presenter, Moon, black-hole center, text positions and diagram registration.

16. Run motion-leakage audit: no background drift, text drift, geometry drift, identity drift or extra camera motion.

17. Run packaging-payoff audit against title, opening, universe-energy reveal and final cutoff.

18. Export 720×1280, 24 fps, Rec.709, H.264 with stereo AAC and measured duration alignment.


## PASS 15 — Completeness and compliance audit

SOURCE VIDEO INSPECTED: YES  

MAJOR SHOTS: 14  

VISUAL STATES: 39  

SCRIPT BEATS: 16  

PERSISTENT ASSETS: 31  

VISUAL CARDS: 39/39  

STANDALONE IMAGE PROMPTS: 39/39  

TEXT BAKE DECISIONS: 39/39  

FRAME STATE CHAINS: 39/39  

TOTAL MOTION EVENTS: 28  

MOTION EVENTS IDENTIFIED: 28/28  

WHY-MOVE ANALYSIS: 28/28 events plus static-state justification  

STATIC-ANCHOR ANALYSIS: 39/39  

MOTION COUPLING CLASSIFIED: 28/28  

MOTION INTERFERENCE CHECK: 39/39  

AI SUITABILITY: 28/28 events; static states explicitly N/A  

PRIMARY METHODS: 39/39  

AI SINGLE-PASS: 2 optional candidates (A06, A22)  

AI MULTI-PASS: 6 text-over-persistent-motion states if all-AI is requested; editor isolation recommended  

AI STATE-CHAIN: 4 useful optional first/last packages  

FIRST/LAST FRAME: A11, A15, A18, A22  

HYBRID: S14 / A22–A28  

DETERMINISTIC: 25 events recommended deterministic or replacement-drawing primary  

STATIC: 11 base/static/end-state cards without a new local event; additional static holds embedded throughout  

AI SOURCE IMAGES IDENTIFIED: 28/28  

AI PROMPTS: 28/28  

AI PROMPTS ≤500: 28/28  

PROMPT CHARACTER COUNTS: 28/28 exact and reported  

TRANSITIONS: 13/13 major shot transitions plus all in-shot replacements  

EDL: COMPLETE  

AUDIO: COMPLETE for measurable mix/transcript; semantic music/SFX identification LIMITED by the mixed source  

MASTER SYNTHESIS: COMPLETE

### Final quality gate

**REFERENCE FIDELITY:** only observed cuts, replacements, reveals, pose changes, local jitter and final push are reconstructed; no decorative animation is introduced.  

**IMAGE:** every required stable state has a source frame, literal description, layout, clean-plate prompt, text plan and fidelity lock.  

**MOTION:** all 28 meaningful events have source/target states, direction, relationship, reason, static anchors, primary method and ≤500-character prompt.  

**MOTION ISOLATION:** exact graphics/text are editor layers; independent S14 captions are isolated over A22.  

**SAME FRAME:** coupled arrows/pose changes stay together; independent text replacements remain separate passes.  

**AI:** used only where coherent motion or local approximation is defensible; exact diagrams and type are not forced through generation.  

**STATE CHAIN:** every sequential event starts from the preceding completed state.  

**EDITING:** all local passes can be composited over a stable base without full-frame drift.  

**FINAL TEST:** a competent animator/editor can identify exactly which element moves, what stays locked, the event order, source image, method, isolation region, and final state without guessing. **PASS.**
