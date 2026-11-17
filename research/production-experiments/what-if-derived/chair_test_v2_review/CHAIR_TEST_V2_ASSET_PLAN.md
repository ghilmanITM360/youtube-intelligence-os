# Chair-test V2 asset plan — generation and approval pack

**STOP BEFORE CAPCUT.** The user generates/approves these images. Nothing here approves timeline editing. After the exact message **“V2 assets imported”**, create **Timeline 03 — V2** and build from zero; preserve Timeline 02 and 0921.mp4 as the rejected comparison.

## Deliverable count and filenames

**13 PNG files: 11 opaque full-frame scene states + 2 transparent object layers.** No I2V clips. Additional poses are required; the old seated/standing pair is insufficient.

Generate the seated master first, then derive the other five test states from that approved image. Generate the concern scene before its stop variant, and the closed foldout before its open variant. All prompts below are complete when used with their specified approved V2 input; no old PNG is an acceptable identity reference.


| ID | Exact filename | Background | Generation order / relationship |
|---|---|---|---|
| A01 | `V2_TEST_SEATED.png` | OPAQUE WHITE | REGENERATE: replaces CHAIR_01 and PERSON_SEATED_01 as a combined scene |
| A02 | `V2_TEST_LEAN.png` | OPAQUE WHITE | NEW registered pose |
| A03 | `V2_TEST_STANDING.png` | OPAQUE WHITE | REGENERATE: replaces PERSON_STANDING_01 |
| A04 | `V2_TEST_PAUSE.png` | OPAQUE WHITE | NEW; replaces the UNSTEADY_ARCS concept for dizziness |
| A05 | `V2_TEST_UNSTEADY.png` | OPAQUE WHITE | NEW; additional animation state required |
| A06 | `V2_TEST_STOP.png` | OPAQUE WHITE | NEW; replaces WARNING_TRIANGLE idea |
| A07 | `V2_COUNT_SLIP.png` | TRANSPARENT RGBA | NEW; replaces SCORE_CARD_EMPTY_01 |
| A08 | `V2_COMPARISON_SCENE.png` | OPAQUE WHITE | NEW |
| A09 | `V2_STAMP.png` | TRANSPARENT RGBA | NEW |
| A10 | `V2_INFERENCE_CONCERN.png` | OPAQUE WHITE | NEW |
| A11 | `V2_INFERENCE_STOP.png` | OPAQUE WHITE | NEW registered reaction state |
| A12 | `V2_FOLDOUT_CLOSED.png` | OPAQUE WHITE | NEW closing master |
| A13 | `V2_FOLDOUT_OPEN.png` | OPAQUE WHITE | NEW; required additional page state |

## Existing assets: final disposition

KEEP: none. REGENERATE: `CHAIR_01.png`, `PERSON_SEATED_01.png`, `PERSON_STANDING_01.png`. Both old people are **REJECTED_FOR_FINAL**. DELETE FROM V2 / replace visual idea: `BG_01_offwhite.png`, `STOPWATCH_OUTLINE_01.png`, `WARNING_TRIANGLE_01.png`, `UNSTEADY_ARCS_01.png`, `SCORE_CARD_EMPTY_01.png`, `DIAGNOSIS_CARD_EMPTY_01.png`. Preserve the original files and Timeline 02. Regeneration of the chair/person is combined into scene states; do not generate a new disconnected chair icon.

## Production choices versus observed rules

All filenames, 2160×3840 dimensions, exact layout guides, white canvas, clinical poses, stamp and foldout are **NEW CREATIVE DECISIONS**. The reference-backed properties are named separately in every prompt. Mild line irregularity is intentional; random scratchiness, thin unreadable lines and uniformly polished vector geometry are not. No measured universal stroke width, palette or typeface is claimed.

Opaque registered plates intentionally reduce mismatched chair/figure contact. The two transparent layers need real alpha outside the drawing and opaque white within paper/stamp bodies. White interiors are necessary occlusion, not a transparency defect.

## Complete image prompts

### A01 — `V2_TEST_SEATED.png`

- **ASSET ID / EXACT FILENAME:** A01 / `V2_TEST_SEATED.png`.
- **USED AT AUDIO WORD / TIMECODE:** V01 0.000; V06 6.140; V14 13.567 — Before / start / sit down.
- **VISUAL PURPOSE:** Character, chair and stable contact master; starts and completes the demonstrated movement.
- **REFERENCE VIDEO(S) / FRAME:** R02-01 2.016 s and R02-05 56.443 s (typing); R09-01 0.949 s (questions). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** REGENERATE: replaces CHAIR_01 and PERSON_SEATED_01 as a combined scene.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame master; reusable static state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Draw one blank-headed line person sitting on an ordinary straight-backed armless four-legged chair, side view facing right. Make the chair as a physical object with a visible seat thickness, back and grounded leg supports, not a pictogram. Thighs meet the seat; knees bend; feet touch the floor in front. Both arms are drawn folded loosely across the chest, clear of chair support; retain that gesture in the prepared and standing variants. Do not illustrate any helper. The actor and chair should form one dominant readable scene, with a little ground line connecting them. Reference borrowing: R02 at 2.016 and 56.443 s supplies the blank head, angular seated line limbs and purposefully detailed furniture; R09 at 0.949 s supplies the coherent chair/desk-object vocabulary, not its composition. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Approve this first. All five test variants below must be edits of this master. Preserve exact canvas, chair, floor, head diameter and line character. Do not regenerate the background each time.

**CAPCUT MOTION:** Hold as a scene plate. Replace with other registered test states. Never move the chair independently.

**WHY THIS MATCHES THE REFERENCE CORPUS:** The person is less detailed than the chair, as in the seated reference examples; body pose and contact carry meaning. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A02 — `V2_TEST_LEAN.png`

- **ASSET ID / EXACT FILENAME:** A02 / `V2_TEST_LEAN.png`.
- **USED AT AUDIO WORD / TIMECODE:** V03 1.520; V10 10.580; V13 13.040 — chair test / times / and then.
- **VISUAL PURPOSE:** Preparation and short return transition, making pose change intentional rather than anatomical teleportation.
- **REFERENCE VIDEO(S) / FRAME:** R02-05 56.443 s (head/torso lean); R09 raw 3–7 s (changed pose with fixed furniture). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW registered pose.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derived state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_TEST_SEATED.png. Change only the participant into a slight forward preparation lean: head and torso incline forward over the grounded feet, hips still close to the seat, arms remain folded across the chest. Do not depict a full standing position or falling. Keep the entire chair and floor pixels unchanged. Preserve head size and single-stroke body construction. Reference borrowing: the leaning seated actor at R02 56.443 s and the pose substitutions with fixed furniture in R09 3–7 s. Borrow their structural economy, not their specific gestures or scene. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Use A01 as direct reference. Two to four frames can bridge the later movement; opening uses a longer anticipatory hold. This is a separate drawing, not a scaled seated sprite.

**CAPCUT MOTION:** Hard pose replacement. Use brief hold for preparation/return; no anatomy tween.

**WHY THIS MATCHES THE REFERENCE CORPUS:** A small authored state precedes the meaningful larger state, while object anchors survive. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A03 — `V2_TEST_STANDING.png`

- **ASSET ID / EXACT FILENAME:** A03 / `V2_TEST_STANDING.png`.
- **USED AT AUDIO WORD / TIMECODE:** V11 11.367–V12 13.040 — stand up / unassisted.
- **VISUAL PURPOSE:** Show the completed upright posture on the floor in front of the chair.
- **REFERENCE VIDEO(S) / FRAME:** R13-01 1.762 s (standing figure construction); R10-02 44.188 s (grounded line figure). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** REGENERATE: replaces PERSON_STANDING_01.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derived state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_TEST_SEATED.png into the standing state. Keep chair and floor exactly unchanged. The same unfilled round-headed line person now stands upright on the FLOOR immediately in front of the seat, facing right, arms still folded across the chest. Feet remain within the footprint established in the seated master; do not put feet on the seat. Preserve head diameter, limb stroke, body proportions and blank face. Chair is visible behind the legs, with sensible occlusion. Reference borrowing: R13 at 1.762 s shows single-stroke standing anatomy; R10 at 44.188 s shows how a tiny ground object anchors a plain line figure. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Match A01 identity and scale. The standing figure must not be a newly designed taller/thinner person. Keep enough separation to read chair behind the figure.

**CAPCUT MOTION:** Hard replace after A02, hold through unassisted, return through A02/A01. Add one tally only after the demonstrated return.

**WHY THIS MATCHES THE REFERENCE CORPUS:** Standing reads through line geometry and relative position, not filled clothing silhouette. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A04 — `V2_TEST_PAUSE.png`

- **ASSET ID / EXACT FILENAME:** A04 / `V2_TEST_PAUSE.png`.
- **USED AT AUDIO WORD / TIMECODE:** V17 16.200–V18 about 18.000 — unsafe / dizziness.
- **VISUAL PURPOSE:** Show discomfort changes behavior while participant remains safely seated.
- **REFERENCE VIDEO(S) / FRAME:** R02-05 56.443 s (hand/head relation); R09-02 6.644 s (behavioral reaction). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW; replaces the UNSTEADY_ARCS concept for dizziness.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derived state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_TEST_SEATED.png. Keep person seated with hips on the same chair, both feet on the same floor, chair unchanged. Change only torso, head and arms: slight forward pause, head inclined, one simple line hand resting against the forehead, other arm relaxed toward the lap. Face stays entirely blank. The pose should read as a person pausing because they do not feel right, not fainting or performing another repetition. No motion arcs, stars, swirls or sweat symbols. Reference borrowing: R02 56.443 s communicates a mental/physical response through head-to-hand relation; R09 6.644 s lets a reaction change the action. These are pose principles, not evidence of a medical symptom in those videos. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Keep head and chair geometry from A01; do not introduce detailed hands, facial expression or different anatomy for symptoms.

**CAPCUT MOTION:** Instant state replacement after timer freezes; held without sway or looping effects.

**WHY THIS MATCHES THE REFERENCE CORPUS:** The body itself changes meaning. Symptom is not a decorative layer beside an unchanged person. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A05 — `V2_TEST_UNSTEADY.png`

- **ASSET ID / EXACT FILENAME:** A05 / `V2_TEST_UNSTEADY.png`.
- **USED AT AUDIO WORD / TIMECODE:** V19 about 18.000–19.067 — ataxia phrase; onset to verify.
- **VISUAL PURPOSE:** A second restrained warning state for generic lack of steadiness; no diagnostic demonstration.
- **REFERENCE VIDEO(S) / FRAME:** R13-04 36.995 s (changed reaction pose); R09-02 6.644 s (state-based consequence). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW; additional animation state required.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derived state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_TEST_SEATED.png. The same line person remains fully seated, hips visibly supported and both feet grounded. Show a small asymmetry in shoulders and torso, head slightly inclined, one angular line arm extended a little to the side as if seeking steadiness, the other resting near the lap. Keep the center of the person over the seat. Do not draw walking, standing, falling, reaching for a moving chair or dramatic distress. No motion marks or effect overlays. Reference borrowing: R13 36.995 s communicates concern through an economical changed body pose while the setting persists; R09 6.644 s shows reaction as a new state. This is an original nonspecific seated warning pose, not a copied clinical illustration. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Same A01 proportions, chair, feet and ink. Only body posture changes. This must stay visually distinct from A04 without escalating into a collapse.

**CAPCUT MOTION:** One held state within the warning phrase; no alternating wobble cycle. Replace with decisive A06 on don’t.

**WHY THIS MATCHES THE REFERENCE CORPUS:** Adds a purposeful visual state without treating generic arcs as explanatory anatomy. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A06 — `V2_TEST_STOP.png`

- **ASSET ID / EXACT FILENAME:** A06 / `V2_TEST_STOP.png`.
- **USED AT AUDIO WORD / TIMECODE:** V04 3.700; V16 14.880; V20 19.067 — safety rule / However / don’t.
- **VISUAL PURPOSE:** Safety overrides procedure in the same physical scene.
- **REFERENCE VIDEO(S) / FRAME:** R04-02 15.283 s (changed presenter gesture); R13-04 36.995 s (hands/pose as reaction). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW; replaces WARNING_TRIANGLE idea.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derived state.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_TEST_SEATED.png. Same person remains seated upright, feet grounded, one arm lifted with a small open stop palm facing outward; suggest the hand using only a few short strokes, not a detailed anatomical hand. The other arm rests loosely near the body. Head stays blank. Keep chair, floor and body proportions identical. The gesture is calm and decisive: this attempt will not proceed. No warning triangle, no badge, no words, no new props. Reference borrowing: R04 15.283 s changes a simple presenter’s whole gesture to mark reversal; R13 36.995 s uses angular arms around a blank head for a meaningful reaction. NEW CREATIVE DECISION: test plates share the same 2160×3840 canvas. Draw chair and principal participant as one registered scene. Chair occupies approximately x28–50%, y45–78%; back on left, seat around y61%; a short floor line at y78%. Principal participant faces right. The unfilled head is approximately 18% of canvas width in diameter, with proportions approved from the master rather than independently regenerated. Seated head is around x49%, y44%; standing head around x55%, y30%. These are starting layout guides, not measured corpus coordinates. Leave upper/right room for a small native time bracket and a physical count slip. Do not reserve a permanent bottom subtitle band. Feet remain on the same floor; seat and chair remain pixel-registered in every derived state.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Use same state in opening and final safety beat to make the rule recognizable. Do not replace the chair with a symbol.

**CAPCUT MOTION:** Hard replacement; freeze native time indicator and cancel only its bracket. Hold person/scene still.

**WHY THIS MATCHES THE REFERENCE CORPUS:** The warning changes action rather than floating as an icon. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A07 — `V2_COUNT_SLIP.png`

- **ASSET ID / EXACT FILENAME:** A07 / `V2_COUNT_SLIP.png`.
- **USED AT AUDIO WORD / TIMECODE:** V09 9.540; V15 13.800; V21 20.767 — count / completed action / your number.
- **VISUAL PURPOSE:** Turn count into a physical record that can be handled and contextualized.
- **REFERENCE VIDEO(S) / FRAME:** R02-05 56.443 s (physical paper/book edges); R09-01 0.949 s (ordinary handheld object in line scene). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW; replaces SCORE_CARD_EMPTY_01.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** TRANSPARENT RGBA separate object layer; white paper interior remains opaque.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Draw one original small physical paper slip, slightly irregular rectangular edges with one tiny folded corner. Black ink contour, white opaque paper interior, no ruled lines, no title, no text or digits. Keep it plainly a sheet of paper, not a rounded UI card, sticky-note tile or badge. Use a near-frontal view with a very slight perspective cue only at the fold. Place paper around x35–65%, y38–58% of the full 2160×3840 canvas with real alpha outside it. Reference borrowing: R02 56.443 s uses specific page contours to make paper/book objects physical; R09 0.949 s keeps held objects in the same line vocabulary as the person. No copied object arrangement.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** The slip shape is repeated inside A08–A13; its white interior can cover artwork behind it. Add all tallies/n only in CapCut. Do not supply a checkerboard painted into the file.

**CAPCUT MOTION:** Reveal by state cut; later enlarge as a physical object. Group native n/tally with it. No floating glow or card shadow.

**WHY THIS MATCHES THE REFERENCE CORPUS:** A count has a physical carrier and continuity across concepts, rather than a heading box. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A08 — `V2_COMPARISON_SCENE.png`

- **ASSET ID / EXACT FILENAME:** A08 / `V2_COMPARISON_SCENE.png`.
- **USED AT AUDIO WORD / TIMECODE:** V22 22.280–24.467 — don’t compare / universal number.
- **VISUAL PURPOSE:** Two substantial people have separate personal records; stamp attempts an invalid common application.
- **REFERENCE VIDEO(S) / FRAME:** R08-04 68.127 s (distinct line figures); R02-08 96.760 s (two actors in shared scene); R10-04 132.562 s (comparison retains context). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame scene; stamp is a separate layer.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Create an original portrait scene with two large line people, not three tiny duplicates. Principal bald blank-headed participant stands lower-left holding their physical blank count slip around chest height. A second blank-headed adult with one small hair contour sits lower-right at a spare straight-edged table, looking toward a separate blank paper on the tabletop. Use different arm poses, but the same head scale and single-stroke anatomy; do not exaggerate ages, heights or body types. Place a small version of the approved chair behind the principal person as a contextual callback, not as another icon. A short floor line joins the physical space. Leave a clear upper-right corridor above the second paper for an oversized stamp to descend later; do not draw the stamp. Figures occupy roughly the middle/lower two-thirds and remain legible at phone size. Reference borrowing: R08 68.127 s distinguishes actors with tiny identity cues while retaining line anatomy; R02 96.760 s puts two distinct actions in one shared scene; R10 132.562 s preserves the owner and conditions of a measurement. All papers blank.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Use A01 for principal head/body construction and A07 for the paper contour. Two records must stay visibly separate. No same-number text generated on either paper.

**CAPCUT MOTION:** Scene cut; native n remains attached to principal slip; separate A09 stamp approaches other record then retracts before contact.

**WHY THIS MATCHES THE REFERENCE CORPUS:** Comparison is a physical attempted action involving real actors, not a grid of identical person symbols. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A09 — `V2_STAMP.png`

- **ASSET ID / EXACT FILENAME:** A09 / `V2_STAMP.png`.
- **USED AT AUDIO WORD / TIMECODE:** V23 23.160–24.467; V26 25.980–29.120; small resting reuse in ending.
- **VISUAL PURPOSE:** One recurring physical metaphor for two invalid shortcuts: universalizing a count and manufacturing a diagnosis.
- **REFERENCE VIDEO(S) / FRAME:** R02-03 28.222 s (physical analogy); R13-03 24.663 s (scale contrast); R03-05 116.760 s (object-based parody). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** TRANSPARENT RGBA separate object layer; solid white interiors.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Draw one oversized old-fashioned rubber hand stamp as an original black-ink physical prop: plain domed handle, short stem and rectangular rubber base, slightly imperfect contour, white interior, a very slight three-quarter view showing a blank front-facing die/face area large enough for editable lettering. Keep geometry clear and a little absurd in scale, with no decorative branding. No words, numbers, existing imprint, hand, person, arrows or paper. Center it around x30–70%, y25–65% on full 2160×3840 transparent RGBA canvas. Real alpha outside the stamp; no checkerboard. Reference borrowing: R02 28.222 s turns a quantity into a concrete physical analogy; R13 24.663 s makes scale mismatch explanatory; R03 116.760 s uses a physical product parody. The stamp itself is a new creative decision, not an object claimed to occur in those frames.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Identical stamp for both failed inferences. Native n then DIAGNOSIS groups with the blank face. Keep proportions and line character consistent with all other objects. No permanently baked rejection stroke.

**CAPCUT MOTION:** Translate as one rigid object for a short descent, stop before paper, then retract. No spin, rubber bounce or impact. Later rotate/place aside as an inactive prop.

**WHY THIS MATCHES THE REFERENCE CORPUS:** An attempted physical transformation can fail visibly; the same object connects both inference errors. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A10 — `V2_INFERENCE_CONCERN.png`

- **ASSET ID / EXACT FILENAME:** A10 / `V2_INFERENCE_CONCERN.png`.
- **USED AT AUDIO WORD / TIMECODE:** V25 24.467–27.560 — score looks low / number alone.
- **VISUAL PURPOSE:** Return concern to the owner of the count and stage the invalid diagnosis shortcut.
- **REFERENCE VIDEO(S) / FRAME:** R02-05 56.443 s (body-directed concern); R09-01/02 0.949/6.644 s (physical desk scene and reaction). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame scene master for A11.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Create original portrait scene using approved V2 principal line person and chair. Person sits lower-left beside a spare table whose blank paper extends into center-right. The same count slip lies on the table, clearly physical and blank. Participant leans the blank head slightly toward the paper, with one hand resting near it and the other near the body. Leave room above the head for a small native question and leave a clear vertical corridor above the paper for the separate stamp. Keep table/chair detail economical but sufficient to show contact. No second card, diagnosis box, arrow or medical icon. Reference borrowing: R02 56.443 s makes concern visible through head and hand relation to a work surface; R09 0.949 and 6.644 s retains a mundane physical setting while interpretation changes. Preserve original V2 line figure construction.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Match A01 figure/chair and A07 paper. Record paper position precisely; A11 must keep it fixed so the count can remain unchanged through the denial.

**CAPCUT MOTION:** Cut to scene; native LOW? with a short speech leader; A09 stamp approaches paper without contact.

**WHY THIS MATCHES THE REFERENCE CORPUS:** The worry belongs to a person within a scene; text is a short question, not a replacement for illustration. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A11 — `V2_INFERENCE_STOP.png`

- **ASSET ID / EXACT FILENAME:** A11 / `V2_INFERENCE_STOP.png`.
- **USED AT AUDIO WORD / TIMECODE:** V28 27.560–29.120 — doesn’t diagnose you.
- **VISUAL PURPOSE:** Block the attempted diagnosis physically while preserving the count.
- **REFERENCE VIDEO(S) / FRAME:** R09-02 6.644 s (behavioral reversal); R04-02 15.283 s (reaction gesture). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW registered reaction state.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derivative of A10.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_INFERENCE_CONCERN.png. Keep table, chair, count paper, background, principal figure’s head size and seated lower body unchanged. Change only upper-body gesture: raise one simple line arm with open palm into the corridor ABOVE the paper, visibly intercepting an approaching oversized object before it can reach the page. The person is calm, not fighting or frightened. Do not draw the stamp; it is a separate layer. Do not cover the paper where editable count will remain visible. Reference borrowing: R09 6.644 s changes behavior as a consequence of an idea; R04 15.283 s makes a reversal legible with a changed angular arm gesture. No copied scene arrangement.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Must be a registered edit of A10, not a new framing. Palm and the planned stamp path must meet convincingly while stamp stays above paper. No extra hands or detailed fingers.

**CAPCUT MOTION:** Hard replace at denial; native stamp stops, die label is crossed out and stamp retracts. Count remains identical.

**WHY THIS MATCHES THE REFERENCE CORPUS:** Negation has a visible consequence; it is no longer a not-equal symbol between two empty boxes. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A12 — `V2_FOLDOUT_CLOSED.png`

- **ASSET ID / EXACT FILENAME:** A12 / `V2_FOLDOUT_CLOSED.png`.
- **USED AT AUDIO WORD / TIMECODE:** V29 29.120–30.760 — Dr. Rehan explains.
- **VISUAL PURPOSE:** Prepare the visual payoff: one result is about to become part of a larger explanation.
- **REFERENCE VIDEO(S) / FRAME:** R02-08 96.760 s (scene-based close); R10-07 265.125 s (person relates to larger explanatory drawing). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW closing master.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame scene.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Create an original portrait closing scene in the same V2 ink vocabulary. Principal blank-headed participant sits lower-left in the approved chair at a simple table. A second generic blank-headed explainer stands lower-right, one arm gesturing toward a physical folded paper on the tabletop. The folded paper has the same small exposed count-slip face as A07, blank for editable n; creases indicate it can unfold upward and sideways. Leave upper-middle space for the opened drawing in the next state. Do not depict Dr. Rehan’s likeness, a medical uniform, stethoscope or authoritative diagnosis. Do not draw the stamp; it will be placed small and inactive at the far lower edge as a separate layer. Reference borrowing: R02 96.760 s closes with actors and physical objects in a coherent environment; R10 265.125 s couples a person to a larger model. Paper, gestures and arrangement must be original.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Principal person stays recognizably A01. Generic explainer uses the same head/line anatomy. A13 keeps these anchors; the sheet grows, not the characters.

**CAPCUT MOTION:** Cut on Dr. Rehan; hold briefly; prepare registered replacement A13.

**WHY THIS MATCHES THE REFERENCE CORPUS:** Closing retains the count’s owner and prepares a new explanatory relation rather than displaying only CTA text. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

### A13 — `V2_FOLDOUT_OPEN.png`

- **ASSET ID / EXACT FILENAME:** A13 / `V2_FOLDOUT_OPEN.png`.
- **USED AT AUDIO WORD / TIMECODE:** V30 30.760–end — interpret it properly / full video.
- **VISUAL PURPOSE:** Visual payoff: count becomes one small part of an expanded explanation.
- **REFERENCE VIDEO(S) / FRAME:** R02 raw 23/25/27 s (add a concrete comparison); R15-08 80.000 s (human vignette within larger explanation); R10-07 265.125 s (board relationship). Source filenames and images: [reference-frame study](REFERENCE_FRAME_STUDY.md).
- **KEEP / REGENERATE / NEW:** NEW; required additional page state.
- **STATIC / LAYER / MULTI-STATE; TRANSPARENT / OPAQUE:** OPAQUE full-frame derivative of A12.

**PROMPT — copy in full:**

> Create an original 2160×3840 portrait 9:16 explanatory ink drawing. Borrow only high-level visual properties from the cited reference frames: unfilled round or slightly oval human heads, single-stroke torso and limbs, angular elbows and knees, mild contour irregularity, white object interiors, detail only where it identifies a physical object or relation. Do not copy any reference composition or character pose exactly. No eyes, nose, mouth, skin fill, shirt, trousers, detailed shoes or filled human silhouette. Black drawing, flat white scene, no paper texture. Keep objects readable at phone size. Use the approved V2 master to maintain drawing consistency, not the old blue-shirt PNGs. No generated words, letters, numerals or symbols; these will be added in CapCut. Edit approved V2_FOLDOUT_CLOSED.png. Keep both people, table, chair, ground, framing and drawing treatment registered. Unfold the physical sheet upward and toward the center into a broad creased paper drawing, occupying the upper-middle portion. Preserve the small count-slip face at the lower-left of this paper so editable n can remain in that corner. On the newly opened paper draw one clear miniature scene of the same chair-test participant and chair, grounded and proportionate, plus a spare open area for future explanation; do not fill it with unrelated icons, charts, diagnostic ranges or fake handwriting. The generic explainer’s line hand points into the larger drawn scene while the principal person looks toward it. The expanded sheet remains visibly folded paper, with irregular edges and crease lines, not a rounded panel. Reference borrowing: R02 23/25/27 s adds physical context to a quantity; R15 80.000 s makes a human vignette part of a larger explanation; R10 265.125 s links figure and drawn model. This unfold metaphor is original. All lettering absent.

**NEGATIVE PROMPT:**

> Corporate explainer clipart; colored shirt; skin tones; outlined fleshy arms or legs; realistic anatomy; emoji; stock icon set; rounded app cards; dashboard; warning triangle; floating stopwatch; unrelated arrows; decorative swooshes; blurred movement; duplicate limbs; ghost poses; collapse; injured person; diagnosis marks; medical cutoff; photorealism; 3D bevels; gradients; cast shadows; paper grain; watermark; logo; baked captions; letters or numbers.

**CONSISTENCY REQUIREMENTS:** Match A12. Preserve count patch position as closely as possible; if paper geometry shifts it, native n must be grouped to follow that exact patch. Final drawing remains visible to the last frame.

**CAPCUT MOTION:** Hard replacement or short hard-mask reveal across the paper only; no generated folding morph. Add small native Full video on channel cue at 31.680 in available space.

**WHY THIS MATCHES THE REFERENCE CORPUS:** The result does not transform into diagnosis; it gains an explanatory setting. Ending visually resolves the core mistaken inference. This borrows the cited examples at a high level; the exact scene is a new creative decision and must be visually approved.

## Native elements — do not generate extra PNGs

| Native ID | Used at words / time | Purpose and construction | Reference grounding |
|---|---|---|---|
| N01 | `30-second` 0.880; `counter` 7.300; `30 seconds` 8.060 | Short black time bracket, endpoint ticks, editable `30 s`, small sweep marker. Make as native lines/text/mask. No stopwatch shell. | R05 18.468 ruler and R03 87.570 time scale; exact V2 bracket is new. |
| N02 | completed demonstration 13.800 | One tally on A07, no second increment for sitting. Hold/freeze at interruption. | R02 action marks and R10 numeric revisions; counting convention here is only an illustrative single demonstration. |
| N03 | `your number` 20.767 onward | Symbolic `n` on physical paper; small first-use `your count` annotation. No invented personal value or threshold. Group to object. | R02 quantity given physical meaning; symbolic n is new. |
| N04 | `unsafe` / `don’t` 14.880–20.767 | Freeze time indicator, optional small red diagonal across time bracket. Never across the person. | R10 41–45 revises/cancels the relevant claim locally. |
| N05 | `universal number` 23.160 | Native n on A09 stamp face, follows stamp. Red rejection stroke after short approach. No actual imprints on other record. | Physical analogy + local rejection; stamp-specific execution is new. |
| N06 | `score looks low` 24.467 | Small `LOW?` with short speech leader connected to principal person; no scale or cutoff. | Selective reaction text in R09 19.932/45.560. |
| N07 | `number alone` / `doesn’t diagnose` 25.980–29.120 | Native `DIAGNOSIS` on stamp face; strike that proposed inference and retract stamp. n remains unchanged. | R09 behavioral reversal, R10 local correction; medical label is supplied script concept. |
| N08 | `full video` 31.680 | One small `Full video on channel` cue beside/under open paper. No card, logo, giant type or separate CTA scene. | Scene-based closes in R02 96.760 and R15 80.000; CTA wording is supplied purpose. |
| N09 | isolated paper state 20.767–22.280 | Native solid white canvas. Exact match to approved opaque plates. | Light-field subset; not claimed universal. |
| N10 | optional accessibility delivery | Separate SRT/closed captions based on unchanged narration. Not burned by default; do not copy the old caption timing blindly. | Absence of persistent transcript bands in sampled portrait frames; accessibility delivery is a new choice. |

## Motion instructions for the later editor

- **Test:** A01 / A02 / A03 / A02 / A01 are separate registered drawings, not morph endpoints for image-to-video. Keep chair, floor and all native marks fixed. Native count changes once for the one demonstration. The clock is an explanatory 30-second window, not a claim that the short excerpt contains a full real-time test.
- **Warning:** freeze procedure first; A04/A05 are held illustrations of a nonspecific reason to stop. A06 concludes. Never alternate A04/A05 as a wobble loop. No extra repetition follows warning.
- **Universal inference:** A08 stays fixed; A09 with native n approaches other record over a short, readable interval, stops before contact and retracts. Preserve original record ownership. A handwritten rejection stroke identifies the stamp action, not a judgment against the second participant.
- **Diagnosis inference:** A10 stages the paper, A09 descends; A11 intercepts. Reuse the same rigid stamp geometry. Cross the claim on its face, not the count. No magical transformation or diagnosis result is drawn.
- **Ending:** A12/A13 create a two-state unfolding. A short hard-mask reveal can bridge them if their geometry permits. If a fold transition cannot read cleanly, use the direct state replacement; do not order a new generative video. Reposition native n only with its paper patch. Keep final image throughout the audio tail.

## Additional states and generation order

1. Approve A01 against the actual seated reference frames. Then generate A02–A06 as registered edits.
2. Generate A07 and A09 as real transparent objects.
3. Generate A08 using A01/A07 as consistency references.
4. Generate A10, then A11 as a registered edit.
5. Generate A12, then A13 as a registered edit.

Required extra states are **lean, pause, unsteady, stop, inference concern/stop, foldout closed/open**. No frame sequence beyond these 13 PNGs is requested. A character sheet can be useful to your generation process, but it is not an additional required import file.

## Approval checks before import

- Compare generated person against R02 2.016/56.443, R09 0.949/6.644 and R13 1.762: head blank/unfilled, body single-stroke, no colored clothes or fleshy silhouette.
- Flip A01–A06 over each other. Chair/ground/head scale must not jump. Every seated pose must contact the chair. Standing feet must remain on floor.
- At phone thumbnail size, each pose must differ through body geometry. Reject any set that needs captions to distinguish readiness, discomfort and stop.
- A08 must read as two distinct actors with separate records, not duplicate symbols or a demographic claim.
- A10/A11 must allow stamp/palm/paper to interact without overlap errors. A13 must show more explanatory context, not a blank giant card.
- All exact words/numerals remain absent from PNGs. Alpha must be genuine on A07/A09; no matte/checkerboard rectangle.

When approved assets are generated/imported, send **“V2 assets imported.”** Only then begin **Timeline 03 — V2**, keep Timeline 02 intact, and compare the new export against 0921.mp4 and these raw reference frames. Do not treat this plan as permission to rebuild now.
