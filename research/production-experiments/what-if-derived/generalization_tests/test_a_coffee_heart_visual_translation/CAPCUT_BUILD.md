# CapCut Build Plan

Project: 2160 × 3840 (9:16). One audio layer, the unmodified narration. Camera
locked for the whole video — no keyframed scale or position on any base plate.

**Global rules (from the frozen brain):**
- Every shot boundary is a **hard cut**. No transition effect of any kind is
  applied anywhere. (`DECISION_RULES.md` §7 — all 186 corpus shot boundaries
  measure a 0.0s gap; zero fades exist.)
- Every reveal is an **opacity on/off at a single frame** or a **wipe mask
  along a fixed path**. No fade-in, no scale-in, no slide-in, no rotation.
  (`CAPCUT_PRODUCTION_SYSTEM.md` §1.)
- All words are **native text layers**. Nothing is baked into a generated
  image. (`ASSET_CREATION_SYSTEM.md`: 18/31 TEXT_SYSTEM rows are native editor
  text layers.)
- Reveals are placed on the **onset of their anchor word**, read off the
  waveform once narration is recorded. (`AUDIO_VISUAL_SYNC_DNA.md`:
  STATE_CHANGE median offset 37ms, 95.7% within 300ms.)
- Narration is never cut, shortened or gap-trimmed.
  (`CAPCUT_PRODUCTION_SYSTEM.md` §4.)

---

## SH01 — The binary question

**Source plate:** IMG01 (mug + heart), full frame, bottom of the stack, static.

**Track stack (bottom to top):**
1. IMG01 base plate
2. G02a — fork lines + left label plate (transparent PNG)
3. T01 — text layer `GOOD?`
4. G02b — right label plate (transparent PNG)
5. T02 — text layer `BAD?`
6. C01 — Dr. Rehan, arm-raised pose (transparent PNG)
7. G03 — red strike stroke (transparent PNG) + a left-to-right wipe mask

**Initial composition (F01.0):** layers 2–7 all hidden. Only the plate is
visible: mug and heart, empty lower two-thirds.

**Operations in order:**
| At | Operation | Layers touched |
|---|---|---|
| onset of "good" (w3) | Turn layers 2 and 3 visible, same frame | G02a, T01 |
| onset of "bad" (w7) | Turn layers 4 and 5 visible, same frame | G02b, T02 |
| onset of "Rehan" (w11) | Turn layer 6 visible, already in final position | C01 |
| onset of "wrong" (w16) | Turn layer 7 visible and run its wipe mask 0% → 100% left to right over ~0.5s | G03 |
| after "question." (w17) | **Hard cut** to SH01 → SH02. No transition effect. | all |

**End state:** F01.4 — full binary model with a red stroke across it, doctor
standing lower-left.

---

## SH02 — Coffee versus energy drink

**Source plate:** IMG02 (baseline + mug + the mug's two strokes), full frame,
static.

**Track stack (bottom to top):**
1. IMG02 base plate
2. O02 — energy-drink can (transparent PNG)
3. G04b — the can's four stimulation strokes, as one grouped PNG
4. G05 — red caution triangle (transparent PNG)

**Initial composition (F02.0):** layers 2–4 hidden. Coffee mug with its two
strokes on the left of the baseline; right half bare.

**Operations in order:**
| At | Operation | Layers touched |
|---|---|---|
| **Hard cut in** on "People" (w18) | SH01 out, SH02 in, no transition effect | — |
| onset of "energy" (w26) | Turn layer 2 visible at final position and scale | O02 |
| onset of "stronger" (w35) | Turn layer 3 visible — **one grouped layer, so all four strokes appear in the same frame** | G04b |
| onset of "dangerous" (w44) | Turn layer 4 visible. No pulse, no glow, no scale keyframes. | G05 |
| after "as well." (w48) | **Hard cut** to SH03 | all |

**End state:** F02.3 — mug with two strokes, can with four strokes and one
caution triangle above it.

---

## SH03 — The consultation, the rejection, the deletion

**Source plate:** IMG03 (Dr. Rehan + blank-plated compact fork), full frame,
static.

**Track stack (bottom to top):**
1. IMG03 base plate
2. **Diagram group** — this must be built as a single compound/grouped clip
   containing the mug, both branch lines and both plates, plus the T01 `GOOD?`
   and T02 `BAD?` text layers nested inside it. Grouping is mandatory: A10
   deletes all of it in one frame.
   *(If the diagram is baked into IMG03's plate, duplicate IMG03, erase the
   diagram from the duplicate, and cut to that duplicate at A10 instead —
   same visual result, one extra plate.)*
3. C02 — patient figure (transparent PNG)
4. G03 — red strike stroke (reused asset) + a left-to-right wipe mask

**Initial composition (F03.0):** layers 3 and 4 hidden. Doctor left, labelled
fork upper-centre, right field empty.

**Operations in order:**
| At | Operation | Layers touched |
|---|---|---|
| **Hard cut in** on "So" (w49) | SH02 out, SH03 in, no transition effect | — |
| onset of "patients" (w53) | Turn layer 3 visible, already in final position | C02 |
| — | **Hold with no change for ~4.3s** while the whole question is spoken (w53–w69). This long static hold is intentional. | none |
| onset of "not" (w70) | Turn layer 4 visible and run its wipe mask 0% → 100% left to right over ~1.0s | G03 |
| onset of "That's" (w77) | **Hide the entire diagram group (layer 2) and layer 4 in the same frame.** No fade, no shrink. The upper-centre goes to bare off-white. | diagram group, G03 |
| — | Hold the emptied frame for ~1.0s through "a wrong question." | none |
| after "question." (w80) | **Hard cut** to SH04 | all |

**End state:** F03.3 — two figures facing each other across an empty field.

---

## SH04 — Coffee to two people

**Source plate:** IMG04 (mug top-centre, two identical figures on a baseline),
full frame, static.

**Track stack (bottom to top):**
1. IMG04 base plate
2. G07a — left connector arrow (transparent PNG) + a wipe mask following the
   arrow's curve from the mug end to the arrowhead
3. G08a — single red response arc (transparent PNG)
4. G07b — right connector arrow (transparent PNG) + its own path wipe mask
5. G08b — three stacked red response arcs, as one grouped PNG

**Initial composition (F04.0):** layers 2–5 hidden. One mug, two identical
figures, empty band between them.

**Operations in order:**
| At | Operation | Layers touched |
|---|---|---|
| **Hard cut in** on "The" (w81) | SH03 out, SH04 in, no transition effect | — |
| onset of "respond" (w89) | Turn layer 2 visible and run its path wipe 0% → 100% over ~0.4s | G07a |
| onset of "caffeine" (w91) | Turn layer 3 visible | G08a |
| onset of "judge" (w100) | Turn layer 4 visible and run its path wipe 0% → 100% over ~0.4s | G07b |
| immediately as that wipe completes, landing on "“good”" (w104) | Turn layer 5 visible — **one grouped layer, all three arcs in the same frame** | G08b |
| after "“bad.”" (w106) | **Hard cut** to SH05 | all |

**End state:** F04.3 — one mug, two arrows, two identical figures, one arc on
the left figure and three on the right.

---

## SH05 — Three factors, then the CTA

**Source plate:** IMG05 (three blank plates + connector + Dr. Rehan), full
frame, static.

**Track stack (bottom to top):**
1. IMG05 base plate
2. **List group** — a single compound/grouped clip containing the three plate
   outlines and the connector line, if they are not baked into the plate. If
   they *are* baked into IMG05 (as specified in `BASE_IMAGES.csv`), then
   prepare a second plate, **IMG05b**, identical to IMG05 but with the plate
   column and connector erased, and cut to it at A17.
3. G10 + T03 — gauge icon and `BLOOD PRESSURE` text, grouped
4. G11 + T04 — heart icon and `HEART RESPONSE` text, grouped
5. G12 + T05 — three-cup icon and `QUANTITY` text, grouped
6. G13 — video card with play mark (transparent PNG)
7. T06 — text layer `WATCH THE FULL VIDEO`

**Initial composition (F05.0):** layers 3–7 hidden. Three empty plates on the
left, doctor on the right.

**Operations in order:**
| At | Operation | Layers touched |
|---|---|---|
| **Hard cut in** on "Dr." (w107) | SH04 out, SH05 in, no transition effect | — |
| onset of "blood" (w111) | Turn layer 3 visible — icon and text in the same frame | G10, T03 |
| onset of "heart" (w113) | Turn layer 4 visible — icon and text in the same frame | G11, T04 |
| onset of "quantity" (w116) | Turn layer 5 visible — icon and text in the same frame | G12, T05 |
| onset of "full" (w124) | **In one frame:** hide layers 2, 3, 4 and 5 (or cut the base to IMG05b) and turn layers 6 and 7 visible. One instantaneous swap. | list group, G10–G12, T03–T05, G13, T06 |
| — | Hold F05.4 through "Watch it on the channel." (~1.8s) | none |
| end of "channel." (w130) | End of video. No exit transition — the final shot has none. | — |

**End state:** F05.4 — Dr. Rehan on the right, video card with a play mark and
`WATCH THE FULL VIDEO` on the left.

---

## Audio layer

One clip, the full narration, unmodified, running under all five shots.
No music bed, no sound effects, no ducking, no noise reduction, no gap
trimming. Any pause or breath in the delivery is preserved and the visual
state simply holds through it.
(`CAPCUT_PRODUCTION_SYSTEM.md` §4; `PACING_DNA.md`: the corpus's 15 measured
non-speech regions are preserved, not deleted.)

## Build order

1. Record narration → import → place on the audio track first.
2. Mark the onset frame of each of these 17 anchor words on the timeline:
   good, bad, Rehan, wrong, People, energy, stronger, dangerous, So, patients,
   not, That's, The, respond, caffeine, judge, Dr., blood, heart, quantity,
   full.
3. Lay the five base plates as hard-cut clips at the five shot boundaries.
4. Add overlay layers per shot, all hidden.
5. Set each layer's visibility at its marked frame.
6. Add the four wipe masks (A04, A09, A11, A13).
7. Add the six text layers.
8. Watch once at phone size with sound; confirm every reveal lands on its word
   and nothing moves that should be static.
