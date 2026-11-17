# Revised Storyboard — Revision 1

20 visual states across 5 shots. Generated from `REVISED_VISUAL_STATES.csv`,
`REVISED_MOTIONS.csv` and `REVISED_SHOT_PLAN.csv` — readable without opening a CSV.

No absolute timestamps appear anywhere. Every trigger is a word onset in the
narration. All durations are marked ESTIMATED and derive from 3.93 words/sec,
the measured portrait-subcorpus rate.

First-pass state IDs are shown beside each revised ID so the two passes can be
compared line by line.

---

## SH01 — IMG01 — 5 states, 4 motions

**Narration:** Is coffee good for your heart-or bad for it? Dr. Rehan says that's actually the wrong question.

**Words:** w1-w17 (17 words) · **Est. duration:** 4.33 ESTIMATEDs
**Transition in:** START · **Transition out:** Red strike completes across the fork (4 frames)

**Purpose:** Install the good/bad binary model and have the named doctor strike it out

**Revision change:** No states or motions changed. M04 strike duration shortened from a spoken phrase to 4 frames.


### R01.0  ·  was F01.0

| | |
|---|---|
| **Script** | "Is coffee" |
| **Trigger** | START of narration ("Is", w1) |
| **What the viewer sees** | Off-white portrait field, 9:16. A flat black line-drawn coffee mug with a side handle on the right sits centred at x36-64%, y18-30%; the liquid inside the rim is a flat coffee-brown band across x39-61%, y19-22%. Directly below it, a single-stroke black outline heart, x42-58%, y34-43%. Everything below y44% is empty off-white field. No text, no arrows, no other objects. |
| **What changed** | (nothing - opening state) |
| **What stays static** | Off-white field; coffee mug; heart; camera |
| **Why** | Put the two subjects of the question on screen before the question is finished being asked |
| **How it arrives** | Hard cut in (no motion) |
| **Hold** | ~0.5s ESTIMATED (2 words) |
| **Next change** | R01.1 on "ON_WORD_START ("good", w3)" |
| **Assets** | E01,O01,G01 |
| **Revision change** | UNCHANGED |


### R01.1  ·  was F01.1

| | |
|---|---|
| **Script** | "good for your heart-or" |
| **Trigger** | ON_WORD_START ("good", w3) |
| **What the viewer sees** | Same off-white field, mug at x36-64% y18-30% and heart at x42-58% y34-43% unchanged. Two straight thin black lines now descend from the bottom point of the heart at x50%,y44%, one to x18%,y56% and one to x82%,y56%, forming a wide inverted V. A blank rounded-rectangle label plate, thin black outline, sits at x10-40%, y56-66% at the end of the left line. Editor text GOOD? is centred inside that left plate. The right line ends in empty field - no plate there yet. |
| **What changed** | Fork lines; left label plate; GOOD? text |
| **What stays static** | Off-white field; mug; heart; camera |
| **Why** | Draw the first half of the binary model on the word that names it |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.0s ESTIMATED (4 words) |
| **Next change** | R01.2 on "ON_WORD_START ("bad", w7)" |
| **Assets** | E01,O01,G01,G02,T01 |
| **Revision change** | UNCHANGED |


### R01.2  ·  was F01.2

| | |
|---|---|
| **Script** | "bad for it? Dr." |
| **Trigger** | ON_WORD_START ("bad", w7) |
| **What the viewer sees** | Same field, mug, heart and both fork lines. A second blank rounded-rectangle label plate, identical in size and stroke to the left one, now sits at x60-90%, y56-66% at the end of the right line. Editor text BAD? is centred inside it. The model is now symmetrical: one mug, one heart, two branches, two labels. Lower field below y68% still empty. |
| **What changed** | Right label plate; BAD? text |
| **What stays static** | Off-white field; mug; heart; fork lines; left plate and GOOD? text; camera |
| **Why** | Complete the binary so the viewer owns the model that is about to be rejected |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.0s ESTIMATED (4 words) |
| **Next change** | R01.3 on "ON_WORD_START ("Rehan", w11)" |
| **Assets** | E01,O01,G01,G02,T01,T02 |
| **Revision change** | KEPT AGAINST the first pass's own cut suggestion - merging would fire a named concept off its word onset |


### R01.3  ·  was F01.3

| | |
|---|---|
| **Script** | "Rehan says that's actually the" |
| **Trigger** | ON_WORD_START ("Rehan", w11) |
| **What the viewer sees** | Same field and complete binary model. A stick figure now stands in the previously empty lower-left field at x8-30%, y70-95%: round head with two small rectangular glasses lenses joined by a bridge, a short filled black beard arc under the chin, a short side-swept hair stroke on top, plain single-stroke body, and the near arm raised at roughly 45 degrees toward the fork above. Faces frame-right. Lower-right field remains empty. |
| **What changed** | Dr. Rehan figure |
| **What stays static** | Off-white field; mug; heart; fork; both plates and their text; camera |
| **Why** | Put the named speaker in frame on his name, so the rejection that follows has an author |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.3s ESTIMATED (5 words) |
| **Next change** | R01.4 on "ON_WORD_START ("wrong", w16)" |
| **Assets** | E01,O01,G01,G02,C01,T01,T02 |
| **Revision change** | UNCHANGED |


### R01.4  ·  was F01.4

| | |
|---|---|
| **Script** | "wrong question." |
| **Trigger** | ON_WORD_START ("wrong", w16) |
| **What the viewer sees** | Same field, model and doctor figure. One thick muted-red hand-drawn stroke, slightly uneven, now crosses the entire fork diagonally from x14%,y68% up to x86%,y52%, cutting through both branch lines and clipping the top edge of both label plates. The plates and their text remain legible under the stroke. Nothing else changes. |
| **What changed** | Muted-red strike stroke |
| **What stays static** | Off-white field; mug; heart; fork; both plates and text; Dr. Rehan; camera |
| **Why** | Reject the model on the word that rejects it, and teach the viewer that a red strike means wrong |
| **How it arrives** | Draw on progressively — 4 frames (0.167s ESTIMATED) |
| **Hold** | ~0.5s ESTIMATED (2 words), held to the cut |
| **Next change** | HARD CUT to the next shot |
| **Assets** | E01,O01,G01,G02,C01,G03,T01,T02 |
| **Revision change** | FRAME UNCHANGED; the strike now draws in 4 frames instead of across a spoken phrase (see M04) |


## SH02 — IMG02 — 4 states, 3 motions

**Narration:** People usually ask me, then what about the energy drinks? So, energy drinks for me are much stronger than coffee and they are a bit more dangerous than coffee as well.

**Words:** w18-w48 (31 words) · **Est. duration:** 7.89 ESTIMATEDs
**Transition in:** HARD CUT · **Transition out:** Caution mark appears above the can

**Purpose:** Compare coffee and an unbranded energy drink as two physical objects on one baseline - strength first, then caution

**Revision change:** Unchanged. The caution triangle was the strongest merge candidate and survives on newly located corpus precedent.


### R02.0  ·  was F02.0

| | |
|---|---|
| **Script** | "People usually ask me, then what about the" |
| **Trigger** | HARD CUT on "People" (w18) |
| **What the viewer sees** | Off-white portrait field. A thin horizontal black baseline runs across x8-92% at y70%. A flat black line-drawn coffee mug with a side handle stands on it at x14-40%, y52-70%, coffee-brown liquid band across x17-34%, y53-56%. Two short black radiating strokes sit above the mug at x20-34%, y42-50%. The right half of the baseline is bare and the whole field above y42% is empty. No text. |
| **What changed** | (nothing - opening state of the shot) |
| **What stays static** | Off-white field; baseline; coffee mug; the mug's two stimulation strokes; camera |
| **Why** | Establish coffee alone, with its stimulation reading already visible as the unit of measure the can will be compared against |
| **How it arrives** | Hard cut in (no motion) |
| **Hold** | ~2.0s ESTIMATED (8 words) |
| **Next change** | R02.1 on "ON_WORD_START ("energy", w26)" |
| **Assets** | E01,O01,G04 |
| **Revision change** | UNCHANGED |


### R02.1  ·  was F02.1

| | |
|---|---|
| **Script** | "energy drinks? So, energy drinks for me are much" |
| **Trigger** | ON_WORD_START ("energy", w26) |
| **What the viewer sees** | Same field, baseline, mug and its two strokes. A tall plain cylindrical can now stands on the same baseline at x60-86%, y44-70%: flat black outline, rounded top rim with a small pull-tab ellipse, one plain horizontal band across its middle, and completely blank sides - no logo, no brand, no lettering, no colour fill. It is visibly taller than the mug. The field above y42% remains empty. |
| **What changed** | Energy-drink can |
| **What stays static** | Off-white field; baseline; mug; mug strokes; camera |
| **Why** | Introduce the second container as a physical object, unbranded, on the word that names it |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~2.3s ESTIMATED (9 words) |
| **Next change** | R02.2 on "ON_WORD_START ("stronger", w35)" |
| **Assets** | E01,O01,G04,O02 |
| **Revision change** | UNCHANGED |


### R02.2  ·  was F02.2

| | |
|---|---|
| **Script** | "stronger than coffee and they are a bit more" |
| **Trigger** | ON_WORD_START ("stronger", w35) |
| **What the viewer sees** | Same field, baseline, mug, mug strokes and can. Four black radiating strokes, in the same hand-drawn style as the mug's two, now sit above the can at x62-84%, y28-42%. They are the same stroke length as the mug's but there are four of them and the group sits higher in frame, so the two groups read as the same unit counted twice over. Nothing else changes. |
| **What changed** | The can's four stimulation strokes |
| **What stays static** | Off-white field; baseline; mug; mug strokes; can; camera |
| **Why** | State the comparison as a countable difference rather than a label |
| **How it arrives** | Pop on together in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~2.3s ESTIMATED (9 words) |
| **Next change** | R02.3 on "ON_WORD_START ("dangerous", w44)" |
| **Assets** | E01,O01,G04,O02 |
| **Revision change** | UNCHANGED |


### R02.3  ·  was F02.3

| | |
|---|---|
| **Script** | "dangerous than coffee as well." |
| **Trigger** | ON_WORD_START ("dangerous", w44) |
| **What the viewer sees** | Same field with both containers and both stroke groups. A single muted-red outlined triangle with a short vertical exclamation stroke and dot inside now sits above the can's strokes at x66-80%, y14-25%. It sits over the can only; the space above the mug stays empty. No other marks, no colour wash, no background change. |
| **What changed** | Muted-red caution triangle |
| **What stays static** | Off-white field; baseline; mug; mug strokes; can; can strokes; camera |
| **Why** | Carry the narration's caution without overstating it - one restrained mark over one object |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.3s ESTIMATED (5 words), held to the cut |
| **Next change** | HARD CUT to the next shot |
| **Assets** | E01,O01,G04,O02,G05 |
| **Revision change** | KEPT, and its precedent status upgraded: warning triangles are directly precedented in three corpus videos, contrary to the first pass's claim |


## SH03 — IMG03 — 3 states, 2 motions

**Narration:** So now, if the patients ask me, so is coffee good or bad for your health? I tell them that should not be the question to be asked. That's a wrong question.

**Words:** w49-w80 (32 words) · **Est. duration:** 8.14 ESTIMATEDs
**Transition in:** HARD CUT · **Transition out:** Diagram and its text removed in one frame

**Purpose:** Re-stage the binary as a real consultation, then delete it outright in front of the person who asked

**Revision change:** One state and one motion removed (F03.2 / A09, the second red strike). The deletion re-anchored from 'That's' (w77) to 'not' (w70), giving the emptied frame a 2.6s payoff hold.


### R03.0  ·  was F03.0

| | |
|---|---|
| **Script** | "So now, if the" |
| **Trigger** | HARD CUT on "So" (w49) |
| **What the viewer sees** | Off-white portrait field. Dr. Rehan stands at x6-28%, y58-92% facing frame-right: round head, rectangular glasses, short filled beard, side-swept hair stroke, plain single-stroke body, near arm lowered. Upper-centre holds a compact binary diagram: a small coffee mug at x44-56%, y14-23% with a coffee-brown liquid band, two thin black lines descending from it to two blank rounded label plates at x24-46% and x54-76%, y34-44%, carrying editor text GOOD? and BAD?. The entire right-hand lower field below y50% is empty. |
| **What changed** | (nothing - opening state of the shot) |
| **What stays static** | Off-white field; Dr. Rehan; compact fork; both plates; GOOD?/BAD? text; camera |
| **Why** | Re-state the binary as something asked inside a consultation, not as a slide |
| **How it arrives** | Hard cut in (no motion) |
| **Hold** | ~1.0s ESTIMATED (4 words) |
| **Next change** | R03.1 on "ON_WORD_START ("patients", w53)" |
| **Assets** | E01,C01,O01,G06,T01,T02 |
| **Revision change** | UNCHANGED |


### R03.1  ·  was F03.1

| | |
|---|---|
| **Script** | "patients ask me, so is coffee good or bad for your health? I tell them that should" |
| **Trigger** | ON_WORD_START ("patients", w53) |
| **What the viewer sees** | Same field, doctor and binary diagram. A second stick figure now stands in the empty right field at x72-94%, y60-92%, facing frame-left toward the doctor: plain round head, no glasses, no beard, no hair marks, plain single-stroke body, near arm slightly raised as if asking. The two figures face each other across the diagram above them. |
| **What changed** | Patient figure |
| **What stays static** | Off-white field; Dr. Rehan; fork; plates; text; camera |
| **Why** | Make the question belong to a patient, and hold that frame while the whole question is spoken |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~4.3s ESTIMATED (17 words) - a long deliberate hold while the question and its setup are delivered |
| **Next change** | R03.2 on "ON_WORD_START ("not", w70)" |
| **Assets** | E01,C01,O01,G06,T01,T02,C02 |
| **Revision change** | Exit method changed from ADDITIVE_REVEAL to STATE_REPLACEMENT: the second strike no longer intervenes, so this state now exits straight into the deletion |


### R03.2  ·  was F03.3

| | |
|---|---|
| **Script** | "not be the question to be asked. That's a wrong question." |
| **Trigger** | ON_WORD_START ("not", w70) |
| **What the viewer sees** | Same off-white field with Dr. Rehan at x6-28%, y58-92% and the patient at x72-94%, y60-92%, both unchanged and still facing each other. The entire upper-centre area is now empty off-white: the mug, both branch lines, both label plates and both text labels are all gone in one frame. Two figures, a large blank field between and above them, nothing else. |
| **What changed** | Whole binary diagram and its text - all removed |
| **What stays static** | Off-white field; Dr. Rehan; patient; camera |
| **Why** | Delete the model before the replacement arrives - the empty space is the argument |
| **How it arrives** | Remove in one frame (state replacement) — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~2.6s ESTIMATED (11 words), held to the cut |
| **Next change** | HARD CUT to the next shot |
| **Assets** | E01,C01,C02 |
| **Revision change** | RE-ANCHORED from 'That's' (w77) to 'not' (w70) and its hold extended from ~1.0s to ~2.6s, because the intervening strike state was removed. The removed group no longer includes a strike stroke. |


## SH04 — IMG04 — 3 states, 2 motions

**Narration:** The real question is, how does your body respond to caffeine or coffee? And that's the main message: don't judge coffee only as "good" or "bad."

**Words:** w81-w106 (26 words) · **Est. duration:** 6.62 ESTIMATEDs
**Transition in:** HARD CUT · **Transition out:** Second reading completes at the right-hand figure

**Purpose:** Replace the deleted model with coffee - person - response, then show two identical people reading differently

**Revision change:** Two states merged into one (F04.1+F04.2). Both curved-arrow draws converted to one-frame coupled pops, which also removes the plan's only unbuildable operation.


### R04.0  ·  was F04.0

| | |
|---|---|
| **Script** | "The real question is, how does your body" |
| **Trigger** | HARD CUT on "The" (w81) |
| **What the viewer sees** | Off-white portrait field. A flat black line-drawn coffee mug with a coffee-brown liquid band sits centred at the top, x42-58%, y12-22%. A thin horizontal baseline runs across x10-90% at y80%. Two identical plain stick figures stand on it, facing forward: left figure x14-36%, y52-80%, right figure x64-86%, y52-80%. Both have plain round heads, no glasses, no beards, no distinguishing marks, and identical posture. The whole band between y24% and y50% is empty off-white. |
| **What changed** | (nothing - opening state of the shot) |
| **What stays static** | Off-white field; baseline; mug; both figures; camera |
| **Why** | Replace the deleted model with a new one: one coffee, two people, nothing decided yet |
| **How it arrives** | Hard cut in (no motion) |
| **Hold** | ~2.0s ESTIMATED (8 words) |
| **Next change** | R04.1 on "ON_WORD_START ("respond", w89)" |
| **Assets** | E01,O01,C03 |
| **Revision change** | Frame unchanged. Asset build instruction tightened: the two figures must be one PNG duplicated in the editor, not two generated figures (see EXECUTABILITY_CHECK) |


### R04.1  ·  was F04.1 + F04.2 (MERGED)

| | |
|---|---|
| **Script** | "respond to caffeine or coffee? And that's the main message: don't" |
| **Trigger** | ON_WORD_START ("respond", w89) |
| **What the viewer sees** | Same field, mug and both figures. A thin black hand-drawn arrow now curves from the bottom-left of the mug at x44%,y23% down and left to the left figure's chest at x28%,y58%, ending in a small open arrowhead; the curve is a single smooth stroke with slightly uneven weight. At the same moment one small muted-red arc, like a single sound-wave stroke, appears at the left figure's chest at x22-30%, y58-63%. It is a single arc only. The right figure and the right half of the frame are unchanged and still empty of marks. |
| **What changed** | Left connector arrow and the left figure's single response arc (appear together) |
| **What stays static** | Off-white field; baseline; mug; both figures; camera |
| **Why** | Show the direction of the new question and the reading it produces as one idea: from the drink, to the person, to a response at the body |
| **How it arrives** | Pop on together in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~4.3s ESTIMATED (17 words) |
| **Next change** | R04.2 on "ON_WORD_START ("judge", w100)" |
| **Assets** | E01,O01,C03,G07,G08 |
| **Revision change** | MERGED from two states two words apart. Arrow and arc are one coupled idea; the corpus reveals coupled elements together rather than staggering them |


### R04.2  ·  was F04.3

| | |
|---|---|
| **Script** | "judge coffee only as "good" or "bad."" |
| **Trigger** | ON_WORD_START ("judge", w100) |
| **What the viewer sees** | Same field, mug, both figures, left arrow and the left figure's single arc. A second thin black hand-drawn arrow now curves from the bottom-right of the mug at x56%,y23% down and right to the right figure's chest at x72%,y58%, and three stacked muted-red arcs - same stroke style as the left figure's single arc, but three of them - sit at the right figure's chest at x70-80%, y55-65%. All four elements appear in the same frame. The two figures are now identical in every way except the number of arcs. Same coffee, same arrows, different reading. |
| **What changed** | Right connector arrow and the right figure's three response arcs (appear together) |
| **What stays static** | Off-white field; baseline; mug; both figures; left arrow; left arc; camera |
| **Why** | State the main message as a picture: one coffee cannot carry one label because the reading is at the person |
| **How it arrives** | Pop on together in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.8s ESTIMATED (7 words), held to the cut |
| **Next change** | HARD CUT to the next shot |
| **Assets** | E01,O01,C03,G07,G08 |
| **Revision change** | Frame unchanged. Motion changed from draw-then-pop to a single one-frame coupled pop, matching the corpus's curved-arrow treatment and making the left and right readings mechanically identical |


## SH05 — IMG05 — 5 states, 4 motions

**Narration:** Dr. Rehan explains what blood pressure, heart response and quantity have to do with it in the full video. Watch it on the channel.

**Words:** w107-w130 (24 words) · **Est. duration:** 6.11 ESTIMATEDs
**Transition in:** HARD CUT · **Transition out:** (none - final shot of the video)

**Purpose:** Name the three factors one at a time into a pre-visible scaffold, then hand off to the full video

**Revision change:** Gauge icon G10 deleted from the top plate (no corpus analogue, and a needle-on-dial implies a reading the narration never gives). Heart and three-cup icons kept - both reuse established shapes.


### R05.0  ·  was F05.0

| | |
|---|---|
| **Script** | "Dr. Rehan explains what" |
| **Trigger** | HARD CUT on "Dr." (w107) |
| **What the viewer sees** | Off-white portrait field. Dr. Rehan stands at x66-92%, y58-92% facing frame-left: round head, rectangular glasses, short filled beard, side-swept hair stroke, plain single-stroke body. On the left, three identical blank rounded-rectangle plates, thin black outline, are stacked vertically at x8-58%, occupying y20-30%, y36-46% and y52-62%. A thin vertical black connector line runs down their left edges at x12% from y25% to y57%. All three plates are completely empty. The lower-left field below y64% is blank. |
| **What changed** | (nothing - opening state of the shot) |
| **What stays static** | Off-white field; Dr. Rehan; three blank plates; connector line; camera |
| **Why** | Show that three things are coming before naming any of them |
| **How it arrives** | Hard cut in (no motion) |
| **Hold** | ~1.0s ESTIMATED (4 words) |
| **Next change** | R05.1 on "ON_WORD_START ("blood", w111)" |
| **Assets** | E01,C01,G09 |
| **Revision change** | UNCHANGED |


### R05.1  ·  was F05.1

| | |
|---|---|
| **Script** | "blood pressure," |
| **Trigger** | ON_WORD_START ("blood", w111) |
| **What the viewer sees** | Same field, doctor, three plates and connector. The top plate is now filled with editor text BLOOD PRESSURE, left-aligned inside the plate at x12-56%, y22-28%. There is no icon in the plate - the text sits alone. The middle and bottom plates remain completely blank. |
| **What changed** | Top plate contents: BLOOD PRESSURE text |
| **What stays static** | Off-white field; Dr. Rehan; all three plates; connector; camera |
| **Why** | Name the first factor on the word that names it, without implying a value, a direction or a threshold |
| **How it arrives** | Pop on in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~0.5s ESTIMATED (2 words) |
| **Next change** | R05.2 on "ON_WORD_START ("heart", w113)" |
| **Assets** | E01,C01,G09,T03 |
| **Revision change** | GAUGE ICON REMOVED. A needle-on-dial has no analogue in 448 corpus assets and reads as a measured value with a threshold, which the narration never supplies |


### R05.2  ·  was F05.2

| | |
|---|---|
| **Script** | "heart response and" |
| **Trigger** | ON_WORD_START ("heart", w113) |
| **What the viewer sees** | Same field, doctor, plates and connector, with the top plate carrying its text. The middle plate is now filled: a small single-stroke black outline heart at x12-22%, y38-44%, with editor text HEART RESPONSE to its right inside the same plate. The bottom plate remains blank. |
| **What changed** | Middle plate contents: heart icon and its text |
| **What stays static** | Off-white field; Dr. Rehan; all three plates; connector; top plate text; camera |
| **Why** | Name the second factor on its word, reusing the same heart shape drawn in SH01 |
| **How it arrives** | Pop on together in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~0.8s ESTIMATED (3 words) |
| **Next change** | R05.3 on "ON_WORD_START ("quantity", w116)" |
| **Assets** | E01,C01,G09,G11,T03,T04 |
| **Revision change** | Icon KEPT - it is the IMG01 heart returning at reduced scale, which is the corpus's reuse behaviour, not a new pictogram |


### R05.3  ·  was F05.3

| | |
|---|---|
| **Script** | "quantity have to do with it in the" |
| **Trigger** | ON_WORD_START ("quantity", w116) |
| **What the viewer sees** | Same field with the top plate carrying its text and the middle plate carrying its heart and text. The bottom plate is now filled: three small coffee cups drawn in a row in decreasing size at x12-26%, y54-60%, each with a coffee-brown liquid band, and editor text QUANTITY to their right inside the same plate. All three plates are now filled and the list is complete. |
| **What changed** | Bottom plate contents: three-cup icon and its text |
| **What stays static** | Off-white field; Dr. Rehan; all three plates; connector; top and middle plate contents; camera |
| **Why** | Complete the list - and make quantity a picture of cups, not a number |
| **How it arrives** | Pop on together in one frame — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~2.0s ESTIMATED (8 words) |
| **Next change** | R05.4 on "ON_WORD_START ("full", w124)" |
| **Assets** | E01,C01,G09,G11,G12,T03,T04,T05 |
| **Revision change** | Icon KEPT - it repeats the already-established mug rather than introducing a new shape |


### R05.4  ·  was F05.4

| | |
|---|---|
| **Script** | "full video. Watch it on the channel." |
| **Trigger** | ON_WORD_START ("full", w124) |
| **What the viewer sees** | Same off-white field with Dr. Rehan unchanged at x66-92%, y58-92%. The three plates, all their contents and the connector line are gone. In their place a single blank rounded rectangle, thin black outline, sits at x8-58%, y28-54%, with a hollow black triangular play mark centred inside it pointing right. Editor text WATCH THE FULL VIDEO sits below the rectangle at x8-58%, y58-63%. Same off-white field, same line weight, same doctor. No logo, no channel art, no colour panel. |
| **What changed** | Three plates, contents and connector removed; video card, play mark and CTA text added in their place |
| **What stays static** | Off-white field; Dr. Rehan; camera |
| **Why** | Hand off to the full video without leaving the visual language the rest of the Short is written in |
| **How it arrives** | Replace in one frame (state replacement) — 1 frame (0.042s ESTIMATED) |
| **Hold** | ~1.8s ESTIMATED (7 words), held to the end |
| **Next change** | End of video |
| **Assets** | E01,C01,G13,T06 |
| **Revision change** | UNCHANGED, with its weakness restated: the swap mechanism is precedented but no corpus video ends on a CTA, so the content of this state is grammar-transferred rather than evidenced |


---

## What the storyboard no longer contains

Three things in the first-pass storyboard are absent here, each removed on
evidence recorded in `STATE_REVIEW.csv` and `MOTION_REVIEW.csv`:

- **F03.2** — the second red strike over the consultation diagram. Removed as a
  repetition of a gesture already taught in SH01 and immediately superseded by
  the deletion seven words later. SH01 now marks the model wrong and SH03
  deletes it: escalation instead of repetition.
- **F04.2 as a separate state** — the left figure's response arc. The arc is
  kept; the stagger is not. It now appears in the same frame as the arrow it
  belongs to.
- **The blood-pressure gauge icon** — no analogue among the brain's 448 assets,
  and a needle on a dial reads as a measured value against a threshold that the
  narration never supplies.

Everything else the first pass drew is still here.
