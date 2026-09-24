# Weird and Worrying Questions — v7.0 Video Forensic Reconstruction Blueprint
> Source authority: the attached MP4. The pasted v7.0 document defines the analysis/output contract; it is not evidence about what appears in the video. All visual and motion claims below are grounded in decoded source frames, adjacent-frame comparison, measured timing, verified audio, or OCR.
## Evidence ledger
- **Source video:** `Weird and worrying questions.mp4`; SHA-256 `eafaf03040a83da4836eb51847d512f2616a8c6deb65d5ee5431a9cf7be574d7`; 7,551,690 bytes.
- **Measured media:** 47.501814 s container duration; 720×1280; vertical 9:16; 24.000 fps nominal; H.264/AVC (`avc1`); Rec.709 metadata. AAC stereo audio, 44.1 kHz, 47.501814 s.
- **Decoded visual evidence:** 191 frames at 4 Hz plus 1,141 dense samples at 24 Hz. Representative source images are full-resolution 720×1280 extractions.
- **Audio evidence:** 47.460136 s decoded PCM; eight Whisper segments, then corrected only where source-card OCR/visual inspection contradicted a word. Overall RMS −19.64 dBFS; absolute peak 0.719849; three measured ≥0.15 s sub−42 dBFS intervals.
- **Text evidence:** 159 OCR observations on proxy frames and 159 on the 34 selected full-resolution frames, followed by human visual confirmation.
- **Limit:** exact original software, font files, easing curves, individual sound-library assets, and any underlying illustration source files cannot be verified. Reconstruction methods are fidelity recommendations, not claims about the original toolchain.
## Pass results and state model
PASS 0 inspected media; PASS 1 found 7 major compositional shots; PASS 2 locked 34 meaningful states; PASS 3 used source-cadence dense sampling; PASS 4 assigned 33 persistent assets; PASS 5 built state chains with 39 motion/transition events; PASSES 6–13 cover script, visuals, images, motion isolation, prompts, edit and audio below; PASSES 14–15 synthesize and audit the system. Long zero-difference runs in the dense metric confirm that most motion is intentionally implemented as holds interrupted by replacement drawings, additive reveals and hard cuts.
# Engine A — Script Intelligence
## A1. Verified script beats
| Beat | Time | Function | Grounded content | Active viewer question | Loop status |
|---|---:|---|---|---|---|
| SB01 | 00:00.000–00:05.600 | QUESTION / HOOK | Shelby’s cold-teeth/hot-coffee hypothetical | Will the premise produce a bodily consequence? | OPEN → ANSWERED by V04/V05 |
| SB02 | 00:06.460–00:08.400 | MICRO-PAYOFF / REACTION | ‘Thank you Shelby for my new recurring nightmare.’ | How bad is the mental image? | ANSWERED by V06 |
| SB03 | 00:08.900–00:12.208 | TRANSITION / PATTERN BREAK | More weird and worrying What If inbox questions; mirror-harm question shown silently | How much more alarming will the inbox become? | ESCALATING |
| SB04 | 00:12.208–00:16.580 | QUESTION / ESCALATION | Jeff asks whether humanity can build a new star | Is this technically possible—and why ask? | PARTIALLY ANSWERED by star visualization |
| SB05 | 00:17.320–00:20.600 | REVERSAL / PAYOFF | Narrator questions Jeff’s motive; MAYBE becomes SUN OBLITERATOR | Is Jeff planning something dangerous? | ANSWERED comedically |
| SB06 | 00:21.240–00:27.020 | QUESTION / CONSEQUENCE | Tomasz proposes a bomb under a volcano | Would intervention stop or worsen the eruption? | ANSWERED by explosion |
| SB07 | 00:28.060–00:33.520 | QUESTION / PARALLEL ESCALATION | AJ proposes antimatter in the Chernobyl reactor | Would an extreme material stop a meltdown? | ANSWERED by a second explosion |
| SB08 | 00:34.400–00:40.320 | MAJOR PAYOFF | AJ and Tomasz receive the ‘what were you thinking’ award | How will the video judge both disaster responses? | ANSWERED / COMBINED CALLBACK |
| SB09 | 00:40.940–00:45.000 | QUESTION / TONAL REVERSAL | Karl asks whether crying can cause dehydration | Is the question merely hypothetical? | OPEN → REFRAMED |
| SB10 | 00:45.000–00:46.640 | EMPATHETIC PAYOFF | ‘Karl, is everything okay?’ | Is Karl personally okay? | OPEN-ENDED CLOSURE |

## A2–A12. Packaging, hook, causality, curiosity and payoff
**TITLE PROMISE:** “Weird and worrying questions” promises a curated sequence of escalating, unsettling hypotheticals. **THUMBNAIL PROMISE:** no separate thumbnail file was supplied; cannot verify. **COMBINED CLICK QUESTION:** which questions are weird, how worrying do they become, and how will the narrator react? **MATCH:** STRONG MATCH—the body repeatedly validates both adjectives and the award bundles the most dangerous entries.

The hook uses a familiar Q-card, an immediate body-risk contradiction (extreme cold versus hot coffee), then a literal consequence. The causal spine is: question → visualized mechanism → destructive/reaction payoff; **BUT** a new submitter escalates the risk; **THEREFORE** two disaster questions are grouped; **PAYOFF** they receive one shared award; **REVERSAL** Karl’s sadness triggers concern rather than ridicule. Curiosity expands through V09–V25, peaks at the double-disaster callback, then deliberately contracts into empathy.

**Payoff ladder:** shattered teeth → tossed cup → mirror threat → new star → Sun Obliterator → volcano blast → reactor blast → joint award → concern for Karl. The sequence earns its largest payoff by repeating the same cause/consequence grammar twice before combining AJ and Tomasz.

**Logic:** the piece is comedic curation, not a scientific answer video. It does not claim the depicted interventions are accurate simulations; it maps each question to a consequence drawing. No unsupported factual conclusion should be inferred from the illustrations.

**Emotion:** curiosity and unease dominate; absurdity supplies humor; the last beat adds empathy. **Retention risks:** the silent mirror question at V09 demands fast reading; Jeff’s machine hold is the longest internal setup; the award copy is readable because the state holds 2.167 s. **Share/replay:** V09 and V28 are shareable; V24’s hand-lettered label may cause a short legibility replay. **CTA/NEXT VIDEO:** none observed; the clip ends on the Karl concern and noise plate.
## A13. Script consensus
**STRONG AGREEMENTS:** repeated question→visual consequence units are instantly understandable; the two-disaster callback is the structural high point; Karl’s close prevents tonal monotony. **IMPORTANT TRADEOFF:** the rapid mirror card strengthens pattern interruption but reduces reading time. **CRITICAL PROBLEM:** none evidenced at clip scale. **HIGH PRIORITY:** if adapting, keep the common card/reader frame so each escalation feels like part of one inbox. **MEDIUM PRIORITY:** keep individual question wording shorter when it must be read silently. **HIGHEST-LEVERAGE FIX:** reserve the strongest combined judgment for two related prior beats, as V26–V28 does.
# Engine B — Visual Intelligence
## B1–B5. Objective grammar, geometry, attention and cinematography
The visual system is a locked frontal 9:16 white stage. A light-gray rounded question card occupies the top ~5–95% width; the faceless reader/desk/chair cluster anchors the bottom ~17–66% width; a scalloped thought bubble normally fills the middle ~6–94% width. The mirror beat and award break that template but preserve the same low reader anchor. There is no evidenced lens change or physical camera move. Perspective is deliberately flat, with thin irregular black pen lines, sparse hatching, white fills and a single recurring saturated red thermometer accent.

Repeated eye path: question card → new central explanatory object → reader reaction. V09 reverses it through large uppercase lettering and the visitor’s black hair block; V26–V28 use the certificate as one dominant plane. Attention is CLEAN/CONTROLLED in ordinary states and intentionally COMPETITIVE only when the award combines recipient line, hazard icons and title.
## B6–B12. Temporal change, editing, information value and continuity
Material change is almost entirely discrete: add bubble, add object, replace drawing, add exact lettering, or hard cut. The only observed continuous motifs are short redraw variations in mug steam and changing gray noise. The persistent reader, furniture, card position, bubble position and white coordinate frame make every replacement legible. Essential/explanatory visuals are the teeth, star apparatus, volcano and reactor; evidential/payoff visuals are their destroyed states; the noise plates are transitional; no persistent decorative motion is evidenced.

Object lifecycle examples: teeth intact → cold thermometer → fragments → hot mug; star apparatus → produced star → suspicious person → MAYBE → weapon; volcano → bomb → blast; reactor → antimatter label → blast; radiation/bomb icons return on the award. Continuity drift is minimal because recurring elements are exact reused drawings. Minor line flicker in long holds is below semantic-change threshold and should not be recreated as object motion.
## B13–B15. Color, typography and visual DNA
**Dominant:** white. **Secondary:** black line art and light gray card fills/noise. **Accent:** thermometer red only, scarce enough to claim first look. **Typography:** question cards use compact black sans-serif, sentence case, left aligned; punch lines and labels use irregular uppercase hand lettering. Exact text is editor-rendered in this reconstruction. **Visual DNA:** faceless stick figures; stable top/middle/bottom modules; scalloped thought bubbles; replacement drawings; flat white depth; locked camera; 0.21 s gray-noise separators; payoff through object transformation rather than camera energy.
# Engine C — Reconstruction and Motion Intelligence
## C. Global production routing
Primary fidelity route: rebuild one registered clean base for the card/reader stage; draw or vector-trace each thought-bubble state; keep all lettering as deterministic overlays; use stepped replacement states at measured cut times; loop only the steam strokes and procedural gray noise. Generative video is not the primary method because exact line registration, card typography and abrupt reference timing are more faithfully reproduced in an editor. Every event below still includes a bounded optional AI instruction and source state.

**Same-frame isolation:** at V06, generate/draw the steam loop and the reader/cup reaction independently, then composite both over the fixed card/bubble/furniture base. **Precision graphics:** exact card wording, MAYBE, SUN OBLITERATOR, ANTIMATTER, award recipients/title and Karl’s closing line remain editor overlays. **Leakage risks:** text drift, bubble-shape drift and reader identity/position drift; prevent them with clean plates, region masks and exact reuse outside each ROI.
# Editing Decision List
| Segment | In | Out | Duration | Visual states | Transition | Cut motivation | Motion hero | Static anchor |
|---|---:|---:|---:|---|---|---|---|---|
| S01 | 00.000 | 08.917 | 8.917 s | V01, V02, V03, V04, V05, V06 | TR01 gray-noise bridge | Hook with bodily-harm hypothetical, then comic reaction | teeth/thermometer/mugs | card + reader/desk |
| S02 | 09.125 | 12.208 | 3.083 s | V08, V09 | hard cut to S03 | Pattern interrupt that broadens the inbox premise | mirror question + visitor | lower reader/desk |
| S03 | 12.208 | 21.167 | 8.959 s | V10, V11, V12, V13, V14, V15 | TR02 gray-noise bridge | Escalate from possible star to suspicious weaponized interpretation | star mechanism → weapon | card + reader/desk + bubble |
| S04 | 21.375 | 28.167 | 6.792 s | V17, V18, V19, V20 | TR03 gray-noise bridge | Present and immediately visualize destructive disaster response | volcano → bomb → blast | card + reader/desk + bubble |
| S05 | 28.375 | 34.750 | 6.375 s | V22, V23, V24, V25 | hard cut to S06 | Parallel second disaster-response question and destruction | reactor → antimatter → blast | card + reader/desk + bubble |
| S06 | 34.750 | 40.750 | 6.000 s | V26, V27, V28 | TR04 gray-noise bridge | Bundle AJ and Tomasz into one comic judgment/payoff | award text | certificate + lower reader |
| S07 | 40.958 | 47.292 | 6.334 s | V30, V31, V32, V33 | TR05 gray-noise end | Switch from hazardous joke to empathetic final button | crying figure → concern | card + reader/desk |
| TR01 | 08.917 | 09.125 | 0.208 s | gray-noise plate | hard in / hard out | recurring section separator | procedural noise | locked 9:16 boundary |
| TR02 | 21.167 | 21.375 | 0.208 s | gray-noise plate | hard in / hard out | recurring section separator | procedural noise | locked 9:16 boundary |
| TR03 | 28.167 | 28.375 | 0.208 s | gray-noise plate | hard in / hard out | recurring section separator | procedural noise | locked 9:16 boundary |
| TR04 | 40.750 | 40.958 | 0.208 s | gray-noise plate | hard in / hard out | recurring section separator | procedural noise | locked 9:16 boundary |
| TR05 | 47.292 | 47.502 | 0.210 s | gray-noise plate | hard in / hard out | recurring section separator | procedural noise | locked 9:16 boundary |

**Measured major-shot statistics:** total 7; average 6.637 s; median 6.375 s; shortest S02 at 3.083 s; longest S03 at 8.959 s. Fastest cluster is the 0.208–0.210 s transition family; slowest cluster is the 6.0–8.959 s question/payoff holds. Cuts align to question changes, drawing completion, consequence reveals or punch-line completion—not arbitrary equal blocks.
# Audio Intelligence
Verified semantic layer: one English narrator, eight Whisper segments spanning 00:00.000–00:46.640. The first segment’s model output ‘eat your teeth’ is rejected because the full-resolution card clearly reads ‘get your teeth’; the report follows the frame evidence. No music or named SFX can be semantically verified from the supplied mix. The stereo side channel measures −38.19 dBFS versus −19.64 dBFS mid, so most energy is centrally correlated; any low-level remainder stays unclassified.

| Audio event | Time | Visual event |
|---|---:|---|
| Shelby question | 00:00.000–00:05.600 | A01–A05 build teeth/temperature/shatter/coffee chain |
| Recurring-nightmare reaction | 00:06.460–00:08.400 | A06 reader toss replacement |
| Inbox reset | 00:08.900–00:12.208 | TR01 then A10 mirror-question pattern break |
| Jeff question | 00:12.208–00:16.580 | A11–A13 card, machine and star |
| Suspicion of Jeff | 00:17.320–00:20.600 | A14–A16 person, MAYBE, Sun Obliterator |
| Tomasz question | 00:21.240–00:27.020 | A19–A22 volcano/bomb/blast |
| AJ question | 00:28.060–00:33.520 | A25–A28 reactor/antimatter/blast |
| Joint award | 00:34.400–00:40.320 | A29–A31 certificate recipient/title build |
| Karl question and concern | 00:40.940–00:46.640 | A34–A37 cry visualization then direct concern |

Measured sub−42 dBFS intervals ≥0.15 s: 34.45–34.70, 45.45–45.90 and 46.90–47.25. These occur near state changes/line endings; do not infer designed silence or a specific SFX without isolated stems. Preserve voice clarity first, match line ends to discrete visual events, and avoid adding impacts where the reference provides only a replacement drawing.
# Thumbnail and Shorts Extraction
**Thumbnail candidates:** V09 (large alarming mirror question + black-haired visitor; remove desk detail and enlarge text/visitor for mobile), V20 or V25 (single blast inside clear thought bubble; retain only one question cue), V28 (award title and paired hazard icons; strongest packaging match), V33 (empathetic contrast; enlarge reader and final question). V28 is the strongest general candidate because it compresses two prior stories into one readable judgment.

**Shorts candidates:** (1) 21.240–40.320, 19.08 s: Tomasz question → explosion → AJ question → explosion → joint award. Hook on the volcano/bomb proposal, preserve both question cards for attribution, and use V28 as payoff; CTA unnecessary. (2) 40.940–46.640, 5.70 s: Karl question → crying visualization → ‘is everything okay?’; context is self-contained, with V31 as core image and V33 as payoff. Use the corresponding standalone prompts and A20–A31 or A35–A37 instructions below; do not invent extra animation.
# Engine D — Master Production Synthesis
## D1–D5. Story, script, visual, motion and AI engines
**Story formula:** unsettling question → literal diagram → consequence/reaction → larger related question → paired escalation → callback award → empathetic reversal. **Script formula:** read exact submission, withhold commentary until the visual consequence is legible, then deliver a one-line judgment. **Visual formula:** persistent card + reader coordinate frame; replace only the thought-bubble payload. **Creator motion formula:** lock camera and base; add one semantic drawing per trigger word; use an instantaneous replacement when the meaning changes; loop only a visible local phenomenon; cut through 0.21 s gray noise between unrelated inbox clusters.

Usually moving/changing: newly introduced explanatory object, consequence drawing, exact punch-line text, steam strokes and transition noise. Usually static: question card, reader-stage geometry, bubble border/tail, furniture and white background. AI-friendly primary states: none required. Optional AI is most plausible for A05 steam; all registration-sensitive text, icons, diagrams and hard replacements are editor-controlled. No first/last-frame generative package is necessary because source timing is abrupt rather than interpolated.
## D6–D9. Image, attention, callbacks and improvements
**MASTER CHARACTER PROMPT:** faceless black-pen stick figure, circular head, single-line limbs/torso, seated side-on at a simple desk, deliberately irregular hand-drawn line weight, no facial features, flat white fill. **MASTER OBJECT PROMPT:** sparse black-outline educational doodle, recognizable silhouette, minimal hatching only where evidenced. **MASTER ENVIRONMENT PROMPT:** pure-white vertical stage with top question module, middle thought module, bottom reader module. **MASTER GRAPHIC PROMPT:** light-gray rounded question panel and irregular scalloped thought bubble. **STYLE/COLOR:** black, white, light gray; red reserved for the thermometer. **TYPOGRAPHY:** exact editor overlays, sans-serif for questions and irregular uppercase hand lettering for punch lines.

Repeated eye path: top question → central object change → lower reaction. Callback chain: radiation icon/volcano bomb → separate explosions → both icons and both names on award. **Critical improvement:** none needed for reference reconstruction. **High:** when adapting, increase V09 reading hold if copy is not already known. **Medium:** slightly enlarge V24’s ANTIMATTER label for small screens. **Optional:** preserve the quiet Karl close; adding a CTA would weaken its tonal function.
## D10. New-topic translation
| Original function | Original image mechanism | Original motion/edit mechanism | New-topic equivalent | Keep | Change |
|---|---|---|---|---|---|
| Bodily-risk hook | object + condition icon + consequence | additive reveals then replacement | any everyday object under two conflicting conditions | card/bubble/reader grammar and trigger order | facts, object and consequence |
| Suspicious capability | machine creates desired output | output reveal then motive reversal | tool creates powerful result, followed by suspicious use | machine→result→motive chain | machine and result |
| Intervention question | hazard + proposed intervention | add intervention then replace with consequence | system plus risky fix | vertical cause/effect layout | hazard, intervention and result |
| Paired callback | two prior hazard icons/names on certificate | sequential exact text reveals | compare two related submissions in one judgment frame | icon reuse and payoff delay | names, award copy, branding |
| Empathetic close | sad literal visualization | remove diagram; address submitter directly | tonal shift from absurdity to concern | quiet hold and direct question | person/fact/context |

Rule: copy production grammar, not surface content.
# Zero-to-Final Rebuild Order
1. Lock the title promise and question sequence.
2. Time the ten script beats to the verified voice track.
3. Build the causal question→visual→consequence→reaction spine.
4. Create the seven-shot and five-transition plan.
5. Register all 34 state frames on a 720×1280 canvas.
6. Build the 33-item persistent asset library.
7. Draw the reader/desk/card master clean plate.
8. Generate or draw every thought-bubble state in chain order.
9. Preserve text-free clean plates for all cards, labels and certificate states.
10. Add exact typography as overlays.
11. Follow the 39-event inventory without adding motion.
12. Apply coupling decisions; keep A05 steam independent from A06 reaction.
13. Isolate every changed ROI over the locked base.
14. Treat all AI passes as optional approximations, not primary.
15. If testing AI, begin with A05 only.
16. Use independent masks for any same-frame AI alternatives.
17. Do not force first/last interpolation across hard reference replacements.
18. Build text, icons, noise and cuts deterministically.
19. Composite loop/reaction layers at V06.
20. Assemble the EDL at measured boundaries.
21. Align narration phrase ends to reveals.
22. Keep pure white/black/light gray color discipline and thermometer red.
23. Audit reader/card/bubble registration across reuse.
24. Inspect text, background and geometry leakage.
25. Confirm each question earns its visual payoff.
26. Export H.264 720×1280 at 24 fps with AAC stereo and verify 47.502 s duration.
# Completeness Audit
SOURCE VIDEO INSPECTED: YES  
MAJOR SHOTS: 7  
VISUAL STATES: 34  
SCRIPT BEATS: 10  
PERSISTENT ASSETS: 33  
VISUAL CARDS: 34/34  
STANDALONE IMAGE PROMPTS: 34/34  
TEXT BAKE DECISIONS: 34/34  
FRAME STATE CHAINS: 7/7 + 5 transition chains  
TOTAL MOTION EVENTS: 39  
MOTION EVENTS IDENTIFIED: 39/39  
WHY-MOVE ANALYSIS: 39/39  
STATIC-ANCHOR ANALYSIS: 39/39  
MOTION COUPLING CLASSIFIED: 39/39  
MOTION INTERFERENCE CHECK: 39/39  
AI SUITABILITY: 39/39  
PRIMARY METHODS: 39/39  
AI SINGLE-PASS: 0 primary  
AI MULTI-PASS: 0 primary; one optional isolated same-frame composite at V06  
AI STATE-CHAIN: 0 primary  
FIRST/LAST FRAME: 0 primary  
HYBRID: 3 events in the V05–V06 steam/reaction chain  
DETERMINISTIC: 36 remaining events  
STATIC: 27 stable state holds  
AI SOURCE IMAGES IDENTIFIED: 39/39  
AI PROMPTS: 39/39 optional bounded alternatives  
AI PROMPTS ≤500: 39/39  
PROMPT CHARACTER COUNTS: 39/39  
TRANSITIONS: 5/5  
EDL: COMPLETE  
AUDIO: COMPLETE for speech/timing; LIMITED for stem identity  
MASTER SYNTHESIS: COMPLETE
# Final Quality Gate
**REFERENCE FIDELITY:** PASS—no decorative camera drift, parallax, particles, glow, wobble or background motion has been added. **IMAGE:** PASS—every state has a source frame, independent prompt, clean-plate decision and overlay plan. **MOTION:** PASS—all 39 observed changes/loops are isolated and ordered. **SAME FRAME:** PASS—steam and the cup reaction are separated. **AI:** PASS—AI remains optional where deterministic registration is superior. **PROMPTS:** PASS—camera, target, action, anchors and end condition are included; every count is ≤500. **STATE CHAIN:** PASS—each event names the correct preceding state. **EDITING:** PASS—masks can preserve all unrelated line art. **FINAL TEST:** a competent animator/editor can rebuild the motion grammar without guessing what moves.
# Visual Reconstruction Cards
The following 34 cards are the production authority. Coordinates are approximate normalized visual maps, not pixel measurements. Every text-bearing state uses a clean generated/drawn plate and exact editor overlay.

## V01 — 00.500s — Shelby question + seated reader
**SHOT:** S01  
**DURATION:** 1.125 s (00.000–01.125)  
**FRAME STATE:** F01.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V01_0000500ms.jpg)

![V01 source frame](weird_worrying_forensics/keyframes/V01_0000500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a light-gray Shelby question card sits at the top; far below, a faceless stick figure reads a small device while seated between a desk/monitor and chair on an otherwise white field. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A light-gray Shelby question card sits at the top; far below, a faceless stick figure reads a small device while seated between a desk/monitor and chair on an otherwise white field.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Shelby asks, ‘Would it be possible to get your teeth to such a cold temperature…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Ground the submitted question and establish the recurring inbox stage.  
**MOTION CUE:** opening state.  
**FUNCTION:** Ground the submitted question and establish the recurring inbox stage.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** opening state. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Ground the submitted question and establish the recurring inbox stage. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A light-gray Shelby question card sits at the top; far below, a faceless stick figure reads a small device while seated between a desk/monitor and chair on an otherwise white field.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** question panel.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** blank card X 5–95/Y 6–28; reader/desk cluster X 17–66/Y 71–95; empty middle X 0–100/Y 29–70. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** question panel → reader’s face/device → desk/monitor.
### 7. ATTENTION ORDER
**FIRST LOOK:** question panel. **SECOND/THIRD:** reader’s face/device → desk/monitor. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** NEW BASE; STABLE. **BASE:** opening. **CHANGES:** opening state.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place a blank light-gray rounded question panel across the upper 86% width; place the faceless seated reader and compact desk-monitor-chair cluster in the lower-left/center, leaving the entire middle white. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V01. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.0. **SHOT:** S01. **MEASURED RANGE:** 00.000–01.125. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
opening → V01/F01.0 → V02. The transition into this state is opening state; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
No incoming animation: this is the opening stable source state. **ANIMATION REQUIRED:** NO; editor action is a 1.125 s hold until A01.
### 17. WHY MOVE
Nothing moves. Stillness lets the viewer read the long opening card and establishes the coordinate system before the first explanatory reveal.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** All visible elements; this opening state is a measured static hold.. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
Allowed motion: none. Lock the full frame. Disturbance risk is avoided by using a static source image, not a generated video hold.
### 20. MOTION COUPLING CLASSIFICATION
STATIC HOLD; no coupling decision is needed.
### 21. RECOMMENDED PRODUCTION METHOD
STATIC HOLD from the extracted/drawn clean plate.
### 22. AI SUITABILITY
N/A; AI would only risk drift in a frame that must remain still.
### 23. AI ISOLATION PLAN
No AI pass. Hold the reference-matched still.
### 24. SOURCE IMAGE FOR EACH AI PASS
Opening source is the V01 reference frame itself; no AI pass begins here.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
**ANIMATION REQUIRED:** NO. **EDITOR ACTION:** hold this still until 1.125 s. **AI PROMPT:** N/A.
### 26. EDITOR / COMPOSITING BUILD
Place the 720×1280 still on a 24 fps sequence, hold to 1.125 s, and keep all transforms at native size/position.
### 27. EDIT OUT / NEXT STATE
At 01.125s, transition to V02. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V01 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V02 — 01.500s — Teeth thought bubble
**SHOT:** S01  
**DURATION:** 1.250 s (01.125–02.375)  
**FRAME STATE:** F01.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V02_0001500ms.jpg)

![V02 source frame](weird_worrying_forensics/keyframes/V02_0001500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the Shelby card and reader remain; a large scalloped thought bubble fills the middle and contains one centered intact row of teeth. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The Shelby card and reader remain; a large scalloped thought bubble fills the middle and contains one centered intact row of teeth.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Shelby’s question continues through ‘…such a cold temperature…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Convert the bodily premise into a concrete object before consequences appear.  
**MOTION CUE:** add scalloped thought bubble and teeth drawing.  
**FUNCTION:** Convert the bodily premise into a concrete object before consequences appear.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add scalloped thought bubble and teeth drawing. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Convert the bodily premise into a concrete object before consequences appear. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The Shelby card and reader remain; a large scalloped thought bubble fills the middle and contains one centered intact row of teeth.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** teeth.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** card X 5–95/Y 6–28; bubble X 6–94/Y 30–69; teeth X 29–75/Y 41–50; reader X 18–66/Y 70–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** teeth → question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** teeth. **SECOND/THIRD:** question panel → reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V01. **CHANGES:** add scalloped thought bubble and teeth drawing.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank top question panel and lower reader stage; add a large scalloped thought bubble across the middle with a single intact front-view row of teeth centered inside. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V02. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.1. **SHOT:** S01. **MEASURED RANGE:** 01.125–02.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V01 → V02/F01.1 → V03. The transition into this state is add scalloped thought bubble and teeth drawing; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A01 (additive reveal; thought bubble and intact teeth; 1.125–1.125 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A01:** Externalizes the cold-teeth premise without moving the persistent reader Direction/speed/path are limited to `instant full-state replacement; no travel path` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** question card, seated reader, desk, chair, monitor, white field. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A01 ALLOWED TO MOVE/CHANGE:** thought bubble and intact teeth. **LOCKED:** question card, seated reader, desk, chair, monitor, white field. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A01: STATE REPLACEMENT—thought bubble and intact teeth is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A01: REPLACEMENT DRAWING / editor cut. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A01: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A01:** isolate `X 7-94 Y 29-70` over the fixed V01/F01.0 base; generate/change only thought bubble and intact teeth; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A01 SOURCE FRAME STATE:** V01/F01.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V01_0000500ms.jpg). If regeneration is required, use the full standalone prompt in card V01, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A01
**SOURCE STATE:** V01/F01.0  
**TARGET STATE:** V02/F01.1  
**TIMESTAMP:** 01.125–01.125  
**MOTION TYPE/HERO:** additive reveal / thought bubble and intact teeth  
**DIRECTION, SPEED, PATH:** instant full-state replacement; no travel path  
**CAMERA:** locked  
**STATIC ANCHORS:** question card, seated reader, desk, chair, monitor, white field  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the observed scalloped thought bubble above the seated reader in one clean replacement beat, containing only the centered intact teeth row. Preserve the question card, reader, desk, chair, monitor, proportions and white background exactly. Hold the completed drawing.”  
**CHARACTER COUNT:** 286 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A01 uses `REPLACEMENT DRAWING / editor cut` in ROI X 7-94 Y 29-70; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 02.375s, transition to V03. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V02 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V03 — 02.750s — Cold thermometer added
**SHOT:** S01  
**DURATION:** 1.500 s (02.375–03.875)  
**FRAME STATE:** F01.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V03_0002750ms.jpg)

![V03 source frame](weird_worrying_forensics/keyframes/V03_0002750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the teeth bubble persists and a slim vertical thermometer with a red bulb now occupies its left edge. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The teeth bubble persists and a slim vertical thermometer with a red bulb now occupies its left edge.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Shelby’s question continues; the visual lands on the temperature idea.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Make the phrase “cold temperature” instantly legible through a scarce color accent.  
**MOTION CUE:** add red-bulb thermometer at left of bubble.  
**FUNCTION:** Make the phrase “cold temperature” instantly legible through a scarce color accent.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add red-bulb thermometer at left of bubble. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Make the phrase “cold temperature” instantly legible through a scarce color accent. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The teeth bubble persists and a slim vertical thermometer with a red bulb now occupies its left edge.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** red thermometer.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** thermometer X 10–20/Y 38–64; teeth X 29–75/Y 41–50; all persistent regions unchanged. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** red thermometer → teeth → question panel.
### 7. ATTENTION ORDER
**FIRST LOOK:** red thermometer. **SECOND/THIRD:** teeth → question panel. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V02. **CHANGES:** add red-bulb thermometer at left of bubble.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank top panel, lower reader and teeth bubble; add a slim outlined thermometer at the bubble’s far left with a small red bulb and red fluid column as the only saturated color. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V03. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.2. **SHOT:** S01. **MEASURED RANGE:** 02.375–03.875. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V02 → V03/F01.2 → V04. The transition into this state is add red-bulb thermometer at left of bubble; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A02 (additive reveal; thermometer; 2.375–2.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A02:** Makes “cold temperature” readable through the only saturated color cue Direction/speed/path are limited to `instant appearance at bubble left` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** teeth, bubble outline, card, reader and desk cluster. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A02 ALLOWED TO MOVE/CHANGE:** thermometer. **LOCKED:** teeth, bubble outline, card, reader and desk cluster. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A02: SEQUENTIAL—thermometer is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A02: VECTOR/REPLACEMENT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A02: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A02:** isolate `X 9-22 Y 36-65` over the fixed V02/F01.1 base; generate/change only thermometer; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A02 SOURCE FRAME STATE:** V02/F01.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V02_0001500ms.jpg). If regeneration is required, use the full standalone prompt in card V02, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A02
**SOURCE STATE:** V02/F01.1  
**TARGET STATE:** V03/F01.2  
**TIMESTAMP:** 02.375–02.375  
**MOTION TYPE/HERO:** additive reveal / thermometer  
**DIRECTION, SPEED, PATH:** instant appearance at bubble left  
**CAMERA:** locked  
**STATIC ANCHORS:** teeth, bubble outline, card, reader and desk cluster  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Reveal only the slim thermometer at the left inside edge of the thought bubble, with a black outline and red bulb/fluid accent matching the target. Keep the teeth, bubble contour, question card, seated reader, furniture and white background fixed. Hold.”  
**CHARACTER COUNT:** 268 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A02 uses `VECTOR/REPLACEMENT OVERLAY` in ROI X 9-22 Y 36-65; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 03.875s, transition to V04. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V03 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V04 — 04.000s — Teeth shattered
**SHOT:** S01  
**DURATION:** 0.667 s (03.875–04.542)  
**FRAME STATE:** F01.3  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V04_0004000ms.jpg)

![V04 source frame](weird_worrying_forensics/keyframes/V04_0004000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the thermometer remains, but the formerly intact teeth are replaced by a dense broken cluster of shards and small oval fragments. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The thermometer remains, but the formerly intact teeth are replaced by a dense broken cluster of shards and small oval fragments.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…that they would shatter…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Pay off “shatter” with one abrupt, readable state replacement.  
**MOTION CUE:** replace intact teeth with dense fragments.  
**FUNCTION:** Pay off “shatter” with one abrupt, readable state replacement.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace intact teeth with dense fragments. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Pay off “shatter” with one abrupt, readable state replacement. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The thermometer remains, but the formerly intact teeth are replaced by a dense broken cluster of shards and small oval fragments.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** shattered cluster.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** fragment cluster X 26–78/Y 39–54; thermometer X 10–20/Y 38–64; bubble/card/reader unchanged. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** shattered cluster → red thermometer → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** shattered cluster. **SECOND/THIRD:** red thermometer → reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V03. **CHANGES:** replace intact teeth with dense fragments.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank top panel, lower reader, bubble and red thermometer; replace the intact teeth with a dense irregular black-line field of broken teeth, shards and small oval fragments in the same center footprint. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V04. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.3. **SHOT:** S01. **MEASURED RANGE:** 03.875–04.542. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V03 → V04/F01.3 → V05. The transition into this state is replace intact teeth with dense fragments; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A03 (replacement drawing; teeth; 3.875–3.875 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A03:** Pays off “shatter” as an immediate visual consequence Direction/speed/path are limited to `intact row switches to dense broken fragments in place` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** thermometer, bubble, card, reader and furniture. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A03 ALLOWED TO MOVE/CHANGE:** teeth. **LOCKED:** thermometer, bubble, card, reader and furniture. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A03: STATE REPLACEMENT—teeth is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A03: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A03: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A03:** isolate `X 28-76 Y 39-52` over the fixed V03/F01.2 base; generate/change only teeth; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A03 SOURCE FRAME STATE:** V03/F01.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V03_0002750ms.jpg). If regeneration is required, use the full standalone prompt in card V03, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A03
**SOURCE STATE:** V03/F01.2  
**TARGET STATE:** V04/F01.3  
**TIMESTAMP:** 03.875–03.875  
**MOTION TYPE/HERO:** replacement drawing / teeth  
**DIRECTION, SPEED, PATH:** intact row switches to dense broken fragments in place  
**CAMERA:** locked  
**STATIC ANCHORS:** thermometer, bubble, card, reader and furniture  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace only the intact teeth row with the observed dense shattered-teeth drawing in the same center position and approximate footprint. Preserve the red thermometer, thought-bubble outline, question card, reader, desk, chair, monitor and white background unchanged. Hold the fragmented end state.”  
**CHARACTER COUNT:** 312 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A03 uses `REPLACEMENT DRAWING` in ROI X 28-76 Y 39-52; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 04.542s, transition to V05. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V04 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V05 — 05.000s — Hot steaming mug added
**SHOT:** S01  
**DURATION:** 1.916 s (04.542–06.458)  
**FRAME STATE:** F01.4  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V05_0005000ms.jpg)

![V05 source frame](weird_worrying_forensics/keyframes/V05_0005000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a steaming outlined mug appears at the right of the shattered-teeth bubble, balancing the red thermometer at left. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A steaming outlined mug appears at the right of the shattered-teeth bubble, balancing the red thermometer at left.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…upon drinking a hot cup of coffee?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Completes the cold-versus-hot causal diagram and starts the only organic loop.  
**MOTION CUE:** add mug; steam line begins a small hand-drawn loop.  
**FUNCTION:** Completes the cold-versus-hot causal diagram and starts the only organic loop.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add mug; steam line begins a small hand-drawn loop. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Completes the cold-versus-hot causal diagram and starts the only organic loop. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A steaming outlined mug appears at the right of the shattered-teeth bubble, balancing the red thermometer at left.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** shattered teeth.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** thermometer X 10–20/Y 38–64; fragments X 26–72/Y 39–54; mug X 73–90/Y 48–62; steam X 76–89/Y 39–49. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** shattered teeth → red thermometer → steaming mug.
### 7. ATTENTION ORDER
**FIRST LOOK:** shattered teeth. **SECOND/THIRD:** red thermometer → steaming mug. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; ANIMATED-LOOP. **BASE:** V04. **CHANGES:** add mug; steam line begins a small hand-drawn loop.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank panel, reader stage, scalloped bubble, shattered teeth and red thermometer; add a small outlined mug at the bubble’s lower-right and two or three short curling steam strokes above it. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V05. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.4. **SHOT:** S01. **MEASURED RANGE:** 04.542–06.458. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V04 → V05/F01.4 → V06. The transition into this state is add mug; steam line begins a small hand-drawn loop; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A04 (additive reveal; mug and first steam drawing; 4.542–4.542 s), A05 (looping line animation; steam strokes; 4.542–8.917 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A04:** Introduces the hot-coffee trigger and establishes steam as its heat signal Direction/speed/path are limited to `mug appears at bubble right; steam rises a short distance` because the reference shows no broader motion.
**A05:** Sustains the hot-cup cue while every other explanatory object remains readable Direction/speed/path are limited to `short upward curling redraws within a narrow area; slow irregular loop` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** shattered teeth, thermometer, bubble, card and reader; mug body, teeth, thermometer, bubble, card, reader/furniture except A06 region. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A04 ALLOWED TO MOVE/CHANGE:** mug and first steam drawing. **LOCKED:** shattered teeth, thermometer, bubble, card and reader. **OTHER ACTIVE:** A05 begins. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A05 ALLOWED TO MOVE/CHANGE:** steam strokes. **LOCKED:** mug body, teeth, thermometer, bubble, card, reader/furniture except A06 region. **OTHER ACTIVE:** A06 after 6.458. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
### 20. MOTION COUPLING CLASSIFICATION
A04: SIMULTANEOUS COUPLED—mug and first steam drawing is isolated from every unrelated anchor; A05: PERSISTENT LOOP—steam strokes is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A04: REPLACEMENT DRAWING + LOOP SETUP; A05: REPLACEMENT DRAWINGS / hybrid. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A04: MEDIUM—exact line/text registration favors the named deterministic method; A05: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A04:** isolate `X 70-91 Y 43-62` over the fixed V04/F01.3 base; generate/change only mug and first steam drawing; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A05:** isolate `X 76-90 Y 37-49` over the fixed V05/F01.4 base; generate/change only steam strokes; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A04 SOURCE FRAME STATE:** V04/F01.3. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V04_0004000ms.jpg). If regeneration is required, use the full standalone prompt in card V04, then apply that card’s exact text overlays before/after motion as appropriate.
**A05 SOURCE FRAME STATE:** V05/F01.4. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V05_0005000ms.jpg). If regeneration is required, use the full standalone prompt in card V05, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A04
**SOURCE STATE:** V04/F01.3  
**TARGET STATE:** V05/F01.4  
**TIMESTAMP:** 04.542–04.542  
**MOTION TYPE/HERO:** additive reveal / mug and first steam drawing  
**DIRECTION, SPEED, PATH:** mug appears at bubble right; steam rises a short distance  
**CAMERA:** locked  
**STATIC ANCHORS:** shattered teeth, thermometer, bubble, card and reader  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add only the outlined hot mug at the lower-right of the thought bubble and its first short steam strokes rising upward. Preserve the shattered teeth, red thermometer, bubble border, card, reader and furniture. Keep the mug fixed at the reference size and location and hold the first steam state.”  
**CHARACTER COUNT:** 310 / 500  
**STATUS:** PASS
#### ANIMATION A05
**SOURCE STATE:** V05/F01.4  
**TARGET STATE:** V05/F01.4  
**TIMESTAMP:** 04.542–08.917  
**MOTION TYPE/HERO:** looping line animation / steam strokes  
**DIRECTION, SPEED, PATH:** short upward curling redraws within a narrow area; slow irregular loop  
**CAMERA:** locked  
**STATIC ANCHORS:** mug body, teeth, thermometer, bubble, card, reader/furniture except A06 region  
**CONFIDENCE:** MEDIUM for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Animate only the two or three black steam strokes above the mug as a subtle hand-drawn upward curl loop within the same narrow region. Keep the mug, shattered teeth, red thermometer, bubble, question card and all lower furniture fixed; after the reader-pose replacement, preserve that pose too.”  
**CHARACTER COUNT:** 309 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A04 uses `REPLACEMENT DRAWING + LOOP SETUP` in ROI X 70-91 Y 43-62; lock/matte everything listed as static. A05 uses `REPLACEMENT DRAWINGS / hybrid` in ROI X 76-90 Y 37-49; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 06.458s, transition to V06. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V05 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V06 — 07.000s — Reader throws cup
**SHOT:** S01  
**DURATION:** 2.459 s (06.458–08.917)  
**FRAME STATE:** F01.5  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V06_0007000ms.jpg)

![V06 source frame](weird_worrying_forensics/keyframes/V06_0007000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the thought bubble remains while the reader changes to a startled throwing pose and a small cup hangs airborne left of the monitor. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The thought bubble remains while the reader changes to a startled throwing pose and a small cup hangs airborne left of the monitor.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Thank you, Shelby, for my new recurring nightmare.’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Turns the narrator’s recurring-nightmare line into a reaction gag.  
**MOTION CUE:** replace lower character pose and add airborne cup while bubble steam persists.  
**FUNCTION:** Turns the narrator’s recurring-nightmare line into a reaction gag.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace lower character pose and add airborne cup while bubble steam persists. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Turns the narrator’s recurring-nightmare line into a reaction gag. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The thought bubble remains while the reader changes to a startled throwing pose and a small cup hangs airborne left of the monitor.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** airborne cup/reader gesture.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** airborne cup X 8–16/Y 71–78; reader/desk X 18–66/Y 70–95; bubble X 6–94/Y 30–69. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** airborne cup/reader gesture → shattered-teeth diagram → card.
### 7. ATTENTION ORDER
**FIRST LOOK:** airborne cup/reader gesture. **SECOND/THIRD:** shattered-teeth diagram → card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE-WITH-LOOP. **BASE:** V05. **CHANGES:** replace lower character pose and add airborne cup while bubble steam persists.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank panel and full thought-bubble diagram with red thermometer, fragments and steaming mug; below, draw the seated faceless reader in a startled one-arm toss pose with a tiny tilted cup airborne left of the monitor. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to get your teeth to such a cold temperature that they would shatter upon drinking a hot cup of coffee? — Shelby Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V06. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F01.5. **SHOT:** S01. **MEASURED RANGE:** 06.458–08.917. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V05 → V06/F01.5 → V07. The transition into this state is replace lower character pose and add airborne cup while bubble steam persists; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A06 (replacement drawing / reaction pose; reader and airborne cup; 6.458–6.458 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A06:** Turns the narrator’s nightmare reaction into a comic discard gesture Direction/speed/path are limited to `reader arm/torso switch; cup appears left of monitor, tilted outward` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** question card, thought bubble, thermometer, shattered teeth, hot mug, desk and chair. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A06 ALLOWED TO MOVE/CHANGE:** reader and airborne cup. **LOCKED:** question card, thought bubble, thermometer, shattered teeth, hot mug, desk and chair. **OTHER ACTIVE:** A05 steam loop. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
### 20. MOTION COUPLING CLASSIFICATION
A06: SIMULTANEOUS INDEPENDENT—reader and airborne cup is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A06: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A06: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A06:** isolate `X 8-59 Y 68-94` over the fixed V05/F01.4 base; generate/change only reader and airborne cup; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A06 SOURCE FRAME STATE:** V05/F01.4. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V05_0005000ms.jpg). If regeneration is required, use the full standalone prompt in card V05, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A06
**SOURCE STATE:** V05/F01.4  
**TARGET STATE:** V06/F01.5  
**TIMESTAMP:** 06.458–06.458  
**MOTION TYPE/HERO:** replacement drawing / reaction pose / reader and airborne cup  
**DIRECTION, SPEED, PATH:** reader arm/torso switch; cup appears left of monitor, tilted outward  
**CAMERA:** locked  
**STATIC ANCHORS:** question card, thought bubble, thermometer, shattered teeth, hot mug, desk and chair  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. In one abrupt hand-drawn replacement, change only the seated reader into the observed startled/tossing pose and place the small tilted cup airborne left of the monitor. Preserve the question card, thought bubble, shattered teeth, thermometer, hot mug, desk, chair and white field; steam may continue independently.”  
**CHARACTER COUNT:** 329 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A06 uses `REPLACEMENT DRAWING` in ROI X 8-59 Y 68-94; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 08.917s, transition to V07. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V06 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V07 — 09.000s — Gray-noise transition
**SHOT:** TR01  
**DURATION:** 0.208 s (08.917–09.125)  
**FRAME STATE:** FTR01  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V07_0009000ms.jpg)

![V07 source frame](weird_worrying_forensics/keyframes/V07_0009000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the entire 9:16 frame is covered by fine neutral-gray television noise; no characters, text or drawing remains. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The entire 9:16 frame is covered by fine neutral-gray television noise; no characters, text or drawing remains.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Narration pivots into ‘Here are some more weird and worrying questions…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Provide the recurring 0.21-second abrasive separator.  
**MOTION CUE:** hard replace scene with changing gray noise.  
**FUNCTION:** Provide the recurring 0.21-second abrasive separator.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace scene with changing gray noise. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Provide the recurring 0.21-second abrasive separator. Information value: TRANSITIONAL. Removing this state would erase the section boundary.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field replaced by gray noise.  
**MAIN SUBJECT:** The entire 9:16 frame is covered by fine neutral-gray television noise; no characters, text or drawing remains.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** uniform texture with no intentional hierarchy.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** noise X 0–100/Y 0–100. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** uniform texture with no intentional hierarchy.
### 7. ATTENTION ORDER
**FIRST LOOK:** uniform texture with no intentional hierarchy. **SECOND/THIRD:** none. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** UNIFORM.
### 8. IMAGE REUSE STATUS
**STATUS:** EXACT REUSE of E03 noise design with a new random frame; ANIMATED-TRANSITION. **BASE:** V06. **CHANGES:** hard replace scene with changing gray noise.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; fill the entire vertical frame with fine evenly distributed neutral-gray television-noise grain, with no recognizable objects, borders, lettering or directional pattern. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V07. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** FTR01. **SHOT:** TR01. **MEASURED RANGE:** 08.917–09.125. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V06 → V07/FTR01 → V08. The transition into this state is hard replace scene with changing gray noise; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A07 (hard replacement; full frame; 8.917–8.917 s), A08 (procedural texture loop; gray noise; 8.917–9.125 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A07:** Resets attention and separates the Shelby beat from the mirror interruption Direction/speed/path are limited to `instant cut from drawing to gray noise` because the reference shows no broader motion.
**A08:** Creates a brief abrasive separator rather than a spatial transition Direction/speed/path are limited to `fine random monochrome pixels change every frame` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** no drawing elements persist; full-frame luminance range and 9:16 boundary. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A07 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** no drawing elements persist. **OTHER ACTIVE:** A08 starts. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A08 ALLOWED TO MOVE/CHANGE:** gray noise. **LOCKED:** full-frame luminance range and 9:16 boundary. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A07: STATE REPLACEMENT—full frame is isolated from every unrelated anchor; A08: PERSISTENT LOOP—gray noise is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A07: EDITOR HARD CUT; A08: EDITOR PROCEDURAL NOISE. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A07: LOW—exact line/text registration favors the named deterministic method; A08: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A07:** isolate `full frame` over the fixed V06/F01.5 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A08:** isolate `full frame` over the fixed V07/FTR01 base; generate/change only gray noise; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A07 SOURCE FRAME STATE:** V06/F01.5. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V06_0007000ms.jpg). If regeneration is required, use the full standalone prompt in card V06, then apply that card’s exact text overlays before/after motion as appropriate.
**A08 SOURCE FRAME STATE:** V07/FTR01. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V07_0009000ms.jpg). If regeneration is required, use the full standalone prompt in card V07, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A07
**SOURCE STATE:** V06/F01.5  
**TARGET STATE:** V07/FTR01  
**TIMESTAMP:** 08.917–08.917  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut from drawing to gray noise  
**CAMERA:** locked  
**STATIC ANCHORS:** no drawing elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from the completed Shelby composition to a full-frame neutral gray television-noise plate. Do not carry the question card, thought bubble, reader or furniture into the transition. Keep the camera/frame fixed at 9:16.”  
**CHARACTER COUNT:** 225 / 500  
**STATUS:** PASS
#### ANIMATION A08
**SOURCE STATE:** V07/FTR01  
**TARGET STATE:** V07/FTR01  
**TIMESTAMP:** 08.917–09.125  
**MOTION TYPE/HERO:** procedural texture loop / gray noise  
**DIRECTION, SPEED, PATH:** fine random monochrome pixels change every frame  
**CAMERA:** locked  
**STATIC ANCHORS:** full-frame luminance range and 9:16 boundary  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked frame. Animate only fine neutral-gray television noise across the full 9:16 image, with small random pixel changes and no shapes, text or camera motion. Maintain even mid-gray density for the observed 0.21-second bridge, then stop on the cut.”  
**CHARACTER COUNT:** 249 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A07 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. A08 uses `EDITOR PROCEDURAL NOISE` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 09.125s, transition to V08. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V07 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V08 — 09.500s — Bare stage reset
**SHOT:** S02  
**DURATION:** 0.750 s (09.125–09.875)  
**FRAME STATE:** F02.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V08_0009500ms.jpg)

![V08 source frame](weird_worrying_forensics/keyframes/V08_0009500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a clean white stage returns with only the seated reader, desk, tilted monitor and chair low in frame; the upper two-thirds are empty. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A clean white stage returns with only the seated reader, desk, tilted monitor and chair low in frame; the upper two-thirds are empty.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Here are some more weird and worrying questions from the What If inbox.’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Create a breath before the mirror-question pattern interrupt.  
**MOTION CUE:** hard exit from noise to seated reader without question card.  
**FUNCTION:** Create a breath before the mirror-question pattern interrupt.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard exit from noise to seated reader without question card. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Create a breath before the mirror-question pattern interrupt. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A clean white stage returns with only the seated reader, desk, tilted monitor and chair low in frame; the upper two-thirds are empty.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** small reader cluster.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** reader/desk cluster X 18–66/Y 72–95; negative space X 0–100/Y 0–71. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** small reader cluster → large empty field.
### 7. ATTENTION ORDER
**FIRST LOOK:** small reader cluster. **SECOND/THIRD:** large empty field. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V07. **CHANGES:** hard exit from noise to seated reader without question card.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place only the recurring faceless seated reader and compact outlined desk, tilted monitor and office chair low in the lower-left/center of a pure white vertical frame; leave the entire upper two-thirds empty. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V08. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F02.0. **SHOT:** S02. **MEASURED RANGE:** 09.125–09.875. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V07 → V08/F02.0 → V09. The transition into this state is hard exit from noise to seated reader without question card; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A09 (hard replacement; full frame; 9.125–9.125 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A09:** Returns to the inbox stage stripped of the question card for a pattern break Direction/speed/path are limited to `instant cut from noise to bare reader stage` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** reader, desk, chair and monitor form new stable anchors. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A09 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** reader, desk, chair and monitor form new stable anchors. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A09: STATE REPLACEMENT—full frame is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A09: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A09: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A09:** isolate `full frame` over the fixed V07/FTR01 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A09 SOURCE FRAME STATE:** V07/FTR01. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V07_0009000ms.jpg). If regeneration is required, use the full standalone prompt in card V07, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A09
**SOURCE STATE:** V07/FTR01  
**TARGET STATE:** V08/F02.0  
**TIMESTAMP:** 09.125–09.125  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut from noise to bare reader stage  
**CAMERA:** locked  
**STATIC ANCHORS:** reader, desk, chair and monitor form new stable anchors  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from full-frame gray noise to the clean white stage with only the seated reader, desk, tilted monitor and chair low in frame. Preserve the exact lower cluster scale and position from the reference. No question card or thought bubble appears.”  
**CHARACTER COUNT:** 250 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A09 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 09.875s, transition to V09. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V08 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V09 — 10.500s — Mirror-harm question + visitor
**SHOT:** S02  
**DURATION:** 2.333 s (09.875–12.208)  
**FRAME STATE:** F02.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V09_0010500ms.jpg)

![V09 source frame](weird_worrying_forensics/keyframes/V09_0010500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see large hand-lettered mirror-harm text fills the upper middle; its curved tail points to a tall black-haired visitor at right holding an oval mirror beside the seated reader. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** Large hand-lettered mirror-harm text fills the upper middle; its curved tail points to a tall black-haired visitor at right holding an oval mirror beside the seated reader.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Same inbox-reset narration; the mirror question itself is visible but not spoken in full.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Visually literalize the title’s ‘worrying’ half without voicing another full question.  
**MOTION CUE:** add hand-lettered question, speech tail and tall black-haired visitor.  
**FUNCTION:** Visually literalize the title’s ‘worrying’ half without voicing another full question.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add hand-lettered question, speech tail and tall black-haired visitor. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Visually literalize the title’s ‘worrying’ half without voicing another full question. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** Large hand-lettered mirror-harm text fills the upper middle; its curved tail points to a tall black-haired visitor at right holding an oval mirror beside the seated reader.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** large question zone.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** lettering zone X 9–82/Y 19–52; visitor X 58–90/Y 55–94; seated reader/desk X 18–61/Y 68–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** large question zone → black hair block/visitor → seated reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** large question zone. **SECOND/THIRD:** black hair block/visitor → seated reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** NEW BASE; STABLE. **BASE:** V08. **CHANGES:** add hand-lettered question, speech tail and tall black-haired visitor.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the lower seated reader/desk cluster; add a tall faceless visitor at lower-right with a solid black rectangular hair/hat block and an oval hand mirror, plus a curved speech-tail line into a large blank lettering zone above. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** HOW MANY MIRRORS REFLECTING (SUN)LIGHT WOULD IT TAKE TO KILL, OR AT LEAST, INJURE SOMEONE? Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V09. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F02.1. **SHOT:** S02. **MEASURED RANGE:** 09.875–12.208. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V08 → V09/F02.1 → V10. The transition into this state is add hand-lettered question, speech tail and tall black-haired visitor; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A10 (additive state replacement; mirror question and visitor; 9.875–9.875 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A10:** Embodies “weird and worrying” with a threatening literal question and second character Direction/speed/path are limited to `full lettering/visitor appear together; no observed travel` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** seated reader, desk, chair, monitor and white field. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A10 ALLOWED TO MOVE/CHANGE:** mirror question and visitor. **LOCKED:** seated reader, desk, chair, monitor and white field. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A10: SIMULTANEOUS COUPLED—mirror question and visitor is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A10: REPLACEMENT DRAWING + deterministic text overlay. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A10: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A10:** isolate `X 8-89 Y 30-91` over the fixed V08/F02.0 base; generate/change only mirror question and visitor; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A10 SOURCE FRAME STATE:** V08/F02.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V08_0009500ms.jpg). If regeneration is required, use the full standalone prompt in card V08, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A10
**SOURCE STATE:** V08/F02.0  
**TARGET STATE:** V09/F02.1  
**TIMESTAMP:** 09.875–09.875  
**MOTION TYPE/HERO:** additive state replacement / mirror question and visitor  
**DIRECTION, SPEED, PATH:** full lettering/visitor appear together; no observed travel  
**CAMERA:** locked  
**STATIC ANCHORS:** seated reader, desk, chair, monitor and white field  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the exact hand-lettered mirror question above the reader, its curved speech tail, and the tall black-haired visitor at right holding a mirror. Reveal them in one clean replacement beat. Preserve the seated reader, desk, monitor, chair, scale, positions and white negative space exactly.”  
**CHARACTER COUNT:** 305 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A10 uses `REPLACEMENT DRAWING + deterministic text overlay` in ROI X 8-89 Y 30-91; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 12.208s, transition to V10. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V09 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V10 — 12.500s — Jeff question card
**SHOT:** S03  
**DURATION:** 0.875 s (12.208–13.083)  
**FRAME STATE:** F03.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V10_0012500ms.jpg)

![V10 source frame](weird_worrying_forensics/keyframes/V10_0012500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the Jeff question replaces the mirror scene; the gray card returns at top and the recurring reader stage sits low on white. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The Jeff question replaces the mirror scene; the gray card returns at top and the recurring reader stage sits low on white.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Jeff asks, given humanity’s current knowledge and abilities…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Open Jeff’s star-building beat on the established inbox grammar.  
**MOTION CUE:** hard replace question and remove visitor/text.  
**FUNCTION:** Open Jeff’s star-building beat on the established inbox grammar.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace question and remove visitor/text. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Open Jeff’s star-building beat on the established inbox grammar. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The Jeff question replaces the mirror scene; the gray card returns at top and the recurring reader stage sits low on white.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** question panel.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** card X 5–95/Y 6–29; reader/desk X 18–66/Y 71–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** question panel. **SECOND/THIRD:** reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V09. **CHANGES:** hard replace question and remove visitor/text.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place a blank light-gray rounded question panel across the upper frame and the recurring faceless reader seated with device beside the compact desk, tilted monitor and chair low below; leave the central region white. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V10. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.0. **SHOT:** S03. **MEASURED RANGE:** 12.208–13.083. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V09 → V10/F03.0 → V11. The transition into this state is hard replace question and remove visitor/text; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A11 (hard cut / state replacement; full composition; 12.208–12.208 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A11:** Ends the standalone mirror gag and begins Jeff’s submitted question Direction/speed/path are limited to `mirror scene switches to Jeff card and base reader` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** reader-stage geometry reappears; no mirror elements persist. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A11 ALLOWED TO MOVE/CHANGE:** full composition. **LOCKED:** reader-stage geometry reappears; no mirror elements persist. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A11: STATE REPLACEMENT—full composition is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A11: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A11: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A11:** isolate `full frame` over the fixed V09/F02.1 base; generate/change only full composition; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A11 SOURCE FRAME STATE:** V09/F02.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V09_0010500ms.jpg). If regeneration is required, use the full standalone prompt in card V09, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A11
**SOURCE STATE:** V09/F02.1  
**TARGET STATE:** V10/F03.0  
**TIMESTAMP:** 12.208–12.208  
**MOTION TYPE/HERO:** hard cut / state replacement / full composition  
**DIRECTION, SPEED, PATH:** mirror scene switches to Jeff card and base reader  
**CAMERA:** locked  
**STATIC ANCHORS:** reader-stage geometry reappears; no mirror elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut to the Jeff question-card base: gray rounded card at top and seated reader/desk/chair low in the white 9:16 frame. Remove all mirror-question lettering, visitor and mirror. Keep the recurring reader-stage proportions registered to the reference.”  
**CHARACTER COUNT:** 254 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A11 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 13.083s, transition to V11. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V10 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V11 — 14.000s — Star-building machine
**SHOT:** S03  
**DURATION:** 1.875 s (13.083–14.958)  
**FRAME STATE:** F03.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V11_0014000ms.jpg)

![V11 source frame](weird_worrying_forensics/keyframes/V11_0014000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a scalloped bubble appears between card and reader, containing a shaded torus/cylindrical machine aimed right and two tiny figures near its lower-right. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A scalloped bubble appears between card and reader, containing a shaded torus/cylindrical machine aimed right and two tiny figures near its lower-right.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…is it possible to build a new star?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Translate ‘build a star’ into a legible engineering mechanism.  
**MOTION CUE:** add thought bubble, cylindrical/torus apparatus and two tiny figures.  
**FUNCTION:** Translate ‘build a star’ into a legible engineering mechanism.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add thought bubble, cylindrical/torus apparatus and two tiny figures. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Translate ‘build a star’ into a legible engineering mechanism. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A scalloped bubble appears between card and reader, containing a shaded torus/cylindrical machine aimed right and two tiny figures near its lower-right.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** apparatus.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** bubble X 6–94/Y 30–69; apparatus X 25–69/Y 34–58; tiny figures X 78–89/Y 49–60. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** apparatus → question panel → tiny witnesses.
### 7. ATTENTION ORDER
**FIRST LOOK:** apparatus. **SECOND/THIRD:** question panel → tiny witnesses. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V10. **CHANGES:** add thought bubble, cylindrical/torus apparatus and two tiny figures.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Jeff panel and lower reader stage; add a large scalloped thought bubble containing a detailed hand-drawn shaded torus and cylindrical apparatus aimed horizontally right, with two tiny stick figures near the lower-right. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V11. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.1. **SHOT:** S03. **MEASURED RANGE:** 13.083–14.958. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V10 → V11/F03.1 → V12. The transition into this state is add thought bubble, cylindrical/torus apparatus and two tiny figures; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A12 (additive reveal; thought bubble and star-building apparatus; 13.083–13.083 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A12:** Converts the abstract “build a new star” question into a machine concept Direction/speed/path are limited to `instant full bubble/apparatus appearance` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** Jeff card, reader, desk, chair and monitor. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A12 ALLOWED TO MOVE/CHANGE:** thought bubble and star-building apparatus. **LOCKED:** Jeff card, reader, desk, chair and monitor. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A12: STATE REPLACEMENT—thought bubble and star-building apparatus is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A12: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A12: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A12:** isolate `X 6-94 Y 28-69` over the fixed V10/F03.0 base; generate/change only thought bubble and star-building apparatus; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A12 SOURCE FRAME STATE:** V10/F03.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V10_0012500ms.jpg). If regeneration is required, use the full standalone prompt in card V10, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A12
**SOURCE STATE:** V10/F03.0  
**TARGET STATE:** V11/F03.1  
**TIMESTAMP:** 13.083–13.083  
**MOTION TYPE/HERO:** additive reveal / thought bubble and star-building apparatus  
**DIRECTION, SPEED, PATH:** instant full bubble/apparatus appearance  
**CAMERA:** locked  
**STATIC ANCHORS:** Jeff card, reader, desk, chair and monitor  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the observed scalloped thought bubble containing the large shaded torus/cylindrical apparatus aimed right and two tiny figures near its lower-right. Preserve the Jeff card, seated reader, desk, chair, monitor, frame scale and white background. Hold the completed drawing.”  
**CHARACTER COUNT:** 290 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A12 uses `REPLACEMENT DRAWING` in ROI X 6-94 Y 28-69; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 14.958s, transition to V12. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V11 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V12 — 15.500s — Machine creates star
**SHOT:** S03  
**DURATION:** 2.417 s (14.958–17.375)  
**FRAME STATE:** F03.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V12_0015500ms.jpg)

![V12 source frame](weird_worrying_forensics/keyframes/V12_0015500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a small radiant star and short beam now sit to the right of the machine; the two tiny witnesses and every outer anchor stay fixed. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A small radiant star and short beam now sit to the right of the machine; the two tiny witnesses and every outer anchor stay fixed.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Jeff’s star question completes as the machine’s output appears.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Deliver the literal star result before the joke pivots to intent.  
**MOTION CUE:** add radiant star and connecting beam at bubble right.  
**FUNCTION:** Deliver the literal star result before the joke pivots to intent.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add radiant star and connecting beam at bubble right. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Deliver the literal star result before the joke pivots to intent. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A small radiant star and short beam now sit to the right of the machine; the two tiny witnesses and every outer anchor stay fixed.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** radiant star.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** apparatus X 25–69/Y 34–58; beam X 62–75/Y 45–48; star X 72–84/Y 38–53; tiny figures X 79–89/Y 50–60. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** radiant star → apparatus → tiny figures.
### 7. ATTENTION ORDER
**FIRST LOOK:** radiant star. **SECOND/THIRD:** apparatus → tiny figures. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V11. **CHANGES:** add radiant star and connecting beam at bubble right.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Jeff panel, reader stage and star-building bubble; add a small bright white circular star with irregular black radial strokes at bubble right and a short thin horizontal beam from the apparatus. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V12. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.2. **SHOT:** S03. **MEASURED RANGE:** 14.958–17.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V11 → V12/F03.2 → V13. The transition into this state is add radiant star and connecting beam at bubble right; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A13 (additive reveal; radiant star and beam; 14.958–14.958 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A13:** Shows the machine’s output and supplies the promised “new star” payoff Direction/speed/path are limited to `star appears to apparatus right; short beam connects horizontally` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** apparatus, tiny figures, bubble, card and reader. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A13 ALLOWED TO MOVE/CHANGE:** radiant star and beam. **LOCKED:** apparatus, tiny figures, bubble, card and reader. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A13: SEQUENTIAL—radiant star and beam is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A13: VECTOR/REPLACEMENT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A13: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A13:** isolate `X 61-84 Y 40-56` over the fixed V11/F03.1 base; generate/change only radiant star and beam; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A13 SOURCE FRAME STATE:** V11/F03.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V11_0014000ms.jpg). If regeneration is required, use the full standalone prompt in card V11, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A13
**SOURCE STATE:** V11/F03.1  
**TARGET STATE:** V12/F03.2  
**TIMESTAMP:** 14.958–14.958  
**MOTION TYPE/HERO:** additive reveal / radiant star and beam  
**DIRECTION, SPEED, PATH:** star appears to apparatus right; short beam connects horizontally  
**CAMERA:** locked  
**STATIC ANCHORS:** apparatus, tiny figures, bubble, card and reader  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add only the small radiant star at the right end of the apparatus and the short horizontal beam joining them. Match the observed size and radial strokes. Keep the machine, two tiny figures, bubble, Jeff card, seated reader, furniture and white background completely fixed. Hold.”  
**CHARACTER COUNT:** 293 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A13 uses `VECTOR/REPLACEMENT OVERLAY` in ROI X 61-84 Y 40-56; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 17.375s, transition to V13. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V12 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V13 — 18.000s — Lone figure in thought bubble
**SHOT:** S03  
**DURATION:** 1.750 s (17.375–19.125)  
**FRAME STATE:** F03.3  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V13_0018000ms.jpg)

![V13 source frame](weird_worrying_forensics/keyframes/V13_0018000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the machine tableau is replaced by one large faceless stick figure standing slightly left of center inside the same thought bubble. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The machine tableau is replaced by one large faceless stick figure standing slightly left of center inside the same thought bubble.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Jeff, is there a reason you need to know this?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Change from feasibility visualization to suspicion about the submitter.  
**MOTION CUE:** replace apparatus scene with large stick figure.  
**FUNCTION:** Change from feasibility visualization to suspicion about the submitter.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace apparatus scene with large stick figure. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Change from feasibility visualization to suspicion about the submitter. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The machine tableau is replaced by one large faceless stick figure standing slightly left of center inside the same thought bubble.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** large thought figure.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** figure X 28–50/Y 34–65; bubble X 6–94/Y 30–69; card/reader unchanged. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** large thought figure → question card → seated reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** large thought figure. **SECOND/THIRD:** question card → seated reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V12. **CHANGES:** replace apparatus scene with large stick figure.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Jeff panel, lower reader and existing scalloped thought bubble; replace all machinery with one large simple faceless standing stick figure slightly left of center inside the bubble. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V13. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.3. **SHOT:** S03. **MEASURED RANGE:** 17.375–19.125. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V12 → V13/F03.3 → V14. The transition into this state is replace apparatus scene with large stick figure; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A14 (replacement drawing; thought-bubble content; 17.375–17.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A14:** Shifts from literal feasibility to suspicion about Jeff’s personal motive Direction/speed/path are limited to `apparatus/star tableau switches to one large standing figure` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** bubble border/tail, Jeff card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A14 ALLOWED TO MOVE/CHANGE:** thought-bubble content. **LOCKED:** bubble border/tail, Jeff card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A14: STATE REPLACEMENT—thought-bubble content is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A14: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A14: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A14:** isolate `X 6-94 Y 28-69` over the fixed V12/F03.2 base; generate/change only thought-bubble content; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A14 SOURCE FRAME STATE:** V12/F03.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V12_0015500ms.jpg). If regeneration is required, use the full standalone prompt in card V12, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A14
**SOURCE STATE:** V12/F03.2  
**TARGET STATE:** V13/F03.3  
**TIMESTAMP:** 17.375–17.375  
**MOTION TYPE/HERO:** replacement drawing / thought-bubble content  
**DIRECTION, SPEED, PATH:** apparatus/star tableau switches to one large standing figure  
**CAMERA:** locked  
**STATIC ANCHORS:** bubble border/tail, Jeff card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace only the star-machine tableau inside the existing thought bubble with the observed large faceless stick figure near center-left. Preserve the bubble outline and tail, Jeff question card, seated reader, desk, chair, monitor and white background exactly. Hold the new figure state.”  
**CHARACTER COUNT:** 302 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A14 uses `REPLACEMENT DRAWING` in ROI X 6-94 Y 28-69; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 19.125s, transition to V14. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V13 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V14 — 19.500s — Maybe reply
**SHOT:** S03  
**DURATION:** 1.500 s (19.125–20.625)  
**FRAME STATE:** F03.4  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V14_0019500ms.jpg)

![V14 source frame](weird_worrying_forensics/keyframes/V14_0019500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the lone thought figure remains and a curved speech tail ends at the hand-lettered word “…MAYBE” on its right. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The lone thought figure remains and a curved speech tail ends at the hand-lettered word “…MAYBE” on its right.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘What are you planning?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Provide a dry, deliberately weak denial.  
**MOTION CUE:** add speech tail and hand-lettered …MAYBE.  
**FUNCTION:** Provide a dry, deliberately weak denial.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add speech tail and hand-lettered …MAYBE. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Provide a dry, deliberately weak denial. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The lone thought figure remains and a curved speech tail ends at the hand-lettered word “…MAYBE” on its right.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** response zone.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** figure X 28–50/Y 34–65; response zone X 46–78/Y 41–55. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** response zone → figure → Jeff card.
### 7. ATTENTION ORDER
**FIRST LOOK:** response zone. **SECOND/THIRD:** figure → Jeff card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V13. **CHANGES:** add speech tail and hand-lettered …MAYBE.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Jeff panel, reader, bubble and large standing thought figure; add only a curved speech-tail line toward a reserved blank response zone on the figure’s right. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff | …MAYBE Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V14. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.4. **SHOT:** S03. **MEASURED RANGE:** 19.125–20.625. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V13 → V14/F03.4 → V15. The transition into this state is add speech tail and hand-lettered …MAYBE; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A15 (text reveal; …MAYBE and speech tail; 19.125–19.125 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A15:** Answers the narrator’s suspicion with a dry non-denial Direction/speed/path are limited to `instant lettering appears to figure right` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** thought figure, bubble, card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A15 ALLOWED TO MOVE/CHANGE:** …MAYBE and speech tail. **LOCKED:** thought figure, bubble, card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A15: SEQUENTIAL—…MAYBE and speech tail is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A15: DETERMINISTIC TEXT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A15: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A15:** isolate `X 41-78 Y 43-58` over the fixed V13/F03.3 base; generate/change only …MAYBE and speech tail; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A15 SOURCE FRAME STATE:** V13/F03.3. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V13_0018000ms.jpg). If regeneration is required, use the full standalone prompt in card V13, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A15
**SOURCE STATE:** V13/F03.3  
**TARGET STATE:** V14/F03.4  
**TIMESTAMP:** 19.125–19.125  
**MOTION TYPE/HERO:** text reveal / …MAYBE and speech tail  
**DIRECTION, SPEED, PATH:** instant lettering appears to figure right  
**CAMERA:** locked  
**STATIC ANCHORS:** thought figure, bubble, card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Reveal only the exact hand-lettered text “…MAYBE” to the right of the thought-bubble figure with its short curved speech tail. Keep the figure, bubble contour, Jeff card, seated reader, desk, chair, monitor and white background fixed. Hold the text.”  
**CHARACTER COUNT:** 264 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A15 uses `DETERMINISTIC TEXT OVERLAY` in ROI X 41-78 Y 43-58; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 20.625s, transition to V15. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V14 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V15 — 20.750s — Sun Obliterator
**SHOT:** S03  
**DURATION:** 0.542 s (20.625–21.167)  
**FRAME STATE:** F03.5  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V15_0020750ms.jpg)

![V15 source frame](weird_worrying_forensics/keyframes/V15_0020750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the thought figure and reply are replaced by an oversized horizontal weapon drawing whose barrel extends right; its body carries the label SUN OBLITERATOR. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The thought figure and reply are replaced by an oversized horizontal weapon drawing whose barrel extends right; its body carries the label SUN OBLITERATOR.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** The suspicious question finishes on the weapon punch line.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Escalate Jeff’s ambiguous motive into an absurd weaponized punch line.  
**MOTION CUE:** replace lone figure with labeled oversized weapon.  
**FUNCTION:** Escalate Jeff’s ambiguous motive into an absurd weaponized punch line.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace lone figure with labeled oversized weapon. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Escalate Jeff’s ambiguous motive into an absurd weaponized punch line. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The thought figure and reply are replaced by an oversized horizontal weapon drawing whose barrel extends right; its body carries the label SUN OBLITERATOR.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** weapon silhouette.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** weapon X 7–91/Y 39–59; label plate X 10–49/Y 43–52; bubble/card/reader unchanged. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** weapon silhouette → label plate → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** weapon silhouette. **SECOND/THIRD:** label plate → reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V14. **CHANGES:** replace lone figure with labeled oversized weapon.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Jeff panel, lower reader and scalloped bubble; replace the bubble interior with an oversized absurd horizontal cannon-like device spanning most of the bubble, with a long segmented barrel and a large blank label plate on its body. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Given humanity’s current knowledge and capabilities, is it possible to build a new star? — Jeff | SUN OBLITERATOR Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V15. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F03.5. **SHOT:** S03. **MEASURED RANGE:** 20.625–21.167. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V14 → V15/F03.5 → V16. The transition into this state is replace lone figure with labeled oversized weapon; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A16 (replacement drawing; Sun Obliterator weapon; 20.625–20.625 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A16:** Escalates ambiguous intent into an absurd weaponized punch line Direction/speed/path are limited to `figure and MAYBE switch to labeled horizontal weapon` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** bubble border/tail, Jeff card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A16 ALLOWED TO MOVE/CHANGE:** Sun Obliterator weapon. **LOCKED:** bubble border/tail, Jeff card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A16: STATE REPLACEMENT—Sun Obliterator weapon is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A16: REPLACEMENT DRAWING + deterministic label. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A16: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A16:** isolate `X 7-91 Y 37-60` over the fixed V14/F03.4 base; generate/change only Sun Obliterator weapon; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A16 SOURCE FRAME STATE:** V14/F03.4. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V14_0019500ms.jpg). If regeneration is required, use the full standalone prompt in card V14, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A16
**SOURCE STATE:** V14/F03.4  
**TARGET STATE:** V15/F03.5  
**TIMESTAMP:** 20.625–20.625  
**MOTION TYPE/HERO:** replacement drawing / Sun Obliterator weapon  
**DIRECTION, SPEED, PATH:** figure and MAYBE switch to labeled horizontal weapon  
**CAMERA:** locked  
**STATIC ANCHORS:** bubble border/tail, Jeff card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace only the figure-and-MAYBE content inside the thought bubble with the observed oversized horizontal device labeled “SUN OBLITERATOR.” Match its placement and footprint. Preserve the bubble border/tail, Jeff card, reader, desk, monitor, chair and white background exactly. Hold.”  
**CHARACTER COUNT:** 299 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A16 uses `REPLACEMENT DRAWING + deterministic label` in ROI X 7-91 Y 37-60; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 21.167s, transition to V16. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V15 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V16 — 21.250s — Gray-noise transition
**SHOT:** TR02  
**DURATION:** 0.208 s (21.167–21.375)  
**FRAME STATE:** FTR02  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V16_0021250ms.jpg)

![V16 source frame](weird_worrying_forensics/keyframes/V16_0021250ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see fine neutral-gray television noise fills the vertical frame with no retained Jeff elements. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** Fine neutral-gray television noise fills the vertical frame with no retained Jeff elements.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Brief transition gap before Tomasz’s question.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Reset between Jeff’s punch line and Tomasz’s question.  
**MOTION CUE:** hard replace scene with changing gray noise.  
**FUNCTION:** Reset between Jeff’s punch line and Tomasz’s question.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace scene with changing gray noise. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Reset between Jeff’s punch line and Tomasz’s question. Information value: TRANSITIONAL. Removing this state would erase the section boundary.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field replaced by gray noise.  
**MAIN SUBJECT:** Fine neutral-gray television noise fills the vertical frame with no retained Jeff elements.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** uniform texture.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** noise X 0–100/Y 0–100. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** uniform texture.
### 7. ATTENTION ORDER
**FIRST LOOK:** uniform texture. **SECOND/THIRD:** none. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** UNIFORM.
### 8. IMAGE REUSE STATUS
**STATUS:** EXACT REUSE of E03 noise design with a new random frame; ANIMATED-TRANSITION. **BASE:** V15. **CHANGES:** hard replace scene with changing gray noise.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; fill the full 9:16 canvas with even fine neutral-gray television-noise grain and no objects, lettering, borders or directional wipe. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V16. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** FTR02. **SHOT:** TR02. **MEASURED RANGE:** 21.167–21.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V15 → V16/FTR02 → V17. The transition into this state is hard replace scene with changing gray noise; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A17 (hard replacement; full frame; 21.167–21.167 s), A18 (procedural texture loop; gray noise; 21.167–21.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A17:** Separates Jeff’s weapon payoff from the next hazardous question Direction/speed/path are limited to `instant cut to gray noise` because the reference shows no broader motion.
**A18:** Provides the recurring brief reset motif Direction/speed/path are limited to `fine random monochrome pixels change every frame` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** no Jeff elements persist; full-frame luminance range and boundary. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A17 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** no Jeff elements persist. **OTHER ACTIVE:** A18 starts. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A18 ALLOWED TO MOVE/CHANGE:** gray noise. **LOCKED:** full-frame luminance range and boundary. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A17: STATE REPLACEMENT—full frame is isolated from every unrelated anchor; A18: PERSISTENT LOOP—gray noise is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A17: EDITOR HARD CUT; A18: EDITOR PROCEDURAL NOISE. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A17: LOW—exact line/text registration favors the named deterministic method; A18: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A17:** isolate `full frame` over the fixed V15/F03.5 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A18:** isolate `full frame` over the fixed V16/FTR02 base; generate/change only gray noise; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A17 SOURCE FRAME STATE:** V15/F03.5. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V15_0020750ms.jpg). If regeneration is required, use the full standalone prompt in card V15, then apply that card’s exact text overlays before/after motion as appropriate.
**A18 SOURCE FRAME STATE:** V16/FTR02. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V16_0021250ms.jpg). If regeneration is required, use the full standalone prompt in card V16, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A17
**SOURCE STATE:** V15/F03.5  
**TARGET STATE:** V16/FTR02  
**TIMESTAMP:** 21.167–21.167  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut to gray noise  
**CAMERA:** locked  
**STATIC ANCHORS:** no Jeff elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from the completed Jeff composition to a full-frame neutral gray television-noise plate. Carry no card, bubble, character or weapon into the transition. Keep the 9:16 frame locked.”  
**CHARACTER COUNT:** 189 / 500  
**STATUS:** PASS
#### ANIMATION A18
**SOURCE STATE:** V16/FTR02  
**TARGET STATE:** V16/FTR02  
**TIMESTAMP:** 21.167–21.375  
**MOTION TYPE/HERO:** procedural texture loop / gray noise  
**DIRECTION, SPEED, PATH:** fine random monochrome pixels change every frame  
**CAMERA:** locked  
**STATIC ANCHORS:** full-frame luminance range and boundary  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked frame. Animate only fine neutral-gray television noise across the full 9:16 image for the observed 0.21-second bridge. Maintain uniform mid-gray density; introduce no text, silhouettes, camera movement or directional wipe.”  
**CHARACTER COUNT:** 229 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A17 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. A18 uses `EDITOR PROCEDURAL NOISE` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 21.375s, transition to V17. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V16 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V17 — 21.750s — Tomasz question card
**SHOT:** S04  
**DURATION:** 1.000 s (21.375–22.375)  
**FRAME STATE:** F04.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V17_0021750ms.jpg)

![V17 source frame](weird_worrying_forensics/keyframes/V17_0021750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a gray Tomasz question card sits at top above the recurring seated reader, desk, monitor and chair; the middle is blank. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A gray Tomasz question card sits at top above the recurring seated reader, desk, monitor and chair; the middle is blank.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Tomasz asks, would it be possible to stop a volcano eruption…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Open the volcano/bomb submission in the same inbox coordinate system.  
**MOTION CUE:** hard exit from noise to new question card.  
**FUNCTION:** Open the volcano/bomb submission in the same inbox coordinate system.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard exit from noise to new question card. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Open the volcano/bomb submission in the same inbox coordinate system. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A gray Tomasz question card sits at top above the recurring seated reader, desk, monitor and chair; the middle is blank.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** question panel.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** card X 5–95/Y 6–29; reader/desk X 18–66/Y 71–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** question panel. **SECOND/THIRD:** reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V16. **CHANGES:** hard exit from noise to new question card.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place a blank light-gray rounded question panel across the upper frame and the recurring faceless reader with small device seated at the outlined desk/monitor/chair cluster low below on pure white. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to stop a volcano eruption by placing a bomb (thermobaric or nuclear) underneath the surface? — Tomasz Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V17. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F04.0. **SHOT:** S04. **MEASURED RANGE:** 21.375–22.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V16 → V17/F04.0 → V18. The transition into this state is hard exit from noise to new question card; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A19 (hard replacement; full frame; 21.375–21.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A19:** Begins the volcano/bomb submission cleanly Direction/speed/path are limited to `noise switches to Tomasz card/base reader` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** new card and recurring reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A19 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** new card and recurring reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A19: STATE REPLACEMENT—full frame is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A19: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A19: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A19:** isolate `full frame` over the fixed V16/FTR02 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A19 SOURCE FRAME STATE:** V16/FTR02. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V16_0021250ms.jpg). If regeneration is required, use the full standalone prompt in card V16, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A19
**SOURCE STATE:** V16/FTR02  
**TARGET STATE:** V17/F04.0  
**TIMESTAMP:** 21.375–21.375  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** noise switches to Tomasz card/base reader  
**CAMERA:** locked  
**STATIC ANCHORS:** new card and recurring reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from gray noise to the Tomasz question-card base with the recurring seated reader, desk, monitor and chair low in the white vertical frame. Match the registered stage geometry; no thought bubble or Jeff elements remain.”  
**CHARACTER COUNT:** 228 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A19 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 22.375s, transition to V18. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V17 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V18 — 23.000s — Volcano thought bubble
**SHOT:** S04  
**DURATION:** 2.000 s (22.375–24.375)  
**FRAME STATE:** F04.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V18_0023000ms.jpg)

![V18 source frame](weird_worrying_forensics/keyframes/V18_0023000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a scalloped bubble appears containing a centered conical volcano and sparse low landscape marks. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A scalloped bubble appears containing a centered conical volcano and sparse low landscape marks.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…to stop a volcano eruption…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Establish the hazard site before adding the proposed bomb.  
**MOTION CUE:** add thought bubble and centered volcano.  
**FUNCTION:** Establish the hazard site before adding the proposed bomb.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add thought bubble and centered volcano. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Establish the hazard site before adding the proposed bomb. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A scalloped bubble appears containing a centered conical volcano and sparse low landscape marks.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** volcano.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** bubble X 6–94/Y 30–69; volcano X 22–79/Y 43–64; reader/card unchanged. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** volcano → question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** volcano. **SECOND/THIRD:** question panel → reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V17. **CHANGES:** add thought bubble and centered volcano.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Tomasz panel and lower reader stage; add a large scalloped thought bubble containing one centered hand-drawn conical volcano with a shallow crater and sparse low ground marks. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to stop a volcano eruption by placing a bomb (thermobaric or nuclear) underneath the surface? — Tomasz Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V18. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F04.1. **SHOT:** S04. **MEASURED RANGE:** 22.375–24.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V17 → V18/F04.1 → V19. The transition into this state is add thought bubble and centered volcano; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A20 (additive reveal; volcano thought bubble; 22.375–22.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A20:** Establishes the physical site before introducing the proposed intervention Direction/speed/path are limited to `instant bubble and volcano appearance` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** Tomasz card and reader-stage cluster. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A20 ALLOWED TO MOVE/CHANGE:** volcano thought bubble. **LOCKED:** Tomasz card and reader-stage cluster. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A20: STATE REPLACEMENT—volcano thought bubble is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A20: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A20: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A20:** isolate `X 6-94 Y 29-69` over the fixed V17/F04.0 base; generate/change only volcano thought bubble; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A20 SOURCE FRAME STATE:** V17/F04.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V17_0021750ms.jpg). If regeneration is required, use the full standalone prompt in card V17, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A20
**SOURCE STATE:** V17/F04.0  
**TARGET STATE:** V18/F04.1  
**TIMESTAMP:** 22.375–22.375  
**MOTION TYPE/HERO:** additive reveal / volcano thought bubble  
**DIRECTION, SPEED, PATH:** instant bubble and volcano appearance  
**CAMERA:** locked  
**STATIC ANCHORS:** Tomasz card and reader-stage cluster  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the scalloped thought bubble above the reader containing the centered hand-drawn volcano and sparse ground marks. Preserve the Tomasz card, seated reader, desk, monitor, chair, scale and white background. Hold the completed volcano state.”  
**CHARACTER COUNT:** 257 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A20 uses `REPLACEMENT DRAWING` in ROI X 6-94 Y 29-69; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 24.375s, transition to V19. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V18 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V19 — 25.500s — Bomb above volcano
**SHOT:** S04  
**DURATION:** 2.875 s (24.375–27.250)  
**FRAME STATE:** F04.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V19_0025500ms.jpg)

![V19 source frame](weird_worrying_forensics/keyframes/V19_0025500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a small striped bomb icon now hangs directly above the volcano crater; the volcano and all outer anchors remain unchanged. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A small striped bomb icon now hangs directly above the volcano crater; the volcano and all outer anchors remain unchanged.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…by placing a bomb, thermobaric or nuclear, underneath the surface?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Clarify the question’s proposed placement as a vertical cause/effect setup.  
**MOTION CUE:** add bomb over crater.  
**FUNCTION:** Clarify the question’s proposed placement as a vertical cause/effect setup.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add bomb over crater. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Clarify the question’s proposed placement as a vertical cause/effect setup. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A small striped bomb icon now hangs directly above the volcano crater; the volcano and all outer anchors remain unchanged.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** bomb.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** bomb X 46–55/Y 34–46; volcano X 22–79/Y 43–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** bomb → crater → question card.
### 7. ATTENTION ORDER
**FIRST LOOK:** bomb. **SECOND/THIRD:** crater → question card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V18. **CHANGES:** add bomb over crater.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Tomasz panel, reader stage, bubble and centered volcano; add one small vertically oriented striped bomb icon directly above the crater with clear white separation. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to stop a volcano eruption by placing a bomb (thermobaric or nuclear) underneath the surface? — Tomasz Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V19. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F04.2. **SHOT:** S04. **MEASURED RANGE:** 24.375–27.250. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V18 → V19/F04.2 → V20. The transition into this state is add bomb over crater; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A21 (additive reveal; bomb icon; 24.375–24.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A21:** Maps the proposed bomb placement to a simple vertical cause/effect setup Direction/speed/path are limited to `bomb appears directly above crater` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** volcano, bubble, card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A21 ALLOWED TO MOVE/CHANGE:** bomb icon. **LOCKED:** volcano, bubble, card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A21: SEQUENTIAL—bomb icon is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A21: REPLACEMENT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A21: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A21:** isolate `X 44-57 Y 34-48` over the fixed V18/F04.1 base; generate/change only bomb icon; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A21 SOURCE FRAME STATE:** V18/F04.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V18_0023000ms.jpg). If regeneration is required, use the full standalone prompt in card V18, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A21
**SOURCE STATE:** V18/F04.1  
**TARGET STATE:** V19/F04.2  
**TIMESTAMP:** 24.375–24.375  
**MOTION TYPE/HERO:** additive reveal / bomb icon  
**DIRECTION, SPEED, PATH:** bomb appears directly above crater  
**CAMERA:** locked  
**STATIC ANCHORS:** volcano, bubble, card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add only the observed striped bomb icon centered above the volcano crater at the reference height and scale. Keep the volcano drawing, thought-bubble contour/tail, Tomasz card, seated reader, desk, chair, monitor and white field unchanged. Hold.”  
**CHARACTER COUNT:** 260 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A21 uses `REPLACEMENT OVERLAY` in ROI X 44-57 Y 34-48; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 27.250s, transition to V20. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V19 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V20 — 27.750s — Volcano explosion
**SHOT:** S04  
**DURATION:** 0.917 s (27.250–28.167)  
**FRAME STATE:** F04.3  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V20_0027750ms.jpg)

![V20 source frame](weird_worrying_forensics/keyframes/V20_0027750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the quiet volcano and bomb are replaced by a large hand-drawn mushroom-cloud eruption that fills most of the thought bubble. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The quiet volcano and bomb are replaced by a large hand-drawn mushroom-cloud eruption that fills most of the thought bubble.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Tomasz’s question finishes as the explosion answer appears.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Deliver the obvious destructive consequence as a visual answer.  
**MOTION CUE:** replace bomb/volcano with mushroom-cloud eruption drawing.  
**FUNCTION:** Deliver the obvious destructive consequence as a visual answer.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace bomb/volcano with mushroom-cloud eruption drawing. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Deliver the obvious destructive consequence as a visual answer. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The quiet volcano and bomb are replaced by a large hand-drawn mushroom-cloud eruption that fills most of the thought bubble.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** mushroom cloud.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** blast X 9–92/Y 33–67; bubble/card/reader fixed. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** mushroom cloud → question card → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** mushroom cloud. **SECOND/THIRD:** question card → reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V19. **CHANGES:** replace bomb/volcano with mushroom-cloud eruption drawing.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Tomasz panel, reader stage and scalloped bubble; replace the interior volcano/bomb with a large black-line mushroom-cloud eruption, wide rolling cloud cap, central column and radiating ground debris. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would it be possible to stop a volcano eruption by placing a bomb (thermobaric or nuclear) underneath the surface? — Tomasz Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V20. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F04.3. **SHOT:** S04. **MEASURED RANGE:** 27.250–28.167. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V19 → V20/F04.3 → V21. The transition into this state is replace bomb/volcano with mushroom-cloud eruption drawing; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A22 (replacement drawing; volcano explosion; 27.250–27.250 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A22:** Provides the destructive visual consequence and comedic answer Direction/speed/path are limited to `bomb/quiet volcano switch to mushroom-cloud eruption` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** thought bubble, Tomasz card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A22 ALLOWED TO MOVE/CHANGE:** volcano explosion. **LOCKED:** thought bubble, Tomasz card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A22: STATE REPLACEMENT—volcano explosion is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A22: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A22: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A22:** isolate `X 8-92 Y 31-67` over the fixed V19/F04.2 base; generate/change only volcano explosion; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A22 SOURCE FRAME STATE:** V19/F04.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V19_0025500ms.jpg). If regeneration is required, use the full standalone prompt in card V19, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A22
**SOURCE STATE:** V19/F04.2  
**TARGET STATE:** V20/F04.3  
**TIMESTAMP:** 27.250–27.250  
**MOTION TYPE/HERO:** replacement drawing / volcano explosion  
**DIRECTION, SPEED, PATH:** bomb/quiet volcano switch to mushroom-cloud eruption  
**CAMERA:** locked  
**STATIC ANCHORS:** thought bubble, Tomasz card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace only the bomb-and-volcano content inside the thought bubble with the observed large mushroom-cloud eruption drawing, retaining approximately the same bubble footprint. Preserve the bubble border/tail, Tomasz card, reader, desk, monitor, chair and white background. Hold the blast state.”  
**CHARACTER COUNT:** 309 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A22 uses `REPLACEMENT DRAWING` in ROI X 8-92 Y 31-67; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 28.167s, transition to V21. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V20 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V21 — 28.250s — Gray-noise transition
**SHOT:** TR03  
**DURATION:** 0.208 s (28.167–28.375)  
**FRAME STATE:** FTR03  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V21_0028250ms.jpg)

![V21 source frame](weird_worrying_forensics/keyframes/V21_0028250ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a full-frame neutral-gray television-noise plate replaces the volcano scene. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A full-frame neutral-gray television-noise plate replaces the volcano scene.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Brief transition gap.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Separate the first disaster-response question from AJ’s parallel one.  
**MOTION CUE:** hard replace scene with changing gray noise.  
**FUNCTION:** Separate the first disaster-response question from AJ’s parallel one.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace scene with changing gray noise. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Separate the first disaster-response question from AJ’s parallel one. Information value: TRANSITIONAL. Removing this state would erase the section boundary.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field replaced by gray noise.  
**MAIN SUBJECT:** A full-frame neutral-gray television-noise plate replaces the volcano scene.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** uniform texture.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** noise X 0–100/Y 0–100. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** uniform texture.
### 7. ATTENTION ORDER
**FIRST LOOK:** uniform texture. **SECOND/THIRD:** none. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** UNIFORM.
### 8. IMAGE REUSE STATUS
**STATUS:** EXACT REUSE of E03 noise design with a new random frame; ANIMATED-TRANSITION. **BASE:** V20. **CHANGES:** hard replace scene with changing gray noise.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; fill the full vertical canvas with dense fine neutral-gray television noise and no text, objects, characters, borders or directional motion. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V21. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** FTR03. **SHOT:** TR03. **MEASURED RANGE:** 28.167–28.375. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V20 → V21/FTR03 → V22. The transition into this state is hard replace scene with changing gray noise; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A23 (hard replacement; full frame; 28.167–28.167 s), A24 (procedural texture loop; gray noise; 28.167–28.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A23:** Resets between the two disaster-response submissions Direction/speed/path are limited to `instant cut to gray noise` because the reference shows no broader motion.
**A24:** Repeats the established inbox separator motif Direction/speed/path are limited to `fine random monochrome pixels change every frame` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** no volcano elements persist; full-frame luminance range and boundary. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A23 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** no volcano elements persist. **OTHER ACTIVE:** A24 starts. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A24 ALLOWED TO MOVE/CHANGE:** gray noise. **LOCKED:** full-frame luminance range and boundary. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A23: STATE REPLACEMENT—full frame is isolated from every unrelated anchor; A24: PERSISTENT LOOP—gray noise is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A23: EDITOR HARD CUT; A24: EDITOR PROCEDURAL NOISE. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A23: LOW—exact line/text registration favors the named deterministic method; A24: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A23:** isolate `full frame` over the fixed V20/F04.3 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A24:** isolate `full frame` over the fixed V21/FTR03 base; generate/change only gray noise; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A23 SOURCE FRAME STATE:** V20/F04.3. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V20_0027750ms.jpg). If regeneration is required, use the full standalone prompt in card V20, then apply that card’s exact text overlays before/after motion as appropriate.
**A24 SOURCE FRAME STATE:** V21/FTR03. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V21_0028250ms.jpg). If regeneration is required, use the full standalone prompt in card V21, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A23
**SOURCE STATE:** V20/F04.3  
**TARGET STATE:** V21/FTR03  
**TIMESTAMP:** 28.167–28.167  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut to gray noise  
**CAMERA:** locked  
**STATIC ANCHORS:** no volcano elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from the completed volcano explosion composition to a full-frame neutral gray television-noise plate. Do not retain the card, thought bubble, blast or reader stage. Keep the 9:16 frame locked.”  
**CHARACTER COUNT:** 201 / 500  
**STATUS:** PASS
#### ANIMATION A24
**SOURCE STATE:** V21/FTR03  
**TARGET STATE:** V21/FTR03  
**TIMESTAMP:** 28.167–28.375  
**MOTION TYPE/HERO:** procedural texture loop / gray noise  
**DIRECTION, SPEED, PATH:** fine random monochrome pixels change every frame  
**CAMERA:** locked  
**STATIC ANCHORS:** full-frame luminance range and boundary  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked frame. Animate only fine neutral-gray television noise across the full 9:16 image for the observed 0.21-second bridge. Preserve even mid-gray density; add no text, drawings, camera motion or directional transition.”  
**CHARACTER COUNT:** 221 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A23 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. A24 uses `EDITOR PROCEDURAL NOISE` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 28.375s, transition to V22. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V21 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V22 — 28.750s — AJ question card
**SHOT:** S05  
**DURATION:** 1.042 s (28.375–29.417)  
**FRAME STATE:** F05.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V22_0028750ms.jpg)

![V22 source frame](weird_worrying_forensics/keyframes/V22_0028750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the AJ anti-matter/Chernobyl question appears in the top gray card above the unchanged reader stage. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The AJ anti-matter/Chernobyl question appears in the top gray card above the unchanged reader stage.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘AJ asks, would dumping antimatter into the Chernobyl reactor…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Begin the second disaster-response setup through exact visual reuse.  
**MOTION CUE:** hard exit from noise to antimatter/Chernobyl question.  
**FUNCTION:** Begin the second disaster-response setup through exact visual reuse.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard exit from noise to antimatter/Chernobyl question. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Begin the second disaster-response setup through exact visual reuse. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The AJ anti-matter/Chernobyl question appears in the top gray card above the unchanged reader stage.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** question panel.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** card X 5–95/Y 6–29; reader/desk X 18–66/Y 71–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** question panel. **SECOND/THIRD:** reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V21. **CHANGES:** hard exit from noise to antimatter/Chernobyl question.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place a blank light-gray rounded question panel across the upper frame and the recurring faceless reader seated with device at the compact outlined desk, monitor and chair low on a pure white background. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would dumping anti-matter into the Chernobyl reactor when it was melting down stop the meltdown? — AJ Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V22. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F05.0. **SHOT:** S05. **MEASURED RANGE:** 28.375–29.417. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V21 → V22/F05.0 → V23. The transition into this state is hard exit from noise to antimatter/Chernobyl question; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A25 (hard replacement; full frame; 28.375–28.375 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A25:** Starts the parallel antimatter/Chernobyl question Direction/speed/path are limited to `noise switches to AJ card/base reader` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** new card and recurring reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A25 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** new card and recurring reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A25: STATE REPLACEMENT—full frame is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A25: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A25: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A25:** isolate `full frame` over the fixed V21/FTR03 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A25 SOURCE FRAME STATE:** V21/FTR03. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V21_0028250ms.jpg). If regeneration is required, use the full standalone prompt in card V21, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A25
**SOURCE STATE:** V21/FTR03  
**TARGET STATE:** V22/F05.0  
**TIMESTAMP:** 28.375–28.375  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** noise switches to AJ card/base reader  
**CAMERA:** locked  
**STATIC ANCHORS:** new card and recurring reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from gray noise to the AJ question-card base with the recurring seated reader, desk, monitor and chair low in the white vertical frame. Match the reference card and stage registration; no volcano imagery remains.”  
**CHARACTER COUNT:** 221 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A25 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 29.417s, transition to V23. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V22 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V23 — 29.500s — Chernobyl reactor thought bubble
**SHOT:** S05  
**DURATION:** 0.541 s (29.417–29.958)  
**FRAME STATE:** F05.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V23_0029500ms.jpg)

![V23 source frame](weird_worrying_forensics/keyframes/V23_0029500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a thought bubble contains a hand-drawn reactor complex with tall central stack and a radiation placard at far left. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A thought bubble contains a hand-drawn reactor complex with tall central stack and a radiation placard at far left.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…into the Chernobyl reactor when it was melting down…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Ground AJ’s proposal in a recognizable hazard/site diagram.  
**MOTION CUE:** add thought bubble, reactor and radiation placard.  
**FUNCTION:** Ground AJ’s proposal in a recognizable hazard/site diagram.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add thought bubble, reactor and radiation placard. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Ground AJ’s proposal in a recognizable hazard/site diagram. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A thought bubble contains a hand-drawn reactor complex with tall central stack and a radiation placard at far left.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** radiation placard.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** bubble X 6–94/Y 30–69; placard X 11–27/Y 47–64; facility X 27–89/Y 38–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** radiation placard → reactor stack → question panel.
### 7. ATTENTION ORDER
**FIRST LOOK:** radiation placard. **SECOND/THIRD:** reactor stack → question panel. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V22. **CHANGES:** add thought bubble, reactor and radiation placard.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank AJ panel and lower reader stage; add a scalloped thought bubble containing an outlined industrial reactor complex with long low buildings and tall central stack, plus a triangular radiation placard at left. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would dumping anti-matter into the Chernobyl reactor when it was melting down stop the meltdown? — AJ Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V23. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F05.1. **SHOT:** S05. **MEASURED RANGE:** 29.417–29.958. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V22 → V23/F05.1 → V24. The transition into this state is add thought bubble, reactor and radiation placard; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A26 (additive reveal; reactor thought bubble; 29.417–29.417 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A26:** Creates the site and hazard icon before antimatter is introduced Direction/speed/path are limited to `instant bubble, facility and radiation placard appearance` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** AJ card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A26 ALLOWED TO MOVE/CHANGE:** reactor thought bubble. **LOCKED:** AJ card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A26: STATE REPLACEMENT—reactor thought bubble is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A26: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A26: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A26:** isolate `X 6-94 Y 29-69` over the fixed V22/F05.0 base; generate/change only reactor thought bubble; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A26 SOURCE FRAME STATE:** V22/F05.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V22_0028750ms.jpg). If regeneration is required, use the full standalone prompt in card V22, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A26
**SOURCE STATE:** V22/F05.0  
**TARGET STATE:** V23/F05.1  
**TIMESTAMP:** 29.417–29.417  
**MOTION TYPE/HERO:** additive reveal / reactor thought bubble  
**DIRECTION, SPEED, PATH:** instant bubble, facility and radiation placard appearance  
**CAMERA:** locked  
**STATIC ANCHORS:** AJ card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the observed scalloped thought bubble containing the hand-drawn Chernobyl reactor complex and radiation placard at left. Preserve the AJ card, seated reader, desk, monitor, chair, scale and white background. Hold the complete facility state.”  
**CHARACTER COUNT:** 260 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A26 uses `REPLACEMENT DRAWING` in ROI X 6-94 Y 29-69; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 29.958s, transition to V24. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V23 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V24 — 31.000s — Antimatter label added
**SHOT:** S05  
**DURATION:** 3.625 s (29.958–33.583)  
**FRAME STATE:** F05.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V24_0031000ms.jpg)

![V24 source frame](weird_worrying_forensics/keyframes/V24_0031000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the reactor persists while a hand-lettered ANTIMATTER label, arrow and tiny particle marks appear above its stack. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The reactor persists while a hand-lettered ANTIMATTER label, arrow and tiny particle marks appear above its stack.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…would dumping antimatter…’ / ‘…stop the meltdown?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Name and locate the proposed substance without disturbing the facility diagram.  
**MOTION CUE:** add ANTIMATTER label and small particle marks above reactor.  
**FUNCTION:** Name and locate the proposed substance without disturbing the facility diagram.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add ANTIMATTER label and small particle marks above reactor. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Name and locate the proposed substance without disturbing the facility diagram. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The reactor persists while a hand-lettered ANTIMATTER label, arrow and tiny particle marks appear above its stack.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** label zone/particles.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** label zone X 12–51/Y 35–44; particles X 49–57/Y 34–42; facility X 27–89/Y 38–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** label zone/particles → radiation placard → reactor.
### 7. ATTENTION ORDER
**FIRST LOOK:** label zone/particles. **SECOND/THIRD:** radiation placard → reactor. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V23. **CHANGES:** add ANTIMATTER label and small particle marks above reactor.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank AJ panel, reader, scalloped bubble, reactor and radiation placard; reserve a blank label zone above the facility and add only a short right-pointing line ending in a few tiny circular particle marks near the stack. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would dumping anti-matter into the Chernobyl reactor when it was melting down stop the meltdown? — AJ | ANTIMATTER Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V24. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F05.2. **SHOT:** S05. **MEASURED RANGE:** 29.958–33.583. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V23 → V24/F05.2 → V25. The transition into this state is add ANTIMATTER label and small particle marks above reactor; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A27 (text/icon reveal; ANTIMATTER label and arrow/particle marks; 29.958–29.958 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A27:** Names and locates the proposed material without disturbing exact facility geometry Direction/speed/path are limited to `instant overlay above facility` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** reactor, placard, bubble, card and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A27 ALLOWED TO MOVE/CHANGE:** ANTIMATTER label and arrow/particle marks. **LOCKED:** reactor, placard, bubble, card and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A27: SEQUENTIAL—ANTIMATTER label and arrow/particle marks is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A27: DETERMINISTIC TEXT + REPLACEMENT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A27: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A27:** isolate `X 12-56 Y 35-43` over the fixed V23/F05.1 base; generate/change only ANTIMATTER label and arrow/particle marks; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A27 SOURCE FRAME STATE:** V23/F05.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V23_0029500ms.jpg). If regeneration is required, use the full standalone prompt in card V23, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A27
**SOURCE STATE:** V23/F05.1  
**TARGET STATE:** V24/F05.2  
**TIMESTAMP:** 29.958–29.958  
**MOTION TYPE/HERO:** text/icon reveal / ANTIMATTER label and arrow/particle marks  
**DIRECTION, SPEED, PATH:** instant overlay above facility  
**CAMERA:** locked  
**STATIC ANCHORS:** reactor, placard, bubble, card and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Reveal only the hand-lettered “ANTIMATTER” label, right-pointing arrow and tiny particle marks above the reactor. Keep the radiation placard, facility, thought-bubble border/tail, AJ card, seated reader, desk, chair, monitor and white background completely fixed. Hold.”  
**CHARACTER COUNT:** 284 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A27 uses `DETERMINISTIC TEXT + REPLACEMENT OVERLAY` in ROI X 12-56 Y 35-43; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 33.583s, transition to V25. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V24 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V25 — 34.000s — Reactor explosion
**SHOT:** S05  
**DURATION:** 1.167 s (33.583–34.750)  
**FRAME STATE:** F05.3  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V25_0034000ms.jpg)

![V25 source frame](weird_worrying_forensics/keyframes/V25_0034000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a large central explosion replaces much of the reactor, while the radiation placard, bubble, AJ card and reader remain. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A large central explosion replaces much of the reactor, while the radiation placard, bubble, AJ card and reader remain.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** AJ’s question completes on the reactor-blast consequence.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Show that the proposed intervention compounds rather than solves the disaster.  
**MOTION CUE:** replace facility center with a large blast drawing.  
**FUNCTION:** Show that the proposed intervention compounds rather than solves the disaster.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** replace facility center with a large blast drawing. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Show that the proposed intervention compounds rather than solves the disaster. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A large central explosion replaces much of the reactor, while the radiation placard, bubble, AJ card and reader remain.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** blast.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** blast X 19–91/Y 33–65; placard X 10–27/Y 48–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** blast → radiation placard → question card.
### 7. ATTENTION ORDER
**FIRST LOOK:** blast. **SECOND/THIRD:** radiation placard → question card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V24. **CHANGES:** replace facility center with a large blast drawing.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank AJ panel, reader stage, thought-bubble border and left radiation placard; replace the facility center with a large irregular black-line explosion cloud and rising blast column while leaving low building fragments beneath. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Would dumping anti-matter into the Chernobyl reactor when it was melting down stop the meltdown? — AJ Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V25. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F05.3. **SHOT:** S05. **MEASURED RANGE:** 33.583–34.750. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V24 → V25/F05.3 → V26. The transition into this state is replace facility center with a large blast drawing; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A28 (replacement drawing; reactor explosion; 33.583–33.583 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A28:** Turns the proposed “solution” into a second obvious disaster Direction/speed/path are limited to `facility center switches to large blast` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** question card, bubble, radiation placard and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A28 ALLOWED TO MOVE/CHANGE:** reactor explosion. **LOCKED:** question card, bubble, radiation placard and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A28: STATE REPLACEMENT—reactor explosion is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A28: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A28: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A28:** isolate `X 17-91 Y 31-66` over the fixed V24/F05.2 base; generate/change only reactor explosion; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A28 SOURCE FRAME STATE:** V24/F05.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V24_0031000ms.jpg). If regeneration is required, use the full standalone prompt in card V24, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A28
**SOURCE STATE:** V24/F05.2  
**TARGET STATE:** V25/F05.3  
**TIMESTAMP:** 33.583–33.583  
**MOTION TYPE/HERO:** replacement drawing / reactor explosion  
**DIRECTION, SPEED, PATH:** facility center switches to large blast  
**CAMERA:** locked  
**STATIC ANCHORS:** question card, bubble, radiation placard and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace the central reactor drawing inside the thought bubble with the observed large explosion cloud while retaining the radiation placard at left. Preserve the bubble border/tail, AJ question card, seated reader, desk, monitor, chair and white background. Hold the blast state.”  
**CHARACTER COUNT:** 294 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A28 uses `REPLACEMENT DRAWING` in ROI X 17-91 Y 31-66; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 34.750s, transition to V26. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V25 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V26 — 34.750s — Award certificate for AJ
**SHOT:** S06  
**DURATION:** 0.292 s (34.750–35.042)  
**FRAME STATE:** F06.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V26_0034750ms.jpg)

![V26 source frame](weird_worrying_forensics/keyframes/V26_0034750ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a large outlined landscape certificate dominates the upper two-thirds; a radiation icon and AJ sit at upper-left, a rosette hangs at lower-right, and the reader gestures below. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A large outlined landscape certificate dominates the upper two-thirds; a radiation icon and AJ sit at upper-left, a rosette hangs at lower-right, and the reader gestures below.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘AJ and Tomasz, in recognition for your disaster response efforts…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Begin the joint-award payoff with AJ as the first recipient.  
**MOTION CUE:** hard cut to large certificate with radiation icon, AJ and seal.  
**FUNCTION:** Begin the joint-award payoff with AJ as the first recipient.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard cut to large certificate with radiation icon, AJ and seal. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Begin the joint-award payoff with AJ as the first recipient. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A large outlined landscape certificate dominates the upper two-thirds; a radiation icon and AJ sit at upper-left, a rosette hangs at lower-right, and the reader gestures below.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** certificate/radiation icon.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** certificate X 6–94/Y 17–55; radiation icon X 10–24/Y 22–34; blank name zone X 25–49/Y 23–33; rosette X 78–91/Y 48–64; reader/desk X 18–67/Y 67–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** certificate/radiation icon → blank recipient zone → gesturing reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** certificate/radiation icon. **SECOND/THIRD:** blank recipient zone → gesturing reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** NEW BASE; STABLE. **BASE:** V25. **CHANGES:** hard cut to large certificate with radiation icon, AJ and seal.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; draw a large blank landscape certificate rectangle across the upper two-thirds with a radiation triangle icon near its upper-left and a rosette seal with two ribbon tails at lower-right; below, place the recurring faceless reader in a one-arm gesturing seated pose beside desk and chair. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** AJ Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V26. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F06.0. **SHOT:** S06. **MEASURED RANGE:** 34.750–35.042. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V25 → V26/F06.0 → V27. The transition into this state is hard cut to large certificate with radiation icon, AJ and seal; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A29 (hard cut / state replacement; award certificate composition; 34.750–34.750 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A29:** Begins the joint comic judgment/payoff after both disaster questions Direction/speed/path are limited to `AJ reactor scene switches to certificate` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** white background; seated reader changes pose and certificate becomes anchor. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A29 ALLOWED TO MOVE/CHANGE:** award certificate composition. **LOCKED:** white background; seated reader changes pose and certificate becomes anchor. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A29: STATE REPLACEMENT—award certificate composition is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A29: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A29: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A29:** isolate `full frame` over the fixed V25/F05.3 base; generate/change only award certificate composition; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A29 SOURCE FRAME STATE:** V25/F05.3. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V25_0034000ms.jpg). If regeneration is required, use the full standalone prompt in card V25, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A29
**SOURCE STATE:** V25/F05.3  
**TARGET STATE:** V26/F06.0  
**TIMESTAMP:** 34.750–34.750  
**MOTION TYPE/HERO:** hard cut / state replacement / award certificate composition  
**DIRECTION, SPEED, PATH:** AJ reactor scene switches to certificate  
**CAMERA:** locked  
**STATIC ANCHORS:** white background; seated reader changes pose and certificate becomes anchor  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut to the award composition: large outlined certificate across the upper two-thirds with radiation icon and “AJ” at upper left, rosette at lower right, and the reader in the observed gesturing pose below. Remove the question card and thought bubble; preserve the white 9:16 field.”  
**CHARACTER COUNT:** 286 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A29 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 35.042s, transition to V27. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V26 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V27 — 36.000s — AJ & TOMASZ awardees
**SHOT:** S06  
**DURATION:** 3.541 s (35.042–38.583)  
**FRAME STATE:** F06.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V27_0036000ms.jpg)

![V27 source frame](weird_worrying_forensics/keyframes/V27_0036000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the certificate header now names AJ & TOMASZ between a radiation icon at left and striped bomb icon at right; the rosette and reader stay fixed. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The certificate header now names AJ & TOMASZ between a radiation icon at left and striped bomb icon at right; the rosette and reader stay fixed.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…we award you…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Unify AJ and Tomasz as recipients of the same comic judgment.  
**MOTION CUE:** add & TOMASZ and bomb icon to certificate header.  
**FUNCTION:** Unify AJ and Tomasz as recipients of the same comic judgment.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add & TOMASZ and bomb icon to certificate header. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Unify AJ and Tomasz as recipients of the same comic judgment. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The certificate header now names AJ & TOMASZ between a radiation icon at left and striped bomb icon at right; the rosette and reader stay fixed.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** recipient line.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** recipient zone X 25–75/Y 23–34; radiation icon X 10–24/Y 22–34; bomb X 78–88/Y 22–35; rosette X 78–91/Y 48–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** recipient line → paired hazard icons → rosette.
### 7. ATTENTION ORDER
**FIRST LOOK:** recipient line. **SECOND/THIRD:** paired hazard icons → rosette. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V26. **CHANGES:** add & TOMASZ and bomb icon to certificate header.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the large blank certificate, radiation triangle, rosette and lower gesturing reader; reserve a long blank recipient line across the certificate top and add a small striped bomb icon at its upper-right. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** AJ & TOMASZ Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V27. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F06.1. **SHOT:** S06. **MEASURED RANGE:** 35.042–38.583. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V26 → V27/F06.1 → V28. The transition into this state is add & TOMASZ and bomb icon to certificate header; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A30 (additive reveal; & TOMASZ and bomb icon; 35.042–35.042 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A30:** Combines the two hazardous submitters into one award recipient line Direction/speed/path are limited to `instant header expansion across certificate top` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** certificate border, AJ, radiation icon, rosette and reader pose. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A30 ALLOWED TO MOVE/CHANGE:** & TOMASZ and bomb icon. **LOCKED:** certificate border, AJ, radiation icon, rosette and reader pose. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A30: SEQUENTIAL—& TOMASZ and bomb icon is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A30: DETERMINISTIC TEXT/ICON OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A30: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A30:** isolate `X 25-88 Y 23-35` over the fixed V26/F06.0 base; generate/change only & TOMASZ and bomb icon; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A30 SOURCE FRAME STATE:** V26/F06.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V26_0034750ms.jpg). If regeneration is required, use the full standalone prompt in card V26, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A30
**SOURCE STATE:** V26/F06.0  
**TARGET STATE:** V27/F06.1  
**TIMESTAMP:** 35.042–35.042  
**MOTION TYPE/HERO:** additive reveal / & TOMASZ and bomb icon  
**DIRECTION, SPEED, PATH:** instant header expansion across certificate top  
**CAMERA:** locked  
**STATIC ANCHORS:** certificate border, AJ, radiation icon, rosette and reader pose  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add only the exact hand-lettered “& TOMASZ” after AJ and the striped bomb icon at the certificate’s upper-right. Preserve the radiation symbol, certificate outline, rosette, seated gesturing reader, desk, monitor, chair and white background exactly. Hold.”  
**CHARACTER COUNT:** 270 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A30 uses `DETERMINISTIC TEXT/ICON OVERLAY` in ROI X 25-88 Y 23-35; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 38.583s, transition to V28. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V27 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V28 — 39.500s — Award title revealed
**SHOT:** S06  
**DURATION:** 2.167 s (38.583–40.750)  
**FRAME STATE:** F06.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V28_0039500ms.jpg)

![V28 source frame](weird_worrying_forensics/keyframes/V28_0039500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the completed certificate adds the two-line hand-lettered title FOR GOD’S SAKE, WHAT / WERE YOU THINKING?! in its center. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The completed certificate adds the two-line hand-lettered title FOR GOD’S SAKE, WHAT / WERE YOU THINKING?! in its center.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…the “For God’s sake, what were you thinking?” award.’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Deliver the segment’s explicit comic verdict and combined payoff.  
**MOTION CUE:** add FOR GOD'S SAKE, WHAT WERE YOU THINKING?! in certificate center.  
**FUNCTION:** Deliver the segment’s explicit comic verdict and combined payoff.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add FOR GOD'S SAKE, WHAT WERE YOU THINKING?! in certificate center. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Deliver the segment’s explicit comic verdict and combined payoff. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The completed certificate adds the two-line hand-lettered title FOR GOD’S SAKE, WHAT / WERE YOU THINKING?! in its center.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** large award-title zone.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** recipient zone X 25–75/Y 23–34; title zone X 14–88/Y 38–52; rosette X 78–91/Y 48–64. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** large award-title zone → recipient line/icons → rosette/reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** large award-title zone. **SECOND/THIRD:** recipient line/icons → rosette/reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V27. **CHANGES:** add FOR GOD'S SAKE, WHAT WERE YOU THINKING?! in certificate center.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank certificate, radiation and bomb icons, rosette and lower gesturing reader; reserve a large centered two-line title zone in the certificate middle with generous white margins. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** AJ & TOMASZ | FOR GOD’S SAKE, WHAT / WERE YOU THINKING?! Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V28. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F06.2. **SHOT:** S06. **MEASURED RANGE:** 38.583–40.750. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V27 → V28/F06.2 → V29. The transition into this state is add FOR GOD'S SAKE, WHAT WERE YOU THINKING?! in certificate center; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A31 (text reveal; award title; 38.583–38.583 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A31:** Delivers the named “what were you thinking” award as the segment’s main punch line Direction/speed/path are limited to `instant two-line title appears in certificate center` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** header names/icons, certificate, rosette and reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A31 ALLOWED TO MOVE/CHANGE:** award title. **LOCKED:** header names/icons, certificate, rosette and reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A31: SEQUENTIAL—award title is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A31: DETERMINISTIC TEXT OVERLAY. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A31: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A31:** isolate `X 14-87 Y 40-53` over the fixed V27/F06.1 base; generate/change only award title; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A31 SOURCE FRAME STATE:** V27/F06.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V27_0036000ms.jpg). If regeneration is required, use the full standalone prompt in card V27, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A31
**SOURCE STATE:** V27/F06.1  
**TARGET STATE:** V28/F06.2  
**TIMESTAMP:** 38.583–38.583  
**MOTION TYPE/HERO:** text reveal / award title  
**DIRECTION, SPEED, PATH:** instant two-line title appears in certificate center  
**CAMERA:** locked  
**STATIC ANCHORS:** header names/icons, certificate, rosette and reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Reveal only the centered two-line hand lettering “FOR GOD’S SAKE, WHAT / WERE YOU THINKING?!” inside the certificate. Preserve AJ & TOMASZ, the radiation and bomb icons, border, rosette, reader pose, furniture and white background. Hold the completed award.”  
**CHARACTER COUNT:** 272 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A31 uses `DETERMINISTIC TEXT OVERLAY` in ROI X 14-87 Y 40-53; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 40.750s, transition to V29. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V28 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V29 — 40.833s — Gray-noise transition
**SHOT:** TR04  
**DURATION:** 0.208 s (40.750–40.958)  
**FRAME STATE:** FTR04  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V29_0040792ms.jpg)

![V29 source frame](weird_worrying_forensics/keyframes/V29_0040792ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see fine full-frame neutral-gray television noise replaces the completed certificate. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** Fine full-frame neutral-gray television noise replaces the completed certificate.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** Brief transition gap before Karl.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Reset attention before the final, emotionally softer question.  
**MOTION CUE:** hard replace award with changing gray noise.  
**FUNCTION:** Reset attention before the final, emotionally softer question.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace award with changing gray noise. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Reset attention before the final, emotionally softer question. Information value: TRANSITIONAL. Removing this state would erase the section boundary.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field replaced by gray noise.  
**MAIN SUBJECT:** Fine full-frame neutral-gray television noise replaces the completed certificate.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** uniform texture.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** noise X 0–100/Y 0–100. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** uniform texture.
### 7. ATTENTION ORDER
**FIRST LOOK:** uniform texture. **SECOND/THIRD:** none. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** UNIFORM.
### 8. IMAGE REUSE STATUS
**STATUS:** EXACT REUSE of E03 noise design with a new random frame; ANIMATED-TRANSITION. **BASE:** V28. **CHANGES:** hard replace award with changing gray noise.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; fill the entire 9:16 frame with even fine neutral-gray television-noise grain and no objects, text, certificate edges or directional wipe. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V29. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** FTR04. **SHOT:** TR04. **MEASURED RANGE:** 40.750–40.958. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V28 → V29/FTR04 → V30. The transition into this state is hard replace award with changing gray noise; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A32 (hard replacement; full frame; 40.750–40.750 s), A33 (procedural texture loop; gray noise; 40.750–40.958 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A32:** Clears the award payoff before the final softer question Direction/speed/path are limited to `instant cut to gray noise` because the reference shows no broader motion.
**A33:** Repeats the brief separator before the emotional tonal shift Direction/speed/path are limited to `fine random monochrome pixels change every frame` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** no certificate elements persist; full-frame luminance range and boundary. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A32 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** no certificate elements persist. **OTHER ACTIVE:** A33 starts. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A33 ALLOWED TO MOVE/CHANGE:** gray noise. **LOCKED:** full-frame luminance range and boundary. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A32: STATE REPLACEMENT—full frame is isolated from every unrelated anchor; A33: PERSISTENT LOOP—gray noise is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A32: EDITOR HARD CUT; A33: EDITOR PROCEDURAL NOISE. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A32: LOW—exact line/text registration favors the named deterministic method; A33: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A32:** isolate `full frame` over the fixed V28/F06.2 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A33:** isolate `full frame` over the fixed V29/FTR04 base; generate/change only gray noise; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A32 SOURCE FRAME STATE:** V28/F06.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V28_0039500ms.jpg). If regeneration is required, use the full standalone prompt in card V28, then apply that card’s exact text overlays before/after motion as appropriate.
**A33 SOURCE FRAME STATE:** V29/FTR04. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V29_0040792ms.jpg). If regeneration is required, use the full standalone prompt in card V29, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A32
**SOURCE STATE:** V28/F06.2  
**TARGET STATE:** V29/FTR04  
**TIMESTAMP:** 40.750–40.750  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut to gray noise  
**CAMERA:** locked  
**STATIC ANCHORS:** no certificate elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from the completed award composition to a full-frame neutral gray television-noise plate. Carry no certificate, text, icons, reader or furniture into the transition. Keep the vertical frame locked.”  
**CHARACTER COUNT:** 206 / 500  
**STATUS:** PASS
#### ANIMATION A33
**SOURCE STATE:** V29/FTR04  
**TARGET STATE:** V29/FTR04  
**TIMESTAMP:** 40.750–40.958  
**MOTION TYPE/HERO:** procedural texture loop / gray noise  
**DIRECTION, SPEED, PATH:** fine random monochrome pixels change every frame  
**CAMERA:** locked  
**STATIC ANCHORS:** full-frame luminance range and boundary  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked frame. Animate only fine neutral-gray television noise across the full 9:16 image for the observed 0.21-second bridge. Maintain even mid-gray density and introduce no lettering, objects, figures or camera motion.”  
**CHARACTER COUNT:** 219 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A32 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. A33 uses `EDITOR PROCEDURAL NOISE` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 40.958s, transition to V30. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V29 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V30 — 41.250s — Karl question card
**SHOT:** S07  
**DURATION:** 1.000 s (40.958–41.958)  
**FRAME STATE:** F07.0  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V30_0041250ms.jpg)

![V30 source frame](weird_worrying_forensics/keyframes/V30_0041250ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the Karl dehydration question occupies the top gray card above the recurring seated reader and blank white middle. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The Karl dehydration question occupies the top gray card above the recurring seated reader and blank white middle.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Karl asks, is it possible to cry so much…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Open the final question while preserving the familiar inbox grammar.  
**MOTION CUE:** hard exit from noise to dehydration question.  
**FUNCTION:** Open the final question while preserving the familiar inbox grammar.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard exit from noise to dehydration question. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Open the final question while preserving the familiar inbox grammar. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The Karl dehydration question occupies the top gray card above the recurring seated reader and blank white middle.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** question panel.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** card X 5–95/Y 6–25; reader/desk X 18–66/Y 71–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** question panel → reader.
### 7. ATTENTION ORDER
**FIRST LOOK:** question panel. **SECOND/THIRD:** reader. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V29. **CHANGES:** hard exit from noise to dehydration question.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; place a blank light-gray rounded question panel across the upper frame and the recurring faceless reader seated with device at the compact outlined desk, tilted monitor and chair low below on pure white. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Is it possible to cry so much you dehydrate yourself? — Karl Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V30. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F07.0. **SHOT:** S07. **MEASURED RANGE:** 40.958–41.958. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V29 → V30/F07.0 → V31. The transition into this state is hard exit from noise to dehydration question; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A34 (hard replacement; full frame; 40.958–40.958 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A34:** Introduces the final question after a clean attention reset Direction/speed/path are limited to `noise switches to Karl card/base reader` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** new question card and recurring reader stage. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A34 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** new question card and recurring reader stage. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A34: STATE REPLACEMENT—full frame is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A34: EDITOR HARD CUT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A34: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A34:** isolate `full frame` over the fixed V29/FTR04 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A34 SOURCE FRAME STATE:** V29/FTR04. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V29_0040792ms.jpg). If regeneration is required, use the full standalone prompt in card V29, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A34
**SOURCE STATE:** V29/FTR04  
**TARGET STATE:** V30/F07.0  
**TIMESTAMP:** 40.958–40.958  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** noise switches to Karl card/base reader  
**CAMERA:** locked  
**STATIC ANCHORS:** new question card and recurring reader stage  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from gray noise to the Karl question-card base with the recurring seated reader, desk, tilted monitor and chair low in the white vertical frame. Match the card and stage registration; no award elements remain.”  
**CHARACTER COUNT:** 218 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A34 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 41.958s, transition to V31. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V30 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V31 — 43.000s — Crying figure in tear pool
**SHOT:** S07  
**DURATION:** 3.042 s (41.958–45.000)  
**FRAME STATE:** F07.1  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V31_0043000ms.jpg)

![V31 source frame](weird_worrying_forensics/keyframes/V31_0043000ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a large thought bubble contains a drooping faceless figure standing in a shallow horizontal pool of tear marks. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** A large thought bubble contains a drooping faceless figure standing in a shallow horizontal pool of tear marks.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…that you dehydrate yourself?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Literalize excessive crying while signaling sadness rather than spectacle.  
**MOTION CUE:** add thought bubble and drooping figure standing in pooled tears.  
**FUNCTION:** Literalize excessive crying while signaling sadness rather than spectacle.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** add thought bubble and drooping figure standing in pooled tears. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Literalize excessive crying while signaling sadness rather than spectacle. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** A large thought bubble contains a drooping faceless figure standing in a shallow horizontal pool of tear marks.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** drooping figure.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** bubble X 6–94/Y 29–71; figure X 41–59/Y 37–64; tear pool X 8–91/Y 57–68. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** drooping figure → tear pool → question card.
### 7. ATTENTION ORDER
**FIRST LOOK:** drooping figure. **SECOND/THIRD:** tear pool → question card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V30. **CHANGES:** add thought bubble and drooping figure standing in pooled tears.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Karl panel and lower reader stage; add a scalloped thought bubble containing one centered drooping faceless stick figure with head bowed, standing in a shallow horizontal wavy pool filled with many short tear marks. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Is it possible to cry so much you dehydrate yourself? — Karl Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V31. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F07.1. **SHOT:** S07. **MEASURED RANGE:** 41.958–45.000. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V30 → V31/F07.1 → V32. The transition into this state is add thought bubble and drooping figure standing in pooled tears; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A35 (additive reveal; crying figure thought bubble; 41.958–41.958 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A35:** Literalizes dehydration-by-crying while shifting the joke toward concern Direction/speed/path are limited to `instant bubble, drooping figure and tear pool appearance` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** Karl card and reader-stage cluster. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A35 ALLOWED TO MOVE/CHANGE:** crying figure thought bubble. **LOCKED:** Karl card and reader-stage cluster. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A35: STATE REPLACEMENT—crying figure thought bubble is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A35: REPLACEMENT DRAWING. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A35: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A35:** isolate `X 6-94 Y 29-71` over the fixed V30/F07.0 base; generate/change only crying figure thought bubble; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A35 SOURCE FRAME STATE:** V30/F07.0. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V30_0041250ms.jpg). If regeneration is required, use the full standalone prompt in card V30, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A35
**SOURCE STATE:** V30/F07.0  
**TARGET STATE:** V31/F07.1  
**TIMESTAMP:** 41.958–41.958  
**MOTION TYPE/HERO:** additive reveal / crying figure thought bubble  
**DIRECTION, SPEED, PATH:** instant bubble, drooping figure and tear pool appearance  
**CAMERA:** locked  
**STATIC ANCHORS:** Karl card and reader-stage cluster  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Add the scalloped thought bubble containing the drooping faceless figure standing in a shallow pool of tear marks. Preserve the Karl question card, seated reader, desk, monitor, chair, scale and white background. Hold the complete crying state.”  
**CHARACTER COUNT:** 259 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A35 uses `REPLACEMENT DRAWING` in ROI X 6-94 Y 29-71; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 45.000s, transition to V32. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V31 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V32 — 45.500s — Reader says …KARL
**SHOT:** S07  
**DURATION:** 0.875 s (45.000–45.875)  
**FRAME STATE:** F07.2  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V32_0045500ms.jpg)

![V32 source frame](weird_worrying_forensics/keyframes/V32_0045500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the thought bubble disappears; the reader shifts to a slumped concerned pose and a curved speech tail leads to the hand-lettered fragment “…KARL”. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The thought bubble disappears; the reader shifts to a slumped concerned pose and a curved speech tail leads to the hand-lettered fragment “…KARL”.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘Karl…’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Pivot from hypothetical illustration to direct personal concern.  
**MOTION CUE:** remove bubble; replace seated pose and add …KARL speech.  
**FUNCTION:** Pivot from hypothetical illustration to direct personal concern.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** remove bubble; replace seated pose and add …KARL speech. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Pivot from hypothetical illustration to direct personal concern. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The thought bubble disappears; the reader shifts to a slumped concerned pose and a curved speech tail leads to the hand-lettered fragment “…KARL”.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** response zone.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** response zone X 26–50/Y 36–45; reader/desk X 17–66/Y 68–95; card X 5–95/Y 6–25. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** response zone → slumped reader → Karl card.
### 7. ATTENTION ORDER
**FIRST LOOK:** response zone. **SECOND/THIRD:** slumped reader → Karl card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V31. **CHANGES:** remove bubble; replace seated pose and add …KARL speech.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Karl question panel, desk, monitor and chair; remove the thought bubble and draw the faceless reader in the observed slumped seated pose, with a curved speech-tail line rising into a blank response zone above. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Is it possible to cry so much you dehydrate yourself? — Karl | …KARL Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V32. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F07.2. **SHOT:** S07. **MEASURED RANGE:** 45.000–45.875. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V31 → V32/F07.2 → V33. The transition into this state is remove bubble; replace seated pose and add …KARL speech; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A36 (replacement drawing + text reveal; concerned reader and …KARL; 45.000–45.000 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A36:** Moves from hypothetical imagery to direct interpersonal concern Direction/speed/path are limited to `bubble disappears; reader pose switches; short speech appears above` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** Karl card, desk, monitor, chair and white field. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A36 ALLOWED TO MOVE/CHANGE:** concerned reader and …KARL. **LOCKED:** Karl card, desk, monitor, chair and white field. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A36: SIMULTANEOUS COUPLED—concerned reader and …KARL is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A36: REPLACEMENT DRAWING + deterministic text. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A36: MEDIUM—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A36:** isolate `X 8-62 Y 34-94` over the fixed V31/F07.1 base; generate/change only concerned reader and …KARL; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A36 SOURCE FRAME STATE:** V31/F07.1. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V31_0043000ms.jpg). If regeneration is required, use the full standalone prompt in card V31, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A36
**SOURCE STATE:** V31/F07.1  
**TARGET STATE:** V32/F07.2  
**TIMESTAMP:** 45.000–45.000  
**MOTION TYPE/HERO:** replacement drawing + text reveal / concerned reader and …KARL  
**DIRECTION, SPEED, PATH:** bubble disappears; reader pose switches; short speech appears above  
**CAMERA:** locked  
**STATIC ANCHORS:** Karl card, desk, monitor, chair and white field  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Remove the thought bubble and replace only the lower reader with the observed slumped/concerned seated pose, then add the exact hand lettering “…KARL” and its curved speech tail above. Preserve the Karl question card, desk, monitor, chair, object scale and white background. Hold.”  
**CHARACTER COUNT:** 295 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A36 uses `REPLACEMENT DRAWING + deterministic text` in ROI X 8-62 Y 34-94; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 45.875s, transition to V33. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V32 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V33 — 46.500s — Reader asks if Karl is okay
**SHOT:** S07  
**DURATION:** 1.417 s (45.875–47.292)  
**FRAME STATE:** F07.3  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V33_0046500ms.jpg)

![V33 source frame](weird_worrying_forensics/keyframes/V33_0046500ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the concerned reader pose holds while the response expands to two lines: “…KARL, IS / EVERYTHING OK?”. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The concerned reader pose holds while the response expands to two lines: “…KARL, IS / EVERYTHING OK?”.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** ‘…is everything okay?’  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** Complete the empathetic final button and close the loop on Karl’s wellbeing.  
**MOTION CUE:** expand hand-lettered speech to …KARL, IS EVERYTHING OK?.  
**FUNCTION:** Complete the empathetic final button and close the loop on Karl’s wellbeing.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** expand hand-lettered speech to …KARL, IS EVERYTHING OK?. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
Complete the empathetic final button and close the loop on Karl’s wellbeing. Information value: ESSENTIAL/EXPLANATORY. Removing this state would break the visible cause, consequence or reaction step.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field.  
**MAIN SUBJECT:** The concerned reader pose holds while the response expands to two lines: “…KARL, IS / EVERYTHING OK?”.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** full response zone.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** response zone X 14–75/Y 34–48; reader/desk X 17–66/Y 68–95. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** full response zone → concerned reader → question card.
### 7. ATTENTION ORDER
**FIRST LOOK:** full response zone. **SECOND/THIRD:** concerned reader → question card. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** CLEAN/CONTROLLED.
### 8. IMAGE REUSE STATUS
**STATUS:** MODIFIED REUSE of the registered stage/base; STABLE. **BASE:** V32. **CHANGES:** expand hand-lettered speech to …KARL, IS EVERYTHING OK?.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; retain the blank Karl panel, desk, monitor, chair and slumped concerned reader with curved speech tail; enlarge the reserved blank response zone above the reader to two centered lines. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** Is it possible to cry so much you dehydrate yourself? — Karl | …KARL, IS / EVERYTHING OK? Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V33. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** F07.3. **SHOT:** S07. **MEASURED RANGE:** 45.875–47.292. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V32 → V33/F07.3 → V34. The transition into this state is expand hand-lettered speech to …KARL, IS EVERYTHING OK?; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A37 (text expansion; …KARL, IS EVERYTHING OK?; 45.875–45.875 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A37:** Completes the empathetic final button and closes the video Direction/speed/path are limited to `partial speech switches to complete two-line question` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** reader pose, Karl card, desk, chair, monitor and background. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A37 ALLOWED TO MOVE/CHANGE:** …KARL, IS EVERYTHING OK?. **LOCKED:** reader pose, Karl card, desk, chair, monitor and background. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A37: SEQUENTIAL—…KARL, IS EVERYTHING OK? is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A37: DETERMINISTIC TEXT REPLACEMENT. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A37: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A37:** isolate `X 13-75 Y 33-47` over the fixed V32/F07.2 base; generate/change only …KARL, IS EVERYTHING OK?; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A37 SOURCE FRAME STATE:** V32/F07.2. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V32_0045500ms.jpg). If regeneration is required, use the full standalone prompt in card V32, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A37
**SOURCE STATE:** V32/F07.2  
**TARGET STATE:** V33/F07.3  
**TIMESTAMP:** 45.875–45.875  
**MOTION TYPE/HERO:** text expansion / …KARL, IS EVERYTHING OK?  
**DIRECTION, SPEED, PATH:** partial speech switches to complete two-line question  
**CAMERA:** locked  
**STATIC ANCHORS:** reader pose, Karl card, desk, chair, monitor and background  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked camera. Replace only “…KARL” with the exact two-line hand lettering “…KARL, IS / EVERYTHING OK?” while retaining the same speech tail and concerned reader pose. Keep the Karl card, desk, tilted monitor, chair, frame geometry and white background fixed. Hold.”  
**CHARACTER COUNT:** 265 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A37 uses `DETERMINISTIC TEXT REPLACEMENT` in ROI X 13-75 Y 33-47; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 47.292s, transition to V34. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V33 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.

## V34 — 47.375s — Gray-noise end plate
**SHOT:** TR05  
**DURATION:** 0.210 s (47.292–47.502)  
**FRAME STATE:** FTR05  
**SOURCE REFERENCE:** [Open full-resolution frame](weird_worrying_forensics/keyframes/V34_0047375ms.jpg)

![V34 source frame](weird_worrying_forensics/keyframes/V34_0047375ms.jpg)
### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see the final composition is replaced by full-frame fine neutral-gray television noise through the file end. Background is pure white except for stated gray/noise regions; the line art is flat and frontal. **LITERAL FRAME DESCRIPTION:** The final composition is replaced by full-frame fine neutral-gray television noise through the file end.
### 2. SCRIPT ↔ VISUAL SYNC
**SPOKEN WORDS:** No verified speech; end noise after the final line.  
**VISUAL APPEARS:** DURING the cited phrase or its immediate edit beat.  
**TRIGGER IDEA:** End on the same short noise motif used between inbox entries.  
**MOTION CUE:** hard replace final scene with changing gray noise.  
**FUNCTION:** End on the same short noise motif used between inbox entries.
### 3. CHANGE FROM PREVIOUS
**ADDED/REMOVED/MOVED/REPLACED:** hard replace final scene with changing gray noise. No rotation, revolution, reframing, color shift or camera motion is observed unless explicitly named by an incoming event. **STATIC:** persistent card/reader/bubble/furniture layers remain registered.
### 4. VISUAL PURPOSE
End on the same short noise motif used between inbox entries. Information value: TRANSITIONAL. Removing this state would erase the section boundary.
### 5. CONSTRUCTION MAP
**BACKGROUND:** pure white vertical field replaced by gray noise.  
**MAIN SUBJECT:** The final composition is replaced by full-frame fine neutral-gray television noise through the file end.  
**SECONDARY:** persistent card/reader/furniture or the listed local explanatory objects.  
**GRAPHICS:** G01 question card, G02 thought bubble and/or G03 speech tail only where visible.  
**TEXT:** editor overlay listed in §11.  
**VISUAL HERO:** uniform texture.  
**STATIC COORDINATE FRAME:** 720×1280 locked canvas.  
**LAYER ORDER:** 1 white/noise field; 2 desk/card/bubble base; 3 explanatory objects/characters; 4 line effects; 5 exact text overlays.
### 6. EXACT LAYOUT
**CANVAS:** 720×1280, 9:16. **APPROXIMATE MAP:** noise X 0–100/Y 0–100. **CROP:** full-frame; no evidenced digital reframe. **MARGINS:** generous white separation between top, middle and lower modules. **DEPTH:** flat graphic planes. **PRIMARY EYE PATH:** uniform texture.
### 7. ATTENTION ORDER
**FIRST LOOK:** uniform texture. **SECOND/THIRD:** none. Contrast comes from scale, black-line density, the gray card or red thermometer—not motion outside the named event. **CONTROL:** UNIFORM.
### 8. IMAGE REUSE STATUS
**STATUS:** EXACT REUSE of E03 noise design with a new random frame; ANIMATED-TRANSITION. **BASE:** V33. **CHANGES:** hard replace final scene with changing gray noise.
### 9. IMAGE DNA
**OUTPUT TYPE:** flat raster or vector-like pen illustration. **SUBJECT/POSE:** exactly as §1. **WARDROBE/MATERIAL:** no wardrobe detail; white paper-like field, black ink lines. **ENVIRONMENT/GEOMETRY:** modular top-card/middle-bubble/lower-reader layout. **CAMERA:** locked frontal view, no lens claim. **LIGHTING:** uniform white, no modeled shadows. **COLOR:** black/white/light gray; red only where thermometer is visible. **STYLE:** deliberately irregular explanatory doodle. **TEXT/GRAPHICS:** blank clean plate plus §11 overlay.
### 10. EXACT STANDALONE IMAGE PROMPT
**STANDALONE IMAGE PROMPT:** Create a vertical 9:16 black-and-white hand-drawn explainer frame on pure white. Use thin irregular black pen outlines, flat white interiors, sparse light-gray only where specified, faceless stick figures, locked frontal composition and generous negative space; fill the full vertical frame with evenly distributed fine neutral-gray television-noise grain and no figures, text, question card, furniture, fade or directional pattern. Keep every text-bearing panel or label area blank for exact editor overlays. Preserve the measured object count, positions, relative scale and recurring reader-stage identity.
### 11. TEXT BAKE / OVERLAY DECISION
**BAKE TEXT:** NO  
**CLEAN PLATE REQUIREMENT:** generate/draw every question panel, response zone, label plate and certificate region without lettering.  
**TEXT OVERLAY SPEC:** No text in this state. Use the visible capitalization and line breaks from the source frame; black, left-aligned sans-serif in Q cards and irregular hand-lettered uppercase for punch lines/labels. If this state contains no text, add none.
### 12. FIDELITY LOCK
**CHARACTER/POSE:** preserve C01/C02/C03/C04/C05 identity and the exact pose visible in V34. **OBJECT COUNT/POSITION/SCALE:** match §1 and §6. **MAP ORIENTATION/CAMERA:** upright locked 9:16 frontal frame. **BACKGROUND/LIGHTING/COLOR:** preserve white/black/light-gray grammar and scarce red accent only where present. **TEXT/NEGATIVE SPACE:** use §11 and retain empty middle/upper zones. **PROHIBITED CHANGES:** no extra camera motion, parallax, breathing, particles, glow, shadows, facial features, line wobble, object drift or decorative animation.
### 13. IMAGE PROMPT COVERAGE AUDIT
**SUBJECT:** High. **POSE:** High or not applicable for noise. **GEOMETRY:** High. **COMPOSITION:** High. **SCALE:** High. **PERSPECTIVE:** High. **LIGHTING:** High. **COLOR:** High. **NEGATIVE SPACE:** High. **TEXT PLAN:** High. **CONTINUITY:** High. This audits prompt coverage only, not generated-image fidelity.
### 14. FRAME STATE ID
**STATE:** FTR05. **SHOT:** TR05. **MEASURED RANGE:** 47.292–47.502. **CONFIDENCE:** HIGH.
### 15. STATE-CHAIN POSITION
V33 → V34/FTR05 → file end. The transition into this state is hard replace final scene with changing gray noise; its outgoing edit is described in §27.
### 16. COMPLETE MOTION EVENT INVENTORY
Incoming/active events: A38 (hard replacement; full frame; 47.292–47.292 s), A39 (procedural texture loop; gray noise; 47.292–47.502 s). No additional motion is evidenced in this state.
### 17. WHY MOVE
**A38:** Ends the piece with the same abrasive transition motif used between inbox entries Direction/speed/path are limited to `instant cut to gray noise` because the reference shows no broader motion.
**A39:** Provides the measured 0.21-second end texture without adding a final title Direction/speed/path are limited to `fine random monochrome pixels change every frame until file end` because the reference shows no broader motion.
### 18. WHAT STAYS STATIC
**STATIC ANCHORS:** no Karl elements persist; full-frame luminance range and boundary. They remain stable for reading, comparison, continuity and attention contrast.
### 19. MOTION INTERFERENCE ANALYSIS
**A38 ALLOWED TO MOVE/CHANGE:** full frame. **LOCKED:** no Karl elements persist. **OTHER ACTIVE:** A39 starts. **DISTURBANCE RISK:** YES—use isolated masks/composite passes.
**A39 ALLOWED TO MOVE/CHANGE:** gray noise. **LOCKED:** full-frame luminance range and boundary. **OTHER ACTIVE:** none. **DISTURBANCE RISK:** NO if the specified ROI is isolated.
### 20. MOTION COUPLING CLASSIFICATION
A38: STATE REPLACEMENT—full frame is isolated from every unrelated anchor; A39: PERSISTENT LOOP—gray noise is isolated from every unrelated anchor.
### 21. RECOMMENDED PRODUCTION METHOD
A38: EDITOR HARD CUT; A39: EDITOR PROCEDURAL NOISE. Original software is not verified; these are reconstruction methods.
### 22. AI SUITABILITY
A38: LOW—exact line/text registration favors the named deterministic method; A39: LOW—exact line/text registration favors the named deterministic method.
### 23. AI ISOLATION PLAN
**A38:** isolate `full frame` over the fixed V33/F07.3 base; generate/change only full frame; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
**A39:** isolate `full frame` over the fixed V34/FTR05 base; generate/change only gray noise; mask the ROI and discard all pixels outside it. Preserve exact text as editor overlays.
### 24. SOURCE IMAGE FOR EACH AI PASS
**A38 SOURCE FRAME STATE:** V33/F07.3. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V33_0046500ms.jpg). If regeneration is required, use the full standalone prompt in card V33, then apply that card’s exact text overlays before/after motion as appropriate.
**A39 SOURCE FRAME STATE:** V34/FTR05. **TYPE:** REFERENCE FRAME / registered clean plate. **SOURCE FILE:** [open](weird_worrying_forensics/keyframes/V34_0047375ms.jpg). If regeneration is required, use the full standalone prompt in card V34, then apply that card’s exact text overlays before/after motion as appropriate.
### 25. ANIMATION PROMPT(S) ≤500 CHARACTERS
#### ANIMATION A38
**SOURCE STATE:** V33/F07.3  
**TARGET STATE:** V34/FTR05  
**TIMESTAMP:** 47.292–47.292  
**MOTION TYPE/HERO:** hard replacement / full frame  
**DIRECTION, SPEED, PATH:** instant cut to gray noise  
**CAMERA:** locked  
**STATIC ANCHORS:** no Karl elements persist  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Hard cut from the completed Karl concern composition to a full-frame neutral gray television-noise plate. Carry no question card, lettering, reader or furniture into the end plate. Keep the 9:16 frame locked.”  
**CHARACTER COUNT:** 208 / 500  
**STATUS:** PASS
#### ANIMATION A39
**SOURCE STATE:** V34/FTR05  
**TARGET STATE:** V34/FTR05  
**TIMESTAMP:** 47.292–47.502  
**MOTION TYPE/HERO:** procedural texture loop / gray noise  
**DIRECTION, SPEED, PATH:** fine random monochrome pixels change every frame until file end  
**CAMERA:** locked  
**STATIC ANCHORS:** full-frame luminance range and boundary  
**CONFIDENCE:** HIGH for occurrence/order; easing is not inferred.  
**AI PROMPT:** “Locked frame. Animate only fine neutral-gray television noise across the entire 9:16 image until the measured file end. Maintain uniform mid-gray density; add no text, shapes, figures, fade or camera motion.”  
**CHARACTER COUNT:** 207 / 500  
**STATUS:** PASS
### 26. EDITOR / COMPOSITING BUILD
Build order: registered base plate → local drawing/icon replacement → exact text overlay → optional masked loop → final hold. A38 uses `EDITOR HARD CUT` in ROI full frame; lock/matte everything listed as static. A39 uses `EDITOR PROCEDURAL NOISE` in ROI full frame; lock/matte everything listed as static. In After Effects use precomps, hold keyframes, masks/track mattes and exact text layers; Premiere/CapCut can reproduce hard cuts and overlay replacements.
### 27. EDIT OUT / NEXT STATE
At 47.502s, transition to file end. Use the next state’s manifest change exactly; do not crossfade unless the named event is a noise bridge. Persistent elements remain registered; replaced elements change on the measured boundary.
### 28. RECONSTRUCTION RULE
Rebuild V34 from its source frame and standalone prompt, apply only the events named in §§16/25, preserve the static anchors in §18, and use the exact overlay plan in §11. If an output drifts in text, line geometry, character identity, background or camera, discard the affected generative pixels and return to the registered deterministic plate.
